from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# from PyQTInterface  import LayerInfo
from PyQTInterface.layermap  import LayerReader
from PyQTInterface  import VisualizationItem
from PyQTInterface  import VariableVisualItem

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


    send_variableVisual_signal = pyqtSignal(VariableVisualItem.VariableVisualItem)

    def __init__(self,variable_type,vis_items=None,variable_obj=None):
        super().__init__()
        self.setMinimumHeight(500)
        self.setFixedWidth(300)
        self.variable_type = variable_type
        self.vis_items= vis_items
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
        self.variable_type_widget = QLabel(self.variable_type)
        # self.variable_type_widget.addItems(QLabel(self.variable_type))
        # self.variable_type_widget.currentIndexChanged.connect(self.updateUI)
        ui_list_a = []
        ui_list_b = []
        if self.variable_type == 'array':
            self.XY_base = QLineEdit()
            self.x_offset = QLineEdit()
            self.y_offset = QLineEdit()
            self.elements_dict_for_Label=[]
            self.elements_dict_for_LineEdit=[]
            # self.elements_dict_for_LineEdit.append(QLineEdit())
            # self.elements_dict_for_LineEdit.append(QLineEdit())
            ui_list_a.extend(['XY','x_offset','y_offset'])#,'Element1','Element2'])
            ui_list_b.extend([self.XY_base,self.x_offset,self.y_offset])
            # ui_list_b.extend(self.elements_dict_for_LineEdit)

        okButton = QPushButton("OK",self)
        cancelButton = QPushButton("Cancel",self)

        okButton.clicked.connect(self.on_buttonBox_accepted)
        cancelButton.clicked.connect(self.cancel_button_accepted)

        self.setupVboxColumn1 = QVBoxLayout()
        self.setupVboxColumn2 = QVBoxLayout()
        setupBox = QHBoxLayout()

        self.setupVboxColumn2.addWidget(self.variable_type_widget)

        self.setupVboxColumn1.addWidget(QLabel("_type"))
        for label in ui_list_a:
            self.setupVboxColumn1.addWidget(QLabel(label))
        for widget in ui_list_b:
            self.setupVboxColumn2.addWidget(widget)




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
        # while self.setupVboxColumn1.count() != 1:               # original typed content delete
        #     tmp = self.setupVboxColumn1.takeAt(1).widget()
        #     tmp.setParent(None)
        #     del tmp
        #     tmp = self.setupVboxColumn2.takeAt(1).widget()
        #     tmp.setParent(None)
        #     self.setupVboxColumn2.removeWidget(tmp)
        #     del tmp
        #
        # currentClassName = self.variable_type_widget.currentText() # like: If, While, Number ,...
        # tmpObj = self._ASTapi._createASTwithName(currentClassName)
        # strList = list(tmpObj._fields)
        # self.addQLabel(strList)
        # self.addQLine(len(strList))
        #

        if self.variable_type_widget.text() == "array":
            for i, vis_item in enumerate(self.vis_items):
                id = vis_item._id
                self.elements_dict_for_Label.append(QLabel('Element '+str(i)))
                self.elements_dict_for_LineEdit.append(QLineEdit(id))

                self.setupVboxColumn1.addWidget(self.elements_dict_for_Label[-1])
                self.setupVboxColumn2.addWidget(self.elements_dict_for_LineEdit[-1])


            # strList = ["_pyCode"]
            # self.addQLabel(strList)
            # self.addQLine(len(strList))

    def addQLabel(self,strList):
        for str in strList:
            self.setupVboxColumn1.addWidget(QLabel(str))
    def addQLine(self,num):
        for i in range(0,num):
            self.setupVboxColumn2.addWidget(QLineEdit())
    def on_buttonBox_accepted(self):
        variable_vis_item = VariableVisualItem.VariableVisualItem()
        variable_vis_item.addToGroupFromList(self.vis_items)
        # self.send_AST_signal.emit(_ASTobj)
        self.send_variableVisual_signal.emit(variable_vis_item)
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
            typeIndex = self.variable_type_widget.findText(type)
            if typeIndex != -1:
                self.variable_type_widget.setCurrentIndex(typeIndex)
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


