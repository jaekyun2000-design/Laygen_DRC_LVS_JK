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
            self.add_constraint_to_treeview(design_dict['constraint_id'])

    def create_qt_constraint(self, constraint_ast=None, constraint_dict=None):
        """
        receive: design constraint_ast or dictionary.
        process: dc info -> qt_dc (by qt_project's feed_design)
        request:
        return : nothing
        """
        pass

    def create_vs_item(self, qt_design_parameter):
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

    def add_constraint_to_treeview(self, constraint_id):
        self.main_window.dockContentWidget3_2.createNewConstraintAST(_id=constraint_id,
                                                                     _parentName=self.main_window._CurrentModuleName,
                                                                     _DesignConstraint=self.main_window._QTObj._qtProject._DesignConstraint)
