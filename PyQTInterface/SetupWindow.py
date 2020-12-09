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
from PyCodes import userDefineExceptions
from PyCodes import EnvForClientSetUp
from PyCodes import QTInterfaceWithAST


import re, ast, time

debugFlag = True

class _BoundarySetupWindow(QWidget):

    send_BoundarySetup_signal = pyqtSignal(VisualizationItem._VisualizationItem)
    send_BoundaryDesign_signal = pyqtSignal(dict)
    send_Destroy_signal = pyqtSignal()
    send_Warning_signal = pyqtSignal(str)
    send_DestroyTmpVisual_signal = pyqtSignal(VisualizationItem._VisualizationItem)

    def __init__(self,BoundaryElement= None):
        super().__init__()
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
                _DesignParameterName = None

                )
        else:
            # self.visualItem = BoundaryElement
            self._DesignParameter = BoundaryElement._ItemTraits
            self.updateUI()



    def initUI(self):
        okButton = QPushButton("OK",self)
        cancelButton = QPushButton("Cancel",self)

        okButton.clicked.connect(self.on_buttonBox_accepted)

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
        self.name_input.setText(self._DesignParameter['_DesignParameterName'])
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


    def on_buttonBox_accepted(self):
        for XY in self.XYdictForLineEdit:
            if not XY.text():
                break
            else:
                try:
                    X = int(XY.text().split(',')[0])
                    Y = int(XY.text().split(',')[1])
                    self._DesignParameter['_XYCoordinates']=[[X,Y]]
                    # self._DesignParameter['_XYCoordinatesForDisplay'] = [[X,Y]]
                except:
                    self.warning = QMessageBox()
                    self.warning.setIcon(QMessageBox.Warning)
                    self.warning.setText("Unvalid XY Coordinates")
        pass

        try:
            self._DesignParameter['_DesignParameterName'] = self.name_input.text()
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


    def AddBoundaryPointWithMouse(self,_MouseEvent):
        ##### When Click the point, adjust x,y locations #####
        if len(self.tmpXYCoordinates) == 0:
            self.tmpXYCoordinates.append([_MouseEvent.scenePos().toPoint().x(),_MouseEvent.scenePos().toPoint().y()])

        else:
            self.tmpXYCoordinates.append([_MouseEvent.scenePos().toPoint().x(),_MouseEvent.scenePos().toPoint().y()])

            xdistance = abs(self.tmpXYCoordinates[-1][0] - self.tmpXYCoordinates[-2][0])
            ydistance = abs(self.tmpXYCoordinates[-1][1] - self.tmpXYCoordinates[-2][1])
            origin = [min(self.tmpXYCoordinates[-1][0],self.tmpXYCoordinates[-2][0]),min(self.tmpXYCoordinates[-1][1],self.tmpXYCoordinates[-2][1])]
            self.tmpXYCoordinates.pop(0)

            self._DesignParameter['_Width'] = xdistance
            self._DesignParameter['_Height'] = ydistance
            self.width_input.setText(str(self._DesignParameter['_Width']))
            self.height_input.setText(str(self._DesignParameter['_Height']))
            self.XYdictForLineEdit[0].setText(str(origin[0])+','+str(origin[1]))

        self._DesignParameter['_Layer'] = self.layer_input.currentText()
        self.visualItem._XYCoordinatesForDisplay = self._DesignParameter['_XYCoordinates']

        self.visualItem.updateTraits(self._DesignParameter)
        self.send_BoundarySetup_signal.emit(self.visualItem)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_buttonBox_accepted()
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.destroy()


