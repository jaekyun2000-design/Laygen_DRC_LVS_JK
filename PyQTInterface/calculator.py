from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import platform

from PyCodes import variable_ast
import collections
import user_setup
import warnings
import re
import copy
# import numpy as np
import os
from generatorLib import drc_api
import user_setup

class ExpressionCalculator(QWidget):
    send_XYCreated_signal = pyqtSignal(str, dict)
    send_dummyconstraints_signal = pyqtSignal(dict, str)
    send_path_row_xy_signal = pyqtSignal("PyQt_PyObject", str)
    send_variable_ast = pyqtSignal("PyQt_PyObject")
    send_variable_wo_post_ast = pyqtSignal("PyQt_PyObject")
    send_expression_signal = pyqtSignal(str, str, dict)
    returnLayer_signal = pyqtSignal(list)
    presetDict = dict()

    def __init__(self,clipboard,purpose):
        # super(ExpressionCalculator, self).__init__()
        super().__init__()

        ######state_flag#######
        self.value_flag=False
        self.value_str = ''

        self.digit_flag=False
        self.waiting = False

        self.arithmetic_flag=False
        self.arithmetic_str = ''

        self.left_parenthesis_flag=False
        self.right_parenthesis_flag=False
        ########################

        self.clipboard = clipboard
        self.display= QTextEdit('')
        # self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight|Qt.AlignTop)
        self.display.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        # self.display.setMinimumHeight(80)
        # print(self.display.layoutDirection())
        # # self.display.setLayoutDirection(Qt.RightToLeft)
        # print(self.display.layoutDirection())
        self.parenthesis_count = 0
        self.purpose = purpose
        self.variable_purpose = False
        self.custom_index = ''
        self.equationList = list()
        self.DRCTreeItemDict = dict()
        self.hierarchy_list = list()
        self.returnedLayer = None

        # self.setFixedSize(786,800)
        self.setMinimumSize(790,800)

        font = self.display.font()
        font.setPointSize(font.pointSize()+6)
        self.display.setFont(font)
        self.init_ui()

    def init_ui(self):
        self.digit_buttons = []
        for i in range(10):
            self.digit_buttons.append(self.create_button(f'{i}', self.digit_clicked))
        self.digit_buttons.append(self.create_button('+/-', self.digit_clicked))
        self.digit_buttons.append(self.create_button('.', self.digit_clicked))
        self.top_buttons = self.create_button('━', self.geo_clicked ,'top')
        self.right_buttons = self.create_button('┃', self.geo_clicked, 'right')
        self.left_buttons = self.create_button('┃', self.geo_clicked, 'left')
        self.bottom_buttons = self.create_button('━', self.geo_clicked, 'bottom')
        self.center_buttons = self.create_button('*',self.geo_clicked, 'center')
        self.left_top_buttons = self.create_button('┏',self.geo_clicked, 'lt')
        self.right_top_buttons = self.create_button('┓',self.geo_clicked, 'rt')
        self.left_bot_buttons = self.create_button('┗',self.geo_clicked, 'lb')
        self.right_bot_buttons = self.create_button('┛',self.geo_clicked, 'rb')

        self.width_button = self.create_button('width',self.geo_clicked,'width')
        self.click_button = self.create_button('click',self.click_clicked,'click')
        self.height_button = self.create_button('height',self.geo_clicked,'height')

        self.plus = self.create_button(' + ',self.arithmetic_clicked)
        self.minus = self.create_button(' - ',self.arithmetic_clicked)
        self.mul = self.create_button(' * ',self.arithmetic_clicked)
        self.div = self.create_button(' / ',self.arithmetic_clicked)
        self.comma = self.create_button(' , ',self.arithmetic_clicked)
        self.left_parenthesis = self.create_button(' ( ',self.parenthesis_clicked)
        self.right_parenthesis = self.create_button(' ) ',self.parenthesis_clicked)

        self.backspace = self.create_button('<-',self.delete_clicked)

        """
        option layout
        """
        self.xy_reference_toggling_group = QGroupBox()
        toggling_group_layout = QHBoxLayout()
        option_box_layout = QHBoxLayout()
        option_box_button_content = QVBoxLayout()
        option_box_button_content_a = QHBoxLayout()
        option_box_button_content_b = QHBoxLayout()

        self.x_button = self.create_radio_button('X',self.xy_reference_clicked)
        self.y_button = self.create_radio_button('Y',self.xy_reference_clicked)
        self.xy_button = self.create_radio_button('XY',self.xy_reference_clicked)
        self.x_button.setChecked(True)
        if self.purpose not in ['init', 'XY_offset'] :
            self.xy_button.setDisabled(True)

        toggling_group_layout.addWidget(self.x_button)
        toggling_group_layout.addWidget(self.y_button)
        toggling_group_layout.addWidget(self.xy_button)
        self.xy_reference_toggling_group.setLayout(toggling_group_layout)

        add_button = self.create_button('ADD',self.add_clicked, size_constraint=dict(height=35))
        edit_button = self.create_button('EDIT',self.edit_clicked, size_constraint=dict(height=35))
        export_button = self.create_button('EXPORT',self.export_clicked, size_constraint=dict(height=35))
        export_path_button = self.create_button('EXPORT FOR PATH',self.export_path_clicked, size_constraint=dict(height=35))
        save_as_variable_button = self.create_button('SAVE VARIABLE',self.variable_save_clicked, size_constraint=dict(height=35))
        export_as_variable_button = self.create_button('EXPORT VARIABLE',self.export_variable_clicked, size_constraint=dict(height=35))
        view_variable_list = self.create_button('VIEW VARIABLE',self.variable_show_clicked, size_constraint=dict(height=35))
        if self.purpose != 'init':
            export_path_button.setDisabled(True)

        # option_hbox_content_a.addWidget(self.xy_reference_toggling_group)
        option_box_button_content_a.addWidget(add_button)
        option_box_button_content_a.addWidget(edit_button)
        option_box_button_content_a.addWidget(export_button)
        option_box_button_content_a.addWidget(export_path_button)
        option_box_button_content_a.setSizeConstraint(QLayout.SetMaximumSize & QLayout.SizeConstraint.SetFixedSize)

        option_box_button_content_b.addWidget(save_as_variable_button)
        option_box_button_content_b.addWidget(export_as_variable_button)
        option_box_button_content_b.addWidget(view_variable_list)
        option_box_button_content_b.setSizeConstraint(QLayout.SetMaximumSize & QLayout.SizeConstraint.SetFixedSize)

        option_box_button_content.addLayout(option_box_button_content_a)
        option_box_button_content.addLayout(option_box_button_content_b)

        option_box_layout.addWidget(self.xy_reference_toggling_group)
        option_box_layout.addLayout(option_box_button_content)

        """
        main layout
        """


        main_layout = QGridLayout()
        # main_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        dl_size = 5
        main_layout.addWidget(self.display, 0, 0, dl_size, 7)
        main_layout.addWidget(self.backspace, 0, 7, dl_size, 1)
        # main_layout.addWidget(self.display, 1, 8)

        for i in range(10):
            if i != 0:
                row = ((9-i) / 3)+dl_size
                col = ((i-1) % 3)+3
                main_layout.addWidget(self.digit_buttons[i], row, col)
            main_layout.addWidget(self.digit_buttons[10], dl_size+3, 3)
            main_layout.addWidget(self.digit_buttons[0], dl_size+3, 4)
            main_layout.addWidget(self.digit_buttons[11], dl_size+3, 5)
        main_layout.addWidget(self.top_buttons,dl_size,1)
        main_layout.addWidget(self.bottom_buttons,dl_size+2,1)
        main_layout.addWidget(self.left_buttons,dl_size+1,0)
        main_layout.addWidget(self.right_buttons,dl_size+1,2)
        main_layout.addWidget(self.center_buttons,dl_size+1,1)
        main_layout.addWidget(self.left_top_buttons,dl_size,0)
        main_layout.addWidget(self.right_top_buttons,dl_size,2)
        main_layout.addWidget(self.left_bot_buttons,dl_size+2,0)
        main_layout.addWidget(self.right_bot_buttons,dl_size+2,2)

        main_layout.addWidget(self.width_button,dl_size+3,0)
        main_layout.addWidget(self.click_button,dl_size+3,1)
        main_layout.addWidget(self.height_button,dl_size+3,2)

        main_layout.addWidget(self.left_parenthesis,dl_size,6)
        main_layout.addWidget(self.mul,dl_size+1,6)
        main_layout.addWidget(self.plus,dl_size+2,6)
        main_layout.addWidget(self.comma,dl_size+3,6)

        main_layout.addWidget(self.right_parenthesis,dl_size,7)
        main_layout.addWidget(self.div,dl_size+1,7)
        main_layout.addWidget(self.minus,dl_size+2,7)



        """
        set stretch
        """
        for r in range(main_layout.rowCount()):
            main_layout.setRowStretch(r,1)
        for c in range(main_layout.columnCount()):
            main_layout.setColumnStretch(c,1)

        top_layout = QVBoxLayout()
        # top_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        top_layout.addLayout(option_box_layout)
        top_layout.setStretchFactor(option_box_layout,0)
        top_layout.addLayout(main_layout)

        self.XWindow = QListWidget()
        if platform.system() != 'Darwin':
            self.XWindow.setStyleSheet("background-image: url(" + os.getcwd().replace("\\",'/') + "/Image/X.png); background-position: center; background-color: rgb(255,255,255); background-repeat: no-repeat; background-attachment: fixed;")
        self.XWindow.itemClicked.connect(self.XitemClicked)
        self.YWindow = QListWidget()
        if platform.system() != 'Darwin':
            self.YWindow.setStyleSheet("background-image: url(" + os.getcwd().replace("\\",'/') + "/Image/Y.png); background-position: center; background-color: rgb(255,255,255); background-repeat: no-repeat; background-attachment: fixed;")
        self.YWindow.itemClicked.connect(self.YitemClicked)
        self.XYWindow = QListWidget()
        if platform.system() != 'Darwin':
            self.XYWindow.setStyleSheet("background-image: url(" + os.getcwd().replace("\\",'/') + "/Image/XY.png); background-position: center; background-color: rgb(255,255,255); background-repeat: no-repeat; background-attachment: fixed;")
        self.XYWindow.itemClicked.connect(self.XYitemClicked)
        if self.purpose not in ['init', 'XY_offset']:
            self.XYWindow.setDisabled(True)
            if platform.system() != 'Darwin':
                self.XYWindow.setStyleSheet("background-image: url(" + os.getcwd().replace("\\",'/') + "/Image/XY_disabled.png); background-position: center; background-color: rgb(255,255,255); background-attachment: fixed;")

        self.first_index_button = QPushButton()
        self.first_index_button.setText('first')
        self.first_index_button.clicked.connect(self.manage_index)
        self.last_index_button = QPushButton()
        self.last_index_button.setText('last')
        self.last_index_button.clicked.connect(self.manage_index)
        self.custom_index_button = QPushButton()
        self.custom_index_button.setText('custom')
        self.custom_index_button.clicked.connect(self.manage_index)

        self.index_layout = QVBoxLayout()

        self.index_button_layout = QHBoxLayout()
        self.index_button_layout.addWidget(self.first_index_button)
        self.index_button_layout.addWidget(self.last_index_button)
        self.index_button_layout.addWidget(self.custom_index_button)

        self.index_input = QLineEdit()
        self.index_input.textChanged.connect(self.store_index_input)
        self.index_label = QLabel('index')

        self.index_input_layout = QHBoxLayout()
        self.index_input_layout.addWidget(self.index_input)
        self.index_input_layout.addWidget(self.index_label)

        self.index_layout.addLayout(self.index_button_layout)
        self.index_layout.addLayout(self.index_input_layout)
        self.index_layout.addSpacing(150)

        self.presetButton = QPushButton()
        self.presetButton.setText('▶')
        self.presetButton.setMaximumWidth(30)
        self.presetWindow = QListWidget()
        self.presetWindow.itemClicked.connect(self.presetClicked)
        self.presetWindow.setDragDropMode(QAbstractItemView.InternalMove)

        DRCText = QLabel('DRC List')
        DRCText.setAlignment(Qt.AlignCenter)
        self.DRCWindow = QTreeWidget()
        self.DRCWindow.setHeaderLabel('')
        self.get_drc_dict()

        # DRCButton = QPushButton("DRC")

        hline1 = QFrame()
        hline1.setFrameShape(QFrame.HLine)
        presetText = QLabel('Preset')
        presetText.setAlignment(Qt.AlignCenter)
        presetText.setMaximumWidth(37)
        hline2 = QFrame()
        hline2.setFrameShape(QFrame.HLine)

        vline = QFrame()
        vline.setFrameShape(QFrame.VLine)
        vline.setLineWidth(10)

        H_layout1 = QHBoxLayout()
        H_layout2 = QHBoxLayout()
        H_layout3 = QHBoxLayout()
        V_layout1 = QVBoxLayout()

        H_layout1.addWidget(self.YWindow)
        # H_layout1.addSpacing(282)
        H_layout1.addLayout(self.index_layout)
        # H_layout1.addSpacing(202)
        # H_layout1.addLayout(V_layout1)
        # V_layout1.addWidget(DRCButton)
        # V_layout1.addSpacing(100)
        H_layout2.addWidget(self.XYWindow)
        H_layout2.addWidget(self.XWindow)

        H_layout3.addWidget(self.presetButton)
        H_layout3.addWidget(hline1)
        H_layout3.addWidget(presetText)
        H_layout3.addWidget(hline2)

        V_layout1.addWidget(DRCText)
        V_layout1.addWidget(self.DRCWindow)

        top_layout.addLayout(H_layout1)
        top_layout.addLayout(H_layout2)
        top_layout.addLayout(H_layout3)
        top_layout.addWidget(self.presetWindow)

        self.DRCWindow.setFixedWidth(200)
        # self.DRCWindow.hide()
        self.presetWindow.setFixedHeight(200)
        self.presetWindow.hide()

        # DRCButton.clicked.connect(self.ExtendDRCWidget)
        self.presetButton.clicked.connect(self.ExtendPresetWidget)

        # self.setLayout(main_layout)
        top_DRC_layout = QHBoxLayout()
        top_DRC_layout.addLayout(top_layout)
        top_DRC_layout.addWidget(vline)
        top_DRC_layout.addLayout(V_layout1)

        self.setLayout(top_DRC_layout)
        self.setWindowTitle('Expression Calculator')
        # self.show()

    # def ExtendDRCWidget(self):
    #     if self.DRCWindow.isHidden():
    #         self.DRCWindow.show()
    #         self.setFixedWidth(786)
    #     else:
    #         self.DRCWindow.hide()
    #         self.setFixedWidth(580)

    def get_drc_dict(self):
        while True:
            if self.DRCWindow.itemAt(0,0) is None:
                break
            else:
                self.DRCWindow.takeTopLevelItem(0)

        self.drc_dict = drc_api.drc_classified_dict

        for layer in self.drc_dict.keys():
            top = QTreeWidgetItem([layer])
            self.DRCTreeItemDict[layer] = top
            for key in self.drc_dict[layer]:
                tmpItem = QTreeWidgetItem(top,[key])
            self.DRCWindow.addTopLevelItem(top)

        self.DRCWindow.itemClicked.connect(self.DRC_click)

    def ExtendPresetWidget(self):
        if self.presetWindow.isHidden():
            self.presetWindow.show()
            self.presetButton.setText('▼')
            self.setFixedHeight(1006)
        else:
            self.presetWindow.hide()
            self.presetButton.setText('▶')
            self.setFixedHeight(800)

    def DRC_click(self):
        display = str()
        _tmp_rule = str()
        _tmp_item_text = self.DRCWindow.currentItem().text(0)
        _tmp_parent_text = self.DRCWindow.currentItem().parent().text(0)

        if self.DRCWindow.currentItem().childCount() == 0:
            if type(self.drc_dict[_tmp_parent_text][_tmp_item_text]) == list:
                for item in self.drc_dict[_tmp_parent_text][_tmp_item_text]:
                    _tmp_rule = _tmp_rule + item + '=None,'

                _tmp_rule = '(' + _tmp_rule[:-1] + ')'
                if self.value_flag:
                    self.equationList[-1] = 'drc.' + self.DRCWindow.currentItem().text(0) + _tmp_rule
                else:
                    self.equationList.append('drc.' + self.DRCWindow.currentItem().text(0) + _tmp_rule)
            else:
                if self.value_flag:
                    self.equationList[-1] = 'drc.' + self.DRCWindow.currentItem().text(0)
                else:
                    self.equationList.append('drc.' + self.DRCWindow.currentItem().text(0))
            self.value_flag = True
            self.arithmetic_flag = False
            self.digit_flag = False
            self.left_parenthesis_flag = False
            self.right_parenthesis_flag = False

            for text in self.equationList:
                display += text
            self.display.setText(display)

    def variable_clicked(self, variable_name):

        if self.value_flag:
            self.equationList[-1] = variable_name
        else:
            self.equationList.append(variable_name)
        self.value_flag = True
        self.arithmetic_flag = False
        self.digit_flag = False
        self.left_parenthesis_flag = False
        self.right_parenthesis_flag = False

        display = ''.join(self.equationList)
        self.display.setText(display)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Delete:
            for itemX in self.XWindow.selectedItems():
                rowX = self.XWindow.row(itemX)
                self.XWindow.takeItem(rowX)
            for itemY in self.YWindow.selectedItems():
                rowY = self.YWindow.row(itemY)
                self.YWindow.takeItem(rowY)
            for itemXY in self.XYWindow.selectedItems():
                rowXY = self.XYWindow.row(itemXY)
                self.XYWindow.takeItem(rowXY)
        elif QKeyEvent.key() == Qt.Key_Backspace:
            self.delete_clicked()
        elif QKeyEvent.text() == 'q':
            self.geo_clicked(clicked=self.left_top_buttons)
        elif QKeyEvent.text() == 'w':
            self.geo_clicked(clicked=self.top_buttons)
        elif QKeyEvent.text() == 'e':
            self.geo_clicked(clicked=self.right_top_buttons)
        elif QKeyEvent.text() == 'a':
            self.geo_clicked(clicked=self.left_buttons)
        elif QKeyEvent.text() == 's':
            self.geo_clicked(clicked=self.center_buttons)
        elif QKeyEvent.text() == 'd':
            self.geo_clicked(clicked=self.right_buttons)
        elif QKeyEvent.text() == 'z':
            self.geo_clicked(clicked=self.left_bot_buttons)
        elif QKeyEvent.text() == 'x':
            self.geo_clicked(clicked=self.bottom_buttons)
        elif QKeyEvent.text() == 'c':
            self.geo_clicked(clicked=self.right_bot_buttons)
        elif QKeyEvent.text() == 'W':
            self.geo_clicked(clicked=self.width_button)
        elif QKeyEvent.text() == 'H':
            self.geo_clicked(clicked=self.height_button)
        elif QKeyEvent.text() == '1':
            self.digit_clicked(clicked=self.digit_buttons[1])
        elif QKeyEvent.text() == '2':
            self.digit_clicked(clicked=self.digit_buttons[2])
        elif QKeyEvent.text() == '3':
            self.digit_clicked(clicked=self.digit_buttons[3])
        elif QKeyEvent.text() == '4':
            self.digit_clicked(clicked=self.digit_buttons[4])
        elif QKeyEvent.text() == '5':
            self.digit_clicked(clicked=self.digit_buttons[5])
        elif QKeyEvent.text() == '6':
            self.digit_clicked(clicked=self.digit_buttons[6])
        elif QKeyEvent.text() == '7':
            self.digit_clicked(clicked=self.digit_buttons[7])
        elif QKeyEvent.text() == '8':
            self.digit_clicked(clicked=self.digit_buttons[8])
        elif QKeyEvent.text() == '9':
            self.digit_clicked(clicked=self.digit_buttons[9])
        elif QKeyEvent.text() == '0':
            self.digit_clicked(clicked=self.digit_buttons[0])
        elif QKeyEvent.text() == '+':
            self.arithmetic_clicked(clicked=self.plus)
        elif QKeyEvent.text() == '-':
            self.arithmetic_clicked(clicked=self.minus)
        elif QKeyEvent.text() == '*':
            self.arithmetic_clicked(clicked=self.mul)
        elif QKeyEvent.text() == '/':
            self.arithmetic_clicked(clicked=self.div)
        elif QKeyEvent.text() == '(':
            self.parenthesis_clicked(clicked=self.left_parenthesis)
        elif QKeyEvent.text() == ')':
            self.parenthesis_clicked(clicked=self.right_parenthesis)

    def getXY(self, XY_id):
        print(XY_id)
        self.show()
        self.presetWindow.clear()
        for _id in ExpressionCalculator.presetDict.keys():
            self.presetWindow.addItem(_id)
        if XY_id in ExpressionCalculator.presetDict:
            for i in range(self.presetWindow.count()):
                if self.presetWindow.item(i).text() == XY_id:
                    self.presetWindow.setCurrentRow(i)
            self.presetClicked()

    def set_preset_window(self):
        self.presetWindow.clear()
        for _id in ExpressionCalculator.presetDict.keys():
            self.presetWindow.addItem(_id)

    def XitemClicked(self):
        if self.YWindow.currentItem():
            self.YWindow.currentItem().setSelected(False)
        if self.XYWindow.currentItem():
            self.XYWindow.currentItem().setSelected(False)

    def YitemClicked(self):
        if self.XWindow.currentItem():
            self.XWindow.currentItem().setSelected(False)
        if self.XYWindow.currentItem():
            self.XYWindow.currentItem().setSelected(False)

    def XYitemClicked(self):
        if self.XWindow.currentItem():
            self.XWindow.currentItem().setSelected(False)
        if self.YWindow.currentItem():
            self.YWindow.currentItem().setSelected(False)


    def create_button(self,text, slot_fcn, name=None, size_constraint = None):
        button = QPushButton(text)
        button.clicked.connect(slot_fcn)
        button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        if name is not None:
            button.setObjectName(name)
        if size_constraint and type(size_constraint) == dict:
            if 'height' in size_constraint:
                button.setMaximumHeight(size_constraint['height'])
            # if 'width' in size_constraint:
            #     button.setMaximumWidth(size_constraint['width'])
        return button

    def click_clicked(self):
        self.hide()
        self.waiting = True

    def waitForClick(self, event):
        if self.waiting == True:
            display = str()
            calc_expression = str(event.scenePos().x())+','+str(event.scenePos().y())

            if self.value_flag:
                print(f'len!!={len(self.value_str)}')
                # self.equationList
                # self.display.setText(self.display.toPlainText()[:-len(self.value_str)] + calc_expression)
                self.equationList[-1] = calc_expression
            else:
                # self.display.setText(self.display.toPlainText() + calc_expression)
                self.equationList.append(calc_expression)

            for text in self.equationList:
                display += text
            self.display.setText(display)

            self.value_flag = True
            self.value_str = calc_expression
            self.arithmetic_flag = False
            self.digit_flag = False
            self.left_parenthesis_flag = False
            self.right_parenthesis_flag = False
            self.show()
            self.waiting = False

    def create_radio_button(self, text, slot_fcn, name=None):
        button = QRadioButton(text)
        button.clicked.connect(slot_fcn)
        if name is not None:
            button.setObjectName(name)
        return button

    def arithmetic_clicked(self,  clicked= None):
        if clicked:
            clicked_button = clicked
        else:
            clicked_button = self.sender()
        arith_sign = clicked_button.text()
        display = str()

        if self.value_flag or self.right_parenthesis_flag:
            if self.equationList[-1][-1] == '.':
                self.equationList[-1] = self.equationList[-1][:-1]
            self.equationList.append(arith_sign)
            self.arithmetic_flag = True
        elif self.arithmetic_flag:
            self.equationList[-1] = arith_sign
        else:
            return
        self.value_flag = False
        self.digit_flag = False
        self.left_parenthesis_flag = False
        self.right_parenthesis_flag = False

        for text in self.equationList:
            display += text
        self.display.setText(display)
        # clicked_button = self.sender()
        # arith_sign = clicked_button.text()
        #
        # if self.value_flag:
        #     self.display.setText(self.display.text() + arith_sign)
        #     self.equationList.append(arith_sign)
        #     self.arithmetic_flag = True
        # elif self.arithmetic_flag:
        #     self.display.setText(self.display.text()[:-1] + arith_sign)
        #     self.equationList[-1] = arith_sign
        # else:
        #     return
        # self.value_flag = False
        # self.digit_flag = False

    def delete_clicked(self):
        if len(self.equationList) != 0:
            display = str()

            isDigit = False
            for num in range(10):
                if self.equationList[-1][0] == str(num):
                    isDigit = True

            if isDigit or self.equationList[-1][-1] == '.':
                if len(self.equationList[-1]) == 1:
                    del self.equationList[-1]
                    self.value_flag = False
                    self.digit_flag = False
                    self.arithmetic_flag = True
                    self.left_parenthesis_flag = False
                    self.right_parenthesis_flag = False
                elif self.equationList[-1] == '0.':
                    del self.equationList[-1]
                    self.value_flag = False
                    self.digit_flag = False
                    self.arithmetic_flag = True
                    self.left_parenthesis_flag = False
                    self.right_parenthesis_flag = False
                else:
                    last = self.equationList[-1][:-1]
                    self.equationList[-1] = last
                    self.value_flag = True
                    self.digit_flag = True
                    self.arithmetic_flag = False
                    self.left_parenthesis_flag = False
                    self.right_parenthesis_flag = False
            elif self.equationList[-1][0:2] == '(-':
                if len(self.equationList[-1]) == 4:
                    del self.equationList[-1]
                    self.value_flag = False
                    self.digit_flag = False
                    self.arithmetic_flag = True
                    self.left_parenthesis_flag = False
                    self.right_parenthesis_flag = False
                else:
                    last = self.equationList[-1][:-2] + self.equationList[-1][-1]
                    self.equationList[-1] = last
                    self.value_flag = True
                    self.digit_flag = True
                    self.arithmetic_flag = False
                    self.left_parenthesis_flag = False
                    self.right_parenthesis_flag = False
            else:
                if self.equationList[-1] == '+' or self.equationList[-1] == '-' or self.equationList[-1] == '*' or self.equationList[-1] == '/':
                    del self.equationList[-1]
                    for num in range(10):
                        if self.equationList[-1][-1] == str(num):
                            isDigit = True
                    if isDigit or self.equationList[-1][0:2] == '(-':
                        self.value_flag = True
                        self.digit_flag = True
                        self.arithmetic_flag = False
                        self.left_parenthesis_flag = False
                        self.right_parenthesis_flag = False
                    else:
                        self.value_flag = True
                        self.digit_flag = False
                        self.arithmetic_flag = False
                        self.left_parenthesis_flag = False
                        self.right_parenthesis_flag = False
                elif self.equationList[-1] == '(':
                    del self.equationList[-1]
                    self.value_flag = False
                    self.digit_flag = False
                    self.arithmetic_flag = True
                    self.left_parenthesis_flag = False
                    self.right_parenthesis_flag = False
                elif self.equationList[-1] == ')':
                    del self.equationList[-1]
                    self.value_flag = True
                    self.digit_flag = True
                    self.arithmetic_flag = False
                    self.left_parenthesis_flag = False
                    self.right_parenthesis_flag = False
                else:
                    del self.equationList[-1]
                    self.value_flag = True
                    self.digit_flag = True
                    self.arithmetic_flag = False
                    self.left_parenthesis_flag = False
                    self.right_parenthesis_flag = False

            if len(self.equationList) == 0:
                self.value_flag = False
                self.digit_flag = False
                self.arithmetic_flag = False
                self.left_parenthesis_flag = False
                self.right_parenthesis_flag = False

            for text in self.equationList:
                display += text
            self.display.setText(display)

    def showXWindow(self):
        self.XWindow.addItem(self.display.toPlainText())
        self.display.clear()

    def showYWindow(self):
        self.YWindow.addItem(self.display.toPlainText())
        self.display.clear()

    def showXYWindow(self):
        self.XYWindow.addItem(self.display.toPlainText())
        self.display.clear()

    def parenthesis_clicked(self, clicked= None):
        if clicked:
            clicked_button = clicked
        else:
            clicked_button = self.sender()
        display = str()

        if clicked_button.text() == ' ( ':
            if not self.value_flag:
                self.parenthesis_count += 1
                self.equationList.append(' ( ')
                self.left_parenthesis_flag = True
                self.right_parenthesis_flag = False
                self.value_flag = False
                self.digit_flag = False
                self.arithmetic_flag = False

        elif clicked_button.text() == ' ) ':
            if self.value_flag or self.right_parenthesis_flag:
                if self.parenthesis_count > 0:
                    self.parenthesis_count -= 1
                    self.equationList.append(' ) ')
                    self.right_parenthesis_flag = True
                    self.left_parenthesis_flag = False
                    self.value_flag = False
                    self.digit_flag = False
                    self.arithmetic_flag = False

        for text in self.equationList:
            display += text
        self.display.setText(display)

    def digit_clicked(self,  clicked= None):
        if clicked:
            clicked_button = clicked
        else:
            clicked_button = self.sender()
        display = str()
        if clicked_button.text() == '+/-':
            if len(self.equationList) == 0:
                pass
            elif len(self.equationList) == 1:
                if self.equationList[-1][0] == ' - ':
                    self.equationList[-1] = self.equationList[-1][1:]
                else:
                    self.equationList[-1] = ' - ' + self.equationList[-1]
            else:
                if self.value_flag:
                    if self.equationList[-2] == ' + ':
                        self.equationList[-2] = ' - '
                    elif self.equationList[-2] == ' - ':
                        self.equationList[-2] = ' + '
                    elif self.equationList[-2] == ' * ' or self.equationList[-2] == ' / ':
                        if self.equationList[-1][0:2] == '(-':
                            self.equationList[-1] = self.equationList[-1][2:-1]
                        else:
                            self.equationList[-1] = '(-' + self.equationList[-1] + ')'
        else:
            digit_value = str(clicked_button.text())

            if self.digit_flag:
                if digit_value == '.':
                    if '.' in self.equationList[-1]:
                        pass
                    else:
                        if self.equationList[-1][0:2] == '(-':
                            self.equationList[-1] = self.equationList[-1][:-1] + digit_value + self.equationList[-1][-1]
                        else:
                            self.equationList[-1] = self.equationList[-1] + digit_value
                else:
                    if self.equationList[-1] == '0':
                        self.equationList[-1] = digit_value
                    else:
                        if self.equationList[-1][0:2] == '(-':
                            self.equationList[-1] = self.equationList[-1][:-1] + digit_value + self.equationList[-1][-1]
                        else:
                            self.equationList[-1] = self.equationList[-1] + digit_value

                self.value_flag = True
                self.digit_flag = True
                self.arithmetic_flag = False
                self.left_parenthesis_flag = False
                self.right_parenthesis_flag = False
            else:
                if self.value_flag:
                    self.equationList[-1] = digit_value

                    self.value_flag = True
                    self.digit_flag = True
                    self.arithmetic_flag = False
                    self.left_parenthesis_flag = False
                    self.right_parenthesis_flag = False
                else:
                    if digit_value == '.':
                        self.equationList.append('0.')
                    else:
                        self.equationList.append(digit_value)

                    self.value_flag = True
                    self.digit_flag = True
                    self.arithmetic_flag = False
                    self.left_parenthesis_flag = False
                    self.right_parenthesis_flag = False

        for text in self.equationList:
            display += text
        self.display.setText(display)


    def geo_clicked(self, clicked= None):
        if clicked:
            clicked_button = clicked
        else:
            clicked_button = self.sender()
        geo_text = clicked_button.objectName()
        hierarchy_list = self.parsing_clipboard()
        display = str()

        if type(hierarchy_list) == Exception:
            return None

        self.geo_text = geo_text
        self.hierarchy_list = hierarchy_list

        calc_expression = geo_text + f'({hierarchy_list})'.replace(" ","").replace("([", "(").replace("])", ")")
        if self.value_flag:
            print(f'len!!={len(self.value_str)}')
            self.equationList[-1] = calc_expression
        else:
            self.equationList.append(calc_expression)
        self.value_flag = True
        self.arithmetic_flag = False
        self.digit_flag = False
        self.left_parenthesis_flag = False
        self.right_parenthesis_flag = False

        for text in self.equationList:
            display += text
        self.display.setText(display)

        self.returnLayer_signal.emit(hierarchy_list)
        # Returned Layer Info conveyed @ this point

        print(self.returnedLayer)

        for idx in range(self.DRCWindow.topLevelItemCount()):
            self.DRCWindow.takeTopLevelItem(0)

        if self.returnedLayer in self.DRCTreeItemDict:
            self.DRCWindow.addTopLevelItem(self.DRCTreeItemDict[self.returnedLayer])
        for layer in self.DRCTreeItemDict.keys():
            if layer != self.returnedLayer:
                self.DRCWindow.addTopLevelItem(self.DRCTreeItemDict[layer])


    def xy_reference_clicked(self):
        pass


    def add_clicked(self):
        while self.parenthesis_count != 0:
            self.display.setText(self.display.toPlainText() + ' ) ')
            self.parenthesis_count -= 1

        if len(self.equationList) != 0:
            if self.arithmetic_flag:
                self.warning = QMessageBox()
                self.warning.setIcon(QMessageBox.Warning)
                self.warning.setText("Incomplete Equation")
                self.warning.show()
            else:
                if self.equationList[-1][-1] == '.':
                    self.display.setText(self.display.toPlainText()[:-1])
                # self.equationList.clear()
                self.value_flag = False
                self.digit_flag = False
                self.arithmetic_flag = False
                self.left_parenthesis_flag = False
                self.right_parenthesis_flag = False

                if self.x_button.isChecked():
                    self.showXWindow()
                    # XYFlag = 'X'
                elif self.y_button.isChecked():
                    self.showYWindow()
                    # XYFlag = 'Y'
                elif self.xy_button.isChecked():
                    # XYFlag = 'XY'
                    self.showXYWindow()
                self.equationList.clear()

        else:
            if self.display.toPlainText() == "" or self.display.toPlainText() == "Nothing In Here":
                self.display.setText("Nothing In Here")
            else:
                if self.x_button.isChecked():
                    self.showXWindow()
                elif self.y_button.isChecked():
                    self.showYWindow()
                elif self.xy_button.isChecked():
                    self.showXYWindow()

    def edit_clicked(self):
        if self.presetWindow.currentItem():
            _id = self.presetWindow.currentItem().text()
            XList = list()
            YList = list()
            XYList = list()
            for i_x in range(self.XWindow.count()):
                self.XWindow.setCurrentRow(i_x)
                XList.append(self.XWindow.currentItem().text())
            for i_y in range(self.YWindow.count()):
                self.YWindow.setCurrentRow(i_y)
                YList.append(self.YWindow.currentItem().text())
            for i_xy in range(self.XYWindow.count()):
                self.XYWindow.setCurrentRow(i_xy)
                XYList.append(self.XYWindow.currentItem().text())
            ExpressionCalculator.presetDict[_id]['X'] = XList
            ExpressionCalculator.presetDict[_id]['Y'] = YList
            ExpressionCalculator.presetDict[_id]['XY'] = XYList

    def export_clicked(self, export_type = False, var_name=None):
        XList = list()
        YList = list()
        XYList = list()
        LEFlag = False

        """
        Export For Path, 또는 Export 를 누르면 Add 되어 있는 모든 요소들을 가져온다.
        """
        for i_x in range(self.XWindow.count()):
            self.XWindow.setCurrentRow(i_x)
            XList.append(self.XWindow.currentItem().text())
        for i_y in range(self.YWindow.count()):
            self.YWindow.setCurrentRow(i_y)
            YList.append(self.YWindow.currentItem().text())
        for i_xy in range(self.XYWindow.count()):
            self.XYWindow.setCurrentRow(i_xy)
            XYList.append(self.XYWindow.currentItem().text())
        output = {'X':XList, 'Y':YList, 'XY':XYList}

        if export_type in [False, "PathXY_row"] and 'vw' in self.__dict__:
            output['variables'], output['variables_id'] = self.vw.export_variables()

        """
        Export를 클릭해서 넘어온 경우에는 단일 좌표 생성 혹은 Logic Expression 생성이다.
        Export For Path를 클릭해서 넘어온 경우에는 좌표를 append할 것이다.
        """

        """
        1. LogicExpression 의 경우 XY 둘중 하나만 결과로 나올 경우이다.
        """
        if not XYList and export_type == False:
            if XList and YList:
                """
                이 경우에는 X값과 Y값이 각각 있으니 XYCoordinate 생성하러 떠난다.
                """
                pass
            else:
                tmp_ast = variable_ast.LogicExpression()
                tmp_ast.info_dict = output
                if self.purpose == 'init':
                    self.send_variable_ast.emit(tmp_ast)
                else:
                    self.send_variable_wo_post_ast.emit(tmp_ast)
                LEFlag = True

        self.XWindow.clear()
        self.YWindow.clear()
        self.XYWindow.clear()
        """
        아래에서 XYCoordinate constraint 생성하거나, 이미 LogicExpression이 만들어진 상태이면 무시,
        그리고 export_type이 PathXY_row인 경우 main으로 output 보내준다.
        """
        if self.purpose == 'init':
            if export_type == 'PathXY_row':
                if self.pw.XYCoordinateList.rowCount() == 0:
                    if not XYList:
                        if not (XList and YList):
                            self.warning = QMessageBox()
                            self.warning.setIcon(QMessageBox.Warning)
                            self.warning.setText("First element for PathXY_row should be XYCoordinates")
                            self.warning.show()
                            self.pw.destroy()
                            del self.pw
                            return
                # self.send_XYCreated_signal.emit(export_type, output)
                tmp_ast = variable_ast.XYCoordinate()
                tmp_ast.info_dict = output
                self.send_variable_wo_post_ast.emit(tmp_ast)
            elif export_type == 'variable':
                self.variable_purpose = True
                tmp_ast = variable_ast.CustomVariable()
                tmp_ast.name = var_name
                tmp_ast.info_dict = output
                self.send_variable_wo_post_ast.emit(tmp_ast)
            elif export_type == 'variable_post':
                tmp_ast = variable_ast.CustomVariable()
                tmp_ast.name = var_name
                tmp_ast.info_dict = output
                self.send_variable_ast.emit(tmp_ast)
            else:
                if LEFlag == False:
                    # self.send_XYCreated_signal.emit('XYCoordinate', output)
                    tmp_ast = variable_ast.XYCoordinate()
                    tmp_ast.info_dict = output
                    self.send_variable_ast.emit(tmp_ast)

        else:
            if LEFlag == True:
                pass
            else:
                tmp_ast = variable_ast.XYCoordinate()
                tmp_ast.info_dict = output
                self.send_variable_wo_post_ast.emit(tmp_ast)
            # self.send_expression_signal.emit(self.display.toPlainText(), self.purpose, output)

        # self.send_variable_ast.emit()

    def export_path_clicked(self):
        if 'pw' not in self.__dict__:
            self.pw = PathWindow(address=self)
            self.pw.show()
            self.send_path_row_xy_signal.connect(self.pw.create_row)

        self.export_clicked('PathXY_row')

    def variable_save_clicked(self):
        if 'vw' not in self.__dict__:
            # self.vw = CVariableWindow()
            # self.vw.request_ast_signal.connect(lambda name: self.export_clicked('variable', name))
            # self.vw.send_selected_variable_ast_signal.connect(self.presetClicked)
            # self.vw.show()
            self.initialize_variable_window()
        else:
            self.vw.show()
        self.name_input_widget = QWidget()
        input_widget = QLineEdit()
        form_layout = QFormLayout()
        form_layout.addRow('variable name', input_widget)
        ok_button = QPushButton()
        ok_button.setText('OK')
        ok_button.clicked.connect(lambda tmp: self.vw.create_variable(input_widget.text()))
        ok_button.clicked.connect(self.name_input_widget.close)
        form_layout.addRow(' ', ok_button)
        self.name_input_widget.setLayout(form_layout)
        self.name_input_widget.show()

    def export_variable_clicked(self):
        self.name_input_widget = QWidget()
        input_widget = QLineEdit()
        form_layout = QFormLayout()
        form_layout.addRow('variable name', input_widget)
        ok_button = QPushButton()
        ok_button.setText('OK')
        ok_button.clicked.connect(lambda tmp: self.export_clicked('variable_post', input_widget.text()))
        ok_button.clicked.connect(self.name_input_widget.close)
        form_layout.addRow(' ', ok_button)
        self.name_input_widget.setLayout(form_layout)
        self.name_input_widget.show()

    def variable_show_clicked(self):
        if 'vw' not in self.__dict__:
            # self.vw = CVariableWindow()
            # self.vw.send_selected_variable_ast_signal.connect(self.presetClicked)
            # self.vw.load_variables(dict())
            # self.vw.show()
            self.initialize_variable_window()
        else:
            self.vw.show()
        self.vw.raise_()

    def initialize_variable_window(self):
        self.vw = CVariableWindow()
        self.vw.send_selected_variable_ast_signal.connect(self.presetClicked)
        self.vw.send_selected_variable_name_signal.connect(self.variable_clicked)
        self.vw.request_ast_signal.connect(lambda name: self.export_clicked('variable', name))
        # self.vw.load_variables(dict())
        self.vw.show()


    def getPathInfo(self, idDict):
        self.send_XYCreated_signal.emit('PathXY', idDict)
        path_ast = variable_ast.PathXY()
        path_ast.info_dict = idDict
        self.send_variable_ast.emit(path_ast)
        del self.pw

    def parsing_clipboard(self):
        try:
            print(self.clipboard.text())
            hierarchy_name_list = eval(self.clipboard.text())
            return hierarchy_name_list
        except:
            return self.abort_clipboard()

    def abort_clipboard(self):
        warnings.warn("You should select target layer first!")
        #debug option#
        if self.clipboard.text():
            print(self.clipboard.text())
        return Exception("No selected layer")

    def storePreset(self, dict, _id):
        ExpressionCalculator.presetDict[_id] = dict
        self.presetWindow.addItem(_id)

    def presetClicked(self, dummy=None):
        if type(dummy) == str:
            _id = dummy
        else:
            _id = self.presetWindow.currentItem().text()

        # if 'XYidlist' in ExpressionCalculator.presetDict[_id]:
        #     self.pw = PathWindow(address=self, idlist=ExpressionCalculator.presetDict[_id]['XYidlist'])
        #     self.send_path_row_xy_signal.connect(self.pw.create_row)
        if 'XY' not in ExpressionCalculator.presetDict[_id]:
            # id_list = []
            # for id_name, xy_ast in ExpressionCalculator.presetDict[_id].items():
            #     id_list.append([id_name, 0, 0])
            #     info_dict = xy_ast.info_dict
            #     if info_dict['X'] or info_dict['XY']:
            #         id_list[-1][1] = 2
            #     if info_dict['Y'] or info_dict['XY']:
            #         id_list[-1][2] = 2
            ast_and_id_list = ExpressionCalculator.presetDict[_id]
            self.pw = PathWindow(address=self, idlist=ast_and_id_list)
            self.send_path_row_xy_signal.connect(self.pw.create_row)
        else:
            if 'X' in ExpressionCalculator.presetDict[_id]:
                XList = ExpressionCalculator.presetDict[_id]['X']
            else:
                XList = []
            if 'Y' in ExpressionCalculator.presetDict[_id]:
                YList = ExpressionCalculator.presetDict[_id]['Y']
            else:
                YList = []
            if 'XY' in ExpressionCalculator.presetDict[_id]:
                XYList = ExpressionCalculator.presetDict[_id]['XY']
            else:
                XYList = []

            if 'variables' in ExpressionCalculator.presetDict[_id]:
                if 'vw' in self.__dict__:
                    self.vw.clear()
                    self.vw.load_variables(ExpressionCalculator.presetDict[_id])
                else:
                    self.initialize_variable_window()
                    self.vw.hide()
                    self.vw.load_variables(ExpressionCalculator.presetDict[_id])


            self.XWindow.clear()
            self.YWindow.clear()
            self.XYWindow.clear()

            for x in XList:
                self.XWindow.addItem(x)
            for y in YList:
                self.YWindow.addItem(y)
            for xy in XYList:
                self.XYWindow.addItem(xy)

    def manage_index(self,_):
        sender = self.sender()
        display = str()

        if sender.text() == 'first':
            self.index_input.setText('0')
            self.index_input.setReadOnly(True)
            index = 0
        elif sender.text() == 'last':
            self.index_input.setText('-1')
            self.index_input.setReadOnly(True)
            index = -1
        elif sender.text() == 'custom':
            self.index_input.setText(self.custom_index)
            self.index_input.setReadOnly(False)
            index = self.custom_index

        if self.hierarchy_list != []:
            # self.hierarchy_list[-1] = self.hierarchy_list[-1][:self.hierarchy_list[-1].find('[')+1] + str(index) + self.hierarchy_list[-1][self.hierarchy_list[-1].find(']'):]
            index_iter_list = re.finditer('\[[a-zA-Z0-9:_\-\+\*\/]*\]', self.hierarchy_list[-1])
            for last_index in index_iter_list:
                pass
            self.hierarchy_list[-1] = self.hierarchy_list[-1][:last_index.span()[0]+1]+str(index)+self.hierarchy_list[-1][last_index.span()[1]-1:]
            # self.hierarchy_list[-1] = re.sub('\[.*\]','['+str(index)+']',self.hierarchy_list[-1])

            calc_expression = self.geo_text + f'({self.hierarchy_list})'.replace(" ", "").replace("([", "(").replace("])", ")")
            if self.value_flag:
                print(f'len!!={len(self.value_str)}')
                self.equationList[-1] = calc_expression
            else:
                self.equationList.append(calc_expression)
            self.value_flag = True
            self.arithmetic_flag = False
            self.digit_flag = False
            self.left_parenthesis_flag = False
            self.right_parenthesis_flag = False

            for text in self.equationList:
                display += text
            self.display.setText(display)

    def store_index_input(self, changed_text):
        if changed_text != 'first' and changed_text != 'last':
            self.custom_index = changed_text

    def receive_constraint_result(self, qt_dc):
        '''
        When calculator requests to create design constraint, but not to post case...
        It means, to create path_row_xy coordinates.
        '''
        if self.variable_purpose:
            self.variable_purpose = False
            self.vw.load_ast(qt_dc._ast)
        elif self.purpose == 'init':
            self.pw.create_row(qt_dc._ast, qt_dc._id)
        elif self.purpose in ['height', 'width']:
            pass

