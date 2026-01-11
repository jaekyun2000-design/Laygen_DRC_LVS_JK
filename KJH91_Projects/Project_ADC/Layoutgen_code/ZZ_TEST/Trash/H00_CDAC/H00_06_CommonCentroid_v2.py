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


        ## CALCULATION START
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

        ############################################################################################################################################################ CALCULATION START

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Sref Gen: CommonArrary
            ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(H00_05_CommonArray._CommonArray._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_MetalType']    = _MetalType
        _Caculation_Parameters['_MetalWidth']   = _MetalWidth
        _Caculation_Parameters['_MetalLength']  = _MetalLength
        _Caculation_Parameters['_Bitsize']      = _Bitsize
        _Caculation_Parameters['_MSB']          =_MSB

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_CommonArray'] = self._SrefElementDeclaration(_DesignObj=H00_05_CommonArray._CommonArray(_DesignParameter=None, _Name='{}:SRF_CommonArray'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_CommonArray']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CommonArray']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CommonArray']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CommonArray']['_XYCoordinates'] = [[0, 0]]



        for i in range(0,_Bitsize+1):
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## BND Gen: VtcExten
            ## Boundary_element Generation
            ## Pre-defined
            _NodeDistance = 300
            _CapDriverDistance = 100  # select Arbitarily
            _Xwidth_BottomExten_Vtc = 50

                    ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_MSB{}_BottomExten_Vtc'.format(i)] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}'.format(_MetalType)][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}'.format(_MetalType)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
            )

                    ## Define Boundary_element _YWidth
            if i ==0:
                tmp = _CapDriverDistance + _NodeDistance
            else:
                tmp1 = self.get_param_KJH4('SRF_CommonArray','SRF_CDAC_B{}_VTC{}_M{}'.format(_Bitsize-i,0,_MetalType),'SRF_CapWShield_A0','SRF_CArray_UCAP_VTC_C{}'.format(0),'BND_UCAP_Bottom_VTC_M{}'.format(_MetalType))
                tmp2 = self.get_param_KJH4('BND_MSB{}_Bottom_Hrz'.format(i-1))
                tmp = abs( tmp1[0][0][0][0][0][0]['_XY_down'][1] - tmp2[0][0]['_XY_down'][1] ) + _NodeDistance

            self._DesignParameter['BND_MSB{}_BottomExten_Vtc'.format(i)]['_YWidth'] = tmp

                    ## Define Boundary_element _XWidth
            self._DesignParameter['BND_MSB{}_BottomExten_Vtc'.format(i)]['_XWidth'] = _Xwidth_BottomExten_Vtc

                    ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_MSB{}_BottomExten_Vtc'.format(i)]['_XYCoordinates'] = [[0, 0]]

                            ## Calculate Sref XYcoord
            tmpXY = []
            for k in range(0, 2**(_Bitsize-i)):
                for j in range(0,2):
                                    ## Calculate
                                        ## Target_coord: _XY_type1
                    tmp1 = self.get_param_KJH4('SRF_CommonArray','SRF_CDAC_B{}_VTC{}_M{}'.format(_Bitsize-i,k,_MetalType),'SRF_CapWShield_A0','SRF_CArray_UCAP_VTC_C{}'.format(j),'BND_UCAP_Bottom_VTC_M{}'.format(_MetalType))
                    target_coord = tmp1[0][0][0][0][0][0]['_XY_down_left']
                                        ## Approaching_coord: _XY_type2
                    tmp2 = self.get_param_KJH4('BND_MSB{}_BottomExten_Vtc'.format(i))
                    approaching_coord = tmp2[0][0]['_XY_up_left']
                                        ## Sref coord
                    tmp3 = self.get_param_KJH4('BND_MSB{}_BottomExten_Vtc'.format(i))
                    Scoord = tmp3[0][0]['_XY_origin']
                                        ## Cal
                    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                    tmpXY.append(New_Scoord)

                                ## Define coordinates
            self._DesignParameter['BND_MSB{}_BottomExten_Vtc'.format(i)]['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## BND Gen: Hrz
            ## Boundary_element Generation
            ## pre-defined
            ywidth_bottom_hrz = 50

            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_MSB{}_Bottom_Hrz'.format(i)] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL{}'.format(_MetalType - 1)][0],
                _Datatype=DesignParameters._LayerMapping['METAL{}'.format(_MetalType - 1)][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )

            ## Define Boundary_element _YWidth
            self._DesignParameter['BND_MSB{}_Bottom_Hrz'.format(i)]['_YWidth'] = ywidth_bottom_hrz

            ## Define Boundary_element _XWidth
            tmp = self.get_param_KJH4('BND_MSB{}_BottomExten_Vtc'.format(i))

            self._DesignParameter['BND_MSB{}_Bottom_Hrz'.format(i)]['_XWidth'] = abs( tmp[0][0]['_XY_left'][0] - tmp[-1][0]['_XY_right'][0] )

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_MSB{}_Bottom_Hrz'.format(i)]['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['BND_MSB{}_Bottom_Hrz'.format(i)]['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('BND_MSB{}_BottomExten_Vtc'.format(i))
            target_coord = tmp1[0][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_MSB{}_Bottom_Hrz'.format(i))
            approaching_coord = tmp2[0][0]['_XY_up_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_MSB{}_Bottom_Hrz'.format(i))
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_MSB{}_Bottom_Hrz'.format(i)]['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Via Gen:
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = _MetalType-1
        _Caculation_Parameters['_Layer2'] = _MetalType
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Bottom_ViaM5M6'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None, _Name='{}:SRF_Bottom_ViaM5M6'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Bottom_ViaM5M6']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Bottom_ViaM5M6']['_Angle'] = 0

            ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Bottom_ViaM5M6']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Bottom_ViaM5M6']['_XYCoordinates'] = [[0, 0]]

        for i in range(0,_Bitsize+1):
            for j in range(0,2**(_Bitsize-i+1)):
                        ## Calculate
                            ## Target_coord
                                #x
                tmp1 = self.get_param_KJH4('BND_MSB{}_BottomExten_Vtc'.format(i))
                target_coord = tmp1[j][0]['_XY_down']
                            ## Approaching_coord
                tmp2 = self.get_param_KJH4('SRF_Bottom_ViaM5M6','SRF_ViaM5M6','BND_Met5Layer')
                approaching_coord = tmp2[0][0][0][0]['_XY_down']
                            ## Sref coord
                tmp3 = self.get_param_KJH4('SRF_Bottom_ViaM5M6')
                Scoord = tmp3[0][0]['_XY_origin']
                            ## Calculate
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Bottom_ViaM5M6']['_XYCoordinates'] = tmpXY



        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')



############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_ADC_H00_07_CDACSIM'
    cellname = 'H00_00_driver_91'
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
    LayoutObj = _CommonCentroid(_DesignParameter=None, _Name=cellname)
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