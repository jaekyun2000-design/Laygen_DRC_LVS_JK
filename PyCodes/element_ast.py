import ast
import copy
import warnings

import astunparse
from PyCodes import ASTmodule
# listTypeData = ['Lib','tb','PlaceDef','RouteDef','DRCDef','Iteration','P_R']
custom_ast_list = ['Generator','Sref','Boundary','Path', 'Text']
#--start constants--

class Generator(ast.AST):
    def __init__(self, *args, **kwargs):
        pass

    _fields = (
        'name',
        'init',
        'place',
        'routing',
        'DRC',
        'main',
    )


class ElementNode(ast.AST):
    def __init__(self, *args, **kwargs):
        pass

    _fields = (
    )

class Boundary(ElementNode):
    def __init__(self, *args, **kwargs):
        super().__init__()
    _fields = (
        'name',     # name str
        'layer',    # layer name str
        'XY',       # double list or variable name str
        'width',    # int or str
        'height'    # int or str
    )

class Path(ElementNode):
    def __init__(self, *args, **kwargs):
        super().__init__()
    _fields = (
        'name',     # name str
        'layer',    # layer name str
        'XY',       # double list or variable name str
        'width',    # int or str
    )

class Sref(ElementNode):
    def __init__(self, *args, **kwargs):
        super().__init__()
    _fields = (
        'name',     # name str
        'library',   # library module str
        'className',    # class name str
        'XY',       # double list or str
        'calculate_fcn',
        'parameters'
    )

class Text(ElementNode):
    def __init__(self, *args, **kwargs):
        super().__init__()
    _fields = (
        'id',  # id str
        'name',  # name str
        'layer',  # layer name str
        'pres',  # list [a,a,a]
        'reflect',  # list [a,a,a]
        'XY',  # double list or variable name str
        'magnitude',  # float
        'angle',  # float
        'text'  # int or str
    )

class VariableNameVisitor(ast.NodeVisitor):
    def __init__(self):
        super(VariableNameVisitor, self).__init__()
        self.variable_name_list = []

    def visit_Name(self, node):
        self.variable_name_list.append(node.id)

    def visit_Constant(self, node):
        if type(node.value) == str:
            try:
                int(node.value)
            except:
                self.variable_name_list.append(node.value)


class GeneratorTransformer(ast.NodeTransformer):
    def visit_Generator(self,node):
        return ast.copy_location(
            ast.ClassDef(
                name=node.name,
                bases= [
                    ast.Name(
                        id = 'StickDiagram._StickDiagram'
                    )
                ],
                body = [
                    ast.FunctionDef(
                        name = '__init__',
                        args = ast.arguments(
                            args=[
                                ast.arg(arg='self',annotation=None),
                                ast.arg(arg='_DesignParameter=None',annotation=None),
                                ast.arg(arg=f'_name="{node.name}"',annotation=None)
                            ],
                            defaults = [],
                            decorator_list=[],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None

                        ),
                        body=[

                        ],
                        decorator_list=[],
                        returns = None
                    ),
                    ast.FunctionDef(
                        name='place',
                        args=ast.arguments(
                            args=[
                                ast.arg(arg='self', annotation=None),
                            ],
                            defaults=[],
                            decorator_list=[],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None

                        ),
                        body=[

                        ],
                        decorator_list=[],
                        returns=None

                    )
                ],
                keywords = [],
                decorator_list = []
            )
            , node
        )

