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
        # self.main_window.bw.send_BoundaryDesign_signal.connect(self.main_window.createNewDesignParameter)
        self.main_window.bw.send_design_message.connect(self.main_window.design_delegator.message_delivery)
        self.main_window.bw.send_Warning_signal.connect(self.main_window.dockContentWidget4ForLoggingMessage._WarningMessage)
        self.main_window.scene.send_xy_signal.connect(self.main_window.bw.AddBoundaryPointWithMouse)
        self.main_window.scene.send_xy_signal.connect(self.main_window.bw.clickCount)
        self.main_window.scene.send_mouse_move_xy_signal.connect(self.main_window.bw.mouseTracking)
        self.main_window.bw.send_Destroy_signal.connect(self.main_window.delete_obj)