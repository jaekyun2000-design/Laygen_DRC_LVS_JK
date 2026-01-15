## Import Basic Modules
    ## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_ADC.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

    ## Library
import copy
import math
import numpy as np
import time
import pickle
import dill as pickle

    ## KJH91 Basic Building Blocks

    ## Building blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.H00_CDAC_v2_Fixed import H00_00_ECAP

############################################################################################################################################################ Class_HEADER
class _UCAP(StickDiagram_KJH1._StickDiagram_KJH):

    _ParametersForDesignCalculation = dict(
        # # Unit CDAC
        _LayoutOption=None,
        _MetalWidth=None,
        _MetalLength=None,
        _MetalSpacing=None,

        # #Unit Cap
        _NumOfElement=None,
    )
    # Initially Defined design_parameter
    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _Name=self._NameDeclaration(_Name=_Name),
                _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                _XYcoordAsCent=dict(_XYcoordAsCent=0),
            )

    ##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
    def _CalculateDesignParameter(self,
                                  # # Unit CDAC
                                  _LayoutOption=None,
                                  _MetalWidth=None,
                                  _MetalLength=None,
                                  _MetalSpacing=None,

                                  # #Unit Cap2
                                  _NumOfElement=None,

                                  ):

        ################################################################################################################################################## Class_HEADER: Pre Defined Parameter Before Calculation
        # Load DRC library
        _DRCobj = DRC.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ############################################################################################################################################################ CALCULATION START
        UCap_start_time = time.time()
        print('#########################################################################################################')
        print( '                                      Calculation Start                                                  ')
        print('#########################################################################################################')

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Sref Gen: Unit Capacitor(1C)
            ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(H00_00_ECAP._ECAP._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_LayoutOption'] = _LayoutOption
        _Caculation_Parameters['_MetalWidth'] = _MetalWidth
        _Caculation_Parameters['_MetalLength'] = _MetalLength
        _Caculation_Parameters['_MetalSpacing'] = _MetalSpacing

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_ECAP'] = self._SrefElementDeclaration(_DesignObj=H00_00_ECAP._ECAP(_DesignParameter=None, _Name='{}:SRF_ECAP'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_ECAP']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_ECAP']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_ECAP']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        self._DesignParameter['SRF_ECAP']['_XYCoordinates'] = [[0, 0]]

        # ## Coordinate cal origianl version
        # tmpXY=[[0,0]]
        # for i in range(_NumOfElement-1):
        #     ## Target_coord: _XY_type1
        #     tmp1 = self.get_param_KJH4('SRF_ECAP','BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
        #     target_coord = tmp1[i][1][0]['_XY_down_left']
        #     ## Approaching_coord: _XY_type2
        #     tmp2 = self.get_param_KJH4('SRF_ECAP','BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
        #     approaching_coord = tmp2[0][0][0]['_XY_down_left']
        #     ## Sref coord
        #     tmp3 = self.get_param_KJH4('SRF_ECAP')
        #     Scoord = tmp3[0][0]['_XY_origin']
        #     ## Cal
        #     New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        #     tmpXY.append(New_Scoord)
        #     ## Define coordinates
        #     self._DesignParameter['SRF_ECAP']['_XYCoordinates'] = tmpXY

        ## Coordinate cal revision1 : get_param 접근 횟수 줄여봄 근데 for 문을 그대로 씀, 약간 빠른듯.
        tmpXY2 = [[0, 0]]
        tmp1 = self.get_param_KJH4('SRF_ECAP', 'BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
        coord1 = tmp1[0][1][0]['_XY_down_left']
        tmp2 = self.get_param_KJH4('SRF_ECAP', 'BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
        coord2 = tmp2[0][0][0]['_XY_down_left']
        distance1 = coord1[0] - coord2[0]

        for i in range(1,_NumOfElement):
            tmpXY2.append([distance1 * i, 0])
        # _tmpXY2 = [[distance1 * i, 0] for i in range(1, _NumOfElement)]
        # tmpXY2.extend(_tmpXY2)
        ## Define coordinates
        self._DesignParameter['SRF_ECAP']['_XYCoordinates'] = tmpXY2

        # ## Coordinate cal revision2 : numpy써서 vector로 생성하는 방법 인데 안빠름.
        #     # Cal distance
        # tmp1 = self.get_param_KJH4('SRF_ECAP', 'BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
        # coord1 = tmp1[0][1][0]['_XY_down_left']
        # tmp2 = self.get_param_KJH4('SRF_ECAP', 'BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
        # coord2 = tmp2[0][0][0]['_XY_down_left']
        # distance1 = coord1[0] - coord2[0]
        #     # gen xcoord
        # vector1 = np.arange(5)
        # xcoord = vector1*distance1
        #     # gen ycoord
        # vector2 = np.zeros_like(vector1)
        #     # stack xy coord
        # tmpXY2 = np.stack((xcoord,vector2),axis=1)
        #     ## Define coordinates
        # self._DesignParameter['SRF_ECAP']['_XYCoordinates'] = tmpXY2


        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')
        UCap_end_time = time.time()
        self.UCap_elapsed_time = UCap_end_time - UCap_start_time



if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_ZZ01_H00_01_UCAP_Fixed'
    cellname = 'H00_00_UCAP_v1'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object ''' ############################################################### ^^^^^^^^^^^^^^^^^^^^^
    InputParams = dict(
        # # Element Cap
        _LayoutOption=[1],
        _MetalWidth=50,
        _MetalLength=1414,
        _MetalSpacing=50,

        # #Unit Cap
        _NumOfElement=20,
     )

    '''Mode_DRCCHECK '''

    Mode_DRCCheck = False
    Num_DRCCheck =1

    for ii in range(0, Num_DRCCheck if Mode_DRCCheck else 1):
        if Mode_DRCCheck:
            ''' Input Parameters for Layout Object '''
        else:
            pass

    ''' Generate Layout Object '''
    LayoutObj = _UCAP(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    ''' Check Time'''
    elapsed_time = time.time() - start_time
    m, s = divmod(elapsed_time,60)
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
    Checker.lib_deletion()
    #Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    #Checker_KJH0.DRCchecker()

    print ('#############################      Finished      ################################')
    print('{} Hours   {} minutes   {} seconds'.format(h, m, s))
    # end of 'main():' ---------------------------------------------------------------------------------------------