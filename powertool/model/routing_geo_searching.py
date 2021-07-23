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
    rotate_0 = np.array([[1,0],
                         [0,1]])
    rotate_90 = np.array([[0,-1],
                          [1,0]])
    rotate_180 = np.array([[-1,0],
                           [0,-1]])
    rotate_270 = np.array([[0,1],
                           [-1,0]])

    reflect_off = np.array([[1,0],
                            [0,1]])

    reflect_on = np.array([[1,0],
                           [0,-1]])


def matrix_dot(tf_matrix, xy):
    return tf_matrix.dot(xy).tolist()

def convert_angle_to_matrix(angle):
    if angle==None:
        angle=0
    return tf_matrix.__dict__['rotate_'+str(int(angle))]

def convert_reflect_to_matrix(reflect):
    if reflect == None or reflect[0] == 0:
        return tf_matrix.reflect_off
    else:
        return tf_matrix.reflect_on

class GeometricField:
    def __init__(self):
        self.interval_tree_by_layer = dict()
        self.stick_diagram = StickDiagram._StickDiagram()

    def xy_projection_to_main_coordinates_system_qt(self,qt_designParameter):
        for name, qt_dp in qt_designParameter.items():
            self.qt_design_parameter_projection(qt_dp,[name])

    def qt_design_parameter_projection(self, qt_dp, structure_hierarchy=[], reflect=tf_matrix.reflect_off, angle=tf_matrix.rotate_0, base_xy = [0,0]):
        dp = qt_dp._DesignParameter
        if dp['_DesignParametertype'] == 1:
            for xy_pair in dp['_XYCoordinates']:
                five_point_xy = self.stick_diagram.CenterCoordinateAndWidth2XYCoordinate(xy_pair,dp['_XWidth'],dp['_YWidth'])
                # transformed_five_point_xy = [base_xy+angle.dot(reflect).dot(xy) for xy in five_point_xy]
                transformed_five_point_xy = [base_xy+reflect.dot(angle).dot(xy) for xy in five_point_xy]
                transformed_five_point_xy_ordered = self.stick_diagram.MinMaxXY2XYCoordinate(self.stick_diagram.XYCoordinate2MinMaxXY(transformed_five_point_xy))
                if '_XYCoordinatesProjection' in dp:
                    dp['_XYCoordinatesProjection'].append(transformed_five_point_xy_ordered)
                else:
                    dp['_XYCoordinatesProjection'] = [transformed_five_point_xy_ordered]
                # dp['_XYCoordinatesProjection'] = transformed_five_point_xy_ordered
                dp['_Hierarchy'] = structure_hierarchy
                # return base_xy + angle.dot(reflect).dot(xy_pair)

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
                    if sub_dp['_DesignParametertype'] == 1 or sub_dp['_DesignParametertype'] == 3:
                        structure_hierarchy_tmp = copy.deepcopy(structure_hierarchy)
                        structure_hierarchy_tmp[-1] += f'[{sref_idx}]'
                        structure_hierarchy_tmp.append(name)
                        self.qt_design_parameter_projection(sub_qt_dp,structure_hierarchy=structure_hierarchy_tmp, reflect=sub_reflect, angle=sub_angle, base_xy=base_xy)





    def xy_projection_to_main_coordinates_system(self,designParameter):
        for name, dp in designParameter.items():
            self.design_parameter_projection(dp,[name])

    def design_parameter_projection(self, dp, structure_hierarchy=[], reflect=tf_matrix.reflect_off, angle=tf_matrix.rotate_0, base_xy = [0,0]):
        # for _, dp in _DesignParameter.items():
        if dp['_DesignParametertype'] == 1:
            for xy_pair in dp['_XYCoordinates']:
                five_point_xy = self.stick_diagram.CenterCoordinateAndWidth2XYCoordinate(xy_pair,dp['_XWidth'],dp['_YWidth'])
                # transformed_five_point_xy = [base_xy+angle.dot(reflect).dot(xy) for xy in five_point_xy]
                transformed_five_point_xy = [base_xy+reflect.dot(angle).dot(xy) for xy in five_point_xy]
                transformed_five_point_xy_ordered = self.stick_diagram.MinMaxXY2XYCoordinate(self.stick_diagram.XYCoordinate2MinMaxXY(transformed_five_point_xy))
                if '_XYCoordinatesProjection' in dp:
                    dp['_XYCoordinatesProjection'].append(transformed_five_point_xy_ordered)
                else:
                    dp['_XYCoordinatesProjection'] = [transformed_five_point_xy_ordered]
                # dp['_XYCoordinatesProjection'] = transformed_five_point_xy_ordered
                dp['_Hierarchy'] = structure_hierarchy
                # return base_xy + angle.dot(reflect).dot(xy_pair)

        elif dp['_DesignParametertype'] == 3:
            # structure_hierarchy.append(dp['_ElementName'])
            for sref_idx in len(0, dp['_XYCoordinates']):
                base_xy = base_xy + angle.dot(reflect).dot(dp['_XYCoordinates'][sref_idx])
                sub_reflect = convert_reflect_to_matrix(dp['_Reflect']).dot(reflect)
                sub_angle = convert_angle_to_matrix(dp['_Angle']).dot(angle)
                # base_xy = base_xy + angle.dot(reflect).dot(dp['_XYCoordinates'][0])
                # sub_reflect = reflect.dot(convert_reflect_to_matrix(dp['_Reflect']))
                # sub_angle = angle.dot(convert_angle_to_matrix(dp['_Angle']))
                for name, sub_dp in dp['_DesignObj']._DesignParameter.items():
                    if sub_dp['_DesignParametertype'] == 1 or sub_dp['_DesignParametertype'] == 3:
                        structure_hierarchy_tmp = copy.deepcopy(structure_hierarchy)
                        structure_hierarchy_tmp[-1] += f'[{sref_idx}]'
                        structure_hierarchy_tmp.append(name)
                        self.design_parameter_projection(sub_dp,structure_hierarchy=structure_hierarchy_tmp, reflect=sub_reflect, angle=sub_angle, base_xy=base_xy)

    def draw_by_projection_xy(self, _DesignParameter):
        fig, ax = plt.subplots()
        vi = []
        blue = (255,0,0)
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
                            edgecolor= edgecolor,
                            facecolor= facecolor,
                            fill = True
                        )
                    )
                    vi.append(QGraphicsRectItem(dp['_XYCoordinatesProjection'][0][0],dp['_XYCoordinatesProjection'][0][1],dp['_XYCoordinatesProjection'][1][0] - dp['_XYCoordinatesProjection'][0][0],
                                                dp['_XYCoordinatesProjection'][2][1] - dp['_XYCoordinatesProjection'][1][1],))
                    # img = cv2.rectangle(img,dp['_XYCoordinatesProjection'][0], dp['_XYCoordinatesProjection'][2],thickness=3)
                elif dp['_DesignParametertype'] == 3:
                    for _, sub_dp in dp['_DesignObj']._DesignParameter.items():
                        stack.append(sub_dp)
        # ax.add_patch(patches.Rectangle(
        #
        # ))
        plt.axis([0,8300,-2500,2500])
        plt.show()
        return vi
        # cv2.imshow('debug', img)
        # cv2.waitKey(0)


    def build_IST_qt(self,qt_DesignParameter):
        stack = [qt_dp_items[1] for qt_dp_items in qt_DesignParameter.items()]
        while stack:
            dp = stack.pop(0)._DesignParameter
            if dp['_DesignParametertype'] == 1:
                if dp['_Layer'] in self.interval_tree_by_layer:
                    self.interval_tree_by_layer[dp['_Layer']].add_boundary_node(dp)
                else:
                    self.interval_tree_by_layer[dp['_Layer']] = IST(direction='horizontal')
                    self.interval_tree_by_layer[dp['_Layer']].add_boundary_node(dp)
            elif dp['_DesignParametertype'] == 3:
                stack.extend([qt_dp_items[1] for qt_dp_items in dp['_ModelStructure'].items()])

    def build_IST(self,_DesignParameter):
        stack = [dp_items[1] for dp_items in _DesignParameter.items()]
        while stack:
            dp = stack.pop(0)
            if dp['_DesignParametertype'] == 1:
                if dp['_Layer'] in self.interval_tree_by_layer:
                    self.interval_tree_by_layer[dp['_Layer']].add_boundary_node(dp)
                else:
                    self.interval_tree_by_layer[dp['_Layer']] = IST(direction='horizontal')
                    self.interval_tree_by_layer[dp['_Layer']].add_boundary_node(dp)
            elif dp['_DesignParametertype'] == 3:
                stack.extend([dp_items[1] for dp_items in dp['_DesignObj']._DesignParameter.items()])


    def search_intersection_qt(self, qt_dp):
        dp = qt_dp._DesignParameter
        if dp['_Layer'] not in self.interval_tree_by_layer:
            return None
        if dp['_DesignParametertype'] == 1:
            xy_points = dp['_XYCoordinatesProjection']
            x_min, x_max, y_min, y_max = min([xy[0] for xy in xy_points]), max([xy[0] for xy in xy_points]), min([xy[1] for xy in xy_points]), max([xy[1] for xy in xy_points])
        elif dp['_DesignParametertype'] == 2:
            #TODO
            #path case update
            if len(dp['_XYCoordinates'][0]) != 2:
                return None
            # x_min, x_max, y_min, y_max = dp['_XYCoordinates'][0][0][0], dp['_XYCoordinates'][0][-1][0], dp['_XYCoordinates'][0][0][1], dp['_XYCoordinates'][0][-1][1]
            x_min, x_max, y_min, y_max = dp['_XYCoordinates'][0][0][0]-dp['_Width'], dp['_XYCoordinates'][0][0][0]+dp['_Width'], \
                                         min(dp['_XYCoordinates'][0][0][1], dp['_XYCoordinates'][0][-1][1]),\
                                         max(dp['_XYCoordinates'][0][0][1], dp['_XYCoordinates'][0][-1][1])

        vertical_tree = IST(direction='vertical')
        for x_intersection_dp in sorted(self.interval_tree_by_layer[dp['_Layer']][x_min:x_max+1]):
            vertical_tree.add_boundary_node(boundary_dp=x_intersection_dp.data[0],idx= x_intersection_dp.data[1])

        intersected_node = sorted(vertical_tree[y_min:y_max+1])
        del vertical_tree

        intersected_dp_hierarchy_names = [ [node.data[0]['_Hierarchy'], node.data[1]] for node in intersected_node ]
        intersected_dp_hierarchy_names.insert(0,dp)


        return intersected_dp_hierarchy_names

    def search_intersection(self, dp):
        if dp['_Layer'] not in self.interval_tree_by_layer:
            return None
        if dp['_DesignParametertype'] == 1:
            xy_points = dp['_XYCoordinatesProjection']
            x_min, x_max, y_min, y_max = min([xy[0] for xy in xy_points]), max([xy[0] for xy in xy_points]), min([xy[1] for xy in xy_points]), max([xy[1] for xy in xy_points])
        elif dp['_DesignParametertype'] == 2:
            #TODO
            #path case update
            if len(dp['_XYCoordinates'][0]) != 2:
                return None
            # x_min, x_max, y_min, y_max = dp['_XYCoordinates'][0][0][0], dp['_XYCoordinates'][0][-1][0], dp['_XYCoordinates'][0][0][1], dp['_XYCoordinates'][0][-1][1]
            x_min, x_max, y_min, y_max = dp['_XYCoordinates'][0][0][0]-dp['_Width'], dp['_XYCoordinates'][0][0][0]+dp['_Width'], \
                                         min(dp['_XYCoordinates'][0][0][1], dp['_XYCoordinates'][0][-1][1]),\
                                         max(dp['_XYCoordinates'][0][0][1], dp['_XYCoordinates'][0][-1][1])

        vertical_tree = IST(direction='vertical')
        for x_intersection_dp in sorted(self.interval_tree_by_layer[dp['_Layer']][x_min:x_max+1]):
            vertical_tree.add_boundary_node(boundary_dp=x_intersection_dp.data[0],idx= x_intersection_dp.data[1])

        intersected_node = sorted(vertical_tree[y_min:y_max+1])
        del vertical_tree

        intersected_dp_hierarchy_names = [ [node.data[0]['_Hierarchy'], node.data[1]] for node in intersected_node ]
        intersected_dp_hierarchy_names.insert(0,dp)


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

    def add_boundary_node(self,boundary_dp,idx=None):
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

                self.addi(lo,hi,[boundary_dp,idx])
        elif self.direction == 'vertical':
            xy_points = boundary_dp['_XYCoordinatesProjection'][idx]
            if self.direction == 'horizontal':
                lo, hi = min([xy[0] for xy in xy_points]), max([xy[0] for xy in xy_points])
            elif self.direction == 'vertical':
                lo, hi = min([xy[1] for xy in xy_points]), max([xy[1] for xy in xy_points])
            self.addi(lo,hi,[boundary_dp,idx])


