from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from PyQTInterface import calculator
import warnings
import re
import copy
# import numpy as np
import os
from generatorLib import drc_api


class ConditionExpressionWidget(QWidget):
    send_output_dict_signal = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        and_button = QPushButton()
        and_button.setText('and')
        and_button.clicked.connect(self.and_or_clicked)

        or_button = QPushButton()
        or_button.setText('or')
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

        self.input_widget = ConditionExpressionWidgetCapsule()
        input_layout = self.input_widget.new_line()

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(input_layout)
        self.main_layout.addLayout(self.button_layout)
        self.setLayout(self.main_layout)

    def and_or_clicked(self, _):
        sender = self.sender()

        input_layout = self.input_widget.add_line(sender.text())

        self.main_layout.removeItem(self.button_layout)
        self.main_layout.addLayout(input_layout)
        self.main_layout.addLayout(self.button_layout)
        self.setLayout(self.main_layout)

    def set_for_expression(self):
        self.input_widget.main_layout.itemAt(0).itemAt(0).itemAt(1).itemAt(1).widget().setDisabled(True)

        self.input_widget.main_layout.itemAt(0).itemAt(1).itemAt(1).widget().setCurrentText('in')
        self.input_widget.main_layout.itemAt(0).itemAt(1).itemAt(1).widget().setDisabled(True)

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


