import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(30,30,600,400)
        self.progress = 0
        self.begin = QPoint()
        self.end = QPoint()
        # print(self.end.x())
        # print(self.end.y())

        self.show()

    def paintEvent(self, event):
        qp = QPainter(self)
        br = QBrush(QColor(100, 10, 10, 40))
        qp.setBrush(br)
        qp.drawRect(QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        print(self.end.x())
        print(self.end.y())
        if self.end.x() == 0 and self.end.y() == 0 and self.progress == 0:
            self.begin = event.pos()
            self.end = event.pos()
            self.setMouseTracking(True)
        elif self.progress == 1:
            self.begin = event.pos()
            self.end = event.pos()
            self.setMouseTracking(True)
            self.progress = 0
        else:
            self.end = event.pos()
            self.setMouseTracking(False)
            self.progress = 1
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    app.aboutToQuit.connect(app.deleteLater)
    sys.exit(app.exec_())