# class IST:
#     def __init__(self, direction:str):
#         if direction == None:
#             self.direction = 'horizontal' # or vertical
#         else:
#             self.direction = direction
#         self.stickdiagram = StickDiagram._StickDiagram()
#         self.root = None
#
#     def add_node(self, dp):
#         pass
#
#     def add_boundary_node(self,boundary_dp):
#         xy_vertex_list = boundary_dp['_XYCoordinatesProjection']
#         # xy_vertex_list = self.stickdiagram.CenterCoordinateAndWidth2XYCoordinate(boundary_dp['_XYCoordinates'][0],
#         #                                                                          boundary_dp['_XWidth'],
#         #                                                                          boundary_dp['_YWidth'])
#         if self.direction is 'horizontal':
#             lo = xy_vertex_list[0][0]
#             hi = xy_vertex_list[1][0]
#             self.insert(lo,hi,boundary_dp['_Hierarchy'])
#         elif self.direction is 'vertical':
#             lo = xy_vertex_list[0][1]
#             hi = xy_vertex_list[2][1]
#             self.insert(lo,hi,boundary_dp['_Hierarchy'])
#
#     def insert(self,lo,hi, element_id):
#         if self.root is None:
#             self.root = ISTnode(lo, hi, element_id, color=Color.black, parent=None)
#             return self.root
#
#         parent_node = self.root
#         while parent_node:          #BST
#             if lo < parent_node.lo:
#                 if parent_node.left:
#                     parent_node = parent_node.left
#                     continue
#                 else:
#                     child = ISTnode(lo,hi,element_id,color=Color.red,parent=parent_node)
#                     parent_node.left = child
#                     break
#
#             elif lo > parent_node.lo:
#                 if parent_node.right:
#                     parent_node = parent_node.right
#                     continue
#                 else:
#                     child = ISTnode(lo,hi,element_id,color=Color.red,parent=parent_node)
#                     parent_node.right = child
#                     break
#
#             else: #lo = parent_node.lo
#                 parent_node.element_id_overlap.append(element_id)
#                 return parent_node
#
#         # while child.parent.color == Color.red:
#         #     if child.parent == child.parent.parent.right: # parent is right node case
#         #         uncle = child.parent.parent.left
#         #         if uncle.color == Color.red: # Case : Parent and uncle is red -> Recoloring
#         #             uncle.color = Color.black
#         #             child.parent.color = Color.black
#         #             child.parent.parent.color = Color.red
#         #             child = child.parent.parent
#         #         elif child == child.parent.left:    #child is left node case
#         #             child = child.parent
#         #             self.left_rotate()
#
#
#     def left_rotate(self,node):
#         pass
#
#
#     def delete(self,lo,hi):
#         pass
#
#     def search(self,lo,hi):
#         pass
#
# class ISTnode:
#     def __init__(self, lo, hi, element_id, color=Color.red, parent = None):
#         self.parent = parent
#         self.left = None
#         self.right = None
#         self.color = color
#         self.lo = lo
#         self.hi = hi
#         self.hi_overlap = []
#         self.max_endpoint = hi
#         self.element_id = element_id
#         self.element_id_overlap = []
#
#     def insert(self,lo,hi, element_id):
#         if lo < self.lo:    # Insert left child
#             if self.left:
#                 self.left.insert(lo,hi,element_id)
#             else:
#                 self.left = ISTnode(lo,hi,element_id,parent=self)
#         elif lo > self.lo:  # Insert right child
#             if self.right:
#                 self.right.insert(lo,hi,element_id)
#             else:
#                 self.right = ISTnode(lo,hi,element_id, parent=self)
#
#             if hi > self.max_endpoint:
#                 self.max_endpoint = hi
#
#         # if lo == self.lo:
#         #     if element_id == self.element_id:
#         #         return
#         #     else:
#         #         self.hi_overlap.append(hi)
#         #         self.element_id_overlap.append(element_id)
#         #         if hi >= self.max_endpoint:
#         #             self.max_endpoint = hi
#         #
#
#         #Restructuring
#         #case1 sibling = black, self = red, child = red
#         # if self.sibling.color == Color.black and self.color == Color.red:
#
#
#
#     def delete(self,lo,hi):
#         """
#         #TODO implement delete functionality
#         Not Implemented Yet
#         :param lo:
#         :param hi:
#         :return:
#         """
#         if hi <self.lo:
#             new_child = self.left.delete(lo,hi)
#             self.left = new_child
#         elif lo > self.hi:
#             new_child = self.right.delete(lo,hi)
#             self.right = new_child
#         else:
#             if self.lo == lo and self.hi == hi:
#                 left, right = None, None
#                 if self.left:
#                     left = self.left
#                 if self.right:
#                     right = self.right
#
#                 if left and right:
#                     #todo height rearrangement
#                     pass
#                 elif left:
#                     return left
#                 elif right:
#                     return right
#                 else:
#                     del self

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
        view.scale(1,-1)
        view.setInteractive(True)
        layout= QVBoxLayout()
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
        super(Cview,self).__init__()
        self.setMouseTracking(True)

    def wheelEvent(self, QWheelEvent):
        zoomInFactor = 1.25
        zoomOutFactor = 1 / zoomInFactor
        self.setTransformationAnchor(QGraphicsView.NoAnchor)
        self.setResizeAnchor(QGraphicsView.NoAnchor)

        oldPosition = self.mapToScene(QWheelEvent.pos())

        if QWheelEvent.angleDelta().y() >0 :
            zoom = zoomInFactor
        else:
            zoom = zoomOutFactor
        self.scale(zoom,zoom)

        newPosition = self.mapToScene(QWheelEvent.pos())

        delta = newPosition - oldPosition
        self.translate(delta.x(),delta.y())

if __name__ == '__main__':
    # root = ISTnode(17,19,1,color='black')
    # root.insert(5,11,2)
    # root.insert(20,22,3)
    # root.insert(15,18,4)
    # root.insert(4,8,5)
    # root.insert(16,23,6)
    debug = False
    if debug :
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