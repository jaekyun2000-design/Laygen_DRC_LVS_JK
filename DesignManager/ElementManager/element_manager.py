from PyCodes import element_ast, variable_ast
from PyCodes import ASTmodule
from PyCodes import userDefineExceptions

class ElementManager:
    def __init__(self):
        self.elementParameterDict = dict()
        self.elementConstraintDict = dict()

        self.dp_id_to_dc_id = dict()
        self.dc_id_to_dp_id = dict()

    def get_dpdict_return_ast(self, dp_dict):
        if dp_dict['_DesignParametertype'] == 1:    #Boundary
            tmpAST = element_ast.Boundary()
            for key in element_ast.Boundary._fields:
                if key == 'name':
                    tmpAST.__dict__[key] = dp_dict['_DesignParameterName']
                elif key == 'layer':
                    tmpAST.__dict__[key] = dp_dict['_Layer']
                elif key == 'XY':
                    tmpAST.__dict__[key] = dp_dict['_XYCoordinates']
                elif key == 'width':
                    tmpAST.__dict__[key] = dp_dict['_XWidth']
                elif key == 'height':
                    tmpAST.__dict__[key] = dp_dict['_YWidth']

        elif dp_dict['_DesignParametertype'] == 2:  #Path
            tmpAST = element_ast.Path()
            for key in element_ast.Path._fields:
                if key == 'name':
                    tmpAST.__dict__[key] = dp_dict['_DesignParameterName']
                elif key == 'layer':
                    tmpAST.__dict__[key] = dp_dict['_Layer']
                elif key == 'XY':
                    tmpAST.__dict__[key] = dp_dict['_XYCoordinates']
                elif key == 'width':
                    tmpAST.__dict__[key] = dp_dict['_Width']

        elif dp_dict['_DesignParametertype'] == 3:  #Sref
            # tmpAST = element_ast.Sref()
            # for key in element_ast.Sref._fields:
            #     if key == 'name':
            #         tmpAST.__dict__[key] = dp_dict['_DesignParameterName']
            #     elif key == 'base':
            #         tmpAST.__dict__[key] = dp_dict['_DesignObj']
            #     elif key == 'XY':
            #         tmpAST.__dict__[key] = dp_dict["_XYCoordinates"]  #Not complete
            return None, None


        # elif dp_dict['_DesignParametertype'] == 8:  #TEXT
        #     #todo Text type support
        #     pass
        #     return None, None
            # tmpAST = element_ast.Sref()
            # for key in element_ast.Sref._fields:
            #     if key == 'name':
            #         tmpAST.__dict__[key] = dp_dict['_DesignParameterName']
            #     elif key == 'base':
            #         tmpAST.__dict__[key] = dp_dict['_DesignObj']
            #     elif key == 'XY':
            #         tmpAST.__dict__[key] = dp_dict["_XYCoordinates"]  #Not complete

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
            # print(dp_dict)
            # 'id',  # name str
            # 'layer',  # layer name str
            # 'pres'  # list [a,a,a]
            # 'reflect',  # list [a,a,a]
            # 'XY',  # double list or variable name str
            # 'magnitude',  # float
            # 'angle',  # float
            # 'text'  # int or str
            tmpAST = element_ast.Text()
            for key in element_ast.Text._fields:
                if key == 'id':
                    tmpAST.__dict__[key] = dp_dict['_id']
                elif key == 'name':
                    tmpAST.__dict__[key] = dp_dict['_DesignParameterName']
                elif key == 'layer':
                    tmpAST.__dict__[key] = dp_dict['_Layer']
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
                    tmpAST.__dict__[key] = dp_dict['_TEXT'].decode()

        # elif dp_dict['_DesignParametertype'] == 'variable':     # Variable dict
        #     tmpAST = variable_ast.ArgumentVariable()
        #     for key in variable_ast.ArgumentVariable._fields:
        #         if key == 'name':
        #             tmpAST.__dict__[key] = dp_dict['name']
        #         elif key == 'value':
        #             tmpAST.__dict__[key] = dp_dict['value']

        else:
            return None, None

        # self.load_dp_dc(dp=None, dc=tmpAST)
        if dp_dict['_DesignParameterName'] in self.elementConstraintDict:
            constraint_id = self.elementConstraintDict[dp_dict['_DesignParameterName']]._id
        else:
            constraint_id = None

        return tmpAST , constraint_id

    # def get_dp_return_ast(self, _qtdp):
        # if dp._type == 1:
        #     dp.
        # elif dp._type == 2:
        #
        # elif dp._type == 3:

    def get_ast_return_dpdict(self, ast):
        if ASTmodule._getASTtype(ast) == 'Boundary':
            tmpDP = dict()
            for key in KeyManager._Boundarykey.keys():
                if key == '_Layer':
                    tmpDP[key] = ast.__dict__['layer']
                elif key == '_DesignParametertype':
                    tmpDP[key] = 1
                elif key == '_XYCoordinates':
                    tmpDP[key] = ast.XY
                    #
                    # for i in range (0,len(ast.XY)):
                    #     slicing = ast.__dict__['XY'][i].find(',')
                    #     tmpDP[key] = [[float(ast.__dict__['XY'][i][:slicing]),float(ast.__dict__['XY'][i][slicing+1:])]]
                    # for i in range (0,len(ast.XY)):
                    #     slicing = ast.__dict__['XY'].find(',')
                    #     tmpDP[key] = [[float(ast.__dict__['XY'][:slicing]),float(ast.__dict__['XY'][slicing+1:])]]
                elif key == '_XWidth':
                    tmpDP[key] = ast.__dict__['width']
                elif key == '_YWidth':
                    tmpDP[key] = ast.__dict__['height']
                elif key == '_Ignore':
                    tmpDP[key] = None
                elif key == '_DesignParameterName':
                    tmpDP[key] = ast.__dict__['name']

        elif ASTmodule._getASTtype(ast) == 'Path':
            tmpDP = dict()
            for key in KeyManager._Pathkey.keys():
                if key == '_DesignParameterName':
                    tmpDP[key] = ast.__dict__['name']
                elif key == '_Layer':
                    tmpDP[key] = ast.__dict__['layer']
                elif key == '_DesignParametertype':
                    tmpDP[key] = 2
                elif key == '_XYCoordinates':
                    tmpDP[key] = ast.__dict__['XY']
                elif key == '_Width':
                    tmpDP[key] = ast.__dict__['width']
                elif key == '_Height':
                    tmpDP[key] = None
                elif key == '_Color':
                    tmpDP[key] = None
                elif key == '_ItemRef':
                    tmpDP[key] = None

        elif ASTmodule._getASTtype(ast) == 'Sref':
            # tmpDP = ast.__dict__
            pass

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
                if key == '_id':
                    tmpDP[key] = ast.__dict__['id']
                elif key == '_DesignParameterType':
                    tmpDP[key] = 8
                elif key == '_DesignParameterName':
                    tmpDP[key] = ast.__dict__['name']
                elif key == '_Layer':
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
        _qtdp._DesignParameterName = _DesignParameterName #string
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
        _qtdp._DesignParameterName = _DesignParameterName #string
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

        self.elementParameterDict[dp._DesignParameterName] = dp
        self.elementConstraintDict[dc._ast.name] = dc

    def load_dp_dc_id(self,dp_id, dc_id):
        self.dc_id_to_dp_id[dc_id] = dp_id
        self.dp_id_to_dc_id[dp_id] = dc_id

    def get_dc_id_by_dp_id(self,dp_id):
        return self.dp_id_to_dc_id[dp_id]

    def get_dp_id_by_dc_id(self,dc_id):
        return self.dc_id_to_dp_id[dc_id]


