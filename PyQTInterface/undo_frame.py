from PyQt5.QtWidgets import QUndoCommand, QUndoStack, QUndoView, QMessageBox
from PyQt5.QtCore import pyqtSignal
import warnings
import datetime

# class Sanpshot:
#     def __init__(self):
#         pass
#
# class SceneSanp(Sanpshot):
#     def __init__(self):
#         pass
#
# class ConstraintSanp(Sanpshot):
#     def __init__(self):
#         self.generator_widget = generator_widget
#         self.candidate_widget = candidate_widget
#
# class DesignObjectSanp(Sanpshot):
#     def __init__(self):
#         pass


class ActionCommand(QUndoCommand):
    project_name = "None"

    def __init__(self, command_log=None):
        super(ActionCommand, self).__init__()
        self.setText(command_log)
        self.save_time= datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.command_log = command_log

    def get_file_name(self):
        return f'./PyQTInterface/Project/autosave/{self.project_name}{self.save_time}'






# class DesignConstraintUndo(QUndoCommand):
#     def __init__(self, source_widget, target_widget,_id, _module, _dc):
#         super(MoveDesignConstraint, self).__init__()
#         # self.text = text
#         self.source_widget = source_widget
#         self.target_widget = target_widget
#         self._id = _id
#         self._module = _module
#         self._dc = _dc
#
#
# class MoveDesignConstraint(QUndoCommand):
#     def __init__(self, source_widget, target_widget,_id, _module, _dc):
#         super(MoveDesignConstraint, self).__init__()
#         # self.text = text
#         self.source_widget = source_widget
#         self.target_widget = target_widget
#         self._id = _id
#         self._module = _module
#         self._dc = _dc
#
#     def undo(self):
#         self.source_widget.createNewConstraintAST(_id=self._id, _parentName=self._module, _DesignConstraint=self._dc)

# class CreateDesignConstraint(DesignConstraintUndo):
#     def __init__(self, source_widget, target_widget,_id, _module, _dc):
#         super(CreateDesignConstraint, self).__init__(source_widget, target_widget,_id, _module, _dc)
#
#     def undo(self):
#         print('delete dc')


class UndoStack(QUndoStack):

    def undo(self):
        # super(UndoStack, self).undo()
        warnings.warn('Currently, only snapshot (autosave) mode is developed.')

class UndoWidget(QUndoView):
    request_load_save_file_signal = pyqtSignal(str)
    def __init__(self):
        super(UndoWidget, self).__init__()

    def mouseDoubleClickEvent(self,event):
        super(UndoWidget, self).mouseDoubleClickEvent(event)
        index = self.selectedIndexes()[0].row()-1
        if index == -1:
            return
        selected_command = self.stack().command(index)
        self.target_save_file_name = f'{selected_command.get_file_name()}.bin'
        info_widget = QMessageBox()
        info_widget.setWindowTitle("Rollback!")
        info_widget.setText("Do you want to rollback?")
        info_widget.setStandardButtons(QMessageBox.Apply | QMessageBox.Abort)
        # self.info_widget.show()
        info_widget.buttonClicked.connect(self.request_load_save_file)
        info_widget.exec()



    def request_load_save_file(self,button):
        if button.text() == 'Apply':
            self.request_load_save_file_signal.emit(self.target_save_file_name)
        # print(selected_command.get_file_name())