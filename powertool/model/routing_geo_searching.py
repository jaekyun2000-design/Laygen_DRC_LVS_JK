from generatorLib import StickDiagram
from enum import Enum
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import copy
# import cv2
import warnings, traceback

from intervaltree import Interval, IntervalTree
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PyQt5.QtWidgets import *


class Color(Enum):
    black = 0
    red = 1


class tf_matrix:
    rotate_0 = np.array([[1, 0],
                         [0, 1]])
    rotate_90 = np.array([[0, -1],
                          [1, 0]])
    rotate_180 = np.array([[-1, 0],
                           [0, -1]])
    rotate_270 = np.array([[0, 1],
                           [-1, 0]])

    reflect_off = np.array([[1, 0],
                            [0, 1]])

    reflect_on = np.array([[1, 0],
                           [0, -1]])


def matrix_dot(tf_matrix, xy):
    return tf_matrix.dot(xy).tolist()


def convert_angle_to_matrix(angle):
    if angle == None:
        angle = 0
    return tf_matrix.__dict__['rotate_' + str(int(angle))]


def convert_reflect_to_matrix(reflect):
    if reflect == None or reflect[0] == 0:
        return tf_matrix.reflect_off
    else:
        return tf_matrix.reflect_on


class GeometricField:
    def __init__(self):
        self.interval_tree_by_layer = dict()
        self.stick_diagram = StickDiagram._StickDiagram()

    def xy_projection_to_main_coordinates_system_qt(self, qt_designParameter):
        for name, qt_dp in qt_designParameter.items():
            self.qt_design_parameter_projection(qt_dp, [name])

    def qt_design_parameter_projection(self, qt_dp, structure_hierarchy=[], reflect=tf_matrix.reflect_off,
                                       angle=tf_matrix.rotate_0, base_xy=[0, 0]):
        dp = qt_dp._DesignParameter
        if dp['_DesignParametertype'] == 1:
            for idx, xy_pair in enumerate(dp['_XYCoordinates']):
                five_point_xy = self.stick_diagram.CenterCoordinateAndWidth2XYCoordinate(xy_pair, dp['_XWidth'],
                                                                                         dp['_YWidth'])
                # transformed_five_point_xy = [base_xy+angle.dot(reflect).dot(xy) for xy in five_point_xy]
                transformed_five_point_xy = [base_xy + reflect.dot(angle).dot(xy) for xy in five_point_xy]
                transformed_five_point_xy_ordered = self.stick_diagram.MinMaxXY2XYCoordinate(
                    self.stick_diagram.XYCoordinate2MinMaxXY(transformed_five_point_xy))
                if '_XYCoordinatesProjection' in dp:
                    dp['_XYCoordinatesProjection'].append(transformed_five_point_xy_ordered)
                else:
                    dp['_XYCoordinatesProjection'] = [transformed_five_point_xy_ordered]
                # dp['_XYCoordinatesProjection'] = transformed_five_point_xy_ordered
                if '_Hierarchy' in dp:
                    dp['_Hierarchy'].append(copy.deepcopy(structure_hierarchy))
                    dp['_Hierarchy'][-1][-1] += f'[{idx}]'
                else:
                    dp['_Hierarchy'] = copy.deepcopy([structure_hierarchy])
                    dp['_Hierarchy'][-1][-1] += f'[{idx}]'

                # return base_xy + angle.dot(reflect).dot(xy_pair)
        elif dp['_DesignParametertype'] == 2:
            for idx, xy_pair_list in enumerate(dp['_XYCoordinates']):
                transformed_five_point_xy_list = []
                # for idx_2, xy_pair in enumerate(xy_pair_list):
                transformed_xy_pairs = [base_xy + reflect.dot(angle).dot(xy) for xy in xy_pair_list]
                if len(transformed_xy_pairs) < 2:
                    warnings.warn("path object has not enough xy points.")
                    break
                for i in range(len(transformed_xy_pairs) - 1):
                    if transformed_xy_pairs[i][0] == transformed_xy_pairs[i + 1][0]:
                        x_width = dp['_Width']
                        y_width = abs(transformed_xy_pairs[i + 1][1] - transformed_xy_pairs[i][1])
                    else:
                        x_width = abs(transformed_xy_pairs[i + 1][0] - transformed_xy_pairs[i][0])
                        y_width = dp['_Width']
                    xy_pair = [(a + b) / 2 for a, b in zip(transformed_xy_pairs[i], transformed_xy_pairs[i + 1])]
                    five_point_xy = self.stick_diagram.CenterCoordinateAndWidth2XYCoordinate(xy_pair, x_width, y_width)
                    transformed_five_point_xy = [base_xy + reflect.dot(angle).dot(xy) for xy in five_point_xy]
                    transformed_five_point_xy_ordered = self.stick_diagram.MinMaxXY2XYCoordinate(
                        self.stick_diagram.XYCoordinate2MinMaxXY(transformed_five_point_xy))
                    transformed_five_point_xy_list.append(transformed_five_point_xy_ordered)
                    if '_Hierarchy' not in dp:
                        dp['_Hierarchy'] = copy.deepcopy([[structure_hierarchy]])
                    else:
                        if idx < len(dp['_Hierarchy']):
                            dp['_Hierarchy'][idx].append(copy.deepcopy(structure_hierarchy))
                        else:
                            dp['_Hierarchy'].append(copy.deepcopy([structure_hierarchy]))
                    # `if '_Hierarchy' in dp:
                    #     dp['_Hierarchy'][-1].append(copy.deepcopy(structure_hierarchy))
                    # else:
                    #     dp['_Hierarchy'] = copy.deepcopy([[structure_hierarchy]])
                    dp['_Hierarchy'][-1][-1][-1] += f'{[idx]}{[i]}'
                if '_XYCoordinatesProjection' in dp:
                    dp['_XYCoordinatesProjection'].append(transformed_five_point_xy_list)
                else:
                    dp['_XYCoordinatesProjection'] = [transformed_five_point_xy_list]


        elif dp['_DesignParametertype'] == 3:
            # structure_hierarchy.append(dp['_ElementName'])
            ############ 이 부분에서 idx 처리 해야함! #####################
            for sref_idx in range(len(dp['_XYCoordinates'])):
                base_xy = base_xy + angle.dot(reflect).dot(dp['_XYCoordinates'][sref_idx])
                sub_reflect = convert_reflect_to_matrix(dp['_Reflect']).dot(reflect)
                sub_angle = convert_angle_to_matrix(dp['_Angle']).dot(angle)
                # base_xy = base_xy + angle.dot(reflect).dot(dp['_XYCoordinates'][0])
                # sub_reflect = reflect.dot(convert_reflect_to_matrix(dp['_Reflect']))
                # sub_angle = angle.dot(convert_angle_to_matrix(dp['_Angle']))
                for name, sub_qt_dp in dp['_ModelStructure'].items():
                    sub_dp = sub_qt_dp._DesignParameter
                    if sub_dp['_DesignParametertype'] == 1 or sub_dp['_DesignParametertype'] == 2 or sub_dp['_DesignParametertype'] == 3:
                        structure_hierarchy_tmp = copy.deepcopy(structure_hierarchy)
                        structure_hierarchy_tmp[-1] += f'[{sref_idx}]'
                        structure_hierarchy_tmp.append(name)
                        self.qt_design_parameter_projection(sub_qt_dp, structure_hierarchy=structure_hierarchy_tmp,
                                                            reflect=sub_reflect, angle=sub_angle, base_xy=base_xy)

    def xy_projection_to_main_coordinates_system(self, designParameter):
        for name, dp in designParameter.items():
            self.design_parameter_projection(dp, [name])

    def design_parameter_projection(self, dp, structure_hierarchy=[], reflect=tf_matrix.reflect_off,
                                    angle=tf_matrix.rotate_0, base_xy=[0, 0]):
        # for _, dp in _DesignParameter.items():
        if dp['_DesignParametertype'] == 1:
            for idx, xy_pair in enumerate(dp['_XYCoordinates']):
                five_point_xy = self.stick_diagram.CenterCoordinateAndWidth2XYCoordinate(xy_pair, dp['_XWidth'],
                                                                                         dp['_YWidth'])
                # transformed_five_point_xy = [base_xy+angle.dot(reflect).dot(xy) for xy in five_point_xy]
                transformed_five_point_xy = [base_xy + reflect.dot(angle).dot(xy) for xy in five_point_xy]
                transformed_five_point_xy_ordered = self.stick_diagram.MinMaxXY2XYCoordinate(
                    self.stick_diagram.XYCoordinate2MinMaxXY(transformed_five_point_xy))
                if '_XYCoordinatesProjection' in dp:
                    dp['_XYCoordinatesProjection'].append(transformed_five_point_xy_ordered)
                else:
                    dp['_XYCoordinatesProjection'] = [transformed_five_point_xy_ordered]
                # dp['_XYCoordinatesProjection'] = transformed_five_point_xy_ordered
                if '_Hierarchy' in dp:
                    dp['_Hierarchy'].append(copy.deepcopy(structure_hierarchy))
                    dp['_Hierarchy'][-1][-1] += f'[{idx}]'
                else:
                    dp['_Hierarchy'] = copy.deepcopy([structure_hierarchy])
                    dp['_Hierarchy'][-1][-1] += f'[{idx}]'

                # return base_xy + angle.dot(reflect).dot(xy_pair)
        elif dp['_DesignParametertype'] == 2:
            for idx, xy_pair_list in enumerate(dp['_XYCoordinates']):
                transformed_five_point_xy_list = []
                # for idx_2, xy_pair in enumerate(xy_pair_list):
                transformed_xy_pairs = [base_xy + reflect.dot(angle).dot(xy) for xy in xy_pair_list]
                if len(transformed_xy_pairs) < 2:
                    warnings.warn("path object has not enough xy points.")
                    break
                for i in range(len(transformed_xy_pairs) - 1):
                    if transformed_xy_pairs[i][0] == transformed_xy_pairs[i + 1][0]:
                        x_width = dp['_Width']
                        y_width = abs(transformed_xy_pairs[i + 1][1] - transformed_xy_pairs[i][1])
                    else:
                        x_width = abs(transformed_xy_pairs[i + 1][0] - transformed_xy_pairs[i][0])
                        y_width = dp['_Width']
                    xy_pair = [(a + b) / 2 for a, b in zip(transformed_xy_pairs[i], transformed_xy_pairs[i + 1])]
                    five_point_xy = self.stick_diagram.CenterCoordinateAndWidth2XYCoordinate(xy_pair, x_width, y_width)
                    transformed_five_point_xy = [base_xy + reflect.dot(angle).dot(xy) for xy in five_point_xy]
                    transformed_five_point_xy_ordered = self.stick_diagram.MinMaxXY2XYCoordinate(
                        self.stick_diagram.XYCoordinate2MinMaxXY(transformed_five_point_xy))
                    transformed_five_point_xy_list.append(transformed_five_point_xy_ordered)
                    if '_Hierarchy' not in dp:
                        dp['_Hierarchy'] = copy.deepcopy([[structure_hierarchy]])
                    else:
                        if idx < len(dp['_Hierarchy']):
                            dp['_Hierarchy'][idx].append(copy.deepcopy(structure_hierarchy))
                        else:
                            dp['_Hierarchy'].append(copy.deepcopy([structure_hierarchy]))
                    # `if '_Hierarchy' in dp:
                    #     dp['_Hierarchy'][-1].append(copy.deepcopy(structure_hierarchy))
                    # else:
                    #     dp['_Hierarchy'] = copy.deepcopy([[structure_hierarchy]])
                    dp['_Hierarchy'][-1][-1][-1] += f'{[idx]}{[i]}'
                if '_XYCoordinatesProjection' in dp:
                    dp['_XYCoordinatesProjection'].append(transformed_five_point_xy_list)
                else:
                    dp['_XYCoordinatesProjection'] = [transformed_five_point_xy_list]
        elif dp['_DesignParametertype'] == 3:
            # structure_hierarchy.append(dp['_ElementName'])
            for sref_idx in range(len(dp['_XYCoordinates'])):
                base_xy = base_xy + angle.dot(reflect).dot(dp['_XYCoordinates'][sref_idx])
                sub_reflect = convert_reflect_to_matrix(dp['_Reflect']).dot(reflect)
                sub_angle = convert_angle_to_matrix(dp['_Angle']).dot(angle)
                for name, sub_dp in dp['_DesignObj']._DesignParameter.items():
                    if sub_dp['_DesignParametertype'] in [1,2,3]:
                        structure_hierarchy_tmp = copy.deepcopy(structure_hierarchy)
                        structure_hierarchy_tmp[-1] += f'[{sref_idx}]'
                        structure_hierarchy_tmp.append(name)
                        self.design_parameter_projection(sub_dp, structure_hierarchy=structure_hierarchy_tmp,
                                                            reflect=sub_reflect, angle=sub_angle, base_xy=base_xy)

    def draw_by_projection_xy(self, _DesignParameter):
        fig, ax = plt.subplots()
        vi = []
        blue = (255, 0, 0)
        # img=np.zeros((10000,10000,3))

        stack = []
        for _, designparameter in _DesignParameter.items():
            stack.append(designparameter)
            while stack:
                dp = stack.pop(0)
                if dp['_DesignParametertype'] == 1:
                    if dp['_Layer'] == 17:
                        edgecolor = facecolor = 'blue'
                    else:
                        edgecolor = facecolor = 'red'
                    # print(dp['_XYCoordinatesProjection'][0],
                    #       dp['_XYCoordinatesProjection'][1][0] - dp['_XYCoordinatesProjection'][0][0],
                    #       dp['_XYCoordinatesProjection'][2][1] - dp['_XYCoordinatesProjection'][1][1],)
                    ax.add_patch(
                        patches.Rectangle(
                            dp['_XYCoordinatesProjection'][0],
                            dp['_XYCoordinatesProjection'][1][0] - dp['_XYCoordinatesProjection'][0][0],
                            dp['_XYCoordinatesProjection'][2][1] - dp['_XYCoordinatesProjection'][1][1],
                            edgecolor=edgecolor,
                            facecolor=facecolor,
                            fill=True
                        )
                    )
                    vi.append(
                        QGraphicsRectItem(dp['_XYCoordinatesProjection'][0][0], dp['_XYCoordinatesProjection'][0][1],
                                          dp['_XYCoordinatesProjection'][1][0] - dp['_XYCoordinatesProjection'][0][0],
                                          dp['_XYCoordinatesProjection'][2][1] - dp['_XYCoordinatesProjection'][1][
                                              1], ))
                    # img = cv2.rectangle(img,dp['_XYCoordinatesProjection'][0], dp['_XYCoordinatesProjection'][2],thickness=3)
                elif dp['_DesignParametertype'] == 3:
                    for _, sub_dp in dp['_DesignObj']._DesignParameter.items():
                        stack.append(sub_dp)
        # ax.add_patch(patches.Rectangle(
        #
        # ))
        plt.axis([0, 8300, -2500, 2500])
        plt.show()
        return vi
        # cv2.imshow('debug', img)
        # cv2.waitKey(0)

    def build_IST_qt(self, qt_DesignParameter):
        stack = [qt_dp_items[1] for qt_dp_items in qt_DesignParameter.items()]
        while stack:
            dp = stack.pop(0)._DesignParameter
            if dp['_DesignParametertype'] == 1 or dp['_DesignParametertype'] == 2:
                if dp['_Layer'] in self.interval_tree_by_layer:
                    self.interval_tree_by_layer[dp['_Layer']].add_element_node(dp)
                else:
                    self.interval_tree_by_layer[dp['_Layer']] = IST(direction='horizontal')
                    self.interval_tree_by_layer[dp['_Layer']].add_element_node(dp)
            # elif dp['_DesignParametertype'] == 2:
            #     if dp['_Layer'] in self.interval_tree_by_layer:
            #         self.interval_tree_by_layer[dp['_Layer']].add_element_node(dp)
            #     else:
            #         self.interval_tree_by_layer[dp['_Layer']] = IST(direction='horizontal')
            #         self.interval_tree_by_layer[dp['_Layer']].add_element_node(dp)
            elif dp['_DesignParametertype'] == 3:
                stack.extend([qt_dp_items[1] for qt_dp_items in dp['_ModelStructure'].items()])

    def build_IST(self, _DesignParameter):
        stack = [dp_items[1] for dp_items in _DesignParameter.items()]
        while stack:
            dp = stack.pop(0)
            if dp['_DesignParametertype'] == 1 or dp['_DesignParametertype'] == 2:
                if dp['_Layer'] in self.interval_tree_by_layer:
                    self.interval_tree_by_layer[dp['_Layer']].add_element_node(dp)
                else:
                    self.interval_tree_by_layer[dp['_Layer']] = IST(direction='horizontal')
                    self.interval_tree_by_layer[dp['_Layer']].add_element_node(dp)
            # elif dp['_DesignParametertype'] == 2:
            #     if dp['_Layer'] in self.interval_tree_by_layer:
            #         self.interval_tree_by_layer[dp['_Layer']].add_element_node(dp)
            #     else:
            #         self.interval_tree_by_layer[dp['_Layer']] = IST(direction='horizontal')
            #         self.interval_tree_by_layer[dp['_Layer']].add_element_node(dp)
            elif dp['_DesignParametertype'] == 3:
                stack.extend([dp_items[1] for dp_items in dp['_DesignObj']._DesignParameter.items()])

    def search_intersection_qt(self, qt_dp):
        dp = qt_dp._DesignParameter
        if dp['_Layer'] not in self.interval_tree_by_layer:
            return None
        if dp['_DesignParametertype'] == 1:
            xy_points = dp['_XYCoordinatesProjection']
            x_min, x_max, y_min, y_max = min([xy[0] for xy in xy_points]), max([xy[0] for xy in xy_points]), min(
                [xy[1] for xy in xy_points]), max([xy[1] for xy in xy_points])
        elif dp['_DesignParametertype'] == 2:
            try:
                intersection_point_list = self.search_path_intersection_points(dp)
                intersected_dp_hierarchy_names = [double_list[0] for double_list in intersection_point_list if
                                                  double_list]
                intersected_dp_hierarchy_names.insert(0, dp)
                return intersected_dp_hierarchy_names
            except:
                print('db')
        vertical_tree = IST(direction='vertical')
        for x_intersection_dp in sorted(self.interval_tree_by_layer[dp['_Layer']][x_min:x_max + 1]):
            vertical_tree.add_element_node(dp=x_intersection_dp.data[0], idx=x_intersection_dp.data[1])

        intersected_node = sorted(vertical_tree[y_min:y_max + 1])
        del vertical_tree

        intersected_dp_hierarchy_names = [[node.data[0]['_Hierarchy'], node.data[1]] for node in intersected_node]
        intersected_dp_hierarchy_names.insert(0, dp)

        return intersected_dp_hierarchy_names

    def search_path_intersection_points(self, dp):
        x_min_list, x_max_list, y_min_list, y_max_list = [], [], [], []
        intersection_point_list = []
        for i in range(len(dp['_XYCoordinates'][0])):
            if i + 1 != len(dp['_XYCoordinates'][0]):
                if dp['_XYCoordinates'][0][i][0] == dp['_XYCoordinates'][0][i + 1][0]:
                    direction = 'vertical'
                    if dp['_XYCoordinates'][0][i][1] < dp['_XYCoordinates'][0][i + 1][1]:
                        direction += 'up'
                    else:
                        direction += 'down'
                else:
                    direction = 'horizontal'
                    if dp['_XYCoordinates'][0][i][0] < dp['_XYCoordinates'][0][i + 1][0]:
                        direction += 'right'
                    else:
                        direction += 'left'

                if 'horizontal' in direction:
                    if 'right' in direction:
                        x_min_list.append(dp['_XYCoordinates'][0][i][0])
                        x_max_list.append(dp['_XYCoordinates'][0][i][0] + 1)
                    else:
                        x_min_list.append(dp['_XYCoordinates'][0][i][0] - 1)
                        x_max_list.append(dp['_XYCoordinates'][0][i][0])
                    y_min_list.append(dp['_XYCoordinates'][0][i][1] - dp['_Width'] / 2)
                    y_max_list.append(dp['_XYCoordinates'][0][i][1] + dp['_Width'] / 2)
                elif 'vertical' in direction:
                    x_min_list.append(dp['_XYCoordinates'][0][i][0] - dp['_Width'] / 2)
                    x_max_list.append(dp['_XYCoordinates'][0][i][0] + dp['_Width'] / 2)
                    if 'up' in direction:
                        y_min_list.append(dp['_XYCoordinates'][0][i][1])
                        y_max_list.append(dp['_XYCoordinates'][0][i][1] + 1)
                    else:
                        y_min_list.append(dp['_XYCoordinates'][0][i][1] - 1)
                        y_max_list.append(dp['_XYCoordinates'][0][i][1])
            else:
                if 'horizontal' in direction:
                    if 'right' in direction:
                        x_min_list.append(dp['_XYCoordinates'][0][i][0] - 1)
                        x_max_list.append(dp['_XYCoordinates'][0][i][0])
                    else:
                        x_min_list.append(dp['_XYCoordinates'][0][i][0])
                        x_max_list.append(dp['_XYCoordinates'][0][i][0] + 1)
                    y_min_list.append(dp['_XYCoordinates'][0][i][1] - dp['_Width'] / 2)
                    y_max_list.append(dp['_XYCoordinates'][0][i][1] + dp['_Width'] / 2)
                elif 'vertical' in direction:
                    x_min_list.append(dp['_XYCoordinates'][0][i][0] - dp['_Width'] / 2)
                    x_max_list.append(dp['_XYCoordinates'][0][i][0] + dp['_Width'] / 2)
                    if 'up' in direction:
                        y_min_list.append(dp['_XYCoordinates'][0][i][1] - 1)
                        y_max_list.append(dp['_XYCoordinates'][0][i][1])
                    else:
                        y_min_list.append(dp['_XYCoordinates'][0][i][1])
                        y_max_list.append(dp['_XYCoordinates'][0][i][1] + 1)

        for i, x_min in enumerate(x_min_list):
            vertical_tree = IST(direction='vertical')
            for x_intersection_dp in sorted(self.interval_tree_by_layer[dp['_Layer']][x_min:x_max_list[i]]):
                vertical_tree.add_element_node(dp=x_intersection_dp.data[0], idx=x_intersection_dp.data[1])

            intersected_node = sorted(vertical_tree[y_min_list[i]:y_max_list[i]])
            del vertical_tree

            for node in intersected_node:
                print(f'hierarchy: {node.data[0]["_Hierarchy"]}')
                print(f'idx = {node.data[1]}')
            intersection_point_list.append( \
                [[node.data[0]['_Hierarchy'][node.data[1][0]][node.data[1][1]], node.data[1]] if type(node.data[1]) == list \
                 else [node.data[0]['_Hierarchy'][node.data[1]], node.data[1]] \
                 for node in intersected_node])
        return intersection_point_list

    def search_intersection(self, dp):
        # if dp['_DesignParametertype'] == 3:
        #     x_min = dp['_XYCoordinates'][0][0]
        #     x_max = x_min +1
        #     y_min = dp['_XYCoordinates'][0][1]
        #     y_max = y_min + 1
        # elif dp['_Layer'] not in self.interval_tree_by_layer:
        #     return None
        #
        if dp['_DesignParametertype'] == 1:
            xy_points = dp['_XYCoordinatesProjection'][0]
            x_min, x_max, y_min, y_max = min([xy[0] for xy in xy_points]), max([xy[0] for xy in xy_points]), min(
                [xy[1] for xy in xy_points]), max([xy[1] for xy in xy_points])
        elif dp['_DesignParametertype'] == 2:
            try:
                intersection_point_list = self.search_path_intersection_points(dp)
                intersected_dp_hierarchy_names = [double_list[0] for double_list in intersection_point_list if
                                                  double_list]
                intersected_dp_hierarchy_names.insert(0, dp)
                return intersected_dp_hierarchy_names
            except:
                traceback.print_exc()
                print('db')
            # # #TODO
            # #path case update
            # if len(dp['_XYCoordinates'][0]) != 2:
            #     return None
            # # x_min, x_max, y_min, y_max = dp['_XYCoordinates'][0][0][0], dp['_XYCoordinates'][0][-1][0], dp['_XYCoordinates'][0][0][1], dp['_XYCoordinates'][0][-1][1]
            # x_min, x_max, y_min, y_max = dp['_XYCoordinates'][0][0][0]-dp['_Width'], dp['_XYCoordinates'][0][0][0]+dp['_Width'], \
            #                              min(dp['_XYCoordinates'][0][0][1], dp['_XYCoordinates'][0][-1][1]),\
            #                              max(dp['_XYCoordinates'][0][0][1], dp['_XYCoordinates'][0][-1][1])
        elif dp['_DesignParametertype'] == 3:
            x_min = dp['_XYCoordinates'][0][0]
            x_max = x_min
            y_min = dp['_XYCoordinates'][0][1]
            y_max = y_min
            vertical_tree = IST(direction='vertical')
            for layer_interval_tree in self.interval_tree_by_layer.values():
                for x_intersection_dp in sorted(layer_interval_tree[x_min:x_max + 1]):
                    vertical_tree.add_element_node(dp=x_intersection_dp.data[0], idx=x_intersection_dp.data[1])

            intersected_node = sorted(vertical_tree[y_min:y_max + 1])
            del vertical_tree
            intersected_dp_hierarchy_names = [[node.data[0]['_Hierarchy'][node.data[1][0]][node.data[1][1]], node.data[1]] if type(node.data[1]) == list
                                              else [node.data[0]['_Hierarchy'][node.data[1]], node.data[1]]
                                              for node in intersected_node]
            intersected_dp_hierarchy_names.insert(0, dp)
            return intersected_dp_hierarchy_names

        vertical_tree = IST(direction='vertical')
        for x_intersection_dp in sorted(self.interval_tree_by_layer[dp['_Layer']][x_min:x_max + 1]):
            vertical_tree.add_element_node(dp=x_intersection_dp.data[0], idx=x_intersection_dp.data[1])

        intersected_node = sorted(vertical_tree[y_min:y_max + 1])
        del vertical_tree

        intersected_dp_hierarchy_names = [[node.data[0]['_Hierarchy'][node.data[1][0]][node.data[1][1]], node.data[1]] if type(node.data[1]) == list
                                          else [node.data[0]['_Hierarchy'][node.data[1]], node.data[1]]
                                          for node in intersected_node]
        intersected_dp_hierarchy_names.insert(0, dp)

        return intersected_dp_hierarchy_names