class PathWindow(QWidget):
    send_output_signal = pyqtSignal(dict)
    send_clicked_item_name_signal = pyqtSignal(str)
    id_ast_match_dict = dict()

    def __init__(self, address=None, idlist=None):
        super().__init__()
        self.address = address
        self.initUI()
        if idlist:
            self.idlist = idlist
            self.updateUI()

    def initUI(self):
        exportButton = QPushButton("Export", self)
        cancelButton = QPushButton("Cancel", self)

        exportButton.clicked.connect(self.exportButton_accepted)
        cancelButton.clicked.connect(self.cancelButton_accepted)

        self.XYCoordinateList = QTableWidget()
        self.XYCoordinateList.setColumnCount(3)
        self.XYCoordinateList.setHorizontalHeaderLabels(['ID', 'X', 'Y'])
        self.XYCoordinateList.verticalHeader().setVisible(False)
        self.XYCoordinateList.setColumnWidth(0,408)
        self.XYCoordinateList.setColumnWidth(1,30)
        self.XYCoordinateList.setColumnWidth(2,30)
        self.XYCoordinateList.itemClicked.connect(self.itemLoad)
        self.send_clicked_item_name_signal.connect(self.address.presetClicked)
        # self.XYCoordinateList

        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(exportButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addWidget(self.XYCoordinateList)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setWindowTitle('Path Setup Window')
        self.setGeometry(300, 300, 500, 500)
        self.show()

    def updateUI(self):
        # for i in range(len(self.idlist)):
        #     if self.idlist[i][1] == 0 and self.idlist[i][2] == 0:
        #         tmpDict = {'X':[], 'Y':[], 'XY':[]}
        #     elif self.idlist[i][1] == 2 and self.idlist[i][2] == 0:
        #         tmpDict = {'X':[1], 'Y':[], 'XY':[]}
        #     elif self.idlist[i][1] == 0 and self.idlist[i][2] == 2:
        #         tmpDict = {'X':[], 'Y':[1], 'XY':[]}
        #     elif self.idlist[i][1] == 2 and self.idlist[i][2] == 2:
        #         tmpDict = {'X':[], 'Y':[], 'XY':[1]}
        #     self.create_row(tmpDict,self.idlist[i][0])
        for _id, _ast in self.idlist.items():
            self.create_row(_ast,_id)

    def itemLoad(self, _clickedItem):
        self.send_clicked_item_name_signal.emit(_clickedItem.text())

    def create_row(self, _ast, _id):
        constraint_dict = _ast.info_dict
        row = self.XYCoordinateList.rowCount()
        self.XYCoordinateList.setRowCount(row+1)
        IDtext = QTableWidgetItem(_id)
        IDtext.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled)
        self.XYCoordinateList.setItem(row,0,IDtext)
        Xcheck = QTableWidgetItem(_id)
        Xcheck.setText('')
        Xcheck.setFlags(Qt.ItemIsSelectable)
        self.XYCoordinateList.setItem(row,1,Xcheck)
        Ycheck = QTableWidgetItem(_id)
        Ycheck.setText('')
        Ycheck.setFlags(Qt.ItemIsSelectable)
        self.XYCoordinateList.setItem(row,2,Ycheck)
        if len(constraint_dict['XY']) == 0:
            if len(constraint_dict['X']) != 0 and len(constraint_dict['Y']) != 0:
                Xcheck.setCheckState(2)
                Ycheck.setCheckState(2)
            elif len(constraint_dict['X']) != 0 and len(constraint_dict['Y']) == 0:
                Xcheck.setCheckState(2)
                Ycheck.setCheckState(0)
            elif len(constraint_dict['X']) == 0 and len(constraint_dict['Y']) != 0:
                Xcheck.setCheckState(0)
                Ycheck.setCheckState(2)
            else:
                Xcheck.setCheckState(0)
                Ycheck.setCheckState(0)
        else:
            Xcheck.setCheckState(2)
            Ycheck.setCheckState(2)

        self.id_ast_match_dict[_id] = _ast

        # CurrentEditPointNum = len(self.XYdictForLineEdit) - 2
        # self.XYdictForLineEdit[CurrentEditPointNum].setText(_id)
        # self.UpdateXYwidget()

    def exportButton_accepted(self):
        # self.send_output_signal.connect(self.address.getPathInfo)
        output_dict = dict()
        for idx in range(self.XYCoordinateList.rowCount()):
            for id, ast in self.id_ast_match_dict.items():
                if self.XYCoordinateList.item(idx, 0).text() == id:
                    output_dict[self.XYCoordinateList.item(idx, 0).text()] = ast

        # self.send_output_signal.emit(output_dict)
        self.address.getPathInfo(output_dict)
        self.destroy()

    def cancelButton_accepted(self):
        del self.address.pw
        self.destroy()

    def closeEvent(self, QCloseEvent):
        del self.address.pw


