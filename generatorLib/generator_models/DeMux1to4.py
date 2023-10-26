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
from generatorLib.generator_models import DFF_Latch
from generatorLib.generator_models import DFFQ
from generatorLib.generator_models import DeMux1to2
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaMet22Met3
from generatorLib.generator_models import DFF_Latch_Latch
from generatorLib.generator_models import DFF_Q_Latch



class DeMux1to4(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name='DeMux1to4'):
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

                                  INV4_Finger=3,
                                  INV4_NMWidth=200,
                                  INV4_PMWidth=400,

                                  TG3_Finger=2,
                                  TG3_NMWidth=200,
                                  TG3_PMWidth=400,

                                  TSI3_Finger=1,
                                  TSI3_NMWidth=200,
                                  TSI3_PMWidth=400,

                                  INV5_Finger=4,
                                  INV5_NMWidth=200,
                                  INV5_PMWidth=400,

                                  INV6_Finger=4,
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




        Parameters_DFF_Latch_Latch = dict(
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

        Parameters_DFF_Q_Latch = dict(
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

            INV4_Finger=INV5_Finger,
            INV4_NMWidth=INV5_NMWidth,
            INV4_PMWidth=INV5_PMWidth,

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
        Parameters_DeMux1to2 = dict(
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
        self._DesignParameter['DFF_Latch_Latch'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=DFF_Latch_Latch.DFF(_Name='DFF_Latch_LatchIn{}'.format(_Name)))[0]
        self._DesignParameter['DFF_Latch_Latch']['_DesignObj']._CalculateDesignParameter(**Parameters_DFF_Latch_Latch)
        self._DesignParameter['DFF_Latch_Latch']['_XYCoordinates'] = [[0, 0]]


        self._DesignParameter['DFF_Q_Latch'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=DFF_Q_Latch.DFF(_Name='DFF_Q_LatchIn{}'.format(_Name)))[0]
        self._DesignParameter['DFF_Q_Latch']['_DesignObj']._CalculateDesignParameter(**Parameters_DFF_Q_Latch)
        self._DesignParameter['DFF_Q_Latch']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['DeMux1to2'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=DeMux1to2.DeMux1to2(_Name='DeMux1to2In{}'.format(_Name)))[0]
        self._DesignParameter['DeMux1to2']['_DesignObj']._CalculateDesignParameter(**Parameters_DeMux1to2)
        self._DesignParameter['DeMux1to2']['_XYCoordinates'] = [[0, 0]]




        self._DesignParameter['DFF_Latch_Latch']['_XYCoordinates'] = [[0,0]]
        self._DesignParameter['DFF_Q_Latch']['_XYCoordinates'] = [\
            [self.getXY('DFF_Latch_Latch')[0][0] + self._DesignParameter['DFF_Latch_Latch']['_DesignObj'].CellXWidth  + 1 * UnitPitch  , 0]]
        self._DesignParameter['DeMux1to2']['_XYCoordinates']=[\
             [self.getXY('DFF_Q_Latch')[0][0] + self._DesignParameter['DFF_Q_Latch']['_DesignObj'].CellXWidth  + 1 * UnitPitch  , 0]]


        ''' VDD Rail, VSS Rail, XVTLayer '''
        # VSS M2
        leftBoundary = self.getXYLeft('DFF_Latch_Latch','TG1', 'vss_supply_m2_y')[0][0]
        rightBoundary = self.getXYRight('DeMux1to2','DFFQ','INV4', 'PbodyContact', '_Met2Layer')[0][0]
        self._DesignParameter['VSSRail_Met2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('DeMux1to2','DFFQ','INV4', 'PbodyContact', '_Met2Layer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, 0]]
        )
        # VSS OD(RX)
        leftBoundary = self.getXYLeft('DFF_Latch_Latch','TG1', 'vss_odlayer')[0][0]
        rightBoundary = self.getXYRight('DeMux1to2','DFFQ','INV4', 'PbodyContact', '_ODLayer')[0][0]
        self._DesignParameter['VSSRail_OD'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('DeMux1to2','DFFQ','INV4', 'PbodyContact', '_ODLayer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, 0]]
        )
        # VSS PP(BP)
        leftBoundary = self.getXYLeft('DFF_Latch_Latch','TG1', 'vss_pplayer')[0][0]
        rightBoundary = self.getXYRight('DeMux1to2','DFFQ','INV4', 'PbodyContact', '_PPLayer')[0][0]
        self._DesignParameter['VSSRail_PP'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('DeMux1to2','DFFQ','INV4', 'PbodyContact', '_PPLayer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, 0]]
        )
        ## VDD
        # VDD M2
        leftBoundary = self.getXYLeft('DFF_Latch_Latch','TG1', 'vdd_supply_m2_y')[0][0]
        rightBoundary = self.getXYRight('DeMux1to2','DFFQ','INV4', 'NbodyContact', '_Met2Layer')[0][0]
        self._DesignParameter['VDDRail_Met2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('DeMux1to2','DFFQ','INV4', 'NbodyContact', '_Met2Layer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY('DeMux1to2','DFFQ','INV4', 'NbodyContact', '_Met2Layer')[0][1]]]
        )
        # VDD OD(RX)
        leftBoundary = self.getXYLeft('DFF_Latch_Latch','TG1', 'vdd_odlayer')[0][0]
        rightBoundary = self.getXYRight('DeMux1to2','DFFQ','INV4', 'NbodyContact', '_ODLayer')[0][0]
        self._DesignParameter['VDDRail_OD'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('DeMux1to2','DFFQ','INV4', 'NbodyContact', '_ODLayer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY('DeMux1to2','DFFQ','INV4', 'NbodyContact', '_ODLayer')[0][1]]]
        )

        # NWLayer
        leftBoundary = self.getXYLeft('DFF_Latch_Latch','TG1', 'NWELL_boundary_0')[0][0]
        rightBoundary = self.getXYRight('DeMux1to2','DFFQ','INV4', '_NWLayerBoundary')[0][0]
        topBoundary = self.getXYTop('DFF_Latch_Latch', '_NWLayer')[0][1]
        botBoundary = self.getXYBot('DeMux1to2','DFFQ', '_NWLayer')[0][1]
        self._DesignParameter['_NWLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=topBoundary - botBoundary,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, (topBoundary + botBoundary) / 2]]
        )

        # PPLayer (ADDED by smlim)
        leftBoundary = self.getXYLeft('DFF_Latch_Latch','TG1', 'pmos', '_PPLayer')[0][0]
        rightBoundary = self.getXYRight('DeMux1to2','DFFQ','INV4', '_PMOS', '_PPLayer')[0][0]

        topBoundary =  self.getXYTop('DFF_Latch_Latch', '_PPLayer')[0][1]
        botBoundary =  self.getXYBot('DeMux1to2','DFFQ','_PPLayer')[0][1]

        self._DesignParameter['_PPLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=topBoundary - botBoundary,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, (topBoundary + botBoundary) / 2]]
        )
        # self._DesignParameter['TG1']['_DesignObj']._DesignParameter['vss_pplayer']['_YWidth'] = self.getYWidth('INV1', 'PbodyContact', '_PPLayer')
        # self._DesignParameter['TG2']['_DesignObj']._DesignParameter['vss_pplayer']['_YWidth'] = self.getYWidth('INV1', 'PbodyContact', '_PPLayer')

        # XVTLayer
        assert XVT in ('SLVT', 'LVT', 'RVT', 'HVT')
        leftBoundary = self.getXYLeft('DFF_Latch_Latch','TG1', 'XVT_boundary_1')[0][0]
        rightBoundary = self.getXYRight('DeMux1to2','DFFQ','INV4', 'XVTLayer')[0][0]
        self._DesignParameter['XVTLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[XVT][0], _Datatype=DesignParameters._LayerMapping[XVT][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('DeMux1to2','DFFQ','INV4', 'XVTLayer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY('DeMux1to2','DFFQ','INV4', 'XVTLayer')[0][1]]]
        )


        tmpMet2Width = 66
        tmpDRC_Met2Spacing = 86
        tmpVia1YWidth = 100
        tmpViaMet2Width = 134
        tmpViaminWidth = 170



        ####################### Data input Routing ##########################
        self._DesignParameter['_ViaMet12Met2_datain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_ViaMet12Met2_datainIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2_datain']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=1))
        self._DesignParameter['_ViaMet12Met2_datain']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet12Met2_datain']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet12Met2_datain']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = tmpVia1YWidth

        self._DesignParameter['_ViaMet22Met3_datain'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='_ViaMet22Met3_datainIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3_datain']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=1))
        self._DesignParameter['_ViaMet22Met3_datain']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet22Met3_datain']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = tmpViaMet2Width
        self._DesignParameter['_ViaMet22Met3_datain']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = tmpVia1YWidth

        self._DesignParameter['_ViaMet12Met2_datain']['_XYCoordinates'] = [[self.getXY('DFF_Q_Latch','_dpin')[0][0],self._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib - tmpViaminWidth / 2 + tmpMet2Width / 2],\
                                                                         [self.getXY('DFF_Latch_Latch','_dpin')[0][0],self._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib - tmpViaminWidth / 2 + tmpMet2Width / 2]]
        self._DesignParameter['_ViaMet22Met3_datain']['_XYCoordinates'] = [[self.getXY('DFF_Q_Latch','_dpin')[0][0],self._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib - tmpViaMet2Width / 2 + tmpMet2Width / 2],\
                                                                         [self.getXY('DFF_Latch_Latch','_dpin')[0][0],self._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib - tmpViaMet2Width / 2 + tmpMet2Width / 2]]

        self._DesignParameter['_Met3_data'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met3_data']['_XYCoordinates'] = [[[self.getXY('DFF_Latch_Latch','TG1', '_Apin')[0][0],self._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib],\
                                                                  [self.getXY('DeMux1to2','DFFQ','TG1', '_Apin')[0][0],self._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib]]]

        self.data = [(self.getXY('DeMux1to2','DFFQ','TG1', '_Apin')[0][0]-self.getXY('DFF_Latch_Latch','TG1', '_Apin')[0][0])/2+self.getXY('DFF_Latch_Latch','TG1', '_Apin')[0][0],\
                     self._DesignParameter['DFF_Latch_Latch']['_DesignObj'].rib - tmpViaMet2Width / 2 + tmpMet2Width / 2]



        ######################## Data output Routing ##########################
        revise_dib = self._DesignParameter['DFF_Latch_Latch']['_DesignObj'].iclkb - tmpViaMet2Width - tmpDRC_Met2Spacing

        self._DesignParameter['_Met1_dataout'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met1_dataout']['_XYCoordinates'] = [[[self.getXY('DFF_Latch_Latch','INV8', 'InputMet1')[0][0],self.getXY('DFF_Latch_Latch','INV8', 'InputMet1')[0][1]],\
                                                                     [self.getXY('DFF_Latch_Latch','INV8', 'InputMet1')[0][0],revise_dib]]]


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



        self._DesignParameter['_ViaMet12Met2_data']['_XYCoordinates'] = [[self.getXY('DFF_Latch_Latch','INV8', 'InputMet1')[0][0] - tmpViaminWidth/2+ tmpMet2Width / 2,revise_dib ],\
                                                                         [self.getXY('DFF_Q_Latch', '_qbpin')[0][0]+ tmpViaminWidth/2- tmpMet2Width / 2,revise_dib]]
        self._DesignParameter['_ViaMet22Met3_data']['_XYCoordinates'] = [[self.getXY('DFF_Latch_Latch','INV8', 'InputMet1')[0][0]- tmpViaminWidth/2+ tmpMet2Width / 2,revise_dib ],\
                                                                         [self.getXY('DFF_Q_Latch', '_qbpin')[0][0]+ tmpViaminWidth/2- tmpMet2Width / 2,revise_dib ]]

        self._DesignParameter['_ViaMet12Met2_data2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_ViaMet12Met2_data2In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2_data2']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=1))
        self._DesignParameter['_ViaMet12Met2_data2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet12Met2_data2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet12Met2_data2']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = tmpVia1YWidth

        self._DesignParameter['_ViaMet22Met3_data2'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='_ViaMet22Met3_data2In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3_data2']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=1))
        self._DesignParameter['_ViaMet22Met3_data2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet22Met3_data2']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = tmpViaminWidth
        self._DesignParameter['_ViaMet22Met3_data2']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = tmpVia1YWidth


        self._DesignParameter['_ViaMet12Met2_data2']['_XYCoordinates'] = [[self.getXY('DeMux1to2','DFF_Latch', '_qbpin')[0][0],self._DesignParameter['DeMux1to2']['_DesignObj']._DesignParameter['DFF_Latch']['_DesignObj'].iclkb- tmpViaMet2Width / 2 + tmpMet2Width / 2 ],\
                                                                         [self.getXY('DeMux1to2','DFFQ', '_qpin')[0][0],self._DesignParameter['DeMux1to2']['_DesignObj']._DesignParameter['DFF_Latch']['_DesignObj'].iclkb]]##DRC 수정
        self._DesignParameter['_ViaMet22Met3_data2']['_XYCoordinates'] = [[self.getXY('DeMux1to2','DFF_Latch', '_qbpin')[0][0],self._DesignParameter['DeMux1to2']['_DesignObj']._DesignParameter['DFF_Latch']['_DesignObj'].iclkb- tmpViaMet2Width / 2 + tmpMet2Width / 2 ],\
                                                                         [self.getXY('DeMux1to2','DFFQ', '_qpin')[0][0],self._DesignParameter['DeMux1to2']['_DesignObj']._DesignParameter['DFF_Latch']['_DesignObj'].iclkb]]



        self.D1 = [self.getXY('DFF_Latch_Latch','INV8', 'InputMet1')[0][0],revise_dib]
        self.D3 = [self.getXY('DFF_Q_Latch', '_qbpin')[0][0],revise_dib]
        self.D2 = [self.getXY('DeMux1to2','DFF_Latch', '_qbpin')[0][0],self._DesignParameter['DeMux1to2']['_DesignObj']._DesignParameter['DFF_Latch']['_DesignObj'].iclkb- tmpViaMet2Width / 2 + tmpMet2Width / 2]
        self.D4 = [self.getXY('DeMux1to2','DFFQ', '_qpin')[0][0],self._DesignParameter['DeMux1to2']['_DesignObj']._DesignParameter['DFF_Latch']['_DesignObj'].iclkb]


        ######################## clk Routing ##########################

        self._DesignParameter['_Met1_clk'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _Width=tmpMet2Width
        )
        self._DesignParameter['_Met1_clk']['_XYCoordinates'] = [[[self.getXY('DFF_Latch_Latch', '_clkpin')[0][0],revise_dib],\
                                                                  [self.getXY('DFF_Latch_Latch', '_clkpin')[0][0],self.getXY('DFF_Latch_Latch', '_clkpin')[0][1]]],\
                                                                [[self.getXY('DFF_Q_Latch', '_clkpin')[0][0],revise_dib],\
                                                                [self.getXY('DFF_Q_Latch', '_clkpin')[0][0],self.getXY('DFF_Q_Latch', '_clkpin')[0][1]]],\
                                                                [[self.getXY('DFF_Latch_Latch', '_clk90pin')[0][0],revise_dib],\
                                                                [self.getXY('DFF_Latch_Latch', '_clk90pin')[0][0],self.getXY('DFF_Latch_Latch', '_clk90pin')[0][1]]],\
                                                                [[self.getXY('DFF_Q_Latch', '_clk90pin')[0][0],revise_dib],\
                                                                [self.getXY('DFF_Q_Latch', '_clk90pin')[0][0],self.getXY('DFF_Q_Latch', '_clk90pin')[0][1]]]]


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



        self._DesignParameter['_ViaMet12Met2_clk']['_XYCoordinates'] = [[self.getXY('DFF_Latch_Latch', '_clkpin')[0][0] - tmpViaminWidth/2+ tmpMet2Width / 2,revise_dib ],\
                                                                         [self.getXY('DFF_Q_Latch', '_clkpin')[0][0]- tmpViaminWidth/2+ tmpMet2Width / 2,revise_dib],\
                                                                        [self.getXY('DFF_Latch_Latch', '_clk90pin')[0][0]- tmpViaminWidth/2+ tmpMet2Width / 2,revise_dib],\
                                                                        [self.getXY('DFF_Q_Latch', '_clk90pin')[0][0]- tmpViaminWidth/2+ tmpMet2Width / 2,revise_dib]]
        self._DesignParameter['_ViaMet22Met3_clk']['_XYCoordinates'] = [[self.getXY('DFF_Latch_Latch', '_clkpin')[0][0]- tmpViaminWidth/2+ tmpMet2Width / 2,revise_dib ],\
                                                                         [self.getXY('DFF_Q_Latch', '_clkpin')[0][0]- tmpViaminWidth/2+ tmpMet2Width / 2,revise_dib ],\
                                                                        [self.getXY('DFF_Latch_Latch', '_clk90pin')[0][0]- tmpViaminWidth/2+ tmpMet2Width / 2,revise_dib],\
                                                                        [self.getXY('DFF_Q_Latch', '_clk90pin')[0][0]- tmpViaminWidth/2+ tmpMet2Width / 2,revise_dib]]


        self.clk = [self.getXY('DFF_Latch_Latch', '_clkpin')[0][0],revise_dib]
        self.clkb = [self.getXY('DFF_Q_Latch', '_clkpin')[0][0],revise_dib]
        self.clk90 = [[self.getXY('DFF_Latch_Latch', '_clk90pin')[0][0],revise_dib],\
                      [self.getXY('DFF_Q_Latch', '_clk90pin')[0][0],revise_dib],\
                      [self.getXY('DeMux1to2','DFF_Latch', '_clkpin')[0][0],revise_dib]]
        self.clk90b = [self.getXY('DeMux1to2','DFFQ', '_clkpin')[0][0],revise_dib]


