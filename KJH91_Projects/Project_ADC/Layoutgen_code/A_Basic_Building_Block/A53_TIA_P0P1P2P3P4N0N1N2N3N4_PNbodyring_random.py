from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC_EGFET

import numpy as np
import copy
import math

from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A52_TIA_P1P2P4_Nbodyring_random
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A51_TIA_N2N3_random
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A51_TIA_P0P3_random
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A51_TIA_N0N1N4_random
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_TIA_Pbodyring

from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_TIA_NbodyContactPhyLen
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_TIA_PbodyContactPhyLen

from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_opppcres_b
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A51_HDVNCAP_2

from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2_YCH




## ########################################################################################################################################################## Class_HEADER
class _TIA_P0P1P2P3P4N0N1N2N3N4_PNbodyring_YCH(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

        # PMOS
        _Tr0_PMOSNumberofGate=None,
        _Tr0_PMOSChannelWidth=None,
        _Tr0_PMOSChannellength=None,
        _Tr0_PMOSGateSpacing	= None,
        _Tr0_PMOSSDWidth			= None,
        _Tr0_PMOSXVT				= None,
        _Tr0_PMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _Tr0_PMOSSource_Via_TF = None,

        # Drain_node_ViaM1M2
        _Tr0_PMOSDrain_Via_TF = None,

        # POLY dummy setting
        _Tr0_PMOSDummy = None, # TF
        # if _PMOSDummy == True
        _Tr0_PMOSDummy_length = None, # None/Value
        _Tr0_PMOSDummy_placement = None, # None/Up/Dn/

        # PMOS
        _Tr1_PMOSNumberofGate=45,
        _Tr1_PMOSChannelWidth=6000,
        _Tr1_PMOSChannellength=150,
        _Tr1_PMOSGateSpacing	= None,
        _Tr1_PMOSSDWidth			= None,
        _Tr1_PMOSXVT				= 'EG',
        _Tr1_PMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _Tr1_PMOSSource_Via_TF = True,

        # Drain_node_ViaM1M2
        _Tr1_PMOSDrain_Via_TF = True,

        # POLY dummy setting
        _Tr1_PMOSDummy = True, # TF
        # if _PMOSDummy == True
        _Tr1_PMOSDummy_length = None, # None/Value
        _Tr1_PMOSDummy_placement = None, # None/'Up'/'Dn'/

        # PMOS
        _Tr2_PMOSNumberofGate=None,
        _Tr2_PMOSChannelWidth=None,
        _Tr2_PMOSChannellength=None,
        _Tr2_PMOSGateSpacing	= None,
        _Tr2_PMOSSDWidth			= None,
        _Tr2_PMOSXVT				= None,
        _Tr2_PMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _Tr2_PMOSSource_Via_TF = None,

        # Drain_node_ViaM1M2
        _Tr2_PMOSDrain_Via_TF = None,

        # POLY dummy setting
        _Tr2_PMOSDummy = None, # TF
        # if _PMOSDummy == True
        _Tr2_PMOSDummy_length = None, # None/Value
        _Tr2_PMOSDummy_placement = None, # None/Up/Dn/

        # PMOS
        _Tr3_PMOSNumberofGate=None,
        _Tr3_PMOSChannelWidth=None,
        _Tr3_PMOSChannellength=None,
        _Tr3_PMOSGateSpacing	= None,
        _Tr3_PMOSSDWidth			= None,
        _Tr3_PMOSXVT				= None,
        _Tr3_PMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _Tr3_PMOSSource_Via_TF = None,

        # Drain_node_ViaM1M2
        _Tr3_PMOSDrain_Via_TF = None,

        # POLY dummy setting
        _Tr3_PMOSDummy = None, # TF
        # if _PMOSDummy == True
        _Tr3_PMOSDummy_length = None, # None/Value
        _Tr3_PMOSDummy_placement = None, # None/Up/Dn/

        #PMOS
        _Tr4_PMOSNumberofGate	= None,
        _Tr4_PMOSChannelWidth	= None,
        _Tr4_PMOSChannellength	= None,
        _Tr4_PMOSGateSpacing		= None,
        _Tr4_PMOSSDWidth			= None,
        _Tr4_PMOSXVT				= None,
        _Tr4_PMOSPCCrit				= None,

        #Source_node_ViaM1M2
        _Tr4_PMOSSource_Via_TF = None,

        #Drain_node_ViaM1M2
        _Tr4_PMOSDrain_Via_TF = None,

        #POLY dummy setting
        _Tr4_PMOSDummy = None, #TF
            #if _PMOSDummy == True
        _Tr4_PMOSDummy_length = None, #None/Value
        _Tr4_PMOSDummy_placement = None, #None/Up/Dn/

        # NMOS Tr0
        _Tr0_NMOSNumberofGate=15,
        _Tr0_NMOSChannelWidth=3000,
        _Tr0_NMOSChannellength=150,
        _Tr0_NMOSGateSpacing=None,
        _Tr0_NMOSSDWidth	= None,
        _Tr0_NMOSXVT			= 'EG',
        _Tr0_NMOSPCCrit			= None,

        # Source_node_ViaM1M2
        _Tr0_NMOSSource_Via_TF= True,

        # Drain_node_ViaM1M2
        _Tr0_NMOSDrain_Via_TF= True,

        # POLY dummy setting
        _Tr0_NMOSDummy= True  , # TF
        # if _PMOSDummy == True
        _Tr0_NMOSDummy_length = None, # None/Value
        _Tr0_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        # NMOS Tr0
        _Tr1_NMOSNumberofGate=15,
        _Tr1_NMOSChannelWidth=3000,
        _Tr1_NMOSChannellength=150,
        _Tr1_NMOSGateSpacing	= None,
        _Tr1_NMOSSDWidth			= None,
        _Tr1_NMOSXVT				= 'EG',
        _Tr1_NMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _Tr1_NMOSSource_Via_TF = True,

        # Drain_node_ViaM1M2
        _Tr1_NMOSDrain_Via_TF = True,

        # POLY dummy setting
        _Tr1_NMOSDummy = True, # TF
        # if _PMOSDummy == True
        _Tr1_NMOSDummy_length = None, # None/Value
        _Tr1_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        # NMOS
        _Tr2_NMOSNumberofGate=5,
        _Tr2_NMOSChannelWidth=3000,
        _Tr2_NMOSChannellength=150,
        _Tr2_NMOSGateSpacing=None,
        _Tr2_NMOSSDWidth	= None,
        _Tr2_NMOSXVT			= 'EG',
        _Tr2_NMOSPCCrit			= None,

        # Source_node_ViaM1M2
        _Tr2_NMOSSource_Via_TF= True,

        # Drain_node_ViaM1M2
        _Tr2_NMOSDrain_Via_TF= True,

        # POLY dummy setting
        _Tr2_NMOSDummy= True  , # TF
        # if _PMOSDummy == True
        _Tr2_NMOSDummy_length = None, # None/Value
        _Tr2_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        # NMOS
        _Tr3_NMOSNumberofGate=1,
        _Tr3_NMOSChannelWidth=3000,
        _Tr3_NMOSChannellength=150,
        _Tr3_NMOSGateSpacing	= None,
        _Tr3_NMOSSDWidth			= None,
        _Tr3_NMOSXVT				= 'EG',
        _Tr3_NMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _Tr3_NMOSSource_Via_TF = True,

        # Drain_node_ViaM1M2
        _Tr3_NMOSDrain_Via_TF = True,

        # POLY dummy setting
        _Tr3_NMOSDummy = True, # TF
        # if _PMOSDummy == True
        _Tr3_NMOSDummy_length = None, # None/Value
        _Tr3_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        # NMOS Tr0
        _Tr4_NMOSNumberofGate=8,
        _Tr4_NMOSChannelWidth=3000,
        _Tr4_NMOSChannellength=150,
        _Tr4_NMOSGateSpacing	= None,
        _Tr4_NMOSSDWidth			= None,
        _Tr4_NMOSXVT				= 'EG',
        _Tr4_NMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _Tr4_NMOSSource_Via_TF = True,

        # Drain_node_ViaM1M2
        _Tr4_NMOSDrain_Via_TF = True,

        # POLY dummy setting
        _Tr4_NMOSDummy = True, # TF
        # if _PMOSDummy == True
        _Tr4_NMOSDummy_length = None, # None/Value
        _Tr4_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        _NumContTop_P1P2P4 = 3,
        _NumContBottom_P1P2P4 = 3,
        _NumContLeft_P1P2P4 = 3,
        _NumContRight_P1P2P4 = 3,

        # N body ring(P0P3)
        _NumContTop_P0P3=3,
        _NumContLeft_P0P3=3,
        _NumContRight_P0P3=3,

        # P body ring
        _NumContTop_Pbody=3,
        _NumContBottom_Pbody=3,
        _NumContLeft_Pbody=3,
        _NumContRight_Pbody=3,

        # Res0
        _ResWidth_res0=400,
        _ResLength_res0=508,
        _CONUMX_res0=None,
        _CONUMY_res0=None,
        _SeriesStripes_res0=4,
        _ParallelStripes_res0=1,

        # Res0
        _ResWidth_res1=400,
        _ResLength_res1=508,
        _CONUMX_res1=None,
        _CONUMY_res1=None,
        _SeriesStripes_res1=4,
        _ParallelStripes_res1=1,

        # Cap0
        _Length_cap0=7800,
        _LayoutOption_cap0=[2, 3, 4, 5],
        _NumFigPair_cap0=50,

        _Array_cap0=1,  # number: 1xnumber
        _Cbot_Ctop_metalwidth_cap0=500,  # number

        # Cap1
        _Length_cap1=7800,
        _LayoutOption_cap1=[2, 3, 4, 5],
        _NumFigPair_cap1=50,

        _Array_cap1=1,  # number: 1xnumber
        _Cbot_Ctop_metalwidth_cap1=500,  # number
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

        ## ################################################################################################################################################ _CalculateDesignParameter

    def _CalculateDesignParameter(self,
                                  # PMOS
                                  _Tr0_PMOSNumberofGate=None,
                                  _Tr0_PMOSChannelWidth=None,
                                  _Tr0_PMOSChannellength=None,
                                  _Tr0_PMOSGateSpacing=None,
                                  _Tr0_PMOSSDWidth=None,
                                  _Tr0_PMOSXVT=None,
                                  _Tr0_PMOSPCCrit=None,

                                  # Source_node_ViaM1M2
                                  _Tr0_PMOSSource_Via_TF=None,

                                  # Drain_node_ViaM1M2
                                  _Tr0_PMOSDrain_Via_TF=None,

                                  # POLY dummy setting
                                  _Tr0_PMOSDummy=None,  # TF
                                  # if _PMOSDummy == True
                                  _Tr0_PMOSDummy_length=None,  # None/Value
                                  _Tr0_PMOSDummy_placement=None,  # None/Up/Dn/

                                  # PMOS
                                  _Tr1_PMOSNumberofGate=None,
                                  _Tr1_PMOSChannelWidth=None,
                                  _Tr1_PMOSChannellength=None,
                                  _Tr1_PMOSGateSpacing=None,
                                  _Tr1_PMOSSDWidth=None,
                                  _Tr1_PMOSXVT	= None,
                                  _Tr1_PMOSPCCrit		= None,

                                  # Source_node_ViaM1M2
                                  _Tr1_PMOSSource_Via_TF= None,

                                  # Drain_node_ViaM1M2
                                  _Tr1_PMOSDrain_Via_TF= None,

                                  # POLY dummy setting
                                  _Tr1_PMOSDummy= None  , # TF
                                  # if _PMOSDummy == True
                                  _Tr1_PMOSDummy_length = None, # None/Value
                                  _Tr1_PMOSDummy_placement = None, # None/Up/Dn/

                                  # PMOS
                                  _Tr2_PMOSNumberofGate=None,
                                  _Tr2_PMOSChannelWidth=None,
                                  _Tr2_PMOSChannellength=None,
                                  _Tr2_PMOSGateSpacing=None,
                                  _Tr2_PMOSSDWidth	= None,
                                  _Tr2_PMOSXVT			= None,
                                  _Tr2_PMOSPCCrit			= None,

                                  # Source_node_ViaM1M2
                                  _Tr2_PMOSSource_Via_TF= None,

                                  # Drain_node_ViaM1M2
                                  _Tr2_PMOSDrain_Via_TF= None,

                                  # POLY dummy setting
                                  _Tr2_PMOSDummy= None  , # TF
                                  # if _PMOSDummy == True
                                  _Tr2_PMOSDummy_length = None, # None/Value
                                  _Tr2_PMOSDummy_placement = None, # None/Up/Dn/

                                  # PMOS
                                  _Tr3_PMOSNumberofGate=None,
                                  _Tr3_PMOSChannelWidth=None,
                                  _Tr3_PMOSChannellength=None,
                                  _Tr3_PMOSGateSpacing=None,
                                  _Tr3_PMOSSDWidth=None,
                                  _Tr3_PMOSXVT	= None,
                                  _Tr3_PMOSPCCrit		= None,

                                  # Source_node_ViaM1M2
                                  _Tr3_PMOSSource_Via_TF= None,

                                  # Drain_node_ViaM1M2
                                  _Tr3_PMOSDrain_Via_TF= None,

                                  # POLY dummy setting
                                  _Tr3_PMOSDummy= None  , # TF
                                  # if _PMOSDummy == True
                                  _Tr3_PMOSDummy_length = None, # None/Value
                                  _Tr3_PMOSDummy_placement = None, # None/Up/Dn/

                                  # PMOS
                                  _Tr4_PMOSNumberofGate=None,
                                  _Tr4_PMOSChannelWidth=None,
                                  _Tr4_PMOSChannellength=None,
                                  _Tr4_PMOSGateSpacing=None,
                                  _Tr4_PMOSSDWidth	= None,
                                  _Tr4_PMOSXVT			= None,
                                  _Tr4_PMOSPCCrit			= None,

                                  # Source_node_ViaM1M2
                                  _Tr4_PMOSSource_Via_TF= None,

                                  # Drain_node_ViaM1M2
                                  _Tr4_PMOSDrain_Via_TF= None,

                                  # POLY dummy setting
                                  _Tr4_PMOSDummy= None  , # TF
                                  # if _PMOSDummy == True
                                  _Tr4_PMOSDummy_length = None, # None/Value
                                  _Tr4_PMOSDummy_placement = None, # None/Up/Dn/

                                  #NMOS
                                  _Tr0_NMOSNumberofGate=None,
                                  _Tr0_NMOSChannelWidth=None,
                                  _Tr0_NMOSChannellength=None,
                                  _Tr0_NMOSGateSpacing=None,
                                  _Tr0_NMOSSDWidth=None,
                                  _Tr0_NMOSXVT	= None,
                                  _Tr0_NMOSPCCrit		= None,

                                  # Source_node_ViaM1M2
                                  _Tr0_NMOSSource_Via_TF= None,

                                  # Drain_node_ViaM1M2
                                  _Tr0_NMOSDrain_Via_TF= None,

                                  # POLY dummy setting
                                  _Tr0_NMOSDummy= None  , # TF
                                  # if _PMOSDummy == True
                                  _Tr0_NMOSDummy_length = None, # None/Value
                                  _Tr0_NMOSDummy_placement = None, # None/Up/Dn/

                                  # NMOS
                                  _Tr1_NMOSNumberofGate=None,
                                  _Tr1_NMOSChannelWidth=None,
                                  _Tr1_NMOSChannellength=None,
                                  _Tr1_NMOSGateSpacing=None,
                                  _Tr1_NMOSSDWidth	= None,
                                  _Tr1_NMOSXVT			= None,
                                  _Tr1_NMOSPCCrit			= None,

                                  # Source_node_ViaM1M2
                                  _Tr1_NMOSSource_Via_TF= None,

                                  # Drain_node_ViaM1M2
                                  _Tr1_NMOSDrain_Via_TF= None,

                                  # POLY dummy setting
                                  _Tr1_NMOSDummy= None  , # TF
                                  # if _PMOSDummy == True
                                  _Tr1_NMOSDummy_length = None, # None/Value
                                  _Tr1_NMOSDummy_placement = None, # None/Up/Dn/

                                  # NMOS
                                  _Tr2_NMOSNumberofGate=None,
                                  _Tr2_NMOSChannelWidth=None,
                                  _Tr2_NMOSChannellength=None,
                                  _Tr2_NMOSGateSpacing=None,
                                  _Tr2_NMOSSDWidth=None,
                                  _Tr2_NMOSXVT=None,
                                  _Tr2_NMOSPCCrit=None,

                                  # Source_node_ViaM1M2
                                  _Tr2_NMOSSource_Via_TF=None,

                                  # Drain_node_ViaM1M2
                                  _Tr2_NMOSDrain_Via_TF=None,

                                  # POLY dummy setting
                                  _Tr2_NMOSDummy=None,  # TF
                                  # if _PMOSDummy == True
                                  _Tr2_NMOSDummy_length=None,  # None/Value
                                  _Tr2_NMOSDummy_placement=None,  # None/Up/Dn/

                                  # NMOS
                                  _Tr3_NMOSNumberofGate=None,
                                  _Tr3_NMOSChannelWidth=None,
                                  _Tr3_NMOSChannellength=None,
                                  _Tr3_NMOSGateSpacing=None,
                                  _Tr3_NMOSSDWidth=None,
                                  _Tr3_NMOSXVT	= None,
                                  _Tr3_NMOSPCCrit		= None,

                                  # Source_node_ViaM1M2
                                  _Tr3_NMOSSource_Via_TF= None,

                                  # Drain_node_ViaM1M2
                                  _Tr3_NMOSDrain_Via_TF= None,

                                  # POLY dummy setting
                                  _Tr3_NMOSDummy= None  , # TF
                                  # if _PMOSDummy == True
                                  _Tr3_NMOSDummy_length = None, # None/Value
                                  _Tr3_NMOSDummy_placement = None, # None/Up/Dn/

                                  # NMOS
                                  _Tr4_NMOSNumberofGate=None,
                                  _Tr4_NMOSChannelWidth=None,
                                  _Tr4_NMOSChannellength=None,
                                  _Tr4_NMOSGateSpacing=None,
                                  _Tr4_NMOSSDWidth	= None,
                                  _Tr4_NMOSXVT			= None,
                                  _Tr4_NMOSPCCrit			= None,

                                  # Source_node_ViaM1M2
                                  _Tr4_NMOSSource_Via_TF= None,

                                  # Drain_node_ViaM1M2
                                  _Tr4_NMOSDrain_Via_TF= None,

                                  # POLY dummy setting
                                  _Tr4_NMOSDummy= None  , # TF
                                  # if _PMOSDummy == True
                                  _Tr4_NMOSDummy_length = None, # None/Value
                                  _Tr4_NMOSDummy_placement = None, # None/Up/Dn/

                                  _NumContTop_P1P2P4=3,
                                  _NumContBottom_P1P2P4=3,
                                  _NumContLeft_P1P2P4=3,
                                  _NumContRight_P1P2P4=3,

                                  # N body ring(P0P3)
                                  _NumContTop_P0P3=3,
                                  _NumContLeft_P0P3=3,
                                  _NumContRight_P0P3=3,

                                  # P body ring
                                  _NumContTop_Pbody=3,
                                  _NumContBottom_Pbody=3,
                                  _NumContLeft_Pbody=3,
                                  _NumContRight_Pbody=3,

                                  # Res0
                                  _ResWidth_res0=400,
                                  _ResLength_res0=508,
                                  _CONUMX_res0=None,
                                  _CONUMY_res0=None,
                                  _SeriesStripes_res0=4,
                                  _ParallelStripes_res0=1,

                                  # Res0
                                  _ResWidth_res1=400,
                                  _ResLength_res1=508,
                                  _CONUMX_res1=None,
                                  _CONUMY_res1=None,
                                  _SeriesStripes_res1=4,
                                  _ParallelStripes_res1=1,

                                  # Cap0
                                  _Length_cap0=7800,
                                  _LayoutOption_cap0=[2, 3, 4, 5],
                                  _NumFigPair_cap0=50,

                                  _Array_cap0=1,  # number: 1xnumber
                                  _Cbot_Ctop_metalwidth_cap0=500,  # number

                                  # Cap1
                                  _Length_cap1=7800,
                                  _LayoutOption_cap1=[2, 3, 4, 5],
                                  _NumFigPair_cap1=50,

                                  _Array_cap1=1,  # number: 1xnumber
                                  _Cbot_Ctop_metalwidth_cap1=500,  # number
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

        ## SREF Generation Tr1Tr2Tr4
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A52_TIA_P1P2P4_Nbodyring_random._TIA_P1P2P4_Nbodyring_YCH._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr1_PMOSNumberofGate'] = _Tr1_PMOSNumberofGate
        _Caculation_Parameters['_Tr1_PMOSChannelWidth'] = _Tr1_PMOSChannelWidth
        _Caculation_Parameters['_Tr1_PMOSChannellength'] = _Tr1_PMOSChannellength
        _Caculation_Parameters['_Tr1_GateSpacing'] = _Tr1_PMOSGateSpacing
        _Caculation_Parameters['_Tr1_SDWidth'] = _Tr1_PMOSSDWidth
        _Caculation_Parameters['_Tr1_XVT'] = _Tr1_PMOSXVT
        _Caculation_Parameters['_Tr1_PCCrit'] = _Tr1_PMOSPCCrit
        _Caculation_Parameters['_Tr1_Source_Via_TF'] = _Tr1_PMOSSource_Via_TF
        _Caculation_Parameters['_Tr1_Drain_Via_TF'] = _Tr1_PMOSDrain_Via_TF
        _Caculation_Parameters['_Tr1_PMOSDummy'] = _Tr1_PMOSDummy
        _Caculation_Parameters['_Tr1_PMOSDummy_length'] = _Tr1_PMOSDummy_length
        _Caculation_Parameters['_Tr1_PMOSDummy_placement'] = _Tr1_PMOSDummy_placement

        _Caculation_Parameters['_Tr2_PMOSNumberofGate'] = _Tr2_PMOSNumberofGate
        _Caculation_Parameters['_Tr2_PMOSChannelWidth'] = _Tr2_PMOSChannelWidth
        _Caculation_Parameters['_Tr2_PMOSChannellength'] = _Tr2_PMOSChannellength
        _Caculation_Parameters['_Tr2_GateSpacing'] = _Tr2_PMOSGateSpacing
        _Caculation_Parameters['_Tr2_SDWidth'] = _Tr2_PMOSSDWidth
        _Caculation_Parameters['_Tr2_XVT'] = _Tr2_PMOSXVT
        _Caculation_Parameters['_Tr2_PCCrit'] = _Tr2_PMOSPCCrit
        _Caculation_Parameters['_Tr2_Source_Via_TF'] = _Tr2_PMOSSource_Via_TF
        _Caculation_Parameters['_Tr2_Drain_Via_TF'] = _Tr2_PMOSDrain_Via_TF
        _Caculation_Parameters['_Tr2_PMOSDummy'] = _Tr2_PMOSDummy
        _Caculation_Parameters['_Tr2_PMOSDummy_length'] = _Tr2_PMOSDummy_length
        _Caculation_Parameters['_Tr2_PMOSDummy_placement'] = _Tr2_PMOSDummy_placement

        _Caculation_Parameters['_Tr4_PMOSNumberofGate'] = _Tr4_PMOSNumberofGate
        _Caculation_Parameters['_Tr4_PMOSChannelWidth'] = _Tr4_PMOSChannelWidth
        _Caculation_Parameters['_Tr4_PMOSChannellength'] = _Tr4_PMOSChannellength
        _Caculation_Parameters['_Tr4_GateSpacing'] = _Tr4_PMOSGateSpacing
        _Caculation_Parameters['_Tr4_SDWidth'] = _Tr4_PMOSSDWidth
        _Caculation_Parameters['_Tr4_XVT'] = _Tr4_PMOSXVT
        _Caculation_Parameters['_Tr4_PCCrit'] = _Tr4_PMOSPCCrit
        _Caculation_Parameters['_Tr4_Source_Via_TF'] = _Tr4_PMOSSource_Via_TF
        _Caculation_Parameters['_Tr4_Drain_Via_TF'] = _Tr4_PMOSDrain_Via_TF
        _Caculation_Parameters['_Tr4_PMOSDummy'] = _Tr4_PMOSDummy
        _Caculation_Parameters['_Tr4_PMOSDummy_length'] = _Tr4_PMOSDummy_length
        _Caculation_Parameters['_Tr4_PMOSDummy_placement'] = _Tr4_PMOSDummy_placement

        _Caculation_Parameters['_NumContTop'] = _NumContTop_P1P2P4
        _Caculation_Parameters['_NumContBottom'] = _NumContBottom_P1P2P4
        _Caculation_Parameters['_NumContLeft'] = _NumContLeft_P1P2P4
        _Caculation_Parameters['_NumContRight'] = _NumContRight_P1P2P4

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Pmos_Tr1Tr2Tr4_Nbodyring'] = self._SrefElementDeclaration(
            _DesignObj=A52_TIA_P1P2P4_Nbodyring_random._TIA_P1P2P4_Nbodyring_YCH(_DesignParameter=None,_Name='{}:SRF_Pmos_Tr1Tr2Tr4_Nbodyring'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Pmos_Tr1Tr2Tr4_Nbodyring']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_Tr1Tr2Tr4_Nbodyring']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_Tr1Tr2Tr4_Nbodyring']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_Tr1Tr2Tr4_Nbodyring']['_XYCoordinates'] = [[0, 0]]


        ## SREF Generation Tr0Tr3
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A51_TIA_P0P3_random._TIA_P0P3_YCH._ParametersForDesignCalculation)

        _Caculation_Parameters['_Tr0_PMOSNumberofGate'] = _Tr0_PMOSNumberofGate
        _Caculation_Parameters['_Tr0_PMOSChannelWidth'] = _Tr0_PMOSChannelWidth
        _Caculation_Parameters['_Tr0_PMOSChannellength'] = _Tr0_PMOSChannellength
        _Caculation_Parameters['_Tr0_GateSpacing'] = _Tr0_PMOSGateSpacing
        _Caculation_Parameters['_Tr0_SDWidth'] = _Tr0_PMOSSDWidth
        _Caculation_Parameters['_Tr0_XVT'] = _Tr0_PMOSXVT
        _Caculation_Parameters['_Tr0_PCCrit'] = _Tr0_PMOSPCCrit
        _Caculation_Parameters['_Tr0_Source_Via_TF'] = _Tr0_PMOSSource_Via_TF
        _Caculation_Parameters['_Tr0_Drain_Via_TF'] = _Tr0_PMOSDrain_Via_TF
        _Caculation_Parameters['_Tr0_PMOSDummy'] = _Tr0_PMOSDummy
        _Caculation_Parameters['_Tr0_PMOSDummy_length'] = _Tr0_PMOSDummy_length
        _Caculation_Parameters['_Tr0_PMOSDummy_placement'] = _Tr0_PMOSDummy_placement

        _Caculation_Parameters['_Tr3_PMOSNumberofGate'] = _Tr3_PMOSNumberofGate
        _Caculation_Parameters['_Tr3_PMOSChannelWidth'] = _Tr3_PMOSChannelWidth
        _Caculation_Parameters['_Tr3_PMOSChannellength'] = _Tr3_PMOSChannellength
        _Caculation_Parameters['_Tr3_GateSpacing'] = _Tr3_PMOSGateSpacing
        _Caculation_Parameters['_Tr3_SDWidth'] = _Tr3_PMOSSDWidth
        _Caculation_Parameters['_Tr3_XVT'] = _Tr3_PMOSXVT
        _Caculation_Parameters['_Tr3_PCCrit'] = _Tr3_PMOSPCCrit
        _Caculation_Parameters['_Tr3_Source_Via_TF'] = _Tr3_PMOSSource_Via_TF
        _Caculation_Parameters['_Tr3_Drain_Via_TF'] = _Tr3_PMOSDrain_Via_TF
        _Caculation_Parameters['_Tr3_PMOSDummy'] = _Tr3_PMOSDummy
        _Caculation_Parameters['_Tr3_PMOSDummy_length'] = _Tr3_PMOSDummy_length
        _Caculation_Parameters['_Tr3_PMOSDummy_placement'] = _Tr3_PMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Pmos_Tr0Tr3'] = self._SrefElementDeclaration(
            _DesignObj=A51_TIA_P0P3_random._TIA_P0P3_YCH(_DesignParameter=None,_Name='{}:SRF_Pmos_Tr0Tr3'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Pmos_Tr0Tr3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_Tr0Tr3']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_Tr0Tr3']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_Tr0Tr3']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4_Nbodyring','SRF_Nbodyring','SRF_NbodyTop','SRF_NbodyContactPhyLen','BND_Met1Layer')
        target_coord = tmp1[0][0][0][0][0][0]['_XY_up']
        target_coord[1] = target_coord[1] + 500
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Pmos_Tr0Tr3','SRF_Pmos_Tr0','SRF_Pmos','BND_EGLayer')
        approaching_coord = tmp2[0][0][0][0][0]['_XY_down']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pmos_Tr0Tr3')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Pmos_Tr0Tr3']['_XYCoordinates'] = tmpXY

