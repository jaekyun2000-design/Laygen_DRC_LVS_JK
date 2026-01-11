
## Import Basic Modules
    ## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

    ## Library
import copy
import math
import numpy as np
import time

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A08_PbodyContactPhyLen_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A07_NbodyContactPhyLen_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.D00_SARLogic_Inverter_KJH1 import D00_00_Inverter_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.D01_SARLogic_XmissionGate_KJH1 import D01_00_Xgate_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.D02_SARLogic_Nor_KJH1 import D02_02_Nor_KJH0


## Define Class
class _GetparamTest(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(

        _Test_distance = 150,

    ## DFF Common
        _DFF_Pbody_NumCont      = 2, # number
        _DFF_Nbody_NumCont      = 2, # number
        _DFF_PMOSXvt2NMOSXvt    = 500, # number
        _DFF_XvtTop2Pbody       = None, # number/None(Minimum)
        _DFF_Xvtdown2Nbody      = None, # number/None(Minimum)

    ## Master Xgate2
        ## Xgate common

        ## Xgate NMOS
        _Mst_Xgate2_NMOS_NumberofGate           = 2,
        _Mst_Xgate2_NMOS_ChannelWidth           = 800,
        _Mst_Xgate2_NMOS_ChannelLength          = 30,
        _Mst_Xgate2_NMOS_XVT                    = 'SLVT',
        _Mst_Xgate2_NMOS_POGate_Comb_length     = 100,

        ## Xgate NMOS
        _Mst_Xgate2_PMOS_NumberofGate           = 3,
        _Mst_Xgate2_PMOS_ChannelWidth           = 200,
        _Mst_Xgate2_PMOS_ChannelLength          = 30,
        _Mst_Xgate2_PMOS_XVT                    = 'SLVT',
        _Mst_Xgate2_PMOS_POGate_Comb_length     = 100,
    )

    ## Initially Generated _DesignParameter
    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
            _Name=self._NameDeclaration(_Name=_Name),
            _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
            )

    ## DesignParameter Calculation
    def _CalculateDesignParameter(self,

        _Test_distance = 150,

    ## DFF Common
        _DFF_Pbody_NumCont      = 2, # number
        _DFF_Nbody_NumCont      = 2, # number
        _DFF_PMOSXvt2NMOSXvt    = 500, # number
        _DFF_XvtTop2Pbody       = None, # number/None(Minimum)
        _DFF_Xvtdown2Nbody      = None, # number/None(Minimum)

    ## Master Xgate2
        ## Xgate common

        ## Xgate NMOS
        _Mst_Xgate2_NMOS_NumberofGate           = 2,
        _Mst_Xgate2_NMOS_ChannelWidth           = 800,
        _Mst_Xgate2_NMOS_ChannelLength          = 30,
        _Mst_Xgate2_NMOS_XVT                    = 'SLVT',
        _Mst_Xgate2_NMOS_POGate_Comb_length     = 100,

        ## Xgate NMOS
        _Mst_Xgate2_PMOS_NumberofGate           = 3,
        _Mst_Xgate2_PMOS_ChannelWidth           = 200,
        _Mst_Xgate2_PMOS_ChannelLength          = 30,
        _Mst_Xgate2_PMOS_XVT                    = 'SLVT',
        _Mst_Xgate2_PMOS_POGate_Comb_length     = 100,

                                  ):

        ## Class_HEADER: Pre Defined Parameter Before Calculation
            ## Load DRC library
        _DRCobj = DRC.DRC()
            ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ## CALCULATION START
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Mst: Xgate2
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D01_00_Xgate_KJH._Xgate._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOS_NumberofGate']                 = _Mst_Xgate2_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth']                 = _Mst_Xgate2_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength']                = _Mst_Xgate2_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing']                  = None
        _Caculation_Parameters['_NMOS_SDWidth']                      = None
        _Caculation_Parameters['_NMOS_XVT']                          = _Mst_Xgate2_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit']                       = True

        _Caculation_Parameters['_NMOS_Source_Via_TF']                = True
        _Caculation_Parameters['_NMOS_Source_Via_Close2POpin_TF']    = True
        _Caculation_Parameters['_NMOS_Source_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOS_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_NMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOS_Drain_Comb_Length']            = None

        _Caculation_Parameters['_NMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOS_PODummy_Length']               = None
        _Caculation_Parameters['_NMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOS_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_POGate_Comb_length']           = _Mst_Xgate2_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOS_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOS_NumberofGate']                 = _Mst_Xgate2_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth']                 = _Mst_Xgate2_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength']                = _Mst_Xgate2_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing']                  = None
        _Caculation_Parameters['_PMOS_SDWidth']                      = None
        _Caculation_Parameters['_PMOS_XVT']                          = _Mst_Xgate2_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit']                       = True

        _Caculation_Parameters['_PMOS_Source_Via_TF']                = True
        _Caculation_Parameters['_PMOS_Source_Via_Close2POpin_TF']    = True
        _Caculation_Parameters['_PMOS_Source_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOS_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_PMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOS_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOS_PODummy_Length']               = None
        _Caculation_Parameters['_PMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOS_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_POGate_Comb_length']           = _Mst_Xgate2_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx']               = [0,1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']           = _DFF_XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody']          = _DFF_Xvtdown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                   = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Mst_Xgate2'] = self._SrefElementDeclaration(_DesignObj=D01_00_Xgate_KJH._Xgate(_DesignParameter=None, _Name='{}:SRF_Mst_Xgate2'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Mst_Xgate2']['_Reflect'] = [1, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Xgate2']['_Angle'] = 180

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Xgate2']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Xgate2']['_XYCoordinates'] = [[21, 38]]


        tmp = self.get_param_KJH4('SRF_Mst_Xgate2','SRF_PMOS','BND_PODummyLayer')
        AA = tmp[0][0][-1][0]['_XY_up_right']
        AB = tmp[0][0][0][0]['_XY_down_right']

        tmp2 = self.get_outter_KJH5('SRF_Mst_Xgate2','SRF_PMOS','BND_PODummyLayer')

        output_element1 = tmp2['_Mostright']['index']
        output_elementname1 = tmp2['_Layercoord'][output_element1[0]][1]
        outter_coord1 = tmp2['_Mostright']['coord']

        output_element2 = tmp2['_Mostup']['index']
        output_elementname2 = tmp2['_Layercoord'][output_element2[0]][1]
        outter_coord2 = tmp2['_Mostup']['coord']


        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'ZZ_TEST'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'ZZ08_Test_getparam_KJH4_96'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

        _Test_distance = 500,

    ## DFF Common
        _DFF_Pbody_NumCont      = 2, # number
        _DFF_Nbody_NumCont      = 2, # number
        _DFF_PMOSXvt2NMOSXvt    = 500, # number
        _DFF_XvtTop2Pbody       = None, # number/None(Minimum)
        _DFF_Xvtdown2Nbody      = None, # number/None(Minimum)

    ## Master Xgate2
        ## Xgate common

        ## Xgate NMOS
        _Mst_Xgate2_NMOS_NumberofGate           = 2,
        _Mst_Xgate2_NMOS_ChannelWidth           = 800,
        _Mst_Xgate2_NMOS_ChannelLength          = 30,
        _Mst_Xgate2_NMOS_XVT                    = 'SLVT',
        _Mst_Xgate2_NMOS_POGate_Comb_length     = 100,

        ## Xgate NMOS
        _Mst_Xgate2_PMOS_NumberofGate           = 3,
        _Mst_Xgate2_PMOS_ChannelWidth           = 200,
        _Mst_Xgate2_PMOS_ChannelLength          = 30,
        _Mst_Xgate2_PMOS_XVT                    = 'SLVT',
        _Mst_Xgate2_PMOS_POGate_Comb_length     = 100,

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
    LayoutObj = _GetparamTest(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

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
# end of 'main():' ---------------------------------------------------------------------------------------------
