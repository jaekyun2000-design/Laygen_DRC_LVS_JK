import warnings
from PyQTInterface import calculator
import user_setup
import copy
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
        self.user_setups = dict()

    def save_from_qt_interface(self, main_window, sub_module=True):
        self.save_user_setup()
        self.top_module = main_window._CurrentModuleName
        self.save_constraint_tree_info(main_window)
        if 'dv' in main_window.__dict__:
            self.save_user_variable_info(main_window)
        self.save_extra_ast_info(main_window)
        self.save_calculator_extra_info()
        if sub_module:
            self.save_module_info(main_window)
        self.save_snapshot_stack(main_window)


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
            tmp_save_form = FileSaveFormat()
            tmp_save_form.save_from_qt_interface(main_window.module_dict[module_name], False)
            main_window.module_dict[module_name]._QTObj._qtProject.tmp_save_file = tmp_save_form
            save_project = main_window.module_dict[module_name]._QTObj._qtProject
            self.module_save_file_dict[module_name] = save_project

    def save_user_setup(self):
        variable_names = [item for item in dir(user_setup) if not item.startswith('__')]
        for variable_name in variable_names:
            self.user_setups[variable_name] = user_setup.__dict__[variable_name]

    def save_snapshot_stack(self, main_window):
        self.snapshot_stack = main_window.undo_stack.export_data()

    def load_qt_interface(self,main_window, _DesignConstraint, sub_module=True):
        self.load_user_setup()
        # main_window._CurrentModuleName = self.top_module
        main_window.set_module_name(self.top_module)
        self.load_from_constraint_tree_info(main_window, _DesignConstraint)
        self.load_user_variable_info(main_window)
        self.load_extra_ast_info(main_window)
        self.load_calculator_extra_info()
        if sub_module:
            self.load_module_info(main_window)
        self.load_snapshot_stack(main_window)

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

    def load_module_info(self, main_window):
        from PyQTInterface import MainWindow
        if self.module_list:
            for module in self.module_list:
                main_window.module_name_list = copy.deepcopy(self.module_list)
                main_window.module_name_list.append(self.top_module)
                main_window.module_dict[self.top_module] = main_window
                if module not in self.module_save_file_dict:
                    raise Exception(f'{module} info file does not exist.')
                #TODO complete code after developing new_main_windw fcn
                main_window.module_dict[module] = MainWindow._MainWindow()
                main_window.module_dict[module].set_module_name(module)

                main_window.module_dict[module]._QTObj._qtProject = self.module_save_file_dict[module]
                dc = main_window.module_dict[module]._QTObj._qtProject._DesignConstraint
                main_window.module_dict[module]._QTObj._qtProject.tmp_save_file.load_qt_interface(main_window.module_dict[module],dc,False)
                top_module = main_window.module_dict[module]._QTObj._qtProject.tmp_save_file.top_module
                if top_module in main_window.module_dict[module]._QTObj._qtProject._DesignParameter:
                    for id_name, qt_parameter in main_window.module_dict[module]._QTObj._qtProject._DesignParameter[top_module].items():
                        vs_item = main_window.module_dict[module].createVisualItemfromDesignParameter(qt_parameter)
                        vs_item._CreateFlag = False
                        main_window.module_dict[module].updateGraphicItem(vs_item)
                main_window.module_dict[module].module_name_list = main_window.module_name_list
                main_window.module_dict[module].module_dict = main_window.module_dict
                main_window.module_dict[module].hide()


    def load_user_setup(self):
        if 'user_setups' in self.__dict__:
            for name, value in self.user_setups.items():
                user_setup.__dict__[name] = value
        from PyQTInterface.layermap import DisplayReader
        from PyQTInterface.layermap import LayerReader
        LayerReader.run_for_process_update()
        DisplayReader.run_for_process_update()

    def load_snapshot_stack(self, main_window):
        if 'snapshot_stack' in self.__dict__:
            main_window.undo_stack.import_data(self.snapshot_stack)