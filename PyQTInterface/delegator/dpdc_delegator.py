import warnings
import ast
import astunparse
import copy

from PyQTInterface.delegator import delegator
from PyQTInterface import VisualizationItem
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
                                                                          odule_name= self.main_window._CurrentModuleName,
                                                                          _ast=constraint_ast)
            self.control_constraint_tree_view(design_dict['constraint_id'])
            if design_dict['parameter']:
                self.create_vs_item(design_dict['parameter'])
        elif constraint_dict:
            pass

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
        visual_item.setToolTip(qt_design_parameter._ElementName + '\n' + str(qt_design_parameter._type))

        self.main_window.updateGraphicItem(visual_item)
        self.main_window.dockContentWidget4ForLoggingMessage._InfoMessage("Design Parameter Created")
        layer_item = VisualizationItem._VisualizationItem().returnLayerDict()
        self.main_window._layerItem = layer_item
        self.main_window.dockContentWidget1_2.layer_table_widget.send_listInLayer_signal.connect(
            self.main_window.scene.getNonselectableLayerList)
        self.main_window.dockContentWidget1_2.layer_table_widget.updateLayerList(self.main_window._layerItem)

    def control_constraint_tree_view(self, constraint_id, channel=2, request='post' ):
        """
        receive: constraint_id, channel (generator(1) or candidate(2), both(3)), request (post or delete or update)
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
            self.main_window._QTObj._qtProject.dp_dict[module][legacy_id]._setDesignParameterValue(_index = key, _value= dp_dict[key])
        self.main_window._QTObj._qtProject.dp_dict[module][legacy_id]._setDesignParameterName(dp_dict['_ElementName'])
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
            for key, value in updated_dict:
                if key not in updated_ast:
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


    def update_vs_item(self, qt_design_parameter):
        if qt_design_parameter is None:
            return None

        id = qt_design_parameter._id

        if id in self.main_window.visualItemDict:
            self.main_window.visualItemDict[id].updateTraits(qt_design_parameter._DesignParameter)
            self.main_window.visualItemDict[id]._id = id
            self.main_window.visualItemDict[id]._ItemTraits['_id'] = id
            self.main_window.visualItemDict[id]._ItemTraits['_ElementName'] = id
            self.main_window.updateGraphicItem(self.main_window.visualItemDict[id])
            return self.main_window.visualItemDict[id]
        return None

    def delete_qt_parameter(self, dp_name, delete_dc=True):
        dp_module = self.main_window._CurrentModuleName

        dc_id = self.main_window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id(dp_name)

        deletionItems = [self.main_window.visualItemDict[dp_name]]  # Delete Visual Item
        for deleteItem in deletionItems:
            self.main_window.scene.removeItem(deleteItem)

        del self.main_window._QTObj._qtProject._DesignParameter[dp_module][dp_name]

        if delete_dc:
            self.main_window.deleteDesignConstraint(dc_id, delete_dp=False)

    def convert_elements_to_sref(self, vis_item_list):
        for vis in vis_item_list:
            if vis._id:
                self.delete_qt_parameter(vis._id)

    def create_sref_by_elements(self, vis_item_dict):
        for key, value in vis_item_dict.items():
            tmp_module_name = key
            vis_item_list = value

        def create_new_window(tmp_module_name, vis_item_list):
            self.main_window.module_name_list.append(tmp_module_name)
            self.main_window.create_new_window(self.main_window.module_dict, tmp_module_name)
            new_project = self.main_window.module_dict[tmp_module_name]

            for vis_item in vis_item_list:
                qt_dp = copy.deepcopy(self.main_window._QTObj._qtProject._DesignParameter[self.main_window._CurrentModuleName][vis_item._id])
                new_project.design_delegator.create_vs_item(qt_dp)

            self.main_window.module_dict[tmp_module_name].set_module_name(tmp_module_name)
            self.main_window.module_dict[tmp_module_name].module_dict = self.main_window.module_dict
            self.main_window.module_dict[tmp_module_name].module_name_list = self.main_window.module_name_list
            self.main_window.hide()

        create_new_window(tmp_module_name, vis_item_list)

    def build_layer_matrix_by_ids(self, dp_names):
        """
        input: qt_dp_names
        output: cell type prediction result str
        """
        print(f'target_dps: {dp_names}')
        tmp_qt_dp = dict()
        for dp_name in dp_names:
            tmp_qt_dp[dp_name] = copy.deepcopy(self.main_window._QTObj._qtProject._DesignParameter[self.main_window._CurrentModuleName][dp_name])
        lay_mat = topAPI.layer_to_matrix.LayerToMatrix(user_setup.matrix_x_step, user_setup.matrix_y_step)
        lay_mat.load_qt_parameters(tmp_qt_dp)
        return self.detect_cell(lay_mat.matrix_by_layer)

    def build_layer_matrix_by_dps(self, qt_dp_dict):
        """
        input: dp_dictionary
        output: cell type prediction result str
        """
        lay_mat = topAPI.layer_to_matrix.LayerToMatrix(user_setup.matrix_x_step, user_setup.matrix_y_step)
        lay_mat.load_qt_parameters(qt_dp_dict)
        return self.detect_cell(lay_mat.matrix_by_layer)

    def detect_cell(self, matrix_by_layer):
        stacked_matrix = None
        cell_data = None
        for layer in user_setup.layer_list:
            if type(stacked_matrix) == np.ndarray:
                if layer in matrix_by_layer:
                    stacked_matrix = np.append(stacked_matrix, [matrix_by_layer[layer]], axis=0)
                else:
                    stacked_matrix = np.append(stacked_matrix, [np.zeros((user_setup.matrix_x_step, user_setup.matrix_y_step))], axis=0)
            else:
                if layer in matrix_by_layer:
                    stacked_matrix = np.array([matrix_by_layer[layer]])
                else:
                    stacked_matrix = np.array([np.zeros((user_setup.matrix_x_step, user_setup.matrix_y_step))])

            cell_data = np.array([stacked_matrix])
        cell_data = cell_data.reshape((1, user_setup.matrix_y_step,user_setup.matrix_y_step, len(user_setup.layer_list)))
        if not topAPI.element_predictor.model:
            topAPI.element_predictor.model = topAPI.element_predictor.create_element_detector_model()
        # if 'model' not in self.__dict__:
        #     self.model = topAPI.element_predictor.create_element_detector_model()
        # result = self.model.predict(cell_data)
        result = topAPI.element_predictor.model.predict(cell_data)
        idx = np.argmax(result)

        return user_setup.data_type_list[idx-1]





