from generatorLib import DRC


from generatorLib.generator_models import MS_moscap_array
from generatorLib.generator_models import MS_inv_sel
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

        inv1_inputs = dict(
            channel_length=channel_length, dummy=dummy, PCCrit=PCCrit, XVT='SLVT',
            finger1=finger1_p, channel_width1=channel_width_finger1_p,
            finger2=finger1_n, channel_width2=channel_width_finger1_n,

            gap_bw_mos_gates=gap_bw_mos_gates,
            supply_num_coy=supply_num_coy,
            distance_to_vdd=distance_to_vdd, distance_to_vss=distance_to_vss, space_bw_gate_nmos=space_bw_gate_nmos,
            space_bw_gate_pmos=space_bw_gate_pmos
        )
        inv2_inputs = dict(
            channel_length=channel_length, dummy=dummy, PCCrit=PCCrit, XVT='SLVT',
            finger1=finger2_p, channel_width1=channel_width_finger2_p,
            finger2=finger2_n, channel_width2=channel_width_finger2_n,

            gap_bw_mos_gates=gap_bw_mos_gates,
            supply_num_coy=supply_num_coy,
            distance_to_vdd=distance_to_vdd, distance_to_vss=distance_to_vss, space_bw_gate_nmos=space_bw_gate_nmos,
            space_bw_gate_pmos=space_bw_gate_pmos
        )
        inv3_inputs = dict(
            channel_length=channel_length, dummy=dummy, PCCrit=PCCrit, XVT='SLVT',
            finger1=finger3_p, channel_width1=channel_width_finger3_p,
            finger2=finger3_n, channel_width2=channel_width_finger3_n,

            gap_bw_mos_gates=gap_bw_mos_gates,
            supply_num_coy=supply_num_coy,
            distance_to_vdd=distance_to_vdd, distance_to_vss=distance_to_vss,
            space_bw_gate_nmos=space_bw_gate_nmos, space_bw_gate_pmos=space_bw_gate_pmos
        )
        moscap_fine_inputs = dict(
            channel_length=channel_length, dummy=dummy, PCCrit=PCCrit, XVT='SLVT',

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

        self._DesignParameter[f'moscap_fine_array'] = \
        self._SrefElementDeclaration(_DesignObj=MS_moscap_array.MOSCAP_ARRAY(_DesignParameter=None,
                                                                    _Name=f'moscap_fine_array_in_{_Name}'),
                                     )[0]
        self._DesignParameter[f'inv1'] = \
        self._SrefElementDeclaration(_DesignObj=MS_inv_sel.INVERTER_SEL(_DesignParameter=None,
                                                                    _Name=f'inv1_in_{_Name}'),
                                     )[0]
        self._DesignParameter[f'inv2'] = \
        self._SrefElementDeclaration(_DesignObj=MS_inv_sel.INVERTER_SEL(_DesignParameter=None,
                                                                    _Name=f'inv2_in_{_Name}'),
                                     )[0]
        self._DesignParameter[f'inv3'] = \
        self._SrefElementDeclaration(_DesignObj=MS_inv_sel.INVERTER_SEL(_DesignParameter=None,
                                                                    _Name=f'inv3_in_{_Name}'),
                                     )[0]

        self._DesignParameter[f'inv1']['_DesignObj']._CalculateDesignParameter(**inv1_inputs)
        self._DesignParameter[f'inv2']['_DesignObj']._CalculateDesignParameter(**inv2_inputs)
        self._DesignParameter[f'inv3']['_DesignObj']._CalculateDesignParameter(**inv3_inputs)
        self._DesignParameter[f'moscap_fine_array']['_DesignObj']._CalculateDesignParameter(**moscap_fine_inputs)

        self._DesignParameter['inv1']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['inv2']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['inv3']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['moscap_fine_array']['_XYCoordinates'] = [[0, 0]]

        cell_width = self._DesignParameter['inv1']['_DesignObj'].cell_width + \
                     self._DesignParameter['inv2']['_DesignObj'].cell_width + \
                     self._DesignParameter['inv3']['_DesignObj'].cell_width + \
                     self._DesignParameter['moscap_fine_array']['_DesignObj'].cell_width + 3 * drc._PolygateMinSpace2

        inv1_x = 0 - cell_width / 2 + abs(self._DesignParameter['inv1']['_DesignObj'].leftmost_poly_edge)
        inv2_x = inv1_x + abs(self._DesignParameter['inv1']['_DesignObj'].rightmost_poly_edge) + \
                 abs(self._DesignParameter['inv2']['_DesignObj'].leftmost_poly_edge) + drc._PolygateMinSpace2 - channel_length / 2
        inv3_x = inv2_x + abs(self._DesignParameter['inv2']['_DesignObj'].rightmost_poly_edge) + \
                 abs(self._DesignParameter['inv3']['_DesignObj'].leftmost_poly_edge) + drc._PolygateMinSpace2 - channel_length / 2
        moscap_x = inv3_x + abs(self._DesignParameter['inv3']['_DesignObj'].rightmost_poly_edge) + \
                 abs(self._DesignParameter['moscap_fine_array']['_DesignObj'].leftmost_poly_edge) + \
                   drc._PolygateMinSpace2 - channel_length / 2

        self._DesignParameter['inv1']['_XYCoordinates'] = [[inv1_x, 0]]
        self._DesignParameter['inv2']['_XYCoordinates'] = [[inv2_x, 0]]
        self._DesignParameter['inv3']['_XYCoordinates'] = [[inv3_x, 0]]
        self._DesignParameter['moscap_fine_array']['_XYCoordinates'] = [[moscap_x, 0]]

        """
        gate_bw_mos alignment
        """
        gap_bw_mos_gates = max(self._DesignParameter['inv1']['_DesignObj'].space_bw_np_gate_centers,
                               self._DesignParameter['inv2']['_DesignObj'].space_bw_np_gate_centers,
                               self._DesignParameter['inv3']['_DesignObj'].space_bw_np_gate_centers,
                               self._DesignParameter['moscap_fine_array']['_DesignObj'].space_bw_np_gate_centers)
        inv1_inputs['gap_bw_mos_gates'] = gap_bw_mos_gates
        inv2_inputs['gap_bw_mos_gates'] = gap_bw_mos_gates
        inv3_inputs['gap_bw_mos_gates'] = gap_bw_mos_gates
        moscap_fine_inputs['gap_bw_mos_gates'] = gap_bw_mos_gates
        """
        space_bw_mos_and_gate alignment
        """
        space_bw_gate_nmos = max(self._DesignParameter['inv1']['_DesignObj'].space_bw_gate_nmos_met1_edges,
                               self._DesignParameter['inv2']['_DesignObj'].space_bw_gate_nmos_met1_edges,
                               self._DesignParameter['inv3']['_DesignObj'].space_bw_gate_nmos_met1_edges,
                               self._DesignParameter['moscap_fine_array']['_DesignObj'].space_bw_gate_nmos_met1_edges)

        space_bw_gate_pmos = max(self._DesignParameter['inv1']['_DesignObj'].space_bw_gate_pmos_met1_edges,
                               self._DesignParameter['inv2']['_DesignObj'].space_bw_gate_pmos_met1_edges,
                               self._DesignParameter['inv3']['_DesignObj'].space_bw_gate_pmos_met1_edges,
                               self._DesignParameter['moscap_fine_array']['_DesignObj'].space_bw_gate_pmos_met1_edges)

        inv1_inputs['space_bw_gate_nmos'] = space_bw_gate_nmos - drc._Metal1MinSpace2
        inv2_inputs['space_bw_gate_nmos'] = space_bw_gate_nmos - drc._Metal1MinSpace2
        inv3_inputs['space_bw_gate_nmos'] = space_bw_gate_nmos - drc._Metal1MinSpace2
        moscap_fine_inputs['space_bw_gate_nmos'] = space_bw_gate_nmos - drc._Metal1MinSpace2

        inv1_inputs['space_bw_gate_pmos'] = space_bw_gate_pmos - drc._Metal1MinSpace2
        inv2_inputs['space_bw_gate_pmos'] = space_bw_gate_pmos - drc._Metal1MinSpace2
        inv3_inputs['space_bw_gate_pmos'] = space_bw_gate_pmos - drc._Metal1MinSpace2
        moscap_fine_inputs['space_bw_gate_pmos'] = space_bw_gate_pmos - drc._Metal1MinSpace2

        self._DesignParameter[f'inv1']['_DesignObj']._CalculateDesignParameter(**inv1_inputs)
        self._DesignParameter[f'inv2']['_DesignObj']._CalculateDesignParameter(**inv2_inputs)
        self._DesignParameter[f'inv3']['_DesignObj']._CalculateDesignParameter(**inv3_inputs)
        self._DesignParameter[f'moscap_fine_array']['_DesignObj']._CalculateDesignParameter(**moscap_fine_inputs)

        """
        vdd, vss rail alignment
        """
        distance_to_vdd_min = max(self._DesignParameter['inv1']['_DesignObj'].distance_to_vdd,
                              self._DesignParameter['inv2']['_DesignObj'].distance_to_vdd,
                              self._DesignParameter['inv3']['_DesignObj'].distance_to_vdd,
                              self._DesignParameter['moscap_fine_array']['_DesignObj'].distance_to_vdd)
        distance_to_vss_min = max(self._DesignParameter['inv1']['_DesignObj'].distance_to_vss,
                              self._DesignParameter['inv2']['_DesignObj'].distance_to_vss,
                              self._DesignParameter['inv3']['_DesignObj'].distance_to_vss,
                              self._DesignParameter['moscap_fine_array']['_DesignObj'].distance_to_vss)
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

        inv1_inputs['distance_to_vdd'] = distance_to_vdd
        inv2_inputs['distance_to_vdd'] = distance_to_vdd
        inv3_inputs['distance_to_vdd'] = distance_to_vdd
        moscap_fine_inputs['distance_to_vdd'] = distance_to_vdd

        inv1_inputs['distance_to_vss'] = distance_to_vss
        inv2_inputs['distance_to_vss'] = distance_to_vss
        inv3_inputs['distance_to_vss'] = distance_to_vss
        moscap_fine_inputs['distance_to_vss'] = distance_to_vss

        self._DesignParameter[f'inv1']['_DesignObj']._CalculateDesignParameter(**inv1_inputs)
        self._DesignParameter[f'inv2']['_DesignObj']._CalculateDesignParameter(**inv2_inputs)
        self._DesignParameter[f'inv3']['_DesignObj']._CalculateDesignParameter(**inv3_inputs)
        self._DesignParameter[f'moscap_fine_array']['_DesignObj']._CalculateDesignParameter(**moscap_fine_inputs)

        print("test")


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

