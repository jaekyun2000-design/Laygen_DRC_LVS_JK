import warnings
import copy

from PyQTInterface import VisualizationItem

from PyQTInterface.delegator import delegator
from PyQTInterface.delegator import dpdc_delegator

class TransferDelegator(delegator.Delegator):
    def __init__(self, main_window):
        super(TransferDelegator, self).__init__(main_window)
        self.main_window = main_window
        self.vs_item_list = []

    def change_used_variable_name(self, _original_id, _new_id, _id_list):
        _tmp_dict = dict()
        _tmp_dict[_original_id] = _new_id
        for _id in _id_list:
            _target_id = self.main_window._QTObj._qtProject._ElementManager.dp_id_to_dc_id[_id]
            dpdc_delegator.DesignDelegator(self.main_window).update_qt_constraint(target_id=_target_id, updated_variable_dict=_tmp_dict)

    def get_xy_difference(self, vs_item_list, center, purpose):
        if purpose == 'move':
            self.vs_item_list = vs_item_list
        elif purpose == 'copy':
            self.vs_item_list = list()
            for vs_item in vs_item_list:
                tmp_vs_item = VisualizationItem._VisualizationItem(
                    self.main_window.visualItemDict[vs_item._id]._ItemTraits)
                self.vs_item_list.append(tmp_vs_item)
                self.main_window.scene.addItem(tmp_vs_item)
        self.center = center
        self.purpose = purpose

    def get_mouse_point(self, xy):
        if self.vs_item_list != []:
            if self.purpose == 'move':
                self.main_window.design_delegator.move_vs_item(self.vs_item_list, self.center, xy, True)
            elif self.purpose == 'copy':
                self.main_window.design_delegator.copy_vs_item(self.vs_item_list, self.center, xy, True)

    def get_click_point(self, xy):
        if self.vs_item_list != []:
            if self.purpose == 'move':
                self.main_window.design_delegator.move_vs_item(self.vs_item_list, self.center, xy, False)
            elif self.purpose == 'copy':
                self.main_window.design_delegator.copy_vs_item(self.vs_item_list, self.center, xy, False)
            self.vs_item_list = []