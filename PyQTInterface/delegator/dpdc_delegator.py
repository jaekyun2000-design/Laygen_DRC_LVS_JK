import warnings
import ast
import astunparse
import copy
import re

from PyQTInterface.delegator import delegator
from PyQTInterface import VisualizationItem
from PyCodes import variable_ast
from powertool import topAPI
import user_setup
import numpy as np

class DesignDelegator(delegator.Delegator):
    def __init__(self, main_window):
        super(DesignDelegator, self).__init__(main_window)

    def create_qt_parameter(self, dp_dict):
        """
        receive: design parameter dictionary.
        process: dp dict -> qt_dp (by qt_project's feed_design)
        request: create_vs_item,,,
        return : nothing
        """
        design_dict = self.main_window._QTObj._qtProject._feed_design(design_type='parameter', module_name= self.main_window._CurrentModuleName, dp_dict= dp_dict)
        design_dict['parameter'].update_unified_expression()
        self.create_vs_item(design_dict['parameter'])
        if design_dict['constraint']:
            self.control_constraint_tree_view(design_dict['constraint_id'])

    def create_qt_constraint(self, constraint_ast=None, constraint_dict=None):
        """
        receive: design constraint_ast or dictionary.
        process: dc info -> qt_dc (by qt_project's feed_design)
        request: if dp was created, create vs item
        return : nothing
        """
        if constraint_ast:
            design_dict = self.main_window._QTObj._qtProject._feed_design(design_type='constraint',
                                                                          module_name=self.main_window._CurrentModuleName,
                                                                          _ast=constraint_ast)
            if variable_ast.GeneratorVariable in constraint_ast.__class__.__bases__:
                constraint_ast.id = design_dict['constraint_id']
                if constraint_ast.__class__ in [variable_ast.XYCoordinate, variable_ast.PathXY, variable_ast.LogicExpression]:
                    self.main_window.calculator_window.storePreset(constraint_ast.info_dict, design_dict['constraint_id'])
            self.control_constraint_tree_view(design_dict['constraint_id'])

            if type(constraint_ast).__name__ in ['Sref', 'MacroCell']:
                gds2gen = topAPI.gds2generator.GDS2Generator(True)
                gds2gen.load_qt_project(self.main_window)

                if type(constraint_ast).__name__ == 'MacroCell':
                    dp_dict = self.main_window._QTObj._qtProject.load_designs_by_macro_ast(constraint_ast)
                    design_dict['parameter']._DesignParameter['_ModelStructure'] = dp_dict
                    design_dict['parameter'].update_unified_expression()
                else:
                    dp_from_gen = gds2gen.code_generation_for_subcell(constraint_ast)

                    if design_dict['parameter']:
                        design_dict['parameter']._DesignParameter['_DesignObj'] = dp_from_gen['_DesignObj']
                        design_dict['parameter']._DesignParameter['_ModelStructure'] = dp_from_gen['_ModelStructure']
                        design_dict['parameter'].update_unified_expression()

            if design_dict['parameter']:
                self.create_vs_item(design_dict['parameter'])
        elif constraint_dict:
            pass

    def copy_qt_constraint(self, qt_dc) -> tuple:
        """
        receive: Design Constraint
        process: source ast --> check copiable or not --> copy version of ast
        return : copy status (status type -int, and log-str)
        """
        copied_ast = copy.deepcopy(qt_dc._ast)
        ast_stack = [copied_ast]
        copy_count = 1
        while ast_stack:
            target_ast = ast_stack.pop(0)
            for field in target_ast._fields:
                if field not in target_ast.__dict__:
                    continue
                child_node = target_ast.__dict__[field]
                if type(child_node) == list:
                    child_asts = list(filter(lambda node: isinstance(node, ast.AST), child_node))
                    ast_stack.extend(child_asts)
                elif isinstance(child_node, ast.AST):
                    ast_stack.append(child_node)
                elif type(child_node) == dict:
                    child_asts = list(filter(lambda node: isinstance(node, ast.AST), child_node.values()))
                    ast_stack.extend(child_asts)
                else:
                    #debug purpose
                    print(f'check for debug: {type(child_node)}')
            copy_count += 1
            if 'name' in target_ast.__dict__:
                new_name = f'{target_ast.name}_copy'
                i=0
                while new_name in self.main_window._QTObj._qtProject._DesignParameter[self.main_window._CurrentModuleName]:
                    new_name = f'{new_name}+{i}'
                    i += 1
                target_ast.name = new_name
            self.create_qt_constraint(target_ast)



    def create_vs_item(self, qt_design_parameter):
        """
        receive: qt_design_parameter
        process: create vs item and save layer info
        request: nothing
        return : nothing
        """
        visual_item = VisualizationItem._VisualizationItem()
        visual_item._CreateFlag = False
        visual_item.updateDesignParameter(qt_design_parameter)
        visual_item.setBoundingRegionGranularity(1)
        self.main_window.visualItemDict[qt_design_parameter._ElementName] = visual_item
        visual_item.setToolTip(f'{qt_design_parameter._ElementName}\n{str(qt_design_parameter._type)}')

        self.main_window.updateGraphicItem(visual_item)
        self.main_window.dockContentWidget4ForLoggingMessage._InfoMessage("Design Parameter Created")
        layer_item = VisualizationItem._VisualizationItem().returnLayerDict()
        self.main_window._layerItem = layer_item
        self.main_window.dockContentWidget1_2.layer_table_widget.send_listInLayer_signal.connect(
            self.main_window.scene.getNonselectableLayerList)
        self.main_window.dockContentWidget1_2.layer_table_widget.updateLayerList(self.main_window._layerItem)

    def control_constraint_tree_view(self, constraint_id, channel=2, request='post' ):
        """
        receive: constraint
        \_id, channel (generator(1) or candidate(2), both(3)), request (post or delete or update)
        process: control constraint info on tree widget
        request: nothing
        return : nothing
        """
        if channel == 1:
            targets = [self.main_window.dockContentWidget3]
        elif channel == 2:
            targets = [self.main_window.dockContentWidget3_2]
        else:
            targets = [self.main_window.dockContentWidget3, self.main_window.dockContentWidget3_2]

        for target in targets:
            if request == 'post':
                target.createNewConstraintAST(_id=constraint_id, _parentName=self.main_window._CurrentModuleName,
                                              _DesignConstraint=self.main_window._QTObj._qtProject._DesignConstraint)
            elif request == 'update':
                target.update_constraint_by_id(constraint_id)

    def update_qt_parameter(self, dp_dict, element_manager_update=True):
        """
        receive: design parameter dictionary
        process: update qt_dp by dp_dict
        request: update vs item
        return : nothing
        """
        legacy_id = dp_dict['_id']
        module = self.main_window._CurrentModuleName
        
        if dp_dict['_id'] != dp_dict['_ElementName']:
            self.main_window.visualItemDict[dp_dict['_ElementName']] = self.main_window.visualItemDict.pop(dp_dict['_id'])


        for key in dp_dict:
            self.main_window._QTObj._qtProject._DesignParameter[module][legacy_id]._setDesignParameterValue(_index = key, _value= dp_dict[key])
        self.main_window._QTObj._qtProject._DesignParameter[module][legacy_id]._setDesignParameterName(dp_dict['_ElementName'])
        design_dict = self.main_window._QTObj._qtProject._update_design(design_type='parameter', module_name=self.main_window._CurrentModuleName,
                                                          dp_dict=dp_dict, id=legacy_id, element_manager_update =element_manager_update,)
        design_dict['parameter'].update_unified_expression()
        self.update_vs_item(design_dict['parameter'])

        if design_dict['constraint_id']:
            self.control_constraint_tree_view(design_dict['constraint_id'],channel=3,request='update')

    def update_qt_constraint(self, target_id, updated_ast=None, updated_dict=None, updated_variable_dict=None):
        # if updated_ast:
        #     design_dict = self.main_window._QTObj._qtProject._update_design(design_type='constraint', module_name=self.main_window._CurrentModuleName,
        #                                                                     _ast=updated_ast,)
        design_dict=None
        target_dc = self.main_window._QTObj._qtProject._DesignConstraint[self.main_window._CurrentModuleName][target_id]
        if updated_dict and not updated_ast:
            updated_ast = target_dc._ast
            for key, value in updated_dict.items():
                if key not in updated_ast.__dict__:
                    warnings.warn(f"key: {key} is not valid field for ast of {target_id} constraint.")
                updated_ast.__dict__[key] = value
        if updated_ast:
            design_dict = self.main_window._QTObj._qtProject._update_design(design_type='constraint', id=target_id,
                                                                            module_name=self.main_window._CurrentModuleName,
                                                                            _ast=updated_ast, )

        if updated_variable_dict:
            updated_ast = target_dc._ast
            from powertool import topAPI
            for key, value in updated_variable_dict.items():
                # naming_refactor.search_ast(original_name=key, changed_name=value, constraints=dict(tmp_module=dict(tmp_dc=target_dc)), dummy_constraints=None)
                for field in updated_ast._fields:
                    if type(updated_ast.__dict__[field]) == str:
                        tmp_ast = ast.parse(updated_ast.__dict__[field])
                        tf = topAPI.naming_refactor.RefactorTransformer(key,value,None)
                        tmp_ast = tf.visit(tmp_ast.body[0])
                        sentence = astunparse.unparse(tmp_ast)[1:-1]
                        updated_ast.__dict__[field] = sentence


        self.control_constraint_tree_view(target_id,channel=3,request='update')
        if design_dict and design_dict['parameter_id']:
            design_dict['parameter'].update_unified_expression()
            self.update_vs_item(design_dict['parameter'])

    def update_vs_item_dict(self, original_name, changed_name):
        if original_name in self.main_window.visualItemDict:
            self.main_window.visualItemDict[changed_name] = self.main_window.visualItemDict.pop(original_name)
        else:
            warnings.warn(f"visual item {original_name} is not exist.")

    def update_vs_item(self, qt_design_parameter):
        if qt_design_parameter is None:
            return None

        id = qt_design_parameter._id

        if id in self.main_window.visualItemDict:
            remove_item_list = self.main_window.visualItemDict[id].updateTraits(qt_design_parameter._DesignParameter)
            # for remove_item in remove_item_list:
            #     self.main_window.scene.removeItem(remove_item)
            #     self.main_window.visualItemDict[id].remove_block_from_group(remove_item)
            if remove_item_list:
                list(map(lambda remove_item: self.main_window.scene.removeItem(remove_item), remove_item_list))
                list(map(lambda remove_item: self.main_window.visualItemDict[id].remove_block_from_group(remove_item), remove_item_list))

            self.main_window.visualItemDict[id]._id = id
            self.main_window.visualItemDict[id]._ItemTraits['_id'] = id
            self.main_window.visualItemDict[id]._ItemTraits['_ElementName'] = id
            self.main_window.visualItemDict[id]._CreateFlag = False
            self.main_window.updateGraphicItem(self.main_window.visualItemDict[id])
            return self.main_window.visualItemDict[id]
        return None

    def move_vs_item(self, vs_item_list, center_xy, mouse_xy, create):
        if create:
            for vs_item in vs_item_list:
                x = mouse_xy[0] - center_xy[0]
                y = mouse_xy[1] - center_xy[1]
                if user_setup._Snap_mode == 'orthogonal':
                    if abs(x) > abs(y):
                        y = 0
                    else:
                        x = 0
                elif user_setup._Snap_mode == 'any_angle':
                    pass
                self.main_window.visualItemDict[vs_item._id].setPos(x,y)
        else:
            for vs_item in vs_item_list:
                qt_dp = copy.deepcopy(self.main_window._QTObj._qtProject._DesignParameter[self.main_window._CurrentModuleName][vs_item._id])
                dp_dict = qt_dp._DesignParameter
                if dp_dict['_DesignParametertype'] == 1 or dp_dict['_DesignParametertype'] == 3:
                    tmp_x = mouse_xy[0] - center_xy[0]
                    tmp_y = mouse_xy[1] - center_xy[1]
                    if user_setup._Snap_mode == 'orthogonal':
                        if abs(tmp_x) > abs(tmp_y):
                            x = mouse_xy[0] - center_xy[0] + dp_dict['_XYCoordinates'][0][0]
                            y = dp_dict['_XYCoordinates'][0][1]
                        else:
                            x = dp_dict['_XYCoordinates'][0][0]
                            y = mouse_xy[1] - center_xy[1] + dp_dict['_XYCoordinates'][0][1]
                    elif user_setup._Snap_mode == 'any_angle':
                        x = mouse_xy[0] - center_xy[0] + dp_dict['_XYCoordinates'][0][0]
                        y = mouse_xy[1] - center_xy[1] + dp_dict['_XYCoordinates'][0][1]
                    dp_dict['_XYCoordinates'] = [[x,y]]
                elif dp_dict['_DesignParametertype'] == 2 or dp_dict['_DesignParametertype'] == 11:
                    for i in range(len(dp_dict['_XYCoordinates'][0])):
                        tmp_x = mouse_xy[0] - center_xy[0]
                        tmp_y = mouse_xy[1] - center_xy[1]
                        if user_setup._Snap_mode == 'orthogonal':
                            if abs(tmp_x) > abs(tmp_y):
                                x = mouse_xy[0] - center_xy[0] + dp_dict['_XYCoordinates'][0][i][0]
                                y = dp_dict['_XYCoordinates'][0][i][1]
                            else:
                                x = dp_dict['_XYCoordinates'][0][i][0]
                                y = mouse_xy[1] - center_xy[1] + dp_dict['_XYCoordinates'][0][i][1]
                        elif user_setup._Snap_mode == 'any_angle':
                            x = mouse_xy[0] - center_xy[0] + dp_dict['_XYCoordinates'][0][i][0]
                            y = mouse_xy[1] - center_xy[1] + dp_dict['_XYCoordinates'][0][i][1]
                        dp_dict['_XYCoordinates'][0].pop(i)
                        dp_dict['_XYCoordinates'][0].insert(i, [x,y])

                self.main_window.visualItemDict[vs_item._id].setPos(0,0)

                self.update_qt_parameter(dp_dict)

    def copy_vs_item(self, vs_item_list, center_xy, mouse_xy, create):
        if create:
            for vs_item in vs_item_list:
                x = mouse_xy[0] - center_xy[0]
                y = mouse_xy[1] - center_xy[1]
                if user_setup._Snap_mode == 'orthogonal':
                    if abs(x) > abs(y):
                        y = 0
                    else:
                        x = 0
                elif user_setup._Snap_mode == 'any_angle':
                    pass
                vs_item.setPos(x,y)
        else:
            for vs_item in vs_item_list:
                _id = vs_item._ItemTraits['_ElementName']
                qt_dp = copy.deepcopy(self.main_window._QTObj._qtProject._DesignParameter[self.main_window._CurrentModuleName][_id])
                dp_dict = qt_dp._DesignParameter
                _id_num = ''
                for i in range(len(_id)):
                    j = -(i+1)
                    if dp_dict['_id'][j] == '_':
                        break
                    elif re.search('[0-9]', dp_dict['_id'][j]):
                        _id_num = dp_dict['_id'][j] + _id_num
                        continue
                    else:
                        break

                if j == -1:
                    _id = _id + '_'
                    _id_num = '-1'
                new_id = _id[:j] + '_' + str(int(_id_num)+1)

                while True:
                    if new_id in self.main_window._QTObj._qtProject._ElementManager.dp_id_to_dc_id:
                        _id_num = str(int(_id_num)+1)
                        new_id = _id[:j] + '_' + str(int(_id_num)+1)
                    else:
                        break

                dp_dict['_ElementName'] = new_id
                dp_dict['_id'] = new_id

                if dp_dict['_DesignParametertype'] == 1 or dp_dict['_DesignParametertype'] == 3:
                    tmp_x = mouse_xy[0] - center_xy[0]
                    tmp_y = mouse_xy[1] - center_xy[1]
                    if user_setup._Snap_mode == 'orthogonal':
                        if abs(tmp_x) > abs(tmp_y):
                            x = mouse_xy[0] - center_xy[0] + dp_dict['_XYCoordinates'][0][0]
                            y = dp_dict['_XYCoordinates'][0][1]
                        else:
                            x = dp_dict['_XYCoordinates'][0][0]
                            y = mouse_xy[1] - center_xy[1] + dp_dict['_XYCoordinates'][0][1]
                    elif user_setup._Snap_mode == 'any_angle':
                        x = mouse_xy[0] - center_xy[0] + dp_dict['_XYCoordinates'][0][0]
                        y = mouse_xy[1] - center_xy[1] + dp_dict['_XYCoordinates'][0][1]
                    dp_dict['_XYCoordinates'] = [[x,y]]
                elif dp_dict['_DesignParametertype'] == 2 or dp_dict['_DesignParametertype'] == 11:
                    tmp_xy = list()
                    for i in range(len(dp_dict['_XYCoordinates'][0])):
                        tmp_x = mouse_xy[0] - center_xy[0]
                        tmp_y = mouse_xy[1] - center_xy[1]
                        if user_setup._Snap_mode == 'orthogonal':
                            if abs(tmp_x) > abs(tmp_y):
                                x = mouse_xy[0] - center_xy[0] + dp_dict['_XYCoordinates'][0][i][0]
                                y = dp_dict['_XYCoordinates'][0][i][1]
                            else:
                                x = dp_dict['_XYCoordinates'][0][i][0]
                                y = mouse_xy[1] - center_xy[1] + dp_dict['_XYCoordinates'][0][i][1]
                        elif user_setup._Snap_mode == 'any_angle':
                            x = mouse_xy[0] - center_xy[0] + dp_dict['_XYCoordinates'][0][i][0]
                            y = mouse_xy[1] - center_xy[1] + dp_dict['_XYCoordinates'][0][i][1]
                        tmp_xy.append([x,y])
                        # dp_dict['_XYCoordinates'][0].pop(i)
                        # dp_dict['_XYCoordinates'][0].insert(i, [x,y])
                    dp_dict['_XYCoordinates'] = [tmp_xy]

                vs_item.setPos(0,0)

                self.create_qt_parameter(dp_dict)
                self.main_window.scene.removeItem(vs_item)

    def delete_qt_parameter(self, dp_name, delete_dc=True):
        dp_module = self.main_window._CurrentModuleName

        dc_id = self.main_window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id(dp_name)

        deletionItems = [self.main_window.visualItemDict[dp_name]]  # Delete Visual Item
        # for deleteItem in deletionItems:
        #     self.main_window.scene.removeItem(deleteItem)
        list(map(lambda deleteItem: self.main_window.scene.removeItem(deleteItem), deletionItems))

        del self.main_window._QTObj._qtProject._DesignParameter[dp_module][dp_name]

        if delete_dc:
            self.main_window.deleteDesignConstraint(dc_id, delete_dp=False)

    def convert_elements_to_sref(self, vis_item_list):
        # for vis in vis_item_list:
        #     if vis._id:
        #         self.delete_qt_parameter(vis._id)
        list(map(lambda vis: self.delete_qt_parameter(vis._id), list(filter(lambda vis: vis._id, vis_item_list))))

    def create_sref_by_elements(self, vis_item_dict):
        def create_new_window(tmp_module_name, vis_item_list):
            self.main_window.module_name_list.append(tmp_module_name)
            self.main_window.create_new_window(self.main_window.module_dict, tmp_module_name)
            new_project = self.main_window.module_dict[tmp_module_name]
            new_project._CurrentModuleName = tmp_module_name
            self.main_window.module_dict[tmp_module_name].set_module_name(tmp_module_name)

            for vis_item in vis_item_list:
                qt_dp = copy.deepcopy(self.main_window._QTObj._qtProject._DesignParameter[self.main_window._CurrentModuleName][vis_item._id])
                new_project.design_delegator.create_qt_parameter(qt_dp._DesignParameter)

            self.main_window.module_dict[tmp_module_name].module_dict = self.main_window.module_dict
            self.main_window.module_dict[tmp_module_name].module_name_list = self.main_window.module_name_list

            self.main_window.hide()

        create_new_window(list(vis_item_dict.items())[0][0], list(vis_item_dict.items())[0][1])

    def build_layer_matrix_by_ids(self, dp_names):
        """
        input: qt_dp_names
        output: cell type prediction result str
        """
        print(f'target_dps: {dp_names}')
        tmp_qt_dp = dict()
        # for dp_name in dp_names:
        #     tmp_qt_dp[dp_name] = copy.deepcopy(self.main_window._QTObj._qtProject._DesignParameter[self.main_window._CurrentModuleName][dp_name])
        list(map(lambda dp_name: tmp_qt_dp[dp_name], list(map(lambda tmp_dp_name: copy.deepcopy(self.main_window._QTObj._qtProject._DesignParameter[self.main_window._CurrentModuleName][tmp_dp_name]), dp_names))))
        lay_mat = topAPI.layer_to_matrix.LayerToMatrix(user_setup.matrix_x_step, user_setup.matrix_y_step, user_setup.layer_list)
        lay_mat.load_qt_parameters(tmp_qt_dp)
        cell_size = lay_mat.get_cell_size()
        return self.detect_cell(lay_mat.matrix_by_layer, cell_size)

    def build_layer_matrix_by_dps(self, qt_dp_dict):
        """
        input: dp_dictionary
        output: cell type prediction result str
        """
        lay_mat = topAPI.layer_to_matrix.LayerToMatrix(user_setup.matrix_x_step, user_setup.matrix_y_step, user_setup.layer_list)
        lay_mat.load_qt_parameters(qt_dp_dict)
        cell_size = lay_mat.get_cell_size()
        return self.detect_cell(lay_mat.matrix_by_layer, cell_size)

    def detect_cell(self, matrix_by_layer, cell_size=None):
        stacked_matrix = None
        cell_data = None
        for layer in user_setup.layer_list:
            if type(stacked_matrix) == np.ndarray:
                stacked_matrix = np.append(stacked_matrix, np.expand_dims(np.array(matrix_by_layer[layer]),2), axis=2)
            else:
                stacked_matrix = np.expand_dims(np.array(matrix_by_layer[layer]),2)
            # if type(stacked_matrix) == np.ndarray:
            #     if layer in matrix_by_layer:
            #         stacked_matrix = np.append(stacked_matrix, np.expand_dims(np.array(matrix_by_layer[layer]),2), axis=2)
            #     else:
            #         stacked_matrix = np.append(stacked_matrix, np.expand_dims(np.zeros((user_setup.matrix_x_step, user_setup.matrix_y_step)),2), axis=2)
            # else:
            #     if layer in matrix_by_layer:
            #         stacked_matrix = np.expand_dims(np.array(matrix_by_layer[layer]), 2)
            #     else:
            #         stacked_matrix = np.expand_dims(np.zeros((user_setup.matrix_x_step, user_setup.matrix_y_step)),2)

        cell_data = np.array([stacked_matrix])
        # import matplotlib.pyplot as plt
        # plt.imshow(cell_data[0, :, :, 3:6])
        # plt.show()
        # cell_data = cell_data.reshape((1, user_setup.matrix_y_step,user_setup.matrix_y_step, len(user_setup.layer_list)))
        if not topAPI.element_predictor.model:
            topAPI.element_predictor.model = topAPI.element_predictor.create_element_detector_model()
        # if 'model' not in self.__dict__:
        #     self.model = topAPI.element_predictor.create_element_detector_model()
        # result = self.model.predict(cell_data)
        result = topAPI.element_predictor.model.predict(cell_data)
        idx = np.argmax(result)

        prediction_cell_type = user_setup.data_type_list[idx-1]
        if prediction_cell_type in ['NMOSWithDummy','PMOSWithDummy']:
             self.detect_parameters_nmos_debug(cell_data, cell_size)
        return user_setup.data_type_list[idx - 1]


    def detect_parameters_nmos_debug(self, cell_data, cell_size=None):
        if not topAPI.parameter_predictor.nmos_model:
            pass
        model = topAPI.parameter_predictor.nmos_model

        results = model.predict(cell_data)
        print(results)
        print(cell_size)
        transformed_output = topAPI.parameter_predictor.transform_outputs(results, cell_size)
        print(transformed_output)




