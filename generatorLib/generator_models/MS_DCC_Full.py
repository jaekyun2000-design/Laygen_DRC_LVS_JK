from generatorLib.generator_models import MS_DCC_Unit

from generatorLib import StickDiagram
from generatorLib import DesignParameters

class DCC_Full(StickDiagram._StickDiagram):
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

    def __init__(self, _DesignParameter=None, _Name='DCC_Full'):
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

        _Name = self._DesignParameter['_Name']['_Name']
        self._DesignParameter['dcc_unit1'] = self._SrefElementDeclaration(
            _DesignObj=MS_DCC_Unit.DCC_Unit(_DesignParameter=None, _Name=f'dcc_unit1_in_{_Name}'))[0]
        self._DesignParameter['dcc_unit2'] = self._SrefElementDeclaration(
            _DesignObj=MS_DCC_Unit.DCC_Unit(_DesignParameter=None, _Name=f'dcc_unit2_in_{_Name}'),
            _Reflect=[1, 0, 0], _Angle= 0)[0]
        dict_for_dcc = dict(channel_length=channel_length, dummy=dummy, PCCrit=PCCrit, XVT=XVT,
                                    supply_num_coy=supply_num_coy, distance_to_vdd=distance_to_vdd,
                                    distance_to_vss=distance_to_vss,
                                    coarse_fine_dimension=coarse_fine_dimension, gap_bw_gates=gap_bw_gates,

                                    #### Dictionary for Inverter ON
                                    finger_on_n=finger_on_n, channel_width_on_n=channel_width_on_n,
                                    finger_on_p=finger_on_p, channel_width_on_p=channel_width_on_p,

                                    #### Dictionary for Inverter COARSE
                                    finger_coarse_p1=finger_coarse_p1, channel_width_coarse_p1=channel_width_coarse_p1,
                                    finger_coarse_p2=finger_coarse_p2, channel_width_coarse_p2=channel_width_coarse_p2,
                                    finger_coarse_n1=finger_coarse_n1, channel_width_coarse_n1=channel_width_coarse_n1,
                                    finger_coarse_n2=finger_coarse_n2, channel_width_coarse_n2=channel_width_coarse_n2,

                                    #### Dictionary for Inverter FINE
                                    finger_fine_p1=finger_fine_p1, channel_width_fine_p1=channel_width_fine_p1,
                                    finger_fine_p2=finger_fine_p2, channel_width_fine_p2=channel_width_fine_p2,
                                    finger_fine_n1=finger_fine_n1, channel_width_fine_n1=channel_width_fine_n1,
                                    finger_fine_n2=finger_fine_n2, channel_width_fine_n2=channel_width_fine_n2,

                                    #### Dictionary for Inverter OUT
                                    finger_out_n=finger_out_n, channel_width_out_n=channel_width_out_n,
                                    finger_out_p=finger_out_p, channel_width_out_p=channel_width_out_p
        )
        self._DesignParameter['dcc_unit1']['_DesignObj']._CalculateDesignParameter(**dict_for_dcc)
        self._DesignParameter['dcc_unit2']['_DesignObj']._CalculateDesignParameter(**dict_for_dcc)

        self._DesignParameter['dcc_unit1']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['dcc_unit2']['_XYCoordinates'] = [[0, 0]]

