import sys

from PyQTInterface.layermap import LayerReader

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSignal, Qt

import traceback

# layer_visible_flag_dict = dict()
# for layer in LayerReader._LayerMapping:
#     layer_visible_flag_dict[layer] = True

class LayerManager(QWidget):
    def __init__(self):
        super(LayerManager, self).__init__()
        self.layer_table_widget = _ManageList(self)
        self.initUI()

    def initUI(self):
        top_layout = QVBoxLayout()
        selection_layout = QHBoxLayout()
        visible_all_button = QPushButton("A-Visible")
        visible_none_button = QPushButton("N-Visible")
        clickable_all_button = QPushButton("A-Clickable")
        clickable_none_button = QPushButton("N-Clickable")
        self.visible_button = QPushButton("NV")
        self.clickable_button = QPushButton("NC")
        # selection_layout.addWidget(visible_all_button)
        # selection_layout.addWidget(visible_none_button)
        # selection_layout.addWidget(clickable_all_button)
        # selection_layout.addWidget(clickable_none_button)
        selection_layout.addWidget(self.visible_button)
        selection_layout.addWidget(self.clickable_button)

        visible_all_button.clicked.connect(self.layer_table_widget.macro_check)
        visible_none_button.clicked.connect(self.layer_table_widget.macro_check)
        clickable_all_button.clicked.connect(self.layer_table_widget.macro_check)
        clickable_none_button.clicked.connect(self.layer_table_widget.macro_check)

        self.visible_button.clicked.connect(self.layer_table_widget.macro_check)
        self.clickable_button.clicked.connect(self.layer_table_widget.macro_check)

        top_layout.addLayout(selection_layout)
        top_layout.addWidget(self.layer_table_widget)
        self.setLayout(top_layout)

    def swapButtonText(self, text):
        if text[-1] == 'V':
            self.visible_button.setText(text)
        elif text[-1] == 'C':
            self.clickable_button.setText(text)


class _ManageList(QTableView):

    send_listInLayer_signal = pyqtSignal(list)
    button_text_signal = pyqtSignal(str)

    def __init__(self, LMaddress):
        super().__init__()
        self.lm = LMaddress
        self._layerList = list()
        self._usedlayer = dict()
        self.visibleGenControl = True
        self.visibleCanControl = True
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

        self.button_text_signal.connect(self.lm.swapButtonText)
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

    def visibleGenState(self, state, genList):
        self.genList = genList
        if state == 2:
            self.visibleGenControl = True
        elif state == 0:
            self.visibleGenControl = False
            pass

    def visibleCanState(self, state, canList):
        self.canList = canList
        if state == 2:
            self.visibleCanControl = True
        elif state == 0:
            self.visibleCanControl = False
            pass

    def itemChanged(self, item):
        try:
            layer = self.model.item(item.index().row()).text()

            if item.checkState() == 0:
                if item.index().column() == 1:
                    self.signal = 'AV'
                elif item.index().column() == 2:
                    self.signal = 'AC'
                self.button_text_signal.emit(self.signal)
            elif item.checkState() == 2:
                if item.index().column() == 1:
                    self.signal = 'NV'
                    for i in range(self.model.rowCount()):
                        if self.model.item(i, 1).checkState() == 0:
                            self.signal = 'AV'
                elif item.index().column() == 2:
                    self.signal = 'NC'
                    for i in range(self.model.rowCount()):
                        if self.model.item(i, 2).checkState() == 0:
                            self.signal = 'AC'
                self.button_text_signal.emit(self.signal)

            if layer not in self._usedlayer:
                return
            Visualitem = self._usedlayer[layer]

            if self.visibleCanControl == False and self.visibleGenControl == False:
                VisualItemForVisible = []
            elif self.visibleCanControl == False:
                VisualItemForVisible = list(set(Visualitem) - set(self.canList))
            elif self.visibleGenControl == False:
                VisualItemForVisible = list(set(Visualitem) - set(self.genList))
            else:
                VisualItemForVisible = Visualitem


            if item.index().column() == 1:
                # if self.visibleGenControl == True and self.visibleCanControl == True:
                if item.checkState() == 0:
                    for x in VisualItemForVisible:
                        try:
                            x.setVisible(False)
                        except:
                            continue
                        # layer_visible_flag_dict[layer] = False

                elif item.checkState() == 2:
                    for x in VisualItemForVisible:
                        try:
                            x.setVisible(True)
                        except:
                            continue
                #         # layer_visible_flag_dict[layer] = True
                # if self.visibleGenControl == False:
                #     VisualitemWithoutGen = list(set(Visualitem) - set(self.genList))
                #     if item.checkState() == 0:
                #         for x in VisualitemWithoutGen:
                #             try:
                #                 x.setVisible(False)
                #             except:
                #                 continue
                #             # layer_visible_flag_dict[layer] = False
                #
                #     elif item.checkState() == 2:
                #         for x in VisualitemWithoutGen:
                #             try:
                #                 x.setVisible(True)
                #             except:
                #                 continue
                #
                # if self.visibleCanControl == False:
                #     VisualitemWithoutCan = list(set(Visualitem) - set(self.canList))
                #     if item.checkState() == 0:
                #         for x in VisualitemWithoutCan:
                #             try:
                #                 x.setVisible(False)
                #             except:
                #                 continue
                #             # layer_visible_flag_dict[layer] = False
                #
                #     elif item.checkState() == 2:
                #         for x in VisualitemWithoutCan:
                #             try:
                #                 x.setVisible(True)
                #             except:
                #                 continue

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

    # def swapButtonText(self, ):


    def macro_check(self):
        # purpose: str, mode: bool
        sender_text = self.sender().text()
        if sender_text[0] == 'A':
            mode = 'on'
        else:
            mode = 'off'

        if sender_text[1] == 'V':
            purpose = 'Visible'
        else:
            purpose = 'Clickable'

        if purpose == 'Visible':
            col = 1
        elif purpose == 'Clickable':
            col = 2

        if mode == 'on':
            state= Qt.Checked
        elif mode == 'off':
            state= Qt.Unchecked

        for row in range(0, self.model.rowCount()):
            self.model.item(row,col).setCheckState(state)

