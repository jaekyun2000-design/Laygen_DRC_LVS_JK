import math
import copy

from generatorLib import StickDiagram
from generatorLib import DesignParameters
from generatorLib import DRC

from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import NbodyContact
from generatorLib.generator_models import PbodyContact
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import Z_PWR_CNT
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaMet22Met3
from generatorLib.generator_models import SupplyRails
from generatorLib.generator_models import Z_PWR_CNT
from generatorLib.generator_models import Summer_upper

class _Summer_middle(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_Finger1=None,_Finger2=None,_Finger3=None,_Finger4=None,_Finger5 =None,_Finger6 =None,_ChannelWidth=None,_NPRatio=None,_ChannelLength=None,_Dummy=None,_XVT=None,
                                      _NumberOfPbodyCOY=None,_GateSpacing=None,_SDWidth=None,_SupplyRailType=1,_SupplyMet1XWidth=None,_SupplyMet1YWidth=None)

    def __init__(self, _DesignParameter=None, _Name='Summer_middle'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _ODLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                          _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                          _XYCoordinates=[],_XWidth=400, _YWidth=400),  # boundary type:1, #path type:2, #sref type: 3, #gds data type: 4, #Design Name data type: 5,  #other data type: ?
                _ODLayerPINDrawing=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['RXPIN'][0],
                                                                    _Datatype=DesignParameters._LayerMapping['RXPIN'][1],
                                                                    _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _POLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                          _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                          _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _POLayerPINDrawing=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PCPIN'][0],
                                                                    _Datatype=DesignParameters._LayerMapping['PCPIN'][1],
                                                                    _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _Met1Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                            _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _Met2Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                            _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _Met3Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                            _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _METAL1PINDrawing=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['M1PIN'][0],
                                                                   _Datatype=DesignParameters._LayerMapping['M1PIN'][1],
                                                                   _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _PPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                          _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                          _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0],
                                                          _Datatype=DesignParameters._LayerMapping['CONT'][1],
                                                          _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                _XYCoordinatePMOSSupplyRouting=dict(_DesignParametertype=7,_XYCoordinates=[]),
                _XYCoordinatePMOSOutputRouting=dict(_DesignParametertype=7,_XYCoordinates=[]),
                _XYCoordinatePMOSGateRouting=dict(_DesignParametertype=7,_XYCoordinates=[]),
                # DistanceXBtwPoly=self._SizeInfoDeclaration(_DesignSizesInList=None)
            )


    def _CalculateDesignParameter(self,
                                  # _Finger1=12,_Finger2=8,_Finger3=14,_ChannelWidth=500,_NPRatio=1,_ChannelLength=30,_Dummy=None,_XVT='LVT',
                                  #     _GateSpacing=None,_SDWidth=None,_SupplyRailType=1,_SupplyMet1XWidth=None,_SupplyMet1YWidth=None
        _Finger1=12,_Finger2=8,_Finger3=14,_Finger4=8,_Finger5 =16,_Finger6= 6,_ChannelWidth=500,_NPRatio=1,_ChannelLength=30,_NumberOfPbodyCOY=3,_Dummy=None,_XVT='LVT',
                                      _GateSpacing=None,_SDWidth=None,_SupplyRailType=1,_SupplyMet1XWidth=None,_SupplyMet1YWidth=None
                                      ):

        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        MinSnapSpacing = _DRCObj._MinSnapSpacing
        _LengthPMOSBtwPO = _DRCObj.DRCPolygateMinSpace(_DRCObj.DRCPolyMinSpace(_Width=_ChannelWidth, _ParallelLength=_ChannelLength)) + _ChannelLength

        ################################### NMOS Genteration #########################################################

        # NMOSparameters1 = copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation)
        # NMOSparameters1['_NMOSNumberofGate'] = _Finger1
        # NMOSparameters1['_NMOSChannelWidth'] = round(_ChannelWidth * _NPRatio)
        # NMOSparameters1['_NMOSChannellength'] = _ChannelLength
        # NMOSparameters1['_NMOSDummy'] = _Dummy
        # NMOSparameters1['_XVT'] = _XVT
        # NMOSparameters1['_GateSpacing'] = _GateSpacing
        # NMOSparameters1['_SDWidth'] = _SDWidth
        #
        # self._DesignParameter['_NMOS1'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='_NMOS1In{}'.format(_Name)))[0]
        # self._DesignParameter['_NMOS1']['_DesignObj']._CalculateNMOSDesignParameter(**NMOSparameters1)
        # self._DesignParameter['_NMOS1']['_XYCoordinates'] = [[0, 0]]

        PMOSparameters1 = copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation)
        PMOSparameters1['_PMOSNumberofGate'] = _Finger1
        PMOSparameters1['_PMOSChannelWidth'] = round(_ChannelWidth * _NPRatio)
        PMOSparameters1['_PMOSChannellength'] = _ChannelLength
        PMOSparameters1['_PMOSDummy'] = _Dummy
        PMOSparameters1['_XVT'] = _XVT
        PMOSparameters1['_GateSpacing'] = _GateSpacing
        PMOSparameters1['_SDWidth'] = _SDWidth

        self._DesignParameter['_PMOS1'] = \
        self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='_PMOS1In{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS1']['_DesignObj']._CalculatePMOSDesignParameter(**PMOSparameters1)
        self._DesignParameter['_PMOS1']['_XYCoordinates'] = [[-(_LengthPMOSBtwPO * ((_Finger1 + _Finger3) / 2 + 1) + _LengthPMOSBtwPO * (_Finger2 + 1)), 0]]


        PMOSparameters2 = copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation)
        PMOSparameters2['_PMOSNumberofGate'] = _Finger2
        PMOSparameters2['_PMOSChannelWidth'] = round(_ChannelWidth * _NPRatio)
        PMOSparameters2['_PMOSChannellength'] = _ChannelLength
        PMOSparameters2['_PMOSDummy'] = _Dummy
        PMOSparameters2['_XVT'] = _XVT
        PMOSparameters2['_GateSpacing'] = _GateSpacing
        PMOSparameters2['_SDWidth'] = _SDWidth

        self._DesignParameter['_PMOS2'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='_PMOS2In{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS2']['_DesignObj']._CalculatePMOSDesignParameter(**PMOSparameters2)
        self._DesignParameter['_PMOS2']['_XYCoordinates'] = [[-(_LengthPMOSBtwPO * ((_Finger3 + _Finger2) / 2 + 1)), 0]]


        PMOSparameters3 = copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation)
        PMOSparameters3['_PMOSNumberofGate'] = _Finger3
        PMOSparameters3['_PMOSChannelWidth'] = round(_ChannelWidth * _NPRatio)
        PMOSparameters3['_PMOSChannellength'] = _ChannelLength
        PMOSparameters3['_PMOSDummy'] = _Dummy
        PMOSparameters3['_XVT'] = _XVT
        PMOSparameters3['_GateSpacing'] = _GateSpacing
        PMOSparameters3['_SDWidth'] = _SDWidth

        self._DesignParameter['_PMOS3'] = \
            self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='_PMOS3In{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS3']['_DesignObj']._CalculatePMOSDesignParameter(**PMOSparameters3)
        self._DesignParameter['_PMOS3']['_XYCoordinates'] = [[0, 0]]

        PMOSparameters4 = copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation)
        PMOSparameters4['_PMOSNumberofGate'] = _Finger2
        PMOSparameters4['_PMOSChannelWidth'] = round(_ChannelWidth * _NPRatio)
        PMOSparameters4['_PMOSChannellength'] = _ChannelLength
        PMOSparameters4['_PMOSDummy'] = _Dummy
        PMOSparameters4['_XVT'] = _XVT
        PMOSparameters4['_GateSpacing'] = _GateSpacing
        PMOSparameters4['_SDWidth'] = _SDWidth

        self._DesignParameter['_PMOS4'] = \
            self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='_PMOS4In{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS4']['_DesignObj']._CalculatePMOSDesignParameter(**PMOSparameters4)
        self._DesignParameter['_PMOS4']['_XYCoordinates'] = [
            [_LengthPMOSBtwPO * ((_Finger3 + _Finger2) / 2 + 1), 0]]

        PMOSparameters5 = copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation)
        PMOSparameters5['_PMOSNumberofGate'] = _Finger1
        PMOSparameters5['_PMOSChannelWidth'] = round(_ChannelWidth * _NPRatio)  # Need to Modify
        PMOSparameters5['_PMOSChannellength'] = _ChannelLength
        PMOSparameters5['_PMOSDummy'] = _Dummy
        PMOSparameters5['_XVT'] = _XVT
        PMOSparameters5['_GateSpacing'] = _GateSpacing
        PMOSparameters5['_SDWidth'] = _SDWidth

        self._DesignParameter['_PMOS5'] = \
            self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='_PMOS5In{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS5']['_DesignObj']._CalculatePMOSDesignParameter(**PMOSparameters5)
        self._DesignParameter['_PMOS5']['_XYCoordinates'] = [[_LengthPMOSBtwPO * ((_Finger1 + _Finger3) / 2 + 1) + _LengthPMOSBtwPO * (_Finger2 + 1), 0]]

        ################################### BPLayer Delete #########################################################

        self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'] =[]
        self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'] = []
        self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'] = []
        self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'] = []
        self._DesignParameter['_PMOS5']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'] = []

        ################################### VSS Genteration #########################################################

        _ContactNum = int(((_Finger1 + 1) * 2 + (_Finger2 + 1) * 2 + _Finger3 + 1) * _LengthPMOSBtwPO // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2))

        _PbodyContact1 = copy.deepcopy(PbodyContact._PbodyContact._ParametersForDesignCalculation)
        _PbodyContact1['_NumberOfPbodyCOX'] = _ContactNum
        _PbodyContact1['_NumberOfPbodyCOY'] = _NumberOfPbodyCOY
        _PbodyContact1['_Met1XWidth'] = _SupplyMet1XWidth
        _PbodyContact1['_Met1YWidth'] = _SupplyMet1YWidth

        self._DesignParameter['PbodyContact1'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_DesignParameter=None, _Name='_PbodyContact1In{}'.format(_Name)))[0]
        self._DesignParameter['PbodyContact1']['_DesignObj']._CalculatePbodyContactDesignParameter(**_PbodyContact1)

        self._DesignParameter['PbodyContact1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']=self._DesignParameter['PbodyContact1']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._PpMinExtensiononPactive

        self._DesignParameter['PbodyContact1']['_XYCoordinates'] = [[0, \
             self._DesignParameter['PbodyContact1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2 + _DRCObj._NMOS2GuardringMinSpace +\
            self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']]]

        ############################################# Metal 1 Routing#########################################################
        #PMOS1,5

        YCo=-self._DesignParameter['PbodyContact1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + self._DesignParameter['PbodyContact1']['_XYCoordinates'][0][1]

        self._DesignParameter['_Met1PMOS1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[], _Width=None)
        self._DesignParameter['_Met1PMOS1']['_Width'] = _LengthPMOSBtwPO*_Finger1+self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        self._DesignParameter['_Met1PMOS1']['_XYCoordinates'] = [[[self._DesignParameter['_PMOS5']['_XYCoordinates'][0][0],self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2],\
                                                                  [self._DesignParameter['_PMOS5']['_XYCoordinates'][0][0],YCo]], \
                                                                     [[self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0],self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2],\
                                                                      [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], YCo]]]

        #PMOS3

        self._DesignParameter['_Met1PMOS2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[], _Width=None)
        self._DesignParameter['_Met1PMOS2']['_Width'] = _LengthPMOSBtwPO*_Finger3+self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        self._DesignParameter['_Met1PMOS2']['_XYCoordinates'] = [[[self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0],self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2],\
                                                                  [self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0],YCo]]]

        ############################################# Poly Dummy Routing#########################################################

        self._DesignParameter['_AdditionalPolyOnGate'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],_XYCoordinates=[], _XWidth=None, _YWidth=None, _ElementName=None, )
        self._DesignParameter['_AdditionalPolyOnGate']['_XWidth'] = self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        self._DesignParameter['_AdditionalPolyOnGate']['_YWidth'] = self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
        self._DesignParameter['_AdditionalPolyOnGate']['_XYCoordinates'] = [[_LengthPMOSBtwPO*(_Finger3/2+0.5),0], [-(_LengthPMOSBtwPO*(_Finger3/2+0.5)),0],[_LengthPMOSBtwPO*(_Finger3/2+0.5+_Finger2+1),0],\
                                                                            [_LengthPMOSBtwPO*(_Finger3/2+0.5+_Finger2+_Finger1+2),0],[-(_LengthPMOSBtwPO*(_Finger3/2+0.5+_Finger2+1)),0],\
                                                                            [-(_LengthPMOSBtwPO*(_Finger3/2+0.5+_Finger2+_Finger1+2)),0]]
        # PMOS1,PMOS5
        self._DesignParameter['_AdditionalPoly1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],_XYCoordinates=[], _XWidth=None, _YWidth=None, _ElementName=None, )
        self._DesignParameter['_AdditionalPoly1']['_XWidth'] = (_Finger1)*_LengthPMOSBtwPO+self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        self._DesignParameter['_AdditionalPoly1']['_YWidth'] =  self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

        self._DesignParameter['_AdditionalPoly1']['_XYCoordinates'] = [[self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0]-_LengthPMOSBtwPO/2,self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2], \
                                                                       [self._DesignParameter['_PMOS5']['_XYCoordinates'][0][0]+_LengthPMOSBtwPO/2,self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + \
                                                                        self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2]]

        # PMOS2, PMOS4
        self._DesignParameter['_AdditionalPoly2'] = self._BoundaryElementDeclaration( _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],_XYCoordinates=[], _XWidth=None, _YWidth=None, _ElementName=None, )
        self._DesignParameter['_AdditionalPoly2']['_XWidth'] = (_Finger2+1) * _LengthPMOSBtwPO + self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        self._DesignParameter['_AdditionalPoly2']['_YWidth'] = self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

        self._DesignParameter['_AdditionalPoly2']['_XYCoordinates'] = [[self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0],\
                                                                       (self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 +self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)],\
                                                                      [self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0],\
                                                                       (self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 +self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)]]

        # PMOS3

        self._DesignParameter['_AdditionalPoly3'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],_XYCoordinates=[], _XWidth=None, _YWidth=None, _ElementName=None, )
        self._DesignParameter['_AdditionalPoly3']['_XWidth'] = (_Finger3 - 1) * _LengthPMOSBtwPO + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        self._DesignParameter['_AdditionalPoly3']['_YWidth'] = self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

        self._DesignParameter['_AdditionalPoly3']['_XYCoordinates'] = [[self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0], \
            (self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 +self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)]]

         ############################################# Contact Placing #########################################################

        # PMOS1,PMOS5
        _ViaPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        _ViaPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = _Finger1-1
        _ViaPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = 1

        self._DesignParameter['_ViaPoly2Met1OnGate1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='_ViaPoly2Met1{}'.format(_Name)))[0]
        self._DesignParameter['_ViaPoly2Met1OnGate1']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureY(**_ViaPoly2Met1)
        self._DesignParameter['_ViaPoly2Met1OnGate1']['_XYCoordinates'] = [[self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0],self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2], \
                                                                       [self._DesignParameter['_PMOS5']['_XYCoordinates'][0][0],\
                                                                         self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2]]
        # PMOS2,PMOS4
        _ViaPoly2Met2 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        _ViaPoly2Met2['_ViaPoly2Met1NumberOfCOX'] = _Finger2-2
        _ViaPoly2Met2['_ViaPoly2Met1NumberOfCOY'] = 1

        self._DesignParameter['_ViaPoly2Met1OnGate2'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='_ViaPoly2Met2{}'.format(_Name)))[0]
        self._DesignParameter['_ViaPoly2Met1OnGate2']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureY(**_ViaPoly2Met2)
        self._DesignParameter['_ViaPoly2Met1OnGate2']['_XYCoordinates'] = [[self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0],\
                                                                       self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 +self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2],\
                                                                      [self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0],\
                                                                       self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 +self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2]]


        # PMOS3

        _ViaPoly2Met3 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        _ViaPoly2Met3['_ViaPoly2Met1NumberOfCOX'] = _Finger3 - 1
        _ViaPoly2Met3['_ViaPoly2Met1NumberOfCOY'] = 1

        self._DesignParameter['_ViaPoly2Met1OnGate3'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='_ViaPoly2Met3{}'.format(_Name)))[0]
        self._DesignParameter['_ViaPoly2Met1OnGate3']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureY(**_ViaPoly2Met3)
        self._DesignParameter['_ViaPoly2Met1OnGate3']['_XYCoordinates'] = [[self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0], \
            self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 +self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2]]

        ############################################# Via1 Placing #########################################################

        _ViaMet12Met2_1 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _ViaMet12Met2_1['_ViaMet12Met2NumberOfCOX'] = 1
        _ViaMet12Met2_1['_ViaMet12Met2NumberOfCOY'] = 2

        self._DesignParameter['_ViaMet12Met2_1'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='_ViaMet12Met2_1{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2_1']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaMet12Met2_1)

        tmp = []

        for i in range(0, _Finger2//2+1):
            tmp.append([self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2 * i][0]+self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0], 0])
        for i in range(0, _Finger2//2+1):
            tmp.append([self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2 * i ][0] + self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0], 0])

        self._DesignParameter['_ViaMet12Met2_1']['_XYCoordinates'] = tmp

        _ViaMet12Met2_2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _ViaMet12Met2_2['_ViaMet12Met2NumberOfCOX'] = 2
        _ViaMet12Met2_2['_ViaMet12Met2NumberOfCOY'] = 1

        self._DesignParameter['_ViaMet12Met2_2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='_ViaMet12Met2_2{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2_2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaMet12Met2_2)

        tmp=[]

        tmp.append([0,self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2])
        self._DesignParameter['_ViaMet12Met2_2']['_XYCoordinates'] = [[self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0],\
                                                                        (self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2)],\
                                                                      [self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0],\
                                                                          (self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2)]]

        ############################################# Via2 Placing #########################################################

        _ViaMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _ViaMet22Met3['_ViaMet22Met3NumberOfCOX'] = 2
        _ViaMet22Met3['_ViaMet22Met3NumberOfCOY'] = 1

        self._DesignParameter['_ViaMet22Met3'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='_ViaMet22Met3{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaMet22Met3)
        # tmp=[]
        #
        # tmp.append([0,self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2])
        self._DesignParameter['_ViaMet22Met3']['_XYCoordinates'] = [[self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0],\
                                                                        (self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2)],\
                                                                      [self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0],\
                                                                          (self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2)]]

        ############################################# Metal 2 Routing ########################################################

        self._DesignParameter['_Met2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],_XYCoordinates=[], _Width=None)
        self._DesignParameter['_Met2Routing']['_Width'] =  self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        self._DesignParameter['_Met2Routing']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet12Met2_1']['_XYCoordinates'][0][0],0],\
                                                                  [self._DesignParameter['_ViaMet12Met2_1']['_XYCoordinates'][_Finger2//2][0],0]],\
                                                                 [[self._DesignParameter['_ViaMet12Met2_1']['_XYCoordinates'][_Finger2//2+1][0],0],\
                                                                  [self._DesignParameter['_ViaMet12Met2_1']['_XYCoordinates'][-1][0],0]]]

        ##################################################### POLayer Pin Delete, Generation & Coordinates  ####################################################

        self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'] = []
        self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'] = []
        self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'] = []

        _POLayerPINDrawing=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PCPIN'][0],_Datatype=DesignParameters._LayerMapping['PCPIN'][1],_XYCoordinates=[], _XWidth=400, _YWidth=400),

        self._DesignParameter['_POLayerPINDrawing']['_XWidth'] = self._DesignParameter['_POLayer']['_XWidth']
        self._DesignParameter['_POLayerPINDrawing']['_YWidth'] = (self._DesignParameter['_POLayer']['_YWidth'] -self._DesignParameter['_ODLayer']['_YWidth']) / 2

        #PMOS2
        tmp = []
        for i in range(0, _Finger2):
            tmp.append([self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0],\
                        self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2 + self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_YWidth'] / 2])

        self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'] = tmp

        # PMOS4
        tmp = []
        for i in range(0, _Finger2):
            tmp.append([self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0],
                        self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2 + self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_YWidth'] / 2])

        self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'] = tmp

        # PMOS3
        tmp = []
        for i in range(0, _Finger3):
            tmp.append([self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0],\
                        self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2 + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_YWidth'] / 2])

        self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'] = tmp
        ##################################################### LVT Layer extend ###########################################

        if _XVT != None:

                self._DesignParameter[_XVT] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping[_XVT][0],
                    _Datatype=DesignParameters._LayerMapping[_XVT][1],
                    _XWidth=2*self._DesignParameter['_PMOS5']['_XYCoordinates'][0][0] ,
                    _YWidth=self._DesignParameter['_PMOS5']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._XvtMinEnclosureOfODY ,
                    _XYCoordinates=self._DesignParameter['_PMOS3']['_XYCoordinates']
                )

        ################################################ Summer_upper ##################################

        _Summer_upper = copy.deepcopy(Summer_upper._Summer_upper._ParametersForDesignCalculation)
        _Summer_upper['_Finger1'] = _Finger4
        _Summer_upper['_Finger2'] = _Finger5
        _Summer_upper['_Finger3'] = _Finger6
        _Summer_upper['_ChannelWidth'] = _ChannelWidth
        _Summer_upper['_NPRatio'] = _NPRatio
        _Summer_upper['_ChannelLength'] = _ChannelLength
        _Summer_upper['_Dummy'] = _Dummy
        _Summer_upper['_XVT'] = _XVT
        _Summer_upper['_GateSpacing'] = _GateSpacing
        _Summer_upper['_SDWidth'] = _SDWidth
        _Summer_upper['_SupplyRailType'] = _SupplyRailType
        _Summer_upper['_SupplyMet1XWidth'] = _SupplyMet1XWidth
        _Summer_upper['_SupplyMet1YWidth'] = _SupplyMet1YWidth
        _Summer_upper['_NumberOfPbodyCOY'] = _NumberOfPbodyCOY


        self._DesignParameter['Summer_upper'] = self._SrefElementDeclaration(_DesignObj=Summer_upper._Summer_upper(_Name='_Summer_upperIn{}'.format(_Name)))[0]
        self._DesignParameter['Summer_upper']['_DesignObj']._CalculateDesignParameter(**_Summer_upper)
        self._DesignParameter['Summer_upper']['_XYCoordinates']=[[self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0]-(_LengthPMOSBtwPO*((_Finger4+_Finger6)//2+_Finger5+2)),\
                                                                  self._DesignParameter['PbodyContact1']['_XYCoordinates'][0][1]+self._DesignParameter['PbodyContact1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']/2+\
                                                                  self._DesignParameter['Summer_upper']['_DesignObj']._DesignParameter['_NWVSS']['_YWidth']/2-\
                                                                  self._DesignParameter['Summer_upper']['_DesignObj']._DesignParameter['PbodyContact2']['_XYCoordinates'][0][1]]]

        ##################################### Metal 2 Routing Between Summer_upper and middle  ##################################
        #왼쪽부터 순서대로 2개의 Met2 Routing
        self._DesignParameter['Met2Routing_1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],_XYCoordinates=[], _Width=None)
        self._DesignParameter['Met2Routing_1']['_Width'] =  self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        self._DesignParameter['Met2Routing_1']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet12Met2_1']['_XYCoordinates'][0][0],0],\
                                                                  [self._DesignParameter['_ViaMet12Met2_1']['_XYCoordinates'][0][0],\
                                                                   self._DesignParameter['Summer_upper']['_XYCoordinates'][0][1]]]]

        self._DesignParameter['Met2Routing_4'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],_XYCoordinates=[], _Width=None)
        self._DesignParameter['Met2Routing_4']['_Width'] =  self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        self._DesignParameter['Met2Routing_4']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet12Met2_1']['_XYCoordinates'][-1][0],0],\
                                                                  [self._DesignParameter['_ViaMet12Met2_1']['_XYCoordinates'][-1][0],\
                                                                   self._DesignParameter['Summer_upper']['_XYCoordinates'][0][1]]]]
        self._DesignParameter['_ViaMet12Met2_1']['_XYCoordinates']
        ########################################### Metal3 Routing ###############################################

        self._DesignParameter['_Met3Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],_XYCoordinates=[], _Width=None)
        self._DesignParameter['_Met3Routing']['_Width'] =  self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        self._DesignParameter['_Met3Routing']['_XYCoordinates'] = [[[self._DesignParameter['Summer_upper']['_DesignObj']._DesignParameter['_ViaMet22Met3_1']['_XYCoordinates'][0][0]-(_LengthPMOSBtwPO*((_Finger4+_Finger6)//2+_Finger5+2)),\
                                                                    self._DesignParameter['Summer_upper']['_DesignObj']._DesignParameter['_ViaMet22Met3_1']['_XYCoordinates'][0][1]+self._DesignParameter['Summer_upper']['_XYCoordinates'][0][1]],\
                                                                    [self._DesignParameter['_ViaMet12Met2_1']['_XYCoordinates'][-1][0],\
                                                                    self._DesignParameter['Summer_upper']['_DesignObj']._DesignParameter['_ViaMet22Met3_1']['_XYCoordinates'][0][1]+self._DesignParameter['Summer_upper']['_XYCoordinates'][0][1]]],\

                                                                   [[self._DesignParameter['Summer_upper']['_DesignObj']._DesignParameter['_ViaMet22Met3_1']['_XYCoordinates'][1][0]-(_LengthPMOSBtwPO*((_Finger4+_Finger6)//2+_Finger5+2)),\
                                                                    self._DesignParameter['Summer_upper']['_DesignObj']._DesignParameter['_ViaMet22Met3_1']['_XYCoordinates'][1][1]+self._DesignParameter['Summer_upper']['_XYCoordinates'][0][1]],\
                                                                    [self._DesignParameter['_ViaMet12Met2_1']['_XYCoordinates'][0][0],\
                                                                    self._DesignParameter['Summer_upper']['_DesignObj']._DesignParameter['_ViaMet22Met3_1']['_XYCoordinates'][1][1]+self._DesignParameter['Summer_upper']['_XYCoordinates'][0][1]]]]


        ############################################ Via2 Placing #########################################################

        _ViaMet22Met3_1 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _ViaMet22Met3_1['_ViaMet22Met3NumberOfCOX'] = 1
        _ViaMet22Met3_1['_ViaMet22Met3NumberOfCOY'] = 2

        self._DesignParameter['_ViaMet22Met3_1'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='_ViaMet22Met3_1{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3_1']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_ViaMet22Met3_1)

        self._DesignParameter['_ViaMet22Met3_1']['_XYCoordinates'] =[[self._DesignParameter['_ViaMet12Met2_1']['_XYCoordinates'][-1][0],\
                                                                    self._DesignParameter['Summer_upper']['_DesignObj']._DesignParameter['_ViaMet22Met3_1']['_XYCoordinates'][0][1]+self._DesignParameter['Summer_upper']['_XYCoordinates'][0][1]],\
                                                                     [self._DesignParameter['_ViaMet12Met2_1']['_XYCoordinates'][0][0],\
                                                                    self._DesignParameter['Summer_upper']['_DesignObj']._DesignParameter['_ViaMet22Met3_1']['_XYCoordinates'][1][1]+self._DesignParameter['Summer_upper']['_XYCoordinates'][0][1]]]



#'C:\\Users\\ljw95\\PycharmProjects\\LayGenGUI'

if __name__ == '__main__':
    #for i in range(0,100):
        import ftplib
        import random

        # _Finger3 = random.randint(2, 20)
        # _Finger2 = random.randint(2, 20)
        # _Finger1 = random.randint(2, 20)
        # _Finger4=random.randint(2, 20)
        # _Finger5=random.randint(2, 20)
        # _Finger6=random.randint(2, 20)
        # _ChannelWidth = random.randrange(300, 500, 2)
        # _ChannelLength = random.randrange(30, 48, 2)

        _Finger1 = 12
        _Finger2 = 8
        _Finger3 = 14
        _Finger4=8
        _Finger5=16
        _Finger6=6
        _ChannelWidth = 500
        _ChannelLength = 30

        _NPRatio = 1
        _NumberOfPbodyCOY=3
        _Dummy = None
        _XVT = 'LVT'
        _GateSpacing = None
        _SDWidth = None
        _SupplyRailType=1
        _SupplyMet1XWidth = None
        _SupplyMet1YWidth = None
        #from Private import MyInfo
         #import DRCchecker

        libname = '_Summer_middle'
        cellname = '_Summer_middle'
        _fileName = cellname + '.gds'

        InputParams = dict(
            _Finger1=_Finger1,
            _Finger2=_Finger2,
            _Finger3=_Finger3,
            _Finger4=_Finger4,
            _Finger5 =_Finger5,
            _Finger6 =_Finger6,
            _NumberOfPbodyCOY=_NumberOfPbodyCOY,
            _ChannelWidth=_ChannelWidth,
            _NPRatio=_NPRatio,
            _ChannelLength=_ChannelLength,
            _Dummy=_Dummy,
            _XVT=_XVT,
            _GateSpacing=_GateSpacing,
            _SDWidth=_SDWidth,
            _SupplyRailType = _SupplyRailType,
            _SupplyMet1XWidth = _SupplyMet1XWidth,
            _SupplyMet1YWidth = _SupplyMet1YWidth
        )



        LayoutObj = _Summer_middle(_DesignParameter=None, _Name=cellname)
        LayoutObj._CalculateDesignParameter(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
        testStreamFile = open('./{}'.format(_fileName), 'wb')
        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()


        ftp = ftplib.FTP('141.223.29.62')
        ftp.login('ljw95', 'dlwodn123')
        ftp.cwd('/mnt/sdc/ljw95/OPUS/ss28')
        myfile = open('_Summer_middle.gds', 'rb')
        ftp.storbinary('STOR _Summer_middle.gds', myfile)
        myfile.close()
        ftp.close()

        # import DRCchecker
        #
        # a = DRCchecker.DRCchecker('ljw95', 'dlwodn123', '/mnt/sdc/ljw95/OPUS/ss28', '/mnt/sdc/ljw95/OPUS/ss28/DRC/run',
        #                           '_Summer_middle', '_Summer_middle', None)
        # a.DRCchecker()
        #
        # print("DRC Clean!!!")