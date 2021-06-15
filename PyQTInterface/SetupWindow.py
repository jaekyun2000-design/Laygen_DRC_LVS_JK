import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsView, QGraphicsScene, QGraphicsItem
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# from PyQTInterface  import LayerInfo
from PyQTInterface.layermap  import LayerReader
from PyQTInterface  import VisualizationItem

from PyCodes import ASTmodule
from PyCodes import element_ast

import logging
import copy
from PyCodes import userDefineExceptions
from PyCodes import EnvForClientSetUp
from PyCodes import QTInterfaceWithAST

from generatorLib import generator_model_api
import traceback
import re, ast, time, sys

debugFlag = True

class _BoundarySetupWindow(QWidget):

    send_BoundarySetup_signal = pyqtSignal(VisualizationItem._VisualizationItem)
    send_BoundaryDesign_signal = pyqtSignal(dict)
    send_Destroy_signal = pyqtSignal(str)
    send_Warning_signal = pyqtSignal(str)
    send_DestroyTmpVisual_signal = pyqtSignal(VisualizationItem._VisualizationItem)

    def __init__(self,BoundaryElement= None):
        super().__init__()
        self.mouse = None
        self.click = 0
        self.initUI()

        if BoundaryElement == None:
            self.visualItem = VisualizationItem._VisualizationItem()
            self._DesignParameter = dict(
                _Layer= None,
                _DesignParametertype = 1,
                _XYCoordinates = [],
                _XWidth = None,
                _YWidth = None,
                _Ignore = None,
                _ElementName = None

                )
        else:
            # self.visualItem = BoundaryElement
            self._DesignParameter = BoundaryElement._ItemTraits
            self.updateUI()



    def initUI(self):
        okButton = QPushButton("OK",self)
        cancelButton = QPushButton("Cancel",self)

        okButton.clicked.connect(self.on_buttonBox_accepted)
        cancelButton.clicked.connect(self.cancel_button_accepted)

        self.XYdictForLineEdit = []
        self.XYdictForLabel = []
        self.tmpXYCoordinates = []

        name = QLabel("Element Name")
        width = QLabel("Width")
        height = QLabel("Height")
        layer = QLabel("Layer")
        self.XYdictForLabel.append(QLabel("XY"))

        self.name_input = QLineEdit()
        self.width_input = QLineEdit()
        self.height_input = QLineEdit()
        self.layer_input = QComboBox()
        self.XYdictForLineEdit.append(QLineEdit())

        _Layer = LayerReader._LayerMapping
        for LayerName in _Layer:
            if _Layer[LayerName][1] != None:       ## Layer is drawing
                if not 'PIN' in LayerName:
                    self.layer_input.addItem(LayerName)
        #
        # _Layer = LayerInfo._Layer()
        # for LayerName in _Layer._LayerName:
        #     self.layer_input.addItem(LayerName)
        # del _Layer

        self.setupVboxColumn1 = QVBoxLayout()
        self.setupVboxColumn2 = QVBoxLayout()
        setupBox = QHBoxLayout()

        self.setupVboxColumn1.addWidget(name)
        self.setupVboxColumn1.addWidget(width)
        self.setupVboxColumn1.addWidget(height)
        self.setupVboxColumn1.addWidget(layer)
        self.setupVboxColumn1.addWidget(self.XYdictForLabel[0])


        self.setupVboxColumn2.addWidget(self.name_input)
        self.setupVboxColumn2.addWidget(self.width_input)
        self.setupVboxColumn2.addWidget(self.height_input)
        self.setupVboxColumn2.addWidget(self.layer_input)
        self.setupVboxColumn2.addWidget(self.XYdictForLineEdit[0])

        setupBox.addLayout(self.setupVboxColumn1)
        setupBox.addLayout(self.setupVboxColumn2)

        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        # hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(setupBox)
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        # vbox.addStretch(1)

        self.setLayout(vbox)


        self.setWindowTitle('Boundary Setup Window')
        self.setGeometry(300,300,500,500)
        self.show()


    def updateUI(self):
        self.name_input.setText(self._DesignParameter['_ElementName'])
        self.width_input.setText(str(self._DesignParameter['_XWidth']))
        self.height_input.setText(str(self._DesignParameter['_YWidth']))
        self.XYdictForLineEdit[0].setText(str(self._DesignParameter['_XYCoordinates'][0][0])+','+ str(self._DesignParameter['_XYCoordinates'][0][1]))
        if type(self._DesignParameter['_Layer']) == int:
            _Layer = LayerReader._LayerMapping
            # _Layer2Name = LayerReader._LayerNameTmp
            # _layerNumber = str(self._DesignParameter['_Layer'])
            for layerExpressionName in _Layer:
                print("layerExpressionName:",layerExpressionName,_Layer[layerExpressionName][0],self._DesignParameter['_Layer'])
                if _Layer[layerExpressionName][0] == self._DesignParameter['_Layer']:
                    self._DesignParameter['_Layer'] = str(layerExpressionName)
                    break

            # self._DesignParameter['_Layer'] =  _Layer2Name[_layerNumber]     #Layer Number             --> Convert Name to Number
            del _Layer
            layerIndex = self.layer_input.findText(self._DesignParameter['_Layer'])
        else:
            layerIndex = self.layer_input.findText(self._DesignParameter['_Layer'])
        if layerIndex != -1:
            self.layer_input.setCurrentIndex(layerIndex)
        #setCurrentIndex
        #findText
        # self.

    def cancel_button_accepted(self):
        self.send_Destroy_signal.emit('bw')
        self.send_DestroyTmpVisual_signal.emit(self.visualItem)
        self.destroy()

    def on_buttonBox_accepted(self):
        for XY in self.XYdictForLineEdit:
            if not XY.text():
                break
            # elif type(XY.text()) == str:
            #     self._DesignParameter['_XYCoordinates'] = self.determineVariableValue("XY", XY.text())
            #     pass
            else:
                try:
                    X = int(XY.text().split(',')[0])
                    Y = int(XY.text().split(',')[1])
                    # self._DesignParameter['_XYCoordinates']=[[X+float(self.width_input.text())/2,Y+float(self.height_input.text())/2]]
                    self._DesignParameter['_XYCoordinates']=[[X,Y]]
                    # self._DesignParameter['_XYCoordinatesForDisplay'] = [[X,Y]]
                except:
                    self.warning = QMessageBox()
                    self.warning.setIcon(QMessageBox.Warning)
                    self.warning.setText("Invalid XY Coordinates")

        try:
            self._DesignParameter['_ElementName'] = self.name_input.text()
            if self._DesignParameter['_ElementName'] == '':
                raise NotImplementedError
            self._DesignParameter['_XWidth'] = float(self.width_input.text())
            self._DesignParameter['_YWidth'] = float(self.height_input.text())
            self._DesignParameter['_Layer'] = self.layer_input.currentText()
            try:
                self.send_DestroyTmpVisual_signal.emit(self.visualItem)
            except:
                pass
            self.send_BoundaryDesign_signal.emit(self._DesignParameter)
            self.destroy()

            if type(self._DesignParameter['_XWidth']) == str:
                self.warning = QMessageBox()
                self.warning.setText("test")
                self.warning.setIcon(QMessageBox.Warning)
                self.warning.show()
        except:
            self.send_Warning_signal.emit("Invalid Design Parameter Input")     #log message
            self.warning = QMessageBox()
            self.warning.setText("Invalid design parameter or Name")
            self.warning.setIcon(QMessageBox.Warning)
            self.warning.show()

    def determineVariableValue(self, _type, _variable):
        return [[0,0]]
        pass

    def AddBoundaryPointWithMouse(self,_MouseEvent):
        if self.click < 2:
            ##### When Click the point, adjust x,y locations #####
            if len(self.tmpXYCoordinates) == 0:
                self.tmpXYCoordinates.append([_MouseEvent.scenePos().toPoint().x(),_MouseEvent.scenePos().toPoint().y()])

            else:
                self.tmpXYCoordinates.append([_MouseEvent.scenePos().toPoint().x(),_MouseEvent.scenePos().toPoint().y()])

                xdistance = abs(self.tmpXYCoordinates[-1][0] - self.tmpXYCoordinates[-2][0])
                ydistance = abs(self.tmpXYCoordinates[-1][1] - self.tmpXYCoordinates[-2][1])
                origin = [(self.tmpXYCoordinates[-1][0]+self.tmpXYCoordinates[-2][0])/2,(self.tmpXYCoordinates[-1][1]+self.tmpXYCoordinates[-2][1])/2]
                self.tmpXYCoordinates.pop(0)

                self._DesignParameter['_XWidth'] = xdistance
                self._DesignParameter['_YWidth'] = ydistance
                self._DesignParameter['_XYCoordinates'] = [origin]
                self.width_input.setText(str(self._DesignParameter['_XWidth']))
                self.height_input.setText(str(self._DesignParameter['_YWidth']))
                self.XYdictForLineEdit[0].setText(str(origin[0])+','+str(origin[1]))

            self._DesignParameter['_Layer'] = self.layer_input.currentText()

            self.visualItem.updateTraits(self._DesignParameter)
            self.send_BoundarySetup_signal.emit(self.visualItem)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_buttonBox_accepted()
            self.send_Destroy_signal.emit('bw')
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.send_DestroyTmpVisual_signal.emit(self.visualItem)
            self.destroy()
            self.send_Destroy_signal.emit('bw')

    def mouseTracking(self, event):
        if self.mouse is not None and self.click < 2:
            xdistance = abs(self.mouse.x() - event.scenePos().x())
            ydistance = abs(self.mouse.y() - event.scenePos().y())
            origin = [(self.mouse.x()+event.scenePos().x())/2, (self.mouse.y()+event.scenePos().y())/2]
            self._DesignParameter['_XWidth'] = xdistance
            self._DesignParameter['_YWidth'] = ydistance
            self._DesignParameter['_XYCoordinates'] = [origin]
            self._DesignParameter['_Layer'] = self.layer_input.currentText()
            self.visualItem.updateTraits(self._DesignParameter)
            self.visualItem.setFlag(QGraphicsItemGroup.ItemIsSelectable,False)
            self.send_BoundarySetup_signal.emit(self.visualItem)

    def clickCount(self, _MouseEvent):
        self.mouse = _MouseEvent.scenePos()
        self.click += 1

class _PathSetupWindow(QWidget):

    send_PathSetup_signal = pyqtSignal(VisualizationItem._VisualizationItem)
    send_PathDesign_signal = pyqtSignal(dict)
    # send_Destroy_signal = pyqtSignal("PyQt_PyObject")
    send_Destroy_signal = pyqtSignal(str)
    send_DestroyTmpVisual_signal = pyqtSignal(VisualizationItem._VisualizationItem)

    def __init__(self, PathElement = None):
        super().__init__()
        self.mouse = None
        self.click = 0
        self.initUI()

        if PathElement is None:
            self._DesignParameter = dict(
                    _ElementName = None,
                    _Layer = None,
                    _DesignParametertype = 2,
                    _XYCoordinates = [],
                    _Width = None,
                    _Height = None,
                    _Color = None,
                    _ItemRef = None, #Reference Of VisualizationItem

                )
            self.visualItem = VisualizationItem._VisualizationItem()
            self.tmpVI = VisualizationItem._VisualizationItem()
            self.tmpDP = copy.deepcopy(self._DesignParameter)
        else:
            # self.visualItem = PathElement
            self.visualItem = VisualizationItem._VisualizationItem()
            self._DesignParameter = PathElement._ItemTraits
            self.updateUI()



    def __del__(self):
        print("del")

    def initUI(self):

        okButton = QPushButton("OK",self)
        cancelButton = QPushButton("Cancel",self)

        okButton.clicked.connect(self.on_buttonBox_accepted)
        cancelButton.clicked.connect(self.cancel_button_accepted)


        self.XYdictForLineEdit = []
        self.XYdictForLabel = []

        name = QLabel("Name")
        width = QLabel("Width")
        layer = QLabel("Layer")
        self.XYdictForLabel.append(QLabel("XY1"))
        self.XYdictForLabel.append(QLabel("XY2"))

        self.name_input = QLineEdit()
        self.width_input = QLineEdit()
        self.layer_input = QComboBox()
        self.XYdictForLineEdit.append(QLineEdit())
        self.XYdictForLineEdit.append(QLineEdit())

        _Layer = LayerReader._LayerMapping
        for LayerName in _Layer:
            if _Layer[LayerName][1] == 0:       ## Layer is drawing
                self.layer_input.addItem(LayerName)
        del _Layer
        #
        # _Layer = LayerInfo._Layer()
        # for LayerName in _Layer._LayerName:
        #     self.layer_input.addItem(LayerName)
        # del _Layer

        self.setupVboxColumn1 = QVBoxLayout()
        self.setupVboxColumn2 = QVBoxLayout()
        setupBox = QHBoxLayout()

        self.setupVboxColumn1.addWidget(name)
        self.setupVboxColumn1.addWidget(width)
        self.setupVboxColumn1.addWidget(layer)
        self.setupVboxColumn1.addWidget(self.XYdictForLabel[0])
        self.setupVboxColumn1.addWidget(self.XYdictForLabel[1])


        self.setupVboxColumn2.addWidget(self.name_input)
        self.setupVboxColumn2.addWidget(self.width_input)
        self.setupVboxColumn2.addWidget(self.layer_input)
        self.setupVboxColumn2.addWidget(self.XYdictForLineEdit[0])
        self.setupVboxColumn2.addWidget(self.XYdictForLineEdit[1])

        setupBox.addLayout(self.setupVboxColumn1)
        setupBox.addLayout(self.setupVboxColumn2)

        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        # hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(setupBox)
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        # vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Path Setup Window')
        self.setGeometry(300,300,500,500)
        self.show()

    def updateUI(self):
        self.name_input.setText(self._DesignParameter['_ElementName'])
        self.width_input.setText(str(self._DesignParameter['_Width']))
        if type(self._DesignParameter['_Layer']) == int:
            layernum2name = LayerReader._LayerNumber2CommonLayerName(LayerReader._LayerMapping)
            _tmplayer = layernum2name[str(self._DesignParameter['_Layer'])]
            layerIndex = self.layer_input.findText(_tmplayer)
        else:
            layerIndex = self.layer_input.findText(self._DesignParameter['_Layer'])
        if layerIndex != -1:
            self.layer_input.setCurrentIndex(layerIndex)
        for i in range(len(self._DesignParameter['_XYCoordinates'][0])):
            CurrentEditPointNum = len(self.XYdictForLineEdit)-2
            displayString= str(self._DesignParameter['_XYCoordinates'][0][i][0])+','+ str(self._DesignParameter['_XYCoordinates'][0][i][1])
            self.XYdictForLineEdit[CurrentEditPointNum].setText(displayString)
            self.UpdateXYwidget()


    def cancel_button_accepted(self):
        self._DesignParameter = dict(
                    _ElementName = None,
                    _Layer = None,
                    _DesignParametertype = 2,
                    _XYCoordinates = [],
                    _Width = None,
                    _Height = None,
                    _Color = None,
                    _ItemRef = None, #Reference Of VisualizationItem
                )
        self.visualItem.updateTraits(self._DesignParameter)
        self.send_Destroy_signal.emit('pw')
        self.destroy()

    def on_buttonBox_accepted(self):
        try:
            self._DesignParameter['_ElementName'] = self.name_input.text()
            if self._DesignParameter['_ElementName'] == '':
                raise NotImplementedError
            self._DesignParameter['_Width'] = self.width_input.text()
            self._DesignParameter['_Layer'] = self.layer_input.currentText()
            self._DesignParameter['_XYCoordinates'] = [[]]

            for XY in self.XYdictForLineEdit:
                if not XY.text():
                    break
                else:
                    try:

                        X = int(XY.text().split(',')[0])
                        Y = int(XY.text().split(',')[1])
                        self._DesignParameter['_XYCoordinates'][0].append([X, Y])
                    except:
                        self.warning = QMessageBox()
                        self.warning.setIcon(QMessageBox.Warning)
                        self.warning.setText("Invalid XYCoordinates")
                        self.warning.show()

            pass
            self.send_DestroyTmpVisual_signal.emit(self.visualItem)
            try:
                self.send_DestroyTmpVisual_signal.emit(self.tmpVI)
            except:
                pass
            self.send_PathDesign_signal.emit(self._DesignParameter)
            self.destroy()
            self.send_Destroy_signal.emit('pw')
            pass
        except:
            self.warning = QMessageBox()
            self.warning.setIcon(QMessageBox.Warning)
            self.warning.setText("Invalid Name")
            self.warning.show()


    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_buttonBox_accepted()
            self.send_Destroy_signal.emit('pw')
        elif QKeyEvent.key() == Qt.Key_Escape:
            self._DesignParameter = dict(
                        _ElementName = None,
                        _Layer = None,
                        _DesignParametertype = 2,
                        _XYCoordinates = [],
                        _Width = None,
                        _Height = None,
                        _Color = None,
                        _ItemRef = None, #Reference Of VisualizationItem
                    )
            self.visualItem.updateTraits(self._DesignParameter)
            self.send_DestroyTmpVisual_signal.emit(self.tmpVI)
            self.destroy()
            self.send_Destroy_signal.emit('pw')

    def AddPathPointWithMouse(self,_MouseEvent):
        # print(self._DesignParameter)

        ##### When Click the point, adjust x,y locations #####
        try:
            if len(self._DesignParameter['_XYCoordinates']) == 0:
                self._DesignParameter['_XYCoordinates'].append([[_MouseEvent.scenePos().toPoint().x(),_MouseEvent.scenePos().toPoint().y()]])
            else:
                xdistance = abs(_MouseEvent.scenePos().x() - self._DesignParameter['_XYCoordinates'][0][-1][0])
                ydistance = abs(_MouseEvent.scenePos().y() - self._DesignParameter['_XYCoordinates'][0][-1][1])

                if xdistance < ydistance:
                    self._DesignParameter['_XYCoordinates'][0].append([self._DesignParameter['_XYCoordinates'][0][-1][0],_MouseEvent.scenePos().toPoint().y()])
                else:
                    self._DesignParameter['_XYCoordinates'][0].append([_MouseEvent.scenePos().toPoint().x(),self._DesignParameter['_XYCoordinates'][0][-1][1]])

            # self._DesignParameter['_XYCoordinates'].append([_MouseEvent.scenePos().toPoint().x(),_MouseEvent.scenePos().toPoint().y(),])

            CurrentEditPointNum = len(self.XYdictForLineEdit)-2
            XYstring = str(self._DesignParameter['_XYCoordinates'][0][-1][0]) + ',' + str(self._DesignParameter['_XYCoordinates'][0][-1][1])
            self.XYdictForLineEdit[CurrentEditPointNum].setText(XYstring)
            self.UpdateXYwidget()
            self._DesignParameter['_Width'] = self.width_input.text()
            self._DesignParameter['_Layer'] = self.layer_input.currentText()
            self.visualItem._ItemTraits['_XYCoordinates'] = self._DesignParameter['_XYCoordinates']
            self.visualItem.updateTraits(self._DesignParameter)
            self.visualItem.setFlag(QGraphicsItemGroup.ItemIsSelectable,False)
            self.send_PathSetup_signal.emit(self.visualItem)
        except:
            print('======a============')
            self.warning = QMessageBox()
            self.warning.setIcon(QMessageBox.Warning)
            self.warning.setText("Invalid Parameter Input")
            self.warning.show()

    def UpdateXYwidget(self):
        CurrentPointNum = len(self.XYdictForLineEdit)
        NewPointNum = CurrentPointNum + 1
        LabelText = "XY" + str(NewPointNum)

        self.XYdictForLabel.append(QLabel(LabelText))
        self.XYdictForLineEdit.append(QLineEdit())

        self.setupVboxColumn1.addWidget(self.XYdictForLabel[-1])
        self.setupVboxColumn2.addWidget(self.XYdictForLineEdit[-1])

    def mouseTracking(self, event):
        if self.mouse is not None:
            if self.click == 0:
                xdistance = abs(self.mouse.x() - event.scenePos().x())
                ydistance = abs(self.mouse.y() - event.scenePos().y())

                if xdistance < ydistance:
                    self.tmpDP['_XYCoordinates'] = [[[self.mouse.x(),self.mouse.y()],[self.mouse.x(),event.scenePos().y()]]]
                else:
                    self.tmpDP['_XYCoordinates'] = [[[self.mouse.x(),self.mouse.y()],[event.scenePos().x(),self.mouse.y()]]]
            else:
                xdistance = abs(self._DesignParameter['_XYCoordinates'][0][-1][0] - event.scenePos().x())
                ydistance = abs(self._DesignParameter['_XYCoordinates'][0][-1][1] - event.scenePos().y())

                if xdistance < ydistance:
                    self.tmpDP['_XYCoordinates'] = [[[self._DesignParameter['_XYCoordinates'][0][-1][0],self._DesignParameter['_XYCoordinates'][0][-1][1]],[self._DesignParameter['_XYCoordinates'][0][-1][0],event.scenePos().y()]]]
                else:
                    self.tmpDP['_XYCoordinates'] = [[[self._DesignParameter['_XYCoordinates'][0][-1][0],self._DesignParameter['_XYCoordinates'][0][-1][1]],[event.scenePos().x(),self._DesignParameter['_XYCoordinates'][0][-1][1]]]]

            self.tmpDP['_Width'] = self.width_input.text()
            self.tmpDP['_Layer'] = self.layer_input.currentText()
            self.tmpVI.updateTraits(self.tmpDP)
            self.send_PathSetup_signal.emit(self.tmpVI)
            self.tmpVI.setFlag(QGraphicsItemGroup.ItemIsSelectable,False)

    def clickCount(self, _MouseEvent):
        self.mouse = _MouseEvent.scenePos()
        self.click += 1

