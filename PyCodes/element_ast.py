import ast
import copy
import warnings

import astunparse
from PyCodes import variable_ast
# listTypeData = ['Lib','tb','PlaceDef','RouteDef','DRCDef','Iteration','P_R']
custom_ast_list = ['Generator','Sref','Boundary','Path', 'Text', 'MacroCell', 'Polygon']
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

class Polygon(ElementNode):
    def __init__(self, *args, **kwargs):
        super().__init__()
    _fields = (
        'name',     # name str
        'layer',    # layer name str
        'XY',       # double list or variable name str
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
    parameter_fields = []
    _fields = (
        'name',     # name str
        'library',   # library module str
        'className',    # class name str
        'XY',       # double list or str
        'calculate_fcn',
        'parameters'
    )

class MacroCell(ElementNode):
    def __init__(self, *args, **kwargs):
        super().__init__()
    _fields = (
        'name',     # name str
        'library',   # library module str
        'XY',       # double list or str
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
                tmp_ast = ast.parse(node.value)
                tmp_ast = tmp_ast.body[0].value
                if type(tmp_ast) == ast.Name:
                    self.variable_name_list.append(node.value)
                else:
                    self.visit(tmp_ast)


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
        node._type = className = type(node).__name__
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
        if syntax == 'ast':
            syntax = ''
        for field in node._fields:
            if node.__dict__[field] == '' or node.__dict__[field] == None:
                raise ValueError(f"Not valid \'{field}\' value : {node.__dict__[field]}")
            if isinstance(node.__dict__[field], ast.AST):
                tmp_ast = run_transformer(node.__dict__[field])
                node.__dict__[field] = astunparse.unparse(tmp_ast).replace('\n', '')
            elif type(node.__dict__[field]) == list and isinstance(node.__dict__[field][0], ast.AST):
                tmp_ast = run_transformer(node.__dict__[field][0])
                node.__dict__[field] = astunparse.unparse(tmp_ast).replace('\n', '')
        if syntax == 'list' :#or syntax == 'string':
            tmp_xy = str(node.XY).replace("'","")
            sentence = f"self._DesignParameter['{node.name}'] = self._BoundaryElementDeclaration(_Layer = DesignParameters._LayerMapping['{node.layer}'][0]," \
                       f"_Datatype = DesignParameters._LayerMapping['{node.layer}'][1], _XWidth = {node.width}, _YWidth = {node.height})\n"
            sentence += f"self._DesignParameter['{node.name}']['_XYCoordinates'] = {tmp_xy}\n"
        elif syntax == 'string':
            tmp_xy = str(node.XY[0]).replace("'","")
            sentence = f"self._DesignParameter['{node.name}'] = self._BoundaryElementDeclaration(_Layer = DesignParameters._LayerMapping['{node.layer}'][0]," \
                       f"_Datatype = DesignParameters._LayerMapping['{node.layer}'][1], _XWidth = {node.width}, _YWidth = {node.height})\n"
            sentence += f"self._DesignParameter['{node.name}']['_XYCoordinates'] = {tmp_xy}\n"
        else:
            sentence = f"self._DesignParameter['{node.name}'] = self._BoundaryElementDeclaration(_Layer = DesignParameters._LayerMapping['{node.layer}'][0]," \
                       f"_Datatype = DesignParameters._LayerMapping['{node.layer}'][1], _XWidth = {node.width}, _YWidth = {node.height})\n"
            sentence += f"self._DesignParameter['{node.name}']['_XYCoordinates'] = {node.XY}\n"
        # print(sentence)
        tmp = ast.parse(sentence)
        return tmp.body

    def visit_Path(self,node):
        syntax = self.xy_syntax_checker(node)
        if syntax == 'ast':
            syntax = ''
        for field in node._fields:
            if node.__dict__[field] == '' or node.__dict__[field] == None:
                raise Exception(f"Not valid {field} value : {node.__dict__[field]}")
            if isinstance(node.__dict__[field], ast.AST):
                tmp_ast = run_transformer(node.__dict__[field])
                node.__dict__[field] = astunparse.unparse(tmp_ast).replace('\n', '')
            elif type(node.__dict__[field]) == list and isinstance(node.__dict__[field][0], ast.AST):
                tmp_ast = run_transformer(node.__dict__[field][0])
                node.__dict__[field] = astunparse.unparse(tmp_ast).replace('\n', '')

        if syntax == 'list' or syntax == 'string':
            tmp_xy = str(node.XY).replace("'", "")
            sentence = f"self._DesignParameter['{node.name}'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['{node.layer}'][0],\
                       _Datatype = DesignParameters._LayerMapping['{node.layer}'][1], _Width = {node.width})\n"
            sentence += f"self._DesignParameter['{node.name}']['_XYCoordinates'] = {tmp_xy}\n"
        else:
            sentence = f"self._DesignParameter['{node.name}'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['{node.layer}'][0],\
                                   _Datatype = DesignParameters._LayerMapping['{node.layer}'][1], _Width = {node.width})\n"
            sentence += f"self._DesignParameter['{node.name}']['_XYCoordinates'] = {node.XY}\n"
        tmp = ast.parse(sentence)
        return tmp.body

    def visit_Sref(self,node):
        syntax = self.xy_syntax_checker(node)
        print(f'debug: {syntax}')
        if syntax == 'ast':
            syntax = ''
        parameter_sentence = ",".join([f'{key} = {value}' for key, value in node.parameters.items()])


        for field in node._fields:
            if node.__dict__[field] == '' or node.__dict__[field] == None:
                raise Exception(f"Not valid {field} value : {node.__dict__[field]}")
            if isinstance(node.__dict__[field], ast.AST):
                tmp_ast = run_transformer(node.__dict__[field])
                node.__dict__[field] = astunparse.unparse(tmp_ast).replace('\n', '')
            elif type(node.__dict__[field]) == list and isinstance(node.__dict__[field][0], ast.AST):
                tmp_ast = run_transformer(node.__dict__[field][0])
                node.__dict__[field] = astunparse.unparse(tmp_ast).replace('\n', '')

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

        else:
            sentence = f"self._DesignParameter['{node.name}'] = self._SrefElementDeclaration(_DesignObj = {node.library}.{node.className}(" \
                       f"_Name = '{node.name}In{{}}'.format(_Name)))[0]\n"
            sentence += f"self._DesignParameter['{node.name}']['_DesignObj'].{node.calculate_fcn}(**dict(" + parameter_sentence + "))\n"
            sentence += f"self._DesignParameter['{node.name}']['_XYCoordinates'] = {node.XY}"

        tmp = ast.parse(sentence)
        return tmp.body

    def visit_Text(self, node):

        for field in node._fields:
            if node.__dict__[field] == '' or node.__dict__[field] == None:
                raise Exception(f"Not valid {field} value : {node.__dict__[field]}")
            if isinstance(node.__dict__[field], ast.AST):
                node.__dict__[field] = astunparse.unparse(node.__dict__[field]).replace('\n', '')
            elif type(node.__dict__[field]) == list and isinstance(node.__dict__[field][0], ast.AST):
                node.__dict__[field] = astunparse.unparse(node.__dict__[field]).replace('\n', '')

        sentence = f"self.{node.name} = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['{node.layer}'][0]," \
                   f"_Datatype = DesignParameters._LayerMapping['{node.layer}'][1], _Presentation = {node.pres}, _Reflect = {node.reflect}, _XYCoordinates = {node.XY}," \
                   f"_Mag = {node.magnitude}, _Angle = {node.angle}, _TEXT = '{node.text}')"
        print(sentence)
        tmp = ast.parse(sentence)
        return tmp.body[0]

    def visit_Polygon(self,node):
        """
        field:
            name
            layer
            XY
        """
        syntax = self.xy_syntax_checker(node)
        if syntax == 'ast':
            syntax = ''
        for field in node._fields:
            if node.__dict__[field] == '' or node.__dict__[field] == None:
                raise ValueError(f"Not valid \'{field}\' value : {node.__dict__[field]}")
            if isinstance(node.__dict__[field], ast.AST):
                tmp_ast = run_transformer(node.__dict__[field])
                node.__dict__[field] = astunparse.unparse(tmp_ast).replace('\n', '')
            elif type(node.__dict__[field]) == list and isinstance(node.__dict__[field][0], ast.AST):
                tmp_ast = run_transformer(node.__dict__[field][0])
                node.__dict__[field] = astunparse.unparse(tmp_ast).replace('\n', '')

        if syntax == 'list':  # or syntax == 'string':
            tmp_xy = str(node.XY).replace("'", "")
            sentence = f"self._DesignParameter['{node.name}'] = self._PolygonElementDeclaration(_Layer = DesignParameters._LayerMapping['{node.layer}'][0]," \
                       f"_Datatype = DesignParameters._LayerMapping['{node.layer}'][1])\n"
            sentence += f"self._DesignParameter['{node.name}']['_XYCoordinates'] = {tmp_xy}\n"
        elif syntax == 'string':
            tmp_xy = str(node.XY[0]).replace("'", "")
            sentence = f"self._DesignParameter['{node.name}'] = self._PolygonElementDeclaration(_Layer = DesignParameters._LayerMapping['{node.layer}'][0]," \
                       f"_Datatype = DesignParameters._LayerMapping['{node.layer}'][1])\n"
            sentence += f"self._DesignParameter['{node.name}']['_XYCoordinates'] = {tmp_xy}\n"
        else:
            sentence = f"self._DesignParameter['{node.name}'] = self._PolygonElementDeclaration(_Layer = DesignParameters._LayerMapping['{node.layer}'][0]," \
                       f"_Datatype = DesignParameters._LayerMapping['{node.layer}'][1])\n"
            sentence += f"self._DesignParameter['{node.name}']['_XYCoordinates'] = {node.XY}\n"
            # print(sentence)
        tmp = ast.parse(sentence)
        return tmp.body
    def visit_MacroCell(self,node):
        """
        field:
            name
            referencce
            XY
        """
        syntax = self.xy_syntax_checker(node)
        if syntax == 'ast':
            syntax = ''
        for field in node._fields:
            if node.__dict__[field] == '' or node.__dict__[field] == None:
                raise ValueError(f"Not valid \'{field}\' value : {node.__dict__[field]}")
            if isinstance(node.__dict__[field], ast.AST):
                tmp_ast = run_transformer(node.__dict__[field])
                node.__dict__[field] = astunparse.unparse(tmp_ast).replace('\n', '')
            elif type(node.__dict__[field]) == list and isinstance(node.__dict__[field][0], ast.AST):
                tmp_ast = run_transformer(node.__dict__[field][0])
                node.__dict__[field] = astunparse.unparse(tmp_ast).replace('\n', '')

        if syntax == 'list':  # or syntax == 'string':
            tmp_xy = str(node.XY).replace("'", "")
            sentence = f"self._DesignParameter['{node.name}'] = self._MacroElementDeclaration(_ReferenceGDS='{node.library}'," \
                       f" _XYCoordinates={tmp_xy})\n"
        elif syntax == 'string':
            tmp_xy = str(node.XY[0]).replace("'", "")
            sentence = f"self._DesignParameter['{node.name}'] = self._MacroElementDeclaration(_ReferenceGDS='{node.library}'," \
                       f" _XYCoordinates={tmp_xy})\n"
        else:
            sentence = f"self._DesignParameter['{node.name}'] = self._MacroElementDeclaration(_ReferenceGDS='{node.library}'," \
                       f" _XYCoordinates={node.XY})\n"
            # print(sentence)
        tmp = ast.parse(sentence)
        return tmp.body
def run_transformer(source_ast):
    module_ast = ast.Module()
    if type(source_ast) == list:
        module_ast.body = copy.deepcopy(source_ast)
    else:
        module_ast.body = copy.deepcopy([source_ast])

    result_ast = variable_ast.IrregularTransformer().visit(module_ast)
    result_ast = variable_ast.VariableTransformer().visit(result_ast)
    return result_ast


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
