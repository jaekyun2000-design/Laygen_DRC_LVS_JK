import ast
import copy
import warnings

import astunparse
from PyCodes import variable_ast
# listTypeData = ['Lib','tb','PlaceDef','RouteDef','DRCDef','Iteration','P_R']
custom_ast_list = ['Generator','Sref','Boundary','Path', 'Text', 'MacroCell']
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

        for field in node._fields:
            if node.__dict__[field] == '' or node.__dict__[field] == None:
                raise ValueError(f"Not valid \'{field}\' value : {node.__dict__[field]}")
            if field == 'XY':
                continue
            if isinstance(node.__dict__[field], ast.AST):
                tmp_ast = run_transformer(node.__dict__[field])
                node.__dict__[field] = astunparse.unparse(tmp_ast).replace('\n', '')
            elif type(node.__dict__[field]) == list and isinstance(node.__dict__[field][0], ast.AST):
                tmp_ast = run_transformer(node.__dict__[field])
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
        elif syntax == 'ast':
            tmp_xy = astunparse.unparse(node.XY).replace('\n', '')
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

        for field in node._fields:
            if node.__dict__[field] == '' or node.__dict__[field] == None:
                raise Exception(f"Not valid {field} value : {node.__dict__[field]}")
            if field == 'XY':
                continue
            if isinstance(node.__dict__[field], ast.AST):
                if type(node.__dict__[field]) == 'LogicExpression':
                    tmp_node = variable_ast.LogicExpression()
                    tmp_node.id = node.__dict__[field].id
                    tmp_node.info_dict = node.__dict__[field].info_dict
                    tmp_code_ast = variable_ast.IrregularTransformer().visit_LogicExpression(tmp_node)
                elif type(node.__dict__[field]) == 'PathXY':
                    tmp_node = variable_ast.PathXY()
                    tmp_node.id = node.__dict__[field].id
                    tmp_node.info_dict = node.__dict__[field].info_dict
                    tmp_code_ast = variable_ast.IrregularTransformer().visit_PathXY(tmp_node)
                else:
                    warnings.warn(f'{type(node.__dict__[field])} is not valid inside Path element.')
                    return
                tmp_code = astunparse.unparse(tmp_code_ast)
                node.__dict__[field] = tmp_code
            elif type(node.__dict__[field]) == list and isinstance(node.__dict__[field][0], ast.AST):
                if type(node.__dict__[field][0]) == 'LogicExpression':
                    tmp_node = variable_ast.LogicExpression()
                    tmp_node.id = node.__dict__[field][0].id
                    tmp_node.info_dict = node.__dict__[field][0].info_dict
                    tmp_code_ast = variable_ast.IrregularTransformer().visit_LogicExpression(tmp_node)
                elif type(node.__dict__[field][0]) == 'PathXY':
                    tmp_node = variable_ast.PathXY()
                    tmp_node.id = node.__dict__[field][0].id
                    tmp_node.info_dict = node.__dict__[field][0].info_dict
                    tmp_code_ast = variable_ast.IrregularTransformer().visit_PathXY(tmp_node)
                else:
                    warnings.warn(f'{type(node.__dict__[field])} is not valid inside Path element.')
                    return
                tmp_code = astunparse.unparse(tmp_code_ast)
                node.__dict__[field] = tmp_code

        if syntax == 'list' or syntax == 'string':
            tmp_xy = str(node.XY).replace("'", "")
            sentence = f"self._DesignParameter['{node.name}'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['{node.layer}'][0],\
                       _Datatype = DesignParameters._LayerMapping['{node.layer}'][1], _Width = {node.width})\n"
            sentence += f"self._DesignParameter['{node.name}']['_XYCoordinates'] = {tmp_xy}\n"
        # elif syntax == 'str':
        #     sentence = f"self._DesignParameter['{node.name}'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['{node.layer}'][0],\
        #                _Datatype = DesignParameters._LayerMapping['{node.layer}'][1],_XYCoordinates = {node.XY}, _Width = {node.width})"
        elif syntax == 'ast':
            tmp_xy = astunparse.unparse(node.XY).replace('\n', '')
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
        parameter_sentence = ",".join([f'{key} = {value}' for key, value in node.parameters.items()])


        for field in node._fields:
            if node.__dict__[field] == '' or node.__dict__[field] == None:
                raise Exception(f"Not valid {field} value : {node.__dict__[field]}")
            if field == 'XY':
                continue
            if isinstance(node.__dict__[field], ast.AST):
                if type(node.__dict__[field]) == 'XYCoordinate':
                    tmp_node = variable_ast.LogicExpression()
                    tmp_node.id = node.__dict__[field].id
                    tmp_node.info_dict = node.__dict__[field].info_dict
                    tmp_code_ast = variable_ast.IrregularTransformer().visit_XYCoordinate(tmp_node)
                    tmp_code = astunparse.unparse(tmp_code_ast)
                    node.__dict__[field] = tmp_code
                else:
                    warnings.warn(f'{type(node.__dict__[field])} is not valid inside SREF element.')
                    return
            elif type(node.__dict__[field]) == list and isinstance(node.__dict__[field][0], ast.AST):
                if type(node.__dict__[field][0]) == 'XYCoordinate':
                    tmp_node = variable_ast.XYCoordinate()
                    tmp_node.id = node.__dict__[field][0].id
                    tmp_node.info_dict = node.__dict__[field][0].info_dict
                    tmp_code_ast = variable_ast.IrregularTransformer().visit_XYCoordinate(tmp_node)
                    tmp_code = astunparse.unparse(tmp_code_ast)
                    node.__dict__[field] = tmp_code
                else:
                    warnings.warn(f'{type(node.__dict__[field])} is not valid inside SREF element.')
                    return

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
        else:
            sentence = f"self._DesignParameter['{node.name}'] = self._SrefElementDeclaration(_DesignObj = {node.library}.{node.className}(" \
                       f"_Name = '{node.name}In{{}}'.format(_Name)))[0]\n"
            sentence += f"self._DesignParameter['{node.name}']['_DesignObj'].{node.calculate_fcn}(**dict(" + parameter_sentence + "))\n"
            sentence += f"self._DesignParameter['{node.name}']['_XYCoordinates'] = {node.XY}"

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

        for field in node._fields:
            if node.__dict__[field] == '' or node.__dict__[field] == None:
                raise Exception(f"Not valid {field} value : {node.__dict__[field]}")
            if field == 'XY':
                continue
            if isinstance(node.__dict__[field], ast.AST):
                node.__dict__[field] = astunparse.unparse(node.__dict__[field]).replace('\n', '')
            elif type(node.__dict__[field]) == list and isinstance(node.__dict__[field][0], ast.AST):
                node.__dict__[field] = astunparse.unparse(node.__dict__[field]).replace('\n', '')

        sentence = f"self.{node.name} = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['{node.layer}'][0],\
 _Datatype = DesignParameters._LayerMapping['{node.layer}'][1], _Presentation = {node.pres}, _Reflect = {node.reflect}, _XYCoordinates = {node.XY},\
 _Mag = {node.magnitude}, _Angle = {node.angle}, _TEXT = '{node.text}')"
        print(sentence)
        tmp = ast.parse(sentence)
        return tmp.body[0]

def run_transformer(source_ast):
    module_ast = ast.Module()
    if type(source_ast) == list:
        module_ast.body = copy.deepcopy(source_ast)
    else:
        module_ast.body = copy.deepcopy([source_ast])
    # result_ast = variable_ast.IrregularTransformer().visit(module_ast)
    # result_ast = element_ast.ElementTransformer().visit(result_ast)
    result_ast = variable_ast.IrregularTransformer().visit(module_ast)
    result_ast = variable_ast.VariableTransformer().visit(result_ast)
    return result_ast