class ConditionExpressionWidgetCapsule(QWidget):
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
        var_cal = QPushButton()
        var_cal.setIcon(QIcon(QPixmap('./image/cal.png')))
        var_cal.clicked.connect(self.cal_clicked)
        var_h_layout = QHBoxLayout()
        var_h_layout.addWidget(var_input)
        var_h_layout.addWidget(var_cal)
        var_v_layout = QVBoxLayout()
        var_v_layout.addWidget(var_label)
        var_v_layout.addLayout(var_h_layout)

        operator_label = QLabel('operator')
        operator_input = QComboBox()
        operator_input.addItems(self.operator)
        operator_input.currentTextChanged.connect(self.operator_changed)
        operator_input.currentTextChanged.connect(self.update_output_dict)
        operator_layout = QVBoxLayout()
        operator_layout.addWidget(operator_label)
        operator_layout.addWidget(operator_input)

        cond_label = QLabel('condition')
        cond_input = QLineEdit()
        cond_input.textChanged.connect(self.update_output_dict)
        cond_cal = QPushButton()
        cond_cal.setIcon(QIcon(QPixmap('./image/cal.png')))
        cond_cal.clicked.connect(self.cal_clicked)
        cond_h_layout = QHBoxLayout()
        cond_h_layout.addWidget(cond_input)
        cond_h_layout.addWidget(cond_cal)
        cond_v_layout = QVBoxLayout()
        cond_v_layout.addWidget(cond_label)
        cond_v_layout.addLayout(cond_h_layout)

        input_layout = QHBoxLayout()
        input_layout.addLayout(var_v_layout)
        input_layout.addLayout(operator_layout)
        input_layout.addLayout(cond_v_layout)

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

        var_input = QLineEdit()
        var_input.textChanged.connect(self.update_output_dict)
        var_cal = QPushButton()
        var_cal.setIcon(QIcon(QPixmap('./image/cal.png')))
        var_cal.clicked.connect(self.cal_clicked)
        var_h_layout = QHBoxLayout()
        var_h_layout.addWidget(var_input)
        var_h_layout.addWidget(var_cal)
        var_v_layout = QVBoxLayout()
        var_v_layout.addWidget(_label)
        var_v_layout.addLayout(var_h_layout)

        and_or_label = QLabel(and_or)
        operator_input = QComboBox()
        operator_input.addItems(self.operator)
        operator_input.currentTextChanged.connect(self.operator_changed)
        operator_input.currentTextChanged.connect(self.update_output_dict)
        operator_layout = QVBoxLayout()
        operator_layout.addWidget(and_or_label)
        operator_layout.addWidget(operator_input)

        cond_input = QLineEdit()
        cond_input.textChanged.connect(self.update_output_dict)
        cond_cal = QPushButton()
        cond_cal.setIcon(QIcon(QPixmap('./image/cal.png')))
        cond_cal.clicked.connect(self.cal_clicked)
        cond_h_layout = QHBoxLayout()
        cond_h_layout.addWidget(cond_input)
        cond_h_layout.addWidget(cond_cal)
        cond_v_layout = QVBoxLayout()
        cond_v_layout.addWidget(_label)
        cond_v_layout.addLayout(cond_h_layout)

        input_layout = QHBoxLayout()
        input_layout.addLayout(var_v_layout)
        input_layout.addLayout(operator_layout)
        input_layout.addLayout(cond_v_layout)

        self.main_layout.addLayout(input_layout)

        return self.main_layout

    def operator_changed(self, _):
        sender = self.sender()

        for i in range(len(self.output_dict_list)):
            op = self.main_layout.itemAt(i).itemAt(1).itemAt(1).widget()
            if sender == op:
                break

        if sender.currentText() == 'None':
            self.main_layout.itemAt(i).itemAt(2).itemAt(1).itemAt(0).widget().setStyleSheet(
                "QLineEdit{background:rgb(222,222,222);}")
            self.main_layout.itemAt(i).itemAt(2).itemAt(1).itemAt(0).widget().setReadOnly(True)
            self.main_layout.itemAt(i).itemAt(2).itemAt(1).itemAt(1).widget().setDisabled(True)
        else:
            self.main_layout.itemAt(i).itemAt(2).itemAt(1).itemAt(0).widget().setStyleSheet(
                "QLineEdit{background:rgb(255,255,255);}")
            self.main_layout.itemAt(i).itemAt(2).itemAt(1).itemAt(0).widget().setReadOnly(False)
            self.main_layout.itemAt(i).itemAt(2).itemAt(1).itemAt(1).widget().setDisabled(False)

    def update_output_dict(self, _):
        for i in range(len(self.output_dict_list)):
            var = self.main_layout.itemAt(i).itemAt(0).itemAt(1).itemAt(0).widget().text()
            op = self.main_layout.itemAt(i).itemAt(1).itemAt(1).widget().currentText()
            cond = self.main_layout.itemAt(i).itemAt(2).itemAt(1).itemAt(0).widget().text()
            self.output_dict_list[i]['variable'] = var
            self.output_dict_list[i]['operator'] = op
            self.output_dict_list[i]['condition'] = cond

    def cal_clicked(self):
        sender = self.sender()

        for i in range(len(self.output_dict_list)):
            if sender == self.main_layout.itemAt(i).itemAt(0).itemAt(1).itemAt(1).widget():
                tmp = 'var'
                break
            if sender == self.main_layout.itemAt(i).itemAt(2).itemAt(1).itemAt(1).widget():
                tmp = 'cond'
                break

        self.sender_list = [i, tmp]

        self.cal = calculator.ExpressionCalculator(clipboard=QGuiApplication.clipboard(),purpose='')
        self.cal.send_expression_signal.connect(self.exported_text)
        self.cal.send_dummyconstraints_signal.connect(self.cal.storePreset)
        self.cal.set_preset_window()
        self.cal.show()

    def exported_text(self, str1, str2, dict1):
        if dict1['X']:
            if self.sender_list[1] == 'var':
                self.main_layout.itemAt(self.sender_list[0]).itemAt(0).itemAt(1).itemAt(0).widget().setText(str(dict1['X']))
            elif self.sender_list[1] == 'cond':
                self.main_layout.itemAt(self.sender_list[0]).itemAt(2).itemAt(1).itemAt(0).widget().setText(str(dict1['X']))
        elif dict1['Y']:
            if self.sender_list[1] == 'var':
                self.main_layout.itemAt(self.sender_list[0]).itemAt(0).itemAt(1).itemAt(0).widget().setText(str(dict1['Y']))
            elif self.sender_list[1] == 'cond':
                self.main_layout.itemAt(self.sender_list[0]).itemAt(2).itemAt(1).itemAt(0).widget().setText(str(dict1['Y']))


