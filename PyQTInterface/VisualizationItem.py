import sys
import os
import re
import traceback
import warnings

import PyQt5.QtGui

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import user_setup
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import copy

from PyQTInterface import list_manager

# from PyCodes import QTInterface

from PyQTInterface import LayerInfo
from PyQTInterface.layermap import LayerReader
from PyQTInterface.layermap import DisplayReader
import lab_feature

# from import list_ma

from PyQTInterface import userDefineExceptions
DEBUG = True
scaleValue = 1

class ElementBlock:
    def __init__(self, block_traits=None):
        if block_traits is None:
            self.block_traits = dict(_XYCoordinates = None)
        else:
            self.block_traits = block_traits
        self.pen = QPen()
        self.brush = QBrush()



    def update_traits(self,block_traits)-> QRect:
        self.block_traits.update(block_traits)

        if self.block_traits["_XYCoordinates"] is None:
            self.block_traits["_XYCoordinates"] = [[0, 0]]

        if type(self.block_traits['_Width']) == str:
            if not self.block_traits["_Width"]:
                print("ERROR: Unvalid Width")
                return None
            self.block_traits['_Width'] = int(self.block_traits['_Width'])

        if type(self.block_traits['_Height']) == str:
            if not self.block_traits["_Height"]:
                print("ERROR: Unvalid Height")
                return None
            self.block_traits['_Height'] = int(self.block_traits['_Height'])

        if self.block_traits["_Pattern"] not in ['X', 'blank']:
            color_name = \
            DisplayReader._DisplayDict[self.block_traits['_LayerName'] + self.block_traits['_DatatypeName']][
                'Fill'].name
            color_patt_name = color_name + self.block_traits["_Pattern"]
            if color_patt_name not in DisplayReader._ColorPatternDict:
                color = \
                DisplayReader._DisplayDict[self.block_traits['_LayerName'] + self.block_traits['_DatatypeName']][
                    'Fill']
                qpix = DisplayReader._PatternDict[self.block_traits["_Pattern"]].create_qbit(color)
                DisplayReader._DisplayDict[color_patt_name] = qpix

        self.pen.setColor(self.block_traits["_Outline"])
        self.pen.setDashPattern(self.block_traits['_LinePattern'])
        self.pen.setCapStyle(Qt.RoundCap)
        self.pen.setWidth(self.block_traits['_LineSize'] + 2)
        self.brush = QBrush()
        self.brush.setColor(self.block_traits["_Color"])

        if self.block_traits['_DesignParametertype'] in [1,2]:
            return QRectF(0,
                        0,
                        self.block_traits["_Width"] * scaleValue,
                        self.block_traits["_Height"] * scaleValue)
        elif self.block_traits['_DesignParametertype'] == 11:
            idx = 0 # this is temporal...
            #TODO
            #get index from Parent!
            return QPolygonF(
                [QPointF(p[0], p[1]) for p in self.block_traits['_XYCoordinates'][idx]]
            )

class _RectBlock(QGraphicsRectItem):
    highlighted_item_list = list()
    shallow_highlight_list = list()

    def __init__(self,_BlockTraits=None):
        super().__init__()
        self.setFlag(QGraphicsItem.ItemIsSelectable, False)
        self.shallow_highlight = False
        self.hover = False
        self.index = None
        self.highlight_flag = False
        self.flag_memory = False
        self.element_info = ElementBlock(_BlockTraits)

        if _BlockTraits is not None:
            rect = self.element_info.update_traits(_BlockTraits)
            self.setRect(rect)

    def updateTraits(self,_BlockTraits):
        rect = self.element_info.update_traits(_BlockTraits)
        self.setRect(rect)


    # def updateRect(self):
    #     # if self._BlockTraits['_DesignParametertype'] is "Boundary" :
    #     if self._BlockTraits["_XYCoordinates"] is None:
    #         self._BlockTraits["_XYCoordinates"] = [[0,0]]
    #
    #     if type(self._BlockTraits['_Width']) == str:
    #         if not self._BlockTraits["_Width"]:
    #             print("ERROR: Unvalid Width")
    #             return None
    #         self._BlockTraits['_Width'] = int(self._BlockTraits['_Width'])
    #
    #     if type(self._BlockTraits['_Height']) == str:
    #         if not self._BlockTraits["_Height"]:
    #             print("ERROR: Unvalid Height")
    #             return None
    #         self._BlockTraits['_Height'] = int(self._BlockTraits['_Height'])
    #
    #
    #     self.setRect(0,
    #                  0,
    #                  self._BlockTraits["_Width"]*scaleValue,
    #                  self._BlockTraits["_Height"]*scaleValue )
    #
    #     if self._BlockTraits["_Pattern"] not in ['X','blank']:
    #         color_name = DisplayReader._DisplayDict[self._BlockTraits['_LayerName'] + self._BlockTraits['_DatatypeName']][
    #             'Fill'].name
    #         color_patt_name = color_name + self._BlockTraits["_Pattern"]
    #         if color_patt_name not in DisplayReader._ColorPatternDict:
    #             color = DisplayReader._DisplayDict[self._BlockTraits['_LayerName'] + self._BlockTraits['_DatatypeName']][
    #                 'Fill']
    #             qpix = DisplayReader._PatternDict[self._BlockTraits["_Pattern"]].create_qbit(color)
    #             DisplayReader._DisplayDict[color_patt_name] = qpix
    #
    #     self.pen.setColor(self._BlockTraits["_Outline"])
    #     self.pen.setDashPattern(self._BlockTraits['_LinePattern'])
    #     self.pen.setCapStyle(Qt.RoundCap)
    #     self.pen.setWidth(self._BlockTraits['_LineSize'] + 2)
    #     self.brush = QBrush()
    #     self.brush.setColor(self._BlockTraits["_Color"])

    def paint(self, painter, option, widget=None):
        # list_manager.layer_visible_flag_dict[self.itemtrait['layer']] is False:
        #     self.setVisible(False)

        self.element_info.block_traits["_Color"].setAlphaF(1)

        # pen = QPen()
        # pen.setColor(self._BlockTraits["_Outline"])
        # pen.setDashPattern(self._BlockTraits['_LinePattern'])
        # pen.setCapStyle(Qt.RoundCap)
        # pen.setWidth(self._BlockTraits['_LineSize']+2)
        # # pen.setStyle(Qt.CustomDashLine)
        #
        # # pen.setWidth(5)
        #
        # brush = QBrush()
        # brush.setColor(self._BlockTraits["_Color"])
        #
        # # print(self.zValue())

        if self.isSelected() or self.highlight_flag:
            # self._BlockTraits["_Color"].setAlphaF(1)
            # self.setZValue(self.zValue()*10000)
            # print("HighLighted",self.zValue())
            self.flag_memory = True
            self.element_info.pen.setStyle(Qt.SolidLine)
            # pen.setColor(self._BlockTraits["_Outline"])
            color = Qt.GlobalColor.white if user_setup._Night_mode else Qt.GlobalColor.black
            self.element_info.pen.setColor(color)
            self.element_info.pen.setWidth(5)
            # self.setZValue(1)
        elif self.shallow_highlight:
            self.flag_memory = True
            self.element_info.pen.setStyle(Qt.DotLine)
            self.element_info.pen.setColor(Qt.GlobalColor.darkGreen)
            self.element_info.pen.setWidth(7)
        elif self.hover:
            self.flag_memory = True
            self.element_info.pen.setStyle(Qt.DotLine)
            self.element_info.pen.setColor(Qt.GlobalColor.darkCyan)
            self.element_info.pen.setWidth(5)
        elif self.flag_memory:
            self.flag_memory = False
            self.element_info.pen.setColor(self.element_info.block_traits["_Outline"])
            self.element_info.pen.setDashPattern(self.element_info.block_traits['_LinePattern'])
            self.element_info.pen.setWidth(self.element_info.block_traits['_LineSize'] + 2)
            self.element_info.brush.setColor(self.element_info.block_traits["_Color"])
        painter.setPen(self.element_info.pen)

        if self.element_info.block_traits["_Pattern"] not in ['X', 'blank']:
            if self.element_info.block_traits['_LayerName']+self.element_info.block_traits['_DatatypeName'] not in DisplayReader._DisplayDict or\
                self.element_info.block_traits["_Pattern"] not in DisplayReader._PatternDict:
                warnings.warn(f'Current process does not have information about object {self.element_info.block_traits["_ElementName"]}.')
                self.hide()
                return
            else:
                self.show()
        color_name = DisplayReader._DisplayDict[self.element_info.block_traits['_LayerName']+self.element_info.block_traits['_DatatypeName']]['Fill'].name
        color_patt_name =color_name+self.element_info.block_traits["_Pattern"]

        if self.element_info.block_traits["_Pattern"] == 'X':
            painter.drawLine(0,0,self.element_info.block_traits["_Width"],self.element_info.block_traits["_Height"])
            painter.drawLine(0,self.element_info.block_traits["_Height"],self.element_info.block_traits["_Width"],0)
        elif self.element_info.block_traits["_Pattern"] == 'blank':
            self.element_info.brush.setStyle(Qt.NoBrush)
        else:
            if color_patt_name not in DisplayReader._ColorPatternDict:
                color = DisplayReader._DisplayDict[self.element_info.block_traits['_LayerName']+self.element_info.block_traits['_DatatypeName']]['Fill']
                qpix = DisplayReader._PatternDict[self.element_info.block_traits["_Pattern"]].create_qbit(color)
                DisplayReader._DisplayDict[color_patt_name] = qpix
            qpix = DisplayReader._DisplayDict[color_patt_name]
            self.element_info.brush.setTexture(qpix)

        if '_type' in self.element_info.block_traits and self.element_info.block_traits['_type'] == 2:
            if self.element_info.block_traits['_Vertical']:
                x1 = self.element_info.block_traits['_Width'] / 2
                x2 = x1
                y1 = 0
                y2 = self.element_info.block_traits['_Height']
            else:
                #horizontal
                x1 = 0
                x2 = self.element_info.block_traits['_Width']
                y1 = self.element_info.block_traits['_Height']/2
                y2 = y1
            painter.drawLine(x1,y1,x2,y2)



        self.element_info.brush.setTransform(QTransform(painter.worldTransform().inverted()[0]))

        painter.setBrush(self.element_info.brush)

        painter.drawRect(self.rect())
        painter.setRenderHint(QPainter.Antialiasing)

    def layerName2paintTrait(self):

        try:
            DisplayInfo = DisplayReader._DisplayDict
            color = DisplayInfo[self.element_info.block_traits['_LayerName']+self.element_info.block_traits['_DatatypeName']]['Fill']
        except:
            self.warning=QMessageBox()
            self.warning.setText("There is no matching QT Color profile")
            print("Color Traits Error")
            self.warning.show()

    def restore_zvalue(self):
        self.setZValue(self.element_info.block_traits['_Layer'])

    def independent_from_group(self):
        self.original_parent = self.parentItem()
        tmp_parent_item = _VisualizationItem()
        tmp_parent_item._ItemTraits = self.original_parent._ItemTraits
        tmp_parent_item.block.append(self)
        self.original_parent.removeFromGroup(self)
        tmp_parent_item.addToGroup(self)

        return tmp_parent_item

    def independent_path_from_group(self, tmp_parent_item=None):
        self.original_parent = self.parentItem()
        if tmp_parent_item:
            pass
        else:
            tmp_parent_item = _VisualizationItem()
            tmp_parent_item._ItemTraits = self.original_parent._ItemTraits
        tmp_parent_item.block.append(self)
        self.original_parent.removeFromGroup(self)
        tmp_parent_item.addToGroup(self)

        return tmp_parent_item

    def set_highlight(self):
        self.highlight_flag = not self.highlight_flag
        if self.highlight_flag:
            self.highlighted_item_list.append(self)
        else:
            self.highlighted_item_list.remove(self)

    def set_shallow_highlight(self):
        self.shallow_highlight = not self.shallow_highlight
        if self.shallow_highlight:
            self.shallow_highlight_list.append(self)
        else:
            self.shallow_highlight_list.remove(self)

