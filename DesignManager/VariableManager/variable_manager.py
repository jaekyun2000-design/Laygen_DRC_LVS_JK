from PyCodes import variable_ast
from PyQTInterface import variableWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class VariableObj:
    def __init__(self):
        self.variable_type = None
        self.variable_id = None
        self.variable_info_dict =dict()
        self.field = None
    def get_variable_info(self):
        return self.variable_info_dict
    def update_variable_info_by_key(self,key:str,value) -> None:
        self.variable_info_dict[key] = value
    def update_variable_info(self,variable_info:dict) -> None:
        self.variable_info_dict = variable_info

class VariableArray(VariableObj):
    def __init__(self):
        super().__init__()
        self.field = ['x_space_distance','y_space_distance','XY','elements']



class Manage_DV_by_id(QObject):

    DVmanager = dict()
    send_DV_signal = pyqtSignal(list)
    send_DV2_signal = pyqtSignal(str, str, str)
    send_DV3_signal = pyqtSignal(str, list)

    def __init__(self, _id, _info, _type, _address):
        super().__init__()
        self._id = _id
        self._info = _info
        self._type = _type
        self._address = _address
        self.connect_signal()

    def connect_signal(self):
        self.vw = variableWindow._createNewDesignVariable()

        self.send_DV_signal.connect(self._address.updateList)
        self.send_DV2_signal.connect(self.vw.addDVtodict)
        self.send_DV3_signal.connect(self._address.manageElements)

        self.emit_signal()

    def emit_signal(self):
        if self._type == 'element array':
            for key in VariableArray().field:
                if self._info[key] == '':
                    pass
                else:
                    if type(self._info[key]) is str:
                        self.DVmanager[self._info[key]] = self._id
                        self.send_DV_signal.emit([self._info[key], None])
                        self.send_DV2_signal.emit(self._info[key], 'id', self._id)
                    if key == 'elements':
                        self.send_DV3_signal.emit(self._id, self._info[key])
class Variable_IDwithAST:
    def __init__(self):
        self.variableIDwithASTDict =dict()