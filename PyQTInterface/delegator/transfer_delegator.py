import warnings

from PyQTInterface.delegator import delegator
from PyQTInterface.delegator import dpdc_delegator

class TransferDelegator(delegator.Delegator):
    def __init__(self, main_window):
        super(TransferDelegator, self).__init__(main_window)
        self.main_window = main_window

    def change_used_variable_name(self, _original_id, _new_id, _id_list):
        _tmp_dict = dict()
        _tmp_dict[_original_id] = _new_id
        for _id in _id_list:
            _target_id = self.main_window._QTObj._qtProject._ElementManager.dp_id_to_dc_id[_id]
            dpdc_delegator.DesignDelegator(self.main_window).update_qt_constraint(target_id=_target_id, updated_variable_dict=_tmp_dict)

