from generatorLib import DRC
from generatorLib.generator_models import NbodyContact
from generatorLib.generator_models import PbodyContact
from generatorLib.generator_models import PMOSWithGate
from generatorLib.generator_models import NMOSWithGate
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import ViaMet12Met2

from generatorLib import StickDiagram
from generatorLib import DesignParameters

import copy, math, warnings
from generatorLib.generator_models import MS_utility as utility


class MOSCAP_ON(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(channel_length=None, dummy=None, PCCrit=None, XVT=None,
                                           finger_on=None, channel_width1=None,
                                           finger2=None, channel_width2=None,
                                           channel_width3=None,
                                           finger4=None, channel_width4=None,

                                           supply_num_coy=None, supply_num_cox=None,
                                           distance_to_vdd=None, distance_to_vss=None,
                                           space_bw_gate_nmos=None, space_bw_gate_pmos=None,
                                           gap_bw_mos_gates=None
                                           )
    """
    finger_on : finger for one pmos and one nmos whose inputs are selb, sel respectively.
    Constraints : finger_on should not be separated, finger number should be odd
    """

    def __init__(self, _DesignParameter=None, _Name='MS_moscap_on'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter(self,
                                  channel_length=None, dummy=None, PCCrit=None, XVT=None,
                                  finger_on = None, channel_width1=None,
                                  finger2=None, channel_width2=None,
                                  channel_width3=None,
                                  finger4=None, channel_width4=None,
                                  gap_bw_mos_gates=None,
                                  supply_num_coy=None, supply_num_cox=None,
                                  distance_to_vdd=None, distance_to_vss=None, space_bw_gate_nmos=None,
                                  space_bw_gate_pmos=None
                                  ):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        _MinSnapSpacing = drc._MinSnapSpacing

        if finger_on % 2 == 0:
            finger_on = finger_on + 1
        """
        MOSFET Generation & Coordinate Settings
        """

        nmos1_inputs = copy.deepcopy(NMOSWithGate._NMOS._ParametersForDesignCalculation)
        nmos1_inputs['finger'] = finger_on
        nmos1_inputs['channel_width'] = channel_width3
        nmos1_inputs['channel_length'] = channel_length
        nmos1_inputs['dummy'] = dummy
        nmos1_inputs['PCCrit'] = PCCrit
        nmos1_inputs['XVT'] = XVT
        nmos1_inputs['enclosure_option'] = 'X'
        if space_bw_gate_nmos != None:
            nmos1_inputs['space_bw_gate_nmos'] = space_bw_gate_nmos

        nmos2_inputs = copy.deepcopy(NMOSWithGate._NMOS._ParametersForDesignCalculation)
        nmos2_inputs['finger'] = finger4
        nmos2_inputs['channel_width'] = channel_width4
        nmos2_inputs['channel_length'] = channel_length
        nmos2_inputs['dummy'] = dummy
        nmos2_inputs['PCCrit'] = PCCrit
        nmos2_inputs['XVT'] = XVT

        if space_bw_gate_nmos != None:
            nmos2_inputs['space_bw_gate_nmos'] = space_bw_gate_nmos
        # if finger4 == 1:
            # nmos2_inputs['gate_option'] = 'rotate'
        pmos1_inputs = copy.deepcopy(PMOSWithGate._PMOS._ParametersForDesignCalculation)
        pmos1_inputs['finger'] = finger_on
        pmos1_inputs['channel_width'] = channel_width1
        pmos1_inputs['channel_length'] = channel_length
        pmos1_inputs['dummy'] = dummy
        pmos1_inputs['PCCrit'] = PCCrit
        pmos1_inputs['XVT'] = XVT
        pmos1_inputs['enclosure_option'] = 'X'
        if space_bw_gate_pmos != None:
            pmos1_inputs['space_bw_gate_pmos'] = space_bw_gate_pmos
        if finger_on == 1:
            nmos1_inputs['gate_option'] = 'rotate'
            pmos1_inputs['gate_option'] = 'rotate'

        pmos2_inputs = copy.deepcopy(PMOSWithGate._PMOS._ParametersForDesignCalculation)
        pmos2_inputs['finger'] = finger2
        pmos2_inputs['channel_width'] = channel_width2
        pmos2_inputs['channel_length'] = channel_length
        pmos2_inputs['dummy'] = dummy
        pmos2_inputs['PCCrit'] = PCCrit
        pmos2_inputs['XVT'] = XVT
        if space_bw_gate_pmos != None:
            pmos2_inputs['space_bw_gate_pmos'] = space_bw_gate_pmos
        # if finger2 == 1:
        #     pmos2_inputs['gate_option'] = 'rotate'

        self._DesignParameter['nmos1'] = \
        self._SrefElementDeclaration(_DesignObj=NMOSWithGate._NMOS(_DesignParameter=None,
                                                                   _Name='nmos1_in_{}'.format(_Name)))[0]
        self._DesignParameter['nmos2'] = \
        self._SrefElementDeclaration(_DesignObj=NMOSWithGate._NMOS(_DesignParameter=None,
                                                                   _Name='nmos2_in_{}'.format(_Name)))[0]
        self._DesignParameter['pmos1'] = \
        self._SrefElementDeclaration(_DesignObj=PMOSWithGate._PMOS(_DesignParameter=None,
                                                                   _Name='pmos1_in_{}'.format(_Name)))[0]
        self._DesignParameter['pmos2'] = \
        self._SrefElementDeclaration(_DesignObj=PMOSWithGate._PMOS(_DesignParameter=None,
                                                                   _Name='pmos2_in_{}'.format(_Name)))[0]

        self._DesignParameter['nmos1']['_DesignObj']._CalculateDesignParameter(**nmos1_inputs)
        self._DesignParameter['nmos2']['_DesignObj']._CalculateDesignParameter(**nmos2_inputs)

        self._DesignParameter['pmos1']['_DesignObj']._CalculateDesignParameter(**pmos1_inputs)
        self._DesignParameter['pmos2']['_DesignObj']._CalculateDesignParameter(**pmos2_inputs)

        self._DesignParameter['nmos1']['_XYCoordinates'] = [[0, 0]]  # tmp value
        self._DesignParameter['nmos2']['_XYCoordinates'] = [[0, 0]]  # tmp value
        self._DesignParameter['pmos1']['_XYCoordinates'] = [[0, 0]]  # tmp value
        self._DesignParameter['pmos2']['_XYCoordinates'] = [[0, 0]]  # tmp value

        nmos1_x_value = self.FloorMinSnapSpacing( \
            0 - (drc._PolygateMinSpace / 2) - self.getXY('nmos1', 'nmos', '_PODummyLayer')[-1][0] - channel_length / 2,
            _MinSnapSpacing)
        nmos2_x_value = self.CeilMinSnapSpacing( \
            0 + (drc._PolygateMinSpace / 2) + self.getXY('nmos2', 'nmos', '_PODummyLayer')[-1][0] + channel_length / 2,
            _MinSnapSpacing)
        pmos1_x_value = self.FloorMinSnapSpacing( \
            0 - (drc._PolygateMinSpace / 2) - self.getXY('pmos1', 'pmos', '_PODummyLayer')[-1][0] - channel_length / 2,
            _MinSnapSpacing)
        pmos2_x_value = self.CeilMinSnapSpacing( \
            0 + (drc._PolygateMinSpace / 2) + self.getXY('pmos2', 'pmos', '_PODummyLayer')[-1][0] + channel_length / 2, \
            _MinSnapSpacing)

        leftside_x_value = min(nmos1_x_value, pmos1_x_value)
        rightside_x_value = max(nmos2_x_value, pmos2_x_value)

        calibration = min(rightside_x_value - leftside_x_value - self.getXY('nmos2', 'nmos', '_PODummyLayer')[-1][0] - \
                          self.getXY('nmos1', 'nmos', '_PODummyLayer')[-1][0],
                          rightside_x_value - leftside_x_value - self.getXY('pmos2', 'pmos', '_PODummyLayer')[-1][0] - \
                          self.getXY('pmos1', 'pmos', '_PODummyLayer')[-1][0])

        calibration = calibration - drc._PolygateMinSpace - channel_length
        leftside_x_value = self.FloorMinSnapSpacing(leftside_x_value + calibration / 2, _MinSnapSpacing)
        rightside_x_value = self.CeilMinSnapSpacing(rightside_x_value - calibration / 2, _MinSnapSpacing)
        if (pmos2_inputs['gate_option'] == 'rotate') or (pmos2_inputs['gate_option'] == 'rotate'):
            if (pmos2_inputs['gate_option'] == 'rotate'):
                gap_bw_mos_gates_min = 2 * drc._MetalxMinSpace + 3 * self.getXWidth('pmos2', 'pmos_gate_via',
                                                                                    '_Met1Layer')
            else:
                gap_bw_mos_gates_min = 2 * drc._MetalxMinSpace + 3 * self.getXWidth('nmos2', 'pmos_gate_via',
                                                                                    '_Met1Layer')

        else:
            gap_bw_mos_gates_min = 2 * drc._Metal1MinSpace + 3 * max(
                self.getYWidth('nmos2', 'nmos_gate_via', '_Met1Layer'),
                self.getYWidth('pmos2', 'pmos_gate_via', '_Met1Layer'))


        if gap_bw_mos_gates == None:
            gap_bw_mos_gates = gap_bw_mos_gates_min
        else:
            if gap_bw_mos_gates < gap_bw_mos_gates_min:
                warnings.warn(f"gap_bw_mos_gates minimum value is {gap_bw_mos_gates_min}")
                gap_bw_mos_gates = gap_bw_mos_gates_min
            else:
                pass

        nmos1_y_value = self.FloorMinSnapSpacing(0 - gap_bw_mos_gates / 2 - \
                                                 self._DesignParameter['nmos1']['_DesignObj'].offset_value,
                                                 _MinSnapSpacing)
        nmos2_y_value = self.FloorMinSnapSpacing(0 - gap_bw_mos_gates / 2 - \
                                                 self._DesignParameter['nmos2']['_DesignObj'].offset_value,
                                                 _MinSnapSpacing)
        pmos1_y_value = self.CeilMinSnapSpacing(0 + gap_bw_mos_gates / 2 + \
                                                self._DesignParameter['pmos1']['_DesignObj'].offset_value,
                                                _MinSnapSpacing)
        pmos2_y_value = self.CeilMinSnapSpacing(0 + gap_bw_mos_gates / 2 + \
                                                self._DesignParameter['pmos2']['_DesignObj'].offset_value,
                                                _MinSnapSpacing)

        self._DesignParameter['nmos1']['_XYCoordinates'] = [[leftside_x_value, nmos1_y_value]]
        self._DesignParameter['nmos2']['_XYCoordinates'] = [[rightside_x_value, nmos2_y_value]]
        self._DesignParameter['pmos1']['_XYCoordinates'] = [[leftside_x_value, pmos1_y_value]]
        self._DesignParameter['pmos2']['_XYCoordinates'] = [[rightside_x_value, pmos2_y_value]]


        """
        Output via generation & Coordinate Settings
        """
        if finger_on != 1:

            via_code_pmos1_output = utility.functions.create_output_via(self, _Name=_Name,
                                                                        via_name='pmos1_output_via',
                                                                        hierarchy_list=['pmos1', 'pmos'],
                                                                        mos_type='pmos',
                                                                        calibre_option='down')
            via_code_nmos1_output = utility.functions.create_output_via(self, _Name=_Name,
                                                                        via_name='nmos1_output_via',
                                                                        hierarchy_list=['nmos1', 'nmos'],
                                                                        mos_type='nmos',
                                                                        calibre_option='up')
            exec(via_code_pmos1_output)
            exec(via_code_nmos1_output)
        else:
            pass

        gap_checker2 = self.getXY('pmos2', 'pmos_gate_via', '_Met1Layer')[0][1] - \
                       self.getXY('nmos2', 'nmos_gate_via', '_Met1Layer')[0][1]

        cnt = 1
        while (1):
            if finger_on != 1:
                cnt = cnt + 1
                drc_test2 = self.getXYBot('nmos1', 'nmos_gate_via', '_Met1Layer')[0][1] - \
                            self.getXYTop('nmos1_output_via', '_Met1Layer')[0][1]
                if drc_test2 < drc._Metal1MinSpace2:
                    calibre_value = drc._Metal1MinSpace2 - drc_test2
                    del self._DesignParameter['nmos1_output_via']
                    calibre_for_input = self.CeilMinSnapSpacing( \
                        self._DesignParameter['nmos1']['_DesignObj'].offset_value - drc._Metal1MinSpace2 + \
                        calibre_value - (self.getYWidth('nmos1', 'nmos', '_Met1Layer') / 2 + self.getYWidth('nmos1',
                                                                                                            'nmos_gate_via',
                                                                                                            '_Met1Layer') / 2),
                        _MinSnapSpacing)
                    nmos1_inputs['space_bw_gate_nmos'] = calibre_for_input
                    nmos2_inputs['space_bw_gate_nmos'] = calibre_for_input
                    self._DesignParameter['nmos1']['_DesignObj']._CalculateDesignParameter(**nmos1_inputs)
                    self._DesignParameter['nmos2']['_DesignObj']._CalculateDesignParameter(**nmos2_inputs)
                    nmos1_y_value = self.FloorMinSnapSpacing(0 - gap_bw_mos_gates / 2 - \
                                                             self._DesignParameter['nmos1']['_DesignObj'].offset_value,
                                                             _MinSnapSpacing)
                    nmos2_y_value = self.FloorMinSnapSpacing(0 - gap_bw_mos_gates / 2 - \
                                                             self._DesignParameter['nmos2']['_DesignObj'].offset_value,
                                                             _MinSnapSpacing)
                    self._DesignParameter['nmos1']['_XYCoordinates'] = [[leftside_x_value, nmos1_y_value]]
                    self._DesignParameter['nmos2']['_XYCoordinates'] = [[rightside_x_value, nmos2_y_value]]
                    via_code_nmos1_output = utility.functions.create_output_via(self, _Name=_Name,
                                                                                via_name='nmos1_output_via',
                                                                                hierarchy_list=['nmos1', 'nmos'],
                                                                                mos_type='nmos',
                                                                                calibre_option='up')
                    exec(via_code_nmos1_output)
                else:
                    break
                if cnt > 3:
                    raise Exception("drc_calibration failed")
                    break
            else:
                break
        """
        Output via Routing
        """
        if finger_on != 1:
            routing_code_nmos1_output = utility.functions.create_output_routing(self, path_name='nmos1_output_routing',
                                                                                via_name='nmos1_output_via',
                                                                                width=None,
                                                                                routing_option='above')
            routing_code_pmos1_output = utility.functions.create_output_routing(self, path_name='pmos1_output_routing',
                                                                                via_name='pmos1_output_via',
                                                                                width=None,
                                                                                routing_option='below')
            exec(routing_code_pmos1_output + routing_code_nmos1_output)

        """
        Supply Via Generation & Routing for pmos1, nmos1
        """
        if finger_on == 1:
            via_code_pmos1_supply = utility.functions.create_output_via(self, _Name=_Name,
                                                                        via_name='pmos1_supply_via',
                                                                        hierarchy_list=['pmos1', 'pmos'],
                                                                        mos_type='pmos',
                                                                        supply_flag=True)

            via_code_nmos1_supply = utility.functions.create_output_via(self, _Name=_Name,
                                                                        via_name='nmos1_supply_via',
                                                                        hierarchy_list=['nmos1', 'nmos'],
                                                                        mos_type='nmos',
                                                                        supply_flag=True)
        else:

            via_code_pmos1_supply = utility.functions.create_output_via(self, _Name=_Name,
                                                                        via_name='pmos1_supply_via',
                                                                        hierarchy_list=['pmos1', 'pmos'],
                                                                        mos_type='pmos', calibre_option='up',
                                                                        supply_flag=True)

            via_code_nmos1_supply = utility.functions.create_output_via(self, _Name=_Name,
                                                                        via_name='nmos1_supply_via',
                                                                        hierarchy_list=['nmos1', 'nmos'],
                                                                        mos_type='nmos', calibre_option='down',
                                                                        supply_flag=True)

        exec(via_code_pmos1_supply + via_code_nmos1_supply)
        if finger_on != 1:
            routing_code_pmos1_supply = utility.functions.create_output_routing(self, path_name='pmos1_supply_routing',
                                                                                via_name='pmos1_supply_via',
                                                                                width=None,
                                                                                routing_option='above')
            routing_code_nmos1_supply = utility.functions.create_output_routing(self, path_name='nmos1_supply_routing',
                                                                                via_name='nmos1_supply_via',
                                                                                width=None,
                                                                                routing_option='below')

            exec(routing_code_pmos1_supply + routing_code_nmos1_supply)

        """
        Input Routing
        """
        self._DesignParameter['input_routing'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _Width=drc._MetalxMinWidth)
        tmp1 = self.getXY('pmos1_supply_via', '_Met2Layer')[0][0]
        tmp2 = self.getXY('nmos1_supply_via', '_Met2Layer')[0][0]
        if tmp1 != tmp2:
            raise Exception("Finger different")
        x_value = tmp1
        source_y = self._DesignParameter['pmos1_supply_via']['_XYCoordinates'][0][1]
        target_y = self._DesignParameter['nmos1_supply_via']['_XYCoordinates'][0][1]
        output_path = [[x_value, target_y], [x_value, source_y]]
        self._DesignParameter['input_routing']['_XYCoordinates'] = [output_path]


        """
        Output Routing
        """
        if finger_on != 1:
            self._DesignParameter['output_routing'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _Width=drc._Metal1MinWidth)
            tmp1 = self.getXY('pmos1_output_via', '_Met2Layer')[-1][0]
            tmp2 = self.getXY('nmos1_output_via', '_Met2Layer')[-1][0]

            x_value = min(tmp1, tmp2)
            source_y = self._DesignParameter['pmos1_output_via']['_XYCoordinates'][-1][1]
            target_y = self._DesignParameter['nmos1_output_via']['_XYCoordinates'][-1][1]
            output_path = [[tmp1, source_y], [x_value, source_y], [x_value, target_y], [tmp2, target_y]]
            self._DesignParameter['output_routing']['_XYCoordinates'] = [output_path]
            x_value_for_output = x_value
        else:
            x_common = self.getXYRight('pmos1', 'pmos_gate_via', '_Met1Layer')[0][0] + drc._Metal1MinSpace2 + \
                       drc._Metal1MinWidth / 2
            y_source = self.getXYTop('pmos1', 'pmos', '_Met1Layer')[-1][1]
            y_target = self.getXYBot('nmos1', 'nmos', '_Met1Layer')[-1][1]
            self._DesignParameter['output_routing_vertical'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _Width=drc._Metal1MinWidth)
            self._DesignParameter['output_routing_vertical']['_XYCoordinates'] = [[[x_common, y_source], [x_common, y_target]]]

            self._DesignParameter['output_routing_horizontal1'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1])
            x_center = (self.getXYRight('nmos1','nmos','_Met1Layer')[-1][0] + x_common) / 2
            np_width = x_common - self.getXYRight('nmos1','nmos','_Met1Layer')[-1][0]
            y_center = self.getXY('nmos1','nmos','_Met1Layer')[-1][1]
            n_height = self.getYWidth('nmos1','nmos','_Met1Layer')
            self._DesignParameter['output_routing_horizontal1']['_XYCoordinates'] = [[x_center, y_center]]
            self._DesignParameter['output_routing_horizontal1']['_XWidth'] = np_width
            self._DesignParameter['output_routing_horizontal1']['_YWidth'] = n_height

            self._DesignParameter['output_routing_horizontal2'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1])
            y_center = self.getXY('pmos1','pmos','_Met1Layer')[-1][1]
            p_height = self.getYWidth('pmos1','pmos','_Met1Layer')
            self._DesignParameter['output_routing_horizontal2']['_XYCoordinates'] = [[x_center, y_center]]
            self._DesignParameter['output_routing_horizontal2']['_XWidth'] = np_width
            self._DesignParameter['output_routing_horizontal2']['_YWidth'] = p_height

            x_value_for_output = x_common

        """
        Supply Rail Generation
        """
        self._DesignParameter['vss'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(
            _DesignParameter=None, _Name='vss_in_{}'.format(_Name)))[0]
        self._DesignParameter['vdd'] = self._SrefElementDeclaration(_DesignObj=NbodyContact._NbodyContact(
            _DesignParameter=None, _Name='vdd_in_{}'.format(_Name)))[0]

        vss_inputs = copy.deepcopy(PbodyContact._PbodyContact._ParametersForDesignCalculation)
        vdd_inputs = copy.deepcopy(NbodyContact._NbodyContact._ParametersForDesignCalculation)

        if (supply_num_coy != None):
            vss_inputs['_NumberOfPbodyCOY'] = supply_num_coy
            vdd_inputs['_NumberOfNbodyCOY'] = supply_num_coy
        else:
            vss_inputs['_NumberOfPbodyCOY'] = 2
            vdd_inputs['_NumberOfNbodyCOY'] = 2

        # num_cox minimum value calculation

        tmp_num_for_supply = 1  # Final COX Value
        rightmost_edge = max(self.getXY('pmos2', 'pmos', '_PODummyLayer')[-1][0],
                             self.getXY('nmos2', 'nmos', '_PODummyLayer')[-1][0])
        leftmost_edge = min(self.getXY('pmos1', 'pmos', '_PODummyLayer')[0][0],
                            self.getXY('nmos1', 'nmos', '_PODummyLayer')[0][0])

        cell_width = rightmost_edge - leftmost_edge
        rail_x_center = self.CeilMinSnapSpacing((rightmost_edge + leftmost_edge) / 2, _MinSnapSpacing)
        while (1):
            vss_inputs['_NumberOfPbodyCOX'] = tmp_num_for_supply
            self._DesignParameter['vss']['_DesignObj']._CalculatePbodyContactDesignParameter(**vss_inputs)
            if self._DesignParameter['vss']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] < cell_width:
                tmp_num_for_supply = tmp_num_for_supply + 1
            else:
                if tmp_num_for_supply == 1:
                    raise NotImplementedError
                else:
                    vdd_inputs['_NumberOfNbodyCOX'] = tmp_num_for_supply
                    self._DesignParameter['vdd']['_DesignObj']._CalculateNbodyContactDesignParameter(**vdd_inputs)
                    break
        if finger_on != 1:
            lower_met1_bound = self.FloorMinSnapSpacing( \
                min(self.getXYBot('nmos1', 'nmos', '_Met1Layer')[0][1],
                    self.getXYBot('nmos2', 'nmos', '_Met1Layer')[0][1],
                    self.getXYBot('nmos1_output_via', '_Met1Layer')[0][1],
                    self.getXYBot('nmos1_supply_via', '_Met1Layer')[0][1]),
                _MinSnapSpacing)
        else:
            lower_met1_bound = self.FloorMinSnapSpacing(
                min(self.getXY('nmos1', 'nmos', '_Met1Layer')[0][1] - self.getYWidth('nmos1', 'nmos', '_Met1Layer') / 2,
                    self.getXY('nmos2', 'nmos', '_Met1Layer')[0][1] - self.getYWidth('nmos2', 'nmos', '_Met1Layer') / 2,
                    self.getXYBot('nmos1_supply_via', '_Met1Layer')[0][1]), _MinSnapSpacing)
        higher_met1_bound = self.CeilMinSnapSpacing(
            max(self.getXY('pmos1', 'pmos', '_Met1Layer')[0][1] + self.getYWidth('pmos1', 'pmos', '_Met1Layer') / 2,
                self.getXY('pmos2', 'pmos', '_Met1Layer')[0][1] + self.getYWidth('pmos2', 'pmos', '_Met1Layer') / 2),
            _MinSnapSpacing)
        vss_y_value = self.FloorMinSnapSpacing(
            lower_met1_bound - self.getYWidth('vss', '_Met1Layer') / 2 - drc._Metal1MinSpace3, _MinSnapSpacing)
        vdd_y_value = self.CeilMinSnapSpacing(
            higher_met1_bound + self.getYWidth('vdd', '_Met1Layer') / 2 + drc._Metal1MinSpace3, _MinSnapSpacing)

        drc_poly1 = vdd_y_value - self.getYWidth('vdd', '_Met1Layer') / 2 - \
                    (max(self.getXYTop('pmos1', 'pmos', '_POLayer')[0][1],
                         self.getXYTop('pmos2', 'pmos', '_POLayer')[0][1]) + drc._PolygateMinSpace2OD)
        drc_poly2 = min(self.getXYBot('nmos1', 'nmos', '_POLayer')[0][1],
                        self.getXYBot('nmos2', 'nmos', '_POLayer')[0][1]) - \
                    drc._PolygateMinSpace2OD - (vss_y_value + self.getYWidth('vss', '_Met1Layer') / 2)

        if drc_poly1 < 0:
            vdd_y_value = vdd_y_value + abs(drc_poly1)
        if drc_poly2 < 0:
            vss_y_value = vss_y_value - abs(drc_poly2)

        if distance_to_vss != None:
            if (distance_to_vss < abs(vss_y_value)):
                distance_to_vss = vss_y_value
            else:
                distance_to_vss = -(distance_to_vss)
        else:
            distance_to_vss = vss_y_value
        if distance_to_vdd != None:
            if (distance_to_vdd < vdd_y_value):
                distance_to_vdd = vdd_y_value
        else:
            distance_to_vdd = vdd_y_value

        self._DesignParameter['vss']['_XYCoordinates'] = [[rail_x_center, distance_to_vss]]
        self._DesignParameter['vdd']['_XYCoordinates'] = [[rail_x_center, distance_to_vdd]]

        """
        Output to MOSCAP gate Routing
        """

        self._DesignParameter['output_to_moscap_routing'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _Width=self.getYWidth('pmos2', 'pmos_gate_via', '_Met1Layer'))

        source_x = x_value_for_output
        target_x = self.getXY('nmos2', 'nmos_gate_via', '_Met1Layer')[0][0]
        target_y1  = self.getXY('nmos2', 'nmos_gate_via', '_Met1Layer')[0][1]
        target_y2  = self.getXY('pmos2', 'pmos_gate_via', '_Met1Layer')[0][1]
        moscap_path = [[[source_x, target_y1], [target_x, target_y1]],[[source_x, target_y2], [target_x, target_y2]]]
        self._DesignParameter['output_to_moscap_routing']['_XYCoordinates'] = moscap_path

        # """
        # Additional BP, XVT, Poly Dummy, enable gate Met1 Generation
        # """
        # self._DesignParameter['additional_nxvt_layer'] = self._BoundaryElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping[f'{XVT}'][0],
        #     _Datatype=DesignParameters._LayerMapping[f'{XVT}'][1])
        # self._DesignParameter['additional_pxvt_layer'] = self._BoundaryElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping[f'{XVT}'][0],
        #     _Datatype=DesignParameters._LayerMapping[f'{XVT}'][1])
        #
        # xvt_leftmostedge = self.FloorMinSnapSpacing(min(
        #     self.getXY('pmos1', 'pmos', f'_{XVT}Layer')[0][0] - self.getXWidth('pmos1', 'pmos', f'_{XVT}Layer') / 2,
        #     self.getXY('nmos1', 'nmos', f'_{XVT}Layer')[0][0] - self.getXWidth('nmos1', 'nmos', f'_{XVT}Layer') / 2),
        #     _MinSnapSpacing)
        # xvt_rightmostedge = self.CeilMinSnapSpacing(max(
        #     self.getXY('pmos2', 'pmos', f'_{XVT}Layer')[0][0] + self.getXWidth('pmos2', 'pmos', f'_{XVT}Layer') / 2,
        #     self.getXY('nmos2', 'nmos', f'_{XVT}Layer')[0][0] + self.getXWidth('nmos2', 'nmos', f'_{XVT}Layer') / 2),
        #     _MinSnapSpacing)
        #
        # pxvt_topmostedge = self.CeilMinSnapSpacing(max(
        #     self.getXY('pmos1', 'pmos', f'_{XVT}Layer')[0][1] + self.getYWidth('pmos1', 'pmos', f'_{XVT}Layer') / 2,
        #     self.getXY('pmos2', 'pmos', f'_{XVT}Layer')[0][1] + self.getYWidth('pmos2', 'pmos', f'_{XVT}Layer') / 2),
        #     _MinSnapSpacing)
        # pxvt_bottommostedge = self.FloorMinSnapSpacing(min(
        #     self.getXY('pmos1', 'pmos', f'_{XVT}Layer')[0][1] - self.getYWidth('pmos1', 'pmos', f'_{XVT}Layer') / 2,
        #     self.getXY('pmos2', 'pmos', f'_{XVT}Layer')[0][1] - self.getYWidth('pmos2', 'pmos', f'_{XVT}Layer') / 2),
        #     _MinSnapSpacing)
        #
        # nxvt_topmostedge = self.CeilMinSnapSpacing(max(
        #     self.getXY('nmos1', 'nmos', f'_{XVT}Layer')[0][1] + self.getYWidth('nmos1', 'nmos', f'_{XVT}Layer') / 2,
        #     self.getXY('nmos2', 'nmos', f'_{XVT}Layer')[0][1] + self.getYWidth('nmos2', 'nmos', f'_{XVT}Layer') / 2),
        #     _MinSnapSpacing)
        # nxvt_bottommostedge = self.FloorMinSnapSpacing(min(
        #     self.getXY('nmos1', 'nmos', f'_{XVT}Layer')[0][1] - self.getYWidth('nmos1', 'nmos', f'_{XVT}Layer') / 2,
        #     self.getXY('nmos2', 'nmos', f'_{XVT}Layer')[0][1] - self.getYWidth('nmos2', 'nmos', f'_{XVT}Layer') / 2),
        #     _MinSnapSpacing)
        #
        # x_center = self.CeilMinSnapSpacing((xvt_leftmostedge + xvt_rightmostedge) / 2, _MinSnapSpacing)
        # nxvt_y_center = self.FloorMinSnapSpacing((nxvt_topmostedge + nxvt_bottommostedge) / 2, _MinSnapSpacing)
        # pxvt_y_center = self.CeilMinSnapSpacing((pxvt_topmostedge + pxvt_bottommostedge) / 2, _MinSnapSpacing)
        #
        # self._DesignParameter['additional_nxvt_layer']['_XWidth'] = xvt_rightmostedge - xvt_leftmostedge
        # self._DesignParameter['additional_pxvt_layer']['_XWidth'] = xvt_rightmostedge - xvt_leftmostedge
        # self._DesignParameter['additional_nxvt_layer']['_YWidth'] = nxvt_topmostedge - nxvt_bottommostedge
        # self._DesignParameter['additional_pxvt_layer']['_YWidth'] = pxvt_topmostedge - pxvt_bottommostedge
        # self._DesignParameter['additional_nxvt_layer']['_XYCoordinates'] = [[x_center, nxvt_y_center]]
        # self._DesignParameter['additional_pxvt_layer']['_XYCoordinates'] = [[x_center, pxvt_y_center]]

        # self._DesignParameter['additional_bp_layer'] = self._PathElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['PIMP'][0],
        #     _Datatype=DesignParameters._LayerMapping['PIMP'][1]
        #     )
        #
        # pp_width = min(self.getYWidth('pmos2', 'pmos', '_PPLayer'), self.getYWidth('pmos1', 'pmos', '_PPLayer'))
        # pp_x_source = self.getXYRight('pmos1', 'pmos', '_PPLayer')[0][0]
        # pp_x_target = self.getXYLeft('pmos2', 'pmos', '_PPLayer')[0][0]
        # pp_y = min(self.getXYLeft('pmos2', 'pmos', '_PPLayer')[0][1], self.getXYRight('pmos1', 'pmos', '_PPLayer')[0][1])
        # self._DesignParameter['additional_bp_layer']['_XYCoordinates'] = [[[pp_x_source, pp_y], [pp_x_target, pp_y]]]
        # self._DesignParameter['additional_bp_layer']['_Width'] = pp_width
        if dummy:
            dummy1 = \
            self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['nmos']['_DesignObj']._DesignParameter[
                '_PODummyLayer']
            dummy2 = \
            self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['nmos']['_DesignObj']._DesignParameter[
                '_PODummyLayer']

            source1 = self.getXYTop('nmos1', 'nmos', '_PODummyLayer')
            source2 = self.getXYTop('nmos2', 'nmos', '_PODummyLayer')
            poly_min_y_value1 = math.ceil(drc._PODummyMinArea / dummy1['_XWidth'])
            poly_min_y_value2 = math.ceil(drc._PODummyMinArea / dummy2['_XWidth'])
            if dummy1['_XWidth'] * dummy1['_YWidth'] < drc._PODummyMinArea:
                self._DesignParameter['additional_poly1'] = self._PathElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['POLY'][0],
                    _Datatype=DesignParameters._LayerMapping['POLY'][1],
                    _Width=dummy1['_XWidth'])
                self._DesignParameter['additional_poly1']['_XYCoordinates'] = [
                    [source1[0], [source1[0][0], source1[0][1] - poly_min_y_value1]],
                    [source1[1], [source1[1][0], source1[1][1] - poly_min_y_value1]]]
            if dummy2['_XWidth'] * dummy2['_YWidth'] < drc._PODummyMinArea:
                self._DesignParameter['additional_poly2'] = self._PathElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['POLY'][0],
                    _Datatype=DesignParameters._LayerMapping['POLY'][1],
                    _Width=dummy1['_XWidth'])
                self._DesignParameter['additional_poly2']['_XYCoordinates'] = [
                    [source2[0], [source2[0][0], source2[0][1] - poly_min_y_value2]],
                    [source2[1], [source2[1][0], source2[1][1] - poly_min_y_value2]]]

            pc_bot = min(source1[0][1] - poly_min_y_value1, source1[1][1] - poly_min_y_value1,
                         source2[0][1] - poly_min_y_value2, source2[1][1] - poly_min_y_value2)
            drc_test3 = pc_bot - self.getXYTop('vss', '_Met1Layer')[0][1] - drc._PolygateMinSpace2OD
            if drc_test3 < 0:
                calibre_value = abs(drc_test3)
                vss_y_value = vss_y_value - calibre_value
                self._DesignParameter['vss']['_XYCoordinates'] = [[rail_x_center, vss_y_value]]

        self._DesignParameter['nwell'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1])

        nwell_bot = self.getXYBot('pmos1', 'pmos', f'_{XVT}Layer')[0][1]
        nwell_top = self.getXYTop('vdd', '_ODLayer')[0][1] + drc._NwMinEnclosurePactive2
        nwell_left = self.getXYLeft('vdd', '_ODLayer')[0][0] - drc._NwMinSpacetoSLVT
        nwell_right = self.getXYRight('vdd', '_ODLayer')[0][0] + drc._NwMinSpacetoSLVT
        nwell_y_center = self.CeilMinSnapSpacing((nwell_top + nwell_bot) / 2, _MinSnapSpacing)
        nwell_x_center = self.CeilMinSnapSpacing((nwell_left + nwell_right) / 2, _MinSnapSpacing)
        nwell_xwidth = nwell_left - nwell_right
        nwell_ywidth = nwell_top - nwell_bot
        self._DesignParameter['nwell']['_XYCoordinates'] = [[nwell_x_center, nwell_y_center]]
        self._DesignParameter['nwell']['_XWidth'] = nwell_xwidth
        self._DesignParameter['nwell']['_YWidth'] = nwell_ywidth

        """
        MOSCAP Metal1 Boundary
        """
        self._DesignParameter['moscap_nmos_met1_layer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1])
        self._DesignParameter['moscap_pmos_met1_layer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1])

        nmos_met1_top = self.getXY('nmos2','nmos','_Met1Layer')[0][1]
        nmos_met1_bot = self.getXY('vss', '_Met1Layer')[0][1]
        nmos_met1_left = self.getXYLeft('nmos2','nmos', '_Met1Layer')[0][0]
        nmos_met1_right = self.getXYRight('nmos2','nmos', '_Met1Layer')[-1][0]

        pmos_met1_top = self.getXY('vdd', '_Met1Layer')[0][1]
        pmos_met1_bot = self.getXY('pmos2','pmos', '_Met1Layer')[0][1]
        pmos_met1_left = self.getXYLeft('pmos2','pmos', '_Met1Layer')[0][0]
        pmos_met1_right = self.getXYRight('pmos2','pmos', '_Met1Layer')[-1][0]

        nmos_center_x = self.CeilMinSnapSpacing((nmos_met1_left + nmos_met1_right) / 2, _MinSnapSpacing)
        nmos_center_y = self.CeilMinSnapSpacing((nmos_met1_top + nmos_met1_bot) / 2, _MinSnapSpacing)
        nmos_width = nmos_met1_right - nmos_met1_left
        nmos_height = nmos_met1_top - nmos_met1_bot

        pmos_center_x = self.CeilMinSnapSpacing((pmos_met1_left + pmos_met1_right) / 2, _MinSnapSpacing)
        pmos_center_y = self.CeilMinSnapSpacing((pmos_met1_top + pmos_met1_bot) / 2, _MinSnapSpacing)
        pmos_width = pmos_met1_right - pmos_met1_left
        pmos_height = pmos_met1_top - pmos_met1_bot

        self._DesignParameter['moscap_nmos_met1_layer']['_XYCoordinates'] = [[nmos_center_x, nmos_center_y]]
        self._DesignParameter['moscap_nmos_met1_layer']['_XWidth'] = nmos_width
        self._DesignParameter['moscap_nmos_met1_layer']['_YWidth'] = nmos_height

        self._DesignParameter['moscap_pmos_met1_layer']['_XYCoordinates'] = [[pmos_center_x, pmos_center_y]]
        self._DesignParameter['moscap_pmos_met1_layer']['_XWidth'] = pmos_width
        self._DesignParameter['moscap_pmos_met1_layer']['_YWidth'] = pmos_height

        self.space_bw_gate_nmos_met1_edges = self.getXYBot('nmos1', 'nmos_gate_via', '_Met1Layer')[0][1] -\
            self.getXYTop('nmos1', 'nmos', '_Met1Layer')[0][1]
        self.space_bw_gate_pmos_met1_edges = abs(self.getXYTop('pmos1', 'pmos_gate_via', '_Met1Layer')[0][1] -\
            self.getXYBot('pmos1', 'pmos', '_Met1Layer')[0][1])

        self.space_bw_np_gate_centers = self.getXY('pmos1', 'pmos_gate_via','_Met1Layer')[0][1] - \
                                        self.getXY('nmos1', 'nmos_gate_via', '_Met1Layer')[0][1]

        self.distance_to_vdd = self._DesignParameter['vdd']['_XYCoordinates'][0][1]
        self.distance_to_vss = abs(self._DesignParameter['vss']['_XYCoordinates'][0][1])

        self.leftmost_poly_edge = min(self.getXYLeft('nmos1','nmos','_PODummyLayer')[0][0],
                                      self.getXYLeft('pmos1','pmos', '_PODummyLayer')[0][0])
        self.rightmost_poly_edge = max(self.getXYRight('nmos2','nmos','_PODummyLayer')[-1][0],
                                      self.getXYRight('pmos2','pmos', '_PODummyLayer')[-1][0])
        self.cell_width = self.rightmost_poly_edge - self.leftmost_poly_edge

if __name__ == '__main__':
    Obj = MOSCAP_ON()
    Obj._CalculateDesignParameter(channel_length=30, dummy=True, PCCrit=True, XVT='SLVT',
                                  finger_on=1, channel_width1=400,
                                  finger2=1, channel_width2=400,
                                  channel_width3=200,
                                  finger4=1, channel_width4=200
                                  )

    Obj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=Obj._DesignParameter)
    _fileName = 'MS_moscap_on.gds'
    testStreamFile = open('./MS_moscap_on.gds', 'wb')
    tmp = Obj._CreateGDSStream(Obj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    import ftplib

    ftp = ftplib.FTP('141.223.29.62')
    ftp.login('kms95', 'dosel545')
    ftp.cwd('/mnt/sdb/kms95/OPUS/ss28')
    myfile = open('MS_moscap_on.gds', 'rb')
    ftp.storbinary('STOR MS_moscap_on.gds', myfile)
    myfile.close()
    ftp.close()
    #
    # import DRCchecker
    #
    # _DRC = DRCchecker.DRCchecker('kms95', 'dosel545', '/mnt/sdb/kms95/OPUS/ss28', '/mnt/sdb/kms95/OPUS/ss28/DRC/run',
    #                              'MS_moscap_on', 'MS_moscap_on')
    # _DRC.DRCchecker()

