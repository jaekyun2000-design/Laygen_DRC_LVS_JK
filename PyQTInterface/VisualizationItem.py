import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import copy

from PyQTInterface import list_manager

# from PyCodes import QTInterface

from PyQTInterface import LayerInfo
from PyQTInterface.layermap import LayerReader
from PyQTInterface.layermap import DisplayReader
import PyQt5

# from import list_ma

from PyQTInterface import userDefineExceptions
DEBUG = True
scaleValue = 1

class _RectBlock(QGraphicsRectItem):
    def __init__(self,_BlockTraits=None):
        super().__init__()
        self.setFlag(QGraphicsItem.ItemIsSelectable, False)
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
        # list_manager.layer_visible_flag_dict[self.itemtrait['layer']] is False:
        #     self.setVisible(False)

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
            # pen.setColor(self._BlockTraits["_Outline"])
            pen.setColor(Qt.GlobalColor.black)
            pen.setWidth(5)
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
    _compareLayer = dict()
    _Layer = LayerReader._LayerMapping
    _subElementLayer = dict()
    for layer in _Layer:
        _subElementLayer[layer] = list()
    _subElementLayer['SRef'] = list()

    def __init__(self,_ItemTraits=None):
        super().__init__()
        self.setBoundingRegionGranularity(1)
        self._id = None
        self._type = None
        self.setFlag(QGraphicsItemGroup.ItemIsSelectable,True)
        # self._XYCoordinatesForDisplay = []
        self._clickFlag = True
        self._isInHierarchy = False
        self._NoShowFlag = False
        self._SimplifyFlag = False
        self._multipleBlockFlag = False
        self._subSrefVisualItem = None
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
            # self._BlockGroup = None,
        else:
            self._ItemTraits = _ItemTraits
            if self._ItemTraits['_DesignParametertype'] == 1:
                for xyPairs in self._ItemTraits['_XYCoordinates']:
                    self.blockGeneration(xyPairs)
            elif self._ItemTraits['_DesignParametertype'] == 2:
                self.blockGeneration(self._ItemTraits['_XYCoordinates'])
            elif self._ItemTraits['_DesignParametertype'] == 3:
                self.blockGeneration(self._ItemTraits['_XYCoordinates'])
            elif self._ItemTraits['_DesignParametertype'] == 8:
                self.blockGeneration(self._ItemTraits['_XYCoordinates'])
            else:
                self.blockGeneration()

    # def paint(self, painter, option, widget) -> None:
    #     super(_VisualizationItem, self).paint(painter, option, widget)
    #     if self._subSrefVisualItem != None:
    #         self._subSrefVisualItem.paint(painter, option, widget)
    #     pass

    def shape(self):
        if self._type == 1:
            return super().shape()
        elif self._type == 2:
            main_path = QPainterPath()
            for i, block in enumerate(self.block):
                try:
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
        else:
            return super().shape()

    def updateDesignParameter(self,QtDesignParameter):
        self._id = QtDesignParameter._id
        self._type = QtDesignParameter._type
        # try:
        #     oldVersionSupportForXYCoordinatesForDisplay = QtDesignParameter._XYCoordinatesForDisplay
        # except:
        #     QtDesignParameter._XYCoordinatesForDisplay = []
        # if QtDesignParameter._XYCoordinatesForDisplay == [] or QtDesignParameter._XYCoordinatesForDisplay == None:
        #     if QtDesignParameter._DesignParameter['_XYCoordinates']:
        #         QtDesignParameter._XYCoordinatesForDisplay = QtDesignParameter._DesignParameter['_XYCoordinates']
        #     else:
        #         QtDesignParameter._XYCoordinatesForDisplay = [[0,0]]



        if self._type == 1:
            self._ItemTraits['_XYCoordinates'] = QtDesignParameter._DesignParameter['_XYCoordinates']
        elif self._type == 2:
            self._ItemTraits['_XYCoordinates'] = QtDesignParameter._DesignParameter['_XYCoordinates']
        elif self._type == 3:
            self._ItemTraits['_XYCoordinates'] = QtDesignParameter._DesignParameter['_XYCoordinates']
        elif self._type == 8:
            self._ItemTraits['_XYCoordinates'] = QtDesignParameter._DesignParameter['_XYCoordinates']

        if QtDesignParameter._ElementName == None:
            QtDesignParameter._ElementName = QtDesignParameter._id
            self._ItemTraits['_ElementName'] = QtDesignParameter._id
        else:
            self._ItemTraits['_ElementName'] = QtDesignParameter._ElementName
        self.updateTraits(QtDesignParameter._DesignParameter)


    def updateTraits(self,_DesignParameter):
        if self._ItemTraits['_XYCoordinates'] == None or len(self._ItemTraits['_XYCoordinates']) == 0 :
            self._ItemTraits['_XYCoordinates'] = None
        else:
            pass

        for key in _DesignParameter.keys():                      #set itemTrait on Object)
            if key == "_XYCoordinates":    # DesignParameter's XYcoordinate is for real xy coordinates,,,
                self._ItemTraits['_XYCoordinates'] = _DesignParameter[key]                 # Itemtrait's XY coordinate matches QtDesignParameter's XYCoordinatesForDisplay
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
                self.setPos(0,0)
            elif self._ItemTraits['_DesignParametertype'] == 3:
                self.block = []
                self.blockGeneration(self._ItemTraits['_XYCoordinates'])
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
            pass

    def updateDesignObj(self,visualItem):
        self._ItemTraits['_VisualizationItems'].append(visualItem)
        # visualItem.setFlag(QGraphicsItemGroup.ItemIsSelectable,False)
        # visualItem._clickFlag = False
        visualItem._isInHierarchy = True

        for item in self._ItemTraits['_VisualizationItems']:
            self.addToGroup(item)


    def blockGeneration(self,_XYCoordinatesPair=None):                                  #This creates visual Block (which maps boundary or Path Item)
            blockTraits = copy.deepcopy(self._ItemTraits)

            _Layer = LayerReader._LayerMapping                      #Layer and Color Mapping
            _Layer2Name = LayerReader._LayerNameTmp
            DisplayInfo = DisplayReader._DisplayDict
            if self._ItemTraits['_DesignParametertype'] == 1 or self._ItemTraits['_DesignParametertype'] == 2 or self._ItemTraits['_DesignParametertype'] == 8:
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
            self.block=[]

            if self._ItemTraits['_DesignParametertype'] == 1:                              # Boundary Case
                tmpBlock = _RectBlock()
                tmpBlock.updateTraits(blockTraits)
                tmpBlock.setPos(_XYCoordinatesPair[0] - blockTraits['_Width']/2,_XYCoordinatesPair[1] - blockTraits['_Height']/2)

                layernum2name = LayerReader._LayerNumber2CommonLayerName(LayerReader._LayerMapping)
                layer = layernum2name[str(blockTraits['_Layer'])]

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

                ############################ Variable Visualization Start ############################

                for field in self._ItemTraits['variable_info']:
                    if type(self._ItemTraits['variable_info'][field]) is not str:
                        if field == 'XY':
                            self._ItemTraits['variable_info'][field] = str(self._ItemTraits['_XYCoordinates'])
                        elif field == 'width':
                            self._ItemTraits['variable_info'][field] = str(self._ItemTraits['_Width'])
                        elif field == 'height':
                            self._ItemTraits['variable_info'][field] = str(self._ItemTraits['_Height'])

                self.widthVariable = QGraphicsTextItem(self._ItemTraits['variable_info']['width'])
                self.heightVariable = QGraphicsTextItem(self._ItemTraits['variable_info']['height'])
                self.XYVariable = QGraphicsTextItem('*' + self._ItemTraits['variable_info']['XY'])

                self.setVariable(type='Boundary')

                ############################ Variable Visualization End ############################

                self.block.append(tmpBlock)
                self.addToGroup(tmpBlock)



            elif self._ItemTraits['_DesignParametertype'] == 2:                            # Path Case
                for i in range(0,len(_XYCoordinatesPair[0])-1):
                    if float(_XYCoordinatesPair[0][i][0]) == float(_XYCoordinatesPair[0][i+1][0]):          #Vertical Case
                        Xmin = _XYCoordinatesPair[0][i][0] - self._ItemTraits['_Width']/2
                        Xwidth = self._ItemTraits['_Width']
                        Ymin = min(_XYCoordinatesPair[0][i][1],_XYCoordinatesPair[0][i+1][1])
                        Ymax = max(_XYCoordinatesPair[0][i][1],_XYCoordinatesPair[0][i+1][1])
                        Ywidth = Ymax - Ymin

                        if len(_XYCoordinatesPair[0]) == 2:                                                    #Only One Block Case
                            pass
                        elif i == 0:                                                                                        #There are more than 2 segments and First Block Case
                            if _XYCoordinatesPair[0][i][1] < _XYCoordinatesPair[0][i+1][1]:          #UpWard Case
                                Ywidth -= self._ItemTraits['_Width']/2
                            elif _XYCoordinatesPair[0][i][1] > _XYCoordinatesPair[0][i+1][1]:        #DownWard Case
                                Ymin += self._ItemTraits['_Width']/2
                                Ywidth -= self._ItemTraits['_Width']/2
                        elif i == len(_XYCoordinatesPair[0])-2:                                                #Last Block Case
                            if _XYCoordinatesPair[0][i][1] < _XYCoordinatesPair[0][i+1][1]:          #UpWard Case
                                Ymin -= self._ItemTraits['_Width']/2
                                Ywidth += self._ItemTraits['_Width']/2
                            elif _XYCoordinatesPair[0][i][1] > _XYCoordinatesPair[0][i+1][1]:        #DownWard Case
                                Ywidth += self._ItemTraits['_Width']/2
                        else:                                                                                               #Interim Block Case
                            if _XYCoordinatesPair[0][i][1] < _XYCoordinatesPair[0][i+1][1]:          #UpWard Case
                                Ymin -= self._ItemTraits['_Width']/2
                            elif _XYCoordinatesPair[0][i][1] > _XYCoordinatesPair[0][i+1][1]:        #DownWard Case
                                Ymin += self._ItemTraits['_Width']/2
                    else:                                                                                                #Horizontal Case
                        Ymin = _XYCoordinatesPair[0][i][1] - self._ItemTraits['_Width']/2
                        Ywidth = self._ItemTraits['_Width']
                        Xmin = min(_XYCoordinatesPair[0][i][0],_XYCoordinatesPair[0][i+1][0])
                        Xmax = max(_XYCoordinatesPair[0][i][0],_XYCoordinatesPair[0][i+1][0])
                        Xwidth = Xmax - Xmin

                        if len(_XYCoordinatesPair[0]) == 2:                                                    #Only One Block Case
                            pass
                        elif i is 0:                                                                                        #There are more than 2 segments and First Block Case
                            if _XYCoordinatesPair[0][i][0] < _XYCoordinatesPair[0][i+1][0]:          #Path to Right Case
                                Xwidth -= self._ItemTraits['_Width']/2
                            elif _XYCoordinatesPair[0][i][0] > _XYCoordinatesPair[0][i+1][0]:        #Path to Left Case
                                Xwidth -= self._ItemTraits['_Width']/2
                                Xmin += self._ItemTraits['_Width']/2
                        elif i is len(_XYCoordinatesPair[0])-2:
                            if _XYCoordinatesPair[0][i][0] < _XYCoordinatesPair[0][i+1][0]:          #Path to Right Case
                                Xmin -= self._ItemTraits['_Width']/2
                                Xwidth += self._ItemTraits['_Width']/2
                            elif _XYCoordinatesPair[0][i][0] > _XYCoordinatesPair[0][i+1][0]:        #Path to Left Case
                                Xwidth += self._ItemTraits['_Width']/2
                        else:
                            if _XYCoordinatesPair[0][i][0] < _XYCoordinatesPair[0][i+1][0]:          #Path to Right Case
                                Xmin -= self._ItemTraits['_Width']/2
                            elif _XYCoordinatesPair[0][i][0] > _XYCoordinatesPair[0][i+1][0]:        #Path to Left Case
                                Xmin += self._ItemTraits['_Width']/2
                    blockTraits['_Width'] = Xwidth
                    blockTraits['_Height'] = Ywidth

                    layernum2name = LayerReader._LayerNumber2CommonLayerName(LayerReader._LayerMapping)
                    layer = layernum2name[str(blockTraits['_Layer'])]

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

                    self.block.append(_RectBlock(blockTraits))  #Block Generation
                    self.block[i].setPos(Xmin*scaleValue,Ymin*scaleValue)
                    self.addToGroup(self.block[i])

                ############################ Variable Visualization Start ############################
                self.XYVariable = list()
                self._ItemTraits['variable_info']['XY'] = list()

                for field in self._ItemTraits['variable_info']:
                    if type(self._ItemTraits['variable_info'][field]) is not str:
                        if field == 'XY':
                            self._ItemTraits['variable_info'][field] = self._ItemTraits['_XYCoordinates']
                        elif field == 'width':
                            self._ItemTraits['variable_info'][field] = str(self._ItemTraits['_Width'])

                for self.idx in range(len(self._ItemTraits['_XYCoordinates'][0])):
                    if self.idx == 0:
                        self.tmpXY = QGraphicsTextItem('*' + str(self._ItemTraits['variable_info']['XY'][0][self.idx]) + '\nwidth: ' + str(self._ItemTraits['variable_info']['width']))
                    else:
                        self.tmpXY = QGraphicsTextItem('*' + str(self._ItemTraits['variable_info']['XY'][0][self.idx]))

                    self.setVariable(type='Path')

                ############################ Variable Visualization End ############################

            elif self._ItemTraits['_DesignParametertype'] == 3:                #SRef Case
                for sub_element_dp_name, sub_element_dp in self._ItemTraits['_DesignParameterRef'].items():
                    sub_element_vi = _VisualizationItem()
                    sub_element_vi.updateDesignParameter(sub_element_dp)
                    sub_element_vi.setFlag(QGraphicsItemGroup.ItemIsSelectable, False)
                    sub_element_vi.setPos(self._ItemTraits['_XYCoordinates'][0][0], self._ItemTraits['_XYCoordinates'][0][1])

                    layernum2name = LayerReader._LayerNumber2CommonLayerName(LayerReader._LayerMapping)
                    if sub_element_vi._ItemTraits['_Layer'] == None:
                        pass
                    else:
                        layer = layernum2name[str(sub_element_vi._ItemTraits['_Layer'])]
                        self._subElementLayer[layer].append(sub_element_vi)

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
                    self.addToGroup(sub_element_vi)

                ############################ Variable Visualization Start ############################

                for field in self._ItemTraits['variable_info']:
                    if type(self._ItemTraits['variable_info'][field]) is not str:
                        if field == 'XY':
                            self._ItemTraits['variable_info'][field] = str(self._ItemTraits['_XYCoordinates'])
                        elif field == 'parameters':
                            self._ItemTraits['variable_info'][field] = str(self._ItemTraits['parameters'])

                tmpParam = str(self._ItemTraits['variable_info']['parameters']).replace(',', ',\n')

                self.XYVariable = QGraphicsTextItem('*' + self._ItemTraits['variable_info']['XY'])
                self.paramVariable = QGraphicsTextItem(tmpParam)

                self.setVariable(type='Sref')

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

                    # text = QPainter()
                    # aa = QRectF(blockTraits['_XYCoordinates'][0][0],blockTraits['_XYCoordinates'][0][1],100,100)
                    # print(aa)
                    # print(type(blockTraits['_TEXT'].decode()))
                    # # text.scale(1, -1)
                    # text.setPen(Qt.GlobalColor.red)
                    # font = QFont()
                    # font.setBold(True)
                    # font.setPointSize(10)
                    # # text.setFont(font)
                    # text.drawText(aa, Qt.AlignCenter, 'x')
                    # #
                    # #
                    # print("?")

                else:
                    layernum2name = LayerReader._LayerNumber2CommonLayerName(LayerReader._LayerMapping)
                    layer = layernum2name[str(blockTraits['_Layer'])]
                    if 'PIN' in layer:
                        try:
                            self.text = QGraphicsTextItem(blockTraits['_TEXT'].decode())
                        except:
                            self.text = QGraphicsTextItem(blockTraits['_TEXT'])

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

            else:
                print("WARNING1: Unvalid DataType Detected!")

            # print('--')
            # print(self._subElementLayer)
            # self.send_subelementlayer_signal.emit(self._subElementLayer)

    def update_dc_variable_info(self, _ast):
        if _ast._type == 'Boundary':
            self.widthVariable.setVisible(False)
            self.heightVariable.setVisible(False)
            self.XYVariable.setVisible(False)

            self.block.remove(self.widthVariable)
            self.block.remove(self.heightVariable)
            self.block.remove(self.XYVariable)

            self.widthVariable = QGraphicsTextItem(str(_ast.width))
            self.heightVariable = QGraphicsTextItem(str(_ast.height))
            self.XYVariable = QGraphicsTextItem('*' + str(_ast.XY))

            self.setVariable(_ast._type)

        elif _ast._type == 'Path':
            replaceXYVariable = self.XYVariable
            self.XYVariable = list()
            for self.idx in range(len(self._ItemTraits['_XYCoordinates'][0])):
                self.replaceXY = replaceXYVariable[self.idx]
                self.replaceXY.setVisible(False)

                self.block.remove(self.replaceXY)

                if self.idx == 0:
                    self.tmpXY = QGraphicsTextItem('*' + str(_ast.XY[0][self.idx]) + '\nwidth: ' + str(_ast.width))
                else:
                    self.tmpXY = QGraphicsTextItem('*' + str(_ast.XY[0][self.idx]))

                self.setVariable(_ast._type)

        elif _ast._type == 'Sref':
            self.XYVariable.setVisible(False)
            self.paramVariable.setVisible(False)

            self.block.remove(self.XYVariable)
            self.block.remove(self.paramVariable)

            tmpParam = str(_ast.parameters).replace(',', ',\n')

            self.XYVariable = QGraphicsTextItem('*' + str(_ast.XY))
            self.paramVariable = QGraphicsTextItem(tmpParam)

            self.setVariable(_ast._type)

    def returnLayerDict(self):
        return self._subElementLayer

    def setVariable(self, type=None):
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

            self.tmpXY.setPos(self._ItemTraits['_XYCoordinates'][0][self.idx][0]-6, self._ItemTraits['_XYCoordinates'][0][self.idx][1]+10)

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
            self.paramVariable.setPos(self.boundingRect().bottomLeft().x() + 20, self.boundingRect().bottomLeft().y() - 20)

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

