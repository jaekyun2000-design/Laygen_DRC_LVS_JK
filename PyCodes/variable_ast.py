import ast
import astunparse


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
        'elements',
        'XY',
        'x_space_distance',
        'y_space_distance',
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
        return [
            ast.For(
                target=ast.Tuple(
                    elts = [
                        ast.Name(
                            id='i'
                        ),
                        ast.Name(
                            id='element'
                        ),
                    ]
                ),
                iter=ast.Call(
                    func = ast.Name(
                        id = 'enumerate'
                    ),
                    args = [
                        ast.Name(
                            id = 'elements'
                        )
                    ],
                    keywords = []
                ),
                body = [
                    ast.Assign(
                        targets = [
                            ast.Subscript(
                                value=1
                            )
                        ],
                        value =ast.List()
                    )
                ],
                orelse = []
            )
        ]


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
    kk = tf.visit(ea)
    print(kk)
    print(astunparse.dump(kk))
    astunparse.unparse(kk)