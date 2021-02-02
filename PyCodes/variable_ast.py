import ast
import astunparse

custom_ast_list = ['GeneratorVariable', 'ArgumentVariable', 'ElementArray','DynamicElementArray','Distance']

class GeneratorVariable(ast.AST):
    def __init__(self, *args, **kwargs):
        pass

    _fields = (
    )

class ArgumentVariable(GeneratorVariable):
    def __init__(self, *args, **kwargs):
        super().__init__()
    _fields = (
        'name',
        'value',
    )


class ElementArray(GeneratorVariable):
    def __init__(self, *args, **kwargs):
        super().__init__()
    _fields = (
        'elements', # list or variable name str
        'XY',       # double list or variable name str
        'x_space_distance',     # int or string
        'y_space_distance',     # int or string
    )

class DynamicElementArray(GeneratorVariable):
    def __init__(self, *args, **kwargs):
        super().__init__()
    _fields = (
        'element',
        'number_variable',
        'XY',
        'x_space_distance',
        'y_space_distance',
    )

class Distance(GeneratorVariable):
    def __init__(self, *args, **kwargs):
        super().__init__()
    _fields = (
        'ref_element',
        'target_element',
        'distance',
    )

class VariableTransformer(ast.NodeTransformer):
    def visit_ElementArray(self,node):
        # sentence0 = f"elements = {node.elements}"
        if type(node.XY) ==str:
            sentence = f"for (i, element) in enumerate({node.elements}):\
                        \tself._DesignParameter[element]['_XYCoordinates'] = [({node.XY}[0][0] + (i * {node.x_space_distance})), ({node.XY}[0][1] + (i * {node.y_space_distance}))]"
        else:
            sentence = f"for (i, element) in enumerate({node.elements}):\
            \tself._DesignParameter[element]['_XYCoordinates'] = [({node.XY[0][0]} + (i * {node.x_space_distance})), ({node.XY[0][1]} + (i * {node.y_space_distance}))]"
        print(sentence)
        # tmp0 = ast.parse(sentence0)
        tmp = ast.parse(sentence)
        return tmp.body

        # return [
        #     ast.For(
        #         target=ast.Tuple(
        #             elts = [
        #                 ast.Name(
        #                     id='i'
        #                 ),
        #                 ast.Name(
        #                     id='element'
        #                 ),
        #             ]
        #         ),
        #         iter=ast.Call(
        #             func = ast.Name(
        #                 id = 'enumerate'
        #             ),
        #             args = [
        #                 ast.Name(
        #                     id=node.elements
        #                 )
        #             ],
        #             keywords = []
        #         ),
        #         body = [
        #             ast.Assign(
        #                 targets = [
        #                     ast.Subscript(
        #                         value=ast.Subscript(
        #                             value = ast.Attribute(
        #                                 value = ast.Name(
        #                                     id = 'self'
        #                                 ),
        #                                 attr = '_DesignParameter'
        #                             ),
        #                             slice = ast.Index(
        #                                 value = ast.Name(
        #                                     id = 'element'
        #                                 )
        #                             )
        #                         ),
        #                         slice = ast.Index(
        #                             value = ast.Str(
        #                                 s = '_XYCoordinates'
        #                             )
        #                         )
        #                     )
        #                 ],
        #                 value = ast.List(
        #                     elts = [
        #                         ast.BinOp(
        #                             # left = ast.Subscript(
        #                             #     value = ast.Name(
        #                             #         id = 'XY'
        #                             #     ),
        #                             #     slice = ast.Index(
        #                             #         value = ast.Num(
        #                             #             n = 0
        #                             #         )
        #                             #     ),
        #                             # ),
        #                             left = ast.Num(
        #                                 n = node.XY[0][0]
        #                             ),
        #                             op=ast.Add()
        #                             ,
        #                             right = ast.BinOp(
        #                                 left = ast.Name(
        #                                     id = 'i'
        #                                 ),
        #                                 op = ast.Mult()
        #                                 ,
        #                                 right = ast.Name(
        #                                     id = int( node.x_space_distance)
        #                                 )
        #                             )
        #                         ),
        #                         ast.BinOp(
        #                             left = ast.Num(
        #                                 n = node.XY[0][1]
        #                             ),
        #                             op = ast.Add()
        #                             ,
        #                             right = ast.BinOp(
        #                                 left=ast.Name(
        #                                     id='i'
        #                                 ),
        #                                 op=ast.Mult()
        #                                 ,
        #                                 right=ast.Name(
        #                                     id = int(node.y_space_distance)
        #                                 )
        #                             )
        #                         )
        #                     ]
        #                 )
        #             )
        #         ],
        #         orelse = []
        #     )
        # ]


    def visit_Sref(self,node):
        return ast.Assign(
                targets=[ast.Name(
                    id=node.name
                )],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(
                            id='self'
                        ),
                        attr='_SrefElementDeclaration'
                    ),
                    args=[]
                    ,
                    keywords=[
                        MacroKeyword(
                            arg='_Layer',
                            id="DesignParameters",
                            attr='LayerMapping',
                            index1=ast.Str(
                                s=node.layer
                            ),
                            index2=ast.Num(
                                n=0
                            )
                        ),
                        MacroKeyword(
                            arg='_Datatype',
                            id="DesignParameters",
                            attr='LayerMapping',
                            index1=ast.Str(
                                s=node.layer
                            ),
                            index2=ast.Num(
                                n=1
                            ),
                        )
                    ]
                )
            )


    def visit_Path(self,node):
        return ast.Assign(
                targets=[ast.Name(
                    id=node.name
                )],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(
                            id='self'
                        ),
                        attr='_PathElementDeclaration'
                    ),
                    args=[]
                    ,
                    keywords=[
                        MacroKeyword(
                            arg = '_Layer',
                            id = "DesignParameters",
                            attr='LayerMapping',
                            index1 = ast.Str(
                                s = node.layer
                            ),
                            index2 = ast.Num(
                                n = 0
                            )
                        ),
                        MacroKeyword(
                            arg='_Datatype',
                            id="DesignParameters",
                            attr='LayerMapping',
                            index1=ast.Str(
                                s=node.layer
                            ),
                            index2=ast.Num(
                                n=1
                            ),
                        )
                    ]
                )
            )

if __name__ == '__main__':
    ea = ElementArray()
    tf = VariableTransformer()
    k = ['a','b']
    ea.elements = 'k'
    # XWidth,YWidth = str(200),
    ea.XY = [['XWidth','YWidth']]
    ea.x_space_distance = '100'
    ea.y_space_distance = '200'

    kk = tf.visit(ea)
    print(kk)
    print(astunparse.dump(kk))
    astunparse.unparse(kk)
    print(astunparse.unparse(kk))