from generatorLib import DRC

from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaMet22Met3
from generatorLib.generator_models import MS_moscap_coarse
from generatorLib import StickDiagram
from generatorLib import DesignParameters

import copy, math, warnings

class MOSCAP_ARRAY(StickDiagram._StickDiagram):
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
                                           gap_bw_mos_gates=None, array_dimension=None,
                                           target_cell = None
                                           )
    def __init__(self, _DesignParameter=None, _Name='MS_moscap_array'):
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
                                  gap_bw_mos_gates=None, array_dimension=None,
                                  target_cell=None
                                  ):
        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        _MinSnapSpacing = drc._MinSnapSpacing

        moscap_coarse_fine_input = dict(
            channel_length=channel_length, dummy=dummy, PCCrit=PCCrit, XVT=XVT,
            finger_sel_p=finger_sel_p, finger_sel_n=finger_sel_n,
            finger_on=finger_on,
            finger_moscap_p=finger_moscap_p, finger_moscap_n=finger_moscap_n,

            channel_width_sel_p=channel_width_sel_p, channel_width_sel_n=channel_width_sel_n,
            channel_width_on_p=channel_width_on_p, channel_width_on_n=channel_width_on_n,
            channel_width_moscap_p=channel_width_moscap_p, channel_width_moscap_n=channel_width_moscap_n,

            supply_num_coy=supply_num_coy, supply_num_cox=supply_num_cox,
            distance_to_vdd=distance_to_vdd, distance_to_vss=distance_to_vss,
            space_bw_gate_nmos=space_bw_gate_nmos, space_bw_gate_pmos=space_bw_gate_pmos,
            gap_bw_mos_gates=gap_bw_mos_gates, target_cell = target_cell
            )
        for i in range(array_dimension):
            self._DesignParameter[f'moscap_{i+1}'] = \
            self._SrefElementDeclaration(_DesignObj=MS_moscap_coarse.MOSCAP_COARSE_FINE(_DesignParameter=None,
                                                                        _Name=f'moscap_{i+1}_in_{_Name}'))[0]
            self._DesignParameter[f'moscap_{i+1}']['_DesignObj']._CalculateDesignParameter(**moscap_coarse_fine_input)

        interval = self._DesignParameter['moscap_1']['_DesignObj'].cell_width + drc._PolygateMinSpace
        if array_dimension % 2 == 1:
            first_cell_x_value = 0 - (array_dimension // 2) * interval
        else:
            first_cell_x_value = 0 - interval * (0.5 + (array_dimension / 2 - 1))

        for i in range(array_dimension):
            x_value = first_cell_x_value + interval * i
            self._DesignParameter[f'moscap_{i + 1}']['_XYCoordinates'] = [[x_value, 0]]

        self.space_bw_gate_nmos_met1_edges = max(self.getXYBot('moscap_1','moscap_on', 'nmos2', 'nmos_gate_via', '_Met1Layer')[0][1] -\
            self.getXYTop('moscap_1', 'moscap_on', 'nmos2', 'nmos', '_Met1Layer')[0][1], self.getXYBot('moscap_1', 'moscap_on',
            'nmos1', 'nmos_gate_via', '_Met1Layer')[0][1] -self.getXYTop('moscap_1', 'moscap_on', 'nmos1', 'nmos', '_Met1Layer')[0][1]
            )
        self.space_bw_gate_pmos_met1_edges = max(abs(self.getXYTop('moscap_1', 'moscap_on', 'pmos2', 'pmos_gate_via', '_Met1Layer')[0][1] -\
            self.getXYBot('moscap_1', 'moscap_on', 'pmos2', 'pmos', '_Met1Layer')[0][1]),abs(self.getXYTop('moscap_1', 'moscap_on', 'pmos1', 'pmos_gate_via', '_Met1Layer')[0][1] -\
            self.getXYBot('moscap_1', 'moscap_on', 'pmos1', 'pmos', '_Met1Layer')[0][1])
                                                 )

        self.space_bw_np_gate_centers = self.getXY('moscap_1', 'moscap_on', 'pmos1','pmos_gate_via','_Met1Layer')[0][1] - \
                                        self.getXY('moscap_1', 'moscap_on', 'nmos1', 'nmos_gate_via', '_Met1Layer')[0][1]

        self.distance_to_vdd = self.getXY('moscap_1', 'moscap_on', 'vdd','_Met1Layer')[0][1]
        self.distance_to_vss = abs(self.getXY('moscap_1', 'moscap_on', 'vss','_Met1Layer')[0][1])

        self.leftmost_poly_edge = min(self.getXYLeft('moscap_1', 'inverter_sel', 'nmos','nmos','_PODummyLayer')[0][0],
                                      self.getXYLeft('moscap_1', 'inverter_sel', 'pmos','pmos', '_PODummyLayer')[0][0])
        self.rightmost_poly_edge = max(self.getXYRight(f'moscap_{array_dimension}','moscap_on', 'nmos2','nmos','_PODummyLayer')[-1][0],
                                      self.getXYRight(f'moscap_{array_dimension}','moscap_on', 'pmos2','pmos', '_PODummyLayer')[-1][0])
        self.cell_width = self.rightmost_poly_edge - self.leftmost_poly_edge

        """
        VIA 23 Generation and Routing
        """

        self._DesignParameter['via_for_input'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(
            _Name='via_input_in{}'.format(_Name)))[0]
        via_inputs = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        via_inputs['_ViaMet22Met3NumberOfCOX'] = 1
        via_inputs['_ViaMet22Met3NumberOfCOY'] = 2
        self._DesignParameter['via_for_input']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(
            **via_inputs)
        via_points = []
        if target_cell == 'fine':
            for i in range(array_dimension):
                via_points.append(self.getXY(f'moscap_{i+1}', 'moscap_on', 'nmos1', 'nmos', '_Met1Layer')[0]
                                   )
        else:
            for i in range(array_dimension):
                via_points.append([self.getXY(f'moscap_{i+1}', 'moscap_on', 'pmos1', 'pmos', '_Met1Layer')[0][0], 0])

        self._DesignParameter['via_for_input']['_XYCoordinates'] = via_points
        self._DesignParameter['input_routing'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=drc._MetalxMinWidth)

        self._DesignParameter['input_routing']['_XYCoordinates'] = [[via_points[0],via_points[-1]]]

if __name__ == '__main__':
    Obj = MOSCAP_ARRAY()
    Obj._CalculateDesignParameter(channel_length=30, dummy=True, PCCrit=None, XVT='SLVT',
                                  finger_sel_p=2, finger_sel_n=2,
                                  finger_on=5,
                                  finger_moscap_p=5, finger_moscap_n=5,

                                  channel_width_sel_p=400, channel_width_sel_n=200,
                                  channel_width_on_p=400, channel_width_on_n=200,
                                  channel_width_moscap_p=400, channel_width_moscap_n=200,

                                  supply_num_coy=None, supply_num_cox=None,
                                  distance_to_vdd=None, distance_to_vss=None,
                                  space_bw_gate_nmos=None, space_bw_gate_pmos=None,
                                  gap_bw_mos_gates=None, array_dimension=5,
                                  target_cell='fine'
                                  )

    Obj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=Obj._DesignParameter)
    _fileName = 'MS_moscap_array.gds'
    testStreamFile = open('./MS_moscap_array.gds', 'wb')
    tmp = Obj._CreateGDSStream(Obj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    import ftplib

    ftp = ftplib.FTP('141.223.29.62')
    ftp.login('kms95', 'dosel545')
    ftp.cwd('/mnt/sdb/kms95/OPUS/ss28')
    myfile = open('MS_moscap_array.gds', 'rb')
    ftp.storbinary('STOR MS_moscap_array.gds', myfile)
    myfile.close()
    ftp.close()


