import sys

from PyQTInterface.layermap import LayerReader

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSignal

import traceback

# layer_visible_flag_dict = dict()
# for layer in LayerReader._LayerMapping:
#     layer_visible_flag_dict[layer] = True

class _ManageList(QTableView):

    send_listInLayer_signal = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self._layerList = list()
        self._usedlayer = dict()
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

    def updateLayerList(self, _layerDict):
        self._usedlayer = _layerDict
        # for layer in _layerDict:
        #     item = _layerDict[layer]
        #     if layer in self._usedlayer:
        #         if self._usedlayer[layer].count(item) == 0:
        #             self._usedlayer[layer].extend(item)
        #     else:
        #         self._usedlayer[layer] = item


    def itemChanged(self, item):
        try:
            layer = self.model.item(item.index().row()).text()
            Visualitem = self._usedlayer[layer]

            if item.index().column() == 1:
                if item.checkState() == 0:
                    for x in Visualitem:
                        try:
                            x.setVisible(False)
                        except:
                            continue
                        # layer_visible_flag_dict[layer] = False

                elif item.checkState() == 2:
                    for x in Visualitem:
                        try:
                            x.setVisible(True)
                        except:
                            continue
                        # layer_visible_flag_dict[layer] = True

            elif item.index().column() == 2:
                if item.checkState() == 0:
                    for x in Visualitem:
                        try:
                            x.setFlag(QGraphicsItem.ItemIsSelectable, False)
                        except:
                            continue
                    self.send_listInLayer_signal.emit(Visualitem)


                elif item.checkState() == 2:
                    for x in Visualitem:
                        try:
                            x.setFlag(QGraphicsItem.ItemIsSelectable, True)
                        except:
                            continue
        except:
            traceback.print_exc()
