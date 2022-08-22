from generatorLib import DRC
from generatorLib.generator_models import NbodyContact
from generatorLib.generator_models import PbodyContact
from generatorLib.generator_models import PMOSWithGate
from generatorLib.generator_models import NMOSWithGate
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import MS_moscap_on
from generatorLib.generator_models import MS_inv_sel
from generatorLib import StickDiagram
from generatorLib import DesignParameters

import copy, math, warnings

class MOSCAP_COARSE_FINE(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(channel_length=None, dummy=None, PCCrit=None, XVT=None,
                                           finger_sel_p=None, finger_sel_n=None,
                                           finger_on = None,
                                           finger_moscap_p = None, finger_moscap_n = None,

                                           channel_width_sel_p = None, channel_width_sel_n = None,
                                           channel_width_on_p = None, channel_width_on_n = None,
                                           channel_width_moscap_p = None, channel_width_moscap_n = None,


                                           supply_num_coy=None, supply_num_cox=None,
                                           distance_to_vdd=None, distance_to_vss=None,
                                           space_bw_gate_nmos=None, space_bw_gate_pmos=None,
                                           gap_bw_mos_gates=None, target_cell = None
                                           )
    def __init__(self, _DesignParameter=None, _Name='MS_moscap_coarse_fine'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter(self,
                                  channel_length=None, dummy=None, PCCrit=None, XVT=None,
                                  finger_sel_p=None, finger_sel_n=None,
                                  finger_on=None,
                                  finger_moscap_p=None, finger_moscap_n=None,

                                  channel_width_sel_p=None, channel_width_sel_n=None,
                                  channel_width_on_p=None, channel_width_on_n=None,
                                  channel_width_moscap_p=None, channel_width_moscap_n=None,

                                  supply_num_coy=None, supply_num_cox=None,
                                  distance_to_vdd=None, distance_to_vss=None,
                                  space_bw_gate_nmos=None, space_bw_gate_pmos=None,
                                  gap_bw_mos_gates=None, target_cell = None
                                  ):
        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        _MinSnapSpacing = drc._MinSnapSpacing

        self._DesignParameter['inverter_sel'] = \
        self._SrefElementDeclaration(_DesignObj=MS_inv_sel.INVERTER_SEL(_DesignParameter=None,
                                                                    _Name=f'inverter_sel_in_{_Name}'))[0]
        self._DesignParameter['moscap_on'] = \
        self._SrefElementDeclaration(_DesignObj=MS_moscap_on.MOSCAP_ON(_DesignParameter=None,
                                                                    _Name=f'moscap_on_in_{_Name}'))[0]
        inv_sel_input = dict(
            channel_length=channel_length, dummy=dummy, PCCrit=PCCrit, XVT=XVT,
            finger1=finger_sel_p, channel_width1=channel_width_sel_p,
            finger2=finger_sel_n, channel_width2=channel_width_sel_n, space_bw_gate_nmos=space_bw_gate_nmos,
            supply_num_coy=supply_num_coy, space_bw_gate_pmos=space_bw_gate_pmos,
            distance_to_vdd=distance_to_vdd, distance_to_vss=distance_to_vss, gap_bw_mos_gates=gap_bw_mos_gates
            )
        moscap_on_input =dict(
            channel_length=channel_length, dummy=dummy, PCCrit=PCCrit, XVT=XVT,
            finger_on=finger_on, channel_width1=channel_width_on_p,
            finger2=finger_moscap_p, channel_width2=channel_width_moscap_p,
            channel_width3=channel_width_on_n,
            finger4=finger_moscap_n, channel_width4=channel_width_moscap_n,
            supply_num_coy=supply_num_coy, space_bw_gate_nmos=space_bw_gate_nmos, space_bw_gate_pmos=space_bw_gate_pmos,
            distance_to_vdd = distance_to_vdd, distance_to_vss=distance_to_vss, gap_bw_mos_gates=gap_bw_mos_gates
            )
        self._DesignParameter['inverter_sel']['_DesignObj']._CalculateDesignParameter(**inv_sel_input)
        self._DesignParameter['moscap_on']['_DesignObj']._CalculateDesignParameter(**moscap_on_input)

        self._DesignParameter['inverter_sel']['_XYCoordinates'] = [[0, 0]]  # tmp value
        self._DesignParameter['moscap_on']['_XYCoordinates'] = [[0, 0]]  # tmp value

        moscap_cell_width = self._DesignParameter['moscap_on']['_DesignObj'].cell_width
        inv_sel_cell_width = self._DesignParameter['inverter_sel']['_DesignObj'].cell_width

        cell_width = inv_sel_cell_width + moscap_cell_width + drc._PolygateMinSpace

        inv_sel_x_value = 0 - self.CeilMinSnapSpacing(cell_width / 2, _MinSnapSpacing) + self.FloorMinSnapSpacing(
            inv_sel_cell_width / 2., _MinSnapSpacing)
        moscap_cell_x_value = 0 + self.CeilMinSnapSpacing(cell_width / 2, _MinSnapSpacing) - \
                              self._DesignParameter['moscap_on']['_DesignObj'].rightmost_poly_edge


        self._DesignParameter['inverter_sel']['_XYCoordinates'] = [[inv_sel_x_value, 0]]
        self._DesignParameter['moscap_on']['_XYCoordinates'] = [[moscap_cell_x_value, 0]]

        """
        via12 generation for inv_sel output & sel_b input
        """

        self._DesignParameter['via_sel_b'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(
            _Name='ViaMet12Met2OnNMOSOutputIn{}'.format(_Name)))[0]
        via_inputs = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        via_inputs['_ViaMet12Met2NumberOfCOX'] = 1
        via_inputs['_ViaMet12Met2NumberOfCOY'] = 2
        self._DesignParameter['via_sel_b']['_DesignObj']._CalculateDesignParameterSameEnclosure(
            **via_inputs)

        via_x_value = (self.getXY('inverter_sel','pmos', 'pmos', '_Met1Layer')[-1][0] +
            self.getXY('moscap_on', 'pmos1', 'pmos', '_Met1Layer')[0][0]) // 2
        if target_cell == 'fine':
            via_y_value = self.getXYTop('inverter_sel', 'pmos', 'pmos_gate_via', '_Met1Layer')[0][1] - \
                self.getYWidth('via_sel_b', '_Met1Layer') / 2
        else:
            via_y_value = self.getXY('inverter_sel', 'pmos', 'pmos_gate_via', '_Met1Layer')[0][1]
        self._DesignParameter['via_sel_b']['_XYCoordinates'] = [[via_x_value, via_y_value]]

        """
        gate_bw_mos alignment
        """
        gap_bw_mos_gates = max(self._DesignParameter['inverter_sel']['_DesignObj'].space_bw_np_gate_centers,
                               self._DesignParameter['moscap_on']['_DesignObj'].space_bw_np_gate_centers)
        inv_sel_input['gap_bw_mos_gates'] = gap_bw_mos_gates
        moscap_on_input['gap_bw_mos_gates'] = gap_bw_mos_gates
        """
        space_bw_mos_and_gate alignment
        """
        space_bw_gate_nmos = max(self._DesignParameter['inverter_sel']['_DesignObj'].space_bw_gate_nmos_met1_edges,
                                 self._DesignParameter['moscap_on']['_DesignObj'].space_bw_gate_nmos_met1_edges)
        space_bw_gate_pmos = max(self._DesignParameter['inverter_sel']['_DesignObj'].space_bw_gate_pmos_met1_edges,
                                 self._DesignParameter['moscap_on']['_DesignObj'].space_bw_gate_pmos_met1_edges)

        inv_sel_input['space_bw_gate_nmos'] = space_bw_gate_nmos - drc._Metal1MinSpace2
        moscap_on_input['space_bw_gate_nmos'] = space_bw_gate_nmos - drc._Metal1MinSpace2
        inv_sel_input['space_bw_gate_pmos'] = space_bw_gate_pmos - drc._Metal1MinSpace2
        moscap_on_input['space_bw_gate_pmos'] = space_bw_gate_pmos - drc._Metal1MinSpace2

        self._DesignParameter['inverter_sel']['_DesignObj']._CalculateDesignParameter(**inv_sel_input)
        self._DesignParameter['moscap_on']['_DesignObj']._CalculateDesignParameter(**moscap_on_input)



        """
        vdd, vss rail alignment
        """

        if distance_to_vdd == None:
            distance_to_vdd = max(self._DesignParameter['inverter_sel']['_DesignObj'].distance_to_vdd,
                                  self._DesignParameter['moscap_on']['_DesignObj'].distance_to_vdd)
        if distance_to_vss == None:
            distance_to_vss = max(self._DesignParameter['inverter_sel']['_DesignObj'].distance_to_vss,
                                  self._DesignParameter['moscap_on']['_DesignObj'].distance_to_vss)

        inv_sel_input['distance_to_vdd'] = distance_to_vdd
        moscap_on_input['distance_to_vdd'] = distance_to_vdd
        inv_sel_input['distance_to_vss'] = distance_to_vss
        moscap_on_input['distance_to_vss'] = distance_to_vss

        self._DesignParameter['inverter_sel']['_DesignObj']._CalculateDesignParameter(**inv_sel_input)
        self._DesignParameter['moscap_on']['_DesignObj']._CalculateDesignParameter(**moscap_on_input)

        """
        inv_sel to via12, via12 to moscap routing
        """
        y_common = self.getXY('moscap_on', 'pmos2', 'pmos_gate_via', '_Met1Layer')[0][1]

        self._DesignParameter['out_in_routing1'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _Width=self.getYWidth('moscap_on', 'pmos2', 'pmos_gate_via', '_Met1Layer'))

        path1_source_x = self._DesignParameter['inverter_sel']['_DesignObj'].x_value_output + \
                         self._DesignParameter['inverter_sel']['_XYCoordinates'][0][0]
        path1_target_x = self.getXY('via_sel_b', '_Met1Layer')[0][0]
        self._DesignParameter['out_in_routing1']['_XYCoordinates'] = [[[path1_source_x, y_common],
                                                                       [path1_target_x, y_common]]]

        self._DesignParameter['out_in_routing2'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _Width=self.getYWidth('moscap_on', 'nmos2', 'nmos_gate_via', '_Met1Layer'))
        path2_source_x = self.getXY('via_sel_b', '_Met1Layer')[0][0]
        path2_target_x = self.getXY('moscap_on', 'pmos1', 'pmos_gate_via', '_Met1Layer')[0][0]
        self._DesignParameter['out_in_routing2']['_XYCoordinates'] = [[[path2_source_x, y_common],
                                                                       [path2_target_x, y_common]]]

        """
        inv_sel to sel input routing
        """
        y_common = self.getXY('moscap_on', 'nmos2', 'nmos_gate_via', '_Met1Layer')[0][1]

        self._DesignParameter['sel_routing'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _Width=self.getYWidth('moscap_on', 'nmos2', 'nmos_gate_via', '_Met1Layer'))

        path_source_x = self.getXY('inverter_sel', 'nmos', 'nmos_gate_via', '_Met1Layer')[0][0]
        path_target_x = self.getXY('moscap_on', 'nmos1', 'nmos_gate_via', '_Met1Layer')[0][0]
        self._DesignParameter['sel_routing']['_XYCoordinates'] = [[[path_source_x, y_common],
                                                                       [path_target_x, y_common]]]

        self.space_bw_gate_nmos_met1_edges = self.getXYBot('moscap_on', 'nmos2', 'nmos_gate_via', '_Met1Layer')[0][1] -\
            self.getXYTop('moscap_on', 'nmos2', 'nmos', '_Met1Layer')[0][1]
        self.space_bw_gate_pmos_met1_edges = abs(self.getXYTop('moscap_on', 'pmos2', 'pmos_gate_via', '_Met1Layer')[0][1] -\
            self.getXYBot('moscap_on', 'pmos2', 'pmos', '_Met1Layer')[0][1])

        self.space_bw_np_gate_centers = self.getXY('moscap_on', 'pmos1', 'pmos_gate_via','_Met1Layer')[0][1] - \
                                        self.getXY('moscap_on', 'nmos1', 'nmos_gate_via', '_Met1Layer')[0][1]

        self.distance_to_vdd = self.getXY('moscap_on', 'vdd', '_Met1Layer')[0][1]
        self.distance_to_vss = abs(self.getXY('moscap_on', 'vss', '_Met1Layer')[0][1])

        self.leftmost_poly_edge = min(self.getXYLeft('inverter_sel', 'nmos','nmos','_PODummyLayer')[0][0],
                                      self.getXYLeft('inverter_sel','pmos','pmos', '_PODummyLayer')[0][0])
        self.rightmost_poly_edge = max(self.getXYRight('moscap_on','nmos2','nmos','_PODummyLayer')[-1][0],
                                      self.getXYRight('moscap_on','pmos2','pmos', '_PODummyLayer')[-1][0])
        self.cell_width = self.rightmost_poly_edge - self.leftmost_poly_edge


if __name__ == '__main__':
    Obj = MOSCAP_COARSE_FINE()
    Obj._CalculateDesignParameter(channel_length=30, dummy=True, PCCrit=True, XVT='SLVT',
                                  finger_sel_p=1, finger_sel_n=3,
                                  finger_on=4,
                                  finger_moscap_p=2, finger_moscap_n=5,

                                  channel_width_sel_p=400, channel_width_sel_n=300,
                                  channel_width_on_p=400, channel_width_on_n=200,
                                  channel_width_moscap_p=400, channel_width_moscap_n=500,

                                  supply_num_coy=None, supply_num_cox=None,
                                  distance_to_vdd=None, distance_to_vss=None,
                                  space_bw_gate_nmos=None, space_bw_gate_pmos=None,
                                  gap_bw_mos_gates=None
                                  )

    Obj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=Obj._DesignParameter)
    _fileName = 'MS_moscap_coarse_fine.gds'
    testStreamFile = open('./MS_moscap_coarse_fine.gds', 'wb')
    tmp = Obj._CreateGDSStream(Obj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    import ftplib

    ftp = ftplib.FTP('141.223.29.62')
    ftp.login('kms95', 'dosel545')
    ftp.cwd('/mnt/sdb/kms95/OPUS/ss28')
    myfile = open('MS_moscap_coarse_fine.gds', 'rb')
    ftp.storbinary('STOR MS_moscap_coarse_fine.gds', myfile)
    myfile.close()
    ftp.close()