class nine_key_calculator(QWidget):
    send_expression_signal = pyqtSignal(str, str, dict)
    send_geometry_info_text = pyqtSignal(str)

    send_variable_wo_post_ast = pyqtSignal("PyQt_PyObject")

    def __init__(self,clipboard,purpose,address):
        # super(ExpressionCalculator, self).__init__()
        super().__init__()

        ######state_flag#######
        self.value_flag=False
        self.value_str = ''
        ########################

        self.clipboard = clipboard
        self.purpose = purpose
        self.address = address
        self.display= QTextEdit('')
        # self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight|Qt.AlignTop)
        self.display.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.display.setFixedHeight(50)
        # self.display.setMinimumHeight(80)
        # print(self.display.layoutDirection())
        # # self.display.setLayoutDirection(Qt.RightToLeft)
        # print(self.display.layoutDirection())
        self.equationList = list()

        font = self.display.font()
        font.setPointSize(font.pointSize()+8)
        self.display.setFont(font)
        self.init_ui()

    def init_ui(self):
        self.top_buttons = self.create_button('━', self.geo_clicked ,'top')
        self.right_buttons = self.create_button('┃', self.geo_clicked, 'right')
        self.left_buttons = self.create_button('┃', self.geo_clicked, 'left')
        self.bottom_buttons = self.create_button('━', self.geo_clicked, 'bottom')
        self.center_buttons = self.create_button('*',self.geo_clicked, 'center')
        self.left_top_buttons = self.create_button('┏',self.geo_clicked, 'lt')
        self.right_top_buttons = self.create_button('┓',self.geo_clicked, 'rt')
        self.left_bot_buttons = self.create_button('┗',self.geo_clicked, 'lb')
        self.right_bot_buttons = self.create_button('┛',self.geo_clicked, 'rb')


        self.backspace = self.create_button('<-',self.delete_clicked)

        """
        option layout
        """
        export_button = self.create_button('EXPORT',self.export_clicked)

        """
        main layout
        """
        main_layout = QGridLayout()

        dl_size = 1
        main_layout.addWidget(self.display, 0, 0, dl_size, 3)
        main_layout.addWidget(self.backspace, 0, 3, dl_size, 1)

        main_layout.addWidget(self.top_buttons,dl_size,1)
        main_layout.addWidget(self.bottom_buttons,dl_size+2,1)
        main_layout.addWidget(self.left_buttons,dl_size+1,0)
        main_layout.addWidget(self.right_buttons,dl_size+1,2)
        main_layout.addWidget(self.center_buttons,dl_size+1,1)
        main_layout.addWidget(self.left_top_buttons,dl_size,0)
        main_layout.addWidget(self.right_top_buttons,dl_size,2)
        main_layout.addWidget(self.left_bot_buttons,dl_size+2,0)
        main_layout.addWidget(self.right_bot_buttons,dl_size+2,2)

        main_layout.addWidget(export_button, dl_size, 3, 3, 1)

        self.setLayout(main_layout)
        self.setWindowTitle(f'Nine-key Calculator for {self.purpose}')
        self.show()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Backspace:
            self.delete_clicked()
        elif QKeyEvent.text() == 'q':
            self.geo_clicked(clicked=self.left_top_buttons)
        elif QKeyEvent.text() == 'w':
            self.geo_clicked(clicked=self.top_buttons)
        elif QKeyEvent.text() == 'e':
            self.geo_clicked(clicked=self.right_top_buttons)
        elif QKeyEvent.text() == 'a':
            self.geo_clicked(clicked=self.left_buttons)
        elif QKeyEvent.text() == 's':
            self.geo_clicked(clicked=self.center_buttons)
        elif QKeyEvent.text() == 'd':
            self.geo_clicked(clicked=self.right_buttons)
        elif QKeyEvent.text() == 'z':
            self.geo_clicked(clicked=self.left_bot_buttons)
        elif QKeyEvent.text() == 'x':
            self.geo_clicked(clicked=self.bottom_buttons)
        elif QKeyEvent.text() == 'c':
            self.geo_clicked(clicked=self.right_bot_buttons)

    def create_button(self,text, slot_fcn, name=None, size_constraint = None):
        button = QPushButton(text)
        button.clicked.connect(slot_fcn)
        button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        if name is not None:
            button.setObjectName(name)
        if size_constraint and type(size_constraint) == dict:
            if 'height' in size_constraint:
                button.setMaximumHeight(size_constraint['height'])
            # if 'width' in size_constraint:
            #     button.setMaximumWidth(size_constraint['width'])
        return button

    def delete_clicked(self):
        if len(self.equationList) != 0:
            display = str()

            if len(self.equationList) != 0:
                del self.equationList[-1]

            for text in self.equationList:
                display += text
            self.display.setText(display)

    def geo_clicked(self, clicked= None):
        if clicked:
            clicked_button = clicked
        else:
            clicked_button = self.sender()
        geo_text = clicked_button.objectName()
        hierarchy_list = self.parsing_clipboard()
        display = str()

        if type(hierarchy_list) == Exception:
            return None

        if self.purpose == 'source':
            hierarchy_list[-1] = hierarchy_list[-1][:hierarchy_list[-1].find('[')]

        calc_expression = geo_text + f'({hierarchy_list})'.replace(" ","").replace("([", "(").replace("])", ")")
        if self.display.toPlainText() == '':
            self.equationList.append(calc_expression)
        else:
            print(f'len!!={len(self.value_str)}')
            self.equationList[-1] = calc_expression

        for text in self.equationList:
            display += text
        self.display.setText(display)

    def export_clicked(self):
        self.send_geometry_info_text.emit(self.display.toPlainText())
        self.destroy()

    def parsing_clipboard(self):
        try:
            print(self.clipboard.text())
            hierarchy_name_list = eval(self.clipboard.text())
            return hierarchy_name_list
        except:
            return self.abort_clipboard()

    def abort_clipboard(self):
        warnings.warn("You should select target layer first!")
        #debug option#
        if self.clipboard.text():
            print(self.clipboard.text())
        return Exception("No selected layer")

    def closeEvent(self, QCloseEvent):
        del self.address.cal

