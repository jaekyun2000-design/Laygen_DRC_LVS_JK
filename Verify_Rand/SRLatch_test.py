import StickDiagram
import DesignParameters
import copy
import DRC
import NMOSWithDummy_iksu
import PMOSWithDummy_iksu
import NbodyContact_iksu
import PbodyContact_iksu
import ViaPoly2Met1
import ViaMet12Met2
import ViaMet22Met3
import ViaMet32Met4
import ViaMet42Met5
import ViaMet52Met6
import math
import random


class _SRLatch(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_Finger1=None, _Finger2=None, _Finger3=None, _Finger4=None,
                                           _NMOSChannelWidth1=None, _PMOSChannelWidth1=None, _NMOSChannelWidth2=None,
                                           _PMOSChannelWidth2=None, _NMOSChannelWidth3=None, _PMOSChannelWidth3=None,
                                           _NMOSChannelWidth4=None, _PMOSChannelWidth4=None,
                                           _ChannelLength=None, _NPRatio=None, _VDD2VSSHeightAtOneSide=None,
                                           _Dummy=None,
                                           _NumSupplyCoX=None, _NumSupplyCoY=None, _SupplyMet1XWidth=None,
                                           _SupplyMet1YWidth=None,
                                           NumViaPoly2Met1CoX=None, NumViaPoly2Met1CoY=None,
                                           NumViaPMOSMet12Met2CoX=None, NumViaPMOSMet12Met2CoY=None,
                                           NumViaNMOSMet12Met2CoX=None, NumViaNMOSMet12Met2CoY=None,
                                           NumViaPMOSMet22Met3CoX=None, NumViaPMOSMet22Met3CoY=None,
                                           NumViaNMOSMet22Met3CoX=None, NumViaNMOSMet22Met3CoY=None, _XVT=None,
                                            _PowerLine=False)

    def __init__(self, _DesignParameter=None, _Name='SRLatch'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter

        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

    def _CalculateDesignParameter(self, _Finger1=None, _Finger2=None, _Finger3=None, _Finger4=None, \
                                  # _PMOSFinger1=None, _PMOSFinger2=None, _PMOSFinger3=None, _PMOSFinger4=None, \
                                  _NMOSChannelWidth1=None, _PMOSChannelWidth1=None, _NMOSChannelWidth2=None,
                                  _PMOSChannelWidth2=None, _NMOSChannelWidth3=None, _PMOSChannelWidth3=None,
                                  _NMOSChannelWidth4=None, _PMOSChannelWidth4=None, _ChannelLength=None, _NPRatio=None, \
                                  _VDD2VSSHeightAtOneSide=None, _Dummy=None, _NumSupplyCoX=None, _NumSupplyCoY=None, \
                                  _SupplyMet1XWidth=None, _SupplyMet1YWidth=None, NumViaPoly2Met1CoX=None, \
                                  NumViaPoly2Met1CoY=None, NumViaPMOSMet12Met2CoX=None, NumViaPMOSMet12Met2CoY=None, \
                                  NumViaNMOSMet12Met2CoX=None, NumViaNMOSMet12Met2CoY=None, NumViaPMOSMet22Met3CoX=None,
                                  NumViaPMOSMet22Met3CoY=None, \
                                  NumViaNMOSMet22Met3CoX=None, NumViaNMOSMet22Met3CoY=None, _XVT=None,
                                  _PowerLine=False):

        _DRCObj = DRC.DRC()
        _Name = 'SRLatch'
        MinSnapSpacing = _DRCObj._MinSnapSpacing
        #####################################################_NMOS Generation###############################################################
        #####################################_NMOS1 Generation######################################
        _NMOSinputs = copy.deepcopy(NMOSWithDummy_iksu._NMOS._ParametersForDesignCalculation)
        _NMOSinputs['_NMOSNumberofGate'] = _Finger1
        _NMOSinputs['_NMOSChannelWidth'] = _NMOSChannelWidth1
        _NMOSinputs['_NMOSChannellength'] = _ChannelLength
        _NMOSinputs['_NMOSDummy'] = _Dummy
        _NMOSinputs['_XVT'] = _XVT
        #     _NMOSinputs['_Flip'] = None

        self._DesignParameter['_NMOS1'] = \
        self._SrefElementDeclaration(_Reflect = [1,0,0], _Angle=0,_DesignObj=NMOSWithDummy_iksu._NMOS(_DesignParameter=None, \
                                                                    _Name='NMOS1In{}'.format(_Name)))[0]
        self._DesignParameter['_NMOS1']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOSinputs)

        del _NMOSinputs

        _NMOSinputs = copy.deepcopy(NMOSWithDummy_iksu._NMOS._ParametersForDesignCalculation)
        _NMOSinputs['_NMOSNumberofGate'] = _Finger1
        _NMOSinputs['_NMOSChannelWidth'] = _NMOSChannelWidth1
        _NMOSinputs['_NMOSChannellength'] = _ChannelLength
        _NMOSinputs['_NMOSDummy'] = _Dummy
        _NMOSinputs['_XVT'] = _XVT
        #     _NMOSinputs['_Flip'] = None

        self._DesignParameter['_NMOS1_r'] = \
        self._SrefElementDeclaration(_DesignObj=NMOSWithDummy_iksu._NMOS(_DesignParameter=None, \
                                                                    _Name='NMOS1_rIn{}'.format(_Name)))[0]
        self._DesignParameter['_NMOS1_r']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOSinputs)

        del _NMOSinputs

        #####################################_NMOS2 Generation######################################
        _NMOSinputs = copy.deepcopy(NMOSWithDummy_iksu._NMOS._ParametersForDesignCalculation)
        _NMOSinputs['_NMOSNumberofGate'] = _Finger2
        _NMOSinputs['_NMOSChannelWidth'] = _NMOSChannelWidth2
        _NMOSinputs['_NMOSChannellength'] = _ChannelLength
        _NMOSinputs['_NMOSDummy'] = _Dummy
        _NMOSinputs['_XVT'] = _XVT
        #     _NMOSinputs['_Flip'] = None

        self._DesignParameter['_NMOS2'] = \
            self._SrefElementDeclaration(_Reflect = [1,0,0], _Angle=0,_DesignObj=NMOSWithDummy_iksu._NMOS(_DesignParameter=None, \
                                                                        _Name='NMOS2In{}'.format(_Name)))[0]
        self._DesignParameter['_NMOS2']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOSinputs)

        del _NMOSinputs

        _NMOSinputs = copy.deepcopy(NMOSWithDummy_iksu._NMOS._ParametersForDesignCalculation)
        _NMOSinputs['_NMOSNumberofGate'] = _Finger2
        _NMOSinputs['_NMOSChannelWidth'] = _NMOSChannelWidth2
        _NMOSinputs['_NMOSChannellength'] = _ChannelLength
        _NMOSinputs['_NMOSDummy'] = _Dummy
        _NMOSinputs['_XVT'] = _XVT
        #     _NMOSinputs['_Flip'] = None

        self._DesignParameter['_NMOS2_r'] = \
        self._SrefElementDeclaration(_DesignObj=NMOSWithDummy_iksu._NMOS(_DesignParameter=None, \
                                                                    _Name='NMOS2_rIn{}'.format(_Name)))[0]
        self._DesignParameter['_NMOS2_r']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOSinputs)

        del _NMOSinputs


        #####################################_NMOS3 Generation######################################
        _NMOSinputs = copy.deepcopy(NMOSWithDummy_iksu._NMOS._ParametersForDesignCalculation)
        _NMOSinputs['_NMOSNumberofGate'] = _Finger3
        _NMOSinputs['_NMOSChannelWidth'] = _NMOSChannelWidth3
        _NMOSinputs['_NMOSChannellength'] = _ChannelLength
        _NMOSinputs['_NMOSDummy'] = _Dummy
        _NMOSinputs['_XVT'] = _XVT
        #     _NMOSinputs['_Flip'] = None

        self._DesignParameter['_NMOS3'] = \
            self._SrefElementDeclaration(_Reflect = [1,0,0], _Angle=0,_DesignObj=NMOSWithDummy_iksu._NMOS(_DesignParameter=None, \
                                                                        _Name='NMOS3In{}'.format(_Name)))[0]
        self._DesignParameter['_NMOS3']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOSinputs)

        del _NMOSinputs

        _NMOSinputs = copy.deepcopy(NMOSWithDummy_iksu._NMOS._ParametersForDesignCalculation)
        _NMOSinputs['_NMOSNumberofGate'] = _Finger3
        _NMOSinputs['_NMOSChannelWidth'] = _NMOSChannelWidth3
        _NMOSinputs['_NMOSChannellength'] = _ChannelLength
        _NMOSinputs['_NMOSDummy'] = _Dummy
        _NMOSinputs['_XVT'] = _XVT
        #     _NMOSinputs['_Flip'] = None

        self._DesignParameter['_NMOS3_r'] = \
        self._SrefElementDeclaration(_DesignObj=NMOSWithDummy_iksu._NMOS(_DesignParameter=None, \
                                                                    _Name='NMOS3_rIn{}'.format(_Name)))[0]
        self._DesignParameter['_NMOS3_r']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOSinputs)

        del _NMOSinputs



        #####################################_NMOS4 Generation######################################
        _NMOSinputs = copy.deepcopy(NMOSWithDummy_iksu._NMOS._ParametersForDesignCalculation)
        _NMOSinputs['_NMOSNumberofGate'] = _Finger4
        _NMOSinputs['_NMOSChannelWidth'] = _NMOSChannelWidth4
        _NMOSinputs['_NMOSChannellength'] = _ChannelLength
        _NMOSinputs['_NMOSDummy'] = _Dummy
        _NMOSinputs['_XVT'] = _XVT
        #     _NMOSinputs['_Flip'] = None

        self._DesignParameter['_NMOS4'] = \
            self._SrefElementDeclaration(_Reflect = [1,0,0], _Angle=0,_DesignObj=NMOSWithDummy_iksu._NMOS(_DesignParameter=None, \
                                                                        _Name='NMOS4In{}'.format(_Name)))[0]
        self._DesignParameter['_NMOS4']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOSinputs)

        del _NMOSinputs


        _NMOSinputs = copy.deepcopy(NMOSWithDummy_iksu._NMOS._ParametersForDesignCalculation)
        _NMOSinputs['_NMOSNumberofGate'] = _Finger4
        _NMOSinputs['_NMOSChannelWidth'] = _NMOSChannelWidth4
        _NMOSinputs['_NMOSChannellength'] = _ChannelLength
        _NMOSinputs['_NMOSDummy'] = _Dummy
        _NMOSinputs['_XVT'] = _XVT
        #     _NMOSinputs['_Flip'] = None

        self._DesignParameter['_NMOS4_r'] = \
        self._SrefElementDeclaration(_DesignObj=NMOSWithDummy_iksu._NMOS(_DesignParameter=None, \
                                                                    _Name='NMOS4_rIn{}'.format(_Name)))[0]
        self._DesignParameter['_NMOS4_r']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOSinputs)

        del _NMOSinputs




        #####################################################_PMOS Generation###############################################################
        #####################################_PMOS1 Generation######################################
        _PMOSinputs = copy.deepcopy(PMOSWithDummy_iksu._PMOS._ParametersForDesignCalculation)
        _PMOSinputs['_PMOSNumberofGate'] = _Finger1
        _PMOSinputs['_PMOSChannelWidth'] = _PMOSChannelWidth1
        _PMOSinputs['_PMOSChannellength'] = _ChannelLength
        _PMOSinputs['_PMOSDummy'] = _Dummy
        _PMOSinputs['_XVT'] = _XVT
        #      _PMOSinputs['_Flip'] = None

        self._DesignParameter['_PMOS1'] = \
            self._SrefElementDeclaration(_DesignObj=PMOSWithDummy_iksu._PMOS(_DesignParameter=None, \
                                                                        _Name='PMOS1In{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS1']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOSinputs)

        del _PMOSinputs

        _PMOSinputs = copy.deepcopy(PMOSWithDummy_iksu._PMOS._ParametersForDesignCalculation)
        _PMOSinputs['_PMOSNumberofGate'] = _Finger1
        _PMOSinputs['_PMOSChannelWidth'] = _PMOSChannelWidth1
        _PMOSinputs['_PMOSChannellength'] = _ChannelLength
        _PMOSinputs['_PMOSDummy'] = _Dummy
        _PMOSinputs['_XVT'] =_XVT
        #      _PMOSinputs['_Flip'] = None

        self._DesignParameter['_PMOS1_r'] = \
            self._SrefElementDeclaration(_Reflect = [1,0,0], _Angle=0,_DesignObj=PMOSWithDummy_iksu._PMOS(_DesignParameter=None, \
                                                                        _Name='PMOS1_rIn{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS1_r']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOSinputs)

        del _PMOSinputs




        #####################################_PMOS2 Generation######################################
        _PMOSinputs = copy.deepcopy(PMOSWithDummy_iksu._PMOS._ParametersForDesignCalculation)
        _PMOSinputs['_PMOSNumberofGate'] = _Finger2
        _PMOSinputs['_PMOSChannelWidth'] = _PMOSChannelWidth2
        _PMOSinputs['_PMOSChannellength'] = _ChannelLength
        _PMOSinputs['_PMOSDummy'] = _Dummy
        _PMOSinputs['_XVT'] = _XVT
        #     _PMOSinputs['_Flip'] = None

        self._DesignParameter['_PMOS2'] = \
            self._SrefElementDeclaration(_DesignObj=PMOSWithDummy_iksu._PMOS(_DesignParameter=None, \
                                                                        _Name='PMOS2In{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS2']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOSinputs)

        del _PMOSinputs

        _PMOSinputs = copy.deepcopy(PMOSWithDummy_iksu._PMOS._ParametersForDesignCalculation)
        _PMOSinputs['_PMOSNumberofGate'] = _Finger2
        _PMOSinputs['_PMOSChannelWidth'] = _PMOSChannelWidth2
        _PMOSinputs['_PMOSChannellength'] = _ChannelLength
        _PMOSinputs['_PMOSDummy'] = _Dummy
        _PMOSinputs['_XVT'] = _XVT
        #      _PMOSinputs['_Flip'] = None

        self._DesignParameter['_PMOS2_r'] = \
            self._SrefElementDeclaration(_Reflect = [1,0,0], _Angle=0,_DesignObj=PMOSWithDummy_iksu._PMOS(_DesignParameter=None, \
                                                                        _Name='PMOS2_rIn{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS2_r']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOSinputs)

        del _PMOSinputs



        #####################################_PMOS3 Generation######################################
        _PMOSinputs = copy.deepcopy(PMOSWithDummy_iksu._PMOS._ParametersForDesignCalculation)
        _PMOSinputs['_PMOSNumberofGate'] = _Finger3
        _PMOSinputs['_PMOSChannelWidth'] = _PMOSChannelWidth3
        _PMOSinputs['_PMOSChannellength'] = _ChannelLength
        _PMOSinputs['_PMOSDummy'] = _Dummy
        _PMOSinputs['_XVT'] = _XVT
        #     _PMOSinputs['_Flip'] = None

        self._DesignParameter['_PMOS3'] = \
            self._SrefElementDeclaration(_DesignObj=PMOSWithDummy_iksu._PMOS(_DesignParameter=None, \
                                                                        _Name='PMOS3In{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS3']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOSinputs)

        del _PMOSinputs

        _PMOSinputs = copy.deepcopy(PMOSWithDummy_iksu._PMOS._ParametersForDesignCalculation)
        _PMOSinputs['_PMOSNumberofGate'] = _Finger3
        _PMOSinputs['_PMOSChannelWidth'] = _PMOSChannelWidth3
        _PMOSinputs['_PMOSChannellength'] = _ChannelLength
        _PMOSinputs['_PMOSDummy'] = _Dummy
        _PMOSinputs['_XVT'] = _XVT
        #      _PMOSinputs['_Flip'] = None

        self._DesignParameter['_PMOS3_r'] = \
            self._SrefElementDeclaration(_Reflect = [1,0,0], _Angle=0,_DesignObj=PMOSWithDummy_iksu._PMOS(_DesignParameter=None, \
                                                                        _Name='PMOS3_rIn{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS3_r']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOSinputs)

        del _PMOSinputs



        #####################################_PMOS4 Generation######################################
        _PMOSinputs = copy.deepcopy(PMOSWithDummy_iksu._PMOS._ParametersForDesignCalculation)
        _PMOSinputs['_PMOSNumberofGate'] = _Finger4
        _PMOSinputs['_PMOSChannelWidth'] = _PMOSChannelWidth4
        _PMOSinputs['_PMOSChannellength'] = _ChannelLength
        _PMOSinputs['_PMOSDummy'] = _Dummy
        _PMOSinputs['_XVT'] = _XVT
        #      _PMOSinputs['_Flip'] = None

        self._DesignParameter['_PMOS4'] = \
            self._SrefElementDeclaration(_DesignObj=PMOSWithDummy_iksu._PMOS(_DesignParameter=None, \
                                                                        _Name='PMOS4In{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS4']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOSinputs)

        del _PMOSinputs

        _PMOSinputs = copy.deepcopy(PMOSWithDummy_iksu._PMOS._ParametersForDesignCalculation)
        _PMOSinputs['_PMOSNumberofGate'] = _Finger4
        _PMOSinputs['_PMOSChannelWidth'] = _PMOSChannelWidth4
        _PMOSinputs['_PMOSChannellength'] = _ChannelLength
        _PMOSinputs['_PMOSDummy'] = _Dummy
        _PMOSinputs['_XVT'] = _XVT
        #      _PMOSinputs['_Flip'] = None

        self._DesignParameter['_PMOS4_r'] = \
            self._SrefElementDeclaration(_Reflect = [1,0,0], _Angle=0,_DesignObj=PMOSWithDummy_iksu._PMOS(_DesignParameter=None, \
                                                                        _Name='PMOS4_rIn{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS4_r']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOSinputs)

        del _PMOSinputs



        #####################################################VIA Generation###############################################################
        #####################################VIA Generation for Gate######################################
        _LenBtwPMOSGates1 = \
        self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting'][
            '_XYCoordinates'][-1][0] - \
        self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting'][
            '_XYCoordinates'][0][0]

        _VIAPMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        _tmpNumCOX = int(_LenBtwPMOSGates1 // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

        if _tmpNumCOX < 1:
            _tmpNumCOX = 1

        if NumViaPoly2Met1CoX != None:
            _tmpNumCOX = NumViaPoly2Met1CoX

        if NumViaPoly2Met1CoY == None:
            _tmpNumCOY = 1
        else:
            _tmpNumCOY = NumViaPoly2Met1CoY

        _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX
        _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = _tmpNumCOY

        self._DesignParameter['_VIAPMOS1Poly2Met1'] = \
        self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, \
                                                                           _Name='ViaPoly2Met1OnPMOS1GateIn{}'.format(
                                                                               _Name)))[0]
        self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
            **_VIAPMOSPoly2Met1)
        del _VIAPMOSPoly2Met1
        del _tmpNumCOX
        del _tmpNumCOY

        _LenBtwPMOSGates2 = \
        self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting'][
            '_XYCoordinates'][-1][0] - \
        self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting'][
            '_XYCoordinates'][0][0]

        _VIAPMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        _tmpNumCOX = int(_LenBtwPMOSGates2 // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

        if _tmpNumCOX < 1:
            _tmpNumCOX = 1

        if NumViaPoly2Met1CoX != None:
            _tmpNumCOX = NumViaPoly2Met1CoX

        if NumViaPoly2Met1CoY == None:
            _tmpNumCOY = 1
        else:
            _tmpNumCOY = NumViaPoly2Met1CoY

        _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX
        _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = _tmpNumCOY


        self._DesignParameter['_VIAPMOS2Poly2Met1'] = \
        self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, \
                                                                           _Name='ViaPoly2Met1OnPMOS2GateIn{}'.format(
                                                                               _Name)))[0]
        self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
            **_VIAPMOSPoly2Met1)
        del _VIAPMOSPoly2Met1
        del _tmpNumCOX
        del _tmpNumCOY

        _LenBtwPMOSGates3 = \
        self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting'][
            '_XYCoordinates'][-1][0] - \
        self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting'][
            '_XYCoordinates'][0][0]

        _VIAPMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        _tmpNumCOX = int(_LenBtwPMOSGates3 // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

        if _tmpNumCOX < 1:
            _tmpNumCOX = 1

        if NumViaPoly2Met1CoX != None:
            _tmpNumCOX = NumViaPoly2Met1CoX

        if NumViaPoly2Met1CoY == None:
            _tmpNumCOY = 1
        else:
            _tmpNumCOY = NumViaPoly2Met1CoY

        _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX
        _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = _tmpNumCOY


        self._DesignParameter['_VIAPMOS3Poly2Met1'] = \
        self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, \
                                                                           _Name='ViaPoly2Met1OnPMOS3GateIn{}'.format(
                                                                               _Name)))[0]
        self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
            **_VIAPMOSPoly2Met1)
        del _VIAPMOSPoly2Met1
        del _tmpNumCOX
        del _tmpNumCOY

        _LenBtwPMOSGates4 = \
        self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting'][
            '_XYCoordinates'][-1][0] - \
        self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting'][
            '_XYCoordinates'][0][0]

        _VIAPMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        _tmpNumCOX = int(_LenBtwPMOSGates4 // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

        if _tmpNumCOX < 1:
            _tmpNumCOX = 1

        if NumViaPoly2Met1CoX != None:
            _tmpNumCOX = NumViaPoly2Met1CoX

        if NumViaPoly2Met1CoY == None:
            _tmpNumCOY = 1
        else:
            _tmpNumCOY = NumViaPoly2Met1CoY

        _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX
        _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = _tmpNumCOY


        self._DesignParameter['_VIAPMOS4Poly2Met1'] = \
        self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, \
                                                                           _Name='ViaPoly2Met1OnPMOS4GateIn{}'.format(
                                                                               _Name)))[0]
        self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
            **_VIAPMOSPoly2Met1)
        del _VIAPMOSPoly2Met1
        del _tmpNumCOX
        del _tmpNumCOY

        #####################################Met1&Met2 Contact######################################
        _PMOSViaNum = NumViaPMOSMet12Met2CoY
        if _PMOSViaNum == None:
            _PMOSViaNum = int(
                self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (
                            _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _PMOSViaNum < 2:
            _PMOSViaNum = 2

        if NumViaPMOSMet12Met2CoX == None:
            NumViaPMOSMet12Met2CoX = 1

        _VIAPMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _VIAPMOSMet12['_ViaMet12Met2NumberOfCOX'] = NumViaPMOSMet12Met2CoX
        _VIAPMOSMet12['_ViaMet12Met2NumberOfCOY'] = _PMOSViaNum

        self._DesignParameter['_ViaMet12Met2OnPMOS'] = \
        self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, \
                                                                           _Name='ViaMet12Met2OnPMOSIn{}'.format(
                                                                               _Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnPMOS'][
            '_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_VIAPMOSMet12)
        del _PMOSViaNum
        del _VIAPMOSMet12

        _NMOSViaNum = NumViaNMOSMet12Met2CoY
        if _NMOSViaNum == None:
            _NMOSViaNum = int(
                self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (
                            _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNum < 2:
            _NMOSViaNum = 2

        if NumViaNMOSMet12Met2CoX == None:
            NumViaNMOSMet12Met2CoX = 1

        _VIANMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _VIANMOSMet12['_ViaMet12Met2NumberOfCOX'] = NumViaNMOSMet12Met2CoX
        _VIANMOSMet12['_ViaMet12Met2NumberOfCOY'] = _NMOSViaNum

        self._DesignParameter['_ViaMet12Met2OnNMOS'] = \
        self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, \
                                                                           _Name='ViaMet12Met2OnNMOSIn{}'.format(
                                                                               _Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnNMOS'][
            '_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_VIANMOSMet12)
        del _NMOSViaNum
        del _VIANMOSMet12

        #####################################################SupplyRail Generation###############################################################
        #####################################VSS Generation######################################
        _ContactNum = _NumSupplyCoX

        _tmpPolySpace = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co)
        _tmpPODummySpace = self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] - self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] +\
                           self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] - self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] +\
                           self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] - self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] +\
                           self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] - self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] +\
                           + 3 * _tmpPolySpace + 4 * _ChannelLength

        if _NumSupplyCoX == None:
            _ContactNum = int((_tmpPODummySpace // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2))) + 3
                           #            6 * _tmpPolySpace + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] +
                           # self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] +
                           # self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] +
                           # self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))
                           #
        if _ContactNum < 2:
            _ContactNum = 2

        if _NumSupplyCoY == None:
            _NumSupplyCoY = 2

        _Pbodyinputs = copy.deepcopy(PbodyContact_iksu._PbodyContact._ParametersForDesignCalculation)
        _Pbodyinputs['_NumberOfPbodyCOX'] = _ContactNum
        _Pbodyinputs['_NumberOfPbodyCOY'] = _NumSupplyCoY
        _Pbodyinputs['_Met1XWidth'] = _SupplyMet1XWidth
        _Pbodyinputs['_Met1YWidth'] = _SupplyMet1YWidth

        self._DesignParameter['PbodyContact'] = \
        self._SrefElementDeclaration(_DesignObj=PbodyContact_iksu._PbodyContact(_DesignParameter=None, \
                                                                           _Name='PbodyContactIn{}'.format(_Name)))[0]
        self._DesignParameter['PbodyContact']['_DesignObj']._CalculatePbodyContactDesignParameter(**_Pbodyinputs)
        del _Pbodyinputs

        #####################################VDD Generation######################################
        _Nbodyinputs = copy.deepcopy(NbodyContact_iksu._NbodyContact._ParametersForDesignCalculation)
        _Nbodyinputs['_NumberOfNbodyCOX'] = _ContactNum
        _Nbodyinputs['_NumberOfNbodyCOY'] = _NumSupplyCoY
        _Nbodyinputs['_Met1XWidth'] = _SupplyMet1XWidth
        _Nbodyinputs['_Met1YWidth'] = _SupplyMet1YWidth

        self._DesignParameter['NbodyContact'] = \
        self._SrefElementDeclaration(_DesignObj=NbodyContact_iksu._NbodyContact(_DesignParameter=None, \
                                                                           _Name='NbodyContactIn{}'.format(_Name)))[0]
        self._DesignParameter['NbodyContact']['_DesignObj']._CalculateNbodyContactDesignParameter(**_Nbodyinputs)
        del _Nbodyinputs

        #####################################################Coordinates Setting###############################################################
        _Met1DistancebtwSupplyandMOS = _DRCObj._Metal1DefaultSpace
        _VDD2VSSMinHeightAtOneSide = self.CeilMinSnapSpacing(self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                     self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                     2 * _Met1DistancebtwSupplyandMOS + 2 * self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + 3 * _DRCObj._Metal1MinSpace2 + _DRCObj._MetalxMinSpace2, MinSnapSpacing)

        if _VDD2VSSHeightAtOneSide == None:
            _VDD2VSSHeightAtOneSide = _VDD2VSSMinHeightAtOneSide
            print('_VDD2VSSMinHeightAtOneSide =', _VDD2VSSMinHeightAtOneSide)

        else:
            if _VDD2VSSHeightAtOneSide < _VDD2VSSMinHeightAtOneSide:
                print('_VDD2VSSMinHeightAtOneSide =', _VDD2VSSMinHeightAtOneSide)
                raise NotImplementedError

        self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        self._DesignParameter['_NMOS1_r']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        self._DesignParameter['_NMOS2_r']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        self._DesignParameter['_NMOS3_r']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        self._DesignParameter['_NMOS4_r']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

        self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        self._DesignParameter['_PMOS1_r']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        self._DesignParameter['_PMOS2_r']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        self._DesignParameter['_PMOS3_r']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        self._DesignParameter['_PMOS4_r']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

        #####################################################MOS Coordinates Setting###############################################################

        self._DesignParameter['_NMOS1']['_XYCoordinates'] = [
            [-self.CeilMinSnapSpacing((self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']) // 2, MinSnapSpacing),
             + self.CeilMinSnapSpacing(self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2  + \
             max(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 + _Met1DistancebtwSupplyandMOS, MinSnapSpacing)]]

        self._DesignParameter['_NMOS1_r']['_XYCoordinates'] = [
            [-self.CeilMinSnapSpacing((self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']) // 2, MinSnapSpacing),
             - self.CeilMinSnapSpacing(self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 + \
               max(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) // 2 + _Met1DistancebtwSupplyandMOS, MinSnapSpacing)]]

        self._DesignParameter['_NMOS2']['_XYCoordinates'] = [[self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + _ChannelLength + _tmpPolySpace,
                                                              self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_NMOS2_r']['_XYCoordinates'] = [[self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1_r']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS2_r']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + _ChannelLength + _tmpPolySpace,
                                                              self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_NMOS3']['_XYCoordinates'] = [[self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0] +
                                                              self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + _ChannelLength + _tmpPolySpace,
                                                              self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_NMOS3_r']['_XYCoordinates'] = [[self._DesignParameter['_NMOS2_r']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS2_r']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS3_r']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + _ChannelLength + _tmpPolySpace,
                                                              self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_NMOS4']['_XYCoordinates'] = [[self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + _ChannelLength + _tmpPolySpace,
                                                              self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_NMOS4_r']['_XYCoordinates'] = [[self._DesignParameter['_NMOS3_r']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS3_r']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS4_r']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + _ChannelLength + _tmpPolySpace,
                                                              self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][1]]]

        self._DesignParameter['_PMOS1']['_XYCoordinates'] = [[self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0],
                                                              self.CeilMinSnapSpacing(_VDD2VSSHeightAtOneSide - self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 - max(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                                                      self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) // 2 - _Met1DistancebtwSupplyandMOS, MinSnapSpacing)]]
        self._DesignParameter['_PMOS1_r']['_XYCoordinates'] = [[self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][0],
                                                              -(self.CeilMinSnapSpacing(_VDD2VSSHeightAtOneSide - self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 - max(self._DesignParameter['_PMOS1_r']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                                                      self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) // 2 - _Met1DistancebtwSupplyandMOS, MinSnapSpacing))]]
        self._DesignParameter['_PMOS2']['_XYCoordinates'] = [[self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0],
                                                              self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_PMOS2_r']['_XYCoordinates'] = [[self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0],
                                                              -(self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1])]]
        self._DesignParameter['_PMOS3']['_XYCoordinates'] = [[self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0],
                                                              self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_PMOS3_r']['_XYCoordinates'] = [[self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0],
                                                              -(self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1])]]
        self._DesignParameter['_PMOS4']['_XYCoordinates'] = [[self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0],
                                                              self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_PMOS4_r']['_XYCoordinates'] = [[self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0],
                                                              -(self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1])]]

        #####################################################Supply Rail Coordinates Setting###############################################################
        MiddleCoordinateX = self.CeilMinSnapSpacing((self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][0]) // 2, MinSnapSpacing)  ## Center of MOSs


        self._DesignParameter['PbodyContact']['_XYCoordinates'] = [[MiddleCoordinateX, 0]]
        self._DesignParameter['NbodyContact']['_XYCoordinates'] = [[MiddleCoordinateX, _VDD2VSSHeightAtOneSide],
                                                                   [MiddleCoordinateX, 0 - _VDD2VSSHeightAtOneSide]]

        self._DesignParameter['SRLatchCenterX'] = {'_Ignore': MiddleCoordinateX, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None} #### Must be used when you s-reference this SRLatch file!!!!!!!!!!!!!!!!!!

        #####################################################Via Met1&Met2 Coordinates Setting###############################################################
        _LengthbtwViaCentertoViaCenter = _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace

        tmpViaMet12Met2OnPMOS = []
        tmpViaMet12Met2OnPMOSandMet212Met3OnPMOS = []
        for i in range(0, len(
                self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting'][
                    '_XYCoordinates'])):
            tmpViaMet12Met2OnPMOS.append([self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] +
                                          self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1] +
                                          self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]])
            tmpViaMet12Met2OnPMOS.append([self._DesignParameter['_PMOS1_r']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] +
                                          self._DesignParameter['_PMOS1_r']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_PMOS1_r']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1] +
                                          self._DesignParameter['_PMOS1_r']['_XYCoordinates'][0][1]])
        for i in range(0, len(
                self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting'][
                    '_XYCoordinates'])):
            tmpViaMet12Met2OnPMOS.append([self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] +
                                          self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1] +
                                          self._DesignParameter['_PMOS2']['_XYCoordinates'][0][1]])
            tmpViaMet12Met2OnPMOS.append([self._DesignParameter['_PMOS2_r']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] +
                                          self._DesignParameter['_PMOS2_r']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_PMOS2_r']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1] +
                                          self._DesignParameter['_PMOS2_r']['_XYCoordinates'][0][1]])
        for i in range(0, len(
                self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting'][
                    '_XYCoordinates'])):
            tmpViaMet12Met2OnPMOS.append([self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] +
                                          self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1] +
                                          self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1]])
            tmpViaMet12Met2OnPMOS.append([self._DesignParameter['_PMOS4_r']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] +
                                          self._DesignParameter['_PMOS4_r']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_PMOS4_r']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1] +
                                          self._DesignParameter['_PMOS4_r']['_XYCoordinates'][0][1]])
        for i in range(0, len(
                self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting'][
                    '_XYCoordinates'])):
            tmpViaMet12Met2OnPMOS.append([self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] +
                                          self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0], \
                                          self.FloorMinSnapSpacing(self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1] +
                                          self._DesignParameter['_PMOS3']['_XYCoordinates'][0][
                                              1] - _LengthbtwViaCentertoViaCenter // 4, MinSnapSpacing)])
            tmpViaMet12Met2OnPMOS.append([self._DesignParameter['_PMOS3_r']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] +
                                          self._DesignParameter['_PMOS3_r']['_XYCoordinates'][0][0], \
                                          self.CeilMinSnapSpacing(self._DesignParameter['_PMOS3_r']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1] +
                                          self._DesignParameter['_PMOS3_r']['_XYCoordinates'][0][
                                              1] + _LengthbtwViaCentertoViaCenter // 4, MinSnapSpacing)])
        for i in range(0, len(self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])):
            tmpViaMet12Met2OnPMOSandMet212Met3OnPMOS.append([self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0], \
                                                             self.CeilMinSnapSpacing(self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1] + _LengthbtwViaCentertoViaCenter // 4, MinSnapSpacing)])
            tmpViaMet12Met2OnPMOSandMet212Met3OnPMOS.append([self._DesignParameter['_PMOS3_r']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS3_r']['_XYCoordinates'][0][0], \
                                                             self.FloorMinSnapSpacing(self._DesignParameter['_PMOS3_r']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_PMOS3_r']['_XYCoordinates'][0][1] - _LengthbtwViaCentertoViaCenter // 4, MinSnapSpacing)])

        self._DesignParameter['_ViaMet12Met2OnPMOS']['_XYCoordinates'] = tmpViaMet12Met2OnPMOS + tmpViaMet12Met2OnPMOSandMet212Met3OnPMOS
        del tmpViaMet12Met2OnPMOS

        tmpViaMet12Met2OnNMOS = []
        tmpViaMet12Met2OnNMOSandMet212Met3OnNMOS = []
        for i in range(0, len(
                self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting'][
                    '_XYCoordinates'])):
            tmpViaMet12Met2OnNMOS.append([self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] +
                                          self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1] +
                                          self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]])
            tmpViaMet12Met2OnNMOS.append([self._DesignParameter['_NMOS1_r']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] +
                                          self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_NMOS1_r']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1] +
                                          self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][1]])
        for i in range(0, len(
                self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting'][
                    '_XYCoordinates'])):
            tmpViaMet12Met2OnNMOS.append([self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] +
                                          self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1] +
                                          self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1]])
            tmpViaMet12Met2OnNMOS.append([self._DesignParameter['_NMOS2_r']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] +
                                          self._DesignParameter['_NMOS2_r']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_NMOS2_r']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1] +
                                          self._DesignParameter['_NMOS2_r']['_XYCoordinates'][0][1]])
        for i in range(0, len(
                self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting'][
                    '_XYCoordinates'])):
            tmpViaMet12Met2OnNMOS.append([self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] +
                                          self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1] +
                                          self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1]])
            tmpViaMet12Met2OnNMOS.append([self._DesignParameter['_NMOS4_r']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] +
                                          self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_NMOS4_r']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1] +
                                          self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][1]])
        for i in range(0, len(
                self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting'][
                    '_XYCoordinates'])):
            tmpViaMet12Met2OnNMOS.append([self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] +
                                          self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0], \
                                          self.CeilMinSnapSpacing(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1] +
                                          self._DesignParameter['_NMOS3']['_XYCoordinates'][0][
                                              1] + _LengthbtwViaCentertoViaCenter // 4, MinSnapSpacing)])
            tmpViaMet12Met2OnNMOS.append([self._DesignParameter['_NMOS3_r']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] +
                                          self._DesignParameter['_NMOS3_r']['_XYCoordinates'][0][0], \
                                          self.FloorMinSnapSpacing(self._DesignParameter['_NMOS3_r']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1] +
                                          self._DesignParameter['_NMOS3_r']['_XYCoordinates'][0][
                                              1] - _LengthbtwViaCentertoViaCenter // 4, MinSnapSpacing)])
        for i in range(0, len(
                self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting'][
                    '_XYCoordinates'])):
            tmpViaMet12Met2OnNMOSandMet212Met3OnNMOS.append([self._DesignParameter['_NMOS3'][
                                                                 '_DesignObj']._DesignParameter[
                                                                 '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][
                                                                 0] +
                                                             self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0], \
                                                             self.FloorMinSnapSpacing(self._DesignParameter['_NMOS3'][
                                                                 '_DesignObj']._DesignParameter[
                                                                 '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][
                                                                 1] +
                                                             self._DesignParameter['_NMOS3']['_XYCoordinates'][0][
                                                                 1] - _LengthbtwViaCentertoViaCenter // 4, MinSnapSpacing)])
            tmpViaMet12Met2OnNMOSandMet212Met3OnNMOS.append([self._DesignParameter['_NMOS3'][
                                                                 '_DesignObj']._DesignParameter[
                                                                 '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][
                                                                 0] +
                                                             self._DesignParameter['_NMOS3_r']['_XYCoordinates'][0][0], \
                                                             self.CeilMinSnapSpacing(self._DesignParameter['_NMOS3'][
                                                                 '_DesignObj']._DesignParameter[
                                                                 '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][
                                                                 1] +
                                                             self._DesignParameter['_NMOS3_r']['_XYCoordinates'][0][
                                                                 1] + _LengthbtwViaCentertoViaCenter // 4, MinSnapSpacing)])

        self._DesignParameter['_ViaMet12Met2OnNMOS']['_XYCoordinates'] = tmpViaMet12Met2OnNMOS + tmpViaMet12Met2OnNMOSandMet212Met3OnNMOS
        del tmpViaMet12Met2OnNMOS

        #####################################################Via Poly Coordinates Setting###############################################################
        #####################################_VIAPMOS1Poly2Met1#####################################
        self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'] = [
            [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0],
             self.FloorMinSnapSpacing(self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] - max(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 - self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - _DRCObj._Metal1MinSpace2, MinSnapSpacing)],
            [self._DesignParameter['_PMOS1_r']['_XYCoordinates'][0][0],
             self.CeilMinSnapSpacing(self._DesignParameter['_PMOS1_r']['_XYCoordinates'][0][1] + max(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 + self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _DRCObj._Metal1MinSpace2, MinSnapSpacing)],
            [self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0],
             self.CeilMinSnapSpacing(self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + max(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 + self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _DRCObj._Metal1MinSpace2, MinSnapSpacing)],
            [self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][0],
             self.FloorMinSnapSpacing(self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][1] - max(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 - self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - _DRCObj._Metal1MinSpace2, MinSnapSpacing)]
        ]

        ############################
        if _Dummy == True :
            if _Finger1 == 1:
                _LengthBtwPoly2Poly = _ChannelLength + _tmpPolySpace
                _LengthNPolyDummyEdge2OriginX = (int(_Finger1 // 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength / 2 - (self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2
                _LengthPPolyDummyEdge2OriginX = (int(_Finger1 // 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength / 2 - (self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2

                _LengthNPolyVIAtoGoUp = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthNPolyDummyEdge2OriginX * _LengthNPolyDummyEdge2OriginX) + MinSnapSpacing
                _LengthPPolyVIAtoGoDown = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthPPolyDummyEdge2OriginX * _LengthPPolyDummyEdge2OriginX) + MinSnapSpacing
                self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'] = [[self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self.FloorMinSnapSpacing(min(self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 - self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 - _LengthPPolyVIAtoGoDown, self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][0][1]), MinSnapSpacing)],
                                                                                 [self._DesignParameter['_PMOS1_r']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(max(self._DesignParameter['_PMOS1_r']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthPPolyVIAtoGoDown, self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][1]), MinSnapSpacing)],
                                                                                 [self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(max(self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyVIAtoGoUp, self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][2][1]), MinSnapSpacing)],
                                                                                 [self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][0], self.FloorMinSnapSpacing(min(self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 - self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 - _LengthNPolyVIAtoGoUp, self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][3][1]), MinSnapSpacing)]]

            #####################################_VIAPMOS2Poly2Met1#####################################
        self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'] = [
                [self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0],
                 self.FloorMinSnapSpacing(self._DesignParameter['_PMOS2']['_XYCoordinates'][0][1] - max(self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 - self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - _DRCObj._Metal1MinSpace2, MinSnapSpacing)],
                [self._DesignParameter['_PMOS2_r']['_XYCoordinates'][0][0],
                 self.CeilMinSnapSpacing(self._DesignParameter['_PMOS2_r']['_XYCoordinates'][0][1] + max(self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 + self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _DRCObj._Metal1MinSpace2, MinSnapSpacing)],
                [self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0],
                 self.CeilMinSnapSpacing(self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1] + max(self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 + self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _DRCObj._Metal1MinSpace2, MinSnapSpacing)],
                [self._DesignParameter['_NMOS2_r']['_XYCoordinates'][0][0],
                 self.FloorMinSnapSpacing(self._DesignParameter['_NMOS2_r']['_XYCoordinates'][0][1] - max(self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 - self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - _DRCObj._Metal1MinSpace2, MinSnapSpacing)]]

            ############################
        if _Dummy == True :
            if _Finger2 == 1:
                _LengthBtwPoly2Poly = _ChannelLength + _tmpPolySpace
                _LengthNPolyDummyEdge2OriginX = (int(_Finger2 // 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength / 2 - (self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2
                _LengthPPolyDummyEdge2OriginX = (int(_Finger2 // 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength / 2 - (self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2

                _LengthNPolyVIAtoGoUp = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthNPolyDummyEdge2OriginX * _LengthNPolyDummyEdge2OriginX) + MinSnapSpacing
                _LengthPPolyVIAtoGoDown = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthPPolyDummyEdge2OriginX * _LengthPPolyDummyEdge2OriginX) + MinSnapSpacing
                self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'] = [[self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0], self.FloorMinSnapSpacing(min(self._DesignParameter['_PMOS2']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 - self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 - _LengthPPolyVIAtoGoDown, self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][0][1]), MinSnapSpacing)],
                                                                                 [self._DesignParameter['_PMOS2_r']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(max(self._DesignParameter['_PMOS2_r']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyVIAtoGoUp, self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][1][1]), MinSnapSpacing)],
                                                                                 [self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(max(self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyVIAtoGoUp, self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][2][1]), MinSnapSpacing)],
                                                                                 [self._DesignParameter['_NMOS2_r']['_XYCoordinates'][0][0], self.FloorMinSnapSpacing(min(self._DesignParameter['_NMOS2_r']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 - self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 - _LengthPPolyVIAtoGoDown, self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][3][1]), MinSnapSpacing)]]

            #####################################_VIAPMOS3Poly2Met1#####################################
        self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'] = [
                [self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0],
                 self.FloorMinSnapSpacing(self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1] - max(self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + _LengthbtwViaCentertoViaCenter / 2) / 2 - self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - _DRCObj._Metal1MinSpace2, MinSnapSpacing)],
                [self._DesignParameter['_PMOS3_r']['_XYCoordinates'][0][0],
                 self.CeilMinSnapSpacing(self._DesignParameter['_PMOS3_r']['_XYCoordinates'][0][1] + max(self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + _LengthbtwViaCentertoViaCenter / 2) / 2 + self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _DRCObj._Metal1MinSpace2, MinSnapSpacing)],
                [self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0],
                 self.CeilMinSnapSpacing(self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + max(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + _LengthbtwViaCentertoViaCenter / 2) / 2 + self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _DRCObj._Metal1MinSpace2, MinSnapSpacing)],
                [self._DesignParameter['_NMOS3_r']['_XYCoordinates'][0][0],
                 self.FloorMinSnapSpacing(self._DesignParameter['_NMOS3_r']['_XYCoordinates'][0][1] - max(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + _LengthbtwViaCentertoViaCenter / 2) / 2 - self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - _DRCObj._Metal1MinSpace2, MinSnapSpacing)]
        ]

            ############################
        if _Dummy == True :
            if _Finger3 == 1:
                _LengthBtwPoly2Poly = _ChannelLength + _tmpPolySpace
                _LengthNPolyDummyEdge2OriginX = (int(_Finger3 // 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength / 2 - (self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2
                _LengthPPolyDummyEdge2OriginX = (int(_Finger3 // 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength / 2 - (self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2

                _LengthNPolyVIAtoGoUp = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthNPolyDummyEdge2OriginX * _LengthNPolyDummyEdge2OriginX) + MinSnapSpacing
                _LengthPPolyVIAtoGoDown = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthPPolyDummyEdge2OriginX * _LengthPPolyDummyEdge2OriginX) + MinSnapSpacing
                self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'] = [[self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0], self.FloorMinSnapSpacing(min(self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 - self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 - _LengthPPolyVIAtoGoDown, self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][0][1]), MinSnapSpacing)],
                                                                                 [self._DesignParameter['_PMOS3_r']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(max(self._DesignParameter['_PMOS3_r']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthPPolyVIAtoGoDown, self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][1][1]), MinSnapSpacing)],
                                                                                 [self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(max(self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyVIAtoGoUp, self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][1]), MinSnapSpacing)],
                                                                                 [self._DesignParameter['_NMOS3_r']['_XYCoordinates'][0][0], self.FloorMinSnapSpacing(min(self._DesignParameter['_NMOS3_r']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 - self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 - _LengthNPolyVIAtoGoUp, self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][3][1]), MinSnapSpacing)]]

            #####################################_VIAPMOS4Poly2Met1#####################################
        self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'] = [
                [self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0],
                 self.FloorMinSnapSpacing(self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1] - max(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 - self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - _DRCObj._Metal1MinSpace2, MinSnapSpacing)],
                [self._DesignParameter['_PMOS4_r']['_XYCoordinates'][0][0],
                 self.CeilMinSnapSpacing(self._DesignParameter['_PMOS4_r']['_XYCoordinates'][0][1] + max(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 + self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _DRCObj._Metal1MinSpace2, MinSnapSpacing)],
                [self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0],
                 self.CeilMinSnapSpacing(self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1] + max(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 + self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _DRCObj._Metal1MinSpace2, MinSnapSpacing)],
                [self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][0],
                 self.FloorMinSnapSpacing(self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][1] - max(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 - self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - _DRCObj._Metal1MinSpace2, MinSnapSpacing)]]

            ############################
        if _Dummy == True :
            if _Finger4 == 1:
                _LengthBtwPoly2Poly = _ChannelLength + _tmpPolySpace
                _LengthNPolyDummyEdge2OriginX = (int(_Finger4 // 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength / 2 - (self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2
                _LengthPPolyDummyEdge2OriginX = (int(_Finger4 // 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength / 2 - (self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2

                _LengthNPolyVIAtoGoUp = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthNPolyDummyEdge2OriginX * _LengthNPolyDummyEdge2OriginX) + MinSnapSpacing
                _LengthPPolyVIAtoGoDown = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthPPolyDummyEdge2OriginX * _LengthPPolyDummyEdge2OriginX) + MinSnapSpacing
                self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'] = [[self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0], self.FloorMinSnapSpacing(min(self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 - self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 - _LengthPPolyVIAtoGoDown, self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][0][1]), MinSnapSpacing)],
                                                                                 [self._DesignParameter['_PMOS4_r']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(max(self._DesignParameter['_PMOS4_r']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyVIAtoGoUp, self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][1][1]), MinSnapSpacing)],
                                                                                 [self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(max(self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyVIAtoGoUp, self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][2][1]), MinSnapSpacing)],
                                                                                 [self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][0], self.FloorMinSnapSpacing(min(self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 - self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 - _LengthPPolyVIAtoGoDown, self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][3][1]), MinSnapSpacing)]]

        #####################################################Routing###############################################################
        #####################################VSS&VDD Met1 Routing######################################
        tmpNMOSSupplyRouting = []
        tmpPMOSSupplyRouting = []

        for i in range(0, len(
                self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting'][
                    '_XYCoordinates'])):
            tmpPMOSSupplyRouting.append([[self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0] +
                                          self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][1] +
                                          self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]], \
                                         [self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0] +
                                          self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['NbodyContact']['_XYCoordinates'][0][1]]])
            tmpPMOSSupplyRouting.append([[self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0] +
                                          self._DesignParameter['_PMOS1_r']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][1] +
                                          self._DesignParameter['_PMOS1_r']['_XYCoordinates'][0][1]], \
                                         [self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0] +
                                          self._DesignParameter['_PMOS1_r']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['NbodyContact']['_XYCoordinates'][1][1]]])

        for j in range(0, len(
                self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting'][
                    '_XYCoordinates'])):
            tmpPMOSSupplyRouting.append([[self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][j][0] +
                                          self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][j][1] +
                                          self._DesignParameter['_PMOS2']['_XYCoordinates'][0][1]], \
                                         [self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][j][0] +
                                          self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['NbodyContact']['_XYCoordinates'][0][1]]])
            tmpPMOSSupplyRouting.append([[self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][j][0] +
                                          self._DesignParameter['_PMOS2_r']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][j][1] +
                                          self._DesignParameter['_PMOS2_r']['_XYCoordinates'][0][1]], \
                                         [self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][j][0] +
                                          self._DesignParameter['_PMOS2_r']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['NbodyContact']['_XYCoordinates'][1][1]]])

        for k in range(0, len(
                self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting'][
                    '_XYCoordinates'])):
            tmpPMOSSupplyRouting.append([[self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][k][0] +
                                          self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][k][1] +
                                          self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1]], \
                                         [self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][k][0] +
                                          self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['NbodyContact']['_XYCoordinates'][0][1]]])
            tmpPMOSSupplyRouting.append([[self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][k][0] +
                                          self._DesignParameter['_PMOS4_r']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][k][1] +
                                          self._DesignParameter['_PMOS4_r']['_XYCoordinates'][0][1]], \
                                         [self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter[
                                              '_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][k][0] +
                                          self._DesignParameter['_PMOS4_r']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['NbodyContact']['_XYCoordinates'][1][1]]])

        self._DesignParameter['_PMOS1SupplyRouting'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XYCoordinates=[], _Width=100)
        self._DesignParameter['_PMOS1SupplyRouting']['_XYCoordinates'] = tmpPMOSSupplyRouting
        self._DesignParameter['_PMOS1SupplyRouting']['_Width'] = \
        self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

        for i in range(0, len(
                self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting'][
                    '_XYCoordinates'])):
            tmpNMOSSupplyRouting.append([[self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0] +
                                          self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][1] +
                                          self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]], \
                                         [self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0] +
                                          self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['PbodyContact']['_XYCoordinates'][0][1]]])
            tmpNMOSSupplyRouting.append([[self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0] +
                                          self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][1] +
                                          self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][1]], \
                                         [self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0] +
                                          self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['PbodyContact']['_XYCoordinates'][0][1]]])

        for j in range(0, len(
                self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting'][
                    '_XYCoordinates'])):
            tmpNMOSSupplyRouting.append([[self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j][0] +
                                          self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j][1] +
                                          self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1]], \
                                         [self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j][0] +
                                          self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['PbodyContact']['_XYCoordinates'][0][1]]])
            tmpNMOSSupplyRouting.append([[self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j][0] +
                                          self._DesignParameter['_NMOS2_r']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j][1] +
                                          self._DesignParameter['_NMOS2_r']['_XYCoordinates'][0][1]], \
                                         [self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j][0] +
                                          self._DesignParameter['_NMOS2_r']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['PbodyContact']['_XYCoordinates'][0][1]]])

        for k in range(0, len(
                self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting'][
                    '_XYCoordinates'])):
            tmpNMOSSupplyRouting.append([[self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][k][0] +
                                          self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][k][1] +
                                          self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1]], \
                                         [self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][k][0] +
                                          self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['PbodyContact']['_XYCoordinates'][0][1]]])
            tmpNMOSSupplyRouting.append([[self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][k][0] +
                                          self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][k][1] +
                                          self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][1]], \
                                         [self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter[
                                              '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][k][0] +
                                          self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['PbodyContact']['_XYCoordinates'][0][1]]])

        self._DesignParameter['_NMOS1SupplyRouting'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XYCoordinates=[], _Width=100)
        self._DesignParameter['_NMOS1SupplyRouting']['_XYCoordinates'] = tmpNMOSSupplyRouting
        self._DesignParameter['_NMOS1SupplyRouting']['_Width'] = \
        self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

        del tmpNMOSSupplyRouting
        del tmpPMOSSupplyRouting

        #####################################Metal Routing######################################
        tmpMet2RoutingOnPMOS = []
        tmpMet2RoutingOnNMOS = []

        _LengthbtwViaCentertoViaCenter = _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace

        tmpMet2RoutingOnPMOS.append([[self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]], \
                                     [self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]])
        tmpMet2RoutingOnPMOS.append([[self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS1_r']['_XYCoordinates'][0][1]], \
                                     [self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS1_r']['_XYCoordinates'][0][1]]])
        tmpMet2RoutingOnPMOS.append([[self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][1]], \
                                     [self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][1]]])
        tmpMet2RoutingOnPMOS.append([[self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2_r']['_XYCoordinates'][0][1]], \
                                     [self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2_r']['_XYCoordinates'][0][1]]])
        tmpMet2RoutingOnPMOS.append([[self.CeilMinSnapSpacing(self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinWidth // 2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet12Met2OnPMOS']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2, MinSnapSpacing)], \
                                     [self.CeilMinSnapSpacing(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0] + _DRCObj._MetalxMinWidth // 2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet12Met2OnPMOS']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2, MinSnapSpacing)]])
        tmpMet2RoutingOnPMOS.append([[self.CeilMinSnapSpacing(self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS3_r']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinWidth // 2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet12Met2OnPMOS']['_XYCoordinates'][1][1] + self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _LengthbtwViaCentertoViaCenter // 4 + _DRCObj._MetalxMinWidth // 2, MinSnapSpacing)], \
                                     [self.CeilMinSnapSpacing(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_PMOS4_r']['_XYCoordinates'][0][0] + _DRCObj._MetalxMinWidth // 2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet12Met2OnPMOS']['_XYCoordinates'][1][1] + self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _LengthbtwViaCentertoViaCenter // 4 + _DRCObj._MetalxMinWidth // 2, MinSnapSpacing)]])

        tmpMet2RoutingOnNMOS.append([[self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]], \
                                     [self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]]])
        tmpMet2RoutingOnNMOS.append([[self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][1]], \
                                     [self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][1]]])
        tmpMet2RoutingOnNMOS.append([[self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1]], \
                                     [self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1]]])
        tmpMet2RoutingOnNMOS.append([[self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS2_r']['_XYCoordinates'][0][1]], \
                                     [self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS2_r']['_XYCoordinates'][0][1]]])
        tmpMet2RoutingOnPMOS.append([[self.CeilMinSnapSpacing(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinWidth // 2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet12Met2OnNMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _LengthbtwViaCentertoViaCenter // 4 + _DRCObj._MetalxMinWidth // 2, MinSnapSpacing)], \
                                     [self.CeilMinSnapSpacing(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + _DRCObj._MetalxMinWidth // 2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet12Met2OnNMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _LengthbtwViaCentertoViaCenter // 4 + _DRCObj._MetalxMinWidth // 2, MinSnapSpacing)]])
        tmpMet2RoutingOnPMOS.append([[self.CeilMinSnapSpacing(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS3_r']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinWidth // 2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet12Met2OnNMOS']['_XYCoordinates'][1][1] - self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2, MinSnapSpacing)], \
                                     [self.CeilMinSnapSpacing(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter[ '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][0] + _DRCObj._MetalxMinWidth // 2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet12Met2OnNMOS']['_XYCoordinates'][1][1] - self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2, MinSnapSpacing)]])

        self._DesignParameter['_Met2Routing1OnPMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met2Routing1OnPMOS']['_Width'] = _DRCObj._MetalxMinWidth
        self._DesignParameter['_Met2Routing1OnPMOS']['_XYCoordinates'] = tmpMet2RoutingOnPMOS

        self._DesignParameter['_Met2Routing1OnNMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met2Routing1OnNMOS']['_Width'] = _DRCObj._MetalxMinWidth
        self._DesignParameter['_Met2Routing1OnNMOS']['_XYCoordinates'] = tmpMet2RoutingOnNMOS

        del tmpMet2RoutingOnPMOS
        del tmpMet2RoutingOnNMOS


        tmpMet2OutputRouting = []
        tmpMet4OutputRouting = []

        tmpMet4OutputRouting.append([[self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1]], \
                                     [self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1]]])
        tmpMet4OutputRouting.append([[self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][1]], \
                                     [self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS4_r']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS4_r']['_XYCoordinates'][0][1]]])


        self._DesignParameter['_Met4OutputRouting'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met4OutputRouting']['_Width'] = _DRCObj._MetalxMinWidth
        self._DesignParameter['_Met4OutputRouting']['_XYCoordinates'] = tmpMet4OutputRouting

        tmpMet2OutputRouting.append([[self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter[
                                          '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0] +
                                      self._DesignParameter['_PMOS2_r']['_XYCoordinates'][0][0],
                                      self._DesignParameter['_PMOS2_r']['_XYCoordinates'][0][1] +
                                      self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter[
                                          '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][1]], \
                                     [self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter[
                                          '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0] +
                                      self._DesignParameter['_NMOS2_r']['_XYCoordinates'][0][0],
                                      self._DesignParameter['_NMOS2_r']['_XYCoordinates'][0][1] +
                                      self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter[
                                          '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][1]]])
        tmpMet2OutputRouting.append([[self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter[
                                          '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0] +
                                      self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0],
                                      self._DesignParameter['_PMOS2']['_XYCoordinates'][0][1] +
                                      self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter[
                                          '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][1]], \
                                     [self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter[
                                          '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0] +
                                      self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0],
                                      self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1] +
                                      self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter[
                                          '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][1]]])
        tmpMet2OutputRouting.append([[self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter[
                                          '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0] +
                                      self._DesignParameter['_PMOS2_r']['_XYCoordinates'][0][0],
                                      self._DesignParameter['_PMOS2_r']['_XYCoordinates'][0][1] +
                                      self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter[
                                          '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][1]], \
                                     [self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter[
                                          '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] +
                                      self._DesignParameter['_NMOS2_r']['_XYCoordinates'][0][0],
                                      self._DesignParameter['_NMOS2_r']['_XYCoordinates'][0][1] +
                                      self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter[
                                          '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][1]]])
        tmpMet2OutputRouting.append([[self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter[
                                          '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0] +
                                      self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0],
                                      self._DesignParameter['_PMOS2']['_XYCoordinates'][0][1] +
                                      self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter[
                                          '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][1]], \
                                     [self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter[
                                          '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] +
                                      self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0],
                                      self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1] +
                                      self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter[
                                          '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][1]]])

        tmpMet2OutputRouting.append([[self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][2][0],
                                      self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][2][1]], [
                                         self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0] +
                                         self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter[
                                             '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0],
                                         self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][2][1]]])
        tmpMet2OutputRouting.append([[self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][3][0],
                                      self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][3][1]], [
                                         self._DesignParameter['_PMOS2_r']['_XYCoordinates'][0][0] +
                                         self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter[
                                             '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0],
                                         self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][3][1]]])

        for j in range(0, len(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
            tmpMet2OutputRouting.append([[self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter[ '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][j][0] + self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1]], \
                                         [self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][j][0] + self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 2, MinSnapSpacing)]])

            tmpMet2OutputRouting.append([[self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][j][0] + self._DesignParameter['_PMOS4_r']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS4_r']['_XYCoordinates'][0][1]], \
                                         [self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][j][0] + self._DesignParameter['_PMOS4_r']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_PMOS4_r']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _LengthbtwViaCentertoViaCenter // 2, MinSnapSpacing)]])

            tmpMet2OutputRouting.append([[self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][j][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1]], \
                                         [self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][j][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _LengthbtwViaCentertoViaCenter // 2, MinSnapSpacing)]])

            tmpMet2OutputRouting.append([[self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][j][0] + self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][1]], \
                                         [self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][j][0] + self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 2, MinSnapSpacing)]])

        self._DesignParameter['_Met2OutputRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met2OutputRouting']['_Width'] = _DRCObj._MetalxMinWidth
        self._DesignParameter['_Met2OutputRouting']['_XYCoordinates'] = tmpMet2OutputRouting

        del tmpMet2OutputRouting
        del tmpMet4OutputRouting

        tmp = []
        for i in range(0, len(self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
            tmp.append([[self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1]], \
                        [self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 2, MinSnapSpacing)]])

            tmp.append([[self._DesignParameter['_PMOS3_r']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS3_r']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS3_r']['_XYCoordinates'][0][1]], \
                        [self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS3_r']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_PMOS3_r']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _LengthbtwViaCentertoViaCenter // 2, MinSnapSpacing)]])

            tmp.append([[self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1]], \
                         [self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _LengthbtwViaCentertoViaCenter // 2, MinSnapSpacing)]])

            tmp.append([[self._DesignParameter['_NMOS3_r']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS3_r']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS3_r']['_XYCoordinates'][0][1]], \
                        [self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS3_r']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_NMOS3_r']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 2, MinSnapSpacing)]])



        self._DesignParameter['_Met2OutputRouting2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met2OutputRouting2']['_Width'] = _DRCObj._MetalxMinWidth
        self._DesignParameter['_Met2OutputRouting2']['_XYCoordinates'] = tmp

        del tmp

        #####################################################Via Met2&Met3 Generation & Coordinates Setting###############################################################
        _PMOSViaNum = NumViaPMOSMet22Met3CoY
        if _PMOSViaNum == None:
            _PMOSViaNum = int(self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

        if _PMOSViaNum < 2:
            _PMOSViaNum = 2

        if NumViaPMOSMet22Met3CoX == None:
            NumViaPMOSMet22Met3CoX = 1

        _VIAPMOSMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _VIAPMOSMet23['_ViaMet22Met3NumberOfCOX'] = NumViaPMOSMet22Met3CoX
        _VIAPMOSMet23['_ViaMet22Met3NumberOfCOY'] = _PMOSViaNum

        self._DesignParameter['_ViaMet22Met3OnPMOS'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnPMOSIn{}'.format(_Name)))[0]


        tmp = []
        for i in range(0, len(
                self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting'][
                    '_XYCoordinates'])):
            tmp.append([self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] +
                        self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter[
                            '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0],
                        self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] +
                        self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter[
                            '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1]])
            tmp.append([self._DesignParameter['_PMOS1_r']['_XYCoordinates'][0][0] +
                        self._DesignParameter['_PMOS1_r']['_DesignObj']._DesignParameter[
                            '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0],
                        self._DesignParameter['_PMOS1_r']['_XYCoordinates'][0][1] +
                        self._DesignParameter['_PMOS1_r']['_DesignObj']._DesignParameter[
                            '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1]])

        self._DesignParameter['_ViaMet22Met3OnPMOS']['_XYCoordinates'] = tmpViaMet12Met2OnPMOSandMet212Met3OnPMOS + tmp
        self._DesignParameter['_ViaMet22Met3OnPMOS']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_VIAPMOSMet23)
        if self._DesignParameter['_ViaMet22Met3OnPMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] * self._DesignParameter['_ViaMet22Met3OnPMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']  < _DRCObj._MetalxMinArea :
            self._DesignParameter['_ViaMet22Met3OnPMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self.CeilMinSnapSpacing(_DRCObj._MetalxMinArea // self._DesignParameter['_ViaMet22Met3OnPMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'], MinSnapSpacing)

        del tmp
        del _PMOSViaNum
        del _VIAPMOSMet23
        del tmpViaMet12Met2OnPMOSandMet212Met3OnPMOS

        _NMOSViaNum = NumViaNMOSMet22Met3CoY
        if _NMOSViaNum == None:
            _NMOSViaNum = int(self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

        if _NMOSViaNum < 2:
            _NMOSViaNum = 2

        if NumViaNMOSMet22Met3CoX == None:
            NumViaNMOSMet22Met3CoX = 1

        _VIANMOSMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _VIANMOSMet23['_ViaMet22Met3NumberOfCOX'] = NumViaNMOSMet22Met3CoX
        _VIANMOSMet23['_ViaMet22Met3NumberOfCOY'] = _NMOSViaNum

        self._DesignParameter['_ViaMet22Met3OnNMOS'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnNMOSIn{}'.format(_Name)))[0]

        tmp = []
        for i in range(0, len(
                self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting'][
                    '_XYCoordinates'])):
            tmp.append([self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] +
                        self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter[
                            '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0],
                        self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] +
                        self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter[
                            '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1]])
            tmp.append([self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][0] +
                        self._DesignParameter['_NMOS1_r']['_DesignObj']._DesignParameter[
                            '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0],
                        self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][1] +
                        self._DesignParameter['_NMOS1_r']['_DesignObj']._DesignParameter[
                            '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1]])

        self._DesignParameter['_ViaMet22Met3OnNMOS']['_XYCoordinates'] = tmpViaMet12Met2OnNMOSandMet212Met3OnNMOS + tmp
        self._DesignParameter['_ViaMet22Met3OnNMOS']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_VIANMOSMet23)
        if self._DesignParameter['_ViaMet22Met3OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] * self._DesignParameter['_ViaMet22Met3OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] < _DRCObj._MetalxMinArea :
            self._DesignParameter['_ViaMet22Met3OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = self.CeilMinSnapSpacing(_DRCObj._MetalxMinArea // self._DesignParameter['_ViaMet22Met3OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'], MinSnapSpacing)

        del tmp
        del _NMOSViaNum
        del _VIANMOSMet23
        del tmpViaMet12Met2OnNMOSandMet212Met3OnNMOS

        self._DesignParameter['_Met3RoutingOnPMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met3RoutingOnPMOS']['_Width'] = _DRCObj._MetalxMinWidth
        self._DesignParameter['_Met3RoutingOnPMOS']['_XYCoordinates'] = [[[self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]], [self.CeilMinSnapSpacing(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0] + _DRCObj._MetalxMinWidth // 2, MinSnapSpacing), self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1]]], \
                                                                         [[self._DesignParameter['_PMOS1_r']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS1_r']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS1_r']['_XYCoordinates'][0][1]], [self.CeilMinSnapSpacing(self._DesignParameter['_PMOS4_r']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS4_r']['_XYCoordinates'][0][0] + _DRCObj._MetalxMinWidth // 2, MinSnapSpacing), self._DesignParameter['_PMOS3_r']['_XYCoordinates'][0][1]]]]

        self._DesignParameter['_Met3RoutingOnNMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met3RoutingOnNMOS']['_Width'] = _DRCObj._MetalxMinWidth
        self._DesignParameter['_Met3RoutingOnNMOS']['_XYCoordinates'] = [[[self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]], [self.CeilMinSnapSpacing(self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] + _DRCObj._MetalxMinWidth // 2 + _DRCObj._MetalxMinSpace, MinSnapSpacing), self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-1][1] + self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1]]], \
                                                                         [[self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1_r']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][1]], [self.CeilMinSnapSpacing(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][0] + _DRCObj._MetalxMinWidth // 2 + _DRCObj._MetalxMinSpace, MinSnapSpacing), self._DesignParameter['_NMOS3_r']['_XYCoordinates'][0][1]]]]


        #####################################################Additional Routing###############################################################
        tmpPMOSGateRouting = []
        tmpNMOSGateRouting = []
        for i in range(0, len(
                self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting'][
                    '_XYCoordinates'])):
            tmpPMOSGateRouting.append([[self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter[
                                            '_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter[
                                            '_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][1] +
                                        self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]], \
                                       [self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter[
                                            '_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][0][1] -
                                        self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter[
                                            '_POLayer']['_YWidth'] // 2]])
            tmpPMOSGateRouting.append([[self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter[
                                            '_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_PMOS1_r']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter[
                                            '_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][1] +
                                        self._DesignParameter['_PMOS1_r']['_XYCoordinates'][0][1]], \
                                       [self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter[
                                            '_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_PMOS1_r']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][1] +
                                        self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter[
                                            '_POLayer']['_YWidth'] // 2]])
            tmpNMOSGateRouting.append([[self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter[
                                            '_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter[
                                            '_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][1] +
                                        self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]], \
                                       [self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter[
                                            '_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][2][1] +
                                        self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter[
                                            '_POLayer']['_YWidth'] // 2]])
            tmpNMOSGateRouting.append([[self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter[
                                            '_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter[
                                            '_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][1] +
                                        self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][1]], \
                                       [self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter[
                                            '_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][3][1] -
                                        self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter[
                                            '_POLayer']['_YWidth'] // 2]])

        self._DesignParameter['_AdditionalPolyOnMOS1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
        self._DesignParameter['_AdditionalPolyOnMOS1']['_Width'] = _ChannelLength
        self._DesignParameter['_AdditionalPolyOnMOS1']['_XYCoordinates'] = tmpPMOSGateRouting + tmpNMOSGateRouting

        del tmpPMOSGateRouting
        del tmpNMOSGateRouting

        tmpPMOSGateRouting = []
        tmpNMOSGateRouting = []
        for i in range(0, len(
                self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting'][
                    '_XYCoordinates'])):
            tmpPMOSGateRouting.append([[self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter[
                                            '_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter[
                                            '_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][1] +
                                        self._DesignParameter['_PMOS2']['_XYCoordinates'][0][1]], \
                                       [self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter[
                                            '_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][0][1] -
                                        self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter[
                                            '_POLayer']['_YWidth'] // 2]])
            tmpPMOSGateRouting.append([[self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter[
                                            '_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_PMOS2_r']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter[
                                            '_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][1] +
                                        self._DesignParameter['_PMOS2_r']['_XYCoordinates'][0][1]], \
                                       [self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter[
                                            '_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_PMOS2_r']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][1][1] +
                                        self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter[
                                            '_POLayer']['_YWidth'] // 2]])
            tmpNMOSGateRouting.append([[self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter[
                                            '_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter[
                                            '_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][1] +
                                        self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1]], \
                                       [self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter[
                                            '_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][2][1] +
                                        self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter[
                                            '_POLayer']['_YWidth'] // 2]])
            tmpNMOSGateRouting.append([[self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter[
                                            '_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_NMOS2_r']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter[
                                            '_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][1] +
                                        self._DesignParameter['_NMOS2_r']['_XYCoordinates'][0][1]], \
                                       [self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter[
                                            '_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_NMOS2_r']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][3][1] -
                                        self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter[
                                            '_POLayer']['_YWidth'] // 2]])

        self._DesignParameter['_AdditionalPolyOnMOS2'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], \
            _XYCoordinates=[], _Width=None)
        self._DesignParameter['_AdditionalPolyOnMOS2']['_Width'] = _ChannelLength
        self._DesignParameter['_AdditionalPolyOnMOS2']['_XYCoordinates'] = tmpPMOSGateRouting + tmpNMOSGateRouting

        del tmpPMOSGateRouting
        del tmpNMOSGateRouting

        tmpPMOSGateRouting = []
        tmpNMOSGateRouting = []
        for i in range(0, len(
                self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting'][
                    '_XYCoordinates'])):
            tmpPMOSGateRouting.append([[self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter[
                                            '_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter[
                                            '_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][1] +
                                        self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1]], \
                                       [self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter[
                                            '_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][0][1] -
                                        self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter[
                                            '_POLayer']['_YWidth'] // 2]])
            tmpPMOSGateRouting.append([[self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter[
                                            '_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_PMOS3_r']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter[
                                            '_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][1] +
                                        self._DesignParameter['_PMOS3_r']['_XYCoordinates'][0][1]], \
                                       [self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter[
                                            '_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_PMOS3_r']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][1][1] +
                                        self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter[
                                            '_POLayer']['_YWidth'] // 2]])
            tmpNMOSGateRouting.append([[self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter[
                                            '_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter[
                                            '_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][1] +
                                        self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1]], \
                                       [self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter[
                                            '_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][1] +
                                        self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter[
                                            '_POLayer']['_YWidth'] // 2]])
            tmpNMOSGateRouting.append([[self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter[
                                            '_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_NMOS3_r']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter[
                                            '_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][1] +
                                        self._DesignParameter['_NMOS3_r']['_XYCoordinates'][0][1]], \
                                       [self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter[
                                            '_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_NMOS3_r']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][3][1] -
                                        self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter[
                                            '_POLayer']['_YWidth'] // 2]])

        self._DesignParameter['_AdditionalPolyOnMOS3'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], \
            _XYCoordinates=[], _Width=None)
        self._DesignParameter['_AdditionalPolyOnMOS3']['_Width'] = _ChannelLength
        self._DesignParameter['_AdditionalPolyOnMOS3']['_XYCoordinates'] = tmpPMOSGateRouting + tmpNMOSGateRouting

        del tmpPMOSGateRouting
        del tmpNMOSGateRouting

        tmpPMOSGateRouting = []
        tmpNMOSGateRouting = []
        for i in range(0, len(
                self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting'][
                    '_XYCoordinates'])):
            tmpPMOSGateRouting.append([[self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter[
                                            '_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter[
                                            '_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][1] +
                                        self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1]], \
                                       [self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter[
                                            '_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][0][1] -
                                        self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter[
                                            '_POLayer']['_YWidth'] // 2]])
            tmpPMOSGateRouting.append([[self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter[
                                            '_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_PMOS4_r']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter[
                                            '_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][1] +
                                        self._DesignParameter['_PMOS4_r']['_XYCoordinates'][0][1]], \
                                       [self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter[
                                            '_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_PMOS4_r']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][1][1] +
                                        self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter[
                                            '_POLayer']['_YWidth'] // 2]])
            tmpNMOSGateRouting.append([[self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter[
                                            '_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter[
                                            '_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][1] +
                                        self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1]], \
                                       [self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter[
                                            '_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][2][1] +
                                        self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter[
                                            '_POLayer']['_YWidth'] // 2]])
            tmpNMOSGateRouting.append([[self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter[
                                            '_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter[
                                            '_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][1] +
                                        self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][1]], \
                                       [self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter[
                                            '_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] +
                                        self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][0],
                                        self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][3][1] -
                                        self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter[
                                            '_POLayer']['_YWidth'] // 2]])

        self._DesignParameter['_AdditionalPolyOnMOS4'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XYCoordinates=[], _Width=None)
        self._DesignParameter['_AdditionalPolyOnMOS4']['_Width'] = _ChannelLength
        self._DesignParameter['_AdditionalPolyOnMOS4']['_XYCoordinates'] = tmpPMOSGateRouting + tmpNMOSGateRouting

        del tmpPMOSGateRouting
        del tmpNMOSGateRouting

        self._DesignParameter['_AdditionalPolyOnGate1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XYCoordinates=[], _XWidth=None, _YWidth=None, _ElementName=None, )
        self._DesignParameter['_AdditionalPolyOnGate1']['_XWidth'] = \
        self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting'][
            '_XYCoordinates'][-1][0] - \
        self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting'][
            '_XYCoordinates'][0][0]
        self._DesignParameter['_AdditionalPolyOnGate1']['_YWidth'] = \
        self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
        self._DesignParameter['_AdditionalPolyOnGate1']['_XYCoordinates'] = self._DesignParameter['_VIAPMOS1Poly2Met1'][
            '_XYCoordinates']

        self._DesignParameter['_AdditionalPolyOnGate2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XYCoordinates=[], _XWidth=None, _YWidth=None, _ElementName=None, )
        self._DesignParameter['_AdditionalPolyOnGate2']['_XWidth'] = \
        self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting'][
            '_XYCoordinates'][-1][0] - \
        self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting'][
            '_XYCoordinates'][0][0]

        self._DesignParameter['_AdditionalPolyOnGate2']['_YWidth'] = \
        self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
        self._DesignParameter['_AdditionalPolyOnGate2']['_XYCoordinates'] = self._DesignParameter['_VIAPMOS2Poly2Met1'][
            '_XYCoordinates']

        self._DesignParameter['_AdditionalPolyOnGate3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XYCoordinates=[], _XWidth=None, _YWidth=None, _ElementName=None, )
        self._DesignParameter['_AdditionalPolyOnGate3']['_XWidth'] = \
        self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting'][
            '_XYCoordinates'][-1][0] - \
        self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting'][
            '_XYCoordinates'][0][0]
        self._DesignParameter['_AdditionalPolyOnGate3']['_YWidth'] = \
        self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
        self._DesignParameter['_AdditionalPolyOnGate3']['_XYCoordinates'] = self._DesignParameter['_VIAPMOS3Poly2Met1'][
            '_XYCoordinates']

        self._DesignParameter['_AdditionalPolyOnGate4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XYCoordinates=[], _XWidth=None, _YWidth=None, _ElementName=None, )
        self._DesignParameter['_AdditionalPolyOnGate4']['_XWidth'] = \
        self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting'][
            '_XYCoordinates'][-1][0] - \
        self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting'][
            '_XYCoordinates'][0][0]
        self._DesignParameter['_AdditionalPolyOnGate4']['_YWidth'] = \
        self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
        self._DesignParameter['_AdditionalPolyOnGate4']['_XYCoordinates'] = self._DesignParameter['_VIAPMOS4Poly2Met1'][
            '_XYCoordinates']

        _NMOSViaNumX = int(
            self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (
                        _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNumX < 2:
            _NMOSViaNumX = 2

        _NMOSViaNumY = int(
            self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (
                        _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNumY < 1:
            _NMOSViaNumY = 1

        _VIANMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _VIANMOSMet12['_ViaMet12Met2NumberOfCOX'] = _NMOSViaNumX
        _VIANMOSMet12['_ViaMet12Met2NumberOfCOY'] = _NMOSViaNumY

        self._DesignParameter['_AdditionalMet12Met2OnGate1'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None,
                                                  _Name='AdditionalViaMet12Met2OnGate1In{}'.format(_Name)))[0]
        self._DesignParameter['_AdditionalMet12Met2OnGate1'][
            '_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_VIANMOSMet12)
        self._DesignParameter['_AdditionalMet12Met2OnGate1']['_XYCoordinates'] = \
        self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates']

        del _NMOSViaNumX
        del _NMOSViaNumY
        del _VIANMOSMet12

        _NMOSViaNumX = int(
            self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (
                        _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNumX < 2:
            _NMOSViaNumX = 2

        _NMOSViaNumY = int(
            self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (
                        _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNumY < 1:
            _NMOSViaNumY = 1

        _VIANMOSMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _VIANMOSMet23['_ViaMet22Met3NumberOfCOX'] = _NMOSViaNumX
        _VIANMOSMet23['_ViaMet22Met3NumberOfCOY'] = _NMOSViaNumY

        self._DesignParameter['_AdditinalMet22Met3OnGate1'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='AdditionalViaMet22Met3OnGate1In{}'.format(_Name)))[0]
        self._DesignParameter['_AdditinalMet22Met3OnGate1']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIANMOSMet23)
        if self._DesignParameter['_AdditinalMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] * self._DesignParameter['_AdditinalMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']  < _DRCObj._MetalxMinArea :
            self._DesignParameter['_AdditinalMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = self.CeilMinSnapSpacing(_DRCObj._MetalxMinArea // self._DesignParameter['_AdditinalMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'], 2 * MinSnapSpacing)
        if self._DesignParameter['_AdditinalMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] * self._DesignParameter['_AdditinalMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']  < _DRCObj._MetalxMinArea :
            self._DesignParameter['_AdditinalMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = self.CeilMinSnapSpacing(_DRCObj._MetalxMinArea // self._DesignParameter['_AdditinalMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'], 2 * MinSnapSpacing)

        self._DesignParameter['_AdditinalMet22Met3OnGate1']['_XYCoordinates'] = [[self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][0][0], self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][0][1]], \
                                                                                 [self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][0], self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][1]]]

        del _NMOSViaNumX
        del _NMOSViaNumY
        del _VIANMOSMet23

        _tmpLength = _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace

        _NMOSViaNumX = int(
            self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (
                        _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNumX < 2:
            _NMOSViaNumX = 2

        _NMOSViaNumY = int(
            self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (
                        _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNumY < 1:
            _NMOSViaNumY = 1

        _VIANMOSMet34 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _VIANMOSMet34['_ViaMet32Met4NumberOfCOX'] = _NMOSViaNumX
        _VIANMOSMet34['_ViaMet32Met4NumberOfCOY'] = _NMOSViaNumY

        self._DesignParameter['_AdditionalMet32Met4OnGate3'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='AdditionalViaMet32Met4OnGate3In{}'.format(_Name)))[0]
        self._DesignParameter['_AdditionalMet32Met4OnGate3']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_VIANMOSMet34)
        self._DesignParameter['_AdditionalMet32Met4OnGate3']['_XYCoordinates'] = [[self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][0],
                                                                                   self.CeilMinSnapSpacing(self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _tmpLength / 4 + _DRCObj._MetalxMinWidth * 3 / 2 + _DRCObj._MetalxMinSpace, MinSnapSpacing)]
                                                                                  ]  ###self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][0][1]]]###self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _tmpLength // 4 + _DRCObj._MetalxMinWidth * 3 // 2 + _DRCObj._MetalxMinSpace]]

        del _NMOSViaNumX
        del _NMOSViaNumY
        del _VIANMOSMet34





        _NMOSViaNumX = 2
        _NMOSViaNumY = 1

        _VIANMOSMet34 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _VIANMOSMet34['_ViaMet32Met4NumberOfCOX'] = _NMOSViaNumX
        _VIANMOSMet34['_ViaMet32Met4NumberOfCOY'] = _NMOSViaNumY


        self._DesignParameter['_AdditionalMet32Met4OverGate3'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='AdditionalMet32Met4OverGate3In{}'.format(_Name)))[0]
        self._DesignParameter['_AdditionalMet32Met4OverGate3']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_VIANMOSMet34)
        self._DesignParameter['_AdditionalMet32Met4OverGate3']['_XYCoordinates'] = [[self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][3][0], self.CeilMinSnapSpacing((self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][1][1] + self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][3][1]) // 2, MinSnapSpacing)],
                                                                                    [self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][0], self._DesignParameter['_AdditinalMet22Met3OnGate1']['_XYCoordinates'][0][1]]]









        _NMOSViaNumX = int(self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNumX < 2:
            _NMOSViaNumX = 2

        _NMOSViaNumY = int(self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNumY < 1:
            _NMOSViaNumY = 1

        _VIANMOSMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _VIANMOSMet23['_ViaMet22Met3NumberOfCOX'] = _NMOSViaNumX
        _VIANMOSMet23['_ViaMet22Met3NumberOfCOY'] = _NMOSViaNumY

        self._DesignParameter['_AdditionalMet22Met3OnGate3'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='AdditionalViaMet22Met3OnGate3In{}'.format(_Name)))[0]
        self._DesignParameter['_AdditionalMet22Met3OnGate3']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIANMOSMet23)
        if self._DesignParameter['_AdditionalMet22Met3OnGate3']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] * self._DesignParameter['_AdditionalMet22Met3OnGate3']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] < _DRCObj._MetalxMinArea :
            self._DesignParameter['_AdditionalMet22Met3OnGate3']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = self.CeilMinSnapSpacing(_DRCObj._MetalxMinArea // self._DesignParameter['_AdditionalMet22Met3OnGate3']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'], 2 * MinSnapSpacing)
        if self._DesignParameter['_AdditionalMet22Met3OnGate3']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] * self._DesignParameter['_AdditionalMet22Met3OnGate3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] < _DRCObj._MetalxMinArea :
            self._DesignParameter['_AdditionalMet22Met3OnGate3']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = self.CeilMinSnapSpacing(_DRCObj._MetalxMinArea // self._DesignParameter['_AdditionalMet22Met3OnGate3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'], 2 * MinSnapSpacing)

        self._DesignParameter['_AdditionalMet22Met3OnGate3']['_XYCoordinates'] = [[self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][0], self.CeilMinSnapSpacing(self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _tmpLength / 4 + _DRCObj._MetalxMinWidth * 3 / 2 + _DRCObj._MetalxMinSpace, MinSnapSpacing)], \
                                                                                  [self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][3][0], self.FloorMinSnapSpacing(self._DesignParameter['_NMOS3_r']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _tmpLength / 4 - _DRCObj._MetalxMinWidth * 3 / 2 - _DRCObj._MetalxMinSpace, MinSnapSpacing)]]


        del _NMOSViaNumX
        del _NMOSViaNumY
        del _VIANMOSMet23



        if _Finger3 != 1 :
            _tmpLengthbtwViaCentertoViaCenter = self.CeilMinSnapSpacing(_LengthbtwViaCentertoViaCenter // 4, MinSnapSpacing)
        else :
            _tmpLengthbtwViaCentertoViaCenter = self.CeilMinSnapSpacing(_LengthbtwViaCentertoViaCenter // 2, MinSnapSpacing)


        _NMOSViaNumX = 2
        _NMOSViaNumY = 1

        _VIANMOSMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _VIANMOSMet23['_ViaMet22Met3NumberOfCOX'] = _NMOSViaNumX
        _VIANMOSMet23['_ViaMet22Met3NumberOfCOY'] = _NMOSViaNumY

        self._DesignParameter['_AdditionalMet22Met3'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='AdditionalViaMet22Met3In{}'.format(_Name)))[0]
        self._DesignParameter['_AdditionalMet22Met3']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIANMOSMet23)
        if self._DesignParameter['_AdditionalMet22Met3']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] * self._DesignParameter['_AdditionalMet22Met3']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']  < _DRCObj._MetalxMinArea :
            self._DesignParameter['_AdditionalMet22Met3']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = self.CeilMinSnapSpacing(_DRCObj._MetalxMinArea // self._DesignParameter['_AdditionalMet22Met3']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'], 2 * MinSnapSpacing)
        if self._DesignParameter['_AdditionalMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] * self._DesignParameter['_AdditionalMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']  < _DRCObj._MetalxMinArea :
            self._DesignParameter['_AdditionalMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = self.CeilMinSnapSpacing(_DRCObj._MetalxMinArea // self._DesignParameter['_AdditionalMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'], 2 * MinSnapSpacing)

        self._DesignParameter['_AdditionalMet22Met3']['_XYCoordinates'] = [[self._DesignParameter['_AdditionalMet32Met4OnGate3']['_XYCoordinates'][0][0] - _tmpLengthbtwViaCentertoViaCenter, self.CeilMinSnapSpacing((self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][1][1] + self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][3][1]) // 2, MinSnapSpacing)]]

        del _NMOSViaNumX
        del _NMOSViaNumY
        del _VIANMOSMet23






        _NMOSViaNumX = 2

        _NMOSViaNumY = 1



        _VIANMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _VIANMOSMet12['_ViaMet12Met2NumberOfCOX'] = _NMOSViaNumX
        _VIANMOSMet12['_ViaMet12Met2NumberOfCOY'] = _NMOSViaNumY

        self._DesignParameter['_AdditionalMet12Met2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='AdditionalViaMet12Met2In{}'.format(_Name)))[0]
        self._DesignParameter['_AdditionalMet12Met2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_VIANMOSMet12)
        self._DesignParameter['_AdditionalMet12Met2']['_XYCoordinates'] = [[self._DesignParameter['_AdditionalMet32Met4OnGate3']['_XYCoordinates'][0][0] - _tmpLengthbtwViaCentertoViaCenter, self.CeilMinSnapSpacing((self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][1][1] + self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][3][1]) // 2, MinSnapSpacing)]]

        del _NMOSViaNumX
        del _NMOSViaNumY
        del _VIANMOSMet12

        _NMOSViaNumX = int(self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNumX < 2:
            _NMOSViaNumX = 2

        _NMOSViaNumY = int(self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNumY < 1:
            _NMOSViaNumY = 1

        _VIANMOSMet34 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _VIANMOSMet34['_ViaMet32Met4NumberOfCOX'] = _NMOSViaNumX
        _VIANMOSMet34['_ViaMet32Met4NumberOfCOY'] = _NMOSViaNumY

        self._DesignParameter['_AdditinalMet32Met4OnGate1'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='AdditionalViaMet32Met4OnMOS1In{}'.format(_Name)))[0]
        self._DesignParameter['_AdditinalMet32Met4OnGate1']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_VIANMOSMet34)
        self._DesignParameter['_AdditinalMet32Met4OnGate1']['_XYCoordinates'] = [[self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][0], self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][1]]]

        del _NMOSViaNumX
        del _NMOSViaNumY
        del _VIANMOSMet34

        _NMOSViaNumX = int(
            self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (
                        _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNumX < 2:
            _NMOSViaNumX = 2

        _NMOSViaNumY = int(
            self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (
                        _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNumY < 1:
            _NMOSViaNumY = 1

        _VIANMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _VIANMOSMet12['_ViaMet12Met2NumberOfCOX'] = _NMOSViaNumX
        _VIANMOSMet12['_ViaMet12Met2NumberOfCOY'] = _NMOSViaNumY

        self._DesignParameter['_AdditionalMet12Met2OnGate3'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None,
                                                  _Name='AdditionalViaMet12Met2OnMOS3In{}'.format(_Name)))[0]
        self._DesignParameter['_AdditionalMet12Met2OnGate3'][
            '_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_VIANMOSMet12)
        if _PMOSChannelWidth3 % 2 == 0 :
            a = 0
        else :
            a = 1
        if _NMOSChannelWidth3 % 2 == 0 :
            b = 0
        else :
            b = 1

        self._DesignParameter['_AdditionalMet12Met2OnGate3']['_XYCoordinates'] = [
            [self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][0][0],
             self.CeilMinSnapSpacing(self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1] -
             self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met2Layer'][
                 '_YWidth'] // 2 - _tmpLength / 4 - _DRCObj._MetalxMinWidth * 3 / 2 - _DRCObj._MetalxMinSpace, MinSnapSpacing)], \
            [self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][1][0],
             self.CeilMinSnapSpacing(self._DesignParameter['_PMOS3_r']['_XYCoordinates'][0][1] +
             self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met2Layer'][
                 '_YWidth'] // 2 + _tmpLength / 4 + _DRCObj._MetalxMinWidth * 3 / 2 + _DRCObj._MetalxMinSpace + a, MinSnapSpacing)], \
            [self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][0],
             self.CeilMinSnapSpacing(self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] +
             self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer'][
                 '_YWidth'] // 2 + _tmpLength / 4 + _DRCObj._MetalxMinWidth * 3 / 2 + _DRCObj._MetalxMinSpace + b, MinSnapSpacing)], \
            [self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][3][0],
             self.CeilMinSnapSpacing(self._DesignParameter['_NMOS3_r']['_XYCoordinates'][0][1] -
             self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer'][
                 '_YWidth'] // 2 - _tmpLength / 4 - _DRCObj._MetalxMinWidth * 3 / 2 - _DRCObj._MetalxMinSpace, MinSnapSpacing)]]

        del _NMOSViaNumX
        del _NMOSViaNumY
        del _VIANMOSMet12



        self._DesignParameter['_AdditionalMet1GateRouting2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
        self._DesignParameter['_AdditionalMet1GateRouting2']['_Width'] = _DRCObj._Metal1MinWidth

        tmpInputRouting = []

        if _Finger2 > 5 and _Finger2 % 4 != 1 :
            for i in range(0, (len(self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']) + 1) // 2):
                tmpInputRouting.append([[self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][2 * i][0], self.CeilMinSnapSpacing(self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][2][1] - self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2, MinSnapSpacing)], \
                                        [self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][2 * i][0], self.CeilMinSnapSpacing(self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][0][1] + self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2, MinSnapSpacing)]])
                tmpInputRouting.append([[self._DesignParameter['_PMOS2_r']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS2_r']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][2 * i][0], self.CeilMinSnapSpacing(self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][3][1] + self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2, MinSnapSpacing)], \
                                        [self._DesignParameter['_NMOS2_r']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS2_r']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][2 * i][0], self.CeilMinSnapSpacing(self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][1][1] - self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2, MinSnapSpacing)]])

        elif _Finger2 > 5 and _Finger2 % 4 == 1 :
            for i in range(1, (len(self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])) // 2 + 1):
                tmpInputRouting.append([[self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][2 * i - 1][0], self.CeilMinSnapSpacing(self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][2][1] - self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2, MinSnapSpacing)], \
                                        [self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][2 * i - 1][0], self.CeilMinSnapSpacing(self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][0][1] + self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2, MinSnapSpacing)]])
                tmpInputRouting.append([[self._DesignParameter['_PMOS2_r']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS2_r']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][2 * i - 1][0], self.CeilMinSnapSpacing(self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][3][1] + self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2, MinSnapSpacing)], \
                                        [self._DesignParameter['_NMOS2_r']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS2_r']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][2 * i - 1][0], self.CeilMinSnapSpacing(self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][1][1] - self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2, MinSnapSpacing)]])



        else :
            tmpInputRouting.append([[self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][0][0], self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][0][1]], [self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][2][0], self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][2][1]]])
            tmpInputRouting.append([[self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][1][0], self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][1][1]], [self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][3][0], self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][3][1]]])

        self._DesignParameter['_AdditionalMet1GateRouting2']['_XYCoordinates'] = tmpInputRouting

        del tmpInputRouting

        self._DesignParameter['_AdditionalMet1GateRouting4'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
        self._DesignParameter['_AdditionalMet1GateRouting4']['_Width'] = _DRCObj._Metal1MinWidth

        tmpInputRouting = []


        if _Finger4 > 5 and _Finger4 % 4 != 1 :
            for i in range(0, (len(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']) + 1) // 2):
                tmpInputRouting.append([[self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][2 * i][0], self.CeilMinSnapSpacing(self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][2][1] - self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2, MinSnapSpacing)], \
                                        [self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][2 * i][0], self.CeilMinSnapSpacing(self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][0][1] + self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2, MinSnapSpacing)]])
                tmpInputRouting.append([[self._DesignParameter['_PMOS4_r']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS4_r']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][2 * i][0], self.CeilMinSnapSpacing(self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][3][1] + self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2, MinSnapSpacing)], \
                                        [self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4_r']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][2 * i][0], self.CeilMinSnapSpacing(self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][1][1] - self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2, MinSnapSpacing)]])

        elif _Finger4 > 5 and _Finger4 % 4 == 1 :
            for i in range(1, (len(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])) // 2 + 1):
                tmpInputRouting.append([[self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][2 * i - 1][0], self.CeilMinSnapSpacing(self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][2][1] - self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2, MinSnapSpacing)], \
                                        [self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][2 * i - 1][0], self.CeilMinSnapSpacing(self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][0][1] + self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2, MinSnapSpacing)]])
                tmpInputRouting.append([[self._DesignParameter['_PMOS4_r']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS4_r']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][2 * i - 1][0], self.CeilMinSnapSpacing(self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][3][1] + self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2, MinSnapSpacing)], \
                                        [self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4_r']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][2 * i - 1][0], self.CeilMinSnapSpacing(self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][1][1] - self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2, MinSnapSpacing)]])




        else :
            tmpInputRouting.append([[self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][0][0], self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][0][1]], [self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][2][0], self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][2][1]]])
            tmpInputRouting.append([[self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][1][0], self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][1][1]], [self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][3][0], self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][3][1]]])

        self._DesignParameter['_AdditionalMet1GateRouting4']['_XYCoordinates'] = tmpInputRouting

        del tmpInputRouting





        self._DesignParameter['_AdditionalMet1Routing1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _XWidth=None, _YWidth=None)
        self._DesignParameter['_AdditionalMet1Routing1']['_XWidth'] = max(self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['_AdditionalMet12Met2OnGate1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
        self._DesignParameter['_AdditionalMet1Routing1']['_YWidth'] = self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        self._DesignParameter['_AdditionalMet1Routing1']['_XYCoordinates'] = self._DesignParameter['_AdditionalMet12Met2OnGate1']['_XYCoordinates']

        self._DesignParameter['_AdditionalMet1Routing3'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
        self._DesignParameter['_AdditionalMet1Routing3']['_Width'] = max(self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['_AdditionalMet12Met2OnGate3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
        self._DesignParameter['_AdditionalMet1Routing3']['_XYCoordinates'] = [[[self._DesignParameter[
                                                                                    '_VIAPMOS3Poly2Met1'][
                                                                                    '_XYCoordinates'][0][0], self.CeilMinSnapSpacing(max(
            self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][0][1] +
            self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,
            self._DesignParameter['_AdditionalMet12Met2OnGate3']['_XYCoordinates'][0][1] +
            self._DesignParameter['_AdditionalMet12Met2OnGate3']['_DesignObj']._DesignParameter['_Met1Layer'][
                '_YWidth'] // 2), MinSnapSpacing)], [self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(min(
            self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][0][1] -
            self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,
            self._DesignParameter['_AdditionalMet12Met2OnGate3']['_XYCoordinates'][0][1] -
            self._DesignParameter['_AdditionalMet12Met2OnGate3']['_DesignObj']._DesignParameter['_Met1Layer'][
                '_YWidth'] // 2), MinSnapSpacing)]], \
                                                                              [[self._DesignParameter[
                                                                                    '_VIAPMOS3Poly2Met1'][
                                                                                    '_XYCoordinates'][1][0], self.CeilMinSnapSpacing(max(
                                                                                  self._DesignParameter[
                                                                                      '_VIAPMOS3Poly2Met1'][
                                                                                      '_XYCoordinates'][1][1] +
                                                                                  self._DesignParameter[
                                                                                      '_VIAPMOS3Poly2Met1'][
                                                                                      '_DesignObj']._DesignParameter[
                                                                                      '_Met1Layer']['_YWidth'] // 2,
                                                                                  self._DesignParameter[
                                                                                      '_AdditionalMet12Met2OnGate3'][
                                                                                      '_XYCoordinates'][1][1] +
                                                                                  self._DesignParameter[
                                                                                      '_AdditionalMet12Met2OnGate3'][
                                                                                      '_DesignObj']._DesignParameter[
                                                                                      '_Met1Layer']['_YWidth'] // 2), MinSnapSpacing)], [
                                                                                   self._DesignParameter[
                                                                                       '_VIAPMOS3Poly2Met1'][
                                                                                       '_XYCoordinates'][1][0], self.CeilMinSnapSpacing(min(
                                                                                      self._DesignParameter[
                                                                                          '_VIAPMOS3Poly2Met1'][
                                                                                          '_XYCoordinates'][1][1] -
                                                                                      self._DesignParameter[
                                                                                          '_VIAPMOS3Poly2Met1'][
                                                                                          '_DesignObj']._DesignParameter[
                                                                                          '_Met1Layer']['_YWidth'] // 2,
                                                                                      self._DesignParameter[
                                                                                          '_AdditionalMet12Met2OnGate3'][
                                                                                          '_XYCoordinates'][1][1] -
                                                                                      self._DesignParameter[
                                                                                          '_AdditionalMet12Met2OnGate3'][
                                                                                          '_DesignObj']._DesignParameter[
                                                                                          '_Met1Layer'][
                                                                                          '_YWidth'] // 2), MinSnapSpacing)]], \
                                                                              [[self._DesignParameter[
                                                                                    '_VIAPMOS3Poly2Met1'][
                                                                                    '_XYCoordinates'][2][0], self.CeilMinSnapSpacing(max(
                                                                                  self._DesignParameter[
                                                                                      '_VIAPMOS3Poly2Met1'][
                                                                                      '_XYCoordinates'][2][1] +
                                                                                  self._DesignParameter[
                                                                                      '_VIAPMOS3Poly2Met1'][
                                                                                      '_DesignObj']._DesignParameter[
                                                                                      '_Met1Layer']['_YWidth'] // 2,
                                                                                  self._DesignParameter[
                                                                                      '_AdditionalMet12Met2OnGate3'][
                                                                                      '_XYCoordinates'][2][1] +
                                                                                  self._DesignParameter[
                                                                                      '_AdditionalMet12Met2OnGate3'][
                                                                                      '_DesignObj']._DesignParameter[
                                                                                      '_Met1Layer']['_YWidth'] // 2), MinSnapSpacing)], [
                                                                                   self._DesignParameter[
                                                                                       '_VIAPMOS3Poly2Met1'][
                                                                                       '_XYCoordinates'][2][0], self.CeilMinSnapSpacing(min(
                                                                                      self._DesignParameter[
                                                                                          '_VIAPMOS3Poly2Met1'][
                                                                                          '_XYCoordinates'][2][1] -
                                                                                      self._DesignParameter[
                                                                                          '_VIAPMOS3Poly2Met1'][
                                                                                          '_DesignObj']._DesignParameter[
                                                                                          '_Met1Layer']['_YWidth'] // 2,
                                                                                      self._DesignParameter[
                                                                                          '_AdditionalMet12Met2OnGate3'][
                                                                                          '_XYCoordinates'][2][1] -
                                                                                      self._DesignParameter[
                                                                                          '_AdditionalMet12Met2OnGate3'][
                                                                                          '_DesignObj']._DesignParameter[
                                                                                          '_Met1Layer'][
                                                                                          '_YWidth'] // 2), MinSnapSpacing)]], \
                                                                              [[self._DesignParameter[
                                                                                    '_VIAPMOS3Poly2Met1'][
                                                                                    '_XYCoordinates'][3][0], self.CeilMinSnapSpacing(max(
                                                                                  self._DesignParameter[
                                                                                      '_VIAPMOS3Poly2Met1'][
                                                                                      '_XYCoordinates'][3][1] +
                                                                                  self._DesignParameter[
                                                                                      '_VIAPMOS3Poly2Met1'][
                                                                                      '_DesignObj']._DesignParameter[
                                                                                      '_Met1Layer']['_YWidth'] // 2,
                                                                                  self._DesignParameter[
                                                                                      '_AdditionalMet12Met2OnGate3'][
                                                                                      '_XYCoordinates'][3][1] +
                                                                                  self._DesignParameter[
                                                                                      '_AdditionalMet12Met2OnGate3'][
                                                                                      '_DesignObj']._DesignParameter[
                                                                                      '_Met1Layer']['_YWidth'] // 2), MinSnapSpacing)], [
                                                                                   self._DesignParameter[
                                                                                       '_VIAPMOS3Poly2Met1'][
                                                                                       '_XYCoordinates'][3][0], self.CeilMinSnapSpacing(min(
                                                                                      self._DesignParameter[
                                                                                          '_VIAPMOS3Poly2Met1'][
                                                                                          '_XYCoordinates'][3][1] -
                                                                                      self._DesignParameter[
                                                                                          '_VIAPMOS3Poly2Met1'][
                                                                                          '_DesignObj']._DesignParameter[
                                                                                          '_Met1Layer']['_YWidth'] // 2,
                                                                                      self._DesignParameter[
                                                                                          '_AdditionalMet12Met2OnGate3'][
                                                                                          '_XYCoordinates'][3][1] -
                                                                                      self._DesignParameter[
                                                                                          '_AdditionalMet12Met2OnGate3'][
                                                                                          '_DesignObj']._DesignParameter[
                                                                                          '_Met1Layer'][
                                                                                          '_YWidth'] // 2), MinSnapSpacing)]]]

        # self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'] + self._DesignParameter['_AdditionalMet12Met2OnGate3']['_XYCoordinates'] ################

        self._DesignParameter['_AdditionalMet1Routing'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XYCoordinates=[], _Width=None)
        self._DesignParameter['_AdditionalMet1Routing']['_Width'] = _DRCObj._Metal1MinWidth
        self._DesignParameter['_AdditionalMet1Routing']['_XYCoordinates'] = [[[self._DesignParameter['_AdditionalMet1GateRouting2']['_XYCoordinates'][-1][0][0],
                                                                               self._DesignParameter[
                                                                                   '_AdditionalMet32Met4OverGate3'][
                                                                                   '_XYCoordinates'][0][1]], [
                                                                                  self._DesignParameter['_NMOS3'][
                                                                                      '_XYCoordinates'][0][0],
                                                                                  self._DesignParameter[
                                                                                      '_AdditionalMet32Met4OverGate3'][
                                                                                      '_XYCoordinates'][0][1]]], \
                                                                             [[self.CeilMinSnapSpacing(self._DesignParameter['_NMOS1'][
                                                                                   '_XYCoordinates'][0][
                                                                                   0] - _DRCObj._Metal1MinWidth // 2, MinSnapSpacing), self.CeilMinSnapSpacing((
                                                                                           self._DesignParameter[
                                                                                               '_VIAPMOS1Poly2Met1'][
                                                                                               '_XYCoordinates'][0][1] +
                                                                                           self._DesignParameter[
                                                                                               '_VIAPMOS1Poly2Met1'][
                                                                                               '_XYCoordinates'][2][
                                                                                               1]) // 2, MinSnapSpacing)], [self._DesignParameter['_AdditionalMet1GateRouting2']['_XYCoordinates'][0][0][0], self.CeilMinSnapSpacing((
                                                                                              self._DesignParameter[
                                                                                                  '_VIAPMOS1Poly2Met1'][
                                                                                                  '_XYCoordinates'][0][
                                                                                                  1] +
                                                                                              self._DesignParameter[
                                                                                                  '_VIAPMOS1Poly2Met1'][
                                                                                                  '_XYCoordinates'][2][
                                                                                                  1]) // 2, MinSnapSpacing)]]]

        self._DesignParameter['_AdditionalMet2Routing'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XYCoordinates=[], _Width=None)
        self._DesignParameter['_AdditionalMet2Routing']['_Width'] = _DRCObj._MetalxMinWidth
        self._DesignParameter['_AdditionalMet2Routing']['_XYCoordinates'] = [[[self._DesignParameter[
                                                                                   '_AdditionalMet12Met2OnGate3'][
                                                                                   '_XYCoordinates'][0][0],
                                                                               self._DesignParameter[
                                                                                   '_AdditionalMet12Met2OnGate3'][
                                                                                   '_XYCoordinates'][0][1]], [
                                                                                  self._DesignParameter['_PMOS2'][
                                                                                      '_XYCoordinates'][0][0] +
                                                                                  self._DesignParameter['_PMOS2'][
                                                                                      '_DesignObj']._DesignParameter[
                                                                                      '_XYCoordinatePMOSOutputRouting'][
                                                                                      '_XYCoordinates'][-1][0],
                                                                                  self._DesignParameter[
                                                                                      '_AdditionalMet12Met2OnGate3'][
                                                                                      '_XYCoordinates'][0][1]]], \
                                                                             [[self._DesignParameter[
                                                                                   '_AdditionalMet12Met2OnGate3'][
                                                                                   '_XYCoordinates'][1][0],
                                                                               self._DesignParameter[
                                                                                   '_AdditionalMet12Met2OnGate3'][
                                                                                   '_XYCoordinates'][1][1]], [
                                                                                  self._DesignParameter['_PMOS2_r'][
                                                                                      '_XYCoordinates'][0][0] +
                                                                                  self._DesignParameter['_PMOS2'][
                                                                                      '_DesignObj']._DesignParameter[
                                                                                      '_XYCoordinatePMOSOutputRouting'][
                                                                                      '_XYCoordinates'][-1][0],
                                                                                  self._DesignParameter[
                                                                                      '_AdditionalMet12Met2OnGate3'][
                                                                                      '_XYCoordinates'][1][1]]]]

        self._DesignParameter['_AdditionalMet3Routing'] = self._PathElementDeclaration(
            DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XYCoordinates=[], _Width=None)
        self._DesignParameter['_AdditionalMet3Routing']['_Width'] = _DRCObj._MetalxMinWidth
        self._DesignParameter['_AdditionalMet3Routing']['_XYCoordinates'] = [[[self._DesignParameter[
                                                                                   '_VIAPMOS1Poly2Met1'][
                                                                                   '_XYCoordinates'][0][0],
                                                                               self._DesignParameter[
                                                                                   '_VIAPMOS1Poly2Met1'][
                                                                                   '_XYCoordinates'][0][1]], [
                                                                                  self._DesignParameter[
                                                                                      '_VIAPMOS3Poly2Met1'][
                                                                                      '_XYCoordinates'][0][0],
                                                                                  self._DesignParameter[
                                                                                      '_VIAPMOS1Poly2Met1'][
                                                                                      '_XYCoordinates'][0][1]]],
                                                                             # [[self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][0][0], self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][0][1] + _DRCObj._MetalxMinWidth // 2], [self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][0], self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _tmpLength // 4 + _DRCObj._MetalxMinWidth * 3 // 2 + _DRCObj._MetalxMinSpace]], \
                                                                             [[self.CeilMinSnapSpacing(self._DesignParameter['_NMOS1'][
                                                                                   '_XYCoordinates'][0][
                                                                                   0] - _DRCObj._Metal1MinWidth // 2, MinSnapSpacing),
                                                                               self._DesignParameter[
                                                                                   '_AdditionalMet12Met2OnGate3'][
                                                                                   '_XYCoordinates'][3][1]],
                                                                              # (self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][1] + self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][3][1]) // 2], #[(self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS2_r']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) // 2 + _DRCObj._Metal1MinWidth // 2, (self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][1] + self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][3][1]) // 2], \
                                                                              # [(self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS2_r']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) // 2 + _DRCObj._Metal1MinWidth // 2, self._DesignParameter['_AdditionalMet12Met2OnGate3']['_XYCoordinates'][3][1]],
                                                                              [self._DesignParameter['_NMOS3_r'][
                                                                                   '_XYCoordinates'][0][0],
                                                                               self._DesignParameter[
                                                                                   '_AdditionalMet12Met2OnGate3'][
                                                                                   '_XYCoordinates'][3][1]]]]

        _ViaNumMet34X = 2
        _ViaNumMet34Y = 1

        _ViaNumMet34 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _ViaNumMet34['_ViaMet32Met4NumberOfCOX'] = _ViaNumMet34X
        _ViaNumMet34['_ViaMet32Met4NumberOfCOY'] = _ViaNumMet34Y

        self._DesignParameter['_VIAMet32Met4forRouting1'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None,
                                                  _Name='VIAMet32Met4forRouting1In{}'.format(_Name)))[0]
        self._DesignParameter['_VIAMet32Met4forRouting1'][
            '_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_ViaNumMet34)
        self._DesignParameter['_VIAMet32Met4forRouting1']['_XYCoordinates'] = [[self._DesignParameter['_NMOS1_r'][
                                                                                    '_XYCoordinates'][0][0],
                                                                                self._DesignParameter[
                                                                                    '_AdditionalMet12Met2OnGate3'][
                                                                                    '_XYCoordinates'][3][
                                                                                    1]]]  ###(self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][1] + self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][3][1]) // 2]]

        del _ViaNumMet34

        _ViaNumMet34X = 1
        _ViaNumMet34Y = 2

        _ViaNumMet34 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _ViaNumMet34['_ViaMet32Met4NumberOfCOX'] = _ViaNumMet34X
        _ViaNumMet34['_ViaMet32Met4NumberOfCOY'] = _ViaNumMet34Y

        self._DesignParameter['_VIAMet32Met4forRoutingY'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None,
                                                  _Name='VIAMet32Met4forRoutingYIn{}'.format(_Name)))[0]
        self._DesignParameter['_VIAMet32Met4forRoutingY'][
            '_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_ViaNumMet34)
        self._DesignParameter['_VIAMet32Met4forRoutingY']['_XYCoordinates'] = [[self._DesignParameter['_NMOS4_r'][
                                                                                    '_XYCoordinates'][0][0] +
                                                                                self._DesignParameter['_NMOS4'][
                                                                                    '_DesignObj']._DesignParameter[
                                                                                    '_PODummyLayer']['_XYCoordinates'][
                                                                                    0][0],
                                                                                self.CeilMinSnapSpacing(self._DesignParameter['_NMOS4_r'][
                                                                                    '_XYCoordinates'][0][1] -
                                                                                self._DesignParameter[
                                                                                    '_VIAMet32Met4forRoutingY'][
                                                                                    '_DesignObj']._DesignParameter[
                                                                                    '_Met4Layer'][
                                                                                    '_YWidth'] // 2 + _DRCObj._MetalxMinWidth // 2, MinSnapSpacing)], \
                                                                               [self._DesignParameter['_PMOS4_r'][
                                                                                    '_XYCoordinates'][0][0] +
                                                                                self._DesignParameter['_PMOS4'][
                                                                                    '_DesignObj']._DesignParameter[
                                                                                    '_PODummyLayer']['_XYCoordinates'][
                                                                                    0][0],
                                                                                self.CeilMinSnapSpacing(self._DesignParameter['_PMOS4_r'][
                                                                                    '_XYCoordinates'][0][1] +
                                                                                self._DesignParameter[
                                                                                    '_VIAMet32Met4forRoutingY'][
                                                                                    '_DesignObj']._DesignParameter[
                                                                                    '_Met4Layer'][
                                                                                    '_YWidth'] // 2 - _DRCObj._MetalxMinWidth // 2, MinSnapSpacing)], \
                                                                               [self._DesignParameter['_NMOS4'][
                                                                                    '_XYCoordinates'][0][0] +
                                                                                self._DesignParameter['_NMOS4'][
                                                                                    '_DesignObj']._DesignParameter[
                                                                                    '_PODummyLayer']['_XYCoordinates'][
                                                                                    0][0],
                                                                                self.CeilMinSnapSpacing(self._DesignParameter['_NMOS4'][
                                                                                    '_XYCoordinates'][0][1] +
                                                                                self._DesignParameter[
                                                                                    '_VIAMet32Met4forRoutingY'][
                                                                                    '_DesignObj']._DesignParameter[
                                                                                    '_Met4Layer'][
                                                                                    '_YWidth'] // 2 - _DRCObj._MetalxMinWidth // 2, MinSnapSpacing)], \
                                                                               [self._DesignParameter['_PMOS4'][
                                                                                    '_XYCoordinates'][0][0] +
                                                                                self._DesignParameter['_PMOS4'][
                                                                                    '_DesignObj']._DesignParameter[
                                                                                    '_PODummyLayer']['_XYCoordinates'][
                                                                                    0][0],
                                                                                self.CeilMinSnapSpacing(self._DesignParameter['_PMOS4'][
                                                                                    '_XYCoordinates'][0][1] -
                                                                                self._DesignParameter[
                                                                                    '_VIAMet32Met4forRoutingY'][
                                                                                    '_DesignObj']._DesignParameter[
                                                                                    '_Met4Layer'][
                                                                                    '_YWidth'] // 2 + _DRCObj._MetalxMinWidth // 2, MinSnapSpacing)]]

        del _ViaNumMet34


        _ViaNumMet34X = 2
        _ViaNumMet34Y = 1

        _ViaNumMet34 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _ViaNumMet34['_ViaMet32Met4NumberOfCOX'] = _ViaNumMet34X
        _ViaNumMet34['_ViaMet32Met4NumberOfCOY'] = _ViaNumMet34Y

        self._DesignParameter['_VIAMet32Met4forRouting2'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None,
                                                  _Name='VIAMet32Met4forRouting2In{}'.format(_Name)))[0]
        self._DesignParameter['_VIAMet32Met4forRouting2'][
            '_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_ViaNumMet34)
        self._DesignParameter['_VIAMet32Met4forRouting2']['_XYCoordinates'] = [[self._DesignParameter['_NMOS1'][
                                                                                    '_XYCoordinates'][0][0], self.CeilMinSnapSpacing((
                                                                                            self._DesignParameter[
                                                                                                '_VIAPMOS1Poly2Met1'][
                                                                                                '_XYCoordinates'][0][
                                                                                                1] +
                                                                                            self._DesignParameter[
                                                                                                '_VIAPMOS1Poly2Met1'][
                                                                                                '_XYCoordinates'][2][
                                                                                                1]) // 2, MinSnapSpacing)]]

        del _ViaNumMet34

        _ViaNumMet23X = 2
        _ViaNumMet23Y = 1

        _ViaNumMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _ViaNumMet23['_ViaMet22Met3NumberOfCOX'] = _ViaNumMet23X
        _ViaNumMet23['_ViaMet22Met3NumberOfCOY'] = _ViaNumMet23Y

        self._DesignParameter['_VIAMet22Met3forRouting2'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='VIAMet22Met3forRouting2In{}'.format(_Name)))[0]
        self._DesignParameter['_VIAMet22Met3forRouting2']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaNumMet23)
        if self._DesignParameter['_VIAMet22Met3forRouting2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] * self._DesignParameter['_VIAMet22Met3forRouting2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']  < _DRCObj._MetalxMinArea :
            self._DesignParameter['_VIAMet22Met3forRouting2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = self.CeilMinSnapSpacing(_DRCObj._MetalxMinArea // self._DesignParameter['_VIAMet22Met3forRouting2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'], 2 * MinSnapSpacing)
        if self._DesignParameter['_VIAMet22Met3forRouting2']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] * self._DesignParameter['_VIAMet22Met3forRouting2']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']  < _DRCObj._MetalxMinArea :
            self._DesignParameter['_VIAMet22Met3forRouting2']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = self.CeilMinSnapSpacing(_DRCObj._MetalxMinArea // self._DesignParameter['_VIAMet22Met3forRouting2']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'], 2 * MinSnapSpacing)


        self._DesignParameter['_VIAMet22Met3forRouting2']['_XYCoordinates'] = [[self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing((self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][0][1] + self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][2][1]) // 2, MinSnapSpacing)]]

        del _ViaNumMet23

        _ViaNumMet12X = 2
        _ViaNumMet12Y = 1

        _ViaNumMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _ViaNumMet12['_ViaMet12Met2NumberOfCOX'] = _ViaNumMet12X
        _ViaNumMet12['_ViaMet12Met2NumberOfCOY'] = _ViaNumMet12Y

        self._DesignParameter['_VIAMet12Met2forRouting2'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None,
                                                  _Name='VIAMet12Met2forRouting2In{}'.format(_Name)))[0]
        self._DesignParameter['_VIAMet12Met2forRouting2'][
            '_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaNumMet12)
        self._DesignParameter['_VIAMet12Met2forRouting2']['_XYCoordinates'] = [[self._DesignParameter['_NMOS1'][
                                                                                    '_XYCoordinates'][0][0], self.CeilMinSnapSpacing((
                                                                                            self._DesignParameter[
                                                                                                '_VIAPMOS1Poly2Met1'][
                                                                                                '_XYCoordinates'][0][
                                                                                                1] +
                                                                                            self._DesignParameter[
                                                                                                '_VIAPMOS1Poly2Met1'][
                                                                                                '_XYCoordinates'][2][
                                                                                                1]) // 2, MinSnapSpacing)]]

        del _ViaNumMet12




        ## Right Metal 4 routing
        self._DesignParameter['_AdditionalMet4Routing3'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XYCoordinates=[], _Width=None)
        self._DesignParameter['_AdditionalMet4Routing3']['_Width'] = self._DesignParameter['_VIAMet32Met4forRouting2']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']
        self._DesignParameter['_AdditionalMet4Routing3']['_XYCoordinates'] = [[[self._DesignParameter[
                                                                                    '_VIAPMOS1Poly2Met1'][
                                                                                    '_XYCoordinates'][1][0],
                                                                                self._DesignParameter[
                                                                                    '_VIAPMOS1Poly2Met1'][
                                                                                    '_XYCoordinates'][1][1]],
                                                                               [self._DesignParameter[
                                                                                    '_VIAPMOS1Poly2Met1'][
                                                                                    '_XYCoordinates'][1][0], self.CeilMinSnapSpacing((
                                                                                            self._DesignParameter[
                                                                                                '_VIAPMOS1Poly2Met1'][
                                                                                                '_XYCoordinates'][0][
                                                                                                1] +
                                                                                            self._DesignParameter[
                                                                                                '_VIAPMOS1Poly2Met1'][
                                                                                                '_XYCoordinates'][2][
                                                                                                1]) // 2 + _DRCObj._MetalxMinWidth // 2, MinSnapSpacing)]]]


        self._DesignParameter['_AdditionalMet4Routing4'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XYCoordinates=[], _Width=None)
        self._DesignParameter['_AdditionalMet4Routing4']['_Width'] = self._DesignParameter['_AdditionalMet32Met4OverGate3']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']

        self._DesignParameter['_AdditionalMet4Routing4']['_XYCoordinates'] = [[[self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_AdditionalMet32Met4OverGate3']['_XYCoordinates'][0][1]], [self._DesignParameter['_NMOS3_r']['_XYCoordinates'][0][0], self._DesignParameter['_AdditionalMet32Met4OverGate3']['_XYCoordinates'][1][1]]]]



        ViaMet32Met4forRoutingoverVSS = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        ViaMet32Met4forRoutingoverVSS['_ViaMet32Met4NumberOfCOX'] = 1
        ViaMet32Met4forRoutingoverVSS['_ViaMet32Met4NumberOfCOY'] = 2
        self._DesignParameter['_ViaMet32Met4forRoutingoverVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4forRoutingoverVSSIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4forRoutingoverVSS']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**ViaMet32Met4forRoutingoverVSS)



        ViaMet22Met3forRoutingoverVSS = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        ViaMet22Met3forRoutingoverVSS['_ViaMet22Met3NumberOfCOX'] = 1
        ViaMet22Met3forRoutingoverVSS['_ViaMet22Met3NumberOfCOY'] = 2
        self._DesignParameter['_ViaMet22Met3forRoutingoverVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3forRoutingoverVSSIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3forRoutingoverVSS']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**ViaMet22Met3forRoutingoverVSS)
        if self._DesignParameter['_ViaMet22Met3forRoutingoverVSS']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] * self._DesignParameter['_ViaMet22Met3forRoutingoverVSS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] < _DRCObj._MetalxMinArea :
            self._DesignParameter['_ViaMet22Met3forRoutingoverVSS']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = self.CeilMinSnapSpacing(_DRCObj._MetalxMinArea // self._DesignParameter['_ViaMet22Met3forRoutingoverVSS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'], MinSnapSpacing)





        self._DesignParameter['_AdditionalMet4Routing1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=None)
        self._DesignParameter['_AdditionalMet4Routing1']['_Width'] = 2 * _DRCObj._MetalxMinWidth  #### ??????
        self._DesignParameter['_AdditionalMet4Routing1']['_XYCoordinates'] = [[[self.CeilMinSnapSpacing(self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] // 2 + self._DesignParameter['_AdditionalMet4Routing1']['_Width'] // 2 + _DRCObj._MetalxMinSpace2, MinSnapSpacing), self.CeilMinSnapSpacing((self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][0][1] + self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][2][1]) // 2, MinSnapSpacing)], \
                                                                               [self.CeilMinSnapSpacing(self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4_r']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] // 2 + self._DesignParameter['_AdditionalMet4Routing1']['_Width'] // 2 + _DRCObj._MetalxMinSpace2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet32Met4forRoutingoverVSS']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2, MinSnapSpacing)]]]



        ####[[self._DesignParameter['_ViaMet32Met4forRoutingoverVSS']['_XYCoordinates'][0], [self._DesignParameter['_ViaMet32Met4forRoutingoverVSS']['_XYCoordinates'][0][0], self._DesignParameter['_AdditionalMet32Met4OnMOS3']['_XYCoordinates'][0][1]], self._DesignParameter['_AdditionalMet32Met4OnMOS3']['_XYCoordinates'][0]]]








        ## Right Metal 2 routing
        self._DesignParameter['_AdditionalMet2Routing1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
        self._DesignParameter['_AdditionalMet2Routing1']['_Width'] = 2 * _DRCObj._MetalxMinWidth  #### ??????






        self._DesignParameter['_AdditionalMet2Routing1']['_XYCoordinates'] = [[[self.CeilMinSnapSpacing(self._DesignParameter['_PMOS4_r']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS4_r']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] // 2 + self._DesignParameter['_AdditionalMet2Routing1']['_Width'] // 2 + _DRCObj._MetalxMinSpace2, MinSnapSpacing), self.CeilMinSnapSpacing((self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][1][1] + self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][3][1]) // 2, MinSnapSpacing)], \
                                                                               [self.CeilMinSnapSpacing(self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] // 2 + self._DesignParameter['_AdditionalMet2Routing1']['_Width'] // 2 + _DRCObj._MetalxMinSpace2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet22Met3forRoutingoverVSS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2, MinSnapSpacing)]]]



        self._DesignParameter['_ViaMet22Met3forRoutingoverVSS']['_XYCoordinates'] = [[self._DesignParameter['_AdditionalMet2Routing1']['_XYCoordinates'][0][0][0], self._DesignParameter['_Met3RoutingOnNMOS']['_XYCoordinates'][0][1][1]]]

        del ViaMet22Met3forRoutingoverVSS

        self._DesignParameter['_ViaMet32Met4forRoutingoverVSS']['_XYCoordinates'] = [[self._DesignParameter['_AdditionalMet4Routing1']['_XYCoordinates'][0][0][0], self._DesignParameter['_Met3RoutingOnNMOS']['_XYCoordinates'][1][1][1]]]

        del ViaMet32Met4forRoutingoverVSS


        self._DesignParameter['_AdditionalMet3RoutingONNMOS4'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=None)
        self._DesignParameter['_AdditionalMet3RoutingONNMOS4']['_Width'] = self._DesignParameter['_Met3RoutingOnNMOS']['_Width']
        self._DesignParameter['_AdditionalMet3RoutingONNMOS4']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet22Met3forRoutingoverVSS']['_XYCoordinates'][0][0], self._DesignParameter['_Met3RoutingOnNMOS']['_XYCoordinates'][0][0][1]], [self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_Met3RoutingOnNMOS']['_XYCoordinates'][0][0][1]]], \
                                                                                    [[self._DesignParameter['_ViaMet32Met4forRoutingoverVSS']['_XYCoordinates'][0][0], self._DesignParameter['_Met3RoutingOnNMOS']['_XYCoordinates'][1][0][1]], [self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_Met3RoutingOnNMOS']['_XYCoordinates'][1][0][1]]]]




        _ViaMOS3Met34 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _ViaMOS3Met34['_ViaMet32Met4NumberOfCOX'] = 2
        _ViaMOS3Met34['_ViaMet32Met4NumberOfCOY'] = 1

        self._DesignParameter['_AdditionalMet32Met4OnMOS4'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='AdditionalMet32Met4OnMOS3In{}'.format(_Name)))[0]
        self._DesignParameter['_AdditionalMet32Met4OnMOS4']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_ViaMOS3Met34)
        self._DesignParameter['_AdditionalMet32Met4OnMOS4']['_XYCoordinates'] = [[self._DesignParameter['_AdditionalMet4Routing1']['_XYCoordinates'][0][0][0], self._DesignParameter['_AdditionalMet4Routing1']['_XYCoordinates'][0][0][1]]]

        del _ViaMOS3Met34


        _ViaMOS4Met23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _ViaMOS4Met23['_ViaMet22Met3NumberOfCOX'] = 2
        _ViaMOS4Met23['_ViaMet22Met3NumberOfCOY'] = 1

        self._DesignParameter['_AdditionalMet22Met3OnMOS4'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='AdditionalMet22Met3OnMOS4In{}'.format(_Name)))[0]
        self._DesignParameter['_AdditionalMet22Met3OnMOS4']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaMOS4Met23)
        if self._DesignParameter['_AdditionalMet22Met3OnMOS4']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] * self._DesignParameter['_AdditionalMet22Met3OnMOS4']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']  < _DRCObj._MetalxMinArea :
            self._DesignParameter['_AdditionalMet22Met3OnMOS4']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = self.CeilMinSnapSpacing(_DRCObj._MetalxMinArea // self._DesignParameter['_AdditionalMet22Met3OnMOS4']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'], 2 * MinSnapSpacing)
        if self._DesignParameter['_AdditionalMet22Met3OnMOS4']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] * self._DesignParameter['_AdditionalMet22Met3OnMOS4']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']  < _DRCObj._MetalxMinArea :
            self._DesignParameter['_AdditionalMet22Met3OnMOS4']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = self.CeilMinSnapSpacing(_DRCObj._MetalxMinArea // self._DesignParameter['_AdditionalMet22Met3OnMOS4']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'], 2 * MinSnapSpacing)

        self._DesignParameter['_AdditionalMet22Met3OnMOS4']['_XYCoordinates'] = self._DesignParameter['_AdditionalMet32Met4OnMOS4']['_XYCoordinates']

        del _ViaMOS4Met23

        _ViaMOS4Met12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _ViaMOS4Met12['_ViaMet12Met2NumberOfCOX'] = 2
        _ViaMOS4Met12['_ViaMet12Met2NumberOfCOY'] = 1

        self._DesignParameter['_AdditionalMet12Met2OnMOS4'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='AdditionalMet12Met2OnMOS4In{}'.format(_Name)))[0]
        self._DesignParameter['_AdditionalMet12Met2OnMOS4']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaMOS4Met12)
        if self._DesignParameter['_AdditionalMet12Met2OnMOS4']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] * self._DesignParameter['_AdditionalMet12Met2OnMOS4']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] < _DRCObj._MetalxMinArea :
            self._DesignParameter['_AdditionalMet12Met2OnMOS4']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = self.CeilMinSnapSpacing(_DRCObj._MetalxMinArea // self._DesignParameter['_AdditionalMet12Met2OnMOS4']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'], 2 * MinSnapSpacing)

        self._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'] = [[self._DesignParameter['_AdditionalMet4Routing1']['_XYCoordinates'][0][0][0], self._DesignParameter['_AdditionalMet4Routing1']['_XYCoordinates'][0][0][1]],[self._DesignParameter['_AdditionalMet2Routing1']['_XYCoordinates'][0][0][0], self._DesignParameter['_AdditionalMet2Routing1']['_XYCoordinates'][0][0][1]]]
        del _ViaMOS4Met12


        self._DesignParameter['_AdditionalMet1RoutingforMOS4'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
        self._DesignParameter['_AdditionalMet1RoutingforMOS4']['_Width'] = self._DesignParameter['_AdditionalMet12Met2OnMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        self._DesignParameter['_AdditionalMet1RoutingforMOS4']['_XYCoordinates'] = [[[self._DesignParameter['_AdditionalMet1GateRouting4']['_XYCoordinates'][-1][0][0], self._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][1][1]], [self._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][1][0], self._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][1][1]]], \
                                                                                    [[self._DesignParameter['_AdditionalMet1GateRouting4']['_XYCoordinates'][-1][0][0], self._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][0][1]], [self._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][0][1]]]]







        #####################################NWELL&SLVT&PPLayer Generation & Coordinates#######################################
        #####################################NWELL Generation & Coordinates#######################################
        _SupplyRailYwidth = _DRCObj._CoMinWidth * _NumSupplyCoY + _DRCObj._CoMinSpace * _NumSupplyCoY
        self._DesignParameter['_NWLayer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates=[], _Width=None)


        self._DesignParameter['_NWLayer']['_Width'] = self.CeilMinSnapSpacing(max(
            self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer'][ '_XWidth'] + 2 * _DRCObj._NwMinEnclosurePactive, self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0] - self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2 + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2 + 2 * _DRCObj._NwMinEnclosurePactive), MinSnapSpacing)
            #self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] + self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] + self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] + _tmpPolySpace * 3 + 2 * _DRCObj._NwMinSpacetoNactive), 2 * MinSnapSpacing)

        self._DesignParameter['_NWLayer']['_XYCoordinates'] = [[[self._DesignParameter['NbodyContact']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] + _SupplyRailYwidth // 2 + _DRCObj._NwMinEnclosurePactive, MinSnapSpacing)], \
                                                                [self._DesignParameter['NbodyContact']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2, MinSnapSpacing) - MinSnapSpacing]], \
                                                               [[self._DesignParameter['NbodyContact']['_XYCoordinates'][1][0], self.CeilMinSnapSpacing(self._DesignParameter['NbodyContact']['_XYCoordinates'][1][1] - _SupplyRailYwidth // 2 - _DRCObj._NwMinEnclosurePactive, MinSnapSpacing)], \
                                                                [self._DesignParameter['NbodyContact']['_XYCoordinates'][1][0], self.CeilMinSnapSpacing(self._DesignParameter['_PMOS1_r']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2, MinSnapSpacing) + MinSnapSpacing]]]

        #####################################XVT Generation & Coordinates#######################################
        # XVT Layer Calculation

        _XVTPMOSLayer = self._DesignParameter['_PMOS1']['_DesignObj']._XVTLayer
        _XVTPMOSLayerMappingName = self._DesignParameter['_PMOS1']['_DesignObj']._XVTLayerMappingName

        _XVTNMOSLayer = self._DesignParameter['_NMOS1']['_DesignObj']._XVTLayer
        _XVTNMOSLayerMappingName = self._DesignParameter['_NMOS1']['_DesignObj']._XVTLayerMappingName


        if _XVT != None:
            self._DesignParameter['_XVTPMOSLayer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping[_XVTPMOSLayerMappingName][0], _Datatype=DesignParameters._LayerMapping[_XVTPMOSLayerMappingName][1], _XYCoordinates=[], _Width=None)
            self._DesignParameter['_XVTPMOSLayer']['_Width'] = self.CeilMinSnapSpacing(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter[_XVTPMOSLayer]['_YWidth'], 2*MinSnapSpacing)
            self._DesignParameter['_XVTPMOSLayer']['_XYCoordinates'] = [[[self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] - self.CeilMinSnapSpacing(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter[_XVTPMOSLayer]['_XWidth'] // 2, MinSnapSpacing), self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]], [self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0] + self.CeilMinSnapSpacing(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter[_XVTPMOSLayer]['_XWidth'] // 2, MinSnapSpacing), self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1]]], \
                                                                        [[self._DesignParameter['_PMOS1_r']['_XYCoordinates'][0][0] - self.CeilMinSnapSpacing(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter[_XVTPMOSLayer]['_XWidth'] // 2, MinSnapSpacing), self._DesignParameter['_PMOS1_r']['_XYCoordinates'][0][1]], [self._DesignParameter['_PMOS4_r']['_XYCoordinates'][0][0] + self.CeilMinSnapSpacing(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter[_XVTPMOSLayer]['_XWidth'] // 2, MinSnapSpacing), self._DesignParameter['_PMOS4_r']['_XYCoordinates'][0][1]]]]

            self._DesignParameter['_XVTNMOSLayer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping[_XVTNMOSLayerMappingName][0], _Datatype=DesignParameters._LayerMapping[_XVTNMOSLayerMappingName][1], _XYCoordinates=[], _Width=None)
            self._DesignParameter['_XVTNMOSLayer']['_Width'] = self.CeilMinSnapSpacing(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter[_XVTNMOSLayer]['_YWidth'], 2*MinSnapSpacing)
            self._DesignParameter['_XVTNMOSLayer']['_XYCoordinates'] = [[[self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] - self.CeilMinSnapSpacing(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter[_XVTNMOSLayer]['_XWidth'] // 2, MinSnapSpacing), self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]], [self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self.CeilMinSnapSpacing(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter[_XVTNMOSLayer]['_XWidth'] // 2, MinSnapSpacing), self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1]]], \
                                                                         [[self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][0] - self.CeilMinSnapSpacing(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter[_XVTNMOSLayer]['_XWidth'] // 2, MinSnapSpacing), self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][1]], [self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][0] + self.CeilMinSnapSpacing(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter[_XVTNMOSLayer]['_XWidth'] // 2, MinSnapSpacing), self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][1]]]]

        #####################################NPLayer & PPLayer Generation & Coordinates#######################################

        self._DesignParameter['_PPLayer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[], _Width=None)
        self._DesignParameter['_PPLayer']['_Width'] = self.CeilMinSnapSpacing(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'], 2*MinSnapSpacing)
        self._DesignParameter['_PPLayer']['_XYCoordinates'] = [[[self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] - self.CeilMinSnapSpacing(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] // 2, MinSnapSpacing), self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]], [self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0] + self.CeilMinSnapSpacing(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] // 2, MinSnapSpacing), self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1]]], \
                                                               [[self._DesignParameter['_PMOS1_r']['_XYCoordinates'][0][0] - self.CeilMinSnapSpacing(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] // 2, MinSnapSpacing), self._DesignParameter['_PMOS1_r']['_XYCoordinates'][0][1]], [self._DesignParameter['_PMOS4_r']['_XYCoordinates'][0][0] + self.CeilMinSnapSpacing(self._DesignParameter['_PMOS4_r']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] // 2, MinSnapSpacing), self._DesignParameter['_PMOS4_r']['_XYCoordinates'][0][1]]]]

        if DesignParameters._Technology != '028nm' :
            self._DesignParameter['_NPLayer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0], _Datatype=DesignParameters._LayerMapping['NIMP'][1], _XYCoordinates=[], _Width=None)
            self._DesignParameter['_NPLayer']['_Width'] = self.CeilMinSnapSpacing(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth'], 2 * MinSnapSpacing)
            self._DesignParameter['_NPLayer']['_XYCoordinates'] = [[[self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] - self.CeilMinSnapSpacing(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth'] // 2,MinSnapSpacing), self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]], \
                                                                    [self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self.CeilMinSnapSpacing(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth'] // 2,MinSnapSpacing), self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1]]],\
                                                                   [[self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][0] - self.CeilMinSnapSpacing(self._DesignParameter['_NMOS1_r']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth'] // 2,MinSnapSpacing), self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][1]], \
                                                                    [self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][0] +  self.CeilMinSnapSpacing(self._DesignParameter['_NMOS4_r']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth'] // 2,MinSnapSpacing), self._DesignParameter['_NMOS4_r']['_XYCoordinates'][0][1]]]]

            self._DesignParameter['_PDKLayer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PDK'][0], _Datatype=DesignParameters._LayerMapping['PDK'][1], _XYCoordinates=[], _Width=None)
            self._DesignParameter['_PDKLayer']['_Width'] = self.CeilMinSnapSpacing(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth'], 2*MinSnapSpacing)
            self._DesignParameter['_PDKLayer']['_XYCoordinates'] = self._DesignParameter['_NPLayer']['_XYCoordinates']

            self._DesignParameter['_AdditionalPPLayer']  = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[], _Width=None)
            self._DesignParameter['_AdditionalPPLayer']['_Width'] = self.CeilMinSnapSpacing(self._DesignParameter['_PPLayer']['_XYCoordinates'][0][1][0] - self._DesignParameter['_PPLayer']['_XYCoordinates'][0][0][0], 2 * MinSnapSpacing)
            self._DesignParameter['_AdditionalPPLayer']['_XYCoordinates'] = [[[self._DesignParameter['NbodyContact']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]], \
                                                                              [self._DesignParameter['NbodyContact']['_XYCoordinates'][0][0], min(self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][0][1], self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][0][1], self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][0][1], self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][0][1]) - self.CeilMinSnapSpacing(self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2, MinSnapSpacing) - _DRCObj._PpMinEnclosureOfPo]], \
                                                                             [[self._DesignParameter['NbodyContact']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS1_r']['_XYCoordinates'][0][1]], \
                                                                              [self._DesignParameter['NbodyContact']['_XYCoordinates'][0][0], max(self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][1], self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][1][1], self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][1][1], self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][1][1]) + self.CeilMinSnapSpacing(self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2, MinSnapSpacing) + _DRCObj._PpMinEnclosureOfPo]]
                                                                             ]

            self._DesignParameter['_AdditionalNPLayer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0], _Datatype=DesignParameters._LayerMapping['NIMP'][1], _XYCoordinates=[], _Width=None)
            self._DesignParameter['_AdditionalNPLayer']['_Width'] = self.CeilMinSnapSpacing(self._DesignParameter['_AdditionalPPLayer']['_Width'], 2 * MinSnapSpacing)
            self._DesignParameter['_AdditionalNPLayer']['_XYCoordinates'] = [[[self._DesignParameter['PbodyContact']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]], \
                                                                              [self._DesignParameter['PbodyContact']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(max(self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][2][1], self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][2][1], self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][1], self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][2][1]) + self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _DRCObj._NpMinEnclosureOfPo, MinSnapSpacing)]], \
                                                                             [[self._DesignParameter['PbodyContact']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][1]], \
                                                                              [self._DesignParameter['PbodyContact']['_XYCoordinates'][0][0], self.FloorMinSnapSpacing(min(self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][3][1], self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][3][1], self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][3][1], self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][3][1]) - self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 - _DRCObj._NpMinEnclosureOfPo, MinSnapSpacing)]]
                                                                             ]

            self._DesignParameter['_AdditionalNWLayer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates=[], _Width=None)
            self._DesignParameter['_AdditionalNWLayer']['_Width'] = self.CeilMinSnapSpacing(self._DesignParameter['_NWLayer']['_Width'], 2*MinSnapSpacing)
            self._DesignParameter['_AdditionalNWLayer']['_XYCoordinates'] = [[self._DesignParameter['_NWLayer']['_XYCoordinates'][0][0],[self._DesignParameter['_NWLayer']['_XYCoordinates'][0][0][0], self._DesignParameter['_AdditionalPPLayer']['_XYCoordinates'][0][1][1]]],\
                                                                             [self._DesignParameter['_NWLayer']['_XYCoordinates'][1][0],[self._DesignParameter['_NWLayer']['_XYCoordinates'][1][0][0], self._DesignParameter['_AdditionalPPLayer']['_XYCoordinates'][1][1][1]]]]



        #####################################Pin Generation & Coordinates#######################################
        self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VDD')
        self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VSS')
        self._DesignParameter['_INpin'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='IN')
        self._DesignParameter['_INbpin'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='INb')
        self._DesignParameter['_OUTpin'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='OUT')
        self._DesignParameter['_OUTbpin'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='OUTb')

        self._DesignParameter['_VDDpin']['_XYCoordinates'] = [[0, _VDD2VSSHeightAtOneSide],
                                                              [0, 0 - _VDD2VSSHeightAtOneSide]]
        self._DesignParameter['_VSSpin']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['_INbpin']['_XYCoordinates'] = [
            [self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][0][0],
             self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_INpin']['_XYCoordinates'] = [
            [self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][1][0],
             self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][1][1]]]
        self._DesignParameter['_OUTpin']['_XYCoordinates'] = [[self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][0] +
                                                               self._DesignParameter['_NMOS1'][
                                                                   '_DesignObj']._DesignParameter[
                                                                   '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][
                                                                   0][0],
                                                               self._DesignParameter['_PMOS1_r']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_OUTbpin']['_XYCoordinates'] = [[self._DesignParameter['_NMOS1_r']['_XYCoordinates'][0][
                                                                    0] + self._DesignParameter['_NMOS1'][
                                                                    '_DesignObj']._DesignParameter[
                                                                    '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][
                                                                    0][0], 0 - (
                                                                self._DesignParameter['_PMOS1_r']['_XYCoordinates'][0][
                                                                    1])]]

        ########################### Additonal Power Line Generation (Metal First then Via) ###############################
        if _PowerLine == True:
            self._DesignParameter['_Met2LayerVDD'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met3LayerVDD'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL3'][0],
                _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met4LayerVDD'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL4'][0],
                _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)

            self._DesignParameter['_Met2LayerVDD']['_XWidth'] = \
            self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_Met2LayerVDD']['_YWidth'] = \
            self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_Met3LayerVDD']['_XWidth'] = \
            self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_Met3LayerVDD']['_YWidth'] = \
            self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_Met4LayerVDD']['_XWidth'] = \
            self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_Met4LayerVDD']['_YWidth'] = \
            self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']

            self._DesignParameter['_Met2LayerVDD']['_XYCoordinates'] = self._DesignParameter['NbodyContact']['_XYCoordinates']
            self._DesignParameter['_Met3LayerVDD']['_XYCoordinates'] = self._DesignParameter['NbodyContact']['_XYCoordinates']
            self._DesignParameter['_Met4LayerVDD']['_XYCoordinates'] = self._DesignParameter['NbodyContact']['_XYCoordinates']

            ############ Via Generations ##############
            _ViaNumVDDX = int(
                (self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer'][
                     '_XWidth'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (
                        _DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
            _ViaNumVDDY = int(
                (self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - _DRCObj._VIAxMinWidth) / (
                            _DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1

            if _ViaNumVDDX <= 1:
                _ViaNumVDDX = 1
                _ViaNumVDDY = int(
                    (self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - _DRCObj._VIAxMinWidth)/ (
                            _DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1
            if _ViaNumVDDY <= 1:
                _ViaNumVDDY = 1
                _ViaNumVDDX = int(
                    (self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (
                            _DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1


            _ViaVDDMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _ViaVDDMet12Met2['_ViaMet12Met2NumberOfCOX'] = _ViaNumVDDX
            _ViaVDDMet12Met2['_ViaMet12Met2NumberOfCOY'] = _ViaNumVDDY
            self._DesignParameter['_ViaMet12Met2VDD'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None,
                                                      _Name='ViaMet12Met2VDDIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2VDD']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(
                **_ViaVDDMet12Met2)
            self._DesignParameter['_ViaMet12Met2VDD']['_XYCoordinates'] = self._DesignParameter['NbodyContact'][
                '_XYCoordinates']

            _ViaVDDMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _ViaVDDMet22Met3['_ViaMet22Met3NumberOfCOX'] = _ViaNumVDDX
            _ViaVDDMet22Met3['_ViaMet22Met3NumberOfCOY'] = _ViaNumVDDY
            self._DesignParameter['_ViaMet22Met3VDD'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None,
                                                      _Name='ViaMet22Met3VDDIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3VDD']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(
                **_ViaVDDMet22Met3)
            self._DesignParameter['_ViaMet22Met3VDD']['_XYCoordinates'] = self._DesignParameter['NbodyContact'][
                '_XYCoordinates']

            _ViaVDDMet32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            _ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOX'] = _ViaNumVDDX
            _ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOY'] = _ViaNumVDDY
            self._DesignParameter['_ViaMet32Met4VDD'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None,
                                                      _Name='ViaMet32Met4VDDIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet32Met4VDD']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(
                **_ViaVDDMet32Met4)
            self._DesignParameter['_ViaMet32Met4VDD']['_XYCoordinates'] = self._DesignParameter['NbodyContact'][
                '_XYCoordinates']


if __name__ == '__main__':

    for i in range(1,2) :
        _Finger1 = 5#random.randint(1, 16)
        _Finger2 = 1#random.randint(1, 16)
        _Finger3 = 2#random.randint(1, 16)
        _Finger4 = 2#random.randint(1, 16)
        _NPRatio = 3#round(2 + random.random())
        _SRRandWidth = 350#random.randrange(350,700,50)
        _NMOSChannelWidth = _SRRandWidth
        _PMOSChannelWidth = int(_SRRandWidth * _NPRatio)


        _ChannelLength = 30

        _VDD2VSSHeightAtOneSide = None
        _NumSupplyCoX = None
        _NumSupplyCoY = None


        _Dummy = True
        _XVT = 'SLVT'
        _PowerLine = False

        libname = 'SRLatch'
        cellname = 'SRLatch'
        _fileName = cellname + '.gds'

        InputParams = dict(
            _Finger1 = _Finger1,
            _Finger2 = _Finger2,
            _Finger3 = _Finger3,
            _Finger4 = _Finger4,

            _NMOSChannelWidth1 = _NMOSChannelWidth,
            _NMOSChannelWidth2 = _NMOSChannelWidth,
            _NMOSChannelWidth3 = _NMOSChannelWidth,
            _NMOSChannelWidth4 = _NMOSChannelWidth,
            _NPRatio = _NPRatio,
            _PMOSChannelWidth1 = _NPRatio * _NMOSChannelWidth,
            _PMOSChannelWidth2 = _NPRatio * _NMOSChannelWidth,
            _PMOSChannelWidth3 = _NPRatio * _NMOSChannelWidth,
            _PMOSChannelWidth4 = _NPRatio * _NMOSChannelWidth,

            _ChannelLength = _ChannelLength,

            _VDD2VSSHeightAtOneSide = None,
            _NumSupplyCoX = None,
            _NumSupplyCoY = None,
            _Dummy = _Dummy,
            _XVT = _XVT,
            _PowerLine = _PowerLine

        )


        LayoutObj = _SRLatch(_DesignParameter=None, _Name=cellname)
        LayoutObj._CalculateDesignParameter(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
        testStreamFile = open('./{}'.format(_fileName), 'wb')
        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        import ftplib
