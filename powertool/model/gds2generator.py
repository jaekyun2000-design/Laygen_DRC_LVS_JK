import astunparse
import PyCodes
from gds_editor_ver3 import gds_stream
from PyQTInterface.layermap import LayerReader
from generatorLib import StickDiagram, DesignParameters
from generatorLib import generator_model_api
import collections
from powertool.model import gds2generator_setting
import warnings, traceback
from powertool.model import clustering, routing_geo_searching
import pickle
import copy
import ast, astunparse
from generatorLib import DRC
drc = DRC.DRC()
import types

def load_pickle(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)

class GDS2Generator():
    def __init__(self,debug=False):
        self.top_deisgn_parameter = dict()
        self.cell_list = []
        self.cell_dp_dict = collections.OrderedDict()
        self.element_parameter_dict = dict()
        self.root_cell = None
        # self.layer_num2name = LayerReader._LayerNumber2LayerName(LayerReader._LayerMapping)

        # if debug:
        #     self.inv_gen = GDS2Generator(False)
        #     self.inv_gen.load_gds('G:\OneDrive - postech.ac.kr\GeneratorAutomation\VariableSuggestion-git\INV2.gds')
        #     self.inv_gen.get_cell_names()
        #     self.inv_gen.set_root_cell('INV')

    def save_as_pickle(self,file_name):
        with open(file_name, 'wb') as f:
            pickle.dump(self,f)

    def code_generation_for_subcell(self, _ast=None):
        from PyCodes import element_ast
        # debug_sref_ast = element_ast.Sref()
        # debug_sref_ast.name = 'testcell'
        # debug_sref_ast.library = 'NMOSWithDummy'
        # debug_sref_ast.className = '_NMOS'
        # debug_sref_ast.XY = [[0,0]]
        # debug_sref_ast.calculate_fcn = '_CalculateNMOSDesignParameter'
        # debug_sref_ast.parameters = dict(
        #     _NMOSNumberofGate=3, _NMOSChannelWidth=400, _NMOSChannellength=60, _NMOSDummy=False
        # )
        # debug_sref_ast = element_ast.Sref()
        # debug_sref_ast.name = 'inv'
        # debug_sref_ast.library = 'Inverter'
        # debug_sref_ast.className = '_Inverter'
        # debug_sref_ast.XY = [[0,0]]
        # debug_sref_ast.calculate_fcn = '_CalculateDesignParameter'
        # debug_sref_ast.parameters = dict(
        #     _Finger=5, _ChannelWidth=400, _ChannelLength=60,
        #     _NPRatio=2, _VDD2VSSHeight=None, _Dummy=False
        # )


        # target_ast = debug_sref_ast
        target_ast = _ast
        target_cell_name = target_ast.name
        if (target_ast.name == '' or None) or (target_ast.XY == '' or None):
            print(" Invalid Name or Coordinates")
            return

        self.code = f'_Name="{target_cell_name}"\n'
        target_ast = element_ast.ElementTransformer().visit(target_ast)
        self.code += astunparse.unparse(target_ast)
        self.root_cell = StickDiagram._StickDiagram()
        self.root_cell._DesignParameter = dict()
        self.root_cell._DesignParameter['_Name'] = StickDiagram._StickDiagram()._NameDeclaration(target_cell_name)
        self.root_cell._DesignParameter['_GDSFile'] = StickDiagram._StickDiagram()._GDSObjDeclaration()
        try:
            self.root_cell.exec_pass(self.code,generator_model_api)
        except:
            traceback.print_exc()
            warnings.warn("Invalid parameters.")
            return None

        return self.build_model_structure(target_cell_name)
        # self.root_cell._DesignParameter[target_cell_name]['_ModelStructure'] = dict()
        # _ModelStructure = self.root_cell._DesignParameter[target_cell_name]['_ModelStructure']
        # element_name_stactk = list(self.root_cell._DesignParameter[target_cell_name]['_DesignObj']._DesignParameter.keys())
        # element_stack = list(self.root_cell._DesignParameter[target_cell_name]['_DesignObj']._DesignParameter.values())
        # model_structure_stack = [_ModelStructure] * len(element_name_stactk)
        # while model_structure_stack:
        #     model_structure = model_structure_stack.pop(0)
        #     element_name = element_name_stactk.pop(0)
        #     element = element_stack.pop(0)
        #
        #     if element['_DesignParametertype'] == 4 or element['_DesignParametertype'] == 5:
        #         continue
        #     elif element['_DesignParametertype'] == 3:
        #         model_structure[element_name] = PyCodes.QTInterfaceWithAST.QtDesignParameter()
        #         model_structure[element_name]._DesignParameter = element
        #         model_structure[element_name]._DesignParameter['_ModelStructure'] = dict()
        #         model_structure[element_name]._type = 3
        #
        #         sub_element_names = list(element['_DesignObj']._DesignParameter.keys())
        #         sub_elements = list(element['_DesignObj']._DesignParameter.values())
        #         sub_model_structures = [ model_structure[element_name]._DesignParameter['_ModelStructure'] ]*len(sub_element_names)
        #         element_name_stactk.extend(sub_element_names)
        #         element_stack.extend(sub_elements)
        #         model_structure_stack.extend(sub_model_structures)
        #     else:
        #         model_structure[element_name] = PyCodes.QTInterfaceWithAST.QtDesignParameter()
        #         model_structure[element_name]._DesignParameter = element
        #         model_structure[element_name]._type = element['_DesignParametertype']
        #         if '_ElementName' not in model_structure[element_name]._DesignParameter:
        #             model_structure[element_name]._DesignParameter['_ElementName'] = element_name
        # return self.root_cell._DesignParameter[target_cell_name]

    def load_qt_id_info(self, project, constraint_ids):
        '''
        This process was required to connect designparm id to element name.
        However, design parm id and name was unified, so no more use... (Maybe)...
        '''
        self.element_manager = project._QTObj._qtProject._ElementManager
        dp_id_list = [self.element_manager.get_dp_id_by_dc_id(constraint_id) for constraint_id in constraint_ids]

        self.dp_name_to_dp_id = dict()
        for dp_id in dp_id_list:
            if dp_id == None:
                continue
            if dp_id not in project._QTObj._qtProject._DesignParameter[self.class_name]:
                # self.dp_name_to_dp_id[dp_id] = dp_id
                continue
            name = project._QTObj._qtProject._DesignParameter[self.class_name][dp_id]._ElementName
            self.dp_name_to_dp_id[name] = dp_id


    def get_updated_designParameters(self):
        self.cell_dp_dict[self.class_name] = StickDiagram._StickDiagram()
        self.root_cell = self.cell_dp_dict[self.class_name]
        self.cell_dp_dict[self.class_name]._DesignParameter = dict()
        self.cell_dp_dict[self.class_name]._DesignParameter['_Name'] = StickDiagram._StickDiagram()._NameDeclaration(
            self.class_name)
        self.cell_dp_dict[self.class_name]._DesignParameter[
            '_GDSFile'] = StickDiagram._StickDiagram()._GDSObjDeclaration()

        self.run_qt_constraint_ast()

        dp_dictionary = dict()
        for dp_name, dp  in self.root_cell._DesignParameter.items():
            if dp_name == '_Name' or dp_name == '_GDSFile':
                continue
            if dp['_DesignParametertype'] == 3:
                dp_dictionary[dp_name] = self.build_model_structure(dp_name)
                # temp = self.dp_name_to_dp_id[dp_name]
                # dp_dictionary[dp_name]['_id'] = temp
            else:
                dp_dictionary[dp_name] = dp
            # if dp_name in self.dp_name_to_dp_id:
            #     temp = self.dp_name_to_dp_id[dp_name]
            #     dp_dictionary[dp_name]['_id'] = temp
            #     dp_dictionary[dp_name]['_ElementName'] = temp
            # else:
            dp_dictionary[dp_name]['_id'] = dp_name
            dp_dictionary[dp_name]['_ElementName'] = dp_name
            print("debug")


        return dp_dictionary

    def build_model_structure(self, target_cell_name):
        self.root_cell._DesignParameter[target_cell_name]['_ModelStructure'] = dict()
        _ModelStructure = self.root_cell._DesignParameter[target_cell_name]['_ModelStructure']
        element_name_stactk = list(
            self.root_cell._DesignParameter[target_cell_name]['_DesignObj']._DesignParameter.keys())
        element_stack = list(self.root_cell._DesignParameter[target_cell_name]['_DesignObj']._DesignParameter.values())
        model_structure_stack = [_ModelStructure] * len(element_name_stactk)
        while model_structure_stack:
            model_structure = model_structure_stack.pop(0)
            element_name = element_name_stactk.pop(0)
            element = element_stack.pop(0)

            if element['_DesignParametertype'] == 4 or element['_DesignParametertype'] == 5:
                continue
            elif element['_DesignParametertype'] == 3:
                model_structure[element_name] = PyCodes.QTInterfaceWithAST.QtDesignParameter()
                model_structure[element_name]._DesignParameter = element
                model_structure[element_name]._DesignParameter['_ModelStructure'] = dict()
                model_structure[element_name]._type = 3
                model_structure[element_name]._ElementName = element_name


                sub_element_names = list(element['_DesignObj']._DesignParameter.keys())
                sub_elements = list(element['_DesignObj']._DesignParameter.values())
                sub_model_structures = [model_structure[element_name]._DesignParameter['_ModelStructure']] * len(
                    sub_element_names)
                element_name_stactk.extend(sub_element_names)
                element_stack.extend(sub_elements)
                model_structure_stack.extend(sub_model_structures)
            else:
                model_structure[element_name] = PyCodes.QTInterfaceWithAST.QtDesignParameter()
                model_structure[element_name]._DesignParameter = element
                model_structure[element_name]._type = element['_DesignParametertype']
                model_structure[element_name]._ElementName = element_name
                if '_ElementName' not in model_structure[element_name]._DesignParameter:
                    model_structure[element_name]._DesignParameter['_ElementName'] = element_name
                if model_structure[element_name]._DesignParameter['_ElementName'] is None:
                    model_structure[element_name]._DesignParameter['_ElementName'] = element_name
        return self.root_cell._DesignParameter[target_cell_name]


    def load_qt_project(self,project):
        """
        :param project:
        :return: import required libraries from library manager, load Class names,
        """
        self.class_name = project._CurrentModuleName
        #TODO library manager should be added later., library manger will add sys path and pass the class names.
        self.libraries = project.library_manager
        if 'dv' in project.__dict__:
            self.user_variables = project.dv.variableDict.values()
        else:
            from PyQTInterface import variableWindow
            self.user_variables = variableWindow._createNewDesignVariable.variableDict.values()
        print('debugPoint')

        pass


    def load_qt_design_parameters(self, QtDesignParameter, top_module):
        for structure_name, structure in QtDesignParameter.items():
            self.convert_qt_structure(structure,structure_name)
            self.cell_dp_dict[structure_name] = StickDiagram._StickDiagram()
            for qt_dp in structure:
                self.convert_qt_structure(structure,structure_name)


    def convert_qt_structure(self, structure, structure_name):
        self.cell_dp_dict[structure_name] = StickDiagram._StickDiagram()
        self.cell_dp_dict[structure_name]._DesignParameter = dict()
        self.cell_dp_dict[structure_name]._DesignParameter['_Name'] = StickDiagram._StickDiagram()._NameDeclaration(structure_name)
        self.cell_dp_dict[structure_name]._DesignParameter['_GDSFile'] = StickDiagram._StickDiagram()._GDSObjDeclaration()
        for _, qt_dp in structure.items():
            self.convert_qt_element(qt_dp, self.cell_dp_dict[structure_name])


    def convert_qt_element(self, element, structure):
        """
        :param element:
        :param structure:
        :return:
        It removes XYcoordinates because of run-time determined object. (Qdp will be implemented only in case of DesignConstraint describes)
        """
        element_name = element._ElementName
        if element._type == 3:
            structure._DesignParameter[element_name] = StickDiagram._StickDiagram()._SrefElementDeclaration(
                # _XYCoordinates=copy.deepcopy(element._DesignParameter['_XYCoordinates']),
                _XYCoordinates=[],
                _Reflect= copy.deepcopy(element._DesignParameter['_Reflect']),
                _Angle=copy.deepcopy(element._DesignParameter['_Angle']),
                _ElementName= copy.deepcopy(element._DesignParameter['_ElementName'])
            )[0]
            structure._DesignParameter[element_name]['_id'] = element._id
            structure._DesignParameter[element_name]['_DesignObj'] = StickDiagram._StickDiagram()
            structure._DesignParameter[element_name]['_DesignObj']._DesignParameter = dict(
                _Name = StickDiagram._StickDiagram()._NameDeclaration(element_name),
                _GDSFile = StickDiagram._StickDiagram()._GDSObjDeclaration()
            )
            for _,sub_qt_element in element._DesignParameter['_ModelStructure'].items():
                self.convert_qt_element(sub_qt_element, structure._DesignParameter[element_name]['_DesignObj'])
        else:
            structure._DesignParameter[element_name] = copy.deepcopy(element._DesignParameter)
            structure._DesignParameter[element_name]['_XYCoordinates'] = []

    def load_qt_design_constraints_ast(self, top_ast):
        self.code = astunparse.unparse(top_ast)

    def load_qt_design_constraints_code(self, code):
        self.code = code

    def run_qt_constraint_ast(self):
        #add libraries
        # self.root_cell.library_import(self.libraries)
        user_variable_sentence = ",".join([f'{variable_dict["DV"]}={variable_dict["value"] if variable_dict["value"] != "" else None}' for variable_dict in self.user_variables])
        fcn_define_code = 'def _CalculateDesignParameter(self,' + user_variable_sentence + '):\n\tpass'
        tmp_ast = ast.parse(fcn_define_code)
        self.code = f'_Name="{self.class_name}"\n' + self.code
        tmp_sub_ast = ast.parse(self.code)
        tmp_ast.body[0].body = tmp_sub_ast.body
        self.code = astunparse.unparse(tmp_ast)
        self.code += '\nself.root_cell._CalculateDesignParameter = types.MethodType(_CalculateDesignParameter, self.root_cell)'
        self.code = 'for name in self.libraries.class_name_dict:\n' \
                    '\tglobals()[name] = self.libraries.libraries[name]\n' + self.code
        exec(self.code,globals(),locals())

        # self.root_cell._CalculateDesignParameter = types.MethodType(_CalculateDesignParameter, self.root_cell)
        self.root_cell._CalculateDesignParameter()




        # exec(self.code)
        # self.root_cell._CalculateDesignParameter = types.MethodType(_CalculateDesignParameter, self.root_cell)
        # self.root_cell.exec_pass(self.code, self.libraries)
        # self.root_cell._CalculateDesignParameter()
        # exec(self.code)
        print('test')


    def load_qt_design_constraints(self, QtDesignConstraint):
        #모든 모듈? dictionary 여러개 받을지... 아니면 top module의 constraint만 받을지... 아니면 top ast만 받을지
        #우선은 모든 모듈에서 작동하도록 만들고, top module 하나만 있다고 가정
        self.element_parameter_dict=dict()
        for module_name, module_qt_dict in QtDesignConstraint.items():
            for id, dc in module_qt_dict.items():
                if any(list(filter(lambda constraint_type: constraint_type in dc._ast._type, ['Boundary','Path','Sref']))):
                    self.element_parameter_dict[dc._ast.name] = self.assign_parameter_to_element_by_qt_constraint(dc)


    def set_root_cell(self, cell_name):
        self.root_cell = self.cell_dp_dict[cell_name]

    def set_topcell_name(self,name):
        if self.root_cell == None:
            raise Exception("You should set root cell!")
        self.root_cell._DesignParameter['_Name']['_Name'] = name

    def get_cell_names(self):
        for key in self.cell_dp_dict:
            print(key)

    def get_element_names(self, cell_name=None):
        if cell_name == None:
            if self.root_cell == None:
                raise Exception("You should set root cell! or You should pass the cell name to get elements names.")
            for key in self.root_cell._DesignParameter:
                print(key)
        else:
            for key in self.cell_dp_dict[cell_name]._DesignParameter:
                print(key)

    def change_element_name(self, cell_name, target_name):
        if target_name in self.root_cell._DesignParameter:
            raise Exception(f'{target_name} is already exists. You cannot change cell name as {target_name}.')
        self.root_cell._DesignParameter[cell_name]['_ElementName'] = target_name
        self.root_cell._DesignParameter[target_name] = self.root_cell._DesignParameter[cell_name]
        self.element_parameter_dict[target_name] = self.element_parameter_dict[cell_name]
        del self.root_cell._DesignParameter[cell_name]
        del self.element_parameter_dict[cell_name]

        # if target_name in self.cell_dp_dict:
        #     raise Exception(f'{target_name} is already exists. You cannot change cell name as {target_name}')
        # self.cell_dp_dict[cell_name]._DesignParameter[cell_name]._ElementName = target_name
        # self.cell_dp_dict[cell_name]._DesignParameter[target_name]._ElementName = self.cell_dp_dict[cell_name]._DesignParameter[cell_name]._ElementName
        # del self.cell_dp_dict[cell_name]._DesignParameter[cell_name]._ElementName



    def ready_for_top_cell(self, cell_name=None):
        if cell_name == None:
            self.root_cell._DesignParameter['_Name'] = StickDiagram._StickDiagram()._NameDeclaration(
                'topcell')
            self.root_cell._DesignParameter['_GDSFile'] = StickDiagram._StickDiagram()._GDSObjDeclaration()
            self.root_cell._UpdateDesignParameter2GDSStructure(
                _DesignParameterInDictionary=self.root_cell._DesignParameter)
            gds_stream = self.root_cell._CreateGDSStream(
                self.root_cell._DesignParameter['_GDSFile']['_GDSFile'])
        else:
            self.cell_dp_dict[cell_name]._DesignParameter['_Name'] = StickDiagram._StickDiagram()._NameDeclaration(
                cell_name)
            self.cell_dp_dict[cell_name]._DesignParameter['_GDSFile'] = StickDiagram._StickDiagram()._GDSObjDeclaration()
            self.cell_dp_dict[cell_name]._UpdateDesignParameter2GDSStructure(
                _DesignParameterInDictionary=self.cell_dp_dict[cell_name]._DesignParameter)
            gds_stream = self.cell_dp_dict[cell_name]._CreateGDSStream(
                self.cell_dp_dict[cell_name]._DesignParameter['_GDSFile']['_GDSFile'])
        return gds_stream

    def update_designparameter_by_user_variable(self):
        if self.root_cell == None:
            raise Exception("You should set root cell!")
        for element_name, element_parameters in self.element_parameter_dict.items():

            if self.root_cell._DesignParameter[element_name]['_DesignParametertype'] == 1 \
                    or self.root_cell._DesignParameter[element_name]['_DesignParametertype'] == 2:
                for parameter_name, value in element_parameters.items():
                    self.root_cell._DesignParameter[element_name][parameter_name] = value
            elif self.root_cell._DesignParameter[element_name]['_DesignParametertype'] == 3:
                if element_parameters is None:
                    warnings.warn(f'{element_name} cell does not have element parameter values.')
                else:
                    try:
                        fcn_name = generator_model_api.find_calculate_fcn_name(self.root_cell._DesignParameter[element_name]['_DesignObj'])
                        getattr(self.root_cell._DesignParameter[element_name]['_DesignObj'], fcn_name)(**element_parameters)
                    except TypeError as error:
                        warnings.warn(f'{element_name} cell calculation has failed.')
                        traceback.print_exc()



    def load_gds(self, gds_file, generator_gds=False):
        """
        Set target gds file, and convert gds to generator format data type. And assign default value of parameter at element_parameter_dict
        :param gds_file:
        :param generator_gds:
        :return:
        """
        gds_stream_obj = gds_stream.GDS_STREAM()
        with open(gds_file, 'rb') as f:
            gds_stream_obj.read_binary_gds_stream(gds_file=f)
            for _tmpStructure in gds_stream_obj._STRUCTURES:
                self.convert_struct(_tmpStructure)
        # in case of last structure
        tmp_structure_list = list(self.cell_dp_dict.items())
        root_structure = tmp_structure_list[0] if generator_gds else tmp_structure_list[-1]
        del tmp_structure_list
        for element_name in root_structure[1]._DesignParameter:
            element = root_structure[1]._DesignParameter[element_name]
            if element_name != '_Name' and element_name != '_GDSFile':
                self.element_parameter_dict[element_name] = self.assign_parameter_to_element(element)

    def convert_struct(self, structure):
        structure_name = structure._STRNAME.strname.decode()
        if '\x00' in structure_name:
            structure_name = structure_name.split('\x00', 1)[0]
        self.cell_dp_dict[structure_name] = StickDiagram._StickDiagram()
        self.cell_dp_dict[structure_name]._DesignParameter = dict()
        self.cell_dp_dict[structure_name]._DesignParameter['_Name'] = StickDiagram._StickDiagram()._NameDeclaration(structure_name)
        self.cell_dp_dict[structure_name]._DesignParameter['_GDSFile'] = StickDiagram._StickDiagram()._GDSObjDeclaration()
        for i, element in enumerate(structure._ELEMENTS):
            self.convert_element(structure_name, element, i)


    def convert_element(self, structure_name, element, num):
        if "_BOUNDARY" in vars(element._ELEMENTS):
            element_name = self.element_name_finder(element, num)
            layer_name = LayerReader._LayerName_unified[str(element._ELEMENTS._LAYER.layer)]
            # layer_name = self.layer_num2name[element._ELEMENTS._LAYER.layer]
            # layer_name = LayerReader._LayerNumber2LayerName(element._ELEMENTS._LAYER.layer)
            xy_coordinates, x, y = self.cell_dp_dict[structure_name].XYCoordinate2CenterCoordinateAndWidth(
                element._ELEMENTS._XY.xy)
            self.cell_dp_dict[structure_name]._DesignParameter[element_name] = self.cell_dp_dict[
                structure_name]._BoundaryElementDeclaration()
            design_dict = dict(_Layer=DesignParameters._LayerMapping[layer_name][0],
                               _Datatype=DesignParameters._LayerMapping[layer_name][1],
                               _XWidth=x,
                               _YWidth=y,
                               _XYCoordinates=[xy_coordinates],
                               _ElementName=element_name, )
            self.cell_dp_dict[structure_name]._DesignParameter[element_name].update(design_dict)
        elif "_PATH" in vars(element._ELEMENTS):
            element_name = self.element_name_finder(element, num)
            layer_name = LayerReader._LayerName_unified[str(element._ELEMENTS._LAYER.layer)]
            self.cell_dp_dict[structure_name]._DesignParameter[element_name] = self.cell_dp_dict[
                structure_name]._PathElementDeclaration()
            design_dict = dict(_Layer=DesignParameters._LayerMapping[layer_name][0],
                               _Datatype=DesignParameters._LayerMapping[layer_name][1],
                               _Width=element._ELEMENTS._WIDTH.width,
                               _XYCoordinates=[element._ELEMENTS._XY.xy],
                               _ElementName=element_name, )
            self.cell_dp_dict[structure_name]._DesignParameter[element_name].update(design_dict)
        elif "_SREF" in vars(element._ELEMENTS):
            sref_structure_name = element._ELEMENTS._SNAME.sname.decode()
            if '\x00' in sref_structure_name:
                sref_structure_name = sref_structure_name.split('\x00', 1)[0]

            element_name = sref_structure_name
            if element_name in self.cell_dp_dict[structure_name]._DesignParameter:
                exists_name_list = [name for name in self.cell_dp_dict[structure_name]._DesignParameter if element_name in name]
                number_of_elements = len(exists_name_list)
                element_name = element_name + '_' + str(number_of_elements)
                if element_name in self.cell_dp_dict[structure_name]._DesignParameter:
                    raise Exception("Duplication elementname found while gds loading.")
            else:
                pass

            reflect=None
            angle=None
            if element._ELEMENTS._STRANS != None:
                if element._ELEMENTS._STRANS._STRANS != None:
                    reflect = [
                        element._ELEMENTS._STRANS._STRANS.reflection,
                        element._ELEMENTS._STRANS._STRANS.abs_mag,
                        element._ELEMENTS._STRANS._STRANS.abs_angle
                    ]
                if element._ELEMENTS._STRANS._ANGLE != None:
                    angle = element._ELEMENTS._STRANS._ANGLE.angle

            self.cell_dp_dict[structure_name]._DesignParameter[element_name] = \
            self.cell_dp_dict[structure_name]._SrefElementDeclaration()[0]
            design_dict = dict(_DesignObj=None,
                               _XYCoordinates=element._ELEMENTS._XY.xy,
                               _ElementName=element_name,
                               _Angle=angle, _Reflect = reflect
                               )
            self.cell_dp_dict[structure_name]._DesignParameter[element_name].update(design_dict)
            self.cell_dp_dict[structure_name]._DesignParameter[element_name]['_DesignObj'] = copy.deepcopy(self.cell_dp_dict[sref_structure_name])

        elif "_TEXT" in vars(element._ELEMENTS):
            pass
        # element_name =
        # self.cell_dp_dict[structure_name]._DesignParameter[]

    def element_name_finder(self, element, num):
        if '_GDS_ELEMENT_NAME' in element.__dict__:
            if element._GDS_ELEMENT_NAME != None:
                return element._GDS_ELEMENT_NAME
            else:
                # todo : assign 임의로 이름
                return f'default_name_{num}'
        else:
            # todo: assign 임의로 이름
            return f'default_name_{num}'

    def assign_generator_to_pcell_element(self,log=True):
        if not self.root_cell:
            raise Exception('There is no root cell.')
        inspector = CellInspector()
        structure_name_to_generator_name = dict()
        for structure_name, structure in self.cell_dp_dict.items():
            if structure == self.root_cell:
                continue
            generator_name = inspector.convert_pcell_name_to_generator_name(structure_name)

            if generator_name:
                structure_name_to_generator_name[structure_name] = generator_name

        for element_name, element in self.root_cell._DesignParameter.items():
            if element_name == '_Name' or element_name == '_GDSFile':
                continue
            if element['_DesignParametertype'] == 3:
                sref_structure_name = element['_DesignObj']._DesignParameter['_Name']['_Name']
                if not sref_structure_name in structure_name_to_generator_name:
                    warnings.warn(f'{sref_structure_name} reference information is no exist.')
                    continue

                self.assign_generator_to_sref_element(element_name, structure_name_to_generator_name[sref_structure_name])

    def assign_initial_value_to_pcell_generator(self,log=True):
        if not self.root_cell:
            raise Exception('There is no root cell.')
        inspector = CellInspector()
        structure_name_to_parameter_dict = dict()
        for structure_name , structure in self.cell_dp_dict.items():
            if structure == self.root_cell:
                continue
            initial_parameter = inspector.inspect(structure, structure_name)
            if initial_parameter:
                structure_name_to_parameter_dict[structure_name] = initial_parameter

        for element_name, element in self.root_cell._DesignParameter.items():
            if element_name == '_Name' or element_name == '_GDSFile':
                continue
            if element['_DesignParametertype'] == 3:
                sref_structure_name = element['_DesignObj']._DesignParameter['_Name']['_Name']
                if not sref_structure_name in structure_name_to_parameter_dict:
                    warnings.warn(f'{sref_structure_name} reference information is no exist.')
                    continue
                self.element_parameter_dict[element_name].update(structure_name_to_parameter_dict[sref_structure_name])

    def assign_generator_to_sref_element(self,element_name, generator_name):
        """
        Structure에 해당하는 StickDiagram cell의 designObj field에 generator class instance를 할당합니다.
        만약 해당 generator class에 해당하는 subcell designparameter inital value가 있는경우 해당 module에서
        _ParametersForDesignCalculation 변수를 할당해줍니다.
        :param sturcture_name:
        :param element_name:
        :param generator_name:
        :return:
        """
        # TODO: designObj assign 할 때, argument (DesignParameter, Name ) 처리하기
        # self.cell_dp_dict[sturcture_name]._DesignParameter[element_name]['_DesignObj'] = generator_model_api.class_dict[
        #     generator_name]()
        # self.cell_dp_dict[sturcture_name]._DesignParameter[element_name]['_DesignObj']._DesignParameter[
        #     '_Name'] = StickDiagram._StickDiagram()._NameDeclaration(element_name)
        # self.cell_dp_dict[sturcture_name]._DesignParameter[element_name]['_DesignObj']._DesignParameter[
        #     '_GDSFile'] = StickDiagram._StickDiagram()._GDSObjDeclaration()


        if self.root_cell is None:
            raise Exception("You should set root_cell.")

        self.root_cell._DesignParameter[element_name]['_DesignObj'] = generator_model_api.class_dict[generator_name]()
        # self.root_cell._DesignParameter[element_name]['_DesignObj']._DesignParameter['_Name'] = StickDiagram._StickDiagram()._NameDeclaration(generator_name)
        # self.root_cell._DesignParameter[element_name]['_DesignObj']._DesignParameter['_Name'] = StickDiagram._StickDiagram()._NameDeclaration(element_name)
        original_structure_name = self.get_structure_name_from_element_name(element_name)
        if original_structure_name:
            self.root_cell._DesignParameter[element_name]['_DesignObj']._DesignParameter['_Name'] = StickDiagram._StickDiagram()._NameDeclaration(original_structure_name)
        else:
            self.root_cell._DesignParameter[element_name]['_DesignObj']._DesignParameter['_Name'] = StickDiagram._StickDiagram()._NameDeclaration(generator_name)


        self.root_cell._DesignParameter[element_name]['_DesignObj']._DesignParameter['_GDSFile'] = StickDiagram._StickDiagram()._GDSObjDeclaration()
        import copy
        self.element_parameter_dict[element_name] = copy.deepcopy(self.root_cell._DesignParameter[element_name]['_DesignObj']._ParametersForDesignCalculation)


        # 여기에다가 ParametersForDesignCalculation 이름으로 찾아서 (subcell에 있는거) 잠시,,, 여기가 element내의 sref인지, structure의 sref인지 확인 필요
        # if element_name in self.cell_dp_dict: # Find Subcell information and get parameters...
        #     if '_ParametersForDesignCalculation' in self.cell_dp_dict[element_name].__dict__:
        #         self.cell_dp_dict[element_name]._ParametersForDesignCalculation
        #     else:
        #         raise Exception('_ParametersForDesignCalculation is not included in generator ')

    def assign_array_to_elements(self,element_name_list, array_element_name):
        num_of_array = len(element_name_list)
        xy = [[0,0]]
        x_space_distance = 0
        y_space_distance = 0

        if self.root_cell._DesignParameter[element_name_list[0]]['_DesignParametertype'] == 1:
            x_list = [self.root_cell._DesignParameter[element_name]['_XYCoordinates'][0][0] for element_name in element_name_list]
            y_list = [self.root_cell._DesignParameter[element_name]['_XYCoordinates'][0][1] for element_name in element_name_list]
            x_list.sort()
            y_list.sort()
            x_space_distance = x_list[1] - x_list[0]
            y_space_distance = y_list[1] - y_list[0]
            xy = [[x_list[0], y_list[0]]]
            # return dict(xy=xy, num_of_array=num_of_array, x_space_distance=x_space_distance, y_space_distance=y_space_distance)
            dict(xy=xy, num_of_array=num_of_array, x_space_distance=x_space_distance, y_space_distance=y_space_distance)

            if array_element_name in self.root_cell._DesignParameter:
                raise Exception("Already exists element name!")
            import copy
            self.root_cell._DesignParameter[array_element_name] = \
                self.root_cell._ElementArrayDeclaration(_XYCoordinates=xy,
                                                        _BaseElement=copy.deepcopy(self.root_cell._DesignParameter[element_name_list[0]]),
                                                        _NumofArray = num_of_array,
                                                        _XOffset = x_space_distance,
                                                        _YOffset = y_space_distance,
                                                        _ElementName=array_element_name)
            self.element_parameter_dict[array_element_name] = dict(_BaseElementParameter=copy.deepcopy(self.element_parameter_dict[element_name_list[0]]),
                                                                   _XYCoordinates=xy,
                                                                   _NumofArray = num_of_array,
                                                                   _XOffset = x_space_distance,
                                                                   _YOffset = y_space_distance)
            for element_name in element_name_list:
                del self.root_cell._DesignParameter[element_name]
                del self.element_parameter_dict[element_name]

        elif self.root_cell._DesignParameter[element_name_list[0]]['_DesignParametertype'] == 2:
            x_list = [self.root_cell._DesignParameter[element_name]['_XYCoordinates'][0][0][0] for element_name in element_name_list]
            y_list = [self.root_cell._DesignParameter[element_name]['_XYCoordinates'][0][0][1] for element_name in element_name_list]
            x_list.sort()
            y_list.sort()
            x_space_distance = x_list[1] - x_list[0]
            y_space_distance = y_list[1] - y_list[0]
            xy = [[x_list[0], y_list[0]]]
            # return dict(xy=xy, num_of_array=num_of_array, x_space_distance=x_space_distance, y_space_distance=y_space_distance)
            dict(xy=xy, num_of_array=num_of_array, x_space_distance=x_space_distance, y_space_distance=y_space_distance)

            if array_element_name in self.root_cell._DesignParameter:
                raise Exception("Already exists element name!")
            import copy
            self.root_cell._DesignParameter[array_element_name] = \
                self.root_cell._ElementArrayDeclaration(_XYCoordinates=xy,
                                                        _BaseElement=copy.deepcopy(self.root_cell._DesignParameter[element_name_list[0]]),
                                                        _NumofArray = num_of_array,
                                                        _XOffset = x_space_distance,
                                                        _YOffset = y_space_distance,
                                                        _ElementName=array_element_name)
            self.element_parameter_dict[array_element_name] = dict(_BaseElementParameter=copy.deepcopy(self.element_parameter_dict[element_name_list[0]]),
                                                                   _XYCoordinates=xy,
                                                                   _NumofArray = num_of_array,
                                                                   _XOffset = x_space_distance,
                                                                   _YOffset = y_space_distance)
            for element_name in element_name_list:
                del self.root_cell._DesignParameter[element_name]
                del self.element_parameter_dict[element_name]

        elif self.root_cell._DesignParameter[element_name_list[0]]['_DesignParametertype'] == 3:
            x_list = [self.root_cell._DesignParameter[element_name]['_XYCoordinates'][0][0] for element_name in element_name_list]
            y_list = [self.root_cell._DesignParameter[element_name]['_XYCoordinates'][0][1] for element_name in element_name_list]
            x_list.sort()
            y_list.sort()
            x_space_distance = x_list[1] - x_list[0]
            y_space_distance = y_list[1] - y_list[0]
            xy = [[x_list[0], y_list[0]]]
            # return dict(xy=xy, num_of_array=num_of_array, x_space_distance=x_space_distance, y_space_distance=y_space_distance)
            dict(xy=xy, num_of_array=num_of_array, x_space_distance=x_space_distance, y_space_distance=y_space_distance)

            if array_element_name in self.root_cell._DesignParameter:
                raise Exception("Already exists element name!")
            import copy
            self.root_cell._DesignParameter[array_element_name] = \
                self.root_cell._ElementArrayDeclaration(_XYCoordinates=xy,
                                                        _BaseElement=copy.deepcopy(self.root_cell._DesignParameter[element_name_list[0]]),
                                                        _NumofArray = num_of_array,
                                                        _XOffset = x_space_distance,
                                                        _YOffset = y_space_distance,
                                                        _ElementName=array_element_name)
            self.element_parameter_dict[array_element_name] = dict(_BaseElementParameter=copy.deepcopy(self.element_parameter_dict[element_name_list[0]]),
                                                                   _XYCoordinates=xy,
                                                                   _NumofArray = num_of_array,
                                                                   _XOffset = x_space_distance,
                                                                   _YOffset = y_space_distance)
            for element_name in element_name_list:
                del self.root_cell._DesignParameter[element_name]
                del self.element_parameter_dict[element_name]






    def assign_parameter_to_element(self, element):
        if element['_DesignParametertype'] == 1:
            output = dict(
                _XYCoordinates=element['_XYCoordinates'],
                _XWidth=element['_XWidth'],
                _YWidth=element['_YWidth'])
        elif element['_DesignParametertype'] == 2:
            output = dict(
                _XYCoordinates=element['_XYCoordinates'],
                _Width=element['_Width'])
        else:
            return None
        return output

    def assign_parameter_to_element_by_qt_constraint(self, qt_dc):
        if qt_dc._type == 'Boundary':
            output = dict(
                _XYCoordinates=qt_dc._ast.XY,
                _XWidth=qt_dc._ast.width,
                _YWidth=qt_dc._ast.height)
        elif qt_dc._type == 'Path':
            output = dict(
                _XYCoordinates=qt_dc._ast.XY,
                _Width=qt_dc._ast.width)
        else:
            return None
        return output
    def assign_parameter_to_sref_generator(self, structure_name, generator_name):
        if generator_name == 'PMOSWithDummy':
            tmp_parameter = CellInspector.inspect_mosfet(None, self.cell_dp_dict[structure_name])
            _ParametersForDesignCalculation = dict(
                _PMOSNumberofGate=tmp_parameter['_MOSNumberofGate'],
                _PMOSChannelWidth=tmp_parameter['_MOSChannelWidth'],
                _PMOSChannellength=tmp_parameter['_MOSChannellength'],
                _PMOSDummy=tmp_parameter['_MOSDummy'],
            )
        elif generator_name == 'NMOSWithDummy':
            tmp_parameter = CellInspector.inspect_mosfet(None, self.cell_dp_dict[structure_name])
            _ParametersForDesignCalculation = dict(
                _NMOSNumberofGate=tmp_parameter['_MOSNumberofGate'],
                _NMOSChannelWidth=tmp_parameter['_MOSChannelWidth'],
                _NMOSChannellength=tmp_parameter['_MOSChannellength'],
                _NMOSDummy=tmp_parameter['_MOSDummy'],
            )

        self.cell_dp_dict[structure_name]._ParametersForDesignCalculation = _ParametersForDesignCalculation

    def get_structure_name_from_element_name(self,element_name):
        while element_name:
            if element_name in self.cell_dp_dict:
                return element_name
            else:
                element_name = element_name[:-1]
        return None


    def user_input_based_description(self,user_parameter_dict):
        '''
        user redefine generator description based on user parameter dictionary.
        '''
        self.update_designparameter_by_user_variable()


