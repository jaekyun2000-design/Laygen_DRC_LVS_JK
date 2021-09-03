from PyQTInterface.delegator import delegator
from PyQTInterface import VisualizationItem

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

    def update_qt_constraint(self):
        pass

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
