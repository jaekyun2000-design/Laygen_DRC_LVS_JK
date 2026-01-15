## Import Basic Modules
    ## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_ADC.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC
#from KJH91_Projects.Project_ADC.Library_and_Engine import DRCv2

    ## Library
import copy
import math
import numpy as np
import time

    ## KJH91 Basic Building Blocks
# from KJH91_Projects.Project_ADC.Layoutgen_code.C11_Tr6Tr11_YJH import C11_00_Tr6Tr11Routed_v02
# from KJH91_Projects.Project_ADC.Layoutgen_code.C12_Tr1Tr2_Tr5Tr7Tr9_Tr4_Tr8_KJH import C12_00_Tr1Tr2_Tr5Tr7Tr9_Tr4_Tr8
# from KJH91_Projects.Project_ADC.Layoutgen_code.C06_Tie4_YJH import C06_00_VddTieCell
# from KJH91_Projects.Project_ADC.Layoutgen_code.C10_Tie8_YJH import C10_00_VddTieCell
# from KJH91_Projects.Project_ADC.Layoutgen_code.C07_Tr12Tr3Tr10_KJH import C07_04_Guardring

from KJH91_Projects.Project_ADC.Layoutgen_code.C11_Tr6Tr11_Fixed import C11_00_Tr6Tr11Routed_v02
from KJH91_Projects.Project_ADC.Layoutgen_code.C12_Tr1Tr2_Tr5Tr7Tr9_Tr4_Tr8_Fixed import C12_00_Tr1Tr2_Tr5Tr7Tr9_Tr4_Tr8
from KJH91_Projects.Project_ADC.Layoutgen_code.C06_Tie4_Fixed import C06_00_VddTieCell
from KJH91_Projects.Project_ADC.Layoutgen_code.C10_Tie8_Fixed import C10_00_VddTieCell
from KJH91_Projects.Project_ADC.Layoutgen_code.C07_Tr12Tr3Tr10_Fixed import C07_04_Guardring

