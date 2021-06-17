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
        self.display.setAlignment(Qt.AlignRight|Qt.AlignTop)
        self.display.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)


        font = self.display.font()
        font.setPointSize(font.pointSize()+8)
        self.display.setFont(font)
        self.init_ui()

    def init_ui(self):
        self.digit_buttons = []
        for i in range(10):
            self.digit_buttons.append(self.create_button(f'{i}', self.digit_clicked))
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
        self.height_button = self.create_button('height',self.geo_clicked,'height')

        self.plus = self.create_button('+',self.arithmetic_clicked)
        self.minus = self.create_button('-',self.arithmetic_clicked)
        self.mul = self.create_button('*',self.arithmetic_clicked)
        self.div = self.create_button('/',self.arithmetic_clicked)

        """
        option layout
        """
        self.xy_reference_toggling_group = QGroupBox()
        toggling_group_layout = QHBoxLayout()
        option_box_layout = QHBoxLayout()

        x_button = self.create_radio_button('X',self.xy_reference_clicked)
        y_button = self.create_radio_button('Y',self.xy_reference_clicked)
        xy_button = self.create_radio_button('XY',self.xy_reference_clicked)
        x_button.setChecked(True)
        toggling_group_layout.addWidget(x_button)
        toggling_group_layout.addWidget(y_button)
        toggling_group_layout.addWidget(xy_button)
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
        main_layout.addWidget(self.display, 0, 0, dl_size, 7)
        # main_layout.addWidget(self.display, 1, 8)

        for i in range(10):
            row = ((9-i) / 3)+dl_size
            col = ((i-1) % 3)+3
            main_layout.addWidget(self.digit_buttons[i], row, col)
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
        top_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        top_layout.addLayout(option_box_layout)
        top_layout.setStretchFactor(option_box_layout,0)
        top_layout.addLayout(main_layout)


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

    def create_radio_button(self, text, slot_fcn, name=None):
        button = QRadioButton(text)
        button.clicked.connect(slot_fcn)
        if name is not None:
            button.setObjectName(name)
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
        geo_text = clicked_button.objectName()
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

    def xy_reference_clicked(self):
        pass

    def send_clicked(self):
        pass

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

