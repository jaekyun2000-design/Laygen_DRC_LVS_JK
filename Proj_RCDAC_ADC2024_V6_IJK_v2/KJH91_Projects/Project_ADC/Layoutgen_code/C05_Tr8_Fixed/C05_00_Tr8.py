
## Import Basic Modules
    ## Engine
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_ADC.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

    ## Library
import copy
import math
import numpy as np
import time

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A03_NmosWithDummy_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A04_PmosWithDummy_KJH2
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A14_Mosfet_KJH3


## Define Class
class _Tr8(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
# TR8
    # Physical dimension
    _Tr8_NumberofGate	            = 4,       # Number
    _Tr8_ChannelWidth	            = 500,     # Number
    _Tr8_ChannelLength	            = 30,       # Number
    _Tr8_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT


    )

    ## Initially Generated _DesignParameter
    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
            _Name=self._NameDeclaration(_Name=_Name),
            _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
            _XYcoordAsCent=dict(_XYcoordAsCent=0),
            )

    ## DesignParameter Calculation
    def _CalculateDesignParameter(self,
# TR8
    # Physical dimension
    _Tr8_NumberofGate	            = 4,       # Number
    _Tr8_ChannelWidth	            = 500,     # Number
    _Tr8_ChannelLength	            = 30,       # Number
    _Tr8_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT


                                  ):

        ## Class_HEADER: Pre Defined Parameter Before Calculation
            ## Load DRC library
        _DRCobj = DRC.DRC()
            ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ## CALCULATION START
        start_time = time.time()
        # end_time = time.time()
        # self.elapsed_time = end_time - start_time
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr4, nfettw
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  M4, nfettw: Sref Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A14_Mosfet_KJH3._Mosfet._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_MosType'] = 'NMOS'
        _Caculation_Parameters['_MosUpDn'] = 'Up'

        _Caculation_Parameters['_NumberofGate']     = _Tr8_NumberofGate
        _Caculation_Parameters['_ChannelWidth']     = _Tr8_ChannelWidth
        _Caculation_Parameters['_ChannelLength']    = _Tr8_ChannelLength
        _Caculation_Parameters['_GateSpacing']      = None
        _Caculation_Parameters['_SDWidth']          = None
        _Caculation_Parameters['_XVT']              = _Tr8_XVT
        _Caculation_Parameters['_PCCrit']           = True

        _Caculation_Parameters['_Source_Via_TF']                = True
        _Caculation_Parameters['_Source_Via_Close2POpin_TF']    = True
        _Caculation_Parameters['_Source_Comb_TF']               = True
        _Caculation_Parameters['_Source_Comb_POpinward_TF']     = True
        _Caculation_Parameters['_Source_Comb_Length']           = None

        _Caculation_Parameters['_Drain_Via_TF']                 = True
        _Caculation_Parameters['_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_Drain_Comb_TF']                = True
        _Caculation_Parameters['_Drain_Comb_POpinward_TF']      = False
        _Caculation_Parameters['_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PODummy_TF']                   = True
        _Caculation_Parameters['_PODummy_Length']               = None
        _Caculation_Parameters['_PODummy_Placement']            = 'Up'

        _Caculation_Parameters['_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_POGate_Comb_TF']               = True
        _Caculation_Parameters['_POGate_Comb_length']           = 250
        _Caculation_Parameters['_POGate_Via_TF']                = True
        _Caculation_Parameters['_POGate_ViaMxMx']               = [0,2]

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Nmos'] = self._SrefElementDeclaration(_DesignObj=A14_Mosfet_KJH3._Mosfet(_DesignParameter=None, _Name='{}:SRF_Nmos'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Nmos']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos']['_XYCoordinates'] = [[0, 0]]


        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')

        # start_time = time.time()
        end_time = time.time()
        self.elapsed_time = end_time - start_time

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ZZ01_C05_00_Tr8_Fixed'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'C03_00_Tr8_v0_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
# TR8
    # Physical dimension
    _Tr8_NumberofGate	            = 4,       # Number
    _Tr8_ChannelWidth	            = 500,     # Number
    _Tr8_ChannelLength	            = 30,       # Number
    _Tr8_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

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
    ## Gen Object:
    LayoutObj = _Tr8(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    ''' Check Time'''
    elapsed_time = time.time() - start_time
    m, s = divmod(elapsed_time, 60)
    h, m = divmod(m, 60)

    print('###############      Sending to FTP Server...      ##################')
    My = MyInfo.USER(DesignParameters._Technology)
    Checker = DRCchecker_KJH0.DRCchecker_KJH0(
    username=My.ID,
    password=My.PW,
    WorkDir=My.Dir_Work,
    DRCrunDir=My.Dir_DRCrun,
    libname=libname,
    cellname=cellname,
    GDSDir=My.Dir_GDS
    )
    # Checker.lib_deletion()
    Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()


    print('#############################      Finished      ################################')
    print('{} Hours   {} minutes   {} seconds'.format(h, m, s))

# end of 'main():' ---------------------------------------------------------------------------------------------
