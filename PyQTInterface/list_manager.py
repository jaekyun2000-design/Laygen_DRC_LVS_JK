import sys

from PyQTInterface.layermap import LayerReader

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class _ManageList(QTableView):

    def __init__(self):
        super().__init__()
        self._layerList = list()
        self._usedlayer = list()
        self.initUI()

    def initUI(self):

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['    Layer    ','Visible','Clickable'])
        self.verticalHeader().setVisible(False)
        self.setShowGrid(False)

        _Layer = LayerReader._LayerMapping

        for layer in _Layer:
            self._layerList.append(layer)

            item = QStandardItem(layer)
            item.setEditable(False)

            itemv = QStandardItem(layer)
            itemv.setCheckable(True)
            itemv.setCheckState(2)
            itemv.setEditable(False)
            itemv.setText('')

            itemc = QStandardItem(layer)
            itemc.setCheckable(True)
            itemc.setCheckState(2)
            itemc.setEditable(False)
            itemc.setText('')

            self.model.appendRow(item)
            self.model.setItem(self.model.rowCount()-1,1,itemv)
            self.model.setItem(self.model.rowCount()-1,2,itemc)

        self.setModel(self.model)
        self.resizeColumnsToContents()

        self.model.itemChanged.connect(self.itemChanged)

    def updateList(self, _layerList):
        self._usedlayer = _layerList

    def itemChanged(self, item):
        try:
            layer = self.model.item(item.index().row()).text()
            Visualitem = self._usedlayer[layer]

            if item.index().column() == 1:
                if item.checkState() == 0:
                    for x in Visualitem:
                        x.setVisible(False)

                elif item.checkState() == 2:
                    for x in Visualitem:
                        x.setVisible(True)

            elif item.index().column() == 2:
                if item.checkState() == 0:
                    for x in Visualitem:
                        x.setFlag(QGraphicsItem.ItemIsSelectable, False)

                elif item.checkState() == 2:
                    for x in Visualitem:
                        x.setFlag(QGraphicsItem.ItemIsSelectable, True)
        except:
            pass
