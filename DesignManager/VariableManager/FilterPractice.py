import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class _FilterWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.fruits = ["banana", "apple", "melon", "pear", "orange", "peach"]
        self.tmpList = self.fruits

        self.model = QListWidget()
        for f in self.tmpList:
            self.model.addItem(f)
        self.model.itemClicked.connect(self._clicked)
        self.model.itemDoubleClicked.connect(self._doubleClicked)

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Filter')

        labelInput = QLabel('Input :')

        self.lineEditInput = QLineEdit()

        okButton = QPushButton("OK", self)
        okButton.clicked.connect(self.ok_clicked)
        cancelButton = QPushButton("Cancel", self)
        cancelButton.clicked.connect(self.cancel_clicked)

        button = QHBoxLayout()
        button.addStretch(2)
        button.addWidget(okButton)
        button.addWidget(cancelButton)

        self.inputBox = QHBoxLayout()

        arrangeWindow = QVBoxLayout()

        self.inputBox.addWidget(labelInput)
        self.inputBox.addWidget(self.lineEditInput)

        arrangeWindow.addLayout(self.inputBox)
        arrangeWindow.addWidget(self.model)
        arrangeWindow.addLayout(button)

        self.setLayout(arrangeWindow)

        self.completer = QCompleter(self.fruits)
        self.lineEditInput.setCompleter(self.completer)

        self.show()

        self.lineEditInput.textChanged.connect(self.filterList)

    def ok_clicked(self):
        if self.lineEditInput.text() not in self.fruits:
            print("Invalid Input")
        else:
            print(self.lineEditInput.text())
            self.destroy()

    def cancel_clicked(self):
        self.destroy()

    def showList(self):
        if self.model:
            self.model.clear()

        for f in self.tmpList:
            self.model.addItem(f)

    def filterList(self):
        self.tmpList = []
        for x in range(len(self.fruits)):
            input = len(self.lineEditInput.text())
            if self.fruits[x][:input] == self.lineEditInput.text():
                self.tmpList.append(self.fruits[x])

        self.showList()

    def _clicked(self, item):
        self.lineEditInput = item

    def _doubleClicked(self, item):
        self.lineEditInput = item

        self.ok_clicked()