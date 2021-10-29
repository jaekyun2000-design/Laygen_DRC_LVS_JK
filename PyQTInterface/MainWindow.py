import os
dir_check=os.getcwd()
if 'PyQTInterface' in dir_check:
    os.chdir('..')

import tracemalloc
snapshot = None
tracemalloc.start()
def trace_memeory():
    global snapshot
    if not snapshot:
        snapshot = tracemalloc.take_snapshot()
    else:
        lines =[]
        top_stats = tracemalloc.take_snapshot().compare_to(snapshot, 'lineno')
        # for stat in top_stats[:10]:
        #     lines.append(str(stat))
        lines.extend([str(stat) for stat in top_stats[:10]])
        print('\n'.join(lines), flush=True)
trace_memeory()


import ast
import sys
import platform
import time

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import traceback
import warnings

import PyCodes.file_save

try:
    sys.path.append('./powertool')
    import topAPI
except:
    traceback.print_exc()
    sys.stderr.write("topAPI support failed\n")
    print("GDS2GEN topAPI module does not exist.")

import multiprocessing as mp
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsView, QGraphicsScene, QGraphicsItem
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


from PyQTInterface import userDefineExceptions
from PyQTInterface import SetupWindow
from PyQTInterface import template
from PyQTInterface.layermap import LayerReader
from PyCodes import QTInterfaceWithAST
from PyCodes import ASTmodule
from PyCodes import element_ast, variable_ast
from DesignManager.ElementManager import element_manager
from DesignManager.VariableManager import FilterPractice
from DesignManager.VariableManager import variable_manager
from PyQTInterface.delegator import delegator
from PyQTInterface.delegator import interface_delegator
from PyQTInterface.delegator import dpdc_delegator
from PyQTInterface.delegator import transfer_delegator

import threading
import re
from PyQTInterface import LayerInfo
from PyQTInterface import VisualizationItem
from PyQTInterface import VariableVisualItem
from PyQTInterface import variableWindow
from PyQTInterface import list_manager
from PyQTInterface import calculator
from PyQTInterface import ConditionalStatement

from generatorLib import generator_model_api
from generatorLib import DRC

##for easy debug##
import json

import copy
import astunparse

##################
import user_setup
DEBUG = user_setup.DEBUG
subnanoMinimumScale =5 # 5 means(default)
subnanoViewScale = 1  #
                      # 1 means(default): coordinates default unit is 1nm,
                      # 0.1 means: coordinates default unit is 0.1nm
                      # 10 means: coordinates default unit is 10nm
EasyDebugFileName = ''

