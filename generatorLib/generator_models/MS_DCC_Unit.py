from generatorLib import DRC
from generatorLib.generator_models import NbodyContact
from generatorLib.generator_models import PbodyContact
from generatorLib.generator_models import PMOSWithGate
from generatorLib.generator_models import NMOSWithGate
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import MS_inverter_on_out
from generatorLib.generator_models import MS_Inverter_array

from generatorLib import StickDiagram
from generatorLib import DesignParameters
from generatorLib import DRC
import math

class DCC_Unit(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict( channel_length=None, dummy=None, PCCrit=None, XVT=None,
                                            supply_num_coy=None, distance_to_vdd=None, distance_to_vss=None,
                                            coarse_fine_dimension=None, gap_bw_gates=None,

                                            #### Dictionary for Inverter ON
                                            finger_on_n=None, channel_width_on_n=None,
                                            finger_on_p=None, channel_width_on_p=None,

                                            #### Dictionary for Inverter COARSE
                                            finger_coarse_p1=None, channel_width_coarse_p1=None,
                                            finger_coarse_p2=None, channel_width_coarse_p2=None,
                                            finger_coarse_n1=None, channel_width_coarse_n1=None,
                                            finger_coarse_n2=None, channel_width_coarse_n2=None,

                                            #### Dictionary for Inverter FINE
                                            finger_fine_p1=None, channel_width_fine_p1=None,
                                            finger_fine_p2=None, channel_width_cfine_p2=None,
                                            finger_fine_n1=None, channel_width_fine_n1=None,
                                            finger_fine_n2=None, channel_width_fine_n2=None,

                                            #### Dictionary for Inverter OUT
                                            finger_out_n=None, channel_width_out_n=None,
                                            finger_out_p=None, channel_width_out_p=None
                                            )


    def __init__(self, _DesignParameter=None, _Name='DCC_Unit'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter(self,     channel_length=None, dummy=None, PCCrit=None, XVT=None,
                                            supply_num_coy=None, distance_to_vdd=None, distance_to_vss=None,
                                            coarse_fine_dimension=None, gap_bw_gates=None,

                                            #### Dictionary for Inverter ON
                                            finger_on_n=None, channel_width_on_n=None,
                                            finger_on_p=None, channel_width_on_p=None,

                                            #### Dictionary for Inverter COARSE
                                            finger_coarse_p1=None, channel_width_coarse_p1=None,
                                            finger_coarse_p2=None, channel_width_coarse_p2=None,
                                            finger_coarse_n1=None, channel_width_coarse_n1=None,
                                            finger_coarse_n2=None, channel_width_coarse_n2=None,

                                            #### Dictionary for Inverter FINE
                                            finger_fine_p1=None, channel_width_fine_p1=None,
                                            finger_fine_p2=None, channel_width_fine_p2=None,
                                            finger_fine_n1=None, channel_width_fine_n1=None,
                                            finger_fine_n2=None, channel_width_fine_n2=None,

                                            #### Dictionary for Inverter OUT
                                            finger_out_n=None, channel_width_out_n=None,
                                            finger_out_p=None, channel_width_out_p=None
                                  ):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        _MinSnapSpacing = drc._MinSnapSpacing

        self._DesignParameter['inverter_coarse'] =\
        self._SrefElementDeclaration(_DesignObj=MS_Inverter_array.INVERTER_ARRAY(_DesignParameter=None,
                                                                            _Name=f'inverter_coarse_in_{_Name}'))[0]
        self._DesignParameter['inverter_fine'] = \
            self._SrefElementDeclaration(_DesignObj=MS_Inverter_array.INVERTER_ARRAY(_DesignParameter=None,
                                                                            _Name=f'inverter_fine_in_{_Name}'))[0]
        self._DesignParameter['inverter_on'] = \
            self._SrefElementDeclaration(_DesignObj=MS_inverter_on_out.INVERTER_ON_OUT(_DesignParameter=None,
                                                                            _Name=f'inverter_on_in_{_Name}'))[0]
        self._DesignParameter['inverter_out'] = \
            self._SrefElementDeclaration(_DesignObj=MS_inverter_on_out.INVERTER_ON_OUT(_DesignParameter=None,
                                                                            _Name=f'inverter_out_in_{_Name}'))[0]

        array_coarse_input = dict(channel_length=channel_length, dummy=dummy, PCCrit=PCCrit, XVT=XVT,
                            finger1=finger_coarse_p1, channel_width1=channel_width_coarse_p1,
                            finger2=finger_coarse_p2, channel_width2=channel_width_coarse_p2,
                            finger3=finger_coarse_n1, channel_width3=channel_width_coarse_n1,
                            finger4=finger_coarse_n2, channel_width4=channel_width_coarse_n2,
                            gap_bw_mos_gates= gap_bw_gates, supply_num_coy=supply_num_coy,
                            cell_number= coarse_fine_dimension,
                            distance_to_vdd=distance_to_vdd, distance_to_vss=distance_to_vss)

        array_fine_input = dict(channel_length=channel_length, dummy=dummy, PCCrit=PCCrit, XVT=XVT,
                            finger1=finger_fine_p1, channel_width1=channel_width_fine_p1,
                            finger2=finger_fine_p2, channel_width2=channel_width_fine_p2,
                            finger3=finger_fine_n1, channel_width3=channel_width_fine_n1,
                            finger4=finger_fine_n2, channel_width4=channel_width_fine_n2,
                            gap_bw_mos_gates= gap_bw_gates, supply_num_coy=supply_num_coy,
                            cell_number= coarse_fine_dimension,
                            distance_to_vdd=distance_to_vdd, distance_to_vss=distance_to_vss)

        on_input = dict(channel_length=channel_length, dummy=dummy, PCCrit=PCCrit, XVT=XVT,
                        finger1=finger_on_p, channel_width1=channel_width_on_p,
                        finger2=finger_on_n, channel_width2=channel_width_on_n,
                        supply_num_coy = supply_num_coy,
                        distance_to_vdd = distance_to_vdd, distance_to_vss = distance_to_vss)

        out_input = dict(channel_length=channel_length, dummy=dummy, PCCrit=PCCrit, XVT=XVT,
                        finger1=finger_out_p, channel_width1=channel_width_out_p,
                        finger2=finger_out_n, channel_width2=channel_width_out_n,
                        supply_num_coy = supply_num_coy,
                        distance_to_vdd = distance_to_vdd, distance_to_vss = distance_to_vss)

        self._DesignParameter['inverter_on']['_DesignObj']._CalculateDesignParameter(**on_input)
        self._DesignParameter['inverter_coarse']['_DesignObj']._CalculateDesignParameter(**array_coarse_input)
        self._DesignParameter['inverter_fine']['_DesignObj']._CalculateDesignParameter(**array_fine_input)
        self._DesignParameter['inverter_out']['_DesignObj']._CalculateDesignParameter(**out_input)

        self._DesignParameter['inverter_on']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['inverter_coarse']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['inverter_fine']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['inverter_out']['_XYCoordinates'] = [[0, 0]]

        cell_width = self._DesignParameter['inverter_on']['_DesignObj'].cell_width + \
                     self._DesignParameter['inverter_coarse']['_DesignObj'].cell_width + \
                     self._DesignParameter['inverter_fine']['_DesignObj'].cell_width + \
                     self._DesignParameter['inverter_out']['_DesignObj'].cell_width + \
                     drc._PolygateMinSpace * 3

        gap_bw_mos_gates = max(self._DesignParameter['inverter_coarse']['_DesignObj'].space_bw_np_gate_centers,
                               self._DesignParameter['inverter_fine']['_DesignObj'].space_bw_np_gate_centers,
                               self._DesignParameter['inverter_on']['_DesignObj'].space_bw_np_gate_centers,
                               self._DesignParameter['inverter_out']['_DesignObj'].space_bw_np_gate_centers)
        on_input['gap_bw_mos_gates'] = gap_bw_mos_gates
        array_coarse_input['gap_bw_mos_gates'] = gap_bw_mos_gates
        array_fine_input['gap_bw_mos_gates'] = gap_bw_mos_gates
        out_input['gap_bw_mos_gates'] = gap_bw_mos_gates

        space_bw_gate_nmos = max(self._DesignParameter['inverter_coarse']['_DesignObj'].space_bw_gate_nmos_met1_edges,
                                 self._DesignParameter['inverter_fine']['_DesignObj'].space_bw_gate_nmos_met1_edges,
                                 self._DesignParameter['inverter_on']['_DesignObj'].space_bw_gate_nmos_met1_edges,
                                 self._DesignParameter['inverter_fine']['_DesignObj'].space_bw_gate_nmos_met1_edges)
        space_bw_gate_pmos = max(self._DesignParameter['inverter_coarse']['_DesignObj'].space_bw_gate_pmos_met1_edges,
                                 self._DesignParameter['inverter_fine']['_DesignObj'].space_bw_gate_pmos_met1_edges,
                                 self._DesignParameter['inverter_on']['_DesignObj'].space_bw_gate_pmos_met1_edges,
                                 self._DesignParameter['inverter_fine']['_DesignObj'].space_bw_gate_pmos_met1_edges)

        on_input['space_bw_gate_nmos'] = space_bw_gate_nmos - drc._Metal1MinSpace2
        array_coarse_input['space_bw_gate_nmos'] = space_bw_gate_nmos - drc._Metal1MinSpace2
        array_fine_input['space_bw_gate_nmos'] = space_bw_gate_nmos - drc._Metal1MinSpace2
        out_input['space_bw_gate_nmos'] = space_bw_gate_nmos - drc._Metal1MinSpace2

        on_input['space_bw_gate_pmos'] = space_bw_gate_pmos - drc._Metal1MinSpace2
        array_coarse_input['space_bw_gate_pmos'] = space_bw_gate_pmos - drc._Metal1MinSpace2
        array_fine_input['space_bw_gate_pmos'] = space_bw_gate_pmos - drc._Metal1MinSpace2
        out_input['space_bw_gate_pmos'] = space_bw_gate_pmos - drc._Metal1MinSpace2

        self._DesignParameter['inverter_on']['_DesignObj']._CalculateDesignParameter(**on_input)
        self._DesignParameter['inverter_coarse']['_DesignObj']._CalculateDesignParameter(**array_coarse_input)
        self._DesignParameter['inverter_fine']['_DesignObj']._CalculateDesignParameter(**array_fine_input)
        self._DesignParameter['inverter_out']['_DesignObj']._CalculateDesignParameter(**out_input)

        distance_to_vdd_min = max(self._DesignParameter['inverter_on']['_DesignObj'].distance_to_vdd,
                                  self._DesignParameter['inverter_coarse']['_DesignObj'].distance_to_vdd,
                                  self._DesignParameter['inverter_fine']['_DesignObj'].distance_to_vdd,
                                  self._DesignParameter['inverter_out']['_DesignObj'].distance_to_vdd)
        distance_to_vss_min = max(self._DesignParameter['inverter_on']['_DesignObj'].distance_to_vss,
                                  self._DesignParameter['inverter_coarse']['_DesignObj'].distance_to_vss,
                                  self._DesignParameter['inverter_fine']['_DesignObj'].distance_to_vss,
                                  self._DesignParameter['inverter_out']['_DesignObj'].distance_to_vss)
        if distance_to_vdd == None:
            distance_to_vdd = distance_to_vdd_min
        else:
            if distance_to_vdd < distance_to_vdd_min:
                # raise Exception("Distance To VDD value Invalid")
                distance_to_vdd = distance_to_vdd_min
            else:
                pass
        on_input['distance_to_vdd'] = distance_to_vdd
        array_coarse_input['distance_to_vdd'] = distance_to_vdd
        array_fine_input['distance_to_vdd'] = distance_to_vdd
        out_input['distance_to_vdd'] = distance_to_vdd

        if distance_to_vss == None:
            distance_to_vss = distance_to_vss_min
        else:
            if distance_to_vss < distance_to_vss_min:
                # raise Exception("Distance To VSS value Invalid")
                distance_to_vss = distance_to_vss_min
            else:
                pass

        on_input['distance_to_vss'] = distance_to_vss
        array_coarse_input['distance_to_vss'] = distance_to_vss
        array_fine_input['distance_to_vss'] = distance_to_vss
        out_input['distance_to_vss'] = distance_to_vss

        self._DesignParameter['inverter_on']['_DesignObj']._CalculateDesignParameter(**on_input)
        self._DesignParameter['inverter_coarse']['_DesignObj']._CalculateDesignParameter(**array_coarse_input)
        self._DesignParameter['inverter_fine']['_DesignObj']._CalculateDesignParameter(**array_fine_input)
        self._DesignParameter['inverter_out']['_DesignObj']._CalculateDesignParameter(**out_input)

        on_center_x =  self.CeilMinSnapSpacing(\
            0 - cell_width / 2 + abs(self._DesignParameter['inverter_on']['_DesignObj'].leftmost_poly_edge),
            _MinSnapSpacing)

        coarse_center_x = on_center_x + self._DesignParameter['inverter_on']['_DesignObj'].rightmost_poly_edge + \
                          abs(self._DesignParameter['inverter_coarse']['_DesignObj'].leftmost_poly_edge)+ drc._PolygateMinSpace
        fine_center_x = coarse_center_x + self._DesignParameter['inverter_coarse']['_DesignObj'].rightmost_poly_edge + \
                          abs(self._DesignParameter['inverter_fine']['_DesignObj'].leftmost_poly_edge) + drc._PolygateMinSpace
        out_center_x = fine_center_x + self._DesignParameter['inverter_fine']['_DesignObj'].rightmost_poly_edge + \
                          abs(self._DesignParameter['inverter_out']['_DesignObj'].leftmost_poly_edge) + drc._PolygateMinSpace


        self._DesignParameter['inverter_on']['_XYCoordinates'] = [[on_center_x, distance_to_vss]]
        self._DesignParameter['inverter_coarse']['_XYCoordinates'] = [[coarse_center_x, distance_to_vss]]
        self._DesignParameter['inverter_fine']['_XYCoordinates'] = [[fine_center_x, distance_to_vss]]
        self._DesignParameter['inverter_out']['_XYCoordinates'] = [[out_center_x, distance_to_vss]]

        """
        Additional BP, XVT, NWELL Layer Generation
        """
        self._DesignParameter['additional_nxvt_layer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[f'{XVT}'][0],
            _Datatype=DesignParameters._LayerMapping[f'{XVT}'][1])
        self._DesignParameter['additional_pxvt_layer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[f'{XVT}'][0],
            _Datatype=DesignParameters._LayerMapping[f'{XVT}'][1])

        xvt_leftmostedge = min(math.floor(self.getXYLeft('inverter_on', 'pmos', 'pmos', f'_{XVT}Layer')[0][0]),
                               math.floor(self.getXYLeft('inverter_on', 'nmos', 'nmos', f'_{XVT}Layer')[0][0])) - _MinSnapSpacing

        xvt_rightmostedge = max(math.ceil(self.getXYRight('inverter_out', 'pmos', 'pmos', f'_{XVT}Layer')[0][0]),
                                math.ceil(self.getXYRight('inverter_out', 'nmos', 'nmos', f'_{XVT}Layer')[0][0])) + _MinSnapSpacing

        pxvt_topmostedge = max(math.ceil(self.getXYTop('inverter_on', 'pmos', 'pmos',  f'_{XVT}Layer')[0][1]),
                               math.ceil(self.getXYTop('inverter_coarse', 'inverter_1', 'additional_pxvt_layer')[0][1]),
                               math.ceil(self.getXYTop('inverter_fine', 'inverter_1', 'additional_pxvt_layer')[0][1]),
                               math.ceil(self.getXYTop('inverter_out', 'pmos', 'pmos',  f'_{XVT}Layer')[0][1]))
        pxvt_bottommostedge = min(math.floor(self.getXYBot('inverter_on', 'pmos', 'pmos',  f'_{XVT}Layer')[0][1]),
                               math.floor(self.getXYBot('inverter_coarse', 'inverter_1', 'additional_pxvt_layer')[0][1]),
                               math.floor(self.getXYBot('inverter_fine', 'inverter_1', 'additional_pxvt_layer')[0][1]),
                               math.floor(self.getXYBot('inverter_out', 'pmos', 'pmos',  f'_{XVT}Layer')[0][1]))

        nxvt_topmostedge = max(math.ceil(self.getXYTop('inverter_on', 'nmos', 'nmos',  f'_{XVT}Layer')[0][1]),
                               math.ceil(self.getXYTop('inverter_coarse', 'inverter_1', 'additional_nxvt_layer')[0][1]),
                               math.ceil(self.getXYTop('inverter_fine', 'inverter_1', 'additional_nxvt_layer')[0][1]),
                               math.ceil(self.getXYTop('inverter_out', 'nmos', 'nmos',  f'_{XVT}Layer')[0][1]))
        nxvt_bottommostedge = min(math.floor(self.getXYBot('inverter_on', 'nmos', 'nmos',  f'_{XVT}Layer')[0][1]),
                               math.floor(self.getXYBot('inverter_coarse', 'inverter_1', 'additional_nxvt_layer')[0][1]),
                               math.floor(self.getXYBot('inverter_fine', 'inverter_1', 'additional_nxvt_layer')[0][1]),
                               math.floor(self.getXYBot('inverter_out', 'nmos', 'nmos',  f'_{XVT}Layer')[0][1]))

        x_center =  self.CeilMinSnapSpacing((xvt_leftmostedge + xvt_rightmostedge) / 2, _MinSnapSpacing)
        nxvt_y_center =  self.CeilMinSnapSpacing((nxvt_topmostedge + nxvt_bottommostedge) / 2, _MinSnapSpacing)
        pxvt_y_center =  self.CeilMinSnapSpacing((pxvt_topmostedge + pxvt_bottommostedge) / 2, _MinSnapSpacing)

        self._DesignParameter['additional_nxvt_layer']['_XWidth'] = xvt_rightmostedge - xvt_leftmostedge
        self._DesignParameter['additional_pxvt_layer']['_XWidth'] = xvt_rightmostedge - xvt_leftmostedge
        self._DesignParameter['additional_nxvt_layer']['_YWidth'] = nxvt_topmostedge - nxvt_bottommostedge
        self._DesignParameter['additional_pxvt_layer']['_YWidth'] = pxvt_topmostedge - pxvt_bottommostedge
        self._DesignParameter['additional_nxvt_layer']['_XYCoordinates'] = [[x_center, nxvt_y_center]]
        self._DesignParameter['additional_pxvt_layer']['_XYCoordinates'] = [[x_center, pxvt_y_center]]


        self._DesignParameter['additional_bp_layer1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1])

        bp_leftmostedge = self.getXYLeft('inverter_on', 'pmos', 'pmos', f'_PPLayer')[0][0] - _MinSnapSpacing
        bp_rightmostedge = self.getXYRight('inverter_out', 'pmos', 'pmos', f'_PPLayer')[0][0] + _MinSnapSpacing
        bp_topmostedge = max(self.getXYTop('inverter_on', 'pmos', 'pmos',  f'_PPLayer')[0][1],
                             self.getXYTop('inverter_coarse', 'inverter_1', 'pmos1', 'pmos', '_PPLayer')[0][1],
                             self.getXYTop('inverter_coarse', 'inverter_1', 'pmos2', 'pmos', '_PPLayer')[0][1],
                             self.getXYTop('inverter_fine', 'inverter_1', 'pmos1', 'pmos', '_PPLayer')[0][1],
                             self.getXYTop('inverter_fine', 'inverter_1', 'pmos2', 'pmos', '_PPLayer')[0][1],
                             self.getXYTop('inverter_out', 'pmos', 'pmos',  f'_PPLayer')[0][1])
        bp_bottommostedge = pxvt_bottommostedge
        bp_x_center =  self.CeilMinSnapSpacing((bp_leftmostedge + bp_rightmostedge) / 2, _MinSnapSpacing)
        bp_y_center =  self.CeilMinSnapSpacing((bp_topmostedge + bp_bottommostedge) / 2, _MinSnapSpacing)

        self._DesignParameter['additional_bp_layer1']['_XWidth'] = bp_rightmostedge - bp_leftmostedge
        self._DesignParameter['additional_bp_layer1']['_YWidth'] = bp_topmostedge - bp_bottommostedge
        self._DesignParameter['additional_bp_layer1']['_XYCoordinates'] = [[bp_x_center, bp_y_center]]


        self._DesignParameter['additional_bp_layer2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1])

        bp_leftmostedge = self.getXYLeft('inverter_on', 'vss', '_PPLayer')[0][0]- _MinSnapSpacing
        bp_rightmostedge = self.getXYRight('inverter_out', 'vss', '_PPLayer')[0][0] + _MinSnapSpacing
        bp_topmostedge = self.getXYTop('inverter_on', 'vss', '_PPLayer')[0][1]
        bp_bottommostedge = self.getXYBot('inverter_on', 'vss', '_PPLayer')[0][1]
        bp_x_center =  self.CeilMinSnapSpacing((bp_leftmostedge + bp_rightmostedge) / 2, _MinSnapSpacing)
        bp_y_center =  self.CeilMinSnapSpacing((bp_topmostedge + bp_bottommostedge) / 2, _MinSnapSpacing)

        self._DesignParameter['additional_bp_layer2']['_XWidth'] = bp_rightmostedge - bp_leftmostedge
        self._DesignParameter['additional_bp_layer2']['_YWidth'] = bp_topmostedge - bp_bottommostedge
        self._DesignParameter['additional_bp_layer2']['_XYCoordinates'] = [[bp_x_center, bp_y_center]]

        self._DesignParameter['additional_rx_layer1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0],
            _Datatype=DesignParameters._LayerMapping['DIFF'][1])

        rx_leftmostedge = self.getXYLeft('inverter_on', 'vss', '_ODLayer')[0][0]- _MinSnapSpacing
        rx_rightmostedge = self.getXYRight('inverter_out', 'vss', '_ODLayer')[0][0]+ _MinSnapSpacing
        rx_topmostedge = self.getXYTop('inverter_on', 'vss', '_ODLayer')[0][1]
        rx_bottommostedge = self.getXYBot('inverter_on', 'vss', '_ODLayer')[0][1]
        rx_x_center =  self.CeilMinSnapSpacing((rx_leftmostedge + rx_rightmostedge) / 2, _MinSnapSpacing)
        rx_y_center =  self.CeilMinSnapSpacing((rx_topmostedge + rx_bottommostedge) / 2, _MinSnapSpacing)

        self._DesignParameter['additional_rx_layer1']['_XWidth'] = rx_rightmostedge - rx_leftmostedge
        self._DesignParameter['additional_rx_layer1']['_YWidth'] = rx_topmostedge - rx_bottommostedge
        self._DesignParameter['additional_rx_layer1']['_XYCoordinates'] = [[rx_x_center, rx_y_center]]


        self._DesignParameter['additional_rx_layer2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0],
            _Datatype=DesignParameters._LayerMapping['DIFF'][1])

        rx_leftmostedge = self.getXYLeft('inverter_on', 'vdd', '_ODLayer')[0][0]- _MinSnapSpacing
        rx_rightmostedge = self.getXYRight('inverter_out', 'vdd', '_ODLayer')[0][0]+ _MinSnapSpacing
        rx_topmostedge = self.getXYTop('inverter_on', 'vdd', '_ODLayer')[0][1]
        rx_bottommostedge = self.getXYBot('inverter_on', 'vdd', '_ODLayer')[0][1]
        rx_x_center =  self.CeilMinSnapSpacing((rx_leftmostedge + rx_rightmostedge) / 2, _MinSnapSpacing)
        rx_y_center =  self.CeilMinSnapSpacing((rx_topmostedge + rx_bottommostedge) / 2, _MinSnapSpacing)

        self._DesignParameter['additional_rx_layer2']['_XWidth'] = rx_rightmostedge - rx_leftmostedge
        self._DesignParameter['additional_rx_layer2']['_YWidth'] = rx_topmostedge - rx_bottommostedge
        self._DesignParameter['additional_rx_layer2']['_XYCoordinates'] = [[rx_x_center, rx_y_center]]

        self._DesignParameter['additional_met1_layer1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1])

        met1_leftmostedge = self.getXYLeft('inverter_on', 'vss', '_Met1Layer')[0][0]
        met1_rightmostedge = self.getXYRight('inverter_out', 'vss', '_Met1Layer')[0][0]
        met1_topmostedge = self.getXYTop('inverter_on', 'vss', '_Met1Layer')[0][1]
        met1_bottommostedge = self.getXYBot('inverter_on', 'vss', '_Met1Layer')[0][1]
        met1_x_center =  self.CeilMinSnapSpacing((met1_leftmostedge + met1_rightmostedge) / 2, _MinSnapSpacing)
        met1_y_center =  self.CeilMinSnapSpacing((met1_topmostedge + met1_bottommostedge) / 2, _MinSnapSpacing)

        self._DesignParameter['additional_met1_layer1']['_XWidth'] = met1_rightmostedge - met1_leftmostedge
        self._DesignParameter['additional_met1_layer1']['_YWidth'] = met1_topmostedge - met1_bottommostedge
        self._DesignParameter['additional_met1_layer1']['_XYCoordinates'] = [[met1_x_center, met1_y_center]]


        self._DesignParameter['additional_met1_layer2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1])

        met1_leftmostedge = self.getXYLeft('inverter_on', 'vdd', '_Met1Layer')[0][0]
        met1_rightmostedge = self.getXYRight('inverter_out', 'vdd', '_Met1Layer')[0][0]
        met1_topmostedge = self.getXYTop('inverter_on', 'vdd', '_Met1Layer')[0][1]
        met1_bottommostedge = self.getXYBot('inverter_on', 'vdd', '_Met1Layer')[0][1]
        met1_x_center =  self.CeilMinSnapSpacing((met1_leftmostedge + met1_rightmostedge) / 2, _MinSnapSpacing)
        met1_y_center =  self.CeilMinSnapSpacing((met1_topmostedge + met1_bottommostedge) / 2, _MinSnapSpacing)

        self._DesignParameter['additional_met1_layer2']['_XWidth'] = met1_rightmostedge - met1_leftmostedge
        self._DesignParameter['additional_met1_layer2']['_YWidth'] = met1_topmostedge - met1_bottommostedge
        self._DesignParameter['additional_met1_layer2']['_XYCoordinates'] = [[met1_x_center, met1_y_center]]

        self._DesignParameter['additional_nwell_layer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1])

        nw_leftmostedge = self.getXYLeft('inverter_on', 'nwell')[0][0]- _MinSnapSpacing
        nw_rightmostedge = self.getXYRight('inverter_out', 'nwell')[0][0]+ _MinSnapSpacing

        nw_topmostedge = max(self.getXYTop('inverter_on', 'nwell')[0][1],
                             self.getXYTop('inverter_coarse','inverter_1', 'nwell')[0][1],
                             self.getXYTop('inverter_fine','inverter_1', 'nwell')[0][1],
                             self.getXYTop('inverter_out', 'nwell')[0][1])
        nw_bottommostedge = min(self.getXYBot('inverter_on', 'nwell')[0][1],
                                self.getXYBot('inverter_coarse', 'inverter_1', 'nwell')[0][1],
                                self.getXYBot('inverter_fine', 'inverter_1', 'nwell')[0][1],
                                self.getXYBot('inverter_out', 'nwell')[0][1])
        if pxvt_bottommostedge < nw_bottommostedge:
            nw_bottommostedge = pxvt_bottommostedge

        nw_x_center =  self.CeilMinSnapSpacing((nw_leftmostedge + nw_rightmostedge) / 2, _MinSnapSpacing)
        nw_y_center =  self.CeilMinSnapSpacing((nw_topmostedge + nw_bottommostedge) / 2, _MinSnapSpacing)

        self._DesignParameter['additional_nwell_layer']['_XWidth'] = nw_rightmostedge - nw_leftmostedge
        self._DesignParameter['additional_nwell_layer']['_YWidth'] = nw_topmostedge - nw_bottommostedge
        self._DesignParameter['additional_nwell_layer']['_XYCoordinates'] = [[nw_x_center, nw_y_center]]


        """
        Output Routing
        """
        self._DesignParameter['output_routing'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1])

        x_source_value =\
            self._DesignParameter['inverter_on']['_XYCoordinates'][0][0] + \
            self._DesignParameter['inverter_on']['_DesignObj']._DesignParameter['output_routing']['_XYCoordinates'][0][1][0]
        x_target_value = \
            self._DesignParameter['inverter_out']['_XYCoordinates'][0][0] + \
            self._DesignParameter['inverter_out']['_DesignObj']._DesignParameter['output_routing']['_XYCoordinates'][0][1][0]

        self._DesignParameter['output_routing']['_Width'] = drc._MetalxMinWidth
        self._DesignParameter['output_routing']['_XYCoordinates'] = [[[x_source_value, distance_to_vss],
                                                                      [x_target_value, distance_to_vss]]]

        print("DCC Calculation End")


if __name__ == '__main__':
    Obj = DCC_Unit()
    Obj._CalculateDesignParameter(  channel_length=30, dummy=True, PCCrit=True, XVT='SLVT',
                                    supply_num_coy=None, distance_to_vdd=None, distance_to_vss=None,
                                    coarse_fine_dimension=5, gap_bw_gates=None,

                                    #### Dictionary for Inverter ON
                                    finger_on_n=3, channel_width_on_n=200,
                                    finger_on_p=4, channel_width_on_p=400,

                                    #### Dictionary for Inverter COARSE
                                    finger_coarse_p1=5, channel_width_coarse_p1=500,
                                    finger_coarse_p2=2, channel_width_coarse_p2=600,
                                    finger_coarse_n1=1, channel_width_coarse_n1=200,
                                    finger_coarse_n2=5, channel_width_coarse_n2=200,

                                    #### Dictionary for Inverter FINE
                                    finger_fine_p1=3, channel_width_fine_p1=700,
                                    finger_fine_p2=1, channel_width_fine_p2=800,
                                    finger_fine_n1=5, channel_width_fine_n1=200,
                                    finger_fine_n2=6, channel_width_fine_n2=200,

                                    #### Dictionary for Inverter OUT
                                    finger_out_n=6, channel_width_out_n=200,
                                    finger_out_p=7, channel_width_out_p=700
                                    )

    Obj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=Obj._DesignParameter)
    _fileName = 'MS_DCC_Unit.gds'
    testStreamFile = open('./MS_DCC_Unit.gds', 'wb')
    tmp = Obj._CreateGDSStream(Obj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    import ftplib

    ftp = ftplib.FTP('141.223.29.62')
    ftp.login('kms95', 'dosel545')
    ftp.cwd('/mnt/sdb/kms95/Desktop')
    myfile = open('MS_DCC_Unit.gds', 'rb')
    ftp.storbinary('STOR MS_DCC_Unit.gds', myfile)
    myfile.close()
    ftp.close()