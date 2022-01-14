import sys
import os
import platform
import warnings

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsView, QGraphicsScene, QGraphicsItem
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# from PyQTInterface  import LayerInfo
from PyQTInterface.layermap  import LayerReader
from PyQTInterface  import VisualizationItem
from PyQTInterface import calculator

from PyCodes import ASTmodule
from PyCodes import element_ast
from PyQTInterface.delegator import delegator
import logging
import copy
from PyCodes import userDefineExceptions
from PyCodes import EnvForClientSetUp
from PyCodes import QTInterfaceWithAST
import user_setup
from generatorLib import generator_model_api
from powertool import topAPI
import traceback
import re, ast, time, sys
from PyQTInterface.delegator import dpdc_delegator

debugFlag = True

class _BoundarySetupWindow(QWidget):

    send_BoundarySetup_signal = pyqtSignal(VisualizationItem._VisualizationItem)
    send_BoundaryDesign_signal = pyqtSignal(dict)
    send_design_message = pyqtSignal(delegator.DelegateMessage)
    send_Destroy_signal = pyqtSignal(str)
    send_Warning_signal = pyqtSignal(str)
    send_DestroyTmpVisual_signal = pyqtSignal(VisualizationItem._VisualizationItem)
    send_name_duplication_check_signal =pyqtSignal(str)

    def __init__(self,BoundaryElement= None):
        super().__init__()
        self.mouse = None
        self.click = 0
        self.initUI()
        self.name_check = True

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

        self.setWindowFlag(Qt.WindowStaysOnTopHint)

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
                # print("layerExpressionName:",layerExpressionName,_Layer[layerExpressionName][0],self._DesignParameter['_LayerUnifiedName'])
                if _Layer[layerExpressionName][0] == self._DesignParameter['_LayerUnifiedName']:
                    self._DesignParameter['_LayerUnifiedName'] = str(layerExpressionName)
                    break

            # self._DesignParameter['_Layer'] =  _Layer2Name[_layerNumber]     #Layer Number             --> Convert Name to Number
            del _Layer
            layerIndex = self.layer_input.findText(self._DesignParameter['_LayerUnifiedName'])
        else:
            layerIndex = self.layer_input.findText(self._DesignParameter['_LayerUnifiedName'])
        if layerIndex != -1:
            self.layer_input.setCurrentIndex(layerIndex)
        #setCurrentIndex
        #findText
        # self.

    def cancel_button_accepted(self):
        self.send_Destroy_signal.emit('bw')
        if 'visualItem' in self.__dict__:
            self.send_DestroyTmpVisual_signal.emit(self.visualItem)
        self.deleteLater()

    def set_name_check(self, flag):
        self.name_check = flag

    def on_buttonBox_accepted(self):
        self.send_name_duplication_check_signal.emit(self.name_input.text())
        if self.name_check == False:
            self.warning = QMessageBox()
            self.warning.setIcon(QMessageBox.Warning)
            self.warning.setText("Name duplication is detected!")
            self.warning.show()
            return None

        for XY in self.XYdictForLineEdit:
            if not XY.text():
                break
            else:
                try:
                    X = float(XY.text().split(',')[0])
                    Y = float(XY.text().split(',')[1])
                    self._DesignParameter['_XYCoordinates']=[[X,Y]]
                except:
                    # traceback.print_exc()
                    self.warning = QMessageBox()
                    self.warning.setIcon(QMessageBox.Warning)
                    self.warning.setText("Invalid XY Coordinates")

        try:
            self._DesignParameter['_ElementName'] = self.name_input.text()
            if self._DesignParameter['_ElementName'] == '':
                raise NotImplementedError
            self._DesignParameter['_XWidth'] = float(self.width_input.text())
            self._DesignParameter['_YWidth'] = float(self.height_input.text())
            self._DesignParameter['_LayerUnifiedName'] = self.layer_input.currentText()
            self._DesignParameter['_Layer'] = None

            if 'visualItem' in self.__dict__:
                self.send_DestroyTmpVisual_signal.emit(self.visualItem)

            self.send_BoundaryDesign_signal.emit(self._DesignParameter)
            print(self._DesignParameter)
            message = delegator.DelegateMessage(arguments=[self._DesignParameter], target_fcn='create_qt_parameter')
            self.send_design_message.emit(message)
            self.click = 2
            self.deleteLater()

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

    def AddBoundaryPointWithMouse(self,xy):
        if self.click < 2:
            ##### When Click the point, adjust x,y locations #####
            if len(self.tmpXYCoordinates) == 0:
                self.tmpXYCoordinates.append(xy)

            else:
                self.tmpXYCoordinates.append(xy)

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

            self._DesignParameter['_LayerUnifiedName'] = self.layer_input.currentText()
            self._DesignParameter['_Layer'] = None

            if self._DesignParameter['_XWidth'] is None:
                self._DesignParameter['_XWidth'] = 0
            if self._DesignParameter['_YWidth'] is None:
                self._DesignParameter['_YWidth'] = 0
            if self._DesignParameter['_XYCoordinates'] == []:
                self._DesignParameter['_XYCoordinates'] = [xy]
            qt_dp = QTInterfaceWithAST.QtDesignParameter()
            for key, value in self._DesignParameter.items():
                qt_dp._setDesignParameterValue(key, value)
            qt_dp.update_unified_expression()

            self.visualItem.updateDesignParameter(qt_dp)
            self.send_BoundarySetup_signal.emit(self.visualItem)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_buttonBox_accepted()
            self.send_Destroy_signal.emit('bw')
        elif QKeyEvent.key() == Qt.Key_Escape:
            if 'visualItem' in self.__dict__:
                self.send_DestroyTmpVisual_signal.emit(self.visualItem)
            self.deleteLater()
            self.send_Destroy_signal.emit('bw')

    def mouseTracking(self, xy):
        if self.mouse is not None and self.click < 2:
            xdistance = abs(self.mouse[0] - xy[0])
            ydistance = abs(self.mouse[1] - xy[1])
            origin = [(self.mouse[0]+xy[0])/2, (self.mouse[1]+xy[1])/2]
            self._DesignParameter['_XWidth'] = xdistance
            self._DesignParameter['_YWidth'] = ydistance
            self._DesignParameter['_XYCoordinates'] = [origin]
            self._DesignParameter['_LayerUnifiedName'] = self.layer_input.currentText()
            self._DesignParameter['_Layer'] = None
            qt_dp = QTInterfaceWithAST.QtDesignParameter()
            for key, value in self._DesignParameter.items():
                qt_dp._setDesignParameterValue(key, value)
            qt_dp.update_unified_expression()
            self.visualItem.updateDesignParameter(qt_dp)
            self.visualItem.setFlag(QGraphicsItemGroup.ItemIsSelectable,False)
            self.send_BoundarySetup_signal.emit(self.visualItem)

    def clickCount(self, xy):
        self.mouse = xy
        self.click += 1