class _MainWindow(QMainWindow):

    send_progressMaximum_signal = pyqtSignal(int)
    send_progressMinimum_signal = pyqtSignal(int)
    send_progressValue_signal = pyqtSignal(int)
    send_callThread_signal = pyqtSignal()
    send_visibleGenState_signal = pyqtSignal(int, list)
    send_visibleCanState_signal = pyqtSignal(int, list)
    send_width_height_ast_signal = pyqtSignal(str, ast.AST)
    send_sref_param_signal = pyqtSignal(str, ast.AST)
    send_tech_node_changed_signal = pyqtSignal()
    send_init_signal = pyqtSignal()

    def __init__(self):
        self.test = False
        super(_MainWindow, self).__init__()
        self.setStyleSheet("border-color: rgb(178, 41, 100)")
        self.module_dict= dict()
        self.module_name_list = []
        self.design_delegator = dpdc_delegator.DesignDelegator(self)
        self.widget_delegator = interface_delegator.WidgetDelegator(self)
        self.transfer_delegator = transfer_delegator.TransferDelegator(self)
        self.visualItemDict = dict()
        self._QTObj = QTInterfaceWithAST.QtInterFace()
        self._ProjectName = None
        self._CurrentModuleName = None
        self.gloabal_clipboard = QGuiApplication.clipboard()
        self.bottom_dock_list = list()
        self.initUI()
        self.easyDebugMode()
        self.progrseeBar_unstable = True
        self.variableList = []
        self._ASTapi = ASTmodule._Custom_AST_API()
        self._layerItem = dict()
        self._id_layer_mapping = dict()
        self.dvstate = False
        self._ElementManager = element_manager.ElementManager()
        self.library_manager = generator_model_api
        self._VariableIDwithAST = variable_manager.Variable_IDwithAST()
        self._DummyConstraints = variable_manager.DummyConstraints()
        self.variable_store_list = list()
        self.test = True
        self.send_init_signal.emit()
        self._QTObj._qtProject._ElementManager.signal.dp_name_update_signal.connect(
            self.design_delegator.update_vs_item_dict
        )

    def reset(self):
        self.module_dict = dict()
        self.module_name_list = []
        self._ElementManager = element_manager.ElementManager()
        self.design_delegator = dpdc_delegator.DesignDelegator(self)
        self.widget_delegator = interface_delegator.WidgetDelegator(self)
        self.transfer_delegator = transfer_delegator.TransferDelegator(self)
        self._QTObj = QTInterfaceWithAST.QtInterFace()
        self._ProjectName = None
        self._CurrentModuleName = None
        self.gloabal_clipboard = QGuiApplication.clipboard()
        self.bottom_dock_list = list()
        self.easyDebugMode()
        self.visualItemDict = dict()
        self.variableList = []
        self._ASTapi = ASTmodule._Custom_AST_API()
        self._layerItem = dict()
        self._id_layer_mapping = dict()
        self.dvstate = False
        self._ElementManager = element_manager.ElementManager()
        self._VariableIDwithAST = variable_manager.Variable_IDwithAST()
        self._DummyConstraints = variable_manager.DummyConstraints()
        self.variable_store_list = list()
        self.test = False
        self.dockContentWidget3.model.clear()
        self.dockContentWidget3_2.model.clear()
        self.scene.clear()
        VisualizationItem._VisualizationItem._compareLayer = dict()
        VisualizationItem._VisualizationItem._subElementLayer = dict()
        for layer in LayerReader._LayerMapping:
            VisualizationItem._VisualizationItem._subElementLayer[layer] = list()
        VisualizationItem._VisualizationItem._subElementLayer['SRef'] = list()
        self.close()

    def vsitem_dict_initialization(self):
        VisualizationItem._VisualizationItem._compareLayer = dict()
        VisualizationItem._VisualizationItem._subElementLayer = dict()
        for layer in LayerReader._LayerMapping:
            VisualizationItem._VisualizationItem._subElementLayer[layer] = list()
        VisualizationItem._VisualizationItem._subElementLayer['SRef'] = list()

    def initUI(self):

        print("***************************Initializing Graphic Interface Start")

        ################# MAIN WINDOW setting ####################
        self.setWindowTitle("S2S GUI PROJECT")
        # self.move(500,100)
        WIDTH = 1920
        LENGTH = 1080
        desktop = QApplication.desktop()
        screenWidth = desktop.width()
        screenLength = desktop.height()
        x = (screenWidth-WIDTH)
        y = (screenLength-LENGTH)
        self.move(50,100)
        self.resize(WIDTH,LENGTH)
        self.show()

        ################# Menu Bar setting ####################

        #First Menu#
        newAction = QAction("New Project",self)
        loadAction = QAction("Load Project",self)
        saveAction = QAction("Save Project",self)
        DebugAction = QAction("Debug constraint",self)
        EncodeAction = QAction("Encode constraint",self)
        RunGDSAction = QAction("Run constraint",self)
        UpdateGDSAction = QAction("Update constraint",self)
        setup_action = QAction("Setup",self)

        # newAction.setShortcut('Ctrl+N')
        # newAction.triggered.connect(self.newProject)

        loadAction.setShortcut('Ctrl+L')
        loadAction.triggered.connect(self.loadProject)

        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.saveProject)

        DebugAction.setShortcut('Ctrl+D')
        DebugAction.triggered.connect(self.debugConstraint)

        EncodeAction.setShortcut('Ctrl+E')
        EncodeAction.triggered.connect(self.encodeConstraint)

        RunGDSAction.setShortcut('Ctrl+R')
        RunGDSAction.triggered.connect(self.runConstraint)

        UpdateGDSAction.setShortcut('Ctrl+U')
        UpdateGDSAction.triggered.connect(self.runConstraint_for_update)

        newAction.setShortcut('Ctrl+C')
        newAction.triggered.connect(self.create_generator_file)

        setup_action.triggered.connect(self.run_setup_update)



        menubar = self.menuBar()
        # menubar.setStyleSheet("background-color: rgb(178, 41, 100)")
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&Project')
        fileMenu.addAction(newAction)
        fileMenu.addAction(loadAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(DebugAction)
        fileMenu.addAction(EncodeAction)
        fileMenu.addAction(RunGDSAction)
        fileMenu.addAction(UpdateGDSAction)
        fileMenu.addAction(setup_action)

        #Second Menu#
        self.statusBar().showMessage("No Module")

        newModuleAction         = QAction("New Module",self)
        moduleManagementAction  = QAction("Module List",self)
        loadGDSAction           = QAction("Load GDS File As a Module",self)
        loadPyCodeAction        = QAction("Load Python source code as Constraint",self)

        newModuleAction.setShortcut('Ctrl+M')
        newModuleAction.triggered.connect(self.show_module_window)

        loadGDSAction.setShortcut('Ctrl+G')
        loadGDSAction.triggered.connect(self.loadGDS)

        loadPyCodeAction.triggered.connect(self.loadPy)

        moduleManagementAction.setShortcut('Ctrl+0')
        moduleManagementAction.triggered.connect(self.moduleManage)

        self.module_name_list = []
        self.module_dict = {self._CurrentModuleName: self} if self._CurrentModuleName else dict()
        self.entireHierarchy = dict()
        self.original_fcn_name = "CalculateDesignParameter"
        self.element_parameter_dict = dict()

        moduleMenu = menubar.addMenu("&Module")
        # self.moduleListSubMenu = moduleMenu.addMenu('&Module List')


        moduleMenu.addAction(newModuleAction)
        moduleMenu.addAction(moduleManagementAction)
        moduleMenu.addAction(loadGDSAction)
        moduleMenu.addAction(loadPyCodeAction)


        #Third Menu
        trace_memory_action = QAction("Inspect memeory (Debuggin)", self)
        auto_array_action = QAction("Inspect array", self)
        auto_pathpoint_action = QAction("Inspect path point", self)
        auto_tech_process_change_action = QAction("Change technology node", self)
        create_sub_module_action = QAction("create sub module from sref", self)

        trace_memory_action.setShortcut('Ctrl+5')
        trace_memory_action.triggered.connect(trace_memeory)

        auto_array_action.setShortcut('Ctrl+1')
        auto_array_action.triggered.connect(self.inspect_array)

        auto_pathpoint_action.setShortcut('Ctrl+2')
        auto_pathpoint_action.triggered.connect(self.inspect_path_point)

        auto_tech_process_change_action.setShortcut('Ctrl+3')
        auto_tech_process_change_action.triggered.connect(self.change_process)

        create_sub_module_action.setShortcut('Ctrl+9')
        create_sub_module_action.triggered.connect(self.create_submodule_by_sref)

        automation_menu = menubar.addMenu("&Automation")
        automation_menu.setObjectName("top_menu_widget")
        automation_menu.addAction(trace_memory_action)
        automation_menu.addAction(auto_array_action)
        automation_menu.addAction(auto_pathpoint_action)
        automation_menu.addAction(auto_tech_process_change_action)
        automation_menu.addAction(create_sub_module_action)

        # automation_menu.setStyleSheet("background-color: rgb(178, 41, 100)")
        # self.setStyleSheet("background-color: rgb(178, 41, 100)")




        # fileMenu.addAction(exitAction)


        ################# Graphics View, Scene setting ####################
        self.scene = _CustomScene()
        graphicView = _CustomView()
        self.variableVisual = VariableVisualItem.VariableVisualItem()
        graphicView.setScene(self.scene)
        graphicView.setRubberBandSelectionMode(Qt.ContainsItemShape)
        graphicView.setDragMode(QGraphicsView.RubberBandDrag)
        graphicView.setAcceptDrops(True)
        graphicView.name_list_signal.connect(self.save_clipboard)
        self.scene.send_module_name_list_signal.connect(graphicView.name_out_fcn)
        self.scene.setItemIndexMethod(QGraphicsScene.NoIndex)
        self.scene.setMinimumRenderSize(5)
        graphicView.centerOn(QPointF(268,-165))
        self.setCentralWidget(graphicView)
        color = Qt.black if user_setup._Night_mode else Qt.white
        self.scene.setBackgroundBrush(QBrush(color))
        graphicView.scale(1,-1)
        graphicView.setInteractive(True)

        graphicView.variable_signal.connect(self.createVariable)
        graphicView.send_widget_message.connect(self.widget_delegator.message_delivery)
        graphicView.send_design_message.connect(self.design_delegator.message_delivery)
        self.scene.setSceneRect(-1000000,-1000000,2000000,2000000)
        self.scene.send_parameterIDList_signal.connect(self.parameterToTemplateHandler)
        self.scene.send_deleteItem_signal.connect(self.deleteDesignParameter)
        self.scene.selectionChanged.connect(self.scene.send_item_list)
        self.scene.send_show_variable_signal.connect(self.variableVisual.toggleVariableVisualization)
        self.scene.send_move_item_signal.connect(self.transfer_delegator.get_xy_difference)
        self.scene.send_mouse_move_xy_signal.connect(self.transfer_delegator.get_mouse_point)
        self.scene.send_xy_signal.connect(self.transfer_delegator.get_click_point)

        ################# Right Dock Widget setting ####################
        self.dockWidget1 = QDockWidget("Element")
        self.dockWidget1.setMaximumHeight(400)
        dockWidget1_1 = QDockWidget("Layer")
        layoutWidget = QWidget()
        dockContentWidget1 = QWidget()
        # self.dockContentWidget1_2 = list_manager._ManageList()
        self.dockContentWidget1_2 = list_manager.LayerManager()

        boundaryButton = QPushButton("Boundary")
        # boundaryButton.clicked.connect(self.makeBoundaryWindow)
        boundaryButton.clicked.connect(self.widget_delegator.make_boundary_window)

        polygonButton = QPushButton("Polygon")
        polygonButton.clicked.connect(self.widget_delegator.make_polygon_window)

        pathButton = QPushButton("Path",dockContentWidget1)
        pathButton.clicked.connect(self.widget_delegator.makePathWindow)

        srefButtonL = QPushButton("SRefLoad",dockContentWidget1)
        srefButtonL.clicked.connect(self.widget_delegator.loadSRefWindow)

        TextButton = QPushButton("Text",dockContentWidget1)
        TextButton.clicked.connect(self.widget_delegator.makeTextWindow)

        PinButton = QPushButton("Pin",dockContentWidget1)
        PinButton.clicked.connect(self.widget_delegator.makePinWindow)

        ElemntClickCheckBox = QCheckBox("Element",dockContentWidget1)
        SrefClickCheckBox = QCheckBox("Sref",dockContentWidget1)
        VariableClickCheckBox = QCheckBox("Variable",dockContentWidget1)

        GeneratorCheckBox = QCheckBox("Generator", dockContentWidget1)
        GeneratorCheckBox.setCheckState(2)
        self.send_visibleGenState_signal.connect(self.dockContentWidget1_2.layer_table_widget.visibleGenState)
        GeneratorCheckBox.stateChanged.connect(self.visibleGenerator)

        CandidateCheckBox = QCheckBox("Candidate", dockContentWidget1)
        CandidateCheckBox.setCheckState(2)
        self.send_visibleCanState_signal.connect(self.dockContentWidget1_2.layer_table_widget.visibleCanState)
        CandidateCheckBox.stateChanged.connect(self.visibleCandidate)

        blackmode_box = QCheckBox("Night Mode", dockContentWidget1)
        state = 2 if user_setup._Night_mode else 0
        blackmode_box.setCheckState(state)
        blackmode_box.stateChanged.connect(self.scene.change_background)

        X_label = QLabel('X:')
        X_value = QLineEdit()
        X_value.setMaximumWidth(40)
        X_value.setMinimumWidth(40)
        X_value.setReadOnly(True)

        Y_label = QLabel('Y:')
        Y_value = QLineEdit()
        Y_value.setMaximumWidth(40)
        Y_value.setMinimumWidth(40)
        Y_value.setReadOnly(True)

        def get_mouse(xy):
            X = xy[0]
            Y = xy[1]

            X_value.setText(str(X))
            Y_value.setText(str(Y))
            XY = str(X) + ',' + str(Y)
            self.statusBar().showMessage(XY)

        self.scene.send_mouse_move_xy_signal.connect(get_mouse)

        def change_snap_mode():
            if user_setup._Snap_mode == 'orthogonal':
                user_setup._Snap_mode = 'any_angle'
            elif user_setup._Snap_mode == 'any_angle':
                user_setup._Snap_mode = 'orthogonal'
            snap_option_button.setText(user_setup._Snap_mode)

        snap_option_button = QPushButton()
        snap_option_button.setText(user_setup._Snap_mode)
        snap_option_button.clicked.connect(change_snap_mode)

        ########## Second tab ############
        self.dv = variableWindow._DesignVariableManagerWindow(dict())
        self.dvstate = True
        self.dv.send_variable_siganl.connect(self.createNewConstraintAST)
        self.dv.send_changedData_signal.connect(self.updateVariableConstraint)
        self.dv.selected_variable_item_id_signal.connect(self.highlightVI)
        self.dv.send_id_in_edited_variable_signal.connect(self.transfer_delegator.change_used_variable_name)

        vboxOnDock1 = QVBoxLayout()             # Layout For Button Widget

        vboxOnDock1.addStretch(10)
        vboxOnDock1.addWidget(boundaryButton)
        vboxOnDock1.addWidget(polygonButton)
        vboxOnDock1.addWidget(pathButton)
        vboxOnDock1.addWidget(srefButtonL)
        vboxOnDock1.addWidget(TextButton)
        vboxOnDock1.addWidget(PinButton)
        vboxOnDock1.addStretch(2)
        hboxOnDock1 = QHBoxLayout()
        hboxOnDock2 = QHBoxLayout()
        hboxOnDock3 = QHBoxLayout()
        hboxOnDock1.addWidget(ElemntClickCheckBox)
        hboxOnDock1.addWidget(SrefClickCheckBox)
        hboxOnDock1.addWidget(VariableClickCheckBox)
        hboxOnDock2.addWidget(GeneratorCheckBox)
        hboxOnDock2.addStretch(2)
        hboxOnDock2.addWidget(CandidateCheckBox)
        hboxOnDock3.addSpacing(20)
        hboxOnDock3.addWidget(X_label)
        hboxOnDock3.addWidget(X_value)
        hboxOnDock3.addSpacing(60)
        hboxOnDock3.addWidget(Y_label)
        hboxOnDock3.addWidget(Y_value)
        hboxOnDock3.addSpacing(20)
        vboxOnDock1.addLayout(hboxOnDock1)
        vboxOnDock1.addLayout(hboxOnDock2)
        vboxOnDock1.addWidget(blackmode_box)
        vboxOnDock1.addLayout(hboxOnDock3)
        vboxOnDock1.addWidget(snap_option_button)
        vboxOnDock1.addStretch(10)

        dockContentWidget1.setLayout(vboxOnDock1)

        gridOnDock1 = QHBoxLayout()
        gridOnDock1.addWidget(dockContentWidget1)

        layoutWidget.setLayout(gridOnDock1)
        self.dockWidget1.setWidget(layoutWidget)

        dockWidget1_1.setWidget(self.dockContentWidget1_2)

        dockWidget_tab3 = QDockWidget("Variable")
        dockWidget_tab3.setWidget(self.dv)

        self.addDockWidget(Qt.RightDockWidgetArea, self.dockWidget1)
        self.addDockWidget(Qt.RightDockWidgetArea, dockWidget1_1)
        self.addDockWidget(Qt.RightDockWidgetArea, dockWidget_tab3)

        self.tabifyDockWidget(self.dockWidget1, dockWidget1_1)
        self.tabifyDockWidget(dockWidget1_1, dockWidget_tab3)


        ################# Left Dock Widget setting ####################
        dockWidget2 = QDockWidget("Design List")
        self.dockContentWidget2 = SetupWindow._SelectedDesignListWidget()
        self.dockContentWidget2.send_request_visual_item.connect(lambda element_name:
                                                                self.dockContentWidget2.update_item_dict(
                                                                element_name = element_name,
                                                                element= self.visualItemDict[element_name])
                                                                )
        self.scene.send_itemList_signal.connect(self.dockContentWidget2.UpdateCustomItem)       # Show the clicked items list
        self.dockContentWidget2.send_UpdateDesignParameter_signal.connect(self.updateDesignParameter)
        self.dockContentWidget2.send_UpdateDesignAST_signal.connect(self.srefUpdate)
        self.dockContentWidget2.send_parameterIDList_signal.connect(self.parameterToTemplateHandler)
        self.dockContentWidget2.send_deleteItem_signal.connect(self.deleteDesignParameter)
        self.scene.send_parameterIDList_signal.connect(self.dockContentWidget2.ModifyingDesign)

        self.dockContentWidget2.createDummyConstraint = self.createDummyConstraint


        dockWidget2.setWidget(self. dockContentWidget2)
        self.addDockWidget(Qt.LeftDockWidgetArea,dockWidget2)

        dockWidget2_2 = QDockWidget("Modifier")
        self.design_modifier = SetupWindow.DesignModifier()
        dockWidget2_2.setWidget(self.design_modifier)

        self.addDockWidget(Qt.LeftDockWidgetArea,dockWidget2_2)
        self.scene.send_selected_list_signal.connect(lambda items: self.design_modifier.update_form(
            self._QTObj._qtProject._DesignConstraint[self._CurrentModuleName]\
                [self._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id(items[0]._id)]))
        # self.design_modifier.send_update_qt_constraint_signal.connect(lambda target_id, update_dict:
        #                                                               self.design_delegator.update_qt_constraint(
        #                                                                   target_id, updated_dict=update_dict
        #                                                               ))
        # self.design_modifier.send_update_ast_signal.connect(self.srefUpdate)
        self.design_modifier.send_update_ast_signal.connect(lambda _ast: self.design_delegator.update_qt_constraint(
            target_id=_ast._id, updated_ast=_ast
        ))
        self.design_modifier.send_update_ast_signal.connect(lambda _ast: self.runConstraint_for_update(
            code= self.encodeConstraint(_ast)
        ))
        # self.design_modifier.send_update_ast_signal.connect(lambda _ast:
        #                                                     self.design_delegator.control_constraint_tree_view(
        #                                                         _ast._id, channel=3, request='update'
        #                                                     ))

        ################# Bottom Dock Widget setting ####################
        self.bottom_dock_tab_widget = QTabWidget()

        if platform.system() != 'Darwin':
            self.bottom_dock_tab_widget.setStyleSheet('background-color:rgb(240,240,240);')
        self.bottom_dock_tab_widget.currentChanged.connect(self.bottom_dock_tab_changed)

        dockWidget3 = QDockWidget("Design Constraint")
        layoutWidget = QWidget()
        self.dockContentWidget3 = SetupWindow._ConstraintTreeViewWidgetAST("Generator")
        self.dockContentWidget3_2 = SetupWindow._ConstraintTreeViewWidgetAST("Candidate")

        # self.sendDownButton = QPushButton()
        # self.sendDownButton.setIcon(QCommonStyle().standardIcon(QStyle.SP_ArrowDown))
        self.sendLeftButton = QPushButton()
        self.sendLeftButton.setIcon(QCommonStyle().standardIcon(QStyle.SP_ArrowLeft))
        self.sendRightButton = QPushButton()
        self.sendRightButton.setIcon(QCommonStyle().standardIcon(QStyle.SP_ArrowRight))

        # self.sendDownButton.clicked.connect(self.deliveryDesignParameter)

        self.sendLeftButton.clicked.connect(self.dockContentWidget3_2.checkSend)
        self.dockContentWidget3_2.send_SendID_signal.connect(self.dockContentWidget3.receiveConstraintID)
        self.dockContentWidget3_2.send_ReceiveDone_signal.connect(self.dockContentWidget3.removeCurrentIndexItem)
        self.dockContentWidget3_2.send_SendCopyConstraint_signal.connect(self.constraintToTemplateHandler)
        self.dockContentWidget3_2.send_UpdateDesignConstraintID_signal.connect(self.get_constraint_update_design)
        self.dockContentWidget3_2.send_UpdateDesignConstraint_signal.connect(self.constraintUpdate2)
        self.dockContentWidget3_2.send_RequestDesignConstraint_signal.connect(self.constraintConvey)
        self.dockContentWidget3_2.send_deleteConstraint_signal.connect(self.deleteDesignConstraint)
        self.dockContentWidget3_2.send_RequestElementManger_signal.connect(self.convey_element_manager)
        self.dockContentWidget3_2.send_DataChanged_signal.connect(self.constraint_data_changed)
        self.dockContentWidget3_2.send_SendID_signal_highlight.connect(self.get_dc_highlight_dp)
        self.scene.send_parameterIDList_signal.connect(self.dockContentWidget3_2.get_dp_highlight_dc)

        self.sendRightButton.clicked.connect(self.dockContentWidget3.checkSend)
        self.dockContentWidget3.send_SendID_signal.connect(self.dockContentWidget3_2.receiveConstraintID)
        self.dockContentWidget3.send_ReceiveDone_signal.connect(self.dockContentWidget3_2.removeCurrentIndexItem)
        self.dockContentWidget3.send_RootDesignConstraint_signal.connect(self.setRootConstraint)
        self.dockContentWidget3.send_SendCopyConstraint_signal.connect(self.constraintToTemplateHandler)
        self.dockContentWidget3.send_UpdateDesignConstraintID_signal.connect(self.get_constraint_update_design)
        self.dockContentWidget3.send_UpdateDesignConstraint_signal.connect(self.constraintUpdate1)
        self.dockContentWidget3.send_RequestDesignConstraint_signal.connect(self.constraintConvey)
        self.dockContentWidget3.send_deleteConstraint_signal.connect(self.deleteDesignConstraint)
        self.dockContentWidget3.send_RequestElementManger_signal.connect(self.convey_element_manager)
        self.dockContentWidget3.send_DataChanged_signal.connect(self.constraint_data_changed)
        self.dockContentWidget3.send_SendID_signal_highlight.connect(self.get_dc_highlight_dp)
        self.scene.send_parameterIDList_signal.connect(self.dockContentWidget3.get_dp_highlight_dc)

        self.sendLeftButton.clicked.connect(self.dockContentWidget3.clearSelection)
        self.sendLeftButton.clicked.connect(self.dockContentWidget3_2.clearSelection)
        self.sendRightButton.clicked.connect(self.dockContentWidget3.clearSelection)
        self.sendRightButton.clicked.connect(self.dockContentWidget3_2.clearSelection)

        vboxLayout = QVBoxLayout()
        # vboxLayout.addWidget(self.sendDownButton)
        vboxLayout.addStretch(4)
        vboxLayout.addWidget(self.sendLeftButton)
        vboxLayout.addWidget(self.sendRightButton)
        vboxLayout.addStretch(4)

        VBoxForPeriButton = QVBoxLayout()
        # self.createConstraintButton = QPushButton("Create")
        self.createConstraintWithPyCodeButton = QPushButton("PyCode")
        # self.createConstraintButtonASTLegacy = QPushButton("CreateAST(Legacy)")
        self.createConstraintButtonAST = QPushButton("CreateAST")
        self.createConstraintButtonCUSTOM = QPushButton("Element(Custom)")
        self.createVariableButtonCUSTOM = QPushButton("Variable(Custom)")
        # self.saveConstraintAsJSONButton = QPushButton("SaveAs...(JSON)")
        self.saveConstraintAsPickleButton = QPushButton("SaveAs...(pickle)")
        # self.loadConstraintFromPickleButton = QPushButton("Load...")
        # self.ConstraintTemplateButton = QPushButton("Template")
        # self.parsetreeEasyRun = QPushButton("easyRun")
        self.variableCallButton = QPushButton("variableCall")
        self.calculatorButton = QPushButton("XYCalculator")
        self.condition_expression_button = QPushButton("condition exp debug")
        self.conditional_stmt_button = QPushButton("condition stmt debug")
        self.add_constraint_view_button = QPushButton("add constraint view")

        VBoxForPeriButton.addStretch(3)
        # VBoxForPeriButton.addWidget(self.createConstraintButton)
        VBoxForPeriButton.addWidget(self.createConstraintWithPyCodeButton)
        # VBoxForPeriButton.addWidget(self.createConstraintButtonASTLegacy)
        VBoxForPeriButton.addWidget(self.createConstraintButtonAST)
        VBoxForPeriButton.addWidget(self.createConstraintButtonCUSTOM)
        VBoxForPeriButton.addWidget(self.createVariableButtonCUSTOM)
        # VBoxForPeriButton.addWidget(self.saveConstraintAsJSONButton)
        VBoxForPeriButton.addWidget(self.saveConstraintAsPickleButton)
        # VBoxForPeriButton.addWidget(self.loadConstraintFromPickleButton)
        # VBoxForPeriButton.addWidget(self.ConstraintTemplateButton)
        # VBoxForPeriButton.addWidget(self.parsetreeEasyRun)
        VBoxForPeriButton.addWidget(self.variableCallButton)
        VBoxForPeriButton.addWidget(self.calculatorButton)
        VBoxForPeriButton.addWidget(self.condition_expression_button)
        VBoxForPeriButton.addWidget(self.conditional_stmt_button)
        VBoxForPeriButton.addWidget(self.add_constraint_view_button)
        VBoxForPeriButton.addStretch(3)

        # self.dockContentWidget3.setDragDropMode(self.dockContectWidget3.MyOwnDragDropMove)

        widget_for_tab = QWidget()
        hbox_for_tab = QHBoxLayout()
        hbox_for_tab.addWidget(self.dockContentWidget3)
        hbox_for_tab.addLayout(vboxLayout)
        hbox_for_tab.addWidget(self.dockContentWidget3_2)
        widget_for_tab.setLayout(hbox_for_tab)
        self.bottom_dock_tab_widget.addTab(widget_for_tab, 'CalculateDesignParameter')
        if platform.system() != 'Darwin':
            self.dockContentWidget3.setStyleSheet('background-color:rgb(255,255,255);')
            self.dockContentWidget3_2.setStyleSheet('background-color:rgb(255,255,255);')

        gridOnDock3 = QHBoxLayout()
        gridOnDock3.addWidget(self.bottom_dock_tab_widget)
        # gridOnDock3.addWidget(widget_for_tab)
        gridOnDock3.addLayout(VBoxForPeriButton)

        layoutWidget.setLayout(gridOnDock3)
        dockWidget3.setWidget(layoutWidget)

        self.addDockWidget(Qt.BottomDockWidgetArea,dockWidget3)
        # self.createConstraintButton.clicked.connect(self.makeConstraintWindow)
        self.createConstraintWithPyCodeButton.clicked.connect(self.widget_delegator.makePyCodeWindow)
        self.createConstraintButtonAST.clicked.connect(self.widget_delegator.makeConstraintWindowAST)
        self.createConstraintButtonCUSTOM.clicked.connect(self.widget_delegator.makeConstraintWindowCUSTOM)
        self.createVariableButtonCUSTOM.clicked.connect(self.widget_delegator.makeVariableWindowCUSTOM)
        # self.saveConstraintAsJSONButton.clicked.connect(self.saveConstraint)
        self.saveConstraintAsPickleButton.clicked.connect(self.saveConstraintP)
        # self.loadConstraintFromPickleButton.clicked.connect(self.loadConstraintP)
        # self.ConstraintTemplateButton.clicked.connect(self.makeTemplateWindow)
        # self.parsetreeEasyRun.clicked.connect(self.easyRun)
        self.variableCallButton.clicked.connect(self.variableListUpdate)
        self.calculatorButton.clicked.connect(self.calculator)
        self.condition_expression_button.clicked.connect(self.condition_expression)
        self.conditional_stmt_button.clicked.connect(self.condition_stmt)
        self.add_constraint_view_button.clicked.connect(self.add_constraint_view)

        ##################Extra widget initialization #########################
        self.calculator_window = calculator.ExpressionCalculator(clipboard=self.gloabal_clipboard, purpose='init')
        self.calculator_window.send_dummyconstraints_signal.connect(self.calculator_window.storePreset)
        self.scene.send_xyCoordinate_signal.connect(self.calculator_window.waitForClick)
        self.calculator_window.returnLayer_signal.connect(self.get_hierarchy_return_layer)
        self.calculator_window.send_XYCreated_signal.connect(self.createDummyConstraint)
        self.send_tech_node_changed_signal.connect(self.calculator_window.get_drc_dict)

        self.vw = variableWindow.VariableSetupWindow(variable_type="boundary_array")
        self.vw.send_output_dict_signal.connect(self.create_variable)
        self.vw.send_DestroyTmpVisual_signal.connect(self.deleteDesignParameter)
        self.vw.request_dummy_constraint_signal.connect(self.delivery_dummy_constraint)
        self.vw.send_clicked_item_signal.connect(self.highlightVI_by_hierarchy_list)
        self.vw.variable_widget.send_exported_width_height_signal.connect(self.createDummyConstraint)
        self.vw.send_variable_signal.connect(self.send_array_variable)

        self.conditional_stmt_window = ConditionalStatement.ConditionStmtWidget()
        self.condition_expression_window = ConditionalStatement.ConditionExpressionWidget()

        self.dockContentWidget3.send_dummy_ast_id_for_xy_signal.connect(self.calculator_window.getXY)
        self.dockContentWidget3_2.send_dummy_ast_id_for_xy_signal.connect(self.calculator_window.getXY)
        self.dockContentWidget3.send_dummy_ast_id_for_array_signal.connect(self.vw.update_ui_by_constraint_id)
        self.dockContentWidget3_2.send_dummy_ast_id_for_array_signal.connect(self.vw.update_ui_by_constraint_id)
        self.dockContentWidget3.send_dummy_ast_id_for_condition_signal.connect(self.conditional_stmt_window.show_list)
        self.dockContentWidget3_2.send_dummy_ast_id_for_condition_signal.connect(self.conditional_stmt_window.init_ui)

        ################ Logging Message Dock Widget setting ####################
        dockWidget4ForLoggingMessage = QDockWidget("Logging Message")
        self.dockContentWidget4ForLoggingMessage = SetupWindow._LogMessageWindow()
        self.dockContentWidget4ForLoggingMessage._InfoMessage("MakeProject")
        dockWidget4ForLoggingMessage.setWidget(self.dockContentWidget4ForLoggingMessage)
        # self.addDockWidget(Qt.BottomDockWidgetArea, dockWidget4ForLoggingMessage)

        print("******************************Initializing Graphic Interface Complete")

    def create_generator_file(self):
        library_list = []
        additional_import_code = ''
        constraint_names = self.dockContentWidget3.model.findItems('', Qt.MatchContains, 1)
        constraint_ids = [item.text() for item in constraint_names]
        for ids in constraint_ids:
            single_module = self._QTObj._qtProject._DesignConstraint[self._CurrentModuleName][ids]
            module_lib = single_module._ast.__dict__['library']
            library_list.append(module_lib)
        cal_code = self.encodeConstraint()
        cal_code = f"\n_DRCObj = DRC.DRC()\n" \
                   f"_Name = '{self._CurrentModuleName}'\n" \
                   f"{cal_code}"
        import_default_code = "from generatorLib import StickDiagram\n" \
                              "from generatorLib import DesignParameters\n" \
                              "import copy\n" \
                              "from generatorLib import DRC\n"
        # for libraries in library_list:
        #     additional_import_code += f"from generatorLib.generator_models import {libraries}\n"
        from functools import reduce
        if library_list != []:
            reduce(lambda additional_import_code, libraries: additional_import_code + f"from generatorLib.generator_models import {libraries}\n", library_list)

        import_code = import_default_code + additional_import_code + '\n'
        class_declaration_code = f"class {self._CurrentModuleName}(StickDiagram._StickDiagram):\n" \
                                 f"\tdef __init__(self, _DesignParameter=None, _Name='{self._CurrentModuleName}'):\n" \
                                 f"\t\tif _DesignParameter != None:\n" \
                                 f"\t\t\tself._DesignParameter = _DesignParameter\n" \
                                 f"\t\telse:\n" \
                                 f"\t\t\tself._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))\n"
        self.user_variables = variableWindow._createNewDesignVariable.variableDict.values()
        user_variable_sentence = ",".join(
            [f'{variable_dict["DV"]}={variable_dict["value"] if variable_dict["value"] != "" else None}' for
             variable_dict in self.user_variables])
        fcn_define_code = '\tdef _CalculateDesignParameter(self,' + user_variable_sentence + '):\n'
        cal_code = re.sub("\n","\n\t\t",cal_code)
        final_code = import_code + class_declaration_code + fcn_define_code + f"\t{cal_code}"

        self.writing_flag = QMessageBox()
        reply = self.writing_flag.question(self,"QMessageBox", "Save code as a Generator File?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            file_write_flag = True
        elif reply == QMessageBox.No:
            file_write_flag = False

        if file_write_flag:
            f = open(f"./generatorLib/generator_models/{self._CurrentModuleName}.py", "w")
            f.write(final_code)
            f.close()

    def create_new_window(self, dict, key):
        dict[key] = _MainWindow()

    def create_submodule_by_sref(self, test=None):
        selected_items = self.scene.selectedItems()
        if len(selected_items) != 1:
            self.warning = QMessageBox()
            self.warning.setText("Select Only One Item")
            self.warning.show()
        else:
            # for selected_item in selected_items:
            #     tmp_module_name = selected_item._ElementName
            selected_item = selected_items[0]
            tmp_module_name = selected_item._ElementName

            if selected_item._ItemTraits['_DesignParametertype'] != 3:
                self.warning = QMessageBox()
                self.warning.setText("Select SRef Item")
                self.warning.show()
            else:

                # tmp_module_name = 'test'
                self.module_name_list.append(tmp_module_name)
                self.module_dict[tmp_module_name] = _MainWindow()
                new_project = self.module_dict[tmp_module_name]
                selected_qt_dp = copy.deepcopy(
                    self._QTObj._qtProject._DesignParameter[self._CurrentModuleName][tmp_module_name])
                new_project._QTObj._qtProject._DesignParameter = {tmp_module_name:selected_qt_dp._DesignParameter['_ModelStructure']}


                self.module_dict[tmp_module_name].set_module_name(tmp_module_name)
                # self.module_dict[tmp_module_name].show()
                self.module_dict[tmp_module_name].module_dict = self.module_dict
                self.module_dict[tmp_module_name].module_name_list = self.module_name_list

                hierarchy_key = selected_qt_dp._DesignParameter['_DesignObj_Name'] + '/' + tmp_module_name
                if len(self.entireHierarchy) == 0:
                    """
                    case when sref load is used (not load gds!)
                    """
                    hierarchy = new_project._QTObj._qtProject._getEntireHierarchy()

                else:
                    if self.entireHierarchy[self._CurrentModuleName][hierarchy_key] is None:
                        hierarchy = {tmp_module_name : dict()}
                    else:
                        hierarchy = {tmp_module_name : self.entireHierarchy[self._CurrentModuleName][hierarchy_key]}
                new_project.create_dc_vi_from_top_dp(hierarchy, test)
                self.hide()

        # print('send!')
        # self.send_create_new_window_signal.emit()
        # print('send end')
    def add_constraint_view(self):
        self.add_constraint_view_flag = True
        self.c_view_configuration = QWidget()
        config_list = ['Fcn Name']
        fcn_str = QLineEdit()
        form_layout = QFormLayout()
        # for config_item in config_list:
        #     form_layout.addRow(config_item, fcn_str)
        list(map(lambda config_item: form_layout.addRow(config_item, fcn_str), config_list))

        cb = QComboBox(self.c_view_configuration)
        cb.addItem('from DP')
        cb.addItem('from original DC')

        ok_button = QPushButton()
        ok_button.setText('OK')

        form_layout.addRow('Options', cb)
        form_layout.addRow(' ', ok_button)

        self.c_view_configuration.setLayout(form_layout)
        self.c_view_configuration.show()

        ok_button.clicked.connect(lambda tmp: self.create_new_constraint_widget(cb.currentText(), fcn_str.text()))

    def create_new_bottom_dock_widget(self, fcn_name):
        self.dockContentWidget3.blockSignals(True)
        self.dockContentWidget3_2.blockSignals(True)

        self.dockContentWidget3 = SetupWindow._ConstraintTreeViewWidgetAST("Generator")
        self.dockContentWidget3_2 = SetupWindow._ConstraintTreeViewWidgetAST("Candidate")

        self.sendDownButton = QPushButton()
        self.sendDownButton.setIcon(QCommonStyle().standardIcon(QStyle.SP_ArrowDown))
        self.sendLeftButton = QPushButton()
        self.sendLeftButton.setIcon(QCommonStyle().standardIcon(QStyle.SP_ArrowLeft))
        self.sendRightButton = QPushButton()
        self.sendRightButton.setIcon(QCommonStyle().standardIcon(QStyle.SP_ArrowRight))

        self.sendDownButton.clicked.connect(self.deliveryDesignParameter)

        self.sendLeftButton.clicked.connect(self.dockContentWidget3_2.checkSend)
        self.dockContentWidget3_2.send_SendID_signal.connect(self.dockContentWidget3.receiveConstraintID)
        self.dockContentWidget3_2.send_ReceiveDone_signal.connect(self.dockContentWidget3.removeCurrentIndexItem)
        self.dockContentWidget3_2.send_SendCopyConstraint_signal.connect(self.constraintToTemplateHandler)
        self.dockContentWidget3_2.send_UpdateDesignConstraintID_signal.connect(self.get_constraint_update_design)
        self.dockContentWidget3_2.send_UpdateDesignConstraint_signal.connect(self.constraintUpdate2)
        self.dockContentWidget3_2.send_RequestDesignConstraint_signal.connect(self.constraintConvey)
        self.dockContentWidget3_2.send_deleteConstraint_signal.connect(self.deleteDesignConstraint)
        self.dockContentWidget3_2.send_RequestElementManger_signal.connect(self.convey_element_manager)
        self.dockContentWidget3_2.send_DataChanged_signal.connect(self.constraint_data_changed)
        self.dockContentWidget3_2.send_SendID_signal_highlight.connect(self.get_dc_highlight_dp)
        self.scene.send_parameterIDList_signal.connect(self.dockContentWidget3_2.get_dp_highlight_dc)

        self.sendRightButton.clicked.connect(self.dockContentWidget3.checkSend)
        self.dockContentWidget3.send_SendID_signal.connect(self.dockContentWidget3_2.receiveConstraintID)
        self.dockContentWidget3.send_ReceiveDone_signal.connect(self.dockContentWidget3_2.removeCurrentIndexItem)
        self.dockContentWidget3.send_RootDesignConstraint_signal.connect(self.setRootConstraint)
        self.dockContentWidget3.send_SendCopyConstraint_signal.connect(self.constraintToTemplateHandler)
        self.dockContentWidget3.send_UpdateDesignConstraintID_signal.connect(self.get_constraint_update_design)
        self.dockContentWidget3.send_UpdateDesignConstraint_signal.connect(self.constraintUpdate1)
        self.dockContentWidget3.send_RequestDesignConstraint_signal.connect(self.constraintConvey)
        self.dockContentWidget3.send_deleteConstraint_signal.connect(self.deleteDesignConstraint)
        self.dockContentWidget3.send_RequestElementManger_signal.connect(self.convey_element_manager)
        self.dockContentWidget3.send_DataChanged_signal.connect(self.constraint_data_changed)
        self.dockContentWidget3.send_SendID_signal_highlight.connect(self.get_dc_highlight_dp)
        self.scene.send_parameterIDList_signal.connect(self.dockContentWidget3.get_dp_highlight_dc)

        self.sendLeftButton.clicked.connect(self.dockContentWidget3.clearSelection)
        self.sendLeftButton.clicked.connect(self.dockContentWidget3_2.clearSelection)
        self.sendRightButton.clicked.connect(self.dockContentWidget3.clearSelection)
        self.sendRightButton.clicked.connect(self.dockContentWidget3_2.clearSelection)

        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(self.sendDownButton)
        vboxLayout.addStretch(3)
        vboxLayout.addWidget(self.sendLeftButton)
        vboxLayout.addWidget(self.sendRightButton)
        vboxLayout.addStretch(4)

        widget_for_tab = QWidget()
        hbox_for_tab = QHBoxLayout()
        hbox_for_tab.addWidget(self.dockContentWidget3)
        hbox_for_tab.addLayout(vboxLayout)
        hbox_for_tab.addWidget(self.dockContentWidget3_2)
        widget_for_tab.setLayout(hbox_for_tab)
        idx = self.bottom_dock_tab_widget.addTab(widget_for_tab, fcn_name)
        if platform.system() != 'Darwin':
            self.dockContentWidget3.setStyleSheet('background-color:rgb(255,255,255);')
            self.dockContentWidget3_2.setStyleSheet('background-color:rgb(255,255,255);')
        self.bottom_dock_tab_widget.setCurrentIndex(idx)

    def bottom_dock_tab_changed(self, idx):
        # for tab_idx in range(self.bottom_dock_tab_widget.count()):
        #     self.bottom_dock_tab_widget.widget(tab_idx).layout().itemAt(0).widget().blockSignals(True)
        #     self.bottom_dock_tab_widget.widget(tab_idx).layout().itemAt(2).widget().blockSignals(True)
        list(map(lambda tab_idx: self.bottom_dock_tab_widget.widget(tab_idx).layout().itemAt(0).widget().blockSignals(True), range(self.bottom_dock_tab_widget.count())))
        list(map(lambda tab_idx: self.bottom_dock_tab_widget.widget(tab_idx).layout().itemAt(2).widget().blockSignals(True), range(self.bottom_dock_tab_widget.count())))

        self.dockContentWidget3 = self.bottom_dock_tab_widget.widget(idx).layout().itemAt(0).widget()
        self.dockContentWidget3_2 = self.bottom_dock_tab_widget.widget(idx).layout().itemAt(2).widget()

        self.dockContentWidget3.blockSignals(False)
        self.dockContentWidget3_2.blockSignals(False)
        fcn_name = self.bottom_dock_tab_widget.tabText(idx)
        self.dp_process_bw_tabs(fcn_name)

    def create_new_constraint_widget(self, mode, fcn_name):
        print(f'********************************Creating New Constraint Widget\n'
              f'Adding New Constraint {mode}, function name: \"{fcn_name}\"')
        self.c_view_configuration.destroy()

        if len(self._QTObj._qtProject._DesignConstraint_topology_dict) == 0:
            """
            Creating Second Tab: Add Original Project Information
            """
            self._QTObj._qtProject._DesignConstraint_topology_dict['CalculateDesignParameter'] = copy.deepcopy(self._QTObj._qtProject._DesignConstraint)
            self._QTObj._qtProject._ElementManager_topology_dict['CalculateDesignParameter'] = copy.deepcopy(self._QTObj._qtProject._ElementManager)
            self._QTObj._qtProject._ElementManager_topology_dict['CalculateDesignParameter'].elementParameterDict = copy.deepcopy(self._QTObj._qtProject._DesignParameter[self._CurrentModuleName])
            print("Design Constraints inside first tab is saved inside topology dictionary")
        else:
            self._QTObj._qtProject._DesignConstraint_topology_dict[self.original_fcn_name] = copy.deepcopy(self._QTObj._qtProject._DesignConstraint)
            self._QTObj._qtProject._ElementManager_topology_dict[self.original_fcn_name] = copy.deepcopy(self._QTObj._qtProject._ElementManager)
            self._QTObj._qtProject._ElementManager_topology_dict[self.original_fcn_name].elementParameterDict = copy.deepcopy(self._QTObj._qtProject._DesignParameter[self._CurrentModuleName])
            print(f"Design Constraints inside {self.original_fcn_name} tab is saved inside topology dictionary")

        if len(self._QTObj._qtProject._DesignParameter) == 0:
            self.warning = QMessageBox()
            self.warning.setText("No Elements to copy!")
            self.warning.show()
            return

        constraint_names_gen = self.dockContentWidget3.model.findItems('', Qt.MatchContains, 1)
        constraint_ids_gen = [item.text() for item in constraint_names_gen]

        constraint_names_can = self.dockContentWidget3_2.model.findItems('', Qt.MatchContains, 1)
        constraint_ids_can = [item.text() for item in constraint_names_can]


        self.create_new_bottom_dock_widget(fcn_name)



        if mode == 'from original DC':
            self._QTObj._qtProject._DesignConstraint = copy.deepcopy(self._QTObj._qtProject._DesignConstraint_topology_dict[self.original_fcn_name])
            self._QTObj._qtProject._ElementManager = copy.deepcopy(self._QTObj._qtProject._ElementManager_topology_dict[self.original_fcn_name])
            for dc_id in constraint_ids_can:
                self.dockContentWidget3_2.createNewConstraintAST(_id=dc_id,
                                                             _parentName=self._CurrentModuleName,
                                                             _DesignConstraint=self._QTObj._qtProject._DesignConstraint)
            for dc_id in constraint_ids_gen:
                self.dockContentWidget3.createNewConstraintAST(_id=dc_id,
                                                             _parentName=self._CurrentModuleName,
                                                             _DesignConstraint=self._QTObj._qtProject._DesignConstraint)
        elif mode == 'from DP':
            current_dp_dict = self._QTObj._qtProject._DesignParameter[self._CurrentModuleName]
            for name, dp in current_dp_dict.items():
                tmpAST = self._QTObj._qtProject._ElementManager.get_dp_return_ast(dp)
                if tmpAST == None:
                    continue
                design_dict = self._QTObj._qtProject._feed_design(design_type='constraint',
                                                                  module_name=self._CurrentModuleName,
                                                                  _ast=tmpAST, element_manager_update=False)
                self.dockContentWidget3_2.createNewConstraintAST(_id=design_dict['constraint_id'],
                                                                 _parentName=self._CurrentModuleName,
                                                                 _DesignConstraint=self._QTObj._qtProject._DesignConstraint)
                self._QTObj._qtProject._ElementManager.load_dp_dc_id(dp_id=name,dc_id=design_dict['constraint_id'])

        self.element_parameter_dict = copy.deepcopy(self._QTObj._qtProject._DesignParameter[self._CurrentModuleName])
        self.original_fcn_name = fcn_name

    def dp_process_bw_tabs(self,fcn_name):
        if self._QTObj._qtProject == None or self.add_constraint_view_flag == True:
            self.add_constraint_view_flag = False
            return

        self._QTObj._qtProject._DesignConstraint_topology_dict[self.original_fcn_name] = copy.deepcopy(self._QTObj._qtProject._DesignConstraint)
        self._QTObj._qtProject._ElementManager_topology_dict[self.original_fcn_name] = copy.deepcopy(self._QTObj._qtProject._ElementManager)

        self._QTObj._qtProject._DesignConstraint = self._QTObj._qtProject._DesignConstraint_topology_dict[fcn_name]
        self._QTObj._qtProject._ElementManager = self._QTObj._qtProject._ElementManager_topology_dict[fcn_name]
        print(f"Original {self.original_fcn_name} tab info successfully saved. Process Changed into {fcn_name} tab.")


        original_dp_set = set(list(self.element_parameter_dict.keys()))
        target_dp_set = set(list(self._QTObj._qtProject._DesignParameter[self._CurrentModuleName].keys()))
        if original_dp_set != target_dp_set:
            self.dp_preserve_flag = QMessageBox()
            reply = self.dp_preserve_flag.question(self,"QMessageBox", "Save current DP Information?",
                                                   QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                dp_preserve = True
            elif reply == QMessageBox.No:
                dp_preserve = False

            if dp_preserve:
                print('dp_preserved')
                """
                dp를 preserve할 경우 현재는 있지만 기존에는 없는 dp에 대해서만 dc 생성
                """
                for dp_name, dp in self._QTObj._qtProject._DesignParameter[self._CurrentModuleName].items():
                    if dp_name not in list(self._QTObj._qtProject._ElementManager_topology_dict[self.original_fcn_name].elementParameterDict.keys()):
                        tmpAST = self._QTObj._qtProject._ElementManager.get_dp_return_ast(dp)
                        design_dict = self._QTObj._qtProject._feed_design(design_type='constraint',
                                                                          module_name=self._CurrentModuleName,
                                                                          _ast=tmpAST, element_manager_update=False)
                        self.dockContentWidget3_2.createNewConstraintAST(_id=design_dict['constraint_id'],
                                                                         _parentName=self._CurrentModuleName,
                                                                         _DesignConstraint=self._QTObj._qtProject._DesignConstraint)
                        tmp_dp_dict, _ = self._QTObj._qtProject._ElementManager.get_ast_return_dpdict(tmpAST)
                        self._QTObj._qtProject._ElementManager.load_dp_dc_id(dp_id=dp_name, dc_id=design_dict['constraint_id'])
            else:
                print('dp_discarded')
                """
                dp정보를 날릴 경우 현재와 과거 dp를 비교하여 없는 dp는 현재 dp목록에서 삭제시킨다.
                """
                # list_to_remove = []
                # for dp_name, dp in self._QTObj._qtProject._DesignParameter[self._CurrentModuleName].items():
                #     if dp_name not in list(self._QTObj._qtProject._ElementManager_topology_dict[self.original_fcn_name].elementParameterDict.keys()):
                #         list_to_remove.append(dp_name)

                topology_keys = list(self._QTObj._qtProject._ElementManager_topology_dict[self.original_fcn_name].elementParameterDict.keys())
                search_keys = list(self._QTObj._qtProject._DesignParameter[self._CurrentModuleName].keys())
                list_to_remove = list(filter(lambda dp_name: dp_name not in topology_keys, search_keys))

                for dp_name in list_to_remove:
                    del self._QTObj._qtProject._DesignParameter[self._CurrentModuleName][dp_name]
                    self.scene.removeItem(self.visualItemDict[dp_name])


        self._QTObj._qtProject._ElementManager_topology_dict[fcn_name].elementParameterDict = copy.deepcopy(self._QTObj._qtProject._DesignParameter[self._CurrentModuleName])
        self.original_fcn_name = fcn_name
    def run_setup_update(self):
        self.setup_widget = QWidget()
        form_layout = QFormLayout()
        setup_list = [item for item in dir(user_setup) if not item.startswith("__")]
        # for setup_item in setup_list:
        #     form_layout.addRow(setup_item, QLineEdit(str(user_setup.__dict__[setup_item])))
        list(map(lambda setup_item: form_layout.addRow(setup_item, QLineEdit(str(user_setup.__dict__[setup_item]))), setup_list))
        self.setup_widget.setLayout(form_layout)
        self.setup_widget.show()

    def calculator(self):
        self.calculator_window.set_preset_window()
        self.calculator_window.show()

    def condition_expression(self):
        self.condition_expression_window.show()
        self.condition_expression_window.send_output_dict_signal.connect(self.create_condition_exp)

    def create_condition_exp(self, output_dict):
        def create_ast_by_dict(info_dict):
            output_ast = variable_ast.ConditionExpression()
            output_ast.variable = create_ast_by_dict(info_dict['variable']) if type(info_dict['variable']) == dict \
            else info_dict['variable']
            output_ast.condition = create_ast_by_dict(info_dict['condition']) if type(info_dict['condition']) == dict \
            else info_dict['condition']
            output_ast.operator = info_dict['operator']
            return output_ast

        test_ast = create_ast_by_dict(output_dict)
        # self.createNewConstraintAST(test_ast)

        ast_list = ASTmodule._searchAST(test_ast)
        idx = ast_list.index(test_ast)
        ast_list.pop(idx)
        _, top_id = self._QTObj._qtProject._createNewDesignConstraintAST(_ASTDtype="ASTsingle",
                                                                     _ParentName=self._CurrentModuleName,
                                                                     _AST=test_ast)
        for sub_ast in ast_list:
            self._QTObj._qtProject._createNewDesignConstraintAST(_ASTDtype="ASTsingle",
                                                                 _ParentName=self._CurrentModuleName,
                                                                 _AST=sub_ast)

        self.dockContentWidget3_2.createNewConstraintAST(_id=top_id[0], _parentName=self._CurrentModuleName,
                                                         _DesignConstraint=self._QTObj._qtProject._DesignConstraint)

    def condition_stmt(self):
        self.conditional_stmt_window.show()
        self.conditional_stmt_window.send_output_list_signal.connect(self.create_condition_stmt)

    def create_condition_stmt(self, output_list):
        condition_stmt_list_ast = variable_ast.ConditionSTMTlist()
        condition_stmt_list_ast.body = []

        def create_exp_ast_by_dict(info_dict):
            output_ast = variable_ast.ConditionExpression()
            output_ast.variable = create_exp_ast_by_dict(info_dict['variable']) if type(info_dict['variable']) == dict \
            else info_dict['variable']
            output_ast.condition = create_exp_ast_by_dict(info_dict['condition']) if type(info_dict['condition']) == dict \
            else info_dict['condition']
            output_ast.operator = info_dict['operator']
            return output_ast

        def create_stmt_ast_by_dict(info_dict):
            output_ast = variable_ast.ConditionSTMT()
            output_ast.c_type = info_dict['c_type']
            output_ast.expression = create_exp_ast_by_dict(info_dict['expression']) if type(info_dict['expression']) == dict \
            else info_dict['expression']
            output_ast.body = []
            # for stmt in info_dict['body']:
            #     output_ast.body.append(create_stmt_ast_by_dict(stmt))
            output_ast.extend(create_stmt_ast_by_dict(stmt) for stmt in info_dict['body'])
            return output_ast

        # for stmt in output_list:
        #     condition_stmt_list_ast.body.append(create_stmt_ast_by_dict(stmt))
        condition_stmt_list_ast.body.extend(create_stmt_ast_by_dict(stmt) for stmt in output_list)

        ast_list = ASTmodule._searchAST(condition_stmt_list_ast)
        idx = ast_list.index(condition_stmt_list_ast)
        ast_list.pop(idx)
        _, top_id = self._QTObj._qtProject._createNewDesignConstraintAST(_ASTDtype="ASTsingle",
                                                                         _ParentName=self._CurrentModuleName,
                                                                         _AST=condition_stmt_list_ast)
        for sub_ast in ast_list:
            self._QTObj._qtProject._createNewDesignConstraintAST(_ASTDtype="ASTsingle",
                                                                 _ParentName=self._CurrentModuleName,
                                                                 _AST=sub_ast)

        self.dockContentWidget3_2.createNewConstraintAST(_id=top_id[0], _parentName=self._CurrentModuleName,
                                                         _DesignConstraint=self._QTObj._qtProject._DesignConstraint)

    def get_dc_highlight_dp(self,dc_id):
        # for seleceted_item in self.scene.selectedItems():
        #     seleceted_item.setSelected(False)
        list(map(lambda seleceted_item: seleceted_item.setSelected(False), self.scene.selectedItems()))
        dp_id = self._QTObj._qtProject._ElementManager.get_dp_id_by_dc_id(dc_id)
        if dp_id:
            try:
                self.visualItemDict[dp_id].setSelected(True)
            except:
                self.warning = QMessageBox()
                self.warning.setText("Corresponding element is not in the dictionary!")
                self.warning.show()


    def change_process(self):
        self.process_list_widget = QListWidget()
        process_list =[]
        process_file_path = './PyQTInterface/layermap/'
        for item in os.listdir(process_file_path):
            if item == '__pycache__':
                continue
            if os.path.isdir(process_file_path+item):
                process_list.append(item)
        self.process_list_widget.addItems(process_list)
        self.process_list_widget.show()
        self.process_list_widget.itemDoubleClicked.connect(self.request_change_process)

    def request_change_process(self, technology_item, test = None):
        # technology_name = self.sender().row(technology_item).text()
        technology_name = technology_item.text() if not test else test

        if user_setup._Technology == technology_name:
            self.message = QMessageBox()
            self.message.setText("Technology is not changed.")
            self.message.setInformativeText("Target technology and current technology is same.")
            self.message.show()
            return None
        else:
            self.message = QMessageBox()
            self.message.setText("Technology Change.")
            self.message.setInformativeText(f"Confirm your action.\n"
                                            f"{user_setup._Technology} to {technology_name}.")
            self.message.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
            # self.message.show()
            choice = self.message.exec() if not test else QMessageBox.Ok
            if choice == QMessageBox.Ok:
                user_setup._Technology = technology_name

                from PyQTInterface.layermap import DisplayReader
                LayerReader.run_for_process_update()
                DisplayReader.run_for_process_update()
                from generatorLib import drc_api
                drc_api.run_for_process_update()
                from generatorLib import DesignParameters
                DesignParameters.run_for_process_update()
                self.send_tech_node_changed_signal.emit()


                if self._CurrentModuleName in self._QTObj._qtProject._DesignParameter:
                    # for qt_dp in self._QTObj._qtProject._DesignParameter[self._CurrentModuleName].values():
                    #     qt_dp.run_for_process_update()
                    list(map(lambda qt_dp: qt_dp.run_for_process_update(), self._QTObj._qtProject._DesignParameter[self._CurrentModuleName].values()))

                remove_vs_items = []
                for dp_name, vs_item in self.visualItemDict.items():
                    # vs_item.invalid_layer_signal.connect(self.warning_invalid_layer)
                    qt_dp = self._QTObj._qtProject._DesignParameter[self._CurrentModuleName][dp_name]
                    # vs_item.rerun_for_process_update(qt_dp)
                    remove_vs_items.extend(vs_item.rerun_for_process_update(qt_dp))
                for rm_item in remove_vs_items:
                    self.scene.removeItem(rm_item)
                    del rm_item

                def min_snap_change():
                    user_setup.MIN_SNAP_SPACING = spin_box.value()
                    self.min_snap_spacing_change.close()
                    print('Process Changed!')
                    self.message = QMessageBox()
                    self.message.setText("Process Changed!")
                    self.message.setInformativeText(
                        f"Technology was changed from {user_setup._Technology} to {technology_name}.")
                    self.message.show()
                    self.process_list_widget.close()

                min_snap_before = user_setup.MIN_SNAP_SPACING

                self.min_snap_spacing_change = QWidget()

                label = QLabel('Minimum spacing option :')

                spin_box = QSpinBox()
                spin_box.setValue(min_snap_before)
                spin_box.setMinimum(1)
                spin_box.setSingleStep(1)

                ok_button = QPushButton()
                ok_button.setText('OK')
                ok_button.clicked.connect(min_snap_change)

                hbox1 = QHBoxLayout()
                hbox2 = QHBoxLayout()
                vbox = QVBoxLayout()
                hbox1.addWidget(label)
                hbox1.addWidget(spin_box)
                hbox2.addStretch(3)
                hbox2.addWidget(ok_button)
                vbox.addLayout(hbox1)
                vbox.addLayout(hbox2)
                self.min_snap_spacing_change.setLayout(vbox)

                self.min_snap_spacing_change.show()

    def warning_invalid_layer(self, layer_name):
        self.warning_widget = QtWarningMsg(f"Not valid layer: {layer_name}")

    def inspect_path_point(self):
        inspector = topAPI.inspector.path_point_inspector(self._QTObj._qtProject._DesignParameter[self._CurrentModuleName])
        output = inspector.get_all_path_connection_info()
        path_list = output['path_list']
        self.path_point_reference = output['path_connection_info']
        print(output)

        self.path_point_widget =QListWidget()
        self.path_point_widget.addItems([str(path['_ElementName']) for path in path_list])

        self.path_point_widget.itemDoubleClicked.connect(self.show_inspect_path_widget)
        self.path_point_widget.show()

    def show_inspect_path_widget(self, path_item):
        row = self.sender().row(path_item)
        reference = copy.deepcopy(self.path_point_reference[row])
        # for ref in reference:
        #     self.highlightVI_by_hierarchy_list(ref[0][0])
        list(map(lambda ref: self.highlightVI_by_hierarchy_list(ref[0][0]), reference))
        self.visualItemDict[path_item.text()].set_shallow_highlight()




    def inspect_array(self):
        inspector = topAPI.inspector.array_inspector(self._QTObj._qtProject._DesignParameter[self._CurrentModuleName])
        output = inspector.inspect()
        if output == None:
            self.warning = QMessageBox()
            self.warning.setText("Unable to recognize Array References; Rearrange the design appropriately!"
                                 "\nDebug: clustering.py, method find_ref")
            self.warning.show()
            return
        groups_list = output['group_list']
        self.reference_list = output['reference_list']


        self.array_list_widget = QListWidget()
        self.array_list_widget.addItems([str(group) for group in groups_list])
        self.array_list_widget.currentRowChanged.connect(self.visualize_inspect_array)

        self.array_list_widget.itemDoubleClicked.connect(self.show_inspect_array_widget)
        self.array_list_widget.show()
        self.test_purpose_var = groups_list
        self.log = []


    def show_inspect_array_widget(self, array_list_item):
        row = self.array_list_widget.row(array_list_item)
        group_ref = self.reference_list[row]
        array_list = eval(array_list_item.text())

        self.vw = variableWindow.VariableSetupWindow(variable_type="boundary_array")
        self.vw.send_output_dict_signal.connect(self.create_variable)
        self.vw.send_DestroyTmpVisual_signal.connect(self.deleteDesignParameter)
        self.vw.request_dummy_constraint_signal.connect(self.delivery_dummy_constraint)
        self.vw.send_clicked_item_signal.connect(self.highlightVI_by_hierarchy_list)
        self.vw.variable_widget.send_exported_width_height_signal.connect(self.createDummyConstraint)
        self.vw.send_variable_signal.connect(self.send_array_variable)

        self.dockContentWidget3.send_dummy_ast_id_for_array_signal.connect(self.vw.update_ui_by_constraint_id)
        self.dockContentWidget3_2.send_dummy_ast_id_for_array_signal.connect(self.vw.update_ui_by_constraint_id)





        if self._QTObj._qtProject._DesignParameter[self._CurrentModuleName][array_list[0]]._type == 1:
            self.vw.variable_type = 'boundary_array'
        elif self._QTObj._qtProject._DesignParameter[self._CurrentModuleName][array_list[0]]._type == 2:
            self.vw.variable_type = 'path_array'
        elif self._QTObj._qtProject._DesignParameter[self._CurrentModuleName][array_list[0]]._type == 3:
            library = self.visualItemDict[array_list[0]]._ItemTraits['library']
            className = self.visualItemDict[array_list[0]]._ItemTraits['className']
            if 'calculate_fcn' in self.visualItemDict[array_list[0]]._ItemTraits:
                calculate_fcn = self.visualItemDict[array_list[0]]._ItemTraits['calculate_fcn']
            else:
                calculate_fcn = None
            parameters = self.visualItemDict[array_list[0]]._ItemTraits['parameters']
            self.vw.variable_type = 'sref_array'
            self.vw.variable_widget.field_value_memory_dict['sref_item_dict'] = {'library':library, 'className':className, 'calculate_fcn':calculate_fcn, 'parameters':parameters}

        self.vw.group_list = group_ref
        self.vw.inspect_array_window_address = self.array_list_widget
        self.vw.getArray(array_list_item)
        self.vw.show()

    def delivery_dummy_constraint(self, dummy_id):
        dummy_constraint = self._QTObj._qtProject._DesignConstraint[self._CurrentModuleName][dummy_id]._ast.info_dict
        self.sender().delivery_dummy_constraint(dummy_constraint)

    def visualize_inspect_array(self, row):
        # for id in self.log:
        #     self.visualItemDict[id].setSelected(False)
        list(map(lambda id: self.visualItemDict[id].setSelected(False), self.log))
        # for id in self.test_purpose_var[row]:
        #     self.visualItemDict[id].setSelected(True)
        #     self.log.append(id)
        list(map(lambda id: self.visualItemDict[id].setSelected(True), self.test_purpose_var[row]))
        self.log.extend(id for id in self.test_purpose_var[row])
        print(row)

    def inspect_geometry(self):
        target_cell = self._QTObj._qtProject._DesignParameter[self._CurrentModuleName]
        geo_search = topAPI.routing_geo_searching.GeometricField()
        geo_search.xy_projection_to_main_coordinates_system_qt(target_cell)
        geo_search.build_IST_qt(target_cell)
        return geo_search

    def save_clipboard(self,save_target,_):
        if type(save_target) == list:
            new_list = list()
            print(save_target)
            print(_)
            for idx in range(len(save_target)):
                if idx != 0:
                    if type(_[idx]) == int:
                        tmp = save_target[idx] + '[' + str(_[idx]) + ']'
                    else:
                        tmp = save_target[idx] + str(_[idx])
                    new_list.append(tmp)
            print(new_list)
            self.gloabal_clipboard.setText(str(new_list))

    def get_hierarchy_return_layer(self, hierarchy_list):
        module = self._QTObj._qtProject._DesignParameter[self._CurrentModuleName]
        layernum2name = LayerReader._LayerNumber2CommonLayerName(LayerReader._LayerMapping)
        for i in range(len(hierarchy_list)):
            element = re.sub("\[.\]","", hierarchy_list[i])
            hierarchy_list[i] = element

        if len(hierarchy_list) == 0:
            return
        elif len(hierarchy_list) == 1:
            _layerInfo = module[hierarchy_list[0]]._DesignParameter['_Layer']
            if type(_layerInfo) == int:
                _layerCommonName = layernum2name[str(_layerInfo)]
            else:
                _layerCommonName = _layerInfo
        else:
            for i in range(len(hierarchy_list)-1):
                module = module[hierarchy_list[i]]._DesignParameter['_ModelStructure']
            try:
                if module[hierarchy_list[-1]]._DesignParameter['_Layer']:
                    _layerCommonName = layernum2name[str(module[hierarchy_list[-1]]._DesignParameter['_Layer'])]
                    self.calculator_window.returnedLayer = _layerCommonName
                else:
                    pass
            except:
                self.warningbox = QMessageBox()
                self.warningbox.setText(f"Check the layer name. Update your design if not done yet.\n"
                                        f"KeyError: {hierarchy_list[-1]}")
                self.warningbox.setIcon(QMessageBox.Warning)
                self.warningbox.show()
                self.calculator_window.destroy()
                del self.calculator_window
                return




    def srefModulization(self,_flattenStatusDict, _sref = None):
        """
        :param _flattenStatusDict:
               _sref param not needed: this param exists only for recursive call
        :return: reconstructed cell structure according to param '_flattenStatusDict'
        """
        _finalModule = dict()
        if _sref == None:
            ########################################## 1. Initial Condition ############################################
            addedModulelist = list(self._QTObj._qtProject._DesignParameter.keys())
            topCellName = addedModulelist[-1]
            number_of_cells = len(self._QTObj._qtProject._DesignParameter[topCellName].values())
            # numberOfCells = int(re.findall('\d+', lastSrefName)[0])
            tmpDict = dict()
            print("             #######################################################################               ")
            print(f"               There are '{number_of_cells}' cells inside '{topCellName}' cell                  ")
            print("             #######################################################################               ")
            for _id, _elements in self._QTObj._qtProject._DesignParameter[topCellName].items():
                if _elements._DesignParameter['_DesignParametertype'] == 3:                      # Sref inside top cell
                    _childName = _elements._DesignParameter['_DesignObj_Name']
                    _childModule = self.srefModulization(_flattenStatusDict, _elements)          # Recursive Call
                    for _id2, elements2 in _childModule.items():
                        name = elements2._DesignParameter['_ElementName']

                        ###### Preventing Name Overwriting #####
                        while True:
                            if name in list(tmpDict.keys()):
                                newName = name + str(1)
                                name = newName
                            else:
                                break
                        #########################################

                        tmpDict[name] = elements2
                else:
                    tmpDict[_id] = _elements
            _finalModule = tmpDict

        else:
            ############################################# 2. Subcell Cases ############################################
            _childName = _sref._DesignParameter['_DesignObj_Name']
            _newChildName = f'{_childName}/{_sref._DesignParameter["_ElementName"]}'
            _parentName = _sref._id
            _parentXY = _sref._DesignParameter['_XYCoordinates']
            tmpDict = dict()
            if _childName in list(self._QTObj._qtProject._DesignParameter.keys()):
                tmpdict = self._QTObj._qtProject._DesignParameter[_childName]
            else:
                tmpdict = _sref._DesignParameter['_ModelStructure']
            for _id1, _modules1 in tmpdict.items():
                if _modules1._DesignParameter['_DesignParametertype'] != 3:
                    tmpDict[_modules1._id] = _modules1
                else :                                      # If one of the subcells is SREF, Recursive call
                    _childModule2 = self.srefModulization(_flattenStatusDict, _modules1)
                    for _id2, elements2 in _childModule2.items():
                        _name = elements2._DesignParameter['_ElementName']
                        while True:
                            if _name in list(tmpDict.keys()):
                                newName = _name + str(1)
                                _name = newName
                            else:
                                break
                        tmpDict[_name] = elements2

            for key, value in _flattenStatusDict.items():   # Check whether to flatten or not
                findHint = _newChildName.find(key)
                if findHint != -1:
                    if value != None:                       # Not Flattening Condition
                        tmpmodule = copy.deepcopy(_sref)
                        tmpmodule._DesignParameter['_ModelStructure'] = tmpDict
                        _finalModule[_childName] = tmpmodule
                        break
                    else:                                   # Flattening Condition
                        """                 
                        Flattening Condition needs XY coordinate modification, and renaming process
                        """
                        for _id, element in tmpDict.items():
                            tmpmodule = copy.deepcopy(element)
                            if tmpmodule._DesignParameter['_DesignParametertype'] == 2:
                                _XYpairs = tmpmodule._DesignParameter['_XYCoordinates'][0]  # [[a,a'],[b,b'],[c,c']]
                                _modifiedXYpairs = []
                                for i in range(0,len(_XYpairs)):
                                    _newXY = [x+y for x,y in zip(_XYpairs[i], _parentXY[0])]
                                    _modifiedXYpairs.append(_newXY)
                                while True:
                                    if tmpmodule._id in _finalModule:   # Preventing name overwriting
                                        newName = tmpmodule._id + str(1)
                                        tmpmodule._id = newName
                                    else:
                                        break
                                tmpmodule._DesignParameter['_XYCoordinates'] = [_modifiedXYpairs]
                                _finalModule[tmpmodule._id] = tmpmodule
                            else:
                                newXY = [[x+y for x,y in zip(tmpmodule._DesignParameter['_XYCoordinates'][0], _parentXY[0])]]
                                tmpmodule._DesignParameter['_XYCoordinates'] = newXY
                                while True:
                                    if tmpmodule._id in _finalModule:   # Preventing name overwriting
                                        newName = tmpmodule._id + str(1)
                                        tmpmodule._id = newName
                                    else:
                                        break
                                _finalModule[tmpmodule._id] = tmpmodule
                        break
        return _finalModule

    def debug_not_defined_variables(self):
        self.dockContentWidget3.blockSignals(True)
        user_variables = variableWindow._createNewDesignVariable.variableDict.values()
        has_value_variable_list = list(filter(lambda x: x['value'] != '', user_variables))

        try:
            debugger_gds2gen = topAPI.gds2generator.GDS2Generator(True)
            debugger_gds2gen.load_qt_project(self)
            debugger_gds2gen.load_qt_design_parameters(self._QTObj._qtProject._DesignParameter, self._CurrentModuleName)

            debugger_gds2gen.user_variables = has_value_variable_list

            module = self._CurrentModuleName
            constraint_names = self.dockContentWidget3.model.findItems('', Qt.MatchContains, 1)
            constraint_ids = [item.text() for item in constraint_names]
            ast_list = []
            for _id in constraint_ids:
                error_id = _id
                ast_list.append(self._QTObj._qtProject._DesignConstraint[module][_id]._ast)
                # result_ast = self.transform_constraints(ast_list)
                result_ast = ASTmodule.run_transformer(ast_list)
                code = astunparse.unparse(result_ast)
                debugger_gds2gen.load_qt_design_constraints_code(code)
                debugger_gds2gen.set_root_cell(self._CurrentModuleName)
                debugger_gds2gen.run_qt_constraint_ast()
                self.dockContentWidget3.set_errored_constraint_id(_id, 'clean')
        except Exception as e:
            error_log = traceback.format_exc()
            self.dockContentWidget3.set_errored_constraint_id(error_id, 'no_value', error_log, e)
            error_variable_name = re.search("\'.+\'", e.args[0]).group()
            self.dockContentWidget3.blockSignals(False)
            return error_variable_name
        self.dockContentWidget3.blockSignals(False)
        return None

    def debugConstraint(self):
        '''
        Run-time debugger for generator constraints.
        If debugger finds error, then it emits error_id signal to constraint_view widget.
        And it returns code describing working code which ends at right before error constraint.
        '''
        self.dockContentWidget3.blockSignals(True)
        try:
            error_id = None
            debugger_gds2gen = topAPI.gds2generator.GDS2Generator(True)
            debugger_gds2gen.load_qt_project(self)
            debugger_gds2gen.load_qt_design_parameters(self._QTObj._qtProject._DesignParameter, self._CurrentModuleName)

            module = self._CurrentModuleName
            constraint_names = self.dockContentWidget3.model.findItems('', Qt.MatchContains, 1)
            constraint_ids = [item.text() for item in constraint_names]
            ast_list = []

            for _id in constraint_ids:
                error_id = _id
                ast_list.append(self._QTObj._qtProject._DesignConstraint[module][_id]._ast)
                # result_ast = self.transform_constraints(ast_list)
                result_ast = ASTmodule.run_transformer(ast_list)
                code = astunparse.unparse(result_ast)
                debugger_gds2gen.load_qt_design_constraints_code(code)
                debugger_gds2gen.set_root_cell(self._CurrentModuleName)
                debugger_gds2gen.run_qt_constraint_ast()
                self.dockContentWidget3.set_errored_constraint_id(_id, 'clean')
                working_code = code
        except Exception as e:
            error_log = traceback.format_exc()
            if error_id:
                self.dockContentWidget3.set_errored_constraint_id(error_id, 'dynamic', error_log, e)
                self.dockContentWidget3.blockSignals(False)
            if 'working_code' in locals():
                return working_code
            else:
                return None
        self.dockContentWidget3.blockSignals(False)
        return None

    def encodeConstraint(self, _ast=None):
        try:
            if not _ast:
                module = self._CurrentModuleName
                constraint_names = self.dockContentWidget3.model.findItems('',Qt.MatchContains,1)
                constraint_ids = [item.text() for item in constraint_names]
                # topAST = self.transform_constraints([self._QTObj._qtProject._DesignConstraint[module][id]._ast for id in constraint_ids])
                topAST = ASTmodule.run_transformer([self._QTObj._qtProject._DesignConstraint[module][id]._ast for id in constraint_ids])
            else:
                topAST = ASTmodule.run_transformer([_ast])

            code = astunparse.unparse(topAST)
            print(code)

            return code
        except:
            traceback.print_exc()
            print("encoding fail")

    def visibleCandidate(self, state):
        constraint_names_can = self.dockContentWidget3_2.model.findItems('', Qt.MatchContains, 1)
        constraint_ids_can = [item.text() for item in constraint_names_can]
        vi_can = []
        viList = []

        ids_len = len(constraint_ids_can)
        for i in range(ids_len):
            dc_id = constraint_ids_can[0]
            dp_id = self._QTObj._qtProject._ElementManager.get_dp_id_by_dc_id(dc_id)
            constraint_ids_can.remove(dc_id)
            constraint_ids_can.append(dp_id)

        for layer in self._layerItem:
            vi_can.extend(self._layerItem[layer])

        for visualItem in vi_can:
            for idx in range(len(constraint_ids_can)):
                if constraint_ids_can[idx] == visualItem._id:
                    viList.append(visualItem)
                    if state == 0:
                        visualItem.setVisible(False)
                    elif state == 2:
                        visualItem.setVisible(True)

        self.send_visibleCanState_signal.emit(state, viList)

    def visibleGenerator(self, state):
        constraint_names_gen = self.dockContentWidget3.model.findItems('', Qt.MatchContains, 1)
        constraint_ids_gen = [item.text() for item in constraint_names_gen]
        vi_gen = []
        viList = []

        ids_len = len(constraint_ids_gen)
        for i in range(ids_len):
            dc_id = constraint_ids_gen[0]
            dp_id = self._QTObj._qtProject._ElementManager.get_dp_id_by_dc_id(dc_id)
            constraint_ids_gen.remove(dc_id)
            constraint_ids_gen.append(dp_id)

        for layer in self._layerItem:
            vi_gen.extend(self._layerItem[layer])

        for idx in range(len(constraint_ids_gen)):
            for visualItem in vi_gen:
                if constraint_ids_gen[idx] == visualItem._id:
                    viList.append(visualItem)
                    if state == 0:
                        visualItem.setVisible(False)
                    elif state == 2:
                        visualItem.setVisible(True)

        self.send_visibleGenState_signal.emit(state, viList)

    def runConstraint(self):
        try:
            if user_setup.GDS2GEN is False:
                return

            self.gds2gen = topAPI.gds2generator.GDS2Generator(True)
            self.gds2gen.load_qt_project(self)
            self.gds2gen.load_qt_design_parameters(self._QTObj._qtProject._DesignParameter,self._CurrentModuleName)
            self.gds2gen.load_qt_design_constraints_code(self.encodeConstraint())
            self.gds2gen.set_root_cell(self._CurrentModuleName)
            self.gds2gen.run_qt_constraint_ast()

            stream_data = self.gds2gen.ready_for_top_cell()
            self.gds2gen.set_topcell_name('test')
            file = open('./tmp.gds','wb')
            stream_data.write_binary_gds_stream(file)
            file.close()

        except:
            traceback.print_exc()
            print("Run fail")


    def runConstraint_for_update(self, code=None):
        '''
        run generator constraint and update visual object by updated designs.
        stop_point is introduced to support line by line execution.
        '''
        try:
            gds2gen = topAPI.gds2generator.GDS2Generator(False)
            gds2gen.load_qt_project(self)
            gds2gen.load_qt_design_parameters(self._QTObj._qtProject._DesignParameter, self._CurrentModuleName)
            # gds2gen.load_qt_design_constraints_code(self.encodeConstraint())
            if code:
                gds2gen.load_qt_design_constraints_code(code)
            else:
                gds2gen.load_qt_design_constraints_code(self.encodeConstraint())
            dp_dict = gds2gen.get_updated_designParameters()                                    # New Info
            for dp in dp_dict.values():
                if '_ModelStructure' in dp:
                    for qt_dp in dp['_ModelStructure'].values():
                        qt_dp.update_unified_expression()

            if self._CurrentModuleName in self._QTObj._qtProject._DesignParameter:
                current_dpdict = self._QTObj._qtProject._DesignParameter[self._CurrentModuleName]   # Unchanged target Info


                updated_dp_name_list = list(filter(lambda dp_name: dp_name  in current_dpdict, list(dp_dict.keys())))
                for dp_name in updated_dp_name_list:
                    current_dpdict[dp_name].update_unified_expression()
                    for key, value in dp_dict[dp_name].items():
                        current_dpdict[dp_name]._DesignParameter[key] = value
                    if current_dpdict[dp_name]._DesignParameter['_DesignParametertype'] == 3:
                        #TODO dp에는 있지만, vsitem은 없는경우 예외처리가 안되어 있음 (사실상 가정하지 않는 케이스 이기 때문)
                        sref_vi = self.visualItemDict[current_dpdict[dp_name]._DesignParameter['_id']]
                        remove_vi_items = sref_vi.updateDesignParameter(current_dpdict[dp_name])
                        for rm_vi in remove_vi_items:
                            self.scene.removeItem(rm_vi)
                        # self.scene.addItem(sref_vi)
                        # self.scene.removeItem(self.visualItemDict[current_dpdict[dp_name]._DesignParameter['_id']])
                        # self.visualItemDict[current_dpdict[dp_name]._DesignParameter['_id']] = sref_vi
                        self._layerItem = sref_vi.returnLayerDict()
                        self.dockContentWidget1_2.layer_table_widget.updateLayerList(self._layerItem)
                    else:
                        self.updateDesignParameter(current_dpdict[dp_name]._DesignParameter, False)

                new_dp_name_list = list(filter(lambda dp_name: dp_name not in current_dpdict, list(dp_dict.keys())))
                for dp_name in new_dp_name_list:
                    dp = dp_dict[dp_name]
                    design_dict = self._QTObj._qtProject._feed_design(design_type='parameter',
                                                                      module_name=self._CurrentModuleName,
                                                                      dp_dict=dp, element_manager_update=False)
                    visualItem = self.createVisualItemfromDesignParameter(
                        self._QTObj._qtProject._DesignParameter[self._CurrentModuleName][design_dict['parameter_id']])
                    visualItem._CreateFlag = False
                    self.updateGraphicItem(visualItem)
                    dc_id = self._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id(dp_name)
                    self._QTObj._qtProject._ElementManager.load_dp_dc_id(dp_id=dp_name, dc_id=dc_id)

                print(dp_dict)
            if not code:
                constraint_names = self.dockContentWidget3.model.findItems('', Qt.MatchContains, 1)
                constraint_ids = [item.text() for item in constraint_names]
                for _id in constraint_ids:
                    self.dockContentWidget3.set_errored_constraint_id(_id, 'clean')

                error_variable_name = self.debug_not_defined_variables()
                if error_variable_name:
                    self.warningbox = QMessageBox()
                    self.warningbox.setText(f"Variable {error_variable_name} was used at generator but not defined.")
                    self.warningbox.setIcon(QMessageBox.Warning)
                    self.warningbox.show()

        except:
            working_code = self.debugConstraint()
            if working_code:
                self.runConstraint_for_update(working_code)
            traceback.print_exc()


    def checkNameDuplication(self,checkItem):
        name = checkItem._ItemTraits['_ElementName']
        for item in self.scene.items():
            try:
                if name == item._ItemTraits['_ElementName']:
                    print("ERROR: Duplicated Name")
                    return True
            except:
                continue
        return False


    def delete_obj(self, obj):
        # sender = self.sender()
        # del sender
        if obj == 'cw':
            del self.cw
        if obj == 'bw':
            del self.bw
        if obj == 'pow':
            del self.pow
        if obj == 'pw':
            del self.pw
        if obj == 'dv':
            del self.dv
        # if obj == 'txtw':
        #     del self.txtw
        if obj == 'pinw':
            del self.pinw
        if obj == 'ls':
            del self.ls
        # self.scene.itemListClickIgnore(False)

    def updateGraphicItem(self,graphicItem):
        for items in self.scene.items():
            if items is graphicItem:
                self.scene.removeItem(items)
                self.scene.update()

        # if not self.checkNameDuplication(graphicItem):
        if graphicItem._CreateFlag is True:
            for item in graphicItem.block:
                if type(item) is VisualizationItem.QGraphicsTextItemWObounding:
                    item.setVisible(True)
        self.visualItemDict[graphicItem._ElementName] = graphicItem
        self.scene.addItem(graphicItem)
        self.scene.send_move_signal.connect(graphicItem.move)
        self.scene.send_moveDone_signal.connect(graphicItem.moveUpdate)

    def deleteGraphicItem(self,graphicItem):
        VisualizationItem._VisualizationItem()._subElementLayer[graphicItem._ItemTraits['_LayerUnifiedName']].remove(graphicItem)
        self.scene.removeItem(graphicItem)

    def newProject(self):
        self.npw = _VersatileWindow("NewProject")
        self.npw.show()
        self.npw.send_Name_signal.connect(self._QTObj._createProject)

    def loadProjectOriginal(self):
        scf = QFileDialog.getOpenFileName(self,'Load Project','./PyQTInterface/Project/')

        try:
            cm = self._CurrentModuleName
            # _data=self._QTObj._qtProject._ParseTreeForDesignConstrain[self._CurrentModuleName]._ParseTree
            _fileName=scf[0]
            self._QTObj._loadProject(_name=_fileName)


            #################Constraint Load ######################
            constraintList = []
            for module in self._QTObj._qtProject._ParseTreeForDesignConstrain:
                updateID = self._QTObj._qtProject._ParseTreeForDesignConstrain[module]._ParseTree['_id']
                moduleName = re.sub(r'\d','',updateID)
                constraintList.append(self._QTObj._qtProject._DesignConstraint[moduleName][updateID])
            self.dockContentWidget3_2.updateConstraintDictFromQTInterface(self._QTObj._qtProject)
            self.dockContentWidget3.updateConstraintDictFromQTInterface(self._QTObj._qtProject)
            for constraint in constraintList:
                self.dockContentWidget3.createNewConstraint(constraint)

            #################DesignParameter Load ######################
            for module in self._QTObj._qtProject._DesignParameter:
                for id in self._QTObj._qtProject._DesignParameter[module]:
                    visualItem = self.createVisualItemfromDesignParameter(self._QTObj._qtProject._DesignParameter[module][id])
                    self.updateGraphicItem(visualItem)

            self.dockContentWidget4ForLoggingMessage._InfoMessage("Project Load Done")

        except:
            print("Load Project Failed")
            self.dockContentWidget4ForLoggingMessage._WarningMessage("Load Project Fail: Unknown")
            pass
    def loadProject(self, test=None):
        if test:
            self.test = False
            scf = [test]
        else:
            scf = QFileDialog.getOpenFileName(self,'Load Project','./PyQTInterface/Project/')

        try:
            cm = self._CurrentModuleName
            _fileName=scf[0]
            if _fileName == '':
                return
            self._QTObj._loadProject(_name=_fileName)
            self._QTObj._qtProject.tmp_save_file.load_qt_interface(self,self._QTObj._qtProject._DesignConstraint)
            # self._QTObj._qtProject.tmp_save_file.load_from_constraint_tree_info(self, self._QTObj._qtProject._DesignConstraint)
            top_module = self._QTObj._qtProject.tmp_save_file.top_module
            if top_module in self._QTObj._qtProject._DesignParameter:
                for id_name, qt_parameter in self._QTObj._qtProject._DesignParameter[top_module].items():
                    vs_item = self.createVisualItemfromDesignParameter(qt_parameter)
                    vs_item._CreateFlag = False
                    self.updateGraphicItem(vs_item)
            self.dockContentWidget4ForLoggingMessage._InfoMessage("Project Load Done")
            self.test = True

        except:
            traceback.print_exc()
            print("Load Project Failed")
            self.dockContentWidget4ForLoggingMessage._WarningMessage("Load Project Fail: Unknown")
            pass


    def saveProject(self, test=None):
        # if _fileName == None:
        if test:
            self.test = False
            scf = [test]
        else:
            scf = QFileDialog.getSaveFileName(self,'Save Project','./PyQTInterface/Project/')
        # else:
        #     scf = [_fileName]
        try:
            if scf[0][-4:] != '.bin':
                _fileName = scf[0] + ".bin"
            else:
                _fileName = scf[0]

            # fileName=_fileName.split('/')[-1]
            # self.updateXYCoordinatesForDisplay()
            self._QTObj._qtProject.tmp_save_file = PyCodes.file_save.FileSaveFormat()
            self._QTObj._qtProject.tmp_save_file.save_from_qt_interface(self)
            self._QTObj._saveProject(_name=_fileName)

            # ######WIP for save whole project#####
            # import json
            # json.dump(self,open('./test.json','w'),indent=4, default=self.json_serialize_dump_obs)

            print("Project saved")
            self.test = True
        except:
            traceback.print_exc()
            print("Save Project Failed")
            self.dockContentWidget4ForLoggingMessage._WarningMessage("Save Project Fail: Unknown")
            pass

        # self._QTObj._saveProject()

    @staticmethod
    def json_serialize_dump_obs(obj):
        if hasattr(obj,"json_dump_obj"):
            return obj.json_dump_obj()
        return obj

    def show_module_window(self):
        if self._QTObj._qtProject == None:
            self.warning = QMessageBox()
            self.warning.setText("There is no Project")
            self.warning.show()
        else:
            self.nmw = _VersatileWindow("NewModule")
            self.nmw.show()
            self.nmw.send_Name_signal.connect(self.create_new_module)

    def create_new_module(self, updateModule):
        self.module_name_list.append(updateModule)
        self.module_dict[updateModule] = _MainWindow()
        new_project = self.module_dict[updateModule]
        new_project._QTObj._qtProject._DesignParameter = dict()

        self.module_dict[updateModule].set_module_name(updateModule)
        self.module_dict[updateModule].show()
        self.module_dict[updateModule].module_dict = self.module_dict
        self.module_dict[updateModule].module_name_list = self.module_name_list
        self.hide()

    def set_module_name(self, module_name):
        if self._CurrentModuleName in self.module_name_list:
            idx = self.module_name_list.index(self._CurrentModuleName)
            del self.module_name_list[idx]
        if self._CurrentModuleName in self.module_dict:
            del self.module_dict[self._CurrentModuleName]

        self.module_name_list.append(module_name)
        self.module_dict[module_name] = self
        self._CurrentModuleName = module_name
        self.dockContentWidget3._CurrentModuleName = module_name
        self.dockContentWidget3_2._CurrentModuleName = module_name

    def updateModule(self,ModuleName):
        if ModuleName not in self.module_name_list:
            self.module_name_list.append(ModuleName)
            self.module_dict[ModuleName] = _MainWindow()
            self.module_dict[ModuleName].module_dict = self.module_dict
            self.module_dict[ModuleName].module_name_list = self.module_name_list
        self.hide()
        self.module_dict[ModuleName].show()

    def moduleManage(self):
        self.mw = SetupWindow._ModuleManageWidget(self.module_name_list)
        self.mw.show()
        self.mw.send_ModuleName_signal.connect(self.updateModule)

    # def create
    def srefCreate(self, _AST):
        """
        Get Sref AST -> Create DP w/ ModelStructure -> Create Constraint -> Create Visual Item
        :param _AST: sref _AST which is made via 'SrefLoad' widget window
        :return: None
        """
        _moduleName = self._CurrentModuleName
        gds2gen = topAPI.gds2generator.GDS2Generator(True)
        _dp = gds2gen.code_generation_for_subcell(_AST)
        tmp_dp_dict, _ = self._QTObj._qtProject._ElementManager.get_ast_return_dpdict(_AST)
        print("########################################################################################")
        print(f"                CUSTOM SREF DP / DC / VisualItem Creation Start                        ")
        print("########################################################################################")
        if len(self._QTObj._qtProject._DesignParameter) == 0:
            self._QTObj._qtProject._DesignParameter[_moduleName] = dict()
            _newParameterID = tmp_dp_dict['_ElementName'] if tmp_dp_dict['_ElementName'] else self._CurrentModuleName + str(0)
            _tmpQtDpObj = QTInterfaceWithAST.QtDesignParameter(_id=_newParameterID,
                                                     _type= 3,
                                                    _ParentName=_moduleName,
                                                    _ElementName= tmp_dp_dict['_ElementName'])
            self._QTObj._qtProject._DesignParameter[_moduleName][_newParameterID] = _tmpQtDpObj
            print("*************************************************************************************")
            print(f" No existing DesignParameters: New DesignParameter creation with Name: {_moduleName}")
            print("*************************************************************************************")
        else:
            _designParameterID = self._QTObj._qtProject._getDesignConstraintId(_moduleName)
            _newParameterID = tmp_dp_dict['_ElementName'] if tmp_dp_dict['_ElementName'] else self._CurrentModuleName + str(0)
            _tmpQtDpObj = QTInterfaceWithAST.QtDesignParameter(_id=_newParameterID,
                                                     _type= 3,
                                                    _ParentName=_moduleName,
                                                    _ElementName= tmp_dp_dict['_ElementName'])
            self._QTObj._qtProject._DesignParameter[_moduleName][_newParameterID] = _tmpQtDpObj
            print("****************************************************************************************")
            print(f" Append to Existing DesignParameters: DesignParameter creation with Name: {_moduleName}")
            print("****************************************************************************************")
        try:
            self._QTObj._qtProject._DesignParameter[_moduleName][_newParameterID]._DesignParameter = tmp_dp_dict
            self._QTObj._qtProject._DesignParameter[_moduleName][_newParameterID]._DesignParameter['_id'] = _newParameterID
            self._QTObj._qtProject._DesignParameter[_moduleName][_newParameterID]._DesignParameter['_DesignObj'] = _dp['_DesignObj']
            self._QTObj._qtProject._DesignParameter[_moduleName][_newParameterID]._DesignParameter['_DesignObj_Name'] = tmp_dp_dict['_ElementName']
            self._QTObj._qtProject._DesignParameter[_moduleName][_newParameterID]._DesignParameter['_DesignParametertype'] = 3
            # self._QTObj._qtProject._DesignParameter[_moduleName][_newParameterID]._DesignParameter['_ElementName'] = _newParameterID
            self._QTObj._qtProject._DesignParameter[_moduleName][_newParameterID]._DesignParameter['_XYCoordinates'] = _dp['_XYCoordinates']
            self._QTObj._qtProject._DesignParameter[_moduleName][_newParameterID]._DesignParameter['_ModelStructure'] = _dp['_ModelStructure']
            self._QTObj._qtProject._DesignParameter[_moduleName][_newParameterID]._DesignParameter['_Reflect'] = None
            self._QTObj._qtProject._DesignParameter[_moduleName][_newParameterID]._DesignParameter['_Angle'] = None

            self._QTObj._qtProject._DesignParameter[_moduleName][_newParameterID]._DesignParameter['parameters'] = _AST.parameters

        except:
            traceback.print_exc()
            self.dockContentWidget4ForLoggingMessage._InfoMessage(" Not enough Parameters Given!")
            print("########################################################################################")
            print(f"                CUSTOM SREF DP / DC / VisualItem Creation Fail!                        ")
            print("########################################################################################")
            self.ls.maintain_window(False)
            return
        _module = self._QTObj._qtProject._DesignParameter[_moduleName]
        design_dict = self._QTObj._qtProject._feed_design(design_type='constraint',
                                                          module_name=_moduleName,
                                                          _ast=_AST, element_manager_update=False)
        self.dockContentWidget3_2.createNewConstraintAST(_id=design_dict['constraint_id'],
                                                         _parentName=_moduleName,
                                                         _DesignConstraint=self._QTObj._qtProject._DesignConstraint)
        self._QTObj._qtProject._ElementManager.load_dp_dc_id(dp_id=_newParameterID, dc_id=design_dict['constraint_id'])
        _module[_newParameterID].update_unified_expression()
        sref_vi = VisualizationItem._VisualizationItem()
        sref_vi.updateDesignParameter(_module[_newParameterID])
        self.scene.addItem(sref_vi)
        self.visualItemDict[_module[_newParameterID]._id] = sref_vi

        self._layerItem = sref_vi.returnLayerDict()

        self.dockContentWidget1_2.layer_table_widget.updateLayerList(self._layerItem)
        print("#####################################################################################")
        print(f"               CUSTOM SREF DP / DC / VisualItem Creation Done                       ")
        print("#####################################################################################")

    def srefUpdate(self, ast_with_id):
        """
        Get Sref AST -> Create DP w/ ModelStructure -> Create Constraint -> Create Visual Item
        :param _AST: sref _AST which is made via 'SrefLoad' widget window
        :return: None
        """
        print("########################################################################################")
        print(f"                CUSTOM SREF DP / DC / VisualItem Update Start                        ")
        print("########################################################################################")

        # dc_id = ast_with_id._id
        dp_id = ast_with_id._id #if ast_with_id._id in self._QTObj._qtProject._DesignParameter else ast_with_id.name
        # module = self.get_id_return_module(dc_id, "_DesignConstraint")
        module = self._CurrentModuleName
        gds2gen = topAPI.gds2generator.GDS2Generator(False)
        _dp = gds2gen.code_generation_for_subcell(ast_with_id)
        tmp_dp_dict , _ = self._QTObj._qtProject._ElementManager.get_ast_return_dpdict(ast_with_id)
        # dp_id = self._QTObj._qtProject._ElementManager.get_dp_id_by_dc_id(dc_id)

        _dp['_id'] = dp_id #set previous element_name
        dc_id = self._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id(dp_id)
        _dp['_ElementName'] = ast_with_id.name
        self.design_delegator.update_qt_parameter(_dp)
        self._QTObj._qtProject._DesignConstraint[self._CurrentModuleName][dc_id]._ast = ast_with_id
        self.design_delegator.control_constraint_tree_view(dc_id,None,'update')

        # self.design_delegator.update_qt_constraint(dc_id,ast_with_id)



        # self._QTObj._qtProject._DesignParameter[module][dp_id]._DesignParameter['_DesignObj'] = _dp['_DesignObj']
        # self._QTObj._qtProject._DesignParameter[module][dp_id]._DesignParameter['_ElementName'] = tmp_dp_dict['_ElementName']
        # self._QTObj._qtProject._DesignParameter[module][dp_id]._DesignParameter['_XYCoordinates'] = _dp['_XYCoordinates']
        # self._QTObj._qtProject._DesignParameter[module][dp_id]._DesignParameter['_ModelStructure'] = _dp['_ModelStructure']
        # self._QTObj._qtProject._DesignParameter[module][dp_id]._DesignParameter['library'] = tmp_dp_dict['library']
        # self._QTObj._qtProject._DesignParameter[module][dp_id]._DesignParameter['className'] = tmp_dp_dict['className']
        # self._QTObj._qtProject._DesignParameter[module][dp_id]._DesignParameter['XY'] = tmp_dp_dict['_XYCoordinates']
        # self._QTObj._qtProject._DesignParameter[module][dp_id]._DesignParameter['calculate_fcn'] = tmp_dp_dict['calculate_fcn']
        # self._QTObj._qtProject._DesignParameter[module][dp_id]._DesignParameter['parameters'] = tmp_dp_dict['parameters']
        # self._QTObj._qtProject._DesignParameter[module][dp_id].update_unified_expression()

        print("****************************************************************************************")
        print(f" Update Existing DesignParameters: DesignParameter creation with Name: {dp_id}")
        print("****************************************************************************************")

        # sref_vi = VisualizationItem._VisualizationItem()
        # sref_vi.updateDesignParameter(self._QTObj._qtProject._DesignParameter[module][dp_id])
        # self.scene.addItem(sref_vi)
        # self.scene.removeItem(self.visualItemDict[dp_id])
        # self.visualItemDict[dp_id] = sref_vi
        # self._layerItem = sref_vi.returnLayerDict()

        self.dockContentWidget1_2.layer_table_widget.updateLayerList(self._layerItem)

    def loadGDS(self, test=None):
        if test:
            scf = [test]
        else:
            scf = QFileDialog.getOpenFileName(self,'Load GDS','./PyQTInterface/GDSFile')
        _fileName=scf[0]
        if _fileName == '':
            print("No File Selected")
            return

        _moduleName = _fileName.replace(".gds","")
        _moduleName = _moduleName.split('/')[-1]
        self.set_module_name(_moduleName)
        originalModuleList = set(self._QTObj._qtProject._DesignParameter)
        # self.dockContentWidget4ForLoggingMessage._InfoMessage("Load GDS File Starts.")
        print("**************************File Load From Legacy Start")
        try:
            self._QTObj._qtProject._loadDesignsFromGDSlegacy(_file = _fileName, _topModuleName = _moduleName)
        except:
            import collections
            self._QTObj._qtProject._DesignParameter = collections.OrderedDict()
            try:
                self._QTObj._qtProject._loadDesignsFromGDSlegacy(_file = _fileName, _topModuleName = _moduleName, _reverse=True)
            except:
                traceback.print_exc()
                warnings.warn("Invalid Technology")
                del originalModuleList
                self._QTObj._qtProject._DesignParameter.clear()
                return
        print("****************************File Load From Legacy Complete")

        if self.progrseeBar_unstable == True:
            updateModuleList = set(self._QTObj._qtProject._DesignParameter)
            addedModuleList = list(updateModuleList-originalModuleList)
            idLength = 0
            self.entireHierarchy = self._QTObj._qtProject._getEntireHierarchy()
            for modules in addedModuleList:
                idLength += len(self._QTObj._qtProject._DesignParameter[modules])

            if DEBUG:
                print(f'DEBUGGING MODE, idLength= {idLength}')

            self.create_dc_vi_from_top_dp(self.entireHierarchy, test=test)

    def create_dc_vi_from_top_dp(self, hierarchy, test=None):

        self.fc = SetupWindow._FlatteningCell(hierarchy, self._QTObj._qtProject._DesignParameter)
        self.fc.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.fc.show()

        flattening_dict = self.fc.ok_button_accepted(test)
        self.fc.destroy()

        print("############################ Cell DP, DC, VISUALITEM CREATION START ###############################")
        visual_item_list = []
        addedModulelist = list(self._QTObj._qtProject._DesignParameter.keys())
        topCellName = addedModulelist[-1]
        # self._CurrentModuleName = topCellName       # Necessary For adding elements inside the cell
        self.set_module_name(topCellName)
        ProcessedModuleDict = self.srefModulization(flattening_dict)            # Reconstruct imported GDS
        self._QTObj._qtProject._DesignParameter[topCellName].clear()            # discard original top cell info
        topcell = self._QTObj._qtProject._DesignParameter[topCellName]
        for _id, _element in ProcessedModuleDict.items():
            # _designConstraintID = self._QTObj._qtProject._getDesignConstraintId(topCellName)
            legacy_dp_id = self._QTObj._qtProject._getDesignParameterId(topCellName)

            if _element._ElementName:
                parameter_id = _element._ElementName
                topcell[parameter_id] = _element
                topcell[parameter_id]._id = _element._ElementName
            else:
                parameter_id = (topCellName + str(legacy_dp_id))
                topcell[parameter_id] = _element
                topcell[parameter_id]._id = parameter_id
            ######################################### AST Creation ################################################

            if topcell[parameter_id]._DesignParameter['_DesignParametertype'] == 3:
                _cellModel = _element._DesignParameter['_DesignObj_Name']
                _cellName = _element._DesignParameter['_ElementName']
                _newCellName = _cellModel + '/' + _cellName
                for key, value in flattening_dict.items():
                    findHint = _newCellName.find(key)
                    if findHint != -1:
                        topcell[parameter_id]._DesignParameter['library'] = value
                        if value != 'MacroCell':    # case Sref
                            _className = generator_model_api.class_name_dict[_element._DesignParameter['library']]
                            topcell[parameter_id]._DesignParameter['className'] =_className
                            topcell[parameter_id]._DesignParameter['parameters'] = \
                                generator_model_api.class_dict[value]._ParametersForDesignCalculation
                        topcell[parameter_id]._ElementName = parameter_id
                        topcell[parameter_id]._DesignParameter['_id'] = parameter_id
                        topcell[parameter_id]._DesignParameter['_ElementName'] = parameter_id
                        tmpAST = self._QTObj._qtProject._ElementManager.get_dp_return_ast(topcell[parameter_id])
                        if tmpAST == None:
                            continue
                        design_dict = self._QTObj._qtProject._feed_design(design_type='constraint',
                                                                          module_name=topCellName,
                                                                          _ast=tmpAST, element_manager_update=False)
                        self.dockContentWidget3_2.createNewConstraintAST(_id=design_dict['constraint_id'],
                                                                         _parentName=topCellName,
                                                                         _DesignConstraint=self._QTObj._qtProject._DesignConstraint)
                        # tmp_dp_dict, _ = self._QTObj._qtProject._ElementManager.get_ast_return_dpdict(tmpAST)
                        self._QTObj._qtProject._ElementManager.load_dp_dc_id(dp_id=parameter_id, dc_id=design_dict['constraint_id'])
                        break
                    else:
                        continue
            else:
                tmpAST = self._QTObj._qtProject._ElementManager.get_dp_return_ast(topcell[parameter_id])
                if tmpAST is None:
                    continue
                design_dict = self._QTObj._qtProject._feed_design(design_type='constraint', module_name=topCellName,
                                                                  _ast=tmpAST, element_manager_update=False)
                self.dockContentWidget3_2.createNewConstraintAST(_id=design_dict['constraint_id'],
                                                                 _parentName=topCellName,
                                                                 _DesignConstraint=self._QTObj._qtProject._DesignConstraint)
                tmp_dp_dict, _ = self._QTObj._qtProject._ElementManager.get_ast_return_dpdict(tmpAST)
                self._QTObj._qtProject._ElementManager.load_dp_dc_id(dp_id=parameter_id, dc_id=design_dict['constraint_id'])

        ####################################### Visual Item Creation ##########################################
        if 'MULTI_THREAD' in user_setup.__dict__ and user_setup.MULTI_THREAD:
            from PyQTInterface import gds_thread
            multi_thread_num = user_setup.MULTI_THREAD_NUM
            gds_thread.thread_result = [None] * multi_thread_num
            gds_thread.finished_work = [0] * multi_thread_num
            gds_thread.job_list = [0] * multi_thread_num

            total_len = len(topcell)
            self.pg_bar = gds_thread.MultiThreadQProgressBar('Creating vs items...', 'Cancel', 0, total_len, self)
            # self.pg_bar.setRange(0,total_len-1)
            self.pg_bar.setWindowModality(Qt.ApplicationModal)
            self.pg_bar.show()
            pool = QThreadPool.globalInstance()
            worker_manager = gds_thread.VSItemRunnableManager(multi_thread_num)
            worker_manager.signal.every_job_doen_signal.connect(self.create_vs_items_from_thread_memory)
            pool.start(worker_manager)
            for i in range(multi_thread_num):
                idx_range = [int(total_len*i/multi_thread_num), int(total_len*(i+1)/multi_thread_num)]
                if i == multi_thread_num - 1:
                    thread_jobs = dict(list(topcell.items())[idx_range[0]:])
                else:
                    thread_jobs = dict(list(topcell.items())[idx_range[0]:idx_range[1]])
                worker = gds_thread.VSItemRunnable(i, thread_jobs)
                worker.signal.one_job_progress_signal.connect(self.pg_bar.add_count)
                worker.signal.every_job_doen_signal.connect(worker_manager.add_job_done)
                pool.start(worker)
        else:
            for parameter_id in topcell.keys():
                if topcell[parameter_id]._DesignParameter['_DesignParametertype'] != 3:
                    visualItem = self.createVisualItemfromDesignParameter(topcell[parameter_id])
                    visual_item_list.append(visualItem)
                    layer = tmp_dp_dict['_LayerUnifiedName']
                    if layer in self._layerItem:
                        self._layerItem[layer].append(visualItem)
                    else:
                        self._layerItem[layer] = [visualItem]
                    self._id_layer_mapping[topcell[parameter_id]._id] = layer
                    self.scene.addItem(visualItem)
                else:
                    sref_vi = VisualizationItem._VisualizationItem()
                    sref_vi.updateDesignParameter(topcell[parameter_id])
                    self.scene.addItem(sref_vi)
                    self.visualItemDict[topcell[parameter_id]._id] = sref_vi
                    self._layerItem = sref_vi.returnLayerDict()
                self.dockContentWidget1_2.layer_table_widget.updateLayerList(self._layerItem)

        print("############################ Cell DP, DC, VISUALITEM CREATION DONE ################################")

    def create_vs_items_from_thread_memory(self):
        from PyQTInterface import gds_thread
        for result_list in gds_thread.thread_result:
            # self.visualItemDict.update(result_list[0])
            for vs_item in result_list[0].values():
                # self.scene.addItem(vs_item)
                self.updateGraphicItem(vs_item)
            self._layerItem.update(result_list[1])
            self._id_layer_mapping.update(result_list[2])
        self.dockContentWidget1_2.layer_table_widget.updateLayerList(self._layerItem)
        self.dockContentWidget1_2.layer_table_widget.send_listInLayer_signal.connect(
            self.scene.getNonselectableLayerList)
        self.pg_bar.set_max()


    def loadPy(self):
        scf = QFileDialog.getOpenFileName(self, 'Load SourceCode', './sourceCode')
        try:
            _fileName = scf[0]

            self.dockContentWidget4ForLoggingMessage._InfoMessage("Convert Pysource to AST.")
            _none, _id = self._QTObj._qtProject._loadConstraintsFromPySource(_file=_fileName, _topModuleName=self._CurrentModuleName)
            self.dockContentWidget4ForLoggingMessage._InfoMessage("Conversion Done!")

            self.dockContentWidget4ForLoggingMessage._InfoMessage("Convert DC to TreeView")
            self.dockContentWidget3_2.createNewConstraintAST(_id=_id, _parentName=self._CurrentModuleName, _DesignConstraint=self._QTObj._qtProject._DesignConstraint)
            self.dockContentWidget4ForLoggingMessage._InfoMessage("Conversion Done!")

        except:
            print("Load PySource Failed")
            self.dockContentWidget4ForLoggingMessage._WarningMessage("Load PySource Fail: Unknown")
            pass

    def threadRun(self):
        self.tmpThread = SetupWindow._ThreadClassForPGbar()
        self.tmpThread.countChanged.connect(self.progressValueUpdate)
        self.tmpThread.start()

    def progressValueUpdate(self,val):
        print(val)
        self.qpd.setValue(val)


    #def launch_ProgressDiag_Thread(self,Name,Cancel,Min,Max):
    #    t = threading.Thread(target=self.progress_Diag,args=(Name,Cancel,Min,Max))
    #    t.start()

    def run_progress_Diag(self,Name,Cancel,Min,Max):
        self.qpd = QProgressDialog(Name,Cancel,Min,Max, self)
        self.qpd.setWindowModality(Qt.WindowModal)
        self.qpd.show()

    def createVariable(self,_type):
        if _type == 'auto_path':
            selected_vis_items = self.scene.selectedItems()
            vis_item = selected_vis_items[0]
            id = vis_item._id
            geo_field = self.inspect_geometry()
            overlay_object = geo_field.search_intersection_qt(self._QTObj._qtProject._DesignParameter[self._CurrentModuleName][id])
            #
            # for obj in overlay_object[1:]:
            #     obj[0][0]
            test= [obj[0][0] for obj in overlay_object[1:]]
            self.log2 = []
            for id in self.log2:
                self.visualItemDict[id].setSelected(False)
            for id in test:
                self.visualItemDict[id].setSelected(True)
                self.log2.append(id)

            print('connection info')
            print(overlay_object[1:])
            return
        elif _type == 'to_sref':
            pass

        selected_vis_items = self.scene.selectedItems()
        self.vw = variableWindow.VariableSetupWindow(variable_type=_type,vis_items=selected_vis_items)
        # self.vw = variableWindow.VariableSetupWindow(variable_type=type,vis_items=selected_vis_items)
        self.vw.send_output_dict_signal.connect(self.create_variable)
        self.vw.send_DestroyTmpVisual_signal.connect(self.deleteDesignParameter)
        self.vw.send_clicked_item_signal.connect(self.highlightVI_by_hierarchy_list)
        self.scene.send_item_clicked_signal.connect(self.vw.clickFromScene)
        self.vw.send_variableVisual_signal.connect(self.createVariableVisual)
        self.vw.variable_widget.send_exported_width_height_signal.connect(self.createDummyConstraint)
        self.vw.send_variable_signal.connect(self.send_array_variable)

    def edit_variable(self, _edit_id, variable_info_dict):
        target_dp_id = self._QTObj._qtProject._ElementManager.get_dp_id_by_dc_id(_edit_id)
        new_dp_id = variable_info_dict['name']
        self._QTObj._qtProject._DesignConstraint[self._CurrentModuleName][_edit_id]._ast.info_dict.clear()
        self._QTObj._qtProject._DesignConstraint[self._CurrentModuleName][_edit_id]._ast.info_dict = variable_info_dict
        if target_dp_id in list(self._QTObj._qtProject._DesignParameter[self._CurrentModuleName].keys()):
            self._QTObj._qtProject._DesignParameter[self._CurrentModuleName][new_dp_id] = \
                self._QTObj._qtProject._DesignParameter[self._CurrentModuleName].pop(target_dp_id)
            self._QTObj._qtProject._DesignParameter[self._CurrentModuleName][new_dp_id]._DesignParameter['_ElementName'] = new_dp_id
            dp_update_info = \
                self._QTObj._qtProject._ElementManager.get_ast_return_dpdict(
                    ast=self._QTObj._qtProject._DesignConstraint[self._CurrentModuleName][_edit_id]._ast,
                    dummy=variable_info_dict)
            for key, value in dp_update_info.items():
                self._QTObj._qtProject._DesignParameter[self._CurrentModuleName][new_dp_id]._setDesignParameterValue(key,
                                                                                                                 value)
        self._QTObj._qtProject._ElementManager.load_dp_dc_id(dp_id=new_dp_id, dc_id=_edit_id)


    def create_variable(self, _edit_id, variable_info_dict):
        if _edit_id in list(self._QTObj._qtProject._DesignConstraint[self._CurrentModuleName].keys()):
            self.edit_variable(_edit_id, variable_info_dict)
            return
        else:
            self.createDummyConstraint(type_for_dc = 'Array', info_dict= variable_info_dict)

    def createVariableVisual(self, variableVisualItem):
        design_dict = self._QTObj._qtProject._feed_design(design_type='parameter', module_name= self._CurrentModuleName, dp_dict= variableVisualItem.__dict__)
        if design_dict['constraint']:
            self.dockContentWidget3_2.createNewConstraintAST(_id=design_dict['constraint_id'],
                                                             _parentName=self._CurrentModuleName,
                                                             _DesignConstraint=self._QTObj._qtProject._DesignConstraint)

        # visualItem = self.createVisualItemfromDesignParameter(
        #     self._QTObj._qtProject._DesignParameter[self._CurrentModuleName][design_dict['parameter_id']])
        if self.dvstate is False:
            self.dv = variableWindow._DesignVariableManagerWindow(self.visualItemDict)
            print(self.dvstate, ':', self.dv)
        else:
            print(self.dvstate, ':', self.dv)
        variable_manager.Manage_DV_by_id(_id=design_dict['constraint_id'], _info=variableVisualItem.variable_info, _type=variableVisualItem._DesignParametertype, _address=self.dv)
        self.scene.addItem(variableVisualItem)
        pass


    def createNewDesignParameter(self,_DesignParameter):
        if self._QTObj._qtProject == None:
            self.warning=QMessageBox()
            self.warning.setText("There is no Project")
            self.warning.show()
            self.dockContentWidget4ForLoggingMessage._WarningMessage("Create DesignParameter Fail: There is no Project")
        elif self._CurrentModuleName is None:
            self.warning=QMessageBox()
            self.warning.setText("There is No Module")
            self.warning.show()
            self.dockContentWidget4ForLoggingMessage._WarningMessage("Create DesignParameter Fail: There is no Module")
        else:
            design_dict = self._QTObj._qtProject._feed_design(design_type='parameter', module_name= self._CurrentModuleName, dp_dict= _DesignParameter)
            design_dict['parameter'].update_unified_expression()
            visualItem = self.createVisualItemfromDesignParameter(design_dict['parameter'])
            visualItem._CreateFlag = False
            self.updateGraphicItem(visualItem)
            self.dockContentWidget4ForLoggingMessage._InfoMessage("Design Parameter Created")

            vi = VisualizationItem._VisualizationItem()
            self._layerItem = vi.returnLayerDict()

            self.dockContentWidget1_2.layer_table_widget.send_listInLayer_signal.connect(self.scene.getNonselectableLayerList)
            self.dockContentWidget1_2.layer_table_widget.updateLayerList(self._layerItem)

            try:
                if design_dict['constraint']:
                    self.dockContentWidget3_2.createNewConstraintAST(_id=design_dict['constraint_id'],
                                                                     _parentName=self._CurrentModuleName,
                                                                     _DesignConstraint=self._QTObj._qtProject._DesignConstraint)
            except:
                print("Invalid ast.")



    def deleteDesignParameter(self, dp_id, delete_dc=True):    # input : Design parameter ID
        """
        Deletes Actual Design Parameter module and visual item(if exists).
        If delete_dc == True:
            calls 'deleteDesignConstraint' and implements constraint deletion

        :param dp_id:
        :param delete_dc: True or False
        :return: None

        """
        # dp_module = dp_id[:-1]
        # while not dp_module in self._QTObj._qtProject._DesignParameter:
        #     dp_module = dp_module[:-1]
        dp_module = self._CurrentModuleName

        dc_id = self._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id(dp_id)

        deletionItems = [self.visualItemDict[dp_id]]     # Delete Visual Item
        for deleteItem in deletionItems:
            self.scene.removeItem(deleteItem)

        del self._QTObj._qtProject._DesignParameter[dp_module][dp_id]

        if delete_dc:
            self.deleteDesignConstraint(dc_id, delete_dp=False)

    def deleteDesignConstraint(self, dc_id, delete_dp=True):  # input : Design constraint ID
        """
        Deletes Actual Design Constraint module.
        If delete_dp == True:
            calls 'deleteDesignParameter' and implements parameter deletion

        :param dc_id:
        :param delete_dp:
        :return:
        """
        i = 0
        dc_module = dc_id[:-1]
        while not dc_module in self._QTObj._qtProject._DesignConstraint:
            dc_module = dc_module[:-1]
            i += 1
            if i > 500:
                warnings.warn(f'Invalid dc_id : {dc_id}.')
                return None

        self.dockContentWidget3.remove_item(dc_id)
        self.dockContentWidget3_2.remove_item(dc_id)
        del self._QTObj._qtProject._DesignConstraint[dc_module][dc_id]

        if delete_dp:
            try:
                dp_id = self._QTObj._qtProject._ElementManager.get_dp_id_by_dc_id(dc_id)  # get Design parameter ID
                self.deleteDesignParameter(dp_id, delete_dc=False)
            except:
                return None

    def updateXYCoordinatesForDisplay(self):
        print("debug,updateXYforDisplay")

        for module in self._QTObj._qtProject._DesignParameter:
            for id in self._QTObj._qtProject._DesignParameter[module]:
                if id in self.visualItemDict:
                    self._QTObj._qtProject._DesignParameter[module][id]._XYCoordinatesForDisplay = self.visualItemDict[id]._XYCoordinatesForDisplay



    def createVisualItemfromDesignParameter(self,DesignParameter):
        visualItem = VisualizationItem._VisualizationItem()
        # if visualItem._XYCoordinatesForDisplay
        visualItem.updateDesignParameter(DesignParameter)
        visualItem.setBoundingRegionGranularity(1)
        self.visualItemDict[DesignParameter._id] = visualItem

        visualItem.setToolTip(DesignParameter._id + '\n' + str(DesignParameter._type))

        return visualItem

    def updateVisualItemFromDesignParameter(self,DesignParameter):
        if DesignParameter is None:
            return None

        id = DesignParameter._id
        # self.visualItemDict[id].updateTraits(DesignParameter._DesignParameter)

        if id in self.visualItemDict:
            self.visualItemDict[id].updateTraits(DesignParameter._DesignParameter)
            self.visualItemDict[id]._id = id
            self.visualItemDict[id]._ItemTraits['_id'] = id
            self.visualItemDict[id]._ItemTraits['_ElementName'] = id
            return self.visualItemDict[id]
        return None

    def updateDesignParameter(self,_DesignParameter, element_manager_update = True):

        _ID = _DesignParameter['_id']
        _Module = self._CurrentModuleName

        if _DesignParameter['_id'] != _DesignParameter['_ElementName']:
            self.visualItemDict[_DesignParameter['_ElementName']] = self.visualItemDict.pop(_DesignParameter['_id'])


        for key in _DesignParameter:
            self._QTObj._qtProject._DesignParameter[_Module][_ID]._setDesignParameterValue(_index = key, _value= _DesignParameter[key])
        self._QTObj._qtProject._DesignParameter[_Module][_ID]._setDesignParameterName(_DesignParameter['_ElementName'])

        # self._QTObj._qtProject._DesignParameter[_Module][_ID]._updateVisualItem()
        # visualItem = self._QTObj._qtProject._DesignParameter[_Module][_ID]._VisualizationItemObj

        design_dict = self._QTObj._qtProject._update_design(design_type='parameter', module_name=self._CurrentModuleName,
                                                          dp_dict=_DesignParameter, id=_ID, element_manager_update =element_manager_update,
                                                            dummy_constraints = self._DummyConstraints)
        if design_dict['parameter']:
            design_dict['parameter'].update_unified_expression()
        visualItem = self.updateVisualItemFromDesignParameter(design_dict['parameter'])
        self.updateGraphicItem(visualItem)

        if design_dict['constraint_id']:
            self.dockContentWidget3_2.update_constraint_by_id(design_dict['constraint_id'])
            self.dockContentWidget3.update_constraint_by_id(design_dict['constraint_id'])

    def get_constraint_update_design(self, id, mother_id):
        if id:
            module = self.get_id_return_module(id,'_DesignConstraint')
            original_dp_id = self._QTObj._qtProject._ElementManager.get_dp_id_by_dc_id(id)
            design_dict = self._QTObj._qtProject._update_design(design_type='constraint', module_name=module,
                                                              _ast=self._QTObj._qtProject._DesignConstraint[module][id]._ast, id=id,
                                                                dummy_constraints = self._DummyConstraints)
            if design_dict['parameter']:
                if design_dict['parameter']._DesignParameter['_DesignParametertype'] == 3:
                    hierarchy_key = design_dict['parameter']._DesignParameter['_DesignObj_Name'] + '/' + str(
                        design_dict[
                            'parameter']._id)
                if original_dp_id != design_dict['parameter_id']:
                    self.visualItemDict[design_dict['parameter_id']] = self.visualItemDict.pop(original_dp_id)
                visualItem = self.updateVisualItemFromDesignParameter(design_dict['parameter'])
                visualItem._CreateFlag = False
                self.updateGraphicItem(visualItem)\
            # else:
            #     pass #exceptional case LATER ( not 1-to-1 matching constraint.... > cannot update visual item)
        if mother_id:
            module = self.get_id_return_module(mother_id, '_DesignConstraint')
            original_dp_id = self._QTObj._qtProject._ElementManager.get_dp_id_by_dc_id(mother_id)
            design_dict  = self._QTObj._qtProject._update_design(design_type='constraint', module_name=module,
                                                                _ast=self._QTObj._qtProject._DesignConstraint[module][
                                                                    mother_id]._ast, id=mother_id,
                                                                 dummy_constraints = self._DummyConstraints)
            if design_dict['parameter']:
                if design_dict['parameter']._DesignParameter['_DesignParametertype'] == 3:
                    hierarchy_key = design_dict['parameter']._DesignParameter['_DesignObj_Name'] + '/' + str(
                        design_dict[
                            'parameter']._id)
                if original_dp_id != design_dict['parameter_id']:
                    self.visualItemDict[design_dict['parameter_id']] = self.visualItemDict.pop(original_dp_id)
            try:
                visualItem = self.updateVisualItemFromDesignParameter(design_dict['parameter'])
                if visualItem:
                    visualItem._CreateFlag = False
                    self.updateGraphicItem(visualItem)
            except:
                traceback.print_exc()

                if design_dict['parameter']._DesignParameter['_DesignParametertype'] == 3:
                    new_key = design_dict['parameter']._DesignParameter['_DesignObj_Name'] + '/' + str(
                        design_dict['parameter']._ElementName)

                    if hierarchy_key in self.entireHierarchy[self._CurrentModuleName]:
                        self.entireHierarchy[self._CurrentModuleName][new_key] = self.entireHierarchy[
                            self._CurrentModuleName].pop(hierarchy_key)



    def deliveryDesignParameter(self):
        deliveryParameter = self.dockContentWidget2.DeliveryItem()
        self.dockContentWidget3_2.receiveDesignParameter(deliveryParameter)

    def send_array_variable(self, variable):
        if variable in self.dv.idDict:
            self.dv.idDict[variable]['id'].append(self.new_array_id)
        else:
            self.cv = variableWindow._createNewDesignVariable()
            self.cv.send_variable_signal.connect(self.dv.updateList)
            self.cv.addDVtodict(variable, 'id', self.new_array_id)
            self.cv.send_variable_signal.emit([variable, ''], 'add')

    def createNewConstraint(self,_ConstraintParameter):
        if self._QTObj._qtProject == None:
            self.warning=QMessageBox()
            self.warning.setText("There is no Project")
            self.warning.show()
            self.dockContentWidget4ForLoggingMessage._WarningMessage("Create DesignConstraint Fail: There is no Project")
        elif self._CurrentModuleName is None:
            self.warning=QMessageBox()
            self.warning.setText("There is No Module")
            self.warning.show()
            self.dockContentWidget4ForLoggingMessage._WarningMessage("Create DesignConstraint Fail: There is no Module")
        else:

            _designConstraintID = self._QTObj._qtProject._getDesignConstraintId(self._CurrentModuleName)
            _newConstraintID = (self._CurrentModuleName + str(_designConstraintID))
            self._QTObj._qtProject._createNewDesignConstraint(_id = _newConstraintID, _type= _ConstraintParameter['Type'], _ParentName= self._CurrentModuleName)
            print(self._QTObj._qtProject._DesignConstraint[self._CurrentModuleName][_newConstraintID])
            for key in _ConstraintParameter:
                if key == "Type":
                    continue
                # print(_ConstraintParameter[key])
                # self._QTObj._qtProject._DesignConstraint[self._CurrentModuleName][_newConstraintID]._setDesignConstraintValue(key,_ConstraintParameter[key])
            self._QTObj._qtProject._DesignConstraint[self._CurrentModuleName][_newConstraintID]._setDesignConstraintValue('_id',_newConstraintID)
            print(self._QTObj._qtProject._DesignConstraint[self._CurrentModuleName][_newConstraintID])
            print("DesignParameter ids ", self._QTObj._qtProject._DesignConstraint[self._CurrentModuleName].keys())
            DC = self._QTObj._qtProject._DesignConstraint[self._CurrentModuleName][_newConstraintID]
            # self.dockContentWidget3_2.createNewConstraint(_id=_newConstraintID, _parentName=self._CurrentModuleName, _DesignConstraint=self._QTObj._qtProject._DesignConstraint)

    def createNewConstraintPyCode(self,_PyCode):

        if self._QTObj._qtProject == None:
            self.warning=QMessageBox()
            self.warning.setText("There is no Project")
            self.warning.show()
            self.dockContentWidget4ForLoggingMessage._WarningMessage("Create DesignConstraint Fail: There is no Project")
        elif self._CurrentModuleName is None:
            self.warning=QMessageBox()
            self.warning.setText("There is No Module")
            self.warning.show()
            self.dockContentWidget4ForLoggingMessage._WarningMessage("Create DesignConstraint Fail: There is no Module")
        else:
            try:
                a , id = self._QTObj._qtProject._createNewDesignConstraintAST( _ASTDtype = "pyCode",_ParentName=self._CurrentModuleName, _pyCode=_PyCode)

                self.dockContentWidget3_2.createNewConstraintAST(_id=id, _parentName=self._CurrentModuleName,_DesignConstraint=self._QTObj._qtProject._DesignConstraint)

            except:
                self.warning = QMessageBox()
                self.warning.setText("Syntax Error")
                self.warning.show()
                self.dockContentWidget4ForLoggingMessage._WarningMessage("Create DesignConstraint Fail: Source Code syntax error")

    def updateVariableConstraint(self,_changedVariableInfo):
        """
        This function should only implemented by changing original data.
        'Add' button inside Variable window will temporarily call this function, which will be rejected @ try, except
        statement.
        :param _changedVariableInfo: {'_vid of changing var' : { 'DV' : name, 'value': value }
        :return:
        Minsu Kim
        """
        _VariableID = list(_changedVariableInfo.keys())[0]
        _VariableName = _changedVariableInfo[_VariableID]['DV']
        _VariableValue = _changedVariableInfo[_VariableID]['value']
        ############ Orignal Value Extraction from _vid Info #####################
        try:
            """
            check whether Add mode called this function. Unless, continue
            기존에 담겨 있는 값이 있어야만 아래 구문이 실행되고, 그렇지 않으면 오류 발생되도록
            """
            _originalName = self._VariableIDwithAST.variableIDwithASTDict[_VariableID].name
        except:
            """
            If Add mode called this function, there is no Constraint to be updated: reject
            """
            return
        ######################## Constraint(AST) Edition ##########################
        print("###############################################################")
        print("           Argument Variable ast Modification Start            ")
        print("###############################################################")
        _Constraints = self._QTObj._qtProject._DesignConstraint
        moduleName = list(_Constraints.values())[0]
        print(f" Modifying Constraint name:\n {_originalName} -> {_VariableName}, VID : {_VariableID}")
        # Constraint update
        for _, module in moduleName.items():
            if (module._ast.name == _originalName):
                module._ast.name = _VariableName    # Automatically change information inside VariableDictwithAST Object
                try:  # Case when changed Item is in the left dockWidget(3)
                    _changedItem = self.dockContentWidget3.model.findItems(module._id, column=1)[0]
                    _changedItemIndex = self.dockContentWidget3.model.indexFromItem(_changedItem)
                    self.dockContentWidget3.refreshItem(_changedItemIndex)

                except:  # Case when changed Item is in the right dockWidget(3_2)
                    try:
                        _changedItem = self.dockContentWidget3_2.model.findItems(module._id, column=1)[0]
                        _changedItemIndex = self.dockContentWidget3_2.model.indexFromItem(_changedItem)
                        self.dockContentWidget3_2.refreshItem(_changedItemIndex)
                    except:
                        raise NotImplementedError
                        return
                print(" Constraint Update Done ")
                print("###############################################################")
                print("           Argument Variable ast Modification Done             ")
                print("###############################################################")

                break

    def createDummyConstraint(self, type_for_dc:str, info_dict:dict):
        """
        For Constraints that do not contain any detailed info
        XY Coordinates, Loops, ... etc.
        :return:
        """
        dockContentFlag = True
        if type_for_dc == "LogicExpressionD":
            type_for_dc = "LogicExpression"
            self.send_width_height_ast_signal.connect(self.vw.variable_widget.get_width_height_ast)
            dockContentFlag = False
        if type_for_dc == "LogicExpressionD_sref":
            type_for_dc = "LogicExpression"
            self.send_sref_param_signal.connect(self.ls.get_param_value_ast)
            dockContentFlag = False
        if self._QTObj._qtProject == None:
            self.warning = QMessageBox()
            self.warning.setText("There is no Project")
            self.warning.show()
            self.dockContentWidget4ForLoggingMessage._WarningMessage(
                "Create DesignConstraint Fail: There is no Project")
        elif self._CurrentModuleName is None:
            self.warning = QMessageBox()
            self.warning.setText("There is No Module")
            self.warning.show()
            self.dockContentWidget4ForLoggingMessage._WarningMessage("Create DesignConstraint Fail: There is no Module")
        else:
            if type_for_dc == 'PathXY_row':
                try:
                    _ASTForVariable = ASTmodule._Custom_AST_API()
                    _ASTtype = 'XYCoordinate'
                    _ASTobj = _ASTForVariable._create_variable_ast_with_name(_ASTtype)

                    _designConstraintID = self._QTObj._qtProject._getDesignConstraintId(self._CurrentModuleName)
                    _newConstraintID = (self._CurrentModuleName + str(_designConstraintID))

                    _ASTobj.id = _newConstraintID
                    _ASTobj._id = _newConstraintID
                    _ASTobj._type = 'XYCoordinate'
                    _ASTobj.info_dict = info_dict
                    self._DummyConstraints.XYDict[_newConstraintID] = info_dict
                    design_dict = self._QTObj._qtProject._feed_design(design_type='constraint',
                                                                      module_name=self._CurrentModuleName,
                                                                      _ast=_ASTobj, element_manager_update=True)
                    self.calculator_window.send_dummyconstraints_signal.emit(info_dict, _newConstraintID)
                    self.calculator_window.send_path_row_xy_signal.emit(_ASTobj, _newConstraintID)
                except:
                    raise Exception("Sending XYCoordinate For Path Failed!")
                    traceback.print_exc()
            else:
                try:
                    print("###############################################################")
                    print(f"                  {type_for_dc} ast creation Start                    ")
                    print("###############################################################")
                    _ASTForVariable = ASTmodule._Custom_AST_API()
                    _ASTtype = type_for_dc
                    _ASTobj = _ASTForVariable._create_variable_ast_with_name(_ASTtype)

                    _designConstraintID = self._QTObj._qtProject._getDesignConstraintId(self._CurrentModuleName)
                    _newConstraintID = (self._CurrentModuleName + str(_designConstraintID))

                    _ASTobj.id = _newConstraintID
                    _ASTobj._id = _newConstraintID
                    _ASTobj._type = type_for_dc
                    _ASTobj.info_dict = info_dict
                    # self.calculator_window.send_dummyconstraints_signal.emit(info_dict, _newConstraintID)
                    if dockContentFlag == True:
                        design_dict = self._QTObj._qtProject._feed_design(design_type='constraint',
                                                                          module_name=self._CurrentModuleName,
                                                                          _ast=_ASTobj)
                        self.dockContentWidget3_2.createNewConstraintAST(_id=design_dict['constraint_id'],
                                                                         _parentName=self._CurrentModuleName,
                                                                         _DesignConstraint=self._QTObj._qtProject._DesignConstraint)

                    ############################## Dummy Constraint Management #############################
                    if (type_for_dc == 'XYCoordinate') or (type_for_dc == 'PathXY') or (type_for_dc == 'LogicExpression'):
                        self.calculator_window.send_dummyconstraints_signal.emit(info_dict, _newConstraintID)
                        if (type_for_dc == 'XYCoordinate'):
                            # self._DummyConstraints.XYDict[_newConstraintID] = info_dict
                            pass
                        elif (type_for_dc == 'PathXY'):
                            # self._DummyConstraints.XYPathDict[_newConstraintID] = info_dict
                            pass
                        elif (type_for_dc == 'LogicExpression'):
                            # self._DummyConstraints.ExpressionDict[_newConstraintID] = info_dict
                            self.send_width_height_ast_signal.emit(_newConstraintID, _ASTobj)
                            self.send_sref_param_signal.emit(_newConstraintID, _ASTobj)
                    elif type_for_dc == 'Array':
                        # self._DummyConstraints.ArrayDict[_newConstraintID] = info_dict
                        self.new_array_id = _newConstraintID
                    #########################################################################################
                    print("###############################################################")
                    print(f"                  {type_for_dc} ast creation Done                    ")
                    print("###############################################################")
                except:
                    print("###############################################################")
                    print(f"                  {type_for_dc} ast creation Failed                  ")
                    print("###############################################################")
                    traceback.print_exc()




    def createVariableConstraint(self, _VariableInfo):
        """
        Creates / Updates Variable AST when button clicked
        :param _VariableInfo: { vid: {name = '', value = ''}}
        :return:
        """
        if self._QTObj._qtProject == None:
            self.warning=QMessageBox()
            self.warning.setText("There is no Project")
            self.warning.show()
            self.dockContentWidget4ForLoggingMessage._WarningMessage("Create DesignConstraint Fail: There is no Project")
        elif self._CurrentModuleName is None:
            self.warning=QMessageBox()
            self.warning.setText("There is No Module")
            self.warning.show()
            self.dockContentWidget4ForLoggingMessage._WarningMessage("Create DesignConstraint Fail: There is no Module")
        else:       # create / update ArgumentVariable AST
            _VariableID = list(_VariableInfo.keys())[0]
            _VariableName = _VariableInfo[_VariableID]['DV']
            print("###############################################################")
            print("             Argument Variable ast creation Start              ")
            print("###############################################################")

            _ASTForVariable = ASTmodule._Custom_AST_API()
            _ASTtype = 'ArgumentVariable'
            _ASTobj = _ASTForVariable._create_variable_ast_with_name(_ASTtype)

            print(f"AST INFO: \n ID = {_VariableID}, NAME = {_VariableName}")
            try:
                if (_VariableName == '' or None):
                    print("Invalid Name input")
                    raise NotImplementedError
                else:
                    _ASTobj.__dict__['name'] = _VariableName
                    self._VariableIDwithAST.variableIDwithASTDict[_VariableID] = _ASTobj
                    design_dict = self._QTObj._qtProject._feed_design(design_type='constraint',
                                                                      module_name=self._CurrentModuleName, _ast=_ASTobj)
                    self.dockContentWidget3_2.createNewConstraintAST(_id=design_dict['constraint_id'],
                                                                     _parentName=self._CurrentModuleName,
                                                                     _DesignConstraint=self._QTObj._qtProject._DesignConstraint)
                    print("###############################################################")
                    print("              Argument Variable ast creation Done              ")
                    print("###############################################################")
            except:
                print("Argument Variable AST Creation failed")


    def createNewConstraintAST(self,_input):
        """
        Creates / Modifies Constraints(AST)
        :param _AST : AST or variable dictionary (type; AST or dict)
        :return:
        """
        if self._QTObj._qtProject == None:
            self.warning=QMessageBox()
            self.warning.setText("There is no Project")
            self.warning.show()
            self.dockContentWidget4ForLoggingMessage._WarningMessage("Create DesignConstraint Fail: There is no Project")
        elif self._CurrentModuleName == None:
            self.warning=QMessageBox()
            self.warning.setText("There is No Module")
            self.warning.show()
            self.dockContentWidget4ForLoggingMessage._WarningMessage("Create DesignConstraint Fail: There is no Module")
        else:
            if type(_input) != dict:    # input is AST type
                design_dict = self._QTObj._qtProject._feed_design(design_type='constraint', module_name=self._CurrentModuleName, _ast= _input)
                self.dockContentWidget3_2.createNewConstraintAST(_id=design_dict['constraint_id'],
                                                                 _parentName=self._CurrentModuleName,
                                                                 _DesignConstraint=self._QTObj._qtProject._DesignConstraint)
                # self._VariableIDwithAST.variableIDwithASTDict[_vid] = _AST
                try:
                    if design_dict['parameter'] is not None:
                        visualItem = self.createVisualItemfromDesignParameter(
                            self._QTObj._qtProject._DesignParameter[self._CurrentModuleName][design_dict['parameter_id']])
                        self.updateGraphicItem(visualItem)

                except:
                    print("Invalid design parameter dict")

            else:
                if (_input) != None:
                    _targetVid = list(_input.keys())[0]
                    if _targetVid in list(self._VariableIDwithAST.variableIDwithASTDict.keys()):
                        self.warning = QMessageBox()
                        self.warning.setIcon(QMessageBox.Warning)
                        self.warning.setText("Target Variable already exists as a constraint")
                        self.warning.show()
                        print("Target Variable already exists as a constraint")
                        return
                    else:
                        self.createVariableConstraint(_input)
                else:
                    print(" AST or Variable Info needed!")

    def constraintConvey(self):
        self.dockContentWidget3._DesignConstraintFromQTobj = self._QTObj._qtProject._DesignConstraint
        self.dockContentWidget3_2._DesignConstraintFromQTobj = self._QTObj._qtProject._DesignConstraint

    def convey_element_manager(self):
        SetupWindow._ConstraintTreeViewWidgetAST._ElementMangerFromQTobj = self._QTObj._qtProject._ElementManager

    def constraintUpdate1(self, updateDict):
        _id = updateDict['_id']
        _Module = self.get_id_return_module(_id,'_DesignConstraint')
        # _Module = re.sub('[0-9]+', '', _id)

        for key in updateDict:
            if type(updateDict[key]) == list:       #If UpdateDict[key] is compound stmt.
                for i, stmtID in enumerate(updateDict[key]):
                    tmpModule = self.get_id_return_module(stmtID,'_DesignConstraint')
                    # tmpModule = re.sub('[0-9]+', '', stmtID)
                    astObj = self._QTObj._qtProject._DesignConstraint[tmpModule][stmtID]._ast
                    updateDict[key][i] = astObj
            else:  # It could be simple stmt or just value
                tmpID = updateDict[key]
                try:  # Simple Stmt Case
                    tmpModule = self.get_id_return_module(tmpID,'_DesignConstraint')
                    # tmpModule = re.sub('[0-9]+', '', tmpID)
                    updateDict[key] = self._QTObj._qtProject._DesignConstraint[tmpModule][tmpID]._ast
                except:  # Just value case
                    print('debug, key = {}, module = {}, id = {}'.format(key, tmpModule, tmpID))
                    pass
        self._QTObj._qtProject._setDesignConstraintValueWithSTMT(_module=_Module,_id=_id,_STMT=updateDict)
        _STMT = self._QTObj._qtProject._DesignConstraint[_Module][_id]._readConstraintValueAsSTMT()

        self.dockContentWidget3.receiveConstraintSTMT(_STMT)

    def constraintUpdate2(self, updateDict):
        _id = updateDict['_id']
        _Module = self.get_id_return_module(_id, '_DesignConstraint')
        # _Module = re.sub('[0-9]+', '', _id)

        for key in updateDict:
            if type(updateDict[key]) == list:       #If UpdateDict[key] is compound stmt.
                for i, stmtID in enumerate(updateDict[key]):
                    tmpModule = self.get_id_return_module(stmtID, '_DesignConstraint')
                    # tmpModule = re.sub('[0-9]+', '', stmtID)
                    astObj = self._QTObj._qtProject._DesignConstraint[tmpModule][stmtID]._ast
                    updateDict[key][i] = astObj
            else:   # It could be simple stmt or just value
                tmpID = updateDict[key]
                try:    # Simple Stmt Case
                    tmpModule = self.get_id_return_module(tmpID, '_DesignConstraint')
                    # tmpModule = re.sub('[0-9]+', '', tmpID)
                    updateDict[key] = self._QTObj._qtProject._DesignConstraint[tmpModule][tmpID]._ast
                except: # Just value case
                    print('debug, key = {}, module = {}, id = {}'.format(key,tmpModule,tmpID))
                    pass



        self._QTObj._qtProject._setDesignConstraintValueWithSTMT(_module=_Module,_id=_id,_STMT=updateDict)
        _STMT = self._QTObj._qtProject._DesignConstraint[_Module][_id]._readConstraintValueAsSTMT()

        self.dockContentWidget3_2.receiveConstraintSTMT(_STMT)


    def setRootConstraint(self,_id):
        _Module = re.sub('[0-9]+', '',_id)
        self._QTObj._qtProject._setRootDesignConstraint(_id=_id,_ParentName=_Module)

    def saveConstraint(self):
        scf = QFileDialog.getSaveFileName(self,'Save file','./PyQTInterface/json/')

        try:
            cm = self._CurrentModuleName
            # _data=self._QTObj._qtProject._ParseTreeForDesignConstrain[self._CurrentModuleName]._ParseTree
            _file=scf[0]

            self._QTObj._qtProject._SaveDataAsJsonFormat(_data=self._QTObj._qtProject._ParseTreeForDesignConstrain[self._CurrentModuleName]._ParseTree, _file=scf[0])
        except:
            print("Save Constraint Failed")
            self.dockContentWidget4ForLoggingMessage._WarningMessage("Save DesignConstraint Fail: Unknown")
            pass


    def saveConstraintP(self):
        scf = QFileDialog.getSaveFileName(self,'Save file','./PyQTInterface/json/')

        try:
            cm = self._CurrentModuleName
            #_data=self._QTObj._qtProject._ParseTreeForDesignConstrain[self._CurrentModuleName]._ParseTree
            _file=scf[0]

            self._QTObj._qtProject._saveDesignConstraintAsPickle( _file=scf[0])
        except:
            print("Save Constraint Failed")
            self.dockContentWidget4ForLoggingMessage._WarningMessage("Save DesignConstraint Fail: Unknown")
        scf = QFileDialog.getOpenFileName(self,'Load file','./')
        try:
            # cm = self._CurrentModuleName
            # _data=self._QTObj._qtProject._ParseTreeForDesignConstrain[self._CurrentModuleName]._ParseTree
            # _file=scf[0]

            self._QTObj._qtProject._loadDesignConstraintAsPickle(_file=scf[0])
            for module in self._QTObj._qtProject._DesignConstraint:
                _rootSTMTlist = ASTmodule._convertPyCodeToSTMTlist[self._QTObj._qtProject._ParseTreeForDesignConstrain[module]._ast]

            # for module in self._QTObj._qtProject._DesignConstraint:
                # self._QTObj._qtProject._DesignConstraint[module][]
        except:
            print("Load Constraint Failed")
            self.dockContentWidget4ForLoggingMessage._WarningMessage("Load DesignConstraint Fail: Unknown")
            pass

    def loadConstraintP(self):
        scf = QFileDialog.getOpenFileName(self,'Load file','./')
        try:
            # cm = self._CurrentModuleName
            # _data=self._QTObj._qtProject._ParseTreeForDesignConstrain[self._CurrentModuleName]._ParseTree
            # _file=scf[0]

            self._QTObj._qtProject._loadDesignConstraintAsPickle(_file=scf[0])
            # for module in self._QTObj._qtProject._DesignConstraint:
            #     self._QTObj._qtProject._DesignConstraint[module][]

        except:
            print("Load Constraint Failed")
            self.dockContentWidget4ForLoggingMessage._WarningMessage("Save DesignConstraint Fail: Unknown")
            pass

    def constraint_data_changed(self, constraint_id):
        '''
        This function is called when items in Design Constraint are changed.
        :param constraint_id: changed constraint id
        :return: None
        '''
        def parse_constraint_to_get_value(_ast):
            variable_visitor = element_ast.VariableNameVisitor()
            if '_type' not in _ast.__dict__:
                _ast._type = ASTmodule._getASTtype(_ast)

            if _ast._type == 'Boundary':
                for _field in _ast._fields:
                    if type(_ast.__dict__[_field]) == list and len(_ast.__dict__[_field]) > 0:
                        if '_ast' in str(type(_ast.__dict__[_field][0])):
                            continue
                    if _field == 'name' or _field == 'layer':
                        continue
                    tmp_ast = ast.parse(str(_ast.__dict__[_field]))
                    print()
                    variable_visitor.visit(tmp_ast)

            elif _ast._type == 'Path':
                for _field in _ast._fields:
                    if type(_ast.__dict__[_field]) == list and len(_ast.__dict__[_field]) > 0:
                        if '_ast' in str(type(_ast.__dict__[_field][0])):
                            continue
                    if _field == 'name' or _field == 'layer':
                        continue
                    tmp_ast = ast.parse(str(_ast.__dict__[_field]))
                    variable_visitor.visit(tmp_ast)

            elif _ast._type == 'Sref':
                for _field in _ast._fields:
                    if type(_ast.__dict__[_field]) == list and len(_ast.__dict__[_field]) > 0:
                        if '_ast' in str(type(_ast.__dict__[_field][0])):
                            continue
                    if _field == 'name' or _field == 'library' or _field == 'className' or _field == 'calculate_fcn':
                        continue
                    elif _field == 'parameters':
                        for parm_string in _ast.parameters.values():
                            tmp_ast = ast.parse(str(parm_string))
                            variable_visitor.visit(tmp_ast)
                    # elif _field == 'XY':
                    #     # if type(_ast.XY) == list and not _ast.XY:
                    #     #     tmp
                    #     tmp_ast = ast.parse(str(_ast.__dict__[_field]))
                    #     variable_visitor.visit(tmp_ast)
                    else:
                        tmp_ast = ast.parse(str(_ast.__dict__[_field]))
                        variable_visitor.visit(tmp_ast)

            variable_name_set = set(variable_visitor.variable_name_list)
            return list(variable_name_set)

        changed_dp_id = self._QTObj._qtProject._ElementManager.get_dp_id_by_dc_id(constraint_id)
        if changed_dp_id:
            old_variable_dict = copy.deepcopy(self.visualItemDict[changed_dp_id]._ItemTraits['variable_info'])
            module_name = self.get_id_return_module(constraint_id,'_DesignConstraint')
            used_variable_list = parse_constraint_to_get_value(self._QTObj._qtProject._DesignConstraint[module_name][constraint_id]._ast)
            # try:
            #     self.visualItemDict[changed_dp_id].update_dc_variable_info(self._QTObj._qtProject._DesignConstraint[module_name][constraint_id]._ast)
            # except:
            #     traceback.print_exc()
            # erased_variable_list = list(set(old_variable_list)-set(used_variable_list))
            current_variable_dict = self.visualItemDict[changed_dp_id]._ItemTraits['variable_info']
            tmpList=list()

            for key in old_variable_dict:
                if old_variable_dict[key] == current_variable_dict[key]:
                    pass
                else:
                    tmpList.append(old_variable_dict[key])
            # old_variable_list = list(set(self.variable_store_list) - set(used_variable_list))
            # self.variable_store_list = used_variable_list
            # print( self.visualItemDict[changed_dp_id]._ItemTraits['variable_info'])

            for var in used_variable_list:
                if var in self.dv.idDict:
                    self.dv.idDict[var]['id'].append(changed_dp_id)
                else:
                    self.cv = variableWindow._createNewDesignVariable()
                    self.cv.send_variable_signal.connect(self.dv.updateList)
                    self.cv.addDVtodict(var, 'id', changed_dp_id)
                    self.cv.send_variable_signal.emit([var, ''], 'add')

            #TODO Debug:
            # 보기에 old_variable_list가 정확하지 않아보임.. a라는 boundary에 변수 수정하다가, b 라는 path 변수 수정하면 날라감
            try:
                for var in tmpList:
                    if var in self.dv.idDict:
                        if changed_dp_id in self.dv.idDict[var]['id']:
                            self.dv.idDict[var]['id'].remove(changed_dp_id)
            except:
                traceback.print_exc()
                #TODO
                # 여기 디버그좀 부탁함당
                # 가끔씩 unhashable type: 'list' 라고 if var in tmpList 구문에서 떠요.

        #######STATIC CONSTRAINT AST DEBUGGING PART###########
        sender = self.sender()
        sender.blockSignals(True)
        try:
            # tested_ast = self.transform_constraints([self._QTObj._qtProject._DesignConstraint[self._CurrentModuleName][constraint_id]._ast])
            tested_ast = ASTmodule.run_transformer([self._QTObj._qtProject._DesignConstraint[self._CurrentModuleName][constraint_id]._ast])
            code = astunparse.unparse(tested_ast)
            sender.set_errored_constraint_id(constraint_id, 'clean')
        except Exception as e:
            error_log = traceback.format_exc()
            sender.set_errored_constraint_id(constraint_id, 'static', error_log, exception = e)
        sender.blockSignals(False)

    def highlightVI(self, _idlist):
        for item in self.visualItemDict:
            self.visualItemDict[item].setSelected(False)
        for _id in _idlist:
            self.visualItemDict[_id].setFlag(QGraphicsItemGroup.ItemIsSelectable, True)
            self.visualItemDict[_id].setSelected(True)

    def highlightVI_by_hierarchy_list(self, _hierarchy_list):
        top_element_name = _hierarchy_list.pop(0)
        top_element_name = top_element_name.split('[')[0]
        self.visualItemDict[top_element_name].highlight_element_by_hierarchy(_hierarchy_list)

    def change_used_variable_name(self, _id_list):
        print(_id_list)

    def makeTemplateWindow(self):
        self.tw = template._TemplateManageWidget(template.templateDict)
        self.tw.show()
        self.tw.send_TemplateName_signal.connect(self.loadTemplate)

    def loadTemplate(self,templateName):
        try:
            # getConstraintTemplate = \
            # a= template.templateDict[templateName]
            # b = self._QTObj
            # c = self._CurrentModuleName
            templatetmp = template._Template()
            getConstraintTemplate = templatetmp.createConstraintFromTemplate(_templateDict=template.templateDict[templateName],_QTObj=self._QTObj,_ModuleName=self._CurrentModuleName)
            self.dockContentWidget3_2.updateConstraintDictFromQTInterface(self._QTObj._qtProject)
            self.dockContentWidget3.updateConstraintDictFromQTInterface(self._QTObj._qtProject)
            self.dockContentWidget3_2.receiveConstraint(getConstraintTemplate)
        except:
            print("fail")
            pass

    def parameterToTemplateHandler(self,designParameterItemIDList,type):
        if type == 5:
            return
        designParameterList = list()
        for id in designParameterItemIDList:
            module = self.get_id_return_module(id,'_DesignParameter')
            # # module = re.sub('[0-9]+', '',id)
            # module = id[:-1]
            # while not module in self._QTObj._qtProject._DesignParameter:
            #     module = module[:-1]
            designParameterList.append(self._QTObj._qtProject._DesignParameter[module][id]._DesignParameter)
        templatetmp = template._Template()
        try:
            receiveConstraintList = templatetmp.receiveDesignParameters(designParameterList=designParameterList,_QTObj=self._QTObj,_ModuleName=self._CurrentModuleName,type=type)
        except:
            pass

        try:
            for constraint in receiveConstraintList:
                self.dockContentWidget3_2.updateConstraintDictFromQTInterface(self._QTObj._qtProject)
                self.dockContentWidget3.updateConstraintDictFromQTInterface(self._QTObj._qtProject)
                self.dockContentWidget3_2.createNewConstraint(constraint)
        except:
            pass

    def constraintToTemplateHandler(self,designConstraint):
        # designConstraintList = list()
        # for id in designConstraintIDList:
        #     module = re.sub('[0-9]+', '',id)
        #     designConstraintList.append(self._QTObj._qtProject._DesignConstraint[module][id]._DesignConstraint)
        templatetmp = template._Template()
        try:
            receiveConstraint = templatetmp.receiveDesignConstraints(designConstraintList=designConstraint,_QTObj=self._QTObj,_ModuleName=self._CurrentModuleName)

            self.dockContentWidget3_2.updateConstraintDictFromQTInterface(self._QTObj._qtProject)
            self.dockContentWidget3.updateConstraintDictFromQTInterface(self._QTObj._qtProject)
            self.dockContentWidget3_2.createNewConstraint(receiveConstraint)
        except:
            pass

    def variableListUpdate(self):
        try:
            for module in self._QTObj._qtProject._DesignConstraint:
                for id in self._QTObj._qtProject._DesignConstraint[module]:
                    if self._QTObj._qtProject._DesignConstraint[module][id]._type == "variable":
                        name = self._QTObj._qtProject._DesignConstraint[module][id]._ParseTree['_name']
                        if not name in self.variableList:
                            self.variableList.append(name)
                    elif self._QTObj._qtProject._DesignConstraint[module][id]._type == "dictionaryElement":
                        try:
                            name = self._QTObj._qtProject._DesignConstraint[module][id]._ParseTree['_dictionaryElement'][0]
                            if not name in self.variableList:
                                self.variableList.append(name)
                        except:
                            pass
        except:
            print('fail')

        if len(self.variableList) != 0:
            self.vcw = template._VariableListWidget(self.variableList)
            self.vcw.show()
            self.vcw.send_VariableName_signal.connect(self.variableNameToTemplateHandler)
        else:
            self.warning = QMessageBox()
            self.warning.setText("There is no Variable")
            self.warning.show()

    def variableNameToTemplateHandler(self,variableName):
        templatetmp = template._Template()
        receiveConstraint = templatetmp.receiveVariableName(variableName,self._QTObj,self._CurrentModuleName)
        self.dockContentWidget3_2.updateConstraintDictFromQTInterface(self._QTObj._qtProject)
        self.dockContentWidget3.updateConstraintDictFromQTInterface(self._QTObj._qtProject)
        self.dockContentWidget3_2.createNewConstraint(receiveConstraint)

    def easyDebugMode(self):
        self._QTObj._createProject("ProjectForEasyDebug")
        self.set_module_name("EasyDebugModule")


    def get_id_return_module(self, id : str, type : str):
        """
        :param id:
        :param type: '_DesignParameter' or '_DesignConstraint'
        :return:
        """
        module = id
        while 1:
            module = module[:-1]
            if module in self._QTObj._qtProject.__dict__[type]:
                return module


class _CustomView(QGraphicsView):
    variable_signal = pyqtSignal(str)
    send_design_message = pyqtSignal(delegator.DelegateMessage)
    send_widget_message = pyqtSignal(delegator.DelegateMessage)
    nameout_signal = pyqtSignal(str)
    name_list_signal = pyqtSignal(list, list)

    def __init__(self):
        super(_CustomView, self).__init__()
        self.show()
        self.setMouseTracking(True)
        self.getModule=None

    def wheelEvent(self, QWheelEvent):
        zoomInFactor = 1.25
        zoomOutFactor = 1 / zoomInFactor
        self.setTransformationAnchor(QGraphicsView.NoAnchor)
        self.setResizeAnchor(QGraphicsView.NoAnchor)

        oldPosition = self.mapToScene(QWheelEvent.pos())

        if QWheelEvent.angleDelta().y() >0 :
            zoom = zoomInFactor
        else:
            zoom = zoomOutFactor
        self.scale(zoom,zoom)

        newPosition = self.mapToScene(QWheelEvent.pos())

        delta = newPosition - oldPosition
        self.translate(delta.x(),delta.y())

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_F:
            print(self.scene().fit_in_view_dict)
            top_left = QPointF(min(self.scene().fit_in_view_dict['left']),max(self.scene().fit_in_view_dict['top']))
            bottom_right = QPointF(max(self.scene().fit_in_view_dict['right']),min(self.scene().fit_in_view_dict['bottom']))
            self.fitInView(QRectF(top_left, bottom_right),Qt.KeepAspectRatio)

            # top_left = QPointF(self.scene().fit_in_view_dict['left'],self.scene().fit_in_view_dict['top'])
            # bottom_right = QPointF(self.scene().fit_in_view_dict['right'],self.scene().fit_in_view_dict['bottom'])
            # self.fitInView(QRectF(top_left, bottom_right),Qt.KeepAspectRatio)

            # every_item = self.scene().items()
            # tmp_group_item = QGraphicsItemGroup()
            # for item in every_item:
            #     if type(item) == VisualizationItem._VisualizationItem:
            #         item.setSelected(False)
            #         if item._subCellFlag:
            #             pass
            #         else:
            #             tmp_group_item.addToGroup(item)
            # # map(lambda item: tmp_group_item.addToGroup(item), every_item)
            #
            # self.scene().addItem(tmp_group_item)
            # self.fitInView(tmp_group_item,Qt.KeepAspectRatio)
            # self.scene().destroyItemGroup(tmp_group_item)
            # del tmp_group_item
            # self.fitInView(self.scene().ghost_group_item,Qt.KeepAspectRatio)
        elif QKeyEvent.key() == Qt.Key_Z:
            self.fitInView(QRectF(-650,-345,1300,690))
            # self.centerOn(QPointF(0,0))

        super().keyPressEvent(QKeyEvent)

    def mousePressEvent(self, event) -> None:
        print()
        if event.button() == Qt.RightButton:
            # print('return')
            return
        # super(_CustomView, self).mousePressEvent(event)
        super().mousePressEvent(event)

    # def dropEvent(self, event) -> None:
    #     super
    def contextMenuEvent(self, event) -> None:
        constraint_create_array = QAction("create array", self)
        convert_to_sref = QAction("convert to sref", self)
        inspect_path_connection = QAction("create auto path", self)
        variable_create_array = QAction("create array variable", self)
        variable_create_distance = QAction("create distance variable", self)
        variable_create_enclosure = QAction("create enclousre variable", self)
        variable_create_connect = QAction("create connect variable", self)
        visual_ungroup = QAction("ungroup multiple xy index cells", self)
        visual_ungroup.setShortcut('Ctrl+G')

        menu = QMenu(self)
        menu.addAction(constraint_create_array)
        menu.addAction(convert_to_sref)
        menu.addAction(inspect_path_connection)
        menu.addAction(variable_create_array)
        menu.addAction(variable_create_distance)
        menu.addAction(variable_create_enclosure)
        menu.addAction(variable_create_connect)
        menu.addAction(visual_ungroup)

        if self.scene().selectedItems():
            if self.scene().selectedItems()[0]._ItemTraits['_DesignParametertype'] == 1:
               constraint_create_array.triggered.connect(lambda tmp: self.variable_emit('boundary_array'))
            elif self.scene().selectedItems()[0]._ItemTraits['_DesignParametertype'] == 2:
               constraint_create_array.triggered.connect(lambda tmp: self.variable_emit('path_array'))
            elif self.scene().selectedItems()[0]._ItemTraits['_DesignParametertype'] == 3:
               constraint_create_array.triggered.connect(lambda tmp: self.variable_emit('sref_array'))
        else:
            constraint_create_array.triggered.connect(lambda tmp: self.variable_emit('boundary_array'))
        convert_to_sref.triggered.connect(lambda tmp: self.variable_emit('to_sref'))
        inspect_path_connection.triggered.connect(lambda tmp: self.variable_emit('auto_path'))
        variable_create_array.triggered.connect(lambda tmp: self.variable_emit('array'))
        variable_create_distance.triggered.connect(lambda tmp: self.variable_emit('distance'))
        variable_create_enclosure.triggered.connect(lambda tmp: self.variable_emit('enclosure'))
        variable_create_connect.triggered.connect(lambda tmp: self.variable_emit('connect'))
        visual_ungroup.triggered.connect(self.scene().ungroup_indexed_item)


        menu.exec(event.globalPos())

    def variable_emit(self, type):
        if type == 'boundary_array':
            self.variable_signal.emit('boundary_array')
        elif type == 'to_sref':
            selected_vis_items = self.scene().selectedItems()
            message = delegator.DelegateMessage(arguments=[selected_vis_items], target_fcn='convert_elements_to_sref_widget')
            self.send_widget_message.emit(message)
            # self.send_design_message.emit(message)
            # self.variable_signal.emit('to_sref')
        elif type == 'path_array':
            self.variable_signal.emit('path_array')
        elif type == 'sref_array':
            self.variable_signal.emit('sref_array')
        if type == 'auto_path':
            self.variable_signal.emit('auto_path')
        elif type == 'array':
            self.variable_signal.emit('element array')
        elif type == 'distance':
            self.variable_signal.emit('distance')
        elif type == 'enclosure':
            self.variable_signal.emit('enclosure')
        elif type == 'connect':
            self.variable_signal.emit('connect')
        # elif type == 'ungroup':
        #     self.variable_signal.emit('ungroup')


    def dragEnterEvent(self, event) -> None:
        print('ed')
        event.accept()
        event.proposedAction()
        super(self).dragEnterEvent(event)
    def dropEvent(self, event) -> None:
        event.accept()
        event.proposedAction()
        super(self).dropEvent(event)

    def name_out_fcn(self,name_list,index_list):
        if self.getModule == None:
            name_list.insert(0,None)
            index_list.insert(0,None)
        else:
            name_list.insert(0,self.getModule._ItemTraits['_ElementName'])
            if self.getModule._ItemTraits['_DesignParametertype'] == 1:
                index_list.insert(0,self.getModule.block[0].index)
            else:
                index_list.insert(0,self.getModule.index)
        self.name_list_signal.emit(name_list,index_list)

class _CustomScene(QGraphicsScene):
    send_debug_signal = pyqtSignal()
    send_xyCoordinate_signal = pyqtSignal(QGraphicsSceneMouseEvent)
    send_xy_signal = pyqtSignal(list)
    send_itemList_signal = pyqtSignal(list)
    send_move_item_signal = pyqtSignal(list, list, str)
    send_parameterIDList_signal = pyqtSignal(list,int)
    send_move_signal = pyqtSignal(QPointF)
    send_moveDone_signal = pyqtSignal()
    send_deleteItem_signal = pyqtSignal(str)
    send_module_name_list_signal = pyqtSignal(list, list)
    send_mouse_move_signal = pyqtSignal(QGraphicsSceneMouseEvent)
    send_mouse_move_xy_signal = pyqtSignal(list)
    send_selected_list_signal = pyqtSignal(list)

    send_show_variable_signal = pyqtSignal(QGraphicsItem)
    send_doubleclick_signal = pyqtSignal(bool)
    send_item_clicked_signal = pyqtSignal(VisualizationItem._VisualizationItem)
    send_change_background_siganl = pyqtSignal(int)

    viewList = []

    def __init__(self, axis=True):
        super().__init__()
        if axis:
            pen = QPen()
            pen.setStyle(Qt.DashLine)
            pen.setColor(Qt.GlobalColor.lightGray)
            pen.setCapStyle(Qt.RoundCap)
            pen.setWidth(3)

            self.addLine(QLineF(-1000000,0,1000000,0),pen)
            self.addLine(QLineF(0,-1000000,0,1000000),pen)

        # self.moveFlag = False
        self.listIgnoreFlag = False
        self.oldPos = QPointF(0,0)
        self.itemList = list()
        self.nslist = list()
        self.tmp_item_dict = dict()
        cursor_item = QPixmap(1,1)
        cursor_item.fill(Qt.yellow)
        self.cursor_item = self.addPixmap(cursor_item)
        # self.cursor_item = QGraphicsRectItem(0,0,1,1)
        # self.cursor_item.setBrush(Qt.yellow)
        # self.cursor_item.setPen(Qt.yellow)
        # self.addItem(self.cursor_item)
        self.point_items_memory = []
        self.selected_item_in_memory = None
        self.fit_in_view_dict = dict(top=list(),bottom=list(),left=list(),right=list())
        # self.fit_in_view_dict = dict(top=0,bottom=0,left=0,right=0)
        # self.ghost_group_item = QGraphicsItemGroup()
        # self.ghost_group_item.setFlag(f)
        # self.addItem(self.ghost_group_item)


    def change_background(self, state):
        if state == 2:
            user_setup._Night_mode = True
            self.setBackgroundBrush(QBrush(Qt.black))
        else:
            user_setup._Night_mode = False
            self.setBackgroundBrush(QBrush(Qt.white))
        self.send_change_background_siganl.emit(state)

    def getNonselectableLayerList(self, _layerlist):
        self.nslist = _layerlist

    def mousePressEvent(self, event):
        for highlighted_rectblock in VisualizationItem._RectBlock.highlighted_item_list:
            highlighted_rectblock.highlight_flag = False
        for s_highlighted_rectblock in VisualizationItem._RectBlock.shallow_highlight_list:
            s_highlighted_rectblock.shallow_highlight = False


        snap = user_setup.MIN_SNAP_SPACING
        x_point = int(int(event.scenePos().toPoint().x() / snap) * snap)
        y_point = int(int(event.scenePos().toPoint().y() / snap) * snap)
        self.send_xy_signal.emit([x_point, y_point])
        self.send_xyCoordinate_signal.emit(event)



        def masking(items):
            masked_output = []
            for item in items:
                if type(item) == VisualizationItem._VisualizationItem:
                    self.send_item_clicked_signal.emit(item)
                    if not item.parentItem():
                        if item not in masked_output:
                            masked_output.append(item)
                    else:
                        mother_item = item.parentItem()
                        if type(mother_item) == VisualizationItem._VisualizationItem:
                            if not mother_item.parentItem():
                                if mother_item is not None and mother_item not in masked_output:
                                    masked_output.append(mother_item)

            return masked_output

        items = self.items(event.scenePos())
        # print(f'debug for via {items}')
        items = masking(items)

        # if not self.point_items_memory:
        #     print('No items in memory!')
        #     print(items)

        before_selected_item = None
        if self.point_items_memory:
            # print(f'1)There is items in memory: {[item._id for item in self.point_items_memory]}')
            if set(items) == set(self.point_items_memory):
                if self.selectedItems():
                    if len(self.selectedItems()) > 1:
                        super(_CustomScene, self).mousePressEvent(event)
                        return
                    # print(f'2)before_selected_item :{self.selectedItems()[0]._id}')
                    before_selected_item = self.selectedItems()[0]
                    if before_selected_item in self.point_items_memory:
                        idx = self.point_items_memory.index(before_selected_item)
                    else:
                        idx = -1
                else:
                    idx = -1
                if idx+1 == len(self.point_items_memory):
                    # print(f'3)idx_overflow :{idx}')
                    self.point_items_memory[idx].restore_zvalue()
                    self.point_items_memory[0].save_zvalue_in_memory()
                    self.point_items_memory[0].setZValue(1000)
                else:
                    if before_selected_item and before_selected_item not in self.point_items_memory:
                        '''
                        어떤 이유인지 모르겠지만, 특정 sref의 경우 bounding box와 실제 클릭이 되는 부분이 다름.
                        masking을 했을 때 items에 해당 visualitem이 선택이 안되지만, 실제로 scene에서는 선택이 되어서
                        문제가 생김.
                        '''
                        # print(f'3) maybe something is wrong!')
                        # print(f'3-info) reset selected item')
                        before_selected_item.restore_zvalue()
                        self.point_items_memory[0].setZValue(1000)
                    else:
                        # print(f'3)idx_not_overflow :{idx}')
                        # print(f'3-info) b_z_values : {[item.zValue() for item in self.point_items_memory]}')
                        self.point_items_memory[idx].restore_zvalue()
                        self.point_items_memory[idx+1].save_zvalue_in_memory()
                        self.point_items_memory[idx+1].setZValue(1000)
            else:
                # if items:
                #     print(f'4)new point : {items[0]._id}')
                # else:
                #     print(f'4)clear')
                map(lambda item: item.restore_zvalue(), self.point_items_memory)
                self.point_items_memory = items
        else:
            self.point_items_memory = items
        super().mousePressEvent(event)

    def addItem(self, QGraphicsItem):
        super(_CustomScene, self).addItem(QGraphicsItem)

        for key in QGraphicsItem.bounding_rect_dict:
            self.fit_in_view_dict[key].append(QGraphicsItem.bounding_rect_dict[key])
        # for key in QGraphicsItem.bounding_rect_dict:
        #     if key == 'left' or key == 'bottom':
        #        if QGraphicsItem.bounding_rect_dict[key] < self.fit_in_view_dict[key]:
        #            self.fit_in_view_dict[key] = QGraphicsItem.bounding_rect_dict[key]
        #     elif key == 'right' or key == 'top':
        #         if QGraphicsItem.bounding_rect_dict[key] > self.fit_in_view_dict[key]:
        #             self.fit_in_view_dict[key] = QGraphicsItem.bounding_rect_dict[key]

    def removeItem(self, QGraphicsItem):
        super(_CustomScene, self).removeItem(QGraphicsItem)

        for key in QGraphicsItem.bounding_rect_dict:
            if QGraphicsItem.bounding_rect_dict[key] in self.fit_in_view_dict[key]:
                self.fit_in_view_dict[key].remove(QGraphicsItem.bounding_rect_dict[key])

    def send_item_list(self):
        # itemList = self.selectedItems()
        # print(itemList)
        # self.send_itemList_signal.emit(itemList)
        print(self.point_items_memory)
        self.send_itemList_signal.emit(self.point_items_memory)
        selected_items = self.selectedItems()
        # selected_items = list(filter(lambda item: type(item) == VisualizationItem._VisualizationItem and not item.parentItem(), self.selectedItems()))
        # if selected_items:
        #     self.send_selected_list_signal.emit(selected_items)
        if self.selectedItems():
            selected_items = list(
                filter(lambda item: type(item) == VisualizationItem._VisualizationItem and not item.parentItem(),
                       self.selectedItems()))
            selected_items = list(filter(lambda item: item._ItemTraits['_ElementName'], selected_items)) # for blocking tmp block
            if selected_items:
                self.send_selected_list_signal.emit(selected_items)

    def dragEnterEvent(self, event: 'QGraphicsSceneDragDropEvent') -> None:
        event.accept()
        print(event.pos())

    def dropEvent(self, event: 'QGraphicsSceneDragDropEvent') -> None:
        event.accept()
        print(event.pos())

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Delete:
            deletionItems = self.selectedItems()
            for deleteItem in deletionItems:
                _ID = deleteItem._ItemTraits['_id']
                self.send_deleteItem_signal.emit(_ID)
        elif QKeyEvent.key() == Qt.Key_M:
            move_items = self.selectedItems()
            bounding_rect_dict = dict(top=float('-inf'),bottom=float('inf'),left=float('inf'),right=float('-inf'))
            for item in move_items:
                if type(item) == VisualizationItem._VisualizationItem:
                    for key in item.bounding_rect_dict:
                        if key == 'left' or key == 'bottom':
                           if item.bounding_rect_dict[key] < bounding_rect_dict[key]:
                               bounding_rect_dict[key] = item.bounding_rect_dict[key]
                        elif key == 'right' or key == 'top':
                            if item.bounding_rect_dict[key] > bounding_rect_dict[key]:
                                bounding_rect_dict[key] = item.bounding_rect_dict[key]

            center_point = [(bounding_rect_dict['left']+bounding_rect_dict['right'])/2, (bounding_rect_dict['top']+bounding_rect_dict['bottom'])/2]
            self.send_move_item_signal.emit(move_items, center_point, 'move')
            # self.moveFlag = True
            # pass
        elif QKeyEvent.key() == Qt.Key_C: #variable Call with XYCoordinates DesignParameter
            copy_items = self.selectedItems()
            bounding_rect_dict = dict(top=float('-inf'),bottom=float('inf'),left=float('inf'),right=float('-inf'))
            for item in copy_items:
                if type(item) == VisualizationItem._VisualizationItem:
                    for key in item.bounding_rect_dict:
                        if key == 'left' or key == 'bottom':
                           if item.bounding_rect_dict[key] < bounding_rect_dict[key]:
                               bounding_rect_dict[key] = item.bounding_rect_dict[key]
                        elif key == 'right' or key == 'top':
                            if item.bounding_rect_dict[key] > bounding_rect_dict[key]:
                                bounding_rect_dict[key] = item.bounding_rect_dict[key]

            center_point = [(bounding_rect_dict['left']+bounding_rect_dict['right'])/2, (bounding_rect_dict['top']+bounding_rect_dict['bottom'])/2]
            self.send_move_item_signal.emit(copy_items, center_point, 'copy')
        elif QKeyEvent.key() == Qt.Key_D: #variableDefine With DesignParameter
            itemList = self.selectedItems()
            parameterIDList = list()
            for item in itemList:
                if type(item) == VisualizationItem._RectBlock:
                    continue
                parameterIDList.append(item._ItemTraits['_id'])
            self.send_parameterIDList_signal.emit(parameterIDList,0)
        elif QKeyEvent.key() == Qt.Key_V: # variable Call With DesignParameter
            itemList = self.selectedItems()
            parameterIDList = list()
            for item in itemList:
                if type(item) == VisualizationItem._RectBlock:
                    continue
                parameterIDList.append(item._ItemTraits['_id'])
            self.send_parameterIDList_signal.emit(parameterIDList,1)
        elif QKeyEvent.key() == Qt.Key_X: #variable Call with XWidth DesignParameter
            itemList = self.selectedItems()
            parameterIDList = list()
            for item in itemList:
                if type(item) == VisualizationItem._RectBlock:
                    continue
                parameterIDList.append(item._ItemTraits['_id'])
            self.send_parameterIDList_signal.emit(parameterIDList,2)
        elif QKeyEvent.key() == Qt.Key_Y: #variable Call with YWidth DesignParameter
            itemList = self.selectedItems()
            parameterIDList = list()
            for item in itemList:
                if type(item) == VisualizationItem._RectBlock:
                    continue
                parameterIDList.append(item._ItemTraits['_id'])
            self.send_parameterIDList_signal.emit(parameterIDList,3)
        # elif QKeyEvent.key() == Qt.Key_C: #variable Call with XYCoordinates DesignParameter
        #     itemList = self.selectedItems()
        #     parameterIDList = list()
        #     for item in itemList:
        #         if type(item) == VisualizationItem._RectBlock:
        #             continue
        #         parameterIDList.append(item._ItemTraits['_id'])
        #     self.send_parameterIDList_signal.emit(parameterIDList,4)
        elif QKeyEvent.key() == Qt.Key_H: #variable Call with XYCoordinates DesignParameter
            itemList = self.selectedItems()
            parameterIDList = list()
            for item in itemList:
                if type(item) == VisualizationItem._RectBlock:
                    continue
                parameterIDList.append(item._ItemTraits['_id'])
            self.send_parameterIDList_signal.emit(parameterIDList,5)
        elif QKeyEvent.key() == Qt.Key_Q: #variable Call with XYCoordinates DesignParameter
            itemList = self.selectedItems()
            for item in itemList:
                self.send_show_variable_signal.emit(item)
        elif QKeyEvent.key() == Qt.Key_Escape:
            print("selectionClear")
            self.clearSelection()
        elif QKeyEvent.key() == Qt.Key_P:
            itemList = self.selectedItems()
            for item in itemList:
                if item._ItemTraits['_DesignParametertype'] == 3:
                    structure_dict = self.copyItem(item)
                    self.newWindow(structure_dict, item)
        elif QKeyEvent.key() == Qt.Key_I:
            itemList = self.selectedItems()
            for item in itemList:
                if item._ItemTraits['_DesignParametertype'] == 1:
                    self.tmp_item_dict = self.ungroup_indexed_item()
                elif item._ItemTraits['_DesignParametertype'] == 2:
                    print('not yet')
                    print(item)
                    self.tmp_item_dict = self.ungroup_indexed_item()
                elif item._ItemTraits['_DesignParametertype'] == 3:
                    print('not yet')
        elif QKeyEvent.key() == Qt.Key_O:
            itemList = self.selectedItems()
            for item in itemList:
                try:
                    if item._ItemTraits['_DesignParametertype'] == 1:
                        if item.block[0].index[0] == len(item._ItemTraits['_XYCoordinates']) - 1 and len(item._ItemTraits['_XYCoordinates']) != 1:
                            self.send_module_name_list_signal.emit([item._ItemTraits['_ElementName']],[-1])
                        else:
                            self.send_module_name_list_signal.emit([item._ItemTraits['_ElementName']], [item.block[0].index])
                    elif item._ItemTraits['_DesignParametertype'] == 2:
                        self.send_module_name_list_signal.emit([item._ItemTraits['_ElementName']], [f'{[item.block[0].index[0]]}'+f'{[item.block[0].index[1]]}'])
                    elif item._ItemTraits['_DesignParametertype'] == 3:
                        self.send_module_name_list_signal.emit([item._ItemTraits['_ElementName']], [item.index])
                except:
                    pass
        elif QKeyEvent.key() == Qt.Key_R:
            for item, children in self.tmp_item_dict.items():
                for child_item in children:
                    item.addToGroup(child_item)
                    self.removeItem(child_item)
                self.addItem(item)

        super().keyPressEvent(QKeyEvent)

            #signal Out!! with DesignaParameterItems

    def mouseMoveEvent(self, QGraphicsSceneMouseEvent):
        super(_CustomScene, self).mouseMoveEvent(QGraphicsSceneMouseEvent)
        # delta = QPointF(QGraphicsSceneMouseEvent.scenePos()-self.oldPos)
        # if self.moveFlag is True:
        #     self.send_move_signal.emit(delta)
        self.oldPos = QGraphicsSceneMouseEvent.scenePos()

        snap = user_setup.MIN_SNAP_SPACING
        xy = [int(int(QGraphicsSceneMouseEvent.scenePos().x()/snap) * snap), int(int(QGraphicsSceneMouseEvent.scenePos().y()/snap) * snap)]
        self.send_mouse_move_xy_signal.emit(xy)
        self.send_mouse_move_signal.emit(QGraphicsSceneMouseEvent)

        # self.cursor_item.setPos(QPoint(xy[0],xy[1]))

    def mouseDoubleClickEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        self.send_doubleclick_signal.emit(True)

    def itemListClickIgnore(self,flag):
        self.listIgnoreFlag = flag

    def newWindow(self, structure_dict, subItem):

        self.viewList.append(_CustomView())
        self.viewList[-1].setWindowTitle(subItem._ItemTraits['_ElementName'])
        self.viewList[-1].getModule = subItem
        self.viewList[-1].nameout_signal.connect(self.receive_module_name)
        self.viewList[-1].name_list_signal.connect(self.receive_module_name)

        self.viewList[-1].setDragMode(QGraphicsView.RubberBandDrag)
        self.viewList[-1].scale(1,-1)
        dummy = _CustomScene(axis=False)
        bg_color = Qt.black if user_setup._Night_mode else Qt.white
        dummy.setBackgroundBrush(QBrush(bg_color))
        self.send_change_background_siganl.connect(dummy.change_background)
        dummy.send_module_name_list_signal.connect(self.viewList[-1].name_out_fcn)

        tmp_group_item = QGraphicsItemGroup()
        for key, value in structure_dict.items():
            try:
                DP = VisualizationItem._VisualizationItem()
                DP._NoVariableFlag = True
                DP.updateDesignParameter(value)
                DP.setToolTip(key)
            except:
                DP = value
            # dummy.addItem(DP)

            if type(DP) == VisualizationItem._VisualizationItem:
                DP.setSelected(False)
                if DP._subCellFlag:
                    pass
                else:
                    tmp_group_item.addToGroup(DP)

        self.viewList[-1].setScene(dummy)
        self.viewList[-1].setGeometry(200,200,1200,800)

        dummy.addItem(tmp_group_item)
        self.viewList[-1].fitInView(tmp_group_item, Qt.KeepAspectRatio)
        dummy.destroyItemGroup(tmp_group_item)
        del tmp_group_item

        self.viewList[-1].show()

    def receive_module_name(self,name_list,index_list):
        if type(name_list) == str:
            name_list = [name_list]
        self.send_module_name_list_signal.emit(name_list,index_list)

    def copyItem(self, item):
        structure_dict = dict()
        for key, value in item._ItemTraits['_DesignParameterRef'].items():
            structure_dict[key] = value
        return structure_dict

    def splitItem(self, item):
        structure_dict = dict()
        for i in range(len(item._ItemTraits['_XYCoordinates'])):
            tmpTraits = copy.deepcopy(item._ItemTraits)
            tmpTraits['_ElementName'] = item._ItemTraits['_ElementName'] + f'[{i}]'
            tmpTraits['_XYCoordinates'] = [item._ItemTraits['_XYCoordinates'][i]]
            indexitem = VisualizationItem._VisualizationItem(tmpTraits)
            indexitem.setIndex(i)
            # indexitem.updateTraits(item)
            key = tmpTraits['_ElementName']
            structure_dict[key] = indexitem
            # for key, value in item._ItemTraits['_DesignParameterRef'].items():
            #     structure_dict[key] = value
        return structure_dict

    def ungroup_indexed_item(self):
        tmp_idx_item_dict = dict()
        for item in self.selectedItems():
            if type(item) == VisualizationItem._VisualizationItem:
                if item._PathUngroupedFlag or (len(item._ItemTraits['_XYCoordinates']) == 1 and item._ItemTraits['_DesignParametertype'] == 2):
                    if len(item.block) != 1:
                        tmp_idx_item_dict[item] = list()
                        for child in item.childItems():
                            if type(child) == VisualizationItem._RectBlock:
                                tmp_vs_item = child.independent_from_group()
                                self.addItem(tmp_vs_item)
                                tmp_vs_item._PathUngroupedFlag = True
                                tmp_idx_item_dict[item].append(child)

                            self.removeItem(item)
                elif len(item._ItemTraits['_XYCoordinates']) > 1:
                    if item._ItemTraits['_DesignParametertype'] == 1:
                        # map(lambda child: child.setFlag(QGraphicsItem.ItemIsSelectable, True), item.childItems())
                        tmp_idx_item_dict[item] = list()
                        for child in item.childItems():
                            if type(child) == VisualizationItem._RectBlock:
                                tmp_vs_item = child.independent_from_group()
                                self.addItem(tmp_vs_item)
                                tmp_idx_item_dict[item].append(child)
                        # map(lambda child: child.independent_from_group(self), item.childItems())
                    elif item._ItemTraits['_DesignParametertype'] == 2:
                        rect_counts_for_connected_path = [len(xy) - 1 for xy in item._ItemTraits['_XYCoordinates']]
                        for idx, rect_count in enumerate(rect_counts_for_connected_path):
                            print(rect_counts_for_connected_path)
                            tmp_vs_item = None
                            rect_count = rect_counts_for_connected_path.pop(0)
                            count = 0
                            print(item.childItems())
                            tmp_idx_item_dict[item] = list()
                            for child in item.childItems():
                                if type(child) == VisualizationItem._RectBlock:
                                    tmp_vs_item = child.independent_path_from_group(tmp_vs_item)
                                    count += 1
                                    if count == rect_count:
                                        self.addItem(tmp_vs_item)
                                        tmp_vs_item._PathUngroupedFlag = True
                                        count = 0
                                        tmp_vs_item = None
                                        tmp_idx_item_dict[item].append(child)
                                        if rect_counts_for_connected_path:
                                            rect_count = rect_counts_for_connected_path.pop(0)

                    self.removeItem(item)

                else:
                    print('Only one index exist.')
                    print(item._ItemTraits['_XYCoordinates'])
            return tmp_idx_item_dict


class _VersatileWindow(QWidget):
    send_Name_signal = pyqtSignal(str)

    def __init__(self,_type):
        super().__init__()
        if _type is None:
            print("SG maker ERROR1")

        self.type = _type

        self.initUI()

    def initUI(self):
        makeButton = QPushButton("MAKE",self)
        loadButton = QPushButton("LOAD",self)
        cancelButton = QPushButton("Cancel",self)

        makeButton.clicked.connect(self.on_makeBox_accepted)

        # self.traitsDict = dict()

        if self.type == "NewProject":
            name = QLabel("Project Name")
        elif self.type == "NewModule":
            name = QLabel("Module Name")
        self.name_input = QLineEdit()


        self.setupVboxColumn1 = QVBoxLayout()
        self.setupVboxColumn2 = QVBoxLayout()
        setupBox = QHBoxLayout()

        self.setupVboxColumn1.addWidget(name)


        self.setupVboxColumn2.addWidget(self.name_input)

        setupBox.addLayout(self.setupVboxColumn1)
        setupBox.addLayout(self.setupVboxColumn2)
        setupBox.addLayout(self.setupVboxColumn2)

        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(makeButton)
        hbox.addWidget(loadButton)
        hbox.addWidget(cancelButton)
        # hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(setupBox)
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        # vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Create Window')
        self.setGeometry(300,300,500,500)
        self.show()

    def on_makeBox_accepted(self):
        self.send_Name_signal.emit(self.name_input.text())
        self.destroy()


    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_makeBox_accepted()
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.destroy()


def custom_excepthook(exctype, value, traceback):
    print("@@@@@@@@@@@@@@@@@@@@@@@There is critical error@@@@@@@@@@@@@@@@@@@@@@@@")
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    print("@@@@@@@@@@@@@@@@@@@@@@@There is critical error@@@@@@@@@@@@@@@@@@@@@@@@")



if __name__ == '__main__':
    sys._excepthook = sys.excepthook
    sys.excepthook = custom_excepthook

    app = QApplication(sys.argv)
    ex = _MainWindow()
    # ex = Tab_widget()

    try:
        app.exec_()
    except:
        print("something wrong")
    # sys.exit(app.exec_())