class CellInspector:
    def __init__(self):
        pass

    def inspect(self, structure, structure_name):
        """Inspect a structure."""
        # common_name = self.convert_pcell_name_to_common_name(list(structure._DesignParameter.keys())[0])
        common_name = self.convert_pcell_name_to_common_name(structure_name)
        method = 'inspect_' + common_name
        inspector = getattr(self, method)
        return inspector(structure)

    def convert_pcell_name_to_generator_name(self, pcell_name):
        if any(list(filter(lambda pch: pch in pcell_name, ['pch','pmos','PMOS']))):
            return 'PMOSWithDummy'
        elif any(list(filter(lambda nch: nch in pcell_name, ['nch','nmos','NMOS']))):
            return 'NMOSWithDummy'
        elif any(list(filter(lambda via: via in pcell_name, ['M2_M1_']))):
            return 'ViaMet12Met2'
        elif any(list(filter(lambda via: via in pcell_name, ['M3_M2_']))):
            return 'ViaMet22Met3'
        elif any(list(filter(lambda via: via in pcell_name, ['M4_M3_']))):
            return 'ViaMet32Met4'
        elif any(list(filter(lambda via: via in pcell_name, ['M5_M4_']))):
            return 'ViaMet42Met5'
        elif any(list(filter(lambda via: via in pcell_name, ['M6_M5_']))):
            return 'ViaMet52Met6'
        elif any(list(filter(lambda via: via in pcell_name, ['M7_M6_']))):
            return 'ViaMet62Met7'
        elif any(list(filter(lambda via: via in pcell_name, ['M7_M6_']))):
            return 'ViaMet62Met7'
        elif any(list(filter(lambda via: via in pcell_name, ['M1_PO_']))):
            return 'ViaPoly2Met1'
        elif any(list(filter(lambda via: via in pcell_name, ['M1_POD']))):
            return 'PbodyContact'
        elif any(list(filter(lambda via: via in pcell_name, ['M1_NOD']))):
            return 'NbodyContact'
        else:
            return None


    def convert_pcell_name_to_common_name(self, pcell_name):
        # if 'pch' in pcell_name:
        if any(list(filter(lambda pch: pch in pcell_name, ['pch','pmos','PMOS']))):
            return 'mosfet'
        elif any(list(filter(lambda pch: pch in pcell_name, ['nch','nmos','NMOS']))):
            return 'mosfet'
        elif any(list(filter(lambda via: via in pcell_name, ['via','VIA','m1m2','M1M2','m2m3','M2M3','m3m4','M3M4','m4m5','M4M5',
                                                             'm5m6','M5M6','m6m7','M6M7','m7m8','M7M8','m8m9','M8M9',
                                                             'M2_M1','M1_PO_','M3_M2']))):
            return 'via'
        elif any(list(filter(lambda via: via in pcell_name, ['M1_POD','M1_NOD']))):
            return 'bodycontact'
        else:
            return None

    def inspect_mosfet(self, structure):
        # TODO considering.... MOSFET,,,, cutted case!!!!!!!! Not, connected......

        # mosfet parameters : _P(N)MOSNumberofGate, _P(N)MOSChannelWidth, _P(N)MOSChannellength, _P(N)MOSDummy
        poly_layer_num = LayerReader._LayerMapping['POLY'][0]
        # met1_lyaer_num = LayerReader._LayerMapping('METAL1')
        _MOSNumberofGate = 0
        for element in structure._DesignParameter:
            if element == '_Name' or element == '_GDSFile':
                continue
            if structure._DesignParameter[element]['_Layer'] is poly_layer_num:
                _MOSNumberofGate += 1
                _MOSChannelWidth = structure._DesignParameter[element]['_YWidth']
                _MOSChannellength = structure._DesignParameter[element]['_XWidth']

        if gds2generator_setting.DUMMY:
            _MOSNumberofGate -= 2
        _MOSDummy = gds2generator_setting.DUMMY

        return dict(_MOSNumberofGate=_MOSNumberofGate, _MOSChannelWidth=_MOSChannelWidth,
                    _MOSChannellength=_MOSChannellength, _MOSDummy=_MOSDummy)

    def inspect_via(self, structure):
        #find via layer
        layer_memory_dict = dict()
        for element in structure._DesignParameter:
            if element == '_Name' or element == '_GDSFile':
                continue
            if structure._DesignParameter[element]['_Layer'] in layer_memory_dict:
                via_layer = structure._DesignParameter[element]['_Layer']
                break
            else:
                layer_memory_dict[structure._DesignParameter[element]['_Layer']] = True

        via_x_list, via_y_list = [], []
        for element in structure._DesignParameter:
            if element == '_Name' or element == '_GDSFile':
                continue
            if structure._DesignParameter[element]['_Layer'] == via_layer:
                via_x_list.append(structure._DesignParameter[element]['_XYCoordinates'][0][0])
                via_y_list.append(structure._DesignParameter[element]['_XYCoordinates'][0][1])
        _NumberOfCOX = len(list(set(via_x_list)))
        _NumberOfCOY = len(list(set(via_y_list)))

        return dict(_NumberOfCOX=_NumberOfCOX, _NumberOfCOY=_NumberOfCOY)

    def inspect_bodycontact(self, structure):
        metal_layer_num = LayerReader._LayerMapping['METAL1'][0]
        contact_layer_num = LayerReader._LayerMapping['CONT'][0]

        via_x_list, via_y_list = [], []
        for element in structure._DesignParameter:
            if element == '_Name' or element == '_GDSFile':
                continue
            if structure._DesignParameter[element]['_Layer'] == metal_layer_num:
                _Met1XWidth = structure._DesignParameter[element]['_XWidth']
                _Met1YWidth = structure._DesignParameter[element]['_YWidth']
            elif structure._DesignParameter[element]['_Layer'] == contact_layer_num:
                via_x_list.append(structure._DesignParameter[element]['_XYCoordinates'][0][0])
                via_y_list.append(structure._DesignParameter[element]['_XYCoordinates'][0][1])

        _NumberOfBodyCOX = len(list(set(via_x_list)))
        _NumberOfBodyCOY = len(list(set(via_y_list)))

        return dict(_NumberOfBodyCOX=_NumberOfBodyCOX, _NumberOfBodyCOY=_NumberOfBodyCOY, _Met1XWidth=_Met1XWidth, _Met1YWidth=_Met1YWidth)