class _PathSetupWindow(QWidget):

    send_PathSetup_signal = pyqtSignal(VisualizationItem._VisualizationItem)
    send_PathDesign_signal = pyqtSignal(dict)
    # send_Destroy_signal = pyqtSignal("PyQt_PyObject")
    send_Destroy_signal = pyqtSignal()
    send_DestroyTmpVisual_signal = pyqtSignal(VisualizationItem._VisualizationItem)

    def __init__(self, PathElement = None):
        super().__init__()
        self.initUI()

        if PathElement is None:
            self._DesignParameter = dict(
                    _DesignParameterName = None,
                    _Layer = None,
                    _DesignParametertype = 2,
                    _XYCoordinates = [],
                    _Width = None,
                    _Height = None,
                    _Color = None,
                    _ItemRef = None, #Reference Of VisualizationItem

                )
            self.visualItem = VisualizationItem._VisualizationItem()
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
        self.name_input.setText(self._DesignParameter['_DesignParameterName'])
        self.width_input.setText(str(self._DesignParameter['_Width']))
        layerIndex = self.layer_input.findText(self._DesignParameter['_Layer'])
        if layerIndex != -1:
            self.layer_input.setCurrentIndex(layerIndex)
        for i in range(len(self._DesignParameter['_XYCoordinates'])):
            CurrentEditPointNum = len(self.XYdictForLineEdit)-2
            displayString= str(self._DesignParameter['_XYCoordinates'][0][i][0])+','+ str(self._DesignParameter['_XYCoordinates'][0][i][1])
            self.XYdictForLineEdit[CurrentEditPointNum].setText(displayString)
            self.UpdateXYwidget()



    def on_buttonBox_accepted(self):
        self._DesignParameter['_DesignParameterName'] = self.name_input.text()
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
                    self._DesignParameter['_XYCoordinates'][0].append([X,Y])
                    # self._DesignParameter['_XYCoordinatesForDisplay'].append([X,Y])

                except:
                    self.warning = QMessageBox()
                    self.warning.setIcon(QMessageBox.Warning)
                    self.warning.setText("Unvalid XY Coordinates")
        pass

        self.send_DestroyTmpVisual_signal.emit(self.visualItem)
        self.send_PathDesign_signal.emit(self._DesignParameter)
        self.send_Destroy_signal.emit()
        pass



    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_buttonBox_accepted()
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.destroy()

    def AddPathPointWithMouse(self,_MouseEvent):
        # print(self._DesignParameter)

        ##### When Click the point, adjust x,y locations #####
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
        self.send_PathSetup_signal.emit(self.visualItem)




    def UpdateXYwidget(self):
        CurrentPointNum = len(self.XYdictForLineEdit)
        NewPointNum = CurrentPointNum + 1
        LabelText = "XY" + str(NewPointNum)

        self.XYdictForLabel.append(QLabel(LabelText))
        self.XYdictForLineEdit.append(QLineEdit())

        self.setupVboxColumn1.addWidget(self.XYdictForLabel[-1])
        self.setupVboxColumn2.addWidget(self.XYdictForLineEdit[-1])

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
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.destroy()

class _SRefSetupWindow(QWidget):

    send_SRefSetup_signal = pyqtSignal(VisualizationItem._VisualizationItem)
    send_SRefDesign_signal = pyqtSignal(dict)
    send_Destroy_signal = pyqtSignal()
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
                _DesignParameterName = None

                )
        else:
            # self.visualItem = BoundaryElement
            self._DesignParameter = SRefElement._ItemTraits
            self.updateUI()



    def initUI(self):
        okButton = QPushButton("OK",self)
        cancelButton = QPushButton("Cancel",self)

        okButton.clicked.connect(self.on_buttonBox_accepted)

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
        self.name_input.setText(self._DesignParameter['_DesignParameterName'])
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


    def on_buttonBox_accepted(self):

        try:
            self._DesignParameter['_DesignParameterName'] = self.name_input.text()
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
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.destroy()

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

class _ConstraintSetupWindowCUSTOM(QWidget):

    send_STMT_signal = pyqtSignal(dict)
    send_CUSTOM_signal = pyqtSignal("PyQt_PyObject")

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
    def on_buttonBox_accepted(self):
        _ASTtype = self.type_input.currentText()
        _ASTobj = self._ASTapi._create_custom_ast_with_name(_ASTtype)
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

        self.send_CUSTOM_signal.emit(_ASTobj)
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

class _ConstraintSetupWindowPyCode(QWidget):

    send_PyCode_signal = pyqtSignal(str)

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