class IST(IntervalTree):
    def __init__(self, intervals=None, direction='horizontal'):
        super(IST, self).__init__(intervals)
        if direction == 'horizontal':
            self.direction = 'horizontal'
        elif direction == 'vertical':
            self.direction = 'vertical'
        else:
            raise Exception("Direction should be horizontal or vertical")

    def add_element_node(self, dp, idx=None):
        if dp['_DesignParametertype'] == 1:
            self.add_boundary_node(dp, idx)
        elif dp['_DesignParametertype'] == 2:
            self.add_path_node(dp, idx)

    def add_path_node(self, path_dp, idx=None):
        if '_XYCoordinatesProjection' not in path_dp:
            warnings.warn(f'{path_dp} designParameter does not have XY coordinates.')
            return None
        if self.direction == 'horizontal':
            for idx, xy_points_list in enumerate(path_dp['_XYCoordinatesProjection']):
                for idx2, xy_points in enumerate(xy_points_list):
                    if self.direction == 'horizontal':
                        lo, hi = min([xy[0] for xy in xy_points]), max([xy[0] for xy in xy_points])
                    elif self.direction == 'vertical':
                        lo, hi = min([xy[1] for xy in xy_points]), max([xy[1] for xy in xy_points])
                    self.addi(lo, hi, [path_dp, [idx, idx2]])
        elif self.direction == 'vertical':
            xy_points = path_dp['_XYCoordinatesProjection'][idx[0]][idx[1]]
            if self.direction == 'horizontal':
                lo, hi = min([xy[0] for xy in xy_points]), max([xy[0] for xy in xy_points])
            elif self.direction == 'vertical':
                lo, hi = min([xy[1] for xy in xy_points]), max([xy[1] for xy in xy_points])
            self.addi(lo, hi, [path_dp, idx])

    def add_boundary_node(self, boundary_dp, idx=None):
        if '_XYCoordinatesProjection' not in boundary_dp:
            warnings.warn(f'{boundary_dp} designParameter does not have XY coordinates.')
            return None
        if self.direction == 'horizontal':
            for idx, xy_points in enumerate(boundary_dp['_XYCoordinatesProjection']):
                # xy_points = boundary_dp['_XYCoordinatesProjection']
                if self.direction == 'horizontal':
                    lo, hi = min([xy[0] for xy in xy_points]), max([xy[0] for xy in xy_points])
                elif self.direction == 'vertical':
                    lo, hi = min([xy[1] for xy in xy_points]), max([xy[1] for xy in xy_points])

                self.addi(lo, hi, [boundary_dp, idx])
        elif self.direction == 'vertical':
            xy_points = boundary_dp['_XYCoordinatesProjection'][idx]
            if self.direction == 'horizontal':
                lo, hi = min([xy[0] for xy in xy_points]), max([xy[0] for xy in xy_points])
            elif self.direction == 'vertical':
                lo, hi = min([xy[1] for xy in xy_points]), max([xy[1] for xy in xy_points])
            self.addi(lo, hi, [boundary_dp, idx])


