import sys
import os
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
from DesignManager.VariableManager import FilterPractice


import threading
import re
from PyQTInterface import LayerInfo
from PyQTInterface import VisualizationItem
from PyQTInterface import VariableVisualItem
from PyQTInterface import variableWindow
from PyQTInterface import list_manager

##for easy debug##
import json


import astunparse

##################
DEBUG = True
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

    def initUI(self):

        print("*********************Initalizing Graphic Interface Start")

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



        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&Project')
        fileMenu.addAction(newAction)
        fileMenu.addAction(loadAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(DebugAction)
        fileMenu.addAction(EncodeAction)

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
        graphicView.setScene(self.scene)
        graphicView.setRubberBandSelectionMode(Qt.ContainsItemShape)
        graphicView.setDragMode(QGraphicsView.RubberBandDrag)
        graphicView.setAcceptDrops(True)
        self.scene.setItemIndexMethod(QGraphicsScene.NoIndex)
        self.scene.setMinimumRenderSize(5)
        self.setCentralWidget(graphicView)
        self.scene.setBackgroundBrush(QBrush(Qt.white))
        graphicView.scale(1,-1)
        graphicView.setInteractive(True)
        # graphicView.setScene(self.scene)

        graphicView.variable_signal.connect(self.createVariable)
        self.scene.setSceneRect(-1000000000,-1000000000,2000000000,2000000000)
        self.scene.send_parameterIDList_signal.connect(self.parameterToTemplateHandler)
        self.scene.send_deleteItem_signal.connect(self.deleteDesignParameter)
        self.scene.selectionChanged.connect(self.scene.send_item_list)
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
        dockWidget1 = QDockWidget()
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
        srefButtonS = QPushButton("SRefSave",dockContentWidget1)
        srefButtonS.clicked.connect(self.makeSRefWindow)

        FilterButton = QPushButton("Filter",dockContentWidget1)
        FilterButton.clicked.connect(self.makeFilterWindow)

        ElemntClickCheckBox = QCheckBox("Element",dockContentWidget1)
        SrefClickCheckBox = QCheckBox("Sref",dockContentWidget1)
        VariableClickCheckBox = QCheckBox("Variable",dockContentWidget1)


        vboxOnDock1 = QVBoxLayout()             # Layout For Button Widget

        vboxOnDock1.addStretch(10)
        vboxOnDock1.addWidget(boundaryButton)
        vboxOnDock1.addWidget(pathButton)
        vboxOnDock1.addWidget(srefButtonL)
        vboxOnDock1.addWidget(srefButtonS)
        vboxOnDock1.addWidget(FilterButton)
        vboxOnDock1.addStretch(2)
        hboxOnDock1 = QHBoxLayout()
        hboxOnDock1.addWidget(ElemntClickCheckBox)
        hboxOnDock1.addWidget(SrefClickCheckBox)
        hboxOnDock1.addWidget(VariableClickCheckBox)
        vboxOnDock1.addLayout(hboxOnDock1)
        vboxOnDock1.addStretch(10)

        dockContentWidget1.setLayout(vboxOnDock1)

        gridOnDock1 = QHBoxLayout()
        # gridOnDock1.addWidget(self.dockContentWidget1_2)
        gridOnDock1.addWidget(dockContentWidget1)

        layoutWidget.setLayout(gridOnDock1)
        dockWidget1.setWidget(layoutWidget)

        self.addDockWidget(Qt.RightDockWidgetArea,dockWidget1)
        dockWidget1_1.setWidget(self.dockContentWidget1_2)
        self.addDockWidget(Qt.RightDockWidgetArea,dockWidget1_1)

        ################# Left Dock Widget setting ####################
        dockWidget2 = QDockWidget("Design List")
        self.dockContentWidget2 = SetupWindow._SelectedDesignListWidget()

        self.scene.send_itemList_signal.connect(self.dockContentWidget2.UpdateCustomItem)       # Show the clicked items list
        self.dockContentWidget2.send_UpdateDesignParameter_signal.connect(self.updateDesignParameter)
        self.dockContentWidget2.send_parameterIDList_signal.connect(self.parameterToTemplateHandler)
        self.dockContentWidget2.send_deleteItem_signal.connect(self.deleteDesignParameter)

        # self.dockContentWidget2.signa.connect(graphicView.keyPressEvent)

        dockWidget2.setWidget(self. dockContentWidget2)
        self.addDockWidget(Qt.LeftDockWidgetArea,dockWidget2)

        ################# Bottom Dock Widget setting ####################
        dockWidget3 = QDockWidget("Design Constraint")
        layoutWidget = QWidget()
        self.dockContentWidget3 = SetupWindow._ConstraintTreeViewWidgetAST("Hierarchy")
        self.dockContentWidget3_2 = SetupWindow._ConstraintTreeViewWidgetAST("Floating")

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
        self.dockContentWidget3_2.send_RecieveDone_signal.connect(self.dockContentWidget3.removeCurrentIndexItem)
        self.dockContentWidget3_2.send_SendCopyConstraint_signal.connect(self.constraintToTemplateHandler)
        self.dockContentWidget3_2.send_UpdateDesignConstraintID_signal.connect(self.get_constraint_update_design)
        self.dockContentWidget3_2.send_UpdateDesignConstraint_signal.connect(self.constraintUpdate2)
        self.dockContentWidget3_2.send_RequesteDesignConstraint_signal.connect(self.constraintConvey)
        self.dockContentWidget3_2.send_deleteID_signal.connect(self.deleteDesignParameterbyDesignConstraint)




        self.sendRightButton.clicked.connect(self.dockContentWidget3.checkSend)
        #self.dockContentWidget3.send_SendSTMT_signal.connect(self.dockContentWidget3_2.receiveConstraintSTMT)
        self.dockContentWidget3.send_SendID_signal.connect(self.dockContentWidget3_2.receiveConstraintID)
        self.dockContentWidget3.send_RecieveDone_signal.connect(self.dockContentWidget3_2.removeCurrentIndexItem)
        self.dockContentWidget3.send_RootDesignConstraint_signal.connect(self.setRootConstraint)
        self.dockContentWidget3.send_SendCopyConstraint_signal.connect(self.constraintToTemplateHandler)
        self.dockContentWidget3.send_UpdateDesignConstraintID_signal.connect(self.get_constraint_update_design)
        self.dockContentWidget3.send_UpdateDesignConstraint_signal.connect(self.constraintUpdate1)
        self.dockContentWidget3.send_RequesteDesignConstraint_signal.connect(self.constraintConvey)
        self.dockContentWidget3.send_deleteID_signal.connect(self.deleteDesignParameterbyDesignConstraint)

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
        print("************************Initalizing Graphic Interface Complete")

    # def threading_test(self,count):


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
            topAST = self._QTObj._qtProject._ParseTreeForDesignConstrain[module]._ast
            topAST = element_ast.ElementTransformer().visit(topAST)
            topAST = variable_ast.VariableTransformer().visit(topAST)
            # topAST = element_ast.MacroTransformer1().visit(topAST)
            # topAST = element_ast.MacroTransformer2().visit(topAST)
            code = astunparse.unparse(topAST)
            print(code)
        except:
            print("encoding fail")

    def checkNameDuplication(self,checkItem):
        name = checkItem._ItemTraits['_DesignParameterName']
        for item in self.scene.items():
            try:
                if name == item._ItemTraits['_DesignParameterName']:
                    print("ERROR: Duplicated Name")
                    return True
            except:
                continue
        return False

    def makeBoundaryWindow(self):
        self.bw = SetupWindow._BoundarySetupWindow()
        self.bw.show()
        # self.bw.send_BoundarySetup_signal.connect(self.updateGraphicItem)
        self.bw.send_DestroyTmpVisual_signal.connect(self.deleteGraphicItem)
        self.bw.send_BoundaryDesign_signal.connect(self.createNewDesignParameter)
        self.bw.send_Warning_signal.connect(self.dockContentWidget4ForLoggingMessage._WarningMessage)
        self.scene.send_xyCoordinate_signal.connect(self.bw.AddBoundaryPointWithMouse)
        self.bw.send_Destroy_signal.connect(self.delete_obj)


    def makePathWindow(self):
        self.scene.itemListClickIgnore(True)
        # self.scene.
        self.pw = SetupWindow._PathSetupWindow()
        self.pw.show()
        self.pw.send_PathSetup_signal.connect(self.updateGraphicItem)
        self.pw.send_PathDesign_signal.connect(self.createNewDesignParameter)
        self.pw.send_DestroyTmpVisual_signal.connect(self.deleteGraphicItem)
        self.pw.send_Destroy_signal.connect(self.delete_obj)
        self.scene.send_xyCoordinate_signal.connect(self.pw.AddPathPointWithMouse)                          # Mouse Interaction connect

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
        scf = QFileDialog.getOpenFileName(self,'Load Design Parameter','./PyQTInterface/modules')
        try:
            _fileName=scf[0]
            self._QTObj._qtProject._loadDesignParameterAsPickle(_file=_fileName)
        except:
            print("Save DesignParameter Failed")
            self.dockContentWidget4ForLoggingMessage._WarningMessage("Save DesignParameter Fail: Unknown")

            #################DesignParameter Load ######################
        for module in self._QTObj._qtProject._DesignParameter:
            for id in self._QTObj._qtProject._DesignParameter[module]:
                visualItem = self.createVisualItemfromDesignParameter(self._QTObj._qtProject._DesignParameter[module][id])
                self.updateGraphicItem(visualItem)

        self.dockContentWidget4ForLoggingMessage._InfoMessage("Project Load Done")


    def makeFilterWindow(self):
        self.fw = FilterPractice._FilterWindow()
        self.fw.show()

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

    # def closingPathWidget(self):
    #     self.scene.itemListClickIgnore(False)
    #     del self.pw

    def delete_obj(self, obj):
        if obj == 'cw':
            del self.cw
        if obj == 'bw':
            del self.bw
        if obj == 'pw':
            del self.pw
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
        visual_item_list = self.scene.items()
        _blockList = list()
        _layerList = list()
        layernum2name = LayerReader._LayerNumber2CommonLayerName(LayerReader._LayerMapping)

        for index in range(0,len(visual_item_list)):
            # print(visual_item_list[index].__class__.__name__)
            if visual_item_list[index].__class__.__name__ == "_RectBlock":
                _blockList.append(visual_item_list[index])

        for i in range(0,len(_blockList)):
            _newLayer = layernum2name[str(_blockList[i].__dict__['_BlockTraits']['_Layer'])]
            if _newLayer in _layerList:
                pass
            else:
                _layerList.append(_newLayer)

        self.dockContentWidget1_2.updateList(_layerList)

        # layer 정보 : _RectBlock
        # layer visual on/off -> _Rectblock on/off  <important>
        # layer click on/off  -> _VisualizationItem

    def deleteGraphicItem(self,graphicItem):
        self.scene.removeItem(graphicItem)

    def newProject(self):
        self.npw = _VersatileWindow("NewProject")
        self.npw.show()
        self.npw.send_Name_signal.connect(self._QTObj._createProject)

    def loadProject(self):
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


    def saveProject(self):
        scf = QFileDialog.getSaveFileName(self,'Save Project','./PyQTInterface/Project/')

        try:
            _fileName=scf[0] + ".bin"

            # fileName=_fileName.split('/')[-1]
            self.updateXYCoordinatesForDisplay()
            self._QTObj._saveProject(_name=_fileName)
            print(1)
        except:
            print("Save Project Failed")
            self.dockContentWidget4ForLoggingMessage._WarningMessage("Save Project Fail: Unknown")
            pass

        # self._QTObj._saveProject()

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

    def loadGDS(self):      ############################################################## What I need to fix is :  LoadGDS means not load SRef!!!! I have to change target GDS Module is root module!!!
        scf = QFileDialog.getOpenFileName(self,'Load GDS','./PyQTInterface/GDSFile')
        try:
            cm = self._CurrentModuleName
            _fileName=scf[0]
            _moduleName = _fileName.replace(".gds","")
            _moduleName = _moduleName.split('/')[-1]
            originalModuleList = set(self._QTObj._qtProject._DesignParameter)
            # self.dockContentWidget4ForLoggingMessage._InfoMessage("Load GDS File Starts.")
            print("loadFile")
            self._QTObj._qtProject._loadDesignsFromGDSlegacy(_file = _fileName, _topModuleName = _moduleName)
            print("FileLoadEnd")
            visual_item_list = []

            if self.progrseeBar_unstable == True:
                updateModuleList = set(self._QTObj._qtProject._DesignParameter)
                addedModuleList = list(updateModuleList-originalModuleList)

                randModule = addedModuleList[0]
                anyId = list(self._QTObj._qtProject._DesignParameter[randModule])[0]
                hierarchyHint=self._QTObj._qtProject._HierarchyFromRootForDesignParameter(_id=anyId,_ParentName=randModule)
                rootModule = list(hierarchyHint[0])[0]

                moduleLength = len(addedModuleList)
                minimumModule = round(moduleLength/50)

                idLength = 0
                for modules in addedModuleList:
                    idLength += len(self._QTObj._qtProject._DesignParameter[modules])


                if DEBUG:
                    print(f'idLength= {idLength}')
                j = 0
                self.qpd = QProgressDialog("Load GDS... (File Transform)","Cancel",0,idLength,self)
                self.qpd.setWindowModality(Qt.WindowModal)
                self.qpd.show()

            self._QTObj._qtProject._UpdateXYCoordinatesForDisplay(_ParentName=rootModule)
            for module in addedModuleList:
                try:
                    for id in self._QTObj._qtProject._DesignParameter[module]:
                        # Step 1 : From QtDeisngParameter -> get AST
                        tmpAST = self._QTObj._qtProject._ElementManager.get_dp_return_ast(self._QTObj._qtProject._DesignParameter[module][id])
                        # Step 2: From ast -> create Constraint
                        design_dict = self._QTObj._qtProject._feed_design(design_type='constraint', module_name=module, _ast=tmpAST, element_manager_update=False)
                        # Step 3: From QtDesignconstraint -> create Visual_ast item
                        try:
                            if design_dict['constraint']:
                                self.dockContentWidget3_2.createNewConstraintAST(_id=design_dict['constraint_id'],
                                                                                 _parentName=module,
                                                                                 _DesignConstraint=self._QTObj._qtProject._DesignConstraint)
                        except:
                            print("Invalid ast.")
                        # Step 4: From QtDesignParameter -> create Visual Element item
                        if self._QTObj._qtProject._DesignParameter[module][id]._DesignParameter['_DesignParametertype'] == 3:
                            continue
                        visualItem = self.createVisualItemfromDesignParameter(self._QTObj._qtProject._DesignParameter[module][id])
                        visual_item_list.append(visualItem)
                        # self.updateGraphicItem(visualItem)
                except:
                    print("module:",module)
                    print("ID:",id)
                    print("ErrorOccured")

                if self.progrseeBar_unstable == True:
                    j += len(self._QTObj._qtProject._DesignParameter[module])
                    self.qpd.setValue(j)
                    if self.qpd.wasCanceled():
                        break

            self.qpd2 = QProgressDialog("Load GDS... (Creating VisualItem)", "Cancel", 0, len(visual_item_list)-1, self)
            self.qpd2.setWindowModality(Qt.WindowModal)
            self.qpd2.show()
            multicore = False
            corenum = 8
            if multicore:
                chunk = int(len(visual_item_list)/corenum)
                procs = []
                for i in range(corenum):
                    if i != corenum-1:
                        proc = mp.Process(target=self.updateGraphicItem, args=visual_item_list[20*i:20*i+20])
                    else:
                        proc = mp.Process(target=self.updateGraphicItem, args=visual_item_list[20 * i:])
                    procs.append(proc)
                    proc.start()
                for proc in procs:
                    proc.join()
            else:
                for i, vis in enumerate(visual_item_list):
                    self.updateGraphicItem(vis)
                    self.qpd2.setValue(i)
                    if self.qpd2.wasCanceled():
                        break

            self._QTObj._qtProject._resetXYCoordinatesForDisplay()

            # After Load All DesignParameter!!!! Now Setting For SRef!!!!
            # for module in addedModuleList:
            #     for id in self._QTObj._qtProject._DesignParameter[module]:
            #         if self._QTObj._qtProject._DesignParameter[module][id]._DesignParameter['_DesignParametertype'] == 3:   #In Case Of SRef!
            #
            #             correspondingModule = self._QTObj._qtProject._DesignParameter[module][id]._DesignParameter['_DesignObj']
            #             for correspondingID in self._QTObj._qtProject._DesignParameter[correspondingModule]:
            #                 print(correspondingID)
            #                 correspondingVisualItem = self.visualItemDict[correspondingID]
            #                 srefVisualItem = self.visualItemDict[id]
            #                 srefVisualItem.updateDesignObj(correspondingVisualItem)
            #                 # print("ee!")
            #             # print("find!!!")

        except:
            print("Load GDS Failed")
            self.dockContentWidget4ForLoggingMessage._WarningMessage("Load GDS Fail: Unknown")
            pass

        print("Load GDS Done")


    # def loadPy(self):
    #     self.loadWorker = ThreaderForProgress.loadPyWorker()
    #     self.loadWorker.loadPy(contentWidget=self.dockContentWidget3_2,_QTobj=self._QTObj,_CurrentModuleName= self._CurrentModuleName)
    #
    # def aloadPy(self):
    #     self.qpd = SetupWindow._Progress()
    #     self.qpd.show()
    #
    # def bloadPy(self,_fileName):
    #
    #     self.dockContentWidget4ForLoggingMessage._InfoMessage("Convert Pysource to AST.")
    #     _none, _id = self._QTObj._qtProject._loadConstraintsFromPySource(_file=_fileName, _topModuleName=self._CurrentModuleName)
    #     self.dockContentWidget4ForLoggingMessage._InfoMessage("Conversion Done!")
    #
    #     self.dockContentWidget4ForLoggingMessage._InfoMessage("Convert DC to TreeView")
    #     self.dockContentWidget3_2.createNewConstraintAST(_id=_id, _parentName=self._CurrentModuleName, _DesignConstraint=self._QTObj._qtProject._DesignConstraint)
    #     self.dockContentWidget4ForLoggingMessage._InfoMessage("Conversion Done!")




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
        self.scene.addItem(variableVisualItem)
        pass


    def createNewDesignParameter(self,_DesignParameter):
        print(_DesignParameter)
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

            try:
                if design_dict['constraint']:
                    self.dockContentWidget3_2.createNewConstraintAST(_id=design_dict['constraint_id'],
                                                                     _parentName=self._CurrentModuleName,
                                                                     _DesignConstraint=self._QTObj._qtProject._DesignConstraint)
            except:
                print("Invalid ast.")



    def deleteDesignParameter(self,_ID):    # input : DesignParameterID
        module = _ID[:-1]
        while not module in self._QTObj._qtProject._DesignParameter:
            module = module[:-1]

        dc_id = self._QTObj._qtProject._ElementManager.get_dc_id_by_dp_id(_ID)

        deletionItems = self.scene.selectedItems()
        for deleteItem in deletionItems:
            self.scene.removeItem(deleteItem)

        self.dockContentWidget3.removeItem_by_ID(dc_id)     #Remove Item displays in constraint Window
        self.dockContentWidget3_2.removeItem_by_ID(dc_id)

    def deleteDesignParameterbyDesignConstraint(self,dc_id): # input : DesignconstraintID
        dc_module = dc_id[:-1]
        while not dc_module in self._QTObj._qtProject._DesignConstraint:
            dc_module = dc_module[:-1]

        try:
            dp_id = self._QTObj._qtProject._ElementManager.get_dp_id_by_dc_id(dc_id)  # get DesignParameterID
        except:
            # del self._QTObj._qtProject._DesignConstraint[dc_module][dc_id]
            return None
        dp_module = dp_id[:-1]
        while not dp_module in self._QTObj._qtProject._DesignParameter:
            dp_module = dp_module[:-1]

        self.visualItemDict[dp_id]
        self.scene.removeItem(self.visualItemDict[dp_id])
        # del self._QTObj._qtProject._DesignParameter[dp_module][dp_id]
        # del self._QTObj._qtProject._DesignConstraint[dc_module][dc_id]



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
        return visualItem

    def updateVisualItemFromDesignParameter(self,DesignParameter):
        id = DesignParameter._id
        if id in self.visualItemDict:
            self.visualItemDict[id].updateTraits(DesignParameter._DesignParameter)
            return self.visualItemDict[id]
        return None

    def updateDesignParameter(self,_DesignParameter):
        _ID = _DesignParameter['_id']
        _Module = _ID[:-1]
        while (_Module in self._QTObj._qtProject._DesignParameter) == False:
            _Module = _Module[:-1]
        # _Module = re.sub('[0-9]+', '',_ID)
        print(_Module)

        for key in _DesignParameter:
            self._QTObj._qtProject._DesignParameter[_Module][_ID]._setDesignParameterValue(_index = key, _value= _DesignParameter[key])
        self._QTObj._qtProject._DesignParameter[_Module][_ID]._setDesignParameterName(_DesignParameter['_DesignParameterName'])

        # self._QTObj._qtProject._DesignParameter[_Module][_ID]._updateVisualItem()
        # visualItem = self._QTObj._qtProject._DesignParameter[_Module][_ID]._VisualizationItemObj
        visualItem = self.updateVisualItemFromDesignParameter(self._QTObj._qtProject._DesignParameter[_Module][_ID])
        self.updateGraphicItem(visualItem)

        design_dict = self._QTObj._qtProject._update_design(design_type='parameter', module_name=self._CurrentModuleName,
                                                          dp_dict=_DesignParameter, id=_ID)

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


    def createNewConstraintAST(self,_AST):

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
            design_dict = self._QTObj._qtProject._feed_design(design_type='constraint', module_name=self._CurrentModuleName, _ast= _AST)
            self.dockContentWidget3_2.createNewConstraintAST(_id=design_dict['constraint_id'], _parentName=self._CurrentModuleName,
                                                             _DesignConstraint=self._QTObj._qtProject._DesignConstraint)

            try:
                if design_dict['parameter']:
                    visualItem = self.createVisualItemfromDesignParameter(
                        self._QTObj._qtProject._DesignParameter[self._CurrentModuleName][design_dict['parameter_id']])
                    self.updateGraphicItem(visualItem)
            except:
                print("Invalid design parameter dict")



    def constraintConvey(self):
        self.dockContentWidget3._DesignConstraintFromQTobj = self._QTObj._qtProject._DesignConstraint
        self.dockContentWidget3_2._DesignConstraintFromQTobj = self._QTObj._qtProject._DesignConstraint

    def constraintUpdate1(self, updateDict):
        _id = updateDict['_id']
        _Module = re.sub('[0-9]+', '', _id)

        for key in updateDict:
            if type(updateDict[key]) == list:       #If UpdateDict[key] is compound stmt.
                for i, stmtID in enumerate(updateDict[key]):
                    tmpModule = re.sub('[0-9]+', '', stmtID)
                    astObj = self._QTObj._qtProject._DesignConstraint[tmpModule][stmtID]._ast
                    updateDict[key][i] = astObj
            else:  # It could be simple stmt or just value
                tmpID = updateDict[key]
                try:  # Simple Stmt Case
                    tmpModule = re.sub('[0-9]+', '', tmpID)
                    updateDict[key] = self._QTObj._qtProject._DesignConstraint[tmpModule][tmpID]._ast
                except:  # Just value case
                    print('debug, key = {}, module = {}, id = {}'.format(key, tmpModule, tmpID))
                    pass
        self._QTObj._qtProject._setDesignConstraintValueWithSTMT(_module=_Module,_id=_id,_STMT=updateDict)
        _STMT = self._QTObj._qtProject._DesignConstraint[_Module][_id]._readConstraintValueAsSTMT()

        self.dockContentWidget3.receiveConstraintSTMT(_STMT)

    def constraintUpdate2(self, updateDict):
        _id = updateDict['_id']
        _Module = re.sub('[0-9]+', '', _id)

        for key in updateDict:
            if type(updateDict[key]) == list:       #If UpdateDict[key] is compound stmt.
                for i, stmtID in enumerate(updateDict[key]):
                    tmpModule = re.sub('[0-9]+', '', stmtID)
                    astObj = self._QTObj._qtProject._DesignConstraint[tmpModule][stmtID]._ast
                    updateDict[key][i] = astObj
            else:   # It could be simple stmt or just value
                tmpID = updateDict[key]
                try:    # Simple Stmt Case
                    tmpModule = re.sub('[0-9]+', '', tmpID)
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
            print(1)
            # for module in self._QTObj._qtProject._DesignConstraint:
                # self._QTObj._qtProject._DesignConstraint[module][]
            # print(1)
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
            # print(1)
        except:
            print("Load Constraint Failed")
            self.dockContentWidget4ForLoggingMessage._WarningMessage("Save DesignConstraint Fail: Unknown")
            pass

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
        # print(1)

    def parameterToTemplateHandler(self,designParameterItemIDList,type):
        designParameterList = list()
        for id in designParameterItemIDList:
            # module = re.sub('[0-9]+', '',id)
            module = id[:-1]
            while not module in self._QTObj._qtProject._DesignParameter:
                module = module[:-1]
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
    def __init__(self):
        super(_CustomView, self).__init__()
        self.show()
        self.setMouseTracking(True)

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

        super().mousePressEvent(event)

    # def dropEvent(self, event) -> None:
    #     super
    def contextMenuEvent(self, event) -> None:
        variable_create_array = QAction("create array variable", self)
        variable_create_distance = QAction("create distance variable", self)
        variable_create_enclosure = QAction("create enclousre variable", self)
        variable_create_connect = QAction("create connect variable", self)

        menu = QMenu(self)
        menu.addAction(variable_create_array)
        menu.addAction(variable_create_distance)
        menu.addAction(variable_create_enclosure)
        menu.addAction(variable_create_connect)

        variable_create_array.triggered.connect(lambda tmp: self.variable_emit('array'))
        variable_create_distance.triggered.connect(lambda tmp: self.variable_emit('distance'))
        variable_create_enclosure.triggered.connect(lambda tmp: self.variable_emit('enclosure'))
        variable_create_connect.triggered.connect(lambda tmp: self.variable_emit('connect'))


        menu.exec(event.globalPos())

    def variable_emit(self, type):
        if type == 'array':
            self.variable_signal.emit('array')
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

class _CustomScene(QGraphicsScene):
    send_debug_signal = pyqtSignal()
    send_xyCoordinate_signal = pyqtSignal(QGraphicsSceneMouseEvent)
    send_itemList_signal = pyqtSignal(list)
    send_parameterIDList_signal = pyqtSignal(list,int)
    send_move_signal = pyqtSignal(QPointF)
    send_moveDone_signal = pyqtSignal()
    send_deleteItem_signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.moveFlag = False
        self.listIgnoreFlag = False
        self.oldPos = QPointF(0,0)
        # self.



    def mousePressEvent(self, event):
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
        self.send_xyCoordinate_signal.emit(event);
        if self.moveFlag is True:
            self.moveFlag = False
            self.send_moveDone_signal.emit()
            print("moveDone emmit")
        else:
            self.oldPos = event.scenePos()
        super().mousePressEvent(event)

    def send_item_list(self):
        itemList = self.selectedItems()
        # print(itemList)
        self.send_itemList_signal.emit(itemList)


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
        elif QKeyEvent.key() == Qt.Key_Escape:
            print("selectionClear")
            self.clearSelection()

        super().keyPressEvent(QKeyEvent)

            #signal Out!! with DesignaParameterItems

    def mouseMoveEvent(self, QGraphicsSceneMouseEvent):
        delta = QPointF(QGraphicsSceneMouseEvent.scenePos()-self.oldPos)
        if self.moveFlag is True:
            self.send_move_signal.emit(delta)
        self.oldPos = QGraphicsSceneMouseEvent.scenePos()

    def itemListClickIgnore(self,flag):
        self.listIgnoreFlag = flag

    # def deliveryContent(self):


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





if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = _MainWindow()
    sys.exit(app.exec_())

