import ast
import astunparse

# listTypeData = ['Lib','tb','PlaceDef','RouteDef','DRCDef','Iteration','P_R']
custom_ast_list = ['Sref','Boundary','Path']
#--start constants--


class ElementNode(ast.AST):
    def __init__(self, *args, **kwargs):
        pass

    _fields = (
    )

class Sref(ElementNode):
    def __init__(self, *args, **kwargs):
        super().__init__()
    _fields = (
        'name',
        'base',
        'XY',
    )

class Boundary(ElementNode):
    def __init__(self, *args, **kwargs):
        super().__init__()
    _fields = (
        'name',
        'layer',
        'XY',
        'width',
        'height'
    )

class Path(ElementNode):
    def __init__(self, *args, **kwargs):
        super().__init__()
    _fields = (
        'name',
        'layer',
        'XY',
        'width',
    )

class MacroKeyword(ast.AST):
    _fields = (
        'arg',
        'id',
        'attr',
        'index1',
        'index2'
    )

class MacroListSubscript(ast.AST):
    _fields = (
        'list_id',
        'list_id_attr',
        'index1',
        'index2'
    )


class MacroSubscript(ast.AST):
    _fields = (
        'id',
        'id_attr',
        'index',
    )

class ElementTransformer(ast.NodeTransformer):
    def visit_Boundary(self,node):
        return [
            ast.Assign(
                targets=[ast.Name(
                    id=node.name
                )],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(
                            id='self'
                        ),
                        attr='_BoundaryElementDeclaration'
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
        ]

    def visit_Sref(self,node):
        return [
            ast.Assign(
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
        ]

    def visit_Path(self,node):
        return [
            ast.Assign(
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
        ]


class MacroTransformer1(ast.NodeTransformer):
    def visit_MacroKeyword(self,node):
        return ast.copy_location(
            ast.keyword(
                    arg=node.arg,
                    value = MacroListSubscript(
                        list_id = node.id,
                        list_id_attr = node.attr,
                        index1 = node.index1,
                        index2 = node.index2
                    )
                    # value=ast.Subscript(
                    #     value=ast.Subscript(
                    #         value=ast.Attribute(
                    #             value=ast.Name(
                    #                 id=node.id
                    #             ),
                    #             attr=node.attr
                    #         ),
                    #         slice=node.index1
                    #     ),
                    #     slice=node.index2
                    # )
                )
            ,node
        )

class MacroTransformer2(ast.NodeTransformer):
    def visit_MacroListSubscript(self,node):
        return ast.copy_location(
            ast.Subscript(
                value=ast.Subscript(
                    value=ast.Attribute(
                        value=ast.Name(
                            id=node.list_id
                        ),
                        attr=node.list_id_attr
                    ),
                    slice=node.index1
                ),
                slice=node.index2
            ),
            node
        )


class MacroSubscript(ast.AST):
    _fields = (
        'id',
        'attr',
        'index',
    )

class MacorSubscriptTransformer(ast.NodeTransformer):
    def visit_MacroSubscript(self,node):
        for field in node._fields:
            if not field in node.__dict__:
                node.__dict__[field] = None
        return ast.copy_location(
            ast.Subscript(
                value=ast.Attribute(
                    value=ast.Name(
                        id=node.id
                    ),
                    attr=node.attr
                ),
                slice=node.index
            ),
            node
        )


if __name__ == '__main__':
    a = Boundary()
    a.name = "OD1"
    a.layer = 'OD'
    b= Path()
    b.name = 'Met1Path'
    b.layer = 'METAL4'
    k = ast.Module()
    k.body = []
    k.body.append(b)
    k.body.append(a)
    k = ElementTransformer().visit(k)
    k = MacroTransformer1().visit(k)
    k = MacroTransformer2().visit(k)
    print(astunparse.unparse(k))

    ab= MacroSubscript(
        id = 'list1',
        index = ast.Num(
            n=0
        )
    )
    ab = MacorSubscriptTransformer().visit(ab)
    print(astunparse.unparse(ab))

    # d = MacroListSubscript(
    #     list_id = 'self',
    #     list_id_attr = '_DesignParameter',
    #     index1 = ast.Str(
    #         s = '_ViaMet32Met4OnInLineTop1',
    #     ),
    #     index2 = ast.Str(
    #         s = '_Wdith',
    #     )
    # )
    # dk = MacroTransformer().visit(d)
