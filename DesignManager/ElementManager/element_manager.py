import ast
import re
import warnings

from PyCodes import element_ast, variable_ast
from PyCodes import ASTmodule
from PyCodes import userDefineExceptions
from PyQt5.QtCore import QObject, pyqtSignal
from PyQTInterface.layermap import LayerReader
from generatorLib import generator_model_api

class ElementMangerSignal(QObject):
    dp_name_update_signal = pyqtSignal(str, str)

class ElementManager:
    def __init__(self):
        self.elementParameterDict = dict()
        self.elementConstraintDict = dict()
        self.variable_finding_walker = element_ast.VariableNameVisitor()
        self.dp_id_to_dc_id = dict()
        self.dc_id_to_dp_id = dict()
        self.signal = ElementMangerSignal()

    def get_dpdict_return_ast(self, dp_dict):
        if dp_dict['_DesignParametertype'] == 1:    #Boundary
            tmpAST = element_ast.Boundary()
            for key in element_ast.Boundary._fields:
                if key == 'name':
                    tmpAST.__dict__[key] = dp_dict['_ElementName']
                elif key == 'layer':
                    tmpAST.__dict__[key] = dp_dict['_LayerUnifiedName']
                elif key == 'XY':
                    tmpAST.__dict__[key] = dp_dict['_XYCoordinates']
                elif key == 'width':
                    tmpAST.__dict__[key] = dp_dict['_XWidth']
                elif key == 'height':
                    tmpAST.__dict__[key] = dp_dict['_YWidth']
        elif dp_dict['_DesignParametertype'] == 11:    #Boundary
            tmpAST = element_ast.Polygon()
            for key in element_ast.Polygon._fields:
                if key == 'name':
                    tmpAST.__dict__[key] = dp_dict['_ElementName']
                elif key == 'layer':
                    tmpAST.__dict__[key] = dp_dict['_LayerUnifiedName']
                elif key == 'XY':
                    tmpAST.__dict__[key] = dp_dict['_XYCoordinates']
        elif dp_dict['_DesignParametertype'] == 2:  #Path
            tmpAST = element_ast.Path()
            for key in element_ast.Path._fields:
                if key == 'name':
                    tmpAST.__dict__[key] = dp_dict['_ElementName']
                elif key == 'layer':
                    tmpAST.__dict__[key] = dp_dict['_LayerUnifiedName']
                elif key == 'XY':
                    tmpAST.__dict__[key] = dp_dict['_XYCoordinates']
                elif key == 'width':
                    tmpAST.__dict__[key] = dp_dict['_Width']

        elif dp_dict['_DesignParametertype'] == 3:  # Sref, MacroCell
            if dp_dict['library'] == 'MacroCell':
                tmpAST = element_ast.MacroCell()
                for key in element_ast.MacroCell._fields:
                    if key == 'name':
                        tmpAST.__dict__[key] = dp_dict['_ElementName']
                    elif key == 'library':
                        tmpAST.__dict__[key] = dp_dict['library']
                    elif key == 'XY':
                        tmpAST.__dict__[key] = dp_dict["_XYCoordinates"]
            else:
                tmpAST = element_ast.Sref()
                for key in element_ast.Sref._fields:
                    if key == 'name':
                        tmpAST.__dict__[key] = dp_dict['_ElementName']
                    elif key == 'library':
                        tmpAST.__dict__[key] = dp_dict['library']
                    elif key == 'className':
                        tmpAST.__dict__[key] = dp_dict['className']
                    elif key == 'XY':
                        tmpAST.__dict__[key] = dp_dict["_XYCoordinates"]
                    elif key == 'calculate_fcn':
                        tmpAST.__dict__[key] = list(generator_model_api.class_function_dict[dp_dict['library']].keys())[0]
                    elif key == 'parameters':
                        tmpAST.__dict__[key] = dp_dict['parameters']


        elif dp_dict['_DesignParametertype'] == 'element array':  #EA
            tmpAST = variable_ast.ElementArray()
            for key in variable_ast.ElementArray._fields:
                if key == 'elements':
                    tmpAST.__dict__[key] = dp_dict['variable_info'][key]
                elif key == 'XY':
                    tmpAST.__dict__[key] = dp_dict['variable_info'][key]
                elif key == 'x_space_distance':
                    tmpAST.__dict__[key] = dp_dict['variable_info'][key]
                elif key == 'y_space_distance':
                    tmpAST.__dict__[key] = dp_dict['variable_info'][key]

        elif dp_dict['_DesignParametertype'] == 8:  #TEXT
            tmpAST = element_ast.Text()
            for key in element_ast.Text._fields:
                # if key == 'id':
                #     tmpAST.__dict__[key] = dp_dict['_id']
                if key == 'name':
                    tmpAST.__dict__[key] = dp_dict['_ElementName']
                elif key == 'layer':
                    tmpAST.__dict__[key] = dp_dict['_LayerUnifiedName']
                elif key == 'XY':
                    tmpAST.__dict__[key] = dp_dict['_XYCoordinates']
                elif key == 'pres':
                    tmpAST.__dict__[key] = dp_dict['_Presentation']
                elif key == 'reflect':
                    tmpAST.__dict__[key] = dp_dict['_Reflect']
                elif key == 'magnitude':
                    tmpAST.__dict__[key] = dp_dict['_Mag']
                elif key == 'angle':
                    tmpAST.__dict__[key] = dp_dict['_Angle']
                elif key == 'text':
                    try:
                        tmpAST.__dict__[key] = dp_dict['_TEXT'].decode()
                    except:
                        tmpAST.__dict__[key] = dp_dict['_TEXT']
        else:
            return None, None

        # self.load_dp_dc(dp=None, dc=tmpAST)
        if dp_dict['_ElementName'] in self.elementConstraintDict:
            constraint_id = self.elementConstraintDict[dp_dict['_ElementName']]._id
        else:
            constraint_id = None
        return tmpAST , constraint_id

    def discriminate_variable(self, key, ast):
        if key == '_XYCoordinates':
            key = 'XY'
        elif key == '_XWidth' or key =='_Width':
            key = 'width'
        elif key == '_YWidth':
            key = 'height'

        if '_ast' in str(type(ast.__dict__[key])):
            return True
        elif type(ast.__dict__[key]) == list:
            for sub_dp_value in ast.__dict__[key]:
                if '_ast' in str(type(sub_dp_value)):
                    return True
                if type(sub_dp_value) == str:
                    tmp_ast = ast.parse(sub_dp_value)
                    self.variable_finding_walker.visit(tmp_ast)
                    if self.variable_finding_walker.variable_name_list:
                        self.variable_finding_walker.variable_name_list = []
                        return True
            return False


    def get_ast_return_dpdict(self, ast, dummy=None):
        if ASTmodule._getASTtype(ast) == 'Boundary':
            tmpDP = dict()
            for key in KeyManager._Boundarykey.keys():
                #Invalid case -> not return (like variable expression)
                #DP only accept determinstic data
                if key in ['_XYCoordinates', '_XWidth', '_YWidth']:
                    if self.discriminate_variable(key,ast):
                        return None, None
                if key == '_LayerUnifiedName':
                    tmpDP[key] = ast.__dict__['layer']
                elif key == '_DesignParametertype':
                    tmpDP[key] = 1
                elif key == '_XYCoordinates':
                    contain_variable = False
                    if type(ast.XY) == list:
                        for idx in range(len(ast.XY)):
                            if re.search('[^0-9-.]', str(ast.XY[idx][0])) is not None or re.search('[^0-9-.]', str(ast.XY[idx][1])) is not None:
                                contain_variable = True
                        if not contain_variable:
                            tmpDP[key] = ast.XY
                    # tmpDP[key] = ast.XY
                elif key == '_XWidth':
                    if re.search('[^0-9-.]', str(ast.__dict__['width'])) is None:
                        tmpDP[key] = ast.__dict__['width']
                    # tmpDP[key] = ast.__dict__['width']
                elif key == '_YWidth':
                    if re.search('[^0-9-.]', str(ast.__dict__['height'])) is None:
                        tmpDP[key] = ast.__dict__['height']
                    # tmpDP[key] = ast.__dict__['height']
                elif key == '_Ignore':
                    tmpDP[key] = None
                elif key == '_ElementName':
                    tmpDP[key] = ast.__dict__['name']
        elif ASTmodule._getASTtype(ast) == 'Polygon':
            tmpDP = dict()
            for key in KeyManager._Boundarykey.keys():
                #Invalid case -> not return (like variable expression)
                #DP only accept determinstic data
                if key in ['_XYCoordinates']:
                    if self.discriminate_variable(key,ast):
                        return None, None
                if key == '_LayerUnifiedName':
                    tmpDP[key] = ast.__dict__['layer']
                elif key == '_DesignParametertype':
                    tmpDP[key] = 11
                elif key == '_XYCoordinates':
                    contain_variable = False
                    if type(ast.XY) == list:
                        for idx in range(len(ast.XY)):
                            if re.search('[^0-9-.]', str(ast.XY[idx][0])) is not None or re.search('[^0-9-.]', str(ast.XY[idx][1])) is not None:
                                contain_variable = True
                        if not contain_variable:
                            tmpDP[key] = ast.XY
                    # tmpDP[key] = ast.XY
                elif key == '_Ignore':
                    tmpDP[key] = None
                elif key == '_ElementName':
                    tmpDP[key] = ast.__dict__['name']

        elif ASTmodule._getASTtype(ast) == 'Path':
            tmpDP = dict()
            for key in KeyManager._Pathkey.keys():
                if key in ['_XYCoordinates', '_Width']:
                    if self.discriminate_variable(key,ast):
                        return None, None

                if key == '_ElementName':
                    tmpDP[key] = ast.__dict__['name']
                elif key == '_LayerUnifiedName':
                    tmpDP[key] = ast.__dict__['layer']
                elif key == '_DesignParametertype':
                    tmpDP[key] = 2
                elif key == '_XYCoordinates':
                    contain_variable = False
                    if type(ast.XY) == list:
                        for i in range(len(ast.__dict__['XY'])):
                            for j in range(len(ast.__dict__['XY'][i])):
                                if re.search('[^0-9-.]', str(ast.__dict__['XY'][i][j][0])) is not None or re.search('[^0-9-.]', str(ast.__dict__['XY'][i][j][1])) is not None:
                                    contain_variable = True
                        if not contain_variable:
                            tmpDP[key] = ast.__dict__['XY']
                    # tmpDP[key] = ast.__dict__['XY']
                elif key == '_Width':
                    if re.search('[^0-9-.]', str(ast.__dict__['width'])) is None:
                        tmpDP[key] = ast.__dict__['width']
                    # tmpDP[key] = ast.__dict__['width']
                elif key == '_Color':
                    tmpDP[key] = None
                elif key == '_ItemRef':
                    tmpDP[key] = None

        elif ASTmodule._getASTtype(ast) == 'Sref':
            tmpDP = dict()
            for key in ast._fields:
                if key in ['XY']:
                    if self.discriminate_variable(key,ast):
                        return None, None

                if key == 'name':
                    tmpDP['_ElementName'] = ast.__dict__['name']
                    # tmpDP[key] = ast.__dict__['name']
                elif key == 'library':
                    tmpDP[key] = ast.__dict__['library']
                elif key == 'className':
                    tmpDP[key] = ast.__dict__['className']
                elif key == 'XY':
                    contain_variable = False
                    if type(ast.__dict__['XY']) == list:
                        for idx in range(len(ast.__dict__['XY'])):
                            if re.search('[^0-9-.]', str(ast.__dict__['XY'][idx][0])) is not None or re.search('[^0-9-.]', str(ast.__dict__['XY'][idx][1])) is not None:
                                contain_variable = True
                        if not contain_variable:
                            tmpDP['_XYCoordinates'] = ast.__dict__['XY']
                    # tmpDP['_XYCoordinates'] = ast.__dict__['XY']
                elif key == 'calculate_fcn':
                    tmpDP[key] = ast.__dict__['calculate_fcn']
                elif key == 'parameters':
                    tmpDP[key] = ast.__dict__['parameters']
            tmpDP['_DesignParametertype'] = 3

        elif ASTmodule._getASTtype(ast) == 'Text':
            # 'id',  # name str
            # 'layer',  # layer name str
            # 'pres'  # list [a,a,a]
            # 'reflect',  # list [a,a,a]
            # 'XY',  # double list or variable name str
            # 'magnitude',  # float
            # 'angle',  # float
            # 'text'  # int or str
            tmpDP = dict()
            for key in KeyManager._Textkey.keys():
                if key in ['_XYCoordinates']:
                    if self.discriminate_variable(key,ast):
                        return None, None

                if key == '_id':
                    tmpDP[key] = ast.__dict__['id']
                elif key == '_DesignParameterType':
                    tmpDP[key] = 8
                elif key == '_ElementName':
                    tmpDP[key] = ast.__dict__['name']
                elif key == '_LayerUnifiedName':
                    tmpDP[key] = ast.__dict__['layer']
                elif key == '_Presentation':
                    tmpDP[key] = ast.__dict__['pres']
                elif key == '_Reflect':
                    tmpDP[key] = ast.__dict__['reflect']
                elif key == '_XYCoordinates':
                    tmpDP[key] = ast.__dict__['XY']
                elif key == '_Mag':
                    tmpDP[key] = ast.__dict__['magnitude']
                elif key == '_Angle':
                    tmpDP[key] = ast.__dict__['angle']
                elif key == '_TEXT':
                    tmpDP[key] = ast.__dict__['text']
                elif key == '_Ignore':
                    tmpDP[key] = None
                elif key == '_ElementName':
                    tmpDP[key] = None
        elif ASTmodule._getASTtype(ast) == 'Array':
            tmpDP = dict()
            for key, value in dummy.items():
                if key == 'name':
                    tmpDP[key] = value
                elif key == 'layer':
                    tmpDP['_LayerUnifiedName'] = value
                elif '_input' in key:
                    dp_key = key.split('_')[0]
                    try:
                        tmpDP[dp_key] = int(value)
                    except:
                        warnings.warn(f'{dp_key} is not numeric value.')
                        warnings.warn('Static value update is impossible.')
            return tmpDP

        else:
            return None

        # self.load_dp_dc(dp=tmpDP, dc=None)

        if ast.__dict__['name'] in self.elementParameterDict:
            parameter_id = self.elementParameterDict[ast.__dict__['name']]._id
        else:
            parameter_id = None


        return tmpDP, parameter_id

    def get_dp_return_dpdict(self,_qtdp):
        """
        _qtdp._id = _id # string
        _qtdp._type = _type  # int, boundary-1, path-2, sref-3
        _qtdp._ParentName = _ParentName # string
        _qtdp._ElementName = _ElementName #string
        _qtdp._DesignParameter = None
        :param _qtdp: input qt_designParameter object
        :return: design parameter dictionary format
        """
        tmpDP = dict()
        if _qtdp._type == None:
            return userDefineExceptions._NoneValueError

        for key in _qtdp._DeisngParameter:
            tmpDP[key] = _qtdp._DesignParameter[key]
        return tmpDP

    def get_dp_return_ast(self,_qtdp):
        """
        _qtdp._id = _id # string
        _qtdp._type = _type  # int, boundary-1, path-2, sref-3
        _qtdp._ParentName = _ParentName # string
        _qtdp._ElementName = _ElementName #string
        _qtdp._DesignParameter = None
        :param _qtdp: input qt_designParameter object
        :return: design constraint ast format
        """
        tmpAST, _ = self.get_dpdict_return_ast(_qtdp._DesignParameter)
        return tmpAST


    def get_dc_return_dpdict(self,_qtdc):
        return userDefineExceptions._NotImplementError

    def get_dc_return_ast(self,_qtdc):
        return userDefineExceptions._NotImplementError

    def load_dp_dc(self,dp,dc):

        self.elementParameterDict[dp._ElementName] = dp
        self.elementConstraintDict[dc._ast.name] = dc

    def load_dp_dc_id(self,dp_id, dc_id):
        self.dc_id_to_dp_id[dc_id] = dp_id
        self.dp_id_to_dc_id[dp_id] = dc_id

    def get_dc_id_by_dp_id(self,dp_id):
        if dp_id in self.dp_id_to_dc_id:
            return self.dp_id_to_dc_id[dp_id]
        else:
            return None

    def get_dp_id_by_dc_id(self,dc_id):
        if dc_id in self.dc_id_to_dp_id:
            return self.dc_id_to_dp_id[dc_id]
        else:
            return None

    def change_dp_id(self,original_id, changed_id):
        dc_id = self.dp_id_to_dc_id[original_id]
        if dc_id:
            self.dp_id_to_dc_id[changed_id] = self.dp_id_to_dc_id.pop(original_id)
            self.dc_id_to_dp_id[dc_id] = changed_id
        self.signal.dp_name_update_signal.emit(original_id, changed_id)

