from generatorLib import DRC
from generatorLib.generator_models import NbodyContact
from generatorLib.generator_models import PbodyContact
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaMet22Met3
from generatorLib.generator_models import ViaMet32Met4
from generatorLib import StickDiagram
from generatorLib import DesignParameters

import copy, math, warnings

class functions():
    def create_output_via(self, _Name = None, via_name=None, mos_type=None, hierarchy_list = None,
                          calibre_option=None,  number_of_coy=None, supply_flag = False):
        """
        :param _Name: name of the designparameter name
        :param via_name: via object name to be generated
        :param mos_type: type of MOSFET
        :param hierarchy_list:
        :param calibre_option: whether to shift created via 'up'side or 'down'side
        :param number_of_coy: optional input for number of Y contact numbers
        :return: code
        implement 'exec(code)' in the main project.
        """
        if (_Name == None) or (via_name == None) or (mos_type == None) or (hierarchy_list == None):
            raise NotImplementedError("Lack Of Necessary Inputs !")
        if mos_type == 'nmos' or mos_type =='NMOS':
            mos_type = 'NMOS'
        elif mos_type == 'pmos' or mos_type == 'PMOS':
            mos_type = 'PMOS'

        if supply_flag:
            output_option = 'Supply'
        else:
            output_option = 'Output'

        hierarchy_tuple_code = ''
        for i in range(len(hierarchy_list)):
            hierarchy_tuple_code = hierarchy_tuple_code + f"'{hierarchy_list[i]}', "

        code =\
        f"self._DesignParameter[\'{via_name}\'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2("\
        f"_DesignParameter= None, _Name= \'{via_name}_in_{_Name}\'))[0]\n"\
        f"via12_inputs = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)\n"\
        f"via12_inputs['_ViaMet12Met2NumberOfCOX'] = 1\n"\
        "tmp_number = 1\n" \
        f"calibre_value = int((drc._VIAxMinSpace + drc._VIAxMinWidth) / 4)\n" \
        f"distance_to_edge = self.getYWidth({hierarchy_tuple_code}'_Met1Layer')\n"\
        f"if {number_of_coy} != None:\n" \
        f"\tvia12_inputs['_ViaMet12Met2NumberOfCOY'] = {number_of_coy}\n" \
        f"\tself._DesignParameter[\'{via_name}\']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**via12_inputs)\n" \
        f"else:\n"\
        "\twhile (1):\n"\
        f"\t\tvia12_inputs['_ViaMet12Met2NumberOfCOY'] = tmp_number\n"\
        f"\t\tself._DesignParameter[\'{via_name}\']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**via12_inputs)\n"
        if calibre_option != None:
            opt_code = f"\t\tfree_space = (distance_to_edge - self.getYWidth(\'{via_name}\', '_Met1Layer'))/2 - calibre_value\n"
        else:
            opt_code = f"\t\tfree_space = (distance_to_edge - self.getYWidth(\'{via_name}\', '_Met1Layer'))/2\n"
        code = code + opt_code +\
        f"\t\tif free_space >= 0:\n"\
        f"\t\t\ttmp_number = tmp_number + 1\n"\
        f"\t\telif free_space < 0:\n"\
        f"\t\t\ttmp_number = tmp_number - 1\n"\
        f"\t\t\tif tmp_number == 1:\n" \
        f"\t\t\t\ttmp_number = 2\n" \
        f"\t\t\tvia12_inputs['_ViaMet12Met2NumberOfCOY'] = tmp_number\n"\
        f"\t\t\tself._DesignParameter[\'{via_name}\']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**via12_inputs)\n"\
        f"\t\t\tbreak\n"

        hierarchy_code = f"coordinate_sets = self.getXY("

        hierarchy_code = hierarchy_code + hierarchy_tuple_code + f"'_XYCoordinate{mos_type}{output_option}Routing')\n"
        code = code + hierarchy_code

        if calibre_option == 'up':
            additional_code1 =\
            f"for i in range(len(coordinate_sets)):\n"\
            f"\tcoordinate_sets[i] = [a + b for a, b in zip(coordinate_sets[i], [0, calibre_value])]\n"
            code = code + additional_code1

        elif calibre_option == 'down':
            additional_code1 = \
            f"for i in range(len(coordinate_sets)):\n"\
            f"\tcoordinate_sets[i] = [a - b for a, b in zip(coordinate_sets[i], [0, calibre_value])]\n"
            code = code + additional_code1
        code = code +\
        f"\nself._DesignParameter[\'{via_name}\']['_XYCoordinates'] = coordinate_sets\n\n"

        return code

    def create_output_routing(self, path_name = None, via_name = None, width = None, routing_option = None):
        if width == None:
            width = 'drc._MetalxMinWidth'
        if routing_option == None:
            routing_option = 'center'
        code =\
        f"self._DesignParameter[\'{path_name}\'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0]," \
        f"_Datatype=DesignParameters._LayerMapping['METAL2'][1],_Width={width})\n"\
        f"calibre_x = self.getXWidth(\'{via_name}\', '_Met2Layer') / 2\n"\
        f"met2_height = self.getYWidth(\'{via_name}\', '_Met2Layer')\n"\
        f"met2_x_left = self.getXY(\'{via_name}\', '_Met2Layer')[0][0] - calibre_x\n"\
        f"met2_x_right = self.getXY(\'{via_name}\', '_Met2Layer')[-1][0] + calibre_x\n" \
        f"met2_y_center = self.getXY(\'{via_name}\', '_Met2Layer')[0][1]\n" \
        f"met2_y_top = self.getXY(\'{via_name}\', '_Met2Layer')[0][1] + met2_height / 2\n"\
        f"met2_y_bottom = self.getXY(\'{via_name}\', '_Met2Layer')[0][1] - met2_height / 2\n"\
        f"calibre_value = {width} / 2\n" \
        f"target_points = []\n"\
        f"source_points = []\n"\
        f"routing_points = []\n"

        if routing_option == 'above':
            option_code = \
                f"source_points.append([met2_x_left, met2_y_top + calibre_value])\n"\
                f"target_points.append([met2_x_right, met2_y_top + calibre_value])\n"\
                f"routing_points.append([source_points[0], target_points[0]])\n"
        elif routing_option == 'top':
            option_code = \
                f"source_points.append([met2_x_left, met2_y_top - calibre_value])\n"\
                f"target_points.append([met2_x_right, met2_y_top - calibre_value])\n"\
                f"routing_points.append([source_points[0], target_points[0]])\n"
        elif routing_option == 'center':
            option_code = \
                f"source_points.append([met2_x_left, met2_y_center])\n"\
                f"target_points.append([met2_x_right, met2_y_center])\n"\
                f"routing_points.append([source_points[0], target_points[0]])\n"
        elif routing_option == 'bottom':
            option_code = \
                f"source_points.append([met2_x_left, met2_y_bottom + calibre_value])\n"\
                f"target_points.append([met2_x_right, met2_y_bottom + calibre_value])\n"\
                f"routing_points.append([source_points[0], target_points[0]])\n"
        elif routing_option == 'below':
            option_code = \
                f"source_points.append([met2_x_left, met2_y_bottom - calibre_value])\n"\
                f"target_points.append([met2_x_right, met2_y_bottom - calibre_value])\n"\
                f"routing_points.append([source_points[0], target_points[0]])\n"
        else:
            raise NotImplementedError(f"Invalid Routing_option Input: {routing_option}")

        code = code + option_code + \
             f"self._DesignParameter[\'{path_name}\']['_XYCoordinates'] = routing_points\n"
        print(code)
        return code