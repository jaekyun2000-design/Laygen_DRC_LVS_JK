from generatorLib import StickDiagram
from generatorLib import DesignParameters
from generatorLib import DRC
from generatorLib.generator_models import Deserializer1toN
import time
start = time.time()
class Deserializer1toN_tb(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name='Deserializer1toN'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter(self,
                                  Deserialize1toN=2,
                                  TG1_Finger=1,
                                  TG1_NMWidth=200,
                                  TG1_PMWidth=400,
                                  TG2_Finger=2,
                                  TG2_NMWidth=200,
                                  TG2_PMWidth=400,

                                  TSI1_Finger=1,
                                  TSI1_NMWidth=200,
                                  TSI1_PMWidth=400,
                                  TSI2_Finger=1,
                                  TSI2_NMWidth=200,
                                  TSI2_PMWidth=400,

                                  INV1_Finger=3,
                                  INV1_NMWidth=200,
                                  INV1_PMWidth=400,

                                  INV2_Finger=1,
                                  INV2_NMWidth=200,
                                  INV2_PMWidth=400,
                                  INV3_Finger=1,
                                  INV3_NMWidth=200,
                                  INV3_PMWidth=400,

                                  INV4_Finger=4,
                                  INV4_NMWidth=200,
                                  INV4_PMWidth=400,

                                  TG3_Finger=1,
                                  TG3_NMWidth=200,
                                  TG3_PMWidth=400,

                                  TSI3_Finger=1,
                                  TSI3_NMWidth=200,
                                  TSI3_PMWidth=400,

                                  INV5_Finger=4,
                                  INV5_NMWidth=200,
                                  INV5_PMWidth=400,

                                  INV6_Finger=1,
                                  INV6_NMWidth=200,
                                  INV6_PMWidth=400,

                                  TG4_Finger=2,
                                  TG4_NMWidth=200,
                                  TG4_PMWidth=400,

                                  TSI4_Finger=1,
                                  TSI4_NMWidth=200,
                                  TSI4_PMWidth=400,

                                  INV7_Finger=4,
                                  INV7_NMWidth=200,
                                  INV7_PMWidth=400,
                                  INV8_Finger=4,
                                  INV8_NMWidth=200,
                                  INV8_PMWidth=400,
                                  INV9_Finger=1,
                                  INV9_NMWidth=200,
                                  INV9_PMWidth=400,
                                  INV10_Finger=1,
                                  INV10_NMWidth=200,
                                  INV10_PMWidth=400,

                                  TG1_Finger_clk=1,
                                  TG2_Finger_clk=2,
                                  TSI1_Finger_clk=1,
                                  TSI2_Finger_clk=1,
                                  INV1_Finger_clk=3,
                                  INV2_Finger_clk=1,
                                  INV3_Finger_clk=1,
                                  INV4_Finger_clk=4,
                                  INV5_Finger_clk=4,

                                  np_ratio=2,
                                  dummy=True,
                                  ChannelLength=30,
                                  GateSpacing=100,
                                  SDWidth=66,
                                  XVT='SLVT',
                                  CellHeight=3000,
                                  SupplyRailType=2

                                  ):

        _Name = self._DesignParameter['_Name']['_Name']

        Parameters_Deserializer1toN_1 = dict(

            Deserialize1toN=Deserialize1toN,
            TG1_Finger=TG1_Finger,
            TG1_NMWidth=TG1_NMWidth,
            TG1_PMWidth=TG1_PMWidth,
            TG2_Finger=TG2_Finger,
            TG2_NMWidth=TG2_NMWidth,
            TG2_PMWidth=TG2_PMWidth,

            TSI1_Finger=TSI1_Finger,
            TSI1_NMWidth=TSI1_NMWidth,
            TSI1_PMWidth=TSI1_PMWidth,
            TSI2_Finger=TSI2_Finger,
            TSI2_NMWidth=TSI2_NMWidth,
            TSI2_PMWidth=TSI2_PMWidth,

            INV1_Finger=INV1_Finger,
            INV1_NMWidth=INV1_NMWidth,
            INV1_PMWidth=INV1_PMWidth,

            INV2_Finger=INV2_Finger,
            INV2_NMWidth=INV2_NMWidth,
            INV2_PMWidth=INV2_PMWidth,
            INV3_Finger=INV3_Finger,
            INV3_NMWidth=INV3_NMWidth,
            INV3_PMWidth=INV3_PMWidth,

            INV4_Finger=INV4_Finger,
            INV4_NMWidth=INV4_NMWidth,
            INV4_PMWidth=INV4_PMWidth,

            TG3_Finger=TG3_Finger,
            TG3_NMWidth=TG3_NMWidth,
            TG3_PMWidth=TG3_PMWidth,

            TSI3_Finger=TSI3_Finger,
            TSI3_NMWidth=TSI3_NMWidth,
            TSI3_PMWidth=TSI3_PMWidth,

            INV5_Finger=INV5_Finger,
            INV5_NMWidth=INV5_NMWidth,
            INV5_PMWidth=INV5_PMWidth,
            INV6_Finger=INV6_Finger,
            INV6_NMWidth=INV6_NMWidth,
            INV6_PMWidth=INV6_PMWidth,

            TG4_Finger=TG4_Finger,
            TG4_NMWidth=TG4_NMWidth,
            TG4_PMWidth=TG4_PMWidth,

            TSI4_Finger=TSI4_Finger,
            TSI4_NMWidth=TSI4_NMWidth,
            TSI4_PMWidth=TSI4_PMWidth,

            INV7_Finger=INV7_Finger,
            INV7_NMWidth=INV7_NMWidth,
            INV7_PMWidth=INV7_PMWidth,
            INV8_Finger=INV8_Finger,
            INV8_NMWidth=INV8_NMWidth,
            INV8_PMWidth=INV8_PMWidth,
            INV9_Finger=INV9_Finger,
            INV9_NMWidth=INV9_NMWidth,
            INV9_PMWidth=INV9_PMWidth,
            INV10_Finger=INV10_Finger,
            INV10_NMWidth=INV10_NMWidth,
            INV10_PMWidth=INV10_PMWidth,

            TG1_Finger_clk=TG1_Finger_clk,
            TG2_Finger_clk=TG2_Finger_clk,

            TSI1_Finger_clk=TSI1_Finger_clk,
            TSI2_Finger_clk=TSI2_Finger_clk,

            INV1_Finger_clk=INV1_Finger_clk,
            INV2_Finger_clk=INV2_Finger_clk,
            INV3_Finger_clk=INV3_Finger_clk,
            INV4_Finger_clk=INV4_Finger_clk,
            INV5_Finger_clk=INV5_Finger_clk,

            np_ratio=np_ratio,
            dummy=dummy,
            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            SDWidth=SDWidth,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType
        )


        ##################################### Placement #################################################
        self._DesignParameter['Deserializer1toN_1'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,_DesignObj=Deserializer1toN.Deserializer1toN(_Name='Deserializer1toN_1In{}'.format(_Name)))[0]
        self._DesignParameter['Deserializer1toN_1']['_DesignObj']._CalculateDesignParameter(**Parameters_Deserializer1toN_1)
        self._DesignParameter['Deserializer1toN_1']['_XYCoordinates'] = [[0, 0]]


''' INV2&3 # of Fingers should be less than 7(6 max)
    otherwise, INV inner routing and qb routing will be overlapped'''
################################ DRC Check #################################
import random
if __name__ == '__main__':
        # list = [2, 4, 8, 16, 32]
        # Deserialize1toN = random.choice(list)
        # TG1_Finger = random.randint(1, 10)
        # TG2_Finger = random.randint(1, 10)
        #
        # INV1_Finger = random.randint(1, 10)
        # INV2_Finger = random.randint(1, 10)
        # INV3_Finger = random.randint(1, 10)
        # INV4_Finger = random.randint(1, 10)
        #
        # TG3_Finger = random.randint(1, 10)
        # INV5_Finger = random.randint(1, 10)
        # INV6_Finger = random.randint(1, 10)
        #
        # TG4_Finger = random.randint(1, 10)
        #
        # INV7_Finger = random.randint(1, 10)
        # INV8_Finger = random.randint(1, 10)
        # INV9_Finger = random.randint(1, 10)
        # INV10_Finger = random.randint(1, 10)

        TG1_Finger = 1
        TG2_Finger = 2
        TSI1_Finger = 1
        TSI2_Finger = 1
        INV1_Finger = 3
        INV2_Finger = 1
        INV3_Finger = 1
        INV4_Finger = 3

        TG3_Finger = 2
        TSI3_Finger = 1
        INV5_Finger = 4
        INV6_Finger = 4
        TG4_Finger = 2
        TSI4_Finger = 1
        INV7_Finger = 4
        INV8_Finger = 4
        INV9_Finger = 1
        INV10_Finger = 1

        Deserialize1toN = 32
        # TSI1_Finger=TSI2_Finger=TSI3_Finger=TSI4_Finger=1
        # random.randrange(200, 250, 10)

        np_ratio = 2#random.randint(2, 3)
        TG1_NMWidth = TG2_NMWidth = TG3_NMWidth = TG4_NMWidth = TSI1_NMWidth = TSI2_NMWidth = TSI3_NMWidth = TSI4_NMWidth = INV1_NMWidth = INV2_NMWidth = INV3_NMWidth \
            = INV4_NMWidth = INV5_NMWidth = INV6_NMWidth = INV7_NMWidth = INV8_NMWidth = INV9_NMWidth = INV10_NMWidth = 200 #random.randrange(200, 400, 50)  # default 200~400
        TG1_PMWidth = TG2_PMWidth = TG3_PMWidth = TG4_PMWidth = TSI1_PMWidth = TSI2_PMWidth = TSI3_PMWidth = TSI4_PMWidth = INV1_PMWidth = INV2_PMWidth = INV3_PMWidth \
            = INV4_PMWidth = INV5_PMWidth = INV6_PMWidth = INV7_PMWidth = INV8_PMWidth = INV9_PMWidth = INV10_PMWidth = TG1_NMWidth * np_ratio  # random.randint(2, 3)  ### np ratio = 2~3사이 가능

        dummy = False  # random.randint(0, 1) #only use 1:32 archetecture
        ChannelLength = 30# random.choice([30, 40])
        GateSpacing = 100
        SDWidth = 66
        list_XVT = ['SLVT', 'RVT', 'LVT', 'HVT']
        XVT_random = random.choice(list_XVT)
        XVT = 'SLVT'  # XVT_random #XVT_random
        CellHeight = 1800  # 3000
        SupplyRailType = 2  # random.randint(1, 2)


        #
        # Deserialize1toN=32
        #
        # np_ratio = 2 # 2~3
        # TG1_NMWidth =TG2_NMWidth=TG3_NMWidth= TG4_NMWidth=TSI1_NMWidth=TSI2_NMWidth=TSI3_NMWidth=TSI4_NMWidth=INV1_NMWidth=INV2_NMWidth=INV3_NMWidth\
        #     =INV4_NMWidth=INV5_NMWidth=INV6_NMWidth=INV7_NMWidth=INV8_NMWidth=INV9_NMWidth=INV10_NMWidth= 400
        # TG1_PMWidth = TG2_PMWidth=TG3_PMWidth=TG4_PMWidth=TSI1_PMWidth=TSI2_PMWidth=TSI3_PMWidth=TSI4_PMWidth=INV1_PMWidth=INV2_PMWidth=INV3_PMWidth\
        #     =INV4_PMWidth=INV5_PMWidth=INV6_PMWidth=INV7_PMWidth=INV8_PMWidth=INV9_PMWidth=INV10_PMWidth= TG1_NMWidth * np_ratio
        # ChannelLength = 30

        TG1_Finger_clk = TG1_Finger
        TG2_Finger_clk = TG2_Finger
        TSI1_Finger_clk = TSI1_Finger = TSI2_Finger = TSI3_Finger = TSI4_Finger = 1
        TSI2_Finger_clk = TSI2_Finger
        INV1_Finger_clk = INV1_Finger
        INV2_Finger_clk = INV2_Finger
        INV3_Finger_clk = INV3_Finger
        INV4_Finger_clk = INV5_Finger
        INV5_Finger_clk = INV6_Finger


        DesignParameters._Technology = 'SS28nm'
        TopObj = Deserializer1toN_tb(_DesignParameter=None, _Name='Deserializer1toN_tb')
        TopObj._CalculateDesignParameter(
            Deserialize1toN=Deserialize1toN,
            TG1_Finger=TG1_Finger,
            TG1_NMWidth=TG1_NMWidth,
            TG1_PMWidth=TG1_PMWidth,
            TG2_Finger=TG2_Finger,
            TG2_NMWidth=TG2_NMWidth,
            TG2_PMWidth=TG2_PMWidth,

            TSI1_Finger=TSI1_Finger,
            TSI1_NMWidth=TSI1_NMWidth,
            TSI1_PMWidth=TSI1_PMWidth,
            TSI2_Finger=TSI2_Finger,
            TSI2_NMWidth=TSI2_NMWidth,
            TSI2_PMWidth=TSI2_PMWidth,

            INV1_Finger=INV1_Finger,
            INV1_NMWidth=INV1_NMWidth,
            INV1_PMWidth=INV1_PMWidth,

            INV2_Finger=INV2_Finger,
            INV2_NMWidth=INV2_NMWidth,
            INV2_PMWidth=INV2_PMWidth,
            INV3_Finger=INV3_Finger,
            INV3_NMWidth=INV3_NMWidth,
            INV3_PMWidth=INV3_PMWidth,

            INV4_Finger=INV4_Finger,
            INV4_NMWidth=INV4_NMWidth,
            INV4_PMWidth=INV4_PMWidth,

            TG3_Finger=TG3_Finger,
            TG3_NMWidth=TG3_NMWidth,
            TG3_PMWidth=TG3_PMWidth,

            TSI3_Finger=TSI3_Finger,
            TSI3_NMWidth=TSI3_NMWidth,
            TSI3_PMWidth=TSI3_PMWidth,

            INV5_Finger=INV5_Finger,
            INV5_NMWidth=INV5_NMWidth,
            INV5_PMWidth=INV5_PMWidth,
            INV6_Finger=INV6_Finger,
            INV6_NMWidth=INV6_NMWidth,
            INV6_PMWidth=INV6_PMWidth,

            TG4_Finger=TG4_Finger,
            TG4_NMWidth=TG4_NMWidth,
            TG4_PMWidth=TG4_PMWidth,

            TSI4_Finger=TSI4_Finger,
            TSI4_NMWidth=TSI4_NMWidth,
            TSI4_PMWidth=TSI4_PMWidth,

            INV7_Finger=INV7_Finger,
            INV7_NMWidth=INV7_NMWidth,
            INV7_PMWidth=INV7_PMWidth,
            INV8_Finger=INV8_Finger,
            INV8_NMWidth=INV8_NMWidth,
            INV8_PMWidth=INV8_PMWidth,
            INV9_Finger=INV9_Finger,
            INV9_NMWidth=INV9_NMWidth,
            INV9_PMWidth=INV9_PMWidth,
            INV10_Finger=INV10_Finger,
            INV10_NMWidth=INV10_NMWidth,
            INV10_PMWidth=INV10_PMWidth,

            TG1_Finger_clk=TG1_Finger_clk,
            TG2_Finger_clk=TG2_Finger_clk,

            TSI1_Finger_clk=TSI1_Finger_clk,
            TSI2_Finger_clk=TSI2_Finger_clk,

            INV1_Finger_clk=INV1_Finger_clk,
            INV2_Finger_clk=INV2_Finger_clk,
            INV3_Finger_clk=INV3_Finger_clk,
            INV4_Finger_clk=INV4_Finger_clk,
            INV5_Finger_clk=INV5_Finger_clk,

            np_ratio=np_ratio,
            dummy=dummy,
            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            SDWidth=SDWidth,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType)

        TopObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=TopObj._DesignParameter)
        testStreamFile = open('./Deserializer1toN.gds', 'wb')
        tmp = TopObj._CreateGDSStream(TopObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        print('#############################      Sending to FTP Server...      ##############################')

        import ftplib
        ftp = ftplib.FTP('141.223.24.53')
        ftp.login('ljw95', 'dlwodn123')
        ftp.cwd('/mnt/sdc/ljw95/OPUS/ss28')
        myfile = open('Deserializer1toN.gds', 'rb')
        ftp.storbinary('STOR Deserializer1toN.gds', myfile)
        myfile.close()
        import DRCchecker

        end = time.time()
        print("TG1_Finger = ", TG1_Finger)
        print("TG2_Finger = ", TG2_Finger)
        print("TG3_Finger = ", TG3_Finger)
        print("TG3_Finger = ", TG4_Finger)
        print("TSI1_Finger = ", TSI1_Finger)
        print("TSI2_Finger = ", TSI2_Finger)
        print("TSI3_Finger = ", TSI3_Finger)
        print("TSI1_Finger = ", TSI4_Finger)
        print("INV1_Finger = ", INV1_Finger)
        print("INV2_Finger = ", INV2_Finger)
        print("INV3_Finger = ", INV3_Finger)
        print("INV4_Finger = ", INV4_Finger)
        print("INV5_Finger = ", INV5_Finger)
        print("INN6_Finger = ", INV6_Finger)
        print("INV3_Finger = ", INV7_Finger)
        print("INV4_Finger = ", INV8_Finger)
        print("INV5_Finger = ", INV9_Finger)
        print("INN6_Finger = ", INV10_Finger)

        # a = DRCchecker.DRCchecker('ljw95','dlwodn123','/mnt/sdc/ljw95/OPUS/ss28','/mnt/sdc/ljw95/OPUS/ss28/DRC/run','Deserializer1toN','Deserializer1toN',None)
        # a.DRCchecker()
        print('   Sending to FTP Server & StreamIn...   '.center(105, '#'))

        print('      Finished       '.center(105, '#'))
        # print("DRC Clean!!!")

        print(f"{end - start:.5f} sec")
        # generation_time = time.time()
        # print("Generation time=",generation_time)