import ast
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
    def __init__(self, _id_to_data_dict):
        if not _id_to_data_dict:
            raise Exception("Not valid input")
        self._id_to_data_dict = _id_to_data_dict

    def visit_XYCoordinate(self,node):
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
        for XYFlag, elements in self._id_to_data_dict.XYDict[_id].items():
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
        sentence = '['
        for _, elementIdList in self._id_to_data_dict.XYPathDict[_id].items():
            for i in range(len(elementIdList)):
                tmp_node = XYCoordinate()
                tmp_node.id = elementIdList[i]
                tmp_code_ast = self.visit_XYCoordinate(tmp_node)
                tmp_code = astunparse.unparse(tmp_code_ast)
                tmp_code = tmp_code[2:-2]
                sentence = sentence + tmp_code + ',\n'
                del tmp_node
        sentence = sentence[:-2] + ']'
        final_tripleList = '[' +sentence+ ']'
        tmp = ast.parse(final_tripleList)
        return tmp.body

    def visit_LogicExpression(self,node):
        _id = node.id
        tmpDict = dict()
        tmpDict['X'] = []
        tmpDict['Y'] = []
        final_x_value = None
        final_y_value = None
        for XYFlag, elements in self._id_to_data_dict.ExpressionDict[_id].items():
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

        if len(tmpDict['X']) != 0:
            for i in range(len(tmpDict['X'])):
                if final_x_value == None:
                    final_x_value = tmpDict['X'][i]
                else:
                    final_x_value = tmpDict['X'][i] + ' + ' + final_x_value
            sentence = final_x_value
        else:

            for j in range(len(tmpDict['Y'])):
                if final_y_value == None:
                    final_y_value = tmpDict['Y'][j]
                else:
                    final_y_value = tmpDict['Y'][j] + ' + ' + final_y_value
            sentence = final_y_value
        sentence = '(' + sentence + ')'
        tmp = ast.parse(sentence)
        return tmp.body

    def visit_Array(self, node):
        _id = node.id
        info_dict = self._id_to_data_dict.ArrayDict[_id]

        ############# Common Elements ################
        _name = info_dict['name']               # Fixed
        _type = info_dict['type']              # Fixed
        _flag = info_dict['flag']     # Fixed
        _width = info_dict['width']
        if _type != "path_array":
            _height = info_dict['height']

        _layer = info_dict['layer']             # Fixed
        XY_source_ref = info_dict['XY_source_ref']
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
                if _flag == 'relative':
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
                if _flag == 'relative':
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

        ################### Width, height, Coordinates Calculation Done ########################
        if _flag == 'relative':
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
                comparison_code = f"path_list = []\n" \
                                  f"if ({layer_xy}[0][0] == {layer_xy}[-1][0]) :\n" \
                                  f"\tmode = 'horizontal'\n" \
                                  f"\t_width = {_height_code}\n" \
                                  f"elif ({layer_xy}[0][1] == {layer_xy}[-1][1]) :\n" \
                                  f"\tmode = 'vertical'\n" \
                                  f"\t_width = {_width_code}\n" \
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
                pass
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
                            f"\t\ttmp = {source_XY_code} + [{_x_distance}, {_y_distance}]\n" \
                            f"\t\tXYList.append(tmp)\n"
                # elif _index == 'Odd':
                #     loop_code = f"XYList = []\n" \
                #                 f"for i in range(len({layer_xy})):\n" \
                #                 f"\tif (i%2 == 1):\n" \
                #                 f"\t\tXYList.append([x+y for x,y in zip({parent_xy} , {layer_xy}[i] ) ] )\n"
                # elif _index == 'Even':
                #     loop_code = f"XYList = []\n" \
                #                 f"for i in range(len({layer_xy})):\n" \
                #                 f"\tif (i%2 == 0):\n" \
                #                 f"\t\tXYList.append([x+y for x,y in zip({parent_xy} , {layer_xy}[i] ) ] )\n"
                # elif _index == 'Custom':
                #     loop_code = f"XYList = []\n" \
                #                 f"for i in range({_row_num}):\n" \
                #                 f"\tfor j in range({_col_num}):\n" \
                #                 f"\t\ttmp = {source_XY_code} + [{_x_distance}, {_y_distance}]" \
                #                 f"\t\tXYList.append(tmp)\n"

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
        if XYFlag == 'FA':
            if function != ('width' or 'height'):
                raise Exception("Invalid Input, Debug")
            else:
                XYFlag = 'XY'
        tmp_string = re.sub('\(|\'|\)', "", expression)
        tmp_string = tmp_string[len(function):]
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

        code = code + f"_DesignParameter['{layer}']"
        offset_x = ''
        offset_y = ''
        offset_xy = None
        for i in range(len(offsets)):
            offset_x += offsets[i] + f'{offset_indices[i]}[0]'
            offset_y += offsets[i] + f'{offset_indices[i]}[1]'
        if function == 'width':
            result = code + '[\'_XWidth\']'
        elif function == 'height':
            result = code + '[\'_YWidth\']'
        if XYFlag == 'X':
            if function == 'lt' or function == 'left' or function == 'lb':
                result = offset_x + '+' + f"{code}['_XYCoordinates']{layer_index}[0] - {code}['_XWidth']/2"
            elif function == 'top' or function == 'bottom' or function == 'center':
                result = offset_x + '+' + f"{code}['_XYCoordinates']{layer_index}[0]"
            elif function == 'rt' or function == 'right' or function == 'rb':
                result = offset_x + '+' + f"{code}['_XYCoordinates']{layer_index}[0] + {code}['_XWidth']/2"
            else:   # Width or Height case
                print(f" XYFlag Redundant: input function: {function}, XYFlag = {XYFlag} for Debugging")
        elif XYFlag == 'Y':
            if function == 'lt' or function == 'rt' or function == 'top':
                result = offset_y + '+' + f"{code}['_XYCoordinates']{layer_index}[1] + {code}['_YWidth']/2"
            elif function == function == 'left' or function == 'right' or function == 'center':
                result = offset_y + '+' + f"{code}['_XYCoordinates']{layer_index}[1]"
            elif function == function == 'lb' or function == 'rb' or function == 'bottom':
                result = offset_y + '+' + f"{code}['_XYCoordinates']{layer_index}[1] - {code}['_YWidth']/2"
            else:   # Width or Height case
                print(f" XYFlag Redundant: input function: {function}, XYFlag = {XYFlag} for Debugging")
                pass
        elif XYFlag == 'XY':
        # X Input first
            if function == 'lt' or function == 'left' or function == 'lb':
                result = offset_x + '+' + f"{code}['_XYCoordinates']{layer_index}[0] - {code}['_XWidth']/2"
            elif function == function == 'top' or function == 'bottom' or function == 'center':
                result = offset_x + '+' + f"{code}['_XYCoordinates']{layer_index}[0]"
            elif function == 'rt' or function == 'right' or function == 'rb':
                result = offset_x + '+' + f"{code}['_XYCoordinates']{layer_index}[0] + {code}['_XWidth']/2"
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
        print(f"Re-Expressed Element: \n{result}")
        if type(result) == str:
            result = '(' + result + ')'
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