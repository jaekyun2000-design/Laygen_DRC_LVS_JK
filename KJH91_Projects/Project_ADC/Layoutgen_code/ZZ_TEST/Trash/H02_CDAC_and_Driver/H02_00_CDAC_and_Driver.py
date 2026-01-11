## Import Basic Modules
    ## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

    ## Library
import copy
import time

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.ZZ_TEST.Trash.H00_CDAC import H00_06_CommonCentroid_v2
from KJH91_Projects.Project_ADC.Layoutgen_code.H01_CDAC_Driver_v2_YJH import H01_01_DriverArray


############################################################################################################################################################ Class_HEADER
class _CDAC_and_Driver(StickDiagram_KJH1._StickDiagram_KJH):
    # Initially Defined design_parameter
    _ParametersForDesignCalculation = dict(
        _MetalType=None,
        _MetalWidth=None,
        _MetalLength=None,
        _Bitsize=None,
        _MSB=None,

        # NumOfDriverUnitsInDriverArray = 2^(_NumOfBits) - 1
        _NumOfBits=4,

        # Driver(Inverter) NMOS
        _Driver_NMOS_NumberofGate=3,  # number
        _Driver_NMOS_ChannelWidth=340,  # number
        _Driver_NMOS_Channellength=30,  # number
        _Driver_NMOS_GateSpacing=None,  # None/number
        _Driver_NMOS_SDWidth=None,  # None/number
        _Driver_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Driver_NMOS_PCCrit=None,  # None/True

        # Source_node_ViaM1M2
        _Driver_NMOS_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _Driver_NMOS_Drain_Via_TF=None,  # True/False

        # POLY dummy setting
        _Driver_NMOS_Dummy=True,  # TF
        # if _PMOSDummy == True
        _Driver_NMOS_Dummy_length=None,  # None/Value
        _Driver_NMOS_Dummy_placement=None,  # None/'Up'/'Dn'/l

        # Driver(Inverter) PMOS
        _Driver_PMOS_NumberofGate=4,  # number
        _Driver_PMOS_ChannelWidth=900,  # number
        _Driver_PMOS_Channellength=30,  # number
        _Driver_PMOS_GateSpacing=None,  # None/number
        _Driver_PMOS_SDWidth=None,  # None/number
        _Driver_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Driver_PMOS_PCCrit=None,  # None/True

        # Source_node_ViaM1M2
        _Driver_PMOS_Source_Via_TF=None,  # True/False

        # Drain_node_ViaM1M2
        _Driver_PMOS_Drain_Via_TF=None,  # True/False

        # POLY dummy setting
        _Driver_PMOS_Dummy=True,  # TF
        # if _PMOSDummy == True
        _Driver_PMOS_Dummy_length=None,  # None/Value
        _Driver_PMOS_Dummy_placement=None,  # None/'Up'/'Dn'/

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

                                  # NumOfDriverUnitsInDriverArray = 2^(_NumOfBits) - 1
                                  _NumOfBits=4,

                                  # Driver(Inverter) NMOS
                                  _Driver_NMOS_NumberofGate=3,  # number
                                  _Driver_NMOS_ChannelWidth=340,  # number
                                  _Driver_NMOS_Channellength=30,  # number
                                  _Driver_NMOS_GateSpacing=None,  # None/number
                                  _Driver_NMOS_SDWidth=None,  # None/number
                                  _Driver_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Driver_NMOS_PCCrit=None,  # None/True

                                  # Source_node_ViaM1M2
                                  _Driver_NMOS_Source_Via_TF=True,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Driver_NMOS_Drain_Via_TF=None,  # True/False

                                  # POLY dummy setting
                                  _Driver_NMOS_Dummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Driver_NMOS_Dummy_length=None,  # None/Value
                                  _Driver_NMOS_Dummy_placement=None,  # None/'Up'/'Dn'/l

                                  # Driver(Inverter) PMOS
                                  _Driver_PMOS_NumberofGate=4,  # number
                                  _Driver_PMOS_ChannelWidth=900,  # number
                                  _Driver_PMOS_Channellength=30,  # number
                                  _Driver_PMOS_GateSpacing=None,  # None/number
                                  _Driver_PMOS_SDWidth=None,  # None/number
                                  _Driver_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Driver_PMOS_PCCrit=None,  # None/True

                                  # Source_node_ViaM1M2
                                  _Driver_PMOS_Source_Via_TF=None,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Driver_PMOS_Drain_Via_TF=None,  # True/False

                                  # POLY dummy setting
                                  _Driver_PMOS_Dummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Driver_PMOS_Dummy_length=None,  # None/Value
                                  _Driver_PMOS_Dummy_placement=None,  # None/'Up'/'Dn'/

                                  ):

        ################################################################################################################################################## Class_HEADER: Pre Defined Parameter Before Calculation
        print('##     Pre Defined Parameter Before Calculation    ##')
        # Load DRC library
        _DRCobj = DRC.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']


        ## CALCULATION START
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

        ############################################################################################################################################################ CALCULATION START

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Sref Gen: CommonArrary
            ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(H00_06_CommonCentroid_v2._CommonCentroid._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_MetalType']    = _MetalType
        _Caculation_Parameters['_MetalWidth']   = _MetalWidth
        _Caculation_Parameters['_MetalLength']  = _MetalLength
        _Caculation_Parameters['_Bitsize']      = _Bitsize
        _Caculation_Parameters['_MSB']          =_MSB

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_CommonCentroid'] = self._SrefElementDeclaration(_DesignObj=H00_06_CommonCentroid_v2._CommonCentroid(_DesignParameter=None, _Name='{}:SRF_CommonCentroid'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_CommonCentroid']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CommonCentroid']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CommonCentroid']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CommonCentroid']['_XYCoordinates'] = [[0, 0]]


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Sref Gen: CommonArrary
            ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters0 = copy.deepcopy(H01_01_DriverArray._DriverArray._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters0['_Driver_NMOS_NumberofGate'] = _Driver_NMOS_NumberofGate
        _Caculation_Parameters0['_Driver_NMOS_ChannelWidth'] =_Driver_NMOS_ChannelWidth
        _Caculation_Parameters0['_Driver_NMOS_Channellength'] =_Driver_NMOS_Channellength
        _Caculation_Parameters0['_Driver_NMOS_GateSpacing'] =_Driver_NMOS_GateSpacing
        _Caculation_Parameters0['_Driver_NMOS_SDWidth'] =_Driver_NMOS_SDWidth
        _Caculation_Parameters0['_Driver_NMOS_XVT'] =_Driver_NMOS_XVT
        _Caculation_Parameters0['_Driver_NMOS_PCCrit'] =_Driver_NMOS_PCCrit
        _Caculation_Parameters0['_Driver_NMOS_Source_Via_TF'] =True #default
        _Caculation_Parameters0['_Driver_NMOS_Drain_Via_TF'] =True
        _Caculation_Parameters0['_Driver_NMOS_Dummy'] = True #default
        _Caculation_Parameters0['_Driver_NMOS_Dummy_length'] =_Driver_NMOS_Dummy_length
        _Caculation_Parameters0['_Driver_NMOS_Dummy_placement'] =_Driver_NMOS_Dummy_length
        _Caculation_Parameters0['_Driver_PMOS_NumberofGate'] = _Driver_PMOS_NumberofGate
        _Caculation_Parameters0['_Driver_PMOS_ChannelWidth'] =_Driver_PMOS_ChannelWidth
        _Caculation_Parameters0['_Driver_PMOS_Channellength'] =_Driver_PMOS_Channellength
        _Caculation_Parameters0['_Driver_PMOS_GateSpacing'] =_Driver_PMOS_GateSpacing
        _Caculation_Parameters0['_Driver_PMOS_SDWidth'] =_Driver_PMOS_SDWidth
        _Caculation_Parameters0['_Driver_PMOS_XVT'] =_Driver_PMOS_XVT
        _Caculation_Parameters0['_Driver_PMOS_PCCrit'] =_Driver_PMOS_PCCrit
        _Caculation_Parameters0['_Driver_PMOS_Source_Via_TF'] =True #default
        _Caculation_Parameters0['_Driver_PMOS_Drain_Via_TF'] =True
        _Caculation_Parameters0['_Driver_PMOS_Dummy'] = True #default
        _Caculation_Parameters0['_Driver_PMOS_Dummy_length'] =_Driver_PMOS_Dummy_length
        _Caculation_Parameters0['_Driver_PMOS_Dummy_length'] =_Driver_PMOS_Dummy_length
        _Caculation_Parameters0['_NumOfBits'] =_NumOfBits


                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_DriverArray'] = self._SrefElementDeclaration(_DesignObj=H01_01_DriverArray._DriverArray(_DesignParameter=None, _Name='{}:SRF_DriverArray'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_DriverArray']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DriverArray']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DriverArray']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters0)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DriverArray']['_XYCoordinates'] = [[0, 0]]


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Bnd gne: Hrz ....
        tmp1 = self.get_param_KJH4('SRF_DriverArray','BND_NWELL')
        tmp2_1 = self.get_outter_KJH4('SRF_CommonCentroid','SRF_CommonArray','SRF_CDAC_B{}_VTC0_M{}'.format(_Bitsize,_MetalType))
        tmp2_2 = self.get_outter_KJH4('SRF_CommonCentroid','SRF_CommonArray','SRF_CDAC_B{}_VTC{}_M{}'.format(_Bitsize,2**_Bitsize-1,_MetalType))
        Capxwidth = abs(tmp2_1['_Mostleft']['coord'][0] - tmp2_2['_Mostright']['coord'][0])
        driverxwidth = tmp1[0][0][0]['_Xwidth']

            ## Boundary_element Generation
        ##Pre-defined
        hrz_ywidth = 50

                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Bottom_Hrz'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL{}'.format(_MetalType - 1)][0],
        _Datatype=DesignParameters._LayerMapping['METAL{}'.format(_MetalType - 1)][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Bottom_Hrz']['_YWidth'] = hrz_ywidth

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Bottom_Hrz']['_XWidth'] =max(Capxwidth,driverxwidth)

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Bottom_Hrz']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Bottom_Hrz']['_XYCoordinates'] = [[0, 0]]

        for i in range(0,_Bitsize+1):
                            ## Calculate
                                ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_CommonCentroid','BND_MSB{}_Bottom_Hrz'.format(i))
            target_coord = tmp1[0][0][0]['_XY_cent']
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Bottom_Hrz')
            approaching_coord = tmp2[0][0]['_XY_cent']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Bottom_Hrz')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Bottom_Hrz']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ReCaculate Coord
        #Pre-defined
        Distance2 = 500

        tmp1 = self.get_param_KJH4('BND_Bottom_Hrz')
        tmp2 = self.get_param_KJH4('SRF_DriverArray','SRF_1C_DriverCell','BND_Output_Node_Hrz_M4')

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_DriverArray']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_Bottom_Hrz')
        target_coord = tmp1[-1][0]['_XY_down']
                            ## Approaching_coord: _XY_type2
                                ## X
        approaching_coordx = tmp2[0][0][0][0]['_XY_right'][0]
                                ## Y
        tmp2_2 = self.get_param_KJH4('SRF_DriverArray','BND_NWELL')
        approaching_coordy = tmp2_2[0][0][0]['_XY_up'][1]
        approaching_coord = [approaching_coordx,approaching_coordy]

                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_DriverArray')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[1] = New_Scoord[1] - Distance2
        New_Scoord[0] = New_Scoord[0] - 25
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_DriverArray']['_XYCoordinates'] = tmpXY



        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## VTC~
        for i in range(0,_Bitsize+1):
                ## Boundary_element Generation
                    ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_Driver{}Out_Vtc_M4'.format(i)] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
            )

                    ## Define Boundary_element _YWidth
            tmp1 = self.get_param_KJH4('BND_Bottom_Hrz')
            tmp2 = self.get_param_KJH4('SRF_DriverArray', 'SRF_{}C_DriverCell'.format(2**(_Bitsize-i)), 'BND_Output_Node_Hrz_M4')
            self._DesignParameter['BND_Driver{}Out_Vtc_M4'.format(i)]['_YWidth'] = abs( tmp1[i][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] )

                    ## Define Boundary_element _XWidth
            self._DesignParameter['BND_Driver{}Out_Vtc_M4'.format(i)]['_XWidth'] = 50

                    ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_Driver{}Out_Vtc_M4'.format(i)]['_XYCoordinates'] = [[0, 0]]

                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['BND_Driver{}Out_Vtc_M4'.format(i)]['_XYCoordinates'] = [[0, 0]]

            for j in range(0,2**(_Bitsize-i)):
                                ## Calculate
                                    ## Target_coord: _XY_type1
                tmp1 = self.get_param_KJH4('SRF_DriverArray', 'SRF_{}C_DriverCell'.format(2**(_Bitsize-i)), 'BND_Output_Node_Hrz_M4')
                target_coord = tmp1[0][j][0][0]['_XY_down_right']
                                    ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('BND_Driver{}Out_Vtc_M4'.format(i))
                approaching_coord = tmp2[0][0]['_XY_down_right']
                                    ## Sref coord
                tmp3 = self.get_param_KJH4('BND_Driver{}Out_Vtc_M4'.format(i))
                Scoord = tmp3[0][0]['_XY_origin']
                                    ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)

                                ## Define coordinates
            self._DesignParameter['BND_Driver{}Out_Vtc_M4'.format(i)]['_XYCoordinates'] = tmpXY



        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')



