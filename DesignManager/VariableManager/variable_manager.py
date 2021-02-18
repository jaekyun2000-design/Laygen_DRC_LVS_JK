from PyCodes import variable_ast

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
        # super().__init__(self)
        self.field = ['x_space_distance','y_space_distance','XY','elements']



class Manage_DV_by_id():

    DVmanager = dict()

    def __init__(self, _id, _info, _type):
        self._id = _id
        self._info = _info
        self._type = _type
        self.print()

    def print(self):
        if self._type == 'element array':
            for key in VariableArray().field:
                if type(self._info[key]) is str:
                    self.DVmanager[self._info[key]] = self._id

        print(self.DVmanager)