## ################################################################################################################### Nbodyring_top
        # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A50_TIA_NbodyContactPhyLen._NbodyContactPhyLen._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length'] = None
        _Caculation_Parameters['_NumCont'] = _NumContTop_P0P3
        _Caculation_Parameters['_Vtc_flag'] = False

        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr0Tr3', 'SRF_Pmos_Tr0', 'SRF_Pmos', 'BND_EGLayer')
        tmp2 = self.get_param_KJH4('SRF_Pmos_Tr0Tr3', 'SRF_Pmos_Tr3', 'SRF_Pmos', 'BND_EGLayer')

        target_coordx = tmp1[0][0][0][0][0]['_XY_right'][0]
        target_coordy = tmp2[0][0][0][0][0]['_XY_left'][0]
        target_length_x = target_coordx - target_coordy
        _Caculation_Parameters['_Length'] = target_length_x + 1000

        # Generate Sref
        self._DesignParameter['SRF_NbodyTop_P0P3'] = self._SrefElementDeclaration(
            _DesignObj=A50_TIA_NbodyContactPhyLen._NbodyContactPhyLen(_DesignParameter=None,_Name='{}:SRF_NbodyTop_P0P3'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_NbodyTop_P0P3']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_NbodyTop_P0P3']['_Angle'] = 0

        # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_NbodyTop_P0P3']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        # Define Sref _XYcoordinate
        self._DesignParameter['SRF_NbodyTop_P0P3']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr0Tr3','SRF_Pmos_Tr0','SRF_Pmos','BND_EGLayer')
        tmp2 = self.get_param_KJH4('SRF_Pmos_Tr0Tr3', 'SRF_Pmos_Tr3', 'SRF_Pmos', 'BND_EGLayer')
        target_coord = tmp1[0][0][0][0][0]['_XY_up']
        target_coord[0] = (tmp1[0][0][0][0][0]['_XY_right'][0] + tmp2[0][0][0][0][0]['_XY_left'][0])/2
        target_coord[1] = target_coord[1] + 500
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_NbodyTop_P0P3','SRF_NbodyContactPhyLen','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_NbodyTop_P0P3')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_NbodyTop_P0P3']['_XYCoordinates'] = tmpXY


## ################################################################################################################### Nbodyring_left
        # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A50_TIA_NbodyContactPhyLen._NbodyContactPhyLen._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length'] = None
        _Caculation_Parameters['_NumCont'] = _NumContLeft_P0P3
        _Caculation_Parameters['_Vtc_flag'] = True

        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr0Tr3', 'SRF_Pmos_Tr3', 'SRF_Pmos', 'BND_EGLayer')

        target_length_y = abs(tmp1[0][0][0][0][0]['_XY_up'][1]-tmp1[0][0][0][0][0]['_XY_down'][1])
        _Caculation_Parameters['_Length'] = target_length_y + 1000

        # Generate Sref
        self._DesignParameter['SRF_NbodyLeft_P0P3'] = self._SrefElementDeclaration(
            _DesignObj=A50_TIA_NbodyContactPhyLen._NbodyContactPhyLen(_DesignParameter=None,_Name='{}:SRF_NbodyLeft_P0P3'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_NbodyLeft_P0P3']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_NbodyLeft_P0P3']['_Angle'] = 0

        # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_NbodyLeft_P0P3']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        # Define Sref _XYcoordinate
        self._DesignParameter['SRF_NbodyLeft_P0P3']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr0Tr3', 'SRF_Pmos_Tr3', 'SRF_Pmos', 'BND_EGLayer')
        target_coord = tmp1[0][0][0][0][0]['_XY_left']
        target_coord[0] = target_coord[0] - 500
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_NbodyLeft_P0P3', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_NbodyLeft_P0P3')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_NbodyLeft_P0P3']['_XYCoordinates'] = tmpXY

## ################################################################################################################### Nbodyring_right
        # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy( A50_TIA_NbodyContactPhyLen._NbodyContactPhyLen._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length'] = None
        _Caculation_Parameters['_NumCont'] = _NumContRight_P0P3
        _Caculation_Parameters['_Vtc_flag'] = True

        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr0Tr3', 'SRF_Pmos_Tr0', 'SRF_Pmos', 'BND_EGLayer')

        target_length_y = abs(tmp1[0][0][0][0][0]['_XY_up'][1] - tmp1[0][0][0][0][0]['_XY_down'][1])
        _Caculation_Parameters['_Length'] = target_length_y + 1000

        # Generate Sref
        self._DesignParameter['SRF_NbodyRight_P0P3'] = self._SrefElementDeclaration(
            _DesignObj=A50_TIA_NbodyContactPhyLen._NbodyContactPhyLen(_DesignParameter=None,_Name='{}:SRF_NbodyRight_P0P3'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_NbodyRight_P0P3']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_NbodyRight_P0P3']['_Angle'] = 0

        # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_NbodyRight_P0P3']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        # Define Sref _XYcoordinate
        self._DesignParameter['SRF_NbodyRight_P0P3']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr0Tr3', 'SRF_Pmos_Tr0', 'SRF_Pmos', 'BND_EGLayer')
        target_coord = tmp1[0][0][0][0][0]['_XY_right']
        target_coord[0] = target_coord[0] + 500
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_NbodyRight_P0P3', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_NbodyRight_P0P3')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_NbodyRight_P0P3']['_XYCoordinates'] = tmpXY

## ################################################################################################################### Nbodyring_P0P3_top_extension

        # Define Boundary_element
        self._DesignParameter['BND_ExtenODLayer_Top_P0P3'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=
                                                                                            DesignParameters._LayerMapping['DIFF'][0],
                                                                                            _Datatype=
                                                                                            DesignParameters._LayerMapping['DIFF'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[],
        )


        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_NbodyTop_P0P3','SRF_NbodyContactPhyLen','BND_ODLayer')
        self._DesignParameter['BND_ExtenODLayer_Top_P0P3']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH4('SRF_NbodyLeft_P0P3','SRF_NbodyContactPhyLen','BND_ODLayer')
        tmp3 = self.get_param_KJH4('SRF_NbodyRight_P0P3','SRF_NbodyContactPhyLen','BND_ODLayer')
        self._DesignParameter['BND_ExtenODLayer_Top_P0P3']['_XWidth'] = abs( tmp3[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0] )

        #Define XYcoord.
        self._DesignParameter['BND_ExtenODLayer_Top_P0P3']['_XYCoordinates'] = [[0,0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_NbodyLeft_P0P3', 'SRF_NbodyContactPhyLen', 'BND_ODLayer')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ExtenODLayer_Top_P0P3')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_ExtenODLayer_Top_P0P3')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_ExtenODLayer_Top_P0P3']['_XYCoordinates'] = tmpXY


        # Define Boundary_element
        self._DesignParameter['BND_ExtenMet1Layer_Top_P0P3'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[],
        )


        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_NbodyTop_P0P3','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_ExtenMet1Layer_Top_P0P3']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH4('SRF_NbodyLeft_P0P3','SRF_NbodyContactPhyLen','BND_Met1Layer')
        tmp3 = self.get_param_KJH4('SRF_NbodyRight_P0P3','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_ExtenMet1Layer_Top_P0P3']['_XWidth'] = abs( tmp3[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0] )

        #Define XYcoord.
        self._DesignParameter['BND_ExtenMet1Layer_Top_P0P3']['_XYCoordinates'] = [[0,0]]

        # Calculate Sref XYcoord
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_NbodyLeft_P0P3', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ExtenMet1Layer_Top_P0P3')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_ExtenMet1Layer_Top_P0P3')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_ExtenMet1Layer_Top_P0P3']['_XYCoordinates'] = tmpXY

