## Import Basic Modules
    ## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

    ## Library
import copy
import time

    ## KJH91 Basic Building Blocks

    ## Building blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.ZZ_TEST.Trash.H00_CDAC import H00_00_UCAP


############################################################################################################################################################ Class_HEADER
class _CArray(StickDiagram_KJH1._StickDiagram_KJH):

    _ParametersForDesignCalculation = dict(
        _MetalType=None,
        _MetalWidth=None,
        _MetalLength=None,
        # _MetalNumber=None,
    )
    # Initially Defined design_parameter
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
                                  # # Unit CDAC
                                  _MetalType=None,
                                  _MetalWidth=None,
                                  _MetalLength=None,
                                  # _MetalNumber=None,
                                  ):

        ################################################################################################################################################## Class_HEADER: Pre Defined Parameter Before Calculation
        print('##     Pre Defined Parameter Before Calculation    ##')
        # Load DRC library
        _DRCobj = DRC.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ############################################################################################################################################################ CALCULATION START
        print('#########################################################################################################')
        print( '                                      Calculation Start                                                  ')
        print('#########################################################################################################')

        ## Generation of CapArray
            ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(H00_00_UCAP._UCAP._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_MetalType'] = _MetalType
        _Caculation_Parameters['_MetalWidth'] = _MetalWidth
        _Caculation_Parameters['_MetalLength'] = _MetalLength
        _MetalNumber = 2
        target_coord = [0, 0] #Initial coordinates of CapArray
        for i in range(_MetalNumber) :
                    ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
            self._DesignParameter['SRF_CArray_UCAP_VTC_C'+str(i)] = self._SrefElementDeclaration(_DesignObj=H00_00_UCAP._UCAP(_DesignParameter=None, _Name='{}:SRF_CArray_UCAP_VTC_C{}'.format(_Name, i)))[0]

                    ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
            self._DesignParameter['SRF_CArray_UCAP_VTC_C'+str(i)]['_Reflect'] = [0, 0, 0]

                    ## Define Sref Angle: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CArray_UCAP_VTC_C'+str(i)]['_Angle'] = 0

                    ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CArray_UCAP_VTC_C'+str(i)]['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                    ## Define Sref _XYcoordinate
                        #Calculating the each unit-capacitors coordinates
            self._DesignParameter['SRF_CArray_UCAP_VTC_C'+str(i)]['_XYCoordinates'] = [target_coord]
            tmp1 = self.get_param_KJH4('SRF_CArray_UCAP_VTC_C'+str(i) , 'BND_UCAP_TRIGHT_VTC_M' + str(_MetalType))
            target_coord = tmp1[0][0][0]['_XY_down_left']


        ##Generation of Covering metal 1 (Shielding upper side e.g: M7 Cover Generation for CapArray consisted of M6)
            ## Boundary_element Generation
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CArray_COVER_VTC_M'+str(_MetalType+1)] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL' + str(_MetalType + 1)][0],
            _Datatype=DesignParameters._LayerMapping['METAL' + str(_MetalType + 1)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_CArray_COVER_VTC_M'+str(_MetalType+1)]['_YWidth'] = _MetalLength

                ## Define Boundary_element _XWidth
                    ##Calculate the covering metal width
        tmp2 = self.get_param_KJH4('SRF_CArray_UCAP_VTC_C0', 'BND_UCAP_TLEFT_VTC_M' + str(_MetalType))
        target_coord = tmp2[0][0][0]['_XY_down_left']
        tmp3 = self.get_param_KJH4('SRF_CArray_UCAP_VTC_C' + str(_MetalNumber - 1) , 'BND_UCAP_TRIGHT_VTC_M' + str(_MetalType))
        target_coord2 = tmp3[0][0][0]['_XY_down_right']
        target_width = abs(target_coord[0] - target_coord2[0])

        self._DesignParameter['BND_CArray_COVER_VTC_M'+str(_MetalType+1)]['_XWidth'] = target_width

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CArray_COVER_VTC_M'+str(_MetalType+1)]['_XYCoordinates'] = [[0, 0]]

        ##Generation of Covering Metal 2 (Shielding lower side)
        self._DesignParameter['BND_CArray_COVER_VTC_M'+str(_MetalType-2)] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL' + str(_MetalType - 2)][0],
            _Datatype=DesignParameters._LayerMapping['METAL' + str(_MetalType - 2)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_CArray_COVER_VTC_M'+str(_MetalType-2)]['_YWidth'] = _MetalLength

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CArray_COVER_VTC_M'+str(_MetalType-2)]['_XWidth'] = target_width

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CArray_COVER_VTC_M'+str(_MetalType-2)]['_XYCoordinates'] = [[0, 0]]

        # # Driving node connecting
        # for i in range(_MetalNumber) :
        #     self._DesignParameter['BND_CArray_DriverM'+str(i)+'_VTC_M' + str(_MetalType)] = self._BoundaryElementDeclaration(
        #         _Layer=DesignParameters._LayerMapping['METAL' + str(_MetalType)][0],
        #         _Datatype=DesignParameters._LayerMapping['METAL' + str(_MetalType)][1],
        #         _XWidth=None,
        #         _YWidth=None,
        #         _XYCoordinates=[],
        #     )
        #     ## Define Boundary_element _YWidth
        #     self._DesignParameter['BND_CArray_DriverM'+str(i)+'_VTC_M' + str(_MetalType)]['_YWidth'] = 458
        #
        #     ## Define Boundary_element _XWidth
        #     self._DesignParameter['BND_CArray_DriverM'+str(i)+'_VTC_M' + str(_MetalType)]['_XWidth'] = _MetalWidth
        #
        #     ## Define Boundary_element _XYCoordinates
        #     tmp3 = self.get_param_KJH4('SRF_CArray_UCAP_VTC_C'+str(i), 'BND_UCAP_Bottom_VTC_M' + str(_MetalType))
        #     target_coord=tmp3[0][0][0]['_XY_down_left']
        #     target_coord[1]=target_coord[1] - 458
        #     self._DesignParameter['BND_CArray_DriverM'+str(i)+'_VTC_M' + str(_MetalType)]['_XYCoordinates'] = [target_coord]
        #
        # self._DesignParameter[ 'BND_CArray_Driver_HRZ_M' + str(_MetalType)] = self._BoundaryElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL' + str(_MetalType)][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL' + str(_MetalType)][1],
        #     _XWidth=None,
        #     _YWidth=None,
        #     _XYCoordinates=[],
        # )
        # ## Define Boundary_element _YWidth
        # self._DesignParameter['BND_CArray_Driver_HRZ_M' + str(_MetalType)]['_YWidth'] = 200
        #
        # ## Define Boundary_element _XWidth
        #     ## Calculation of XWidth
        # tmp3 = self.get_param_KJH4('SRF_CArray_UCAP_VTC_C0' , 'BND_UCAP_Bottom_VTC_M' + str(_MetalType))
        # target_coord2= tmp3[0][0][0]['_XY_down_left']
        # tmp4= self.get_param_KJH4('SRF_CArray_UCAP_VTC_C'+str(_MetalNumber-1) , 'BND_UCAP_Bottom_VTC_M' + str(_MetalType))
        # target_coord3= tmp4[0][0][0]['_XY_down_right']
        # target_width= abs(target_coord3[0] - target_coord2[0])
        # self._DesignParameter['BND_CArray_Driver_HRZ_M' + str(_MetalType)]['_XWidth'] = target_width
        #
        # ## Define Boundary_element _XYCoordinates
        # tmp3 = self.get_param_KJH4('BND_CArray_DriverM0_VTC_M' + str(_MetalType))
        # target_coord2= tmp3[0][0]['_XY_down_left']
        # target_coord2[1]=target_coord2[1]-200
        # self._DesignParameter['BND_CArray_Driver_HRZ_M' + str(_MetalType)]['_XYCoordinates'] = [target_coord2]

if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_KJB
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'H00_03_CDAC'
    cellname = 'H00_00_driver_v0_4'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object ''' ############################################################### ^^^^^^^^^^^^^^^^^^^^^
    InputParams = dict(
        # # Unit CDAC
        _MetalType=6, #Poly:0, M1:1, M2:2 ...
        _MetalWidth=50,
        _MetalLength=1414,
        # _MetalNumber=2,
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
    LayoutObj = _CArray(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('###############      Sending to FTP Server...      ##################')
    My = MyInfo_KJB.USER(DesignParameters._Technology)
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