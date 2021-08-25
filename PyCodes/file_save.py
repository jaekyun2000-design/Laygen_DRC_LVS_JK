import warnings
from PyQTInterface import calculator

class FileSaveFormat:
    def __init__(self):
        self.top_module = None
        self.id_items_for_edit = []
        self.id_items_for_run = []
        self.user_variables = []
        self.user_variables_ids = []
        self.variable_store_list = []
        self.module_list = []
        self.module_save_file_dict = dict()
        self._DummyConstraints = None

    def save_from_qt_interface(self, main_window, sub_module=True):
        self.top_module = main_window._CurrentModuleName
        self.save_constraint_tree_info(main_window)
        if 'dv' in main_window.__dict__:
            self.save_user_variable_info(main_window)
        self.save_extra_ast_info(main_window)
        self.save_calculator_extra_info()
        if sub_module:
            self.save_module_info(main_window)



    def save_constraint_tree_info(self,main_window):
        from PyQt5.QtCore import Qt
        id_items_for_run = main_window.dockContentWidget3.model.findItems('',Qt.MatchContains,1)
        id_items_for_edit = main_window.dockContentWidget3_2.model.findItems('',Qt.MatchContains,1)

        self.id_items_for_run = [item.text() for item in id_items_for_run]
        self.id_items_for_edit = [item.text() for item in id_items_for_edit]

    def save_user_variable_info(self,main_window):
        # self.user_variables = list(main_window.dv.variableDict.values())
        self.user_variables = main_window.dv.variableDict
        self.user_variables_ids = main_window.dv.idDict
        self.variable_store_list = main_window.variable_store_list
        #TODO id save

    def save_extra_ast_info(self,main_window):
        self._DummyConstraints = main_window._DummyConstraints

    def save_calculator_extra_info(self):
        self.presetDict = calculator.ExpressionCalculator.presetDict

    def save_module_info(self, main_window):
        self.module_list = list(filter(lambda element_name: element_name != self.top_module, main_window.module_name_list))
        for module_name in self.module_list:
            if module_name == self.top_module:
                continue
            save_file = FileSaveFormat()
            save_file.save_from_qt_interface(main_window.module_dict[module_name], False)
            self.module_save_file_dict[module_name] = save_file

    def load_qt_interface(self,main_window, _DesignConstraint):
        main_window._CurrentModuleName = self.top_module
        self.load_from_constraint_tree_info(main_window, _DesignConstraint)
        self.load_user_variable_info(main_window)
        self.load_extra_ast_info(main_window)
        self.load_calculator_extra_info()
        self.load_module_info()

    def load_from_constraint_tree_info(self,main_window, _DesignConstraint):
        if 'id_items_for_run' not in self.__dict__:
            warnings.warn("There is no constraint window information.")
            return
        for id in self.id_items_for_run:
            main_window.dockContentWidget3.createNewConstraintAST(_id=id, _parentName=self.top_module,
                                                                   _DesignConstraint= _DesignConstraint)
        for id in self.id_items_for_edit:
            main_window.dockContentWidget3_2.createNewConstraintAST(_id=id, _parentName=self.top_module,
                                                                   _DesignConstraint= _DesignConstraint)

    def load_user_variable_info(self,main_window):
        from PyQTInterface import variableWindow
        if 'user_variables' in self.__dict__:
            variableWindow._createNewDesignVariable.variableDict = self.user_variables
            main_window.dv.variableDict = self.user_variables
        if 'user_variables_ids' in self.__dict__:
            variableWindow._createNewDesignVariable.idDict = self.user_variables_ids
            main_window.dv.idDict = self.user_variables_ids
        if 'variable_store_list' in self.__dict__:
            main_window.variable_store_list = self.variable_store_list
        variable_info_lists = [ [variable['DV'], variable['value']] for variable in self.user_variables.values()]
        for variable_info_list in variable_info_lists:
            main_window.dv.updateList(variable_info_list,'add')

        # main_window.dv.initUI()
        # main_window.dv.variableDict = self.user_variables_ids
        # main_window.dv.idDict = self.user_variables_ids
        if 'user_variables' not in self.__dict__:
            warnings.warn("There is no user_variables window information.")
            return
        # for variable_dict in self.user_variables:
        #     main_window.dv.updateList(list(variable_dict.values()), _type='add')
        #     main_window.dv.variableDict.append(variable_dict)

        # for variable_dict in self.user_variables.values():
        #     main_window.dv.updateList(list(variable_dict.values()), _type='add')

    def load_extra_ast_info(self,main_window):
        if '_DummyConstraints' in self.__dict__:
            if self._DummyConstraints:
                main_window._DummyConstraints = self._DummyConstraints

    def load_calculator_extra_info(self):
        calculator.ExpressionCalculator.presetDict = self.presetDict

    def load_module_info(self):
        if self.module_list:
            for module in self.module_list:
                if module not in self.module_save_file_dict:
                    raise Exception(f'{module} info file does not exist.')
                #TODO complete code after developing new_main_windw fcn
                self.module_save_file_dict[module]

