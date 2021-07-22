from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# from PyQTInterface  import LayerInfo
from PyQTInterface.layermap  import LayerReader
from PyQTInterface  import VisualizationItem
from PyQTInterface  import VariableVisualItem
from PyQTInterface import calculator

from PyCodes import ASTmodule
from PyCodes import element_ast

import logging
from PyCodes import userDefineExceptions
from PyCodes import EnvForClientSetUp
from PyCodes import QTInterfaceWithAST

from DesignManager.VariableManager import variable_manager

import re, ast, time
import os


class VariableSetupWindow(QWidget):

    send_BoundarySetup_signal = pyqtSignal(VisualizationItem._VisualizationItem)
    send_BoundaryDesign_signal = pyqtSignal(dict)
    send_Destroy_signal = pyqtSignal(str)
    send_Warning_signal = pyqtSignal(str)
    send_DestroyTmpVisual_signal = pyqtSignal(VisualizationItem._VisualizationItem)
    send_output_dict_signal = pyqtSignal(dict)


    send_variableVisual_signal = pyqtSignal(VariableVisualItem.VariableVisualItem)

    def __init__(self,variable_type,vis_items=None,variable_obj=None,test=None):
        super().__init__()
        self.setMinimumHeight(500)
        self.setFixedWidth(300)
        self.variable_type = variable_type
        self.vis_items= vis_items
        self._QTObj = test
        self.itemList = list()
        self.output_dict = dict()
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

        if self.variable_type == 'c_array':
            self.output_dict['type'] = 'c_array'
            self.XY_source_ref = QLineEdit()
            self.XY_source_ref.field_name = 'XY_source_ref'
            self.XY_source_ref.setReadOnly(True)
            self.width_combo = QComboBox()
            self.width_combo.addItems(['Auto', 'Custom'])
            self.width_combo.currentTextChanged.connect(self.getWidth)
            self.width_input = QLineEdit()
            self.width_input.setStyleSheet("QLineEdit{background:rgb(222,222,222);}")
            self.width_input.setReadOnly(True)
            # self.XY_source_ref.textChanged.connect(self.update_output_dict)
            self.XY_target_ref = QLineEdit()
            self.XY_target_ref.field_name = 'XY_target_ref'
            self.XY_target_ref.setReadOnly(True)
            # self.XY_target_ref.textChanged.connect(self.update_output_dict)

            self.deleteItemList = QListWidget()

            hbox1 = QHBoxLayout()
            hbox2 = QHBoxLayout()
            cal_for_source = QPushButton()
            cal_for_source.setIcon(QIcon(os.getcwd().replace("\\",'/') + "/Image/cal.png"))
            cal_for_source.clicked.connect(self.showSourceCal)
            cal_for_target = QPushButton()
            cal_for_target.setIcon(QIcon(os.getcwd().replace("\\",'/') + "/Image/cal.png"))
            cal_for_target.clicked.connect(self.showTargetCal)
            hbox1.addWidget(self.XY_source_ref)
            hbox1.addWidget(cal_for_source)
            hbox2.addWidget(self.XY_target_ref)
            hbox2.addWidget(cal_for_target)

            self.rule = QComboBox()
            self.rule.field_name = 'rule'
            self.rule.addItems(['All', 'Even', 'Odd', 'Custom'])
            self.rule.currentTextChanged.connect(self.getRule)

            self.rule_input = QLineEdit()
            self.rule_input.setStyleSheet("QLineEdit{background:rgb(222,222,222);}")
            self.rule_input.setReadOnly(True)

            self.elements_dict_for_Label = []
            self.elements_dict_for_LineEdit = []
            # self.elements_dict_for_LineEdit.append(QLineEdit())
            # self.elements_dict_for_LineEdit.append(QLineEdit())
            self.ui_list_a.extend(['XY_source_ref', 'width', '', 'XY_target_ref', 'Rule', ''])  # ,'Element1','Element2'])
            self.ui_list_b.extend([hbox1, self.width_combo, self.width_input, hbox2, self.rule, self.rule_input])
            # self.ui_list_b.extend(self.elements_dict_for_LineEdit)
        elif self.variable_type == 'element array':
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
            try:
                self.setupVboxColumn2.addWidget(widget)
            except:
                self.setupVboxColumn2.addLayout(widget)

        setupBox.addLayout(self.setupVboxColumn1)
        setupBox.addLayout(self.setupVboxColumn2)

        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(setupBox)
        if self.variable_type == 'c_array':
            vbox.addWidget(self.deleteItemList)
        vbox.addStretch(3)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setWindowTitle('Constarint Setup Window')
        self.setGeometry(300,300,500,500)
        self.updateUI()
        if self.vis_items is not None:
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
        if self.variable_type_widget.text() == "c_array":
            if self.vis_items is not None:
                for i, vis_item in enumerate(self.vis_items):
                    id = vis_item._id
                    self.itemList.append(id)
                    self.deleteItemList.addItem(id)
                # self.elements_dict_for_Label.append(QLabel('Element '+str(i)))
                # self.elements_dict_for_LineEdit.append(QLineEdit(id))
                #
                # self.setupVboxColumn1.addWidget(self.elements_dict_for_Label[-1])
                # self.setupVboxColumn2.addWidget(self.elements_dict_for_LineEdit[-1])

        elif self.variable_type_widget.text() == "element array":
            for i, vis_item in enumerate(self.vis_items):
                id = vis_item._id
                self.elements_dict_for_Label.append(QLabel('Element '+str(i)))
                self.elements_dict_for_LineEdit.append(QLineEdit(id))

                self.setupVboxColumn1.addWidget(self.elements_dict_for_Label[-1])
                self.setupVboxColumn2.addWidget(self.elements_dict_for_LineEdit[-1])


            # strList = ["_pyCode"]
            # self.addQLabel(strList)
            # self.addQLine(len(strList))

    def getArray(self, test):
        input_text = test.text()
        name_flag = False
        _from = 0
        _end = 0
        for idx in range(len(input_text)):
            if input_text[idx] == "'":
                _end = idx
                if name_flag:
                    tmp_text = input_text[_from:_end]
                    self.deleteItemList.addItem(tmp_text)
                _from = idx+1
                name_flag = not name_flag

        self.show()

    def getWidth(self, text):
        if text == 'Auto':
            self.width_input.setStyleSheet("QLineEdit{background:rgb(222,222,222);}")
            self.width_input.setReadOnly(True)
        elif text == 'Custom':
            self.width_input.setStyleSheet("QLineEdit{background:rgb(255,255,255);}")
            self.width_input.setReadOnly(False)

    def getRule(self, text):
        if text == 'Custom':
            self.rule_input.setStyleSheet("QLineEdit{background:rgb(255,255,255);}")
            self.rule_input.setReadOnly(False)
        else:
            self.rule_input.setStyleSheet("QLineEdit{background:rgb(222,222,222);}")
            self.rule_input.setReadOnly(True)

    def clickFromScene(self, item):
        if 'cal' not in self.__dict__:
            itemID = item._id
            if itemID not in self.itemList:
                self.deleteItemList.addItem(itemID)
                self.itemList.append(itemID)

    def addQLabel(self,strList):
        for str in strList:
            self.setupVboxColumn1.addWidget(QLabel(str))
    def addQLine(self,num):
        for i in range(0,num):
            self.setupVboxColumn2.addWidget(QLineEdit())
    def on_buttonBox_accepted(self):
        if self.XY_source_ref.text() == '' or self.XY_target_ref.text() == '':
            self.warning = QMessageBox()
            self.warning.setText("Incomplete")
            self.warning.setIcon(QMessageBox.Warning)
            self.warning.show()
            return

        variable_vis_item = VariableVisualItem.VariableVisualItem()
        variable_vis_item.addToGroupFromList(self.vis_items)
        variable_info = dict()

        if self.variable_type == 'c_array':
            dp_id = self.XY_source_ref.text()[self.XY_source_ref.text().find("'")+1:-3]
            print(self._QTObj)
            dc_id = self._QTObj._qtProject._ElementManager.dp_id_to_dc_id[dp_id]
            print(dc_id)
            print(self.XY_source_ref.text())
            print(self.XY_target_ref.text())
            self.send_output_dict_signal.emit(self.output_dict)
        else:
            self.XY_base_text = self.XY_base.text()
            self.x_offset_text = self.x_offset.text()
            self.y_offset_text = self.y_offset.text()

            if ',' in self.XY_base_text:
                slicing = self.XY_base_text.find(',')
                self.XY_base_text = [[float(self.XY_base_text[:slicing]), float(self.XY_base_text[slicing + 1:])]]

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
        elif QKeyEvent.key() == Qt.Key_Delete:
            for item in self.deleteItemList.selectedItems():
                self.itemList.remove(item.text())
                row = self.deleteItemList.row(item)
                self.deleteItemList.takeItem(row)

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

    def showSourceCal(self):
        self.cal = calculator.nine_key_calculator(clipboard=QGuiApplication.clipboard(),purpose='source',address=self)
        self.cal.send_expression_signal.connect(self.exportedText)
        self.cal.show()

    def showTargetCal(self):
        self.cal = calculator.nine_key_calculator(clipboard=QGuiApplication.clipboard(),purpose='target',address=self)
        self.cal.send_expression_signal.connect(self.exportedText)
        self.cal.show()

    def exportedText(self, text, purpose):
        if self.variable_type == 'c_array':
            if purpose == 'source':
                self.XY_source_ref.setText(text)
            elif purpose == 'target':
                self.XY_target_ref.setText(text)

        del self.cal


