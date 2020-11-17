from PyCodes import element_ast
from PyCodes import ASTmodule

class ElementManager:
    def __init__(self):
        self.elementParameterDict = dict()
        self.elementConstraintDict = dict()

    def get_dpdict_return_ast(self, dp_dict):
        if dp_dict['_DesignParametertype'] == 1:    #Boundary
            tmpAST = element_ast.Boundary()
            for key in element_ast.Boundary._fields:
                tmpAST.__dict__[key] = dp_dict[key]

        elif dp_dict['_DesignParametertype'] == 2:  #Path
            tmpAST = element_ast.Path()
            for key in element_ast.Path._fields:
                tmpAST.__dict__[key] = dp_dict[key]

        elif dp_dict['_DesignParametertype'] == 3:  #Sref
            tmpAST = element_ast.Sref()
            for key in element_ast.Sref._fields:
                tmpAST.__dict__[key] = dp_dict[key]

        else:
            return None

        return tmpAST


    def get_ast_return_dpdict(self, ast):
        if ASTmodule._getASTtype(_ast) == 'Boundary':
            tmpDP = dict()
            for key in KeyManager._Boundarykey.keys():
                if key == '_DesignParametertype':
                    tmpDP[key] = 1
                elif key == '_XYCoordinates':
                    tmpDP[key] = [[int(ast.__dict__[key][0]),int(ast.__dict__[key][-1])]]
                elif key == '_Ignore':
                    tmpDP[key] = None
                else:
                    tmpDP[key] = ast.__dict__[key]

        elif ASTmodule._getASTtype(_ast) == 'Path':
            tmpDP = dict()
            for key in KeyManager._Boundarykey.keys():
                if key == '_DesignParametertype':
                    tmpDP[key] = 1
                elif key == '_XYCoordinates':
                    tmpDP[key] = [[int(ast.__dict__[key][0]),int(ast.__dict__[key][-1])]]
                elif key == '_Ignore':
                    tmpDP[key] = None
                else:
                    tmpDP[key] = ast.__dict__[key]

        return tmpDP

    def load_designpar_dc(self,dp,dc):
        self.elementParameterDict[dp.name] = dp
        self.elementConstraintDict[dc.name] = dc

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

if __name__ == '__main__':
    a = ElementManager()
    # x = {'_Layer': 'PIMP', '_DesignParametertype': 1, '_XYCoordinates': [[0, 0]], '_XWidth': 100.0, '_YWidth': 100.0, '_Ignore': None, '_DesignParameterName': 'qwe'}    # Boundary sample
    x = {'_DesignParameterName': 'qwe', '_Layer': 'PIMP', '_DesignParametertype': 2, '_XYCoordinates': [[-445, 233], [33, 233], [33, -8]], '_Width': 100.0, '_Height': None, '_Color': None, '_ItemRef':None}  # Path sample
    _ast = element_ast.Boundary()
    _ast.__dict__ = dict(_DesignParameterName='qwe', _Layer='PIMP', _XWidth='100.0', _YWidth='100.0', _XYCoordinates='0,0')

    print(a.get_dpdict_return_ast(x))
    # print(a.get_ast_return_dpdict(_ast))