class _SRefSetupWindowOG(QWidget):

    send_SRefSetup_signal = pyqtSignal(VisualizationItem._VisualizationItem)
    send_Destroy_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.initUI()


        self.visualItem = VisualizationItem._VisualizationItem()
        self._DesignParameter = dict(
                _Name = None,
                _DataType = "SRef",
                _XYCoordinates = [],
                _ItemRef = None #Reference Of VisualizationItem
        )


    def initUI(self):
        saveButton = QPushButton("SAVE",self)
        loadButton = QPushButton("LOAD",self)
        cancelButton = QPushButton("Cancel",self)

        saveButton.clicked.connect(self.on_saveBox_accepted)

        # self._DesignParameter = dict()

        name = QLabel("Name")
        self.name_input = QLineEdit()


        self.setupVboxColumn1 = QVBoxLayout()
        self.setupVboxColumn2 = QVBoxLayout()
        setupBox = QHBoxLayout()

        self.setupVboxColumn1.addWidget(name)


        self.setupVboxColumn2.addWidget(self.name_input)

        setupBox.addLayout(self.setupVboxColumn1)
        setupBox.addLayout(self.setupVboxColumn2)

        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(saveButton)
        hbox.addWidget(loadButton)
        hbox.addWidget(cancelButton)
        # hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(setupBox)
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        # vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('SRef Setup Window')
        self.setGeometry(300,300,500,500)
        self.show()

    def on_saveBox_accepted(self):
        # save implement!!
        self.destroy()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            pass
        #self.send_Destroy_signal.emit()
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.destroy()
        #self.send_Destroy_signal.emit()

class _SRefSetupWindow(QWidget):

    send_SRefSetup_signal = pyqtSignal(VisualizationItem._VisualizationItem)
    send_SRefDesign_signal = pyqtSignal(dict)
    send_Destroy_signal = pyqtSignal(str)
    send_Warning_signal = pyqtSignal(str)

    def __init__(self,SRefElement= None):
        super().__init__()
        self.initUI()

        if SRefElement == None:
            self.visualItem = VisualizationItem._VisualizationItem()
            self._DesignParameter = dict(
                _Layer= None,
                _DesignParametertype = 3,
                _XYCoordinates = [],
                _XWidth = None,
                _YWidth = None,
                _Ignore = None,
                _ElementName = None

                )
        else:
            # self.visualItem = BoundaryElement
            self._DesignParameter = SRefElement._ItemTraits
            self.updateUI()



    def initUI(self):
        okButton = QPushButton("OK",self)
        cancelButton = QPushButton("Cancel",self)

        okButton.clicked.connect(self.on_buttonBox_accepted)
        cancelButton.clicked.connect(self.cancel_button_accepted)

        name = QLabel("Element Name")
        width = QLabel("Width")
        height = QLabel("Height")
        layer = QLabel("Layer")
        self.name_input = QLineEdit()
        self.width_input = QLineEdit()
        self.height_input = QLineEdit()
        self.layer_input = QComboBox()

        _Layer = LayerReader._LayerMapping
        for LayerName in _Layer:
            if _Layer[LayerName][1] == 0:       ## Layer is drawing
                self.layer_input.addItem(LayerName)
        #
        # _Layer = LayerInfo._Layer()
        # for LayerName in _Layer._LayerName:
        #     self.layer_input.addItem(LayerName)
        # del _Layer

        self.setupVboxColumn1 = QVBoxLayout()
        self.setupVboxColumn2 = QVBoxLayout()
        setupBox = QHBoxLayout()

        self.setupVboxColumn1.addWidget(name)
        self.setupVboxColumn1.addWidget(width)
        self.setupVboxColumn1.addWidget(height)
        self.setupVboxColumn1.addWidget(layer)


        self.setupVboxColumn2.addWidget(self.name_input)
        self.setupVboxColumn2.addWidget(self.width_input)
        self.setupVboxColumn2.addWidget(self.height_input)
        self.setupVboxColumn2.addWidget(self.layer_input)

        setupBox.addLayout(self.setupVboxColumn1)
        setupBox.addLayout(self.setupVboxColumn2)

        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        # hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(setupBox)
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        # vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Boundary Setup Window')
        self.setGeometry(300,300,500,500)
        self.show()

    def updateUI(self):
        self.name_input.setText(self._DesignParameter['_ElementName'])
        self.width_input.setText(str(self._DesignParameter['_XWidth']))
        self.height_input.setText(str(self._DesignParameter['_YWidth']))
        if type(self._DesignParameter['_Layer']) == int:
            _Layer = LayerReader._LayerMapping
            # _Layer2Name = LayerReader._LayerNameTmp
            # _layerNumber = str(self._DesignParameter['_Layer'])
            for layerExpressionName in _Layer:
                print("layerExpressionName:",layerExpressionName,_Layer[layerExpressionName][0],self._DesignParameter['_Layer'])
                if _Layer[layerExpressionName][0] == self._DesignParameter['_Layer']:
                    self._DesignParameter['_Layer'] = str(layerExpressionName)
                    break

            # self._DesignParameter['_Layer'] =  _Layer2Name[_layerNumber]     #Layer Number             --> Convert Name to Number
            del _Layer
            layerIndex = self.layer_input.findText(self._DesignParameter['_Layer'])
        else:
            layerIndex = self.layer_input.findText(self._DesignParameter['_Layer'])
        if layerIndex != -1:
            self.layer_input.setCurrentIndex(layerIndex)
        #setCurrentIndex
        #findText
        # self.

    def cancel_button_accepted(self):
        self.destroy()
    def on_buttonBox_accepted(self):

        try:
            self._DesignParameter['_ElementName'] = self.name_input.text()
            self._DesignParameter['_XWidth'] = float(self.width_input.text())
            self._DesignParameter['_YWidth'] = float(self.height_input.text())
            self._DesignParameter['_Layer'] = self.layer_input.currentText()
            self.send_BoundaryDesign_signal.emit(self._DesignParameter)
            self.destroy()
        except:
            self.send_Warning_signal.emit("Invalid Design Parameter Input")
            self.warning = QMessageBox()
            self.warning.setText("Invalid design parameter input")
            self.warning.setIcon(QMessageBox.Warning)
            self.warning.show()


    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_buttonBox_accepted()
            self.send_Destroy_signal.emit('sw')
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.destroy()
            self.send_Destroy_signal.emit('sw')

class _LoadSRefWindow(QWidget):

    send_DesignConstraint_signal = pyqtSignal("PyQt_PyObject")
    send_destroy_signal = pyqtSignal(str)

    def __init__(self, SRefElement = None, create=False):
        super().__init__()
        self.create = create
        self.par_valueForLineEdit = []
        self.paramDict = dict()
        self.initUI()

        if SRefElement is None:
            self.create = True
            self.visualItem = VisualizationItem._VisualizationItem()
        else:
            self._DesignParameter = SRefElement._ItemTraits
            self.updateUI()

    def initUI(self):
        self.name = QLabel("name")
        self.library = QLabel("library")
        self.class_name = QLabel("className")
        self.XY = QLabel("XY")
        self.cal_fcn = QLabel("calculate_fcn")

        self.pars = QLabel("\nPARAMETERS")

        self.name_input = QLineEdit()
        self.library_input = QComboBox()
        self.class_name_input = QLineEdit()
        self.XY_input = QLineEdit()
        self.cal_fcn_input = QComboBox()

        self.library_input.addItems(generator_model_api.class_dict.keys())
        self.class_name_input.setText(generator_model_api.class_name_dict[self.library_input.currentText()])
        self.cal_fcn_input.addItems(generator_model_api.class_function_dict[self.library_input.currentText()])

        self.class_name_input.setEnabled(False)
        pars_font = QFont('tmp',10)
        self.pars.setFont(pars_font)
        self.pars.setAlignment(Qt.AlignCenter)

        self.library_input.currentIndexChanged.connect(self.updateClassName)
        self.library_input.currentIndexChanged.connect(self.updatecalfcn)
        self.cal_fcn_input.currentIndexChanged.connect(self.updateparameter)

        okButton = QPushButton("OK",self)
        cancelButton = QPushButton("Cancel",self)

        okButton.clicked.connect(self.on_buttonBox_accepted)
        cancelButton.clicked.connect(self.cancel_button_accepted)

        self.setupVboxColumn1 = QVBoxLayout()
        self.setupVboxColumn2 = QVBoxLayout()
        setupHBox1 = QHBoxLayout()
        setupHBox2 = QHBoxLayout()

        self.setupVboxColumn1.addWidget(self.name)
        self.setupVboxColumn1.addWidget(self.library)
        self.setupVboxColumn1.addWidget(self.class_name)
        self.setupVboxColumn1.addWidget(self.XY)
        self.setupVboxColumn1.addWidget(self.cal_fcn)

        self.setupVboxColumn2.addWidget(self.name_input)
        self.setupVboxColumn2.addWidget(self.library_input)
        self.setupVboxColumn2.addWidget(self.class_name_input)
        self.setupVboxColumn2.addWidget(self.XY_input)
        self.setupVboxColumn2.addWidget(self.cal_fcn_input)

        self.parVBox1 = QVBoxLayout()
        self.parVBox2 = QVBoxLayout()

        self.par_name = []
        self.par_value = []
        par_list = generator_model_api.class_function_dict[self.library_input.currentText()][self.cal_fcn_input.currentText()]
        for idx in range(len(par_list)):
            self.par_name.append(par_list[idx].name)
            self.par_value.append(par_list[idx].default)

            self.par_valueForLineEdit.append(QLineEdit())
            self.par_valueForLineEdit[-1].setText(str(self.par_value[-1]))

            self.parVBox1.addWidget(QLabel(self.par_name[-1]))
            self.parVBox2.addWidget(self.par_valueForLineEdit[-1])

        setupHBox1.addLayout(self.setupVboxColumn1)
        setupHBox1.addLayout(self.setupVboxColumn2)
        setupHBox2.addLayout(self.parVBox1)
        setupHBox2.addLayout(self.parVBox2)

        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(setupHBox1)
        vbox.addWidget(self.pars)
        vbox.addLayout(setupHBox2)
        vbox.addStretch(3)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setWindowTitle('LoadSRef Window')
        self.setGeometry(300,300,500,500)
        self.show()

    def updateUI(self):
        self.name_input.setText(self._DesignParameter['_ElementName'])
        self.library_input.setCurrentText(self._DesignParameter['library'])
        self.class_name_input.setText(self._DesignParameter['className'])
        self.XY_input.setText(str(self._DesignParameter['_XYCoordinates'][0][0])+','+str(self._DesignParameter['_XYCoordinates'][0][1]))
        if 'calculate_fcn' in self._DesignParameter.keys():
            self.cal_fcn_input.setCurrentText(self._DesignParameter['calculate_fcn'])
        i = 0
        for value in self._DesignParameter['parameters'].values():
            self.par_valueForLineEdit[i].setText(str(value))
            i += 1

    def updateClassName(self):
        self.class_name_input.setText(generator_model_api.class_name_dict[self.library_input.currentText()])

    def updatecalfcn(self):
        self.cal_fcn_input.clear()
        self.cal_fcn_input.addItems(generator_model_api.class_function_dict[self.library_input.currentText()])

    def updateparameter(self):
        while self.parVBox1.count() != 0:
            tmp = self.parVBox1.takeAt(0).widget()
            tmp.setParent(None)
            del tmp
            tmp = self.parVBox2.takeAt(0).widget()
            tmp.setParent(None)
            self.parVBox2.removeWidget(tmp)
            del tmp

        self.par_valueForLineEdit = []

        if self.cal_fcn_input.currentText() == "":
            pass
        else:
            self.par_name = []
            self.par_value = []
            par_list = generator_model_api.class_function_dict[self.library_input.currentText()][self.cal_fcn_input.currentText()]
            for idx in range(len(par_list)):
                self.par_name.append(par_list[idx].name)
                self.par_value.append(par_list[idx].default)

                self.par_valueForLineEdit.append(QLineEdit())
                self.par_valueForLineEdit[-1].setText(str(self.par_value[-1]))

                self.parVBox1.addWidget(QLabel(self.par_name[-1]))
                self.parVBox2.addWidget(self.par_valueForLineEdit[-1])

    def DetermineCoordinateWithMouse(self, _MouseEvent):
        self.XY_input.setText(str(_MouseEvent.scenePos().toPoint().x()) + ',' + str(_MouseEvent.scenePos().toPoint().y()))

    def on_buttonBox_accepted(self):
        for idx in range(len(self.par_valueForLineEdit)):
            self.paramDict[self.par_name[idx]] = self.par_valueForLineEdit[idx].text()

        tmpAST = element_ast.Sref()
        for key in element_ast.Sref._fields:
            if key == 'name':
                tmpAST.__dict__[key] = self.name_input.text()
            elif key == 'library':
                tmpAST.__dict__[key] = self.library_input.currentText()
            elif key == 'className':
                tmpAST.__dict__[key] = self.class_name_input.text()
            elif key == 'XY':
                # tmpAST.__dict__[key] = self.XY_input.text()
                tmpAST.__dict__[key] = [[float(i) for i in self.XY_input.text().split(',')]]
            elif key == 'calculate_fcn':
                tmpAST.__dict__[key] = self.cal_fcn_input.currentText()
            elif key == 'parameters':
                tmpAST.__dict__[key] = self.paramDict

        if not self.create:
            tmpAST._id = self._DesignParameter['_id']
        self.send_DesignConstraint_signal.emit(tmpAST)
        # if self.create:
        #     self.send_DesignConstraint_signal.emit(tmpAST)
        # else:
        #     tmpAST._id = self._DesignParameter['_id']
        #     self.send_DesignConstraint_signal.emit(self._DesignParameter)

        self.destroy()

    def cancel_button_accepted(self):
        self.destroy()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return or QKeyEvent.key() == Qt.Key_Enter:
            self.on_buttonBox_accepted()
            self.send_destroy_signal.emit('ls')
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.destroy()
            self.send_destroy_signal.emit('ls')

