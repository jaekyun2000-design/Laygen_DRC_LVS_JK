from PyQTInterface import SetupWindow
from PyQTInterface.delegator import delegator

    
    
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
        self.main_window.ls.send_exported_sref_signal.connect(self.main_window.createDummyConstraint)
        self.main_window.scene.send_xy_signal.connect(self.main_window.ls.DetermineCoordinateWithMouse)
        self.main_window.ls.send_destroy_signal.connect(self.main_window.delete_obj)


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
