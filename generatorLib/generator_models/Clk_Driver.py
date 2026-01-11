import math
import copy

#
from generatorLib import StickDiagram
from generatorLib import DesignParameters
from generatorLib import DRC

#
from generator_models import TristateInverter
from generator_models import Inverter
from generator_models import Transmission_gate

from generator_models import DFFQb
from generator_models import ViaMet12Met2
from generator_models import ViaMet22Met3




class Clk_Driver(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name='Clk_Driver'):
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

                                  INV5_Finger=4,
                                  INV5_NMWidth=200,
                                  INV5_PMWidth=400,

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




        Parameters_DFFQb1 = dict(
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

            INV5_Finger=INV5_Finger,
            INV5_NMWidth=INV5_NMWidth,
            INV5_PMWidth=INV5_PMWidth,

            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            SDWidth=SDWidth,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType
        )

        Parameters_DFFQb2 = dict(
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

            INV5_Finger=INV5_Finger,
            INV5_NMWidth=INV5_NMWidth,
            INV5_PMWidth=INV5_PMWidth,

            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            SDWidth=SDWidth,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType
        )

        self._DesignParameter['DFFQb1'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=DFFQb.DFF(_Name='DFFQb1In{}'.format(_Name)))[0]
        self._DesignParameter['DFFQb1']['_DesignObj']._CalculateDesignParameter(**Parameters_DFFQb1)
        self._DesignParameter['DFFQb1']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['DFFQb2'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=DFFQb.DFF(_Name='DFFQb2In{}'.format(_Name)))[0]
        self._DesignParameter['DFFQb2']['_DesignObj']._CalculateDesignParameter(**Parameters_DFFQb2)
        self._DesignParameter['DFFQb2']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['DFFQb1']['_XYCoordinates'] = [[0,0]]
        self._DesignParameter['DFFQb2']['_XYCoordinates'] = [
            [self.getXY('DFFQb1')[0][0] + self._DesignParameter['DFFQb1']['_DesignObj'].CellXWidth  + 2 * UnitPitch  , 0]]



        ''' VDD Rail, VSS Rail, XVTLayer '''
        # VSS M2
        leftBoundary = self.getXYLeft('DFFQb1','TG1', 'vss_supply_m2_y')[0][0]
        rightBoundary = self.getXYRight('DFFQb2','INV5', 'PbodyContact', '_Met2Layer')[0][0]
        self._DesignParameter['VSSRail_Met2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('DFFQb2','INV5', 'PbodyContact', '_Met2Layer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, 0]]
        )
        # VSS OD(RX)
        leftBoundary = self.getXYLeft('DFFQb1','TG1', 'vss_odlayer')[0][0]
        rightBoundary = self.getXYRight('DFFQb2','INV5', 'PbodyContact', '_ODLayer')[0][0]
        self._DesignParameter['VSSRail_OD'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('DFFQb2','INV5', 'PbodyContact', '_ODLayer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, 0]]
        )
        # VSS PP(BP)
        leftBoundary = self.getXYLeft('DFFQb1','TG1', 'vss_pplayer')[0][0]
        rightBoundary = self.getXYRight('DFFQb2','INV5', 'PbodyContact', '_PPLayer')[0][0]
        self._DesignParameter['VSSRail_PP'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('DFFQb2','INV5', 'PbodyContact', '_PPLayer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, 0]]
        )
        ## VDD
        # VDD M2
        leftBoundary = self.getXYLeft('DFFQb1','TG1', 'vdd_supply_m2_y')[0][0]
        rightBoundary = self.getXYRight('DFFQb2','INV5', 'NbodyContact', '_Met2Layer')[0][0]
        self._DesignParameter['VDDRail_Met2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('DFFQb2','INV5', 'NbodyContact', '_Met2Layer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY('DFFQb2','INV5', 'NbodyContact', '_Met2Layer')[0][1]]]
        )
        # VDD OD(RX)
        leftBoundary = self.getXYLeft('DFFQb1','TG1', 'vdd_odlayer')[0][0]
        rightBoundary = self.getXYRight('DFFQb2','INV5', 'NbodyContact', '_ODLayer')[0][0]
        self._DesignParameter['VDDRail_OD'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('DFFQb2','INV5', 'NbodyContact', '_ODLayer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY('DFFQb2','INV5', 'NbodyContact', '_ODLayer')[0][1]]]
        )

        # NWLayer
        leftBoundary = self.getXYLeft('DFFQb1','TG1', 'NWELL_boundary_0')[0][0]
        rightBoundary = self.getXYRight('DFFQb2','INV5', '_NWLayerBoundary')[0][0]
        topBoundary = self.getXYTop('DFFQb1', '_NWLayer')[0][1]
        botBoundary = self.getXYBot('DFFQb1', '_NWLayer')[0][1]
        self._DesignParameter['_NWLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=topBoundary - botBoundary,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, (topBoundary + botBoundary) / 2]]
        )

        # PPLayer (ADDED by smlim)
        leftBoundary = self.getXYLeft('DFFQb1','TG1', 'pmos', '_PPLayer')[0][0]
        rightBoundary = self.getXYRight('DFFQb2','INV5', '_PMOS', '_PPLayer')[0][0]

        topBoundary =  self.getXYTop('DFFQb1', '_PPLayer')[0][1]
        botBoundary =  self.getXYBot('DFFQb1', '_PPLayer')[0][1]

        self._DesignParameter['_PPLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=topBoundary - botBoundary,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, (topBoundary + botBoundary) / 2]]
        )

        # XVTLayer
        assert XVT in ('SLVT', 'LVT', 'RVT', 'HVT')
        leftBoundary = self.getXYLeft('DFFQb1','TG1', 'XVT_boundary_1')[0][0]
        rightBoundary = self.getXYRight('DFFQb2','INV5', 'XVTLayer')[0][0]
        self._DesignParameter['XVTLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[XVT][0], _Datatype=DesignParameters._LayerMapping[XVT][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('DFFQb2','INV5', 'XVTLayer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY('DFFQb2','INV5', 'XVTLayer')[0][1]]]
        )

        tmpMet2Width = 66
        tmpDRC_Met2Spacing = 86
        tmpVia1YWidth = 100
        tmpViaMet2Width = 134
        tmpViaminWidth = 170


        ####################### DFFQb1 & DFFQb2 connection ##########################

        self._DesignParameter['_Met2_connect'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met2_connect']['_XYCoordinates'] = [[[self.getXY('DFFQb1', '_qpin')[0][0],self._DesignParameter['DFFQb1']['_DesignObj'].iclkb],\
                                                                  [self.getXY('DFFQb2', '_dpin')[0][0],self._DesignParameter['DFFQb1']['_DesignObj'].iclkb]]]


        self._DesignParameter['_ViaMet12Met2_connect'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_ViaMet12Met2_connectIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2_connect']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=1))
        self._DesignParameter['_ViaMet12Met2_connect']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet12Met2_connect']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet12Met2_connect']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = tmpVia1YWidth


        self._DesignParameter['_ViaMet12Met2_connect']['_XYCoordinates'] = [[self.getXY('DFFQb2', '_dpin')[0][0],self._DesignParameter['DFFQb1']['_DesignObj'].iclkb+ tmpViaMet2Width / 2 - tmpMet2Width / 2]]

        ######################## DFFQb2 out to DFFQb1 in ##########################

        self._DesignParameter['_ViaMet12Met2_fb'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_ViaMet12Met2_fbIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2_fb']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=1))
        self._DesignParameter['_ViaMet12Met2_fb']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet12Met2_fb']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet12Met2_fb']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = tmpVia1YWidth

        self._DesignParameter['_ViaMet22Met3_fb'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='_ViaMet22Met3_fbIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3_fb']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=1))
        self._DesignParameter['_ViaMet22Met3_fb']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet22Met3_fb']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet22Met3_fb']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = tmpVia1YWidth



        self._DesignParameter['_ViaMet12Met2_fb']['_XYCoordinates'] = [[self.getXY('DFFQb2','_qbpin')[0][0] ,self._DesignParameter['DFFQb1']['_DesignObj'].rib ],\
                                                                         [self.getXY('DFFQb1', '_dpin')[0][0],self._DesignParameter['DFFQb1']['_DesignObj'].rib- tmpViaminWidth/2+ tmpMet2Width / 2]]
        self._DesignParameter['_ViaMet22Met3_fb']['_XYCoordinates'] = [[self.getXY('DFFQb2','_qbpin')[0][0],self._DesignParameter['DFFQb1']['_DesignObj'].rib],\
                                                                         [self.getXY('DFFQb1', '_dpin')[0][0],self._DesignParameter['DFFQb1']['_DesignObj'].rib- tmpViaminWidth/2+ tmpMet2Width / 2]]


        self._DesignParameter['_Met3_fb'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met3_fb']['_XYCoordinates'] = [[[self.getXY('DFFQb2','_qbpin')[0][0] ,self._DesignParameter['DFFQb1']['_DesignObj'].rib],\
                                                                  [self.getXY('DFFQb1', '_dpin')[0][0],self._DesignParameter['DFFQb1']['_DesignObj'].rib]]]



        ######################## Divided Clock output ##########################
        revise_dib = self._DesignParameter['DFFQb1']['_DesignObj'].iclkb - tmpViaMet2Width - tmpDRC_Met2Spacing

        self._DesignParameter['_ViaMet12Met2_data'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_ViaMet12Met2_dataIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2_data']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=1))
        self._DesignParameter['_ViaMet12Met2_data']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet12Met2_data']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet12Met2_data']['_DesignObj']._DesignParameter['_COLayer']['_XWidth'] = tmpVia1YWidth

        self._DesignParameter['_ViaMet22Met3_data'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='_ViaMet22Met3_dataIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3_data']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=1))
        self._DesignParameter['_ViaMet22Met3_data']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet22Met3_data']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet22Met3_data']['_DesignObj']._DesignParameter['_COLayer']['_XWidth'] = tmpVia1YWidth


        self._DesignParameter['_ViaMet12Met2_data']['_XYCoordinates'] = [[self.getXY('DFFQb1','_qbpin')[0][0] - tmpViaminWidth/2+ tmpMet2Width / 2,self._DesignParameter['DFFQb1']['_DesignObj'].iclk ],\
                                                                         [self.getXY('DFFQb2', '_qbpin')[0][0]- tmpViaminWidth/2+ tmpMet2Width / 2,self._DesignParameter['DFFQb1']['_DesignObj'].iclk]]
        self._DesignParameter['_ViaMet22Met3_data']['_XYCoordinates'] = [[self.getXY('DFFQb1','_qbpin')[0][0]- tmpViaminWidth/2+ tmpMet2Width / 2,self._DesignParameter['DFFQb1']['_DesignObj'].iclk],\
                                                                         [self.getXY('DFFQb2', '_qbpin')[0][0]- tmpViaminWidth/2+ tmpMet2Width / 2,self._DesignParameter['DFFQb1']['_DesignObj'].iclk]]

        self._DesignParameter['_Met1_clkout'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met1_clkout']['_XYCoordinates'] = [[[self.getXY('DFFQb1', '_clkpin')[0][0],revise_dib],\
                                                                  [self.getXY('DFFQb1', '_clkpin')[0][0],self.getXY('DFFQb1', '_clkpin')[0][1]]],\
                                                                [[self.getXY('DFFQb2', '_clkpin')[0][0],revise_dib],\
                                                                [self.getXY('DFFQb2', '_clkpin')[0][0],self.getXY('DFFQb2', '_clkpin')[0][1]]]]



        self.f = [self.getXY('DFFQb1', '_qpin')[-1][0],self._DesignParameter['DFFQb1']['_DesignObj'].iclkb]
        self.fb = [self.getXY('DFFQb1','_qbpin')[0][0] ,self._DesignParameter['DFFQb1']['_DesignObj'].iclk]
        self.f90 = [self.getXY('DFFQb2', '_qpin')[-1][0],self._DesignParameter['DFFQb1']['_DesignObj'].iclkb]
        self.f90b = [self.getXY('DFFQb2', '_qbpin')[0][0] ,self._DesignParameter['DFFQb1']['_DesignObj'].iclk]



        ######################################## clk input ################################

        revise_dib = self._DesignParameter['DFFQb1']['_DesignObj'].iclkb - tmpViaMet2Width - tmpDRC_Met2Spacing

        self._DesignParameter['_Met1_clk'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met1_clk']['_XYCoordinates'] = [[[self.getXY('DFFQb1', '_clkpin')[0][0],revise_dib],\
                                                                  [self.getXY('DFFQb1', '_clkpin')[0][0],self.getXY('DFFQb1', '_clkpin')[0][1]]],\
                                                                [[self.getXY('DFFQb2', '_clkpin')[0][0],revise_dib],\
                                                                [self.getXY('DFFQb2', '_clkpin')[0][0],self.getXY('DFFQb2', '_clkpin')[0][1]]]]

        self._DesignParameter['_Met3_clk'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met3_clk']['_XYCoordinates'] = [[[self.getXY('DFFQb1', '_clkpin')[0][0],revise_dib],\
                                                                  [self.getXY('DFFQb2', '_clkpin')[0][0],revise_dib]]]


        self._DesignParameter['_ViaMet12Met2_clk'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_ViaMet12Met2_clkIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2_clk']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=1))
        self._DesignParameter['_ViaMet12Met2_clk']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet12Met2_clk']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet12Met2_clk']['_DesignObj']._DesignParameter['_COLayer']['_XWidth'] = tmpVia1YWidth

        self._DesignParameter['_ViaMet22Met3_clk'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='_ViaMet22Met3_clkIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3_clk']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=1))
        self._DesignParameter['_ViaMet22Met3_clk']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet22Met3_clk']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet22Met3_clk']['_DesignObj']._DesignParameter['_COLayer']['_XWidth'] = tmpVia1YWidth



        self._DesignParameter['_ViaMet12Met2_clk']['_XYCoordinates'] = [[self.getXY('DFFQb1', '_clkpin')[0][0]- tmpViaminWidth/2+ tmpMet2Width / 2,revise_dib ],\
                                                                         [self.getXY('DFFQb2', '_clkpin')[0][0]- tmpViaminWidth/2+ tmpMet2Width / 2,revise_dib ]]
        self._DesignParameter['_ViaMet22Met3_clk']['_XYCoordinates'] = [[self.getXY('DFFQb1', '_clkpin')[0][0]- tmpViaminWidth/2+ tmpMet2Width / 2,revise_dib ],\
                                                                         [self.getXY('DFFQb2', '_clkpin')[0][0]- tmpViaminWidth/2+ tmpMet2Width / 2,revise_dib ]]


        self.clkinput = [self.getXY('DFFQb1', '_clkpin')[0][0],revise_dib]


        ########################## cell width ##################
        self.CellXWidth = max(self.getXY('DFFQb2','INV5', '_PMOS', '_POLayer')[-1][0],self.getXY('DFFQb2','INV5', '_PMOS', '_POLayer')[0][0]) + UnitPitch
        self.CellYWidth = CellHeight




