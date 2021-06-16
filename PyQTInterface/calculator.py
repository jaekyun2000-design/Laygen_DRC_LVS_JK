from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import warnings
class ExpressionCalculator(QWidget):
    def __init__(self,clipboard):
        # super(ExpressionCalculator, self).__init__()
        super().__init__()

        ######state_flag#######
        self.value_flag=False
        self.value_str = ''

        self.digit_flag=False

        self.arithmetic_flag=False
        self.arithmetic_str = ''
        ########################



        self.clipboard = clipboard
        self.display= QLineEdit('')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)

        font = self.display.font()
        font.setPointSize(font.pointSize()+8)
        self.display.setFont(font)
        self.init_ui()

    def init_ui(self):
        self.digit_buttons = []
        for i in range(10):
            self.digit_buttons.append(self.create_button(f'{i}', self.digit_clicked))
        self.top_buttons = self.create_button('top', self.geo_clicked)
        self.right_buttons = self.create_button('right', self.geo_clicked)
        self.left_buttons = self.create_button('left', self.geo_clicked)
        self.bottom_buttons = self.create_button('bottom', self.geo_clicked)
        self.center_buttons = self.create_button('center',self.geo_clicked)

        self.plus = self.create_button('+',self.arithmetic_clicked)
        self.minus = self.create_button('-',self.arithmetic_clicked)
        self.mul = self.create_button('*',self.arithmetic_clicked)
        self.div = self.create_button('/',self.arithmetic_clicked)

        main_layout = QGridLayout()
        main_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        main_layout.addWidget(self.display, 0, 0, 2, 8)

        for i in range(10):
            row = ((9-i) / 3)+2
            col = ((i-1) % 3)+4
            main_layout.addWidget(self.digit_buttons[i], row, col)
        main_layout.addWidget(self.top_buttons,2,2)
        main_layout.addWidget(self.bottom_buttons,4,2)
        main_layout.addWidget(self.left_buttons,3,1)
        main_layout.addWidget(self.right_buttons,3,3)
        main_layout.addWidget(self.center_buttons,3,2)

        main_layout.addWidget(self.div,2,7)
        main_layout.addWidget(self.mul,3,7)
        main_layout.addWidget(self.minus,4,7)
        main_layout.addWidget(self.plus,5,7)


        self.setLayout(main_layout)
        self.setWindowTitle('Expression Calculator')
        self.show()

    def create_button(self,text, slot_fcn):
        button = QPushButton(text)
        button.clicked.connect(slot_fcn)
        return button

    def arithmetic_clicked(self):
        clicked_button = self.sender()
        arith_sign = clicked_button.text()

        if self.value_flag:
            self.display.setText(self.display.text() + arith_sign)
            self.arithmetic_flag = True
        elif self.arithmetic_flag:
            self.display.setText(self.display.text()[:-1] + arith_sign)
        else:
            return
        self.value_flag = False
        self.digit_flag = False



    def digit_clicked(self):
        clicked_button = self.sender()
        digit_value = str(int(clicked_button.text()))

        if self.digit_flag:
            self.display.setText(self.display.text() + digit_value)
            self.value_str += digit_value
        else:
            if self.value_flag:
                self.display.setText(self.display.text()[:-len(self.value_str)] + digit_value)
            else:
                self.display.setText(self.display.text() + digit_value)
            self.value_flag = True
            self.value_str = digit_value
            self.digit_flag = True

    def geo_clicked(self):
        clicked_button = self.sender()
        geo_text = clicked_button.text()
        hierarchy_list = self.parsing_clipboard()
        if type(hierarchy_list) == Exception:
            return None
        calc_expression = geo_text + f'({hierarchy_list})'
        if self.value_flag:
            print(f'len!!={len(self.value_str)}')
            self.display.setText(self.display.text()[:-len(self.value_str)] + calc_expression)
        else:
            self.display.setText(self.display.text() + calc_expression)
        self.value_flag = True
        self.value_str = calc_expression
        self.arithmetic_flag = False
        self.digit_flag = False

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