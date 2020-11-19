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

        # elif dp_dict['_DesignParametertype'] == 3:  #Sref
        #     tmpAST = element_ast.Sref()
        #     for key in element_ast.Sref._fields:
        #         if key == '_DesignParameterName':
        #             tmpAST.__dict__['name'] = dp_dict[key]
        #         elif key == 'base':
        #             tmpAST.__dict__['base'] = dp_dict[key]
        #         elif key == '_XYCoordinates':
        #             tmpAST.__dict__['XY'] = dp_dict[key]  #Not complete

        else:
            return None

        self.load_dp_dc(dp=None, dc=tmpAST)

        return tmpAST


    def get_ast_return_dpdict(self, ast):
        if ASTmodule._getASTtype(_ast) == 'Boundary':
            tmpDP = dict()
            for key in KeyManager._Boundarykey.keys():
                if key == '_Layer':
                    tmpDP[key] = ast.__dict__['layer']
                elif key == '_DesignParametertype':
                    tmpDP[key] = 1
                elif key == '_XYCoordinates':
                    tmpDP[key] = ast.__dict__['XY']
                elif key == '_XWidth':
                    tmpDP[key] = ast.__dict__['width']
                elif key == '_YWidth':
                    tmpDP[key] = ast.__dict__['height']
                elif key == '_Ignore':
                    tmpDP[key] = None
                elif key == '_DesignParameterName':
                    tmpDP[key] = ast.__dict__['name']

        elif ASTmodule._getASTtype(_ast) == 'Path':
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

        # elif ASTmodule._getASTtype(_ast) == 'SRef':
        #     tmpDP = dict()
        #     for key in KeyManager._Pathkey.keys():
        #         if key == '_DesignParametertype':
        #             tmpDP[key] = 3
        #         elif key == '_Height':
        #             tmpDP[key] = None
        #         elif key == '_Color':
        #             tmpDP[key] = None
        #         elif key == '_ItemRef':
        #             tmpDP[key] = None
        #         else:
        #             tmpDP[key] = ast.__dict__[key]

        else:
            return None

        self.load_dp_dc(dp=tmpDP, dc=None)

        return tmpDP

    def load_dp_dc(self,dp,dc):
        if dc == None:
            self.elementParameterDict[dp['_DesignParameterName']] = dp
        elif dp == None:
            self.elementConstraintDict[dc.__dict__['name']] = dc

        print(dp)
        print(dc)
        print('---')

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

if __name__ == '__main__':
    a = ElementManager()
    # x = {'_Layer': 'PIMP', '_DesignParametertype': 1, '_XYCoordinates': [[0, 0]], '_XWidth': 100.0, '_YWidth': 100.0, '_Ignore': None, '_DesignParameterName': 'qwe'}    # DP Boundary sample
    x = {'_DesignParameterName': 'qwe', '_Layer': 'PIMP', '_DesignParametertype': 2, '_XYCoordinates': [[-445, 233], [33, 233], [33, -8]], '_Width': 100.0, '_Height': None, '_Color': None, '_ItemRef':None}  # DP Path sample
    # _ast = element_ast.Boundary()
    # _ast.__dict__ = dict(name='qwe', layer='PIMP', width=100.0, height=100.0, XY=[[0,0]]) # DC Boundary sample
    _ast = element_ast.Path()
    _ast.__dict__ = dict(name='qwe',layer='PIMP',XY=[[-445, 233], [33, 233], [33, -8]],width=100) # DC Path sample

    a.get_dpdict_return_ast(x)
    a.get_ast_return_dpdict(_ast)
