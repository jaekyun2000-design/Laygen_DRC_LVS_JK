from PyQTInterface import SetupWindow

class Delegator:
    def __init__(self, main_window):
        self.main_window= main_window

    def create_widget(self, widget_name, widget_type):
        pass

    def close_widget(self, widget_name):
        pass
    
    
    
class SetupWindowDelegator(Delegator):
    def __init__(self):
        super(SetupWindowDelegator, self).__init__()

    def make_boundary_window(self):
        self.main_window.bw = SetupWindow._BoundarySetupWindow()
        self.main_window.bw.show()
