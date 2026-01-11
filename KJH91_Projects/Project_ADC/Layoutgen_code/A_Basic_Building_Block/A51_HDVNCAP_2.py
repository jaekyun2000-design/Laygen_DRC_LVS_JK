
## Import Basic Modules
    ## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC_EGFET

    ## Library
import copy
import math
import numpy as np
import time
import re

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_HDVNCAP

    ## Building blocks
# from KJH91_Projects.Project_ADC.Layoutgen_code.C01_HDVNCAP_Array import C01_03_Array


## Define Class
class _HDVNCAP_2(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(

    _Length_cap0 = None,
    _LayoutOption_cap0 = None,
    _NumFigPair_cap0 = None,

    _Array_cap0 = None, #number: 1xnumber
    _Cbot_Ctop_metalwidth_cap0 = None, #number

    _Length_cap1 = None,
    _LayoutOption_cap1 = None,
    _NumFigPair_cap1 = None,

    _Array_cap1 = None, #number: 1xnumber
    _Cbot_Ctop_metalwidth_cap1 = None, #number

    )

    ## Initially Generated _DesignParameter
    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
            _Name=self._NameDeclaration(_Name=_Name),
            _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
            _XYcoordAsCent=dict(_XYcoordAsCent=0),
            )


    ## DesignParameter Calculation
    def _CalculateDesignParameter(self,

        _Length_cap0 = None,
        _LayoutOption_cap0 = None,
        _NumFigPair_cap0 = None,

        _Array_cap0 = None, #number: 1xnumber
        _Cbot_Ctop_metalwidth_cap0 = None, #number

        _Length_cap1=None,
        _LayoutOption_cap1=None,
        _NumFigPair_cap1=None,

        _Array_cap1=None,  # number: 1xnumber
        _Cbot_Ctop_metalwidth_cap1=None,  # number

    ):

        ## Class_HEADER: Pre Defined Parameter Before Calculation
        ## Load DRC library
        _DRCobj = DRC_EGFET.DRC()
        ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ## CALCULATION START
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## HDVCAP cap0
        ## SREF Generation
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A50_HDVNCAP._Guardring._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length'] = _Length_cap0
        _Caculation_Parameters['_LayoutOption'] = _LayoutOption_cap0
        _Caculation_Parameters['_NumFigPair'] = _NumFigPair_cap0
        _Caculation_Parameters['_Array'] = _Array_cap0
        _Caculation_Parameters['_Cbot_Ctop_metalwidth'] = _Cbot_Ctop_metalwidth_cap0

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_cap0'] = self._SrefElementDeclaration(
            _DesignObj=A50_HDVNCAP._Guardring(_DesignParameter=None, _Name='{}:SRF_cap0'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_cap0']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_cap0']['_Angle'] = 90

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_cap0']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_cap0']['_XYCoordinates'] = [[0, 0]]

## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## HDVCAP cap1
        ## SREF Generation
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A50_HDVNCAP._Guardring._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length'] = _Length_cap1
        _Caculation_Parameters['_LayoutOption'] = _LayoutOption_cap1
        _Caculation_Parameters['_NumFigPair'] = _NumFigPair_cap1
        _Caculation_Parameters['_Array'] = _Array_cap1
        _Caculation_Parameters['_Cbot_Ctop_metalwidth'] = _Cbot_Ctop_metalwidth_cap1

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_cap1'] = self._SrefElementDeclaration(
            _DesignObj=A50_HDVNCAP._Guardring(_DesignParameter=None, _Name='{}:SRF_cap1'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_cap1']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_cap1']['_Angle'] = 90

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_cap1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_cap1']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_cap0', 'SRF_Pbodyring', 'SRF_PbodyBottom', 'SRF_PbodyContactPhyLen','BND_Met1Layer')
        target_coord = tmp1[0][0][0][0][0][0]['_XY_down']
        target_coord[0] = target_coord[0] + 400
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_cap1', 'SRF_Pbodyring', 'SRF_PbodyTop', 'SRF_PbodyContactPhyLen','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0][0][0]['_XY_up']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_cap1')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['SRF_cap1']['_XYCoordinates'] = tmpXY

## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## cap0 cap1 metal1 extension
        # Define Boundary_element
        self._DesignParameter['BND_Met1Layer_Extension'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[],
        )

        # Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('SRF_cap0', 'SRF_Pbodyring', 'SRF_PbodyRight', 'SRF_PbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_Met1Layer_Extension']['_YWidth'] = tmp[0][0][0][0][0][0]['_Xwidth']

        # Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_cap0', 'SRF_Pbodyring', 'SRF_PbodyTop', 'SRF_PbodyContactPhyLen','BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_cap1', 'SRF_Pbodyring', 'SRF_PbodyBottom', 'SRF_PbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_Met1Layer_Extension']['_XWidth'] = abs(tmp1[0][0][0][0][0][0]['_XY_up'][0] - tmp2[0][0][0][0][0][0]['_XY_down'][0])
        # Define XYcoord.
        self._DesignParameter['BND_Met1Layer_Extension']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_cap0', 'SRF_Pbodyring', 'SRF_PbodyTop', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        target_coord = tmp1[0][0][0][0][0][0]['_XY_up_right']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Met1Layer_Extension')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Met1Layer_Extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['BND_Met1Layer_Extension']['_XYCoordinates'] = tmpXY


        print('##############################')
        print('##     Calculation_End    ##')
        print('##############################')


## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_AJH
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_A51_HDVNCAP_2_v3'
    cellname = 'A51_HDVNCAP_2'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(


            _Length_cap0=7800,
            _LayoutOption_cap0=[2, 3, 4, 5],  # Writedown [number1, number2, number3, ...]
            _NumFigPair_cap0=50,  # number (ref:75)

            _Array_cap0=1,  # number: 1xnumber
            _Cbot_Ctop_metalwidth_cap0=500,  # number

            _Length_cap1=7800,
            _LayoutOption_cap1=[2, 3, 4, 5],  # Writedown [number1, number2, number3, ...]
            _NumFigPair_cap1=50,  # number (ref:75)

            _Array_cap1=1,  # number: 1xnumber
            _Cbot_Ctop_metalwidth_cap1=500,  # number
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
    ## Gen Object:
    LayoutObj = _HDVNCAP_2(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('###############      Sending to FTP Server...      ##################')
    My = MyInfo_AJH.USER(DesignParameters._Technology)
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