class _PolygonSetupWindow(QWidget):

    send_PolygonSetup_signal = pyqtSignal(VisualizationItem._VisualizationItem)
    send_PolygonDesign_signal = pyqtSignal(dict)
    send_design_message = pyqtSignal(delegator.DelegateMessage)
    send_Destroy_signal = pyqtSignal(str)
    send_Warning_signal = pyqtSignal(str)
    send_DestroyTmpVisual_signal = pyqtSignal(VisualizationItem._VisualizationItem)
    send_name_duplication_check_signal =pyqtSignal(str)

    def __init__(self, PolygonElement = None):
        super().__init__()
        self.mouse = None
        self.click = 0
        self.initUI()
        self.name_check = True


        if PolygonElement is None:
            self._DesignParameter = dict(
                    _ElementName = None,
                    _Layer = None,
                    _DesignParametertype = 11,
                    _XYCoordinates = [],
                    _Color = None
                )
            self.visualItem = VisualizationItem._VisualizationItem()
            self.tmpDP = copy.deepcopy(self._DesignParameter)
            self.doubleClickEvent = False
        else:
            # self.visualItem = PolygonElement
            self.visualItem = VisualizationItem._VisualizationItem()
            self._DesignParameter = PolygonElement._ItemTraits
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
        layer = QLabel("Layer")
        self.XYdictForLabel.append(QLabel("XY1"))
        self.XYdictForLabel.append(QLabel("XY2"))

        self.name_input = QLineEdit()
        self.layer_input = QComboBox()
        self.XYdictForLineEdit.append(QLineEdit())
        self.XYdictForLineEdit.append(QLineEdit())

        _Layer = LayerReader._LayerMapping
        for LayerName in _Layer:
            if _Layer[LayerName][1] != None:       ## Layer is drawing
                if not 'PIN' in LayerName:
                    self.layer_input.addItem(LayerName)

        self.setupVboxColumn1 = QVBoxLayout()
        self.setupVboxColumn2 = QVBoxLayout()
        setupBox = QHBoxLayout()

        self.setupVboxColumn1.addWidget(name)
        self.setupVboxColumn1.addWidget(layer)
        self.setupVboxColumn1.addWidget(self.XYdictForLabel[0])
        self.setupVboxColumn1.addWidget(self.XYdictForLabel[1])


        self.setupVboxColumn2.addWidget(self.name_input)
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

        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.setWindowTitle('Polygon Setup Window')
        self.setGeometry(300,300,500,500)
        self.show()

    def updateUI(self):
        self.name_input.setText(self._DesignParameter['_ElementName'])
        layerIndex = self.layer_input.findText(self._DesignParameter['_LayerUnifiedName'])
        if layerIndex != -1:
            self.layer_input.setCurrentIndex(layerIndex)
        for i in range(len(self._DesignParameter['_XYCoordinates'][0])):
            CurrentEditPointNum = len(self.XYdictForLineEdit)-2
            displayString= str(self._DesignParameter['_XYCoordinates'][0][i][0])+','+ str(self._DesignParameter['_XYCoordinates'][0][i][1])
            self.XYdictForLineEdit[CurrentEditPointNum].setText(displayString)
            self.UpdateXYwidget()


    def cancel_button_accepted(self):
        self.send_DestroyTmpVisual_signal.emit(self.visualItem)
        self.send_Destroy_signal.emit('pow')
        self.deleteLater()

    def set_name_check(self, flag):
        self.name_check = flag

    def on_buttonBox_accepted(self):
        self.send_name_duplication_check_signal.emit(self.name_input.text())
        if self.name_check == False:
            self.warning = QMessageBox()
            self.warning.setIcon(QMessageBox.Warning)
            self.warning.setText("Name duplication is detected!")
            self.warning.show()
            return None
        try:
            self._DesignParameter['_ElementName'] = self.name_input.text()
            if self._DesignParameter['_ElementName'] == '':
                raise NotImplementedError
            self._DesignParameter['_LayerUnifiedName'] = self.layer_input.currentText()
            self._DesignParameter['_Layer'] = None
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

            self.send_PolygonDesign_signal.emit(self._DesignParameter)
            self.deleteLater()
            self.send_Destroy_signal.emit('pow')
        except:
            traceback.print_exc()
            self.warning = QMessageBox()
            self.warning.setIcon(QMessageBox.Warning)
            self.warning.setText("Invalid Name")
            self.warning.show()


    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_buttonBox_accepted()
            self.send_Destroy_signal.emit('pow')
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.deleteLater()
            self.send_Destroy_signal.emit('pow')

    def AddPolygonPointWithMouse(self,xy):
        if self.doubleClickEvent == False:
            ##### When Click the point, adjust x,y locations #####
            try:
                if len(self._DesignParameter['_XYCoordinates']) == 0:
                    self._DesignParameter['_XYCoordinates'].append([xy])
                else:
                    xdistance = abs(xy[0] - self._DesignParameter['_XYCoordinates'][0][-1][0])
                    ydistance = abs(xy[1] - self._DesignParameter['_XYCoordinates'][0][-1][1])

                    if xdistance < ydistance:
                        self._DesignParameter['_XYCoordinates'][0].append([self._DesignParameter['_XYCoordinates'][0][-1][0],xy[1]])
                    else:
                        self._DesignParameter['_XYCoordinates'][0].append([xy[0],self._DesignParameter['_XYCoordinates'][0][-1][1]])

                # self._DesignParameter['_XYCoordinates'].append([_MouseEvent.scenePos().toPoint().x(),_MouseEvent.scenePos().toPoint().y(),])

                CurrentEditPointNum = len(self.XYdictForLineEdit)-2
                XYstring = str(self._DesignParameter['_XYCoordinates'][0][-1][0]) + ',' + str(self._DesignParameter['_XYCoordinates'][0][-1][1])
                self.XYdictForLineEdit[CurrentEditPointNum].setText(XYstring)
                self.UpdateXYwidget()
            except:
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

    # def mouseTracking(self, xy):
    #     if self.mouse is not None:
    #         if self.doubleClickEvent == False:
    #             tmp_dp = copy.deepcopy(self._DesignParameter)
    #             if self.click == 0:
    #                 xdistance = abs(self.mouse.x() - xy[0])
    #                 ydistance = abs(self.mouse.y() - xy[1])
    #
    #                 if xdistance < ydistance:
    #                     tmp_dp['_XYCoordinates'] = [[self.mouse,[self.mouse[0],xy[1]]]]
    #                 else:
    #                     tmp_dp['_XYCoordinates'] = [[self.mouse,[xy[0],self.mouse[1]]]]
    #             else:
    #                 xdistance = abs(self._DesignParameter['_XYCoordinates'][0][-1][0] - xy[0])
    #                 ydistance = abs(self._DesignParameter['_XYCoordinates'][0][-1][1] - xy[1])
    #
    #                 if xdistance < ydistance:
    #                     if len(tmp_dp['_XYCoordinates'][0]) == 1:
    #                         tmp_dp['_XYCoordinates'] = [[[self._DesignParameter['_XYCoordinates'][0][-1][0],self._DesignParameter['_XYCoordinates'][0][-1][1]],[self._DesignParameter['_XYCoordinates'][0][-1][0],xy[1]]]]
    #                     else:
    #                         tmp_dp['_XYCoordinates'][0].append([[self._DesignParameter['_XYCoordinates'][0][-1][0],self._DesignParameter['_XYCoordinates'][0][-1][1]],[self._DesignParameter['_XYCoordinates'][0][-1][0],xy[1]]][-1])
    #                 else:
    #                     if len(tmp_dp['_XYCoordinates'][0]) == 1:
    #                         tmp_dp['_XYCoordinates'] = [[[self._DesignParameter['_XYCoordinates'][0][-1][0],self._DesignParameter['_XYCoordinates'][0][-1][1]],[xy[0],self._DesignParameter['_XYCoordinates'][0][-1][1]]]]
    #                     else:
    #                         tmp_dp['_XYCoordinates'][0].append([[self._DesignParameter['_XYCoordinates'][0][-1][0],self._DesignParameter['_XYCoordinates'][0][-1][1]],[xy[0],self._DesignParameter['_XYCoordinates'][0][-1][1]]][-1])
    #
    #             tmp_dp['_LayerUnifiedName'] = self.layer_input.currentText()
    #             tmp_dp['_type'] = 11
    #             qt_dp = QTInterfaceWithAST.QtDesignParameter(_type=2)
    #             for key, value in tmp_dp.items():
    #                 qt_dp._setDesignParameterValue(key, value)
    #             qt_dp.update_unified_expression()
    #             self.visualItem._ItemTraits['_XYCoordinates'] = self._DesignParameter['_XYCoordinates']
    #             self.visualItem.updateDesignParameter(qt_dp)
    #             self.send_PolygonSetup_signal.emit(self.visualItem)
    #             self.visualItem.setFlag(QGraphicsItemGroup.ItemIsSelectable,False)
    #
    # def clickCount(self, xy):
    #     self.mouse = xy
    #     self.click += 1
    #
    # def quitCreate(self, doubleClickEvent):
    #     self.doubleClickEvent = doubleClickEvent

class _PathSetupWindow(QWidget):

    send_PathSetup_signal = pyqtSignal(VisualizationItem._VisualizationItem)
    send_PathDesign_signal = pyqtSignal(dict)
    # send_Destroy_signal = pyqtSignal("PyQt_PyObject")
    send_Destroy_signal = pyqtSignal(str)
    send_DestroyTmpVisual_signal = pyqtSignal(VisualizationItem._VisualizationItem)
    send_name_duplication_check_signal =pyqtSignal(str)

    def __init__(self, PathElement = None):
        super().__init__()
        self.mouse = None
        self.click = 0
        self.initUI()
        self.name_check = True

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
            self.tmpDP = copy.deepcopy(self._DesignParameter)
            self.doubleClickEvent = False
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
        self.okButton = okButton

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
            if _Layer[LayerName][1] != None:       ## Layer is drawing
                if not 'PIN' in LayerName:
                    self.layer_input.addItem(LayerName)

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

        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.setWindowTitle('Path Setup Window')
        self.setGeometry(300,300,500,500)
        self.show()

    def updateUI(self):
        self.name_input.setText(self._DesignParameter['_ElementName'])
        self.width_input.setText(str(self._DesignParameter['_Width']))
        # if type(self._DesignParameter['_Layer']) == int:
        #     layernum2name = LayerReader._LayerNumber2CommonLayerName(LayerReader._LayerMapping)
        #     _tmplayer = layernum2name[str(self._DesignParameter['_Layer'])]
        #     layerIndex = self.layer_input.findText(_tmplayer)
        # else:
        layerIndex = self.layer_input.findText(self._DesignParameter['_LayerUnifiedName'])
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
        self.send_DestroyTmpVisual_signal.emit(self.visualItem)
        self.send_Destroy_signal.emit('pw')
        self.deleteLater()


    def set_name_check(self, flag):
        self.name_check = flag


    def on_buttonBox_accepted(self):
        self.send_name_duplication_check_signal.emit(self.name_input.text())
        if self.name_check == False:
            self.warning = QMessageBox()
            self.warning.setIcon(QMessageBox.Warning)
            self.warning.setText("Name duplication is detected!")
            self.warning.show()
            return None
        try:
            self._DesignParameter['_ElementName'] = self.name_input.text()
            if self._DesignParameter['_ElementName'] == '':
                raise NotImplementedError
            self._DesignParameter['_Width'] = self.width_input.text()
            self._DesignParameter['_LayerUnifiedName'] = self.layer_input.currentText()
            self._DesignParameter['_Layer'] = None
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
            self.send_PathDesign_signal.emit(self._DesignParameter)
            # self.deleteLater()
            self.deleteLater()
            self.send_Destroy_signal.emit('pw')
            pass
        except:
            traceback.print_exc()
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
            self.deleteLater()
            self.send_Destroy_signal.emit('pw')

    def AddPathPointWithMouse(self,xy):
        if self.doubleClickEvent == False:
            ##### When Click the point, adjust x,y locations #####
            try:
                if len(self._DesignParameter['_XYCoordinates']) == 0:
                    self._DesignParameter['_XYCoordinates'].append([xy])
                else:
                    xdistance = abs(xy[0] - self._DesignParameter['_XYCoordinates'][0][-1][0])
                    ydistance = abs(xy[1] - self._DesignParameter['_XYCoordinates'][0][-1][1])

                    if xdistance < ydistance:
                        self._DesignParameter['_XYCoordinates'][0].append([self._DesignParameter['_XYCoordinates'][0][-1][0],xy[1]])
                    else:
                        self._DesignParameter['_XYCoordinates'][0].append([xy[0],self._DesignParameter['_XYCoordinates'][0][-1][1]])

                # self._DesignParameter['_XYCoordinates'].append([_MouseEvent.scenePos().toPoint().x(),_MouseEvent.scenePos().toPoint().y(),])

                CurrentEditPointNum = len(self.XYdictForLineEdit)-2
                XYstring = str(self._DesignParameter['_XYCoordinates'][0][-1][0]) + ',' + str(self._DesignParameter['_XYCoordinates'][0][-1][1])
                self.XYdictForLineEdit[CurrentEditPointNum].setText(XYstring)
                self.UpdateXYwidget()
                self._DesignParameter['_Width'] = self.width_input.text()
                self._DesignParameter['_LayerUnifiedName'] = self.layer_input.currentText()
                self._DesignParameter['_type'] = 2
                qt_dp = QTInterfaceWithAST.QtDesignParameter(_type=2)
                for key, value in self._DesignParameter.items():
                    qt_dp._setDesignParameterValue(key, value)
                qt_dp.update_unified_expression()
                self.visualItem._ItemTraits['_XYCoordinates'] = self._DesignParameter['_XYCoordinates']
                self.visualItem.updateDesignParameter(qt_dp)
                self.visualItem.setFlag(QGraphicsItemGroup.ItemIsSelectable,False)
                self.send_PathSetup_signal.emit(self.visualItem)
            except:
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

    def mouseTracking(self, xy):
        if self.mouse is not None:
            if self.doubleClickEvent == False:
                tmp_dp = copy.deepcopy(self._DesignParameter)
                if self.click == 0:
                    xdistance = abs(self.mouse.x() - xy[0])
                    ydistance = abs(self.mouse.y() - xy[1])

                    if xdistance < ydistance:
                        tmp_dp['_XYCoordinates'] = [[self.mouse,[self.mouse[0],xy[1]]]]
                    else:
                        tmp_dp['_XYCoordinates'] = [[self.mouse,[xy[0],self.mouse[1]]]]
                else:
                    xdistance = abs(self._DesignParameter['_XYCoordinates'][0][-1][0] - xy[0])
                    ydistance = abs(self._DesignParameter['_XYCoordinates'][0][-1][1] - xy[1])

                    if xdistance < ydistance:
                        if len(tmp_dp['_XYCoordinates'][0]) == 1:
                            tmp_dp['_XYCoordinates'] = [[[self._DesignParameter['_XYCoordinates'][0][-1][0],self._DesignParameter['_XYCoordinates'][0][-1][1]],[self._DesignParameter['_XYCoordinates'][0][-1][0],xy[1]]]]
                        else:
                            tmp_dp['_XYCoordinates'][0].append([[self._DesignParameter['_XYCoordinates'][0][-1][0],self._DesignParameter['_XYCoordinates'][0][-1][1]],[self._DesignParameter['_XYCoordinates'][0][-1][0],xy[1]]][-1])
                    else:
                        if len(tmp_dp['_XYCoordinates'][0]) == 1:
                            tmp_dp['_XYCoordinates'] = [[[self._DesignParameter['_XYCoordinates'][0][-1][0],self._DesignParameter['_XYCoordinates'][0][-1][1]],[xy[0],self._DesignParameter['_XYCoordinates'][0][-1][1]]]]
                        else:
                            tmp_dp['_XYCoordinates'][0].append([[self._DesignParameter['_XYCoordinates'][0][-1][0],self._DesignParameter['_XYCoordinates'][0][-1][1]],[xy[0],self._DesignParameter['_XYCoordinates'][0][-1][1]]][-1])

                tmp_dp['_Width'] = self.width_input.text()
                tmp_dp['_LayerUnifiedName'] = self.layer_input.currentText()
                tmp_dp['_type'] = 2
                qt_dp = QTInterfaceWithAST.QtDesignParameter(_type=2)
                for key, value in tmp_dp.items():
                    qt_dp._setDesignParameterValue(key, value)
                qt_dp.update_unified_expression()
                self.visualItem._ItemTraits['_XYCoordinates'] = self._DesignParameter['_XYCoordinates']
                self.visualItem.updateDesignParameter(qt_dp)
                self.send_PathSetup_signal.emit(self.visualItem)
                self.visualItem.setFlag(QGraphicsItemGroup.ItemIsSelectable,False)




    def clickCount(self, xy):
        self.mouse = xy
        self.click += 1

    def quitCreate(self, doubleClickEvent):
        self.doubleClickEvent = doubleClickEvent