class CVariableWindow(QListWidget):
    request_ast_signal = pyqtSignal(str)
    send_selected_variable_ast_signal = pyqtSignal(str)
    send_selected_variable_name_signal = pyqtSignal(str)

    def __init__(self):
        super(CVariableWindow, self).__init__()
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.initUI()
        self.variable_name_list = []
        self.tmp_ast_id = None
        self.tmp_ast = None
        self.variable_ast_id_dict = dict()
        self.variable_ast_dict = collections.OrderedDict()
        self.itemDoubleClicked.connect(lambda item: self.send_selected_variable_ast_signal.emit(self.variable_ast_id_dict[item.text()]) )
        self.itemClicked.connect(lambda item: self.send_selected_variable_name_signal.emit(item.text()) )


    def initUI(self):
        pass

    def create_variable(self, name):
        self.request_ast_signal.emit(name)
        if self.tmp_ast_id:
            self.variable_ast_id_dict[name] = self.tmp_ast_id
            self.variable_ast_dict[name] = self.tmp_ast
            self.variable_name_list.append(name)
            self.addItem(name)

    def delete_variable(self, item):
        del self.variable_ast_id_dict[item.text()]
        del self.variable_ast_dict[item.text()]
        # name_idx = self.variable_name_list.index(item.text())
        # self.variable_name_list.pop(name_idx)
        self.removeItemWidget(item)

    def load_ast(self, _ast):
        self.tmp_ast_id = _ast._id
        self.tmp_ast = _ast

    def load_variables(self, info_dict:dict):
        if 'variables' in info_dict:
            self.addItems([var_ast.name for var_ast in info_dict['variables']])
            for var_ast in info_dict['variables']:
                self.variable_ast_id_dict[var_ast.name] = var_ast._id
                self.variable_ast_dict[var_ast.name] = var_ast

    def export_variables(self):
        output_list = [_ast for _ast in self.variable_ast_dict.values()]
        output_id_list = [_id for _id in self.variable_ast_id_dict.values()]
        self.clear()
        return output_list, output_id_list

    def clear(self):
        super(CVariableWindow, self).clear()
        self.variable_name_list = []
        self.tmp_ast_id = None
        self.variable_ast_id_dict = dict()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Delete:
            target_item = self.selectedItems()[0]
            if target_item:
                self.delete_variable(target_item)
