import os
import sys
import re

from generatorLib.generator_models import NMOSWithDummy
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

        print("test")


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
        self.dp_verification()

    def dp_verification(self, gds_dp = None, generator_dp = None):
        import numpy as np
        import cv2

        zeros = np.zeros((240,320), dtype=np.uint8)
        cv2.imshow('black', zeros)
        print(zeros)

    def gds_to_image(self,dp):
        diff_list_1 = []
        poly_list_1 = []
        m1_list_1 = []
        m2_list_1 = []
        m3_list_1 = []
        m4_list_1 = []
        m5_list_1 = []
        m6_list_1 =[]
        m7_list_1 = []
        via12_list_1 = []
        via23_list_1 = []
        via34_list_1 = []
        via45_list_1 = []
        via56_list_1 = []
        nwell_list_1 = []

        diff_list_2 = []
        poly_list_2 = []
        m1_list_2 = []
        m2_list_2 = []
        m3_list_2 = []
        m4_list_2 = []
        m5_list_2 = []
        m6_list_2 =[]
        m7_list_2 = []
        via12_list_2 = []
        via23_list_2 = []
        via34_list_2 = []
        via45_list_2 = []
        via56_list_2 = []
        nwell_list_2 = []

        for key, qt_dp in dp.items():
            layer_name = qt_dp._DesignParameter['_LayerUnifiedName']



#
# if __name__ == '__main__':
#
#     tmp_obj = parameterPrediction()
#     tmp_obj.load_gds()