class LayoutReader:
    def __init__(self):
        self.layer_elements = dict()
        self.x_min = None
        self.y_min = None
        self.x_max = None
        self.y_max = None

    def load_qt_design_parameters(self, qt_design_parameters):
        # gds2gen = GDS2Generator()
        # gds2gen.load_qt_design_parameters(qt_design_parameters)
        geo_field = routing_geo_searching.GeometricField()
        geo_field.xy_projection_to_main_coordinates_system_qt(qt_design_parameters)
        def create_layer_element_by_dp(dp, idx):
            if dp['_DesignParametertype'] == 1:
                x_width = dp['_XWidth']
                y_width = dp['_YWidth']
                layer_name = LayerReader._LayerName_unified[str(dp['_Layer'])]
                x_min = min([xy[0] for xy in dp['_XYCoordinatesProjection'][0]])
                y_min = min([xy[1] for xy in dp['_XYCoordinatesProjection'][0]])
                lb_xy = [x_min,y_min]
                if layer_name in self.layer_elements:
                    self.layer_elements[layer_name].append(element_node(layer_name,x_width,y_width,lb_xy,idx))
                else:
                    self.layer_elements[layer_name] = []
                    self.layer_elements[layer_name].append(element_node(layer_name, x_width, y_width, lb_xy,idx))
                idx += 1

                x_max = x_min + dp['_XWidth']
                y_max = y_min + dp['_YWidth']
                self.x_min = min(self.x_min,x_min) if self.x_min else x_min
                self.y_min = min(self.y_min,y_min) if self.y_min else y_min
                self.x_max = max(self.x_max,x_max) if self.x_max else x_max
                self.y_max = max(self.y_max,y_max) if self.y_max else y_max

            elif dp['_DesignParametertype'] == 2:
                for path_xy_point in dp['_XYCoordinatesProjection'][0]:
                    x_min = min([xy[0] for xy in path_xy_point])
                    y_min = min([xy[1] for xy in path_xy_point])
                    lb_xy = [x_min, y_min]
                    x_max = max([xy[0] for xy in path_xy_point])
                    y_max = max([xy[1] for xy in path_xy_point])
                    rt_xy = [x_max, y_max]
                    x_width = x_max - x_min
                    y_width = y_max - y_min
                    layer_name = LayerReader._LayerName_unified[str(dp['_Layer'])]
                    if layer_name in self.layer_elements:
                        self.layer_elements[layer_name].append(element_node(layer_name, x_width, y_width, lb_xy, idx))
                    else:
                        self.layer_elements[layer_name] = []
                        self.layer_elements[layer_name].append(element_node(layer_name, x_width, y_width, lb_xy, idx))
                    idx += 1
                    self.x_min = min(self.x_min, x_min) if self.x_min else x_min
                    self.y_min = min(self.y_min, y_min) if self.y_min else y_min
                    self.x_max = max(self.x_max, x_max) if self.x_max else x_max
                    self.y_max = max(self.y_max, y_max) if self.y_max else y_max
            elif dp['_DesignParametertype'] == 3:
                for sub_dp in dp['_DesignObj']._DesignParameter.values():
                    idx = create_layer_element_by_dp(sub_dp,idx)
            return idx

        idx = 0
        for dp in qt_design_parameters._DesignParameter.values():
            create_layer_element_by_dp(dp, idx)


    def load_gds(self, gds_file, root_cell_name):
        gds2gen = GDS2Generator()
        gds2gen.load_gds(gds_file)
        gds2gen.set_root_cell(root_cell_name)
        geo_field = routing_geo_searching.GeometricField()
        geo_field.xy_projection_to_main_coordinates_system(gds2gen.root_cell._DesignParameter)
        def create_layer_element_by_dp(dp, idx):
            if dp['_DesignParametertype'] == 1:
                x_width = dp['_XWidth']
                y_width = dp['_YWidth']
                layer_name = LayerReader._LayerName_unified[str(dp['_Layer'])]
                x_min = min([xy[0] for xy in dp['_XYCoordinatesProjection'][0]])
                y_min = min([xy[1] for xy in dp['_XYCoordinatesProjection'][0]])
                lb_xy = [x_min,y_min]
                if layer_name in self.layer_elements:
                    self.layer_elements[layer_name].append(element_node(layer_name,x_width,y_width,lb_xy,idx))
                else:
                    self.layer_elements[layer_name] = []
                    self.layer_elements[layer_name].append(element_node(layer_name, x_width, y_width, lb_xy,idx))
                idx += 1

                x_max = x_min + dp['_XWidth']
                y_max = y_min + dp['_YWidth']
                self.x_min = min(self.x_min,x_min) if self.x_min else x_min
                self.y_min = min(self.y_min,y_min) if self.y_min else y_min
                self.x_max = max(self.x_max,x_max) if self.x_max else x_max
                self.y_max = max(self.y_max,y_max) if self.y_max else y_max

            elif dp['_DesignParametertype'] == 2:
                for path_xy_point in dp['_XYCoordinatesProjection'][0]:
                    x_min = min([xy[0] for xy in path_xy_point])
                    y_min = min([xy[1] for xy in path_xy_point])
                    lb_xy = [x_min, y_min]
                    x_max = max([xy[0] for xy in path_xy_point])
                    y_max = max([xy[1] for xy in path_xy_point])
                    rt_xy = [x_max, y_max]
                    x_width = x_max - x_min
                    y_width = y_max - y_min
                    layer_name = LayerReader._LayerName_unified[str(dp['_Layer'])]
                    if layer_name in self.layer_elements:
                        self.layer_elements[layer_name].append(element_node(layer_name, x_width, y_width, lb_xy, idx))
                    else:
                        self.layer_elements[layer_name] = []
                        self.layer_elements[layer_name].append(element_node(layer_name, x_width, y_width, lb_xy, idx))
                    idx += 1
                    self.x_min = min(self.x_min, x_min) if self.x_min else x_min
                    self.y_min = min(self.y_min, y_min) if self.y_min else y_min
                    self.x_max = max(self.x_max, x_max) if self.x_max else x_max
                    self.y_max = max(self.y_max, y_max) if self.y_max else y_max
            elif dp['_DesignParametertype'] == 3:
                for sub_dp in dp['_DesignObj']._DesignParameter.values():
                    idx = create_layer_element_by_dp(sub_dp,idx)
            return idx

        idx = 0
        for dp in gds2gen.root_cell._DesignParameter.values():
            create_layer_element_by_dp(dp, idx)

    def __len__(self):
        length = 0
        for elements_list in self.layer_elements.values():
            length += len(elements_list)
        return length



