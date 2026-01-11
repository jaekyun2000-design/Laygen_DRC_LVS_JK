from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1

from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import StickDiagram
from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import NMOSWithDummy
from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import PMOSWithDummy_iksu
from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import NbodyContact
from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import PbodyContact
from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import ViaPoly2Met1
from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import ViaMet12Met2
from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import ViaMet22Met3
from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import ViaMet32Met4
from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import ContGeneration
import math
from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import DesignParameters
from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import user_define_exceptions

import copy
import time
from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import DRC
from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import psubring
import random
import ftplib
from ftplib import FTP
import base64

class _PMOSWithDummyOfSlicer(StickDiagram_KJH1._StickDiagram_KJH):
    _ParametersForDesignCalculation=dict(
                                        _CLKinputPMOSFinger1=None, _CLKinputPMOSFinger2=None, _PMOSFinger=None, _PMOSChannelWidth=None,
                                        _ChannelLength=None, _Dummy=False, _XVT=None, _GuardringWidth=None, _Guardring=False,
                                        _NumSupplyCOY=None, _NumSupplyCOX=None, _SupplyMet1XWidth=None, _SupplyMet1YWidth=None, _VDD2VSSHeight=None,
                                        _NumVIAPoly2Met1COX=None, _NumVIAPoly2Met1COY=None, _NumVIAMet12COX=None, _NumVIAMet12COY=None)


    def __init__(self, _DesignParameter=None, _Name='PMOSWithDummyOfSlicer'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),_XYcoordAsCent=dict(_XYcoordAsCent=1),)


    def _CalculateDesignParameter(self, _CLKinputPMOSFinger1 = None, _CLKinputPMOSFinger2 = None, _PMOSFinger = None, _PMOSChannelWidth = None,
                                      _ChannelLength = None, _Dummy = False, _XVT = None, _GuardringWidth = None, _Guardring = False,
                                      _NumSupplyCOY=None, _NumSupplyCOX=None, _SupplyMet1XWidth=None, _SupplyMet1YWidth=None, _VDD2VSSHeight = None,
                                      _NumVIAPoly2Met1COX=None, _NumVIAPoly2Met1COY=None, _NumVIAMet12COX=None, _NumVIAMet12COY=None
                                 ):

            _DRCObj = DRC.DRC()
            _XYCoordinateOfPMOS = [[0, 0]]
            #_PODummyWidth = 30
            MinSnapSpacing = _DRCObj._MinSnapSpacing
            _Name = self._DesignParameter['_Name']['_Name']
            _CLKinputPMOSFinger = _CLKinputPMOSFinger1 + _CLKinputPMOSFinger2

            ##############################################################################################################################################################
            ################################################################### PMOS Generation  #########################################################################
            ##############################################################################################################################################################

            # PMOS1(CLK input) Generation
            _PMOS1inputs = copy.deepcopy(PMOSWithDummy_iksu._PMOS._ParametersForDesignCalculation)
            _PMOS1inputs['_PMOSNumberofGate'] = _CLKinputPMOSFinger1 + _CLKinputPMOSFinger2
            _PMOS1inputs['_PMOSChannelWidth'] = _PMOSChannelWidth
            _PMOS1inputs['_PMOSChannellength'] = _ChannelLength
            _PMOS1inputs['_PMOSDummy'] = _Dummy
            _PMOS1inputs['_XVT'] = _XVT
            self._DesignParameter['_PMOS1'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy_iksu._PMOS(_DesignParameter=None, _Name='{}:PMOS1'.format(_Name)))[0]
            self._DesignParameter['_PMOS1']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOS1inputs)

            # PMOS2(CLK input) Generation
            _PMOS2inputs = copy.deepcopy(PMOSWithDummy_iksu._PMOS._ParametersForDesignCalculation)
            _PMOS2inputs['_PMOSNumberofGate'] = _CLKinputPMOSFinger1 + _CLKinputPMOSFinger2
            _PMOS2inputs['_PMOSChannelWidth'] = _PMOSChannelWidth
            _PMOS2inputs['_PMOSChannellength'] = _ChannelLength
            _PMOS2inputs['_PMOSDummy'] = _Dummy
            _PMOS2inputs['_XVT'] = _XVT
            self._DesignParameter['_PMOS2'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy_iksu._PMOS(_DesignParameter=None, _Name='{}:PMOS2'.format(_Name)))[0]
            self._DesignParameter['_PMOS2']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOS2inputs)

            # PMOS3 Generation
            _PMOS3inputs = copy.deepcopy(PMOSWithDummy_iksu._PMOS._ParametersForDesignCalculation)
            _PMOS3inputs['_PMOSNumberofGate'] = _PMOSFinger
            _PMOS3inputs['_PMOSChannelWidth'] = _PMOSChannelWidth
            _PMOS3inputs['_PMOSChannellength'] = _ChannelLength
            _PMOS3inputs['_PMOSDummy'] = _Dummy
            _PMOS3inputs['_XVT'] = _XVT
            self._DesignParameter['_PMOS3'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy_iksu._PMOS(_DesignParameter=None, _Name='{}:PMOS3'.format(_Name)))[0]
            self._DesignParameter['_PMOS3']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOS3inputs)

            # PMOS4 Generation
            _PMOS4inputs = copy.deepcopy(PMOSWithDummy_iksu._PMOS._ParametersForDesignCalculation)
            _PMOS4inputs['_PMOSNumberofGate'] = _PMOSFinger
            _PMOS4inputs['_PMOSChannelWidth'] = _PMOSChannelWidth
            _PMOS4inputs['_PMOSChannellength'] = _ChannelLength
            _PMOS4inputs['_PMOSDummy'] = _Dummy
            _PMOS4inputs['_XVT'] = _XVT
            self._DesignParameter['_PMOS4'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy_iksu._PMOS(_DesignParameter=None, _Name='{}:PMOS4'.format(_Name)))[0]
            self._DesignParameter['_PMOS4']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOS4inputs)

            #############################################################################################################################################################################
            ################################################################### PMOS Gate Generation ####################################################################################
            #############################################################################################################################################################################
            # CONT Generation for PMOS1 Gate
            _LenBtwPMOSGates = self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] - \
            self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0]

            _VIAPMOSPoly2Met1PMOS1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
            _tmpNumCOX = int(_LenBtwPMOSGates // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

            if _tmpNumCOX < 1:
                _VIAPMOSPoly2Met1PMOS1['_ViaPoly2Met1NumberOfCOX'] = 1
                _VIAPMOSPoly2Met1PMOS1['_ViaPoly2Met1NumberOfCOY'] = 1
            else:
                _VIAPMOSPoly2Met1PMOS1['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX
                _VIAPMOSPoly2Met1PMOS1['_ViaPoly2Met1NumberOfCOY'] = 1

            self._DesignParameter['_VIAPMOSPoly2Met1PMOS1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None,_Name='{}:ViaPoly2Met1OnPMOSGate1'.format(_Name)))[0]
            self._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIAPMOSPoly2Met1PMOS1)
            del _tmpNumCOX
            del _LenBtwPMOSGates

            # CONT Generation for PMOS2 Gate
            _LenBtwPMOSGates = self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] - \
            self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0]

            _VIAPMOSPoly2Met1PMOS2 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
            _tmpNumCOX = int(_LenBtwPMOSGates // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

            if _tmpNumCOX < 1:
                _VIAPMOSPoly2Met1PMOS2['_ViaPoly2Met1NumberOfCOX'] = 1
                _VIAPMOSPoly2Met1PMOS2['_ViaPoly2Met1NumberOfCOY'] = 1
            else:
                _VIAPMOSPoly2Met1PMOS2['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX
                _VIAPMOSPoly2Met1PMOS2['_ViaPoly2Met1NumberOfCOY'] = 1

            self._DesignParameter['_VIAPMOSPoly2Met1PMOS2'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None,_Name='{}:ViaPoly2Met1OnPMOSGate2'.format(_Name)))[0]
            self._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIAPMOSPoly2Met1PMOS2)
            del _tmpNumCOX
            del _LenBtwPMOSGates

            # CONT Generation for PMOS3 Gate
            _LenBtwPMOSGates = self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] - \
            self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0]

            _VIAPMOSPoly2Met1PMOS3 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
            _tmpNumCOX = int(_LenBtwPMOSGates // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

            if _tmpNumCOX < 1:
                _VIAPMOSPoly2Met1PMOS3['_ViaPoly2Met1NumberOfCOX'] = 1
                _VIAPMOSPoly2Met1PMOS3['_ViaPoly2Met1NumberOfCOY'] = 1
            else:
                _VIAPMOSPoly2Met1PMOS3['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX
                _VIAPMOSPoly2Met1PMOS3['_ViaPoly2Met1NumberOfCOY'] = 1

            self._DesignParameter['_VIAPMOSPoly2Met1PMOS3'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None,_Name='{}:ViaPoly2Met1OnPMOSGate3'.format(_Name)))[0]
            self._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIAPMOSPoly2Met1PMOS3)
            del _tmpNumCOX
            del _LenBtwPMOSGates
            #
            # CONT Generation for PMOS4 Gate
            _LenBtwPMOSGates = self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] - \
            self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0]

            _VIAPMOSPoly2Met1PMOS4 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
            _tmpNumCOX = int(_LenBtwPMOSGates // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

            if _tmpNumCOX < 1:
                _VIAPMOSPoly2Met1PMOS4['_ViaPoly2Met1NumberOfCOX'] = 1
                _VIAPMOSPoly2Met1PMOS4['_ViaPoly2Met1NumberOfCOY'] = 1
            else:
                _VIAPMOSPoly2Met1PMOS4['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX
                _VIAPMOSPoly2Met1PMOS4['_ViaPoly2Met1NumberOfCOY'] = 1

            self._DesignParameter['_VIAPMOSPoly2Met1PMOS4'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None,_Name='{}:ViaPoly2Met1OnPMOSGate4'.format(_Name)))[0]
            self._DesignParameter['_VIAPMOSPoly2Met1PMOS4']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIAPMOSPoly2Met1PMOS4)
            del _tmpNumCOX
            del _LenBtwPMOSGates

            ##################################################################################################################################################################################
            #################################################################### Coordinate Settings #########################################################################################
            ##################################################################################################################################################################################

            # _LengthPMOSBtwPO = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + _ChannelLength
            if DesignParameters._Technology == '028nm':
                _LengthPMOSBtwPO = _DRCObj.DRCPolyMinSpace(_Width=_PMOSChannelWidth, _ParallelLength=_ChannelLength) + _ChannelLength
            else:
                _LengthPMOSBtwPO = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + _ChannelLength
            _LengthPMOSBtwCOnDummy= self.CeilMinSnapSpacing(_DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth//2) + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD + _ChannelLength//2, MinSnapSpacing)
            _LengthPMOSBtwPOnDummy= self.CeilMinSnapSpacing(_DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + _DRCObj._PolygateMinSpace2Co) + _ChannelLength // 2 + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD + _ChannelLength//2, MinSnapSpacing)

            # PMOS3(L) Coordinate Setting
            if (_PMOSFinger % 2) == 0:
                # _xycoordinatetmp = [[self.CeilMinSnapSpacing(_XYCoordinateOfPMOS[0][0] - (_LengthPMOSBtwPO*(_PMOSFinger//2) + _LengthPMOSBtwCOnDummy) - _DRCObj._PolygateMinSpace//2 - _ChannelLength//2, MinSnapSpacing), _XYCoordinateOfPMOS[0][1]]]
                _xycoordinatetmp = [[self.CeilMinSnapSpacing(_XYCoordinateOfPMOS[0][0] - (_LengthPMOSBtwPO*(_PMOSFinger//2) + _LengthPMOSBtwCOnDummy) - _LengthPMOSBtwPO//2 - _ChannelLength//2, MinSnapSpacing), _XYCoordinateOfPMOS[0][1]]]
                self._DesignParameter['_PMOS3']['_XYCoordinates'] = _xycoordinatetmp
                tmp=_xycoordinatetmp[0][0]
            elif (_PMOSFinger % 2) == 1:
                # _xycoordinatetmp = [[self.CeilMinSnapSpacing(_XYCoordinateOfPMOS[0][0] - (_LengthPMOSBtwPO*(_PMOSFinger//2) + _LengthPMOSBtwPOnDummy) - _DRCObj._PolygateMinSpace//2 - _ChannelLength//2, MinSnapSpacing), _XYCoordinateOfPMOS[0][1]]]
                _xycoordinatetmp = [[self.CeilMinSnapSpacing(_XYCoordinateOfPMOS[0][0] - (_LengthPMOSBtwPO*(_PMOSFinger//2) + _LengthPMOSBtwPOnDummy) - _LengthPMOSBtwPO//2 - _ChannelLength//2, MinSnapSpacing), _XYCoordinateOfPMOS[0][1]]]
                self._DesignParameter['_PMOS3']['_XYCoordinates'] = _xycoordinatetmp
                tmp=_xycoordinatetmp[0][0]

            # PMOS4(R) Coordinate Setting
            if (_PMOSFinger % 2) == 0:
                # self._DesignParameter['_PMOS4']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(_XYCoordinateOfPMOS[0][0] + (_LengthPMOSBtwPO*(_PMOSFinger//2) + _LengthPMOSBtwCOnDummy) + _DRCObj._PolygateMinSpace//2 + _ChannelLength//2, MinSnapSpacing), _XYCoordinateOfPMOS[0][1]]]
                self._DesignParameter['_PMOS4']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(_XYCoordinateOfPMOS[0][0] + (_LengthPMOSBtwPO*(_PMOSFinger//2) + _LengthPMOSBtwCOnDummy) + _LengthPMOSBtwPO//2 + _ChannelLength//2, MinSnapSpacing), _XYCoordinateOfPMOS[0][1]]]
            elif (_PMOSFinger % 2) == 1:
                # self._DesignParameter['_PMOS4']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(_XYCoordinateOfPMOS[0][0] + (_LengthPMOSBtwPO*(_PMOSFinger//2) + _LengthPMOSBtwPOnDummy) + _DRCObj._PolygateMinSpace//2 + _ChannelLength//2, MinSnapSpacing), _XYCoordinateOfPMOS[0][1]]]
                self._DesignParameter['_PMOS4']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(_XYCoordinateOfPMOS[0][0] + (_LengthPMOSBtwPO*(_PMOSFinger//2) + _LengthPMOSBtwPOnDummy) + _LengthPMOSBtwPO//2 + _ChannelLength//2, MinSnapSpacing), _XYCoordinateOfPMOS[0][1]]]

            # CLK PMOS1(L) Coordinate Setting
            if (_CLKinputPMOSFinger % 2) == 0:
                # self._DesignParameter['_PMOS1']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(_XYCoordinateOfPMOS[0][0] - abs(2*tmp) - (_LengthPMOSBtwPO*(_CLKinputPMOSFinger//2) + _LengthPMOSBtwCOnDummy) - _DRCObj._PolygateMinSpace//2 - _ChannelLength//2, MinSnapSpacing), _XYCoordinateOfPMOS[0][1]]]
                self._DesignParameter['_PMOS1']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(_XYCoordinateOfPMOS[0][0] - abs(2*tmp) - (_LengthPMOSBtwPO*(_CLKinputPMOSFinger//2) + _LengthPMOSBtwCOnDummy) - _LengthPMOSBtwPO//2 - _ChannelLength//2, MinSnapSpacing), _XYCoordinateOfPMOS[0][1]]]
            elif (_CLKinputPMOSFinger % 2) == 1:
                # self._DesignParameter['_PMOS1']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(_XYCoordinateOfPMOS[0][0] - abs(2*tmp) - (_LengthPMOSBtwPO*(_CLKinputPMOSFinger//2) + _LengthPMOSBtwPOnDummy) - _DRCObj._PolygateMinSpace//2 - _ChannelLength//2, MinSnapSpacing), _XYCoordinateOfPMOS[0][1]]]
                self._DesignParameter['_PMOS1']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(_XYCoordinateOfPMOS[0][0] - abs(2*tmp) - (_LengthPMOSBtwPO*(_CLKinputPMOSFinger//2) + _LengthPMOSBtwPOnDummy) - _LengthPMOSBtwPO//2 - _ChannelLength//2, MinSnapSpacing), _XYCoordinateOfPMOS[0][1]]]

            # CLK PMOS2(R) Coordinate Setting
            if (_CLKinputPMOSFinger % 2) == 0:
                # self._DesignParameter['_PMOS2']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(_XYCoordinateOfPMOS[0][0] + abs(2*tmp) + (_LengthPMOSBtwPO*(_CLKinputPMOSFinger//2) + _LengthPMOSBtwCOnDummy)  + _DRCObj._PolygateMinSpace//2 + _ChannelLength//2, MinSnapSpacing), _XYCoordinateOfPMOS[0][1]]]
                self._DesignParameter['_PMOS2']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(_XYCoordinateOfPMOS[0][0] + abs(2*tmp) + (_LengthPMOSBtwPO*(_CLKinputPMOSFinger//2) + _LengthPMOSBtwCOnDummy)  + _LengthPMOSBtwPO//2 + _ChannelLength//2, MinSnapSpacing), _XYCoordinateOfPMOS[0][1]]]
            elif (_CLKinputPMOSFinger % 2) == 1:
                # self._DesignParameter['_PMOS2']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(_XYCoordinateOfPMOS[0][0] + abs(2*tmp) + (_LengthPMOSBtwPO*(_CLKinputPMOSFinger//2) + _LengthPMOSBtwPOnDummy)  + _DRCObj._PolygateMinSpace//2 + _ChannelLength//2, MinSnapSpacing), _XYCoordinateOfPMOS[0][1]]]
                self._DesignParameter['_PMOS2']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(_XYCoordinateOfPMOS[0][0] + abs(2*tmp) + (_LengthPMOSBtwPO*(_CLKinputPMOSFinger//2) + _LengthPMOSBtwPOnDummy)  + _LengthPMOSBtwPO//2 + _ChannelLength//2, MinSnapSpacing), _XYCoordinateOfPMOS[0][1]]]




















            ##################################################################################################################################################################################
            ################################################################# PMOS VIA1 Generation ###########################################################################################
            ##################################################################################################################################################################################
            # VIA Generation for PMOS12 Output
            _VIACLKPMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _VIACLKPMOSMet12['_ViaMet12Met2NumberOfCOX'] = 1
            _ViaNumY = int((_PMOSChannelWidth - 2 * _DRCObj._Metal1MinEnclosureVia12) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
            if _ViaNumY < 1 :
                _ViaNumY = 1
            _VIACLKPMOSMet12['_ViaMet12Met2NumberOfCOY'] = _ViaNumY
            self._DesignParameter['_ViaMet12Met2OnPMOSOutput1'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='{}:ViaMet12Met2OnPMOSOutput1'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_VIACLKPMOSMet12)

            # tmp = []
            # for i in range(0, len(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])) :
            #     tmp.append([self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1]])

            # _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            if DesignParameters._Technology == '028nm':
                _LengthPMOSBtwMet1 = _DRCObj.DRCPolyMinSpace(_Width=_PMOSChannelWidth, _ParallelLength=_ChannelLength) + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            else:
                _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            tmp = []
            tmpx = []
            PMOS12tmp = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0] - _LengthPMOSBtwMet1]
            PMOS12tmp2 = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] - _LengthPMOSBtwMet1, self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0]]
            PMOS12tmp3 = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0]]
            # PMOS12tmp4 = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0]]
            if (_CLKinputPMOSFinger % 2) == 0:
                if (_CLKinputPMOSFinger1 % 2) == 0:
                    for j in PMOS12tmp3:
                        for i in range(0, int(_CLKinputPMOSFinger//2)):
                            tmpx=[self.CeilMinSnapSpacing(j - (_CLKinputPMOSFinger//2 - 1)*_LengthPMOSBtwMet1 + (2*i)*_LengthPMOSBtwMet1, MinSnapSpacing), self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]
                            tmp.append(tmpx)
                elif (_CLKinputPMOSFinger1 % 2) == 1:
                    for j in PMOS12tmp3:
                        for i in range(0, int(_CLKinputPMOSFinger//2 + 1)):
                            tmpx = [self.CeilMinSnapSpacing(j - (_CLKinputPMOSFinger//2) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1, MinSnapSpacing), self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]
                            tmp.append(tmpx)

            elif (_CLKinputPMOSFinger % 2) == 1:
                if (_CLKinputPMOSFinger1 % 2) == 0:
                    for j in PMOS12tmp:
                        for i in range(0, int(_CLKinputPMOSFinger//2 + 1)):
                            tmpx=[self.CeilMinSnapSpacing(j - (_CLKinputPMOSFinger//2-0.5)*_LengthPMOSBtwMet1 + (2*i)*_LengthPMOSBtwMet1, MinSnapSpacing), self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]
                            tmp.append(tmpx)
                elif (_CLKinputPMOSFinger1 % 2) == 1:
                    for j in PMOS12tmp2:
                        for i in range(0, int(_CLKinputPMOSFinger//2 + 1)):
                            tmpx = [self.CeilMinSnapSpacing(j - (_CLKinputPMOSFinger//2-0.5) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1, MinSnapSpacing), self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]
                            tmp.append(tmpx)

            self._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'] = tmp
            del tmp
            del tmpx
            del _ViaNumY
            print('x')

            # VIA Generation for PMOS23 Output
            _VIACLKPMOSMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _VIACLKPMOSMet23['_ViaMet22Met3NumberOfCOX'] = 1
            _ViaNumY =  int((_PMOSChannelWidth - 2 * _DRCObj._Metal1MinEnclosureVia12) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
            if _ViaNumY < 1 :
                _ViaNumY = 1
            _VIACLKPMOSMet23['_ViaMet22Met3NumberOfCOY'] = _ViaNumY
            self._DesignParameter['_ViaMet22Met3OnPMOSOutput1'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='{}:ViaMet22Met3OnPMOSOutput1'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3OnPMOSOutput1']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_VIACLKPMOSMet23)

            # _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            if DesignParameters._Technology == '028nm':
                _LengthPMOSBtwMet1 = _DRCObj.DRCPolyMinSpace(_Width=_PMOSChannelWidth, _ParallelLength=_ChannelLength) + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            else:
                _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            tmp = []

            # for i in range(0, int((_CLKinputPMOSFinger1 + 1) // 2)) :
            #     tmp.append([self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1]])
            #     tmp.append([-(self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0]), self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1]])

            tmpx = []
            tmpy = []
            PMOS23tmp = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0] - _LengthPMOSBtwMet1]
            PMOS23tmp2 = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] - _LengthPMOSBtwMet1, self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0]]
            PMOS23tmp3 = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0]]
            # PMOS12tmp4 = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0]]
            if (_CLKinputPMOSFinger % 2) == 0:
                if (_CLKinputPMOSFinger1 % 2) == 0:
                    for j in PMOS12tmp3:
                        for i in range(0, _CLKinputPMOSFinger//2):
                            tmpx=[self.CeilMinSnapSpacing(j - (_CLKinputPMOSFinger//2 - 1)*_LengthPMOSBtwMet1 + (2*i)*_LengthPMOSBtwMet1, MinSnapSpacing), self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]
                            tmp.append(tmpx)
                elif (_CLKinputPMOSFinger1 % 2) == 1:
                    for j in PMOS12tmp3:
                    #for j in PMOS12tmp3:
                        for i in range(0, _CLKinputPMOSFinger//2 + 1):
                            tmpx = [self.CeilMinSnapSpacing(j - (_CLKinputPMOSFinger//2) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1, MinSnapSpacing), self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]
                            tmp.append(tmpx)

            elif (_CLKinputPMOSFinger % 2) == 1:
                if (_CLKinputPMOSFinger1 % 2) == 0:
                    for j in PMOS12tmp:
                        for i in range(0, int(_CLKinputPMOSFinger//2 + 1)):
                            tmpx=[self.CeilMinSnapSpacing(j - (_CLKinputPMOSFinger//2-0.5)*_LengthPMOSBtwMet1 + (2*i)*_LengthPMOSBtwMet1, MinSnapSpacing), self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]
                            tmp.append(tmpx)
                elif (_CLKinputPMOSFinger1 % 2) == 1:
                    for j in PMOS12tmp2:
                        for i in range(0, int(_CLKinputPMOSFinger//2 + 1)):
                            tmpx = [self.CeilMinSnapSpacing(j - (_CLKinputPMOSFinger//2-0.5) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1, MinSnapSpacing), self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]
                            tmp.append(tmpx)

            self._DesignParameter['_ViaMet22Met3OnPMOSOutput1']['_XYCoordinates'] = tmp[0:int((_CLKinputPMOSFinger1+1) // 2)]
            for i in range(len(self._DesignParameter['_ViaMet22Met3OnPMOSOutput1']['_XYCoordinates'])):
                tmpy.append([-1 * self._DesignParameter['_ViaMet22Met3OnPMOSOutput1']['_XYCoordinates'][i][0], self._DesignParameter['_ViaMet22Met3OnPMOSOutput1']['_XYCoordinates'][i][1]])
            self._DesignParameter['_ViaMet22Met3OnPMOSOutput1']['_XYCoordinates'] = tmp[0:int((_CLKinputPMOSFinger1+1) // 2)] + tmpy

            del tmp
            del tmpx
            del tmpy
            del _ViaNumY
            print('x')

            # VIA Generation for PMOS34 Output
            _VIACLKPMOSMet34 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            _VIACLKPMOSMet34['_ViaMet32Met4NumberOfCOX'] = 1
            _ViaNumY =  int((_PMOSChannelWidth - 2 * _DRCObj._Metal1MinEnclosureVia12) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
            if _ViaNumY < 1:
                _ViaNumY = 1
            _VIACLKPMOSMet34['_ViaMet32Met4NumberOfCOY'] = _ViaNumY
            self._DesignParameter['_ViaMet32Met4OnPMOSOutput1'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='{}:ViaMet32Met4OnPMOSOutput1'.format(_Name)))[0]
            self._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_VIACLKPMOSMet34)

            # _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + \
            #                      self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            if DesignParameters._Technology == '028nm':
                _LengthPMOSBtwMet1 = _DRCObj.DRCPolyMinSpace(_Width=_PMOSChannelWidth, _ParallelLength=_ChannelLength) + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            else:
                _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            tmp = []
            tmpx = []
            tmpy = []
            PMOS23tmp = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0],
                         self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0] - _LengthPMOSBtwMet1]
            PMOS23tmp2 = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] - _LengthPMOSBtwMet1,
                          self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0]]
            PMOS23tmp3 = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0],
                          self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0]]
            PMOS12tmp4 = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0]]
            if (_CLKinputPMOSFinger % 2) == 0:
                if (_CLKinputPMOSFinger1 % 2) == 0:
                    for j in PMOS12tmp3:
                        for i in range(0, int(_CLKinputPMOSFinger // 2)):
                            tmpx = [self.CeilMinSnapSpacing(j - (_CLKinputPMOSFinger // 2 - 1) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1, MinSnapSpacing),
                                self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]
                            tmp.append(tmpx)
                elif (_CLKinputPMOSFinger1 % 2) == 1:
                    for j in PMOS12tmp3:
                        for i in range(0, int(_CLKinputPMOSFinger // 2 + 1)):
                            tmpx = [self.CeilMinSnapSpacing(j - (_CLKinputPMOSFinger // 2) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1, MinSnapSpacing),
                                    self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]
                            tmp.append(tmpx)

            elif (_CLKinputPMOSFinger % 2) == 1:
                if (_CLKinputPMOSFinger1 % 2) == 0:
                    for j in PMOS12tmp:
                        for i in range(0, int(_CLKinputPMOSFinger // 2 + 1)):
                            tmpx = [
                                self.CeilMinSnapSpacing(j - (_CLKinputPMOSFinger // 2 - 0.5) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1, MinSnapSpacing),
                                self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]
                            tmp.append(tmpx)
                elif (_CLKinputPMOSFinger1 % 2) == 1:
                    for j in PMOS12tmp2:
                        for i in range(0, int(_CLKinputPMOSFinger // 2 + 1)):
                            tmpx = [
                                self.CeilMinSnapSpacing(j - (_CLKinputPMOSFinger // 2 - 0.5) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1, MinSnapSpacing),
                                self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]
                            tmp.append(tmpx)


            self._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'] = tmp[0:int((_CLKinputPMOSFinger1+1) // 2)]
            for i in range(len(self._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'])):
                tmpy.append([-1 * self._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'][i][0], self._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'][i][1]])
            self._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'] = tmp[0:int((_CLKinputPMOSFinger1+1) // 2)] + tmpy
            del tmp
            del tmpx
            del tmpy
            del _ViaNumY
            print('x')


            # VIA Generation for Inner PMOS34 Output
            _VIAPMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _VIAPMOSMet12['_ViaMet12Met2NumberOfCOX'] = 1
            _ViaNumY =  int((_PMOSChannelWidth - 2 * _DRCObj._Metal1MinEnclosureVia12) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
            if _ViaNumY < 1 :
                _ViaNumY = 1
            _VIAPMOSMet12['_ViaMet12Met2NumberOfCOY'] = _ViaNumY
            self._DesignParameter['_ViaMet12Met2OnPMOSOutput2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='{}:ViaMet12Met2OnPMOSOutput2'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_VIAPMOSMet12)
            del _ViaNumY


            _VIAPMOSMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _VIAPMOSMet23['_ViaMet22Met3NumberOfCOX'] = 1
            _ViaNumY =  int((_PMOSChannelWidth - 2 * _DRCObj._Metal1MinEnclosureVia12) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
            if _ViaNumY < 1 :
                _ViaNumY = 1
            _VIAPMOSMet23['_ViaMet22Met3NumberOfCOY'] = _ViaNumY
            self._DesignParameter['_ViaMet22Met3OnPMOSOutput2'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='{}:ViaMet22Met3OnPMOSOutput2'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3OnPMOSOutput2']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_VIAPMOSMet23)


            # tmp1 = []
            # tmp2 = []
            # for i in range(0, len(self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
            #     tmp1.append([self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1]])
            #     tmp2.append([-(self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0]), self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][1]])

            # _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            if DesignParameters._Technology == '028nm':
                _LengthPMOSBtwMet1 = _DRCObj.DRCPolyMinSpace(_Width=_PMOSChannelWidth, _ParallelLength=_ChannelLength) + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            else:
                _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            tmp = []
            tmpx = []
            PMOS34tmp = [self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0]+_LengthPMOSBtwMet1]
            PMOS34tmp2 = [self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0]]

            if (_PMOSFinger % 2) == 1:
                for j in PMOS34tmp:
                    for i in range(0, int((_PMOSFinger-1)// 2 + 1)):
                        tmpx=[self.CeilMinSnapSpacing(j - ((_PMOSFinger+1)//2 + 0.5)*_LengthPMOSBtwMet1 + _LengthPMOSBtwMet1 * (2*i+1), MinSnapSpacing), self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1]]
                        tmp.append(tmpx)
            elif (_PMOSFinger % 2) == 0:
                for j in PMOS34tmp2:
                    for i in range(0, int(_PMOSFinger//2+1)):
                        tmpx=[self.CeilMinSnapSpacing(j - (_PMOSFinger//2)*_LengthPMOSBtwMet1 + _LengthPMOSBtwMet1 * (2*i), MinSnapSpacing), self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1]]
                        tmp.append(tmpx)
            self._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'] = tmp
   #         self._DesignParameter['_ViaMet22Met3OnPMOSOutput2']['_XYCoordinates'] = tmp
            del tmp
            del tmpx
          #  del tmp1
          #  del tmp2
            del _ViaNumY
            print('x')


            # if DesignParameters._Technology in ('028nm','045nm','065nm') :
            #     _Met1SpacebtwVIAMOS = _DRCObj._Metal1MinSpace21
            # else :
            #     _Met1SpacebtwVIAMOS = _DRCObj._Metal1MinSpace

            _Met1SpacebtwVIAMOS = _DRCObj._Metal1MinSpace2

            # PMOS Gate Coordinate Setting
            self._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'] = [[self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0],
                                                                           self.CeilMinSnapSpacing(self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] - max(self._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,  self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2) - \
                                                                           self._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 - _Met1SpacebtwVIAMOS, MinSnapSpacing)

                                                                                  ]]

            self._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'] = [[self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0],
                                                                           self.CeilMinSnapSpacing(self._DesignParameter['_PMOS2']['_XYCoordinates'][0][1] - max(self._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,  self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2) - \
                                                                           self._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 - _Met1SpacebtwVIAMOS, MinSnapSpacing)
                                                                                  ]]


            self._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_XYCoordinates'] = [[self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0],
                                                                            self.CeilMinSnapSpacing(self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1] - max(self._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,  self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2) - \
                                                                           self._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 - _Met1SpacebtwVIAMOS, MinSnapSpacing)
                                                                                  ]]

            self._DesignParameter['_VIAPMOSPoly2Met1PMOS4']['_XYCoordinates'] = [[self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0],
                                                                            self.CeilMinSnapSpacing(self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1] - max(self._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,  self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2) - \
                                                                           self._DesignParameter['_VIAPMOSPoly2Met1PMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 - _Met1SpacebtwVIAMOS, MinSnapSpacing)
                                                                                  ]]

            self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

            if _Dummy == True :

                if _PMOSFinger == 1 :
                    _LengthBtwPoly2Poly2 = _ChannelLength + 2 * _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinWidth
                    _LengthNPolyDummyEdge2OriginX2 = int(round((int(_PMOSFinger // 2) + 1) * _LengthBtwPoly2Poly2 - _ChannelLength // 2 - (self._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) + 0.5)) // 2
                    _LengthNPolyGateEdge2OriginY2 = (self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] // 2) - (self._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] // 2)
                    _LengthBtwPolyEdge1 = math.sqrt(_LengthNPolyDummyEdge2OriginX2 * _LengthNPolyDummyEdge2OriginX2 + _LengthNPolyGateEdge2OriginY2 * _LengthNPolyGateEdge2OriginY2)


                    _LengthNPolyVIAtoGoUp2 = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthNPolyDummyEdge2OriginX2 * _LengthNPolyDummyEdge2OriginX2) + 1


                    if _LengthBtwPolyEdge1 + 1 < _DRCObj._PolygateMinSpaceAtCorner:
                        self._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_XYCoordinates'] = [
                          #  [self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] // 2 + self._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] // 2 + _LengthNPolyVIAtoGoUp2],
                            [self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] // 2 - self._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] // 2 - _LengthNPolyVIAtoGoUp2, MinSnapSpacing)], \
                            ]
                        self._DesignParameter['_VIAPMOSPoly2Met1PMOS4']['_XYCoordinates'] = [
                            [self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] // 2 - self._DesignParameter['_VIAPMOSPoly2Met1PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] // 2 - _LengthNPolyVIAtoGoUp2, MinSnapSpacing)]
                           ]



            #######################################################################################################################################################################################
            ############################################### Additional POLY Layer Generation to avoid DRC Error ####################################################################################
            ########################################################################################################################################################################################
            self._DesignParameter['_AdditionalPolyOnPMOS1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_Width=400)
            self._DesignParameter['_AdditionalPolyOnPMOS2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_Width=400)
            self._DesignParameter['_AdditionalPolyOnPMOS3'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_Width=400)
            self._DesignParameter['_AdditionalPolyOnPMOS4'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_Width=400)

            # PMOS1 Poly Layer Generation
            tmp1 = [[[self.CeilMinSnapSpacing(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] // 2 + self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], MinSnapSpacing),
                      self._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1]],
                     [self.CeilMinSnapSpacing(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0] - self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] // 2 + self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], MinSnapSpacing),
                      self._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1]]]]

            self._DesignParameter['_AdditionalPolyOnPMOS1']['_XYCoordinates'] = tmp1
            self._DesignParameter['_AdditionalPolyOnPMOS1']['_Width'] = self._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']


            self._DesignParameter['_AdditionalPolyGateOnPMOS1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_Width=400)

            tmp = []
            for i in range(0, len(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]], [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1]]])
            self._DesignParameter['_AdditionalPolyGateOnPMOS1']['_XYCoordinates'] = tmp
            # self._DesignParameter['_AdditionalPolyGateOnPMOS1']['_Width'] = _DRCObj._PolygateMinWidth
            self._DesignParameter['_AdditionalPolyGateOnPMOS1']['_Width'] = _ChannelLength
            del tmp

            # PMOS2 Poly Layer Generation
            tmp2 = [[[self.CeilMinSnapSpacing(self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] // 2 + self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0], MinSnapSpacing),
                      self._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1]],
                     [self.CeilMinSnapSpacing(self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0] - self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] // 2 + self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0], MinSnapSpacing),
                      self._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1]]]]
            self._DesignParameter['_AdditionalPolyOnPMOS2']['_XYCoordinates'] = tmp2
            self._DesignParameter['_AdditionalPolyOnPMOS2']['_Width'] = self._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']

            self._DesignParameter['_AdditionalPolyGateOnPMOS2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_Width=400)

            tmp = []
            for i in range(0, len(self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][1]], [self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1]]])
            self._DesignParameter['_AdditionalPolyGateOnPMOS2']['_XYCoordinates'] = tmp
            # self._DesignParameter['_AdditionalPolyGateOnPMOS2']['_Width'] = _DRCObj._PolygateMinWidth
            self._DesignParameter['_AdditionalPolyGateOnPMOS2']['_Width'] = _ChannelLength
            del tmp



            # PMOS3 Poly Layer Generation
            tmp3 = [[[self.CeilMinSnapSpacing(self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] // 2 + self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0], MinSnapSpacing),
                      self._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_XYCoordinates'][0][1]],
                     [self.CeilMinSnapSpacing(self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0] - self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] // 2 + self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0], MinSnapSpacing),
                      self._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_XYCoordinates'][0][1]]]]
            self._DesignParameter['_AdditionalPolyOnPMOS3']['_XYCoordinates'] = tmp3
            self._DesignParameter['_AdditionalPolyOnPMOS3']['_Width'] = self._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']

            self._DesignParameter['_AdditionalPolyGateOnPMOS3'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_Width=400)

            tmp = []
            for i in range(0, len(self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1]], [self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_XYCoordinates'][0][1]]])
            self._DesignParameter['_AdditionalPolyGateOnPMOS3']['_XYCoordinates'] = tmp
            # self._DesignParameter['_AdditionalPolyGateOnPMOS3']['_Width'] = _DRCObj._PolygateMinWidth
            self._DesignParameter['_AdditionalPolyGateOnPMOS3']['_Width'] = _ChannelLength
            del tmp



            # PMOS4 Poly Layer Generation
            tmp4 = [[[self.CeilMinSnapSpacing(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] // 2 + self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0], MinSnapSpacing),
                      self._DesignParameter['_VIAPMOSPoly2Met1PMOS4']['_XYCoordinates'][0][1]],
                     [self.CeilMinSnapSpacing(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0] - self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] // 2 + self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0], MinSnapSpacing),
                      self._DesignParameter['_VIAPMOSPoly2Met1PMOS4']['_XYCoordinates'][0][1]]]]
            self._DesignParameter['_AdditionalPolyOnPMOS4']['_XYCoordinates'] = tmp4
            self._DesignParameter['_AdditionalPolyOnPMOS4']['_Width'] = self._DesignParameter['_VIAPMOSPoly2Met1PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']

            self._DesignParameter['_AdditionalPolyGateOnPMOS4'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=400)

            tmp = []
            for i in range(0, len(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1]], [self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_VIAPMOSPoly2Met1PMOS4']['_XYCoordinates'][0][1]]])
            self._DesignParameter['_AdditionalPolyGateOnPMOS4']['_XYCoordinates'] = tmp
            # self._DesignParameter['_AdditionalPolyGateOnPMOS4']['_Width'] = _DRCObj._PolygateMinWidth
            self._DesignParameter['_AdditionalPolyGateOnPMOS4']['_Width'] = _ChannelLength
            del tmp

            #########################################################################################################################################
            ############################################### Guardring Generation ####################################################################
            #########################################################################################################################################
            _XVTPMOSLayer = self._DesignParameter['_PMOS1']['_DesignObj']._XVTLayer
            _XVTPMOSLayerMappingName = self._DesignParameter['_PMOS1']['_DesignObj']._XVTLayerMappingName


            if _Guardring == True:
                print ('#################################     Guardring Layer Generation ###########################################')


                toptmp = self.CeilMinSnapSpacing(self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] + max(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) //2 +  _GuardringWidth//2 + _DRCObj._Metal1DefaultSpace, MinSnapSpacing)
                bottomtmp =self.CeilMinSnapSpacing( min(self._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_XYCoordinates'][0][1], self._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1]) - self._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 - _DRCObj._Metal1DefaultSpace - _GuardringWidth // 2, MinSnapSpacing)
                lefttmp = self.CeilMinSnapSpacing(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] // 2 - _GuardringWidth//2 + self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0]  - _DRCObj._Metal1DefaultSpace, MinSnapSpacing)
                righttmp = self.CeilMinSnapSpacing(self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] - self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] // 2 + _GuardringWidth//2 + self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0] + _DRCObj._Metal1DefaultSpace, MinSnapSpacing)


                _GuardringCetPointX = self.CeilMinSnapSpacing(int(round(lefttmp + righttmp + 0.5)) // 2, MinSnapSpacing)
                _GuardringCetPointY = self.CeilMinSnapSpacing(int(round(toptmp + bottomtmp + 0.5)) // 2, MinSnapSpacing)
                _GuardringXWidth = self.CeilMinSnapSpacing(int(righttmp - lefttmp - _GuardringWidth), MinSnapSpacing)
                _GuardringYWidth = self.CeilMinSnapSpacing(int(toptmp - bottomtmp - _GuardringWidth), MinSnapSpacing)
                # if _GuardringXWidth % 2 == 1 :
                #     _GuardringXWidth = _GuardringXWidth + 1
                # if _GuardringYWidth % 2 == 1 :
                #     _GuardringYWidth = _GuardringYWidth + 1
                # if _GuardringCetPointX % 2 == 1 :
                #     _GuardringCetPointX = _GuardringCetPointX + 1
                # if _GuardringCetPointY % 2 == 1 :
                #     _GuardringCetPointY = _GuardringCetPointY + 1



                _NMOSSubringinputs = copy.deepcopy(psubring._PSubring._ParametersForDesignCalculation)
                _NMOSSubringinputs['_PType'] = False
                _NMOSSubringinputs['_XWidth'] = _GuardringXWidth
                _NMOSSubringinputs['_YWidth'] = _GuardringYWidth
                _NMOSSubringinputs['_Width'] = _GuardringWidth

                self._DesignParameter['_Guardring'] = self._SrefElementDeclaration(_DesignObj=psubring._PSubring(_DesignParameter=None, _Name='{}:Guardring'.format(_Name)))[0]
                self._DesignParameter['_Guardring']['_DesignObj']._CalculatePSubring(**_NMOSSubringinputs)

                self._DesignParameter['_Guardring']['_XYCoordinates'] = [[_GuardringCetPointX, _GuardringCetPointY]]




                # tmp5 = [[[lefttmp-self._DesignParameter['_RingMetal1Layer1']['_Width']//2, toptmp],[righttmp+self._DesignParameter['_RingMetal1Layer1']['_Width']//2, toptmp]]] # top
                # tmp6 = [[[lefttmp-self._DesignParameter['_RingMetal1Layer1']['_Width']//2, bottomtmp],[righttmp+self._DesignParameter['_RingMetal1Layer1']['_Width']//2, bottomtmp]]] # bottom
                # tmp7 = [[[lefttmp, toptmp+self._DesignParameter['_RingMetal1Layer1']['_Width']//2], [lefttmp, bottomtmp-self._DesignParameter['_RingMetal1Layer1']['_Width']//2]]] # left
                # tmp8 = [[[righttmp, toptmp+self._DesignParameter['_RingMetal1Layer1']['_Width']//2], [righttmp, bottomtmp-self._DesignParameter['_RingMetal1Layer1']['_Width']//2]]] #right
                #
                # self._DesignParameter['_RingMetal1Layer1']['_XYCoordinates'] = tmp5
                # self._DesignParameter['_RingMetal1Layer2']['_XYCoordinates'] = tmp6
                # self._DesignParameter['_RingMetal1Layer3']['_XYCoordinates'] = tmp7
                # self._DesignParameter['_RingMetal1Layer4']['_XYCoordinates'] = tmp8
                #
                # self._DesignParameter['_RingODLayer1']['_XYCoordinates'] = tmp5
                # self._DesignParameter['_RingODLayer2']['_XYCoordinates'] = tmp6
                # self._DesignParameter['_RingODLayer3']['_XYCoordinates'] = tmp7
                # self._DesignParameter['_RingODLayer4']['_XYCoordinates'] = tmp8
                #

            # CONT Generation for Guardring
            #     self._DesignParameter['_CONT1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            #     self._DesignParameter['_CONT2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            #
            #     self._DesignParameter['_CONT1']['_XWidth'] = _DRCObj._CoMinWidth
            #     self._DesignParameter['_CONT1']['_YWidth'] = _DRCObj._CoMinWidth
            #     self._DesignParameter['_CONT2']['_XWidth'] = _DRCObj._CoMinWidth
            #     self._DesignParameter['_CONT2']['_YWidth'] = _DRCObj._CoMinWidth
            #
            #     _XNumberOfCO1 = int((righttmp - lefttmp - self._DesignParameter['_RingMetal1Layer1']['_Width'] - 2 * _DRCObj._Metal1MinEnclosureCO2) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) # Horizontal Ring
            #     _YNumberOfCO1 = int((self._DesignParameter['_RingMetal1Layer1']['_Width'] - 2 * _DRCObj._Metal1MinEnclosureCO)// (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))
            #     _XNumberOfCO2 = int((self._DesignParameter['_RingMetal1Layer1']['_Width'] - 2 * _DRCObj._Metal1MinEnclosureCO)// (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))
            #     _YNumberOfCO2 = int((toptmp - bottomtmp - self._DesignParameter['_RingMetal1Layer1']['_Width'] - 2 * _DRCObj._Metal1MinEnclosureCO2) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))   # Verical Ring
            #
            # # CONT Coordinate Setting
            # _LengthRingBtwCO = _DRCObj._CoMinSpace + _DRCObj._CoMinWidth
            # tmp = []
            # tmp2=[toptmp, bottomtmp]
            #
            # for i in range(0, _XNumberOfCO1):
            #     for j in range(0, _YNumberOfCO1):
            #         for k in tmp2:
            #             if (_XNumberOfCO1 % 2) == 1 and (_YNumberOfCO1 % 2) == 0:
            #                 _xycoordinatetmp = [(righttmp+lefttmp)//2 - (_XNumberOfCO1 - 1) // 2 * _LengthRingBtwCO + i * _LengthRingBtwCO,
            #                                     k - (_YNumberOfCO1 // 2 - 0.5) * _LengthRingBtwCO + j * _LengthRingBtwCO]
            #             elif (_XNumberOfCO1 % 2) == 1 and (_YNumberOfCO1 % 2) == 1:
            #                 _xycoordinatetmp = [(righttmp+lefttmp)//2 - (_XNumberOfCO1 - 1) // 2 * _LengthRingBtwCO + i * _LengthRingBtwCO,
            #                                     k - (_YNumberOfCO1 - 1) // 2 * _LengthRingBtwCO + j * _LengthRingBtwCO]
            #             elif (_XNumberOfCO1 % 2) == 0 and (_YNumberOfCO1 % 2) == 0:
            #                 _xycoordinatetmp = [(righttmp+lefttmp)//2 - (_XNumberOfCO1 // 2 - 0.5) * _LengthRingBtwCO + i * _LengthRingBtwCO,
            #                                     k - (_YNumberOfCO1 // 2 - 0.5) * _LengthRingBtwCO + j * _LengthRingBtwCO]
            #             elif (_XNumberOfCO1 % 2) == 0 and (_YNumberOfCO1 % 2) == 1:
            #                 _xycoordinatetmp = [(righttmp+lefttmp)//2 - (_XNumberOfCO1 // 2 - 0.5) * _LengthRingBtwCO + i * _LengthRingBtwCO,
            #                                     k - (_YNumberOfCO1 - 1) // 2 * _LengthRingBtwCO + j * _LengthRingBtwCO]
            #             tmp.append(_xycoordinatetmp)
            # self._DesignParameter['_CONT1']['_XYCoordinates'] = tmp
            #
            # tmp = []
            # tmp2 = [-1, 1]
            # for i in range(0, _XNumberOfCO2):
            #     for j in range(0, _YNumberOfCO2):
            #         for k in tmp2:
            #             if (_XNumberOfCO2 % 2) == 1 and (_YNumberOfCO2 % 2) == 0:
            #                 _xycoordinatetmp = [tmp7[0][0][0]*k - (_XNumberOfCO2 - 1) // 2 * _LengthRingBtwCO + i * _LengthRingBtwCO,
            #                                     (toptmp+bottomtmp)//2 - (_YNumberOfCO2 // 2 - 0.5) * _LengthRingBtwCO + j * _LengthRingBtwCO]
            #             elif (_XNumberOfCO2 % 2) == 1 and (_YNumberOfCO2 % 2) == 1:
            #                 _xycoordinatetmp = [tmp7[0][0][0]*k - (_XNumberOfCO2 - 1) // 2 * _LengthRingBtwCO + i * _LengthRingBtwCO,
            #                                     (toptmp+bottomtmp)//2 - (_YNumberOfCO2 - 1) // 2 * _LengthRingBtwCO + j * _LengthRingBtwCO]
            #             elif (_XNumberOfCO2 % 2) == 0 and (_YNumberOfCO2 % 2) == 0:
            #                 _xycoordinatetmp = [tmp7[0][0][0]*k - (_XNumberOfCO2 // 2 - 0.5) * _LengthRingBtwCO + i * _LengthRingBtwCO,
            #                                     (toptmp+bottomtmp)//2 - (_YNumberOfCO2 // 2 - 0.5) * _LengthRingBtwCO + j * _LengthRingBtwCO]
            #             elif (_XNumberOfCO2 % 2) == 0 and (_YNumberOfCO2 % 2) == 1:
            #                 _xycoordinatetmp = [tmp7[0][0][0]*k - (_XNumberOfCO2 // 2 - 0.5) * _LengthRingBtwCO + i * _LengthRingBtwCO,
            #                                     (toptmp+bottomtmp)//2 - (_YNumberOfCO2 - 1) // 2 * _LengthRingBtwCO + j * _LengthRingBtwCO]
            #             tmp.append(_xycoordinatetmp)
            # self._DesignParameter['_CONT2']['_XYCoordinates'] = tmp

            #########################################################################################################################################
            ############################################### NW layer Generation #####################################################################
            #########################################################################################################################################
            self._DesignParameter['_NWLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0],_Datatype=DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400)
            self._DesignParameter['_NWLayer']['_XWidth'] = self.CeilMinSnapSpacing(righttmp - lefttmp + _GuardringWidth + 2*_DRCObj._NwMinEnclosurePactive, 2 * MinSnapSpacing)
            self._DesignParameter['_NWLayer']['_YWidth'] = self.CeilMinSnapSpacing(toptmp - bottomtmp + _GuardringWidth + 2*_DRCObj._NwMinEnclosurePactive, 2 * MinSnapSpacing)
            self._DesignParameter['_NWLayer']['_XYCoordinates'] = [[self.CeilMinSnapSpacing((righttmp+lefttmp)//2, MinSnapSpacing), self.CeilMinSnapSpacing((toptmp+bottomtmp)//2, MinSnapSpacing)]]

            # tmp1 = self.get_param_KJH4('_NWLayer')
            # tmp2 = self.get_param_KJH4('_Guardring')
            ###########################################################################################################################################
            ############################################### SLVT layer Generation #####################################################################
            ###########################################################################################################################################

            if _XVT != None :
                self._DesignParameter['_XVTPMOSLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping[_XVTPMOSLayerMappingName][0], _Datatype=DesignParameters._LayerMapping[_XVTPMOSLayerMappingName][1], _XYCoordinates=[], _XWidth=None, _YWidth=None)
                self._DesignParameter['_XVTPMOSLayer']['_XWidth'] = self.CeilMinSnapSpacing(self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0] - self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], 2 * MinSnapSpacing)
                self._DesignParameter['_XVTPMOSLayer']['_YWidth'] = self.CeilMinSnapSpacing(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter[_XVTPMOSLayer]['_YWidth'], 2 * MinSnapSpacing)
                self._DesignParameter['_XVTPMOSLayer']['_XYCoordinates'] = [[self.CeilMinSnapSpacing((righttmp+lefttmp)//2, MinSnapSpacing), self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]]

            ###########################################################################################################################################
            ############################################### BP layer Generation #####################################################################
            ###########################################################################################################################################
            self._DesignParameter['_BPLayer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[],_Width=400)
            self._DesignParameter['_BPLayer']['_Width'] = self.CeilMinSnapSpacing(self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0] - self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'], 2*MinSnapSpacing)
            self._DesignParameter['_BPLayer']['_XYCoordinates'] = [[[self.CeilMinSnapSpacing((righttmp+lefttmp)//2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2, MinSnapSpacing)], \
                                                                   [self.CeilMinSnapSpacing((righttmp+lefttmp)//2, MinSnapSpacing), self.CeilMinSnapSpacing(min(self._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1], self._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1], self._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_XYCoordinates'][0][1], self._DesignParameter['_VIAPMOSPoly2Met1PMOS4']['_XYCoordinates'][0][1]) - self._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] // 2 - _DRCObj._PpMinEnclosureOfPo, MinSnapSpacing)]]]

            #########################################################################################################################################
            ################################################ Routing Generation #####################################################################
            #########################################################################################################################################
            # PMOS Metal1 VDD --- Source Routing
            self._DesignParameter['_VDDMet1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_VDDMet1']['_Width'] = self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']##_DRCObj._CoMinWidth + 2*_DRCObj._Metal1MinEnclosureCO

            # _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            if DesignParameters._Technology == '028nm':
                _LengthPMOSBtwMet1 = _DRCObj.DRCPolyMinSpace(_Width=_PMOSChannelWidth, _ParallelLength=_ChannelLength) + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            else:
                _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            tmpx  = []
            VDDtmp = toptmp
            MOStmp = self.CeilMinSnapSpacing(self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']//2, MinSnapSpacing)
            # PMOS12tmp = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0]-_LengthPMOSBtwMet1, self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0]-_LengthPMOSBtwMet1]
            # PMOS12tmp2 = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0]-_LengthPMOSBtwMet1]
            PMOS34tmp = [self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0]]
            PMOS34tmp2 = [self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0]-_LengthPMOSBtwMet1]

            PMOS12tmp = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0] + _LengthPMOSBtwMet1]
            PMOS12tmp2 = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0] - _LengthPMOSBtwMet1]
            PMOS12tmp3 = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0]]

            print('x')



            ##################### PMOS12 VDD Met2 Routing Coordinate ############################
            if (_CLKinputPMOSFinger % 2) == 0: # Even = Finger1+Finger2
                if (_CLKinputPMOSFinger1 % 2) == 1: # Even = Finger1+Finger2 and Odd = Finger1
                    for i in range (0, int(_CLKinputPMOSFinger//2)): # The number of the VDD routing
                        for k in PMOS12tmp3:
                            tmpx.append([[self.CeilMinSnapSpacing(k-(_CLKinputPMOSFinger//2 - 1)*_LengthPMOSBtwMet1 + (2*i)*_LengthPMOSBtwMet1, MinSnapSpacing), VDDtmp],
                                         [self.CeilMinSnapSpacing(k-(_CLKinputPMOSFinger//2 - 1)*_LengthPMOSBtwMet1 + (2*i)*_LengthPMOSBtwMet1, MinSnapSpacing), MOStmp]])
                elif (_CLKinputPMOSFinger1 % 2) == 0: # Even = Finger1+Finger2 and Even = Finger1
                    for i in range (0, int(_CLKinputPMOSFinger//2 + 1)):
                        for k in PMOS12tmp3:
                            tmpx.append([[self.CeilMinSnapSpacing(k - (_CLKinputPMOSFinger // 2) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1, MinSnapSpacing), VDDtmp],
                                         [self.CeilMinSnapSpacing(k - (_CLKinputPMOSFinger // 2) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1, MinSnapSpacing), MOStmp]])

            elif (_CLKinputPMOSFinger % 2) == 1: # Odd = Finger1+Finger2
                if (_CLKinputPMOSFinger1 % 2) == 0: # Odd = Finger1 + Finger2 and Even = Finger1
                    for i in range (0, int((_CLKinputPMOSFinger//2 + 1))): # + 0.5
                        for k in PMOS12tmp:
                            tmpx.append([[self.CeilMinSnapSpacing(k - ((_CLKinputPMOSFinger // 2 + 0.5)) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1, MinSnapSpacing), VDDtmp],
                                         [self.CeilMinSnapSpacing(k - ((_CLKinputPMOSFinger // 2 + 0.5)) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1, MinSnapSpacing), MOStmp]])
                elif (_CLKinputPMOSFinger1 % 2) == 1: # Odd = Finger1+Finger2 and Odd = Finger1
                    for i in range (0, int((_CLKinputPMOSFinger//2 + 1))): # + 0.5
                        for k in PMOS12tmp2:
                            tmpx.append([[self.CeilMinSnapSpacing(k - ((_CLKinputPMOSFinger//2 - 0.5)) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1, MinSnapSpacing), VDDtmp],
                                         [self.CeilMinSnapSpacing(k - ((_CLKinputPMOSFinger//2 - 0.5)) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1, MinSnapSpacing), MOStmp]])



            if (_PMOSFinger % 2 ) == 1:
                for i in range(0, int((_PMOSFinger - 1)//2 + 1 )):
                    for k in PMOS34tmp2:
                        tmpx.append([[self.CeilMinSnapSpacing(k - ((_PMOSFinger+1)//2-0.5)*_LengthPMOSBtwMet1 + _LengthPMOSBtwMet1*(i*2+1), MinSnapSpacing), VDDtmp],
                                     [self.CeilMinSnapSpacing(k - ((_PMOSFinger+1)//2-0.5)*_LengthPMOSBtwMet1 + _LengthPMOSBtwMet1*(i*2+1), MinSnapSpacing), MOStmp]
                                    ])
            elif (_PMOSFinger % 2) == 0:
                for i in range(0, int(_PMOSFinger // 2)):
                    for k in PMOS34tmp:
                        tmpx.append([[self.CeilMinSnapSpacing(k - (_PMOSFinger//2) * _LengthPMOSBtwMet1 + _LengthPMOSBtwMet1*(i*2+1), MinSnapSpacing), VDDtmp],
                                     [self.CeilMinSnapSpacing(k - (_PMOSFinger//2) * _LengthPMOSBtwMet1 + _LengthPMOSBtwMet1*(i*2+1), MinSnapSpacing), MOStmp]])


            self._DesignParameter['_VDDMet1']['_XYCoordinates'] = tmpx

            print('x')

            # axis variable
            self._DesignParameter['PMOS_toptmp']= {'_Ignore': toptmp, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}
            self._DesignParameter['PMOS_bottomtmp']= {'_Ignore': bottomtmp, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}
            self._DesignParameter['PMOS_righttmp']= {'_Ignore': righttmp, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}
            self._DesignParameter['PMOS_lefttmp']= {'_Ignore': lefttmp, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}




            #########################################################################################################################################
            ################################################ Routing Generation #####################################################################
            #########################################################################################################################################
            # # PMOS Met2 Routing
            # self._DesignParameter['_Met2PMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
            # self._DesignParameter['_Met2PMOS']['_Width'] = _DRCObj._MetalxMinWidth
            # # k = len(self._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'])
            # k = _CLKinputPMOSFinger//2
            #
            # self._DesignParameter['_Met2PMOS']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0], self._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][k-1]],
            #
            #                                                         [self._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1], self._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][k+2]],
            #
            #                                                         [self._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][k], self._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][0]],
            #
            #                                                         [self._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][k+1], self._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][-1]]
            #                                                        ]

            print('xxx')

            pass
if __name__ == '__main__':
    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_YCH
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'PMOSSlicer_SS_v2'
    cellname = 'PMOSSlicer'
    _fileName = cellname + '.gds'

    _CLKinputPMOSFinger1=6
    _CLKinputPMOSFinger2=6
    _PMOSFinger=6
    _PMOSChannelWidth=350
    _ChannelLength=30
    _Dummy=False
    _XVT='HVT'
    _GuardringWidth=150
    _Guardring=True
    _NumSupplyCOY=None
    _NumSupplyCOX=None
    _SupplyMet1XWidth=None
    _SupplyMet1YWidth=None
    _VDD2VSSHeight=None
    _NumVIAPoly2Met1COX=None
    _NumVIAPoly2Met1COY=None
    _NumVIAMet12COX=None
    _NumVIAMet12COY=None

    ''' Input Parameters for Layout Object '''  ############################################################### ^^^^^^^^^^^^^^^^^^^^^
    InputParams = dict(
        _CLKinputPMOSFinger1=_CLKinputPMOSFinger1,
        _CLKinputPMOSFinger2 = _CLKinputPMOSFinger2,
        _PMOSFinger = _PMOSFinger,
        _PMOSChannelWidth = _PMOSChannelWidth,
        _ChannelLength = _ChannelLength,
        _Dummy = _Dummy,
        _XVT = _XVT,
        _GuardringWidth = _GuardringWidth,
        _Guardring = _Guardring,
        _NumSupplyCOY = _NumSupplyCOY,
        _NumSupplyCOX = _NumSupplyCOX,
        _SupplyMet1XWidth = _SupplyMet1XWidth,
        _SupplyMet1YWidth = _SupplyMet1YWidth,
        _VDD2VSSHeight = _VDD2VSSHeight,
        _NumVIAPoly2Met1COX = _NumVIAPoly2Met1COX,
        _NumVIAPoly2Met1COY = _NumVIAPoly2Met1COY,
        _NumVIAMet12COX = _NumVIAMet12COX,
        _NumVIAMet12COY = _NumVIAMet12COY

    )
    '''Mode_DRCCHECK '''

    Mode_DRCCheck = False
    Num_DRCCheck = 1

    for ii in range(0, Num_DRCCheck if Mode_DRCCheck else 1):
        if Mode_DRCCheck:
            ''' Input Parameters for Layout Object '''
        else:
            pass

    ''' Generate Layout Object '''
    LayoutObj = _PMOSWithDummyOfSlicer(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('###############      Sending to FTP Server...      ##################')
    My = MyInfo_YCH.USER(DesignParameters._Technology)
    Checker = DRCchecker_KJH0.DRCchecker_KJH0(
        username=My.ID,
        password=My.PW,
        WorkDir=My.Dir_Work,
        DRCrunDir=My.Dir_DRCrun,
        libname=libname,
        cellname=cellname,
        GDSDir=My.Dir_GDS
    )
    Checker.lib_deletion()
    # Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()

    ''' Check Time'''
    elapsed_time = time.time() - start_time
    m, s = divmod(elapsed_time, 60)
    h, m = divmod(m, 60)

    print('#############################      Finished      ################################')