class KeyManager():
    _Boundarykey = dict(
        _Layer=None,
        _DesignParametertype=1,
        _XYCoordinates=[],
        _XWidth=None,
        _YWidth=None,
        _Ignore=None,
        _DesignParameterName=None
        )

    _Pathkey = dict(
        _DesignParameterName=None,
        _Layer=None,
        _DesignParametertype=2,
        _XYCoordinates=[],
        _Width=None,
        _Height=None,
        _Color=None,
        _ItemRef=None
        )

    _SRefkey = dict(
        _Name=None,
        _DataType="SRef",
        _XYCoordinates=[],
        _ItemRef=None
        )

    _Textkey = dict(
        _id=None,
        _DesignParameterType=8,
        _Layer=None,
        _Presentation=None,
        _Reflect=None,
        _XYCoordinates=[],
        _Mag=None,
        _Angle=None,
        _TEXT=None,
        _Ignore=None,
        _ElementName=None,
        _DesignParameterName=None
        )

# if __name__ == '__main__':
#     a = ElementManager()
#     # x = {'_Layer': 'PIMP', '_DesignParametertype': 1, '_XYCoordinates': [[0, 0]], '_XWidth': 100.0, '_YWidth': 100.0, '_Ignore': None, '_DesignParameterName': 'qwe'}    # DP Boundary sample
#     x = {'_DesignParameterName': 'qwe', '_Layer': 'PIMP', '_DesignParametertype': 2, '_XYCoordinates': [[-445, 233], [33, 233], [33, -8]], '_Width': 100.0, '_Height': None, '_Color': None, '_ItemRef':None}  # DP Path sample
#     # _ast = element_ast.Boundary()
#     # _ast.__dict__ = dict(name='qwe', layer='PIMP', width=100.0, height=100.0, XY=[[0,0]]) # DC Boundary sample
#     _ast = element_ast.Path()
#     _ast.__dict__ = dict(name='qwe',layer='PIMP',XY=[[-445, 233], [33, 233], [33, -8]],width=100) # DC Path sample
#
#     a.get_dpdict_return_ast(x)
#     a.get_ast_return_dpdict(_ast)
