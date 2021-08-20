from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# from PyQTInterface  import LayerInfo
from PyQTInterface.layermap  import LayerReader
from PyQTInterface  import VisualizationItem
from PyQTInterface import SetupWindow
from PyQTInterface  import VariableVisualItem
from PyQTInterface import calculator
import warnings
import traceback
from PyCodes import ASTmodule
from PyCodes import element_ast

import logging
from PyCodes import userDefineExceptions
from PyCodes import EnvForClientSetUp
from PyCodes import QTInterfaceWithAST

from DesignManager.VariableManager import variable_manager

import re, ast, time
import copy
import os


class VariableSetupWindow(QWidget):

    send_BoundarySetup_signal = pyqtSignal(VisualizationItem._VisualizationItem)
    send_BoundaryDesign_signal = pyqtSignal(dict)
    send_Destroy_signal = pyqtSignal(str)
    send_Warning_signal = pyqtSignal(str)
    # send_DestroyTmpVisual_signal = pyqtSignal(VisualizationItem._VisualizationItem)
    send_DestroyTmpVisual_signal = pyqtSignal(str)
    send_output_dict_signal = pyqtSignal(str, dict)
    send_clicked_item_signal = pyqtSignal(list)
    request_dummy_constraint_signal = pyqtSignal(str)


    send_variableVisual_signal = pyqtSignal(VariableVisualItem.VariableVisualItem)

    def __init__(self,variable_type,vis_items=None,variable_obj=None,group_ref_list=None,inspect_array_window_address=None):
        super().__init__()
        self._edit_id = None
        self.setMinimumHeight(500)
        self.setMinimumWidth(300)
        self.variable_type = variable_type
        self.flag_type = 'relative'
        self.vis_items= vis_items
        self.group_list = group_ref_list
        self.inspect_array_window_address = inspect_array_window_address
        self.itemList = list()
        self.relative_or_offset = 'relative'
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

    def button_image_change(self,checked):
        sender = self.sender()
        if checked:
            sender.setIcon(QIcon(QPixmap('./image/ON.png')))
            sender.setText("  Relative Expression  ")
            self.expressionType = 'relative'
        else:
            sender.setIcon(QIcon(QPixmap('./image/OFF.png')))
            sender.setText("  Offset Expression  ")
            self.expressionType = 'offset'

    def initUI(self):
        self.layout_list = []
        self.variable_type_widget = QComboBox()
        self.variable_type_widget.addItems(['boundary_array', 'path_array', 'sref_array'])
        self.variable_type_widget.setCurrentText(self.variable_type)
        self.variable_type_widget.currentTextChanged.connect(self.typeChanged)

        self.relative_or_offset_button = QPushButton()
        self.relative_or_offset_button.setIcon(QIcon(QPixmap('./image/ON.png')))
        self.relative_or_offset_button.setIconSize(QSize(50,30))
        self.relative_or_offset_button.setFlat(True)
        self.relative_or_offset_button.setCheckable(True)
        self.relative_or_offset_button.setChecked(True)
        self.relative_or_offset_button.setAutoFillBackground(False)
        self.relative_or_offset_button.toggled.connect(self.button_image_change)
        self.relative_or_offset_button.toggled.connect(self.change_ui)
        self.relative_or_offset_button.setText("  Relative Expression  ")

        self.ui_list_a_offset = ['_type', 'XY_ref', 'x_offset', 'y_offset']  # ,'Element1','Element2'])
        self.XY_source_ref = QLineEdit()
        self.x_offset = QLineEdit()
        self.y_offset = QLineEdit()
        hbox_xy = QHBoxLayout()
        cal_for_source = QPushButton()
        cal_for_source.setIcon(QIcon(os.getcwd().replace("\\", '/') + "/Image/cal.png"))
        cal_for_source.clicked.connect(self.showSourceCal)
        hbox_xy.addWidget(self.XY_source_ref)
        hbox_xy.addWidget(cal_for_source)
        self.ui_list_b_offset= [self.variable_type_widget, hbox_xy, self.x_offset, self.y_offset]

        # self.create_ui_relative()
        self.deleteItemList = QListWidget()

        self.okButton = QPushButton("OK",self)
        self.cancelButton = QPushButton("Cancel",self)

        self.okButton.clicked.connect(self.on_buttonBox_accepted)
        self.cancelButton.clicked.connect(self.cancel_button_accepted)

        self.setupVboxColumn1 = QVBoxLayout()
        self.setupVboxColumn2 = QVBoxLayout()
        self.setupBox = QHBoxLayout()
        self.layout_list.append(self.setupBox)

        self.setupVboxColumn2.addWidget(self.variable_type_widget)

        self.setupVboxColumn1.addWidget(QLabel("_type"))
        # tmp_list = []
        # for label in self.ui_list_a:
        #     label_widget = QLabel(label)
        #     self.setupVboxColumn1.addWidget(label_widget)
        #     tmp_list.append(label_widget)
        # self.ui_list_a = tmp_list
        # for widget in self.ui_list_b:
        #     try:
        #         self.setupVboxColumn2.addWidget(widget)
        #     except:
        #         self.setupVboxColumn2.addLayout(widget)

        self.setupBox.addLayout(self.setupVboxColumn1)
        self.setupBox.addLayout(self.setupVboxColumn2)

        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(self.okButton)
        hbox.addWidget(self.cancelButton)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(QLabel("_type"))
        hbox2.addWidget(self.variable_type_widget)

        vbox = QVBoxLayout()
        vbox.addWidget(self.relative_or_offset_button)
        vbox.addStretch(1)
        # vbox.addLayout(self.setupBox)
        self.variable_widget = variableContentWidget()
        self.variable_widget.request_show('boundary', 'relative')
        self.variable_widget.send_clicked_item_signal.connect(self.send_clicked_item)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.variable_widget)
        # if self.variable_type == 'path_array':
        vbox.addWidget(self.deleteItemList)
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        self.layout_list.extend([hbox,vbox])

        self.setLayout(vbox)

        self.setWindowTitle('Constarint Setup Window')
        self.setGeometry(300,300,500,500)
        # self.updateUI()
        if self.vis_items is not None:
            for vis_item in self.vis_items:
                id = vis_item._id
                self.itemList.append(id)
                self.deleteItemList.addItem(id)
            self.show()

    def typeChanged(self, variable_type):
        self.variable_type = variable_type
        if self.relative_or_offset_button.isChecked():
            self.variable_widget.request_show(variable_type[:-6], 'relative')
        else:
            self.variable_widget.request_show(variable_type[:-6], 'offset')

    def update_ui_by_constraint_id(self, dummy_id):
        self.deleteItemList.clear()
        self._edit_id = dummy_id
        self.request_dummy_constraint_signal.emit(dummy_id)
        self.variable_type_widget.setCurrentText(self.current_dummy_constraint['type'])
        self.variable_widget.request_load(self.current_dummy_constraint)
        self.show()

    def delivery_dummy_constraint(self, dummy_constraint):
        self.current_dummy_constraint = copy.deepcopy(dummy_constraint)

    def change_ui(self, _):
        if self.relative_or_offset_button.isChecked():
            self.variable_widget.request_show(self.variable_type[:-6], 'relative')
            self.flag_type = 'relative'
        else:
            self.variable_widget.request_show(self.variable_type[:-6], 'offset')
            self.flag_type = 'offset'


    def updateUI(self):
        #TODO
        #아마 필요 없는 fcn 인듯, 나중에 확인하고 삭제
        if self.vis_items is not None:
            for i, vis_item in enumerate(self.vis_items):
                id = vis_item._id
                self.itemList.append(id)
                self.deleteItemList.addItem(id)



        legacy = False
        if legacy:
            if self.variable_type_widget.text() == "path_array":
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
                if self.vis_items is not None:
                    for i, vis_item in enumerate(self.vis_items):
                        id = vis_item._id
                        self.deleteItemList.addItem(id)

    def getArray(self, array_list_item):
        self.deleteItemList.clear()
        for field_name in self.group_list:
            if field_name == 'XY_source_ref' or field_name == 'XY_target_ref':
                self.variable_widget.field_value_memory_dict[field_name] =\
                    'center(' + str(self.group_list[field_name])[1:-1] + ')'
            else:
                self.variable_widget.field_value_memory_dict[field_name] = self.group_list[field_name]
        array_list = eval(array_list_item.text())
        self.deleteItemList.addItems(array_list)
        self.variable_type_widget.setCurrentText(self.variable_type)
        self.variable_widget.request_show(self.variable_type[:-6], self.relative_or_offset)
        self.show()

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
        output_dict = self.variable_widget.field_value_memory_dict
        if output_dict['name'] == '':
            self.warning = QMessageBox()
            self.warning.setText("Incomplete Name")
            self.warning.setIcon(QMessageBox.Warning)
            self.warning.show()
            return
        if self.relative_or_offset == 'relative':
            if self.variable_type == 'path_array':
                if output_dict['XY_source_ref'] == '' or output_dict['XY_target_ref'] == '':
                    self.warning = QMessageBox()
                    self.warning.setText("Incomplete Source of Target")
                    self.warning.setIcon(QMessageBox.Warning)
                    self.warning.show()
                    return
            elif self.variable_type == 'boundary_array':
                if output_dict['XY_source_ref'] == '':
                    self.warning = QMessageBox()
                    self.warning.setText("Incomplete Source")
                    self.warning.setIcon(QMessageBox.Warning)
                    self.warning.show()
                    return
            elif self.variable_type == 'sref_array':
                if output_dict['XY_source_ref'] == '':
                    self.warning = QMessageBox()
                    self.warning.setText("Incomplete Source")
                    self.warning.setIcon(QMessageBox.Warning)
                    self.warning.show()
                    return
                if output_dict['sref_item'] == '':
                    self.warning = QMessageBox()
                    self.warning.setText("Incomplete SRef")
                    self.warning.setIcon(QMessageBox.Warning)
                    self.warning.show()
                    return
        elif self.relative_or_offset == 'offset':
            if output_dict['XY_ref'] == '':
                self.warning = QMessageBox()
                self.warning.setText("Incomplete Reference")
                self.warning.setIcon(QMessageBox.Warning)
                self.warning.show()
                return

        for idx in range(self.deleteItemList.count()):
            _id = self.deleteItemList.item(idx).text()
            self.send_DestroyTmpVisual_signal.emit(_id)

        output_dict['type'] = self.variable_type
        output_dict['flag'] = self.flag_type

        self.send_output_dict_signal.emit(self._edit_id, copy.deepcopy(output_dict))

        self.variable_widget.refresh_memory_dict()

        if self.inspect_array_window_address is not None:
            self.inspect_array_window_address.close()
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
        if self.variable_type == 'path_array':
            if purpose == 'source':
                self.XY_source_ref.takeItem(0)
                self.XY_source_ref.addItem(text)
                self.XY_source_ref.setCurrentRow(0)
            elif purpose == 'target':
                self.XY_target_ref.takeItem(0)
                self.XY_target_ref.addItem(text)
        if self.variable_type == 'boundary_array':
            self.XY_source_ref.takeItem(0)
            self.XY_source_ref.addItem(text)

        del self.cal

    def send_clicked_item(self, hierarchy_list):
        self.send_clicked_item_signal.emit(hierarchy_list)

