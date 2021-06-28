from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import warnings
import re
import copy
# import numpy as np
import os


class ExpressionCalculator(QWidget):
    # send_expression_signal =  pyqtSignal(dict)
    send_XYCreated_signal = pyqtSignal(str, dict)
    send_dummyconstraints_signal = pyqtSignal(dict, str)
    send_path_row_xy_signal = pyqtSignal(dict, str)
    presetDict = dict()

    def __init__(self,clipboard):
        # super(ExpressionCalculator, self).__init__()
        super().__init__()

        ######state_flag#######
        self.value_flag=False
        self.value_str = ''

        self.digit_flag=False
        self.waiting = False

        self.arithmetic_flag=False
        self.arithmetic_str = ''
        ########################

        self.clipboard = clipboard
        self.display= QTextEdit('')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight|Qt.AlignTop)
        self.display.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
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

        self.backspace = self.create_button('<-',self.delete_clicked)

        """
        option layout
        """
        self.xy_reference_toggling_group = QGroupBox()
        toggling_group_layout = QHBoxLayout()
        option_box_layout = QHBoxLayout()

        self.x_button = self.create_radio_button('X',self.xy_reference_clicked)
        self.y_button = self.create_radio_button('Y',self.xy_reference_clicked)
        self.xy_button = self.create_radio_button('XY',self.xy_reference_clicked)
        self.x_button.setChecked(True)

        toggling_group_layout.addWidget(self.x_button)
        toggling_group_layout.addWidget(self.y_button)
        toggling_group_layout.addWidget(self.xy_button)
        self.xy_reference_toggling_group.setLayout(toggling_group_layout)

        add_button = self.create_button('ADD',self.send_clicked, size_constraint=dict(height=35))
        edit_button = self.create_button('EDIT',self.edit_clicked, size_constraint=dict(height=35))
        export_button = self.create_button('EXPORT',self.export_clicked, size_constraint=dict(height=35))
        export_path_button = self.create_button('EXPORT FOR PATH',self.export_path_clicked, size_constraint=dict(height=35))

        option_box_layout.addWidget(self.xy_reference_toggling_group)
        option_box_layout.addWidget(add_button)
        option_box_layout.addWidget(edit_button)
        option_box_layout.addWidget(export_button)
        option_box_layout.addWidget(export_path_button)
        # option_box_layout.SetMaximumSize(50)
        option_box_layout.setSizeConstraint(QLayout.SetMaximumSize & QLayout.SizeConstraint.SetFixedSize)
        # option_box_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)

        """
        main layout
        """


        main_layout = QGridLayout()
        # main_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        dl_size = 5
        main_layout.addWidget(self.display, 0, 0, dl_size, 6)
        main_layout.addWidget(self.backspace, 0, 6, dl_size, 1)
        # main_layout.addWidget(self.display, 1, 8)

        for i in range(10):
            if i is not 0:
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

        main_layout.addWidget(self.div,dl_size,6)
        main_layout.addWidget(self.mul,dl_size+1,6)
        main_layout.addWidget(self.minus,dl_size+2,6)
        main_layout.addWidget(self.plus,dl_size+3,6)



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
        self.XWindow.setStyleSheet("background-image: url(" + os.getcwd().replace("\\",'/') + "/Image/X.png); background-position: center; background-color: rgb(255,255,255); background-repeat: no-repeat;")
        self.XWindow.itemClicked.connect(self.XitemClicked)
        self.YWindow = QListWidget()
        self.YWindow.setStyleSheet("background-image: url(" + os.getcwd().replace("\\",'/') + "/Image/Y.png); background-position: center; background-color: rgb(255,255,255); background-repeat: no-repeat;")
        self.YWindow.itemClicked.connect(self.YitemClicked)
        self.XYWindow = QListWidget()
        self.XYWindow.setStyleSheet("background-image: url(" + os.getcwd().replace("\\",'/') + "/Image/XY.png); background-position: center; background-color: rgb(255,255,255); background-repeat: no-repeat;")
        self.XYWindow.itemClicked.connect(self.XYitemClicked)
        self.presetWindow = QListWidget()
        self.presetWindow.itemClicked.connect(self.presetClicked)
        for _id in self.presetDict.keys():
            self.presetWindow.addItem(_id)
        H_layout1 = QHBoxLayout()
        H_layout2 = QHBoxLayout()
        H_layout3 = QHBoxLayout()

        H_layout1.addWidget(self.YWindow)
        H_layout1.addSpacing(283)
        H_layout2.addWidget(self.XYWindow)
        H_layout2.addWidget(self.XWindow)
        H_layout3.addWidget(self.presetWindow)
        top_layout.addLayout(H_layout1)
        top_layout.addLayout(H_layout2)
        top_layout.addLayout(H_layout3)

        # self.setLayout(main_layout)
        self.setLayout(top_layout)
        self.setWindowTitle('Expression Calculator')
        self.show()

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
            calc_expression = '['+str(event.scenePos().x())+','+str(event.scenePos().y())+']'

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
            self.show()
            self.waiting = False

    def create_radio_button(self, text, slot_fcn, name=None):
        button = QRadioButton(text)
        button.clicked.connect(slot_fcn)
        if name is not None:
            button.setObjectName(name)
        return button

    def arithmetic_clicked(self):
        clicked_button = self.sender()
        arith_sign = clicked_button.text()
        display = str()

        if self.value_flag:
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
        if len(self.equationList) is not 0:
            display = str()

            isDigit = False
            for num in range(10):
                if self.equationList[-1][-1] == str(num):
                    isDigit = True

            if isDigit or self.equationList[-1][-1] == '.':
                if len(self.equationList[-1]) == 1:
                    del self.equationList[-1]
                    self.value_flag = False
                    self.digit_flag = False
                    self.arithmetic_flag = True
                elif self.equationList[-1] == '0.':
                    del self.equationList[-1]
                    self.value_flag = False
                    self.digit_flag = False
                    self.arithmetic_flag = True
                else:
                    last = self.equationList[-1][:-1]
                    self.equationList[-1] = last
                    self.value_flag = True
                    self.digit_flag = True
                    self.arithmetic_flag = False
            elif self.equationList[-1][0:2] == '(-':
                if len(self.equationList[-1]) == 4:
                    del self.equationList[-1]
                    self.value_flag = False
                    self.digit_flag = False
                    self.arithmetic_flag = True
                else:
                    last = self.equationList[-1][:-2] + self.equationList[-1][-1]
                    self.equationList[-1] = last
                    self.value_flag = True
                    self.digit_flag = True
                    self.arithmetic_flag = False
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
                    else:
                        self.value_flag = True
                        self.digit_flag = False
                        self.arithmetic_flag = False
                else:
                    del self.equationList[-1]
                    self.value_flag = True
                    self.digit_flag = True
                    self.arithmetic_flag = False

            if len(self.equationList) is 0:
                    self.value_flag = False
                    self.digit_flag = False
                    self.arithmetic_flag = False

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

    def digit_clicked(self):
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
            else:
                if self.value_flag:
                    self.equationList[-1] = digit_value
                else:
                    if digit_value == '.':
                        self.equationList.append('0.')
                    else:
                        self.equationList.append(digit_value)

                    self.value_flag = True
                    self.digit_flag = True
                    self.arithmetic_flag = False

        for text in self.equationList:
            display += text
        self.display.setText(display)

        # clicked_button = self.sender()
        # if clicked_button.text() == '+/-':
        #     if len(self.value_str) < len(self.display.text()):
        #         if self.value_flag:
        #             if self.display.text()[-len(self.value_str)-1] == '+':
        #                 self.display.setText(self.display.text()[:-len(self.value_str)-1] + '-' + self.display.text()[-len(self.value_str):])
        #             elif self.display.text()[-len(self.value_str)-1] == '-':
        #                 self.display.setText(self.display.text()[:-len(self.value_str)-1] + '+' + self.display.text()[-len(self.value_str):])
        #             elif self.display.text()[-len(self.value_str):-len(self.value_str)+2] == '(-':
        #                 self.display.setText(self.display.text()[:-len(self.value_str)] + self.display.text()[-len(self.value_str)+2:-1])
        #                 self.value_str = self.value_str[2:-1]
        #             elif self.display.text()[-len(self.value_str)-1] == '*':
        #                 self.display.setText(self.display.text()[:-len(self.value_str)] + '(-' + self.display.text()[-len(self.value_str):] + ')')
        #                 self.value_str = '(-' + self.value_str + ')'
        #             elif self.display.text()[-len(self.value_str)-1] == '/':
        #                 self.display.setText(self.display.text()[:-len(self.value_str)] + '(-' + self.display.text()[-len(self.value_str):] + ')')
        #                 self.value_str = '(-' + self.value_str + ')'
        #         else:
        #             pass
        #         self.value_flag = True
        #         self.digit_flag = True
        #
        #     elif len(self.value_str) == len(self.display.text()):
        #         if len(self.display.text()) is not 0:
        #             if self.display.text()[0] is not '-':
        #                 self.display.setText('-' + self.display.text())
        #                 self.value_str = '-' + self.value_str
        #             else:
        #                 self.display.setText(self.display.text()[1:])
        #                 self.value_str = self.value_str[:1]
        #
        #
        # else:
        #     digit_value = str(clicked_button.text())
        #
        #     if self.digit_flag:
        #         self.display.setText(self.display.text() + digit_value)
        #         self.value_str += digit_value
        #         self.equationList[-1] = self.value_str
        #     else:
        #         if self.value_flag:
        #             self.display.setText(self.display.text()[:-len(self.value_str)] + digit_value)
        #             self.equationList[-1] = digit_value
        #         else:
        #             self.display.setText(self.display.text() + digit_value)
        #             self.equationList.append(digit_value)
        #         self.value_flag = True
        #         self.value_str = digit_value
        #         self.digit_flag = True

    def geo_clicked(self):
        clicked_button = self.sender()
        geo_text = clicked_button.objectName()
        hierarchy_list = self.parsing_clipboard()
        display = str()

        if type(hierarchy_list) == Exception:
            return None
        calc_expression = geo_text + f'({hierarchy_list})'.replace(" ","")
        if self.value_flag:
            print(f'len!!={len(self.value_str)}')
            self.equationList[-1] = calc_expression
        else:
            self.equationList.append(calc_expression)
        self.value_flag = True
        self.arithmetic_flag = False
        self.digit_flag = False

        for text in self.equationList:
            display += text
        self.display.setText(display)

        # clicked_button = self.sender()
        # geo_text = clicked_button.objectName()
        # hierarchy_list = self.parsing_clipboard()
        # if type(hierarchy_list) == Exception:
        #     return None
        # calc_expression = geo_text + f'({hierarchy_list})'
        # if self.value_flag:
        #     print(f'len!!={len(self.value_str)}')
        #     self.display.setText(self.display.text()[:-len(self.value_str)] + calc_expression)
        #     self.equationList[-1] = calc_expression
        # else:
        #     self.display.setText(self.display.text() + calc_expression)
        #     self.equationList.append(calc_expression)
        # self.value_flag = True
        # self.value_str = calc_expression
        # self.arithmetic_flag = False
        # self.digit_flag = False

    def xy_reference_clicked(self):
        pass

        # if function == 'lt':
        #     if XYFlag == 'X':
        #         result = f"self._DesignParameter['{operands[0]}']['_DesignObj']._DesignParameter['{operands[1]}']['_XYCoordinates'][0][0] " \
        #              f"-self._DesignParameter['{operands[0]}']['_DesignObj']._DesignParameter['{operands[1]}']['_XWidth']/2"
        #     elif XYFlag == 'Y':
        #         result = f"self._DesignParameter['{operands[0]}']['_DesignObj']._DesignParameter['{operands[1]}']['_XYCoordinates'][0][0]" \
        #              f"+ self._DesignParameter['{operands[0]}']['_DesignObj']._DesignParameter['{operands[1]}']['_YWidth']/2"
        #     elif XYFlag == 'XY':
        #         result = f" [self._DesignParameter['{operands[0]}']['_DesignObj']._DesignParameter['{operands[1]}']['_XYCoordinates'][0][0] " \
        #                  f"-self._DesignParameter['{operands[0]}']['_DesignObj']._DesignParameter['{operands[1]}']['_XWidth']/2," \
        #                  f"self._DesignParameter['{operands[0]}']['_DesignObj']._DesignParameter['{operands[1]}']['_XYCoordinates'][0][0]" \
        #                  f"+ self._DesignParameter['{operands[0]}']['_DesignObj']._DesignParameter['{operands[1]}']['_YWidth']/2]"

    def send_clicked(self):
        XYFlag = None
        if len(self.equationList) is not 0:
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

                if self.x_button.isChecked() is True:
                    self.showXWindow()
                    # XYFlag = 'X'
                elif self.y_button.isChecked() is True:
                    self.showYWindow()
                    # XYFlag = 'Y'
                elif self.xy_button.isChecked() is True:
                    # XYFlag = 'XY'
                    self.showXYWindow()
                self.equationList.clear()

        else:
            self.display.setText("Nothing In Here")

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
            self.presetDict[_id]['X'] = XList
            self.presetDict[_id]['Y'] = YList
            self.presetDict[_id]['XY'] = XYList

    def export_clicked(self, export_type = False):
        output = dict()
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
        output = {'X':XList, 'Y':YList, 'XY':XYList}
        # print(output)

        if not XYList:
            if XList and YList:
                pass
            else:
                self.warning = QMessageBox()
                self.warning.setText("X field and Y field both should not be empty")
                self.warning.show()
                return

        self.XWindow.clear()
        self.YWindow.clear()
        self.XYWindow.clear()

        if export_type == False:
            self.send_XYCreated_signal.emit('XYCoordinate', output)
        else:
            self.send_XYCreated_signal.emit(export_type, output)

    def export_path_clicked(self):
        if 'pw' not in self.__dict__:
            self.pw = PathWindow(self)
            self.pw.show()
            self.send_path_row_xy_signal.connect(self.pw.create_row)

        self.export_clicked('XYCoordinate_for_path_row')

    def getPathInfo(self, idDict):
        self.send_XYCreated_signal.emit('XYCoordinate_for_path', idDict)

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

    def test(self, dict, _id):
        self.presetDict[_id] = dict
        self.presetWindow.addItem(_id)
        print(self.presetDict)

    def presetClicked(self):
        _id = self.presetWindow.currentItem().text()
        XList = self.presetDict[_id]['X']
        YList = self.presetDict[_id]['Y']
        XYList = self.presetDict[_id]['XY']

        self.XWindow.clear()
        self.YWindow.clear()
        self.XYWindow.clear()

        for x in XList:
            self.XWindow.addItem(x)
        for y in YList:
            self.YWindow.addItem(y)
        for xy in XYList:
            self.XYWindow.addItem(xy)


