import math
import copy

#
from generatorLib import StickDiagram
from generatorLib import DesignParameters
from generatorLib import DRC

#
from generatorLib.generator_models import Fill_cap
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaMet22Met3
from generatorLib.generator_models import ViaMet32Met4
from generatorLib.generator_models import ViaMet42Met5
from generatorLib.generator_models import Deserializer1to32
from generatorLib.generator_models import Deserializer1toN
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import Clk_Driver



class Deserializer2toN(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name='Deserializer2toN'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name


    def _CalculateDesignParameter(self,
                                  Deserialize1toN=32,
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

                                  dummy=True,
                                  ChannelLength=30,
                                  GateSpacing=100,
                                  SDWidth=66,
                                  XVT='SLVT',
                                  CellHeight=1800,
                                  SupplyRailType=2,
                                  Fillcap=True
                                  ):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        UnitPitch = ChannelLength + GateSpacing



        if TG1_NMWidth>200 :
            CellHeight=2000
        Parameters_Deserializer1to32_1 = dict(
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

            dummy=dummy,
            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            SDWidth=SDWidth,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType
        )
        Parameters_Deserializer1to32_2 = dict(
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

            dummy=dummy,
            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            SDWidth=SDWidth,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType
        )
        Parameters_Clk_Driver_1 = dict(
            TG1_Finger=TG1_Finger_clk,
            TG1_NMWidth=TG1_NMWidth,
            TG1_PMWidth=TG1_PMWidth,
            TG2_Finger=TG2_Finger_clk,
            TG2_NMWidth=TG2_NMWidth,
            TG2_PMWidth=TG2_PMWidth,

            TSI1_Finger=TSI1_Finger_clk,
            TSI1_NMWidth=TSI1_NMWidth,
            TSI1_PMWidth=TSI1_PMWidth,
            TSI2_Finger=TSI2_Finger_clk,
            TSI2_NMWidth=TSI2_NMWidth,
            TSI2_PMWidth=TSI2_PMWidth,

            INV1_Finger=INV1_Finger_clk,
            INV1_NMWidth=INV1_NMWidth,
            INV1_PMWidth=INV1_PMWidth,

            INV2_Finger=INV2_Finger_clk,
            INV2_NMWidth=INV2_NMWidth,
            INV2_PMWidth=INV2_PMWidth,
            INV3_Finger=INV3_Finger_clk,
            INV3_NMWidth=INV3_NMWidth,
            INV3_PMWidth=INV3_PMWidth,

            INV4_Finger=INV4_Finger_clk,
            INV4_NMWidth=INV4_NMWidth,
            INV4_PMWidth=INV4_PMWidth,

            INV5_Finger=INV5_Finger_clk,
            INV5_NMWidth=INV5_NMWidth,
            INV5_PMWidth=INV5_PMWidth,

            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            SDWidth=SDWidth,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType
        )
        Parameters_Clk_Driver_2 = dict(
            TG1_Finger=TG1_Finger_clk,
            TG1_NMWidth=TG1_NMWidth,
            TG1_PMWidth=TG1_PMWidth,
            TG2_Finger=TG2_Finger_clk,
            TG2_NMWidth=TG2_NMWidth,
            TG2_PMWidth=TG2_PMWidth,

            TSI1_Finger=TSI1_Finger_clk,
            TSI1_NMWidth=TSI1_NMWidth,
            TSI1_PMWidth=TSI1_PMWidth,
            TSI2_Finger=TSI2_Finger_clk,
            TSI2_NMWidth=TSI2_NMWidth,
            TSI2_PMWidth=TSI2_PMWidth,

            INV1_Finger=INV1_Finger_clk,
            INV1_NMWidth=INV1_NMWidth,
            INV1_PMWidth=INV1_PMWidth,

            INV2_Finger=INV2_Finger_clk,
            INV2_NMWidth=INV2_NMWidth,
            INV2_PMWidth=INV2_PMWidth,
            INV3_Finger=INV3_Finger_clk,
            INV3_NMWidth=INV3_NMWidth,
            INV3_PMWidth=INV3_PMWidth,

            INV4_Finger=INV4_Finger_clk,
            INV4_NMWidth=INV4_NMWidth,
            INV4_PMWidth=INV4_PMWidth,

            INV5_Finger=INV5_Finger_clk,
            INV5_NMWidth=INV5_NMWidth,
            INV5_PMWidth=INV5_PMWidth,

            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            SDWidth=SDWidth,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType
        )

        Parameters_Fill_cap_1 = dict(
            Cap_poly_x_length=500,
            Cap_poly_nmos_y_width=200,
            Cap_poly_pmos_y_width=400,
            Cell_height=CellHeight,
            Power_CO_Pitch=500,
            Power_CO_Num=None,
            vss_nmosgate_space=58,
            vdd_pmosgate_space=58,
            gate2pwr_co_num=2,
            XVT=XVT
        )

#####################################################################################################################
#####################################################################################################################
############################################## Deserializer 2to64 ###################################################
#####################################################################################################################
#####################################################################################################################
        tmpMet2Width = 66
        tmpDRC_Met2Spacing = 86
        tmpVia1YWidth = 100
        tmpViaMet2Width = 134
        tmpViaminWidth = 170
        tmpDSspace = 130

        ##################################### Placement #################################################
        self._DesignParameter['Deserializer1toN_1'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=Deserializer1to32.Deserializer1toN(_Name='Deserializer1toN_1In{}'.format(_Name)))[0]
        self._DesignParameter['Deserializer1toN_1']['_DesignObj']._CalculateDesignParameter(**Parameters_Deserializer1to32_1)
        self._DesignParameter['Deserializer1toN_1']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['Deserializer1toN_2'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=Deserializer1to32.Deserializer1toN(_Name='DeserializertoN_2In{}'.format(_Name)))[0]
        self._DesignParameter['Deserializer1toN_2']['_DesignObj']._CalculateDesignParameter(**Parameters_Deserializer1to32_2)
        self._DesignParameter['Deserializer1toN_2']['_XYCoordinates'] = [[0, 0]]


        self._DesignParameter['Clk_Driver_1'] = self._SrefElementDeclaration(
            _Reflect=[1, 0, 0], _Angle=0,
            _DesignObj=Clk_Driver.Clk_Driver(_Name='Clk_Driver_1In{}'.format(_Name)))[0]
        self._DesignParameter['Clk_Driver_1']['_DesignObj']._CalculateDesignParameter(**Parameters_Clk_Driver_1)
        self._DesignParameter['Clk_Driver_1']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['Clk_Driver_2'] = self._SrefElementDeclaration(
            _Reflect=[1, 0, 0], _Angle=0,
            _DesignObj=Clk_Driver.Clk_Driver(_Name='Clk_Driver_2In{}'.format(_Name)))[0]
        self._DesignParameter['Clk_Driver_2']['_DesignObj']._CalculateDesignParameter(**Parameters_Clk_Driver_2)
        self._DesignParameter['Clk_Driver_2']['_XYCoordinates'] = [[0, 0]]


        self._DesignParameter['Deserializer1toN_2']['_XYCoordinates'] = [[self.getXY('Deserializer1toN_1')[0][0],
                                                                   self._DesignParameter['Deserializer1toN_1']['_XYCoordinates'][0][1] + 10 * CellHeight]]

        self._DesignParameter['Clk_Driver_1']['_XYCoordinates'] = [[
            self.getXY('Deserializer1toN_1')[0][0] + self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['Clk_Driver_1']['_XYCoordinates'][0][0] ,
            self._DesignParameter['Deserializer1toN_1']['_XYCoordinates'][0][1]+6*CellHeight]]

        self._DesignParameter['Clk_Driver_2']['_XYCoordinates'] = [[
                self.getXY('Clk_Driver_1')[0][0] + self._DesignParameter['Clk_Driver_1']['_DesignObj'].CellXWidth + UnitPitch,
                self._DesignParameter['Clk_Driver_1']['_XYCoordinates'][0][1]]]


####################### Clk_Driver 1 to 2 connection ##########################

        self._DesignParameter['_Met3_clk_connect'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met3_clk_connect']['_XYCoordinates'] = [
            [[self.getXY('Clk_Driver_1')[0][0] + self._DesignParameter['Clk_Driver_1']['_DesignObj'].f[0],
              -self.getXY('Clk_Driver_1')[0][1] - self._DesignParameter['Clk_Driver_1']['_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclkb+12*CellHeight], \
             [self.getXY('Clk_Driver_1')[0][0] + self._DesignParameter['Clk_Driver_1']['_DesignObj'].f90b[0] + tmpMet2Width / 2,
              -self.getXY('Clk_Driver_1')[0][1]
              -self._DesignParameter['Clk_Driver_1']['_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclkb+12*CellHeight]], \
            [[self.getXY('Clk_Driver_2')[0][0] + self._DesignParameter['Clk_Driver_2']['_DesignObj'].clkinput[0],
              -self.getXY('Clk_Driver_2')[0][1] - self._DesignParameter['Clk_Driver_2']['_DesignObj'].clkinput[1]+12*CellHeight], \
             [self.getXY('Clk_Driver_1')[0][0] + self._DesignParameter['Clk_Driver_1']['_DesignObj'].f90b[0] + tmpMet2Width / 2,
              -self.getXY('Clk_Driver_2')[0][1] - self._DesignParameter['Clk_Driver_2']['_DesignObj'].clkinput[1]+12*CellHeight]], \
            [[self.getXY('Clk_Driver_1')[0][0] + self._DesignParameter['Clk_Driver_1']['_DesignObj'].f90b[0],
              -self.getXY('Clk_Driver_2')[0][1] - self._DesignParameter['Clk_Driver_2']['_DesignObj'].clkinput[1] + tmpMet2Width / 2+12*CellHeight], \
             [self.getXY('Clk_Driver_1')[0][0] + self._DesignParameter['Clk_Driver_1']['_DesignObj'].f90b[0],
              -self.getXY('Clk_Driver_1')[0][1] - self._DesignParameter['Clk_Driver_1']['_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclkb - tmpMet2Width / 2+12*CellHeight]]]

        self._DesignParameter['_ViaMet22Met3_Clk_Drive'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='_ViaMet22Met3_Clk_DriveIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3_Clk_Drive']['_DesignObj']._CalculateDesignParameterSameEnclosure(
            **dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=1))
        self._DesignParameter['_ViaMet22Met3_Clk_Drive']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet22Met3_Clk_Drive']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet22Met3_Clk_Drive']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = tmpVia1YWidth

        self._DesignParameter['_ViaMet22Met3_Clk_Drive']['_XYCoordinates'] = [
            [self.getXY('Clk_Driver_1')[0][0] + self._DesignParameter['Clk_Driver_1']['_DesignObj'].f[0],
             -self.getXY('Clk_Driver_1')[0][1] -
             self._DesignParameter['Clk_Driver_1']['_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclkb + tmpViaMet2Width / 2 - tmpMet2Width / 2+12*CellHeight], \
            [self.getXY('Clk_Driver_1')[0][0] + self._DesignParameter['Clk_Driver_1']['_DesignObj'].f90[0],
             -self.getXY('Clk_Driver_1')[0][1] -
             self._DesignParameter['Clk_Driver_1']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclkb + tmpViaMet2Width / 2 - tmpMet2Width / 2+12*CellHeight], \
            [self.getXY('Clk_Driver_2')[0][0] + self._DesignParameter['Clk_Driver_2']['_DesignObj'].f[0],
             -self.getXY('Clk_Driver_2')[0][1] -
             self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclkb + tmpViaMet2Width / 2 - tmpMet2Width / 2+12*CellHeight], \
            [self.getXY('Clk_Driver_2')[0][0] + self._DesignParameter['Clk_Driver_2']['_DesignObj'].f90[0],
             -self.getXY('Clk_Driver_2')[0][1] -
             self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclkb + tmpViaMet2Width / 2 - tmpMet2Width / 2+12*CellHeight]]

        self._DesignParameter['_Met3_clk_drc'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met3_clk_drc']['_XYCoordinates'] = [[[self.getXY('Clk_Driver_2')[0][0] + self._DesignParameter['Clk_Driver_2']['_DesignObj'].f[0],
             -self.getXY('Clk_Driver_2')[0][1] -self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclkb+12*CellHeight],\
            [self.getXY('Clk_Driver_2')[0][0] + self._DesignParameter['Clk_Driver_2']['_DesignObj'].f[0],\
             -self.getXY('Clk_Driver_2')[0][1] -self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclkb-70+12*CellHeight]]]

        # XVTLayer
        assert XVT in ('SLVT', 'LVT', 'RVT', 'HVT')
        leftBoundary = self.getXYLeft('Clk_Driver_1', 'DFFQb1', 'TG1', 'XVT_boundary_1')[0][0]


        rightBoundary = self.getXYRight('Clk_Driver_2', 'DFFQb2', 'INV5', 'XVTLayer')[0][0]

        YCoord = [self.getXY('Clk_Driver_2', 'DFFQb1', 'TG1', 'XVT_boundary_1')[0][1]]

        self._DesignParameter['XVTLayer'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping[XVT][0], _Datatype=DesignParameters._LayerMapping[XVT][1],
            _Width=self.getYWidth('Clk_Driver_2', 'DFFQb2', 'INV5', 'XVTLayer')
        )
        self._DesignParameter['XVTLayer']['_XYCoordinates'] = [
            [[rightBoundary, YCoord[0]], [leftBoundary, YCoord[0]]]]

        # NWLayer
        NW_margin = 10
        leftBoundary = self.getXYLeft('Clk_Driver_1', 'DFFQb1', 'TG1', 'NWELL_boundary_0')[0][0]


        rightBoundary = self.getXYRight('Clk_Driver_2', 'DFFQb2', 'INV5', '_NWLayerBoundary')[0][0]

        YCoord = [(self.getXYTop('Clk_Driver_2', 'DFFQb1', '_NWLayer')[0][1] -
                   self.getXYBot('Clk_Driver_2', 'DFFQb1', '_NWLayer')[0][1]) / 2 +
                  self.getXYBot('Clk_Driver_2', 'DFFQb1', '_NWLayer')[0][1]]



        self._DesignParameter['_NWLayer'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _Width=self.getXYTop('Deserializer1toN_1','DeMux1to2_1', 'DFF_Latch', '_NWLayer')[0][1] -
                   self.getXYBot('Deserializer1toN_1','DeMux1to2_1', 'DFF_Latch', '_NWLayer')[0][1] + NW_margin
        )
        self._DesignParameter['_NWLayer']['_XYCoordinates'] = [
            [[rightBoundary, YCoord[0]], [leftBoundary,YCoord[0]]]]


        if Fillcap is True:
            fillcap_spacing=384
            self._DesignParameter['Fill_cap_1'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=Fill_cap.FillCapCell(_Name='Fill_cap_1In{}'.format(_Name)))[0]
            self._DesignParameter['Fill_cap_1']['_DesignObj']._CalculateDesignParameter(**Parameters_Fill_cap_1)
            self._DesignParameter['Fill_cap_1']['_XYCoordinates'] = [[0, 0]]


            self._DesignParameter['Fill_cap_1']['_XYCoordinates'] = [[
                self.getXY('Deserializer1toN_1')[0][0] + self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['Clk_Driver_1']['_XYCoordinates'][0][0]+fillcap_spacing,
                self._DesignParameter['Deserializer1toN_1']['_XYCoordinates'][0][1]]]
            self._DesignParameter['Fill_cap_1']['_XYCoordinates'].append(
                    [self.getXY('Deserializer1toN_1')[0][0] + self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['Clk_Driver_1']['_XYCoordinates'][0][0]+fillcap_spacing ,
                    self._DesignParameter['Deserializer1toN_1']['_XYCoordinates'][0][1]+10*CellHeight])
            k=0
            num=math.floor(self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_1']['_DesignObj'].CellXWidth/(2*fillcap_spacing+tmpDSspace))
            for i in range(num-1):
                k=k+1
                self._DesignParameter['Fill_cap_1']['_XYCoordinates'].append(
                    [self.getXY('Deserializer1toN_1')[0][0] + self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['Clk_Driver_1']['_XYCoordinates'][0][0]+fillcap_spacing+k*tmpDSspace+2*k*fillcap_spacing,
                    self._DesignParameter['Deserializer1toN_1']['_XYCoordinates'][0][1]])
                self._DesignParameter['Fill_cap_1']['_XYCoordinates'].append(
                    [self.getXY('Deserializer1toN_1')[0][0] + self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['Clk_Driver_1']['_XYCoordinates'][0][0]+fillcap_spacing +k*tmpDSspace+2*k*fillcap_spacing,
                    self._DesignParameter['Deserializer1toN_1']['_XYCoordinates'][0][1]+10*CellHeight])
                self._DesignParameter['Fill_cap_1']['_DesignObj']._DesignParameter['vssrail']['_XYCoordinates']=[]
                self._DesignParameter['Fill_cap_1']['_DesignObj']._DesignParameter['vddrail']['_XYCoordinates'] = []


######################## Clk driver Delete #####################################
        self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['Clk_Driver_1']['_XYCoordinates'] = []
        self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['Clk_Driver_2']['_XYCoordinates'] = []
        self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['Clk_Driver_1']['_XYCoordinates'] = []
        self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['Clk_Driver_2']['_XYCoordinates'] = []


        ####################### CLK input Routing ##########################
        clkrouting=200
        clkrouting4=100

        self._DesignParameter['_Met4_clkin'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _Width=clkrouting4
        )
        self._DesignParameter['_Met4_clkin']['_XYCoordinates'] = [[[self.getXY('Clk_Driver_1')[0][0] +self._DesignParameter['Clk_Driver_1']['_DesignObj'].clkinput[0] + 4 * tmpDSspace,
                                                                    15 * CellHeight+ tmpDSspace+3*clkrouting/2-tmpMet2Width/2], \
                                                                   [self.getXY('Clk_Driver_1')[0][0] +self._DesignParameter['Clk_Driver_1']['_DesignObj'].clkinput[0] + 4 * tmpDSspace,
                                                                    -self.getXY('Clk_Driver_1')[0][1] -self._DesignParameter['Clk_Driver_1']['_DesignObj'].clkinput[1]+12*CellHeight]], \
                                                                  [[self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to2_3']['_DesignObj'].clk[0] + 4 * tmpDSspace,
                                                                    self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to2_3']['_DesignObj'].clk[1]],
                                                                   [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to2_3']['_DesignObj'].clk[0] + 4 * tmpDSspace,
                                                                        5 * CellHeight + tmpDSspace + 3 * clkrouting / 2 - tmpMet2Width / 2]], \
                                                                  [[self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to2_3']['_DesignObj'].clkb[0] - 4 * tmpDSspace,
                                                                    self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to2_3']['_DesignObj'].clkb[1]],
                                                                   [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to2_3']['_DesignObj'].clkb[0] - 4 * tmpDSspace,
                                                                       5 * CellHeight - tmpDSspace - 3 * clkrouting / 2 + tmpMet2Width / 2]]]  # clk_dividier signal

        self._DesignParameter['_ViaMet32Met4_clkin'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='_ViaMet32Met4_clkinIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4_clkin']['_DesignObj']._CalculateDesignParameterSameEnclosure(
            **dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=1))
        self._DesignParameter['_ViaMet32Met4_clkin']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet32Met4_clkin']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet32Met4_clkin']['_DesignObj']._DesignParameter['_COLayer']['_XWidth'] = tmpVia1YWidth

        self._DesignParameter['_ViaMet32Met4_clkin']['_XYCoordinates'] = [
            [self.getXY('Clk_Driver_1')[0][0] + self._DesignParameter['Clk_Driver_1']['_DesignObj'].clkinput[0] + 4 * tmpDSspace,
             15 * CellHeight+ tmpDSspace+3*clkrouting/2-tmpMet2Width/2], \
            [self.getXY('Clk_Driver_1')[0][0] + self._DesignParameter['Clk_Driver_1']['_DesignObj'].clkinput[0] + 4 * tmpDSspace,
             -self.getXY('Clk_Driver_1')[0][1] - self._DesignParameter['Clk_Driver_1']['_DesignObj'].clkinput[1] + 12 * CellHeight], \
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to2_3']['_DesignObj'].clkb[0] - 4 * tmpDSspace,
             self.getXY('Deserializer1toN_2')[0][1] +self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to2_3']['_DesignObj'].clkb[1]],\
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to2_3']['_DesignObj'].clk[0] + 4 * tmpDSspace,
              self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to2_3']['_DesignObj'].clk[1]]]


        ####################### CLK input Routing end ##########################

######################## Clk  input Routing Delete #####################################
        self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['_Met3_clkin']['_XYCoordinates'] = []
        #self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['_Met4_clkin']['_XYCoordinates'] = []
        self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['_ViaMet32Met4_clkin2']['_XYCoordinates'] = []
        self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['_Met4_clkin_2']['_XYCoordinates'] = []
        self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['_ViaMet32Met4_clkin_2']['_XYCoordinates'] = []

        self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['_Met4_clkin_2']['_XYCoordinates'] = []
        self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['_ViaMet32Met4_clkin_2']['_XYCoordinates'] = []

######################## Clk driver 1 to 2 connection Delete #####################################
        self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['_Met3_clk_connect']['_XYCoordinates'] = []
        self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['_ViaMet22Met3_Clk_Drive']['_XYCoordinates'] = []
        self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['_Met3_clk_drc']['_XYCoordinates'] = []
        self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['_Met3_clk_connect']['_XYCoordinates'] = []
        self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['_ViaMet22Met3_Clk_Drive']['_XYCoordinates'] = []
        self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['_Met3_clk_drc']['_XYCoordinates'] = []

############ 1st to 2nd stage clk and clkb via Delete ########################################

        self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['_ViaMet32Met4_clk1st_del']['_XYCoordinates'] = []
        self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['_ViaMet32Met4_clk1st_2_del']['_XYCoordinates'] = []
        self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['_ViaMet32Met4_clk1st_del']['_XYCoordinates'] = []
        self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['_ViaMet32Met4_clk1st_2_del']['_XYCoordinates'] = []
        self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['_Met3_clk1st_via2']['_XYCoordinates'] = []
        self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['_Met3_clk1st_via2']['_XYCoordinates'] = []

        ####################### 1st to 2nd stage clk and clkb  ##########################

        self._DesignParameter['_Met4_clk1st'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met5_clk1st'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met3_clk1st_revise'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=tmpMet2Width
        )

        self._DesignParameter['_ViaMet32Met4_clk1st'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='_ViaMet32Met4_clk1stIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4_clk1st']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=1))
        self._DesignParameter['_ViaMet32Met4_clk1st']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet32Met4_clk1st']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet32Met4_clk1st']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = tmpVia1YWidth

        self._DesignParameter['_ViaMet32Met4_clk1st_2'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='_ViaMet32Met4_clk1st_2In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=1))
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_DesignObj']._DesignParameter['_COLayer']['_XWidth'] = tmpVia1YWidth

        self._DesignParameter['_ViaMet42Met5_clk1st'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_Name='_ViaMet42Met5_clk1stIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet42Met5_clk1st']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet42Met5NumberOfCOX=1, _ViaMet42Met5NumberOfCOY=1))
        self._DesignParameter['_ViaMet42Met5_clk1st']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet42Met5_clk1st']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet42Met5_clk1st']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = tmpVia1YWidth

        self._DesignParameter['_ViaMet42Met5_clk1st_2'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_Name='_ViaMet42Met5_clk1st_2In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet42Met5_clk1st_2']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet42Met5NumberOfCOX=1, _ViaMet42Met5NumberOfCOY=1))
        self._DesignParameter['_ViaMet42Met5_clk1st_2']['_DesignObj']._DesignParameter['_Met5Layer']['_XWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet42Met5_clk1st_2']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet42Met5_clk1st_2']['_DesignObj']._DesignParameter['_COLayer']['_XWidth'] = tmpVia1YWidth


        self._DesignParameter['_ViaMet32Met4_clk1st']['_XYCoordinates']=[[self.getXY('Clk_Driver_1','DFFQb1','_qpin')[-1][0],self.getXY('Clk_Driver_1','DFFQb1','_qpin')[-1][1]]]
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'] =[[self.getXY('Clk_Driver_1','DFFQb1','_qbpin')[0][0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                             self.getXY('Clk_Driver_1')[0][1]-self._DesignParameter['Clk_Driver_1']['_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclk]]

        self._DesignParameter['_ViaMet32Met4_clk1st']['_XYCoordinates'].append([self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1][0],self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1][1]])
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'].append([self.getXY('Clk_Driver_1','DFFQb2','_qbpin')[0][0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self.getXY('Clk_Driver_1')[0][1]-self._DesignParameter['Clk_Driver_1']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclk])

        self._DesignParameter['_ViaMet42Met5_clk1st']['_XYCoordinates']=[[self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1][0],self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1][1]]]
        self._DesignParameter['_ViaMet42Met5_clk1st_2']['_XYCoordinates']=[[self.getXY('Clk_Driver_1','DFFQb2','_qbpin')[0][0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self.getXY('Clk_Driver_1')[0][1]-self._DesignParameter['Clk_Driver_1']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclk]]

        self._DesignParameter['_ViaMet42Met5_clk1st']['_XYCoordinates'].append([self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1][0],CellHeight/2])
        self._DesignParameter['_ViaMet42Met5_clk1st']['_XYCoordinates'].append([self.getXY('Clk_Driver_1','DFFQb2','_qbpin')[0][0],CellHeight/2])
        self._DesignParameter['_ViaMet42Met5_clk1st']['_XYCoordinates'].append([self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1][0],10*CellHeight+CellHeight/2])
        self._DesignParameter['_ViaMet42Met5_clk1st']['_XYCoordinates'].append([self.getXY('Clk_Driver_1','DFFQb2','_qbpin')[0][0],10*CellHeight+CellHeight/2])


        ### To fix minimum area M3 drc error
        self._DesignParameter['_Met3_clk1st_revise']['_XYCoordinates']=[[[self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1][0],self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1][1]+tmpViaMet2Width/2],\
                                                                      [self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1][0],self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1][1]-tmpViaminWidth+tmpViaMet2Width/2]],\
                                                                        [[self.getXY('Clk_Driver_2','DFFQb2','_qpin')[-1][0],self.getXY('Clk_Driver_2','DFFQb2','_qpin')[-1][1]+tmpViaMet2Width/2],\
                                                                      [self.getXY('Clk_Driver_2','DFFQb2','_qpin')[-1][0],self.getXY('Clk_Driver_2','DFFQb2','_qpin')[-1][1]-tmpViaminWidth+tmpViaMet2Width/2]]]


        #### clk to lower
        self._DesignParameter['_Met4_clk1st']['_XYCoordinates'] = [[self.getXY('Clk_Driver_1','DFFQb1','_qpin')[-1],\
                                                                       [self.getXY('Clk_Driver_1','DFFQb1','_qpin')[-1][0],CellHeight/2]]]#q

        self._DesignParameter['_Met4_clk1st']['_XYCoordinates'].append([[self.getXY('Clk_Driver_1','DFFQb1','_qbpin')[0][0],10*CellHeight+self._DesignParameter['Clk_Driver_1']['_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclk],\
                                                                       [self.getXY('Clk_Driver_1','DFFQb1','_qbpin')[0][0],10*CellHeight+CellHeight/2]])#qb

        ### clk to upper
        self._DesignParameter['_Met4_clk1st']['_XYCoordinates'].append([self.getXY('Clk_Driver_1','DFFQb1','_qpin')[-1],\
                                                                       [self.getXY('Clk_Driver_1','DFFQb1','_qpin')[-1][0],10*CellHeight+CellHeight/2]])#q

        self._DesignParameter['_Met4_clk1st']['_XYCoordinates'].append([[self.getXY('Clk_Driver_1','DFFQb1','_qbpin')[0][0],self._DesignParameter['Clk_Driver_1']['_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclk],\
                                                                       [self.getXY('Clk_Driver_1','DFFQb1','_qbpin')[0][0],10*CellHeight+CellHeight/2]])#qb
        ### clk to upper phase 90
        self._DesignParameter['_Met5_clk1st']['_XYCoordinates']=[[self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1],\
                                                                       [self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1][0],CellHeight/2]]]#q

        self._DesignParameter['_Met5_clk1st']['_XYCoordinates'].append([[self.getXY('Clk_Driver_1','DFFQb2','_qbpin')[0][0],self._DesignParameter['Clk_Driver_1']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclk],\
                                                                       [self.getXY('Clk_Driver_1','DFFQb2','_qbpin')[0][0],CellHeight/2]])#qb
        ### clk to lower phase 90
        self._DesignParameter['_Met5_clk1st']['_XYCoordinates'].append([self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1],\
                                                                       [self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1][0],10*CellHeight+CellHeight/2]])#q

        self._DesignParameter['_Met5_clk1st']['_XYCoordinates'].append([[self.getXY('Clk_Driver_1','DFFQb2','_qbpin')[0][0],self._DesignParameter['Clk_Driver_1']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclk],\
                                                                       [self.getXY('Clk_Driver_1','DFFQb2','_qbpin')[0][0],10*CellHeight+CellHeight/2]])#qb
        ########### 1st to 2nd stage clk and clkb end!!!!


        ########################## Clk driver2 clk routing via erase delete #########################################
        self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['_ViaMet32Met4_clk2nd_del']['_XYCoordinates'] = []
        self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['_ViaMet32Met4_clk2nd_del_2']['_XYCoordinates'] = []
        self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['_ViaMet32Met4_clk2nd_del']['_XYCoordinates'] = []
        self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['_ViaMet32Met4_clk2nd_del_2']['_XYCoordinates'] = []

        ####################### 2nd to 3rd stage clk and clkb  ##########################

        self._DesignParameter['_Met3_clk2nd'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met5_clk2nd'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5'][0],
            _Datatype=DesignParameters._LayerMapping['METAL5'][1],
            _Width=tmpMet2Width
        )

        self._DesignParameter['_ViaMet32Met4_clk2nd'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='_ViaMet32Met4_clk2ndIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4_clk2nd']['_DesignObj']._CalculateDesignParameterSameEnclosure(
            **dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=1))
        self._DesignParameter['_ViaMet32Met4_clk2nd']['_DesignObj']._DesignParameter['_Met4Layer'][
            '_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet32Met4_clk2nd']['_DesignObj']._DesignParameter['_Met3Layer'][
            '_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet32Met4_clk2nd']['_DesignObj']._DesignParameter['_COLayer'][
            '_YWidth'] = tmpVia1YWidth

        self._DesignParameter['_ViaMet32Met4_clk2nd_2'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='_ViaMet32Met4_clk2nd_2In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_DesignObj']._CalculateDesignParameterSameEnclosure(
            **dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=1))
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_DesignObj']._DesignParameter['_Met4Layer'][
            '_XWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_DesignObj']._DesignParameter['_Met3Layer'][
            '_XWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_DesignObj']._DesignParameter['_COLayer'][
            '_XWidth'] = tmpVia1YWidth

        self._DesignParameter['_ViaMet42Met5_clk2nd'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet42Met5._ViaMet42Met5(_Name='_ViaMet42Met5_clk2ndIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet42Met5_clk2nd']['_DesignObj']._CalculateDesignParameterSameEnclosure(
            **dict(_ViaMet42Met5NumberOfCOX=1, _ViaMet42Met5NumberOfCOY=1))
        self._DesignParameter['_ViaMet42Met5_clk2nd']['_DesignObj']._DesignParameter['_Met5Layer'][
            '_YWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet42Met5_clk2nd']['_DesignObj']._DesignParameter['_Met4Layer'][
            '_YWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet42Met5_clk2nd']['_DesignObj']._DesignParameter['_COLayer'][
            '_YWidth'] = tmpVia1YWidth

        self._DesignParameter['_ViaMet42Met5_clk2nd_2'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet42Met5._ViaMet42Met5(_Name='_ViaMet42Met5_clk2nd_2In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet42Met5_clk2nd_2']['_DesignObj']._CalculateDesignParameterSameEnclosure(
            **dict(_ViaMet42Met5NumberOfCOX=1, _ViaMet42Met5NumberOfCOY=1))
        self._DesignParameter['_ViaMet42Met5_clk2nd_2']['_DesignObj']._DesignParameter['_Met5Layer'][
            '_XWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet42Met5_clk2nd_2']['_DesignObj']._DesignParameter['_Met4Layer'][
            '_XWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet42Met5_clk2nd_2']['_DesignObj']._DesignParameter['_COLayer'][
            '_XWidth'] = tmpVia1YWidth
        #via34
        #DDFQb1
        self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'] = [
            [self.getXY('Clk_Driver_2', 'DFFQb1', '_qpin')[-1][0],
             self.getXY('Clk_Driver_2', 'DFFQb1', '_qpin')[-1][1]]]
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'] = [
            [self.getXY('Clk_Driver_2', 'DFFQb1', '_qbpin')[0][0] - tmpViaminWidth / 2 + tmpMet2Width / 2,
             self.getXY('Clk_Driver_2')[0][1]-self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclk]]
        # DDFQb2
        # self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append(
        #     [self.getXY('Clk_Driver_2', 'DFFQb2', '_qpin')[-1][0],
        #      self.getXY('Clk_Driver_2', 'DFFQb2', '_qpin')[-1][1]])
        # self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append(
        #     [self.getXY('Clk_Driver_2', 'DFFQb2', '_qbpin')[0][0] - tmpViaminWidth / 2 + tmpMet2Width / 2,
        #      self.getXY('Clk_Driver_2')[0][1]-self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclk])
        # via45
        # DDFQb1
        self._DesignParameter['_ViaMet42Met5_clk2nd']['_XYCoordinates'] = [
            [self.getXY('Clk_Driver_2', 'DFFQb1', '_qpin')[-1][0],
             self.getXY('Clk_Driver_2', 'DFFQb1', '_qpin')[-1][1]]]
        self._DesignParameter['_ViaMet42Met5_clk2nd_2']['_XYCoordinates'] = [
            [self.getXY('Clk_Driver_2', 'DFFQb1', '_qbpin')[0][0] - tmpViaminWidth / 2 + tmpMet2Width / 2,
             self.getXY('Clk_Driver_2')[0][1]-self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclk]]
        # DDFQb2
        # self._DesignParameter['_ViaMet42Met5_clk2nd']['_XYCoordinates'].append(
        #     [self.getXY('Clk_Driver_2', 'DFFQb2', '_qpin')[-1][0],
        #      self.getXY('Clk_Driver_2', 'DFFQb2', '_qpin')[-1][1]])
        # self._DesignParameter['_ViaMet42Met5_clk2nd_2']['_XYCoordinates'].append(
        #     [self.getXY('Clk_Driver_2', 'DFFQb2', '_qbpin')[0][0] - tmpViaminWidth / 2 + tmpMet2Width / 2,
        #      self.getXY('Clk_Driver_2')[0][1]-self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclk])

        # lower
        self._DesignParameter['_Met5_clk2nd']['_XYCoordinates']=[
            [self.getXY('Clk_Driver_2', 'DFFQb1', '_qpin')[-1], \
             [self.getXY('Clk_Driver_2', 'DFFQb1', '_qpin')[-1][0], \
              self.getXY('Deserializer1toN_1')[0][1] + \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclkb]]]  # f16

        self._DesignParameter['_Met5_clk2nd']['_XYCoordinates'].append([self.getXY('Clk_Driver_2', 'DFFQb1','_qbpin')[0], \
                                                                        [self.getXY('Clk_Driver_2', 'DFFQb1','_qbpin')[0][0],
                                                                         self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['Clk_Driver_2'][
                 '_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclk]])  # f16b



        # upper
        self._DesignParameter['_Met5_clk2nd']['_XYCoordinates'].append(
            [self.getXY('Clk_Driver_2', 'DFFQb1', '_qpin')[-1], \
             [self.getXY('Clk_Driver_2', 'DFFQb1', '_qpin')[-1][0], \
              self.getXY('Deserializer1toN_2')[0][1] + \
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclkb]])  # f16

        self._DesignParameter['_Met5_clk2nd']['_XYCoordinates'].append([self.getXY('Clk_Driver_2', 'DFFQb1','_qbpin')[0], \
                                                                        [self.getXY('Clk_Driver_2', 'DFFQb1','_qbpin')[0][0], \
                                                                         self.getXY('Deserializer1toN_2')[0][1] + \
                                                                         self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['Clk_Driver_2'][
                 '_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclk]])  # f16b

        ## via added for added routing (f16_90 f16_90b)
        ### 34via 45 via added ###
        ##DDFQb1
        # lower

        self._DesignParameter['_ViaMet42Met5_clk2nd']['_XYCoordinates'].append(
            [self.getXY('Clk_Driver_2', 'DFFQb1', '_qpin')[-1][0],
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['Clk_Driver_2'][
                 '_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclkb])
        self._DesignParameter['_ViaMet42Met5_clk2nd']['_XYCoordinates'].append(
            [self.getXY('Clk_Driver_2', 'DFFQb1', '_qbpin')[0][0],
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['Clk_Driver_2'][
                 '_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclk])

        # upper

        self._DesignParameter['_ViaMet42Met5_clk2nd']['_XYCoordinates'].append(
            [self.getXY('Clk_Driver_2', 'DFFQb1', '_qpin')[-1][0],
             self.getXY('Deserializer1toN_2')[0][1] + \
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['Clk_Driver_2'][
                 '_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclkb])
        self._DesignParameter['_ViaMet42Met5_clk2nd']['_XYCoordinates'].append(
            [self.getXY('Clk_Driver_2', 'DFFQb1', '_qbpin')[0][0],
             self.getXY('Deserializer1toN_2')[0][1] + \
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['Clk_Driver_2'][
                 '_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclk])


        a = self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0] + \
                self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0]
        b = self.getXY('Clk_Driver_2', 'DFFQb2', '_qbpin')[0][0] + 12 * tmpDSspace

        ####################### 2nd to 3rd stage clk and clkb end ##########################
        if a > b or a < (b - 10 * tmpDSspace):
            self._DesignParameter['_Met3_clk1st_via3'] = self._PathElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                    _Width=tmpMet2Width
                    )

            self._DesignParameter['_Met3_clk1st_via3']['_XYCoordinates']=[
                    [[self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 12 * tmpDSspace,
                      self.getXY('Clk_Driver_2')[0][1]-self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclkb], \
                     [self.getXY('Clk_Driver_2', 'DFFQb2','_qpin')[-1][0],
                      self.getXY('Clk_Driver_2')[0][1]-self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclkb]]]
            self._DesignParameter['_Met3_clk1st_via3']['_XYCoordinates'].append(
                    [[self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 10 * tmpDSspace,
                      self.getXY('Clk_Driver_2')[0][1]-self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclk], \
                     [self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0],
                      self.getXY('Clk_Driver_2')[0][1]-self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclk]])


            #### clk driver to demux

            self._DesignParameter['_Met5_clk2nd']['_XYCoordinates'].append(
                [[self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 12 * tmpDSspace,
                  +CellHeight / 2], \
                 [self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 12 * tmpDSspace, \
                  10*CellHeight +CellHeight/2]])

            self._DesignParameter['_Met5_clk2nd']['_XYCoordinates'].append(
                [[self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 10 * tmpDSspace,
                  +CellHeight / 2], \
                 [self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 10 * tmpDSspace, \
                  10*CellHeight +CellHeight/2]])

            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 12 * tmpDSspace,
                      self.getXY('Clk_Driver_2')[0][1]-self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclkb])
            self._DesignParameter['_ViaMet42Met5_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 12 * tmpDSspace,
                      self.getXY('Clk_Driver_2')[0][1]-self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclkb])

            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 10 * tmpDSspace,
                      self.getXY('Clk_Driver_2')[0][1]-self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclk])
            self._DesignParameter['_ViaMet42Met5_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 10 * tmpDSspace,
                      self.getXY('Clk_Driver_2')[0][1]-self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclk])

            ##lower
            self._DesignParameter['_ViaMet42Met5_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 10 * tmpDSspace,CellHeight/2])

            self._DesignParameter['_ViaMet42Met5_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 12 * tmpDSspace,CellHeight/2])
            ###upper
            self._DesignParameter['_ViaMet42Met5_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 10 * tmpDSspace,10*CellHeight+CellHeight/2])

            self._DesignParameter['_ViaMet42Met5_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 12 * tmpDSspace,10*CellHeight+CellHeight/2])


        else:
            self._DesignParameter['_Met3_clk1st_via3'] = self._PathElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                    _Width=tmpMet2Width
                    )

            self._DesignParameter['_Met3_clk1st_via3']['_XYCoordinates']=[
                    [[self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 22 * tmpDSspace,
                      self.getXY('Clk_Driver_2')[0][1]-self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclkb], \
                     [self.getXY('Clk_Driver_2', 'DFFQb2','_qpin')[-1][0],
                      self.getXY('Clk_Driver_2')[0][1]-self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclkb]]]
            self._DesignParameter['_Met3_clk1st_via3']['_XYCoordinates'].append(
                    [[self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 20 * tmpDSspace,
                      self.getXY('Clk_Driver_2')[0][1]-self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclk], \
                     [self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0],
                      self.getXY('Clk_Driver_2')[0][1]-self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclk]])


            self._DesignParameter['_Met5_clk2nd']['_XYCoordinates'].append(
                [[self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 22 * tmpDSspace,
                  +CellHeight / 2], \
                 [self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 22 * tmpDSspace, \
                  20*CellHeight +CellHeight/2]])

            self._DesignParameter['_Met5_clk2nd']['_XYCoordinates'].append(
                [[self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 20 * tmpDSspace,
                  +CellHeight / 2], \
                 [self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 20 * tmpDSspace, \
                  20*CellHeight +CellHeight/2]])

            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 22 * tmpDSspace,
                      self.getXY('Clk_Driver_2')[0][1]-self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclkb])
            self._DesignParameter['_ViaMet42Met5_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 22 * tmpDSspace,
                      self.getXY('Clk_Driver_2')[0][1]-self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclkb])

            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 20 * tmpDSspace,
                      self.getXY('Clk_Driver_2')[0][1]-self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclk])
            self._DesignParameter['_ViaMet42Met5_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 20 * tmpDSspace,
                      self.getXY('Clk_Driver_2')[0][1]-self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclk])

            ##lower
            self._DesignParameter['_ViaMet42Met5_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 20 * tmpDSspace,CellHeight/2])

            self._DesignParameter['_ViaMet42Met5_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 22 * tmpDSspace,CellHeight/2])
            ###upper
            self._DesignParameter['_ViaMet42Met5_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 20 * tmpDSspace,10*CellHeight+CellHeight/2])

            self._DesignParameter['_ViaMet42Met5_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2','_qbpin')[0][0] + 22 * tmpDSspace,10*CellHeight+CellHeight/2])






        ############# Clk Driver to DeMux Delete and revise #######################
        self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['_ViaMet32Met4_clk2nd22']['_XYCoordinates'] = []
        self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['_Met3_clk1st_via3']['_XYCoordinates'] = []

        self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['_ViaMet32Met4_clk2nd22']['_XYCoordinates'] = []
        self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['_Met3_clk1st_via3']['_XYCoordinates'] = []

        # self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['_Met4_clk2nd_del']['_XYCoordinates'] = []
        # self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['_Met4_clk2nd_del']['_XYCoordinates'] = []
        #
        # self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['_Met3_clk1st_via']['_XYCoordinates'] = []
        # self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['_Met3_clk1st_via']['_XYCoordinates'] = []


        ############# Clk Driver to DeMux Delete and revise end #######################


        ############# Clk Driver added final f16 #######################


        ############# Clk Driver added final f16 end #######################



        ########################## Pin Generation ##################
        Dataoutspacing = 200

        '''Pin generation'''
        self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VDD')
        self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VSS')

        self._DesignParameter['_Din_even'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='D_even')

        self._DesignParameter['_Din_odd'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='D_odd')

        self._DesignParameter['Q_even0'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<0>')
        self._DesignParameter['Q_even1'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<1>')
        self._DesignParameter['Q_even2'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<2>')
        self._DesignParameter['Q_even3'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<3>')
        self._DesignParameter['Q_even4'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<4>')
        self._DesignParameter['Q_even5'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<5>')
        self._DesignParameter['Q_even6'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<6>')
        self._DesignParameter['Q_even7'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<7>')
        self._DesignParameter['Q_even8'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<8>')
        self._DesignParameter['Q_even9'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<9>')
        self._DesignParameter['Q_even10'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<10>')
        self._DesignParameter['Q_even11'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<11>')
        self._DesignParameter['Q_even12'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<12>')
        self._DesignParameter['Q_even13'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<13>')
        self._DesignParameter['Q_even14'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<14>')
        self._DesignParameter['Q_even15'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<15>')
        self._DesignParameter['Q_even16'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<16>')
        self._DesignParameter['Q_even17'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<17>')
        self._DesignParameter['Q_even18'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<18>')
        self._DesignParameter['Q_even19'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<19>')
        self._DesignParameter['Q_even20'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<20>')
        self._DesignParameter['Q_even21'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<21>')
        self._DesignParameter['Q_even22'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<22>')
        self._DesignParameter['Q_even23'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<23>')
        self._DesignParameter['Q_even24'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<24>')
        self._DesignParameter['Q_even25'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<25>')
        self._DesignParameter['Q_even26'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<26>')
        self._DesignParameter['Q_even27'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<27>')
        self._DesignParameter['Q_even28'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<28>')
        self._DesignParameter['Q_even29'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<29>')
        self._DesignParameter['Q_even30'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<30>')
        self._DesignParameter['Q_even31'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_even<31>')

        self._DesignParameter['Q_odd0'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<0>')
        self._DesignParameter['Q_odd1'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<1>')
        self._DesignParameter['Q_odd2'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<2>')
        self._DesignParameter['Q_odd3'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<3>')
        self._DesignParameter['Q_odd4'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<4>')
        self._DesignParameter['Q_odd5'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<5>')
        self._DesignParameter['Q_odd6'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<6>')
        self._DesignParameter['Q_odd7'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<7>')
        self._DesignParameter['Q_odd8'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<8>')
        self._DesignParameter['Q_odd9'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<9>')
        self._DesignParameter['Q_odd10'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<10>')
        self._DesignParameter['Q_odd11'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<11>')
        self._DesignParameter['Q_odd12'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<12>')
        self._DesignParameter['Q_odd13'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<13>')
        self._DesignParameter['Q_odd14'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<14>')
        self._DesignParameter['Q_odd15'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<15>')
        self._DesignParameter['Q_odd16'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<16>')
        self._DesignParameter['Q_odd17'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<17>')
        self._DesignParameter['Q_odd18'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<18>')
        self._DesignParameter['Q_odd19'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<19>')
        self._DesignParameter['Q_odd20'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<20>')
        self._DesignParameter['Q_odd21'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<21>')
        self._DesignParameter['Q_odd22'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<22>')
        self._DesignParameter['Q_odd23'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<23>')
        self._DesignParameter['Q_odd24'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<24>')
        self._DesignParameter['Q_odd25'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<25>')
        self._DesignParameter['Q_odd26'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<26>')
        self._DesignParameter['Q_odd27'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<27>')
        self._DesignParameter['Q_odd28'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<28>')
        self._DesignParameter['Q_odd29'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<29>')
        self._DesignParameter['Q_odd30'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<30>')
        self._DesignParameter['Q_odd31'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q_odd<31>')

        self._DesignParameter['_clkpin'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='clk')
        self._DesignParameter['_clkbpin'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='clkb')

        self._DesignParameter['_VDDpin']['_XYCoordinates'] = [
            [self.getXY('Clk_Driver_1')[0][0] + tmpDSspace, self.getXY('Clk_Driver_1')[0][1] + CellHeight], \
            [self.getXY('Clk_Driver_1')[0][0] + tmpDSspace, self.getXY('Clk_Driver_1')[0][1] + 3 * CellHeight], \
            [self.getXY('Clk_Driver_1')[0][0] + tmpDSspace, self.getXY('Clk_Driver_1')[0][1] + 5 * CellHeight], \
            [self.getXY('Clk_Driver_1')[0][0] + tmpDSspace, self.getXY('Clk_Driver_1')[0][1] - CellHeight], \
            [self.getXY('Clk_Driver_1')[0][0] + tmpDSspace, self.getXY('Clk_Driver_1')[0][1] - 3 * CellHeight],\
            [self.getXY('Clk_Driver_1')[0][0] + tmpDSspace, self.getXY('Clk_Driver_1')[0][1] + 7 *CellHeight], \
            [self.getXY('Clk_Driver_1')[0][0] + tmpDSspace, self.getXY('Clk_Driver_1')[0][1] + 9 *CellHeight], \
            [self.getXY('Clk_Driver_1')[0][0] + tmpDSspace, self.getXY('Clk_Driver_1')[0][1] - 5 *CellHeight], \
            [self.getXY('Clk_Driver_1')[0][0] + tmpDSspace, self.getXY('Clk_Driver_1')[0][1] - 7 *CellHeight], \
            [self.getXY('Clk_Driver_1')[0][0] + tmpDSspace, self.getXY('Clk_Driver_1')[0][1] - 9* CellHeight]]

        self._DesignParameter['_VSSpin']['_XYCoordinates'] = [
            [self.getXY('Clk_Driver_1')[0][0] + tmpDSspace, self.getXY('Clk_Driver_1')[0][1]], \
            [self.getXY('Clk_Driver_1')[0][0] + tmpDSspace, self.getXY('Clk_Driver_1')[0][1] + 2 * CellHeight], \
            [self.getXY('Clk_Driver_1')[0][0] + tmpDSspace, self.getXY('Clk_Driver_1')[0][1] + 4 * CellHeight], \
            [self.getXY('Clk_Driver_1')[0][0] + tmpDSspace, self.getXY('Clk_Driver_1')[0][1] - 2 * CellHeight], \
            [self.getXY('Clk_Driver_1')[0][0] + tmpDSspace, self.getXY('Clk_Driver_1')[0][1] - 4 * CellHeight],\
            [self.getXY('Clk_Driver_1')[0][0] + tmpDSspace, self.getXY('Clk_Driver_1')[0][1] + 6 * CellHeight], \
            [self.getXY('Clk_Driver_1')[0][0] + tmpDSspace, self.getXY('Clk_Driver_1')[0][1] + 8 * CellHeight],\
            [self.getXY('Clk_Driver_1')[0][0] + tmpDSspace, self.getXY('Clk_Driver_1')[0][1] - 6 * CellHeight], \
            [self.getXY('Clk_Driver_1')[0][0] + tmpDSspace, self.getXY('Clk_Driver_1')[0][1] - 8 * CellHeight], \
            [self.getXY('Clk_Driver_1')[0][0] + tmpDSspace, self.getXY('Clk_Driver_1')[0][1] - 10 * CellHeight]]

        self._DesignParameter['_Din_even']['_XYCoordinates'] = self.getXY('Deserializer1toN_1','DeMux1to2_3', 'DFF_Latch', '_dpin')
        self._DesignParameter['_Din_odd']['_XYCoordinates'] = self.getXY('Deserializer1toN_2','DeMux1to2_3', 'DFF_Latch', '_dpin')

        CellXWidth = self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_1']['_DesignObj'].CellXWidth
        ################ Q_even ########################
        ### Demux1
        self._DesignParameter['Q_even0']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_1']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk + Dataoutspacing]]
        self._DesignParameter['Q_even8']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_1']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk]]
        self._DesignParameter['Q_even16']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_1']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclkb]]
        self._DesignParameter['Q_even24']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_1']['_DesignObj'].D4[1]]]
        ### Demux8
        self._DesignParameter['Q_even1']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_8']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk + Dataoutspacing]]
        self._DesignParameter['Q_even9']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_8']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk]]
        self._DesignParameter['Q_even17']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_8']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclkb]]
        self._DesignParameter['Q_even25']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_8']['_DesignObj'].D4[1]]]
        ### Demux3
        self._DesignParameter['Q_even4']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_3']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk + Dataoutspacing]]
        self._DesignParameter['Q_even12']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_3']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk]]
        self._DesignParameter['Q_even20']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_3']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclkb]]
        self._DesignParameter['Q_even28']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_3']['_DesignObj'].D4[1]]]
        ### Demux6
        self._DesignParameter['Q_even5']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_6']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk + Dataoutspacing]]
        self._DesignParameter['Q_even13']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_6']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk]]
        self._DesignParameter['Q_even21']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_6']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclkb]]
        self._DesignParameter['Q_even29']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_6']['_DesignObj'].D4[1]]]

        ### Demux2
        self._DesignParameter['Q_even2']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_2']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk - Dataoutspacing]]
        self._DesignParameter['Q_even10']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_2']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk]]
        self._DesignParameter['Q_even18']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_2']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclkb]]
        self._DesignParameter['Q_even26']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_2']['_DesignObj'].D4[1]]]
        ### Demux4
        self._DesignParameter['Q_even6']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_4']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk - Dataoutspacing]]
        self._DesignParameter['Q_even14']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_4']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk]]
        self._DesignParameter['Q_even22']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_4']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclkb]]
        self._DesignParameter['Q_even30']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_4']['_DesignObj'].D4[1]]]
        ### Demux5
        self._DesignParameter['Q_even7']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_5']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk - Dataoutspacing]]
        self._DesignParameter['Q_even15']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_5']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk]]
        self._DesignParameter['Q_even23']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_5']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclkb]]
        self._DesignParameter['Q_even31']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_5']['_DesignObj'].D4[1]]]
        ### Demux7
        self._DesignParameter['Q_even3']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_7']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk - Dataoutspacing]]
        self._DesignParameter['Q_even11']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_7']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk]]
        self._DesignParameter['Q_even19']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_7']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclkb]]
        self._DesignParameter['Q_even27']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_1']['_DesignObj']._DesignParameter['DeMux1to4_7']['_DesignObj'].D4[1]]]


        ################ Q_odd ###################
        ### Demux1
        self._DesignParameter['Q_odd0']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_1']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk + Dataoutspacing]]
        self._DesignParameter['Q_odd8']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_1']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk]]
        self._DesignParameter['Q_odd16']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_1']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclkb]]
        self._DesignParameter['Q_odd24']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_1']['_DesignObj'].D4[1]]]

        ### Demux8
        self._DesignParameter['Q_odd1']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_8']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk + Dataoutspacing]]
        self._DesignParameter['Q_odd9']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_8']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk]]
        self._DesignParameter['Q_odd17']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_8']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclkb]]
        self._DesignParameter['Q_odd25']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_8']['_DesignObj'].D4[1]]]
        ### Demux3
        self._DesignParameter['Q_odd4']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_3']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk + Dataoutspacing]]
        self._DesignParameter['Q_odd12']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_3']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk]]
        self._DesignParameter['Q_odd20']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_3']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclkb]]
        self._DesignParameter['Q_odd28']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_3']['_DesignObj'].D4[1]]]
        ### Demux6
        self._DesignParameter['Q_odd5']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_6']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk + Dataoutspacing]]
        self._DesignParameter['Q_odd13']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_6']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk]]
        self._DesignParameter['Q_odd21']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_6']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclkb]]
        self._DesignParameter['Q_odd29']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][1] +
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_6']['_DesignObj'].D4[1]]]

        ### Demux2
        self._DesignParameter['Q_odd2']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_2']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk - Dataoutspacing]]
        self._DesignParameter['Q_odd10']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_2']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk]]
        self._DesignParameter['Q_odd18']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_2']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclkb]]
        self._DesignParameter['Q_odd26']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_2']['_DesignObj'].D4[1]]]
        ### Demux4
        self._DesignParameter['Q_odd6']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_4']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk - Dataoutspacing]]
        self._DesignParameter['Q_odd14']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_4']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk]]
        self._DesignParameter['Q_odd22']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_4']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclkb]]
        self._DesignParameter['Q_odd30']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_4']['_DesignObj'].D4[1]]]
        ### Demux5
        self._DesignParameter['Q_odd7']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_5']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk - Dataoutspacing]]
        self._DesignParameter['Q_odd15']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_5']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk]]
        self._DesignParameter['Q_odd23']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_5']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclkb]]
        self._DesignParameter['Q_odd31']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_5']['_DesignObj'].D4[1]]]
        ### Demux7
        self._DesignParameter['Q_odd3']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_7']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk - Dataoutspacing]]
        self._DesignParameter['Q_odd11']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_7']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclk]]
        self._DesignParameter['Q_odd19']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_7']['_DesignObj']._DesignParameter['DFF_Latch_Latch'][
                 '_DesignObj'].iclkb]]
        self._DesignParameter['Q_odd27']['_XYCoordinates'] = [
            [self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][0] + CellXWidth - tmpDSspace, \
             self.getXY('Deserializer1toN_2')[0][1]+self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][1] -
             self._DesignParameter['Deserializer1toN_2']['_DesignObj']._DesignParameter['DeMux1to4_7']['_DesignObj'].D4[1]]]


        self._DesignParameter['_clkpin']['_XYCoordinates'] = [
            [self.getXY('Deserializer1toN_1','DeMux1to2_3')[0][0] + tmpDSspace,self.getXY('Deserializer1toN_1','DeMux1to2_3')[0][1] + 15 * CellHeight+ tmpDSspace+3*clkrouting/2-tmpMet2Width/2]]
        self._DesignParameter['_clkbpin']['_XYCoordinates'] = [[self.getXY('Deserializer1toN_1','DeMux1to2_3')[0][0] + tmpDSspace,
                                                                self.getXY('Deserializer1toN_1','DeMux1to2_3')[0][1]+ 15 * CellHeight - tmpDSspace-3*clkrouting/2+tmpMet2Width/2]]




''' INV2&3 # of Fingers should be less than 7(6 max)
    otherwise, INV inner routing and qb routing will be overlapped'''
################################ DRC Check #################################
import random
if __name__ == '__main__':
    for i in range(0,100):
        list=[2,8,16,32]
        Deserialize1toN=random.choice(list)
        TG1_Finger = random.randint(1,5)
        TG2_Finger = random.randint(1, 5)
        TSI1_Finger = random.randint(1,2)
        TSI2_Finger = random.randint(1,2)
        INV1_Finger = random.randint(1,5)
        INV2_Finger = random.randint(1,5)
        INV3_Finger = random.randint(1,5)
        INV4_Finger = random.randint(1,5)

        TG3_Finger = random.randint(1, 5)
        TSI3_Finger = random.randint(1, 2)
        INV5_Finger = random.randint(1, 5)
        INV6_Finger = random.randint(1, 5)

        TG4_Finger = random.randint(1, 5)
        TSI4_Finger = random.randint(1, 2)
        INV7_Finger = random.randint(1, 5)
        INV8_Finger = random.randint(1, 5)
        INV9_Finger = random.randint(1, 5)
        INV10_Finger = random.randint(1, 5)



        TG1_Finger_clk = random.randint(1, 5)
        TG2_Finger_clk = random.randint(1, 5)
        TSI1_Finger_clk = random.randint(1, 2)
        TSI2_Finger_clk = random.randint(1, 2)
        INV1_Finger_clk = random.randint(1, 5)
        INV2_Finger_clk = random.randint(1, 5)
        INV3_Finger_clk = random.randint(1, 5)
        INV4_Finger_clk = random.randint(1, 5)
        INV5_Finger_clk = random.randint(1, 5)

        Deserialize1toN=32

        TSI1_Finger=TSI2_Finger=TSI3_Finger=TSI4_Finger=1
        #random.randrange(200, 250, 10)

        TG1_NMWidth =TG2_NMWidth=TG3_NMWidth= TG4_NMWidth=TSI1_NMWidth=TSI2_NMWidth=TSI3_NMWidth=TSI4_NMWidth=INV1_NMWidth=INV2_NMWidth=INV3_NMWidth\
            =INV4_NMWidth=INV5_NMWidth=INV6_NMWidth=INV7_NMWidth=INV8_NMWidth=INV9_NMWidth=INV10_NMWidth=200        #random.randrange(200, 250, 10)
        TG1_PMWidth = TG2_PMWidth=TG3_PMWidth=TG4_PMWidth=TSI1_PMWidth=TSI2_PMWidth=TSI3_PMWidth=TSI4_PMWidth=INV1_PMWidth=INV2_PMWidth=INV3_PMWidth\
            =INV4_PMWidth=INV5_PMWidth=INV6_PMWidth=INV7_PMWidth=INV8_PMWidth=INV9_PMWidth=INV10_PMWidth=TG1_NMWidth*2

        # TSI1_NMWidth = TSI2_NMWidth = TSI3_NMWidth = TSI4_NMWidth=150
        # TSI1_PMWidth = TSI2_PMWidth = TSI3_PMWidth = TSI4_PMWidth=300
        #
        # INV1_NMWidth=INV2_NMWidth=INV3_NMWidth\
        #     =INV4_NMWidth=INV5_NMWidth=INV6_NMWidth=INV7_NMWidth=INV8_NMWidth=INV9_NMWidth=INV10_NMWidth=200
        # INV1_PMWidth=INV2_PMWidth=INV3_PMWidth\
        #     =INV4_PMWidth=INV5_PMWidth=INV6_PMWidth=INV7_PMWidth=INV8_PMWidth=INV9_PMWidth=INV10_PMWidth=400

        dummy=False #only use in 1:N archetecture not 2:N
        ChannelLength = 30
        GateSpacing = 100
        SDWidth = 66
        XVT = 'SLVT'
        CellHeight = 1800
        SupplyRailType = 2
        Fillcap= False
        # TG1_Finger_clk = TG1_Finger
        # TG2_Finger_clk = TG2_Finger
        # TSI1_Finger_clk = TSI1_Finger
        # TSI2_Finger_clk = TSI2_Finger
        # INV1_Finger_clk = INV1_Finger
        # INV2_Finger_clk = INV2_Finger
        # INV3_Finger_clk = INV3_Finger
        # INV4_Finger_clk = INV5_Finger
        # INV5_Finger_clk = INV6_Finger
        #
        TG1_Finger = 1
        TG2_Finger = 2
        TSI1_Finger = 1
        TSI2_Finger = 1
        INV1_Finger = 3
        INV2_Finger = 2
        INV3_Finger = 2
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

        TG1_Finger_clk = 1
        TG2_Finger_clk = 2
        TSI1_Finger_clk = 1
        TSI2_Finger_clk = 1
        INV1_Finger_clk = 3
        INV2_Finger_clk = 2
        INV3_Finger_clk = 2
        INV4_Finger_clk = 6
        INV5_Finger_clk = 6

        # print("itr = ", i)
        # print("TG1_Finger = ", TG1_Finger)
        # print("TG2_Finger = ", TG2_Finger)
        # print("TG3_Finger = ", TG3_Finger)
        # print("TSI1_Finger = ", TSI1_Finger)
        # print("TSI2_Finger = ", TSI2_Finger)
        # print("TSI3_Finger = ", TSI3_Finger)
        # print("INV1_Finger = ", INV1_Finger)
        # print("INV2_Finger = ", INV2_Finger)
        # print("INV3_Finger = ", INV3_Finger)
        # print("INV4_Finger = ", INV4_Finger)
        # print("INV5_Finger = ", INV5_Finger)
        # print("INN6_Finger = ", INV6_Finger)

        DesignParameters._Technology = 'SS28nm'
        TopObj = Deserializer2toN(_DesignParameter=None, _Name='Deserializer2toN')
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

            dummy=dummy,
            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            SDWidth=SDWidth,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType,
            Fillcap = Fillcap
        )

        TopObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=TopObj._DesignParameter)
        testStreamFile = open('./Deserializer2toN.gds', 'wb')
        tmp = TopObj._CreateGDSStream(TopObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()
        print('#############################      Sending to FTP Server...      ##############################')
       # i=i+1
        #print("itr = ", i)
        import ftplib
        import time

        ftp = ftplib.FTP('141.223.24.53')
        ftp.login('ljw95', 'dlwodn123')
        ftp.cwd('/mnt/sdc/ljw95/OPUS/ss28')
        myfile = open('Deserializer2toN.gds', 'rb')
        ftp.storbinary('STOR Deserializer2toN.gds', myfile)
        myfile.close()

        import DRCchecker

        a = DRCchecker.DRCchecker('ljw95','dlwodn123','/mnt/sdc/ljw95/OPUS/ss28','/mnt/sdc/ljw95/OPUS/ss28/DRC/run','Deserializer2toN','Deserializer2toN',None)
        a.DRCchecker()

        print ("DRC Clean!!!")



        # a = DRCchecker.DRCchecker('ljw95', 'dlwodn123', '/mnt/sdc/ljw95/OPUS/ss28', '/mnt/sdc/ljw95/OPUS/ss28/DRC/run',
        #                           'Deserializer1to32', 'Deserializer1to32', None)
        # print('   Sending to FTP Server & StreamIn...   '.center(105, '#'))
        # a.Upload2FTP()
        # a.StreamIn(tech='028nm')
        #
        #
        # # a.DRCchecker()
        # print("#################################### preparing ####################################")
        # print("#################################### preparing ####################################")
        # print("#################################### preparing ####################################")
        # print("################################po#### preparing ####################################")
        # print("#################################### preparing ####################################")
        # print("#################################### preparing ####################################")
        # time.sleep(3)
        # # time.sleep(0.5)
        # # print("#################################### Generating ####################################")
        # # print("#################################### Generating ####################################")
        # # print("#################################### Generating ####################################")
        # # print("#################################### Generating ####################################")
        # # print("#################################### Generating ####################################")
        # #
        # # time.sleep(5)
        # # a.DRCchecker()
        # print('      Finished       '.center(105, '#'))
        # print("DRC Clean!!!")