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
from generatorLib.generator_models import ViaPoly2Met1_resize
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaMet22Met3
from generatorLib.generator_models import SupplyRails
from generatorLib.generator_models import Z_PWR_CNT

class _Mux_uppper(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_Finger=None,_ChannelWidth=None,_NPRatio=None,_ChannelLength=None,_Dummy=None,_XVT=None,
                                      _GateSpacing=None,_SDWidth=None)

    def __init__(self, _DesignParameter=None, _Name='_Mux_upper'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))


    def _CalculateDesignParameter(self,_Finger=None,_ChannelWidth=None,_NPRatio=None,_ChannelLength=None,_Dummy=None,_XVT=None,
                                      _GateSpacing=None,_SDWidth=None
                                      ):

        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        MinSnapSpacing = _DRCObj._MinSnapSpacing

        ################################### PMOS Genteration #########################################################

        PMOSparameters = copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation)
        PMOSparameters['_PMOSNumberofGate'] = _Finger
        PMOSparameters['_PMOSChannelWidth'] = round(_ChannelWidth * _NPRatio)  # Need to Modify
        PMOSparameters['_PMOSChannellength'] = _ChannelLength
        PMOSparameters['_PMOSDummy'] = _Dummy
        PMOSparameters['_XVT'] = _XVT
        PMOSparameters['_GateSpacing'] = _GateSpacing
        PMOSparameters['_SDWidth'] = _SDWidth

        self._DesignParameter['_PMOS'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='_PMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS']['_DesignObj']._CalculatePMOSDesignParameter(**PMOSparameters)
        self._DesignParameter['-PMOS']['_XYCoordinates']=[[0,0]]


if __name__ == '__main__':
    #for i in range(0,100):
        import ftplib
       # import random

        _Finger = 2
        _ChannelWidth = 500
        _NPRatio = 2
        _ChannelLength = 30
        _Dummy = None
        _XVT = None
        _GateSpacing = None
        _SDWidth = None

         #from Private import MyInfo
         #import DRCchecker

        libname = '_Mux_uppper'
        cellname = '_Mux_upper'
        _fileName = cellname + '.gds'

        InputParams = dict(
            _Finger=_Finger,
            _ChannelWidth=_ChannelWidth,
            _NPRatio=_NPRatio,
            _ChannelLength=_ChannelLength,
            _Dummy=_Dummy,
            _XVT=_XVT,
            _GateSpacing=_GateSpacing,
            _SDWidth=_SDWidth

        )



        LayoutObj = _Mux_upper(_DesignParameter=None, _Name=cellname)
        LayoutObj._CalculateDesignParameter(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
        testStreamFile = open('./{}'.format(_fileName), 'wb')
        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()


        ftp = ftplib.FTP('141.223.29.62')
        ftp.login('ljw95', 'dlwodn123')
        ftp.cwd('/mnt/sdc/ljw95/OPUS/ss28')
        myfile = open('_Mux_uppper.gds', 'rb')
        ftp.storbinary('STOR _Mux_upper.gds', myfile)
        myfile.close()
        ftp.close()