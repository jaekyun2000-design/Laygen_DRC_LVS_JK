## Import Basic Modules
    ## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

    ## Library
import copy
import time

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.ZZ_TEST.Trash.H00_CDAC import H00_02_CapWithShielding


class _CapWithDummy(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
            _MetalType=None,
            _MetalWidth=None,
            _MetalLength=None,
            _MetalNumber=None,
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
                                  _MetalNumber=None,
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
        if _MetalNumber != 0 : ## Generate Dummy Cap
            ## Generation of CapWithShielding
                ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
            _Caculation_Parameters = copy.deepcopy(
                H00_02_CapWithShielding._CapWithShielding._ParametersForDesignCalculation)
                    ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
            _Caculation_Parameters['_MetalType'] = _MetalType
            _Caculation_Parameters['_MetalWidth'] = _MetalWidth
            _Caculation_Parameters['_MetalLength'] = _MetalLength
            _Caculation_Parameters['_MetalNumber'] = _MetalNumber
                    ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
            self._DesignParameter['SRF_CapWDummy_Cap_C0'] = self._SrefElementDeclaration(_DesignObj=H00_02_CapWithShielding._CapWithShielding(_DesignParameter=None, _Name='{}:SRF_CapWDummy_Cap_C0'.format(_Name)))[0]
                    ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
            self._DesignParameter['SRF_CapWDummy_Cap_C0']['_Reflect'] = [0, 0, 0]

                    ## Define Sref Angle: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CapWDummy_Cap_C0']['_Angle'] = 0

                    ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CapWDummy_Cap_C0']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)
            print(1)

                    ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CapWDummy_Cap_C0']['_XYCoordinates'] = [[0, 0]]
            ## Generation of DummyMetal range _MetalType -2 of _MetalType+1
            for i in range(_MetalType-2, _MetalType+1) :
                ## Generate numbers of '_MetalNumber" for each metal types
                for j in range(_MetalNumber):
                    self._DesignParameter['BND_CapWDummy_Dummy_VTC_M' + str(i) +str(j)] = self._BoundaryElementDeclaration(
                        _Layer=DesignParameters._LayerMapping['METAL' + str(i)][0],
                        _Datatype=DesignParameters._LayerMapping['METAL' + str(i)][1],
                        _XWidth=None,
                        _YWidth=None,
                        _XYCoordinates=[],
                    )

                    ## Define Boundary_element _YWidth
                    self._DesignParameter['BND_CapWDummy_Dummy_VTC_M' + str(i) +str(j)]['_YWidth'] = _MetalLength

                    ## Define Boundary_element _XWidth
                    # Calculating Shielding metal width
                    self._DesignParameter['BND_CapWDummy_Dummy_VTC_M' + str(i) +str(j)]['_XWidth'] = _MetalWidth
                    ## Define Boundary_element _XYCoordinates
                # Calculating Dummy metal coordinates
                    tmp1 = self.get_param_KJH4('SRF_CapWDummy_Cap_C0','SRF_CapWShield_A0','SRF_CArray_UCAP_VTC_C'+str(j), 'BND_UCAP_TLEFT_VTC_M'+ str(_MetalType))
                    target_coord= tmp1[0][0][0][0][0]['_XY_down_right'][0]
                    _CapSpacing = 50
                    x_coordinate = target_coord + _CapSpacing
                    self._DesignParameter['BND_CapWDummy_Dummy_VTC_M' + str(i) +str(j)]['_XYCoordinates'] = [[x_coordinate, 0]]

            ## Generation of Via for Dummy metals
            for k in range(_MetalNumber):
                ## Sref generation: ViaX
                ## Define ViaX Parameter
                _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
                _Caculation_Parameters['_Layer1'] = _MetalType - 2
                _Caculation_Parameters['_Layer2'] = _MetalType
                _Caculation_Parameters['_COX'] = None
                _Caculation_Parameters['_COY'] = None

                ## Sref ViaX declaration
                self._DesignParameter['SRF_CapWDummy_Dummy_VIA_V' + str(k)] = self._SrefElementDeclaration(
                    _DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None,
                                                                _Name='{}:SRF_Dummy_VIA_V{}'.format(_Name,k)))[0]

                ## Define Sref Relection
                self._DesignParameter['SRF_CapWDummy_Dummy_VIA_V' + str(k)]['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle
                self._DesignParameter['SRF_CapWDummy_Dummy_VIA_V' + str(k)]['_Angle'] = 0
                # 'BND_CDAC_SHIELD_VTC' + str(j) + '_M' + str(i)
                ## Calcuate Overlapped XYcoord
                tmp1 = self.get_param_KJH4('BND_CapWDummy_Dummy_VTC_M' +str(_MetalType-1) + str(k) )
                tmp2 = self.get_param_KJH4('BND_CapWDummy_Dummy_VTC_M' + str(_MetalType) + str(k) )
                Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

                ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
                _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureX')

                ## Define _COX and _COY
                _Caculation_Parameters['_COX'] = _COX
                _Caculation_Parameters['_COY'] = _COY

                ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
                self._DesignParameter['SRF_CapWDummy_Dummy_VIA_V' + str(k)]['_DesignObj']._CalculateDesignParameterXmin(
                    **_Caculation_Parameters)

                ## Calculate Sref XYcoord
                tmp1 = self.get_param_KJH4('BND_CapWDummy_Dummy_VTC_M' + str(_MetalType) + str(k) )
                target_coord = tmp1[0][0]['_XY_cent']
                self._DesignParameter['SRF_CapWDummy_Dummy_VIA_V' + str(k)]['_XYCoordinates'] = [target_coord]
        else : pass ## Does not Generate Dummy Cap.

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_KJB
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'H00_00_CAP'
    cellname = 'H00_00_dummy_v1'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object ''' ############################################################### ^^^^^^^^^^^^^^^^^^^^^
    InputParams = dict(
        # # Unit CDAC
        _MetalType=6, #Poly:0, M1:1, M2:2 ...
        _MetalWidth=50,
        _MetalLength=1414,
        _MetalNumber=2,

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
    LayoutObj = _CapWithDummy(_DesignParameter=None, _Name=cellname)
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