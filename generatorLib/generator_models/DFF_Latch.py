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

#
from generatorLib import CoordinateCalc as CoordCalc


class DFF(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name='DFF'):
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
                                  TG2_Finger=1,
                                  TG2_NMWidth=320,
                                  TG2_PMWidth=584,

                                  TSI1_Finger=1,
                                  TSI1_NMWidth=200,
                                  TSI1_PMWidth=400,
                                  TSI2_Finger=1,
                                  TSI2_NMWidth=200,
                                  TSI2_PMWidth=400,

                                  INV1_Finger=4,
                                  INV1_NMWidth=250,
                                  INV1_PMWidth=500,

                                  INV2_Finger=1,
                                  INV2_NMWidth=200,
                                  INV2_PMWidth=400,
                                  INV3_Finger=1,
                                  INV3_NMWidth=200,
                                  INV3_PMWidth=400,

                                  INV4_Finger=1,
                                  INV4_NMWidth=100,
                                  INV4_PMWidth=200,

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

        Parameters_TG1 = dict(
            nmos_gate=TG1_Finger,
            pmos_gate=TG1_Finger,
            nmos_width=TG1_NMWidth,
            pmos_width=TG1_PMWidth,
            length=ChannelLength,
            XVT=XVT,
            vss2vdd_height=CellHeight,
            gate_spacing=GateSpacing,
            sdwidth=SDWidth,
            power_xdistance=UnitPitch,
            #out_even_up_mode=True
        )
        Parameters_TG2 = dict(
            nmos_gate=TG2_Finger,
            pmos_gate=TG2_Finger,
            nmos_width=TG2_NMWidth,
            pmos_width=TG2_PMWidth,
            length=ChannelLength,
            XVT=XVT,
            vss2vdd_height=CellHeight,
            gate_spacing=GateSpacing,
            sdwidth=SDWidth,
            power_xdistance=UnitPitch,
            #out_even_up_mode=True
        )

        Parameters_TSI1 = dict(
            NMOSWidth=TSI1_NMWidth,
            PMOSWidth=TSI1_PMWidth,
            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType
        )
        Parameters_TSI1_f3 = dict(
        NumFinger_NM1 = TSI1_Finger,
        NumFinger_NM2 = TSI1_Finger,
        Width_NM1 = TSI1_NMWidth,
        Width_NM2 = TSI1_NMWidth,
        Width_PM1 = TSI1_PMWidth,
        Width_PM2 = TSI1_PMWidth,

        ChannelLength = ChannelLength,
        GateSpacing = GateSpacing,
        XVT = XVT,

        CellHeight = CellHeight,  # Option
        SupplyRailType = SupplyRailType
        )

        Parameters_TSI2 = dict(
            NMOSWidth=TSI2_NMWidth,
            PMOSWidth=TSI2_PMWidth,
            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType
        )
        Parameters_TSI2_f3 = dict(
            NumFinger_NM1=TSI2_Finger,
            NumFinger_NM2=TSI2_Finger,
            Width_NM1=TSI2_NMWidth,
            Width_NM2=TSI2_NMWidth,
            Width_PM1=TSI2_PMWidth,
            Width_PM2=TSI2_PMWidth,

            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            XVT=XVT,

            CellHeight=CellHeight,  # Option
            SupplyRailType=SupplyRailType
        )

        Parameters_INV1 = dict(
            _Finger=INV1_Finger,
            _ChannelWidth=INV1_NMWidth,
            _ChannelLength=ChannelLength,
            _NPRatio=INV1_PMWidth / INV1_NMWidth,

            _VDD2VSSHeight=CellHeight,
            _VDD2PMOSHeight=None,
            _VSS2NMOSHeight=None,
            _YCoordOfInput=None,

            _Dummy=True,
            _XVT=XVT,
            _GateSpacing=GateSpacing,
            _SDWidth=SDWidth,

            _SupplyRailType=SupplyRailType,
        )

        Parameters_INV2 = dict(
            _Finger=INV2_Finger,
            _ChannelWidth=INV2_NMWidth,
            _ChannelLength=ChannelLength,
            _NPRatio=INV2_PMWidth / INV2_NMWidth,

            _VDD2VSSHeight=CellHeight,
            _VDD2PMOSHeight=None,
            _VSS2NMOSHeight=None,
            _YCoordOfInput=None,

            _Dummy=True,
            _XVT=XVT,
            _GateSpacing=GateSpacing,
            _SDWidth=SDWidth,

            _SupplyRailType=SupplyRailType,
        )

        Parameters_INV3 = dict(
            _Finger=INV3_Finger,
            _ChannelWidth=INV3_NMWidth,
            _ChannelLength=ChannelLength,
            _NPRatio=INV3_PMWidth / INV3_NMWidth,

            _VDD2VSSHeight=CellHeight,
            _VDD2PMOSHeight=None,
            _VSS2NMOSHeight=None,
            _YCoordOfInput=None,

            _Dummy=True,
            _XVT=XVT,
            _GateSpacing=GateSpacing,
            _SDWidth=SDWidth,

            _SupplyRailType=SupplyRailType,
        )

        Parameters_INV4 = dict(
            _Finger=INV4_Finger,
            _ChannelWidth=INV4_NMWidth,
            _ChannelLength=ChannelLength,
            _NPRatio=INV4_PMWidth / INV4_NMWidth,

            _VDD2VSSHeight=CellHeight,
            _VDD2PMOSHeight=None,
            _VSS2NMOSHeight=None,
            _YCoordOfInput=None,

            _Dummy=True,
            _XVT=XVT,
            _GateSpacing=GateSpacing,
            _SDWidth=SDWidth,

            _SupplyRailType=SupplyRailType,
        )
        Parameters_TG3 = dict(
            nmos_gate=TG3_Finger,
            pmos_gate=TG3_Finger,
            nmos_width=TG3_NMWidth,
            pmos_width=TG3_PMWidth,
            length=ChannelLength,
            XVT=XVT,
            vss2vdd_height=CellHeight,
            gate_spacing=GateSpacing,
            sdwidth=SDWidth,
            power_xdistance=UnitPitch,
            #out_even_up_mode=True
        )

        Parameters_TSI3 = dict(
            NMOSWidth=TSI3_NMWidth,
            PMOSWidth=TSI3_PMWidth,
            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType
        )
        Parameters_TSI3_f3 = dict(
            NumFinger_NM1=TSI3_Finger,
            NumFinger_NM2=TSI3_Finger,
            Width_NM1=TSI3_NMWidth,
            Width_NM2=TSI3_NMWidth,
            Width_PM1=TSI3_PMWidth,
            Width_PM2=TSI3_PMWidth,

            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            XVT=XVT,

            CellHeight=CellHeight,  # Option
            SupplyRailType=SupplyRailType
        )
        Parameters_INV5 = dict(
            _Finger=INV5_Finger,
            _ChannelWidth=INV5_NMWidth,
            _ChannelLength=ChannelLength,
            _NPRatio=INV5_PMWidth / INV5_NMWidth,

            _VDD2VSSHeight=CellHeight,
            _VDD2PMOSHeight=None,
            _VSS2NMOSHeight=None,
            _YCoordOfInput=None,

            _Dummy=True,
            _XVT=XVT,
            _GateSpacing=GateSpacing,
            _SDWidth=SDWidth,

            _SupplyRailType=SupplyRailType,
        )
        Parameters_INV6 = dict(
            _Finger=INV6_Finger,
            _ChannelWidth=INV6_NMWidth,
            _ChannelLength=ChannelLength,
            _NPRatio=INV6_PMWidth / INV6_NMWidth,

            _VDD2VSSHeight=CellHeight,
            _VDD2PMOSHeight=None,
            _VSS2NMOSHeight=None,
            _YCoordOfInput=None,

            _Dummy=True,
            _XVT=XVT,
            _GateSpacing=GateSpacing,
            _SDWidth=SDWidth,

            _SupplyRailType=SupplyRailType,
        )

        self._DesignParameter['TG1'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=Transmission_gate.Transmission_gate(_Name='TG1In{}'.format(_Name)))[0]
        self._DesignParameter['TG1']['_DesignObj']._CalculateDesignParameter(**Parameters_TG1)
        self._DesignParameter['TG1']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['TG2'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=Transmission_gate.Transmission_gate(_Name='TG2In{}'.format(_Name)))[0]
        self._DesignParameter['TG2']['_DesignObj']._CalculateDesignParameter(**Parameters_TG2)
        self._DesignParameter['TG2']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['TG3'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=Transmission_gate.Transmission_gate(_Name='TG3In{}'.format(_Name)))[0]
        self._DesignParameter['TG3']['_DesignObj']._CalculateDesignParameter(**Parameters_TG3)
        self._DesignParameter['TG3']['_XYCoordinates'] = [[0, 0]]

        if TSI1_Finger == 1:
            self._DesignParameter['TSI1'] = self._SrefElementDeclaration(
                _Reflect=[0, 0, 0], _Angle=0,
                _DesignObj=TristateInverter.TristateInverter(_Name='TSI1In{}'.format(_Name)))[0]
            self._DesignParameter['TSI1']['_DesignObj']._CalculateDesignParameterFinger1_v2(**Parameters_TSI1)
            self._DesignParameter['TSI1']['_XYCoordinates'] = [[0, 0]]
        elif TSI1_Finger == 2:
            self._DesignParameter['TSI1'] = self._SrefElementDeclaration(
                _Reflect=[0, 0, 0], _Angle=0,
                _DesignObj=TristateInverter.TristateInverter(_Name='TSI1In{}'.format(_Name)))[0]
            self._DesignParameter['TSI1']['_DesignObj']._CalculateDesignParameterFinger2_v2(**Parameters_TSI1)
            self._DesignParameter['TSI1']['_XYCoordinates'] = [[0, 0]]
        elif TSI1_Finger >= 3:
            self._DesignParameter['TSI1'] = self._SrefElementDeclaration(
                _Reflect=[0, 0, 0], _Angle=0,
                _DesignObj=TristateInverter.TristateInverter(_Name='TSI1In{}'.format(_Name)))[0]
            self._DesignParameter['TSI1']['_DesignObj']._CalculateDesignParameterF3(**Parameters_TSI1_f3)
            self._DesignParameter['TSI1']['_XYCoordinates'] = [[0, 0]]

        if TSI2_Finger == 1:
            self._DesignParameter['TSI2'] = self._SrefElementDeclaration(
                _Reflect=[0, 0, 0], _Angle=0,
                _DesignObj=TristateInverter.TristateInverter(_Name='TSI2In{}'.format(_Name)))[0]
            self._DesignParameter['TSI2']['_DesignObj']._CalculateDesignParameterFinger1_v2(**Parameters_TSI2)
            self._DesignParameter['TSI2']['_XYCoordinates'] = [[0, 0]]
        elif TSI2_Finger == 2:
            self._DesignParameter['TSI2'] = self._SrefElementDeclaration(
                _Reflect=[0, 0, 0], _Angle=0,
                _DesignObj=TristateInverter.TristateInverter(_Name='TSI2In{}'.format(_Name)))[0]
            self._DesignParameter['TSI2']['_DesignObj']._CalculateDesignParameterFinger2_v2(**Parameters_TSI2)
            self._DesignParameter['TSI2']['_XYCoordinates'] = [[0, 0]]
        elif TSI2_Finger >= 3:
            self._DesignParameter['TSI2'] = self._SrefElementDeclaration(
                _Reflect=[0, 0, 0], _Angle=0,
                _DesignObj=TristateInverter.TristateInverter(_Name='TSI2In{}'.format(_Name)))[0]
            self._DesignParameter['TSI2']['_DesignObj']._CalculateDesignParameterF3(**Parameters_TSI2_f3)
            self._DesignParameter['TSI2']['_XYCoordinates'] = [[0, 0]]

        if TSI3_Finger == 1:
            self._DesignParameter['TSI3'] = self._SrefElementDeclaration(
                _Reflect=[0, 0, 0], _Angle=0,
                _DesignObj=TristateInverter.TristateInverter(_Name='TSI3In{}'.format(_Name)))[0]
            self._DesignParameter['TSI3']['_DesignObj']._CalculateDesignParameterFinger1_v2(**Parameters_TSI3)
            self._DesignParameter['TSI3']['_XYCoordinates'] = [[0, 0]]
        elif TSI3_Finger == 2:
            self._DesignParameter['TSI3'] = self._SrefElementDeclaration(
                _Reflect=[0, 0, 0], _Angle=0,
                _DesignObj=TristateInverter.TristateInverter(_Name='TSI3In{}'.format(_Name)))[0]
            self._DesignParameter['TSI3']['_DesignObj']._CalculateDesignParameterFinger2_v2(**Parameters_TSI3)
            self._DesignParameter['TSI3']['_XYCoordinates'] = [[0, 0]]
        elif TSI3_Finger >= 3:
            self._DesignParameter['TSI3'] = self._SrefElementDeclaration(
                _Reflect=[0, 0, 0], _Angle=0,
                _DesignObj=TristateInverter.TristateInverter(_Name='TSI3In{}'.format(_Name)))[0]
            self._DesignParameter['TSI3']['_DesignObj']._CalculateDesignParameterF3(**Parameters_TSI3_f3)
            self._DesignParameter['TSI3']['_XYCoordinates'] = [[0, 0]]



        self._DesignParameter['INV1'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=Inverter._Inverter(_Name='INV1In{}'.format(_Name)))[0]
        self._DesignParameter['INV1']['_DesignObj']._CalculateDesignParameter_v3(**Parameters_INV1)
        self._DesignParameter['INV1']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['INV2'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=Inverter._Inverter(_Name='INV2In{}'.format(_Name)))[0]
        self._DesignParameter['INV2']['_DesignObj']._CalculateDesignParameter_v3(**Parameters_INV2)
        self._DesignParameter['INV2']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['INV3'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=Inverter._Inverter(_Name='INV3In{}'.format(_Name)))[0]
        self._DesignParameter['INV3']['_DesignObj']._CalculateDesignParameter_v3(**Parameters_INV3)
        self._DesignParameter['INV3']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['INV4'] = self._SrefElementDeclaration(
            _Reflect=[1, 0, 0], _Angle=180,
            _DesignObj=Inverter._Inverter(_Name='INV4In{}'.format(_Name)))[0]
        self._DesignParameter['INV4']['_DesignObj']._CalculateDesignParameter_v3(**Parameters_INV4)
        self._DesignParameter['INV4']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['INV5'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=Inverter._Inverter(_Name='INV5In{}'.format(_Name)))[0]
        self._DesignParameter['INV5']['_DesignObj']._CalculateDesignParameter_v3(**Parameters_INV5)
        self._DesignParameter['INV5']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['INV6'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=Inverter._Inverter(_Name='INV6In{}'.format(_Name)))[0]
        self._DesignParameter['INV6']['_DesignObj']._CalculateDesignParameter_v3(**Parameters_INV6)
        self._DesignParameter['INV6']['_XYCoordinates'] = [[0, 0]]


        #
        self._DesignParameter['TG1']['_XYCoordinates'] = [[self._DesignParameter['TG1']['_DesignObj'].CellXWidth / 2, 0]]
        if INV1_Finger >= 3:
            self._DesignParameter['INV1']['_XYCoordinates'] = [
                [self.getXY('TG1')[0][0] + self._DesignParameter['TG1']['_DesignObj'].CellXWidth / 2 + self._DesignParameter['INV1']['_DesignObj'].CellXWidth / 2, 0]
            ]
        else:
            self._DesignParameter['INV1']['_XYCoordinates'] = [
                [self.getXY('TG1')[0][0] + self._DesignParameter['TG1']['_DesignObj'].CellXWidth / 2 + 2 * UnitPitch + self._DesignParameter['INV1']['_DesignObj'].CellXWidth / 2, 0]
            ]
        self._DesignParameter['TSI1']['_XYCoordinates'] = [
            [self.getXY('INV1')[0][0] + self._DesignParameter['INV1']['_DesignObj'].CellXWidth / 2 + 2 * UnitPitch + self._DesignParameter['TSI1']['_DesignObj'].CellXWidth / 2, 0]
        ]
        self._DesignParameter['TG2']['_XYCoordinates'] = [
            [self.getXY('TSI1')[0][0] + self._DesignParameter['TSI1']['_DesignObj'].CellXWidth / 2 + 1 * UnitPitch + self._DesignParameter['TG2']['_DesignObj'].CellXWidth / 2, 0]
        ]
        self._DesignParameter['INV2']['_XYCoordinates'] = [
            [self.getXY('TG2')[0][0] + self._DesignParameter['TG2']['_DesignObj'].CellXWidth / 2 + 1 * UnitPitch + self._DesignParameter['INV2']['_DesignObj'].CellXWidth / 2, 0]
        ]
        self._DesignParameter['INV3']['_XYCoordinates'] = [
            [self.getXY('INV2')[0][0] + self._DesignParameter['INV2']['_DesignObj'].CellXWidth / 2 + self._DesignParameter['INV3']['_DesignObj'].CellXWidth / 2, 0]
        ]
        self._DesignParameter['TSI2']['_XYCoordinates'] = [
            [self.getXY('INV3')[0][0] + self._DesignParameter['INV3']['_DesignObj'].CellXWidth / 2 + 2 * UnitPitch + self._DesignParameter['TSI2']['_DesignObj'].CellXWidth / 2, 0]
        ]
        self._DesignParameter['INV4']['_XYCoordinates'] = [
            [self.getXY('TSI2')[0][0] + self._DesignParameter['TSI2']['_DesignObj'].CellXWidth / 2 + 1 * UnitPitch + self._DesignParameter['INV4']['_DesignObj'].CellXWidth / 2, 0]
        ]
        self._DesignParameter['TG3']['_XYCoordinates'] = [
            [self.getXY('INV4')[0][0] + self._DesignParameter['INV4']['_DesignObj'].CellXWidth / 2 + 1 * UnitPitch + self._DesignParameter['TG3']['_DesignObj'].CellXWidth / 2, 0]
        ]
        if INV5_Finger >= 3:
            self._DesignParameter['INV5']['_XYCoordinates'] = [
                [self.getXY('TG3')[0][0] + self._DesignParameter['TG3']['_DesignObj'].CellXWidth / 2 + self._DesignParameter['INV5']['_DesignObj'].CellXWidth / 2, 0]
            ]
        else:
            self._DesignParameter['INV5']['_XYCoordinates'] = [
                [self.getXY('TG3')[0][0] + self._DesignParameter['TG3']['_DesignObj'].CellXWidth / 2 + 2 * UnitPitch + self._DesignParameter['INV5']['_DesignObj'].CellXWidth / 2, 0]
            ]
        self._DesignParameter['TSI3']['_XYCoordinates'] = [
            [self.getXY('INV5')[0][0] + self._DesignParameter['INV5']['_DesignObj'].CellXWidth / 2 + 2 * UnitPitch + self._DesignParameter['TSI3']['_DesignObj'].CellXWidth / 2, 0]
        ]
        self._DesignParameter['INV6']['_XYCoordinates'] = [
            [self.getXY('TSI3')[0][0] + self._DesignParameter['TSI3']['_DesignObj'].CellXWidth / 2  + 1 * UnitPitch + self._DesignParameter['INV6']['_DesignObj'].CellXWidth / 2, 0]
        ]

        ''' VDD Rail, VSS Rail, XVTLayer '''
        # VSS M2
        leftBoundary = self.getXYLeft('TG1', 'vss_supply_m2_y')[0][0]
        rightBoundary = self.getXYRight('INV6', 'PbodyContact', '_Met2Layer')[0][0]
        self._DesignParameter['VSSRail_Met2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('INV6', 'PbodyContact', '_Met2Layer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, 0]]
        )
        # VSS OD(RX)
        leftBoundary = self.getXYLeft('TG1', 'vss_odlayer')[0][0]
        rightBoundary = self.getXYRight('INV6', 'PbodyContact', '_ODLayer')[0][0]
        self._DesignParameter['VSSRail_OD'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('INV6', 'PbodyContact', '_ODLayer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, 0]]
        )
        # VSS PP(BP)
        leftBoundary = self.getXYLeft('TG1', 'vss_pplayer')[0][0]
        rightBoundary = self.getXYRight('INV6', 'PbodyContact', '_PPLayer')[0][0]
        self._DesignParameter['VSSRail_PP'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('INV6', 'PbodyContact', '_PPLayer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, 0]]
        )
        ## VDD
        # VDD M2
        leftBoundary = self.getXYLeft('TG1', 'vdd_supply_m2_y')[0][0]
        rightBoundary = self.getXYRight('INV6', 'NbodyContact', '_Met2Layer')[0][0]
        self._DesignParameter['VDDRail_Met2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('INV6', 'NbodyContact', '_Met2Layer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY('INV6', 'NbodyContact', '_Met2Layer')[0][1]]]
        )
        # VDD OD(RX)
        leftBoundary = self.getXYLeft('TG1', 'vdd_odlayer')[0][0]
        rightBoundary = self.getXYRight('INV6', 'NbodyContact', '_ODLayer')[0][0]
        self._DesignParameter['VDDRail_OD'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('INV6', 'NbodyContact', '_ODLayer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY('INV6', 'NbodyContact', '_ODLayer')[0][1]]]
        )

        # NWLayer
        leftBoundary = self.getXYLeft('TG1', 'NWELL_boundary_0')[0][0]
        rightBoundary = self.getXYRight('INV6', '_NWLayerBoundary')[0][0]
        topBoundary = max(
            self.getXYTop('TG1', 'NWELL_boundary_0')[0][1],
            self.getXYTop('TG2', 'NWELL_boundary_0')[0][1],
            self.getXYTop('TSI1', 'nwlayer')[0][1],
            self.getXYTop('TSI2', 'nwlayer')[0][1],
            self.getXYTop('INV1', '_NWLayerBoundary')[0][1],
            self.getXYTop('INV2', '_NWLayerBoundary')[0][1],
            self.getXYTop('INV3', '_NWLayerBoundary')[0][1],
            self.getXYTop('INV4', '_NWLayerBoundary')[0][1],
            self.getXYTop('TG3', 'NWELL_boundary_0')[0][1],
            self.getXYTop('TSI3', 'nwlayer')[0][1],
            self.getXYTop('INV5', '_NWLayerBoundary')[0][1],
            self.getXYTop('INV6', '_NWLayerBoundary')[0][1]
        )
        botBoundary = min(
            self.getXYBot('TG1', 'NWELL_boundary_0')[0][1],
            self.getXYBot('TG2', 'NWELL_boundary_0')[0][1],
            self.getXYBot('TSI1', 'nwlayer')[0][1],
            self.getXYBot('TSI2', 'nwlayer')[0][1],
            self.getXYBot('INV1', '_NWLayerBoundary')[0][1],
            self.getXYBot('INV2', '_NWLayerBoundary')[0][1],
            self.getXYBot('INV3', '_NWLayerBoundary')[0][1],
            self.getXYBot('INV4', '_NWLayerBoundary')[0][1],
            self.getXYTop('TG3', 'NWELL_boundary_0')[0][1],
            self.getXYTop('TSI3', 'nwlayer')[0][1],
            self.getXYTop('INV5', '_NWLayerBoundary')[0][1],
            self.getXYTop('INV6', '_NWLayerBoundary')[0][1]
        )
        self._DesignParameter['_NWLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=topBoundary - botBoundary,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, (topBoundary + botBoundary) / 2]]
        )

        # PPLayer (ADDED by smlim)
        leftBoundary = self.getXYLeft('TG1', 'pmos', '_PPLayer')[0][0]
        rightBoundary = self.getXYRight('INV6', '_PMOS', '_PPLayer')[0][0]
        if TSI1_Finger >= 3:
            topboundary_TSI1 = self.getXYTop('TSI1', 'PM1', '_PPLayer')[0][1]
            botboundary_TSI1 = self.getXYBot('TSI1', 'PM1', '_PPLayer')[0][1]
        else:
            topboundary_TSI1 = self.getXYTop('TSI1', 'PMOS', '_PPLayer')[0][1]
            botboundary_TSI1 = self.getXYBot('TSI1', 'PMOS', '_PPLayer')[0][1]
        if TSI2_Finger >= 3:
            topboundary_TSI2 = self.getXYTop('TSI2', 'PM1', '_PPLayer')[0][1]
            botboundary_TSI2 = self.getXYBot('TSI2', 'PM1', '_PPLayer')[0][1]
        else:
            topboundary_TSI2 = self.getXYTop('TSI2', 'PMOS', '_PPLayer')[0][1]
            botboundary_TSI2 = self.getXYBot('TSI2', 'PMOS', '_PPLayer')[0][1]

        # if TSI1_Finger >= 3:
        #     topboundary_TSI3 = self.getXYTop('TSI3', 'PM1', '_PPLayer')[0][1]
        #     botboundary_TSI3 = self.getXYBot('TSI3', 'PM1', '_PPLayer')[0][1]
        # else:
        #     topboundary_TSI3 = self.getXYTop('TSI3', 'PMOS', '_PPLayer')[0][1]
        #     botboundary_TSI3 = self.getXYBot('TSI3', 'PMOS', '_PPLayer')[0][1]

        topBoundary = max(
            self.getXYTop('TG1', 'pmos', '_PPLayer')[0][1],
            self.getXYTop('TG2', 'pmos', '_PPLayer')[0][1],
            self.getXYTop('TG3', 'pmos', '_PPLayer')[0][1],
            topboundary_TSI1,
            topboundary_TSI2,
           # topboundary_TSI3,
            self.getXYTop('INV1', '_PMOS', '_PPLayer')[0][1],
            self.getXYTop('INV2', '_PMOS', '_PPLayer')[0][1],
            self.getXYTop('INV3', '_PMOS', '_PPLayer')[0][1],
            self.getXYTop('INV4', '_PMOS', '_PPLayer')[0][1],
            self.getXYTop('INV5', '_PMOS', '_PPLayer')[0][1],
            self.getXYTop('INV6', '_PMOS', '_PPLayer')[0][1],
        )
        botBoundary = min(
            self.getXYTop('TG1', 'pmos', '_PPLayer')[0][1],
            self.getXYTop('TG2', 'pmos', '_PPLayer')[0][1],
            self.getXYTop('TG3', 'pmos', '_PPLayer')[0][1],
            botboundary_TSI1,
            botboundary_TSI2,
        #    botboundary_TSI3,
            self.getXYTop('INV1', '_PMOS', '_PPLayer')[0][1],
            self.getXYTop('INV2', '_PMOS', '_PPLayer')[0][1],
            self.getXYTop('INV3', '_PMOS', '_PPLayer')[0][1],
            self.getXYTop('INV4', '_PMOS', '_PPLayer')[0][1],
            self.getXYTop('INV5', '_PMOS', '_PPLayer')[0][1],
            self.getXYTop('INV6', '_PMOS', '_PPLayer')[0][1],
        )

        self._DesignParameter['_PPLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=topBoundary - botBoundary,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, (topBoundary + botBoundary) / 2]]
        )
        self._DesignParameter['TG1']['_DesignObj']._DesignParameter['vss_pplayer']['_YWidth'] = self.getYWidth('INV1', 'PbodyContact', '_PPLayer')
        self._DesignParameter['TG2']['_DesignObj']._DesignParameter['vss_pplayer']['_YWidth'] = self.getYWidth('INV1', 'PbodyContact', '_PPLayer')
        self._DesignParameter['TG3']['_DesignObj']._DesignParameter['vss_pplayer']['_YWidth'] = self.getYWidth('INV1', 'PbodyContact', '_PPLayer')





        # XVTLayer
        assert XVT in ('SLVT', 'LVT', 'RVT', 'HVT')
        leftBoundary = self.getXYLeft('TG1', 'XVT_boundary_1')[0][0]
        rightBoundary = self.getXYRight('INV6', 'XVTLayer')[0][0]
        self._DesignParameter['XVTLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[XVT][0], _Datatype=DesignParameters._LayerMapping[XVT][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('INV6', 'XVTLayer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY('INV6', 'XVTLayer')[0][1]]]
        )

        '''dib routing '''
        tmpMet2Width = 66
        tmpDRC_Met2Spacing = 86
        tmpVia1YWidth = 100
        tmpViaMet2Width = 134

        leftBoundary = self.getXY('TG1')[0][0] + self._DesignParameter['TG1']['_DesignObj']._DesignParameter['m1_drain_routing_y']['_XYCoordinates'][-1][0][0] - self.getWidth('TG1', 'm1_drain_routing_y') / 2
        if INV1_Finger <= 2:
            YCoord_dib = self.getXYTop('INV1', '_NMOS', '_Met1Layer')[0][1] + tmpDRC_Met2Spacing + tmpMet2Width / 2

        elif INV1_Finger >= 3:
            YCoord_dib = self.getXYTop('INV1', '_ViaMet12Met2OnNMOSOutput', '_Met2Layer')[0][1] + tmpDRC_Met2Spacing + tmpMet2Width / 2

        if TSI1_Finger == 1:
            rightBoundary2 = self.getXY('TSI1')[0][0] + self.getWidth('TSI1', 'OutputRouting') / 2
        elif TSI1_Finger == 2:
            rightBoundary2 = self.getXYRight('TSI1', 'met1_output_5')[0][0]
            if INV1_Finger >= 3:
                YCoord_dib = self.getXYTop('INV1', '_ViaMet12Met2OnNMOSOutput', '_Met2Layer')[0][1] + tmpDRC_Met2Spacing + tmpMet2Width / 2
            else:
                YCoord_dib = self.getXYBot('TSI1', 'met1_output_5')[0][1] + tmpViaMet2Width - tmpMet2Width / 2
        elif TSI1_Finger >= 3:
            rightBoundary2 = self.getXYRight('TSI1', 'Met1RouteY_Out')[0][0]
            YCoord_dib = self.getXYTop('TSI1', 'via1ForNM2', '_Met2Layer')[0][1] + drc._Metal1MinSpace2 + tmpMet2Width / 2

        # TG1y to TSI1out
        self._DesignParameter['_Met2_dib'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=rightBoundary2 - leftBoundary,
            _YWidth=tmpMet2Width,
            _XYCoordinates=[[(rightBoundary2 + leftBoundary) / 2, YCoord_dib]]
        )

        # insert via
        self._DesignParameter['_ViaMet12Met2dib'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_ViaMet12Met2dibIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2dib']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=1))
        self._DesignParameter['_ViaMet12Met2dib']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet12Met2dib']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = tmpVia1YWidth
        self._DesignParameter['_ViaMet12Met2dib']['_XYCoordinates'] = [[self.getXYLeft('_Met2_dib')[0][0] + tmpMet2Width / 2, self.getXY('_Met2_dib')[0][1] + tmpViaMet2Width / 2 - tmpMet2Width / 2],
                                                                       [self.getXYRight('_Met2_dib')[0][0] - tmpMet2Width / 2, self.getXY('_Met2_dib')[0][1] - tmpViaMet2Width / 2 + tmpMet2Width / 2]]

        # Additional routing
        if INV1_Finger <= 2:
            self._DesignParameter['_Met1_dib_add'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _Width=self.getXWidth('INV1', '_VIAPoly2Met1_F1', '_Met1Layer'),
                _XYCoordinates=[[[self.getXY('INV1', '_VIAPoly2Met1_F1', '_Met1Layer')[0][0], self.getXYBot('_Met2_dib')[0][1]],
                                 [self.getXY('INV1', '_VIAPoly2Met1_F1', '_Met1Layer')[0][0], self.getXYTop('INV1', '_VIAPoly2Met1_F1', '_Met1Layer')[0][1]]]]
            )
            self._DesignParameter['_ViaMet12Met2dib']['_XYCoordinates'].append([self.getXY('INV1', '_VIAPoly2Met1_F1', '_Met1Layer')[0][0], self.getXY('_Met2_dib')[0][1] + tmpViaMet2Width / 2 - tmpMet2Width / 2])
        else:
            self._DesignParameter['_ViaMet12Met2dib']['_XYCoordinates'].append([self.getXY('INV1')[0][0] + self._DesignParameter['INV1']['_DesignObj']._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][0], tmpViaMet2Width / 2 + (self.getXYTop('INV1', '_ViaMet12Met2OnNMOSOutput', '_Met2Layer')[0][1] - drc._MetalxMinEnclosureVia3 + drc._VIAzMinEnclosureByMetxOrMety + drc._VIAyMinSpace - (self.getXYBot('_ViaMet12Met2dib', '_COLayer')[0][1] - self.getXYBot('_ViaMet12Met2dib', '_Met2Layer')[0][1]))])

        if TSI1_Finger == 2:
            self._DesignParameter['_Met1_dib_add2'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=tmpMet2Width,
                _YWidth=self.getYWidth('TSI1', 'met1_output_5'),
                _XYCoordinates=[[self.getXYRight('TSI1', 'met1_output_5')[0][0] - tmpMet2Width / 2, self.getXY('TSI1', 'met1_output_5')[0][1]]]
            )

        '''dib routing (added by jwlee)'''
        leftBoundary = self.getXY('TG3')[0][0] + self._DesignParameter['TG3']['_DesignObj']._DesignParameter['m1_drain_routing_y']['_XYCoordinates'][-1][0][0] - self.getWidth('TG3', 'm1_drain_routing_y') / 2
        if INV5_Finger <= 2:
            YCoord_dib2 = self.getXYTop('INV5', '_NMOS', '_Met1Layer')[0][1] + tmpDRC_Met2Spacing + tmpMet2Width / 2

        elif INV5_Finger >= 3:
            YCoord_dib2 = self.getXYTop('INV5', '_ViaMet12Met2OnNMOSOutput', '_Met2Layer')[0][1] + tmpDRC_Met2Spacing + tmpMet2Width / 2

        if TSI3_Finger == 1:
            rightBoundary2 = self.getXY('TSI3')[0][0] + self.getWidth('TSI3', 'OutputRouting') / 2
        elif TSI3_Finger == 2:
            rightBoundary2 = self.getXYRight('TSI3', 'met1_output_5')[0][0]
            if INV5_Finger >= 3:
                YCoord_dib2 = self.getXYTop('INV5', '_ViaMet12Met2OnNMOSOutput', '_Met2Layer')[0][1] + tmpDRC_Met2Spacing + tmpMet2Width / 2
            else:
                YCoord_dib2 = self.getXYBot('TSI3', 'met1_output_5')[0][1] + tmpViaMet2Width - tmpMet2Width / 2
        elif TSI3_Finger >= 3:
            rightBoundary2 = self.getXYRight('TSI3', 'Met1RouteY_Out')[0][0]
            YCoord_dib2 = self.getXYTop('TSI3', 'via1ForNM2', '_Met2Layer')[0][1] + drc._Metal1MinSpace2 + tmpMet2Width / 2

        # TG3y to TSI3out
        self._DesignParameter['_Met2_dib_latch'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=rightBoundary2 - leftBoundary,
            _YWidth=tmpMet2Width,
            _XYCoordinates=[[(rightBoundary2 + leftBoundary) / 2, YCoord_dib2]]
        )

        # insert via (latch)
        self._DesignParameter['_ViaMet12Met2dib_latch'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_ViaMet12Met2dib_latchIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2dib_latch']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=1))
        self._DesignParameter['_ViaMet12Met2dib_latch']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet12Met2dib_latch']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet12Met2dib_latch']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = tmpVia1YWidth
        self._DesignParameter['_ViaMet12Met2dib_latch']['_XYCoordinates'] = [[self.getXYLeft('_Met2_dib_latch')[0][0] + tmpMet2Width / 2, self.getXY('_Met2_dib_latch')[0][1] + tmpViaMet2Width / 2 - tmpMet2Width / 2],
                                                                       [self.getXYRight('_Met2_dib_latch')[0][0] - tmpMet2Width / 2, self.getXY('_Met2_dib_latch')[0][1] - tmpViaMet2Width / 2 + tmpMet2Width / 2]]

        # Additional routing(latch)
        if INV5_Finger <= 2:
            self._DesignParameter['_Met1_dib_add_latch'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _Width=self.getXWidth('INV5', '_VIAPoly2Met1_F1', '_Met1Layer'),
                _XYCoordinates=[[[self.getXY('INV5', '_VIAPoly2Met1_F1', '_Met1Layer')[0][0], self.getXYBot('_Met2_dib_latch')[0][1]],
                                 [self.getXY('INV5', '_VIAPoly2Met1_F1', '_Met1Layer')[0][0], self.getXYTop('INV5', '_VIAPoly2Met1_F1', '_Met1Layer')[0][1]]]]
            )
            self._DesignParameter['_ViaMet12Met2dib_latch']['_XYCoordinates'].append([self.getXY('INV5', '_VIAPoly2Met1_F1', '_Met1Layer')[0][0], self.getXY('_Met2_dib_latch')[0][1] + tmpViaMet2Width / 2 - tmpMet2Width / 2])
        else:
            self._DesignParameter['_ViaMet12Met2dib_latch']['_XYCoordinates'].append([self.getXY('INV5')[0][0] + self._DesignParameter['INV5']['_DesignObj']._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][0], tmpViaMet2Width / 2 + (self.getXYTop('INV5', '_ViaMet12Met2OnNMOSOutput', '_Met2Layer')[0][1] - drc._MetalxMinEnclosureVia3 + drc._VIAzMinEnclosureByMetxOrMety + drc._VIAyMinSpace - (self.getXYBot('_ViaMet12Met2dib_latch', '_COLayer')[0][1] - self.getXYBot('_ViaMet12Met2dib_latch', '_Met2Layer')[0][1]))])

        if TSI3_Finger == 2:
            self._DesignParameter['_Met1_dib_add2_latch'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=tmpMet2Width,
                _YWidth=self.getYWidth('TSI3', 'met1_output_5'),
                _XYCoordinates=[[self.getXYRight('TSI3', 'met1_output_5')[0][0] - tmpMet2Width / 2, self.getXY('TSI3', 'met1_output_5')[0][1]]]
            )

        ''''dib Routing1 end'''

        # '''iclkb routing(ADDED by smlim)'''
        leftBoundary = self.getXYLeft('TG1', 'gate_output', '_Met1Layer')[0][0]
        if TSI2_Finger == 1:
            rightBoundary = self.getXYRight('TSI2', 'InputVia_EN', '_Met1Layer')[0][0]
            YCoord_iclkb = self.getXYBot('TG2', 'gate_input', '_Met1Layer')[0][1]
        elif TSI2_Finger == 2:
            rightBoundary = self.getXYLeft('TSI2', 'InputVia_EN', '_Met1Layer')[0][0] + tmpMet2Width
            YCoord_iclkb = self.getXYBot('TG2', 'gate_input', '_Met1Layer')[0][1]
        elif TSI2_Finger >= 3:
            rightBoundary = self.getXYLeft('TSI2', 'polyInputEN', '_Met1Layer')[0][0] + tmpMet2Width
            YCoord_iclkb = self.getXYBot('TG2', 'gate_input', '_Met1Layer')[0][1] + tmpMet2Width / 2


        # TG1en to TSI2en
        self._DesignParameter['_Met2_iclkb'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=tmpMet2Width,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, YCoord_iclkb]]
        )
        self._DesignParameter['_Met1_iclkb'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met1_iclkb']['_XYCoordinates'] = [[[self.getXYLeft('_Met2_iclkb')[0][0] + tmpMet2Width / 2, self.getXYBot('_Met2_iclkb')[0][1]], [self.getXYLeft('_Met2_iclkb')[0][0] + tmpMet2Width / 2, self.getXYTop('TG1', 'gate_output', '_Met1Layer')[0][1]]], # to TG1en
                                                                  [[self.getXY('TG2', 'gate_input', '_Met1Layer')[0][0], self.getXYBot('_Met2_iclkb')[0][1]], [self.getXY('TG2', 'gate_input', '_Met1Layer')[0][0], self.getXYTop('TG2', 'gate_input', '_Met1Layer')[0][1]]]] # to TG2enb
        if TSI1_Finger == 1:
            xCoordOfInputViaENandENb = - self.getXWidth('TSI1', 'NMOS', '_Met1Layer') / 2 - drc._Metal1MinSpaceAtCorner - self.getXWidth('TSI1', 'InputVia_ENb', '_Met1Layer') / 2
            self._DesignParameter['_Met1_iclkb']['_XYCoordinates'].append([[self.getXY('TSI1', 'InputVia_ENb', '_Met1Layer')[0][0] + xCoordOfInputViaENandENb, self.getXYBot('_Met2_iclkb')[0][1]],
                                                                            [self.getXY('TSI1', 'InputVia_ENb', '_Met1Layer')[0][0] + xCoordOfInputViaENandENb, self.getXYBot('TSI1', 'InputVia_ENb', '_Met1Layer')[0][1] + tmpMet2Width / 2],
                                                                            [self.getXYRight('TSI1', 'InputVia_ENb', '_Met1Layer')[0][0] ,self.getXYBot('TSI1', 'InputVia_ENb', '_Met1Layer')[0][1] + tmpMet2Width / 2]]) # to TSI1enb
        elif TSI1_Finger == 2:
            self._DesignParameter['_Met1_iclkb']['_XYCoordinates'].append([[self.getXYRight('TSI1', 'InputVia_ENb', '_Met1Layer')[0][0] - tmpMet2Width / 2, self.getXYBot('_Met2_iclkb')[0][1]],
                                                                            [self.getXYRight('TSI1', 'InputVia_ENb', '_Met1Layer')[0][0] - tmpMet2Width / 2, self.getXYTop('TSI1', 'InputVia_ENb', '_Met1Layer')[0][1]]])  # to TSI1enb
        elif TSI1_Finger >= 3:
            self._DesignParameter['_Met1_iclkb']['_XYCoordinates'].append([[self.getXYLeft('TSI1', 'polyInputA', '_Met1Layer')[0][0] - drc._Metal1MinSpace2 - tmpMet2Width / 2, self.getXYBot('_Met2_iclkb')[0][1]],
                                                                           [self.getXYLeft('TSI1', 'polyInputA', '_Met1Layer')[0][0] - drc._Metal1MinSpace2 - tmpMet2Width / 2, self.getXYTop('_Met2_iclkb')[0][1] + tmpViaMet2Width + drc._Metal1MinSpace2 * 2 + tmpViaMet2Width - tmpMet2Width / 2],
                                                                           [self.getXY('TSI1', 'polyInputA', '_Met1Layer')[0][0] + drc._Metal1MinSpace2 + tmpMet2Width / 2, self.getXYTop('_Met2_iclkb')[0][1] + tmpViaMet2Width + drc._Metal1MinSpace2 * 2 + tmpViaMet2Width - tmpMet2Width / 2],
                                                                           [self.getXY('TSI1', 'polyInputA', '_Met1Layer')[0][0] + drc._Metal1MinSpace2 + tmpMet2Width / 2, self.getXYTop('TSI1', 'polyInputENb', '_Met1Layer')[0][1] - tmpMet2Width / 2],
                                                                           [self.getXYRight('TSI1', 'polyInputENb', '_Met1Layer')[0][0], self.getXYTop('TSI1', 'polyInputENb', '_Met1Layer')[0][1] - tmpMet2Width / 2]])  # to TSI1enb

        if TSI2_Finger == 1:
            self._DesignParameter['_Met1_iclkb']['_XYCoordinates'].append([[self.getXY('TSI2', 'InputVia_EN', '_Met1Layer')[0][0], self.getXYTop('_Met2_iclkb')[0][1]],
                                                                           [self.getXY('TSI2', 'InputVia_EN', '_Met1Layer')[0][0], self.getXYBot('TSI2', 'InputVia_EN', '_Met1Layer')[0][1]]])
        elif TSI2_Finger == 2:
            self._DesignParameter['_Met1_iclkb']['_XYCoordinates'].append([[self.getXYLeft('TSI2', 'InputVia_EN', '_Met1Layer')[0][0] + tmpMet2Width / 2, self.getXYTop('_Met2_iclkb')[0][1]],
                                                                            [self.getXYLeft('TSI2', 'InputVia_EN', '_Met1Layer')[0][0] + tmpMet2Width / 2, self.getXYBot('TSI2', 'InputVia_EN', '_Met1Layer')[0][1]]])
        elif TSI2_Finger >= 3:
            self._DesignParameter['_Met1_iclkb']['_XYCoordinates'].append([[self.getXYLeft('TSI2', 'polyInputEN', '_Met1Layer')[0][0] + tmpMet2Width / 2, self.getXYTop('_Met2_iclkb')[0][1]],
                                                                            [self.getXYLeft('TSI2', 'polyInputEN', '_Met1Layer')[0][0] + tmpMet2Width / 2, self.getXYBot('TSI2', 'polyInputEN', '_Met1Layer')[0][1]]])

        if INV3_Finger >= 3:
            self._DesignParameter['_Met1_iclkb']['_XYCoordinates'].append([[self.getXY('INV2')[0][0] + self._DesignParameter['INV2']['_DesignObj']._DesignParameter['_OutputRouting']['_XYCoordinates'][-1][0][0] - self.getWidth('INV2', '_OutputRouting') / 2, self.getXY('INV3')[0][1] + (self._DesignParameter['INV3']['_DesignObj']._DesignParameter['_InputRouting']['_XYCoordinates'][0][1][1] + self._DesignParameter['INV3']['_DesignObj']._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][1]) / 2],
                                                                           [self.getXYLeft('INV3', '_VIAMOSPoly2Met1LeftMost', '_Met1Layer')[0][0] + tmpMet2Width, self.getXY('INV3')[0][1] + (self._DesignParameter['INV3']['_DesignObj']._DesignParameter['_InputRouting']['_XYCoordinates'][0][1][1] + self._DesignParameter['INV3']['_DesignObj']._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][1]) / 2]]) # inputrouting 잡아서 가운데 좌표로 y 좌표 세팅
        else:
            self._DesignParameter['_Met1_iclkb']['_XYCoordinates'].append([[self.getXYRight('INV3', '_VIAPoly2Met1_F1', '_Met1Layer')[0][0], self.getXY('INV3', '_VIAPoly2Met1_F1', '_Met1Layer')[0][1]],
                                                                           [self.getXY('INV2')[0][0] + self._DesignParameter['INV2']['_DesignObj']._DesignParameter['_OutputRouting']['_XYCoordinates'][-1][0][0] - self.getWidth('INV2', '_OutputRouting') / 2, self.getXY('INV3', '_VIAPoly2Met1_F1', '_Met1Layer')[0][1]]])


        # insert via
        self._DesignParameter['_ViaMet12Met2iclkb'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_ViaMet12Met2iclkbIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2iclkb']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=1))
        self._DesignParameter['_ViaMet12Met2iclkb']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet12Met2iclkb']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet12Met2iclkb']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = tmpVia1YWidth
        self._DesignParameter['_ViaMet12Met2iclkb']['_XYCoordinates'] = [[self.getXYLeft('_Met2_iclkb')[0][0] + tmpMet2Width / 2, self.getXY('_Met2_iclkb')[0][1] + tmpViaMet2Width / 2 - tmpMet2Width / 2], # TG1 EN
                                                                         [self._DesignParameter['_Met1_iclkb']['_XYCoordinates'][2][0][0], self.getXY('_Met2_iclkb')[0][1] + tmpViaMet2Width / 2 - tmpMet2Width / 2], # TSI1 ENb
                                                                         [self._DesignParameter['_Met1_iclkb']['_XYCoordinates'][1][0][0], self.getXY('_Met2_iclkb')[0][1] + tmpViaMet2Width / 2 - tmpMet2Width / 2], # TG2 ENb
                                                                         [self.getXY('INV2')[0][0] + self._DesignParameter['INV2']['_DesignObj']._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][0], self.getXY('_Met2_iclkb')[0][1] - tmpViaMet2Width / 2 + tmpMet2Width / 2], # INV2 out
                                                                         [self.getXYRight('_Met2_iclkb')[0][0] - tmpMet2Width / 2, self.getXY('_Met2_iclkb')[0][1] - tmpViaMet2Width / 2 + tmpMet2Width / 2]] # TSI2 EN

        '''iclkb routing (ADDED by jw)'''

        self._DesignParameter['_Met2_iclkb_latch2'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met2_iclkb_latch2']['_XYCoordinates'] = [[[rightBoundary, YCoord_iclkb],
                                                                  [self.getXYRight('TG3', 'gate_output', '_Met1Layer')[0][0], YCoord_iclkb]]]

        # TG1en to TSI2en
        self._DesignParameter['_Met1_iclkb_latch'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _Width=tmpMet2Width
        )

        leftBoundary = self.getXYLeft('TG3', 'gate_output', '_Met1Layer')[0][0]
        rightBoundary = self.getXYRight('TSI3', 'InputVia_EN', '_Met1Layer')[0][0]

        self._DesignParameter['_Met2_iclkb_latch'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=tmpMet2Width,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, YCoord_iclkb]]
        )

        self._DesignParameter['_Met1_iclkb_latch']['_XYCoordinates'] = [[[self.getXYLeft('_Met2_iclkb_latch')[0][0] + tmpMet2Width / 2, self.getXYBot('_Met2_iclkb_latch')[0][1]], [self.getXYLeft('_Met2_iclkb_latch')[0][0] + tmpMet2Width / 2, self.getXYTop('TG3', 'gate_output', '_Met1Layer')[0][1]]]] # to TG1en

        if TSI3_Finger == 1:
            xCoordOfInputViaENandENb = - self.getXWidth('TSI3', 'NMOS', '_Met1Layer') / 2 - drc._Metal1MinSpaceAtCorner - self.getXWidth('TSI3', 'InputVia_ENb', '_Met1Layer') / 2
            self._DesignParameter['_Met1_iclkb_latch']['_XYCoordinates'].append([[self.getXY('TSI3', 'InputVia_ENb', '_Met1Layer')[0][0] + xCoordOfInputViaENandENb, self.getXYBot('_Met2_iclkb')[0][1]],
                                                                            [self.getXY('TSI3', 'InputVia_ENb', '_Met1Layer')[0][0] + xCoordOfInputViaENandENb, self.getXYBot('TSI3', 'InputVia_ENb', '_Met1Layer')[0][1] + tmpMet2Width / 2],
                                                                            [self.getXYRight('TSI3', 'InputVia_ENb', '_Met1Layer')[0][0] ,self.getXYBot('TSI3', 'InputVia_ENb', '_Met1Layer')[0][1] + tmpMet2Width / 2]]) # to TSI1enb
        elif TSI3_Finger == 2:
            self._DesignParameter['_Met1_iclkb_latch']['_XYCoordinates'].append([[self.getXYRight('TSI3', 'InputVia_ENb', '_Met1Layer')[0][0] - tmpMet2Width / 2, self.getXYBot('_Met2_iclkb')[0][1]],
                                                                            [self.getXYRight('TSI3', 'InputVia_ENb', '_Met1Layer')[0][0] - tmpMet2Width / 2, self.getXYTop('TSI3', 'InputVia_ENb', '_Met1Layer')[0][1]]])  # to TSI1enb
        elif TSI3_Finger >= 3:
            self._DesignParameter['_Met1_iclkb_latch']['_XYCoordinates'].append([[self.getXYLeft('TSI3', 'polyInputA', '_Met1Layer')[0][0] - drc._Metal1MinSpace2 - tmpMet2Width / 2, self.getXYBot('_Met2_iclkb')[0][1]],
                                                                           [self.getXYLeft('TSI3', 'polyInputA', '_Met1Layer')[0][0] - drc._Metal1MinSpace2 - tmpMet2Width / 2, self.getXYTop('_Met2_iclkb')[0][1] + tmpViaMet2Width + drc._Metal1MinSpace2 * 2 + tmpViaMet2Width - tmpMet2Width / 2],
                                                                           [self.getXY('TSI3', 'polyInputA', '_Met1Layer')[0][0] + drc._Metal1MinSpace2 + tmpMet2Width / 2, self.getXYTop('_Met2_iclkb')[0][1] + tmpViaMet2Width + drc._Metal1MinSpace2 * 2 + tmpViaMet2Width - tmpMet2Width / 2],
                                                                           [self.getXY('TSI3', 'polyInputA', '_Met1Layer')[0][0] + drc._Metal1MinSpace2 + tmpMet2Width / 2, self.getXYTop('TSI3', 'polyInputENb', '_Met1Layer')[0][1] - tmpMet2Width / 2],
                                                                           [self.getXYRight('TSI3', 'polyInputENb', '_Met1Layer')[0][0], self.getXYTop('TSI3', 'polyInputENb', '_Met1Layer')[0][1] - tmpMet2Width / 2]])  # to TSI1enb



        # insert via
        self._DesignParameter['_ViaMet12Met2iclkb_latch'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_ViaMet12Met2iclkb_latchIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2iclkb_latch']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=1))
        self._DesignParameter['_ViaMet12Met2iclkb_latch']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet12Met2iclkb_latch']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = tmpVia1YWidth
        self._DesignParameter['_ViaMet12Met2iclkb_latch']['_XYCoordinates']=[[self.getXYLeft('_Met2_iclkb_latch')[0][0] + tmpMet2Width / 2, self.getXY('_Met2_iclkb_latch')[0][1] + tmpViaMet2Width / 2 - tmpMet2Width / 2], # TG1 EN
                                                                         [self._DesignParameter['_Met1_iclkb_latch']['_XYCoordinates'][1][0][0], self.getXY('_Met2_iclkb_latch')[0][1] + tmpViaMet2Width / 2 - tmpMet2Width / 2]] # TSI1 ENb

        rightBoundary = self._DesignParameter['_ViaMet12Met2iclkb_latch']['_XYCoordinates'][1][0]

        self._DesignParameter['_Met2_iclkb_latch'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=tmpMet2Width,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, YCoord_iclkb]]
        )

        ''''iclkb Routing end'''


        '''rib routing(ADDED by smlim)'''
        rightBoundary = self.getXY('TG2')[0][0] + self._DesignParameter['TG2']['_DesignObj']._DesignParameter['m1_source_routing_y']['_XYCoordinates'][0][0][0] + self.getWidth('TG2', 'm1_source_routing_y') / 2 # only when INV Finger > 3
        leftBoundary = self.getXY('INV1')[0][0] + self._DesignParameter['INV1']['_DesignObj']._DesignParameter['_OutputRouting']['_XYCoordinates'][-1][0][0] - self.getWidth('INV1', '_OutputRouting') / 2
        YCoord_rib = self.getXY('_Met2_iclkb')[0][1] + tmpViaMet2Width + drc._Metal1MinSpace2

        # TG1y to TSI1out
        self._DesignParameter['_Met2_rib'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=tmpMet2Width,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, YCoord_rib]]
        )

        # insert via
        self._DesignParameter['_ViaMet12Met2rib'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_ViaMet12Met2ribIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2rib']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=1))
        self._DesignParameter['_ViaMet12Met2rib']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet12Met2rib']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet12Met2rib']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = tmpVia1YWidth
        self._DesignParameter['_ViaMet12Met2rib']['_XYCoordinates'] = [[self.getXYLeft('_Met2_rib')[0][0] + tmpMet2Width / 2, self.getXY('_Met2_rib')[0][1] - tmpViaMet2Width / 2 + tmpMet2Width / 2],
                                                                       [self.getXYRight('_Met2_rib')[0][0] - tmpMet2Width / 2, self.getXY('_Met2_rib')[0][1] - tmpViaMet2Width / 2 + tmpMet2Width / 2]]
        if TSI1_Finger >= 3:
            self._DesignParameter['_ViaMet12Met2rib']['_XYCoordinates'].append([self.getXY('TSI1', 'polyInputA', '_Met1Layer')[0][0], self.getXY('_Met2_rib')[0][1] - tmpViaMet2Width / 2 + tmpMet2Width / 2])
        else:
            self._DesignParameter['_ViaMet12Met2rib']['_XYCoordinates'].append([self.getXY('TSI1', 'InputVia_A', '_Met1Layer')[0][0], self.getXY('_Met2_rib')[0][1] - tmpViaMet2Width / 2 + tmpMet2Width / 2])

         # Additional Routing
        if TSI1_Finger == 1:
            self._DesignParameter['_Met1_rib_add'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _Width=tmpMet2Width,
                _XYCoordinates=[[[self.getXY('_ViaMet12Met2rib', '_Met2Layer')[-1][0], self.getXYTop('_ViaMet12Met2rib', '_Met2Layer')[-1][1]],
                                 [self.getXY('_ViaMet12Met2rib', '_Met2Layer')[-1][0], self.getXYBot('TSI1', 'InputVia_A', '_Met1Layer')[0][1]]]]
            )
        elif TSI1_Finger == 2:
            self._DesignParameter['_Met1_rib_add'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _Width=tmpMet2Width,
                _XYCoordinates=[[[self.getXY('_ViaMet12Met2rib', '_Met2Layer')[-1][0], self.getXYTop('_ViaMet12Met2rib', '_Met2Layer')[-1][1]],
                                 [self.getXY('_ViaMet12Met2rib', '_Met2Layer')[-1][0], self.getXYBot('TSI1', 'InputVia_A', '_Met1Layer')[0][1]]]]
            )
        elif TSI1_Finger >= 3:
            self._DesignParameter['_Met1_rib_add'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _Width=tmpMet2Width,
                _XYCoordinates=[[[self.getXY('_ViaMet12Met2rib', '_Met2Layer')[-1][0], self.getXYTop('_ViaMet12Met2rib', '_Met2Layer')[-1][1]],
                                 [self.getXY('_ViaMet12Met2rib', '_Met2Layer')[-1][0], self.getXYBot('TSI1', 'polyInputA', '_Met1Layer')[0][1]]]]
            )



        '''''rib Routing_latch (added by jw)'''

        if INV6_Finger <= 2:
            rightBoundary=self.getXY('INV6', '_VIAPoly2Met1_F1', '_Met1Layer')[0][0]+ tmpMet2Width/2
        else:
            rightBoundary=self.getXY('INV6')[0][0] + self._DesignParameter['INV6']['_DesignObj']._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][0]+ tmpMet2Width/2


        leftBoundary = self.getXY('INV5', '_PMOS', '_XYCoordinatePMOSOutputRouting')[-1][0] + self.getWidth('INV5', '_OutputRouting') / 2- tmpMet2Width
        YCoord_rib = self.getXY('_Met2_iclkb')[0][1] + tmpViaMet2Width + drc._Metal1MinSpace2

        # TG3y to TSI3out
        self._DesignParameter['_Met2_rib_latch'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=tmpMet2Width,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, YCoord_rib]]
        )

        # insert via

        self._DesignParameter['_ViaMet12Met2rib']['_XYCoordinates'].append([self.getXYLeft('_Met2_rib_latch')[0][0] + tmpMet2Width / 2, self.getXY('_Met2_rib_latch')[0][1] - tmpViaMet2Width / 2 + tmpMet2Width / 2])
        self._DesignParameter['_ViaMet12Met2rib']['_XYCoordinates'].append([self.getXYRight('_Met2_rib_latch')[0][0] - tmpMet2Width / 2, self.getXY('_Met2_rib_latch')[0][1] - tmpViaMet2Width / 2 + tmpMet2Width / 2])
        if TSI3_Finger >= 3:
            self._DesignParameter['_ViaMet12Met2rib']['_XYCoordinates'].append([self.getXY('TSI3', 'polyInputA', '_Met1Layer')[0][0], self.getXY('_Met2_rib_latch')[0][1] - tmpViaMet2Width / 2 + tmpMet2Width / 2])
        else:
            self._DesignParameter['_ViaMet12Met2rib']['_XYCoordinates'].append([self.getXY('TSI3', 'InputVia_A', '_Met1Layer')[0][0], self.getXY('_Met2_rib_latch')[0][1] - tmpViaMet2Width / 2 + tmpMet2Width / 2])

        '''rib_latch routing end'''

        # Additional Routing
        if TSI3_Finger == 1:
            self._DesignParameter['_Met1_rib_add2'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _Width=tmpMet2Width,
                _XYCoordinates=[[[self.getXY('_ViaMet12Met2rib', '_Met2Layer')[-1][0], self.getXYTop('_ViaMet12Met2rib', '_Met2Layer')[-1][1]],
                                 [self.getXY('_ViaMet12Met2rib', '_Met2Layer')[-1][0], self.getXYBot('TSI3', 'InputVia_A', '_Met1Layer')[0][1]]]]
            )
        elif TSI3_Finger == 2:
            self._DesignParameter['_Met1_rib_add2'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _Width=tmpMet2Width,
                _XYCoordinates=[[[self.getXY('_ViaMet12Met2rib', '_Met2Layer')[-1][0], self.getXYTop('_ViaMet12Met2rib', '_Met2Layer')[-1][1]],
                                 [self.getXY('_ViaMet12Met2rib', '_Met2Layer')[-1][0], self.getXYBot('TSI3', 'InputVia_A', '_Met1Layer')[0][1]]]]
            )
        elif TSI3_Finger >= 3:
            self._DesignParameter['_Met1_rib_add2'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _Width=tmpMet2Width,
                _XYCoordinates=[[[self.getXY('_ViaMet12Met2rib', '_Met2Layer')[-1][0], self.getXYTop('_ViaMet12Met2rib', '_Met2Layer')[-1][1]],
                                 [self.getXY('_ViaMet12Met2rib', '_Met2Layer')[-1][0], self.getXYBot('TSI3', 'polyInputA', '_Met1Layer')[0][1]]]]
            )






        '''qb routing(ADDED by smlim)'''
        leftBoundary = self.getXY('TG2')[0][0] + self._DesignParameter['TG2']['_DesignObj']._DesignParameter['m1_drain_routing_y']['_XYCoordinates'][-1][0][0] - self.getWidth('TG2', 'm1_drain_routing_y') / 2
        YCoord_qb = YCoord_rib
        if INV4_Finger <= 2:
            rightBoundary = self.getXYRight('INV4', '_VIAPoly2Met1_F1', '_Met1Layer')[0][0]
        elif INV4_Finger >= 3:
            rightBoundary = self.getXYRight('INV4', '_VIAMOSPoly2Met1LeftMost', '_Met1Layer')[-1][0]

        # TSI2A to INV4out
        self._DesignParameter['_Met1_qb'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _Width=tmpMet2Width
        )
        if TSI2_Finger == 1:
            self._DesignParameter['_Met1_qb']['_XYCoordinates'] = [[[self.getXYLeft('TSI2', 'InputVia_A', '_Met1Layer')[0][0], self.getXY('TSI2', 'InputVia_A', '_Met1Layer')[0][1]],
                                                                    [self.getXY('INV4', '_PMOS', '_XYCoordinatePMOSOutputRouting')[-1][0] + self.getWidth('INV4', '_OutputRouting') / 2, self.getXY('TSI2', 'InputVia_A', '_Met1Layer')[0][1]]]]
        elif TSI2_Finger == 2:
            self._DesignParameter['_Met1_qb']['_XYCoordinates'] = [[[self.getXYLeft('TSI2', 'InputVia_A', '_Met1Layer')[0][0] + tmpMet2Width / 2, self.getXYTop('TSI2', 'InputVia_A', '_Met1Layer')[0][1]],
                                                                    [self.getXYLeft('TSI2', 'InputVia_A', '_Met1Layer')[0][0] + tmpMet2Width / 2, self.getXYTop('TSI2', 'NMOS', '_Met1Layer')[0][1] + drc._Metal1MinSpace2 + tmpMet2Width / 2]]] # y축 바꾸기
        elif TSI2_Finger >= 3:
            self._DesignParameter['_Met1_qb']['_XYCoordinates'] = [[[self.getXY('TSI2', 'ViaForVSS', 'METAL2_boundary_0')[1][0], self.getXYTop('TSI2', 'polyInputA', '_Met1Layer')[0][1]],
                                                                    [self.getXY('TSI2', 'ViaForVSS', 'METAL2_boundary_0')[1][0], self.getXYTop('TSI2', 'Met1RouteX_NMOut')[0][1] - tmpMet2Width]]]




        # TG2y to INV4in & TSI2out
        self._DesignParameter['_Met2_qb'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=tmpMet2Width,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, YCoord_qb]]
        )

        # Additional Routing
        if TSI2_Finger == 2:
            self._DesignParameter['_Met1_qb_add'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=tmpMet2Width,
                _YWidth=self.getYWidth('TSI2', 'met1_output_5'),
                _XYCoordinates=[[self.getXYRight('TSI2', 'met1_output_5')[0][0] - tmpMet2Width / 2, self.getXY('TSI2', 'met1_output_5')[0][1]]]
            )
            self._DesignParameter['_Met2_qb_add'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                _XWidth=self.getXY('INV4', '_PMOS', '_XYCoordinatePMOSOutputRouting')[-1][0] - self._DesignParameter['_Met1_qb']['_XYCoordinates'][0][0][0] + tmpMet2Width,
                _YWidth=tmpMet2Width,
                _XYCoordinates=[[(self.getXY('INV4', '_PMOS', '_XYCoordinatePMOSOutputRouting')[-1][0] + self._DesignParameter['_Met1_qb']['_XYCoordinates'][0][0][0]) / 2,
                                 self._DesignParameter['_Met1_qb']['_XYCoordinates'][0][1][1] + tmpMet2Width / 2]]
            )
            if INV4_Finger >= 3:
                self._DesignParameter['_Met2_qb_add2'] = self._PathElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                    _Width=tmpMet2Width,
                    _XYCoordinates=[[[self.getXYRight('_Met2_qb_add')[0][0] - tmpMet2Width / 2, self.getXYTop('_Met2_qb_add')[0][1]],
                                     [self.getXYRight('_Met2_qb_add')[0][0] - tmpMet2Width / 2, self.getXYBot('INV4', '_ViaMet12Met2OnNMOSOutput', '_Met2Layer')[-1][1]]]]
                )
        elif TSI2_Finger >= 3:
            self._DesignParameter['_Met2_qb_add'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                _XWidth=self.getXY('INV4', '_PMOS', '_XYCoordinatePMOSOutputRouting')[-1][0] - self._DesignParameter['_Met1_qb']['_XYCoordinates'][0][0][0] + tmpMet2Width,
                _YWidth=tmpMet2Width,
                _XYCoordinates=[[(self.getXY('INV4', '_PMOS', '_XYCoordinatePMOSOutputRouting')[-1][0] + self._DesignParameter['_Met1_qb']['_XYCoordinates'][0][0][0]) / 2,
                                 self._DesignParameter['_Met1_qb']['_XYCoordinates'][0][1][1] + tmpMet2Width / 2]]
            )
            if INV4_Finger >= 3:
                self._DesignParameter['_Met2_qb_add2'] = self._PathElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                    _Width=tmpMet2Width,
                    _XYCoordinates=[[[self.getXYRight('_Met2_qb_add')[0][0] - tmpMet2Width / 2, self.getXYTop('_Met2_qb_add')[0][1]],
                                     [self.getXYRight('_Met2_qb_add')[0][0] - tmpMet2Width / 2, self.getXYBot('INV4', '_ViaMet12Met2OnNMOSOutput', '_Met2Layer')[-1][1]]]]
                )

        # insert via
        self._DesignParameter['_ViaMet12Met2qb'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_ViaMet12Met2qbIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2qb']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=1))
        self._DesignParameter['_ViaMet12Met2qb']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet12Met2qb']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet12Met2qb']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = tmpVia1YWidth
        self._DesignParameter['_ViaMet12Met2qb']['_XYCoordinates'] = [[self.getXYLeft('_Met2_qb')[0][0] + tmpMet2Width / 2, self.getXY('_Met2_qb')[0][1] - tmpViaMet2Width / 2 + tmpMet2Width / 2],
                                                                       [self.getXYRight('_Met2_qb')[0][0] - tmpMet2Width / 2, self.getXY('_Met2_qb')[0][1]- tmpViaMet2Width / 2 + tmpMet2Width / 2]]
        if TSI2_Finger == 1:
            self._DesignParameter['_ViaMet12Met2qb']['_XYCoordinates'].append([self.getXY('TSI2')[0][0], self.getXY('_Met2_qb')[0][1] - tmpViaMet2Width / 2 + tmpMet2Width / 2])
        elif TSI2_Finger == 2:
            self._DesignParameter['_ViaMet12Met2qb']['_XYCoordinates'].append([self.getXYRight('TSI2', 'met1_output_5')[0][0] - tmpMet2Width / 2, self.getXY('_Met2_qb')[0][1] - tmpViaMet2Width / 2 + tmpMet2Width / 2])
            self._DesignParameter['_ViaMet12Met2qb']['_XYCoordinates'].append([self.getXYLeft('_Met2_qb_add')[0][0] + tmpMet2Width / 2, self.getXY('_Met2_qb_add')[0][1] + tmpViaMet2Width / 2 - tmpMet2Width / 2])
            if INV4_Finger < 3:
                self._DesignParameter['_ViaMet12Met2qb']['_XYCoordinates'].append([self.getXYRight('_Met2_qb_add')[0][0] - tmpMet2Width / 2, self.getXY('_Met2_qb_add')[0][1] + tmpViaMet2Width / 2 - tmpMet2Width / 2])
        elif TSI2_Finger >= 3:
            self._DesignParameter['_ViaMet12Met2qb']['_XYCoordinates'].append([self.getXY('TSI2', 'Met1RouteY_Out')[0][0], self.getXY('_Met2_qb')[0][1] - tmpViaMet2Width / 2 + tmpMet2Width / 2])
            self._DesignParameter['_ViaMet12Met2qb']['_XYCoordinates'].append([self.getXYLeft('_Met2_qb_add')[0][0] + tmpMet2Width / 2, self.getXY('_Met2_qb_add')[0][1] + tmpViaMet2Width / 2 - tmpMet2Width / 2])
            if INV4_Finger < 3:
                self._DesignParameter['_ViaMet12Met2qb']['_XYCoordinates'].append([self.getXYRight('_Met2_qb_add')[0][0] - tmpMet2Width / 2, self.getXY('_Met2_qb_add')[0][1] + tmpViaMet2Width / 2 - tmpMet2Width / 2])



        ###### TG3in to inv4out (added by jwlee)


        if INV4_Finger >= 3:
            YCoord_dib3 = self.getXYTop('INV4', '_ViaMet12Met2OnNMOSOutput', '_Met2Layer')[0][1] + tmpDRC_Met2Spacing + tmpMet2Width / 2
        elif INV4_Finger < 3:
            YCoord_dib3=YCoord_dib2
        TG3in = self.getXY('TG3')[0][0] +self._DesignParameter['TG3']['_DesignObj']._DesignParameter['m1_source_routing_y']['_XYCoordinates'][0][0][0]
        self._DesignParameter['_Met2_inv4'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _Width=tmpMet2Width
        )

        self._DesignParameter['_Met2_inv4']['_XYCoordinates']=[[[self.getXY('INV4', '_PMOS', '_XYCoordinatePMOSOutputRouting')[-1][0] - tmpMet2Width/2, YCoord_dib3],
                                                             [TG3in + tmpMet2Width/2, YCoord_dib3]]]

        #YCoord_dib2
        # insert via for q routing
        self._DesignParameter['_ViaMet12Met2q'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_ViaMet12Met2qIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2q']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=1))
        self._DesignParameter['_ViaMet12Met2q']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet12Met2q']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet12Met2q']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = tmpVia1YWidth
        if TSI2_Finger ==1:
            self._DesignParameter['_ViaMet12Met2q']['_XYCoordinates'] = [[self.getXY('INV4', '_PMOS', '_XYCoordinatePMOSOutputRouting')[-1][0] + self.getWidth('INV4', '_OutputRouting') / 2- tmpMet2Width/2, YCoord_dib3],[TG3in+ self.getWidth('INV4', '_OutputRouting') / 2- tmpMet2Width/2, YCoord_dib3]]

        elif TSI2_Finger==2:
            self._DesignParameter['_ViaMet12Met2q']['_XYCoordinates'] = [[TG3in+ self.getWidth('INV4', '_OutputRouting') / 2- tmpMet2Width/2, YCoord_dib3]]

        #self._DesignParameter['_ViaMet12Met2q']['_XYCoordinates'] = [[self.getXY('INV4', '_PMOS', '_XYCoordinatePMOSOutputRouting')[-1][0] + self.getWidth('INV4', '_OutputRouting') / 2- tmpMet2Width/2, YCoord_dib3+ tmpViaMet2Width / 2 - tmpMet2Width / 2],[TG3in+ self.getWidth('INV4', '_OutputRouting') / 2- tmpMet2Width/2, YCoord_dib3+ tmpViaMet2Width / 2 - tmpMet2Width / 2]]



        # '''clk routing(ADDED by smlim)'''
        # leftBoundary = self.getXYLeft('TG2', 'gate_output', '_Met1Layer')[0][0]
        # YCoord_clk = self.getXY('TG2', 'gate_output', '_Met1Layer')[0][1]
        # if INV2_Finger <= 2:
        #     rightBoundary = self.getXYRight('INV2', '_VIAPoly2Met1_F1', '_Met1Layer')[0][0]
        # elif INV2_Finger >= 3:
        #     rightBoundary = self.getXY('INV2')[0][0] + self._DesignParameter['INV2']['_DesignObj']._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][0]
        #
        # # TG2y to INV4in & TSI2out
        # self._DesignParameter['_Met1_clk'] = self._BoundaryElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        #     _XWidth=rightBoundary - leftBoundary,
        #     _YWidth=tmpMet2Width,
        #     _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, YCoord_clk]]
        # )


        # '''iclk routing(ADDED by smlim)'''
        leftBoundary = self.getXYLeft('TG1', 'gate_input', '_Met1Layer')[0][0]
        YCoord_iclk = self.getXYTop('_Met2_rib')[0][1] + drc._Metal1MinSpace2 + tmpViaMet2Width - tmpMet2Width / 2
        if TSI2_Finger == 1:
            rightBoundary = self.getXYRight('TSI2', 'InputVia_ENb', '_Met1Layer')[0][0]
        elif TSI2_Finger == 2:
            rightBoundary = self.getXYLeft('TSI2', 'InputVia_ENb', '_Met1Layer')[0][0] - tmpMet2Width /2 - drc._Metal1MinSpace2
        elif TSI2_Finger >= 3:
            rightBoundary = min(self.getXYLeft('TSI2', 'polyInputENb', '_Met1Layer')[0][0], self.getXYLeft('TSI2', 'Met1RouteX_PMOut')[0][0]) - tmpMet2Width /2 - drc._Metal1MinSpace2

        # TG1enb to TSI2enb
        self._DesignParameter['_Met2_iclk'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=tmpMet2Width,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, YCoord_iclk]]
        )
        self._DesignParameter['_Met1_iclk'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met1_iclk']['_XYCoordinates'] = [[[self.getXYLeft('_Met2_iclk')[0][0] + tmpMet2Width / 2, self.getXYTop('_Met2_iclk')[0][1]],
                                                                  [self.getXYLeft('_Met2_iclk')[0][0] + tmpMet2Width / 2, self.getXYBot('TG1', 'gate_input', '_Met1Layer')[0][1]]]] # to TG1 enb

        # Additional Routing
        if TSI1_Finger == 1:
            self._DesignParameter['_Met1_iclk']['_XYCoordinates'].append([[self.getXYRight('TSI1', 'InputVia_EN', '_Met1Layer')[0][0], self.getXYBot('TSI1', 'InputVia_EN', '_Met1Layer')[0][1] + tmpMet2Width / 2],
                                                                      [self.getXY('TSI1', 'InputVia_ENb', '_Met1Layer')[0][0] + xCoordOfInputViaENandENb * 2, self.getXYBot('TSI1', 'InputVia_EN', '_Met1Layer')[0][1] + tmpMet2Width / 2],
                                                                      [self.getXY('TSI1', 'InputVia_ENb', '_Met1Layer')[0][0] + xCoordOfInputViaENandENb * 2, self.getXYTop('_Met2_iclk')[0][1]]]) # to TSI1en
        elif TSI1_Finger == 2:
            self._DesignParameter['_Met1_iclk']['_XYCoordinates'].append([[self.getXYRight('TSI1', 'InputVia_EN', '_Met1Layer')[0][0], self.getXYBot('TSI1', 'InputVia_EN', '_Met1Layer')[0][1] + tmpMet2Width / 2],
                                                                      [self.getXYLeft('TSI1', 'InputVia_A', '_Met1Layer')[0][0] - drc._Metal1MinSpace2 - tmpMet2Width / 2, self.getXYBot('TSI1', 'InputVia_EN', '_Met1Layer')[0][1] + tmpMet2Width / 2],
                                                                      [self.getXYLeft('TSI1', 'InputVia_A', '_Met1Layer')[0][0] - drc._Metal1MinSpace2 - tmpMet2Width / 2, self.getXYTop('_Met2_iclk')[0][1]]]) # to TSI1en
            self._DesignParameter['_Met1_iclk_add1'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _Width=self.getYWidth('TSI1', 'InputVia_EN', '_Met1Layer'),
                _XYCoordinates=[[[self._DesignParameter['_Met1_iclk']['_XYCoordinates'][1][0][0], self.getXY('TSI1', 'InputVia_EN', '_Met1Layer')[0][1]],
                                 [self._DesignParameter['_Met1_iclk']['_XYCoordinates'][1][1][0], self.getXY('TSI1', 'InputVia_EN', '_Met1Layer')[0][1]]]]
            )
        elif TSI1_Finger >= 3:
            self._DesignParameter['_Met1_iclk']['_XYCoordinates'].append([[self.getXYRight('TSI1', 'polyInputEN', '_Met1Layer')[0][0], self.getXYBot('TSI1', 'polyInputEN', '_Met1Layer')[0][1] + tmpMet2Width / 2],
                                                                          [self.getXY('TSI1', 'polyInputA', '_Met1Layer')[0][0], self.getXYBot('TSI1', 'polyInputEN', '_Met1Layer')[0][1] + tmpMet2Width / 2],
                                                                          [self.getXY('TSI1', 'polyInputA', '_Met1Layer')[0][0], self.getXY('_Met2_dib')[0][1]],
                                                                          [self.getXYLeft('TSI1', 'polyInputA', '_Met1Layer')[0][0] - drc._Metal1MinSpace2 * 2 - (tmpMet2Width * 3) / 2, self.getXY('_Met2_dib')[0][1]],
                                                                          [self.getXYLeft('TSI1', 'polyInputA', '_Met1Layer')[0][0] - drc._Metal1MinSpace2 * 2 - (tmpMet2Width * 3) / 2, self.getXYTop('_Met2_iclk')[0][1]]]) # to TSI1en

        if TSI2_Finger == 1:
            self._DesignParameter['_Met1_iclk']['_XYCoordinates'].append([[self.getXYRight('_Met2_iclk')[0][0] - tmpMet2Width / 2, self.getXYTop('_Met2_iclk')[0][1]],
                                                                          [self.getXYRight('_Met2_iclk')[0][0] - tmpMet2Width / 2, self.getXYBot('TSI2', 'InputVia_ENb', '_Met1Layer')[0][1]]])  # to TSI2 enb
        elif TSI2_Finger == 2:
            self._DesignParameter['_Met1_iclk']['_XYCoordinates'].append([[self.getXYRight('TSI2', 'InputVia_ENb', '_Met1Layer')[0][0], self.getXYBot('TSI2', 'InputVia_ENb', '_Met1Layer')[0][1] + tmpMet2Width / 2],
                                                                      [self.getXYRight('_Met2_iclk')[0][0] - tmpMet2Width / 2, self.getXYBot('TSI2', 'InputVia_ENb', '_Met1Layer')[0][1] + tmpMet2Width / 2],
                                                                      [self.getXYRight('_Met2_iclk')[0][0] - tmpMet2Width / 2, self.getXYTop('_Met2_iclk')[0][1]]])
            self._DesignParameter['_Met1_iclk_add2'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _Width=self.getYWidth('TSI2', 'InputVia_EN', '_Met1Layer'),
                _XYCoordinates=[[[self.getXYRight('TSI2', 'InputVia_ENb', '_Met1Layer')[0][0], self.getXY('TSI2', 'InputVia_ENb', '_Met1Layer')[0][1]],
                                 [self.getXYRight('_Met2_iclk')[0][0] - tmpMet2Width / 2, self.getXY('TSI2', 'InputVia_ENb', '_Met1Layer')[0][1]]]]
            )
        elif TSI2_Finger >= 3:
            self._DesignParameter['_Met1_iclk']['_XYCoordinates'].append([[self.getXYRight('TSI2', 'polyInputENb', '_Met1Layer')[0][0], self.getXYBot('TSI2', 'polyInputENb', '_Met1Layer')[0][1] + tmpMet2Width / 2],
                                                                      [self.getXYRight('_Met2_iclk')[0][0] - tmpMet2Width / 2, self.getXYBot('TSI2', 'polyInputENb', '_Met1Layer')[0][1] + tmpMet2Width / 2],
                                                                      [self.getXYRight('_Met2_iclk')[0][0] - tmpMet2Width / 2, self.getXYTop('_Met2_iclk')[0][1]]]) # to TSI2enb





        # insert via
        self._DesignParameter['_ViaMet12Met2iclk'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_ViaMet12Met2iclkIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2iclk']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=1))
        self._DesignParameter['_ViaMet12Met2iclk']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = tmpViaMet2Width

        self._DesignParameter['_ViaMet12Met2iclk']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = tmpVia1YWidth
        self._DesignParameter['_ViaMet12Met2iclk']['_XYCoordinates'] = [[self.getXYLeft('_Met2_iclk')[0][0] + tmpMet2Width / 2, self.getXY('_Met2_iclk')[0][1] - tmpViaMet2Width / 2 + tmpMet2Width / 2],
                                                                         [self.getXY('INV3')[0][0] + self._DesignParameter['INV3']['_DesignObj']._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][0], self.getXY('_Met2_iclk')[0][1] - tmpViaMet2Width / 2 + tmpMet2Width / 2],
                                                                         [self.getXYRight('_Met2_iclk')[0][0] - tmpMet2Width / 2, self.getXY('_Met2_iclk')[0][1] - tmpViaMet2Width / 2 + tmpMet2Width / 2]]
        if TSI1_Finger == 1:
            self._DesignParameter['_ViaMet12Met2iclk']['_XYCoordinates'].append([self._DesignParameter['_Met1_iclk']['_XYCoordinates'][1][1][0], self.getXY('_Met2_iclk')[0][1] - tmpViaMet2Width / 2 + tmpMet2Width / 2])
        elif TSI1_Finger == 2:
            self._DesignParameter['_ViaMet12Met2iclk']['_XYCoordinates'].append([self._DesignParameter['_Met1_iclk']['_XYCoordinates'][1][1][0], self.getXY('_Met2_iclk')[0][1] - tmpViaMet2Width / 2 + tmpMet2Width / 2])
        elif TSI1_Finger >= 3:
            self._DesignParameter['_ViaMet12Met2iclk']['_XYCoordinates'].append([self._DesignParameter['_Met1_iclk']['_XYCoordinates'][1][-1][0], self.getXY('_Met2_iclk')[0][1] - tmpViaMet2Width / 2 + tmpMet2Width / 2])



        '''' clk routing (added by jw)'''''
        self._DesignParameter['_Met2_iclk_latch2'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met2_iclk_latch2']['_XYCoordinates'] = [[[self.getXYRight('TG3', 'gate_input', '_Met1Layer')[0][0], YCoord_iclk],
                                                                  [rightBoundary, YCoord_iclk]]]

        leftBoundary = self.getXYLeft('TG3', 'gate_input', '_Met1Layer')[0][0]
        YCoord_iclk = self.getXYTop('_Met2_rib')[0][1] + drc._Metal1MinSpace2 + tmpViaMet2Width - tmpMet2Width / 2
        rightBoundary = self.getXY('TSI3', 'InputVia_ENb', '_Met1Layer')[0][0]


        # TG1enb to TSI2enb
        self._DesignParameter['_Met2_iclk_latch'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=tmpMet2Width,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, YCoord_iclk]]
        )



        self._DesignParameter['_Met1_iclk_latch'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met1_iclk_latch']['_XYCoordinates'] = [[[self.getXYLeft('_Met2_iclk_latch')[0][0] + tmpMet2Width / 2, self.getXYTop('_Met2_iclk_latch')[0][1]],
                                                                  [self.getXYLeft('_Met2_iclk_latch')[0][0] + tmpMet2Width / 2, self.getXYBot('TG3', 'gate_input', '_Met1Layer')[0][1]]]] # to TG1 enb

        # Additional Routing
        if TSI3_Finger == 1:
            self._DesignParameter['_Met1_iclk_latch']['_XYCoordinates'].append([[self.getXYRight('TSI3', 'InputVia_EN', '_Met1Layer')[0][0], self.getXYBot('TSI3', 'InputVia_EN', '_Met1Layer')[0][1] + tmpMet2Width / 2],
                                                                      [self.getXY('TSI3', 'InputVia_ENb', '_Met1Layer')[0][0] + xCoordOfInputViaENandENb * 2, self.getXYBot('TSI3', 'InputVia_EN', '_Met1Layer')[0][1] + tmpMet2Width / 2],
                                                                      [self.getXY('TSI3', 'InputVia_ENb', '_Met1Layer')[0][0] + xCoordOfInputViaENandENb * 2, self.getXYTop('_Met2_iclk_latch')[0][1]]]) # to TSI1en
        elif TSI3_Finger == 2:
            self._DesignParameter['_Met1_iclk_latch']['_XYCoordinates'].append([[self.getXYRight('TSI3', 'InputVia_EN', '_Met1Layer')[0][0], self.getXYBot('TSI3', 'InputVia_EN', '_Met1Layer')[0][1] + tmpMet2Width / 2],
                                                                      [self.getXYLeft('TSI3', 'InputVia_A', '_Met1Layer')[0][0] - drc._Metal1MinSpace2 - tmpMet2Width / 2, self.getXYBot('TSI3', 'InputVia_EN', '_Met1Layer')[0][1] + tmpMet2Width / 2],
                                                                      [self.getXYLeft('TSI3', 'InputVia_A', '_Met1Layer')[0][0] - drc._Metal1MinSpace2 - tmpMet2Width / 2, self.getXYTop('_Met2_iclk_latch')[0][1]]]) # to TSI1en
            self._DesignParameter['_Met1_iclk_add1_latch'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _Width=self.getYWidth('TSI3', 'InputVia_EN', '_Met1Layer'),
                _XYCoordinates=[[[self._DesignParameter['_Met1_iclk_latch']['_XYCoordinates'][1][0][0], self.getXY('TSI3', 'InputVia_EN', '_Met1Layer')[0][1]],
                                 [self._DesignParameter['_Met1_iclk_latch']['_XYCoordinates'][1][1][0], self.getXY('TSI3', 'InputVia_EN', '_Met1Layer')[0][1]]]]
            )
        elif TSI3_Finger >= 3:
            self._DesignParameter['_Met1_iclk_latch']['_XYCoordinates'].append([[self.getXYRight('TSI3', 'polyInputEN', '_Met1Layer')[0][0], self.getXYBot('TSI3', 'polyInputEN', '_Met1Layer')[0][1] + tmpMet2Width / 2],
                                                                          [self.getXY('TSI3', 'polyInputA', '_Met1Layer')[0][0], self.getXYBot('TSI3', 'polyInputEN', '_Met1Layer')[0][1] + tmpMet2Width / 2],
                                                                          [self.getXY('TSI3', 'polyInputA', '_Met1Layer')[0][0], self.getXY('_Met2_dib')[0][1]],
                                                                          [self.getXYLeft('TSI3', 'polyInputA', '_Met1Layer')[0][0] - drc._Metal1MinSpace2 * 2 - (tmpMet2Width * 3) / 2, self.getXY('_Met2_dib')[0][1]],
                                                                          [self.getXYLeft('TSI3', 'polyInputA', '_Met1Layer')[0][0] - drc._Metal1MinSpace2 * 2 - (tmpMet2Width * 3) / 2, self.getXYTop('_Met2_iclk_latch')[0][1]]]) # to TSI1en

        self._DesignParameter['_ViaMet12Met2iclk_latch'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_ViaMet12Met2iclk_latchIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2iclk_latch']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=1))
        self._DesignParameter['_ViaMet12Met2iclk_latch']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = tmpViaMet2Width

        self._DesignParameter['_ViaMet12Met2iclk_latch']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = tmpVia1YWidth
        self._DesignParameter['_ViaMet12Met2iclk_latch']['_XYCoordinates'] = [[self.getXYLeft('_Met2_iclk_latch')[0][0] + tmpMet2Width / 2, self.getXY('_Met2_iclk_latch')[0][1] - tmpViaMet2Width / 2 + tmpMet2Width / 2]]

        if TSI3_Finger == 1:
            self._DesignParameter['_ViaMet12Met2iclk_latch']['_XYCoordinates'].append([self._DesignParameter['_Met1_iclk_latch']['_XYCoordinates'][1][1][0], self.getXY('_Met2_iclk_latch')[0][1] - tmpViaMet2Width / 2 + tmpMet2Width / 2])
        elif TSI3_Finger == 2:
            self._DesignParameter['_ViaMet12Met2iclk_latch']['_XYCoordinates'].append([self._DesignParameter['_Met1_iclk_latch']['_XYCoordinates'][1][1][0], self.getXY('_Met2_iclk_latch')[0][1] - tmpViaMet2Width / 2 + tmpMet2Width / 2])
        elif TSI3_Finger >= 3:
            self._DesignParameter['_ViaMet12Met2iclk_latch']['_XYCoordinates'].append([self._DesignParameter['_Met1_iclk_latch']['_XYCoordinates'][1][-1][0], self.getXY('_Met2_iclk_latch')[0][1] - tmpViaMet2Width / 2 + tmpMet2Width / 2])

        rightBoundary = self._DesignParameter['_ViaMet12Met2iclk_latch']['_XYCoordinates'][1][0]


        # TG1enb to TSI2enb
        self._DesignParameter['_Met2_iclk_latch'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=tmpMet2Width,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, YCoord_iclk]]
        )


        '''''end'''
        ################# TG2 CLK routing revise (Added by jwlee)
        self._DesignParameter['_Met1_iclk2'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met1_iclk2']['_XYCoordinates']=[[[self.getXYRight('TG2', 'gate_output', '_Met1Layer')[0][0]-tmpMet2Width / 2, self.getXYTop('_Met2_iclk')[0][1]],
                                                                  [self.getXYRight('TG2', 'gate_output', '_Met1Layer')[0][0]-tmpMet2Width / 2, self.getXYBot('TG2', 'gate_output', '_Met1Layer')[0][1]]]]
        # insert via(Added by jwlee)
        self._DesignParameter['_ViaMet12Met2iclk2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_ViaMet12Met2iclk2In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2iclk2']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=1))
        self._DesignParameter['_ViaMet12Met2iclk2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet12Met2iclk2']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = tmpVia1YWidth
        self._DesignParameter['_ViaMet12Met2iclk2']['_XYCoordinates'] = [[self.getXYRight('TG2', 'gate_output', '_Met1Layer')[0][0]-tmpMet2Width / 2,  self.getXY('_Met2_iclk')[0][1] - tmpViaMet2Width / 2 + tmpMet2Width / 2]]


        ########################### inv4 revise ###########
        if INV4_Finger>=3:
            self._DesignParameter['INV4']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'] = []

            _ViaOnPMOSOutput = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _ViaOnPMOSOutput['_ViaMet12Met2NumberOfCOX'] = 1
            _ViaOnPMOSOutput['_ViaMet12Met2NumberOfCOY'] = 1

            self._DesignParameter['inv4output']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='inv4outputIn{}'.format(_Name)))[0]
            self._DesignParameter['inv4output']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaOnPMOSOutput)
            self._DesignParameter['inv4output']['_XYCoordinates']= self.getXY('INV4', '_NMOS', '_XYCoordinateNMOSOutputRouting')

        ########################### inv5 revise ###########
        if INV5_Finger >= 3:
            self._DesignParameter['INV5']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'] = []

            _ViaOnPMOSOutput = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _ViaOnPMOSOutput['_ViaMet12Met2NumberOfCOX'] = 1
            _ViaOnPMOSOutput['_ViaMet12Met2NumberOfCOY'] = 1

            self._DesignParameter['inv5output'] = \
            self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='inv5outputIn{}'.format(_Name)))[0]
            self._DesignParameter['inv5output']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(
                **_ViaOnPMOSOutput)
            self._DesignParameter['inv5output']['_XYCoordinates'] = self.getXY('INV5', '_NMOS','_XYCoordinateNMOSOutputRouting')

        '''Pin generation'''
        self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VDD')
        self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VSS')
        self._DesignParameter['_dpin'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='D')
        self._DesignParameter['_qpin'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q')
        self._DesignParameter['_qbpin'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Qb')
        self._DesignParameter['_clkpin'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='clk')

        # #Q Coordinate
        # if INV6_Finger <= 2:
        #     Q_coordinate = self.getXYRight('INV4', '_VIAPoly2Met1_F1', '_Met1Layer')[0][0]
        # elif INV6_Finger >= 3:
        #     Q_coordinate = self.getXYRight('INV4', '_VIAMOSPoly2Met1LeftMost', '_Met1Layer')[-1][0]

        self._DesignParameter['_VDDpin']['_XYCoordinates'] = self.getXY('TG1', '_VDDpin')
        self._DesignParameter['_VSSpin']['_XYCoordinates'] = self.getXY('TG1', '_VSSpin')
        self._DesignParameter['_dpin']['_XYCoordinates'] = self.getXY('TG1', '_Apin')

        self._DesignParameter['_qpin']['_XYCoordinates'] = self.getXY('_Met2_rib_latch')
        self._DesignParameter['_qbpin']['_XYCoordinates'] = [[self.getXY('INV6', '_PMOS', '_XYCoordinatePMOSOutputRouting')[-1][0],YCoord_iclkb]]
        self._DesignParameter['_clkpin']['_XYCoordinates'] = self.getXY('INV2','InputMet1')


''' INV2&3 # of Fingers should be less than 7(6 max)
    otherwise, INV inner routing and qb routing will be overlapped'''


################################ DRC Check #################################
import random
if __name__ == '__main__':
     # for i in range(0,100):
     #    TG1_Finger = random.randint(1,5)
     #    TG2_Finger = random.randint(1, 5)
     #    TSI1_Finger = random.randint(1,2)
     #    TSI2_Finger = random.randint(1,2)
     #    INV1_Finger = random.randint(1,5)
     #    INV2_Finger = random.randint(1,5)
     #    INV3_Finger = random.randint(1,5)
     #    INV4_Finger = random.randint(1,5)
     #
     #    TG3_Finger = random.randint(1, 5)
     #    TSI3_Finger = random.randint(1, 2)
     #    INV5_Finger = random.randint(1, 5)
     #    INV6_Finger = random.randint(1, 5)

        #TSI3_Finger = 2
        #TG2_Finger = 1
        TG1_NMWidth = 200
        TG1_PMWidth = 400

        TG2_NMWidth = 200
        TG2_PMWidth = 400

        TSI1_NMWidth = 200
        TSI1_PMWidth = 400

        TSI2_NMWidth = 200
        TSI2_PMWidth = 400

        INV1_NMWidth = 200
        INV1_PMWidth = 400

        INV2_NMWidth = 200
        INV2_PMWidth = 400

        INV3_NMWidth = 200
        INV3_PMWidth = 400

        INV4_NMWidth = 200
        INV4_PMWidth = 400

        TG3_NMWidth = 200
        TG3_PMWidth = 400

        TSI3_NMWidth = 200
        TSI3_PMWidth = 400

        INV5_NMWidth = 200
        INV5_PMWidth = 400

        INV6_NMWidth = 200
        INV6_PMWidth = 400

        ChannelLength = 30
        GateSpacing = 100
        SDWidth = 66
        XVT = 'SLVT'
        CellHeight = 1800
        SupplyRailType = 2

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
        TopObj = DFF(_DesignParameter=None, _Name='DFF')
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

            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            SDWidth=SDWidth,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType)

        TopObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=TopObj._DesignParameter)
        testStreamFile = open('./DFF.gds', 'wb')
        tmp = TopObj._CreateGDSStream(TopObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()
        print('#############################      Sending to FTP Server...      ##############################')

        import ftplib

        ftp = ftplib.FTP('141.223.24.53')
        ftp.login('ljw95', 'dlwodn123')
        ftp.cwd('/mnt/sdc/ljw95/OPUS/ss28')
        myfile = open('DFF.gds', 'rb')
        ftp.storbinary('STOR DFF.gds', myfile)
        myfile.close()

        # import DRCchecker
        # a = DRCchecker.DRCchecker('ljw95','dlwodn123','/mnt/sdc/ljw95/OPUS/ss28','/mnt/sdc/ljw95/OPUS/ss28/DRC/run','DFF','DFF',None)
        # a.DRCchecker()
        #
        # print ("DRC Clean!!!")