## Define Class
class _C07C11C12TieCellsRouted(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
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
    _Tr8_NumberofGate	            = 4,       # Number
    _Tr8_ChannelWidth	            = 500,     # Number
    _Tr8_ChannelLength	            = 30,       # Number
    _Tr8_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR6
    # Physical dimension
    _Tr6_NumberofGate	            = 1,       # Number
    _Tr6_ChannelWidth	            = 500,     # Number
    _Tr6_ChannelLength	            = 30,       # Number
    _Tr6_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR11
    # Physical dimension
    _Tr11_NumberofGate	            = 20,       # Number
    _Tr11_ChannelWidth	            = 500,     # Number
    _Tr11_ChannelLength	            = 30,       # Number
    _Tr11_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# Tie4N
    # Physical dimension
    _Tie4N_NumberofGate     	    = 5,       # Number
    _Tie4N_ChannelWidth	            = 250,     # Number
    _Tie4N_ChannelLength	        = 30,       # Number
    _Tie4N_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# Tie4P
    # Physical dimension
    _Tie4P_NumberofGate	            = 5,       # Number
    _Tie4P_ChannelWidth	            = 500,     # Number
    _Tie4P_ChannelLength	        = 30,       # Number
    _Tie4P_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# Tie8N
    # Physical dimension
    _Tie8N_NumberofGate	            = 4,       # Number
    _Tie8N_ChannelWidth	            = 250,     # Number
    _Tie8N_ChannelLength	        = 30,       # Number
    _Tie8N_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# Tie8P
    # Physical dimension
    _Tie8P_NumberofGate	            = 4,       # Number
    _Tie8P_ChannelWidth	            = 500,     # Number
    _Tie8P_ChannelLength	        = 30,       # Number
    _Tie8P_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR12
    # Physical dimension
    _Tr12_NumberofGate	            = 4,       # Number
    _Tr12_ChannelWidth	            = 1500,     # Number
    _Tr12_ChannelLength	            = 30,       # Number
    _Tr12_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
# TR3
    # Physical dimension
    _Tr3_NumberofGate	            = 2,       # Number
    _Tr3_ChannelWidth	            = 100,     # Number
    _Tr3_ChannelLength	            = 30,       # Number
    _Tr3_XVT				        = 'LVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
# TR10
    # Physical dimension
    _Tr10_NumberofGate	            = 8,       # Number
    _Tr10_ChannelWidth	            = 780,     # Number
    _Tr10_ChannelLength	            = 30,       # Number
    _Tr10_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT


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
    _Tr8_NumberofGate	            = 4,       # Number
    _Tr8_ChannelWidth	            = 500,     # Number
    _Tr8_ChannelLength	            = 30,       # Number
    _Tr8_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR6
    # Physical dimension
    _Tr6_NumberofGate	            = 1,       # Number
    _Tr6_ChannelWidth	            = 500,     # Number
    _Tr6_ChannelLength	            = 30,       # Number
    _Tr6_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR11
    # Physical dimension
    _Tr11_NumberofGate	            = 20,       # Number
    _Tr11_ChannelWidth	            = 500,     # Number
    _Tr11_ChannelLength	            = 30,       # Number
    _Tr11_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# Tie4N
    # Physical dimension
    _Tie4N_NumberofGate     	    = 5,       # Number
    _Tie4N_ChannelWidth	            = 250,     # Number
    _Tie4N_ChannelLength	        = 30,       # Number
    _Tie4N_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# Tie4P
    # Physical dimension
    _Tie4P_NumberofGate	            = 5,       # Number
    _Tie4P_ChannelWidth	            = 500,     # Number
    _Tie4P_ChannelLength	        = 30,       # Number
    _Tie4P_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# Tie8N
    # Physical dimension
    _Tie8N_NumberofGate	            = 4,       # Number
    _Tie8N_ChannelWidth	            = 250,     # Number
    _Tie8N_ChannelLength	        = 30,       # Number
    _Tie8N_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# Tie8P
    # Physical dimension
    _Tie8P_NumberofGate	            = 4,       # Number
    _Tie8P_ChannelWidth	            = 500,     # Number
    _Tie8P_ChannelLength	        = 30,       # Number
    _Tie8P_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR12
    # Physical dimension
    _Tr12_NumberofGate	            = 4,       # Number
    _Tr12_ChannelWidth	            = 1500,     # Number
    _Tr12_ChannelLength	            = 30,       # Number
    _Tr12_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
# TR3
    # Physical dimension
    _Tr3_NumberofGate	            = 2,       # Number
    _Tr3_ChannelWidth	            = 100,     # Number
    _Tr3_ChannelLength	            = 30,       # Number
    _Tr3_XVT				        = 'LVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
# TR10
    # Physical dimension
    _Tr10_NumberofGate	            = 8,       # Number
    _Tr10_ChannelWidth	            = 780,     # Number
    _Tr10_ChannelLength	            = 30,       # Number
    _Tr10_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT


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



        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  C12(Tr(1,2) - Tr(5,7,9) Routed) SREF Generation
        _Caculation_Parameters = copy.deepcopy(C12_00_Tr1Tr2_Tr5Tr7Tr9_Tr4_Tr8._Tr1Tr2_Tr5Tr7Tr9_Tr4_Tr8._ParametersForDesignCalculation)
        _Caculation_Parameters['_Inputnode_width']      = _Inputnode_width
        _Caculation_Parameters['_Outputnode_width']     = _Outputnode_width

        _Caculation_Parameters['_Tr1_NumberofGate']     = _Tr1_NumberofGate
        _Caculation_Parameters['_Tr1_ChannelWidth']     = _Tr1_ChannelWidth
        _Caculation_Parameters['_Tr1_ChannelLength']    = _Tr1_ChannelLength
        _Caculation_Parameters['_Tr1_XVT']              = _Tr1_XVT

        _Caculation_Parameters['_Tr2_NumberofGate']     = _Tr2_NumberofGate
        _Caculation_Parameters['_Tr2_ChannelWidth']     = _Tr2_ChannelWidth
        _Caculation_Parameters['_Tr2_ChannelLength']    = _Tr2_ChannelLength
        _Caculation_Parameters['_Tr2_XVT']              = _Tr2_XVT

        _Caculation_Parameters['_Tr4_NumberofGate']     = _Tr4_NumberofGate
        _Caculation_Parameters['_Tr4_ChannelWidth']     = _Tr4_ChannelWidth
        _Caculation_Parameters['_Tr4_ChannelLength']    = _Tr4_ChannelLength
        _Caculation_Parameters['_Tr4_XVT']              = _Tr4_XVT

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

        _Caculation_Parameters['_Tr8_NumberofGate']     = _Tr8_NumberofGate
        _Caculation_Parameters['_Tr8_ChannelWidth']     = _Tr8_ChannelWidth
        _Caculation_Parameters['_Tr8_ChannelLength']    = _Tr8_ChannelLength
        _Caculation_Parameters['_Tr8_XVT']              = _Tr8_XVT

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_C12'] = self._SrefElementDeclaration(_DesignObj=C12_00_Tr1Tr2_Tr5Tr7Tr9_Tr4_Tr8._Tr1Tr2_Tr5Tr7Tr9_Tr4_Tr8(_DesignParameter=None, _Name='{}:SRF_C12'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_C12']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C12']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C12']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C12']['_XYCoordinates'] = [[0, 0]]

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  _C11(Tr6 - Tr11 Routed) SREF Generation
        _Caculation_Parameters = copy.deepcopy(C11_00_Tr6Tr11Routed_v02._Tr4Tr6Routed._ParametersForDesignCalculation)

        _Caculation_Parameters['_Tr6_NumberofGate']     = _Tr6_NumberofGate
        _Caculation_Parameters['_Tr6_ChannelWidth']     = _Tr6_ChannelWidth
        _Caculation_Parameters['_Tr6_ChannelLength']    = _Tr6_ChannelLength
        _Caculation_Parameters['_Tr6_XVT']              = _Tr6_XVT

        _Caculation_Parameters['_Tr11_NumberofGate']     = _Tr11_NumberofGate
        _Caculation_Parameters['_Tr11_ChannelWidth']     = _Tr11_ChannelWidth
        _Caculation_Parameters['_Tr11_ChannelLength']    = _Tr11_ChannelLength
        _Caculation_Parameters['_Tr11_XVT']              = _Tr11_XVT

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_C11'] = self._SrefElementDeclaration(_DesignObj=C11_00_Tr6Tr11Routed_v02._Tr4Tr6Routed(_DesignParameter=None, _Name='{}:SRF_C11'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_C11']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C11']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C11']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## initialized Sref coordinate
        self._DesignParameter['SRF_C11']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
            ## Target_coord: _XY_type1
        tmp1_1 = self.get_outter_KJH4('SRF_C12','SRF_C05_02_Pin','SRF_Pbodyring2')
        target_coordx = tmp1_1['_Mostright']['coord'][0]

        tmp1_2 = tmp1_1
        tmp1_3 = self.get_outter_KJH4('SRF_C12','SRF_C02_04_Guardring', 'SRF_Pbodyring')
        tmp1_4 = self.get_outter_KJH4('SRF_C12','SRF_C03_02_Pin', 'SRF_Pbodyring2')

        tmp1_5 = min(tmp1_2['_Mostup']['coord'][0],tmp1_3['_Mostup']['coord'][0],tmp1_4['_Mostup']['coord'][0])
        target_coordy = tmp1_5

        target_coord = [target_coordx, target_coordy]

            ## Approaching_coord: _XY_type2
        tmp2_1 = self.get_outter_KJH4('SRF_C11')
        approaching_coordx = tmp2_1['_Mostright']['coord'][0]

        tmp2_2 = self.get_param_KJH4('SRF_C11', 'SRF_Tr6','SRF_Nbodyring', 'SRF_NbodyBottom', 'SRF_NbodyContactPhyLen', 'BND_Nwell')
        approaching_coord = [approaching_coordx, tmp2_2[0][0][0][0][0][0][0]['_XY_down'][1]]
            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_C11')
        Scoord = tmp3[0][0]['_XY_origin']
        NWminspaceT3 = 2500  # DRC NWminspaceT3
        Scoord[1] = Scoord[1] + NWminspaceT3
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['SRF_C11']['_XYCoordinates'] = tmpXY

        tmp3_1 = tmp1_1['_Mostup']['coord'][0]
        tmp3_2 = self.get_outter_KJH4('SRF_C11')['_Mostdown']['coord'][0]
        if tmp3_2 - tmp3_1 < _DRCobj._PpMinSpace:
            PPmargin = 100
            Scoord[1] = Scoord[1] - (tmp3_2 - tmp3_1) + _DRCobj._PpMinSpace + PPmargin
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY = []
            tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['SRF_C11']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Vp node M4 HrzRoute Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_VpNode_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_C11', 'PTH_Tr6Tr11DrainRouting_M3_1')
        tmp2 = self.get_param_KJH4('SRF_C12', 'SRF_C02_04_Guardring', 'BND_Tr5Tr7_Gate_Hrz_M3')

        self._DesignParameter['BND_VpNode_Hrz_M3']['_YWidth'] = abs(tmp1[0][0][0]['_Xwidth'])

        ## Define Boundary_element _XWidth
        C11Tr5GateM4VtcRoutePathWidth = 300
        self._DesignParameter['BND_VpNode_Hrz_M3']['_XWidth'] = tmp1[0][0][0]['_XY_down_left'][0] - tmp2[0][0][0][0]['_XY_down'][0] #+ C11Tr5GateM4VtcRoutePathWidth

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_VpNode_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_VpNode_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_VpNode_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_down_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_VpNode_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_VpNode_Hrz_M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Vp node M4 VtcRoute Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_VpNode_Vtc_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_VpNode_Hrz_M3')
        tmp1_2 = self.get_param_KJH4('SRF_C12', 'SRF_C02_04_Guardring', 'BND_Tr5Tr7_Gate_Hrz_M3')
        self._DesignParameter['BND_VpNode_Vtc_M3']['_YWidth'] = abs(tmp1[0][0]['_XY_up'][1] - tmp1_2[0][0][0][0]['_XY_down'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_VpNode_Vtc_M3']['_XWidth'] = self._DesignParameter['BND_VpNode_Hrz_M3']['_YWidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_VpNode_Vtc_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_VpNode_Vtc_M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_VpNode_Vtc_M3')
        approaching_coord = tmp2[0][0]['_XY_up']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_VpNode_Vtc_M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_VpNode_Vtc_M3']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Tie4 Sref generation
        _Caculation_Parameters = copy.deepcopy(C06_00_VddTieCell._TieCell4._ParametersForDesignCalculation)

        _Caculation_Parameters['_Tie4N_NumberofGate']   = _Tie4N_NumberofGate
        _Caculation_Parameters['_Tie4N_ChannelWidth']   = _Tie4N_ChannelWidth
        _Caculation_Parameters['_Tie4N_ChannelLength']  = _Tie4N_ChannelLength
        _Caculation_Parameters['_Tie4N_XVT']            = _Tie4N_XVT

        _Caculation_Parameters['_Tie4P_NumberofGate']   = _Tie4P_NumberofGate
        _Caculation_Parameters['_Tie4P_ChannelWidth']   = _Tie4P_ChannelWidth
        _Caculation_Parameters['_Tie4P_ChannelLength']  = _Tie4P_ChannelLength
        _Caculation_Parameters['_Tie4P_XVT']            = _Tie4P_XVT

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Tie4'] = self._SrefElementDeclaration(_DesignObj=C06_00_VddTieCell._TieCell4(_DesignParameter=None, _Name='{}:SRF_Tie4'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Tie4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tie4']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tie4']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## initialized Sref coordinate
        self._DesignParameter['SRF_Tie4']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Target_coord: _XY_type1
        tmp = self.get_outter_KJH4('SRF_C12','SRF_C03_02_Pin')
        tmp1_1 = tmp['_Mostleft']['coord'][0]
        tmp1_2 = tmp['_Mostup']['coord'][0]
        target_coord = [tmp1_1, tmp1_2]
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_Tie4', 'SRF_PMOS_Body_Contact','SRF_NbodyContactPhyLen','BND_Nwell')
        approaching_coord = tmp2[0][0][0][0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Tie4')
        Scoord = tmp3[0][0]['_XY_origin']
        C12Tie4space = 100
        Scoord[0] = Scoord[0] - max(_DRCobj._Metal1MinSpace3, C12Tie4space)
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['SRF_Tie4']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Tie4 Drain <-> Tr4 gate route M2 Hrz Boundary_element Generation

        ## Tie4 Drain <-> Tr4 gate route M2 Hrz Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Tie4Tr4Route_Tie4Hrz_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Tie4', 'SRF_TieCellPMOSRouted', 'SRF_Pmos','BND_Drain_Hrz_M2')
        Tie4Tr4Route_Tie4HrzPathWidth = 150
        self._DesignParameter['BND_Tie4Tr4Route_Tie4Hrz_M2']['_YWidth'] = max(tmp1[0][0][0][0][0]['_Ywidth'], Tie4Tr4Route_Tie4HrzPathWidth)

                ## Define Boundary_element _XWidth
        tmp2_1 = tmp1[0][0][0][0][0]['_XY_up_left'][0]
        tmp2_2 = self.get_param_KJH4('SRF_C12', 'SRF_C03_02_Pin','SRF_Guardring','SRF_Tr4','SRF_Nmos','BND_Gate_Hrz_Mx')[0][0][0][0][0][0][0]['_XY_up_right'][0]
        tmp2 = int((tmp2_1 + tmp2_2) / 2)
        self._DesignParameter['BND_Tie4Tr4Route_Tie4Hrz_M2']['_XWidth'] = abs(tmp1[0][0][0][0][0]['_XY_up_left'][0] - tmp2)

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Tie4Tr4Route_Tie4Hrz_M2']['_XYCoordinates'] = [[0, 0]]

                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_Tie4Tr4Route_Tie4Hrz_M2')
        approaching_coord = tmp3[0][0]['_XY_down_left']
                            ## Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Tie4Tr4Route_Tie4Hrz_M2']['_XYCoordinates'] = tmpXY



        # Tie4 Drain <-> Tr4 gate route M2 Vtc Boundary
        self._DesignParameter['BND_Tie4Tr4Route_Vtc_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_Tie4Tr4Route_Tie4Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_C12', 'SRF_C03_02_Pin','SRF_Guardring','SRF_Tr4','SRF_Nmos','BND_Gate_Hrz_Mx')
        self._DesignParameter['BND_Tie4Tr4Route_Vtc_M2']['_YWidth'] = abs(tmp1[0][0]['_XY_up_right'][1] - tmp2[0][0][0][0][0][0][0]['_XY_down_right'][1])

                ## Define Boundary_element _XWidth
        Tie4Tr4Route_VtcRoutePathWidth = 300
        self._DesignParameter['BND_Tie4Tr4Route_Vtc_M2']['_XWidth'] = Tie4Tr4Route_VtcRoutePathWidth

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Tie4Tr4Route_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp1[0][0]['_XY_up_right']
                            ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_Tie4Tr4Route_Vtc_M2')
        approaching_coord = tmp3[0][0]['_XY_up_right']
                            ## Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Tie4Tr4Route_Vtc_M2']['_XYCoordinates'] = tmpXY



        # Tie4 Drain <-> Tr4 gate route M2 Vtc Boundary
        self._DesignParameter['BND_Tie4Tr4Route_Tr4Hrz_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_Tie4Tr4Route_Vtc_M2')
        tmp2 = self.get_param_KJH4('SRF_C12', 'SRF_C03_02_Pin','SRF_Guardring','SRF_Tr4','SRF_Nmos','BND_Gate_Hrz_Mx')
        self._DesignParameter['BND_Tie4Tr4Route_Tr4Hrz_M2']['_YWidth'] = tmp2[0][0][0][0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth

        self._DesignParameter['BND_Tie4Tr4Route_Tr4Hrz_M2']['_XWidth'] = abs(tmp1[0][0]['_XY_up_left'][0] - tmp2[0][0][0][0][0][0][0]['_XY_up_right'][0])

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Tie4Tr4Route_Tr4Hrz_M2']['_XYCoordinates'] = [[0, 0]]

                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp1[0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_Tie4Tr4Route_Tr4Hrz_M2')
        approaching_coord = tmp3[0][0]['_XY_down_left']
                            ## Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Tie4Tr4Route_Tr4Hrz_M2']['_XYCoordinates'] = tmpXY



        ## Tie8 Sref generation
        _Caculation_Parameters = copy.deepcopy(C10_00_VddTieCell._TieCell8._ParametersForDesignCalculation)

        _Caculation_Parameters['_Tie8N_NumberofGate'] = _Tie8N_NumberofGate
        _Caculation_Parameters['_Tie8N_ChannelWidth'] = _Tie8N_ChannelWidth
        _Caculation_Parameters['_Tie8N_ChannelLength'] = _Tie8N_ChannelLength
        _Caculation_Parameters['_Tie8N_XVT'] = _Tie8N_XVT

        _Caculation_Parameters['_Tie8P_NumberofGate'] = _Tie8P_NumberofGate
        _Caculation_Parameters['_Tie8P_ChannelWidth'] = _Tie8P_ChannelWidth
        _Caculation_Parameters['_Tie8P_ChannelLength'] = _Tie8P_ChannelLength
        _Caculation_Parameters['_Tie8P_XVT'] = _Tie8P_XVT

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Tie8'] = self._SrefElementDeclaration(_DesignObj=C10_00_VddTieCell._TieCell8(_DesignParameter=None, _Name='{}:SRF_Tie8'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Tie8']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tie8']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tie8']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## initialized Sref coordinate
        self._DesignParameter['SRF_Tie8']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Target_coord: _XY_type1
        tmp = self.get_outter_KJH4('SRF_C12','SRF_C05_02_Pin')
        tmp1_1 = tmp['_Mostright']['coord'][0]
        tmp1_2 = tmp['_Mostup']['coord'][0]
        target_coord = [tmp1_1, tmp1_2]
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_Tie8', 'SRF_PMOS_Body_Contact','SRF_NbodyContactPhyLen','BND_Nwell')
        approaching_coord = tmp2[0][0][0][0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Tie8')
        Scoord = tmp3[0][0]['_XY_origin']
        C12Tie8space = 100
        Scoord[0] = Scoord[0] + max(_DRCobj._Metal1MinSpace3, C12Tie8space)
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['SRF_Tie8']['_XYCoordinates'] = tmpXY


        ## Tie8 Drain <-> Tr8 gate route
        # M2 Hrz(Tie8쪽에 붙은) Boundary_element Generation
        self._DesignParameter['BND_Tie8Tr8Route_Tie8Hrz_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Tie8', 'SRF_TieCellPMOSRouted', 'SRF_Pmos','BND_Drain_Hrz_M2')
        Tie8Tr8Route_Tie8HrzPathWidth = 150
        self._DesignParameter['BND_Tie8Tr8Route_Tie8Hrz_M2']['_YWidth'] = max(tmp1[0][0][0][0][0]['_Ywidth'], Tie8Tr8Route_Tie8HrzPathWidth)

        ## Define Boundary_element _XWidth
        tmp2_1 = tmp1[0][0][0][0][0]['_XY_up_right'][0]
        tmp2_2 = self.get_param_KJH4('SRF_C12', 'SRF_C05_02_Pin','SRF_Guardring','SRF_Tr8','SRF_Nmos' ,'BND_Gate_Hrz_Mx')[0][0][0][0][0][0][0]['_XY_up_left'][0]
        tmp2 = int((tmp2_1 + tmp2_2) / 2)
        self._DesignParameter['BND_Tie8Tr8Route_Tie8Hrz_M2']['_XWidth'] = abs(tmp1[0][0][0][0][0]['_XY_up_left'][0] - tmp2)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Tie8Tr8Route_Tie8Hrz_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0]['_XY_down_right']
        ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_Tie8Tr8Route_Tie8Hrz_M2')
        approaching_coord = tmp3[0][0]['_XY_down_right']
        ## Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Tie8Tr8Route_Tie8Hrz_M2']['_XYCoordinates'] = tmpXY


        ## Tie8 Drain <-> Tr8 gate route M2 Vtc Boundary
        self._DesignParameter['BND_Tie8Tr8Route_Vtc_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_Tie8Tr8Route_Tie8Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_C12', 'SRF_C05_02_Pin','SRF_Guardring','SRF_Tr8','SRF_Nmos' ,'BND_Gate_Hrz_Mx')
        self._DesignParameter['BND_Tie8Tr8Route_Vtc_M2']['_YWidth'] = abs(tmp1[0][0]['_XY_up_left'][1] - tmp2[0][0][0][0][0][0][0]['_XY_down_left'][1])

                ## Define Boundary_element _XWidth
        Tie8Tr8Route_VtcRoutePathWidth = 300
        self._DesignParameter['BND_Tie8Tr8Route_Vtc_M2']['_XWidth'] = Tie8Tr8Route_VtcRoutePathWidth

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Tie8Tr8Route_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp1[0][0]['_XY_up_left']
                            ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_Tie8Tr8Route_Vtc_M2')
        approaching_coord = tmp3[0][0]['_XY_up_left']
                            ## Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Tie8Tr8Route_Vtc_M2']['_XYCoordinates'] = tmpXY



        ## Tie8 Drain <-> Tr8 gate route M2 Vtc Boundary
        # M2 Hrz(Tr8쪽에 붙은) Boundary_element Generation
        self._DesignParameter['BND_Tie8Tr8Route_Tr8Hrz_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_Tie8Tr8Route_Vtc_M2')
        tmp2 = self.get_param_KJH4('SRF_C12', 'SRF_C05_02_Pin','SRF_Guardring','SRF_Tr8','SRF_Nmos' ,'BND_Gate_Hrz_Mx')
        self._DesignParameter['BND_Tie8Tr8Route_Tr8Hrz_M2']['_YWidth'] = tmp2[0][0][0][0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Tie8Tr8Route_Tr8Hrz_M2']['_XWidth'] = abs(tmp1[0][0]['_XY_up_right'][0] - tmp2[0][0][0][0][0][0][0]['_XY_down_left'][0])

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Tie8Tr8Route_Tr8Hrz_M2']['_XYCoordinates'] = [[0, 0]]

                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp1[0][0]['_XY_down_right']
                            ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_Tie8Tr8Route_Tr8Hrz_M2')
        approaching_coord = tmp3[0][0]['_XY_down_right']
                            ## Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Tie8Tr8Route_Tr8Hrz_M2']['_XYCoordinates'] = tmpXY


            ## C07(Tr12Tr3Tr10)_04_Guardring SREF Generation
        _Caculation_Parameters = copy.deepcopy(C07_04_Guardring._Guardring._ParametersForDesignCalculation)

        _Caculation_Parameters['_Tr12_NumberofGate'] = _Tr12_NumberofGate
        _Caculation_Parameters['_Tr12_ChannelWidth'] = _Tr12_ChannelWidth
        _Caculation_Parameters['_Tr12_ChannelLength'] = _Tr12_ChannelLength
        _Caculation_Parameters['_Tr12_XVT'] = _Tr12_XVT

        _Caculation_Parameters['_Tr3_NumberofGate'] = _Tr3_NumberofGate
        _Caculation_Parameters['_Tr3_ChannelWidth'] = _Tr3_ChannelWidth
        _Caculation_Parameters['_Tr3_ChannelLength'] = _Tr3_ChannelLength
        _Caculation_Parameters['_Tr3_XVT'] = _Tr3_XVT

        _Caculation_Parameters['_Tr10_NumberofGate'] = _Tr10_NumberofGate
        _Caculation_Parameters['_Tr10_ChannelWidth'] = _Tr10_ChannelWidth
        _Caculation_Parameters['_Tr10_ChannelLength'] = _Tr10_ChannelLength
        _Caculation_Parameters['_Tr10_XVT'] = _Tr10_XVT

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_C07'] = self._SrefElementDeclaration(_DesignObj=C07_04_Guardring._Guardring(_DesignParameter=None, _Name='{}:SRF_C07'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_C07']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C07']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C07']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## initialized Sref coordinate
        self._DesignParameter['SRF_C07']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Target_coord: _XY_type1
        tmp = self.get_outter_KJH4('SRF_C12', 'SRF_C03_02_Pin')
        tmp1_1 = tmp['_Mostright']['coord'][0]
        tmp1_2 = tmp['_Mostup']['coord'][0]
        target_coord = [tmp1_1, tmp1_2]
        ## Approaching_coord: _XY_type2
        tmp2_1 = self.get_param_KJH4('SRF_C07', 'SRF_Tr12Tr3Tr10', 'SRF_Tr3','BND_Source_Hrz_M2')[0][0][0][0][0]['_XY_down_right'][0]
        tmp2_2 = self.get_outter_KJH4('SRF_C07')['_Mostdown']['coord'][0]
        approaching_coord = [tmp2_1, tmp2_2]
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_C07')
        Scoord = tmp3[0][0]['_XY_origin']
        C07C12space = 100
        Scoord[1] = Scoord[1] + max(_DRCobj._PpMinSpace, C07C12space)
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['SRF_C07']['_XYCoordinates'] = tmpXY


        ## Tr3 Drain <-> Tr4 Source route_M2
        # M2 Hrz boundary route generation
        self._DesignParameter['BND_Tr3Tr4Route_Vtc_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_C07', 'SRF_Tr12Tr3Tr10', 'SRF_Tr3','BND_Source_Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_C12', 'SRF_C03_02_Pin', 'SRF_Guardring', 'SRF_Tr4','SRF_Nmos','BND_Source_Hrz_M2')
        self._DesignParameter['BND_Tr3Tr4Route_Vtc_M2']['_YWidth'] = abs(tmp1[0][0][0][0][0]['_XY_up_right'][1] - tmp2[0][0][0][0][0][0][0]['_XY_down_right'][1])

        ## Define Boundary_element _XWidth
        Tr3Tr4Route_VtcRoutePathWidth = 300
        self._DesignParameter['BND_Tr3Tr4Route_Vtc_M2']['_XWidth'] = Tr3Tr4Route_VtcRoutePathWidth

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Tr3Tr4Route_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0]['_XY_up_right']
        ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_Tr3Tr4Route_Vtc_M2')
        approaching_coord = tmp3[0][0]['_XY_up_right']
        ## Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Tr3Tr4Route_Vtc_M2']['_XYCoordinates'] = tmpXY


        ## Tr3 Drain <-> Tr4 Source route_M2
        # M2 Hrz boundary route generation
        self._DesignParameter['BND_Tr3Tr4Route_Hrz_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Tr3Tr4Route_Vtc_M2')
        tmp2 = self.get_param_KJH4('SRF_C12', 'SRF_C03_02_Pin', 'SRF_Guardring', 'SRF_Tr4','SRF_Nmos','BND_Source_Hrz_M2')
        self._DesignParameter['BND_Tr3Tr4Route_Hrz_M2']['_YWidth'] = tmp2[0][0][0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        Tr3Tr4Route_VtcRoutePathWidth = 300
        self._DesignParameter['BND_Tr3Tr4Route_Hrz_M2']['_XWidth'] = abs(tmp1[0][0]['_XY_down_right'][0] - tmp2[0][0][0][0][0][0][0]['_XY_down_left'][0])

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Tr3Tr4Route_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0]['_XY_down_right']
        ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_Tr3Tr4Route_Hrz_M2')
        approaching_coord = tmp3[0][0]['_XY_down_right']
        ## Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Tr3Tr4Route_Hrz_M2']['_XYCoordinates'] = tmpXY




        ## Tr10 Drain <-> Tr8 Source route_M2
        # Tr10 Drain 쪽 가장 긴 Horizontal Boundary_element Generation
        self._DesignParameter['BND_Tr8Tr10Route_Tr10Hrz_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        Tr8Tr10Route_Tr10HrzRoutePathWidth = 300
        self._DesignParameter['BND_Tr8Tr10Route_Tr10Hrz_M2']['_YWidth'] = Tr8Tr10Route_Tr10HrzRoutePathWidth

                ## Define Boundary_element _XWidth
        tmp1_1 = self.get_outter_KJH4('SRF_C12', 'SRF_C02_04_Guardring')['_Mostright']['coord'][0]
        tmp1_2 = self.get_outter_KJH4('SRF_C12', 'SRF_C05_02_Pin')['_Mostleft']['coord'][0]
        tmp1 = int((tmp1_1 + tmp1_2)/2)
        tmp2 = self.get_param_KJH4('SRF_C07', 'SRF_Tr12Tr3Tr10', 'SRF_Tr10', 'BND_Source_Hrz_M2')
        self._DesignParameter['BND_Tr8Tr10Route_Tr10Hrz_M2']['_XWidth'] = abs(tmp2[0][0][0][0][0]['_XY_up_left'][0] - tmp1) + Tr8Tr10Route_Tr10HrzRoutePathWidth

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Tr8Tr10Route_Tr10Hrz_M2']['_XYCoordinates'] = [[0, 0]]

                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp2[0][0][0][0][0]['_XY_up_left']
                            ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_Tr8Tr10Route_Tr10Hrz_M2')
        approaching_coord = tmp3[0][0]['_XY_up_left']
                            ## Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Tr8Tr10Route_Tr10Hrz_M2']['_XYCoordinates'] = tmpXY

        ## Tr10 Drain <-> Tr8 Source route_M2
        # Vertical Boundary_element Generation
        self._DesignParameter['BND_Tr8Tr10Route_Vtc_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Tr8Tr10Route_Tr10Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_C12', 'SRF_C05_02_Pin', 'SRF_Guardring', 'SRF_Tr8', 'SRF_Nmos','BND_Source_Hrz_M2')
        self._DesignParameter['BND_Tr8Tr10Route_Vtc_M2']['_YWidth'] = abs(tmp1[0][0]['_XY_up_right'][1] - tmp2[0][0][0][0][0][0][0]['_XY_down_left'][1])

        ## Define Boundary_element _XWidth
        Tr8Tr10Route_VtcRoutePathWidth = 300
        self._DesignParameter['BND_Tr8Tr10Route_Vtc_M2']['_XWidth'] = Tr8Tr10Route_VtcRoutePathWidth

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Tr8Tr10Route_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0]['_XY_up_right']
        ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_Tr8Tr10Route_Vtc_M2')
        approaching_coord = tmp3[0][0]['_XY_up_right']
        ## Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Tr8Tr10Route_Vtc_M2']['_XYCoordinates'] = tmpXY


        ## Tr10 Drain <-> Tr8 Source route_M2
        # Tr8 쪽 Horizontal Boundary_element Generation
        self._DesignParameter['BND_Tr8Tr10Route_Tr8Hrz_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Tr8Tr10Route_Vtc_M2')
        tmp2 = self.get_param_KJH4('SRF_C12', 'SRF_C05_02_Pin', 'SRF_Guardring', 'SRF_Tr8', 'SRF_Nmos','BND_Source_Hrz_M2')
        self._DesignParameter['BND_Tr8Tr10Route_Tr8Hrz_M2']['_YWidth'] = tmp2[0][0][0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Tr8Tr10Route_Tr8Hrz_M2']['_XWidth'] = abs(tmp1[0][0]['_XY_down_left'][0] - tmp2[0][0][0][0][0][0][0]['_XY_down_right'][0])

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Tr8Tr10Route_Tr8Hrz_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp2[0][0][0][0][0][0][0]['_XY_up_right']
        ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_Tr8Tr10Route_Tr8Hrz_M2')
        approaching_coord = tmp3[0][0]['_XY_up_right']
        ## Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Tr8Tr10Route_Tr8Hrz_M2']['_XYCoordinates'] = tmpXY

        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')
        # start_time = time.time()
        end_time = time.time()
        self.elapsed_time = end_time - start_time



############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    Start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ZZ01_C13_00_C07C11C12TieCellsRouted_Fixed'
    cellname = 'C13_00_C07C11C12TieCellsRouted_v01_99'
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
    _Tr8_NumberofGate	            = 4,       # Number
    _Tr8_ChannelWidth	            = 500,     # Number
    _Tr8_ChannelLength	            = 30,       # Number
    _Tr8_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
# TR6
    # Physical dimension
    _Tr6_NumberofGate	            = 1,       # Number
    _Tr6_ChannelWidth	            = 500,     # Number
    _Tr6_ChannelLength	            = 30,       # Number
    _Tr6_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
# TR11
    # Physical dimension
    _Tr11_NumberofGate	            = 20,       # Number
    _Tr11_ChannelWidth	            = 500,     # Number
    _Tr11_ChannelLength	            = 30,       # Number
    _Tr11_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
# Tie4N
    # Physical dimension
    _Tie4N_NumberofGate     	    = 5,       # Number
    _Tie4N_ChannelWidth	            = 250,     # Number
    _Tie4N_ChannelLength	        = 30,       # Number
    _Tie4N_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
# Tie4P
    # Physical dimension
    _Tie4P_NumberofGate	            = 5,       # Number
    _Tie4P_ChannelWidth	            = 500,     # Number
    _Tie4P_ChannelLength	        = 30,       # Number
    _Tie4P_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
# Tie8N
    # Physical dimension
    _Tie8N_NumberofGate	            = 4,       # Number
    _Tie8N_ChannelWidth	            = 250,     # Number
    _Tie8N_ChannelLength	        = 30,       # Number
    _Tie8N_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
# Tie8P
    # Physical dimension
    _Tie8P_NumberofGate	            = 4,       # Number
    _Tie8P_ChannelWidth	            = 500,     # Number
    _Tie8P_ChannelLength	        = 30,       # Number
    _Tie8P_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
# TR12
    # Physical dimension
    _Tr12_NumberofGate	            = 4,       # Number
    _Tr12_ChannelWidth	            = 1500,     # Number
    _Tr12_ChannelLength	            = 30,       # Number
    _Tr12_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
# TR3
    # Physical dimension
    _Tr3_NumberofGate	            = 2,       # Number
    _Tr3_ChannelWidth	            = 100,     # Number
    _Tr3_ChannelLength	            = 30,       # Number
    _Tr3_XVT				        = 'LVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
# TR10
    # Physical dimension
    _Tr10_NumberofGate	            = 8,       # Number
    _Tr10_ChannelWidth	            = 780,     # Number
    _Tr10_ChannelLength	            = 30,       # Number
    _Tr10_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

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
    LayoutObj = _C07C11C12TieCellsRouted(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    # testStreamFile = open('./gdsfile/{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    ''' Check Time'''
    elapsed_time = time.time() - Start_time
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
    Checker.lib_deletion()
    # Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()

    print('#############################      Finished      ################################')
    print('{} Hours   {} minutes   {} seconds'.format(h, m, s))
# end of 'main():' ---------------------------------------------------------------------------------------------