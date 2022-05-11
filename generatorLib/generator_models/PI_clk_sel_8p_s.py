from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib import CoordinateCalc as CoordCalc
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaMet22Met3
from generatorLib.generator_models import MUX_PI_4to2
from generatorLib.generator_models import Inverter_onesemicon


class PI_clk_sel_8p_s(StickDiagram._StickDiagram):
    def __init__(self, _DesignParameter=None, _Name='PI_clk_sel_8p_s'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name


    def _CalculateDesignParamter(self,
                                 TristateInv1_Finger=1,
                                 Inv_Finger=1,
                                 TristateInv2_Finger=2,
                                 Inv2_Finger=1,

                                 TristateInv1_PMOSWidth=500,
                                 TristateInv1_NMOSWidth=250,
                                 TristateInv1_VDD2PMOS=None,    # 402
                                 TristateInv1_VSS2NMOS=None,     # 275

                                 TristateInv2_PMOSWidth=400,
                                 TristateInv2_NMOSWidth=200,
                                 TristateInv2_VDD2PMOS=None,     # 402
                                 TristateInv2_VSS2NMOS=None,      # 301

                                 TristateInv3_NumFinger_NM1=3,
                                 TristateInv3_NumFinger_NM2=3,
                                 TristateInv3_Width_NM1=250,
                                 TristateInv3_Width_NM2=250,
                                 TristateInv3_Width_PM1=500,
                                 TristateInv3_Width_PM2=500,
                                 TristateInv3_YCoord_InputA=None,    # 750

                                 Inv_NMOSWidth=200,
                                 Inv_PMOSWidth=400,

                                 Inv2_NMOSWidth=300,
                                 Inv2_PMOSWidth=600,

                                 ChannelLength=30,
                                 GateSpacing=100,
                                 XVT='SLVT',
                                 CellHeight=1800,
                                 SupplyRailType=1,

                                 ):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        UnitPitch = ChannelLength + GateSpacing


        Parameters = dict(TristateInv1_Finger=TristateInv1_Finger,
                          Inv_Finger=Inv_Finger,
                          TristateInv2_Finger=TristateInv2_Finger,

                          TristateInv1_PMOSWidth=TristateInv1_PMOSWidth,
                          TristateInv1_NMOSWidth=TristateInv1_NMOSWidth,
                          TristateInv1_VDD2PMOS=TristateInv1_VDD2PMOS,
                          TristateInv1_VSS2NMOS=TristateInv1_VSS2NMOS,

                          TristateInv2_PMOSWidth=TristateInv2_PMOSWidth,
                          TristateInv2_NMOSWidth=TristateInv2_NMOSWidth,
                          TristateInv2_VDD2PMOS=TristateInv2_VDD2PMOS,
                          TristateInv2_VSS2NMOS=TristateInv2_VSS2NMOS,

                          TristateInv3_NumFinger_NM1=TristateInv3_NumFinger_NM1,
                          TristateInv3_NumFinger_NM2=TristateInv3_NumFinger_NM2,
                          TristateInv3_Width_NM1=TristateInv3_Width_NM1,
                          TristateInv3_Width_NM2=TristateInv3_Width_NM2,
                          TristateInv3_Width_PM1=TristateInv3_Width_PM1,
                          TristateInv3_Width_PM2=TristateInv3_Width_PM2,
                          TristateInv3_YCoord_InputA=TristateInv3_YCoord_InputA,

                          Inv_NMOSWidth=Inv_NMOSWidth,
                          Inv_PMOSWidth=Inv_PMOSWidth,

                          ChannelLength=ChannelLength,
                          GateSpacing=GateSpacing,
                          XVT=XVT,
                          CellHeight=CellHeight,
                          SupplyRailType=SupplyRailType,)

        self._DesignParameter['Mux1'] = self._SrefElementDeclaration(
            _DesignObj=MUX_PI_4to2.MUX_PI_4to2(_Name='Mux1In{}'.format(_Name)))[0]
        self._DesignParameter['Mux1']['_DesignObj']._CalculateDesignParamter(**Parameters)
        self._DesignParameter['Mux1']['_XYCoordinates'] = [[0,0]]

        self._DesignParameter['Mux2'] = self._SrefElementDeclaration(
            _Reflect=[1, 0, 0], _Angle=0,
            _DesignObj=MUX_PI_4to2.MUX_PI_4to2(_Name='Mux2In{}'.format(_Name)))[0]
        self._DesignParameter['Mux2']['_DesignObj']._CalculateDesignParamter(**Parameters)
        self._DesignParameter['Mux2']['_XYCoordinates'] = [[0, 4*CellHeight]]

        Parameters_Inv = dict(
            _Finger=Inv2_Finger,
            _ChannelWidth=Inv2_NMOSWidth,
            _ChannelLength=ChannelLength,
            _NPRatio=Inv2_PMOSWidth / Inv2_NMOSWidth,

            _VDD2VSSHeight=CellHeight,
            _VDD2PMOSHeight=None,
            _VSS2NMOSHeight=None,
            _YCoordOfInput=None,

            _Dummy=True,
            _XVT=XVT,
            _GateSpacing=GateSpacing,
            _SDWidth=66,

            _NumViaPMOSMet12Met2CoY=None,
            _NumViaNMOSMet12Met2CoY=None,
            _SupplyRailType=SupplyRailType,
        )
        self._DesignParameter['Inv0'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0, _DesignObj=Inverter_onesemicon._Inverter(_Name='Inv0In{}'.format(_Name)))[0]
        self._DesignParameter['Inv0']['_DesignObj']._CalculateDesignParameter_v3(**Parameters_Inv)
        self._DesignParameter['Inv1'] = self._SrefElementDeclaration(
            _Reflect=[1, 0, 0], _Angle=0, _DesignObj=Inverter_onesemicon._Inverter(_Name='Inv1In{}'.format(_Name)))[0]
        self._DesignParameter['Inv1']['_DesignObj']._CalculateDesignParameter_v3(**Parameters_Inv)
        self._DesignParameter['Inv2'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0, _DesignObj=Inverter_onesemicon._Inverter(_Name='Inv2In{}'.format(_Name)))[0]
        self._DesignParameter['Inv2']['_DesignObj']._CalculateDesignParameter_v3(**Parameters_Inv)
        self._DesignParameter['Inv3'] = self._SrefElementDeclaration(
            _Reflect=[1, 0, 0], _Angle=0, _DesignObj=Inverter_onesemicon._Inverter(_Name='Inv3In{}'.format(_Name)))[0]
        self._DesignParameter['Inv3']['_DesignObj']._CalculateDesignParameter_v3(**Parameters_Inv)

        XCoord_Inv = self.getXYRight('Mux1', 'MuxHalf1', 'VDDRail')[0][0] + self._DesignParameter['Inv2']['_DesignObj'].CellXWidth / 2

        self._DesignParameter['Inv0']['_XYCoordinates'] = [[XCoord_Inv, 0]]
        self._DesignParameter['Inv1']['_XYCoordinates'] = [[XCoord_Inv, CellHeight * 2]]
        self._DesignParameter['Inv2']['_XYCoordinates'] = [[XCoord_Inv, CellHeight * 2]]
        self._DesignParameter['Inv3']['_XYCoordinates'] = [[XCoord_Inv, CellHeight * 4]]

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
        YWidth = 2*(CellHeight - min(botBoundary1, botBoundary2))

        self._DesignParameter['_NWLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=YWidth,
            _XYCoordinates=[
                [(rightBoundary + leftBoundary) / 2, CellHeight * 1],
                [(rightBoundary + leftBoundary) / 2, CellHeight * 3]
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
                [(rightBoundary + leftBoundary) / 2, CellHeight * 2 - YCoord_PPLayer1],
                [(rightBoundary + leftBoundary) / 2, CellHeight * 2 + YCoord_PPLayer1],
                [(rightBoundary + leftBoundary) / 2, CellHeight * 4 - YCoord_PPLayer1],

            ]
        )


        ''' -------------------------------------------------------------------------------------------------------- '''
        print(''.center(105, '#'))
        print('     {} Calculation End     '.format(_Name).center(105, '#'))
        print(''.center(105, '#'))