class _TextSetupWindow(QWidget):

    send_TextSetup_signal = pyqtSignal(VisualizationItem._VisualizationItem)
    send_TextDesign_signal = pyqtSignal(dict)
    send_Destroy_signal = pyqtSignal(str)
    send_Warning_signal = pyqtSignal(str)
    send_DestroyTmpVisual_signal = pyqtSignal(VisualizationItem._VisualizationItem)

    def __init__(self,TextElement=None):
        super().__init__()
        self.initUI()
        if TextElement == None:
            self.visualItem = VisualizationItem._VisualizationItem()
            self._DesignParameter = dict(
                _ElementName = None,
                _DesignParametertype = 8,
                _Layer = 'text',
                _XYCoordinates = [],
                _Presentation = None,
                _Reflect = None,
                _Mag = None,
                _Angle = None,
                _TEXT = None
                )
        else:
            self._DesignParameter = TextElement._ItemTraits
            self.updateUI()


    def initUI(self):
        okButton = QPushButton("OK",self)
        cancelButton = QPushButton("Cancel",self)

        okButton.clicked.connect(self.on_buttonBox_accepted)
        cancelButton.clicked.connect(self.cancel_button_accepted)

        self.text = None
        self.mag = None
        self.XY_input = []

        textLabel = QLabel("Text")
        magLabel = QLabel("Width")
        XYLabel = QLabel("XY")

        self.text_input = QLineEdit()
        self.width_input = QLineEdit()
        self.XY_input.append(QLineEdit())

        self.setupVboxColumn1 = QVBoxLayout()
        self.setupVboxColumn2 = QVBoxLayout()
        setupBox = QHBoxLayout()

        self.setupVboxColumn1.addWidget(textLabel)
        self.setupVboxColumn1.addWidget(magLabel)
        self.setupVboxColumn1.addWidget(XYLabel)

        self.setupVboxColumn2.addWidget(self.text_input)
        self.setupVboxColumn2.addWidget(self.width_input)
        self.setupVboxColumn2.addWidget(self.XY_input[0])

        setupBox.addLayout(self.setupVboxColumn1)
        setupBox.addLayout(self.setupVboxColumn2)

        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        # hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(setupBox)
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        # vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Text Setup Window')
        self.setGeometry(300,300,500,200)
        self.show()


    def updateUI(self):
        self.text_input.setText(self._DesignParameter['_TEXT'])
        self.width_input.setText(str(self._DesignParameter['_Width']))
        self.XY_input[0].setText(str(self._DesignParameter['_XYCoordinates'][0][0])+','+str(self._DesignParameter['_XYCoordinates'][0][1]))

    def cancel_button_accepted(self):
        self.destroy()

    def on_buttonBox_accepted(self):
        try:
            for XY in self.XY_input:
                if not XY.text():
                    raise NotImplementedError
            else:
                    try:
                        X = int(XY.text().split(',')[0])
                        Y = int(XY.text().split(',')[1])
                        self._DesignParameter['_XYCoordinates']=[[X,Y]]
                    except:
                        self.warning = QMessageBox()
                        self.warning.setIcon(QMessageBox.Warning)
                        self.warning.setText("Invalid XY Coordinates")
                        self.warning.show()

            self._DesignParameter['_ElementName'] = self.text_input.text()
            if self._DesignParameter['_ElementName'] == '':
                raise NotImplementedError
            self._DesignParameter['_TEXT'] = self.text_input.text()
            self._DesignParameter['_Mag'] = float(self.width_input.text())
            self.send_TextDesign_signal.emit(self._DesignParameter)
            self.destroy()

            # if type(self._DesignParameter['_XWidth']) == str:
            #     self.warning = QMessageBox()
            #     self.warning.setText("test")
            #     self.warning.setIcon(QMessageBox.Warning)
            #     self.warning.show()
        except:
            self.send_Warning_signal.emit("Invalid Design Parameter Input")     #log message
            self.warning = QMessageBox()
            self.warning.setText("Invalid design parameter or Name")
            self.warning.setIcon(QMessageBox.Warning)
            self.warning.show()

    def DetermineCoordinateWithMouse(self, _MouseEvent):
        ##### When Click the point, adjust x,y locations #####
        self.XY_input[0].setText(str(_MouseEvent.scenePos().toPoint().x())+','+str(_MouseEvent.scenePos().toPoint().y()))

        self.visualItem.updateTraits(self._DesignParameter)
        self.send_TextSetup_signal.emit(self.visualItem)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_buttonBox_accepted()
            self.send_Destroy_signal.emit('txtw')
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.destroy()
            self.send_Destroy_signal.emit('txtw')

class _PinSetupWindow(QWidget):

    send_PinSetup_signal = pyqtSignal(VisualizationItem._VisualizationItem)
    send_PinDesign_signal = pyqtSignal(dict)
    send_Destroy_signal = pyqtSignal(str)
    send_Warning_signal = pyqtSignal(str)
    send_DestroyTmpVisual_signal = pyqtSignal(VisualizationItem._VisualizationItem)

    def __init__(self,PinElement=None):
        super().__init__()
        self.initUI()
        if PinElement == None:
            self.visualItem = VisualizationItem._VisualizationItem()
            self._DesignParameter = dict(
                _ElementName = None,
                _DesignParametertype = 8,
                _Layer = None,
                _XYCoordinates = [],
                _Presentation = None,
                _Reflect = None,
                _Mag = None,
                _Angle = None,
                _TEXT = None
                )
        else:
            self._DesignParameter = PinElement._ItemTraits
            self.updateUI()


    def initUI(self):
        okButton = QPushButton("OK",self)
        cancelButton = QPushButton("Cancel",self)

        okButton.clicked.connect(self.on_buttonBox_accepted)
        cancelButton.clicked.connect(self.cancel_button_accepted)

        self.layer = None
        self.text = None
        self.mag = None
        self.XY_input = []

        layerLabel = QLabel("Layer")
        textLabel = QLabel("Text")
        magLabel = QLabel("Width")
        XYLabel = QLabel("XY")

        self.layer_input = QComboBox()
        self.text_input = QLineEdit()
        self.width_input = QLineEdit()
        self.XY_input.append(QLineEdit())

        _Layer = LayerReader._LayerMapping
        for LayerName in _Layer:
            if _Layer[LayerName][1] != None:       ## Layer is pin
                if 'PIN' in LayerName:
                    self.layer_input.addItem(LayerName)

        self.setupVboxColumn1 = QVBoxLayout()
        self.setupVboxColumn2 = QVBoxLayout()
        setupBox = QHBoxLayout()

        self.setupVboxColumn1.addWidget(layerLabel)
        self.setupVboxColumn1.addWidget(textLabel)
        self.setupVboxColumn1.addWidget(magLabel)
        self.setupVboxColumn1.addWidget(XYLabel)

        self.setupVboxColumn2.addWidget(self.layer_input)
        self.setupVboxColumn2.addWidget(self.text_input)
        self.setupVboxColumn2.addWidget(self.width_input)
        self.setupVboxColumn2.addWidget(self.XY_input[0])

        setupBox.addLayout(self.setupVboxColumn1)
        setupBox.addLayout(self.setupVboxColumn2)

        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        # hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(setupBox)
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        # vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Text Setup Window')
        self.setGeometry(300,300,500,200)
        self.show()


    def updateUI(self):
        self.text_input.setText(self._DesignParameter['_TEXT'])
        self.width_input.setText(str(self._DesignParameter['_Width']))
        self.XY_input[0].setText(str(self._DesignParameter['_XYCoordinates'][0][0])+','+str(self._DesignParameter['_XYCoordinates'][0][1]))

    def cancel_button_accepted(self):
        self.destroy()

    def on_buttonBox_accepted(self):
        for XY in self.XY_input:
            if not XY.text():
                break
            else:
                try:
                    X = int(XY.text().split(',')[0])
                    Y = int(XY.text().split(',')[1])
                    self._DesignParameter['_XYCoordinates']=[[X,Y]]
                except:
                    self.warning = QMessageBox()
                    self.warning.setIcon(QMessageBox.Warning)
                    self.warning.setText("Invalid XY Coordinates")

        try:
            self._DesignParameter['_ElementName'] = self.text_input.text()
            if self._DesignParameter['_ElementName'] == '':
                raise NotImplementedError
            self._DesignParameter['_TEXT'] = self.text_input.text()
            self._DesignParameter['_Mag'] = float(self.width_input.text())
            self._DesignParameter['_Layer'] = self.layer_input.currentText()
            self.send_PinDesign_signal.emit(self._DesignParameter)
            self.destroy()

            # if type(self._DesignParameter['_XWidth']) == str:
            #     self.warning = QMessageBox()
            #     self.warning.setText("test")
            #     self.warning.setIcon(QMessageBox.Warning)
            #     self.warning.show()
        except:
            self.send_Warning_signal.emit("Invalid Design Parameter Input")     #log message
            self.warning = QMessageBox()
            self.warning.setText("Invalid design parameter or Name")
            self.warning.setIcon(QMessageBox.Warning)
            self.warning.show()

    def DetermineCoordinateWithMouse(self, _MouseEvent):
        ##### When Click the point, adjust x,y locations #####
        self.XY_input[0].setText(str(_MouseEvent.scenePos().toPoint().x())+','+str(_MouseEvent.scenePos().toPoint().y()))

        self.visualItem.updateTraits(self._DesignParameter)
        self.send_PinSetup_signal.emit(self.visualItem)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_buttonBox_accepted()
            self.send_Destroy_signal.emit('pinw')
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.destroy()
            self.send_Destroy_signal.emit('pinw')

