
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

from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A10_PbodyRing_KJH3



    ## Building blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.C01_HDVNCAP_Array import C01_03_Array



## Define Class
class _HDVNCAP_Array(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(

    _Length = None,
    _LayoutOption = None,
    _NumFigPair = None,

    _Array_row = None, #number: 1xnumber
    _Array_col = None,
    _Cbot_Ctop_metalwidth = None, #number

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

    _Length = None,
    _LayoutOption = None,
    _NumFigPair = None,

    _Array_row = None, #number: 1xnumber
    _Array_col = None,
    _Cbot_Ctop_metalwidth = None, #number

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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## HDVCAP Generation for calculation only
            ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C01_03_Array._Array._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length']                   = _Length
        _Caculation_Parameters['_LayoutOption']             = _LayoutOption
        _Caculation_Parameters['_NumFigPair']               = _NumFigPair
        _Caculation_Parameters['_Array']                    = _Array_col
        _Caculation_Parameters['_Cbot_Ctop_metalwidth']     = _Cbot_Ctop_metalwidth

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Array'] = self._SrefElementDeclaration(_DesignObj=C01_03_Array._Array(_DesignParameter=None, _Name='{}:SRF_Array'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Array']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Array']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Array']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        tmpXY = []
        tmpXY.append([0, 0])
                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Array']['_XYCoordinates'] = tmpXY

        for i in range(_Array_row - 1):
            tmp1 = self.get_param_KJH4('SRF_Array','BND_CBot_METAL{}'.format(_LayoutOption[-1]))
            target_coord = tmp1[-1][0][0]['_XY_up_left'] + [0,_Cbot_Ctop_metalwidth]
            approaching_coord = tmp1[0][0][0]['_XY_down_left']
            tmp3 = self.get_param_KJH4('SRF_Array')
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            # Define
            self._DesignParameter['SRF_Array']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Guardring Gen.
        ## Guardring
            ## Pre-defined
        _NumCont        = 3
        _right_margin   = 100
        _left_margin    = 100
        _up_margin      = 100
        _down_margin    = 100

            ## Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A10_PbodyRing_KJH3._PbodyRing._ParametersForDesignCalculation)
        _Caculation_Parameters['_XlengthIntn']      = None
        _Caculation_Parameters['_YlengthIntn']      = None
        _Caculation_Parameters['_NumContTop']       = _NumCont
        _Caculation_Parameters['_NumContBottom']    = _NumCont
        _Caculation_Parameters['_NumContLeft']      = _NumCont
        _Caculation_Parameters['_NumContRight']     = _NumCont

            ## Find Outter boundary
        tmp = self.get_outter_KJH4('SRF_Array')

            ## Define _XlengthIntn
        _Caculation_Parameters['_XlengthIntn'] = abs(tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0]) + _right_margin + _left_margin # option: + _NwellWidth

            ## Define _YlengthIntn
        _Caculation_Parameters['_YlengthIntn'] = abs(tmp['_Mostup']['coord'][0] - tmp['_Mostdown']['coord'][0]) + _up_margin + _down_margin # option + _NwellWidth

            ## Generate Sref
        self._DesignParameter['SRF_Pbodyring'] = self._SrefElementDeclaration(_DesignObj=A10_PbodyRing_KJH3._PbodyRing(_DesignParameter=None, _Name='{}:SRF_Pbodyring'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Pbodyring']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Pbodyring']['_Angle'] = 0

            ## Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_Pbodyring']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            ## Define Sref _XYcoordinate
        self._DesignParameter['SRF_Pbodyring']['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Pbodyring']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        target_coord = [tmp['_Mostleft']['coord'][0], tmp['_Mostdown']['coord'][0]]
                    ## Approaching_coord
                        ## x
        tmp2_1 = self.get_param_KJH4('SRF_Pbodyring', 'SRF_PbodyLeft', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coordx = tmp2_1[0][0][0][0][0]['_XY_right'][0]
                        ## y
        tmp2_2 = self.get_param_KJH4('SRF_Pbodyring', 'SRF_PbodyBottom', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coordy = tmp2_2[0][0][0][0][0]['_XY_up'][1]

        approaching_coord = [approaching_coordx, approaching_coordy]
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pbodyring')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] - _left_margin # option: - _NwellWidth
        New_Scoord[1] = New_Scoord[1] - _down_margin # option: - _NwellWidth
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Pbodyring']['_XYCoordinates'] = tmpXY

        #### Bot: Even / Top: Odd
        # Define Boundary_element
        self._DesignParameter['BND_MetLayer_CBotConn'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}'.format(_LayoutOption[-1])][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}'.format(_LayoutOption[-1])][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Array', 'BND_CBot_METAL{}'.format(_LayoutOption[-1]))

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_MetLayer_CBotConn']['_YWidth'] = tmp1[-1][0][0]['_XY_up_left'][1] - tmp1[0][0][0]['_XY_down_left'][1]

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_MetLayer_CBotConn']['_XWidth'] = tmp1[0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_MetLayer_CBotConn']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        tmp3 = self.get_param_KJH4('BND_MetLayer_CBotConn')

        for i in range(_Array_col//2 + 1):
            # Calculate
            # Target_coord
            target_coord = tmp1[0][i][0]['_XY_down_left']
            # Approaching_coord
            approaching_coord = tmp3[0][0]['_XY_down_left']
            # Sref coord
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        self._DesignParameter['BND_MetLayer_CBotConn']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_MetLayer_CTopConn'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}'.format(_LayoutOption[-1])][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}'.format(_LayoutOption[-1])][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Array', 'BND_CTop_METAL{}'.format(_LayoutOption[-1]))

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_MetLayer_CTopConn']['_YWidth'] = tmp1[-1][0][0]['_XY_up_left'][1] - tmp1[0][0][0]['_XY_down_left'][1]

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_MetLayer_CTopConn']['_XWidth'] = tmp1[0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_MetLayer_CTopConn']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        tmp3 = self.get_param_KJH4('BND_MetLayer_CTopConn')

        for i in range((_Array_col+1)//2):
            # Calculate
            # Target_coord
            target_coord = tmp1[0][i][0]['_XY_down_left']
            # Approaching_coord
            approaching_coord = tmp3[0][0]['_XY_down_left']
            # Sref coord
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        self._DesignParameter['BND_MetLayer_CTopConn']['_XYCoordinates'] = tmpXY


        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_AJH
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_A50_HDVNCAP_Array'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'A50_HDVNCAP_Array'
    _fileName = cellname + '.gds'

    InputParams = dict(

    _Length = 7800,
    _LayoutOption = [2,3,4,5], # Writedown [number1, number2, number3, ...]
    _NumFigPair = 30, #number (ref:75)

    _Array_row = 4, #number: row x col  O O O
    _Array_col = 5, #            2 x 3  O O O
    _Cbot_Ctop_metalwidth = 500, #number

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
    LayoutObj = _HDVNCAP_Array(_DesignParameter=None, _Name=cellname)
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
    Checker.lib_deletion()
    # Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()

    ''' Check Time'''
    elapsed_time = time.time() - start_time
    m, s = divmod(elapsed_time, 60)
    h, m = divmod(m, 60)

    print('#############################      Finished      ################################')
# end of 'main():' ---------------------------------------------------------------------------------------------
