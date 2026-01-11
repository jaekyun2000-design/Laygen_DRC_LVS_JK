## Import Basic Modules
    ## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

    ## Library
import copy
import time

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.ZZ_TEST.Trash.H00_CDAC import H00_01_CapArray


## Define Class
class _CapWithShielding(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
            _MetalType=None,
            _MetalWidth=None,
            _MetalLength=None,
            # _MetalNumber=None,
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
                                    ##Ground_Shielding
                                  _MetalType=None,
                                  _MetalWidth=None,
                                  _MetalLength=None,
                                  # _MetalNumber=None,
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

        ## Generation of CapArray
            ## SREF Generation
            ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(H00_01_CapArray._CArray._ParametersForDesignCalculation)
            ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_MetalType'] = _MetalType
        _Caculation_Parameters['_MetalWidth'] = _MetalWidth
        _Caculation_Parameters['_MetalLength'] = _MetalLength
        # _Caculation_Parameters['_MetalNumber'] = _MetalNumber
            ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_CapWShield_A0'] = self._SrefElementDeclaration(_DesignObj=H00_01_CapArray._CArray(_DesignParameter=None, _Name='{}:SRF_CapWShield_A0'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_CapWShield_A0']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CapWShield_A0']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CapWShield_A0']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CapWShield_A0']['_XYCoordinates'] = [[0, 0]]

        ##Generation of staking Metals for GND Shielding
            ## Boundary_element Generation
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        for i in range(_MetalType - 2, _MetalType + 2):
            self._DesignParameter['BND_CapWShield_Shield_HRZ_M' + str(i)] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL' + str(i)][0],
            _Datatype=DesignParameters._LayerMapping['METAL' + str(i)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
            )

                ## Define Boundary_element _YWidth
            _Shield_Length=400 #constant value
            self._DesignParameter['BND_CapWShield_Shield_HRZ_M' + str(i)]['_YWidth'] = _Shield_Length

                    ## Define Boundary_element _XWidth
                        #Calculating Shielding metal width
            tmp1= self.get_outter_KJH4('SRF_CapWShield_A0')['_Mostright']['coord'][0]
            _Shield_Width=tmp1
            self._DesignParameter['BND_CapWShield_Shield_HRZ_M' + str(i)]['_XWidth'] = _Shield_Width
                    ## Define Boundary_element _XYCoordinates
                        #Calculating Shielding metal coordinates
            tmp2= self.get_outter_KJH4('SRF_CapWShield_A0')['_Mostup']['coord'][0]
            _Shield_ycoordinates= tmp2 + _Shield_Length
            self._DesignParameter['BND_CapWShield_Shield_HRZ_M' + str(i)]['_XYCoordinates'] = [[0, _Shield_ycoordinates]]

            _MetalNumber =2
            target_coord = [0,0]
            target_coord[1] = tmp2 + _Shield_Length
                ## tmp Metal Generation for generating via at stacking metal(connecting shielding metals)
            for j in range(_MetalNumber+1) :
                self._DesignParameter['BND_CapWShield_Shield_VTC' + str(j) + '_M' + str(i)] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['METAL' + str(i)][0],
                    _Datatype=DesignParameters._LayerMapping['METAL' + str(i)][1],
                    _XWidth=None,
                    _YWidth=None,
                    _XYCoordinates=[],
                )
                ## Define Boundary_element _YWidth
                _Top_Length = 400  # constant
                self._DesignParameter['BND_CapWShield_Shield_VTC' + str(j) + '_M' + str(i)]['_YWidth'] = _Shield_Length

                ## Define Boundary_element _XWidth
                self._DesignParameter['BND_CapWShield_Shield_VTC' + str(j) + '_M' + str(i)]['_XWidth'] = _MetalWidth
                ## Define Boundary_element _XYCoordinates
                self._DesignParameter['BND_CapWShield_Shield_VTC' + str(j) + '_M' + str(i)]['_XYCoordinates'] = [target_coord]

                    ##Calculating tmp metal coordinates
                if j == _MetalNumber : ##index error 방지
                    j=j-1 ##index error 방지
                tmp3 = self.get_param_KJH4('SRF_CapWShield_A0' , 'SRF_CArray_UCAP_VTC_C' + str(j), 'BND_UCAP_TRIGHT_VTC_M' + str(_MetalType))
                target_coord = tmp3[0][0][0][0]['_XY_up_left']
                target_coord[1] = target_coord[1] + _Shield_Length


        ##Inter Metal Generation for connecting staking Metals and Cap_Array
            ## Boundary_element Generation
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_CapWShield_Shield_CNT_M'+str(_MetalType-2)] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL' + str(_MetalType - 2)][0],
                _Datatype=DesignParameters._LayerMapping['METAL' + str(_MetalType - 2)][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )

                ## Define Boundary_element _YWidth
            self._DesignParameter['BND_CapWShield_Shield_CNT_M'+str(_MetalType-2)]['_YWidth'] = _Shield_Length

                ## Define Boundary_element _XWidth
            self._DesignParameter['BND_CapWShield_Shield_CNT_M'+str(_MetalType-2)]['_XWidth'] = _Shield_Width

                ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_CapWShield_Shield_CNT_M'+str(_MetalType-2)]['_XYCoordinates'] = [[0, tmp2]]
        # target_coord = [_MetalWidth/2, _Shield_Length/2]
        # target_coord[1] = target_coord[1]+tmp2 + _Shield_Length
        ## Generation of Via for Shielding metal
        for k in range(_MetalNumber+1):
            ## Sref generation: ViaX
            ## Define ViaX Parameter
            _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
            _Caculation_Parameters['_Layer1'] = _MetalType - 2
            _Caculation_Parameters['_Layer2'] = _MetalType + 1
            _Caculation_Parameters['_COX'] = None
            _Caculation_Parameters['_COY'] = None

            ## Sref ViaX declaration 1
            self._DesignParameter['SRF_CapWShield_Shield_VIA_V' + str(k)] = self._SrefElementDeclaration(
                _DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_Shield_VIA_V{}'.format(_Name,k)))[0]

            ## Define Sref Relection
            self._DesignParameter['SRF_CapWShield_Shield_VIA_V' + str(k)]['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
            self._DesignParameter['SRF_CapWShield_Shield_VIA_V' + str(k)]['_Angle'] = 0
            # 'BND_CDAC_SHIELD_VTC' + str(j) + '_M' + str(i)
            ## Calcuate Overlapped XYcoord
            tmp1 = self.get_param_KJH4('BND_CapWShield_Shield_VTC' + str(k) + '_M' + str(_MetalType))
            tmp2 = self.get_param_KJH4('BND_CapWShield_Shield_VTC' + str(k) + '_M' + str(_MetalType + 1))
            Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
            _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'],
                                                        'MinEnclosureX')

            ## Define _COX and _COY
            _Caculation_Parameters['_COX'] = _COX
            _Caculation_Parameters['_COY'] = _COY

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
            self._DesignParameter['SRF_CapWShield_Shield_VIA_V' + str(k)]['_DesignObj']._CalculateDesignParameterXmin(
                **_Caculation_Parameters)

            ## Calculate Sref XYcoord
            tmp1 = self.get_param_KJH4('BND_CapWShield_Shield_VTC' + str(k) + '_M' + str(_MetalType))
            target_coord = tmp1[0][0]['_XY_cent']
            self._DesignParameter['SRF_CapWShield_Shield_VIA_V' + str(k)]['_XYCoordinates'] = [target_coord]
            # if k == _MetalNumber:  ##index error 방지
            #     k = k - 1  ##index error 방지
            # tmp1 = self.get_param_KJH4('BND_Shield_VTC' + str(k) + '_M' + str(_MetalType))
            # target_coord = tmp1[0][0]['_XY_cent']


if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_KJB
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'H00_07_CDACSIM'
    cellname = 'H00_00_driver_v01'
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
    LayoutObj = _CapWithShielding(_DesignParameter=None, _Name=cellname)
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
    # end of 'main():' -------------------------------------------------------------------------------------