class _ConstraintSetupWindow(QWidget):

    send_DesignConstraint_signal = pyqtSignal(dict)

    def __init__(self,_ParseTree = None):
        super().__init__()
        self.initUI()
        if _ParseTree == None:
            self._ParseTree = dict()
        else:
            self._ParseTree = _ParseTree
            self.updateUIvalue()
    def initUI(self):
        self.type_input = QComboBox()
        comboItemList = ["pyCode","scriptDefine","libImport","classDefine","classCall","functionDefine","functionCall","argument","statement","forLoop","condition","whileLoop","ifControl","ifLogic","logic","logicOp","expression","op","variableDefine","variableCall","variable",\
                         "dictionaryUpdate","dictionaryDefine","dictionaryCall","dictionaryElement","listDefine","listCall","number","string"]
        self.type_input.addItems(comboItemList)
        self.type_input.currentIndexChanged.connect(self.updateUI)


        okButton = QPushButton("OK",self)
        cancelButton = QPushButton("Cancel",self)

        okButton.clicked.connect(self.on_buttonBox_accepted)
        cancelButton.clicked.connect(self.cancel_button_accepted)


        self.setupVboxColumn1 = QVBoxLayout()
        self.setupVboxColumn2 = QVBoxLayout()
        setupBox = QHBoxLayout()


        self.setupVboxColumn1.addWidget(QLabel("Type"))

        self.setupVboxColumn2.addWidget(self.type_input)


        setupBox.addLayout(self.setupVboxColumn1)
        setupBox.addLayout(self.setupVboxColumn2)

        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(setupBox)
        vbox.addStretch(3)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setWindowTitle('Constarint Setup Window')
        self.setGeometry(300,300,500,500)
        self.updateUI()
        self.show()
    def updateUI(self):
        while self.setupVboxColumn1.count() != 1:
            tmp = self.setupVboxColumn1.takeAt(1).widget()
            tmp.setParent(None)
            del tmp
            tmp = self.setupVboxColumn2.takeAt(1).widget()
            tmp.setParent(None)
            self.setupVboxColumn2.removeWidget(tmp)
            del tmp

        if self.type_input.currentText() == "pyCode":
            strList = ["_name","_file"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "scriptDefine":
            strList = ["_name","_libImport","_variableDefine","_classDefine","_functionDefine","_statements","_pyCode"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "libImport":
            strList = ["_name","_pyCode"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "classDefine":
            strList = ["_name","_inheritance","_statements","_functionDefine","_pyCode"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "classCall":
            strList = ["_name","_arguments"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "functionDefine":
            strList = ["_name","_arguments","_statements","_pyCode"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "functionCall":
            strList = ["_name","_arguments"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "argument":
            strList = ["_name","_value"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "statement":
            strList = ["_pyCode","_forLoop","_ifControl","_whileLoop","_expression","_dictionaryDefine","_variableDefine","_returnValueDefine"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "forLoop":
            strList = ["_index","_condition","_statements"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "condition":
            strList = ["_list"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "whileLoop":
            strList = ["_logic","_statements"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "ifControl":
            strList = ["_ifLogic","_elifLogic","_elseLogic"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "ifLogic":
            strList = ["_ifLogic","_elifLogic","_statements"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "logic":
            strList = ["_leftBracket","_rightBracket","_logic","_logicOp"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "logicOp":
            strList = ["_logicOp"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "expression":
            strList = ["_leftBracket","_rightBracket","_expression","_op","_logic","_classCall","_functionCall","_dictionaryCall","_dictionaryDefine","_listCall","_listDefine","_variableCall","_number","_string"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "op":
            strList = ["op"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "variableDefine":
            strList = ["_variable","_expression"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "variableCall":
            strList = ["_variable"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "variable":
            strList = ["_name"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "dictionaryUpdate":
            strList = ["_variable","_dictionaryElements"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "dictionaryDefine":
            strList = ["_dictionaryElements"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "dictionaryCall":
            strList = ["_variable","_key"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "dictionaryElement":
            strList = ["_dictionaryElement"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "listDefine":
            strList = ["_var","_rangeFunction","_forLoopInList"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "listCall":
            strList = ["_variable","_index"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "number":
            strList = ["_value"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "string":
            strList = ["_string"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
    def addQLabel(self,strList):
        for str in strList:
            self.setupVboxColumn1.addWidget(QLabel(str))
    def addQLine(self,num):
        for i in range(0,num):
            self.setupVboxColumn2.addWidget(QLineEdit())
    def cancel_button_accepted(self):
        self.destroy()
    def on_buttonBox_accepted(self):
        for i in range(0,self.setupVboxColumn1.count()):
            ttmp = self.setupVboxColumn2.itemAt(i).widget()
            key = self.setupVboxColumn1.itemAt(i).widget().text()
            try:
                value = self.setupVboxColumn2.itemAt(i).widget().text()
            except:
                value = self.setupVboxColumn2.itemAt(i).widget().currentText()

            if value == "":
                value = []


            self._ParseTree[key] = value
        self.send_DesignConstraint_signal.emit(self._ParseTree)
        self.destroy()
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_buttonBox_accepted()
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.destroy()
    def updateUIvalue(self):
        try:
            type = self._ParseTree["Type"]
            typeIndex = self.type_input.findText(type)
            if typeIndex != -1:
                self.type_input.setCurrentIndex(typeIndex)
            else:
                print("ERROR")
                return
            for key in self._ParseTree:
                for i in range(1,self.setupVboxColumn1.count()):
                    labelFieldName = self.setupVboxColumn1.itemAt(i).widget().text()
                    if labelFieldName == key:
                        self.setupVboxColumn2.itemAt(i).widget().setText(self._ParseTree[key])
                        break
        except:
            print("updateFail")

class _ConstraintSetupWindowSTMT(QWidget):

    send_STMT_signal = pyqtSignal(dict)

    def __init__(self,_STMT = None):
        super().__init__()
        self.initUI()
        if _STMT == None:                      #_ParseTree[0] = "Type", _ParseTree[1] = "PyCode" or dict(AST) , ... ParseTree[n] = dict(AST)
            #self._ParseTree = ["TypeNull"]
            self._STMT = dict()
        else:
            #self._ParseTree = _ParseTree
            self._STMT = _STMT
            self.updateUIvalue()
    def initUI(self):
        self.type_input = QComboBox()
        #comboItemList = ["pyCode","scriptDefine","libImport","classDefine","classCall","functionDefine","functionCall","argument","statement","forLoop","condition","whileLoop","ifControl","ifLogic","logic","logicOp","expression","op","variableDefine","variableCall","variable",\
        #                 "dictionaryUpdate","dictionaryDefine","dictionaryCall","dictionaryElement","listDefine","listCall","number","string"]
        #comboItemList = ["pyCode","If","While","For","Try","With","FunctionDef","ClassDef"]
        comboItemList = ASTmodule.stmtList
        self.type_input.addItems(comboItemList)
        self.type_input.currentIndexChanged.connect(self.updateUI)


        okButton = QPushButton("OK",self)
        cancelButton = QPushButton("Cancel",self)

        okButton.clicked.connect(self.on_buttonBox_accepted)
        cancelButton.clicked.connect(self.cancel_button_accepted)


        self.setupVboxColumn1 = QVBoxLayout()
        self.setupVboxColumn2 = QVBoxLayout()
        setupBox = QHBoxLayout()


        self.setupVboxColumn1.addWidget(QLabel("_type"))

        self.setupVboxColumn2.addWidget(self.type_input)


        setupBox.addLayout(self.setupVboxColumn1)
        setupBox.addLayout(self.setupVboxColumn2)

        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(setupBox)
        vbox.addStretch(3)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setWindowTitle('Constarint Setup Window')
        self.setGeometry(300,300,500,500)
        self.updateUI()
        self.show()
    def updateUI(self):
        while self.setupVboxColumn1.count() != 1:
            tmp = self.setupVboxColumn1.takeAt(1).widget()
            tmp.setParent(None)
            del tmp
            tmp = self.setupVboxColumn2.takeAt(1).widget()
            tmp.setParent(None)
            self.setupVboxColumn2.removeWidget(tmp)
            del tmp




        if self.type_input.currentText() == "pyCode":
            strList = ["_pyCode"]
            self.addQLabel(strList)
            self.addQLine(len(strList))

        elif self.type_input.currentText() == "scriptDefine":
            strList = ["_name","_libImport","_variableDefine","_classDefine","_functionDefine","_statements","_pyCode"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "libImport":
            strList = ["_name","_pyCode"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "classDefine":
            strList = ["_name","_inheritance","_statements","_functionDefine","_pyCode"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "classCall":
            strList = ["_name","_arguments"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "functionDefine":
            strList = ["_name","_arguments","_statements","_pyCode"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "functionCall":
            strList = ["_name","_arguments"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "argument":
            strList = ["_name","_value"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "statement":
            strList = ["_pyCode","_forLoop","_ifControl","_whileLoop","_expression","_dictionaryDefine","_variableDefine","_returnValueDefine"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "forLoop":
            strList = ["_index","_condition","_statements"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "condition":
            strList = ["_list"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "whileLoop":
            strList = ["_logic","_statements"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "ifControl":
            strList = ["_ifLogic","_elifLogic","_elseLogic"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "ifLogic":
            strList = ["_ifLogic","_elifLogic","_statements"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "logic":
            strList = ["_leftBracket","_rightBracket","_logic","_logicOp"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "logicOp":
            strList = ["_logicOp"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "expression":
            strList = ["_leftBracket","_rightBracket","_expression","_op","_logic","_classCall","_functionCall","_dictionaryCall","_dictionaryDefine","_listCall","_listDefine","_variableCall","_number","_string"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "op":
            strList = ["op"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "variableDefine":
            strList = ["_variable","_expression"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "variableCall":
            strList = ["_variable"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "variable":
            strList = ["_name"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "dictionaryUpdate":
            strList = ["_variable","_dictionaryElements"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "dictionaryDefine":
            strList = ["_dictionaryElements"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "dictionaryCall":
            strList = ["_variable","_key"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "dictionaryElement":
            strList = ["_dictionaryElement"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "listDefine":
            strList = ["_var","_rangeFunction","_forLoopInList"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "listCall":
            strList = ["_variable","_index"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "number":
            strList = ["_value"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "string":
            strList = ["_string"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
    def addQLabel(self,strList):
        for str in strList:
            self.setupVboxColumn1.addWidget(QLabel(str))
    def addQLine(self,num):
        for i in range(0,num):
            self.setupVboxColumn2.addWidget(QLineEdit())
    def cancel_button_accepted(self):
        self.destroy()
    def on_buttonBox_accepted(self):
        stmtType = self.type_input.currentText()
        stmt = dict()
        stmt['_type'] = stmtType

        for i in range(0,self.setupVboxColumn1.count()):
            key = self.setupVboxColumn1.itemAt(i).widget().text()
            try:
                value = self.setupVboxColumn2.itemAt(i).widget().text()
            except:
                value = self.setupVboxColumn2.itemAt(i).widget().currentText()

            if value == "":
                value = []
        #self._ParseTree[1][stmtType][key] = value
        stmt[key] = value
        self._STMT = stmt
        self.send_STMT_signal.emit(self._STMT)
        self.destroy()
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_buttonBox_accepted()
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.destroy()
    def updateUIvalue(self):
        try:
            type = self._ParseTree['_type']
            typeIndex = self.type_input.findText(type)
            if typeIndex != -1:
                self.type_input.setCurrentIndex(typeIndex)
            else:
                print("ERROR")
                return
            for key in self._ParseTree:
                for i in range(1,self.setupVboxColumn1.count()):
                    labelFieldName = self.setupVboxColumn1.itemAt(i).widget().text()
                    if labelFieldName == key:
                        self.setupVboxColumn2.itemAt(i).widget().setText(self._ParseTree[key])
                        break
        except:
            print("updateFail")

class _ConstraintSetupWindowAST(QWidget):

    send_STMT_signal = pyqtSignal(dict)
    send_AST_signal = pyqtSignal("PyQt_PyObject")
    send_destroy_signal = pyqtSignal(str)

    def __init__(self,_AST = None, _STMT = None, _ASTapi = None):
        super().__init__()
        if _ASTapi == None:
            self._ASTapi = ASTmodule._Custom_AST_API()
        else:
            self._ASTapi = _ASTapi

        self.initUI()

        if _AST == None:        #This is for editing created AST.       AST --> STMT
            self._AST = None
        else:
            self._AST = _AST
            #self.updateUIvalue()       #AST to STMT convert fuunction before excute updateUIvalue

        if _STMT == None:
            self._STMT = []
        else:
            self._STMT = _STMT
            self.updateUIvalue()



    def initUI(self):
        self.type_input = QComboBox()
        comboItemList = self._ASTapi.stmtList
        self.type_input.addItems(comboItemList)
        self.type_input.currentIndexChanged.connect(self.updateUI)


        okButton = QPushButton("OK",self)
        cancelButton = QPushButton("Cancel",self)

        okButton.clicked.connect(self.on_buttonBox_accepted)
        cancelButton.clicked.connect(self.cancel_button_accepted)

        self.setupVboxColumn1 = QVBoxLayout()
        self.setupVboxColumn2 = QVBoxLayout()
        setupBox = QHBoxLayout()


        self.setupVboxColumn1.addWidget(QLabel("_type"))

        self.setupVboxColumn2.addWidget(self.type_input)


        setupBox.addLayout(self.setupVboxColumn1)
        setupBox.addLayout(self.setupVboxColumn2)

        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(setupBox)
        vbox.addStretch(3)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setWindowTitle('Constarint Setup Window')
        self.setGeometry(300,300,500,500)
        self.updateUI()
        self.show()
    def updateUI(self):
        while self.setupVboxColumn1.count() != 1:               # original typed content delete
            tmp = self.setupVboxColumn1.takeAt(1).widget()
            tmp.setParent(None)
            del tmp
            tmp = self.setupVboxColumn2.takeAt(1).widget()
            tmp.setParent(None)
            self.setupVboxColumn2.removeWidget(tmp)
            del tmp

        currentClassName = self.type_input.currentText() # like: If, While, Number ,...
        tmpObj = self._ASTapi._createASTwithName(currentClassName)
        strList = list(tmpObj._fields)
        self.addQLabel(strList)
        self.addQLine(len(strList))


        if self.type_input.currentText() == "pyCode":
            strList = ["_pyCode"]
            self.addQLabel(strList)
            self.addQLine(len(strList))

    def addQLabel(self,strList):
        for str in strList:
            self.setupVboxColumn1.addWidget(QLabel(str))
    def addQLine(self,num):
        for i in range(0,num):
            self.setupVboxColumn2.addWidget(QLineEdit())
    def on_buttonBox_accepted(self):
        _ASTtype = self.type_input.currentText()
        _ASTobj = self._ASTapi._createASTwithName(_ASTtype)
        for i in range(0,self.setupVboxColumn1.count()):
            key = self.setupVboxColumn1.itemAt(i).widget().text()
            try:
                value = self.setupVboxColumn2.itemAt(i).widget().text()
            except:
                value = self.setupVboxColumn2.itemAt(i).widget().currentText()
            try:
                _ASTobj.__dict__[key] = value
            except:
                print("Value Initialization Fail")

        self.send_AST_signal.emit(_ASTobj)
        self.destroy()

    def cancel_button_accepted(self):
        self.destroy()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_buttonBox_accepted()
            self.send_destroy_signal.emit('cw')
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.destroy()
            self.send_destroy_signal.emit('cw')
    def updateUIvalue(self):
        try:
            type = self._ParseTree['_type']
            typeIndex = self.type_input.findText(type)
            if typeIndex != -1:
                self.type_input.setCurrentIndex(typeIndex)
            else:
                print("ERROR")
                return
            for key in self._ParseTree:
                for i in range(1,self.setupVboxColumn1.count()):
                    labelFieldName = self.setupVboxColumn1.itemAt(i).widget().text()
                    if labelFieldName == key:
                        self.setupVboxColumn2.itemAt(i).widget().setText(self._ParseTree[key])
                        break
        except:
            print("updateFail")

class _ConstraintSetupWindowCUSTOM(QWidget):

    send_STMT_signal = pyqtSignal(dict)
    send_CUSTOM_signal = pyqtSignal("PyQt_PyObject")
    send_Destroy_signal = pyqtSignal(str)

    def __init__(self,_AST = None, _STMT = None, _ASTapi = None):
        super().__init__()
        if _ASTapi == None:
            self._ASTapi = ASTmodule._Custom_AST_API()
        else:
            self._ASTapi = _ASTapi

        self.initUI()

        if _AST == None:        #This is for editing created AST.       AST --> STMT
            self._AST = None
        else:
            self._AST = _AST
            #self.updateUIvalue()       #AST to STMT convert fuunction before excute updateUIvalue

        if _STMT == None:
            self._STMT = []
        else:
            self._STMT = _STMT
            self.updateUIvalue()



    def initUI(self):
        self.type_input = QComboBox()
        comboItemList = self._ASTapi.custom_stmt_list
        self.type_input.addItems(comboItemList)
        self.type_input.currentIndexChanged.connect(self.updateUI)


        okButton = QPushButton("OK",self)
        cancelButton = QPushButton("Cancel",self)

        okButton.clicked.connect(self.on_buttonBox_accepted)
        cancelButton.clicked.connect(self.cancel_button_accepted)


        self.setupVboxColumn1 = QVBoxLayout()
        self.setupVboxColumn2 = QVBoxLayout()
        setupBox = QHBoxLayout()


        self.setupVboxColumn1.addWidget(QLabel("_type"))

        self.setupVboxColumn2.addWidget(self.type_input)


        setupBox.addLayout(self.setupVboxColumn1)
        setupBox.addLayout(self.setupVboxColumn2)

        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(setupBox)
        vbox.addStretch(3)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setWindowTitle('Constarint Setup Window')
        self.setGeometry(300,300,500,500)
        self.updateUI()
        self.show()
    def updateUI(self):
        while self.setupVboxColumn1.count() != 1:               # original typed content delete
            tmp = self.setupVboxColumn1.takeAt(1).widget()
            tmp.setParent(None)
            del tmp
            tmp = self.setupVboxColumn2.takeAt(1).widget()
            tmp.setParent(None)
            self.setupVboxColumn2.removeWidget(tmp)
            del tmp

        currentClassName = self.type_input.currentText() # like: If, While, Number ,...
        tmpObj = self._ASTapi._create_custom_ast_with_name(currentClassName)
        strList = list(tmpObj._fields)
        self.addQLabel(strList)
        self.addQLine(len(strList))


        if self.type_input.currentText() == "pyCode":
            strList = ["_pyCode"]
            self.addQLabel(strList)
            self.addQLine(len(strList))

    def addQLabel(self,strList):
        for str in strList:
            self.setupVboxColumn1.addWidget(QLabel(str))
    def addQLine(self,num):
        for i in range(0,num):
            self.setupVboxColumn2.addWidget(QLineEdit())
    def cancel_button_accepted(self):
        self.destroy()
    def on_buttonBox_accepted(self):
        _ASTtype = self.type_input.currentText()
        _ASTobj = self._ASTapi._create_custom_ast_with_name(_ASTtype)
        for i in range(0,self.setupVboxColumn1.count()):
            key = self.setupVboxColumn1.itemAt(i).widget().text()
            if key == 'XY':
                try:
                    value = self.setupVboxColumn2.itemAt(i).widget().text()
                    xy_split = value.split(',')
                    _ASTobj.__dict__[key] = [[int(xy_split[0]),int(xy_split[1])]]
                except:
                    self.warning = QMessageBox()
                    self.warning.setText("Invalid Parameter Input")
                    self.warning.show()
                    return
            else:
                try:
                    value = self.setupVboxColumn2.itemAt(i).widget().text()
                except:
                    value = self.setupVboxColumn2.itemAt(i).widget().currentText()
                try:
                    _ASTobj.__dict__[key] = value
                except:
                    print("Value Initialization Fail")

        self.send_CUSTOM_signal.emit(_ASTobj)
        self.destroy()
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_buttonBox_accepted()
            self.send_Destroy_signal.emit('cw')
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.destroy()
            self.send_Destroy_signal.emit('cw')
    def updateUIvalue(self):
        try:
            type = self._ParseTree['_type']
            typeIndex = self.type_input.findText(type)
            if typeIndex != -1:
                self.type_input.setCurrentIndex(typeIndex)
            else:
                print("ERROR")
                return
            for key in self._ParseTree:
                for i in range(1,self.setupVboxColumn1.count()):
                    labelFieldName = self.setupVboxColumn1.itemAt(i).widget().text()
                    if labelFieldName == key:
                        self.setupVboxColumn2.itemAt(i).widget().setText(self._ParseTree[key])
                        break
        except:
            print("updateFail")

class _VariableSetupWindowCUSTOM(QWidget):

    send_STMT_signal = pyqtSignal(dict)
    send_CUSTOM_signal = pyqtSignal("PyQt_PyObject")
    send_Destroy_signal = pyqtSignal(str)

    def __init__(self,_AST = None, _STMT = None, _ASTapi = None):
        super().__init__()
        if _ASTapi == None:
            self._ASTapi = ASTmodule._Custom_AST_API()
        else:
            self._ASTapi = _ASTapi

        self.initUI()

        if _AST == None:        #This is for editing created AST.       AST --> STMT
            self._AST = None
        else:
            self._AST = _AST
            #self.updateUIvalue()       #AST to STMT convert fuunction before excute updateUIvalue

        if _STMT == None:
            self._STMT = []
        else:
            self._STMT = _STMT
            self.updateUIvalue()



    def initUI(self):
        self.type_input = QComboBox()
        comboItemList = self._ASTapi.custom_variable_list
        self.type_input.addItems(comboItemList)
        self.type_input.currentIndexChanged.connect(self.updateUI)


        okButton = QPushButton("OK",self)
        cancelButton = QPushButton("Cancel",self)

        okButton.clicked.connect(self.on_buttonBox_accepted)
        cancelButton.clicked.connect(self.cancel_button_accepted)


        self.setupVboxColumn1 = QVBoxLayout()
        self.setupVboxColumn2 = QVBoxLayout()
        setupBox = QHBoxLayout()


        self.setupVboxColumn1.addWidget(QLabel("_type"))

        self.setupVboxColumn2.addWidget(self.type_input)


        setupBox.addLayout(self.setupVboxColumn1)
        setupBox.addLayout(self.setupVboxColumn2)

        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(setupBox)
        vbox.addStretch(3)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setWindowTitle('Constraint Setup Window')
        self.setGeometry(300,300,500,500)
        self.updateUI()
        self.show()
    def updateUI(self):
        while self.setupVboxColumn1.count() != 1:               # original typed content delete
            tmp = self.setupVboxColumn1.takeAt(1).widget()
            tmp.setParent(None)
            del tmp
            tmp = self.setupVboxColumn2.takeAt(1).widget()
            tmp.setParent(None)
            self.setupVboxColumn2.removeWidget(tmp)
            del tmp

        currentClassName = self.type_input.currentText() # like: If, While, Number ,...
        tmpObj = self._ASTapi._create_variable_ast_with_name(currentClassName)
        strList = list(tmpObj._fields)
        self.addQLabel(strList)
        self.addQLine(len(strList))


        if self.type_input.currentText() == "pyCode":
            strList = ["_pyCode"]
            self.addQLabel(strList)
            self.addQLine(len(strList))

    def addQLabel(self,strList):
        for str in strList:
            self.setupVboxColumn1.addWidget(QLabel(str))
    def addQLine(self,num):
        for i in range(0,num):
            self.setupVboxColumn2.addWidget(QLineEdit())
    def cancel_button_accepted(self):
        self.destroy()
    def on_buttonBox_accepted(self):
        _ASTtype = self.type_input.currentText()
        _ASTobj = self._ASTapi._create_variable_ast_with_name(_ASTtype)
        for i in range(0,self.setupVboxColumn1.count()):
            key = self.setupVboxColumn1.itemAt(i).widget().text()
            if key == 'XY':
                value = self.setupVboxColumn2.itemAt(i).widget().text()
                xy_split = value.split(',')
                _ASTobj.__dict__[key] = [[int(xy_split[0]),int(xy_split[1])]]
            else:
                try:
                    value = self.setupVboxColumn2.itemAt(i).widget().text()
                except:
                    value = self.setupVboxColumn2.itemAt(i).widget().currentText()
                try:
                    _ASTobj.__dict__[key] = value
                except:
                    print("Value Initialization Fail")

        self.send_CUSTOM_signal.emit(_ASTobj)
        self.destroy()
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_buttonBox_accepted()
            self.send_Destroy_signal.emit('cw')
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.destroy()
            self.send_Destroy_signal.emit('cw')
    def updateUIvalue(self):
        try:
            type = self._ParseTree['_type']
            typeIndex = self.type_input.findText(type)
            if typeIndex != -1:
                self.type_input.setCurrentIndex(typeIndex)
            else:
                print("ERROR")
                return
            for key in self._ParseTree:
                for i in range(1,self.setupVboxColumn1.count()):
                    labelFieldName = self.setupVboxColumn1.itemAt(i).widget().text()
                    if labelFieldName == key:
                        self.setupVboxColumn2.itemAt(i).widget().setText(self._ParseTree[key])
                        break
        except:
            print("updateFail")

class _ConstraintSetupWindowPyCode(QWidget):

    send_PyCode_signal = pyqtSignal(str)
    send_Destroy_signal = pyqtSignal(str)

    def __init__(self,_ParseTree = None):
        super().__init__()
        self.initUI()
        if _ParseTree == None:                      #_ParseTree[0] = "Type", _ParseTree[1] = "PyCode" or dict(AST) , ... ParseTree[n] = dict(AST)
            self._ParseTree = ["TypeNull"]
        else:
            self._ParseTree = _ParseTree
            self.updateUIvalue()
    def initUI(self):
        self.type_input = QComboBox()
        #comboItemList = ["pyCode","scriptDefine","libImport","classDefine","classCall","functionDefine","functionCall","argument","statement","forLoop","condition","whileLoop","ifControl","ifLogic","logic","logicOp","expression","op","variableDefine","variableCall","variable",\
        #                 "dictionaryUpdate","dictionaryDefine","dictionaryCall","dictionaryElement","listDefine","listCall","number","string"]
        #comboItemList = ["pyCode","If","While","For","Try","With","FunctionDef","ClassDef"]
        comboItemList = ['pyCode']
        #comboItemList = comboItemList + ASTmodule.stmtList
        self.type_input.addItems(comboItemList)
        self.type_input.currentIndexChanged.connect(self.updateUI)


        okButton = QPushButton("OK",self)
        cancelButton = QPushButton("Cancel",self)

        okButton.clicked.connect(self.on_buttonBox_accepted)
        cancelButton.clicked.connect(self.cancel_button_accepted)


        self.setupVboxColumn1 = QVBoxLayout()
        self.setupVboxColumn2 = QVBoxLayout()
        setupBox = QHBoxLayout()


        self.setupVboxColumn1.addWidget(QLabel("Type"))

        self.setupVboxColumn2.addWidget(self.type_input)


        setupBox.addLayout(self.setupVboxColumn1)
        setupBox.addLayout(self.setupVboxColumn2)

        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(setupBox)
        vbox.addStretch(3)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setWindowTitle('Constarint Setup Window')
        self.setGeometry(300,300,500,500)
        self.updateUI()
        self.show()
    def updateUI(self):
        while self.setupVboxColumn1.count() != 1:
            tmp = self.setupVboxColumn1.takeAt(1).widget()
            tmp.setParent(None)
            del tmp
            tmp = self.setupVboxColumn2.takeAt(1).widget()
            tmp.setParent(None)
            self.setupVboxColumn2.removeWidget(tmp)
            del tmp




        if self.type_input.currentText() == "pyCode":
            strList = ["_pyCode"]
            self.addQLabel(strList)
            self.addQLine(len(strList))

        elif self.type_input.currentText() == "scriptDefine":
            strList = ["_name","_libImport","_variableDefine","_classDefine","_functionDefine","_statements","_pyCode"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "libImport":
            strList = ["_name","_pyCode"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "classDefine":
            strList = ["_name","_inheritance","_statements","_functionDefine","_pyCode"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "classCall":
            strList = ["_name","_arguments"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "functionDefine":
            strList = ["_name","_arguments","_statements","_pyCode"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "functionCall":
            strList = ["_name","_arguments"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "argument":
            strList = ["_name","_value"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "statement":
            strList = ["_pyCode","_forLoop","_ifControl","_whileLoop","_expression","_dictionaryDefine","_variableDefine","_returnValueDefine"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "forLoop":
            strList = ["_index","_condition","_statements"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "condition":
            strList = ["_list"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "whileLoop":
            strList = ["_logic","_statements"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "ifControl":
            strList = ["_ifLogic","_elifLogic","_elseLogic"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "ifLogic":
            strList = ["_ifLogic","_elifLogic","_statements"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "logic":
            strList = ["_leftBracket","_rightBracket","_logic","_logicOp"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "logicOp":
            strList = ["_logicOp"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "expression":
            strList = ["_leftBracket","_rightBracket","_expression","_op","_logic","_classCall","_functionCall","_dictionaryCall","_dictionaryDefine","_listCall","_listDefine","_variableCall","_number","_string"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "op":
            strList = ["op"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "variableDefine":
            strList = ["_variable","_expression"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "variableCall":
            strList = ["_variable"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "variable":
            strList = ["_name"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "dictionaryUpdate":
            strList = ["_variable","_dictionaryElements"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "dictionaryDefine":
            strList = ["_dictionaryElements"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "dictionaryCall":
            strList = ["_variable","_key"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "dictionaryElement":
            strList = ["_dictionaryElement"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "listDefine":
            strList = ["_var","_rangeFunction","_forLoopInList"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "listCall":
            strList = ["_variable","_index"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "number":
            strList = ["_value"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
        elif self.type_input.currentText() == "string":
            strList = ["_string"]
            self.addQLabel(strList)
            self.addQLine(len(strList))
    def addQLabel(self,strList):
        for str in strList:
            self.setupVboxColumn1.addWidget(QLabel(str))
    def addQLine(self,num):
        for i in range(0,num):
            self.setupVboxColumn2.addWidget(QLineEdit())
    def cancel_button_accepted(self):
        self.destroy()
    def on_buttonBox_accepted(self):
        if self.type_input.currentText() == "pyCode":
            try:
                value = self.setupVboxColumn2.itemAt(1).widget().text()
            except:
                value = self.setupVboxColumn2.itemAt(1).widget().currentText()
            self._ParseTree[0] = "pyCode"
            self._ParseTree.append(value)
        self.send_PyCode_signal.emit(value)
        self.destroy()
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_buttonBox_accepted()
            self.send_Destroy_signal.emit('cw')
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.destroy()
            self.send_Destroy_signal.emit('cw')
    def updateUIvalue(self):
        try:
            type = self._ParseTree["Type"]
            typeIndex = self.type_input.findText(type)
            if typeIndex != -1:
                self.type_input.setCurrentIndex(typeIndex)
            else:
                print("ERROR")
                return
            for key in self._ParseTree:
                for i in range(1,self.setupVboxColumn1.count()):
                    labelFieldName = self.setupVboxColumn1.itemAt(i).widget().text()
                    if labelFieldName == key:
                        self.setupVboxColumn2.itemAt(i).widget().setText(self._ParseTree[key])
                        break
        except:
            print("updateFail")

class _SelectedDesignListWidget(QListWidget):

    send_UpdateDesignParameter_signal = pyqtSignal(dict)
    send_UpdateDesignAST_signal = pyqtSignal("PyQt_PyObject")
    send_parameterIDList_signal = pyqtSignal(list,int)
    send_deleteItem_signal = pyqtSignal(str)
    # send_Up

    def __init__(self):
        super().__init__()
        self.itemDict = dict()
        self.idDict = dict()
        self.currentItemChanged.connect(self.UpdateSelectedItem)
        self.itemDoubleClicked.connect(self.ModifyingDesign)


    def UpdateCustomItem(self,_items):                  #Add Selected Visualization Items on List
        i=0
        j=0
        k=0

        # for storedItem in self.itemDict:
        #     self.itemDict[storedItem].setSelected(False)

        self.blockSignals(True)
        self.clear()
        self.itemDict.clear()
        self.idDict.clear()
        self.blockSignals(False)


        for item in _items:
            if type(item) == VisualizationItem._VisualizationItem:
                tmpName = item._ItemTraits['_ElementName']
                if tmpName == None:
                    continue
                # tmpName = item._ElementName
                self.itemDict[tmpName] = item
                self.idDict[tmpName] = item._ItemTraits['_id']
                item.setSelected(True)
                # print(item.isSelected())

                if not self.findItems(tmpName, Qt.MatchExactly):  # Check whether it is empty or not
                    self.addItem(QListWidgetItem(tmpName))

            else:
                continue
            # if type(item) == VisualizationItem._RectBlock:
            #     continue
            # elif type(item) == QGraphicsPathItem:
            #     continue
            # elif item._clickFlag == False:
            #     continue


    def UpdateSelectedItem(self,current,previous):
        # if previous is None:
        #     for storedItem in self.itemDict:
        #         self.itemDict[storedItem].setSelected(False)
        # else:
        #     nameOfPrevious = previous.text()
        #     self.itemDict[nameOfPrevious].setSelected(False)

        nameOfCurrent = current.text()
        self.itemDict[nameOfCurrent].setSelected(True)


    def DeleteCustomItem(self,item):
        pass

    def ModifyingDesign(self,item):
        modifyingObject = self.itemDict[item.text()]

        if modifyingObject._ItemTraits['_DesignParametertype'] == 1:
            self.bw = _BoundarySetupWindow(modifyingObject)
            self.bw.show()
            self.bw.send_BoundaryDesign_signal.connect(self.send_UpdateDesignParameter_signal)
        elif modifyingObject._ItemTraits['_DesignParametertype'] == 2:
            self.pw = _PathSetupWindow(modifyingObject)
            self.pw.show()
            self.pw.send_PathDesign_signal.connect(self.send_UpdateDesignParameter_signal)
            self.pw.send_Destroy_signal.connect(self.pw.close)
        elif modifyingObject._ItemTraits['_DesignParametertype'] == 3:
            self.sw = _LoadSRefWindow(modifyingObject)
            self.sw.show()
            self.sw.send_DesignConstraint_signal.connect(self.send_UpdateDesignAST_signal)
            self.sw.send_destroy_signal.connect(self.sw.close)
        elif modifyingObject._ItemTraits['_DesignParametertype'] == 8:
            if modifyingObject._ItemTraits['_Layer'] == 'text':
                self.txtw = _TextSetupWindow(modifyingObject)
                self.txtw.show()
                self.txtw.send_TextDesign_signal.connect(self.send_UpdateDesignParameter_signal)
                self.txtw.send_Destroy_signal.connect(self.txtw.close)
            else:
                self.pinw = _PinSetupWindow(modifyingObject)
                self.pinw.show()
                self.pinw.send_PinDesign_signal.connect(self.send_UpdateDesignParameter_signal)
                self.pinw.send_Destroy_signal.connect(self.pinw.close)

    def DeliveryItem(self):
        try:
            designParameter = self.itemDict[self.currentItem().text()]
            return designParameter
        except:
            print("Warning, DesignParameter is not selected")
        # return self.itemDict[]

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_D:
            print("variableDefine With DesignParameter")
            itemList = self.selectedItems()
            parameterIDList = list()
            for item in itemList:
                parameterIDList.append(self.idDict[item.text()])
            self.send_parameterIDList_signal.emit(parameterIDList,0)
        elif QKeyEvent.key() == Qt.Key_V:
            print("variable Call With DesignParameter")
            itemList = self.selectedItems()
            parameterIDList = list()
            for item in itemList:
                parameterIDList.append(self.idDict[item.text()])
            self.send_parameterIDList_signal.emit(parameterIDList,1)
        elif QKeyEvent.key() == Qt.Key_X:
            print("variable Call With DesignParameter")
            itemList = self.selectedItems()
            parameterIDList = list()
            for item in itemList:
                parameterIDList.append(self.idDict[item.text()])
            self.send_parameterIDList_signal.emit(parameterIDList,2)
        elif QKeyEvent.key() == Qt.Key_Y:
            print("variable Call With DesignParameter")
            itemList = self.selectedItems()
            parameterIDList = list()
            for item in itemList:
                parameterIDList.append(self.idDict[item.text()])
            self.send_parameterIDList_signal.emit(parameterIDList,3)
        elif QKeyEvent.key() == Qt.Key_C:
            print("variable Call With DesignParameter")
            itemList = self.selectedItems()
            parameterIDList = list()
            for item in itemList:
                parameterIDList.append(self.idDict[item.text()])
            self.send_parameterIDList_signal.emit(parameterIDList,4)
        elif QKeyEvent.key() == Qt.Key_Delete:
            deletionItems = self.selectedItems()
            for deleteItem in deletionItems:
                _ID = self.idDict[deleteItem.text()]
                self.send_deleteItem_signal.emit(_ID)

class _ConstraintTreeViewWidgetAST(QTreeView):

    send_UpdateDesignConstraint_signal = pyqtSignal(dict)
    send_SendDesignConstraint_signal = pyqtSignal(QTInterfaceWithAST.QtDesinConstraint)
    send_UpdateDesignConstraintID_signal = pyqtSignal(str,str)
    send_SendASTDict_signal = pyqtSignal(list)
    send_SendSTMT_signal = pyqtSignal(dict)
    send_SendID_signal = pyqtSignal(str)
    send_SendCopyConstraint_signal = pyqtSignal(QTInterfaceWithAST.QtDesinConstraint)
    send_RootDesignConstraint_signal = pyqtSignal(str)
    send_ReceiveDone_signal = pyqtSignal()
    send_RequestDesignConstraint_signal = pyqtSignal()
    send_RequestElementManger_signal = pyqtSignal()
    send_DataChanged_signal = pyqtSignal(str)
    # send_deleteID_signal = pyqtSignal(str)
    send_deleteConstraint_signal = pyqtSignal(str)

    originalKeyPress = QTreeView.keyPressEvent

    _ElementMangerFromQTobj = None

    def __init__(self,type):
        super().__init__()
        self._DesignConstraintFromQTobj = []
        self.initUI(type)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)
        self.itemToDesignConstraintDict = dict()
        self.itemToASTDict = dict()
        self.item_dict = dict()
        self.removeFlag = False

        self.EditMode = False
        self.setAnimated(True)

        # self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setContextMenuPolicy(Qt.CustomContextMenu)

        ########## context #########
        self.customContextMenuRequested.connect(self.custom_context)

        self.context_menu_for_list = QMenu(self)
        add_blank_row_action = QAction("Append row", self.context_menu_for_list)
        reset_list_action = QAction("Reset", self.context_menu_for_list)
        self.context_menu_for_list.addActions([add_blank_row_action,reset_list_action])

        self.context_menu_for_dict = QMenu(self)
        add_blank_row_dict_action = QAction("Append row", self.context_menu_for_dict)
        self.context_menu_for_dict.addActions([add_blank_row_dict_action])

        self.context_menu_for_plain_item = QMenu(self)
        insert_above_action = QAction("Insert above", self.context_menu_for_plain_item)
        insert_below_action = QAction("Insert below", self.context_menu_for_plain_item)
        # self.context_menu_for_plain_item.addAction


        add_blank_row_action.triggered.connect(self.append_row)
        add_blank_row_dict_action.triggered.connect(self.append_row)

        #########WIP tb for combobox#########
        # index = self.model.index(0,0,QModelIndex())
        # self.model.setData(index,"a")
        # combo_degelate = ComboDelegate(self,['a','b'])
        # self.setItemDelegateForColumn(4,combo_degelate)
        # self.show()
        # self.model.appendRow([QStandardItem('aa'),QStandardItem('aa'),QStandardItem('aa')])
        # self.openPersistentEditor(self.model.index(0,4))

    def initUI(self,type):
        self.model = _ConstraintModel()
        if type == "Generator":
            self.model.setHeaderData(0,Qt.Horizontal,"Constraint Container (Generator)")
        else:
            self.model.setHeaderData(0,Qt.Horizontal,"Constraint Container (Candidate)")
        self.model.setHeaderData(1,Qt.Horizontal,"Constraint ID")
        self.model.setHeaderData(2,Qt.Horizontal,"Constraint Type")
        self.model.setHeaderData(3,Qt.Horizontal,"Value")
        self.model.setHeaderData(4,Qt.Horizontal,"fcn_type")

        self.setModel(self.model)

        self.resizeColumnToContents(0)

        self.debugType = type

    def createNewConstraintAST(self,_id , _parentName, _DesignConstraint):
        self._DesignConstraintFromQTobj = _DesignConstraint
        rc = self.model.createNewColumnWithID(_id=_id, _parentName=_parentName, _DesignConstraint = _DesignConstraint)

        if _DesignConstraint[_parentName][_id]._type == 'Sref':
            sref_item = self.model.item(rc,0)
            calculate_name_item = sref_item.child(4,4) #row=4 for calculate_fcn in Sref ast
            idx = self.model.indexFromItem(calculate_name_item).siblingAtColumn(4)
            fcn_list = list(generator_model_api.class_function_dict[_DesignConstraint[_parentName][_id]._ast.library].keys())
            combo_delegetor = ComboDelegate(self,fcn_list)
            self.setItemDelegateForColumn(4,combo_delegetor)
            # idx = self.model.index(rc,3,QModelIndex())
            # self.model.appendRow([QStandardItem('aa')])
            # self.openPersistentEditor(self.model.index(rc,3))
            self.openPersistentEditor(idx)


    def UpdateSelectedItem(self, item):
        if item == None:
            pass
        else:
            constraint = self.model._ConstraintDict[item.text()]
            self.cw = _ConstraintSetupWindow(constraint._ParseTree)
            self.cw.show()

    def mouseDoubleClickEvent(self, QMouseEvent):

        ####################double click update flow#######################
        # 1> same field value find ! and update to Constraint  (If class is not constraint case only)
        # 2> If class is constraint : it refresh sub-hierarchy value.
        # 2-2> If class is not constraint but list type or dictionary type: it refresh sub-hierarchy value.(Maybe?)
        ################# 3rd step is Unnecessary ########## 3> If class has parent : it update same-hierarchy value for parent
        ###################################################################
        #0 : placeholder, #1 : ID, #2: ConstraintRealType, #3: value
        # a = self.model.findItems('',Qt.MatchContains,1)
        # ids = [item.text() for item in a]
        try:
            ###Step 1 update value#####################################
            itemIDitem = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(1))     #ID
            itemID = itemIDitem.text()
            motherID = None
            moduleName = re.sub(r'\d','',itemID)
            try:
                valueItem = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(3))    #ConstraintValue
                value = valueItem.text()
            except:
                value = None

            if moduleName in self._DesignConstraintFromQTobj:
                pass
            else:
                motherIDItem = self.model.itemFromIndex(self.currentIndex().parent().siblingAtColumn(1))
                motherID = motherIDItem.text()
                motherModuleName = re.sub(r'\d','',motherID)
                placeHolderItem = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(0))
                placeHolder = placeHolderItem.text()

                #if parent is not AST case (Double list or dictionary case)
                if motherModuleName not in self._DesignConstraintFromQTobj:
                    grandparentIDItem = self.model.itemFromIndex(self.currentIndex().parent().parent().siblingAtColumn(1))
                    grandparentID = grandparentIDItem.text()
                    grandParentModuleName = re.sub(r'\d','',grandparentID)
                    fieldItem = self.model.itemFromIndex(self.currentIndex().parent().siblingAtColumn(0))
                    field = fieldItem.text()
                    if type(self._DesignConstraintFromQTobj[grandParentModuleName][grandparentID]._ast.__dict__[field]) == dict:
                        self.updateDesignConstraintWithDict(Module=grandParentModuleName,Id=grandparentID,Field=field,Key=placeHolder,StringValue=value)
                    else:
                        idx = itemIDitem.row()
                        self.updateDesignConstraintWithList(Module=grandParentModuleName, Id=grandparentID, Field=field,
                                                            Idx=idx, StringValue=value)
                else:
                    self.updateDesginConstraintWithSTR(Module=motherModuleName,Id=motherID,Field =placeHolder ,StringValue=value)

            ###Step 2 sub-hierarchy refresh#####################################            #To expand unseen contents <Constraint Case>
            if moduleName == '':
                pass
            elif moduleName in self._DesignConstraintFromQTobj:
                if itemID in self._DesignConstraintFromQTobj[moduleName]:
                    self.refreshItem(self.currentIndex())
                else:
                    print('Warning during mouseDoubleClickEvent, Valid module name ({}), but invalid ID ({})'.format(moduleName,itemID))

            ###Step 3 sub-hierarchy refresh for placeholder's children #####################################    #To expand unseen contents <value = *, Case>
            if self.currentIndex().parent().isValid():  # Sub-hierarchy case        Do nothing??->Yes, it does something....
                self.refreshItem(self.currentIndex())

            self.send_UpdateDesignConstraintID_signal.emit(itemID,motherID)

        except:
            traceback.print_exc()
            print("Value Update Fail!")

    def update_constraint_by_id(self, id):
        if id in self.model._ConstraintItem:
            itemIDitem = self.model._ConstraintItem[id]
            index= self.model.indexFromItem(itemIDitem)
            self.refreshItem(index)



    def updateDesginConstraintWithSTR(self,Module,Id,Field,StringValue):
        # convert: String type value --> Adequate type
        if StringValue == None or StringValue == "" or StringValue == "*":
            return

        tmpChildModule = re.sub(r'\d','',StringValue)
        if tmpChildModule in self._DesignConstraintFromQTobj:                        #Check whether it is constraint or not
            if StringValue in self._DesignConstraintFromQTobj[tmpChildModule]:
                _value = self._DesignConstraintFromQTobj[tmpChildModule][StringValue]._ast
                self._DesignConstraintFromQTobj[Module][Id]._appendDesignConstraintValue(_index=Field,_value=_value)
                return
        else:
            try:
                _value = ast.literal_eval(StringValue)
            except:
                _value = StringValue

            self._DesignConstraintFromQTobj[Module][Id]._setDesignConstraintValue(_index=Field,_value=_value)
            return

    def updateDesignConstraintWithDict(self,Module,Id,Field,Key,StringValue):
        self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field][Key] = StringValue

    def updateDesignConstraintWithList(self,Module,Id,Field,Idx,StringValue):
        # if Idx <= len(self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field]):
        #     self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field].append(None)

        try:
            self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field][Idx] = [float(value) for value in StringValue.split(',')]
        except:
            self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field][Idx] = StringValue
        # self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field][Idx] = StringValue.split(',')

    def remove_item(self, ID):
        """
        This function is made for display item deletion purpose;
        Actual module deletion is not implemented in this function.

        :param ID:
        :return: (None), remove display item
        """

        _items = self.model.findItems(ID,column=1)
        for item in _items:
            # ID_by_Item_index = self.model.indexFromItem(item).siblingAtColumn(1)
            # ID_by_Item = self.model.itemFromIndex(ID_by_Item_index).text()  # Constraint ID of corresponding item
            if self.model.indexFromItem(item).parent().isValid():
                parentIndex = self.model.indexFromItem(item).parent()
                self.model.removeRow(item.row(), parentIndex)
            else:
                self.model.removeRow(item.row())
        self.removeFlag = False

    def checkSend(self):
        print("check Evaluation")
        try:
            if self.currentIndex().row() == -1:
                self.warning = QMessageBox()
                self.warning.setText("There is no selected Constraint")
                self.warning.show()
                return
            elif self.model.itemFromIndex(self.currentIndex().siblingAtColumn(1)).text() == '' or self.model.itemFromIndex(self.currentIndex().siblingAtColumn(1)).text() == None:
                self.warning = QMessageBox()
                self.warning.setText("Only Constraint Can be moved!")
                self.warning.show()
                return
            else:
                selectedItem=self.model.itemFromIndex(self.currentIndex().siblingAtColumn(1))
                self.removeFlag = True
                #self.send_SendSTMT_signal.emit(self.itemToASTDict[selectedItem.text()])
                self.send_SendID_signal.emit(selectedItem.text())

        except:
            self.warning = QMessageBox()
            self.warning.setText("Constraint Transfer failed")
            self.warning.show()

    def removeCurrentIndexItem(self):
        if self.removeFlag == False:
            return

        selectedItem =self.model.itemFromIndex(self.currentIndex().siblingAtColumn(1))
        if selectedItem.text() in self.model._ConstraintItem:
            del self.model._ConstraintItem[selectedItem.text()]
        if self.currentIndex().parent().isValid():
            motherIDleItem = self.model.itemFromIndex(self.currentIndex().parent().siblingAtColumn(1))
            motherID = motherIDleItem.text()
            motherValueItem = self.model.itemFromIndex(self.currentIndex().parent().siblingAtColumn(3))
            motherValue = motherValueItem.text()

            motherTypeItem = self.model.itemFromIndex(self.currentIndex().parent().siblingAtColumn(0))
            motherType = motherTypeItem.text()

            removeNameItem = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(1))
            removeID = removeNameItem.text()
            removeTypeItem = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(0))
            removeType = removeTypeItem.text()

            updateDict = dict()

            ############## Simple STMT case ################
            if motherValue != '*':
                motherModule = re.sub(r'\d','',motherID)
                self._DesignConstraintFromQTobj[motherModule][motherID]._ast.__dict__[removeType] = None
                for i in range(0, removeTypeItem.rowCount()):
                    removeTypeItem.takeRow(0)
            ############## Compound STMT case ################
            else:
                grandParentIDItem = self.model.itemFromIndex(self.currentIndex().parent().parent().siblingAtColumn(1))
                grandParentID = grandParentIDItem.text()
                grandParentTypeItem = self.model.itemFromIndex(self.currentIndex().parent().parent().siblingAtColumn(0))
                grandParentModule = re.sub(r'\d','',grandParentID)

                deleteLine = removeTypeItem.row()
                self._DesignConstraintFromQTobj[grandParentModule][grandParentID]._ast.__dict__[motherType].pop(deleteLine)
                motherTypeItem.takeRow(deleteLine)
                self.refreshItem(self.currentIndex().parent())

        else:
            sibling_index = self.model.indexFromItem(selectedItem).siblingAtColumn(1)
            sibling_id = self.model.itemFromIndex(sibling_index).text()
            self.remove_item(sibling_id)

    def updateConstraintDictFromQTInterface(self,_qtProject):
        # for constraint in _QTInterface.
        for module in _qtProject._DesignConstraint:
            for id in _qtProject._DesignConstraint[module]:
                self.itemToDesignConstraintDict[id] = _qtProject._DesignConstraint[module][id]
        self.model.updateConstraintDictFromView(self.itemToDesignConstraintDict)
        # pass

    def removeHierarchyConstraintfromDictionary(self,constraint):
        hierarchyNameList = constraint._findSubHierarchy(_MaxSearchDepth=10)
        for key in hierarchyNameList:
            if key[0] in self.itemToDesignConstraintDict:
                del self.itemToDesignConstraintDict[key[0]]

    def receiveConstraintID(self,_id):
            _module = re.sub(r'\d','',_id)
            if _module not in self._DesignConstraintFromQTobj:
                self.send_RequestDesignConstraint_signal.emit()
#            if _module in self._DesignConstraintFromQTobj:
#                if _id in self._DesignConstraintFromQTobj[_module]:
#                    _updateFlag = True
#            else:
#                _updateFlag = False
#                print('Warning during receiveConstraintSTMT, module and id update from QT is fail')
#            if _updateFlag == True:     #Receive update value
#                pass
 #           else:                       #Receive new value (from other side, Floadting --> heirarchy or Heirarchy --> Floation)
            if self.currentIndex().row() == -1:                 # Not selected any target parent constraint
                #self.createNewConstraintSTMTList([_STMT],_idToSTMTdict)
                self.createNewConstraintAST(_id=_id,_parentName=_module,_DesignConstraint=self._DesignConstraintFromQTobj)
                self.send_ReceiveDone_signal.emit()
                self.send_RootDesignConstraint_signal.emit(_id)
            else:
                ####### At first check whether it is possible to modify or not ####### (In case of Constraint itself, you cannot modify!! only parsetrees are possible to modify
                #######Case2: If it is constraint. < cannot change>
                constraintItem = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(1))
                constraintName = constraintItem.text()
                constraintModule = re.sub(r'\d','',constraintName)
                if constraintModule in self._DesignConstraintFromQTobj:
                    print("It isn't allowed to change constraint")
                    self.warning = QMessageBox()
                    self.warning.setText("It isn't allowed to change constraint itself")
                    self.warning.show()
                    return
                #######Case3: If it has parent.
                else:
                    motherIdItem = self.model.itemFromIndex(self.currentIndex().parent().siblingAtColumn(1))
                    motherId = motherIdItem.text()
                    motherModule = re.sub(r'\d','',motherId)
                    if motherModule not in self._DesignConstraintFromQTobj:
                        self.send_RequestDesignConstraint_signal.emit()
                    placeHolder = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(0)).text()
                    self.updateDesginConstraintWithSTR(Module=motherModule, Id=motherId, Field=placeHolder, StringValue=_id)
                    #_itemType = self._DesignConstraintFromQTobj[motherModule][motherId]._ast[placeHolder]._type
                    currentItemId = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(3))
                    #currentItemType = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(2))
                    currentItemId.setText('*')
                    #currentItemType.setText(_itemType)
                index = self.currentIndex()

                try:
                    self.refreshItem(index)
                    print("debug:receiveDone")
                    self.send_ReceiveDone_signal.emit()
                except:
                    import traceback
                    traceback.print_exc()
                    print("Somehow failed Refresh")
                    pass

    def refreshItem(self,itemIndex):  #Refresh Design Constraint

        indexIDItem = self.model.itemFromIndex(itemIndex.siblingAtColumn(1))
        valueItem = self.model.itemFromIndex(itemIndex.siblingAtColumn(3))
        indexID = indexIDItem.text()
        value = valueItem.text()
        tmpModuel =  re.sub(r'\d','',indexID)
        self.send_RequestDesignConstraint_signal.emit()

        if tmpModuel in self._DesignConstraintFromQTobj:                #Constraint Case -> expand subhierarchy
            if indexID in self._DesignConstraintFromQTobj[tmpModuel]:
                dc = self._DesignConstraintFromQTobj[tmpModuel][indexID]
                self.model.updateRowChildWithAST(_DesignConstraint= dc, motherIndex=itemIndex)

        #elif indexID == "" or indexID == None:                    #If refresh Item is parsetree and it has at least one child constraint
        elif value == "*":
            indexTypeItem = self.model.itemFromIndex(itemIndex.siblingAtColumn(0))
            type = indexTypeItem.text()
            motherIndex = itemIndex.parent().siblingAtColumn(1)
            motherItem = self.model.itemFromIndex(motherIndex)
            motherName = motherItem.text()
            # motherModule = re.sub(r'\d','',motherName)
            motherModule = get_id_return_module(id=motherName, type='_DesignConstraint', moduleDict=self._DesignConstraintFromQTobj)
            _ast = self._DesignConstraintFromQTobj[motherModule][motherName]._ast

            self.model.readParseTreeForMultiChildren(motherItem=indexTypeItem,_AST=_ast ,key=type)


            # updateConstraint = self.itemToDesignConstraintDict[indexItemName]
            #
            # self.model.updateRowChild(updateConstraint, motherIndex=itemIndex)


        elif itemIndex.parent().isValid() == True:                          # If refresh Item is parsetree and it has mother constraint
            motherIndex = itemIndex.parent().siblingAtColumn(1)
            motherItem = self.model.itemFromIndex(motherIndex)
            originalRow = motherIndex.row()
            motherName = motherItem.text()

            #indexID.setEditable(True)
            tmpModuel = re.sub(r'\d', '', motherName)
            if tmpModuel not in self._DesignConstraintFromQTobj:
                #do nothing! (field value is not constraint but list or dictionary case)
                return

            dc = self._DesignConstraintFromQTobj[tmpModuel][motherName]
            self.model.updateRowChildWithAST(_DesignConstraint= dc,motherIndex=itemIndex.parent())

        else:
            print("Refresh Else")
            pass

        # self.model.resizeColumnToContents(0)
        self.resizeColumnToContents(0)

    def keyPressEvent(self, QKeyEvent):

        if QKeyEvent.key() == Qt.Key_Escape:
            self.clearSelection()
            self.setCurrentIndex(self.model.index(-1,-1))
        elif QKeyEvent.key() == Qt.Key_F2:
            if self.currentIndex().isValid() ==False:
                return
            elif self.currentIndex().column() == 0:
                return
            else:
                item = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(1))
                itemName = item.text()
                if (itemName in self.itemToDesignConstraintDict) == True:
                    return
        elif QKeyEvent.key() == Qt.Key_Delete:  # If delete key pushed, 'deleteConstraint_signal' sent to MainWindow
            try:
                self.removeFlag = True
                selectedItem = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(1))
                id = selectedItem.text()  # Constraint ID of corresponding item
                if id != "":
                    self.send_deleteConstraint_signal.emit(id)
                else:
                    parent_item = self.model.itemFromIndex(self.currentIndex().parent().siblingAtColumn(1))
                    parent_id = parent_item.text()
                    if parent_id != "":
                        module = get_id_return_module(parent_id,'_DesignConstraint',self._DesignConstraintFromQTobj)
                        field_item = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(0))
                        field = field_item.text()
                        del self._DesignConstraintFromQTobj[module][parent_id]._ast.__dict__[field]
                        self.refreshItem(self.model.indexFromItem(parent_item))
                    else:
                        ### double list or dictionary ###
                        grandparent_item = self.model.itemFromIndex(self.currentIndex().parent().parent().siblingAtColumn(1))
                        grandparent_id = grandparent_item.text()
                        module = get_id_return_module(grandparent_id, '_DesignConstraint',self._DesignConstraintFromQTobj)
                        field_item = self.model.itemFromIndex(self.currentIndex().parent().siblingAtColumn(0))
                        field = field_item.text()
                        current_item = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(0))
                        key_value = current_item.text()
                        if key_value != '': # dictionary case
                            del self._DesignConstraintFromQTobj[module][grandparent_id]._ast.__dict__[field][key_value]
                        else:
                            row = current_item.row()
                            del self._DesignConstraintFromQTobj[module][grandparent_id]._ast.__dict__[field][row]
                        self.refreshItem(self.model.indexFromItem(parent_item))

            except:
                traceback.print_exc()
        elif QKeyEvent.key() == Qt.Key_C:
            if self.currentIndex().isValid() ==False:
                return
            nameItem = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(1))
            name = nameItem.text()
            if name in self.itemToDesignConstraintDict:
                self.removeFlag = False
                self.send_SendCopyConstraint_signal.emit(self.itemToDesignConstraintDict[name])
                print("copy!!")
        elif QKeyEvent.key() == Qt.Key_F5:
            self.resizeColumnToContents(0)

        self.originalKeyPress(self,QKeyEvent)

    def receiveDesignParameter(self,DesignParameter):
        type = DesignParameter._ItemTraits['_DesignParametertype'] #number
        layer = DesignParameter._ItemTraits['_Layer']              #string

        if type == 1:
            s_type = "_BoundaryElement"
        elif type == 2:
            s_type = "_PathElement"
        elif type == 3:
            s_type = "_BoundaryElement"
        else:
            print("Undefined Type Error")
            return

        DeclarationString = "self."+s_type+"Declaration"
        if type == 1 or type == 2:
            DeclarationString += "(_Layer=DesignParameters._LayerMapping['"+layer+"'][0],_Datatype=DesignParameters._LayerMapping['"+layer+"'],_XYCoordinates=[],"
            if type == 1:
                Xwidth = str(DesignParameter._ItemTraits['_XWidth'])
                Ywidth = str(DesignParameter._ItemTraits['_YWidth'])
                DeclarationString += "_XWidth="+Xwidth+",_YWidth="+Ywidth+"),"
            else:
                width = str(DesignParameter._ItemTraits['_Width'])
                DeclarationString += "_Width="+width+"),"

        print(DeclarationString)

    def update_design_by_module_id(self,_designConstraint,moudle,id):
        pass

    def dataChanged(self, topLeft:QModelIndex, bottomRight:QModelIndex, roles) -> None:
        super().dataChanged(topLeft, bottomRight, roles)
        self.mouseDoubleClickEvent(topLeft)
        # self.refreshItem(topLeft)
        id_item = self.model.itemFromIndex(topLeft.siblingAtColumn(1))
        id = id_item.text()
        recursive_count = 0
        while '' == id or id is None:
            tmp_idx = self.model.indexFromItem(id_item).parent().siblingAtColumn(1)
            id_item = self.model.itemFromIndex(tmp_idx)
            id = id_item.text()
            recursive_count += 1
            if recursive_count > 9:
                raise Exception("Invalid ID.")
        self.send_DataChanged_signal.emit(id)


    def custom_context(self, point : QPoint):
        try:
            idx = self.indexAt(point)
            if idx.isValid():
                type_item = self.model.itemFromIndex(idx.siblingAtColumn(2))
                if "list" in type_item.text():
                    self.context_menu_for_list.exec_(self.viewport().mapToGlobal(point))
                if "dict" in type_item.text():
                    self.context_menu_for_dict.exec_(self.viewport().mapToGlobal(point))
        except:
            traceback.print_exc()
            pass

    def append_row(self):
        current_item = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(0))
        current_item.appendRow([QStandardItem(),QStandardItem(),QStandardItem(),QStandardItem()])
        print("what happend?")

    def get_dp_highlight_dc(self,dp_id_list,_):
        """
        :param dp_id_list: design_parameter_list
        :param _: not use (trigger signal return dp_di_list and type, but this slot does not use type.
        :return:
        """
        self.selectionModel().clearSelection()

        self.send_RequestElementManger_signal.emit()
        dc_id_list = [self._ElementMangerFromQTobj.get_dc_id_by_dp_id(_id) for _id in dp_id_list]
        constraint_names_item = self.model.findItems('', Qt.MatchContains, 1)
        selection_model = QItemSelectionModel(self.model)
        for item in constraint_names_item:
            if item.text() in dc_id_list:
                try:
                    selected_item_idx = self.model.indexFromItem(item)
                    # self.selectionModel().select(selected_item_idx,QItemSelectionModel.Rows, QItemSelectionModel.Select)
                    self.selectionModel().select(selected_item_idx,
                                                 QItemSelectionModel.Rows | QItemSelectionModel.Select | QItemSelectionModel.Current)
                    self.setCurrentIndex(selected_item_idx)
                    self.scrollTo(selected_item_idx)
                except:
                    traceback.print_exc()


        # constraint_ids = [item.text() for item in constraint_names]








class _ConstraintModel(QStandardItemModel):
    def __init__(self):
        QStandardItemModel.__init__(self)
        self._DesignConstraintFromQTobj = None
        self._ConstraintNameList = []
        self._ConstraintDict = dict()
        self._ConstraintItem = dict()
        self._Root = None
        self.setColumnCount(5)
        # self.testInitial()

    def readConstraint(self,rootConstraint):
        # rootConstraint = QTDesignConstraint
        rootType = rootConstraint._type
        rootName = rootConstraint._id
        # rootValue = rootConstraint._ParseTree

        self.setItem(0,0,QStandardItem(rootType))
        self.setItem(0,1,QStandardItem(rootName))
        # self.setItem(0,2,rootValue)

    def createNewColumnWithID(self,_id, _parentName, _DesignConstraint, rc = None):
        self._DesignConstraintFromQTobj = _DesignConstraint
        _type = self._DesignConstraintFromQTobj[_parentName][_id]._type
        tmpConstraintType = QStandardItem(_type)
        self._ConstraintItem[_id] = tmpConstraintType

        if rc == None:
            rc = self.rowCount()

        self.insertRow(rc, [tmpConstraintType, QStandardItem(_id), QStandardItem(_type),QStandardItem(), QStandardItem() ])
        # Item Field:  0-> PlaceHolder Type , 1-> _id , 2-> Content Type , 3 -> value
        #self._ConstraintNameList.append(constraintName)
        self.readParseTreeWtihAST(motherItem=tmpConstraintType, _AST= _DesignConstraint[_parentName][_id]._ast)
        return rc

    def updateRowChildWithAST(self,_DesignConstraint,rc=None,motherIndex=None):
        if motherIndex == None:                                             #When There is no parent  (It Creats a New Row)
            tmpConstraintType = QStandardItem(_DesignConstraint._type)
            constraintName = _DesignConstraint._id
            self._ConstraintItem[constraintName] = tmpConstraintType

            if rc == None:
                rc= self.rowCount()
            #0 : placeholder, #1 : ID, #2: ConstraintRealType, #3: value
            self.insertRow(rc,[tmpConstraintType,QStandardItem(constraintName), QStandardItem(_DesignConstraint._type), QStandardItem()])
            self.readParseTreeWtihAST(tmpConstraintType,_DesignConstraint._ast)
        else:                                                               #When there is a parent
            if motherIndex.isValid() == False:
                self.warning=QMessageBox()
                self.warning.setText("Mother Index is invalid")
                self.warning.show()
                return

            item = self.itemFromIndex(motherIndex.siblingAtColumn(0))
            self.readParseTreeWtihAST(item,_DesignConstraint._ast)

    def returnChildValueForUpdate(self,motherIndex=None):         #Update Written Text into Real DesignConstraint Value
        if motherIndex == None:         #if Mother is None: update cannot start
            print('Invalid Mother Index')
            return

        motherIDitem = self.itemFromIndex(motherIndex.siblingAtColumn(1))
        motherID = motherIDitem.text()
        motherTypeItem = self.itemFromIndex(motherIndex.siblingAtColumn(0))
        motherType = motherTypeItem.text()
        updateValueDict = dict()
        updateValueDict['_id'] = None

        motherID_Module = re.sub(r'\d','',motherID)
        if motherID_Module in self._DesignConstraintFromQTobj:
            #Module Valid Case
            if motherID in self._DesignConstraintFromQTobj[motherID_Module]:
                tmpAST = self._DesignConstraintFromQTobj[motherID_Module][motherID]._ast
                for field in tmpAST._fields:
                    updateValueDict[field] = tmpAST.__dict__[field]
                return updateValueDict
            else:
                print('Error occured, during parsing child value! ID is not valid. (Module({}) is valid.)'.format(motherID_Module))



        if motherName == "*":
            #updateValueDict['_type'] = motherType
            updateList = []
            for row in range(0,motherTypeItem.rowCount()):
                #updateKeyValue = []
                childNameItem = motherTypeItem.child(row, 1)
                childName = childNameItem.text()

                #try:            #This part reconsider
                #    childNameItem = float(childName)


                childTypeItem = motherTypeItem.child(row, 0)
                childType = childTypeItem.text()

                #updateValueDict[childType] = childName
                #updateKeyValue = (childType,childName)
                updateList.append(childName)
            updateValueDict[motherType] = updateList
            grandParentModuleItem = self.itemFromIndex(motherIndex.parent().siblingAtColumn(1))
            grandParentName = grandParentModuleItem.text()
            updateValueDict['_id'] = grandParentName
        else:
            for row in range(0,motherTypeItem.rowCount()):          #For each child's item
                childNameItem = motherTypeItem.child(row,1)
                if childNameItem is None:                           #If Child doesn't have any update value, then pass
                    continue

                childTypeItem = motherTypeItem.child(row,0)
                childType = childTypeItem.text()

                childName = childNameItem.text()
                #if childName in self._ConstraintDict:
                #    continue
                if childName == "*":
                    continue
                elif childName == "":
                    continue
                #elif childName == "@None":
                #    self._ConstraintDict[motherName]._setDesignConstraintValue(_index=childType,_value=None)
                else:
                    if childName == "reset":
                        childName = None
                    try:
                        childName = int(childName)
                    except:
                        pass

                    #try:
                    #    if childType != "_string":
                    #        childName = childName.split(';')
                    #    else:
                    #        childName = childName
                    #except:
                    #    pass


                    ###########Depend On Child Type###########  name --> string, value --> string In List
                    # if childType == "_value" or childType == "_string":
                    #     if type(childName) != list:
                    #         childName = [childName]

                    #if childType == '_name' and type(childName) == list:
                    #    childName = childName[0]

                    #Not sure 2020-03-16 ;;;;
                    #if type(childName) == list:
                    #    childName = childName[0]

                    updateValueDict[childType] = childName
                    # self._ConstraintDict[motherName]._setDesignConstraintValue(_index=childType,_value=childName)



        return updateValueDict

    def updateOriginalColumn(self,DesignConstraint):
        try:
            if self._ConstraintDict[DesignConstraint._id] == None:
                return
            else:
                updateItem = self._ConstraintItem[DesignConstraint._id]
                # self.refresh(updateItem)
                # self.readParseTree(updateItem,DesignConstraint)


                # print("FindText:",DesignConstraint._id)
                # print("All Items:")
                #
                #
                # if len(matchItem) == 0:
                #     print("UpdateFail Because There are no matched Item")
                # else:
                #     print("Ready to Update!!!!")
        except:
            print("Update fail")

    def readHierarchy(self,DesignConstraint,_depth=None):
        hierarchyList = DesignConstraint._findSubHierarchy(_depth)
        print("Read Hierarchy")
        print(hierarchyList)
        self.readParseTree(self._ConstraintItem[DesignConstraint._id],DesignConstraint)



        pass

    def readParseTree(self,motherItem,_STMTList):
        # print("Start Reading ParseTree")
        # print("Mother Item: ",motherItem.text())

        for stmt in _STMTList:
            for key in stmt:
                if key == "_id" or key == "_type" or key == 'lineno' or key == 'col_offset' or key == 'end_lineno' or key == 'end_col_offset':
                    continue
                else:
                    if type(stmt[key]) == list:
                        constraintName = '*'
                        value = constraintName
                    elif type(stmt[key]) == dict:
                        constraintName = stmt[key]['_id']
                        value = stmt[key]['_type']
                    else:
                        value = stmt[key]
                        try:
                            value = str(value)
                        except:
                            print("value, value Type:" , value, type(value))
                        constraintName = value

                    # tmpName = stmt[key]
                    #
                    # if type(tmpName) == str:
                    #     pass
                    # elif type(tmpName) == None:
                    #     tmpName = "@None"
                    # elif type(tmpName) == int or type(tmpName) == float:
                    #     tmpName = str(tmpName)
                    # else:
                    #     if type(tmpName) == dict:
                    #         tmpName = tmpName['_id']
                    #     elif type(tmpName) == list:
                    #         if len(tmpName) == 0:
                    #             tmpName = ""
                    #         else:
                    #             if key == "body" or key == "targets" or key == "ops" or key =='keys' or key =='values':
                    #                 tmpName = '*'
                    #             else:
                    #                 try:
                    #                     tmpName = tmpName[0]['_id']
                    #                 except:
                    #                     tmpName = ''

                    checkChild = self.findChildrenWithText(motherItem,key)
                    if checkChild != None:
                        checkChild.setText(constraintName)
                        continue




                    tmpA = QStandardItem(key)
                    tmpB = QStandardItem(constraintName)
                    tmpC = QStandardItem(value)

                    # tmpA.appendRow([QStandardItem("hi"),QStandardItem("test")])
                    motherItem.appendRow([tmpA, tmpB,tmpC])


                # if type(tmpName) == str:
                #     pass
                # elif tmpName == None:
                #     tmpName = ""
                # else:
                #     if type(tmpName) == dict:#QTInterface.QtDesinConstraint._ParseTree:
                #         tmpName = tmpName['_id']
                #         # self._ConstraintDict[tmpName] = DesignConstraint.
                #
                #
                #     elif type(tmpName) == list:
                #         if len(tmpName) == 0:
                #             tmpName =""
                #         else:
                #             if type(tmpName[0]) == str:
                #                 if len(tmpName) >1 and type(tmpName[1]) == str:
                #                     tmpName = tmpName[0] + "," +tmpName[1]
                #                 else:
                #                     tmpName = tmpName[0]
                #             elif type(tmpName[0]) == int:
                #                 tmpName = str(tmpName[0])
                #             else:
                #                 if keys == "_statements" or keys == "_arguments" or keys == "_libImport" or keys == "_dictionaryElements" or keys == "_functionDefine" or keys == "_logic" or keys == "_dictionaryElement" or keys == "_elifLogic" or keys == "_classDefine":
                #                     tmpName = "*"
                #                 else:
                #                     try:
                #                         tmpName = tmpName[0]['_id']
                #                     except:
                #                         tmpName = ""


                # checkChild = self.findChildrenWithText(motherItem,keys)   #If Constraint has child constraint, then show Constraint Name for Child constraint.
                # if  checkChild != None:
                #     checkChild.setText(tmpName)
                #     continue
                #
                #
                # tmpA = QStandardItem(keys)
                # tmpB = QStandardItem(tmpName)
                # # tmpA.appendRow([QStandardItem("hi"),QStandardItem("test")])
                # motherItem.appendRow([tmpA,tmpB])
                # pass

    def readParseTreeWtihAST(self,motherItem,_AST):
            # if debugFlag == True:
            #     print("Start Reading ParseTree with AST")
            #     print("Mother Item: ",motherItem.text())

            for field in _AST._fields:
                if field in _AST.__dict__:
                    childVariable = _AST.__dict__[field]
                else:
                    _AST.__dict__[field] = None
                    childVariable = None
                if type(childVariable) == None:
                    continue
                if childVariable == None:   # <Child is None>
                    _placeholder = field
                    _id = None
                    _constraintValue = None
                    _constraintRealType = None
                elif childVariable == "":
                    _placeholder = field
                    _id = None
                    _constraintValue = str(childVariable)
                    _constraintRealType = None
                elif type(childVariable) == int or type(childVariable) == float or type(childVariable) == str:
                    _placeholder = field
                    _id = ''
                    _constraintValue = str(childVariable)
                    _constraintRealType = str(type(childVariable))
                elif type(childVariable) == list or type(childVariable) == dict:     #Compound STMT
                    _placeholder = field
                    _id = ''
                    _constraintRealType = str(type(childVariable))
                    _constraintValue = '*'
                else:
                    # if _placeholder == 'XY':
                    #     _id = ''
                    #     _constraintRealType = list
                    #     _constraintValue = '*'
                    #
                    #
                    # else:
                    ##check wether it is constriant!
                    try:

                        childID = childVariable._id
                        childModule = re.sub(r'\d','',childID)
                        _placeholder = field
                        _id = childVariable._id
                        _constraintRealType = childVariable._type
                        _constraintValue = None
                    except:
                        print('debug Porint')
                        print("error,it must be ast, but it seems that it doesn't have enough info or not ast.")
                        print("_placeholder = {}".format(field))
                        print("id = {}".format(_id))
                        print("_constraintRealType = {}".format(childVariable._type))
                        print("id = {}".format(_id))

                checkChild = self.findChildrenWithText(motherItem, field)
                if checkChild != None:
                    child = self.findChildrenWithContainer(motherItem,_placeholder)
                    if child != None:
                        value_item_index = child.index().siblingAtColumn(3)
                        value_item = self.itemFromIndex(value_item_index)
                        value_item.setText(_constraintValue)
                    checkChild = None
                    continue


                tmpA = QStandardItem(_placeholder)
                tmpB = QStandardItem(_id)
                tmpC = QStandardItem(_constraintRealType)
                tmpD = QStandardItem(_constraintValue)

                # tmpA.appendRow([QStandardItem("hi"),QStandardItem("test")])
                motherItem.appendRow([tmpA, tmpB, tmpC, tmpD, QStandardItem()])

    def readParseTreeForMultiChildren(self,motherItem=None,_AST = None,key=None):
        checkChild = self.findChildrenWithText(motherItem,key,column=0)   #If Constraint has child constraint, then show Constraint Name for Child constraint.

        if key not in _AST.__dict__:
            return
        #print('d start')
        #print('debug key and val:{} ,  {}'.format(key,_AST.__dict__[key]))
        #print('debug type: {}'.format(type(_AST.__dict__[key])))
        if len(_AST.__dict__[key]) != 0 and type(_AST.__dict__[key]) == list:
            valueItem = self.itemFromIndex(motherItem.index().siblingAtColumn(3))
            valueItem.setText("*")



        #test,, delete code order change...
        #When dictionary field double clicked, it has some problems
        for row in range(0,motherItem.rowCount()):
            print(motherItem.rowCount())
            motherItem.removeRow(0)

        for childAST in _AST.__dict__[key]:   #### childConstraint is item in list!
            if type(childAST) == list:
                # for row in range(0,motherItem.rowCount()):
                #     motherItem.removeRows(0)
                if type(childAST[0]) != list:   #Boundary case
                    print("List case display")
                    tmpC = QStandardItem(str(type(childAST)))
                    tmpD = str(childAST[0]) + ',' + str(childAST[1])
                    tmpD = QStandardItem(tmpD)
                    motherItem.appendRow([QStandardItem(), QStandardItem(), tmpC, tmpD])
                else:
                    for child_child_AST in childAST:
                        print("Doubled-list case display")
                        tmpC = QStandardItem(str(type(child_child_AST)))
                        tmpD = str(child_child_AST[0]) + ',' + str(child_child_AST[1])
                        tmpD = QStandardItem(tmpD)
                        motherItem.appendRow([QStandardItem(), QStandardItem(), tmpC, tmpD])
            elif type(childAST) == str:
                tmpA = QStandardItem(childAST)
                tmpD = QStandardItem(str(_AST.__dict__[key][childAST]))
                motherItem.appendRow([tmpA, QStandardItem(), QStandardItem(), tmpD])
            else:
                childASTid = childAST._id
                _type = childAST._type

                if self.findChildrenWithName(motherItem,childASTid) != None:
                    print("duplication Detect!")
                    print("duplication Item text",self.findChildrenWithName(motherItem,childASTid).text())
                    continue

                tmpA = QStandardItem(_type)
                tmpB = QStandardItem(childASTid)
                motherItem.appendRow([tmpA,tmpB,QStandardItem(_type),QStandardItem()])

    def findChildrenWithText(self,parentItem,key,column=None):
        if column == None:
            column = 1
        a = parentItem.hasChildren()
        for i in range(0,parentItem.rowCount()):
            childItem = parentItem.child(i,0)
            if childItem.text() == key:         # In Case Key and Child is matched
                valueIndex = childItem.index().siblingAtColumn(column)
                return self.itemFromIndex(valueIndex)
                # return childItem
                # return childItem.index()
        return None

    def findChildrenWithName(self,parentItem,name):
        for i in range(0,parentItem.rowCount()):
            childItem = parentItem.child(i,1)
            if childItem.text() == name:
                valueIndex = childItem.index().siblingAtColumn(1)
                return self.itemFromIndex(valueIndex)
        return None

    def findChildrenWithContainer(self,parentItem,name):
        for i in range(0,parentItem.rowCount()):
            childItem = parentItem.child(i,0)
            if childItem.text() == name:
                valueIndex = childItem.index().siblingAtColumn(0)
                return self.itemFromIndex(valueIndex)
        return None


    def updateConstraintDictFromView(self,constraintDict):
        self._ConstraintDict = []
        self._ConstraintDict = constraintDict


    def testInitial(self):


        item = QStandardItem("testTop")
        item2 = QStandardItem("testTop2")
        item3 = QStandardItem("testTop3")
        item4 = QStandardItem("testTop4")
        item.appendRow([item2,item3])
        # item2.appendRow(item4)
        self.setItem(0,0,item)
        self.setItem(0,1,item4)
        item2.appendRow([QStandardItem("hi"),QStandardItem("test")])
        item2.appendRow([QStandardItem("hello"),QStandardItem("te3st")])



class QtTextEditLogger(logging.Handler):
    def __init__(self, parent):
        super().__init__()
        self.widget = QPlainTextEdit(parent)
        self.widget.setReadOnly(True)

    def emit(self, record):
        msg = self.format(record)
        self.widget.appendPlainText(msg)

class _LogMessageWindow(QDialog, QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        logTextBox = QtTextEditLogger(self)
        # You can format what is printed to text box
        logTextBox.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logging.getLogger().addHandler(logTextBox)
        # You can control the logging level
        logging.getLogger().setLevel(logging.DEBUG)

        #self._button = QPushButton(self)
        #self._button.setText('Test Me')

        layout = QVBoxLayout()
        # Add the new logging box widget to the layout
        layout.addWidget(logTextBox.widget)
        #layout.addWidget(self._button)
        self.setLayout(layout)
        # self._InfoMessage()
        # self._WarningMessage()


        # Connect signal to slot
        #self._button.clicked.connect(self.test)
    def _InfoMessage(self, _message = None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print(self._id, " : _LogMessageWindow, _InfoMessage  Run.")
        if _message == None:
            #return userDefineExceptions._InvalidInputError
            #print(userDefineExceptions._InvalidInputError)
            self._ErrorMessage(_message ="_InfoMessage Func: "+ userDefineExceptions._InvalidInputError)
        else:
            try:
                logging.info(_message)
            except:
                #return userDefineExceptions._UnkownError
                self._ErrorMessage(_message="_InfoMessage Func: " + userDefineExceptions._UnkownError)

    def _WarningMessage(self, _message = None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print(self._id, " : _LogMessageWindow, _InfoMessage  Run.")
        if _message == None:
            #return userDefineExceptions._InvalidInputError
            #print(userDefineExceptions._InvalidInputError)
            self._ErrorMessage(_message="_WarningMessage Func: "+userDefineExceptions._InvalidInputError)
        else:
            try:
                logging.warning(_message)
            except:
                #return userDefineExceptions._UnkownError
                self._ErrorMessage(_message="_WarningMessage Func: " + userDefineExceptions._UnkownError)
    def _ErrorMessage(self, _message = None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print(self._id, " : _LogMessageWindow, _InfoMessage  Run.")
        if _message == None:
            #return userDefineExceptions._InvalidInputError
            #print(userDefineExceptions._InvalidInputError)
            self._ErrorMessage(_message="_ErrorMessage Func: "+userDefineExceptions._InvalidInputError)
        else:
            try:
                logging.error(_message)
            except:
                #return userDefineExceptions._UnkownError
                self._ErrorMessage(_message="_ErrorMessage Func: " + userDefineExceptions._UnkownError)
    def _DebugMessage(self, _message = None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print(self._id, " : _LogMessageWindow, _InfoMessage  Run.")
        if _message == None:
            #return userDefineExceptions._InvalidInputError
            #print(userDefineExceptions._InvalidInputError)
            self._ErrorMessage(_message="_DebugMessage Func: "+userDefineExceptions._InvalidInputError)
        else:
            try:
                logging.debug(_message)
            except:
                #return userDefineExceptions._UnkownError
                self._ErrorMessage(_message="_DebugMessage Func: " + userDefineExceptions._UnkownError)
    def test(self):
        logging.debug('damn, a bug')
        logging.info('something to remember')
        logging.warning('that\'s not right')
        logging.error('foobar')

class _ModuleManageWidget(QWidget):

    send_ModuleName_signal = pyqtSignal(str)

    def __init__(self, moduleList=None):
        super().__init__()
        self.mouduleList = moduleList
        self.initUI()

    def initUI(self):
        createButton = QPushButton("Create",self)
        selectButton = QPushButton("Select",self)

        createButton.clicked.connect(self.on_createBox_accepted)
        selectButton.clicked.connect(self.on_selectBox_accepted)

        self.manageListWidget = QListWidget()

        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(createButton)
        hbox.addWidget(selectButton)
        # hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        # vbox.addLayout(setupBox)
        vbox.addWidget(self.manageListWidget)
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        # vbox.addStretch(1)


        self.moduleListshow()
        self.setLayout(vbox)

        self.setWindowTitle('Module Managemenet')
        self.setGeometry(300,300,500,500)
        self.show()

    def moduleListshow(self):
        for module in self.mouduleList:
            self.manageListWidget.addItem(QListWidgetItem(module))

    def on_selectBox_accepted(self):
        try:
            self.send_ModuleName_signal.emit(self.manageListWidget.currentItem().text())        #Current Module Name emit!!
        except:
            print("no module is selected")
        self.destroy()

    def on_createBox_accepted(self):
        pass

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_selectBox_accepted()
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.destroy()
#
# class _CustomFileDialog(QFileDialog):
#     def __init__(self):
#         super().__init__(QFileDialog)
#
#         self.initUI()
#
#     def initUI(self):
#         pass

class _ThreadClassForPGbar(QThread):
    countChanged = pyqtSignal(int)
    update = pyqtSignal(int)
    def __init__(self, parent = None):
        QThread.__init__(self)
        self._name = None
        self._cancel = 'cancel'
        self._min = 0
        self._max = 0
        self.timeLimit = 100000
        self.countChanged.connect(self.updateValue)
    def run(self):
        count = 0
        print('Thread Run!')
        while count < self.timeLimit:
            count += 1
            time.sleep(1)
            print('signal Emit')
            self.update.emit(count)

    def updateValue(self, val):
        print('setValueFcnIn,',val)
        self.qpd.setValue(val)
        print(val)

class _ThreadWorker(QObject):
    signal_progress = pyqtSignal(int)
    timeLimit = 10000
    def doWork(self):
        count = 0
        print('work Start')
        while count < self.timeLimit:
            count += 1
            time.sleep(1)
            print('send signal')
            self.signal_progress.emit(count)

class _Progress(QProgressBar):
    def __init__(self,parent=None):
        super(_Progress, self).__init__(parent)
        self.setValue(0)
        self.setMaximum(0)
        self.setMinimum(0)
        self.thread = _ThreadClassForPGbar(self)

        #self.thread.started.connect(self.updateZero)
        self.thread.update.connect(self.update)
        self.thread.finished.connect(self.close)

        self.thread.start()


    def updateZero(self):
        self.setValue(0)

    def update(self,val):
        self.setValue(val)

class _FlatteningCell(QWidget):

    send_flattendict_signal = pyqtSignal(dict)
    # send_ok_signal = pyqtSignal()

    def __init__(self,  _hierarchydict):
        self.grouping = False
        try:
            sys.path.append('..\VariableSuggestion-git')
            import topAPI
            # topAPI.gds2generator.CellInspector()
            self.grouping = True
            self.inspector = topAPI.gds2generator.CellInspector()
        except:
            import traceback
            traceback.print_exc()
        super().__init__()
        self.loop_obj = QEventLoop()
        self._hdict = _hierarchydict
        self.model = QTreeWidget()
        self.model.setColumnCount(4)
        self.model.setHeaderLabels(['Design Object', 'Cell Name', 'Flatten Option', 'Generator Name'])
        self.itemlist = list()
        self.combolist = list(generator_model_api.class_dict.keys())
        self.initUI()

    def initUI(self):
        self.okButton = QPushButton("OK",self)
        self.okButton.clicked.connect(self.loop_obj.quit)

        top_cell = list(self._hdict.keys())

        top_item = QTreeWidgetItem(top_cell)


        self.loop(top_item, self._hdict[top_cell[0]], True)

        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(self.okButton)

        vbox = QVBoxLayout()
        vbox.addWidget(self.model)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setWindowTitle('SRef Flattening Window')
        self.setGeometry(300,300,900,500)
        self.show()

    def ok_button_accepted(self):

        self.loop_obj.exec_()

        _flatten_dict = dict()

        for item in self.itemlist:
            if self.model.itemWidget(item, 2).checkState() == 2:
                _flatten_dict[item.text(0) + '/' + item.text(1)] = None
            else:
                _flatten_dict[item.text(0) + '/' + item.text(1)] = self.model.itemWidget(item, 3).currentText()

        return _flatten_dict


    def loop(self, parent_item, parent_dict, isTop):
        for key in parent_dict:
            if parent_dict[key] is None:
                design_object, cell_name = self.slice(key)
                item = QTreeWidgetItem(parent_item, [design_object])
                item.setText(1, cell_name)
                self.itemlist.append(item)
            else:
                design_object, cell_name = self.slice(key)
                item = QTreeWidgetItem(parent_item,[design_object])
                item.setText(1, cell_name)
                self.itemlist.append(item)
                self.loop(item, parent_dict[key], False)
            self.modifyBraches(item, cell_name)

        if isTop == True:
            self.model.insertTopLevelItem(0, parent_item)

    def slice(self, subcellname):
        slash = subcellname.find('/')
        design_object = subcellname[:slash]
        cell_name = subcellname[slash+1:]

        return design_object, cell_name

    def modifyBraches(self, item, cn):
        cell_name = QLabel(cn)

        check = QCheckBox()
        check.setText(item.text(1))

        combo = QComboBox()
        combo.addItems(self.combolist)

        check.setText('OFF')
        combo.setEnabled(True)

        if self.grouping:
            module_name = self.inspector.convert_pcell_name_to_generator_name(item.text(0))
            print(module_name, item.text(0))
            module_index = combo.findText(module_name)
            if module_index != -1:
                combo.setCurrentIndex(module_index)

        check.stateChanged.connect(self.ActivateCombobox)

        # self.model.setItemWidget(item, 1, cell_name)
        self.model.setItemWidget(item, 2, check)
        self.model.setItemWidget(item, 3, combo)

    def ActivateCombobox(self, state):
        item = self.model.currentItem()
        siblingcheckbox = self.model.itemWidget(item, 2)
        siblingcombobox = self.model.itemWidget(item, 3)

        if state == 2:
            siblingcheckbox.setText('ON')
            siblingcombobox.setEnabled(False)
        else:
            siblingcheckbox.setText('OFF')
            siblingcombobox.setEnabled(True)

class ComboDelegate(QItemDelegate):
    def __init__(self,parent,create_fcn_list):
        super(ComboDelegate, self).__init__(parent)
        self.create_fcn_list = create_fcn_list

    def createEditor(self, parent: QWidget, option: 'QStyleOptionViewItem', index: QModelIndex) -> QWidget:
        combo_box = QComboBox(parent)
        # row = index.row()
        for fcn_name in self.create_fcn_list:
            combo_box.addItem(fcn_name)
        return combo_box

    def setEditorData(self, editor: QWidget, index: QModelIndex) -> None:
        current_text = index.data(Qt.EditRole)
        combo_idx = editor.findText(current_text)
        if combo_idx >= 0 :
            editor.setCurrentIndex(combo_idx)

    def setModelData(self, editor: QWidget, model: QAbstractItemModel, index: QModelIndex) -> None:
        model.setData(index, editor.currentText(), Qt.EditRole)
    # def setModelData(self, editor: QWidget, model: QtCore.QAbstractItemModel, index: QtCore.QModelIndex) -> None:
    #     model.setData(index,editor.currentText())
    #
    # def setEditorData(self, editor: QWidget, index: QtCore.QModelIndex) -> None:
    #     text = index.model().data(index).toString()
    #     combo_idx = comboitems

# class CheckboxDelegate(QStyledItemDelegate):
#     def __init__(self):
#         super(CheckboxDelegate, self).__init__()
#
#     def paint(self):

def get_id_return_module(id : str, type : str, moduleDict):
    """
    :param id:
    :param type: '_DesignParameter' or '_DesignConstraint'
    :return:
    """
    module = id
    while 1:
        module = module[:-1]
        if module in moduleDict:
            return module