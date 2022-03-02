from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib import CoordinateCalc as CoordCalc
from generatorLib.generator_models import TristateInverter
from generatorLib.generator_models import Inverter_onesemicon
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaMet22Met3
from generatorLib.generator_models import MUX_4to2


class MUX_PI_4to2_FULL(StickDiagram._StickDiagram):
    def __init__(self, _DesignParameter=None, _Name='MUX_PI_4to2_FULL'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name


    def _CalculateDesignParamter(self,
                                 TristateInv1_Finger=1,
                                 TristateInv2_Finger=2,
                                 Inv_Finger=1,

                                 ChannelLength=30,
                                 GateSpacing=100,
                                 # XVT='SLVT',
                                 CellHeight=1800,
                                 SupplyRailType=1,

                                 ):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        UnitPitch = ChannelLength + GateSpacing


        Parameters = dict(TristateInv1_Finger=TristateInv1_Finger,
                          Inv_Finger=Inv_Finger,
                         TristateInv2_Finger=TristateInv2_Finger,


                         ChannelLength=ChannelLength,
                         GateSpacing=GateSpacing,
                         CellHeight=CellHeight,
                         SupplyRailType=SupplyRailType,)

        self._DesignParameter['MUX_FULL1'] = self._SrefElementDeclaration(
            _DesignObj=MUX_4to2.MUX_PI_4to2(_Name='MUX_FULL1In{}'.format(_Name)))[0]
        self._DesignParameter['MUX_FULL1']['_DesignObj']._CalculateDesignParamter(**Parameters)
        self._DesignParameter['MUX_FULL1']['_XYCoordinates'] = [[0,0]]

        self._DesignParameter['MUX_FULL2'] = self._SrefElementDeclaration(
            _Reflect=[1, 0, 0], _Angle=0,
            _DesignObj=MUX_4to2.MUX_PI_4to2(_Name='MUX_FULL2In{}'.format(_Name)))[0]
        self._DesignParameter['MUX_FULL2']['_DesignObj']._CalculateDesignParamter(**Parameters)
        self._DesignParameter['MUX_FULL2']['_XYCoordinates'] = [[0, 2*CellHeight]]


        # if TristateInv2_Finger == 2:
        #     pass
        # elif TristateInv2_Finger == 1:
        #     self._DesignParameter['path_1'] = self._PathElementDeclaration(
        #         _Layer=DesignParameters._LayerMapping['METAL2'][0],
        #         _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        #         _Width=66
        #     )
        #     YCoordOftempRoute = 1033
        #     self._DesignParameter['path_1']['_XYCoordinates'] = [
        #         [[self.getXY('MUX_FULL1', 'Via1_TSINV2_A')[0][0], self.getXY('MUX_FULL1', 'Via1_TSINV2_A')[0][1]],
        #          [self.getXY('MUX_FULL1', 'Via1_TSINV2_A')[0][0] - 2*UnitPitch, self.getXY('MUX_FULL1', 'Via1_TSINV2_A')[0][1]]],
        #         [[self.getXY('MUX_FULL1', 'Via1_TSINV3_A')[0][0], self.getXY('MUX_FULL1', 'Via1_TSINV3_A')[0][1]],
        #          [self.getXY('MUX_FULL1', 'Via1_TSINV3_A')[0][0], YCoordOftempRoute],
        #          [self.getXY('MUX_FULL1', 'Via1_TSINV2_A')[0][0] - UnitPitch, YCoordOftempRoute]],
        #         [[self.getXY('MUX_FULL2', 'Via1_TSINV2_A')[0][0], self.getXY('MUX_FULL2', 'Via1_TSINV2_A')[0][1]],
        #           [self.getXY('MUX_FULL2', 'Via1_TSINV2_A')[0][0] - UnitPitch, self.getXY('MUX_FULL2', 'Via1_TSINV2_A')[0][1]]],
        #         [[self.getXY('MUX_FULL2', 'Via1_TSINV3_A')[0][0], self.getXY('MUX_FULL2', 'Via1_TSINV3_A')[0][1]],
        #          [self.getXY('MUX_FULL2', 'Via1_TSINV3_A')[0][0], 2*CellHeight - YCoordOftempRoute],
        #          [self.getXY('MUX_FULL2', 'Via1_TSINV2_A')[0][0] - 2*UnitPitch, 2*CellHeight - YCoordOftempRoute]]
        #     ]

