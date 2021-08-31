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
    send_output_dict_signal = pyqtSignal(dict)

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

    def and_or_clicked(self, _):
        sender = self.sender()

        input_layout = self.input_widget.add_line(sender.text())

        self.main_layout.removeItem(self.button_layout)
        self.main_layout.addLayout(input_layout)
        self.main_layout.addLayout(self.button_layout)
        self.setLayout(self.main_layout)

    def ok_clicked(self):
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
        if len(output_and_or_list) == 0:
            tmp_dict = output_dict
        else:
            for idx in range(len(output_and_or_list)):
                tmp_dict = dict(variable=None,
                                operator=None,
                                condition=None)
                tmp_dict['variable'] = output_dict_list[idx]
                tmp_dict['operator'] = output_and_or_list[idx]
                tmp_dict['condition'] = output_dict_list[idx + 1]

                output_dict_list[idx + 1] = tmp_dict

        print(tmp_dict)
        self.send_output_dict_signal.emit(tmp_dict)
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

    def operator_changed(self, _):
        sender = self.sender()

        for i in range(len(self.output_dict_list)):
            op = self.main_layout.itemAt(i).itemAt(1).itemAt(1).widget()
            if sender == op:
                break

        if sender.currentText() == 'None':
            self.main_layout.itemAt(i).itemAt(2).itemAt(1).widget().setStyleSheet(
                "QLineEdit{background:rgb(222,222,222);}")
            self.main_layout.itemAt(i).itemAt(2).itemAt(1).widget().setReadOnly(True)
        else:
            self.main_layout.itemAt(i).itemAt(2).itemAt(1).widget().setStyleSheet(
                "QLineEdit{background:rgb(255,255,255);}")
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
    send_output_list_signal = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.input_widget = applyConditionalStatementCapsule()

        if_button = QPushButton()
        if_button.setText('if')
        if_button.setMinimumWidth(50)
        if_button.setMaximumWidth(50)
        if_button.clicked.connect(self.stmt_clicked)
        if_button.clicked.connect(self.change_if)

        else_button = QPushButton()
        else_button.setText('else')
        else_button.setDisabled(True)
        else_button.setMinimumWidth(50)
        else_button.setMaximumWidth(50)
        else_button.clicked.connect(self.stmt_clicked)
        else_button.clicked.connect(self.disable_else)

        for_button = QPushButton()
        for_button.setText('for')
        for_button.setMinimumWidth(50)
        for_button.setMaximumWidth(50)
        for_button.clicked.connect(self.stmt_clicked)
        for_button.clicked.connect(self.disable_else)

        while_button = QPushButton()
        while_button.setText('while')
        while_button.setMinimumWidth(50)
        while_button.setMaximumWidth(50)
        while_button.clicked.connect(self.stmt_clicked)
        while_button.clicked.connect(self.disable_else)

        ok_button = QPushButton()
        ok_button.setText('OK')
        ok_button.clicked.connect(self.ok_clicked)

        cancel_button = QPushButton()
        cancel_button.setText('cancel')
        cancel_button.clicked.connect(self.cancel_clicked)

        option_layout = QHBoxLayout()
        option_layout.addWidget(if_button)
        option_layout.addWidget(else_button)
        option_layout.addWidget(for_button)
        option_layout.addWidget(while_button)
        option_layout.addSpacing(600)

        self.button_layout = QHBoxLayout()
        self.button_layout.addSpacing(300)
        self.button_layout.addWidget(ok_button)
        self.button_layout.addWidget(cancel_button)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(option_layout)
        self.main_layout.addSpacing(30)
        self.main_layout.addLayout(self.button_layout)

        self.setLayout(self.main_layout)

        self.setMinimumWidth(600)
        self.setMaximumWidth(600)

        self.show()

    def change_if(self):
        sender = self.sender()
        sender.setText('elif')

        self.main_layout.itemAt(0).itemAt(1).widget().setDisabled(False)

    def disable_else(self):
        self.main_layout.itemAt(0).itemAt(0).widget().setText('if')
        self.main_layout.itemAt(0).itemAt(1).widget().setDisabled(True)

    def stmt_clicked(self):
        sender = self.sender()

        input_layout = self.input_widget.new_line(sender.text())

        self.main_layout.removeItem(self.button_layout)
        self.main_layout.addLayout(input_layout)
        self.main_layout.addLayout(self.button_layout)
        self.input_widget.main_layout = self.main_layout
        self.setLayout(self.main_layout)

    def ok_clicked(self):
        output_list = self.input_widget.update_output_dict()

        self.send_output_list_signal.emit(output_list)
        self.destroy()

    def cancel_clicked(self):
        self.destroy()


