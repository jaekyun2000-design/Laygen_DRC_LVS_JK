## Import Basic Modules
    ## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

    ## Library
import copy
import time

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.ZZ_TEST.Trash.H00_CDAC import H00_05_CommonArray


############################################################################################################################################################ Class_HEADER
class _CommonCentroid(StickDiagram_KJH1._StickDiagram_KJH):
    # Initially Defined design_parameter
    _ParametersForDesignCalculation = dict(
        _MetalType=None,
        _MetalWidth=None,
        _MetalLength=None,
        _numberOfBit=None,
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
                                  _numberOfBit=None,
                                  _DriverLength=None
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
        ## Generate M-bit CDAC using CommonCentroid
            ## SREF Generation
        _Caculation_Parameters = copy.deepcopy(H00_05_CommonArray._CommonArray._ParametersForDesignCalculation)
        _Caculation_Parameters['_MetalType'] = _MetalType
        _Caculation_Parameters['_MetalWidth'] = _MetalWidth
        _Caculation_Parameters['_MetalLength'] = _MetalLength
        _Caculation_Parameters['_Bitsize'] = _numberOfBit
        _Caculation_Parameters['_MSB'] = 2

            ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_CDAC_B'+str(_numberOfBit)+'_M'+str(_MetalType)] = self._SrefElementDeclaration(_DesignObj=H00_05_CommonArray._CommonArray(_DesignParameter=None, _Name='{}:SRF_CDAC_B{}_M{}'.format(_Name, _numberOfBit, _MetalType)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_CDAC_B'+str(_numberOfBit)+'_M'+str(_MetalType)]['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CDAC_B'+str(_numberOfBit)+'_M'+str(_MetalType)]['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CDAC_B'+str(_numberOfBit)+'_M'+str(_MetalType)]['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CDAC_B'+str(_numberOfBit)+'_M'+str(_MetalType)]['_XYCoordinates'] = [[0, 0]]

        ##Generate Driving node, if n bit then n-number of driving node generation
            ##Selecting Driver node information.
        _DriverMetal = 5
        _DriverMetalType = 'METAL'+str(5)
        _CapDriverDistance = 100 # select Arbitarily
        _NodeDistance= 60 #_DRCobj._Metal1MinWidth
        _DriverWidth= 50


            ##Generate n-number of Horizental driver node
        for i in range(_numberOfBit+1) :
            self._DesignParameter['BND_CDAC_Driver'+str(_numberOfBit-i)+'_Hrz_M' + str(_MetalType)] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[_DriverMetalType][0],
            _Datatype=DesignParameters._LayerMapping[_DriverMetalType][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
            ## Define Boundary_element _YWidth
            self._DesignParameter['BND_CDAC_Driver'+str(_numberOfBit-i)+'_Hrz_M' + str(_MetalType)]['_YWidth'] = _DriverWidth

            ## Define Boundary_element _XWidth

            self._DesignParameter['BND_CDAC_Driver'+str(_numberOfBit-i)+'_Hrz_M' + str(_MetalType)]['_XWidth'] =

            ## Define Boundary_element _XYCoordinates
                ##Calculate each n-Driver coordinates
            # tmp_y = self.get_outter_KJH4('SRF_CDAC_B'+str(_numberOfBit)+'_M'+str(_MetalType))['_Mostdown']['coord'][1]
            if i == 0 :
                tmp_y = self.get_outter_KJH4('SRF_CDAC_B' + str(_numberOfBit) + '_M' + str(_MetalType))['_Mostdown']['coord']
                Drive_y = tmp_y[1] - (_CapDriverDistance + _DriverWidth)
            else :
                tmp1 = self.get_outter_KJH4('SRF_CDAC_B'+str(_numberOfBit-i+1)+'_VIA0_V0')['_Mostdown']['coord'][1]
                Drive_y = tmp1 - ( _NodeDistance + _MetalWidth)

            self._DesignParameter['BND_CDAC_Driver'+str(_numberOfBit-i)+'_Hrz_M' + str(_MetalType)]['_XYCoordinates'] = [ [0, Drive_y ] ]
            _numOfMetal = int(pow(2, _numberOfBit-i))






            for j in range(_numOfMetal) :#각 BIT의 Metal수만큼 iteration 한 후 driving node에 연결시키기
                for k in range(2): # 각 cap마다 2개의 drive node를 가지고 있음.
                    self._DesignParameter['BND_CDAC_B'+str(_numberOfBit-i)+'_Connect' + str(j) + '_VTC'+str(k)+'_M' + str(_MetalType)] = self._BoundaryElementDeclaration(
                        _Layer=DesignParameters._LayerMapping['METAL' + str(_MetalType)][0],
                        _Datatype=DesignParameters._LayerMapping['METAL' + str(_MetalType)][1],
                        _XWidth=None,
                        _YWidth=None,
                        _XYCoordinates=[],
                    )
                    # Define Boundary_element _YWidth
                                ## Calculate YWidth of connecting node
                    tmp1= self.get_param_KJH4('BND_CDAC_Driver'+str(_numberOfBit-i)+'_Hrz_M'+str(_MetalType))
                    target_coord = tmp1[0][0]['_XY_down_left']
                    tmp2= self.get_param_KJH4('SRF_CDAC_B'+str(_numberOfBit)+'_M'+str(_MetalType),'SRF_CDAC_B'+str(_numberOfBit-i)+'_VTC'+str(j)+'_M'+str(_MetalType),'SRF_CapWShield_A0','SRF_CArray_UCAP_VTC_C'+str(k),'BND_UCAP_Bottom_VTC_M'+str(_MetalType))
                    connect_coordinate = tmp2[0][0][0][0][0][0]['_XY_down_left']
                    connect_YWidth= abs(connect_coordinate[1] - target_coord[1])
                    self._DesignParameter['BND_CDAC_B'+str(_numberOfBit-i)+'_Connect' + str(j) + '_VTC'+str(k)+'_M' + str(_MetalType)]['_YWidth'] = connect_YWidth

                    ## Define Boundary_element _XWidth
                    self._DesignParameter['BND_CDAC_B'+str(_numberOfBit-i)+'_Connect' + str(j) + '_VTC'+str(k)+'_M' + str(_MetalType)]['_XWidth'] = _MetalWidth

                    ## Define Boundary_element _XYCoordinates
                        ##Calculate each connector coordinates
                    self._DesignParameter['BND_CDAC_B'+str(_numberOfBit-i)+'_Connect' + str(j) + '_VTC'+str(k)+'_M' + str(_MetalType)]['_XYCoordinates'] = [[connect_coordinate[0], target_coord[1]]]

                    ##Generating Via stack for driving node
                    _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
                    _Caculation_Parameters['_Layer1'] = _DriverMetal #Type of driver node
                    _Caculation_Parameters['_Layer2'] = _MetalType  #M6, Cap metal
                    _Caculation_Parameters['_COX'] = 1
                    _Caculation_Parameters['_COY'] = 2

                        ## Sref ViaX declaration
                    self._DesignParameter['SRF_CDAC_B'+str(_numberOfBit-i)+'_VIA'+str(j)+'_V' + str(k)] = self._SrefElementDeclaration(
                        _DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None,
                                                                    _Name='{}:SRF_CDAC_B{}_VIA{}_V{}'.format(_Name, _numberOfBit-i, j,k)))[0]

                        ## Define Sref Relection
                    self._DesignParameter['SRF_CDAC_B'+str(_numberOfBit-i)+'_VIA'+str(j)+'_V' + str(k)]['_Reflect'] = [0, 0, 0]

                        ## Define Sref Angle
                    self._DesignParameter['SRF_CDAC_B'+str(_numberOfBit-i)+'_VIA'+str(j)+'_V' + str(k)]['_Angle'] = 0

                        ## Calcuate Overlapped XYcoord
                    # # tmp1 = self.get_param_KJH4('BND_CDAC_Driver0_Hrz_M'+str(_MetalType))
                    # # tmp2 = self.get_param_KJH4('BND_CDAC_Driver1_Hrz_M' + str(_MetalType))
                    # # target_coord4= abs(tmp1[0][0]['_XY_down_left'][1] -tmp2[0][0]['_XY_down_left'][1])
                    # # # tmp1 = self.get_param_KJH4('BND_CDAC_Driver1_Hrz_M'+str(_MetalType))
                    # # # tmp2 = self.get_param_KJH4('BND_CDAC_B'+str(i)+'Connect' + str(j) + '_VTC_M' + str(_MetalType))
                    # # # Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])
                    # #
                    # # ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY
                    # # _COX, _COY = self._CalculateNumViaByXYWidth(_MetalWidth, target_coord4+45,'MinEnclosureX')
                    #
                    # ## Define _COX and _COY
                    # _Caculation_Parameters['_COX'] = _COX
                    # _Caculation_Parameters['_COY'] = _COY

                        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
                    self._DesignParameter['SRF_CDAC_B'+str(_numberOfBit-i)+'_VIA'+str(j)+'_V' + str(k)]['_DesignObj']._CalculateDesignParameterXmin(
                        **_Caculation_Parameters)

                        ## Calculate Sref XYcoord
                    tmp1 = self.get_param_KJH4('BND_CDAC_Driver'+str(_numberOfBit-i)+'_Hrz_M'+str(_MetalType))
                    tmp2 = self.get_param_KJH4('BND_CDAC_B'+str(_numberOfBit-i)+'_Connect' + str(j) + '_VTC'+str(k)+'_M' + str(_MetalType))
                    target_coord2 = tmp1[0][0]['_XY_cent']
                    target_coord3 = tmp2[0][0]['_XY_cent']

                    self._DesignParameter['SRF_CDAC_B'+str(_numberOfBit-i)+'_VIA'+str(j)+'_V' + str(k)]['_XYCoordinates'] = [[target_coord3[0] , target_coord2[1]]]

        #     ##Connecting Driver node and Bottom plate of each unit cap
        #     ##각 N-bit에 대해, 연결하고 via까지 쌓기
        # for i in range(_numberOfBit+1) :
        #     _numOfMetal = int(pow(2,i))
        #     for j in range(_numOfMetal) : #각 BIT의 Metal수만큼 iteration 한 후 driving node에 연결시키기
        #         self._DesignParameter['BND_CDAC_B'+str(i)+'Connect' + str(j) + '_VTC_M' + str(_MetalType)] = self._BoundaryElementDeclaration(
        #             _Layer=DesignParameters._LayerMapping['METAL'+str(_MetalType)][0],
        #             _Datatype=DesignParameters._LayerMapping['METAL'+str(_MetalType)][1],
        #             _XWidth=None,
        #             _YWidth=None,
        #             _XYCoordinates=[],
        #         )
        #         #0 1 2 3 4 , i=
        #         ## Define Boundary_element _YWidth
        #             ## Calculate YWidth of connecting node
        #         tmp1= self.get_param_KJH4('BND_CDAC_Driver'+str(_numberOfBit-i)+'_Hrz_M'+str(_MetalType))
        #         target_coord = tmp1[0][0]['_XY_down_left']
        #         connect_YWidth= abs(tmp_y - target_coord[1])
        #         self._DesignParameter['BND_CDAC_B'+str(i)+'Connect' + str(j) + '_VTC_M' + str(_MetalType)]['_YWidth'] = connect_YWidth
        #
        #         ## Define Boundary_element _XWidth
        #         self._DesignParameter['BND_CDAC_B'+str(i)+'Connect' + str(j) + '_VTC_M' + str(_MetalType)]['_XWidth'] = _MetalWidth
        #
        #         ## Define Boundary_element _XYCoordinates
        #             ##Calculate each connector coordinates
        #         tmp2= self.get_param_KJH4('SRF_CDAC_B'+str(_numberOfBit)+'_M'+str(_MetalType),'SRF_CDAC_B'+str(i)+'_VTC'+str(j)+'_M'+str(_MetalType),'BND_UCAP_Bottom_VTC_M'+str(_MetalType))
        #         connect_xcoordinate = tmp2[0][0][0][0]['_XY_down_left'][0]
        #         self._DesignParameter['BND_CDAC_B'+str(i)+'Connect' + str(j) + '_VTC_M' + str(_MetalType)]['_XYCoordinates'] = [[connect_xcoordinate, target_coord[1]]]
        #
        #         ##Generate Via between driving node and bottom plate node
        #         _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
        #         _Caculation_Parameters['_Layer1'] = _DriverMetal #Type of driver node
        #         _Caculation_Parameters['_Layer2'] = _MetalType  #M6, Cap metal
        #         _Caculation_Parameters['_COX'] = None
        #         _Caculation_Parameters['_COY'] = None
        #
        #         ## Sref ViaX declaration
        #         self._DesignParameter['SRF_CDAC_B'+str(i)+'_VIA_V' + str(j)] = self._SrefElementDeclaration(
        #             _DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None,
        #                                                         _Name='{}:SRF_CDAC_B{}_VIA_V{}'.format(_Name, i, j)))[0]
        #
        #         ## Define Sref Relection
        #         self._DesignParameter['SRF_CDAC_B'+str(i)+'_VIA_V' + str(j)]['_Reflect'] = [0, 0, 0]
        #
        #         ## Define Sref Angle
        #         self._DesignParameter['SRF_CDAC_B'+str(i)+'_VIA_V' + str(j)]['_Angle'] = 0
        #
        #         ## Calcuate Overlapped XYcoord
        #         tmp1 = self.get_param_KJH4('BND_CDAC_Driver0_Hrz_M'+str(_MetalType))
        #         tmp2 = self.get_param_KJH4('BND_CDAC_Driver1_Hrz_M' + str(_MetalType))
        #         target_coord4= abs(tmp1[0][0]['_XY_down_left'][1] -tmp2[0][0]['_XY_down_left'][1])
        #         # tmp1 = self.get_param_KJH4('BND_CDAC_Driver1_Hrz_M'+str(_MetalType))
        #         # tmp2 = self.get_param_KJH4('BND_CDAC_B'+str(i)+'Connect' + str(j) + '_VTC_M' + str(_MetalType))
        #         # Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])
        #
        #         ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        #         _COX, _COY = self._CalculateNumViaByXYWidth(_MetalWidth, target_coord4+45,
        #                                                     'MinEnclosureX')
        #
        #         ## Define _COX and _COY
        #         _Caculation_Parameters['_COX'] = _COX
        #         _Caculation_Parameters['_COY'] = _COY
        #
        #         ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        #         self._DesignParameter['SRF_CDAC_B'+str(i)+'_VIA_V' + str(j)]['_DesignObj']._CalculateDesignParameterXmin(
        #             **_Caculation_Parameters)
        #
        #         ## Calculate Sref XYcoord
        #         tmp1 = self.get_param_KJH4('BND_CDAC_Driver'+str(_numberOfBit-i)+'_Hrz_M'+str(_MetalType))
        #         tmp2 = self.get_param_KJH4('BND_CDAC_B'+str(i)+'Connect' + str(j) + '_VTC_M' + str(_MetalType))
        #         target_coord2 = tmp1[0][0]['_XY_cent']
        #         target_coord3 = tmp2[0][0]['_XY_cent']
        #
        #         self._DesignParameter['SRF_CDAC_B'+str(i)+'_VIA_V' + str(j)]['_XYCoordinates'] = [[target_coord3[0] , target_coord2[1]]]
        #



############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'H00_07_CDACSIM'
    cellname = 'H00_00_driver_v19'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object ''' ############################################################### ^^^^^^^^^^^^^^^^^^^^^
    InputParams = dict(
        # # Unit CDAC
        _MetalType=6, #Poly:0, M1:1, M2:2 ...
        _MetalWidth=50,
        _MetalLength=1414,
        # _MetalNumber=3,
        _numberOfBit=3,
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
    LayoutObj = _CommonCentroid(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./gdsfile/{}'.format(_fileName), 'wb')
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