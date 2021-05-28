import ast
import astunparse

# listTypeData = ['Lib','tb','PlaceDef','RouteDef','DRCDef','Iteration','P_R']
custom_ast_list = ['Generator','Sref','Boundary','Path']
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

    def visit_Boundary(self,node):
        sentence = f"self._DesignParameter['{node.name}'] = self._BoundaryElementDeclaration(_Layer = DesignParameters._LayerMapping['{node.layer}'][0],\
                  _Datatype = DesignParameters._LayerMapping['{node.layer}'][1],_XYCoordinates = {node.XY},\
                  _XWidth = {node.width}, _YWidth = {node.height})"
        # print(sentence)
        tmp = ast.parse(sentence)
        return tmp.body[0]

    def visit_Path(self,node):
        sentence = f"self._DesignParameter['{node.name}'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['{node.layer}'][0],\
_Datatype = DesignParameters._LayerMapping['{node.layer}'][1],_XYCoordinates = {node.XY}, _Width = {node.width})"
        tmp = ast.parse(sentence)
        return tmp.body[0]

    def visit_Sref(self,node):
        if (type(node.XY) == list) or node.XY.find(',') == -1:
            parameter_sentence = ",".join([f'{key} = {value}' for key, value in node.parameters.items()])
            sentence = f"self._DesignParameter['{node.name}'] = self._SrefElementDeclaration(_DesignObj = {node.library}.{node.className}("\
                       f"_Name = '{node.name}In{{}}'.format(_Name)), _XYCoordinates = {node.XY})[0]\n"
            # sentence = f"self._DesignParameter['{node.name}'] = self._SrefElementDeclaration(_DesignObj = {node.library}.{node.className}(_DesignParameter = " \
            #            f"dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))," \
            #            f"_Name = '{node.name}In{{}}'.format(_Name)), _XYCoordinates = {node.XY})[0]\n"
            sentence +=f"self._DesignParameter['{node.name}']['_DesignObj'].{node.calculate_fcn}(**dict(" +parameter_sentence + "))"
            # sentence +=f"self._DesignParameter['{node.name}']['_DesignObj']._CalculateDesignParameter(**dict(" +parameter_sentence + "))"
                       # f"self._DesignParameter['{node.name}']['_DesignObj']._CalculateDesignParameter(**{node.parameters})"
                       # f" dict( dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))," \
                       # f" ** {node.parameters})" \
        else:
            parameter_sentence = ",".join([f'{key} = {value}' for key, value in node.parameters.items()])
            sentence = f"self._DesignParameter['{node.name}'] = self._SrefElementDeclaration(_DesignObj = {node.library}.{node.className}(" \
                       f"_Name = '{node.name}In{{}}'.format(_Name)), _XYCoordinates = [[{node.XY}]])[0]\n"
            # sentence = f"self._DesignParameter['{node.name}'] = self._SrefElementDeclaration(_DesignObj = {node.library}.{node.className}(_DesignParameter = " \
            #            f"dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))," \
            #            f"_Name = '{node.name}In{{}}'.format(_Name)), _XYCoordinates = {node.XY})[0]\n"
            sentence += f"self._DesignParameter['{node.name}']['_DesignObj'].{node.calculate_fcn}(**dict(" + parameter_sentence + "))"
            # sentence +=f"self._DesignParameter['{node.name}']['_DesignObj']._CalculateDesignParameter(**dict(" +parameter_sentence + "))"
            # f"self._DesignParameter['{node.name}']['_DesignObj']._CalculateDesignParameter(**{node.parameters})"
            # f" dict( dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))," \
            # f" ** {node.parameters})" \

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
    c = Sref()
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

    c.name = 'NMOS'
    c.library = 'NMOSWithDummy'
    c.className = '_NMOS'
    c.XY = [[0,0]]

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
    st = ElementTransformer().visit_Sref(c)

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