class _LoadSRefWindow(QWidget):

    send_DesignConstraint_signal = pyqtSignal("PyQt_PyObject")
    send_array_signal = pyqtSignal("PyQt_PyObject")
    send_destroy_signal = pyqtSignal(str)
    send_exported_sref_signal = pyqtSignal(str, dict)
    send_name_duplication_check_signal =pyqtSignal(str)

    def __init__(self, purpose = None, SRefElement = None):
        super().__init__()
        self.purpose = purpose
        self.create = False
        self.option = True
        self.par_valueForLineEdit = []
        self.par_button_for_cal = []
        self.paramDict = dict()
        self.initUI()
        self.name_check = True

        if SRefElement is None:
            self.create = True
            self.visualItem = VisualizationItem._VisualizationItem()
        elif purpose == 'array_load':
            self.create = True
            self.array_dict = SRefElement
            self.updateUI_for_array()
        else:
            self._DesignParameter = SRefElement._ItemTraits
            self.updateUI()

    def initUI(self):
        if self.purpose == 'main_load':
            self.name = QLabel("name")
        self.library = QLabel("library")
        self.class_name = QLabel("className")
        if self.purpose == 'main_load':
            self.XY = QLabel("XY")
        self.cal_fcn = QLabel("calculate_fcn")

        self.pars = QLabel("\nPARAMETERS")


        if self.purpose == 'main_load':
            self.name_input = QLineEdit()
        self.library_input = QComboBox()
        self.class_name_input = QLineEdit()
        if self.purpose == 'main_load':
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

        if self.purpose == 'main_load':
            self.setupVboxColumn1.addWidget(self.name)
        self.setupVboxColumn1.addWidget(self.library)
        self.setupVboxColumn1.addWidget(self.class_name)
        if self.purpose == 'main_load':
            self.setupVboxColumn1.addWidget(self.XY)
        self.setupVboxColumn1.addWidget(self.cal_fcn)

        if self.purpose == 'main_load':
            self.setupVboxColumn2.addWidget(self.name_input)
        self.setupVboxColumn2.addWidget(self.library_input)
        self.setupVboxColumn2.addWidget(self.class_name_input)
        if self.purpose == 'main_load':
            self.setupVboxColumn2.addWidget(self.XY_input)
        self.setupVboxColumn2.addWidget(self.cal_fcn_input)

        self.parVBox1 = QVBoxLayout()
        self.parVBox2 = QVBoxLayout()
        self.parVBox3 = QVBoxLayout()

        self.par_name = []
        self.par_value = []
        par_list = generator_model_api.class_function_dict[self.library_input.currentText()][self.cal_fcn_input.currentText()]
        for idx in range(len(par_list)):
            self.par_name.append(par_list[idx].name)
            self.par_value.append(par_list[idx].default)

            self.par_valueForLineEdit.append(QLineEdit())
            self.par_valueForLineEdit[-1].setText(str(self.par_value[-1]))

            cal_button = QPushButton()
            cal_button.setIcon(QIcon(os.getcwd().replace("\\", '/') + "/Image/cal.png"))
            cal_button.clicked.connect(self.show_cal)

            self.par_button_for_cal.append(cal_button)

            self.parVBox1.addWidget(QLabel(self.par_name[-1]))
            self.parVBox2.addWidget(self.par_valueForLineEdit[-1])
            self.parVBox3.addWidget(self.par_button_for_cal[-1])

        setupHBox1.addLayout(self.setupVboxColumn1)
        setupHBox1.addLayout(self.setupVboxColumn2)
        setupHBox2.addLayout(self.parVBox1)
        setupHBox2.addLayout(self.parVBox2)
        setupHBox2.addLayout(self.parVBox3)

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

        self.setWindowFlag(Qt.WindowStaysOnTopHint)

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

    def update_library(self, library_name):
        self.library_input.setCurrentText(library_name)

    def updateUI_for_array(self):
        if self.array_dict:
            print(self.array_dict)
            # self.name_input.setText(self._DesignParameter['_ElementName'])
            self.library_input.setCurrentText(self.array_dict['library'])
            self.class_name_input.setText(self.array_dict['className'])
            # self.XY_input.setText(str(self._DesignParameter['_XYCoordinates'][0][0])+','+str(self._DesignParameter['_XYCoordinates'][0][1]))
            if 'calculate_fcn' in self.array_dict.keys():
                self.cal_fcn_input.setCurrentText(self.array_dict['calculate_fcn'])
            i = 0
            for value in self.array_dict['parameters'].values():
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
            tmp = self.parVBox3.takeAt(0).widget()
            tmp.setParent(None)
            self.parVBox3.removeWidget(tmp)
            del tmp

        self.par_valueForLineEdit = []
        self.par_button_for_cal = []

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

                cal_button = QPushButton()
                cal_button.setIcon(QIcon(os.getcwd().replace("\\", '/') + "/Image/cal.png"))
                cal_button.clicked.connect(self.show_cal)

                self.par_button_for_cal.append(cal_button)

                self.parVBox1.addWidget(QLabel(self.par_name[-1]))
                self.parVBox2.addWidget(self.par_valueForLineEdit[-1])
                self.parVBox3.addWidget(self.par_button_for_cal[-1])

    def DetermineCoordinateWithMouse(self, xy):
        # self.XY_input.setText(str(_MouseEvent.scenePos().toPoint().x()) + ',' + str(_MouseEvent.scenePos().toPoint().y()))
        self.XY_input.setText(str(xy[0]) + ',' + str(xy[1]))

    def set_name_check(self, flag):
        self.name_check = flag

    def on_buttonBox_accepted(self):
        if 'name_input' in self.__dict__:
            self.send_name_duplication_check_signal.emit(self.name_input.text())
        if self.name_check == False:
            self.warning = QMessageBox()
            self.warning.setIcon(QMessageBox.Warning)
            self.warning.setText("Name duplication is detected!")
            self.warning.show()
            return None
        for idx in range(len(self.par_valueForLineEdit)):
            self.paramDict[self.par_name[idx]] = self.par_valueForLineEdit[idx].text()

        tmpAST = element_ast.Sref()
        for key in element_ast.Sref._fields:
            if key == 'name':
                if self.purpose == 'main_load':
                    tmpAST.__dict__[key] = self.name_input.text()
            elif key == 'library':
                tmpAST.__dict__[key] = self.library_input.currentText()
            elif key == 'className':
                tmpAST.__dict__[key] = self.class_name_input.text()
            elif key == 'XY':
                # tmpAST.__dict__[key] = self.XY_input.text()
                if self.purpose == 'main_load':
                    tmpAST.__dict__[key] = [[float(i) for i in self.XY_input.text().split(',')]]
            elif key == 'calculate_fcn':
                tmpAST.__dict__[key] = self.cal_fcn_input.currentText()
            elif key == 'parameters':
                tmpAST.__dict__[key] = self.paramDict
                tmpAST.parameter_fields = list(self.paramDict.keys())

        if not self.create:
            tmpAST._id = self._DesignParameter['_id']

        if self.purpose == 'main_load':
            self.send_DesignConstraint_signal.emit(tmpAST)
        elif self.purpose == 'array_load':
            self.send_array_signal.emit(tmpAST)

        if self.option:
            self.deleteLater()
            # self.deleteLater()
        else:
            self.option = True

    def maintain_window(self, option):
        self.option = option

    def cancel_button_accepted(self):
        self.deleteLater()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return or QKeyEvent.key() == Qt.Key_Enter:
            self.on_buttonBox_accepted()
            self.send_destroy_signal.emit('ls')
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.deleteLater()
            self.send_destroy_signal.emit('ls')

    def show_cal(self):
        sender = self.sender()
        self.cal_idx = self.par_button_for_cal.index(sender)

        self.cal = calculator.ExpressionCalculator(clipboard=QGuiApplication.clipboard(),purpose='sref')
        self.cal.send_expression_signal.connect(self.exported_text)
        self.cal.send_dummyconstraints_signal.connect(self.cal.storePreset)
        self.cal.set_preset_window()
        self.cal.show()

    def exported_text(self, text, purpose, output_dict):
        self.output_dict = output_dict
        self.send_exported_sref_signal.emit('LogicExpressionD_sref', output_dict)

    def get_param_value_ast(self, _id, _ast):
        self.par_valueForLineEdit[self.cal_idx].setText(_id)

    def get_runtime_info(self, status):
        if status == 'error':
            self.warning = QMessageBox()
            self.warning.setText("Invalid Parameter!")
            self.warning.show()
            self.option = False

