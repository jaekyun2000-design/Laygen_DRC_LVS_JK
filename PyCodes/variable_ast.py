import ast
import warnings

import astunparse
import re
import copy
from PyCodes import element_ast

custom_ast_list = ['GeneratorVariable', 'LogicExpression', 'ElementArray','DynamicElementArray','Distance',
                   'ArgumentVariable', 'XYCoordinate', 'PathXY', 'Array']



class GeneratorVariable(ast.AST):
    def __init__(self, *args, **kwargs):
        pass

    _fields = (
    )

class LogicExpression(GeneratorVariable):
    """
    LogicExpression class:
    Variable declaration with initial deterministic value
    Usage: 'logic expression'
    """
    def __init__(self, *args, **kwargs):
        super().__init__()
    _fields = (
        'id',    # str
    )
class XYCoordinate(GeneratorVariable):
    def __init__(self, *args, **kwargs):
        super().__init__()
    _fields = (
        'id',       # str
    )

class Array(GeneratorVariable):
    def __init__(self, *args, **kwargs):
        super().__init__()
    _fields = (
        'id',    # str
    )

class PathXY(GeneratorVariable):
    def __init__(self, *args, **kwargs):
        super().__init__()

    _fields = (
        'id',  # str
    )

class ConditionSTMTlist(GeneratorVariable):
    def __init__(self):
        super().__init__()

    _fields = (
        'body',
    )

class ConditionSTMT(GeneratorVariable):
    def __init__(self):
        super().__init__()

    _fields = (
        'c_type',
        'expression',
        'body',
    )


