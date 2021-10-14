import sys, os

from PyQTInterface import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from PyQt5 import QtWidgets
import user_setup

# window = MainWindow._MainWindow()
window=None

class HiddenConsole:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')
    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

def test_main_window(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window
    window.show()
    qtbot.waitForWindowShown(window)
    # assert window.test == 1
    assert window.test == True
    window.reset()

##################################test for dp creation##################################
def test_boundary_window(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window
    window.show()
    window.widget_delegator.make_boundary_window()
    qtbot.waitForWindowShown(window.bw)
    window.bw.AddBoundaryPointWithMouse([0,0])
    window.bw.clickCount([0,0])
    window.bw.AddBoundaryPointWithMouse([100,100])
    window.bw.clickCount([100,100])
    qtbot.keyClicks(window.bw.name_input,'boundary_test')
    window.bw.on_buttonBox_accepted()

    assert window._QTObj._qtProject._DesignParameter['EasyDebugModule']
    assert window._QTObj._qtProject._DesignParameter['EasyDebugModule']['boundary_test']
    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('boundary_test')
    assert window._QTObj._qtProject._DesignConstraint['EasyDebugModule'][dc_id]
    assert window.visualItemDict['boundary_test']
    assert window.visualItemDict['boundary_test'] in window.scene.items()
    window.reset()


def test_path_window(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window
    window.show()
    window.widget_delegator.makePathWindow()
    qtbot.waitForWindowShown(window.pw)
    qtbot.keyClicks(window.pw.width_input, '100')
    window.pw.AddPathPointWithMouse([0,0])
    window.pw.clickCount([0,0])
    window.pw.AddPathPointWithMouse([100,0])
    window.pw.clickCount([100,0])
    window.pw.AddPathPointWithMouse([100,500])
    window.pw.clickCount([100,500])

    qtbot.keyClicks(window.pw.name_input,'path_test')
    window.pw.on_buttonBox_accepted()

    assert window._QTObj._qtProject._DesignParameter['EasyDebugModule']['path_test']
    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('path_test')
    assert window._QTObj._qtProject._DesignConstraint['EasyDebugModule'][dc_id]
    assert window.visualItemDict['path_test']
    assert window.visualItemDict['path_test'] in window.scene.items()
    window.reset()


def test_sref_window(qtbot):
    global window
    with HiddenConsole():
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
    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('sref_test')
    assert window._QTObj._qtProject._DesignConstraint['EasyDebugModule'][dc_id]
    assert window.visualItemDict['sref_test']
    assert window.visualItemDict['sref_test'] in window.scene.items()
    window.reset()


def test_text_window(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window
    window.widget_delegator.makeTextWindow()
    qtbot.waitForWindowShown(window.txtw)
    # qtbot.addWidget(window.txtw)
    qtbot.keyClicks(window.txtw.name_input, 'text_test')
    qtbot.keyClicks(window.txtw.text_input, 'TEST TEXT WINDOW')
    qtbot.keyClicks(window.txtw.width_input, '100')
    # qtbot.keyClicks(window.txtw.XY_input, "0,0")
    window.txtw.DetermineCoordinateWithMouse([0,0])
    window.txtw.on_buttonBox_accepted()

    assert window._QTObj._qtProject._DesignParameter['EasyDebugModule']['text_test']
    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('text_test')
    assert window._QTObj._qtProject._DesignConstraint['EasyDebugModule'][dc_id]
    assert window.visualItemDict['text_test']
    assert window.visualItemDict['text_test'] in window.scene.items()
    window.reset()


def test_pin_window(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window
    window.widget_delegator.makePinWindow()
    qtbot.waitForWindowShown(window.pinw)
    # qtbot.addWidget(window.pinw)
    qtbot.keyClicks(window.pinw.name_input, 'pin_test')
    qtbot.keyClicks(window.pinw.layer_input, 'METAL1PIN')
    qtbot.keyClicks(window.pinw.text_input, 'METAL1PIN_test')
    qtbot.keyClicks(window.pinw.width_input, '100')
    window.pinw.DetermineCoordinateWithMouse([0, 0])
    window.pinw.on_buttonBox_accepted()
    # qtbot.keyClicks(window.pinw.XY_input, '0,0')

    assert window._QTObj._qtProject._DesignParameter['EasyDebugModule']['pin_test']
    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('pin_test')
    assert window._QTObj._qtProject._DesignConstraint['EasyDebugModule'][dc_id]
    assert window.visualItemDict['pin_test']
    assert window.visualItemDict['pin_test'] in window.scene.items()
    window.reset()


##################################test for dp edit##################################
def test_boundary_edit_window(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window
    window.widget_delegator.make_boundary_window()
    qtbot.waitForWindowShown(window.bw)
    window.bw.AddBoundaryPointWithMouse([0,0])
    window.bw.clickCount([0,0])
    window.bw.AddBoundaryPointWithMouse([100,100])
    window.bw.clickCount([100,100])
    qtbot.keyClicks(window.bw.name_input,'boundary_edit_test')
    window.bw.on_buttonBox_accepted()

    # send vs items to selected design item list widget
    window.dockContentWidget2.UpdateCustomItem([window.visualItemDict['boundary_edit_test']])
    target_item = window.dockContentWidget2.findItems('boundary_edit_test', QtCore.Qt.MatchFlag.MatchExactly)[0]
    assert target_item

    window.dockContentWidget2.ModifyingDesign(target_item)
    assert window.dockContentWidget2.bw

    #change design value
    boundary_widget = window.dockContentWidget2.bw
    boundary_widget.name_input.clear()
    qtbot.keyClicks(boundary_widget.name_input, 'boundary_name_change')
    idx = boundary_widget.layer_input.findText('METAL1')
    boundary_widget.layer_input.setCurrentIndex(idx)
    boundary_widget.on_buttonBox_accepted()

    assert window._QTObj._qtProject._DesignParameter['EasyDebugModule']['boundary_name_change']
    assert 'boundary_edit_test' not in window._QTObj._qtProject._DesignParameter['EasyDebugModule']
    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('boundary_name_change')
    assert window._QTObj._qtProject._DesignConstraint['EasyDebugModule'][dc_id]
    assert window.visualItemDict['boundary_name_change']
    assert window.visualItemDict['boundary_name_change'] in window.scene.items()
    assert window._QTObj._qtProject._DesignParameter['EasyDebugModule']['boundary_name_change']._DesignParameter['_LayerUnifiedName'] == 'METAL1'
    window.reset()

def test_path_edit_window(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window
    window.widget_delegator.makePathWindow()
    qtbot.waitForWindowShown(window.pw)
    qtbot.keyClicks(window.pw.width_input, '100')
    window.pw.AddPathPointWithMouse([0,0])
    window.pw.clickCount([0,0])
    window.pw.AddPathPointWithMouse([100,0])
    window.pw.clickCount([100,0])
    window.pw.AddPathPointWithMouse([100,500])
    window.pw.clickCount([100,500])

    qtbot.keyClicks(window.pw.name_input,'path_edit_test')
    window.pw.on_buttonBox_accepted()

    # send vs items to selected design item list widget
    window.dockContentWidget2.UpdateCustomItem([window.visualItemDict['path_edit_test']])
    target_item = window.dockContentWidget2.findItems('path_edit_test', QtCore.Qt.MatchFlag.MatchExactly)[0]
    assert target_item

    window.dockContentWidget2.ModifyingDesign(target_item)
    assert window.dockContentWidget2.pw

    # change design value
    path_widget = window.dockContentWidget2.pw
    path_widget.name_input.clear()
    qtbot.keyClicks(path_widget.name_input, 'path_name_change')
    idx = path_widget.layer_input.findText('METAL3')
    path_widget.layer_input.setCurrentIndex(idx)
    path_widget.on_buttonBox_accepted()

    assert window._QTObj._qtProject._DesignParameter['EasyDebugModule']['path_name_change']
    assert 'path_edit_test' not in window._QTObj._qtProject._DesignParameter['EasyDebugModule']
    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('path_name_change')
    assert window._QTObj._qtProject._DesignConstraint['EasyDebugModule'][dc_id]
    assert window.visualItemDict['path_name_change']
    assert window.visualItemDict['path_name_change'] in window.scene.items()
    assert window._QTObj._qtProject._DesignParameter['EasyDebugModule']['path_name_change']._DesignParameter[
               '_LayerUnifiedName'] == 'METAL3'
    window.reset()

def test_sref_edit_window(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window
    window.widget_delegator.loadSRefWindow()
    qtbot.waitForWindowShown(window.ls)
    qtbot.keyClicks(window.ls.name_input, 'sref_edit_test')
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

    # send vs items to selected design item list widget
    window.dockContentWidget2.UpdateCustomItem([window.visualItemDict['sref_edit_test']])
    target_item = window.dockContentWidget2.findItems('sref_edit_test', QtCore.Qt.MatchFlag.MatchExactly)[0]
    assert target_item

    window.dockContentWidget2.ModifyingDesign(target_item)
    assert window.dockContentWidget2.sw

    # change design value
    sref_widget = window.dockContentWidget2.sw
    sref_widget.name_input.clear()
    qtbot.keyClicks(sref_widget.name_input, 'sref_name_change')
    qtbot.keyClicks(sref_widget.library_input, 'PbodyContact')
    for idx, par_name in enumerate(sref_widget.par_name):
        if 'COX' in par_name:
            sref_widget.par_valueForLineEdit[idx].clear()
            qtbot.keyClicks(sref_widget.par_valueForLineEdit[idx], '10')
        elif 'COY' in par_name:
            sref_widget.par_valueForLineEdit[idx].clear()
            qtbot.keyClicks(sref_widget.par_valueForLineEdit[idx], '2')
    sref_widget.on_buttonBox_accepted()

    assert window._QTObj._qtProject._DesignParameter['EasyDebugModule']['sref_name_change']
    assert 'path_edit_test' not in window._QTObj._qtProject._DesignParameter['EasyDebugModule']
    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('sref_name_change')
    assert window._QTObj._qtProject._DesignConstraint['EasyDebugModule'][dc_id]
    assert window._QTObj._qtProject._DesignConstraint['EasyDebugModule'][dc_id]._ast
    assert window._QTObj._qtProject._DesignConstraint['EasyDebugModule'][dc_id]._ast.library == 'PbodyContact'
    assert window.visualItemDict['sref_name_change']
    assert window.visualItemDict['sref_name_change'] in window.scene.items()
    window.reset()


##################################test for dc creation##################################
def test_create_pycode(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window

    window.widget_delegator.makePyCodeWindow()
    qtbot.waitForWindowShown(window.cw)
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(1).widget(), 'pycode_test')
    window.cw.on_buttonBox_accepted()
    window.reset()

def test_create_ast(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window

    window.widget_delegator.makeConstraintWindowAST()
    qtbot.waitForWindowShown(window.cw)
    qtbot.keyClicks(window.cw.type_input, 'Assign')
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(1).widget(), 'targets')
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(2).widget(), 'values')
    window.cw.on_buttonBox_accepted()
    window.reset()

def test_create_element(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window
    window.widget_delegator.makeConstraintWindowCUSTOM()
    qtbot.waitForWindowShown(window.cw)
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(1).widget(), 'test_boundary')
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(2).widget(), 'PIMP')
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(3).widget(), '0,0')
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(4).widget(), '100')
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(5).widget(), '200')
    window.cw.on_buttonBox_accepted()
    assert window._QTObj._qtProject._DesignParameter['EasyDebugModule']['test_boundary']
    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('test_boundary')
    assert window._QTObj._qtProject._DesignConstraint['EasyDebugModule'][dc_id]
    assert window.visualItemDict['test_boundary']
    assert window.visualItemDict['test_boundary'] in window.scene.items()
    window.reset()

def test_create_XYCalculator(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window
    window.calculator()
    qtbot.waitForWindowShown(window.calculator_window)

    test_create_element(qtbot)
    window.calculator_window.display.setText("center('test_boundary[0]') + rt('test_boundary[0]') *"
                                             " width('test_boundary[0]') / bottom('test_boundary[0]') + 2")
    window.calculator_window.equationList = ["center('test_boundary[0]') + rt('test_boundary[0]') * " \
                                            "width('test_boundary[0]') / bottom('test_boundary[0]') + 2"]
    window.calculator_window.xy_button.setChecked(True)

    window.calculator_window.add_clicked()
    window.calculator_window.y_button.setChecked(True)
    window.calculator_window.display.setText("center('test_boundary[0]') + rb('test_boundary[0]') *"
                                             " height('test_boundary[0]') / bottom('test_boundary[0]') + 2")
    window.calculator_window.equationList = ["center('test_boundary[0]') + rb('test_boundary[0]') * " \
                                        "height('test_boundary[0]') / bottom('test_boundary[0]') + 2"]
    window.calculator_window.add_clicked()
    window.calculator_window.export_clicked()
    window.reset()
    # qtbot.stop()

def test_create_conditionexp(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_create_conditionstmt(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_add_constraint_view_from_dp(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_add_constraint_view_from_dc(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_assign_variable(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window

##################################test for dc execution##################################
def test_encode_constraint(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window

def test_run_constraint_boundary(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_run_constraint_path(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_run_constraint_sref(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_run_constraint_with_variable(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_run_constraint_for_update(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_run_constraint_from_project(qtbot):
    '''
    pre_defined project load and run...
    '''
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_run_constraint_multi_constraint_view(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


##################################test for dp-dc pairing##################################
def test_paring_after_dp_creation(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window
    window.show()
    window.widget_delegator.make_boundary_window()
    qtbot.waitForWindowShown(window.bw)
    window.bw.AddBoundaryPointWithMouse([0,0])
    window.bw.clickCount([0,0])
    window.bw.AddBoundaryPointWithMouse([100,100])
    window.bw.clickCount([100,100])
    qtbot.keyClicks(window.bw.name_input,'pairing_test')
    window.bw.on_buttonBox_accepted()

    ## dp에서 찾아서 H키 누르기
    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('pairing_test')
    assert window._QTObj._qtProject._ElementManager.get_dp_id_by_dc_id(dc_id) == 'pairing_test'
    window.visualItemDict['pairing_test'].setSelected(True)
    qtbot.keyClicks(window.centralWidget(), 'H')
    idx = window.dockContentWidget3_2.currentIndex()
    assert dc_id == window.dockContentWidget3_2.model.itemFromIndex(idx).text()

    ## dc에서 찾아서 H키 누르기
    for item_key in list(window.visualItemDict.keys()):
        window.visualItemDict[item_key].setSelected(False)
    qtbot.keyClicks(window.dockContentWidget3_2, 'H')
    for item_key in list(window.visualItemDict.keys()):
        if window.visualItemDict[item_key].isSelected():
            dp_id = item_key
    assert window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id(dp_id) == dc_id
    window.reset()

def test_paring_after_dc_creation(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window
    window.show()
    window.widget_delegator.makeConstraintWindowCUSTOM()
    qtbot.waitForWindowShown(window.cw)
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(1).widget(),'pairing_test')
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(2).widget(),'PIMP')
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(3).widget(),'0,0')
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(4).widget(),'100')
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(5).widget(),'100')
    window.cw.on_buttonBox_accepted()

    ## dp에서 찾아서 H키 누르기
    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('pairing_test')
    assert window._QTObj._qtProject._ElementManager.get_dp_id_by_dc_id(dc_id) == 'pairing_test'
    window.visualItemDict['pairing_test'].setSelected(True)
    qtbot.keyClicks(window.centralWidget(), 'H')
    idx = window.dockContentWidget3_2.currentIndex()
    assert dc_id == window.dockContentWidget3_2.model.itemFromIndex(idx).text()

    ## dc에서 찾아서 H키 누르기
    for item_key in list(window.visualItemDict.keys()):
        window.visualItemDict[item_key].setSelected(False)
    qtbot.keyClicks(window.dockContentWidget3_2, 'H')
    for item_key in list(window.visualItemDict.keys()):
        if window.visualItemDict[item_key].isSelected():
            dp_id = item_key
    assert window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id(dp_id) == dc_id
    window.reset()

def test_paring_after_project_load(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window
    window.show()
    ### Create boundary ###
    window.widget_delegator.make_boundary_window()
    qtbot.waitForWindowShown(window.bw)
    window.bw.AddBoundaryPointWithMouse([0,0])
    window.bw.clickCount([0,0])
    window.bw.AddBoundaryPointWithMouse([100,100])
    window.bw.clickCount([100,100])
    qtbot.keyClicks(window.bw.name_input,'pairing_test')
    window.bw.on_buttonBox_accepted()

    ### Project save ###
    file_name = './PyQTInterface/Project/pairing_test'
    window.saveProject(file_name)

    ### New module ###
    window.show_module_window()
    qtbot.keyClicks(window.nmw.name_input, 'proj_pairing_test')
    window.nmw.on_makeBox_accepted()

    ### Project load ###
    file_name = './PyQTInterface/Project/pairing_test.bin'
    window.module_dict['proj_pairing_test'].loadProject(file_name)

    ## dp에서 찾아서 H키 누르기
    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('pairing_test')
    assert window._QTObj._qtProject._ElementManager.get_dp_id_by_dc_id(dc_id) == 'pairing_test'
    window.visualItemDict['pairing_test'].setSelected(True)
    qtbot.keyClicks(window.centralWidget(), 'H')
    idx = window.dockContentWidget3_2.currentIndex()
    assert dc_id == window.dockContentWidget3_2.model.itemFromIndex(idx).text()

    ## dc에서 찾아서 H키 누르기
    for item_key in list(window.visualItemDict.keys()):
        window.visualItemDict[item_key].setSelected(False)
    qtbot.keyClicks(window.dockContentWidget3_2, 'H')
    for item_key in list(window.visualItemDict.keys()):
        if window.visualItemDict[item_key].isSelected():
            dp_id = item_key
    assert window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id(dp_id) == dc_id
    window.reset()

def test_paring_after_gds_load(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window
    window.show()
    ### GDS load ###
    import user_setup
    if user_setup._Technology != 'SS28nm':
        window.request_change_process(None, 'SS28nm')
    user_setup.MULTI_THREAD = False
    file_name = './PyQTInterface/GDSFile/RX_term_resistor_v2.gds'
    window.loadGDS(test=file_name)

    ## dp에서 찾아서 H키 누르기
    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('METAL2_path_6')
    assert window._QTObj._qtProject._ElementManager.get_dp_id_by_dc_id(dc_id) == 'METAL2_path_6'
    window.visualItemDict['METAL2_path_6'].setSelected(True)
    qtbot.keyClicks(window.centralWidget(), 'H')
    idx = window.dockContentWidget3_2.currentIndex()
    assert dc_id == window.dockContentWidget3_2.model.itemFromIndex(idx).text()

    ## dc에서 찾아서 H키 누르기
    for item_key in list(window.visualItemDict.keys()):
        window.visualItemDict[item_key].setSelected(False)
    qtbot.keyClicks(window.dockContentWidget3_2, 'H')
    for item_key in list(window.visualItemDict.keys()):
        if window.visualItemDict[item_key].isSelected():
            dp_id = item_key
    assert window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id(dp_id) == dc_id
    window.reset()

def test_paring_after_create_submodule(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window
    window.show()
    ### Load GDS ###
    import user_setup
    if user_setup._Technology != 'TSMC65nm':
        window.request_change_process(None, 'TSMC65nm')
    user_setup.MULTI_THREAD = False
    file_name = './PyQTInterface/GDSFile/INV2.gds'
    window.loadGDS(test=file_name)
    vs_dict = window.visualItemDict['NMOSInINV_0']
    vs_dict.setSelected(True)

    ### Create submodule ###
    window.create_submodule_by_sref(test=True)
    window = window.module_dict['NMOSInINV_0']

    ## dp에서 찾아서 H키 누르기
    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('POLY_boundary_9')
    assert window._QTObj._qtProject._ElementManager.get_dp_id_by_dc_id(dc_id) == 'POLY_boundary_9'
    window.visualItemDict['POLY_boundary_9'].setSelected(True)
    qtbot.keyClicks(window.centralWidget(), 'H')
    idx = window.dockContentWidget3_2.currentIndex()
    assert dc_id == window.dockContentWidget3_2.model.itemFromIndex(idx).text()

    ## dc에서 찾아서 H키 누르기
    for item_key in list(window.visualItemDict.keys()):
        window.visualItemDict[item_key].setSelected(False)
    qtbot.keyClicks(window.dockContentWidget3_2, 'H')
    for item_key in list(window.visualItemDict.keys()):
        if window.visualItemDict[item_key].isSelected():
            dp_id = item_key
    assert window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id(dp_id) == dc_id
    window.reset()

def test_paring_after_convert_sref_assign(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window
    window.show()
    ### Load GDS ###
    import user_setup
    if user_setup._Technology != 'TSMC65nm':
        window.request_change_process(None, 'TSMC65nm')
    user_setup.MULTI_THREAD = False
    file_name = './PyQTInterface/GDSFile/INV2.gds'
    window.loadGDS(test=file_name)
    vs_dict = window.visualItemDict['NMOSInINV_0']
    vs_dict.setSelected(True)

    ### Assign to sref ###
    window.widget_delegator.convert_elements_to_sref_widget([vs_dict])
    qtbot.waitForWindowShown(window.widget_delegator.choice_widget)
    qtbot.mouseClick(window.widget_delegator.choice_widget.layout().itemAt(0).widget(), QtCore.Qt.LeftButton)
    qtbot.waitForWindowShown(window.widget_delegator.ls)
    qtbot.keyClicks(window.widget_delegator.ls.name_input, 'assign_pairing_test')
    qtbot.keyClicks(window.widget_delegator.ls.library_input, 'NMOSWithDummy')
    qtbot.keyClicks(window.widget_delegator.ls.XY_input, '0,0')
    for idx, par_name in enumerate(window.widget_delegator.ls.par_name):
        if 'Number' in par_name:
            window.widget_delegator.ls.par_valueForLineEdit[idx].clear()
            qtbot.keyClicks(window.widget_delegator.ls.par_valueForLineEdit[idx], '5')
        elif 'Width' in par_name:
            window.widget_delegator.ls.par_valueForLineEdit[idx].clear()
            qtbot.keyClicks(window.widget_delegator.ls.par_valueForLineEdit[idx], '500')
        elif 'length' in par_name:
            window.widget_delegator.ls.par_valueForLineEdit[idx].clear()
            qtbot.keyClicks(window.widget_delegator.ls.par_valueForLineEdit[idx], '30')
        elif '_XVT' in par_name:
            window.widget_delegator.ls.par_valueForLineEdit[idx].clear()
            qtbot.keyClicks(window.widget_delegator.ls.par_valueForLineEdit[idx], '"NVT"')
    window.widget_delegator.ls.on_buttonBox_accepted()

    ## dp에서 찾아서 H키 누르기
    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('assign_pairing_test')
    assert window._QTObj._qtProject._ElementManager.get_dp_id_by_dc_id(dc_id) == 'assign_pairing_test'
    window.visualItemDict['assign_pairing_test'].setSelected(True)
    qtbot.keyClicks(window.centralWidget(), 'H')
    idx = window.dockContentWidget3_2.currentIndex()
    assert dc_id == window.dockContentWidget3_2.model.itemFromIndex(idx).text()

    ## dc에서 찾아서 H키 누르기
    for item_key in list(window.visualItemDict.keys()):
        window.visualItemDict[item_key].setSelected(False)
    qtbot.keyClicks(window.dockContentWidget3_2, 'H')
    for item_key in list(window.visualItemDict.keys()):
        if window.visualItemDict[item_key].isSelected():
            dp_id = item_key
    assert window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id(dp_id) == dc_id
    window.reset()

def test_paring_after_convert_create_assign(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window
    window.show()
    ### Load GDS ###
    import user_setup
    if user_setup._Technology != 'TSMC65nm':
        window.request_change_process(None, 'TSMC65nm')
    user_setup.MULTI_THREAD = False
    file_name = './PyQTInterface/GDSFile/INV2.gds'
    window.loadGDS(test=file_name)
    vs_dict = window.visualItemDict['NMOSInINV_0']
    vs_dict.setSelected(True)

    ### Create sref ###
    window.widget_delegator.create_sref([vs_dict])
    qtbot.waitForWindowShown(window.widget_delegator.get_module_name_widget)
    qtbot.keyClicks(window.widget_delegator.module_name, 'create_pairing_test')
    qtbot.mouseClick(window.widget_delegator.get_module_name_widget.layout().itemAt(1).itemAt(1).widget(), QtCore.Qt.LeftButton)
    window = window.module_dict['create_pairing_test']

    ## dp에서 찾아서 H키 누르기
    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('NMOSInINV_0')
    assert window._QTObj._qtProject._ElementManager.get_dp_id_by_dc_id(dc_id) == 'NMOSInINV_0'
    window.visualItemDict['NMOSInINV_0'].setSelected(True)
    qtbot.keyClicks(window.centralWidget(), 'H')
    idx = window.dockContentWidget3_2.currentIndex()
    assert dc_id == window.dockContentWidget3_2.model.itemFromIndex(idx).text()

    ## dc에서 찾아서 H키 누르기
    for item_key in list(window.visualItemDict.keys()):
        window.visualItemDict[item_key].setSelected(False)
    qtbot.keyClicks(window.dockContentWidget3_2, 'H')
    for item_key in list(window.visualItemDict.keys()):
        if window.visualItemDict[item_key].isSelected():
            dp_id = item_key
    assert window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id(dp_id) == dc_id
    window.reset()

##################################test for scene_visible##################################
def test_visible(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window
    window.show()
    ### Create METAL1 boundary ###
    window.widget_delegator.make_boundary_window()
    qtbot.waitForWindowShown(window.bw)
    window.bw.AddBoundaryPointWithMouse([0,0])
    window.bw.clickCount([0,0])
    window.bw.AddBoundaryPointWithMouse([100,100])
    window.bw.clickCount([100,100])
    qtbot.keyClicks(window.bw.layer_input,'METAL1')
    qtbot.keyClicks(window.bw.name_input,'visible_test')
    window.bw.on_buttonBox_accepted()

    ### Set all non-visible ###
    qtbot.mouseClick(window.dockContentWidget1_2.visible_button, QtCore.Qt.LeftButton)

    ### Assertion ###
    assert not window.visualItemDict['visible_test'].isVisible()

    ### Set all visible ###
    qtbot.mouseClick(window.dockContentWidget1_2.visible_button, QtCore.Qt.LeftButton)

    ### Assertion ###
    assert window.visualItemDict['visible_test'].isVisible()
    window.reset()


def test_clickable(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window
    window.show()

    ### Create METAL1 boundary ###
    window.widget_delegator.make_boundary_window()
    qtbot.waitForWindowShown(window.bw)
    window.bw.AddBoundaryPointWithMouse([0,0])
    window.bw.clickCount([0,0])
    window.bw.AddBoundaryPointWithMouse([100,100])
    window.bw.clickCount([100,100])
    qtbot.keyClicks(window.bw.layer_input,'METAL1')
    qtbot.keyClicks(window.bw.name_input,'clickable_test')
    window.bw.on_buttonBox_accepted()

    ### Set all non-clickable ###
    qtbot.mouseClick(window.dockContentWidget1_2.clickable_button, QtCore.Qt.LeftButton)

    ### Assertion ###\
    print(window.visualItemDict['clickable_test'].ItemIsSelectable)
    # assert not window.visualItemDict['clickable_test'].ItemIsSelectable

    ### Set all clickable ###
    qtbot.mouseClick(window.dockContentWidget1_2.clickable_button, QtCore.Qt.LeftButton)

    ### Assertion ###
    print(window.visualItemDict['clickable_test'].ItemIsSelectable)
    # assert window.visualItemDict['clickable_test'].ItemIsSelectable

    window.reset()

def test_used_layer(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_generator_show_hide(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_candidate_show_hide(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


##################################test for project##################################
def test_project_save(qtbot):
    global window
    with HiddenConsole():
        if window:
            window.close()
        window = MainWindow._MainWindow()
        # qtbot.addWidget(window)
        qtbot.waitForWindowShown(window)
    #create boundary
    window.widget_delegator.make_boundary_window()
    qtbot.waitForWindowShown(window.bw)
    window.bw.AddBoundaryPointWithMouse([0, 0])
    window.bw.clickCount([0, 0])
    window.bw.AddBoundaryPointWithMouse([100, 100])
    window.bw.clickCount([100, 100])
    qtbot.keyClicks(window.bw.name_input, 'boundary_test')
    window.bw.on_buttonBox_accepted()

    #create path
    window.widget_delegator.makePathWindow()
    qtbot.waitForWindowShown(window.pw)
    qtbot.keyClicks(window.pw.width_input, '100')
    window.pw.AddPathPointWithMouse([0, 0])
    window.pw.clickCount([0, 0])
    window.pw.AddPathPointWithMouse([100, 0])
    window.pw.clickCount([100, 0])
    window.pw.AddPathPointWithMouse([100, 500])
    window.pw.clickCount([100, 500])
    qtbot.keyClicks(window.pw.name_input, 'path_test')
    window.pw.on_buttonBox_accepted()

    #create sref
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


    file_name = './PyQTInterface/Project/test_project'
    window.saveProject(file_name)
    assert window.test
    window.reset()


def test_project_load(qtbot):
    global window
    with HiddenConsole():
        if window:
            window.close()
        window = MainWindow._MainWindow()
    #     qtbot.addWidget(window)
    #     qtbot.waitForWindowShown(window)
    file_name = './PyQTInterface/Project/test_project.bin'
    window.loadProject(file_name)
    assert window.test
    window.reset()


def test_load_gds(qtbot):
    global window
    with HiddenConsole():
        if window:
            window.close()
        window = MainWindow._MainWindow()
        # qtbot.addWidget(window)
        # qtbot.waitForWindowShown(window)
    import user_setup
    if user_setup._Technology != 'SS28nm':
        window.request_change_process(None, 'SS28nm')
    user_setup.MULTI_THREAD = False
    file_name = './PyQTInterface/GDSFile/RX_term_resistor_v2.gds'
    window.loadGDS(test=file_name)
    assert len(window._QTObj._qtProject._DesignParameter['RX_term_resistor_v2']) == 118
    assert len(window._QTObj._qtProject._DesignConstraint['RX_term_resistor_v2']) == 118
    assert len(window.scene.items()) == 2640
    # window.reset()


##################################test for scene_right_click##################################
def test_elements_array_boundary_relative(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_elements_array_boundary_offset(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_elements_array_path_relative(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_elements_array_path_offset(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_elements_array_sref_relative(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_elements_array_sref_offset(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_elements_convert_assign(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_elements_convert_create(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


##################################test for multimodule##################################

def test_module_create(qtbot):
    global window
    with HiddenConsole():
        if not window:
            window = MainWindow._MainWindow()
    window.reset()
    window.show_module_window()
    qtbot.keyClicks(window.nmw.name_input, 'test_module')
    window.nmw.on_makeBox_accepted()

    assert 'test_module' in window.module_name_list
    assert 'test_module' in window.module_dict

    new_window = window.module_dict['test_module']
    assert 'test_module' in new_window.module_name_list
    assert 'test_module' in new_window.module_dict
    window.reset()

def test_module_shift(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window
    window.reset()
    window.show_module_window()
    qtbot.keyClicks(window.nmw.name_input, 'test_module')
    window.nmw.on_makeBox_accepted()
    new_window = window.module_dict['test_module']

    assert 'EasyDebugModule' in new_window.module_dict
    new_window.moduleManage()
    assert new_window.mw.manageListWidget.findItems('EasyDebugModule', QtCore.Qt.MatchFlag.MatchExactly)
    item = new_window.mw.manageListWidget.findItems('EasyDebugModule', QtCore.Qt.MatchFlag.MatchExactly)[0]
    new_window.mw.manageListWidget.setCurrentItem(item)
    new_window.mw.on_selectBox_accepted()
    assert not new_window.isVisible()
    assert window.isVisible()
    assert window._CurrentModuleName == 'EasyDebugModule'

    window.moduleManage()
    assert window.mw.manageListWidget.findItems('test_module', QtCore.Qt.MatchFlag.MatchExactly)
    item = window.mw.manageListWidget.findItems('test_module', QtCore.Qt.MatchFlag.MatchExactly)[0]
    window.mw.manageListWidget.setCurrentItem(item)
    window.mw.on_selectBox_accepted()
    assert new_window.isVisible()
    assert not window.isVisible()
    assert new_window._CurrentModuleName == 'test_module'
    window.reset()

def test_module_run(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


##################################test for calculator##################################
def test_calculator_xy_coord(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_calculator_expression(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_calculator_index(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_calculator_drc(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_calculator_number(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_calculator_preset_load(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_calculator_path_xy(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


##################################test for automation##################################
def test_inspect_array(qtbot):
    global window
    with HiddenConsole():
        if window:
            window.reset()
        window = MainWindow._MainWindow()
    if user_setup._Technology != 'TSMC65nm':
        window.request_change_process(None, 'TSMC65nm')
    user_setup.MULTI_THREAD = True
    file_name = './PyQTInterface/GDSFile/INV2.gds'
    window.loadGDS(test=file_name)
    window.inspect_array()
    assert window.array_list_widget.count() == 8
    window.reset()

def test_inspect_path(qtbot):
    global window
    with HiddenConsole():
        if window:
            window.reset()
        window = MainWindow._MainWindow()
        # qtbot.addWidget(window)
        # qtbot.waitForWindowShown(window)
    import user_setup
    if user_setup._Technology != 'TSMC65nm':
        window.request_change_process(None, 'TSMC65nm')
    user_setup.MULTI_THREAD = True
    file_name = './PyQTInterface/GDSFile/INV2.gds'
    window.loadGDS(test=file_name)
    window.inspect_path_point()
    assert window.path_point_widget.count() == 15
    window.reset()


def test_technology_node_change(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window
    import user_setup
    from PyQTInterface.layermap import LayerReader
    from PyQTInterface.layermap import DisplayReader
    from generatorLib import drc_api
    from generatorLib import DesignParameters


    def test_drc(technology):
        drc_test = drc_api.drc_classified_dict
        every_items = [len(item) for item in drc_test.values()]
        length = sum(every_items)
        if technology == 'TSMC65nm':
            assert length == 153
        elif technology == 'SS28nm':
            assert length == 184
        elif technology == 'TSMC90nm':
            assert length == 138
        elif technology == 'TSMC45nm':
            assert length == 149

    def test_layer(technology):
        test1 = len(LayerReader._ExtendLayerMappingTmp)
        test2 = len(LayerReader._LayDatNumToName)
        test3 = len(LayerReader._LayerNum2CommonName)
        if technology == 'SS28nm':
            assert test1 == 1173
            assert test2 == 29
            assert test3 == 101
        elif technology == 'TSMC45nm':
            assert test1 == 1174
            assert test2 == 56
            assert test3 == 179
        elif technology == 'TSMC65nm':
            assert test1 == 481
            assert test2 == 58
            assert test3 == 166
        elif technology == 'TSMC90nm':
            assert test1 == 448
            assert test2 == 55
            assert test3 == 166


    def test_display(technology):
        # test1 = len(DisplayReader._DisplayDict)
        test2 = len(DisplayReader._LinePatternDict)
        test3 = len(DisplayReader._PatternDict)

        if technology == 'SS28nm':
            # assert test1 == 1576
            assert test2 == 16
            assert test3 == 120
        elif technology == 'TSMC45nm':
            # assert test1 == 2201
            assert test2 == 9
            assert test3 == 46
        elif technology == 'TSMC65nm':
            # assert test1 == 933
            assert test2 == 9
            assert test3 == 47
        elif technology == 'TSMC90nm':
            # assert test1 == 931
            assert test2 == 9
            assert test3 == 47

    def test_dp(technology):
        test1 = len(DesignParameters._LayerMapping)
        test2 = len(DesignParameters._LayerMappingTmp)

        if technology == 'SS28nm':
            assert test1 == 51
            assert test2 == 1173
        elif technology == 'TSMC45nm':
            assert test1 == 38
            assert test2 == 1174
        elif technology == 'TSMC65nm':
            assert test1 == 40
            assert test2 == 481
        elif technology == 'TSMC90nm':
            assert test1 == 38
            assert test2 == 448

    def test_process(technology):
        if user_setup._Technology != technology:
            window.request_change_process(None, technology)
        else:
            return
        test_drc(technology)
        test_layer(technology)
        test_display(technology)
        test_dp(technology)

    test_process('TSMC65nm')
    test_process('SS28nm')
    test_process('TSMC65nm')
    test_process('TSMC45nm')
    test_process('TSMC90nm')

    window.reset()


def test_create_submodule_from_sref(qtbot):
    global window
    with HiddenConsole():
        if not window:
            window = MainWindow._MainWindow()
        window.show()
    import user_setup
    if user_setup._Technology != 'TSMC65nm':
        window.request_change_process(None, 'TSMC65nm')
    user_setup.MULTI_THREAD = False
    file_name = './PyQTInterface/GDSFile/INV2.gds'
    window.loadGDS(test=file_name)
    vs_dict = window.visualItemDict['NMOSInINV_0']
    vs_dict.setSelected(True)
    window.create_submodule_by_sref(test=True)
    assert window.module_dict['NMOSInINV_0']
    window = window.module_dict['NMOSInINV_0']
    assert window.module_dict['INV']
    assert window._QTObj._qtProject._DesignParameter['NMOSInINV_0']
    assert len(window._QTObj._qtProject._DesignParameter['NMOSInINV_0']) == 32
    assert len(window._QTObj._qtProject._DesignConstraint['NMOSInINV_0']) == 32
    item_list = list(window._QTObj._qtProject._DesignParameter['NMOSInINV_0'].keys())
    for item in item_list:
        assert window.visualItemDict[item]
        assert window.visualItemDict[item] in window.scene.items()

    window.reset()

##################################test for scene##################################
def test_boundary_design_edit(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_path_design_edit(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_sref_design_edit(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_text_design_edit(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_pin_design_edit(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_dp_highlight(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_dp_copy(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_dp_move(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window

    ### create sref ###
    window.widget_delegator.loadSRefWindow()
    qtbot.waitForWindowShown(window.ls)
    qtbot.keyClicks(window.ls.name_input, 'sref_test')
    qtbot.keyClicks(window.ls.XY_input, '-1000,-1000')
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
    print(1)


##################################test for dc_constraint_view##################################
def test_ast_typing(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_ast_shift(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_ast_id_double_click(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_ast_id_highlight(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_ast_id_delete(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window



