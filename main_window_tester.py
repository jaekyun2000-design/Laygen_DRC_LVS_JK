import sys, os

from PyQt5.QtWidgets import QPushButton

from PyQTInterface import MainWindow
from PyQt5 import QtCore
import user_setup
from PyQt5 import QtGui
from PyQt5 import QtWidgets
user_setup.DL_FEATURE=False


window=None

class HiddenConsole:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')
    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

def test_main_window(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
    window.show()
    qtbot.waitForWindowShown(window)
    # assert window.test == 1
    assert window.test == True

##################################test for dp creation##################################
def test_boundary_window(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
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


def test_path_window(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
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



def test_sref_window(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
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



def test_text_window(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
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



def test_pin_window(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
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



##################################test for dp edit##################################
def test_boundary_edit_window(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
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


def test_path_edit_window(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
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


def test_sref_edit_window(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
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



##################################test for dc creation##################################
def test_create_pycode(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()

    window.widget_delegator.makePyCodeWindow()
    qtbot.waitForWindowShown(window.cw)
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(1).widget(), 'pycode_test')
    window.cw.on_buttonBox_accepted()


def test_create_ast(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()

    window.widget_delegator.makeConstraintWindowAST()
    qtbot.waitForWindowShown(window.cw)
    qtbot.keyClicks(window.cw.type_input, 'Assign')
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(1).widget(), 'targets')
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(2).widget(), 'values')
    window.cw.on_buttonBox_accepted()


def test_create_element(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
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


def test_create_XYCalculator(qtbot):
    with HiddenConsole():
        window = MainWindow._MainWindow()
    # XYCoordinate
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

    # Logic Expression
    window.calculator()
    qtbot.waitForWindowShown(window.calculator_window)

    test_create_element(qtbot)
    window.calculator_window.display.setText("center('test_boundary[0]') + rt('test_boundary[0]') *"
                                             " width('test_boundary[0]') / bottom('test_boundary[0]') + 2")
    window.calculator_window.equationList = ["center('test_boundary[0]') + rt('test_boundary[0]') * " \
                                            "width('test_boundary[0]') / bottom('test_boundary[0]') + 2"]
    window.calculator_window.y_button.setChecked(True)
    window.calculator_window.add_clicked()
    window.calculator_window.y_button.setChecked(True)
    window.calculator_window.display.setText("center('test_boundary[0]') + rb('test_boundary[0]') *"
                                             " height('test_boundary[0]') / bottom('test_boundary[0]') + 2")
    window.calculator_window.equationList = ["center('test_boundary[0]') + rb('test_boundary[0]') * " \
                                        "height('test_boundary[0]') / bottom('test_boundary[0]') + 2"]
    window.calculator_window.add_clicked()
    window.calculator_window.export_clicked()


    dc_id_xy = list(window._QTObj._qtProject._DesignConstraint['EasyDebugModule'].keys())[0]
    dc_id_LE = list(window._QTObj._qtProject._DesignConstraint['EasyDebugModule'].keys())[1]
    assert window._QTObj._qtProject._DesignConstraint['EasyDebugModule'][dc_id_xy]._ast._type == 'XYCoordinate'
    assert window._QTObj._qtProject._DesignConstraint['EasyDebugModule'][dc_id_LE]._ast._type == 'LogicExpression'

def test_create_conditionexp(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
    window.condition_expression()
    qtbot.waitForWindowShown(window.condition_expression_window)
    window.condition_expression_window.input_widget.add_line('and')
    qtbot.keyClicks(window.condition_expression_window.input_widget.main_layout.itemAt(0).itemAt(0).itemAt(1).itemAt(0).widget(), 'test1')
    qtbot.keyClicks(window.condition_expression_window.input_widget.main_layout.itemAt(0).itemAt(2).itemAt(1).itemAt(0).widget(), 'cond1')
    qtbot.keyClicks(window.condition_expression_window.input_widget.main_layout.itemAt(1).itemAt(0).itemAt(1).itemAt(0).widget(), 'test2')
    qtbot.keyClicks(window.condition_expression_window.input_widget.main_layout.itemAt(1).itemAt(2).itemAt(1).itemAt(0).widget(), 'cond2')
    window.condition_expression_window.ok_clicked()
    dc_id = list(window._QTObj._qtProject._DesignConstraint['EasyDebugModule'].keys())[0]
    stmt_module = window._QTObj._qtProject._DesignConstraint['EasyDebugModule'][dc_id]
    assert window._QTObj._qtProject._DesignConstraint['EasyDebugModule'][dc_id]
    assert window._QTObj._qtProject._DesignConstraint['EasyDebugModule'][dc_id]._ast._type == 'ConditionExpression'

def test_create_conditionstmt(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()

def test_add_constraint_view_from_dp(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()

    import user_setup
    if user_setup._Technology != 'SS28nm':
        window.request_change_process(None, 'SS28nm')
    user_setup.MULTI_THREAD = False
    file_name = './PyQTInterface/GDSFile/ResistorBank.gds'
    window.loadGDS(test=file_name)
    # test_load_gds(qtbot)
    window.add_constraint_view()
    qtbot.keyClicks(window.c_view_configuration.layout().itemAt(0,1).widget(), 'test')
    my_layout = window.c_view_configuration.layout()

    my_layout.itemAt(2, 1).widget().click()
    assert window._QTObj._qtProject._ElementManager_topology_dict['CalculateDesignParameter']
    assert window._QTObj._qtProject._DesignConstraint_topology_dict['CalculateDesignParameter']



def test_add_constraint_view_from_dc(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()

    import user_setup
    if user_setup._Technology != 'SS28nm':
        window.request_change_process(None, 'SS28nm')
    user_setup.MULTI_THREAD = False
    file_name = './PyQTInterface/GDSFile/ResistorBank.gds'
    window.loadGDS(test=file_name)
    # test_load_gds(qtbot)
    window.add_constraint_view()
    qtbot.keyClicks(window.c_view_configuration.layout().itemAt(0,1).widget(), 'test')
    my_layout = window.c_view_configuration.layout()

    qtbot.keyClicks(my_layout.itemAt(1,1).widget(), 'from original DC')
    my_layout.itemAt(2, 1).widget().click()

    assert window._QTObj._qtProject._ElementManager_topology_dict['CalculateDesignParameter']
    assert window._QTObj._qtProject._DesignConstraint_topology_dict['CalculateDesignParameter']
    assert len(window._QTObj._qtProject._DesignConstraint_topology_dict['CalculateDesignParameter']) ==\
        len(window._QTObj._qtProject._DesignConstraint)

def test_assign_variable(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()

    window.widget_delegator.makeConstraintWindowCUSTOM()
    qtbot.waitForWindowShown(window.cw)
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(1).widget(), 'test_boundary')
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(2).widget(), 'PIMP')
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(3).widget(), '0,0')
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(4).widget(), 'width_test')
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(5).widget(), 'length_test')
    window.cw.on_buttonBox_accepted()

    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('test_boundary')
    for i in range(window.dockContentWidget3_2.model.rowCount()):
        if window.dockContentWidget3_2.model.item(i,1).text() == dc_id:
            window.dockContentWidget3_2.setCurrentIndex(window.dockContentWidget3_2.model.item(i).index())
    qtbot.mouseClick(window.sendLeftButton, QtCore.Qt.LeftButton)

    window.dockContentWidget3.setCurrentIndex(window.dockContentWidget3.model.item(0).index().child(2,3))
    index = window.dockContentWidget3.currentIndex()
    window.dockContentWidget3.model.setData(index.siblingAtColumn(3), 'XY_test')
    assert len(window.dv.variableDict) == 4



##################################test for dc execution##################################
def test_encode_constraint(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()

    import user_setup
    if user_setup._Technology != 'TSMC65nm':
        window.request_change_process(None, 'TSMC65nm')
    user_setup.MULTI_THREAD = False
    file_name = './PyQTInterface/GDSFile/INV2.gds'
    window.loadGDS(test=file_name)
    window.min_snap_spacing_change.destroy()
    vs_dict = window.visualItemDict['NMOSInINV_0']
    vs_dict.setSelected(True)

    window.widget_delegator.convert_elements_to_sref_widget([vs_dict])
    qtbot.waitForWindowShown(window.widget_delegator.choice_widget)
    qtbot.mouseClick(window.widget_delegator.choice_widget.layout().itemAt(0).widget(), QtCore.Qt.LeftButton)
    qtbot.waitForWindowShown(window.widget_delegator.ls)
    qtbot.keyClicks(window.widget_delegator.ls.name_input, 'encode_test')
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

    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('encode_test')
    for i in range(window.dockContentWidget3_2.model.rowCount()):
        if window.dockContentWidget3_2.model.item(i,1).text() == dc_id:
            window.dockContentWidget3_2.setCurrentIndex(window.dockContentWidget3_2.model.item(i).index())
    qtbot.mouseClick(window.sendLeftButton, QtCore.Qt.LeftButton)
    code = window.encodeConstraint()
    assert code


def test_run_constraint_boundary(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()

    window.widget_delegator.makeConstraintWindowCUSTOM()
    qtbot.waitForWindowShown(window.cw)
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(1).widget(), 'test_boundary')
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(2).widget(), 'PIMP')
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(3).widget(), '0,0')
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(4).widget(), '100')
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(5).widget(), '200')
    window.cw.on_buttonBox_accepted()

    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('test_boundary')
    for i in range(window.dockContentWidget3_2.model.rowCount()):
        if window.dockContentWidget3_2.model.item(i,1).text() == dc_id:
            window.dockContentWidget3_2.setCurrentIndex(window.dockContentWidget3_2.model.item(i).index())
    qtbot.mouseClick(window.sendLeftButton, QtCore.Qt.LeftButton)

    window.dockContentWidget3.setCurrentIndex(window.dockContentWidget3.model.item(0).index().child(3,3))
    index = window.dockContentWidget3.currentIndex()
    window.dockContentWidget3.model.setData(index.siblingAtColumn(3), '200')

    # qtbot.mouseClick(window.dockContentWidget3.model.item(0).child(3,3).widget(), QtCore.Qt.LeftButton)
    # qtbot.keyPress(window, QtCore.Qt.Key_F2)
    # item = window.dockContentWidget3.model.itemFromIndex(index).text()
    # window.dockContentWidget3.keyPressEvent(QKeyEvent = Qt.Key_F2)
    # qtbot.keyClicks(window.dockContentWidget3.model.XY_value_index, '200')
    # window.dockContentWidget3.model.item(0).index().child(3,3).setText('200')
    # ow.dockContentWidget3.model.indexFromItem(XY_value_item).text()
    # qtbot.keyClicks(window.dockContentWidget3.currentIndex().child(3,4).text(), '100,100')

    window.runConstraint()
    assert window.visualItemDict['test_boundary']
    assert window._QTObj._qtProject._DesignParameter['EasyDebugModule']['test_boundary']
    # qtbot.stop()

def test_run_constraint_path(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()

    window.widget_delegator.makePathWindow()
    qtbot.waitForWindowShown(window.pw)
    qtbot.keyClicks(window.pw.width_input, '100')
    window.pw.AddPathPointWithMouse([0, 0])
    window.pw.clickCount([0, 0])
    window.pw.AddPathPointWithMouse([100, 0])
    window.pw.clickCount([100, 0])
    window.pw.AddPathPointWithMouse([100, 500])
    window.pw.clickCount([100, 500])

    qtbot.keyClicks(window.pw.name_input, 'test_path')
    window.pw.on_buttonBox_accepted()

    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('test_path')
    for i in range(window.dockContentWidget3_2.model.rowCount()):
        if window.dockContentWidget3_2.model.item(i,1).text() == dc_id:
            window.dockContentWidget3_2.setCurrentIndex(window.dockContentWidget3_2.model.item(i).index())
    qtbot.mouseClick(window.sendLeftButton, QtCore.Qt.LeftButton)
    window.runConstraint()

    assert window.visualItemDict['test_path']
    assert window._QTObj._qtProject._DesignParameter['EasyDebugModule']['test_path']
    # qtbot.stop()


def test_run_constraint_sref(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()

    window.widget_delegator.loadSRefWindow()
    qtbot.waitForWindowShown(window.ls)
    qtbot.keyClicks(window.ls.name_input, 'test_sref')
    qtbot.keyClicks(window.ls.XY_input, '0,0')
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
    window.ls.destroy()
    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('test_sref')
    for i in range(window.dockContentWidget3_2.model.rowCount()):
        if window.dockContentWidget3_2.model.item(i,1).text() == dc_id:
            window.dockContentWidget3_2.setCurrentIndex(window.dockContentWidget3_2.model.item(i).index())
    qtbot.mouseClick(window.sendLeftButton, QtCore.Qt.LeftButton)

    window.runConstraint()

    # qtbot.stop()

def test_run_constraint_with_variable(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()

    window.widget_delegator.makeConstraintWindowCUSTOM()
    qtbot.waitForWindowShown(window.cw)
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(1).widget(), 'test_boundary')
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(2).widget(), 'PIMP')
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(3).widget(), '0,0')
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(4).widget(), '100')
    qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(5).widget(), 'length_test')
    window.cw.on_buttonBox_accepted()

    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('test_boundary')
    for i in range(window.dockContentWidget3_2.model.rowCount()):
        if window.dockContentWidget3_2.model.item(i,1).text() == dc_id:
            window.dockContentWidget3_2.setCurrentIndex(window.dockContentWidget3_2.model.item(i).index())
    qtbot.mouseClick(window.sendLeftButton, QtCore.Qt.LeftButton)

    window.dockContentWidget3.setCurrentIndex(window.dockContentWidget3.model.item(0).index().child(3,3))
    index = window.dockContentWidget3.currentIndex()
    window.dockContentWidget3.model.setData(index.siblingAtColumn(3), 'width_test')

    window.dv.model.setData(window.dv.model.index(1, 1), '100')
    window.dv.model.setData(window.dv.model.index(2, 1), '200')
    window.runConstraint_for_update()

    assert window.visualItemDict['test_boundary']


def test_run_constraint_for_update(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()

        window.widget_delegator.makeConstraintWindowCUSTOM()
        qtbot.waitForWindowShown(window.cw)
        qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(1).widget(), 'test_boundary')
        qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(2).widget(), 'PIMP')
        qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(3).widget(), '0,0')
        qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(4).widget(), '100')
        qtbot.keyClicks(window.cw.setupVboxColumn2.itemAt(5).widget(), '200')
        window.cw.on_buttonBox_accepted()

        dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('test_boundary')
        for i in range(window.dockContentWidget3_2.model.rowCount()):
            if window.dockContentWidget3_2.model.item(i, 1).text() == dc_id:
                window.dockContentWidget3_2.setCurrentIndex(window.dockContentWidget3_2.model.item(i).index())
        qtbot.mouseClick(window.sendLeftButton, QtCore.Qt.LeftButton)

        window.dockContentWidget3.setCurrentIndex(window.dockContentWidget3.model.item(0).index().child(3, 3))
        index = window.dockContentWidget3.currentIndex()
        window.dockContentWidget3.model.setData(index.siblingAtColumn(3), '200')

        window.widget_delegator.makePathWindow()
        qtbot.waitForWindowShown(window.pw)
        qtbot.keyClicks(window.pw.width_input, '100')
        window.pw.AddPathPointWithMouse([0, 0])
        window.pw.clickCount([0, 0])
        window.pw.AddPathPointWithMouse([100, 0])
        window.pw.clickCount([100, 0])
        window.pw.AddPathPointWithMouse([100, 500])
        window.pw.clickCount([100, 500])

        qtbot.keyClicks(window.pw.name_input, 'test_path')
        window.pw.on_buttonBox_accepted()

        dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('test_path')
        for i in range(window.dockContentWidget3_2.model.rowCount()):
            if window.dockContentWidget3_2.model.item(i, 1).text() == dc_id:
                window.dockContentWidget3_2.setCurrentIndex(window.dockContentWidget3_2.model.item(i).index())
        qtbot.mouseClick(window.sendLeftButton, QtCore.Qt.LeftButton)

        window.widget_delegator.loadSRefWindow()
        qtbot.waitForWindowShown(window.ls)
        qtbot.keyClicks(window.ls.name_input, 'test_sref')
        qtbot.keyClicks(window.ls.XY_input, '0,0')
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
        window.ls.destroy()
        dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('test_sref')
        for i in range(window.dockContentWidget3_2.model.rowCount()):
            if window.dockContentWidget3_2.model.item(i, 1).text() == dc_id:
                window.dockContentWidget3_2.setCurrentIndex(window.dockContentWidget3_2.model.item(i).index())
        qtbot.mouseClick(window.sendLeftButton, QtCore.Qt.LeftButton)

        window.runConstraint_for_update()
        assert window.visualItemDict['test_boundary']
        assert window.visualItemDict['test_path']
        assert window.visualItemDict['test_sref']
        assert window._QTObj._qtProject._DesignParameter['EasyDebugModule']['test_boundary']
        assert window._QTObj._qtProject._DesignParameter['EasyDebugModule']['test_path']
        assert window._QTObj._qtProject._DesignParameter['EasyDebugModule']['test_sref']

        #   Error Log:
        #    self.code = f'_Name="{self.class_name}"\n' + self.code
        #    TypeError: can only concatenate str (not "NoneType") to str

def test_run_constraint_from_project(qtbot):
    '''
    pre_defined project load and run...
    '''

    with HiddenConsole():
        window = MainWindow._MainWindow()

    window.show()
    file_name = './PyQTInterface/Project/test_project.bin'
    window.loadProject(file_name)

    window.dockContentWidget3_2.setCurrentIndex(window.dockContentWidget3_2.model.index(0,0))
    qtbot.mouseClick(window.sendLeftButton, QtCore.Qt.LeftButton)
    # XY_idx = window.dockContentWidget3.model.index(0,0).child(3,0)

    window.dockContentWidget3.model.setData(window.dockContentWidget3.model.index(0,0).child(3, 3), '200')

    window.runConstraint_for_update()

    # qtbot.stop()
def test_run_constraint_multi_constraint_view(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()


##################################test for dp-dc pairing##################################
def test_paring_after_dp_creation(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
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


def test_paring_after_dc_creation(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
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


def test_paring_after_project_load(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
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


def test_paring_after_gds_load(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
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


def test_paring_after_create_submodule(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
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


def test_paring_after_convert_sref_assign(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
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


def test_paring_after_convert_create_assign(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
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


##################################test for scene_visible##################################
def test_visible(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
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



def test_clickable(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
    window.show()

    ### Initialize visualization item class dict ###
    window.vsitem_dict_initialization()

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

    ### Assertion ###
    assert not int(window.visualItemDict['clickable_test'].flags() & QtWidgets.QGraphicsItem.ItemIsSelectable) == window.visualItemDict['clickable_test'].ItemIsSelectable

    ### Set all clickable ###
    qtbot.mouseClick(window.dockContentWidget1_2.clickable_button, QtCore.Qt.LeftButton)

    ### Assertion ###
    assert int(window.visualItemDict['clickable_test'].flags() & QtWidgets.QGraphicsItem.ItemIsSelectable) == window.visualItemDict['clickable_test'].ItemIsSelectable



def test_used_layer(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
    window.show()

    ### Initialize visualization item class dict ###
    window.vsitem_dict_initialization()

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

    ### Create METAL2 boundary ###
    window.widget_delegator.make_boundary_window()
    qtbot.waitForWindowShown(window.bw)
    window.bw.AddBoundaryPointWithMouse([0,0])
    window.bw.clickCount([0,0])
    window.bw.AddBoundaryPointWithMouse([-100,-100])
    window.bw.clickCount([-100,-100])
    qtbot.keyClicks(window.bw.layer_input,'METAL2')
    qtbot.keyClicks(window.bw.name_input,'clickable_test')
    window.bw.on_buttonBox_accepted()

    ### Create PIMP boundary ###
    window.widget_delegator.make_boundary_window()
    qtbot.waitForWindowShown(window.bw)
    window.bw.AddBoundaryPointWithMouse([0,0])
    window.bw.clickCount([0,0])
    window.bw.AddBoundaryPointWithMouse([100,-100])
    window.bw.clickCount([100,-100])
    qtbot.keyClicks(window.bw.layer_input,'PIMP')
    qtbot.keyClicks(window.bw.name_input,'clickable_test')
    window.bw.on_buttonBox_accepted()

    ### Set show used layer ###
    qtbot.mouseClick(window.dockContentWidget1_2.show_layer_option_button, QtCore.Qt.LeftButton)

    ### Assertion ###
    for i in range(window.dockContentWidget1_2.layer_table_widget.model().rowCount()):
        assert window.dockContentWidget1_2.layer_table_widget.model().item(i).text() in ['METAL1', 'METAL2', 'PIMP']


def test_generator_show_hide(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
    window.show()
    ### Create METAL1 boundary ###
    window.widget_delegator.make_boundary_window()
    qtbot.waitForWindowShown(window.bw)
    window.bw.AddBoundaryPointWithMouse([0,0])
    window.bw.clickCount([0,0])
    window.bw.AddBoundaryPointWithMouse([100,100])
    window.bw.clickCount([100,100])
    qtbot.keyClicks(window.bw.layer_input,'METAL1')
    qtbot.keyClicks(window.bw.name_input,'gen_show_test')
    window.bw.on_buttonBox_accepted()

    ### Send to generator dc ###
    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('gen_show_test')
    for i in range(window.dockContentWidget3_2.model.rowCount()):
        if window.dockContentWidget3_2.model.item(i,1).text() == dc_id:
            window.dockContentWidget3_2.setCurrentIndex(window.dockContentWidget3_2.model.item(i).index())
    qtbot.mouseClick(window.sendLeftButton, QtCore.Qt.LeftButton)

    ### Set generator non-visible ###
    qtbot.mouseClick(window.dockWidget1.widget().layout().itemAt(0).widget().layout().itemAt(9).itemAt(0).widget(), QtCore.Qt.LeftButton)

    ### Assertion ###
    assert not window.visualItemDict['gen_show_test'].isVisible()

    ### Set generator visible ###
    qtbot.mouseClick(window.dockWidget1.widget().layout().itemAt(0).widget().layout().itemAt(9).itemAt(0).widget(), QtCore.Qt.LeftButton)

    ### Assertion ###
    assert window.visualItemDict['gen_show_test'].isVisible()


def test_candidate_show_hide(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
    window.show()
    ### Create METAL1 boundary ###
    window.widget_delegator.make_boundary_window()
    qtbot.waitForWindowShown(window.bw)
    window.bw.AddBoundaryPointWithMouse([0,0])
    window.bw.clickCount([0,0])
    window.bw.AddBoundaryPointWithMouse([100,100])
    window.bw.clickCount([100,100])
    qtbot.keyClicks(window.bw.layer_input,'METAL1')
    qtbot.keyClicks(window.bw.name_input,'can_show_test')
    window.bw.on_buttonBox_accepted()

    ### Set candidate non-visible ###
    qtbot.mouseClick(window.dockWidget1.widget().layout().itemAt(0).widget().layout().itemAt(9).itemAt(2).widget(), QtCore.Qt.LeftButton)

    ### Assertion ###
    assert not window.visualItemDict['can_show_test'].isVisible()

    ### Set candidate visible ###
    qtbot.mouseClick(window.dockWidget1.widget().layout().itemAt(0).widget().layout().itemAt(9).itemAt(2).widget(), QtCore.Qt.LeftButton)

    ### Assertion ###
    assert window.visualItemDict['can_show_test'].isVisible()



##################################test for project##################################
def test_project_save(qtbot):

    with HiddenConsole():
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



def test_project_load(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
    #     qtbot.addWidget(window)
    #     qtbot.waitForWindowShown(window)
    file_name = './PyQTInterface/Project/test_project.bin'
    window.loadProject(file_name)
    assert window.test



def test_load_gds(qtbot):

    with HiddenConsole():
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
    #


##################################test for scene_right_click##################################
def test_elements_array_boundary_relative(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
    ### Create source sref ###
    window.widget_delegator.loadSRefWindow()
    qtbot.waitForWindowShown(window.ls)
    qtbot.keyClicks(window.ls.name_input, 'source')
    qtbot.keyClicks(window.ls.XY_input, '0,0')
    qtbot.keyClicks(window.ls.library_input, 'NbodyContact')
    for idx, par_name in enumerate(window.ls.par_name):
        if 'COX' in par_name:
            window.ls.par_valueForLineEdit[idx].clear()
            qtbot.keyClicks(window.ls.par_valueForLineEdit[idx], '5')
        elif 'COY' in par_name:
            window.ls.par_valueForLineEdit[idx].clear()
            qtbot.keyClicks(window.ls.par_valueForLineEdit[idx], '1')
    window.ls.on_buttonBox_accepted()

    ### Create relative boundary array ###
    window.createVariable('boundary_array')
    qtbot.waitForWindowShown(window.vw)
    test_widget = window.vw.variable_widget
    row_layout = test_widget.widget_dictionary['boundaryrelative'].layout()
    qtbot.keyClicks(row_layout.itemAt(0).itemAt(1).widget(), 'boundary_relative_array_test')
    qtbot.keyClicks(row_layout.itemAt(1).itemAt(1).widget(), 'METAL1')
    QtGui.QGuiApplication.clipboard().setText("['source[0]', '_COLayer[0]']")
    qtbot.mouseClick(row_layout.itemAt(2).itemAt(2).widget(), QtCore.Qt.LeftButton)
    qtbot.waitForWindowShown(test_widget.cal)
    qtbot.mouseClick(test_widget.cal.center_buttons, QtCore.Qt.LeftButton)
    qtbot.mouseClick(test_widget.cal.layout().itemAtPosition(3,3).widget(), QtCore.Qt.LeftButton)
    qtbot.keyClicks(row_layout.itemAt(8).itemAt(1).widget(), '500')
    window.vw.on_buttonBox_accepted()

    ### Send to generator dc ###
    for i in range(window.dockContentWidget3_2.model.rowCount()):
        window.dockContentWidget3_2.setCurrentIndex(window.dockContentWidget3_2.model.item(0).index())
        qtbot.mouseClick(window.sendLeftButton, QtCore.Qt.LeftButton)

    window.runConstraint_for_update()

    ### Assertion ###
    assert window.visualItemDict['boundary_relative_array_test']
    source_XY = list()
    for XY in window.visualItemDict['source'].sub_element_dict['_COLayer[0]']._ItemTraits['_XYCoordinates']:
        tmp_XY = [window.visualItemDict['source']._ItemTraits['_XYCoordinates'][0][0]+XY[0],window.visualItemDict['source']._ItemTraits['_XYCoordinates'][0][1]+XY[1]]
        source_XY.append(tmp_XY)
    array_XY = window.visualItemDict['boundary_relative_array_test']._ItemTraits['_XYCoordinates']
    assert source_XY == array_XY
    assert window.visualItemDict['boundary_relative_array_test']._ItemTraits['_Height'] == 500


def test_elements_array_path_relative(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
    ### Create source sref ###
    window.widget_delegator.loadSRefWindow()
    qtbot.waitForWindowShown(window.ls)
    qtbot.keyClicks(window.ls.name_input, 'source')
    qtbot.keyClicks(window.ls.XY_input, '0,0')
    qtbot.keyClicks(window.ls.library_input, 'NbodyContact')
    for idx, par_name in enumerate(window.ls.par_name):
        if 'COX' in par_name:
            window.ls.par_valueForLineEdit[idx].clear()
            qtbot.keyClicks(window.ls.par_valueForLineEdit[idx], '5')
        elif 'COY' in par_name:
            window.ls.par_valueForLineEdit[idx].clear()
            qtbot.keyClicks(window.ls.par_valueForLineEdit[idx], '1')
    window.ls.on_buttonBox_accepted()

    ### Create target sref ###
    window.widget_delegator.loadSRefWindow()
    qtbot.waitForWindowShown(window.ls)
    qtbot.keyClicks(window.ls.name_input, 'target')
    qtbot.keyClicks(window.ls.XY_input, '0,300')
    qtbot.keyClicks(window.ls.library_input, 'NbodyContact')
    for idx, par_name in enumerate(window.ls.par_name):
        if 'COX' in par_name:
            window.ls.par_valueForLineEdit[idx].clear()
            qtbot.keyClicks(window.ls.par_valueForLineEdit[idx], '5')
        elif 'COY' in par_name:
            window.ls.par_valueForLineEdit[idx].clear()
            qtbot.keyClicks(window.ls.par_valueForLineEdit[idx], '1')
    window.ls.on_buttonBox_accepted()

    ### Create relative path array ###
    window.createVariable('path_array')
    qtbot.waitForWindowShown(window.vw)
    test_widget = window.vw.variable_widget
    test_widget.request_show('path', 'relative')
    row_layout = test_widget.widget_dictionary['pathrelative'].layout()
    qtbot.keyClicks(row_layout.itemAt(0).itemAt(1).widget(), 'path_relative_array_test')
    qtbot.keyClicks(row_layout.itemAt(1).itemAt(1).widget(), 'METAL1')
    QtGui.QGuiApplication.clipboard().setText("['source[0]', '_COLayer[0]']")
    qtbot.mouseClick(row_layout.itemAt(2).itemAt(2).widget(), QtCore.Qt.LeftButton)
    qtbot.waitForWindowShown(test_widget.cal)
    qtbot.mouseClick(test_widget.cal.center_buttons, QtCore.Qt.LeftButton)
    qtbot.mouseClick(test_widget.cal.layout().itemAtPosition(3,3).widget(), QtCore.Qt.LeftButton)
    QtGui.QGuiApplication.clipboard().setText("['target[0]', '_COLayer[0]']")
    qtbot.mouseClick(row_layout.itemAt(7).itemAt(2).widget(), QtCore.Qt.LeftButton)
    qtbot.waitForWindowShown(test_widget.cal)
    qtbot.mouseClick(test_widget.cal.center_buttons, QtCore.Qt.LeftButton)
    qtbot.mouseClick(test_widget.cal.layout().itemAtPosition(3,3).widget(), QtCore.Qt.LeftButton)
    window.vw.on_buttonBox_accepted()

    ### Send to generator dc ###
    for i in range(window.dockContentWidget3_2.model.rowCount()):
        window.dockContentWidget3_2.setCurrentIndex(window.dockContentWidget3_2.model.item(0).index())
        qtbot.mouseClick(window.sendLeftButton, QtCore.Qt.LeftButton)

    window.runConstraint_for_update()

    ### Assertion ###
    tmp = window.visualItemDict
    assert 'path_relative_array_test' in window.visualItemDict
    source_XY = list()
    target_XY = list()
    for XY in window.visualItemDict['source'].sub_element_dict['_COLayer[0]']._ItemTraits['_XYCoordinates']:
        tmp_XY = [window.visualItemDict['source']._ItemTraits['_XYCoordinates'][0][0]+XY[0],window.visualItemDict['source']._ItemTraits['_XYCoordinates'][0][1]+XY[1]]
        source_XY.append(tmp_XY)
    for XY in window.visualItemDict['target'].sub_element_dict['_COLayer[0]']._ItemTraits['_XYCoordinates']:
        tmp_XY = [window.visualItemDict['target']._ItemTraits['_XYCoordinates'][0][0]+XY[0],window.visualItemDict['target']._ItemTraits['_XYCoordinates'][0][1]+XY[1]]
        target_XY.append(tmp_XY)
    array_XY = window.visualItemDict['path_relative_array_test']._ItemTraits['_XYCoordinates']
    for i in range(len(source_XY)):
        assert array_XY[i] == [source_XY[i], target_XY[i]]


def test_elements_array_sref_relative(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
    ### Create source sref ###
    window.widget_delegator.loadSRefWindow()
    qtbot.waitForWindowShown(window.ls)
    qtbot.keyClicks(window.ls.name_input, 'source')
    qtbot.keyClicks(window.ls.XY_input, '0,0')
    qtbot.keyClicks(window.ls.library_input, 'NbodyContact')
    for idx, par_name in enumerate(window.ls.par_name):
        if 'COX' in par_name:
            window.ls.par_valueForLineEdit[idx].clear()
            qtbot.keyClicks(window.ls.par_valueForLineEdit[idx], '5')
        elif 'COY' in par_name:
            window.ls.par_valueForLineEdit[idx].clear()
            qtbot.keyClicks(window.ls.par_valueForLineEdit[idx], '1')
    window.ls.on_buttonBox_accepted()

    ### Create relative boundary array ###
    window.createVariable('sref_array')
    qtbot.waitForWindowShown(window.vw)
    test_widget = window.vw.variable_widget
    test_widget.request_show('sref', 'relative')
    row_layout = test_widget.widget_dictionary['srefrelative'].layout()
    qtbot.keyClicks(row_layout.itemAt(0).itemAt(1).widget(), 'sref_relative_array_test')
    QtGui.QGuiApplication.clipboard().setText("['source[0]', '_COLayer[0]']")
    qtbot.mouseClick(row_layout.itemAt(1).itemAt(2).widget(), QtCore.Qt.LeftButton)
    qtbot.waitForWindowShown(test_widget.cal)
    qtbot.mouseClick(test_widget.cal.center_buttons, QtCore.Qt.LeftButton)
    qtbot.mouseClick(test_widget.cal.layout().itemAtPosition(3,3).widget(), QtCore.Qt.LeftButton)
    qtbot.mouseClick(row_layout.itemAt(2).itemAt(2).widget(), QtCore.Qt.LeftButton)
    qtbot.waitForWindowShown(test_widget.ls)
    qtbot.keyClicks(test_widget.ls.library_input, 'NbodyContact')
    for idx, par_name in enumerate(test_widget.ls.par_name):
        if 'COX' in par_name:
            test_widget.ls.par_valueForLineEdit[idx].clear()
            qtbot.keyClicks(test_widget.ls.par_valueForLineEdit[idx], '1')
        elif 'COY' in par_name:
            test_widget.ls.par_valueForLineEdit[idx].clear()
            qtbot.keyClicks(test_widget.ls.par_valueForLineEdit[idx], '3')
    test_widget.ls.on_buttonBox_accepted()
    window.vw.on_buttonBox_accepted()

    ### Send to generator dc ###
    for i in range(window.dockContentWidget3_2.model.rowCount()):
        window.dockContentWidget3_2.setCurrentIndex(window.dockContentWidget3_2.model.item(0).index())
        qtbot.mouseClick(window.sendLeftButton, QtCore.Qt.LeftButton)

    window.runConstraint_for_update()

    ### Assertion ###
    tmp = window.visualItemDict
    assert window.visualItemDict['sref_relative_array_test']
    source_XY = list()
    for XY in window.visualItemDict['source'].sub_element_dict['_COLayer[0]']._ItemTraits['_XYCoordinates']:
        tmp_XY = [window.visualItemDict['source']._ItemTraits['_XYCoordinates'][0][0]+XY[0],window.visualItemDict['source']._ItemTraits['_XYCoordinates'][0][1]+XY[1]]
        source_XY.append(tmp_XY)
    array_XY = window.visualItemDict['sref_relative_array_test']._ItemTraits['_XYCoordinates']
    assert source_XY == array_XY


def test_elements_array_boundary_offset(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()


def test_elements_array_path_offset(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()


def test_elements_array_sref_offset(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()


def test_elements_convert_assign(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()


def test_elements_convert_create(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()


##################################test for multimodule##################################

def test_module_create(qtbot):
    with HiddenConsole():
        window = MainWindow._MainWindow()

    window.show_module_window()
    qtbot.keyClicks(window.nmw.name_input, 'test_module')
    window.nmw.on_makeBox_accepted()

    assert 'test_module' in window.module_name_list
    assert 'test_module' in window.module_dict

    new_window = window.module_dict['test_module']
    assert 'test_module' in new_window.module_name_list
    assert 'test_module' in new_window.module_dict


def test_module_shift(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()

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


def test_module_run(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()


##################################test for calculator##################################
def test_calculator_xy_coord(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()


def test_calculator_expression(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()


def test_calculator_index(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()


def test_calculator_drc(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()


def test_calculator_number(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()


def test_calculator_preset_load(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()


def test_calculator_path_xy(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()


##################################test for automation##################################
def test_inspect_array(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
    if user_setup._Technology != 'TSMC65nm':
        window.request_change_process(None, 'TSMC65nm')
    user_setup.MULTI_THREAD = False
    file_name = './PyQTInterface/GDSFile/INV2.gds'
    window.loadGDS(test=file_name)
    window.inspect_array()
    assert window.array_list_widget.count() == 8


def test_inspect_path(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
        # qtbot.addWidget(window)
        # qtbot.waitForWindowShown(window)
    import user_setup
    if user_setup._Technology != 'TSMC65nm':
        window.request_change_process(None, 'TSMC65nm')
    user_setup.MULTI_THREAD = False
    file_name = './PyQTInterface/GDSFile/INV2.gds'
    window.loadGDS(test=file_name)
    window.inspect_path_point()
    assert window.path_point_widget.count() == 15



def test_technology_node_change(qtbot):
    with HiddenConsole():
        window = MainWindow._MainWindow()
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
            assert test1 == 53
            assert test2 == 1173
        elif technology == 'TSMC45nm':
            assert test1 == 38
            assert test2 == 1174
        elif technology == 'TSMC65nm':
            assert test1 == 47
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




def test_create_submodule_from_sref(qtbot):
    with HiddenConsole():
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



##################################test for scene##################################
# def test_boundary_design_edit(qtbot):
#
#     with HiddenConsole():
#         window = MainWindow._MainWindow()
#
#
# def test_path_design_edit(qtbot):
#
#     with HiddenConsole():
#         window = MainWindow._MainWindow()
#
#
# def test_sref_design_edit(qtbot):
#
#     with HiddenConsole():
#         window = MainWindow._MainWindow()


def test_text_design_edit(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
    window.show()

    ### Create text ###
    window.widget_delegator.makeTextWindow()
    qtbot.waitForWindowShown(window.txtw)
    qtbot.keyClicks(window.txtw.name_input,'text_edit_test')
    qtbot.keyClicks(window.txtw.text_input,'text_edit_test')
    qtbot.keyClicks(window.txtw.width_input,'10')
    window.txtw.DetermineCoordinateWithMouse([100,100])
    window.txtw.on_buttonBox_accepted()

    ### Selecte text ###
    window.dockContentWidget2.UpdateCustomItem([window.visualItemDict['text_edit_test']])
    target_item = window.dockContentWidget2.findItems('text_edit_test', QtCore.Qt.MatchFlag.MatchExactly)[0]
    assert target_item

    window.dockContentWidget2.ModifyingDesign(target_item)
    assert window.dockContentWidget2.txtw

    ### Edit design ###
    test_widget = window.dockContentWidget2.txtw
    test_widget.name_input.clear()
    test_widget.text_input.clear()
    test_widget.width_input.clear()
    qtbot.keyClicks(test_widget.name_input, 'text_name_change')
    qtbot.keyClicks(test_widget.text_input, 'text_name_change')
    qtbot.keyClicks(test_widget.width_input, '20')
    test_widget.on_buttonBox_accepted()

    assert window._QTObj._qtProject._DesignParameter['EasyDebugModule']['text_name_change']
    assert 'text_edit_test' not in window._QTObj._qtProject._DesignParameter['EasyDebugModule']
    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('text_name_change')
    assert window._QTObj._qtProject._DesignConstraint['EasyDebugModule'][dc_id]
    assert window.visualItemDict['text_name_change']
    assert window.visualItemDict['text_name_change'] in window.scene.items()


def test_pin_design_edit(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()
    window.show()

    ### Create pin ###
    window.widget_delegator.makePinWindow()
    qtbot.waitForWindowShown(window.pinw)
    qtbot.keyClicks(window.pinw.name_input,'pin_edit_test')
    qtbot.keyClicks(window.pinw.layer_input,'METAL1PIN')
    qtbot.keyClicks(window.pinw.text_input,'pin_edit_test')
    qtbot.keyClicks(window.pinw.width_input,'10')
    window.pinw.DetermineCoordinateWithMouse([100,100])
    window.pinw.on_buttonBox_accepted()

    ### Selecte pin ###
    window.dockContentWidget2.UpdateCustomItem([window.visualItemDict['pin_edit_test']])
    target_item = window.dockContentWidget2.findItems('pin_edit_test', QtCore.Qt.MatchFlag.MatchExactly)[0]
    assert target_item

    window.dockContentWidget2.ModifyingDesign(target_item)
    assert window.dockContentWidget2.pinw

    ### Edit design ###
    test_widget = window.dockContentWidget2.pinw
    test_widget.name_input.clear()
    test_widget.text_input.clear()
    test_widget.width_input.clear()
    qtbot.keyClicks(test_widget.name_input, 'pin_name_change')
    qtbot.keyClicks(test_widget.text_input, 'pin_name_change')
    qtbot.keyClicks(test_widget.width_input, '20')
    idx = test_widget.layer_input.findText('METAL2PIN')
    test_widget.layer_input.setCurrentIndex(idx)
    test_widget.on_buttonBox_accepted()

    assert window._QTObj._qtProject._DesignParameter['EasyDebugModule']['pin_name_change']
    assert 'pin_edit_test' not in window._QTObj._qtProject._DesignParameter['EasyDebugModule']
    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('pin_name_change')
    assert window._QTObj._qtProject._DesignConstraint['EasyDebugModule'][dc_id]
    assert window.visualItemDict['pin_name_change']
    assert window.visualItemDict['pin_name_change'] in window.scene.items()
    assert window._QTObj._qtProject._DesignParameter['EasyDebugModule']['pin_name_change']._DesignParameter['_LayerUnifiedName'] == 'METAL2PIN'


# def test_dp_highlight(qtbot):
#
#     with HiddenConsole():
#         window = MainWindow._MainWindow()


def test_dp_copy(qtbot):
    user_setup._Snap_mode='any_angle'
    with HiddenConsole():
        window = MainWindow._MainWindow()
    window.show()
    ### Create boundary ###
    window.widget_delegator.make_boundary_window()
    qtbot.waitForWindowShown(window.bw)
    window.bw.AddBoundaryPointWithMouse([0,0])
    window.bw.clickCount([0,0])
    window.bw.AddBoundaryPointWithMouse([100,100])
    window.bw.clickCount([100,100])
    qtbot.keyClicks(window.bw.name_input,'copy_test')
    window.bw.on_buttonBox_accepted()

    ### Connect signal ###
    window.scene.send_move_item_signal.connect(window.transfer_delegator.get_xy_difference)
    window.scene.send_mouse_move_xy_signal.connect(window.transfer_delegator.get_mouse_point)
    window.scene.send_xy_signal.connect(window.transfer_delegator.get_click_point)

    ### Copy item ###
    window.visualItemDict['copy_test'].setSelected(True)
    qtbot.keyClicks(window.centralWidget(), 'C')
    qtbot.mouseClick(window.centralWidget().viewport(), QtCore.Qt.LeftButton, pos=window.centralWidget().mapFromScene(QtCore.QPoint(0,0)))

    ### Assertion ###
    assert 'copy_test' in window.visualItemDict
    assert 'copy_test_0' in window.visualItemDict
    assert window.visualItemDict['copy_test']._ItemTraits['_XYCoordinates'] in [[[50,50]], [[50.,50.]]]
    assert window.visualItemDict['copy_test_0']._ItemTraits['_XYCoordinates'] in [[[0,0]], [[0.,0.]]]

    # for dp_id in list(window.visualItemDict.keys()):
    #     if dp_id is not None:
    #         if 'copy_test' in dp_id:
    #             assert window.visualItemDict[dp_id]._ItemTraits['_XYCoordinates'] in [[[50,50]],[[0.,0.]]]

def test_dp_move(qtbot):
    user_setup._Snap_mode = 'any_angle'
    with HiddenConsole():
        window = MainWindow._MainWindow()
    window.show()
    ### Create boundary ###
    window.widget_delegator.make_boundary_window()
    qtbot.waitForWindowShown(window.bw)
    window.bw.AddBoundaryPointWithMouse([0,0])
    window.bw.clickCount([0,0])
    window.bw.AddBoundaryPointWithMouse([100,100])
    window.bw.clickCount([100,100])
    qtbot.keyClicks(window.bw.name_input,'move_test')
    window.bw.on_buttonBox_accepted()

    ### Connect signal ###
    window.scene.send_move_item_signal.connect(window.transfer_delegator.get_xy_difference)
    window.scene.send_mouse_move_xy_signal.connect(window.transfer_delegator.get_mouse_point)
    window.scene.send_xy_signal.connect(window.transfer_delegator.get_click_point)

    ### Move item ###
    window.visualItemDict['move_test'].setSelected(True)
    qtbot.keyClicks(window.centralWidget(), 'M')
    qtbot.mouseClick(window.centralWidget().viewport(), QtCore.Qt.LeftButton, pos=window.centralWidget().mapFromScene(QtCore.QPoint(0,0)))

    ### Assertion ###
    assert window.visualItemDict['move_test']._ItemTraits['_XYCoordinates'] == [[0,0]]

##################################test for dc_constraint_view##################################
def test_ast_typing(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()


def test_ast_shift(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()


def test_ast_id_double_click(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()


def test_ast_id_highlight(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()


def test_ast_id_delete(qtbot):

    with HiddenConsole():
        window = MainWindow._MainWindow()