############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_ADC_H02_00_CDAC_and_Driver'
    cellname = 'H02_00_CDAC_and_Driver_95'
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

        # NumOfDriverUnitsInDriverArray = 2^(_NumOfBits) - 1
        _NumOfBits=4,

        # Driver(Inverter) NMOS
        _Driver_NMOS_NumberofGate=3,  # number
        _Driver_NMOS_ChannelWidth=340,  # number
        _Driver_NMOS_Channellength=30,  # number
        _Driver_NMOS_GateSpacing=None,  # None/number
        _Driver_NMOS_SDWidth=None,  # None/number
        _Driver_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Driver_NMOS_PCCrit=None,  # None/True

        # Source_node_ViaM1M2
        _Driver_NMOS_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _Driver_NMOS_Drain_Via_TF=None,  # True/False

        # POLY dummy setting
        _Driver_NMOS_Dummy=True,  # TF
        # if _PMOSDummy == True
        _Driver_NMOS_Dummy_length=None,  # None/Value
        _Driver_NMOS_Dummy_placement=None,  # None/'Up'/'Dn'/l

        # Driver(Inverter) PMOS
        _Driver_PMOS_NumberofGate=4,  # number
        _Driver_PMOS_ChannelWidth=900,  # number
        _Driver_PMOS_Channellength=30,  # number
        _Driver_PMOS_GateSpacing=None,  # None/number
        _Driver_PMOS_SDWidth=None,  # None/number
        _Driver_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Driver_PMOS_PCCrit=None,  # None/True

        # Source_node_ViaM1M2
        _Driver_PMOS_Source_Via_TF=None,  # True/False

        # Drain_node_ViaM1M2
        _Driver_PMOS_Drain_Via_TF=None,  # True/False

        # POLY dummy setting
        _Driver_PMOS_Dummy=True,  # TF
        # if _PMOSDummy == True
        _Driver_PMOS_Dummy_length=None,  # None/Value
        _Driver_PMOS_Dummy_placement=None,  # None/'Up'/'Dn'/


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
    LayoutObj = _CDAC_and_Driver(_DesignParameter=None, _Name=cellname)
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
    Checker.lib_deletion()
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