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

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.H00_CDAC_v2 import H00_02_CapWithShield
from KJH91_Projects.Project_ADC.Layoutgen_code.H00_CDAC_v2 import H00_03_DummyCapUnit

############################################################################################################################################################ Class_HEADER
class _CommonArray(StickDiagram_KJH1._StickDiagram_KJH):
    # Initially Defined design_parameter
    _ParametersForDesignCalculation = dict(
        # # Unit CDAC
        _LayoutOption=None,
        _ShieldingLayer=None,  # Poly:0, M1:1, M2:2 ...
        _MetalWidth=None,
        _MetalLength=None,
        _MetalSpacing=None,

        # #Unit Cap
        _NumOfElement=None,

        # # Shielding & Top Connect node
        _ConnectLength=None,
        _ExtendLength=None,
        _Bitsize=None,

        # # Dummy Cap Option
        _DummyCap_TopBottomShort=None,
        _NumOfDummyCaps=None,  # Number of dummy cap(one side)
    )

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
                                  # # Unit Capacitor (0.5fF)
                                  # # Unit CDAC
                                  _LayoutOption=None,
                                  _ShieldingLayer=None,# Poly:0, M1:1, M2:2 ...
                                  _MetalWidth=None,
                                  _MetalLength=None,
                                  _MetalSpacing=None,

                                  # #Unit Cap
                                  _NumOfElement=None,

                                  # # Shielding & Top Connect node
                                  _ConnectLength=None,
                                  _ExtendLength=None,
                                  _Bitsize=None,

                                  # # Dummy Cap Option
                                  _DummyCap_TopBottomShort=None,
                                  _NumOfDummyCaps=None,  # Number of dummy cap(one side)
                                  ):

        ################################################################################################################################################## Class_HEADER: Pre Defined Parameter Before Calculation
        # Load DRC library
        _DRCobj = DRC.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ############################################################################################################################################################ CALCULATION START
        CommonArray_start_time = time.time()
        print(
            '#########################################################################################################')
        print(
            '                                      Calculation Start                                                  ')
        print(
            '#########################################################################################################')

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Cap Array Gen: Common-Centroid Method
        # Capsize = 2 ** (_Bitsize)

        ## SREF Generation
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(H00_02_CapWithShield._CapWithShield._ParametersForDesignCalculation)
        _Caculation_Parameters['_LayoutOption'] = _LayoutOption
        _Caculation_Parameters['_ShieldingLayer'] = _ShieldingLayer
        _Caculation_Parameters['_MetalWidth'] = _MetalWidth
        _Caculation_Parameters['_MetalLength'] = _MetalLength
        _Caculation_Parameters['_MetalSpacing'] = _MetalSpacing

        _Caculation_Parameters['_NumOfElement'] = _NumOfElement

        _Caculation_Parameters['_ConnectLength'] = _ConnectLength
        _Caculation_Parameters['_ExtendLength'] = _ExtendLength

        # for i in range(_Bitsize) :
        #     ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        #     self._DesignParameter['SRF_CDAC_B{}'.format(_Bitsize-i-1)] = self._SrefElementDeclaration(_DesignObj=H00_02_CapWithShield._CapWithShield(_DesignParameter=None, _Name='{}:SRF_CDAC_B{}'.format(_Name, _Bitsize-i-1)))[0]
        #
        #     ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        #     self._DesignParameter['SRF_CDAC_B{}'.format(_Bitsize-i-1)]['_Reflect'] = [0, 0, 0]
        #
        #     ## Define Sref Angle: ex)'_NMOS_POWER'
        #     self._DesignParameter['SRF_CDAC_B{}'.format(_Bitsize-i-1)]['_Angle'] = 0
        #
        #     ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        #     self._DesignParameter['SRF_CDAC_B{}'.format(_Bitsize-i-1)]['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)
        #
        #     ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        #     self._DesignParameter['SRF_CDAC_B{}'.format(_Bitsize-i-1)]['_XYCoordinates'] = [[0, 0]]

        # # Revision1 version : 원래 코드가 이상했어서 위에거 주석처리한게 전부인데 속도 개빨라짐
        # for i in range(_Bitsize):
        #     _CapSize = 2 ** (_Bitsize - i - 1)
        #     print('#########################################')
        #     print('##    {}C Driver Calculation_Start     ##'.format(_CapSize))
        #     print('#########################################')
        #
        #     ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        #     self._DesignParameter['SRF_CDAC_B{}'.format(_Bitsize - i - 1)] = self._SrefElementDeclaration(_DesignObj=H00_02_CapWithShield._CapWithShield(_DesignParameter=None,_Name='{}:SRF_CDAC_B{}'.format(_Name, _Bitsize - i - 1)))[0]
        #
        #     ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        #     self._DesignParameter['SRF_CDAC_B{}'.format(_Bitsize - i - 1)]['_Reflect'] = [0, 0, 0]
        #
        #     ## Define Sref Angle: ex)'_NMOS_POWER'
        #     self._DesignParameter['SRF_CDAC_B{}'.format(_Bitsize - i - 1)]['_Angle'] = 0
        #
        #     ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        #     self._DesignParameter['SRF_CDAC_B{}'.format(_Bitsize - i - 1)]['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)
        #
        #     ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        #     self._DesignParameter['SRF_CDAC_B{}'.format(_Bitsize - i - 1)]['_XYCoordinates'] = [[0, 0]]
        #
        #     tmp1 = self.get_param_KJH4('SRF_CDAC_B{}'.format(_Bitsize-i-1), 'SRF_UCAP', 'SRF_ECAP', 'BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
        #     _CapLength = abs(tmp1[0][0][-1][-1][0]['_XY_right'][0] - tmp1[0][0][0][0][0]['_XY_right'][0])
        #     # tmp2 = self.get_param_KJH4()
        #     tmpXY = []
        #     for j in range(_CapSize):
        #         # 시작점 : ((2 ** i) * DistanceBtwTr)
        #         # 복사/붙혀넣기 간격 : j * (2 ** (i+1)) * DistanceBtwTr
        #         tmp = [j * (2 ** (i + 1)) * _CapLength + ((2 ** i) * _CapLength), 0]
        #         tmpXY.append(tmp)
        #
        #     # Define coord
        #     self._DesignParameter['SRF_CDAC_B{}'.format(_Bitsize - i - 1)]['_XYCoordinates'] = tmpXY


        # Revision2 version: Rename으로 시간단축
        for i in range(_Bitsize):
            _CapSize = 2 ** (_Bitsize - i - 1)
            print('#########################################')
            print('##    {}C Driver Calculation_Start     ##'.format(_CapSize))
            print('#########################################')

            if i ==0:
                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
                self._DesignParameter['SRF_CDAC_B{}'.format(_Bitsize - i - 1)] = self._SrefElementDeclaration(_DesignObj=H00_02_CapWithShield._CapWithShield(_DesignParameter=None,_Name='{}:SRF_CDAC_B{}'.format(_Name, _Bitsize - i - 1)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
                self._DesignParameter['SRF_CDAC_B{}'.format(_Bitsize - i - 1)]['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_CDAC_B{}'.format(_Bitsize - i - 1)]['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_CDAC_B{}'.format(_Bitsize - i - 1)]['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)
            else:
                self._DesignParameter['SRF_CDAC_B{}'.format(_Bitsize - i - 1)] = copy.deepcopy(self._DesignParameter['SRF_CDAC_B{}'.format(_Bitsize - 0 - 1)])
                self.rename_srf_prefix(self._DesignParameter['SRF_CDAC_B{}'.format(_Bitsize - i - 1)], 'SRF_CDAC_B{}'.format(_Bitsize - 0 - 1), 'SRF_CDAC_B{}'.format(_Bitsize - i - 1))

            ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CDAC_B{}'.format(_Bitsize - i - 1)]['_XYCoordinates'] = [[0, 0]]

            tmp1 = self.get_param_KJH4('SRF_CDAC_B{}'.format(_Bitsize-i-1), 'SRF_UCAP', 'SRF_ECAP', 'BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
            _CapLength = abs(tmp1[0][0][-1][-1][0]['_XY_right'][0] - tmp1[0][0][0][0][0]['_XY_right'][0])
            # tmp2 = self.get_param_KJH4()
            tmpXY = []
            for j in range(_CapSize):
                # 시작점 : ((2 ** i) * DistanceBtwTr)
                # 복사/붙혀넣기 간격 : j * (2 ** (i+1)) * DistanceBtwTr
                tmp = [j * (2 ** (i + 1)) * _CapLength + ((2 ** i) * _CapLength), 0]
                tmpXY.append(tmp)

            # Define coord
            self._DesignParameter['SRF_CDAC_B{}'.format(_Bitsize - i - 1)]['_XYCoordinates'] = tmpXY

        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')
        CommonArray_end_time = time.time()
        self.CommonArray_elapsed_time = CommonArray_end_time - CommonArray_start_time

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_ZZ00_RcdacSar_H00_04_CommonArrary'
    cellname = 'H00_00_CommonArray_v3'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object ''' ############################################################### ^^^^^^^^^^^^^^^^^^^^^
    InputParams = dict(
        # # Element CDAC
        _LayoutOption=[3,4],
        _ShieldingLayer=1,  # Poly:0, M1:1, M2:2 ...
        _MetalWidth=50,
        _MetalLength=1414,
        _MetalSpacing=50,

        # #Unit Cap
        _NumOfElement=2,

        # # Shielding & Top Connect node
        _ConnectLength=400,
        _ExtendLength=400,

        # # CommonCentroid Array
        _Bitsize=6,

        # # Dummy Cap Option
        _DummyCap_TopBottomShort=True,
        _NumOfDummyCaps=3,  # Number of dummy cap(one side)
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
    LayoutObj = _CommonArray(_DesignParameter=None, _Name=cellname)
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

    print('##########'
          '#####      Sending to FTP Server...      ##################')
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