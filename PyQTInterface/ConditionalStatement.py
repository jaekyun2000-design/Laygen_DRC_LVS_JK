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

class createConditionalStatement(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        and_button = QPushButton()
        and_button.setText('AND')
        and_button.clicked.connect(self.and_or_clicked)

        or_button = QPushButton()
        or_button.setText('OR')
        or_button.clicked.connect(self.and_or_clicked)

        ok_button = QPushButton()
        ok_button.setText('OK')
        ok_button.clicked.connect(self.ok_clicked)

        cancel_button = QPushButton()
        cancel_button.setText('cancel')
        cancel_button.clicked.connect(self.cancel_clicked)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(and_button)
        self.button_layout.addWidget(or_button)
        self.button_layout.addSpacing(150)
        self.button_layout.addWidget(ok_button)
        self.button_layout.addWidget(cancel_button)

        self.input_widget = createConditionalStatementCapsule()
        input_layout = self.input_widget.new_line()

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(input_layout)
        self.main_layout.addLayout(self.button_layout)
        self.setLayout(self.main_layout)

        self.show()

    def and_or_clicked(self,_):
        sender = self.sender()

        input_layout = self.input_widget.add_line(sender.text())

        self.main_layout.removeItem(self.button_layout)
        self.main_layout.addLayout(input_layout)
        self.main_layout.addLayout(self.button_layout)
        self.setLayout(self.main_layout)

    def ok_clicked(self):
        output_list = list()
        output_dict_list = self.input_widget.output_dict_list
        output_and_or_list = self.input_widget.output_and_or_list

        for output_dict in output_dict_list:
            if output_dict['operator'] == 'None':
                if output_dict['variable'] == '':
                    self.warning = QMessageBox()
                    self.warning.setText("Fill variable")
                    self.warning.show()
                    return

            elif output_dict['operator'] != 'None':
                if output_dict['variable'] == '' or output_dict['condition'] == '':
                    self.warning = QMessageBox()
                    self.warning.setText("Fill variable and condition")
                    self.warning.show()
                    return

            output_list.append(output_dict)
            idx = output_dict_list.index(output_dict)
            if idx != len(output_dict_list)-1:
                output_list.append(output_and_or_list[idx])

        print(output_list)
        self.destroy()

    def cancel_clicked(self):
        self.destroy()


class createConditionalStatementCapsule(QWidget):
    def __init__(self):
        super().__init__()
        self.operator = ['==', '!=', '>', '<', '>=', '<=', 'is', 'is not', 'in', 'not in', 'None']
        self.output_dict_list = list()
        self.output_and_or_list = list()

    def new_line(self):
        output_dict = dict(variable=None,
                           operator='==',
                           condition=None)
        self.output_dict_list.append(output_dict)

        var_label = QLabel('variable')
        var_input = QLineEdit()
        var_input.textChanged.connect(self.update_output_dict)
        var_layout = QVBoxLayout()
        var_layout.addWidget(var_label)
        var_layout.addWidget(var_input)

        operator_label = QLabel('operator')
        operator_input = QComboBox()
        operator_input.addItems(self.operator)
        operator_input.currentTextChanged.connect(self.operator_changed)
        operator_input.currentTextChanged.connect(self.update_output_dict)
        operator_layout = QVBoxLayout()
        operator_layout.addWidget(operator_label)
        operator_layout.addWidget(operator_input)

        condition_label = QLabel('condition')
        condition_input = QLineEdit()
        condition_input.textChanged.connect(self.update_output_dict)
        condition_layout = QVBoxLayout()
        condition_layout.addWidget(condition_label)
        condition_layout.addWidget(condition_input)

        input_layout = QHBoxLayout()
        input_layout.addLayout(var_layout)
        input_layout.addLayout(operator_layout)
        input_layout.addLayout(condition_layout)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(input_layout)

        return self.main_layout

    def add_line(self, and_or):
        output_dict = dict(variable=None,
                           operator='==',
                           condition=None)
        self.output_dict_list.append(output_dict)
        self.output_and_or_list.append(and_or)

        _label = QLabel('')

        self.var_input = QLineEdit()
        self.var_input.textChanged.connect(self.update_output_dict)
        var_layout = QVBoxLayout()
        var_layout.addWidget(_label)
        var_layout.addWidget(self.var_input)

        and_or_label = QLabel(and_or)
        self.operator_input = QComboBox()
        self.operator_input.addItems(self.operator)
        self.operator_input.currentTextChanged.connect(self.operator_changed)
        self.operator_input.currentTextChanged.connect(self.update_output_dict)
        operator_layout = QVBoxLayout()
        operator_layout.addWidget(and_or_label)
        operator_layout.addWidget(self.operator_input)

        self.condition_input = QLineEdit()
        self.condition_input.textChanged.connect(self.update_output_dict)
        condition_layout = QVBoxLayout()
        condition_layout.addWidget(_label)
        condition_layout.addWidget(self.condition_input)

        input_layout = QHBoxLayout()
        input_layout.addLayout(var_layout)
        input_layout.addLayout(operator_layout)
        input_layout.addLayout(condition_layout)

        self.main_layout.addLayout(input_layout)

        return self.main_layout

    def operator_changed(self,_):
        sender = self.sender()

        for i in range(len(self.output_dict_list)):
            op = self.main_layout.itemAt(i).itemAt(1).itemAt(1).widget()
            if sender == op:
                break

        if sender.currentText() == 'None':
            self.main_layout.itemAt(i).itemAt(2).itemAt(1).widget().setStyleSheet("QLineEdit{background:rgb(222,222,222);}")
            self.main_layout.itemAt(i).itemAt(2).itemAt(1).widget().setReadOnly(True)
        else:
            self.main_layout.itemAt(i).itemAt(2).itemAt(1).widget().setStyleSheet("QLineEdit{background:rgb(255,255,255);}")
            self.main_layout.itemAt(i).itemAt(2).itemAt(1).widget().setReadOnly(False)

    def update_output_dict(self, _):
        for i in range(len(self.output_dict_list)):
            var = self.main_layout.itemAt(i).itemAt(0).itemAt(1).widget().text()
            op = self.main_layout.itemAt(i).itemAt(1).itemAt(1).widget().currentText()
            cond = self.main_layout.itemAt(i).itemAt(2).itemAt(1).widget().text()
            self.output_dict_list[i]['variable'] = var
            self.output_dict_list[i]['operator'] = op
            self.output_dict_list[i]['condition'] = cond

class applyConditionalStatement(QWidget):
    def __init__(self):
        super().__init__()
        self.option = ['if', 'dummy']
        self.init_ui()

    def init_ui(self):
        option_input = QComboBox()
        option_input.addItems(self.option)
        option_input.currentTextChanged.connect(self.option_changed)

        if_button = QPushButton()
        if_button.setText('if')

        else_button = QPushButton()
        else_button.setText('else')

        ok_button = QPushButton()
        ok_button.setText('OK')
        ok_button.clicked.connect(self.ok_clicked)

        cancel_button = QPushButton()
        cancel_button.setText('cancel')
        cancel_button.clicked.connect(self.cancel_clicked)

        button_layout = QHBoxLayout()
        button_layout.addWidget(if_button)
        button_layout.addWidget(else_button)

        self.option_layout = QHBoxLayout()
        self.option_layout.addWidget(option_input)
        self.option_layout.addSpacing(150)
        self.option_layout.addLayout(button_layout)

        self.setLayout(self.option_layout)

        self.show()

    def option_changed(self):
        sender = self.sender()

        if sender.currentText() == 'if':
            if_button = QPushButton()
            if_button.setText('if')

            else_button = QPushButton()
            else_button.setText('else')

            old_button_layout = self.option_layout.itemAt(2)
            for i in range(old_button_layout.count()):
                old_button_layout.removeItem(old_button_layout.itemAt(i))
            self.option_layout.removeItem(old_button_layout)
            button_layout = QHBoxLayout()
            button_layout.addWidget(if_button)
            button_layout.addWidget(else_button)
            self.option_layout.addLayout(button_layout)

            self.setLayout(self.option_layout)

        else:
            if_button = QPushButton()
            if_button.setText('else')

            else_button = QPushButton()
            else_button.setText('if')

            dummy_button = QPushButton()
            dummy_button.setText('dummy')

            old_button_layout = self.option_layout.itemAt(2)
            for i in range(old_button_layout.count()):
                old_button_layout.removeItem(old_button_layout.itemAt(i))
            self.option_layout.removeItem(old_button_layout)
            button_layout = QHBoxLayout()
            button_layout.addWidget(if_button)
            button_layout.addWidget(else_button)
            button_layout.addWidget(dummy_button)
            self.option_layout.addLayout(button_layout)

            self.setLayout(self.option_layout)