class CustomQTableView(QTableView): ### QAbstractItemView class inherited

    send_dataChanged_signal = pyqtSignal(tuple)  # This Signal emits topLeft index & bottomRight index to DV Object

    def __init__(self):
        super(CustomQTableView, self).__init__()

    def dataChanged(self, *args, **kwargs): # args[0] : topLeft, args[1]: bottomRight, args[2]: roles
        super(CustomQTableView, self).dataChanged(*args, **kwargs)
        self.send_dataChanged_signal.emit(args)

class _DesignVariableManagerWindow(QWidget):

    send_variable_siganl = pyqtSignal(dict)
    send_changedData_signal = pyqtSignal(dict)
    selected_variable_item_id_signal = pyqtSignal(list)
    elementDict = dict()

    def __init__(self, itemDict):
        super().__init__()
        self.table = CustomQTableView()
        self.table.setShowGrid(False)
        self.table.verticalHeader().setVisible(False)
        self.itemDict = itemDict
        self.selectedItem = None
        self.initUI()

    def initUI(self):
        # print(self.itemDict)
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Name', 'Value'])

        labelInput = QLabel('Input :')
        self.lineEditInput = QLineEdit()

        self.variableDict = _createNewDesignVariable().variableDict
        self.idDict = _createNewDesignVariable().idDict
        self.filterList = list(self.idDict.keys())

        for key in self.variableDict:
            item1 = QStandardItem(self.variableDict[key]['DV'])
            item1.setTextAlignment(Qt.AlignCenter)
            item1.setEditable(False)
            item2 = QStandardItem(self.variableDict[key]['value'])
            # item2.setEditable(False)
            item2.setTextAlignment(Qt.AlignCenter)

            self.model.appendRow(item1)
            self.model.setItem(self.model.rowCount() - 1, 1, item2)

        addButton = QPushButton("Add", self)
        addButton.clicked.connect(self.add_clicked)
        checkButton = QPushButton("check", self)
        checkButton.clicked.connect(self.check_clicked)
        editButton = QPushButton("Edit", self)
        editButton.clicked.connect(self.edit_clicked)
        deleteButton = QPushButton("Delete", self)
        deleteButton.clicked.connect(self.delete_clicked)
        sendButton = QPushButton("Send", self)
        sendButton.clicked.connect(self.send_clicked)

        userInput = QHBoxLayout()

        userInput.addWidget(labelInput)
        userInput.addWidget(self.lineEditInput)

        button = QVBoxLayout()

        button1 = QHBoxLayout()
        button1.addWidget(addButton)
        button1.addStretch(2)
        button1.addWidget(checkButton)
        button1.addStretch(2)
        button1.addWidget(editButton)

        button2 = QHBoxLayout()
        button2.addWidget(deleteButton)
        button2.addStretch(2)
        button2.addWidget(sendButton)

        button.addLayout(button1)
        button.addLayout(button2)

        self.table.setModel(self.model)

        self.completer = QCompleter(self.filterList)
        self.lineEditInput.setCompleter(self.completer)

        self.arrangeWindow = QVBoxLayout()
        self.arrangeWindow.addLayout(userInput)
        self.arrangeWindow.addWidget(self.table)
        self.arrangeWindow.addLayout(button)

        self.setLayout(self.arrangeWindow)
        self.table.horizontalHeader().setDefaultSectionSize(127)
        self.table.resizeRowsToContents()

        self.model.itemChanged.connect(self.itemChanged)
        self.lineEditInput.textChanged.connect(self.filterVariables)
        self.table.clicked.connect(self.itemClicked)
        self.table.send_dataChanged_signal.connect(self.data_changed)

    def data_changed(self, inclusive_index):
        """
        This function is created by Minsu Kim in order to receive the signal from CustomQTableView object
        When Variable is changed, Update should be done in Constraint window as well
        """
        _index = inclusive_index[0]
        _nameindex = _index.siblingAtColumn(0)
        _valueindex = _index.siblingAtColumn(1)
        _valueitemid = _valueindex.data()
        _nameitemid = _nameindex.data()
        _changedvariabledict = dict(DV=_nameitemid, value=_valueitemid)
        for _vid, _varInfo in self.variableDict.items():
            _varName = list(_varInfo.values())[0]
            if (_changedvariabledict['DV'] == _varName):
                _vidOfChangedVar = _vid
                _VarDictWithID = dict()
                _VarDictWithID[_vidOfChangedVar] = _changedvariabledict
                self.send_changedData_signal.emit(_VarDictWithID)
                break

    def add_clicked(self):
        self.addWidget = _createNewDesignVariable()
        self.addWidget.show()
        self.addWidget.send_variable_signal.connect(self.updateList)

    def check_clicked(self):
        print('variableDict:', self.variableDict)
        print('idDict:', self.idDict)

    def edit_clicked(self):
        if self.selectedItem == None:
            self.msg = QMessageBox()
            self.msg.setText("Nothing selected")
            self.msg.show()
        else:
            vid = self.idDict[self.selectedItem]['vid']
            DV = self.variableDict[vid]['DV']
            value = self.variableDict[vid]['value']

            self.editWidget = _editDesignVariable(self, vid, DV, value)
            self.editWidget.show()
            self.selectedItem = None

    def delete_clicked(self):
        if self.selectedItem == None:
            self.msg = QMessageBox()
            self.msg.setText("Nothing selected")
            self.msg.show()
        else:
            vid = self.idDict[self.selectedItem]['vid']
            DV = self.variableDict[vid]['DV']

            del self.variableDict[vid]

            self.updateList([DV, None], 'delete')
            self.selectedItem = None

    def send_clicked(self):
        if self.selectedItem == None:
            self.msg = QMessageBox()
            self.msg.setText("Nothing selected")
            self.msg.show()
        else:
            vid = self.idDict[self.selectedItem]['vid']
            tmpdict = dict()
            tmpdict[vid] = self.variableDict[vid]

            self.send_variable_siganl.emit(tmpdict)

            self.selectedItem = None

    def updateList(self, variable_info_list, _type=None):
        _name, _value = variable_info_list[0], variable_info_list[1]
        name, value = QStandardItem(_name), QStandardItem(_value)
        name.setEditable(False)
        # value.setEditable(False)
        name.setTextAlignment(Qt.AlignCenter)
        value.setTextAlignment(Qt.AlignCenter)

        if _name in self.idDict:
            if _type == 'add':
                self.model.appendRow(name)
                self.model.setItem(self.model.rowCount() - 1, 1, value)
            elif _type == 'edit':
                self.model.setItem(self.selectedRow, 1, value)
            elif _type == 'delete':
                self.model.takeRow(self.selectedRow)

                del self.idDict[_name]
            else:
                pass
        else:
            if _type == 'edit':
                self.model.setItem(self.selectedRow, 0, name)
            else:
                self.model.appendRow(name)
                self.model.setItem(self.model.rowCount() - 1, 1, value)

        self.filterList = list(self.idDict.keys())
        self.completer = QCompleter(self.filterList)
        self.lineEditInput.setCompleter(self.completer)
        self.table.resizeRowsToContents()

    def itemChanged(self, item):
        row = item.index().row()
        _item = self.model.item(row).text()
        if _item in self.idDict:
            vid = self.idDict[_item]['vid']
            self.variableDict[vid]['value'] = item.text()

    def itemClicked(self, item):
        _item = self.model.item(item.row()).text()
        self.selectedRow = item.row()
        self.selectedItem = _item
        _idlist = self.idDict[_item]['id']
        self.selected_variable_item_id_signal.emit(_idlist)

    def manageElements(self, id, elements):
        self.elementDict[id] = elements
        # print(self.elementDict)

    def filterVariables(self):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(['Name', 'Value'])

        for variableName in self.idDict:
            if self.lineEditInput.text() in variableName:
                key = self.idDict[variableName]['vid']
                item1 = QStandardItem(self.variableDict[key]['DV'])
                item1.setTextAlignment(Qt.AlignCenter)
                item1.setEditable(False)
                item2 = QStandardItem(self.variableDict[key]['value'])
                # item2.setEditable(False)
                item2.setTextAlignment(Qt.AlignCenter)

                self.model.appendRow(item1)
                self.model.setItem(self.model.rowCount() - 1, 1, item2)
        self.table.resizeRowsToContents()