''' INV2&3 # of Fingers should be less than 7(6 max)
    otherwise, INV inner routing and qb routing will be overlapped'''
################################ DRC Check #################################
import random
if __name__ == '__main__':
   # for i in range(0,100):
        TG1_Finger = random.randint(1, 5)
        TG2_Finger = random.randint(1, 5)
        TSI1_Finger = random.randint(1, 2)
        TSI2_Finger = random.randint(1, 2)
        INV1_Finger = random.randint(1, 5)
        INV2_Finger = random.randint(1, 5)
        INV3_Finger = random.randint(1, 5)
        INV4_Finger = random.randint(1, 5)

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

        npratio =2

        # TG1_NMWidth = random.randrange(200, 250, 2)
        # TG1_PMWidth = TG1_NMWidth * npratio
        # TG2_NMWidth = random.randrange(200, 250, 2)
        # TG2_PMWidth = TG2_NMWidth * npratio
        # TSI1_NMWidth = random.randrange(200, 250, 2)
        # TSI1_PMWidth = TSI1_NMWidth * npratio
        # TSI2_NMWidth = random.randrange(200, 250, 2)
        # TSI2_PMWidth = TSI2_NMWidth * npratio
        # INV1_NMWidth = random.randrange(200, 250, 2)
        # INV1_PMWidth = INV1_NMWidth * npratio
        # INV2_NMWidth = random.randrange(200, 250, 2)
        # INV2_PMWidth = INV2_NMWidth * npratio
        # INV3_NMWidth = random.randrange(200, 250, 2)
        # INV3_PMWidth = INV3_NMWidth * npratio
        # INV4_NMWidth = random.randrange(200, 250, 2)
        # INV4_PMWidth = INV4_NMWidth * npratio

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

        TG4_NMWidth = 200
        TG4_PMWidth = 400

        TSI4_NMWidth = 200
        TSI4_PMWidth = 400

        INV7_NMWidth = 200
        INV7_PMWidth = 400

        INV8_NMWidth = 200
        INV8_PMWidth = 400

        INV9_NMWidth = 200
        INV9_PMWidth = 400

        INV10_NMWidth = 200
        INV10_PMWidth = 400

        ChannelLength = 30
        GateSpacing = 100
        SDWidth = 66
        XVT = 'SLVT'
        CellHeight = 1800
        SupplyRailType = 2

        TG1_Finger = 1
        TG2_Finger = 2 #not fo DFF_Q_Latch
        TSI1_Finger = 1
        TSI2_Finger = 1 #not fo DFF_Q_Latch #문제 2
        INV1_Finger = 3
        INV2_Finger = 1
        INV3_Finger = 1
        INV4_Finger = 3 #not fo DFF_Q_Latch
        TG3_Finger = 2
        TSI3_Finger = 1
        INV5_Finger = 4 #문제 1
        INV6_Finger = 4 #not fo DFF_Q_Latch
        TG4_Finger = 2
        TSI4_Finger = 1
        INV7_Finger = 4
        INV8_Finger = 4
        INV9_Finger = 1
        INV10_Finger = 1



        #print("itr = ", i)
        # print("TG1_Finger = ", TG1_Finger)
        # print("TSI1_Finger = ", TSI1_Finger)
        # print("TSI2_Finger = ", TSI2_Finger)
        # print("INV1_Finger = ", INV1_Finger)
        # print("INV2_Finger = ", INV2_Finger)
        # print("INV3_Finger = ", INV3_Finger)
        # print("INV4_Finger = ", INV4_Finger)

        DesignParameters._Technology = 'SS28nm'
        TopObj = DeMux1to4(_DesignParameter=None, _Name='DeMux1to4')
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

            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            SDWidth=SDWidth,
            XVT=XVT,
            CellHeight=CellHeight,
            SupplyRailType=SupplyRailType)

        TopObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=TopObj._DesignParameter)
        testStreamFile = open('./DeMux1to4.gds', 'wb')
        tmp = TopObj._CreateGDSStream(TopObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()
        print('#############################      Sending to FTP Server...      ##############################')

        import ftplib

        ftp = ftplib.FTP('141.223.24.53')
        ftp.login('ljw95', 'dlwodn123')
        ftp.cwd('/mnt/sdc/ljw95/OPUS/ss28')
        myfile = open('DeMux1to4.gds', 'rb')
        ftp.storbinary('STOR DeMux1to4.gds', myfile)
        myfile.close()

        import DRCchecker
        a = DRCchecker.DRCchecker('ljw95','dlwodn123','/mnt/sdc/ljw95/OPUS/ss28','/mnt/sdc/ljw95/OPUS/ss28/DRC/run','DeMux1to4','DeMux1to4',None)
        a.DRCchecker()

        print ("DRC Clean!!!")
