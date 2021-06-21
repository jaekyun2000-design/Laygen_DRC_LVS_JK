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
        self.display= QLineEdit('')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight|Qt.AlignTop)
        self.display.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
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

        self.plus = self.create_button('+',self.arithmetic_clicked)
        self.minus = self.create_button('-',self.arithmetic_clicked)
        self.mul = self.create_button('*',self.arithmetic_clicked)
        self.div = self.create_button('/',self.arithmetic_clicked)

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

        export_button = self.create_button('EXPORT',self.send_clicked)

        option_box_layout.addWidget(self.xy_reference_toggling_group)
        option_box_layout.addWidget(export_button)
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
        self.YWindow = QListWidget()
        self.YWindow.setStyleSheet("background-image: url(" + os.getcwd().replace("\\",'/') + "/Image/Y.png); background-position: center; background-color: rgb(255,255,255); background-repeat: no-repeat;")
        self.XYWindow = QListWidget()
        self.XYWindow.setStyleSheet("background-image: url(" + os.getcwd().replace("\\",'/') + "/Image/XY.png); background-position: center; background-color: rgb(255,255,255); background-repeat: no-repeat;")
        H_layout1 = QHBoxLayout()
        H_layout2 = QHBoxLayout()

        H_layout1.addWidget(self.YWindow)
        H_layout1.addSpacing(283)
        H_layout2.addWidget(self.XYWindow)
        H_layout2.addWidget(self.XWindow)
        top_layout.addLayout(H_layout1)
        top_layout.addLayout(H_layout2)

        # self.setLayout(main_layout)
        self.setLayout(top_layout)
        self.setWindowTitle('Expression Calculator')
        self.show()

    def create_button(self,text, slot_fcn, name=None):
        button = QPushButton(text)
        button.clicked.connect(slot_fcn)
        button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        if name is not None:
            button.setObjectName(name)
        return button

    def click_clicked(self):
        self.hide()
        self.waiting = True

    def waitForClick(self, event):
        if self.waiting == True:
            calc_expression = '['+str(event.scenePos().x())+','+str(event.scenePos().y())+']'

            if self.value_flag:
                print(f'len!!={len(self.value_str)}')
                self.display.setText(self.display.text()[:-len(self.value_str)] + calc_expression)
                self.equationList[-1] = calc_expression
            else:
                self.display.setText(self.display.text() + calc_expression)
                self.equationList.append(calc_expression)

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
        self.XWindow.addItem(self.display.text())
        self.display.clear()

    def showYWindow(self):
        self.YWindow.addItem(self.display.text())
        self.display.clear()

    def showXYWindow(self):
        self.XYWindow.addItem(self.display.text())
        self.display.clear()

    def digit_clicked(self):
        clicked_button = self.sender()
        display = str()
        if clicked_button.text() == '+/-':
            if len(self.equationList) == 0:
                pass
            elif len(self.equationList) == 1:
                if self.equationList[-1][0] == '-':
                    self.equationList[-1] = self.equationList[-1][1:]
                else:
                    self.equationList[-1] = '-' + self.equationList[-1]
            else:
                if self.value_flag:
                    if self.equationList[-2] == '+':
                        self.equationList[-2] = '-'
                    elif self.equationList[-2] == '-':
                        self.equationList[-2] = '+'
                    elif self.equationList[-2] == '*' or self.equationList[-2] == '/':
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
                    pass
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
        calc_expression = geo_text + f'({hierarchy_list})'
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
    def expressionTransformer(self, expression, XYFlag):
        """
        :param expression: code to be re-expressed
        :param XYFlag: Which mode is checked?
        :return: re-expressed code
        """
        function = expression[0:2]
        if function == 'to':
            function = 'top'
        elif function == 'bo':
            function = 'bottom'
        elif function == 'le':
            function = 'left'
        elif function == 'ri':
            function = 'right'
        elif function == 'ce':
            function = 'center'
        elif function == 'wi':
            function = 'width'
        elif function == 'he':
            function = 'height'

        operands = re.split(',', re.sub(f'{function}|\(|\'|\)|\[|]', "", expression))
        code = 'self.'                  # Code Always Starts with 'self.' string
        layer = operands[-1]
        objects = operands[0: len(operands)-1]
        for i in range(len(objects)):           # append code from the start
            code = code + f"_DesignParameter['{objects[i]}']['_DesignObj']."
        code = code + f"_DesignParameter['{layer}']"
        if function == 'width':
            result = code + '[\'_XWidth\']'
        elif function == 'height':
            result = code + '[\'_YWidth\']'

        if XYFlag == 'X':
            if function == 'lt' or function == 'left' or function == 'lb':
                result = f"{code}['_XYCoordinates'][0][0] - {code}['_XWidth']/2"
            elif function == 'top' or function == 'bottom' or function == 'center':
                result = f"{code}['_XYCoordinates'][0][0]"
            elif function == 'rt' or function == 'right' or function == 'rb':
                result = f"{code}['_XYCoordinates'][0][0] + {code}['_XWidth']/2"
            else:   # Width or Height case
                print(f" XYFlag Redundant: input function: {function}, XYFlag = {XYFlag} for Debugging")
        elif XYFlag == 'Y':
            if function == 'lt' or function == 'rt' or function == 'top':
                result = f"{code}['_XYCoordinates'][0][1] + {code}['_YWidth']/2"
            elif function == function == 'left' or function == 'right' or function == 'center':
                result = f"{code}['_XYCoordinates'][0][1]"
            elif function == function == 'lb' or function == 'rb' or function == 'bottom':
                result = f"{code}['_XYCoordinates'][0][0] - {code}['_YWidth']/2"
            else:   # Width or Height case
                print(f" XYFlag Redundant: input function: {function}, XYFlag = {XYFlag} for Debugging")
                pass
        elif XYFlag == 'XY':
        # X Input first
            if function == 'lt' or function == 'left' or function == 'lb':
                result = f"{code}['_XYCoordinates'][0][0] - {code}['_XWidth']/2"
            elif function == function == 'top' or function == 'bottom' or function == 'center':
                result = f"{code}['_XYCoordinates'][0][0]"
            elif function == 'rt' or function == 'right' or function == 'rb':
                result = f"{code}['_XYCoordinates'][0][0] + {code}['_XWidth']/2"
            else:   # Width or Height case
                print(f" XYFlag Redundant: input function: {function}, XYFlag = {XYFlag}_X for Debugging")
                pass
        # Y input afterwards
            if function == 'lt' or function == 'rt' or function == 'top':
                result = result + f", {code}['_XYCoordinates'][0][1] + {code}['_YWidth']/2"
            elif function == 'left' or function == 'right' or function == 'center':
                result = result + f", {code}['_XYCoordinates'][0][1]"
            elif function == 'lb' or function == 'rb' or function == 'bottom':
                result = result + f", {code}['_XYCoordinates'][0][0] - {code}['_YWidth']/2"
            else:  # Width or Height case
                print(f" XYFlag Redundant: input function: {function}, XYFlag = {XYFlag}_Y for Debugging")
                pass
            result = re.split(',', result)
        print(f"Re-Expressed Element: \n{result}")
        return result

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
                    self.display.setText(self.display.text()[:-1])
                # self.equationList.clear()
                self.value_flag = False
                self.digit_flag = False
                self.arithmetic_flag = False

                if self.x_button.isChecked() is True:
                    self.showXWindow()
                    XYFlag = 'X'
                elif self.y_button.isChecked() is True:
                    self.showYWindow()
                    XYFlag = 'Y'
                elif self.xy_button.isChecked() is True:
                    XYFlag = 'XY'
                    self.showXYWindow()


                for i in range(len(self.equationList)):
                    isFunction = re.search('\(\[\'.*\'\]\)', self.equationList[i])
                    if isFunction != None:
                        re_expressed_element = self.expressionTransformer(self.equationList[i], XYFlag = XYFlag)
                        self.equationList[i] = re_expressed_element
                    else:
                        pass
                if XYFlag != 'XY':
                    FinalCode = ' '.join(self.equationList)
                elif XYFlag == 'XY':
                    # X_calc
                    x_list = copy.deepcopy(self.equationList)
                    for i in range(len(x_list)):
                        if type(x_list[i]) == list:
                            x_list[i] = x_list[i][0]
                    # Y_calc
                    y_list = copy.deepcopy(self.equationList)
                    for i in range(len(y_list)):
                        if type(y_list[i]) == list:
                            y_list[i] = y_list[i][1]
                    X_expression = ' '.join(x_list)
                    Y_expression = ' '.join(y_list)
                    FinalCode = list()
                    FinalCode.append(X_expression)
                    FinalCode.append(Y_expression)

                    # for i in range(len(self.equationList)):
                    #     if type(self.equationList[i]) != list:
                    #         self.equationList[i] = [self.equationList[i],self.equationList[i]]
                    # tmpCode = ' '.join(self.equationList)
                    # mul_div_list = re.sub('\+|-',tmpCode)
                    # mul_div_list_elements = mul_div_list.split()
                    # for i in range(len(mul_div_list_elements)):
                    #     if mul_div_list_elements[i] == '*':
                    #         product = np.multiply(mul_div_list_elements[i-1], mul_div_list_elements[i+1])
                    #         self.equationList[i-1] = product
                    #         self.equationList.remove(i)
                    #         self.equationList.remove(i+1)
                    #     elif mul_div_list_elements[i] == '/':
                    #         quotient = np.divide(mul_div_list_elements[i-1], mul_div_list_elements[i+1])
                    #         self.equationList[i-1] = quotient
                    #         self.equationList.remove(i)
                    #         self.equationList.remove(i+1)

                print(f"Final Code: \n {FinalCode}")
                self.equationList.clear()

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

