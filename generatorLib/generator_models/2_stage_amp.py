import math
import copy

#
from generatorLib import StickDiagram
from generatorLib import DesignParameters
from generatorLib import DRC

#
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import NCAP
from generatorLib.generator_models import opppcres_b_sm
from generatorLib.generator_models import PbodyContact_sm
from generatorLib.generator_models import PSubRing_sm
from generatorLib.generator_models import NSubRing_sm

from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import ViaPoly2Met1_resize
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaMet22Met3

#
from generatorLib import CoordinateCalc as CoordCalc


class _SingleEnded2StageOPAmp(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name='_SingleEnded2StageOPAmp'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name


    def _CalculateDesignParameter(self,
                                  P0_Finger=None,
                                  P1_Finger=None,
                                  P2_Finger=None,
                                  P3_Finger=None,

                                  N0_Finger=None,
                                  N1_Finger=None,
                                  N2_Finger=None,
                                  N3_Finger=None,
                                  N4_Finger=None,

                                  ChannelLength=None,
                                  MOS_Width=None,
                                  GateSpacing=None,
                                  SDWidth=None,
                                  XVT=None,

                                  NCAP_XWidth=None,  # Length
                                  NCAP_YWidth=None,  # Width
                                  NCAP_NumofGate=None,
                                  NCAP_NumofRX=None,   # 270deg rotate

                                  ResWidth=None,
                                  ResLength=None,
                                  ResCONUMX=None,
                                  ResCONUMY=None,
                                  _SeriesStripes=None,
                                  _ParallelStripes = None,

                                  _GuardringCOpitch=None,
                                  _GuardringbyArea=True,
                                  _GuardringNumofCO=None,
                                  _GuardringThickness=None,
                                  _GuardringPPEnclosure=None
                                  ):

        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        UnitPitch = ChannelLength + GateSpacing

        def roundReal(val, digits):
            return round(val+10**(-len(str(val))-1), digits)

        Parameters_P0 = dict(
            _PMOSNumberofGate=P0_Finger,
            _PMOSChannelWidth=MOS_Width,
            _PMOSChannellength=ChannelLength,
            _PMOSDummy=True,
            _GateSpacing=GateSpacing,
            _SDWidth=SDWidth,
            _XVT=XVT
        )

        Parameters_P1 = dict(
            _PMOSNumberofGate=P1_Finger,
            _PMOSChannelWidth=MOS_Width,
            _PMOSChannellength=ChannelLength,
            _PMOSDummy=True,
            _GateSpacing=GateSpacing,
            _SDWidth=SDWidth,
            _XVT=XVT
        )

        Parameters_P2 = dict(
            _PMOSNumberofGate=P2_Finger,
            _PMOSChannelWidth=MOS_Width,
            _PMOSChannellength=ChannelLength,
            _PMOSDummy=True,
            _GateSpacing=GateSpacing,
            _SDWidth=SDWidth,
            _XVT=XVT
        )

        Parameters_P3 = dict(
            _PMOSNumberofGate=P3_Finger,
            _PMOSChannelWidth=MOS_Width,
            _PMOSChannellength=ChannelLength,
            _PMOSDummy=True,
            _GateSpacing=GateSpacing,
            _SDWidth=SDWidth,
            _XVT=XVT
        )

        Parameters_N0 = dict(
            _NMOSNumberofGate=N0_Finger,
            _NMOSChannelWidth=MOS_Width,
            _NMOSChannellength=ChannelLength,
            _NMOSDummy=True,
            _GateSpacing=GateSpacing,
            _SDWidth=SDWidth,
            _XVT=XVT
        )

        Parameters_N1 = dict(
            _NMOSNumberofGate=N1_Finger,
            _NMOSChannelWidth=MOS_Width,
            _NMOSChannellength=ChannelLength,
            _NMOSDummy=True,
            _GateSpacing=GateSpacing,
            _SDWidth=SDWidth,
            _XVT=XVT
        )

        Parameters_N2 = dict(
            _NMOSNumberofGate=N2_Finger,
            _NMOSChannelWidth=MOS_Width,
            _NMOSChannellength=ChannelLength,
            _NMOSDummy=True,
            _GateSpacing=GateSpacing,
            _SDWidth=SDWidth,
            _XVT=XVT
        )

        Parameters_N3 = dict(
            _NMOSNumberofGate=N3_Finger,
            _NMOSChannelWidth=MOS_Width,
            _NMOSChannellength=ChannelLength,
            _NMOSDummy=True,
            _GateSpacing=GateSpacing,
            _SDWidth=SDWidth,
            _XVT=XVT
        )

        Parameters_N4 = dict(
            _NMOSNumberofGate=N4_Finger,
            _NMOSChannelWidth=MOS_Width,
            _NMOSChannellength=ChannelLength,
            _NMOSDummy=True,
            _GateSpacing=GateSpacing,
            _SDWidth=SDWidth,
            _XVT=XVT
        )

        Parameters_NCAP = dict(
            _XWidth=NCAP_XWidth,
            _YWidth=NCAP_YWidth,
            _NumofGates=NCAP_NumofGate,
            _NumofOD=NCAP_NumofRX,
            NumOfCOX=None,
            NumOfCOY=None,
            Guardring=False
        )

        Parameters_RES = dict(
            _ResWidth=ResWidth,
            _ResLength=ResLength,
            _CONUMX=ResCONUMX,
            _CONUMY=ResCONUMY,
            _SeriesStripes=_SeriesStripes,
            _ParallelStripes=_ParallelStripes
        )

        print('#########################################################################################################')
        print('                                    {}  2 stage OP Amp Calculation Start                                 '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')

        print('******************************************* Locate instances *******************************************')
        # cascade PMOS (left)
        self._DesignParameter['P0'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=180, _DesignObj=PMOSWithDummy._PMOS(_Name='P0In{}'.format(_Name)))[0]
        self._DesignParameter['P0']['_DesignObj']._CalculatePMOSDesignParameter(**Parameters_P0)
        self._DesignParameter['P0']['_XYCoordinates'] = [[0, 0]]

        # cascade PMOS (right)
        self._DesignParameter['P1'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=PMOSWithDummy._PMOS(_Name='P1In{}'.format(_Name)))[0]
        self._DesignParameter['P1']['_DesignObj']._CalculatePMOSDesignParameter(**Parameters_P1)
        self._DesignParameter['P1']['_XYCoordinates'] = [[0, 0]]

        # 2nd stage PMOS
        self._DesignParameter['P2'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=PMOSWithDummy._PMOS(_Name='P2In{}'.format(_Name)))[0]
        self._DesignParameter['P2']['_DesignObj']._CalculatePMOSDesignParameter(**Parameters_P2)
        self._DesignParameter['P2']['_XYCoordinates'] = [[0, 0]]

        # current mirror PMOS
        self._DesignParameter['P3'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=180, _DesignObj=PMOSWithDummy._PMOS(_Name='P3In{}'.format(_Name)))[0]
        self._DesignParameter['P3']['_DesignObj']._CalculatePMOSDesignParameter(**Parameters_P3)
        self._DesignParameter['P3']['_XYCoordinates'] = [[0, 0]]

        # input NMOS (left)
        self._DesignParameter['N0'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=180, _DesignObj=NMOSWithDummy._NMOS(_Name='N0In{}'.format(_Name)))[0]
        self._DesignParameter['N0']['_DesignObj']._CalculateNMOSDesignParameter(**Parameters_N0)
        self._DesignParameter['N0']['_XYCoordinates'] = [[0, 0]]

        # input NMOS (right)
        self._DesignParameter['N1'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=NMOSWithDummy._NMOS(_Name='N1In{}'.format(_Name)))[0]
        self._DesignParameter['N1']['_DesignObj']._CalculateNMOSDesignParameter(**Parameters_N1)
        self._DesignParameter['N1']['_XYCoordinates'] = [[0, 0]]

        # bias NMOS
        self._DesignParameter['N2'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=NMOSWithDummy._NMOS(_Name='N2In{}'.format(_Name)))[0]
        self._DesignParameter['N2']['_DesignObj']._CalculateNMOSDesignParameter(**Parameters_N2)
        self._DesignParameter['N2']['_XYCoordinates'] = [[0, 0]]

        # 2nd stage NMOS
        self._DesignParameter['N3'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=NMOSWithDummy._NMOS(_Name='N3In{}'.format(_Name)))[0]
        self._DesignParameter['N3']['_DesignObj']._CalculateNMOSDesignParameter(**Parameters_N3)
        self._DesignParameter['N3']['_XYCoordinates'] = [[0, 0]]

        # current mirror NMOS
        self._DesignParameter['N4'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=180, _DesignObj=NMOSWithDummy._NMOS(_Name='N4In{}'.format(_Name)))[0]
        self._DesignParameter['N4']['_DesignObj']._CalculateNMOSDesignParameter(**Parameters_N4)
        self._DesignParameter['N4']['_XYCoordinates'] = [[0, 0]]

        # compensation Cap
        self._DesignParameter['NCAP'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=90, _DesignObj=NCAP._NCap(_Name='NCAPIn{}'.format(_Name)))[0]
        self._DesignParameter['NCAP']['_DesignObj']._CalculateNCapDesignParameter(**Parameters_NCAP)
        self._DesignParameter['NCAP']['_XYCoordinates'] = [[0, 0]]

        # RHP zero Res
        self._DesignParameter['RES'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=270, _DesignObj=opppcres_b_sm._Opppcres(_Name='RESIn{}'.format(_Name)))[0]
        self._DesignParameter['RES']['_DesignObj']._CalculateOpppcresDesignParameter(**Parameters_RES)
        self._DesignParameter['RES']['_XYCoordinates'] = [[0, 0]]



        print('******************************* Calculate total X width & dummy fingers ********************************')
        # temporary placement of Pbodycontact btw NCAP & RES
        _tmpPbodyMet1XWidth = max(self._DesignParameter['NCAP']['_DesignObj']._DesignParameter['NWELL']['_XWidth'], self._DesignParameter['RES']['_DesignObj']._DesignParameter['_PRESLayer']['_XWidth'])
        if _GuardringPPEnclosure != None:
            _PbodyMet1XWidth = _tmpPbodyMet1XWidth + _GuardringPPEnclosure * 2
        else:
            if DesignParameters._Technology == 'SS28nm':
                _PbodyMet1XWidth = _tmpPbodyMet1XWidth + 2 * _DRCObj._PpMinExtensiononPactive2
                if _tmpPbodyMet1XWidth < 170:
                    _PbodyMet1XWidth = _tmpPbodyMet1XWidth + 2 * _DRCObj._PpMinExtensiononPactive2 + 28
            else:
                _PbodyMet1XWidth = _tmpPbodyMet1XWidth + 2 * _DRCObj._PpMinExtensiononPactive
        self._DesignParameter['PbodyContact'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=90, _DesignObj=PbodyContact_sm._PbodyContact(_Name='PbodyContactIn{}'.format(_Name)))[0]
        self._DesignParameter['PbodyContact']['_DesignObj']._CalculatePbodyContactDesignParameter(_InputModeArea=_GuardringbyArea, _NumberOfPbodyCOX=_GuardringNumofCO, _NumberOfPbodyCOY=_GuardringNumofCO,
                                                                                                  _Met1XWidth=_PbodyMet1XWidth, _Met1YWidth=_GuardringThickness,
                                                                                                  _COXpitch=_GuardringCOpitch, _COYpitch=_GuardringCOpitch, _PPEnclosure=_GuardringPPEnclosure)
        self._DesignParameter['PbodyContact']['_XYCoordinates'] = [[0, 0]]

        # find maximum X width of elements
        PMOS_total_width = (abs(self.getXYRight('P0', '_PODummyLayer')[0][0]) + abs(self.getXYLeft('P1', '_PODummyLayer')[0][0]) + abs(self.getXYLeft('P2', '_PODummyLayer')[0][0]) + abs(self.getXYRight('P3', '_PODummyLayer')[0][0])) * 2 - ChannelLength * 3 + _DRCObj._MetalxMinSpace41 * 2
        NMOS_total_width = (abs(self.getXYRight('N0', '_PODummyLayer')[0][0]) + abs(self.getXYLeft('N1', '_PODummyLayer')[0][0]) + abs(self.getXYLeft('N2', '_PODummyLayer')[0][0]) + abs(self.getXYLeft('N3', '_PODummyLayer')[0][0]) + abs(self.getXYRight('N4', '_PODummyLayer')[0][0])) * 2 - ChannelLength * 4 + _DRCObj._MetalxMinSpace41 * 2
        if _GuardringPPEnclosure + _DRCObj._PpMinSpacetoPRES > _DRCObj._RXMinSpacetoPRES:
            CapRes_total_width = abs(self.getYWidth('NCAP', 'NWELL') + self.getYWidth('PbodyContact', '_PPLayer') + self.getYWidth('RES', '_PRESLayer')) + _DRCObj._PpMinSpacetoPRES * 2
        else:
            CapRes_total_width = abs(self.getYWidth('NCAP', 'NWELL') + self.getYWidth('PbodyContact', '_PPLayer') - _GuardringPPEnclosure * 2 + self.getYWidth('RES', '_PRESLayer')) + _DRCObj._RXMinSpacetoPRES * 2
        Max_XWidth = max(PMOS_total_width, NMOS_total_width, CapRes_total_width)

        # calculate dummy fingers
        if Max_XWidth == PMOS_total_width:
            [P0Dummy_Finger, P1Dummy_Finger, P2Dummy_Finger] = [0, 0, 0]
            N0Dummy_Finger = int(((Max_XWidth - _DRCObj._MetalxMinSpace41 * 2) / 2 - (N2_Finger + 1) * UnitPitch / 2 - (N0_Finger + 1) * UnitPitch - (N4_Finger + 1) * UnitPitch) / UnitPitch)
            N1Dummy_Finger = int(((Max_XWidth - _DRCObj._MetalxMinSpace41 * 2) / 2 - (N2_Finger + 1) * UnitPitch / 2 - (N1_Finger + 1) * UnitPitch - (N3_Finger + 1) * UnitPitch) / UnitPitch)
        elif Max_XWidth == PMOS_total_width:
            [N0Dummy_Finger, N1Dummy_Finger] = [0, 0]
            P1Dummy_Finger = N2_Finger
            P0Dummy_Finger = int(((Max_XWidth - _DRCObj._MetalxMinSpace41 * 2) / 2 - (P1Dummy_Finger + 1) * UnitPitch / 2 - (P0_Finger + 1) * UnitPitch - (P3_Finger + 1) * UnitPitch) / UnitPitch)
            P2Dummy_Finger = int(((Max_XWidth - _DRCObj._MetalxMinSpace41 * 2) / 2 - (P1Dummy_Finger + 1) * UnitPitch / 2 - (P1_Finger + 1) * UnitPitch - (P2_Finger + 1) * UnitPitch) / UnitPitch)
        else:
            N0Dummy_Finger = int(((Max_XWidth - _DRCObj._PpMinSpacetoPRES * 2) / 2 - (N2_Finger + 1) * UnitPitch / 2 - (N0_Finger + 1) * UnitPitch - (N4_Finger + 1) * UnitPitch) / UnitPitch)
            N1Dummy_Finger = int(((Max_XWidth - _DRCObj._PpMinSpacetoPRES * 2) / 2 - (N2_Finger + 1) * UnitPitch / 2 - (N1_Finger + 1) * UnitPitch - (N3_Finger + 1) * UnitPitch) / UnitPitch)
            P1Dummy_Finger = N2_Finger
            P0Dummy_Finger = int(((Max_XWidth - _DRCObj._PpMinSpacetoPRES * 2) / 2 - (P1Dummy_Finger + 1) * UnitPitch / 2 - (P0_Finger + 1) * UnitPitch - (P3_Finger + 1) * UnitPitch) / UnitPitch)
            P2Dummy_Finger = int(((Max_XWidth - _DRCObj._PpMinSpacetoPRES * 2) / 2 - (P1Dummy_Finger + 1) * UnitPitch / 2 - (P1_Finger + 1) * UnitPitch - (P2_Finger + 1) * UnitPitch) / UnitPitch)



        print('******************************** NMOS Coordinate setting & Gate contact ********************************')
        NMOS_Ycoordinate = 0
        self._DesignParameter['N2']['_XYCoordinates'] = [[0, NMOS_Ycoordinate]]
        self._DesignParameter['N0']['_XYCoordinates'] = \
            [[self.getXY('N2')[0][0] - (N2_Finger / 2 + 0.5) * UnitPitch - (N0_Finger / 2 + 0.5) * UnitPitch, NMOS_Ycoordinate]]
        self._DesignParameter['N1']['_XYCoordinates'] = \
            [[self.getXY('N2')[0][0] + (N2_Finger / 2 + 0.5) * UnitPitch + (N1_Finger / 2 + 0.5) * UnitPitch, NMOS_Ycoordinate]]

        if N0Dummy_Finger >= 1:
            self._DesignParameter['N0Dummy'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0, _DesignObj=NMOSWithDummy._NMOS(_Name='N0DummyIn{}'.format(_Name)))[0]
            self._DesignParameter['N0Dummy']['_DesignObj']._CalculateNMOSDesignParameter(_NMOSNumberofGate=N0Dummy_Finger, _NMOSChannelWidth=MOS_Width, _NMOSChannellength=ChannelLength, _NMOSDummy=False, _GateSpacing=GateSpacing, _SDWidth=SDWidth, _XVT=XVT)
            self._DesignParameter['N0Dummy']['_XYCoordinates'] = [[self.getXY('N0')[0][0] - (N0_Finger / 2 + 0.5) * UnitPitch - (N0Dummy_Finger / 2 + 0.5) * UnitPitch, NMOS_Ycoordinate]]
            self._DesignParameter['N4']['_XYCoordinates'] = \
                [[self.getXY('N0Dummy')[0][0] - (N0Dummy_Finger / 2 + 0.5) * UnitPitch - (N4_Finger / 2 + 0.5) * UnitPitch, NMOS_Ycoordinate]]

        if N1Dummy_Finger >= 1:
            self._DesignParameter['N1Dummy'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0, _DesignObj=NMOSWithDummy._NMOS(_Name='N1DummyIn{}'.format(_Name)))[0]
            self._DesignParameter['N1Dummy']['_DesignObj']._CalculateNMOSDesignParameter(_NMOSNumberofGate=N1Dummy_Finger, _NMOSChannelWidth=MOS_Width, _NMOSChannellength=ChannelLength, _NMOSDummy=False, _GateSpacing=GateSpacing, _SDWidth=SDWidth, _XVT=XVT)
            self._DesignParameter['N1Dummy']['_XYCoordinates'] = [[self.getXY('N1')[0][0] + (N1_Finger / 2 + 0.5) * UnitPitch + (N1Dummy_Finger / 2 + 0.5) * UnitPitch, NMOS_Ycoordinate]]
            self._DesignParameter['N3']['_XYCoordinates'] = \
                [[self.getXY('N1Dummy')[0][0] + (N1Dummy_Finger / 2 + 0.5) * UnitPitch + (N3_Finger / 2 + 0.5) * UnitPitch, NMOS_Ycoordinate]]


        # NMOS Gate contact
        PolyGate_YWidth = _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByPOAtLeastTwoSide

        N0PolyGate_XWidth = abs(self.getXYLeft('N0', '_POLayer')[-1][0] - self.getXYRight('N0', '_POLayer')[0][0])
        N0PolyGate_COXnum = int((N0PolyGate_XWidth - 2 * _DRCObj._Metal1MinEnclosureCO2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)
        N0PolyGate_XYCoordinates = [[self.getXY('N0')[0][0], self.getXYTop('N0', '_ODLayer')[0][1] + _DRCObj._XvtMinEnclosureOfODY + PolyGate_YWidth / 2]]
        self._DesignParameter['N0PolyGate'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0, _DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='N0PolyGateIn{}'.format(_Name)))[0]
        self._DesignParameter['N0PolyGate']['_DesignObj']._CalculateDesignParameter(_ViaPoly2Met1NumberOfCOX=N0PolyGate_COXnum, _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=None, Met1YWidth=PolyGate_YWidth, POXWidth=N0PolyGate_XWidth, POYWidth=PolyGate_YWidth)
        self._DesignParameter['N0PolyGate']['_XYCoordinates'] = N0PolyGate_XYCoordinates

        N1PolyGate_XWidth = abs(self.getXYRight('N1', '_POLayer')[-1][0] - self.getXYLeft('N1', '_POLayer')[0][0])
        N1PolyGate_COXnum = int((N1PolyGate_XWidth - 2 * _DRCObj._Metal1MinEnclosureCO2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)
        N1PolyGate_XYCoordinates = [[self.getXY('N1')[0][0], self.getXYTop('N1', '_ODLayer')[0][1] + _DRCObj._XvtMinEnclosureOfODY + PolyGate_YWidth / 2]]
        self._DesignParameter['N1PolyGate'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0, _DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='N1PolyGateIn{}'.format(_Name)))[0]
        self._DesignParameter['N1PolyGate']['_DesignObj']._CalculateDesignParameter(_ViaPoly2Met1NumberOfCOX=N1PolyGate_COXnum, _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=None, Met1YWidth=PolyGate_YWidth, POXWidth=N1PolyGate_XWidth, POYWidth=PolyGate_YWidth)
        self._DesignParameter['N1PolyGate']['_XYCoordinates'] = N1PolyGate_XYCoordinates

        N2PolyGate_XWidth = abs(self.getXYRight('N2', '_POLayer')[-1][0] - self.getXYLeft('N2', '_POLayer')[0][0])
        N2PolyGate_COXnum = int((N2PolyGate_XWidth - 2 * _DRCObj._Metal1MinEnclosureCO2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)
        N2PolyGate_XYCoordinates = [[self.getXY('N2')[0][0], self.getXYTop('N2', '_ODLayer')[0][1] + _DRCObj._XvtMinEnclosureOfODY + PolyGate_YWidth / 2]]
        self._DesignParameter['N2PolyGate'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0, _DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='N2PolyGateIn{}'.format(_Name)))[0]
        self._DesignParameter['N2PolyGate']['_DesignObj']._CalculateDesignParameter(_ViaPoly2Met1NumberOfCOX=N2PolyGate_COXnum, _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=None, Met1YWidth=PolyGate_YWidth, POXWidth=N2PolyGate_XWidth, POYWidth=PolyGate_YWidth)
        self._DesignParameter['N2PolyGate']['_XYCoordinates'] = N2PolyGate_XYCoordinates

        N3PolyGate_XWidth = abs(self.getXYRight('N3', '_POLayer')[-1][0] - self.getXYLeft('N3', '_POLayer')[0][0])
        N3PolyGate_COXnum = int((N3PolyGate_XWidth - 2 * _DRCObj._Metal1MinEnclosureCO2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)
        N3PolyGate_XYCoordinates = [[self.getXY('N3')[0][0], self.getXYTop('N3', '_ODLayer')[0][1] + _DRCObj._XvtMinEnclosureOfODY + PolyGate_YWidth / 2]]
        self._DesignParameter['N3PolyGate'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0, _DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='N3PolyGateIn{}'.format(_Name)))[0]
        self._DesignParameter['N3PolyGate']['_DesignObj']._CalculateDesignParameter(_ViaPoly2Met1NumberOfCOX=N3PolyGate_COXnum, _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=None, Met1YWidth=PolyGate_YWidth, POXWidth=N3PolyGate_XWidth, POYWidth=PolyGate_YWidth)
        self._DesignParameter['N3PolyGate']['_XYCoordinates'] = N3PolyGate_XYCoordinates

        N4PolyGate_XWidth = abs(self.getXYLeft('N4', '_POLayer')[-1][0] - self.getXYRight('N4', '_POLayer')[0][0])
        N4PolyGate_COXnum = int((N4PolyGate_XWidth - 2 * _DRCObj._Metal1MinEnclosureCO2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)
        N4PolyGate_XYCoordinates = [[self.getXY('N4')[0][0], self.getXYTop('N4', '_ODLayer')[0][1] + _DRCObj._XvtMinEnclosureOfODY + PolyGate_YWidth / 2]]
        self._DesignParameter['N4PolyGate'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0, _DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='N4PolyGateIn{}'.format(_Name)))[0]
        self._DesignParameter['N4PolyGate']['_DesignObj']._CalculateDesignParameter(_ViaPoly2Met1NumberOfCOX=N4PolyGate_COXnum, _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=None, Met1YWidth=PolyGate_YWidth, POXWidth=N4PolyGate_XWidth, POYWidth=PolyGate_YWidth)
        self._DesignParameter['N4PolyGate']['_XYCoordinates'] = N4PolyGate_XYCoordinates

        if N0Dummy_Finger >= 1:
            N0DummyPolyGate_XWidth = abs(self.getXYRight('N0Dummy', '_POLayer')[-1][0] - self.getXYLeft('N0Dummy', '_POLayer')[0][0])
            N0DummyPolyGate_XYCoordinates = [[self.getXY('N0Dummy')[0][0], self.getXYBot('N0Dummy', '_ODLayer')[0][1] - _DRCObj._XvtMinEnclosureOfODY - PolyGate_YWidth / 2]]
            if N0DummyPolyGate_XWidth > 1210:   # By DRC
                N0DummyPolyGate_Met1XWidth = 1210
                N0DummyPolyGate_COXnum = int((N0DummyPolyGate_Met1XWidth - 2 * _DRCObj._Metal1MinEnclosureCO2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)
                self._DesignParameter['N0DummyPolyGate'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0, _DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='N0DummyPolyGateIn{}'.format(_Name)))[0]
                self._DesignParameter['N0DummyPolyGate']['_DesignObj']._CalculateDesignParameter(_ViaPoly2Met1NumberOfCOX=N0DummyPolyGate_COXnum, _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=N0DummyPolyGate_Met1XWidth, Met1YWidth=PolyGate_YWidth, POXWidth=N0DummyPolyGate_XWidth, POYWidth=PolyGate_YWidth)
                self._DesignParameter['N0DummyPolyGate']['_XYCoordinates'] = N0DummyPolyGate_XYCoordinates
            else:
                N0DummyPolyGate_COXnum = int((N0DummyPolyGate_XWidth - 2 * _DRCObj._Metal1MinEnclosureCO2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)
                self._DesignParameter['N0DummyPolyGate'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0, _DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='N0DummyPolyGateIn{}'.format(_Name)))[0]
                self._DesignParameter['N0DummyPolyGate']['_DesignObj']._CalculateDesignParameter(_ViaPoly2Met1NumberOfCOX=N0DummyPolyGate_COXnum, _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=None, Met1YWidth=PolyGate_YWidth, POXWidth=N0DummyPolyGate_XWidth, POYWidth=PolyGate_YWidth)
                self._DesignParameter['N0DummyPolyGate']['_XYCoordinates'] = N0DummyPolyGate_XYCoordinates

        if N1Dummy_Finger >= 1:
            N1DummyPolyGate_XWidth = abs(self.getXYRight('N1Dummy', '_POLayer')[-1][0] - self.getXYLeft('N1Dummy', '_POLayer')[0][0])
            N1DummyPolyGate_XYCoordinates = [[self.getXY('N1Dummy')[0][0], self.getXYBot('N1Dummy', '_ODLayer')[0][1] - _DRCObj._XvtMinEnclosureOfODY - PolyGate_YWidth / 2]]
            if N1DummyPolyGate_XWidth > 1210:   # By DRC
                N1DummyPolyGate_Met1XWidth = 1210
                N1DummyPolyGate_COXnum = int((N1DummyPolyGate_Met1XWidth - 2 * _DRCObj._Metal1MinEnclosureCO2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)
                self._DesignParameter['N1DummyPolyGate'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0, _DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='N1DummyPolyGateIn{}'.format(_Name)))[0]
                self._DesignParameter['N1DummyPolyGate']['_DesignObj']._CalculateDesignParameter(_ViaPoly2Met1NumberOfCOX=N1DummyPolyGate_COXnum, _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=N1DummyPolyGate_Met1XWidth, Met1YWidth=PolyGate_YWidth, POXWidth=N1DummyPolyGate_XWidth, POYWidth=PolyGate_YWidth)
                self._DesignParameter['N1DummyPolyGate']['_XYCoordinates'] = N1DummyPolyGate_XYCoordinates
            else:
                N1DummyPolyGate_COXnum = int((N1DummyPolyGate_XWidth - 2 * _DRCObj._Metal1MinEnclosureCO2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)
                self._DesignParameter['N1DummyPolyGate'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0, _DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='N1DummyPolyGateIn{}'.format(_Name)))[0]
                self._DesignParameter['N1DummyPolyGate']['_DesignObj']._CalculateDesignParameter(_ViaPoly2Met1NumberOfCOX=N1DummyPolyGate_COXnum, _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=None, Met1YWidth=PolyGate_YWidth, POXWidth=N1DummyPolyGate_XWidth, POYWidth=PolyGate_YWidth)
                self._DesignParameter['N1DummyPolyGate']['_XYCoordinates'] = N1DummyPolyGate_XYCoordinates


        # Guardring for NMOS
        NMOSringXWidth = max((abs(self.getXYRight('N3', '_PODummyLayer')[-1][0] - self.getXY('N2')[0][0]) + _DRCObj._MetalxMinSpace41) * 2, CapRes_total_width + _GuardringPPEnclosure * 2)
        NMOSringYWidth = (abs(self.getXYTop('N2PolyGate', '_Met1Layer')[0][1] - self.getXY('N2')[0][1])) * 2 + _DRCObj._MetalxMinSpace41 + 115  # DRC error -> see like dummy -> should be >=110 to act normal Tr
        self._DesignParameter['PSubRing'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=PSubRing_sm.PSubRing(_Name='PSubRingIn{}'.format(_Name)))[0]
        self._DesignParameter['PSubRing']['_DesignObj']._CalculateDesignParameter(_MetalOpen=None, _Height=NMOSringYWidth, _Width=NMOSringXWidth, _Thickness=_GuardringThickness, _COpitch=_GuardringCOpitch, _PPEnclosure=_GuardringPPEnclosure)
        self._DesignParameter['PSubRing']['_XYCoordinates'] = [[self._DesignParameter['N2']['_XYCoordinates'][0][0], self._DesignParameter['N2']['_XYCoordinates'][0][1] + (115 - _DRCObj._MetalxMinSpace41) / 2]]



        print('******************************** PMOS Coordinate setting & Gate contact ********************************')
        PMOS_Ycoordinate = 0
        self._DesignParameter['P1Dummy'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0, _DesignObj=PMOSWithDummy._PMOS(_Name='P1DummyIn{}'.format(_Name)))[0]
        self._DesignParameter['P1Dummy']['_DesignObj']._CalculatePMOSDesignParameter(_PMOSNumberofGate=P1Dummy_Finger, _PMOSChannelWidth=MOS_Width, _PMOSChannellength=ChannelLength, _PMOSDummy=False, _GateSpacing=GateSpacing, _SDWidth=SDWidth, _XVT=XVT)
        self._DesignParameter['P1Dummy']['_XYCoordinates'] = [[0, PMOS_Ycoordinate]]
        self._DesignParameter['P0']['_XYCoordinates'] = \
            [[self.getXY('P1Dummy')[0][0] - (P1Dummy_Finger / 2 + 0.5) * UnitPitch - (P0_Finger / 2 + 0.5) * UnitPitch, PMOS_Ycoordinate]]
        self._DesignParameter['P1']['_XYCoordinates'] = \
            [[self.getXY('P1Dummy')[0][0] + (P1Dummy_Finger / 2 + 0.5) * UnitPitch + (P1_Finger / 2 + 0.5) * UnitPitch, PMOS_Ycoordinate]]

        if P0Dummy_Finger >= 1:
            self._DesignParameter['P0Dummy'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0, _DesignObj=PMOSWithDummy._PMOS(_Name='P0DummyIn{}'.format(_Name)))[0]
            self._DesignParameter['P0Dummy']['_DesignObj']._CalculatePMOSDesignParameter(_PMOSNumberofGate=P0Dummy_Finger, _PMOSChannelWidth=MOS_Width, _PMOSChannellength=ChannelLength, _PMOSDummy=False, _GateSpacing=GateSpacing, _SDWidth=SDWidth, _XVT=XVT)
            self._DesignParameter['P0Dummy']['_XYCoordinates'] = [[self.getXY('P0')[0][0] - (P0_Finger / 2 + 0.5) * UnitPitch - (P0Dummy_Finger / 2 + 0.5) * UnitPitch, PMOS_Ycoordinate]]
            self._DesignParameter['P3']['_XYCoordinates'] = \
                [[self.getXY('P0Dummy')[0][0] - (P0Dummy_Finger / 2 + 0.5) * UnitPitch - (P3_Finger / 2 + 0.5) * UnitPitch, PMOS_Ycoordinate]]

        if P2Dummy_Finger >= 1:
            self._DesignParameter['P2Dummy'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0, _DesignObj=PMOSWithDummy._PMOS(_Name='P2DummyIn{}'.format(_Name)))[0]
            self._DesignParameter['P2Dummy']['_DesignObj']._CalculatePMOSDesignParameter(_PMOSNumberofGate=P2Dummy_Finger, _PMOSChannelWidth=MOS_Width, _PMOSChannellength=ChannelLength, _PMOSDummy=False, _GateSpacing=GateSpacing, _SDWidth=SDWidth, _XVT=XVT)
            self._DesignParameter['P2Dummy']['_XYCoordinates'] = [[self.getXY('P1')[0][0] + (P1_Finger / 2 + 0.5) * UnitPitch + (P2Dummy_Finger / 2 + 0.5) * UnitPitch, PMOS_Ycoordinate]]
            self._DesignParameter['P2']['_XYCoordinates'] = \
                [[self.getXY('P2Dummy')[0][0] + (P2Dummy_Finger / 2 + 0.5) * UnitPitch + (P2_Finger / 2 + 0.5) * UnitPitch, PMOS_Ycoordinate]]


        # PMOS Gate contact
        PolyGate_YWidth = _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByPOAtLeastTwoSide

        P0PolyGate_XWidth = abs(self.getXYLeft('P0', '_POLayer')[-1][0] - self.getXYRight('P0', '_POLayer')[0][0])
        P0PolyGate_COXnum = int((P0PolyGate_XWidth - 2 * _DRCObj._Metal1MinEnclosureCO2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)
        P0PolyGate_XYCoordinates = [[self.getXY('P0')[0][0], self.getXYBot('P0', '_ODLayer')[0][1] - _DRCObj._XvtMinEnclosureOfODY - PolyGate_YWidth / 2]]
        self._DesignParameter['P0PolyGate'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0, _DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='P0PolyGateIn{}'.format(_Name)))[0]
        self._DesignParameter['P0PolyGate']['_DesignObj']._CalculateDesignParameter(_ViaPoly2Met1NumberOfCOX=P0PolyGate_COXnum, _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=None, Met1YWidth=PolyGate_YWidth, POXWidth=P0PolyGate_XWidth, POYWidth=PolyGate_YWidth)
        self._DesignParameter['P0PolyGate']['_XYCoordinates'] = P0PolyGate_XYCoordinates

        P1PolyGate_XWidth = abs(self.getXYRight('P1', '_POLayer')[-1][0] - self.getXYLeft('P1', '_POLayer')[0][0])
        P1PolyGate_COXnum = int((P1PolyGate_XWidth - 2 * _DRCObj._Metal1MinEnclosureCO2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)
        P1PolyGate_XYCoordinates = [[self.getXY('P1')[0][0], self.getXYBot('P1', '_ODLayer')[0][1] - _DRCObj._XvtMinEnclosureOfODY - PolyGate_YWidth / 2]]
        self._DesignParameter['P1PolyGate'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0, _DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='P1PolyGateIn{}'.format(_Name)))[0]
        self._DesignParameter['P1PolyGate']['_DesignObj']._CalculateDesignParameter(_ViaPoly2Met1NumberOfCOX=P1PolyGate_COXnum, _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=None, Met1YWidth=PolyGate_YWidth, POXWidth=P1PolyGate_XWidth, POYWidth=PolyGate_YWidth)
        self._DesignParameter['P1PolyGate']['_XYCoordinates'] = P1PolyGate_XYCoordinates

        P2PolyGate_XWidth = abs(self.getXYRight('P2', '_POLayer')[-1][0] - self.getXYLeft('P2', '_POLayer')[0][0])
        P2PolyGate_COXnum = int((P2PolyGate_XWidth - 2 * _DRCObj._Metal1MinEnclosureCO2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)
        P2PolyGate_XYCoordinates = [[self.getXY('P2')[0][0], self.getXYBot('P2', '_ODLayer')[0][1] - _DRCObj._XvtMinEnclosureOfODY - PolyGate_YWidth / 2]]
        self._DesignParameter['P2PolyGate'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0, _DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='P2PolyGateIn{}'.format(_Name)))[0]
        self._DesignParameter['P2PolyGate']['_DesignObj']._CalculateDesignParameter(_ViaPoly2Met1NumberOfCOX=P2PolyGate_COXnum, _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=None, Met1YWidth=PolyGate_YWidth, POXWidth=P2PolyGate_XWidth, POYWidth=PolyGate_YWidth)
        self._DesignParameter['P2PolyGate']['_XYCoordinates'] = P2PolyGate_XYCoordinates

        P3PolyGate_XWidth = abs(self.getXYLeft('P3', '_POLayer')[-1][0] - self.getXYRight('P3', '_POLayer')[0][0])
        P3PolyGate_COXnum = int((P3PolyGate_XWidth - 2 * _DRCObj._Metal1MinEnclosureCO2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)
        P3PolyGate_XYCoordinates = [[self.getXY('P3')[0][0], self.getXYBot('P3', '_ODLayer')[0][1] - _DRCObj._XvtMinEnclosureOfODY - PolyGate_YWidth / 2]]
        self._DesignParameter['P3PolyGate'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0, _DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='P3PolyGateIn{}'.format(_Name)))[0]
        self._DesignParameter['P3PolyGate']['_DesignObj']._CalculateDesignParameter(_ViaPoly2Met1NumberOfCOX=P3PolyGate_COXnum, _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=None, Met1YWidth=PolyGate_YWidth, POXWidth=P3PolyGate_XWidth, POYWidth=PolyGate_YWidth)
        self._DesignParameter['P3PolyGate']['_XYCoordinates'] = P3PolyGate_XYCoordinates

        if P0Dummy_Finger >= 1:
            P0DummyPolyGate_XWidth = abs(self.getXYRight('P0Dummy', '_POLayer')[-1][0] - self.getXYLeft('P0Dummy', '_POLayer')[0][0])
            P0DummyPolyGate_XYCoordinates = [[self.getXY('P0Dummy')[0][0], self.getXYTop('P0Dummy', '_ODLayer')[0][1] + _DRCObj._XvtMinEnclosureOfODY + PolyGate_YWidth / 2]]
            if P0DummyPolyGate_XWidth > 1210:   # By DRC
                P0DummyPolyGate_Met1XWidth = 1210
                P0DummyPolyGate_COXnum = int((P0DummyPolyGate_Met1XWidth - 2 * _DRCObj._Metal1MinEnclosureCO2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)
                self._DesignParameter['P0DummyPolyGate'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0, _DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='P0DummyPolyGateIn{}'.format(_Name)))[0]
                self._DesignParameter['P0DummyPolyGate']['_DesignObj']._CalculateDesignParameter(_ViaPoly2Met1NumberOfCOX=P0DummyPolyGate_COXnum, _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=P0DummyPolyGate_Met1XWidth, Met1YWidth=PolyGate_YWidth, POXWidth=P0DummyPolyGate_XWidth, POYWidth=PolyGate_YWidth)
                self._DesignParameter['P0DummyPolyGate']['_XYCoordinates'] = P0DummyPolyGate_XYCoordinates
            else:
                P0DummyPolyGate_COXnum = int((P0DummyPolyGate_XWidth - 2 * _DRCObj._Metal1MinEnclosureCO2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)
                self._DesignParameter['P0DummyPolyGate'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0, _DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='P0DummyPolyGateIn{}'.format(_Name)))[0]
                self._DesignParameter['P0DummyPolyGate']['_DesignObj']._CalculateDesignParameter(_ViaPoly2Met1NumberOfCOX=P0DummyPolyGate_COXnum, _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=None, Met1YWidth=PolyGate_YWidth, POXWidth=P0DummyPolyGate_XWidth, POYWidth=PolyGate_YWidth)
                self._DesignParameter['P0DummyPolyGate']['_XYCoordinates'] = P0DummyPolyGate_XYCoordinates

        P1DummyPolyGate_XWidth = abs(self.getXYRight('P1Dummy', '_POLayer')[-1][0] - self.getXYLeft('P1Dummy', '_POLayer')[0][0])
        P1DummyPolyGate_XYCoordinates = [[self.getXY('P1Dummy')[0][0], self.getXYTop('P1Dummy', '_ODLayer')[0][1] + _DRCObj._XvtMinEnclosureOfODY + PolyGate_YWidth / 2]]
        if P1DummyPolyGate_XWidth > 1210:   # By DRC
            P1DummyPolyGate_Met1XWidth = 1210
            P1DummyPolyGate_COXnum = int((P1DummyPolyGate_Met1XWidth - 2 * _DRCObj._Metal1MinEnclosureCO2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)
            self._DesignParameter['P1DummyPolyGate'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0, _DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='P1DummyPolyGateIn{}'.format(_Name)))[0]
            self._DesignParameter['P1DummyPolyGate']['_DesignObj']._CalculateDesignParameter(_ViaPoly2Met1NumberOfCOX=P1DummyPolyGate_COXnum, _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=P1DummyPolyGate_Met1XWidth, Met1YWidth=PolyGate_YWidth, POXWidth=P1DummyPolyGate_XWidth, POYWidth=PolyGate_YWidth)
            self._DesignParameter['P1DummyPolyGate']['_XYCoordinates'] = P1DummyPolyGate_XYCoordinates
        else:
            P1DummyPolyGate_COXnum = int((P1DummyPolyGate_XWidth - 2 * _DRCObj._Metal1MinEnclosureCO2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)
            self._DesignParameter['P1DummyPolyGate'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0, _DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='P1DummyPolyGateIn{}'.format(_Name)))[0]
            self._DesignParameter['P1DummyPolyGate']['_DesignObj']._CalculateDesignParameter(_ViaPoly2Met1NumberOfCOX=P1DummyPolyGate_COXnum, _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=None, Met1YWidth=PolyGate_YWidth, POXWidth=P1DummyPolyGate_XWidth, POYWidth=PolyGate_YWidth)
            self._DesignParameter['P1DummyPolyGate']['_XYCoordinates'] = P1DummyPolyGate_XYCoordinates

        if P2Dummy_Finger >= 1:
            P2DummyPolyGate_XWidth = abs(self.getXYRight('P2Dummy', '_POLayer')[-1][0] - self.getXYLeft('P2Dummy', '_POLayer')[0][0])
            P2DummyPolyGate_XYCoordinates = [[self.getXY('P2Dummy')[0][0], self.getXYTop('P2Dummy', '_ODLayer')[0][1] + _DRCObj._XvtMinEnclosureOfODY + PolyGate_YWidth / 2]]
            if P2DummyPolyGate_XWidth > 1210:   # By DRC
                P2DummyPolyGate_Met1XWidth = 1210
                P2DummyPolyGate_COXnum = int((P2DummyPolyGate_Met1XWidth - 2 * _DRCObj._Metal1MinEnclosureCO2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)
                self._DesignParameter['P2DummyPolyGate'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0, _DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='P2DummyPolyGateIn{}'.format(_Name)))[0]
                self._DesignParameter['P2DummyPolyGate']['_DesignObj']._CalculateDesignParameter(_ViaPoly2Met1NumberOfCOX=P2DummyPolyGate_COXnum, _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=P2DummyPolyGate_Met1XWidth, Met1YWidth=PolyGate_YWidth, POXWidth=P2DummyPolyGate_XWidth, POYWidth=PolyGate_YWidth)
                self._DesignParameter['P2DummyPolyGate']['_XYCoordinates'] = P2DummyPolyGate_XYCoordinates
            else:
                P2DummyPolyGate_COXnum = int((P2DummyPolyGate_XWidth - 2 * _DRCObj._Metal1MinEnclosureCO2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)
                self._DesignParameter['P2DummyPolyGate'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0, _DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='P2DummyPolyGateIn{}'.format(_Name)))[0]
                self._DesignParameter['P2DummyPolyGate']['_DesignObj']._CalculateDesignParameter(_ViaPoly2Met1NumberOfCOX=P2DummyPolyGate_COXnum, _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=None, Met1YWidth=PolyGate_YWidth, POXWidth=P2DummyPolyGate_XWidth, POYWidth=PolyGate_YWidth)
                self._DesignParameter['P2DummyPolyGate']['_XYCoordinates'] = P2DummyPolyGate_XYCoordinates


        # Guardring for PMOS
        PMOSringXWidth = max((abs(self.getXYRight('P2', '_PODummyLayer')[-1][0] - self.getXY('P1Dummy')[0][0]) + _DRCObj._MetalxMinSpace41) * 2, CapRes_total_width + _GuardringPPEnclosure * 2)
        PMOSringYWidth = (abs(self.getXYTop('P1DummyPolyGate', '_Met1Layer')[0][1] - self.getXY('P1Dummy')[0][1])) * 2 + _DRCObj._MetalxMinSpace41 + 115  # DRC error -> see like dummy -> should be >=110 to act normal Tr
        self._DesignParameter['NSubRing'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=NSubRing_sm.NSubRing(_Name='NSubRingIn{}'.format(_Name)))[0]
        self._DesignParameter['NSubRing']['_DesignObj']._CalculateDesignParameter(_MetalOpen=None, _Height=PMOSringYWidth, _Width=PMOSringXWidth, _Thickness=_GuardringThickness, _COpitch=_GuardringCOpitch, _NWEnclosure=_GuardringPPEnclosure)
        self._DesignParameter['NSubRing']['_XYCoordinates'] = [[self._DesignParameter['P1Dummy']['_XYCoordinates'][0][0], self._DesignParameter['P1Dummy']['_XYCoordinates'][0][1] - (115 - _DRCObj._MetalxMinSpace41) / 2]]


        # YCoordinate re-setting
        PMOS_Ycoordinate = self._DesignParameter['PSubRing']['_XYCoordinates'][0][1] + self.getXYTop('PSubRing', 'top', '_Met1Layer')[0][1] + _DRCObj._MetalyMinSpace5 + _GuardringThickness + PMOSringYWidth / 2
        self._DesignParameter['P0']['_XYCoordinates'][0][1] += PMOS_Ycoordinate
        self._DesignParameter['P1']['_XYCoordinates'][0][1] += PMOS_Ycoordinate
        self._DesignParameter['P2']['_XYCoordinates'][0][1] += PMOS_Ycoordinate
        self._DesignParameter['P3']['_XYCoordinates'][0][1] += PMOS_Ycoordinate
        self._DesignParameter['P0Dummy']['_XYCoordinates'][0][1] += PMOS_Ycoordinate
        self._DesignParameter['P1Dummy']['_XYCoordinates'][0][1] += PMOS_Ycoordinate
        self._DesignParameter['P2Dummy']['_XYCoordinates'][0][1] += PMOS_Ycoordinate
        self._DesignParameter['P0PolyGate']['_XYCoordinates'][0][1] += PMOS_Ycoordinate
        self._DesignParameter['P1PolyGate']['_XYCoordinates'][0][1] += PMOS_Ycoordinate
        self._DesignParameter['P2PolyGate']['_XYCoordinates'][0][1] += PMOS_Ycoordinate
        self._DesignParameter['P3PolyGate']['_XYCoordinates'][0][1] += PMOS_Ycoordinate
        self._DesignParameter['P0DummyPolyGate']['_XYCoordinates'][0][1] += PMOS_Ycoordinate
        self._DesignParameter['P1DummyPolyGate']['_XYCoordinates'][0][1] += PMOS_Ycoordinate
        self._DesignParameter['P2DummyPolyGate']['_XYCoordinates'][0][1] += PMOS_Ycoordinate
        self._DesignParameter['NSubRing']['_XYCoordinates'][0][1] += PMOS_Ycoordinate


        # Add XVT, NWELL Layer
        self._DesignParameter['XVTLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping[XVT][0], _Datatype=DesignParameters._LayerMapping[XVT][1],
                                                                             _XWidth=self.getXYRight('P2', '_ODLayer')[0][0] - self.getXYLeft('P3', '_ODLayer')[0][0] + 2 * _DRCObj._XvtMinEnclosureOfODX,
                                                                             _YWidth=self.getYWidth('P2', '_ODLayer') + 2 * _DRCObj._XvtMinEnclosureOfODY,
                                                                             _XYCoordinates=[self._DesignParameter['N2']['_XYCoordinates'][0], self._DesignParameter['P1Dummy']['_XYCoordinates'][0]])

        self._DesignParameter['NWLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                            _XWidth=self.getXYRight('NSubRing', 'top', '_NWLayer')[0][0] - self.getXYLeft('NSubRing', 'top', '_NWLayer')[0][0],
                                                                            _YWidth=self.getXYTop('NSubRing', 'top', '_NWLayer')[0][1] - self.getXYBot('NSubRing', 'bot', '_NWLayer')[0][1],
                                                                            _XYCoordinates=self._DesignParameter['NSubRing']['_XYCoordinates'])



        print('************************************ NCAP & RES Coordinate setting *************************************')
        # Guardring for NCAP & RES
        if _GuardringPPEnclosure != None:
            CapRes_ringYWidth = max(self.getXWidth('NCAP', 'NWELL'), self.getXWidth('RES', '_PRESLayer')) + _GuardringPPEnclosure * 2
            CapRes_Ycoordinate = self.getXYBot('PSubRing', 'bot', '_PPLayer')[0][1] - CapRes_ringYWidth / 2 + _GuardringPPEnclosure
        else:
            if DesignParameters._Technology == 'SS28nm':
                CapRes_ringYWidth = max(self.getXWidth('NCAP', 'NWELL'), self.getXWidth('RES', '_PRESLayer')) + 2 * _DRCObj._PpMinExtensiononPactive2
                CapRes_Ycoordinate = self.getXYBot('PSubRing', 'bot', '_PPLayer')[0][1] - CapRes_ringYWidth / 2 + _DRCObj._PpMinExtensiononPactive2
                if max(self.getXWidth('NCAP', 'NWELL'), self.getXWidth('RES', '_PRESLayer')) < 170:
                    CapRes_ringYWidth = max(self.getXWidth('NCAP', 'NWELL'), self.getXWidth('RES', '_PRESLayer')) + 2 * _DRCObj._PpMinExtensiononPactive2 + 28
                    CapRes_Ycoordinate = self.getXYBot('PSubRing', 'bot', '_PPLayer')[0][1] - CapRes_ringYWidth / 2 + _DRCObj._PpMinExtensiononPactive2 + 28
            else:
                CapRes_ringYWidth = max(self.getXWidth('NCAP', 'NWELL'), self.getXWidth('RES', '_PRESLayer')) + 2 * _DRCObj._PpMinExtensiononPactive
                CapRes_Ycoordinate = self.getXYBot('PSubRing', 'bot', '_PPLayer')[0][1] - CapRes_ringYWidth / 2 + _DRCObj._PpMinExtensiononPactive

        self._DesignParameter['PSubRing_CapRes'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=PSubRing_sm.PSubRing(_Name='PSubRing_CapResIn{}'.format(_Name)))[0]
        self._DesignParameter['PSubRing_CapRes']['_DesignObj']._CalculateDesignParameter(_MetalOpen='top', _Height=CapRes_ringYWidth, _Width=NMOSringXWidth, _Thickness=_GuardringThickness, _COpitch=_GuardringCOpitch, _PPEnclosure=_GuardringPPEnclosure)
        self._DesignParameter['PSubRing_CapRes']['_XYCoordinates'] = [[self._DesignParameter['N2']['_XYCoordinates'][0][0], CapRes_Ycoordinate]]


        # RES & PbodyContact
        RESYcoordinate = CapRes_Ycoordinate + abs(self._DesignParameter['RES']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]
                                                  - self._DesignParameter['RES']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][0]) / 2
        if _GuardringPPEnclosure + _DRCObj._PpMinSpacetoPRES > _DRCObj._RXMinSpacetoPRES:
            self._DesignParameter['RES']['_XYCoordinates'] = [[self._DesignParameter['PSubRing_CapRes']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0]
                                                               - self.getYWidth('PSubRing_CapRes', 'right', '_PPLayer') / 2 - _DRCObj._PpMinSpacetoPRES - self.getYWidth('RES', '_PRESLayer') / 2, RESYcoordinate]]
            self._DesignParameter['PbodyContact']['_XYCoordinates'] = [[self._DesignParameter['RES']['_XYCoordinates'][0][0] - self.getYWidth('RES', '_PRESLayer') / 2
                                                               - _DRCObj._PpMinSpacetoPRES - self.getYWidth('PbodyContact', '_PPLayer') / 2, CapRes_Ycoordinate]]
        else:
            self._DesignParameter['RES']['_XYCoordinates'] = [[self._DesignParameter['PSubRing_CapRes']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0]
                                                               - self.getYWidth('PSubRing_CapRes', 'right', '_ODLayer') / 2 - _DRCObj._RXMinSpacetoPRES - self.getYWidth('RES', '_PRESLayer') / 2, RESYcoordinate]]
            self._DesignParameter['PbodyContact']['_XYCoordinates'] = [[self._DesignParameter['RES']['_XYCoordinates'][0][0] - self.getYWidth('RES', '_PRESLayer') / 2
                                                               - _DRCObj._RXMinSpacetoPRES - self.getYWidth('PbodyContact', '_ODLayer') / 2, CapRes_Ycoordinate]]


        # NCAP
        self._DesignParameter['NCAP']['_XYCoordinates'] = [[(self._DesignParameter['PbodyContact']['_XYCoordinates'][0][0]
                                                             + self._DesignParameter['PSubRing_CapRes']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0]) / 2, CapRes_Ycoordinate]]



        print('********************************************* VSS Routing **********************************************')
        # N2
        self._DesignParameter['_N2VSSRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self.getXWidth('N2', '_Met1Layer'))
        tmp = []
        for i in range(0, N2_Finger // 2 + 1):
            tmp.append([[self.getXY('N2', '_Met1Layer')[2*i][0], self.getXYTop('N2', '_Met1Layer')[2*i][1]], [self.getXY('N2', '_Met1Layer')[2*i][0], self.getXYBot('PSubRing', 'bot', '_Met1Layer')[0][1]]])
        self._DesignParameter['_N2VSSRouting']['_XYCoordinates'] = tmp
        del tmp

        # N3
        self._DesignParameter['_N3VSSRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self.getXWidth('N3', '_Met1Layer'))
        tmp = []
        for i in range(0, N3_Finger // 2 + 1):
            tmp.append([[self.getXY('N3', '_Met1Layer')[2*i][0], self.getXYTop('N3', '_Met1Layer')[2*i][1]], [self.getXY('N3', '_Met1Layer')[2*i][0], self.getXYBot('PSubRing', 'bot', '_Met1Layer')[0][1]]])
        self._DesignParameter['_N3VSSRouting']['_XYCoordinates'] = tmp
        del tmp

        # N4
        self._DesignParameter['_N4VSSRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self.getXWidth('N4', '_Met1Layer'))
        tmp = []
        for i in range(0, N4_Finger // 2 + 1):
            tmp.append([[self.getXY('N4', '_Met1Layer')[2*i][0], self.getXYTop('N4', '_Met1Layer')[2*i][1]], [self.getXY('N4', '_Met1Layer')[2*i][0], self.getXYBot('PSubRing', 'bot', '_Met1Layer')[0][1]]])
        self._DesignParameter['_N4VSSRouting']['_XYCoordinates'] = tmp
        del tmp

        # N0Dummy
        if N0Dummy_Finger >= 1:
            N0DummyVSSWidth = self.getXYRight('N0Dummy', '_Met1Layer')[-1][0] - self.getXYLeft('N0Dummy', '_Met1Layer')[0][0]
            self._DesignParameter['_N0DummyVSSRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=N0DummyVSSWidth)
            self._DesignParameter['_N0DummyVSSRouting']['_XYCoordinates'] = [[[self.getXY('N0Dummy')[0][0], self.getXYBot('N0Dummy', '_Met1Layer')[0][1]],
                                                                              [self.getXY('N0Dummy')[0][0], self.getXYBot('PSubRing', 'bot', '_Met1Layer')[0][1]]]]

        # N1Dummy
        if N1Dummy_Finger >= 1:
            N1DummyVSSWidth = self.getXYRight('N1Dummy', '_Met1Layer')[-1][0] - self.getXYLeft('N1Dummy', '_Met1Layer')[0][0]
            self._DesignParameter['_N1DummyVSSRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=N1DummyVSSWidth)
            self._DesignParameter['_N1DummyVSSRouting']['_XYCoordinates'] = [[[self.getXY('N1Dummy')[0][0], self.getXYBot('N1Dummy', '_Met1Layer')[0][1]],
                                                                              [self.getXY('N1Dummy')[0][0], self.getXYBot('PSubRing', 'bot', '_Met1Layer')[0][1]]]]



        print('********************************************* VDD Routing **********************************************')
        # P0
        self._DesignParameter['_P0VDDRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self.getXWidth('P0', '_Met1Layer'))
        tmp = []
        for i in range(0, int(roundReal(P1_Finger / 2, 0))):
            tmp.append([[self.getXY('P0', '_Met1Layer')[2*i+1][0], self.getXYBot('P0', '_Met1Layer')[2*i+1][1]], [self.getXY('P0', '_Met1Layer')[2*i+1][0], self.getXYTop('NSubRing', 'top', '_Met1Layer')[0][1]]])
        self._DesignParameter['_P0VDDRouting']['_XYCoordinates'] = tmp
        del tmp

        # P1
        self._DesignParameter['_P1VDDRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self.getXWidth('P1', '_Met1Layer'))
        tmp = []
        for i in range(0, int(roundReal(P1_Finger / 2, 0))):
            tmp.append([[self.getXY('P1', '_Met1Layer')[2*i+1][0], self.getXYBot('P1', '_Met1Layer')[2*i+1][1]], [self.getXY('P1', '_Met1Layer')[2*i+1][0], self.getXYTop('NSubRing', 'top', '_Met1Layer')[0][1]]])
        self._DesignParameter['_P1VDDRouting']['_XYCoordinates'] = tmp
        del tmp

        # P2
        self._DesignParameter['_P2VDDRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self.getXWidth('P2', '_Met1Layer'))
        tmp = []
        if P2_Finger % 2 == 0:  # to make output in the rightmost
            for i in range(0, P2_Finger // 2):
                tmp.append([[self.getXY('P2', '_Met1Layer')[2*i+1][0], self.getXYBot('P2', '_Met1Layer')[2*i+1][1]], [self.getXY('P2', '_Met1Layer')[2*i+1][0], self.getXYTop('NSubRing', 'top', '_Met1Layer')[0][1]]])
        else:
            for i in range(0, P2_Finger // 2 + 1):
                tmp.append([[self.getXY('P2', '_Met1Layer')[2*i][0], self.getXYBot('P2', '_Met1Layer')[2*i][1]], [self.getXY('P2', '_Met1Layer')[2*i][0], self.getXYTop('NSubRing', 'top', '_Met1Layer')[0][1]]])
        self._DesignParameter['_P2VDDRouting']['_XYCoordinates'] = tmp
        del tmp

        # P3
        self._DesignParameter['_P3VDDRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self.getXWidth('P3', '_Met1Layer'))
        tmp = []
        for i in range(0, P3_Finger // 2 + 1):
            tmp.append([[self.getXY('P3', '_Met1Layer')[2*i][0], self.getXYBot('P3', '_Met1Layer')[2*i][1]], [self.getXY('P3', '_Met1Layer')[2*i][0], self.getXYTop('NSubRing', 'top', '_Met1Layer')[0][1]]])
        self._DesignParameter['_P3VDDRouting']['_XYCoordinates'] = tmp
        del tmp

        # P0dummy
        P0DummyVDDWidth = self.getXYRight('P0Dummy', '_Met1Layer')[-1][0] - self.getXYLeft('P0Dummy', '_Met1Layer')[0][0]
        self._DesignParameter['_P0DummyVDDRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=P0DummyVDDWidth)
        self._DesignParameter['_P0DummyVDDRouting']['_XYCoordinates'] = [[[self.getXY('P0Dummy')[0][0], self.getXYTop('P0Dummy', '_Met1Layer')[0][1]],
                                                                          [self.getXY('P0Dummy')[0][0], self.getXYTop('NSubRing', 'top', '_Met1Layer')[0][1]]]]

        # P1dummy
        P1DummyVDDWidth = self.getXYRight('P1Dummy', '_Met1Layer')[-1][0] - self.getXYLeft('P1Dummy', '_Met1Layer')[0][0]
        self._DesignParameter['_P1DummyVDDRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=P1DummyVDDWidth)
        self._DesignParameter['_P1DummyVDDRouting']['_XYCoordinates'] = [[[self.getXY('P1Dummy')[0][0], self.getXYTop('P1Dummy', '_Met1Layer')[0][1]],
                                                                          [self.getXY('P1Dummy')[0][0], self.getXYTop('NSubRing', 'top', '_Met1Layer')[0][1]]]]

        # P2dummy
        P2DummyVDDWidth = self.getXYRight('P2Dummy', '_Met1Layer')[-1][0] - self.getXYLeft('P2Dummy', '_Met1Layer')[0][0]
        self._DesignParameter['_P2DummyVDDRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=P2DummyVDDWidth)
        self._DesignParameter['_P2DummyVDDRouting']['_XYCoordinates'] = [[[self.getXY('P2Dummy')[0][0], self.getXYTop('P2Dummy', '_Met1Layer')[0][1]],
                                                                          [self.getXY('P2Dummy')[0][0], self.getXYTop('NSubRing', 'top', '_Met1Layer')[0][1]]]]



        print('********************************************* NCAP Routing *********************************************')
        # RX Metal1 Routing
        self._DesignParameter['_NCAPMet1RXRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=NCAP_YWidth / 2)
        tmp = []
        for i in range(0, NCAP_NumofRX):
            tmp.append([[self._DesignParameter['NCAP']['_XYCoordinates'][0][0] + self._DesignParameter['NCAP']['_DesignObj'].getXY('Viapoly2Met1V')[i][1],
                         self._DesignParameter['NCAP']['_XYCoordinates'][0][1] + self._DesignParameter['NCAP']['_DesignObj'].getXY('Viapoly2Met1V')[i][0]],
                        [self._DesignParameter['NCAP']['_XYCoordinates'][0][0] + self._DesignParameter['NCAP']['_DesignObj'].getXY('Viapoly2Met1V')[NCAP_NumofRX*NCAP_NumofGate+i][1],
                         self._DesignParameter['NCAP']['_XYCoordinates'][0][1] + self._DesignParameter['NCAP']['_DesignObj'].getXY('Viapoly2Met1V')[NCAP_NumofRX*NCAP_NumofGate+i][0]]])
        self._DesignParameter['_NCAPMet1RXRouting']['_XYCoordinates'] = tmp
        del tmp

        # Poly gate Metal1 Routing
        self._DesignParameter['_NCAPMet1PolyRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self.getYWidth('NCAP', 'Viapoly2Met1H', '_Met1Layer'))
        tmp = []
        for i in range(0, NCAP_NumofRX + 1):
            tmp.append([[self._DesignParameter['NCAP']['_XYCoordinates'][0][0] + self._DesignParameter['NCAP']['_DesignObj'].getXY('Viapoly2Met1H')[i][1],
                         self._DesignParameter['NCAP']['_XYCoordinates'][0][1] + self._DesignParameter['NCAP']['_DesignObj'].getXY('Viapoly2Met1H')[i][0]],
                        [self._DesignParameter['NCAP']['_XYCoordinates'][0][0] + self._DesignParameter['NCAP']['_DesignObj'].getXY('Viapoly2Met1H')[NCAP_NumofRX + i + 1][1],
                         self._DesignParameter['NCAP']['_XYCoordinates'][0][1] + self._DesignParameter['NCAP']['_DesignObj'].getXY('Viapoly2Met1H')[NCAP_NumofRX + i + 1][0]]])
        self._DesignParameter['_NCAPMet1PolyRouting']['_XYCoordinates'] = tmp
        del tmp

        # RX Metal1 to Metal2 via gen.
        NCAPViaRX_XWidth = self._DesignParameter['_NCAPMet1RXRouting']['_Width']
        NCAPViaRX_COXnum = int((NCAPViaRX_XWidth - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) + 1)
        tmp = []
        for i in range(0, len(self._DesignParameter['NCAP']['_DesignObj']._DesignParameter['Viapoly2Met1V']['_XYCoordinates'])):
            tmp.append([self._DesignParameter['NCAP']['_XYCoordinates'][0][0] + self._DesignParameter['NCAP']['_DesignObj'].getXY('Viapoly2Met1V')[i][1],
                        self._DesignParameter['NCAP']['_XYCoordinates'][0][1] + self._DesignParameter['NCAP']['_DesignObj'].getXY('Viapoly2Met1V')[i][0]])
        self._DesignParameter['NCAPViaRX'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='NCAPViaRXIn{}'.format(_Name)))[0]
        self._DesignParameter['NCAPViaRX']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=NCAPViaRX_COXnum, _ViaMet12Met2NumberOfCOY=1)
        self._DesignParameter['NCAPViaRX']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self.getXWidth('NCAP', 'Viapoly2Met1V', '_Met1Layer')
        self._DesignParameter['NCAPViaRX']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self.getXWidth('NCAP', 'Viapoly2Met1V', '_Met1Layer')
        self._DesignParameter['NCAPViaRX']['_XYCoordinates'] = tmp
        del tmp

        # RX Metal2 Routing
        self._DesignParameter['_NCAPMet2RXRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=self.getYWidth('NCAPViaRX', '_Met2Layer'))
        tmp = []
        for i in range(0, NCAP_NumofGate + 1):
            tmp.append([[self.getXYLeft('NCAPViaRX', '_Met2Layer')[NCAP_NumofRX * i][0], self.getXY('NCAPViaRX', '_Met2Layer')[NCAP_NumofRX * i][1]],
                        [self.getXYRight('NCAPViaRX', '_Met2Layer')[NCAP_NumofRX * (i + 1) - 1][0], self.getXY('NCAPViaRX', '_Met2Layer')[NCAP_NumofRX * (i + 1) - 1][1]]])
        self._DesignParameter['_NCAPMet2RXRouting']['_XYCoordinates'] = tmp
        del tmp

        # Poly gate Metal1 to Metal2 via gen.
        NCAPViaPoly_YWidth = NCAP_XWidth / 2
        NCAPViaPoly_COYnum = int((NCAPViaPoly_YWidth - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) + 1)
        tmp = []
        for i in range(0, len(self._DesignParameter['NCAP']['_DesignObj']._DesignParameter['Viapoly2Met1H']['_XYCoordinates'])):
            tmp.append([self._DesignParameter['NCAP']['_XYCoordinates'][0][0] + self._DesignParameter['NCAP']['_DesignObj'].getXY('Viapoly2Met1H')[i][1],
                        self._DesignParameter['NCAP']['_XYCoordinates'][0][1] + self._DesignParameter['NCAP']['_DesignObj'].getXY('Viapoly2Met1H')[i][0]])
        self._DesignParameter['NCAPViaPoly'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='NCAPViaPolyIn{}'.format(_Name)))[0]
        self._DesignParameter['NCAPViaPoly']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=NCAPViaPoly_COYnum)
        self._DesignParameter['NCAPViaPoly']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self.getYWidth('NCAP', 'Viapoly2Met1H', '_Met1Layer')
        self._DesignParameter['NCAPViaPoly']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = self.getYWidth('NCAP', 'Viapoly2Met1H', '_Met1Layer')
        self._DesignParameter['NCAPViaPoly']['_XYCoordinates'] = tmp
        del tmp

        # Poly gate Metal2 Routing
        self._DesignParameter['_NCAPMet2PolyRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=self.getYWidth('NCAPViaPoly', '_Met2Layer'))
        tmp = []
        for i in range(0, NCAP_NumofGate):
            tmp.append([[self.getXYLeft('NCAPViaPoly', '_Met2Layer')[(NCAP_NumofRX + 1) * i][0], self.getXY('NCAPViaPoly', '_Met2Layer')[(NCAP_NumofRX + 1) * i][1]],
                        [self.getXYRight('NCAPViaPoly', '_Met2Layer')[(NCAP_NumofRX + 1) * (i + 1) - 1][0], self.getXY('NCAPViaPoly', '_Met2Layer')[(NCAP_NumofRX + 1) * (i + 1) - 1][1]]])
        self._DesignParameter['_NCAPMet2PolyRouting']['_XYCoordinates'] = tmp
        del tmp



        print('********************************************** VB Routing **********************************************')
        # N4 Gate - Drain (M1)
        self._DesignParameter['_VBMet1Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=SDWidth)
        tmp = []
        for i in range(0, int(roundReal(N4_Finger / 2, 0))):
            tmp.append([[self.getXY('N4', '_Met1Layer')[2*i+1][0], self.getXYBot('N4', '_Met1Layer')[2*i+1][1]], [self.getXY('N4', '_Met1Layer')[2*i+1][0], self.getXYTop('N4PolyGate', '_Met1Layer')[0][1]]])
        self._DesignParameter['_VBMet1Routing']['_XYCoordinates'] = tmp

        if len(tmp) > N4_Finger // 2:
            self._DesignParameter['N4PolyGate_Met1Add'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self.getYWidth('N4PolyGate', '_Met1Layer'))
            self._DesignParameter['N4PolyGate_Met1Add']['_XYCoordinates'] = [[[self.getXYLeft('N4PolyGate', '_Met1Layer')[0][0], self.getXY('N4PolyGate', '_Met1Layer')[0][1]],
                                                                              [self.getXYRight('N4', '_Met1Layer')[-1][0], self.getXY('N4PolyGate', '_Met1Layer')[0][1]]]]
        del tmp

        # P3 Gate - Drain (M1)
        tmp = []
        for i in range(0, int(roundReal(P3_Finger / 2, 0))):
            tmp.append([[self.getXY('P3', '_Met1Layer')[2*i+1][0], self.getXYTop('P3', '_Met1Layer')[2*i+1][1]], [self.getXY('P3', '_Met1Layer')[2*i+1][0], self.getXYBot('P3PolyGate', '_Met1Layer')[0][1]]])
        self._DesignParameter['_VBMet1Routing']['_XYCoordinates'] += tmp

        if len(tmp) > P3_Finger // 2:
            self._DesignParameter['P3PolyGate_Met1Add'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self.getYWidth('P3PolyGate', '_Met1Layer'))
            self._DesignParameter['P3PolyGate_Met1Add']['_XYCoordinates'] = [[[self.getXYLeft('P3PolyGate', '_Met1Layer')[0][0], self.getXY('P3PolyGate', '_Met1Layer')[0][1]],
                                                                              [self.getXYRight('P3', '_Met1Layer')[-1][0], self.getXY('P3PolyGate', '_Met1Layer')[0][1]]]]
        del tmp

        # N4 Gate - P3 Gate (M3)
        # if N4PolyGate_XWidth >= P3PolyGate_XWidth:
        #     _VBMet3Routing_Width = P3PolyGate_XWidth
        #     _VBMet3Routing_XCoord = self.getXY('P3PolyGate')[0][0]
        # else:
        #     _VBMet3Routing_Width = P3PolyGate_XWidth
        #     _VBMet3Routing_XCoord = self.getXY('N4PolyGate')[0][0]
        # _VBMet3Routing_COXnum = int((_VBMet3Routing_Width - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) + 1)
        #
        # self._DesignParameter['_VBMet12Met2Via'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_VBMet12Met2ViaIn{}'.format(_Name)))[0]
        # self._DesignParameter['_VBMet12Met2Via']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=_VBMet3Routing_COXnum, _ViaMet12Met2NumberOfCOY=1)
        # self._DesignParameter['_VBMet12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = _VBMet3Routing_Width
        # self._DesignParameter['_VBMet12Met2Via']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = _VBMet3Routing_Width
        # self._DesignParameter['_VBMet12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self.getYWidth('N4PolyGate', '_Met1Layer')
        # self._DesignParameter['_VBMet12Met2Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self._DesignParameter['_VBMet12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        # self._DesignParameter['_VBMet12Met2Via']['_XYCoordinates'] = [[_VBMet3Routing_XCoord, self.getXY('N4PolyGate')[0][1]], [_VBMet3Routing_XCoord, self.getXY('P3PolyGate')[0][1]]]
        #
        # self._DesignParameter['_VBMet22Met3Via'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='_VBMet22Met3ViaIn{}'.format(_Name)))[0]
        # self._DesignParameter['_VBMet22Met3Via']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=_VBMet3Routing_COXnum, _ViaMet22Met3NumberOfCOY=1)
        # self._DesignParameter['_VBMet22Met3Via']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = _VBMet3Routing_Width
        # self._DesignParameter['_VBMet22Met3Via']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = _VBMet3Routing_Width
        # self._DesignParameter['_VBMet22Met3Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self._DesignParameter['_VBMet12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        # self._DesignParameter['_VBMet22Met3Via']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = self._DesignParameter['_VBMet12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        # self._DesignParameter['_VBMet22Met3Via']['_XYCoordinates'] = self._DesignParameter['_VBMet12Met2Via']['_XYCoordinates']
        #
        # self._DesignParameter['_VBMet3Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=self.getXWidth('_VBMet22Met3Via', '_Met3Layer'))
        # self._DesignParameter['_VBMet3Routing']['_XYCoordinates'] = [self.getXY('_VBMet22Met3Via')]

        if N4PolyGate_XWidth >= P3PolyGate_XWidth:
            _VBMet3Routing_XCoord = self.getXY('P3PolyGate')[0][0]
        else:
            _VBMet3Routing_XCoord = self.getXY('N4PolyGate')[0][0]
        self._DesignParameter['_VBMet12Met2Via'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_VBMet12Met2ViaIn{}'.format(_Name)))[0]
        self._DesignParameter['_VBMet12Met2Via']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1)
        self._DesignParameter['_VBMet12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self.getYWidth('N4PolyGate', '_Met1Layer')
        self._DesignParameter['_VBMet12Met2Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self._DesignParameter['_VBMet12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        self._DesignParameter['_VBMet12Met2Via']['_XYCoordinates'] = [[_VBMet3Routing_XCoord, self.getXY('N4PolyGate')[0][1]], [_VBMet3Routing_XCoord, self.getXY('P3PolyGate')[0][1]]]

        self._DesignParameter['_VBMet22Met3Via'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='_VBMet22Met3ViaIn{}'.format(_Name)))[0]
        self._DesignParameter['_VBMet22Met3Via']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=1)
        self._DesignParameter['_VBMet22Met3Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self._DesignParameter['_VBMet12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        self._DesignParameter['_VBMet22Met3Via']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = self._DesignParameter['_VBMet12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        self._DesignParameter['_VBMet22Met3Via']['_XYCoordinates'] = [self._DesignParameter['_VBMet12Met2Via']['_XYCoordinates'][0], self._DesignParameter['_VBMet12Met2Via']['_XYCoordinates'][1]]

        self._DesignParameter['_VBMet3Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=_DRCObj._MetalxMinWidth)
        self._DesignParameter['_VBMet3Routing']['_XYCoordinates'] = [[[self.getXY('_VBMet22Met3Via')[0][0], self.getXYBot('_VBMet22Met3Via', '_Met3Layer')[0][1]], [self.getXY('_VBMet22Met3Via')[1][0], self.getXYTop('_VBMet22Met3Via', '_Met3Layer')[1][1]]]]

        # mid (M2)
        _VBMet2Routing_YCoord = (self.getXY('NSubRing')[0][1] - self.getXY('PSubRing')[0][1]) / 2
        self._DesignParameter['_VBMet2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_DRCObj._MetalxMinWidth)
        self._DesignParameter['_VBMet2Routing']['_XYCoordinates'] = [[[self.getXY('_VBMet22Met3Via')[0][0] - _DRCObj._MetalxMinWidth / 2, _VBMet2Routing_YCoord], [self.getXY('N3PolyGate')[0][0] + _DRCObj._MetalxMinWidth / 2, _VBMet2Routing_YCoord]]]
        self._DesignParameter['_VBMet32Met2Via'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=90, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='_VBMet32Met2ViaIn{}'.format(_Name)))[0]
        self._DesignParameter['_VBMet32Met2Via']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=1)
        self._DesignParameter['_VBMet32Met2Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self.getWidth('_VBMet3Routing')
        self._DesignParameter['_VBMet32Met2Via']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = self.getWidth('_VBMet3Routing')
        self._DesignParameter['_VBMet32Met2Via']['_XYCoordinates'] = [[self._DesignParameter['_VBMet3Routing']['_XYCoordinates'][0][0][0], _VBMet2Routing_YCoord]]

        # mid - N2 Gate (M2)
        self._DesignParameter['_VBMet12Met2Via']['_XYCoordinates'].append(self.getXY('N2PolyGate')[0])
        self._DesignParameter['_VBMet2Routing']['_XYCoordinates'].append([[self.getXY('N2PolyGate')[0][0], self.getXY('N2PolyGate')[0][1] - self.getYWidth('_VBMet12Met2Via', '_Met2Layer') / 2],
                                                                          [self.getXY('N2PolyGate')[0][0], _VBMet2Routing_YCoord + self.getWidth('_VBMet2Routing') / 2]])

        # mid - N3 Gate (M2)
        self._DesignParameter['_VBMet12Met2Via']['_XYCoordinates'].append(self.getXY('N3PolyGate')[0])
        self._DesignParameter['_VBMet2Routing']['_XYCoordinates'].append([[self.getXY('N3PolyGate')[0][0], self.getXY('N3PolyGate')[0][1] - self.getYWidth('_VBMet12Met2Via', '_Met2Layer') / 2],
                                                                          [self.getXY('N3PolyGate')[0][0], _VBMet2Routing_YCoord + self.getWidth('_VBMet2Routing') / 2]])



        print('********************************************** Tr Routing **********************************************')
        # N0,N1 Source - N2 Drain (M2)
        self._DesignParameter['_InSN2DMet12Met2Via'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=90, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_InSN2DMet12Met2ViaIn{}'.format(_Name)))[0]
        self._DesignParameter['_InSN2DMet12Met2Via']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1)
        self._DesignParameter['_InSN2DMet12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self.getXWidth('N2', '_Met1Layer')
        self._DesignParameter['_InSN2DMet12Met2Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self._DesignParameter['_InSN2DMet12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        tmp = []
        for i in range(0, int(roundReal(N0_Finger / 2, 0))):
            tmp.append([self.getXY('N0', '_Met1Layer')[2 * i + 1][0], self.getXYBot('N0', '_Met1Layer')[2 * i + 1][1] + self.getXWidth('_InSN2DMet12Met2Via', '_Met2Layer') / 2])
        for i in range(0, int(roundReal(N2_Finger / 2, 0))):
            tmp.append([self.getXY('N2', '_Met1Layer')[2 * i + 1][0], self.getXYBot('N2', '_Met1Layer')[2 * i + 1][1] + self.getXWidth('_InSN2DMet12Met2Via', '_Met2Layer') / 2])
        for i in range(0, int(roundReal(N1_Finger / 2, 0))):
            tmp.append([self.getXY('N1', '_Met1Layer')[2 * i + 1][0], self.getXYBot('N1', '_Met1Layer')[2 * i + 1][1] + self.getXWidth('_InSN2DMet12Met2Via', '_Met2Layer') / 2])
        self._DesignParameter['_InSN2DMet12Met2Via']['_XYCoordinates'] = tmp
        self._DesignParameter['_InSN2DMet12Met2Via']['_XYCoordinates'].sort()
        del tmp

        self._DesignParameter['_InSN2DMet2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_DRCObj._MetalxMinWidth)
        self._DesignParameter['_InSN2DMet2Routing']['_XYCoordinates'] = [[self._DesignParameter['_InSN2DMet12Met2Via']['_XYCoordinates'][0], self._DesignParameter['_InSN2DMet12Met2Via']['_XYCoordinates'][-1]]]


        # N0 Drain - P0 Gate (M3) - P0 Drain
        self._DesignParameter['_N0Met12Met2Via'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=90, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_N0Met12Met2ViaIn{}'.format(_Name)))[0]
        self._DesignParameter['_N0Met12Met2Via']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1)
        self._DesignParameter['_N0Met12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self.getXWidth('N2', '_Met1Layer')
        self._DesignParameter['_N0Met12Met2Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self._DesignParameter['_N0Met12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        self._DesignParameter['_N0Met22Met3Via'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=90, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='_N0Met22Met3ViaIn{}'.format(_Name)))[0]
        self._DesignParameter['_N0Met22Met3Via']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=1)
        self._DesignParameter['_N0Met22Met3Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self.getXWidth('N0', '_Met1Layer')
        self._DesignParameter['_N0Met22Met3Via']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = self._DesignParameter['_N0Met22Met3Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
        tmp = []
        for i in range(0, N0_Finger // 2 + 1):
            tmp.append([self.getXY('N0', '_Met1Layer')[2 * i][0], self.getXYTop('N0', '_Met1Layer')[2 * i][1] - self.getXWidth('_N0Met22Met3Via', '_Met2Layer') / 2])
        self._DesignParameter['_N0Met12Met2Via']['_XYCoordinates'] = tmp
        self._DesignParameter['_N0Met22Met3Via']['_XYCoordinates'] = tmp
        del tmp

        self._DesignParameter['_N1Met12Met2Via'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=90, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_N1Met12Met2ViaIn{}'.format(_Name)))[0]
        self._DesignParameter['_N1Met12Met2Via']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1)
        self._DesignParameter['_N1Met12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self.getXWidth('N2', '_Met1Layer')
        self._DesignParameter['_N1Met12Met2Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self._DesignParameter['_N1Met12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        self._DesignParameter['_N1Met22Met3Via'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=90, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='_N1Met22Met3ViaIn{}'.format(_Name)))[0]
        self._DesignParameter['_N1Met22Met3Via']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=1)
        self._DesignParameter['_N1Met22Met3Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self.getXWidth('N0', '_Met1Layer')
        self._DesignParameter['_N1Met22Met3Via']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = self._DesignParameter['_N1Met22Met3Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
        tmp = []
        for i in range(0, N1_Finger // 2 + 1):
            tmp.append([self.getXY('N1', '_Met1Layer')[2 * i][0], self.getXYTop('N1', '_Met1Layer')[2 * i][1] - self.getXWidth('_N1Met22Met3Via', '_Met2Layer') / 2])
        self._DesignParameter['_N1Met12Met2Via']['_XYCoordinates'] = tmp
        self._DesignParameter['_N1Met22Met3Via']['_XYCoordinates'] = tmp
        del tmp

        self._DesignParameter['_N0N1Met3Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=_DRCObj._MetalxMinWidth)
        self._DesignParameter['_N0N1Met3Routing']['_XYCoordinates'] = [[self._DesignParameter['_N0Met22Met3Via']['_XYCoordinates'][0], self._DesignParameter['_N0Met22Met3Via']['_XYCoordinates'][-1]],
                                                                       [self._DesignParameter['_N1Met22Met3Via']['_XYCoordinates'][0], self._DesignParameter['_N1Met22Met3Via']['_XYCoordinates'][-1]],
                                                                       [self._DesignParameter['_N0Met22Met3Via']['_XYCoordinates'][0], [self._DesignParameter['_N0Met22Met3Via']['_XYCoordinates'][0][0], self.getXY('P0PolyGate')[0][1]]]]

        self._DesignParameter['_P0Met32Met2Via'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='_P0Met32Met2ViaIn{}'.format(_Name)))[0]
        self._DesignParameter['_P0Met32Met2Via']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=1)
        self._DesignParameter['_P0Met32Met2Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self.getYWidth('P0PolyGate', '_Met1Layer')
        self._DesignParameter['_P0Met32Met2Via']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = self._DesignParameter['_P0Met32Met2Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
        self._DesignParameter['_P0Met32Met2Via']['_XYCoordinates'] = [self._DesignParameter['_N0N1Met3Routing']['_XYCoordinates'][-1][-1]]

        self._DesignParameter['_P0Met22Met1Via'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_P0Met22Met1ViaIn{}'.format(_Name)))[0]
        self._DesignParameter['_P0Met22Met1Via']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1)
        self._DesignParameter['_P0Met22Met1Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self.getYWidth('P0PolyGate', '_Met1Layer')
        self._DesignParameter['_P0Met22Met1Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self._DesignParameter['_P0Met22Met1Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        self._DesignParameter['_P0Met22Met1Via']['_XYCoordinates'] = self._DesignParameter['_P0Met32Met2Via']['_XYCoordinates']


        # P0 Gate - P1 Gate (M1)
        self._DesignParameter['_P0P1Met1Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self.getYWidth('P0PolyGate', '_Met1Layer'))
        self._DesignParameter['_P0P1Met1Routing']['_XYCoordinates'] = [[self.getXYLeft('P0PolyGate', '_Met1Layer')[0], self.getXYRight('P1PolyGate', '_Met1Layer')[0]]]


        # P0 Drain, P1 Drain (M2)
        self._DesignParameter['_P0Met12Met2Via'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=90, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_P0Met12Met2ViaIn{}'.format(_Name)))[0]
        self._DesignParameter['_P0Met12Met2Via']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1)
        self._DesignParameter['_P0Met12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self.getXWidth('P0', '_Met1Layer')
        self._DesignParameter['_P0Met12Met2Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self._DesignParameter['_P0Met12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        tmp = []
        for i in range(0, P0_Finger // 2 + 1):
            tmp.append(self.getXY('P0', '_Met1Layer')[2 * i])
        self._DesignParameter['_P0Met12Met2Via']['_XYCoordinates'] = tmp
        del tmp

        self._DesignParameter['_P1Met12Met2Via'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=90, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_P1Met12Met2ViaIn{}'.format(_Name)))[0]
        self._DesignParameter['_P1Met12Met2Via']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1)
        self._DesignParameter['_P1Met12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self.getXWidth('P0', '_Met1Layer')
        self._DesignParameter['_P1Met12Met2Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self._DesignParameter['_P1Met12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        tmp = []
        for i in range(0, P1_Finger // 2 + 1):
            tmp.append(self.getXY('P1', '_Met1Layer')[2 * i])
        self._DesignParameter['_P1Met12Met2Via']['_XYCoordinates'] = tmp
        del tmp

        self._DesignParameter['_P0Met2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_DRCObj._MetalxMinWidth)
        self._DesignParameter['_P0Met2Routing']['_XYCoordinates'] = [[self._DesignParameter['_P0Met12Met2Via']['_XYCoordinates'][0], self._DesignParameter['_P0Met12Met2Via']['_XYCoordinates'][-1]],
                                                                     [self._DesignParameter['_P0Met12Met2Via']['_XYCoordinates'][0], self._DesignParameter['_P0Met32Met2Via']['_XYCoordinates'][0]]]

        self._DesignParameter['_P1Met2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_DRCObj._MetalxMinWidth)
        self._DesignParameter['_P1Met2Routing']['_XYCoordinates'] = [[self._DesignParameter['_P1Met12Met2Via']['_XYCoordinates'][0], self._DesignParameter['_P1Met12Met2Via']['_XYCoordinates'][-1]]]


        # P1 Drain - N1 Drain (M3)
        self._DesignParameter['_P1Met22Met3Via'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=90, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='_P1Met22Met3ViaIn{}'.format(_Name)))[0]
        self._DesignParameter['_P1Met22Met3Via']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=1)
        self._DesignParameter['_P1Met22Met3Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self.getXWidth('P1', '_Met1Layer')
        self._DesignParameter['_P1Met22Met3Via']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = self._DesignParameter['_P1Met22Met3Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
        self._DesignParameter['_P1Met22Met3Via']['_XYCoordinates'] = [self._DesignParameter['_P1Met12Met2Via']['_XYCoordinates'][0]]

        self._DesignParameter['_P1Met3Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=_DRCObj._MetalxMinWidth)
        self._DesignParameter['_P1Met3Routing']['_XYCoordinates'] = [[self._DesignParameter['_P1Met22Met3Via']['_XYCoordinates'][0], self._DesignParameter['_N1Met22Met3Via']['_XYCoordinates'][0]]]


        # P2 Gate - N1 Drain (M3)
        self._DesignParameter['_P2Met12Met2Via'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_P2Met12Met2ViaIn{}'.format(_Name)))[0]
        self._DesignParameter['_P2Met12Met2Via']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1)
        self._DesignParameter['_P2Met12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self.getYWidth('N4PolyGate', '_Met1Layer')
        self._DesignParameter['_P2Met12Met2Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self._DesignParameter['_P2Met12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        self._DesignParameter['_P2Met12Met2Via']['_XYCoordinates'] = [[self.getXYLeft('P2PolyGate', '_Met1Layer')[0][0] + self.getXWidth('_P2Met12Met2Via', '_Met2Layer') / 2, self.getXY('P2PolyGate')[0][1]]]

        self._DesignParameter['_P2Met22Met3Via'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='_P2Met22Met3ViaIn{}'.format(_Name)))[0]
        self._DesignParameter['_P2Met22Met3Via']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=1)
        self._DesignParameter['_P2Met22Met3Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self._DesignParameter['_P2Met12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        self._DesignParameter['_P2Met22Met3Via']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = self._DesignParameter['_P2Met12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        self._DesignParameter['_P2Met22Met3Via']['_XYCoordinates'] = self._DesignParameter['_P2Met12Met2Via']['_XYCoordinates']

        self._DesignParameter['_P2Met3Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=_DRCObj._MetalxMinWidth)
        self._DesignParameter['_P2Met3Routing']['_XYCoordinates'] = [[self._DesignParameter['_P2Met22Met3Via']['_XYCoordinates'][0],
                                                                      [self._DesignParameter['_P2Met22Met3Via']['_XYCoordinates'][0][0], self._DesignParameter['_N1Met22Met3Via']['_XYCoordinates'][-1][1] - self.getWidth('_P2Met3Routing') / 2]],
                                                                     [[self._DesignParameter['_P2Met22Met3Via']['_XYCoordinates'][0][0], self._DesignParameter['_N1Met22Met3Via']['_XYCoordinates'][-1][1]],
                                                                      self._DesignParameter['_N1Met22Met3Via']['_XYCoordinates'][-1]]]


        # P2 Drain - N3 Drain (M3) (OUT)
        self._DesignParameter['_P2DMet12Met2Via'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=90, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_P2DMet12Met2ViaIn{}'.format(_Name)))[0]
        self._DesignParameter['_P2DMet12Met2Via']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1)
        self._DesignParameter['_P2DMet12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self.getXWidth('P2', '_Met1Layer')
        self._DesignParameter['_P2DMet12Met2Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self._DesignParameter['_P2DMet12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        tmp = []
        for i in range(0, int(roundReal(P2_Finger / 2, 0))):
            tmp.append(self.getXY('P2', '_Met1Layer')[2 * i + 1])
        self._DesignParameter['_P2DMet12Met2Via']['_XYCoordinates'] = tmp
        del tmp

        self._DesignParameter['_P2DMet2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_DRCObj._MetalxMinWidth)
        self._DesignParameter['_P2DMet2Routing']['_XYCoordinates'] = [[self._DesignParameter['_P2DMet12Met2Via']['_XYCoordinates'][0], self._DesignParameter['_P2DMet12Met2Via']['_XYCoordinates'][-1]]]

        self._DesignParameter['_N3DMet12Met2Via'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=90, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_N3DMet12Met2ViaIn{}'.format(_Name)))[0]
        self._DesignParameter['_N3DMet12Met2Via']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1)
        self._DesignParameter['_N3DMet12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self.getXWidth('N3', '_Met1Layer')
        self._DesignParameter['_N3DMet12Met2Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self._DesignParameter['_N3DMet12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        tmp = []
        for i in range(0, int(roundReal(N3_Finger / 2, 0))):
            tmp.append(self.getXY('N3', '_Met1Layer')[2 * i + 1])
        self._DesignParameter['_N3DMet12Met2Via']['_XYCoordinates'] = tmp
        del tmp

        self._DesignParameter['_N3DMet2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_DRCObj._MetalxMinWidth)
        self._DesignParameter['_N3DMet2Routing']['_XYCoordinates'] = [[self._DesignParameter['_N3DMet12Met2Via']['_XYCoordinates'][0], self._DesignParameter['_N3DMet12Met2Via']['_XYCoordinates'][-1]]]

        self._DesignParameter['_OUTMet22Met3Via'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=90, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='_OUTMet22Met3ViaIn{}'.format(_Name)))[0]
        self._DesignParameter['_OUTMet22Met3Via']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=1)
        self._DesignParameter['_OUTMet22Met3Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self._DesignParameter['_N3DMet12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        self._DesignParameter['_OUTMet22Met3Via']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = self._DesignParameter['_OUTMet22Met3Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
        self._DesignParameter['_OUTMet22Met3Via']['_XYCoordinates'] = [self._DesignParameter['_P2DMet12Met2Via']['_XYCoordinates'][-1], self._DesignParameter['_N3DMet12Met2Via']['_XYCoordinates'][-1]]

        self._DesignParameter['_OUTMet3Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=_DRCObj._MetalxMinWidth)
        self._DesignParameter['_OUTMet3Routing']['_XYCoordinates'] = [[self._DesignParameter['_OUTMet22Met3Via']['_XYCoordinates'][0], self._DesignParameter['_OUTMet22Met3Via']['_XYCoordinates'][-1]]]



        print('****************************************** NCAP & RES Routing ******************************************')
        # NCAP - Resistor
        self._DesignParameter['_NCAP2RESMet2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=self.getWidth('_NCAPMet2RXRouting'))
        self._DesignParameter['_NCAP2RESMet2Routing']['_XYCoordinates'] = [[self.getXY('_NCAPMet2RXRouting')[0][0],
                                                                            [self._DesignParameter['RES']['_XYCoordinates'][0][0] + self._DesignParameter['RES']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][1] + self.getYWidth('RES', '_Met1Layer') / 2,
                                                                             self.getXY('_NCAPMet2RXRouting')[0][0][1]]]]

        self._DesignParameter['_NCAP2RESMet1Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self.getYWidth('RES', '_Met1Layer'))
        self._DesignParameter['_NCAP2RESMet1Routing']['_XYCoordinates'] = [[[self._DesignParameter['RES']['_XYCoordinates'][0][0] + self._DesignParameter['RES']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][1],
                                                                             self.getXY('_NCAPMet2RXRouting')[0][0][1] - self.getWidth('_NCAPMet2RXRouting') / 2],
                                                                            [self._DesignParameter['RES']['_XYCoordinates'][0][0] + self._DesignParameter['RES']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][1],
                                                                             self._DesignParameter['RES']['_XYCoordinates'][0][1] - abs(self._DesignParameter['RES']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0])]]]

        self._DesignParameter['_NCAP2RESVia'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_NCAP2RESViaIn{}'.format(_Name)))[0]
        self._DesignParameter['_NCAP2RESVia']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1)
        self._DesignParameter['_NCAP2RESVia']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self.getWidth('_NCAP2RESMet2Routing')
        self._DesignParameter['_NCAP2RESVia']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self._DesignParameter['_NCAP2RESVia']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        self._DesignParameter['_NCAP2RESVia']['_XYCoordinates'] = [[self._DesignParameter['_NCAP2RESMet2Routing']['_XYCoordinates'][0][1][0] - self.getXWidth('_NCAP2RESVia', '_Met1Layer') / 2, self._DesignParameter['_NCAP2RESMet2Routing']['_XYCoordinates'][0][1][1]]]


        # OUT - RES
        self._DesignParameter['_OUTMet3Routing']['_XYCoordinates'].append([self._DesignParameter['_OUTMet3Routing']['_XYCoordinates'][0][-1],
                                                                           [self._DesignParameter['_OUTMet3Routing']['_XYCoordinates'][0][-1][0],
                                                                            self._DesignParameter['RES']['_XYCoordinates'][0][1] - abs(self._DesignParameter['RES']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + self.getXWidth('RES', '_Met1Layer') / 2 - _DRCObj._MetalxMinWidth]])

        self._DesignParameter['_OUTMet2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_DRCObj._MetalxMinWidth)
        self._DesignParameter['_OUTMet2Routing']['_XYCoordinates'] = [[[self._DesignParameter['_NCAP2RESMet1Routing']['_XYCoordinates'][0][0][0] - self.getYWidth('RES','_Met1Layer') / 2,
                                                                        self._DesignParameter['_OUTMet3Routing']['_XYCoordinates'][-1][-1][1] + self.getWidth('_OUTMet2Routing') / 2],
                                                                       [self._DesignParameter['_OUTMet3Routing']['_XYCoordinates'][-1][-1][0] + self.getWidth('_OUTMet3Routing') / 2,
                                                                        self._DesignParameter['_OUTMet3Routing']['_XYCoordinates'][-1][-1][1] + self.getWidth('_OUTMet2Routing') / 2]]]

        self._DesignParameter['_OUTMet22Met3Via']['_XYCoordinates'].append([self._DesignParameter['_OUTMet3Routing']['_XYCoordinates'][-1][-1][0],
                                                                            self._DesignParameter['_OUTMet3Routing']['_XYCoordinates'][-1][-1][1] + self.getXWidth('_OUTMet22Met3Via', '_Met3Layer') / 2])

        self._DesignParameter['_OUTMet12Met2Via'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=90, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_OUTMet12Met2ViaIn{}'.format(_Name)))[0]
        self._DesignParameter['_OUTMet12Met2Via']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1)
        self._DesignParameter['_OUTMet12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self.getYWidth('RES', '_Met1Layer')
        self._DesignParameter['_OUTMet12Met2Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self._DesignParameter['_OUTMet12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        self._DesignParameter['_OUTMet12Met2Via']['_XYCoordinates'] = [[self._DesignParameter['_NCAP2RESMet1Routing']['_XYCoordinates'][0][0][0], self._DesignParameter['RES']['_XYCoordinates'][0][1] - abs(self._DesignParameter['RES']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + self.getXWidth('RES', '_Met1Layer') / 2 - self.getXWidth('_OUTMet12Met2Via', '_Met1Layer') / 2]]


        # 1 stage out - CAP
        OUT1NCAP_COYnum = int((self.getWidth('_NCAPMet2PolyRouting') - 2 * _DRCObj._MetalxMinEnclosureCO2 - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) + 1) - 1
        self._DesignParameter['OUT1NCAPVia'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='OUT1NCAPViaIn{}'.format(_Name)))[0]
        self._DesignParameter['OUT1NCAPVia']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=OUT1NCAP_COYnum)
        self._DesignParameter['OUT1NCAPVia']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self.getWidth('_NCAPMet2PolyRouting')
        self._DesignParameter['OUT1NCAPVia']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = self._DesignParameter['OUT1NCAPVia']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']

        self._DesignParameter['_OUT1NCAPMet3Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=self.getXWidth('OUT1NCAPVia', '_Met3Layer'))
        self._DesignParameter['_OUT1NCAPMet3Routing']['_XYCoordinates'] = [[[self.getXY('_P2Met3Routing')[0][1][0] + self.getWidth('_P2Met3Routing') / 2 - self.getWidth('_OUT1NCAPMet3Routing') / 2,
                                                                             self.getXY('_P2Met3Routing')[0][1][1]],
                                                                            [self.getXY('_P2Met3Routing')[0][1][0] + self.getWidth('_P2Met3Routing') / 2 - self.getWidth('_OUT1NCAPMet3Routing') / 2,
                                                                             self.getXY('_NCAPMet2PolyRouting')[0][-1][1] - abs(self.getWidth('_NCAPMet2PolyRouting')) / 2]]]

        self._DesignParameter['_OUT1NCAPMet2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=self.getWidth('_NCAPMet2PolyRouting'))

        for i in range(0, NCAP_NumofGate):
            self._DesignParameter['OUT1NCAPVia']['_XYCoordinates'].append([self.getXY('_OUT1NCAPMet3Routing')[0][0][0], self.getXY('_NCAPMet2PolyRouting')[i][-1][1]])
            self._DesignParameter['_OUT1NCAPMet2Routing']['_XYCoordinates'].append([self.getXY('_NCAPMet2PolyRouting')[i][-1],[self.getXY('_OUT1NCAPMet3Routing')[0][0][0], self.getXY('_NCAPMet2PolyRouting')[i][-1][1]]])



        print('******************************************** PIN Generation ********************************************')
        self._DesignParameter['PIN_VSS'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='VSS')

        self._DesignParameter['PIN_VDD'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='VDD')

        self._DesignParameter['PIN_INP'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='INP')

        self._DesignParameter['PIN_INN'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='INN')

        self._DesignParameter['DRW_VB'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='VB')

        self._DesignParameter['PIN_VSS']['_XYCoordinates'] = self.getXY('PSubRing', 'top')[0]
        self._DesignParameter['PIN_VDD']['_XYCoordinates'] = self.getXY('NSubRing', 'top')[0]
        self._DesignParameter['PIN_INP']['_XYCoordinates'] = self.getXY('N1PolyGate')[0]
        self._DesignParameter['PIN_INN']['_XYCoordinates'] = self.getXY('N0PolyGate')[0]
        self._DesignParameter['DRW_VB']['_XYCoordinates'] = self.getXY('N0PolyGate')[0]


################################# DRC Check #################################
import random
if __name__ == '__main__':
    P0_Finger = 10
    P1_Finger = 10
    P2_Finger = 18
    P3_Finger = 4

    N0_Finger = 10
    N1_Finger = 10
    N2_Finger = 4
    N3_Finger = 4
    N4_Finger = 8

    ChannelLength = 50
    MOS_Width = 1000
    GateSpacing = 114
    SDWidth = 50
    XVT = 'RVT'

    NCAP_XWidth = 3500
    NCAP_YWidth = 2550
    NCAP_NumofGate = 2
    NCAP_NumofRX = 3

    ResWidth = 1650
    ResLength = 1500
    ResCONUMX = None
    ResCONUMY = 1
    _SeriesStripes = 2
    _ParallelStripes = 1

    _GuardringCOpitch = 142
    _GuardringbyArea = True
    _GuardringNumofCO = None
    _GuardringThickness = 348
    _GuardringPPEnclosure = 56


    DesignParameters._Technology = 'SS28nm'
    TopObj = _SingleEnded2StageOPAmp(_DesignParameter=None, _Name='_SingleEnded2StageOPAmp')
    TopObj._CalculateDesignParameter(
        P0_Finger=P0_Finger,
        P1_Finger=P1_Finger,
        P2_Finger=P2_Finger,
        P3_Finger=P3_Finger,

        N0_Finger=N0_Finger,
        N1_Finger=N1_Finger,
        N2_Finger=N2_Finger,
        N3_Finger=N3_Finger,
        N4_Finger=N4_Finger,

        ChannelLength=ChannelLength,
        MOS_Width=MOS_Width,
        GateSpacing=GateSpacing,
        SDWidth=SDWidth,
        XVT=XVT,

        NCAP_XWidth=NCAP_XWidth,  # Length
        NCAP_YWidth=NCAP_YWidth,  # Width
        NCAP_NumofGate=NCAP_NumofGate,
        NCAP_NumofRX=NCAP_NumofRX,  # 270deg rotate

        ResWidth=ResWidth,
        ResLength=ResLength,
        ResCONUMX=ResCONUMX,
        ResCONUMY=ResCONUMY,
        _SeriesStripes=_SeriesStripes,
        _ParallelStripes=_ParallelStripes,

        _GuardringCOpitch=_GuardringCOpitch,
        _GuardringbyArea=_GuardringbyArea,
        _GuardringNumofCO=_GuardringNumofCO,
        _GuardringThickness=_GuardringThickness,
        _GuardringPPEnclosure=_GuardringPPEnclosure
    )
    TopObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=TopObj._DesignParameter)
    testStreamFile = open('./_SingleEnded2StageOPAmp.gds', 'wb')
    tmp = TopObj._CreateGDSStream(TopObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('#############################      Sending to FTP Server...      ##############################')

    import ftplib

    ftp = ftplib.FTP('141.223.24.53')
    ftp.login('smlim96', 'min753531')
    ftp.cwd('/mnt/sdc/smlim96/OPUS/ss28')
    myfile = open('_SingleEnded2StageOPAmp.gds', 'rb')
    ftp.storbinary('STOR _SingleEnded2StageOPAmp.gds', myfile)
    myfile.close()

    # import DRCchecker
    # a = DRCchecker.DRCchecker('smlim96','min753531','/mnt/sdc/smlim96/OPUS/ss28','/mnt/sdc/smlim96/OPUS/ss28/DRC/run','DFF','DFF',None)
    # a.DRCchecker()
    #
    # print ("DRC Clean!!!")