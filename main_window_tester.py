import sys

from PyQTInterface import MainWindow
from PyQt5.QtWidgets import QApplication


def test_main_window(qtbot):
    global window
    window = MainWindow._MainWindow()
    qtbot.addWidget(window)
    window.show()
    qtbot.waitForWindowShown(window)
    assert window.test == 1

def test_boundary_window(qtbot):
    window.widget_delegator.make_boundary_window()
    window.bw.AddBoundaryPointWithMouse([0,0])
    window.bw.clickCount([0,0])
    window.bw.AddBoundaryPointWithMouse([100,100])
    window.bw.clickCount([100,100])
    qtbot.keyClicks(window.bw.name_input,'test')
    window.bw.on_buttonBox_accepted()

    assert window._QTObj._qtProject._DesignParameter['EasyDebugModule']
    assert window._QTObj._qtProject._DesignParameter['EasyDebugModule']['test']
    assert window.visualItemDict['test']
    assert window.visualItemDict['test'] in window.scene.items()

def test_path_window(qtbot):
    window.widget_delegator.makePathWindow()
    window.pw.AddPathPointWithMouse([0,0])
    window.pw.clickCount([0,0])
    window.pw.AddPathPointWithMouse([100,0])
    window.pw.clickCount([100,0])
    window.pw.AddPathPointWithMouse([100,500])
    window.pw.clickCount([100,500])
    qtbot.keyClicks(window.pw.name_input,'test2')
    window.pw.on_buttonBox_accepted()

    assert window._QTObj._qtProject._DesignParameter['EasyDebugModule']['test2']
    assert window.visualItemDict['test2']
    assert window.visualItemDict['test2'] in window.scene.items()