class PathWindow(QWidget):
    send_output_signal = pyqtSignal(dict)

    def __init__(self, address):
        super().__init__()
        self.address = address
        self.initUI()

    def initUI(self):
        exportButton = QPushButton("Export", self)
        cancelButton = QPushButton("Cancel", self)

        exportButton.clicked.connect(self.exportButton_accepted)
        cancelButton.clicked.connect(self.cancelButton_accepted)

        self.XYdictForLineEdit = []
        self.XYdictForLabel = []

        self.XYdictForLabel.append(QLabel("XY1"))
        self.XYdictForLabel.append(QLabel("XY2"))

        self.XYdictForLineEdit.append(QLineEdit())
        self.XYdictForLineEdit.append(QLineEdit())
        self.XYdictForLineEdit[0].setReadOnly(True)
        self.XYdictForLineEdit[1].setReadOnly(True)


        self.setupVboxColumn1 = QVBoxLayout()
        self.setupVboxColumn2 = QVBoxLayout()
        setupBox = QHBoxLayout()

        self.setupVboxColumn1.addWidget(self.XYdictForLabel[0])
        self.setupVboxColumn1.addWidget(self.XYdictForLabel[1])

        self.setupVboxColumn2.addWidget(self.XYdictForLineEdit[0])
        self.setupVboxColumn2.addWidget(self.XYdictForLineEdit[1])

        setupBox.addLayout(self.setupVboxColumn1)
        setupBox.addLayout(self.setupVboxColumn2)

        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(exportButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(setupBox)
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        # vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Path Setup Window')
        self.setGeometry(300, 300, 500, 500)
        self.show()

    def create_row(self, constraint_dict, _id):
        CurrentEditPointNum = len(self.XYdictForLineEdit) - 2
        self.XYdictForLineEdit[CurrentEditPointNum].setText(_id)
        self.UpdateXYwidget()

    def exportButton_accepted(self):
        output = dict(XYidlist=list())
        self.send_output_signal.connect(self.address.getPathInfo)

        for idx in range(len(self.XYdictForLineEdit)-2):
            output['XYidlist'].append(self.XYdictForLineEdit[idx].text())

        self.send_output_signal.emit(output)
        self.destroy()

    def cancelButton_accepted(self):
        self.destroy()

    def UpdateXYwidget(self):
        CurrentPointNum = len(self.XYdictForLineEdit)
        NewPointNum = CurrentPointNum + 1
        LabelText = "XY" + str(NewPointNum)

        self.XYdictForLabel.append(QLabel(LabelText))
        self.XYdictForLineEdit.append(QLineEdit())

        self.setupVboxColumn1.addWidget(self.XYdictForLabel[-1])
        self.setupVboxColumn2.addWidget(self.XYdictForLineEdit[-1])
        self.XYdictForLineEdit[-1].setReadOnly(True)