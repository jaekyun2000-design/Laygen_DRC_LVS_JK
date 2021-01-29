import sys

from PyQTInterface.layermap import LayerReader

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# class _ManageList(QListWidget):
#
#     def __init__(self):
#         super().__init__()
#
#     def updateList(self, _layerList):
#         self.layerlist = _layerList
#         self.clear()
#         for layer in self.layerlist:
#             item = QListWidgetItem()
#             self.addItem(item)
#             checkBox1 = QCheckBox(layer)
#             self.setItemWidget(item, checkBox1)

# class _ManageList(QTableWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         # model = QStandardItemModel()
#         # model.setHeaderData(0,Qt.Horizontal,"Constraint Container(Floating)")
#         # model.setHeaderData(1,Qt.Horizontal,"Constraint ID")
#         # model.setHeaderData(2,Qt.Horizontal,"Constraint Type")
#         # model.setHeaderData(3,Qt.Horizontal,"Value")
#         #
#         # self.setModel(model)
#         # model = QStandardItemModel()
#         # model.setHorizontalHeaderLabels(['    Layer    ','Visible','Clickable'])
#         #
#         # self.setModel(model)
#         # self.resizeColumnsToContents()
#         self.clear()
#
#         self.setColumnCount(3)
#         self.setRowCount(20)
#
#         self.setHorizontalHeaderLabels(['    Layer    ','Visible','Clickable'])
#         self.verticalHeader().setVisible(False)
#         self.resizeColumnsToContents()
#
#
#     def updateList(self, _layerList):
#         self.layerlist = _layerList
#
#         for layer in self.layerlist:
#             self.insertRow(1)
#             item = QTableWidgetItem(layer)
#             self.setItem(1,1,item)

class _ManageList(QTableView):

    def __init__(self):
        super().__init__()
        self._Row = 0
        self._layerList = list()
        self._visibleList = list()
        self._clickableList = list()
        self._usedlayer = list()
        self.initUI()

    def initUI(self):
        # model = QStandardItemModel()
        # model.setHeaderData(0,Qt.Horizontal,"Constraint Container(Floating)")
        # model.setHeaderData(1,Qt.Horizontal,"Constraint ID")
        # model.setHeaderData(2,Qt.Horizontal,"Constraint Type")
        # model.setHeaderData(3,Qt.Horizontal,"Value")
        #
        # self.setModel(model)

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['    Layer    ','Visible','Clickable'])
        self.verticalHeader().setVisible(False)

        _Layer = LayerReader._LayerMapping

        for layer in _Layer:
            layervisible = layer+'_V'
            layerclickable = layer+'_C'

            self._layerList.append(layer)
            self._visibleList.append(layervisible)
            self._clickableList.append(layerclickable)

            item = QStandardItem(layer)

            itemv = QStandardItem(layervisible)
            itemv.setCheckable(True)
            itemv.setText('')

            itemc = QStandardItem(layerclickable)
            itemc.setCheckable(True)
            itemc.setText('')

            model.appendRow(item)
            model.setItem(self._Row,1,itemv)
            model.setItem(self._Row,2,itemc)
            self._Row += 1

        # print(self._layerList)
        # print(self._visibleList)
        # print(self._clickableList)

        self.setModel(model)
        self.resizeColumnsToContents()


    def updateList(self, _layerList):
        self._usedlayer = _layerList
        print(self._usedlayer)