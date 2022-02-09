from PyQt5.QtWidgets import QUndoCommand, QUndoStack
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
