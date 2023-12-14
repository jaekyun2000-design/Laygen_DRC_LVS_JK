import math
import copy

#
from generatorLib import StickDiagram
from generatorLib import DesignParameters
from generatorLib import DRC

#
from generatorLib.generator_models import TristateInverter
from generatorLib.generator_models import Inverter
from generatorLib.generator_models import Transmission_gate
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaMet22Met3
from generatorLib.generator_models import ViaMet32Met4
from generatorLib.generator_models import ViaMet42Met5

from generatorLib.generator_models import Clk_Driver
from generatorLib.generator_models import DeMux1to4
from generatorLib.generator_models import DeMux1to2




class Deserializer1to32(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name='Deserializer1to32'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name


    def _CalculateDesignParameter(self,
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


                                  ChannelLength=30,
                                  GateSpacing=100,
                                  SDWidth=66,
                                  XVT='SLVT',
                                  CellHeight=1800,
                                  SupplyRailType=2

                                  ):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        UnitPitch = ChannelLength + GateSpacing


        Parameters_DeMux1to2_1 = dict(
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

            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            SDWidth=SDWidth,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType
        )

        Parameters_DeMux1to2_2 = dict(
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

            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            SDWidth=SDWidth,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType
        )
        Parameters_DeMux1to2_3 = dict(
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

            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            SDWidth=SDWidth,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType
        )
        Parameters_DeMux1to2_4 = dict(
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

            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            SDWidth=SDWidth,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType
        )
        Parameters_DeMux1to2_5 = dict(
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

        Parameters_DeMux1to4_1 = dict(
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

            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            SDWidth=SDWidth,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType
        )
        Parameters_DeMux1to4_2 = dict(
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

            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            SDWidth=SDWidth,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType
        )
        Parameters_DeMux1to4_3 = dict(
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

            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            SDWidth=SDWidth,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType
        )
        Parameters_DeMux1to4_4 = dict(
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

            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            SDWidth=SDWidth,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType
        )
        Parameters_DeMux1to4_5 = dict(
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

            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            SDWidth=SDWidth,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType
        )
        Parameters_DeMux1to4_6 = dict(
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

            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            SDWidth=SDWidth,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType
        )
        Parameters_DeMux1to4_7 = dict(
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

            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            SDWidth=SDWidth,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType
        )
        Parameters_DeMux1to4_8 = dict(
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

            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            SDWidth=SDWidth,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType
        )

        ##################################### Placement #################################################
        self._DesignParameter['DeMux1to2_1'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=DeMux1to2.DeMux1to2(_Name='DeMux1to2_1In{}'.format(_Name)))[0]
        self._DesignParameter['DeMux1to2_1']['_DesignObj']._CalculateDesignParameter(**Parameters_DeMux1to2_1)
        self._DesignParameter['DeMux1to2_1']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['DeMux1to2_2'] = self._SrefElementDeclaration(
            _Reflect=[1, 0, 0], _Angle=0,
            _DesignObj=DeMux1to2.DeMux1to2(_Name='DeMux1to2_2In{}'.format(_Name)))[0]
        self._DesignParameter['DeMux1to2_2']['_DesignObj']._CalculateDesignParameter(**Parameters_DeMux1to2_2)
        self._DesignParameter['DeMux1to2_2']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['DeMux1to2_3'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=DeMux1to2.DeMux1to2(_Name='DeMux1to2_3In{}'.format(_Name)))[0]
        self._DesignParameter['DeMux1to2_3']['_DesignObj']._CalculateDesignParameter(**Parameters_DeMux1to2_3)
        self._DesignParameter['DeMux1to2_3']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['DeMux1to2_4'] = self._SrefElementDeclaration(
            _Reflect=[1, 0, 0], _Angle=0,
            _DesignObj=DeMux1to2.DeMux1to2(_Name='DeMux1to2_4In{}'.format(_Name)))[0]
        self._DesignParameter['DeMux1to2_4']['_DesignObj']._CalculateDesignParameter(**Parameters_DeMux1to2_4)
        self._DesignParameter['DeMux1to2_4']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['DeMux1to2_5'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=DeMux1to2.DeMux1to2(_Name='DeMux1to2_5In{}'.format(_Name)))[0]
        self._DesignParameter['DeMux1to2_5']['_DesignObj']._CalculateDesignParameter(**Parameters_DeMux1to2_5)
        self._DesignParameter['DeMux1to2_5']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['Clk_Driver_1'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=Clk_Driver.Clk_Driver(_Name='Clk_Driver_1In{}'.format(_Name)))[0]
        self._DesignParameter['Clk_Driver_1']['_DesignObj']._CalculateDesignParameter(**Parameters_Clk_Driver_1)
        self._DesignParameter['Clk_Driver_1']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['Clk_Driver_2'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=Clk_Driver.Clk_Driver(_Name='Clk_Driver_2In{}'.format(_Name)))[0]
        self._DesignParameter['Clk_Driver_2']['_DesignObj']._CalculateDesignParameter(**Parameters_Clk_Driver_2)
        self._DesignParameter['Clk_Driver_2']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['DeMux1to4_1'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=DeMux1to4.DeMux1to4(_Name='DeMux1to4_1In{}'.format(_Name)))[0]
        self._DesignParameter['DeMux1to4_1']['_DesignObj']._CalculateDesignParameter(**Parameters_DeMux1to4_1)
        self._DesignParameter['DeMux1to4_1']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['DeMux1to4_2'] = self._SrefElementDeclaration(
            _Reflect=[1, 0, 0], _Angle=0,
            _DesignObj=DeMux1to4.DeMux1to4(_Name='DeMux1to4_2In{}'.format(_Name)))[0]
        self._DesignParameter['DeMux1to4_2']['_DesignObj']._CalculateDesignParameter(**Parameters_DeMux1to4_2)
        self._DesignParameter['DeMux1to4_2']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['DeMux1to4_3'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=DeMux1to4.DeMux1to4(_Name='DeMux1to4_3In{}'.format(_Name)))[0]
        self._DesignParameter['DeMux1to4_3']['_DesignObj']._CalculateDesignParameter(**Parameters_DeMux1to4_3)
        self._DesignParameter['DeMux1to4_3']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['DeMux1to4_4'] = self._SrefElementDeclaration(
            _Reflect=[1, 0, 0], _Angle=0,
            _DesignObj=DeMux1to4.DeMux1to4(_Name='DeMux1to4_4In{}'.format(_Name)))[0]
        self._DesignParameter['DeMux1to4_4']['_DesignObj']._CalculateDesignParameter(**Parameters_DeMux1to4_4)
        self._DesignParameter['DeMux1to4_4']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['DeMux1to4_5'] = self._SrefElementDeclaration(
            _Reflect=[1, 0, 0], _Angle=0,
            _DesignObj=DeMux1to4.DeMux1to4(_Name='DeMux1to4_5In{}'.format(_Name)))[0]
        self._DesignParameter['DeMux1to4_5']['_DesignObj']._CalculateDesignParameter(**Parameters_DeMux1to4_5)
        self._DesignParameter['DeMux1to4_5']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['DeMux1to4_6'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=DeMux1to4.DeMux1to4(_Name='DeMux1to4_6In{}'.format(_Name)))[0]
        self._DesignParameter['DeMux1to4_6']['_DesignObj']._CalculateDesignParameter(**Parameters_DeMux1to4_6)
        self._DesignParameter['DeMux1to4_6']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['DeMux1to4_7'] = self._SrefElementDeclaration(
            _Reflect=[1, 0, 0], _Angle=0,
            _DesignObj=DeMux1to4.DeMux1to4(_Name='DeMux1to4_7In{}'.format(_Name)))[0]
        self._DesignParameter['DeMux1to4_7']['_DesignObj']._CalculateDesignParameter(**Parameters_DeMux1to4_7)
        self._DesignParameter['DeMux1to4_7']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['DeMux1to4_8'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=DeMux1to4.DeMux1to4(_Name='DeMux1to4_8In{}'.format(_Name)))[0]
        self._DesignParameter['DeMux1to4_8']['_DesignObj']._CalculateDesignParameter(**Parameters_DeMux1to4_8)
        self._DesignParameter['DeMux1to4_8']['_XYCoordinates'] = [[0, 0]]



        self._DesignParameter['DeMux1to2_3']['_XYCoordinates'] = [[0,0]]
        self._DesignParameter['DeMux1to2_2']['_XYCoordinates'] = [[self.getXY('DeMux1to2_3')[0][0] , self._DesignParameter['DeMux1to2_3']['_XYCoordinates'][0][1]+2*CellHeight]]
        self._DesignParameter['DeMux1to2_1']['_XYCoordinates'] = [[self.getXY('DeMux1to2_3')[0][0] , self._DesignParameter['DeMux1to2_3']['_XYCoordinates'][0][1]+2*CellHeight]]
        self._DesignParameter['DeMux1to2_4']['_XYCoordinates'] = [[self.getXY('DeMux1to2_3')[0][0] , self._DesignParameter['DeMux1to2_3']['_XYCoordinates'][0][1]]]
        self._DesignParameter['DeMux1to2_5']['_XYCoordinates'] = [[self.getXY('DeMux1to2_3')[0][0] , self._DesignParameter['DeMux1to2_3']['_XYCoordinates'][0][1]-2*CellHeight]]

        #+self._DesignParameter['Clk_Driver_1']['_DesignObj']._DesignParameter['DFFQb1']['_DesignObj']._DesignParameter['TG1']['_DesignObj'].CellXWidth/2
        self._DesignParameter['Clk_Driver_1']['_XYCoordinates'] = [[
            self.getXY('DeMux1to2_3')[0][0] + self._DesignParameter['DeMux1to2_3']['_DesignObj'].CellXWidth +UnitPitch,
            self._DesignParameter['DeMux1to2_3']['_XYCoordinates'][0][1]]]

        self._DesignParameter['Clk_Driver_2']['_XYCoordinates'] = [[
            self.getXY('Clk_Driver_1')[0][0] + self._DesignParameter['Clk_Driver_1']['_DesignObj'].CellXWidth +UnitPitch ,
            self._DesignParameter['DeMux1to2_3']['_XYCoordinates'][0][1]]]

        self._DesignParameter['DeMux1to4_4']['_XYCoordinates'] = [[
            self.getXY('DeMux1to2_3')[0][0] + self._DesignParameter['DeMux1to2_3']['_DesignObj'].CellXWidth +UnitPitch  ,
            self._DesignParameter['DeMux1to2_3']['_XYCoordinates'][0][1]+2*CellHeight]]
        self._DesignParameter['DeMux1to4_3']['_XYCoordinates'] = [[
            self.getXY('DeMux1to2_3')[0][0] + self._DesignParameter['DeMux1to2_3']['_DesignObj'].CellXWidth +UnitPitch ,
            self._DesignParameter['DeMux1to2_3']['_XYCoordinates'][0][1]+2*CellHeight]]
        self._DesignParameter['DeMux1to4_2']['_XYCoordinates'] = [[
            self.getXY('DeMux1to2_3')[0][0] + self._DesignParameter['DeMux1to2_3']['_DesignObj'].CellXWidth  +UnitPitch ,
            self._DesignParameter['DeMux1to2_3']['_XYCoordinates'][0][1]+4*CellHeight]]
        self._DesignParameter['DeMux1to4_1']['_XYCoordinates'] = [[
            self.getXY('DeMux1to2_3')[0][0] + self._DesignParameter['DeMux1to2_3']['_DesignObj'].CellXWidth  +UnitPitch ,
            self._DesignParameter['DeMux1to2_3']['_XYCoordinates'][0][1]+4*CellHeight]]

        self._DesignParameter['DeMux1to4_5']['_XYCoordinates'] = [[
            self.getXY('DeMux1to2_3')[0][0] + self._DesignParameter['DeMux1to2_3']['_DesignObj'].CellXWidth  +UnitPitch ,
            self._DesignParameter['DeMux1to2_3']['_XYCoordinates'][0][1]]]
        self._DesignParameter['DeMux1to4_6']['_XYCoordinates'] = [[
            self.getXY('DeMux1to2_3')[0][0] + self._DesignParameter['DeMux1to2_3']['_DesignObj'].CellXWidth +UnitPitch  ,
            self._DesignParameter['DeMux1to2_3']['_XYCoordinates'][0][1]-2*CellHeight]]
        self._DesignParameter['DeMux1to4_7']['_XYCoordinates'] = [[
            self.getXY('DeMux1to2_3')[0][0] + self._DesignParameter['DeMux1to2_3']['_DesignObj'].CellXWidth +UnitPitch,
            self._DesignParameter['DeMux1to2_3']['_XYCoordinates'][0][1]-2*CellHeight]]
        self._DesignParameter['DeMux1to4_8']['_XYCoordinates'] = [[
            self.getXY('DeMux1to2_3')[0][0] + self._DesignParameter['DeMux1to2_3']['_DesignObj'].CellXWidth   +UnitPitch,
            self._DesignParameter['DeMux1to2_3']['_XYCoordinates'][0][1]-4*CellHeight]]

        tmpMet2Width = 66
        tmpDRC_Met2Spacing = 86
        tmpVia1YWidth = 100
        tmpViaMet2Width = 134
        tmpViaminWidth = 170
        tmpDSspace = 130

        ''' VDD Rail, VSS Rail, XVTLayer '''
        # VSS M2
        leftBoundary = self.getXYLeft('DeMux1to2_1','DFF_Latch','TG1', 'vss_supply_m2_y')[0][0]

        if self.getXYRight('DeMux1to4_3','DeMux1to2','DFFQ','INV4', 'PbodyContact', '_Met2Layer')[0][0]>self.getXYRight('Clk_Driver_2','DFFQb2','INV5', 'PbodyContact', '_Met2Layer')[0][0]:
            rightBoundary = self.getXYRight('DeMux1to4_3', 'DeMux1to2', 'DFFQ', 'INV4', 'PbodyContact', '_Met2Layer')[0][0]

        else :
            rightBoundary = self.getXYRight('Clk_Driver_2', 'DFFQb2', 'INV5', 'PbodyContact', '_Met2Layer')[0][0]

        YCoord = [self.getXY('DeMux1to2_1')[0][1],self.getXY('DeMux1to2_3')[0][1],self.getXY('DeMux1to2_5')[0][1]]

        self._DesignParameter['VSSRail_Met2'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _Width=self.getYWidth('DeMux1to2_1','DFFQ','INV4', 'PbodyContact', '_Met2Layer')
        )
        self._DesignParameter['VSSRail_Met2']['_XYCoordinates'] = [[[rightBoundary,YCoord[0]],[leftBoundary,YCoord[0]]],[[rightBoundary,YCoord[1]],[leftBoundary,YCoord[1]]],[[rightBoundary,YCoord[2]],[leftBoundary,YCoord[2]]]]



        # VSS OD(RX)
        leftBoundary = self.getXYLeft('DeMux1to2_1','DFF_Latch','TG1', 'vss_odlayer')[0][0]

        if self.getXYRight('DeMux1to4_3','DeMux1to2','DFFQ','INV4', 'PbodyContact', '_ODLayer')[0][0]>self.getXYRight('Clk_Driver_2','DFFQb2','INV5', 'PbodyContact', '_ODLayer')[0][0]:
            rightBoundary = self.getXYRight('DeMux1to4_3', 'DeMux1to2', 'DFFQ', 'INV4', 'PbodyContact', '_ODLayer')[0][0]

        else :
            rightBoundary = self.getXYRight('Clk_Driver_2', 'DFFQb2', 'INV5', 'PbodyContact', '_ODLayer')[0][0]

        YCoord = [self.getXY('DeMux1to2_1')[0][1],self.getXY('DeMux1to2_3')[0][1],self.getXY('DeMux1to2_5')[0][1]]

        self._DesignParameter['VSSRail_OD'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1],
            _Width=self.getYWidth('DeMux1to2_1','DFFQ','INV4', 'PbodyContact', '_ODLayer')
        )
        self._DesignParameter['VSSRail_OD']['_XYCoordinates'] = [[[rightBoundary,YCoord[0]],[leftBoundary,YCoord[0]]],[[rightBoundary,YCoord[1]],[leftBoundary,YCoord[1]]],[[rightBoundary,YCoord[2]],[leftBoundary,YCoord[2]]]]



        # VSS PP(BP)
        leftBoundary = self.getXYLeft('DeMux1to2_1','DFF_Latch','TG1', 'vss_pplayer')[0][0]

        if self.getXYRight('DeMux1to4_3','DeMux1to2','DFFQ','INV4', 'PbodyContact', '_PPLayer')[0][0]>self.getXYRight('Clk_Driver_2','DFFQb2','INV5', 'PbodyContact', '_PPLayer')[0][0]:
            rightBoundary = self.getXYRight('DeMux1to4_3', 'DeMux1to2', 'DFFQ', 'INV4', 'PbodyContact', '_PPLayer')[0][0]

        else :
            rightBoundary = self.getXYRight('Clk_Driver_2', 'DFFQb2', 'INV5', 'PbodyContact', '_PPLayer')[0][0]

        YCoord = [self.getXY('DeMux1to2_1')[0][1],self.getXY('DeMux1to2_3')[0][1],self.getXY('DeMux1to2_5')[0][1]]

        self._DesignParameter['VSSRail_PP'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _Width=self.getYWidth('DeMux1to2_1','DFFQ','INV4', 'PbodyContact', '_PPLayer')
        )
        self._DesignParameter['VSSRail_PP']['_XYCoordinates'] = [[[rightBoundary,YCoord[0]],[leftBoundary,YCoord[0]]],[[rightBoundary,YCoord[1]],[leftBoundary,YCoord[1]]],[[rightBoundary,YCoord[2]],[leftBoundary,YCoord[2]]]]



        ## VDD
        # VDD M2
        leftBoundary = self.getXYLeft('DeMux1to2_1','DFF_Latch','TG1', 'vdd_supply_m2_y')[0][0]

        if self.getXYRight('DeMux1to4_3','DeMux1to2','DFFQ','INV4',  'NbodyContact', '_Met2Layer')[0][0]>self.getXYRight('Clk_Driver_2','DFFQb2','INV5',  'NbodyContact', '_Met2Layer')[0][0]:
            rightBoundary = self.getXYRight('DeMux1to4_3', 'DeMux1to2', 'DFFQ', 'INV4',  'NbodyContact', '_Met2Layer')[0][0]

        else :
            rightBoundary = self.getXYRight('Clk_Driver_2', 'DFFQb2', 'INV5',  'NbodyContact', '_Met2Layer')[0][0]

        YCoord = [self.getXY('DeMux1to2_1',  'DFF_Latch', 'TG1', 'vdd_supply_m2_y')[0][1],self.getXY('DeMux1to2_3',  'DFF_Latch', 'TG1', 'vdd_supply_m2_y')[0][1],self.getXY('DeMux1to2_5',  'DFF_Latch', 'TG1', 'vdd_supply_m2_y')[0][1]]

        self._DesignParameter['VDDRail_Met2'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _Width=self.getYWidth('DeMux1to2_1','DFFQ','INV4',  'NbodyContact', '_Met2Layer')
        )
        self._DesignParameter['VDDRail_Met2']['_XYCoordinates'] = [[[rightBoundary,YCoord[0]],[leftBoundary,YCoord[0]]],[[rightBoundary,YCoord[1]],[leftBoundary,YCoord[1]]],[[rightBoundary,YCoord[2]],[leftBoundary,YCoord[2]]]]


        # VDD OD(RX)

        leftBoundary = self.getXYLeft('DeMux1to2_1','DFF_Latch','TG1', 'vdd_odlayer')[0][0]

        if self.getXYRight('DeMux1to4_3','DeMux1to2','DFFQ','INV4',  'NbodyContact', '_ODLayer')[0][0]>self.getXYRight('Clk_Driver_2','DFFQb2','INV5',  'NbodyContact', '_ODLayer')[0][0]:
            rightBoundary = self.getXYRight('DeMux1to4_3', 'DeMux1to2', 'DFFQ', 'INV4',  'NbodyContact', '_ODLayer')[0][0]

        else :
            rightBoundary = self.getXYRight('Clk_Driver_2', 'DFFQb2', 'INV5',  'NbodyContact', '_ODLayer')[0][0]

        YCoord = [self.getXY('DeMux1to2_1',  'DFF_Latch', 'TG1', 'vdd_odlayer')[0][1],self.getXY('DeMux1to2_3',  'DFF_Latch', 'TG1', 'vdd_odlayer')[0][1],self.getXY('DeMux1to2_5',  'DFF_Latch', 'TG1', 'vdd_odlayer')[0][1]]

        self._DesignParameter['VDDRail_OD'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1],
            _Width=self.getYWidth('DeMux1to2_1','DFFQ','INV4',  'NbodyContact', '_ODLayer')
        )
        self._DesignParameter['VDDRail_OD']['_XYCoordinates'] = [[[rightBoundary,YCoord[0]],[leftBoundary,YCoord[0]]],[[rightBoundary,YCoord[1]],[leftBoundary,YCoord[1]]],[[rightBoundary,YCoord[2]],[leftBoundary,YCoord[2]]]]


        # NWLayer
        NW_margin = 10
        leftBoundary = self.getXYLeft('DeMux1to2_1','DFF_Latch','TG1', 'NWELL_boundary_0')[0][0]

        if self.getXYRight('DeMux1to4_3','DeMux1to2','DFFQ','INV4',  '_NWLayerBoundary')[0][0]>self.getXYRight('Clk_Driver_2','DFFQb2','INV5',  '_NWLayerBoundary')[0][0]:
            rightBoundary = self.getXYRight('DeMux1to4_3', 'DeMux1to2', 'DFFQ', 'INV4',  '_NWLayerBoundary')[0][0]

        else :
            rightBoundary = self.getXYRight('Clk_Driver_2', 'DFFQb2', 'INV5',  '_NWLayerBoundary')[0][0]

        YCoord = [(self.getXYTop('DeMux1to2_1',  'DFF_Latch', '_NWLayer')[0][1]-self.getXYBot('DeMux1to2_1',  'DFF_Latch', '_NWLayer')[0][1])/2+self.getXYBot('DeMux1to2_1',  'DFF_Latch', '_NWLayer')[0][1],\
                 (self.getXYTop('DeMux1to2_3',  'DFF_Latch', '_NWLayer')[0][1]-self.getXYBot('DeMux1to2_3',  'DFF_Latch', '_NWLayer')[0][1])/2+self.getXYBot('DeMux1to2_3',  'DFF_Latch', '_NWLayer')[0][1],\
                  (self.getXYTop('DeMux1to2_5',  'DFF_Latch', '_NWLayer')[0][1]-self.getXYBot('DeMux1to2_5',  'DFF_Latch', '_NWLayer')[0][1])/2+self.getXYBot('DeMux1to2_5',  'DFF_Latch', '_NWLayer')[0][1],\
                  (self.getXYTop('DeMux1to2_2',  'DFF_Latch', '_NWLayer')[0][1]-self.getXYBot('DeMux1to2_2',  'DFF_Latch', '_NWLayer')[0][1])/2+self.getXYBot('DeMux1to2_2',  'DFF_Latch', '_NWLayer')[0][1],\
                  (self.getXYTop('DeMux1to2_4',  'DFF_Latch', '_NWLayer')[0][1]-self.getXYBot('DeMux1to2_4',  'DFF_Latch', '_NWLayer')[0][1])/2+self.getXYBot('DeMux1to2_4',  'DFF_Latch', '_NWLayer')[0][1]]


        self._DesignParameter['_NWLayer'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _Width= self.getXYTop('DeMux1to2_1','DFF_Latch', '_NWLayer')[0][1]-self.getXYBot('DeMux1to2_1','DFF_Latch', '_NWLayer')[0][1]+NW_margin
        )
        self._DesignParameter['_NWLayer']['_XYCoordinates'] = [[[rightBoundary,YCoord[0]],[leftBoundary,YCoord[0]]],[[rightBoundary,YCoord[1]],[leftBoundary,YCoord[1]]],[[rightBoundary,YCoord[2]],[leftBoundary,YCoord[2]]],[[rightBoundary,YCoord[3]],[leftBoundary,YCoord[3]]],[[rightBoundary,YCoord[4]],[leftBoundary,YCoord[4]]]]



        # PPLayer (ADDED by smlim)
        PP_margin=10
        leftBoundary = self.getXYLeft('DeMux1to2_1','DFF_Latch','TG1',  'pmos', '_PPLayer')[0][0]

        if self.getXYRight('DeMux1to4_3','DeMux1to2','DFFQ','INV4',   '_PMOS', '_PPLayer')[0][0]>self.getXYRight('Clk_Driver_2','DFFQb2','INV5',  '_PMOS', '_PPLayer')[0][0]:
            rightBoundary = self.getXYRight('DeMux1to4_3', 'DeMux1to2', 'DFFQ', 'INV4',   '_PMOS', '_PPLayer')[0][0]

        else :
            rightBoundary = self.getXYRight('Clk_Driver_2', 'DFFQb2', 'INV5',   '_PMOS', '_PPLayer')[0][0]

        YCoord = [(self.getXYTop('DeMux1to2_1',  '_PPLayer')[0][1]-self.getXYBot('DeMux1to2_1',   '_PPLayer')[0][1])/2.0+ float(self.getXYBot('DeMux1to2_1',   '_PPLayer')[0][1]),\
                  (self.getXYTop('DeMux1to2_3',  '_PPLayer')[0][1]-self.getXYBot('DeMux1to2_3',   '_PPLayer')[0][1])/2.0+ float(self.getXYBot('DeMux1to2_3',  '_PPLayer')[0][1]),\
                  (self.getXYTop('DeMux1to2_5',   '_PPLayer')[0][1]-self.getXYBot('DeMux1to2_5',   '_PPLayer')[0][1])/2.0+ float(self.getXYBot('DeMux1to2_5',  '_PPLayer')[0][1]),\
                  (self.getXYTop('DeMux1to2_2',  '_PPLayer')[0][1]-self.getXYBot('DeMux1to2_2',   '_PPLayer')[0][1])/2.0+ float(self.getXYBot('DeMux1to2_2',  '_PPLayer')[0][1]),\
                  (self.getXYTop('DeMux1to2_4',   '_PPLayer')[0][1]-self.getXYBot('DeMux1to2_4',   '_PPLayer')[0][1])/2.0+ float(self.getXYBot('DeMux1to2_4',  '_PPLayer')[0][1])]

        self._DesignParameter['_PPLayer'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _Width= float(self.getXYTop('DeMux1to4_4','_PPLayer')[0][1])-float(self.getXYBot('DeMux1to4_4', '_PPLayer')[0][1]) + PP_margin
        )
        self._DesignParameter['_PPLayer']['_XYCoordinates'] = [[[rightBoundary,YCoord[0]],[leftBoundary,YCoord[0]]],[[rightBoundary,YCoord[1]],[leftBoundary,YCoord[1]]],[[rightBoundary,YCoord[2]],[leftBoundary,YCoord[2]]],[[rightBoundary,YCoord[3]],[leftBoundary,YCoord[3]]],[[rightBoundary,YCoord[4]],[leftBoundary,YCoord[4]]]]


        # XVTLayer
        assert XVT in ('SLVT', 'LVT', 'RVT', 'HVT')
        leftBoundary = self.getXYLeft('DeMux1to2_1','DFF_Latch','TG1',  'XVT_boundary_1')[0][0]

        if self.getXYRight('DeMux1to4_3','DeMux1to2','DFFQ','INV4',  'XVTLayer')[0][0]>self.getXYRight('Clk_Driver_2','DFFQb2','INV5', 'XVTLayer')[0][0]:
            rightBoundary = self.getXYRight('DeMux1to4_3', 'DeMux1to2', 'DFFQ', 'INV4',  'XVTLayer')[0][0]

        else :
            rightBoundary = self.getXYRight('Clk_Driver_2', 'DFFQb2', 'INV5',   'XVTLayer')[0][0]

        YCoord = [self.getXY('DeMux1to2_1',  'DFF_Latch', 'TG1', 'XVT_boundary_1')[0][1],self.getXY('DeMux1to2_3',  'DFF_Latch', 'TG1', 'XVT_boundary_1')[0][1],self.getXY('DeMux1to2_5',  'DFF_Latch',  'TG1', 'XVT_boundary_1')[0][1],self.getXY('DeMux1to2_2',  'DFF_Latch',  'TG1', 'XVT_boundary_1')[0][1],self.getXY('DeMux1to2_4',  'DFF_Latch',  'TG1', 'XVT_boundary_1')[0][1]]

        self._DesignParameter['XVTLayer'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping[XVT][0], _Datatype=DesignParameters._LayerMapping[XVT][1],
            _Width= self.getYWidth('DeMux1to2_1',  'DFF_Latch','INV5', 'XVTLayer')
        )
        self._DesignParameter['XVTLayer']['_XYCoordinates'] = [[[rightBoundary,YCoord[0]],[leftBoundary,YCoord[0]]],[[rightBoundary,YCoord[1]],[leftBoundary,YCoord[1]]],[[rightBoundary,YCoord[2]],[leftBoundary,YCoord[2]]],[[rightBoundary,YCoord[3]],[leftBoundary,YCoord[3]]],[[rightBoundary,YCoord[4]],[leftBoundary,YCoord[4]]]]

        ####################### CLK input Routing ##########################

        self._DesignParameter['_Met3_clkin'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met3_clkin']['_XYCoordinates'] = [[[self._DesignParameter['DeMux1to2_3']['_DesignObj'].clk[0],self.getXY('DeMux1to2_3')[0][1]+self._DesignParameter['DeMux1to2_3']['_DesignObj'].clk[1]],[self._DesignParameter['DeMux1to2_3']['_DesignObj'].clk[0]+4*tmpDSspace,self.getXY('DeMux1to2_3')[0][1]+self._DesignParameter['DeMux1to2_3']['_DesignObj'].clk[1]]],\
                                                                  [[self.getXY('DeMux1to2_3')[0][0],self.getXY('DeMux1to2_3')[0][1]+3*CellHeight],[self._DesignParameter['DeMux1to2_3']['_DesignObj'].clk[0]+4*tmpDSspace,self.getXY('DeMux1to2_3')[0][1]+3*CellHeight]],\
                                                                  [[self._DesignParameter['DeMux1to2_3']['_DesignObj'].clkb[0],self.getXY('DeMux1to2_3')[0][1]+self._DesignParameter['DeMux1to2_3']['_DesignObj'].clkb[1]],[self._DesignParameter['DeMux1to2_3']['_DesignObj'].clkb[0]-4*tmpDSspace,self.getXY('DeMux1to2_3')[0][1]+self._DesignParameter['DeMux1to2_3']['_DesignObj'].clkb[1]]],\
                                                                  [[self.getXY('DeMux1to2_3')[0][0],self.getXY('DeMux1to2_3')[0][1]+3*CellHeight-tmpDSspace],[self._DesignParameter['DeMux1to2_3']['_DesignObj'].clkb[0]-4*tmpDSspace,self.getXY('DeMux1to2_3')[0][1]+3*CellHeight-tmpDSspace]],\
                                                                  [[self.getXY('Clk_Driver_1')[0][0]+self._DesignParameter['Clk_Driver_1']['_DesignObj'].clkinput[0]+4*tmpDSspace,self.getXY('Clk_Driver_1')[0][1]+3*CellHeight],[self.getXY('DeMux1to2_3')[0][0],self.getXY('Clk_Driver_1')[0][1]+3*CellHeight]]]#clk_divier



        self._DesignParameter['_Met4_clkin'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met4_clkin']['_XYCoordinates'] = [[[self._DesignParameter['DeMux1to2_3']['_DesignObj'].clk[0]+4*tmpDSspace,self._DesignParameter['DeMux1to2_3']['_DesignObj'].clk[1]],[self._DesignParameter['DeMux1to2_3']['_DesignObj'].clk[0]+4*tmpDSspace,self.getXY('DeMux1to2_3')[0][1]+3*CellHeight]],\
                                                                    [[self._DesignParameter['DeMux1to2_3']['_DesignObj'].clkb[0]-4*tmpDSspace,self._DesignParameter['DeMux1to2_3']['_DesignObj'].clkb[1]],[self._DesignParameter['DeMux1to2_3']['_DesignObj'].clkb[0]-4*tmpDSspace,self.getXY('DeMux1to2_3')[0][1]+3*CellHeight-tmpDSspace]],\
                                                                  [[self.getXY('Clk_Driver_1')[0][0]+self._DesignParameter['Clk_Driver_1']['_DesignObj'].clkinput[0]+4*tmpDSspace,self.getXY('Clk_Driver_1')[0][1]+3*CellHeight],\
                                                                   [self.getXY('Clk_Driver_1')[0][0]+self._DesignParameter['Clk_Driver_1']['_DesignObj'].clkinput[0]+4*tmpDSspace,self.getXY('Clk_Driver_1')[0][1]+self._DesignParameter['Clk_Driver_1']['_DesignObj'].clkinput[1]]]] #clk_dividier signal




        self._DesignParameter['_ViaMet32Met4_clkin'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='_ViaMet32Met4_clkinIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4_clkin']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=1))
        self._DesignParameter['_ViaMet32Met4_clkin']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet32Met4_clkin']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet32Met4_clkin']['_DesignObj']._DesignParameter['_COLayer']['_XWidth'] = tmpVia1YWidth

        self._DesignParameter['_ViaMet32Met4_clkin']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to2_3']['_DesignObj'].clk[0]+4*tmpDSspace,self._DesignParameter['DeMux1to2_3']['_DesignObj'].clk[1]],\
                                                                          [self._DesignParameter['DeMux1to2_3']['_DesignObj'].clk[0]+4*tmpDSspace,self.getXY('DeMux1to2_3')[0][1]+3*CellHeight],\
                                                                          [self._DesignParameter['DeMux1to2_3']['_DesignObj'].clkb[0]-4*tmpDSspace,self._DesignParameter['DeMux1to2_3']['_DesignObj'].clkb[1]],\
                                                                          [self._DesignParameter['DeMux1to2_3']['_DesignObj'].clkb[0]-4*tmpDSspace,self.getXY('DeMux1to2_3')[0][1]+3*CellHeight-tmpDSspace],\
                                                                          [self.getXY('Clk_Driver_1')[0][0]+self._DesignParameter['Clk_Driver_1']['_DesignObj'].clkinput[0]+4*tmpDSspace,self.getXY('Clk_Driver_1')[0][1]+3*CellHeight],\
                                                                           [self.getXY('Clk_Driver_1')[0][0]+self._DesignParameter['Clk_Driver_1']['_DesignObj'].clkinput[0]+4*tmpDSspace,self.getXY('Clk_Driver_1')[0][1]+self._DesignParameter['Clk_Driver_1']['_DesignObj'].clkinput[1]]]





        ####################### CLK input Routing end ##########################

        ####################### Clk_Driver 1 to 2 connection ##########################

        self._DesignParameter['_Met3_clk_connect'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met3_clk_connect']['_XYCoordinates'] = [
            [[self.getXY('Clk_Driver_1')[0][0]+self._DesignParameter['Clk_Driver_1']['_DesignObj'].f[0],self.getXY('Clk_Driver_1')[0][1]+self._DesignParameter['Clk_Driver_1']['_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclkb],\
            [self.getXY('Clk_Driver_1')[0][0]+self._DesignParameter['Clk_Driver_1']['_DesignObj'].f90b[0] + tmpMet2Width / 2,self.getXY('Clk_Driver_1')[0][1]+self._DesignParameter['Clk_Driver_1']['_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclkb]],\
            [[self.getXY('Clk_Driver_2')[0][0]+self._DesignParameter['Clk_Driver_2']['_DesignObj'].clkinput[0],self.getXY('Clk_Driver_2')[0][1]+self._DesignParameter['Clk_Driver_2']['_DesignObj'].clkinput[1]],\
            [self.getXY('Clk_Driver_1')[0][0]+self._DesignParameter['Clk_Driver_1']['_DesignObj'].f90b[0] + tmpMet2Width / 2,self.getXY('Clk_Driver_2')[0][1]+self._DesignParameter['Clk_Driver_2']['_DesignObj'].clkinput[1]]],\
            [[self.getXY('Clk_Driver_1')[0][0]+self._DesignParameter['Clk_Driver_1']['_DesignObj'].f90b[0],self.getXY('Clk_Driver_2')[0][1]+self._DesignParameter['Clk_Driver_2']['_DesignObj'].clkinput[1] - tmpMet2Width / 2],\
            [self.getXY('Clk_Driver_1')[0][0]+self._DesignParameter['Clk_Driver_1']['_DesignObj'].f90b[0],self.getXY('Clk_Driver_1')[0][1]+self._DesignParameter['Clk_Driver_1']['_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclkb + tmpMet2Width / 2]]]



        self._DesignParameter['_ViaMet22Met3_Clk_Drive'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='_ViaMet22Met3_Clk_DriveIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3_Clk_Drive']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=1))
        self._DesignParameter['_ViaMet22Met3_Clk_Drive']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet22Met3_Clk_Drive']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet22Met3_Clk_Drive']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = tmpVia1YWidth



        self._DesignParameter['_ViaMet22Met3_Clk_Drive']['_XYCoordinates'] = [[self.getXY('Clk_Driver_1')[0][0]+self._DesignParameter['Clk_Driver_1']['_DesignObj'].f[0],self.getXY('Clk_Driver_1')[0][1]+self._DesignParameter['Clk_Driver_1']['_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclkb- tmpViaMet2Width / 2 + tmpMet2Width / 2],\
                                                                              [self.getXY('Clk_Driver_1')[0][0]+self._DesignParameter['Clk_Driver_1']['_DesignObj'].f90[0],self.getXY('Clk_Driver_1')[0][1]+self._DesignParameter['Clk_Driver_1']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclkb- tmpViaMet2Width / 2 + tmpMet2Width / 2],\
                                                                              [self.getXY('Clk_Driver_2')[0][0]+self._DesignParameter['Clk_Driver_2']['_DesignObj'].f[0],self.getXY('Clk_Driver_2')[0][1]+self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclkb- tmpViaMet2Width / 2 + tmpMet2Width / 2],\
                                                                              [self.getXY('Clk_Driver_2')[0][0]+self._DesignParameter['Clk_Driver_2']['_DesignObj'].f90[0],self.getXY('Clk_Driver_2')[0][1]+self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclkb- tmpViaMet2Width / 2 + tmpMet2Width / 2]]

        ####################### 1st stage data ouput to 2nd stage data input ##########################

        self._DesignParameter['_Met3_data1to2'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met3_data1to2']['_XYCoordinates'] = [[[self._DesignParameter['DeMux1to2_3']['_DesignObj'].D1[0]+tmpDSspace,self._DesignParameter['DeMux1to2_3']['_DesignObj'].D1[1]],\
                                                                       [self._DesignParameter['DeMux1to2_3']['_DesignObj'].D2[0],self._DesignParameter['DeMux1to2_3']['_DesignObj'].D1[1]]]]



        self._DesignParameter['_Met4_data1to2'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met4_data1to2']['_XYCoordinates'] = [[[self._DesignParameter['DeMux1to2_3']['_DesignObj'].D1[0],self.getXY('DeMux1to2_1')[0][1]+self._DesignParameter['DeMux1to2_1']['_DesignObj'].datain[1]],self._DesignParameter['DeMux1to2_3']['_DesignObj'].D1],\
                                                                    [[self._DesignParameter['DeMux1to2_3']['_DesignObj'].D1[0]+tmpDSspace,self.getXY('DeMux1to2_5')[0][1]+self._DesignParameter['DeMux1to2_5']['_DesignObj'].datain[1]],[self._DesignParameter['DeMux1to2_3']['_DesignObj'].D1[0]+tmpDSspace,self._DesignParameter['DeMux1to2_3']['_DesignObj'].D1[1]]]]


        self._DesignParameter['_ViaMet32Met4_data1to2'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='_ViaMet32Met4_data1to2In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4_data1to2']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=1))
        self._DesignParameter['_ViaMet32Met4_data1to2']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet32Met4_data1to2']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet32Met4_data1to2']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = tmpVia1YWidth

        self._DesignParameter['_ViaMet32Met4_data1to2']['_XYCoordinates'] = [self._DesignParameter['DeMux1to2_3']['_DesignObj'].D1,[self._DesignParameter['DeMux1to2_3']['_DesignObj'].D1[0]+tmpDSspace,self._DesignParameter['DeMux1to2_3']['_DesignObj'].D2[1]]]

        self._DesignParameter['_ViaMet32Met4_data1to2_2'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='_ViaMet32Met4_data1to2_2In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4_data1to2_2']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=1))
        self._DesignParameter['_ViaMet32Met4_data1to2_2']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet32Met4_data1to2_2']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet32Met4_data1to2_2']['_DesignObj']._DesignParameter['_COLayer']['_XWidth'] = tmpVia1YWidth

        self._DesignParameter['_ViaMet32Met4_data1to2_2']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to2_3']['_DesignObj'].D1[0],self.getXY('DeMux1to2_1')[0][1]+self._DesignParameter['DeMux1to2_1']['_DesignObj'].datain[1]],\
                                                                               [self._DesignParameter['DeMux1to2_3']['_DesignObj'].D1[0]+tmpDSspace,self.getXY('DeMux1to2_5')[0][1]+self._DesignParameter['DeMux1to2_5']['_DesignObj'].datain[1]],\
                                                                               [self._DesignParameter['DeMux1to2_3']['_DesignObj'].D1[0]+tmpDSspace,-self._DesignParameter['DeMux1to2_5']['_DesignObj'].datain[1]],\
                                                                               [self._DesignParameter['DeMux1to2_3']['_DesignObj'].D1[0],self.getXY('DeMux1to2_1')[0][1]-self._DesignParameter['DeMux1to2_2']['_DesignObj'].datain[1]]]

        ####################### 2nd stage data ouput to 3rd stage data input ##########################

        self._DesignParameter['_Met3_data2to3'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met4_data2to3'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _Width=tmpMet2Width
        )

        self._DesignParameter['_ViaMet32Met4_data2to3'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='_ViaMet32Met4_data2to3In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4_data2to3']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=1))
        self._DesignParameter['_ViaMet32Met4_data2to3']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet32Met4_data2to3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet32Met4_data2to3']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = tmpVia1YWidth



        ####D2,D4
        ### DeMux1to2_1
        self._DesignParameter['_Met3_data2to3']['_XYCoordinates'] = [[[self.getXY('DeMux1to2_1','DFFQ','_qpin')[0][0]-tmpMet2Width/2,self.getXY('DeMux1to4_3')[0][1]+self._DesignParameter['DeMux1to4_3']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib],\
                                                                       [self.getXY('DeMux1to4_3','DFF_Latch_Latch','_dpin')[0][0],self.getXY('DeMux1to4_3')[0][1]+self._DesignParameter['DeMux1to4_3']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib]],\
                                                                     [[self.getXY('DeMux1to2_1','DFFQ','_qpin')[0][0],self.getXY('DeMux1to2_1','DFFQ','_qpin')[0][1]],\
                                                                      [self.getXY('DeMux1to2_1','DFFQ','_qpin')[0][0],self.getXY('DeMux1to4_3')[0][1]+self._DesignParameter['DeMux1to4_3']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib]]]

        ### DeMux1to2_5
        self._DesignParameter['_Met3_data2to3']['_XYCoordinates'].append([[self.getXY('DeMux1to2_5','DFFQ','_qpin')[0][0]-tmpMet2Width/2,self.getXY('DeMux1to4_6')[0][1]+self._DesignParameter['DeMux1to4_6']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib],\
                                                                       [self.getXY('DeMux1to4_6','DFF_Latch_Latch','_dpin')[0][0],self.getXY('DeMux1to4_6')[0][1]+self._DesignParameter['DeMux1to4_6']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib]])

        self._DesignParameter['_Met3_data2to3']['_XYCoordinates'].append([[self.getXY('DeMux1to2_5','DFFQ','_qpin')[0][0],self.getXY('DeMux1to2_5','DFFQ','_qpin')[0][1]],\
                                                                      [self.getXY('DeMux1to2_5','DFFQ','_qpin')[0][0],self.getXY('DeMux1to4_6')[0][1]+self._DesignParameter['DeMux1to4_6']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib]])

        ### DeMux1to2_2
        self._DesignParameter['_Met3_data2to3']['_XYCoordinates'].append([[(self.getXY('DeMux1to2_2','DFFQ','_qpin')[0][0]-tmpMet2Width/2),self.getXY('DeMux1to2_2')[0][1]-self._DesignParameter['DeMux1to4_4']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib],\
                                                                       [self.getXY('DeMux1to4_4','DFF_Latch_Latch','_dpin')[0][0],self.getXY('DeMux1to2_2')[0][1]-self._DesignParameter['DeMux1to4_4']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib]])

        self._DesignParameter['_Met3_data2to3']['_XYCoordinates'].append([[self.getXY('DeMux1to2_2','DFFQ','_qpin')[0][0],self.getXY('DeMux1to2_2','DFFQ','_qpin')[0][1]],\
                                                                      [self.getXY('DeMux1to2_2','DFFQ','_qpin')[0][0],self.getXY('DeMux1to2_2')[0][1]-self._DesignParameter['DeMux1to4_4']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib]])

        ### DeMux1to2_4
        self._DesignParameter['_Met3_data2to3']['_XYCoordinates'].append([[(self.getXY('DeMux1to2_4','DFFQ','_qpin')[0][0]-tmpMet2Width/2),-self._DesignParameter['DeMux1to4_5']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib],\
                                                                       [self.getXY('DeMux1to4_5','DFF_Latch_Latch','_dpin')[0][0],-self._DesignParameter['DeMux1to4_5']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib]])

        self._DesignParameter['_Met3_data2to3']['_XYCoordinates'].append([[self.getXY('DeMux1to2_4','DFFQ','_qpin')[0][0],self.getXY('DeMux1to2_4','DFFQ','_qpin')[0][1]],\
                                                                      [self.getXY('DeMux1to2_4','DFFQ','_qpin')[0][0],-(self.getXY('DeMux1to4_5')[0][1]+self._DesignParameter['DeMux1to4_5']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib)]])

        ###D1,D3
        ## DeMux1to2_1
        self._DesignParameter['_Met3_data2to3']['_XYCoordinates'].append([[self.getXY('DeMux1to2_1','DFF_Latch','_qbpin')[0][0],self.getXY('DeMux1to2_1','DFF_Latch','_qbpin')[0][1]],\
                                                                       [self.getXY('DeMux1to2_1','DFFQ','_qpin')[0][0]-2*tmpDSspace,self.getXY('DeMux1to2_1','DFF_Latch','_qbpin')[0][1]]])
        self._DesignParameter['_Met3_data2to3']['_XYCoordinates'].append([[self.getXY('DeMux1to2_1','DFFQ','_qpin')[0][0]-2*tmpDSspace,self.getXY('DeMux1to4_1')[0][1]+self._DesignParameter['DeMux1to4_1']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib],\
                                                                           [self.getXY('DeMux1to4_1','DFF_Latch_Latch','_dpin')[0][0],self.getXY('DeMux1to4_1')[0][1]+self._DesignParameter['DeMux1to4_1']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib]])
        self._DesignParameter['_Met4_data2to3']['_XYCoordinates']=[[[self.getXY('DeMux1to2_1','DFFQ','_qpin')[0][0]-2*tmpDSspace,self.getXY('DeMux1to4_1')[0][1]+self._DesignParameter['DeMux1to4_1']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib],\
                                                                          [self.getXY('DeMux1to2_1','DFFQ','_qpin')[0][0]-2*tmpDSspace,self.getXY('DeMux1to2_1','DFF_Latch','_qbpin')[0][1]]]]
        self._DesignParameter['_ViaMet32Met4_data2to3']['_XYCoordinates']=[[self.getXY('DeMux1to2_1','DFFQ','_qpin')[0][0]-2*tmpDSspace,self.getXY('DeMux1to4_1')[0][1]+self._DesignParameter['DeMux1to4_1']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib- tmpViaMet2Width / 2 + tmpMet2Width / 2],\
                                                                            [self.getXY('DeMux1to2_1','DFFQ','_qpin')[0][0]-2*tmpDSspace,self.getXY('DeMux1to2_1','DFF_Latch','_qbpin')[0][1]+ tmpViaMet2Width / 2 - tmpMet2Width / 2]]


        ### DeMux1to2_5
        self._DesignParameter['_Met3_data2to3']['_XYCoordinates'].append([[self.getXY('DeMux1to2_5','DFF_Latch','_qbpin')[0][0],self.getXY('DeMux1to2_5','DFF_Latch','_qbpin')[0][1]],\
                                                                       [self.getXY('DeMux1to2_5','DFFQ','_qpin')[0][0]-2*tmpDSspace,self.getXY('DeMux1to2_5','DFF_Latch','_qbpin')[0][1]]])
        self._DesignParameter['_Met3_data2to3']['_XYCoordinates'].append([[self.getXY('DeMux1to2_5','DFFQ','_qpin')[0][0]-2*tmpDSspace,self.getXY('DeMux1to4_8')[0][1]+self._DesignParameter['DeMux1to4_8']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib],\
                                                                           [self.getXY('DeMux1to4_8','DFF_Latch_Latch','_dpin')[0][0],self.getXY('DeMux1to4_8')[0][1]+self._DesignParameter['DeMux1to4_8']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib]])
        self._DesignParameter['_Met4_data2to3']['_XYCoordinates'].append([[self.getXY('DeMux1to2_5','DFFQ','_qpin')[0][0]-2*tmpDSspace,self.getXY('DeMux1to4_8')[0][1]+self._DesignParameter['DeMux1to4_8']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib],\
                                                                          [self.getXY('DeMux1to2_5','DFFQ','_qpin')[0][0]-2*tmpDSspace,self.getXY('DeMux1to2_5','DFF_Latch','_qbpin')[0][1]]])
        self._DesignParameter['_ViaMet32Met4_data2to3']['_XYCoordinates'].append([self.getXY('DeMux1to2_5','DFFQ','_qpin')[0][0]-2*tmpDSspace,self.getXY('DeMux1to4_8')[0][1]+self._DesignParameter['DeMux1to4_8']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib+ tmpViaMet2Width / 2 - tmpMet2Width / 2])
        self._DesignParameter['_ViaMet32Met4_data2to3']['_XYCoordinates'].append([self.getXY('DeMux1to2_5','DFFQ','_qpin')[0][0]-2*tmpDSspace,self.getXY('DeMux1to2_5','DFF_Latch','_qbpin')[0][1]- tmpViaMet2Width / 2 + tmpMet2Width / 2])

        ### DeMux1to2_2
        self._DesignParameter['_Met3_data2to3']['_XYCoordinates'].append([[self.getXY('DeMux1to2_2','DFF_Latch','_qbpin')[0][0],self.getXY('DeMux1to2_2','DFF_Latch','_qbpin')[0][1]],\
                                                                       [self.getXY('DeMux1to2_1','DFFQ','_qpin')[0][0]-4*tmpDSspace,self.getXY('DeMux1to2_2','DFF_Latch','_qbpin')[0][1]]])
        self._DesignParameter['_Met3_data2to3']['_XYCoordinates'].append([[self.getXY('DeMux1to2_1','DFFQ','_qpin')[0][0]-4*tmpDSspace,self.getXY('DeMux1to4_1')[0][1]-self._DesignParameter['DeMux1to4_1']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib],\
                                                                           [self.getXY('DeMux1to4_1','DFF_Latch_Latch','_dpin')[0][0],self.getXY('DeMux1to4_1')[0][1]-self._DesignParameter['DeMux1to4_1']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib]])
        self._DesignParameter['_Met4_data2to3']['_XYCoordinates'].append([[self.getXY('DeMux1to2_1','DFFQ','_qpin')[0][0]-4*tmpDSspace,self.getXY('DeMux1to4_1')[0][1]-self._DesignParameter['DeMux1to4_1']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib],\
                                                                          [self.getXY('DeMux1to2_1','DFFQ','_qpin')[0][0]-4*tmpDSspace,self.getXY('DeMux1to2_2','DFF_Latch','_qbpin')[0][1]]])
        self._DesignParameter['_ViaMet32Met4_data2to3']['_XYCoordinates'].append([self.getXY('DeMux1to2_1','DFFQ','_qpin')[0][0]-4*tmpDSspace,self.getXY('DeMux1to4_1')[0][1]-self._DesignParameter['DeMux1to4_1']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib- tmpViaMet2Width / 2 + tmpMet2Width / 2])
        self._DesignParameter['_ViaMet32Met4_data2to3']['_XYCoordinates'].append([self.getXY('DeMux1to2_1','DFFQ','_qpin')[0][0]-4*tmpDSspace,self.getXY('DeMux1to2_2','DFF_Latch','_qbpin')[0][1]+ tmpViaMet2Width / 2 - tmpMet2Width / 2])

        ### DeMux1to2_4
        self._DesignParameter['_Met3_data2to3']['_XYCoordinates'].append([[self.getXY('DeMux1to2_5','DFF_Latch','_qbpin')[0][0],self.getXY('DeMux1to2_4','DFF_Latch','_qbpin')[0][1]],\
                                                                       [self.getXY('DeMux1to2_5','DFFQ','_qpin')[0][0]-4*tmpDSspace,self.getXY('DeMux1to2_4','DFF_Latch','_qbpin')[0][1]]])
        self._DesignParameter['_Met3_data2to3']['_XYCoordinates'].append([[self.getXY('DeMux1to2_5','DFFQ','_qpin')[0][0]-4*tmpDSspace,self.getXY('DeMux1to4_7')[0][1]-self._DesignParameter['DeMux1to4_8']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib],\
                                                                           [self.getXY('DeMux1to4_8','DFF_Latch_Latch','_dpin')[0][0],self.getXY('DeMux1to4_7')[0][1]-self._DesignParameter['DeMux1to4_8']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib]])
        self._DesignParameter['_Met4_data2to3']['_XYCoordinates'].append([[self.getXY('DeMux1to2_5','DFFQ','_qpin')[0][0]-4*tmpDSspace,self.getXY('DeMux1to4_7')[0][1]-self._DesignParameter['DeMux1to4_8']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib],\
                                                                          [self.getXY('DeMux1to2_5','DFFQ','_qpin')[0][0]-4*tmpDSspace,self.getXY('DeMux1to2_4','DFF_Latch','_qbpin')[0][1]]])
        self._DesignParameter['_ViaMet32Met4_data2to3']['_XYCoordinates'].append([self.getXY('DeMux1to2_5','DFFQ','_qpin')[0][0]-4*tmpDSspace,self.getXY('DeMux1to4_7')[0][1]-self._DesignParameter['DeMux1to4_8']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib+ tmpViaMet2Width / 2 - tmpMet2Width / 2])
        self._DesignParameter['_ViaMet32Met4_data2to3']['_XYCoordinates'].append([self.getXY('DeMux1to2_5','DFFQ','_qpin')[0][0]-4*tmpDSspace,self.getXY('DeMux1to2_4','DFF_Latch','_qbpin')[0][1]- tmpViaMet2Width / 2 + tmpMet2Width / 2])

        ####################### 2nd stage data ouput to 3rd stage data input end!!!!!!


        ####################### 3rd stage data ouput to next circuit ##########################
        Dataoutspacing=200

        self._DesignParameter['_Met3_data3toend'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met4_data3toend'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _Width=tmpMet2Width
        )

        self._DesignParameter['_ViaMet32Met4_data3toend'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='_ViaMet32Met4_data3toendIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4_data3toend']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=1))
        self._DesignParameter['_ViaMet32Met4_data3toend']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet32Met4_data3toend']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet32Met4_data3toend']['_DesignObj']._DesignParameter['_COLayer']['_XWidth'] = tmpVia1YWidth


        ## DeMux1to4_1 ##

        DeMux1to4x=self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]
        DeMux1to4y=self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][1]
        D1x=self._DesignParameter['DeMux1to4_1']['_DesignObj'].D1[0]
        D1y=self._DesignParameter['DeMux1to4_1']['_DesignObj'].D1[1]
        D2x = self._DesignParameter['DeMux1to4_1']['_DesignObj'].D2[0]
        D2y = self._DesignParameter['DeMux1to4_1']['_DesignObj'].D2[1]
        D3x = self._DesignParameter['DeMux1to4_1']['_DesignObj'].D3[0]
        D3y = self._DesignParameter['DeMux1to4_1']['_DesignObj'].D3[1]
        D4x = self._DesignParameter['DeMux1to4_1']['_DesignObj'].D4[0]
        D4y = self._DesignParameter['DeMux1to4_1']['_DesignObj'].D4[1]
        iclk=self._DesignParameter['DeMux1to4_1']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclk
        iclkb=self._DesignParameter['DeMux1to4_1']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclkb
        CellXWidth=self._DesignParameter['DeMux1to4_1']['_DesignObj'].CellXWidth
        self._DesignParameter['_Met3_data3toend']['_XYCoordinates']=[[[DeMux1to4x+D1x,DeMux1to4y+iclk+Dataoutspacing],\
                                                                      [DeMux1to4x+CellXWidth,DeMux1to4y+iclk+Dataoutspacing]],\
                                                                     [[DeMux1to4x+D2x,DeMux1to4y+iclk],\
                                                                      [DeMux1to4x+CellXWidth,DeMux1to4y+iclk]],\
                                                                     [[DeMux1to4x+D3x,DeMux1to4y+iclkb],\
                                                                      [DeMux1to4x+CellXWidth,DeMux1to4y+iclkb]],\
                                                                     [[DeMux1to4x+D4x,DeMux1to4y+D4y],\
                                                                      [DeMux1to4x+CellXWidth,DeMux1to4y+D4y]]]

        self._DesignParameter['_Met4_data3toend']['_XYCoordinates']=[[[DeMux1to4x+D1x,DeMux1to4y+iclk+Dataoutspacing],\
                                                                      [DeMux1to4x+D1x,DeMux1to4y+D1y]],\
                                                                     [[DeMux1to4x+D2x,DeMux1to4y+iclk],\
                                                                      [DeMux1to4x+D2x,DeMux1to4y+D2y]],\
                                                                     [[DeMux1to4x+D3x,DeMux1to4y+iclkb],\
                                                                      [DeMux1to4x+D3x,DeMux1to4y+D3y]]]

        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates']=[[DeMux1to4x+D1x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y+iclk+Dataoutspacing],\
                                                                      [DeMux1to4x+D1x- tmpViaMet2Width / 2 + tmpMet2Width / 2,DeMux1to4y+D1y],\
                                                                     [DeMux1to4x+D2x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y+iclk],\
                                                                      [DeMux1to4x+D2x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y+D2y],\
                                                                     [DeMux1to4x+D3x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y+iclkb],\
                                                                      [DeMux1to4x+D3x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y+D3y]]

        ## DeMux1to4_2 ##

        DeMux1to4x=self._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][0]
        DeMux1to4y=self._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][1]

        D1x=self._DesignParameter['DeMux1to4_2']['_DesignObj'].D1[0]
        D1y=self._DesignParameter['DeMux1to4_2']['_DesignObj'].D1[1]
        D2x = self._DesignParameter['DeMux1to4_2']['_DesignObj'].D2[0]
        D2y = self._DesignParameter['DeMux1to4_2']['_DesignObj'].D2[1]
        D3x = self._DesignParameter['DeMux1to4_2']['_DesignObj'].D3[0]
        D3y = self._DesignParameter['DeMux1to4_2']['_DesignObj'].D3[1]
        D4x = self._DesignParameter['DeMux1to4_2']['_DesignObj'].D4[0]
        D4y = self._DesignParameter['DeMux1to4_2']['_DesignObj'].D4[1]

        iclk=self._DesignParameter['DeMux1to4_2']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclk
        iclkb=self._DesignParameter['DeMux1to4_2']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclkb
        CellXWidth=self._DesignParameter['DeMux1to4_2']['_DesignObj'].CellXWidth

        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D1x,DeMux1to4y-iclk-Dataoutspacing],[DeMux1to4x+CellXWidth,DeMux1to4y-iclk-Dataoutspacing]])
        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D2x,DeMux1to4y-iclk],[DeMux1to4x+CellXWidth,DeMux1to4y-iclk]])
        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D3x,DeMux1to4y-iclkb],[DeMux1to4x+CellXWidth,DeMux1to4y-iclkb]])
        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D4x,DeMux1to4y-D4y],[DeMux1to4x+CellXWidth,DeMux1to4y-D4y]])

        self._DesignParameter['_Met4_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D1x,DeMux1to4y-iclk-Dataoutspacing],[DeMux1to4x+D1x,DeMux1to4y-D1y]])
        self._DesignParameter['_Met4_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D2x,DeMux1to4y-iclk],[DeMux1to4x+D2x,DeMux1to4y-D2y]])
        self._DesignParameter['_Met4_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D3x,DeMux1to4y-iclkb],[DeMux1to4x+D3x,DeMux1to4y-D3y]])

        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D1x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y-iclk-Dataoutspacing])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D1x- tmpViaMet2Width / 2 + tmpMet2Width / 2,DeMux1to4y-D1y])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D2x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y-iclk])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D2x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y-D2y])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D3x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y-iclkb])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D3x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y-D3y])

        ## DeMux1to4_3 ##

        DeMux1to4x=self._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][0]
        DeMux1to4y=self._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][1]

        D1x=self._DesignParameter['DeMux1to4_3']['_DesignObj'].D1[0]
        D1y=self._DesignParameter['DeMux1to4_3']['_DesignObj'].D1[1]
        D2x = self._DesignParameter['DeMux1to4_3']['_DesignObj'].D2[0]
        D2y = self._DesignParameter['DeMux1to4_3']['_DesignObj'].D2[1]
        D3x = self._DesignParameter['DeMux1to4_3']['_DesignObj'].D3[0]
        D3y = self._DesignParameter['DeMux1to4_3']['_DesignObj'].D3[1]
        D4x = self._DesignParameter['DeMux1to4_3']['_DesignObj'].D4[0]
        D4y = self._DesignParameter['DeMux1to4_3']['_DesignObj'].D4[1]

        iclk=self._DesignParameter['DeMux1to4_3']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclk
        iclkb=self._DesignParameter['DeMux1to4_3']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclkb
        CellXWidth=self._DesignParameter['DeMux1to4_3']['_DesignObj'].CellXWidth

        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D1x,DeMux1to4y+iclk+Dataoutspacing],[DeMux1to4x+CellXWidth,DeMux1to4y+iclk+Dataoutspacing]])
        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D2x,DeMux1to4y+iclk],[DeMux1to4x+CellXWidth,DeMux1to4y+iclk]])
        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D3x,DeMux1to4y+iclkb],[DeMux1to4x+CellXWidth,DeMux1to4y+iclkb]])
        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D4x,DeMux1to4y+D4y],[DeMux1to4x+CellXWidth,DeMux1to4y+D4y]])

        self._DesignParameter['_Met4_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D1x,DeMux1to4y+iclk+Dataoutspacing],[DeMux1to4x+D1x,DeMux1to4y+D1y]])
        self._DesignParameter['_Met4_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D2x,DeMux1to4y+iclk],[DeMux1to4x+D2x,DeMux1to4y+D2y]])
        self._DesignParameter['_Met4_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D3x,DeMux1to4y+iclkb],[DeMux1to4x+D3x,DeMux1to4y+D3y]])

        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D1x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y+iclk+Dataoutspacing])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D1x- tmpViaMet2Width / 2 + tmpMet2Width / 2,DeMux1to4y+D1y])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D2x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y+iclk])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D2x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y+D2y])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D3x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y+iclkb])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D3x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y+D3y])


        ## DeMux1to4_4 ##
        DeMux1to4x=self._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][0]
        DeMux1to4y=self._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][1]

        D1x=self._DesignParameter['DeMux1to4_3']['_DesignObj'].D1[0]
        D1y=self._DesignParameter['DeMux1to4_3']['_DesignObj'].D1[1]
        D2x = self._DesignParameter['DeMux1to4_3']['_DesignObj'].D2[0]
        D2y = self._DesignParameter['DeMux1to4_3']['_DesignObj'].D2[1]
        D3x = self._DesignParameter['DeMux1to4_3']['_DesignObj'].D3[0]
        D3y = self._DesignParameter['DeMux1to4_3']['_DesignObj'].D3[1]
        D4x = self._DesignParameter['DeMux1to4_3']['_DesignObj'].D4[0]
        D4y = self._DesignParameter['DeMux1to4_3']['_DesignObj'].D4[1]

        iclk=self._DesignParameter['DeMux1to4_3']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclk
        iclkb=self._DesignParameter['DeMux1to4_3']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclkb
        CellXWidth=self._DesignParameter['DeMux1to4_3']['_DesignObj'].CellXWidth

        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D1x,DeMux1to4y-iclk-Dataoutspacing],[DeMux1to4x+CellXWidth,DeMux1to4y-iclk-Dataoutspacing]])
        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D2x,DeMux1to4y-iclk],[DeMux1to4x+CellXWidth,DeMux1to4y-iclk]])
        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D3x,DeMux1to4y-iclkb],[DeMux1to4x+CellXWidth,DeMux1to4y-iclkb]])
        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D4x,DeMux1to4y-D4y],[DeMux1to4x+CellXWidth,DeMux1to4y-D4y]])

        self._DesignParameter['_Met4_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D1x,DeMux1to4y-iclk-Dataoutspacing],[DeMux1to4x+D1x,DeMux1to4y-D1y]])
        self._DesignParameter['_Met4_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D2x,DeMux1to4y-iclk],[DeMux1to4x+D2x,DeMux1to4y-D2y]])
        self._DesignParameter['_Met4_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D3x,DeMux1to4y-iclkb],[DeMux1to4x+D3x,DeMux1to4y-D3y]])

        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D1x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y-iclk-Dataoutspacing])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D1x- tmpViaMet2Width / 2 + tmpMet2Width / 2,DeMux1to4y-D1y])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D2x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y-iclk])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D2x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y-D2y])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D3x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y-iclkb])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D3x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y-D3y])

        ## DeMux1to4_5 ##
        DeMux1to4x=self._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][0]
        DeMux1to4y=0

        D1x=self._DesignParameter['DeMux1to4_3']['_DesignObj'].D1[0]
        D1y=self._DesignParameter['DeMux1to4_3']['_DesignObj'].D1[1]
        D2x = self._DesignParameter['DeMux1to4_3']['_DesignObj'].D2[0]
        D2y = self._DesignParameter['DeMux1to4_3']['_DesignObj'].D2[1]
        D3x = self._DesignParameter['DeMux1to4_3']['_DesignObj'].D3[0]
        D3y = self._DesignParameter['DeMux1to4_3']['_DesignObj'].D3[1]
        D4x = self._DesignParameter['DeMux1to4_3']['_DesignObj'].D4[0]
        D4y = self._DesignParameter['DeMux1to4_3']['_DesignObj'].D4[1]

        iclk=self._DesignParameter['DeMux1to4_3']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclk
        iclkb=self._DesignParameter['DeMux1to4_3']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclkb
        CellXWidth=self._DesignParameter['DeMux1to4_3']['_DesignObj'].CellXWidth

        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D1x,DeMux1to4y-iclk-Dataoutspacing],[DeMux1to4x+CellXWidth,DeMux1to4y-iclk-Dataoutspacing]])
        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D2x,DeMux1to4y-iclk],[DeMux1to4x+CellXWidth,DeMux1to4y-iclk]])
        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D3x,DeMux1to4y-iclkb],[DeMux1to4x+CellXWidth,DeMux1to4y-iclkb]])
        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D4x,DeMux1to4y-D4y],[DeMux1to4x+CellXWidth,DeMux1to4y-D4y]])

        self._DesignParameter['_Met4_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D1x,DeMux1to4y-iclk-Dataoutspacing],[DeMux1to4x+D1x,DeMux1to4y-D1y]])
        self._DesignParameter['_Met4_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D2x,DeMux1to4y-iclk],[DeMux1to4x+D2x,DeMux1to4y-D2y]])
        self._DesignParameter['_Met4_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D3x,DeMux1to4y-iclkb],[DeMux1to4x+D3x,DeMux1to4y-D3y]])

        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D1x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y-iclk-Dataoutspacing])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D1x- tmpViaMet2Width / 2 + tmpMet2Width / 2,DeMux1to4y-D1y])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D2x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y-iclk])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D2x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y-D2y])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D3x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y-iclkb])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D3x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y-D3y])


        ## DeMux1to4_6 ##
        DeMux1to4x=self._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][0]
        DeMux1to4y=self._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][1]

        D1x=self._DesignParameter['DeMux1to4_6']['_DesignObj'].D1[0]
        D1y=self._DesignParameter['DeMux1to4_6']['_DesignObj'].D1[1]
        D2x = self._DesignParameter['DeMux1to4_6']['_DesignObj'].D2[0]
        D2y = self._DesignParameter['DeMux1to4_6']['_DesignObj'].D2[1]
        D3x = self._DesignParameter['DeMux1to4_6']['_DesignObj'].D3[0]
        D3y = self._DesignParameter['DeMux1to4_6']['_DesignObj'].D3[1]
        D4x = self._DesignParameter['DeMux1to4_6']['_DesignObj'].D4[0]
        D4y = self._DesignParameter['DeMux1to4_6']['_DesignObj'].D4[1]

        iclk=self._DesignParameter['DeMux1to4_6']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclk
        iclkb=self._DesignParameter['DeMux1to4_6']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclkb
        CellXWidth=self._DesignParameter['DeMux1to4_6']['_DesignObj'].CellXWidth

        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D1x,DeMux1to4y+iclk+Dataoutspacing],[DeMux1to4x+CellXWidth,DeMux1to4y+iclk+Dataoutspacing]])
        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D2x,DeMux1to4y+iclk],[DeMux1to4x+CellXWidth,DeMux1to4y+iclk]])
        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D3x,DeMux1to4y+iclkb],[DeMux1to4x+CellXWidth,DeMux1to4y+iclkb]])
        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D4x,DeMux1to4y+D4y],[DeMux1to4x+CellXWidth,DeMux1to4y+D4y]])

        self._DesignParameter['_Met4_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D1x,DeMux1to4y+iclk+Dataoutspacing],[DeMux1to4x+D1x,DeMux1to4y+D1y]])
        self._DesignParameter['_Met4_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D2x,DeMux1to4y+iclk],[DeMux1to4x+D2x,DeMux1to4y+D2y]])
        self._DesignParameter['_Met4_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D3x,DeMux1to4y+iclkb],[DeMux1to4x+D3x,DeMux1to4y+D3y]])

        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D1x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y+iclk+Dataoutspacing])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D1x- tmpViaMet2Width / 2 + tmpMet2Width / 2,DeMux1to4y+D1y])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D2x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y+iclk])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D2x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y+D2y])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D3x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y+iclkb])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D3x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y+D3y])

        ## DeMux1to4_7 ##
        DeMux1to4x=self._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][0]
        DeMux1to4y=self._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][1]

        D1x=self._DesignParameter['DeMux1to4_6']['_DesignObj'].D1[0]
        D1y=self._DesignParameter['DeMux1to4_6']['_DesignObj'].D1[1]
        D2x = self._DesignParameter['DeMux1to4_6']['_DesignObj'].D2[0]
        D2y = self._DesignParameter['DeMux1to4_6']['_DesignObj'].D2[1]
        D3x = self._DesignParameter['DeMux1to4_6']['_DesignObj'].D3[0]
        D3y = self._DesignParameter['DeMux1to4_6']['_DesignObj'].D3[1]
        D4x = self._DesignParameter['DeMux1to4_6']['_DesignObj'].D4[0]
        D4y = self._DesignParameter['DeMux1to4_6']['_DesignObj'].D4[1]

        iclk=self._DesignParameter['DeMux1to4_6']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclk
        iclkb=self._DesignParameter['DeMux1to4_6']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclkb
        CellXWidth=self._DesignParameter['DeMux1to4_6']['_DesignObj'].CellXWidth

        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D1x,DeMux1to4y-iclk-Dataoutspacing],[DeMux1to4x+CellXWidth,DeMux1to4y-iclk-Dataoutspacing]])
        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D2x,DeMux1to4y-iclk],[DeMux1to4x+CellXWidth,DeMux1to4y-iclk]])
        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D3x,DeMux1to4y-iclkb],[DeMux1to4x+CellXWidth,DeMux1to4y-iclkb]])
        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D4x,DeMux1to4y-D4y],[DeMux1to4x+CellXWidth,DeMux1to4y-D4y]])

        self._DesignParameter['_Met4_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D1x,DeMux1to4y-iclk-Dataoutspacing],[DeMux1to4x+D1x,DeMux1to4y-D1y]])
        self._DesignParameter['_Met4_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D2x,DeMux1to4y-iclk],[DeMux1to4x+D2x,DeMux1to4y-D2y]])
        self._DesignParameter['_Met4_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D3x,DeMux1to4y-iclkb],[DeMux1to4x+D3x,DeMux1to4y-D3y]])

        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D1x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y-iclk-Dataoutspacing])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D1x- tmpViaMet2Width / 2 + tmpMet2Width / 2,DeMux1to4y-D1y])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D2x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y-iclk])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D2x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y-D2y])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D3x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y-iclkb])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D3x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y-D3y])

        ## DeMux1to4_8 ##
        DeMux1to4x=self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0]
        DeMux1to4y=self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][1]

        D1x=self._DesignParameter['DeMux1to4_8']['_DesignObj'].D1[0]
        D1y=self._DesignParameter['DeMux1to4_8']['_DesignObj'].D1[1]
        D2x = self._DesignParameter['DeMux1to4_8']['_DesignObj'].D2[0]
        D2y = self._DesignParameter['DeMux1to4_8']['_DesignObj'].D2[1]
        D3x = self._DesignParameter['DeMux1to4_8']['_DesignObj'].D3[0]
        D3y = self._DesignParameter['DeMux1to4_8']['_DesignObj'].D3[1]
        D4x = self._DesignParameter['DeMux1to4_8']['_DesignObj'].D4[0]
        D4y = self._DesignParameter['DeMux1to4_8']['_DesignObj'].D4[1]

        iclk=self._DesignParameter['DeMux1to4_8']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclk
        iclkb=self._DesignParameter['DeMux1to4_8']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclkb
        CellXWidth=self._DesignParameter['DeMux1to4_8']['_DesignObj'].CellXWidth

        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D1x,DeMux1to4y+iclk+Dataoutspacing],[DeMux1to4x+CellXWidth,DeMux1to4y+iclk+Dataoutspacing]])
        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D2x,DeMux1to4y+iclk],[DeMux1to4x+CellXWidth,DeMux1to4y+iclk]])
        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D3x,DeMux1to4y+iclkb],[DeMux1to4x+CellXWidth,DeMux1to4y+iclkb]])
        self._DesignParameter['_Met3_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D4x,DeMux1to4y+D4y],[DeMux1to4x+CellXWidth,DeMux1to4y+D4y]])

        self._DesignParameter['_Met4_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D1x,DeMux1to4y+iclk+Dataoutspacing],[DeMux1to4x+D1x,DeMux1to4y+D1y]])
        self._DesignParameter['_Met4_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D2x,DeMux1to4y+iclk],[DeMux1to4x+D2x,DeMux1to4y+D2y]])
        self._DesignParameter['_Met4_data3toend']['_XYCoordinates'].append([[DeMux1to4x+D3x,DeMux1to4y+iclkb],[DeMux1to4x+D3x,DeMux1to4y+D3y]])

        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D1x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y+iclk+Dataoutspacing])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D1x- tmpViaMet2Width / 2 + tmpMet2Width / 2,DeMux1to4y+D1y])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D2x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y+iclk])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D2x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y+D2y])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D3x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y+iclkb])
        self._DesignParameter['_ViaMet32Met4_data3toend']['_XYCoordinates'].append([DeMux1to4x+D3x+ tmpViaMet2Width / 2 - tmpMet2Width / 2,DeMux1to4y+D3y])

        ####################### 3rd stage data ouput to next circuit end!!!!!!!!




        ####################### 1st to 2nd stage clk and clkb  ##########################

        self._DesignParameter['_Met3_clk1st'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met4_clk1st'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _Width=tmpMet2Width
        )

        self._DesignParameter['_Met3_clk1st_via'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met3_clk1st_via2'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=tmpMet2Width+16
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

        # self._DesignParameter['_ViaMet32Met4_clk1st_3'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='_ViaMet32Met4_clk1st_3In{}'.format(_Name)))[0]
        # self._DesignParameter['_ViaMet32Met4_clk1st_3']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=1))
        # #self._DesignParameter['_ViaMet32Met4_clk1st_3']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] = tmpViaminWidth
        # self._DesignParameter['_ViaMet32Met4_clk1st_3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = tmpViaminWidth
        #

        self._DesignParameter['_ViaMet32Met4_clk1st']['_XYCoordinates']=[[self.getXY('Clk_Driver_1','DFFQb1','_qpin')[-1][0],self.getXY('Clk_Driver_1','DFFQb1','_qpin')[-1][1]]]
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'] =[[self.getXY('Clk_Driver_1','DFFQb1','_qbpin')[0][0]-tmpViaminWidth/2+tmpMet2Width/2,self._DesignParameter['Clk_Driver_1']['_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclk]]

        self._DesignParameter['_ViaMet32Met4_clk1st']['_XYCoordinates'].append([self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1][0],self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1][1]])
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'].append([self.getXY('Clk_Driver_1','DFFQb2','_qbpin')[0][0]-tmpViaminWidth/2+tmpMet2Width/2,self._DesignParameter['Clk_Driver_1']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclk])
        ### To fix minimum area M3 drc error
        self._DesignParameter['_Met3_clk1st_via']['_XYCoordinates']=[[[self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1][0],self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1][1]-tmpViaMet2Width/2],[self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1][0],self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1][1]+tmpViaminWidth-tmpViaMet2Width/2]],\
                                                                     [[self.getXY('Clk_Driver_2','DFFQb2','_qpin')[-1][0],self.getXY('Clk_Driver_2','DFFQb2','_qpin')[-1][1]-tmpViaMet2Width/2],[self.getXY('Clk_Driver_2','DFFQb2','_qpin')[-1][0],self.getXY('Clk_Driver_2','DFFQb2','_qpin')[-1][1]+tmpViaminWidth-tmpViaMet2Width/2]],\
                                                                     [[self.getXY('Clk_Driver_2','DFFQb1','_qpin')[-1][0],self.getXY('Clk_Driver_2','DFFQb1','_qpin')[-1][1]-tmpViaMet2Width/2],[self.getXY('Clk_Driver_2','DFFQb1','_qpin')[-1][0],self.getXY('Clk_Driver_2','DFFQb1','_qpin')[-1][1]+tmpViaminWidth-tmpViaMet2Width/2]]]
        self._DesignParameter['_Met3_clk1st_via2']['_XYCoordinates']=[[[self.getXY('Clk_Driver_2','DFFQb2','_qpin')[-1][0],self.getXY('Clk_Driver_2','DFFQb2','_qpin')[-1][1]-tmpViaMet2Width/2],[self.getXY('Clk_Driver_2','DFFQb2','_qpin')[-1][0],self.getXY('Clk_Driver_2','DFFQb2','_qpin')[-1][1]+tmpViaminWidth-tmpViaMet2Width/2]],\
                                                                     [[self.getXY('Clk_Driver_2','DFFQb1','_qpin')[-1][0],self.getXY('Clk_Driver_2','DFFQb1','_qpin')[-1][1]-tmpViaMet2Width/2],[self.getXY('Clk_Driver_2','DFFQb1','_qpin')[-1][0],self.getXY('Clk_Driver_2','DFFQb1','_qpin')[-1][1]+tmpViaminWidth-tmpViaMet2Width/2]]]

        # self._DesignParameter['_ViaMet32Met4_clk1st_3']['_XYCoordinates']=[[self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1][0],self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1][1]+tmpMet2Width/2],\
        #                                                                    [self.getXY('Clk_Driver_2','DFFQb2','_qpin')[-1][0],self.getXY('Clk_Driver_2','DFFQb2','_qpin')[-1][1]+tmpMet2Width/2],\
        #                                                                    [self.getXY('Clk_Driver_2','DFFQb1','_qpin')[-1][0],self.getXY('Clk_Driver_2','DFFQb1','_qpin')[-1][1]+tmpMet2Width/2]]

        #### DeMux1to2_1
        self._DesignParameter['_Met4_clk1st']['_XYCoordinates'] = [[self.getXY('Clk_Driver_1','DFFQb1','_qpin')[-1],\
                                                                       [self.getXY('Clk_Driver_1','DFFQb1','_qpin')[-1][0],CellHeight+tmpDSspace]]]#q

        self._DesignParameter['_Met4_clk1st']['_XYCoordinates'].append([[self.getXY('Clk_Driver_1','DFFQb1','_qbpin')[0][0],self._DesignParameter['Clk_Driver_1']['_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclk],\
                                                                       [self.getXY('Clk_Driver_1','DFFQb1','_qbpin')[0][0],CellHeight-tmpDSspace]])#qb

        self._DesignParameter['_Met4_clk1st']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to2_1']['_DesignObj'].clk[0],self.getXY('DeMux1to2_1')[0][1]+self._DesignParameter['DeMux1to2_1']['_DesignObj'].clk[1]],\
                                                                       [self._DesignParameter['DeMux1to2_1']['_DesignObj'].clk[0],CellHeight+tmpDSspace]])#q

        self._DesignParameter['_Met4_clk1st']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to2_1']['_DesignObj'].clkb[0],self.getXY('DeMux1to2_1')[0][1]+self._DesignParameter['DeMux1to2_1']['_DesignObj'].clkb[1]],\
                                                                       [self._DesignParameter['DeMux1to2_1']['_DesignObj'].clkb[0],CellHeight-tmpDSspace]])#qb

        self._DesignParameter['_Met3_clk1st']['_XYCoordinates'] = [[[self._DesignParameter['DeMux1to2_1']['_DesignObj'].clk[0],CellHeight+tmpDSspace],\
                                                                       [self.getXY('Clk_Driver_1','DFFQb1','_qpin')[-1][0],CellHeight+tmpDSspace]]]#q

        self._DesignParameter['_Met3_clk1st']['_XYCoordinates'].append([[self.getXY('Clk_Driver_1','DFFQb1','_qbpin')[0][0],CellHeight-tmpDSspace],\
                                                                        [self._DesignParameter['DeMux1to2_1']['_DesignObj'].clkb[0],CellHeight-tmpDSspace]])#qb
        #Demux1to2_1 via
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to2_1']['_DesignObj'].clk[0]-tmpViaminWidth/2+tmpMet2Width / 2,self.getXY('DeMux1to2_1')[0][1]+self._DesignParameter['DeMux1to2_1']['_DesignObj'].clk[1]])
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to2_1']['_DesignObj'].clkb[0]-tmpViaminWidth/2+tmpMet2Width / 2,self.getXY('DeMux1to2_1')[0][1]+self._DesignParameter['DeMux1to2_1']['_DesignObj'].clkb[1]])
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to2_1']['_DesignObj'].clk[0]+tmpViaminWidth/2-tmpMet2Width / 2,CellHeight+tmpDSspace])
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'].append([self.getXY('Clk_Driver_1','DFFQb1','_qpin')[-1][0]-tmpViaminWidth/2+tmpMet2Width / 2,CellHeight+tmpDSspace])
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'].append([self.getXY('Clk_Driver_1','DFFQb1','_qbpin')[0][0]-tmpViaminWidth/2+tmpMet2Width / 2,CellHeight-tmpDSspace])
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to2_1']['_DesignObj'].clkb[0]+tmpViaminWidth/2-tmpMet2Width / 2,CellHeight-tmpDSspace])



        ###DeMux1to2_5
        self._DesignParameter['_Met4_clk1st']['_XYCoordinates'].append([self.getXY('Clk_Driver_1','DFFQb1','_qpin')[-1],\
                                                                       [self.getXY('Clk_Driver_1','DFFQb1','_qpin')[-1][0],-tmpDSspace]])#q

        self._DesignParameter['_Met4_clk1st']['_XYCoordinates'].append([[self.getXY('Clk_Driver_1','DFFQb1','_qbpin')[0][0],self._DesignParameter['Clk_Driver_1']['_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclk],\
                                                                       [self.getXY('Clk_Driver_1','DFFQb1','_qbpin')[0][0],+tmpDSspace]])#qb

        self._DesignParameter['_Met4_clk1st']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to2_5']['_DesignObj'].clk[0],self.getXY('DeMux1to2_5')[0][1]+self._DesignParameter['DeMux1to2_5']['_DesignObj'].clk[1]],\
                                                                       [self._DesignParameter['DeMux1to2_5']['_DesignObj'].clk[0],-tmpDSspace]])#q

        self._DesignParameter['_Met4_clk1st']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to2_5']['_DesignObj'].clkb[0],self.getXY('DeMux1to2_5')[0][1]+self._DesignParameter['DeMux1to2_5']['_DesignObj'].clkb[1]],\
                                                                       [self._DesignParameter['DeMux1to2_5']['_DesignObj'].clkb[0],+tmpDSspace]])#qb

        self._DesignParameter['_Met3_clk1st']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to2_5']['_DesignObj'].clk[0],-tmpDSspace],\
                                                                       [self.getXY('Clk_Driver_1','DFFQb1','_qpin')[-1][0],-tmpDSspace]])#q

        self._DesignParameter['_Met3_clk1st']['_XYCoordinates'].append([[self.getXY('Clk_Driver_1','DFFQb1','_qbpin')[0][0],+tmpDSspace],\
                                                                        [self._DesignParameter['DeMux1to2_5']['_DesignObj'].clkb[0],+tmpDSspace]])#qb
        #Demux1to2_5 via
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to2_5']['_DesignObj'].clk[0]-tmpViaminWidth/2+tmpMet2Width / 2,self.getXY('DeMux1to2_5')[0][1]+self._DesignParameter['DeMux1to2_5']['_DesignObj'].clk[1]])
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to2_5']['_DesignObj'].clkb[0]-tmpViaminWidth/2+tmpMet2Width / 2,self.getXY('DeMux1to2_5')[0][1]+self._DesignParameter['DeMux1to2_5']['_DesignObj'].clkb[1]])
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to2_5']['_DesignObj'].clk[0]+tmpViaminWidth/2-tmpMet2Width / 2,-tmpDSspace])
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'].append([self.getXY('Clk_Driver_1','DFFQb1','_qpin')[-1][0]-tmpViaminWidth/2+tmpMet2Width / 2,-tmpDSspace])
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'].append([self.getXY('Clk_Driver_1','DFFQb1','_qbpin')[0][0]-tmpViaminWidth/2+tmpMet2Width / 2,tmpDSspace])
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to2_5']['_DesignObj'].clkb[0]+tmpViaminWidth/2-tmpMet2Width / 2,tmpDSspace])



        ###DeMux1to2_2
        self._DesignParameter['_Met4_clk1st']['_XYCoordinates'].append([self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1],\
                                                                       [self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1][0],CellHeight]])#q

        self._DesignParameter['_Met4_clk1st']['_XYCoordinates'].append([[self.getXY('Clk_Driver_1','DFFQb2','_qbpin')[0][0],self._DesignParameter['Clk_Driver_1']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclk],\
                                                                       [self.getXY('Clk_Driver_1','DFFQb2','_qbpin')[0][0],CellHeight-2*tmpDSspace]])#qb

        self._DesignParameter['_Met4_clk1st']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to2_2']['_DesignObj'].clk[0]-tmpDSspace,self.getXY('DeMux1to2_2')[0][1]-self._DesignParameter['DeMux1to2_2']['_DesignObj'].clk[1]],\
                                                                       [self._DesignParameter['DeMux1to2_2']['_DesignObj'].clk[0]-tmpDSspace,CellHeight]])#q

        self._DesignParameter['_Met4_clk1st']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to2_2']['_DesignObj'].clkb[0]-tmpDSspace,self.getXY('DeMux1to2_2')[0][1]-self._DesignParameter['DeMux1to2_2']['_DesignObj'].clkb[1]],\
                                                                       [self._DesignParameter['DeMux1to2_2']['_DesignObj'].clkb[0]-tmpDSspace,CellHeight-2*tmpDSspace]])#qb

        self._DesignParameter['_Met3_clk1st']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to2_2']['_DesignObj'].clk[0]-tmpDSspace,CellHeight],\
                                                                       [self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1][0],CellHeight]])#q

        self._DesignParameter['_Met3_clk1st']['_XYCoordinates'].append([[self.getXY('Clk_Driver_1','DFFQb2','_qbpin')[0][0],CellHeight-2*tmpDSspace],\
                                                                        [self._DesignParameter['DeMux1to2_2']['_DesignObj'].clkb[0]-tmpDSspace,CellHeight-2*tmpDSspace]])#qb
        #Demux1to2_2 via
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to2_2']['_DesignObj'].clk[0]-tmpViaminWidth/2+tmpMet2Width / 2-tmpDSspace,self.getXY('DeMux1to2_2')[0][1]-self._DesignParameter['DeMux1to2_2']['_DesignObj'].clk[1]])
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to2_2']['_DesignObj'].clkb[0]-tmpViaminWidth/2+tmpMet2Width / 2-tmpDSspace,self.getXY('DeMux1to2_2')[0][1]-self._DesignParameter['DeMux1to2_2']['_DesignObj'].clkb[1]])
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to2_2']['_DesignObj'].clk[0]+tmpViaminWidth/2-tmpMet2Width / 2-tmpDSspace,CellHeight])
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'].append([self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1][0]-tmpViaminWidth/2+tmpMet2Width / 2,CellHeight])
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'].append([self.getXY('Clk_Driver_1','DFFQb2','_qbpin')[0][0]-tmpViaminWidth/2+tmpMet2Width / 2,CellHeight-2*tmpDSspace])
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to2_2']['_DesignObj'].clkb[0]+tmpViaminWidth/2-tmpMet2Width / 2-tmpDSspace,CellHeight-2*tmpDSspace])


        ###DeMux1to2_4
        self._DesignParameter['_Met4_clk1st']['_XYCoordinates'].append([self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1],\
                                                                       [self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1][0],0]])#q

        self._DesignParameter['_Met4_clk1st']['_XYCoordinates'].append([[self.getXY('Clk_Driver_1','DFFQb2','_qbpin')[0][0],self._DesignParameter['Clk_Driver_1']['_DesignObj']._DesignParameter['DFFQb2']['_DesignObj'].iclk],\
                                                                       [self.getXY('Clk_Driver_1','DFFQb2','_qbpin')[0][0],2*tmpDSspace]])#qb

        self._DesignParameter['_Met4_clk1st']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to2_4']['_DesignObj'].clk[0]-tmpDSspace,self.getXY('DeMux1to2_4')[0][1]-self._DesignParameter['DeMux1to2_4']['_DesignObj'].clk[1]],\
                                                                       [self._DesignParameter['DeMux1to2_4']['_DesignObj'].clk[0]-tmpDSspace,0]])#q

        self._DesignParameter['_Met4_clk1st']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to2_4']['_DesignObj'].clkb[0]-tmpDSspace,self.getXY('DeMux1to2_4')[0][1]-self._DesignParameter['DeMux1to2_4']['_DesignObj'].clkb[1]],\
                                                                       [self._DesignParameter['DeMux1to2_4']['_DesignObj'].clkb[0]-tmpDSspace,2*tmpDSspace]])#qb

        self._DesignParameter['_Met3_clk1st']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to2_4']['_DesignObj'].clk[0]-tmpDSspace,0],\
                                                                       [self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1][0],0]])#q

        self._DesignParameter['_Met3_clk1st']['_XYCoordinates'].append([[self.getXY('Clk_Driver_1','DFFQb2','_qbpin')[0][0],2*tmpDSspace],\
                                                                        [self._DesignParameter['DeMux1to2_4']['_DesignObj'].clkb[0]-tmpDSspace,2*tmpDSspace]])#qb
        #Demux1to2_4 via
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to2_4']['_DesignObj'].clk[0]-tmpViaminWidth/2+tmpMet2Width / 2-tmpDSspace,self.getXY('DeMux1to2_4')[0][1]-self._DesignParameter['DeMux1to2_4']['_DesignObj'].clk[1]])
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to2_4']['_DesignObj'].clkb[0]-tmpViaminWidth/2+tmpMet2Width / 2-tmpDSspace,self.getXY('DeMux1to2_4')[0][1]-self._DesignParameter['DeMux1to2_4']['_DesignObj'].clkb[1]])
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to2_4']['_DesignObj'].clk[0]+tmpViaminWidth/2-tmpMet2Width / 2-tmpDSspace,0])
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'].append([self.getXY('Clk_Driver_1','DFFQb2','_qpin')[-1][0]-tmpViaminWidth/2+tmpMet2Width / 2,0])
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'].append([self.getXY('Clk_Driver_1','DFFQb2','_qbpin')[0][0]-tmpViaminWidth/2+tmpMet2Width / 2,2*tmpDSspace])
        self._DesignParameter['_ViaMet32Met4_clk1st_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to2_4']['_DesignObj'].clkb[0]+tmpViaminWidth/2-tmpMet2Width / 2-tmpDSspace,2*tmpDSspace])



        ########### 1st to 2nd stage clk and clkb end!!!!



        ####################### 2nd to 3rd stage clk and clkb  ##########################

        self._DesignParameter['_Met3_clk2nd'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met4_clk2nd'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _Width=tmpMet2Width
        )

        self._DesignParameter['_ViaMet32Met4_clk2nd'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='_ViaMet32Met4_clk2ndIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4_clk2nd']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=1))
        self._DesignParameter['_ViaMet32Met4_clk2nd']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet32Met4_clk2nd']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet32Met4_clk2nd']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = tmpVia1YWidth

        self._DesignParameter['_ViaMet32Met4_clk2nd_2'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='_ViaMet32Met4_clk2nd_2In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=1))
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_DesignObj']._DesignParameter['_COLayer']['_XWidth'] = tmpVia1YWidth

        self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates']=[[self.getXY('Clk_Driver_2','DFFQb1','_qpin')[-1][0],self.getXY('Clk_Driver_2','DFFQb1','_qpin')[-1][1]]]
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'] =[[self.getXY('Clk_Driver_2','DFFQb1','_qbpin')[0][0]-tmpViaminWidth/2+tmpMet2Width/2,self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb1']['_DesignObj'].iclk]]

        a=self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0]
        b=self.getXY('Clk_Driver_2', 'DFFQb2', '_qbpin')[0][0] + 12 * tmpDSspace

        ######## To fix Routing error
        if a>b or a<(b-10* tmpDSspace):  ##Clk f16 90 and f16 90b signal
            #### clk driver to demux
            # lower
            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'] = [
                [self.getXY('Clk_Driver_2', 'DFFQb1', '_qpin')[-1], \
                 [self.getXY('Clk_Driver_2', 'DFFQb1', '_qpin')[-1][0], -tmpDSspace]], \
                [[self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0] +
                  self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0] + 4 * tmpDSspace, -tmpDSspace],
                 [self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0] +
                  self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0] + 4 * tmpDSspace,
                  -2 * CellHeight - tmpDSspace]]]  # f16

            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self.getXY('Clk_Driver_2', 'DFFQb1',
                                                                                        '_qbpin')[0][0],
                                                                             self._DesignParameter['Clk_Driver_2'][
                                                                                 '_DesignObj']._DesignParameter[
                                                                                 'DFFQb1']['_DesignObj'].iclk], \
                                                                            [self.getXY('Clk_Driver_2', 'DFFQb1',
                                                                                        '_qbpin')[0][0],
                                                                             +tmpDSspace]])  # f16b
            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clkb[0] + 3 * tmpDSspace,
                                                                             tmpDSspace], \
                                                                            [self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clkb[0] + 3 * tmpDSspace,
                                                                             -2 * CellHeight + tmpDSspace]])  # f16b

            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clk90[2][
                                                                                 0] + 4 * tmpDSspace, 0], \
                                                                            [self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clk90[2][
                                                                                 0] + 4 * tmpDSspace,
                                                                             -2 * CellHeight]])  # f16_90

            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clk90[2][
                                                                                 0] + 3 * tmpDSspace, 2 * tmpDSspace], \
                                                                            [self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clk90[2][
                                                                                 0] + 3 * tmpDSspace,
                                                                             -2 * CellHeight + 2 * tmpDSspace]])  # f16_90b

            # added
            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self.getXY('Clk_Driver_2', 'DFFQb2',
                                                                                        '_qbpin')[0][
                                                                                 0] + 12 * tmpDSspace,
                                                                             self._DesignParameter['Clk_Driver_2'][
                                                                                 '_DesignObj']._DesignParameter[
                                                                                 'DFFQb2']['_DesignObj'].iclkb], \
                                                                            [self.getXY('Clk_Driver_2', 'DFFQb2',
                                                                                        '_qbpin')[0][
                                                                                 0] + 12 * tmpDSspace, 0]])  # f16_90

            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self.getXY('Clk_Driver_2', 'DFFQb2',
                                                                                        '_qbpin')[0][
                                                                                 0] + 10 * tmpDSspace,
                                                                             self._DesignParameter['Clk_Driver_2'][
                                                                                 '_DesignObj']._DesignParameter[
                                                                                 'DFFQb2']['_DesignObj'].iclk], \
                                                                            [self.getXY('Clk_Driver_2', 'DFFQb2',
                                                                                        '_qbpin')[0][
                                                                                 0] + 10 * tmpDSspace,
                                                                             2 * tmpDSspace]])  # f16_90b

            # upper
            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb1', '_qpin')[-1], \
                 [self.getXY('Clk_Driver_2', 'DFFQb1', '_qpin')[-1][0], 1 * CellHeight + tmpDSspace]])  # f16
            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clkb[0] + 4 * tmpDSspace,
                                                                             1 * CellHeight + tmpDSspace], \
                                                                            [self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clkb[0] + 4 * tmpDSspace,
                                                                             3 * CellHeight + tmpDSspace]])  # f16

            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self.getXY('Clk_Driver_2', 'DFFQb1',
                                                                                        '_qbpin')[0][0],
                                                                             self._DesignParameter['Clk_Driver_2'][
                                                                                 '_DesignObj']._DesignParameter[
                                                                                 'DFFQb1']['_DesignObj'].iclk], \
                                                                            [self.getXY('Clk_Driver_2', 'DFFQb1',
                                                                                        '_qbpin')[0][0],
                                                                             1 * CellHeight - tmpDSspace]])  # f16b
            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clkb[0] + 3 * tmpDSspace,
                                                                             3 * CellHeight - tmpDSspace], \
                                                                            [self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clkb[0] + 3 * tmpDSspace,
                                                                             1 * CellHeight - tmpDSspace]])  # f16b

            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clk90[2][
                                                                                 0] + 4 * tmpDSspace, 1 * CellHeight], \
                                                                            [self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clk90[2][
                                                                                 0] + 4 * tmpDSspace,
                                                                             3 * CellHeight]])  # f16_90

            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clk90[2][
                                                                                 0] + 3 * tmpDSspace,
                                                                             1 * CellHeight - 2 * tmpDSspace], \
                                                                            [self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clk90[2][
                                                                                 0] + 3 * tmpDSspace,
                                                                             3 * CellHeight - 2 * tmpDSspace]])  # f16_90b

            # added
            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self.getXY('Clk_Driver_2', 'DFFQb2',
                                                                                        '_qbpin')[0][
                                                                                 0] + 12 * tmpDSspace,
                                                                             self._DesignParameter['Clk_Driver_2'][
                                                                                 '_DesignObj']._DesignParameter[
                                                                                 'DFFQb2']['_DesignObj'].iclkb], \
                                                                            [self.getXY('Clk_Driver_2', 'DFFQb2',
                                                                                        '_qbpin')[0][
                                                                                 0] + 12 * tmpDSspace,
                                                                             1 * CellHeight]])  # f16_90

            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self.getXY('Clk_Driver_2', 'DFFQb2',
                                                                                        '_qbpin')[0][
                                                                                 0] + 10 * tmpDSspace,
                                                                             self._DesignParameter['Clk_Driver_2'][
                                                                                 '_DesignObj']._DesignParameter[
                                                                                 'DFFQb2']['_DesignObj'].iclk], \
                                                                            [self.getXY('Clk_Driver_2', 'DFFQb2',
                                                                                        '_qbpin')[0][
                                                                                 0] + 10 * tmpDSspace,
                                                                             1 * CellHeight - 2 * tmpDSspace]])  # f16_90b
            ## via added for added routing (f16_90 f16_90b)

            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2', '_qbpin')[0][0] + 12 * tmpDSspace,
                 self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb2'][
                     '_DesignObj'].iclkb])  # f16_90
            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2', '_qbpin')[0][0] + 10 * tmpDSspace,
                 self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb2'][
                     '_DesignObj'].iclk])  # f16_90b

            # upper
            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append([self._DesignParameter[
                                                                                        'DeMux1to4_1'][
                                                                                        '_XYCoordinates'][0][0] +
                                                                                    self._DesignParameter[
                                                                                        'DeMux1to4_1'][
                                                                                        '_DesignObj'].clk90[2][
                                                                                        0] + 4 * tmpDSspace,
                                                                                    1 * CellHeight])  # f16_90
            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append([self._DesignParameter[
                                                                                        'DeMux1to4_1'][
                                                                                        '_XYCoordinates'][0][0] +
                                                                                    self._DesignParameter[
                                                                                        'DeMux1to4_1'][
                                                                                        '_DesignObj'].clk90[2][
                                                                                        0] + 3 * tmpDSspace,
                                                                                    1 * CellHeight - 2 * tmpDSspace])  # f16_90b
            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2', '_qbpin')[0][0] + 12 * tmpDSspace, 1 * CellHeight])  # f16_90
            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2', '_qbpin')[0][0] + 10 * tmpDSspace,
                 1 * CellHeight - 2 * tmpDSspace])  # f16_90b

            # lower
            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append([self._DesignParameter[
                                                                                        'DeMux1to4_1'][
                                                                                        '_XYCoordinates'][0][0] +
                                                                                    self._DesignParameter[
                                                                                        'DeMux1to4_1'][
                                                                                        '_DesignObj'].clk90[2][
                                                                                        0] + 4 * tmpDSspace, 0])
            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append([self._DesignParameter[
                                                                                        'DeMux1to4_1'][
                                                                                        '_XYCoordinates'][0][0] +
                                                                                    self._DesignParameter[
                                                                                        'DeMux1to4_1'][
                                                                                        '_DesignObj'].clk90[2][
                                                                                        0] + 3 * tmpDSspace,
                                                                                    2 * tmpDSspace])
            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2', '_qbpin')[0][0] + 12 * tmpDSspace, 0])  # f16_90
            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2', '_qbpin')[0][0] + 10 * tmpDSspace, +2 * tmpDSspace])  # f16_90b

            ### rotue revise added met3
            # Qb2 stage met3
            self._DesignParameter['_Met3_clk1st_via']['_XYCoordinates'].append([[self.getXY('Clk_Driver_2', 'DFFQb2',
                                                                                            '_qbpin')[0][
                                                                                     0] + 12 * tmpDSspace,
                                                                                 self._DesignParameter['Clk_Driver_2'][
                                                                                     '_DesignObj']._DesignParameter[
                                                                                     'DFFQb2']['_DesignObj'].iclkb], \
                                                                                [self.getXY('Clk_Driver_2', 'DFFQb2',
                                                                                            '_qpin')[-1][0],
                                                                                 self._DesignParameter['Clk_Driver_2'][
                                                                                     '_DesignObj']._DesignParameter[
                                                                                     'DFFQb2']['_DesignObj'].iclkb]])
            self._DesignParameter['_Met3_clk1st_via']['_XYCoordinates'].append([[self.getXY('Clk_Driver_2', 'DFFQb2',
                                                                                            '_qbpin')[0][
                                                                                     0] + 10 * tmpDSspace,
                                                                                 self._DesignParameter['Clk_Driver_2'][
                                                                                     '_DesignObj']._DesignParameter[
                                                                                     'DFFQb2']['_DesignObj'].iclk], \
                                                                                [self.getXY('Clk_Driver_2', 'DFFQb2',
                                                                                            '_qbpin')[0][0],
                                                                                 self._DesignParameter['Clk_Driver_2'][
                                                                                     '_DesignObj']._DesignParameter[
                                                                                     'DFFQb2']['_DesignObj'].iclk]])
            # upper
            self._DesignParameter['_Met3_clk1st_via']['_XYCoordinates'].append(
                [[self.getXY('Clk_Driver_2', 'DFFQb2', '_qbpin')[0][0] + 12 * tmpDSspace, 1 * CellHeight], \
                 [self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0] +
                  self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0] + 4 * tmpDSspace, 1 * CellHeight]])
            self._DesignParameter['_Met3_clk1st_via']['_XYCoordinates'].append([[self.getXY('Clk_Driver_2', 'DFFQb2',
                                                                                            '_qbpin')[0][
                                                                                     0] + 10 * tmpDSspace,
                                                                                 1 * CellHeight - 2 * tmpDSspace], \
                                                                                [self._DesignParameter['DeMux1to4_1'][
                                                                                     '_XYCoordinates'][0][0] +
                                                                                 self._DesignParameter['DeMux1to4_1'][
                                                                                     '_DesignObj'].clk90[2][
                                                                                     0] + 3 * tmpDSspace,
                                                                                 1 * CellHeight - 2 * tmpDSspace]])
            # lower
            self._DesignParameter['_Met3_clk1st_via']['_XYCoordinates'].append(
                [[self.getXY('Clk_Driver_2', 'DFFQb2', '_qbpin')[0][0] + 12 * tmpDSspace, 0], \
                 [self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0] +
                  self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0] + 4 * tmpDSspace, 0]])
            self._DesignParameter['_Met3_clk1st_via']['_XYCoordinates'].append(
                [[self.getXY('Clk_Driver_2', 'DFFQb2', '_qbpin')[0][0] + 10 * tmpDSspace, +2 * tmpDSspace], \
                 [self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0] +
                  self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0] + 3 * tmpDSspace, 2 * tmpDSspace]])

        else :
            #### clk driver to demux
            # lower
            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'] = [
                [self.getXY('Clk_Driver_2', 'DFFQb1', '_qpin')[-1], \
                 [self.getXY('Clk_Driver_2', 'DFFQb1', '_qpin')[-1][0], -tmpDSspace]], \
                [[self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0] +
                  self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0] + 4 * tmpDSspace, -tmpDSspace],
                 [self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0] +
                  self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0] + 4 * tmpDSspace,
                  -2 * CellHeight - tmpDSspace]]]  # f16

            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self.getXY('Clk_Driver_2', 'DFFQb1',
                                                                                        '_qbpin')[0][0],
                                                                             self._DesignParameter['Clk_Driver_2'][
                                                                                 '_DesignObj']._DesignParameter[
                                                                                 'DFFQb1']['_DesignObj'].iclk], \
                                                                            [self.getXY('Clk_Driver_2', 'DFFQb1',
                                                                                        '_qbpin')[0][0],
                                                                             +tmpDSspace]])  # f16b
            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clkb[0] + 3 * tmpDSspace,
                                                                             tmpDSspace], \
                                                                            [self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clkb[0] + 3 * tmpDSspace,
                                                                             -2 * CellHeight + tmpDSspace]])  # f16b

            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clk90[2][
                                                                                 0] + 4 * tmpDSspace, 0], \
                                                                            [self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clk90[2][
                                                                                 0] + 4 * tmpDSspace,
                                                                             -2 * CellHeight]])  # f16_90

            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clk90[2][
                                                                                 0] + 3 * tmpDSspace, 2 * tmpDSspace], \
                                                                            [self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clk90[2][
                                                                                 0] + 3 * tmpDSspace,
                                                                             -2 * CellHeight + 2 * tmpDSspace]])  # f16_90b

            # added
            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self.getXY('Clk_Driver_2', 'DFFQb2',
                                                                                        '_qbpin')[0][
                                                                                 0] + 22 * tmpDSspace,
                                                                             self._DesignParameter['Clk_Driver_2'][
                                                                                 '_DesignObj']._DesignParameter[
                                                                                 'DFFQb2']['_DesignObj'].iclkb], \
                                                                            [self.getXY('Clk_Driver_2', 'DFFQb2',
                                                                                        '_qbpin')[0][
                                                                                 0] + 22 * tmpDSspace, 0]])  # f16_90

            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self.getXY('Clk_Driver_2', 'DFFQb2',
                                                                                        '_qbpin')[0][
                                                                                 0] + 20 * tmpDSspace,
                                                                             self._DesignParameter['Clk_Driver_2'][
                                                                                 '_DesignObj']._DesignParameter[
                                                                                 'DFFQb2']['_DesignObj'].iclk], \
                                                                            [self.getXY('Clk_Driver_2', 'DFFQb2',
                                                                                        '_qbpin')[0][
                                                                                 0] + 20 * tmpDSspace,
                                                                             2 * tmpDSspace]])  # f16_90b

            # upper
            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb1', '_qpin')[-1], \
                 [self.getXY('Clk_Driver_2', 'DFFQb1', '_qpin')[-1][0], 1 * CellHeight + tmpDSspace]])  # f16
            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clkb[0] + 4 * tmpDSspace,
                                                                             1 * CellHeight + tmpDSspace], \
                                                                            [self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clkb[0] + 4 * tmpDSspace,
                                                                             3 * CellHeight + tmpDSspace]])  # f16

            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self.getXY('Clk_Driver_2', 'DFFQb1',
                                                                                        '_qbpin')[0][0],
                                                                             self._DesignParameter['Clk_Driver_2'][
                                                                                 '_DesignObj']._DesignParameter[
                                                                                 'DFFQb1']['_DesignObj'].iclk], \
                                                                            [self.getXY('Clk_Driver_2', 'DFFQb1',
                                                                                        '_qbpin')[0][0],
                                                                             1 * CellHeight - tmpDSspace]])  # f16b
            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clkb[0] + 3 * tmpDSspace,
                                                                             3 * CellHeight - tmpDSspace], \
                                                                            [self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clkb[0] + 3 * tmpDSspace,
                                                                             1 * CellHeight - tmpDSspace]])  # f16b

            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clk90[2][
                                                                                 0] + 4 * tmpDSspace, 1 * CellHeight], \
                                                                            [self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clk90[2][
                                                                                 0] + 4 * tmpDSspace,
                                                                             3 * CellHeight]])  # f16_90

            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clk90[2][
                                                                                 0] + 3 * tmpDSspace,
                                                                             1 * CellHeight - 2 * tmpDSspace], \
                                                                            [self._DesignParameter['DeMux1to4_1'][
                                                                                 '_XYCoordinates'][0][0] +
                                                                             self._DesignParameter['DeMux1to4_1'][
                                                                                 '_DesignObj'].clk90[2][
                                                                                 0] + 3 * tmpDSspace,
                                                                             3 * CellHeight - 2 * tmpDSspace]])  # f16_90b

            # added
            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self.getXY('Clk_Driver_2', 'DFFQb2',
                                                                                        '_qbpin')[0][
                                                                                 0] + 22 * tmpDSspace,
                                                                             self._DesignParameter['Clk_Driver_2'][
                                                                                 '_DesignObj']._DesignParameter[
                                                                                 'DFFQb2']['_DesignObj'].iclkb], \
                                                                            [self.getXY('Clk_Driver_2', 'DFFQb2',
                                                                                        '_qbpin')[0][
                                                                                 0] + 22 * tmpDSspace,
                                                                             1 * CellHeight]])  # f16_90

            self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self.getXY('Clk_Driver_2', 'DFFQb2',
                                                                                        '_qbpin')[0][
                                                                                 0] + 20 * tmpDSspace,
                                                                             self._DesignParameter['Clk_Driver_2'][
                                                                                 '_DesignObj']._DesignParameter[
                                                                                 'DFFQb2']['_DesignObj'].iclk], \
                                                                            [self.getXY('Clk_Driver_2', 'DFFQb2',
                                                                                        '_qbpin')[0][
                                                                                 0] + 20 * tmpDSspace,
                                                                             1 * CellHeight - 2 * tmpDSspace]])  # f16_90b
            ## via added for added routing (f16_90 f16_90b)

            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2', '_qbpin')[0][0] + 22 * tmpDSspace,
                 self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb2'][
                     '_DesignObj'].iclkb])  # f16_90
            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2', '_qbpin')[0][0] + 20 * tmpDSspace,
                 self._DesignParameter['Clk_Driver_2']['_DesignObj']._DesignParameter['DFFQb2'][
                     '_DesignObj'].iclk])  # f16_90b

            # upper
            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append([self._DesignParameter[
                                                                                        'DeMux1to4_1'][
                                                                                        '_XYCoordinates'][0][0] +
                                                                                    self._DesignParameter[
                                                                                        'DeMux1to4_1'][
                                                                                        '_DesignObj'].clk90[2][
                                                                                        0] + 4 * tmpDSspace,
                                                                                    1 * CellHeight])  # f16_90
            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append([self._DesignParameter[
                                                                                        'DeMux1to4_1'][
                                                                                        '_XYCoordinates'][0][0] +
                                                                                    self._DesignParameter[
                                                                                        'DeMux1to4_1'][
                                                                                        '_DesignObj'].clk90[2][
                                                                                        0] + 3 * tmpDSspace,
                                                                                    1 * CellHeight - 2 * tmpDSspace])  # f16_90b
            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2', '_qbpin')[0][0] + 22 * tmpDSspace, 1 * CellHeight])  # f16_90
            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2', '_qbpin')[0][0] + 20 * tmpDSspace,
                 1 * CellHeight - 2 * tmpDSspace])  # f16_90b

            # lower
            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append([self._DesignParameter[
                                                                                        'DeMux1to4_1'][
                                                                                        '_XYCoordinates'][0][0] +
                                                                                    self._DesignParameter[
                                                                                        'DeMux1to4_1'][
                                                                                        '_DesignObj'].clk90[2][
                                                                                        0] + 4 * tmpDSspace, 0])
            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append([self._DesignParameter[
                                                                                        'DeMux1to4_1'][
                                                                                        '_XYCoordinates'][0][0] +
                                                                                    self._DesignParameter[
                                                                                        'DeMux1to4_1'][
                                                                                        '_DesignObj'].clk90[2][
                                                                                        0] + 3 * tmpDSspace,
                                                                                    2 * tmpDSspace])
            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2', '_qbpin')[0][0] + 22 * tmpDSspace, 0])  # f16_90
            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append(
                [self.getXY('Clk_Driver_2', 'DFFQb2', '_qbpin')[0][0] + 20 * tmpDSspace, +2 * tmpDSspace])  # f16_90b

            ### rotue revise added met3
            # Qb2 stage met3
            self._DesignParameter['_Met3_clk1st_via']['_XYCoordinates'].append([[self.getXY('Clk_Driver_2', 'DFFQb2',
                                                                                            '_qbpin')[0][
                                                                                     0] + 22 * tmpDSspace,
                                                                                 self._DesignParameter['Clk_Driver_2'][
                                                                                     '_DesignObj']._DesignParameter[
                                                                                     'DFFQb2']['_DesignObj'].iclkb], \
                                                                                [self.getXY('Clk_Driver_2', 'DFFQb2',
                                                                                            '_qpin')[-1][0],
                                                                                 self._DesignParameter['Clk_Driver_2'][
                                                                                     '_DesignObj']._DesignParameter[
                                                                                     'DFFQb2']['_DesignObj'].iclkb]])
            self._DesignParameter['_Met3_clk1st_via']['_XYCoordinates'].append([[self.getXY('Clk_Driver_2', 'DFFQb2',
                                                                                            '_qbpin')[0][
                                                                                     0] + 20 * tmpDSspace,
                                                                                 self._DesignParameter['Clk_Driver_2'][
                                                                                     '_DesignObj']._DesignParameter[
                                                                                     'DFFQb2']['_DesignObj'].iclk], \
                                                                                [self.getXY('Clk_Driver_2', 'DFFQb2',
                                                                                            '_qbpin')[0][0],
                                                                                 self._DesignParameter['Clk_Driver_2'][
                                                                                     '_DesignObj']._DesignParameter[
                                                                                     'DFFQb2']['_DesignObj'].iclk]])
            # upper
            self._DesignParameter['_Met3_clk1st_via']['_XYCoordinates'].append(
                [[self.getXY('Clk_Driver_2', 'DFFQb2', '_qbpin')[0][0] + 22 * tmpDSspace, 1 * CellHeight], \
                 [self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0] +
                  self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0] + 4 * tmpDSspace, 1 * CellHeight]])
            self._DesignParameter['_Met3_clk1st_via']['_XYCoordinates'].append([[self.getXY('Clk_Driver_2', 'DFFQb2',
                                                                                            '_qbpin')[0][
                                                                                     0] + 20 * tmpDSspace,
                                                                                 1 * CellHeight - 2 * tmpDSspace], \
                                                                                [self._DesignParameter['DeMux1to4_1'][
                                                                                     '_XYCoordinates'][0][0] +
                                                                                 self._DesignParameter['DeMux1to4_1'][
                                                                                     '_DesignObj'].clk90[2][
                                                                                     0] + 3 * tmpDSspace,
                                                                                 1 * CellHeight - 2 * tmpDSspace]])
            # lower
            self._DesignParameter['_Met3_clk1st_via']['_XYCoordinates'].append(
                [[self.getXY('Clk_Driver_2', 'DFFQb2', '_qbpin')[0][0] + 22 * tmpDSspace, 0], \
                 [self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0] +
                  self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0] + 4 * tmpDSspace, 0]])
            self._DesignParameter['_Met3_clk1st_via']['_XYCoordinates'].append(
                [[self.getXY('Clk_Driver_2', 'DFFQb2', '_qbpin')[0][0] + 20 * tmpDSspace, +2 * tmpDSspace], \
                 [self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0] +
                  self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0] + 3 * tmpDSspace, 2 * tmpDSspace]])

        # #upper
        # self._DesignParameter['_Met3_clk1st_via']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0]+3*tmpDSspace,1*CellHeight-tmpDSspace],\
        #                                                                     [self.getXY('Clk_Driver_2','DFFQb2','_qbpin')[0][0],1*CellHeight-tmpDSspace]])#f16b
        # self._DesignParameter['_Met3_clk1st_via']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0]+4*tmpDSspace,1*CellHeight+tmpDSspace],\
        #                                                                     [self.getXY('Clk_Driver_2','DFFQb2','_qpin')[-1][0],1*CellHeight+tmpDSspace]])#f16
        # #lower
        # self._DesignParameter['_Met3_clk1st_via']['_XYCoordinates'].append([[self.getXY('Clk_Driver_2','DFFQb2','_qpin')[-1][0],-tmpDSspace],\
        #                                                                     [self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0]+4*tmpDSspace,-tmpDSspace]])#f16
        # self._DesignParameter['_Met3_clk1st_via']['_XYCoordinates'].append([[self.getXY('Clk_Driver_2','DFFQb2','_qbpin')[0][0],+tmpDSspace],\
        #                                                                     [self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0]+3*tmpDSspace,tmpDSspace]])#f16b

        self._DesignParameter['_Met3_clk2nd_Q1'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=tmpMet2Width
        )
        # self._DesignParameter['_Met3_clk2nd_Q1'] = self._PathElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        #     _Width=tmpViaMet2Width
        # )
        #Qb1 stage met3
        #upper
        self._DesignParameter['_Met3_clk2nd_Q1']['_XYCoordinates']=[[[self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0]+3*tmpDSspace,1*CellHeight-tmpDSspace+tmpViaMet2Width/2-tmpMet2Width/2],\
                                                                            [self.getXY('Clk_Driver_2','DFFQb1','_qbpin')[0][0],1*CellHeight-tmpDSspace+tmpViaMet2Width/2-tmpMet2Width/2]]]#f16b
        self._DesignParameter['_Met3_clk2nd_Q1']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0]+4*tmpDSspace,1*CellHeight+tmpDSspace-tmpViaMet2Width/2+tmpMet2Width/2],\
                                                                            [self.getXY('Clk_Driver_2','DFFQb1','_qpin')[-1][0],1*CellHeight+tmpDSspace-tmpViaMet2Width/2+tmpMet2Width/2]])#f16
        #lower
        self._DesignParameter['_Met3_clk2nd_Q1']['_XYCoordinates'].append([[self.getXY('Clk_Driver_2','DFFQb1','_qpin')[-1][0],-tmpDSspace+tmpViaMet2Width/2-tmpMet2Width/2],\
                                                                            [self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0]+4*tmpDSspace,-tmpDSspace+tmpViaMet2Width/2-tmpMet2Width/2]])#f16
        self._DesignParameter['_Met3_clk2nd_Q1']['_XYCoordinates'].append([[self.getXY('Clk_Driver_2','DFFQb1','_qbpin')[0][0],+tmpDSspace-tmpViaMet2Width/2+tmpMet2Width/2],\
                                                                            [self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0]+3*tmpDSspace,tmpDSspace-tmpViaMet2Width/2+tmpMet2Width/2]])#f16b


        #### demux to demux clk routing
        ### metal4
        #upper
        #clk
        self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk[0],self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk[1]],\
                                                                       [self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_4']['_DesignObj'].clk[0],self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_4']['_DesignObj'].clk[1]]])
        #clkb
        self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0],self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[1]],\
                                                                       [self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_4']['_DesignObj'].clkb[0],self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_4']['_DesignObj'].clkb[1]]])
        #clk90
        self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[0][0],self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[0][1]],\
                                                                       [self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_4']['_DesignObj'].clk90[0][0],self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_4']['_DesignObj'].clk90[0][1]]])
        self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[1][0],self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[1][1]],\
                                                                       [self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_4']['_DesignObj'].clk90[1][0],self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_4']['_DesignObj'].clk90[1][1]]])
        self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0],self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][1]],\
                                                                       [self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_4']['_DesignObj'].clk90[2][0],self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_4']['_DesignObj'].clk90[2][1]]])
        #clk90b
        self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90b[0],self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90b[1]],\
                                                                       [self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_4']['_DesignObj'].clk90b[0],self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_4']['_DesignObj'].clk90b[1]]])


        #lower
        #clk
        self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clk[0],self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clk[1]],\
                                                                       [self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_5']['_DesignObj'].clk[0],self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_5']['_DesignObj'].clk[1]]])
        #clkb
        self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clkb[0],self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clkb[1]],\
                                                                       [self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_5']['_DesignObj'].clkb[0],self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_5']['_DesignObj'].clkb[1]]])
        #clk90
        self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clk90[0][0],self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clk90[0][1]],\
                                                                       [self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_5']['_DesignObj'].clk90[0][0],self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_5']['_DesignObj'].clk90[0][1]]])
        self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clk90[1][0],self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clk90[1][1]],\
                                                                       [self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_5']['_DesignObj'].clk90[1][0],self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_5']['_DesignObj'].clk90[1][1]]])
        self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clk90[2][0],self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clk90[2][1]],\
                                                                       [self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_5']['_DesignObj'].clk90[2][0],self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_5']['_DesignObj'].clk90[2][1]]])
        #clk90b
        self._DesignParameter['_Met4_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clk90b[0],self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clk90b[1]],\
                                                                       [self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_5']['_DesignObj'].clk90b[0],self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_5']['_DesignObj'].clk90b[1]]])


        # upper
        # clk
        self._DesignParameter['_Met3_clk2nd']['_XYCoordinates'] = [[[self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk[0],3*CellHeight+tmpDSspace],\
                                                                       [self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0]+4*tmpDSspace,3*CellHeight+tmpDSspace]]]
        # clkb
        self._DesignParameter['_Met3_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0],3*CellHeight-tmpDSspace],\
                                                                        [self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0]+3*tmpDSspace,3*CellHeight-tmpDSspace]])
        # clk90
        self._DesignParameter['_Met3_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[0][0],3*CellHeight],\
                                                                        [self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0]+4*tmpDSspace,3*CellHeight]])
        self._DesignParameter['_Met3_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[1][0],3*CellHeight],\
                                                                        [self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0]+4*tmpDSspace,3*CellHeight]])
        self._DesignParameter['_Met3_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[-1][0],3*CellHeight],\
                                                                        [self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0]+4*tmpDSspace,3*CellHeight]])
        # clk90b
        self._DesignParameter['_Met3_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90b[0],3*CellHeight-2*tmpDSspace],\
                                                                        [self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0]+3*tmpDSspace,3*CellHeight-2*tmpDSspace]])

        # lower
        # clk
        self._DesignParameter['_Met3_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clk[0],-2*CellHeight-tmpDSspace],\
                                                                       [self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0]+4*tmpDSspace,-2*CellHeight-tmpDSspace]])
        # clkb
        self._DesignParameter['_Met3_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clkb[0],-2*CellHeight+tmpDSspace],\
                                                                        [self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0]+3*tmpDSspace,-2*CellHeight+tmpDSspace]])
        # clk90
        self._DesignParameter['_Met3_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clk90[0][0],-2*CellHeight],\
                                                                        [self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0]+4*tmpDSspace,-2*CellHeight]])
        self._DesignParameter['_Met3_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clk90[1][0],-2*CellHeight],\
                                                                        [self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0]+4*tmpDSspace,-2*CellHeight]])
        self._DesignParameter['_Met3_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clk90[-1][0],-2*CellHeight],\
                                                                        [self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0]+4*tmpDSspace,-2*CellHeight]])
        # clk90b
        self._DesignParameter['_Met3_clk2nd']['_XYCoordinates'].append([[self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clk90b[0],-2*CellHeight+2*tmpDSspace],\
                                                                        [self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0]+3*tmpDSspace,-2*CellHeight+2*tmpDSspace]])

        ##### metal 3
        ############ clk routing via
        #added via\
        #upper #f16 and f16b
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk[0]-tmpViaminWidth/2 + tmpMet2Width/2,3*CellHeight+tmpDSspace])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0]+4*tmpDSspace-tmpViaminWidth/2 + tmpMet2Width/2,3*CellHeight+tmpDSspace])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0]-tmpViaminWidth/2 + tmpMet2Width/2,3*CellHeight-tmpDSspace])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0]+3*tmpDSspace-tmpViaminWidth/2 + tmpMet2Width/2,3*CellHeight-tmpDSspace])
        a1=self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0]+3*tmpDSspace
        b1=self.getXY('Clk_Driver_2','DFFQb1','_qbpin')[0][0]

        if 0<b1-a1<tmpDSspace+1 :
            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0]+3*tmpDSspace,1*CellHeight-tmpDSspace+tmpViaMet2Width/2])
            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append([self.getXY('Clk_Driver_2','DFFQb1','_qpin')[-1][0],1*CellHeight+tmpDSspace-tmpViaMet2Width/2])
        else :
            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0]+3*tmpDSspace,1*CellHeight-tmpDSspace])
            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append([self.getXY('Clk_Driver_2','DFFQb1','_qpin')[-1][0],1*CellHeight+tmpDSspace])


        self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append([self.getXY('Clk_Driver_2','DFFQb1','_qbpin')[0][0],1*CellHeight-tmpDSspace])
        self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0]+4*tmpDSspace,1*CellHeight+tmpDSspace])

        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[0][0]-tmpViaminWidth/2 + tmpMet2Width/2,3*CellHeight])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0]+4*tmpDSspace-tmpViaminWidth/2 + tmpMet2Width/2,3*CellHeight])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[1][0]-tmpViaminWidth/2 + tmpMet2Width/2,3*CellHeight])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0]+4*tmpDSspace-tmpViaminWidth/2 + tmpMet2Width/2,3*CellHeight])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[-1][0]-tmpViaminWidth/2 + tmpMet2Width/2,3*CellHeight])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0]+4*tmpDSspace-tmpViaminWidth/2 + tmpMet2Width/2,3*CellHeight])

        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90b[0]-tmpViaminWidth/2 + tmpMet2Width/2,3*CellHeight-2*tmpDSspace])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0]+3*tmpDSspace-tmpViaminWidth/2 + tmpMet2Width/2,3*CellHeight-2*tmpDSspace])

        #lower
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk[0]-tmpViaminWidth/2 + tmpMet2Width/2,-2*CellHeight-tmpDSspace])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0]+4*tmpDSspace-tmpViaminWidth/2 + tmpMet2Width/2,-2*CellHeight-tmpDSspace])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0]-tmpViaminWidth/2 + tmpMet2Width/2,-2*CellHeight+tmpDSspace])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0]+3*tmpDSspace-tmpViaminWidth/2 + tmpMet2Width/2,-2*CellHeight+tmpDSspace])

        if 0<b1-a1<tmpDSspace+1 :
            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0]+3*tmpDSspace,tmpDSspace-tmpViaMet2Width/2])
            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append([self.getXY('Clk_Driver_2','DFFQb1','_qpin')[-1][0],-tmpDSspace+tmpViaMet2Width/2])
        else :
            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0]+3*tmpDSspace,tmpDSspace])
            self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append([self.getXY('Clk_Driver_2','DFFQb1','_qpin')[-1][0],-tmpDSspace])



        self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append([self.getXY('Clk_Driver_2','DFFQb1','_qbpin')[0][0],+tmpDSspace])

        self._DesignParameter['_ViaMet32Met4_clk2nd']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0]+4*tmpDSspace,-tmpDSspace])

        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[0][0]-tmpViaminWidth/2 + tmpMet2Width/2,-2*CellHeight])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0]+4*tmpDSspace-tmpViaminWidth/2 + tmpMet2Width/2,-2*CellHeight])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[1][0]-tmpViaminWidth/2 + tmpMet2Width/2,-2*CellHeight])
        #self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self.getXY('Clk_Driver_2','DFFQb2','_qpin')[-1][0]-tmpViaminWidth/2 + tmpMet2Width/2,-2*CellHeight])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[-1][0]-tmpViaminWidth/2 + tmpMet2Width/2,-2*CellHeight])
        #self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self.getXY('Clk_Driver_2','DFFQb2','_qpin')[-1][0]-tmpViaminWidth/2 + tmpMet2Width/2,-2*CellHeight])

        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90b[0]-tmpViaminWidth/2 + tmpMet2Width/2,-2*CellHeight+2*tmpDSspace])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0]+3*tmpDSspace-tmpViaminWidth/2 + tmpMet2Width/2,-2*CellHeight+2*tmpDSspace])

        #clk via added
        #clk
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk[0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk[1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_2']['_DesignObj'].clk[0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_2']['_DesignObj'].clk[1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_3']['_DesignObj'].clk[0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_3']['_DesignObj'].clk[1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_4']['_DesignObj'].clk[0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_4']['_DesignObj'].clk[1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_5']['_DesignObj'].clk[0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_5']['_DesignObj'].clk[1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_6']['_DesignObj'].clk[0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_6']['_DesignObj'].clk[1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_7']['_DesignObj'].clk[0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_7']['_DesignObj'].clk[1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clk[0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clk[1]])
        #clkb
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clkb[1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_2']['_DesignObj'].clkb[0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_2']['_DesignObj'].clkb[1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_3']['_DesignObj'].clkb[0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_3']['_DesignObj'].clkb[1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_4']['_DesignObj'].clkb[0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_4']['_DesignObj'].clkb[1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_5']['_DesignObj'].clkb[0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_5']['_DesignObj'].clkb[1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_6']['_DesignObj'].clkb[0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_6']['_DesignObj'].clkb[1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_7']['_DesignObj'].clkb[0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_7']['_DesignObj'].clkb[1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clkb[0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clkb[1]])

        #clk90
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[0][0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[0][1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_2']['_DesignObj'].clk90[0][0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_2']['_DesignObj'].clk90[0][1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_3']['_DesignObj'].clk90[0][0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_3']['_DesignObj'].clk90[0][1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_4']['_DesignObj'].clk90[0][0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_4']['_DesignObj'].clk90[0][1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_5']['_DesignObj'].clk90[0][0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_5']['_DesignObj'].clk90[0][1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_6']['_DesignObj'].clk90[0][0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_6']['_DesignObj'].clk90[0][1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_7']['_DesignObj'].clk90[0][0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_7']['_DesignObj'].clk90[0][1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clk90[0][0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clk90[0][1]])

        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[1][0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[1][1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_2']['_DesignObj'].clk90[1][0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_2']['_DesignObj'].clk90[1][1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_3']['_DesignObj'].clk90[1][0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_3']['_DesignObj'].clk90[1][1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_4']['_DesignObj'].clk90[1][0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_4']['_DesignObj'].clk90[1][1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_5']['_DesignObj'].clk90[1][0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_5']['_DesignObj'].clk90[1][1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_6']['_DesignObj'].clk90[1][0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_6']['_DesignObj'].clk90[1][1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_7']['_DesignObj'].clk90[1][0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_7']['_DesignObj'].clk90[1][1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clk90[1][0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clk90[1][1]])

        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90[2][1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_2']['_DesignObj'].clk90[2][0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_2']['_DesignObj'].clk90[2][1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_3']['_DesignObj'].clk90[2][0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_3']['_DesignObj'].clk90[2][1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_4']['_DesignObj'].clk90[2][0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_4']['_DesignObj'].clk90[2][1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_5']['_DesignObj'].clk90[2][0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_5']['_DesignObj'].clk90[2][1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_6']['_DesignObj'].clk90[2][0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_6']['_DesignObj'].clk90[2][1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_7']['_DesignObj'].clk90[2][0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_7']['_DesignObj'].clk90[2][1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clk90[2][0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clk90[2][1]])


        #clk90b
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90b[0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_1']['_DesignObj'].clk90b[1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_2']['_DesignObj'].clk90b[0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_2']['_DesignObj'].clk90b[1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_3']['_DesignObj'].clk90b[0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_3']['_DesignObj'].clk90b[1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_4']['_DesignObj'].clk90b[0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_4']['_DesignObj'].clk90b[1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_5']['_DesignObj'].clk90b[0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_5']['_DesignObj'].clk90b[1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_6']['_DesignObj'].clk90b[0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_6']['_DesignObj'].clk90b[1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_7']['_DesignObj'].clk90b[0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][1]-self._DesignParameter['DeMux1to4_7']['_DesignObj'].clk90b[1]])
        self._DesignParameter['_ViaMet32Met4_clk2nd_2']['_XYCoordinates'].append([self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clk90b[0]-tmpViaminWidth/2+tmpMet2Width/2,\
                                                                                  self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][1]+self._DesignParameter['DeMux1to4_8']['_DesignObj'].clk90b[1]])

        ####################### 2nd to 3rd stage clk and clkb end!!!!!!!

        ########################## Pin Generation ##################

        '''Pin generation'''
        self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VDD')
        self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VSS')

        self._DesignParameter['_Dinpin'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='data')

        self._DesignParameter['_Dout0in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<0>')
        self._DesignParameter['_Dout1in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<1>')
        self._DesignParameter['_Dout2in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<2>')
        self._DesignParameter['_Dout3in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<3>')
        self._DesignParameter['_Dout4in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<4>')
        self._DesignParameter['_Dout5in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<5>')
        self._DesignParameter['_Dout6in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<6>')
        self._DesignParameter['_Dout7in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<7>')
        self._DesignParameter['_Dout8in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<8>')
        self._DesignParameter['_Dout9in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<9>')
        self._DesignParameter['_Dout10in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<10>')
        self._DesignParameter['_Dout11in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<11>')
        self._DesignParameter['_Dout12in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<12>')
        self._DesignParameter['_Dout13in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<13>')
        self._DesignParameter['_Dout14in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<14>')
        self._DesignParameter['_Dout15in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<15>')
        self._DesignParameter['_Dout16in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<16>')
        self._DesignParameter['_Dout17in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<17>')
        self._DesignParameter['_Dout18in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<18>')
        self._DesignParameter['_Dout19in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<19>')
        self._DesignParameter['_Dout20in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<20>')
        self._DesignParameter['_Dout21in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<21>')
        self._DesignParameter['_Dout22in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<22>')
        self._DesignParameter['_Dout23in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<23>')
        self._DesignParameter['_Dout24in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<24>')
        self._DesignParameter['_Dout25in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<25>')
        self._DesignParameter['_Dout26in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<26>')
        self._DesignParameter['_Dout27in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<27>')
        self._DesignParameter['_Dout28in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<28>')
        self._DesignParameter['_Dout29in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<29>')
        self._DesignParameter['_Dout30in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<30>')
        self._DesignParameter['_Dout31in'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='out<31>')

        self._DesignParameter['_clkpin'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='clk')
        self._DesignParameter['_clkbpin'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='clkb')

        self._DesignParameter['_VDDpin']['_XYCoordinates'] = [[self.getXY('Clk_Driver_1')[0][0]+tmpDSspace,self.getXY('Clk_Driver_1')[0][1]+CellHeight],\
                                                              [self.getXY('Clk_Driver_1')[0][0]+tmpDSspace,self.getXY('Clk_Driver_1')[0][1]+3*CellHeight],\
                                                              [self.getXY('Clk_Driver_1')[0][0]+tmpDSspace,self.getXY('Clk_Driver_1')[0][1]+5*CellHeight],\
                                                              [self.getXY('Clk_Driver_1')[0][0]+tmpDSspace,self.getXY('Clk_Driver_1')[0][1]-CellHeight],\
                                                              [self.getXY('Clk_Driver_1')[0][0]+tmpDSspace,self.getXY('Clk_Driver_1')[0][1]-3*CellHeight]]

        self._DesignParameter['_VSSpin']['_XYCoordinates'] = [[self.getXY('Clk_Driver_1')[0][0]+tmpDSspace,self.getXY('Clk_Driver_1')[0][1]],\
                                                              [self.getXY('Clk_Driver_1')[0][0]+tmpDSspace,self.getXY('Clk_Driver_1')[0][1]+2*CellHeight],\
                                                              [self.getXY('Clk_Driver_1')[0][0]+tmpDSspace,self.getXY('Clk_Driver_1')[0][1]+4*CellHeight],\
                                                              [self.getXY('Clk_Driver_1')[0][0]+tmpDSspace,self.getXY('Clk_Driver_1')[0][1]-2*CellHeight],\
                                                              [self.getXY('Clk_Driver_1')[0][0]+tmpDSspace,self.getXY('Clk_Driver_1')[0][1]-4*CellHeight]]
        self._DesignParameter['_Dinpin']['_XYCoordinates'] = self.getXY('DeMux1to2_3','DFF_Latch','_dpin')

        CellXWidth = self._DesignParameter['DeMux1to4_1']['_DesignObj'].CellXWidth
        ### Demux1
        self._DesignParameter['_Dout0in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][1] + self._DesignParameter['DeMux1to4_1']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclk + Dataoutspacing]]
        self._DesignParameter['_Dout8in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][1] + self._DesignParameter['DeMux1to4_1']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclk ]]
        self._DesignParameter['_Dout16in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][1] + self._DesignParameter['DeMux1to4_1']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclkb ]]
        self._DesignParameter['_Dout24in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_1']['_XYCoordinates'][0][1] + self._DesignParameter['DeMux1to4_1']['_DesignObj'].D4[1]]]
        ### Demux8
        self._DesignParameter['_Dout1in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][1] + self._DesignParameter['DeMux1to4_8']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclk + Dataoutspacing]]
        self._DesignParameter['_Dout9in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][1] + self._DesignParameter['DeMux1to4_8']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclk ]]
        self._DesignParameter['_Dout17in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][1] + self._DesignParameter['DeMux1to4_8']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclkb ]]
        self._DesignParameter['_Dout25in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_8']['_XYCoordinates'][0][1] + self._DesignParameter['DeMux1to4_8']['_DesignObj'].D4[1]]]
        ### Demux3
        self._DesignParameter['_Dout4in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][1] + self._DesignParameter['DeMux1to4_3']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclk + Dataoutspacing]]
        self._DesignParameter['_Dout12in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][1] + self._DesignParameter['DeMux1to4_3']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclk ]]
        self._DesignParameter['_Dout20in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][1] + self._DesignParameter['DeMux1to4_3']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclkb ]]
        self._DesignParameter['_Dout28in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_3']['_XYCoordinates'][0][1] + self._DesignParameter['DeMux1to4_3']['_DesignObj'].D4[1]]]
        ### Demux6
        self._DesignParameter['_Dout5in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][1] + self._DesignParameter['DeMux1to4_6']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclk + Dataoutspacing]]
        self._DesignParameter['_Dout13in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][1] + self._DesignParameter['DeMux1to4_6']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclk ]]
        self._DesignParameter['_Dout21in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][1] + self._DesignParameter['DeMux1to4_6']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclkb ]]
        self._DesignParameter['_Dout29in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_6']['_XYCoordinates'][0][1] + self._DesignParameter['DeMux1to4_6']['_DesignObj'].D4[1]]]

        ### Demux2
        self._DesignParameter['_Dout2in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][1] - self._DesignParameter['DeMux1to4_2']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclk - Dataoutspacing]]
        self._DesignParameter['_Dout10in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][1] - self._DesignParameter['DeMux1to4_2']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclk ]]
        self._DesignParameter['_Dout18in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][1] - self._DesignParameter['DeMux1to4_2']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclkb ]]
        self._DesignParameter['_Dout26in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_2']['_XYCoordinates'][0][1] - self._DesignParameter['DeMux1to4_2']['_DesignObj'].D4[1]]]
        ### Demux4
        self._DesignParameter['_Dout6in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][1] - self._DesignParameter['DeMux1to4_4']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclk - Dataoutspacing]]
        self._DesignParameter['_Dout14in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][1] - self._DesignParameter['DeMux1to4_4']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclk ]]
        self._DesignParameter['_Dout22in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][1] - self._DesignParameter['DeMux1to4_4']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclkb ]]
        self._DesignParameter['_Dout30in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_4']['_XYCoordinates'][0][1] - self._DesignParameter['DeMux1to4_4']['_DesignObj'].D4[1]]]
        ### Demux5
        self._DesignParameter['_Dout7in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][1] - self._DesignParameter['DeMux1to4_5']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclk - Dataoutspacing]]
        self._DesignParameter['_Dout15in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][1] - self._DesignParameter['DeMux1to4_5']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclk ]]
        self._DesignParameter['_Dout23in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][1] - self._DesignParameter['DeMux1to4_5']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclkb ]]
        self._DesignParameter['_Dout31in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_5']['_XYCoordinates'][0][1] - self._DesignParameter['DeMux1to4_5']['_DesignObj'].D4[1]]]
        ### Demux7
        self._DesignParameter['_Dout3in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][1] - self._DesignParameter['DeMux1to4_7']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclk - Dataoutspacing]]
        self._DesignParameter['_Dout11in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][1] - self._DesignParameter['DeMux1to4_7']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclk ]]
        self._DesignParameter['_Dout19in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][1] - self._DesignParameter['DeMux1to4_7']['_DesignObj']._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclkb ]]
        self._DesignParameter['_Dout27in']['_XYCoordinates'] = [[self._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][0] + CellXWidth-tmpDSspace, \
              self._DesignParameter['DeMux1to4_7']['_XYCoordinates'][0][1] - self._DesignParameter['DeMux1to4_7']['_DesignObj'].D4[1]]]

        self._DesignParameter['_clkpin']['_XYCoordinates'] = [[self.getXY('DeMux1to2_3')[0][0]+tmpDSspace,self.getXY('DeMux1to2_3')[0][1]+3*CellHeight]]
        self._DesignParameter['_clkbpin']['_XYCoordinates'] = [[self.getXY('DeMux1to2_3')[0][0]+tmpDSspace,self.getXY('DeMux1to2_3')[0][1]+3*CellHeight-tmpDSspace]]

        # ########################## cell width ##################
        # self.CellXWidth = self.getXY('DFFQb2','INV5', '_PMOS', '_POLayer')[-1][0] + UnitPitch
        # self.CellYWidth = CellHeight
        #
        #


''' INV2&3 # of Fingers should be less than 7(6 max)
    otherwise, INV inner routing and qb routing will be overlapped'''
################################ DRC Check #################################
import random
if __name__ == '__main__':
    for i in range(0,100):
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

        TG1_Finger_clk = TG1_Finger
        TG2_Finger_clk = TG2_Finger
        TSI1_Finger_clk = TSI1_Finger
        TSI2_Finger_clk = TSI2_Finger
        INV1_Finger_clk = INV1_Finger
        INV2_Finger_clk = INV2_Finger
        INV3_Finger_clk = INV3_Finger
        INV4_Finger_clk = INV5_Finger
        INV5_Finger_clk = INV6_Finger

        # TG1_Finger_clk = random.randint(1, 5)
        # TG2_Finger_clk = random.randint(1, 5)
        # TSI1_Finger_clk = random.randint(1, 2)
        # TSI2_Finger_clk = random.randint(1, 2)
        # INV1_Finger_clk = random.randint(1, 5)
        # INV2_Finger_clk = random.randint(1, 5)
        # INV3_Finger_clk = random.randint(1, 5)
        # INV4_Finger_clk = random.randint(1, 5)
        # INV5_Finger_clk = random.randint(1, 5)

        TG1_NMWidth =TG2_NMWidth=TG3_NMWidth= TG4_NMWidth=TSI1_NMWidth=TSI2_NMWidth=TSI3_NMWidth=TSI4_NMWidth=INV1_NMWidth=INV2_NMWidth=INV3_NMWidth\
            =INV4_NMWidth=INV5_NMWidth=INV6_NMWidth=INV7_NMWidth=INV8_NMWidth=INV9_NMWidth=INV10_NMWidth=200
        TG1_PMWidth = TG2_PMWidth=TG3_PMWidth=TG4_PMWidth=TSI1_PMWidth=TSI2_PMWidth=TSI3_PMWidth=TSI4_PMWidth=INV1_PMWidth=INV2_PMWidth=INV3_PMWidth\
            =INV4_PMWidth=INV5_PMWidth=INV6_PMWidth=INV7_PMWidth=INV8_PMWidth=INV9_PMWidth=INV10_PMWidth=400

        INV1_NMWidth=INV2_NMWidth=INV3_NMWidth\
            =INV4_NMWidth=INV5_NMWidth=INV6_NMWidth=INV7_NMWidth=INV8_NMWidth=INV9_NMWidth=INV10_NMWidth=250
        INV1_PMWidth=INV2_PMWidth=INV3_PMWidth\
            =INV4_PMWidth=INV5_PMWidth=INV6_PMWidth=INV7_PMWidth=INV8_PMWidth=INV9_PMWidth=INV10_PMWidth=500

        ChannelLength = 30
        GateSpacing = 100
        SDWidth = 66
        XVT = 'SLVT'
        CellHeight = 1800
        SupplyRailType = 2

        # TG1_Finger = 1
        # TG2_Finger = 2
        # TSI1_Finger = 1
        # TSI2_Finger = 1
        # INV1_Finger = 3
        # INV2_Finger = 1
        # INV3_Finger = 1
        # INV4_Finger = 3
        # TG3_Finger = 2
        # TSI3_Finger = 1
        # INV5_Finger = 4
        # INV6_Finger = 4
        # TG4_Finger = 2
        # TSI4_Finger = 1
        # INV7_Finger = 4
        # INV8_Finger = 4
        # INV9_Finger = 1
        # INV10_Finger = 1
        #
        # TG1_Finger_clk = 1
        # TG2_Finger_clk = 2
        # TSI1_Finger_clk = 1
        # TSI2_Finger_clk = 1
        # INV1_Finger_clk = 3
        # INV2_Finger_clk = 1
        # INV3_Finger_clk = 1
        # INV4_Finger_clk = 4
        # INV5_Finger_clk = 4

        print("itr = ", i)
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
        TopObj = Deserializer1to32(_DesignParameter=None, _Name='Deserializer1to32')
        TopObj._CalculateDesignParameter(
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


            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            SDWidth=SDWidth,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType)

        TopObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=TopObj._DesignParameter)
        testStreamFile = open('./Deserializer1to32.gds', 'wb')
        tmp = TopObj._CreateGDSStream(TopObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()
        print('#############################      Sending to FTP Server...      ##############################')
        i=i+1
        print("itr = ", i)
        import ftplib

        ftp = ftplib.FTP('141.223.24.53')
        ftp.login('ljw95', 'dlwodn123')
        ftp.cwd('/mnt/sdc/ljw95/OPUS/ss28')
        myfile = open('Deserializer1to32.gds', 'rb')
        ftp.storbinary('STOR Deserializer1to32.gds', myfile)
        myfile.close()

        import DRCchecker
        a = DRCchecker.DRCchecker('ljw95','dlwodn123','/mnt/sdc/ljw95/OPUS/ss28','/mnt/sdc/ljw95/OPUS/ss28/DRC/run','Deserializer1to32','Deserializer1to32',None)
        a.DRCchecker()

        print ("DRC Clean!!!")
