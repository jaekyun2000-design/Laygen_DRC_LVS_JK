from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
import time
from generatorLib import DRC
from generatorLib import CoordinateCalc as CoordCalc
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaMet22Met3
from generatorLib.generator_models import MUX_PI_4to2
from generatorLib.generator_models import MUX_PI_4to2_half
from generatorLib.generator_models import Inverter


class PI_clk_sel_8p_s(StickDiagram._StickDiagram):
    def __init__(self, _DesignParameter=None, _Name='PI_clk_sel_8p_s'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter_v2(self,
                                     TristateInv1_Finger=1,
                                     TristateInv1_PMOSWidth=400,
                                     TristateInv1_NMOSWidth=200,
                                     TristateInv1_VDD2PMOS=None,            # Optional (Not work when finger >= 3)
                                     TristateInv1_VSS2NMOS=None,            # Optional (Not work when finger >= 3)
                                     TristateInv1_YCoordOfInputA=None,      # Optional
                                     TristateInv1_YCoordOfInputEN=None,     # Optional
                                     TristateInv1_YCoordOfInputENb=None,    # Optional

                                     TristateInv2_Finger=2,
                                     TristateInv2_PMOSWidth=400,
                                     TristateInv2_NMOSWidth=200,
                                     TristateInv2_VDD2PMOS=None,            # Optional (Not work when finger >= 3)
                                     TristateInv2_VSS2NMOS=None,            # Optional (Not work when finger >= 3)
                                     TristateInv2_YCoordOfInputA=None,      # Optional
                                     TristateInv2_YCoordOfInputEN=None,     # Optional
                                     TristateInv2_YCoordOfInputENb=None,    # Optional

                                     Inv_Finger=1,
                                     Inv_PMOSWidth=400,
                                     Inv_NMOSWidth=200,
                                     Inv_VDD2PMOS=None,                     # Optional
                                     Inv_VSS2NMOS=None,                     # Optional
                                     Inv_YCoordOfInOut=None,                # Optional

                                     Inv2_Finger=1,
                                     Inv2_PMOSWidth=400,
                                     Inv2_NMOSWidth=200,
                                     Inv2_VDD2PMOS=None,                    # Optional
                                     Inv2_VSS2NMOS=None,                    # Optional
                                     Inv2_YCoordOfInOut=None,               # Optional

                                     ChannelLength=30,
                                     GateSpacing=100,
                                     XVT='SLVT',
                                     CellHeight=1800,
                                     SupplyRailType=1,
                                     ):

        """
        top

        """

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        UnitPitch = ChannelLength + GateSpacing

        # Minimum CellHeight Calculation
        ParametersForMinHeightCalc_MUX4to2 = dict(
            TristateInv1_Finger=TristateInv1_Finger,
            TristateInv1_PMOSWidth=TristateInv1_PMOSWidth,
            TristateInv1_NMOSWidth=TristateInv1_NMOSWidth,
            TristateInv2_Finger=TristateInv2_Finger,
            TristateInv2_PMOSWidth=TristateInv2_PMOSWidth,
            TristateInv2_NMOSWidth=TristateInv2_NMOSWidth,
            Inv_Finger=Inv_Finger,
            Inv_NMOSWidth=Inv_NMOSWidth,
            Inv_PMOSWidth=Inv_PMOSWidth,
            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            XVT=XVT,
            SupplyRailType=SupplyRailType)
        # additional valid check?
        self._DesignParameter['MuxHalf_CalcMinHeight'] = self._SrefElementDeclaration(
            _DesignObj=MUX_PI_4to2_half.MUX_PI_4to2_half(_Name='MuxHalf_CalcMinHeightIn{}'.format(_Name)))[0]
        minCellHeight_MUX4to2Half = self._DesignParameter['MuxHalf_CalcMinHeight']['_DesignObj']._CalculateMinHeight(**ParametersForMinHeightCalc_MUX4to2)

        ParametersForMinHeightCalc_Inv2 = dict(
            _Finger=Inv2_Finger,
            _ChannelWidth=Inv2_NMOSWidth,
            _ChannelLength=ChannelLength,
            _NPRatio=Inv2_PMOSWidth / Inv2_NMOSWidth,
            _Dummy=True,
            _XVT=XVT,
            _GateSpacing=GateSpacing,
            # _SDWidth=SDWidth,
            _SupplyRailType=SupplyRailType
        )
        self._DesignParameter['INV2_CalcMinHeight'] = self._SrefElementDeclaration(_DesignObj=Inverter._Inverter(_Name='INV2_CalcMinHeightIn{}'.format(_Name)))[0]
        minCellHeight_INV = self._DesignParameter['INV2_CalcMinHeight']['_DesignObj']._CalcMinHeight(**ParametersForMinHeightCalc_Inv2)
        minCellHeight = max(minCellHeight_MUX4to2Half, minCellHeight_INV)

        del self._DesignParameter['MuxHalf_CalcMinHeight']
        del self._DesignParameter['INV2_CalcMinHeight']

        if CellHeight == None:
            _CellHeight = minCellHeight
        elif CellHeight < minCellHeight:
            raise NotImplementedError(f"Input CellHeight={CellHeight}, but minimum value is {minCellHeight}")
        else:
            _CellHeight = CellHeight


        Parameters = dict(TristateInv1_Finger=TristateInv1_Finger,
                          TristateInv1_PMOSWidth=TristateInv1_PMOSWidth,
                          TristateInv1_NMOSWidth=TristateInv1_NMOSWidth,
                          TristateInv1_VDD2PMOS=TristateInv1_VDD2PMOS,            # Optional (Not work when finger >= 3)
                          TristateInv1_VSS2NMOS=TristateInv1_VSS2NMOS,            # Optional (Not work when finger >= 3)
                          TristateInv1_YCoordOfInputA=TristateInv1_YCoordOfInputA,      # Optional
                          TristateInv1_YCoordOfInputEN=TristateInv1_YCoordOfInputEN,     # Optional
                          TristateInv1_YCoordOfInputENb=TristateInv1_YCoordOfInputENb,    # Optional

                          TristateInv2_Finger=TristateInv2_Finger,
                          TristateInv2_PMOSWidth=TristateInv2_PMOSWidth,
                          TristateInv2_NMOSWidth=TristateInv2_NMOSWidth,
                          TristateInv2_VDD2PMOS=TristateInv2_VDD2PMOS,            # Optional (Not work when finger >= 3)
                          TristateInv2_VSS2NMOS=TristateInv2_VSS2NMOS,            # Optional (Not work when finger >= 3)
                          TristateInv2_YCoordOfInputA=TristateInv2_YCoordOfInputA,      # Optional
                          TristateInv2_YCoordOfInputEN=TristateInv2_YCoordOfInputEN,     # Optional
                          TristateInv2_YCoordOfInputENb=TristateInv2_YCoordOfInputENb,    # Optional

                          Inv_Finger=Inv_Finger,
                          Inv_NMOSWidth=Inv_NMOSWidth,
                          Inv_PMOSWidth=Inv_PMOSWidth,
                          Inv_VDD2PMOS=Inv_VDD2PMOS,                 # Optional
                          Inv_VSS2NMOS=Inv_VSS2NMOS,                 # Optional
                          Inv_YCoordOfInOut=Inv_YCoordOfInOut,                # Optional

                          ChannelLength=ChannelLength,
                          GateSpacing=GateSpacing,
                          XVT=XVT,
                          CellHeight=_CellHeight,
                          SupplyRailType=SupplyRailType,)

        self._DesignParameter['Mux1'] = self._SrefElementDeclaration(
            _DesignObj=MUX_PI_4to2.MUX_PI_4to2(_Name='Mux1In{}'.format(_Name)))[0]
        self._DesignParameter['Mux1']['_DesignObj']._CalculateDesignParameter_v2(**Parameters)
        self._DesignParameter['Mux1']['_XYCoordinates'] = [[0,0]]

        self._DesignParameter['Mux2'] = self._SrefElementDeclaration(
            _Reflect=[1, 0, 0], _Angle=0,
            _DesignObj=MUX_PI_4to2.MUX_PI_4to2(_Name='Mux2In{}'.format(_Name)))[0]
        self._DesignParameter['Mux2']['_DesignObj']._CalculateDesignParameter_v2(**Parameters)
        self._DesignParameter['Mux2']['_XYCoordinates'] = [[0, 4*_CellHeight]]

        Parameters_Inv = dict(
            _Finger=Inv2_Finger,
            _ChannelWidth=Inv2_NMOSWidth,
            _ChannelLength=ChannelLength,
            _NPRatio=Inv2_PMOSWidth/Inv2_NMOSWidth,

            _VDD2VSSHeight=_CellHeight,
            _VDD2PMOSHeight=Inv2_VDD2PMOS,
            _VSS2NMOSHeight=Inv2_VSS2NMOS,
            _YCoordOfInput=Inv2_YCoordOfInOut,

            _Dummy=True,
            _XVT=XVT,
            _GateSpacing=GateSpacing,
            _SDWidth=66,
            _SupplyRailType=SupplyRailType,
        )


        self._DesignParameter['Inv0'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0, _DesignObj=Inverter._Inverter(_Name='Inv0In{}'.format(_Name)))[0]
        self._DesignParameter['Inv0']['_DesignObj']._CalculateDesignParameter_v3(**Parameters_Inv)
        self._DesignParameter['Inv1'] = self._SrefElementDeclaration(
            _Reflect=[1, 0, 0], _Angle=0, _DesignObj=Inverter._Inverter(_Name='Inv1In{}'.format(_Name)))[0]
        self._DesignParameter['Inv1']['_DesignObj']._CalculateDesignParameter_v3(**Parameters_Inv)
        self._DesignParameter['Inv2'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0, _DesignObj=Inverter._Inverter(_Name='Inv2In{}'.format(_Name)))[0]
        self._DesignParameter['Inv2']['_DesignObj']._CalculateDesignParameter_v3(**Parameters_Inv)
        self._DesignParameter['Inv3'] = self._SrefElementDeclaration(
            _Reflect=[1, 0, 0], _Angle=0, _DesignObj=Inverter._Inverter(_Name='Inv3In{}'.format(_Name)))[0]
        self._DesignParameter['Inv3']['_DesignObj']._CalculateDesignParameter_v3(**Parameters_Inv)

        XCoord_Inv = self.getXYRight('Mux1', 'MuxHalf1', 'VDDRail')[0][0] + self._DesignParameter['Inv2']['_DesignObj'].CellXWidth / 2

        self._DesignParameter['Inv0']['_XYCoordinates'] = [[XCoord_Inv, 0]]
        self._DesignParameter['Inv1']['_XYCoordinates'] = [[XCoord_Inv, _CellHeight * 2]]
        self._DesignParameter['Inv2']['_XYCoordinates'] = [[XCoord_Inv, _CellHeight * 2]]
        self._DesignParameter['Inv3']['_XYCoordinates'] = [[XCoord_Inv, _CellHeight * 4]]

        # PODummy - INVerter InputVia0
        if Parameters_Inv['_Finger'] in (1, 2):
            tmpStrPMOS = 'PMOS' if Parameters['TristateInv2_Finger'] in (1, 2) else 'PM2'  # check
            tmpStrNMOS = 'NMOS' if Parameters['TristateInv2_Finger'] in (1, 2) else 'NM2'
            xDistance = self.getXYLeft('Inv0', '_VIAPoly2Met1_F1', '_POLayer')[0][0] - CoordCalc.getXYCoords_MaxX(self.getXYRight('Mux1', 'MuxHalf1', 'TristateInv3', tmpStrPMOS, '_PODummyLayer'))[0][0]
            yDistancePMOS = self.getXYBot('Mux1', 'MuxHalf1', 'TristateInv3', tmpStrPMOS, '_PODummyLayer')[0][1] - self.getXYTop('Inv0', '_VIAPoly2Met1_F1', '_POLayer')[0][1]
            yDistanceNMOS = self.getXYBot('Inv0', '_VIAPoly2Met1_F1', '_POLayer')[0][1] - self.getXYTop('Mux1', 'MuxHalf1', 'TristateInv3', tmpStrNMOS, '_PODummyLayer')[0][1]
            if xDistance ** 2 + min(abs(yDistancePMOS), abs(yDistanceNMOS)) ** 2 < drc._PolygateMinSpace ** 2 or yDistancePMOS < 0 or yDistanceNMOS < 0:
                yDistance_min_byDRC = self.CeilMinSnapSpacing(math.sqrt(drc._PolygateMinSpace ** 2 - xDistance ** 2), drc._MinSnapSpacing)
                yMax = min(self.getXYBot('Mux1', 'MuxHalf1', 'TristateInv3', tmpStrPMOS, '_PODummyLayer')[0][1], self.getXYBot('Inv0', '_PMOS', '_PODummyLayer')[0][1]) - yDistance_min_byDRC
                yMin = max(self.getXYTop('Mux1', 'MuxHalf1', 'TristateInv3', tmpStrNMOS, '_PODummyLayer')[0][1], self.getXYTop('Inv0', '_NMOS', '_PODummyLayer')[0][1]) + yDistance_min_byDRC
                if yMax - yMin < self.getYWidth('Inv0', '_VIAPoly2Met1_F1', '_POLayer'):
                    raise NotImplementedError
                else:
                    # re calculate Inverter
                    del self._DesignParameter['Inv0']
                    del self._DesignParameter['Inv1']
                    del self._DesignParameter['Inv2']
                    del self._DesignParameter['Inv3']
                    Parameters_Inv['_YCoordOfInput'] = (yMax + yMin) / 2
                    self._DesignParameter['Inv0'] = self._SrefElementDeclaration(
                        _Reflect=[0, 0, 0], _Angle=0, _DesignObj=Inverter._Inverter(_Name='Inv0In{}'.format(_Name)))[0]
                    self._DesignParameter['Inv0']['_DesignObj']._CalculateDesignParameter_v3(**Parameters_Inv)
                    self._DesignParameter['Inv1'] = self._SrefElementDeclaration(
                        _Reflect=[1, 0, 0], _Angle=0, _DesignObj=Inverter._Inverter(_Name='Inv1In{}'.format(_Name)))[0]
                    self._DesignParameter['Inv1']['_DesignObj']._CalculateDesignParameter_v3(**Parameters_Inv)
                    self._DesignParameter['Inv2'] = self._SrefElementDeclaration(
                        _Reflect=[0, 0, 0], _Angle=0, _DesignObj=Inverter._Inverter(_Name='Inv2In{}'.format(_Name)))[0]
                    self._DesignParameter['Inv2']['_DesignObj']._CalculateDesignParameter_v3(**Parameters_Inv)
                    self._DesignParameter['Inv3'] = self._SrefElementDeclaration(
                        _Reflect=[1, 0, 0], _Angle=0, _DesignObj=Inverter._Inverter(_Name='Inv3In{}'.format(_Name)))[0]
                    self._DesignParameter['Inv3']['_DesignObj']._CalculateDesignParameter_v3(**Parameters_Inv)

                    XCoord_Inv = self.getXYRight('Mux1', 'MuxHalf1', 'VDDRail')[0][0] + self._DesignParameter['Inv2']['_DesignObj'].CellXWidth / 2
                    self._DesignParameter['Inv0']['_XYCoordinates'] = [[XCoord_Inv, 0]]
                    self._DesignParameter['Inv1']['_XYCoordinates'] = [[XCoord_Inv, _CellHeight * 2]]
                    self._DesignParameter['Inv2']['_XYCoordinates'] = [[XCoord_Inv, _CellHeight * 2]]
                    self._DesignParameter['Inv3']['_XYCoordinates'] = [[XCoord_Inv, _CellHeight * 4]]
            else:
                pass  # No DRC Error
        else:
            pass


        ''' --- TristateInverter3 - LastInverter '''
        if TristateInv2_Finger == 1:
            pass
        elif TristateInv2_Finger == 2:
            rightBoundary = self.getXYRight('Inv0', 'InputMet1')[0][0]
            leftBoundary = self.getXYLeft('Mux1', 'MuxHalf1', 'TristateInv3', 'met1_output_5')[0][0]
            self._DesignParameter['Met1Boundary01'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=rightBoundary - leftBoundary,
                _YWidth=66,
                _XYCoordinates=[
                    [(rightBoundary + leftBoundary) / 2, self.getXY('Inv0', 'InputMet1')[0][1]],
                    [(rightBoundary + leftBoundary) / 2, self.getXY('Inv1', 'InputMet1')[0][1]],
                    [(rightBoundary + leftBoundary) / 2, self.getXY('Inv2', 'InputMet1')[0][1]],
                    [(rightBoundary + leftBoundary) / 2, self.getXY('Inv3', 'InputMet1')[0][1]],
                ]
            )
        else:
            rightBoundary = self.getXYRight('Inv0', 'InputMet1')[0][0]
            leftBoundary = self.getXYLeft('Mux1', 'MuxHalf1', 'TristateInv3', 'Met1RouteY_Out')[0][0]
            self._DesignParameter['Met1Boundary01'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=rightBoundary-leftBoundary,
                _YWidth=66,
                _XYCoordinates=[
                    [(rightBoundary + leftBoundary) / 2, self.getXY('Inv0', 'InputMet1')[0][1]],
                    [(rightBoundary + leftBoundary) / 2, self.getXY('Inv1', 'InputMet1')[0][1]],
                    [(rightBoundary + leftBoundary) / 2, self.getXY('Inv2', 'InputMet1')[0][1]],
                    [(rightBoundary + leftBoundary) / 2, self.getXY('Inv3', 'InputMet1')[0][1]],
                ]
            )

        # NW
        rightBoundary = self.getXYRight('Inv0', '_NWLayerBoundary')[0][0]
        leftBoundary = self.getXYLeft('Mux1', 'MuxHalf1', '_NWLayer')[0][0]

        botBoundary1 = self.getXYBot('Inv0', '_NWLayerBoundary')[0][1]
        botBoundary2 = self.getXYBot('Mux1', 'MuxHalf1', '_NWLayer')[0][1]
        YWidth = 2*(_CellHeight - min(botBoundary1, botBoundary2))

        self._DesignParameter['_NWLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=YWidth,
            _XYCoordinates=[
                [(rightBoundary + leftBoundary) / 2, _CellHeight * 1],
                [(rightBoundary + leftBoundary) / 2, _CellHeight * 3]
            ]
        )

        # BP
        rightBoundary = self.getXYRight('Inv0', '_PMOS', '_PPLayer')[0][0]
        leftBoundary = self.getXYLeft('Mux1', 'MuxHalf1', '_PPLayerForPMOS')[0][0]

        topBoundary1 = self.getXYTop('Mux1', 'MuxHalf1', '_PPLayerForPMOS')[0][1]
        botBoundary1 = self.getXYBot('Mux1', 'MuxHalf1', '_PPLayerForPMOS')[0][1]
        topBoundary2 = self.getXYTop('Inv0', '_PMOS', '_PPLayer')[0][1]
        botBoundary2 = self.getXYBot('Inv0', '_PMOS', '_PPLayer')[0][1]
        topBoundary = max(topBoundary1, topBoundary2)
        botBoundary = min(botBoundary1, botBoundary2)
        YCoord_PPLayer1 = (topBoundary + botBoundary) / 2

        self._DesignParameter['_PPLayerForPMOS'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=topBoundary-botBoundary,
            _XYCoordinates=[
                [(rightBoundary + leftBoundary) / 2, YCoord_PPLayer1],
                [(rightBoundary + leftBoundary) / 2, _CellHeight * 2 - YCoord_PPLayer1],
                [(rightBoundary + leftBoundary) / 2, _CellHeight * 2 + YCoord_PPLayer1],
                [(rightBoundary + leftBoundary) / 2, _CellHeight * 4 - YCoord_PPLayer1],

            ]
        )


        ''' -------------------------------------------------------------------------------------------------------- '''
        print(''.center(105, '#'))
        print('     {} Calculation End     '.format(_Name).center(105, '#'))
        print(''.center(105, '#'))


if __name__ == '__main__':
    from Private import Myinfo
    import DRCchecker_test2 as DRCchecker
    from generatorLib.IksuPack import PlaygroundBot

    My = Myinfo.USER(DesignParameters._Technology)
    Bot = PlaygroundBot.PGBot(token=My.BotToken, chat_id=My.ChatID)


    libname = 'TEST_PI_clk_sel_8p'
    cellname = 'PI_clk_sel_8p'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''

    InputParams = dict(
        TristateInv1_Finger=9,
        TristateInv1_PMOSWidth=620,
        TristateInv1_NMOSWidth=860,
        TristateInv1_VDD2PMOS=None,  # Optional (Not work when finger >= 3)
        TristateInv1_VSS2NMOS=None,  # Optional (Not work when finger >= 3)
        TristateInv1_YCoordOfInputA=None,  # Optional
        TristateInv1_YCoordOfInputEN=None,  # Optional
        TristateInv1_YCoordOfInputENb=None,  # Optional

        TristateInv2_Finger=5,
        TristateInv2_PMOSWidth=240,
        TristateInv2_NMOSWidth=200,
        TristateInv2_VDD2PMOS=None,  # Optional (Not work when finger >= 3)
        TristateInv2_VSS2NMOS=None,  # Optional (Not work when finger >= 3)
        TristateInv2_YCoordOfInputA=None,  # Optional
        TristateInv2_YCoordOfInputEN=None,  # Optional
        TristateInv2_YCoordOfInputENb=None,  # Optional

        Inv_Finger=8,
        Inv_PMOSWidth=680,
        Inv_NMOSWidth=780,
        Inv_VDD2PMOS=None,  # Optional
        Inv_VSS2NMOS=None,  # Optional
        Inv_YCoordOfInOut=None,  # Optional

        Inv2_Finger=1,
        Inv2_PMOSWidth=280,
        Inv2_NMOSWidth=960,
        Inv2_VDD2PMOS=None,  # Optional
        Inv2_VSS2NMOS=None,  # Optional
        Inv2_YCoordOfInOut=None,  # Optional

        ChannelLength=30,
        GateSpacing=100,
        XVT='SLVT',
        CellHeight=None,            #
        SupplyRailType=1,
    )

    Checker = DRCchecker.DRCchecker(
        username=My.ID,
        password=My.PW,
        WorkDir=My.Dir_Work,
        DRCrunDir=My.Dir_DRCrun,
        GDSDir=My.Dir_GDS,
        libname=libname,
        cellname=cellname,
    )

    Mode_DRCCheck = True  # True | False
    Num_DRCCheck = 100

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
                    InputParams['TristateInv1_Finger'] = DRCchecker.RandomParam(start=1, stop=10, step=1)
                    InputParams['TristateInv2_Finger'] = DRCchecker.RandomParam(start=1, stop=10, step=1)
                    InputParams['Inv_Finger'] = DRCchecker.RandomParam(start=1, stop=10, step=1)
                    InputParams['Inv2_Finger'] = DRCchecker.RandomParam(start=1, stop=10, step=1)

                    InputParams['TristateInv1_PMOSWidth'] = DRCchecker.RandomParam(start=200, stop=1000, step=20)
                    InputParams['TristateInv1_NMOSWidth'] = DRCchecker.RandomParam(start=200, stop=1000, step=20)
                    InputParams['TristateInv2_PMOSWidth'] = DRCchecker.RandomParam(start=200, stop=1000, step=20)
                    InputParams['TristateInv2_NMOSWidth'] = DRCchecker.RandomParam(start=200, stop=1000, step=20)
                    InputParams['Inv_PMOSWidth'] = DRCchecker.RandomParam(start=200, stop=1000, step=20)
                    InputParams['Inv_NMOSWidth'] = DRCchecker.RandomParam(start=200, stop=1000, step=20)
                    InputParams['Inv2_PMOSWidth'] = DRCchecker.RandomParam(start=200, stop=1000, step=20)
                    InputParams['Inv2_NMOSWidth'] = DRCchecker.RandomParam(start=200, stop=1000, step=20)

                    print("   Last Layout Object's Input Parameters are   ".center(105, '='))
                    inputParamStr = '\n'.join(f'{k} : {v}' for k, v in InputParams.items())
                    print(inputParamStr)
                    print("".center(105, '='))

                    ''' ---------------------------------- Generate Layout Object -------------------------------------------'''
                    LayoutObj = PI_clk_sel_8p_s(_Name=cellname)
                    LayoutObj._CalculateDesignParameter_v2(**InputParams)
                    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
                    with open(f'./{_fileName}', 'wb') as f:
                        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
                        tmp.write_binary_gds_stream(f)
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
                print(inputParamStr)
                print("".center(105, '='))
                m, s = divmod(time.time() - start_time, 60)
                h, m = divmod(m, 60)
                Bot.send2Bot(f'Error Occurred During Checking DRC({ii + 1}/{Num_DRCCheck})...\n'
                             f'ErrMsg : {e}\n'
                             f'============================\n'
                             f'** InputParameters:\n'
                             f'{inputParamStr}\n'
                             f'============================\n'
                             f'** Elapsed Time: {int(h)}:{int(m):0>2}:{int(s):0>2}s')

            if (ii + 1) == Num_DRCCheck:
                # end time return by str
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
        LayoutObj = PI_clk_sel_8p_s(_Name=cellname)
        LayoutObj._CalculateDesignParameter_v2(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
        with open(f'./{_fileName}', 'wb') as f:
            tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
            tmp.write_binary_gds_stream(f)

        print('   Sending to FTP Server & StreamIn...   '.center(105, '#'))
        Checker.Upload2FTP()
        Checker.StreamIn(tech=DesignParameters._Technology)

    print('      Finished       '.center(105, '#'))