## ################################################################################################################### Nbodyring_P0P3_Nwell_extension
        self._DesignParameter['BND_Nwell_Extension_P0P3'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['NWELL'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_ExtenMet1Layer_Top_P0P3')
        tmp2 = self.get_param_KJH4('SRF_NbodyRight_P0P3', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Nwell_Extension_P0P3']['_YWidth'] = abs(tmp1[0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1]) + 112

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Nwell_Extension_P0P3']['_XWidth'] = abs(tmp1[0][0]['_XY_left'][0] - tmp2[0][0][0][0]['_XY_right'][0]) + 112

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Nwell_Extension_P0P3']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_ExtenMet1Layer_Top_P0P3')
        target_coord = tmp1[0][0]['_XY_up_left']
        target_coord[0] = target_coord[0] - 56
        target_coord[1] = target_coord[1] + 56
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Nwell_Extension_P0P3')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Nwell_Extension_P0P3')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Nwell_Extension_P0P3']['_XYCoordinates'] = tmpXY



        ## SREF Generation N2N3
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A51_TIA_N2N3_random._TIA_N2N3_YCH._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr2_NMOSNumberofGate'] = _Tr2_NMOSNumberofGate
        _Caculation_Parameters['_Tr2_NMOSChannelWidth'] = _Tr2_NMOSChannelWidth
        _Caculation_Parameters['_Tr2_NMOSChannellength'] = _Tr2_NMOSChannellength
        _Caculation_Parameters['_Tr2_GateSpacing'] = _Tr2_NMOSGateSpacing
        _Caculation_Parameters['_Tr2_SDWidth'] = _Tr2_NMOSSDWidth
        _Caculation_Parameters['_Tr2_XVT'] = _Tr2_NMOSXVT
        _Caculation_Parameters['_Tr2_PCCrit'] = _Tr2_NMOSPCCrit
        _Caculation_Parameters['_Tr2_Source_Via_TF'] = _Tr2_NMOSSource_Via_TF
        _Caculation_Parameters['_Tr2_Drain_Via_TF'] = _Tr2_NMOSDrain_Via_TF
        _Caculation_Parameters['_Tr2_NMOSDummy'] = _Tr2_NMOSDummy
        _Caculation_Parameters['_Tr2_NMOSDummy_length'] = _Tr2_NMOSDummy_length
        _Caculation_Parameters['_Tr2_NMOSDummy_placement'] = _Tr2_NMOSDummy_placement

        _Caculation_Parameters['_Tr3_NMOSNumberofGate'] = _Tr3_NMOSNumberofGate
        _Caculation_Parameters['_Tr3_NMOSChannelWidth'] = _Tr3_NMOSChannelWidth
        _Caculation_Parameters['_Tr3_NMOSChannellength'] = _Tr3_NMOSChannellength
        _Caculation_Parameters['_Tr3_GateSpacing'] = _Tr3_NMOSGateSpacing
        _Caculation_Parameters['_Tr3_SDWidth'] = _Tr3_NMOSSDWidth
        _Caculation_Parameters['_Tr3_XVT'] = _Tr3_NMOSXVT
        _Caculation_Parameters['_Tr3_PCCrit'] = _Tr3_NMOSPCCrit
        _Caculation_Parameters['_Tr3_Source_Via_TF'] = _Tr3_NMOSSource_Via_TF
        _Caculation_Parameters['_Tr3_Drain_Via_TF'] = _Tr3_NMOSDrain_Via_TF
        _Caculation_Parameters['_Tr3_NMOSDummy'] = _Tr3_NMOSDummy
        _Caculation_Parameters['_Tr3_NMOSDummy_length'] = _Tr3_NMOSDummy_length
        _Caculation_Parameters['_Tr3_NMOSDummy_placement'] = _Tr3_NMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Nmos_Tr2Tr3'] = self._SrefElementDeclaration(
            _DesignObj=A51_TIA_N2N3_random._TIA_N2N3_YCH(_DesignParameter=None, _Name='{}:SRF_Nmos_Tr2Tr3'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Nmos_Tr2Tr3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos_Tr2Tr3']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos_Tr2Tr3']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos_Tr2Tr3']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_NbodyLeft_P0P3', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_left']
        target_coord[0] = target_coord[0] - 500
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Nmos_Tr2Tr3', 'SRF_Nmos_Tr3', 'SRF_Nmos', 'BND_EGLayer')
        approaching_coord = tmp2[0][0][0][0][0]['_XY_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Nmos_Tr2Tr3')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Nmos_Tr2Tr3']['_XYCoordinates'] = tmpXY

## ################################################################################################################### Pbodyring
        ## SREF Generation Pbodyring
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A50_TIA_Pbodyring._PbodyRing._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_XlengthIntn'] = None
        _Caculation_Parameters['_YlengthIntn'] = None
        _Caculation_Parameters['_NumContTop'] = _NumContTop_Pbody
        _Caculation_Parameters['_NumContBottom'] = _NumContBottom_Pbody
        _Caculation_Parameters['_NumContLeft'] = _NumContLeft_Pbody
        _Caculation_Parameters['_NumContRight'] = _NumContRight_Pbody

        tmp1 = self.get_param_KJH4('SRF_NbodyTop_P0P3','SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4_Nbodyring', 'SRF_Nbodyring', 'SRF_NbodyBottom', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        tmp3 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4_Nbodyring', 'SRF_Nbodyring', 'SRF_NbodyLeft', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        tmp4 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4_Nbodyring', 'SRF_Nbodyring', 'SRF_NbodyRight', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')

        _Caculation_Parameters['_XlengthIntn'] = abs(tmp4[0][0][0][0][0][0]['_XY_right'][0]-tmp3[0][0][0][0][0][0]['_XY_left'][0]) + 400
        _Caculation_Parameters['_YlengthIntn'] = abs(tmp1[0][0][0][0]['_XY_up'][1]-tmp2[0][0][0][0][0][0]['_XY_down'][1]) + 400

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Pbodyring'] = self._SrefElementDeclaration(
            _DesignObj=A50_TIA_Pbodyring._PbodyRing(_DesignParameter=None, _Name='{}:SRF_Pbodyring'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Pbodyring']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbodyring']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbodyring']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbodyring']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4_Nbodyring', 'SRF_Nbodyring', 'SRF_NbodyBottom', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        target_coord = tmp1[0][0][0][0][0][0]['_XY_down']
        target_coord[1] = target_coord[1] - 200
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Pbodyring', 'SRF_PbodyBottom', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0][0]['_XY_up']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pbodyring')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['SRF_Pbodyring']['_XYCoordinates'] = tmpXY

        ## SREF Generation NMOS Tr0Tr2Tr4
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A51_TIA_N0N1N4_random._TIA_N0N1N4_YCH._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr0_NMOSNumberofGate'] = _Tr0_NMOSNumberofGate
        _Caculation_Parameters['_Tr0_NMOSChannelWidth'] = _Tr0_NMOSChannelWidth
        _Caculation_Parameters['_Tr0_NMOSChannellength'] = _Tr0_NMOSChannellength
        _Caculation_Parameters['_Tr0_GateSpacing'] = _Tr0_NMOSGateSpacing
        _Caculation_Parameters['_Tr0_SDWidth'] = _Tr0_NMOSSDWidth
        _Caculation_Parameters['_Tr0_XVT'] = _Tr0_NMOSXVT
        _Caculation_Parameters['_Tr0_PCCrit'] = _Tr0_NMOSPCCrit
        _Caculation_Parameters['_Tr0_Source_Via_TF'] = _Tr0_NMOSSource_Via_TF
        _Caculation_Parameters['_Tr0_Drain_Via_TF'] = _Tr0_NMOSDrain_Via_TF
        _Caculation_Parameters['_Tr0_NMOSDummy'] = _Tr0_NMOSDummy
        _Caculation_Parameters['_Tr0_NMOSDummy_length'] = _Tr0_NMOSDummy_length
        _Caculation_Parameters['_Tr0_NMOSDummy_placement'] = _Tr0_NMOSDummy_placement

        _Caculation_Parameters['_Tr1_NMOSNumberofGate'] = _Tr1_NMOSNumberofGate
        _Caculation_Parameters['_Tr1_NMOSChannelWidth'] = _Tr1_NMOSChannelWidth
        _Caculation_Parameters['_Tr1_NMOSChannellength'] = _Tr1_NMOSChannellength
        _Caculation_Parameters['_Tr1_GateSpacing'] = _Tr1_NMOSGateSpacing
        _Caculation_Parameters['_Tr1_SDWidth'] = _Tr1_NMOSSDWidth
        _Caculation_Parameters['_Tr1_XVT'] = _Tr1_NMOSXVT
        _Caculation_Parameters['_Tr1_PCCrit'] = _Tr1_NMOSPCCrit
        _Caculation_Parameters['_Tr1_Source_Via_TF'] = _Tr1_NMOSSource_Via_TF
        _Caculation_Parameters['_Tr1_Drain_Via_TF'] = _Tr1_NMOSDrain_Via_TF
        _Caculation_Parameters['_Tr1_NMOSDummy'] = _Tr1_NMOSDummy
        _Caculation_Parameters['_Tr1_NMOSDummy_length'] = _Tr1_NMOSDummy_length
        _Caculation_Parameters['_Tr1_NMOSDummy_placement'] = _Tr1_NMOSDummy_placement

        _Caculation_Parameters['_Tr4_NMOSNumberofGate'] = _Tr4_NMOSNumberofGate
        _Caculation_Parameters['_Tr4_NMOSChannelWidth'] = _Tr4_NMOSChannelWidth
        _Caculation_Parameters['_Tr4_NMOSChannellength'] = _Tr4_NMOSChannellength
        _Caculation_Parameters['_Tr4_GateSpacing'] = _Tr4_NMOSGateSpacing
        _Caculation_Parameters['_Tr4_SDWidth'] = _Tr4_NMOSSDWidth
        _Caculation_Parameters['_Tr4_XVT'] = _Tr4_NMOSXVT
        _Caculation_Parameters['_Tr4_PCCrit'] = _Tr4_NMOSPCCrit
        _Caculation_Parameters['_Tr4_Source_Via_TF'] = _Tr4_NMOSSource_Via_TF
        _Caculation_Parameters['_Tr4_Drain_Via_TF'] = _Tr4_NMOSDrain_Via_TF
        _Caculation_Parameters['_Tr4_NMOSDummy'] = _Tr4_NMOSDummy
        _Caculation_Parameters['_Tr4_NMOSDummy_length'] = _Tr4_NMOSDummy_length
        _Caculation_Parameters['_Tr4_NMOSDummy_placement'] = _Tr4_NMOSDummy_placement


        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Nmos_Tr0Tr1Tr4'] = self._SrefElementDeclaration(
            _DesignObj=A51_TIA_N0N1N4_random._TIA_N0N1N4_YCH(_DesignParameter=None, _Name='{}:SRF_Nmos_Tr0Tr1Tr4'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Nmos_Tr0Tr1Tr4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos_Tr0Tr1Tr4']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos_Tr0Tr1Tr4']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos_Tr0Tr1Tr4']['_XYCoordinates'] = [[0, 0]]


        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Pbodyring','SRF_PbodyBottom','SRF_PbodyContactPhyLen','BND_Met1Layer')
        target_coord = tmp1[0][0][0][0][0]['_XY_down']
        target_coord[1] = target_coord[1] - 500
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4','SRF_Nmos_Tr4', 'SRF_Nmos', 'BND_EGLayer')
        approaching_coord = tmp2[0][0][0][0][0]['_XY_up']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Nmos_Tr0Tr1Tr4']['_XYCoordinates'] = tmpXY

## ################################################################################################################### Pbody_Left_N0N1N4
        # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(
            A50_TIA_PbodyContactPhyLen._PbodyContactPhyLen._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length'] = None
        _Caculation_Parameters['_NumCont'] = _NumContBottom_Pbody
        _Caculation_Parameters['_Vtc_flag'] = True

        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4','SRF_Nmos_Tr0', 'SRF_Nmos', 'BND_EGLayer')

        target_length_y = abs(tmp1[0][0][0][0][0]['_XY_up'][1] - tmp1[0][0][0][0][0]['_XY_down'][1])
        _Caculation_Parameters['_Length'] = target_length_y + 1000

        # Generate Sref
        self._DesignParameter['SRF_PbodyLeft_N0N1N4'] = self._SrefElementDeclaration(
            _DesignObj=A50_TIA_PbodyContactPhyLen._PbodyContactPhyLen(_DesignParameter=None, _Name='{}:SRF_PbodyLeft_N0N1N4'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_PbodyLeft_N0N1N4']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_PbodyLeft_N0N1N4']['_Angle'] = 0

        # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_PbodyLeft_N0N1N4']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        # Define Sref _XYcoordinate
        self._DesignParameter['SRF_PbodyLeft_N0N1N4']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4','SRF_Nmos_Tr0', 'SRF_Nmos', 'BND_EGLayer')
        target_coord = tmp1[0][0][0][0][0]['_XY_left']
        target_coord[0] = target_coord[0] - 500
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_PbodyLeft_N0N1N4','SRF_PbodyContactPhyLen','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_PbodyLeft_N0N1N4')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_PbodyLeft_N0N1N4']['_XYCoordinates'] = tmpXY

## ################################################################################################################### Pbody_Right_N0N1N4
        # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(
            A50_TIA_PbodyContactPhyLen._PbodyContactPhyLen._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length'] = None
        _Caculation_Parameters['_NumCont'] = _NumContBottom_Pbody
        _Caculation_Parameters['_Vtc_flag'] = True

        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4', 'SRF_Nmos_Tr0', 'SRF_Nmos', 'BND_EGLayer')

        target_length_y = abs(tmp1[0][0][0][0][0]['_XY_up'][1] - tmp1[0][0][0][0][0]['_XY_down'][1])
        _Caculation_Parameters['_Length'] = target_length_y + 1000

        # Generate Sref
        self._DesignParameter['SRF_PbodyRight_N0N1N4'] = self._SrefElementDeclaration(
            _DesignObj=A50_TIA_PbodyContactPhyLen._PbodyContactPhyLen(_DesignParameter=None,
                                                                      _Name='{}:SRF_PbodyRight_N0N1N4'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_PbodyRight_N0N1N4']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_PbodyRight_N0N1N4']['_Angle'] = 0

        # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_PbodyRight_N0N1N4']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        # Define Sref _XYcoordinate
        self._DesignParameter['SRF_PbodyRight_N0N1N4']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4', 'SRF_Nmos_Tr1', 'SRF_Nmos', 'BND_EGLayer')
        target_coord = tmp1[0][0][0][0][0]['_XY_right']
        target_coord[0] = target_coord[0] + 500
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_PbodyRight_N0N1N4', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_PbodyRight_N0N1N4')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_PbodyRight_N0N1N4']['_XYCoordinates'] = tmpXY

        # ################################################################################################################### resistor0

        ## SREF Generation Resistor0
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A50_opppcres_b._Opppcres_b_YCH._ParametersForDesignCalculation)
        _Caculation_Parameters['_ResWidth'] = _ResWidth_res0
        _Caculation_Parameters['_ResLength'] = _ResLength_res0
        _Caculation_Parameters['_CONUMX'] = _CONUMX_res0
        _Caculation_Parameters['_CONUMY'] = _CONUMY_res0
        _Caculation_Parameters['_SeriesStripes'] = _SeriesStripes_res0
        _Caculation_Parameters['_ParallelStripes'] = _ParallelStripes_res0

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Res0'] = self._SrefElementDeclaration(
            _DesignObj=A50_opppcres_b._Opppcres_b_YCH(_DesignParameter=None, _Name='{}:SRF_Res0'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Res0']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Res0']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Res0']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Res0']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_PbodyLeft_N0N1N4', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_left']
        target_coord[0] = target_coord[0] - 600
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Res0', '_POLayer')
        approaching_coord = tmp2[0][-1][0]['_XY_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Res0')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Res0']['_XYCoordinates'] = tmpXY

## ################################################################################################################### resistor1

        ## SREF Generation Resistor1
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A50_opppcres_b._Opppcres_b_YCH._ParametersForDesignCalculation)
        _Caculation_Parameters['_ResWidth'] = _ResWidth_res1
        _Caculation_Parameters['_ResLength'] = _ResLength_res1
        _Caculation_Parameters['_CONUMX'] = _CONUMX_res1
        _Caculation_Parameters['_CONUMY'] = _CONUMY_res1
        _Caculation_Parameters['_SeriesStripes'] = _SeriesStripes_res1
        _Caculation_Parameters['_ParallelStripes'] = _ParallelStripes_res1

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Res1'] = self._SrefElementDeclaration(
            _DesignObj=A50_opppcres_b._Opppcres_b_YCH(_DesignParameter=None, _Name='{}:SRF_Res1'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Res1']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Res1']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Res1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Res1']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_PbodyRight_N0N1N4', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_right']
        target_coord[0] = target_coord[0] + 600
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Res1', '_POLayer')
        approaching_coord = tmp2[0][0][0]['_XY_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Res1')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Res1']['_XYCoordinates'] = tmpXY

## ################################################################################################################### Pbody_Left_res0

        # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(
            A50_TIA_PbodyContactPhyLen._PbodyContactPhyLen._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length'] = None
        _Caculation_Parameters['_NumCont'] = _NumContBottom_Pbody
        _Caculation_Parameters['_Vtc_flag'] = True

        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4', 'SRF_Nmos_Tr0', 'SRF_Nmos', 'BND_EGLayer')
        tmp2 = self.get_param_KJH4('SRF_Res0', '_POLayer')

        target_length_y = abs(tmp1[0][0][0][0][0]['_XY_up'][1] - tmp1[0][0][0][0][0]['_XY_down'][1])
        _Caculation_Parameters['_Length'] = target_length_y + 1000

        # Generate Sref
        self._DesignParameter['SRF_PbodyLeft_res0'] = self._SrefElementDeclaration(
            _DesignObj=A50_TIA_PbodyContactPhyLen._PbodyContactPhyLen(_DesignParameter=None, _Name='{}:SRF_PbodyLeft_res0'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_PbodyLeft_res0']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_PbodyLeft_res0']['_Angle'] = 0

        # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_PbodyLeft_res0']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        # Define Sref _XYcoordinate
        self._DesignParameter['SRF_PbodyLeft_res0']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Res0', '_POLayer')
        target_coord = tmp1[0][0][0]['_XY_left']
        target_coord[0] = target_coord[0] - 600
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_PbodyLeft_res0','SRF_PbodyContactPhyLen','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_PbodyLeft_res0')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_PbodyLeft_res0']['_XYCoordinates'] = tmpXY



## ################################################################################################################### Pbody_Right_res1
        # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(
            A50_TIA_PbodyContactPhyLen._PbodyContactPhyLen._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length'] = None
        _Caculation_Parameters['_NumCont'] = _NumContBottom_Pbody
        _Caculation_Parameters['_Vtc_flag'] = True

        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4', 'SRF_Nmos_Tr1', 'SRF_Nmos', 'BND_EGLayer')
        tmp2 = self.get_param_KJH4('SRF_Res1', '_POLayer')

        target_length_y = abs(tmp1[0][0][0][0][0]['_XY_up'][1] - tmp1[0][0][0][0][0]['_XY_down'][1])
        _Caculation_Parameters['_Length'] = target_length_y + 1000

        # Generate Sref
        self._DesignParameter['SRF_PbodyRight_res1'] = self._SrefElementDeclaration(
            _DesignObj=A50_TIA_PbodyContactPhyLen._PbodyContactPhyLen(_DesignParameter=None,_Name='{}:SRF_PbodyRight_res1'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_PbodyRight_res1']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_PbodyRight_res1']['_Angle'] = 0

        # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_PbodyRight_res1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        # Define Sref _XYcoordinate
        self._DesignParameter['SRF_PbodyRight_res1']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Res1', '_POLayer')
        target_coord = tmp1[0][-1][0]['_XY_right']
        target_coord[0] = target_coord[0] + 600
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_PbodyRight_res1', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_PbodyRight_res1')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_PbodyRight_res1']['_XYCoordinates'] = tmpXY

