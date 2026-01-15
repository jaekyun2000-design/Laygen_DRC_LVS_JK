
## Import Basic Modules
    ## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_ADC.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

    ## Library
import copy
import math
import numpy as np
import time
import re

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2


    ## Building blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.C01_HDVNCAP_Array import C01_02_Boundary



## Define Class
class _Array(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(

    _Length = None,
    _LayoutOption = None,
    _NumFigPair = None,

    _Array = None, #number: 1xnumber
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

    _Array = None, #number: 1xnumber
    _Cbot_Ctop_metalwidth = None, #number

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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## HDVCAP Generation for calculation only
            ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C01_02_Boundary._Boundary._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length']       = _Length
        _Caculation_Parameters['_LayoutOption'] = _LayoutOption
        _Caculation_Parameters['_NumFigPair']   = _NumFigPair

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_HDVNCAP_forCal'] = self._SrefElementDeclaration(_DesignObj=C01_02_Boundary._Boundary(_DesignParameter=None, _Name='{}:SRF_HDVNCAP_forCal'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_HDVNCAP_forCal']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_HDVNCAP_forCal']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_HDVNCAP_forCal']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_HDVNCAP_forCal']['_XYCoordinates'] = [[0, 0]]

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## CBot/Ctop --> HDVNCAP Gen.
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## CBot/Ctop gen
        ## Cbot or Ctop flag: if flag = 0, then Cbot
        flag = 0

        ## Cbot/Ctop metal ywidth
        tmp = self.get_param_KJH4('SRF_HDVNCAP_forCal', 'BND_PortA_Hrz_METAL{}'.format(_LayoutOption[-1]))
        cbot_ctop_metal_ywidth = tmp[0][0][0]['_Xwidth']
        del self._DesignParameter['SRF_HDVNCAP_forCal']

        ## Calculate Sref XYcoord
        tmpXY = []
        tmpXY2 = [[0, 0]]
        tmpXY3 = []
        tmpXY4 = []

        for i in range(0,_Array+1):
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## CBot
            if flag == 0:
                if i == 0:
                    ## Boundary_element Generation
                    ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
                    self._DesignParameter['BND_CBot_METAL{}'.format(_LayoutOption[-1])] = self._BoundaryElementDeclaration(
                        _Layer=DesignParameters._LayerMapping['METAL{}'.format(_LayoutOption[-1])][0],
                        _Datatype=DesignParameters._LayerMapping['METAL{}'.format(_LayoutOption[-1])][1],
                        _XWidth=None,
                        _YWidth=None,
                        _XYCoordinates=[],
                    )

                    ## Define Boundary_element _YWidth
                    self._DesignParameter['BND_CBot_METAL{}'.format(_LayoutOption[-1])]['_YWidth'] = cbot_ctop_metal_ywidth + 150

                    ## Define Boundary_element _XWidth
                    self._DesignParameter['BND_CBot_METAL{}'.format(_LayoutOption[-1])]['_XWidth'] = _Cbot_Ctop_metalwidth

                    ## Define Boundary_element _XYCoordinates
                    self._DesignParameter['BND_CBot_METAL{}'.format(_LayoutOption[-1])]['_XYCoordinates'] = [[0, 0]]

                if i != 0:
                    ## Calculate
                    ## Target_coord: _XY_type1
                    tmp1 = self.get_param_KJH4('SRF_HDVNCAP','BND_PortB_Hrz_METAL{}'.format(_LayoutOption[-1]))
                    target_coord = tmp1[-1][0][0]['_XY_down_left']
                    ## Approaching_coord: _XY_type2
                    tmp2 = self.get_param_KJH4('BND_CBot_METAL{}'.format(_LayoutOption[-1]))
                    approaching_coord = tmp2[0][0]['_XY_down_left']
                    ## Sref coord
                    tmp3 = self.get_param_KJH4('BND_CBot_METAL{}'.format(_LayoutOption[-1]))
                    Scoord = tmp3[0][0]['_XY_origin']
                    ## Cal
                    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                    tmpXY2.append(New_Scoord)
                    ## Define coordinates
                    self._DesignParameter['BND_CBot_METAL{}'.format(_LayoutOption[-1])]['_XYCoordinates'] = tmpXY2


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## CTop
            if flag == 1:
                if i == 1:
                    ## Boundary_element Generation
                    ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
                    self._DesignParameter['BND_CTop_METAL{}'.format(_LayoutOption[-1])] = self._BoundaryElementDeclaration(
                        _Layer=DesignParameters._LayerMapping['METAL{}'.format(_LayoutOption[-1])][0],
                        _Datatype=DesignParameters._LayerMapping['METAL{}'.format(_LayoutOption[-1])][1],
                        _XWidth=None,
                        _YWidth=None,
                        _XYCoordinates=[],
                    )

                    ## Define Boundary_element _YWidth
                    self._DesignParameter['BND_CTop_METAL{}'.format(_LayoutOption[-1])]['_YWidth'] = cbot_ctop_metal_ywidth + 150

                    ## Define Boundary_element _XWidth
                    self._DesignParameter['BND_CTop_METAL{}'.format(_LayoutOption[-1])]['_XWidth'] = _Cbot_Ctop_metalwidth

                    ## Define Boundary_element _XYCoordinates
                    self._DesignParameter['BND_CTop_METAL{}'.format(_LayoutOption[-1])]['_XYCoordinates'] = [[0, 0]]

                ## Calculate
                ## Target_coord: _XY_type1
                tmp1 = self.get_param_KJH4('SRF_HDVNCAP','BND_PortB_Hrz_METAL{}'.format(_LayoutOption[-1]))
                target_coord = tmp1[-1][0][0]['_XY_down_left']
                ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('BND_CTop_METAL{}'.format(_LayoutOption[-1]))
                approaching_coord = tmp2[0][0]['_XY_down_left']
                ## Sref coord
                tmp3 = self.get_param_KJH4('BND_CTop_METAL{}'.format(_LayoutOption[-1]))
                Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY3.append(New_Scoord)
                ## Define coordinates
                self._DesignParameter['BND_CTop_METAL{}'.format(_LayoutOption[-1])]['_XYCoordinates'] = tmpXY3


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## HDVCAP Generation
            if i == 0 :
                    ## SREF Generation
                        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
                _Caculation_Parameters = copy.deepcopy(C01_02_Boundary._Boundary._ParametersForDesignCalculation)
                        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
                _Caculation_Parameters['_Length']       = _Length
                _Caculation_Parameters['_LayoutOption'] = _LayoutOption
                _Caculation_Parameters['_NumFigPair']   = _NumFigPair

                        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
                self._DesignParameter['SRF_HDVNCAP'] = self._SrefElementDeclaration(_DesignObj=C01_02_Boundary._Boundary(_DesignParameter=None, _Name='{}:SRF_HDVNCAP'.format(_Name)))[0]

                        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
                self._DesignParameter['SRF_HDVNCAP']['_Reflect'] = [0, 0, 0]

                        ## Define Sref Angle: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_HDVNCAP']['_Angle'] = 90

                        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_HDVNCAP']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                    ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_HDVNCAP']['_XYCoordinates'] = [[0, 0]]

            if i != _Array:
                        ## if Cbot
                if flag == 0:

                    ## Calculate
                    ## Target_coord: _XY_type1
                    tmp1 = self.get_param_KJH4('BND_CBot_METAL{}'.format(_LayoutOption[-1]))
                    target_coord = tmp1[-1][0]['_XY_up_right']
                    ## Approaching_coord: _XY_type2
                    tmp2 = self.get_param_KJH4('SRF_HDVNCAP','BND_PortA_Hrz_METAL{}'.format(_LayoutOption[-1]))
                    approaching_coord = tmp2[0][0][0]['_XY_up_right']
                    ## Sref coord
                    tmp3 = self.get_param_KJH4('SRF_HDVNCAP')
                    Scoord = tmp3[0][0]['_XY_origin']
                    ## Cal
                    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                    tmpXY.append(New_Scoord)
                    ## Define coordinates
                    self._DesignParameter['SRF_HDVNCAP']['_XYCoordinates'] = tmpXY

                    flag = 1

                        ## if Ctop
                else:
                    ## Calculate
                    ## Target_coord: _XY_type1
                    tmp1 = self.get_param_KJH4('BND_CTop_METAL{}'.format(_LayoutOption[-1]))
                    target_coord = tmp1[-1][0]['_XY_up_right']
                    ## Approaching_coord: _XY_type2
                    tmp2 = self.get_param_KJH4('SRF_HDVNCAP','BND_PortA_Hrz_METAL{}'.format(_LayoutOption[-1]))
                    approaching_coord = tmp2[0][0][0]['_XY_up_right']
                    ## Sref coord
                    tmp3 = self.get_param_KJH4('SRF_HDVNCAP')
                    Scoord = tmp3[0][0]['_XY_origin']
                    ## Cal
                    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                    tmpXY.append(New_Scoord)
                    ## Define coordinates
                    self._DesignParameter['SRF_HDVNCAP']['_XYCoordinates'] = tmpXY

                    flag = 0

        '''
        ## Labeling:    PortA     ex)METAL1PIN, METAL2PIN, METAL3PIN, METAL4PIN, METAL5PIN, METAL6PIN, METAL7PIN, METAL8PIN(IA), METAL9PIN(IB),
        self._DesignParameter['TXT_PortA_Met{}Layer'.format(_LayoutOption[-1])] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}PIN'.format(_LayoutOption[-1])][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}PIN'.format(_LayoutOption[-1])][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.1, _Angle=0, _TEXT=None,
            _XYCoordinates=None,
        )

            # Portname
        self._DesignParameter['TXT_PortA_Met{}Layer'.format(_LayoutOption[-1])]['_TEXT'] = 'PortA'

            ## Define Coordinates
        tmp = self.get_param_KJH4('BND_CBot_METAL{}'.format(_LayoutOption[-1]))
        tmpXY = []
        for i in range(math.ceil((_Array+1)/2)):
            # range(math.ceil((_HDVNCAP_Array+1)/2))
            tmpXY.append(tmp[i][0]['_XY_cent'])

        self._DesignParameter['TXT_PortA_Met{}Layer'.format(_LayoutOption[-1])]['_XYCoordinates'] = tmpXY


        ## Labeling:    PortB     ex)METAL1PIN, METAL2PIN, METAL3PIN, METAL4PIN, METAL5PIN, METAL6PIN, METAL7PIN, METAL8PIN(IA), METAL9PIN(IB),
        self._DesignParameter['TXT_PortB_Met{}Layer'.format(_LayoutOption[-1])] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}PIN'.format(_LayoutOption[-1])][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}PIN'.format(_LayoutOption[-1])][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.1, _Angle=0, _TEXT=None,
            _XYCoordinates=None,
        )

            # Portname
        self._DesignParameter['TXT_PortB_Met{}Layer'.format(_LayoutOption[-1])]['_TEXT'] = 'PortB'

            ## Define Coordinates
        tmp = self.get_param_KJH4('BND_CTop_METAL{}'.format(_LayoutOption[-1]))
        tmpXY = []
        for i in range(int((_Array+1)/2)):
            tmpXY.append(tmp[i][0]['_XY_cent'])
        self._DesignParameter['TXT_PortB_Met{}Layer'.format(_LayoutOption[-1])]['_XYCoordinates'] = tmpXY
        '''




        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## CBot/Ctop --> HDVNCAP Gen.


        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ADC_C01_HDVNCAP'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'C01_02_Array_v0_71'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

    _Length = 500, #Ref:5000
    _LayoutOption = [3,4,5,6], # Writedown [number1, number2, number3, ...]
    _NumFigPair = 5, #Ref:75

    _Array = 3, #number: 1xnumber
    _Cbot_Ctop_metalwidth = 1000, #number
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
    LayoutObj = _Array(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('###############      Sending to FTP Server...      ##################')
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
