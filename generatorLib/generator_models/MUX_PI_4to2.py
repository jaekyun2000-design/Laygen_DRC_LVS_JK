from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
import time
from generatorLib import DRC
from generatorLib import CoordinateCalc as CoordCalc
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaMet22Met3
from generatorLib.generator_models import MUX_PI_4to2_half


class MUX_PI_4to2(StickDiagram._StickDiagram):
    def __init__(self, _DesignParameter=None, _Name='MUX_PI_4to2'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParamter_v2(self,
                                    TristateInv1_Finger=1,
                                    TristateInv1_PMOSWidth=400,
                                    TristateInv1_NMOSWidth=200,
                                    TristateInv1_VDD2PMOS=None,  # Optional (Not work when finger >= 3)
                                    TristateInv1_VSS2NMOS=None,  # Optional (Not work when finger >= 3)
                                    TristateInv1_YCoordOfInputA=None,  # Optional
                                    TristateInv1_YCoordOfInputEN=None,  # Optional
                                    TristateInv1_YCoordOfInputENb=None,  # Optional

                                    TristateInv2_Finger=2,
                                    TristateInv2_PMOSWidth=400,
                                    TristateInv2_NMOSWidth=200,
                                    TristateInv2_VDD2PMOS=None,  # Optional (Not work when finger >= 3)
                                    TristateInv2_VSS2NMOS=None,  # Optional (Not work when finger >= 3)
                                    TristateInv2_YCoordOfInputA=None,  # Optional
                                    TristateInv2_YCoordOfInputEN=None,  # Optional
                                    TristateInv2_YCoordOfInputENb=None,  # Optional

                                    Inv_Finger=1,
                                    Inv_NMOSWidth=200,
                                    Inv_PMOSWidth=400,
                                    Inv_VDD2PMOS=None,  # Optional
                                    Inv_VSS2NMOS=None,  # Optional
                                    Inv_YCoordOfInOut=None,  # Optional

                                    ChannelLength=30,
                                    GateSpacing=100,
                                    XVT='SLVT',
                                    CellHeight=1800,
                                    SupplyRailType=1,
                                    ):
        """
        top function

        """
        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        UnitPitch = ChannelLength + GateSpacing


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
                          CellHeight=CellHeight,
                          SupplyRailType=SupplyRailType,)


        if CellHeight == None:
            ParametersForMinHeightCalc = dict(
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
            minCellHeight = self._DesignParameter['MuxHalf_CalcMinHeight']['_DesignObj']._CalculateMinHeight(**ParametersForMinHeightCalc)





            Parameters['CellHeight'] = minCellHeight
            _CellHeight = minCellHeight
            print(f"Input CellHeigth={CellHeight}, it is set to minimum value({Parameters['CellHeight']}). ")
        else:
            _CellHeight = CellHeight

        self._DesignParameter['MuxHalf1'] = self._SrefElementDeclaration(
            _DesignObj=MUX_PI_4to2_half.MUX_PI_4to2_half(_Name='MuxHalf1In{}'.format(_Name)))[0]
        self._DesignParameter['MuxHalf1']['_DesignObj']._CalculateDesignParamter_v2(**Parameters)
        self._DesignParameter['MuxHalf1']['_XYCoordinates'] = [[0,0]]

        self._DesignParameter['MuxHalf2'] = self._SrefElementDeclaration(
            _Reflect=[1, 0, 0], _Angle=0,
            _DesignObj=MUX_PI_4to2_half.MUX_PI_4to2_half(_Name='MuxHalf2In{}'.format(_Name)))[0]
        self._DesignParameter['MuxHalf2']['_DesignObj']._CalculateDesignParamter_v2(**Parameters)
        self._DesignParameter['MuxHalf2']['_XYCoordinates'] = [[0, 2*_CellHeight]]

        ''' Between Inverter1 and TristateInverter2 '''
        # Path
        self._DesignParameter['Met2Path1'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _Width=66
        )
        self._DesignParameter['Met2Path2'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _Width=66
        )
        self._DesignParameter['Met2Path3'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _Width=66
        )
        self._DesignParameter['Met2Path4'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _Width=66
        )
        if TristateInv2_Finger == 1:

            # YCoordOftempRoute1 = 1033
            # YCoordOftempRoute2 = 2567
            YCoordOftempRoute1 = self.getXYTop('MuxHalf1', 'Via1_temp2_3', '_Met2Layer')[0][1] + drc._MetalxMinSpaceAtCorner + self.getWidth('Met2Path2') / 2
            YCoordOftempRoute2 = self.getXYBot('MuxHalf2', 'Via1_temp2_3', '_Met2Layer')[0][1] - drc._MetalxMinSpaceAtCorner - self.getWidth('Met2Path4') / 2
            self._DesignParameter['Met2Path1']['_XYCoordinates'] = [
                [[self.getXY('MuxHalf1', 'Via1_TSINV2_A')[0][0], self.getXYBot('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1] + self.getWidth('Met2Path1') / 2],
                 [self.getXY('MuxHalf1', 'Via1_TSINV2_A')[0][0] - 2 * UnitPitch, self.getXYBot('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1] + self.getWidth('Met2Path1') / 2]]
            ]
            self._DesignParameter['Met2Path2']['_XYCoordinates'] = [
                [[self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][0], self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][1]],
                 [self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][0], YCoordOftempRoute1],
                 [self.getXY('MuxHalf1', 'Via1_TSINV2_A')[0][0] - 1 * UnitPitch, YCoordOftempRoute1]]   ##
            ]
            self._DesignParameter['Met2Path3']['_XYCoordinates'] = [
                [[self.getXY('MuxHalf2', 'Via1_TSINV2_A')[0][0], self.getXYTop('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1] - self.getWidth('Met2Path3') / 2],
                 [self.getXY('MuxHalf2', 'Via1_TSINV2_A')[0][0] - 1 * UnitPitch, self.getXYTop('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1] - self.getWidth('Met2Path3') / 2]],
            ]
            self._DesignParameter['Met2Path4']['_XYCoordinates'] = [
                [[self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][0], self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][1]],
                 [self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][0], YCoordOftempRoute2],
                 [self.getXY('MuxHalf2', 'Via1_TSINV2_A')[0][0] - 2 * UnitPitch, YCoordOftempRoute2]]   ##
            ]

        elif TristateInv2_Finger == 2:
            # YCoordOftempRoute1 = 1033
            # YCoordOftempRoute2 = 2567
            YCoordOftempRoute1 = max(self.getXYTop('MuxHalf1', 'Via1_temp23', '_Met2Layer')[0][1], self.getXYTop('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1]) + drc._MetalxMinSpaceAtCorner + self.getWidth('Met2Path2') / 2
            YCoordOftempRoute2 = min(self.getXYBot('MuxHalf2', 'Via1_temp23', '_Met2Layer')[0][1], self.getXYBot('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1]) - drc._MetalxMinSpaceAtCorner - self.getWidth('Met2Path4') / 2
            self._DesignParameter['Met2Path1']['_XYCoordinates'] = [
                [[self.getXY('MuxHalf1', 'Via1_TSINV2_A')[0][0], self.getXYBot('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1] + self.getWidth('Met2Path1') / 2],
                 [self.getXY('MuxHalf1', 'TristateInv2', 'NMOS', '_Met1Layer')[-1][0] - 2 * UnitPitch, self.getXYBot('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1] + self.getWidth('Met2Path1') / 2]]
            ]
            self._DesignParameter['Met2Path2']['_XYCoordinates'] = [
                [[self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][0], self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][1]],
                 [self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][0], YCoordOftempRoute1],
                 [self.getXY('MuxHalf1', 'TristateInv2', 'NMOS', '_Met1Layer')[-1][0] - 1 * UnitPitch, YCoordOftempRoute1]]     ##
            ]
            self._DesignParameter['Met2Path3']['_XYCoordinates'] = [
                [[self.getXY('MuxHalf2', 'Via1_TSINV2_A')[0][0], self.getXYTop('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1] - self.getWidth('Met2Path3') / 2],
                 [self.getXY('MuxHalf1', 'TristateInv2', 'NMOS', '_Met1Layer')[-1][0] - 1 * UnitPitch, self.getXYTop('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1] - self.getWidth('Met2Path3') / 2]],
            ]
            self._DesignParameter['Met2Path4']['_XYCoordinates'] = [
                [[self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][0], self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][1]],
                 [self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][0], YCoordOftempRoute2],
                 [self.getXY('MuxHalf1', 'TristateInv2', 'NMOS', '_Met1Layer')[-1][0] - 2 * UnitPitch, YCoordOftempRoute2]]     ##
            ]
        else:
            # YCoordOftempRoute1 = 1066
            # YCoordOftempRoute2 = 2534
            YCoordOftempRoute1 = max(self.getXYTop('MuxHalf1', 'Via1_temp23', '_Met2Layer')[0][1],
                                     self.getXYTop('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1],
                                     self.getXYBot('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1] + self.getYWidth('MuxHalf1', 'Via1_temp23', '_Met2Layer')) \
                                 + drc._MetalxMinSpaceAtCorner + self.getWidth('Met2Path2') / 2
            if self.getXYBot('MuxHalf1', 'TristateInv2', 'via1ForPM1', '_Met2Layer')[0][1] - (YCoordOftempRoute1 + self.getWidth('Met2Path2') / 2) < drc._MetalxMinSpaceAtCorner:
                raise NotImplementedError
            YCoordOftempRoute2 = min(self.getXYBot('MuxHalf2', 'Via1_temp23', '_Met2Layer')[0][1],
                                     self.getXYBot('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1],
                                     self.getXYTop('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1] - self.getYWidth('MuxHalf1', 'Via1_temp23', '_Met2Layer')) \
                                 - drc._MetalxMinSpaceAtCorner - self.getWidth('Met2Path4') / 2
            self._DesignParameter['Met2Path1']['_XYCoordinates'] = [
                [[self.getXY('MuxHalf1', 'Via1_TSINV2_A')[0][0], self.getXYBot('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1] + self.getWidth('Met2Path1') / 2],
                 [self.getXY('MuxHalf1', 'TristateInv2', 'NM2', '_Met1Layer')[-1][0] - 2 * UnitPitch, self.getXYBot('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1] + self.getWidth('Met2Path1') / 2]]
            ]
            self._DesignParameter['Met2Path2']['_XYCoordinates'] = [
                [[self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][0], self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][1]],
                 [self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][0], YCoordOftempRoute1],
                 [self.getXY('MuxHalf1', 'TristateInv2', 'NM2', '_Met1Layer')[-1][0] - 1 * UnitPitch, YCoordOftempRoute1]]      ##
            ]
            self._DesignParameter['Met2Path3']['_XYCoordinates'] = [
                [[self.getXY('MuxHalf2', 'Via1_TSINV2_A')[0][0], self.getXYTop('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1] - self.getWidth('Met2Path3') / 2],
                 [self.getXY('MuxHalf1', 'TristateInv2', 'NM2', '_Met1Layer')[-1][0] - 1 * UnitPitch, self.getXYTop('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1] - self.getWidth('Met2Path3') / 2]],
            ]
            self._DesignParameter['Met2Path4']['_XYCoordinates'] = [
                [[self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][0], self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][1]],
                 [self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][0], YCoordOftempRoute2],
                 [self.getXY('MuxHalf1', 'TristateInv2', 'NM2', '_Met1Layer')[-1][0] - 2 * UnitPitch, YCoordOftempRoute2]]      ##
            ]

        # Via2
        self._DesignParameter['Via2ForPath1'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2ForPath1In{}'.format(_Name)))[0]
        self._DesignParameter['Via2ForPath1']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2)
        self._DesignParameter['Via2ForPath2'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2ForPath2In{}'.format(_Name)))[0]
        self._DesignParameter['Via2ForPath2']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2)
        self._DesignParameter['Via2ForPath3'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2ForPath3In{}'.format(_Name)))[0]
        self._DesignParameter['Via2ForPath3']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2)
        self._DesignParameter['Via2ForPath4'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2ForPath4In{}'.format(_Name)))[0]
        self._DesignParameter['Via2ForPath4']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2)

        self._DesignParameter['Via2ForPath1']['_XYCoordinates'] = [
            [self._DesignParameter['Met2Path1']['_XYCoordinates'][0][-1][0],
             self._DesignParameter['Met2Path1']['_XYCoordinates'][0][-1][1] - self.getWidth('Met2Path1') / 2 + self.getYWidth('Via2ForPath1', '_Met2Layer') / 2]
        ]
        self._DesignParameter['Via2ForPath2']['_XYCoordinates'] = [
            [self._DesignParameter['Met2Path2']['_XYCoordinates'][0][-1][0],
             self._DesignParameter['Met2Path2']['_XYCoordinates'][0][-1][1] - self.getWidth('Met2Path2') / 2 + self.getYWidth('Via2ForPath2', '_Met2Layer') / 2]
        ]
        self._DesignParameter['Via2ForPath3']['_XYCoordinates'] = [
            [self._DesignParameter['Met2Path3']['_XYCoordinates'][0][-1][0],
             self._DesignParameter['Met2Path3']['_XYCoordinates'][0][-1][1] + self.getWidth('Met2Path3') / 2 - self.getYWidth('Via2ForPath3', '_Met2Layer') / 2]
        ]
        self._DesignParameter['Via2ForPath4']['_XYCoordinates'] = [
            [self._DesignParameter['Met2Path4']['_XYCoordinates'][0][-1][0],
             self._DesignParameter['Met2Path4']['_XYCoordinates'][0][-1][1] + self.getWidth('Met2Path4') / 2 - self.getYWidth('Via2ForPath4', '_Met2Layer') / 2]
        ]

        # Met3
        topBoundary = max(self.getXYTop('Via2ForPath3', '_Met3Layer')[0][1], self.getXYTop('Via2ForPath4', '_Met3Layer')[0][1])
        botBoundary = min(self.getXYBot('Via2ForPath1', '_Met3Layer')[0][1], self.getXYBot('Via2ForPath2', '_Met3Layer')[0][1])
        self._DesignParameter['Met3Boundary5'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=self.getXWidth('Via2ForPath1', '_Met3Layer'),
            _YWidth=topBoundary-botBoundary,
            _XYCoordinates=[[self.getXY('Via2ForPath1', '_Met3Layer')[0][0], (topBoundary + botBoundary) / 2]]
        )
        self._DesignParameter['Met3Boundary6'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=self.getXWidth('Via2ForPath2', '_Met3Layer'),
            _YWidth=topBoundary - botBoundary,
            _XYCoordinates=[[self.getXY('Via2ForPath2', '_Met3Layer')[0][0], (topBoundary + botBoundary) / 2]]
        )

        # Via1
        self._DesignParameter['Via1ForPath1'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1ForPath1In{}'.format(_Name)))[0]
        self._DesignParameter['Via1ForPath1']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
        self._DesignParameter['Via1ForPath1']['_XYCoordinates'] = self.getXY('Via2ForPath1')
        self._DesignParameter['Via1ForPath3'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1ForPath3In{}'.format(_Name)))[0]
        self._DesignParameter['Via1ForPath3']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
        self._DesignParameter['Via1ForPath3']['_XYCoordinates'] = self.getXY('Via2ForPath1')

        # met1
        rightBoundary = self.getXYRight('Met3Boundary6')[0][0]
        leftBoundary = CoordCalc.getXYCoords_MaxX(self.getXY('MuxHalf1', 'Inv1', 'PIN_Y'))[0][0] - self.getWidth('MuxHalf1', 'Inv1', '_OutputRouting') / 2
        self._DesignParameter['Met1Boundary7'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=rightBoundary-leftBoundary,
            _YWidth=66
        )
        self._DesignParameter['Met1Boundary8'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self.getXWidth('Met1Boundary7'),
            _YWidth=self.getYWidth('Met1Boundary7')
        )
        self._DesignParameter['Met1Boundary7']['_XYCoordinates'] = [
            [(rightBoundary + leftBoundary) / 2, self.getXYTop('Via1ForPath1', '_Met1Layer')[0][1] - self.getYWidth('Met1Boundary7') / 2]
        ]
        self._DesignParameter['Met1Boundary8']['_XYCoordinates'] = [
            [(rightBoundary + leftBoundary) / 2, _CellHeight * 2 - self.getXY('Met1Boundary7')[0][1]]
        ]

        ''' Met3 '''
        self._DesignParameter['Met3boundary09'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=66
        )
        self._DesignParameter['Met3boundary10'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=self.getWidth('Met3boundary09')
        )
        self._DesignParameter['Met3boundary09']['_XYCoordinates'] = [
            [self.getXYBot('MuxHalf1', 'Via2_temp00', '_Met3Layer')[0],
             self.getXYTop('MuxHalf2', 'Via2_temp00', '_Met3Layer')[0]]
        ]
        self._DesignParameter['Met3boundary10']['_XYCoordinates'] = [
            [self.getXYBot('MuxHalf1', 'Via2_temp00', '_Met3Layer')[1],
             self.getXYTop('MuxHalf2', 'Via2_temp00', '_Met3Layer')[1]]
        ]

        self._DesignParameter['Met3boundary11'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=self.getWidth('Met3boundary09')
        )
        self._DesignParameter['Met3boundary12'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=self.getWidth('Met3boundary09')
        )

        self._DesignParameter['Met3boundary09']['_XYCoordinates'] = [
            [self.getXYBot('MuxHalf1', 'Via2_temp05', '_Met3Layer')[0],
             self.getXYTop('MuxHalf2', 'Via2_temp05', '_Met3Layer')[0]]
        ]
        self._DesignParameter['Met3boundary10']['_XYCoordinates'] = [
            [self.getXYBot('MuxHalf1', 'Via2_temp05', '_Met3Layer')[1],
             self.getXYTop('MuxHalf2', 'Via2_temp05', '_Met3Layer')[1]]
        ]


    # def _CalculateDesignParamter(self,
    #                              TristateInv1_Finger=1,
    #                              Inv_Finger=1,
    #                              TristateInv2_Finger=2,
    #
    #                              TristateInv1_PMOSWidth=500,
    #                              TristateInv1_NMOSWidth=250,
    #                              TristateInv1_VDD2PMOS=None,
    #                              TristateInv1_VSS2NMOS=None,
    #
    #                              TristateInv2_PMOSWidth=400,
    #                              TristateInv2_NMOSWidth=200,
    #                              TristateInv2_VDD2PMOS=None,
    #                              TristateInv2_VSS2NMOS=None,
    #
    #                              TristateInv3_NumFinger_NM1=3,
    #                              TristateInv3_NumFinger_NM2=3,
    #                              TristateInv3_Width_NM1=250,
    #                              TristateInv3_Width_NM2=250,
    #                              TristateInv3_Width_PM1=500,
    #                              TristateInv3_Width_PM2=500,
    #                              TristateInv3_YCoord_InputA=750,
    #
    #                              Inv_NMOSWidth=200,
    #                              Inv_PMOSWidth=400,
    #
    #                              ChannelLength=30,
    #                              GateSpacing=100,
    #                              XVT='SLVT',
    #                              CellHeight=1800,
    #                              SupplyRailType=1,
    #
    #                              ):
    #
    #     drc = DRC.DRC()
    #     _Name = self._DesignParameter['_Name']['_Name']
    #
    #     UnitPitch = ChannelLength + GateSpacing
    #
    #
    #     Parameters = dict(TristateInv1_Finger=TristateInv1_Finger,
    #                       Inv_Finger=Inv_Finger,
    #                       TristateInv2_Finger=TristateInv2_Finger,
    #
    #                       TristateInv1_PMOSWidth=TristateInv1_PMOSWidth,
    #                       TristateInv1_NMOSWidth=TristateInv1_NMOSWidth,
    #                       TristateInv1_VDD2PMOS=TristateInv1_VDD2PMOS,
    #                       TristateInv1_VSS2NMOS=TristateInv1_VSS2NMOS,
    #
    #                       TristateInv2_PMOSWidth=TristateInv2_PMOSWidth,
    #                       TristateInv2_NMOSWidth=TristateInv2_NMOSWidth,
    #                       TristateInv2_VDD2PMOS=TristateInv2_VDD2PMOS,
    #                       TristateInv2_VSS2NMOS=TristateInv2_VSS2NMOS,
    #
    #                       TristateInv3_NumFinger_NM1=TristateInv3_NumFinger_NM1,
    #                       TristateInv3_NumFinger_NM2=TristateInv3_NumFinger_NM2,
    #                       TristateInv3_Width_NM1=TristateInv3_Width_NM1,
    #                       TristateInv3_Width_NM2=TristateInv3_Width_NM2,
    #                       TristateInv3_Width_PM1=TristateInv3_Width_PM1,
    #                       TristateInv3_Width_PM2=TristateInv3_Width_PM2,
    #                       TristateInv3_YCoord_InputA=TristateInv3_YCoord_InputA,
    #
    #                       Inv_NMOSWidth=Inv_NMOSWidth,
    #                       Inv_PMOSWidth=Inv_PMOSWidth,
    #
    #                       ChannelLength=ChannelLength,
    #                       GateSpacing=GateSpacing,
    #                       XVT=XVT,
    #                       CellHeight=CellHeight,
    #                       SupplyRailType=SupplyRailType,)
    #
    #     self._DesignParameter['MuxHalf1'] = self._SrefElementDeclaration(
    #         _DesignObj=MUX_PI_4to2_half.MUX_PI_4to2_half(_Name='MuxHalf1In{}'.format(_Name)))[0]
    #     self._DesignParameter['MuxHalf1']['_DesignObj']._CalculateDesignParamter(**Parameters)
    #     self._DesignParameter['MuxHalf1']['_XYCoordinates'] = [[0,0]]
    #
    #     self._DesignParameter['MuxHalf2'] = self._SrefElementDeclaration(
    #         _Reflect=[1, 0, 0], _Angle=0,
    #         _DesignObj=MUX_PI_4to2_half.MUX_PI_4to2_half(_Name='MuxHalf2In{}'.format(_Name)))[0]
    #     self._DesignParameter['MuxHalf2']['_DesignObj']._CalculateDesignParamter(**Parameters)
    #     self._DesignParameter['MuxHalf2']['_XYCoordinates'] = [[0, 2*CellHeight]]
    #
    #     ''' Between Inverter1 and TristateInverter2 '''
    #     # Path
    #     self._DesignParameter['Met2Path1'] = self._PathElementDeclaration(
    #         _Layer=DesignParameters._LayerMapping['METAL2'][0],
    #         _Datatype=DesignParameters._LayerMapping['METAL2'][1],
    #         _Width=66
    #     )
    #     self._DesignParameter['Met2Path2'] = self._PathElementDeclaration(
    #         _Layer=DesignParameters._LayerMapping['METAL2'][0],
    #         _Datatype=DesignParameters._LayerMapping['METAL2'][1],
    #         _Width=66
    #     )
    #     self._DesignParameter['Met2Path3'] = self._PathElementDeclaration(
    #         _Layer=DesignParameters._LayerMapping['METAL2'][0],
    #         _Datatype=DesignParameters._LayerMapping['METAL2'][1],
    #         _Width=66
    #     )
    #     self._DesignParameter['Met2Path4'] = self._PathElementDeclaration(
    #         _Layer=DesignParameters._LayerMapping['METAL2'][0],
    #         _Datatype=DesignParameters._LayerMapping['METAL2'][1],
    #         _Width=66
    #     )
    #     if TristateInv2_Finger == 1:
    #
    #         YCoordOftempRoute1 = 1033
    #         YCoordOftempRoute2 = 2567
    #         self._DesignParameter['Met2Path1']['_XYCoordinates'] = [
    #             [[self.getXY('MuxHalf1', 'Via1_TSINV2_A')[0][0], self.getXYBot('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1] + self.getWidth('Met2Path1') / 2],
    #              [self.getXY('MuxHalf1', 'Via1_TSINV2_A')[0][0] - 2 * UnitPitch, self.getXYBot('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1] + self.getWidth('Met2Path1') / 2]]
    #         ]
    #         self._DesignParameter['Met2Path2']['_XYCoordinates'] = [
    #             [[self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][0], self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][1]],
    #              [self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][0], YCoordOftempRoute1],
    #              [self.getXY('MuxHalf1', 'Via1_TSINV2_A')[0][0] - 1 * UnitPitch, YCoordOftempRoute1]]
    #         ]
    #         self._DesignParameter['Met2Path3']['_XYCoordinates'] = [
    #             [[self.getXY('MuxHalf2', 'Via1_TSINV2_A')[0][0], self.getXYTop('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1] - self.getWidth('Met2Path3') / 2],
    #              [self.getXY('MuxHalf2', 'Via1_TSINV2_A')[0][0] - 1 * UnitPitch, self.getXYTop('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1] - self.getWidth('Met2Path3') / 2]],
    #         ]
    #         self._DesignParameter['Met2Path4']['_XYCoordinates'] = [
    #             [[self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][0], self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][1]],
    #              [self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][0], YCoordOftempRoute2],
    #              [self.getXY('MuxHalf2', 'Via1_TSINV2_A')[0][0] - 2 * UnitPitch, YCoordOftempRoute2]]
    #         ]
    #
    #     elif TristateInv2_Finger == 2:
    #         YCoordOftempRoute1 = 1033
    #         YCoordOftempRoute2 = 2567
    #         self._DesignParameter['Met2Path1']['_XYCoordinates'] = [
    #             [[self.getXY('MuxHalf1', 'Via1_TSINV2_A')[0][0], self.getXYBot('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1] + self.getWidth('Met2Path1') / 2],
    #              [self.getXY('MuxHalf1', 'TristateInv2', 'NMOS', '_Met1Layer')[-1][0] - 2 * UnitPitch, self.getXYBot('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1] + self.getWidth('Met2Path1') / 2]]
    #         ]
    #         self._DesignParameter['Met2Path2']['_XYCoordinates'] = [
    #             [[self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][0], self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][1]],
    #              [self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][0], YCoordOftempRoute1],
    #              [self.getXY('MuxHalf1', 'TristateInv2', 'NMOS', '_Met1Layer')[-1][0] - 1 * UnitPitch, YCoordOftempRoute1]]
    #         ]
    #         self._DesignParameter['Met2Path3']['_XYCoordinates'] = [
    #             [[self.getXY('MuxHalf2', 'Via1_TSINV2_A')[0][0], self.getXYTop('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1] - self.getWidth('Met2Path3') / 2],
    #              [self.getXY('MuxHalf1', 'TristateInv2', 'NMOS', '_Met1Layer')[-1][0] - 1 * UnitPitch, self.getXYTop('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1] - self.getWidth('Met2Path3') / 2]],
    #         ]
    #         self._DesignParameter['Met2Path4']['_XYCoordinates'] = [
    #             [[self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][0], self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][1]],
    #              [self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][0], YCoordOftempRoute2],
    #              [self.getXY('MuxHalf1', 'TristateInv2', 'NMOS', '_Met1Layer')[-1][0] - 2 * UnitPitch, YCoordOftempRoute2]]
    #         ]
    #     else:
    #         YCoordOftempRoute1 = 1066
    #         YCoordOftempRoute2 = 2534
    #         self._DesignParameter['Met2Path1']['_XYCoordinates'] = [
    #             [[self.getXY('MuxHalf1', 'Via1_TSINV2_A')[0][0], self.getXYBot('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1] + self.getWidth('Met2Path1') / 2],
    #              [self.getXY('MuxHalf1', 'TristateInv2', 'NM2', '_Met1Layer')[-1][0] - 2 * UnitPitch, self.getXYBot('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1] + self.getWidth('Met2Path1') / 2]]
    #         ]
    #         self._DesignParameter['Met2Path2']['_XYCoordinates'] = [
    #             [[self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][0], self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][1]],
    #              [self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][0], YCoordOftempRoute1],
    #              [self.getXY('MuxHalf1', 'TristateInv2', 'NM2', '_Met1Layer')[-1][0] - 1 * UnitPitch, YCoordOftempRoute1]]
    #         ]
    #         self._DesignParameter['Met2Path3']['_XYCoordinates'] = [
    #             [[self.getXY('MuxHalf2', 'Via1_TSINV2_A')[0][0], self.getXYTop('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1] - self.getWidth('Met2Path3') / 2],
    #              [self.getXY('MuxHalf1', 'TristateInv2', 'NM2', '_Met1Layer')[-1][0] - 1 * UnitPitch, self.getXYTop('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1] - self.getWidth('Met2Path3') / 2]],
    #         ]
    #         self._DesignParameter['Met2Path4']['_XYCoordinates'] = [
    #             [[self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][0], self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][1]],
    #              [self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][0], YCoordOftempRoute2],
    #              [self.getXY('MuxHalf1', 'TristateInv2', 'NM2', '_Met1Layer')[-1][0] - 2 * UnitPitch, YCoordOftempRoute2]]
    #         ]
    #
    #     # Via2
    #     self._DesignParameter['Via2ForPath1'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2ForPath1In{}'.format(_Name)))[0]
    #     self._DesignParameter['Via2ForPath1']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2)
    #     self._DesignParameter['Via2ForPath2'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2ForPath2In{}'.format(_Name)))[0]
    #     self._DesignParameter['Via2ForPath2']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2)
    #     self._DesignParameter['Via2ForPath3'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2ForPath3In{}'.format(_Name)))[0]
    #     self._DesignParameter['Via2ForPath3']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2)
    #     self._DesignParameter['Via2ForPath4'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2ForPath4In{}'.format(_Name)))[0]
    #     self._DesignParameter['Via2ForPath4']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2)
    #
    #     self._DesignParameter['Via2ForPath1']['_XYCoordinates'] = [
    #         [self._DesignParameter['Met2Path1']['_XYCoordinates'][0][-1][0],
    #          self._DesignParameter['Met2Path1']['_XYCoordinates'][0][-1][1] - self.getWidth('Met2Path1') / 2 + self.getYWidth('Via2ForPath1', '_Met2Layer') / 2]
    #     ]
    #     self._DesignParameter['Via2ForPath2']['_XYCoordinates'] = [
    #         [self._DesignParameter['Met2Path2']['_XYCoordinates'][0][-1][0],
    #          self._DesignParameter['Met2Path2']['_XYCoordinates'][0][-1][1] - self.getWidth('Met2Path2') / 2 + self.getYWidth('Via2ForPath2', '_Met2Layer') / 2]
    #     ]
    #     self._DesignParameter['Via2ForPath3']['_XYCoordinates'] = [
    #         [self._DesignParameter['Met2Path3']['_XYCoordinates'][0][-1][0],
    #          self._DesignParameter['Met2Path3']['_XYCoordinates'][0][-1][1] + self.getWidth('Met2Path3') / 2 - self.getYWidth('Via2ForPath3', '_Met2Layer') / 2]
    #     ]
    #     self._DesignParameter['Via2ForPath4']['_XYCoordinates'] = [
    #         [self._DesignParameter['Met2Path4']['_XYCoordinates'][0][-1][0],
    #          self._DesignParameter['Met2Path4']['_XYCoordinates'][0][-1][1] + self.getWidth('Met2Path4') / 2 - self.getYWidth('Via2ForPath4', '_Met2Layer') / 2]
    #     ]
    #
    #     # Met3
    #     topBoundary = max(self.getXYTop('Via2ForPath3', '_Met3Layer')[0][1], self.getXYTop('Via2ForPath4', '_Met3Layer')[0][1])
    #     botBoundary = min(self.getXYBot('Via2ForPath1', '_Met3Layer')[0][1], self.getXYBot('Via2ForPath2', '_Met3Layer')[0][1])
    #     self._DesignParameter['Met3Boundary5'] = self._BoundaryElementDeclaration(
    #         _Layer=DesignParameters._LayerMapping['METAL3'][0],
    #         _Datatype=DesignParameters._LayerMapping['METAL3'][1],
    #         _XWidth=self.getXWidth('Via2ForPath1', '_Met3Layer'),
    #         _YWidth=topBoundary-botBoundary,
    #         _XYCoordinates=[[self.getXY('Via2ForPath1', '_Met3Layer')[0][0], (topBoundary + botBoundary) / 2]]
    #     )
    #     self._DesignParameter['Met3Boundary6'] = self._BoundaryElementDeclaration(
    #         _Layer=DesignParameters._LayerMapping['METAL3'][0],
    #         _Datatype=DesignParameters._LayerMapping['METAL3'][1],
    #         _XWidth=self.getXWidth('Via2ForPath2', '_Met3Layer'),
    #         _YWidth=topBoundary - botBoundary,
    #         _XYCoordinates=[[self.getXY('Via2ForPath2', '_Met3Layer')[0][0], (topBoundary + botBoundary) / 2]]
    #     )
    #
    #     # Via1
    #     self._DesignParameter['Via1ForPath1'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1ForPath1In{}'.format(_Name)))[0]
    #     self._DesignParameter['Via1ForPath1']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
    #     self._DesignParameter['Via1ForPath1']['_XYCoordinates'] = self.getXY('Via2ForPath1')
    #     self._DesignParameter['Via1ForPath3'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1ForPath3In{}'.format(_Name)))[0]
    #     self._DesignParameter['Via1ForPath3']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
    #     self._DesignParameter['Via1ForPath3']['_XYCoordinates'] = self.getXY('Via2ForPath1')
    #
    #     # met1
    #     rightBoundary = self.getXYRight('Met3Boundary6')[0][0]
    #     leftBoundary = CoordCalc.getXYCoords_MaxX(self.getXY('MuxHalf1', 'Inv1', 'PIN_Y'))[0][0] - self.getWidth('MuxHalf1', 'Inv1', '_OutputRouting') / 2
    #     self._DesignParameter['Met1Boundary7'] = self._BoundaryElementDeclaration(
    #         _Layer=DesignParameters._LayerMapping['METAL1'][0],
    #         _Datatype=DesignParameters._LayerMapping['METAL1'][1],
    #         _XWidth=rightBoundary-leftBoundary,
    #         _YWidth=66
    #     )
    #     self._DesignParameter['Met1Boundary8'] = self._BoundaryElementDeclaration(
    #         _Layer=DesignParameters._LayerMapping['METAL1'][0],
    #         _Datatype=DesignParameters._LayerMapping['METAL1'][1],
    #         _XWidth=self.getXWidth('Met1Boundary7'),
    #         _YWidth=self.getYWidth('Met1Boundary7')
    #     )
    #     self._DesignParameter['Met1Boundary7']['_XYCoordinates'] = [
    #         [(rightBoundary + leftBoundary) / 2, self.getXYTop('Via1ForPath1', '_Met1Layer')[0][1] - self.getYWidth('Met1Boundary7') / 2]
    #     ]
    #     self._DesignParameter['Met1Boundary8']['_XYCoordinates'] = [
    #         [(rightBoundary + leftBoundary) / 2, CellHeight * 2 - self.getXY('Met1Boundary7')[0][1]]
    #     ]
    #
    #     ''' Met3 '''
    #     self._DesignParameter['Met3boundary09'] = self._PathElementDeclaration(
    #         _Layer=DesignParameters._LayerMapping['METAL3'][0],
    #         _Datatype=DesignParameters._LayerMapping['METAL3'][1],
    #         _Width=66
    #     )
    #     self._DesignParameter['Met3boundary10'] = self._PathElementDeclaration(
    #         _Layer=DesignParameters._LayerMapping['METAL3'][0],
    #         _Datatype=DesignParameters._LayerMapping['METAL3'][1],
    #         _Width=self.getWidth('Met3boundary09')
    #     )
    #     self._DesignParameter['Met3boundary09']['_XYCoordinates'] = [
    #         [self.getXYBot('MuxHalf1', 'Via2_temp00', '_Met3Layer')[0],
    #          self.getXYTop('MuxHalf2', 'Via2_temp00', '_Met3Layer')[0]]
    #     ]
    #     self._DesignParameter['Met3boundary10']['_XYCoordinates'] = [
    #         [self.getXYBot('MuxHalf1', 'Via2_temp00', '_Met3Layer')[1],
    #          self.getXYTop('MuxHalf2', 'Via2_temp00', '_Met3Layer')[1]]
    #     ]
    #
    #     self._DesignParameter['Met3boundary11'] = self._PathElementDeclaration(
    #         _Layer=DesignParameters._LayerMapping['METAL3'][0],
    #         _Datatype=DesignParameters._LayerMapping['METAL3'][1],
    #         _Width=self.getWidth('Met3boundary09')
    #     )
    #     self._DesignParameter['Met3boundary12'] = self._PathElementDeclaration(
    #         _Layer=DesignParameters._LayerMapping['METAL3'][0],
    #         _Datatype=DesignParameters._LayerMapping['METAL3'][1],
    #         _Width=self.getWidth('Met3boundary09')
    #     )
    #
    #     self._DesignParameter['Met3boundary09']['_XYCoordinates'] = [
    #         [self.getXYBot('MuxHalf1', 'Via2_temp05', '_Met3Layer')[0],
    #          self.getXYTop('MuxHalf2', 'Via2_temp05', '_Met3Layer')[0]]
    #     ]
    #     self._DesignParameter['Met3boundary10']['_XYCoordinates'] = [
    #         [self.getXYBot('MuxHalf1', 'Via2_temp05', '_Met3Layer')[1],
    #          self.getXYTop('MuxHalf2', 'Via2_temp05', '_Met3Layer')[1]]
    #     ]


if __name__ == '__main__':
    from Private import Myinfo
    import DRCchecker_test2 as DRCchecker
    from generatorLib.IksuPack import PlaygroundBot

    My = Myinfo.USER(DesignParameters._Technology)
    Bot = PlaygroundBot.PGBot(token=My.BotToken, chat_id=My.ChatID)


    libname = 'TEST_MUX4to2'
    cellname = 'MUX4to2'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    # InputParams = dict(
    #     TristateInv1_Finger=3,
    #     TristateInv1_PMOSWidth=400,
    #     TristateInv1_NMOSWidth=250,
    #     TristateInv1_VDD2PMOS=None,  # Optional (Not work when finger >= 3)
    #     TristateInv1_VSS2NMOS=None,  # Optional (Not work when finger >= 3)
    #     TristateInv1_YCoordOfInputA=None,  # Optional
    #     TristateInv1_YCoordOfInputEN=None,  # Optional
    #     TristateInv1_YCoordOfInputENb=None,  # Optional
    #
    #     TristateInv2_Finger=12,
    #     TristateInv2_PMOSWidth=400,
    #     TristateInv2_NMOSWidth=200,
    #     TristateInv2_VDD2PMOS=None,  # Optional (Not work when finger >= 3)
    #     TristateInv2_VSS2NMOS=None,  # Optional (Not work when finger >= 3)
    #     TristateInv2_YCoordOfInputA=None,  # Optional
    #     TristateInv2_YCoordOfInputEN=None,  # Optional
    #     TristateInv2_YCoordOfInputENb=None,  # Optional
    #
    #     Inv_Finger=9,
    #     Inv_PMOSWidth=400,
    #     Inv_NMOSWidth=200,
    #     Inv_VDD2PMOS=None,  # Optional
    #     Inv_VSS2NMOS=None,  # Optional
    #     Inv_YCoordOfInOut=None,  # Optional
    #
    #     ChannelLength=30,
    #     GateSpacing=100,
    #     XVT='SLVT',
    #     CellHeight=None,            #
    #     SupplyRailType=1,
    # )

    # drc check
    InputParams = dict(
        TristateInv1_Finger=11,
        TristateInv1_PMOSWidth=760,
        TristateInv1_NMOSWidth=420,
        TristateInv1_VDD2PMOS=None,  # Optional (Not work when finger >= 3)
        TristateInv1_VSS2NMOS=None,  # Optional (Not work when finger >= 3)
        TristateInv1_YCoordOfInputA=None,  # Optional
        TristateInv1_YCoordOfInputEN=None,  # Optional
        TristateInv1_YCoordOfInputENb=None,  # Optional

        TristateInv2_Finger=1,
        TristateInv2_PMOSWidth=980,
        TristateInv2_NMOSWidth=480,
        TristateInv2_VDD2PMOS=None,  # Optional (Not work when finger >= 3)
        TristateInv2_VSS2NMOS=None,  # Optional (Not work when finger >= 3)
        TristateInv2_YCoordOfInputA=None,  # Optional
        TristateInv2_YCoordOfInputEN=None,  # Optional
        TristateInv2_YCoordOfInputENb=None,  # Optional

        Inv_Finger=10,
        Inv_PMOSWidth=580,
        Inv_NMOSWidth=880,
        Inv_VDD2PMOS=None,  # Optional
        Inv_VSS2NMOS=None,  # Optional
        Inv_YCoordOfInOut=None,  # Optional

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
    Num_DRCCheck = 20

    if Mode_DRCCheck:
        ErrCount = 0            # DRC error
        knownErrorCount = 0     # failed to generate design. NotImplementedError

        start_time = time.time()
        for ii in range(0, Num_DRCCheck):
            # if ii == 0:
            #     Bot.send2Bot(f'Start DRC checker...\nCellName: {cellname}\nTotal # of Run: {Num_DRCCheck}')

            forLoopCntMax = 10
            for iii in range(0, forLoopCntMax):
                try:
                    ''' ------------------------------- Random Parameters for Layout Object -------------------------------- '''
                    InputParams['TristateInv1_Finger'] = DRCchecker.RandomParam(start=1, stop=15, step=1)
                    InputParams['TristateInv2_Finger'] = DRCchecker.RandomParam(start=1, stop=15, step=1)
                    InputParams['Inv_Finger'] = DRCchecker.RandomParam(start=1, stop=15, step=1)

                    InputParams['TristateInv1_PMOSWidth'] = DRCchecker.RandomParam(start=200, stop=1000, step=20)
                    InputParams['TristateInv1_NMOSWidth'] = DRCchecker.RandomParam(start=200, stop=1000, step=20)
                    InputParams['TristateInv2_PMOSWidth'] = DRCchecker.RandomParam(start=200, stop=1000, step=20)
                    InputParams['TristateInv2_NMOSWidth'] = DRCchecker.RandomParam(start=200, stop=1000, step=20)
                    InputParams['Inv_PMOSWidth'] = DRCchecker.RandomParam(start=200, stop=1000, step=20)
                    InputParams['Inv_NMOSWidth'] = DRCchecker.RandomParam(start=200, stop=1000, step=20)

                    print("   Last Layout Object's Input Parameters are   ".center(105, '='))
                    tmpStr = '\n'.join(f'{k} : {v}' for k, v in InputParams.items())
                    print(tmpStr)
                    print("".center(105, '='))

                    ''' ---------------------------------- Generate Layout Object -------------------------------------------'''
                    LayoutObj = MUX_PI_4to2(_Name=cellname)
                    LayoutObj._CalculateDesignParamter_v2(**InputParams)
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
        LayoutObj = MUX_PI_4to2(_Name=cellname)
        LayoutObj._CalculateDesignParamter_v2(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
        testStreamFile = open('./{}'.format(_fileName), 'wb')
        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        print('   Sending to FTP Server & StreamIn...   '.center(105, '#'))
        Checker.Upload2FTP()
        Checker.StreamIn(tech=DesignParameters._Technology)

    print('      Finished       '.center(105, '#'))
