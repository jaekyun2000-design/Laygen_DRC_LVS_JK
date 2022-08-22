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

class INVERTER_SEL(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict( channel_length=None, dummy=None, PCCrit=None, XVT=None,
                                            finger1=None, channel_width1=None,
                                            finger2=None, channel_width2=None,
                                            supply_num_coy = None, supply_num_cox = None,
                                            distance_to_vdd = None, distance_to_vss = None,
                                            space_bw_gate_nmos = None, space_bw_gate_pmos = None
                                           )
    def __init__(self, _DesignParameter=None, _Name='MS_inverter_sel'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter(self,
                                  channel_length=None, dummy=None, PCCrit=None, XVT=None,
                                  finger1=None, channel_width1=None,
                                  finger2=None, channel_width2=None,

                                  gap_bw_mos_gates=None,
                                  supply_num_coy=None, supply_num_cox=None,
                                  distance_to_vdd=None, distance_to_vss=None, space_bw_gate_nmos = None,
                                  space_bw_gate_pmos=None
                                  ):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        _MinSnapSpacing=drc._MinSnapSpacing

        nmos_inputs = copy.deepcopy(NMOSWithGate._NMOS._ParametersForDesignCalculation)
        nmos_inputs['finger'] = finger2
        nmos_inputs['channel_width'] = channel_width2
        nmos_inputs['channel_length'] = channel_length
        nmos_inputs['dummy'] = dummy
        nmos_inputs['PCCrit'] = PCCrit
        nmos_inputs['XVT'] = XVT

        if space_bw_gate_nmos != None:
            nmos_inputs['space_bw_gate_nmos'] = space_bw_gate_nmos
        if finger2 == 1:
            nmos_inputs['gate_option'] = 'rotate'

        pmos_inputs = copy.deepcopy(PMOSWithGate._PMOS._ParametersForDesignCalculation)
        pmos_inputs['finger'] = finger1
        pmos_inputs['channel_width'] = channel_width1
        pmos_inputs['channel_length'] = channel_length
        pmos_inputs['dummy'] = dummy
        pmos_inputs['PCCrit'] = PCCrit
        pmos_inputs['XVT'] = XVT
        if space_bw_gate_pmos != None:
            pmos_inputs['space_bw_gate_pmos'] = space_bw_gate_pmos
        if finger1 == 1:
            pmos_inputs['gate_option'] = 'rotate'

        self._DesignParameter['nmos'] = self._SrefElementDeclaration(_DesignObj=NMOSWithGate._NMOS(_DesignParameter=None,
                                                                        _Name='nmos_in_{}'.format(_Name)))[0]
        self._DesignParameter['pmos'] = self._SrefElementDeclaration(_DesignObj=PMOSWithGate._PMOS(_DesignParameter=None,
                                                                        _Name='pmos_in_{}'.format(_Name)))[0]

        self._DesignParameter['nmos']['_DesignObj']._CalculateDesignParameter(**nmos_inputs)
        self._DesignParameter['pmos']['_DesignObj']._CalculateDesignParameter(**pmos_inputs)
        self._DesignParameter['nmos']['_XYCoordinates'] = [[0, 0]]     # tmp value
        self._DesignParameter['pmos']['_XYCoordinates'] = [[0, 0]]     # tmp value


        gap_bw_mos_gates_min =2 * drc._Metal1MinSpace + 3 * self.getYWidth('nmos', 'nmos_gate_via', '_Met1Layer')
        if gap_bw_mos_gates == None:
            gap_bw_mos_gates = gap_bw_mos_gates_min
        else:
            if gap_bw_mos_gates < gap_bw_mos_gates_min:
                warnings.warn(f"gap_bw_mos_gates minimum value is {gap_bw_mos_gates_min}")
                gap_bw_mos_gates = gap_bw_mos_gates_min
            else:
                pass
        nmos_y_value =  self.CeilMinSnapSpacing(0 - gap_bw_mos_gates/2 -\
                        self._DesignParameter['nmos']['_DesignObj'].offset_value, _MinSnapSpacing)
        pmos_y_value =  self.CeilMinSnapSpacing(0 + gap_bw_mos_gates/2 +\
                        self._DesignParameter['pmos']['_DesignObj'].offset_value, _MinSnapSpacing)

        self._DesignParameter['nmos']['_XYCoordinates'] = [[0, nmos_y_value]]
        self._DesignParameter['pmos']['_XYCoordinates'] = [[0, pmos_y_value]]


        """
        Output via generation & Coordinate Settings
        """

        via_code_pmos_output = utility.functions.create_output_via(self,_Name = _Name,
                                                       via_name = 'pmos_output_via',
                                                       hierarchy_list = ['pmos','pmos'],
                                                       mos_type = 'pmos')

        via_code_nmos_output = utility.functions.create_output_via(self,_Name = _Name,
                                                       via_name = 'nmos_output_via',
                                                       hierarchy_list = ['nmos','nmos'],
                                                       mos_type = 'nmos')

        exec(via_code_pmos_output)
        exec(via_code_nmos_output)
        cnt = 1
        while(1):
            cnt = cnt + 1
            drc_test2 = self.getXYBot('nmos','nmos_gate_via', '_Met1Layer')[0][1] -\
                        self.getXYTop('nmos_output_via', '_Met1Layer')[0][1]
            if drc_test2 < drc._Metal1MinSpace2:
                calibre_value = drc._Metal1MinSpace2 - drc_test2
                del self._DesignParameter['nmos_output_via']
                calibre_for_input =self.CeilMinSnapSpacing(\
                    self._DesignParameter['nmos']['_DesignObj'].offset_value +\
                    calibre_value - (self.getYWidth('nmos', 'nmos', '_Met1Layer')/2 + self.getYWidth('nmos', 'nmos_gate_via',
                                                    '_Met1Layer')/2), _MinSnapSpacing)
                nmos_inputs['space_bw_gate_nmos'] = calibre_for_input
                self._DesignParameter['nmos']['_DesignObj']._CalculateDesignParameter(**nmos_inputs)

                nmos_y_value =  self.FloorMinSnapSpacing(0 - gap_bw_mos_gates / 2 - \
                                self._DesignParameter['nmos']['_DesignObj'].offset_value, _MinSnapSpacing)
                self._DesignParameter['nmos']['_XYCoordinates'] = [[0, nmos_y_value]]
                via_code_nmos_output = utility.functions.create_output_via(self, _Name=_Name,
                                                                            via_name='nmos_output_via',
                                                                            hierarchy_list=['nmos', 'nmos'],
                                                                            mos_type='nmos')
                exec(via_code_nmos_output)
            else:
                break
            if cnt > 2:
                raise Exception("DRC calibration failed")
                break

        """
        Output via Routing
        """

        routing_code_nmos_output = utility.functions.create_output_routing(self, path_name = 'nmos_output_routing',
                                                                       via_name = 'nmos_output_via',
                                                                       width = None,
                                                                       routing_option = 'top')

        routing_code_pmos_output = utility.functions.create_output_routing(self, path_name = 'pmos_output_routing',
                                                                       via_name = 'pmos_output_via',
                                                                       width = None,
                                                                       routing_option = 'bottom')
        exec(routing_code_pmos_output + routing_code_nmos_output)


        """
        Output Routing
        """
        self._DesignParameter['output_routing'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _Width=drc._MetalxMinWidth)
        tmp1 = self.getXY('pmos_output_via','_Met2Layer')[-1][0]
        tmp2= self.getXY('nmos_output_via', '_Met2Layer')[-1][0]

        x_value = min(tmp1,tmp2)
        source_y = self._DesignParameter['pmos_output_routing']['_XYCoordinates'][0][-1][1]
        target_y= self._DesignParameter['nmos_output_routing']['_XYCoordinates'][0][-1][1]
        output_path =[[tmp1, source_y], [x_value, source_y],[x_value, target_y],[tmp2, target_y]]
        self._DesignParameter['output_routing']['_XYCoordinates'] = [output_path]
        x_value_output = x_value

        """
        Input Routing
        """
        self._DesignParameter['input_routing'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1])

        min_cox = min(len(self.getXY('nmos', 'nmos_gate_via','_COLayer')),
                      len(self.getXY('pmos', 'pmos_gate_via','_COLayer')))

        routing_path_level = min_cox // 3
        if routing_path_level == 0:
            routing_path_level = 1
        self._DesignParameter['input_routing']['_Width'] = drc._Metal1MinWidth * routing_path_level
        if finger1 == 1:
            self._DesignParameter['input_routing']['_Width'] = self.getXWidth('pmos', 'pmos_gate_via', '_Met1Layer')
        x_value = self.getXY('pmos','pmos_gate_via', '_Met1Layer')[0][0]
        y_value_n = self.getXY('nmos', 'nmos_gate_via', '_Met1Layer')[0][1]
        y_value_p = self.getXY('pmos', 'pmos_gate_via', '_Met1Layer')[0][1]
        if finger1 != 1:
            if abs(x_value - x_value_output) < drc._MetalxMinWidth * 2:
                calibre_value = 2 * drc._MetalxMinWidth - abs(x_value - x_value_output)
                x_value = x_value - calibre_value
                y_value_n = self.getXY('nmos', 'nmos_gate_via', '_Met1Layer')[0][1] - \
                            self.getYWidth('nmos', 'nmos_gate_via', '_Met1Layer') / 2
                y_value_p = self.getXY('pmos', 'pmos_gate_via', '_Met1Layer')[0][1] + \
                            self.getYWidth('pmos', 'pmos_gate_via', '_Met1Layer') / 2
        path_inputs = [[[x_value, y_value_n],[x_value, y_value_p]]]
        self._DesignParameter['input_routing']['_XYCoordinates'] = path_inputs


        """
        Supply Rail Generation
        """
        self._DesignParameter['vss'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(
            _DesignParameter=None, _Name='vss_in_{}'.format(_Name)))[0]
        self._DesignParameter['vdd'] = self._SrefElementDeclaration(_DesignObj=NbodyContact._NbodyContact(
            _DesignParameter=None, _Name='vdd_in_{}'.format(_Name)))[0]

        vss_inputs = copy.deepcopy(PbodyContact._PbodyContact._ParametersForDesignCalculation)
        vdd_inputs = copy.deepcopy(NbodyContact._NbodyContact._ParametersForDesignCalculation)

        if (supply_num_coy != None) and (supply_num_cox >= 1):
            vss_inputs['_NumberOfPbodyCOY'] = supply_num_coy
            vdd_inputs['_NumberOfNbodyCOY'] = supply_num_coy
        else:
            vss_inputs['_NumberOfPbodyCOY'] = 2
            vdd_inputs['_NumberOfNbodyCOY'] = 2

        # num_cox minimum value calculation

        tmp_num_for_supply = 1  # Final COX Value
        rightmost_edge = max(self.getXY('pmos','pmos','_PODummyLayer')[-1][0],
                             self.getXY('nmos','nmos','_PODummyLayer')[-1][0])
        leftmost_edge = min(self.getXY('pmos','pmos','_PODummyLayer')[0][0],
                            self.getXY('nmos','nmos','_PODummyLayer')[0][0])

        cell_width = rightmost_edge - leftmost_edge
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

        if (supply_num_cox != None) and (tmp_num_for_supply < supply_num_cox):
            vss_inputs['_NumberOfPbodyCOX'] = supply_num_cox
            vdd_inputs['_NumberOfNbodyCOX'] = supply_num_cox
            self._DesignParameter['vss']['_DesignObj']._CalculatePbodyContactDesignParameter(**vss_inputs)
            self._DesignParameter['vdd']['_DesignObj']._CalculateNbodyContactDesignParameter(**vdd_inputs)

        lower_met1_bound = self.FloorMinSnapSpacing(\
            min(self.getXY('nmos','nmos','_Met1Layer')[0][1] - self.getYWidth('nmos','nmos','_Met1Layer')/2,
                self.getXY('nmos_output_via','_Met1Layer')[0][1] - self.getYWidth('nmos_output_via','_Met1Layer')/2), _MinSnapSpacing)
        higher_met1_bound = self.CeilMinSnapSpacing(\
            self.getXY('pmos','pmos','_Met1Layer')[0][1] + self.getYWidth('pmos','pmos','_Met1Layer')/2 , _MinSnapSpacing)

        vss_y_value = self.FloorMinSnapSpacing(\
            lower_met1_bound - self.getYWidth('vss','_Met1Layer')/2 - drc._Metal1MinSpace3, _MinSnapSpacing)
        vdd_y_value = self.CeilMinSnapSpacing(\
            higher_met1_bound + self.getYWidth('vdd', '_Met1Layer') / 2 + drc._Metal1MinSpace3, _MinSnapSpacing)

        drc_poly1 = vdd_y_value - self.getYWidth('vdd', '_Met1Layer') / 2 - \
                    (self.getXYTop('pmos', 'pmos', '_POLayer')[0][1] + drc._PolygateMinSpace2OD)
        drc_poly2 = (self.getXYBot('nmos', 'nmos', '_POLayer')[0][1] - drc._PolygateMinSpace2OD) - \
                    (vss_y_value + self.getYWidth('vss', '_Met1Layer') / 2)
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
            if (distance_to_vdd != None) and (distance_to_vdd < vdd_y_value):
                distance_to_vdd = vdd_y_value
        else:
            distance_to_vdd = vdd_y_value



        self._DesignParameter['vss']['_XYCoordinates'] = [[0, distance_to_vss]]
        self._DesignParameter['vdd']['_XYCoordinates'] = [[0, distance_to_vdd]]

        """
        Additional Poly Dummy, NWELL Generation
        """
        if dummy:
            dummy1 = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']
            source1 = self.getXYTop('nmos', 'nmos', '_PODummyLayer')
            poly_min_y_value = math.ceil(drc._PODummyMinArea / dummy1['_XWidth'])

            if dummy1['_XWidth'] * dummy1['_YWidth'] < drc._PODummyMinArea:
                self._DesignParameter['additional_poly1'] = self._PathElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['POLY'][0],
                    _Datatype=DesignParameters._LayerMapping['POLY'][1],
                    _Width=dummy1['_XWidth'])
                self._DesignParameter['additional_poly1']['_XYCoordinates'] = [
                    [source1[0], [source1[0][0], source1[0][1] - poly_min_y_value]],
                    [source1[1], [source1[1][0], source1[1][1] - poly_min_y_value]]]
            pc_bot = source1[0][1] - poly_min_y_value

            drc_test3 = pc_bot - self.getXYTop('vss','_Met1Layer')[0][1] - drc._PolygateMinSpace2OD
            if drc_test3 < 0:
                calibre_value = abs(drc_test3)
                vss_y_value = vss_y_value - calibre_value
                self._DesignParameter['vss']['_XYCoordinates'] = [[0, vss_y_value]]

        self._DesignParameter['nwell'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1])

        nwell_bot = self.getXYBot('pmos', 'pmos', f'_{XVT}Layer')[0][1]
        nwell_top = self.getXYTop('vdd', '_ODLayer')[0][1] + drc._NwMinEnclosurePactive2
        nwell_left = self.getXYLeft('vdd', '_ODLayer')[0][0] - drc._NwMinEnclosurePactive2* 2
        nwell_right = self.getXYRight('vdd', '_ODLayer')[0][0] + drc._NwMinEnclosurePactive2* 2
        nwell_y_center = self.CeilMinSnapSpacing((nwell_top + nwell_bot) / 2, _MinSnapSpacing)
        nwell_x_center = self.CeilMinSnapSpacing((nwell_left + nwell_right) / 2, _MinSnapSpacing)
        nwell_xwidth = nwell_right - nwell_left
        nwell_ywidth = nwell_top - nwell_bot
        self._DesignParameter['nwell']['_XYCoordinates'] = [[nwell_x_center, nwell_y_center]]
        self._DesignParameter['nwell']['_XWidth'] = nwell_xwidth
        self._DesignParameter['nwell']['_YWidth'] = nwell_ywidth


        """
        Supply VSS VDD Routing
        """
        nmos_supply_points = self.getXY('nmos', 'nmos', '_XYCoordinateNMOSSupplyRouting')
        pmos_supply_points = self.getXY('pmos', 'pmos', '_XYCoordinatePMOSSupplyRouting')

        self._DesignParameter['supply_routing'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _Width=drc._Metal1MinWidth)
        supply_path = []
        for i in range(len(nmos_supply_points)):
            supply_path.append([[nmos_supply_points[i][0],nmos_supply_points[0][1]], [nmos_supply_points[i][0], distance_to_vss]])
        for i in range(len(pmos_supply_points)):
            supply_path.append([[pmos_supply_points[i][0], pmos_supply_points[0][1]],[pmos_supply_points[i][0], distance_to_vdd]])
        self._DesignParameter['supply_routing']['_XYCoordinates'] = supply_path

        self.space_bw_gate_nmos_met1_edges = self.getXYBot('nmos', 'nmos_gate_via', '_Met1Layer')[0][1] -\
            self.getXYTop('nmos', 'nmos', '_Met1Layer')[0][1]
        self.space_bw_gate_pmos_met1_edges = abs(self.getXYTop('pmos', 'pmos_gate_via', '_Met1Layer')[0][1] -\
            self.getXYBot('pmos', 'pmos', '_Met1Layer')[0][1])

        self.space_bw_np_gate_centers = self.getXY('pmos','pmos','_Met1Layer')[0][1] - \
                                        self.getXY('nmos', 'nmos', '_Met1Layer')[0][1] - \
                                        self._DesignParameter['nmos']['_DesignObj'].offset_value - \
                                        self._DesignParameter['pmos']['_DesignObj'].offset_value

        self.distance_to_vdd = self._DesignParameter['vdd']['_XYCoordinates'][0][1]
        self.distance_to_vss = abs(self._DesignParameter['vss']['_XYCoordinates'][0][1])

        self.leftmost_poly_edge = min(self.getXYLeft('nmos','nmos','_PODummyLayer')[0][0],
                                      self.getXYLeft('pmos','pmos', '_PODummyLayer')[0][0])
        self.rightmost_poly_edge = max(self.getXYRight('nmos','nmos','_PODummyLayer')[-1][0],
                                      self.getXYRight('pmos','pmos', '_PODummyLayer')[-1][0])
        self.cell_width = self.rightmost_poly_edge - self.leftmost_poly_edge

        # self._DesignParameter['additional_xvt_layer'] = self._BoundaryElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping[f'{XVT}'][0],
        #     _Datatype=DesignParameters._LayerMapping[f'{XVT}'][1])
        # if



