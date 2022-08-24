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
                                  TG2_PMWidth=640,

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
            out_even_up_mode=True
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
            out_even_up_mode=True
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
        Parameters_TSI2 = dict(
            NMOSWidth=TSI2_NMWidth,
            PMOSWidth=TSI2_PMWidth,
            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            XVT=XVT,
            CellHeight=CellHeight,
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

        self._DesignParameter['TG1'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=transmission_gate.Transmission_gate(_Name='TG1In{}'.format(_Name)))[0]
        self._DesignParameter['TG1']['_DesignObj']._CalculateDesignParameter(**Parameters_TG1)
        self._DesignParameter['TG1']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['TG2'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=transmission_gate.Transmission_gate(_Name='TG2In{}'.format(_Name)))[0]
        self._DesignParameter['TG2']['_DesignObj']._CalculateDesignParameter(**Parameters_TG2)
        self._DesignParameter['TG2']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['TSI1'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=TristateInverter.TristateInverter(_Name='TSI1In{}'.format(_Name)))[0]
        self._DesignParameter['TSI1']['_DesignObj']._CalculateDesignParameterFinger1(**Parameters_TSI1)
        self._DesignParameter['TSI1']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['TSI2'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=TristateInverter.TristateInverter(_Name='TSI2In{}'.format(_Name)))[0]
        self._DesignParameter['TSI2']['_DesignObj']._CalculateDesignParameterFinger1(**Parameters_TSI1)
        self._DesignParameter['TSI2']['_XYCoordinates'] = [[0, 0]]

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

        #
        self._DesignParameter['TG1']['_XYCoordinates'] = [[self._DesignParameter['TG1']['_DesignObj'].CellXWidth / 2, 0]]
        self._DesignParameter['INV1']['_XYCoordinates'] = [
            [self.getXY('TG1')[0][0] + self._DesignParameter['TG1']['_DesignObj'].CellXWidth / 2 + self._DesignParameter['INV1']['_DesignObj'].CellXWidth / 2, 0]
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


        ''' VDD Rail, VSS Rail, XVTLayer '''
        # VSS M2
        leftBoundary = self.getXYLeft('TG1', 'vss_supply_m2_y')[0][0]
        rightBoundary = self.getXYRight('INV4', 'PbodyContact', '_Met2Layer')[0][0]
        self._DesignParameter['VSSRail_Met2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('INV4', 'PbodyContact', '_Met2Layer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, 0]]
        )
        # VSS OD(RX)
        leftBoundary = self.getXYLeft('TG1', 'vss_odlayer')[0][0]
        rightBoundary = self.getXYRight('INV4', 'PbodyContact', '_ODLayer')[0][0]
        self._DesignParameter['VSSRail_OD'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('INV4', 'PbodyContact', '_ODLayer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, 0]]
        )
        # VSS PP(BP)
        leftBoundary = self.getXYLeft('TG1', 'vss_pplayer')[0][0]
        rightBoundary = self.getXYRight('INV4', 'PbodyContact', '_PPLayer')[0][0]
        self._DesignParameter['VSSRail_PP'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('INV4', 'PbodyContact', '_PPLayer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, 0]]
        )
        ## VDD
        # VDD M2
        leftBoundary = self.getXYLeft('TG1', 'vdd_supply_m2_y')[0][0]
        rightBoundary = self.getXYRight('INV4', 'NbodyContact', '_Met2Layer')[0][0]
        self._DesignParameter['VDDRail_Met2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('INV4', 'NbodyContact', '_Met2Layer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY('INV4', 'NbodyContact', '_Met2Layer')[0][1]]]
        )
        # VDD OD(RX)
        leftBoundary = self.getXYLeft('TG1', 'vdd_odlayer')[0][0]
        rightBoundary = self.getXYRight('INV4', 'NbodyContact', '_ODLayer')[0][0]
        self._DesignParameter['VDDRail_OD'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('INV4', 'NbodyContact', '_ODLayer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY('INV4', 'NbodyContact', '_ODLayer')[0][1]]]
        )

        # NWLayer
        leftBoundary = self.getXYLeft('TG1', 'NWELL_boundary_0')[0][0]
        rightBoundary = self.getXYRight('INV4', '_NWLayerBoundary')[0][0]
        topBoundary = max(
            self.getXYTop('TG1', 'NWELL_boundary_0')[0][1],
            self.getXYTop('TG2', 'NWELL_boundary_0')[0][1],
            self.getXYTop('TSI1', 'nwlayer')[0][1],
            self.getXYTop('TSI2', 'nwlayer')[0][1],
            self.getXYTop('INV1', '_NWLayerBoundary')[0][1],
            self.getXYTop('INV2', '_NWLayerBoundary')[0][1],
            self.getXYTop('INV3', '_NWLayerBoundary')[0][1],
            self.getXYTop('INV4', '_NWLayerBoundary')[0][1]
        )
        botBoundary = min(
            self.getXYBot('TG1', 'NWELL_boundary_0')[0][1],
            self.getXYBot('TG2', 'NWELL_boundary_0')[0][1],
            self.getXYBot('TSI1', 'nwlayer')[0][1],
            self.getXYBot('TSI2', 'nwlayer')[0][1],
            self.getXYBot('INV1', '_NWLayerBoundary')[0][1],
            self.getXYBot('INV2', '_NWLayerBoundary')[0][1],
            self.getXYBot('INV3', '_NWLayerBoundary')[0][1],
            self.getXYBot('INV4', '_NWLayerBoundary')[0][1]
        )
        self._DesignParameter['_NWLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=topBoundary - botBoundary,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, (topBoundary + botBoundary) / 2]]
        )

        # XVTLayer
        assert XVT in ('SLVT', 'LVT', 'RVT', 'HVT')
        leftBoundary = self.getXYLeft('TG1', 'XVT_boundary_1')[0][0]
        rightBoundary = self.getXYRight('INV4', 'XVTLayer')[0][0]
        self._DesignParameter['XVTLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[XVT][0], _Datatype=DesignParameters._LayerMapping[XVT][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('INV4', 'XVTLayer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY('INV4', 'XVTLayer')[0][1]]]
        )


        ''' Met2 '''
        tmpDRC_Met2Spacing = 86
        tmpMet2Width = 66
        ''' dib2 '''
        YCoord_dib2 = self.getXYTop('INV1', '_ViaMet12Met2OnNMOSOutput', '_Met2Layer')[0][1] + tmpDRC_Met2Spacing + tmpMet2Width / 2
        leftBoundary = self.getXY('TG1')[0][0] + self._DesignParameter['TG1']['_DesignObj']._DesignParameter['m1_drain_routing_y']['_XYCoordinates'][-1][0][0] - self.getWidth('TG1', 'm1_drain_routing_y') / 2
        rightBoundary = self.getXY('TSI1')[0][0] + self.getWidth('TSI1', 'OutputRouting') / 2   # only when TSI Finger==1

        self._DesignParameter['met2_dib2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=tmpMet2Width,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, YCoord_dib2]]
        )



        # iclkb
        YCoord_met2iclkb = YCoord_dib2 + tmpDRC_Met2Spacing + tmpMet2Width
        leftBoundary = self.getXY('TG1', 'gate_output', '_Met1Layer')[0][0]
        rightBoundary = self.getXY('TSI2', 'InputVia_EN', '_Met1Layer')[0][0] - UnitPitch
        self._DesignParameter['met2_iclkb'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=tmpMet2Width,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, YCoord_met2iclkb]]
        )

        # iclk
        YCoord_met2iclk = YCoord_dib2 + tmpDRC_Met2Spacing + tmpMet2Width
        leftBoundary = self.getXY('TG1', 'gate_output', '_Met1Layer')[0][0]
        rightBoundary = self.getXY('TSI2', 'InputVia_EN', '_Met1Layer')[0][0] - UnitPitch
        self._DesignParameter['met2_iclk'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=tmpMet2Width,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, YCoord_met2iclk]]
        )




        ''' Met1 '''
        # inv2-inv3
        leftBoundary = self.getXY('INV2', 'PIN_Y')[0][0]
        rightBoundary = self.getXY('INV3', 'InputMet1')[0][0]
        self._DesignParameter['met1_INV2OUT_2_INV3IN'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('INV3', 'InputMet1') if INV3_Finger in (1,2) else 66,
            # _YWidth=66,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY('INV3', 'InputMet1')[0][1]]]
        )

        # TG2 - INV2
        # Align first!
        leftBoundary = self.getXY('TG2', 'gate_output')[0][0]
        rightBoundary = self.getXY('INV2', 'InputMet1')[0][0]
        self._DesignParameter['met1_TG2_2_INV2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=66,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXYBot('TG2', 'gate_output', '_Met1Layer')[0][1] + 33]]
        )

        # INV4 - TSI2(A)
        leftBoundary = self.getXY('TSI2', 'InputVia_A', '_Met1Layer')[0][0]
        rightBoundary = self.getXY('INV4', 'PIN_Y')[0][0]
        self._DesignParameter['met1_INV4_2_TSI2A'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=66,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXYBot('TSI2', 'InputVia_A', '_Met1Layer')[0][1] + 33]]
        )