class KeyManager():
    _Boundarykey = dict(
        _LayerUnifiedName=None,
        _DesignParametertype=1,
        _XYCoordinates=[],
        _XWidth=None,
        _YWidth=None,
        _Ignore=None,
        _ElementName=None
        )

    _Pathkey = dict(
        _ElementName=None,
        _LayerUnifiedName=None,
        _DesignParametertype=2,
        _XYCoordinates=[],
        _Width=None,
        _Height=None,
        _Color=None,
        _ItemRef=None
        )

    _SRefkey = dict(
        _id = None,
        _DesignParametertype = 3,
        _DesignObj = None,
        _DesignLibraryName = None,
        _className = None,
        _Parameters = None,
        _XYCoordinates = [],
        _Reflect = None,
        _Angle = None,
        _Ignore = None,
        _ElementName = None
        )

    _Textkey = dict(
        _id=None,
        _DesignParameterType=8,
        _LayerUnifiedName=None,
        _Presentation=None,
        _Reflect=None,
        _XYCoordinates=[],
        _Mag=None,
        _Angle=None,
        _TEXT=None,
        _Ignore=None,
        _ElementName=None
        )




# if __name__ == '__main__':
#     a = ElementManager()
#     # x = {'_Layer': 'PIMP', '_DesignParametertype': 1, '_XYCoordinates': [[0, 0]], '_XWidth': 100.0, '_YWidth': 100.0, '_Ignore': None, '_ElementName': 'qwe'}    # DP Boundary sample
#     x = {'_ElementName': 'qwe', '_Layer': 'PIMP', '_DesignParametertype': 2, '_XYCoordinates': [[-445, 233], [33, 233], [33, -8]], '_Width': 100.0, '_Height': None, '_Color': None, '_ItemRef':None}  # DP Path sample
#     # _ast = element_ast.Boundary()
#     # _ast.__dict__ = dict(name='qwe', layer='PIMP', width=100.0, height=100.0, XY=[[0,0]]) # DC Boundary sample
#     _ast = element_ast.Path()
#     _ast.__dict__ = dict(name='qwe',layer='PIMP',XY=[[-445, 233], [33, 233], [33, -8]],width=100) # DC Path sample
#
#     a.get_dpdict_return_ast(x)
#     a.get_ast_return_dpdict(_ast)
