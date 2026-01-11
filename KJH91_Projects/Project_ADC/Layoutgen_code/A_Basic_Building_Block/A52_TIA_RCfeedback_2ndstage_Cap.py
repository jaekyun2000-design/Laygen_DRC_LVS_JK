from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC_EGFET

import numpy as np
import copy
import math

from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_HDVNCAP

class _TIA_RCfeedback_2ndstage_Cap(StickDiagram_KJH1._StickDiagram_KJH):

    _ParametersForDesignCalculation = dict(

        # Cap_2nd_0
        _Length_2nd_cap0=9000,
        _LayoutOption_2nd_cap0=[2, 3, 4],
        _NumFigPair_2nd_cap0=20,
        _Array_2nd_cap0=1,
        _Cbot_Ctop_metalwidth_2nd_cap0=500,

        # Cap_2nd_1
        _Length_2nd_cap1=9000,
        _LayoutOption_2nd_cap1=[2, 3, 4],
        _NumFigPair_2nd_cap1=20,
        _Array_2nd_cap1=1,
        _Cbot_Ctop_metalwidth_2nd_cap1=500,

        # Cap_2nd_2
        _Length_2nd_cap2=9000,
        _LayoutOption_2nd_cap2=[2, 3, 4],
        _NumFigPair_2nd_cap2=20,
        _Array_2nd_cap2=1,
        _Cbot_Ctop_metalwidth_2nd_cap2=500,

        # Cap_2nd_3
        _Length_2nd_cap3=9000,
        _LayoutOption_2nd_cap3=[2, 3, 4],
        _NumFigPair_2nd_cap3=20,
        _Array_2nd_cap3=1,
        _Cbot_Ctop_metalwidth_2nd_cap3=500,

        # Cap_2nd_4
        _Length_2nd_cap4=9000,
        _LayoutOption_2nd_cap4=[2, 3, 4],
        _NumFigPair_2nd_cap4=20,
        _Array_2nd_cap4=1,
        _Cbot_Ctop_metalwidth_2nd_cap4=500,

        # Cap_2nd_5
        _Length_2nd_cap5=9000,
        _LayoutOption_2nd_cap5=[2, 3, 4],
        _NumFigPair_2nd_cap5=20,
        _Array_2nd_cap5=1,
        _Cbot_Ctop_metalwidth_2nd_cap5=500,
    )

    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _Name=self._NameDeclaration(_Name=_Name),
                _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                _XYcoordAsCent=dict(_XYcoordAsCent=0),
                _XYCoordinatePort1Routing=dict(_DesignParametertype=7, _XYCoordinates=[]),
                _XYCoordinatePort2Routing=dict(_DesignParametertype=7, _XYCoordinates=[]),
            )

        ## ################################################################################################################################################ _CalculateDesignParameter

    def _CalculateDesignParameter(self,

                                  # Cap_2nd_0
                                  _Length_2nd_cap0=9000,
                                  _LayoutOption_2nd_cap0=[2, 3, 4],
                                  _NumFigPair_2nd_cap0=20,
                                  _Array_2nd_cap0=1,
                                  _Cbot_Ctop_metalwidth_2nd_cap0=500,

                                  # Cap_2nd_1
                                  _Length_2nd_cap1=9000,
                                  _LayoutOption_2nd_cap1=[2, 3, 4],
                                  _NumFigPair_2nd_cap1=20,
                                  _Array_2nd_cap1=1,
                                  _Cbot_Ctop_metalwidth_2nd_cap1=500,

                                  # Cap_2nd_2
                                  _Length_2nd_cap2=9000,
                                  _LayoutOption_2nd_cap2=[2, 3, 4],
                                  _NumFigPair_2nd_cap2=20,
                                  _Array_2nd_cap2=1,
                                  _Cbot_Ctop_metalwidth_2nd_cap2=500,

                                  # Cap_2nd_3
                                  _Length_2nd_cap3=9000,
                                  _LayoutOption_2nd_cap3=[2, 3, 4],
                                  _NumFigPair_2nd_cap3=20,
                                  _Array_2nd_cap3=1,
                                  _Cbot_Ctop_metalwidth_2nd_cap3=500,

                                  # Cap_2nd_4
                                  _Length_2nd_cap4=9000,
                                  _LayoutOption_2nd_cap4=[2, 3, 4],
                                  _NumFigPair_2nd_cap4=20,
                                  _Array_2nd_cap4=1,
                                  _Cbot_Ctop_metalwidth_2nd_cap4=500,

                                  # Cap_2nd_5
                                  _Length_2nd_cap5=9000,
                                  _LayoutOption_2nd_cap5=[2, 3, 4],
                                  _NumFigPair_2nd_cap5=20,
                                  _Array_2nd_cap5=1,
                                  _Cbot_Ctop_metalwidth_2nd_cap5=500,
                                  ):

        ## ################################################################################################################################# Class_HEADER: Pre Defined Parameter Before Calculation
        # Load DRC library
        _DRCObj = DRC_EGFET.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ## ################################################################################################################################# Calculation_Start
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## HDVCAP cap0 ~ 5
        ## SREF Generation
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A50_HDVNCAP._Guardring._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length'] = _Length_2nd_cap0
        _Caculation_Parameters['_LayoutOption'] = _LayoutOption_2nd_cap0
        _Caculation_Parameters['_NumFigPair'] = _NumFigPair_2nd_cap0
        _Caculation_Parameters['_Array'] = _Array_2nd_cap0
        _Caculation_Parameters['_Cbot_Ctop_metalwidth'] = _Cbot_Ctop_metalwidth_2nd_cap0

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_cap0'] = self._SrefElementDeclaration(
            _DesignObj=A50_HDVNCAP._Guardring(_DesignParameter=None, _Name='{}:SRF_cap0'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_cap0']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_cap0']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_cap0']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_cap0']['_XYCoordinates'] = [[0, 0]]

        print('##############################')
        print('##     Calculation_End    ##')
        print('##############################')


## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from TIA_Proj_YCH.Library_and_Engine.Private import MyInfo_YCH
    from TIA_Proj_YCH.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_A52_TIA_RCfeedback_2ndstage_Cap_v4'
    cellname = 'A52_TIA_RCfeedback_2ndstage_Cap'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        # Cap_2nd_0
        _Length_2nd_cap0=9000,
        _LayoutOption_2nd_cap0=[2,3,4],
        _NumFigPair_2nd_cap0=45,
        _Array_2nd_cap0=3,
        _Cbot_Ctop_metalwidth_2nd_cap0=500,


    )

    '''Mode_DRCCHECK '''
    Mode_DRCCheck = False
    Num_DRCCheck = 1

    for ii in range(0, Num_DRCCheck if Mode_DRCCheck else 1):
        if Mode_DRCCheck:
            ''' Input Parameters for Layout Object '''
        else:
            pass

    ''' Generate Layout Object '''
    LayoutObj = _TIA_RCfeedback_2ndstage_Cap(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('###############      Sending to FTP Server...      ##################')
    My = MyInfo_YCH.USER(DesignParameters._Technology)
    Checker = DRCchecker_KJH0.DRCchecker_KJH0(
        username=My.ID,
        password=My.PW,
        WorkDir=My.Dir_Work,
        DRCrunDir=My.Dir_DRCrun,
        libname=libname,
        cellname=cellname,
        GDSDir=My.Dir_GDS
    )
    # Checker.lib_deletion()
    Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()
    print('#############################      Finished      ################################')
# end of 'main():' ---------------------------------------------------------------------------------------------