class PolygonBlock(QGraphicsPolygonItem):
    highlighted_item_list = list()
    shallow_highlight_list = list()

    def __init__(self, _BlockTraits=None):
        super().__init__()
        self.setFlag(QGraphicsItem.ItemIsSelectable, False)
        self.shallow_highlight = False
        self.hover = False
        self.index = None
        self.highlight_flag = False
        self.flag_memory = False
        self.element_info = ElementBlock(_BlockTraits)

        if _BlockTraits is not None:
            polygon = self.element_info.update_traits(_BlockTraits)
            self.setPolygon(polygon)

    def updateTraits(self, _BlockTraits):
        polygon = self.element_info.update_traits(_BlockTraits)
        self.setPolygon(polygon)


    def paint(self, painter, option, widget=None):
        self.element_info.block_traits["_Color"].setAlphaF(1)

        if self.isSelected() or self.highlight_flag:
            # self._BlockTraits["_Color"].setAlphaF(1)
            # self.setZValue(self.zValue()*10000)
            # print("HighLighted",self.zValue())
            self.flag_memory = True
            self.element_info.pen.setStyle(Qt.SolidLine)
            # pen.setColor(self._BlockTraits["_Outline"])
            color = Qt.GlobalColor.white if user_setup._Night_mode else Qt.GlobalColor.black
            self.element_info.pen.setColor(color)
            self.element_info.pen.setWidth(5)
            # self.setZValue(1)
        elif self.shallow_highlight:
            self.flag_memory = True
            self.element_info.pen.setStyle(Qt.DotLine)
            self.element_info.pen.setColor(Qt.GlobalColor.darkGreen)
            self.element_info.pen.setWidth(7)
        elif self.hover:
            self.flag_memory = True
            self.element_info.pen.setStyle(Qt.DotLine)
            self.element_info.pen.setColor(Qt.GlobalColor.darkCyan)
            self.element_info.pen.setWidth(5)
        elif self.flag_memory:
            self.flag_memory = False
            self.element_info.pen.setColor(self.element_info.block_traits["_Outline"])
            self.element_info.pen.setDashPattern(self.element_info.block_traits['_LinePattern'])
            self.element_info.pen.setWidth(self.element_info.block_traits['_LineSize'] + 2)
            self.element_info.brush.setColor(self.element_info.block_traits["_Color"])
        painter.setPen(self.element_info.pen)

        if self.element_info.block_traits["_Pattern"] not in ['X', 'blank']:
            if self.element_info.block_traits['_LayerName'] + self.element_info.block_traits[
                '_DatatypeName'] not in DisplayReader._DisplayDict or \
                    self.element_info.block_traits["_Pattern"] not in DisplayReader._PatternDict:
                warnings.warn(
                    f'Current process does not have information about object {self.element_info.block_traits["_ElementName"]}.')
                self.hide()
                return
            else:
                self.show()
        color_name = DisplayReader._DisplayDict[
            self.element_info.block_traits['_LayerName'] + self.element_info.block_traits['_DatatypeName']]['Fill'].name
        color_patt_name = color_name + self.element_info.block_traits["_Pattern"]

        if self.element_info.block_traits["_Pattern"] == 'X':
            painter.drawLine(0, 0, self.element_info.block_traits["_Width"], self.element_info.block_traits["_Height"])
            painter.drawLine(0, self.element_info.block_traits["_Height"], self.element_info.block_traits["_Width"], 0)
        elif self.element_info.block_traits["_Pattern"] == 'blank':
            self.element_info.brush.setStyle(Qt.NoBrush)
        else:
            if color_patt_name not in DisplayReader._ColorPatternDict:
                color = DisplayReader._DisplayDict[
                    self.element_info.block_traits['_LayerName'] + self.element_info.block_traits['_DatatypeName']][
                    'Fill']
                qpix = DisplayReader._PatternDict[self.element_info.block_traits["_Pattern"]].create_qbit(color)
                DisplayReader._DisplayDict[color_patt_name] = qpix
            qpix = DisplayReader._DisplayDict[color_patt_name]
            self.element_info.brush.setTexture(qpix)

        if '_type' in self.element_info.block_traits and self.element_info.block_traits['_type'] == 2:
            if self.element_info.block_traits['_Vertical']:
                x1 = self.element_info.block_traits['_Width'] / 2
                x2 = x1
                y1 = 0
                y2 = self.element_info.block_traits['_Height']
            else:
                # horizontal
                x1 = 0
                x2 = self.element_info.block_traits['_Width']
                y1 = self.element_info.block_traits['_Height'] / 2
                y2 = y1
            painter.drawLine(x1, y1, x2, y2)

        self.element_info.brush.setTransform(QTransform(painter.worldTransform().inverted()[0]))

        painter.setBrush(self.element_info.brush)

        painter.drawPolygon(self.polygon())
        painter.setRenderHint(QPainter.Antialiasing)

    def layerName2paintTrait(self):

        try:
            DisplayInfo = DisplayReader._DisplayDict
            color = \
            DisplayInfo[self.element_info.block_traits['_LayerName'] + self.element_info.block_traits['_DatatypeName']][
                'Fill']
        except:
            self.warning = QMessageBox()
            self.warning.setText("There is no matching QT Color profile")
            print("Color Traits Error")
            self.warning.show()

    def restore_zvalue(self):
        self.setZValue(self.element_info.block_traits['_Layer'])

    def independent_from_group(self):
        self.original_parent = self.parentItem()
        tmp_parent_item = _VisualizationItem()
        tmp_parent_item._ItemTraits = self.original_parent._ItemTraits
        tmp_parent_item.block.append(self)
        self.original_parent.removeFromGroup(self)
        tmp_parent_item.addToGroup(self)

        return tmp_parent_item

    def independent_path_from_group(self, tmp_parent_item=None):
        self.original_parent = self.parentItem()
        if tmp_parent_item:
            pass
        else:
            tmp_parent_item = _VisualizationItem()
            tmp_parent_item._ItemTraits = self.original_parent._ItemTraits
        tmp_parent_item.block.append(self)
        self.original_parent.removeFromGroup(self)
        tmp_parent_item.addToGroup(self)

        return tmp_parent_item

    def set_highlight(self):
        self.highlight_flag = not self.highlight_flag
        if self.highlight_flag:
            self.highlighted_item_list.append(self)
        else:
            self.highlighted_item_list.remove(self)

    def set_shallow_highlight(self):
        self.shallow_highlight = not self.shallow_highlight
        if self.shallow_highlight:
            self.shallow_highlight_list.append(self)
        else:
            self.shallow_highlight_list.remove(self)


