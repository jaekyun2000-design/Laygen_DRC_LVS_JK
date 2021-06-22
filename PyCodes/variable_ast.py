import ast
import astunparse

custom_ast_list = ['GeneratorVariable', 'LogicExpression', 'ElementArray','DynamicElementArray','Distance',
                   'ArgumentVariable', 'LogicExpression', 'XYCoordinate']



class GeneratorVariable(ast.AST):
    def __init__(self, *args, **kwargs):
        pass

    _fields = (
    )

class LogicExpression(GeneratorVariable):
    """
    LogicExpression class:
    Variable declaration with initial deterministic value
    Usage: 'name' = 'logic expression'
    """
    def __init__(self, *args, **kwargs):
        super().__init__()
    _fields = (
        'name',     # str
        'value',    # str
    )
class XYCoordinate(GeneratorVariable):

    def __init__(self, *args, **kwargs):
        super().__init__()
    _fields = (
        'id',     #str
    )

class ArgumentVariable(GeneratorVariable):
    """
    ArgumentVariable class:
    Argument declaration with empty value space
    values will be assigned @ runtime referring Variable Manager administrated values
    """
    def __init__(self, *args, **kwargs):
        super().__init__()
    _fields = (
        'name',      # str
    )
class ElementArray(GeneratorVariable):
    """
    ElementArray class:
    Array declaration
    encoded python code will be expressed w/ a loop
    """
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
        if type(node.XY) ==str:
            sentence = f"for (i, element) in enumerate({node.elements}):\
                        \tself._DesignParameter[element]['_XYCoordinates'] = [({node.XY}[0][0] + (i * {node.x_space_distance})), ({node.XY}[0][1] + (i * {node.y_space_distance}))]"
        else:
            sentence = f"for (i, element) in enumerate({node.elements}):\
            \tself._DesignParameter[element]['_XYCoordinates'] = [({node.XY[0][0]} + (i * {node.x_space_distance})), ({node.XY[0][1]} + (i * {node.y_space_distance}))]"
        # print(sentence)
        tmp = ast.parse(sentence)
        return tmp.body

    def visit_LogicExpression(self,node):
        sentence = f"{node.name} = {node.value}"
        # print(sentence)
        tmp = ast.parse(sentence)
        return tmp.body

    def visit_ArgumentVariable(self,node):
        sentence = f"{node.name} = None"
        tmp = ast.parse(sentence)
        return tmp.body

    def visit_XYCoordinate(self, node):

        pass


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