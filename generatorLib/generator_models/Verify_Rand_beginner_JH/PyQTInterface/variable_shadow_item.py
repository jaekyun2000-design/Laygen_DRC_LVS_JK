from PyQt5.QtWidgets import*
from PyQt5.QtGui import QColor,QPen,QBrush,QTransform
from PyQt5.QtCore import Qt




class VariableBlock(QGraphicsRectItem):
    def __init__(self,_BlockTraits=None):
        super().__init__()
        # self.setFlag(QGraphicsItem.ItemIsSelectable,False)
        if _BlockTraits is None:
            self._BlockTraits = dict(
                variable_type = None,
                variable_name=None,
                xycoordinates = None,
                width = None,
                height = None,
            )

        else:
            self._BlockTraits = _BlockTraits
            self.updateRect()

    def updateTraits(self,_BlockTraits):
        for key in _BlockTraits.keys():
            self._BlockTraits[key] = _BlockTraits[key]
        self.updateRect()



    def updateRect(self):
        if self._BlockTraits["_XYCoordinates"] is None:
            self._BlockTraits["_XYCoordinates"] = [[0,0]]

        if type(self._BlockTraits['_Width']) == str:
            if not self._BlockTraits["_Width"]:
                print("ERROR: Unvalid Width")
                return None
            self._BlockTraits['_Width'] = int(self._BlockTraits['_Width'])

        if type(self._BlockTraits['_Height']) == str:
            if not self._BlockTraits["_Height"]:
                print("ERROR: Unvalid Height")
                return None
            self._BlockTraits['_Height'] = int(self._BlockTraits['_Height'])


        self.setRect(0,
                     0,
                     self._BlockTraits["_Width"],
                     self._BlockTraits["_Height"] )


    def paint(self, painter, option, widget=None):
        self._BlockTraits["_Color"].setAlphaF(1)

        pen = QPen()
        pen.setColor(self._BlockTraits["_Outline"])
        brush = QBrush()
        brush.setColor(self._BlockTraits["_Color"])

        # print(self.zValue())

        if self.isSelected():
            # self._BlockTraits["_Color"].setAlphaF(1)
            # self.setZValue(self.zValue()*10000)
            # print("HighLighted",self.zValue())
            pen.setStyle(Qt.DashLine)
            pen.setColor(self._BlockTraits["_Outline"])
            pen.setWidth(3)
            self.setZValue(1)
        else:
            self.setZValue(self._BlockTraits['_Layer']/1000)



        brush.setStyle(Qt.NoBrush)
        brush.setStyle(Qt.SolidPattern)

        #
        # if not (self._BlockTraits["_Pattern"] == "blank" or self._BlockTraits["_Pattern"] == "stipple0" or self._BlockTraits["_Pattern"] == "dagger" or self._BlockTraits["_Pattern"] == "brick"):
        #     brush.setStyle(Qt.SolidPattern)

        brush.setTransform(QTransform(painter.worldTransform().inverted()[0]))
        # print("zValue : ", self.zValue())
        painter.setPen(pen)
        painter.setBrush(brush)

        painter.drawRect(self.rect())