class element_node:
    def __init__(self,layer_name,x_width,y_width,lb_xy, idx):
        self.layer_name = layer_name
        self.x_width = x_width
        self.y_width = y_width
        self.lb_xy = lb_xy
        self.idx = idx

if __name__ == '__main__':
    # gds2gen = GDS2Generator()
    # gds2gen.load_gds('./Data/test_gds/test.gds')
    # gds2gen.load_gds('./INV2.gds')
    # gds2gen.load_gds('./ic616.gds',generator_gds=False)
    # gds2gen.load_gds('./Data/test_gds/netname.gds')
    # gds2gen.assign_generator_to_sref_element('test', 'nch_CDNS_614921977861', 'NMOSWithDummy')
    # del gds2gen.cell_dp_dict['test']._DesignParameter['pch_CDNS_614921977860']
    # CellInspector.inspect(CellInspector(), gds2gen.cell_dp_dict['nch_CDNS_614921977861'], 'nch_CDNS_614921977861')
    # gds2gen.cell_dp_dict['test']._DesignParameter['nch_CDNS_614921977861']['_DesignObj']._CalculateNMOSDesignParameter(
    #     **dict(_NMOSNumberofGate=3, _NMOSChannelWidth=300, _NMOSChannellength=70))
    # gds2gen.update_designparameter_by_user_variable('test')
    # gds2gen.cell_dp_dict['test']._DesignParameter['nch_CDNS_614921977861']['_ElementName'] = 'genNMOS'
    # stream_data = gds2gen.ready_for_top_cell('test')
    # file = open('./generator_made_with_default_name.gds', 'wb')
    # stream_data.write_binary_gds_stream(file)
    # file.close()
    xy_debug = False
    if xy_debug:
        xy_gen = GDS2Generator()
        xy_gen.load_gds('./xy.gds')
        gf = routing_geo_searching.GeometricField()
        gf.xy_projection_to_main_coordinates_system(xy_gen.cell_dp_dict['xy_test_2']._DesignParameter)


    load_inv_and_make_generator = True
    if load_inv_and_make_generator:
        inv_gen = GDS2Generator()
        inv_gen.load_gds('./INV2.gds')
        inv_gen.get_cell_names()
        inv_gen.set_root_cell('INV')
        inv_gen.get_element_names()
        #### assign generator to pcell element of root structure,, automatically. ####
        inv_gen.assign_generator_to_pcell_element()
        # if pcell to generator conversion fail... or there is custom generator...
        # You can use 'assign_generator_to_sref_element' fcn.
        inv_gen.assign_initial_value_to_pcell_generator()
        #### inspect pcell generator default design  ####
        inv_gen.update_designparameter_by_user_variable()




        #Assign new element name.
        inv_gen.change_element_name('M2_M1_CDNS_572756093850', 'via_M1M2_onNMOS')
        inv_gen.change_element_name('M2_M1_CDNS_572756093850_1', 'via_M1M2_onNMOS_1')
        inv_gen.change_element_name('M2_M1_CDNS_572756093850_2', 'via_M1M2_onNMOS_2')
        inv_gen.change_element_name('M1_NOD_CDNS_572756093851', 'body_M1NOD')
        inv_gen.change_element_name('M2_M1_CDNS_572756093852', 'via_M1M2_onPMOS')
        inv_gen.change_element_name('M2_M1_CDNS_572756093852_1', 'via_M1M2_onPMOS_1')
        inv_gen.change_element_name('M2_M1_CDNS_572756093852_2', 'via_M1M2_onPMOS_2')
        inv_gen.change_element_name('M1_PO_CDNS_572756093853', 'via_M1PO')
        inv_gen.change_element_name('M1_POD_CDNS_572756093854', 'body_M1POD')

        # inv_gen.assign_generator_to_sref_element('via_M1M2_1','ViaMet12Met2')
        # inv_gen.assign_generator_to_sref_element('via_M1M2_2','ViaMet12Met2')
        # inv_gen.assign_generator_to_sref_element('body_M1NOD','NbodyContact')
        # inv_gen.assign_generator_to_sref_element('body_M1POD','PbodyContact')
        # inv_gen.assign_generator_to_sref_element('via_M1PO','ViaPoly2Met1')
        # inv_gen.assign_generator_to_sref_element('NMOSInINV','NMOSWithDummy')
        # inv_gen.assign_generator_to_sref_element('PMOSInINV','PMOSWithDummy')

        # nmos_parm = CellInspector.inspect(CellInspector(), inv_gen.cell_dp_dict['NMOSInINV'], 'NMOSInINV')
        # pmos_parm = CellInspector.inspect(CellInspector(), inv_gen.cell_dp_dict['PMOSInINV'], 'PMOSInINV')
        # viam1m2parm1 = CellInspector.inspect(CellInspector(), inv_gen.cell_dp_dict['M2_M1_CDNS_572756093850'], 'M2_M1_CDNS_572756093850')
        # viam1m2parm2 = CellInspector.inspect(CellInspector(), inv_gen.cell_dp_dict['M2_M1_CDNS_572756093852'], 'M2_M1_CDNS_572756093852')
        # viapolyparm = CellInspector.inspect(CellInspector(), inv_gen.cell_dp_dict['M1_PO_CDNS_572756093853'], 'M1_PO_CDNS_572756093853')
        # nbody_parm = CellInspector.inspect(CellInspector(), inv_gen.cell_dp_dict['M1_NOD_CDNS_572756093851'], 'M1_NOD_CDNS_572756093851')
        # pbody_parm = CellInspector.inspect(CellInspector(), inv_gen.cell_dp_dict['M1_POD_CDNS_572756093854'], 'M1_POD_CDNS_572756093854')


        #
        # inv_gen.element_parameter_dict['NMOSInINV'].update(nmos_parm)
        # inv_gen.element_parameter_dict['PMOSInINV'].update(pmos_parm)
        # inv_gen.element_parameter_dict['via_M1M2_onNMOS'].update(viam1m2parm1)
        # inv_gen.element_parameter_dict['via_M1M2_onNMOS_1'].update(viam1m2parm1)
        # inv_gen.element_parameter_dict['via_M1M2_onNMOS_2'].update(viam1m2parm1)
        # inv_gen.element_parameter_dict['via_M1M2_onPMOS'].update(viam1m2parm2)
        # inv_gen.element_parameter_dict['via_M1M2_onPMOS_1'].update(viam1m2parm2)
        # inv_gen.element_parameter_dict['via_M1M2_onPMOS_2'].update(viam1m2parm2)
        # inv_gen.element_parameter_dict['via_M1PO'].update(viapolyparm)
        # inv_gen.element_parameter_dict['body_M1NOD'].update(nbody_parm)
        # inv_gen.element_parameter_dict['body_M1POD'].update(pbody_parm)
        cluster_model = clustering.determinstic_clustering(inv_gen.root_cell._DesignParameter)
        cluster_model.layer_matching()
        cluster_model.build_layer_ist()
        cluster_model.intersection_matching_path()
        # cluster_model.sref_matching()
        cluster_model.delete_solo_element_group()
        groups_list = cluster_model.get_array_groups()
        groups_list2 = cluster_model.get_routing_groups()

        # print(groups_list[0])
        # #output: ['default_name_0', 'default_name_1', 'default_name_2']
        # #grouping array element 만들고, assign 해보기~.~
        # groups_list[1].pop(3)
        # for i, group_list in enumerate(groups_list):
        #     inv_gen.assign_array_to_elements(group_list,'array_ele'+str(i))

        print(groups_list2)


        # User design parameter
        # def user_input_based_description(**user_input):
        #     inv_gen.element_parameter_dict['NMOSInINV']['_MOSNumberofGate'] = \
        #         inv_gen.element_parameter_dict['PMOSInINV']['_MOSNumberofGate'] = \
        #         user_input['NumOfFinger']
        #     inv_gen.element_parameter_dict['NMOSInINV']['_MOSDummy'] = \
        #         inv_gen.element_parameter_dict['PMOSInINV']['_MOSDummy'] = \
        #         user_input['Dummy']
        #     inv_gen.element_parameter_dict['NMOSInINV']['_MOSChannelWidth'] = \
        #         user_input['NMOS_width']
        #     inv_gen.element_parameter_dict['PMOSInINV']['_MOSChannelWidth'] = \
        #         user_input['NMOS_width'] * user_input['PI_ratio']



        inv_gen.update_designparameter_by_user_variable()






        stream_data = inv_gen.ready_for_top_cell()
        inv_gen.set_topcell_name('INV')
        file = open('./inv_gengen.gds', 'wb')
        stream_data.write_binary_gds_stream(file)
        file.close()