class Widget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        from model import gds2generator
        xy_gen = gds2generator.GDS2Generator()
        xy_gen.load_gds('./tt3.gds')
        xy_gen.set_root_cell('tt3')
        gf = GeometricField()
        gf.xy_projection_to_main_coordinates_system(xy_gen.root_cell._DesignParameter)
        vi_list = gf.draw_by_projection_xy(xy_gen.root_cell._DesignParameter)

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('drawRect')
        self.scene = QGraphicsScene()
        view = Cview()
        view.setScene(self.scene)
        view.scale(1, -1)
        view.setInteractive(True)
        layout = QVBoxLayout()
        layout.addWidget(view)
        # self.scene.setSceneRect(-10000,-10000,20000,20000)
        self.setLayout(layout)
        for vi in vi_list:
            self.scene.addItem(vi)
        self.show()

    # def paintEvent(self, e):
    #     qp = QPainter()
    #     qp.begin(self)
    #     # self.draw_rect(qp)
    #     qp.end()
    #
    # def draw_rect(self, qp):
    #     qp.setBrush(QColor(180, 100, 160))
    #     qp.setPen(QPen(QColor(60, 60, 60), 3))
    #     qp.drawRect(20, 20, 100, 100)
    #
    #     qp.setBrush(QColor(40, 150, 20))
    #     qp.setPen(QPen(Qt.blue, 2))
    #     qp.drawRect(180, 120, 50, 120)
    #
    #     qp.setBrush(Qt.yellow)
    #     qp.setPen(QPen(Qt.red, 5))
    #     qp.drawRect(280, 30, 80, 40)


