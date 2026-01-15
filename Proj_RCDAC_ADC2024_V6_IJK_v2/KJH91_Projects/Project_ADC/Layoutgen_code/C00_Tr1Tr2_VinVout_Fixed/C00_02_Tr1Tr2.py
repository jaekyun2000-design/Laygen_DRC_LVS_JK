
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

    ##
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.C00_Tr1Tr2_VinVout_Fixed import C00_00_Tr1
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.C00_Tr1Tr2_VinVout_Fixed import C00_01_Tr2


## Define Class
class _Tr1Tr2(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
# Input/Output node
    # INPUT node
    _Inputnode_width = 500,  # number
    # OUTPUT node
    _Outputnode_width = 500,  # number

# TR1
    # Physical dimension
    _Tr1_NumberofGate	= 12,       # Number
    _Tr1_ChannelWidth	            = 100,     # Number
    _Tr1_ChannelLength	            = 30,       # Number
    _Tr1_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR2
    # Physical dimension
    _Tr2_NumberofGate	= 5,       # Number
    _Tr2_ChannelWidth	            = 700,     # Number
    _Tr2_ChannelLength	            = 30,       # Number
    _Tr2_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

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
# Input/Output node
    # INPUT node
    _Inputnode_width = 500,  # number
    # OUTPUT node
    _Outputnode_width = 500,  # number

# TR1
    # Physical dimension
    _Tr1_NumberofGate	= 12,       # Number
    _Tr1_ChannelWidth	            = 100,     # Number
    _Tr1_ChannelLength	            = 30,       # Number
    _Tr1_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR2
    # Physical dimension
    _Tr2_NumberofGate	= 5,       # Number
    _Tr2_ChannelWidth	            = 700,     # Number
    _Tr2_ChannelLength	            = 30,       # Number
    _Tr2_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr1, nfettw
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Tr1, nfettw: Sref Gen.
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C00_00_Tr1._Tr1._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr1_NumberofGate']     =   _Tr1_NumberofGate
        _Caculation_Parameters['_Tr1_ChannelWidth']     =   _Tr1_ChannelWidth
        _Caculation_Parameters['_Tr1_ChannelLength']    =   _Tr1_ChannelLength
        _Caculation_Parameters['_Tr1_XVT']              =   _Tr1_XVT

        _Caculation_Parameters['_Inputnode_width']          =   _Inputnode_width
        _Caculation_Parameters['_Outputnode_width']         =   _Outputnode_width


                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Tr1'] = self._SrefElementDeclaration(_DesignObj=C00_00_Tr1._Tr1(_DesignParameter=None, _Name='{}:SRF_Tr1'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Tr1']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr1']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr1']['_XYCoordinates'] = [[0, 0]]


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr2, slvtnfettw
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Tr2, slvtnfettw: Sref Gen.
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C00_01_Tr2._Tr2._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr2_NumberofGate']     =   _Tr2_NumberofGate
        _Caculation_Parameters['_Tr2_ChannelWidth']     =   _Tr2_ChannelWidth
        _Caculation_Parameters['_Tr2_ChannelLength']    =   _Tr2_ChannelLength
        _Caculation_Parameters['_Tr2_XVT']              =   _Tr2_XVT

        _Caculation_Parameters['_Inputnode_width']      =   _Inputnode_width

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Tr2'] = self._SrefElementDeclaration(_DesignObj=C00_01_Tr2._Tr2(_DesignParameter=None, _Name='{}:SRF_Tr2'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Tr2']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr2']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr2']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr2']['_XYCoordinates'] = [[0, 0]]


                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Tr2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ## Targetx
        tmp1_1 = self.get_param_KJH4('SRF_Tr1','SRF_Nmos','BND_PODummyLayer')
        target_coordx = tmp1_1[0][0][0][0]['_XY_left'][0]
                                ## Targety
        tmp1_2 = self.get_param_KJH4('SRF_Tr1','SRF_Tr1_Source_ViaM1Mx','SRF_ViaM1M2','BND_Met1Layer')
        target_coordy = tmp1_2[0][0][0][0][0]['_XY_up'][1]
        target_coord = [target_coordx,target_coordy]

                            ## Approaching_coord: _XY_type2
                                ## approx
        tmp2_1 = self.get_param_KJH4('SRF_Tr2','SRF_Nmos','BND_PODummyLayer')
        approaching_coordx = tmp2_1[0][0][-1][0]['_XY_right'][0]
                                ## approy
        tmp2_2 = self.get_param_KJH4('SRF_Tr2','SRF_Tr2_Drain_ViaM1Mx','SRF_ViaM1M2','BND_Met1Layer')
        approaching_coordy = tmp2_2[0][0][0][0][0]['_XY_up'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Tr2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] - _DRCobj._PolygateMinSpace2
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Tr2']['_XYCoordinates'] = tmpXY

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
    libname = 'Proj_ZZ01_C00_02_Tr1Tr2_fixed'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'C00_02_Tr1Tr2_v0_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

# Input/Output node
    # INPUT node
    _Inputnode_width = 500,  # number
    # OUTPUT node
    _Outputnode_width = 500,  # number

# TR1
    # Physical dimension
    _Tr1_NumberofGate	            = 12,       # Number
    _Tr1_ChannelWidth	            = 100,     # Number
    _Tr1_ChannelLength	            = 30,       # Number
    _Tr1_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR2
    # Physical dimension
    _Tr2_NumberofGate	            = 5,       # Number
    _Tr2_ChannelWidth	            = 700,     # Number
    _Tr2_ChannelLength	            = 30,       # Number
    _Tr2_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

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
    LayoutObj = _Tr1Tr2(_DesignParameter=None, _Name=cellname)
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