class _createNewDesignVariable(QWidget):

    send_variable_signal = pyqtSignal(list, str)
    variableDict = dict()
    idDict = dict()

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

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Enter or QKeyEvent.key() == Qt.Key_Return:
            self.ok_clicked()

    def ok_clicked(self):
        if self.name.text() == '':
            self.warning = QMessageBox()
            self.warning.setIcon(QMessageBox.Warning)
            self.warning.setText("Invalid Name")
            self.warning.show()
        else:
            self.addDVtodict(self.name.text(), type='value', value=self.value.text())
            self.send_variable_signal.emit([self.name.text(), self.value.text()], self.add)
            self.destroy()

    def cancel_clicked(self):
        self.destroy()

    def addDVtodict(self, DV, type, value):
        vid_list = list(self.variableDict.keys())
        if vid_list == []:
            vid = 'vid0'
        else:
            tmp = int(vid_list[-1][3:])+1
            vid = 'vid' + str(tmp)

        if DV not in self.idDict:
            self.idDict[DV] = {'vid':vid, 'id':list()}
            self.variableDict[vid] = {'DV':DV, 'value':None}

            if type == 'id':
                self.idDict[DV][type].append(value)
            elif type == 'value':
                self.variableDict[vid][type] = value

            self.add = 'add'

        else:
            self.add = None
            self.warning = QMessageBox()
            self.warning.setIcon(QMessageBox.Warning)
            self.warning.setText("This variable already exists")
            self.warning.show()

