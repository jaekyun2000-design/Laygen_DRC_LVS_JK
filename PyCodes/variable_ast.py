import ast
import astunparse
import re
import copy

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

class IrregularTransformer(ast.NodeTransformer):
    def __init__(self, _id_to_data_dict):
        if not _id_to_data_dict:
            raise Exception("Not valid input")
        self._id_to_data_dict = _id_to_data_dict

    def visit_XYCoordinate(self,node):
        _id = node._id
        tmpDict = dict()
        tmpDict['X'] = []
        tmpDict['Y'] = []
        tmpDict['XY'] = []
        final_x_value = None
        final_y_value = None

        # for XYFlag, elements in self._id_to_data_dict.items():
        for XYFlag, elements in self._id_to_data_dict.XYDict[_id].items():
            for j in range(len(elements)):
                expression = elements[j]
                operands_with_operators_list = re.split(' ', expression)
                for i in range(len(operands_with_operators_list)):
                    isFunction = re.search('\(\[\'.*\'\]\)', operands_with_operators_list[i])
                    if isFunction != None:
                        re_expressed_element = self.expressionTransformer(operands_with_operators_list[i],
                                                                          XYFlag=XYFlag)
                        operands_with_operators_list[i] = re_expressed_element
                    else:
                        pass
                if XYFlag != 'XY':
                    intermediateCode = ' '.join(operands_with_operators_list)
                elif XYFlag == 'XY':
                    # X_calc
                    x_list = copy.deepcopy(operands_with_operators_list)
                    for i in range(len(x_list)):
                        if type(x_list[i]) == list:
                            x_list[i] = x_list[i][0]
                    # Y_calc
                    y_list = copy.deepcopy(operands_with_operators_list)
                    for i in range(len(y_list)):
                        if type(y_list[i]) == list:
                            y_list[i] = y_list[i][1]
                    X_expression = ' '.join(x_list)
                    Y_expression = ' '.join(y_list)
                    intermediateCode = list()
                    intermediateCode.append(X_expression)
                    intermediateCode.append(Y_expression)

                tmpDict[XYFlag].append(intermediateCode)

        for i in range(len(tmpDict['X'])):
            if final_x_value == None:
                final_x_value = tmpDict['X'][i]
            else:
                final_x_value = tmpDict['X'][i] + ' + ' + final_x_value
        for j in range(len(tmpDict['Y'])):
            if final_y_value == None:
                final_y_value = tmpDict['Y'][j]
            else:
                final_y_value = tmpDict['Y'][j] + ' + ' + final_y_value
        for k in range(len(tmpDict['XY'])):
            if final_x_value == None:
                final_x_value = tmpDict['XY'][k][0]
                if final_y_value == None:       # XY input initially
                    final_y_value = tmpDict['XY'][k][1]
                elif final_y_value != None:
                    final_y_value = tmpDict['XY'][k][1] + ' + ' + final_y_value
            elif final_x_value != None:
                final_x_value = tmpDict['XY'][k][0] + ' + ' + final_x_value
                if final_y_value == None:
                    final_y_value = tmpDict['XY'][k][1]
                elif final_y_value != None:
                    final_y_value = tmpDict['XY'][k][1] + ' + ' + final_y_value

        if final_x_value == None or final_y_value == None:
            print("X field and Y field both should not be empty")
            raise Exception("X field and Y field both should not be empty")

        sentence = []
        sentence.append(final_x_value)
        sentence.append(final_y_value)
        sentence = '[['+final_x_value+','+final_y_value+']]'
        # sentence = f"'{sentence}'"
        # return list(sentence)
        # print(sentence)
        tmp = ast.parse(sentence)
        return tmp.body

    def expressionTransformer(self, expression, XYFlag):
        """
        :param expression: code to be re-expressed
        :param XYFlag: Which mode is checked?
        :return: re-expressed code
        """
        function = expression[0:2]
        if function == 'to':
            function = 'top'
        elif function == 'bo':
            function = 'bottom'
        elif function == 'le':
            function = 'left'
        elif function == 'ri':
            function = 'right'
        elif function == 'ce':
            function = 'center'
        elif function == 'wi':
            function = 'width'
        elif function == 'he':
            function = 'height'

        operands = re.split(',', re.sub(f'{function}|\(|\'|\)|\[|]', "", expression))
        # TODO Variable 이름에 function sequence가 들어갔을 때 어떻게 제거하지 않고 두느냐
        code = 'self.'                  # Code Always Starts with 'self.' string
        layer = operands[-1]
        objects = operands[0: len(operands)-1]
        for i in range(len(objects)):           # append code from the start
            code = code + f"_DesignParameter['{objects[i]}']['_DesignObj']."
        code = code + f"_DesignParameter['{layer}']"
        if function == 'width':
            result = code + '[\'_XWidth\']'
        elif function == 'height':
            result = code + '[\'_YWidth\']'

        if XYFlag == 'X':
            if function == 'lt' or function == 'left' or function == 'lb':
                result = f"{code}['_XYCoordinates'][0][0] - {code}['_XWidth']/2"
            elif function == 'top' or function == 'bottom' or function == 'center':
                result = f"{code}['_XYCoordinates'][0][0]"
            elif function == 'rt' or function == 'right' or function == 'rb':
                result = f"{code}['_XYCoordinates'][0][0] + {code}['_XWidth']/2"
            else:   # Width or Height case
                print(f" XYFlag Redundant: input function: {function}, XYFlag = {XYFlag} for Debugging")
        elif XYFlag == 'Y':
            if function == 'lt' or function == 'rt' or function == 'top':
                result = f"{code}['_XYCoordinates'][0][1] + {code}['_YWidth']/2"
            elif function == function == 'left' or function == 'right' or function == 'center':
                result = f"{code}['_XYCoordinates'][0][1]"
            elif function == function == 'lb' or function == 'rb' or function == 'bottom':
                result = f"{code}['_XYCoordinates'][0][0] - {code}['_YWidth']/2"
            else:   # Width or Height case
                print(f" XYFlag Redundant: input function: {function}, XYFlag = {XYFlag} for Debugging")
                pass
        elif XYFlag == 'XY':
        # X Input first
            if function == 'lt' or function == 'left' or function == 'lb':
                result = f"{code}['_XYCoordinates'][0][0] - {code}['_XWidth']/2"
            elif function == function == 'top' or function == 'bottom' or function == 'center':
                result = f"{code}['_XYCoordinates'][0][0]"
            elif function == 'rt' or function == 'right' or function == 'rb':
                result = f"{code}['_XYCoordinates'][0][0] + {code}['_XWidth']/2"
            else:   # Width or Height case
                print(f" XYFlag Redundant: input function: {function}, XYFlag = {XYFlag}_X for Debugging")
        # Y input afterwards
            if function == 'lt' or function == 'rt' or function == 'top':
                result = result + f", {code}['_XYCoordinates'][0][1] + {code}['_YWidth']/2"
            elif function == 'left' or function == 'right' or function == 'center':
                result = result + f", {code}['_XYCoordinates'][0][1]"
            elif function == 'lb' or function == 'rb' or function == 'bottom':
                result = result + f", {code}['_XYCoordinates'][0][0] - {code}['_YWidth']/2"
            else:  # Width or Height case
                print(f" XYFlag Redundant: input function: {function}, XYFlag = {XYFlag}_Y for Debugging")
            if (function != 'width') & (function != 'height'):
                result = re.split(',', result)
        print(f"Re-Expressed Element: \n{result}")
        return result


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