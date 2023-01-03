import os
import sys

import re
import numpy as np
import cv2
import argparse
import imutils
# from skimage.measure import compare_ssim

import warnings
from PyQTInterface.layermap import LayerReader
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaMet22Met3
from generatorLib.generator_models import ViaMet32Met4
from generatorLib.generator_models import ViaMet42Met5
from generatorLib.generator_models import ViaMet52Met6
from generatorLib.generator_models import ViaMet62Met7


class parameterPrediction():
    def __init__(self):
        super().__init__()
    def nmos_checker(self, cell_dp_dict = None):
        expected_width = 0
        expected_length = 0
        expected_dummy = False
        expected_pccrit = False
        poly_cnt = 0
        parent_name = None

        cont_x_list = []
        cont_y_list = []
        for dp_name, qt_dp in cell_dp_dict.items():
            if qt_dp._DesignParameter['_LayerUnifiedName'] == 'DIFF':
                if (qt_dp._DesignParameter['_XYCoordinates'][0][0] == 0) and \
                        (qt_dp._DesignParameter['_XYCoordinates'][0][1] == 0):
                    expected_width = qt_dp._DesignParameter['_YWidth']
            elif qt_dp._DesignParameter['_LayerUnifiedName'] == 'CONT':
                if (qt_dp._DesignParameter['_XYCoordinates'][0][0]) not in cont_x_list:
                    cont_x_list.append(qt_dp._DesignParameter['_XYCoordinates'][0][0])
                if (qt_dp._DesignParameter['_XYCoordinates'][0][1]) not in cont_y_list:
                    cont_y_list.append(qt_dp._DesignParameter['_XYCoordinates'][0][1])
            elif qt_dp._DesignParameter['_LayerUnifiedName'] == 'POLY':
                if (qt_dp._DesignParameter['_DatatypeName'] == '_drawing'):
                    poly_cnt = poly_cnt + 1
                    if qt_dp._DesignParameter['_XWidth'] != 0:
                        expected_length = qt_dp._DesignParameter['_XWidth']
                elif (qt_dp._DesignParameter['_DatatypeName'] == '_crit'):
                    expected_pccrit = True
            parent_name = qt_dp._ParentName
        expected_finger = len(cont_x_list) - 1
        expected_dummy = True if expected_finger == poly_cnt - 2 else expected_dummy
        print( expected_width, expected_length, poly_cnt, expected_dummy, expected_pccrit)

        nmos_obj = NMOSWithDummy._NMOS()
        nmos_obj._CalculateNMOSDesignParameter(_NMOSNumberofGate = expected_finger,
                                       _NMOSChannelWidth = expected_width,
                                       _NMOSChannellength = expected_length,
                                       _NMOSDummy = expected_dummy,
                                       _PCCrit = expected_pccrit)

        ### Checking Algorithm
        self.dp_verification(gds_dp = cell_dp_dict, generator_dp = nmos_obj._DesignParameter,
                             parent_name = parent_name)



    def via_checker(self, cell_dp_dict = None, class_name = None):
        expected_width = 0
        expected_length = 0

        layer_list = []
        metal_layer = []
        via_layer_qt = []


        via_x_list = []
        via_y_list = []

        for _, qt_dp in cell_dp_dict.items():
            layer_name = qt_dp._DesignParameter['_LayerUnifiedName']
            if layer_name not in layer_list:
                layer_list.append(layer_name)

            if re.search("VIA", layer_name):
                if (qt_dp._DesignParameter['_XYCoordinates'][0][0]) not in via_x_list:
                    via_x_list.append(qt_dp._DesignParameter['_XYCoordinates'][0][0])
                if (qt_dp._DesignParameter['_XYCoordinates'][0][1]) not in via_y_list:
                    via_y_list.append(qt_dp._DesignParameter['_XYCoordinates'][0][1])
                via_layer_qt.append(qt_dp)

            if layer_name == 'METAL1':
                metal_layer.append('METAL1')
                if (expected_width == 0) & (expected_length == 0):
                    expected_width = qt_dp._DesignParameter['_XWidth']
                    expected_length = qt_dp._DesignParameter['_YWidth']
            elif layer_name == 'METAL2':
                metal_layer.append('METAL2')
                if (expected_width == 0) & (expected_length == 0):
                    expected_width = qt_dp._DesignParameter['_XWidth']
                    expected_length = qt_dp._DesignParameter['_YWidth']
            elif layer_name == 'METAL3':
                metal_layer.append('METAL3')
                if (expected_width == 0) & (expected_length == 0):
                    expected_width = qt_dp._DesignParameter['_XWidth']
                    expected_length = qt_dp._DesignParameter['_YWidth']
            elif layer_name == 'METAL4':
                metal_layer.append('METAL4')
                if (expected_width == 0) & (expected_length == 0):
                    expected_width = qt_dp._DesignParameter['_XWidth']
                    expected_length = qt_dp._DesignParameter['_YWidth']
            elif layer_name == 'METAL5':
                metal_layer.append('METAL5')
                if (expected_width == 0) & (expected_length == 0):
                    expected_width = qt_dp._DesignParameter['_XWidth']
                    expected_length = qt_dp._DesignParameter['_YWidth']
            elif layer_name == 'METAL6':
                metal_layer.append('METAL6')
                if (expected_width == 0) & (expected_length == 0):
                    expected_width = qt_dp._DesignParameter['_XWidth']
                    expected_length = qt_dp._DesignParameter['_YWidth']
            elif layer_name == 'METAL7':
                metal_layer.append('METAL7')
                if (expected_width == 0) & (expected_length == 0):
                    expected_width = qt_dp._DesignParameter['_XWidth']
                    expected_length = qt_dp._DesignParameter['_YWidth']

        target_class = None
        if 'METAL2' in metal_layer:
            if 'METAL1' in metal_layer:
                target_class = 'ViaMet12Met2'
                via_obj = ViaMet12Met2._ViaMet12Met2()
            elif 'METAL3' in metal_layer:
                target_class = 'ViaMet22Met3'
                via_obj = ViaMet22Met3._ViaMet22Met3()
        elif 'METAL4' in metal_layer:
            if 'METAL3' in metal_layer:
                target_class = 'ViaMet32Met4'
                via_obj = ViaMet32Met4._ViaMet32Met4()
            elif 'METAL5' in metal_layer:
                target_class = 'ViaMet42Met5'
                via_obj = ViaMet42Met5._ViaMet42Met5()
        elif 'METAL6' in metal_layer:
            if 'METAL5' in metal_layer:
                target_class = 'ViaMet52Met6'
                via_obj = ViaMet52Met6._ViaMet52Met6()
            elif 'METAL7' in metal_layer:
                target_class = 'ViaMet62Met7'
                via_obj = ViaMet62Met7._ViaMet62Met7()

        if class_name != target_class :
            print("Classification Wrong!")

        enclosure_code = ""
        for item in via_layer_qt:
            if item._DesignParameter['_XYCoordinates'][0][0] == via_x_list[-1]:
                if item._DesignParameter['_XYCoordinates'][0][1] == via_y_list[-1]:
                    via_right_edge = item._DesignParameter['_XYCoordinates'][0][0] + item._DesignParameter['_XWidth'] / 2
                    via_top_edge = item._DesignParameter['_XYCoordinates'][0][1] + item._DesignParameter['_YWidth'] / 2
                    if (expected_width / 2 - 1) <= via_right_edge <= (expected_width / 2 + 1):
                        enclosure_code = 'MinimumEnclosureX'
                    elif (expected_length / 2 - 1) <= via_top_edge <= (expected_length / 2 + 1):
                        enclosure_code = 'MinimumEnclosureY'
        if via_obj:
            code = f"via_obj._Calculate{target_class}DesignParameter{enclosure_code}(_{target_class}NumberOfCOX = len(via_x_list), " \
                   f"_{target_class}NumberOfCOY = len(via_y_list))"
            exec(code)

        # self.dp_verification(gds_dp = cell_dp_dict, generator_dp = via_obj._DesignParameter)

    def dp_verification(self, gds_dp = None, generator_dp = None, parent_name = None):
        gen_layer_dict = self.layer_classification_gen(generator_dp)
        gds_layer_dict = self.layer_classification_gds(gds_dp)

        """
        Layer verification : 'DIFF','POLY','CONT','METAL','VIA'
        """

        for layer, dp_name in gen_layer_dict.items():
            generator_dp[dp_name]
        print("A")



        # image1 = self.gds_layer_to_image_gds(dp = gds_dp, layer = 'METAL1')
        # image2 = self.gds_layer_to_image_generator(dp = generator_dp, layer = 'METAL1')
        # cv2.imshow(f"gds_{parent_name}",image1)
        # cv2.imshow(f"generator_{parent_name}",image2)
        #
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # (score, diff) = compare_ssim(image1, image2, full=True)
        # diff = (diff*255).astype("uint8")
        # print(f"SSIM: {score}")

    def create_polygon_gen(self,gen_layer_dict = None, generator_dp = None):
        min_x = None

        for layer, dp_name in gen_layer_dict.items():
            for i in range(len(generator_dp[dp_name]['_XYCoordinates'])):
                polygon_coordinate_list = self.center_width_to_polygon(generator_dp[dp_name]['_XYCoordinates'][i],
                                             generator_dp[dp_name]['_XWidth'],
                                             generator_dp[dp_name]['_YWidth'])

        pass

    def layer_classification_gen(self, dp = None):
        classified_dict = dict()
        _Layer = LayerReader._LayerMapping
        layernum2name = LayerReader._LayDatNum2LayDatName(LayerReader._LayerMapping)
        for dp_name, info in dp.items():
            if info['_DesignParametertype'] == 1:
                layer_name = layernum2name[str(info['_Layer'])]
                layer_name = layer_name[str(info['_Datatype'])]
                if re.search("PIN", layer_name):
                    layer_name = layer_name[:re.search("PIN", layer_name).start()]

                if layer_name not in classified_dict.keys():
                    classified_dict[f'{layer_name}'] = []
                    classified_dict[f'{layer_name}'].append(dp_name)
                else:
                    classified_dict[f'{layer_name}'].append(dp_name)

        return classified_dict

    def layer_classification_gds(self, dp = None):
        classified_dict = dict()
        for dp_name, qt_dp in dp.items():
            layer_name = qt_dp._DesignParameter['_LayerUnifiedName']
            if (qt_dp._DesignParameter['_XWidth'] == 0) or (qt_dp._DesignParameter['_YWidth'] == 0):
                continue

            if layer_name not in classified_dict.keys():
                classified_dict[f'{layer_name}'] = []
                classified_dict[f'{layer_name}'].append(dp_name)
            else:
                classified_dict[f'{layer_name}'].append(dp_name)

        return classified_dict



    def gds_layer_to_image_gds(self,dp = None, layer = None):
        if layer == None:
            warnings.warn("No Layer Information")
            return
        layer_XY_list = []
        min_xy = []
        max_xy = []

        for key, qt_dp in dp.items():
            layer_name = qt_dp._DesignParameter['_LayerUnifiedName']
            if layer_name == layer:
                for i in range(len(qt_dp._DesignParameter['_XYCoordinates'])):
                    layer_min_x = qt_dp._DesignParameter['_XYCoordinates'][i][0] - qt_dp._DesignParameter['_XWidth'] / 2
                    layer_min_y = qt_dp._DesignParameter['_XYCoordinates'][i][1] - qt_dp._DesignParameter['_YWidth'] / 2
                    layer_max_x = qt_dp._DesignParameter['_XYCoordinates'][i][0] + qt_dp._DesignParameter['_XWidth'] / 2
                    layer_max_y = qt_dp._DesignParameter['_XYCoordinates'][i][1] + qt_dp._DesignParameter['_YWidth'] / 2

                    if len(layer_XY_list) == 0:
                        min_xy.append([layer_min_x, layer_min_y])
                        max_xy.append([layer_max_x, layer_max_y])
                    else:
                        if layer_min_x < min_xy[0][0]:
                            min_xy[0][0] = layer_min_x

                        if layer_min_y < min_xy[0][1]:
                            min_xy[0][1] = layer_min_y

                        if layer_max_x > max_xy[0][0]:
                            max_xy[0][0] = layer_max_x

                        if layer_max_y > max_xy[0][1]:
                            max_xy[0][1] = layer_max_y

                    layer_XY_list.append([[layer_min_x, layer_min_y], [layer_max_x, layer_max_y]])

        offset_x = - min_xy[0][0]
        offset_y = - min_xy[0][1]

        width = int(max_xy[0][0] - min_xy[0][0])
        height = int(max_xy[0][1] - min_xy[0][1])

        """
        blue : (255, 0, 0)
        green : (0, 255, 0)
        red : (0, 0, 255)
        white : (255, 255, 255)
        yellow : (0,255,255)
        """

        layer_image = np.zeros((height,width,3), np.uint8)
        for i in range(len(layer_XY_list)):
            starting_pt = (int(layer_XY_list[i][0][0] + offset_x), int(layer_XY_list[i][0][1] + offset_y))
            end_pt = ((int(layer_XY_list[i][1][0] + offset_x), int(layer_XY_list[i][1][1] + offset_y)))
            cv2.rectangle(layer_image, starting_pt, end_pt, (0,255,255), -1)

        return(layer_image)

    def gds_layer_to_image_generator(self,dp = None, layer = None):
        if layer == None:
            warnings.warn("No Layer Information")
            return

        _Layer = LayerReader._LayerMapping
        layernum2name = LayerReader._LayDatNum2LayDatName(LayerReader._LayerMapping)

        layer_XY_list = []
        min_xy = []
        max_xy = []

        for boundary_name, info in dp.items():
            if info['_DesignParametertype'] == 1:
                layer_name = layernum2name[str(info['_Layer'])]
                layer_name = layer_name[str(info['_Datatype'])]
                if layer_name == layer:
                    for i in range(len(info['_XYCoordinates'])):
                        layer_min_x = info['_XYCoordinates'][i][0] - info['_XWidth'] / 2
                        layer_min_y = info['_XYCoordinates'][i][1] - info['_YWidth'] / 2
                        layer_max_x = info['_XYCoordinates'][i][0] + info['_XWidth'] / 2
                        layer_max_y = info['_XYCoordinates'][i][1] + info['_YWidth'] / 2

                        if len(layer_XY_list) == 0:
                            min_xy.append([layer_min_x, layer_min_y])
                            max_xy.append([layer_max_x, layer_max_y])
                        else:
                            if layer_min_x < min_xy[0][0]:
                                min_xy[0][0] = layer_min_x

                            if layer_min_y < min_xy[0][1]:
                                min_xy[0][1] = layer_min_y

                            if layer_max_x > max_xy[0][0]:
                                max_xy[0][0] = layer_max_x

                            if layer_max_y > max_xy[0][1]:
                                max_xy[0][1] = layer_max_y

                        layer_XY_list.append([[layer_min_x, layer_min_y], [layer_max_x, layer_max_y]])

        offset_x = - min_xy[0][0]
        offset_y = - min_xy[0][1]

        width = int(max_xy[0][0] - min_xy[0][0])
        height = int(max_xy[0][1] - min_xy[0][1])

        """
        blue : (255, 0, 0)
        green : (0, 255, 0)
        red : (0, 0, 255)
        white : (255, 255, 255)
        yellow : (0,255,255)
        """

        layer_image = np.zeros((height,width,3), np.uint8)
        for i in range(len(layer_XY_list)):
            starting_pt = (int(layer_XY_list[i][0][0] + offset_x), int(layer_XY_list[i][0][1] + offset_y))
            end_pt = ((int(layer_XY_list[i][1][0] + offset_x), int(layer_XY_list[i][1][1] + offset_y)))
            cv2.rectangle(layer_image, starting_pt, end_pt, (0,255,255), -1)

        return(layer_image)

    def center_width_to_polygon(self, center = list, xwidth = None, ywidth = None):

        """
        center type : single list
        """

        if (int(xwidth) % 2 == 1) or (int(ywidth) % 2 == 1):
            warnings.warn("MinSnapSpacing Issue during verfication")

        left_x = center[0] - xwidth / 2
        right_x = center[0] + xwidth / 2
        top_y = center[1] + ywidth / 2
        bottom_y = center[1] - ywidth / 2

        """
        return : four coordinates from bottom left, counterclockwise
        """

        return [[left_x, bottom_y],[right_x, bottom_y], [right_x, top_y], [left_x, top_y]]


# if __name__ == '__main__':
#
#     tmp_obj = parameterPrediction()
#     tmp_obj.load_gds()

