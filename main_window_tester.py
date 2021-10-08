import sys

from PyQTInterface import MainWindow
from PyQt5.QtWidgets import QApplication

# window = MainWindow._MainWindow()
window=None
def test_main_window(qtbot):
    global window
    window = MainWindow._MainWindow() if not window else window
    # qtbot.addWidget(window)
    window.show()
    qtbot.waitForWindowShown(window)
    assert window.test == 1

def test_boundary_window(qtbot):
    # qtbot.addWidget(window)
    global window
    window = MainWindow._MainWindow() if not window else window
    window.widget_delegator.make_boundary_window()
    qtbot.waitForWindowShown(window.bw)
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
    # qtbot.addWidget(window)
    global window
    window = MainWindow._MainWindow() if not window else window
    window.widget_delegator.makePathWindow()
    # qtbot.waitForWindowShown(window.pw)
    qtbot.keyClicks(window.pw.width_input, '100')
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

def test_sref_window(qtbot):
    global window
    window = MainWindow._MainWindow() if not window else window

    window.widget_delegator.loadSRefWindow()
    qtbot.waitForWindowShown(window.ls)
    qtbot.keyClicks(window.ls.name_input, 'sref_test')
    qtbot.keyClicks(window.ls.XY_input, '1000,1000')
    qtbot.keyClicks(window.ls.library_input, 'NMOSWithDummy')
    for idx, par_name in enumerate(window.ls.par_name):
        if 'Number' in par_name:
            window.ls.par_valueForLineEdit[idx].clear()
            qtbot.keyClicks(window.ls.par_valueForLineEdit[idx], '5')
        elif 'Width' in par_name:
            window.ls.par_valueForLineEdit[idx].clear()
            qtbot.keyClicks(window.ls.par_valueForLineEdit[idx], '500')
        elif 'length' in par_name:
            window.ls.par_valueForLineEdit[idx].clear()
            qtbot.keyClicks(window.ls.par_valueForLineEdit[idx], '30')
        elif '_XVT' in par_name:
            window.ls.par_valueForLineEdit[idx].clear()
            qtbot.keyClicks(window.ls.par_valueForLineEdit[idx], '"NVT"')
    window.ls.on_buttonBox_accepted()

    assert window._QTObj._qtProject._DesignParameter['EasyDebugModule']['sref_test']
    assert window.visualItemDict['sref_test']
    assert window.visualItemDict['sref_test'] in window.scene.items()


