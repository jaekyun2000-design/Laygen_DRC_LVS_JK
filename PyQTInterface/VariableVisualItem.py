import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from PyQt5.QtWidgets import*
from PyQt5.QtGui import QColor,QPen,QBrush,QTransform
from PyQt5.QtCore import Qt
import copy

# from PyCodes import QTInterface

from PyQTInterface import LayerInfo
from PyQTInterface.layermap import LayerReader
from PyQTInterface.layermap import DisplayReader
import PyQt5

from PyQTInterface import userDefineExceptions

scaleValue = 1

class VariableVisualItem(QGraphicsItemGroup):
    def __init__(self, variable_traits=None):
        super().__init__()
        self.variable_id = None
        self.type = None
        self.setFlag(QGraphicsItemGroup.ItemIsSelectable,True)
        self.sub_visual_item = []


    def addToGroupFromList(self,visual_item_list):
        self.sub_visual_item.extend(visual_item_list)
        for vsitem in visual_item_list:
            self.addToGroup(vsitem)
        #
        # self._XYCoordinatesForDisplay = []
        # self._clickFlag = True
        # self._isInHierarchy = False
        # self._NoShowFlag = False
        # self._SimplifyFlag = False
        # self._multipleBlockFlag = False
        # if _ItemTraits is None:
        #     self._ItemTraits = dict(
        #         _DesignParameterName = None,
        #         _Layer = None,
        #
        #         _DesignParametertype = None,
        #         _XYCoordinates = None,
        #         _Width = None,
        #         _Height = None,
        #         _Color = None,
        #         _DesignParameterRef=None,   #Reference of Design Parameter
        #         _VisualizationItems = []    #This is for SRef!!
        #     )
        #     self.block = []
        #     # self._BlockGroup = None,
        # else:
        #     self._ItemTraits = _ItemTraits
        #     self.block = []
        #     self.blockGeneration()