class variableContentWidget(QWidget):
    send_clicked_item_signal = pyqtSignal(list)
    send_exported_width_height_signal = pyqtSignal(str, dict)
    send_width_height_ast_signal = pyqtSignal(str, ast.AST)

    def __init__(self):
        super(variableContentWidget, self).__init__()
        self.name_list = ['boundary', 'path', 'sref']
        self.option_list = ['offset', 'relative']
        self.widget_dictionary = dict()
        self.vbox = QVBoxLayout()
        self.field_value_memory_dict = dict()

        self.initUI()

    def initUI(self):
        for name in self.name_list:
            for option in self.option_list:
                field_info = self.return_field_list(name, option)
                for i, field_name in enumerate(field_info['field_list']):
                    self.field_value_memory_dict[field_name] = ''
                    if field_name == 'layer':
                        self.field_value_memory_dict[field_name] = 'PIMP'
                    if field_name == 'index':
                        self.field_value_memory_dict[field_name] = 'All'
                    if field_name == 'width':
                        self.field_value_memory_dict[field_name] = 'Auto'
                    if field_name == 'height':
                        self.field_value_memory_dict[field_name] = 'Auto'
                self.create_skeleton(name, option, field_info)

        self.setLayout(self.vbox)

    def refresh_memory_dict(self):
        for name in self.name_list:
            for option in self.option_list:
                field_info = self.return_field_list(name, option)
                for i, field_name in enumerate(field_info['field_list']):
                    self.field_value_memory_dict[field_name] = ''
                    if field_name == 'layer':
                        self.field_value_memory_dict[field_name] = 'PIMP'
                    if field_name == 'index':
                        self.field_value_memory_dict[field_name] = 'All'
                    if field_name == 'width':
                        self.field_value_memory_dict[field_name] = 'Auto'
                    if field_name == 'height':
                        self.field_value_memory_dict[field_name] = 'Auto'

    def request_load(self, output_dictionary):
        self.field_value_memory_dict = output_dictionary
        self.request_show(output_dictionary['type'][:-6], output_dictionary['flag'])

    def request_show(self, name, option):
        for widget in self.widget_dictionary.values():
            widget.hide()
        self.widget_dictionary[name+option].show()
        field_info = self.return_field_list(name, option)
        for i, field_name in enumerate(field_info['field_list']):
            row_layout = self.widget_dictionary[name+option].layout()
            if field_name in self.field_value_memory_dict:
                if field_info['input_type_list'][i] == 'line':
                    row_layout.itemAt(i).itemAt(1).widget().setText(str(self.field_value_memory_dict[field_name]))
                elif field_info['input_type_list'][i] == 'double_line':
                    row_layout.itemAt(i).itemAt(1).layout().itemAt(0).widget().setText(str(self.field_value_memory_dict['row']))
                    row_layout.itemAt(i).itemAt(1).layout().itemAt(1).widget().setText(str(self.field_value_memory_dict['col']))
                elif field_info['input_type_list'][i] == 'combo':
                    row_layout.itemAt(i).itemAt(1).widget().setCurrentText(str(self.field_value_memory_dict[field_name]))
                elif field_info['input_type_list'][i] == 'list':
                    row_layout.itemAt(i).itemAt(1).widget().addItem(self.field_value_memory_dict[field_name])
                    while row_layout.itemAt(i).itemAt(1).widget().count() != 1:
                        row_layout.itemAt(i).itemAt(1).widget().takeItem(0)
                    row_layout.itemAt(i).itemAt(1).widget().setCurrentRow(0)
            else:
                continue

    def create_skeleton(self, name, option, field_info):
        tmp_vbox= QVBoxLayout()
        for i, field_name in enumerate(field_info['field_list']):
            if field_info['input_type_list'][i] == 'line':
                tmp_layout = self.create_line_field(field_name)
            elif field_info['input_type_list'][i] == 'double_line':
                tmp_layout = self.create_double_line_field(field_name)
            elif field_info['input_type_list'][i] == 'combo':
                tmp_layout = self.create_combo_field(field_name)
            elif field_info['input_type_list'][i] == 'list':
                tmp_layout = self.create_list_field(field_name)
            tmp_vbox.addLayout(tmp_layout)
        tmp_widget = QWidget()
        tmp_widget.setLayout(tmp_vbox)
        self.widget_dictionary[name+option] = tmp_widget
        self.vbox.addWidget(tmp_widget)

    def return_field_list(self, name, option):
        if option == 'offset':
            if name == 'boundary':
                field_list = ['name', 'layer', 'XY_ref', 'width', 'width_text', 'height', 'height_text', 'x_offset',
                              'y_offset', 'row', 'col', 'width_input', 'height_input']
                input_type_list = ['line', 'combo', 'list', 'combo', 'line', 'combo', 'line', 'line', 'line',
                                   'double_line', None, None, None]
            elif name == 'path':
                field_list = ['name', 'layer', 'XY_ref', 'width', 'width_text', 'x_offset', 'y_offset', 'row', 'col', 'width_input']
                input_type_list = ['line', 'combo', 'list', 'combo', 'line', 'line', 'line', 'double_line', None, None]
            elif name == 'sref':
                field_list = ['name', 'XY_ref', 'x_offset', 'y_offset', 'row', 'col']
                input_type_list = ['line', 'list', 'line', 'line', 'double_line', None]
        elif option == 'relative':
            if name == 'boundary':
                field_list = ['name', 'layer', 'XY_source_ref', 'index', 'index_input', 'width', 'width_text',
                              'height', 'height_text', 'width_input', 'height_input']
                input_type_list = ['line', 'combo', 'list', 'combo', 'line', 'combo', 'line', 'combo', 'line', None, None]
            elif name == 'path':
                field_list = ['name', 'layer', 'XY_source_ref', 'index', 'index_input', 'width', 'width_text',
                              'XY_target_ref', 'width_input']
                input_type_list = ['line', 'combo', 'list', 'combo', 'line', 'combo', 'line', 'list', None]
            elif name == 'sref':
                field_list = ['name', 'XY_source_ref', 'sref_item', 'index', 'index_input', 'sref_item_dict']
                input_type_list = ['line', 'list', 'list', 'combo', 'line', None]

        field_info = dict(field_list=field_list, input_type_list=input_type_list)
        return field_info

    def create_line_field(self,name):
        tmp_label_widget = QLabel(name)
        tmp_label_widget.setFixedWidth(90)
        tmp_input_widget = QLineEdit()

        if name == 'index_input':
            tmp_input_widget.setStyleSheet("QLineEdit{background:rgb(222,222,222);}")
            tmp_input_widget.setReadOnly(True)
        elif name == 'width_text':
            tmp_input_widget.setStyleSheet("QLineEdit{background:rgb(222,222,222);}")
            tmp_input_widget.setReadOnly(True)
            additional_button = QPushButton()
            additional_button.setIcon(QIcon(os.getcwd().replace("\\", '/') + "/Image/cal.png"))
            additional_button.clicked.connect(self.show_width_cal)
        elif name == 'height_text':
            tmp_input_widget.setStyleSheet("QLineEdit{background:rgb(222,222,222);}")
            tmp_input_widget.setReadOnly(True)
            additional_button = QPushButton()
            additional_button.setIcon(QIcon(os.getcwd().replace("\\", '/') + "/Image/cal.png"))
            additional_button.clicked.connect(self.show_height_cal)

        tmp_input_widget.field_name = name
        tmp_input_widget.textChanged.connect(self.update_output_dict)

        output_layout = QHBoxLayout()
        output_layout.addWidget(tmp_label_widget)
        output_layout.addWidget(tmp_input_widget)
        if name == 'width_text' or name == 'height_text':
            output_layout.addWidget(additional_button)

        return output_layout

    def create_double_line_field(self, name):
        tmp_label_widget = QLabel('row x col')
        tmp_label_widget.setFixedWidth(90)
        tmp_input_widget1 = QLineEdit()
        tmp_input_widget2 = QLineEdit()
        tmp_input_widget1.field_name = 'row'
        tmp_input_widget1.textChanged.connect(self.update_output_dict)
        tmp_input_widget2.field_name = 'col'
        tmp_input_widget2.textChanged.connect(self.update_output_dict)

        rowcol_layout = QHBoxLayout()
        rowcol_layout.addWidget(tmp_input_widget1)
        rowcol_layout.addWidget(tmp_input_widget2)

        output_layout = QHBoxLayout()
        output_layout.addWidget(tmp_label_widget)
        output_layout.addLayout(rowcol_layout)

        return output_layout

    def create_combo_field(self, name):
        tmp_label_widget = QLabel(name)
        tmp_label_widget.setFixedWidth(90)
        tmp_input_widget = QComboBox()

        if name == 'layer':
            _Layer = LayerReader._LayerMapping
            for LayerName in _Layer:
                if _Layer[LayerName] == None:
                    warnings.warn(
                        f'Current Layer {LayerName} does not match any layer in current technology node.')
                    continue
                if _Layer[LayerName][1] == 0:
                    tmp_input_widget.addItem(LayerName)
        elif name == 'index':
            tmp_input_widget.addItems(['All', 'Even', 'Odd', 'Custom'])
            tmp_input_widget.currentTextChanged.connect(self.get_index)
        elif name == 'width':
            tmp_input_widget.addItems(['Auto', 'Custom'])
            tmp_input_widget.currentTextChanged.connect(self.get_width)
            tmp_input_widget.setCurrentIndex(1)
        elif name == 'height':
            tmp_input_widget.addItems(['Auto', 'Custom'])
            tmp_input_widget.currentTextChanged.connect(self.get_height)
            tmp_input_widget.setCurrentIndex(0)

        tmp_input_widget.field_name = name
        tmp_input_widget.currentTextChanged.connect(self.update_output_dict)

        output_layout = QHBoxLayout()
        output_layout.addWidget(tmp_label_widget)
        output_layout.addWidget(tmp_input_widget)

        return output_layout

    def create_list_field(self, name):
        tmp_label_widget = QLabel(name)
        tmp_label_widget.setFixedWidth(90)
        tmp_input_widget = QListWidget()
        tmp_input_widget.field_name = name

        if name == 'sref_item':
            additional_button = QPushButton()
            additional_button.setText('SRefLoad')
            additional_button.clicked.connect(self.show_sref_load)
        else:
            additional_button = QPushButton()
            additional_button.setIcon(QIcon(os.getcwd().replace("\\", '/') + "/Image/cal.png"))
            if name[3:-4] == 'source':
                additional_button.clicked.connect(self.show_source_cal)
            elif name[3:-4] == 'target':
                additional_button.clicked.connect(self.show_target_cal)
            elif name[3:-4] == '':
                additional_button.clicked.connect(self.show_ref_cal)
            tmp_input_widget.itemClicked.connect(self.item_clicked)

        tmp_input_widget.setMaximumHeight(20)
        tmp_input_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        tmp_input_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        tmp_input_widget.addItem('')
        tmp_input_widget.currentItemChanged.connect(self.update_output_dict)

        output_layout = QHBoxLayout()
        output_layout.addWidget(tmp_label_widget)
        output_layout.addWidget(tmp_input_widget)
        output_layout.addWidget(additional_button)

        return output_layout

    def show_sref_load(self):
        if self.field_value_memory_dict['sref_item'] == '':
            self.ls = SetupWindow._LoadSRefWindow(purpose='array_load')
        else:
            self.ls = SetupWindow._LoadSRefWindow(purpose='array_load', SRefElement=self.field_value_memory_dict['sref_item_dict'])
        self.ls.show()
        self.ls.send_array_signal.connect(self.exported_sref)
        # self.scene.send_xyCoordinate_signal.connect(self.ls.DetermineCoordinateWithMouse)
        # self.ls.send_destroy_signal.connect(self.delete_obj)

    def show_width_cal(self):
        self.cal = calculator.ExpressionCalculator(clipboard=QGuiApplication.clipboard(),purpose='width')
        self.cal.send_expression_signal.connect(self.exported_text)
        self.cal.send_dummyconstraints_signal.connect(self.cal.storePreset)
        self.cal.set_preset_window()
        self.cal.show()

    def show_height_cal(self):
        self.cal = calculator.ExpressionCalculator(clipboard=QGuiApplication.clipboard(),purpose='height')
        self.cal.send_expression_signal.connect(self.exported_text)
        self.cal.send_dummyconstraints_signal.connect(self.cal.storePreset)
        self.cal.set_preset_window()
        self.cal.show()

    def show_source_cal(self):
        self.cal = calculator.nine_key_calculator(clipboard=QGuiApplication.clipboard(),purpose='source',address=self)
        self.cal.send_expression_signal.connect(self.exported_text)
        self.cal.show()

    def show_target_cal(self):
        self.cal = calculator.nine_key_calculator(clipboard=QGuiApplication.clipboard(),purpose='target',address=self)
        self.cal.send_expression_signal.connect(self.exported_text)
        self.cal.show()

    def show_ref_cal(self):
        self.cal = calculator.nine_key_calculator(clipboard=QGuiApplication.clipboard(),purpose='ref',address=self)
        self.cal.send_expression_signal.connect(self.exported_text)
        self.cal.show()

    def exported_sref(self, sref_ast):
        sref_dict = sref_ast.__dict__

        source_widget = self.widget_dictionary['srefrelative'].layout().itemAt(2).itemAt(1).widget()
        source_widget.takeItem(0)
        source_widget.addItem(sref_dict['library'])
        source_widget.setCurrentRow(0)

        self.field_value_memory_dict['sref_item_dict'] = sref_dict

    def exported_text(self, text, purpose, output_dict):
        if purpose == 'width':
            self.width_height = 'width'
            self.output_dict = output_dict
            self.send_exported_width_height_signal.emit('LogicExpressionD', output_dict)

        elif purpose == 'height':
            self.width_height = 'height'
            self.output_dict = output_dict
            self.send_exported_width_height_signal.emit('LogicExpressionD', output_dict)

        elif purpose == 'source' or purpose == 'target' or purpose == 'ref':
            for info, widget in self.widget_dictionary.items():
                if not widget.isHidden():
                    if purpose == 'source':
                        if info == 'srefrelative':
                            source_widget = self.widget_dictionary[info].layout().itemAt(1).itemAt(1).widget()
                        else:
                            source_widget = self.widget_dictionary[info].layout().itemAt(2).itemAt(1).widget()
                        source_widget.takeItem(0)
                        source_widget.addItem(text)
                        source_widget.setCurrentRow(0)
                    elif purpose == 'target':
                        target_widget = self.widget_dictionary[info].layout().itemAt(7).itemAt(1).widget()
                        target_widget.takeItem(0)
                        target_widget.addItem(text)
                        target_widget.setCurrentRow(0)
                    elif purpose == 'ref':
                        if info == 'srefoffset':
                            ref_widget = self.widget_dictionary[info].layout().itemAt(1).itemAt(1).widget()
                        else:
                            ref_widget = self.widget_dictionary[info].layout().itemAt(2).itemAt(1).widget()
                        ref_widget.takeItem(0)
                        ref_widget.addItem(text)
                        ref_widget.setCurrentRow(0)

                    del self.cal

    def get_width_height_ast(self, _id, _ast):
        for info, widget in self.widget_dictionary.items():
            if not widget.isHidden():
                if info == 'boundaryrelative':
                    width_text_widget = self.widget_dictionary[info].layout().itemAt(6).itemAt(1).widget()
                    height_text_widget = self.widget_dictionary[info].layout().itemAt(8).itemAt(1).widget()
                elif info == 'pathrelative':
                    width_text_widget = self.widget_dictionary[info].layout().itemAt(6).itemAt(1).widget()
                elif info == 'boundaryoffset':
                    width_text_widget = self.widget_dictionary[info].layout().itemAt(4).itemAt(1).widget()
                    height_text_widget = self.widget_dictionary[info].layout().itemAt(6).itemAt(1).widget()
                elif info == 'pathoffset':
                    width_text_widget = self.widget_dictionary[info].layout().itemAt(4).itemAt(1).widget()
        try:
            if self.width_height == 'width':
                width_text_widget.setText(_id)
                self.field_value_memory_dict['width_input'] = _ast
            elif self.width_height == 'height':
                height_text_widget.setText(_id)
                self.field_value_memory_dict['height_input'] = _ast
            self.cal.send_dummyconstraints_signal.emit(self.output_dict, _id)
        except:
            traceback.print_exc()

    def get_index(self, text):
        for info, widget in self.widget_dictionary.items():
            if not widget.isHidden():
                index_input_widget = self.widget_dictionary[info].layout().itemAt(4).itemAt(1).widget()

                if text == 'Custom':
                    index_input_widget.setStyleSheet("QLineEdit{background:rgb(255,255,255);}")
                    index_input_widget.setReadOnly(False)
                else:
                    index_input_widget.setStyleSheet("QLineEdit{background:rgb(222,222,222);}")
                    index_input_widget.setReadOnly(True)

    def get_width(self, text):
        for info, widget in self.widget_dictionary.items():
            if not widget.isHidden():
                if info[-6:] == 'offset':
                    width_input_widget = self.widget_dictionary[info].layout().itemAt(4).itemAt(1).widget()
                elif info[-8:] == 'relative':
                    width_input_widget = self.widget_dictionary[info].layout().itemAt(6).itemAt(1).widget()

                if text == 'Custom':
                    width_input_widget.setStyleSheet("QLineEdit{background:rgb(255,255,255);}")
                    width_input_widget.setReadOnly(False)
                elif text == 'Auto':
                    width_input_widget.setStyleSheet("QLineEdit{background:rgb(222,222,222);}")
                    width_input_widget.setReadOnly(True)
                    if info == 'boundaryoffset':
                        height_widget = self.widget_dictionary[info].layout().itemAt(5).itemAt(1).widget()
                        height_widget.setCurrentText('Custom')
                    elif info == 'boundaryrelative':
                        height_widget = self.widget_dictionary[info].layout().itemAt(7).itemAt(1).widget()
                        height_widget.setCurrentText('Custom')

    def get_height(self, text):
        for info, widget in self.widget_dictionary.items():
            if not widget.isHidden():
                if info[-6:] == 'offset':
                    height_input_widget = self.widget_dictionary[info].layout().itemAt(6).itemAt(1).widget()
                    width_widget = self.widget_dictionary[info].layout().itemAt(3).itemAt(1).widget()
                elif info[-8:] == 'relative':
                    height_input_widget = self.widget_dictionary[info].layout().itemAt(8).itemAt(1).widget()
                    width_widget = self.widget_dictionary[info].layout().itemAt(5).itemAt(1).widget()

                if text == 'Custom':
                    height_input_widget.setStyleSheet("QLineEdit{background:rgb(255,255,255);}")
                    height_input_widget.setReadOnly(False)
                elif text == 'Auto':
                    height_input_widget.setStyleSheet("QLineEdit{background:rgb(222,222,222);}")
                    height_input_widget.setReadOnly(True)
                    width_widget.setCurrentText('Custom')

    def item_clicked(self, item):
        hierarchy_list = list(eval('['+re.search('\(.*\)',item.text()).group()[1:-1] + ']' ))
        self.send_clicked_item_signal.emit(hierarchy_list)

    def update_output_dict(self, changed_text):
        sender = self.sender()
        name = sender.field_name

        if type(changed_text) == QListWidgetItem:
            changed_text = changed_text.text()

        self.field_value_memory_dict[name] = changed_text


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