class ElementTransformer(ast.NodeTransformer):

    def xy_syntax_checker(self,node):
        node._type = ASTmodule._getASTtype(node)
        if node._type == 'Path':
            if 'XY' in node.__dict__:
                if type(node.XY) != list:
                    return None  ## 기본적으로 모든 value는 list 안에 들어가 있음
                else:
                    if type(node.XY[0]) == str:
                        return 'string'
                    elif type(node.XY[0]) == list:
                        if type(node.XY[0][0]) == list:
                            return 'list'
                        elif type(node.XY[0][0]) == str:
                            return 'string'
                        else:
                            return 'ast'
                    else:
                        return 'ast'
        else:
            if 'XY' in node.__dict__:
                if type(node.XY) != list:
                    return None  ## 기본적으로 모든 value는 list 안에 들어가 있음
                else:
                    if type(node.XY[0]) == list:
                        return 'list'
                    elif type(node.XY[0]) == str:
                        return 'string'
                    else:
                        return 'ast'

    def xy_string_syntax_corrector(self,node):
        tmp_xy = copy.deepcopy(node.xy)
        if type(tmp_xy) != list:
            warnings.warn("Invalid xy detected")
        for i, level1_element in enumerate(tmp_xy):
            if type(level1_element) == str: # input is variable
                pass                        # ex) [ 'var1']
            elif type(level1_element) == list:
                for j, level2_element in enumerate(level1_element):
                    for k, level3_element in enumerate(level2_element):
                        if type(level3_element) == str:
                            tmp_xy[i][j][k] = level3_element.replace("'","\\'").replace('"','\\"')
                        elif type(level3_element) == list:
                            for l, level4_element in enumerate(level3_element):
                                tmp_xy[i][j][k][l] = level4_element.replace("'","\\'").replace('"','\\"')
            elif '_ast' in str(node.__class__):                           # input is ast
                pass
            else:
                pass
        return tmp_xy


    def visit_Boundary(self,node):
        syntax = self.xy_syntax_checker(node)

        if syntax == 'list' :#or syntax == 'string':
            tmp_xy = str(node.XY).replace("'","")
            sentence = f"self._DesignParameter['{node.name}'] = self._BoundaryElementDeclaration(_Layer = DesignParameters._LayerMapping['{node.layer}'][0],\
                      _Datatype = DesignParameters._LayerMapping['{node.layer}'][1],_XYCoordinates = {tmp_xy},\
                      _XWidth = {node.width}, _YWidth = {node.height})"
        elif syntax == 'string':
            tmp_xy = str(node.XY[0]).replace("'","")
            sentence = f"self._DesignParameter['{node.name}'] = self._BoundaryElementDeclaration(_Layer = DesignParameters._LayerMapping['{node.layer}'][0],\
                                  _Datatype = DesignParameters._LayerMapping['{node.layer}'][1],_XYCoordinates = {tmp_xy},\
                                  _XWidth = {node.width}, _YWidth = {node.height})"
        elif syntax == 'ast':
            tmp_xy = astunparse.unparse(node.XY).replace('\n', '')
            sentence = f"self._DesignParameter['{node.name}'] = self._BoundaryElementDeclaration(_Layer = DesignParameters._LayerMapping['{node.layer}'][0],\
                                              _Datatype = DesignParameters._LayerMapping['{node.layer}'][1],_XYCoordinates = {tmp_xy},\
                                              _XWidth = {node.width}, _YWidth = {node.height})"
        # print(sentence)
        tmp = ast.parse(sentence)
        return tmp.body[0]

    def visit_Path(self,node):
        syntax = self.xy_syntax_checker(node)

        if syntax == 'list' or syntax == 'string':
            tmp_xy = str(node.XY).replace("'", "")
            sentence = f"self._DesignParameter['{node.name}'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['{node.layer}'][0],\
                       _Datatype = DesignParameters._LayerMapping['{node.layer}'][1],_XYCoordinates = {tmp_xy}, _Width = {node.width})"
        # elif syntax == 'str':
        #     sentence = f"self._DesignParameter['{node.name}'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['{node.layer}'][0],\
        #                _Datatype = DesignParameters._LayerMapping['{node.layer}'][1],_XYCoordinates = {node.XY}, _Width = {node.width})"
        elif syntax == 'ast':
            tmp_xy = astunparse.unparse(node.XY).replace('\n', '')
            sentence = f"self._DesignParameter['{node.name}'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['{node.layer}'][0],\
                       _Datatype = DesignParameters._LayerMapping['{node.layer}'][1],_XYCoordinates = {node.XY}, _Width = {node.width})"
        tmp = ast.parse(sentence)
        return tmp.body[0]

    def visit_Sref(self,node):
        syntax = self.xy_syntax_checker(node)
        print(f'debug: {syntax}')
        parameter_sentence = ",".join([f'{key} = {value}' for key, value in node.parameters.items()])

        if syntax == 'list':
            tmp_xy = str(node.XY).replace("'", "")
            sentence = f"self._DesignParameter['{node.name}'] = self._SrefElementDeclaration(_DesignObj = {node.library}.{node.className}("\
                       f"_Name = '{node.name}In{{}}'.format(_Name)))[0]\n"
            sentence +=f"self._DesignParameter['{node.name}']['_DesignObj'].{node.calculate_fcn}(**dict(" +parameter_sentence + "))\n"
            sentence +=f"self._DesignParameter['{node.name}']['_XYCoordinates'] = {tmp_xy}"

        elif syntax == 'string': # need to check
            tmp_xy = str(node.XY).replace("'", "")
            sentence = f"self._DesignParameter['{node.name}'] = self._SrefElementDeclaration(_DesignObj = {node.library}.{node.className}(" \
                       f"_Name = '{node.name}In{{}}'.format(_Name)))[0]\n"
            sentence += f"self._DesignParameter['{node.name}']['_DesignObj'].{node.calculate_fcn}(**dict(" + parameter_sentence + "))\n"
            sentence += f"self._DesignParameter['{node.name}']['_XYCoordinates'] = [[{tmp_xy}]]"

        elif syntax == 'ast':
            tmp_xy = astunparse.unparse(node.XY).replace('\n','')
            sentence = f"self._DesignParameter['{node.name}'] = self._SrefElementDeclaration(_DesignObj = {node.library}.{node.className}(" \
                       f"_Name = '{node.name}In{{}}'.format(_Name)))[0]\n"
            sentence += f"self._DesignParameter['{node.name}']['_DesignObj'].{node.calculate_fcn}(**dict(" + parameter_sentence + "))\n"
            sentence += f"self._DesignParameter['{node.name}']['_XYCoordinates'] = {tmp_xy}"

        # if (type(node.XY) == list) or node.XY.find(',') == -1:
        #     parameter_sentence = ",".join([f'{key} = {value}' for key, value in node.parameters.items()])
        #     sentence = f"self._DesignParameter['{node.name}'] = self._SrefElementDeclaration(_DesignObj = {node.library}.{node.className}("\
        #                f"_Name = '{node.name}In{{}}'.format(_Name)))[0]\n"
        #     sentence +=f"self._DesignParameter['{node.name}']['_DesignObj'].{node.calculate_fcn}(**dict(" +parameter_sentence + "))\n"
        #     sentence +=f"self._DesignParameter['{node.name}']['_XYCoordinates'] = {node.XY}"
        #
        # else:
        #     parameter_sentence = ",".join([f'{key} = {value}' for key, value in node.parameters.items()])
        #     sentence = f"self._DesignParameter['{node.name}'] = self._SrefElementDeclaration(_DesignObj = {node.library}.{node.className}(" \
        #                f"_Name = '{node.name}In{{}}'.format(_Name)))[0]\n"
        #     sentence += f"self._DesignParameter['{node.name}']['_DesignObj'].{node.calculate_fcn}(**dict(" + parameter_sentence + "))\n"
        #     sentence += f"self._DesignParameter['{node.name}']['_XYCoordinates'] = [[{node.XY}]]"


        tmp = ast.parse(sentence)
        return tmp.body

    def visit_Text(self, node):
        sentence = f"self.{node.name} = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['{node.layer}'][0],\
 _Datatype = DesignParameters._LayerMapping['{node.layer}'][1], _Presentation = {node.pres}, _Reflect = {node.reflect}, _XYCoordinates = {node.XY},\
 _Mag = {node.magnitude}, _Angle = {node.angle}, _TEXT = '{node.text}')"
        print(sentence)
        tmp = ast.parse(sentence)
        return tmp.body[0]