class _MacroCellWindow(QWidget):
    send_DesignConstraint_signal = pyqtSignal("PyQt_PyObject")
    send_destroy_signal = pyqtSignal(str)
    send_name_duplication_check_signal =pyqtSignal(str)

    def __init__(self, MacroCellElement = None):
        super().__init__()
        self.create = False
        self.option = True
        self.paramDict = dict()
        self.initUI()
        self.name_check = True

        if MacroCellElement is None:
            self.create = True
            self.visualItem = VisualizationItem._VisualizationItem()
        else:
            self._DesignParameter = MacroCellElement._ItemTraits
            self.updateUI()

    def initUI(self):
        self.name = QLabel("name")
        self.library = QLabel("library")
        self.XY = QLabel("XY")

        self.name_input = QLineEdit()
        self.library_input = QLineEdit()
        self.library_input.setReadOnly(True)
        self.XY_input = QLineEdit()

        scf = QFileDialog.getOpenFileName(self,'Load GDS','./PyQTInterface/GDSFile')
        self._fileName = scf[0]
        if self._fileName == '':
            print("No File Selected")
            return
        else:
            # if platform.system() in ['Linux', 'Darwin']:
            #     generator_class_name = _fileName.split('\\')[-1][:-4]
            # else:
            #     generator_class_name = _fileName.split('/')[-1][:-4]
            generator_class_name = self._fileName.split('/')[-1][:-4]
            self.library_input.setText(generator_class_name)


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
        self.setupVboxColumn1.addWidget(self.XY)

        self.setupVboxColumn2.addWidget(self.name_input)
        self.setupVboxColumn2.addWidget(self.library_input)
        self.setupVboxColumn2.addWidget(self.XY_input)

        setupHBox1.addLayout(self.setupVboxColumn1)
        setupHBox1.addLayout(self.setupVboxColumn2)

        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(setupHBox1)
        vbox.addStretch(3)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.setWindowTitle('MacroCell Window')
        self.setGeometry(300,300,500,500)
        self.show()

    def updateUI(self):
        self.name_input.setText(self._DesignParameter['_ElementName'])
        self.library_input.setCurrentText(self._DesignParameter['library'])
        self.XY_input.setText(str(self._DesignParameter['_XYCoordinates'][0][0])+','+str(self._DesignParameter['_XYCoordinates'][0][1]))

    def update_library(self, library_name):
        self.library_input.setCurrentText(library_name)

    def updateUI_for_array(self):
        if self.array_dict:
            self.library_input.setCurrentText(self.array_dict['library'])

    def DetermineCoordinateWithMouse(self, xy):
        # self.XY_input.setText(str(_MouseEvent.scenePos().toPoint().x()) + ',' + str(_MouseEvent.scenePos().toPoint().y()))
        self.XY_input.setText(str(xy[0]) + ',' + str(xy[1]))

    def set_name_check(self, flag):
        self.name_check = flag

    def on_buttonBox_accepted(self):
        self.send_name_duplication_check_signal.emit(self.name_input.text())
        if self.name_check == False:
            self.warning = QMessageBox()
            self.warning.setIcon(QMessageBox.Warning)
            self.warning.setText("Name duplication is detected!")
            self.warning.show()
            return None
        tmpAST = element_ast.MacroCell()
        for key in element_ast.MacroCell._fields:
            if key == 'name':
                tmpAST.__dict__[key] = self.name_input.text()
            elif key == 'library':
                tmpAST.__dict__[key] =  self._fileName
            elif key == 'XY':
                tmpAST.__dict__[key] = [[float(i) for i in self.XY_input.text().split(',')]]

        self.send_DesignConstraint_signal.emit(tmpAST)

        if self.option:
            self.deleteLater()
        else:
            self.option = True

    def maintain_window(self, option):
        self.option = option

    def cancel_button_accepted(self):
        self.deleteLater()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return or QKeyEvent.key() == Qt.Key_Enter:
            self.on_buttonBox_accepted()
            self.send_destroy_signal.emit('mc')
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.deleteLater()
            self.send_destroy_signal.emit('mc')


