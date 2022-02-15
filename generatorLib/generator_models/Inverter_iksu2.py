import math
import copy

#
from generatorLib import StickDiagram
from generatorLib import DesignParameters
from generatorLib import DRC

#
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import NbodyContact
from generatorLib.generator_models import PbodyContact
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaMet22Met3
from generatorLib.generator_models import SupplyRails

#
from generatorLib import CoordinateCalc as CoordCalc


class _Inverter(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_Finger=1, _ChannelWidth=200, _ChannelLength=30, _NPRatio=2,
                                           _VDD2VSSHeight=1800,
                                           _VDD2PMOSHeight=500,
                                           _VSS2NMOSHeight=300,
                                           _Dummy=True, _GateSpacing=120,  _XVT='SLVT',
                                           _NumViaPoly2Met1CoX=None,
                                           _NumViaPoly2Met1CoY=None,
                                           _NumViaPMOSMet12Met2CoY=None,
                                           _NumViaNMOSMet12Met2CoY=None
    )

    def __init__(self, _DesignParameter=None, _Name='Inverter'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

    def _CalculateDesignParameter_v3(self,
                                     _Finger=1,
                                     _ChannelWidth=200,
                                     _ChannelLength=30,
                                     _NPRatio=2,

                                     _VDD2VSSHeight=1800,
                                     _VDD2PMOSHeight=599,
                                     _VSS2NMOSHeight=461,

                                     _Dummy=True,
                                     _XVT='SLVT',
                                     _GateSpacing=120,
                                     _SDWidth=66,

                                     _NumViaPoly2Met1CoX=None,
                                     _NumViaPoly2Met1CoY=None,
                                     _NumViaPMOSMet12Met2CoY=None,
                                     _NumViaNMOSMet12Met2CoY=None,
                                     ):
        """

        :param _Finger:
        :param _ChannelWidth:
        :param _ChannelLength:
        :param _NPRatio:
        :param _Dummy:
        :param _XVT:
        :param _GateSpacing:
        :param _VDD2VSSHeight:
        :param _NumViaPoly2Met1CoX:
        :param _NumViaPoly2Met1CoY:
        :param _NumViaPMOSMet12Met2CoY: (optional, but recommended to None) | None(default) : calculated by 'YWidth of MOSFET's S/D Metal1', minimum : 2
        :param _NumViaNMOSMet12Met2CoY: (optional, but recommended to None) | None(default) : calculated by 'YWidth of MOSFET's S/D Metal1', minimum : 2
        :return:
        """

        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        MinSnapSpacing = _DRCObj._MinSnapSpacing

        print(''.center(105, '#'))
        print('     {} Calculation Start     '.format(_Name).center(105, '#'))
        print(''.center(105, '#'))

        ''' ------------------------------------------ MOSFET Generation ------------------------------------------- '''
        # 1) _NMOS Generation ------------------------------------------------------------------------------------------
        NMOSparameters = copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation)
        NMOSparameters['_NMOSNumberofGate'] = _Finger
        NMOSparameters['_NMOSChannelWidth'] = _ChannelWidth
        NMOSparameters['_NMOSChannellength'] = _ChannelLength
        NMOSparameters['_NMOSDummy'] = _Dummy
        NMOSparameters['_XVT'] = _XVT
        NMOSparameters['_GateSpacing'] = _GateSpacing
        NMOSparameters['_SDWidth'] = _SDWidth

        self._DesignParameter['_NMOS'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOS_In{}'.format(_Name)))[0]
        self._DesignParameter['_NMOS']['_DesignObj']._CalculateNMOSDesignParameter(**NMOSparameters)

        # 2) _PMOS Generation ------------------------------------------------------------------------------------------
        PMOSparameters = copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation)
        PMOSparameters['_PMOSNumberofGate'] = _Finger
        PMOSparameters['_PMOSChannelWidth'] = round(_ChannelWidth * _NPRatio)  # Need to Modify
        PMOSparameters['_PMOSChannellength'] = _ChannelLength
        PMOSparameters['_PMOSDummy'] = _Dummy
        PMOSparameters['_XVT'] = _XVT
        PMOSparameters['_GateSpacing'] = _GateSpacing
        PMOSparameters['_SDWidth'] = _SDWidth

        self._DesignParameter['_PMOS'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOS_In{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS']['_DesignObj']._CalculatePMOSDesignParameter(**PMOSparameters)


        ''' ---------------------------------------- Supply Rail Generation ---------------------------------------- '''
        self._DesignParameter['PbodyContact'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VSSRailIn{}'.format(_Name)))[0]
        self._DesignParameter['PbodyContact']['_DesignObj']._CalculateDesignParameter(
            **dict(NumPitch=_Finger + 1, UnitPitch=(_GateSpacing + _ChannelLength),
                   Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=True, deleteViaAndMet1=False))
        self._DesignParameter['PbodyContact']['_XYCoordinates'] = [[0.0, 0.0]]
        self._DesignParameter['NbodyContact'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VDDRailIn{}'.format(_Name)))[0]
        self._DesignParameter['NbodyContact']['_DesignObj']._CalculateDesignParameter(
            **dict(NumPitch=_Finger + 1, UnitPitch=(_ChannelLength + _GateSpacing),
                   Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=False, deleteViaAndMet1=False))
        self._DesignParameter['NbodyContact']['_XYCoordinates'] = [[0, _VDD2VSSHeight]]


        ''' -------------------------------------------- Via Generation -------------------------------------------- '''
        # 1) VIA Generation for PMOS Output ----------------------------------------------------------------------------
        if _NumViaPMOSMet12Met2CoY == None:  # Default : calculate
            YWidthOfPMOSMet1 = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            NumViaYPMOS = int((YWidthOfPMOSMet1 - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
        else:
            NumViaYPMOS = _NumViaPMOSMet12Met2CoY

        VIAPMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        VIAPMOSMet12['_ViaMet12Met2NumberOfCOX'] = 1
        VIAPMOSMet12['_ViaMet12Met2NumberOfCOY'] = NumViaYPMOS if (NumViaYPMOS > 2) else 2

        self._DesignParameter['_ViaMet12Met2OnPMOSOutput'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='ViaMet12Met2OnPMOSOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._CalculateDesignParameterSameEnclosure(**VIAPMOSMet12)

        # 1-1) Metal1 YWidth re-calculation
        self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
            = max(self.getYWidth('_ViaMet12Met2OnPMOSOutput', '_Met1Layer'), self.getYWidth('_PMOS', '_Met1Layer'))

        Area_M1for_ViaMet12Met2OnPMOSOutput = self.getXWidth('_ViaMet12Met2OnPMOSOutput', '_Met1Layer') \
                                              * self.getYWidth('_ViaMet12Met2OnPMOSOutput', '_Met1Layer')
        if Area_M1for_ViaMet12Met2OnPMOSOutput < _DRCObj._Metal1MinArea:
            YWidth_recalculated_byMinArea = self.CeilMinSnapSpacing(_DRCObj._Metal1MinArea / self.getXWidth('_ViaMet12Met2OnPMOSOutput', '_Met1Layer'), 2 * MinSnapSpacing)
            self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = YWidth_recalculated_byMinArea
        else:
            pass

        # 2) VIA Generation for NMOS Output ----------------------------------------------------------------------------
        if _NumViaNMOSMet12Met2CoY == None:  # Default : calculate
            YWidthOfNMOSMet1 = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            NumViaYNMOS = int((YWidthOfNMOSMet1 - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
        else:
            NumViaYNMOS = _NumViaNMOSMet12Met2CoY

        VIANMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        VIANMOSMet12['_ViaMet12Met2NumberOfCOX'] = 1
        VIANMOSMet12['_ViaMet12Met2NumberOfCOY'] = NumViaYNMOS if (NumViaYNMOS > 2) else 2

        self._DesignParameter['_ViaMet12Met2OnNMOSOutput'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='ViaMet12Met2OnNMOSOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._CalculateDesignParameterSameEnclosure(**VIANMOSMet12)

        # 2-1) Metal1 YWidth re-calculation
        self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
            = max(self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                  self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
        Area_M1for_ViaMet12Met2OnNMOSOutput = self.getXWidth('_ViaMet12Met2OnNMOSOutput', '_Met1Layer') \
                                              * self.getYWidth('_ViaMet12Met2OnNMOSOutput', '_Met1Layer')
        if Area_M1for_ViaMet12Met2OnNMOSOutput < _DRCObj._Metal1MinArea:
            YWidth_recalculated_byMinArea = self.CeilMinSnapSpacing(_DRCObj._Metal1MinArea / self.getXWidth('_ViaMet12Met2OnNMOSOutput', '_Met1Layer'), 2 * MinSnapSpacing)
            self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = YWidth_recalculated_byMinArea
        else:
            pass

        # 3) Input VIA Generation for Finger=1 / or calculate input poly-M1 contact YWidth     -> Need to check
        if _Finger == 1:
            _VIAMOSPoly2Met1_F1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
            _VIAMOSPoly2Met1_F1['_ViaPoly2Met1NumberOfCOX'] = 1  # Need to Modify (by calculation for wide channel length)
            _VIAMOSPoly2Met1_F1['_ViaPoly2Met1NumberOfCOY'] = 1  # Need to Modify (by user input parameter)
            self._DesignParameter['_VIANMOSPoly2Met1_F1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='ViaPoly2Met1_F1OnNMOSGateIn{}'.format(_Name)))[0]
            self._DesignParameter['_VIANMOSPoly2Met1_F1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIAMOSPoly2Met1_F1)
            self._DesignParameter['_VIAPMOSPoly2Met1_F1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='ViaPoly2Met1_F1OnPMOSGateIn{}'.format(_Name)))[0]
            self._DesignParameter['_VIAPMOSPoly2Met1_F1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIAMOSPoly2Met1_F1)

            self._DesignParameter['_VIANMOSPoly2Met1_F1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + 2 * _DRCObj._Metal1MinEnclosureVia3
            self._DesignParameter['_VIAPMOSPoly2Met1_F1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + 2 * _DRCObj._Metal1MinEnclosureVia3
        else:
            WidthOfInputXM1 = _DRCObj._CoMinWidth + 2 * _DRCObj._Metal1MinEnclosureCO2  # how?? you have to choose / Need to Modify (by user input parameter) / ambiguous name


        ''' -------------------------------------------------------------------------------------------------------- '''
        ''' ------------------------------------------ Coordinates setting ----------------------------------------- '''
        ''' -------------------------------------------------------------------------------------------------------- '''
        # 1) Calculate Distance Between 'Supply rail' and 'MOSFET'  : concern (SS28nm, TSMC65nm) and (Dummy T/F)
        if DesignParameters._Technology == 'SS28nm':
            DistanceBtwVSS2NMOS1 = (self.getYWidth('PbodyContact', '_PPLayer') + self.getYWidth('_NMOS','_POLayer')) / 2
            DistanceBtwVSS2NMOS2 = 0.5 * (self.getYWidth('PbodyContact', '_ODLayer') + self.getYWidth('_NMOS', '_ODLayer')) \
                                   + _DRCObj._OdMinSpace  # OD Layer(for Pbody) - OD Layer (for NMOS)     OD=RX
            if '_PODummyLayer' in self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter:
                DistanceBtwVSS2NMOS3 = 0.5 * self.getYWidth('PbodyContact', '_ODLayer') \
                                       + 0.5 * self.getYWidth('_NMOS', '_PODummyLayer') \
                                       + _DRCObj._PolygateMinSpace2OD  # OD Layer(for Pbody) - PO Dummy Layer (for NMOS)     OD=RX
            else:
                DistanceBtwVSS2NMOS3 = 0
            if '_Met1Layer' in self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter:
                DistanceBtwVSS2NMOS4 = 0.5 * self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
                                       + 0.5 * max(self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                                   self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) \
                                       + _DRCObj._Metal1MinSpace2  # Need to Modify
            else:
                DistanceBtwVSS2NMOS4 = 0
            DistanceBtwVSS2NMOS_minimum = max(DistanceBtwVSS2NMOS1, DistanceBtwVSS2NMOS2, DistanceBtwVSS2NMOS3,DistanceBtwVSS2NMOS4)

            DistanceBtwVDD2PMOS1 = 0.5 * self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] \
                                   + 0.5 * self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] \
                                   + _DRCObj._OdMinSpace
            DistanceBtwVD2PMOS2 = 0.5 * self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] \
                                  + 0.5 * self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] \
                                  + _DRCObj._OdMinSpace  # OD Layer(for Nbody) - OD Layer (for PMOS)     OD=RX
            if '_PODummyLayer' in self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter:
                DistanceBtwVDD2PMOS3 = 0.5 * self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] \
                                       + 0.5 * self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] \
                                       + _DRCObj._PolygateMinSpace2OD  # OD Layer(for Nbody) - PO Dummy Layer (for PMOS)     OD=RX
            else:
                DistanceBtwVDD2PMOS3 = 0
            if '_Met1Layer' in self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter:
                DistanceBtwVDD2PMOS4 = 0.5 * self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
                                       + 0.5 * max(self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                                   self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) \
                                       + _DRCObj._Metal1MinSpace2  # Need to Modify
            else:
                DistanceBtwVDD2PMOS4 = 0
            DistanceBtwVDD2PMOS_minimum = max(DistanceBtwVDD2PMOS1, DistanceBtwVD2PMOS2, DistanceBtwVDD2PMOS3, DistanceBtwVDD2PMOS4)

        elif DesignParameters._Technology == 'TSMC65nm':
            DistanceBtwVSS2NMOS_minimum = 0.5 * self.getYWidth('PbodyContact', '_PPLayer') + 0.5 * self.getYWidth('_NMOS', '_NPLayer')
            DistanceBtwVDD2PMOS_minimum = 0.5 * self.getYWidth('_PMOS', '_PPLayer') + 0.5 * self.getYWidth('NbodyContact', '_NPLayer')
        else:
            raise NotImplementedError

        if _VSS2NMOSHeight == None:
            DistanceBtwVSS2NMOS = DistanceBtwVSS2NMOS_minimum
        elif _VSS2NMOSHeight < DistanceBtwVSS2NMOS_minimum:
            raise Exception("Too short '_VSS2NMOSHeight'.")
        else:
            DistanceBtwVSS2NMOS = _VSS2NMOSHeight

        if _VDD2PMOSHeight == None:
            DistanceBtwVDD2PMOS = DistanceBtwVDD2PMOS_minimum
        elif _VDD2PMOSHeight < DistanceBtwVDD2PMOS_minimum:
            raise Exception("Too short '_VDD2PMOSHeight'.")
        else:
            DistanceBtwVDD2PMOS = _VDD2PMOSHeight

        # 2) Calculate Distance between 'MOSFET' and 'Input gate Contact'
        if _Finger != 1:
            if DesignParameters._Technology == 'SS28nm':
                tmp_space = _DRCObj._Metal1MinSpaceAtCorner
            else:  # only checked when 65nm
                tmp_space = _DRCObj._Metal1MinSpace

            DistanceBtwNMOS2PolyInput = 0.5 * max(
                self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) \
                                        + 0.5 * WidthOfInputXM1 \
                                        + tmp_space

            DistanceBtwPMOS2PolyInput = 0.5 * max(
                self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) \
                                        + 0.5 * WidthOfInputXM1 \
                                        + tmp_space

        else:  # Finger == 1
            XCoordinateOfViaF1 = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][0][0]

            _LengthBtwPolyDummyEdge2PolyEdge = - self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] \
                                               - 0.5*self.getXWidth('_NMOS', '_PODummyLayer') \
                                               + XCoordinateOfViaF1 \
                                               - 0.5*self.getXWidth('_VIANMOSPoly2Met1_F1', '_POLayer')

            _LengthNPolyDummytoGoUp_Finger2 = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthBtwPolyDummyEdge2PolyEdge * _LengthBtwPolyDummyEdge2PolyEdge) + 1
            _LengthPPolyDummytoGoUp_Finger2 = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthBtwPolyDummyEdge2PolyEdge * _LengthBtwPolyDummyEdge2PolyEdge) + 1

            DistanceBtwNMOS2PolyInput = \
                0.5 * self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] \
                + _LengthNPolyDummytoGoUp_Finger2 \
                + 0.5 * self._DesignParameter['_VIANMOSPoly2Met1_F1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
            DistanceBtwPMOS2PolyInput = \
                0.5 * self._DesignParameter['_VIAPMOSPoly2Met1_F1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] \
                + _LengthPPolyDummytoGoUp_Finger2 \
                + 0.5 * self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']


        # 3) Calculate Total Minimum Height of Inverter (Between Supply rails, VDD - VSS)
        if DesignParameters._Technology == 'SS28nm':
            _VDD2VSSMinHeight1 = DistanceBtwVSS2NMOS + DistanceBtwNMOS2PolyInput + DistanceBtwPMOS2PolyInput + DistanceBtwVDD2PMOS
            _VDD2VSSMinHeight2 = DistanceBtwVSS2NMOS + DistanceBtwVDD2PMOS \
                                 + 0.5 * self.getYWidth('_NMOS', '_PODummyLayer') \
                                 + 0.5 * self.getYWidth('_PMOS', '_PODummyLayer') \
                                 + _DRCObj._PolygateMinSpace
            # Add by poly dummy gate space 96
            _VDD2VSSMinHeight = max(_VDD2VSSMinHeight1, _VDD2VSSMinHeight2)

        else:  # Need to consider NP PP Layer overlapped
            # 1) Overlapped polygate of PMOS and NMOS -> PP and NP are overlapped
            _VDD2VSSMinHeight1 = DistanceBtwVSS2NMOS + DistanceBtwNMOS2PolyInput + DistanceBtwPMOS2PolyInput + DistanceBtwVDD2PMOS  # Maybe Not seletec
            # 2) calculate by PP and NP layer -> It works, but not a general design. -> Need Very Wide Poly routing and specific width M1
            _VDD2VSSMinHeight2 = DistanceBtwVSS2NMOS \
                                 + 0.5 * self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_NPLayer'][
                                     '_YWidth'] \
                                 + 0.5 * self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer'][
                                     '_YWidth'] \
                                 + DistanceBtwVDD2PMOS
            # 3)  two independant poly gates and gap by '_PolygateMinSpace2'
            _VDD2VSSMinHeight3 = DistanceBtwVSS2NMOS + DistanceBtwNMOS2PolyInput + DistanceBtwPMOS2PolyInput + DistanceBtwVDD2PMOS + WidthOfInputXM1 + _DRCObj._PolygateMinSpace2  # Need to Modify by using 'DRCPolyMinSpace' later

            _VDD2VSSMinHeight = max(_VDD2VSSMinHeight1, _VDD2VSSMinHeight2, _VDD2VSSMinHeight3)


        # 4) Determine the total height and Validate it
        if _VDD2VSSHeight == None:
            _VDD2VSSHeight = _VDD2VSSMinHeight
        else:
            if _VDD2VSSHeight < _VDD2VSSMinHeight:
                print("ERROR! VDD2VSSMinHeight =", _VDD2VSSMinHeight)  # Need to Print More information(input parameter...)
                raise NotImplementedError

        # 5) Setting Coordinates of 'SupplyLines and MOSFETs'
        self._DesignParameter['PbodyContact']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['NbodyContact']['_XYCoordinates'] = [[0, _VDD2VSSHeight]]
        self._DesignParameter['_NMOS']['_XYCoordinates'] = [[0, DistanceBtwVSS2NMOS]]
        self._DesignParameter['_PMOS']['_XYCoordinates'] = [[0, (_VDD2VSSHeight - DistanceBtwVDD2PMOS)]]

        # 6) Setting Coordinates of 'Output Routing Via (M1V1M2)'
        tmpNMOSOutputRouting, tmpPMOSOutputRouting = [], []
        for i in range(0, len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):  # Assumption : same MOSFETs' fingers
            tmpPMOSOutputRouting.append(CoordCalc.Add(
                self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i],
                self._DesignParameter['_PMOS']['_XYCoordinates'][0]))
            tmpNMOSOutputRouting.append(CoordCalc.Add(
                self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i],
                self._DesignParameter['_NMOS']['_XYCoordinates'][0]))

        self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'] = tmpPMOSOutputRouting
        self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'] = tmpNMOSOutputRouting


        ''' VSS & VDD Supply Routing (Metal1) ---------------------------------------------------------------------- '''
        '''
            Function : Route 'VDD-PMOS(source)' and 'VSS-NMOS(source)' by 'METAL1'
                       (Set the Leftmost Metal of MOSFET as the source)
            Require  : NMOS, PMOS, NbodyContact, PbodyContact (Coordinates)
        '''

        tmpPathForSupplyRoutingOnPMOS, tmpPathForSupplyRoutingOnNMOS = [], []
        for XYs in self.getXY('_NMOS', '_XYCoordinateNMOSSupplyRouting'):
            tmpPathForSupplyRoutingOnNMOS.append([
                [XYs[0], XYs[1] + self.getYWidth('_NMOS', '_Met1Layer') / 2],
                [XYs[0], self.getXY('PbodyContact')[0][1]]
            ])
        for XYs in self.getXY('_PMOS', '_XYCoordinatePMOSSupplyRouting'):
            tmpPathForSupplyRoutingOnPMOS.append([
                [XYs[0], XYs[1] - self.getYWidth('_PMOS', '_Met1Layer') / 2],
                [XYs[0], self.getXY('NbodyContact')[0][1]]
            ])

        self._DesignParameter['_NMOSSupplyRouting'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _Width=self.getXWidth('_NMOS', '_Met1Layer'),
            _XYCoordinates=tmpPathForSupplyRoutingOnNMOS
        )

        self._DesignParameter['_PMOSSupplyRouting'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _Width=self.getXWidth('_PMOS', '_Met1Layer'),
            _XYCoordinates=tmpPathForSupplyRoutingOnPMOS
        )



        #####################################VIA re-Coordinates for Poly Dummy######################################
        # Need to Modify
        if (_Finger == 1) and (DesignParameters._Technology == 'SS28nm'):
            self._DesignParameter['_VIANMOSPoly2Met1_F1']['_XYCoordinates'] = [
                [XCoordinateOfViaF1,  # self._DesignParameter['_NMOS']['_XYCoordinates'][0][0],
                 self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] +
                 self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 +
                 self._DesignParameter['_VIANMOSPoly2Met1_F1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyDummytoGoUp_Finger2]]
            self._DesignParameter['_VIAPMOSPoly2Met1_F1']['_XYCoordinates'] = [
                [XCoordinateOfViaF1,  # self._DesignParameter['_PMOS']['_XYCoordinates'][0][0],
                 self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] -
                 self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 -
                 self._DesignParameter['_VIAPMOSPoly2Met1_F1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 - _LengthPPolyDummytoGoUp_Finger2]]
        elif (_Finger == 1) and (DesignParameters._Technology == 'TSMC65nm'):
            raise NotImplementedError
        elif DesignParameters._Technology not in ('SS28nm', 'TSMC65nm'):
            raise NotImplementedError
        else:
            pass

        # Poly Boundary Generation MOS Gate -----------------------------------------------------------------------
        '''
        Require : PMOS, NMOS
        '''
        if _Finger != 1:
            _LenBtwPMOSGates = \
                self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] \
                - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0] \
                + _ChannelLength
            _LenBtwNMOSGates = \
                self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] \
                - self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0] \
                + _ChannelLength

        else:
            _LenBtwPMOSGates = abs(self.getXY('_VIAPMOSPoly2Met1_F1')[0][0] - self.getXY('_PMOS', '_XYCoordinatePMOSGateRouting')[0][0]) \
                               + self.getXWidth('_VIAPMOSPoly2Met1_F1', '_POLayer') / 2 \
                               + self.getXWidth('_PMOS', '_POLayer') / 2
            _LenBtwNMOSGates = abs(self.getXY('_VIANMOSPoly2Met1_F1')[0][0] - self.getXY('_NMOS', '_XYCoordinateNMOSGateRouting')[0][0]) \
                               + self.getXWidth('_VIANMOSPoly2Met1_F1', '_POLayer') / 2 \
                               + self.getXWidth('_NMOS', '_POLayer') / 2

        self._DesignParameter['_PolyRouteXOnPMOS'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1])
        self._DesignParameter['_PolyRouteXOnNMOS'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1])
        self._DesignParameter['_PolyRouteXOnPMOS']['_XWidth'] = _LenBtwPMOSGates
        self._DesignParameter['_PolyRouteXOnNMOS']['_XWidth'] = _LenBtwNMOSGates
        self._DesignParameter['_PolyRouteXOnPMOS']['_YWidth'] = _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByPOAtLeastTwoSide  # calculated when only one row -> should be changed
        self._DesignParameter['_PolyRouteXOnNMOS']['_YWidth'] = _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByPOAtLeastTwoSide

        # Additional Poly Routing --------------------------------------------------------------------------------------
        '''
        Function : Route poly layers [ {Input gate poly left - Input gate poly right(row)}, {NMOS gate poly - Input M1 poly(column)}, {PMOS gate poly - Input M1 poly(column)} ]
        Output   : Update self._DesignParameter['_PolyRouteXOn{PMOS, NMOS}'] & self._DesignParameter['_PolyRouteYOn{PMOS, NMOS}'] 
        Require  : NMOS, PMOS (XYCoordinates)
        '''
        # Row Line (Only setting Coordinates)
        if _Finger != 1:
            self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'] = [
                [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0],
                 self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + DistanceBtwNMOS2PolyInput]
            ]

            self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'] = [
                [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0],
                 self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - DistanceBtwPMOS2PolyInput]
            ]
        else:
            self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'] = [
                [self.getXY('_NMOS', '_POLayer')[0][0] + _ChannelLength / 2 - _LenBtwNMOSGates / 2,
                 self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + DistanceBtwNMOS2PolyInput]
            ]

            self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'] = [
                [self.getXY('_PMOS', '_POLayer')[0][0] + _ChannelLength / 2 - _LenBtwPMOSGates / 2,
                 self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - DistanceBtwPMOS2PolyInput]
            ]

        # Column Line
        self._DesignParameter['_PolyRouteYOnPMOS'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1])
        self._DesignParameter['_PolyRouteYOnNMOS'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1])
        self._DesignParameter['_PolyRouteYOnPMOS']['_Width'] = _ChannelLength
        self._DesignParameter['_PolyRouteYOnNMOS']['_Width'] = _ChannelLength

        tmpPolyRouteYOnPMOS, tmpPolyRouteYOnNMOS = [], []
        for i in range(0, len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])):
            tmpPolyRouteYOnPMOS.append([[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] +
                                         self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0],
                                         self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] +
                                         self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][1]],
                                        [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] +
                                         self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0],
                                         self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'][0][1] + self.getYWidth('_PolyRouteXOnPMOS') / 2]
                                        ])
            tmpPolyRouteYOnNMOS.append([[self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] +
                                         self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0],
                                         self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] +
                                         self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][1]],
                                        [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] +
                                         self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0],
                                         self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][1] - self.getYWidth('_PolyRouteXOnPMOS') / 2]
                                        ])

        self._DesignParameter['_PolyRouteYOnPMOS']['_XYCoordinates'] = tmpPolyRouteYOnPMOS
        self._DesignParameter['_PolyRouteYOnNMOS']['_XYCoordinates'] = tmpPolyRouteYOnNMOS



        # Output Metal (1&2) Boundary & Routing ------------------------------------------------------------------------

        # Output M1 Routing (Column Line)
        tmpOutputRoutingM1Y = []
        for i in range(0, (len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']) + 1) // 2):
            tmpOutputRoutingM1Y.append([CoordCalc.Add(self.getXY('_PMOS', '_XYCoordinatePMOSOutputRouting')[2 * i], [0, +self.getYWidth('_PMOS', '_Met1Layer')/2]),
                                        CoordCalc.Add(self.getXY('_NMOS', '_XYCoordinateNMOSOutputRouting')[2 * i], [0, -self.getYWidth('_NMOS', '_Met1Layer')/2])
                                        ])  #

        if (_Finger % 4 == 2) and (_Finger != 2):  # exception case (6, 10, 14, 18, ...)
            del tmpOutputRoutingM1Y[-1]
            tmpOutputRoutingM1Y.append(
                [CoordCalc.Add(self._DesignParameter['_PMOS']['_XYCoordinates'][0],
                               self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter[
                                   '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1]),
                 CoordCalc.Add(self._DesignParameter['_NMOS']['_XYCoordinates'][0],
                               self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter[
                                   '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1])])
        else:
            pass

        self._DesignParameter['_OutputRouting'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1])
        # self._DesignParameter['_OutputRouting']['_Width'] = _DRCObj._Metal1MinWidth           # Need to Modify
        self._DesignParameter['_OutputRouting']['_Width'] = self.getXWidth('_ViaMet12Met2OnNMOSOutput', '_Met1Layer')
        self._DesignParameter['_OutputRouting']['_XYCoordinates'] = tmpOutputRoutingM1Y

        if _Finger == 1:
            del self._DesignParameter['_ViaMet12Met2OnNMOSOutput']
            del self._DesignParameter['_ViaMet12Met2OnPMOSOutput']

        # Output M2 Routing (Row Line)
        self._DesignParameter['_Met2OnOutput'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1])
        # self._DesignParameter['_Met2OnOutput']['_Width'] = _DRCObj._MetalxMinWidth  # Need to Modify
        self._DesignParameter['_Met2OnOutput']['_Width'] = _DRCObj._VIAxMinWidth + 2 * _DRCObj._MetalxMinEnclosureVia3
        self._DesignParameter['_Met2OnOutput']['_XYCoordinates'] = \
            [[CoordCalc.getXYCoords_MaxX(self.getXY('_PMOS', '_XYCoordinatePMOSOutputRouting'))[0],
              CoordCalc.getXYCoords_MinX(self.getXY('_PMOS', '_XYCoordinatePMOSOutputRouting'))[0]],
             [CoordCalc.getXYCoords_MaxX(self.getXY('_NMOS', '_XYCoordinateNMOSOutputRouting'))[0],
              CoordCalc.getXYCoords_MinX(self.getXY('_NMOS', '_XYCoordinateNMOSOutputRouting'))[0]]]

        # Input Contact (Poly to M1)------------------------------------------------------------------------------------
        '''
        Function : Make Contact(Poly to M1) for _PolyRouteXOn{}
                   2 kind of calculation
                   (1) surrounded by output metal(left and right)   if _Finger > 4
                   (2) rightmost 
        Require : OutputRouting, _PolyRouteXOn{NMOS PMOS}, PMOS, NMOS

        '''
        # (0)
        _VIATempPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        _VIATempPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = 3
        _VIATempPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = 1
        self._DesignParameter['_VIATempPoly2Met1'] = self._SrefElementDeclaration(
            _DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='ViaPoly2Met1_TempIn{}'.format(_Name)))[0]
        self._DesignParameter['_VIATempPoly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
            **_VIATempPoly2Met1)

        distance_input = self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'][0][1] - \
                         self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][1]
        distance_contact = distance_input - \
                           self._DesignParameter['_VIATempPoly2Met1']['_DesignObj']._DesignParameter['_COLayer'][
                               '_YWidth']
        distance_poly = distance_input - max(self._DesignParameter['_PolyRouteXOnPMOS']['_YWidth'],
                                             self._DesignParameter['_VIATempPoly2Met1']['_DesignObj']._DesignParameter[
                                                 '_POLayer']['_YWidth'])
        distance_metal1 = distance_input - \
                          self._DesignParameter['_VIATempPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer'][
                              '_YWidth']

        flag_poly = True if distance_poly < _DRCObj.DRCPolyMinSpace(
            _Width=self._DesignParameter['_PolyRouteXOnPMOS']['_XWidth'],
            _ParallelLength=self._DesignParameter['_PolyRouteXOnPMOS']['_YWidth']) else False
        flag_metal = True if distance_metal1 < _DRCObj._Metal1MinSpace else False
        flag_contact = True if distance_contact < _DRCObj._CoMinSpace else False
        if (not flag_contact) and (not flag_metal) and (not flag_poly):
            flag_horizontal_inputvia_PCCOM1 = False
            Average2Up, Average2Dn = 0, 0
        else:
            flag_horizontal_inputvia_PCCOM1 = True
            Average2Up = self.CeilMinSnapSpacing(float(distance_input) / 2.0, _DRCObj._MinSnapSpacing)
            Average2Dn = distance_input - Average2Up

            self._DesignParameter['_PolyRouteXOnMOS'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1])
            self._DesignParameter['_PolyRouteXOnMOS']['_XWidth'] = self._DesignParameter['_PolyRouteXOnPMOS']['_XWidth']
            self._DesignParameter['_PolyRouteXOnMOS']['_YWidth'] = self.RounddownMinSnapSpacing(
                distance_input + self._DesignParameter['_PolyRouteXOnPMOS']['_YWidth'], 2 * _DRCObj._MinSnapSpacing)
            self._DesignParameter['_PolyRouteXOnMOS']['_XYCoordinates'] = [
                CoordCalc.Add(self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0],
                              [0, Average2Up])]

        # (1) surrounded by output metal  /  of Input Contact (Poly to M1)
        if _Finger > 4:  # No Need else statement (when finger is 1, 2, 3, it covers on (2))
            ''' ************************ temporal DRC... Need 2 Modify Later ************************ '''
            if DesignParameters._Technology == 'SS28nm':
                _tmpDRC_Metal1MinSpaceAtCorner = 70
                # _tmpDRC_Metal1MinSpaceAtCorner = _DRCObj._Metal1MinSpaceAtCorner
            else:
                _tmpDRC_Metal1MinSpaceAtCorner = _DRCObj._Metal1MinSpaceAtCorner

            # Calculate Number of Contact_X 'tmpNumCOX'
            lengthM1BtwOutputRouting = self._DesignParameter['_OutputRouting']['_XYCoordinates'][1][0][0] \
                                       - self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][0] \
                                       - self._DesignParameter['_OutputRouting']['_Width'] \
                                       - 2 * _tmpDRC_Metal1MinSpaceAtCorner

            unitLengthBtwCOX = _DRCObj._CoMinWidth + _DRCObj._CoMinSpace
            tmpNumCOX = int((
                                        lengthM1BtwOutputRouting - _DRCObj._CoMinWidth - 2 * _DRCObj._Metal1MinEnclosureCO2) // unitLengthBtwCOX) + 1

            # NMOS & PMOS
            _VIANMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
            _VIAPMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
            _VIANMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = tmpNumCOX
            _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = tmpNumCOX
            _VIANMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = 1
            _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = 1

            self._DesignParameter['_VIANMOSPoly2Met1'] = self._SrefElementDeclaration(
                _DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='ViaPoly2Met1OnNMOSGateIn{}'.format(_Name)))[0]
            self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
                **_VIANMOSPoly2Met1)
            self._DesignParameter['_VIAPMOSPoly2Met1'] = self._SrefElementDeclaration(
                _DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='ViaPoly2Met1OnPMOSGateIn{}'.format(_Name)))[0]
            self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
                **_VIAPMOSPoly2Met1)

            tmpInputPCCOM1onNMOS, tmpInputPCCOM1onPMOS = [], []
            for i in range(0, len(self._DesignParameter['_OutputRouting']['_XYCoordinates']) - 1):
                tmpInputPCCOM1onNMOS.append(
                    [self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][2 * i + 1][0],
                     self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][1] + Average2Up])
                tmpInputPCCOM1onPMOS.append(
                    [self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'][2 * i + 1][0],
                     self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'][0][1] - Average2Dn])

            self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'] = tmpInputPCCOM1onNMOS
            self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'] = tmpInputPCCOM1onPMOS

            # exception case
            if (_Finger % 4 == 2) and (_Finger != 2):
                del self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'][-1]
                del self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][-1]

        ## (2) rightmost output metal  /  of Input Contact (Poly to M1)
        if (_Finger % 4 == 2) and (_Finger != 2):  # exception case
            tmpLeftM1Boundary = self._DesignParameter['_OutputRouting']['_XYCoordinates'][-2][0][0] \
                                + 0.5 * self._DesignParameter['_OutputRouting']['_Width'] \
                                + _DRCObj._Metal1MinSpaceAtCorner
            tmpRightM1Boundary = self._DesignParameter['_OutputRouting']['_XYCoordinates'][-1][0][0] \
                                 - 0.5 * self._DesignParameter['_OutputRouting']['_Width'] \
                                 - _DRCObj._Metal1MinSpaceAtCorner
            tmpLeftCoBoundary = tmpLeftM1Boundary + _DRCObj._Metal1MinEnclosureCO2  # Calculate by M1-CO
            tmpRightCoBoundary = tmpRightM1Boundary - _DRCObj._Metal1MinEnclosureCO2  # Calculate by M1-CO
        elif _Finger != 1:
            tmpLeftM1Boundary = self._DesignParameter['_OutputRouting']['_XYCoordinates'][-1][0][0] \
                                + 0.5 * self._DesignParameter['_OutputRouting']['_Width'] \
                                + _DRCObj._Metal1MinSpaceAtCorner
            tmpRightPOBoundary = \
            self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][0] \
            + 0.5 * _ChannelLength
            tmpLeftCoBoundary = tmpLeftM1Boundary + _DRCObj._Metal1MinEnclosureCO2  # Calculate by M1-CO
            tmpRightCoBoundary = tmpRightPOBoundary - _DRCObj._CoMinEnclosureByPOAtLeastTwoSide  # Calculate by PO-CO
        elif (_Finger == 1) and (DesignParameters._Technology == 'SS28nm'):
            tmpLeftCoBoundary = 0
            tmpRightCoBoundary = 0
        else:
            raise NotImplementedError

        NumCoRightMost = int((tmpRightCoBoundary - tmpLeftCoBoundary - _DRCObj._CoMinWidth) // (
                    _DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 1

        if NumCoRightMost > 0:
            _VIAMOSPoly2Met1RightMost = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)

            _VIAMOSPoly2Met1RightMost['_ViaPoly2Met1NumberOfCOX'] = NumCoRightMost
            _VIAMOSPoly2Met1RightMost['_ViaPoly2Met1NumberOfCOY'] = 1

            self._DesignParameter['_VIAMOSPoly2Met1RightMost'] = self._SrefElementDeclaration(
                _DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='ViaPoly2Met1RightMostOnNMOSGateIn{}'.format(_Name)))[0]
            self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
                **_VIAMOSPoly2Met1RightMost)
            self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_XYCoordinates'] = [
                [self.RounddownMinSnapSpacing((tmpLeftCoBoundary + tmpRightCoBoundary) / 2, MinSnapSpacing),
                 self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][1] + Average2Up],
                [self.RounddownMinSnapSpacing((tmpLeftCoBoundary + tmpRightCoBoundary) / 2, MinSnapSpacing),
                 self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'][0][1] - Average2Dn]
            ]  # both NMOS & PMOS

        if '_VIAPMOSPoly2Met1_F1' in self._DesignParameter:
            self._DesignParameter['_VIANMOSPoly2Met1'] = self._DesignParameter['_VIANMOSPoly2Met1_F1']
            self._DesignParameter['_VIAPMOSPoly2Met1'] = self._DesignParameter['_VIAPMOSPoly2Met1_F1']
            del self._DesignParameter['_VIANMOSPoly2Met1_F1']
            del self._DesignParameter['_VIAPMOSPoly2Met1_F1']

        # Input Met1 Routing -------------------------------------------------------------------------------------------
        '''
        When there is a gap between (routed) poly gates, route them by Met1 (column line)
        Strategy : Route Input M1 on the same YCoordinates as the SupplyRouting M1
                   (Supply M1 outside the poly gate route is ignored)
        '''
        tmpInputRouting = []  # if list is appended twice, tmp=[ [[1,2],[3,4]], [[5,6],[7,8]] ]
        if '_VIANMOSPoly2Met1' in self._DesignParameter:
            for i in range(0, len(self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'])):
                tmpInputRouting.append([self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'][i],
                                        self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][i]])
        if '_VIAMOSPoly2Met1RightMost' in self._DesignParameter:
            tmpInputRouting.append(self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_XYCoordinates'])

        self._DesignParameter['_InputRouting'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1])
        # self._DesignParameter['_InputRouting']['_Width'] = _DRCObj._Metal1MinWidth
        self._DesignParameter['_InputRouting']['_Width'] = _DRCObj._VIAxMinWidth + 2 * _DRCObj._Metal1MinEnclosureVia3
        self._DesignParameter['_InputRouting']['_XYCoordinates'] = tmpInputRouting

        ################################################################################################################
        # # Input M1 Route up tp M2
        if DesignParameters._Technology in ('SS28nm', 'TSMC65nm'):
            # count input M1 segment
            tmpCount_GateViaLayer = 0

            if '_VIAMOSPoly2Met1RightMost' in self._DesignParameter:
                tmpCount_GateViaLayer += 1
                flag_exception_rightmost = True
            else:
                flag_exception_rightmost = False
            if '_VIAPMOSPoly2Met1' in self._DesignParameter:
                tmpCount_GateViaLayer += len(self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'])

            if (DesignParameters._Technology == 'SS28nm') and (tmpCount_GateViaLayer > 1) and flag_horizontal_inputvia_PCCOM1:
                # M1V1M2
                # (1) Normal width
                _LengthM1_VIAPMOSPoly2Met1 = self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
                _NumViaInputM12 = int((_LengthM1_VIAPMOSPoly2Met1 - _DRCObj._VIAxMinWidth - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide)
                                      // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

                _ViaMet12Met2forInput = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
                _ViaMet12Met2forInput['_ViaMet12Met2NumberOfCOX'] = _NumViaInputM12
                _ViaMet12Met2forInput['_ViaMet12Met2NumberOfCOY'] = 1
                self._DesignParameter['_ViaMet12Met2forInput'] = self._SrefElementDeclaration(
                    _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='ViaMet12Met2forInputIn{}'.format(_Name)))[0]
                self._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._CalculateDesignParameterSameEnclosure(**_ViaMet12Met2forInput)

                # (2) RightMost
                if flag_exception_rightmost:
                    _LengthM1_VIAPMOSPoly2Met1_RightMost = self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
                    _NumViaInputM12_RightMost = int((_LengthM1_VIAPMOSPoly2Met1_RightMost - _DRCObj._VIAxMinWidth - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide)
                                                    // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

                    _ViaMet12Met2forInput2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
                    _ViaMet12Met2forInput2['_ViaMet12Met2NumberOfCOX'] = _NumViaInputM12_RightMost
                    _ViaMet12Met2forInput2['_ViaMet12Met2NumberOfCOY'] = 1
                    self._DesignParameter['_ViaMet12Met2forInput2'] = self._SrefElementDeclaration(
                        _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='ViaMet12Met2forInput2In{}'.format(_Name)))[0]
                    self._DesignParameter['_ViaMet12Met2forInput2']['_DesignObj']._CalculateDesignParameterSameEnclosure(**_ViaMet12Met2forInput2)

                tmpXYs = []
                for i in range(0, len(self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'])):
                    tmpXYs.append([self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] +
                                   self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][i][0],
                                   self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][1]])
                self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'] = tmpXYs

                if flag_exception_rightmost:
                    self._DesignParameter['_ViaMet12Met2forInput2']['_XYCoordinates'] = \
                        [[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] +
                          self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_XYCoordinates'][0][0],
                          self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][1]]]

                self._DesignParameter['_CLKMet2InRouting'] = self._PathElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['METAL2'][0],
                    _Datatype=DesignParameters._LayerMapping['METAL2'][1])
                self._DesignParameter['_CLKMet2InRouting']['_Width'] = self._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
                self._DesignParameter['_CLKMet2InRouting']['_XYCoordinates'] = [
                    [self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'][0],
                     self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'][-1]]]
                if flag_exception_rightmost:
                    self._DesignParameter['_CLKMet2InRouting']['_XYCoordinates'] = [
                        [self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'][0],
                         self._DesignParameter['_ViaMet12Met2forInput2']['_XYCoordinates'][0]]]

            elif (DesignParameters._Technology in ('SS28nm', 'TSMC65nm')) and (tmpCount_GateViaLayer > 1):
                # M1V1M2
                # (1) Normal width
                _LengthM1Y_VIAMOSPoly2Met1 = \
                self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
                + abs(self._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][1] -
                      self._DesignParameter['_InputRouting']['_XYCoordinates'][0][1][1])
                _NumViaInputM12 = int((_LengthM1Y_VIAMOSPoly2Met1 - _DRCObj._VIAxMinWidth - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide)
                                      // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

                _ViaMet12Met2forInput = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
                _ViaMet12Met2forInput['_ViaMet12Met2NumberOfCOX'] = 1
                _ViaMet12Met2forInput['_ViaMet12Met2NumberOfCOY'] = _NumViaInputM12 if _NumViaInputM12 < 3 else 3
                self._DesignParameter['_ViaMet12Met2forInput'] = self._SrefElementDeclaration(
                    _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='ViaMet12Met2forInputIn{}'.format(_Name)))[0]
                self._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._CalculateDesignParameterSameEnclosure(**_ViaMet12Met2forInput)

                tmpXYs = []
                for i in range(0, len(self._DesignParameter['_InputRouting']['_XYCoordinates'])):
                    tmpXYs.append([self._DesignParameter['_InputRouting']['_XYCoordinates'][i][0][0],
                                   (self._DesignParameter['_InputRouting']['_XYCoordinates'][i][0][1] +
                                    self._DesignParameter['_InputRouting']['_XYCoordinates'][i][1][1]) / 2])
                self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'] = tmpXYs

                self._DesignParameter['_CLKMet2InRouting'] = self._PathElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1])
                # self._DesignParameter['_CLKMet2InRouting']['_Width'] = _DRCObj._MetalxMinWidth
                self._DesignParameter['_CLKMet2InRouting']['_Width'] = _DRCObj._VIAxMinWidth + 2 * _DRCObj._Metal1MinEnclosureVia3
                self._DesignParameter['_CLKMet2InRouting']['_XYCoordinates'] = [
                    # [CoordCalc.Add(self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'][0], [0, -self.getXWidth('_ViaMet12Met2forInput', '_Met2Layer')]),
                    #  CoordCalc.Add(self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'][-1], [0, self.getXWidth('_ViaMet12Met2forInput', '_Met2Layer')])]]
                    [self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'][0],
                     self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'][-1]]
                ]

        # end of 'if _VDD2VSSHeight == _VDD2VSSMinHeight:'

        # exception case... Need to Modify later...... Not tested in 65nm
        if DesignParameters._Technology == 'SS28nm':
            _DRC_M1MinWidth_WhenCalcMinArea = 130

            if (_Finger == 1) and (_VDD2VSSHeight == _VDD2VSSMinHeight):
                tmpX = self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
                tmpY = self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
                if (tmpX * tmpY) < _DRCObj._Metal1MinArea:
                    tmpY_calc = self.CeilMinSnapSpacing(_DRCObj._Metal1MinArea / tmpX, MinSnapSpacing)
                    if tmpY_calc < _DRC_M1MinWidth_WhenCalcMinArea:  # Rule by samsung28nm GR501aSE only for 28nm...
                        tmpY_calc = _DRC_M1MinWidth_WhenCalcMinArea

                    self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = tmpY_calc

            elif (_Finger == 2) and (_VDD2VSSHeight == _VDD2VSSMinHeight):
                tmpX = self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
                tmpY = self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
                if (tmpX * tmpY) < _DRCObj._Metal1MinArea:
                    tmpX_calc = self.CeilMinSnapSpacing(_DRCObj._Metal1MinArea / tmpY, MinSnapSpacing)
                    if tmpX_calc < _DRC_M1MinWidth_WhenCalcMinArea:  # Rule by samsung28nm GR501aSE only for 28nm...
                        tmpX_calc = _DRC_M1MinWidth_WhenCalcMinArea
                    self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = tmpX_calc
                    self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] = \
                        self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] \
                        + tmpX_calc / 2 - tmpX / 2

        """ Routing Finished / Next : Additional Layers """

        ''' ---------------------------------------- PP/NP Additional Layer ---------------------------------------- '''
        if DesignParameters._Technology == 'TSMC65nm':
            Ybot_PolyRouteXOnPMOS = self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'][0][1] - 0.5 * \
                                    self._DesignParameter['_PolyRouteXOnPMOS']['_YWidth']
            Ytop_PolyRouteXOnNMOS = self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][1] + 0.5 * \
                                    self._DesignParameter['_PolyRouteXOnNMOS']['_YWidth']

            # case 1) Enlarge each PP/NP Layers
            if abs(Ybot_PolyRouteXOnPMOS - Ytop_PolyRouteXOnNMOS) >= 2 * _DRCObj._PpMinEnclosureOfPo:
                self._DesignParameter['_PIMPforGatePoly'] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['PIMP'][0],
                    _Datatype=DesignParameters._LayerMapping['PIMP'][1])
                self._DesignParameter['_NIMPforGatePoly'] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['NIMP'][0],
                    _Datatype=DesignParameters._LayerMapping['NIMP'][1])

                self._DesignParameter['_PIMPforGatePoly']['_XYCoordinates'] = \
                self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates']
                self._DesignParameter['_NIMPforGatePoly']['_XYCoordinates'] = \
                self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates']
                self._DesignParameter['_PIMPforGatePoly']['_XWidth'] = \
                self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']
                self._DesignParameter['_NIMPforGatePoly']['_XWidth'] = \
                self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']
                self._DesignParameter['_PIMPforGatePoly']['_YWidth'] = self._DesignParameter['_PolyRouteXOnPMOS'][
                                                                           '_YWidth'] + 2 * _DRCObj._PpMinEnclosureOfPo
                self._DesignParameter['_NIMPforGatePoly']['_YWidth'] = self._DesignParameter['_PolyRouteXOnNMOS'][
                                                                           '_YWidth'] + 2 * _DRCObj._PpMinEnclosureOfPo

            # case 2) Fill the gap between PP&NP Layer with only NP Layer
            else:
                Ybot_PPLayerOnPMOS = self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - 0.5 * \
                                     self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']
                Ytop_NPLayerOnNMOS = self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + 0.5 * \
                                     self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']

                self._DesignParameter['_NIMPforGatePoly'] = self._PathElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['NIMP'][0],
                    _Datatype=DesignParameters._LayerMapping['NIMP'][1])
                self._DesignParameter['_NIMPforGatePoly']['_Width'] = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']
                self._DesignParameter['_NIMPforGatePoly']['_XYCoordinates'] = [
                    [[self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][0], Ybot_PPLayerOnPMOS],
                     [self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][0], Ytop_NPLayerOnNMOS]]]
        elif DesignParameters._Technology == 'SS28nm':
            pass
        else:
            raise NotImplementedError

        ''' ------------------------------------------- NWELL Generation ------------------------------------------- '''
        '''
        Function    : Generate NWELL by PathElementDeclaration (column line)
        Requirement : NbodyContact(ODLayer), _PMOS(ODLayer)
        '''
        XWidth1_NWLayer = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._NwMinEnclosurePactive
        XWidth2_NWLayer = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._NwMinEnclosurePactive2
        XWidth_NWLayer = max(XWidth1_NWLayer, XWidth2_NWLayer)

        XYCoordinatesOfNW_top = CoordCalc.Add(self._DesignParameter['NbodyContact']['_XYCoordinates'][0],
                                              [0, self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2 + _DRCObj._NwMinEnclosurePactive])
        XYCoordinatesOfNW_bot = CoordCalc.Add(self._DesignParameter['_PMOS']['_XYCoordinates'][0],
                                              [0, -self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2 - _DRCObj._NwMinEnclosurePactive])
        YWidth_NWLayer = abs(XYCoordinatesOfNW_top[1] - XYCoordinatesOfNW_bot[1])

        if (XWidth_NWLayer * YWidth_NWLayer) < _DRCObj._NwMinArea:
            XWidth_NWLayer = self.CeilMinSnapSpacing(_DRCObj._NwMinArea / YWidth_NWLayer, 2 * MinSnapSpacing)
        else:
            pass

        self._DesignParameter['_NWLayer'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1])
        self._DesignParameter['_NWLayer']['_Width'] = XWidth_NWLayer
        self._DesignParameter['_NWLayer']['_XYCoordinates'] = [[XYCoordinatesOfNW_top, XYCoordinatesOfNW_bot]]

        ''' ----------------------------------------  XVT Layer Modification --------------------------------------- '''
        if DesignParameters._Technology == 'SS28nm':
            assert _XVT in ('SLVT', 'LVT', 'RVT', 'HVT')

            self._DesignParameter['XVTLayer'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping[_XVT][0], _Datatype=DesignParameters._LayerMapping[_XVT][1])
            self._DesignParameter['XVTLayer']['_XWidth'] = (_GateSpacing + _ChannelLength) * (_Finger + 1)
            self._DesignParameter['XVTLayer']['_YWidth'] = _VDD2VSSHeight
            self._DesignParameter['XVTLayer']['_XYCoordinates'] = [[0, _VDD2VSSHeight/2]]

        elif DesignParameters._Technology == 'TSMC65nm':
            pass  # No Need to Modify XVT Layer
        else:
            raise NotImplementedError

        # ''' -------------------------------------  Pin Generation & Coordinates ------------------------------------ '''
        # self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
        #     _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.04, _Angle=0, _TEXT='VSS')
        #
        # self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
        #     _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.04, _Angle=0, _TEXT='VDD')
        #
        # self._DesignParameter['_Inputpin'] = self._TextElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
        #     _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.01, _Angle=0, _TEXT='A')
        #
        # self._DesignParameter['_Outputpin'] = self._TextElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
        #     _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.01, _Angle=0, _TEXT='Y')
        #
        # self._DesignParameter['_VSSpin']['_XYCoordinates'] = [[0, 0]]
        # self._DesignParameter['_VDDpin']['_XYCoordinates'] = [[0, _VDD2VSSHeight]]
        # self._DesignParameter['_Inputpin']['_XYCoordinates'] = [
        #     [round((self._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][0] +
        #             self._DesignParameter['_InputRouting']['_XYCoordinates'][0][1][0]) / 2),
        #      round((self._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][1] +
        #             self._DesignParameter['_InputRouting']['_XYCoordinates'][0][1][1]) / 2)]
        # ]
        # self._DesignParameter['_Outputpin']['_XYCoordinates'] = [
        #     [round((self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][0] +
        #             self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][1][0]) / 2),
        #      self._DesignParameter['_Inputpin']['_XYCoordinates'][0][1]]
        # ]


        print(''.center(105, '#'))
        print('     {} Calculation End     '.format(_Name).center(105, '#'))
        print(''.center(105, '#'))


    def _CalculateDesignParameter_v2(self,
                                     _Finger=1,
                                     _ChannelWidth=200,
                                     _ChannelLength=30,
                                     _NPRatio=2,

                                     _VDD2VSSHeight=1800,
                                     _VDD2PMOSHeight=599,
                                     _VSS2NMOSHeight=461,

                                     _Dummy=True,
                                     _XVT='SLVT',
                                     _GateSpacing=120,
                                     _SDWidth=66,

                                     _NumViaPoly2Met1CoX=None,
                                     _NumViaPoly2Met1CoY=None,
                                     _NumViaPMOSMet12Met2CoY=None,
                                     _NumViaNMOSMet12Met2CoY=None,
                                     ):
        """

        :param _Finger:
        :param _ChannelWidth:
        :param _ChannelLength:
        :param _NPRatio:
        :param _Dummy:
        :param _XVT:
        :param _GateSpacing:
        :param _VDD2VSSHeight:
        :param _NumViaPoly2Met1CoX:
        :param _NumViaPoly2Met1CoY:
        :param _NumViaPMOSMet12Met2CoY: (optional, but recommended to None) | None(default) : calculated by 'YWidth of MOSFET's S/D Metal1', minimum : 2
        :param _NumViaNMOSMet12Met2CoY: (optional, but recommended to None) | None(default) : calculated by 'YWidth of MOSFET's S/D Metal1', minimum : 2
        :return:
        """

        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        MinSnapSpacing = _DRCObj._MinSnapSpacing

        print(''.center(105, '#'))
        print('     {} Calculation Start     '.format(_Name).center(105, '#'))
        print(''.center(105, '#'))

        ''' ------------------------------------------ MOSFET Generation ------------------------------------------- '''
        # 1) _NMOS Generation ------------------------------------------------------------------------------------------
        NMOSparameters = copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation)
        NMOSparameters['_NMOSNumberofGate'] = _Finger
        NMOSparameters['_NMOSChannelWidth'] = _ChannelWidth
        NMOSparameters['_NMOSChannellength'] = _ChannelLength
        NMOSparameters['_NMOSDummy'] = _Dummy
        NMOSparameters['_XVT'] = _XVT
        NMOSparameters['_GateSpacing'] = _GateSpacing
        NMOSparameters['_SDWidth'] = _SDWidth

        self._DesignParameter['_NMOS'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOS_In{}'.format(_Name)))[0]
        self._DesignParameter['_NMOS']['_DesignObj']._CalculateNMOSDesignParameter(**NMOSparameters)

        # 2) _PMOS Generation ------------------------------------------------------------------------------------------
        PMOSparameters = copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation)
        PMOSparameters['_PMOSNumberofGate'] = _Finger
        PMOSparameters['_PMOSChannelWidth'] = round(_ChannelWidth * _NPRatio)  # Need to Modify
        PMOSparameters['_PMOSChannellength'] = _ChannelLength
        PMOSparameters['_PMOSDummy'] = _Dummy
        PMOSparameters['_XVT'] = _XVT
        PMOSparameters['_GateSpacing'] = _GateSpacing
        PMOSparameters['_SDWidth'] = _SDWidth

        self._DesignParameter['_PMOS'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOS_In{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS']['_DesignObj']._CalculatePMOSDesignParameter(**PMOSparameters)


        ''' ---------------------------------------- Supply Rail Generation ---------------------------------------- '''
        self._DesignParameter['PbodyContact'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VSSRailIn{}'.format(_Name)))[0]
        self._DesignParameter['PbodyContact']['_DesignObj']._CalculateDesignParameter(
            **dict(NumPitch=_Finger + 1, UnitPitch=(_GateSpacing + _ChannelLength),
                   Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=True, deleteViaAndMet1=False))
        self._DesignParameter['PbodyContact']['_XYCoordinates'] = [[0.0, 0.0]]
        self._DesignParameter['NbodyContact'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VDDRailIn{}'.format(_Name)))[0]
        self._DesignParameter['NbodyContact']['_DesignObj']._CalculateDesignParameter(
            **dict(NumPitch=_Finger + 1, UnitPitch=(_ChannelLength + _GateSpacing),
                   Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=False, deleteViaAndMet1=False))
        self._DesignParameter['NbodyContact']['_XYCoordinates'] = [[0, _VDD2VSSHeight]]


        ''' -------------------------------------------- Via Generation -------------------------------------------- '''
        # 1) VIA Generation for PMOS Output ----------------------------------------------------------------------------
        if _NumViaPMOSMet12Met2CoY == None:  # Default : calculate
            YWidthOfPMOSMet1 = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            NumViaYPMOS = int((YWidthOfPMOSMet1 - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
        else:
            NumViaYPMOS = _NumViaPMOSMet12Met2CoY

        VIAPMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        VIAPMOSMet12['_ViaMet12Met2NumberOfCOX'] = 1
        VIAPMOSMet12['_ViaMet12Met2NumberOfCOY'] = NumViaYPMOS if (NumViaYPMOS > 2) else 2

        self._DesignParameter['_ViaMet12Met2OnPMOSOutput'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='ViaMet12Met2OnPMOSOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._CalculateDesignParameterSameEnclosure(**VIAPMOSMet12)

        # 1-1) Metal1 YWidth re-calculation
        self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
            = max(self.getYWidth('_ViaMet12Met2OnPMOSOutput', '_Met1Layer'), self.getYWidth('_PMOS', '_Met1Layer'))

        Area_M1for_ViaMet12Met2OnPMOSOutput = self.getXWidth('_ViaMet12Met2OnPMOSOutput', '_Met1Layer') \
                                              * self.getYWidth('_ViaMet12Met2OnPMOSOutput', '_Met1Layer')
        if Area_M1for_ViaMet12Met2OnPMOSOutput < _DRCObj._Metal1MinArea:
            YWidth_recalculated_byMinArea = self.CeilMinSnapSpacing(_DRCObj._Metal1MinArea / self.getXWidth('_ViaMet12Met2OnPMOSOutput', '_Met1Layer'), 2 * MinSnapSpacing)
            self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = YWidth_recalculated_byMinArea
        else:
            pass

        # 2) VIA Generation for NMOS Output ----------------------------------------------------------------------------
        if _NumViaNMOSMet12Met2CoY == None:  # Default : calculate
            YWidthOfNMOSMet1 = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            NumViaYNMOS = int((YWidthOfNMOSMet1 - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
        else:
            NumViaYNMOS = _NumViaNMOSMet12Met2CoY

        VIANMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        VIANMOSMet12['_ViaMet12Met2NumberOfCOX'] = 1
        VIANMOSMet12['_ViaMet12Met2NumberOfCOY'] = NumViaYNMOS if (NumViaYNMOS > 2) else 2

        self._DesignParameter['_ViaMet12Met2OnNMOSOutput'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='ViaMet12Met2OnNMOSOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._CalculateDesignParameterSameEnclosure(**VIANMOSMet12)

        # 2-1) Metal1 YWidth re-calculation
        self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
            = max(self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                  self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
        Area_M1for_ViaMet12Met2OnNMOSOutput = self.getXWidth('_ViaMet12Met2OnNMOSOutput', '_Met1Layer') \
                                              * self.getYWidth('_ViaMet12Met2OnNMOSOutput', '_Met1Layer')
        if Area_M1for_ViaMet12Met2OnNMOSOutput < _DRCObj._Metal1MinArea:
            YWidth_recalculated_byMinArea = self.CeilMinSnapSpacing(_DRCObj._Metal1MinArea / self.getXWidth('_ViaMet12Met2OnNMOSOutput', '_Met1Layer'), 2 * MinSnapSpacing)
            self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = YWidth_recalculated_byMinArea
        else:
            pass

        # 3) Input VIA Generation for Finger=1 / or calculate input poly-M1 contact YWidth     -> Need to check
        if _Finger == 1:
            _VIAMOSPoly2Met1_F1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
            _VIAMOSPoly2Met1_F1['_ViaPoly2Met1NumberOfCOX'] = 1  # Need to Modify (by calculation for wide channel length)
            _VIAMOSPoly2Met1_F1['_ViaPoly2Met1NumberOfCOY'] = 1  # Need to Modify (by user input parameter)
            self._DesignParameter['_VIANMOSPoly2Met1_F1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='ViaPoly2Met1_F1OnNMOSGateIn{}'.format(_Name)))[0]
            self._DesignParameter['_VIANMOSPoly2Met1_F1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIAMOSPoly2Met1_F1)
            self._DesignParameter['_VIAPMOSPoly2Met1_F1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='ViaPoly2Met1_F1OnPMOSGateIn{}'.format(_Name)))[0]
            self._DesignParameter['_VIAPMOSPoly2Met1_F1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIAMOSPoly2Met1_F1)

            self._DesignParameter['_VIANMOSPoly2Met1_F1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + 2 * _DRCObj._Metal1MinEnclosureVia3
            self._DesignParameter['_VIAPMOSPoly2Met1_F1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + 2 * _DRCObj._Metal1MinEnclosureVia3
        else:
            WidthOfInputXM1 = _DRCObj._CoMinWidth + 2 * _DRCObj._Metal1MinEnclosureCO2  # how?? you have to choose / Need to Modify (by user input parameter) / ambiguous name


        ''' -------------------------------------------------------------------------------------------------------- '''
        ''' ------------------------------------------ Coordinates setting ----------------------------------------- '''
        ''' -------------------------------------------------------------------------------------------------------- '''
        # 1) Calculate Distance Between 'Supply rail' and 'MOSFET'  : concern (SS28nm, TSMC65nm) and (Dummy T/F)
        if DesignParameters._Technology == 'SS28nm':
            DistanceBtwVSS2NMOS1 = (self.getYWidth('PbodyContact', '_PPLayer') + self.getYWidth('_NMOS','_POLayer')) / 2
            DistanceBtwVSS2NMOS2 = 0.5 * (self.getYWidth('PbodyContact', '_ODLayer') + self.getYWidth('_NMOS', '_ODLayer')) \
                                   + _DRCObj._OdMinSpace  # OD Layer(for Pbody) - OD Layer (for NMOS)     OD=RX
            if '_PODummyLayer' in self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter:
                DistanceBtwVSS2NMOS3 = 0.5 * self.getYWidth('PbodyContact', '_ODLayer') \
                                       + 0.5 * self.getYWidth('_NMOS', '_PODummyLayer') \
                                       + _DRCObj._PolygateMinSpace2OD  # OD Layer(for Pbody) - PO Dummy Layer (for NMOS)     OD=RX
            else:
                DistanceBtwVSS2NMOS3 = 0
            if '_Met1Layer' in self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter:
                DistanceBtwVSS2NMOS4 = 0.5 * self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
                                       + 0.5 * max(self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                                   self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) \
                                       + _DRCObj._Metal1MinSpace2  # Need to Modify
            else:
                DistanceBtwVSS2NMOS4 = 0
            DistanceBtwVSS2NMOS_minimum = max(DistanceBtwVSS2NMOS1, DistanceBtwVSS2NMOS2, DistanceBtwVSS2NMOS3,DistanceBtwVSS2NMOS4)

            DistanceBtwVDD2PMOS1 = 0.5 * self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] \
                                   + 0.5 * self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] \
                                   + _DRCObj._OdMinSpace
            DistanceBtwVD2PMOS2 = 0.5 * self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] \
                                  + 0.5 * self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] \
                                  + _DRCObj._OdMinSpace  # OD Layer(for Nbody) - OD Layer (for PMOS)     OD=RX
            if '_PODummyLayer' in self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter:
                DistanceBtwVDD2PMOS3 = 0.5 * self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] \
                                       + 0.5 * self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] \
                                       + _DRCObj._PolygateMinSpace2OD  # OD Layer(for Nbody) - PO Dummy Layer (for PMOS)     OD=RX
            else:
                DistanceBtwVDD2PMOS3 = 0
            if '_Met1Layer' in self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter:
                DistanceBtwVDD2PMOS4 = 0.5 * self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
                                       + 0.5 * max(self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                                   self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) \
                                       + _DRCObj._Metal1MinSpace2  # Need to Modify
            else:
                DistanceBtwVDD2PMOS4 = 0
            DistanceBtwVDD2PMOS_minimum = max(DistanceBtwVDD2PMOS1, DistanceBtwVD2PMOS2, DistanceBtwVDD2PMOS3, DistanceBtwVDD2PMOS4)

        elif DesignParameters._Technology == 'TSMC65nm':
            DistanceBtwVSS2NMOS_minimum = 0.5 * self.getYWidth('PbodyContact', '_PPLayer') + 0.5 * self.getYWidth('_NMOS', '_NPLayer')
            DistanceBtwVDD2PMOS_minimum = 0.5 * self.getYWidth('_PMOS', '_PPLayer') + 0.5 * self.getYWidth('NbodyContact', '_NPLayer')
        else:
            raise NotImplementedError

        if _VSS2NMOSHeight == None:
            DistanceBtwVSS2NMOS = DistanceBtwVSS2NMOS_minimum
        elif _VSS2NMOSHeight < DistanceBtwVSS2NMOS_minimum:
            raise Exception("Too short '_VSS2NMOSHeight'.")
        else:
            DistanceBtwVSS2NMOS = _VSS2NMOSHeight

        if _VDD2PMOSHeight == None:
            DistanceBtwVDD2PMOS = DistanceBtwVDD2PMOS_minimum
        elif _VDD2PMOSHeight < DistanceBtwVDD2PMOS_minimum:
            raise Exception("Too short '_VDD2PMOSHeight'.")
        else:
            DistanceBtwVDD2PMOS = _VDD2PMOSHeight

        # 2) Calculate Distance between 'MOSFET' and 'Input gate Contact'
        if _Finger != 1:
            if DesignParameters._Technology == 'SS28nm':
                tmp_space = _DRCObj._Metal1MinSpaceAtCorner
            else:  # only checked when 65nm
                tmp_space = _DRCObj._Metal1MinSpace

            DistanceBtwNMOS2PolyInput = 0.5 * max(
                self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) \
                                        + 0.5 * WidthOfInputXM1 \
                                        + tmp_space

            DistanceBtwPMOS2PolyInput = 0.5 * max(
                self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) \
                                        + 0.5 * WidthOfInputXM1 \
                                        + tmp_space

        else:  # Finger == 1
            XCoordinateOfViaF1 = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][0][0]

            _LengthBtwPolyDummyEdge2PolyEdge = - self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] \
                                               - 0.5*self.getXWidth('_NMOS', '_PODummyLayer') \
                                               + XCoordinateOfViaF1 \
                                               - 0.5*self.getXWidth('_VIANMOSPoly2Met1_F1', '_POLayer')

            _LengthNPolyDummytoGoUp_Finger2 = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthBtwPolyDummyEdge2PolyEdge * _LengthBtwPolyDummyEdge2PolyEdge) + 1
            _LengthPPolyDummytoGoUp_Finger2 = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthBtwPolyDummyEdge2PolyEdge * _LengthBtwPolyDummyEdge2PolyEdge) + 1

            DistanceBtwNMOS2PolyInput = \
                0.5 * self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] \
                + _LengthNPolyDummytoGoUp_Finger2 \
                + 0.5 * self._DesignParameter['_VIANMOSPoly2Met1_F1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
            DistanceBtwPMOS2PolyInput = \
                0.5 * self._DesignParameter['_VIAPMOSPoly2Met1_F1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] \
                + _LengthPPolyDummytoGoUp_Finger2 \
                + 0.5 * self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']


        # 3) Calculate Total Minimum Height of Inverter (Between Supply rails, VDD - VSS)
        if DesignParameters._Technology == 'SS28nm':
            _VDD2VSSMinHeight1 = DistanceBtwVSS2NMOS + DistanceBtwNMOS2PolyInput + DistanceBtwPMOS2PolyInput + DistanceBtwVDD2PMOS
            _VDD2VSSMinHeight2 = DistanceBtwVSS2NMOS + DistanceBtwVDD2PMOS \
                                 + 0.5 * self.getYWidth('_NMOS', '_PODummyLayer') \
                                 + 0.5 * self.getYWidth('_PMOS', '_PODummyLayer') \
                                 + _DRCObj._PolygateMinSpace
            # Add by poly dummy gate space 96
            _VDD2VSSMinHeight = max(_VDD2VSSMinHeight1, _VDD2VSSMinHeight2)

        else:  # Need to consider NP PP Layer overlapped
            # 1) Overlapped polygate of PMOS and NMOS -> PP and NP are overlapped
            _VDD2VSSMinHeight1 = DistanceBtwVSS2NMOS + DistanceBtwNMOS2PolyInput + DistanceBtwPMOS2PolyInput + DistanceBtwVDD2PMOS  # Maybe Not seletec
            # 2) calculate by PP and NP layer -> It works, but not a general design. -> Need Very Wide Poly routing and specific width M1
            _VDD2VSSMinHeight2 = DistanceBtwVSS2NMOS \
                                 + 0.5 * self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_NPLayer'][
                                     '_YWidth'] \
                                 + 0.5 * self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer'][
                                     '_YWidth'] \
                                 + DistanceBtwVDD2PMOS
            # 3)  two independant poly gates and gap by '_PolygateMinSpace2'
            _VDD2VSSMinHeight3 = DistanceBtwVSS2NMOS + DistanceBtwNMOS2PolyInput + DistanceBtwPMOS2PolyInput + DistanceBtwVDD2PMOS + WidthOfInputXM1 + _DRCObj._PolygateMinSpace2  # Need to Modify by using 'DRCPolyMinSpace' later

            _VDD2VSSMinHeight = max(_VDD2VSSMinHeight1, _VDD2VSSMinHeight2, _VDD2VSSMinHeight3)


        # 4) Determine the total height and Validate it
        if _VDD2VSSHeight == None:
            _VDD2VSSHeight = _VDD2VSSMinHeight
        else:
            if _VDD2VSSHeight < _VDD2VSSMinHeight:
                print("ERROR! VDD2VSSMinHeight =", _VDD2VSSMinHeight)  # Need to Print More information(input parameter...)
                raise NotImplementedError

        # 5) Setting Coordinates of 'SupplyLines and MOSFETs'
        self._DesignParameter['PbodyContact']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['NbodyContact']['_XYCoordinates'] = [[0, _VDD2VSSHeight]]
        self._DesignParameter['_NMOS']['_XYCoordinates'] = [[0, DistanceBtwVSS2NMOS]]
        self._DesignParameter['_PMOS']['_XYCoordinates'] = [[0, (_VDD2VSSHeight - DistanceBtwVDD2PMOS)]]

        # 6) Setting Coordinates of 'Output Routing Via (M1V1M2)'
        tmpNMOSOutputRouting, tmpPMOSOutputRouting = [], []
        for i in range(0, len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):  # Assumption : same MOSFETs' fingers
            tmpPMOSOutputRouting.append(CoordCalc.Add(
                self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i],
                self._DesignParameter['_PMOS']['_XYCoordinates'][0]))
            tmpNMOSOutputRouting.append(CoordCalc.Add(
                self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i],
                self._DesignParameter['_NMOS']['_XYCoordinates'][0]))

        self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'] = tmpPMOSOutputRouting
        self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'] = tmpNMOSOutputRouting


        ''' VSS & VDD Supply Routing (Metal1) ---------------------------------------------------------------------- '''
        '''
            Function : Route 'VDD-PMOS(source)' and 'VSS-NMOS(source)' by 'METAL1'
                       (Set the Leftmost Metal of MOSFET as the source)
            Require  : NMOS, PMOS, NbodyContact, PbodyContact (Coordinates)
        '''

        tmpPathForSupplyRoutingOnPMOS, tmpPathForSupplyRoutingOnNMOS = [], []
        for XYs in self.getXY('_NMOS', '_XYCoordinateNMOSSupplyRouting'):
            tmpPathForSupplyRoutingOnNMOS.append([
                [XYs[0], XYs[1] + self.getYWidth('_NMOS', '_Met1Layer') / 2],
                [XYs[0], self.getXY('PbodyContact')[0][1]]
            ])
        for XYs in self.getXY('_PMOS', '_XYCoordinatePMOSSupplyRouting'):
            tmpPathForSupplyRoutingOnPMOS.append([
                [XYs[0], XYs[1] - self.getYWidth('_PMOS', '_Met1Layer') / 2],
                [XYs[0], self.getXY('NbodyContact')[0][1]]
            ])

        self._DesignParameter['_NMOSSupplyRouting'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _Width=self.getXWidth('_NMOS', '_Met1Layer'),
            _XYCoordinates=tmpPathForSupplyRoutingOnNMOS
        )

        self._DesignParameter['_PMOSSupplyRouting'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _Width=self.getXWidth('_PMOS', '_Met1Layer'),
            _XYCoordinates=tmpPathForSupplyRoutingOnPMOS
        )



        #####################################VIA re-Coordinates for Poly Dummy######################################
        # Need to Modify
        if (_Finger == 1) and (DesignParameters._Technology == 'SS28nm'):
            self._DesignParameter['_VIANMOSPoly2Met1_F1']['_XYCoordinates'] = [
                [XCoordinateOfViaF1,  # self._DesignParameter['_NMOS']['_XYCoordinates'][0][0],
                 self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] +
                 self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 +
                 self._DesignParameter['_VIANMOSPoly2Met1_F1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyDummytoGoUp_Finger2]]
            self._DesignParameter['_VIAPMOSPoly2Met1_F1']['_XYCoordinates'] = [
                [XCoordinateOfViaF1,  # self._DesignParameter['_PMOS']['_XYCoordinates'][0][0],
                 self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] -
                 self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 -
                 self._DesignParameter['_VIAPMOSPoly2Met1_F1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 - _LengthPPolyDummytoGoUp_Finger2]]
        elif (_Finger == 1) and (DesignParameters._Technology == 'TSMC65nm'):
            raise NotImplementedError
        elif DesignParameters._Technology not in ('SS28nm', 'TSMC65nm'):
            raise NotImplementedError
        else:
            pass

        # Poly Boundary Generation MOS Gate -----------------------------------------------------------------------
        '''
        Require : PMOS, NMOS
        '''
        if _Finger != 1:
            _LenBtwPMOSGates = \
                self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] \
                - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0] \
                + _ChannelLength
            _LenBtwNMOSGates = \
                self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] \
                - self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0] \
                + _ChannelLength

        else:
            _LenBtwPMOSGates = abs(self.getXY('_VIAPMOSPoly2Met1_F1')[0][0] - self.getXY('_PMOS', '_XYCoordinatePMOSGateRouting')[0][0]) \
                               + self.getXWidth('_VIAPMOSPoly2Met1_F1', '_POLayer') / 2 \
                               + self.getXWidth('_PMOS', '_POLayer') / 2
            _LenBtwNMOSGates = abs(self.getXY('_VIANMOSPoly2Met1_F1')[0][0] - self.getXY('_NMOS', '_XYCoordinateNMOSGateRouting')[0][0]) \
                               + self.getXWidth('_VIANMOSPoly2Met1_F1', '_POLayer') / 2 \
                               + self.getXWidth('_NMOS', '_POLayer') / 2

        self._DesignParameter['_PolyRouteXOnPMOS'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1])
        self._DesignParameter['_PolyRouteXOnNMOS'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1])
        self._DesignParameter['_PolyRouteXOnPMOS']['_XWidth'] = _LenBtwPMOSGates
        self._DesignParameter['_PolyRouteXOnNMOS']['_XWidth'] = _LenBtwNMOSGates
        self._DesignParameter['_PolyRouteXOnPMOS']['_YWidth'] = _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByPOAtLeastTwoSide  # calculated when only one row -> should be changed
        self._DesignParameter['_PolyRouteXOnNMOS']['_YWidth'] = _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByPOAtLeastTwoSide

        # Additional Poly Routing --------------------------------------------------------------------------------------
        '''
        Function : Route poly layers [ {Input gate poly left - Input gate poly right(row)}, {NMOS gate poly - Input M1 poly(column)}, {PMOS gate poly - Input M1 poly(column)} ]
        Output   : Update self._DesignParameter['_PolyRouteXOn{PMOS, NMOS}'] & self._DesignParameter['_PolyRouteYOn{PMOS, NMOS}'] 
        Require  : NMOS, PMOS (XYCoordinates)
        '''
        # Row Line (Only setting Coordinates)
        if _Finger != 1:
            self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'] = [
                [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0],
                 self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + DistanceBtwNMOS2PolyInput]
            ]

            self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'] = [
                [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0],
                 self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - DistanceBtwPMOS2PolyInput]
            ]
        else:
            self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'] = [
                [self.getXY('_NMOS', '_POLayer')[0][0] + _ChannelLength / 2 - _LenBtwNMOSGates / 2,
                 self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + DistanceBtwNMOS2PolyInput]
            ]

            self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'] = [
                [self.getXY('_PMOS', '_POLayer')[0][0] + _ChannelLength / 2 - _LenBtwPMOSGates / 2,
                 self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - DistanceBtwPMOS2PolyInput]
            ]

        # Column Line
        self._DesignParameter['_PolyRouteYOnPMOS'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1])
        self._DesignParameter['_PolyRouteYOnNMOS'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1])
        self._DesignParameter['_PolyRouteYOnPMOS']['_Width'] = _ChannelLength
        self._DesignParameter['_PolyRouteYOnNMOS']['_Width'] = _ChannelLength

        tmpPolyRouteYOnPMOS, tmpPolyRouteYOnNMOS = [], []
        for i in range(0, len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])):
            tmpPolyRouteYOnPMOS.append([[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] +
                                         self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0],
                                         self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] +
                                         self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][1]],
                                        [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] +
                                         self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0],
                                         self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'][0][1] + self.getYWidth('_PolyRouteXOnPMOS') / 2]
                                        ])
            tmpPolyRouteYOnNMOS.append([[self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] +
                                         self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0],
                                         self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] +
                                         self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][1]],
                                        [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] +
                                         self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0],
                                         self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][1] - self.getYWidth('_PolyRouteXOnPMOS') / 2]
                                        ])

        self._DesignParameter['_PolyRouteYOnPMOS']['_XYCoordinates'] = tmpPolyRouteYOnPMOS
        self._DesignParameter['_PolyRouteYOnNMOS']['_XYCoordinates'] = tmpPolyRouteYOnNMOS



        # Output Metal (1&2) Boundary & Routing ------------------------------------------------------------------------

        # Output M1 Routing (Column Line)
        tmpOutputRoutingM1Y = []
        for i in range(0, (len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']) + 1) // 2):
            tmpOutputRoutingM1Y.append([CoordCalc.Add(self.getXY('_PMOS', '_XYCoordinatePMOSOutputRouting')[2 * i], [0, +self.getYWidth('_PMOS', '_Met1Layer')/2]),
                                        CoordCalc.Add(self.getXY('_NMOS', '_XYCoordinateNMOSOutputRouting')[2 * i], [0, -self.getYWidth('_NMOS', '_Met1Layer')/2])
                                        ])  #

        if (_Finger % 4 == 2) and (_Finger != 2):  # exception case (6, 10, 14, 18, ...)
            del tmpOutputRoutingM1Y[-1]
            tmpOutputRoutingM1Y.append(
                [CoordCalc.Add(self._DesignParameter['_PMOS']['_XYCoordinates'][0],
                               self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter[
                                   '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1]),
                 CoordCalc.Add(self._DesignParameter['_NMOS']['_XYCoordinates'][0],
                               self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter[
                                   '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1])])
        else:
            pass

        self._DesignParameter['_OutputRouting'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1])
        # self._DesignParameter['_OutputRouting']['_Width'] = _DRCObj._Metal1MinWidth           # Need to Modify
        self._DesignParameter['_OutputRouting']['_Width'] = self.getXWidth('_ViaMet12Met2OnNMOSOutput', '_Met1Layer')
        self._DesignParameter['_OutputRouting']['_XYCoordinates'] = tmpOutputRoutingM1Y

        if _Finger == 1:
            del self._DesignParameter['_ViaMet12Met2OnNMOSOutput']
            del self._DesignParameter['_ViaMet12Met2OnPMOSOutput']

        # Output M2 Routing (Row Line)
        self._DesignParameter['_Met2OnOutput'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1])
        # self._DesignParameter['_Met2OnOutput']['_Width'] = _DRCObj._MetalxMinWidth  # Need to Modify
        self._DesignParameter['_Met2OnOutput']['_Width'] = _DRCObj._VIAxMinWidth + 2 * _DRCObj._MetalxMinEnclosureVia3
        self._DesignParameter['_Met2OnOutput']['_XYCoordinates'] = \
            [[CoordCalc.getXYCoords_MaxX(self.getXY('_PMOS', '_XYCoordinatePMOSOutputRouting'))[0],
              CoordCalc.getXYCoords_MinX(self.getXY('_PMOS', '_XYCoordinatePMOSOutputRouting'))[0]],
             [CoordCalc.getXYCoords_MaxX(self.getXY('_NMOS', '_XYCoordinateNMOSOutputRouting'))[0],
              CoordCalc.getXYCoords_MinX(self.getXY('_NMOS', '_XYCoordinateNMOSOutputRouting'))[0]]]

        # Input Contact (Poly to M1)------------------------------------------------------------------------------------
        '''
        Function : Make Contact(Poly to M1) for _PolyRouteXOn{}
                   2 kind of calculation
                   (1) surrounded by output metal(left and right)   if _Finger > 4
                   (2) rightmost 
        Require : OutputRouting, _PolyRouteXOn{NMOS PMOS}, PMOS, NMOS

        '''
        # (0)
        _VIATempPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        _VIATempPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = 3
        _VIATempPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = 1
        self._DesignParameter['_VIATempPoly2Met1'] = self._SrefElementDeclaration(
            _DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='ViaPoly2Met1_TempIn{}'.format(_Name)))[0]
        self._DesignParameter['_VIATempPoly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
            **_VIATempPoly2Met1)

        distance_input = self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'][0][1] - \
                         self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][1]
        distance_contact = distance_input - \
                           self._DesignParameter['_VIATempPoly2Met1']['_DesignObj']._DesignParameter['_COLayer'][
                               '_YWidth']
        distance_poly = distance_input - max(self._DesignParameter['_PolyRouteXOnPMOS']['_YWidth'],
                                             self._DesignParameter['_VIATempPoly2Met1']['_DesignObj']._DesignParameter[
                                                 '_POLayer']['_YWidth'])
        distance_metal1 = distance_input - \
                          self._DesignParameter['_VIATempPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer'][
                              '_YWidth']

        flag_poly = True if distance_poly < _DRCObj.DRCPolyMinSpace(
            _Width=self._DesignParameter['_PolyRouteXOnPMOS']['_XWidth'],
            _ParallelLength=self._DesignParameter['_PolyRouteXOnPMOS']['_YWidth']) else False
        flag_metal = True if distance_metal1 < _DRCObj._Metal1MinSpace else False
        flag_contact = True if distance_contact < _DRCObj._CoMinSpace else False
        if (not flag_contact) and (not flag_metal) and (not flag_poly):
            flag_horizontal_inputvia_PCCOM1 = False
            Average2Up, Average2Dn = 0, 0
        else:
            flag_horizontal_inputvia_PCCOM1 = True
            Average2Up = self.CeilMinSnapSpacing(float(distance_input) / 2.0, _DRCObj._MinSnapSpacing)
            Average2Dn = distance_input - Average2Up

            self._DesignParameter['_PolyRouteXOnMOS'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1])
            self._DesignParameter['_PolyRouteXOnMOS']['_XWidth'] = self._DesignParameter['_PolyRouteXOnPMOS']['_XWidth']
            self._DesignParameter['_PolyRouteXOnMOS']['_YWidth'] = self.RounddownMinSnapSpacing(
                distance_input + self._DesignParameter['_PolyRouteXOnPMOS']['_YWidth'], 2 * _DRCObj._MinSnapSpacing)
            self._DesignParameter['_PolyRouteXOnMOS']['_XYCoordinates'] = [
                CoordCalc.Add(self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0],
                              [0, Average2Up])]

        # (1) surrounded by output metal  /  of Input Contact (Poly to M1)
        if _Finger > 4:  # No Need else statement (when finger is 1, 2, 3, it covers on (2))
            ''' ************************ temporal DRC... Need 2 Modify Later ************************ '''
            if DesignParameters._Technology == 'SS28nm':
                _tmpDRC_Metal1MinSpaceAtCorner = 70
                # _tmpDRC_Metal1MinSpaceAtCorner = _DRCObj._Metal1MinSpaceAtCorner
            else:
                _tmpDRC_Metal1MinSpaceAtCorner = _DRCObj._Metal1MinSpaceAtCorner

            # Calculate Number of Contact_X 'tmpNumCOX'
            lengthM1BtwOutputRouting = self._DesignParameter['_OutputRouting']['_XYCoordinates'][1][0][0] \
                                       - self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][0] \
                                       - self._DesignParameter['_OutputRouting']['_Width'] \
                                       - 2 * _tmpDRC_Metal1MinSpaceAtCorner

            unitLengthBtwCOX = _DRCObj._CoMinWidth + _DRCObj._CoMinSpace
            tmpNumCOX = int((
                                        lengthM1BtwOutputRouting - _DRCObj._CoMinWidth - 2 * _DRCObj._Metal1MinEnclosureCO2) // unitLengthBtwCOX) + 1

            # NMOS & PMOS
            _VIANMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
            _VIAPMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
            _VIANMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = tmpNumCOX
            _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = tmpNumCOX
            _VIANMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = 1
            _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = 1

            self._DesignParameter['_VIANMOSPoly2Met1'] = self._SrefElementDeclaration(
                _DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='ViaPoly2Met1OnNMOSGateIn{}'.format(_Name)))[0]
            self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
                **_VIANMOSPoly2Met1)
            self._DesignParameter['_VIAPMOSPoly2Met1'] = self._SrefElementDeclaration(
                _DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='ViaPoly2Met1OnPMOSGateIn{}'.format(_Name)))[0]
            self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
                **_VIAPMOSPoly2Met1)

            tmpInputPCCOM1onNMOS, tmpInputPCCOM1onPMOS = [], []
            for i in range(0, len(self._DesignParameter['_OutputRouting']['_XYCoordinates']) - 1):
                tmpInputPCCOM1onNMOS.append(
                    [self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][2 * i + 1][0],
                     self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][1] + Average2Up])
                tmpInputPCCOM1onPMOS.append(
                    [self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'][2 * i + 1][0],
                     self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'][0][1] - Average2Dn])

            self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'] = tmpInputPCCOM1onNMOS
            self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'] = tmpInputPCCOM1onPMOS

            # exception case
            if (_Finger % 4 == 2) and (_Finger != 2):
                del self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'][-1]
                del self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][-1]

        ## (2) rightmost output metal  /  of Input Contact (Poly to M1)
        if (_Finger % 4 == 2) and (_Finger != 2):  # exception case
            tmpLeftM1Boundary = self._DesignParameter['_OutputRouting']['_XYCoordinates'][-2][0][0] \
                                + 0.5 * self._DesignParameter['_OutputRouting']['_Width'] \
                                + _DRCObj._Metal1MinSpaceAtCorner
            tmpRightM1Boundary = self._DesignParameter['_OutputRouting']['_XYCoordinates'][-1][0][0] \
                                 - 0.5 * self._DesignParameter['_OutputRouting']['_Width'] \
                                 - _DRCObj._Metal1MinSpaceAtCorner
            tmpLeftCoBoundary = tmpLeftM1Boundary + _DRCObj._Metal1MinEnclosureCO2  # Calculate by M1-CO
            tmpRightCoBoundary = tmpRightM1Boundary - _DRCObj._Metal1MinEnclosureCO2  # Calculate by M1-CO
        elif _Finger != 1:
            tmpLeftM1Boundary = self._DesignParameter['_OutputRouting']['_XYCoordinates'][-1][0][0] \
                                + 0.5 * self._DesignParameter['_OutputRouting']['_Width'] \
                                + _DRCObj._Metal1MinSpaceAtCorner
            tmpRightPOBoundary = \
            self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][0] \
            + 0.5 * _ChannelLength
            tmpLeftCoBoundary = tmpLeftM1Boundary + _DRCObj._Metal1MinEnclosureCO2  # Calculate by M1-CO
            tmpRightCoBoundary = tmpRightPOBoundary - _DRCObj._CoMinEnclosureByPOAtLeastTwoSide  # Calculate by PO-CO
        elif (_Finger == 1) and (DesignParameters._Technology == 'SS28nm'):
            tmpLeftCoBoundary = 0
            tmpRightCoBoundary = 0
        else:
            raise NotImplementedError

        NumCoRightMost = int((tmpRightCoBoundary - tmpLeftCoBoundary - _DRCObj._CoMinWidth) // (
                    _DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 1

        if NumCoRightMost > 0:
            _VIAMOSPoly2Met1RightMost = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)

            _VIAMOSPoly2Met1RightMost['_ViaPoly2Met1NumberOfCOX'] = NumCoRightMost
            _VIAMOSPoly2Met1RightMost['_ViaPoly2Met1NumberOfCOY'] = 1

            self._DesignParameter['_VIAMOSPoly2Met1RightMost'] = self._SrefElementDeclaration(
                _DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='ViaPoly2Met1RightMostOnNMOSGateIn{}'.format(_Name)))[0]
            self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
                **_VIAMOSPoly2Met1RightMost)
            self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_XYCoordinates'] = [
                [self.RounddownMinSnapSpacing((tmpLeftCoBoundary + tmpRightCoBoundary) / 2, MinSnapSpacing),
                 self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][1] + Average2Up],
                [self.RounddownMinSnapSpacing((tmpLeftCoBoundary + tmpRightCoBoundary) / 2, MinSnapSpacing),
                 self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'][0][1] - Average2Dn]
            ]  # both NMOS & PMOS

        if '_VIAPMOSPoly2Met1_F1' in self._DesignParameter:
            self._DesignParameter['_VIANMOSPoly2Met1'] = self._DesignParameter['_VIANMOSPoly2Met1_F1']
            self._DesignParameter['_VIAPMOSPoly2Met1'] = self._DesignParameter['_VIAPMOSPoly2Met1_F1']
            del self._DesignParameter['_VIANMOSPoly2Met1_F1']
            del self._DesignParameter['_VIAPMOSPoly2Met1_F1']

        # Input Met1 Routing -------------------------------------------------------------------------------------------
        '''
        When there is a gap between (routed) poly gates, route them by Met1 (column line)
        Strategy : Route Input M1 on the same YCoordinates as the SupplyRouting M1
                   (Supply M1 outside the poly gate route is ignored)
        '''
        tmpInputRouting = []  # if list is appended twice, tmp=[ [[1,2],[3,4]], [[5,6],[7,8]] ]
        if '_VIANMOSPoly2Met1' in self._DesignParameter:
            for i in range(0, len(self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'])):
                tmpInputRouting.append([self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'][i],
                                        self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][i]])
        if '_VIAMOSPoly2Met1RightMost' in self._DesignParameter:
            tmpInputRouting.append(self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_XYCoordinates'])

        self._DesignParameter['_InputRouting'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1])
        # self._DesignParameter['_InputRouting']['_Width'] = _DRCObj._Metal1MinWidth
        self._DesignParameter['_InputRouting']['_Width'] = _DRCObj._VIAxMinWidth + 2 * _DRCObj._Metal1MinEnclosureVia3
        self._DesignParameter['_InputRouting']['_XYCoordinates'] = tmpInputRouting

        ################################################################################################################
        # # Input M1 Route up tp M2
        if DesignParameters._Technology in ('SS28nm', 'TSMC65nm'):
            # count input M1 segment
            tmpCount_GateViaLayer = 0

            if '_VIAMOSPoly2Met1RightMost' in self._DesignParameter:
                tmpCount_GateViaLayer += 1
                flag_exception_rightmost = True
            else:
                flag_exception_rightmost = False
            if '_VIAPMOSPoly2Met1' in self._DesignParameter:
                tmpCount_GateViaLayer += len(self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'])

            if (DesignParameters._Technology == 'SS28nm') and (tmpCount_GateViaLayer > 1) and flag_horizontal_inputvia_PCCOM1:
                # M1V1M2
                # (1) Normal width
                _LengthM1_VIAPMOSPoly2Met1 = self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
                _NumViaInputM12 = int((_LengthM1_VIAPMOSPoly2Met1 - _DRCObj._VIAxMinWidth - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide)
                                      // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

                _ViaMet12Met2forInput = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
                _ViaMet12Met2forInput['_ViaMet12Met2NumberOfCOX'] = _NumViaInputM12
                _ViaMet12Met2forInput['_ViaMet12Met2NumberOfCOY'] = 1
                self._DesignParameter['_ViaMet12Met2forInput'] = self._SrefElementDeclaration(
                    _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='ViaMet12Met2forInputIn{}'.format(_Name)))[0]
                self._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._CalculateDesignParameterSameEnclosure(**_ViaMet12Met2forInput)

                # (2) RightMost
                if flag_exception_rightmost:
                    _LengthM1_VIAPMOSPoly2Met1_RightMost = self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
                    _NumViaInputM12_RightMost = int((_LengthM1_VIAPMOSPoly2Met1_RightMost - _DRCObj._VIAxMinWidth - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide)
                                                    // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

                    _ViaMet12Met2forInput2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
                    _ViaMet12Met2forInput2['_ViaMet12Met2NumberOfCOX'] = _NumViaInputM12_RightMost
                    _ViaMet12Met2forInput2['_ViaMet12Met2NumberOfCOY'] = 1
                    self._DesignParameter['_ViaMet12Met2forInput2'] = self._SrefElementDeclaration(
                        _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='ViaMet12Met2forInput2In{}'.format(_Name)))[0]
                    self._DesignParameter['_ViaMet12Met2forInput2']['_DesignObj']._CalculateDesignParameterSameEnclosure(**_ViaMet12Met2forInput2)

                tmpXYs = []
                for i in range(0, len(self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'])):
                    tmpXYs.append([self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] +
                                   self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][i][0],
                                   self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][1]])
                self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'] = tmpXYs

                if flag_exception_rightmost:
                    self._DesignParameter['_ViaMet12Met2forInput2']['_XYCoordinates'] = \
                        [[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] +
                          self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_XYCoordinates'][0][0],
                          self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][1]]]

                self._DesignParameter['_CLKMet2InRouting'] = self._PathElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['METAL2'][0],
                    _Datatype=DesignParameters._LayerMapping['METAL2'][1])
                self._DesignParameter['_CLKMet2InRouting']['_Width'] = self._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
                self._DesignParameter['_CLKMet2InRouting']['_XYCoordinates'] = [
                    [self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'][0],
                     self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'][-1]]]
                if flag_exception_rightmost:
                    self._DesignParameter['_CLKMet2InRouting']['_XYCoordinates'] = [
                        [self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'][0],
                         self._DesignParameter['_ViaMet12Met2forInput2']['_XYCoordinates'][0]]]

            elif (DesignParameters._Technology in ('SS28nm', 'TSMC65nm')) and (tmpCount_GateViaLayer > 1):
                # M1V1M2
                # (1) Normal width
                _LengthM1Y_VIAMOSPoly2Met1 = \
                self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
                + abs(self._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][1] -
                      self._DesignParameter['_InputRouting']['_XYCoordinates'][0][1][1])
                _NumViaInputM12 = int((_LengthM1Y_VIAMOSPoly2Met1 - _DRCObj._VIAxMinWidth - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide)
                                      // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

                _ViaMet12Met2forInput = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
                _ViaMet12Met2forInput['_ViaMet12Met2NumberOfCOX'] = 1
                _ViaMet12Met2forInput['_ViaMet12Met2NumberOfCOY'] = _NumViaInputM12 if _NumViaInputM12 < 3 else 3
                self._DesignParameter['_ViaMet12Met2forInput'] = self._SrefElementDeclaration(
                    _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='ViaMet12Met2forInputIn{}'.format(_Name)))[0]
                self._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._CalculateDesignParameterSameEnclosure(**_ViaMet12Met2forInput)

                tmpXYs = []
                for i in range(0, len(self._DesignParameter['_InputRouting']['_XYCoordinates'])):
                    tmpXYs.append([self._DesignParameter['_InputRouting']['_XYCoordinates'][i][0][0],
                                   (self._DesignParameter['_InputRouting']['_XYCoordinates'][i][0][1] +
                                    self._DesignParameter['_InputRouting']['_XYCoordinates'][i][1][1]) / 2])
                self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'] = tmpXYs

                self._DesignParameter['_CLKMet2InRouting'] = self._PathElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1])
                # self._DesignParameter['_CLKMet2InRouting']['_Width'] = _DRCObj._MetalxMinWidth
                self._DesignParameter['_CLKMet2InRouting']['_Width'] = _DRCObj._VIAxMinWidth + 2 * _DRCObj._Metal1MinEnclosureVia3
                self._DesignParameter['_CLKMet2InRouting']['_XYCoordinates'] = [
                    # [CoordCalc.Add(self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'][0], [0, -self.getXWidth('_ViaMet12Met2forInput', '_Met2Layer')]),
                    #  CoordCalc.Add(self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'][-1], [0, self.getXWidth('_ViaMet12Met2forInput', '_Met2Layer')])]]
                    [self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'][0],
                     self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'][-1]]
                ]

        # end of 'if _VDD2VSSHeight == _VDD2VSSMinHeight:'

        # exception case... Need to Modify later...... Not tested in 65nm
        if DesignParameters._Technology == 'SS28nm':
            _DRC_M1MinWidth_WhenCalcMinArea = 130

            if (_Finger == 1) and (_VDD2VSSHeight == _VDD2VSSMinHeight):
                tmpX = self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
                tmpY = self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
                if (tmpX * tmpY) < _DRCObj._Metal1MinArea:
                    tmpY_calc = self.CeilMinSnapSpacing(_DRCObj._Metal1MinArea / tmpX, MinSnapSpacing)
                    if tmpY_calc < _DRC_M1MinWidth_WhenCalcMinArea:  # Rule by samsung28nm GR501aSE only for 28nm...
                        tmpY_calc = _DRC_M1MinWidth_WhenCalcMinArea

                    self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = tmpY_calc

            elif (_Finger == 2) and (_VDD2VSSHeight == _VDD2VSSMinHeight):
                tmpX = self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
                tmpY = self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
                if (tmpX * tmpY) < _DRCObj._Metal1MinArea:
                    tmpX_calc = self.CeilMinSnapSpacing(_DRCObj._Metal1MinArea / tmpY, MinSnapSpacing)
                    if tmpX_calc < _DRC_M1MinWidth_WhenCalcMinArea:  # Rule by samsung28nm GR501aSE only for 28nm...
                        tmpX_calc = _DRC_M1MinWidth_WhenCalcMinArea
                    self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = tmpX_calc
                    self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] = \
                        self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] \
                        + tmpX_calc / 2 - tmpX / 2

        """ Routing Finished / Next : Additional Layers """

        ''' ---------------------------------------- PP/NP Additional Layer ---------------------------------------- '''
        if DesignParameters._Technology == 'TSMC65nm':
            Ybot_PolyRouteXOnPMOS = self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'][0][1] - 0.5 * \
                                    self._DesignParameter['_PolyRouteXOnPMOS']['_YWidth']
            Ytop_PolyRouteXOnNMOS = self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][1] + 0.5 * \
                                    self._DesignParameter['_PolyRouteXOnNMOS']['_YWidth']

            # case 1) Enlarge each PP/NP Layers
            if abs(Ybot_PolyRouteXOnPMOS - Ytop_PolyRouteXOnNMOS) >= 2 * _DRCObj._PpMinEnclosureOfPo:
                self._DesignParameter['_PIMPforGatePoly'] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['PIMP'][0],
                    _Datatype=DesignParameters._LayerMapping['PIMP'][1])
                self._DesignParameter['_NIMPforGatePoly'] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['NIMP'][0],
                    _Datatype=DesignParameters._LayerMapping['NIMP'][1])

                self._DesignParameter['_PIMPforGatePoly']['_XYCoordinates'] = \
                self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates']
                self._DesignParameter['_NIMPforGatePoly']['_XYCoordinates'] = \
                self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates']
                self._DesignParameter['_PIMPforGatePoly']['_XWidth'] = \
                self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']
                self._DesignParameter['_NIMPforGatePoly']['_XWidth'] = \
                self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']
                self._DesignParameter['_PIMPforGatePoly']['_YWidth'] = self._DesignParameter['_PolyRouteXOnPMOS'][
                                                                           '_YWidth'] + 2 * _DRCObj._PpMinEnclosureOfPo
                self._DesignParameter['_NIMPforGatePoly']['_YWidth'] = self._DesignParameter['_PolyRouteXOnNMOS'][
                                                                           '_YWidth'] + 2 * _DRCObj._PpMinEnclosureOfPo

            # case 2) Fill the gap between PP&NP Layer with only NP Layer
            else:
                Ybot_PPLayerOnPMOS = self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - 0.5 * \
                                     self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']
                Ytop_NPLayerOnNMOS = self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + 0.5 * \
                                     self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']

                self._DesignParameter['_NIMPforGatePoly'] = self._PathElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['NIMP'][0],
                    _Datatype=DesignParameters._LayerMapping['NIMP'][1])
                self._DesignParameter['_NIMPforGatePoly']['_Width'] = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']
                self._DesignParameter['_NIMPforGatePoly']['_XYCoordinates'] = [
                    [[self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][0], Ybot_PPLayerOnPMOS],
                     [self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][0], Ytop_NPLayerOnNMOS]]]
        elif DesignParameters._Technology == 'SS28nm':
            pass
        else:
            raise NotImplementedError

        ''' ------------------------------------------- NWELL Generation ------------------------------------------- '''
        '''
        Function    : Generate NWELL by PathElementDeclaration (column line)
        Requirement : NbodyContact(ODLayer), _PMOS(ODLayer)
        '''
        XWidth1_NWLayer = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._NwMinEnclosurePactive
        XWidth2_NWLayer = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._NwMinEnclosurePactive2
        XWidth_NWLayer = max(XWidth1_NWLayer, XWidth2_NWLayer)

        XYCoordinatesOfNW_top = CoordCalc.Add(self._DesignParameter['NbodyContact']['_XYCoordinates'][0],
                                              [0, self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2 + _DRCObj._NwMinEnclosurePactive])
        XYCoordinatesOfNW_bot = CoordCalc.Add(self._DesignParameter['_PMOS']['_XYCoordinates'][0],
                                              [0, -self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2 - _DRCObj._NwMinEnclosurePactive])
        YWidth_NWLayer = abs(XYCoordinatesOfNW_top[1] - XYCoordinatesOfNW_bot[1])

        if (XWidth_NWLayer * YWidth_NWLayer) < _DRCObj._NwMinArea:
            XWidth_NWLayer = self.CeilMinSnapSpacing(_DRCObj._NwMinArea / YWidth_NWLayer, 2 * MinSnapSpacing)
        else:
            pass

        self._DesignParameter['_NWLayer'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1])
        self._DesignParameter['_NWLayer']['_Width'] = XWidth_NWLayer
        self._DesignParameter['_NWLayer']['_XYCoordinates'] = [[XYCoordinatesOfNW_top, XYCoordinatesOfNW_bot]]

        ''' ----------------------------------------  XVT Layer Modification --------------------------------------- '''
        if DesignParameters._Technology == 'SS28nm':
            assert _XVT in ('SLVT', 'LVT', 'RVT', 'HVT')

            self._DesignParameter['XVTLayer'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping[_XVT][0], _Datatype=DesignParameters._LayerMapping[_XVT][1])
            self._DesignParameter['XVTLayer']['_XWidth'] = (_GateSpacing + _ChannelLength) * (_Finger + 1)
            self._DesignParameter['XVTLayer']['_YWidth'] = _VDD2VSSHeight
            self._DesignParameter['XVTLayer']['_XYCoordinates'] = [[0, _VDD2VSSHeight/2]]

        elif DesignParameters._Technology == 'TSMC65nm':
            pass  # No Need to Modify XVT Layer
        else:
            raise NotImplementedError

        # ''' -------------------------------------  Pin Generation & Coordinates ------------------------------------ '''
        # self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
        #     _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.04, _Angle=0, _TEXT='VSS')
        #
        # self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
        #     _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.04, _Angle=0, _TEXT='VDD')
        #
        # self._DesignParameter['_Inputpin'] = self._TextElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
        #     _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.01, _Angle=0, _TEXT='A')
        #
        # self._DesignParameter['_Outputpin'] = self._TextElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
        #     _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.01, _Angle=0, _TEXT='Y')
        #
        # self._DesignParameter['_VSSpin']['_XYCoordinates'] = [[0, 0]]
        # self._DesignParameter['_VDDpin']['_XYCoordinates'] = [[0, _VDD2VSSHeight]]
        # self._DesignParameter['_Inputpin']['_XYCoordinates'] = [
        #     [round((self._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][0] +
        #             self._DesignParameter['_InputRouting']['_XYCoordinates'][0][1][0]) / 2),
        #      round((self._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][1] +
        #             self._DesignParameter['_InputRouting']['_XYCoordinates'][0][1][1]) / 2)]
        # ]
        # self._DesignParameter['_Outputpin']['_XYCoordinates'] = [
        #     [round((self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][0] +
        #             self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][1][0]) / 2),
        #      self._DesignParameter['_Inputpin']['_XYCoordinates'][0][1]]
        # ]


        print(''.center(105, '#'))
        print('     {} Calculation End     '.format(_Name).center(105, '#'))
        print(''.center(105, '#'))
