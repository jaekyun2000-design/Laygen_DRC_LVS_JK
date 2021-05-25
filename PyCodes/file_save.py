class FileSaveFormat:
    def __init__(self):
        self.top_module = None


    def save_from_qt_interface(self, main_window):
        self.top_module = main_window._CurrentModuleName
        self.save_constraint_tree_info(main_window)


    def save_constraint_tree_info(self,main_window):
        from PyQt5.QtCore import Qt
        id_items_for_run = main_window.dockContentWidget3.model.findItems('',Qt.MatchContains,1)
        id_items_for_edit = main_window.dockContentWidget3_2.model.findItems('',Qt.MatchContains,1)

        self.id_items_for_run = [item.text() for item in id_items_for_run]
        self.id_items_for_edit = [item.text() for item in id_items_for_edit]

    def save_user_variable_info(self,main_window):
        pass

    def load_from_constraint_tree_info(self,main_window, _DesignConstraint):
        for id in self.id_items_for_run:
            main_window.dockContentWidget3.createNewConstraintAST(_id=id, _parentName=self.top_module,
                                                                   _DesignConstraint= _DesignConstraint)
        for id in self.id_items_for_edit:
            main_window.dockContentWidget3_2.createNewConstraintAST(_id=id, _parentName=self.top_module,
                                                                   _DesignConstraint= _DesignConstraint)

    def load_user_variable_info(self,main_window):
        pass