if __name__ == '__main__':
    import random
    for i in range(0,1):
        # finger_on_n = random.randrange(1, 9, 1)
        # finger_on_p = random.randrange(1, 9, 1)
        # finger_coarse_p1 = random.randrange(1, 9, 1)
        # finger_coarse_p2 = random.randrange(1, 9, 1)
        # finger_coarse_n1 = random.randrange(1, 9, 1)
        # finger_coarse_n2 = random.randrange(1, 9, 1)
        # finger_fine_p1 = random.randrange(1, 9, 1)
        # finger_fine_p2 = random.randrange(1, 9, 1)
        # finger_fine_n1 = random.randrange(1, 9, 1)
        # finger_fine_n2 = random.randrange(1, 9, 1)
        #
        # finger_out_n = random.randrange(1,9,1)
        # finger_out_p = random.randrange(1,9,1)
        #
        # channel_width_on_n = random.randrange(200,650,50)
        # channel_width_coarse_n1 = random.randrange(200,650,50)
        # channel_width_coarse_n2 = random.randrange(200,650,50)
        # channel_width_fine_n1 = random.randrange(200,650,50)
        # channel_width_fine_n2 = random.randrange(200,650,50)
        # channel_width_out_n = random.randrange(200,650,50)
        #
        # channel_width_on_p = random.randrange(400,1350,50)
        # channel_width_coarse_p1 = random.randrange(400,1350,50)
        # channel_width_coarse_p2 = random.randrange(400,1350,50)
        # channel_width_fine_p1 = random.randrange(400,1350,50)
        # channel_width_fine_p2 = random.randrange(400,1350,50)
        # channel_width_out_p = random.randrange(400,1350,50)
        #
        # gap_bw_gates = random.randrange(400,800,50)
        # supply_num_coy = random.randrange(1,5,1)
        # coarse_fine_dimension = random.randrange(2, 8, 1)
        # dummy = True
        # channel_length = random.randrange(30,100, 10)

        finger_on_n = 1
        finger_on_p = 6
        finger_coarse_p1 = 7
        finger_coarse_p2 = 3
        finger_coarse_n1 = 4
        finger_coarse_n2 = 2
        finger_fine_p1 = 2
        finger_fine_p2 = 4
        finger_fine_n1 = 1
        finger_fine_n2 = 3

        finger_out_n = 5
        finger_out_p = 4

        channel_width_on_n = 200
        channel_width_coarse_n1 = 400
        channel_width_coarse_n2 = 600
        channel_width_fine_n1 = 500
        channel_width_fine_n2 = 250
        channel_width_out_n = 350

        channel_width_on_p = 500
        channel_width_coarse_p1 = 400
        channel_width_coarse_p2 = 600
        channel_width_fine_p1 = 550
        channel_width_fine_p2 = 640
        channel_width_out_p = 480

        gap_bw_gates = None
        supply_num_coy = None
        coarse_fine_dimension = 4
        dummy = True
        channel_length = 30

        Obj = DCC_Full()
        Obj._CalculateDesignParameter(  channel_length=channel_length, dummy=dummy, PCCrit=True, XVT='SLVT',
                                        supply_num_coy=None,
                                        coarse_fine_dimension=coarse_fine_dimension, gap_bw_gates=gap_bw_gates,

                                        #### Dictionary for Inverter ON
                                        finger_on_n=finger_on_n, channel_width_on_n=channel_width_on_n,
                                        finger_on_p=finger_on_p, channel_width_on_p=channel_width_on_p,

                                        #### Dictionary for Inverter COARSE
                                        finger_coarse_p1=finger_coarse_p1, channel_width_coarse_p1=channel_width_coarse_p1,
                                        finger_coarse_p2=finger_coarse_p2, channel_width_coarse_p2=channel_width_coarse_p2,
                                        finger_coarse_n1=finger_coarse_n1, channel_width_coarse_n1=channel_width_coarse_n1,
                                        finger_coarse_n2=finger_coarse_n2, channel_width_coarse_n2=channel_width_coarse_n2,

                                        #### Dictionary for Inverter FINE
                                        finger_fine_p1=finger_fine_p1, channel_width_fine_p1=channel_width_fine_p1,
                                        finger_fine_p2=finger_fine_p2, channel_width_fine_p2=channel_width_fine_p2,
                                        finger_fine_n1=finger_fine_n1, channel_width_fine_n1=channel_width_fine_n1,
                                        finger_fine_n2=finger_fine_n2, channel_width_fine_n2=channel_width_fine_n2,

                                        #### Dictionary for Inverter OUT
                                        finger_out_n=finger_out_n, channel_width_out_n=channel_width_out_n,
                                        finger_out_p=finger_out_p, channel_width_out_p=channel_width_out_p
                                        )

        Obj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=Obj._DesignParameter)
        _fileName = 'DCC_Full.gds'
        testStreamFile = open('./DCC_Full.gds', 'wb')
        tmp = Obj._CreateGDSStream(Obj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        import ftplib

        ftp = ftplib.FTP('141.223.29.62')
        ftp.login('kms95', 'dosel545')
        ftp.cwd('/mnt/sdb/kms95/OPUS/ss28')
        myfile = open('DCC_Full.gds', 'rb')
        ftp.storbinary('STOR DCC_Full.gds', myfile)
        myfile.close()
        ftp.close()
        # import DRCchecker
        #
        # _DRC = DRCchecker.DRCchecker('kms95','dosel545','/mnt/sdb/kms95/OPUS/ss28','/mnt/sdb/kms95/OPUS/ss28/DRC/run','DCC_Full','DCC_Full')
        # _DRC.DRCchecker()