import user_setup
from PyQTInterface import SetupWindow
from PyQTInterface.delegator import delegator

from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit
    
    
class WidgetDelegator(delegator.Delegator):
    def __init__(self, main_window):
        super(WidgetDelegator, self).__init__(main_window)

    def make_boundary_window(self):
        self.main_window.bw = SetupWindow._BoundarySetupWindow()
        self.main_window.bw.show()
        self.main_window.bw.send_BoundarySetup_signal.connect(self.main_window.updateGraphicItem)
        self.main_window.bw.send_DestroyTmpVisual_signal.connect(self.main_window.deleteGraphicItem)
        self.main_window.bw.send_design_message.connect(self.main_window.design_delegator.message_delivery)
        self.main_window.bw.send_Warning_signal.connect(self.main_window.dockContentWidget4ForLoggingMessage._WarningMessage)
        self.main_window.scene.send_xy_signal.connect(self.main_window.bw.AddBoundaryPointWithMouse)
        self.main_window.scene.send_xy_signal.connect(self.main_window.bw.clickCount)
        self.main_window.scene.send_mouse_move_xy_signal.connect(self.main_window.bw.mouseTracking)
        self.main_window.bw.send_Destroy_signal.connect(self.main_window.delete_obj)

    def make_polygon_window(self):
        self.main_window.pow = SetupWindow._PolygonSetupWindow()
        self.main_window.pow.show()
        self.main_window.pow.send_PolygonSetup_signal.connect(self.main_window.updateGraphicItem)
        self.main_window.pow.send_PolygonDesign_signal.connect(self.main_window.createNewDesignParameter)
        self.main_window.pow.send_design_message.connect(self.main_window.design_delegator.message_delivery)
        self.main_window.pow.send_Warning_signal.connect(self.main_window.dockContentWidget4ForLoggingMessage._WarningMessage)
        self.main_window.scene.send_xy_signal.connect(self.main_window.pow.AddPolygonPointWithMouse)
        # self.main_window.scene.send_xy_signal.connect(self.main_window.pow.clickCount)
        # self.main_window.scene.send_mouse_move_xy_signal.connect(self.main_window.pow.mouseTracking)
        self.main_window.pow.send_Destroy_signal.connect(self.main_window.delete_obj)

    def makePathWindow(self):
        self.main_window.scene.itemListClickIgnore(True)
        self.main_window.pw = SetupWindow._PathSetupWindow()
        self.main_window.pw.show()
        self.main_window.pw.send_PathSetup_signal.connect(self.main_window.updateGraphicItem)
        self.main_window.pw.send_PathDesign_signal.connect(self.main_window.createNewDesignParameter)
        self.main_window.pw.send_DestroyTmpVisual_signal.connect(self.main_window.deleteGraphicItem)
        self.main_window.pw.send_Destroy_signal.connect(self.main_window.delete_obj)
        self.main_window.scene.send_xy_signal.connect(self.main_window.pw.AddPathPointWithMouse)
        self.main_window.scene.send_xy_signal.connect(self.main_window.pw.clickCount)  # Mouse Interaction connect
        self.main_window.scene.send_mouse_move_xy_signal.connect(self.main_window.pw.mouseTracking)
        self.main_window.scene.send_doubleclick_signal.connect(self.main_window.pw.quitCreate)

    def loadSRefWindow(self):
        self.main_window.ls = SetupWindow._LoadSRefWindow(purpose='main_load')
        self.main_window.ls.show()
        self.main_window.ls.send_DesignConstraint_signal.connect(self.main_window.srefCreate)
        self.main_window.scene.send_xy_signal.connect(self.main_window.ls.DetermineCoordinateWithMouse)
        self.main_window.ls.send_destroy_signal.connect(self.main_window.delete_obj)

    def loadMacroCellWindow(self):
        self.main_window.mc = SetupWindow._MacroCellWindow()
        self.main_window.mc.show()
        self.main_window.mc.send_DesignConstraint_signal.connect(self.main_window.design_delegator.create_qt_constraint)
        self.main_window.scene.send_xy_signal.connect(self.main_window.mc.DetermineCoordinateWithMouse)
        self.main_window.mc.send_destroy_signal.connect(self.main_window.delete_obj)

    def makeTextWindow(self):
        self.main_window.txtw = SetupWindow._TextSetupWindow()
        self.main_window.txtw.show()
        self.main_window.txtw.send_TextSetup_signal.connect(self.main_window.updateGraphicItem)
        self.main_window.txtw.send_DestroyTmpVisual_signal.connect(self.main_window.deleteGraphicItem)
        self.main_window.txtw.send_TextDesign_signal.connect(self.main_window.createNewDesignParameter)
        self.main_window.txtw.send_Warning_signal.connect(self.main_window.dockContentWidget4ForLoggingMessage._WarningMessage)
        self.main_window.scene.send_xy_signal.connect(self.main_window.txtw.DetermineCoordinateWithMouse)
        self.main_window.txtw.send_Destroy_signal.connect(self.main_window.delete_obj)

    def makePinWindow(self):
        self.main_window.pinw = SetupWindow._PinSetupWindow()
        self.main_window.pinw.show()
        self.main_window.pinw.send_PinSetup_signal.connect(self.main_window.updateGraphicItem)
        self.main_window.pinw.send_DestroyTmpVisual_signal.connect(self.main_window.deleteGraphicItem)
        self.main_window.pinw.send_PinDesign_signal.connect(self.main_window.createNewDesignParameter)
        self.main_window.pinw.send_Warning_signal.connect(self.main_window.dockContentWidget4ForLoggingMessage._WarningMessage)
        self.main_window.scene.send_xy_signal.connect(self.main_window.pinw.DetermineCoordinateWithMouse)
        self.main_window.pinw.send_Destroy_signal.connect(self.main_window.delete_obj)

    def makePyCodeWindow(self):
        self.main_window.cw = SetupWindow._ConstraintSetupWindowPyCode()
        self.main_window.cw.show()
        self.main_window.cw.send_PyCode_signal.connect(self.main_window.createNewConstraintPyCode)

    def makeConstraintWindowAST(self):
        self.main_window.cw = SetupWindow._ConstraintSetupWindowAST(_ASTapi = self.main_window._ASTapi)
        self.main_window.cw.show()
        self.main_window.cw.send_AST_signal.connect(self.main_window.createNewConstraintAST)
        self.main_window.cw.send_destroy_signal.connect(self.main_window.delete_obj)

    def makeConstraintWindowCUSTOM(self):
        self.main_window.cw = SetupWindow._ConstraintSetupWindowCUSTOM(_ASTapi = self.main_window._ASTapi)
        self.main_window.cw.show()
        self.main_window.cw.send_CUSTOM_signal.connect(self.main_window.createNewConstraintAST)

    def makeVariableWindowCUSTOM(self):
        self.main_window.cw = SetupWindow._VariableSetupWindowCUSTOM(_ASTapi=self.main_window._ASTapi)
        self.main_window.cw.show()
        self.main_window.cw.send_CUSTOM_signal.connect(self.main_window.createNewConstraintAST)

    def convert_elements_to_sref_widget(self, vis_item_list):
        """
        choice between assign generator or create generator
        """
        self.choice_widget = QWidget()
        layout = QHBoxLayout()
        assign_btn = QPushButton('assign')
        create_btn = QPushButton('create')
        layout.addWidget(assign_btn)
        layout.addWidget(create_btn)
        self.choice_widget.setLayout(layout)
        self.choice_widget.show()

        message = delegator.DelegateMessage(arguments=[vis_item_list], target_fcn='convert_elements_to_sref')
        def delievery_message(_):
            self.main_window.design_delegator.message_delivery(message)

        def assign_gen():
            # dp_ids = [vis_item._ElementName for vis_item in vis_item_list]
            dp_ids = [vis_item._ItemTraits['_ElementName'] for vis_item in vis_item_list]
            if user_setup.DL_FEATURE:
                library_name = self.main_window.design_delegator.build_layer_matrix_by_ids(dp_ids)
            self.choice_widget.close()
            self.ls = SetupWindow._LoadSRefWindow(purpose='main_load')
            if user_setup.DL_FEATURE:
                self.ls.update_library(library_name)
            self.ls.show()
            self.ls.send_DesignConstraint_signal.connect(self.main_window.srefCreate)
            self.ls.send_DesignConstraint_signal.connect(delievery_message)
            self.ls.send_exported_sref_signal.connect(self.main_window.createDummyConstraint)
            self.main_window.scene.send_xy_signal.connect(self.ls.DetermineCoordinateWithMouse)
            message = delegator.DelegateMessage(arguments=[vis_item_list], target_fcn='convert_elements_to_sref')

        def create_gen():
            # message = delegator.DelegateMessage(arguments=[vis_item_list], target_fcn='create_sref_by_elements')
            message = delegator.DelegateMessage(arguments=[vis_item_list], target_fcn='create_sref')
            self.main_window.widget_delegator.message_delivery(message)
            # delievery_message(None)
            self.choice_widget.close()

        assign_btn.clicked.connect(assign_gen)
        create_btn.clicked.connect(create_gen)

    def create_sref(self, vis_item_list):
        def send_module_name():
            tmp_dict = {'vis_item_dict': {self.module_name.text() : vis_item_list}}

            message = delegator.DelegateMessage(arguments_dict=tmp_dict, target_fcn='create_sref_by_elements')
            self.main_window.design_delegator.message_delivery(message)

            self.get_module_name_widget.close()

        self.get_module_name_widget = QWidget()

        self.module_name = QLineEdit()
        ok_button = QPushButton()
        ok_button.setText('OK')
        ok_button.clicked.connect(send_module_name)

        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        hbox.addSpacing(200)
        hbox.addWidget(ok_button)

        vbox.addWidget(self.module_name)
        vbox.addLayout(hbox)

        self.get_module_name_widget.setLayout(vbox)
        self.get_module_name_widget.show()