# class MacroTransformer1(ast.NodeTransformer):
#     def visit_MacroKeyword(self,node):
#         return ast.copy_location(
#             ast.keyword(
#                     arg=node.arg,
#                     value = MacroListSubscript(
#                         list_id = node.id,
#                         list_id_attr = node.attr,
#                         index1 = node.index1,
#                         index2 = node.index2
#                     )
#                     # value=ast.Subscript(
#                     #     value=ast.Subscript(
#                     #         value=ast.Attribute(
#                     #             value=ast.Name(
#                     #                 id=node.id
#                     #             ),
#                     #             attr=node.attr
#                     #         ),
#                     #         slice=node.index1
#                     #     ),
#                     #     slice=node.index2
#                     # )
#                 )
#             ,node
#         )
#
# class MacroTransformer2(ast.NodeTransformer):
#     def visit_MacroListSubscript(self,node):
#         return ast.copy_location(
#             ast.Subscript(
#                 value=ast.Subscript(
#                     value=ast.Attribute(
#                         value=ast.Name(
#                             id=node.list_id
#                         ),
#                         attr=node.list_id_attr
#                     ),
#                     slice=node.index1
#                 ),
#                 slice=node.index2
#             ),
#             node
#         )
#
#
# class MacroSubscript(ast.AST):
#     _fields = (
#         'id',
#         'attr',
#         'index',
#     )
#
# class MacorSubscriptTransformer(ast.NodeTransformer):
#     def visit_MacroSubscript(self,node):
#         for field in node._fields:
#             if not field in node.__dict__:
#                 node.__dict__[field] = None
#         return ast.copy_location(
#             ast.Subscript(
#                 value=ast.Attribute(
#                     value=ast.Name(
#                         id=node.id
#                     ),
#                     attr=node.attr
#                 ),
#                 slice=node.index
#             ),
#             node
#         )
#

    ###### Below is the partial genuine ast format of Boundary Element : Do not delete #######

    #     return ast.Assign(
    #             targets=[ast.Name(
    #                 id=node.name
    #             )],
    #             value=ast.Call(
    #                 func=ast.Attribute(
    #                     value=ast.Name(
    #                         id='self'
    #                     ),
    #                     attr='_BoundaryElementDeclaration'
    #                 ),
    #                 args=[]
    #                 ,
    #                 keywords=[
    #                     MacroKeyword(
    #                         arg='_Layer',
    #                         id="DesignParameters",
    #                         attr='LayerMapping',
    #                         index1=ast.Str(
    #                             s=node.layer
    #                         ),
    #                         index2=ast.Num(
    #                             n=0
    #                         )
    #                     ),
    #                     MacroKeyword(
    #                         arg='_Datatype',
    #                         id="DesignParameters",
    #                         attr='LayerMapping',
    #                         index1=ast.Str(
    #                             s=node.layer
    #                         ),
    #                         index2=ast.Num(
    #                             n=1
    #                         ),
    #                     )
    #                 ]
    #             )
    #         )




        # return ast.Assign(
        #         targets=[ast.Name(
        #             id=node.name
        #         )],
        #         value=ast.Call(
        #             func=ast.Attribute(
        #                 value=ast.Name(
        #                     id='self'
        #                 ),
        #                 attr='_PathElementDeclaration'
        #             ),
        #             args=[]
        #             ,
        #             keywords=[
        #                 MacroKeyword(
        #                     arg = '_Layer',
        #                     id = "DesignParameters",
        #                     attr='LayerMapping',
        #                     index1 = ast.Str(
        #                         s = node.layer
        #                     ),
        #                     index2 = ast.Num(
        #                         n = 0
        #                     )
        #                 ),
        #                 MacroKeyword(
        #                     arg='_Datatype',
        #                     id="DesignParameters",
        #                     attr='LayerMapping',
        #                     index1=ast.Str(
        #                         s=node.layer
        #                     ),
        #                     index2=ast.Num(
        #                         n=1
        #                     ),
        #                 )
        #             ]
        #         )
        #     )


        # return ast.Assign(
        #         targets=[ast.Name(
        #             id=node.name
        #         )],
        #         value=ast.Call(
        #             func=ast.Attribute(
        #                 value=ast.Name(
        #                     id='self'
        #                 ),
        #                 attr='_SrefElementDeclaration'
        #             ),
        #             args=[]
        #             ,
        #             keywords=[
        #                 MacroKeyword(
        #                     arg='_Layer',
        #                     id="DesignParameters",
        #                     attr='LayerMapping',
        #                     index1=ast.Str(
        #                         s=node.layer
        #                     ),
        #                     index2=ast.Num(
        #                         n=0
        #                     )
        #                 ),
        #                 MacroKeyword(
        #                     arg='_Datatype',
        #                     id="DesignParameters",
        #                     attr='LayerMapping',
        #                     index1=ast.Str(
        #                         s=node.layer
        #                     ),
        #                     index2=ast.Num(
        #                         n=1
        #                     ),
        #                 )
        #             ]
        #         )
        #     )


