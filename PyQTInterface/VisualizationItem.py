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

class _RectBlock(QGraphicsRectItem):
    def __init__(self,_BlockTraits=None):
        super().__init__()
        # self.setFlag(QGraphicsItem.ItemIsSelectable,False)
        if _BlockTraits is None:
            self._BlockTraits = dict(
                _Layer = None,
                _LayerName = None,
                _XYCoordinates = None,

                _Width = None,
                _Height = None,
                _Color = None,
                _ItemRef = None, #Reference Of VisualizationItem

            )


        else:
            self._BlockTraits = _BlockTraits
            self.updateRect()

    def updateTraits(self,_BlockTraits):
        for key in _BlockTraits.keys():
            self._BlockTraits[key] = _BlockTraits[key]
        # self.layerName2paintTrait()
        self.updateRect()



    def updateRect(self):
        # if self._BlockTraits['_DesignParametertype'] is "Boundary" :
        if self._BlockTraits["_XYCoordinates"] is None:
            self._BlockTraits["_XYCoordinates"] = [[0,0]]

        if type(self._BlockTraits['_Width']) == str:
            if not self._BlockTraits["_Width"]:
                print("ERROR: Unvalid Width")
                return None
            self._BlockTraits['_Width'] = int(self._BlockTraits['_Width'])

        if type(self._BlockTraits['_Height']) == str:
            if not self._BlockTraits["_Height"]:
                print("ERROR: Unvalid Height")
                return None
            self._BlockTraits['_Height'] = int(self._BlockTraits['_Height'])


        self.setRect(0,
                     0,
                     self._BlockTraits["_Width"]*scaleValue,
                     self._BlockTraits["_Height"]*scaleValue )


    def paint(self, painter, option, widget=None):
        self._BlockTraits["_Color"].setAlphaF(1)

        pen = QPen()
        pen.setColor(self._BlockTraits["_Outline"])
        brush = QBrush()
        brush.setColor(self._BlockTraits["_Color"])

        # print(self.zValue())

        if self.isSelected():
            # self._BlockTraits["_Color"].setAlphaF(1)
            # self.setZValue(self.zValue()*10000)
            # print("HighLighted",self.zValue())
            pen.setStyle(Qt.DashLine)
            pen.setColor(self._BlockTraits["_Outline"])
            pen.setWidth(3)
            self.setZValue(1)
        else:
            self.setZValue(self._BlockTraits['_Layer']/1000)


        if self._BlockTraits["_Pattern"] == "blank":
            brush.setStyle(Qt.NoBrush)
        elif self._BlockTraits["_Pattern"] == "solid":
            brush.setStyle(Qt.SolidPattern)
        elif self._BlockTraits["_Pattern"] == "dots":
            brush.setStyle(Qt.Dense1Pattern)
        elif self._BlockTraits["_Pattern"] == "dot4":
            brush.setStyle(Qt.Dense6Pattern)
        elif self._BlockTraits["_Pattern"] == "hLine":
            brush.setStyle(Qt.HorPattern)
        elif self._BlockTraits["_Pattern"] == "vLine":
            brush.setStyle(Qt.VerPattern)
        elif self._BlockTraits["_Pattern"] == "cross":
            brush.setStyle(Qt.DiagCrossPattern)
        elif self._BlockTraits["_Pattern"] == "grid":
            brush.setStyle(Qt.CrossPattern)
        elif self._BlockTraits["_Pattern"] == "slash":
            brush.setStyle(Qt.BDiagPattern)
        elif self._BlockTraits["_Pattern"] == "backSlash":
            brush.setStyle(Qt.FDiagPattern)


        elif self._BlockTraits["_Pattern"] == "stipple0":
            brush.setStyle(Qt.BDiagPattern)
        elif self._BlockTraits["_Pattern"] == "dagger":
            brush.setStyle(Qt.Dense7Pattern)
        elif self._BlockTraits["_Pattern"] == "brick":
            brush.setStyle(Qt.CrossPattern)
            # brush.setTransform()
        else:
            brush.setStyle(Qt.SolidPattern)

        #
        # if not (self._BlockTraits["_Pattern"] == "blank" or self._BlockTraits["_Pattern"] == "stipple0" or self._BlockTraits["_Pattern"] == "dagger" or self._BlockTraits["_Pattern"] == "brick"):
        #     brush.setStyle(Qt.SolidPattern)

        brush.setTransform(QTransform(painter.worldTransform().inverted()[0]))
        # print("zValue : ", self.zValue())
        painter.setPen(pen)
        painter.setBrush(brush)

        painter.drawRect(self.rect())


    def layerName2paintTrait(self):

        try:
            DisplayInfo = DisplayReader._DisplayDict
            color = DisplayInfo[self._BlockTraits['_LayerName']]['Fill']
        except:
            self.warning=QMessageBox()
            self.warning.setText("There is no matching QT Color profile")
            print("Color Traits Error")
            self.warning.show()