class ConditionStmtWidget(QWidget):
    send_output_list_signal = pyqtSignal(list)
    send_ast_id_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.input_widget = ConditionStmtWidgetCapsule()
        self.input_widget.adjust_size_signal.connect(self.adjustSize)

        if_button = QPushButton()
        if_button.setText('if')
        if_button.setMinimumWidth(50)
        if_button.setMaximumWidth(50)
        if_button.clicked.connect(self.c_type_clicked)
        if_button.clicked.connect(self.change_if)

        elif_button = QPushButton()
        elif_button.setText('elif')
        elif_button.setDisabled(True)
        elif_button.setMinimumWidth(50)
        elif_button.setMaximumWidth(50)
        elif_button.clicked.connect(self.c_type_clicked)

        else_button = QPushButton()
        else_button.setText('else')
        else_button.setDisabled(True)
        else_button.setMinimumWidth(50)
        else_button.setMaximumWidth(50)
        else_button.clicked.connect(self.c_type_clicked)
        else_button.clicked.connect(self.disable_else)

        for_button = QPushButton()
        for_button.setText('for')
        for_button.setMinimumWidth(50)
        for_button.setMaximumWidth(50)
        for_button.clicked.connect(self.c_type_clicked)
        for_button.clicked.connect(self.disable_else)

        while_button = QPushButton()
        while_button.setText('while')
        while_button.setMinimumWidth(50)
        while_button.setMaximumWidth(50)
        while_button.clicked.connect(self.c_type_clicked)
        while_button.clicked.connect(self.disable_else)

        ok_button = QPushButton()
        ok_button.setText('OK')
        ok_button.clicked.connect(self.ok_clicked)

        cancel_button = QPushButton()
        cancel_button.setText('cancel')
        cancel_button.clicked.connect(self.cancel_clicked)

        option_layout = QHBoxLayout()
        option_layout.addWidget(if_button)
        option_layout.addWidget(elif_button)
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
        self.main_layout.itemAt(0).itemAt(1).widget().setDisabled(False)
        self.main_layout.itemAt(0).itemAt(2).widget().setDisabled(False)

    def disable_else(self):
        self.main_layout.itemAt(0).itemAt(1).widget().setDisabled(True)
        self.main_layout.itemAt(0).itemAt(2).widget().setDisabled(True)

    def c_type_clicked(self):
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


