import sys

from PyQt5.QtWidgets import *

class _ManageList(QListWidget):

    def __init__(self):
        super().__init__()
        self.itemDict = dict()
        self.idDict = dict()

    def updateList(self, _layerList):
        self.layerlist = _layerList
        self.clear()
        for layer in self.layerlist:
            self.addItem(QListWidgetItem(layer).text())