if __name__ == '__main__':
    for i in range(10):
        import random

        # gate_options = ['left', 'right', 'rotate']
        # gate_option = random.choice(gate_options)
        finger1 = random.randrange(1, 2, 1)
        finger2 = random.randrange(1, 2, 1)

        # finger_on_p = random.randrange(1, 11, 1)
        # finger_coarse_p1 = random.randrange(1, 11, 1)
        # finger_coarse_p2 = random.randrange(1, 11, 1)
        # finger_coarse_n1 = random.randrange(1, 11, 1)
        # finger_coarse_n2 = random.randrange(1, 11, 1)
        # finger_fine_p1 = random.randrange(1, 11, 1)
        # finger_fine_p2 = random.randrange(1, 11, 1)
        # finger_fine_n1 = random.randrange(1, 11, 1)
        # finger_fine_n2 = random.randrange(1, 11, 1)
        #
        # finger_out_n = random.randrange(1, 11, 1)
        # finger_out_p = random.randrange(1, 11, 1)

        channel_width1 = random.randrange(400, 850, 50)
        channel_width2 = random.randrange(200, 850, 50)
        # channel_width_coarse_n1 = random.randrange(200, 650, 50)
        # channel_width_coarse_n2 = random.randrange(200, 650, 50)
        # channel_width_fine_n1 = random.randrange(200, 650, 50)
        # channel_width_fine_n2 = random.randrange(200, 650, 50)
        # channel_width_out_n = random.randrange(200, 650, 50)

        # channel_width_on_p = random.randrange(400, 1350, 50)
        # channel_width_coarse_p1 = random.randrange(400, 1350, 50)
        # channel_width_coarse_p2 = random.randrange(400, 1350, 50)
        # channel_width_fine_p1 = random.randrange(400, 1350, 50)
        # channel_width_fine_p2 = random.randrange(400, 1350, 50)
        # channel_width_out_p = random.randrange(400, 1350, 50)

        space_bw_gate_nmos = random.randrange(0, 100, 2)
        # supply_num_coy = random.randrange(1, 5, 1)
        # coarse_fine_dimension = random.randrange(2, 8, 1)
        dummy = random.randrange(0, 2, 1)
        channel_length = random.randrange(30, 100, 2)

        Obj = INVERTER_SEL()
        Obj._CalculateDesignParameter(channel_length=channel_length, dummy=dummy, PCCrit=True, XVT='SLVT',
                                      finger1=finger1, channel_width1=channel_width1,
                                      finger2=finger2, channel_width2=channel_width2,space_bw_gate_nmos = space_bw_gate_nmos
                                      )

        Obj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=Obj._DesignParameter)
        _fileName = 'MS_inverter_sel.gds'
        testStreamFile = open('./MS_inverter_sel.gds', 'wb')
        tmp = Obj._CreateGDSStream(Obj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        import ftplib

        ftp = ftplib.FTP('141.223.29.62')
        ftp.login('kms95', 'dosel545')
        ftp.cwd('/mnt/sdb/kms95/OPUS/ss28')
        myfile = open('MS_inverter_sel.gds', 'rb')
        ftp.storbinary('STOR MS_inverter_sel.gds', myfile)
        myfile.close()
        ftp.close()

        import DRCchecker

        _DRC = DRCchecker.DRCchecker('kms95', 'dosel545', '/mnt/sdb/kms95/OPUS/ss28', '/mnt/sdb/kms95/OPUS/ss28/DRC/run',
                                     'MS_inverter_sel', 'MS_inverter_sel')
        _DRC.DRCchecker()