class applyConditionalStatementCapsule(QWidget):
    def __init__(self):
        super().__init__()

    def new_line(self, clicked_button):
        stmt_label = QLabel(clicked_button)
        stmt_label.setMinimumWidth(30)
        stmt_label.setMaximumWidth(30)

        exp_input = QLineEdit()

        hbox1 = QHBoxLayout()
        hbox1.addWidget(stmt_label)
        hbox1.addWidget(exp_input)

        if_button = QPushButton()
        if_button.setText('if')
        if_button.indent = 0
        if_button.setMinimumWidth(50)
        if_button.setMaximumWidth(50)
        if_button.clicked.connect(self.stmt_clicked)
        if_button.clicked.connect(self.change_if)

        else_button = QPushButton()
        else_button.setText('else')
        else_button.setDisabled(True)
        else_button.indent = 0
        else_button.setMinimumWidth(50)
        else_button.setMaximumWidth(50)
        else_button.clicked.connect(self.stmt_clicked)
        else_button.clicked.connect(self.disable_else)

        for_button = QPushButton()
        for_button.setText('for')
        for_button.indent = 0
        for_button.setMinimumWidth(50)
        for_button.setMaximumWidth(50)
        for_button.clicked.connect(self.stmt_clicked)
        for_button.clicked.connect(self.disable_else)

        while_button = QPushButton()
        while_button.setText('while')
        while_button.indent = 0
        while_button.setMinimumWidth(50)
        while_button.setMaximumWidth(50)
        while_button.clicked.connect(self.stmt_clicked)
        while_button.clicked.connect(self.disable_else)

        hbox2 = QHBoxLayout()
        hbox2.addSpacing(35)
        hbox2.addWidget(if_button)
        hbox2.addWidget(else_button)
        hbox2.addWidget(for_button)
        hbox2.addWidget(while_button)
        hbox2.addSpacing(600)

        main_layout = QVBoxLayout()
        main_layout.addLayout(hbox1)
        main_layout.addLayout(hbox2)

        return main_layout

    def change_if(self):
        sender = self.sender()
        sender.setText('elif')

        for i in range(2, self.main_layout.count() - 1):
            if sender == self.main_layout.itemAt(i).itemAt(1).itemAt(1).widget() or \
                    sender == self.main_layout.itemAt(i).itemAt(1).itemAt(2).widget() or \
                    sender == self.main_layout.itemAt(i).itemAt(1).itemAt(3).widget() or \
                    sender == self.main_layout.itemAt(i).itemAt(1).itemAt(4).widget():
                break

        self.main_layout.itemAt(i).itemAt(1).itemAt(2).widget().setDisabled(False)

    def disable_else(self):
        sender = self.sender()

        for i in range(2, self.main_layout.count() - 1):
            if sender == self.main_layout.itemAt(i).itemAt(1).itemAt(1).widget() or \
                    sender == self.main_layout.itemAt(i).itemAt(1).itemAt(2).widget() or \
                    sender == self.main_layout.itemAt(i).itemAt(1).itemAt(3).widget() or \
                    sender == self.main_layout.itemAt(i).itemAt(1).itemAt(4).widget():
                break

        self.main_layout.itemAt(i).itemAt(1).itemAt(1).widget().setText('if')
        self.main_layout.itemAt(i).itemAt(1).itemAt(2).widget().setDisabled(True)

    def stmt_clicked(self):
        sender = self.sender()
        indent = sender.indent

        input_layout = self.add_line(sender.text(), indent + 1)
        count = self.main_layout.count()

        for i in range(2, count - 1):
            if sender == self.main_layout.itemAt(i).itemAt(1).itemAt(1).widget() or \
                    sender == self.main_layout.itemAt(i).itemAt(1).itemAt(2).widget() or \
                    sender == self.main_layout.itemAt(i).itemAt(1).itemAt(3).widget() or \
                    sender == self.main_layout.itemAt(i).itemAt(1).itemAt(4).widget():
                break

        if i == count - 2:
            j = count - 1
        else:
            for j in range(i + 1, count - 1):
                if sender.indent >= self.main_layout.itemAt(j).itemAt(1).itemAt(1).widget().indent:
                    break
                j = count - 1

        input_layout.parent_layout = self.main_layout.itemAt(i)
        self.main_layout.insertLayout(j, input_layout)

    def add_line(self, clicked_button, indent):
        stmt_label = QLabel(clicked_button)
        stmt_label.setMinimumWidth(30)
        stmt_label.setMaximumWidth(30)

        exp_input = QLineEdit()

        hbox1 = QHBoxLayout()
        hbox1.addSpacing(40 * indent)
        hbox1.addWidget(stmt_label)
        hbox1.addWidget(exp_input)

        if_button = QPushButton()
        if_button.setText('if')
        if_button.indent = indent
        if_button.setMinimumWidth(50)
        if_button.setMaximumWidth(50)
        if_button.clicked.connect(self.stmt_clicked)
        if_button.clicked.connect(self.change_if)

        else_button = QPushButton()
        else_button.setText('else')
        else_button.setDisabled(True)
        else_button.indent = indent
        else_button.setMinimumWidth(50)
        else_button.setMaximumWidth(50)
        else_button.clicked.connect(self.stmt_clicked)

        for_button = QPushButton()
        for_button.setText('for')
        for_button.indent = indent
        for_button.setMinimumWidth(50)
        for_button.setMaximumWidth(50)
        for_button.clicked.connect(self.stmt_clicked)

        while_button = QPushButton()
        while_button.setText('while')
        while_button.indent = indent
        while_button.setMinimumWidth(50)
        while_button.setMaximumWidth(50)
        while_button.clicked.connect(self.stmt_clicked)

        hbox2 = QHBoxLayout()
        hbox2.addSpacing(40 * indent + 35)
        hbox2.addWidget(if_button)
        hbox2.addWidget(else_button)
        hbox2.addWidget(for_button)
        hbox2.addWidget(while_button)
        hbox2.addSpacing(600)

        add_layout = QVBoxLayout()
        add_layout.addLayout(hbox1)
        add_layout.addLayout(hbox2)

        return add_layout

    def update_output_dict(self):
        count = self.main_layout.count()
        output_list = list()

        for i in range(2, count - 1):
            if 'parent_layout' in self.main_layout.itemAt(i).__dict__:
                self.main_layout.itemAt(i).tmp_dict = dict(stmt=self.main_layout.itemAt(i).itemAt(0).itemAt(1).widget().text(),
                                                           expression=self.main_layout.itemAt(i).itemAt(0).itemAt(2).widget().text(),
                                                           body=list())
                self.main_layout.itemAt(i).parent_layout.tmp_dict['body'].append(self.main_layout.itemAt(i).tmp_dict)
            else:
                self.main_layout.itemAt(i).tmp_dict = dict(stmt=self.main_layout.itemAt(i).itemAt(0).itemAt(0).widget().text(),
                                                           expression=self.main_layout.itemAt(i).itemAt(0).itemAt(1).widget().text(),
                                                           body=list())
                output_list.append(self.main_layout.itemAt(i).tmp_dict)

        return output_list