class _SelectedDesignListWidget(QListWidget):

    send_UpdateDesignParameter_signal = pyqtSignal(dict)
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

        for storedItem in self.itemDict:
            self.itemDict[storedItem].setSelected(False)

        self.blockSignals(True)
        self.clear()
        self.itemDict.clear()
        self.idDict.clear()
        self.blockSignals(False)


        for item in _items:
            if type(item) == VisualizationItem._RectBlock:
                continue
            elif item._clickFlag == False:
                continue

            tmpName = item._ItemTraits['_DesignParameterName']
            # tmpName = item._DesignParameterName
            self.itemDict[tmpName] = item
            self.idDict[tmpName] = item._ItemTraits['_id']
            item.setSelected(True)
            print(item.isSelected())

            if not self.findItems(tmpName,Qt.MatchExactly):     #Check whether it is empty or not
                self.addItem(QListWidgetItem(tmpName))

    def UpdateSelectedItem(self,current,previous):
        if previous is None:
            for storedItem in self.itemDict:
                self.itemDict[storedItem].setSelected(False)
        else:
            nameOfPrevious = previous.text()
            self.itemDict[nameOfPrevious].setSelected(False)

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
            pass

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
    send_SendASTDict_signal = pyqtSignal(list)
    send_SendSTMT_signal = pyqtSignal(dict)
    send_SendID_signal = pyqtSignal(str)
    send_SendCopyConstraint_signal = pyqtSignal(QTInterfaceWithAST.QtDesinConstraint)
    send_RootDesignConstraint_signal = pyqtSignal(str)
    send_RecieveDone_signal = pyqtSignal()
    send_RequesteDesignConstraint_signal = pyqtSignal()



    originalKeyPress = QTreeView.keyPressEvent

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

    def initUI(self,type):
        self.model = _ConstraintModel()
        if type == "Hierarchy":
            self.model.setHeaderData(0,Qt.Horizontal,"Constraint Container(Hierarchy)")
        else:
            self.model.setHeaderData(0,Qt.Horizontal,"Constraint Container(Floating)")
        self.model.setHeaderData(1,Qt.Horizontal,"Constraint ID")
        self.model.setHeaderData(2,Qt.Horizontal,"Constraint Type")
        self.model.setHeaderData(3,Qt.Horizontal,"Value")

        self.setModel(self.model)

        self.debugType = type

    def createNewConstraintAST(self,_id , _parentName, _DesignConstraint):
        self._DesignConstraintFromQTobj = _DesignConstraint
        self.model.createNewColumnWithID(_id=_id, _parentName=_parentName, _DesignConstraint = _DesignConstraint)


    def UpdateSelectedItem(self, item):
        if item == None:
            pass
        else:
            constraint = self.model._ConstraintDict[item.text()]
            self.cw = _ConstraintSetupWindow(constraint._ParseTree)
            self.cw.show()


    def mouseDoubleClickEventLegacy(self, QMouseEvent):
        try:                                                                                                    #0 : placeholder, #1 : ID, #2: ConstraintRealType, #3: value
            item = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(1))     #ID
            itemName = item.text()
            try:
                valueItem = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(3))    #Constraint
                value = valueItem.text()
            except:
                value = None

            try:
                #if valueItem != '*' and not (itemName in self.itemToASTDict) and itemName != None:
                if value == None and itemName != None:
                    updateDict = dict()
                    updateDict['_id'] = itemName
                    self.itemToASTDict[itemName] = None
                    self.send_UpdateDesignConstraint_signal.emit(updateDict)
            except:
                print('debug: value:',value,valueItem)



            if self.currentIndex().parent().isValid():
                # self.model.updatechildValue2Constraint(self.currentIndex().parent())
                updateDict = self.model.returnChildValueForUpdate(self.currentIndex().parent())
                motherModuleItem = self.model.itemFromIndex(self.currentIndex().parent().siblingAtColumn(1))
                motherName = motherModuleItem.text()
                if updateDict['_id'] == None:
                    updateDict['_id'] = motherName
            else:
                # self.model.updatechildValue2Constraint(self.currentIndex())
                updateDict = self.model.returnChildValueForUpdate(self.currentIndex())
                updateDict['_id'] = itemName

            #############AST################
            #update mouse double click --> send update value to DC
            # DC update check --> send DC to Model
            # Model refresh ITEM


            self.send_UpdateDesignConstraint_signal.emit(updateDict)


            self.refreshItem(self.currentIndex())


        except:
            print("Value Update Fail!")

    def mouseDoubleClickEvent(self, QMouseEvent):

        ####################double click update flow#######################
        # 1> same field value find ! and update to Constraint  (If class is not constraint case only)
        # 2> If class is constraint : it refresh sub-hierarchy value.
        ################# 3rd step is Unnecessary ########## 3> If class has parent : it update same-hierarchy value for parent
        ###################################################################
        #0 : placeholder, #1 : ID, #2: ConstraintRealType, #3: value


        try:
            ###Step 1 update value#####################################
            itemIDitem = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(1))     #ID
            itemID = itemIDitem.text()
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

                self.updateDesginConstraintWithSTR(Module=motherModuleName,Id=motherID,Field =placeHolder ,StringValue=value)

            ###Step 2 sub-hierarchy refresh#####################################            #To expand unseen contents <Constraint Case>
            if moduleName in self._DesignConstraintFromQTobj:
                if itemID in self._DesignConstraintFromQTobj[moduleName]:
                    self.refreshItem(self.currentIndex())
                else:
                    print('Warning during mouseDoubleClickEvent, Valid module name ({}), but invalid ID ({})'.format(moduleName,itemID))

            ###Step 3 sub-hierarchy refresh for placeholder's children #####################################    #To expand unseen contents <value = *, Case>
            if self.currentIndex().parent().isValid():  # Sub-hierarchy case        Do nothing??
                self.refreshItem(self.currentIndex())

        except:
            print("Value Update Fail!")


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


    def removeItem(self,item):
        if self.model.indexFromItem(item).parent().isValid():
            parentIndex = self.model.indexFromItem(item).parent()
            self.model.removeRow(item.row(),parentIndex)
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
            self.warning.setText("Only Constraint Can be moved!")
            self.warning.show()

    def removeCurrentIndexItem(self):
        if self.removeFlag == False:
            return

        selectedItem =self.model.itemFromIndex(self.currentIndex().siblingAtColumn(1))
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


                #updateDict[motherType] = originalDesignValues
                #updateDict['_id'] = grandParentName
                #self.send_UpdateDesignConstraint_signal.emit(updateDict)