class _TextSetupWindow(QWidget):

    send_TextSetup_signal = pyqtSignal(VisualizationItem._VisualizationItem)
    send_TextDesign_signal = pyqtSignal(dict)
    send_Destroy_signal = pyqtSignal(str)
    send_Warning_signal = pyqtSignal(str)
    send_DestroyTmpVisual_signal = pyqtSignal(VisualizationItem._VisualizationItem)
    send_name_duplication_check_signal =pyqtSignal(str)

    def __init__(self,TextElement=None):
        super().__init__()
        self.initUI()
        self.name_check = True
        if TextElement == None:
            self.visualItem = VisualizationItem._VisualizationItem()
            self._DesignParameter = dict(
                _ElementName = None,
                _DesignParametertype = 8,
                _LayerUnifiedName = 'text',
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

        self.name = None
        self.text = None
        self.mag = None
        self.XY_input = []

        nameLabel = QLabel("Name")
        textLabel = QLabel("Text")
        magLabel = QLabel("Width")
        XYLabel = QLabel("XY")

        self.name_input = QLineEdit()
        self.text_input = QLineEdit()
        self.width_input = QLineEdit()
        self.XY_input.append(QLineEdit())

        self.setupVboxColumn1 = QVBoxLayout()
        self.setupVboxColumn2 = QVBoxLayout()
        setupBox = QHBoxLayout()

        self.setupVboxColumn1.addWidget(nameLabel)
        self.setupVboxColumn1.addWidget(textLabel)
        self.setupVboxColumn1.addWidget(magLabel)
        self.setupVboxColumn1.addWidget(XYLabel)

        self.setupVboxColumn2.addWidget(self.name_input)
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

        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.setWindowTitle('Text Setup Window')
        self.setGeometry(300,300,500,200)
        self.show()


    def updateUI(self):
        self.text_input.setText(self._DesignParameter['_TEXT'])
        self.width_input.setText(str(self._DesignParameter['_Width']))
        self.XY_input[0].setText(str(self._DesignParameter['_XYCoordinates'][0][0])+','+str(self._DesignParameter['_XYCoordinates'][0][1]))

    def cancel_button_accepted(self):
        self.deleteLater()

    def set_name_check(self, flag):
        self.name_check = flag

    def on_buttonBox_accepted(self):
        self.send_name_duplication_check_signal.emit(self.name_input.text())
        if self.name_check == False:
            self.warning = QMessageBox()
            self.warning.setIcon(QMessageBox.Warning)
            self.warning.setText("Name duplication is detected!")
            self.warning.show()
            return None
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

            self._DesignParameter['_ElementName'] = self.name_input.text()
            if self._DesignParameter['_ElementName'] == '':
                raise NotImplementedError
            self._DesignParameter['_TEXT'] = self.text_input.text()
            self._DesignParameter['_Mag'] = int(self.width_input.text())
            self.send_TextDesign_signal.emit(self._DesignParameter)
            self.deleteLater()
            self.send_Destroy_signal.emit('txtw')
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

    def DetermineCoordinateWithMouse(self, xy):
        ##### When Click the point, adjust x,y locations #####
        X = xy[0]
        Y = xy[1]
        self.XY_input[0].setText(str(X)+','+str(Y))
        self._DesignParameter['_XYCoordinates']=[[X,Y]]
        self._DesignParameter['_ElementName'] = self.text_input.text()
        self._DesignParameter['_TEXT'] = self.text_input.text()
        try:
            self._DesignParameter['_Mag'] = int(self.width_input.text())
        except:
            self._DesignParameter['_Mag'] = 10

        qt_dp = QTInterfaceWithAST.QtDesignParameter()
        for key, value in self._DesignParameter.items():
            qt_dp._setDesignParameterValue(key, value)
        # qt_dp.update_unified_expression()

        self.visualItem.updateDesignParameter(qt_dp)
        # self.visualItem.updateTraits(self._DesignParameter)
        self.send_TextSetup_signal.emit(self.visualItem)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_buttonBox_accepted()
            self.send_Destroy_signal.emit('txtw')
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.deleteLater()
            self.send_Destroy_signal.emit('txtw')

class _PinSetupWindow(QWidget):

    send_PinSetup_signal = pyqtSignal(VisualizationItem._VisualizationItem)
    send_PinDesign_signal = pyqtSignal(dict)
    send_Destroy_signal = pyqtSignal(str)
    send_Warning_signal = pyqtSignal(str)
    send_DestroyTmpVisual_signal = pyqtSignal(VisualizationItem._VisualizationItem)
    send_name_duplication_check_signal =pyqtSignal(str)

    def __init__(self,PinElement=None):
        super().__init__()
        self.initUI()
        self.name_check = True
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

        self.name = None
        self.layer = None
        self.text = None
        self.mag = None
        self.XY_input = []

        nameLabel = QLabel("Name")
        layerLabel = QLabel("Layer")
        textLabel = QLabel("Text")
        magLabel = QLabel("Width")
        XYLabel = QLabel("XY")

        self.name_input = QLineEdit()
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

        self.setupVboxColumn1.addWidget(nameLabel)
        self.setupVboxColumn1.addWidget(layerLabel)
        self.setupVboxColumn1.addWidget(textLabel)
        self.setupVboxColumn1.addWidget(magLabel)
        self.setupVboxColumn1.addWidget(XYLabel)

        self.setupVboxColumn2.addWidget(self.name_input)
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

        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.setWindowTitle('Text Setup Window')
        self.setGeometry(300,300,500,200)
        self.show()

    def updateUI(self):
        self.name_input.setText(self._DesignParameter['_ElementName'])
        self.text_input.setText(self._DesignParameter['_TEXT'])
        self.width_input.setText(str(self._DesignParameter['_Width']))
        self.XY_input[0].setText(str(self._DesignParameter['_XYCoordinates'][0][0])+','+str(self._DesignParameter['_XYCoordinates'][0][1]))

    def cancel_button_accepted(self):
        self.deleteLater()

    def set_name_check(self, flag):
        self.name_check = flag

    def on_buttonBox_accepted(self):
        self.send_name_duplication_check_signal.emit(self.name_input.text())
        if self.name_check == False:
            self.warning = QMessageBox()
            self.warning.setIcon(QMessageBox.Warning)
            self.warning.setText("Name duplication is detected!")
            self.warning.show()
            return None
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
            self._DesignParameter['_ElementName'] = self.name_input.text()
            if self._DesignParameter['_ElementName'] == '':
                raise NotImplementedError
            self._DesignParameter['_TEXT'] = self.text_input.text()
            self._DesignParameter['_Mag'] = float(self.width_input.text())
            self._DesignParameter['_LayerUnifiedName'] = self.layer_input.currentText()
            self.send_PinDesign_signal.emit(self._DesignParameter)
            self.deleteLater()
            self.send_Destroy_signal.emit('pinw')

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

    def DetermineCoordinateWithMouse(self, xy):
        ##### When Click the point, adjust x,y locations #####
        X = xy[0]
        Y = xy[1]
        self.XY_input[0].setText(str(X)+','+str(Y))
        self._DesignParameter['_XYCoordinates']=[[X,Y]]
        self._DesignParameter['_ElementName'] = self.text_input.text()
        self._DesignParameter['_TEXT'] = self.text_input.text()
        self._DesignParameter['_Mag'] = float(self.width_input.text())
        self._DesignParameter['_LayerUnifiedName'] = self.layer_input.currentText()

        qt_dp = QTInterfaceWithAST.QtDesignParameter()
        for key, value in self._DesignParameter.items():
            qt_dp._setDesignParameterValue(key, value)
        qt_dp.update_unified_expression()

        self.visualItem.updateDesignParameter(qt_dp)
        # self.visualItem.updateTraits(self._DesignParameter)
        self.send_PinSetup_signal.emit(self.visualItem)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_buttonBox_accepted()
            self.send_Destroy_signal.emit('pinw')
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.deleteLater()
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
        self.deleteLater()
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
        self.deleteLater()
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_buttonBox_accepted()
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.deleteLater()
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
        self.deleteLater()
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
        self.deleteLater()
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_buttonBox_accepted()
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.deleteLater()
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
        self.deleteLater()

    def cancel_button_accepted(self):
        self.deleteLater()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_buttonBox_accepted()
            self.send_destroy_signal.emit('cw')
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.deleteLater()
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
        self.deleteLater()
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
        self.deleteLater()
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_buttonBox_accepted()
            self.send_Destroy_signal.emit('cw')
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.deleteLater()
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
        self.deleteLater()
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
        self.deleteLater()
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_buttonBox_accepted()
            self.send_Destroy_signal.emit('cw')
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.deleteLater()
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
        comboItemList = ['pyCode', 'scriptDefine']
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
        self.deleteLater()
    def on_buttonBox_accepted(self):
        if self.type_input.currentText() == "pyCode":
            try:
                value = self.setupVboxColumn2.itemAt(1).widget().text()
            except:
                value = self.setupVboxColumn2.itemAt(1).widget().currentText()
            self._ParseTree[0] = "pyCode"
            self._ParseTree.append(value)
        self.send_PyCode_signal.emit(value)
        self.deleteLater()
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_buttonBox_accepted()
            self.send_Destroy_signal.emit('cw')
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.deleteLater()
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
    send_request_visual_item = pyqtSignal(str)
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
                if item.parentItem():
                    continue
                tmpName = item._ItemTraits['_ElementName']
                if tmpName == None:
                    continue
                # tmpName = item._ElementName
                self.itemDict[tmpName] = item
                self.idDict[tmpName] = item._ItemTraits['_ElementName']
                # item.setSelected(True)
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

    def update_item_dict(self, element_name, element):
        self.itemDict[element_name] = element

    def ModifyingDesign(self,item,_=None):
        '''
        when user double clicked item at design list (input: widget item)
        or
        when user type 'key_H' at scene (input: element name list)
        --> pop up design element edit widget,
        '''
        if type(item) == list:
            element_text = item[0]
        else:
            element_text = item.text()

        if element_text not in self.itemDict:
            self.send_request_visual_item.emit(element_text)

        modifyingObject = self.itemDict[element_text]

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
            try:
                self.sw = _LoadSRefWindow(purpose='main_load', SRefElement=modifyingObject)
                self.sw.show()
                self.sw.send_DesignConstraint_signal.connect(self.send_UpdateDesignAST_signal)
                self.sw.send_exported_sref_signal.connect(self.createDummyConstraint)
                self.sw.send_destroy_signal.connect(self.sw.close)
            except:
                warnings.warn('Not Implemented.')
        elif modifyingObject._ItemTraits['_DesignParametertype'] == 8:
            if modifyingObject._ItemTraits['_LayerUnifiedName'] == 'text':
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
    send_SendID_signal_highlight = pyqtSignal(str)
    send_SendCopyConstraint_signal = pyqtSignal(QTInterfaceWithAST.QtDesinConstraint)
    send_RootDesignConstraint_signal = pyqtSignal(str)
    send_ReceiveDone_signal = pyqtSignal()
    send_RequestDesignConstraint_signal = pyqtSignal()
    send_RequestElementManger_signal = pyqtSignal()
    send_DataChanged_signal = pyqtSignal(str)
    # send_deleteID_signal = pyqtSignal(str)
    send_deleteConstraint_signal = pyqtSignal(str)
    send_dummy_ast_id_for_xy_signal = pyqtSignal(str)
    send_dummy_ast_id_for_array_signal = pyqtSignal(str)
    send_dummy_ast_id_for_condition_signal = pyqtSignal(str)
    request_sref_redefine_signal = pyqtSignal("PyQt_PyObject")


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
        self._CurrentModuleName = None
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

        self.context_menu_for_xy = QMenu(self)
        browse_expression_action = QAction("View expression", self.context_menu_for_xy)
        self.context_menu_for_xy.addActions([browse_expression_action])

        self.context_menu_for_array = QMenu(self)
        self.context_menu_for_array.addActions([browse_expression_action])

        self.context_menu_for_condition = QMenu(self)
        self.context_menu_for_condition.addActions([browse_expression_action])
        browse_expression_action.triggered.connect(self.browse_expression)

        self.context_menu_for_sref = QMenu(self)
        browse_expression_action = QAction("Create redefine expression", self.context_menu_for_sref)
        self.context_menu_for_sref.addActions([browse_expression_action])

        add_blank_row_action.triggered.connect(self.append_row)
        add_blank_row_dict_action.triggered.connect(self.append_row)
        browse_expression_action.triggered.connect(self.browse_expression)

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
        # self.model.setHeaderData(4,Qt.Horizontal,"fcn_type")

        self.setModel(self.model)

        self.resizeColumnToContents(0)

        self.debugType = type

    def createNewConstraintAST(self,_id , _parentName, _DesignConstraint):
        self._DesignConstraintFromQTobj = _DesignConstraint
        rc = self.model.createNewColumnWithID(_id=_id, _parentName=_parentName, _DesignConstraint = _DesignConstraint)

        # if _DesignConstraint[_parentName][_id]._type == 'Sref':
        #     sref_item = self.model.item(rc,0)
        #     calculate_name_item = sref_item.child(4,4) #row=4 for calculate_fcn in Sref ast
        #     idx = self.model.indexFromItem(calculate_name_item).siblingAtColumn(4)
        #     if _DesignConstraint[_parentName][_id]._ast.library == 'MacroCell':
        #         pass
        #     else:
        #         fcn_list = list(generator_model_api.class_function_dict[_DesignConstraint[_parentName][_id]._ast.library].keys())
        #         combo_delegetor = ComboDelegate(self,fcn_list)
        #         self.setItemDelegateForColumn(4,combo_delegetor)
        #     # idx = self.model.index(rc,3,QModelIndex())
        #     # self.model.appendRow([QStandardItem('aa')])
        #     # self.openPersistentEditor(self.model.index(rc,3))
        #     self.openPersistentEditor(idx)

    def reload_new_id(self, match_dict):
        item_count = self.model.rowCount()
        item_stack = [self.model.itemFromIndex(self.model.index(row,0)) for row in range(0,item_count)]
        while item_stack:
            item = item_stack.pop(0)
            child_count = item.rowCount()
            child_stack = [item.child(row) for row in range(0,child_count)]
            item_stack.extend(child_stack)
            id_idx = self.model.indexFromItem(item).siblingAtColumn(1)
            id_item = self.model.itemFromIndex(id_idx)
            old_id = id_item.text()

            if old_id in match_dict:
                id_item.setText(match_dict[old_id])



    def UpdateSelectedItem(self, item):
        if item == None:
            pass
        else:
            constraint = self.model._ConstraintDict[item.text()]
            self.cw = _ConstraintSetupWindow(constraint._ParseTree)
            self.cw.show()

    def set_errored_constraint_id(self, constraint_id, error_flag, error_log = None, exception = None):
        if exception:
            error_line = error_log.split('\n')[-2]
            error_type = type(exception).__name__
            if error_type in ['TypeError', 'ValueError']:
                error_element = re.search("\'.+\'",exception.args[0]).group()
                error_log = f'Error found at : {error_element} \n'
                error_log += f'Orignal error log: {error_line}'
            elif error_type in ['KeyError']:
                error_element = exception.args[0]
                error_log = f'Trying to refer not valid key: {error_element} \n'
                # error_log += f'Orignal error log: {error_line}'
            elif error_type in ['NameError']:
                error_element = re.search("\'.+\'",exception.args[0]).group()
                error_log = f'Variable {error_element} was not defined'
            else:
                # error_element = re.search("\'.+\'", exception.args[0]).group()
                # error_log = f'Error found at: {error_element} \n'
                error_log += f'Orignal error type and log: {error_type}, {error_line}'

        if constraint_id in self.model._ConstraintItem:
            item = self.model._ConstraintItem[constraint_id]
            index = self.model.indexFromItem(item)
            if error_flag == 'static':
                self.model.setData(index, QBrush(Qt.yellow), Qt.BackgroundRole)
                if error_log:
                    item.setToolTip(error_log)
            elif error_flag == 'dynamic':
                self.model.setData(index, QBrush(Qt.red), Qt.BackgroundRole)
                item.setToolTip(error_log)
            elif error_flag == 'clean':
                og_color = self.palette().color(QPalette.Base)
                self.model.setData(index, og_color, Qt.BackgroundRole)
                item.setToolTip(None)
            elif error_flag == 'no_value':
                self.model.setData(index, QBrush(Qt.yellow), Qt.BackgroundRole)
                item.setToolTip(error_log)


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
            if not itemIDitem:
                return
            itemID = itemIDitem.text()
            motherID = None
            # moduleName = re.sub(r'\d','',itemID)
            moduleName = self._CurrentModuleName
            try:
                valueItem = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(3))    #ConstraintValue
                value = valueItem.text()
            except:
                value = None

            # if moduleName in self._DesignConstraintFromQTobj:
            if itemID in self._DesignConstraintFromQTobj[moduleName]:
                pass
            else:
                motherIDItem = self.model.itemFromIndex(self.currentIndex().parent().siblingAtColumn(1))
                motherID = motherIDItem.text()
                # motherModuleName = re.sub(r'\d','',motherID)
                motherModuleName = self._CurrentModuleName
                placeHolderItem = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(0))
                placeHolder = placeHolderItem.text()

                #if parent is not AST case (Double list or dictionary case)
                # if motherModuleName not in self._DesignConstraintFromQTobj:
                if motherID not in self._DesignConstraintFromQTobj[motherModuleName]:
                    grandparentIDItem = self.model.itemFromIndex(self.currentIndex().parent().parent().siblingAtColumn(1))
                    grandparentID = grandparentIDItem.text()
                    grandParentModuleName = self._CurrentModuleName
                    fieldItem = self.model.itemFromIndex(self.currentIndex().parent().siblingAtColumn(0))
                    field = fieldItem.text()
                    '''
                    Triple-list check
                    grandparent -> replace with greatgrandparent
                    '''
                    if field == '':
                        field_item = self.model.itemFromIndex(self.currentIndex().parent().parent().siblingAtColumn(0))
                        field = field_item.text()
                        idx1 = motherIDItem.row()
                        idx2 = itemIDitem.row()
                        great_grandparent_id_item = self.model.itemFromIndex(self.currentIndex().parent().parent().parent().siblingAtColumn(1))
                        great_grandparent_id = great_grandparent_id_item.text()
                        great_grandparent_module_name = self._CurrentModuleName
                        self.updateDesignConstraintWithList_grandchild(Module=great_grandparent_module_name,Id=great_grandparent_id,Field=field,idx1=idx1, idx2=idx2,StringValue=value)

                    elif type(self._DesignConstraintFromQTobj[grandParentModuleName][grandparentID]._ast.__dict__[field]) == dict:
                        self.updateDesignConstraintWithDict(Module=grandParentModuleName,Id=grandparentID,Field=field,Key=placeHolder,StringValue=value)
                    else:
                        idx = itemIDitem.row()
                        self.updateDesignConstraintWithList(Module=grandParentModuleName, Id=grandparentID, Field=field,
                                                            Idx=idx, StringValue=value)
                else:
                    self.updateDesginConstraintWithSTR(Module=motherModuleName,Id=motherID,Field =placeHolder ,StringValue=value)

            ###Step 2 sub-hierarchy refresh#####################################            #To expand unseen contents <Constraint Case>
            if itemID not in self._DesignConstraintFromQTobj[moduleName]:
                pass
            elif moduleName in self._DesignConstraintFromQTobj:
                if itemID in self._DesignConstraintFromQTobj[moduleName]:
                    self.refreshItem(self.currentIndex())
                else:
                    warnings.warn('During mouseDoubleClickEvent, Valid module name ({}), but invalid ID ({})'.format(moduleName,itemID))

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

        if Field == 'id':
            return

        # tmpChildModule = re.sub(r'\d','',StringValue)
        tmpChildModule = self._CurrentModuleName
        if tmpChildModule in self._DesignConstraintFromQTobj:                        #Check whether it is constraint or not
            if StringValue in self._DesignConstraintFromQTobj[tmpChildModule]:
                _value = self._DesignConstraintFromQTobj[tmpChildModule][StringValue]._ast
                self._DesignConstraintFromQTobj[Module][Id]._appendDesignConstraintValue(_index=Field,_value=_value)
                return
            elif Id in self._DesignConstraintFromQTobj[tmpChildModule]:
                try:
                    _value = ast.literal_eval(StringValue)
                except:
                    _value = StringValue
                self._DesignConstraintFromQTobj[Module][Id]._setDesignConstraintValue(_index=Field, _value=_value)
        else:
            try:
                _value = ast.literal_eval(StringValue)
            except:
                _value = StringValue

            self._DesignConstraintFromQTobj[Module][Id]._setDesignConstraintValue(_index=Field,_value=_value)
            return

    def updateDesignConstraintWithSTR_grandchild(self, module, grand_id, field1, field2, value_id):
        # convert: String type value --> Adequate type
        if value_id == None or value_id == "" or value_id == "*":
            return

        if value_id == 'id':
            return

        # tmpChildModule = re.sub(r'\d','',StringValue)
        tmpChildModule = self._CurrentModuleName
        if tmpChildModule in self._DesignConstraintFromQTobj:                        #Check whether it is constraint or not
            if value_id in self._DesignConstraintFromQTobj[tmpChildModule]:
                _value = self._DesignConstraintFromQTobj[tmpChildModule][value_id]._ast
                org_val =self._DesignConstraintFromQTobj[module][grand_id]._ast.__dict__[field1]
                org_val[field2] = _value
                self._DesignConstraintFromQTobj[module][grand_id]._setDesignConstraintValue(_index=field1,_value=org_val)
                return
        # else:
        #     try:
        #         _value = ast.literal_eval(value_id)
        #     except:
        #         _value = value_id
        #     #TODO
        #     self._DesignConstraintFromQTobj[module][grand_id]._setDesignConstraintValue(_index=field2,_value=_value)
        #     # return

    def updateDesignConstraintWithDict(self,Module,Id,Field,Key,StringValue):
        self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field][Key] = StringValue

    def updateDesignConstraintWithList(self,Module,Id,Field,Idx,StringValue):
        # if Idx <= len(self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field]):
        #     self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field].append(None)
        if StringValue == "*":
            return
        if self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field] == None:
            self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field] = []
        if Idx >= len(self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field]):
            self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field].append(None)
        if ',' in StringValue:
            # if Idx >= len(self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field]):
            #     self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field].append(None)
            try:
                self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field][Idx] = [float(value) for value in StringValue.split(',')]
            except:
                # self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field][Idx] = '[' + StringValue + ']'
                self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field][Idx] = [value for value in StringValue.split(',')]
        else:
            self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field][Idx] = StringValue
        # try:
        #     print(self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field][Idx])
        #     self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field][Idx] = [float(value) for value in StringValue.split(',')]
        # except:
        #     self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field][Idx] = StringValue
        # self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field][Idx] = StringValue.split(',')

    def updateDesignConstraintWithList_grandchild(self,Module,Id,Field,idx1,idx2,StringValue):
        # if Idx <= len(self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field]):
        #     self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field].append(None)
        if StringValue == "*":
            return
        if self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field] == None:
            self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field] = []
        if idx1 >= len(self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field]):
            self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field].append([])
        if idx2 >= len(self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field][idx1]):
            self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field][idx1].append(None)
        if ',' in StringValue:
            # if idx1 >= len(self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field]):
            #     self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field].append([])
            # if idx2 >= len(self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field][idx1]):
            #     self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field][idx1].append(None)
            try:
                self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field][idx1][idx2] = [float(value) for value in StringValue.split(',')]
            except:
                self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field][idx1][idx2] = [value for value in StringValue.split(',')]
        else:
            self._DesignConstraintFromQTobj[Module][Id]._ast.__dict__[Field][idx1][idx2] = StringValue
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
            # _module = re.sub(r'\d','',_id)
            _module = self._CurrentModuleName
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
                constraintModule = get_id_return_module(constraintName, '_DesignConstraint',
                                                        self._DesignConstraintFromQTobj)
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
                    grand_id = None
                    # motherModule = re.sub(r'\d','',motherId)
                    motherModule = self._CurrentModuleName
                    if motherModule not in self._DesignConstraintFromQTobj:
                        self.send_RequestDesignConstraint_signal.emit()
                    if motherId not in self._DesignConstraintFromQTobj[motherModule]:
                        grand_id_item = self.model.itemFromIndex(self.currentIndex().parent().parent().siblingAtColumn(1))
                        grand_id =grand_id_item.text()
                        first_field_item = self.model.itemFromIndex(self.currentIndex().parent().siblingAtColumn(0))
                        first_field = first_field_item.text()
                    placeHolder = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(0)).text()
                    if not grand_id:
                        self.updateDesginConstraintWithSTR(Module=motherModule, Id=motherId, Field=placeHolder, StringValue=_id)
                        currentItemId = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(3))
                        currentItemId.setText('*')
                    else:
                        value_field = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(3))
                        value_field.setText('')
                        self.updateDesignConstraintWithSTR_grandchild(module=self._CurrentModuleName, grand_id=grand_id,
                                                                      field1=first_field, field2=placeHolder,
                                                                      value_id=_id)
                        currentItemType = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(2))
                        id_field = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(1))
                        id_field.setText(_id)
                        # value_field = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(3))
                        # value_field.setText('')
                        _itemType = self._DesignConstraintFromQTobj[motherModule][_id]._type
                        currentItemType.setText(str(_itemType))

                    # #_itemType = self._DesignConstraintFromQTobj[motherModule][motherId]._ast[placeHolder]._type
                    # currentItemId = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(3))
                    # #currentItemType = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(2))
                    # currentItemId.setText('*')
                    # #currentItemType.setText(_itemType)
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
        # tmpModuel = re.sub(r'\d','',indexID)
        tmpModule = self._CurrentModuleName
        self.send_RequestDesignConstraint_signal.emit()

        if tmpModule in self._DesignConstraintFromQTobj and indexID in self._DesignConstraintFromQTobj[tmpModule]:                #Constraint Case -> expand subhierarchy
            # if indexID in self._DesignConstraintFromQTobj[tmpModule]:
            dc = self._DesignConstraintFromQTobj[tmpModule][indexID]
            self.model.updateRowChildWithAST(_DesignConstraint= dc, motherIndex=itemIndex)

        #elif indexID == "" or indexID == None:                    #If refresh Item is parsetree and it has at least one child constraint
        elif value == "*":
            indexTypeItem = self.model.itemFromIndex(itemIndex.siblingAtColumn(0))
            _key = indexTypeItem.text()
            motherIndex = itemIndex.parent().siblingAtColumn(1)

            """
            Check Triple list case or not (Path case.)
            """
            motherItem = self.model.itemFromIndex(motherIndex)
            motherName = motherItem.text()

            mother_container_name = self.model.itemFromIndex(motherIndex.siblingAtColumn(1)).text()
            if mother_container_name == '':
                grandparent_nameitem = self.model.itemFromIndex(motherIndex.parent().siblingAtColumn(1))
                grandparent_item = self.model.itemFromIndex(motherIndex.parent().siblingAtColumn(0))
                grandparent_name = grandparent_nameitem.text()
                grandparent_module = get_id_return_module(id=grandparent_name, type='_DesignConstraint', moduleDict=self._DesignConstraintFromQTobj)
                _ast = self._DesignConstraintFromQTobj[grandparent_module][grandparent_name]._ast
                mother_item_for_key = self.model.itemFromIndex(motherIndex.siblingAtColumn(0))
                _key = mother_item_for_key.text()
                motherItem = self.model.itemFromIndex(itemIndex.siblingAtColumn(0))
                self.model.readParseTreeForGrandChildren(grandparent_item=grandparent_item,mother_item=motherItem,_AST=_ast,key=_key)

            else:
                motherModule = get_id_return_module(id=motherName, type='_DesignConstraint', moduleDict=self._DesignConstraintFromQTobj)
                _ast = self._DesignConstraintFromQTobj[motherModule][motherName]._ast

                self.model.readParseTreeForMultiChildren(motherItem=indexTypeItem,_AST=_ast ,key=_key)


            # updateConstraint = self.itemToDesignConstraintDict[indexItemName]
            #
            # self.model.updateRowChild(updateConstraint, motherIndex=itemIndex)


        elif itemIndex.parent().isValid() == True:                          # If refresh Item is parsetree and it has mother constraint
            motherIndex = itemIndex.parent().siblingAtColumn(1)
            motherItem = self.model.itemFromIndex(motherIndex)
            originalRow = motherIndex.row()
            motherName = motherItem.text()

            #indexID.setEditable(True)
            tmpModule = self._CurrentModuleName
            if tmpModule not in self._DesignConstraintFromQTobj:
                #do nothing! (field value is not constraint but list or dictionary case)
                return

            if motherName in self._DesignConstraintFromQTobj[tmpModule]:
                dc = self._DesignConstraintFromQTobj[tmpModule][motherName]
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
                    parent_item = self.model.itemFromIndex(self.currentIndex().parent().siblingAtColumn(1))
                    parent_id = parent_item.text()
                    ##### sref parameter case... maybe... i dont want to think ...
                    if parent_id == "":
                        grandparent_item = self.model.itemFromIndex(
                            self.currentIndex().parent().parent().siblingAtColumn(1))
                        grandparent_id = grandparent_item.text()
                        module = self._CurrentModuleName
                        field_item = self.model.itemFromIndex(self.currentIndex().parent().siblingAtColumn(0))
                        field = field_item.text()
                        current_item = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(0))
                        key_value = current_item.text()
                        if key_value != '':  # dictionary case
                            del self._DesignConstraintFromQTobj[module][grandparent_id]._ast.__dict__[field][key_value]
                        else:
                            row = current_item.row()
                            type = self._DesignConstraintFromQTobj[module][grandparent_id]._ast._type
                            if field == 'XY' and type == 'Path':
                                if row == len(
                                        self._DesignConstraintFromQTobj[module][grandparent_id]._ast.__dict__[field][
                                            0]) - 1:
                                    del self._DesignConstraintFromQTobj[module][grandparent_id]._ast.__dict__[field][0][
                                        row]
                            else:
                                del self._DesignConstraintFromQTobj[module][grandparent_id]._ast.__dict__[field][row]
                        self.refreshItem(self.model.indexFromItem(parent_item))
                else:
                    parent_item = self.model.itemFromIndex(self.currentIndex().parent().siblingAtColumn(1))
                    parent_id = parent_item.text()
                    if parent_id != "":
                        module = get_id_return_module(parent_id,'_DesignConstraint',self._DesignConstraintFromQTobj)
                        field_item = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(0))
                        field = field_item.text()
                        del self._DesignConstraintFromQTobj[module][parent_id]._ast.__dict__[field]
                        ## if sub-constraint has children rows... ##
                        selected_item_col_zero = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(0))
                        for row in range(0,selected_item_col_zero.rowCount()):
                            selected_item_col_zero.removeRow(0)
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
                            type = self._DesignConstraintFromQTobj[module][grandparent_id]._ast._type
                            if field == 'XY' and type == 'Path':
                                if row == len(self._DesignConstraintFromQTobj[module][grandparent_id]._ast.__dict__[field][0]) - 1:
                                    del self._DesignConstraintFromQTobj[module][grandparent_id]._ast.__dict__[field][0][row]
                            else:
                                del self._DesignConstraintFromQTobj[module][grandparent_id]._ast.__dict__[field][row]
                        self.refreshItem(self.model.indexFromItem(parent_item))

            except:
                traceback.print_exc()
        elif QKeyEvent.key() == Qt.Key_C:
            if self.currentIndex().isValid() ==False:
                return
            nameItem = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(1))
            name = nameItem.text()
            module_name = self._CurrentModuleName
            if name not in self._DesignConstraintFromQTobj[module_name]:
                self.send_RequestDesignConstraint_signal.emit()
            if name in self._DesignConstraintFromQTobj[module_name]:
                self.removeFlag = False
                self.send_SendCopyConstraint_signal.emit(self._DesignConstraintFromQTobj[module_name][name])
                print("copy!!")
        elif QKeyEvent.key() == Qt.Key_F5:
            self.resizeColumnToContents(0)
        elif QKeyEvent.key() == Qt.Key_BracketRight:
            self.collapseAll()
        elif QKeyEvent.key() == Qt.Key_BracketLeft:
            self.expandAll()
        elif QKeyEvent.key() == Qt.Key_H:
            id_item = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(1))
            id_string = id_item.text()
            self.send_SendID_signal_highlight.emit(id_string)

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

        # print(DeclarationString)

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

                if type_item.text() in ['XYCoordinate', 'PathXY', 'LogicExpression', 'CustomVariable']:
                    self.context_menu_for_xy.exec_(self.viewport().mapToGlobal(point))
                elif type_item.text() == 'Array':
                    self.context_menu_for_array.exec_(self.viewport().mapToGlobal(point))
                elif type_item.text() == "ConditionSTMTlist":
                    self.context_menu_for_condition.exec_(self.viewport().mapToGlobal(point))
                elif type_item.text() == "Sref":
                    self.context_menu_for_sref.exec_(self.viewport().mapToGlobal(point))
                # elif "str" in type_item.text():
                #     if idx.parent():
                #         parent_type_item = self.model.itemFromIndex(idx.parent().siblingAtColumn(2))
                #         if parent_type_item.text() == 'XYCoordinate' or 'PathXY':
                #             self.context_menu_for_xy.exec_(self.viewport().mapToGlobal(point))
                # elif "list" in type_item.text():
                #     self.context_menu_for_list.exec_(self.viewport().mapToGlobal(point))
                # elif "dict" in type_item.text():
                #     self.context_menu_for_dict.exec_(self.viewport().mapToGlobal(point))
        except:
            traceback.print_exc()
            pass

    def append_row(self):
        current_item = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(0))
        current_item.appendRow([QStandardItem(),QStandardItem(),QStandardItem(),QStandardItem()])
        print("what happend?")

    def browse_expression(self):
        current_item =self.model.itemFromIndex(self.currentIndex().siblingAtColumn(1))
        type_name = self.model.itemFromIndex(self.currentIndex().siblingAtColumn(0)).text()
        if type_name in ['XYCoordinate', 'PathXY', 'LogicExpression', 'CustomVariable']:
            self.send_dummy_ast_id_for_xy_signal.emit(current_item.text())
        elif type_name == 'Array':
            self.send_dummy_ast_id_for_array_signal.emit(current_item.text())
        elif type_name == "ConditionSTMTlist":
            self.send_dummy_ast_id_for_condition_signal.emit(current_item.text())
        elif type_name == 'Sref':
            # self.request_sref_redefine_signal.emit(current_item.text())
            org_ast = self._DesignConstraintFromQTobj[self._CurrentModuleName][current_item.text()]._ast
            redef_ast = element_ast.SrefR()
            redef_ast.name = org_ast.name
            redef_ast.calculate_fcn = org_ast.calculate_fcn
            redef_ast.parameter_fields.extend(org_ast.parameter_fields)
            for parm_name in org_ast.parameters:
                redef_ast.parameters[parm_name] = None
            self.request_sref_redefine_signal.emit(redef_ast)


        # if current_item.text() != None:
        #     self.send_dummy_ast_id_for_xy_signal.emit(current_item.text())
        # else:
        #     parent_item = self.model.itemFromIndex(self.currentIndex().parent().siblingAtColumn(1))
        #     self.send_dummy_ast_id_for_xy_signal.emit(parent_item.text())


    def get_dp_highlight_dc(self,dp_id_list,_):
        """
        :param dp_id_list: design_parameter_list
        :param _: not use (trigger signal return dp_di_list and type, but this slot does not use type.
        :return:
        """
        self.clearSelection()

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

    def clearSelection(self):
        super(_ConstraintTreeViewWidgetAST, self).clearSelection()
        self.setCurrentIndex(self.model.index(-1,-1))

        # constraint_ids = [item.text() for item in constraint_names]