class ConditionStmtWidgetCapsule(QWidget):
    adjust_size_signal = pyqtSignal()
    for_exp_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

    def new_line(self, clicked_button):
        c_type_label = QLabel(clicked_button)
        c_type_label.setMinimumWidth(30)
        c_type_label.setMaximumWidth(30)

        exp_input = QLineEdit()
        exp_input.setPlaceholderText('expression')

        comment_input = QLineEdit()
        comment_input.setPlaceholderText('comment')
        comment_input.setMinimumWidth(90)
        comment_input.setMaximumWidth(90)

        exp_button = QPushButton()
        exp_button.setText('create')
        exp_button.setMinimumWidth(70)
        exp_button.setMaximumWidth(70)
        exp_button.clicked.connect(self.show_create_widget)

        hbox1 = QHBoxLayout()
        hbox1.addSpacing(0)
        hbox1.addWidget(c_type_label)
        if clicked_button == 'else':
            hbox1.addSpacing(500)
            hbox1.addWidget(comment_input)
            hbox1.addSpacing(76)
        else:
            hbox1.addWidget(exp_input)
            hbox1.addWidget(comment_input)
            hbox1.addWidget(exp_button)

        if_button = QPushButton()
        if_button.setText('if')
        if_button.indent = 0
        if_button.setMinimumWidth(50)
        if_button.setMaximumWidth(50)
        if_button.clicked.connect(self.c_type_clicked)
        if_button.clicked.connect(self.change_if)

        elif_button = QPushButton()
        elif_button.setText('elif')
        elif_button.setDisabled(True)
        elif_button.indent = 0
        elif_button.setMinimumWidth(50)
        elif_button.setMaximumWidth(50)
        elif_button.clicked.connect(self.c_type_clicked)

        else_button = QPushButton()
        else_button.setText('else')
        else_button.setDisabled(True)
        else_button.indent = 0
        else_button.setMinimumWidth(50)
        else_button.setMaximumWidth(50)
        else_button.clicked.connect(self.c_type_clicked)
        else_button.clicked.connect(self.disable_else)

        for_button = QPushButton()
        for_button.setText('for')
        for_button.indent = 0
        for_button.setMinimumWidth(50)
        for_button.setMaximumWidth(50)
        for_button.clicked.connect(self.c_type_clicked)
        for_button.clicked.connect(self.disable_else)

        while_button = QPushButton()
        while_button.setText('while')
        while_button.indent = 0
        while_button.setMinimumWidth(50)
        while_button.setMaximumWidth(50)
        while_button.clicked.connect(self.c_type_clicked)
        while_button.clicked.connect(self.disable_else)

        delete_button = QPushButton()
        delete_button.setText('delete')
        delete_button.setMinimumWidth(70)
        delete_button.setMaximumWidth(70)
        delete_button.clicked.connect(self.delete_line)

        hbox2 = QHBoxLayout()
        hbox2.addSpacing(35)
        hbox2.addWidget(if_button)
        hbox2.addWidget(elif_button)
        hbox2.addWidget(else_button)
        hbox2.addWidget(for_button)
        hbox2.addWidget(while_button)
        hbox2.addSpacing(600)
        hbox2.addWidget(delete_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(hbox1)
        main_layout.addLayout(hbox2)

        return main_layout

    def change_if(self):
        sender = self.sender()

        for i in range(2, self.main_layout.count() - 1):
            if sender == self.main_layout.itemAt(i).itemAt(1).itemAt(1).widget() or \
                    sender == self.main_layout.itemAt(i).itemAt(1).itemAt(2).widget() or \
                    sender == self.main_layout.itemAt(i).itemAt(1).itemAt(3).widget() or \
                    sender == self.main_layout.itemAt(i).itemAt(1).itemAt(4).widget() or \
                    sender == self.main_layout.itemAt(i).itemAt(1).itemAt(5).widget():
                break

        self.main_layout.itemAt(i).itemAt(1).itemAt(2).widget().setDisabled(False)
        self.main_layout.itemAt(i).itemAt(1).itemAt(3).widget().setDisabled(False)

    def disable_else(self):
        sender = self.sender()

        for i in range(2, self.main_layout.count() - 1):
            if sender == self.main_layout.itemAt(i).itemAt(1).itemAt(1).widget() or \
                    sender == self.main_layout.itemAt(i).itemAt(1).itemAt(2).widget() or \
                    sender == self.main_layout.itemAt(i).itemAt(1).itemAt(3).widget() or \
                    sender == self.main_layout.itemAt(i).itemAt(1).itemAt(4).widget() or \
                    sender == self.main_layout.itemAt(i).itemAt(1).itemAt(5).widget():
                break

        self.main_layout.itemAt(i).itemAt(1).itemAt(2).widget().setDisabled(True)
        self.main_layout.itemAt(i).itemAt(1).itemAt(3).widget().setDisabled(True)

    def c_type_clicked(self):
        sender = self.sender()
        indent = sender.indent

        input_layout = self.add_line(sender.text(), indent + 1)
        count = self.main_layout.count()

        for i in range(2, count - 1):
            if sender == self.main_layout.itemAt(i).itemAt(1).itemAt(1).widget() or \
                    sender == self.main_layout.itemAt(i).itemAt(1).itemAt(2).widget() or \
                    sender == self.main_layout.itemAt(i).itemAt(1).itemAt(3).widget() or \
                    sender == self.main_layout.itemAt(i).itemAt(1).itemAt(4).widget() or \
                    sender == self.main_layout.itemAt(i).itemAt(1).itemAt(5).widget():
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
        c_type_label = QLabel(clicked_button)
        c_type_label.setMinimumWidth(30)
        c_type_label.setMaximumWidth(30)

        exp_input = QLineEdit()
        exp_input.setPlaceholderText('expression')

        comment_input = QLineEdit()
        comment_input.setPlaceholderText('comment')
        comment_input.setMinimumWidth(90)
        comment_input.setMaximumWidth(90)

        exp_button = QPushButton()
        exp_button.setText('create')
        exp_button.setMinimumWidth(70)
        exp_button.setMaximumWidth(70)
        exp_button.clicked.connect(self.show_create_widget)

        hbox1 = QHBoxLayout()
        hbox1.addSpacing(40 * indent)
        hbox1.addWidget(c_type_label)
        if clicked_button == 'else':
            hbox1.addSpacing(500)
            hbox1.addWidget(comment_input)
            hbox1.addSpacing(81)
        else:
            hbox1.addWidget(exp_input)
            hbox1.addWidget(comment_input)
            hbox1.addWidget(exp_button)

        if_button = QPushButton()
        if_button.setText('if')
        if_button.indent = indent
        if_button.setMinimumWidth(50)
        if_button.setMaximumWidth(50)
        if_button.clicked.connect(self.c_type_clicked)
        if_button.clicked.connect(self.change_if)

        elif_button = QPushButton()
        elif_button.setText('elif')
        elif_button.setDisabled(True)
        elif_button.indent = indent
        elif_button.setMinimumWidth(50)
        elif_button.setMaximumWidth(50)
        elif_button.clicked.connect(self.c_type_clicked)

        else_button = QPushButton()
        else_button.setText('else')
        else_button.setDisabled(True)
        else_button.indent = indent
        else_button.setMinimumWidth(50)
        else_button.setMaximumWidth(50)
        else_button.clicked.connect(self.c_type_clicked)

        for_button = QPushButton()
        for_button.setText('for')
        for_button.indent = indent
        for_button.setMinimumWidth(50)
        for_button.setMaximumWidth(50)
        for_button.clicked.connect(self.c_type_clicked)

        while_button = QPushButton()
        while_button.setText('while')
        while_button.indent = indent
        while_button.setMinimumWidth(50)
        while_button.setMaximumWidth(50)
        while_button.clicked.connect(self.c_type_clicked)

        delete_button = QPushButton()
        delete_button.setText('delete')
        delete_button.setMinimumWidth(70)
        delete_button.setMaximumWidth(70)
        delete_button.clicked.connect(self.delete_line)

        hbox2 = QHBoxLayout()
        hbox2.addSpacing(40 * indent + 35)
        hbox2.addWidget(if_button)
        hbox2.addWidget(elif_button)
        hbox2.addWidget(else_button)
        hbox2.addWidget(for_button)
        hbox2.addWidget(while_button)
        hbox2.addSpacing(600)
        hbox2.addWidget(delete_button)

        add_layout = QVBoxLayout()
        add_layout.addLayout(hbox1)
        add_layout.addLayout(hbox2)

        return add_layout

    def delete_line(self):
        sender = self.sender()
        count = self.main_layout.count()

        for i in range(2, count - 1):
            if sender == self.main_layout.itemAt(i).itemAt(1).itemAt(7).widget():
                tmp_layout = self.main_layout.takeAt(i)
                for _ in range(tmp_layout.itemAt(0).count()):
                    tmp_widget_item = tmp_layout.itemAt(0).takeAt(0)
                    if tmp_widget_item is not None:
                        tmp_widget = tmp_widget_item.widget()
                        if tmp_widget is not None:
                            tmp_widget.setParent(None)
                        del tmp_widget
                for _ in range(tmp_layout.itemAt(1).count()):
                    tmp_widget_item = tmp_layout.itemAt(1).takeAt(0)
                    if tmp_widget_item is not None:
                        tmp_widget = tmp_widget_item.widget()
                        if tmp_widget is not None:
                            tmp_widget.setParent(None)
                        del tmp_widget
                break

        for _ in range(i, count - 2):
            if 'parent_layout' in self.main_layout.itemAt(i).__dict__:
                if self.main_layout.itemAt(i).parent_layout == tmp_layout:
                    self.delete_child_line(self.main_layout.takeAt(i))
                if self.main_layout.itemAt(i).itemAt(0).itemAt(1).widget().text() == 'else':
                    self.delete_child_line(self.main_layout.takeAt(i))
                    break
            else:
                if self.main_layout.itemAt(i).itemAt(0).itemAt(1).widget().text() == 'else':
                    self.delete_child_line(self.main_layout.takeAt(i))
                    break

        count = self.main_layout.count()

        if i != count - 1:
            if self.main_layout.itemAt(i).itemAt(0).itemAt(1).widget().text() == 'elif':
                self.main_layout.itemAt(i).itemAt(0).itemAt(1).widget().setText('if')

        for j in range(2, i):
            if 'parent_layout' in self.main_layout.itemAt(i+1-j).__dict__:
                if 'parent_layout' in tmp_layout.__dict__:
                    if self.main_layout.itemAt(i+1-j).parent_layout == tmp_layout.parent_layout:
                        if self.main_layout.itemAt(i+1-j).itemAt(0).itemAt(1).widget().text() == 'if' or \
                                self.main_layout.itemAt(i+1-j).itemAt(0).itemAt(1).widget().text() == 'elif':
                            self.main_layout.itemAt(i+1-j).parent_layout.itemAt(1).itemAt(2).widget().setDisabled(False)
                            self.main_layout.itemAt(i+1-j).parent_layout.itemAt(1).itemAt(3).widget().setDisabled(False)
                else:
                    if 'parent_layout' not in self.main_layout.itemAt(i+1-j).__dict__:
                        if self.main_layout.itemAt(i+1-j).itemAt(0).itemAt(1).widget().text() == 'if' or \
                                self.main_layout.itemAt(i+1-j).itemAt(0).itemAt(1).widget().text() == 'elif':
                            self.main_layout.itemAt(0).itemAt(1).widget().setDisabled(False)
                            self.main_layout.itemAt(0).itemAt(2).widget().setDisabled(False)
                        else:
                            break
            else:
                if 'parent_layout' in tmp_layout.__dict__:
                    break
                else:
                    if j == i - 1:
                        if self.main_layout.itemAt(j).itemAt(0).itemAt(1).widget().text() == 'if' or \
                                self.main_layout.itemAt(j).itemAt(0).itemAt(1).widget().text() == 'elif':
                            self.main_layout.itemAt(0).itemAt(1).widget().setDisabled(False)
                            self.main_layout.itemAt(0).itemAt(2).widget().setDisabled(False)

        del tmp_layout
        self.adjust_size_signal.emit()

    def delete_child_line(self, delete_layout):
            tmp_layout = delete_layout
            for _ in range(tmp_layout.itemAt(0).count()):
                tmp_widget_item = tmp_layout.itemAt(0).takeAt(0)
                if tmp_widget_item is not None:
                    tmp_widget = tmp_widget_item.widget()
                    if tmp_widget is not None:
                        tmp_widget.setParent(None)
                    del tmp_widget
            for _ in range(tmp_layout.itemAt(1).count()):
                tmp_widget_item = tmp_layout.itemAt(1).takeAt(0)
                if tmp_widget_item is not None:
                    tmp_widget = tmp_widget_item.widget()
                    if tmp_widget is not None:
                        tmp_widget.setParent(None)
                    del tmp_widget
            del tmp_layout

    def update_output_dict(self):
        count = self.main_layout.count()
        output_list = list()

        for i in range(2, count - 1):
            if 'parent_layout' in self.main_layout.itemAt(i).__dict__:
                self.main_layout.itemAt(i).tmp_dict = dict(c_type=self.main_layout.itemAt(i).itemAt(0).itemAt(1).widget().text(),
                                                           expression=self.main_layout.itemAt(i).itemAt(0).itemAt(2).widget().text(),
                                                           body=list())
                self.main_layout.itemAt(i).parent_layout.tmp_dict['body'].append(self.main_layout.itemAt(i).tmp_dict)
            else:
                self.main_layout.itemAt(i).tmp_dict = dict(c_type=self.main_layout.itemAt(i).itemAt(0).itemAt(1).widget().text(),
                                                           expression=self.main_layout.itemAt(i).itemAt(0).itemAt(2).widget().text(),
                                                           body=list())
                output_list.append(self.main_layout.itemAt(i).tmp_dict)

        return output_list

    def show_create_widget(self):
        sender = self.sender()
        count = self.main_layout.count()
        
        self.create_widget = ConditionExpressionWidget()

        for i in range(2, count - 1):
            if sender == self.main_layout.itemAt(i).itemAt(0).itemAt(4).widget():
                self.idx = i
                break

        if self.main_layout.itemAt(i).itemAt(0).itemAt(1).widget().text() == 'for':
            self.for_exp_signal.connect(self.create_widget.set_for_expression)
            self.for_exp_signal.emit()

        self.create_widget.send_output_dict_signal.connect(self.get_stmt)
        self.create_widget.show()

    def get_stmt(self, output_dict):
        if type(output_dict['variable']) == dict:
            output_dict['variable'] = '(' + self.get_stmt(output_dict['variable']) + ')'
            output_dict['condition'] = '(' + output_dict['condition']['variable'] + ' ' +\
                                       output_dict['condition']['operator'] + ' ' +\
                                       output_dict['condition']['condition'] + ')'
            output_text = output_dict['variable'] + ' ' + output_dict['operator'] + ' ' + output_dict['condition']
            print(self.main_layout.itemAt(self.idx).itemAt(0).itemAt(1).widget())
            self.main_layout.itemAt(self.idx).itemAt(0).itemAt(2).widget().setText(output_text)
            return output_text
        else:
            output_text = output_dict['variable'] + ' ' + output_dict['operator'] + ' ' + output_dict['condition']
            print(self.main_layout.itemAt(self.idx).itemAt(0).itemAt(1).widget())
            self.main_layout.itemAt(self.idx).itemAt(0).itemAt(2).widget().setText(output_text)
            return output_text