from generatorLib import DRC


from generatorLib.generator_models import MS_moscap_array
from generatorLib.generator_models import MS_inverter_chain
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaMet22Met3
from generatorLib import StickDiagram
from generatorLib import DesignParameters

import copy, math, warnings

class MOSCAP_FINE_FULL(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(channel_length=None, dummy=None, PCCrit=None, XVT=None,
                                           supply_num_coy=None, supply_num_cox=None,
                                           distance_to_vdd=None, distance_to_vss=None,
                                           space_bw_gate_nmos=None, space_bw_gate_pmos=None,
                                           gap_bw_mos_gates=None, array_dimension=None,

                                           # INVERTER WITH INPUT COARSE

                                           finger1_n= None, finger1_p = None,
                                           channel_width_finger1_n=None, channel_width_finger1_p=None,

                                           #INVERTER WITH INPUT FINE

                                           finger2_n=None, finger2_p=None,
                                           channel_width_finger2_n=None, channel_width_finger2_p=None,

                                           # INVERTER IN LATCH

                                           finger3_n=None, finger3_p=None,
                                           channel_width_finger3_n=None, channel_width_finger3_p=None,

                                           # MOSCAP FINE INPUTS
                                           finger_sel_p=None, finger_sel_n=None,
                                           finger_on = None,
                                           finger_moscap_p = None, finger_moscap_n = None,

                                           channel_width_sel_p = None, channel_width_sel_n = None,
                                           channel_width_on_p = None, channel_width_on_n = None,
                                           channel_width_moscap_p = None, channel_width_moscap_n = None

                                           )

    def __init__(self, _DesignParameter=None, _Name=f'MS_moscap_fine_full'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter(self,
                                  channel_length=None, dummy=None, PCCrit=None, XVT=None,
                                  supply_num_coy=None,
                                  distance_to_vdd=None, distance_to_vss=None,
                                  space_bw_gate_nmos=None, space_bw_gate_pmos=None,
                                  gap_bw_mos_gates=None, array_dimension=None,

                                  # INVERTER WITH INPUT COARSE

                                  finger1_n=None, finger1_p=None,
                                  channel_width_finger1_n=None, channel_width_finger1_p=None,

                                  # INVERTER WITH INPUT FINE

                                  finger2_n=None, finger2_p=None,
                                  channel_width_finger2_n=None, channel_width_finger2_p=None,

                                  # INVERTER IN LATCH

                                  finger3_n=None, finger3_p=None,
                                  channel_width_finger3_n=None, channel_width_finger3_p=None,

                                  # MOSCAP FINE INPUTS
                                  finger_sel_p=None, finger_sel_n=None,
                                  finger_on=None,
                                  finger_moscap_p=None, finger_moscap_n=None,

                                  channel_width_sel_p=None, channel_width_sel_n=None,
                                  channel_width_on_p=None, channel_width_on_n=None,
                                  channel_width_moscap_p=None, channel_width_moscap_n=None,
                                  target_cell = 'fine'
                                  ):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        _MinSnapSpacing = drc._MinSnapSpacing

        inv_chain_inputs = dict(
            channel_length=channel_length, dummy=dummy, PCCrit=PCCrit, XVT=XVT,
            finger1_p=finger1_p, channel_width_finger1_p=channel_width_finger1_p,
            finger1_n=finger1_n, channel_width_finger1_n=channel_width_finger1_n,

            gap_bw_mos_gates=gap_bw_mos_gates,
            supply_num_coy=supply_num_coy,
            distance_to_vdd=distance_to_vdd, distance_to_vss=distance_to_vss, space_bw_gate_nmos=space_bw_gate_nmos,
            space_bw_gate_pmos=space_bw_gate_pmos,

            finger2_p=finger2_p, channel_width_finger2_p=channel_width_finger2_p,
            finger2_n=finger2_n, channel_width_finger2_n=channel_width_finger2_n,
            finger3_p=finger3_p, channel_width_finger3_p=channel_width_finger3_p,
            finger3_n=finger3_n, channel_width_finger3_n=channel_width_finger3_n,

        )
        moscap_fine_inputs = dict(
            channel_length=channel_length, dummy=dummy, PCCrit=PCCrit, XVT=XVT,

            finger_sel_p=finger_sel_p, finger_sel_n=finger_sel_n,
            finger_on=finger_on,
            finger_moscap_p=finger_moscap_p, finger_moscap_n=finger_moscap_n,
            channel_width_sel_p=channel_width_sel_p, channel_width_sel_n=channel_width_sel_n,
            channel_width_on_p=channel_width_on_p, channel_width_on_n=channel_width_on_n,
            channel_width_moscap_p=channel_width_moscap_p, channel_width_moscap_n=channel_width_moscap_n,
            target_cell=target_cell, array_dimension = array_dimension,

            gap_bw_mos_gates = gap_bw_mos_gates, supply_num_coy=supply_num_coy,
            distance_to_vdd=distance_to_vdd, distance_to_vss=distance_to_vss,
            space_bw_gate_nmos=space_bw_gate_nmos, space_bw_gate_pmos=space_bw_gate_pmos
        )

        self._DesignParameter[f'moscap_fine_array1'] = \
        self._SrefElementDeclaration(_DesignObj=MS_moscap_array.MOSCAP_ARRAY(_DesignParameter=None,
                                                                    _Name=f'moscap_fine_array1_in_{_Name}'),
                                     _Reflect = [1,0,0], _Angle = 180)[0]
        self._DesignParameter[f'moscap_fine_array2'] = \
        self._SrefElementDeclaration(_DesignObj=MS_moscap_array.MOSCAP_ARRAY(_DesignParameter=None,
                                                                    _Name=f'moscap_fine_array_in2_{_Name}'),
                                     )[0]
        self._DesignParameter[f'inv_chain1'] = \
        self._SrefElementDeclaration(_DesignObj=MS_inverter_chain.INVERTER_CHAIN(_DesignParameter=None,
                                                                    _Name=f'inv1_in_{_Name}'),
                                     )[0]
        self._DesignParameter[f'inv_chain2'] = \
        self._SrefElementDeclaration(_DesignObj=MS_inverter_chain.INVERTER_CHAIN(_DesignParameter=None,
                                                                    _Name=f'inv2_in_{_Name}'),
                                     _Reflect = [1,0,0], _Angle = 180)[0]


        self._DesignParameter[f'inv_chain1']['_DesignObj']._CalculateDesignParameter(**inv_chain_inputs)
        self._DesignParameter[f'inv_chain2']['_DesignObj']._CalculateDesignParameter(**inv_chain_inputs)
        self._DesignParameter[f'moscap_fine_array1']['_DesignObj']._CalculateDesignParameter(**moscap_fine_inputs)
        self._DesignParameter[f'moscap_fine_array2']['_DesignObj']._CalculateDesignParameter(**moscap_fine_inputs)

        self._DesignParameter['inv_chain1']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['inv_chain2']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['moscap_fine_array1']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['moscap_fine_array2']['_XYCoordinates'] = [[0, 0]]

        cell_width = (self._DesignParameter['inv_chain1']['_DesignObj'].cell_width + \
                     self._DesignParameter['moscap_fine_array1']['_DesignObj'].cell_width) * 2 + \
                     3 * drc._PolygateMinSpace

        inv_chain_x = abs(self._DesignParameter['inv_chain1']['_DesignObj'].rightmost_poly_edge) + \
                      drc._PolygateMinSpace / 2 + channel_length / 2
        moscap_fine_x = self._DesignParameter['inv_chain1']['_DesignObj'].cell_width + drc._PolygateMinSpace - channel_length / 2 + \
                    abs(self._DesignParameter['moscap_fine_array1']['_DesignObj'].leftmost_poly_edge)

        # moscap_fine1_x = 0 - cell_width / 2 + abs(self._DesignParameter['moscap_fine_array1']['_DesignObj'].rightmost_poly_edge)
        #
        # inv_chain1_x = moscap_fine1_x + drc._PolygateMinSpace - channel_length / 2 + \
        #                abs(self._DesignParameter['moscap_fine_array1']['_DesignObj'].leftmost_poly_edge) + \
        #                abs(self._DesignParameter['inv_chain1']['_DesignObj'].leftmost_poly_edge)
        #
        # inv_chain2_x = inv_chain1_x + drc._PolygateMinSpace - channel_length / 2 + \
        #                abs(self._DesignParameter['inv_chain1']['_DesignObj'].rightmost_poly_edge) + \
        #                abs(self._DesignParameter['inv_chain2']['_DesignObj'].rightmost_poly_edge)
        #
        # moscap_fine2_x = inv_chain2_x + drc._PolygateMinSpace - channel_length / 2 + \
        #                abs(self._DesignParameter['inv_chain2']['_DesignObj'].leftmost_poly_edge) + \
        #                abs(self._DesignParameter['moscap_fine_array2']['_DesignObj'].leftmost_poly_edge)


        self._DesignParameter['inv_chain1']['_XYCoordinates'] = [[-inv_chain_x, 0]]
        self._DesignParameter['inv_chain2']['_XYCoordinates'] = [[inv_chain_x, 0]]
        self._DesignParameter['moscap_fine_array1']['_XYCoordinates'] = [[-moscap_fine_x, 0]]
        self._DesignParameter['moscap_fine_array2']['_XYCoordinates'] = [[moscap_fine_x, 0]]

        """
        gate_bw_mos alignment
        """
        gap_bw_mos_gates = max(self._DesignParameter['inv_chain1']['_DesignObj'].space_bw_np_gate_centers,
                               self._DesignParameter['moscap_fine_array1']['_DesignObj'].space_bw_np_gate_centers)
        inv_chain_inputs['gap_bw_mos_gates'] = gap_bw_mos_gates
        moscap_fine_inputs['gap_bw_mos_gates'] = gap_bw_mos_gates

        """
        space_bw_mos_and_gate alignment
        """
        space_bw_gate_nmos = self._DesignParameter['moscap_fine_array1']['_DesignObj'].space_bw_gate_nmos_met1_edges
        space_bw_gate_pmos = self._DesignParameter['moscap_fine_array1']['_DesignObj'].space_bw_gate_pmos_met1_edges

        inv_chain_inputs['space_bw_gate_nmos'] = space_bw_gate_nmos - drc._Metal1MinSpace2
        moscap_fine_inputs['space_bw_gate_nmos'] = space_bw_gate_nmos - drc._Metal1MinSpace2

        inv_chain_inputs['space_bw_gate_pmos'] = space_bw_gate_pmos - drc._Metal1MinSpace2
        moscap_fine_inputs['space_bw_gate_pmos'] = space_bw_gate_pmos - drc._Metal1MinSpace2

        self._DesignParameter[f'inv_chain1']['_DesignObj']._CalculateDesignParameter(**inv_chain_inputs)
        self._DesignParameter[f'inv_chain2']['_DesignObj']._CalculateDesignParameter(**inv_chain_inputs)
        self._DesignParameter[f'moscap_fine_array1']['_DesignObj']._CalculateDesignParameter(**moscap_fine_inputs)
        self._DesignParameter[f'moscap_fine_array2']['_DesignObj']._CalculateDesignParameter(**moscap_fine_inputs)

        """
        vdd, vss rail alignment
        """
        distance_to_vdd_min = max(self._DesignParameter['inv_chain1']['_DesignObj'].distance_to_vdd,
                              self._DesignParameter['moscap_fine_array1']['_DesignObj'].distance_to_vdd)
        distance_to_vss_min = max(self._DesignParameter['inv_chain1']['_DesignObj'].distance_to_vss,
                              self._DesignParameter['moscap_fine_array1']['_DesignObj'].distance_to_vss)
        if distance_to_vdd == None:
            distance_to_vdd = distance_to_vdd_min
        else:
            if distance_to_vdd < distance_to_vdd_min:
                distance_to_vdd = distance_to_vdd_min
            else:
                pass

        if distance_to_vss == None:
            distance_to_vss = distance_to_vss_min
        else:
            if abs(distance_to_vss) < distance_to_vss_min:
                distance_to_vss = distance_to_vss_min
            else:
                pass

        inv_chain_inputs['distance_to_vdd'] = distance_to_vdd
        moscap_fine_inputs['distance_to_vdd'] = distance_to_vdd

        inv_chain_inputs['distance_to_vss'] = distance_to_vss
        moscap_fine_inputs['distance_to_vss'] = distance_to_vss

        self._DesignParameter[f'inv_chain1']['_DesignObj']._CalculateDesignParameter(**inv_chain_inputs)
        self._DesignParameter[f'inv_chain2']['_DesignObj']._CalculateDesignParameter(**inv_chain_inputs)
        self._DesignParameter[f'moscap_fine_array1']['_DesignObj']._CalculateDesignParameter(**moscap_fine_inputs)
        self._DesignParameter[f'moscap_fine_array2']['_DesignObj']._CalculateDesignParameter(**moscap_fine_inputs)

        """
        Via12 for Latch Connection Generation
        """
        self._DesignParameter['via_12_array'] = \
        self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(
            _Name='via_12_array_in_{}'.format(_Name)))[0]
        via_inputs = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        via_inputs['_ViaMet12Met2NumberOfCOX'] = 2
        via_inputs['_ViaMet12Met2NumberOfCOY'] = 1
        self._DesignParameter['via_12_array']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(
            **via_inputs)
        y_value1 = self.getXYTop('inv_chain1', 'inv3','pmos','pmos_gate_via','_Met1Layer')[0][1] - \
            self.getYWidth('via_12_array', '_Met1Layer') / 2
        x_value1 = self.getXYRight('inv_chain1', 'inv3','pmos','pmos_gate_via','_Met1Layer')[0][0] + \
                   self.getXWidth('via_12_array', '_Met1Layer') / 2

        y_value2 = self.getXYBot('inv_chain1', 'inv3','nmos','nmos_gate_via','_Met1Layer')[0][1] + \
            self.getYWidth('via_12_array', '_Met1Layer') / 2
        x_value2 = -(self.getXYRight('inv_chain1', 'inv3','nmos','nmos_gate_via','_Met1Layer')[0][0] + \
                   self.getXWidth('via_12_array', '_Met1Layer') / 2)

        via_xy = [[x_value1, y_value1], [x_value2, y_value2]]
        self._DesignParameter['via_12_array']['_XYCoordinates'] = via_xy
        """
        Routing for Latch connection
        """
        self._DesignParameter['latch_routing'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _Width=drc._MetalxMinWidth)

        path_xy = []
        ## PMOS Part

        xy_ref = self.getXYBot('inv_chain1', 'inv3', 'pmos_output_via', '_Met2Layer')[-1]
        xy_comp = self.getXY('inv_chain1', 'inv3', 'pmos', 'pmos_gate_via', '_Met1Layer')[0]
        hor_value = xy_ref[0] - xy_comp[0]
        vert_value = xy_ref[1] - xy_comp[1] + drc._MetalxMinWidth / 2

        if hor_value < vert_value :
            path_xy.append([[x_value1, y_value1], [-xy_comp[0], y_value1]])
        else:
            path_xy.append([[x_value1, y_value1], [-xy_ref[0], y_value1], [-xy_ref[0], xy_ref[1]]])

        ### NMOS Part
        xy_ref = self.getXY('inv_chain1', 'inv3', 'nmos_output_via', '_Met2Layer')[-1]
        xy_comp = self.getXY('inv_chain1', 'inv3', 'nmos', 'nmos_gate_via', '_Met1Layer')[0]
        hor_value = xy_ref[0] - xy_comp[0]
        vert_value = -(xy_ref[1] - xy_comp[1])

        if hor_value < vert_value:
            path_xy.append([[x_value2, y_value2], [xy_comp[0], y_value2]])
        else:
            path_xy.append([[x_value2, y_value2], [xy_ref[0], y_value2], [xy_ref[0], xy_ref[1]]])

        self._DesignParameter['latch_routing']['_XYCoordinates'] = path_xy

        """
        Additional Layers : Met1 & RX for Rails, SLVT Layer, BP Layer,

        """
        self._DesignParameter['additional_nxvt_layer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[f'{XVT}'][0],
            _Datatype=DesignParameters._LayerMapping[f'{XVT}'][1])
        self._DesignParameter['additional_pxvt_layer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[f'{XVT}'][0],
            _Datatype=DesignParameters._LayerMapping[f'{XVT}'][1])

        xvt_top_p = max(
            self.getXYTop('inv_chain1', 'inv1', 'pmos', 'pmos', f'_{XVT}Layer')[0][1],
            self.getXYTop('inv_chain1', 'inv2', 'pmos', 'pmos', f'_{XVT}Layer')[0][1],
            self.getXYTop('inv_chain1', 'inv3', 'pmos', 'pmos', f'_{XVT}Layer')[0][1],
            self.getXYTop('moscap_fine_array1', 'moscap_1', 'inverter_sel', 'pmos', 'pmos', f'_{XVT}Layer')[0][1],
            self.getXYTop('moscap_fine_array1', 'moscap_1', 'moscap_on', 'pmos1', 'pmos', f'_{XVT}Layer')[0][1],
            self.getXYTop('moscap_fine_array1', 'moscap_1', 'moscap_on', 'pmos2', 'pmos', f'_{XVT}Layer')[0][1])
        xvt_bot_p = min(
            self.getXYBot('inv_chain1', 'inv1', 'pmos', 'pmos', f'_{XVT}Layer')[0][1],
            self.getXYBot('inv_chain1', 'inv2', 'pmos', 'pmos', f'_{XVT}Layer')[0][1],
            self.getXYBot('inv_chain1', 'inv3', 'pmos', 'pmos', f'_{XVT}Layer')[0][1],
            self.getXYBot('moscap_fine_array1', 'moscap_1', 'inverter_sel', 'pmos', 'pmos', f'_{XVT}Layer')[0][1],
            self.getXYBot('moscap_fine_array1', 'moscap_1', 'moscap_on', 'pmos1', 'pmos', f'_{XVT}Layer')[0][1],
            self.getXYBot('moscap_fine_array1', 'moscap_1', 'moscap_on', 'pmos2', 'pmos', f'_{XVT}Layer')[0][1])

        xvt_top_n = max(
            self.getXYTop('inv_chain1', 'inv1', 'nmos', 'nmos', f'_{XVT}Layer')[0][1],
            self.getXYTop('inv_chain1', 'inv2', 'nmos', 'nmos', f'_{XVT}Layer')[0][1],
            self.getXYTop('inv_chain1', 'inv3', 'nmos', 'nmos', f'_{XVT}Layer')[0][1],
            self.getXYTop('moscap_fine_array1', 'moscap_1', 'inverter_sel', 'nmos', 'nmos', f'_{XVT}Layer')[0][1],
            self.getXYTop('moscap_fine_array1', 'moscap_1', 'moscap_on', 'nmos1', 'nmos', f'_{XVT}Layer')[0][1],
            self.getXYTop('moscap_fine_array1', 'moscap_1', 'moscap_on', 'nmos2', 'nmos', f'_{XVT}Layer')[0][1])
        xvt_bot_n = min(
            self.getXYBot('inv_chain1', 'inv1', 'nmos', 'nmos', f'_{XVT}Layer')[0][1],
            self.getXYBot('inv_chain1', 'inv2', 'nmos', 'nmos', f'_{XVT}Layer')[0][1],
            self.getXYBot('inv_chain1', 'inv3', 'nmos', 'nmos', f'_{XVT}Layer')[0][1],
            self.getXYBot('moscap_fine_array1', 'moscap_1', 'inverter_sel', 'nmos', 'nmos', f'_{XVT}Layer')[0][1],
            self.getXYBot('moscap_fine_array1', 'moscap_1', 'moscap_on', 'nmos1', 'nmos', f'_{XVT}Layer')[0][1],
            self.getXYBot('moscap_fine_array1', 'moscap_1', 'moscap_on', 'nmos2', 'nmos', f'_{XVT}Layer')[0][1])
        xvt_hor_edge = max(
            self.getXYRight('moscap_fine_array2', f'moscap_{array_dimension}', 'moscap_on', 'pmos2', 'pmos',
                            f'_{XVT}Layer')[0][0],
            self.getXYRight('moscap_fine_array2', f'moscap_{array_dimension}', 'moscap_on', 'nmos2', 'nmos',
                            f'_{XVT}Layer')[0][0]
        )
        pxvt_y_center = self.CeilMinSnapSpacing((xvt_bot_p + xvt_top_p) / 2, _MinSnapSpacing)
        nxvt_y_center = self.CeilMinSnapSpacing((xvt_bot_n + xvt_top_n) / 2, _MinSnapSpacing)

        self._DesignParameter['additional_pxvt_layer']['_XYCoordinates'] = [[0, pxvt_y_center]]
        self._DesignParameter['additional_pxvt_layer']['_XWidth'] = 2 * xvt_hor_edge
        self._DesignParameter['additional_pxvt_layer']['_YWidth'] = (xvt_top_p - xvt_bot_p)

        self._DesignParameter['additional_nxvt_layer']['_XYCoordinates'] = [[0, nxvt_y_center]]
        self._DesignParameter['additional_nxvt_layer']['_XWidth'] = 2 * xvt_hor_edge
        self._DesignParameter['additional_nxvt_layer']['_YWidth'] = (xvt_top_n - xvt_bot_n)



        self._DesignParameter['additional_bp_layer_pmos'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1])

        bp_top = max(
            self.getXYTop('inv_chain1', 'inv1', 'pmos', 'pmos', f'_PPLayer')[0][1],
            self.getXYTop('inv_chain1', 'inv2', 'pmos', 'pmos', f'_PPLayer')[0][1],
            self.getXYTop('inv_chain1', 'inv3', 'pmos', 'pmos', f'_PPLayer')[0][1],
            self.getXYTop('moscap_fine_array2', 'moscap_1', 'inverter_sel', 'pmos', 'pmos', f'_PPLayer')[0][1],
            self.getXYTop('moscap_fine_array2', 'moscap_1', 'moscap_on', 'pmos1', 'pmos', f'_PPLayer')[0][1],
            self.getXYTop('moscap_fine_array2', 'moscap_1', 'moscap_on', 'pmos2', 'pmos', f'_PPLayer')[0][1])
        bp_bot = min(
            self.getXYBot('inv_chain1', 'inv1', 'pmos', 'pmos', f'_PPLayer')[0][1],
            self.getXYBot('inv_chain1', 'inv2', 'pmos', 'pmos', f'_PPLayer')[0][1],
            self.getXYBot('inv_chain1', 'inv3', 'pmos', 'pmos', f'_PPLayer')[0][1],
            self.getXYBot('moscap_fine_array2', 'moscap_1', 'inverter_sel', 'pmos', 'pmos', f'_PPLayer')[0][1],
            self.getXYBot('moscap_fine_array2', 'moscap_1', 'moscap_on', 'pmos1', 'pmos', f'_PPLayer')[0][1],
            self.getXYBot('moscap_fine_array2', 'moscap_1', 'moscap_on', 'pmos2', 'pmos', f'_PPLayer')[0][1])
        bp_hor_edge = self.getXYRight('moscap_fine_array2', f'moscap_{array_dimension}', 'moscap_on', 'pmos2', 'pmos',
                                      f'_PPLayer')[0][0]
        bp_y_center = self.CeilMinSnapSpacing((bp_top + bp_bot) / 2, _MinSnapSpacing)
        self._DesignParameter['additional_bp_layer_pmos']['_XYCoordinates'] = [[0, bp_y_center]]
        self._DesignParameter['additional_bp_layer_pmos']['_XWidth'] = 2 * bp_hor_edge
        self._DesignParameter['additional_bp_layer_pmos']['_YWidth'] = (bp_top - bp_bot)


        distance_to_vss = self.getXY('moscap_fine_array2', f'moscap_{array_dimension}', 'moscap_on', 'vss',
                                     f'_Met1Layer')[0][1]

        self._DesignParameter['additional_bp_layer_rail'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1])

        bp_hor_edge = self.getXYRight('moscap_fine_array2', f'moscap_{array_dimension}', 'moscap_on', 'vss',
                                      f'_PPLayer')[0][0]
        bp_height = self.getYWidth('moscap_fine_array2', f'moscap_{array_dimension}', 'moscap_on', 'vss',
                                   f'_PPLayer')
        self._DesignParameter['additional_bp_layer_rail']['_XYCoordinates'] = [[0, distance_to_vss]]
        self._DesignParameter['additional_bp_layer_rail']['_XWidth'] = 2 * bp_hor_edge
        self._DesignParameter['additional_bp_layer_rail']['_YWidth'] = bp_height

        distance_to_vdd = self.getXY('moscap_fine_array2', f'moscap_{array_dimension}', 'moscap_on', 'vdd',
                                     f'_Met1Layer')[0][1]
        self._DesignParameter['additional_rx_layer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0],
            _Datatype=DesignParameters._LayerMapping['DIFF'][1])

        rx_rightmostedge = self.getXYRight('moscap_fine_array2', f'moscap_{array_dimension}', 'moscap_on', 'vss',
                                           f'_ODLayer')[0][0]
        rx_height = self.getYWidth('moscap_fine_array2', f'moscap_{array_dimension}', 'moscap_on', 'vdd',
                                   f'_ODLayer')
        self._DesignParameter['additional_rx_layer']['_XWidth'] = 2 * rx_rightmostedge
        self._DesignParameter['additional_rx_layer']['_YWidth'] = rx_height
        self._DesignParameter['additional_rx_layer']['_XYCoordinates'] = [[0, distance_to_vss], [0, distance_to_vdd]]

        self._DesignParameter['additional_met1_layer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1])

        met1_rightmostedge = self.getXYRight('moscap_fine_array2', f'moscap_{array_dimension}', 'moscap_on', 'vss',
                                             f'_Met1Layer')[0][0]
        met1_height = self.getYWidth('moscap_fine_array2', f'moscap_{array_dimension}', 'moscap_on', 'vdd',
                                     f'_Met1Layer')

        self._DesignParameter['additional_met1_layer']['_XWidth'] = 2 * met1_rightmostedge
        self._DesignParameter['additional_met1_layer']['_YWidth'] = met1_height
        self._DesignParameter['additional_met1_layer']['_XYCoordinates'] = [[0, distance_to_vdd], [0, distance_to_vss]]

        self._DesignParameter['additional_nwell_layer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1])

        nw_top = max(self.getXYTop('moscap_fine_array2', 'moscap_1', 'moscap_on', 'nwell')[0][1],
                     self.getXYTop('moscap_fine_array2', 'moscap_1', 'inverter_sel', 'nwell')[0][1])

        nw_hor_edge = self.getXYRight('moscap_fine_array2', f'moscap_{array_dimension}', 'moscap_on', 'nwell')[0][0]

        nw_y_center = self.FloorMinSnapSpacing((nw_top + xvt_bot_p) / 2, _MinSnapSpacing)
        self._DesignParameter['additional_nwell_layer']['_XYCoordinates'] = [[0, nw_y_center]]
        self._DesignParameter['additional_nwell_layer']['_XWidth'] = 2 * nw_hor_edge
        self._DesignParameter['additional_nwell_layer']['_YWidth'] = (nw_top - xvt_bot_p)

if __name__ == '__main__':
    Obj = MOSCAP_FINE_FULL()
    import random
    import time
    cnt = 1
    for i in range(0,1):
        print("Generating Random Input Variables...")
        time.sleep(5)

        channel_length = random.randrange(30,100, 10)
        finger_sel_p = random.randrange(1, 9, 1)
        finger_sel_n= random.randrange(1, 9, 1)
        finger_on= random.randrange(1, 9, 1)
        finger_moscap_p= random.randrange(1, 9, 1)
        finger_moscap_n= random.randrange(1, 9, 1)

        finger1_n= random.randrange(1, 9, 1)
        finger1_p= random.randrange(1, 9, 1)
        finger2_n= random.randrange(1, 9, 1)
        finger2_p= random.randrange(1, 9, 1)
        finger3_n= random.randrange(1, 9, 1)
        finger3_p= random.randrange(1, 9, 1)

        channel_width_sel_p= random.randrange(400,1350,50)
        channel_width_sel_n= random.randrange(200,650,50)
        channel_width_on_p= random.randrange(400,1350,50)
        channel_width_on_n= random.randrange(200,650,50)
        channel_width_moscap_p= random.randrange(400,1350,50)
        channel_width_moscap_n= random.randrange(200,650,50)

        channel_width_finger1_n= random.randrange(200,650,50)
        channel_width_finger1_p= random.randrange(400,1350,50)
        channel_width_finger2_n= random.randrange(200,650,50)
        channel_width_finger2_p= random.randrange(400,1350,50)
        channel_width_finger3_n= random.randrange(200,650,50)
        channel_width_finger3_p= random.randrange(400,1350,50)

        supply_num_coy= random.randrange(1,5,1)



        gap_bw_mos_gates= random.randrange(100,1800,50)
        array_dimension = random.randrange(2, 8, 1)

        print("Waiting For 10 seconds before Calculation initialization...")
        time.sleep(10)

        Obj._CalculateDesignParameter(
            channel_length=channel_length, dummy='True', PCCrit='True', XVT='SLVT',
            supply_num_coy=supply_num_coy,
            distance_to_vdd=None, distance_to_vss=None,
            space_bw_gate_nmos=None, space_bw_gate_pmos=None,
            gap_bw_mos_gates=gap_bw_mos_gates, array_dimension=array_dimension,

            # INVERTER WITH INPUT COARSE

            finger1_n=finger1_n, finger1_p=finger1_p,
            channel_width_finger1_n=channel_width_finger1_n, channel_width_finger1_p=channel_width_finger1_p,

            # INVERTER WITH INPUT FINE

            finger2_n=finger2_n, finger2_p=finger2_p,
            channel_width_finger2_n=channel_width_finger2_n, channel_width_finger2_p=channel_width_finger2_p,

            # INVERTER IN LATCH

            finger3_n=finger3_n, finger3_p=finger3_p,
            channel_width_finger3_n=channel_width_finger3_n, channel_width_finger3_p=channel_width_finger3_p,

            # MOSCAP FINE INPUTS
            finger_sel_p=finger_sel_p, finger_sel_n=finger_sel_n,
            finger_on=finger_on,
            finger_moscap_p=finger_moscap_p, finger_moscap_n=finger_moscap_n,

            channel_width_sel_p=channel_width_sel_p, channel_width_sel_n=channel_width_sel_n,
            channel_width_on_p=channel_width_on_p, channel_width_on_n=channel_width_on_n,
            channel_width_moscap_p=channel_width_moscap_p, channel_width_moscap_n=channel_width_moscap_n,

        )


        Obj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=Obj._DesignParameter)
        _fileName = 'MS_moscap_fine_full.gds'
        testStreamFile = open('./MS_moscap_fine_full.gds', 'wb')
        tmp = Obj._CreateGDSStream(Obj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        import ftplib

        ftp = ftplib.FTP('141.223.29.62')
        ftp.login('kms95', 'dosel545')
        ftp.cwd('/mnt/sdb/kms95/OPUS/ss28')
        myfile = open('MS_moscap_fine_full.gds', 'rb')
        ftp.storbinary('STOR MS_moscap_fine_full.gds', myfile)
        myfile.close()
        ftp.close()

        # import DRCchecker
        #
        # _DRC = DRCchecker.DRCchecker('kms95','dosel545','/mnt/sdb/kms95/OPUS/ss28','/mnt/sdb/kms95/OPUS/ss28/DRC/run',
        #                              'MS_moscap_fine_full','MS_moscap_fine_full')
        # print(f"Count of Loop : {cnt}")
        # _DRC.DRCchecker()

        print("Waiting For 10 seconds before another loop....")
        cnt = cnt + 1
        time.sleep(10)

