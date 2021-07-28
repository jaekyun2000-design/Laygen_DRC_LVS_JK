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
    # send_DestroyTmpVisual_signal = pyqtSignal(VisualizationItem._VisualizationItem)
    send_DestroyTmpVisual_signal = pyqtSignal(str)
    send_output_dict_signal = pyqtSignal(dict)


    send_variableVisual_signal = pyqtSignal(VariableVisualItem.VariableVisualItem)

    def __init__(self,variable_type,vis_items=None,variable_obj=None,ref_list=None,inspect_array_window_address=None):
        super().__init__()
        self.setMinimumHeight(500)
        self.setFixedWidth(300)
        self.variable_type = variable_type
        self.vis_items= vis_items
        self.group_list = ref_list
        self.inspect_array_window_address = inspect_array_window_address
        self.itemList = list()
        self.output_dict = dict()
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
        else:
            sender.setIcon(QIcon(QPixmap('./image/OFF.png')))
            sender.setText("  Offset Expression  ")

    def initUI(self):
        self.layout_list = []
        self.variable_type_widget = QComboBox()
        self.variable_type_widget.addItems(['boundary_array', 'path_array', 'sref_array'])
        self.variable_type_widget.setCurrentText(self.variable_type)
        self.variable_type_widget.currentTextChanged.connect(self.typeChanged)
        # self.variable_type_widget.addItems(QLabel(self.variable_type))
        # self.variable_type_widget.currentIndexChanged.connect(self.updateUI)
        self.ui_list_a = []
        self.ui_list_b = []
        self.ui_list_c = []
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

        self.create_ui_relative()
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
        tmp_list = []
        for label in self.ui_list_a:
            label_widget = QLabel(label)
            self.setupVboxColumn1.addWidget(label_widget)
            tmp_list.append(label_widget)
        self.ui_list_a = tmp_list
        for widget in self.ui_list_b:
            try:
                self.setupVboxColumn2.addWidget(widget)
            except:
                self.setupVboxColumn2.addLayout(widget)

        self.setupBox.addLayout(self.setupVboxColumn1)
        self.setupBox.addLayout(self.setupVboxColumn2)

        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(self.okButton)
        hbox.addWidget(self.cancelButton)

        vbox = QVBoxLayout()
        vbox.addWidget(self.relative_or_offset_button)
        vbox.addStretch(1)
        vbox.addLayout(self.setupBox)
        # if self.variable_type == 'path_array':
        vbox.addWidget(self.deleteItemList)
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        self.layout_list.extend([hbox,vbox])

        if self.variable_type == 'boundary_array':
            self.output_dict['width'] = 'Auto'
            self.output_dict['length'] = 'Auto'
            self.output_dict['index'] = 'All'
        elif self.variable_type == 'path_array':
            self.output_dict['width'] = 'Auto'
            self.output_dict['index'] = 'All'
        elif self.variable_type == 'sref_array':
            self.output_dict['index'] = 'All'

        self.setLayout(vbox)

        self.setWindowTitle('Constarint Setup Window')
        self.setGeometry(300,300,500,500)
        self.updateUI()
        if self.vis_items is not None:
            self.show()

    def update_ui(self):
        tmp_list = []
        for label in self.ui_list_a:
            label_widget = QLabel(label)
            self.setupVboxColumn1.addWidget(label_widget)
            tmp_list.append(label_widget)
        self.ui_list_a = tmp_list
        for widget in self.ui_list_b:
            try:
                self.setupVboxColumn2.addWidget(widget)
            except:
                self.setupVboxColumn2.addLayout(widget)

    def typeChanged(self, variable_type):
        self.variable_type = variable_type
        self.reset_ui()
        self.create_ui_relative()
        self.update_ui()

    def create_ui_relative(self):
        self.ui_list_a = []
        self.ui_list_b = []
        self.ui_list_c = []
        if self.variable_type == 'path_array':
            self.output_dict['type'] = 'path_array'
            # self.XY_source_ref = QLineEdit()
            # self.XY_source_ref.field_name = 'XY_source_ref'
            # self.XY_source_ref.textChanged.connect(self.update_output_dict)
            # self.XY_source_ref.setReadOnly(True)
            # self.XY_source_ref.textChanged.connect(self.update_output_dict)
            # self.XY_source_ref.setReadOnly(True)
            self.XY_source_ref = QListWidget()
            self.XY_source_ref.field_name = 'XY_source_ref'
            self.XY_source_ref.setMaximumHeight(20)
            self.XY_source_ref.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.XY_source_ref.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.XY_source_ref.itemClicked.connect(self.showClickedItem)
            self.XY_source_ref.currentItemChanged.connect(self.showClickedItem)
            self.XY_source_ref.currentItemChanged.connect(self.update_output_dict)
            self.width_combo = QComboBox()
            self.width_combo.addItems(['Auto', 'Custom'])
            self.width_combo.field_name = 'width'
            self.width_combo.currentTextChanged.connect(self.getWidth)
            self.width_combo.currentTextChanged.connect(self.update_output_dict)
            self.width_input = QLineEdit()
            self.width_input.setStyleSheet("QLineEdit{background:rgb(222,222,222);}")
            self.width_input.setReadOnly(True)
            self.width_input.field_name = 'width'
            self.width_input.textChanged.connect(self.update_output_dict)
            # self.XY_target_ref = QLineEdit()
            # self.XY_target_ref.field_name = 'XY_target_ref'
            # self.XY_target_ref.setReadOnly(True)
            # self.XY_target_ref.textChanged.connect(self.update_output_dict)
            self.XY_target_ref = QListWidget()
            self.XY_target_ref.field_name = 'XY_target_ref'
            self.XY_target_ref.setMaximumHeight(20)
            self.XY_target_ref.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.XY_target_ref.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.XY_target_ref.itemClicked.connect(self.showClickedItem)
            self.XY_target_ref.currentItemChanged.connect(self.showClickedItem)
            self.XY_target_ref.currentItemChanged.connect(self.update_output_dict)


            hbox1 = QHBoxLayout()
            hbox2 = QHBoxLayout()
            self.layout_list.extend([hbox1,hbox2])
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

            self.index = QComboBox()
            self.index.field_name = 'index'
            self.index.addItems(['All', 'Even', 'Odd', 'Custom'])
            self.index.currentTextChanged.connect(self.getIndex)
            self.index.currentTextChanged.connect(self.update_output_dict)

            self.index_input = QLineEdit()
            self.index_input.setStyleSheet("QLineEdit{background:rgb(222,222,222);}")
            self.index_input.setReadOnly(True)
            self.index_input.field_name = 'index'
            self.index_input.textChanged.connect(self.update_output_dict)

            self.elements_dict_for_Label = []
            self.elements_dict_for_LineEdit = []
            # self.elements_dict_for_LineEdit.append(QLineEdit())
            # self.elements_dict_for_LineEdit.append(QLineEdit())
            self.ui_list_a.extend(['XY_source_ref', 'width', '', 'XY_target_ref', 'index', ''])  # ,'Element1','Element2'])
            self.ui_list_b.extend([hbox1, self.width_combo, self.width_input, hbox2, self.index, self.index_input])
            # self.ui_list_b.extend(self.elements_dict_for_LineEdit)
        elif self.variable_type == 'boundary_array':
            self.output_dict['type'] = 'boundary_array'
            # self.XY_source_ref = QLineEdit()
            # self.XY_source_ref.field_name = 'XY_source_ref'
            # self.XY_source_ref.textChanged.connect(self.update_output_dict)
            # self.XY_source_ref.setReadOnly(True)
            self.XY_source_ref = QListWidget()
            self.XY_source_ref.field_name = 'XY_source_ref'
            self.XY_source_ref.setMaximumHeight(20)
            self.XY_source_ref.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.XY_source_ref.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.XY_source_ref.itemClicked.connect(self.showClickedItem)
            self.XY_source_ref.currentItemChanged.connect(self.showClickedItem)
            self.XY_source_ref.currentItemChanged.connect(self.update_output_dict)
            self.width_combo = QComboBox()
            self.width_combo.addItems(['Auto', 'Custom'])
            self.width_combo.field_name = 'width'
            self.width_combo.currentTextChanged.connect(self.getWidth)
            self.width_combo.currentTextChanged.connect(self.update_output_dict)
            self.width_input = QLineEdit()
            self.width_input.setStyleSheet("QLineEdit{background:rgb(222,222,222);}")
            self.width_input.setReadOnly(True)
            self.width_input.field_name = 'width'
            self.width_input.textChanged.connect(self.update_output_dict)
            self.length_combo = QComboBox()
            self.length_combo.addItems(['Auto', 'Custom'])
            self.length_combo.field_name = 'length'
            self.length_combo.currentTextChanged.connect(self.getLength)
            self.length_combo.currentTextChanged.connect(self.update_output_dict)
            self.length_input = QLineEdit()
            self.length_input.setStyleSheet("QLineEdit{background:rgb(222,222,222);}")
            self.length_input.setReadOnly(True)
            self.length_input.field_name = 'length'
            self.length_input.textChanged.connect(self.update_output_dict)


            hbox1 = QHBoxLayout()
            self.layout_list.append(hbox1)
            cal_for_source = QPushButton()
            cal_for_source.setIcon(QIcon(os.getcwd().replace("\\", '/') + "/Image/cal.png"))
            cal_for_source.clicked.connect(self.showSourceCal)
            hbox1.addWidget(self.XY_source_ref)
            hbox1.addWidget(cal_for_source)

            self.index = QComboBox()
            self.index.field_name = 'index'
            self.index.addItems(['All', 'Even', 'Odd', 'Custom'])
            self.index.currentTextChanged.connect(self.getIndex)
            self.index.currentTextChanged.connect(self.update_output_dict)

            self.index_input = QLineEdit()
            self.index_input.setStyleSheet("QLineEdit{background:rgb(222,222,222);}")
            self.index_input.setReadOnly(True)
            self.index_input.field_name = 'index'
            self.index_input.textChanged.connect(self.update_output_dict)

            self.elements_dict_for_Label = []
            self.elements_dict_for_LineEdit = []
            # self.elements_dict_for_LineEdit.append(QLineEdit())
            # self.elements_dict_for_LineEdit.append(QLineEdit())
            self.ui_list_a.extend(
                ['XY_source_ref', 'width', '', 'length', '',  'index', ''])  # ,'Element1','Element2'])
            self.ui_list_b.extend([hbox1, self.width_combo, self.width_input, self.length_combo, self.length_input, self.index, self.index_input])
            # self.ui_list_b.extend(self.elements_dict_for_LineEdit)

        elif self.variable_type == 'sref_array':
            self.output_dict['type'] = 'sref_array'
            # self.XY_source_ref = QLineEdit()
            # self.XY_source_ref.field_name = 'XY_source_ref'
            # self.XY_source_ref.textChanged.connect(self.update_output_dict)
            # self.XY_source_ref.setReadOnly(True)
            self.XY_source_ref = QListWidget()
            self.XY_source_ref.field_name = 'XY_source_ref'
            self.XY_source_ref.setMaximumHeight(20)
            self.XY_source_ref.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.XY_source_ref.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.XY_source_ref.itemClicked.connect(self.showClickedItem)
            self.XY_source_ref.currentItemChanged.connect(self.showClickedItem)
            self.XY_source_ref.currentItemChanged.connect(self.update_output_dict)


            hbox1 = QHBoxLayout()
            cal_for_source = QPushButton()
            cal_for_source.setIcon(QIcon(os.getcwd().replace("\\", '/') + "/Image/cal.png"))
            cal_for_source.clicked.connect(self.showSourceCal)
            hbox1.addWidget(self.XY_source_ref)
            hbox1.addWidget(cal_for_source)
            self.layout_list.append(hbox1)

            self.index = QComboBox()
            self.index.field_name = 'index'
            self.index.addItems(['All', 'Even', 'Odd', 'Custom'])
            self.index.currentTextChanged.connect(self.getIndex)
            self.index.currentTextChanged.connect(self.update_output_dict)

            self.index_input = QLineEdit()
            self.index_input.setStyleSheet("QLineEdit{background:rgb(222,222,222);}")
            self.index_input.setReadOnly(True)
            self.index_input.field_name = 'index'
            self.index_input.textChanged.connect(self.update_output_dict)

            self.elements_dict_for_Label = []
            self.elements_dict_for_LineEdit = []
            self.ui_list_a.extend(
                ['XY_source_ref', 'index', ''])  # ,'Element1','Element2'])
            self.ui_list_b.extend([hbox1, self.index, self.index_input])
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




    def create_ui_offset(self):
        self.ui_list_a = []
        self.ui_list_b = []
        self.ui_list_c = []

        self.x_offset = QLineEdit()
        self.y_offset = QLineEdit()
        self.row_col = QHBoxLayout()
        self.row = QLineEdit()
        self.col = QLineEdit()
        self.row_col.addWidget(self.row)
        self.row_col.addWidget(self.col)

        if self.variable_type == 'path_array':
            self.output_dict['type'] = 'path_array'
            self.XY_ref = QLineEdit()
            self.XY_ref.field_name = 'XY_ref'
            self.XY_ref.textChanged.connect(self.update_output_dict)
            self.XY_ref.setReadOnly(True)
            self.width_combo = QComboBox()
            self.width_combo.addItems(['Auto', 'Custom'])
            self.width_combo.field_name = 'width'
            self.width_combo.currentTextChanged.connect(self.getWidth)
            self.width_combo.currentTextChanged.connect(self.update_output_dict)
            self.width_input = QLineEdit()
            self.width_input.setStyleSheet("QLineEdit{background:rgb(222,222,222);}")
            self.width_input.setReadOnly(True)
            self.width_input.field_name = 'width'
            self.width_input.textChanged.connect(self.update_output_dict)


            hbox1 = QHBoxLayout()
            cal_for_source = QPushButton()
            cal_for_source.setIcon(QIcon(os.getcwd().replace("\\", '/') + "/Image/cal.png"))
            cal_for_source.clicked.connect(self.showSourceCal)
            hbox1.addWidget(self.XY_source_ref)
            hbox1.addWidget(cal_for_source)

            self.elements_dict_for_Label = []
            self.elements_dict_for_LineEdit = []

            self.ui_list_a.extend(
                ['XY_ref', 'width', '', 'x_offset', 'y_offset', 'row x col'])  # ,'Element1','Element2'])
            self.ui_list_b.extend([hbox1, self.width_combo, self.width_input, self.x_offset, self.y_offset, self.row_col])
            # self.ui_list_b.extend(self.elements_dict_for_LineEdit)
        elif self.variable_type == 'boundary_array':
            self.output_dict['type'] = 'boundary_array'
            self.XY_ref = QLineEdit()
            self.XY_ref.field_name = 'XY_ref'
            self.XY_ref.textChanged.connect(self.update_output_dict)
            self.XY_ref.setReadOnly(True)
            self.width_combo = QComboBox()
            self.width_combo.addItems(['Auto', 'Custom'])
            self.width_combo.field_name = 'width'
            self.width_combo.currentTextChanged.connect(self.getWidth)
            self.width_combo.currentTextChanged.connect(self.update_output_dict)
            self.width_input = QLineEdit()
            self.width_input.setStyleSheet("QLineEdit{background:rgb(222,222,222);}")
            self.width_input.setReadOnly(True)
            self.width_input.field_name = 'width'
            self.width_input.textChanged.connect(self.update_output_dict)
            self.length_combo = QComboBox()
            self.length_combo.addItems(['Auto', 'Custom'])
            self.length_combo.field_name = 'length'
            self.length_combo.currentTextChanged.connect(self.getLength)
            self.length_combo.currentTextChanged.connect(self.update_output_dict)
            self.length_input = QLineEdit()
            self.length_input.setStyleSheet("QLineEdit{background:rgb(222,222,222);}")
            self.length_input.setReadOnly(True)
            self.length_input.field_name = 'length'
            self.length_input.textChanged.connect(self.update_output_dict)

            hbox1 = QHBoxLayout()
            self.layout_list.append(hbox1)
            cal_for_source = QPushButton()
            cal_for_source.setIcon(QIcon(os.getcwd().replace("\\", '/') + "/Image/cal.png"))
            cal_for_source.clicked.connect(self.showSourceCal)
            hbox1.addWidget(self.XY_source_ref)
            hbox1.addWidget(cal_for_source)


            self.elements_dict_for_Label = []
            self.elements_dict_for_LineEdit = []
            # self.elements_dict_for_LineEdit.append(QLineEdit())
            # self.elements_dict_for_LineEdit.append(QLineEdit())
            self.ui_list_a.extend(
                ['XY_ref', 'width', '', 'length', '', 'x_offset', 'y_offset', 'row x col'])  # ,'Element1','Element2'])
            self.ui_list_b.extend(
                [hbox1, self.width_combo, self.width_input, self.length_combo, self.length_input,
                 self.x_offset, self.y_offset, self.row_col])
            # self.ui_list_b.extend(self.elements_dict_for_LineEdit)

        elif self.variable_type == 'sref_array':
            self.output_dict['type'] = 'sref_array'
            self.XY_ref = QLineEdit()
            self.XY_ref.field_name = 'XY_ref'
            self.XY_ref.textChanged.connect(self.update_output_dict)
            self.XY_ref.setReadOnly(True)

            hbox1 = QHBoxLayout()
            cal_for_source = QPushButton()
            cal_for_source.setIcon(QIcon(os.getcwd().replace("\\", '/') + "/Image/cal.png"))
            cal_for_source.clicked.connect(self.showSourceCal)
            hbox1.addWidget(self.XY_source_ref)
            hbox1.addWidget(cal_for_source)
            self.layout_list.append(hbox1)

            self.elements_dict_for_Label = []
            self.elements_dict_for_LineEdit = []
            self.ui_list_a.extend(
                ['XY_source_ref', 'x_offset', 'y_offset', 'row x col'])  # ,'Element1','Element2'])
            self.ui_list_b.extend([hbox1, self.x_offset, self.y_offset, self.row_col])
            # self.ui_list_b.extend(self.elements_dict_for_LineEdit)


        elif self.variable_type == 'element array':
            self.XY_base = QLineEdit()
            self.x_offset = QLineEdit()
            self.y_offset = QLineEdit()
            self.elements_dict_for_Label = []
            self.elements_dict_for_LineEdit = []
            # self.elements_dict_for_LineEdit.append(QLineEdit())
            # self.elements_dict_for_LineEdit.append(QLineEdit())
            self.ui_list_a.extend(['XY', 'x_space_distance', 'y_space_distance'])  # ,'Element1','Element2'])
            self.ui_list_b.extend([self.XY_base, self.x_offset, self.y_offset])

            # self.ui_list_b.extend(self.elements_dict_for_LineEdit)


    def reset_ui(self):
        while self.setupVboxColumn1.count() != 1:
            # tmp = self.setupVboxColumn1.takeAt(1).widget()
            tmp = self.setupVboxColumn1.takeAt(1)
            if tmp.widget():
                widget = tmp.widget()
                widget.setParent(None)
                del widget
            # tmp = self.setupVboxColumn2.takeAt(1).widget()
            tmp = self.setupVboxColumn2.takeAt(1)
            if tmp.widget():
                widget = tmp.widget()
                widget.setParent(None)
                del widget
                # tmp.setParent(None)
                # del tmp
            else:
                lay = tmp.layout()
                while lay.count() != 0:
                    tmp = lay.takeAt(0)
                    if tmp.widget():
                        widget = tmp.widget()
                        widget.setParent(None)
                        del widget
                    else:
                        tmp.widget().close()

        # # while layout_item.count() != 0:
        # #     if layout_item.takeAt(0).widget()
        # if layout_item:
        #     sub_item = layout_item.takeAt(0)
        #     if sub_item.layout():
        #         sub_layout = sub_item.layout()
        #         self.reset_ui(sub_layout)
        #         sub_layout.setParent(None)
        #         layout_item.removeItem(sub_layout)
        #         del sub_layout
        #     if sub_item.widget():
        #         sub_widget = sub_item.widget()
        #         sub_widget.setParent(None)
        #         layout_item.removeWidget(sub_widget)
        #         del sub_widget
        #     layout_item.removeItem(sub_item)
        #     del sub_item

    def change_ui(self, _):
        if self.relative_or_offset_button.isChecked():
            self.reset_ui()
            self.create_ui_relative()
            self.update_ui()
        else:
            self.reset_ui()
            self.create_ui_offset()
            self.update_ui()


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
                        # self.elements_dict_for_Label.append(QLabel('Element '+str(i)))
                        # self.elements_dict_for_LineEdit.append(QLineEdit(id))
                        #
                        # self.setupVboxColumn1.addWidget(self.elements_dict_for_Label[-1])
                        # self.setupVboxColumn2.addWidget(self.elements_dict_for_LineEdit[-1])


                # strList = ["_pyCode"]
                # self.addQLabel(strList)
                # self.addQLine(len(strList))

    def showClickedItem(self, clicked_item):
        if 'XY_source_ref' in self.__dict__:
            self.XY_source_ref.setCurrentRow(0)
        elif 'XY_target_ref' in self.__dict__:
            self.XY_target_ref.setCurrentRow(0)

        if clicked_item:
            print(clicked_item.text())

    def getArray(self, array_list_item):
        if self.variable_type == 'path_array':
            self.deleteItemList.clear()
            input_text = array_list_item.text()
            name_flag = False
            source = ''
            target = ''
            _from = 0
            _end = 0
            for idx in range(len(input_text)):
                if input_text[idx] == "'":
                    _end = idx
                    if name_flag:
                        tmp_text = input_text[_from:_end]
                        self.deleteItemList.addItem(tmp_text)
                        for jdx in range(len(self.group_list)):
                            if tmp_text == self.group_list[jdx][0]['_id']:
                                source = 'center(' + str(self.group_list[jdx][1][0]) + ')'
                                target = 'center(' + str(self.group_list[jdx][2][0]) + ')'
                    _from = idx+1
                    name_flag = not name_flag

            self.XY_source_ref.insertItem(0, source)
            self.XY_source_ref.setCurrentRow(0)
            self.XY_target_ref.insertItem(0, target)
            self.XY_target_ref.setCurrentRow(0)
            self.show()
        elif self.variable_type == 'boundary_array':
            self.deleteItemList.clear()
            input_text = array_list_item.text()
            name_flag = False
            source = ''
            _from = 0
            _end = 0
            for idx in range(len(input_text)):
                if input_text[idx] == "'":
                    _end = idx
                    if name_flag:
                        tmp_text = input_text[_from:_end]
                        self.deleteItemList.addItem(tmp_text)
                        for jdx in range(len(self.group_list)):
                            if tmp_text == self.group_list[jdx][0]['_id']:
                                source = 'center(' + str(self.group_list[jdx][1][0]) + ')'
                    _from = idx+1
                    name_flag = not name_flag

            self.XY_source_ref.insertItem(0, source)
            self.XY_source_ref.setCurrentRow(0)
            self.show()
        else:
            self.deleteItemList.clear()
            array_list = eval(array_list_item.text())
            self.deleteItemList.addItems(array_list)
            # self.variable_type = "element array"
            # self.reset_ui(self.layout())
            self.show()

    def getWidth(self, text):
        if text == 'Auto':
            self.width_input.setStyleSheet("QLineEdit{background:rgb(222,222,222);}")
            self.width_input.setReadOnly(True)
        elif text == 'Custom':
            self.width_input.setStyleSheet("QLineEdit{background:rgb(255,255,255);}")
            self.width_input.setReadOnly(False)

    def getLength(self, text):
        if text == 'Auto':
            self.length_input.setStyleSheet("QLineEdit{background:rgb(222,222,222);}")
            self.length_input.setReadOnly(True)
        elif text == 'Custom':
            self.length_input.setStyleSheet("QLineEdit{background:rgb(255,255,255);}")
            self.length_input.setReadOnly(False)

    def getIndex(self, text):
        if text == 'Custom':
            self.index_input.setStyleSheet("QLineEdit{background:rgb(255,255,255);}")
            self.index_input.setReadOnly(False)
        else:
            self.index_input.setStyleSheet("QLineEdit{background:rgb(222,222,222);}")
            self.index_input.setReadOnly(True)

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

    def update_output_dict(self, changed_text):
        sender = self.sender()
        key = sender.field_name
        if type(changed_text) == QListWidgetItem:
            changed_text = changed_text.text()
        self.output_dict[key] = changed_text

    def on_buttonBox_accepted(self):
        if self.variable_type == 'path_array':
            if self.XY_source_ref.item(0).text() == '' or self.XY_target_ref.item(0).text() == '':
                self.warning = QMessageBox()
                self.warning.setText("Incomplete")
                self.warning.setIcon(QMessageBox.Warning)
                self.warning.show()
                return

        for idx in range(self.deleteItemList.count()):
            _id = self.deleteItemList.item(idx).text()
            print(_id)
            self.send_DestroyTmpVisual_signal.emit(_id)

        print(self.deleteItemList)
        self.send_output_dict_signal.emit(self.output_dict)

        # variable_vis_item = VariableVisualItem.VariableVisualItem()
        # variable_vis_item.addToGroupFromList(self.vis_items)
        # variable_info = dict()

        # if self.variable_type == 'path_array':
        #     # dp_id = self.XY_source_ref.text()[self.XY_source_ref.text().find("'")+1:-3]
        #     # dc_id = self._QTObj._qtProject._ElementManager.dp_id_to_dc_id[dp_id]
        #     # print(self.XY_source_ref.text().replace(dp_id,dc_id))
        #     # print(self.XY_target_ref.text().replace(dp_id,dc_id))
        #     # print(self.XY_source_ref.text())
        #     # print(self.XY_target_ref.text())
        #     self.send_output_dict_signal.emit(self.output_dict)
        # else:
        #     self.XY_base_text = self.XY_base.text()
        #     self.x_offset_text = self.x_offset.text()
        #     self.y_offset_text = self.y_offset.text()
        #
        #     if ',' in self.XY_base_text:
        #         slicing = self.XY_base_text.find(',')
        #         self.XY_base_text = [[float(self.XY_base_text[:slicing]), float(self.XY_base_text[slicing + 1:])]]
        #
        #     try:
        #         self.x_offset_text = float(self.x_offset.text())
        #     except:
        #         pass
        #
        #     try:
        #         self.y_offset_text = float(self.y_offset.text())
        #     except:
        #         pass
        #
        #     self.ui_list_c.extend([self.XY_base_text, self.x_offset_text, self.y_offset_text])
        #
        #     for i, key in enumerate(self.ui_list_a):
        #         variable_info[key] = self.ui_list_c[i]
        #     if self.variable_type == 'element array':
        #         tmp_list = []
        #         for i in range(len(self.elements_dict_for_LineEdit)):
        #             tmp_list.append(self.elements_dict_for_LineEdit[i].text())
        #         variable_info['elements'] = tmp_list
        #     variable_vis_item._DesignParametertype= self.variable_type
        #     variable_vis_item.set_variable_info(variable_info)
        #     self.send_variableVisual_signal.emit(variable_vis_item)
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