class _VisualizationItem(QGraphicsItemGroup):
    invalid_layer_signal = pyqtSignal(str)
    _compareLayer = dict()
    _Layer = LayerReader._LayerMapping
    _subElementLayer = dict()
    for layer in _Layer:
        _subElementLayer[layer] = list()
    _subElementLayer['SRef'] = list()

    def __init__(self,_ItemTraits=None):
        super().__init__()
        self.setBoundingRegionGranularity(1)
        self.sub_element_dict = dict()
        self._id = None
        self._type = None
        self.setFlag(QGraphicsItemGroup.ItemIsSelectable,True)
        self.setAcceptHoverEvents(True)
        # self._XYCoordinatesForDisplay = []
        self._clickFlag = True
        self._isInHierarchy = False
        self._NoShowFlag = False
        self._SimplifyFlag = False
        self._multipleBlockFlag = False
        self._subSrefVisualItem = None
        self._NoVariableFlag = False
        self._subCellFlag = False
        self._IndexFlag = False
        self._PathUngroupedFlag = False
        self._CreateFlag = True
        self.index = None
        if _ItemTraits is None:
            self._ItemTraits = dict(
                _ElementName = None,
                _Layer = None,

                _DesignParametertype = None,
                _XYCoordinates = None,
                _Width = None,
                _Height = None,
                _Reflect = None,
                _Angle = None,
                _Color = None,
                _DesignParameterRef=None,   #Reference of Design Parameter
                _VisualizationItems = [],    #This is for SRef!!
                variable_info = dict(
                                    XY = None,
                                    width = None,
                                    height = None,
                                    parameters = None
                                )
            )
            self.block = []
            self.bounding_rect_dict = dict(top=0,bottom=0,left=0,right=0)
            # self._BlockGroup = None,
        else:
            self.block = []
            self._ItemTraits = _ItemTraits
            if self._ItemTraits['_DesignParametertype'] == 1:
                for idx, xyPairs in enumerate(self._ItemTraits['_XYCoordinates']):
                    self.blockGeneration(xyPairs, idx)
            elif self._ItemTraits['_DesignParametertype'] == 2:
                for idx, xyPairs in enumerate(self._ItemTraits['_XYCoordinates']):
                    self.blockGeneration(xyPairs, idx)
            elif self._ItemTraits['_DesignParametertype'] == 3:
                for idx, xyPairs in enumerate(self._ItemTraits['_XYCoordinates']):
                    self.blockGeneration(xyPairs, idx)
            elif self._ItemTraits['_DesignParametertype'] == 8:
                self.blockGeneration(self._ItemTraits['_XYCoordinates'])
            else:
                self.blockGeneration()

    # def paint(self, painter, option, widget) -> None:
    #     super(_VisualizationItem, self).paint(painter, option, widget)
    #     if self._subSrefVisualItem != None:
    #         self._subSrefVisualItem.paint(painter, option, widget)
    #     pass
    def restore_zvalue(self):

        self.setZValue(0)
        # for block in self.block:
        #     block.restore_zvalue()

    def shape(self):
        # if self._type == 1:
        #     # return super().shape()
        #     main_path = QPainterPath()
        #     for i, block in enumerate(self.block):
        #         if type(block) != _RectBlock:
        #             continue
        #         else:
        #             tmp_rect = block.rect()
        #             tmp_rect.translate(block.pos())
        #             main_path.addRect(tmp_rect)
        #     return main_path
        # if self.parentItem():
        #     return QPainterPath()


        if self._type == 1 or self._type == 2:
            main_path = QPainterPath()
            for i, block in enumerate(self.block):
                try:
                    if type(block) != _RectBlock:
                        # print(f'block! {type(block)}')
                        continue
                    tmp_rect = block.rect()
                    tmp_rect.translate(block.pos())
                    points = [tmp_rect.topLeft(),tmp_rect.bottomLeft(),tmp_rect.bottomRight(),tmp_rect.topRight()]
                    # if DEBUG:
                    #     print(f'points: {points}')
                    poly = QPolygonF(points)
                    main_path.addPolygon(poly)
                    main_path.closeSubpath()
                except:
                    pass
            return main_path
        # elif self._type == 3:
        #     main_path = QPainterPath()
        #     for block in self.childItems():
        #         if type(block) != _RectBlock and type(block) != _VisualizationItem:
        #             continue
        #         else:
        #             tmp_path = block.shape()
        #             tmp_path.translate(block.pos())
        #             main_path.addPath(tmp_path)
        #             main_path.closeSubpath()
        #     # path_item = QGraphicsPathItem(main_path)
        #     # path_item.setPen(QPen(Qt.GlobalColor.red,3,Qt.SolidLine))
        #     # self.addToGroup(path_item)
        #     return main_path
        else:
            return super().shape()

    def updateDesignParameter(self,QtDesignParameter):
        remove_item_list= []
        for child in self.childItems():
            if type(child) == _VisualizationItem:
                sub_element_dp_name = child._ElementName
                if sub_element_dp_name in QtDesignParameter._DesignParameter['_ModelStructure']:
                    remove_item_list.extend(child.updateDesignParameter(QtDesignParameter._DesignParameter['_ModelStructure'][sub_element_dp_name]))
                # else:
                #     search_stack = [child]
                #     while search_stack:
                #         search_item = search_stack.pop(0)
                #         sub_children = child.childItems()
                #         search_stack.extend(sub_children)
                #         remove_item_list.extend(sub_children)
                #         for sub_child in sub_children:
                #             search_item.removeFromGroup(sub_child)
            self.removeFromGroup(child)
            remove_item_list.append(child)


        self._id = QtDesignParameter._id
        self._type = QtDesignParameter._type
        self._ItemTraits['_type'] = self._type
        # self._CreateFlag = False
        # try:
        #     oldVersionSupportForXYCoordinatesForDisplay = QtDesignParameter._XYCoordinatesForDisplay
        # except:
        #     QtDesignParameter._XYCoordinatesForDisplay = []
        # if QtDesignParameter._XYCoordinatesForDisplay == [] or QtDesignParameter._XYCoordinatesForDisplay == None:
        #     if QtDesignParameter._DesignParameter['_XYCoordinates']:
        #         QtDesignParameter._XYCoordinatesForDisplay = QtDesignParameter._DesignParameter['_XYCoordinates']
        #     else:
        #         QtDesignParameter._XYCoordinatesForDisplay = [[0,0]]


        if not QtDesignParameter._DesignParameter['_XYCoordinates'] or type(QtDesignParameter._DesignParameter['_XYCoordinates'][0]) == list:
            if self._type == 1:
                self._ItemTraits['_XYCoordinates'] = copy.deepcopy(QtDesignParameter._DesignParameter['_XYCoordinates'])
            elif self._type == 2:
                self._ItemTraits['_XYCoordinates'] = copy.deepcopy(QtDesignParameter._DesignParameter['_XYCoordinates'])
            elif self._type == 3:
                self._ItemTraits['_XYCoordinates'] = copy.deepcopy(QtDesignParameter._DesignParameter['_XYCoordinates'])
            elif self._type == 8:
                self._ItemTraits['_XYCoordinates'] = copy.deepcopy(QtDesignParameter._DesignParameter['_XYCoordinates'])

        if QtDesignParameter._ElementName == None:
            QtDesignParameter._ElementName = QtDesignParameter._id
            self._ItemTraits['_ElementName'] = QtDesignParameter._id
        else:
            self._ItemTraits['_ElementName'] = QtDesignParameter._ElementName
        remove_item_list.extend(self.updateTraits(QtDesignParameter._DesignParameter) if self.updateTraits(QtDesignParameter._DesignParameter) else [])
        return remove_item_list


    def updateTraits(self,_DesignParameter):
        if _DesignParameter['_XYCoordinates'] == None:
            return
        
        if self._ItemTraits['_XYCoordinates'] == None or len(self._ItemTraits['_XYCoordinates']) == 0 :
            self._ItemTraits['_XYCoordinates'] = None
        else:
            pass

        for key in _DesignParameter.keys():                      #set itemTrait on Object)
            '''
            invalid key skipping for visual item
            '''
            if key == "_XYCoordinates":    # DesignParameter's XYcoordinate is for real xy coordinates,,,
                self._ItemTraits['_XYCoordinates'] = copy.deepcopy(_DesignParameter[key])                 # Itemtrait's XY coordinate matches QtDesignParameter's XYCoordinatesForDisplay
            elif key == "_ElementName":
                self._ElementName = _DesignParameter[key]
            else:
                self._ItemTraits[key] = _DesignParameter[key]

        if self._ItemTraits['_DesignParametertype'] == 1:           # Boundary
            try:
                self._ItemTraits['_Width'] = int(self._ItemTraits['_XWidth'])
                self._ItemTraits['_Height'] = int(self._ItemTraits['_YWidth'])
            except:
                self.warning = QMessageBox()
                self.warning.setText("Invalid Design Value")
                self.warning.setIcon(QMessageBox.Warning)
                return
        elif self._ItemTraits['_DesignParametertype'] == 2:         # Path
            try:
                self._ItemTraits['_Width'] = int(self._ItemTraits['_Width'])
            except:
                self.warning = QMessageBox()
                self.warning.setText("Invalid Design Value")
                self.warning.setIcon(QMessageBox.Warning)
                return
        elif self._ItemTraits['_DesignParametertype'] == 3:
            try:
                self._ItemTraits['_DesignParameterRef'] = _DesignParameter['_ModelStructure']
                self._ItemTraits['_Reflect'] = _DesignParameter['_Reflect']
                self._ItemTraits['_Angle'] = _DesignParameter['_Angle']
            except:
                pass
            # for key in _DesignParameter['_ModelStructure']:
            #     self._ItemTraits['_VisualizationItems'].append(_DesignParameter['_ModelStructure'][key])
        elif self._ItemTraits['_DesignParametertype'] == 8:
            self._ItemTraits['_Width'] = _DesignParameter['_Mag']
            self._ItemTraits['_Reflect'] = _DesignParameter['_Reflect']
            self._ItemTraits['_Angle'] = _DesignParameter['_Angle']
            pass
        if self._multipleBlockFlag == None:
            _multipleBlockFlag = False


        try:
            remove_item_list = []
            for i in range(len(self.block)):
                # remove_item_list.append(self.block[i])
                self.removeFromGroup(self.block[i])
            for child in self.childItems():
                # self.removeFromGroup(child)
                remove_item_list.append(child)
            if self._ItemTraits['_DesignParametertype'] == 1:
                self.block = []
                for idx, xyPairs in enumerate(self._ItemTraits['_XYCoordinates']):
                    self.blockGeneration(xyPairs, idx)
                self.setPos(0,0)
            elif self._ItemTraits['_DesignParametertype'] == 2:
                self.block = []
                for idx, xyPairs in enumerate(self._ItemTraits['_XYCoordinates']):
                    self.blockGeneration(xyPairs, idx)
                self.setPos(0,0)
            elif self._ItemTraits['_DesignParametertype'] == 3:
                self.block = []
                for idx, xyPairs in enumerate(self._ItemTraits['_XYCoordinates']):
                    self.blockGeneration(xyPairs, idx)
                self.setPos(0,0)
            elif self._ItemTraits['_DesignParametertype'] == 8:
                self.block = []
                self.blockGeneration(self._ItemTraits['_XYCoordinates'])
                self.setPos(0,0)
            else:
                self.block = []
                self.blockGeneration()
                self.setPos(0,0)
        except:
            traceback.print_exc()
        return remove_item_list

    def remove_block_from_group(self, remove_item):
        for i in range(len(remove_item.block)):
            self.removeFromGroup(remove_item.block[i])

    def updateDesignObj(self,visualItem):
        self._ItemTraits['_VisualizationItems'].append(visualItem)
        # visualItem.setFlag(QGraphicsItemGroup.ItemIsSelectable,False)
        # visualItem._clickFlag = False
        visualItem._isInHierarchy = True

        for item in self._ItemTraits['_VisualizationItems']:
            self.addToGroup(item)


    def blockGeneration(self,_XYCoordinatesPair=None, idx=None):                                  #This creates visual Block (which maps boundary or Path Item)
        # blockTraits = copy.deepcopy(self._ItemTraits)
        blockTraits = lab_feature.deepish_copy(self._ItemTraits)


        DisplayInfo = DisplayReader._DisplayDict

        if blockTraits['_Layer'] is not None: #Load GDS case
            try:
                if '_DatatypeName' not in blockTraits or not blockTraits['_DatatypeName']:
                    if 'crit' in blockTraits['_LayerUnifiedName']:
                        blockTraits['_DatatypeName'] = '_crit'
                    elif 'pin' in blockTraits['_LayerUnifiedName']:
                        blockTraits['_DatatypeName'] = '_pin'
                    else:
                        blockTraits['_DatatypeName'] = '_drawing'
            except:
                print('debug')

            layer_data_name = blockTraits['_LayerName']+blockTraits['_DatatypeName']
            if layer_data_name not in DisplayReader._DisplayDict:
                DisplayReader.readtechfile()
            if blockTraits['_LayerName']+blockTraits['_DatatypeName'] not in DisplayInfo:
                warnings.warn(
                    f'Current process does not have information about object {blockTraits["_ElementName"]}.')
                self.hide()
                return

            blockTraits['_Color'] =  DisplayInfo[blockTraits['_LayerName']+blockTraits['_DatatypeName']]['Fill']
            blockTraits['_Outline'] =  DisplayInfo[blockTraits['_LayerName']+blockTraits['_DatatypeName']]['Outline']
            blockTraits['_Pattern'] =  DisplayInfo[blockTraits['_LayerName']+blockTraits['_DatatypeName']]['Stipple']
            blockTraits['_LinePattern'] =  DisplayInfo[blockTraits['_LayerName']+blockTraits['_DatatypeName']]['LineStyle']['pattern']
            blockTraits['_LineSize'] =  DisplayInfo[blockTraits['_LayerName']+blockTraits['_DatatypeName']]['LineStyle']['size']

        if self._ItemTraits['_DesignParametertype'] == 1:                              # Boundary Case
            if blockTraits['_LayerUnifiedName'] is None:
                return
            tmpBlock = _RectBlock()
            tmpBlock.updateTraits(blockTraits)
            tmpBlock.setPos(_XYCoordinatesPair[0] - blockTraits['_Width']/2,_XYCoordinatesPair[1] - blockTraits['_Height']/2)
            tmpBlock.index = [idx]

            # layernum2name = LayerReader._LayerNumber2CommonLayerName(LayerReader._LayerMapping)
            # layer = layernum2name[str(blockTraits['_Layer'])]
            layer = blockTraits['_LayerUnifiedName']

            if self in self._compareLayer:
                if self._compareLayer[self] == layer:
                    tmpLayer = None
                else:
                    tmpLayer = self._compareLayer[self]
                    self._compareLayer[self] = layer
            else:
                tmpLayer = None
                self._compareLayer[self] = layer
                if layer not in self._subElementLayer:
                    self._subElementLayer[layer] = [self]
                else:
                    self._subElementLayer[layer].append(self)

            if tmpLayer == None:
                pass
            else:
                if tmpLayer in self._subElementLayer:
                    self._subElementLayer[tmpLayer].remove(self)
                self._subElementLayer[layer].append(self)

            self.block.append(tmpBlock)
            self.addToGroup(tmpBlock)

            self.bounding_rect_dict = dict(top=self.boundingRect().bottom(),
                                           bottom=self.boundingRect().top(),
                                           left=self.boundingRect().left(),
                                           right=self.boundingRect().right())

            ############################ Variable Visualization Start ############################

            # for field in self._ItemTraits['variable_info']:
            #     if field == 'XY':
            #         self._ItemTraits['variable_info'][field] = str(self._ItemTraits['_XYCoordinates'])
            #     elif field == 'width':
            #         self._ItemTraits['variable_info'][field] = str(self._ItemTraits['_Width'])
            #     elif field == 'height':
            #         self._ItemTraits['variable_info'][field] = str(self._ItemTraits['_Height'])
            #
            # self.widthVariable = QGraphicsTextItemWObounding(self._ItemTraits['variable_info']['width'])
            # self.heightVariable = QGraphicsTextItemWObounding(self._ItemTraits['variable_info']['height'])
            # self.XYVariable = QGraphicsTextItemWObounding(f"*{self._ItemTraits['variable_info']['XY']}")
            #
            # self.setVariable(type='Boundary')

            ############################ Variable Visualization End ############################
        elif self._ItemTraits['_DesignParametertype'] == 11:                              # Boundary Case
            if blockTraits['_LayerUnifiedName'] is None:
                return
            tmpBlock = PolygonBlock()
            tmpBlock.updateTraits(blockTraits)
            tmpBlock.setPos(0,0)
            # tmpBlock.setPos(_XYCoordinatesPair[0] - blockTraits['_Width']/2,_XYCoordinatesPair[1] - blockTraits['_Height']/2)
            tmpBlock.index = [idx]

            # layernum2name = LayerReader._LayerNumber2CommonLayerName(LayerReader._LayerMapping)
            # layer = layernum2name[str(blockTraits['_Layer'])]
            layer = blockTraits['_LayerUnifiedName']

            if self in self._compareLayer:
                if self._compareLayer[self] == layer:
                    tmpLayer = None
                else:
                    tmpLayer = self._compareLayer[self]
                    self._compareLayer[self] = layer
            else:
                tmpLayer = None
                self._compareLayer[self] = layer
                if layer not in self._subElementLayer:
                    self._subElementLayer[layer] = [self]
                else:
                    self._subElementLayer[layer].append(self)

            if tmpLayer == None:
                pass
            else:
                if tmpLayer in self._subElementLayer:
                    self._subElementLayer[tmpLayer].remove(self)
                self._subElementLayer[layer].append(self)

            self.block.append(tmpBlock)
            self.addToGroup(tmpBlock)

            self.bounding_rect_dict = dict(top=self.boundingRect().bottom(),
                                           bottom=self.boundingRect().top(),
                                           left=self.boundingRect().left(),
                                           right=self.boundingRect().right())

            ############################ Variable Visualization Start ############################

            # for field in self._ItemTraits['variable_info']:
            #     if field == 'XY':
            #         self._ItemTraits['variable_info'][field] = str(self._ItemTraits['_XYCoordinates'])
            #     elif field == 'width':
            #         self._ItemTraits['variable_info'][field] = str(self._ItemTraits['_Width'])
            #     elif field == 'height':
            #         self._ItemTraits['variable_info'][field] = str(self._ItemTraits['_Height'])
            #
            # self.widthVariable = QGraphicsTextItemWObounding(self._ItemTraits['variable_info']['width'])
            # self.heightVariable = QGraphicsTextItemWObounding(self._ItemTraits['variable_info']['height'])
            # self.XYVariable = QGraphicsTextItemWObounding(f"*{self._ItemTraits['variable_info']['XY']}")
            #
            # self.setVariable(type='Boundary')

            ############################ Variable Visualization End ############################



        elif self._ItemTraits['_DesignParametertype'] == 2:                            # Path Case
            if blockTraits['_LayerUnifiedName'] is None:
                return
            for i in range(0,len(_XYCoordinatesPair)-1):
                if float(_XYCoordinatesPair[i][0]) == float(_XYCoordinatesPair[i+1][0]):          #Vertical Case
                    Xmin = _XYCoordinatesPair[i][0] - self._ItemTraits['_Width']/2
                    Xwidth = self._ItemTraits['_Width']
                    Ymin = min(_XYCoordinatesPair[i][1],_XYCoordinatesPair[i+1][1])
                    Ymax = max(_XYCoordinatesPair[i][1],_XYCoordinatesPair[i+1][1])
                    Ywidth = Ymax - Ymin

                    if len(_XYCoordinatesPair) == 2:                                                    #Only One Block Case
                        pass
                    elif i == 0:                                                                                        #There are more than 2 segments and First Block Case
                        if _XYCoordinatesPair[i][1] < _XYCoordinatesPair[i+1][1]:          #UpWard Case
                            Ywidth -= self._ItemTraits['_Width']/2
                        elif _XYCoordinatesPair[i][1] > _XYCoordinatesPair[i+1][1]:        #DownWard Case
                            Ymin += self._ItemTraits['_Width']/2
                            Ywidth -= self._ItemTraits['_Width']/2
                    elif i == len(_XYCoordinatesPair)-2:                                                #Last Block Case
                        if _XYCoordinatesPair[i][1] < _XYCoordinatesPair[i+1][1]:          #UpWard Case
                            Ymin -= self._ItemTraits['_Width']/2
                            Ywidth += self._ItemTraits['_Width']/2
                        elif _XYCoordinatesPair[i][1] > _XYCoordinatesPair[i+1][1]:        #DownWard Case
                            Ywidth += self._ItemTraits['_Width']/2
                    else:                                                                                               #Interim Block Case
                        if _XYCoordinatesPair[i][1] < _XYCoordinatesPair[i+1][1]:          #UpWard Case
                            Ymin -= self._ItemTraits['_Width']/2
                        elif _XYCoordinatesPair[i][1] > _XYCoordinatesPair[i+1][1]:        #DownWard Case
                            Ymin += self._ItemTraits['_Width']/2
                    vertical = True
                else:                                                                                                #Horizontal Case
                    Ymin = _XYCoordinatesPair[i][1] - self._ItemTraits['_Width']/2
                    Ywidth = self._ItemTraits['_Width']
                    Xmin = min(_XYCoordinatesPair[i][0],_XYCoordinatesPair[i+1][0])
                    Xmax = max(_XYCoordinatesPair[i][0],_XYCoordinatesPair[i+1][0])
                    Xwidth = Xmax - Xmin

                    if len(_XYCoordinatesPair) == 2:                                                    #Only One Block Case
                        pass
                    elif i == 0:                                                                                        #There are more than 2 segments and First Block Case
                        if _XYCoordinatesPair[i][0] < _XYCoordinatesPair[i+1][0]:          #Path to Right Case
                            Xwidth -= self._ItemTraits['_Width']/2
                        elif _XYCoordinatesPair[i][0] > _XYCoordinatesPair[i+1][0]:        #Path to Left Case
                            Xwidth -= self._ItemTraits['_Width']/2
                            Xmin += self._ItemTraits['_Width']/2
                    elif i == len(_XYCoordinatesPair)-2:
                        if _XYCoordinatesPair[i][0] < _XYCoordinatesPair[i+1][0]:          #Path to Right Case
                            Xmin -= self._ItemTraits['_Width']/2
                            Xwidth += self._ItemTraits['_Width']/2
                        elif _XYCoordinatesPair[i][0] > _XYCoordinatesPair[i+1][0]:        #Path to Left Case
                            Xwidth += self._ItemTraits['_Width']/2
                    else:
                        if _XYCoordinatesPair[i][0] < _XYCoordinatesPair[i+1][0]:          #Path to Right Case
                            Xmin -= self._ItemTraits['_Width']/2
                        elif _XYCoordinatesPair[i][0] > _XYCoordinatesPair[i+1][0]:        #Path to Left Case
                            Xmin += self._ItemTraits['_Width']/2
                    vertical = False
                blockTraits['_Width'] = Xwidth
                blockTraits['_Height'] = Ywidth
                blockTraits['_Vertical'] = vertical

                # layernum2name = LayerReader._LayerNumber2CommonLayerName(LayerReader._LayerMapping)
                # layer = layernum2name[str(blockTraits['_Layer'])]
                layer = blockTraits['_LayerUnifiedName']

                if self in self._compareLayer:
                    if self._compareLayer[self] == layer:
                        tmpLayer = None
                    else:
                        tmpLayer = self._compareLayer[self]
                        self._compareLayer[self] = layer
                else:
                    tmpLayer = None
                    self._compareLayer[self] = layer
                    self._subElementLayer[layer].append(self)

                if tmpLayer == None:
                    pass
                else:
                    self._subElementLayer[tmpLayer].remove(self)
                    self._subElementLayer[layer].append(self)

                self.index = idx
                # block = _RectBlock(copy.deepcopy(blockTraits))
                block = _RectBlock(lab_feature.deepish_copy(blockTraits))

                block.index = [idx, i]

                self.block.append(block)  #Block Generation
                self.block[-1].setPos(Xmin*scaleValue,Ymin*scaleValue)
                self.addToGroup(self.block[-1])

            self.bounding_rect_dict = dict(top=self.boundingRect().bottom(),
                                           bottom=self.boundingRect().top(),
                                           left=self.boundingRect().left(),
                                           right=self.boundingRect().right())

            ############################ Variable Visualization Start ############################
            # self.XYVariable = list()
            # self._ItemTraits['variable_info']['XY'] = list()
            #
            # for field in self._ItemTraits['variable_info']:
            #     if field == 'XY':
            #         self._ItemTraits['variable_info'][field] = self._ItemTraits['_XYCoordinates']
            #     elif field == 'width':
            #         self._ItemTraits['variable_info'][field] = str(self._ItemTraits['_Width'])
            #
            # for self.idx in range(len(self._ItemTraits['_XYCoordinates'][0])):
            #     if self.idx == 0:
            #         self.tmpXY = QGraphicsTextItemWObounding('*' + str(self._ItemTraits['variable_info']['XY'][0][self.idx]) + '\nwidth: ' + str(self._ItemTraits['variable_info']['width']))
            #     else:
            #         self.tmpXY = QGraphicsTextItemWObounding('*' + str(self._ItemTraits['variable_info']['XY'][-1][self.idx]))
            #
            #     self.setVariable(type='Path')

            ############################ Variable Visualization End ############################

        elif self._ItemTraits['_DesignParametertype'] == 3:                #SRef Case
            self.index = idx
            tmp_vs_item_group = QGraphicsItemGroup()
            for sub_element_dp_name, sub_element_dp in self._ItemTraits['_DesignParameterRef'].items():
                sub_element_vi = _VisualizationItem()
                sub_element_vi._NoVariableFlag = True
                sub_element_vi._subCellFlag = True
                sub_element_vi.updateDesignParameter(sub_element_dp)
                sub_element_vi.setFlag(QGraphicsItemGroup.ItemIsSelectable, False)
                sub_element_vi.setPos(_XYCoordinatesPair[0], _XYCoordinatesPair[1])

                # layernum2name = LayerReader._LayerNumber2CommonLayerName(LayerReader._LayerMapping)
                if sub_element_vi._ItemTraits['_Layer'] == None:
                    pass
                else:
                    if type(sub_element_vi._ItemTraits['_Layer']) == int:
                        # layer = layernum2name[str(sub_element_vi._ItemTraits['_Layer'])]
                        try:
                            layer = sub_element_vi._ItemTraits['_LayerUnifiedName']
                        except:
                            traceback.print_exc()
                            print(sub_element_vi._ItemTraits)
                        if layer not in self._subElementLayer:
                            self._subElementLayer[layer] = [sub_element_vi]
                        else:
                            self._subElementLayer[layer].append(sub_element_vi)
                    else:
                        self._subElementLayer[sub_element_vi._ItemTraits['_Layer']].append(sub_element_vi)

                if sub_element_vi._ItemTraits['_DesignParametertype'] != 8:
                    if self._ItemTraits['_Reflect'] == None and self._ItemTraits['_Angle'] == None:
                        pass
                    elif self._ItemTraits['_Reflect'] == [0, 0, 0]:
                        rot = self._ItemTraits['_Angle']
                        sub_element_vi.setRotation(rot)
                    elif self._ItemTraits['_Reflect'] == [1, 0, 0]:
                        sub_element_vi.setTransform(QTransform(1,0,0,-1,0,0))
                        if self._ItemTraits['_Angle'] == None:
                            pass
                        else:
                            rot = 360 - self._ItemTraits['_Angle']
                            sub_element_vi.setRotation(rot)

                tmp_vs_item_group.addToGroup(sub_element_vi)
                self.addToGroup(sub_element_vi)
                self.sub_element_dict[sub_element_dp_name+f'[{idx}]'] = sub_element_vi

            self.bounding_rect_dict = dict(top=tmp_vs_item_group.boundingRect().bottom(),
                                           bottom=tmp_vs_item_group.boundingRect().top(),
                                           left=tmp_vs_item_group.boundingRect().left(),
                                           right=tmp_vs_item_group.boundingRect().right())

            ############################ Variable Visualization Start ############################

            # for field in self._ItemTraits['variable_info']:
            #     if field == 'XY':
            #         self._ItemTraits['variable_info'][field] = str(self._ItemTraits['_XYCoordinates'])
            #     elif field == 'parameters':
            #         self._ItemTraits['variable_info'][field] = str(self._ItemTraits['parameters'])
            #
            # tmpParam = str(self._ItemTraits['variable_info']['parameters']).replace(',', ',\n')
            #
            # self.XYVariable = QGraphicsTextItemWObounding('*' + self._ItemTraits['variable_info']['XY'])
            # self.paramVariable = QGraphicsTextItemWObounding(tmpParam)
            #
            # self.setVariable(type='Sref')

            ############################ Variable Visualization End ############################

            self._subElementLayer['SRef'].append(self)

        elif self._ItemTraits['_DesignParametertype'] == 8:                #Text Case
            if blockTraits['_Layer'] == 127:
                try:
                    self.text = QGraphicsTextItem(blockTraits['_TEXT'].decode())
                except:
                    self.text = QGraphicsTextItem(blockTraits['_TEXT'])

                if blockTraits['_Width'] < 1:
                    fontSize = 1000 * blockTraits['_Width']
                else:
                    fontSize = blockTraits['_Width']
                font = QFont('tmp', fontSize)
                self.text.setFont(font)
                self.text.setPos(blockTraits['_XYCoordinates'][0][0],blockTraits['_XYCoordinates'][0][1])
                self.text.setTransform(QTransform(1,0,0,-1,0,0))

                self.block.append(self.text)
                self.addToGroup(self.text)

                self._subElementLayer['text'].append(self)

            else:
                # layernum2name = LayerReader._LayerNumber2CommonLayerName(LayerReader._LayerMapping)
                # layer = layernum2name[str(blockTraits['_Layer'])]
                layer = blockTraits['_LayerUnifiedName']
                if 'PIN' in layer:
                    try:
                        self.text = QGraphicsTextItem(blockTraits['_TEXT'].decode())
                    except:
                        self.text = QGraphicsTextItem(blockTraits['_TEXT'])

                    if not blockTraits['_Color']:
                        blockTraits['_Color'] = Qt.GlobalColor.white
                    self.text.setDefaultTextColor(blockTraits['_Color'])
                    if blockTraits['_Width'] < 1:
                        fontSize = 1000 * blockTraits['_Width']
                    else:
                        fontSize = blockTraits['_Width']
                    font = QFont('tmp', fontSize)
                    self.text.setFont(font)
                    self.text.setPos(blockTraits['_XYCoordinates'][0][0], blockTraits['_XYCoordinates'][0][1])
                    self.text.setTransform(QTransform(1, 0, 0, -1, 0, 0))

                    _point = QGraphicsTextItem('X')
                    _point.setDefaultTextColor(blockTraits['_Color'])
                    _point_font = QFont('tmp2', 20)
                    _point.setFont(_point_font)
                    _point.setPos(blockTraits['_XYCoordinates'][0][0] - 12, blockTraits['_XYCoordinates'][0][1] - 17)

                    if self in self._compareLayer:
                        if self._compareLayer[self] == layer:
                            tmpLayer = None
                        else:
                            tmpLayer = self._compareLayer[self]
                            self._compareLayer[self] = layer
                    else:
                        tmpLayer = None
                        self._compareLayer[self] = layer
                        self._subElementLayer[layer].append(self)

                    if tmpLayer == None:
                        pass
                    else:
                        self._subElementLayer[tmpLayer].remove(self)
                        self._subElementLayer[layer].append(self)

                    self.block.append(self.text)
                    self.block.append(_point)
                    self.addToGroup(self.text)
                    self.addToGroup(_point)

            self.bounding_rect_dict = dict(top=self.boundingRect().bottom(),
                                           bottom=self.boundingRect().top(),
                                           left=self.boundingRect().left(),
                                           right=self.boundingRect().right())

        else:
            print("WARNING1: Unvalid DataType Detected!")

        for block in self.block:
            if type(block) == _RectBlock:
                block.setZValue(block.element_info.block_traits['_Layer'])
        if self._type == 1 or self._type == 2:
            self.setZValue(self._ItemTraits['_Layer'])
        elif self._type == 3:
            z_list = []
            for child in self.childItems():
                z_list.append(child.zValue())
            self.setZValue(max(z_list))
        # print('--')
        # print(self._subElementLayer)
        # self.send_subelementlayer_signal.emit(self._subElementLayer)

    def update_dc_variable_info(self, _ast):
        if _ast._type == 'Boundary':
            for field in ['XY', 'layer' , 'width', 'height']:
                if field not in _ast.__dict__:
                    return None
            if type(_ast.XY) != list :
                return None
            if type(_ast.width) != int :
                return None
            if type(_ast.height) != int :
                return None

            for field in self._ItemTraits['variable_info']:
                if field == 'XY':
                    self._ItemTraits['variable_info'][field] = str(_ast.XY)
                elif field == 'width':
                    self._ItemTraits['variable_info'][field] = str(_ast.width)
                elif field == 'height':
                    self._ItemTraits['variable_info'][field] = str(_ast.height)

            self.widthVariable.setVisible(False)
            self.heightVariable.setVisible(False)
            self.XYVariable.setVisible(False)

            self.block.remove(self.widthVariable)
            self.block.remove(self.heightVariable)
            self.block.remove(self.XYVariable)

            self.widthVariable = QGraphicsTextItemWObounding(str(_ast.width))
            self.heightVariable = QGraphicsTextItemWObounding(str(_ast.height))
            self.XYVariable = QGraphicsTextItemWObounding('*' + str(_ast.XY))

            self.setVariable(_ast._type)

        elif _ast._type == 'Path':
            for field in self._ItemTraits['variable_info']:
                if field == 'XY':
                    self._ItemTraits['variable_info'][field] = _ast.XY
                elif field == 'width':
                    self._ItemTraits['variable_info'][field] = str(_ast.width)
            replaceXYVariable = self.XYVariable
            self.XYVariable = list()
            for self.idx in range(len(self._ItemTraits['_XYCoordinates'][0])):
                self.replaceXY = replaceXYVariable[self.idx]
                self.replaceXY.setVisible(False)

                self.block.remove(self.replaceXY)

                if self.idx == 0:
                    if _ast.XY is not None:
                        self.tmpXY = QGraphicsTextItemWObounding('*' + str(_ast.XY[0][self.idx]) + '\nwidth: ' + str(_ast.width))
                    else:
                        self.tmpXY = QGraphicsTextItemWObounding('*' + str(_ast.XY) + '\nwidth: ' + str(_ast.width))
                else:
                    if _ast.XY is not None:
                        self.tmpXY = QGraphicsTextItemWObounding('*' + str(_ast.XY[0][self.idx]))
                    else:
                        self.tmpXY = QGraphicsTextItemWObounding('*' + str(_ast.XY) + '\nwidth: ' + str(_ast.width))

                self.setVariable(_ast._type)

        elif _ast._type == 'Sref':
            for field in self._ItemTraits['variable_info']:
                if field == 'XY':
                    self._ItemTraits['variable_info'][field] = _ast.XY
                elif field == 'parameters':
                    self._ItemTraits['variable_info'][field] = _ast.parameters
            # self.XYVariable.setVisible(False)
            # self.paramVariable.setVisible(False)

            # self.block.remove(self.XYVariable)
            # self.block.remove(self.paramVariable)

            tmpParam = str(_ast.parameters).replace(',', ',\n')

            self.XYVariable = QGraphicsTextItemWObounding('*' + str(_ast.XY))
            self.paramVariable = QGraphicsTextItemWObounding(tmpParam)

            self.setVariable(_ast._type)

    def returnLayerDict(self):
        return self._subElementLayer

    def setVariable(self, type=None):
        if self._NoVariableFlag == False:
            fontSize = 10
            font = QFont('tmp', fontSize)
            font.setBold(True)

            if type == None:
                pass
            elif type == 'Boundary':
                self.widthVariable.setFont(font)
                self.heightVariable.setFont(font)
                self.XYVariable.setFont(font)

                self.widthVariable.setPos(self._ItemTraits['_XYCoordinates'][0][0]-6,
                                          self._ItemTraits['_XYCoordinates'][0][1] - self._ItemTraits['_Height'] / 2 + 20)
                self.heightVariable.setPos(self._ItemTraits['_XYCoordinates'][0][0] + self._ItemTraits['_Width'] / 2 - 20,
                                           self._ItemTraits['_XYCoordinates'][0][1]+10)
                self.XYVariable.setPos(self._ItemTraits['_XYCoordinates'][0][0]-6, self._ItemTraits['_XYCoordinates'][0][1]+10)

                self.widthVariable.setDefaultTextColor(Qt.GlobalColor.red)
                self.heightVariable.setDefaultTextColor(Qt.GlobalColor.red)
                self.XYVariable.setDefaultTextColor(Qt.GlobalColor.red)

                self.widthVariable.setTransform(QTransform(1, 0, 0, -1, 0, 0))
                self.heightVariable.setTransform(QTransform(1, 0, 0, -1, 0, 0))
                self.XYVariable.setTransform(QTransform(1, 0, 0, -1, 0, 0))

                self.widthVariable.setVisible(False)
                self.heightVariable.setVisible(False)
                self.XYVariable.setVisible(False)

                self.widthVariable.setZValue(1)
                self.heightVariable.setZValue(1)
                self.XYVariable.setZValue(1)

                self.block.append(self.widthVariable)
                self.block.append(self.heightVariable)
                self.block.append(self.XYVariable)
                self.addToGroup(self.widthVariable)
                self.addToGroup(self.heightVariable)
                self.addToGroup(self.XYVariable)

            elif type == 'Path':
                self.tmpXY.setFont(font)

                self.tmpXY.setPos(self._ItemTraits['_XYCoordinates'][-1][self.idx][0]-6, self._ItemTraits['_XYCoordinates'][-1][self.idx][1]+10)

                self.tmpXY.setDefaultTextColor(Qt.GlobalColor.red)

                self.tmpXY.setTransform(QTransform(1, 0, 0, -1, 0, 0))

                self.tmpXY.setVisible(False)

                self.tmpXY.setZValue(1)

                self.XYVariable.append(self.tmpXY)
                self.block.append(self.tmpXY)
                self.addToGroup(self.tmpXY)

            elif type == 'Sref':
                self.XYVariable.setFont(font)
                self.paramVariable.setFont(font)

                self.XYVariable.setPos(self._ItemTraits['_XYCoordinates'][0][0]-6, self._ItemTraits['_XYCoordinates'][0][1]+10)
                self.paramVariable.setPos(self.bounding_rect_dict['left'] + 20, self.bounding_rect_dict['top'] - 20)

                self.XYVariable.setDefaultTextColor(Qt.GlobalColor.red)
                self.paramVariable.setDefaultTextColor(Qt.GlobalColor.red)

                self.XYVariable.setTransform(QTransform(1, 0, 0, -1, 0, 0))
                self.paramVariable.setTransform(QTransform(1, 0, 0, -1, 0, 0))

                self.XYVariable.setVisible(False)
                self.paramVariable.setVisible(False)

                self.XYVariable.setZValue(1)
                self.paramVariable.setZValue(1)

                self.block.append(self.XYVariable)
                self.block.append(self.paramVariable)
                self.addToGroup(self.XYVariable)
                self.addToGroup(self.paramVariable)

    def setIndex(self, idx):
        self.XYVariable.setVisible(False)
        self.block.remove(self.XYVariable)
        self.XYVariable = QGraphicsTextItemWObounding(str(idx))
        self.setVariable('Boundary')


    def returnItem(self):
        if self._ItemTraits['_DesignParametertype'] == "Boundary":
            return self._BlockGroup
        elif self._ItemTraits['_DesignParametertype'] == "Path":
            pass
        elif self._ItemTraits['_DesignParametertype'] == "SRef":
            pass
        else:
            print("WARNING2: Unvalid DataType Return Request!")


    def move(self,delta):
        # print("delta:",delta)
        if self.isSelected() == True and self._isInHierarchy == False:
            self.setPos( (self.pos()+delta) )
            # self._XYCoordinatesExternal[0] += delta.x()
            # self._XYCoordinatesExternal[1] += delta.y()
            # self.updatePos()
            # for i in range(0,len(self._ItemTraits['_XYCoordinates'])):
            #     print(1)
            #     self._ItemTraits['_XYCoordinates'][i][0] += delta.x()
            #     self._ItemTraits['_XYCoordinates'][i][1] += delta.y()

        pass

    def moveUpdate(self):
        # x = int(self.pos())
        # y = int(self.pos())
        x = self.pos().x()
        y = self.pos().y()
        self._ItemTraits['_XYCoordinates'] = [[int(x),int(y)]]

    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        if self.isSelected():
            self.setSelected(False)

    def save_zvalue_in_memory(self):
        self.z_value_memory = self.zValue()

    def set_hover_flag(self, hover:bool):
        for block in self.childItems():
            if type(block) == _VisualizationItem:
                block.set_hover_flag(hover)
            else:
                block.hover = hover

    def hoverEnterEvent(self, event: 'QGraphicsSceneHoverEvent') -> None:
        super(_VisualizationItem, self).hoverEnterEvent(event)
        # for block in self.block:
        #     block.hover = True
        self.set_hover_flag(True)
        self.update()

    def hoverLeaveEvent(self, event: 'QGraphicsSceneHoverEvent') -> None:
        super(_VisualizationItem, self).hoverLeaveEvent(event)
        self.set_hover_flag(False)
        # for block in self.block:
        #     block.hover = False

    def independent_from_group(self):
        self.original_parent = self.parentItem()
        # tmp_parent_item = _VisualizationItem()
        # tmp_parent_item._ItemTraits = self.original_parent._ItemTraits
        self.original_parent.removeFromGroup(self)
        return self

    def highlight_element_by_hierarchy(self, hierarchy_list):
        tmp_vsitem = self
        while hierarchy_list:
            element_name = hierarchy_list.pop(0)

            if element_name not in tmp_vsitem.sub_element_dict:
                element_name_with_idx_list = list(filter(lambda x: element_name in x, list(tmp_vsitem.sub_element_dict.keys())))
                # for element in element_name_with_idx_list:
                #     # tmp_vsitem.sub_element_dict[element].setSelected(True)
                #     tmp_vsitem.sub_element_dict[element].set_highlight()
                list(map(lambda element: tmp_vsitem.sub_element_dict[element].set_highlight(), element_name_with_idx_list))
                # return None
            else:
                tmp_vsitem = tmp_vsitem.sub_element_dict[element_name]
        # tmp_vsitem.setSelected(True)
        tmp_vsitem.set_highlight()

    def set_highlight(self):
        for _rect_block in self.block:
            if type(_rect_block) == _RectBlock:
                _rect_block.set_highlight()
                _rect_block.update()

    def set_shallow_highlight(self):
        for _rect_block in self.block:
            if type(_rect_block) == _RectBlock:
                _rect_block.set_shallow_highlight()
                _rect_block.update()

    def rerun_for_process_update(self, qt_dp):
        remove_item_list = self.updateDesignParameter(qt_dp)
        return remove_item_list

    def clean_delete(self):
        # remove_item_list = []
        # remove_item_list.extend(self.childItems())
        # for child in remove_item_list:
        #     self.removeFromGroup(child)
        #     remove_item_list.append(child)

        rm_vs_item = self.childItems()
        for child in self.childItems():
            if type(child) == _VisualizationItem:
                rm_vs_item.extend(child.clean_delete())
            else:
                rm_vs_item.extend(child.childItems())
            self.removeFromGroup(child)
        return rm_vs_item
        # child_items = self.childItems()
        # parent_items = []
        # for i in range(len(child_items)):
        #     parent_items.append(self)
        # child_search_stack = self.childItems()
        # while child_search_stack:
        #     child = child_search_stack.pop(0)
        #     parent = parent_items.pop(0)
        #     grandchildren = child.childItems()
        #     if grandchildren:
        #         child_search_stack.extend(grandchildren)
        #         child_items.extend(grandchildren)
        #         for i in range(len(grandchildren)):
        #             parent_items.append(child)
        #     parent.removeFromGroup(child)

        # for child in child_items:
        # #     self.removeFromGroup(child)
        # if self._ItemTraits['_DesignParametertype'] == 1:
        #     for idx, xyPairs in enumerate(self._ItemTraits['_XYCoordinates']):
        #         self.blockGeneration(xyPairs, idx)
        # elif self._ItemTraits['_DesignParametertype'] == 2:
        #     for idx, xyPairs in enumerate(self._ItemTraits['_XYCoordinates']):
        #         self.blockGeneration(xyPairs, idx)
        # elif self._ItemTraits['_DesignParametertype'] == 3:
        #     for idx, xyPairs in enumerate(self._ItemTraits['_XYCoordinates']):
        #         self.blockGeneration(xyPairs, idx)
        # elif self._ItemTraits['_DesignParametertype'] == 8:
        #     self.blockGeneration(self._ItemTraits['_XYCoordinates'])
        # else:
        #     self.blockGeneration()


        # return child_items


        # if self._ItemTraits['_DesignParametertype'] == 1:
        #     for idx, xyPairs in enumerate(self._ItemTraits['_XYCoordinates']):
        #         self.blockGeneration(xyPairs, idx)
        # elif self._ItemTraits['_DesignParametertype'] == 2:
        #     for idx, xyPairs in enumerate(self._ItemTraits['_XYCoordinates']):
        #         self.blockGeneration(xyPairs, idx)
        # elif self._ItemTraits['_DesignParametertype'] == 3:
        #     for idx, xyPairs in enumerate(self._ItemTraits['_XYCoordinates']):
        #         self.blockGeneration(xyPairs, idx)
        # elif self._ItemTraits['_DesignParametertype'] == 8:
        #     self.blockGeneration(self._ItemTraits['_XYCoordinates'])
        # else:
        #     self.blockGeneration()
        #
        #
        #

class QGraphicsTextItemWObounding(QGraphicsTextItem):
    # pass
    def shape(self):
        return QPainterPath()

    # def boundingRect(self) -> QRectF:
    #     return QRect(0,0,0,0)






dict(
    layer           = 16    ,
    layerName       ='PP'   ,
    Datatype        ='0'    ,
    layerUnifiedName='POLY'     ,
    DatatypeName    ='Drawing'  ,
)