#            #I need to make restoreItem #
#            removeID = selectedItem.text()
#            if removeID in self.itemToASTDict:
#                self.refreshItem(self.currentIndex().parent())
#                self.removeItem(selectedItem)
#                # del self.itemToASTDict[removeID]
#            else:
#                print('InValid Remove Request')

            #######################################################################IF THERE IS Hierarchy of Remove Item --> I have to update itemToDesignConstraintDict also!!!!!!!!!!!!!!!!!!!!!!!!!!################################################
            # I am not sure whether it is necessary or not
            # self.removeHierarchyConstraintfromDictionary(self.itemToDesignConstraintDict[removeName])
            # self.model.updateConstraintDictFromView(self.itemToDesignConstraintDict)

        else:
            self.removeItem(selectedItem)


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
                self.send_RequesteDesignConstraint_signal.emit()
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
                self.send_RecieveDone_signal.emit()
                self.send_RootDesignConstraint_signal.emit(_id)
            else:
                ####### At first check whether it is possible to modify or not ####### (In case of Constraint itself, you cannot modify!! only parsetrees are possible to modify
                #######Case2: If it is constraint. < cannot change>
                constraintItem = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(1))
                constraintName = constraintItem.text()
                constraintModule = re.sub(r'\d','',constraintName)
                if constraintModule in self._DesignConstraintFromQTobj:
                    print("It isn't allow to change constraint")
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
                        self.send_RequesteDesignConstraint_signal.emit()
                    placeHolder = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(0)).text()
                    self.updateDesginConstraintWithSTR(Module=motherModule, Id=motherId, Field=placeHolder, StringValue=_id)
                    #_itemType = self._DesignConstraintFromQTobj[motherModule][motherId]._ast[placeHolder]._type
                    currentItemId = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(3))
                    #currentItemType = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(2))
                    currentItemId.setText('*')
                    #currentItemType.setText(_itemType)
                index = self.currentIndex()

                #try:
                self.refreshItem(index)
                print("debug:receiveDone")
                self.send_RecieveDone_signal.emit()
                #except:
                 #   print("Somehow failed Refresh")
                  #  pass

    def refreshItem(self,itemIndex):  #Refresh Design Constraint

        indexIDItem = self.model.itemFromIndex(itemIndex.siblingAtColumn(1))
        valueItem = self.model.itemFromIndex(itemIndex.siblingAtColumn(3))
        indexID = indexIDItem.text()
        value = valueItem.text()
        tmpModuel =  re.sub(r'\d','',indexID)
        self.send_RequesteDesignConstraint_signal.emit()

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
            motherModule = re.sub(r'\d','',motherName)
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
        elif QKeyEvent.key() == Qt.Key_Delete:
            self.removeFlag = True
            self.removeCurrentIndexItem()
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


