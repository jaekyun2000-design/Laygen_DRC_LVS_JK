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

from DesignManager.VariableManager import variable_manager

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
        self.ui_list_a = []
        self.ui_list_b = []
        self.ui_list_c = []
        if self.variable_type == 'element array':
            self.XY_base = QLineEdit()
            self.x_offset = QLineEdit()
            self.y_offset = QLineEdit()
            self.elements_dict_for_Label=[]
            self.elements_dict_for_LineEdit=[]
            # self.elements_dict_for_LineEdit.append(QLineEdit())
            # self.elements_dict_for_LineEdit.append(QLineEdit())
            self.ui_list_a.extend(['XY','x_space_distance','y_space_distance'])#,'Element1','Element2'])
            self.ui_list_b.extend([self.XY_base,self.x_offset,self.y_offset])
            # self.ui_list_b.extend(self.elements_dict_for_LineEdit)

        okButton = QPushButton("OK",self)
        cancelButton = QPushButton("Cancel",self)

        okButton.clicked.connect(self.on_buttonBox_accepted)
        cancelButton.clicked.connect(self.cancel_button_accepted)

        self.setupVboxColumn1 = QVBoxLayout()
        self.setupVboxColumn2 = QVBoxLayout()
        setupBox = QHBoxLayout()

        self.setupVboxColumn2.addWidget(self.variable_type_widget)

        self.setupVboxColumn1.addWidget(QLabel("_type"))
        for label in self.ui_list_a:
            self.setupVboxColumn1.addWidget(QLabel(label))
        for widget in self.ui_list_b:
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

        if self.variable_type_widget.text() == "element array":
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
        variable_info = dict()

        self.XY_base_text = self.XY_base.text()
        self.x_offset_text = self.x_offset.text()
        self.y_offset_text = self.y_offset.text()

        if ',' in self.XY_base_text:
            slicing = self.XY_base_text.find(',')
            self.XY_base_text = [[float(self.XY_base_text[:slicing]), float(self.XY_base_text[slicing + 1:])]]

        print(self.XY_base_text)
        print(type(self.XY_base_text))

        try:
            self.x_offset_text = float(self.x_offset.text())
        except:
            pass

        try:
            self.y_offset_text = float(self.y_offset.text())
        except:
            pass

        self.ui_list_c.extend([self.XY_base_text, self.x_offset_text, self.y_offset_text])

        for i, key in enumerate(self.ui_list_a):
            variable_info[key] = self.ui_list_c[i]
        if self.variable_type == 'element array':
            tmp_list = []
            for i in range(len(self.elements_dict_for_LineEdit)):
                tmp_list.append(self.elements_dict_for_LineEdit[i].text())
            variable_info['elements'] = tmp_list
        variable_vis_item._DesignParametertype= self.variable_type
        variable_vis_item.set_variable_info(variable_info)
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
            type = self._ParseTree['_DesignParametertype']
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


class _DesignVariableManagerWindow(QWidget):

    send_destroy_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.table = QTableView()
        self.table.setShowGrid(False)
        self.table.verticalHeader().setVisible(False)
        self.initUI()

    def initUI(self):
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Name', 'Value'])

        variableDict = _createNewDesignVariable().variableDict

        for key in variableDict:
            item1 = QStandardItem(key)
            item1.setTextAlignment(Qt.AlignCenter)
            item2 = QStandardItem(variableDict[key])
            item2.setTextAlignment(Qt.AlignCenter)

            self.model.appendRow(item1)
            self.model.setItem(self.model.rowCount()-1,1,item2)

            self.table.resizeRowsToContents()

        addButton = QPushButton("Add", self)
        addButton.clicked.connect(self.add_clicked)
        quitButton = QPushButton("Quit", self)
        quitButton.clicked.connect(self.quit_clicked)

        button = QHBoxLayout()
        button.addWidget(addButton)
        button.addStretch(2)
        button.addWidget(quitButton)

        self.table.setModel(self.model)

        self.arrangeWindow = QVBoxLayout()
        self.arrangeWindow.addWidget(self.table)
        self.arrangeWindow.addLayout(button)

        self.setLayout(self.arrangeWindow)
        self.table.horizontalHeader().setDefaultSectionSize(127)

    def add_clicked(self):
        self.addWidget = _createNewDesignVariable()
        self.addWidget.show()
        self.addWidget.send_variable_signal.connect(self.updateList)

    def quit_clicked(self):
        self.send_destroy_signal.emit('dv')
        self.destroy()

    def updateList(self, variable_info_list):
        _name, _value = variable_info_list[0], variable_info_list[1]
        name, value = QStandardItem(_name), QStandardItem(_value)
        name.setTextAlignment(Qt.AlignCenter)
        value.setTextAlignment(Qt.AlignCenter)

        self.model.appendRow(name)
        self.model.setItem(self.model.rowCount()-1,1,value)

        self.table.resizeRowsToContents()


        #add버튼 추가해서 직접 만들기, manager에 없는 경우 자동 생성


class _createNewDesignVariable(QWidget):

    send_variable_signal = pyqtSignal(list)
    variableDict = dict()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        nameInput = QLabel('Name :')
        self.name = QLineEdit()
        valueInput = QLabel('Value :')
        self.value = QLineEdit()

        okButton = QPushButton("OK", self)
        okButton.clicked.connect(self.ok_clicked)
        cancelButton = QPushButton("Cancel", self)
        cancelButton.clicked.connect(self.cancel_clicked)

        button = QHBoxLayout()
        button.addStretch(2)
        button.addWidget(okButton)
        button.addWidget(cancelButton)

        self.inputBox1 = QVBoxLayout()
        self.inputBox2 = QVBoxLayout()
        arrangeWindow = QHBoxLayout()

        vbox = QVBoxLayout()

        self.inputBox1.addWidget(nameInput)
        self.inputBox1.addWidget(valueInput)

        self.inputBox2.addWidget(self.name)
        self.inputBox2.addWidget(self.value)

        arrangeWindow.addLayout(self.inputBox1)
        arrangeWindow.addLayout(self.inputBox2)

        vbox.addLayout(arrangeWindow)
        vbox.addLayout(button)

        self.setLayout(vbox)

    def ok_clicked(self):
        self.send_variable_signal.emit([self.name.text(), self.value.text()])
        self.variableDict[self.name.text()] = self.value.text()
        self.destroy()

    def cancel_clicked(self):
        self.destroy()

    def get_DV(self):
        self.vm = variable_manager.Manage_DV_by_id()
        self.vm.send_DV_signal.connect(self.add_DV())

    def add_DV(self, DV):
        self.variableDict[DV] = ''