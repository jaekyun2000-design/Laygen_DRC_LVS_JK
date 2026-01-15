
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

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A03_NmosWithDummy_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A04_PmosWithDummy_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A05_NbodyContact_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A06_PbodyContact_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A07_NbodyContactPhyLen_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A08_PbodyContactPhyLen_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A09_NbodyRing_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A10_PbodyRing_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A11_NbodyContactforDeepNwell_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A12_NbodyContactPhyLenforDeepNwell_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A13_NbodyRingforDeepNwell_KJH

    ##
from KJH91_Projects.Project_ADC.Layoutgen_code.C00_Tr1Tr2_VinVout_Fixed import C00_03_Guardring
from KJH91_Projects.Project_ADC.Layoutgen_code.C02_Tr5Tr7Tr9_Ctop_Fixed import C02_04_Guardring
from KJH91_Projects.Project_ADC.Layoutgen_code.C03_Tr4_Fixed import C03_02_Pin
from KJH91_Projects.Project_ADC.Layoutgen_code.C05_Tr8_Fixed import C05_02_Pin



## Define Class
class _Tr1Tr2_Tr5Tr7Tr9_Tr4_Tr8(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
# Input/Output node
    # INPUT node
    _Inputnode_width = 500,  # number
    # OUTPUT node
    _Outputnode_width = 500,  # number

# TR1
    # Physical dimension
    _Tr1_NumberofGate	            = 12,       # Number
    _Tr1_ChannelWidth	            = 100,     # Number
    _Tr1_ChannelLength	            = 30,       # Number
    _Tr1_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR2
    # Physical dimension
    _Tr2_NumberofGate	            = 5,       # Number
    _Tr2_ChannelWidth	            = 700,     # Number
    _Tr2_ChannelLength	            = 30,       # Number
    _Tr2_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR4
    # Physical dimension
    _Tr4_NumberofGate	= 4,       # Number
    _Tr4_ChannelWidth	            = 500,     # Number
    _Tr4_ChannelLength	            = 30,       # Number
    _Tr4_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR5
    # Physical dimension
    _Tr5_NumberofGate	= 2,       # Number
    _Tr5_ChannelWidth	            = 1000,     # Number
    _Tr5_ChannelLength	            = 30,       # Number
    _Tr5_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR7
    # Physical dimension
    _Tr7_NumberofGate               = 3,  # Number
    _Tr7_ChannelWidth	            = 233,     # Number
    _Tr7_ChannelLength	            = 30,       # Number
    _Tr7_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR9
    # Physical dimension
    _Tr9_NumberofGate               = 3,  # Number
    _Tr9_ChannelWidth	            = 500,     # Number
    _Tr9_ChannelLength	            = 30,       # Number
    _Tr9_XVT				        = 'LVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR8
    # Physical dimension
    _Tr8_NumberofGate	= 4,       # Number
    _Tr8_ChannelWidth	            = 500,     # Number
    _Tr8_ChannelLength	            = 30,       # Number
    _Tr8_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
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
# Input/Output node
    # INPUT node
    _Inputnode_width = 500,  # number
    # OUTPUT node
    _Outputnode_width = 500,  # number

# TR1
    # Physical dimension
    _Tr1_NumberofGate	            = 12,       # Number
    _Tr1_ChannelWidth	            = 100,     # Number
    _Tr1_ChannelLength	            = 30,       # Number
    _Tr1_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR2
    # Physical dimension
    _Tr2_NumberofGate	            = 5,       # Number
    _Tr2_ChannelWidth	            = 700,     # Number
    _Tr2_ChannelLength	            = 30,       # Number
    _Tr2_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR4
    # Physical dimension
    _Tr4_NumberofGate	= 4,       # Number
    _Tr4_ChannelWidth	            = 500,     # Number
    _Tr4_ChannelLength	            = 30,       # Number
    _Tr4_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR5
    # Physical dimension
    _Tr5_NumberofGate	= 2,       # Number
    _Tr5_ChannelWidth	            = 1000,     # Number
    _Tr5_ChannelLength	            = 30,       # Number
    _Tr5_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR7
    # Physical dimension
    _Tr7_NumberofGate               = 3,  # Number
    _Tr7_ChannelWidth	            = 233,     # Number
    _Tr7_ChannelLength	            = 30,       # Number
    _Tr7_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR9
    # Physical dimension
    _Tr9_NumberofGate               = 3,  # Number
    _Tr9_ChannelWidth	            = 500,     # Number
    _Tr9_ChannelLength	            = 30,       # Number
    _Tr9_XVT				        = 'LVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR8
    # Physical dimension
    _Tr8_NumberofGate	= 4,       # Number
    _Tr8_ChannelWidth	            = 500,     # Number
    _Tr8_ChannelLength	            = 30,       # Number
    _Tr8_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT


                                  ):

        ## Class_HEADER: Pre Defined Parameter Before Calculation
            ## Load DRC library
        _DRCobj = DRC.DRC()
            ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ## CALCULATION START
        start_time = time.time()
        # end_time = time.time()
        # self.elapsed_time = end_time - start_time
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr4
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr4: Sref Gen
        ## SREF Generation
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C03_02_Pin._Pin._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr4_NumberofGate'] = _Tr4_NumberofGate
        _Caculation_Parameters['_Tr4_ChannelWidth'] = _Tr4_ChannelWidth
        _Caculation_Parameters['_Tr4_ChannelLength'] = _Tr4_ChannelLength
        _Caculation_Parameters['_Tr4_XVT'] = _Tr4_XVT

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_C03_02_Pin'] = self._SrefElementDeclaration(_DesignObj=C03_02_Pin._Pin(_DesignParameter=None, _Name='{}:SRF_C03_02_Pin'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_C03_02_Pin']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C03_02_Pin']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C03_02_Pin']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C03_02_Pin']['_XYCoordinates'] = [[0, 0]]


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr5Tr7Tr9
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr5Tr7Tr9: Sref Gen
            ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C02_04_Guardring._Guardring._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr5_NumberofGate']     = _Tr5_NumberofGate
        _Caculation_Parameters['_Tr5_ChannelWidth']     = _Tr5_ChannelWidth
        _Caculation_Parameters['_Tr5_ChannelLength']    = _Tr5_ChannelLength
        _Caculation_Parameters['_Tr5_XVT']              = _Tr5_XVT

        _Caculation_Parameters['_Tr7_NumberofGate']     = _Tr7_NumberofGate
        _Caculation_Parameters['_Tr7_ChannelWidth']     = _Tr7_ChannelWidth
        _Caculation_Parameters['_Tr7_ChannelLength']    = _Tr7_ChannelLength
        _Caculation_Parameters['_Tr7_XVT']              = _Tr7_XVT

        _Caculation_Parameters['_Tr9_NumberofGate']     = _Tr9_NumberofGate
        _Caculation_Parameters['_Tr9_ChannelWidth']     = _Tr9_ChannelWidth
        _Caculation_Parameters['_Tr9_ChannelLength']    = _Tr9_ChannelLength
        _Caculation_Parameters['_Tr9_XVT']              = _Tr9_XVT


                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_C02_04_Guardring'] = self._SrefElementDeclaration(_DesignObj=C02_04_Guardring._Guardring(_DesignParameter=None, _Name='{}:SRF_C02_04_Guardring'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_C02_04_Guardring']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C02_04_Guardring']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C02_04_Guardring']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C02_04_Guardring']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##x
        tmp1_1 = self.get_outter_KJH4('SRF_C03_02_Pin','SRF_Pbodyring2')
        target_coordx = tmp1_1['_Mostright']['coord'][0]
                                ##y
        tmp1_2 = self.get_param_KJH4('SRF_C03_02_Pin','SRF_Guardring','SRF_Tr4','SRF_Nmos','BND_Drain_Hrz_M2')
        target_coordy = tmp1_2[0][0][0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##x
        tmp2_1 = self.get_outter_KJH4('SRF_C02_04_Guardring','SRF_Pbodyring')
        approaching_coordx = tmp2_1['_Mostleft']['coord'][0]
                                ##y
        tmp2_2 = self.get_param_KJH4('SRF_C02_04_Guardring','SRF_Tr5Tr7Tr9','SRF_Tr5','BND_Drain_Hrz_M2')
        approaching_coordy = tmp2_2[0][0][0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_C02_04_Guardring')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        tmp4_1 = target_coordx
        tmp4_2 = self.get_param_KJH4('SRF_C03_02_Pin','SRF_Guardring', 'BND_Deepnwell')[0][0][0][0]['_XY_right'][0]
        tmp5_1 = self.get_param_KJH4('SRF_C02_04_Guardring','BND_Deepnwell')[0][0][0]['_XY_left'][0]
        tmp5_2 = approaching_coordx
        C02C03MinSpace = _DRCobj._T3toT3minspace - (tmp4_1 - tmp4_2) - (tmp5_1 - tmp5_2)
        C02C03space = 1200
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] + max(C02C03MinSpace, C02C03space)
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_C02_04_Guardring']['_XYCoordinates'] = tmpXY



        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr8
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr8: Sref Gen
            ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C05_02_Pin._Pin._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr8_NumberofGate']     = _Tr8_NumberofGate
        _Caculation_Parameters['_Tr8_ChannelWidth']     = _Tr8_ChannelWidth
        _Caculation_Parameters['_Tr8_ChannelLength']    = _Tr8_ChannelLength
        _Caculation_Parameters['_Tr8_XVT']              = _Tr8_XVT

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_C05_02_Pin'] = self._SrefElementDeclaration(_DesignObj=C05_02_Pin._Pin(_DesignParameter=None, _Name='{}:SRF_C05_02_Pin'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_C05_02_Pin']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C05_02_Pin']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C05_02_Pin']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C05_02_Pin']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##x
        tmp1_1 = self.get_outter_KJH4('SRF_C02_04_Guardring','SRF_Pbodyring')
        target_coordx = tmp1_1['_Mostright']['coord'][0]
                                ##y
        tmp1_2 = self.get_param_KJH4('SRF_C02_04_Guardring','BND_Tr7_Source_Tr9_Gate_Hrz_M2')
        target_coordy = tmp1_2[0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##x
        tmp2_1 = self.get_outter_KJH4('SRF_C05_02_Pin','SRF_Pbodyring2')
        approaching_coordx = tmp2_1['_Mostleft']['coord'][0]
                                ##y
        tmp2_2 = self.get_param_KJH4('SRF_C05_02_Pin','SRF_Guardring','SRF_Tr8','SRF_Nmos','BND_Drain_Hrz_M2')
        approaching_coordy = tmp2_2[0][0][0][0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_C05_02_Pin')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        tmp4_1 = target_coordx
        tmp4_2 = self.get_param_KJH4('SRF_C02_04_Guardring', 'BND_Deepnwell')[0][0][0]['_XY_right'][0]
        tmp5_1 = self.get_param_KJH4('SRF_C05_02_Pin', 'SRF_Guardring', 'BND_Deepnwell')[0][0][0][0]['_XY_left'][0]
        tmp5_2 = approaching_coordx
        C02C05MinSpace = _DRCobj._T3toT3minspace - abs(tmp4_1 - tmp4_2) - abs(tmp5_1 - tmp5_2)
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        C02C05space = 1200
        New_Scoord[0] = New_Scoord[0] + max(C02C05MinSpace, C02C05space)
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_C05_02_Pin']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr1Tr2
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr1Tr2: Sref Gen
            ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C00_03_Guardring._Guardring._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr1_NumberofGate']     = _Tr1_NumberofGate
        _Caculation_Parameters['_Tr1_ChannelWidth']     = _Tr1_ChannelWidth
        _Caculation_Parameters['_Tr1_ChannelLength']    = _Tr1_ChannelLength
        _Caculation_Parameters['_Tr1_XVT']              = _Tr1_XVT

        _Caculation_Parameters['_Tr2_NumberofGate']     = _Tr2_NumberofGate
        _Caculation_Parameters['_Tr2_ChannelWidth']     = _Tr2_ChannelWidth
        _Caculation_Parameters['_Tr2_ChannelLength']    = _Tr2_ChannelLength
        _Caculation_Parameters['_Tr2_XVT']              = _Tr2_XVT

        _Caculation_Parameters['_Inputnode_width']          = _Inputnode_width
        _Caculation_Parameters['_Outputnode_width']         = _Outputnode_width

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_C00_03_Guardring'] = self._SrefElementDeclaration(_DesignObj=C00_03_Guardring._Guardring(_DesignParameter=None, _Name='{}:SRF_C00_03_Guardring'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_C00_03_Guardring']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C00_03_Guardring']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C00_03_Guardring']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C00_03_Guardring']['_XYCoordinates'] = [[0, 0]]


                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##x
        tmp1_1 = self.get_param_KJH4('SRF_C02_04_Guardring','SRF_Tr5Tr7Tr9','SRF_Tr5','BND_Drain_Hrz_M2')
        target_coordx = tmp1_1[0][0][0][0][0]['_XY_right'][0]
                                ##y
        tmp1_2 = self.get_outter_KJH4('SRF_C05_02_Pin','SRF_Pbodyring2')
        tmp1_3 = self.get_outter_KJH4('SRF_C02_04_Guardring', 'SRF_Pbodyring')
        tmp1_4 = self.get_outter_KJH4('SRF_C03_02_Pin', 'SRF_Pbodyring2')
        tmp1_5 = min(tmp1_2['_Mostdown']['coord'][0],tmp1_3['_Mostdown']['coord'][0],tmp1_4['_Mostdown']['coord'][0])
        target_coordy = tmp1_5

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##x
        tmp2_1 = self.get_param_KJH4('SRF_C00_03_Guardring','SRF_Tr1Tr2','SRF_Tr2','BND_Gate_Hrz_M3')
        approaching_coordx = tmp2_1[0][0][0][0][0]['_XY_right'][0]
                                ##y
        tmp2_2 = self.get_outter_KJH4('SRF_C00_03_Guardring','SRF_Pbodyring2')
        approaching_coordy = tmp2_2['_Mostup']['coord'][0]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_C00_03_Guardring')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        C00C03space = 500
        New_Scoord[1] = New_Scoord[1] - max(_DRCobj._PpMinSpace, C00C03space)
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_C00_03_Guardring']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## VN node
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Vn node: M2 Vtc
            ## pre-defined
        Vn_vtc_metal_width = 300

            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Vn_Vtc_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_C00_03_Guardring','SRF_Tr1Tr2','SRF_Tr2','SRF_Gate_ViaM0M3','SRF_ViaM1M2','BND_Met2Layer')
        tmp2 =self.get_param_KJH4('SRF_C02_04_Guardring','SRF_Tr5Tr7Tr9','SRF_Tr5','BND_Drain_Hrz_M2')

        self._DesignParameter['BND_Vn_Vtc_M2']['_YWidth'] = abs( tmp2[0][0][0][0][0]['_XY_down'][1] - tmp1[0][0][0][0][0][0][0]['_XY_down'][1] )

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Vn_Vtc_M2']['_XWidth'] = Vn_vtc_metal_width

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Vn_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Vn_Vtc_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_C00_03_Guardring','SRF_Tr1Tr2','SRF_Tr2','BND_Gate_Hrz_M3')
        target_coord = tmp1[0][0][0][0][0]['_XY_down_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Vn_Vtc_M2')
        approaching_coord = tmp2[0][0]['_XY_down_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Vn_Vtc_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Vn_Vtc_M2']['_XYCoordinates'] = tmpXY


            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Vn node: M2 Hrz
            ## pre-defined
        Vn_vtc_metal_width = 300

            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Vn_Hrz_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Vn_Hrz_M2']['_YWidth'] = Vn_vtc_metal_width

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_C03_02_Pin','SRF_Guardring','SRF_Tr4','SRF_Nmos','BND_Drain_Hrz_M2')
        tmp2 =self.get_param_KJH4('SRF_C02_04_Guardring','SRF_Tr5Tr7Tr9','SRF_Tr5','BND_Drain_Hrz_M2')

        self._DesignParameter['BND_Vn_Hrz_M2']['_XWidth'] = abs( tmp2[0][0][0][0][0]['_XY_right'][0] - tmp1[0][0][0][0][0][0]['_XY_left'][0] )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Vn_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Vn_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_C02_04_Guardring','SRF_Tr5Tr7Tr9','SRF_Tr5','BND_Drain_Hrz_M2')
        target_coord = tmp1[0][0][0][0][0]['_XY_down_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Vn_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Vn_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Vn_Hrz_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## VG node
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## VG node: M2 Hrz
        ## pre-defined
        Vg_hrz_metal_width = 300

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Vg_Hrz_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Vg_Hrz_M2']['_YWidth'] = Vg_hrz_metal_width

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_C05_02_Pin', 'SRF_Guardring', 'SRF_Tr8','SRF_Nmos' ,'BND_Drain_Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_C02_04_Guardring', 'SRF_Tr5Tr7Tr9', 'SRF_Tr7', 'BND_Source_Hrz_M2')

        self._DesignParameter['BND_Vg_Hrz_M2']['_XWidth'] = abs(tmp1[0][0][0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Vg_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Vg_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_C05_02_Pin', 'SRF_Guardring', 'SRF_Tr8','SRF_Nmos', 'BND_Drain_Hrz_M2')
        target_coord = tmp1[0][0][0][0][0][0]['_XY_up_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Vg_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Vg_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Vg_Hrz_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Path_element Generation 2
        ## Path Name:
        Path_name = 'Vg_Tr1toTr8_M2'

        ## Path Width: ***** must be even number ***
        Path_width = Vg_hrz_metal_width

        ## tmp
        tmpXY = []
        tmpMetal = []
        tmpViaTF = []
        tmpViaDir = []
        tmpViaWid = []

        ## coord1
        ## P1 calculation
        tmp = self.get_param_KJH4('SRF_C00_03_Guardring','SRF_Tr1Tr2','SRF_Tr1','BND_Gate_Hrz_M3')
        P1 = tmp[0][0][0][0][0]['_XY_down_right']
        ## P2 calculation
        tmp1_2 = self.get_param_KJH4('BND_Vg_Hrz_M2')
        P2 = [tmp[0][0][0][0][0]['_XY_down_right'][0],tmp1_2[0][0]['_XY_right'][1]]
        ## Metal Layer
        Metal = 2
        ## Via: True=1/False=0
        ViaTF = 0
        ## Via: Vtc=1/Hrz=0/Ovl=2
        ViaDir = 1
        ## Via width: None/[1,3]
        ViaWid = None

        tmpXY.append([P1, P2])
        tmpMetal.append(Metal)
        tmpViaTF.append(ViaTF)
        tmpViaDir.append(ViaDir)
        tmpViaWid.append(ViaWid)

        ## coord2
        ## P1 calculation
        P1 = copy.deepcopy(P2)
        ## P2 calculation
        tmp = self.get_param_KJH4('BND_Vg_Hrz_M2')
        P2 = tmp[0][0]['_XY_right']
        ## Metal Layer
        Metal = 2
        ## Via True=1/False=0
        ViaTF = 0
        ## Via Vtc=1/Hrz=0/Ovl=2
        ViaDir = 2
        ## Via width: None/[1,3]
        ViaWid = None

        tmpXY.append([P1, P2])
        tmpMetal.append(Metal)
        tmpViaTF.append(ViaTF)
        tmpViaDir.append(ViaDir)
        tmpViaWid.append(ViaWid)


        tmpXY = self.get_PTH_KJH2(Path_name, Path_width, tmpXY, tmpMetal, tmpViaTF, tmpViaDir, tmpViaWid, _Name)

        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')
        # start_time = time.time()
        end_time = time.time()
        self.elapsed_time = end_time - start_time

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ZZ01_C12_00_Tr1Tr2_Tr5Tr7Tr9_Tr4_Tr8_Fixed'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'C12_00_Tr1Tr2_Tr5Tr7Tr9_Tr4_Tr8_v0_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
# Input/Output node
    # INPUT node
    _Inputnode_width = 500,  # number
    # OUTPUT node
    _Outputnode_width = 500,  # number

# TR1
    # Physical dimension
    _Tr1_NumberofGate	            = 1,       # Number
    _Tr1_ChannelWidth	            = 100,     # Number
    _Tr1_ChannelLength	            = 30,       # Number
    _Tr1_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR2
    # Physical dimension
    _Tr2_NumberofGate	            = 5,       # Number
    _Tr2_ChannelWidth	            = 700,     # Number
    _Tr2_ChannelLength	            = 30,       # Number
    _Tr2_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR4
    # Physical dimension
    _Tr4_NumberofGate	            = 4,       # Number
    _Tr4_ChannelWidth	            = 500,     # Number
    _Tr4_ChannelLength	            = 30,       # Number
    _Tr4_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR5
    # Physical dimension
    _Tr5_NumberofGate	            = 2,       # Number
    _Tr5_ChannelWidth	            = 1000,     # Number
    _Tr5_ChannelLength	            = 30,       # Number
    _Tr5_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR7
    # Physical dimension
    _Tr7_NumberofGate               = 3,  # Number
    _Tr7_ChannelWidth	            = 233,     # Number
    _Tr7_ChannelLength	            = 30,       # Number
    _Tr7_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR9
    # Physical dimension
    _Tr9_NumberofGate               = 3,  # Number
    _Tr9_ChannelWidth	            = 500,     # Number
    _Tr9_ChannelLength	            = 30,       # Number
    _Tr9_XVT				        = 'LVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR8
    # Physical dimension
    _Tr8_NumberofGate	= 4,       # Number
    _Tr8_ChannelWidth	            = 500,     # Number
    _Tr8_ChannelLength	            = 30,       # Number
    _Tr8_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT


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
    LayoutObj = _Tr1Tr2_Tr5Tr7Tr9_Tr4_Tr8(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    ''' Check Time'''
    elapsed_time = time.time() - start_time
    m, s = divmod(elapsed_time, 60)
    h, m = divmod(m, 60)

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
    # Checker.lib_deletion()
    Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()

    print('#############################      Finished      ################################')
    print('{} Hours   {} minutes   {} seconds'.format(h, m, s))
# end of 'main():' ---------------------------------------------------------------------------------------------