class Cview(QGraphicsView):
    def __init__(self):
        super(Cview, self).__init__()
        self.setMouseTracking(True)

    def wheelEvent(self, QWheelEvent):
        zoomInFactor = 1.25
        zoomOutFactor = 1 / zoomInFactor
        self.setTransformationAnchor(QGraphicsView.NoAnchor)
        self.setResizeAnchor(QGraphicsView.NoAnchor)

        oldPosition = self.mapToScene(QWheelEvent.pos())

        if QWheelEvent.angleDelta().y() > 0:
            zoom = zoomInFactor
        else:
            zoom = zoomOutFactor
        self.scale(zoom, zoom)

        newPosition = self.mapToScene(QWheelEvent.pos())

        delta = newPosition - oldPosition
        self.translate(delta.x(), delta.y())


if __name__ == '__main__':
    # root = ISTnode(17,19,1,color='black')
    # root.insert(5,11,2)
    # root.insert(20,22,3)
    # root.insert(15,18,4)
    # root.insert(4,8,5)
    # root.insert(16,23,6)
    debug = False
    if debug:
        from model import gds2generator

        # xy_gen = gds2generator.GDS2Generator()
        # xy_gen.load_gds('./xy_test34.gds')
        # xy_gen.set_root_cell('xy_test_34')
        xy_gen = gds2generator.GDS2Generator()
        xy_gen.load_gds('./INV2.gds')
        xy_gen.set_root_cell('INV')
        gf = GeometricField()
        gf.xy_projection_to_main_coordinates_system(xy_gen.root_cell._DesignParameter)
        gf.draw_by_projection_xy(xy_gen.root_cell._DesignParameter)
        gf.build_IST(xy_gen.root_cell._DesignParameter)

    visualQT = False
    if visualQT:
        app = QApplication(sys.argv)
        ex = Widget()
        sys.exit(app.exec_())
