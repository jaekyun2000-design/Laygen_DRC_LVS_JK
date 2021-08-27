from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import warnings
import re
import copy
# import numpy as np
import os
from generatorLib import drc_api

class CreateConditionalStatement(QWidget):
    def __init__(self):
        super().__init__()
        self.operator = ['==', '!=', '>', '<', '>=', '<=', 'is', 'is not', 'in', 'not in', 'None']
        self.init_ui()

    def init_ui(self):
        var_label = QLabel('variable')
        self.var_input = QLineEdit()
        var_layout = QVBoxLayout()
        var_layout.addWidget(var_label)
        var_layout.addWidget(self.var_input)

        operator_label = QLabel('operator')
        self.operator_input = QComboBox()
        self.operator_input.addItems(self.operator)
        self.operator_input.currentTextChanged.connect(self.operator_changed)
        operator_layout = QVBoxLayout()
        operator_layout.addWidget(operator_label)
        operator_layout.addWidget(self.operator_input)

        condition_label = QLabel('condition')
        self.condition_input = QLineEdit()
        condition_layout = QVBoxLayout()
        condition_layout.addWidget(condition_label)
        condition_layout.addWidget(self.condition_input)

        ok_button = QPushButton()
        ok_button.setText('OK')
        ok_button.clicked.connect(self.ok_clicked)

        cancel_button = QPushButton()
        cancel_button.setText('cancel')
        cancel_button.clicked.connect(self.cancel_clicked)

        input_layout = QHBoxLayout()
        input_layout.addLayout(var_layout)
        input_layout.addLayout(operator_layout)
        input_layout.addLayout(condition_layout)

        button_layout = QHBoxLayout()
        button_layout.addSpacing(200)
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

        self.show()

    def operator_changed(self, op_input):
        if op_input == 'None':
            self.condition_input.setStyleSheet("QLineEdit{background:rgb(222,222,222);}")
            self.condition_input.setReadOnly(True)
        else:
            self.condition_input.setStyleSheet("QLineEdit{background:rgb(255,255,255);}")
            self.condition_input.setReadOnly(False)

    def ok_clicked(self):
        if self.operator_input.currentText() == 'None':
            if self.var_input.text() == '':
                self.warning = QMessageBox()
                self.warning.setText("Fill variable")
                self.warning.show()
        elif self.operator_input.currentText() != 'None':
            if self.var_input.text() == '' or self.condition_input.text() == '':
                self.warning = QMessageBox()
                self.warning.setText("Fill variable and condition")
                self.warning.show()
            else:
                print(self.var_input.text(), self.operator_input.currentText(), self.condition_input.text())
                self.destroy()

    def cancel_clicked(self):
        self.destroy()