if __name__ == '__main__':
    a = Boundary()
    b = Path()
    # c = Sref()
    d = Text()

    a.name = 'AdditionalMetal1Layer'
    a.layer = 'METAL1'
    a.XY = [[2,4]]
    a.width= '_XWidth'
    a.height = 200

    b.name = 'AdditionalODPath'
    b.layer = 'DIFF'
    b.XY = 'XYcenter'
    b.width = 200

    # c.name = 'NMOS'
    # c.library = 'NMOSWithDummy'
    # c.className = '_NMOS'
    # c.XY = [[0,0]]

    d.id = 'textname'
    d.layer = 'METAL1PIN'
    d.XY = [[0,0]]
    d.pres = [0,1,2]
    d.reflect = [0,0,0]
    d.magnitude = 0.1
    d.angle = 0.1
    d.text = 'VDD'

    ef = ElementTransformer().visit_Boundary(a)
    pt = ElementTransformer().visit_Path(b)
    # st = ElementTransformer().visit_Sref(c)
    print("DEBUG")

    # ab= MacroSubscript(
    #     id = 'list1',
    #     index = ast.Num(
    #         n=0
    #     )
    # )
    # ab = MacorSubscriptTransformer().visit(ab)
    # print(astunparse.unparse(ab))
    #
    # k = Generator()
    # k.name = 'FF'
    # asa = GeneratorTransformer()
    # kk = asa.visit(k)
    # astunparse.unparse(kk)
    # print(astunparse.unparse(kk))
    # # d = MacroListSubscript(
    # #     list_id = 'self',
    # #     list_id_attr = '_DesignParameter',
    # #     index1 = ast.Str(
    # #         s = '_ViaMet32Met4OnInLineTop1',
    # #     ),
    # #     index2 = ast.Str(
    # #         s = '_Wdith',
    # #     )
    # # )
    # # dk = MacroTransformer().visit(d)
