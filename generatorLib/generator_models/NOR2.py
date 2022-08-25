from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
import time
from generatorLib import DRC
from generatorLib import CoordinateCalc as CoordCalc
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import CascodePMOS
from generatorLib.generator_models import SupplyRails
from generatorLib.generator_models import Z_PWR_CNT
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import ViaPoly2Met1_resize


class NOR2(StickDiagram._StickDiagram):
    def __init__(self, _DesignParameter=None, _Name='NOR2'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name

        self.Num_HorizontalInputViaMode = 5

    def _CalculateDesignParameter(self,
                                  NumFinger_PM=1,
                                  NumFinger_NM=2,
                                  PMOSWidth=400,
                                  NMOSWidth=200,

                                  CellHeight=None,
                                  YCoordOfPM=None,
                                  YCoordOfNM=None,
                                  YCoordOfInputOutput=None,

                                  ChannelLength=30,
                                  GateSpacing=100,
                                  XVT='SLVT',
                                  SupplyRailType=1
                                  ):

        tmpLength = NMOSWidth + PMOSWidth

        self._CalculateDesignParameter_i(
            NumFinger_NM=NumFinger_NM,
            NumFinger_PM=NumFinger_PM,
            NMOSWidth=NMOSWidth,
            PMOSWidth=PMOSWidth,

            YCoordOfNM=tmpLength * 3,
            YCoordOfInputOutput=tmpLength * 6,
            YCoordOfPM=tmpLength * 9,
            CellHeight=tmpLength * 12,

            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            XVT=XVT,
            SupplyRailType=SupplyRailType,
        )

        ''' Calc Y-distance '''
        MinDistance = self._CalcMinDistance()   # dict VSS2NMOS_min, VDD2PMOS_min, NMOS2IO_min, PMOS2IO_min

        # CellHeight   - top priority
        MinCellHeight = MinDistance['VSS2NMOS_min'] + MinDistance['NMOS2IO_min'] + MinDistance['PMOS2IO_min'] + MinDistance['VDD2PMOS_min']
        if CellHeight == None:
            _CellHeight = MinCellHeight
        elif CellHeight < MinCellHeight:
            raise NotImplementedError(f"Input CellHeight={CellHeight}, But MinCellHeight={MinCellHeight}")
        else:
            _CellHeight = CellHeight

        # YCoordOfNM
        if YCoordOfNM == None:
            _YCoordOfNM = MinDistance['VSS2NMOS_min']
        elif YCoordOfNM < MinDistance['VSS2NMOS_min']:
            raise NotImplementedError(f"Input YCoordOfNM={YCoordOfNM}, But VSS2NMOS_min={MinDistance['VSS2NMOS_min']}")
        else:
            _YCoordOfNM = YCoordOfNM

        # YCoordOfPM
        if YCoordOfPM == None:
            _YCoordOfPM = _CellHeight - MinDistance['VDD2PMOS_min']
        elif YCoordOfPM > _CellHeight - MinDistance['VDD2PMOS_min']:
            raise NotImplementedError(f"Input YCoordOfPM={YCoordOfPM}, But YCoordOfPM_min={_CellHeight - MinDistance['VDD2PMOS_min']}")
        else:
            _YCoordOfPM = YCoordOfPM



        # YCoordOfInputOutput
        if (_YCoordOfPM - _YCoordOfNM) < (MinDistance['NMOS2IO_min'] + MinDistance['PMOS2IO_min']):
            raise NotImplementedError('Too short btw NMOS and PMOS')

        if YCoordOfInputOutput == None:
            _YCoordOfInputOutput = ((_YCoordOfNM + MinDistance['NMOS2IO_min']) + (_YCoordOfPM - MinDistance['PMOS2IO_min'])) / 2
        elif YCoordOfInputOutput < _YCoordOfNM + MinDistance['NMOS2IO_min']:
            raise NotImplementedError(f"YCoordOfInputOutput={YCoordOfInputOutput}, But MinBoundary={_YCoordOfNM + MinDistance['NMOS2IO_min']}")
        elif YCoordOfInputOutput > _YCoordOfPM - MinDistance['PMOS2IO_min']:
            raise NotImplementedError(f"YCoordOfInputOutput={YCoordOfInputOutput}, But MaxBoundary={_YCoordOfPM - MinDistance['PMOS2IO_min']}")
        else:
            _YCoordOfInputOutput = YCoordOfInputOutput




        # initialize
        tmpName = self._DesignParameter['_Name']['_Name']
        del self._DesignParameter
        self.__init__(_Name=tmpName)

        # re-calculate
        self._CalculateDesignParameter_i(
            NumFinger_NM=NumFinger_NM,
            NumFinger_PM=NumFinger_PM,
            NMOSWidth=NMOSWidth,
            PMOSWidth=PMOSWidth,

            YCoordOfNM=_YCoordOfNM,
            YCoordOfInputOutput=_YCoordOfInputOutput,
            YCoordOfPM=_YCoordOfPM,
            CellHeight=_CellHeight,

            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing, XVT=XVT,
            SupplyRailType=SupplyRailType,
        )


    def _CalcMinDistance(self):

        drc = DRC.DRC()

        ''' (1) VSS2NMOS_min {SupplyRailType}'''
        DistanceBtwVSS2NMOS1 = 0.5 * (self.getYWidth('VSSRail', '_PPLayer') + self.getYWidth('NMOS', '_POLayer'))
        DistanceBtwVSS2NMOS2 = 0.5 * (self.getYWidth('VSSRail', '_ODLayer') + self.getYWidth('NMOS', '_ODLayer')) + drc._OdMinSpace  # OD Layer(for Pbody) - OD Layer (for NMOS)     OD=RX
        if '_PODummyLayer' in self._DesignParameter['NMOS']['_DesignObj']._DesignParameter:
            DistanceBtwVSS2NMOS3 = 0.5 * (self.getYWidth('VSSRail', '_ODLayer') + self.getYWidth('NMOS', '_PODummyLayer')) + drc._PolygateMinSpace2OD  # OD Layer(for Pbody) - PO Dummy Layer (for NMOS)     OD=RX
        else:
            DistanceBtwVSS2NMOS3 = 0
        if self.SupplyRailType == 1:
            DistanceBtwVSS2NMOS4 = 0.5 * (self.getYWidth('VSSRail', '_Met1Layer') + self.getYWidth('NMOS', '_Met1Layer')) + drc._Metal1MinSpaceAtCorner
        else:       # if self.SupplyRailType == 2:
            DistanceBtwVSS2NMOS4 = 0.5 * self.getYWidth('NMOS', '_Met1Layer') + 0.5 * drc._Metal1MinSpaceAtCorner
        DistanceBtwVSS2NMOS5 = 0.5 * (self.getYWidth('VSSRail', '_PPLayer') + self.getYWidth('NMOS', '_ODLayer')) + drc._OdMinSpace2Pp
        VSS2NMOS_min = max(DistanceBtwVSS2NMOS1, DistanceBtwVSS2NMOS2, DistanceBtwVSS2NMOS3, DistanceBtwVSS2NMOS4, DistanceBtwVSS2NMOS5)

        ''' (2) VDD2PMOS_min {NumFinger_PM, SupplyRailType}'''
        if '_NPLayer' in self._DesignParameter['PMOS']['_DesignObj']._DesignParameter:
            DistanceBtwVDD2PMOS1 = 0.5 * (self.getYWidth('VDDRail', '_NPLayer') + self.getYWidth('PMOS', '_POLayer'))       # need to check
        else:
            DistanceBtwVDD2PMOS1 = 0
        DistanceBtwVDD2PMOS2 = 0.5 * (self.getYWidth('VDDRail', '_ODLayer') + self.getYWidth('PMOS', '_ODLayer')) + drc._OdMinSpace  # OD Layer(for Nbody) - OD Layer (for PMOS)     OD=RX
        if '_PODummyLayer' in self._DesignParameter['PMOS']['_DesignObj']._DesignParameter:
            DistanceBtwVDD2PMOS3 = 0.5 * (self.getYWidth('VDDRail', '_ODLayer') + self.getYWidth('PMOS', '_PODummyLayer')) + drc._PolygateMinSpace2OD  # OD Layer(for Nbody) - PO Dummy Layer (for PMOS)     OD=RX
        else:
            DistanceBtwVDD2PMOS3 = 0
        if self.NumFinger_PM == 1 and self.SupplyRailType == 1:
            DistanceBtwVDD2PMOS4 = 0.5 * (self.getYWidth('VDDRail', '_Met1Layer') + self.getYWidth('PMOS', '_Met1Layer')) + drc._Metal1MinSpaceAtCorner
        elif self.NumFinger_PM > 1 and self.SupplyRailType == 1:
            DistanceBtwVDD2PMOS4 = 0.5 * self.getYWidth('VDDRail', '_Met1Layer') + (self.getXYTop('Met1RouteX_PMUp')[0][1] - self.getXY('PMOS')[0][1]) + drc._Metal1MinSpaceAtCorner
        elif self.NumFinger_PM == 1 and self.SupplyRailType == 2:
            DistanceBtwVDD2PMOS4 = 0.5 * drc._Metal1MinSpaceAtCorner
        else:       # if self.NumFinger_PM != 1 and self.SupplyRailType == 2:
            DistanceBtwVDD2PMOS4 = (self.getXYTop('Met1RouteX_PMUp')[0][1] - self.getXY('PMOS')[0][1]) + 0.5 * drc._Metal1MinSpaceAtCorner
        DistanceBtwVDD2PMOS5 = 0.5 * (self.getYWidth('VDDRail', '_ODLayer') + self.getYWidth('PMOS', '_PPLayer')) + drc._OdMinSpace2Pp

        VDD2PMOS_min = max(DistanceBtwVDD2PMOS1, DistanceBtwVDD2PMOS2, DistanceBtwVDD2PMOS3, DistanceBtwVDD2PMOS4, DistanceBtwVDD2PMOS5)


        ''' (3) NMOS2IO_min {finger_nmos, finger_pmos(1ornot)} '''
        gapBtwMet1 = drc._Metal1MinSpaceAtCorner
        if self.NumFinger_NM == 1:
            if self.NumFinger_PM == 1:
                DistanceBtwNMOS2IO1 = 0.5 * (self.getYWidth('ViaPoly_InputAB', '_Met1Layer') + self.getYWidth('NMOS', '_Met1Layer')) + gapBtwMet1
            elif self.NumFinger_PM < self.Num_HorizontalInputViaMode:
                DistanceBtwNMOS2IO1 = 0.5 * self.getYWidth('ViaPoly_InputAB', '_Met1Layer') + (self.getXYTop('Met1RouteX_NMout')[0][1] - self.getXY('NMOS')[0][1]) + gapBtwMet1
            else:
                DistanceBtwNMOS2IO1 = 0.5 * (self.getYWidth('ViaPoly_InputAB', '_Met1Layer') + self.getYWidth('NMOS', '_Met1Layer')) + gapBtwMet1
        else:   # self.NumFinger_NM > 1:
            DistanceBtwNMOS2IO1 = 0.5 * self.getYWidth('ViaPoly_InputAB', '_Met1Layer') + (self.getXYTop('Met1RouteX_NMout')[0][1] - self.getXY('NMOS')[0][1]) + gapBtwMet1

        if '_PODummyLayer' in self._DesignParameter['NMOS']['_DesignObj']._DesignParameter:
            DistanceBtwNMOS2IO2 = 0.5 * (self.getYWidth('ViaPoly_InputAB', '_POLayer') + self.getYWidth('NMOS', '_PODummyLayer')) + drc._PolygateMinSpace
        else:
            DistanceBtwNMOS2IO2 = 0
        NMOS2IO_min = max(DistanceBtwNMOS2IO1, DistanceBtwNMOS2IO2)
        '''
        if self.NumFinger_PM == 1 and self.NumFinger_NM == 1:
            DistanceBtwNMOS2IO1 = 0.5 * (self.getYWidth('ViaPoly_InputAB', '_Met1Layer') + self.getYWidth('NMOS', '_Met1Layer')) + gapBtwMet1
        elif self.NumFinger_PM == 1 and self.NumFinger_NM > 1:
            DistanceBtwNMOS2IO1 = 0.5 * self.getYWidth('ViaPoly_InputAB', '_Met1Layer') + (self.getXYTop('Met1RouteX_NMout')[0][1] - self.getXY('NMOS')[0][1]) + gapBtwMet1

        elif self.NumFinger_PM > 1 and self.NumFinger_NM == 1:
            DistanceBtwNMOS2IO1 = 0.5 * self.getYWidth('ViaPoly_InputAB', '_Met1Layer') + (self.getXYTop('Met1RouteX_NMout')[0][1] - self.getXY('NMOS')[0][1]) + gapBtwMet1

        else:  # self.NumFinger_NM > 1:
            DistanceBtwNMOS2IO1 = 0.5 * self.getYWidth('ViaPoly_InputAB', '_Met1Layer') + (self.getXYTop('Met1RouteX_NMside')[0][1] - self.getXY('NMOS')[0][1]) + gapBtwMet1
        NMOS2IO_min = DistanceBtwNMOS2IO1
        '''

        ''' (4) PMOS2IO_min {finger_pmos, finger_max} '''
        gapBtwMet1 = drc._Metal1MinSpaceAtCorner
        if self.NumFinger_PM == 1:
            DistanceBtwPMOS2IO1 = 0.5 * (self.getYWidth('PMOS', '_Met1Layer') + self.getYWidth('ViaPoly_InputAB', '_Met1Layer')) + gapBtwMet1
        elif max(self.NumFinger_PM, self.NumFinger_NM) < self.Num_HorizontalInputViaMode:
            DistanceBtwPMOS2IO1 = 0.5 * self.getYWidth('ViaPoly_InputAB', '_Met1Layer') + (self.getXY('PMOS')[0][1] - self.getXYBot('Met1RouteX_PMDown')[0][1]) + gapBtwMet1
        else:  # finger_max >= self.Num_HorizontalInputViaMode:  same with second case?
            DistanceBtwPMOS2IO1 = 0.5 * self.getYWidth('ViaPoly_InputAB', '_Met1Layer') + (self.getXY('PMOS')[0][1] - self.getXYBot('Met1RouteX_OutputPM2NM_PMside')[0][1]) + gapBtwMet1
        if '_PODummyLayer' in self._DesignParameter['PMOS']['_DesignObj']._DesignParameter:
            DistanceBtwPMOS2IO2 = 0.5 * (self.getYWidth('ViaPoly_InputAB', '_POLayer') + self.getYWidth('PMOS', '_PODummyLayer')) + drc._PolygateMinSpace
        else:
            DistanceBtwPMOS2IO2 = 0
        PMOS2IO_min = max(DistanceBtwPMOS2IO1, DistanceBtwPMOS2IO2)


        print('** minimum Y-distance Calculation ------')
        print(f'VSS2NMOS_min = {VSS2NMOS_min}')
        print(f'VDD2PMOS_min = {VDD2PMOS_min}')
        print(f'NMOS2IO_min = {NMOS2IO_min}')
        print(f'PMOS2IO_min = {PMOS2IO_min}')

        return dict(VSS2NMOS_min=VSS2NMOS_min, VDD2PMOS_min=VDD2PMOS_min, NMOS2IO_min=NMOS2IO_min, PMOS2IO_min=PMOS2IO_min)

    def _CalculateDesignParameter_i(self,
                                    NumFinger_NM=1,
                                    NumFinger_PM=2,
                                    NMOSWidth=200,
                                    PMOSWidth=400,
                                    CellHeight=1800,
                                    YCoordOfNM=300,
                                    YCoordOfPM=1300,
                                    YCoordOfInputOutput=750,
                                    ChannelLength=30,
                                    GateSpacing=100,
                                    XVT='SLVT',
                                    SupplyRailType=1):

        self.NumFinger_NM = NumFinger_NM
        self.NumFinger_PM = NumFinger_PM
        self.NMOSWidth = NMOSWidth
        self.PMOSWidth = PMOSWidth
        self.SupplyRailType = SupplyRailType

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        YWidth_Met1HorizontalRouting = 66

        self._DesignParameter['VSSRail'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VSSRailIn{}'.format(_Name)))[0]
        self._DesignParameter['VDDRail'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VDDRailIn{}'.format(_Name)))[0]
        if SupplyRailType == 1:
            self._DesignParameter['VSSRail']['_DesignObj']._CalculateDesignParameter(
                **dict(NumPitch=((max(NumFinger_NM, NumFinger_PM) * 2) + 1), UnitPitch=(GateSpacing + ChannelLength),
                       Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=True, deleteViaAndMet1=False))
            self._DesignParameter['VDDRail']['_DesignObj']._CalculateDesignParameter(
                **dict(NumPitch=((max(NumFinger_NM, NumFinger_PM) * 2) + 1), UnitPitch=(ChannelLength + GateSpacing),
                       Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=False, deleteViaAndMet1=False))
        elif SupplyRailType == 2:
            self._DesignParameter['VSSRail']['_DesignObj']._CalculateDesignParameter(
                **dict(NumPitch=((max(NumFinger_NM, NumFinger_PM) * 2) + 1), UnitPitch=(GateSpacing + ChannelLength),
                       Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=True, deleteViaAndMet1=True))
            self._DesignParameter['VDDRail']['_DesignObj']._CalculateDesignParameter(
                **dict(NumPitch=((max(NumFinger_NM, NumFinger_PM) * 2) + 1), UnitPitch=(ChannelLength + GateSpacing),
                       Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=False, deleteViaAndMet1=True))
        else:
            raise NotImplementedError
        self._DesignParameter['VSSRail']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['VDDRail']['_XYCoordinates'] = [[0, CellHeight]]

        self._DesignParameter['XVTLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[XVT][0], _Datatype=DesignParameters._LayerMapping[XVT][1],
            _XWidth=self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'],
            _YWidth=CellHeight)
        self._DesignParameter['XVTLayer']['_XYCoordinates'] = [[0, (CellHeight / 2)]]
        self._DesignParameter['NMOS'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['NMOS']['_DesignObj']._CalculateNMOSDesignParameter(
            **dict(_NMOSNumberofGate=(NumFinger_NM * 2), _NMOSChannelWidth=NMOSWidth, _NMOSChannellength=ChannelLength,
                   _NMOSDummy=True, _GateSpacing=GateSpacing, _SDWidth=66, _XVT=XVT))
        self._DesignParameter['NMOS']['_XYCoordinates'] = [[0, YCoordOfNM]]
        self._DesignParameter['PMOS'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['PMOS']['_DesignObj']._CalculatePMOSDesignParameter(
            **dict(_PMOSNumberofGate=(NumFinger_PM * 2), _PMOSChannelWidth=PMOSWidth, _PMOSChannellength=ChannelLength,
                   _PMOSDummy=True, _GateSpacing=GateSpacing, _SDWidth=66, _XVT=XVT))
        self._DesignParameter['PMOS']['_XYCoordinates'] = [[0, YCoordOfPM]]

        # po dummy
        if '_PODummyLayer' in self._DesignParameter['PMOS']['_DesignObj']._DesignParameter:
            Area_PmosDummy = self.getXWidth('PMOS', '_PODummyLayer') * self.getYWidth('PMOS', '_PODummyLayer')
            if Area_PmosDummy < drc._PODummyMinArea:
                YWidth_PmosDummy_Recalc = self.CeilMinSnapSpacing(drc._PODummyMinArea / self.getXWidth('PMOS', '_PODummyLayer'), drc._MinSnapSpacing * 2)
                self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] = YWidth_PmosDummy_Recalc
        if '_PODummyLayer' in self._DesignParameter['NMOS']['_DesignObj']._DesignParameter:
            Area_NmosDummy = self.getXWidth('NMOS', '_PODummyLayer') * self.getYWidth('NMOS', '_PODummyLayer')
            if Area_NmosDummy < drc._PODummyMinArea:
                YWidth_NmosDummy_Recalc = self.CeilMinSnapSpacing(drc._PODummyMinArea / self.getXWidth('NMOS', '_PODummyLayer'), drc._MinSnapSpacing * 2)
                self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] = YWidth_NmosDummy_Recalc

        XYList = []
        xy_offset = (0, (((- self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2) - (((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) / 2)))
        for i in range(
                len(self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
            if (i % 2) == 0:
                XYList.append([((x + y) + z) for (x, y, z) in
                               zip([(0 + self._DesignParameter['NMOS']['_XYCoordinates'][0][0]),
                                    (0 + self._DesignParameter['NMOS']['_XYCoordinates'][0][1])],
                                   self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i], xy_offset)])
        self._DesignParameter['Met1RouteY_VSS2NM'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)))
        self._DesignParameter['Met1RouteY_VSS2NM']['_XYCoordinates'] = XYList

        XYList = []
        xy_offset = (0, ((self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2) + (
                    (drc._Metal1MinSpaceAtCorner + YWidth_Met1HorizontalRouting) / 2)))
        for i in range(
                len(self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
            if (i % 2) == 1:
                XYList.append([((x + y) + z) for (x, y, z) in
                               zip([(0 + self._DesignParameter['NMOS']['_XYCoordinates'][0][0]),
                                    (0 + self._DesignParameter['NMOS']['_XYCoordinates'][0][1])],
                                   self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i], xy_offset)])
        self._DesignParameter['Met1RouteY_NMout'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
            _YWidth=(drc._Metal1MinSpaceAtCorner + YWidth_Met1HorizontalRouting))
        self._DesignParameter['Met1RouteY_NMout']['_XYCoordinates'] = XYList
        self._DesignParameter['Met1RouteX_NMout'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=((self._DesignParameter['Met1RouteY_NMout']['_XYCoordinates'][(- 1)][0] + (self._DesignParameter['Met1RouteY_NMout']['_XWidth'] / 2)) - (self._DesignParameter['Met1RouteY_NMout']['_XYCoordinates'][0][0] - (self._DesignParameter['Met1RouteY_NMout']['_XWidth'] / 2))),
            _YWidth=YWidth_Met1HorizontalRouting)
        self._DesignParameter['Met1RouteX_NMout']['_XYCoordinates'] = [[(((self._DesignParameter['Met1RouteY_NMout']['_XYCoordinates'][(- 1)][0] + (self._DesignParameter['Met1RouteY_NMout']['_XWidth'] / 2)) + (self._DesignParameter['Met1RouteY_NMout']['_XYCoordinates'][0][0] - (self._DesignParameter['Met1RouteY_NMout']['_XWidth'] / 2))) / 2),
                                                                        ((self._DesignParameter['Met1RouteY_NMout']['_XYCoordinates'][0][1] + (self._DesignParameter['Met1RouteY_NMout']['_YWidth'] / 2)) - (self._DesignParameter['Met1RouteX_NMout']['_YWidth'] / 2))]]

        ''' Optional '''
        if SupplyRailType == 2:
            XYList = []
            xy_offset = (0, ((- self._DesignParameter['Met1RouteY_VSS2NM']['_YWidth']) / 2))
            for i in range(len(self._DesignParameter['Met1RouteY_VSS2NM']['_XYCoordinates'])):
                xy = (self._DesignParameter['Met1RouteY_VSS2NM']['_XYCoordinates'][i][0] if (type(self._DesignParameter['Met1RouteY_VSS2NM']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['Met1RouteY_VSS2NM']['_XYCoordinates'][i])
                XYList.append([((x + y) + z) for (x, y, z) in zip([0, 0], xy, xy_offset)])
            self._DesignParameter['VSSVia'] = self._SrefElementDeclaration(_DesignObj=Z_PWR_CNT.Z_PWR_CNT(_Name='VSSViaIn{}'.format(_Name)))[0]
            self._DesignParameter['VSSVia']['_DesignObj']._CalculateDesignParameter(**dict(_Xnum=1, _Xdistance=0))
            self._DesignParameter['VSSVia']['_XYCoordinates'] = XYList
        else:
            pass



        ''' CLI Gen. '''
        # Met1Routing
        self._DesignParameter['Met1RouteY_PMOut'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
            _YWidth=(drc._Metal1MinSpaceAtCorner + YWidth_Met1HorizontalRouting)
        )
        self._DesignParameter['Met1RouteY_PMUp'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
            _YWidth=(drc._Metal1MinSpaceAtCorner + YWidth_Met1HorizontalRouting)
        )

        tmpXYs_PMout = []
        tmpXYs_PMintermediate = []
        for i in range(0, NumFinger_PM + 1):
            if i % 2 == 1:
                tmpXYs_PMout.append(
                    CoordCalc.Sum(self.getXY('PMOS', '_Met1Layer')[NumFinger_PM + i],
                                  [0, -self.getYWidth('PMOS', '_Met1Layer')/2],
                                  [0, -self.getYWidth('Met1RouteY_PMOut')/2])
                )
            else:
                tmpXYs_PMintermediate.append(
                    CoordCalc.Sum(self.getXY('PMOS', '_Met1Layer')[NumFinger_PM + i],
                                  [0, +self.getYWidth('PMOS', '_Met1Layer')/2],
                                  [0, +self.getYWidth('Met1RouteY_PMUp')/2])
                )
        self._DesignParameter['Met1RouteY_PMOut']['_XYCoordinates'] = tmpXYs_PMout
        self._DesignParameter['Met1RouteY_PMUp']['_XYCoordinates'] = tmpXYs_PMintermediate

        self._DesignParameter['Met1RouteX_PMOut'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=CoordCalc.getXYCoords_MaxX(self.getXY('Met1RouteY_PMOut'))[0][0] - CoordCalc.getXYCoords_MinX(self.getXY('Met1RouteY_PMOut'))[0][0] + self.getXWidth('Met1RouteY_PMOut'),
            _YWidth=YWidth_Met1HorizontalRouting
        )
        self._DesignParameter['Met1RouteX_PMOut']['_XYCoordinates'] = [[
            (self.getXY('Met1RouteY_PMOut')[0][0] + self.getXY('Met1RouteY_PMOut')[-1][0]) / 2,
            self.getXY('Met1RouteY_PMOut')[0][1] - self.getYWidth('Met1RouteY_PMOut') / 2 + self.getYWidth('Met1RouteX_PMOut') / 2
        ]]

        self._DesignParameter['Met1RouteX_PMUp'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=CoordCalc.getXYCoords_MaxX(self.getXY('Met1RouteY_PMUp'))[0][0] - CoordCalc.getXYCoords_MinX(self.getXY('Met1RouteY_PMUp'))[0][0] + self.getXWidth('Met1RouteY_PMUp'),
            _YWidth=YWidth_Met1HorizontalRouting
        )
        self._DesignParameter['Met1RouteX_PMUp']['_XYCoordinates'] = [[
            (self.getXY('Met1RouteY_PMUp')[0][0] + self.getXY('Met1RouteY_PMUp')[-1][0]) / 2,
            self.getXY('Met1RouteY_PMUp')[0][1] + self.getYWidth('Met1RouteY_PMUp')/2 - self.getYWidth('Met1RouteX_PMUp')/2
        ]]

        #
        self._DesignParameter['Met1RouteY_PMDown'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
            _YWidth=(drc._Metal1MinSpaceAtCorner + YWidth_Met1HorizontalRouting)
        )
        self._DesignParameter['Met1RouteY_PM2VDD'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
            _YWidth=CellHeight - (self.getXY('PMOS', '_Met1Layer')[0][1] + self.getYWidth('PMOS', '_Met1Layer')/2)
        )
        tmpXYs_PMDown = []
        tmpXYs_PM2VDD = []
        for i in range(0, NumFinger_PM + 1):
            if i % 2 == 0:
                tmpXYs_PMDown.append(
                    CoordCalc.Sum(self.getXY('PMOS', '_Met1Layer')[NumFinger_PM - i],
                                  [0, -self.getYWidth('PMOS', '_Met1Layer') / 2],
                                  [0, -self.getYWidth('Met1RouteY_PMDown') / 2])
                )
            else:
                tmpXYs_PM2VDD.append(
                    CoordCalc.Sum(self.getXY('PMOS', '_Met1Layer')[NumFinger_PM - i],
                                  [0, +self.getYWidth('PMOS', '_Met1Layer') / 2],
                                  [0, +self.getYWidth('Met1RouteY_PM2VDD') / 2])
                )
        self._DesignParameter['Met1RouteY_PMDown']['_XYCoordinates'] = tmpXYs_PMDown
        self._DesignParameter['Met1RouteY_PM2VDD']['_XYCoordinates'] = tmpXYs_PM2VDD

        self._DesignParameter['Met1RouteX_PMDown'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=CoordCalc.getXYCoords_MaxX(self.getXY('Met1RouteY_PMDown'))[0][0] - CoordCalc.getXYCoords_MinX(self.getXY('Met1RouteY_PMDown'))[0][0] + self.getXWidth('Met1RouteY_PMDown'),
            _YWidth=YWidth_Met1HorizontalRouting
        )
        self._DesignParameter['Met1RouteX_PMDown']['_XYCoordinates'] = [[
            (self.getXY('Met1RouteY_PMDown')[0][0] + self.getXY('Met1RouteY_PMDown')[-1][0]) / 2,
            self.getXY('Met1RouteY_PMDown')[0][1] - self.getYWidth('Met1RouteY_PMDown') / 2 + self.getYWidth('Met1RouteX_PMDown') / 2
        ]]

        ''' Optional '''
        if SupplyRailType == 2:
            tmpXYs = []
            for XYs in self.getXY('Met1RouteY_PM2VDD'):
                tmpXYs.append(CoordCalc.Sum(XYs, [0, +self.getYWidth('Met1RouteY_PM2VDD') / 2]))
            self._DesignParameter['ViaForVDD'] = self._SrefElementDeclaration(_DesignObj=Z_PWR_CNT.Z_PWR_CNT(_Name='ViaForVDDIn{}'.format(_Name)))[0]
            self._DesignParameter['ViaForVDD']['_DesignObj']._CalculateDesignParameter(**dict(_Xnum=1, _Xdistance=0))
            self._DesignParameter['ViaForVDD']['_XYCoordinates'] = tmpXYs
        else:
            pass

        # Nwell Layer
        YCoord_NwellTopBoundary = self.getXY('VDDRail', '_ODLayer')[0][1] + self.getYWidth('VDDRail', '_ODLayer') / 2 + drc._NwMinEnclosurePactive
        YCoord_NwellBotBoundary = self.getXY('PMOS', '_ODLayer')[0][1] - (self.getYWidth('PMOS', '_ODLayer') / 2 + drc._NwMinEnclosurePactive)
        XWidth1_NWELL = self.getXWidth('PMOS', '_ODLayer') + 2 * drc._NwMinEnclosurePactive2
        XWidth2_NWELL = self.getXWidth('VDDRail', '_ODLayer') + 2 * drc._NwMinEnclosurePactive
        self._DesignParameter['NwellLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=max(XWidth1_NWELL, XWidth2_NWELL),
            _YWidth=YCoord_NwellTopBoundary - YCoord_NwellBotBoundary,
            _XYCoordinates=[[0, (YCoord_NwellTopBoundary + YCoord_NwellBotBoundary)/2]]
        )


        ''' Input Via Out Output Met1 '''

        if max(NumFinger_NM, NumFinger_PM) < self.Num_HorizontalInputViaMode:
            self._DesignParameter['Met1RouteY_OutputPM2NM'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=self.getXWidth('Met1RouteY_PMOut'),
                _YWidth=(self.getXY('Met1RouteX_PMOut')[0][1] + self.getYWidth('Met1RouteX_PMOut') / 2) - (self.getXY('Met1RouteX_NMout')[0][1] - self.getYWidth('Met1RouteX_NMout') / 2)
            )

            self._DesignParameter['ViaPoly_InputAB'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='ViaPoly_InputABIn{}'.format(_Name)))[0]
            self._DesignParameter['ViaPoly_InputAB']['_DesignObj']._CalculateDesignParameter(
                **dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2,
                       Met1XWidth=66, Met1YWidth=200, POXWidth=50, POYWidth=200))


            if max(NumFinger_NM, NumFinger_PM) == 1:                    # (P,N) = (1,1)
                XCoord_OutputMet1Y = 0
                XCoord_InputA = self.getXY('PMOS', '_Met1Layer')[0][0]
                XCoord_InputB = self.getXY('PMOS', '_Met1Layer')[-1][0]
            elif NumFinger_PM == 1:                                     # (P,N) = (1,2), (1,3), ...  rare condition
                XCoord_OutputMet1Y = 0
                XCoord_InputA = - max(NumFinger_NM, NumFinger_PM) / 2 * (GateSpacing + ChannelLength)
                XCoord_InputB = + max(NumFinger_NM, NumFinger_PM) / 2 * (GateSpacing + ChannelLength)
            elif max(NumFinger_NM, NumFinger_PM) == 2:                  # (P,N) = (2,1), (2,2)
                XCoord_OutputMet1Y = self.getXY('PMOS', '_Met1Layer')[-1][0]
                XCoord_InputA = - max(NumFinger_NM, NumFinger_PM) / 2 * (GateSpacing + ChannelLength)
                XCoord_InputB = + max(NumFinger_NM, NumFinger_PM) / 2 * (GateSpacing + ChannelLength)
            else:
                XCoord_InputA = - max(NumFinger_NM, NumFinger_PM) / 2 * (GateSpacing + ChannelLength)
                XCoord_InputB = + max(NumFinger_NM, NumFinger_PM) // 2 * (GateSpacing + ChannelLength)
                XCoord_OutputMet1Y = XCoord_InputB + (GateSpacing + ChannelLength)


            self._DesignParameter['Met1RouteY_OutputPM2NM']['_XYCoordinates'] = [[
                XCoord_OutputMet1Y,
                ((self.getXY('Met1RouteX_PMOut')[0][1] + self.getYWidth('Met1RouteX_PMOut') / 2) + (self.getXY('Met1RouteX_NMout')[0][1] - self.getYWidth('Met1RouteX_NMout') / 2)) / 2
            ]]
            self._DesignParameter['ViaPoly_InputAB']['_XYCoordinates'] = [
                [XCoord_InputA, YCoordOfInputOutput],
                [XCoord_InputB, YCoordOfInputOutput]
            ]



            RightBoundary_Met1X_OutputPM2NM_PMside = max(
                self.getXY('Met1RouteY_OutputPM2NM')[0][0] + self.getXWidth('Met1RouteY_OutputPM2NM') / 2,
                self.getXY('Met1RouteX_PMOut')[0][0] + self.getXWidth('Met1RouteX_PMOut') / 2
            )
            LeftBoundary_Met1X_OutputPM2NM_PMside = min(
                self.getXY('Met1RouteY_OutputPM2NM')[0][0] - self.getXWidth('Met1RouteY_OutputPM2NM') / 2,
                self.getXY('Met1RouteX_PMOut')[0][0] + self.getXWidth('Met1RouteX_PMOut') / 2
            )
            self._DesignParameter['Met1RouteX_OutputPM2NM_PMside'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=RightBoundary_Met1X_OutputPM2NM_PMside - LeftBoundary_Met1X_OutputPM2NM_PMside,
                _YWidth=YWidth_Met1HorizontalRouting
            )
            self._DesignParameter['Met1RouteX_OutputPM2NM_PMside']['_XYCoordinates'] = [[
                (RightBoundary_Met1X_OutputPM2NM_PMside + LeftBoundary_Met1X_OutputPM2NM_PMside) / 2,
                self.getXY('Met1RouteX_PMOut')[0][1]
            ]]

            self._DesignParameter['Met1RouteX_OutputPM2NM_NMside'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=(self.getXY('Met1RouteY_OutputPM2NM')[0][0] + self.getXWidth('Met1RouteY_OutputPM2NM') / 2) - (self.getXY('Met1RouteY_NMout')[0][0] - self.getXWidth('Met1RouteY_NMout') / 2),
                _YWidth=YWidth_Met1HorizontalRouting
            )
            self._DesignParameter['Met1RouteX_OutputPM2NM_NMside']['_XYCoordinates'] = [[
                ((self.getXY('Met1RouteY_OutputPM2NM')[0][0] + self.getXWidth('Met1RouteY_OutputPM2NM') / 2) + (self.getXY('Met1RouteY_NMout')[0][0] - self.getXWidth('Met1RouteY_NMout') / 2)) / 2,
                self.getXY('Met1RouteY_OutputPM2NM')[0][1] - self.getYWidth('Met1RouteY_OutputPM2NM') / 2 + self.getYWidth('Met1RouteX_OutputPM2NM_NMside') / 2
            ]]






            ''' PolyRouting For Input Gate '''
            self._DesignParameter['PolyRouteY_PMB'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=ChannelLength,
                _YWidth=(self.getXY('PMOS', '_POLayer')[0][1] - self.getYWidth('PMOS', '_POLayer') / 2) - (self.getXY('ViaPoly_InputAB', '_POLayer')[0][1] + self.getYWidth('ViaPoly_InputAB', '_POLayer') / 2)
            )
            tmpXYs = []
            for i, XYs in enumerate(self.getXY('PMOS', '_POLayer')):
                if i >= NumFinger_PM:
                    tmpXYs.append([
                        XYs[0],
                        ((self.getXY('PMOS', '_POLayer')[0][1] - self.getYWidth('PMOS', '_POLayer') / 2) + (self.getXY('ViaPoly_InputAB', '_POLayer')[0][1] + self.getYWidth('ViaPoly_InputAB', '_POLayer') / 2)) / 2
                    ])
            self._DesignParameter['PolyRouteY_PMB']['_XYCoordinates'] = tmpXYs

            self._DesignParameter['PolyRouteY_NMB'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=ChannelLength,
                _YWidth=(self.getXY('ViaPoly_InputAB', '_POLayer')[0][1] - self.getYWidth('ViaPoly_InputAB', '_POLayer') / 2) - (self.getXY('NMOS', '_POLayer')[0][1] + self.getYWidth('NMOS', '_POLayer') / 2)
            )
            tmpXYs = []
            for i, XYs in enumerate(self.getXY('NMOS', '_POLayer')):
                if i >= NumFinger_NM:
                    tmpXYs.append([
                        XYs[0],
                        ((self.getXY('ViaPoly_InputAB', '_POLayer')[0][1] - self.getYWidth('ViaPoly_InputAB', '_POLayer') / 2) + (self.getXY('NMOS', '_POLayer')[0][1] + self.getYWidth('NMOS', '_POLayer') / 2)) / 2
                    ])
            self._DesignParameter['PolyRouteY_NMB']['_XYCoordinates'] = tmpXYs


            RightBoundary_PMPolyB = max(
                self.getXY('ViaPoly_InputAB', '_POLayer')[1][0] + self.getXWidth('ViaPoly_InputAB', '_POLayer') / 2,
                self.getXY('PMOS', '_POLayer')[-1][0] + self.getXWidth('PMOS', '_POLayer') / 2)
            LeftBoundary_PMPolyB = min(
                self.getXY('ViaPoly_InputAB', '_POLayer')[1][0] - self.getXWidth('ViaPoly_InputAB', '_POLayer') / 2,
                self.getXY('PMOS', '_POLayer')[NumFinger_PM][0] - self.getXWidth('PMOS', '_POLayer') / 2)
            self._DesignParameter['PolyRouteX_PM_InputB'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=RightBoundary_PMPolyB - LeftBoundary_PMPolyB,
                _YWidth=50
            )
            self._DesignParameter['PolyRouteX_PM_InputB']['_XYCoordinates'] = [[
                (RightBoundary_PMPolyB + LeftBoundary_PMPolyB) / 2,
                self.getXY('PolyRouteY_PMB')[0][1] - self.getYWidth('PolyRouteY_PMB') / 2 - self.getYWidth('PolyRouteX_PM_InputB') / 2
            ]]
            RightBoundary_NMPolyB = max(
                self.getXY('ViaPoly_InputAB', '_POLayer')[1][0] + self.getXWidth('ViaPoly_InputAB', '_POLayer') / 2,
                self.getXY('NMOS', '_POLayer')[-1][0] + self.getXWidth('NMOS', '_POLayer') / 2)
            LeftBoundary_NMPolyB = min(
                self.getXY('ViaPoly_InputAB', '_POLayer')[1][0] - self.getXWidth('ViaPoly_InputAB', '_POLayer') / 2,
                self.getXY('NMOS', '_POLayer')[NumFinger_NM][0] - self.getXWidth('NMOS', '_POLayer') / 2)
            self._DesignParameter['PolyRouteX_NM_InputB'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=RightBoundary_NMPolyB - LeftBoundary_NMPolyB,
                _YWidth=self.getYWidth('PolyRouteX_PM_InputB')
            )
            self._DesignParameter['PolyRouteX_NM_InputB']['_XYCoordinates'] = [[
                (RightBoundary_NMPolyB + LeftBoundary_NMPolyB) / 2,
                self.getXY('PolyRouteY_NMB')[0][1] + self.getYWidth('PolyRouteY_NMB') / 2 + self.getYWidth('PolyRouteX_NM_InputB') / 2
            ]]




            RightBoundary_PMPolyA = max(self.getXY('ViaPoly_InputAB', '_POLayer')[0][0] + self.getXWidth('ViaPoly_InputAB', '_POLayer') / 2,
                                        self.getXY('PMOS', '_POLayer')[NumFinger_PM-1][0] + self.getXWidth('PMOS', '_POLayer') / 2)
            LeftBoundary_PMPolyA = min(self.getXY('ViaPoly_InputAB', '_POLayer')[0][0] - self.getXWidth('ViaPoly_InputAB', '_POLayer') / 2,
                                       self.getXY('PMOS', '_POLayer')[0][0] - self.getXWidth('PMOS', '_POLayer') / 2)
            self._DesignParameter['PolyRouteX_PM_InputA'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=RightBoundary_PMPolyA - LeftBoundary_PMPolyA,
                _YWidth=self.getYWidth('PolyRouteX_PM_InputB')
            )
            self._DesignParameter['PolyRouteX_PM_InputA']['_XYCoordinates'] = [[
                (RightBoundary_PMPolyA + LeftBoundary_PMPolyA) / 2,
                self.getXY('ViaPoly_InputAB', '_POLayer')[0][1] + self.getYWidth('ViaPoly_InputAB', '_POLayer') / 2 - self.getYWidth('PolyRouteX_PM_InputA') / 2
                # 1100
            ]]

            RightBoundary_NMPolyA = max(
                self.getXY('ViaPoly_InputAB', '_POLayer')[0][0] + self.getXWidth('ViaPoly_InputAB', '_POLayer') / 2,
                self.getXY('NMOS', '_POLayer')[NumFinger_NM - 1][0] + self.getXWidth('NMOS', '_POLayer') / 2)
            LeftBoundary_NMPolyA = min(
                self.getXY('ViaPoly_InputAB', '_POLayer')[0][0] - self.getXWidth('ViaPoly_InputAB', '_POLayer') / 2,
                self.getXY('NMOS', '_POLayer')[0][0] - self.getXWidth('NMOS', '_POLayer') / 2)
            self._DesignParameter['PolyRouteX_NM_InputA'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=RightBoundary_NMPolyA - LeftBoundary_NMPolyA,
                _YWidth=self.getYWidth('PolyRouteX_PM_InputB')
            )
            self._DesignParameter['PolyRouteX_NM_InputA']['_XYCoordinates'] = [[
                (RightBoundary_NMPolyA + LeftBoundary_NMPolyA) / 2,
                self.getXY('ViaPoly_InputAB', '_POLayer')[0][1] - self.getYWidth('ViaPoly_InputAB', '_POLayer') / 2 + self.getYWidth('PolyRouteX_NM_InputA') / 2
                # 700
            ]]


            self._DesignParameter['PolyRouteY_PMA'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=ChannelLength,
                _YWidth=((self.getXY('PMOS', '_POLayer')[0][1] - self.getYWidth('PMOS', '_POLayer') / 2) - (self.getXY('PolyRouteX_PM_InputA')[0][1] + self.getYWidth('PolyRouteX_PM_InputA') / 2))
            )
            tmpXYs = []
            for i, XYs in enumerate(self.getXY('PMOS', '_POLayer')):
                if i < NumFinger_PM:
                    tmpXYs.append([
                        XYs[0],
                        ((self.getXY('PMOS', '_POLayer')[0][1] - self.getYWidth('PMOS', '_POLayer') / 2) + (self.getXY('PolyRouteX_PM_InputA')[0][1] + self.getYWidth('PolyRouteX_PM_InputA') / 2)) / 2
                    ])
            self._DesignParameter['PolyRouteY_PMA']['_XYCoordinates'] = tmpXYs

            self._DesignParameter['PolyRouteY_NMA'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=ChannelLength,
                _YWidth=((self.getXY('PolyRouteX_NM_InputA')[0][1] - self.getYWidth('PolyRouteX_NM_InputA') / 2) - (self.getXY('NMOS', '_POLayer')[0][1] + self.getYWidth('NMOS', '_POLayer') / 2))
            )
            tmpXYs = []
            for i, XYs in enumerate(self.getXY('NMOS', '_POLayer')):
                if i < NumFinger_NM:
                    tmpXYs.append([
                        XYs[0],
                        ((self.getXY('PolyRouteX_NM_InputA')[0][1] - self.getYWidth('PolyRouteX_NM_InputA') / 2) + (self.getXY('NMOS', '_POLayer')[0][1] + self.getYWidth('NMOS', '_POLayer') / 2)) / 2
                    ])
            self._DesignParameter['PolyRouteY_NMA']['_XYCoordinates'] = tmpXYs

            self._DesignParameter['PolyRouteY_PMNMA'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=self.getXWidth('ViaPoly_InputAB', '_POLayer'),
                _YWidth=((self.getXY('PolyRouteX_PM_InputA')[0][1] - self.getYWidth('PolyRouteX_PM_InputA') / 2) - (self.getXY('PolyRouteX_NM_InputA')[0][1] + self.getYWidth('PolyRouteX_NM_InputA') / 2)),
                _XYCoordinates=[[
                    self.getXY('ViaPoly_InputAB')[0][0],
                    ((self.getXY('PolyRouteX_PM_InputA')[0][1] - self.getYWidth('PolyRouteX_PM_InputA') / 2) + (self.getXY('PolyRouteX_NM_InputA')[0][1] + self.getYWidth('PolyRouteX_NM_InputA') / 2)) / 2
                ]]
            )

        else:       #  if not max(NumFinger_NM, NumFinger_PM) < self.Num_HorizontalInputViaMode:
            topBoundary_Met1YOutputPM2NM = self.getXY('Met1RouteX_PMOut')[0][1] - self.getYWidth('Met1RouteX_PMOut') / 2 - drc._Metal1MinSpaceAtCorner
            botBoundary_Met1YOutputPM2NM = self.getXY('Met1RouteX_NMout')[0][1] - self.getYWidth('Met1RouteX_NMout') / 2

            self._DesignParameter['Met1RouteY_OutputPM2NM'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=self.getXWidth('Met1RouteY_PMOut'),
                _YWidth=topBoundary_Met1YOutputPM2NM - botBoundary_Met1YOutputPM2NM
            )
            self._DesignParameter['Met1RouteY_OutputPM2NM']['_XYCoordinates'] = [[
                0, (topBoundary_Met1YOutputPM2NM + botBoundary_Met1YOutputPM2NM) / 2
            ]]

            rightBoundary_Met1XOutputPMside = self.getXY('Met1RouteY_PMOut')[0][0] + self.getXWidth('Met1RouteY_PMOut') / 2
            leftBoundary_Met1XOutputPMside = self.getXY('Met1RouteY_OutputPM2NM')[0][0] - self.getXWidth('Met1RouteY_OutputPM2NM') / 2
            self._DesignParameter['Met1RouteX_OutputPM2NM_PMside'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=rightBoundary_Met1XOutputPMside - leftBoundary_Met1XOutputPMside,
                _YWidth=self.getXWidth('Met1RouteY_PMOut')
            )
            self._DesignParameter['Met1RouteX_OutputPM2NM_PMside']['_XYCoordinates'] = [[
                (rightBoundary_Met1XOutputPMside + leftBoundary_Met1XOutputPMside) / 2,
                self.getXY('Met1RouteY_OutputPM2NM')[0][1] + self.getYWidth('Met1RouteY_OutputPM2NM') / 2 - self.getYWidth('Met1RouteX_OutputPM2NM_PMside') / 2
            ]]

            botBoundary_Met1YOutputPMside = self.getXY('Met1RouteX_OutputPM2NM_PMside')[0][1] - self.getYWidth('Met1RouteX_OutputPM2NM_PMside') / 2
            topBoundary_Met1YOutputPMside = self.getXY('Met1RouteX_PMOut')[0][1] + self.getYWidth('Met1RouteX_PMOut') / 2

            self._DesignParameter['Met1RouteY_OutputPM2NM_PMside'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=self.getXWidth('Met1RouteY_PMOut'),
                _YWidth=topBoundary_Met1YOutputPMside - botBoundary_Met1YOutputPMside
            )
            self._DesignParameter['Met1RouteY_OutputPM2NM_PMside']['_XYCoordinates'] = [[
                self.getXY('Met1RouteX_OutputPM2NM_PMside')[0][0] + self.getXWidth('Met1RouteX_OutputPM2NM_PMside') / 2 - self.getXWidth('Met1RouteY_OutputPM2NM_PMside') / 2,
                (topBoundary_Met1YOutputPMside + botBoundary_Met1YOutputPMside) / 2
            ]]

            # boundary: Contact edge
            rightBoundary_InputPolyGate1_byPM = self.getXY('PMOS', '_POLayer')[-1][0] + self.getXWidth('PMOS', '_POLayer') / 2 - drc._CoMinEnclosureByPOAtLeastTwoSide
            rightBoundary_InputPolyGate2_byNM = self.getXY('NMOS', '_POLayer')[-1][0] + self.getXWidth('NMOS', '_POLayer') / 2 - drc._CoMinEnclosureByPOAtLeastTwoSide
            rightBoundary_InputPolyGate = max(rightBoundary_InputPolyGate1_byPM, rightBoundary_InputPolyGate2_byNM)
            leftBoundary_InputMet1 = self.getXY('Met1RouteY_OutputPM2NM')[0][0] + self.getXWidth('Met1RouteY_OutputPM2NM') / 2 + drc._Metal1MinSpaceAtCorner
            leftBoundary_InputPolyGate = leftBoundary_InputMet1 + drc._Metal1MinEnclosureCO2
            xNumViaInputGate = int((rightBoundary_InputPolyGate - leftBoundary_InputPolyGate - drc._CoMinWidth) // (drc._CoMinWidth + drc._CoMinSpace)) + 1
            print('xNumViaInputGate:', xNumViaInputGate)
            self._DesignParameter['ViaPoly_InputAB'] = self._SrefElementDeclaration(
                _DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='ViaPoly_InputABIn{}'.format(_Name)))[0]
            self._DesignParameter['ViaPoly_InputAB']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
                **dict(_ViaPoly2Met1NumberOfCOX=xNumViaInputGate, _ViaPoly2Met1NumberOfCOY=1))
            self._DesignParameter['ViaPoly_InputAB']['_XYCoordinates'] = [
                [-(rightBoundary_InputPolyGate + leftBoundary_InputPolyGate) / 2, YCoordOfInputOutput],
                [+(rightBoundary_InputPolyGate + leftBoundary_InputPolyGate) / 2, YCoordOfInputOutput]
            ]

            self._DesignParameter['PolyRouteY_PMB'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=ChannelLength,
                _YWidth=(self.getXY('PMOS', '_POLayer')[0][1] - self.getYWidth('PMOS', '_POLayer') / 2) - (self.getXY('ViaPoly_InputAB', '_POLayer')[0][1] + self.getYWidth('ViaPoly_InputAB', '_POLayer') / 2)
            )
            tmpXYs = []
            for i, XYs in enumerate(self.getXY('PMOS', '_POLayer')):
                if i >= NumFinger_PM:
                    tmpXYs.append([
                        XYs[0],
                        ((self.getXY('PMOS', '_POLayer')[0][1] - self.getYWidth('PMOS', '_POLayer') / 2) + (self.getXY('ViaPoly_InputAB', '_POLayer')[0][1] + self.getYWidth('ViaPoly_InputAB', '_POLayer') / 2)) / 2
                    ])
            self._DesignParameter['PolyRouteY_PMB']['_XYCoordinates'] = tmpXYs

            self._DesignParameter['PolyRouteY_NMB'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=ChannelLength,
                _YWidth=(self.getXY('ViaPoly_InputAB', '_POLayer')[0][1] - self.getYWidth('ViaPoly_InputAB', '_POLayer') / 2) - (self.getXY('NMOS', '_POLayer')[0][1] + self.getYWidth('NMOS', '_POLayer') / 2)
            )
            tmpXYs = []
            for i, XYs in enumerate(self.getXY('NMOS', '_POLayer')):
                if i >= NumFinger_NM:
                    tmpXYs.append([
                        XYs[0],
                        ((self.getXY('ViaPoly_InputAB', '_POLayer')[0][1] - self.getYWidth('ViaPoly_InputAB', '_POLayer') / 2) + (self.getXY('NMOS', '_POLayer')[0][1] + self.getYWidth('NMOS', '_POLayer') / 2)) / 2
                    ])
            self._DesignParameter['PolyRouteY_NMB']['_XYCoordinates'] = tmpXYs

            RightBoundary_PMPolyB = max(
                self.getXY('ViaPoly_InputAB', '_POLayer')[1][0] + self.getXWidth('ViaPoly_InputAB', '_POLayer') / 2,
                self.getXY('PMOS', '_POLayer')[-1][0] + self.getXWidth('PMOS', '_POLayer') / 2)
            LeftBoundary_PMPolyB = min(
                self.getXY('ViaPoly_InputAB', '_POLayer')[1][0] - self.getXWidth('ViaPoly_InputAB', '_POLayer') / 2,
                self.getXY('PMOS', '_POLayer')[NumFinger_PM][0] - self.getXWidth('PMOS', '_POLayer') / 2)
            self._DesignParameter['PolyRouteX_PM_InputB'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=RightBoundary_PMPolyB - LeftBoundary_PMPolyB,
                _YWidth=self.getYWidth('ViaPoly_InputAB', '_POLayer')
            )
            self._DesignParameter['PolyRouteX_PM_InputB']['_XYCoordinates'] = [[
                (RightBoundary_PMPolyB + LeftBoundary_PMPolyB) / 2,
                self.getXY('PolyRouteY_PMB')[0][1] - self.getYWidth('PolyRouteY_PMB') / 2 - self.getYWidth('PolyRouteX_PM_InputB') / 2
            ]]
            RightBoundary_NMPolyB = max(
                self.getXY('ViaPoly_InputAB', '_POLayer')[1][0] + self.getXWidth('ViaPoly_InputAB', '_POLayer') / 2,
                self.getXY('NMOS', '_POLayer')[-1][0] + self.getXWidth('NMOS', '_POLayer') / 2)
            LeftBoundary_NMPolyB = min(
                self.getXY('ViaPoly_InputAB', '_POLayer')[1][0] - self.getXWidth('ViaPoly_InputAB', '_POLayer') / 2,
                self.getXY('NMOS', '_POLayer')[NumFinger_NM][0] - self.getXWidth('NMOS', '_POLayer') / 2)
            self._DesignParameter['PolyRouteX_NM_InputB'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=RightBoundary_NMPolyB - LeftBoundary_NMPolyB,
                _YWidth=self.getYWidth('PolyRouteX_PM_InputB')
            )
            self._DesignParameter['PolyRouteX_NM_InputB']['_XYCoordinates'] = [[
                (RightBoundary_NMPolyB + LeftBoundary_NMPolyB) / 2,
                self.getXY('PolyRouteY_NMB')[0][1] + self.getYWidth('PolyRouteY_NMB') / 2 + self.getYWidth('PolyRouteX_NM_InputB') / 2
            ]]

            RightBoundary_PMPolyA = max(
                self.getXY('ViaPoly_InputAB', '_POLayer')[0][0] + self.getXWidth('ViaPoly_InputAB', '_POLayer') / 2,
                self.getXY('PMOS', '_POLayer')[NumFinger_PM - 1][0] + self.getXWidth('PMOS', '_POLayer') / 2)
            LeftBoundary_PMPolyA = min(
                self.getXY('ViaPoly_InputAB', '_POLayer')[0][0] - self.getXWidth('ViaPoly_InputAB', '_POLayer') / 2,
                self.getXY('PMOS', '_POLayer')[0][0] - self.getXWidth('PMOS', '_POLayer') / 2)
            self._DesignParameter['PolyRouteX_PM_InputA'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=RightBoundary_PMPolyA - LeftBoundary_PMPolyA,
                _YWidth=self.getYWidth('PolyRouteX_PM_InputB')
            )
            self._DesignParameter['PolyRouteX_PM_InputA']['_XYCoordinates'] = [[
                (RightBoundary_PMPolyA + LeftBoundary_PMPolyA) / 2,
                self.getXY('ViaPoly_InputAB', '_POLayer')[0][1] + self.getYWidth('ViaPoly_InputAB', '_POLayer') / 2 - self.getYWidth('PolyRouteX_PM_InputA') / 2
            ]]

            RightBoundary_NMPolyA = max(
                self.getXY('ViaPoly_InputAB', '_POLayer')[0][0] + self.getXWidth('ViaPoly_InputAB', '_POLayer') / 2,
                self.getXY('NMOS', '_POLayer')[NumFinger_NM - 1][0] + self.getXWidth('NMOS', '_POLayer') / 2)
            LeftBoundary_NMPolyA = min(
                self.getXY('ViaPoly_InputAB', '_POLayer')[0][0] - self.getXWidth('ViaPoly_InputAB', '_POLayer') / 2,
                self.getXY('NMOS', '_POLayer')[0][0] - self.getXWidth('NMOS', '_POLayer') / 2)
            self._DesignParameter['PolyRouteX_NM_InputA'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=RightBoundary_NMPolyA - LeftBoundary_NMPolyA,
                _YWidth=self.getYWidth('PolyRouteX_PM_InputB')
            )
            self._DesignParameter['PolyRouteX_NM_InputA']['_XYCoordinates'] = [[
                (RightBoundary_NMPolyA + LeftBoundary_NMPolyA) / 2,
                self.getXY('ViaPoly_InputAB', '_POLayer')[0][1] - self.getYWidth('ViaPoly_InputAB', '_POLayer') / 2 + self.getYWidth('PolyRouteX_NM_InputA') / 2
            ]]

            self._DesignParameter['PolyRouteY_PMA'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=ChannelLength,
                _YWidth=((self.getXY('PMOS', '_POLayer')[0][1] - self.getYWidth('PMOS', '_POLayer') / 2) - (self.getXY('PolyRouteX_PM_InputA')[0][1] + self.getYWidth('PolyRouteX_PM_InputA') / 2))
            )
            tmpXYs = []
            for i, XYs in enumerate(self.getXY('PMOS', '_POLayer')):
                if i < NumFinger_PM:
                    tmpXYs.append([
                        XYs[0],
                        ((self.getXY('PMOS', '_POLayer')[0][1] - self.getYWidth('PMOS', '_POLayer') / 2) + (self.getXY('PolyRouteX_PM_InputA')[0][1] + self.getYWidth('PolyRouteX_PM_InputA') / 2)) / 2
                    ])
            self._DesignParameter['PolyRouteY_PMA']['_XYCoordinates'] = tmpXYs

            self._DesignParameter['PolyRouteY_NMA'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=ChannelLength,
                _YWidth=((self.getXY('PolyRouteX_NM_InputA')[0][1] - self.getYWidth('PolyRouteX_NM_InputA') / 2) - (self.getXY('NMOS', '_POLayer')[0][1] + self.getYWidth('NMOS', '_POLayer') / 2))
            )
            tmpXYs = []
            for i, XYs in enumerate(self.getXY('NMOS', '_POLayer')):
                if i < NumFinger_NM:
                    tmpXYs.append([
                        XYs[0],
                        ((self.getXY('PolyRouteX_NM_InputA')[0][1] - self.getYWidth('PolyRouteX_NM_InputA') / 2) + (self.getXY('NMOS', '_POLayer')[0][1] + self.getYWidth('NMOS', '_POLayer') / 2)) / 2
                    ])
            self._DesignParameter['PolyRouteY_NMA']['_XYCoordinates'] = tmpXYs

            self._DesignParameter['PolyRouteY_PMNMA'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=self.getXWidth('ViaPoly_InputAB', '_POLayer'),
                _YWidth=((self.getXY('PolyRouteX_PM_InputA')[0][1] - self.getYWidth('PolyRouteX_PM_InputA') / 2) - (self.getXY('PolyRouteX_NM_InputA')[0][1] + self.getYWidth('PolyRouteX_NM_InputA') / 2)),
                _XYCoordinates=[[
                    self.getXY('ViaPoly_InputAB')[0][0],
                    ((self.getXY('PolyRouteX_PM_InputA')[0][1] - self.getYWidth('PolyRouteX_PM_InputA') / 2) + (self.getXY('PolyRouteX_NM_InputA')[0][1] + self.getYWidth('PolyRouteX_NM_InputA') / 2)) / 2
                ]]
            )
        # End of 'if max(NumFinger_NM, NumFinger_PM) < self.Num_HorizontalInputViaMode:   else:   '

        if NumFinger_PM == 1:
            del self._DesignParameter['PMOS']
            del self._DesignParameter['Met1RouteX_PMUp']
            del self._DesignParameter['Met1RouteY_PMUp']
            del self._DesignParameter['Met1RouteX_PMDown']
            del self._DesignParameter['Met1RouteY_PMDown']
            del self._DesignParameter['Met1RouteX_PMOut']
            del self._DesignParameter['Met1RouteY_PMOut']
            if 'Met1RouteY_OutputPM2NM_PMside' in self._DesignParameter:
                del self._DesignParameter['Met1RouteY_OutputPM2NM_PMside']

            self._DesignParameter['PMOS'] = self._SrefElementDeclaration(_DesignObj=CascodePMOS._CascodePMOS(_Name='PMOSIn{}'.format(_Name)))[0]
            self._DesignParameter['PMOS']['_DesignObj']._CalculateDesignParameter(
                **dict(_PMOSChannelWidth=PMOSWidth, _PMOSChannellength=ChannelLength,
                       _PMOSDummy=True, _GateSpacing=GateSpacing, _SDWidth=66, _XVT=XVT))
            self._DesignParameter['PMOS']['_XYCoordinates'] = [[0, YCoordOfPM]]

            # po dummy
            if '_PODummyLayer' in self._DesignParameter['PMOS']['_DesignObj']._DesignParameter:
                Area_PmosDummy = self.getXWidth('PMOS', '_PODummyLayer') * self.getYWidth('PMOS', '_PODummyLayer')
                if Area_PmosDummy < drc._PODummyMinArea:
                    YWidth_PmosDummy_Recalc = self.CeilMinSnapSpacing(drc._PODummyMinArea / self.getXWidth('PMOS', '_PODummyLayer'), drc._MinSnapSpacing * 2)
                    self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] = YWidth_PmosDummy_Recalc

            self._DesignParameter['Met1RouteX_OutputPM2NM_PMside']['_XYCoordinates'] = [[
                self.getXY('Met1RouteX_OutputPM2NM_PMside')[0][0],
                self.getXY('PMOS', '_Met1Layer')[0][1] - self.getYWidth('PMOS', '_Met1Layer') / 2 + self.getYWidth('Met1RouteX_OutputPM2NM_PMside') / 2
            ]]

            TopBoundary_Met1RouteY_OutputPM2NM = self.getXY('Met1RouteX_OutputPM2NM_PMside')[0][1] + self.getYWidth('Met1RouteX_OutputPM2NM_PMside') / 2
            BotBoundary_Met1RouteY_OutputPM2NM = self.getXY('Met1RouteX_NMout')[0][1] - self.getYWidth('Met1RouteX_NMout') / 2

            self._DesignParameter['Met1RouteY_OutputPM2NM']['_YWidth'] = TopBoundary_Met1RouteY_OutputPM2NM - BotBoundary_Met1RouteY_OutputPM2NM
            self._DesignParameter['Met1RouteY_OutputPM2NM']['_XYCoordinates'] = [[
                0, (TopBoundary_Met1RouteY_OutputPM2NM + BotBoundary_Met1RouteY_OutputPM2NM) / 2
            ]]
        else:
            pass

        ''' Pin(Label) '''
        self._DesignParameter['PIN_VSS'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.04, _Angle=0, _TEXT='VSS',
            _XYCoordinates=[[0, 0]]
        )
        self._DesignParameter['PIN_VDD'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.04, _Angle=0, _TEXT='VDD',
            _XYCoordinates=[[0, CellHeight]]
        )
        self._DesignParameter['PIN_A'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='A',
            _XYCoordinates=[self.getXY('ViaPoly_InputAB')[0]],
        )
        self._DesignParameter['PIN_B'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='B',
            _XYCoordinates=[self.getXY('ViaPoly_InputAB')[1]],
        )
        self._DesignParameter['PIN_Y'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='Y',
            _XYCoordinates=[[self.getXY('Met1RouteY_OutputPM2NM')[0][0], YCoordOfInputOutput]]
        )


if __name__ == '__main__':
    from Private import Myinfo
    import DRCchecker_test2 as DRCchecker
    from generatorLib.IksuPack import PlaygroundBot

    My = Myinfo.USER(DesignParameters._Technology)
    Bot = PlaygroundBot.PGBot(token=My.BotToken, chat_id=My.ChatID)


    libname = 'TEST_NOR2'
    cellname = 'NOR2'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''

    InputParams = dict(
        NumFinger_PM=5,
        NumFinger_NM=5,
        PMOSWidth=600,
        NMOSWidth=30,

        CellHeight=None,
        YCoordOfNM=None,
        YCoordOfPM=None,
        YCoordOfInputOutput=None,

        ChannelLength=30,
        GateSpacing=100,
        XVT='SLVT',
        SupplyRailType=2,
    )

    Mode_DRCCheck = False  # True | False
    Num_DRCCheck = 10

    Checker = DRCchecker.DRCchecker(
        username=My.ID,
        password=My.PW,
        WorkDir=My.Dir_Work,
        DRCrunDir=My.Dir_DRCrun,
        GDSDir=My.Dir_GDS,
        libname=libname,
        cellname=cellname,
    )



    if Mode_DRCCheck:
        ErrCount = 0            # DRC error
        knownErrorCount = 0     # failed to generate design. NotImplementedError

        start_time = time.time()
        for ii in range(0, Num_DRCCheck):
            if ii == 0:
                Bot.send2Bot(f'Start DRC checker...\nCellName: {cellname}\nTotal # of Run: {Num_DRCCheck}')

            forLoopCntMax = 10
            for iii in range(0, forLoopCntMax):
                try:
                    ''' ------------------------------- Random Parameters for Layout Object -------------------------------- '''
                    InputParams['NumFinger_PM'] = DRCchecker.RandomParam(start=1, stop=15, step=1)
                    InputParams['NumFinger_NM'] = DRCchecker.RandomParam(start=1, stop=15, step=1)
                    InputParams['PMOSWidth'] = DRCchecker.RandomParam(start=200, stop=1000, step=20)
                    InputParams['NMOSWidth'] = DRCchecker.RandomParam(start=200, stop=1000, step=20)

                    InputParams['SupplyRailType'] = DRCchecker.RandomParam(start=1, stop=2, step=1)

                    print("   Last Layout Object's Input Parameters are   ".center(105, '='))
                    tmpStr = '\n'.join(f'{k} : {v}' for k, v in InputParams.items())
                    print(tmpStr)
                    print("".center(105, '='))

                    ''' ---------------------------------- Generate Layout Object -------------------------------------------'''
                    LayoutObj = NOR2(_Name=cellname)
                    LayoutObj._CalculateDesignParameter(**InputParams)
                    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
                    testStreamFile = open('./{}'.format(_fileName), 'wb')
                    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
                    tmp.write_binary_gds_stream(testStreamFile)
                    testStreamFile.close()
                except NotImplementedError:  # something known error !
                    print(f"forLoopCnt = {iii + 1}")
                    if iii + 1 == forLoopCntMax:
                        raise NotImplementedError
                else:
                    knownErrorCount = knownErrorCount + iii
                    # Bot.send2Bot(f"NotImplementedError...\nknownErrorCount = {knownErrorCount}")
                    break
            # end of for loop

            print('   Sending to FTP Server & StreamIn...   '.center(105, '#'))
            Checker.Upload2FTP()
            Checker.StreamIn(tech=DesignParameters._Technology)

            print(f'   DRC checking... {ii + 1}/{Num_DRCCheck}   '.center(105, '#'))
            try:
                Checker.DRCchecker()
            except Exception as e:      # something error
                ErrCount = ErrCount + 1
                print('Error Occurred: ', e)
                print("   Last Layout Object's Input Parameters are   ".center(105, '='))
                print(tmpStr)
                print("".center(105, '='))
                m, s = divmod(time.time() - start_time, 60)
                h, m = divmod(m, 60)
                Bot.send2Bot(f'Error Occurred During Checking DRC({ii + 1}/{Num_DRCCheck})...\n'
                             f'CellName : {cellname}\n'
                             f'ErrMsg : {e}\n'
                             f'============================\n'
                             f'** InputParameters:\n'
                             f'{tmpStr}\n'
                             f'============================\n'
                             f'** Elapsed Time: {int(h)}:{int(m):0>2}:{int(s):0>2}s')

            if (ii + 1) == Num_DRCCheck:
                elapsed_time = time.time() - start_time
                m, s = divmod(elapsed_time, 60)
                h, m = divmod(m, 60)
                Bot.send2Bot(f'DRC Checker Finished.\n'
                             f'CellName: {cellname}\n'
                             f'Total # of known Err: {knownErrorCount}\n'
                             f'Total # of DRC Err: {ErrCount}\n'
                             f'Total # of Run: {Num_DRCCheck}\n'
                             f'Elapsed Time: {int(h)}:{int(m):0>2}:{int(s):0>2}s')
    else:
        ''' ------------------------------------ Generate Layout Object ---------------------------------------------'''
        LayoutObj = NOR2(_Name=cellname)
        LayoutObj._CalculateDesignParameter(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
        testStreamFile = open('./{}'.format(_fileName), 'wb')
        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        print('   Sending to FTP Server & StreamIn...   '.center(105, '#'))
        Checker.Upload2FTP()
        Checker.StreamIn(tech=DesignParameters._Technology)

    print('      Finished       '.center(105, '#'))
