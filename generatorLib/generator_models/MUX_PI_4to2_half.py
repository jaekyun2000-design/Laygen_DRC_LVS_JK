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


class MUX_PI_4to2_half(StickDiagram._StickDiagram):
    def __init__(self, _DesignParameter=None, _Name='MUX_PI_4to2_half'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name


    def _CalculateDesignParamter(self,
                                 TristateInv1_Finger=1,
                                 Inv_Finger=1,
                                 TristateInv2_Finger=2,

                                 TristateInv1_PMOSWidth=500,
                                 TristateInv1_NMOSWidth=250,
                                 TristateInv1_VDD2PMOS=400,
                                 TristateInv1_VSS2NMOS=275,

                                 TristateInv2_PMOSWidth=400,
                                 TristateInv2_NMOSWidth=200,
                                 TristateInv2_VDD2PMOS=410,
                                 TristateInv2_VSS2NMOS=310,

                                 TristateInv3_NumFinger_NM1=3,
                                 TristateInv3_NumFinger_NM2=3,
                                 TristateInv3_Width_NM1=250,
                                 TristateInv3_Width_NM2=250,
                                 TristateInv3_Width_PM1=500,
                                 TristateInv3_Width_PM2=500,
                                 TristateInv3_YCoord_InputA=750,

                                 Inv_NMOSWidth=200,
                                 Inv_PMOSWidth=400,

                                 ChannelLength=30,
                                 GateSpacing=100,
                                 XVT='SLVT',
                                 CellHeight=1800,
                                 SupplyRailType=1,

                                 ):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        UnitPitch = ChannelLength + GateSpacing

        Parameters1_TristateInv = dict(
            NMOSWidth=TristateInv1_NMOSWidth,
            PMOSWidth=TristateInv1_PMOSWidth,
            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            XVT=XVT,
            CellHeight=CellHeight,
            VDD2PMOS=TristateInv1_VDD2PMOS,
            VSS2NMOS=TristateInv1_VSS2NMOS,
            SupplyRailType=SupplyRailType
        )
        Parameters3_TristateInvF2 = dict(
            NMOSWidth=TristateInv2_NMOSWidth,
            PMOSWidth=TristateInv2_PMOSWidth,
            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            XVT=XVT,
            CellHeight=CellHeight,
            VDD2PMOS=TristateInv2_VDD2PMOS,
            VSS2NMOS=TristateInv2_VSS2NMOS,
            SupplyRailType=SupplyRailType
        )
        Parameters3_TristateInvF3 = dict(
            NumFinger_NM1=TristateInv3_NumFinger_NM1,
            NumFinger_NM2=TristateInv3_NumFinger_NM2,
            Width_NM1=TristateInv3_Width_NM1,
            Width_NM2=TristateInv3_Width_NM2,
            Width_PM1=TristateInv3_Width_PM1,
            Width_PM2=TristateInv3_Width_PM2,

            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            XVT=XVT,

            CellHeight=CellHeight,  # Required
            YCoord_InputA=TristateInv3_YCoord_InputA,      # Option
            YCoord_InputEN=None,    # Option
            YCoord_InputENb=None    # Option
        )

        Parameters2_Inv = dict(
            _Finger=Inv_Finger,
            _ChannelWidth=Inv_NMOSWidth,
            _ChannelLength=ChannelLength,
            _NPRatio=Inv_PMOSWidth/Inv_NMOSWidth,

            _VDD2VSSHeight=CellHeight,
            _VDD2PMOSHeight=None,
            _VSS2NMOSHeight=None,
            _YCoordOfInput=None,

            _Dummy=True,
            _XVT=XVT,
            _GateSpacing=GateSpacing,
            _SDWidth=66,

            _SupplyRailType=SupplyRailType,
        )


        ''' ------------------------------------------ Tristate Inverter ------------------------------------------- '''
        if TristateInv1_Finger == 1:
            self._DesignParameter['TristateInv0'] = self._SrefElementDeclaration(
                _Reflect=[1,0,0], _Angle=180,
                _DesignObj=TristateInverter.TristateInverter(_Name='TristateInv0In{}'.format(_Name)))[0]
            self._DesignParameter['TristateInv0']['_DesignObj']._CalculateDesignParameterFinger1(**Parameters1_TristateInv)
            self._DesignParameter['TristateInv0']['_XYCoordinates'] = [
                [self._DesignParameter['TristateInv0']['_DesignObj'].CellXWidth / 2, 0]
            ]
            self._DesignParameter['TristateInv1'] = self._SrefElementDeclaration(
                _Reflect=[0,0,0], _Angle=0,
                _DesignObj=TristateInverter.TristateInverter(_Name='TristateInv1In{}'.format(_Name)))[0]
            self._DesignParameter['TristateInv1']['_DesignObj']._CalculateDesignParameterFinger1(**Parameters1_TristateInv)
            self._DesignParameter['TristateInv1']['_XYCoordinates'] = [
                [self._DesignParameter['TristateInv0']['_DesignObj'].CellXWidth * 3 / 2 + 2 * UnitPitch, 0]
            ]

            #
            RightBoundary_Met1Route_net011 = self.getXY('TristateInv1', 'PMOS')[0][0]
            LeftBoundary_Met1Route_net011 = self.getXY('TristateInv0', 'PMOS')[0][0]
            self._DesignParameter['Met1Route_net011'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=RightBoundary_Met1Route_net011-LeftBoundary_Met1Route_net011,
                _YWidth=self.getWidth('TristateInv0', 'OutputRouting')
            )

            self._DesignParameter['Met1Route_net011']['_XYCoordinates'] = [
                [(RightBoundary_Met1Route_net011 + LeftBoundary_Met1Route_net011) / 2,
                 self.getXY('TristateInv0', 'PMOS', '_Met1Layer')[0][1] - self.getYWidth('TristateInv0', 'PMOS', '_Met1Layer') / 2 + self.getYWidth('Met1Route_net011') / 2]
            ]

            # leftdown to rightup
            self._DesignParameter['Met1Route_temp1'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _Width=66
            )
            self._DesignParameter['Met1Route_temp1']['_XYCoordinates'] = [[
                [int(self.getXY('TristateInv0', 'InputVia_EN', '_Met1Layer')[0][0] + 0*UnitPitch), int(self.getXY('TristateInv0', 'InputVia_EN', '_Met1Layer')[0][1])],
                [int(self.getXY('TristateInv0', 'InputVia_EN', '_Met1Layer')[0][0] + 2*UnitPitch), int(self.getXY('TristateInv0', 'InputVia_EN', '_Met1Layer')[0][1])],
                [int(self.getXY('TristateInv0', 'InputVia_EN', '_Met1Layer')[0][0] + 2*UnitPitch), int(self.getXY('TristateInv1', 'InputVia_ENb', '_Met1Layer')[0][1] - self.getYWidth('TristateInv1', 'InputVia_ENb', '_Met1Layer') / 2 + self.getWidth('Met1Route_temp1')/2)],
                [int(self.getXY('TristateInv1', 'InputVia_ENb', '_Met1Layer')[0][0]), int(self.getXY('TristateInv1', 'InputVia_ENb', '_Met1Layer')[0][1] - self.getYWidth('TristateInv1', 'InputVia_ENb', '_Met1Layer') / 2 + self.getWidth('Met1Route_temp1')/2)]
            ]]
            self._DesignParameter['Met1Route_temp2'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _Width=66
            )
            self._DesignParameter['Met1Route_temp2']['_XYCoordinates'] = [[
                [int(self.getXY('TristateInv0', 'InputVia_ENb', '_Met1Layer')[0][0] + 0*UnitPitch), int(self.getXY('TristateInv0', 'InputVia_ENb', '_Met1Layer')[0][1] - self.getYWidth('TristateInv0', 'InputVia_ENb', '_Met1Layer')/2 + 33)],
                [int(self.getXY('TristateInv0', 'InputVia_ENb', '_Met1Layer')[0][0] + 1*UnitPitch), int(self.getXY('TristateInv0', 'InputVia_ENb', '_Met1Layer')[0][1] - self.getYWidth('TristateInv0', 'InputVia_ENb', '_Met1Layer')/2 + 33)]
            ]]

            self._DesignParameter['Via1_temp3'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1temp3In{}'.format(_Name)))[0]
            self._DesignParameter['Via1_temp3']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2
            )
            self._DesignParameter['Via1_temp3']['_XYCoordinates'] = [
                [int(self.getXY('TristateInv0', 'InputVia_ENb', '_Met1Layer')[0][0] + 1*UnitPitch), int(self.getXY('TristateInv0', 'InputVia_ENb', '_Met1Layer')[0][1]) + 33 - self.getYWidth('Via1_temp3', '_Met1Layer') / 2 - self.getYWidth('TristateInv0', 'InputVia_ENb', '_Met1Layer')/2 + 33]
            ]

            self._DesignParameter['Met2Route_temp4'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                _Width=66
            )
            self._DesignParameter['Met2Route_temp4']['_XYCoordinates'] = [[
                [self.getXY('Via1_temp3')[0][0], self.getXY('Via1_temp3')[0][1]],
                [self.getXY('Via1_temp3')[0][0], self.getXY('TristateInv1', 'InputVia_EN')[0][1]],
                [self.getXY('TristateInv1', 'InputVia_EN')[0][0], self.getXY('TristateInv1', 'InputVia_EN')[0][1]],
            ]]

            self._DesignParameter['Via1_temp5'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1temp5In{}'.format(_Name)))[0]
            self._DesignParameter['Via1_temp5']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2
            )
            self._DesignParameter['Via1_temp5']['_XYCoordinates'] = self.getXY('TristateInv1', 'InputVia_EN')


            # #
            self._DesignParameter['Via2_temp00'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2temp00In{}'.format(_Name)))[0]
            self._DesignParameter['Via2_temp00']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2
            )
            self._DesignParameter['Via2_temp00']['_XYCoordinates'] = [
                [self.getXY('TristateInv0', 'InputVia_EN')[0][0], self.getXY('TristateInv0', 'InputVia_EN')[0][1]],
                [self.getXY('TristateInv1', 'InputVia_EN')[0][0], self.getXY('TristateInv1', 'InputVia_EN')[0][1]],
            ]
            self._DesignParameter['Met3Route_temp01'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL3'][0],
                _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                _Width=66
            )
            self._DesignParameter['Met3Route_temp01']['_XYCoordinates'] = [
                [[self.getXY('Via2_temp00')[0][0], self.getXY('Via2_temp00')[0][1]],
                 [self.getXY('Via2_temp00')[0][0], CellHeight]],
                [[self.getXY('Via2_temp00')[1][0], self.getXY('Via2_temp00')[1][1]],
                 [self.getXY('Via2_temp00')[1][0], CellHeight]]
            ]


        elif TristateInv1_Finger == 2:
            self._DesignParameter['TristateInv0'] = self._SrefElementDeclaration(
                _Reflect=[1, 0, 0], _Angle=180,
                _DesignObj=TristateInverter.TristateInverter(_Name='TristateInv0In{}'.format(_Name)))[0]
            self._DesignParameter['TristateInv0']['_DesignObj']._CalculateDesignParameterFinger2(**Parameters3_TristateInvF2)
            self._DesignParameter['TristateInv0']['_XYCoordinates'] = [
                [self._DesignParameter['TristateInv0']['_DesignObj'].CellXWidth / 2, 0]
            ]
            self._DesignParameter['TristateInv1'] = self._SrefElementDeclaration(
                _Reflect=[0, 0, 0], _Angle=0,
                _DesignObj=TristateInverter.TristateInverter(_Name='TristateInv1In{}'.format(_Name)))[0]
            self._DesignParameter['TristateInv1']['_DesignObj']._CalculateDesignParameterFinger2(**Parameters3_TristateInvF2)
            self._DesignParameter['TristateInv1']['_XYCoordinates'] = [
                [self.getXY('TristateInv0')[0][0] + self._DesignParameter['TristateInv0']['_DesignObj'].CellXWidth / 2 + 2 * UnitPitch + self._DesignParameter['TristateInv1']['_DesignObj'].CellXWidth / 2, 0]
            ]

            # output node connection
            RightBoundary_Met1Route_net011 = self.getXY('TristateInv1', 'met1_output_4')[0][0] + self.getXWidth('TristateInv1', 'met1_output_4') / 2
            LeftBoundary_Met1Route_net011 = self.getXY('TristateInv0', 'met1_output_4')[0][0] - self.getXWidth('TristateInv0', 'met1_output_4') / 2
            self._DesignParameter['Met1Route_net011'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=RightBoundary_Met1Route_net011 - LeftBoundary_Met1Route_net011,
                _YWidth=self.getYWidth('TristateInv0', 'met1_output_3')
            )

            self._DesignParameter['Met1Route_net011']['_XYCoordinates'] = [
                [(RightBoundary_Met1Route_net011 + LeftBoundary_Met1Route_net011) / 2,
                 self.getXY('TristateInv0', 'met1_output_3')[0][1]]
            ]

            # leftdown to rightup
            self._DesignParameter['Met1Route_temp021'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _Width=66
            )
            self._DesignParameter['Met1Route_temp021']['_XYCoordinates'] = [[
                [self.getXY('TristateInv0', 'InputVia_EN', '_Met1Layer')[0][0], self.getXY('TristateInv0', 'InputVia_EN', '_Met1Layer')[0][1]],
                [(self.getXY('TristateInv1', 'NMOS', '_Met1Layer')[0][0] - UnitPitch), self.getXY('TristateInv0', 'InputVia_EN', '_Met1Layer')[0][1]],
                [(self.getXY('TristateInv1', 'NMOS', '_Met1Layer')[0][0] - UnitPitch), self.getXY('TristateInv1', 'InputVia_ENb', '_Met1Layer')[0][1]],
                [self.getXY('TristateInv1', 'InputVia_ENb', '_Met1Layer')[0][0], self.getXY('TristateInv1', 'InputVia_ENb', '_Met1Layer')[0][1]]
            ]]
            self._DesignParameter['Met1Route_temp022'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _Width=66
            )
            self._DesignParameter['Met1Route_temp022']['_XYCoordinates'] = [[
                [self.getXY('TristateInv0', 'InputVia_ENb', '_Met1Layer')[0][0], self.getXY('TristateInv0', 'InputVia_ENb', '_Met1Layer')[0][1]],
                [self.getXY('TristateInv0', 'NMOS', '_Met1Layer')[0][0] + UnitPitch, self.getXY('TristateInv0', 'InputVia_ENb', '_Met1Layer')[0][1]],
                [self.getXY('TristateInv0', 'NMOS', '_Met1Layer')[0][0] + UnitPitch, self.getXY('TristateInv0', 'InputVia_A', '_Met1Layer')[0][1]]
            ]]

            self._DesignParameter['Via1_temp023'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1temp023In{}'.format(_Name)))[0]
            self._DesignParameter['Via1_temp023']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2
            )
            self._DesignParameter['Via1_temp023']['_XYCoordinates'] = [
                [self.getXY('TristateInv0', 'NMOS', '_Met1Layer')[0][0] + UnitPitch, self.getXY('TristateInv0', 'InputVia_A', '_Met1Layer')[0][1]]
            ]

            self._DesignParameter['Met2Route_temp024'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                _Width=66
            )
            self._DesignParameter['Met2Route_temp024']['_XYCoordinates'] = [[
                [self.getXY('Via1_temp023')[0][0], self.getXY('Via1_temp023')[0][1]],
                [self.getXY('Via1_temp023')[0][0], self.getXY('TristateInv1', 'InputVia_EN')[0][1]],
                [self.getXY('TristateInv1', 'InputVia_EN')[0][0], self.getXY('TristateInv1', 'InputVia_EN')[0][1]]
            ]]
            #
            self._DesignParameter['Via1_temp026'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1temp026In{}'.format(_Name)))[0]
            self._DesignParameter['Via1_temp026']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1
            )
            self._DesignParameter['Via1_temp026']['_XYCoordinates'] = self.getXY('TristateInv0', 'InputVia_EN')
            self._DesignParameter['TristateInv0']['_DesignObj']._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self.getYWidth('Via1_temp026', '_Met1Layer')
            self._DesignParameter['TristateInv0']['_DesignObj']._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self.getYWidth('Via1_temp026', '_Met1Layer')
            self._DesignParameter['TristateInv1']['_DesignObj']._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self.getYWidth('Via1_temp026', '_Met1Layer')
            self._DesignParameter['TristateInv1']['_DesignObj']._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self.getYWidth('Via1_temp026', '_Met1Layer')


            self._DesignParameter['Via2_temp024'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2temp024In{}'.format(_Name)))[0]
            self._DesignParameter['Via2_temp024']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=1
            )
            self._DesignParameter['Via2_temp024']['_XYCoordinates'] = self.getXY('TristateInv0', 'InputVia_EN')

            self._DesignParameter['Via2_temp025'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2temp025In{}'.format(_Name)))[0]
            self._DesignParameter['Via2_temp025']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=1
            )
            self._DesignParameter['Via2_temp025']['_XYCoordinates'] = self.getXY('TristateInv1', 'InputVia_EN')

            # #
            self._DesignParameter['Via2_temp00'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2temp00In{}'.format(_Name)))[0]
            self._DesignParameter['Via2_temp00']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=1
            )
            self._DesignParameter['Via2_temp00']['_XYCoordinates'] = [
                [self.getXY('TristateInv0', 'InputVia_EN')[0][0], self.getXY('TristateInv0', 'InputVia_EN')[0][1]],
                [self.getXY('TristateInv1', 'InputVia_EN')[0][0], self.getXY('TristateInv1', 'InputVia_EN')[0][1]],
            ]
            self._DesignParameter['Met3Route_temp01'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL3'][0],
                _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                _Width=66
            )
            self._DesignParameter['Met3Route_temp01']['_XYCoordinates'] = [
                [[self.getXY('Via2_temp00')[0][0], self.getXY('Via2_temp00')[0][1]],
                 [self.getXY('Via2_temp00')[0][0], CellHeight]],
                [[self.getXY('Via2_temp00')[1][0], self.getXY('Via2_temp00')[1][1]],
                 [self.getXY('Via2_temp00')[1][0], CellHeight]]
            ]
        else:
            self._DesignParameter['TristateInv0'] = self._SrefElementDeclaration(
                _Reflect=[1, 0, 0], _Angle=180,
                _DesignObj=TristateInverter.TristateInverter(_Name='TristateInv0In{}'.format(_Name)))[0]
            self._DesignParameter['TristateInv0']['_DesignObj']._CalculateDesignParameterFinger3orMore_v2(
                **Parameters3_TristateInvF3)
            self._DesignParameter['TristateInv0']['_XYCoordinates'] = [
                [self._DesignParameter['TristateInv0']['_DesignObj'].CellXWidth / 2, 0]
            ]
            self._DesignParameter['TristateInv1'] = self._SrefElementDeclaration(
                _Reflect=[0, 0, 0], _Angle=0,
                _DesignObj=TristateInverter.TristateInverter(_Name='TristateInv1In{}'.format(_Name)))[0]
            self._DesignParameter['TristateInv1']['_DesignObj']._CalculateDesignParameterFinger3orMore_v2(
                **Parameters3_TristateInvF3)
            self._DesignParameter['TristateInv1']['_XYCoordinates'] = [
                [self.getXY('TristateInv0')[0][0] + self._DesignParameter['TristateInv0']['_DesignObj'].CellXWidth / 2 + 2 * UnitPitch + self._DesignParameter['TristateInv1']['_DesignObj'].CellXWidth / 2, 0]
            ]

            # output node connection
            RightBoundary_Met1Route_net011 = self.getXY('TristateInv1', 'Met1RouteX_PMOut')[0][0] + self.getXWidth(
                'TristateInv1', 'Met1RouteX_PMOut') / 2
            LeftBoundary_Met1Route_net011 = self.getXY('TristateInv0', 'Met1RouteX_PMOut')[0][0] - self.getXWidth(
                'TristateInv0', 'Met1RouteX_PMOut') / 2
            self._DesignParameter['Met1Route_net011'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=RightBoundary_Met1Route_net011 - LeftBoundary_Met1Route_net011,
                _YWidth=self.getYWidth('TristateInv0', 'Met1RouteX_PMOut')
            )

            self._DesignParameter['Met1Route_net011']['_XYCoordinates'] = [
                [(RightBoundary_Met1Route_net011 + LeftBoundary_Met1Route_net011) / 2,
                 self.getXY('TristateInv0', 'Met1RouteX_PMOut')[0][1]]
            ]

            # leftdown to rightup
            self._DesignParameter['Met1Route_temp021'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _Width=66
            )
            self._DesignParameter['Met1Route_temp021']['_XYCoordinates'] = [[
                [self.getXY('TristateInv0')[0][0] -
                 self._DesignParameter['TristateInv0']['_DesignObj']._DesignParameter['polyInputEN']['_XYCoordinates'][
                     0][0],
                 self.getXY('TristateInv0', 'polyInputEN', '_Met1Layer')[0][1]],
                [(self.getXY('TristateInv1', 'NM1', '_Met1Layer')[0][0] - UnitPitch),
                 self.getXY('TristateInv0', 'polyInputEN', '_Met1Layer')[0][1]],
                [(self.getXY('TristateInv1', 'NM1', '_Met1Layer')[0][0] - UnitPitch),
                 self.getXY('TristateInv1', 'polyInputENb', '_Met1Layer')[0][1]],
                [self.getXY('TristateInv1', 'polyInputENb', '_Met1Layer')[0][0],
                 self.getXY('TristateInv1', 'polyInputENb', '_Met1Layer')[0][1]]
            ]]
            self._DesignParameter['Met1Route_temp022'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _Width=66
            )
            self._DesignParameter['Met1Route_temp022']['_XYCoordinates'] = [[
                [self.getXY('TristateInv0')[0][0] - self._DesignParameter['TristateInv0']['_DesignObj']._DesignParameter['polyInputENb']['_XYCoordinates'][0][0],
                 self.getXY('TristateInv0', 'polyInputENb', '_Met1Layer')[0][1]],
                [self.getXY('TristateInv0', 'NM1', '_Met1Layer')[0][0] + UnitPitch,
                 self.getXY('TristateInv0', 'polyInputENb', '_Met1Layer')[0][1]],
                [self.getXY('TristateInv0', 'NM1', '_Met1Layer')[0][0] + UnitPitch,
                 self.getXY('TristateInv0', 'polyInputA', '_Met1Layer')[0][1]]
            ]]

            self._DesignParameter['Via1_temp023'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1temp023In{}'.format(_Name)))[0]
            self._DesignParameter['Via1_temp023']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2
            )
            self._DesignParameter['Via1_temp023']['_XYCoordinates'] = [
                [self.getXY('TristateInv0', 'NM1', '_Met1Layer')[0][0] + UnitPitch,
                 self.getXY('TristateInv0', 'polyInputA', '_Met1Layer')[0][1]]
            ]

            self._DesignParameter['Met2Route_temp024'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                _Width=66
            )
            self._DesignParameter['Met2Route_temp024']['_XYCoordinates'] = [[
                [self.getXY('Via1_temp023')[0][0], self.getXY('Via1_temp023')[0][1]],
                [self.getXY('Via1_temp023')[0][0], self.getXY('TristateInv1', 'polyInputEN')[0][1]],
                [self.getXY('TristateInv1', 'polyInputEN')[0][0], self.getXY('TristateInv1', 'polyInputEN')[0][1]]
            ]]

            self._DesignParameter['Via1_temp026'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1temp026In{}'.format(_Name)))[0]
            self._DesignParameter['Via1_temp026']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1
            )
            self._DesignParameter['Via1_temp026']['_XYCoordinates'] = [[
                self.getXY('TristateInv0')[0][0] -
                self._DesignParameter['TristateInv0']['_DesignObj']._DesignParameter['polyInputEN']['_XYCoordinates'][
                    0][0],
                self.getXY('TristateInv0')[0][1] +
                self._DesignParameter['TristateInv0']['_DesignObj']._DesignParameter['polyInputEN']['_XYCoordinates'][
                    0][1]
            ]]

            self._DesignParameter['Via2_temp024'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2temp024In{}'.format(_Name)))[0]
            self._DesignParameter['Via2_temp024']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=1
            )
            self._DesignParameter['Via2_temp024']['_XYCoordinates'] = [[
                self.getXY('TristateInv0')[0][0] -
                self._DesignParameter['TristateInv0']['_DesignObj']._DesignParameter['polyInputEN']['_XYCoordinates'][
                    0][0],
                self.getXY('TristateInv0')[0][1] +
                self._DesignParameter['TristateInv0']['_DesignObj']._DesignParameter['polyInputEN']['_XYCoordinates'][
                    0][1]
            ]]
            self._DesignParameter['Via2_temp025'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2temp025In{}'.format(_Name)))[0]
            self._DesignParameter['Via2_temp025']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=1
            )
            self._DesignParameter['Via2_temp025']['_XYCoordinates'] = self.getXY('TristateInv1', 'polyInputEN')

            # #
            self._DesignParameter['Via2_temp00'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2temp00In{}'.format(_Name)))[0]
            self._DesignParameter['Via2_temp00']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=1
            )
            self._DesignParameter['Via2_temp00']['_XYCoordinates'] = [
                [self.getXY('TristateInv0')[0][0] - self._DesignParameter['TristateInv0']['_DesignObj']._DesignParameter['polyInputEN']['_XYCoordinates'][0][0], self.getXY('TristateInv0', 'polyInputEN')[0][1]],
                [self.getXY('TristateInv1', 'polyInputEN')[0][0], self.getXY('TristateInv1', 'polyInputEN')[0][1]],
            ]
            self._DesignParameter['Met3Route_temp01'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL3'][0],
                _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                _Width=66
            )
            self._DesignParameter['Met3Route_temp01']['_XYCoordinates'] = [
                [[self.getXY('Via2_temp00')[0][0], self.getXY('Via2_temp00')[0][1]],
                 [self.getXY('Via2_temp00')[0][0], CellHeight]],
                [[self.getXY('Via2_temp00')[1][0], self.getXY('Via2_temp00')[1][1]],
                 [self.getXY('Via2_temp00')[1][0], CellHeight]]
            ]

        # end of ...

        if TristateInv1_Finger in (1,2):
            tempword = 'InputVia_A'
            tempCOX = 1
            tempCOY = 2
        else:
            tempword = 'polyInputA'
            tempCOX = 2
            tempCOY = 1

        ''' Input '''
        self._DesignParameter['Via1_temp6'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1temp6In{}'.format(_Name)))[0]
        self._DesignParameter['Via1_temp6']['_DesignObj']._CalculateDesignParameterSameEnclosure(
            _ViaMet12Met2NumberOfCOX=tempCOX, _ViaMet12Met2NumberOfCOY=tempCOY
        )
        self._DesignParameter['Via1_temp6']['_XYCoordinates'] = [
            [self.getXY('TristateInv0')[0][0] - self._DesignParameter['TristateInv0']['_DesignObj']._DesignParameter[tempword]['_XYCoordinates'][0][0],
             self.getXY('TristateInv0', tempword)[0][1]]
        ]

        self._DesignParameter['Via1_temp7'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1temp7In{}'.format(_Name)))[0]
        self._DesignParameter['Via1_temp7']['_DesignObj']._CalculateDesignParameterSameEnclosure(
            _ViaMet12Met2NumberOfCOX=tempCOX, _ViaMet12Met2NumberOfCOY=tempCOY
        )
        self._DesignParameter['Via1_temp7']['_XYCoordinates'] = self.getXY('TristateInv1', tempword)

        self._DesignParameter['Met2Route_temp8'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _Width=66
        )
        YCoordOfIN1 = 1033
        self._DesignParameter['Met2Route_temp8']['_XYCoordinates'] = [
            [[self.getXY('Via1_temp6')[0][0], self.getXY('Via1_temp6')[0][1] + self.getYWidth('Via1_temp6', '_Met2Layer') / 2 - 33],
             [0, self.getXY('Via1_temp6')[0][1] + self.getYWidth('Via1_temp6', '_Met2Layer') / 2 - 33]],
            [[self.getXY('Via1_temp7')[0][0], self.getXY('Via1_temp7')[0][1]],
             [self.getXY('Via1_temp7')[0][0], YCoordOfIN1],
             [0, YCoordOfIN1]]
        ]



        ''' ----------------------------------------------- Inverter ----------------------------------------------- '''
        self._DesignParameter['Inv0'] = self._SrefElementDeclaration(
            _DesignObj=Inverter_onesemicon._Inverter(_Name='Inv0In{}'.format(_Name)))[0]
        self._DesignParameter['Inv0']['_DesignObj']._CalculateDesignParameter_v3(**Parameters2_Inv)
        self._DesignParameter['Inv0']['_XYCoordinates'] = [
            [self.getXY('TristateInv1')[0][0] + self._DesignParameter['TristateInv1']['_DesignObj'].CellXWidth / 2 + self._DesignParameter['Inv0']['_DesignObj'].CellXWidth / 2, 0]
        ]
        self._DesignParameter['Inv1'] = self._SrefElementDeclaration(
            _DesignObj=Inverter_onesemicon._Inverter(_Name='Inv1In{}'.format(_Name)))[0]
        self._DesignParameter['Inv1']['_DesignObj']._CalculateDesignParameter_v3(**Parameters2_Inv)
        self._DesignParameter['Inv1']['_XYCoordinates'] = [
            [self.getXY('Inv0')[0][0] + self._DesignParameter['Inv0']['_DesignObj'].CellXWidth / 2 + self._DesignParameter['Inv1']['_DesignObj'].CellXWidth / 2, 0]
        ]

        # Input Via1 For Inverters -> Finger 많을 때 이미 Via1이 존재할 수도 있음... 추후 수정
        NumViaX, NumViaY = ViaMet12Met2._ViaMet12Met2.CalcNumViaSameEnclosure(
            XWidth=self.getXWidth('Inv0', 'InputMet1'),
            YWidth=self.getYWidth('Inv0', 'InputMet1')
        )
        if NumViaX > 2:
            NumViaX = 2
        if NumViaY > 2:
            NumViaY = 2
        assert NumViaX * NumViaY >= 2, 'Inverter Input Via(M1V1M2) 개수가 적음.'

        self._DesignParameter['Via1ForInv'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1ForInvIn{}'.format(_Name)))[0]
        self._DesignParameter['Via1ForInv']['_DesignObj']._CalculateDesignParameterSameEnclosure(
            _ViaMet12Met2NumberOfCOX=NumViaX, _ViaMet12Met2NumberOfCOY=NumViaY
        )
        self._DesignParameter['Via1ForInv']['_XYCoordinates'] = [
            self.getXY('Inv0', 'InputMet1')[0],
            self.getXY('Inv1', 'InputMet1')[0]
        ]
        self._DesignParameter['Met2ForInverterInput'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=(self.getXY('Via1ForInv', '_Met2Layer')[1][0] - self.getXY('Via1ForInv', '_Met2Layer')[0][0]) + self.getXWidth('Via1ForInv', '_Met2Layer'),
            _YWidth=66
        )
        self._DesignParameter['Met2ForInverterInput']['_XYCoordinates'] = [
            [(self.getXY('Via1ForInv', '_Met2Layer')[1][0] + self.getXY('Via1ForInv', '_Met2Layer')[0][0]) / 2,
             self.getXY('Via1ForInv', '_Met2Layer')[0][1]]
        ]

        # Metal1 from TristateInverters' Output to Inverter's Input
        self._DesignParameter['Met1From3SInvtoInv'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _Width=66
        )

        if TristateInv1_Finger == 1:
            TopBoundary1ForUpperRoute_3SInvMet1 = self.getXY('TristateInv1', 'PMOS', '_Met1Layer')[0][1] - self.getYWidth('TristateInv1', 'PMOS', '_Met1Layer') / 2
            TopBoundary2ForUpperRoute_InvMet1 = self.getXY('Inv1', '_PMOS', '_Met1Layer')[0][1] - self.getYWidth('Inv1', '_PMOS', '_Met1Layer') / 2
            TopBoundaryForUpperRoute = min(TopBoundary1ForUpperRoute_3SInvMet1, TopBoundary2ForUpperRoute_InvMet1)
            BotBoundaryForUpperRoute = self.getXY('TristateInv1', 'InputVia_A', '_Met1Layer')[0][1] + self.getYWidth('TristateInv1', 'InputVia_A', '_Met1Layer') / 2
            GapForUpperRoute = TopBoundaryForUpperRoute - BotBoundaryForUpperRoute

            BotBoundary1ForLowerRoute_3SInvMet1 = self.getXY('TristateInv1', 'NMOS', '_Met1Layer')[0][1] + self.getYWidth('TristateInv1', 'NMOS', '_Met1Layer') / 2
            BotBoundary2ForLowerRoute_InvMet1 = self.getXY('Inv1', '_NMOS', '_Met1Layer')[0][1] + self.getYWidth('Inv1', '_NMOS', '_Met1Layer') / 2
            BotBoundaryForLowerRoute = min(BotBoundary1ForLowerRoute_3SInvMet1, BotBoundary2ForLowerRoute_InvMet1)
            TopBoundaryForLowerRoute = self.getXY('TristateInv1', 'InputVia_A', '_Met1Layer')[0][1] - self.getYWidth('TristateInv1', 'InputVia_A', '_Met1Layer') / 2
            GapForLowerRoute = TopBoundaryForLowerRoute - BotBoundaryForLowerRoute

            if min(GapForUpperRoute, GapForLowerRoute) < 2*drc._Metal1MinSpaceAtCorner:
                raise NotImplementedError
            else:
                if GapForUpperRoute > GapForLowerRoute:
                    self._DesignParameter['Met1From3SInvtoInv']['_XYCoordinates']=[
                        [self.getXY('Via1ForInv')[0],
                         [self.getXY('Via1ForInv')[0][0], (TopBoundaryForUpperRoute + BotBoundaryForUpperRoute) / 2],
                         [self.getXY('TristateInv1')[0][0], (TopBoundaryForUpperRoute + BotBoundaryForUpperRoute) / 2]]
                    ]
                else:
                    self._DesignParameter['Met1From3SInvtoInv']['_XYCoordinates'] = [
                        [self.getXY('Via1ForInv')[0],
                         [self.getXY('Via1ForInv')[0][0], (TopBoundaryForLowerRoute + BotBoundaryForLowerRoute) / 2],
                         [self.getXY('TristateInv1')[0][0], (TopBoundaryForLowerRoute + BotBoundaryForLowerRoute) / 2]]
                    ]
        elif TristateInv1_Finger == 2:
            self._DesignParameter['Met1From3SInvtoInv']['_XYCoordinates'] = [
                [self.getXY('Via1ForInv')[0],
                 [self.getXY('TristateInv1', 'met1_output_5')[0][0], self.getXY('Via1ForInv')[0][1]]]
            ]

        else:
            self._DesignParameter['Met1From3SInvtoInv']['_XYCoordinates'] = [
                [self.getXY('Via1ForInv')[0],
                 [self.getXY('TristateInv1', 'Met1RouteY_Out')[0][0], self.getXY('Via1ForInv')[0][1]]]
            ]






        ''' ------------------------------------------ Tristate Inverter ------------------------------------------- '''

        if TristateInv2_Finger == 1:
            self._DesignParameter['TristateInv2'] = self._SrefElementDeclaration(
                _Reflect=[1,0,0], _Angle=180,
                _DesignObj=TristateInverter.TristateInverter(_Name='TristateInv2In{}'.format(_Name)))[0]
            self._DesignParameter['TristateInv2']['_DesignObj']._CalculateDesignParameterFinger1(**Parameters1_TristateInv)
            self._DesignParameter['TristateInv2']['_XYCoordinates'] = [
                [self.getXY('Inv1')[0][0] + self._DesignParameter['Inv0']['_DesignObj'].CellXWidth / 2 + UnitPitch*2 + self._DesignParameter['TristateInv2']['_DesignObj'].CellXWidth / 2, 0]
            ]
            self._DesignParameter['TristateInv3'] = self._SrefElementDeclaration(
                _Reflect=[0,0,0], _Angle=0,
                _DesignObj=TristateInverter.TristateInverter(_Name='TristateInv3In{}'.format(_Name)))[0]
            self._DesignParameter['TristateInv3']['_DesignObj']._CalculateDesignParameterFinger1(**Parameters1_TristateInv)
            self._DesignParameter['TristateInv3']['_XYCoordinates'] = [
                [self.getXY('TristateInv2')[0][0] + self._DesignParameter['TristateInv2']['_DesignObj'].CellXWidth / 2 + 2 * UnitPitch + self._DesignParameter['TristateInv3']['_DesignObj'].CellXWidth / 2, 0]
            ]

            #
            RightBoundary_Met1Route_net211 = self.getXY('TristateInv3', 'PMOS')[0][0]
            LeftBoundary_Met1Route_net211 = self.getXY('TristateInv2', 'PMOS')[0][0]
            self._DesignParameter['Met1Route_net211'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=RightBoundary_Met1Route_net211-LeftBoundary_Met1Route_net211,
                _YWidth=self.getWidth('TristateInv2', 'OutputRouting')
            )

            self._DesignParameter['Met1Route_net211']['_XYCoordinates'] = [
                [(RightBoundary_Met1Route_net211 + LeftBoundary_Met1Route_net211) / 2,
                 self.getXY('TristateInv2', 'PMOS', '_Met1Layer')[0][1] - self.getYWidth('TristateInv2', 'PMOS', '_Met1Layer') / 2 + self.getYWidth('Met1Route_net211') / 2]
            ]

            # leftdown to rightup
            self._DesignParameter['Met1Route_temp2_1'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _Width=66
            )
            self._DesignParameter['Met1Route_temp2_1']['_XYCoordinates'] = [[
                [int(self.getXY('TristateInv2', 'InputVia_EN', '_Met1Layer')[0][0] + 0*UnitPitch), int(self.getXY('TristateInv2', 'InputVia_EN', '_Met1Layer')[0][1])],
                [int(self.getXY('TristateInv2', 'InputVia_EN', '_Met1Layer')[0][0] + 2*UnitPitch), int(self.getXY('TristateInv2', 'InputVia_EN', '_Met1Layer')[0][1])],
                [int(self.getXY('TristateInv2', 'InputVia_EN', '_Met1Layer')[0][0] + 2*UnitPitch), int(self.getXY('TristateInv1', 'InputVia_ENb', '_Met1Layer')[0][1] - self.getYWidth('TristateInv3', 'InputVia_ENb', '_Met1Layer') / 2 + self.getWidth('Met1Route_temp2_1')/2)],
                [int(self.getXY('TristateInv3', 'InputVia_ENb', '_Met1Layer')[0][0]), int(self.getXY('TristateInv3', 'InputVia_ENb', '_Met1Layer')[0][1] - self.getYWidth('TristateInv3', 'InputVia_ENb', '_Met1Layer') / 2 + self.getWidth('Met1Route_temp2_1')/2)]
            ]]
            self._DesignParameter['Met1Route_temp2_2'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _Width=66
            )
            self._DesignParameter['Met1Route_temp2_2']['_XYCoordinates'] = [[
                [int(self.getXY('TristateInv2', 'InputVia_ENb', '_Met1Layer')[0][0] + 0*UnitPitch), int(self.getXY('TristateInv2', 'InputVia_ENb', '_Met1Layer')[0][1] - self.getYWidth('TristateInv2', 'InputVia_ENb', '_Met1Layer')/2 + 33)],
                [int(self.getXY('TristateInv2', 'InputVia_ENb', '_Met1Layer')[0][0] + 1*UnitPitch), int(self.getXY('TristateInv2', 'InputVia_ENb', '_Met1Layer')[0][1] - self.getYWidth('TristateInv2', 'InputVia_ENb', '_Met1Layer')/2 + 33)]
            ]]

            self._DesignParameter['Via1_temp2_3'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1temp2_3In{}'.format(_Name)))[0]
            self._DesignParameter['Via1_temp2_3']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2
            )
            self._DesignParameter['Via1_temp2_3']['_XYCoordinates'] = [
                [int(self.getXY('TristateInv2', 'InputVia_ENb', '_Met1Layer')[0][0] + 1*UnitPitch), int(self.getXY('TristateInv2', 'InputVia_ENb', '_Met1Layer')[0][1]) + 33 - self.getYWidth('Via1_temp2_3', '_Met1Layer') / 2 - self.getYWidth('TristateInv2', 'InputVia_ENb', '_Met1Layer')/2 + 33]
            ]

            self._DesignParameter['Met2Route_temp2_4'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                _Width=66
            )
            self._DesignParameter['Met2Route_temp2_4']['_XYCoordinates'] = [[
                [self.getXY('Via1_temp2_3')[0][0], self.getXY('Via1_temp2_3')[0][1]],
                [self.getXY('Via1_temp2_3')[0][0], self.getXY('TristateInv3', 'InputVia_EN')[0][1]],
                [self.getXY('TristateInv3', 'InputVia_EN')[0][0], self.getXY('TristateInv3', 'InputVia_EN')[0][1]],
            ]]

            self._DesignParameter['Via1_temp2_5'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1temp2_5In{}'.format(_Name)))[0]
            self._DesignParameter['Via1_temp2_5']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2
            )
            self._DesignParameter['Via1_temp2_5']['_XYCoordinates'] = self.getXY('TristateInv3', 'InputVia_EN')

            # #
            self._DesignParameter['Via2_temp05'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2temp05In{}'.format(_Name)))[0]
            self._DesignParameter['Via2_temp05']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2
            )
            self._DesignParameter['Via2_temp05']['_XYCoordinates'] = [
                [self.getXY('TristateInv2', 'InputVia_EN')[0][0], self.getXY('TristateInv2', 'InputVia_EN')[0][1]],
                [self.getXY('TristateInv3', 'InputVia_EN')[0][0], self.getXY('TristateInv3', 'InputVia_EN')[0][1]],
            ]
            self._DesignParameter['Met3Route_temp06'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL3'][0],
                _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                _Width=66
            )
            self._DesignParameter['Met3Route_temp06']['_XYCoordinates'] = [
                [[self.getXY('Via2_temp05')[0][0], self.getXY('Via2_temp05')[0][1]],
                 [self.getXY('Via2_temp05')[0][0], CellHeight]],
                [[self.getXY('Via2_temp05')[1][0], self.getXY('Via2_temp05')[1][1]],
                 [self.getXY('Via2_temp05')[1][0], CellHeight]]
            ]


            # ##
            self._DesignParameter['Via1_TSINV2_A'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1_TSINV2_AIn{}'.format(_Name)))[0]
            self._DesignParameter['Via1_TSINV2_A']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2
            )
            self._DesignParameter['Via1_TSINV2_A']['_XYCoordinates'] = self.getXY('TristateInv2', 'InputVia_A')

            self._DesignParameter['Via1_TSINV3_A'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1_TSINV3_AIn{}'.format(_Name)))[0]
            self._DesignParameter['Via1_TSINV3_A']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2
            )
            self._DesignParameter['Via1_TSINV3_A']['_XYCoordinates'] = self.getXY('TristateInv3', 'InputVia_A')


        elif TristateInv2_Finger == 2:
            self._DesignParameter['TristateInv2'] = self._SrefElementDeclaration(
                _Reflect=[1, 0, 0], _Angle=180,
                _DesignObj=TristateInverter.TristateInverter(_Name='TristateInv2In{}'.format(_Name)))[0]
            self._DesignParameter['TristateInv2']['_DesignObj']._CalculateDesignParameterFinger2(**Parameters3_TristateInvF2)
            self._DesignParameter['TristateInv2']['_XYCoordinates'] = [
                [self.getXY('Inv1')[0][0] + self._DesignParameter['Inv0']['_DesignObj'].CellXWidth / 2 + UnitPitch*2 + self._DesignParameter['TristateInv2']['_DesignObj'].CellXWidth / 2, 0]
            ]
            self._DesignParameter['TristateInv3'] = self._SrefElementDeclaration(
                _Reflect=[0, 0, 0], _Angle=0,
                _DesignObj=TristateInverter.TristateInverter(_Name='TristateInv3In{}'.format(_Name)))[0]
            self._DesignParameter['TristateInv3']['_DesignObj']._CalculateDesignParameterFinger2(**Parameters3_TristateInvF2)
            self._DesignParameter['TristateInv3']['_XYCoordinates'] = [
                [self.getXY('TristateInv2')[0][0] + self._DesignParameter['TristateInv2']['_DesignObj'].CellXWidth / 2 + 2 * UnitPitch + self._DesignParameter['TristateInv3']['_DesignObj'].CellXWidth / 2, 0]
            ]

            # output node connection
            RightBoundary_Met1Route_net211 = self.getXY('TristateInv3', 'met1_output_4')[0][0] + self.getXWidth('TristateInv3', 'met1_output_4') / 2
            LeftBoundary_Met1Route_net211 = self.getXY('TristateInv2', 'met1_output_4')[0][0] - self.getXWidth('TristateInv2', 'met1_output_4') / 2
            self._DesignParameter['Met1Route_net211'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=RightBoundary_Met1Route_net211 - LeftBoundary_Met1Route_net211,
                _YWidth=self.getYWidth('TristateInv2', 'met1_output_3')
            )

            self._DesignParameter['Met1Route_net211']['_XYCoordinates'] = [
                [(RightBoundary_Met1Route_net211 + LeftBoundary_Met1Route_net211) / 2,
                 self.getXY('TristateInv2', 'met1_output_3')[0][1]]
            ]

            # leftdown to rightup
            self._DesignParameter['Met1Route_temp21'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _Width=66
            )
            self._DesignParameter['Met1Route_temp21']['_XYCoordinates'] = [[
                [self.getXY('TristateInv2', 'InputVia_EN', '_Met1Layer')[0][0], self.getXY('TristateInv2', 'InputVia_EN', '_Met1Layer')[0][1]],
                [(self.getXY('TristateInv3', 'NMOS', '_Met1Layer')[0][0] - UnitPitch), self.getXY('TristateInv2', 'InputVia_EN', '_Met1Layer')[0][1]],
                [(self.getXY('TristateInv3', 'NMOS', '_Met1Layer')[0][0] - UnitPitch), self.getXY('TristateInv3', 'InputVia_ENb', '_Met1Layer')[0][1]],
                [self.getXY('TristateInv3', 'InputVia_ENb', '_Met1Layer')[0][0], self.getXY('TristateInv3', 'InputVia_ENb', '_Met1Layer')[0][1]]
            ]]
            self._DesignParameter['Met1Route_temp22'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _Width=66
            )
            self._DesignParameter['Met1Route_temp22']['_XYCoordinates'] = [[
                [self.getXY('TristateInv2', 'InputVia_ENb', '_Met1Layer')[0][0], self.getXY('TristateInv2', 'InputVia_ENb', '_Met1Layer')[0][1]],
                [self.getXY('TristateInv2', 'NMOS', '_Met1Layer')[0][0] + UnitPitch, self.getXY('TristateInv2', 'InputVia_ENb', '_Met1Layer')[0][1]],
                [self.getXY('TristateInv2', 'NMOS', '_Met1Layer')[0][0] + UnitPitch, self.getXY('TristateInv2', 'InputVia_A', '_Met1Layer')[0][1]]
            ]]

            self._DesignParameter['Via1_temp23'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1temp23In{}'.format(_Name)))[0]
            self._DesignParameter['Via1_temp23']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2
            )
            self._DesignParameter['Via1_temp23']['_XYCoordinates'] = [
                [self.getXY('TristateInv2', 'NMOS', '_Met1Layer')[0][0] + UnitPitch, self.getXY('TristateInv2', 'InputVia_A', '_Met1Layer')[0][1]]
            ]

            self._DesignParameter['Met2Route_temp24'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                _Width=66
            )
            self._DesignParameter['Met2Route_temp24']['_XYCoordinates'] = [[
                [self.getXY('Via1_temp23')[0][0], self.getXY('Via1_temp23')[0][1]],
                [self.getXY('Via1_temp23')[0][0], self.getXY('TristateInv3', 'InputVia_EN')[0][1]],
                [self.getXY('TristateInv3', 'InputVia_EN')[0][0], self.getXY('TristateInv3', 'InputVia_EN')[0][1]]
            ]]

            self._DesignParameter['Via1_temp26'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1temp26In{}'.format(_Name)))[0]
            self._DesignParameter['Via1_temp26']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1
            )
            self._DesignParameter['Via1_temp26']['_XYCoordinates'] = self.getXY('TristateInv2', 'InputVia_EN')
            self._DesignParameter['TristateInv2']['_DesignObj']._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self.getYWidth('Via1_temp26', '_Met1Layer')
            self._DesignParameter['TristateInv2']['_DesignObj']._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self.getYWidth('Via1_temp26', '_Met1Layer')


            self._DesignParameter['Via2_temp24'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2temp24In{}'.format(_Name)))[0]
            self._DesignParameter['Via2_temp24']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=1
            )
            self._DesignParameter['Via2_temp24']['_XYCoordinates'] = self.getXY('TristateInv2', 'InputVia_EN')

            self._DesignParameter['Via2_temp25'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2temp25In{}'.format(_Name)))[0]
            self._DesignParameter['Via2_temp25']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=1
            )
            self._DesignParameter['Via2_temp25']['_XYCoordinates'] = self.getXY('TristateInv3', 'InputVia_EN')

            # #
            self._DesignParameter['Via2_temp05'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2temp05In{}'.format(_Name)))[0]
            self._DesignParameter['Via2_temp05']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=1
            )
            self._DesignParameter['Via2_temp05']['_XYCoordinates'] = [
                [self.getXY('TristateInv2', 'InputVia_EN')[0][0], self.getXY('TristateInv2', 'InputVia_EN')[0][1]],
                [self.getXY('TristateInv3', 'InputVia_EN')[0][0], self.getXY('TristateInv3', 'InputVia_EN')[0][1]],
            ]
            self._DesignParameter['Met3Route_temp06'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL3'][0],
                _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                _Width=66
            )
            self._DesignParameter['Met3Route_temp06']['_XYCoordinates'] = [
                [[self.getXY('Via2_temp05')[0][0], self.getXY('Via2_temp05')[0][1]],
                 [self.getXY('Via2_temp05')[0][0], CellHeight]],
                [[self.getXY('Via2_temp05')[1][0], self.getXY('Via2_temp05')[1][1]],
                 [self.getXY('Via2_temp05')[1][0], CellHeight]]
            ]

            self._DesignParameter['Via1_TSINV2_A'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1_TSINV2_AIn{}'.format(_Name)))[0]
            self._DesignParameter['Via1_TSINV2_A']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2
            )
            # self._DesignParameter['Via1_TSINV2_A']['_XYCoordinates'] = [
            #     [self.getXY('TristateInv2')[0][0] - self._DesignParameter['TristateInv2']['_DesignObj']._DesignParameter['InputVia_A']['_XYCoordinates'][0][0], self.getXY('TristateInv2', 'InputVia_A')[0][1]]
            # ]
            self._DesignParameter['Via1_TSINV2_A']['_XYCoordinates'] = self.getXY('TristateInv2', 'InputVia_A')

            self._DesignParameter['Via1_TSINV3_A'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1_TSINV3_AIn{}'.format(_Name)))[0]
            self._DesignParameter['Via1_TSINV3_A']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2
            )
            self._DesignParameter['Via1_TSINV3_A']['_XYCoordinates'] = self.getXY('TristateInv3', 'InputVia_A')

        else:
            self._DesignParameter['TristateInv2'] = self._SrefElementDeclaration(
                _Reflect=[1, 0, 0], _Angle=180,
                _DesignObj=TristateInverter.TristateInverter(_Name='TristateInv2In{}'.format(_Name)))[0]
            self._DesignParameter['TristateInv2']['_DesignObj']._CalculateDesignParameterFinger3orMore_v2(**Parameters3_TristateInvF3)
            self._DesignParameter['TristateInv2']['_XYCoordinates'] = [
                [self.getXY('Inv1')[0][0] + self._DesignParameter['Inv0']['_DesignObj'].CellXWidth / 2 + UnitPitch * 2 + self._DesignParameter['TristateInv2']['_DesignObj'].CellXWidth / 2, 0]
            ]
            self._DesignParameter['TristateInv3'] = self._SrefElementDeclaration(
                _Reflect=[0, 0, 0], _Angle=0,
                _DesignObj=TristateInverter.TristateInverter(_Name='TristateInv3In{}'.format(_Name)))[0]
            self._DesignParameter['TristateInv3']['_DesignObj']._CalculateDesignParameterFinger3orMore_v2(**Parameters3_TristateInvF3)
            self._DesignParameter['TristateInv3']['_XYCoordinates'] = [
                [self.getXY('TristateInv2')[0][0] + self._DesignParameter['TristateInv2']['_DesignObj'].CellXWidth / 2 + 2 * UnitPitch + self._DesignParameter['TristateInv3']['_DesignObj'].CellXWidth / 2, 0]
            ]

            # output node connection
            RightBoundary_Met1Route_net211 = self.getXY('TristateInv3', 'Met1RouteX_PMOut')[0][0] + self.getXWidth('TristateInv3', 'Met1RouteX_PMOut') / 2
            LeftBoundary_Met1Route_net211 = self.getXY('TristateInv2', 'Met1RouteX_PMOut')[0][0] - self.getXWidth('TristateInv2', 'Met1RouteX_PMOut') / 2
            self._DesignParameter['Met1Route_net211'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=RightBoundary_Met1Route_net211 - LeftBoundary_Met1Route_net211,
                _YWidth=self.getYWidth('TristateInv2', 'Met1RouteX_PMOut')
            )

            self._DesignParameter['Met1Route_net211']['_XYCoordinates'] = [
                [(RightBoundary_Met1Route_net211 + LeftBoundary_Met1Route_net211) / 2,
                 self.getXY('TristateInv2', 'Met1RouteX_PMOut')[0][1]]
            ]

            # leftdown to rightup
            self._DesignParameter['Met1Route_temp21'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _Width=66
            )
            self._DesignParameter['Met1Route_temp21']['_XYCoordinates'] = [[
                [self.getXY('TristateInv2')[0][0] - self._DesignParameter['TristateInv2']['_DesignObj']._DesignParameter['polyInputEN']['_XYCoordinates'][0][0],
                 self.getXY('TristateInv2', 'polyInputEN', '_Met1Layer')[0][1]],
                [(self.getXY('TristateInv3', 'NM1', '_Met1Layer')[0][0] - UnitPitch),
                 self.getXY('TristateInv2', 'polyInputEN', '_Met1Layer')[0][1]],
                [(self.getXY('TristateInv3', 'NM1', '_Met1Layer')[0][0] - UnitPitch),
                 self.getXY('TristateInv3', 'polyInputENb', '_Met1Layer')[0][1]],
                [self.getXY('TristateInv3', 'polyInputENb', '_Met1Layer')[0][0],
                 self.getXY('TristateInv3', 'polyInputENb', '_Met1Layer')[0][1]]
            ]]
            self._DesignParameter['Met1Route_temp22'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _Width=66
            )
            self._DesignParameter['Met1Route_temp22']['_XYCoordinates'] = [[
                [self.getXY('TristateInv2')[0][0] - self._DesignParameter['TristateInv2']['_DesignObj']._DesignParameter['polyInputENb']['_XYCoordinates'][0][0],
                 self.getXY('TristateInv2', 'polyInputENb', '_Met1Layer')[0][1]],
                [self.getXY('TristateInv2', 'NM1', '_Met1Layer')[0][0] + UnitPitch,
                 self.getXY('TristateInv2', 'polyInputENb', '_Met1Layer')[0][1]],
                [self.getXY('TristateInv2', 'NM1', '_Met1Layer')[0][0] + UnitPitch,
                 self.getXY('TristateInv2', 'polyInputA', '_Met1Layer')[0][1]]
            ]]

            self._DesignParameter['Via1_temp23'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1temp23In{}'.format(_Name)))[0]
            self._DesignParameter['Via1_temp23']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2
            )
            self._DesignParameter['Via1_temp23']['_XYCoordinates'] = [
                [self.getXY('TristateInv2', 'NM1', '_Met1Layer')[0][0] + UnitPitch,
                 self.getXY('TristateInv2', 'polyInputA', '_Met1Layer')[0][1]]
            ]

            self._DesignParameter['Met2Route_temp24'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                _Width=66
            )
            self._DesignParameter['Met2Route_temp24']['_XYCoordinates'] = [[
                [self.getXY('Via1_temp23')[0][0], self.getXY('Via1_temp23')[0][1]],
                [self.getXY('Via1_temp23')[0][0], self.getXY('TristateInv3', 'polyInputEN')[0][1]],
                [self.getXY('TristateInv3', 'polyInputEN')[0][0], self.getXY('TristateInv3', 'polyInputEN')[0][1]]
            ]]

            self._DesignParameter['Via1_temp26'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1temp26In{}'.format(_Name)))[0]
            self._DesignParameter['Via1_temp26']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1
            )
            self._DesignParameter['Via1_temp26']['_XYCoordinates'] = [[
                self.getXY('TristateInv2')[0][0] - self._DesignParameter['TristateInv2']['_DesignObj']._DesignParameter['polyInputEN']['_XYCoordinates'][0][0],
                self.getXY('TristateInv2')[0][1] + self._DesignParameter['TristateInv2']['_DesignObj']._DesignParameter['polyInputEN']['_XYCoordinates'][0][1]
            ]]

            self._DesignParameter['Via2_temp24'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2temp24In{}'.format(_Name)))[0]
            self._DesignParameter['Via2_temp24']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=1
            )
            self._DesignParameter['Via2_temp24']['_XYCoordinates'] = [[
                self.getXY('TristateInv2')[0][0] - self._DesignParameter['TristateInv2']['_DesignObj']._DesignParameter['polyInputEN']['_XYCoordinates'][0][0],
                self.getXY('TristateInv2')[0][1] + self._DesignParameter['TristateInv2']['_DesignObj']._DesignParameter['polyInputEN']['_XYCoordinates'][0][1]
            ]]
            self._DesignParameter['Via2_temp25'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2temp25In{}'.format(_Name)))[0]
            self._DesignParameter['Via2_temp25']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=1
            )
            self._DesignParameter['Via2_temp25']['_XYCoordinates'] = self.getXY('TristateInv3', 'polyInputEN')


            # #
            self._DesignParameter['Via2_temp05'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2temp05In{}'.format(_Name)))[0]
            self._DesignParameter['Via2_temp05']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=1
            )
            self._DesignParameter['Via2_temp05']['_XYCoordinates'] = [
                [self.getXY('TristateInv2')[0][0] - self._DesignParameter['TristateInv2']['_DesignObj']._DesignParameter['polyInputEN']['_XYCoordinates'][0][0],
                 self.getXY('TristateInv2', 'polyInputEN')[0][1]],


                [self.getXY('TristateInv3', 'polyInputEN')[0][0], self.getXY('TristateInv3', 'polyInputEN')[0][1]],
            ]
            self._DesignParameter['Met3Route_temp06'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL3'][0],
                _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                _Width=66
            )
            self._DesignParameter['Met3Route_temp06']['_XYCoordinates'] = [
                [[self.getXY('Via2_temp05')[0][0], self.getXY('Via2_temp05')[0][1]],
                 [self.getXY('Via2_temp05')[0][0], CellHeight]],
                [[self.getXY('Via2_temp05')[1][0], self.getXY('Via2_temp05')[1][1]],
                 [self.getXY('Via2_temp05')[1][0], CellHeight]]
            ]

            self._DesignParameter['Via1_TSINV2_A'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1_TSINV2_AIn{}'.format(_Name)))[0]
            self._DesignParameter['Via1_TSINV2_A']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1
            )
            # self._DesignParameter['Via1_TSINV2_A']['_XYCoordinates'] = [
            #     [self.getXY('TristateInv2')[0][0] - self._DesignParameter['TristateInv2']['_DesignObj']._DesignParameter['polyInputA']['_XYCoordinates'][0][0], self.getXY('TristateInv2', 'polyInputA')[0][1]]
            # ]
            self._DesignParameter['Via1_TSINV2_A']['_XYCoordinates'] = self.getXY('TristateInv2', 'polyInputA')

            self._DesignParameter['Via1_TSINV3_A'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1_TSINV3_AIn{}'.format(_Name)))[0]
            self._DesignParameter['Via1_TSINV3_A']['_DesignObj']._CalculateDesignParameterSameEnclosure(
                _ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1
            )
            self._DesignParameter['Via1_TSINV3_A']['_XYCoordinates'] = self.getXY('TristateInv3', 'polyInputA')



        RightBoundary = self.getXY('TristateInv3')[0][0] + self._DesignParameter['TristateInv3']['_DesignObj'].CellXWidth / 2

        self._DesignParameter['XVT'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[XVT][0],
            _Datatype=DesignParameters._LayerMapping[XVT][1],
            _XWidth=RightBoundary,
            _YWidth=CellHeight,
            _XYCoordinates=[[RightBoundary/2, CellHeight/2]]
        )

        self._DesignParameter['VDDRail'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=RightBoundary,
            _YWidth=300,
            _XYCoordinates=[[RightBoundary / 2, CellHeight], [RightBoundary / 2, 0]]
        )

        '''  '''
        # OD RX DIFF
        rightBoundary = self.getXYRight('TristateInv3', 'VSSRail', '_ODLayer')[0][0]
        leftBoundary = self.getXYLeft('TristateInv0', 'VSSRail', '_ODLayer')[0][0]
        self._DesignParameter['_ODLayerForVSSRail'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0],
            _Datatype=DesignParameters._LayerMapping['DIFF'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('TristateInv0', 'VSSRail', '_ODLayer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, 0]]
        )
        self._DesignParameter['_ODLayerForVDDRail'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0],
            _Datatype=DesignParameters._LayerMapping['DIFF'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('TristateInv0', 'VDDRail', '_ODLayer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, CellHeight]]
        )

        # PIMP PP on vssrail
        rightBoundary = self.getXYRight('TristateInv3', 'VSSRail', '_PPLayer')[0][0]
        leftBoundary = self.getXYLeft('TristateInv0', 'VSSRail', '_PPLayer')[0][0]
        self._DesignParameter['_PPLayerForVSSRail'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('TristateInv0', 'VSSRail', '_PPLayer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, 0]]
        )



        # PIMP PP on pmos
        if TristateInv1_Finger in (1, 2):
            leftBoundary = self.getXYLeft('TristateInv0', 'PMOS', '_PPLayer')[0][0]
            topBoundary1 = self.getXYTop('TristateInv0', 'PMOS', '_PPLayer')[0][1]
            botBoundary1 = self.getXYBot('TristateInv0', 'PMOS', '_PPLayer')[0][1]
        else:
            leftBoundary = self.getXYLeft('TristateInv0', 'PM1', '_PPLayer')[0][0]
            topBoundary1 = self.getXYTop('TristateInv0', 'PM1', '_PPLayer')[0][1]
            botBoundary1 = self.getXYBot('TristateInv0', 'PM1', '_PPLayer')[0][1]

        if TristateInv2_Finger in (1, 2):
            rightBoundary = self.getXYRight('TristateInv3', 'PMOS', '_PPLayer')[0][0]
            topBoundary2 = self.getXYTop('TristateInv3', 'PMOS', '_PPLayer')[0][1]
            botBoundary2 = self.getXYBot('TristateInv3', 'PMOS', '_PPLayer')[0][1]
        else:
            rightBoundary = self.getXYRight('TristateInv3', 'PM2', '_PPLayer')[0][0]
            topBoundary2 = self.getXYTop('TristateInv3', 'PM2', '_PPLayer')[0][1]
            botBoundary2 = self.getXYBot('TristateInv3', 'PM2', '_PPLayer')[0][1]

        topBoundary3 = self.getXYTop('Inv0', '_PMOS', '_PPLayer')[0][1]
        botBoundary3 = self.getXYBot('Inv0', '_PMOS', '_PPLayer')[0][1]
        topBoundary = max(topBoundary1, topBoundary2, topBoundary3)
        botBoundary = min(botBoundary1, botBoundary2, botBoundary3)

        self._DesignParameter['_PPLayerForPMOS'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=topBoundary-botBoundary,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, (topBoundary + botBoundary) / 2]]
        )

        # NW
        rightBoundary = self.getXYRight('TristateInv3', 'nwlayer')[0][0]
        leftBoundary = self.getXYLeft('TristateInv0', 'nwlayer')[0][0]

        topBoundary1 = self.getXYTop('TristateInv0', 'nwlayer')[0][1]
        botBoundary1 = self.getXYBot('TristateInv0', 'nwlayer')[0][1]
        topBoundary2 = self.getXYTop('TristateInv3', 'nwlayer')[0][1]
        botBoundary2 = self.getXYBot('TristateInv3', 'nwlayer')[0][1]
        topBoundary3 = self.getXYTop('Inv0', '_NWLayerBoundary')[0][1]
        botBoundary3 = self.getXYBot('Inv0', '_NWLayerBoundary')[0][1]
        topBoundary = max(topBoundary1, topBoundary2, topBoundary3)
        botBoundary = min(botBoundary1, botBoundary2, botBoundary3)

        self._DesignParameter['_NWLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=topBoundary-botBoundary,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, (topBoundary + botBoundary) / 2]]
        )
