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


class VariableSetupWindow(QWidget):

    send_BoundarySetup_signal = pyqtSignal(VisualizationItem._VisualizationItem)
    send_BoundaryDesign_signal = pyqtSignal(dict)
    send_Destroy_signal = pyqtSignal(str)
    send_Warning_signal = pyqtSignal(str)
    send_DestroyTmpVisual_signal = pyqtSignal(VisualizationItem._VisualizationItem)

    def __init__(self,variable_obj):
        super().__init__()
        self.height(500)
        self.width(300)
        self.initUI()

        if variable_obj == None:
            pass
            # self.visualItem = VisualizationItem._VisualizationItem()
            # self._DesignParameter = dict(
            #     _Layer= None,
            #     _DesignParametertype = 1,
            #     _XYCoordinates = [],
            #     _XWidth = None,
            #     _YWidth = None,
            #     _Ignore = None,
            #     _DesignParameterName = None
            #
            #     )
        else:
            # self._DesignParameter = BoundaryElement._ItemTraits
            self.updateUI()


    def initUI(self):
        self.variable_type_input = QComboBox()
        comboItemList = self._ASTapi.stmtList
        self.variable_type_input.addItems(comboItemList)
        self.variable_type_input.currentIndexChanged.connect(self.updateUI)


        okButton = QPushButton("OK",self)
        cancelButton = QPushButton("Cancel",self)

        okButton.clicked.connect(self.on_buttonBox_accepted)
        cancelButton.clicked.connect(self.cancel_button_accepted)

        self.setupVboxColumn1 = QVBoxLayout()
        self.setupVboxColumn2 = QVBoxLayout()
        setupBox = QHBoxLayout()


        self.setupVboxColumn1.addWidget(QLabel("_type"))

        self.setupVboxColumn2.addWidget(self.variable_type_input)


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

        currentClassName = self.variable_type_input.currentText() # like: If, While, Number ,...
        tmpObj = self._ASTapi._createASTwithName(currentClassName)
        strList = list(tmpObj._fields)
        self.addQLabel(strList)
        self.addQLine(len(strList))


        if self.variable_type_input.currentText() == "pyCode":
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
        _ASTtype = self.variable_type_input.currentText()
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
            self.send_Destroy_signal.emit('cw')
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.destroy()
            self.send_Destroy_signal.emit('cw')
    def updateUIvalue(self):
        try:
            type = self._ParseTree['_type']
            typeIndex = self.variable_type_input.findText(type)
            if typeIndex != -1:
                self.variable_type_input.setCurrentIndex(typeIndex)
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

    def cancel_button_accepted(self):
        self.destroy()
    def on_buttonBox_accepted(self):
        for XY in self.XYdictForLineEdit:
            if not XY.text():
                break
            else:
                try:
                    X = int(XY.text().split(',')[0])
                    Y = int(XY.text().split(',')[1])
                    self._DesignParameter['_XYCoordinates']=[[X+float(self.width_input.text())/2,Y+float(self.height_input.text())/2]]
                    # self._DesignParameter['_XYCoordinatesForDisplay'] = [[X,Y]]
                except:
                    self.warning = QMessageBox()
                    self.warning.setIcon(QMessageBox.Warning)
                    self.warning.setText("Unvalid XY Coordinates")
        pass

        try:
            self._DesignParameter['_DesignParameterName'] = self.name_input.text()
            if self._DesignParameter['_DesignParameterName'] == '':
                raise NotImplementedError
            self._DesignParameter['_XWidth'] = float(self.width_input.text())
            self._DesignParameter['_YWidth'] = float(self.height_input.text())
            self._DesignParameter['_Layer'] = self.layer_input.currentText()
            self.send_BoundaryDesign_signal.emit(self._DesignParameter)
            self.destroy()
        except:
            self.send_Warning_signal.emit("Invalid Design Parameter Input")     #log message
            self.warning = QMessageBox()
            self.warning.setText("Invalid design parameter or Name")
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
            self.send_Destroy_signal.emit('bw')
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.destroy()
            self.send_Destroy_signal.emit('bw')
