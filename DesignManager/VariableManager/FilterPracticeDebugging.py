import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class _MainWindow(QMainWindow):

    def __init__(self):
        super(_MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        ################# MAIN WINDOW setting ####################
        self.setWindowTitle("FilterPractice")
        # self.move(500,100)
        WIDTH = 800
        LENGTH = 500
        desktop = QApplication.desktop()
        screenWidth = desktop.width()
        screenLength = desktop.height()
        x = (screenWidth - WIDTH)
        y = (screenLength - LENGTH)
        self.move(1180, 670)
        self.resize(WIDTH, LENGTH)
        self.show()

        ###########
        dockWidget1 = QDockWidget()
        dockContentWidget1 = QWidget()

        test = 'test'

        self.moveButton = QPushButton("Move", self)
        self.moveButton.clicked.connect(self.makeFilterWindow)
        self.moveButton.installEventFilter(self)
        self.moveButton.setToolTip(test)

        button = QHBoxLayout()
        button.addWidget(self.moveButton)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(button)

        dockContentWidget1.setLayout(mainLayout)
        dockWidget1.setWidget(dockContentWidget1)
        self.addDockWidget(Qt.TopDockWidgetArea, dockWidget1)

    def makeFilterWindow(self):
        self.fw = _FilterWindow()
        self.fw.show()

    def eventFilter(self, obj, event):
        if obj == self.moveButton and event.type() == QtCore.QEvent.HoverEnter:
            self.onHovered()
        return super(_MainWindow, self).eventFilter(obj, event)

    def onHovered(self):
        print("hovered")


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

        self.lineEditInput = []
        self.lineEditInput.append(QLineEdit())

        self.okButton = QPushButton("OK", self)
        self.okButton.clicked.connect(self.ok_clicked)
        cancelButton = QPushButton("Cancel", self)
        cancelButton.clicked.connect(self.cancel_clicked)

        button = QHBoxLayout()
        button.addStretch(2)
        button.addWidget(self.okButton)
        button.addWidget(cancelButton)

        self.inputBox = QHBoxLayout()

        arrangeWindow = QVBoxLayout()

        self.inputBox.addWidget(labelInput)
        self.inputBox.addWidget(self.lineEditInput[0])

        arrangeWindow.addLayout(self.inputBox)
        arrangeWindow.addWidget(self.model)
        arrangeWindow.addLayout(button)

        self.setLayout(arrangeWindow)

        self.completer = QCompleter(self.fruits)
        self.lineEditInput[0].setCompleter(self.completer)

        self.show()

        self.lineEditInput[0].textChanged.connect(self.filterList)

    def ok_clicked(self):
        if self.lineEditInput[0].text() not in self.fruits:
            print("Invalid Input")
        else:
            print(self.lineEditInput[0].text())
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
            input = len(self.lineEditInput[0].text())
            if self.fruits[x][:input] == self.lineEditInput[0].text():
                self.tmpList.append(self.fruits[x])

        self.showList()

    def _clicked(self, item):
        self.lineEditInput[0].setText(item.text())

    def _doubleClicked(self, item):
        self.lineEditInput[0] = item

        self.ok_clicked()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = _MainWindow()
    sys.exit(app.exec_())