class _ConstraintModel(QStandardItemModel):
    def __init__(self):
        QStandardItemModel.__init__(self)
        self._DesignConstraintFromQTobj = None
        self._ConstraintNameList = []
        self._ConstraintDict = dict()
        self._ConstraintItem = dict()
        self._Root = None
        self.setColumnCount(4)
        # self.testInitial()

    def readConstraint(self,rootConstraint):
        # rootConstraint = QTDesignConstraint
        rootType = rootConstraint._type
        rootName = rootConstraint._id
        # rootValue = rootConstraint._ParseTree

        self.setItem(0,0,QStandardItem(rootType))
        self.setItem(0,1,QStandardItem(rootName))
        # self.setItem(0,2,rootValue)

    def createNewColumn(self,_STMTList,rc=None):
        for stmt in _STMTList:
            _type = stmt['_type']
            tmpConstraintType = QStandardItem(_type)
            constraintName = stmt['_id']
            self._ConstraintItem[constraintName] =tmpConstraintType

            if rc == None:
                rc= self.rowCount()

            self.insertRow(rc,[tmpConstraintType,QStandardItem(constraintName),tmpConstraintType])


            self._ConstraintNameList.append(constraintName)
            self.readParseTree(tmpConstraintType,_STMTList)

    def createNewColumnWithID(self,_id, _parentName, _DesignConstraint, rc = None):
        self._DesignConstraintFromQTobj = _DesignConstraint
        _type = self._DesignConstraintFromQTobj[_parentName][_id]._type
        tmpConstraintType = QStandardItem(_type)
        # self._ConstraintItem[_id] = tmpConstraintType

        if rc == None:
            rc = self.rowCount()


        self.insertRow(rc, [tmpConstraintType, QStandardItem(_id), QStandardItem(_type),QStandardItem() ])
        # Item Field:  0-> PlaceHolder Type , 1-> _id , 2-> Content Type , 3 -> value
        #self._ConstraintNameList.append(constraintName)
        self.readParseTreeWtihAST(motherItem=tmpConstraintType, _AST= _DesignConstraint[_parentName][_id]._ast)

    def updateRowChild(self,_STMTLIst,rc=None,motherIndex=None):
        if motherIndex == None:                                             #When There is no parent  (It Creats a New Row)
            tmpConstraintType = QStandardItem(_STMTLIst['_type'])
            constraintName = _STMTLIst['_id']
            self._ConstraintItem[constraintName] = tmpConstraintType

            if rc == None:
                rc= self.rowCount()


            self.insertRow(rc,[tmpConstraintType,QStandardItem(constraintName)])

            self._ConstraintNameList.append(constraintName)
            self._ConstraintDict[constraintName] = _STMTLIst
            self.readParseTree(tmpConstraintType,_STMTLIst)
        else:                                                               #When there is a parent
            if motherIndex.isValid() == False:
                self.warning=QMessageBox()
                self.warning.setText("Mother Index is invalid")
                self.warning.show()
                return

            item = self.itemFromIndex(motherIndex.siblingAtColumn(0))

            self.readParseTree(item,_STMTLIst)

    def updateRowChildWithAST(self,_DesignConstraint,rc=None,motherIndex=None):
        if motherIndex == None:                                             #When There is no parent  (It Creats a New Row)
            tmpConstraintType = QStandardItem(_DesignConstraint._type)
            constraintName = _DesignConstraint._id

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
        print("Start Reading ParseTree")
        print("Mother Item: ",motherItem.text())

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
            if debugFlag == True:
                print("Start Reading ParseTree with AST")
                print("Mother Item: ",motherItem.text())

            for field in _AST._fields:
                childVariable = _AST.__dict__[field]
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
                elif type(childVariable) == list:     #Compound STMT
                    _placeholder = field
                    _id = ''
                    _constraintRealType = str(type(childVariable))
                    _constraintValue = '*'
                else:
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
                    checkChild = None
                    continue


                tmpA = QStandardItem(_placeholder)
                tmpB = QStandardItem(_id)
                tmpC = QStandardItem(_constraintRealType)
                tmpD = QStandardItem(_constraintValue)

                # tmpA.appendRow([QStandardItem("hi"),QStandardItem("test")])
                motherItem.appendRow([tmpA, tmpB, tmpC, tmpD])

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

        for childAST in _AST.__dict__[key]:   #### childConstraint is item in list!
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