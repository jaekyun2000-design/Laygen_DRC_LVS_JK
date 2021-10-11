import sys, os

from PyQTInterface import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore

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
    assert window.test == True

##################################test for dp creation##################################
def test_boundary_window(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window
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

    qtbot.keyClicks(window.pw.name_input,'path_test')
    window.pw.on_buttonBox_accepted()

    assert window._QTObj._qtProject._DesignParameter['EasyDebugModule']['path_test']
    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('path_test')
    assert window._QTObj._qtProject._DesignConstraint['EasyDebugModule'][dc_id]
    assert window.visualItemDict['path_test']
    assert window.visualItemDict['path_test'] in window.scene.items()


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


def test_text_window(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window
    window.widget_delegator.makeTextWindow()
    qtbot.waitForWindowShown(window.txtw)
    qtbot.keyClicks(window.txtw.name_input, 'text_test')
    qtbot.keyClicks(window.txtw.text_input, 'TEST TEXT WINDOW')
    qtbot.keyClicks(window.txtw.width_input, '100')
    qtbot.keyClicks(window.txtw.XY_input, '0,0')

    assert window._QTObj._qtProject._DesignParameter['EasyDebugModule']['text_test']
    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('text_test')
    assert window._QTObj._qtProject._DesignConstraint['EasyDebugModule'][dc_id]
    assert window.visualItemDict['text_test']
    assert window.visualItemDict['text_test'] in window.scene.items()


def test_pin_window(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window
    window.widget_delegator.makePinWindow()
    qtbot.waitForWindowShown(window.pinw)
    qtbot.keyClicks(window.pinw.name_input, 'pin_test')
    qtbot.keyClicks(window.pinw.layer_input, 'METAL1PIN')
    qtbot.keyClicks(window.pinw.text_input, 'METAL1PIN_test')
    qtbot.keyClicks(window.pinw.width_input, '100')
    qtbot.keyClicks(window.pinw.XY_input, '0,0')

    assert window._QTObj._qtProject._DesignParameter['EasyDebugModule']['pin_test']
    dc_id = window._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id('pin_test')
    assert window._QTObj._qtProject._DesignConstraint['EasyDebugModule'][dc_id]
    assert window.visualItemDict['pin_test']
    assert window.visualItemDict['pin_test'] in window.scene.items()



##################################test for dc creation##################################
def test_create_pycode(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_create_ast(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_create_element(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_create_XYCalculator(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


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


def test_paring_after_dc_creation(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_paring_after_project_load(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_paring_after_gds_load(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_paring_after_create_submodule(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_paring_after_convert_sref_assign(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_paring_after_convert_create_assign(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


##################################test for scene_visible##################################
def test_visible(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_clickable(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


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
        qtbot.addWidget(window)
        qtbot.waitForWindowShown(window)
    test_boundary_window(qtbot)
    test_path_window(qtbot)
    test_sref_window(qtbot)
    file_name = './PyQTInterface/Project/test_project'
    window.saveProject(file_name)

    assert window.test



# def test_project_load(qtbot):
#     global window
#     with HiddenConsole():
#         if window:
#             window.close()
#         window = MainWindow._MainWindow()
#         qtbot.addWidget(window)
#         qtbot.waitForWindowShown(window)
#     file_name = './PyQTInterface/Project/test_project.bin'
#     window.loadProject(file_name)
#     assert window.test

def test_load_gds(qtbot):
    global window
    with HiddenConsole():
        if window:
            window.close()
        window = MainWindow._MainWindow()
        qtbot.addWidget(window)
        qtbot.waitForWindowShown(window)
    import user_setup
    if user_setup._Technology != 'SS28nm':
        window.request_change_process(None, 'SS28nm')
    user_setup.MULTI_THREAD = False
    file_name = './PyQTInterface/GDSFile/RX_term_resistor_v2.gds'
    window.loadGDS(test=file_name)
    assert len(window._QTObj._qtProject._DesignParameter['RX_term_resistor_v2']) == 118
    assert len(window._QTObj._qtProject._DesignConstraint['RX_term_resistor_v2']) == 118
    assert len(window.scene.items()) == 2640



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
def test_module_shift(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window

def test_module_create(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window

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
        window = MainWindow._MainWindow() if not window else window


def test_inspect_path(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_technology_node_change(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


def test_create_submodule_from_sref(qtbot):
    global window
    with HiddenConsole():
        window = MainWindow._MainWindow() if not window else window


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