class _VisualizationItem(QGraphicsItemGroup):
    def __init__(self,_ItemTraits=None):
        super().__init__()

        self._id = None
        self._type = None
        self.setFlag(QGraphicsItemGroup.ItemIsSelectable,True)
        # self._XYCoordinatesForDisplay = []
        self._clickFlag = True
        self._isInHierarchy = False
        self._NoShowFlag = False
        self._SimplifyFlag = False
        self._multipleBlockFlag = False
        if _ItemTraits is None:
            self._ItemTraits = dict(
                _DesignParameterName = None,
                _Layer = None,

                _DesignParametertype = None,
                _XYCoordinates = None,
                _Width = None,
                _Height = None,
                _Color = None,
                _DesignParameterRef=None,   #Reference of Design Parameter
                _VisualizationItems = []    #This is for SRef!!
            )
            self.block = []
            # self._BlockGroup = None,
        else:
            self._ItemTraits = _ItemTraits
            self.block = []
            self.blockGeneration()

    def updateDesignParameter(self,QtDesignParameter):
        self._id = QtDesignParameter._id
        self._type = QtDesignParameter._type
        try:
            oldVersionSupportForXYCoordinatesForDisplay = QtDesignParameter._XYCoordinatesForDisplay
        except:
            QtDesignParameter._XYCoordinatesForDisplay = []
        if QtDesignParameter._XYCoordinatesForDisplay == [] or QtDesignParameter._XYCoordinatesForDisplay == None:
            if QtDesignParameter._DesignParameter['_XYCoordinatesForDisplay']:
                QtDesignParameter._XYCoordinatesForDisplay = QtDesignParameter._DesignParameter['_XYCoordinatesForDisplay']
            else:
                QtDesignParameter._XYCoordinatesForDisplay = [[0,0]]



        if self._type == 1:
            self._ItemTraits['_XYCoordinates'] = QtDesignParameter._XYCoordinatesForDisplay
            QtDesignParameter._DesignParameter["_XYCoordinatesForDisplay"] = QtDesignParameter._XYCoordinatesForDisplay
        elif self._type == 2:
            self._ItemTraits['_XYCoordinates'] = QtDesignParameter._XYCoordinatesForDisplay
            QtDesignParameter._DesignParameter["_XYCoordinatesForDisplay"] = QtDesignParameter._XYCoordinatesForDisplay

        if QtDesignParameter._DesignParameterName == None:
            QtDesignParameter._DesignParameterName = QtDesignParameter._id
            self._ItemTraits['_DesignParameterName'] = QtDesignParameter._id
        else:
            self._ItemTraits['_DesignParameterName'] = QtDesignParameter._DesignParameterName
        self.updateTraits(QtDesignParameter._DesignParameter)
        # tmpX = self._XYCoordinatesForDisplay[0][0]
        # tmpY = self._XYCoordinatesForDisplay[0][1]
        # self.setPos(tmpX,tmpY)


    def updateTraits(self,_DesignParameter):
        if self._ItemTraits['_XYCoordinates'] or len(self._ItemTraits['_XYCoordinates']) == 0 :
            self._ItemTraits['_XYCoordinates'] = [[0,0]]
        else:
            pass
            # self._ItemTraits['_XYCoordinates'] = self._XYCoordinatesForDisplay

        for key in _DesignParameter.keys():                      #set itemTrait on Object)
            if key == "_XYCoordinates":
                self._ItemTraits[key] = _DesignParameter[key]
            if key == "_XYCoordinatesForDisplay":
                  self._ItemTraits["_XYCoordinates"] = _DesignParameter["_XYCoordinatesForDisplay"]

            elif key == "_DesignParameterName":
                self._DesignParameterName = _DesignParameter[key]
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
        elif self._ItemTraits['_DesignParametertype'] == 3:
            pass

        if self._multipleBlockFlag == None:
            _multipleBlockFlag = False



        for i in range(0,len(self.block)):
            self.removeFromGroup(self.block[i])
        if self._ItemTraits['_DesignParametertype'] == 1:
            self.block = []
            for xyPairs in self._ItemTraits['_XYCoordinates']:
                self.blockGeneration(xyPairs)
            self.setPos(0,0)
        elif self._ItemTraits['_DesignParametertype'] == 2:
            self.block = []
            self.blockGeneration(self._ItemTraits['_XYCoordinates'])
            # for xyPairs in self._ItemTraits['_XYCoordinates']:
            #     print([xyPairs])
            #     self.blockGeneration([xyPairs])
            self.setPos(0,0)
        else:
            self.block = []
            self.blockGeneration()
            self.setPos(0,0)
        # self.setPos(self._XYCoordinatesForDisplay[0],self._XYCoordinatesForDisplay[1])
        # print("last:",self.pos())
        # self.updatePos()

    #
    # def updatePos(self):
    #     self.setPos(self._XYCoordinatesExternal[0],self._XYCoordinatesExternal[1])
    def updateDesignObj(self,visualItem):
        self._ItemTraits['_VisualizationItems'].append(visualItem)
        # visualItem.setFlag(QGraphicsItemGroup.ItemIsSelectable,False)
        # visualItem._clickFlag = False
        visualItem._isInHierarchy = True

        for item in self._ItemTraits['_VisualizationItems']:
                # self.block.append(_RectBlock())
                # self.block[i].updateTraits(blockTraits)
                # self.block[i].setPos(self._XYCoordinatesForDisplay[i][0],self._XYCoordinatesForDisplay[i][1])
            self.addToGroup(item)

    #BlockGeneration Original!!
    # def blockGeneration(self):                                  #This creates visual Block (which maps boundary or Path Item)
    #     blockTraits = copy.deepcopy(self._ItemTraits)
    #
    #     _Layer = LayerReader._LayerMapping                      #Layer and Color Mapping
    #     _Layer2Name = LayerReader._LayerNameTmp
    #     DisplayInfo = DisplayReader._DisplayDict
    #     if self._ItemTraits['_DesignParametertype'] == 1 or self._ItemTraits['_DesignParametertype'] == 2:
    #         if type(self._ItemTraits['_Layer']) == str:                         #When GUI Creates DesignParameter --> It has Layer Information in the form of "String" : ex) Met1, Met2, Via12, PIMP
    #             blockTraits['_Layer'] =  _Layer[self._ItemTraits['_Layer']][0]     #Layer Number             --> Convert Name to Number
    #             blockTraits['_LayerName'] =  _Layer[self._ItemTraits['_Layer']][2]  #Layer Original Name    --> Original Name is required to access color information
    #         else:                                                               #When GUI load DesignParameter from GDS File --> It has Layer Information in the form of "Number" : ex) 1,4,7
    #             blockTraits['_Layer'] =  self._ItemTraits['_Layer']     #Layer Number
    #             blockTraits['_LayerName'] =  _Layer2Name[str(blockTraits['_Layer'])]#Layer Original Name        -->Original Name is required to access color infromation
    #         print(blockTraits['_DesignParameterName'])
    #         blockTraits['_Color'] =  DisplayInfo[blockTraits['_LayerName']]['Fill']
    #         blockTraits['_Outline'] =  DisplayInfo[blockTraits['_LayerName']]['Outline']
    #         blockTraits['_Pattern'] =  DisplayInfo[blockTraits['_LayerName']]['Stipple']
    #
    #
    #
    #     del _Layer
    #     # blockTraits['_Layer'] = _Layer._Layer[self._ItemTraits['_Layer']]
    #     # blockTraits['_XYCoordinates'] = [[0,0]]
    #     # del _Layer
    #     self.block=[]
    #
    #     if self._ItemTraits['_DesignParametertype'] is 1:                              # Boundary Case
    #         # self.block.append(_RectBlock())
    #         # self.block[0].updateTraits(blockTraits)
    #         # self.block[0].setPos(self._XYCoordinatesForDisplay[0][0],self._XYCoordinatesForDisplay[0][1])
    #         # self.addToGroup(self.block[0])
    #         # for i in range(0,len(self._ItemTraits['_XYCoordinates'])):
    #         for i in range(0,1):
    #             self.block.append(_RectBlock())
    #             self.block[i].updateTraits(blockTraits)
    #             self.block[i].setPos(self._XYCoordinatesForDisplay[i][0]*scaleValue,self._XYCoordinatesForDisplay[i][1]*scaleValue)
    #             self.addToGroup(self.block[i])
    #
    #
    #
    #
    #     elif self._ItemTraits['_DesignParametertype'] is 2:                            # Path Case
    #         for i in range(0,len(self._ItemTraits['_XYCoordinates'])-1):
    #             if float(self._ItemTraits["_XYCoordinates"][i][0]) == float(self._ItemTraits["_XYCoordinates"][i+1][0]):          #Vertical Case
    #                 Xmin = self._ItemTraits['_XYCoordinates'][i][0] - self._ItemTraits['_Width']/2
    #                 Xwidth = self._ItemTraits['_Width']
    #                 Ymin = min(self._ItemTraits['_XYCoordinates'][i][1],self._ItemTraits['_XYCoordinates'][i+1][1])
    #                 Ymax = max(self._ItemTraits['_XYCoordinates'][i][1],self._ItemTraits['_XYCoordinates'][i+1][1])
    #                 Ywidth = Ymax - Ymin
    #
    #                 if len(self._ItemTraits['_XYCoordinates']) is 2:                                                    #Only One Block Case
    #                     pass
    #                 elif i is 0:                                                                                        #There are more than 2 segments and First Block Case
    #                     if self._ItemTraits["_XYCoordinates"][i][1] < self._ItemTraits["_XYCoordinates"][i+1][1]:          #UpWard Case
    #                         Ywidth -= self._ItemTraits['_Width']/2
    #                     elif self._ItemTraits["_XYCoordinates"][i][1] > self._ItemTraits["_XYCoordinates"][i+1][1]:        #DownWard Case
    #                         Ymin += self._ItemTraits['_Width']/2
    #                         Ywidth -= self._ItemTraits['_Width']/2
    #                 elif i is len(self._ItemTraits['_XYCoordinates'])-2:                                                #Last Block Case
    #                     if self._ItemTraits["_XYCoordinates"][i][1] < self._ItemTraits["_XYCoordinates"][i+1][1]:          #UpWard Case
    #                         Ymin -= self._ItemTraits['_Width']/2
    #                         Ywidth += self._ItemTraits['_Width']/2
    #                     elif self._ItemTraits["_XYCoordinates"][i][1] > self._ItemTraits["_XYCoordinates"][i+1][1]:        #DownWard Case
    #                         Ywidth += self._ItemTraits['_Width']/2
    #                 else:                                                                                               #Interim Block Case
    #                     if self._ItemTraits["_XYCoordinates"][i][1] < self._ItemTraits["_XYCoordinates"][i+1][1]:          #UpWard Case
    #                         Ymin -= self._ItemTraits['_Width']/2
    #                     elif self._ItemTraits["_XYCoordinates"][i][1] > self._ItemTraits["_XYCoordinates"][i+1][1]:        #DownWard Case
    #                         Ymin += self._ItemTraits['_Width']/2
    #             else:                                                                                                #Horizontal Case
    #                 print(self._ItemTraits['_XYCoordinates'][i][1])
    #                 print(self._ItemTraits['_Width'])
    #                 Ymin = self._ItemTraits['_XYCoordinates'][i][1] - self._ItemTraits['_Width']/2
    #                 Ywidth = self._ItemTraits['_Width']
    #                 Xmin = min(self._ItemTraits['_XYCoordinates'][i][0],self._ItemTraits['_XYCoordinates'][i+1][0])
    #                 Xmax = max(self._ItemTraits['_XYCoordinates'][i][0],self._ItemTraits['_XYCoordinates'][i+1][0])
    #                 Xwidth = Xmax - Xmin
    #
    #                 if len(self._ItemTraits['_XYCoordinates']) is 2:                                                    #Only One Block Case
    #                     pass
    #                 elif i is 0:                                                                                        #There are more than 2 segments and First Block Case
    #                     if self._ItemTraits["_XYCoordinates"][i][0] < self._ItemTraits["_XYCoordinates"][i+1][0]:          #Path to Right Case
    #                         Xwidth -= self._ItemTraits['_Width']/2
    #                     elif self._ItemTraits["_XYCoordinates"][i][0] > self._ItemTraits["_XYCoordinates"][i+1][0]:        #Path to Left Case
    #                         Xwidth -= self._ItemTraits['_Width']/2
    #                         Xmin += self._ItemTraits['_Width']/2
    #                 elif i is len(self._ItemTraits['_XYCoordinates'])-2:
    #                     if self._ItemTraits["_XYCoordinates"][i][0] < self._ItemTraits["_XYCoordinates"][i+1][0]:          #Path to Right Case
    #                         Xmin -= self._ItemTraits['_Width']/2
    #                         Xwidth += self._ItemTraits['_Width']/2
    #                     elif self._ItemTraits["_XYCoordinates"][i][0] > self._ItemTraits["_XYCoordinates"][i+1][0]:        #Path to Left Case
    #                         Xwidth += self._ItemTraits['_Width']/2
    #                 else:
    #                     if self._ItemTraits["_XYCoordinates"][i][0] < self._ItemTraits["_XYCoordinates"][i+1][0]:          #Path to Right Case
    #                         Xmin -= self._ItemTraits['_Width']/2
    #                     elif self._ItemTraits["_XYCoordinates"][i][0] > self._ItemTraits["_XYCoordinates"][i+1][0]:        #Path to Left Case
    #                         Xmin += self._ItemTraits['_Width']/2
    #             blockTraits['_Width'] = Xwidth
    #             blockTraits['_Height'] = Ywidth
    #             self.block.append(_RectBlock(blockTraits))  #Block Generation
    #             self.block[i].setPos(Xmin*scaleValue,Ymin*scaleValue)
    #             self.addToGroup(self.block[i])
    #         # for xyPairs in (self._ItemTraits['_XYCoordinates']):
    #         #     for i in range(0,len(xyPairs)-1):
    #         #         if float(xyPairs[i][0]) == float(xyPairs[i+1][0]):          #Vertical Case
    #         #             Xmin = xyPairs[i][0] - self._ItemTraits['_Width']/2
    #         #             Xwidth = self._ItemTraits['_Width']
    #         #             Ymin = min(xyPairs[i][1],xyPairs[i+1][1])
    #         #             Ymax = max(xyPairs[i][1],xyPairs[i+1][1])
    #         #             Ywidth = Ymax - Ymin
    #         #
    #         #             if len(xyPairs) is 2:                                                    #Only One Block Case
    #         #                 pass
    #         #             elif i is 0:                                                                                        #There are more than 2 segments and First Block Case
    #         #                 if xyPairs[i][1] < xyPairs[i+1][1]:          #UpWard Case
    #         #                     Ywidth -= self._ItemTraits['_Width']/2
    #         #                 elif xyPairs[i][1] > xyPairs[i+1][1]:        #DownWard Case
    #         #                     Ymin += self._ItemTraits['_Width']/2
    #         #                     Ywidth -= self._ItemTraits['_Width']/2
    #         #             elif i is len(xyPairs)-2:                                                #Last Block Case
    #         #                 if xyPairs[i][1] < xyPairs[i+1][1]:          #UpWard Case
    #         #                     Ymin -= self._ItemTraits['_Width']/2
    #         #                     Ywidth += self._ItemTraits['_Width']/2
    #         #                 elif xyPairs[i][1] > xyPairs[i+1][1]:        #DownWard Case
    #         #                     Ywidth += self._ItemTraits['_Width']/2
    #         #             else:                                                                                               #Interim Block Case
    #         #                 if xyPairs[i][1] < xyPairs[i+1][1]:          #UpWard Case
    #         #                     Ymin -= self._ItemTraits['_Width']/2
    #         #                 elif xyPairs[i][1] > xyPairs[i+1][1]:        #DownWard Case
    #         #                     Ymin += self._ItemTraits['_Width']/2
    #         #         else:                                                                                                #Horizontal Case
    #         #             print(xyPairs[i][1])
    #         #             print(self._ItemTraits['_Width'])
    #         #             Ymin = xyPairs[i][1] - self._ItemTraits['_Width']/2
    #         #             Ywidth = self._ItemTraits['_Width']
    #         #             Xmin = min(xyPairs[i][0],xyPairs[i+1][0])
    #         #             Xmax = max(xyPairs[i][0],xyPairs[i+1][0])
    #         #             Xwidth = Xmax - Xmin
    #         #
    #         #             if len(xyPairs) is 2:                                                    #Only One Block Case
    #         #                 pass
    #         #             elif i is 0:                                                                                        #There are more than 2 segments and First Block Case
    #         #                 if xyPairs[i][0] < xyPairs[i+1][0]:          #Path to Right Case
    #         #                     Xwidth -= self._ItemTraits['_Width']/2
    #         #                 elif xyPairs[i][0] > xyPairs[i+1][0]:        #Path to Left Case
    #         #                     Xwidth -= self._ItemTraits['_Width']/2
    #         #                     Xmin += self._ItemTraits['_Width']/2
    #         #             elif i is len(xyPairs)-2:
    #         #                 if xyPairs[i][0] < xyPairs[i+1][0]:          #Path to Right Case
    #         #                     Xmin -= self._ItemTraits['_Width']/2
    #         #                     Xwidth += self._ItemTraits['_Width']/2
    #         #                 elif xyPairs[i][0] > xyPairs[i+1][0]:        #Path to Left Case
    #         #                     Xwidth += self._ItemTraits['_Width']/2
    #         #             else:
    #         #                 if xyPairs[i][0] < xyPairs[i+1][0]:          #Path to Right Case
    #         #                     Xmin -= self._ItemTraits['_Width']/2
    #         #                 elif xyPairs[i][0] > xyPairs[i+1][0]:        #Path to Left Case
    #         #                     Xmin += self._ItemTraits['_Width']/2
    #         #         blockTraits['_Width'] = Xwidth
    #         #         blockTraits['_Height'] = Ywidth
    #         #         self.block.append(_RectBlock(blockTraits))  #Block Generation
    #         #         self.block[i].setPos(Xmin*scaleValue,Ymin*scaleValue)
    #         #         self.addToGroup(self.block[i])
    #     elif self._ItemTraits['_DesignParametertype'] is 3:                #SRef Case
    #         for item in self._ItemTraits['_VisualizationItems']:
    #             # self.block.append(_RectBlock())
    #             # self.block[i].updateTraits(blockTraits)
    #             # self.block[i].setPos(self._XYCoordinatesForDisplay[i][0],self._XYCoordinatesForDisplay[i][1])
    #             self.addToGroup(item)
    #
    #         # self.addToGroup(self.block[i])
    #         # for Obj in self._ItemTraits['_DesignObj']:
    #         #     pass
    #         # self.addToGroup(self.SRefComponent)
    #         pass
    #     elif self._ItemTraits['_DesignParametertype'] is 8:                #Test Case
    #         pass
    #     else:
    #         print("WARNING1: Unvalid DataType Detected!")
    def blockGeneration(self,_XYCoordinatesPair=None):                                  #This creates visual Block (which maps boundary or Path Item)
            blockTraits = copy.deepcopy(self._ItemTraits)

            _Layer = LayerReader._LayerMapping                      #Layer and Color Mapping
            _Layer2Name = LayerReader._LayerNameTmp
            DisplayInfo = DisplayReader._DisplayDict
            if self._ItemTraits['_DesignParametertype'] == 1 or self._ItemTraits['_DesignParametertype'] == 2:
                if type(self._ItemTraits['_Layer']) == str:                         #When GUI Creates DesignParameter --> It has Layer Information in the form of "String" : ex) Met1, Met2, Via12, PIMP
                    blockTraits['_Layer'] =  _Layer[self._ItemTraits['_Layer']][0]     #Layer Number             --> Convert Name to Number
                    blockTraits['_LayerName'] =  _Layer[self._ItemTraits['_Layer']][2]  #Layer Original Name    --> Original Name is required to access color information
                else:                                                               #When GUI load DesignParameter from GDS File --> It has Layer Information in the form of "Number" : ex) 1,4,7
                    blockTraits['_Layer'] =  self._ItemTraits['_Layer']     #Layer Number
                    blockTraits['_LayerName'] =  _Layer2Name[str(blockTraits['_Layer'])]#Layer Original Name        -->Original Name is required to access color infromation
                blockTraits['_Color'] =  DisplayInfo[blockTraits['_LayerName']]['Fill']
                blockTraits['_Outline'] =  DisplayInfo[blockTraits['_LayerName']]['Outline']
                blockTraits['_Pattern'] =  DisplayInfo[blockTraits['_LayerName']]['Stipple']



            del _Layer
            del _Layer2Name
            # blockTraits['_Layer'] = _Layer._Layer[self._ItemTraits['_Layer']]
            # blockTraits['_XYCoordinates'] = [[0,0]]
            # del _Layer
            self.block=[]

            if self._ItemTraits['_DesignParametertype'] is 1:                              # Boundary Case
                # self.block.append(_RectBlock())
                # self.block[0].updateTraits(blockTraits)
                # self.block[0].setPos(self._XYCoordinatesForDisplay[0][0],self._XYCoordinatesForDisplay[0][1])
                # self.addToGroup(self.block[0])
                # for i in range(0,len(self._ItemTraits['_XYCoordinates'])):
                # for i in range(0,1):
                #     self.block.append(_RectBlock())
                #     self.block[i].updateTraits(blockTraits)
                #     self.block[i].setPos(self._XYCoordinatesForDisplay[i][0]*scaleValue,self._XYCoordinatesForDisplay[i][1]*scaleValue)
                #     self.addToGroup(self.block[i])
                tmpBlock = _RectBlock()
                tmpBlock.updateTraits(blockTraits)
                tmpBlock.setPos(_XYCoordinatesPair[0],_XYCoordinatesPair[1])
                self.block.append(tmpBlock)
                self.addToGroup(tmpBlock)



            elif self._ItemTraits['_DesignParametertype'] is 2:                            # Path Case
                for i in range(0,len(_XYCoordinatesPair)-1):
                    if float(_XYCoordinatesPair[i][0]) == float(_XYCoordinatesPair[i+1][0]):          #Vertical Case
                        Xmin = _XYCoordinatesPair[i][0] - self._ItemTraits['_Width']/2
                        Xwidth = self._ItemTraits['_Width']
                        Ymin = min(_XYCoordinatesPair[i][1],_XYCoordinatesPair[i+1][1])
                        Ymax = max(_XYCoordinatesPair[i][1],_XYCoordinatesPair[i+1][1])
                        Ywidth = Ymax - Ymin

                        if len(_XYCoordinatesPair) is 2:                                                    #Only One Block Case
                            pass
                        elif i is 0:                                                                                        #There are more than 2 segments and First Block Case
                            if _XYCoordinatesPair[i][1] < _XYCoordinatesPair[i+1][1]:          #UpWard Case
                                Ywidth -= self._ItemTraits['_Width']/2
                            elif _XYCoordinatesPair[i][1] > _XYCoordinatesPair[i+1][1]:        #DownWard Case
                                Ymin += self._ItemTraits['_Width']/2
                                Ywidth -= self._ItemTraits['_Width']/2
                        elif i is len(_XYCoordinatesPair)-2:                                                #Last Block Case
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
                    else:                                                                                                #Horizontal Case
                        Ymin = _XYCoordinatesPair[i][1] - self._ItemTraits['_Width']/2
                        Ywidth = self._ItemTraits['_Width']
                        Xmin = min(_XYCoordinatesPair[i][0],_XYCoordinatesPair[i+1][0])
                        Xmax = max(_XYCoordinatesPair[i][0],_XYCoordinatesPair[i+1][0])
                        Xwidth = Xmax - Xmin

                        if len(_XYCoordinatesPair) is 2:                                                    #Only One Block Case
                            pass
                        elif i is 0:                                                                                        #There are more than 2 segments and First Block Case
                            if _XYCoordinatesPair[i][0] < _XYCoordinatesPair[i+1][0]:          #Path to Right Case
                                Xwidth -= self._ItemTraits['_Width']/2
                            elif _XYCoordinatesPair[i][0] > _XYCoordinatesPair[i+1][0]:        #Path to Left Case
                                Xwidth -= self._ItemTraits['_Width']/2
                                Xmin += self._ItemTraits['_Width']/2
                        elif i is len(_XYCoordinatesPair)-2:
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
                    blockTraits['_Width'] = Xwidth
                    blockTraits['_Height'] = Ywidth
                    self.block.append(_RectBlock(blockTraits))  #Block Generation
                    self.block[i].setPos(Xmin*scaleValue,Ymin*scaleValue)
                    self.addToGroup(self.block[i])
            elif self._ItemTraits['_DesignParametertype'] is 3:                #SRef Case
                for item in self._ItemTraits['_VisualizationItems']:
                    # self.block.append(_RectBlock())
                    # self.block[i].updateTraits(blockTraits)
                    # self.block[i].setPos(self._XYCoordinatesForDisplay[i][0],self._XYCoordinatesForDisplay[i][1])
                    self.addToGroup(item)

                # self.addToGroup(self.block[i])
                # for Obj in self._ItemTraits['_DesignObj']:
                #     pass
                # self.addToGroup(self.SRefComponent)
                pass
            elif self._ItemTraits['_DesignParametertype'] is 8:                #Test Case
                pass
            else:
                print("WARNING1: Unvalid DataType Detected!")


    def returnItem(self):
        if self._ItemTraits['_DesignParametertype'] is "Boundary":
            return self._BlockGroup
        elif self._ItemTraits['_DesignParametertype'] is "Path":
            pass
        elif self._ItemTraits['_DesignParametertype'] is "SRef":
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
