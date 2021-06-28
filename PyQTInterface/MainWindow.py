import ast
import sys
import os
dir_check=os.getcwd()
if 'PyQTInterface' in dir_check:
    os.chdir('..')

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


import threading
import re
from PyQTInterface import LayerInfo
from PyQTInterface import VisualizationItem
from PyQTInterface import VariableVisualItem
from PyQTInterface import variableWindow
from PyQTInterface import list_manager
from PyQTInterface import calculator

from generatorLib import generator_model_api

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



class _CustomSignals(QObject):
    itemSelection = pyqtSignal()
    itemSelectionDestroy = pyqtSignal()
    xycoordinateSignal = pyqtSignal()



class _MainWindow(QMainWindow):

    # def MACRO(self):


    # send_Boundary_signal = pyqtSignal()
    # send_ProjectName_signal = pyqtSignal(str)
    # send_ModuleName_signal = pyqtSignal(str)
    # send_createNewDesignParameter_signal = pyqtSignal(str,int,str)QApplication
    send_progressMaximum_signal = pyqtSignal(int)
    send_progressMinimum_signal = pyqtSignal(int)
    send_progressValue_signal = pyqtSignal(int)
    send_callThread_signal = pyqtSignal()
    send_visibleGenState_signal = pyqtSignal(int, list)
    send_visibleCanState_signal = pyqtSignal(int, list)

    def __init__(self):
        super(_MainWindow, self).__init__()
        self._QTObj = QTInterfaceWithAST.QtInterFace()
        self._ProjectName = None
        self._CurrentModuleName = None
        self.initUI()
        self.easyDebugMode()
        self.progrseeBar_unstable = True
        self.visualItemDict = dict()
        self.variableList = []
        self._ASTapi = ASTmodule._Custom_AST_API()
        self._layerItem = dict()
        self._id_layer_mapping = dict()
        self.dvstate = False
        self._ElementManager = element_manager.ElementManager()
        self.library_manager = generator_model_api
        self._VariableIDwithAST = variable_manager.Variable_IDwithAST()
        self._DummyConstraints = variable_manager.DummyConstraints()
        self.gloabal_clipboard = QGuiApplication.clipboard()
        self.variable_store_list = list()

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

        newAction.setShortcut('Ctrl+N')
        newAction.triggered.connect(self.newProject)

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



        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&Project')
        fileMenu.addAction(newAction)
        fileMenu.addAction(loadAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(DebugAction)
        fileMenu.addAction(EncodeAction)
        fileMenu.addAction(RunGDSAction)
        fileMenu.addAction(UpdateGDSAction)

        #Second Menu#
        self.statusBar().showMessage("No Module")

        newModuleAction         = QAction("New Module",self)
        moduleManagementAction  = QAction("Module List",self)
        loadGDSAction           = QAction("Load GDS File As a Module",self)
        loadPyCodeAction        = QAction("Load Python source code as Constraint",self)

        newModuleAction.setShortcut('Ctrl+M')
        newModuleAction.triggered.connect(self.newModule)

        moduleManagementAction.triggered.connect(self.moduleManage)
        self.moduleList = []

        loadGDSAction.triggered.connect(self.loadGDS)
        loadPyCodeAction.triggered.connect(self.loadPy)

        moduleMenu = menubar.addMenu("&Module")
        # self.moduleListSubMenu = moduleMenu.addMenu('&Module List')


        moduleMenu.addAction(newModuleAction)
        moduleMenu.addAction(moduleManagementAction)
        moduleMenu.addAction(loadGDSAction)
        moduleMenu.addAction(loadPyCodeAction)




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
        # self.scene.setMinimumRenderSize(5)
        self.setCentralWidget(graphicView)
        self.scene.setBackgroundBrush(QBrush(Qt.white))
        graphicView.scale(1,-1)
        graphicView.setInteractive(True)
        # graphicView.setScene(self.scene)

        graphicView.variable_signal.connect(self.createVariable)
        self.scene.setSceneRect(-1000000,-1000000,2000000,2000000)
        self.scene.send_parameterIDList_signal.connect(self.parameterToTemplateHandler)
        self.scene.send_deleteItem_signal.connect(self.deleteDesignParameter)
        self.scene.selectionChanged.connect(self.scene.send_item_list)
        self.scene.send_show_variable_signal.connect(self.variableVisual.toggleVariableVisualization)
        # self.scene.send_debug_signal.connect(self.sceneDebug)

        # if DEBUG:
        #     a,b,c= QPointF(0, 0) ,QPointF(100, 0) ,QPointF(100, 500)
        #     points = [a,b,c]
        #     aa,bb,cc= QPointF(0, 0) ,QPointF(0, 100) ,QPointF(500, 100)
        #     pointss = [aa,bb,cc]
        #     poly = QPolygonF(points)
        #     poly2 = QPolygonF(pointss)
        #     path = QPainterPath()
        #     path.moveTo(0,0)
        #     path.addPolygon(poly)
        #     path.closeSubpath()
        #     path.addPolygon(poly2)
        #     path.closeSubpath()
        #     painter = QPainter()
        #     brush = QBrush(QColor(50,50,50))
        #     painter.fillPath(path,brush)
        #     self.scene.addPath(path)


        ################# Right Dock Widget setting ####################
        dockWidget1 = QDockWidget("Element")
        dockWidget1.setMaximumHeight(400)
        dockWidget1_1 = QDockWidget("Layer")
        layoutWidget = QWidget()
        dockContentWidget1 = QWidget()
        self.dockContentWidget1_2 = list_manager._ManageList()

        boundaryButton = QPushButton("Boundary")
        boundaryButton.clicked.connect(self.makeBoundaryWindow)

        pathButton = QPushButton("Path",dockContentWidget1)
        pathButton.clicked.connect(self.makePathWindow)

        srefButtonL = QPushButton("SRefLoad",dockContentWidget1)
        srefButtonL.clicked.connect(self.loadSRefWindow)
        # srefButtonS = QPushButton("SRefSave",dockContentWidget1)
        # srefButtonS.clicked.connect(self.makeSRefWindow)

        TextButton = QPushButton("Text",dockContentWidget1)
        TextButton.clicked.connect(self.makeTextWindow)

        PinButton = QPushButton("Pin",dockContentWidget1)
        PinButton.clicked.connect(self.makePinWindow)

        # FilterButton = QPushButton("Filter",dockContentWidget1)
        # FilterButton.clicked.connect(self.makeFilterWindow)
        #
        # VariableButton = QPushButton("Variable",dockContentWidget1)
        # VariableButton.clicked.connect(self.makeVariableWindow)

        ElemntClickCheckBox = QCheckBox("Element",dockContentWidget1)
        SrefClickCheckBox = QCheckBox("Sref",dockContentWidget1)
        VariableClickCheckBox = QCheckBox("Variable",dockContentWidget1)

        GeneratorCheckBox = QCheckBox("Generator", dockContentWidget1)
        GeneratorCheckBox.setCheckState(2)
        self.send_visibleGenState_signal.connect(self.dockContentWidget1_2.visibleGenState)
        GeneratorCheckBox.stateChanged.connect(self.visibleGenerator)

        CandidateCheckBox = QCheckBox("Candidate", dockContentWidget1)
        CandidateCheckBox.setCheckState(2)
        self.send_visibleCanState_signal.connect(self.dockContentWidget1_2.visibleCanState)
        CandidateCheckBox.stateChanged.connect(self.visibleCandidate)


        ########## Second tab ############
        self.dv = variableWindow._DesignVariableManagerWindow(dict())
        self.dvstate = True
        self.dv.send_variable_siganl.connect(self.createNewConstraintAST)
        self.dv.send_changedData_signal.connect(self.updateVariableConstraint)
        self.dv.selected_variable_item_id_signal.connect(self.highlightVI)

        vboxOnDock1 = QVBoxLayout()             # Layout For Button Widget

        vboxOnDock1.addStretch(10)
        vboxOnDock1.addWidget(boundaryButton)
        vboxOnDock1.addWidget(pathButton)
        vboxOnDock1.addWidget(srefButtonL)
        # vboxOnDock1.addWidget(srefButtonS)
        vboxOnDock1.addWidget(TextButton)
        vboxOnDock1.addWidget(PinButton)
        # vboxOnDock1.addWidget(FilterButton)
        # vboxOnDock1.addWidget(VariableButton)
        vboxOnDock1.addStretch(2)
        hboxOnDock1 = QHBoxLayout()
        hboxOnDock2 = QHBoxLayout()
        hboxOnDock1.addWidget(ElemntClickCheckBox)
        hboxOnDock1.addWidget(SrefClickCheckBox)
        hboxOnDock1.addWidget(VariableClickCheckBox)
        hboxOnDock2.addWidget(GeneratorCheckBox)
        hboxOnDock2.addStretch(2)
        hboxOnDock2.addWidget(CandidateCheckBox)
        vboxOnDock1.addLayout(hboxOnDock1)
        vboxOnDock1.addLayout(hboxOnDock2)
        vboxOnDock1.addStretch(10)

        dockContentWidget1.setLayout(vboxOnDock1)

        gridOnDock1 = QHBoxLayout()
        # gridOnDock1.addWidget(self.dockContentWidget1_2)
        gridOnDock1.addWidget(dockContentWidget1)

        layoutWidget.setLayout(gridOnDock1)
        dockWidget1.setWidget(layoutWidget)

        # self.addDockWidget(Qt.RightDockWidgetArea,dockWidget1_1)
        # self.addDockWidget(Qt.RightDockWidgetArea,dockWidget1)
        dockWidget1_1.setWidget(self.dockContentWidget1_2)

        # self.doctWidget_tab1 = QDockWidget("Layers")
        # unified_widget = QWidget()
        # v_layout_widget = QVBoxLayout()
        # v_layout_widget.addWidget(dockWidget1_1)
        # v_layout_widget.addWidget(dockWidget1)
        # unified_widget.setLayout(v_layout_widget)
        # self.doctWidget_tab1.setWidget(unified_widget)
        # self.addDockWidget(Qt.RightDockWidgetArea,self.doctWidget_tab1)
        # # self.addDockWidget(Qt.RightDockWidgetArea,dockWidget1_1)
        #
        # dockWidget_tab2 = QDockWidget("Variable")
        # dockWidget_tab2.setWidget(self.dv)
        # self.addDockWidget(Qt.RightDockWidgetArea, dockWidget_tab2)

        dockWidget_tab3 = QDockWidget("Variable")
        dockWidget_tab3.setWidget(self.dv)

        self.addDockWidget(Qt.RightDockWidgetArea, dockWidget1)
        self.addDockWidget(Qt.RightDockWidgetArea, dockWidget1_1)
        self.addDockWidget(Qt.RightDockWidgetArea, dockWidget_tab3)

        self.tabifyDockWidget(dockWidget1, dockWidget1_1)
        self.tabifyDockWidget(dockWidget1_1, dockWidget_tab3)


        ################# Left Dock Widget setting ####################
        dockWidget2 = QDockWidget("Design List")
        self.dockContentWidget2 = SetupWindow._SelectedDesignListWidget()

        self.scene.send_itemList_signal.connect(self.dockContentWidget2.UpdateCustomItem)       # Show the clicked items list
        self.dockContentWidget2.send_UpdateDesignParameter_signal.connect(self.updateDesignParameter)
        self.dockContentWidget2.send_UpdateDesignAST_signal.connect(self.srefUpdate)
        self.dockContentWidget2.send_parameterIDList_signal.connect(self.parameterToTemplateHandler)
        self.dockContentWidget2.send_deleteItem_signal.connect(self.deleteDesignParameter)

        # self.dockContentWidget2.signa.connect(graphicView.keyPressEvent)

        dockWidget2.setWidget(self. dockContentWidget2)
        self.addDockWidget(Qt.LeftDockWidgetArea,dockWidget2)

        ################# Bottom Dock Widget setting ####################
        dockWidget3 = QDockWidget("Design Constraint")
        layoutWidget = QWidget()
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
        #self.dockContentWidget3_2.send_SendSTMT_signal.connect(self.dockContentWidget3.receiveConstraintSTMT)
        self.dockContentWidget3_2.send_SendID_signal.connect(self.dockContentWidget3.receiveConstraintID)
        self.dockContentWidget3_2.send_ReceiveDone_signal.connect(self.dockContentWidget3.removeCurrentIndexItem)
        self.dockContentWidget3_2.send_SendCopyConstraint_signal.connect(self.constraintToTemplateHandler)
        self.dockContentWidget3_2.send_UpdateDesignConstraintID_signal.connect(self.get_constraint_update_design)
        self.dockContentWidget3_2.send_UpdateDesignConstraint_signal.connect(self.constraintUpdate2)
        self.dockContentWidget3_2.send_RequestDesignConstraint_signal.connect(self.constraintConvey)
        self.dockContentWidget3_2.send_deleteConstraint_signal.connect(self.deleteDesignConstraint)
        self.dockContentWidget3_2.send_RequestElementManger_signal.connect(self.convey_element_manager)
        self.dockContentWidget3_2.send_DataChanged_signal.connect(self.constraint_data_changed)
        self.scene.send_parameterIDList_signal.connect(self.dockContentWidget3_2.get_dp_highlight_dc)




        self.sendRightButton.clicked.connect(self.dockContentWidget3.checkSend)
        #self.dockContentWidget3.send_SendSTMT_signal.connect(self.dockContentWidget3_2.receiveConstraintSTMT)
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
        self.scene.send_parameterIDList_signal.connect(self.dockContentWidget3.get_dp_highlight_dc)

        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(self.sendDownButton)
        vboxLayout.addStretch(3)
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
        self.saveConstraintAsJSONButton = QPushButton("SaveAs...(JSON)")
        self.saveConstraintAsPickleButton = QPushButton("SaveAs...(pickle)")
        self.loadConstraintFromPickleButton = QPushButton("Load...")
        self.ConstraintTemplateButton = QPushButton("Template")
        # self.parsetreeEasyRun = QPushButton("easyRun")
        self.variableCallButton = QPushButton("variableCall")
        self.sref_debug = QPushButton("XYCalculator")

        VBoxForPeriButton.addStretch(3)
        # VBoxForPeriButton.addWidget(self.createConstraintButton)
        VBoxForPeriButton.addWidget(self.createConstraintWithPyCodeButton)
        # VBoxForPeriButton.addWidget(self.createConstraintButtonASTLegacy)
        VBoxForPeriButton.addWidget(self.createConstraintButtonAST)
        VBoxForPeriButton.addWidget(self.createConstraintButtonCUSTOM)
        VBoxForPeriButton.addWidget(self.createVariableButtonCUSTOM)
        VBoxForPeriButton.addWidget(self.saveConstraintAsJSONButton)
        VBoxForPeriButton.addWidget(self.saveConstraintAsPickleButton)
        VBoxForPeriButton.addWidget(self.loadConstraintFromPickleButton)
        VBoxForPeriButton.addWidget(self.ConstraintTemplateButton)
        # VBoxForPeriButton.addWidget(self.parsetreeEasyRun)
        VBoxForPeriButton.addWidget(self.variableCallButton)
        VBoxForPeriButton.addWidget(self.sref_debug)
        VBoxForPeriButton.addStretch(3)

        # self.dockContentWidget3.setDragDropMode(self.dockContectWidget3.MyOwnDragDropMove)

        gridOnDock3 = QHBoxLayout()
        gridOnDock3.addWidget(self.dockContentWidget3)
        gridOnDock3.addLayout(vboxLayout)
        gridOnDock3.addWidget(self.dockContentWidget3_2)
        gridOnDock3.addLayout(VBoxForPeriButton)

        layoutWidget.setLayout(gridOnDock3)
        dockWidget3.setWidget(layoutWidget)

        self.addDockWidget(Qt.BottomDockWidgetArea,dockWidget3)
        # self.createConstraintButton.clicked.connect(self.makeConstraintWindow)
        self.createConstraintWithPyCodeButton.clicked.connect(self.makePyCodeWindow)
        self.createConstraintButtonAST.clicked.connect(self.makeConstraintWindowAST)
        self.createConstraintButtonCUSTOM.clicked.connect(self.makeConstraintWindowCUSTOM)
        self.createVariableButtonCUSTOM.clicked.connect(self.makeVariableWindowCUSTOM)
        self.saveConstraintAsJSONButton.clicked.connect(self.saveConstraint)
        self.saveConstraintAsPickleButton.clicked.connect(self.saveConstraintP)
        self.loadConstraintFromPickleButton.clicked.connect(self.loadConstraintP)
        self.ConstraintTemplateButton.clicked.connect(self.makeTemplateWindow)
        # self.parsetreeEasyRun.clicked.connect(self.easyRun)
        self.variableCallButton.clicked.connect(self.variableListUpdate)
        self.sref_debug.clicked.connect(self.clipboard_test)


        ################ Logging Message Dock Widget setting ####################
        dockWidget4ForLoggingMessage = QDockWidget("Logging Message")
        self.dockContentWidget4ForLoggingMessage = SetupWindow._LogMessageWindow()
        self.dockContentWidget4ForLoggingMessage._InfoMessage("MakeProject")
        #        self.
        #
        # self.scene.send_itemList_signal.connect(self.dockContentWidget3.UpdateCustomItem)
        #
        dockWidget4ForLoggingMessage.setWidget(self.dockContentWidget4ForLoggingMessage)
        self.addDockWidget(Qt.BottomDockWidgetArea, dockWidget4ForLoggingMessage)

    # def sceneDebug(self):
    #     for key in self.visualItemDict:
    #         tmp = self.visualItemDict[key]
    #         path = tmp.shape()
    #         brush = QBrush(QColor(50,50,50))
    #         painter = QPainter()
    #         painter.fillPath(path,brush)
    #         self.scene.addPath(path)
    #         # if DEBUG:
    #         #     a,b,c= QPointF(0, 0) ,QPointF(100, 0) ,QPointF(100, 500)
    #         #     points = [a,b,c]
    #         #     aa,bb,cc= QPointF(0, 0) ,QPointF(0, 100) ,QPointF(500, 100)
    #         #     pointss = [aa,bb,cc]
    #         #     poly = QPolygonF(points)
    #         #     poly2 = QPolygonF(pointss)
    #         #     path = QPainterPath()
    #         #     path.moveTo(0,0)
    #         #     path.addPolygon(poly)
    #         #     path.closeSubpath()
    #         #     path.addPolygon(poly2)
    #         #     path.closeSubpath()
    #         #     painter = QPainter()
    #         #     brush = QBrush(QColor(50,50,50))
    #         #     painter.fillPath(path,brush)
    #         #     self.scene.addPath(path)
        print("******************************Initializing Graphic Interface Complete")

    # def threading_test(self,count):

    def debug(self,name_list):
        print(name_list)

    def clipboard_test(self):
        self.calculator_window = calculator.ExpressionCalculator(clipboard=self.gloabal_clipboard)
        self.scene.send_xyCoordinate_signal.connect(self.calculator_window.waitForClick)
        self.calculator_window.send_XYCreated_signal.connect(self.createDummyConstraint)
        self.calculator_window.show()

    def save_clipboard(self,save_target):
        if type(save_target) == list:
            print(save_target)
            self.gloabal_clipboard.setText(str(save_target[1:]))

    def sref_debug_module(self):
        # tmpcell = {'INV': {'Sub1': {'Sub2': {'PMOS': None}, 'NMOS': None,}, 'NMOS': None, 'PMOS': None}}
        # # tmpcell = {'Gen1': {'Gen2-1': {'Gen3': None}, 'Gen2-2': None}}
        #
        # self.fc = SetupWindow._FlatteningCell(tmpcell)
        # self.fc.show()

        tmp_generator = generator_model_api.class_dict['NMOSWithDummy']()
        name = 'sref_name'
        library = 'NMOSWithDummy'
        className = 'Is_it_necessary?'
        XY = [[0,0]]
        import ast
        # parameters = ast.parse(str(tmp_generator._ParametersForDesignCalculation))
        sref_ast = element_ast.Sref()
        sref_ast.name = name
        sref_ast.library = library
        sref_ast.className = className
        sref_ast.XY = XY
        sref_ast.parameters = tmp_generator._ParametersForDesignCalculation
        # a , id = self._QTObj._qtProject._createNewDesignConstraintAST( _ASTDtype = "pyCode",_ParentName=self._CurrentModuleName, _pyCode=str(tmp_generator._ParametersForDesignCalculation))
        # sref_ast.parameters = self._QTObj._qtProject._DesignConstraint[self._CurrentModuleName][id]
        # sref_ast.parameters = " "
        design_dict = self._QTObj._qtProject._feed_design(design_type='constraint', module_name=self._CurrentModuleName, _ast= sref_ast)
        self.dockContentWidget3_2.createNewConstraintAST(_id=design_dict['constraint_id'], _parentName=self._CurrentModuleName,
                                                         _DesignConstraint=self._QTObj._qtProject._DesignConstraint)


        # tmp_generator._ParametersForDesignCalculation

    def sref_visual_debug(self):
        DesignParameter = QTInterfaceWithAST.QtDesignParameter(_id='test1',_type=1, _ParentName='INV', _ElementName='name')
        DesignParameter._createDesignParameter()
        DesignParameter._setDesignParameterValue(_index='_Layer', _value='METAL1')
        DesignParameter._setDesignParameterValue(_index='_Datatype', _value='PIMP')
        DesignParameter._setDesignParameterValue(_index='_XYCoordinatesForDisplay', _value=[[0,0]])
        DesignParameter._setDesignParameterValue(_index='_XWidth', _value=100)
        DesignParameter._setDesignParameterValue(_index='_YWidth', _value=100)
        DesignParameter._setDesignParameterValue(_index='_Ignore', _value=False)
        DesignParameter._setDesignParameterValue(_index='_ElementName', _value='name')
        visualItem = VisualizationItem._VisualizationItem()
        visualItem.updateDesignParameter(DesignParameter)
        visualItem.setBoundingRegionGranularity(1)
        self.visualItemDict[DesignParameter._id] = visualItem

        visualItem.setToolTip(DesignParameter._id + '\n' + str(DesignParameter._type))
        # self.scene.addItem(visualItem)

        visualItem2 = VisualizationItem._VisualizationItem()

        visualItem2.setPos(-200,0)
        visualItem2._subSrefVisualItem = visualItem
        self.scene.addItem(visualItem2)
        # visualItem3 = VisualizationItem._VisualizationItem()
        # visualItem3.addToGroup(visualItem)
        # self.scene.addItem(visualItem3)
        # return visualItem

        pass
    # def hierarchyCalculator(self, _targetDict, _level = None):
    #     if _level == None:
    #         _level = 1
    #     else:
    #         _level = _level
    #     for key, value in _targetDict.items():
    #         if key == 'flattenFlag' :
    #             continue
    #         elif value['subcell'] == None:
    #             break
    #         else:
    #             _level = _level + 1
    #             subLevel = self.hierarchyCalculator(value['subcell'], _level)
    #             _level = max(subLevel, _level)
    #     return _level




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
            lastSrefName = list(self._QTObj._qtProject._DesignParameter[topCellName].keys())[-1]
            numberOfCells = int(re.findall('\d+', lastSrefName)[0])
            tmpDict = dict()
            print("             #######################################################################               ")
            print(f"               There are '{numberOfCells + 1}' cells inside '{topCellName}' cell                  ")
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
            _newChildName = _childName + '/' + _sref._DesignParameter['_ElementName']
            _parentName = _sref._id
            _parentXY = _sref._DesignParameter['_XYCoordinates']
            tmpDict = dict()
            for _id1, _modules1 in self._QTObj._qtProject._DesignParameter[_childName].items():
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

    def debugConstraint(self):
        try:
            print("test")
            look = self._QTObj._qtProject._ParseTreeForDesignConstrain[self._CurrentModuleName]._ast
            print(astunparse.dump(look))
        except:
            print('fail')
            pass

    def encodeConstraint(self):
        try:
            module = self._CurrentModuleName
            # topAST = self._QTObj._qtProject._ParseTreeForDesignConstrain[module]._ast
            constraint_names = self.dockContentWidget3.model.findItems('',Qt.MatchContains,1)
            constraint_ids = [item.text() for item in constraint_names]
            topAST = ast.Module()
            topAST.body = [self._QTObj._qtProject._DesignConstraint[module][id]._ast for id in constraint_ids]

            # # TODO: XYCoordinate AST 한번에 처리하는 것이 더 좋은가
            # for i in range(len(constraint_ids)):
            #     if constraint_ids[i] in list(self._DummyConstraints.XYDict.keys()):
            #         topAST = variable_ast.IrregularTransformer(self._DummyConstraints.XYDict[constraint_ids[i]]).visit(topAST)
            topAST = variable_ast.IrregularTransformer(self._DummyConstraints).visit(topAST)


            topAST = element_ast.ElementTransformer().visit(topAST)
            # variable_ast.VariableTransformer.infoDict = self._DummyConstraints.XYDict
            topAST = variable_ast.VariableTransformer().visit(topAST)
            code = astunparse.unparse(topAST)
            print(code)

            return code
        except:
            traceback.print_exc()
            print("encoding fail")

    # def createAdditionalCode(self):
    #     modules = self._QTObj._qtProject._DesignConstraint[self._CurrentModuleName]
    #     for _, module in modules.items():
    #         if module._type == 'XYCoordinate':
    #             coordinateInfo = self._DummyConstraints.XYDict[module._id]
    #             for key, value in coordinateInfo.items():
    #                 if key == 'X':
    #                     Xelements = re.split('',value)
    #                     print("Debug")
    #
    #                 elif key == 'Y':
    #                     Yelements = re.split(value)
    #                     print("Debug")
    #
    #                 elif key == 'XY':
    #                     XYelements = re.split(value)
    #                     print("Debug")

    def visibleCandidate(self, state):
        constraint_names_can = self.dockContentWidget3_2.model.findItems('', Qt.MatchContains, 1)
        constraint_ids_can = [item.text() for item in constraint_names_can]
        vi_can = []
        viList = []

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
            # self.gds2gen.load_qt_design_constraints(self._QTObj._qtProject._DesignConstraint)
            self.gds2gen.set_root_cell(self._CurrentModuleName)
            # self.gds2gen.update_designparameter_by_user_variable()
            self.gds2gen.run_qt_constraint_ast()

            stream_data = self.gds2gen.ready_for_top_cell()
            self.gds2gen.set_topcell_name('test')
            file = open('./tmp.gds','wb')
            stream_data.write_binary_gds_stream(file)
            file.close()
            #
            # module = self._CurrentModuleName
            # topAST = self._QTObj._qtProject._ParseTreeForDesignConstrain[module]._ast
            # topAST = element_ast.ElementTransformer().visit(topAST)
            # topAST = variable_ast.VariableTransformer().visit(topAST)
            # code = astunparse.unparse(topAST)
            # print(code)
        except:
            traceback.print_exc()
            print("Run fail")


    def runConstraint_for_update(self):
        try:
            gds2gen = topAPI.gds2generator.GDS2Generator(False)
            gds2gen.load_qt_project(self)
            gds2gen.load_qt_design_parameters(self._QTObj._qtProject._DesignParameter, self._CurrentModuleName)
            gds2gen.load_qt_design_constraints_code(self.encodeConstraint())
            constraint_ids = [item.text() for item in self.dockContentWidget3.model.findItems('', Qt.MatchContains, 1)]
            gds2gen.load_qt_id_info(self, constraint_ids)
            # gds2gen.set_root_cell(self._CurrentModuleName)
            # gds2gen.run_qt_constraint_ast()
            dp_dict = gds2gen.get_updated_designParameters()                                    # New Info
            current_dpdict = self._QTObj._qtProject._DesignParameter[self._CurrentModuleName]   # Unchanged target Info

            for _dpName, _qtdp in current_dpdict.items():
                for _newdpName, _newqtdp in dp_dict.items():
                    if _dpName == _newqtdp['_id']:          # Match Whether Updated Item corresponds to existing qtDesignParameter
                        if _qtdp._DesignParameter['_DesignParametertype'] == 1:
                            _qtdp._DesignParameter['_XYCoordinates'] = _newqtdp['_XYCoordinates']
                            _qtdp._DesignParameter['_Layer'] = LayerReader._LayerName_unified[str(_newqtdp['_Layer'])]
                            _qtdp._DesignParameter['_XWidth'] = _newqtdp['_XWidth']
                            _qtdp._DesignParameter['_YWidth'] = _newqtdp['_YWidth']
                            _qtdp._DesignParameter['_Datatype'] = _newqtdp['_Datatype']
                            # _qtdp._DesignParameter['_Reflect'] = _newqtdp['_Reflect']
                            # _qtdp._DesignParameter['_Angle'] = _newqtdp['_Angle']
                            _qtdp._DesignParameter['_Ignore'] = _newqtdp['_Ignore']
                            self.updateDesignParameter(_qtdp._DesignParameter, False)

                        elif _qtdp._DesignParameter['_DesignParametertype'] == 2:
                            _qtdp._DesignParameter['_XYCoordinates'] = _newqtdp['_XYCoordinates']
                            _qtdp._DesignParameter['_Layer'] = LayerReader._LayerName_unified[str(_newqtdp['_Layer'])]
                            _qtdp._DesignParameter['_Width'] = _newqtdp['_Width']
                            _qtdp._DesignParameter['_Datatype'] = _newqtdp['_Datatype']
                            _qtdp._DesignParameter['_Ignore'] = _newqtdp['_Ignore']
                            self.updateDesignParameter(_qtdp._DesignParameter, False)

                        elif _qtdp._DesignParameter['_DesignParametertype'] == 3:
                            _qtdp._DesignParameter['_DesignObj'] = _newqtdp['_DesignObj']
                            _qtdp._DesignParameter['_XYCoordinates'] = _newqtdp['_XYCoordinates']
                            _qtdp._DesignParameter['_Reflect'] = _newqtdp['_Reflect']
                            _qtdp._DesignParameter['_Angle'] = _newqtdp['_Angle']
                            _qtdp._DesignParameter['_Ignore'] = _newqtdp['_Ignore']
                            _qtdp._DesignParameter['_ModelStructure'] = _newqtdp['_ModelStructure']
                            sref_vi = VisualizationItem._VisualizationItem()
                            sref_vi.updateDesignParameter(_qtdp)
                            self.scene.addItem(sref_vi)
                            self.scene.removeItem(self.visualItemDict[_qtdp._DesignParameter['_id']])
                            self.visualItemDict[_qtdp._DesignParameter['_id']] = sref_vi
                            self._layerItem = sref_vi.returnLayerDict()
                            self.dockContentWidget1_2.updateLayerList(self._layerItem)

                        break
                    else:
                        pass

            print(dp_dict)

        except :
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

    def makeBoundaryWindow(self):
        self.bw = SetupWindow._BoundarySetupWindow()
        self.bw.show()
        self.bw.send_BoundarySetup_signal.connect(self.updateGraphicItem)
        self.bw.send_DestroyTmpVisual_signal.connect(self.deleteGraphicItem)
        self.bw.send_BoundaryDesign_signal.connect(self.createNewDesignParameter)
        self.bw.send_Warning_signal.connect(self.dockContentWidget4ForLoggingMessage._WarningMessage)
        self.scene.send_xyCoordinate_signal.connect(self.bw.AddBoundaryPointWithMouse)
        self.scene.send_xyCoordinate_signal.connect(self.bw.clickCount)
        self.scene.send_mouse_move_signal.connect(self.bw.mouseTracking)
        self.bw.send_Destroy_signal.connect(self.delete_obj)


    def makePathWindow(self):
        self.scene.itemListClickIgnore(True)
        self.pw = SetupWindow._PathSetupWindow()
        self.pw.show()
        self.pw.send_PathSetup_signal.connect(self.updateGraphicItem)
        self.pw.send_PathDesign_signal.connect(self.createNewDesignParameter)
        self.pw.send_DestroyTmpVisual_signal.connect(self.deleteGraphicItem)
        self.pw.send_Destroy_signal.connect(self.delete_obj)
        self.scene.send_xyCoordinate_signal.connect(self.pw.AddPathPointWithMouse)
        self.scene.send_xyCoordinate_signal.connect(self.pw.clickCount)                          # Mouse Interaction connect
        self.scene.send_mouse_move_signal.connect(self.pw.mouseTracking)
        self.scene.send_doubleclick_signal.connect(self.pw.quitCreate)

    def makeSRefWindow(self):
        scf = QFileDialog.getSaveFileName(self,'Save Design Parameter','./PyQTInterface/modules')
        try:
            _fileName=scf[0]
            self._QTObj._qtProject._saveDesignParameterAsPickle(_file=_fileName)
        except:
            print("Save DesignParameter Failed")
            self.dockContentWidget4ForLoggingMessage._WarningMessage("Save DesignParameter Fail: Unknown")
            pass

    def loadSRefWindow(self):
        self.ls = SetupWindow._LoadSRefWindow()
        self.ls.show()
        self.ls.send_DesignConstraint_signal.connect(self.srefCreate)
        self.scene.send_xyCoordinate_signal.connect(self.ls.DetermineCoordinateWithMouse)
        self.ls.send_destroy_signal.connect(self.delete_obj)
        # self.ls.send_TextSetup_signal.connect(self.updateGraphicItem)
        # self.ls.send_DestroyTmpVisual_signal.connect(self.deleteGraphicItem)
        # self.ls.send_Warning_signal.connect(self.dockContentWidget4ForLoggingMessage._WarningMessage)
        # self.scene.send_xyCoordinate_signal.connect(self.ls.DetermineCoordinateWithMouse)

    # def loadSRefWindowlegacy(self):
    #     scf = QFileDialog.getOpenFileName(self,'Load Design Parameter','./PyQTInterface/modules')
    #     try:
    #         _fileName=scf[0]
    #         self._QTObj._qtProject._loadDesignParameterAsPickle(_file=_fileName)
    #     except:
    #         print("Save DesignParameter Failed")
    #         self.dockContentWidget4ForLoggingMessage._WarningMessage("Save DesignParameter Fail: Unknown")
    #
    #         #################DesignParameter Load ######################
    #     for module in self._QTObj._qtProject._DesignParameter:
    #         for id in self._QTObj._qtProject._DesignParameter[module]:
    #             visualItem = self.createVisualItemfromDesignParameter(self._QTObj._qtProject._DesignParameter[module][id])
    #             self.updateGraphicItem(visualItem)
    #
    #     self.dockContentWidget4ForLoggingMessage._InfoMessage("Project Load Done")

    def makeTextWindow(self):
        self.txtw = SetupWindow._TextSetupWindow()
        self.txtw.show()
        self.txtw.send_TextSetup_signal.connect(self.updateGraphicItem)
        self.txtw.send_DestroyTmpVisual_signal.connect(self.deleteGraphicItem)
        self.txtw.send_TextDesign_signal.connect(self.createNewDesignParameter)
        self.txtw.send_Warning_signal.connect(self.dockContentWidget4ForLoggingMessage._WarningMessage)
        self.scene.send_xyCoordinate_signal.connect(self.txtw.DetermineCoordinateWithMouse)
        self.txtw.send_Destroy_signal.connect(self.delete_obj)

    def makePinWindow(self):
        self.pinw = SetupWindow._PinSetupWindow()
        self.pinw.show()
        self.pinw.send_PinSetup_signal.connect(self.updateGraphicItem)
        self.pinw.send_DestroyTmpVisual_signal.connect(self.deleteGraphicItem)
        self.pinw.send_PinDesign_signal.connect(self.createNewDesignParameter)
        self.pinw.send_Warning_signal.connect(self.dockContentWidget4ForLoggingMessage._WarningMessage)
        self.scene.send_xyCoordinate_signal.connect(self.pinw.DetermineCoordinateWithMouse)
        self.pinw.send_Destroy_signal.connect(self.delete_obj)

    # def makeFilterWindow(self):
    #     # self.fw = FilterPractice._FilterWindow()
    #     self.fw = variableWindow._TmpClass(self.visualItemDict)
    #     self.fw.show()
    #
    # def makeVariableWindow(self):
    #     self.dv = variableWindow._DesignVariableManagerWindow(self.visualItemDict)
    #     self.dvstate = True
    #     self.dv.show()
    #     self.dv.send_variable_siganl.connect(self.createNewConstraintAST)
    #     self.dv.send_changedData_signal.connect(self.updateVariableConstraint)
    #     self.dv.send_destroy_signal.connect(self.delete_obj)

    def makeConstraintWindow(self):
        self.cw = SetupWindow._ConstraintSetupWindow()
        self.cw.show()
        self.cw.send_DesignConstraint_signal.connect(self.createNewConstraint)

    def makePyCodeWindow(self):
        self.cw = SetupWindow._ConstraintSetupWindowPyCode()
        self.cw.show()
        self.cw.send_PyCode_signal.connect(self.createNewConstraintPyCode)

    def makeConstraintWindowAST(self):
        self.cw = SetupWindow._ConstraintSetupWindowAST(_ASTapi = self._ASTapi)
        self.cw.show()
        self.cw.send_AST_signal.connect(self.createNewConstraintAST)
        self.cw.send_destroy_signal.connect(self.delete_obj)

    def makeConstraintWindowCUSTOM(self):
        self.cw = SetupWindow._ConstraintSetupWindowCUSTOM(_ASTapi = self._ASTapi)
        self.cw.show()
        self.cw.send_CUSTOM_signal.connect(self.createNewConstraintAST)

    def makeVariableWindowCUSTOM(self):
        self.cw = SetupWindow._VariableSetupWindowCUSTOM(_ASTapi=self._ASTapi)
        self.cw.show()
        self.cw.send_CUSTOM_signal.connect(self.createNewConstraintAST)

    def delete_obj(self, obj):
        if obj == 'cw':
            del self.cw
        if obj == 'bw':
            del self.bw
        if obj == 'pw':
            del self.pw
        if obj == 'dv':
            del self.dv
        if obj == 'txtw':
            del self.txtw
        if obj == 'pinw':
            del self.pinw
        if obj == 'ls':
            del self.ls
        self.scene.itemListClickIgnore(False)

    def updateGraphicItem(self,graphicItem):
        for items in self.scene.items():
            if items is graphicItem:
                self.scene.removeItem(items)
                self.scene.update()

        # if not self.checkNameDuplication(graphicItem):
        self.scene.addItem(graphicItem)
        self.scene.send_move_signal.connect(graphicItem.move)
        self.scene.send_moveDone_signal.connect(graphicItem.moveUpdate)
        # visual_item_list = self.scene.items()
        # _blockList = list()
        # _layerList = list()
        # layernum2name = LayerReader._LayerNumber2CommonLayerName(LayerReader._LayerMapping)
        #
        # for index in range(0,len(visual_item_list)):
        #     # print(visual_item_list[index].__class__.__name__)
        #     if visual_item_list[index].__class__.__name__ == "_RectBlock":
        #         _blockList.append(visual_item_list[index])
        #
        # for i in range(0,len(_blockList)):
        #     _newLayer = layernum2name[str(_blockList[i].__dict__['_BlockTraits']['_Layer'])]
        #     if _newLayer in _layerList:
        #         pass
        #     else:
        #         _layerList.append(_newLayer)

        # self.dockContentWidget1_2.updateLayerList(self._layerItem)

        # layer 정보 : _RectBlock
        # layer visual on/off -> _Rectblock on/off  <important>
        # layer click on/off  -> _VisualizationItem

    def deleteGraphicItem(self,graphicItem):
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
    def loadProject(self):
        scf = QFileDialog.getOpenFileName(self,'Load Project','./PyQTInterface/Project/')

        try:
            cm = self._CurrentModuleName
            _fileName=scf[0]
            self._QTObj._loadProject(_name=_fileName)
            self._QTObj._qtProject.tmp_save_file.load_qt_interface(self,self._QTObj._qtProject._DesignConstraint)
            # self._QTObj._qtProject.tmp_save_file.load_from_constraint_tree_info(self, self._QTObj._qtProject._DesignConstraint)
            top_module = self._QTObj._qtProject.tmp_save_file.top_module
            if top_module in self._QTObj._qtProject._DesignParameter:
                for id_name, qt_parameter in self._QTObj._qtProject._DesignParameter[top_module].items():
                    vs_item = self.createVisualItemfromDesignParameter(qt_parameter)
                    self.updateGraphicItem(vs_item)
            self.dockContentWidget4ForLoggingMessage._InfoMessage("Project Load Done")


        except:
            traceback.print_exc()
            print("Load Project Failed")
            self.dockContentWidget4ForLoggingMessage._WarningMessage("Load Project Fail: Unknown")
            pass


    def saveProject(self):
        # if _fileName == None:
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

    def newModule(self):
        if self._QTObj._qtProject == None:
            self.warning = QMessageBox()
            self.warning.setText("There is no Project")
            self.warning.show()
        else:
            self.nmw = _VersatileWindow("NewModule")
            self.nmw.show()
            self.nmw.send_Name_signal.connect(self.updateModule)


    def updateModule(self,ModuleName):
        if (ModuleName in self.moduleList) == False:
            self.moduleList.append(ModuleName)
            # self.moduleListManagement(option="add",ModuleName=ModuleName)
        self._CurrentModuleName = ModuleName
        self.statusBar().showMessage( ("Project: "+self._QTObj._qtProject._name+", Module: "+self._CurrentModuleName) , 0 )
        # self.statusBar().addPermanentWidget( QLabel(str("Project: "+self._QTObj._qtProject._name+", Module: "+self._CurrentModuleName)) )

    def moduleManage(self):
        self.mw = SetupWindow._ModuleManageWidget(self.moduleList)
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
            _newParameterID = self._CurrentModuleName + str(0)
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
            _newParameterID = (_moduleName + str(_designParameterID))
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
            self._QTObj._qtProject._DesignParameter[_moduleName][_newParameterID]._DesignParameter['_DesignParametertype'] = 3
            # self._QTObj._qtProject._DesignParameter[_moduleName][_newParameterID]._DesignParameter['_ElementName'] = _newParameterID
            self._QTObj._qtProject._DesignParameter[_moduleName][_newParameterID]._DesignParameter['_XYCoordinates'] = _dp['_XYCoordinates']
            self._QTObj._qtProject._DesignParameter[_moduleName][_newParameterID]._DesignParameter['_ModelStructure'] = _dp['_ModelStructure']
        except:
            self.dockContentWidget4ForLoggingMessage._InfoMessage(" Not enough Parameters Given!")
            print("########################################################################################")
            print(f"                CUSTOM SREF DP / DC / VisualItem Creation Fail!                        ")
            print("########################################################################################")
            return
        _module = self._QTObj._qtProject._DesignParameter[_moduleName]
        design_dict = self._QTObj._qtProject._feed_design(design_type='constraint',
                                                          module_name=_moduleName,
                                                          _ast=_AST, element_manager_update=False)
        self.dockContentWidget3_2.createNewConstraintAST(_id=design_dict['constraint_id'],
                                                         _parentName=_moduleName,
                                                         _DesignConstraint=self._QTObj._qtProject._DesignConstraint)
        self._QTObj._qtProject._ElementManager.load_dp_dc_id(dp_id=_newParameterID, dc_id=design_dict['constraint_id'])
        sref_vi = VisualizationItem._VisualizationItem()
        sref_vi.updateDesignParameter(_module[_newParameterID])
        self.scene.addItem(sref_vi)
        self.visualItemDict[_module[_newParameterID]._id] = sref_vi

        self._layerItem = sref_vi.returnLayerDict()

        self.dockContentWidget1_2.updateLayerList(self._layerItem)
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

        dc_id = ast_with_id._id
        module = self.get_id_return_module(dc_id, "_DesignConstraint")
        gds2gen = topAPI.gds2generator.GDS2Generator(False)
        _dp = gds2gen.code_generation_for_subcell(ast_with_id)
        tmp_dp_dict , _ = self._QTObj._qtProject._ElementManager.get_ast_return_dpdict(ast_with_id)
        dp_id = self._QTObj._qtProject._ElementManager.get_dp_id_by_dc_id(dc_id)

        self._QTObj._qtProject._DesignParameter[module][dp_id]._DesignParameter['_DesignObj'] = _dp['_DesignObj']
        self._QTObj._qtProject._DesignParameter[module][dp_id]._DesignParameter['_ElementName'] = tmp_dp_dict['_ElementName']
        self._QTObj._qtProject._DesignParameter[module][dp_id]._DesignParameter['_XYCoordinates'] = _dp['_XYCoordinates']
        self._QTObj._qtProject._DesignParameter[module][dp_id]._DesignParameter['_ModelStructure'] = _dp['_ModelStructure']
        self._QTObj._qtProject._DesignParameter[module][dp_id]._DesignParameter['library'] = tmp_dp_dict['library']
        self._QTObj._qtProject._DesignParameter[module][dp_id]._DesignParameter['className'] = tmp_dp_dict['className']
        self._QTObj._qtProject._DesignParameter[module][dp_id]._DesignParameter['XY'] = tmp_dp_dict['_XYCoordinates']
        self._QTObj._qtProject._DesignParameter[module][dp_id]._DesignParameter['calculate_fcn'] = tmp_dp_dict['calculate_fcn']
        self._QTObj._qtProject._DesignParameter[module][dp_id]._DesignParameter['parameters'] = tmp_dp_dict['parameters']

        print("****************************************************************************************")
        print(f" Update Existing DesignParameters: DesignParameter creation with Name: {dp_id}")
        print("****************************************************************************************")

        sref_vi = VisualizationItem._VisualizationItem()
        sref_vi.updateDesignParameter(self._QTObj._qtProject._DesignParameter[module][dp_id])
        self.scene.addItem(sref_vi)
        self.scene.removeItem(self.visualItemDict[dp_id])
        self.visualItemDict[dp_id] = sref_vi
        self._layerItem = sref_vi.returnLayerDict()

        self.dockContentWidget1_2.updateLayerList(self._layerItem)

    def loadGDS(self):
        scf = QFileDialog.getOpenFileName(self,'Load GDS','./PyQTInterface/GDSFile')
        _fileName=scf[0]
        if _fileName == '':
            print("No File Selected")
            return

        _moduleName = _fileName.replace(".gds","")
        _moduleName = _moduleName.split('/')[-1]
        originalModuleList = set(self._QTObj._qtProject._DesignParameter)
        # self.dockContentWidget4ForLoggingMessage._InfoMessage("Load GDS File Starts.")
        print("**************************File Load From Legacy Start")
        try:
            self._QTObj._qtProject._loadDesignsFromGDSlegacy(_file = _fileName, _topModuleName = _moduleName)
        except:
            import collections
            self._QTObj._qtProject._DesignParameter = collections.OrderedDict()
            self._QTObj._qtProject._loadDesignsFromGDSlegacy(_file = _fileName, _topModuleName = _moduleName, _reverse=True)
        print("****************************File Load From Legacy Complete")

        if self.progrseeBar_unstable == True:
            updateModuleList = set(self._QTObj._qtProject._DesignParameter)
            addedModuleList = list(updateModuleList-originalModuleList)
            idLength = 0
            # randModule = addedModuleList[0]
            # anyId = list(self._QTObj._qtProject._DesignParameter[randModule])[0]
            # hierarchyHint=self._QTObj._qtProject._HierarchyFromRootForDesignParameter(_id=anyId,_ParentName=randModule)
            # rootModule = list(hierarchyHint[0])[0]
            #
            # moduleLength = len(addedModuleList)
            # minimumModule = round(moduleLength/50)
            entireHierarchy = self._QTObj._qtProject._getEntireHierarchy()
            for modules in addedModuleList:
                idLength += len(self._QTObj._qtProject._DesignParameter[modules])

            if DEBUG:
                print(f'DEBUGGING MODE, idLength= {idLength}')

            self.fc = SetupWindow._FlatteningCell(entireHierarchy)
            self.fc.show()
            flattening_dict = self.fc.ok_button_accepted()
            self.fc.destroy()

            print("############################ Cell DP, DC, VISUALITEM CREATION START ###############################")
            visual_item_list = []
            addedModulelist = list(self._QTObj._qtProject._DesignParameter.keys())
            topCellName = addedModulelist[-1]
            self._CurrentModuleName = topCellName       # Necessary For adding elements inside the cell
            ProcessedModuleDict = self.srefModulization(flattening_dict)            # Reconstruct imported GDS
            self._QTObj._qtProject._DesignParameter[topCellName].clear()            # discard original top cell info
            topcell = self._QTObj._qtProject._DesignParameter[topCellName]
            for _id, _element in ProcessedModuleDict.items():
                _designConstraintID = self._QTObj._qtProject._getDesignConstraintId(topCellName)
                _newConstraintID = (topCellName + str(_designConstraintID))
                topcell[_newConstraintID] = _element
                topcell[_newConstraintID]._id = _newConstraintID
                ######################################### AST Creation ################################################
                if topcell[_newConstraintID]._DesignParameter['_DesignParametertype'] == 3:
                    _cellModel = _element._DesignParameter['_DesignObj_Name']
                    _cellName = _element._DesignParameter['_ElementName']
                    _newCellName = _cellModel + '/' + _cellName
                    for key, value in flattening_dict.items():
                        findHint = _newCellName.find(key)
                        if findHint != -1:
                            topcell[_newConstraintID]._DesignParameter['library'] = value
                            _className = generator_model_api.class_name_dict[_element._DesignParameter['library']]
                            topcell[_newConstraintID]._DesignParameter['className'] =_className
                            topcell[_newConstraintID]._DesignParameter['parameters'] = \
                                generator_model_api.class_dict[value]._ParametersForDesignCalculation


                            topcell[_newConstraintID]._ElementName = _newConstraintID
                            topcell[_newConstraintID]._DesignParameter['_id'] = _newConstraintID
                            topcell[_newConstraintID]._DesignParameter['_ElementName'] = _newConstraintID
                            tmpAST = self._QTObj._qtProject._ElementManager.get_dp_return_ast(topcell[_newConstraintID])
                            if tmpAST == None:
                                continue
                            design_dict = self._QTObj._qtProject._feed_design(design_type='constraint',
                                                                              module_name=topCellName,
                                                                              _ast=tmpAST, element_manager_update=False)
                            self.dockContentWidget3_2.createNewConstraintAST(_id=design_dict['constraint_id'],
                                                                             _parentName=topCellName,
                                                                             _DesignConstraint=self._QTObj._qtProject._DesignConstraint)
                            tmp_dp_dict, _ = self._QTObj._qtProject._ElementManager.get_ast_return_dpdict(tmpAST)
                            self._QTObj._qtProject._ElementManager.load_dp_dc_id(dp_id=_newConstraintID, dc_id=design_dict['constraint_id'])
                            break
                        else:
                            continue
                else:
                    tmpAST = self._QTObj._qtProject._ElementManager.get_dp_return_ast(topcell[_newConstraintID])
                    if tmpAST is None:
                        continue
                    design_dict = self._QTObj._qtProject._feed_design(design_type='constraint', module_name=topCellName,
                                                                      _ast=tmpAST, element_manager_update=False)
                    self.dockContentWidget3_2.createNewConstraintAST(_id=design_dict['constraint_id'],
                                                                     _parentName=topCellName,
                                                                     _DesignConstraint=self._QTObj._qtProject._DesignConstraint)
                    tmp_dp_dict, _ = self._QTObj._qtProject._ElementManager.get_ast_return_dpdict(tmpAST)
                    self._QTObj._qtProject._ElementManager.load_dp_dc_id(dp_id=_newConstraintID, dc_id=design_dict['constraint_id'])

                ####################################### Visual Item Creation ##########################################
                if topcell[_newConstraintID]._DesignParameter['_DesignParametertype'] != 3:
                    visualItem = self.createVisualItemfromDesignParameter(topcell[_newConstraintID])
                    visual_item_list.append(visualItem)
                    # layernum2name = LayerReader._LayerNumber2CommonLayerName(LayerReader._LayerMapping)
                    # layer = layernum2name[str(tmp_dp_dict['_Layer'])]
                    layer = tmp_dp_dict['_Layer']
                    if layer in self._layerItem:
                        self._layerItem[layer].append(visualItem)
                    else:
                        self._layerItem[layer] = [visualItem]

                    self._id_layer_mapping[topcell[_newConstraintID]._id] = layer
                    self.scene.addItem(visualItem)
                else:
                    sref_vi = VisualizationItem._VisualizationItem()
                    sref_vi.updateDesignParameter(topcell[_newConstraintID])
                    self.scene.addItem(sref_vi)
                    self.visualItemDict[topcell[_newConstraintID]._id] = sref_vi

                    self._layerItem = sref_vi.returnLayerDict()

                self.dockContentWidget1_2.updateLayerList(self._layerItem)

                    # for i in range(len(sref_vi.returnLayerDict()['PIMP'])):
                    #     print(sref_vi.returnLayerDict()['PIMP'][i]._ItemTraits)

            print("############################ Cell DP, DC, VISUALITEM CREATION DONE ################################")

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

    def createVariable(self,type):
        selected_vis_items = self.scene.selectedItems()
        self.vw = variableWindow.VariableSetupWindow(variable_type=type,vis_items=selected_vis_items)
        self.vw.send_variableVisual_signal.connect(self.createVariableVisual)

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
            visualItem = self.createVisualItemfromDesignParameter(
                self._QTObj._qtProject._DesignParameter[self._CurrentModuleName][design_dict['parameter_id']])
            self.updateGraphicItem(visualItem)
            self.dockContentWidget4ForLoggingMessage._InfoMessage("Design Parameter Created")

            vi = VisualizationItem._VisualizationItem()
            self._layerItem = vi.returnLayerDict()

            self.dockContentWidget1_2.send_listInLayer_signal.connect(self.scene.getNonselectableLayerList)
            self.dockContentWidget1_2.updateLayerList(self._layerItem)

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
        dp_module = dp_id[:-1]
        while not dp_module in self._QTObj._qtProject._DesignParameter:
            dp_module = dp_module[:-1]

        dc_id = self._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id(dp_id)

        deletionItems = self.scene.selectedItems()      # Delete Visual Item
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

        # _ID = _DesignParameter['_id']
        # _Module = _ID[:-1]
        # while (_Module in self._QTObj._qtProject._DesignParameter) == False:
        #     _Module = _Module[:-1]
        #
        for module in self._QTObj._qtProject._DesignParameter:
            for id in self._QTObj._qtProject._DesignParameter[module]:
                if id in self.visualItemDict:
                    self._QTObj._qtProject._DesignParameter[module][id]._XYCoordinatesForDisplay = self.visualItemDict[id]._XYCoordinatesForDisplay

        #
        #
        # for visualItemName in self.visualItemDict:
        #     print(self.visualItemDict[visualItemName]._XYCoordinatesForDisplay)
        #




    # def createVisualItemfromDesignParameter(self,DesignParameter): #Origin
    #     visualItem = VisualizationItem._VisualizationItem()
    #     visualItem.updateTraits(DesignParameter._DesignParameter)
    #     self.visualItemDict[DesignParameter._id] = visualItem
    #     return visualItem

    def createVisualItemfromDesignParameter(self,DesignParameter):
        visualItem = VisualizationItem._VisualizationItem()
        # if visualItem._XYCoordinatesForDisplay
        visualItem.updateDesignParameter(DesignParameter)
        visualItem.setBoundingRegionGranularity(1)
        self.visualItemDict[DesignParameter._id] = visualItem

        visualItem.setToolTip(DesignParameter._id + '\n' + str(DesignParameter._type))

        # layer = visualItem._ItemTraits['_Layer']
        # if layer in self._layerItem:
        #     self._layerItem[layer].append(visualItem)
        # else:
        #     self._layerItem[layer] = [visualItem]
        #
        # self._id_layer_mapping[DesignParameter._id] = layer

        return visualItem

    def updateVisualItemFromDesignParameter(self,DesignParameter):
        id = DesignParameter._id
        self.visualItemDict[id].updateTraits(DesignParameter._DesignParameter)

        if id in self.visualItemDict:
            self.visualItemDict[id].updateTraits(DesignParameter._DesignParameter)
            return self.visualItemDict[id]
        return None

    def updateDesignParameter(self,_DesignParameter, element_manager_update = True):
        _ID = _DesignParameter['_id']
        _Module = _ID[:-1]
        while (_Module in self._QTObj._qtProject._DesignParameter) == False:
            _Module = _Module[:-1]
        # _Module = re.sub('[0-9]+', '',_ID)
        print(_Module)

        for key in _DesignParameter:
            self._QTObj._qtProject._DesignParameter[_Module][_ID]._setDesignParameterValue(_index = key, _value= _DesignParameter[key])
        self._QTObj._qtProject._DesignParameter[_Module][_ID]._setDesignParameterName(_DesignParameter['_ElementName'])

        # self._QTObj._qtProject._DesignParameter[_Module][_ID]._updateVisualItem()
        # visualItem = self._QTObj._qtProject._DesignParameter[_Module][_ID]._VisualizationItemObj
        visualItem = self.updateVisualItemFromDesignParameter(self._QTObj._qtProject._DesignParameter[_Module][_ID])
        self.updateGraphicItem(visualItem)

        design_dict = self._QTObj._qtProject._update_design(design_type='parameter', module_name=self._CurrentModuleName,
                                                          dp_dict=_DesignParameter, id=_ID, element_manager_update =element_manager_update)

        if design_dict['constraint_id']:
            self.dockContentWidget3_2.update_constraint_by_id(design_dict['constraint_id'])
            self.dockContentWidget3.update_constraint_by_id(design_dict['constraint_id'])

    def get_constraint_update_design(self, id, mother_id):
        if id:
            module = self.get_id_return_module(id,'_DesignConstraint')
            design_dict = self._QTObj._qtProject._update_design(design_type='constraint', module_name=module,
                                                              _ast=self._QTObj._qtProject._DesignConstraint[module][id]._ast, id=id)
            try:
                visualItem = self.updateVisualItemFromDesignParameter(design_dict['parameter'])
                self.updateGraphicItem(visualItem)
            except:
                pass #exceptional case LATER ( not 1-to-1 matching constraint.... > cannot update visual item)
        if mother_id:
            module = self.get_id_return_module(mother_id, '_DesignConstraint')
            design_dict  = self._QTObj._qtProject._update_design(design_type='constraint', module_name=module,
                                                                _ast=self._QTObj._qtProject._DesignConstraint[module][
                                                                    mother_id]._ast, id=mother_id)
            if design_dict['parameter']:
                if design_dict['parameter']._DesignParameter['_DesignParametertype'] == 1:
                    if design_dict['parameter']._DesignParameter['_XWidth'] == None or design_dict['parameter']._DesignParameter['_YWidth'] == None or design_dict['parameter']._DesignParameter['_XYCoordinates'] == None :
                            pass
                elif design_dict['parameter']._DesignParameter['_DesignParametertype'] == 2:
                    if design_dict['parameter']._DesignParameter['_Width'] == None or design_dict['parameter']._DesignParameter['_XYCoordinates'] == None :
                        pass
                elif design_dict['parameter']._DesignParameter['_DesignParametertype'] == 3:
                    if design_dict['parameter']._DesignParameter['_XYCoordinates'] == None :
                        pass
                else:
                    visualItem = self.updateVisualItemFromDesignParameter(design_dict['parameter'])
                    self.updateGraphicItem(visualItem)

    def deliveryDesignParameter(self):
        deliveryParameter = self.dockContentWidget2.DeliveryItem()
        self.dockContentWidget3_2.receiveDesignParameter(deliveryParameter)

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

    def createDummyConstraint(self, type, info_dict):
        """
        For Constraints that do not contain any detailed info
        XY Coordinates, Loops, ... etc.
        :return:
        """
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
            if type == 'XYCoordinate':
                try:
                    print("###############################################################")
                    print("               XYCoordinate ast creation Start                 ")
                    print("###############################################################")
                    _ASTForVariable = ASTmodule._Custom_AST_API()
                    _ASTtype = type
                    _ASTobj = _ASTForVariable._create_variable_ast_with_name(_ASTtype)

                    _designConstraintID = self._QTObj._qtProject._getDesignConstraintId(self._CurrentModuleName)
                    _newConstraintID = (self._CurrentModuleName + str(_designConstraintID))

                    _ASTobj.__dict__['id'] = _newConstraintID
                    self._DummyConstraints.XYDict[_newConstraintID] = info_dict
                    design_dict = self._QTObj._qtProject._feed_design(design_type='constraint',
                                                                      module_name=self._CurrentModuleName, _ast=_ASTobj)
                    self.dockContentWidget3_2.createNewConstraintAST(_id=design_dict['constraint_id'],
                                                                     _parentName=self._CurrentModuleName,
                                                                     _DesignConstraint=self._QTObj._qtProject._DesignConstraint)

                    print("###############################################################")
                    print("                XYCoordinate ast creation Done                 ")
                    print("###############################################################")
                except:
                    print("###############################################################")
                    print("                XYCoordinate ast creation Failed               ")
                    print("###############################################################")
                else:
                    pass

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

                # self._VariableIDwithAST.variableIDwithASTDict[_vid] = _AST
                try:
                    if design_dict['parameter']:
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

        # _id = updateDict['_id']
        # _Module = re.sub('[0-9]+', '', _id)
        #
        # for key in updateDict:
        #     if key == "_id":
        #         continue
        #     else:
        #         self._QTObj._qtProject._DesignConstraint[_Module][_id]._setDesignConstraintValue(_index=key, _value=updateDict[key])
        # _STMT = self._QTObj._qtProject._DesignConstraint[_Module][_id]._readConstraintValueAsSTMT()
        #
        # self.dockContentWidget3_2.receiveConstraintSTMT(_STMT)


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
            self.visualItemDict[changed_dp_id].update_dc_variable_info(self._QTObj._qtProject._DesignConstraint[module_name][constraint_id]._ast)

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
            for var in tmpList:
                if var in self.dv.idDict:
                    if changed_dp_id in self.dv.idDict[var]['id']:
                        self.dv.idDict[var]['id'].remove(changed_dp_id)

    def highlightVI(self, _idlist):
        for item in self.visualItemDict:
            self.visualItemDict[item].setSelected(False)
        for _id in _idlist:
            self.visualItemDict[_id].setFlag(QGraphicsItemGroup.ItemIsSelectable, True)
            self.visualItemDict[_id].setSelected(True)

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
        self.updateModule("EasyDebugModule")


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

    # def easyRun(self):
    #     try:
    #         file = './PyQTInterface/json/' + EasyDebugFileName + '.json'
    #         #with open('./PyQTInterface/json/INV_IITP.json') as js:
    #         with open(file) as js:
    #             jsonData = json.load(js)
    #             constraint = jsonData
    #
    #             testObj0 = ParseTree.pyCodeParseTree()
    #             testObj0.BuildParseTree(_Constraints=constraint)
    #             testObj0.CompilepyCode()
    #             # testObj0.PyCodeScriptGeneration( fileName= 'default.py', mode = 'wt', text = None)
    #             testObj0.PyCodeScriptGeneration(fileName= 'INV1.py')
    #             print(testObj0._ParseTree._lineCodes)
    #     except:
    #         self.error = QMessageBox()
    #         self.error.setText("Easy Run Fail")
    #         self.error.show()


class _CustomView(QGraphicsView):
    variable_signal = pyqtSignal(str)
    nameout_signal = pyqtSignal(str)
    name_list_signal = pyqtSignal(list)

    def __init__(self):
        super(_CustomView, self).__init__()
        self.show()
        self.setMouseTracking(True)
        self.modulename=None

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

    def mousePressEvent(self, event) -> None:
        if event.button() == Qt.RightButton:
            # print('return')
            return
        # super(_CustomView, self).mousePressEvent(event)
        super().mousePressEvent(event)

    # def dropEvent(self, event) -> None:
    #     super
    def contextMenuEvent(self, event) -> None:
        constraint_create_array = QAction("create array", self)
        variable_create_array = QAction("create array variable", self)
        variable_create_distance = QAction("create distance variable", self)
        variable_create_enclosure = QAction("create enclousre variable", self)
        variable_create_connect = QAction("create connect variable", self)

        menu = QMenu(self)
        menu.addAction(constraint_create_array)
        menu.addAction(variable_create_array)
        menu.addAction(variable_create_distance)
        menu.addAction(variable_create_enclosure)
        menu.addAction(variable_create_connect)

        constraint_create_array.triggered.connect(lambda tmp: self.variable_emit('c_array'))
        variable_create_array.triggered.connect(lambda tmp: self.variable_emit('array'))
        variable_create_distance.triggered.connect(lambda tmp: self.variable_emit('distance'))
        variable_create_enclosure.triggered.connect(lambda tmp: self.variable_emit('enclosure'))
        variable_create_connect.triggered.connect(lambda tmp: self.variable_emit('connect'))


        menu.exec(event.globalPos())

    def variable_emit(self, type):
        if type == 'c_array':
            self.variable_signal.emit('c_array')
        elif type == 'array':
            self.variable_signal.emit('element array')
        elif type == 'distance':
            self.variable_signal.emit('distance')
        elif type == 'enclosure':
            self.variable_signal.emit('enclosure')
        elif type == 'connect':
            self.variable_signal.emit('connect')


    def dragEnterEvent(self, event) -> None:
        print('ed')
        event.accept()
        event.proposedAction()
        super(self).dragEnterEvent(event)
    def dropEvent(self, event) -> None:
        event.accept()
        event.proposedAction()
        super(self).dropEvent(event)

    def name_out_fcn(self,name_list):
        name_list.insert(0,self.modulename)
        self.name_list_signal.emit(name_list)

class _CustomScene(QGraphicsScene):
    send_debug_signal = pyqtSignal()
    send_xyCoordinate_signal = pyqtSignal(QGraphicsSceneMouseEvent)
    send_itemList_signal = pyqtSignal(list)
    send_parameterIDList_signal = pyqtSignal(list,int)
    send_move_signal = pyqtSignal(QPointF)
    send_moveDone_signal = pyqtSignal()
    send_deleteItem_signal = pyqtSignal(str)
    send_module_name_list_signal = pyqtSignal(list)
    send_mouse_move_signal = pyqtSignal(QGraphicsSceneMouseEvent)
    send_show_variable_signal = pyqtSignal(QGraphicsItem)
    send_doubleclick_signal = pyqtSignal(bool)

    viewList = []

    def __init__(self, axis=True):
        super().__init__()
        if axis:
            pen = QPen()
            pen.setStyle(Qt.SolidLine)
            pen.setColor(Qt.GlobalColor.red)
            pen.setCapStyle(Qt.RoundCap)
            pen.setWidth(3)

            self.addLine(QLineF(-1000000,0,1000000,0),pen)
            self.addLine(QLineF(0,-1000000,0,1000000),pen)

        self.moveFlag = False
        self.listIgnoreFlag = False
        self.oldPos = QPointF(0,0)
        self.itemList = list()
        self.nslist = list()

    def getNonselectableLayerList(self, _layerlist):
        self.nslist = _layerlist

    def mousePressEvent(self, event):
        _RectBlock_list = list()
        # for i in range(len(self.items(event.scenePos()))):
        #     if i%2 == 1:
        #         _RectBlock_list.append(self.items(event.scenePos())[i])
        #     else:
        #         pass
        for layer in self.nslist:
            if layer in self.itemList:
                self.itemList.remove(layer)

        if len(self.selectedItems()) != 0:
            selected = self.selectedItems()
            for i in range(len(selected)):
                self.itemList.append(selected[i])
                selected[i].setFlag(QGraphicsItemGroup.ItemIsSelectable, False)
        else:
            for i in range(len(self.itemList)):
                self.itemList[i].setFlag(QGraphicsItemGroup.ItemIsSelectable, True)
            self.itemList.clear()




        # if event.button() == Qt.LeftButton:
        #     for i in range(len(_RectBlock_list)):
        #         # _RectBlock_list[i].mousePressEvent(event)
        #         # _RectBlock_list[i].setSelected(True)
        #         if _RectBlock_list[i].isSelected():
        #             _RectBlock_list[i].setSelected(False)
        #             try:
        #                 _RectBlock_list[i+1].setSelected(True)
        #                 break
        #             except:
        #                 pass
                        # _RectBlock_list[0].setSelected(True)

        # self.selectionChanged.emit()

        # if event.button() == Qt.RightButton:
        #     print('return')
        #     return
        # super(self).mousePressEvent(event)
        # itemList = self.items(event.scenePos(),Qt.IntersectsItemShape)
        # for item in itemList:
        #     print(f'click{item}item')
        #     item.setSelected(True)
        # self.send_debug_signal.emit()
        # if self.listIgnoreFlag is True:
        #     pass
        # else:
        #     # itemList = self.items(event.scenePos())
        #     # itemList = self.items(event.scenePos(),Qt.IntersectsItemShape)
        #     # if DEBUG:
        #     #     print("MousePressDebug")
        #     #     print(itemList)
        #     # self.send_itemList_signal.emit(itemList)                  #Temporary stop, Unstable (I need to find DesignParameterWith Id, without Module Name
        self.send_xyCoordinate_signal.emit(event)
        if self.moveFlag is True:
            self.moveFlag = False
            self.send_moveDone_signal.emit()
            print("moveDone emmit")
        else:
            # self.oldPos = event.scenePos()
            pass
        super().mousePressEvent(event)

    def send_item_list(self):
        itemList = self.selectedItems()
        # print(itemList)
        self.send_itemList_signal.emit(itemList)
        pass


    def dragEnterEvent(self, event: 'QGraphicsSceneDragDropEvent') -> None:
        event.accept()
        print(event.pos())

    def dropEvent(self, event: 'QGraphicsSceneDragDropEvent') -> None:
        event.accept()
        print(event.pos())

    # def eventFilter(self, obj, event):
    #     if obj ==  and event.type() == QEvent.HoverEnter:
    #         self.onHovered()
    #     return super(_CustomScene, self).eventFilter(obj, event)
    #
    # def onHovered(self):
    #     print("hovered")

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Delete:
            deletionItems = self.selectedItems()
            for deleteItem in deletionItems:
                # self.removeItem(deleteItem)
                # if type(deleteItem) == VisualizationItem._RectBlock:
                #     continue
                _ID = deleteItem._ItemTraits['_id']
                self.send_deleteItem_signal.emit(_ID)
        elif QKeyEvent.key() == Qt.Key_M:
            self.moveFlag = True
            pass
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
        elif QKeyEvent.key() == Qt.Key_C: #variable Call with XYCoordinates DesignParameter
            itemList = self.selectedItems()
            parameterIDList = list()
            for item in itemList:
                if type(item) == VisualizationItem._RectBlock:
                    continue
                parameterIDList.append(item._ItemTraits['_id'])
            self.send_parameterIDList_signal.emit(parameterIDList,4)
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
                    subElement = item._ItemTraits['_ElementName']
                    structure_dict = self.copyItem(item)
                    self.newWindow(structure_dict, subElement)
        elif QKeyEvent.key() == Qt.Key_I:
            itemList = self.selectedItems()
            for item in itemList:
                index = len(item._ItemTraits['_XYCoordinates'])
                if item._ItemTraits['_DesignParametertype'] == 1:
                    if index is not 1:
                        subElement = item._ItemTraits['_ElementName']
                        structure_dict = self.splitItem(item, index)
                        self.newWindow(structure_dict, subElement)
                        print(structure_dict)
                elif item._ItemTraits['_DesignParametertype'] == 2:
                    print('not yet')
                    # if index is not 1:
                    #     subElement = item._ItemTraits['_ElementName']
                    #     structure_dict = self.splitItem(item, index)
                    #     self.newWindow(structure_dict, subElement)
                    #     print(structure_dict)
                elif item._ItemTraits['_DesignParametertype'] == 3:
                    print('not yet')
                    # if index is not 1:
                    #     subElement = item._ItemTraits['_ElementName']
                    #     structure_dict = self.splitItem(item, index)
                    #     self.newWindow(structure_dict, subElement)
                    #     print(structure_dict)
        elif QKeyEvent.key() == Qt.Key_O:
            itemList = self.selectedItems()
            for item in itemList:
                try:
                    self.send_module_name_list_signal.emit([item._ItemTraits['_ElementName']])
                except:
                    pass

        super().keyPressEvent(QKeyEvent)

            #signal Out!! with DesignaParameterItems

    def mouseMoveEvent(self, QGraphicsSceneMouseEvent):
        delta = QPointF(QGraphicsSceneMouseEvent.scenePos()-self.oldPos)
        if self.moveFlag is True:
            self.send_move_signal.emit(delta)
        self.oldPos = QGraphicsSceneMouseEvent.scenePos()
        self.send_mouse_move_signal.emit(QGraphicsSceneMouseEvent)

    def mouseDoubleClickEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        self.send_doubleclick_signal.emit(True)

    def itemListClickIgnore(self,flag):
        self.listIgnoreFlag = flag

    def newWindow(self, structure_dict, subElementName):

        self.viewList.append(_CustomView())
        self.viewList[-1].setWindowTitle(subElementName)
        self.viewList[-1].modulename = subElementName
        self.viewList[-1].nameout_signal.connect(self.receive_module_name)
        self.viewList[-1].name_list_signal.connect(self.receive_module_name)

        self.viewList[-1].setDragMode(QGraphicsView.RubberBandDrag)
        self.viewList[-1].scale(1,-1)
        dummy = _CustomScene(axis=False)
        dummy.send_module_name_list_signal.connect(self.viewList[-1].name_out_fcn)
        for key, value in structure_dict.items():
            try:
                DP = VisualizationItem._VisualizationItem()
                DP._NoVariableFlag = True
                DP.updateDesignParameter(value)
                DP.setToolTip(key)
            except:
                DP = value
            dummy.addItem(DP)

        self.viewList[-1].setScene(dummy)
        self.viewList[-1].setGeometry(200,200,1200,800)
        self.viewList[-1].show()

    def receive_module_name(self,name_list):
        if type(name_list) == str:
            name_list = [name_list]
        self.send_module_name_list_signal.emit(name_list)

    def copyItem(self, item):
        structure_dict = dict()
        for key, value in item._ItemTraits['_DesignParameterRef'].items():
            structure_dict[key] = value
        return structure_dict

    def splitItem(self, item, index):
        structure_dict = dict()
        for i in range(index):
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

#
# class _QActionCustom(QAction):
#     send_Text_signal = pyqtSignal(str)
#     def __init__(self):
#         super().__init__()
#
#     def triggered(self, checked=False):
#
#         self.send_Text_signal.emit(self.text())

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
    try:
        app.exec_()
    except:
        print("something wrong")
    # sys.exit(app.exec_())


