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


class _LDO_Bottom(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_Finger1=None,_Finger2=None,_Finger3=None,_Finger4=None,_Finger5 =None,_Finger6 =None,_Finger7=None,_Finger8 = None,
                                _Finger9 = None,_Finger10 = None,_ChannelWidth=None,_NPRatio=None,_ChannelLength=None,_Dummy=None,_XVT=None,_PCCrit=None,
                                      _NumberOfPbodyCOY=None,_GateSpacing=None,_SDWidth=None,_SupplyRailType=1,_SupplyMet1XWidth=None,_SupplyMet1YWidth=None, _ResWidth = None,
		    _ResLength = None,_CONUMY = None,_XWidth = None,_YWidth = None,_NumofGates = None,guardring_right = None,guardring_left = None,guardring_top = None,guardring_bot = None,Guardring=None)

    def __init__(self, _DesignParameter=None, _Name='_LDO_Bottom'):
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

            _Finger1 = 3,_Finger2 = 3,_Finger3 = 8,_Finger4 = 4,_Finger5 = 2,_Finger6 = 9,_Finger7 = 8,_Finger8 = 9,_Finger9 = 30,_Finger10=40,_ChannelWidth = 600,_ChannelLength = 30
            ,_NPRatio = 1,_NumberOfPbodyCOY = 3,_Dummy = None,_XVT = 'LVT',_PCCrit = None,_GateSpacing = None,_SDWidth = None,_SupplyRailType = 1
            , _SupplyMet1XWidth = None,_SupplyMet1YWidth = None,_ResWidth = 938,_ResLength = 580,_CONUMY = 1,_XWidth = 838,_YWidth = 1874,Guardring = False,_NumofGates = 1,guardring_right = 3,guardring_left = 3,guardring_top = 3,guardring_bot = 3
    ):

        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        MinSnapSpacing = _DRCObj._MinSnapSpacing
        _LengthPMOSBtwPO = _DRCObj.DRCPolygateMinSpace(_DRCObj.DRCPolyMinSpace(_Width=_ChannelWidth, _ParallelLength=_ChannelLength)) + _ChannelLength
        _XYCoordinatesofMOS = [[0, 0]]


        ################################### PMOS Genteration #########################################################

        PMOSparameters1 = copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation)
        PMOSparameters1['_PMOSNumberofGate'] = _Finger1
        PMOSparameters1['_PMOSChannelWidth'] = round(_ChannelWidth * _NPRatio)
        PMOSparameters1['_PMOSChannellength'] = _ChannelLength
        PMOSparameters1['_PMOSDummy'] = _Dummy
        PMOSparameters1['_XVT'] = _XVT
        PMOSparameters1['_GateSpacing'] = _GateSpacing
        PMOSparameters1['_SDWidth'] = _SDWidth

        self._DesignParameter['_PMOS1'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='_PMOS1In{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS1']['_DesignObj']._CalculatePMOSDesignParameter(**PMOSparameters1)
        self._DesignParameter['_PMOS1']['_XYCoordinates'] = _XYCoordinatesofMOS


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
        self._DesignParameter['_PMOS2']['_XYCoordinates'] = [[(_LengthPMOSBtwPO * ((_Finger1 + _Finger2)/2 + 1))+_XYCoordinatesofMOS[0][0], _XYCoordinatesofMOS[0][1]]]


        PMOSparameters3 = copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation)
        PMOSparameters3['_PMOSNumberofGate'] = _Finger3
        PMOSparameters3['_PMOSChannelWidth'] = round(_ChannelWidth * _NPRatio)
        PMOSparameters3['_PMOSChannellength'] = _ChannelLength
        PMOSparameters3['_PMOSDummy'] = _Dummy
        PMOSparameters3['_XVT'] = _XVT
        PMOSparameters3['_GateSpacing'] = _GateSpacing
        PMOSparameters3['_SDWidth'] = _SDWidth

        self._DesignParameter['_PMOS3'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='_PMOS3In{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS3']['_DesignObj']._CalculatePMOSDesignParameter(**PMOSparameters3)
        self._DesignParameter['_PMOS3']['_XYCoordinates'] = [[(_LengthPMOSBtwPO * ((_Finger3 + _Finger1)/2 + _Finger2+2))+_XYCoordinatesofMOS[0][0], _XYCoordinatesofMOS[0][1]]]


        PMOSparameters4 = copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation)
        PMOSparameters4['_PMOSNumberofGate'] = _Finger2
        PMOSparameters4['_PMOSChannelWidth'] = round(_ChannelWidth * _NPRatio)
        PMOSparameters4['_PMOSChannellength'] = _ChannelLength
        PMOSparameters4['_PMOSDummy'] = _Dummy
        PMOSparameters4['_XVT'] = _XVT
        PMOSparameters4['_GateSpacing'] = _GateSpacing
        PMOSparameters4['_SDWidth'] = _SDWidth

        self._DesignParameter['_PMOS4'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='_PMOS4In{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS4']['_DesignObj']._CalculatePMOSDesignParameter(**PMOSparameters4)
        self._DesignParameter['_PMOS4']['_XYCoordinates'] = [[_LengthPMOSBtwPO * ((_Finger1 + _Finger4)/2 +_Finger2+_Finger3+ 3)+_XYCoordinatesofMOS[0][0], _XYCoordinatesofMOS[0][1]]]

        ################################### NMOS Genteration #########################################################

        NMOS2inputs = copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation)
        NMOS2inputs['_NMOSNumberofGate'] = _Finger5
        NMOS2inputs['_NMOSDummy'] = _Dummy
        NMOS2inputs['_GateSpacing'] = _GateSpacing
        NMOS2inputs['_SDWidth'] = _SDWidth
        NMOS2inputs['_XVT'] = _XVT
        NMOS2inputs['_PCCrit'] = _PCCrit
        NMOS2inputs['_NMOSChannelWidth'] = _ChannelWidth
        NMOS2inputs['_NMOSChannellength'] = _ChannelWidth

        self._DesignParameter['_NMOS1'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOS1In{}'.format(_Name)))[0]
        self._DesignParameter['_NMOS1']['_DesignObj']._CalculateNMOSDesignParameter(**NMOS2inputs)
        self._DesignParameter['_NMOS1']['_XYCoordinates'] = _XYCoordinatesofMOS

        # NMOSparameters1 = copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation)
        # NMOSparameters1['_NMOSNumberofGate'] = _Finger5
        # NMOSparameters1['_NMOSChannelWidth'] = round(_ChannelWidth * _NPRatio)
        # NMOSparameters1['_NMOSChannellength'] = _ChannelWidth
        # NMOSparameters1['_NMOSDummy'] = _Dummy
        # NMOSparameters1['_XVT'] = _XVT
        # NMOSparameters1['_GateSpacing'] = _GateSpacing
        # NMOSparameters1['_SDWidth'] = _SDWidth
        # NMOSparameters1['_PCCrit'] = _PCCrit
        #
        # self._DesignParameter['_NMOS1'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0,_DesignObj=NMOSWithDummy._NMOS(_Name='_NMOS1In{}'.format(_Name)))[0]
        # self._DesignParameter['_NMOS1']['_DesignObj']._CalculateNMOSDesignParameter(**NMOSparameters1)
        # self._DesignParameter['_NMOS1']['_XYCoordinates'] = [[(_LengthPMOSBtwPO * ((_Finger5 + _Finger6)/2 + 1))+_XYCoordinatesofMOS[0][0],_XYCoordinatesofMOS[0][1]-(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']+_DRCObj._OPlayeroverPoly)]]

        # NMOSparameters2 = copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation)
        # NMOSparameters2['_NMOSNumberofGate'] = _Finger6
        # NMOSparameters2['_NMOSChannelWidth'] = round(_ChannelWidth * _NPRatio)
        # NMOSparameters2['_NMOSChannellength'] = _ChannelLength
        # NMOSparameters2['_NMOSDummy'] = _Dummy
        # NMOSparameters2['_XVT'] = _XVT
        # NMOSparameters2['_GateSpacing'] = _GateSpacing
        # NMOSparameters2['_SDWidth'] = _SDWidth
        #
        # self._DesignParameter['_NMOS2'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0,_DesignObj=NMOSWithDummy._NMOS(_Name='_NMOS2In{}'.format(_Name)))[0]
        # self._DesignParameter['_NMOS2']['_DesignObj']._CalculateNMOSDesignParameter(**NMOSparameters2)
        # self._DesignParameter['_NMOS2']['_XYCoordinates'] = [[_XYCoordinatesofMOS[0][0],_XYCoordinatesofMOS[0][1]-(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']+_DRCObj._OPlayeroverPoly)]]
        #
        # NMOSparameters3 = copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation)
        # NMOSparameters3['_NMOSNumberofGate'] = _Finger7
        # NMOSparameters3['_NMOSChannelWidth'] = round(_ChannelWidth * _NPRatio)
        # NMOSparameters3['_NMOSChannellength'] = _ChannelLength
        # NMOSparameters3['_NMOSDummy'] = _Dummy
        # NMOSparameters3['_XVT'] = _XVT
        # NMOSparameters3['_GateSpacing'] = _GateSpacing
        # NMOSparameters3['_SDWidth'] = _SDWidth
        #
        # self._DesignParameter['_NMOS3'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0,_DesignObj=NMOSWithDummy._NMOS(_Name='_NMOS3In{}'.format(_Name)))[0]
        # self._DesignParameter['_NMOS3']['_DesignObj']._CalculateNMOSDesignParameter(**NMOSparameters3)
        # self._DesignParameter['_NMOS3']['_XYCoordinates'] = [[(_LengthPMOSBtwPO * ((_Finger5 + _Finger7)/2 + _Finger6+2))+_XYCoordinatesofMOS[0][0],_XYCoordinatesofMOS[0][1]-(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']+_DRCObj._OPlayeroverPoly)]]



        ################################### BPLayer Genteration #########################################################



if __name__ == '__main__':
   #  for i in range(0,100):
        import ftplib
        import random


        # _Finger2 = random.randint(6, 30)
        # _Finger4=random.randint(2, 30)
        # _Finger5=random.randint(2, 30)
        # _Finger9=random.randint(2, 30)
        # _ChannelWidth = random.randrange(300, 500, 2)
        # _ChannelLength = random.randrange(30, 48, 2)



        _Finger1 = 3
        _Finger2 = 3
        _Finger3 = 8
        _Finger4 = 4
        _Finger5 = 2
        _Finger6 = 9
        _Finger7 = 8
        _Finger8 = 9
        _Finger9 = 30
        _Finger10 = 40

        _ChannelWidth = 600
        _ChannelLength = 30


        _NPRatio = 1
        _NumberOfPbodyCOY=3
        _Dummy = None
        _XVT = 'LVT'
        _PCCrit=None
        _GateSpacing = None
        _SDWidth = None
        _SupplyRailType=1
        _SupplyMet1XWidth = None
        _SupplyMet1YWidth = None

        _ResWidth = 938
        _ResLength = 580
        _CONUMY = 1
        _XWidth = 838
        _YWidth = 1874
        Guardring = False
        _NumofGates = 1
        guardring_right = 3
        guardring_left = 3
        guardring_top = 3
        guardring_bot = 3


        #from Private import MyInfo
         #import DRCchecker

        libname = '_LDO_Bottom'
        cellname = '_LDO_Bottom'
        _fileName = cellname + '.gds'

        InputParams = dict(
            _Finger1=_Finger1,
            _Finger2=_Finger2,
            _Finger3=_Finger3,
            _Finger4=_Finger4,
            _Finger5 =_Finger5,
            _Finger6 =_Finger6,
            _Finger7=_Finger7,
            _Finger8 = _Finger8,
            _Finger9 = _Finger9,
            _Finger10 = _Finger10,
            _NumberOfPbodyCOY=_NumberOfPbodyCOY,
            _ChannelWidth=_ChannelWidth,
            _NPRatio=_NPRatio,
            _ChannelLength=_ChannelLength,
            _Dummy=_Dummy,
            _XVT=_XVT,
            _PCCrit=_PCCrit,
            _GateSpacing=_GateSpacing,
            _SDWidth=_SDWidth,
            _SupplyRailType = _SupplyRailType,
            _SupplyMet1XWidth = _SupplyMet1XWidth,
            _SupplyMet1YWidth = _SupplyMet1YWidth,
            _ResWidth = _ResWidth,
		    _ResLength = _ResLength,
		    _CONUMY = _CONUMY  ,
		    _XWidth = _XWidth,
		    _YWidth = _YWidth,
		    _NumofGates = _NumofGates,
		    guardring_right = guardring_right,
		    guardring_left = guardring_left,
		    guardring_top = guardring_top,
		    guardring_bot = guardring_bot,
            Guardring=Guardring
        )



        LayoutObj = _LDO_Bottom(_DesignParameter=None, _Name=cellname)
        LayoutObj._CalculateDesignParameter(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
        testStreamFile = open('./{}'.format(_fileName), 'wb')
        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()


        ftp = ftplib.FTP('141.223.29.62')
        ftp.login('ljw95', 'dlwodn123')
        ftp.cwd('/mnt/sdc/ljw95/OPUS/ss28')
        myfile = open('_LDO_Bottom.gds', 'rb')
        ftp.storbinary('STOR _LDO_Bottom.gds', myfile)
        myfile.close()
        ftp.close()

        # import DRCchecker
        #
        # a = DRCchecker.DRCchecker('ljw95', 'dlwodn123', '/mnt/sdc/ljw95/OPUS/ss28', '/mnt/sdc/ljw95/OPUS/ss28/DRC/run',
        #                           '_Summer_middle', '_Summer_middle', None)
        # a.DRCchecker()
        #
        # print("DRC Clean!!!")