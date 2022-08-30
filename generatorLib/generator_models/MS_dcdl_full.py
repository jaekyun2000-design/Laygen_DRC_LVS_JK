from generatorLib import DRC


from generatorLib.generator_models import MS_inverters_with_moscap_fine
from generatorLib.generator_models import MS_moscap_coarse_full

from generatorLib import StickDiagram
from generatorLib import DesignParameters

import copy, math, warnings

class DCDL_FULL(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(
                                            #########            UNIVERSAL INPUTS             ##########
                                            channel_length=None, dummy=None, PCCrit=None, XVT=None,
                                            supply_num_coy=None,
                                            distance_to_vdd=None, distance_to_vss=None,
                                            space_bw_gate_nmos=None, space_bw_gate_pmos=None,
                                            gap_bw_mos_gates=None,

                                            ######### INVERTERS WITH MOSCAP FINE ARRAY INPUTS ##########
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
                                            finger_sel_p_fine=None, finger_sel_n_fine=None,
                                            finger_on_fine=None,
                                            finger_moscap_p_fine=None, finger_moscap_n_fine=None,

                                            channel_width_sel_p_fine=None, channel_width_sel_n_fine=None,
                                            channel_width_on_p_fine=None, channel_width_on_n_fine=None,
                                            channel_width_moscap_p_fine=None, channel_width_moscap_n_fine=None,

                                            array_dimension_for_moscap_fine = None,

                                            #########        MOSCAP COARSE ARRAY INPUTS        ##########
                                            finger_sel_p_coarse = None, finger_sel_n_coarse = None,
                                            finger_on_coarse = None,
                                            finger_moscap_p_coarse = None, finger_moscap_n_coarse = None,
                                            channel_width_sel_p_coarse=None, channel_width_sel_n_coarse=None,
                                            channel_width_on_p_coarse=None, channel_width_on_n_coarse=None,
                                            channel_width_moscap_p_coarse=None, channel_width_moscap_n_coarse=None,

                                            array_dimension_for_moscap_coarse=None

                                           )

    def __init__(self, _DesignParameter=None, _Name=f'MS_DCDL_full'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter(self,
                                  #########            UNIVERSAL INPUTS             ##########
                                  channel_length=None, dummy=None, PCCrit=None, XVT=None,
                                  supply_num_coy=None,
                                  distance_to_vdd=None, distance_to_vss=None,
                                  space_bw_gate_nmos=None, space_bw_gate_pmos=None,
                                  gap_bw_mos_gates=None,

                                  ######### INVERTERS WITH MOSCAP FINE ARRAY INPUTS ##########
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
                                  finger_sel_p_fine=None, finger_sel_n_fine=None,
                                  finger_on_fine=None,
                                  finger_moscap_p_fine=None, finger_moscap_n_fine=None,

                                  channel_width_sel_p_fine=None, channel_width_sel_n_fine=None,
                                  channel_width_on_p_fine=None, channel_width_on_n_fine=None,
                                  channel_width_moscap_p_fine=None, channel_width_moscap_n_fine=None,

                                  array_dimension_for_moscap_fine=None,

                                  #########        MOSCAP COARSE ARRAY INPUTS        ##########
                                  finger_sel_p_coarse=None, finger_sel_n_coarse=None,
                                  finger_on_coarse=None,
                                  finger_moscap_p_coarse=None, finger_moscap_n_coarse=None,
                                  channel_width_sel_p_coarse=None, channel_width_sel_n_coarse=None,
                                  channel_width_on_p_coarse=None, channel_width_on_n_coarse=None,
                                  channel_width_moscap_p_coarse=None, channel_width_moscap_n_coarse=None,

                                  array_dimension_for_moscap_coarse=None

                                  ):
        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        _MinSnapSpacing = drc._MinSnapSpacing

        moscap_fine_inputs = dict(
            ######### INVERTERS WITH MOSCAP FINE ARRAY INPUTS ##########
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
            finger_sel_p=finger_sel_p_fine, finger_sel_n=finger_sel_n_fine,
            finger_on=finger_on_fine,
            finger_moscap_p=finger_moscap_p_fine, finger_moscap_n=finger_moscap_n_fine,

            channel_width_sel_p=channel_width_sel_p_fine, channel_width_sel_n=channel_width_sel_n_fine,
            channel_width_on_p=channel_width_on_p_fine, channel_width_on_n=channel_width_on_n_fine,
            channel_width_moscap_p=channel_width_moscap_p_fine,
            channel_width_moscap_n=channel_width_moscap_n_fine,

            array_dimension=array_dimension_for_moscap_fine,

            #########            UNIVERSAL INPUTS             ##########
            channel_length=channel_length, dummy=dummy, PCCrit=PCCrit, XVT=XVT,
            supply_num_coy=supply_num_coy,
            distance_to_vdd=distance_to_vdd, distance_to_vss=distance_to_vss,
            space_bw_gate_nmos=space_bw_gate_nmos, space_bw_gate_pmos=space_bw_gate_pmos,
            gap_bw_mos_gates=gap_bw_mos_gates

        )
        moscap_coarse_inputs = dict(
            #########        MOSCAP COARSE ARRAY INPUTS        ##########
            finger_sel_p=finger_sel_p_coarse, finger_sel_n=finger_sel_n_coarse,
            finger_on=finger_on_coarse,
            finger_moscap_p=finger_moscap_p_coarse, finger_moscap_n=finger_moscap_n_coarse,
            channel_width_sel_p=channel_width_sel_p_coarse, channel_width_sel_n=channel_width_sel_n_coarse,
            channel_width_on_p=channel_width_on_p_coarse, channel_width_on_n=channel_width_on_n_coarse,
            channel_width_moscap_p=channel_width_moscap_p_coarse,
            channel_width_moscap_n=channel_width_moscap_n_coarse,

            array_dimension=array_dimension_for_moscap_coarse,

            #########            UNIVERSAL INPUTS             ##########
            channel_length=channel_length, dummy=dummy, PCCrit=PCCrit, XVT=XVT,
            supply_num_coy=supply_num_coy,
            distance_to_vdd=distance_to_vdd, distance_to_vss=distance_to_vss,
            space_bw_gate_nmos=space_bw_gate_nmos, space_bw_gate_pmos=space_bw_gate_pmos,
            gap_bw_mos_gates=gap_bw_mos_gates
        )
        self._DesignParameter['top_line'] = self._SrefElementDeclaration(_DesignObj=MS_inverters_with_moscap_fine.
                            MOSCAP_FINE_FULL(_DesignParameter=None,
                            _Name=f'dcdl_top_line_in_{_Name}'),
                            _Reflect=[1, 0, 0], _Angle= 0)[0]
        self._DesignParameter['bottom_line'] = self._SrefElementDeclaration(_DesignObj=MS_moscap_coarse_full.
                            MOSCAP_COARSE_FULL(_DesignParameter=None,
                            _Name=f'dcdl_bot_line_in_{_Name}'),
                            )[0]
        self._DesignParameter['top_line']['_DesignObj']._CalculateDesignParameter(**moscap_fine_inputs)
        self._DesignParameter['bottom_line']['_DesignObj']._CalculateDesignParameter(**moscap_coarse_inputs)

        top_line_y = self._DesignParameter['bottom_line']['_DesignObj'].rail_to_rail_distance + \
                     self._DesignParameter['top_line']['_DesignObj'].distance_to_vdd


        self._DesignParameter['bottom_line']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['top_line']['_XYCoordinates'] = [[0, top_line_y]]

        if self._DesignParameter['bottom_line']['_DesignObj'].cell_width < self._DesignParameter['top_line']['_DesignObj'].cell_width:
            # self._DesignParameter['bottom_line']['_DesignObj']
            self.delete_vdd(self._DesignParameter['bottom_line']['_DesignObj']._DesignParameter['moscap_coarse_full2'])
            self.delete_vdd(self._DesignParameter['bottom_line']['_DesignObj']._DesignParameter['moscap_coarse_full3'])
        else:
            self.delete_vdd(self._DesignParameter['top_line'])

        """
        moscap coarse met3 routing
        """
        self._DesignParameter['moscap_coarse_routing'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=drc._MetalxMinWidth)

        target_y_value = self._DesignParameter['bottom_line']['_DesignObj'].met3_routing_y_value
        source_xy = self._DesignParameter['top_line']['_DesignObj'].via23_point

        source_y_real_value = 0 + top_line_y - source_xy[0][1]

        source_xy_real = [[source_xy[0][0], source_y_real_value], [source_xy[1][0], source_y_real_value]]
        path_xy = [[source_xy_real[0], [source_xy_real[0][0], target_y_value]], [source_xy_real[1],
                                                                                 [source_xy_real[1][0], target_y_value]]]
        self._DesignParameter['moscap_coarse_routing']['_XYCoordinates'] = path_xy
        print("test")


    def delete_vdd(self, object):
        for key1, element1 in object.items():
            if key1 == '_DesignObj':
                for key2, element2 in element1._DesignParameter.items():
                    if key2 == 'vdd':
                        element2['_XYCoordinates'] = []
                    else:
                        if element2['_DesignParametertype'] == 3:
                            self.delete_vdd(element2)

if __name__ == '__main__':
    Obj = DCDL_FULL()
    import random
    import time
    cnt = 1
    for i in range(0,200):
        print("Generating Random Input Variables...")
        time.sleep(5)

        channel_length = random.randrange(30,100, 10)
        gap_bw_mos_gates = random.randrange(100,1800,50)
        array_dimension = random.randrange(2, 8, 1)
        supply_num_coy= random.randrange(1,5,1)


        finger_sel_p_fine = random.randrange(1, 9, 1)
        finger_sel_n_fine= random.randrange(1, 9, 1)
        finger_on_fine= random.randrange(1, 9, 1)
        finger_moscap_p_fine= random.randrange(1, 9, 1)
        finger_moscap_n_fine= random.randrange(1, 9, 1)

        finger_sel_p_coarse = random.randrange(1, 9, 1)
        finger_sel_n_coarse= random.randrange(1, 9, 1)
        finger_on_coarse= random.randrange(1, 9, 1)
        finger_moscap_p_coarse= random.randrange(1, 9, 1)
        finger_moscap_n_coarse= random.randrange(1, 9, 1)

        finger1_n= random.randrange(1, 9, 1)
        finger1_p= random.randrange(1, 9, 1)
        finger2_n= random.randrange(1, 9, 1)
        finger2_p= random.randrange(1, 9, 1)
        finger3_n= random.randrange(1, 9, 1)
        finger3_p= random.randrange(1, 9, 1)

        channel_width_sel_p_fine= random.randrange(400,1350,50)
        channel_width_sel_n_fine= random.randrange(200,650,50)
        channel_width_on_p_fine= random.randrange(400,1350,50)
        channel_width_on_n_fine= random.randrange(200,650,50)
        channel_width_moscap_p_fine= random.randrange(400,1350,50)
        channel_width_moscap_n_fine= random.randrange(200,650,50)

        channel_width_sel_p_coarse= random.randrange(400,1350,50)
        channel_width_sel_n_coarse= random.randrange(200,650,50)
        channel_width_on_p_coarse= random.randrange(400,1350,50)
        channel_width_on_n_coarse= random.randrange(200,650,50)
        channel_width_moscap_p_coarse= random.randrange(400,1350,50)
        channel_width_moscap_n_coarse= random.randrange(200,650,50)

        channel_width_finger1_n= random.randrange(200,650,50)
        channel_width_finger1_p= random.randrange(400,1350,50)
        channel_width_finger2_n= random.randrange(200,650,50)
        channel_width_finger2_p= random.randrange(400,1350,50)
        channel_width_finger3_n= random.randrange(200,650,50)
        channel_width_finger3_p= random.randrange(400,1350,50)

        array_dimension_for_moscap_fine = random.randrange(2,8,1)
        array_dimension_for_moscap_coarse = random.randrange(2, 8, 1)




        print("Waiting For 10 seconds before Calculation initialization...")
        print(f"Count of Loop : {cnt}")
        time.sleep(10)

        Obj._CalculateDesignParameter(
            ######### INVERTERS WITH MOSCAP FINE ARRAY INPUTS ##########
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
            finger_sel_p_fine=finger_sel_p_fine, finger_sel_n_fine=finger_sel_n_fine,
            finger_on_fine=finger_on_fine,
            finger_moscap_p_fine=finger_moscap_p_fine, finger_moscap_n_fine=finger_moscap_n_fine,

            channel_width_sel_p_fine=channel_width_sel_p_fine, channel_width_sel_n_fine=channel_width_sel_n_fine,
            channel_width_on_p_fine=channel_width_on_p_fine, channel_width_on_n_fine=channel_width_on_n_fine,
            channel_width_moscap_p_fine=channel_width_moscap_p_fine,
            channel_width_moscap_n_fine=channel_width_moscap_n_fine,

            array_dimension_for_moscap_fine=array_dimension_for_moscap_fine,

            #########            UNIVERSAL INPUTS             ##########
            channel_length=channel_length, dummy='True', PCCrit='True', XVT='SLVT',
            supply_num_coy=supply_num_coy,
            gap_bw_mos_gates=gap_bw_mos_gates,

            #########        MOSCAP COARSE ARRAY INPUTS        ##########
            finger_sel_p_coarse=finger_sel_p_coarse, finger_sel_n_coarse=finger_sel_n_coarse,
            finger_on_coarse=finger_on_coarse,
            finger_moscap_p_coarse=finger_moscap_p_coarse, finger_moscap_n_coarse=finger_moscap_n_coarse,
            channel_width_sel_p_coarse=channel_width_sel_p_coarse,
            channel_width_sel_n_coarse=channel_width_sel_n_coarse,
            channel_width_on_p_coarse=channel_width_on_p_coarse, channel_width_on_n_coarse=channel_width_on_n_coarse,
            channel_width_moscap_p_coarse=channel_width_moscap_p_coarse,
            channel_width_moscap_n_coarse=channel_width_moscap_n_coarse,

            array_dimension_for_moscap_coarse=array_dimension_for_moscap_coarse

        )


        Obj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=Obj._DesignParameter)
        _fileName = 'MS_DCDL_full.gds'
        testStreamFile = open('./MS_DCDL_full.gds', 'wb')
        tmp = Obj._CreateGDSStream(Obj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        import ftplib

        ftp = ftplib.FTP('141.223.29.62')
        ftp.login('kms95', 'dosel545')
        ftp.cwd('/mnt/sdb/kms95/OPUS/ss28')
        myfile = open('MS_DCDL_full.gds', 'rb')
        ftp.storbinary('STOR MS_DCDL_full.gds', myfile)
        myfile.close()
        ftp.close()

        import DRCchecker
        print(f"Count of Loop : {cnt}")
        _DRC = DRCchecker.DRCchecker('kms95','dosel545','/mnt/sdb/kms95/OPUS/ss28','/mnt/sdb/kms95/OPUS/ss28/DRC/run',
                                     'MS_DCDL_full','MS_DCDL_full')

        _DRC.DRCchecker()

        print("Waiting For 10 seconds before another loop....")
        cnt = cnt + 1
        time.sleep(10)