## ################################################################################################################### HDVNCAP_2(C0C1)
        # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A51_HDVNCAP_2._HDVNCAP_2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length_cap0'] = _Length_cap0
        _Caculation_Parameters['_LayoutOption_cap0'] = _LayoutOption_cap0
        _Caculation_Parameters['_NumFigPair_cap0'] = _NumFigPair_cap0
        _Caculation_Parameters['_Array_cap0'] = _Array_cap0
        _Caculation_Parameters['_Cbot_Ctop_metalwidth_cap0'] = _Cbot_Ctop_metalwidth_cap0

        _Caculation_Parameters['_Length_cap1'] = _Length_cap1
        _Caculation_Parameters['_LayoutOption_cap1'] = _LayoutOption_cap1
        _Caculation_Parameters['_NumFigPair_cap1'] = _NumFigPair_cap1
        _Caculation_Parameters['_Array_cap1'] = _Array_cap1
        _Caculation_Parameters['_Cbot_Ctop_metalwidth_cap1'] = _Cbot_Ctop_metalwidth_cap1


        # Generate Sref
        self._DesignParameter['SRF_cap0cap1'] = self._SrefElementDeclaration(
            _DesignObj=A51_HDVNCAP_2._HDVNCAP_2(_DesignParameter=None, _Name='{}:SRF_cap0cap1'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_cap0cap1']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_cap0cap1']['_Angle'] = 0

        # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_cap0cap1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        # Define Sref _XYcoordinate
        self._DesignParameter['SRF_cap0cap1']['_XYCoordinates'] = [[0, 0]]


        tmpXY = []
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4_Nbodyring','SRF_Pmos_Tr1Tr2Tr4','SRF_Pmos_Tr4', 'SRF_Pmos', 'BND_EGLayer')
        tmp2 = self.get_param_KJH4('SRF_PbodyLeft_res0','SRF_PbodyContactPhyLen','BND_Met1Layer')
        target_coord[0] = tmp1[0][0][0][0][0][0]['_XY_cent'][0]
        target_coord[1] = tmp2[0][0][0][0]['_XY_down'][1]
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_cap0cap1','BND_Met1Layer_Extension')
        approaching_coord = tmp2[0][0][0]['_XY_up']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_cap0cap1')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)

        tmpXY.append(New_Scoord)

        self._DesignParameter['SRF_cap0cap1']['_XYCoordinates'] = tmpXY


        # Routing

        ## ################################################################################################################### NMOS0 source routing
        # Define Boundary_element
        self._DesignParameter['BND_Metal1Layer_Connect_N0toRing_Source'] = self._BoundaryElementDeclaration(
                                                                                                        _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                        _XWidth=None,
                                                                                                        _YWidth=None,
                                                                                                        _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4', 'SRF_Nmos_Tr0', 'SRF_Nmos', 'BND_Met1Layer_Source')
        tmp2 = self.get_param_KJH4('SRF_cap0cap1','BND_Met1Layer_Extension')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal1Layer_Connect_N0toRing_Source']['_YWidth'] = abs(tmp1[0][0][0][0][0]['_XY_cent'][1] - tmp2[0][0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal1Layer_Connect_N0toRing_Source']['_XWidth'] = tmp1[0][0][0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal1Layer_Connect_N0toRing_Source']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        for i in range(0, int(_Tr0_NMOSNumberofGate / 2) + 1):
            # Calculate
            # Target_coord
            tmp1 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4', 'SRF_Nmos_Tr0', 'SRF_Nmos', 'BND_Met1Layer_Source')
            target_coord = tmp1[0][0][0][i][0]['_XY_cent']
            # Approaching_coord
            tmp2 = self.get_param_KJH4('BND_Metal1Layer_Connect_N0toRing_Source')
            approaching_coord = tmp2[0][0]['_XY_up']
            # Sref coord
            tmp3 = self.get_param_KJH4('BND_Metal1Layer_Connect_N0toRing_Source')
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            # Define
            self._DesignParameter['BND_Metal1Layer_Connect_N0toRing_Source']['_XYCoordinates'] = tmpXY


                ## ################################################################################################################### NMOS1 source routing
        # Define Boundary_element
        self._DesignParameter['BND_Metal1Layer_Connect_N1toRing_Source'] = self._BoundaryElementDeclaration(
                                                                                                    _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                    _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                    _XWidth=None,
                                                                                                    _YWidth=None,
                                                                                                    _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4', 'SRF_Nmos_Tr1', 'SRF_Nmos', 'BND_Met1Layer_Source')
        tmp2 = self.get_param_KJH4('SRF_cap0cap1', 'BND_Met1Layer_Extension')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal1Layer_Connect_N1toRing_Source']['_YWidth'] = abs(
            tmp1[0][0][0][0][0]['_XY_cent'][1] - tmp2[0][0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal1Layer_Connect_N1toRing_Source']['_XWidth'] = tmp1[0][0][0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal1Layer_Connect_N1toRing_Source']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        for i in range(0, int(_Tr1_NMOSNumberofGate / 2) + 1):
            # Calculate
            # Target_coord
            tmp1 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4', 'SRF_Nmos_Tr1', 'SRF_Nmos', 'BND_Met1Layer_Source')
            target_coord = tmp1[0][0][0][i][0]['_XY_cent']
            # Approaching_coord
            tmp2 = self.get_param_KJH4('BND_Metal1Layer_Connect_N1toRing_Source')
            approaching_coord = tmp2[0][0]['_XY_up']
            # Sref coord
            tmp3 = self.get_param_KJH4('BND_Metal1Layer_Connect_N1toRing_Source')
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            # Define
            self._DesignParameter['BND_Metal1Layer_Connect_N1toRing_Source']['_XYCoordinates'] = tmpXY


        ## ################################################################################################################### NMOS4 source routing
        # Define Boundary_element
        self._DesignParameter['BND_Metal1Layer_Connect_N4toRing_Source'] = self._BoundaryElementDeclaration(
                                                                                                    _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                    _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                    _XWidth=None,
                                                                                                    _YWidth=None,
                                                                                                    _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4', 'SRF_Nmos_Tr4', 'SRF_Nmos', 'BND_Met1Layer_Source')
        tmp2 = self.get_param_KJH4('SRF_cap0cap1', 'BND_Met1Layer_Extension')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal1Layer_Connect_N4toRing_Source']['_YWidth'] = abs(
            tmp1[0][0][0][0][0]['_XY_cent'][1] - tmp2[0][0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal1Layer_Connect_N4toRing_Source']['_XWidth'] = tmp1[0][0][0][0][0][
            '_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal1Layer_Connect_N4toRing_Source']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        for i in range(0, int(_Tr4_NMOSNumberofGate / 2) + 1):
            # Calculate
            # Target_coord
            tmp1 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4', 'SRF_Nmos_Tr4', 'SRF_Nmos', 'BND_Met1Layer_Source')
            target_coord = tmp1[0][0][0][i][0]['_XY_cent']
            # Approaching_coord
            tmp2 = self.get_param_KJH4('BND_Metal1Layer_Connect_N4toRing_Source')
            approaching_coord = tmp2[0][0]['_XY_up']
            # Sref coord
            tmp3 = self.get_param_KJH4('BND_Metal1Layer_Connect_N4toRing_Source')
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            # Define
            self._DesignParameter['BND_Metal1Layer_Connect_N4toRing_Source']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### PMOS0 source routing
        # Define Boundary_element
        self._DesignParameter['BND_Metal1Layer_Connect_P0toRing_Source'] = self._BoundaryElementDeclaration(
                                                                                                        _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                        _XWidth=None,
                                                                                                        _YWidth=None,
                                                                                                        _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr0Tr3','SRF_Pmos_Tr0','SRF_Pmos', 'BND_Met1Layer_Source')
        tmp2 = self.get_param_KJH4('SRF_NbodyTop_P0P3','SRF_NbodyContactPhyLen','BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal1Layer_Connect_P0toRing_Source']['_YWidth'] = abs(
            tmp1[0][0][0][0][0]['_XY_cent'][1] - tmp2[0][0][0][0]['_XY_up'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal1Layer_Connect_P0toRing_Source']['_XWidth'] = tmp1[0][0][0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal1Layer_Connect_P0toRing_Source']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        for i in range(0, int(_Tr0_PMOSNumberofGate / 2) + 1):
            # Calculate
            # Target_coord
            tmp1 = self.get_param_KJH4('SRF_Pmos_Tr0Tr3','SRF_Pmos_Tr0','SRF_Pmos', 'BND_Met1Layer_Source')
            target_coord = tmp1[0][0][0][i][0]['_XY_cent']
            # Approaching_coord
            tmp2 = self.get_param_KJH4('BND_Metal1Layer_Connect_P0toRing_Source')
            approaching_coord = tmp2[0][0]['_XY_down']
            # Sref coord
            tmp3 = self.get_param_KJH4('BND_Metal1Layer_Connect_P0toRing_Source')
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            # Define
            self._DesignParameter['BND_Metal1Layer_Connect_P0toRing_Source']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### PMOS3 source routing
        # Define Boundary_element
        self._DesignParameter['BND_Metal1Layer_Connect_P3toRing_Source'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr0Tr3', 'SRF_Pmos_Tr3', 'SRF_Pmos', 'BND_Met1Layer_Source')
        tmp2 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4_Nbodyring','SRF_Nbodyring','SRF_NbodyTop','SRF_NbodyContactPhyLen','BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal1Layer_Connect_P3toRing_Source']['_YWidth'] = abs(tmp1[0][0][0][0][0]['_XY_cent'][1] - tmp2[0][0][0][0][0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal1Layer_Connect_P3toRing_Source']['_XWidth'] = tmp1[0][0][0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal1Layer_Connect_P3toRing_Source']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        for i in range(0, int(_Tr3_PMOSNumberofGate / 2) + 1):
            # Calculate
            # Target_coord
            tmp1 = self.get_param_KJH4('SRF_Pmos_Tr0Tr3', 'SRF_Pmos_Tr3', 'SRF_Pmos', 'BND_Met1Layer_Source')
            target_coord = tmp1[0][0][0][i][0]['_XY_cent']
            # Approaching_coord
            tmp2 = self.get_param_KJH4('BND_Metal1Layer_Connect_P3toRing_Source')
            approaching_coord = tmp2[0][0]['_XY_up']
            # Sref coord
            tmp3 = self.get_param_KJH4('BND_Metal1Layer_Connect_P3toRing_Source')
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            # Define
            self._DesignParameter['BND_Metal1Layer_Connect_P3toRing_Source']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### NMOS2 source routing
        # Define Boundary_element
        self._DesignParameter['BND_Metal1Layer_Connect_N2toRing_Source'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr2Tr3', 'SRF_Nmos_Tr2', 'SRF_Nmos', 'BND_Met1Layer_Source')
        tmp2 = self.get_param_KJH4('SRF_Pbodyring', 'SRF_PbodyTop', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal1Layer_Connect_N2toRing_Source']['_YWidth'] = abs(tmp1[0][0][0][0][0]['_XY_cent'][1] - tmp2[0][0][0][0][0]['_XY_up'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal1Layer_Connect_N2toRing_Source']['_XWidth'] = tmp1[0][0][0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal1Layer_Connect_N2toRing_Source']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        for i in range(0, int(_Tr2_NMOSNumberofGate / 2) + 1):
            # Calculate
            # Target_coord
            tmp1 = self.get_param_KJH4('SRF_Nmos_Tr2Tr3', 'SRF_Nmos_Tr2', 'SRF_Nmos', 'BND_Met1Layer_Source')
            target_coord = tmp1[0][0][0][i][0]['_XY_cent']
            # Approaching_coord
            tmp2 = self.get_param_KJH4('BND_Metal1Layer_Connect_N2toRing_Source')
            approaching_coord = tmp2[0][0]['_XY_down']
            # Sref coord
            tmp3 = self.get_param_KJH4('BND_Metal1Layer_Connect_N2toRing_Source')
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            # Define
            self._DesignParameter['BND_Metal1Layer_Connect_N2toRing_Source']['_XYCoordinates'] = tmpXY

        # 12/30 clear
        ## ################################################################################################################### NMOS0, NMOS1 gate routing
        ## ################################################################################################################### NMOS0 gate Metal1
        # Define Boundary_element
        self._DesignParameter['BND_Metal1Layer_Connect_N0_Gate'] = self._BoundaryElementDeclaration(
                                                                                                        _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                        _XWidth=None,
                                                                                                        _YWidth=None,
                                                                                                        _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4', 'SRF_Nmos_Tr0', 'BND_POLayer_Hrz_Gate')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal1Layer_Connect_N0_Gate']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal1Layer_Connect_N0_Gate']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal1Layer_Connect_N0_Gate']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4', 'SRF_Nmos_Tr0', 'BND_POLayer_Hrz_Gate')
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal1Layer_Connect_N0_Gate')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal1Layer_Connect_N0_Gate')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal1Layer_Connect_N0_Gate']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### NMOS0 gate Metal1-Poly CA
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 0
        _Caculation_Parameters['_Layer2'] = 1
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_NMOS0_Gate_ViaM0M1'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,_Name='{}:SRF_NMOS0_Gate_ViaM0M1'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_NMOS0_Gate_ViaM0M1']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_NMOS0_Gate_ViaM0M1']['_Angle'] = 0

        # Calculate _COY
        _Caculation_Parameters['_COY'] = 1

        # Calculate _COX
        # Calculate Number of V1
        tmp = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4', 'SRF_Nmos_Tr0', 'BND_POLayer_Hrz_Gate')
        M1_Xwidth = tmp[0][0][0][0]['_Xwidth']
        Num_V1 = int((M1_Xwidth - 2 * 4) / (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 0
        # Define Num of V1
        if Num_V1 < 2:
            _Caculation_Parameters['_COX'] = 2
        else:
            _Caculation_Parameters['_COX'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_NMOS0_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_NMOS0_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]

        # For num of M1 in Nmos

        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4', 'SRF_Nmos_Tr0', 'BND_POLayer_Hrz_Gate')
        target_coord = tmp1[0][0][0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_NMOS0_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_POLayer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_NMOS0_Gate_ViaM0M1')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['SRF_NMOS0_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### NMOS0 gate Metal1 extension
        # Define Boundary_element
        self._DesignParameter['BND_Metal1Layer_Connect_N0_Gate_extension'] = self._BoundaryElementDeclaration(
                                                                                                            _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                            _XWidth=None,
                                                                                                            _YWidth=None,
                                                                                                            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Metal1Layer_Connect_N0_Gate')
        tmp2 = self.get_param_KJH4('SRF_NMOS0_Gate_ViaM0M1','SRF_ViaM0M1','BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal1Layer_Connect_N0_Gate_extension']['_YWidth'] = tmp2[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal1Layer_Connect_N0_Gate_extension']['_XWidth'] = tmp1[0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal1Layer_Connect_N0_Gate_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_NMOS0_Gate_ViaM0M1','SRF_ViaM0M1','BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal1Layer_Connect_N0_Gate_extension')
        approaching_coord = tmp2[0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal1Layer_Connect_N0_Gate_extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal1Layer_Connect_N0_Gate_extension']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### NMOS0 gate Metal2
        # Define Boundary_element
        self._DesignParameter['BND_Metal2Layer_Connect_N0_Gate'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Metal1Layer_Connect_N0_Gate')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal2Layer_Connect_N0_Gate']['_YWidth'] = tmp1[0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal2Layer_Connect_N0_Gate']['_XWidth'] = tmp1[0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal2Layer_Connect_N0_Gate']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal1Layer_Connect_N0_Gate')
        target_coord = tmp1[0][0]['_XY_down_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal2Layer_Connect_N0_Gate')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal2Layer_Connect_N0_Gate')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal2Layer_Connect_N0_Gate']['_XYCoordinates'] = tmpXY

# 12/30 clear
        ## ################################################################################################################### NMOS0 gate Metal3
        # Define Boundary_element
        self._DesignParameter['BND_Metal3Layer_Connect_N0_Gate'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Metal1Layer_Connect_N0_Gate')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal3Layer_Connect_N0_Gate']['_YWidth'] = tmp1[0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal3Layer_Connect_N0_Gate']['_XWidth'] = tmp1[0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal3Layer_Connect_N0_Gate']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal1Layer_Connect_N0_Gate')
        target_coord = tmp1[0][0]['_XY_down_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal3Layer_Connect_N0_Gate')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal3Layer_Connect_N0_Gate')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal3Layer_Connect_N0_Gate']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### NMOS0_Gate_ViaM1M3
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Nmos0_Gate_ViaM1M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,_Name='{}:SRF_Nmos0_Gate_ViaM1M3'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Nmos0_Gate_ViaM1M3']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Nmos0_Gate_ViaM1M3']['_Angle'] = 0

        # Calcuate _COY
        _Caculation_Parameters['_COY'] = 1

        # Calcuate _COX
        tmp = self.get_param_KJH4('BND_Metal3Layer_Connect_N0_Gate')
        M3_xwidth = tmp[0][0]['_Xwidth']
        Num_V1 = int((M3_xwidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COX'] = 2
        else:
            _Caculation_Parameters['_COX'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Nmos0_Gate_ViaM1M3']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Nmos0_Gate_ViaM1M3']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal3Layer_Connect_N0_Gate')
        target_coord = tmp1[0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Nmos0_Gate_ViaM1M3','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Nmos0_Gate_ViaM1M3')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Nmos0_Gate_ViaM1M3']['_XYCoordinates'] = tmpXY


        ## ################################################################################################################### NMOS1 gate Metal1
        # Define Boundary_element
        self._DesignParameter['BND_Metal1Layer_Connect_N1_Gate'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4', 'SRF_Nmos_Tr1', 'BND_POLayer_Hrz_Gate')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal1Layer_Connect_N1_Gate']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal1Layer_Connect_N1_Gate']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal1Layer_Connect_N1_Gate']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4', 'SRF_Nmos_Tr1', 'BND_POLayer_Hrz_Gate')
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal1Layer_Connect_N1_Gate')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal1Layer_Connect_N1_Gate')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal1Layer_Connect_N1_Gate']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### NMOS1 gate Metal1-Poly CA
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 0
        _Caculation_Parameters['_Layer2'] = 1
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_NMOS1_Gate_ViaM0M1'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_NMOS1_Gate_ViaM0M1'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_NMOS1_Gate_ViaM0M1']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_NMOS1_Gate_ViaM0M1']['_Angle'] = 0

        # Calculate _COY
        _Caculation_Parameters['_COY'] = 1

        # Calculate _COX
        # Calculate Number of V1
        tmp = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4', 'SRF_Nmos_Tr1', 'BND_POLayer_Hrz_Gate')
        M1_Xwidth = tmp[0][0][0][0]['_Xwidth']
        Num_V1 = int((M1_Xwidth - 2 * 4) / (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 0
        # Define Num of V1
        if Num_V1 < 2:
            _Caculation_Parameters['_COX'] = 2
        else:
            _Caculation_Parameters['_COX'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_NMOS1_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_NMOS1_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]

        # For num of M1 in Nmos

        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4', 'SRF_Nmos_Tr1', 'BND_POLayer_Hrz_Gate')
        target_coord = tmp1[0][0][0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_NMOS1_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_POLayer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_NMOS1_Gate_ViaM0M1')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['SRF_NMOS1_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### NMOS1 gate Metal1 extension
        # Define Boundary_element
        self._DesignParameter['BND_Metal1Layer_Connect_N1_Gate_extension'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Metal1Layer_Connect_N1_Gate')
        tmp2 = self.get_param_KJH4('SRF_NMOS1_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal1Layer_Connect_N1_Gate_extension']['_YWidth'] = tmp2[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal1Layer_Connect_N1_Gate_extension']['_XWidth'] = tmp1[0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal1Layer_Connect_N1_Gate_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_NMOS1_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal1Layer_Connect_N1_Gate_extension')
        approaching_coord = tmp2[0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal1Layer_Connect_N1_Gate_extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal1Layer_Connect_N1_Gate_extension']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### NMOS1 gate Metal2
        # Define Boundary_element
        self._DesignParameter['BND_Metal2Layer_Connect_N1_Gate'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Metal1Layer_Connect_N1_Gate')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal2Layer_Connect_N1_Gate']['_YWidth'] = tmp1[0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal2Layer_Connect_N1_Gate']['_XWidth'] = tmp1[0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal2Layer_Connect_N1_Gate']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal1Layer_Connect_N1_Gate')
        target_coord = tmp1[0][0]['_XY_down_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal2Layer_Connect_N1_Gate')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal2Layer_Connect_N1_Gate')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal2Layer_Connect_N1_Gate']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### NMOS1 gate Metal3
        # Define Boundary_element
        self._DesignParameter['BND_Metal3Layer_Connect_N1_Gate'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Metal1Layer_Connect_N1_Gate')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal3Layer_Connect_N1_Gate']['_YWidth'] = tmp1[0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal3Layer_Connect_N1_Gate']['_XWidth'] = tmp1[0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal3Layer_Connect_N1_Gate']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal1Layer_Connect_N1_Gate')
        target_coord = tmp1[0][0]['_XY_down_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal3Layer_Connect_N1_Gate')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal3Layer_Connect_N1_Gate')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal3Layer_Connect_N1_Gate']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### NMOS1_Gate_ViaM1M3
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Nmos1_Gate_ViaM1M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_Nmos1_Gate_ViaM1M3'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Nmos1_Gate_ViaM1M3']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Nmos1_Gate_ViaM1M3']['_Angle'] = 0

        # Calcuate _COY
        _Caculation_Parameters['_COY'] = 1

        # Calcuate _COX
        tmp = self.get_param_KJH4('BND_Metal3Layer_Connect_N1_Gate')
        M3_xwidth = tmp[0][0]['_Xwidth']
        Num_V1 = int(
            (M3_xwidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COX'] = 2
        else:
            _Caculation_Parameters['_COX'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Nmos1_Gate_ViaM1M3']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Nmos1_Gate_ViaM1M3']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal3Layer_Connect_N1_Gate')
        target_coord = tmp1[0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Nmos1_Gate_ViaM1M3', 'SRF_ViaM2M3', 'BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Nmos1_Gate_ViaM1M3')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Nmos1_Gate_ViaM1M3']['_XYCoordinates'] = tmpXY

        # 여기까지 drc 검증 완료 !!
        # 12/30 drc clear

        ## ################################################################################################################### NMOS0, NMOS1 Gate connect METAL3
        # Define Boundary_element
        self._DesignParameter['BND_Metal3Layer_Connect_N0_N1_Gate'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Metal3Layer_Connect_N0_Gate')
        tmp2 = self.get_param_KJH4('BND_Metal3Layer_Connect_N1_Gate')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal3Layer_Connect_N0_N1_Gate']['_YWidth'] = 200

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal3Layer_Connect_N0_N1_Gate']['_XWidth'] = abs(tmp2[0][0]['_XY_right'][0]-tmp1[0][0]['_XY_left'][0])

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal3Layer_Connect_N0_N1_Gate']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        tmp11 = self.get_param_KJH4('BND_Metal3Layer_Connect_N0_Gate')
        tmp12 = self.get_param_KJH4('BND_Metal3Layer_Connect_N1_Gate')
        tmp13 = self.get_param_KJH4('SRF_Nmos1_Gate_ViaM1M3', 'SRF_ViaM2M3', 'BND_Met3Layer')
        target_coordx = abs((tmp11[0][0]['_XY_left'][0] + tmp12[0][0]['_XY_right'][0])/2)
        target_coordy = tmp13[0][0][0][0]['_XY_down'][1]
        target_coord = [target_coordx, target_coordy]
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal3Layer_Connect_N0_N1_Gate')
        approaching_coord = tmp2[0][0]['_XY_down']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal3Layer_Connect_N0_N1_Gate')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal3Layer_Connect_N0_N1_Gate']['_XYCoordinates'] = tmpXY


        ## ################################################################################################################### NMOS0 Gate,Drain connect METAL3
        # Define Boundary_element
        self._DesignParameter['BND_Metal3Layer_Connect_N0_Drain_Gate'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4','SRF_Nmos_Tr0', 'BND_Metal3Layer_Hrz_Drain')
        tmp2 = self.get_param_KJH4('BND_Metal3Layer_Connect_N0_N1_Gate')


        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal3Layer_Connect_N0_Drain_Gate']['_YWidth'] = abs(tmp2[0][0]['_XY_up'][1]-tmp1[0][0][0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal3Layer_Connect_N0_Drain_Gate']['_XWidth'] = abs(tmp1[0][0][-1][0]['_XY_right'][0] - tmp1[0][0][0][0]['_XY_left'][0])

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal3Layer_Connect_N0_Drain_Gate']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4','SRF_Nmos_Tr0', 'BND_Metal3Layer_Hrz_Drain')
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal3Layer_Connect_N0_Drain_Gate')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal3Layer_Connect_N0_Drain_Gate')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal3Layer_Connect_N0_Drain_Gate']['_XYCoordinates'] = tmpXY

## ################################################################################################################### NMOS2 Drain, NMOS3 Source connect METAL2
        # Define Boundary_element
        self._DesignParameter['BND_Metal2Layer_Connect_N2_N3_Drain_Source'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr2Tr3','SRF_Nmos_Tr2','BND_Metal1Layer_Connect_Gate_extension')
        tmp2 = self.get_param_KJH4('SRF_Nmos_Tr2Tr3','SRF_Nmos_Tr3','SRF_Nmos', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal2Layer_Connect_N2_N3_Drain_Source']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal2Layer_Connect_N2_N3_Drain_Source']['_XWidth'] = (
            abs(tmp2[0][0][0][-1][0][0][0]['_XY_right'][0] - tmp1[0][0][0][0]['_XY_left'][0]))

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal2Layer_Connect_N2_N3_Drain_Source']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr2Tr3','SRF_Nmos_Tr2','BND_Metal1Layer_Connect_Gate_extension')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal2Layer_Connect_N2_N3_Drain_Source')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal2Layer_Connect_N2_N3_Drain_Source')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal2Layer_Connect_N2_N3_Drain_Source']['_XYCoordinates'] = tmpXY


        ## ################################################################################################################### NMOS2 Drain, NMOS3 Source connect ViaM1M2
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Nmos2_Drain_NMOS3_Source_ViaM1M2'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_Nmos2_Drain_NMOS3_Source_ViaM1M2'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Nmos2_Drain_NMOS3_Source_ViaM1M2']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Nmos2_Drain_NMOS3_Source_ViaM1M2']['_Angle'] = 0

        # Calcuate _COY
        _Caculation_Parameters['_COY'] = 1

        # Calcuate _COX
        tmp = self.get_param_KJH4('SRF_Nmos_Tr2Tr3','SRF_Nmos_Tr2','BND_Metal1Layer_Connect_Gate_extension')
        M3_xwidth = tmp[0][0][0][0]['_Xwidth']
        Num_V1 = int(
            (M3_xwidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COX'] = 2
        else:
            _Caculation_Parameters['_COX'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Nmos2_Drain_NMOS3_Source_ViaM1M2']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Nmos2_Drain_NMOS3_Source_ViaM1M2']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr2Tr3','SRF_Nmos_Tr2','BND_Metal1Layer_Connect_Gate_extension')
        target_coord = tmp1[0][0][0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Nmos2_Drain_NMOS3_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Nmos2_Drain_NMOS3_Source_ViaM1M2')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Nmos2_Drain_NMOS3_Source_ViaM1M2']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### NMOS3 Source extension METAL2
        # Define Boundary_element
        self._DesignParameter['BND_Metal2Layer_Connect_N3_Source_extension'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr2Tr3', 'SRF_Nmos_Tr2', 'BND_Metal1Layer_Connect_Gate_extension')
        tmp2 = self.get_param_KJH4('SRF_Nmos_Tr2Tr3', 'SRF_Nmos_Tr3', 'SRF_Nmos', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal2Layer_Connect_N3_Source_extension']['_YWidth'] = abs(tmp2[0][0][0][0][0][0][0]['_XY_cent'][1]-tmp1[0][0][0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal2Layer_Connect_N3_Source_extension']['_XWidth'] = tmp2[0][0][0][0][0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal2Layer_Connect_N3_Source_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        SRF_Source_ViaM1M2_count = self.get_param_KJH4('SRF_Nmos_Tr2Tr3', 'SRF_Nmos_Tr3', 'SRF_Nmos', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
        print(len(SRF_Source_ViaM1M2_count[0][0][0]))
        print(len(SRF_Source_ViaM1M2_count[0][0][0][0]))
        for i in range (0, len(SRF_Source_ViaM1M2_count[0][0][0])):
            # Target_coord
            tmp1 = self.get_param_KJH4('SRF_Nmos_Tr2Tr3', 'SRF_Nmos_Tr3', 'SRF_Nmos', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
            target_coord = tmp1[0][0][0][i][0][0][0]['_XY_cent']
            # Approaching_coord
            tmp2 = self.get_param_KJH4('BND_Metal2Layer_Connect_N3_Source_extension')
            approaching_coord = tmp2[0][0]['_XY_up']
            # Sref coord
            tmp3 = self.get_param_KJH4('BND_Metal2Layer_Connect_N3_Source_extension')
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            # Define
            self._DesignParameter['BND_Metal2Layer_Connect_N3_Source_extension']['_XYCoordinates'] = tmpXY

        # DRC 검증 완료 (04/06)
        # 12/30 clear
## ################################################################################################################### Metal2 PMOS0 Gate PMOS3 Gate connect
        # Define Boundary_element
        self._DesignParameter['BND_Metal2Layer_Connect_P0_P3_Gate'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr0Tr3', 'SRF_Pmos_Tr0', 'BND_Met1Layer_Gate_connect')
        tmp2 = self.get_param_KJH4('SRF_Pmos_Tr0Tr3', 'SRF_Pmos_Tr3', 'BND_Met1Layer_Drain_Gate_connect')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal2Layer_Connect_P0_P3_Gate']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal2Layer_Connect_P0_P3_Gate']['_XWidth'] = (abs(tmp1[0][0][-1][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0]))

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal2Layer_Connect_P0_P3_Gate']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr0Tr3', 'SRF_Pmos_Tr0', 'BND_Met1Layer_Gate_connect')
        target_coord = tmp1[0][0][-1][0]['_XY_up_right']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal2Layer_Connect_P0_P3_Gate')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal2Layer_Connect_P0_P3_Gate')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal2Layer_Connect_P0_P3_Gate']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### PMOS0 Gate connect ViaM1M2
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None


        # Sref ViaX declaration
        self._DesignParameter['SRF_Pmos0_Gate_ViaM1M2'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None, _Name='{}:SRF_Pmos0_Gate_ViaM1M2'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Pmos0_Gate_ViaM1M2']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Pmos0_Gate_ViaM1M2']['_Angle'] = 0

        # Calcuate _COX
        _Caculation_Parameters['_COX'] = 2

        # Calcuate _COY
        tmp = self.get_param_KJH4('SRF_Pmos_Tr0Tr3', 'SRF_Pmos_Tr0', 'BND_Met1Layer_Gate_connect')
        M3_ywidth = tmp[0][0][0][0]['_Ywidth']
        Num_V1 = int(
            (M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COY'] = 2
        else:
            _Caculation_Parameters['_COY'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Pmos0_Gate_ViaM1M2']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Pmos0_Gate_ViaM1M2']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        SRF_Gate_ViaM1M2_count = self.get_param_KJH4('SRF_Pmos_Tr0Tr3', 'SRF_Pmos_Tr0', 'BND_Met1Layer_Gate_connect')
        print(len(SRF_Gate_ViaM1M2_count[0][0]))
        for i in range (0, len(SRF_Gate_ViaM1M2_count[0][0])):
            # Target_coord
            tmp1 = self.get_param_KJH4('SRF_Pmos_Tr0Tr3', 'SRF_Pmos_Tr0', 'BND_Met1Layer_Gate_connect')
            target_coord = tmp1[0][0][i][0]['_XY_cent']
            # Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_Pmos0_Gate_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']
            # Sref coord
            tmp3 = self.get_param_KJH4('SRF_Pmos0_Gate_ViaM1M2')
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            # Define
            self._DesignParameter['SRF_Pmos0_Gate_ViaM1M2']['_XYCoordinates'] = tmpXY


        ## ################################################################################################################### PMOS3 Gate connect ViaM1M2
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None


        # Sref ViaX declaration
        self._DesignParameter['SRF_Pmos3_Gate_ViaM1M2'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None, _Name='{}:SRF_Pmos3_Gate_ViaM1M2'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Pmos3_Gate_ViaM1M2']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Pmos3_Gate_ViaM1M2']['_Angle'] = 0

        # Calcuate _COX
        _Caculation_Parameters['_COX'] = 2

        # Calcuate _COY
        tmp = self.get_param_KJH4('SRF_Pmos_Tr0Tr3', 'SRF_Pmos_Tr3', 'BND_Met1Layer_Gate_connect')
        M3_ywidth = tmp[0][0][0][0]['_Ywidth']
        Num_V1 = int(
            (M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COY'] = 2
        else:
            _Caculation_Parameters['_COY'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Pmos3_Gate_ViaM1M2']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Pmos3_Gate_ViaM1M2']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        SRF_Gate_ViaM1M2_count = self.get_param_KJH4('SRF_Pmos_Tr0Tr3', 'SRF_Pmos_Tr3', 'BND_Met1Layer_Gate_connect')
        for i in range (0, len(SRF_Gate_ViaM1M2_count[0][0])):
            # Target_coord
            tmp1 = self.get_param_KJH4('SRF_Pmos_Tr0Tr3', 'SRF_Pmos_Tr3', 'BND_Met1Layer_Gate_connect')
            target_coord = tmp1[0][0][i][0]['_XY_cent']
            # Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_Pmos3_Gate_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']
            # Sref coord
            tmp3 = self.get_param_KJH4('SRF_Pmos3_Gate_ViaM1M2')
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            # Define
            self._DesignParameter['SRF_Pmos3_Gate_ViaM1M2']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Metal2 PMOS0 Gate NMOS3 Gate connect
        # Define Boundary_element
        self._DesignParameter['BND_Metal2Layer_Connect_P0_N3_Gate'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Metal2Layer_Connect_P0_P3_Gate')
        tmp2 = self.get_param_KJH4('SRF_Nmos_Tr2Tr3', 'SRF_Nmos_Tr3', 'BND_Met1Layer_Gate_connect')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal2Layer_Connect_P0_N3_Gate']['_YWidth'] = tmp1[0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal2Layer_Connect_P0_N3_Gate']['_XWidth'] = (abs(tmp1[0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0]))

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal2Layer_Connect_P0_N3_Gate']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal2Layer_Connect_P0_P3_Gate')
        target_coord = tmp1[0][0]['_XY_up_right']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal2Layer_Connect_P0_N3_Gate')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal2Layer_Connect_P0_N3_Gate')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal2Layer_Connect_P0_N3_Gate']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Metal2 PMOS0 Gate NMOS3 Gate connect extension
        # Define Boundary_element
        self._DesignParameter['BND_Metal2Layer_Connect_P0_N3_Gate_extension'] = self._BoundaryElementDeclaration(
                                                                        _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                        _XWidth=None,
                                                                        _YWidth=None,
                                                                        _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Metal2Layer_Connect_P0_N3_Gate')
        tmp2 = self.get_param_KJH4('SRF_NbodyRight_P0P3', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal2Layer_Connect_P0_N3_Gate_extension']['_YWidth'] = tmp1[0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal2Layer_Connect_P0_N3_Gate_extension']['_XWidth'] = abs(tmp1[0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_right'][0]) + 1000

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal2Layer_Connect_P0_N3_Gate_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal2Layer_Connect_P0_N3_Gate')
        target_coord = tmp1[0][0]['_XY_right']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal2Layer_Connect_P0_N3_Gate_extension')
        approaching_coord = tmp2[0][0]['_XY_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal2Layer_Connect_P0_N3_Gate_extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal2Layer_Connect_P0_N3_Gate_extension']['_XYCoordinates'] = tmpXY

        # 12/30 clear
        ## ################################################################################################################### Metal2 PMOS0 Gate PMOS4 Gate connect
        # Define Boundary_element
        self._DesignParameter['BND_Metal2Layer_Connect_P0_P4_Gate_Hrz'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Metal2Layer_Connect_P0_N3_Gate_extension')
        tmp2 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4_Nbodyring','SRF_Pmos_Tr1Tr2Tr4','SRF_Pmos_Tr4','BND_Metal2Layer_Hrz_Gate')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal2Layer_Connect_P0_P4_Gate_Hrz']['_YWidth'] = tmp2[0][0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal2Layer_Connect_P0_P4_Gate_Hrz']['_XWidth'] = abs(
            tmp1[0][0]['_XY_right'][0] - tmp2[0][0][0][0][0]['_XY_left'][0])

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal2Layer_Connect_P0_P4_Gate_Hrz']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4_Nbodyring','SRF_Pmos_Tr1Tr2Tr4','SRF_Pmos_Tr4','BND_Metal2Layer_Hrz_Gate')
        target_coord = tmp1[0][0][0][0][0]['_XY_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal2Layer_Connect_P0_P4_Gate_Hrz')
        approaching_coord = tmp2[0][0]['_XY_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal2Layer_Connect_P0_P4_Gate_Hrz')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal2Layer_Connect_P0_P4_Gate_Hrz']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Metal2 PMOS0 Gate PMOS4 Gate connect
        # Define Boundary_element
        self._DesignParameter['BND_Metal2Layer_Connect_P0_P4_Gate_Vtc'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Metal2Layer_Connect_P0_P4_Gate_Hrz')
        tmp2 = self.get_param_KJH4('BND_Metal2Layer_Connect_P0_N3_Gate_extension')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal2Layer_Connect_P0_P4_Gate_Vtc']['_YWidth'] = abs(tmp2[0][0]['_XY_up'][1]-tmp1[0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal2Layer_Connect_P0_P4_Gate_Vtc']['_XWidth'] = tmp1[0][0]['_Ywidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal2Layer_Connect_P0_P4_Gate_Vtc']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal2Layer_Connect_P0_P4_Gate_Hrz')
        target_coord = tmp1[0][0]['_XY_down_right']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal2Layer_Connect_P0_P4_Gate_Vtc')
        approaching_coord = tmp2[0][0]['_XY_down_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal2Layer_Connect_P0_P4_Gate_Vtc')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal2Layer_Connect_P0_P4_Gate_Vtc']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### NMOS3 Gate connect ViaM1M2
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Nmos3_Gate_ViaM1M2'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_Nmos3_Gate_ViaM1M2'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Nmos3_Gate_ViaM1M2']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Nmos3_Gate_ViaM1M2']['_Angle'] = 0

        # Calcuate _COX
        _Caculation_Parameters['_COX'] = 2

        # Calcuate _COY
        tmp = self.get_param_KJH4('SRF_Nmos_Tr2Tr3', 'SRF_Nmos_Tr3', 'BND_Met1Layer_Gate_connect')
        M3_ywidth = tmp[0][0][0][0]['_Ywidth']
        Num_V1 = int(
            (M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COY'] = 2
        else:
            _Caculation_Parameters['_COY'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Nmos3_Gate_ViaM1M2']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Nmos3_Gate_ViaM1M2']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        SRF_Gate_ViaM1M2_count = self.get_param_KJH4('SRF_Nmos_Tr2Tr3', 'SRF_Nmos_Tr3', 'BND_Met1Layer_Gate_connect')
        for i in range(0, len(SRF_Gate_ViaM1M2_count[0][0])):
            # Target_coord
            tmp1 = self.get_param_KJH4('SRF_Nmos_Tr2Tr3', 'SRF_Nmos_Tr3', 'BND_Met1Layer_Gate_connect')
            target_coord = tmp1[0][0][i][0]['_XY_cent']
            # Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_Nmos3_Gate_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']
            # Sref coord
            tmp3 = self.get_param_KJH4('SRF_Nmos3_Gate_ViaM1M2')
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            # Define
            self._DesignParameter['SRF_Nmos3_Gate_ViaM1M2']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### NMOS0 Drain PMOS1 Drain connect Metal5
        # Define Boundary_element
        self._DesignParameter['BND_Metal5Layer_Connect_N0_P1_Drain'] = self._BoundaryElementDeclaration(
                                                                                                    _Layer=DesignParameters._LayerMapping['METAL5'][0],
                                                                                                    _Datatype=DesignParameters._LayerMapping['METAL5'][1],
                                                                                                    _XWidth=None,
                                                                                                    _YWidth=None,
                                                                                                    _XYCoordinates=[],
        )


        tmp1 = self.get_param_KJH4('BND_Metal3Layer_Connect_N0_Drain_Gate')
        tmp2 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4_Nbodyring','BND_Metal3Layer_Connect_P1_Drain')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal5Layer_Connect_N0_P1_Drain']['_YWidth'] = abs(tmp2[0][0][0]['_XY_up'][1]-tmp1[0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal5Layer_Connect_N0_P1_Drain']['_XWidth'] = 500

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal5Layer_Connect_N0_P1_Drain']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal3Layer_Connect_N0_Drain_Gate')
        target_coord = tmp1[0][0]['_XY_down_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal5Layer_Connect_N0_P1_Drain')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal5Layer_Connect_N0_P1_Drain')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal5Layer_Connect_N0_P1_Drain']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### PMOS1 Drain connect ViaM3M5
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 5
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Pmos1_Drain_ViaM3M5'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_Pmos1_Drain_ViaM3M5'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Pmos1_Drain_ViaM3M5']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Pmos1_Drain_ViaM3M5']['_Angle'] = 0

        # Calcuate _COX
        _Caculation_Parameters['_COX'] = 3

        # Calcuate _COY
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4_Nbodyring','BND_Metal3Layer_Connect_P1_Drain')
        tmp2 = self.get_param_KJH4('BND_Metal5Layer_Connect_N0_P1_Drain')
        M3_ywidth = tmp1[0][0][0]['_Ywidth']
        Num_V1 = int(
            (M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        # Define Num of COY
        # if Num_V1 < 2:
        #     _Caculation_Parameters['_COY'] = 2
        # else:
        _Caculation_Parameters['_COY'] = 2

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Pmos1_Drain_ViaM3M5']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Pmos1_Drain_ViaM3M5']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1x = self.get_param_KJH4('BND_Metal5Layer_Connect_N0_P1_Drain')
        tmp1y = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4_Nbodyring', 'BND_Metal3Layer_Connect_P1_Drain')
        target_coordx = tmp1x[0][0]['_XY_up'][0]
        target_coordy = tmp1y[0][0][0]['_XY_cent'][1]
        target_coord = [target_coordx, target_coordy]
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Pmos1_Drain_ViaM3M5', 'SRF_ViaM3M4', 'BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pmos1_Drain_ViaM3M5')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Pmos1_Drain_ViaM3M5']['_XYCoordinates'] = tmpXY

        # tmp1 = self.get_param_KJH4('SRF_Pmos1_Drain_ViaM3M5', 'SRF_ViaM3M4', 'BND_Met4Layer')
        # tmp2 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4_Nbodyring', 'BND_Metal3Layer_Connect_P1_Drain')
        # if (tmp2[0][0]['_XY_right'][0] < tmp1[0][0][0][0]['_XY_right'][0]):




        # 12/30 clear
        ## 10/17 수정
        # PMOS1 Drian ViaM3M5 extension
        tmp1 = self.get_param_KJH4('SRF_Pmos1_Drain_ViaM3M5', 'SRF_ViaM3M4', 'BND_Met4Layer')
        tmp2 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4_Nbodyring', 'BND_Metal3Layer_Connect_P1_Drain')
        if (tmp1[0][0][0][0]['_XY_right'][0] > tmp2[0][0][0]['_XY_right'][0]):
            # Define Boundary_element
            self._DesignParameter['BND_Metal3Layer_Extension_P1_Drain'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL3'][0],
                _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )

            # Define Boundary_element _YWidth
            self._DesignParameter['BND_Metal3Layer_Extension_P1_Drain']['_YWidth'] = max (tmp2[0][0][0]['_Ywidth'], tmp1[0][0][0][0]['_Ywidth'])

            # Define Boundary_element _XWidth
            self._DesignParameter['BND_Metal3Layer_Extension_P1_Drain']['_XWidth'] = abs(
                tmp1[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0]['_XY_left'][0])

            # Calculate Sref XYcoord
            # initialize coordinate
            self._DesignParameter['BND_Metal3Layer_Extension_P1_Drain']['_XYCoordinates'] = [[0, 0]]
            tmpXY = []
            # Calculate
            # Target_coord
            tmp1 = self.get_param_KJH4('SRF_Pmos1_Drain_ViaM3M5', 'SRF_ViaM3M4', 'BND_Met4Layer')
            target_coord = tmp1[0][0][0][0]['_XY_right']
            # Approaching_coord
            tmp2 = self.get_param_KJH4('BND_Metal3Layer_Extension_P1_Drain')
            approaching_coord = tmp2[0][0]['_XY_right']
            # Sref coord
            tmp3 = self.get_param_KJH4('BND_Metal3Layer_Extension_P1_Drain')
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            # Define
            self._DesignParameter['BND_Metal3Layer_Extension_P1_Drain']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### NMOS0 Drain connect ViaM3M5
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 5
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Nmos0_Drain_ViaM3M5'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_Nmos0_Drain_ViaM3M5'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Nmos0_Drain_ViaM3M5']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Nmos0_Drain_ViaM3M5']['_Angle'] = 0

        # Calcuate _COX
        _Caculation_Parameters['_COX'] = 3

        # Calcuate _COY
        tmp1 = self.get_param_KJH4('BND_Metal3Layer_Connect_N0_Drain_Gate')
        tmp2 = self.get_param_KJH4('BND_Metal5Layer_Connect_N0_P1_Drain')
        M3_ywidth = tmp1[0][0]['_Ywidth']
        Num_V1 = int(
            (M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COY'] = 2
        else:
            _Caculation_Parameters['_COY'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Nmos0_Drain_ViaM3M5']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Nmos0_Drain_ViaM3M5']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal5Layer_Connect_N0_P1_Drain')
        target_coord = tmp1[0][0]['_XY_down']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Nmos0_Drain_ViaM3M5', 'SRF_ViaM3M4', 'BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Nmos0_Drain_ViaM3M5')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Nmos0_Drain_ViaM3M5']['_XYCoordinates'] = tmpXY

        # DRC 검증 완료
## ################################################################################################################### PMOS1,2 Source PMOS0 Drain connect Metal4
        # Define Boundary_element
        self._DesignParameter['BND_Metal4Layer_Connect_P1_P2_Source_P4_Drain'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['METAL4'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['METAL4'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4_Nbodyring','BND_Metal3Layer_Connect_P1P2_Source')
        tmp2 = self.get_param_KJH4('SRF_Pmos_Tr0Tr3', 'SRF_Pmos_Tr0','BND_Metal3Layer_Connect_P0_Drain')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal4Layer_Connect_P1_P2_Source_P4_Drain']['_YWidth'] = abs(tmp2[0][0][0][0]['_XY_up'][1]-tmp1[0][0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal4Layer_Connect_P1_P2_Source_P4_Drain']['_XWidth'] = 1000

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal4Layer_Connect_P1_P2_Source_P4_Drain']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr0Tr3', 'SRF_Pmos_Tr0','BND_Metal3Layer_Connect_P0_Drain')
        target_coord = tmp1[0][0][0][0]['_XY_up']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal4Layer_Connect_P1_P2_Source_P4_Drain')
        approaching_coord = tmp2[0][0]['_XY_up']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal4Layer_Connect_P1_P2_Source_P4_Drain')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal4Layer_Connect_P1_P2_Source_P4_Drain']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### PMOS0 Drain connect ViaM3M4
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Pmos0_Drain_ViaM3M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_Pmos0_Drain_ViaM3M4'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Pmos0_Drain_ViaM3M4']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Pmos0_Drain_ViaM3M4']['_Angle'] = 0

        # Calcuate _COX
        _Caculation_Parameters['_COX'] = 7

        # Calcuate _COY
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr0Tr3', 'SRF_Pmos_Tr0','BND_Metal3Layer_Connect_P0_Drain')
        tmp2 = self.get_param_KJH4('BND_Metal4Layer_Connect_P1_P2_Source_P4_Drain')
        M3_ywidth = tmp1[0][0][0][0]['_Ywidth']
        Num_V1 = int(
            (M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COY'] = 2
        else:
            _Caculation_Parameters['_COY'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Pmos0_Drain_ViaM3M4']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Pmos0_Drain_ViaM3M4']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal4Layer_Connect_P1_P2_Source_P4_Drain')
        target_coord = tmp1[0][0]['_XY_up']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Pmos0_Drain_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pmos0_Drain_ViaM3M4')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Pmos0_Drain_ViaM3M4']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### PMOS1,2 Source connect ViaM3M4
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Pmos1_Pmos2_Source_ViaM3M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_Pmos1_Pmos2_Source_ViaM3M4'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Pmos1_Pmos2_Source_ViaM3M4']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Pmos1_Pmos2_Source_ViaM3M4']['_Angle'] = 0

        # Calcuate _COX
        _Caculation_Parameters['_COX'] = 7

        # Calcuate _COY
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4_Nbodyring','BND_Metal3Layer_Connect_P1P2_Source')
        tmp2 = self.get_param_KJH4('BND_Metal4Layer_Connect_P1_P2_Source_P4_Drain')
        M3_ywidth = tmp1[0][0][0]['_Ywidth']
        Num_V1 = int(
            (M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COY'] = 2
        else:
            _Caculation_Parameters['_COY'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Pmos1_Pmos2_Source_ViaM3M4']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Pmos1_Pmos2_Source_ViaM3M4']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal4Layer_Connect_P1_P2_Source_P4_Drain')
        target_coord = tmp1[0][0]['_XY_down']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Pmos1_Pmos2_Source_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pmos1_Pmos2_Source_ViaM3M4')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Pmos1_Pmos2_Source_ViaM3M4']['_XYCoordinates'] = tmpXY

        # 12/30 clear
        # DRC 검증 완료
        ## ################################################################################################################### NMOS1 Drain NMOS4 Gate connect
        ## ################################################################################################################### NMOS4 Gate connect METAL2
        # Define Boundary_element
        self._DesignParameter['BND_Metal2Layer_Connect_N4_Gate'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4', 'SRF_Nmos_Tr4', 'BND_Met1Layer_Drain_connect' )
        tmp2 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4', 'SRF_Nmos_Tr1', 'BND_Metal3Layer_Connect_N1_Drain')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal2Layer_Connect_N4_Gate']['_YWidth'] = abs(tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        # self._DesignParameter['BND_Metal2Layer_Connect_N4_Gate']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']
        self._DesignParameter['BND_Metal2Layer_Connect_N4_Gate']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth'] / 2 # 12/31 수정

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal2Layer_Connect_N4_Gate']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4', 'SRF_Nmos_Tr4', 'BND_Met1Layer_Drain_connect' )
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal2Layer_Connect_N4_Gate')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal2Layer_Connect_N4_Gate')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal2Layer_Connect_N4_Gate']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### NMOS4 Gate connect ViaM1M2
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Nmos4_Gate_ViaM1M2'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_Nmos4_Gate_ViaM1M2'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Nmos4_Gate_ViaM1M2']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Nmos4_Gate_ViaM1M2']['_Angle'] = 0

        # Calcuate _COY
        _Caculation_Parameters['_COY'] = 1

        # Calcuate _COX
        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4', 'SRF_Nmos_Tr4', 'BND_Met1Layer_Drain_connect')

        M3_ywidth = tmp1[0][0][0][0]['_Xwidth']
        Num_V1 = int(
            (M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COX'] = 2
        else:
            _Caculation_Parameters['_COX'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Nmos4_Gate_ViaM1M2']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Nmos4_Gate_ViaM1M2']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4', 'SRF_Nmos_Tr4', 'BND_Met1Layer_Drain_connect')
        target_coord = tmp1[0][0][0][0]['_XY_up']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Nmos4_Gate_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Nmos4_Gate_ViaM1M2')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Nmos4_Gate_ViaM1M2']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### NMOS1 Drain connect extension METAL3
        # Define Boundary_element
        self._DesignParameter['BND_Metal3Layer_Connect_N1_Drain_extension'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Metal2Layer_Connect_N4_Gate' )
        tmp2 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4', 'SRF_Nmos_Tr1', 'BND_Metal3Layer_Connect_N1_Drain')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal3Layer_Connect_N1_Drain_extension']['_YWidth'] = min(1000, tmp2[0][0][0][0]['_Ywidth'])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal3Layer_Connect_N1_Drain_extension']['_XWidth'] = abs(tmp2[0][0][0][0]['_XY_right'][0]-tmp1[0][0]['_XY_left'][0])

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal3Layer_Connect_N1_Drain_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4', 'SRF_Nmos_Tr1', 'BND_Metal3Layer_Connect_N1_Drain' )
        target_coord = tmp1[0][0][0][0]['_XY_right']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal3Layer_Connect_N1_Drain_extension')
        approaching_coord = tmp2[0][0]['_XY_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal3Layer_Connect_N1_Drain_extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal3Layer_Connect_N1_Drain_extension']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### NMOS1 Drain, NMOS4 Gate connect ViaM2M3
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Nmos1_Drain_Nmos4_Gate_ViaM2M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_Nmos1_Drain_Nmos4_Gate_ViaM2M3'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Nmos1_Drain_Nmos4_Gate_ViaM2M3']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Nmos1_Drain_Nmos4_Gate_ViaM2M3']['_Angle'] = 0

        # Calcuate _COY
        _Caculation_Parameters['_COY'] = 2

        # Calcuate _COX
        tmp1 = self.get_param_KJH4('BND_Metal2Layer_Connect_N4_Gate')

        M3_ywidth = tmp1[0][0]['_Xwidth']
        Num_V1 = int(
            (M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COX'] = 2
        else:
            _Caculation_Parameters['_COX'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Nmos1_Drain_Nmos4_Gate_ViaM2M3']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Nmos1_Drain_Nmos4_Gate_ViaM2M3']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1x = self.get_param_KJH4('BND_Metal2Layer_Connect_N4_Gate')
        tmp1y = self.get_param_KJH4('BND_Metal3Layer_Connect_N1_Drain_extension')
        target_coordx = tmp1x[0][0]['_XY_down'][0]
        target_coordy = tmp1y[0][0]['_XY_down'][1]
        target_coord = [target_coordx, target_coordy] # 12/31 수정
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Nmos1_Drain_Nmos4_Gate_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Nmos1_Drain_Nmos4_Gate_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Nmos1_Drain_Nmos4_Gate_ViaM2M3']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### NMOS1 Drain PMOS2 Drain connect METAL5
        # Define Boundary_element
        self._DesignParameter['BND_Metal5Layer_Connect_N1_P2_Drain'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL5'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL5'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Metal3Layer_Connect_N1_Drain_extension')
        tmp2 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4_Nbodyring', 'BND_Metal3Layer_Connect_P2_Drain')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal5Layer_Connect_N1_P2_Drain']['_YWidth'] = abs(tmp2[0][0][0]['_XY_up'][1] - tmp1[0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal5Layer_Connect_N1_P2_Drain']['_XWidth'] = 1000

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal5Layer_Connect_N1_P2_Drain']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal3Layer_Connect_N1_Drain_extension')
        target_coord = tmp1[0][0]['_XY_down_right']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal5Layer_Connect_N1_P2_Drain')
        approaching_coord = tmp2[0][0]['_XY_down_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal5Layer_Connect_N1_P2_Drain')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal5Layer_Connect_N1_P2_Drain']['_XYCoordinates'] = tmpXY

        # ## ################################################################################################################### PMOS2 Drain connect ViaM3M5
        # # Define ViaX Parameter
        # _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        # _Caculation_Parameters['_Layer1'] = 3
        # _Caculation_Parameters['_Layer2'] = 5
        # _Caculation_Parameters['_COX'] = None
        # _Caculation_Parameters['_COY'] = None
        #
        # # Sref ViaX declaration
        # self._DesignParameter['SRF_Pmos2_Drain_ViaM3M5'] = self._SrefElementDeclaration(
        #     _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
        #                                                     _Name='{}:SRF_Pmos2_Drain_ViaM3M5'.format(_Name)))[0]
        #
        # # Define Sref Relection
        # self._DesignParameter['SRF_Pmos2_Drain_ViaM3M5']['_Reflect'] = [0, 0, 0]
        #
        # # Define Sref Angle
        # self._DesignParameter['SRF_Pmos2_Drain_ViaM3M5']['_Angle'] = 0
        #
        # # Calcuate _COX
        # _Caculation_Parameters['_COX'] = 7
        #
        # # Calcuate _COY
        # tmp1 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4_Nbodyring', 'BND_Metal3Layer_Connect_P2_Drain')
        # tmp2 = self.get_param_KJH4('BND_Metal5Layer_Connect_N1_P2_Drain')
        # M3_ywidth = tmp1[0][0][0]['_Ywidth']
        # Num_V1 = int(
        #     (M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        # # Define Num of COY
        # # if Num_V1 < 2:
        # #     _Caculation_Parameters['_COY'] = 2
        # # else:
        # _Caculation_Parameters['_COY'] = 2
        #
        # # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        # self._DesignParameter['SRF_Pmos2_Drain_ViaM3M5']['_DesignObj']._CalculateDesignParameterXmin(
        #     **_Caculation_Parameters)  ## Option: Xmin, Ymin
        #
        # # Calculate Sref XYcoord
        # tmpXY = []
        # # initialized Sref coordinate
        # self._DesignParameter['SRF_Pmos2_Drain_ViaM3M5']['_XYCoordinates'] = [[0, 0]]
        #
        # # Calculate
        # # Target_coord
        # tmp1x = self.get_param_KJH4('BND_Metal5Layer_Connect_N1_P2_Drain')
        # tmp1y = self.get_param_KJH4('BND_Metal3Layer_Connect_N1_extension')
        # target_coordx = tmp1x[0][0]['_XY_cent'][0]
        # target_coordy = tmp1y[0][0]['_XY_cent'][1]
        # target_coord = [target_coordx, target_coordy]
        # # Approaching_coord
        # tmp2 = self.get_param_KJH4('SRF_Pmos2_Drain_ViaM3M5', 'SRF_ViaM3M4', 'BND_Met4Layer')
        # approaching_coord = tmp2[0][0][0][0]['_XY_up']
        # # Sref coord
        # tmp3 = self.get_param_KJH4('SRF_Pmos2_Drain_ViaM3M5')
        # Scoord = tmp3[0][0]['_XY_origin']
        # # Cal
        # New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        # tmpXY.append(New_Scoord)
        # # Define
        # self._DesignParameter['SRF_Pmos2_Drain_ViaM3M5']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### NMOS1 Drain connect ViaM3M5
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 5
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Nmos1_Drain_ViaM3M5'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_Nmos1_Drain_ViaM3M5'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Nmos1_Drain_ViaM3M5']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Nmos1_Drain_ViaM3M5']['_Angle'] = 0

        # Calcuate _COX
        _Caculation_Parameters['_COX'] = 7

        # Calcuate _COY
        tmp1 = self.get_param_KJH4('BND_Metal3Layer_Connect_N1_Drain_extension')
        tmp2 = self.get_param_KJH4('BND_Metal5Layer_Connect_N1_P2_Drain')
        M3_ywidth = tmp1[0][0]['_Ywidth']
        Num_V1 = int(
            (M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COY'] = 2
        else:
            _Caculation_Parameters['_COY'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Nmos1_Drain_ViaM3M5']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Nmos1_Drain_ViaM3M5']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal5Layer_Connect_N1_P2_Drain')
        target_coord = tmp1[0][0]['_XY_down']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Nmos1_Drain_ViaM3M5', 'SRF_ViaM3M4', 'BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Nmos1_Drain_ViaM3M5')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Nmos1_Drain_ViaM3M5']['_XYCoordinates'] = tmpXY

        #12/31 추가
        ## ################################################################################################################### NMOS0 Gate,Drain connect METAL3
        # Define Boundary_element
        self._DesignParameter['BND_Metal3Layer_Extension_N0_Gate'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4( 'SRF_Nmos0_Drain_ViaM3M5', 'SRF_ViaM3M4', 'BND_Met3Layer')
        tmp2 = self.get_param_KJH4('BND_Metal3Layer_Connect_N0_N1_Gate')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal3Layer_Extension_N0_Gate']['_YWidth'] = abs(
            tmp2[0][0]['_XY_up'][1] - tmp1[0][0][0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal3Layer_Extension_N0_Gate']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal3Layer_Extension_N0_Gate']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Nmos0_Drain_ViaM3M5', 'SRF_ViaM3M4', 'BND_Met3Layer')
        target_coord = tmp1[0][0][0][0]['_XY_down_right']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal3Layer_Extension_N0_Gate')
        approaching_coord = tmp2[0][0]['_XY_down_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal3Layer_Extension_N0_Gate')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal3Layer_Extension_N0_Gate']['_XYCoordinates'] = tmpXY

        # 12/31 clear
        ## ################################################################################################################### NMOS4 Drain PMOS4 Drain connect METAL5 (Vout)
        # Define Boundary_element
        self._DesignParameter['BND_Metal5Layer_Connect_N4_P4_Drain'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['METAL5'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['METAL5'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4_Nbodyring','SRF_Pmos_Tr1Tr2Tr4','SRF_Pmos_Tr4','BND_Metal3Layer_Connect_P4_Drain')
        tmp2 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4','SRF_Nmos_Tr4', 'BND_Metal3Layer_Connect_N4_Drain')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal5Layer_Connect_N4_P4_Drain']['_YWidth'] = abs(
            tmp1[0][0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal5Layer_Connect_N4_P4_Drain']['_XWidth'] = 500

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal5Layer_Connect_N4_P4_Drain']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4_Nbodyring','SRF_Pmos_Tr1Tr2Tr4','SRF_Pmos_Tr4','BND_Metal3Layer_Connect_P4_Drain')
        target_coord = tmp1[0][0][0][0][0]['_XY_up']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal5Layer_Connect_N4_P4_Drain')
        approaching_coord = tmp2[0][0]['_XY_up']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal5Layer_Connect_N4_P4_Drain')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal5Layer_Connect_N4_P4_Drain']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### PMOS4 Drain connect ViaM3M5
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 5
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Pmos4_Drain_ViaM3M5'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_Pmos4_Drain_ViaM3M5'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Pmos4_Drain_ViaM3M5']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Pmos4_Drain_ViaM3M5']['_Angle'] = 0

        # Calcuate _COX
        _Caculation_Parameters['_COX'] = 3

        # Calcuate _COY
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4_Nbodyring','SRF_Pmos_Tr1Tr2Tr4','SRF_Pmos_Tr4','BND_Metal3Layer_Connect_P4_Drain')
        # tmp2 = self.get_param_KJH4('BND_Metal4Layer_Connect_N1_P2_Drain')
        M3_ywidth = tmp1[0][0][0][0][0]['_Ywidth']
        Num_V1 = int(
            (M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COY'] = 2
        else:
            _Caculation_Parameters['_COY'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Pmos4_Drain_ViaM3M5']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Pmos4_Drain_ViaM3M5']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal5Layer_Connect_N4_P4_Drain')
        target_coord = tmp1[0][0]['_XY_up']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Pmos4_Drain_ViaM3M5', 'SRF_ViaM3M4', 'BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pmos4_Drain_ViaM3M5')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Pmos4_Drain_ViaM3M5']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### NMOS4 Drain connect ViaM3M5
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 5
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Nmos4_Drain_ViaM3M5'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_Nmos4_Drain_ViaM3M5'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Nmos4_Drain_ViaM3M5']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Nmos4_Drain_ViaM3M5']['_Angle'] = 0

        # Calcuate _COX
        _Caculation_Parameters['_COX'] = 3

        # Calcuate _COY
        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr0Tr1Tr4','SRF_Nmos_Tr4', 'BND_Metal3Layer_Connect_N4_Drain')
        # tmp2 = self.get_param_KJH4('BND_Metal4Layer_Connect_N4_P4_Drain')
        M3_ywidth = tmp1[0][0][0][0]['_Ywidth']
        Num_V1 = int(
            (M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COY'] = 2
        else:
            _Caculation_Parameters['_COY'] = Num_V1 - 3

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Nmos4_Drain_ViaM3M5']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Nmos4_Drain_ViaM3M5']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal5Layer_Connect_N4_P4_Drain')
        target_coord = tmp1[0][0]['_XY_down']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Nmos4_Drain_ViaM3M5', 'SRF_ViaM3M4', 'BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Nmos4_Drain_ViaM3M5')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Nmos4_Drain_ViaM3M5']['_XYCoordinates'] = tmpXY

        # 12/31 clear

        # 저항, 커패시터 제외하고 라우팅 끝 DRC 검증 완 (04/06)


        # A53_TIA_P0P1P2P3P4N0N1N2N3N4_PNbodyring: SRF_cap0cap1:SRF_cap1: SRF_Array:SRF_HDVNCAP: SRF_Via2_PortA_Hrz - M3, M4 있음
        ## ################################################################################################################### Cao0, Cap1 portB connect METAL4
        # Define Boundary_element
        self._DesignParameter['BND_Metal4Layer_Connect_C0_C1_PortB'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['METAL4'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_cap0cap1', 'SRF_cap0', 'SRF_Array','SRF_HDVNCAP', 'BND_PortB_Hrz_METAL4')
        tmp2 = self.get_param_KJH4('SRF_cap0cap1', 'SRF_cap1', 'SRF_Array','SRF_HDVNCAP', 'BND_PortB_Hrz_METAL4')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal4Layer_Connect_C0_C1_PortB']['_YWidth'] = tmp1[0][0][0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal4Layer_Connect_C0_C1_PortB']['_XWidth'] = abs(tmp2[0][0][0][0][0][0]['_XY_left'][0]- tmp1[0][0][0][0][0][0]['_XY_right'][0])

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal4Layer_Connect_C0_C1_PortB']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_cap0cap1', 'SRF_cap0', 'SRF_Array','SRF_HDVNCAP', 'BND_PortB_Hrz_METAL4')
        target_coord = tmp1[0][0][0][0][0][0]['_XY_down_right']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal4Layer_Connect_C0_C1_PortB')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal4Layer_Connect_C0_C1_PortB')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal4Layer_Connect_C0_C1_PortB']['_XYCoordinates'] = tmpXY


        ## ################################################################################################################### Cao0, Cap1 portA connect METAL5
        # Define Boundary_element
        self._DesignParameter['BND_Metal5Layer_Connect_C0_C1_PortA'] = self._BoundaryElementDeclaration(
                                                                    _Layer=DesignParameters._LayerMapping['METAL5'][0],
                                                                    _Datatype=DesignParameters._LayerMapping['METAL5'][1],
                                                                    _XWidth=None,
                                                                    _YWidth=None,
                                                                    _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_cap0cap1', 'SRF_cap0', 'SRF_Array', 'BND_CBot_METAL5')
        tmp2 = self.get_param_KJH4('SRF_cap0cap1', 'SRF_cap1', 'SRF_Array', 'BND_CBot_METAL5')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal5Layer_Connect_C0_C1_PortA']['_YWidth'] = tmp1[0][0][0][0][0]['_Xwidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal5Layer_Connect_C0_C1_PortA']['_XWidth'] = abs(tmp2[0][0][0][0][0]['_XY_down'][0] - tmp1[0][0][0][0][0]['_XY_up'][0])

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal5Layer_Connect_C0_C1_PortA']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_cap0cap1', 'SRF_cap0', 'SRF_Array',  'BND_CBot_METAL5')
        target_coord = tmp1[0][0][0][0][0]['_XY_up_right']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal5Layer_Connect_C0_C1_PortA')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal5Layer_Connect_C0_C1_PortA')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal5Layer_Connect_C0_C1_PortA']['_XYCoordinates'] = tmpXY

## ################################################################################################################### Cao0, Cap1 portA Pmos4, Nmos4 Drain connect METAL6
        # Define Boundary_element
        self._DesignParameter['BND_Metal6Layer_Connect_C0_C1_PortA_P4_N4_Drain'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['METAL6'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['METAL6'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Metal5Layer_Connect_C0_C1_PortA')
        tmp2 = self.get_param_KJH4('BND_Metal5Layer_Connect_N4_P4_Drain')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal6Layer_Connect_C0_C1_PortA_P4_N4_Drain']['_YWidth'] = abs(tmp2[0][0]['_XY_up'][1]-tmp1[0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal6Layer_Connect_C0_C1_PortA_P4_N4_Drain']['_XWidth'] = 2000

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal6Layer_Connect_C0_C1_PortA_P4_N4_Drain']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal5Layer_Connect_N4_P4_Drain')
        target_coord = tmp1[0][0]['_XY_up']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal6Layer_Connect_C0_C1_PortA_P4_N4_Drain')
        approaching_coord = tmp2[0][0]['_XY_up']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal6Layer_Connect_C0_C1_PortA_P4_N4_Drain')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal6Layer_Connect_C0_C1_PortA_P4_N4_Drain']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### PMOS4, NMOS4 Drain connect ViaM5M6
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 5
        _Caculation_Parameters['_Layer2'] = 6
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Pmos4_Nmos4_Drain_ViaM5M6'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_Pmos4_Nmos4_Drain_ViaM5M6'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Pmos4_Nmos4_Drain_ViaM5M6']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Pmos4_Nmos4_Drain_ViaM5M6']['_Angle'] = 0

        # Calcuate _COX
        _Caculation_Parameters['_COX'] = 3

        # Calcuate _COY
        tmp1 = self.get_param_KJH4('BND_Metal5Layer_Connect_N4_P4_Drain')
        M3_ywidth = tmp1[0][0]['_Ywidth']
        Num_V1 = int(
            (M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COY'] = 2
        else:
            _Caculation_Parameters['_COY'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Pmos4_Nmos4_Drain_ViaM5M6']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Pmos4_Nmos4_Drain_ViaM5M6']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal5Layer_Connect_N4_P4_Drain')
        target_coord = tmp1[0][0]['_XY_up']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Pmos4_Nmos4_Drain_ViaM5M6', 'SRF_ViaM5M6', 'BND_Met6Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pmos4_Nmos4_Drain_ViaM5M6')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Pmos4_Nmos4_Drain_ViaM5M6']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### C0, C1 PortA connect ViaM5M6
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 5
        _Caculation_Parameters['_Layer2'] = 6
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_C0_C1_PortA_ViaM5M6'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_C0_C1_PortA_ViaM5M6'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_C0_C1_PortA_ViaM5M6']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_C0_C1_PortA_ViaM5M6']['_Angle'] = 0

        # Calcuate _COX
        _Caculation_Parameters['_COX'] = 14

        # Calcuate _COY
        tmp1 = self.get_param_KJH4('BND_Metal5Layer_Connect_C0_C1_PortA')
        M3_ywidth = tmp1[0][0]['_Ywidth']
        Num_V1 = int(
            (M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COY'] = 2
        else:
            _Caculation_Parameters['_COY'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_C0_C1_PortA_ViaM5M6']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_C0_C1_PortA_ViaM5M6']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal6Layer_Connect_C0_C1_PortA_P4_N4_Drain')
        target_coord = tmp1[0][0]['_XY_down']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_C0_C1_PortA_ViaM5M6', 'SRF_ViaM5M6', 'BND_Met6Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_C0_C1_PortA_ViaM5M6')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_C0_C1_PortA_ViaM5M6']['_XYCoordinates'] = tmpXY

        # 12/31 clear
        # DRC 검증 완료 (04/06)
        ## ################################################################################################################### Res0 portA Cao0 portB connect METAL2
        # Res seires = 1, parallel = 1 일 때를 기준으로 코딩
        # Define Boundary_element
        # tmptest = self.get_param_KJH4('SRF_Res0', '_Met1Layer')
        # 04/07 ~
        self._DesignParameter['BND_Metal2Layer_Connect_R0_PortA_C0_PortB'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Res0', '_Met1Layer')
        tmp2 = self.get_param_KJH4('BND_Metal4Layer_Connect_C0_C1_PortB')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal2Layer_Connect_R0_PortA_C0_PortB']['_YWidth'] = abs(tmp1[0][0][0]['_XY_up'][1] - tmp2[0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal2Layer_Connect_R0_PortA_C0_PortB']['_XWidth'] = tmp1[0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal2Layer_Connect_R0_PortA_C0_PortB']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Res0', '_Met1Layer')
        target_coord = tmp1[0][0][0]['_XY_up']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal2Layer_Connect_R0_PortA_C0_PortB')
        approaching_coord = tmp2[0][0]['_XY_up']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal2Layer_Connect_R0_PortA_C0_PortB')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal2Layer_Connect_R0_PortA_C0_PortB']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### R0 PortA connect ViaM1M2
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_R0_PortA_ViaM1M2'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_R0_PortA_ViaM1M2'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_R0_PortA_ViaM1M2']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_R0_PortA_ViaM1M2']['_Angle'] = 0

        # Calcuate _COY
        _Caculation_Parameters['_COY'] = 1

        # Calcuate _COX
        tmp1 = self.get_param_KJH4('SRF_Res0', '_Met1Layer')
        M3_ywidth = tmp1[0][0][0]['_Xwidth']
        Num_V1 = int(
            (M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COX'] = 2
        else:
            _Caculation_Parameters['_COX'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_R0_PortA_ViaM1M2']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_R0_PortA_ViaM1M2']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Res0', '_Met1Layer')
        target_coord = tmp1[0][0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_R0_PortA_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_R0_PortA_ViaM1M2')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_R0_PortA_ViaM1M2']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Res0 portA METAL1 extension
        self._DesignParameter['BND_Metal1Layer_R0_PortA_extension'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Res0', '_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_R0_PortA_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal1Layer_R0_PortA_extension']['_YWidth'] = tmp2[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal1Layer_R0_PortA_extension']['_XWidth'] = tmp1[0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal1Layer_R0_PortA_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Res0', '_Met1Layer')
        target_coord = tmp1[0][0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal1Layer_R0_PortA_extension')
        approaching_coord = tmp2[0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal1Layer_R0_PortA_extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal1Layer_R0_PortA_extension']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Res0 portA METAL2 extension
        self._DesignParameter['BND_Metal2Layer_R0_PortA_extension'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Res0', '_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_R0_PortA_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal2Layer_R0_PortA_extension']['_YWidth'] = tmp2[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal2Layer_R0_PortA_extension']['_XWidth'] = tmp1[0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal2Layer_R0_PortA_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Res0', '_Met1Layer')
        target_coord = tmp1[0][0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal2Layer_R0_PortA_extension')
        approaching_coord = tmp2[0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal2Layer_R0_PortA_extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal2Layer_R0_PortA_extension']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Res1 portA Cao1 portB connect METAL2
        # Res seires = 1, parallel = 1 일 때를 기준으로 코딩
        # Define Boundary_element
        # tmptest = self.get_param_KJH4('SRF_Res0', '_Met1Layer')
        # 04/07 ~
        self._DesignParameter['BND_Metal2Layer_Connect_R1_PortA_C1_PortB'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Res1', '_Met1Layer')
        tmp2 = self.get_param_KJH4('BND_Metal4Layer_Connect_C0_C1_PortB')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal2Layer_Connect_R1_PortA_C1_PortB']['_YWidth'] = abs(
            tmp1[0][0][0]['_XY_up'][1] - tmp2[0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal2Layer_Connect_R1_PortA_C1_PortB']['_XWidth'] = tmp1[0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal2Layer_Connect_R1_PortA_C1_PortB']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Res1', '_Met1Layer')
        target_coord = tmp1[0][0][0]['_XY_up']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal2Layer_Connect_R1_PortA_C1_PortB')
        approaching_coord = tmp2[0][0]['_XY_up']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal2Layer_Connect_R1_PortA_C1_PortB')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal2Layer_Connect_R1_PortA_C1_PortB']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### R1 PortA connect ViaM1M2
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_R1_PortA_ViaM1M2'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_R1_PortA_ViaM1M2'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_R1_PortA_ViaM1M2']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_R1_PortA_ViaM1M2']['_Angle'] = 0

        # Calcuate _COY
        _Caculation_Parameters['_COY'] = 1

        # Calcuate _COX
        tmp1 = self.get_param_KJH4('SRF_Res1', '_Met1Layer')
        M3_ywidth = tmp1[0][0][0]['_Xwidth']
        Num_V1 = int(
            (M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COX'] = 2
        else:
            _Caculation_Parameters['_COX'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_R1_PortA_ViaM1M2']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_R1_PortA_ViaM1M2']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Res1', '_Met1Layer')
        target_coord = tmp1[0][0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_R1_PortA_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_R1_PortA_ViaM1M2')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_R1_PortA_ViaM1M2']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Res1 portA METAL1 extension
        self._DesignParameter['BND_Metal1Layer_R1_PortA_extension'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Res1', '_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_R1_PortA_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal1Layer_R1_PortA_extension']['_YWidth'] = tmp2[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal1Layer_R1_PortA_extension']['_XWidth'] = tmp1[0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal1Layer_R1_PortA_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Res1', '_Met1Layer')
        target_coord = tmp1[0][0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal1Layer_R1_PortA_extension')
        approaching_coord = tmp2[0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal1Layer_R1_PortA_extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal1Layer_R1_PortA_extension']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Res1 portA METAL2 extension
        self._DesignParameter['BND_Metal2Layer_R1_PortA_extension'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Res1', '_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_R1_PortA_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal2Layer_R1_PortA_extension']['_YWidth'] = tmp2[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal2Layer_R1_PortA_extension']['_XWidth'] = tmp1[0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal2Layer_R1_PortA_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Res1', '_Met1Layer')
        target_coord = tmp1[0][0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal2Layer_R1_PortA_extension')
        approaching_coord = tmp2[0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal2Layer_R1_PortA_extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal2Layer_R1_PortA_extension']['_XYCoordinates'] = tmpXY

        # DRC 검증 완료(04/07)
        # 12/31 clear
        ## ################################################################################################################### Nmos1 Drain connect METAL3 extension
        # Define Boundary_element
        self._DesignParameter['BND_Metal3Layer_Connect_N1_extension'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4_Nbodyring', 'BND_Metal3Layer_Connect_P2_Drain')
        tmp2 = self.get_param_KJH4('SRF_Res0', '_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal3Layer_Connect_N1_extension']['_YWidth'] = min (tmp1[0][0][0]['_Ywidth'], 1000)

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal3Layer_Connect_N1_extension']['_XWidth'] = abs(
            tmp1[0][0][0]['_XY_right'][0] - tmp2[0][0][0]['_XY_left'][0])

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal3Layer_Connect_N1_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4_Nbodyring', 'BND_Metal3Layer_Connect_P2_Drain')
        target_coord = tmp1[0][0][0]['_XY_up_right']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal3Layer_Connect_N1_extension')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal3Layer_Connect_N1_extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal3Layer_Connect_N1_extension']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Nmos1 Drain Res0 PortB connect METAL5
        # Define Boundary_element
        self._DesignParameter['BND_Metal5Layer_Connect_N1_Drain_R0_PortB'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['METAL5'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['METAL5'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Metal3Layer_Connect_N1_extension')
        tmp2 = self.get_param_KJH4('SRF_Res0', '_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal5Layer_Connect_N1_Drain_R0_PortB']['_YWidth'] = abs(tmp1[0][0]['_XY_up'][1]-tmp2[0][1][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal5Layer_Connect_N1_Drain_R0_PortB']['_XWidth'] = tmp2[0][1][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal5Layer_Connect_N1_Drain_R0_PortB']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal3Layer_Connect_N1_extension')
        target_coord = tmp1[0][0]['_XY_up_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal5Layer_Connect_N1_Drain_R0_PortB')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal5Layer_Connect_N1_Drain_R0_PortB')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal5Layer_Connect_N1_Drain_R0_PortB']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### PMOS2 Drain connect ViaM3M5
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 5
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Pmos2_Drain_ViaM3M5'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_Pmos2_Drain_ViaM3M5'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Pmos2_Drain_ViaM3M5']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Pmos2_Drain_ViaM3M5']['_Angle'] = 0

        # Calcuate _COX
        _Caculation_Parameters['_COX'] = 7

        # Calcuate _COY
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4_Nbodyring', 'BND_Metal3Layer_Connect_P2_Drain')
        tmp2 = self.get_param_KJH4('BND_Metal5Layer_Connect_N1_P2_Drain')
        M3_ywidth = tmp1[0][0][0]['_Ywidth']
        Num_V1 = int(
            (M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        # Define Num of COY
        # if Num_V1 < 2:
        #     _Caculation_Parameters['_COY'] = 2
        # else:
        _Caculation_Parameters['_COY'] = 2

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Pmos2_Drain_ViaM3M5']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Pmos2_Drain_ViaM3M5']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1x = self.get_param_KJH4('BND_Metal5Layer_Connect_N1_P2_Drain')
        tmp1y = self.get_param_KJH4('BND_Metal3Layer_Connect_N1_extension')
        target_coordx = tmp1x[0][0]['_XY_cent'][0]
        target_coordy = tmp1y[0][0]['_XY_cent'][1]
        target_coord = [target_coordx, target_coordy]
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Pmos2_Drain_ViaM3M5', 'SRF_ViaM3M4', 'BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pmos2_Drain_ViaM3M5')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Pmos2_Drain_ViaM3M5']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### N1 Drain connect ViaM3M5
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 5
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_N1_Drain_ViaM3M5'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_N1_Drain_ViaM3M5'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_N1_Drain_ViaM3M5']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_N1_Drain_ViaM3M5']['_Angle'] = 0

        # Calcuate _COY
        _Caculation_Parameters['_COY'] = 2

        # Calcuate _COX
        tmp1 = self.get_param_KJH4('BND_Metal5Layer_Connect_N1_Drain_R0_PortB')
        M3_ywidth = tmp1[0][0]['_Xwidth']
        Num_V1 = int(
            (M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COX'] = 2
        else:
            _Caculation_Parameters['_COX'] = Num_V1 - 2

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_N1_Drain_ViaM3M5']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_N1_Drain_ViaM3M5']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1x = self.get_param_KJH4('BND_Metal5Layer_Connect_N1_Drain_R0_PortB')
        tmp1y = self.get_param_KJH4('BND_Metal3Layer_Connect_N1_extension')
        target_coordx = tmp1x[0][0]['_XY_cent'][0]
        target_coordy = tmp1y[0][0]['_XY_cent'][1]
        target_coord = [target_coordx, target_coordy]
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_N1_Drain_ViaM3M5', 'SRF_ViaM3M4', 'BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_N1_Drain_ViaM3M5')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_N1_Drain_ViaM3M5']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### R0 PortB connect ViaM1M5
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 5
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_R0_PortB_ViaM1M5'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_R0_PortB_ViaM1M5'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_R0_PortB_ViaM1M5']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_R0_PortB_ViaM1M5']['_Angle'] = 0

        # Calcuate _COY
        _Caculation_Parameters['_COY'] = 1

        # Calcuate _COX
        tmp1 = self.get_param_KJH4('SRF_Res0', '_Met1Layer')
        M3_ywidth = tmp1[0][1][0]['_Xwidth']
        Num_V1 = int(
            (M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COX'] = 2
        else:
            _Caculation_Parameters['_COX'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_R0_PortB_ViaM1M5']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_R0_PortB_ViaM1M5']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Res0', '_Met1Layer')
        target_coord = tmp1[0][1][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_R0_PortB_ViaM1M5', 'SRF_ViaM1M2', 'BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_R0_PortB_ViaM1M5')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_R0_PortB_ViaM1M5']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Res0 portB METAL1 extension
        self._DesignParameter['BND_Metal1Layer_R0_PortB_extension'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Res0', '_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_R0_PortB_ViaM1M5', 'SRF_ViaM1M2', 'BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal1Layer_R0_PortB_extension']['_YWidth'] = tmp2[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal1Layer_R0_PortB_extension']['_XWidth'] = tmp1[0][1][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal1Layer_R0_PortB_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Res0', '_Met1Layer')
        target_coord = tmp1[0][1][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal1Layer_R0_PortB_extension')
        approaching_coord = tmp2[0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal1Layer_R0_PortB_extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal1Layer_R0_PortB_extension']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Res0 portB METAL2 extension
        self._DesignParameter['BND_Metal2Layer_R0_PortB_extension'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Res0', '_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_R0_PortB_ViaM1M5', 'SRF_ViaM1M2', 'BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal2Layer_R0_PortB_extension']['_YWidth'] = tmp2[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal2Layer_R0_PortB_extension']['_XWidth'] = tmp1[0][1][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal2Layer_R0_PortB_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Res0', '_Met1Layer')
        target_coord = tmp1[0][1][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal2Layer_R0_PortB_extension')
        approaching_coord = tmp2[0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal2Layer_R0_PortB_extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal2Layer_R0_PortB_extension']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Res0 portB METAL3 extension
        self._DesignParameter['BND_Metal3Layer_R0_PortB_extension'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Res0', '_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_R0_PortB_ViaM1M5', 'SRF_ViaM1M2', 'BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal3Layer_R0_PortB_extension']['_YWidth'] = tmp2[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal3Layer_R0_PortB_extension']['_XWidth'] = tmp1[0][1][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal3Layer_R0_PortB_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Res0', '_Met1Layer')
        target_coord = tmp1[0][1][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal3Layer_R0_PortB_extension')
        approaching_coord = tmp2[0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal3Layer_R0_PortB_extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal3Layer_R0_PortB_extension']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Res0 portB METAL4 extension
        self._DesignParameter['BND_Metal4Layer_R0_PortB_extension'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Res0', '_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_R0_PortB_ViaM1M5', 'SRF_ViaM1M2', 'BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal4Layer_R0_PortB_extension']['_YWidth'] = tmp2[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal4Layer_R0_PortB_extension']['_XWidth'] = tmp1[0][1][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal4Layer_R0_PortB_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Res0', '_Met1Layer')
        target_coord = tmp1[0][1][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal4Layer_R0_PortB_extension')
        approaching_coord = tmp2[0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal4Layer_R0_PortB_extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal4Layer_R0_PortB_extension']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Res0 portB METAL5 extension
        self._DesignParameter['BND_Metal5Layer_R0_PortB_extension'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5'][0],
            _Datatype=DesignParameters._LayerMapping['METAL5'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Res0', '_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_R0_PortB_ViaM1M5', 'SRF_ViaM1M2', 'BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal5Layer_R0_PortB_extension']['_YWidth'] = tmp2[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal5Layer_R0_PortB_extension']['_XWidth'] = tmp1[0][1][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal5Layer_R0_PortB_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Res0', '_Met1Layer')
        target_coord = tmp1[0][1][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal5Layer_R0_PortB_extension')
        approaching_coord = tmp2[0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal5Layer_R0_PortB_extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal5Layer_R0_PortB_extension']['_XYCoordinates'] = tmpXY

        # ################################################################################################################### Nmos1 Drain Res1 PortB connect METAL5
        # Define Boundary_element
        self._DesignParameter['BND_Metal5Layer_Connect_N1_Drain_R1_PortB'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5'][0],
            _Datatype=DesignParameters._LayerMapping['METAL5'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Metal3Layer_Connect_N1_extension')
        tmp2 = self.get_param_KJH4('SRF_Res1', '_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal5Layer_Connect_N1_Drain_R1_PortB']['_YWidth'] = abs(
            tmp1[0][0]['_XY_up'][1] - tmp2[0][1][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal5Layer_Connect_N1_Drain_R1_PortB']['_XWidth'] = tmp2[0][1][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal5Layer_Connect_N1_Drain_R1_PortB']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Res1', '_Met1Layer')
        target_coord = tmp1[0][1][0]['_XY_down_right']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal5Layer_Connect_N1_Drain_R1_PortB')
        approaching_coord = tmp2[0][0]['_XY_down_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal5Layer_Connect_N1_Drain_R1_PortB')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal5Layer_Connect_N1_Drain_R1_PortB']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### N1 Drain connect ViaM3M5_2
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 5
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_N1_Drain_ViaM3M5_2'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_N1_Drain_ViaM3M5_2'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_N1_Drain_ViaM3M5_2']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_N1_Drain_ViaM3M5_2']['_Angle'] = 0

        # Calcuate _COY
        _Caculation_Parameters['_COY'] = 2

        # Calcuate _COX
        tmp1 = self.get_param_KJH4('BND_Metal5Layer_Connect_N1_Drain_R1_PortB')
        M3_ywidth = tmp1[0][0]['_Xwidth']
        Num_V1 = int(
            (M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COX'] = 2
        else:
            _Caculation_Parameters['_COX'] = Num_V1 - 2

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_N1_Drain_ViaM3M5_2']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_N1_Drain_ViaM3M5_2']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1x = self.get_param_KJH4('BND_Metal5Layer_Connect_N1_Drain_R1_PortB')
        tmp1y = self.get_param_KJH4('BND_Metal3Layer_Connect_N1_extension')
        target_coordx = tmp1x[0][0]['_XY_cent'][0]
        target_coordy = tmp1y[0][0]['_XY_cent'][1]
        target_coord = [target_coordx, target_coordy]
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_N1_Drain_ViaM3M5_2', 'SRF_ViaM3M4', 'BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_N1_Drain_ViaM3M5_2')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_N1_Drain_ViaM3M5_2']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### R1 PortB connect ViaM1M5
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 5
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_R1_PortB_ViaM1M5'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_R1_PortB_ViaM1M5'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_R1_PortB_ViaM1M5']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_R1_PortB_ViaM1M5']['_Angle'] = 0

        # Calcuate _COY
        _Caculation_Parameters['_COY'] = 1

        # Calcuate _COX
        tmp1 = self.get_param_KJH4('SRF_Res1', '_Met1Layer')
        M3_ywidth = tmp1[0][1][0]['_Xwidth']
        Num_V1 = int(
            (M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COX'] = 2
        else:
            _Caculation_Parameters['_COX'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_R1_PortB_ViaM1M5']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_R1_PortB_ViaM1M5']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Res1', '_Met1Layer')
        target_coord = tmp1[0][1][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_R1_PortB_ViaM1M5', 'SRF_ViaM1M2', 'BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_R1_PortB_ViaM1M5')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_R1_PortB_ViaM1M5']['_XYCoordinates'] = tmpXY



        ## ################################################################################################################### Res1 portB METAL1 extension
        self._DesignParameter['BND_Metal1Layer_R1_PortB_extension'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Res1', '_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_R1_PortB_ViaM1M5', 'SRF_ViaM1M2', 'BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal1Layer_R1_PortB_extension']['_YWidth'] = tmp2[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal1Layer_R1_PortB_extension']['_XWidth'] = tmp1[0][1][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal1Layer_R1_PortB_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Res1', '_Met1Layer')
        target_coord = tmp1[0][1][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal1Layer_R1_PortB_extension')
        approaching_coord = tmp2[0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal1Layer_R1_PortB_extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal1Layer_R1_PortB_extension']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Res1 portB METAL2 extension
        self._DesignParameter['BND_Metal2Layer_R1_PortB_extension'] = self._BoundaryElementDeclaration(
                                                                        _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                        _XWidth=None,
                                                                        _YWidth=None,
                                                                        _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Res1', '_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_R1_PortB_ViaM1M5', 'SRF_ViaM1M2', 'BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal2Layer_R1_PortB_extension']['_YWidth'] = tmp2[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal2Layer_R1_PortB_extension']['_XWidth'] = tmp1[0][1][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal2Layer_R1_PortB_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Res1', '_Met1Layer')
        target_coord = tmp1[0][1][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal2Layer_R1_PortB_extension')
        approaching_coord = tmp2[0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal2Layer_R1_PortB_extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal2Layer_R1_PortB_extension']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Res1 portB METAL3 extension
        self._DesignParameter['BND_Metal3Layer_R1_PortB_extension'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Res1', '_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_R1_PortB_ViaM1M5', 'SRF_ViaM1M2', 'BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal3Layer_R1_PortB_extension']['_YWidth'] = tmp2[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal3Layer_R1_PortB_extension']['_XWidth'] = tmp1[0][1][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal3Layer_R1_PortB_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Res1', '_Met1Layer')
        target_coord = tmp1[0][1][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal3Layer_R1_PortB_extension')
        approaching_coord = tmp2[0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal3Layer_R1_PortB_extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal3Layer_R1_PortB_extension']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Res1 portB METAL4 extension
        self._DesignParameter['BND_Metal4Layer_R1_PortB_extension'] = self._BoundaryElementDeclaration(
                                                                    _Layer=DesignParameters._LayerMapping['METAL4'][0],
                                                                    _Datatype=DesignParameters._LayerMapping['METAL4'][1],
                                                                    _XWidth=None,
                                                                    _YWidth=None,
                                                                    _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Res1', '_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_R1_PortB_ViaM1M5', 'SRF_ViaM1M2', 'BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal4Layer_R1_PortB_extension']['_YWidth'] = tmp2[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal4Layer_R1_PortB_extension']['_XWidth'] = tmp1[0][1][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal4Layer_R1_PortB_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Res1', '_Met1Layer')
        target_coord = tmp1[0][1][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal4Layer_R1_PortB_extension')
        approaching_coord = tmp2[0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal4Layer_R1_PortB_extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal4Layer_R1_PortB_extension']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Res1 portB METAL5 extension
        self._DesignParameter['BND_Metal5Layer_R1_PortB_extension'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5'][0],
            _Datatype=DesignParameters._LayerMapping['METAL5'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Res1', '_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_R1_PortB_ViaM1M5', 'SRF_ViaM1M2', 'BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal5Layer_R1_PortB_extension']['_YWidth'] = tmp2[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal5Layer_R1_PortB_extension']['_XWidth'] = tmp1[0][1][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal5Layer_R1_PortB_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Res1', '_Met1Layer')
        target_coord = tmp1[0][1][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal5Layer_R1_PortB_extension')
        approaching_coord = tmp2[0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal5Layer_R1_PortB_extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal5Layer_R1_PortB_extension']['_XYCoordinates'] = tmpXY





        print('##############################')
        print('##     Calculation_End    ##')
        print('##############################')

        # 4/8 초안 완성 / DRC, LVS 검증 완료
        # 12/31 clear

## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_YCH
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0
    import random

    for _iter in range(1):

        # libname = 'Proj_A53_TIA_P0P1P2P3P4N0N1N2N3N4_PNbodyring_thesis_v{}'.format(_iter + )
        cellname = 'A53_TIA_P0P1P2P3P4N0N1N2N3N4_PNbodyring_v{}'.format(_iter+10)
        _fileName = cellname + '.gds'

        _TRP0_P3_N2_N3_ChannelWidth = random.randrange(3000, 20000, 1000)
        _TRP1_P2_P4_ChannelWidth = random.randrange(3000, 20000, 1000)
        _TRN0_N1_N4_ChannelWidth = random.randrange(3000, 20000, 1000)

        _TR1_2_PMOSNumberofGate = random.randrange(15, 25, 1)
        _TR0_PMOSNumberofGate = random.randrange(2, 15, 1)
        _TR3_PMOSNumberofGate = random.randrange(2, 4, 1)
        _TR4_PMOSNumberofGate = random.randrange(15, 25, 1)
        _TR0_1_NMOSNumberofGate = random.randrange(4, 10, 1)
        _TR4_NMOSNumberofGate = random.randrange(3, 10, 1)
        _TR2_NMOSNumberofGate = random.randrange(2, 5, 1)
        _TR3_NMOSNumberofGate = random.randrange(2, 5, 1)

        _Res_Width = random.randrange(500, 1500, 100)
        _Res_Length = random.randrange(500, 1500, 100)

        _Cap_Length = random.randrange(5000, 9000, 1000)
        _Cap_finger = random.randrange(30, 70, 10)

        # _TRP0_P3_N2_N3_ChannelWidth = 6000
        # _TRP1_P2_P4_ChannelWidth = 9000
        # _TRN0_N1_N4_ChannelWidth = 8000
        #
        # _TR1_2_PMOSNumberofGate = 20
        # _TR0_PMOSNumberofGate = 3
        # _TR3_PMOSNumberofGate = 3
        # _TR4_PMOSNumberofGate = 21
        # _TR0_1_NMOSNumberofGate = 6
        # _TR4_NMOSNumberofGate = 3
        # _TR2_NMOSNumberofGate = 4
        # _TR3_NMOSNumberofGate = 4
        #
        # _Res_Width = 1100
        # _Res_Length = 1400
        #
        # _Cap_Length = 8000
        # _Cap_finger = 65

        ''' Input Parameters for Layout Object '''
        InputParams = dict(
            # PMOS
            _Tr0_PMOSNumberofGate=_TR0_PMOSNumberofGate,
            _Tr0_PMOSChannelWidth=_TRP0_P3_N2_N3_ChannelWidth,
            _Tr0_PMOSChannellength=150,
            _Tr0_PMOSGateSpacing=None,
            _Tr0_PMOSSDWidth	= None,
            _Tr0_PMOSXVT			= 'EG',
            _Tr0_PMOSPCCrit			= None,

            # Source_node_ViaM1M2
            _Tr0_PMOSSource_Via_TF= True,

            # Drain_node_ViaM1M2
            _Tr0_PMOSDrain_Via_TF= True,

            # POLY dummy setting
            _Tr0_PMOSDummy= True  , # TF
            # if _PMOSDummy == True
            _Tr0_PMOSDummy_length = None, # None/Value
            _Tr0_PMOSDummy_placement = None, # None/'Up'/'Dn'/

            # PMOS
            _Tr1_PMOSNumberofGate=_TR1_2_PMOSNumberofGate,
            _Tr1_PMOSChannelWidth=_TRP1_P2_P4_ChannelWidth,
            _Tr1_PMOSChannellength=150,
            _Tr1_PMOSGateSpacing=None,
            _Tr1_PMOSSDWidth	= None,
            _Tr1_PMOSXVT			= 'EG',
            _Tr1_PMOSPCCrit			= None,

            # Source_node_ViaM1M2
            _Tr1_PMOSSource_Via_TF= True,

            # Drain_node_ViaM1M2
            _Tr1_PMOSDrain_Via_TF= True,

            # POLY dummy setting
            _Tr1_PMOSDummy= True  , # TF
            # if _PMOSDummy == True
            _Tr1_PMOSDummy_length = None, # None/Value
            _Tr1_PMOSDummy_placement = None, # None/'Up'/'Dn'/

            # PMOS
            _Tr2_PMOSNumberofGate	= _TR1_2_PMOSNumberofGate,
            _Tr2_PMOSChannelWidth	= _TRP1_P2_P4_ChannelWidth,
            _Tr2_PMOSChannellength	= 150,
            _Tr2_PMOSGateSpacing		= None,
            _Tr2_PMOSSDWidth			= None,
            _Tr2_PMOSXVT				= 'EG',
            _Tr2_PMOSPCCrit				= None,

            # Source_node_ViaM1M2
            _Tr2_PMOSSource_Via_TF = True,

            # Drain_node_ViaM1M2
            _Tr2_PMOSDrain_Via_TF = True,

            # POLY dummy setting
            _Tr2_PMOSDummy = True, # TF
            # if _PMOSDummy == True
            _Tr2_PMOSDummy_length = None, # None/Value
            _Tr2_PMOSDummy_placement = None, # None/'Up'/'Dn'/

            # PMOS
            _Tr3_PMOSNumberofGate=_TR3_PMOSNumberofGate,
            _Tr3_PMOSChannelWidth=_TRP0_P3_N2_N3_ChannelWidth,
            _Tr3_PMOSChannellength=150,
            _Tr3_PMOSGateSpacing=None,
            _Tr3_PMOSSDWidth	= None,
            _Tr3_PMOSXVT			= 'EG',
            _Tr3_PMOSPCCrit			= None,

            # Source_node_ViaM1M2
            _Tr3_PMOSSource_Via_TF= True,

            # Drain_node_ViaM1M2
            _Tr3_PMOSDrain_Via_TF= True,

            # POLY dummy setting
            _Tr3_PMOSDummy= True  , # TF
            # if _PMOSDummy == True
            _Tr3_PMOSDummy_length = None, # None/Value
            _Tr3_PMOSDummy_placement = None, # None/'Up'/'Dn'/

            # PMOS
            _Tr4_PMOSNumberofGate=_TR4_PMOSNumberofGate,
            _Tr4_PMOSChannelWidth=_TRP1_P2_P4_ChannelWidth,
            _Tr4_PMOSChannellength=150,
            _Tr4_PMOSGateSpacing	= None,
            _Tr4_PMOSSDWidth			= None,
            _Tr4_PMOSXVT				= 'EG',
            _Tr4_PMOSPCCrit				= None,

            # Source_node_ViaM1M2
            _Tr4_PMOSSource_Via_TF = True,

            # Drain_node_ViaM1M2
            _Tr4_PMOSDrain_Via_TF = True,

            # POLY dummy setting
            _Tr4_PMOSDummy = True, # TF
            # if _PMOSDummy == True
            _Tr4_PMOSDummy_length = None, # None/Value
            _Tr4_PMOSDummy_placement = None, # None/'Up'/'Dn'/

            # NMOS Tr0
            _Tr0_NMOSNumberofGate=_TR0_1_NMOSNumberofGate,
            _Tr0_NMOSChannelWidth=_TRN0_N1_N4_ChannelWidth,
            _Tr0_NMOSChannellength=150,
            _Tr0_NMOSGateSpacing=None,
            _Tr0_NMOSSDWidth	= None,
            _Tr0_NMOSXVT			= 'EG',
            _Tr0_NMOSPCCrit			= None,

            # Source_node_ViaM1M2
            _Tr0_NMOSSource_Via_TF= True,

            # Drain_node_ViaM1M2
            _Tr0_NMOSDrain_Via_TF= True,

            # POLY dummy setting
            _Tr0_NMOSDummy= True  , # TF
            # if _PMOSDummy == True
            _Tr0_NMOSDummy_length = None, # None/Value
            _Tr0_NMOSDummy_placement = None, # None/'Up'/'Dn'/

            # NMOS Tr1
            _Tr1_NMOSNumberofGate=_TR0_1_NMOSNumberofGate,
            _Tr1_NMOSChannelWidth=_TRN0_N1_N4_ChannelWidth,
            _Tr1_NMOSChannellength=150,
            _Tr1_NMOSGateSpacing	= None,
            _Tr1_NMOSSDWidth			= None,
            _Tr1_NMOSXVT				= 'EG',
            _Tr1_NMOSPCCrit				= None,

            # Source_node_ViaM1M2
            _Tr1_NMOSSource_Via_TF = True,

            # Drain_node_ViaM1M2
            _Tr1_NMOSDrain_Via_TF = True,

            # POLY dummy setting
            _Tr1_NMOSDummy = True, # TF
            # if _PMOSDummy == True
            _Tr1_NMOSDummy_length = None, # None/Value
            _Tr1_NMOSDummy_placement = None, # None/'Up'/'Dn'/

            # NMOS
            _Tr2_NMOSNumberofGate=_TR2_NMOSNumberofGate,
            _Tr2_NMOSChannelWidth=_TRP0_P3_N2_N3_ChannelWidth,
            _Tr2_NMOSChannellength=150,
            _Tr2_NMOSGateSpacing=None,
            _Tr2_NMOSSDWidth	= None,
            _Tr2_NMOSXVT			= 'EG',
            _Tr2_NMOSPCCrit			= None,

            # Source_node_ViaM1M2
            _Tr2_NMOSSource_Via_TF= True,

            # Drain_node_ViaM1M2
            _Tr2_NMOSDrain_Via_TF= True,

            # POLY dummy setting
            _Tr2_NMOSDummy= True  , # TF
            # if _PMOSDummy == True
            _Tr2_NMOSDummy_length = None, # None/Value
            _Tr2_NMOSDummy_placement = None, # None/'Up'/'Dn'/

            # NMOS
            _Tr3_NMOSNumberofGate=_TR3_NMOSNumberofGate,
            _Tr3_NMOSChannelWidth=_TRP0_P3_N2_N3_ChannelWidth,
            _Tr3_NMOSChannellength=150,
            _Tr3_NMOSGateSpacing	= None,
            _Tr3_NMOSSDWidth			= None,
            _Tr3_NMOSXVT				= 'EG',
            _Tr3_NMOSPCCrit				= None,

            # Source_node_ViaM1M2
            _Tr3_NMOSSource_Via_TF = True,

            # Drain_node_ViaM1M2
            _Tr3_NMOSDrain_Via_TF = True,

            # POLY dummy setting
            _Tr3_NMOSDummy = True, # TF
            # if _PMOSDummy == True
            _Tr3_NMOSDummy_length = None, # None/Value
            _Tr3_NMOSDummy_placement = None, # None/'Up'/'Dn'/

            # NMOS Tr4
            _Tr4_NMOSNumberofGate=_TR4_NMOSNumberofGate,
            _Tr4_NMOSChannelWidth=_TRN0_N1_N4_ChannelWidth,
            _Tr4_NMOSChannellength=150,
            _Tr4_NMOSGateSpacing	= None,
            _Tr4_NMOSSDWidth			= None,
            _Tr4_NMOSXVT				= 'EG',
            _Tr4_NMOSPCCrit				= None,

            # Source_node_ViaM1M2
            _Tr4_NMOSSource_Via_TF = False,

            # Drain_node_ViaM1M2
            _Tr4_NMOSDrain_Via_TF = False,

            # POLY dummy setting
            _Tr4_NMOSDummy = True, # TF
            # if _PMOSDummy == True
            _Tr4_NMOSDummy_length = None, # None/Value
            _Tr4_NMOSDummy_placement = None, # None/'Up'/'Dn'/

            # N body ring(P1P2P4)
            _NumContTop_P1P2P4 = 3,
            _NumContBottom_P1P2P4=3,
            _NumContLeft_P1P2P4=3,
            _NumContRight_P1P2P4=3,

            # N body ring(P0P3)
            _NumContTop_P0P3 = 3,
            _NumContLeft_P0P3 = 3,
            _NumContRight_P0P3 = 3,

            # P body ring
            _NumContTop_Pbody = 3,
            _NumContBottom_Pbody=3,
            _NumContLeft_Pbody=3,
            _NumContRight_Pbody=3,

            # Res0
            _ResWidth_res0 = _Res_Width,
            _ResLength_res0 = _Res_Length,
            _CONUMX_res0 = None,
            _CONUMY_res0 = None,
            _SeriesStripes_res0 = 1,
            _ParallelStripes_res0 = 1, # 고정

            # Res1
            _ResWidth_res1=_Res_Width,
            _ResLength_res1=_Res_Length,
            _CONUMX_res1=None,
            _CONUMY_res1=None,
            _SeriesStripes_res1=1,
            _ParallelStripes_res1=1, # 고정

            # Cap0
            _Length_cap0=_Cap_Length,
            _LayoutOption_cap0=[2,3,4,5], # 고정
            _NumFigPair_cap0=_Cap_finger,

            _Array_cap0=1,  # number: 1xnumber
            _Cbot_Ctop_metalwidth_cap0=500,  # number

            # Cap1
            _Length_cap1=_Cap_Length,
            _LayoutOption_cap1=[2,3,4,5], # 고정
            _NumFigPair_cap1=_Cap_finger,

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
        LayoutObj = _TIA_P0P1P2P3P4N0N1N2N3N4_PNbodyring_YCH(_DesignParameter=None, _Name=cellname)
        LayoutObj._CalculateDesignParameter(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
        testStreamFile = open('./{}'.format(_fileName), 'wb')
        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        # print('###############      Sending to FTP Server...      ##################')
        # My = MyInfo_YCH.USER(DesignParameters._Technology)
        # Checker = DRCchecker_KJH0.DRCchecker_KJH0(
        #     username=My.ID,
        #     password=My.PW,
        #     WorkDir=My.Dir_Work,
        #     DRCrunDir=My.Dir_DRCrun,
        #     libname=libname,
        #     cellname=cellname,
        #     GDSDir=My.Dir_GDS
        # )
        # # Checker.lib_deletion()
        # Checker.cell_deletion()
        # Checker.Upload2FTP()
        # Checker.StreamIn(tech=DesignParameters._Technology)
        # Checker_KJH0.DRCchecker()
        print('#############################      Finished      ################################')
    # end of 'main():' ---------------------------------------------------------------------------------------------