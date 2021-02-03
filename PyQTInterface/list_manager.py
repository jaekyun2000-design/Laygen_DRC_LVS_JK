import sys

from PyQTInterface.layermap import LayerReader

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

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

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['    Layer    ','Visible','Clickable'])
        self.verticalHeader().setVisible(False)

        _Layer = LayerReader._LayerMapping

        for layer in _Layer:
            layervisible = layer+'_V'
            layerclickable = layer+'_C'

            self._layerList.append(layer)
            self._visibleList.append(layervisible)
            self._clickableList.append(layerclickable)

            item = QStandardItem(layer)
            item.setEditable(False)

            itemv = QStandardItem(layervisible)
            itemv.setCheckable(True)
            itemv.setCheckState(2)
            itemv.setEditable(False)
            itemv.setText('')

            itemc = QStandardItem(layerclickable)
            itemc.setCheckable(True)
            itemc.setCheckState(2)
            itemc.setEditable(False)
            itemc.setText('')

            self.model.appendRow(item)
            self.model.setItem(self._Row,1,itemv)
            self.model.setItem(self._Row,2,itemc)
            self._Row += 1

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