''' INV2&3 # of Fingers should be less than 7(6 max)
    otherwise, INV inner routing and qb routing will be overlapped'''
################################ DRC Check #################################
import random
if __name__ == '__main__':
    # for i in range(0,100):
    #     TG1_Finger = random.randint(1,5)
    #     TG2_Finger = random.randint(1, 5)
    #     TSI1_Finger = random.randint(1,2)
    #     TSI2_Finger = random.randint(1,2)
    #     INV1_Finger = random.randint(1,5)
    #     INV2_Finger = random.randint(1,5)
    #     INV3_Finger = random.randint(1,5)
    #     INV4_Finger = random.randint(1,5)
    #     INV5_Finger = random.randint(1,5)

        npratio =2

        # TG1_NMWidth = random.randrange(200, 250, 2)
        # TG1_PMWidth = TG1_NMWidth*npratio
        # TG2_NMWidth = random.randrange(200, 250, 2)
        # TG2_PMWidth = TG2_NMWidth*npratio
        # TSI1_NMWidth = random.randrange(200, 250, 2)
        # TSI1_PMWidth = TSI1_NMWidth*npratio
        # TSI2_NMWidth = random.randrange(200, 250, 2)
        # TSI2_PMWidth = TSI2_NMWidth*npratio
        # INV1_NMWidth = random.randrange(200, 250, 2)
        # INV1_PMWidth = INV1_NMWidth*npratio
        # INV2_NMWidth = random.randrange(200, 250, 2)
        # INV2_PMWidth = INV2_NMWidth*npratio
        # INV3_NMWidth = random.randrange(200, 250, 2)
        # INV3_PMWidth = INV3_NMWidth*npratio
        # INV4_NMWidth = random.randrange(200, 250, 2)
        # INV4_PMWidth = INV4_NMWidth*npratio
        # INV5_NMWidth = random.randrange(200, 250, 2)
        # INV5_PMWidth = INV4_NMWidth * npratio

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

        INV5_NMWidth = 200
        INV5_PMWidth = 400

        TG1_Finger = 1
        TG2_Finger = 2
        TSI1_Finger = 1
        TSI2_Finger = 1
        INV1_Finger = 3
        INV2_Finger = 1
        INV3_Finger = 1
        INV4_Finger = 4
        INV5_Finger = 4

        ChannelLength = 30
        GateSpacing = 100
        SDWidth = 66
        XVT = 'SLVT'
        CellHeight = 1800
        SupplyRailType = 2


        # print("itr = ", i)
        # print("TG1_Finger = ", TG1_Finger)
        # print("TSI1_Finger = ", TSI1_Finger)
        # print("TSI2_Finger = ", TSI2_Finger)
        # print("INV1_Finger = ", INV1_Finger)
        # print("INV2_Finger = ", INV2_Finger)
        # print("INV3_Finger = ", INV3_Finger)
        # print("INV4_Finger = ", INV4_Finger)
        # print("INV5_Finger = ", INV5_Finger)

        DesignParameters._Technology = 'SS28nm'
        TopObj = Clk_Driver(_DesignParameter=None, _Name='Clk_Driver')
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

            INV5_Finger=INV5_Finger,
            INV5_NMWidth=INV5_NMWidth,
            INV5_PMWidth=INV5_PMWidth,

            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            SDWidth=SDWidth,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType)

        TopObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=TopObj._DesignParameter)
        testStreamFile = open('./Clk_Driver.gds', 'wb')
        tmp = TopObj._CreateGDSStream(TopObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()
        print('#############################      Sending to FTP Server...      ##############################')

        import ftplib

        ftp = ftplib.FTP('141.223.24.53')
        ftp.login('ljw95', 'dlwodn123')
        ftp.cwd('/mnt/sdc/ljw95/OPUS/ss28')
        myfile = open('Clk_Driver.gds', 'rb')
        ftp.storbinary('STOR Clk_Driver.gds', myfile)
        myfile.close()

        # import DRCchecker
        # a = DRCchecker.DRCchecker('ljw95','dlwodn123','/mnt/sdc/ljw95/OPUS/ss28','/mnt/sdc/ljw95/OPUS/ss28/DRC/run','Clk_Driver','Clk_Driver',None)
        # a.DRCchecker()
        #
        # print ("DRC Clean!!!")