class _ConstraintModel(QStandardItemModel):
    def __init__(self):
        QStandardItemModel.__init__(self)
        self._DesignConstraintFromQTobj = None
        self._ConstraintNameList = []
        self._ConstraintDict = dict()
        self._ConstraintItem = dict()

        self._Root = None
        self.setColumnCount(4)

        self._CurrentModuleName = None
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

        self.insertRow(rc, [tmpConstraintType, QStandardItem(_id), QStandardItem(_type),QStandardItem()])
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

        motherID_Module = self._CurrentModuleName
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
        # print(hierarchyList)
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
                        childModule = self._CurrentModuleName
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
                motherItem.appendRow([tmpA, tmpB, tmpC, tmpD])

    def readParseTreeForMultiChildren(self,motherItem=None,_AST = None,key=None,grandparentItem=None):
        checkChild = self.findChildrenWithText(motherItem,key,column=0)   #If Constraint has child constraint, then show Constraint Name for Child constraint.

        if key not in _AST.__dict__:
            return

        if type(_AST.__dict__[key]) == list and len(_AST.__dict__[key]) != 0 :
            valueItem = self.itemFromIndex(motherItem.index().siblingAtColumn(3))
            valueItem.setText("*")



        #test,, delete code order change...
        #When dictionary field double clicked, it has some problems
        for row in range(0,motherItem.rowCount()):
            # print(motherItem.rowCount())
            motherItem.removeRow(0)

        for childAST in _AST.__dict__[key]:   #### childConstraint is item in list!
            if type(childAST) == list:
                # for row in range(0,motherItem.rowCount()):
                #     motherItem.removeRows(0)
                if type(childAST[0]) != list:   #Boundary case
                    print("List case display")
                    tmpB = QStandardItem()
                    tmpC = QStandardItem(str(type(childAST)))
                    tmpD = str(childAST[0]) + ',' + str(childAST[1])
                    tmpD = QStandardItem(tmpD)
                    motherItem.appendRow([QStandardItem(), QStandardItem(), tmpC, tmpD])
                else:
                    tmpB = QStandardItem()
                    tmpC = QStandardItem(str(type(childAST)))
                    motherItem.appendRow([QStandardItem(''),QStandardItem(''),tmpC, QStandardItem('*')])
                    # for child_child_AST in childAST:
                    #     print("Doubled-list case display")
                    #     tmpC = QStandardItem(str(type(child_child_AST)))
                    #     tmpD = str(child_child_AST[0]) + ',' + str(child_child_AST[1])
                    #     tmpD = QStandardItem(tmpD)
                    #     motherItem.appendRow([QStandardItem(), QStandardItem(), tmpC, tmpD])
            elif type(childAST) == str:
                tmpA = QStandardItem(childAST)
                tmpB = QStandardItem()
                tmpC = QStandardItem()
                if type(_AST.__dict__[key]) == dict:
                    tmpD = QStandardItem(str(_AST.__dict__[key][childAST]))
                    if isinstance(_AST.__dict__[key][childAST], ast.AST):
                        tmpB = QStandardItem(_AST.__dict__[key][childAST]._id)
                        try:
                            tmpC = QStandardItem(_AST.__dict__[key][childAST]._type)
                        except:
                            tmpC = QStandardItem(str(type(_AST.__dict__[key][childAST])))
                        tmpD = QStandardItem('*')

                elif type(_AST.__dict__[key]) == list:
                    tmpD = QStandardItem()
                else:
                    tmpD = QStandardItem()
                    # tmpD = QStandardItem(str(_AST.__dict__[key][]))
                motherItem.appendRow([tmpA, tmpB, tmpC, tmpD])
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

    def readParseTreeForGrandChildren(self,grandparent_item=None,mother_item=None, _AST = None,key=None):
        if key not in _AST.__dict__:
            return

        for row in range(0,mother_item.rowCount()):
            # print(mother_item.rowCount())
            mother_item.removeRow(0)

        for childAST in _AST.__dict__[key]:   #### childConstraint is item in list!
            if type(childAST) == list:
                if type(childAST[0]) != list:   #Boundary case
                    print("List case display")
                    tmpC = QStandardItem(str(type(childAST)))
                    tmpD = str(childAST[0]) + ',' + str(childAST[1])
                    tmpD = QStandardItem(tmpD)
                    mother_item.appendRow([QStandardItem(), QStandardItem(), tmpC, tmpD])
                else:
                    for child_child_AST in childAST:
                        print("Doubled-list case display")
                        tmpC = QStandardItem(str(type(child_child_AST)))
                        tmpD = str(child_child_AST[0]) + ',' + str(child_child_AST[1])
                        tmpD = QStandardItem(tmpD)
                        mother_item.appendRow([QStandardItem(), QStandardItem(), tmpC, tmpD])
            elif type(childAST) == str:
                tmpA = QStandardItem(childAST)
                tmpD = QStandardItem(str(_AST.__dict__[key][childAST]))
                mother_item.appendRow([tmpA, QStandardItem(), QStandardItem(), tmpD])
            else:
                childASTid = childAST._id
                _type = childAST._type

                if self.findChildrenWithName(mother_item,childASTid) != None:
                    print("duplication Detect!")
                    print("duplication Item text",self.findChildrenWithName(mother_item,childASTid).text())
                    continue

                tmpA = QStandardItem(_type)
                tmpB = QStandardItem(childASTid)
                mother_item.appendRow([tmpA,tmpB,QStandardItem(_type),QStandardItem()])


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
        # logging.getLogger().addHandler(logTextBox)
        # You can control the logging level
        # logging.getLogger().setLevel(logging.DEBUG)

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
        self.manageListWidget.itemDoubleClicked.connect(self.item_double_clicked)

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
        self.deleteLater()

    def item_double_clicked(self, double_clicked_item):
        self.send_ModuleName_signal.emit(double_clicked_item.text())        #Current Module Name emit!!
        self.deleteLater()

    def on_createBox_accepted(self):
        pass

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_selectBox_accepted()
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.deleteLater()
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
        # print(val)

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

    def __init__(self,  _hierarchydict, dp):
        self.grouping = False
        try:
            if user_setup.DL_FEATURE:
                if not topAPI.element_predictor.model:
                    topAPI.element_predictor.model = topAPI.element_predictor.create_element_detector_model()
            else:
                self.inspector = topAPI.gds2generator.CellInspector()
            self.grouping = True
        except:
            import traceback
            traceback.print_exc()
        super().__init__()
        self.loop_obj = QEventLoop()
        self._hdict = _hierarchydict
        self.model = QTreeWidget()
        self.model.setColumnCount(5)
        self.model.setHeaderLabels(['Design Object', 'Cell Name', 'Flatten Option', 'Macro Cell', 'Generator Name'])
        self.dp = dp
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

    def ok_button_accepted(self, test=None):

        if test:
            pass
        else:
            self.loop_obj.exec_()

        _flatten_dict = dict()

        for item in self.itemlist:
            if self.model.itemWidget(item, 2).checkState() == 2:
                _flatten_dict[f'{item.text(0)}/{item.text(1)}'] = None
            elif self.model.itemWidget(item, 3).checkState() == 2:
                _flatten_dict[f'{item.text(0)}/{item.text(1)}'] = 'MacroCell'
            else:
                _flatten_dict[f'{item.text(0)}/{item.text(1)}'] = self.model.itemWidget(item, 4).currentText()
        # print(_flatten_dict)
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

        flattenCheck = QCheckBox()
        flattenCheck.setText(item.text(1))

        macroCheck = QCheckBox()
        macroCheck.setText(item.text(1))

        combo = QComboBox()
        combo.addItems(self.combolist)

        flattenCheck.setText('OFF')
        macroCheck.setText('OFF')
        combo.setEnabled(True)

        if self.grouping:
            if user_setup.DL_FEATURE:
                tmp_dp = self.dp[item.text(0)]
                tmp_delegator = dpdc_delegator.DesignDelegator(None)
                library_name = tmp_delegator.build_layer_matrix_by_dps(tmp_dp)
                module_index = combo.findText(library_name)
                if module_index != -1:
                    combo.setCurrentIndex(module_index)
            else:
                module_name = self.inspector.convert_pcell_name_to_generator_name(item.text(0))
                module_index = combo.findText(module_name)
                if module_index != -1:
                    combo.setCurrentIndex(module_index)

        flattenCheck.stateChanged.connect(self.ActivateCombobox)
        macroCheck.stateChanged.connect(self.ActivateCombobox)

        # self.model.setItemWidget(item, 1, cell_name)
        self.model.setItemWidget(item, 2, flattenCheck)
        self.model.setItemWidget(item, 3, macroCheck)
        self.model.setItemWidget(item, 4, combo)

    def ActivateCombobox(self, state):
        item = self.model.currentItem()
        siblingFlattenCheckbox = self.model.itemWidget(item, 2)
        siblingMacroCheckbox = self.model.itemWidget(item, 3)
        siblingcombobox = self.model.itemWidget(item, 4)

        if siblingFlattenCheckbox.checkState() == 2:
            siblingFlattenCheckbox.setText('ON')
            siblingMacroCheckbox.setEnabled(False)
            siblingcombobox.setEnabled(False)
        elif siblingMacroCheckbox.checkState() == 2:
            siblingMacroCheckbox.setText('ON')
            siblingFlattenCheckbox.setEnabled(False)
            siblingcombobox.setEnabled(False)
        else:
            siblingFlattenCheckbox.setText('OFF')
            siblingMacroCheckbox.setText('OFF')
            siblingFlattenCheckbox.setEnabled(True)
            siblingMacroCheckbox.setEnabled(True)
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
#
class DesignModifier(QWidget):
    send_update_qt_constraint_signal = pyqtSignal(str, dict)
    send_update_ast_signal = pyqtSignal("PyQt_PyObject")

    def __init__(self):
        super(DesignModifier, self).__init__()
        self.layer_list = LayerReader._LayerMapping
        self.form_layout_dict = dict()
        self.field_value_dict = {
            'Boundary': dict(
                name=QLineEdit(),
                layer=QComboBox(),
                width=QLineEdit(),
                height=QLineEdit()
            ),
            'Polygon': dict(
                name=QLineEdit(),
                layer=QComboBox(),
            ),
            'Path': dict(
                name=QLineEdit(),
                layer=QComboBox(),
                width=QLineEdit(),
            ),
            'Sref': dict(
            ),
            'MacroCell': dict(
                name=QLineEdit()
            ),
            'Text':dict(
                name=QLineEdit(),
                text=QLineEdit(),
            )

        }
        self.main_layout = QVBoxLayout()
        self.create_form()
        self.setLayout(self.main_layout)
        self.apply_button = QPushButton('Apply')
        self.apply_button.clicked.connect(self.update_constraint)
        self.main_layout.addWidget(self.apply_button)
        self.current_type = None
        self.current_ast = None

    def create_form(self):
        for type_name, value_widget_dict in self.field_value_dict.items():
            tmp_widget = QWidget()
            layout = QFormLayout()
            tmp_widget.setLayout(layout)
            self.form_layout_dict[type_name] = tmp_widget
            for field_name, input_widget in value_widget_dict.items():
                layout.addRow(QLabel(field_name), input_widget)
            self.main_layout.addWidget(tmp_widget)
            tmp_widget.hide()

    def update_form(self, design_const):
        if design_const._type == 'Array':
            return
        self.current_type = design_const._type
        if self.current_type == 'Sref':
            self.update_sref_form(design_const)
        for type_name, form_widget in self.form_layout_dict.items():
            if type_name == self.current_type:
                form_widget.show()
            else:
                form_widget.hide()

        for field in design_const._ast._fields:
            if field in self.field_value_dict[self.current_type]:
                if type(self.field_value_dict[self.current_type][field]) == QLineEdit:
                    self.field_value_dict[self.current_type][field].setText(str(design_const._ast.__dict__[field]))
                elif type(self.field_value_dict[self.current_type][field]) == QComboBox:
                    self.field_value_dict[self.current_type][field].clear()
                    self.field_value_dict[self.current_type][field].addItems(list(LayerReader._LayerMapping.keys()))
                    idx = self.field_value_dict[self.current_type][field].findText(design_const._ast.layer)
                    self.field_value_dict[self.current_type][field].setCurrentIndex(idx)
        self.current_ast = design_const._ast
        self.updateGeometry()

    def update_sref_form(self, design_const):
        layout = self.form_layout_dict['Sref'].layout()
        while layout.count() != 0:
            child = layout.takeAt(0)
            layout.removeWidget(child.widget())
            del child

        self.field_value_dict['Sref'].clear()
        for parameter, value in design_const._ast.parameters.items():
            input_widget = QLineEdit(str(value))
            self.field_value_dict['Sref'][parameter] = input_widget
            layout.addRow(QLabel(parameter), input_widget)

    def update_constraint(self):
        if not self.current_type:
            return

        tmp_ast = copy.deepcopy(self.current_ast)
        # tmp_ast.constraint_id = tmp_ast._id
        # tmp_ast._id = tmp_ast.name
        update_dict = dict()
        for field_name, widget in self.field_value_dict[self.current_type].items():
            if type(widget) == QLineEdit:
                update_dict[field_name] = widget.text()
            elif type(widget) == QComboBox:
                update_dict[field_name] = widget.currentText()

        if self.current_ast._type == 'Sref':
            #TODO
            # 이름 필드와 파라미터 필드 구분..
            tmp_ast.parameters.update(update_dict)
            # self.send_update_ast_signal.emit(self.current_ast)
        else:
            tmp_ast.__dict__.update(update_dict)
        # self.send_update_ast_signal.emit(self.current_ast)
        self.send_update_ast_signal.emit(tmp_ast)


        # self.send_update_qt_constraint_signal.emit(self.current_design_id, update_dict)





def get_id_return_module(id : str, type : str, moduleDict):
    """
    :param id:
    :param type: '_DesignParameter' or '_DesignConstraint'
    :return:
    """
    module = id
    candidate = re.sub(r'\d', '', id)
    iteration =0
    while 1:
        module = module[:-1]
        iteration += 1
        if module in moduleDict:
            return module
        if iteration >100:
            return candidate