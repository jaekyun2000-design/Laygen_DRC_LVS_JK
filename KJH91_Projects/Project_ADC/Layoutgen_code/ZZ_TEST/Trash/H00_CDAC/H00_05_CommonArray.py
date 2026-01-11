## Import Basic Modules
    ## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

    ## Library
import copy
import math
import time

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.ZZ_TEST.Trash.H00_CDAC import H00_02_CapWithShielding


############################################################################################################################################################ Class_HEADER
class _CommonArray(StickDiagram_KJH1._StickDiagram_KJH):
    # Initially Defined design_parameter
    _ParametersForDesignCalculation = dict(
        _MetalType=None,
        _MetalWidth=None,
        _MetalLength=None,
        _Bitsize=None,
        _MSB=None,
    )

    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _Name=self._NameDeclaration(_Name=_Name),
                _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
            )

    ##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
    def _CalculateDesignParameter(self,
                                  # # Unit Capacitor (0.5fF)
                                  _MetalType=None,
                                  _MetalWidth=None,
                                  _MetalLength=None,
                                  _Bitsize=None,
                                  _MSB=None,
                                  ):

        ################################################################################################################################################## Class_HEADER: Pre Defined Parameter Before Calculation
        print('##     Pre Defined Parameter Before Calculation    ##')
        # Load DRC library
        _DRCobj = DRC.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ############################################################################################################################################################ CALCULATION START
        print(
            '#########################################################################################################')
        print(
            '                                      Calculation Start                                                  ')
        print(
            '#########################################################################################################')

        Total_Bitsize1 = int(math.pow(2,_Bitsize))
        _CapSpacing = 50
        target_xcoord= 0
        total_bit = _Bitsize
        if _MSB == 2  :
            ## Generation of MSB bit Array (Common centroid layout Roughting)
            for i in range( 0 , int(Total_Bitsize1)) :
                   ## SREF Generation
                        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
                _Caculation_Parameters = copy.deepcopy(
                    H00_02_CapWithShielding._CapWithShielding._ParametersForDesignCalculation)
                        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
                _Caculation_Parameters['_MetalType'] = _MetalType
                _Caculation_Parameters['_MetalWidth'] = _MetalWidth
                _Caculation_Parameters['_MetalLength'] = _MetalLength

                        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
                self._DesignParameter['SRF_CDAC_B'+str(_Bitsize)+'_VTC'+str(i)+'_M'+str(_MetalType)] = self._SrefElementDeclaration(_DesignObj=H00_02_CapWithShielding._CapWithShielding(_DesignParameter=None, _Name='{}:SRF_CDAC_B{}_VTC{}_M{}'.format(_Name, _Bitsize, i, _MetalType)))[0]

                        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
                self._DesignParameter['SRF_CDAC_B'+str(_Bitsize)+'_VTC'+str(i)+'_M'+str(_MetalType)]['_Reflect'] = [0, 0, 0]

                        ## Define Sref Angle: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_CDAC_B'+str(_Bitsize)+'_VTC'+str(i)+'_M'+str(_MetalType)]['_Angle'] = 0

                        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_CDAC_B'+str(_Bitsize)+'_VTC'+str(i)+'_M'+str(_MetalType)]['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_CDAC_B'+str(_Bitsize)+'_VTC'+str(i)+'_M'+str(_MetalType)]['_XYCoordinates'] = [[target_xcoord,0]]
                            ##Calculation of each unit cap coordinates
                target_xcoord = self.get_outter_KJH4('SRF_CDAC_B'+str(_Bitsize)+'_VTC'+str(i)+'_M'+str(_MetalType))['_Mostright']['coord'][0] - _MetalWidth

                # tmp1 = self.get_param_KJH4('SRF_CDAC_B'+str(_Bitsize)+'_VTC'+str(i)+'_M'+str(_MetalType),'SRF_CapWShield_A0',,'BND_UCAP_TRIGHT_VTC_M'+str(_MetalType))
                # target_coord = tmp1[0][0][0]['_XY_down_left']
                if i == 0: utmp= target_xcoord # store distance of unit cap
                target_xcoord = target_xcoord + utmp
            _Bitsize=_Bitsize-1
            _MSB = _MSB-1

        if _MSB == 1 :
            Total_Bitsize2 = int(math.pow(2, _Bitsize))
            for j in range(0,int(Total_Bitsize2/2)) :

                    ## SREF Generation
                    ##Generate LEFT half part
                        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
                _Caculation_Parameters = copy.deepcopy(
                    H00_02_CapWithShielding._CapWithShielding._ParametersForDesignCalculation)
                        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
                _Caculation_Parameters['_MetalType'] = _MetalType
                _Caculation_Parameters['_MetalWidth'] = _MetalWidth
                _Caculation_Parameters['_MetalLength'] = _MetalLength

                        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
                self._DesignParameter['SRF_CDAC_B'+str(_Bitsize)+'_VTC'+str(j)+'_M'+str(_MetalType)] = self._SrefElementDeclaration(_DesignObj=H00_02_CapWithShielding._CapWithShielding(_DesignParameter=None, _Name='{}:SRF_CDAC_B{}_VTC{}_M{}'.format(_Name, _Bitsize, j, _MetalType)))[0]

                        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
                self._DesignParameter['SRF_CDAC_B'+str(_Bitsize)+'_VTC'+str(j)+'_M'+str(_MetalType)]['_Reflect'] = [0, 0, 0]

                        ## Define Sref Angle: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_CDAC_B'+str(_Bitsize)+'_VTC'+str(j)+'_M'+str(_MetalType)]['_Angle'] = 0

                        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_CDAC_B'+str(_Bitsize)+'_VTC'+str(j)+'_M'+str(_MetalType)]['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
                target_coord_left = self.get_outter_KJH4('SRF_CDAC_B'+str(_Bitsize+1)+'_VTC'+str(j)+'_M'+str(_MetalType))['_Mostright']['coord'][0] - _MetalWidth
                self._DesignParameter['SRF_CDAC_B'+str(_Bitsize)+'_VTC'+str(j)+'_M'+str(_MetalType)]['_XYCoordinates'] = [[target_coord_left,0]]


                _Caculation_Parameters = copy.deepcopy(
                    H00_02_CapWithShielding._CapWithShielding._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
                _Caculation_Parameters['_MetalType'] = _MetalType
                _Caculation_Parameters['_MetalWidth'] = _MetalWidth
                _Caculation_Parameters['_MetalLength'] = _MetalLength

                ##Generate Right half part
                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
                self._DesignParameter['SRF_CDAC_B' + str(_Bitsize) + '_VTC' + str(Total_Bitsize2 - j - 1) + '_M' + str(_MetalType)] = self._SrefElementDeclaration(_DesignObj=H00_02_CapWithShielding._CapWithShielding(_DesignParameter=None,
                                                                                                                                                                                                                        _Name='{}:SRF_CDAC_B{}_VTC{}_M{}'.format(_Name, _Bitsize, Total_Bitsize2 - j - 1, _MetalType)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
                self._DesignParameter['SRF_CDAC_B' + str(_Bitsize) + '_VTC' + str(Total_Bitsize2 - j - 1) + '_M' + str(_MetalType)]['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_CDAC_B' + str(_Bitsize) + '_VTC' + str(Total_Bitsize2 - j - 1) + '_M' + str(_MetalType)]['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_CDAC_B' + str(_Bitsize) + '_VTC' + str(Total_Bitsize2 - j - 1) + '_M' + str(_MetalType)][
                    '_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
                target_coord_right = self.get_outter_KJH4('SRF_CDAC_B'+str(_Bitsize+1)+'_VTC'+str(int(Total_Bitsize1-j-2))+'_M'+str(_MetalType))['_Mostright']['coord'][0] - _MetalWidth
                # target_coord_right=tmp3[0][0][0]['_XY_down_left']
                self._DesignParameter['SRF_CDAC_B' + str(_Bitsize) + '_VTC' + str(Total_Bitsize2 - j - 1) + '_M' + str(_MetalType)]['_XYCoordinates'] = [[target_coord_right,0]]

            _Bitsize=_Bitsize-1
            tmp_Bitsize=_Bitsize
            if _Bitsize>=1 :
                for l in range(tmp_Bitsize) : #Bit 수만큼 iteration. 0,1
                    total_bitsize = int(pow(2, _Bitsize)) #각 bit의 metal 개수 계산 절반으로 나누기.
                    tmp_num=int(total_bitsize/2) #절반으로 나누기.
                    for k in range(int(total_bitsize/2)) :  #metal 개수의 절반만큼 iteration. 각 iteration 마다 양 끝 pair metal 생성.
                        _Caculation_Parameters = copy.deepcopy(
                            H00_02_CapWithShielding._CapWithShielding._ParametersForDesignCalculation)
                        _Caculation_Parameters['_MetalType'] = _MetalType
                        _Caculation_Parameters['_MetalWidth'] = _MetalWidth
                        _Caculation_Parameters['_MetalLength'] = _MetalLength

                        ##Generate Left half part
                        self._DesignParameter['SRF_CDAC_B' + str(_Bitsize) + '_VTC' + str(k) + '_M' + str(_MetalType)] = self._SrefElementDeclaration(_DesignObj=H00_02_CapWithShielding._CapWithShielding(_DesignParameter=None,
                                                                                                                                                                                                           _Name='{}:SRF_CDAC_B{}_VTC{}_M{}'.format(
                                                                                      _Name, _Bitsize, k, _MetalType)))[0]
                        self._DesignParameter['SRF_CDAC_B' + str(_Bitsize) + '_VTC' + str(k) + '_M' + str(_MetalType)]['_Reflect'] = [0, 0, 0]

                        self._DesignParameter['SRF_CDAC_B' + str(_Bitsize) + '_VTC' + str(k) + '_M' + str(_MetalType)]['_Angle'] = 0

                        self._DesignParameter['SRF_CDAC_B' + str(_Bitsize) + '_VTC' + str(k) + '_M' + str(_MetalType)]['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                            ##Calculate Left half part coordinates
                        target_coord_left = self.get_outter_KJH4('SRF_CDAC_B' + str(total_bit) + '_VTC' + str( int(Total_Bitsize1/2) - total_bitsize + k ) + '_M' + str(_MetalType))['_Mostright']['coord'][0] - _MetalWidth

                        # target_coord_left = tmp2[0][0][0]['_XY_down_left']
                        self._DesignParameter['SRF_CDAC_B' + str(_Bitsize) + '_VTC' + str(k) + '_M' + str(_MetalType)]['_XYCoordinates'] = [[target_coord_left,0]]

                        ##Generate Right half part
                        self._DesignParameter['SRF_CDAC_B' + str(_Bitsize) + '_VTC' + str(total_bitsize-k-1) + '_M' + str(_MetalType)] = self._SrefElementDeclaration(_DesignObj=H00_02_CapWithShielding._CapWithShielding(_DesignParameter=None, _Name='{}:SRF_CDAC_B{}_VTC{}_M{}'.format(_Name, _Bitsize, total_bitsize - k - 1, _MetalType)))[0]

                        self._DesignParameter['SRF_CDAC_B' + str(_Bitsize) + '_VTC' + str(total_bitsize-k-1) + '_M' + str(_MetalType)]['_Reflect'] = [0, 0, 0]

                        self._DesignParameter['SRF_CDAC_B' + str(_Bitsize) + '_VTC' + str(total_bitsize-k-1) + '_M' + str(_MetalType)]['_Angle'] = 0

                        self._DesignParameter['SRF_CDAC_B' + str(_Bitsize) + '_VTC' + str(total_bitsize-k-1) + '_M' + str(_MetalType)]['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)
                        target_coord_right = self.get_outter_KJH4('SRF_CDAC_B' + str(total_bit) + '_VTC' + str(int(Total_Bitsize1/2) + total_bitsize - 2 - k) + '_M' + str(_MetalType))['_Mostright']['coord'][0] - _MetalWidth
                        # target_coord_right = tmp3[0][0][0]['_XY_down_left']
                        self._DesignParameter['SRF_CDAC_B' + str(_Bitsize) + '_VTC' + str(total_bitsize-k-1) + '_M' + str(_MetalType)]['_XYCoordinates'] = [[target_coord_right,0]]
                    _Bitsize = _Bitsize - 1

                ##Generate LSB Metal
                _Caculation_Parameters = copy.deepcopy(
                    H00_02_CapWithShielding._CapWithShielding._ParametersForDesignCalculation)
                _Caculation_Parameters['_MetalType'] = _MetalType
                _Caculation_Parameters['_MetalWidth'] = _MetalWidth
                _Caculation_Parameters['_MetalLength'] = _MetalLength

                self._DesignParameter['SRF_CDAC_B0_VTC0_M' + str(_MetalType)] = self._SrefElementDeclaration(_DesignObj=H00_02_CapWithShielding._CapWithShielding(_DesignParameter=None,
                                                                                                                                                                  _Name='{}:SRF_CDAC_B0_VTC0_M{}'.format(
                                                                              _Name, _MetalType)))[0]
                self._DesignParameter['SRF_CDAC_B0_VTC0_M' + str(_MetalType)]['_Reflect'] = [0, 0, 0]

                self._DesignParameter['SRF_CDAC_B0_VTC0_M' + str(_MetalType)]['_Angle'] = 0

                self._DesignParameter['SRF_CDAC_B0_VTC0_M' + str(_MetalType)]['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ##Calculate LSB part coordinates
                target_coord = self.get_outter_KJH4('SRF_CDAC_B' + str(total_bit) + '_VTC' + str(
                    int(Total_Bitsize1 / 2) - 1) + '_M' + str(_MetalType))['_Mostright']['coord'][0] - _MetalWidth

                self._DesignParameter['SRF_CDAC_B0_VTC0_M' + str(_MetalType)]['_XYCoordinates'] = [[target_coord,0]]



############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_ADC_H00_07_CDACSIM'
    cellname = 'H00_00_driver_v05'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object ''' ############################################################### ^^^^^^^^^^^^^^^^^^^^^
    InputParams = dict(
        # # Unit CDAC
        _MetalType=6, #Poly:0, M1:1, M2:2 ...
        _MetalWidth=50,
        _MetalLength=1414,
        # _MetalNumber=3,
        _Bitsize=3,
        _MSB=2,
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
    #Checker.lib_deletion()
    #Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    #Checker_KJH0.DRCchecker()

    ''' Check Time'''
    elapsed_time = time.time() - start_time
    m, s = divmod(elapsed_time,60)
    h, m = divmod(m, 60)


    print ('#############################      Finished      ################################')
    # end of 'main():' ---------------------------------------------------------------------------------------------