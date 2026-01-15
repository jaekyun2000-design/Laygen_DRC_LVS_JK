## Import Basic Modules
    ## Engine
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Library_and_Engine import DesignParameters
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Library_and_Engine import DRC
#from KJH91_Projects.Project_ADC.Library_and_Engine import DRCv2

    ## Library
import copy
import math
import numpy as np
import time

    ## KJH91 Basic Building Blocks
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.C13_C07C11C12TieCellsRouted_Fixed import C13_00_C07C11C12TieCellsRouted_YJ_v01_00_random
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.C01_HDVNCAP_Array_Fixed import C01_04_Guardring_random
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3

## Define Class
class _CtopCbotRouted(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
## Bootstrapped Switch
    # Input/Output node
        # INPUT node
        _Sampler_Inputnode_width = 500,  # number
        # OUTPUT node
        _Sampler_Outputnode_width = 500,  # number
    # TR1
        # Physical dimension
        _Sampler_Tr1_NumberofGate	            = 1,       # Number
        _Sampler_Tr1_ChannelWidth	            = 100,     # Number
        _Sampler_Tr1_ChannelLength	            = 30,       # Number
        _Sampler_Tr1_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # TR2
        # Physical dimension
        _Sampler_Tr2_NumberofGate	            = 5,       # Number
        _Sampler_Tr2_ChannelWidth	            = 700,     # Number
        _Sampler_Tr2_ChannelLength	            = 30,       # Number
        _Sampler_Tr2_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # TR4
        # Physical dimension
        _Sampler_Tr4_NumberofGate	            = 4,       # Number
        _Sampler_Tr4_ChannelWidth	            = 500,     # Number
        _Sampler_Tr4_ChannelLength	            = 30,       # Number
        _Sampler_Tr4_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # TR5
        # Physical dimension
        _Sampler_Tr5_NumberofGate	            = 2,       # Number
        _Sampler_Tr5_ChannelWidth	            = 1000,     # Number
        _Sampler_Tr5_ChannelLength	            = 30,       # Number
        _Sampler_Tr5_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # TR7
        # Physical dimension
        _Sampler_Tr7_NumberofGate               = 3,  # Number
        _Sampler_Tr7_ChannelWidth	            = 233,     # Number
        _Sampler_Tr7_ChannelLength	            = 30,       # Number
        _Sampler_Tr7_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # TR9
        # Physical dimension
        _Sampler_Tr9_NumberofGate               = 3,  # Number
        _Sampler_Tr9_ChannelWidth	            = 500,     # Number
        _Sampler_Tr9_ChannelLength	            = 30,       # Number
        _Sampler_Tr9_XVT				        = 'LVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # TR8
        # Physical dimension
        _Sampler_Tr8_NumberofGate	            = 4,       # Number
        _Sampler_Tr8_ChannelWidth	            = 500,     # Number
        _Sampler_Tr8_ChannelLength	            = 30,       # Number
        _Sampler_Tr8_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # TR6
        # Physical dimension
        _Sampler_Tr6_NumberofGate	            = 1,       # Number
        _Sampler_Tr6_ChannelWidth	            = 500,     # Number
        _Sampler_Tr6_ChannelLength	            = 30,       # Number
        _Sampler_Tr6_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # TR11
        # Physical dimension
        _Sampler_Tr11_NumberofGate	            = 20,       # Number
        _Sampler_Tr11_ChannelWidth	            = 500,     # Number
        _Sampler_Tr11_ChannelLength	            = 30,       # Number
        _Sampler_Tr11_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # Tie4N
        # Physical dimension
        _Sampler_Tie4N_NumberofGate     	    = 5,       # Number
        _Sampler_Tie4N_ChannelWidth	            = 250,     # Number
        _Sampler_Tie4N_ChannelLength	        = 30,       # Number
        _Sampler_Tie4N_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # Tie4P
        # Physical dimension
        _Sampler_Tie4P_NumberofGate	            = 5,       # Number
        _Sampler_Tie4P_ChannelWidth	            = 500,     # Number
        _Sampler_Tie4P_ChannelLength	        = 30,       # Number
        _Sampler_Tie4P_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # Tie8N
        # Physical dimension
        _Sampler_Tie8N_NumberofGate	            = 4,       # Number
        _Sampler_Tie8N_ChannelWidth	            = 250,     # Number
        _Sampler_Tie8N_ChannelLength	        = 30,       # Number
        _Sampler_Tie8N_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # Tie8P
        # Physical dimension
        _Sampler_Tie8P_NumberofGate	            = 4,       # Number
        _Sampler_Tie8P_ChannelWidth	            = 500,     # Number
        _Sampler_Tie8P_ChannelLength	        = 30,       # Number
        _Sampler_Tie8P_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # TR12
        # Physical dimension
        _Sampler_Tr12_NumberofGate	            = 4,       # Number
        _Sampler_Tr12_ChannelWidth	            = 1500,     # Number
        _Sampler_Tr12_ChannelLength	            = 30,       # Number
        _Sampler_Tr12_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # TR3
        # Physical dimension
        _Sampler_Tr3_NumberofGate	            = 2,       # Number
        _Sampler_Tr3_ChannelWidth	            = 100,     # Number
        _Sampler_Tr3_ChannelLength	            = 30,       # Number
        _Sampler_Tr3_XVT				        = 'LVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # TR10
        # Physical dimension
        _Sampler_Tr10_NumberofGate	            = 8,       # Number
        _Sampler_Tr10_ChannelWidth	            = 780,     # Number
        _Sampler_Tr10_ChannelLength	            = 30,       # Number
        _Sampler_Tr10_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

    # HDVNCAP
        _Sampler_HDVNCAP_Length = 7000,
        _Sampler_HDVNCAP_LayoutOption = [3,4,5,6], # Writedown [number1, number2, number3, ...]
        _Sampler_HDVNCAP_NumFigPair = 62, #number (ref:75)

        _Sampler_HDVNCAP_Array = 3, #number: 1xnumber
        _Sampler_HDVNCAP_Cbot_Ctop_metalwidth = 1000, #number
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
## Bootstrapped Switch
    # Input/Output node
        # INPUT node
        _Sampler_Inputnode_width = 500,  # number
        # OUTPUT node
        _Sampler_Outputnode_width = 500,  # number
    # TR1
        # Physical dimension
        _Sampler_Tr1_NumberofGate	            = 1,       # Number
        _Sampler_Tr1_ChannelWidth	            = 100,     # Number
        _Sampler_Tr1_ChannelLength	            = 30,       # Number
        _Sampler_Tr1_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # TR2
        # Physical dimension
        _Sampler_Tr2_NumberofGate	            = 5,       # Number
        _Sampler_Tr2_ChannelWidth	            = 700,     # Number
        _Sampler_Tr2_ChannelLength	            = 30,       # Number
        _Sampler_Tr2_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # TR4
        # Physical dimension
        _Sampler_Tr4_NumberofGate	            = 4,       # Number
        _Sampler_Tr4_ChannelWidth	            = 500,     # Number
        _Sampler_Tr4_ChannelLength	            = 30,       # Number
        _Sampler_Tr4_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # TR5
        # Physical dimension
        _Sampler_Tr5_NumberofGate	            = 2,       # Number
        _Sampler_Tr5_ChannelWidth	            = 1000,     # Number
        _Sampler_Tr5_ChannelLength	            = 30,       # Number
        _Sampler_Tr5_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # TR7
        # Physical dimension
        _Sampler_Tr7_NumberofGate               = 3,  # Number
        _Sampler_Tr7_ChannelWidth	            = 233,     # Number
        _Sampler_Tr7_ChannelLength	            = 30,       # Number
        _Sampler_Tr7_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # TR9
        # Physical dimension
        _Sampler_Tr9_NumberofGate               = 3,  # Number
        _Sampler_Tr9_ChannelWidth	            = 500,     # Number
        _Sampler_Tr9_ChannelLength	            = 30,       # Number
        _Sampler_Tr9_XVT				        = 'LVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # TR8
        # Physical dimension
        _Sampler_Tr8_NumberofGate	            = 4,       # Number
        _Sampler_Tr8_ChannelWidth	            = 500,     # Number
        _Sampler_Tr8_ChannelLength	            = 30,       # Number
        _Sampler_Tr8_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # TR6
        # Physical dimension
        _Sampler_Tr6_NumberofGate	            = 1,       # Number
        _Sampler_Tr6_ChannelWidth	            = 500,     # Number
        _Sampler_Tr6_ChannelLength	            = 30,       # Number
        _Sampler_Tr6_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # TR11
        # Physical dimension
        _Sampler_Tr11_NumberofGate	            = 20,       # Number
        _Sampler_Tr11_ChannelWidth	            = 500,     # Number
        _Sampler_Tr11_ChannelLength	            = 30,       # Number
        _Sampler_Tr11_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # Tie4N
        # Physical dimension
        _Sampler_Tie4N_NumberofGate     	    = 5,       # Number
        _Sampler_Tie4N_ChannelWidth	            = 250,     # Number
        _Sampler_Tie4N_ChannelLength	        = 30,       # Number
        _Sampler_Tie4N_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # Tie4P
        # Physical dimension
        _Sampler_Tie4P_NumberofGate	            = 5,       # Number
        _Sampler_Tie4P_ChannelWidth	            = 500,     # Number
        _Sampler_Tie4P_ChannelLength	        = 30,       # Number
        _Sampler_Tie4P_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # Tie8N
        # Physical dimension
        _Sampler_Tie8N_NumberofGate	            = 4,       # Number
        _Sampler_Tie8N_ChannelWidth	            = 250,     # Number
        _Sampler_Tie8N_ChannelLength	        = 30,       # Number
        _Sampler_Tie8N_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # Tie8P
        # Physical dimension
        _Sampler_Tie8P_NumberofGate	            = 4,       # Number
        _Sampler_Tie8P_ChannelWidth	            = 500,     # Number
        _Sampler_Tie8P_ChannelLength	        = 30,       # Number
        _Sampler_Tie8P_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # TR12
        # Physical dimension
        _Sampler_Tr12_NumberofGate	            = 4,       # Number
        _Sampler_Tr12_ChannelWidth	            = 1500,     # Number
        _Sampler_Tr12_ChannelLength	            = 30,       # Number
        _Sampler_Tr12_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # TR3
        # Physical dimension
        _Sampler_Tr3_NumberofGate	            = 2,       # Number
        _Sampler_Tr3_ChannelWidth	            = 100,     # Number
        _Sampler_Tr3_ChannelLength	            = 30,       # Number
        _Sampler_Tr3_XVT				        = 'LVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
    # TR10
        # Physical dimension
        _Sampler_Tr10_NumberofGate	            = 8,       # Number
        _Sampler_Tr10_ChannelWidth	            = 780,     # Number
        _Sampler_Tr10_ChannelLength	            = 30,       # Number
        _Sampler_Tr10_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

    # HDVNCAP
        _Sampler_HDVNCAP_Length = 7000,
        _Sampler_HDVNCAP_LayoutOption = [3,4,5,6], # Writedown [number1, number2, number3, ...]
        _Sampler_HDVNCAP_NumFigPair = 62, #number (ref:75)

        _Sampler_HDVNCAP_Array = 3, #number: 1xnumber
        _Sampler_HDVNCAP_Cbot_Ctop_metalwidth = 1000, #number
                                  ):


            ## Load DRC library
        _DRCobj = DRC.DRC()
            ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ## CALCULATION START
        C13_01_CtopCbotRouted_YJ_v01_00_start_time = time.time()
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')



            ## C13_00(C07C11C12TieCellsRouted) SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C13_00_C07C11C12TieCellsRouted_YJ_v01_00_random._C07C11C12TieCellsRouted._ParametersForDesignCalculation)

        _Caculation_Parameters['_Inputnode_width']     = _Sampler_Inputnode_width
        _Caculation_Parameters['_Outputnode_width']     = _Sampler_Outputnode_width

        _Caculation_Parameters['_Tr1_NumberofGate']     = _Sampler_Tr1_NumberofGate
        _Caculation_Parameters['_Tr1_ChannelWidth']     = _Sampler_Tr1_ChannelWidth
        _Caculation_Parameters['_Tr1_ChannelLength']    = _Sampler_Tr1_ChannelLength
        _Caculation_Parameters['_Tr1_XVT']              = _Sampler_Tr1_XVT

        _Caculation_Parameters['_Tr2_NumberofGate']     = _Sampler_Tr2_NumberofGate
        _Caculation_Parameters['_Tr2_ChannelWidth']     = _Sampler_Tr2_ChannelWidth
        _Caculation_Parameters['_Tr2_ChannelLength']    = _Sampler_Tr2_ChannelLength
        _Caculation_Parameters['_Tr2_XVT']              = _Sampler_Tr2_XVT

        _Caculation_Parameters['_Tr4_NumberofGate']     = _Sampler_Tr4_NumberofGate
        _Caculation_Parameters['_Tr4_ChannelWidth']     = _Sampler_Tr4_ChannelWidth
        _Caculation_Parameters['_Tr4_ChannelLength']    = _Sampler_Tr4_ChannelLength
        _Caculation_Parameters['_Tr4_XVT']              = _Sampler_Tr4_XVT

        _Caculation_Parameters['_Tr5_NumberofGate']     = _Sampler_Tr5_NumberofGate
        _Caculation_Parameters['_Tr5_ChannelWidth']     = _Sampler_Tr5_ChannelWidth
        _Caculation_Parameters['_Tr5_ChannelLength']    = _Sampler_Tr5_ChannelLength
        _Caculation_Parameters['_Tr5_XVT']              = _Sampler_Tr5_XVT

        _Caculation_Parameters['_Tr7_NumberofGate']     = _Sampler_Tr7_NumberofGate
        _Caculation_Parameters['_Tr7_ChannelWidth']     = _Sampler_Tr7_ChannelWidth
        _Caculation_Parameters['_Tr7_ChannelLength']    = _Sampler_Tr7_ChannelLength
        _Caculation_Parameters['_Tr7_XVT']              = _Sampler_Tr7_XVT

        _Caculation_Parameters['_Tr9_NumberofGate']     = _Sampler_Tr9_NumberofGate
        _Caculation_Parameters['_Tr9_ChannelWidth']     = _Sampler_Tr9_ChannelWidth
        _Caculation_Parameters['_Tr9_ChannelLength']    = _Sampler_Tr9_ChannelLength
        _Caculation_Parameters['_Tr9_XVT']              = _Sampler_Tr9_XVT

        _Caculation_Parameters['_Tr8_NumberofGate']     = _Sampler_Tr8_NumberofGate
        _Caculation_Parameters['_Tr8_ChannelWidth']     = _Sampler_Tr8_ChannelWidth
        _Caculation_Parameters['_Tr8_ChannelLength']    = _Sampler_Tr8_ChannelLength
        _Caculation_Parameters['_Tr8_XVT']              = _Sampler_Tr8_XVT

        _Caculation_Parameters['_Tr6_NumberofGate']     = _Sampler_Tr6_NumberofGate
        _Caculation_Parameters['_Tr6_ChannelWidth']     = _Sampler_Tr6_ChannelWidth
        _Caculation_Parameters['_Tr6_ChannelLength']    = _Sampler_Tr6_ChannelLength
        _Caculation_Parameters['_Tr6_XVT']              = _Sampler_Tr6_XVT

        _Caculation_Parameters['_Tr11_NumberofGate']     = _Sampler_Tr11_NumberofGate
        _Caculation_Parameters['_Tr11_ChannelWidth']     = _Sampler_Tr11_ChannelWidth
        _Caculation_Parameters['_Tr11_ChannelLength']    = _Sampler_Tr11_ChannelLength
        _Caculation_Parameters['_Tr11_XVT']              = _Sampler_Tr11_XVT

        _Caculation_Parameters['_Tie4N_NumberofGate']     = _Sampler_Tie4N_NumberofGate
        _Caculation_Parameters['_Tie4N_ChannelWidth']     = _Sampler_Tie4N_ChannelWidth
        _Caculation_Parameters['_Tie4N_ChannelLength']    = _Sampler_Tie4N_ChannelLength
        _Caculation_Parameters['_Tie4N_XVT']              = _Sampler_Tie4N_XVT

        _Caculation_Parameters['_Tie4P_NumberofGate']     = _Sampler_Tie4P_NumberofGate
        _Caculation_Parameters['_Tie4P_ChannelWidth']     = _Sampler_Tie4P_ChannelWidth
        _Caculation_Parameters['_Tie4P_ChannelLength']    = _Sampler_Tie4P_ChannelLength
        _Caculation_Parameters['_Tie4P_XVT']              = _Sampler_Tie4P_XVT

        _Caculation_Parameters['_Tie8N_NumberofGate']     = _Sampler_Tie8N_NumberofGate
        _Caculation_Parameters['_Tie8N_ChannelWidth']     = _Sampler_Tie8N_ChannelWidth
        _Caculation_Parameters['_Tie8N_ChannelLength']    = _Sampler_Tie8N_ChannelLength
        _Caculation_Parameters['_Tie8N_XVT']              = _Sampler_Tie8N_XVT

        _Caculation_Parameters['_Tie8P_NumberofGate']     = _Sampler_Tie8P_NumberofGate
        _Caculation_Parameters['_Tie8P_ChannelWidth']     = _Sampler_Tie8P_ChannelWidth
        _Caculation_Parameters['_Tie8P_ChannelLength']    = _Sampler_Tie8P_ChannelLength
        _Caculation_Parameters['_Tie8P_XVT']              = _Sampler_Tie8P_XVT

        _Caculation_Parameters['_Tr12_NumberofGate']     = _Sampler_Tr12_NumberofGate
        _Caculation_Parameters['_Tr12_ChannelWidth']     = _Sampler_Tr12_ChannelWidth
        _Caculation_Parameters['_Tr12_ChannelLength']    = _Sampler_Tr12_ChannelLength
        _Caculation_Parameters['_Tr12_XVT']              = _Sampler_Tr12_XVT

        _Caculation_Parameters['_Tr3_NumberofGate']     = _Sampler_Tr3_NumberofGate
        _Caculation_Parameters['_Tr3_ChannelWidth']     = _Sampler_Tr3_ChannelWidth
        _Caculation_Parameters['_Tr3_ChannelLength']    = _Sampler_Tr3_ChannelLength
        _Caculation_Parameters['_Tr3_XVT']              = _Sampler_Tr3_XVT

        _Caculation_Parameters['_Tr10_NumberofGate']     = _Sampler_Tr10_NumberofGate
        _Caculation_Parameters['_Tr10_ChannelWidth']     = _Sampler_Tr10_ChannelWidth
        _Caculation_Parameters['_Tr10_ChannelLength']    = _Sampler_Tr10_ChannelLength
        _Caculation_Parameters['_Tr10_XVT']              = _Sampler_Tr10_XVT

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_C13_00'] = self._SrefElementDeclaration(_DesignObj=C13_00_C07C11C12TieCellsRouted_YJ_v01_00_random._C07C11C12TieCellsRouted(_DesignParameter=None, _Name='{}:SRF_C13_00'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_C13_00']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C13_00']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C13_00']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C13_00']['_XYCoordinates'] = [[0, 0]]


        ## HDVNCAP Array SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C01_04_Guardring_random._Guardring._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length']           = _Sampler_HDVNCAP_Length
        _Caculation_Parameters['_LayoutOption']     = _Sampler_HDVNCAP_LayoutOption
        _Caculation_Parameters['_NumFigPair']       = _Sampler_HDVNCAP_NumFigPair
        _Caculation_Parameters['_Array']            = _Sampler_HDVNCAP_Array
        _Caculation_Parameters['_Cbot_Ctop_metalwidth'] = _Sampler_HDVNCAP_Cbot_Ctop_metalwidth

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_HDVNCAP'] = self._SrefElementDeclaration(_DesignObj=C01_04_Guardring_random._Guardring(_DesignParameter=None, _Name='{}:SRF_HDVNCAP'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_HDVNCAP']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_HDVNCAP']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_HDVNCAP']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_HDVNCAP']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_C13_00', 'SRF_C12','SRF_C00_03_Guardring','SRF_Pbodyring2', 'SRF_PbodyBottom', 'SRF_PbodyContactPhyLen','BND_PPLayer')
        target_coordy = tmp1[0][0][0][0][0][0][0][0]['_XY_down'][1]
        tmp1_1 = self.get_outter_KJH4('SRF_C13_00', 'SRF_Tie8')
        tmp1_2 = self.get_outter_KJH4('SRF_C13_00', 'SRF_Tie4')

        target_coordx = round(0.5*(tmp1_1['_Mostright']['coord'][0] + tmp1_2['_Mostleft']['coord'][0]))
        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_HDVNCAP','SRF_Pbodyring', 'SRF_PbodyTop', 'SRF_PbodyContactPhyLen','BND_PPLayer')
        approaching_coord = tmp2[0][0][0][0][0][0]['_XY_up']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_HDVNCAP')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        C01C13_00Space = 2000
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[1] = New_Scoord[1] - C01C13_00Space
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['SRF_HDVNCAP']['_XYCoordinates'] = tmpXY



        ## CTop Vtc Metal (M4)
        ## Class_HEADER: Pre Defined Parameter Before Calculation
        CTop_Hrz_M5_PathWidth = 1000
        Ctop_Vtc_M4_PathWidth = 1000

        # Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Ctop_Vtc_M5'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL5'][0],
        _Datatype=DesignParameters._LayerMapping['METAL5'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        # tmp0 = self.get_param_KJH4('SRF_C13_00', 'SRF_C11', 'SRF_Tr11', 'SRF_Nbodyring', 'SRF_NbodyBottom', 'SRF_NbodyContactPhyLen','BND_Nwell')
        # tmp1 = tmp0[0][0][0][0][0][0][0][0]['_XY_down'][1]
        tmp0 = self.get_param_KJH4('SRF_C13_00', 'SRF_C12', 'SRF_C02_04_Guardring', 'SRF_Nbodyring', 'SRF_NbodyTop','SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        tmp1 = tmp0[0][0][0][0][0][0][0][0]['_XY_up'][1]
        tmp2 = self.get_outter_KJH4('SRF_C13_00', 'SRF_C12', 'SRF_C00_03_Guardring')
        self._DesignParameter['BND_Ctop_Vtc_M5']['_YWidth'] = int(abs(tmp1 - tmp2['_Mostdown']['coord'][0]) + (C01C13_00Space + CTop_Hrz_M5_PathWidth)/2)

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Ctop_Vtc_M5']['_XWidth'] = Ctop_Vtc_M4_PathWidth

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Ctop_Vtc_M5']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1_1 = self.get_param_KJH4('SRF_C13_00', 'SRF_Tie8', 'SRF_PMOS_Body_Contact','SRF_NbodyContactPhyLen','BND_Nwell')
        tmp1_2 = tmp1
        target_coord = [tmp1_1[0][0][0][0][0][0]['_XY_right'][0], tmp1_2]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Ctop_Vtc_M5')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Ctop_Vtc_M5')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Ctop_Vtc_M5']['_XYCoordinates'] = tmpXY



        # Ctop <-> C12(Tr5Tr7Tr9) Guardring Routing (M4 layer Hrz Boundary)
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CtopC12Nbodyring_Hrz_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        CtopC12Nbodyring_Hrz_M4_PathWidth = 400
        self._DesignParameter['BND_CtopC12Nbodyring_Hrz_M4']['_YWidth'] = CtopC12Nbodyring_Hrz_M4_PathWidth

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('BND_Ctop_Vtc_M5')
        tmp2 = self.get_param_KJH4('SRF_C13_00', 'SRF_C12', 'SRF_C02_04_Guardring', 'SRF_Tr5Tr7Tr9', 'SRF_Tr9', 'BND_Gate_Hrz_poly')
        tmp2_1 = tmp2[0][0][0][0][0][0][0]['_XY_left'][0]
        self._DesignParameter['BND_CtopC12Nbodyring_Hrz_M4']['_XWidth'] = abs(tmp1[0][0]['_XY_right'][0] - tmp2_1)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_CtopC12Nbodyring_Hrz_M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp3 = self.get_param_KJH4('SRF_C13_00', 'SRF_C12', 'SRF_C02_04_Guardring', 'SRF_Nbodyring', 'SRF_NbodyTop', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        target_coord = [tmp2_1, tmp3[0][0][0][0][0][0][0][0]['_XY_cent'][1]]
        ## Approaching_coord: _XY_type2
        tmp4 = self.get_param_KJH4('BND_CtopC12Nbodyring_Hrz_M4')
        approaching_coord = tmp4[0][0]['_XY_left']
        ## Sref coord
        tmp5 = self.get_param_KJH4('BND_CtopC12Nbodyring_Hrz_M4')
        Scoord = tmp5[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CtopC12Nbodyring_Hrz_M4']['_XYCoordinates'] = tmpXY




###########
        # Viastack (BND_CtopC12Nbodyring_Hrz_M4 <-> BND_Ctop_Vtc_M5)
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 4
        _Caculation_Parameters['_Layer2'] = 5
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CtopNode_ViaM4M5'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,_Name='{}:SRF_Ctop_ViaM4M5'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CtopNode_ViaM4M5']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CtopNode_ViaM4M5']['_Angle'] = 0

        ## Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH4('BND_CtopC12Nbodyring_Hrz_M4')
        tmp2 = self.get_param_KJH4('BND_Ctop_Vtc_M5')
        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

        ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

        ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CtopNode_ViaM4M5']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CtopNode_ViaM4M5']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        target_coord = Ovlpcoord[0]['_XY_cent']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CtopNode_ViaM4M5', 'SRF_ViaM4M5', 'BND_Met5Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CtopNode_ViaM4M5')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CtopNode_ViaM4M5']['_XYCoordinates'] = tmpXY



        # Viastack (BND_CtopC12Nbodyring_Hrz_M4 <-> C02 Pbodyring(bottom) BND_Met1Layer) generation
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CtopC02Guardring_ViaM1M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,_Name='{}:SRF_CtopC02Guardring_ViaM1M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CtopC02Guardring_ViaM1M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CtopC02Guardring_ViaM1M4']['_Angle'] = 0

        ## Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH4('BND_CtopC12Nbodyring_Hrz_M4')
        tmp2 = self.get_param_KJH4('SRF_C13_00', 'SRF_C12', 'SRF_C02_04_Guardring', 'SRF_Nbodyring', 'SRF_NbodyTop', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0][0][0][0][0][0][0])

        ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

        ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CtopC02Guardring_ViaM1M4']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CtopC02Guardring_ViaM1M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_CtopC12Nbodyring_Hrz_M4')
        target_coord = tmp1[0][0]['_XY_left']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CtopC02Guardring_ViaM1M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CtopC02Guardring_ViaM1M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CtopC02Guardring_ViaM1M4']['_XYCoordinates'] = tmpXY




        ## Ctop M5 Hrz Route Boundary (HDVNCap 상단) Generetion
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CtopNode_Hrz_M5'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5'][0],
            _Datatype=DesignParameters._LayerMapping['METAL5'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        CtopNode_Hrz_M5_PathWidth = 1000
        self._DesignParameter['BND_CtopNode_Hrz_M5']['_YWidth'] = CtopNode_Hrz_M5_PathWidth

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('BND_Ctop_Vtc_M5')
        tmp2 = self.get_param_KJH4('SRF_HDVNCAP', 'SRF_Array', 'BND_CTop_METAL{}'.format(_Sampler_HDVNCAP_LayoutOption[-1]))
        tmp3_1 = abs(tmp1[0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0])
        tmp3_2 = abs(tmp2[0][0][-1][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0])
        self._DesignParameter['BND_CtopNode_Hrz_M5']['_XWidth'] = max(tmp3_1, tmp3_2)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_CtopNode_Hrz_M5']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = [tmp2[0][0][0][0]['_XY_left'][0], tmp1[0][0]['_XY_down'][1]]
        ## Approaching_coord: _XY_type2
        tmp5 = self.get_param_KJH4('BND_CtopNode_Hrz_M5')
        approaching_coord = tmp5[0][0]['_XY_down_left']
        ## Sref coord
        Scoord = tmp5[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CtopNode_Hrz_M5']['_XYCoordinates'] = tmpXY




        # HDVNCap <-> BND_CtopNode_Hrz_M5 routing
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CtopHDVNCap_Vtc_M7'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL7'][0],
            _Datatype=DesignParameters._LayerMapping['METAL7'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1_1 = self.get_param_KJH4('SRF_HDVNCAP', 'SRF_Array', 'BND_CTop_METAL{}'.format(_Sampler_HDVNCAP_LayoutOption[-1]))
        tmp1_2 = self.get_param_KJH4('BND_CtopNode_Hrz_M5')
        self._DesignParameter['BND_CtopHDVNCap_Vtc_M7']['_YWidth'] = abs(tmp1_2[0][0]['_XY_up'][1] - tmp1_1[0][0][0][0]['_XY_down'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CtopHDVNCap_Vtc_M7']['_XWidth'] = _Sampler_HDVNCAP_Cbot_Ctop_metalwidth

        ## initialized Sref coordinate
        self._DesignParameter['BND_CtopHDVNCap_Vtc_M7']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        for i in range(int((_Sampler_HDVNCAP_Array + 1) / 2)):
            ## Target_coord: _XY_type1
            tmp2_1 = tmp1_1[0][0][i][0]['_XY_left'][0]
            tmp2_2 = tmp1_2[0][0]['_XY_up'][1]
            target_coord = [tmp2_1, tmp2_2]
            ## Approaching_coord: _XY_type2
            tmp3 = self.get_param_KJH4('BND_CtopHDVNCap_Vtc_M7')
            approaching_coord = tmp3[0][0]['_XY_up_left']
            ## Sref coord
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        ## Define coordinates
        self._DesignParameter['BND_CtopHDVNCap_Vtc_M7']['_XYCoordinates'] = tmpXY




        ################################################################################################################
        ## CBot Vtc Metal (M4)
        # Boundary_element Generation
        self._DesignParameter['BND_Cbot_Vtc_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        # tmp0 = self.get_param_KJH4('SRF_C13_00', 'SRF_C11', 'SRF_Tr11', 'SRF_Nbodyring', 'SRF_NbodyBottom', 'SRF_NbodyContactPhyLen','BND_Nwell')
        # tmp0 = self.get_param_KJH4('SRF_C13_00', 'SRF_C07', 'SRF_Pbodyring', 'SRF_PbodyTop','SRF_PbodyContactPhyLen', 'BND_PPLayer')
        tmp0 = self.get_param_KJH4('SRF_C13_00', 'SRF_C11', 'SRF_Tr6', 'SRF_Pbodyring', 'SRF_PbodyBottom', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        tmp1 = tmp0[0][0][0][0][0][0][0][0]['_XY_down'][1]
        # tmp1 = tmp0[0][0][0][0][0][0][0]['_XY_up'][1]
        tmp2 = self.get_outter_KJH4('SRF_C13_00', 'SRF_C12', 'SRF_C00_03_Guardring')
        self._DesignParameter['BND_Cbot_Vtc_M4']['_YWidth'] = abs(tmp1 - tmp2['_Mostdown']['coord'][0])

        ## Define Boundary_element _XWidth
        CBot_Vtc_M4_PathWidth = 1000
        self._DesignParameter['BND_Cbot_Vtc_M4']['_XWidth'] = CBot_Vtc_M4_PathWidth

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Cbot_Vtc_M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1_1 = self.get_param_KJH4('SRF_C13_00', 'SRF_Tie4', 'SRF_PMOS_Body_Contact', 'SRF_NbodyContactPhyLen','BND_Nwell')[0][0][0][0][0][0]['_XY_left'][0]
        tmp1_2 = tmp1
        target_coord = [tmp1_1, tmp1_2]
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Cbot_Vtc_M4')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Cbot_Vtc_M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Cbot_Vtc_M4']['_XYCoordinates'] = tmpXY




        # Cbot <-> C11(Tr6Tr11) Guardring Routing (M4 layer Hrz Boundary)
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CbotTr6Pbodyring_Hrz_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        CbotTr6Pbodyring_Hrz_M4_PathWidth = 400
        self._DesignParameter['BND_CbotTr6Pbodyring_Hrz_M4']['_YWidth'] = CbotTr6Pbodyring_Hrz_M4_PathWidth

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('BND_Cbot_Vtc_M4')
        tmp2 = self.get_param_KJH4('SRF_C13_00', 'SRF_C11', 'SRF_Tr6', 'SRF_Pbodyring', 'SRF_PbodyBottom', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        tmp3 = tmp2[0][0][0][0][0][0][0][0]['_XY_up_right'][0]
        self._DesignParameter['BND_CbotTr6Pbodyring_Hrz_M4']['_XWidth'] = abs(tmp3 - tmp1[0][0]['_XY_left'][0])

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_CbotTr6Pbodyring_Hrz_M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        # Cbot을 C11의 Tr6 가드링 밑 쪽 메탈 가운데 위와 라우팅
        target_coord = tmp2[0][0][0][0][0][0][0][0]['_XY_up_right']
        ## Approaching_coord: _XY_type2
        tmp4 = self.get_param_KJH4('BND_CbotTr6Pbodyring_Hrz_M4')
        approaching_coord = tmp4[0][0]['_XY_up_right']
        ## Sref coord
        tmp5 = self.get_param_KJH4('BND_CbotTr6Pbodyring_Hrz_M4')
        Scoord = tmp5[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CbotTr6Pbodyring_Hrz_M4']['_XYCoordinates'] = tmpXY




        # Viastack (BND_CbotTr6Pbodyring_Hrz_M4 <-> Tr6 Pbodyring(bottom) BND M1 layer) generation
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CbotTr6Pbodyring_ViaM1M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(
            _DesignParameter=None,
            _Name='{}:SRF_CbotTr6Pbodyring_ViaM1M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CbotTr6Pbodyring_ViaM1M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CbotTr6Pbodyring_ViaM1M4']['_Angle'] = 0

        ## Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH4('BND_CbotTr6Pbodyring_Hrz_M4')
        tmp2 = self.get_param_KJH4('SRF_C13_00', 'SRF_C11', 'SRF_Tr6', 'SRF_Pbodyring', 'SRF_PbodyBottom', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0][0][0][0][0][0][0])

        ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

        ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CbotTr6Pbodyring_ViaM1M4']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CbotTr6Pbodyring_ViaM1M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        # tmp1 = self.get_param_KJH4('BND_CbotTr6Pbodyring_Hrz_M4')
        # target_coord = tmp1[0][0]['_XY_up_right']
        target_coord = Ovlpcoord[0]['_XY_cent']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CbotTr6Pbodyring_ViaM1M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CbotTr6Pbodyring_ViaM1M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CbotTr6Pbodyring_ViaM1M4']['_XYCoordinates'] = tmpXY




        # BND_Cbot_Vtc_M4 <-> Tr12 Source Guardring Routing (M2 layer Hrz Boundary)
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CbotTr12Source_Hrz_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        CbotTr12Source_Hrz_M2_PathWidth = 300
        self._DesignParameter['BND_CbotTr12Source_Hrz_M2']['_YWidth'] = CbotTr12Source_Hrz_M2_PathWidth

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('BND_Cbot_Vtc_M4')
        tmp2 = self.get_param_KJH4('SRF_C13_00', 'SRF_C07', 'SRF_Tr12Tr3Tr10', 'SRF_Tr12', 'BND_Source_Hrz_M2')
        self._DesignParameter['BND_CbotTr12Source_Hrz_M2']['_XWidth'] = abs(tmp2[0][0][0][0][0][0]['_XY_right'][0] - tmp1[0][0]['_XY_left'][0])

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_CbotTr12Source_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp2[0][0][0][0][0][0]['_XY_up_right']
        ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_CbotTr12Source_Hrz_M2')
        approaching_coord = tmp3[0][0]['_XY_up_right']
        ## Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CbotTr12Source_Hrz_M2']['_XYCoordinates'] = tmpXY




        # Viastack (BND_Cbot_Vtc_M4 <-> BND_CbotTr12Source_Hrz_M2) generation
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CbotTr12Source_ViaM2M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(
            _DesignParameter=None,
            _Name='{}:SRF_CbotTr12Source_ViaM2M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CbotTr12Source_ViaM2M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CbotTr12Source_ViaM2M4']['_Angle'] = 0

        ## Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH4('BND_Cbot_Vtc_M4')
        tmp2 = self.get_param_KJH4('BND_CbotTr12Source_Hrz_M2')
        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

        ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

        ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CbotTr12Source_ViaM2M4']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CbotTr12Source_ViaM2M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        target_coord = Ovlpcoord[0]['_XY_cent']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CbotTr12Source_ViaM2M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CbotTr12Source_ViaM2M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CbotTr12Source_ViaM2M4']['_XYCoordinates'] = tmpXY




        #####
        # Cbot <-> C00(Tr1Tr2) PGuardring Vtc Route (Cbot_Hrz_M4에서 위 쪽으로 올라가는 M4 Boundary)
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CbotC00Pbodyring_Vtc_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1_2 = self.get_param_KJH4('BND_Cbot_Vtc_M4')
        tmp1_1 = self.get_param_KJH4('SRF_C13_00', 'SRF_C12', 'SRF_C00_03_Guardring', 'SRF_Pbodyring', 'SRF_PbodyBottom', 'SRF_PbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_CbotC00Pbodyring_Vtc_M4']['_YWidth'] = abs(tmp1_1[0][0][0][0][0][0][0][0]['_XY_up'][1] - tmp1_2[0][0]['_XY_down'][1])

        ## Define Boundary_element _XWidth
        CbotC00Pbodyring_Vtc_M4_PathWidth = 1000
        self._DesignParameter['BND_CbotC00Pbodyring_Vtc_M4']['_XWidth'] = CbotC00Pbodyring_Vtc_M4_PathWidth

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_CbotC00Pbodyring_Vtc_M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp3 = self.get_param_KJH4('SRF_C13_00', 'SRF_C12', 'SRF_C00_03_Guardring', 'SRF_Tr1Tr2', 'SRF_Tr2', 'BND_Gate_Hrz_M0')  #############
        target_coord = [tmp3[0][0][0][0][0][0][0]['_XY_left'][0], tmp1_1[0][0][0][0][0][0][0][0]['_XY_up'][1]]
        ## Approaching_coord: _XY_type2
        tmp5 = self.get_param_KJH4('BND_CbotC00Pbodyring_Vtc_M4')
        approaching_coord = tmp5[0][0]['_XY_up_left']
        ## Sref coord
        Scoord = tmp5[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CbotC00Pbodyring_Vtc_M4']['_XYCoordinates'] = tmpXY




        # Cbot <-> C00(Tr1Tr2) PGuardring Routing (M4 layer Hrz Boundary)
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CbotNode_Hrz_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        CbotC00Pbodyring_Hrz_M4_PathWidth = 1000
        self._DesignParameter['BND_CbotNode_Hrz_M4']['_YWidth'] = CbotC00Pbodyring_Hrz_M4_PathWidth

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('BND_Cbot_Vtc_M4')
        tmp2 = self.get_param_KJH4('SRF_HDVNCAP', 'SRF_Array', 'BND_CBot_METAL{}'.format(_Sampler_HDVNCAP_LayoutOption[-1]))
        tmp3 = self.get_param_KJH4('BND_CbotC00Pbodyring_Vtc_M4')
        tmpRight = max(tmp2[0][0][-1][0]['_XY_right'][0], tmp3[0][0]['_XY_right'][0])
        tmpLeft = min(tmp2[0][0][0][0]['_XY_left'][0], tmp1[0][0]['_XY_left'][0])
        self._DesignParameter['BND_CbotNode_Hrz_M4']['_XWidth'] = abs(tmpRight - tmpLeft)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_CbotNode_Hrz_M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = [tmpLeft, tmp1[0][0]['_XY_down_left'][1]]
        ## Approaching_coord: _XY_type2
        tmp5 = self.get_param_KJH4('BND_CbotNode_Hrz_M4')
        approaching_coord = tmp5[0][0]['_XY_down_left']
        ## Sref coord
        tmp6 = self.get_param_KJH4('BND_CbotNode_Hrz_M4')
        Scoord = tmp6[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CbotNode_Hrz_M4']['_XYCoordinates'] = tmpXY




        # Viastack (BND_CbotC00Pbodyring_Vtc_M4 <-> C00Pbodyring M1 Layer) generation
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CbotC00Pbodyring_ViaM1M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(
            _DesignParameter=None,
            _Name='{}:SRF_CbotC00Pbodyring_ViaM1M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CbotC00Pbodyring_ViaM1M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CbotC00Pbodyring_ViaM1M4']['_Angle'] = 0

        ## Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH4('SRF_C13_00', 'SRF_C12', 'SRF_C00_03_Guardring', 'SRF_Pbodyring', 'SRF_PbodyBottom', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        tmp2 = self.get_param_KJH4('BND_CbotC00Pbodyring_Vtc_M4')
        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0][0][0][0][0][0][0], tmp2[0][0])

        ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

        ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CbotC00Pbodyring_ViaM1M4']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CbotC00Pbodyring_ViaM1M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        # tmp1_2 = self.get_param_KJH4('SRF_C13_00', 'SRF_C12', 'SRF_C00_03_Guardring', 'SRF_Pbodyring', 'SRF_PbodyBottom', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        # target_coord = [tmp2[0][0]['_XY_cent'][0], tmp1_2[0][0][0][0][0][0][0][0]['_XY_cent'][1]]
        target_coord =Ovlpcoord[0]['_XY_cent']
        ## Approaching_coord
        tmp3 = self.get_param_KJH4('SRF_CbotC00Pbodyring_ViaM1M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        approaching_coord = tmp3[0][0][0][0]['_XY_cent']
        ## Sref coord
        tmp4 = self.get_param_KJH4('SRF_CbotC00Pbodyring_ViaM1M4')
        Scoord = tmp4[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CbotC00Pbodyring_ViaM1M4']['_XYCoordinates'] = tmpXY




        # HDVNCap <-> BND_CbotNode_Hrz_M4 routing
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CbotHDVNCap_Vtc_M7'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL7'][0],
            _Datatype=DesignParameters._LayerMapping['METAL7'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1_1 = self.get_param_KJH4('SRF_HDVNCAP', 'SRF_Array', 'BND_CBot_METAL{}'.format(_Sampler_HDVNCAP_LayoutOption[-1]))
        tmp1_2 = self.get_param_KJH4('BND_CbotNode_Hrz_M4')
        self._DesignParameter['BND_CbotHDVNCap_Vtc_M7']['_YWidth'] = abs(tmp1_2[0][0]['_XY_up'][1] - tmp1_1[0][0][0][0]['_XY_down'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CbotHDVNCap_Vtc_M7']['_XWidth'] = _Sampler_HDVNCAP_Cbot_Ctop_metalwidth

        ## initialized Sref coordinate
        self._DesignParameter['BND_CbotHDVNCap_Vtc_M7']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        for i in range(math.ceil((_Sampler_HDVNCAP_Array + 1) / 2)):
            ## Target_coord: _XY_type1
            tmp2_1 = tmp1_1[0][0][i][0]['_XY_right'][0]
            tmp2_2 = tmp1_2[0][0]['_XY_up'][1]
            target_coord = [tmp2_1, tmp2_2]
            ## Approaching_coord: _XY_type2
            tmp3 = self.get_param_KJH4('BND_CbotHDVNCap_Vtc_M7')
            approaching_coord = tmp3[0][0]['_XY_up_right']
            ## Sref coord
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        ## Define coordinates
        self._DesignParameter['BND_CbotHDVNCap_Vtc_M7']['_XYCoordinates'] = tmpXY




        ## BND_CbotHDVNCap_vtc_M7 <-> HDVNCAP Via SREF generation
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 4
        _Caculation_Parameters['_Layer2'] = 7
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        ## Sref ViaX declaration
        self._DesignParameter['SRF_HDVNCapCbotHrzPath_ViaM4M7'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(
            _DesignParameter=None,
            _Name='{}:SRF_HDVNCapCbotHrzPath_ViaM4M7'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_HDVNCapCbotHrzPath_ViaM4M7']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_HDVNCapCbotHrzPath_ViaM4M7']['_Angle'] = 0

        ## initialized Sref coordinate
        self._DesignParameter['SRF_HDVNCapCbotHrzPath_ViaM4M7']['_XYCoordinates'] = [[0, 0]]

        tmp1 = self.get_param_KJH4('BND_CbotNode_Hrz_M4')
        tmp2 = self.get_param_KJH4('BND_CbotHDVNCap_Vtc_M7')

        ## Calculate Sref XYcoord
        tmpXY = []
        for i in range(math.ceil((_Sampler_HDVNCAP_Array + 1) / 2)):
            ## Calcuate Overlapped XYcoord
            Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[i][0])

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
            _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

            ## Define _COX and _COY
            _Caculation_Parameters['_COX'] = _COX
            _Caculation_Parameters['_COY'] = _COY

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
            self._DesignParameter['SRF_HDVNCapCbotHrzPath_ViaM4M7']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate
            ## Target_coord
            target_coord = [tmp2[i][0]['_XY_cent'][0], tmp1[0][0]['_XY_cent'][1]]
            ## Approaching_coord
            tmp3 = self.get_param_KJH4('SRF_HDVNCapCbotHrzPath_ViaM4M7', 'SRF_ViaM6M7', 'BND_Met7Layer')
            approaching_coord = tmp3[0][0][0][0]['_XY_cent']
            ## Sref coord
            tmp4 = self.get_param_KJH4('SRF_HDVNCapCbotHrzPath_ViaM4M7')
            Scoord = tmp4[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_HDVNCapCbotHrzPath_ViaM4M7']['_XYCoordinates'] = tmpXY




        # HDVNCap M6 <-> CBot Node M7 Vtc line Via
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 6
        _Caculation_Parameters['_Layer2'] = 7
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        ## Sref ViaX declaration
        self._DesignParameter['SRF_HDVNCapCbotHrzPath_ViaM6M7'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(
            _DesignParameter=None,
            _Name='{}:SRF_HDVNCapCbotHrzPath_ViaM6M7'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_HDVNCapCbotHrzPath_ViaM6M7']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_HDVNCapCbotHrzPath_ViaM6M7']['_Angle'] = 0

        ## initialized Sref coordinate
        self._DesignParameter['SRF_HDVNCapCbotHrzPath_ViaM6M7']['_XYCoordinates'] = [[0, 0]]

        tmp1 = self.get_param_KJH4('SRF_HDVNCAP', 'SRF_Array', 'BND_CBot_METAL{}'.format(_Sampler_HDVNCAP_LayoutOption[-1]))
        tmp2 = self.get_param_KJH4('BND_CbotHDVNCap_Vtc_M7')

        ## Calculate Sref XYcoord
        tmpXY = []
        for i in range(int((_Sampler_HDVNCAP_Array + 1) / 2)):
            ## Calcuate Overlapped XYcoord
            Ovlpcoord = self.get_ovlp_KJH2(tmp2[i][0], tmp1[0][0][i][0])

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
            _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'],'MinEnclosureY')

            ## Define _COX and _COY
            _Caculation_Parameters['_COX'] = _COX
            _Caculation_Parameters['_COY'] = _COY

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
            self._DesignParameter['SRF_HDVNCapCbotHrzPath_ViaM6M7']['_DesignObj']._CalculateDesignParameterYmin( **_Caculation_Parameters)

            ## Calculate
            ## Target_coord
            target_coord = [tmp1[0][0][i][0]['_XY_cent'][0], tmp2[0][0]['_XY_down'][1]]
            ## Approaching_coord
            tmp3 = self.get_param_KJH4('SRF_HDVNCapCbotHrzPath_ViaM6M7', 'SRF_ViaM6M7', 'BND_Met7Layer')
            approaching_coord = tmp3[0][0][0][0]['_XY_down']
            ## Sref coord
            tmp4 = self.get_param_KJH4('SRF_HDVNCapCbotHrzPath_ViaM6M7')
            Scoord = tmp4[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        ## Define
        self._DesignParameter['SRF_HDVNCapCbotHrzPath_ViaM6M7']['_XYCoordinates'] = tmpXY





        ####################################
        ## BND_CtopHDVNCap_Vtc_M7 <-> HDVNCAP Via SREF generation
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 4
        _Caculation_Parameters['_Layer2'] = 7
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        ## Sref ViaX declaration
        self._DesignParameter['SRF_HDVNCapCtopHrzPath_ViaM4M7'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(
            _DesignParameter=None,
            _Name='{}:SRF_HDVNCapCtopHrzPath_ViaM4M7'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_HDVNCapCtopHrzPath_ViaM4M7']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_HDVNCapCtopHrzPath_ViaM4M7']['_Angle'] = 0

        ## initialized Sref coordinate
        self._DesignParameter['SRF_HDVNCapCtopHrzPath_ViaM4M7']['_XYCoordinates'] = [[0, 0]]

        tmp1 = self.get_param_KJH4('BND_CtopNode_Hrz_M5')
        tmp2 = self.get_param_KJH4('BND_CtopHDVNCap_Vtc_M7')

        ## Calculate Sref XYcoord
        tmpXY = []
        for i in range(int((_Sampler_HDVNCAP_Array + 1) / 2)):
            ## Calcuate Overlapped XYcoord
            Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[i][0])

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
            _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'],'MinEnclosureY')

            ## Define _COX and _COY
            _Caculation_Parameters['_COX'] = _COX
            _Caculation_Parameters['_COY'] = _COY

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
            self._DesignParameter['SRF_HDVNCapCtopHrzPath_ViaM4M7']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate
            ## Target_coord
            target_coord = [tmp2[i][0]['_XY_cent'][0], tmp1[0][0]['_XY_cent'][1]]
            ## Approaching_coord
            tmp3 = self.get_param_KJH4('SRF_HDVNCapCtopHrzPath_ViaM4M7', 'SRF_ViaM6M7', 'BND_Met7Layer')
            approaching_coord = tmp3[0][0][0][0]['_XY_cent']
            ## Sref coord
            tmp4 = self.get_param_KJH4('SRF_HDVNCapCtopHrzPath_ViaM4M7')
            Scoord = tmp4[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_HDVNCapCtopHrzPath_ViaM4M7']['_XYCoordinates'] = tmpXY




        # HDVNCap M6 <-> CTop Node M7 Vtc line Via
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 6
        _Caculation_Parameters['_Layer2'] = 7
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        ## Sref ViaX declaration
        self._DesignParameter['SRF_HDVNCapCtopHrzPath_ViaM6M7'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(
            _DesignParameter=None,
            _Name='{}:SRF_HDVNCapCtopHrzPath_ViaM6M7'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_HDVNCapCtopHrzPath_ViaM6M7']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_HDVNCapCtopHrzPath_ViaM6M7']['_Angle'] = 0

        ## initialized Sref coordinate
        self._DesignParameter['SRF_HDVNCapCtopHrzPath_ViaM6M7']['_XYCoordinates'] = [[0, 0]]

        tmp1 = self.get_param_KJH4('SRF_HDVNCAP', 'SRF_Array', 'BND_CTop_METAL{}'.format(_Sampler_HDVNCAP_LayoutOption[-1]))
        tmp2 = self.get_param_KJH4('BND_CtopHDVNCap_Vtc_M7')

        ## Calculate Sref XYcoord
        tmpXY = []
        for i in range(int((_Sampler_HDVNCAP_Array + 1) / 2)):
            ## Calcuate Overlapped XYcoord
            Ovlpcoord = self.get_ovlp_KJH2(tmp2[i][0], tmp1[0][0][i][0])

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
            _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'],'MinEnclosureY')

            ## Define _COX and _COY
            _Caculation_Parameters['_COX'] = _COX
            _Caculation_Parameters['_COY'] = _COY

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
            self._DesignParameter['SRF_HDVNCapCtopHrzPath_ViaM6M7']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate
            ## Target_coord
            target_coord = [tmp1[0][0][i][0]['_XY_cent'][0], tmp2[0][0]['_XY_down'][1]]
            ## Approaching_coord
            tmp3 = self.get_param_KJH4('SRF_HDVNCapCtopHrzPath_ViaM6M7', 'SRF_ViaM6M7', 'BND_Met7Layer')
            approaching_coord = tmp3[0][0][0][0]['_XY_down']
            ## Sref coord
            tmp4 = self.get_param_KJH4('SRF_HDVNCapCtopHrzPath_ViaM6M7')
            Scoord = tmp4[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        ## Define
        self._DesignParameter['SRF_HDVNCapCtopHrzPath_ViaM6M7']['_XYCoordinates'] = tmpXY






        ##############################
        ## Input Metal6 Boundary generation
        self._DesignParameter['BND_InputNode_Hrz_M6'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6'][0],
            _Datatype=DesignParameters._LayerMapping['METAL6'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1_1 = self.get_param_KJH4('SRF_C13_00', 'SRF_C12', 'SRF_C00_03_Guardring', 'SRF_Tr1Tr2', 'SRF_Tr1', 'SRF_Tr1_Source_ViaM1Mx', 'SRF_ViaM1M2', 'BND_Met1Layer')
        tmp1_2 = self.get_param_KJH4('SRF_C13_00', 'SRF_C12', 'SRF_C00_03_Guardring', 'SRF_Tr1Tr2', 'SRF_Tr2', 'SRF_Tr2_Drain_ViaM1Mx', 'SRF_ViaM1M2', 'BND_Met1Layer')
        self._DesignParameter['BND_InputNode_Hrz_M6']['_YWidth'] = max(tmp1_1[0][0][0][0][0][0][0][0][0]['_Ywidth'], tmp1_2[0][0][0][0][0][0][0][0][0]['_Ywidth'])

        ## Define Boundary_element _XWidth
        InputNodePathExtension = 8000
        self._DesignParameter['BND_InputNode_Hrz_M6']['_XWidth'] = abs(tmp1_1[0][0][0][0][0][-1][0][0][0]['_XY_right'][0] - \
                                                                       tmp1_2[0][0][0][0][0][0][0][0][0]['_XY_left'][0]) + InputNodePathExtension

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_InputNode_Hrz_M6']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1_1[0][0][0][0][0][-1][0][0][0]['_XY_up_right']
        ## Approaching_coord: _XY_type2
        tmp4 = self.get_param_KJH4('BND_InputNode_Hrz_M6')
        approaching_coord = tmp4[0][0]['_XY_up_right']
        ## Sref coord
        tmp5 = self.get_param_KJH4('BND_InputNode_Hrz_M6')
        Scoord = tmp5[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_InputNode_Hrz_M6']['_XYCoordinates'] = tmpXY

        ## Output Metal6 Boundary generation
        self._DesignParameter['BND_OutputNode_Hrz_M6'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6'][0],
            _Datatype=DesignParameters._LayerMapping['METAL6'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_C13_00', 'SRF_C12', 'SRF_C00_03_Guardring', 'SRF_Tr1Tr2', 'SRF_Tr1', 'SRF_Tr1_Drain_ViaM1Mx', 'SRF_ViaM1M2', 'BND_Met1Layer')
        tmp1_1 = self.get_param_KJH4('BND_Ctop_Vtc_M5')
        self._DesignParameter['BND_OutputNode_Hrz_M6']['_YWidth'] = tmp1[0][0][0][0][0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        OutputNodePathExtension = 0
        self._DesignParameter['BND_OutputNode_Hrz_M6']['_XWidth'] = abs(tmp1_1[0][0]['_XY_right'][0] - \
                                                                        tmp1[0][0][0][0][0][0][0][0][0]['_XY_left'][0]) + 0

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_OutputNode_Hrz_M6']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0][0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp4 = self.get_param_KJH4('BND_OutputNode_Hrz_M6')
        approaching_coord = tmp4[0][0]['_XY_up_left']
        ## Sref coord
        tmp5 = self.get_param_KJH4('BND_OutputNode_Hrz_M6')
        Scoord = tmp5[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_OutputNode_Hrz_M6']['_XYCoordinates'] = tmpXY


        ## CALCULATION END
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')
        C13_01_CtopCbotRouted_YJ_v01_00_end_time = time.time()
        self. C13_01_CtopCbotRouted_YJ_v01_00_elapsed_time =  C13_01_CtopCbotRouted_YJ_v01_00_end_time -  C13_01_CtopCbotRouted_YJ_v01_00_start_time


############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    Start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0
    import random

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    # libname = 'Proj_ZZ01_C13_01_CtopCobtRouted_Fixed'
    for _iter in range(5):

        cellname = 'C13_01_CtopCbotRouted_v{}'.format(_iter+17)
        _fileName = cellname + '.gds'

        _Tr1_Gate = random.randrange(2, 10, 1)
        _Tr2_Gate = random.randrange(2, 10, 1)
        _Tr1_Tr2_Width = random.randrange(350, 1000, 50)


        _Tr4_Gate = random.randrange(2, 10, 1)
        _Tr4_Tr5_Tr7_Tr8_Tr9_Width = random.randrange(350, 1000, 50)

        _Tr5_Gate = random.randrange(2, 10, 1)
        _Tr7_Gate = random.randrange(2, 10, 1)
        _Tr9_Gate = random.randrange(2, 10, 1)
        _Tr8_Gate = random.randrange(2, 10, 1)

        _Tr6_Gate = random.randrange(1, 5, 1)
        _Tr6_Width = random.randrange(400, 1000, 100)
        _Tr11_Gate = random.randrange(1, 5, 1)
        _Tr11_Width = random.randrange(400, 1000, 100)

        _Tie4_Tie8_Gate = random.randrange(1, 5, 1)
        _Tie4_Tie8_Width = random.randrange(400, 1000, 100)

        _Tr12_Gate = random.randrange(2, 5, 1)
        _Tr3_Gate = random.randrange(2, 5, 1)
        _Tr10_Gate = random.randrange(2, 5, 1)
        _Tr12_Tr3_Tr10_Width = random.randrange(400, 1000, 100)

        ''' Input Parameters for Layout Object '''
        InputParams = dict(
    ## Bootstrapped Switch
        # Input/Output node
            # INPUT node
            _Sampler_Inputnode_width = 500,  # number
            # OUTPUT node
            _Sampler_Outputnode_width = 500,  # number
        # TR1
            # Physical dimension
            _Sampler_Tr1_NumberofGate	            = _Tr1_Gate,       # Number
            _Sampler_Tr1_ChannelWidth	            = _Tr1_Tr2_Width,     # Number
            _Sampler_Tr1_ChannelLength	            = 30,       # Number
            _Sampler_Tr1_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
        # TR2
            # Physical dimension
            _Sampler_Tr2_NumberofGate	            = _Tr2_Gate,       # Number
            _Sampler_Tr2_ChannelWidth	            = _Tr1_Tr2_Width,     # Number
            _Sampler_Tr2_ChannelLength	            = 30,       # Number
            _Sampler_Tr2_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
        # TR4
            # Physical dimension
            _Sampler_Tr4_NumberofGate	            = _Tr4_Gate,       # Number
            _Sampler_Tr4_ChannelWidth	            = _Tr4_Tr5_Tr7_Tr8_Tr9_Width,     # Number
            _Sampler_Tr4_ChannelLength	            = 30,       # Number
            _Sampler_Tr4_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
        # TR5
            # Physical dimension
            _Sampler_Tr5_NumberofGate	            = _Tr5_Gate,       # Number
            _Sampler_Tr5_ChannelWidth	            = _Tr4_Tr5_Tr7_Tr8_Tr9_Width,     # Number
            _Sampler_Tr5_ChannelLength	            = 30,       # Number
            _Sampler_Tr5_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
        # TR7
            # Physical dimension
            _Sampler_Tr7_NumberofGate               = _Tr7_Gate,  # Number
            _Sampler_Tr7_ChannelWidth	            = _Tr4_Tr5_Tr7_Tr8_Tr9_Width,     # Number
            _Sampler_Tr7_ChannelLength	            = 30,       # Number
            _Sampler_Tr7_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
        # TR9
            # Physical dimension
            _Sampler_Tr9_NumberofGate               = _Tr9_Gate,  # Number
            _Sampler_Tr9_ChannelWidth	            = _Tr4_Tr5_Tr7_Tr8_Tr9_Width,     # Number
            _Sampler_Tr9_ChannelLength	            = 30,       # Number
            _Sampler_Tr9_XVT				        = 'LVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
        # TR8
            # Physical dimension
            _Sampler_Tr8_NumberofGate	            = _Tr8_Gate,       # Number
            _Sampler_Tr8_ChannelWidth	            = _Tr4_Tr5_Tr7_Tr8_Tr9_Width,     # Number
            _Sampler_Tr8_ChannelLength	            = 30,       # Number
            _Sampler_Tr8_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
        # TR6
            # Physical dimension
            _Sampler_Tr6_NumberofGate	            = _Tr6_Gate,       # Number
            _Sampler_Tr6_ChannelWidth	            = _Tr6_Width,     # Number
            _Sampler_Tr6_ChannelLength	            = 30,       # Number
            _Sampler_Tr6_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
        # TR11
            # Physical dimension
            _Sampler_Tr11_NumberofGate	            = _Tr11_Gate,       # Number
            _Sampler_Tr11_ChannelWidth	            = _Tr11_Width,     # Number
            _Sampler_Tr11_ChannelLength	            = 30,       # Number
            _Sampler_Tr11_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
        # Tie4N
            # Physical dimension
            _Sampler_Tie4N_NumberofGate     	    = _Tie4_Tie8_Gate,       # Number
            _Sampler_Tie4N_ChannelWidth	            = _Tie4_Tie8_Width,     # Number
            _Sampler_Tie4N_ChannelLength	        = 30,       # Number
            _Sampler_Tie4N_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
        # Tie4P
            # Physical dimension
            _Sampler_Tie4P_NumberofGate	            = _Tie4_Tie8_Gate,       # Number
            _Sampler_Tie4P_ChannelWidth	            = _Tie4_Tie8_Width,     # Number
            _Sampler_Tie4P_ChannelLength	        = 30,       # Number
            _Sampler_Tie4P_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
        # Tie8N
            # Physical dimension
            _Sampler_Tie8N_NumberofGate	            = _Tie4_Tie8_Gate,       # Number
            _Sampler_Tie8N_ChannelWidth	            = _Tie4_Tie8_Width,     # Number
            _Sampler_Tie8N_ChannelLength	        = 30,       # Number
            _Sampler_Tie8N_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
        # Tie8P
            # Physical dimension
            _Sampler_Tie8P_NumberofGate	            = _Tie4_Tie8_Gate,       # Number
            _Sampler_Tie8P_ChannelWidth	            = _Tie4_Tie8_Width,     # Number
            _Sampler_Tie8P_ChannelLength	        = 30,       # Number
            _Sampler_Tie8P_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
        # TR12
            # Physical dimension
            _Sampler_Tr12_NumberofGate	            = _Tr12_Gate,       # Number
            _Sampler_Tr12_ChannelWidth	            = _Tr12_Tr3_Tr10_Width,     # Number
            _Sampler_Tr12_ChannelLength	            = 30,       # Number
            _Sampler_Tr12_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
        # TR3
            # Physical dimension
            _Sampler_Tr3_NumberofGate	            = _Tr3_Gate,       # Number
            _Sampler_Tr3_ChannelWidth	            = _Tr12_Tr3_Tr10_Width,     # Number
            _Sampler_Tr3_ChannelLength	            = 30,       # Number
            _Sampler_Tr3_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
        # TR10
            # Physical dimension
            _Sampler_Tr10_NumberofGate	            = _Tr10_Gate,       # Number
            _Sampler_Tr10_ChannelWidth	            = _Tr12_Tr3_Tr10_Width,     # Number
            _Sampler_Tr10_ChannelLength	            = 30,       # Number
            _Sampler_Tr10_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

        # HDVNCAP
            _Sampler_HDVNCAP_Length = random.randrange(2000, 10000, 1000),
            _Sampler_HDVNCAP_LayoutOption = [3,4,5,6], # Writedown [number1, number2, number3, ...]
            _Sampler_HDVNCAP_NumFigPair = random.randrange(10, 50, 2), #number (ref:75)

            _Sampler_HDVNCAP_Array = 3, #number: 1xnumber
            _Sampler_HDVNCAP_Cbot_Ctop_metalwidth = 1000, #number
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
        LayoutObj = _CtopCbotRouted(_DesignParameter=None, _Name=cellname)
        LayoutObj._CalculateDesignParameter(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
        # testStreamFile = open('./gdsfile/{}'.format(_fileName), 'wb')
        testStreamFile = open('./{}'.format(_fileName), 'wb')
        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

    ''' Check Time'''
    elapsed_time = time.time() - Start_time
    m, s = divmod(elapsed_time, 60)
    h, m = divmod(m, 60)

    # print('###############      Sending to FTP Server...      ##################')
    # My = MyInfo.USER(DesignParameters._Technology)
    # Checker = DRCchecker_KJH0.DRCchecker_KJH0(
    #     username=My.ID,
    #     password=My.PW,
    #     WorkDir=My.Dir_Work,
    #     DRCrunDir=My.Dir_DRCrun,
    #     libname=libname,
    #     cellname=cellname,
    #     GDSDir=My.Dir_GDS
    # )
    # Checker.lib_deletion()
    # # Checker.cell_deletion()
    # Checker.Upload2FTP()
    # Checker.StreamIn(tech=DesignParameters._Technology)
    # # Checker_KJH0.DRCchecker()

    print('#############################      Finished      ################################')
    print('{} Hours   {} minutes   {} seconds'.format(h, m, s))
# end of 'main():' ---------------------------------------------------------------------------------------------

















