from generatorLib import DRC
from generatorLib.generator_models import NbodyContact
from generatorLib.generator_models import PbodyContact
from generatorLib.generator_models import PMOSWithGate
from generatorLib.generator_models import NMOSWithGate
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import MS_inverter_coarse_fine

from generatorLib import StickDiagram
from generatorLib import DesignParameters

import copy, math, warnings

class INVERTER_ARRAY(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict( channel_length=None, dummy=None, PCCrit=None, XVT=None,
                                            finger1=None, channel_width1=None,
                                            finger2=None, channel_width2=None,
                                            finger3=None, channel_width3=None,
                                            finger4=None, channel_width4=None,
                                            cell_number=None,

                                            supply_num_coy=None, supply_num_cox=None,
                                            distance_to_vdd=None, distance_to_vss=None, space_bw_gate_nmos = None,
                                            space_bw_gate_pmos=None
                                           )

    def __init__(self, _DesignParameter=None, _Name='MS_inverter_array'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter(self,
                                  channel_length=None, dummy=None, PCCrit=None, XVT = None,
                                  finger1=None, channel_width1=None,
                                  finger2=None, channel_width2=None,
                                  finger3=None, channel_width3=None,
                                  finger4=None, channel_width4=None,
                                  gap_bw_mos_gates=None, supply_num_coy=None, space_bw_gate_nmos = None,
                                  distance_to_vdd=None, distance_to_vss=None, cell_number=None,
                                  space_bw_gate_pmos=None
                                  ):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        for i in range(cell_number):
            self._DesignParameter[f'inverter_{i+1}'] = \
            self._SrefElementDeclaration(_DesignObj=MS_inverter_coarse_fine.INVERTER_COARSE_FINE(_DesignParameter=None,
                                                                       _Name=f'inverter_{i+1}_in_{_Name}'))[0]
            universal_input = dict(channel_length=channel_length, dummy=dummy, PCCrit=PCCrit, XVT=XVT,
                                            finger1=finger1, channel_width1=channel_width1,
                                            finger2=finger2, channel_width2=channel_width2,
                                            finger3=finger3, channel_width3=channel_width3,
                                            finger4=finger4, channel_width4=channel_width4,
                                            gap_bw_mos_gates= gap_bw_mos_gates,
                                            space_bw_gate_nmos=space_bw_gate_nmos,
                                            space_bw_gate_pmos=space_bw_gate_pmos,
                                            supply_num_coy=supply_num_coy,
                                            distance_to_vdd=distance_to_vdd, distance_to_vss=distance_to_vss)

            self._DesignParameter[f'inverter_{i+1}']['_DesignObj']._CalculateDesignParameter(**universal_input)

        interval = self._DesignParameter['inverter_1']['_DesignObj'].cell_width + drc._PolygateMinSpace
        if cell_number % 2 == 1:
            first_cell_x_value = 0 - (cell_number // 2) * interval
        else:
            first_cell_x_value = 0 - interval * (0.5 + (cell_number / 2 - 1))

        for i in range(cell_number):
            x_value = first_cell_x_value + interval * i
            self._DesignParameter[f'inverter_{i + 1}']['_XYCoordinates'] = [[x_value, 0]]

        # """
        # Layer Extension
        # """
        # self._DesignParameter['additional_nxvt_layer'] = self._PathElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping[f'{XVT}'][0],
        #     _Datatype=DesignParameters._LayerMapping[f'{XVT}'][1])
        # self._DesignParameter['additional_pxvt_layer'] = self._PathElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping[f'{XVT}'][0],
        #     _Datatype=DesignParameters._LayerMapping[f'{XVT}'][1])
        # self._DesignParameter['additional_met1_vdd'] = self._PathElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL1'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL1'][1])
        # self._DesignParameter['additional_met1_vss'] = self._PathElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL1'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL1'][1])
        # self._DesignParameter['nwell'] = self._PathElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['NWELL'][0],
        #     _Datatype=DesignParameters._LayerMapping['NWELL'][1])
        # self._DesignParameter['additional_bp_layer'] = self._PathElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['PIMP'][0],
        #     _Datatype=DesignParameters._LayerMapping['PIMP'][1]
        #     )
        #
        # nxvt_source = self.getXYLeft('inverter_1', 'additional_nxvt_layer')
        # nxvt_target = self.getXYRight(f'inverter_{cell_number}', 'additional_nxvt_layer')
        # nxvt_path = [[nxvt_source[0], nxvt_target[0]]]
        # nxvt_width = self.getYWidth(f'inverter_1', 'additional_nxvt_layer')
        # self._DesignParameter['additional_nxvt_layer']['_XYCoordinates'] = nxvt_path
        # self._DesignParameter['additional_nxvt_layer']['_Width'] = nxvt_width
        #
        # pxvt_source = self.getXYLeft('inverter_1', 'additional_pxvt_layer')
        # pxvt_target = self.getXYRight(f'inverter_{cell_number}', 'additional_pxvt_layer')
        # pxvt_path = [[pxvt_source[0], pxvt_target[0]]]
        # pxvt_width = self.getYWidth(f'inverter_1', 'additional_pxvt_layer')
        # self._DesignParameter['additional_pxvt_layer']['_XYCoordinates'] = pxvt_path
        # self._DesignParameter['additional_pxvt_layer']['_Width'] = pxvt_width
        #
        # bp_source = self._DesignParameter['inverter_1']['_DesignObj']._DesignParameter['additional_bp_layer']['_XYCoordinates'][0][0]
        # bp_target = self._DesignParameter['inverter_1']['_DesignObj']._DesignParameter['additional_bp_layer']['_XYCoordinates'][0][1]
        # bp_path = [[bp_source, bp_target]]
        # bp_width = self._DesignParameter['inverter_1']['_DesignObj']._DesignParameter['additional_bp_layer']['_Width']
        #     # self.getYWidth(f'inverter_1', 'additional_bp_layer')
        # self._DesignParameter['additional_bp_layer']['_XYCoordinates'] = bp_path
        # self._DesignParameter['additional_bp_layer']['_Width'] = bp_width
        #
        # nwell_source = self.getXYLeft('inverter_1', 'nwell')
        # nwell_target = self.getXYRight(f'inverter_{cell_number}', 'nwell')
        # nwell_path = [[nwell_source[0], nwell_target[0]]]
        # nwell_width = self.getYWidth(f'inverter_1', 'nwell')
        # self._DesignParameter['nwell']['_XYCoordinates'] = nwell_path
        # self._DesignParameter['nwell']['_Width'] = nwell_width

        # met1_source1 = self.getXYLeft('inverter_1', 'vdd', '_Met1Layer')
        # met1_target1 = self.getXYRight(f'inverter_{cell_number}', 'vdd', '_Met1Layer')
        # met1_source2 = self.getXYLeft('inverter_1', 'vss', '_Met1Layer')
        # met1_target2 = self.getXYRight(f'inverter_{cell_number}', 'vss', '_Met1Layer')
        # met1_path_vdd = [[met1_source1[0], met1_target1[0]]]
        # met1_path_vss = [[met1_source2[0], met1_target2[0]]]
        # met1_width1 = self.getYWidth(f'inverter_1', 'vdd', '_Met1Layer')
        # met1_width2 = self.getYWidth(f'inverter_1', 'vss', '_Met1Layer')
        # self._DesignParameter['additional_met1_vdd']['_Width'] = met1_width1
        # self._DesignParameter['additional_met1_vss']['_Width'] = met1_width2
        # self._DesignParameter['additional_met1_vdd']['_XYCoordinates'] = met1_path_vdd
        # self._DesignParameter['additional_met1_vss']['_XYCoordinates'] = met1_path_vss

        self.space_bw_gate_nmos_met1_edges = max(self.getXYBot('inverter_1', 'nmos2', 'nmos_gate_via', '_Met1Layer')[0][1] -\
            self.getXYTop('inverter_1', 'nmos2', 'nmos', '_Met1Layer')[0][1], self.getXYBot('inverter_1', \
            'nmos1', 'nmos_gate_via', '_Met1Layer')[0][1] -self.getXYTop('inverter_1', 'nmos1', 'nmos', '_Met1Layer')[0][1]
            )
        self.space_bw_gate_pmos_met1_edges = max(abs(self.getXYTop('inverter_1', 'pmos2', 'pmos_gate_via', '_Met1Layer')[0][1] -\
            self.getXYBot('inverter_1', 'pmos2', 'pmos', '_Met1Layer')[0][1]),abs(self.getXYTop('inverter_1', 'pmos1', 'pmos_gate_via', '_Met1Layer')[0][1] -\
            self.getXYBot('inverter_1', 'pmos1', 'pmos', '_Met1Layer')[0][1])
                                                 )

        self.space_bw_np_gate_centers = self.getXY('inverter_1', 'pmos1','pmos_gate_via','_Met1Layer')[0][1] - \
                                        self.getXY('inverter_1', 'nmos1', 'nmos_gate_via', '_Met1Layer')[0][1]

        self.distance_to_vdd = self.getXY('inverter_1', 'vdd','_Met1Layer')[0][1]
        self.distance_to_vss = abs(self.getXY('inverter_1', 'vss','_Met1Layer')[0][1])

        self.leftmost_poly_edge = min(self.getXYLeft('inverter_1', 'nmos1','nmos','_PODummyLayer')[0][0],
                                      self.getXYLeft('inverter_1', 'pmos1','pmos', '_PODummyLayer')[0][0])
        self.rightmost_poly_edge = max(self.getXYRight(f'inverter_{cell_number}','nmos2','nmos','_PODummyLayer')[-1][0],
                                      self.getXYRight(f'inverter_{cell_number}','pmos2','pmos', '_PODummyLayer')[-1][0])
        self.cell_width = self.rightmost_poly_edge - self.leftmost_poly_edge



if __name__ == '__main__':
    Obj = INVERTER_ARRAY()
    Obj._CalculateDesignParameter(channel_length=30, dummy=True, PCCrit=True, XVT='SLVT',
                                  finger1=15, channel_width1=400,
                                  finger2=2, channel_width2=1600,
                                  finger3=8, channel_width3=800,
                                  finger4=20, channel_width4=200, cell_number=5
                                  )

    Obj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=Obj._DesignParameter)
    _fileName = 'MS_Inverter_array.gds'
    testStreamFile = open('./MS_Inverter_array.gds', 'wb')
    tmp = Obj._CreateGDSStream(Obj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    import ftplib

    ftp = ftplib.FTP('141.223.29.62')
    ftp.login('kms95', 'dosel545')
    ftp.cwd('/mnt/sdb/kms95/Desktop')
    myfile = open('MS_Inverter_array.gds', 'rb')
    ftp.storbinary('STOR MS_Inverter_array.gds', myfile)
    myfile.close()
    ftp.close()