class _editDesignVariable(QWidget):

    send_DV_signal = pyqtSignal(list, str)

    def __init__(self, address, vid, DV, value):
        super().__init__()
        self.address = address
        self.vid = vid
        self.DV = DV
        self.value = value
        self.initUI()

    def initUI(self):
        self.variableDict = _createNewDesignVariable().variableDict
        self.idDict = _createNewDesignVariable().idDict

        self.send_DV_signal.connect(self.address.updateList)

        nameInput = QLabel('Name :')
        self.name = QLineEdit(self.DV)
        valueInput = QLabel('Value :')
        self.value = QLineEdit(self.value)

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

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Enter or QKeyEvent.key() == Qt.Key_Return:
            self.ok_clicked()

    def ok_clicked(self):
        if self.name.text() == '':
            self.warning = QMessageBox()
            self.warning.setIcon(QMessageBox.Warning)
            self.warning.setText("Invalid Name")
            self.warning.show()
        else:
            for _vid, info in self.variableDict.items():
                if _vid == self.vid:
                    pass
                elif info['DV'] == self.name.text():  # If Target name already exists in variable window: reject
                    self.warning = QMessageBox()
                    self.warning.setIcon(QMessageBox.Warning)
                    self.warning.setText("This Name Already Exists")
                    self.warning.show()
                    return

            self.variableDict[self.vid]['DV'] = self.name.text()
            self.variableDict[self.vid]['value'] = self.value.text()

            test_list = [self.name.text(), self.value.text()]

            self.send_DV_signal.emit(test_list, 'edit')

            if self.name.text() in self.idDict:
                self.idDict[self.name.text()] = self.idDict[self.DV]
            else:
                self.idDict[self.name.text()] = self.idDict[self.DV]
                del self.idDict[self.DV]

            self.destroy()

    def cancel_clicked(self):
        self.destroy()