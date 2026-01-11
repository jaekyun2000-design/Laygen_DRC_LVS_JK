## Import Basic Modules
    ## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

    ## Library
import copy
import numpy as np
import time

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.ZZ_TEST.Trash.H00_CDAC import H00_03_CapWithDummy, \
    H00_02_CapWithShielding


class _CDAC(StickDiagram_KJH1._StickDiagram_KJH):
    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
            _MetalType=None,
            _MetalWidth=None,
            _MetalLength=None,
            _MetalNumber=None, ##Vector Type
            _DummyNumber=None, ##Vector Type
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
                                  _DummyNumber=None,
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


        ##Generation of First Dummy Array
            ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(H00_03_CapWithDummy._CapWithDummy._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_MetalType'] = _MetalType
        _Caculation_Parameters['_MetalWidth'] = _MetalWidth
        _Caculation_Parameters['_MetalLength'] = _MetalLength
        _Caculation_Parameters['_MetalNumber'] = _DummyNumber[0]

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_DummyCap_C0'] = self._SrefElementDeclaration(_DesignObj=H00_03_CapWithDummy._CapWithDummy(_DesignParameter=None, _Name='{}:SRF_DummyCap_C0'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_DummyCap_C0']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DummyCap_C0']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DummyCap_C0']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DummyCap_C0']['_XYCoordinates'] = [[0, 0]]
                ## Calculate XYCorrdinates of following Capacitor
        if _DummyNumber[0] == 0 : targetcoord = 0 ## In case of Dummy Number is zero
        else : targetcoord = abs(self.get_outter_KJH4('SRF_DummyCap_C0')['_Mostright']['coord'][0] - _MetalWidth)

        ##Generation of CDAC
        for i in range(len(_MetalNumber)) :
            ## Generation of M-bit Capacitor Array( Capacitance : 2 to the M times 0.5f )
                ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
            _Caculation_Parameters = copy.deepcopy(
                H00_02_CapWithShielding._CapWithShielding._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
            _Caculation_Parameters['_MetalType'] = _MetalType
            _Caculation_Parameters['_MetalWidth'] = _MetalWidth
            _Caculation_Parameters['_MetalLength'] = _MetalLength
            _Caculation_Parameters['_MetalNumber'] = _MetalNumber[i]

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
            self._DesignParameter['SRF_Cap_C'+str(i)] = self._SrefElementDeclaration(
                _DesignObj=H00_02_CapWithShielding._CapWithShielding(_DesignParameter=None,
                                                                     _Name='{}:SRF_Cap_C{}'.format(_Name,i)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
            self._DesignParameter['SRF_Cap_C'+str(i)]['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_Cap_C'+str(i)]['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_Cap_C'+str(i)]['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_Cap_C'+str(i)]['_XYCoordinates'] = [[targetcoord, 0]]
            targetcoord = abs(self.get_outter_KJH4('SRF_Cap_C'+str(i))['_Mostright']['coord'][0] - _MetalWidth)

            #Generation of Dummy Capacitor
                ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
            _Caculation_Parameters = copy.deepcopy(H00_03_CapWithDummy._CapWithDummy._ParametersForDesignCalculation)
            ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
            _Caculation_Parameters['_MetalType'] = _MetalType
            _Caculation_Parameters['_MetalWidth'] = _MetalWidth
            _Caculation_Parameters['_MetalLength'] = _MetalLength
            _Caculation_Parameters['_MetalNumber'] = _DummyNumber[i+1]

            ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
            self._DesignParameter['SRF_DummyCap_C'+str(i+1)] = self._SrefElementDeclaration(
                _DesignObj=H00_03_CapWithDummy._CapWithDummy(_DesignParameter=None,
                                                             _Name='{}:SRF_DummyCap_C{}'.format(_Name,i+1)))[0]

            ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
            self._DesignParameter['SRF_DummyCap_C'+str(i+1)]['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_DummyCap_C'+str(i+1)]['_Angle'] = 0

            ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_DummyCap_C'+str(i+1)]['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_DummyCap_C'+str(i+1)]['_XYCoordinates'] = [[targetcoord, 0]]

            if _DummyNumber[i+1] == 0:
                targetcoord = targetcoord  ## In case of Dummy Number is zero
            else:
                targetcoord = abs(self.get_outter_KJH4('SRF_DummyCap_C'+str(i+1))['_Mostright']['coord'][0] - _MetalWidth)




############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_KJB
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'H00_Simul'
    cellname = 'H00_04_driver_v02'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object ''' ############################################################### ^^^^^^^^^^^^^^^^^^^^^
    InputParams = dict(
        # # Unit CDAC
        _MetalType=6, #Poly:0, M1:1, M2:2 ...
        _MetalWidth=50,
        _MetalLength=1414,
        _MetalNumber=np.array([0]),  ##Vector Type
        _DummyNumber=np.array([2,0]),  ##Vector Type
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
    LayoutObj = _CDAC(_DesignParameter=None, _Name=cellname)
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