class ConditionExpression(GeneratorVariable):
    def __init__(self):
        super().__init__()

    _fields = (
        'variable',
        'operator',
        'condition',
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

class PathArray(GeneratorVariable):
    """
        PathArray class:
        Array declaration for path
        encoded python code will be expressed w/ a loop
        """

    def __init__(self, *args, **kwargs):
        super().__init__()

    _fields = (
        'name',
        'XY_source_ref',
        'XY_target_ref',
        'width',
        'layer',
        'index',
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
    def __init__(self):
        pass
        # if not _id_to_data_dict:
        #     raise Exception("Not valid input")
        # self._id_to_data_dict = _id_to_data_dict

    def visit_XYCoordinate(self, node):
        x_list = []
        y_list = []
        xy_list = []
        for xy_flag, elements in node.info_dict.items():
            tf =CustomFunctionTransformer(xy_flag)
            if xy_flag == 'X':
                x_list.extend([tf.visit(ast.parse(element).body[0]) for element in elements])
            elif xy_flag == 'Y':
                y_list.extend([tf.visit(ast.parse(element).body[0]) for element in elements])
            elif xy_flag == 'XY':
                xy_list.extend([tf.visit(ast.parse(element).body[0]) for element in elements])

        x_string = "+".join([astunparse.unparse(x_ast) for x_ast in x_list])
        y_string = "+".join([astunparse.unparse(y_ast) for y_ast in y_list])

        xy_x_string_list = [astunparse.unparse(xy_ast.value.value.elts[0]) for xy_ast in xy_list]
        xy_y_string_list = [astunparse.unparse(xy_ast.value.value.elts[1]) for xy_ast in xy_list]

        xy_x_string = "+".join(xy_x_string_list)
        xy_y_string = "+".join(xy_y_string_list)

        final_x_string = f'{x_string} + {xy_x_string}' if xy_x_string else x_string
        final_y_string = f'{y_string} + {xy_y_string}' if xy_y_string else y_string

        if final_x_string and final_y_string:
            final_string = f"[[{final_x_string}, {final_y_string}]]"
            final_ast = ast.parse(final_string).body[0]
            return final_ast
        else:
            raise Exception("Not Enough XY coordinates information!")



    def visit_XYCoordinate_legacy(self,node):
        if type(node.id) == list:
            _id = node.id[0]
        else:
            _id = node.id
        tmpDict = dict()
        tmpDict['X'] = []
        tmpDict['Y'] = []
        tmpDict['XY'] = []
        final_x_value = None
        final_y_value = None

        # for XYFlag, elements in self._id_to_data_dict.items():
        # When PathXY transformer called this function,
        # for XYFlag, elements in self._id_to_data_dict.XYDict[_id].items():
        for XYFlag, elements in node.info_dict.items():

            for j in range(len(elements)):
                expression = elements[j]
                operands_with_operators_list = re.split(' ', expression)
                for i in range(len(operands_with_operators_list)):
                    isFunction = re.search('\(\'.*\'\)', operands_with_operators_list[i])
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
            if final_x_value == None and final_y_value == None:
                raise Exception("X and Y value both empty")
            elif final_x_value == None:
                final_x_value = self.old_x_value
            elif final_y_value == None:
                final_y_value = self.old_y_value

        self.old_x_value = final_x_value
        self.old_y_value = final_y_value
        sentence = []
        sentence.append(final_x_value)
        sentence.append(final_y_value)
        sentence = '[['+final_x_value+','+final_y_value+']]'
        tmp = ast.parse(sentence)
        return tmp.body

    def visit_PathXY(self, node):
        if type(node.id) == list:
            _id = node.id[0]
        else:
            _id = node.id

        memory_xy_ast = None
        xy_list = []
        for xy_ast in node.info_dict.values():
            if (xy_ast.info_dict['X'] and xy_ast.info_dict['Y']) or xy_ast.info_dict['XY']:
                memory_xy_ast = xy_ast
                xy_list.append(xy_ast)
            elif xy_ast.info_dict['X']:
                memory_y = memory_xy_ast.info_dict['Y']
                memory_y.extend(memory_xy_ast.info_dict['XY'])
                tmp_ast = copy.deepcopy(xy_ast)
                tmp_ast.info_dict['Y'].extend(memory_y)
                memory_xy_ast = tmp_ast
                xy_list.append(tmp_ast)
            elif xy_ast.info_dict['Y']:
                memory_x = memory_xy_ast.info_dict['X']
                memory_x.extend(memory_xy_ast.info_dict['XY'])
                tmp_ast = copy.deepcopy(xy_ast)
                tmp_ast.info_dict['X'].extend(memory_x)
                memory_xy_ast = tmp_ast
                xy_list.append(tmp_ast)

        converted_xy_ast_list = [self.visit_XYCoordinate(xy_ast) for xy_ast in xy_list]
        sentenced_xy_list = ",".join([astunparse.unparse(xy_ast)[2:-2] for xy_ast in converted_xy_ast_list])
        final_sentence = f"[[{sentenced_xy_list}]]"
        final_ast = ast.parse(final_sentence).body
        return final_ast

    def visit_PathXYLegacy(self, node):
        if type(node.id) == list:
            _id = node.id[0]
        else:
            _id = node.id
        sentence = '['
        # for _, elementIdList in self._id_to_data_dict.XYPathDict[_id].items():
        for sub_ast_id, ast_obj in node.info_dict.items():
                tmp_code_ast = self.visit_XYCoordinate(ast_obj)
                tmp_code = astunparse.unparse(tmp_code_ast)
                tmp_code = tmp_code[2:-2]
                sentence = sentence + tmp_code + ',\n'

        sentence = sentence[:-2] + ']'
        final_tripleList = '[' +sentence+ ']'
        tmp = ast.parse(final_tripleList)
        return tmp.body

    def visit_LogicExpression(self, node):
        expression_list = []
        for xy_flag, elements in node.info_dict.items():
            if not elements:
                continue
            tf = CustomFunctionTransformer(xy_flag)
            expression_list.extend([tf.visit(ast.parse(element).body[0]) for element in elements])
        final_string = "+".join([astunparse.unparse(exp_ast).replace("\n","") for exp_ast in expression_list])
        final_ast = ast.parse(final_string).body
        return final_ast


    def visit_LogicExpressionLegacy(self,node):
        _id = node.id
        tmpDict = dict()
        tmpDict['X'] = []
        tmpDict['Y'] = []
        final_x_value = None
        final_y_value = None
        # for XYFlag, elements in self._id_to_data_dict.ExpressionDict[_id].items():
        for XYFlag, elements in node.info_dict.items():
            if len(elements) == 0:
                pass
            else:
                for i in range(len(elements)):
                    expression = elements[i]
                    operands_with_operators_list = re.split(' ', expression)
                    for j in range(len(operands_with_operators_list)):
                        isFunction =  re.search('\(\'.*\'\)', operands_with_operators_list[j])
                        if isFunction != None:
                            re_expressed_element = self.expressionTransformer(operands_with_operators_list[j],
                                                                              XYFlag=XYFlag)
                            operands_with_operators_list[j] = re_expressed_element
                        else:
                            pass
                    if XYFlag == 'XY':
                        continue
                    else:
                        intermediateCode = ' '.join(operands_with_operators_list)
                        tmpDict[XYFlag].append(intermediateCode)


        for i in range(len(tmpDict['X'])):
            if final_x_value == None:
                final_x_value = tmpDict['X'][i]
            else:
                final_x_value = tmpDict['X'][i] + ' + ' + final_x_value

        sentence1 = final_x_value
        if  sentence1 == None:
            sentence1 = '0'


        for j in range(len(tmpDict['Y'])):
            if final_y_value == None:
                final_y_value = tmpDict['Y'][j]
            else:
                final_y_value = tmpDict['Y'][j] + ' + ' + final_y_value
        sentence2 = final_y_value
        if sentence2 == None:
            sentence2 = '0'

        sentence = '(' +sentence1+ '+' +sentence2+ ')'
        tmp = ast.parse(sentence)
        return tmp.body

    def visit_Array(self, node):
        _id = node.id
        # info_dict = self._id_to_data_dict.ArrayDict[_id]
        info_dict = node.info_dict
        _width = ''
        _height = ''
        for key in info_dict.keys():
            if isinstance(info_dict[key], ast.AST):
                # tmpAST = IrregularTransformer(self._id_to_data_dict).visit(info_dict[key])
                tmpAST = IrregularTransformer().visit(info_dict[key])
                sentence = astunparse.unparse(tmpAST)
                info_dict[key] = sentence

        ############ Common Elements ################
        _name = info_dict['name']               # Fixed
        _type = info_dict['type']              # Fixed
        _flag = info_dict['flag']     # Fixed
        _width = info_dict['width']
        _layer = info_dict['layer']
        if _type != "path_array":
            _height = info_dict['height']
        try:
            XY_source_ref = info_dict['XY_source_ref']
        except:
            XY_source_ref = info_dict['XY_ref']
        ###############################################
        if _flag == 'relative':
            ########### Elements For relative #############
            _index = info_dict['index']
            if _index == 'Custom':
                _index = info_dict['index_input'].split(',')
            if _type == 'path_array':
                XY_target_ref = info_dict['XY_target_ref']   # For Path
            ###############################################
        else:
            ############ Elements For Offset ##############
            _XY_ref = info_dict['XY_ref']
            _x_distance = info_dict['x_offset']     # Fixed
            _y_distance = info_dict['y_offset']     # Fixed
            _row_num = info_dict['row']             # Fixed
            _col_num = info_dict['col']             # Fixed
            ###############################################

        ####### XY Coordinate, Width, Height Extraction @ Layout Generator Source Code ######
        if _flag == "relative":
            if "," in XY_source_ref:
                source_wo_layer = ",".join(XY_source_ref.split(",")[:-1]) + ')'
                parent_xy = self.expressionTransformer(source_wo_layer, 'XY')
                parent_xy = "[" + parent_xy[0] + ',' + parent_xy[1] + "]"

            else:
                parent_xy = '[0,0]'

            tmp_string = re.findall('\(.*\)', XY_source_ref)[0]
            tmp_string = re.sub('\(|\'|\)', "", tmp_string)
            tmp_string = re.sub(" ", "" , tmp_string)
            operands = re.split(',', tmp_string)
            # above operands include indices

            code = 'self.'
            offset_indices = []
            objects = operands[:-1]
            for i in range(len(objects)):  # append code from the start
                offset_indices.append(re.findall('\[.*\]', objects[i])[0])
                object = objects[i][:-len(offset_indices[i])]
                code = code + f"_DesignParameter['{object}']['_DesignObj']."
            layer = operands[-1]

            layer_xy = code + f"_DesignParameter['{layer}']" + '[\'_XYCoordinates\']'
            _width_code = code + f"_DesignParameter['{layer}']" + '[\'_XWidth\']'
            _height_code = code + f"_DesignParameter['{layer}']" + '[\'_YWidth\']'

            ########################### for path array ############################
            if _type == "path_array":
                target_xy = self.expressionTransformer(XY_target_ref, 'XY')
                tmp_string2 = re.findall('\(.*\)', XY_target_ref)[0]
                tmp_string2 = re.sub('\(|\'|\)', "", tmp_string2)
                tmp_string2 = re.sub(" ", "", tmp_string2)
                operands2 = re.split(',', tmp_string2)
                # above operands include indices

                code2 = 'self.'
                offset_indices = []
                objects = operands2[:-1]
                for i in range(len(objects)):  # append code from the start
                    offset_indices.append(re.findall('\[.*\]', objects[i])[0])
                    object = objects[i][:-len(offset_indices[i])]
                    code2 = code2 + f"_DesignParameter['{object}']['_DesignObj']."
                layer_with_index2 = operands2[-1]
                layer_index2 = re.findall('\[.*\]', layer_with_index2)[0]
                layer2 = layer_with_index2[:-len(layer_index2)]

                _target_layer_xy = code2 + f"_DesignParameter['{layer2}']" + '[\'_XYCoordinates\']'
                _target_width_code = code2 + f"_DesignParameter['{layer2}']" + '[\'_XWidth\']'
                _target_height_code = code2 + f"_DesignParameter['{layer2}']" + '[\'_YWidth\']'
            ###########################################################################

            if info_dict['width'] == 'Auto':  # If Width is 'Auto', height should be fixed.
                if _type == 'path_array':
                    _width = _width_code
                elif _type == 'boundary_array':
                    # Width : Auto, height: Value
                    _width = _width_code
                    _height = info_dict['height_input']
                elif _type == 'sref_array':
                    _width = 'Blank'
                    _height = 'Blank'
            else:  # If _width is not 'Auto', height can either be 'Auto' or Fixed
                _width = info_dict['width_input']
                if _type == 'path_array':   # path does not have 'height' input
                    pass
                elif _type == 'boundary_array':
                    if info_dict['height'] == 'Auto':
                        _height = _height_code
                    else:
                        _height = info_dict["height_input"]
                elif _type == 'sref_array':
                    _width = 'Blank'
                    _height = 'Blank'

            if _width == '':
                _width = info_dict['width_text']
            _width = re.sub("\n", "", _width)
            print(f"width for {node.id} = {_width}")

            if _height == '':
                _height = info_dict['height_text']
            _height = re.sub("\n", "", _height)
            print(f"height for {node.id} = {_height}")

            ################### Width, height, Coordinates Calculation Done ########################

            if _type == 'boundary_array':
                if _index == 'All':
                    loop_code = f"XYList = []\n" \
                                f"for i in range(len({layer_xy})):\n" \
                                f"\tXYList.append([x+y for x,y in zip({parent_xy} , {layer_xy}[i] ) ] )\n"
                elif _index == 'Odd':
                    loop_code = f"XYList = []\n" \
                                f"for i in range(len({layer_xy})):\n" \
                                f"\tif (i%2 == 1):\n" \
                                f"\t\tXYList.append([x+y for x,y in zip({parent_xy} , {layer_xy}[i] ) ] )\n"
                elif _index == 'Even':
                    loop_code = f"XYList = []\n" \
                                f"for i in range(len({layer_xy})):\n" \
                                f"\tif (i%2 == 0):\n" \
                                f"\t\tXYList.append([x+y for x,y in zip({parent_xy} , {layer_xy}[i] ) ] )\n"

                tmp_node = element_ast.Boundary()
                tmp_node.name = _name
                tmp_node.layer = _layer
                tmp_node.XY = 'XYList'
                tmp_node.width = _width
                tmp_node.height = _height
                tmp_code_ast = element_ast.ElementTransformer().visit_Boundary(tmp_node)
                tmp_code = astunparse.unparse(tmp_code_ast)

                sentence = loop_code + '\n' + tmp_code
                del tmp_node
            elif _type == 'path_array':
                comparison_code = f"\npath_list = []\n" \
                                  f"if ({layer_xy}[0][0] == {layer_xy}[-1][0]) :\n" \
                                  f"\tmode = 'horizontal'\n" \
                                  f"\t_width = {_width}\n" \
                                  f"elif ({layer_xy}[0][1] == {layer_xy}[-1][1]) :\n" \
                                  f"\tmode = 'vertical'\n" \
                                  f"\t_width = {_width}\n" \
                                  f"else:\n" \
                                  f"\tprint('Invalid Target Input')\n"
                if _index == 'All':
                    case_code = f"if mode == 'vertical':\n" \
                                f"\txy_with_offset = []\n" \
                                f"\ttarget_y_value = {target_xy[1]}\n" \
                                f"\tfor i in range(len({layer_xy})):\n" \
                                f"\t\txy_with_offset.append([x+y for x,y in zip({parent_xy} , {layer_xy}[i])])\n" \
                                f"\n" \
                                f"\tfor i in range(len(xy_with_offset)):\n" \
                                f"\t\tpath_list.append([xy_with_offset[i],[xy_with_offset[i][0],target_y_value]])\n" \
                                f"elif mode == 'horizontal':\n" \
                                f"\txy_with_offset = []\n" \
                                f"\ttarget_x_value = {target_xy[0]}\n" \
                                f"\tfor i in range(len({layer_xy})):\n" \
                                f"\t\txy_with_offset.append([x+y for x,y in zip({parent_xy} , {layer_xy}[i])])\n" \
                                f"\n" \
                                f"\tfor i in range(len(xy_with_offset)):\n" \
                                f"\t\tpath_list.append([xy_with_offset[i],[target_x_value, xy_with_offset[i][1]]])\n"
                elif _index == 'Odd':
                    case_code = f"if mode == 'vertical':\n" \
                                f"\txy_with_offset = []\n" \
                                f"\ttarget_y_value = {target_xy[1]}\n" \
                                f"\tfor i in range(len({layer_xy})):\n" \
                                f"\t\tif (i%2 == 1):\n" \
                                f"\t\t\txy_with_offset.append([x+y for x,y in zip({parent_xy} , {layer_xy}[i])])\n" \
                                f"\n" \
                                f"\tfor i in range(len(xy_with_offset)):\n" \
                                f"\t\tpath_list.append([xy_with_offset[i],[xy_with_offset[i][0],target_y_value]])\n" \
                                f"elif mode == 'horizontal':\n" \
                                f"\txy_with_offset = []\n" \
                                f"\ttarget_x_value = {target_xy[0]}\n" \
                                f"\tfor i in range(len({layer_xy})):\n" \
                                f"\t\tif (i%2 == 1):\n" \
                                f"\t\t\txy_with_offset.append([x+y for x,y in zip({parent_xy} , {layer_xy}[i])])\n" \
                                f"\n" \
                                f"\tfor i in range(len(xy_with_offset)):\n" \
                                f"\t\tpath_list.append([xy_with_offset[i],[target_x_value, xy_with_offset[i][1]]])\n"
                elif _index == 'Even':
                    case_code = f"if mode == 'vertical':\n" \
                                f"\txy_with_offset = []\n" \
                                f"\ttarget_y_value = {target_xy[1]}\n" \
                                f"\tfor i in range(len({layer_xy})):\n" \
                                f"\t\tif (i%2 == 0):\n" \
                                f"\t\t\txy_with_offset.append([x+y for x,y in zip({parent_xy} , {layer_xy}[i])])\n" \
                                f"\n" \
                                f"\tfor i in range(len(xy_with_offset)):\n" \
                                f"\t\tpath_list.append([xy_with_offset[i],[xy_with_offset[i][0],target_y_value]])\n" \
                                f"elif mode == 'horizontal':\n" \
                                f"\txy_with_offset = []\n" \
                                f"\ttarget_x_value = {target_xy[0]}\n" \
                                f"\tfor i in range(len({layer_xy})):\n" \
                                f"\t\tif (i%2 == 0):\n" \
                                f"\t\t\txy_with_offset.append([x+y for x,y in zip({parent_xy} , {layer_xy}[i])])\n" \
                                f"\n" \
                                f"\tfor i in range(len(xy_with_offset)):\n" \
                                f"\t\tpath_list.append([xy_with_offset[i],[target_x_value, xy_with_offset[i][1]]])\n"
                else:       # Custom Index
                    case_code = f"if mode == 'vertical':\n" \
                                f"\txy_with_offset = []\n" \
                                f"\ttarget_y_value = {target_xy[1]}\n" \
                                f"\tfor i in range(len({layer_xy})):\n" \
                                f"\t\tif i in {_index}:\n" \
                                f"\t\t\txy_with_offset.append([x+y for x,y in zip({parent_xy} , {layer_xy}[i])])\n" \
                                f"\n" \
                                f"\tfor i in range(len(xy_with_offset)):\n" \
                                f"\t\tpath_list.append([xy_with_offset[i],[xy_with_offset[i][0],target_y_value]])\n" \
                                f"elif mode == 'horizontal':\n" \
                                f"\txy_with_offset = []\n" \
                                f"\ttarget_x_value = {target_xy[0]}\n" \
                                f"\tfor i in range(len({layer_xy})):\n" \
                                f"\t\tif i in {_index}:\n" \
                                f"\t\t\txy_with_offset.append([x+y for x,y in zip({parent_xy} , {layer_xy}[i])])\n" \
                                f"\n" \
                                f"\tfor i in range(len(xy_with_offset)):\n" \
                                f"\t\tpath_list.append([xy_with_offset[i],[target_x_value, xy_with_offset[i][1]]])\n"
                tmp_node = element_ast.Path()
                tmp_node.name = _name
                tmp_node.layer = _layer
                tmp_node.XY = 'path_list'
                tmp_node.width = '_width'
                tmp_code_ast = element_ast.ElementTransformer().visit_Path(tmp_node)
                tmp_code = astunparse.unparse(tmp_code_ast)
                sentence = comparison_code + case_code + tmp_code
                del tmp_node
            elif _type == 'sref_array':
                if _index == 'All':
                    loop_code = f"XYList = []\n" \
                                f"for i in range(len({layer_xy})):\n" \
                                f"\tXYList.append([x+y for x,y in zip({parent_xy} , {layer_xy}[i] ) ] )\n"
                elif _index == 'Odd':
                    loop_code = f"XYList = []\n" \
                                f"for i in range(len({layer_xy})):\n" \
                                f"\tif (i%2 == 1):\n" \
                                f"\t\tXYList.append([x+y for x,y in zip({parent_xy} , {layer_xy}[i] ) ] )\n"
                elif _index == 'Even':
                    loop_code = f"XYList = []\n" \
                                f"for i in range(len({layer_xy})):\n" \
                                f"\tif (i%2 == 0):\n" \
                                f"\t\tXYList.append([x+y for x,y in zip({parent_xy} , {layer_xy}[i] ) ] )\n"

                tmp_node = element_ast.Sref()
                tmp_node.name = _name
                tmp_node.XY = 'XYList'
                tmp_node.library = info_dict['sref_item_dict']['library']
                tmp_node.className = info_dict['sref_item_dict']['className']
                tmp_node.calculate_fcn = info_dict['sref_item_dict']['calculate_fcn']
                tmp_node.parameters = info_dict['sref_item_dict']['parameters']
                tmp_code_ast = element_ast.ElementTransformer().visit_Sref(tmp_node)
                tmp_code = astunparse.unparse(tmp_code_ast)

                sentence = loop_code + '\n' + tmp_code
                del tmp_node
        ###############################################################################################################
        ###############################################################################################################
        ###############################################################################################################
        ###############################################################################################################
        elif _flag == 'offset':
            if "," in XY_source_ref:
                source_wo_layer = ",".join(XY_source_ref.split(",")[:-1]) + ')'
                parent_xy = self.expressionTransformer(source_wo_layer, 'XY')
                parent_xy = "[" + parent_xy[0] + ',' + parent_xy[1] + "]"

            else:
                parent_xy = '[0,0]'

            tmp_string = re.findall('\(.*\)', XY_source_ref)[0]
            tmp_string = re.sub('\(|\'|\)', "", tmp_string)
            tmp_string = re.sub(" ", "", tmp_string)
            operands = re.split(',', tmp_string)
            # above operands include indices

            code = 'self.'
            offset_indices = []
            objects = operands[:-1]
            for i in range(len(objects)):  # append code from the start
                offset_indices.append(re.findall('\[.*\]', objects[i])[0])
                object = objects[i][:-len(offset_indices[i])]
                code = code + f"_DesignParameter['{object}']['_DesignObj']."
            layer = operands[-1]

            layer_xy = code + f"_DesignParameter['{layer}']" + '[\'_XYCoordinates\']'
            _width_code = code + f"_DesignParameter['{layer}']" + '[\'_XWidth\']'
            _height_code = code + f"_DesignParameter['{layer}']" + '[\'_YWidth\']'

            if info_dict['width'] == 'Auto':  # If Width is 'Auto', height should be fixed.
                if _type == 'path_array':
                    pass
                elif _type == 'boundary_array':
                    # Width : Auto, height: Value
                    _width = _width_code
                    _height = info_dict['height_input']
                elif _type == 'sref_array':
                    _width = 'Blank'
                    _height = 'Blank'
            else:  # If _width is not 'Auto', height can either be 'Auto' or Fixed
                _width = info_dict['width_input']
                if _type == 'path_array':  # path does not have 'height' input
                    pass
                elif _type == 'boundary_array':
                    if info_dict['height'] == 'Auto':
                        _height = _height_code
                    else:
                        _height = info_dict["height_input"]
                elif _type == 'sref_array':
                    _width = 'Blank'
                    _height = 'Blank'

            source_XY_code = parent_xy + '+' + layer_xy

        ################### Width, height, Coordinates Calculation Done ########################
        if _flag == 'offset':
            if _type == 'boundary_array':
                loop_code = f"XYList = []\n" \
                            f"for i in range({_row_num}):\n" \
                            f"\tfor j in range({_col_num}):\n" \
                            f"\t\tXYList.append([x+y for x,y in zip({source_XY_code} , [{_x_distance}, {_y_distance}])\n"

                tmp_node = element_ast.Boundary()
                tmp_node.name = _name
                tmp_node.layer = _layer
                tmp_node.XY = 'XYList'
                tmp_node.width = _width
                tmp_node.height = _height
                tmp_code_ast = element_ast.ElementTransformer().visit_Boundary(tmp_node)
                tmp_code = astunparse.unparse(tmp_code_ast)

                sentence = loop_code + '\n' + tmp_code
                del tmp_node
            elif _type == 'path_array':
                # loop_code
                pass
            elif _type == 'sref_array':
                loop_code = loop_code = f"XYList = []\n" \
                            f"for i in range({_row_num}):\n" \
                            f"\tfor j in range({_col_num}):\n" \
                            f"\t\tXYList.append([x+y for x,y in zip({source_XY_code} , [{_x_distance}, {_y_distance}])\n"
            tmp_node = element_ast.Sref()
            tmp_node.name = _name
            tmp_node.XY = 'XYList'
            tmp_node.library = info_dict['sref_item_dict']['library']
            tmp_node.className = info_dict['sref_item_dict']['className']
            tmp_node.calculate_fcn = info_dict['sref_item_dict']['calculate_fcn']
            tmp_node.parameters = info_dict['sref_item_dict']['parameters']
            tmp_code_ast = element_ast.ElementTransformer().visit_Sref(tmp_node)
            tmp_code = astunparse.unparse(tmp_code_ast)

            sentence = loop_code + '\n' + tmp_code
            del tmp_node



        return ast.parse(sentence).body
    def get_expression_del_func(self, expression):
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

        tmp_string = expression[len(function):]
        return tmp_string

    def expressionTransformer(self, expression, XYFlag):
        """
        :param expression: code to be re-expressed
        :param XYFlag: Which mode is checked?
        :return: re-expressed code
        """
        minus = True if expression[0] == '-' else False
        function_list = FunctionNameFinder().visit(ast.parse(expression))
        # tmp_str = re.sub("\(|\)", "", expression)
        # function = tmp_str[0:2]
        # if function == 'to':
        #     function = 'top'
        # elif function == 'bo':
        #     function = 'bottom'
        # elif function == 'le':
        #     function = 'left'
        # elif function == 'ri':
        #     function = 'right'
        # elif function == 'ce':
        #     function = 'center'
        # elif function == 'wi':
        #     function = 'width'
        # elif function == 'he':
        #     function = 'height'
        function = function_list[0]
        if XYFlag == 'FA':
            if function != ('width' or 'height'):
                raise Exception("Invalid Input, Debug")
            else:
                XYFlag = 'XY'
        tmp_string = re.sub('\(|\'|\)', "", expression)
        tmp_string = tmp_string[len(function):] if not minus else tmp_string[len(function)+1:]
        tmp_string = re.sub(" ","",tmp_string)
        operands = re.split(',', tmp_string)

        code = 'self.'  # Code Always Starts with 'self.' string
        offsets = []
        offset_indices = []
        layer_with_index = operands[-1]
        layer_index = re.findall('\[.*\]', layer_with_index)[0]
        layer = layer_with_index[:-len(layer_index)]
        objects = operands[0: len(operands) - 1]
        for i in range(len(objects)):  # append code from the start
            offset_indices.append(re.findall('\[.*\]', objects[i])[0])
            object = objects[i][:-len(offset_indices[i])]
            code = code + f"_DesignParameter['{object}']['_DesignObj']."
            offsets.append(code[:-15] + '[\'_XYCoordinates\']')

        if re.search("\[.+\][\[.+\]]+",layer_index) and function != 'center':
            print(f"Source '{expression}' includes Path Index: function '{function}' replaced into 'center' ")
            function = "center"


        code = code + f"_DesignParameter['{layer}']"
        offset_x = ''
        offset_y = ''

        for i in range(len(offsets)):
            offset_x += offsets[i] + f'{offset_indices[i]}[0]'
            offset_y += offsets[i] + f'{offset_indices[i]}[1]'
        if function == 'width':
            result = code + '[\'_XWidth\']'
        elif function == 'height':
            result = code + '[\'_YWidth\']'

        if offset_x == '':
            offset_x = '0'
        if offset_y == '':
            offset_y = '0'

        if XYFlag == 'X':
            if function == 'lt' or function == 'left' or function == 'lb':
                result = offset_x + ' +' + f"{code}['_XYCoordinates']{layer_index}[0] - {code}['_XWidth']/2"
            elif function == 'top' or function == 'bottom' or function == 'center':
                result = offset_x + ' +' + f"{code}['_XYCoordinates']{layer_index}[0]"
            elif function == 'rt' or function == 'right' or function == 'rb':
                result = offset_x + ' +' + f"{code}['_XYCoordinates']{layer_index}[0] + {code}['_XWidth']/2"
            else:   # Width or Height case
                print(f" XYFlag Redundant: input function: {function}, XYFlag = {XYFlag} for Debugging")
        elif XYFlag == 'Y':
            if function == 'lt' or function == 'rt' or function == 'top':
                result = offset_y + ' +' + f"{code}['_XYCoordinates']{layer_index}[1] + {code}['_YWidth']/2"
            elif function == function == 'left' or function == 'right' or function == 'center':
                result = offset_y + ' +' + f"{code}['_XYCoordinates']{layer_index}[1]"
            elif function == function == 'lb' or function == 'rb' or function == 'bottom':
                result = offset_y + ' +' + f"{code}['_XYCoordinates']{layer_index}[1] - {code}['_YWidth']/2"
            else:   # Width or Height case
                print(f" XYFlag Redundant: input function: {function}, XYFlag = {XYFlag} for Debugging")
                pass
        elif XYFlag == 'XY':
        # X Input first
            if function == 'lt' or function == 'left' or function == 'lb':
                result = offset_x + ' +' + f"{code}['_XYCoordinates']{layer_index}[0] - {code}['_XWidth']/2"
            elif function == function == 'top' or function == 'bottom' or function == 'center':
                result = offset_x + ' +' + f"{code}['_XYCoordinates']{layer_index}[0]"
            elif function == 'rt' or function == 'right' or function == 'rb':
                result = offset_x + ' +' + f"{code}['_XYCoordinates']{layer_index}[0] + {code}['_XWidth']/2"
            else:   # Width or Height case
                print(f" XYFlag Redundant: input function: {function}, XYFlag = {XYFlag}_X for Debugging")
        # Y input afterwards
            if function == 'lt' or function == 'rt' or function == 'top':
                result = result + f", {offset_y} + {code}['_XYCoordinates']{layer_index}[1] + {code}['_YWidth']/2"
            elif function == 'left' or function == 'right' or function == 'center':
                result = result + f", {offset_y} + {code}['_XYCoordinates']{layer_index}[1]"
            elif function == 'lb' or function == 'rb' or function == 'bottom':
                result = result + f", {offset_y} + {code}['_XYCoordinates']{layer_index}[1] - {code}['_YWidth']/2"
            else:  # Width or Height case
                print(f" XYFlag Redundant: input function: {function}, XYFlag = {XYFlag}_Y for Debugging")
            if (function != 'width') & (function != 'height'):
                result = re.split(',', result)
        if minus:
            result = f'-{result}'
        print(f"Re-Expressed Element: \n{result}")
        if type(result) == str:
            result = '(' + result + ')'
        return result

    def visit_ConditionSTMTlist(self, node):
        return_str = ''
        for stmt in node.body:
            stmt_py_ast = self.visit(stmt)
            if type(stmt_py_ast) == list:
                if type(stmt_py_ast[0]) != ast.If:
                    return_str += '\nelse:\n' + astunparse.unparse(self.visit(stmt)).replace('\n','\n\t')
                    continue
            return_str += astunparse.unparse(self.visit(stmt))
        return ast.parse(return_str)


    def visit_ConditionSTMT(self, node):
        tmp_node = copy.deepcopy(node)
        if tmp_node.c_type == 'else':
            tmp_node.expression = ''
        else:
            if 'expression' in tmp_node.__dict__ and tmp_node.expression:
                if isinstance(tmp_node.expression, ast.AST):
                    tmp_node.expression = astunparse.unparse(self.visit(tmp_node.expression))[1:-1]
            else:
                tmp_node.expression = ''
        return_str = str(tmp_node.c_type) + ' ' + str(tmp_node.expression) + ':' + '\n'
        if not tmp_node.body:
            return_str += '\tpass'
        else:
            for body_stmt in tmp_node.body:
                if isinstance(body_stmt, ast.AST):
                    body_py_ast = run_transformer(body_stmt)
                    return_str += '\t' + str(astunparse.unparse(body_py_ast))[1:-1].replace('\n','\n\t') + '\n'
                else:
                    return_str += '\t' + str(body_stmt) + '\n'
        if tmp_node.c_type in ['else', 'elif']:
            return_str = 'if None:\n\tpass\n' + return_str
            tmp_ast = ast.parse(return_str)
            return tmp_ast.body[0].orelse   #return list type
        else:
            return ast.parse(return_str)    #return module type

    def visit_ConditionExpression(self, node):
        tmp_node = copy.deepcopy(node)
        for field in tmp_node._fields:
            if isinstance(tmp_node.__dict__[field], ast.AST):
                tmp_node.__dict__[field] = astunparse.unparse(run_transformer(tmp_node.__dict__[field]))[1:-1]
        return_str = str(tmp_node.variable) + ' '+ str(tmp_node.operator) + ' '+ str(tmp_node.condition)
        return ast.parse(return_str)



def run_transformer(source_ast):
    module_ast = ast.Module()
    if type(source_ast) == list:
        module_ast.body = copy.deepcopy(source_ast)
    else:
        module_ast.body = copy.deepcopy([source_ast])
    result_ast = element_ast.ElementTransformer().visit(module_ast)
    result_ast = IrregularTransformer().visit(result_ast)
    result_ast = VariableTransformer().visit(result_ast)
    return result_ast

class FunctionNameFinder(ast.NodeVisitor):
    def __init__(self):
        super(FunctionNameFinder, self).__init__()
        self.func_name_list = []
    def generic_visit(self, node):
        if 'func' in node.__dict__ and node.func:
            self.func_name_list.append(node.func.id)
        super(FunctionNameFinder, self).generic_visit(node)
        return self.func_name_list

class CustomFunctionTransformer(ast.NodeTransformer):
    def __init__(self, flag):
        super(CustomFunctionTransformer, self).__init__()
        self.flag = flag

    def generic_visit(self, node):
        if 'func' in node.__dict__ and node.func:
            method = 'transform_' + node.func.id
            if method in dir(self):
                method = 'transform_' + node.func.id
                transformer = getattr(self, method, self.generic_visit)
                tf_string = transformer(node)
                tf_ast = ast.parse(tf_string).body[0]
                node = tf_ast
        return super(CustomFunctionTransformer, self).generic_visit(node)

    def generic_transform(self, node):
        ### default action describe ###
        pass

    def translate_base_string(self, arg_names):
        # args = [arg_node.value for arg_node in node.args]
        arg_names_copy = copy.deepcopy(arg_names)
        last_element = arg_names_copy.pop(-1)

        base_string = 'self._DesignParameter'
        while arg_names_copy:
            element = arg_names_copy.pop(0)
            base_string += f"['{element}']['_DesignObj']._DesignParameter"
        base_string += f"['{last_element}']"
        return base_string

    def extract_element_string(self, arg_names):
        base_string = 'self._DesignParameter'
        last_element = arg_names.pop(-1)
        while arg_names:
            element = arg_names.pop(0)
            base_string += f"['{element}']['_DesignObj']._DesignParameter"
        base_string += f"['{last_element}']"
        return base_string

    def extract_xy_string(self, arg_names, last_index):
        base_string = self.extract_element_string(arg_names) + f"['_XYCoordinates']{last_index}"
        x = base_string + '[0]'
        y = base_string + '[1]'
        return x, y

    def extract_xy_hierarchy_string(self, arg_names, arg_indexes):
        x_list = [None] * len(arg_names)
        y_list = [None] * len(arg_names)
        for i in range(len(arg_names)):
            xy_info = self.extract_xy_string(arg_names[:i+1], arg_indexes[i])
            x_list[i] = xy_info[0]
            y_list[i] = xy_info[1]
        return "+".join(x_list), "+".join(y_list)

    def parse_args_info(self, args):
        args = [arg_node.value for arg_node in args]
        arg_names = list(map(lambda arg: re.sub('\[.*\]', '', arg), args))
        arg_indexes = list(map(lambda arg: re.findall('\[.*\]', arg)[0], args))
        return arg_names, arg_indexes

    def transform_top(self, node):
        arg_names, arg_indexes = self.parse_args_info(node.args)
        base_element_string = self.translate_base_string(arg_names)
        base_xy_string_tuple = self.extract_xy_hierarchy_string(arg_names, arg_indexes)

        output_x = base_xy_string_tuple[0]
        output_y = base_xy_string_tuple[1] + "+" + base_element_string + f"['_YWidth']/2"

        if self.flag == 'X':
            return output_x
        elif self.flag == 'Y':
            return output_y
        else:
            return "[" + ",".join([output_x, output_y]) + "]"

    def transform_bot(self, node):
        arg_names, arg_indexes = self.parse_args_info(node.args)
        base_element_string = self.translate_base_string(arg_names)
        base_xy_string_tuple = self.extract_xy_hierarchy_string(arg_names, arg_indexes)

        output_x = base_xy_string_tuple[0]
        output_y = base_xy_string_tuple[1] + "-" + base_element_string + f"['_YWidth']/2"

        if self.flag == 'X':
            return output_x
        elif self.flag == 'Y':
            return output_y
        else:
            return "[" + ",".join([output_x, output_y]) + "]"

    def transform_center(self, node):
        arg_names, arg_indexes = self.parse_args_info(node.args)
        base_element_string = self.translate_base_string(arg_names)
        base_xy_string_tuple = self.extract_xy_hierarchy_string(arg_names, arg_indexes)

        output_x = base_xy_string_tuple[0]
        output_y = base_xy_string_tuple[1]

        if self.flag == 'X':
            return output_x
        elif self.flag == 'Y':
            return output_y
        else:
            return "[" + ",".join([output_x, output_y]) + "]"

    def transform_right(self, node):
        arg_names, arg_indexes = self.parse_args_info(node.args)
        base_element_string = self.translate_base_string(arg_names)
        base_xy_string_tuple = self.extract_xy_hierarchy_string(arg_names, arg_indexes)

        output_x = f"{base_xy_string_tuple[0]} + {base_element_string}['_XWidth']/2"
        output_y = base_xy_string_tuple[1]

        if self.flag == 'X':
            return output_x
        elif self.flag == 'Y':
            return output_y
        else:
            return "[" + ",".join([output_x, output_y]) + "]"

    def transform_rb(self, node):
        arg_names, arg_indexes = self.parse_args_info(node.args)
        base_element_string = self.translate_base_string(arg_names)
        base_xy_string_tuple = self.extract_xy_hierarchy_string(arg_names, arg_indexes)

        output_x = f"{base_xy_string_tuple[0]} + {base_element_string}['_XWidth']/2"
        output_y = f"{base_xy_string_tuple[0]} - {base_element_string}['_YWidth']/2"

        if self.flag == 'X':
            return output_x
        elif self.flag == 'Y':
            return output_y
        else:
            return "[" + ",".join([output_x, output_y]) + "]"

    def transform_rt(self, node):
        arg_names, arg_indexes = self.parse_args_info(node.args)
        base_element_string = self.translate_base_string(arg_names)
        base_xy_string_tuple = self.extract_xy_hierarchy_string(arg_names, arg_indexes)

        output_x = f"{base_xy_string_tuple[0]} + {base_element_string}['_XWidth']/2"
        output_y = f"{base_xy_string_tuple[0]} + {base_element_string}['_YWidth']/2"

        if self.flag == 'X':
            return output_x
        elif self.flag == 'Y':
            return output_y
        else:
            return "[" + ",".join([output_x, output_y]) + "]"



    def transform_left(self, node):
        arg_names, arg_indexes = self.parse_args_info(node.args)
        base_element_string = self.translate_base_string(arg_names)
        base_xy_string_tuple = self.extract_xy_hierarchy_string(arg_names, arg_indexes)

        output_x = f"{base_xy_string_tuple[0]} - {base_element_string}['_XWidth']/2"
        output_y = f"{base_xy_string_tuple[0]}"

        if self.flag == 'X':
            return output_x
        elif self.flag == 'Y':
            return output_y
        else:
            return "[" + ",".join([output_x, output_y]) + "]"


    def transform_lt(self, node):
        arg_names, arg_indexes = self.parse_args_info(node.args)
        base_element_string = self.translate_base_string(arg_names)
        base_xy_string_tuple = self.extract_xy_hierarchy_string(arg_names, arg_indexes)

        output_x = f"{base_xy_string_tuple[0]} - {base_element_string}['_XWidth']/2"
        output_y = f"{base_xy_string_tuple[0]} + {base_element_string}['_YWidth']/2"

        if self.flag == 'X':
            return output_x
        elif self.flag == 'Y':
            return output_y
        else:
            return "[" + ",".join([output_x, output_y]) + "]"


    def transform_lb(self, node):
        arg_names, arg_indexes = self.parse_args_info(node.args)
        base_element_string = self.translate_base_string(arg_names)
        base_xy_string_tuple = self.extract_xy_hierarchy_string(arg_names, arg_indexes)

        output_x = f"{base_xy_string_tuple[0]} - {base_element_string}['_XWidth']/2"
        output_y = f"{base_xy_string_tuple[0]} - {base_element_string}['_YWidth']/2"

        if self.flag == 'X':
            return output_x
        elif self.flag == 'Y':
            return output_y
        else:
            return "[" + ",".join([output_x, output_y]) + "]"


    def transform_height(self, node):
        arg_names, arg_indexes = self.parse_args_info(node.args)
        base_element_string = self.translate_base_string(arg_names)

        if self.flag == 'XY':
            raise Exception('Height cannot be expressed as XY coordinates.')

        return f"{base_element_string}['_YWidth']"

    def transform_width(self, node):
        arg_names, arg_indexes = self.parse_args_info(node.args)
        base_element_string = self.translate_base_string(arg_names)

        if self.flag == 'XY':
            raise Exception('Height cannot be expressed as XY coordinates.')

        return f"{base_element_string}['_XWidth']"







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

    def visit_ArgumentVariable(self,node):
        sentence = f"{node.name} = None"
        tmp = ast.parse(sentence)
        return tmp.body

if __name__ == '__main__':
    # ea = ElementArray()
    # tf = VariableTransformer()
    # k = ['a','b']
    # ea.elements = 'k'
    # # XWidth,YWidth = str(200),
    # ea.XY = [['XWidth','YWidth']]
    # ea.x_space_distance = '100'
    # ea.y_space_distance = '200'
    #
    # kk = tf.visit(ea)
    # print(kk)
    # print(astunparse.dump(kk))
    # astunparse.unparse(kk)
    # print(astunparse.unparse(kk))



    tf = CustomFunctionTransformer('XY')
    node = ast.parse("top('abc[0]','_COLayer[0]')")
    node_tmp = node.body[0].value
    # tf.transform_top(node_tmp)
    a = tf.visit(node_tmp)

# a = ConditionSTMTlist()
# bb = ConditionSTMT()
# bb.c_type = 'if'
#
# b = ConditionSTMT()
# b.c_type = 'else'
# c = ConditionExpression()
# variable__ = ast.parse('a').body[0]
# c.variable = variable__
# # c.variable = 1
# c.operator = '>'
# c.condition = '0'
# # b.expression = c
# bb.expression = c
# tmp = ast.parse('print("hello")')
# b.body = tmp.body
# a.body = [b]
# tf = IrregularTransformer()
# k = tf.visit(a)
# print(astunparse.unparse(k))

