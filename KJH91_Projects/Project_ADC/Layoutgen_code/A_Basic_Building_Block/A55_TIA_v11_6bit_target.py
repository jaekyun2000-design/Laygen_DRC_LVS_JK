from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC_EGFET

import numpy as np
import copy
import math
import time

from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A53_TIA_P0P1P2P3P4N0N1N2N3N4_PNbodyring

from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_opppcres_b
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_TIA_Pbodyring


from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2_YCH

from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A53_TIA_RCfeedback_2ndstage
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A53_TIA_RCfeedback_1ststage


## ########################################################################################################################################################## Class_HEADER
class _TIA_YCH(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(
        # first op-amp
        # PMOS
        _op1_Tr0_PMOSNumberofGate=None,
        _op1_Tr0_PMOSChannelWidth=None,
        _op1_Tr0_PMOSChannellength=None,
        _op1_Tr0_PMOSGateSpacing	= None,
        _op1_Tr0_PMOSSDWidth			= None,
        _op1_Tr0_PMOSXVT				= None,
        _op1_Tr0_PMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _op1_Tr0_PMOSSource_Via_TF = None,

        # Drain_node_ViaM1M2
        _op1_Tr0_PMOSDrain_Via_TF = None,

        # POLY dummy setting
        _op1_Tr0_PMOSDummy = None, # TF
        # if _PMOSDummy == True
        _op1_Tr0_PMOSDummy_length = None, # None/Value
        _op1_Tr0_PMOSDummy_placement = None, # None/Up/Dn/

        # PMOS
        _op1_Tr1_PMOSNumberofGate=45,
        _op1_Tr1_PMOSChannelWidth=6000,
        _op1_Tr1_PMOSChannellength=150,
        _op1_Tr1_PMOSGateSpacing	= None,
        _op1_Tr1_PMOSSDWidth			= None,
        _op1_Tr1_PMOSXVT				= 'EG',
        _op1_Tr1_PMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _op1_Tr1_PMOSSource_Via_TF = True,

        # Drain_node_ViaM1M2
        _op1_Tr1_PMOSDrain_Via_TF = True,

        # POLY dummy setting
        _op1_Tr1_PMOSDummy = True, # TF
        # if _PMOSDummy == True
        _op1_Tr1_PMOSDummy_length = None, # None/Value
        _op1_Tr1_PMOSDummy_placement = None, # None/'Up'/'Dn'/

        # PMOS
        _op1_Tr2_PMOSNumberofGate=None,
        _op1_Tr2_PMOSChannelWidth=None,
        _op1_Tr2_PMOSChannellength=None,
        _op1_Tr2_PMOSGateSpacing	= None,
        _op1_Tr2_PMOSSDWidth			= None,
        _op1_Tr2_PMOSXVT				= None,
        _op1_Tr2_PMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _op1_Tr2_PMOSSource_Via_TF = None,

        # Drain_node_ViaM1M2
        _op1_Tr2_PMOSDrain_Via_TF = None,

        # POLY dummy setting
        _op1_Tr2_PMOSDummy = None, # TF
        # if _PMOSDummy == True
        _op1_Tr2_PMOSDummy_length = None, # None/Value
        _op1_Tr2_PMOSDummy_placement = None, # None/Up/Dn/

        # PMOS
        _op1_Tr3_PMOSNumberofGate=None,
        _op1_Tr3_PMOSChannelWidth=None,
        _op1_Tr3_PMOSChannellength=None,
        _op1_Tr3_PMOSGateSpacing	= None,
        _op1_Tr3_PMOSSDWidth			= None,
        _op1_Tr3_PMOSXVT				= None,
        _op1_Tr3_PMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _op1_Tr3_PMOSSource_Via_TF = None,

        # Drain_node_ViaM1M2
        _op1_Tr3_PMOSDrain_Via_TF = None,

        # POLY dummy setting
        _op1_Tr3_PMOSDummy = None, # TF
        # if _PMOSDummy == True
        _op1_Tr3_PMOSDummy_length = None, # None/Value
        _op1_Tr3_PMOSDummy_placement = None, # None/Up/Dn/

        #PMOS
        _op1_Tr4_PMOSNumberofGate	= None,
        _op1_Tr4_PMOSChannelWidth	= None,
        _op1_Tr4_PMOSChannellength	= None,
        _op1_Tr4_PMOSGateSpacing		= None,
        _op1_Tr4_PMOSSDWidth			= None,
        _op1_Tr4_PMOSXVT				= None,
        _op1_Tr4_PMOSPCCrit				= None,

        #Source_node_ViaM1M2
        _op1_Tr4_PMOSSource_Via_TF = None,

        #Drain_node_ViaM1M2
        _op1_Tr4_PMOSDrain_Via_TF = None,

        #POLY dummy setting
        _op1_Tr4_PMOSDummy = None, #TF
            #if _PMOSDummy == True
        _op1_Tr4_PMOSDummy_length = None, #None/Value
        _op1_Tr4_PMOSDummy_placement = None, #None/Up/Dn/

        # NMOS Tr0
        _op1_Tr0_NMOSNumberofGate=15,
        _op1_Tr0_NMOSChannelWidth=3000,
        _op1_Tr0_NMOSChannellength=150,
        _op1_Tr0_NMOSGateSpacing=None,
        _op1_Tr0_NMOSSDWidth	= None,
        _op1_Tr0_NMOSXVT			= 'EG',
        _op1_Tr0_NMOSPCCrit			= None,

        # Source_node_ViaM1M2
        _op1_Tr0_NMOSSource_Via_TF= True,

        # Drain_node_ViaM1M2
        _op1_Tr0_NMOSDrain_Via_TF= True,

        # POLY dummy setting
        _op1_Tr0_NMOSDummy= True  , # TF
        # if _PMOSDummy == True
        _op1_Tr0_NMOSDummy_length = None, # None/Value
        _op1_Tr0_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        # NMOS Tr0
        _op1_Tr1_NMOSNumberofGate=15,
        _op1_Tr1_NMOSChannelWidth=3000,
        _op1_Tr1_NMOSChannellength=150,
        _op1_Tr1_NMOSGateSpacing	= None,
        _op1_Tr1_NMOSSDWidth			= None,
        _op1_Tr1_NMOSXVT				= 'EG',
        _op1_Tr1_NMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _op1_Tr1_NMOSSource_Via_TF = True,

        # Drain_node_ViaM1M2
        _op1_Tr1_NMOSDrain_Via_TF = True,

        # POLY dummy setting
        _op1_Tr1_NMOSDummy = True, # TF
        # if _PMOSDummy == True
        _op1_Tr1_NMOSDummy_length = None, # None/Value
        _op1_Tr1_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        # NMOS for VBN
        _op1_Tr2_NMOSNumberofGate=5,
        _op1_Tr2_NMOSChannelWidth=3000,
        _op1_Tr2_NMOSChannellength=150,
        _op1_Tr2_NMOSGateSpacing=None,
        _op1_Tr2_NMOSSDWidth	= None,
        _op1_Tr2_NMOSXVT			= 'EG',
        _op1_Tr2_NMOSPCCrit			= None,

        # Source_node_ViaM1M2
        _op1_Tr2_NMOSSource_Via_TF= True,

        # Drain_node_ViaM1M2
        _op1_Tr2_NMOSDrain_Via_TF= True,

        # POLY dummy setting
        _op1_Tr2_NMOSDummy= True  , # TF
        # if _PMOSDummy == True
        _op1_Tr2_NMOSDummy_length = None, # None/Value
        _op1_Tr2_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        # NMOS for VBP
        _op1_Tr3_NMOSNumberofGate=1,
        _op1_Tr3_NMOSChannelWidth=3000,
        _op1_Tr3_NMOSChannellength=150,
        _op1_Tr3_NMOSGateSpacing	= None,
        _op1_Tr3_NMOSSDWidth			= None,
        _op1_Tr3_NMOSXVT				= 'EG',
        _op1_Tr3_NMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _op1_Tr3_NMOSSource_Via_TF = True,

        # Drain_node_ViaM1M2
        _op1_Tr3_NMOSDrain_Via_TF = True,

        # POLY dummy setting
        _op1_Tr3_NMOSDummy = True, # TF
        # if _PMOSDummy == True
        _op1_Tr3_NMOSDummy_length = None, # None/Value
        _op1_Tr3_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        # NMOS 2nd Stage
        _op1_Tr4_NMOSNumberofGate=8,
        _op1_Tr4_NMOSChannelWidth=3000,
        _op1_Tr4_NMOSChannellength=150,
        _op1_Tr4_NMOSGateSpacing	= None,
        _op1_Tr4_NMOSSDWidth			= None,
        _op1_Tr4_NMOSXVT				= 'EG',
        _op1_Tr4_NMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _op1_Tr4_NMOSSource_Via_TF = True,

        # Drain_node_ViaM1M2
        _op1_Tr4_NMOSDrain_Via_TF = True,

        # POLY dummy setting
        _op1_Tr4_NMOSDummy = True, # TF
        # if _PMOSDummy == True
        _op1_Tr4_NMOSDummy_length = None, # None/Value
        _op1_Tr4_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        _op1_NumContTop_P1P2P4 = 3,
        _op1_NumContBottom_P1P2P4 = 3,
        _op1_NumContLeft_P1P2P4 = 3,
        _op1_NumContRight_P1P2P4 = 3,

        # N body ring(P0P3)
        _op1_NumContTop_P0P3=3,
        _op1_NumContLeft_P0P3=3,
        _op1_NumContRight_P0P3=3,

        # P body ring
        _op1_NumContTop_Pbody=3,
        _op1_NumContBottom_Pbody=3,
        _op1_NumContLeft_Pbody=3,
        _op1_NumContRight_Pbody=3,

        # Res0
        _op1_ResWidth_res0=400,
        _op1_ResLength_res0=508,
        _op1_CONUMX_res0=None,
        _op1_CONUMY_res0=None,
        _op1_SeriesStripes_res0=4,
        _op1_ParallelStripes_res0=1,

        # Res0
        _op1_ResWidth_res1=400,
        _op1_ResLength_res1=508,
        _op1_CONUMX_res1=None,
        _op1_CONUMY_res1=None,
        _op1_SeriesStripes_res1=4,
        _op1_ParallelStripes_res1=1,

        # Cap0
        _op1_Length_cap0=7800,
        _op1_LayoutOption_cap0=[2, 3, 4, 5],
        _op1_NumFigPair_cap0=50,

        _op1_Array_cap0=1,  # number: 1xnumber
        _op1_Cbot_Ctop_metalwidth_cap0=500,  # number

        # Cap1
        _op1_Length_cap1=7800,
        _op1_LayoutOption_cap1=[2, 3, 4, 5],
        _op1_NumFigPair_cap1=50,

        _op1_Array_cap1=1,  # number: 1xnumber
        _op1_Cbot_Ctop_metalwidth_cap1=500,  # number

        # second op-amp
        # PMOS
        _op2_Tr0_PMOSNumberofGate=None,
        _op2_Tr0_PMOSChannelWidth=None,
        _op2_Tr0_PMOSChannellength=None,
        _op2_Tr0_PMOSGateSpacing=None,
        _op2_Tr0_PMOSSDWidth	= None,
        _op2_Tr0_PMOSXVT			= None,
        _op2_Tr0_PMOSPCCrit			= None,

        # Source_node_ViaM1M2
        _op2_Tr0_PMOSSource_Via_TF= None,

        # Drain_node_ViaM1M2
        _op2_Tr0_PMOSDrain_Via_TF= None,

        # POLY dummy setting
        _op2_Tr0_PMOSDummy= None  , # TF
        # if _PMOSDummy == True
        _op2_Tr0_PMOSDummy_length = None, # None/Value
        _op2_Tr0_PMOSDummy_placement = None, # None/Up/Dn/

        # PMOS
        _op2_Tr1_PMOSNumberofGate=45,
        _op2_Tr1_PMOSChannelWidth=6000,
        _op2_Tr1_PMOSChannellength=150,
        _op2_Tr1_PMOSGateSpacing	= None,
        _op2_Tr1_PMOSSDWidth			= None,
        _op2_Tr1_PMOSXVT				= 'EG',
        _op2_Tr1_PMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _op2_Tr1_PMOSSource_Via_TF = True,

        # Drain_node_ViaM1M2
        _op2_Tr1_PMOSDrain_Via_TF = True,

        # POLY dummy setting
        _op2_Tr1_PMOSDummy = True, # TF
        # if _PMOSDummy == True
        _op2_Tr1_PMOSDummy_length = None, # None/Value
        _op2_Tr1_PMOSDummy_placement = None, # None/'Up'/'Dn'/

        # PMOS
        _op2_Tr2_PMOSNumberofGate=None,
        _op2_Tr2_PMOSChannelWidth=None,
        _op2_Tr2_PMOSChannellength=None,
        _op2_Tr2_PMOSGateSpacing	= None,
        _op2_Tr2_PMOSSDWidth			= None,
        _op2_Tr2_PMOSXVT				= None,
        _op2_Tr2_PMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _op2_Tr2_PMOSSource_Via_TF = None,

        # Drain_node_ViaM1M2
        _op2_Tr2_PMOSDrain_Via_TF = None,

        # POLY dummy setting
        _op2_Tr2_PMOSDummy = None, # TF
        # if _PMOSDummy == True
        _op2_Tr2_PMOSDummy_length = None, # None/Value
        _op2_Tr2_PMOSDummy_placement = None, # None/Up/Dn/

        # PMOS
        _op2_Tr3_PMOSNumberofGate=None,
        _op2_Tr3_PMOSChannelWidth=None,
        _op2_Tr3_PMOSChannellength=None,
        _op2_Tr3_PMOSGateSpacing	= None,
        _op2_Tr3_PMOSSDWidth			= None,
        _op2_Tr3_PMOSXVT				= None,
        _op2_Tr3_PMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _op2_Tr3_PMOSSource_Via_TF = None,

        # Drain_node_ViaM1M2
        _op2_Tr3_PMOSDrain_Via_TF = None,

        # POLY dummy setting
        _op2_Tr3_PMOSDummy = None, # TF
        # if _PMOSDummy == True
        _op2_Tr3_PMOSDummy_length = None, # None/Value
        _op2_Tr3_PMOSDummy_placement = None, # None/Up/Dn/

        # PMOS
        _op2_Tr4_PMOSNumberofGate	= None,
        _op2_Tr4_PMOSChannelWidth	= None,
        _op2_Tr4_PMOSChannellength	= None,
        _op2_Tr4_PMOSGateSpacing		= None,
        _op2_Tr4_PMOSSDWidth			= None,
        _op2_Tr4_PMOSXVT				= None,
        _op2_Tr4_PMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _op2_Tr4_PMOSSource_Via_TF = None,

        # Drain_node_ViaM1M2
        _op2_Tr4_PMOSDrain_Via_TF = None,

        # POLY dummy setting
        _op2_Tr4_PMOSDummy = None, # TF
        # if _PMOSDummy == True
        _op2_Tr4_PMOSDummy_length = None, # None/Value
        _op2_Tr4_PMOSDummy_placement = None, # None/Up/Dn/

        # NMOS Tr0
        _op2_Tr0_NMOSNumberofGate=15,
        _op2_Tr0_NMOSChannelWidth=3000,
        _op2_Tr0_NMOSChannellength=150,
        _op2_Tr0_NMOSGateSpacing=None,
        _op2_Tr0_NMOSSDWidth	= None,
        _op2_Tr0_NMOSXVT			= 'EG',
        _op2_Tr0_NMOSPCCrit			= None,

        # Source_node_ViaM1M2
        _op2_Tr0_NMOSSource_Via_TF= True,

        # Drain_node_ViaM1M2
        _op2_Tr0_NMOSDrain_Via_TF= True,

        # POLY dummy setting
        _op2_Tr0_NMOSDummy= True  , # TF
        # if _PMOSDummy == True
        _op2_Tr0_NMOSDummy_length = None, # None/Value
        _op2_Tr0_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        # NMOS Tr0
        _op2_Tr1_NMOSNumberofGate=15,
        _op2_Tr1_NMOSChannelWidth=3000,
        _op2_Tr1_NMOSChannellength=150,
        _op2_Tr1_NMOSGateSpacing	= None,
        _op2_Tr1_NMOSSDWidth			= None,
        _op2_Tr1_NMOSXVT				= 'EG',
        _op2_Tr1_NMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _op2_Tr1_NMOSSource_Via_TF = True,

        # Drain_node_ViaM1M2
        _op2_Tr1_NMOSDrain_Via_TF = True,

        # POLY dummy setting
        _op2_Tr1_NMOSDummy = True, # TF
        # if _PMOSDummy == True
        _op2_Tr1_NMOSDummy_length = None, # None/Value
        _op2_Tr1_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        # NMOS
        _op2_Tr2_NMOSNumberofGate=5,
        _op2_Tr2_NMOSChannelWidth=3000,
        _op2_Tr2_NMOSChannellength=150,
        _op2_Tr2_NMOSGateSpacing=None,
        _op2_Tr2_NMOSSDWidth	= None,
        _op2_Tr2_NMOSXVT			= 'EG',
        _op2_Tr2_NMOSPCCrit			= None,

        # Source_node_ViaM1M2
        _op2_Tr2_NMOSSource_Via_TF= True,

        # Drain_node_ViaM1M2
        _op2_Tr2_NMOSDrain_Via_TF= True,

        # POLY dummy setting
        _op2_Tr2_NMOSDummy= True  , # TF
        # if _PMOSDummy == True
        _op2_Tr2_NMOSDummy_length = None, # None/Value
        _op2_Tr2_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        # NMOS
        _op2_Tr3_NMOSNumberofGate=1,
        _op2_Tr3_NMOSChannelWidth=3000,
        _op2_Tr3_NMOSChannellength=150,
        _op2_Tr3_NMOSGateSpacing	= None,
        _op2_Tr3_NMOSSDWidth			= None,
        _op2_Tr3_NMOSXVT				= 'EG',
        _op2_Tr3_NMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _op2_Tr3_NMOSSource_Via_TF = True,

        # Drain_node_ViaM1M2
        _op2_Tr3_NMOSDrain_Via_TF = True,

        # POLY dummy setting
        _op2_Tr3_NMOSDummy = True, # TF
        # if _PMOSDummy == True
        _op2_Tr3_NMOSDummy_length = None, # None/Value
        _op2_Tr3_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        # NMOS Tr0
        _op2_Tr4_NMOSNumberofGate=8,
        _op2_Tr4_NMOSChannelWidth=3000,
        _op2_Tr4_NMOSChannellength=150,
        _op2_Tr4_NMOSGateSpacing	= None,
        _op2_Tr4_NMOSSDWidth			= None,
        _op2_Tr4_NMOSXVT				= 'EG',
        _op2_Tr4_NMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _op2_Tr4_NMOSSource_Via_TF = True,

        # Drain_node_ViaM1M2
        _op2_Tr4_NMOSDrain_Via_TF = True,

        # POLY dummy setting
        _op2_Tr4_NMOSDummy = True, # TF
        # if _PMOSDummy == True
        _op2_Tr4_NMOSDummy_length = None, # None/Value
        _op2_Tr4_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        _op2_NumContTop_P1P2P4 = 3,
        _op2_NumContBottom_P1P2P4 = 3,
        _op2_NumContLeft_P1P2P4 = 3,
        _op2_NumContRight_P1P2P4 = 3,

        # N body ring(P0P3)
        _op2_NumContTop_P0P3=3,
        _op2_NumContLeft_P0P3=3,
        _op2_NumContRight_P0P3=3,

        # P body ring
        _op2_NumContTop_Pbody=3,
        _op2_NumContBottom_Pbody=3,
        _op2_NumContLeft_Pbody=3,
        _op2_NumContRight_Pbody=3,

        # Res0
        _op2_ResWidth_res0=400,
        _op2_ResLength_res0=508,
        _op2_CONUMX_res0=None,
        _op2_CONUMY_res0=None,
        _op2_SeriesStripes_res0=4,
        _op2_ParallelStripes_res0=1,

        # Res0
        _op2_ResWidth_res1=400,
        _op2_ResLength_res1=508,
        _op2_CONUMX_res1=None,
        _op2_CONUMY_res1=None,
        _op2_SeriesStripes_res1=4,
        _op2_ParallelStripes_res1=1,

        # Cap0
        _op2_Length_cap0=7800,
        _op2_LayoutOption_cap0=[2, 3, 4, 5],
        _op2_NumFigPair_cap0=50,

        _op2_Array_cap0=1,  # number: 1xnumber
        _op2_Cbot_Ctop_metalwidth_cap0=500,  # number

        # Cap1
        _op2_Length_cap1=7800,
        _op2_LayoutOption_cap1=[2, 3, 4, 5],
        _op2_NumFigPair_cap1=50,

        _op2_Array_cap1=1,  # number: 1xnumber
        _op2_Cbot_Ctop_metalwidth_cap1=500,  # number


        # ResA
        _ResWidth_resA=1000,
        _ResLength_resA=2800,
        _CONUMX_resA=None,
        _CONUMY_resA=None,
        _SeriesStripes_resA=5,
        _ParallelStripes_resA=1,

        ### 2nd Feedback
        # Res_2nd
        _ResWidth_2nd=None,
        _ResLength_2nd=None,
        _CONUMX_2nd=None,
        _CONUMY_2nd=None,
        _SeriesStripes_2nd=None,
        _ParallelStripes_2nd=None,
        _Res_Port1Layer=None,
        _Res_Port2Layer=None,

        # Cap_2nd
        _Length_2nd=9000,
        _LayoutOption_2nd=[2, 3, 4],
        _NumFigPair_2nd=20,
        _Array_2nd_row=2,
        _Array_2nd_col=3,
        _Cbot_Ctop_metalwidth_2nd=500,

        ### 1st Feedback
        # Parallel Res
        _Par_ResWidth=None,
        _Par_ResLength=None,
        _Par_SeriesStripes=None,
        _Par_ParallelStripes=None,

        # Series Res
        _Ser_ResWidth=None,
        _Ser_ResLength=None,
        _Ser_SeriesStripes=None,
        _Ser_ParallelStripes=None,

        ### TG NMOS PMOS
        _TG_NumberofGate=None,  # number
        _TG_NMOSChannelWidth=None,  # number
        _TG_PMOSChannelWidth=None,
        _TG_Channellength=None,  # number
        _TG_XVT	= None  , # 'XVT' ex)SLVT LVT RVT HVT EG
        _INV_NumberofGate=None,
        _NMOS_Pbody_NumCont=None,
        _PMOS_Nbody_NumCont=None,

        _Parallel_Stack=None,

        # Cap_1st
        _Length_1st=9000,
        _LayoutOption_1st=[2, 3, 4],
        _NumFigPair_1st=20,
        _Array_1st_row=1,
        _Array_1st_col=1,
        _Cbot_Ctop_metalwidth_1st=500,

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
                                  # first op-amp
                                  # PMOS
                                  _op1_Tr0_PMOSNumberofGate=None,
                                  _op1_Tr0_PMOSChannelWidth=None,
                                  _op1_Tr0_PMOSChannellength=None,
                                  _op1_Tr0_PMOSGateSpacing=None,
                                  _op1_Tr0_PMOSSDWidth	= None,
                                  _op1_Tr0_PMOSXVT			= None,
                                  _op1_Tr0_PMOSPCCrit			= None,

                                  # Source_node_ViaM1M2
                                  _op1_Tr0_PMOSSource_Via_TF= None,

                                  # Drain_node_ViaM1M2
                                  _op1_Tr0_PMOSDrain_Via_TF= None,

                                  # POLY dummy setting
                                  _op1_Tr0_PMOSDummy= None  , # TF
                                  # if _PMOSDummy == True
                                  _op1_Tr0_PMOSDummy_length = None, # None/Value
                                  _op1_Tr0_PMOSDummy_placement = None, # None/Up/Dn/

                                  # PMOS
                                  _op1_Tr1_PMOSNumberofGate=45,
                                  _op1_Tr1_PMOSChannelWidth=6000,
                                  _op1_Tr1_PMOSChannellength=150,
                                  _op1_Tr1_PMOSGateSpacing	= None,
                                  _op1_Tr1_PMOSSDWidth			= None,
                                  _op1_Tr1_PMOSXVT				= 'EG',
                                  _op1_Tr1_PMOSPCCrit				= None,

                                  # Source_node_ViaM1M2
                                  _op1_Tr1_PMOSSource_Via_TF = True,

                                  # Drain_node_ViaM1M2
                                  _op1_Tr1_PMOSDrain_Via_TF = True,

                                  # POLY dummy setting
                                  _op1_Tr1_PMOSDummy = True, # TF
                                  # if _PMOSDummy == True
                                  _op1_Tr1_PMOSDummy_length = None, # None/Value
                                  _op1_Tr1_PMOSDummy_placement = None, # None/'Up'/'Dn'/

                                  # PMOS
                                  _op1_Tr2_PMOSNumberofGate=None,
                                  _op1_Tr2_PMOSChannelWidth=None,
                                  _op1_Tr2_PMOSChannellength=None,
                                  _op1_Tr2_PMOSGateSpacing	= None,
                                  _op1_Tr2_PMOSSDWidth			= None,
                                  _op1_Tr2_PMOSXVT				= None,
                                  _op1_Tr2_PMOSPCCrit				= None,

                                  # Source_node_ViaM1M2
                                  _op1_Tr2_PMOSSource_Via_TF = None,

                                  # Drain_node_ViaM1M2
                                  _op1_Tr2_PMOSDrain_Via_TF = None,

                                  # POLY dummy setting
                                  _op1_Tr2_PMOSDummy = None, # TF
                                  # if _PMOSDummy == True
                                  _op1_Tr2_PMOSDummy_length = None, # None/Value
                                  _op1_Tr2_PMOSDummy_placement = None, # None/Up/Dn/

                                  # PMOS
                                  _op1_Tr3_PMOSNumberofGate=None,
                                  _op1_Tr3_PMOSChannelWidth=None,
                                  _op1_Tr3_PMOSChannellength=None,
                                  _op1_Tr3_PMOSGateSpacing	= None,
                                  _op1_Tr3_PMOSSDWidth			= None,
                                  _op1_Tr3_PMOSXVT				= None,
                                  _op1_Tr3_PMOSPCCrit				= None,

                                  # Source_node_ViaM1M2
                                  _op1_Tr3_PMOSSource_Via_TF = None,

                                  # Drain_node_ViaM1M2
                                  _op1_Tr3_PMOSDrain_Via_TF = None,

                                  # POLY dummy setting
                                  _op1_Tr3_PMOSDummy = None, # TF
                                  # if _PMOSDummy == True
                                  _op1_Tr3_PMOSDummy_length = None, # None/Value
                                  _op1_Tr3_PMOSDummy_placement = None, # None/Up/Dn/

                                  # PMOS
                                  _op1_Tr4_PMOSNumberofGate	= None,
                                  _op1_Tr4_PMOSChannelWidth	= None,
                                  _op1_Tr4_PMOSChannellength	= None,
                                  _op1_Tr4_PMOSGateSpacing		= None,
                                  _op1_Tr4_PMOSSDWidth			= None,
                                  _op1_Tr4_PMOSXVT				= None,
                                  _op1_Tr4_PMOSPCCrit				= None,

                                  # Source_node_ViaM1M2
                                  _op1_Tr4_PMOSSource_Via_TF = None,

                                  # Drain_node_ViaM1M2
                                  _op1_Tr4_PMOSDrain_Via_TF = None,

                                  # POLY dummy setting
                                  _op1_Tr4_PMOSDummy = None, # TF
                                  # if _PMOSDummy == True
                                  _op1_Tr4_PMOSDummy_length = None, # None/Value
                                  _op1_Tr4_PMOSDummy_placement = None, # None/Up/Dn/

                                  # NMOS Tr0
                                  _op1_Tr0_NMOSNumberofGate=15,
                                  _op1_Tr0_NMOSChannelWidth=3000,
                                  _op1_Tr0_NMOSChannellength=150,
                                  _op1_Tr0_NMOSGateSpacing=None,
                                  _op1_Tr0_NMOSSDWidth	= None,
                                  _op1_Tr0_NMOSXVT			= 'EG',
                                  _op1_Tr0_NMOSPCCrit			= None,

                                  # Source_node_ViaM1M2
                                  _op1_Tr0_NMOSSource_Via_TF= True,

                                  # Drain_node_ViaM1M2
                                  _op1_Tr0_NMOSDrain_Via_TF= True,

                                  # POLY dummy setting
                                  _op1_Tr0_NMOSDummy= True  , # TF
                                  # if _PMOSDummy == True
                                  _op1_Tr0_NMOSDummy_length = None, # None/Value
                                  _op1_Tr0_NMOSDummy_placement = None, # None/'Up'/'Dn'/

                                  # NMOS Tr0
                                  _op1_Tr1_NMOSNumberofGate=15,
                                  _op1_Tr1_NMOSChannelWidth=3000,
                                  _op1_Tr1_NMOSChannellength=150,
                                  _op1_Tr1_NMOSGateSpacing	= None,
                                  _op1_Tr1_NMOSSDWidth			= None,
                                  _op1_Tr1_NMOSXVT				= 'EG',
                                  _op1_Tr1_NMOSPCCrit				= None,

                                  # Source_node_ViaM1M2
                                  _op1_Tr1_NMOSSource_Via_TF = True,

                                  # Drain_node_ViaM1M2
                                  _op1_Tr1_NMOSDrain_Via_TF = True,

                                  # POLY dummy setting
                                  _op1_Tr1_NMOSDummy = True, # TF
                                  # if _PMOSDummy == True
                                  _op1_Tr1_NMOSDummy_length = None, # None/Value
                                  _op1_Tr1_NMOSDummy_placement = None, # None/'Up'/'Dn'/

                                  # NMOS
                                  _op1_Tr2_NMOSNumberofGate=5,
                                  _op1_Tr2_NMOSChannelWidth=3000,
                                  _op1_Tr2_NMOSChannellength=150,
                                  _op1_Tr2_NMOSGateSpacing=None,
                                  _op1_Tr2_NMOSSDWidth	= None,
                                  _op1_Tr2_NMOSXVT			= 'EG',
                                  _op1_Tr2_NMOSPCCrit			= None,

                                  # Source_node_ViaM1M2
                                  _op1_Tr2_NMOSSource_Via_TF= True,

                                  # Drain_node_ViaM1M2
                                  _op1_Tr2_NMOSDrain_Via_TF= True,

                                  # POLY dummy setting
                                  _op1_Tr2_NMOSDummy= True  , # TF
                                  # if _PMOSDummy == True
                                  _op1_Tr2_NMOSDummy_length = None, # None/Value
                                  _op1_Tr2_NMOSDummy_placement = None, # None/'Up'/'Dn'/

                                  # NMOS
                                  _op1_Tr3_NMOSNumberofGate=1,
                                  _op1_Tr3_NMOSChannelWidth=3000,
                                  _op1_Tr3_NMOSChannellength=150,
                                  _op1_Tr3_NMOSGateSpacing	= None,
                                  _op1_Tr3_NMOSSDWidth			= None,
                                  _op1_Tr3_NMOSXVT				= 'EG',
                                  _op1_Tr3_NMOSPCCrit				= None,

                                  # Source_node_ViaM1M2
                                  _op1_Tr3_NMOSSource_Via_TF = True,

                                  # Drain_node_ViaM1M2
                                  _op1_Tr3_NMOSDrain_Via_TF = True,

                                  # POLY dummy setting
                                  _op1_Tr3_NMOSDummy = True, # TF
                                  # if _PMOSDummy == True
                                  _op1_Tr3_NMOSDummy_length = None, # None/Value
                                  _op1_Tr3_NMOSDummy_placement = None, # None/'Up'/'Dn'/

                                  # NMOS Tr0
                                  _op1_Tr4_NMOSNumberofGate=8,
                                  _op1_Tr4_NMOSChannelWidth=3000,
                                  _op1_Tr4_NMOSChannellength=150,
                                  _op1_Tr4_NMOSGateSpacing	= None,
                                  _op1_Tr4_NMOSSDWidth			= None,
                                  _op1_Tr4_NMOSXVT				= 'EG',
                                  _op1_Tr4_NMOSPCCrit				= None,

                                  # Source_node_ViaM1M2
                                  _op1_Tr4_NMOSSource_Via_TF = True,

                                  # Drain_node_ViaM1M2
                                  _op1_Tr4_NMOSDrain_Via_TF = True,

                                  # POLY dummy setting
                                  _op1_Tr4_NMOSDummy = True, # TF
                                  # if _PMOSDummy == True
                                  _op1_Tr4_NMOSDummy_length = None, # None/Value
                                  _op1_Tr4_NMOSDummy_placement = None, # None/'Up'/'Dn'/

                                  _op1_NumContTop_P1P2P4 = 3,
                                  _op1_NumContBottom_P1P2P4 = 3,
                                  _op1_NumContLeft_P1P2P4 = 3,
                                  _op1_NumContRight_P1P2P4 = 3,

                                  # N body ring(P0P3)
                                  _op1_NumContTop_P0P3=3,
                                  _op1_NumContLeft_P0P3=3,
                                  _op1_NumContRight_P0P3=3,

                                  # P body ring
                                  _op1_NumContTop_Pbody=3,
                                  _op1_NumContBottom_Pbody=3,
                                  _op1_NumContLeft_Pbody=3,
                                  _op1_NumContRight_Pbody=3,

                                  # Res0
                                  _op1_ResWidth_res0=400,
                                  _op1_ResLength_res0=508,
                                  _op1_CONUMX_res0=None,
                                  _op1_CONUMY_res0=None,
                                  _op1_SeriesStripes_res0=4,
                                  _op1_ParallelStripes_res0=1,

                                  # Res0
                                  _op1_ResWidth_res1=400,
                                  _op1_ResLength_res1=508,
                                  _op1_CONUMX_res1=None,
                                  _op1_CONUMY_res1=None,
                                  _op1_SeriesStripes_res1=4,
                                  _op1_ParallelStripes_res1=1,

                                  # Cap0
                                  _op1_Length_cap0=7800,
                                  _op1_LayoutOption_cap0=[2, 3, 4, 5],
                                  _op1_NumFigPair_cap0=50,

                                  _op1_Array_cap0=1,  # number: 1xnumber
                                  _op1_Cbot_Ctop_metalwidth_cap0=500,  # number

                                  # Cap1
                                  _op1_Length_cap1=7800,
                                  _op1_LayoutOption_cap1=[2, 3, 4, 5],
                                  _op1_NumFigPair_cap1=50,

                                  _op1_Array_cap1=1,  # number: 1xnumber
                                  _op1_Cbot_Ctop_metalwidth_cap1=500,  # number

                                  # second op-amp
                                  # PMOS
                                  _op2_Tr0_PMOSNumberofGate=None,
                                  _op2_Tr0_PMOSChannelWidth=None,
                                  _op2_Tr0_PMOSChannellength=None,
                                  _op2_Tr0_PMOSGateSpacing=None,
                                  _op2_Tr0_PMOSSDWidth	= None,
                                  _op2_Tr0_PMOSXVT			= None,
                                  _op2_Tr0_PMOSPCCrit			= None,

                                  # Source_node_ViaM1M2
                                  _op2_Tr0_PMOSSource_Via_TF= None,

                                  # Drain_node_ViaM1M2
                                  _op2_Tr0_PMOSDrain_Via_TF= None,

                                  # POLY dummy setting
                                  _op2_Tr0_PMOSDummy= None  , # TF
                                  # if _PMOSDummy == True
                                  _op2_Tr0_PMOSDummy_length = None, # None/Value
                                  _op2_Tr0_PMOSDummy_placement = None, # None/Up/Dn/

                                  # PMOS
                                  _op2_Tr1_PMOSNumberofGate=45,
                                  _op2_Tr1_PMOSChannelWidth=6000,
                                  _op2_Tr1_PMOSChannellength=150,
                                  _op2_Tr1_PMOSGateSpacing	= None,
                                  _op2_Tr1_PMOSSDWidth			= None,
                                  _op2_Tr1_PMOSXVT				= 'EG',
                                  _op2_Tr1_PMOSPCCrit				= None,

                                  # Source_node_ViaM1M2
                                  _op2_Tr1_PMOSSource_Via_TF = True,

                                  # Drain_node_ViaM1M2
                                  _op2_Tr1_PMOSDrain_Via_TF = True,

                                  # POLY dummy setting
                                  _op2_Tr1_PMOSDummy = True, # TF
                                  # if _PMOSDummy == True
                                  _op2_Tr1_PMOSDummy_length = None, # None/Value
                                  _op2_Tr1_PMOSDummy_placement = None, # None/'Up'/'Dn'/

                                  # PMOS
                                  _op2_Tr2_PMOSNumberofGate=None,
                                  _op2_Tr2_PMOSChannelWidth=None,
                                  _op2_Tr2_PMOSChannellength=None,
                                  _op2_Tr2_PMOSGateSpacing	= None,
                                  _op2_Tr2_PMOSSDWidth			= None,
                                  _op2_Tr2_PMOSXVT				= None,
                                  _op2_Tr2_PMOSPCCrit				= None,

                                  # Source_node_ViaM1M2
                                  _op2_Tr2_PMOSSource_Via_TF = None,

                                  # Drain_node_ViaM1M2
                                  _op2_Tr2_PMOSDrain_Via_TF = None,

                                  # POLY dummy setting
                                  _op2_Tr2_PMOSDummy = None, # TF
                                  # if _PMOSDummy == True
                                  _op2_Tr2_PMOSDummy_length = None, # None/Value
                                  _op2_Tr2_PMOSDummy_placement = None, # None/Up/Dn/

                                  # PMOS
                                  _op2_Tr3_PMOSNumberofGate=None,
                                  _op2_Tr3_PMOSChannelWidth=None,
                                  _op2_Tr3_PMOSChannellength=None,
                                  _op2_Tr3_PMOSGateSpacing	= None,
                                  _op2_Tr3_PMOSSDWidth			= None,
                                  _op2_Tr3_PMOSXVT				= None,
                                  _op2_Tr3_PMOSPCCrit				= None,

                                  # Source_node_ViaM1M2
                                  _op2_Tr3_PMOSSource_Via_TF = None,

                                  # Drain_node_ViaM1M2
                                  _op2_Tr3_PMOSDrain_Via_TF = None,

                                  # POLY dummy setting
                                  _op2_Tr3_PMOSDummy = None, # TF
                                  # if _PMOSDummy == True
                                  _op2_Tr3_PMOSDummy_length = None, # None/Value
                                  _op2_Tr3_PMOSDummy_placement = None, # None/Up/Dn/

                                  # PMOS
                                  _op2_Tr4_PMOSNumberofGate	= None,
                                  _op2_Tr4_PMOSChannelWidth	= None,
                                  _op2_Tr4_PMOSChannellength	= None,
                                  _op2_Tr4_PMOSGateSpacing		= None,
                                  _op2_Tr4_PMOSSDWidth			= None,
                                  _op2_Tr4_PMOSXVT				= None,
                                  _op2_Tr4_PMOSPCCrit				= None,

                                  # Source_node_ViaM1M2
                                  _op2_Tr4_PMOSSource_Via_TF = None,

                                  # Drain_node_ViaM1M2
                                  _op2_Tr4_PMOSDrain_Via_TF = None,

                                  # POLY dummy setting
                                  _op2_Tr4_PMOSDummy = None, # TF
                                  # if _PMOSDummy == True
                                  _op2_Tr4_PMOSDummy_length = None, # None/Value
                                  _op2_Tr4_PMOSDummy_placement = None, # None/Up/Dn/

                                  # NMOS Tr0
                                  _op2_Tr0_NMOSNumberofGate=15,
                                  _op2_Tr0_NMOSChannelWidth=3000,
                                  _op2_Tr0_NMOSChannellength=150,
                                  _op2_Tr0_NMOSGateSpacing=None,
                                  _op2_Tr0_NMOSSDWidth	= None,
                                  _op2_Tr0_NMOSXVT			= 'EG',
                                  _op2_Tr0_NMOSPCCrit			= None,

                                  # Source_node_ViaM1M2
                                  _op2_Tr0_NMOSSource_Via_TF= True,

                                  # Drain_node_ViaM1M2
                                  _op2_Tr0_NMOSDrain_Via_TF= True,

                                  # POLY dummy setting
                                  _op2_Tr0_NMOSDummy= True  , # TF
                                  # if _PMOSDummy == True
                                  _op2_Tr0_NMOSDummy_length = None, # None/Value
                                  _op2_Tr0_NMOSDummy_placement = None, # None/'Up'/'Dn'/

                                  # NMOS Tr0
                                  _op2_Tr1_NMOSNumberofGate=15,
                                  _op2_Tr1_NMOSChannelWidth=3000,
                                  _op2_Tr1_NMOSChannellength=150,
                                  _op2_Tr1_NMOSGateSpacing	= None,
                                  _op2_Tr1_NMOSSDWidth			= None,
                                  _op2_Tr1_NMOSXVT				= 'EG',
                                  _op2_Tr1_NMOSPCCrit				= None,

                                  # Source_node_ViaM1M2
                                  _op2_Tr1_NMOSSource_Via_TF = True,

                                  # Drain_node_ViaM1M2
                                  _op2_Tr1_NMOSDrain_Via_TF = True,

                                  # POLY dummy setting
                                  _op2_Tr1_NMOSDummy = True, # TF
                                  # if _PMOSDummy == True
                                  _op2_Tr1_NMOSDummy_length = None, # None/Value
                                  _op2_Tr1_NMOSDummy_placement = None, # None/'Up'/'Dn'/

                                  # NMOS
                                  _op2_Tr2_NMOSNumberofGate=5,
                                  _op2_Tr2_NMOSChannelWidth=3000,
                                  _op2_Tr2_NMOSChannellength=150,
                                  _op2_Tr2_NMOSGateSpacing=None,
                                  _op2_Tr2_NMOSSDWidth	= None,
                                  _op2_Tr2_NMOSXVT			= 'EG',
                                  _op2_Tr2_NMOSPCCrit			= None,

                                  # Source_node_ViaM1M2
                                  _op2_Tr2_NMOSSource_Via_TF= True,

                                  # Drain_node_ViaM1M2
                                  _op2_Tr2_NMOSDrain_Via_TF= True,

                                  # POLY dummy setting
                                  _op2_Tr2_NMOSDummy= True  , # TF
                                  # if _PMOSDummy == True
                                  _op2_Tr2_NMOSDummy_length = None, # None/Value
                                  _op2_Tr2_NMOSDummy_placement = None, # None/'Up'/'Dn'/

                                  # NMOS
                                  _op2_Tr3_NMOSNumberofGate=1,
                                  _op2_Tr3_NMOSChannelWidth=3000,
                                  _op2_Tr3_NMOSChannellength=150,
                                  _op2_Tr3_NMOSGateSpacing	= None,
                                  _op2_Tr3_NMOSSDWidth			= None,
                                  _op2_Tr3_NMOSXVT				= 'EG',
                                  _op2_Tr3_NMOSPCCrit				= None,

                                  # Source_node_ViaM1M2
                                  _op2_Tr3_NMOSSource_Via_TF = True,

                                  # Drain_node_ViaM1M2
                                  _op2_Tr3_NMOSDrain_Via_TF = True,

                                  # POLY dummy setting
                                  _op2_Tr3_NMOSDummy = True, # TF
                                  # if _PMOSDummy == True
                                  _op2_Tr3_NMOSDummy_length = None, # None/Value
                                  _op2_Tr3_NMOSDummy_placement = None, # None/'Up'/'Dn'/

                                  # NMOS Tr0
                                  _op2_Tr4_NMOSNumberofGate=8,
                                  _op2_Tr4_NMOSChannelWidth=3000,
                                  _op2_Tr4_NMOSChannellength=150,
                                  _op2_Tr4_NMOSGateSpacing	= None,
                                  _op2_Tr4_NMOSSDWidth			= None,
                                  _op2_Tr4_NMOSXVT				= 'EG',
                                  _op2_Tr4_NMOSPCCrit				= None,

                                  # Source_node_ViaM1M2
                                  _op2_Tr4_NMOSSource_Via_TF = True,

                                  # Drain_node_ViaM1M2
                                  _op2_Tr4_NMOSDrain_Via_TF = True,

                                  # POLY dummy setting
                                  _op2_Tr4_NMOSDummy = True, # TF
                                  # if _PMOSDummy == True
                                  _op2_Tr4_NMOSDummy_length = None, # None/Value
                                  _op2_Tr4_NMOSDummy_placement = None, # None/'Up'/'Dn'/

                                  _op2_NumContTop_P1P2P4 = 3,
                                  _op2_NumContBottom_P1P2P4 = 3,
                                  _op2_NumContLeft_P1P2P4 = 3,
                                  _op2_NumContRight_P1P2P4 = 3,

                                  # N body ring(P0P3)
                                  _op2_NumContTop_P0P3=3,
                                  _op2_NumContLeft_P0P3=3,
                                  _op2_NumContRight_P0P3=3,

                                  # P body ring
                                  _op2_NumContTop_Pbody=3,
                                  _op2_NumContBottom_Pbody=3,
                                  _op2_NumContLeft_Pbody=3,
                                  _op2_NumContRight_Pbody=3,

                                  # Res0
                                  _op2_ResWidth_res0=400,
                                  _op2_ResLength_res0=508,
                                  _op2_CONUMX_res0=None,
                                  _op2_CONUMY_res0=None,
                                  _op2_SeriesStripes_res0=4,
                                  _op2_ParallelStripes_res0=1,

                                  # Res0
                                  _op2_ResWidth_res1=400,
                                  _op2_ResLength_res1=508,
                                  _op2_CONUMX_res1=None,
                                  _op2_CONUMY_res1=None,
                                  _op2_SeriesStripes_res1=4,
                                  _op2_ParallelStripes_res1=1,

                                  # Cap0
                                  _op2_Length_cap0=7800,
                                  _op2_LayoutOption_cap0=[2, 3, 4, 5],
                                  _op2_NumFigPair_cap0=50,

                                  _op2_Array_cap0=1,  # number: 1xnumber
                                  _op2_Cbot_Ctop_metalwidth_cap0=500,  # number

                                  # Cap1
                                  _op2_Length_cap1=7800,
                                  _op2_LayoutOption_cap1=[2, 3, 4, 5],
                                  _op2_NumFigPair_cap1=50,

                                  _op2_Array_cap1=1,  # number: 1xnumber
                                  _op2_Cbot_Ctop_metalwidth_cap1=500,  # number


                                  # ResA
                                  _ResWidth_resA=1000,
                                  _ResLength_resA=2800,
                                  _CONUMX_resA=None,
                                  _CONUMY_resA=None,
                                  _SeriesStripes_resA=5,
                                  _ParallelStripes_resA=1,

                                  # 2nd Stage FB
                                  _ResWidth_2nd=None,
                                  _ResLength_2nd=None,
                                  _CONUMX_2nd=None,
                                  _CONUMY_2nd=None,
                                  _SeriesStripes_2nd=None,
                                  _ParallelStripes_2nd=None,
                                  _Res_Port1Layer=None,
                                  _Res_Port2Layer=None,

                                  # Cap_2nd
                                  _Length_2nd=9000,
                                  _LayoutOption_2nd=[2, 3, 4],
                                  _NumFigPair_2nd=20,
                                  _Array_2nd_row=2,
                                  _Array_2nd_col=3,
                                  _Cbot_Ctop_metalwidth_2nd=500,

                                  ### 1st Feedback
                                  # Parallel Res
                                  _Par_ResWidth=None,
                                  _Par_ResLength=None,
                                  _Par_SeriesStripes=None,
                                  _Par_ParallelStripes=None,

                                  # Series Res
                                  _Ser_ResWidth=None,
                                  _Ser_ResLength=None,
                                  _Ser_SeriesStripes=None,
                                  _Ser_ParallelStripes=None,

                                  ### TG NMOS PMOS
                                  _TG_NumberofGate=None,  # number
                                  _TG_NMOSChannelWidth=None,  # number
                                  _TG_PMOSChannelWidth=None,
                                  _TG_Channellength=None,  # number
                                  _TG_XVT=None,  # 'XVT' ex)SLVT LVT RVT HVT EG
                                  _INV_NumberofGate=None,
                                  _NMOS_Pbody_NumCont=None,
                                  _PMOS_Nbody_NumCont=None,

                                  _Parallel_Stack=None,

                                  # Cap_1st
                                  _Length_1st=9000,
                                  _LayoutOption_1st=[2, 3, 4],
                                  _NumFigPair_1st=20,
                                  _Array_1st_row=1,
                                  _Array_1st_col=1,
                                  _Cbot_Ctop_metalwidth_1st=500,

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
        _Caculation_Parameters = copy.deepcopy(A53_TIA_P0P1P2P3P4N0N1N2N3N4_PNbodyring._TIA_P0P1P2P3P4N0N1N2N3N4_PNbodyring_YCH._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr0_PMOSNumberofGate'] = _op1_Tr0_PMOSNumberofGate
        _Caculation_Parameters['_Tr0_PMOSChannelWidth'] = _op1_Tr0_PMOSChannelWidth
        _Caculation_Parameters['_Tr0_PMOSChannellength'] = _op1_Tr0_PMOSChannellength
        _Caculation_Parameters['_Tr0_PMOSGateSpacing'] = _op1_Tr0_PMOSGateSpacing
        _Caculation_Parameters['_Tr0_PMOSSDWidth'] = _op1_Tr0_PMOSSDWidth
        _Caculation_Parameters['_Tr0_PMOSXVT'] = _op1_Tr0_PMOSXVT
        _Caculation_Parameters['_Tr0_PMOSPCCrit'] = _op1_Tr0_PMOSPCCrit
        _Caculation_Parameters['_Tr0_PMOSSource_Via_TF'] = _op1_Tr0_PMOSSource_Via_TF
        _Caculation_Parameters['_Tr0_PMOSDrain_Via_TF'] = _op1_Tr0_PMOSDrain_Via_TF
        _Caculation_Parameters['_Tr0_PMOSDummy'] = _op1_Tr0_PMOSDummy
        _Caculation_Parameters['_Tr0_PMOSDummy_length'] = _op1_Tr0_PMOSDummy_length
        _Caculation_Parameters['_Tr0_PMOSDummy_placement'] = _op1_Tr0_PMOSDummy_placement

        _Caculation_Parameters['_Tr1_PMOSNumberofGate'] = _op1_Tr1_PMOSNumberofGate
        _Caculation_Parameters['_Tr1_PMOSChannelWidth'] = _op1_Tr1_PMOSChannelWidth
        _Caculation_Parameters['_Tr1_PMOSChannellength'] = _op1_Tr1_PMOSChannellength
        _Caculation_Parameters['_Tr1_PMOSGateSpacing'] = _op1_Tr1_PMOSGateSpacing
        _Caculation_Parameters['_Tr1_PMOSSDWidth'] = _op1_Tr1_PMOSSDWidth
        _Caculation_Parameters['_Tr1_PMOSXVT'] = _op1_Tr1_PMOSXVT
        _Caculation_Parameters['_Tr1_PMOSPCCrit'] = _op1_Tr1_PMOSPCCrit
        _Caculation_Parameters['_Tr1_PMOSSource_Via_TF'] = _op1_Tr1_PMOSSource_Via_TF
        _Caculation_Parameters['_Tr1_PMOSDrain_Via_TF'] = _op1_Tr1_PMOSDrain_Via_TF
        _Caculation_Parameters['_Tr1_PMOSDummy'] = _op1_Tr1_PMOSDummy
        _Caculation_Parameters['_Tr1_PMOSDummy_length'] = _op1_Tr1_PMOSDummy_length
        _Caculation_Parameters['_Tr1_PMOSDummy_placement'] = _op1_Tr1_PMOSDummy_placement

        _Caculation_Parameters['_Tr2_PMOSNumberofGate'] = _op1_Tr2_PMOSNumberofGate
        _Caculation_Parameters['_Tr2_PMOSChannelWidth'] = _op1_Tr2_PMOSChannelWidth
        _Caculation_Parameters['_Tr2_PMOSChannellength'] = _op1_Tr2_PMOSChannellength
        _Caculation_Parameters['_Tr2_PMOSGateSpacing'] = _op1_Tr2_PMOSGateSpacing
        _Caculation_Parameters['_Tr2_PMOSSDWidth'] = _op1_Tr2_PMOSSDWidth
        _Caculation_Parameters['_Tr2_PMOSXVT'] = _op1_Tr2_PMOSXVT
        _Caculation_Parameters['_Tr2_PMOSPCCrit'] = _op1_Tr2_PMOSPCCrit
        _Caculation_Parameters['_Tr2_PMOSSource_Via_TF'] = _op1_Tr2_PMOSSource_Via_TF
        _Caculation_Parameters['_Tr2_PMOSDrain_Via_TF'] = _op1_Tr2_PMOSDrain_Via_TF
        _Caculation_Parameters['_Tr2_PMOSDummy'] = _op1_Tr2_PMOSDummy
        _Caculation_Parameters['_Tr2_PMOSDummy_length'] = _op1_Tr2_PMOSDummy_length
        _Caculation_Parameters['_Tr2_PMOSDummy_placement'] = _op1_Tr2_PMOSDummy_placement

        _Caculation_Parameters['_Tr3_PMOSNumberofGate'] = _op1_Tr3_PMOSNumberofGate
        _Caculation_Parameters['_Tr3_PMOSChannelWidth'] = _op1_Tr3_PMOSChannelWidth
        _Caculation_Parameters['_Tr3_PMOSChannellength'] = _op1_Tr3_PMOSChannellength
        _Caculation_Parameters['_Tr3_PMOSGateSpacing'] = _op1_Tr3_PMOSGateSpacing
        _Caculation_Parameters['_Tr3_PMOSSDWidth'] = _op1_Tr3_PMOSSDWidth
        _Caculation_Parameters['_Tr3_PMOSXVT'] = _op1_Tr3_PMOSXVT
        _Caculation_Parameters['_Tr3_PMOSPCCrit'] = _op1_Tr3_PMOSPCCrit
        _Caculation_Parameters['_Tr3_PMOSSource_Via_TF'] = _op1_Tr3_PMOSSource_Via_TF
        _Caculation_Parameters['_Tr3_PMOSDrain_Via_TF'] = _op1_Tr3_PMOSDrain_Via_TF
        _Caculation_Parameters['_Tr3_PMOSDummy'] = _op1_Tr3_PMOSDummy
        _Caculation_Parameters['_Tr3_PMOSDummy_length'] = _op1_Tr3_PMOSDummy_length
        _Caculation_Parameters['_Tr3_PMOSDummy_placement'] = _op1_Tr3_PMOSDummy_placement

        _Caculation_Parameters['_Tr4_PMOSNumberofGate'] = _op1_Tr4_PMOSNumberofGate
        _Caculation_Parameters['_Tr4_PMOSChannelWidth'] = _op1_Tr4_PMOSChannelWidth
        _Caculation_Parameters['_Tr4_PMOSChannellength'] = _op1_Tr4_PMOSChannellength
        _Caculation_Parameters['_Tr4_PMOSGateSpacing'] = _op1_Tr4_PMOSGateSpacing
        _Caculation_Parameters['_Tr4_PMOSSDWidth'] = _op1_Tr4_PMOSSDWidth
        _Caculation_Parameters['_Tr4_PMOSXVT'] = _op1_Tr4_PMOSXVT
        _Caculation_Parameters['_Tr4_PMOSPCCrit'] = _op1_Tr4_PMOSPCCrit
        _Caculation_Parameters['_Tr4_PMOSSource_Via_TF'] = _op1_Tr4_PMOSSource_Via_TF
        _Caculation_Parameters['_Tr4_PMOSDrain_Via_TF'] = _op1_Tr4_PMOSDrain_Via_TF
        _Caculation_Parameters['_Tr4_PMOSDummy'] = _op1_Tr4_PMOSDummy
        _Caculation_Parameters['_Tr4_PMOSDummy_length'] = _op1_Tr4_PMOSDummy_length
        _Caculation_Parameters['_Tr4_PMOSDummy_placement'] = _op1_Tr4_PMOSDummy_placement

        _Caculation_Parameters['_Tr0_NMOSNumberofGate'] = _op1_Tr0_NMOSNumberofGate
        _Caculation_Parameters['_Tr0_NMOSChannelWidth'] = _op1_Tr0_NMOSChannelWidth
        _Caculation_Parameters['_Tr0_NMOSChannellength'] = _op1_Tr0_NMOSChannellength
        _Caculation_Parameters['_Tr0_NMOSGateSpacing'] = _op1_Tr0_NMOSGateSpacing
        _Caculation_Parameters['_Tr0_NMOSSDWidth'] = _op1_Tr0_NMOSSDWidth
        _Caculation_Parameters['_Tr0_NMOSXVT'] = _op1_Tr0_NMOSXVT
        _Caculation_Parameters['_Tr0_NMOSPCCrit'] = _op1_Tr0_NMOSPCCrit
        _Caculation_Parameters['_Tr0_NMOSSource_Via_TF'] = _op1_Tr0_NMOSSource_Via_TF
        _Caculation_Parameters['_Tr0_NMOSDrain_Via_TF'] = _op1_Tr0_NMOSDrain_Via_TF
        _Caculation_Parameters['_Tr0_NMOSDummy'] = _op1_Tr0_NMOSDummy
        _Caculation_Parameters['_Tr0_NMOSDummy_length'] = _op1_Tr0_NMOSDummy_length
        _Caculation_Parameters['_Tr0_NMOSDummy_placement'] = _op1_Tr0_NMOSDummy_placement

        _Caculation_Parameters['_Tr1_NMOSNumberofGate'] = _op1_Tr1_NMOSNumberofGate
        _Caculation_Parameters['_Tr1_NMOSChannelWidth'] = _op1_Tr1_NMOSChannelWidth
        _Caculation_Parameters['_Tr1_NMOSChannellength'] = _op1_Tr1_NMOSChannellength
        _Caculation_Parameters['_Tr1_NMOSGateSpacing'] = _op1_Tr1_NMOSGateSpacing
        _Caculation_Parameters['_Tr1_NMOSSDWidth'] = _op1_Tr1_NMOSSDWidth
        _Caculation_Parameters['_Tr1_NMOSXVT'] = _op1_Tr1_NMOSXVT
        _Caculation_Parameters['_Tr1_NMOSPCCrit'] = _op1_Tr1_NMOSPCCrit
        _Caculation_Parameters['_Tr1_NMOSSource_Via_TF'] = _op1_Tr1_NMOSSource_Via_TF
        _Caculation_Parameters['_Tr1_NMOSDrain_Via_TF'] = _op1_Tr1_NMOSDrain_Via_TF
        _Caculation_Parameters['_Tr1_NMOSDummy'] = _op1_Tr1_NMOSDummy
        _Caculation_Parameters['_Tr1_NMOSDummy_length'] = _op1_Tr1_NMOSDummy_length
        _Caculation_Parameters['_Tr1_NMOSDummy_placement'] = _op1_Tr1_NMOSDummy_placement

        _Caculation_Parameters['_Tr2_NMOSNumberofGate'] = _op1_Tr2_NMOSNumberofGate
        _Caculation_Parameters['_Tr2_NMOSChannelWidth'] = _op1_Tr2_NMOSChannelWidth
        _Caculation_Parameters['_Tr2_NMOSChannellength'] = _op1_Tr2_NMOSChannellength
        _Caculation_Parameters['_Tr2_NMOSGateSpacing'] = _op1_Tr2_NMOSGateSpacing
        _Caculation_Parameters['_Tr2_NMOSSDWidth'] = _op1_Tr2_NMOSSDWidth
        _Caculation_Parameters['_Tr2_NMOSXVT'] = _op1_Tr2_NMOSXVT
        _Caculation_Parameters['_Tr2_NMOSPCCrit'] = _op1_Tr2_NMOSPCCrit
        _Caculation_Parameters['_Tr2_NMOSSource_Via_TF'] = _op1_Tr2_NMOSSource_Via_TF
        _Caculation_Parameters['_Tr2_NMOSDrain_Via_TF'] = _op1_Tr2_NMOSDrain_Via_TF
        _Caculation_Parameters['_Tr2_NMOSDummy'] = _op1_Tr2_NMOSDummy
        _Caculation_Parameters['_Tr2_NMOSDummy_length'] = _op1_Tr2_NMOSDummy_length
        _Caculation_Parameters['_Tr2_NMOSDummy_placement'] = _op1_Tr2_NMOSDummy_placement

        _Caculation_Parameters['_Tr3_NMOSNumberofGate'] = _op1_Tr3_NMOSNumberofGate
        _Caculation_Parameters['_Tr3_NMOSChannelWidth'] = _op1_Tr3_NMOSChannelWidth
        _Caculation_Parameters['_Tr3_NMOSChannellength'] = _op1_Tr3_NMOSChannellength
        _Caculation_Parameters['_Tr3_NMOSGateSpacing'] = _op1_Tr3_NMOSGateSpacing
        _Caculation_Parameters['_Tr3_NMOSSDWidth'] = _op1_Tr3_NMOSSDWidth
        _Caculation_Parameters['_Tr3_NMOSXVT'] = _op1_Tr3_NMOSXVT
        _Caculation_Parameters['_Tr3_NMOSPCCrit'] = _op1_Tr3_NMOSPCCrit
        _Caculation_Parameters['_Tr3_NMOSSource_Via_TF'] = _op1_Tr3_NMOSSource_Via_TF
        _Caculation_Parameters['_Tr3_NMOSDrain_Via_TF'] = _op1_Tr3_NMOSDrain_Via_TF
        _Caculation_Parameters['_Tr3_NMOSDummy'] = _op1_Tr3_NMOSDummy
        _Caculation_Parameters['_Tr3_NMOSDummy_length'] = _op1_Tr3_NMOSDummy_length
        _Caculation_Parameters['_Tr3_NMOSDummy_placement'] = _op1_Tr3_NMOSDummy_placement

        _Caculation_Parameters['_Tr4_NMOSNumberofGate'] = _op1_Tr4_NMOSNumberofGate
        _Caculation_Parameters['_Tr4_NMOSChannelWidth'] = _op1_Tr4_NMOSChannelWidth
        _Caculation_Parameters['_Tr4_NMOSChannellength'] = _op1_Tr4_NMOSChannellength
        _Caculation_Parameters['_Tr4_NMOSGateSpacing'] = _op1_Tr4_NMOSGateSpacing
        _Caculation_Parameters['_Tr4_NMOSSDWidth'] = _op1_Tr4_NMOSSDWidth
        _Caculation_Parameters['_Tr4_NMOSXVT'] = _op1_Tr4_NMOSXVT
        _Caculation_Parameters['_Tr4_NMOSPCCrit'] = _op1_Tr4_NMOSPCCrit
        _Caculation_Parameters['_Tr4_NMOSSource_Via_TF'] = _op1_Tr4_NMOSSource_Via_TF
        _Caculation_Parameters['_Tr4_NMOSDrain_Via_TF'] = _op1_Tr4_NMOSDrain_Via_TF
        _Caculation_Parameters['_Tr4_NMOSDummy'] = _op1_Tr4_NMOSDummy
        _Caculation_Parameters['_Tr4_NMOSDummy_length'] = _op1_Tr4_NMOSDummy_length
        _Caculation_Parameters['_Tr4_NMOSDummy_placement'] = _op1_Tr4_NMOSDummy_placement

        _Caculation_Parameters['_NumContTop_P1P2P4'] = _op1_NumContTop_P1P2P4
        _Caculation_Parameters['_NumContBottom_P1P2P4'] = _op1_NumContBottom_P1P2P4
        _Caculation_Parameters['_NumContLeft_P1P2P4'] = _op1_NumContLeft_P1P2P4
        _Caculation_Parameters['_NumContRight_P1P2P4'] = _op1_NumContRight_P1P2P4

        _Caculation_Parameters['_NumContTop_P0P3'] = _op1_NumContTop_P0P3
        _Caculation_Parameters['_NumContLeft_P0P3'] = _op1_NumContLeft_P0P3
        _Caculation_Parameters['_NumContRight_P0P3'] = _op1_NumContRight_P0P3

        _Caculation_Parameters['_NumContTop_Pbody'] = _op1_NumContTop_Pbody
        _Caculation_Parameters['_NumContBottom_Pbody'] = _op1_NumContTop_Pbody
        _Caculation_Parameters['_NumContLeft_Pbody'] = _op1_NumContLeft_Pbody
        _Caculation_Parameters['_NumContRight_Pbody'] = _op1_NumContRight_Pbody

        _Caculation_Parameters['_ResWidth_res0'] = _op1_ResWidth_res0
        _Caculation_Parameters['_ResLength_res0'] = _op1_ResLength_res0
        _Caculation_Parameters['_CONUMX_res0'] = _op1_CONUMX_res0
        _Caculation_Parameters['_CONUMY_res0'] = _op1_CONUMY_res0
        _Caculation_Parameters['_SeriesStripes_res0'] = _op1_SeriesStripes_res0
        _Caculation_Parameters['_ParallelStripes_res0'] = _op1_ParallelStripes_res0

        _Caculation_Parameters['_ResWidth_res1'] = _op1_ResWidth_res1
        _Caculation_Parameters['_ResLength_res1'] = _op1_ResLength_res1
        _Caculation_Parameters['_CONUMX_res1'] = _op1_CONUMX_res1
        _Caculation_Parameters['_CONUMY_res1'] = _op1_CONUMY_res1
        _Caculation_Parameters['_SeriesStripes_res1'] = _op1_SeriesStripes_res1
        _Caculation_Parameters['_ParallelStripes_res1'] = _op1_ParallelStripes_res1

        _Caculation_Parameters['_Length_cap0'] = _op1_Length_cap0
        _Caculation_Parameters['_LayoutOption_cap0'] = _op1_LayoutOption_cap0
        _Caculation_Parameters['_NumFigPair_cap0'] = _op1_NumFigPair_cap0
        _Caculation_Parameters['_Array_cap0'] = _op1_Array_cap0
        _Caculation_Parameters['_Cbot_Ctop_metalwidth_cap0'] = _op1_Cbot_Ctop_metalwidth_cap0

        _Caculation_Parameters['_Length_cap1'] = _op1_Length_cap1
        _Caculation_Parameters['_LayoutOption_cap1'] = _op1_LayoutOption_cap1
        _Caculation_Parameters['_NumFigPair_cap1'] = _op1_NumFigPair_cap1
        _Caculation_Parameters['_Array_cap1'] = _op1_Array_cap1
        _Caculation_Parameters['_Cbot_Ctop_metalwidth_cap1'] = _op1_Cbot_Ctop_metalwidth_cap1


        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_amp1'] = self._SrefElementDeclaration(
            _DesignObj=A53_TIA_P0P1P2P3P4N0N1N2N3N4_PNbodyring._TIA_P0P1P2P3P4N0N1N2N3N4_PNbodyring_YCH(_DesignParameter=None,_Name='{}:SRF_amp1'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_amp1']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_amp1']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_amp1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_amp1']['_XYCoordinates'] = [[0, 0]]

        ## SREF Generation Resistor
        _Caculation_Parameters = copy.deepcopy(A50_opppcres_b._Opppcres_b_YCH._ParametersForDesignCalculation)
        _Caculation_Parameters['_ResWidth'] = _ResWidth_resA
        _Caculation_Parameters['_ResLength'] = _ResLength_resA
        _Caculation_Parameters['_CONUMX'] = _CONUMX_resA
        _Caculation_Parameters['_CONUMY'] = _CONUMY_resA
        _Caculation_Parameters['_SeriesStripes'] = _SeriesStripes_resA
        _Caculation_Parameters['_ParallelStripes'] = _ParallelStripes_resA

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_ResA'] = self._SrefElementDeclaration(
            _DesignObj=A50_opppcres_b._Opppcres_b_YCH(_DesignParameter=None, _Name='{}:SRF_ResA'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_ResA']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_ResA']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_ResA']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_ResA']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        # Calculate
        # Target_coord
        tmp11 = self.get_param_KJH4('SRF_amp1','SRF_Pbodyring', 'SRF_PbodyBottom', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        tmp12 = self.get_param_KJH4('SRF_amp1', 'BND_Metal6Layer_Connect_C0_C1_PortA_P4_N4_Drain')
        target_coordx = tmp11[0][0][0][0][0][0]['_XY_right'][0] + 2500
        target_coordy = tmp12[0][0][0]['_XY_up'][1]
        target_coord = [target_coordx, target_coordy]
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_ResA','_PRESLayer')
        approaching_coord = tmp2[0][0][0]['_XY_up_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_ResA')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_ResA']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Pbodyring
        ## SREF Generation Pbodyring
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A50_TIA_Pbodyring._PbodyRing._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_XlengthIntn'] = None
        _Caculation_Parameters['_YlengthIntn'] = None
        _Caculation_Parameters['_NumContTop'] = 2
        _Caculation_Parameters['_NumContBottom'] = 2
        _Caculation_Parameters['_NumContLeft'] = 2
        _Caculation_Parameters['_NumContRight'] = 2

        tmp1 = self.get_param_KJH4('SRF_ResA','_PRESLayer')


        _Caculation_Parameters['_XlengthIntn'] = abs(
            tmp1[0][0][0]['_XY_right'][0] - tmp1[0][0][0]['_XY_left'][0]) + 245 * 2
        _Caculation_Parameters['_YlengthIntn'] = abs(
            tmp1[0][0][0]['_XY_up'][1] - tmp1[0][0][0]['_XY_down'][1]) + 245 * 2

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Pbodyring_ResA'] = self._SrefElementDeclaration(
            _DesignObj=A50_TIA_Pbodyring._PbodyRing(_DesignParameter=None, _Name='{}:SRF_Pbodyring_ResA'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Pbodyring_ResA']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbodyring_ResA']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbodyring_ResA']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbodyring_ResA']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_ResA','_PRESLayer')
        target_coord = tmp1[0][0][0]['_XY_up']
        target_coord[1] = target_coord[1] + 245
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Pbodyring_ResA', 'SRF_PbodyTop', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0][0]['_XY_down']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pbodyring_ResA')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['SRF_Pbodyring_ResA']['_XYCoordinates'] = tmpXY

        # ################################################################################################################### amp1 vout ResA PortB connect METAL9(IB)
        # Define Boundary_element
        self._DesignParameter['BND_Metal9Layer_Connect_amp1_Vout_RA_PortB'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL9'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL9'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_ResA','_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_amp1', 'BND_Metal6Layer_Connect_C0_C1_PortA_P4_N4_Drain')
        # print(_SeriesStripes_resA)
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal9Layer_Connect_amp1_Vout_RA_PortB']['_YWidth'] = 2000

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal9Layer_Connect_amp1_Vout_RA_PortB']['_XWidth'] = abs(tmp1[0][_SeriesStripes_resA][0]['_XY_right'][0] - tmp2[0][0][0]['_XY_left'][0])

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal9Layer_Connect_amp1_Vout_RA_PortB']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_ResA','_Met1Layer')
        target_coord = tmp1[0][_SeriesStripes_resA][0]['_XY_right']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal9Layer_Connect_amp1_Vout_RA_PortB')
        approaching_coord = tmp2[0][0]['_XY_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal9Layer_Connect_amp1_Vout_RA_PortB')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal9Layer_Connect_amp1_Vout_RA_PortB']['_XYCoordinates'] = tmpXY

        # DRC 검증 완료 (4/10) IB via 박는거부터 시작
        ## ################################################################################################################### amp1 Vout connect ViaM7M9 (ViaM7-IB는 따로 해야함)
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 7
        _Caculation_Parameters['_Layer2'] = 9
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_amp1_Vout_ViaM7M9'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_amp1_Vout_ViaM7M9'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_amp1_Vout_ViaM7M9']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_amp1_Vout_ViaM7M9']['_Angle'] = 0

        # Calcuate _COY
        _Caculation_Parameters['_COY'] = 2

        # Calcuate _COX
        _Caculation_Parameters['_COX'] = 3

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_amp1_Vout_ViaM7M9']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_amp1_Vout_ViaM7M9']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_amp1', 'BND_Metal6Layer_Connect_C0_C1_PortA_P4_N4_Drain')
        target_coord = tmp1[0][0][0]['_XY_up']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_amp1_Vout_ViaM7M9', 'SRF_ViaM7M8', 'BND_Met7Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_amp1_Vout_ViaM7M9')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_amp1_Vout_ViaM7M9']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### amp1 Vout connect ViaM6M7
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 6
        _Caculation_Parameters['_Layer2'] = 7
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_amp1_Vout_ViaM6M7'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_amp1_Vout_ViaM6M7'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_amp1_Vout_ViaM6M7']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_amp1_Vout_ViaM6M7']['_Angle'] = 0

        # Calcuate _COX
        _Caculation_Parameters['_COX'] = 14

        # Calcuate _COY
        tmp1 = self.get_param_KJH4('SRF_amp1', 'BND_Metal6Layer_Connect_C0_C1_PortA_P4_N4_Drain')
        tmp2 = self.get_param_KJH4('SRF_amp1_Vout_ViaM7M9', 'SRF_ViaM7M8', 'BND_Met7Layer')
        M3_ywidth = abs(tmp1[0][0][0]['_XY_up'][1]-tmp2[0][0][0][0]['_XY_down'][1])
        Num_V1 = int(
            (M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COY'] = 2
        else:
            _Caculation_Parameters['_COY'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_amp1_Vout_ViaM6M7']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_amp1_Vout_ViaM6M7']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_amp1', 'BND_Metal6Layer_Connect_C0_C1_PortA_P4_N4_Drain')
        target_coord = tmp1[0][0][0]['_XY_up_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_amp1_Vout_ViaM6M7', 'SRF_ViaM6M7', 'BND_Met7Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_amp1_Vout_ViaM6M7')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_amp1_Vout_ViaM6M7']['_XYCoordinates'] = tmpXY

        # ################################################################################################################### ResA PortB METAL1 extension
        # Define Boundary_element
        self._DesignParameter['BND_Metal1Layer_RA_PortB_extension'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_ResA', '_Met1Layer')
        tmp2 = self.get_param_KJH4('BND_Metal9Layer_Connect_amp1_Vout_RA_PortB')
        # print(_SeriesStripes_resA)
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal1Layer_RA_PortB_extension']['_YWidth'] = abs(tmp1[0][_SeriesStripes_resA][0]['_XY_up'][1] - tmp2[0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal1Layer_RA_PortB_extension']['_XWidth'] = tmp1[0][_SeriesStripes_resA][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal1Layer_RA_PortB_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_ResA', '_Met1Layer')
        target_coord = tmp1[0][_SeriesStripes_resA][0]['_XY_up_right']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal1Layer_RA_PortB_extension')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal1Layer_RA_PortB_extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal1Layer_RA_PortB_extension']['_XYCoordinates'] = tmpXY

        # ################################################################################################################### ResA PortB METAL7
        # Define Boundary_element
        self._DesignParameter['BND_Metal7Layer_RA_PortB'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL7'][0],
            _Datatype=DesignParameters._LayerMapping['METAL7'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Metal1Layer_RA_PortB_extension')

        # print(_SeriesStripes_resA)
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal7Layer_RA_PortB']['_YWidth'] = tmp1[0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal7Layer_RA_PortB']['_XWidth'] = tmp1[0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal7Layer_RA_PortB']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal1Layer_RA_PortB_extension')
        target_coord = tmp1[0][0]['_XY_up_right']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal7Layer_RA_PortB')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal7Layer_RA_PortB')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal7Layer_RA_PortB']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### ResA PortB connect ViaM1M7
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 7
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_ResA_PortB_ViaM1M7'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_ResA_PortB_ViaM1M7'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_ResA_PortB_ViaM1M7']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_ResA_PortB_ViaM1M7']['_Angle'] = 0

        # Calcuate _COY
        _Caculation_Parameters['_COY'] = 7

        # Calcuate _COX
        tmp1 = self.get_param_KJH4('BND_Metal7Layer_RA_PortB')
        # tmp2 = self.get_param_KJH4('SRF_amp1_Vout_ViaM7M9', 'SRF_ViaM7M8', 'BND_Met7Layer')
        M3_xwidth = tmp1[0][0]['_Xwidth']
        Num_V1 = int(
            (M3_xwidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COX'] = 2
        else:
            _Caculation_Parameters['_COX'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_ResA_PortB_ViaM1M7']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_ResA_PortB_ViaM1M7']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal7Layer_RA_PortB')
        target_coord = tmp1[0][0]['_XY_down_right']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_ResA_PortB_ViaM1M7', 'SRF_ViaM6M7', 'BND_Met7Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_ResA_PortB_ViaM1M7')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_ResA_PortB_ViaM1M7']['_XYCoordinates'] = tmpXY

        # ################################################################################################################### ResA PortB METAL7
        # Define Boundary_element
        self._DesignParameter['BND_Metal7Layer_RA_PortB_extension'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL7'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL7'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Metal9Layer_Connect_amp1_Vout_RA_PortB')

        # print(_SeriesStripes_resA)
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal7Layer_RA_PortB_extension']['_YWidth'] = tmp1[0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal7Layer_RA_PortB_extension']['_XWidth'] = tmp1[0][0]['_Ywidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal7Layer_RA_PortB_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal9Layer_Connect_amp1_Vout_RA_PortB')
        target_coord = tmp1[0][0]['_XY_up_right']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal7Layer_RA_PortB_extension')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal7Layer_RA_PortB_extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal7Layer_RA_PortB_extension']['_XYCoordinates'] = tmpXY

        # ################################################################################################################### ResA PortB METAL8
        # Define Boundary_element
        self._DesignParameter['BND_Metal8Layer_RA_PortB_extension'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['METAL8'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['METAL8'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Metal7Layer_RA_PortB_extension')

        # print(_SeriesStripes_resA)
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal8Layer_RA_PortB_extension']['_YWidth'] = tmp1[0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal8Layer_RA_PortB_extension']['_XWidth'] = tmp1[0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal8Layer_RA_PortB_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal7Layer_RA_PortB_extension')
        target_coord = tmp1[0][0]['_XY_up_right']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal8Layer_RA_PortB_extension')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal8Layer_RA_PortB_extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal8Layer_RA_PortB_extension']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### ResA PortB connect ViaM7M9
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 7
        _Caculation_Parameters['_Layer2'] = 9
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_ResA_PortB_ViaM7M9'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_ResA_PortB_ViaM7M9'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_ResA_PortB_ViaM7M9']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_ResA_PortB_ViaM7M9']['_Angle'] = 0

        # Calcuate _COY
        _Caculation_Parameters['_COY'] = 2

        # Calcuate _COX
        # tmp1 = self.get_param_KJH4('BND_Metal7Layer_RA_PortB')
        # # tmp2 = self.get_param_KJH4('SRF_amp1_Vout_ViaM7M9', 'SRF_ViaM7M8', 'BND_Met7Layer')
        # M3_xwidth = tmp1[0][0]['_Xwidth']
        # Num_V1 = int(
        #     (M3_xwidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))
        # # Define Num of COY
        # if Num_V1 < 2:
        #     _Caculation_Parameters['_COX'] = 2
        # else:
        #     _Caculation_Parameters['_COX'] = Num_V1
        _Caculation_Parameters['_COX'] = 2

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_ResA_PortB_ViaM7M9']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_ResA_PortB_ViaM7M9']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal8Layer_RA_PortB_extension')
        target_coord = tmp1[0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_ResA_PortB_ViaM7M9', 'SRF_ViaM7M8', 'BND_Met7Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_ResA_PortB_ViaM7M9')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_ResA_PortB_ViaM7M9']['_XYCoordinates'] = tmpXY

        # DRC, LVS 검증 완료(04/12)

        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A53_TIA_P0P1P2P3P4N0N1N2N3N4_PNbodyring._TIA_P0P1P2P3P4N0N1N2N3N4_PNbodyring_YCH._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr0_PMOSNumberofGate'] = _op2_Tr0_PMOSNumberofGate
        _Caculation_Parameters['_Tr0_PMOSChannelWidth'] = _op2_Tr0_PMOSChannelWidth
        _Caculation_Parameters['_Tr0_PMOSChannellength'] = _op2_Tr0_PMOSChannellength
        _Caculation_Parameters['_Tr0_PMOSGateSpacing'] = _op2_Tr0_PMOSGateSpacing
        _Caculation_Parameters['_Tr0_PMOSSDWidth'] = _op2_Tr0_PMOSSDWidth
        _Caculation_Parameters['_Tr0_PMOSXVT'] = _op2_Tr0_PMOSXVT
        _Caculation_Parameters['_Tr0_PMOSPCCrit'] = _op2_Tr0_PMOSPCCrit
        _Caculation_Parameters['_Tr0_PMOSSource_Via_TF'] = _op2_Tr0_PMOSSource_Via_TF
        _Caculation_Parameters['_Tr0_PMOSDrain_Via_TF'] = _op2_Tr0_PMOSDrain_Via_TF
        _Caculation_Parameters['_Tr0_PMOSDummy'] = _op2_Tr0_PMOSDummy
        _Caculation_Parameters['_Tr0_PMOSDummy_length'] = _op2_Tr0_PMOSDummy_length
        _Caculation_Parameters['_Tr0_PMOSDummy_placement'] = _op2_Tr0_PMOSDummy_placement

        _Caculation_Parameters['_Tr1_PMOSNumberofGate'] = _op2_Tr1_PMOSNumberofGate
        _Caculation_Parameters['_Tr1_PMOSChannelWidth'] = _op2_Tr1_PMOSChannelWidth
        _Caculation_Parameters['_Tr1_PMOSChannellength'] = _op2_Tr1_PMOSChannellength
        _Caculation_Parameters['_Tr1_PMOSGateSpacing'] = _op2_Tr1_PMOSGateSpacing
        _Caculation_Parameters['_Tr1_PMOSSDWidth'] = _op2_Tr1_PMOSSDWidth
        _Caculation_Parameters['_Tr1_PMOSXVT'] = _op2_Tr1_PMOSXVT
        _Caculation_Parameters['_Tr1_PMOSPCCrit'] = _op2_Tr1_PMOSPCCrit
        _Caculation_Parameters['_Tr1_PMOSSource_Via_TF'] = _op2_Tr1_PMOSSource_Via_TF
        _Caculation_Parameters['_Tr1_PMOSDrain_Via_TF'] = _op2_Tr1_PMOSDrain_Via_TF
        _Caculation_Parameters['_Tr1_PMOSDummy'] = _op2_Tr1_PMOSDummy
        _Caculation_Parameters['_Tr1_PMOSDummy_length'] = _op2_Tr1_PMOSDummy_length
        _Caculation_Parameters['_Tr1_PMOSDummy_placement'] = _op2_Tr1_PMOSDummy_placement

        _Caculation_Parameters['_Tr2_PMOSNumberofGate'] = _op2_Tr2_PMOSNumberofGate
        _Caculation_Parameters['_Tr2_PMOSChannelWidth'] = _op2_Tr2_PMOSChannelWidth
        _Caculation_Parameters['_Tr2_PMOSChannellength'] = _op2_Tr2_PMOSChannellength
        _Caculation_Parameters['_Tr2_PMOSGateSpacing'] = _op2_Tr2_PMOSGateSpacing
        _Caculation_Parameters['_Tr2_PMOSSDWidth'] = _op2_Tr2_PMOSSDWidth
        _Caculation_Parameters['_Tr2_PMOSXVT'] = _op2_Tr2_PMOSXVT
        _Caculation_Parameters['_Tr2_PMOSPCCrit'] = _op2_Tr2_PMOSPCCrit
        _Caculation_Parameters['_Tr2_PMOSSource_Via_TF'] = _op2_Tr2_PMOSSource_Via_TF
        _Caculation_Parameters['_Tr2_PMOSDrain_Via_TF'] = _op2_Tr2_PMOSDrain_Via_TF
        _Caculation_Parameters['_Tr2_PMOSDummy'] = _op2_Tr2_PMOSDummy
        _Caculation_Parameters['_Tr2_PMOSDummy_length'] = _op2_Tr2_PMOSDummy_length
        _Caculation_Parameters['_Tr2_PMOSDummy_placement'] = _op2_Tr2_PMOSDummy_placement

        _Caculation_Parameters['_Tr3_PMOSNumberofGate'] = _op2_Tr3_PMOSNumberofGate
        _Caculation_Parameters['_Tr3_PMOSChannelWidth'] = _op2_Tr3_PMOSChannelWidth
        _Caculation_Parameters['_Tr3_PMOSChannellength'] = _op2_Tr3_PMOSChannellength
        _Caculation_Parameters['_Tr3_PMOSGateSpacing'] = _op2_Tr3_PMOSGateSpacing
        _Caculation_Parameters['_Tr3_PMOSSDWidth'] = _op2_Tr3_PMOSSDWidth
        _Caculation_Parameters['_Tr3_PMOSXVT'] = _op2_Tr3_PMOSXVT
        _Caculation_Parameters['_Tr3_PMOSPCCrit'] = _op2_Tr3_PMOSPCCrit
        _Caculation_Parameters['_Tr3_PMOSSource_Via_TF'] = _op2_Tr3_PMOSSource_Via_TF
        _Caculation_Parameters['_Tr3_PMOSDrain_Via_TF'] = _op2_Tr3_PMOSDrain_Via_TF
        _Caculation_Parameters['_Tr3_PMOSDummy'] = _op2_Tr3_PMOSDummy
        _Caculation_Parameters['_Tr3_PMOSDummy_length'] = _op2_Tr3_PMOSDummy_length
        _Caculation_Parameters['_Tr3_PMOSDummy_placement'] = _op2_Tr3_PMOSDummy_placement

        _Caculation_Parameters['_Tr4_PMOSNumberofGate'] = _op2_Tr4_PMOSNumberofGate
        _Caculation_Parameters['_Tr4_PMOSChannelWidth'] = _op2_Tr4_PMOSChannelWidth
        _Caculation_Parameters['_Tr4_PMOSChannellength'] = _op2_Tr4_PMOSChannellength
        _Caculation_Parameters['_Tr4_PMOSGateSpacing'] = _op2_Tr4_PMOSGateSpacing
        _Caculation_Parameters['_Tr4_PMOSSDWidth'] = _op2_Tr4_PMOSSDWidth
        _Caculation_Parameters['_Tr4_PMOSXVT'] = _op2_Tr4_PMOSXVT
        _Caculation_Parameters['_Tr4_PMOSPCCrit'] = _op2_Tr4_PMOSPCCrit
        _Caculation_Parameters['_Tr4_PMOSSource_Via_TF'] = _op2_Tr4_PMOSSource_Via_TF
        _Caculation_Parameters['_Tr4_PMOSDrain_Via_TF'] = _op2_Tr4_PMOSDrain_Via_TF
        _Caculation_Parameters['_Tr4_PMOSDummy'] = _op2_Tr4_PMOSDummy
        _Caculation_Parameters['_Tr4_PMOSDummy_length'] = _op2_Tr4_PMOSDummy_length
        _Caculation_Parameters['_Tr4_PMOSDummy_placement'] = _op2_Tr4_PMOSDummy_placement

        _Caculation_Parameters['_Tr0_NMOSNumberofGate'] = _op2_Tr0_NMOSNumberofGate
        _Caculation_Parameters['_Tr0_NMOSChannelWidth'] = _op2_Tr0_NMOSChannelWidth
        _Caculation_Parameters['_Tr0_NMOSChannellength'] = _op2_Tr0_NMOSChannellength
        _Caculation_Parameters['_Tr0_NMOSGateSpacing'] = _op2_Tr0_NMOSGateSpacing
        _Caculation_Parameters['_Tr0_NMOSSDWidth'] = _op2_Tr0_NMOSSDWidth
        _Caculation_Parameters['_Tr0_NMOSXVT'] = _op2_Tr0_NMOSXVT
        _Caculation_Parameters['_Tr0_NMOSPCCrit'] = _op2_Tr0_NMOSPCCrit
        _Caculation_Parameters['_Tr0_NMOSSource_Via_TF'] = _op2_Tr0_NMOSSource_Via_TF
        _Caculation_Parameters['_Tr0_NMOSDrain_Via_TF'] = _op2_Tr0_NMOSDrain_Via_TF
        _Caculation_Parameters['_Tr0_NMOSDummy'] = _op2_Tr0_NMOSDummy
        _Caculation_Parameters['_Tr0_NMOSDummy_length'] = _op2_Tr0_NMOSDummy_length
        _Caculation_Parameters['_Tr0_NMOSDummy_placement'] = _op2_Tr0_NMOSDummy_placement

        _Caculation_Parameters['_Tr1_NMOSNumberofGate'] = _op2_Tr1_NMOSNumberofGate
        _Caculation_Parameters['_Tr1_NMOSChannelWidth'] = _op2_Tr1_NMOSChannelWidth
        _Caculation_Parameters['_Tr1_NMOSChannellength'] = _op2_Tr1_NMOSChannellength
        _Caculation_Parameters['_Tr1_NMOSGateSpacing'] = _op2_Tr1_NMOSGateSpacing
        _Caculation_Parameters['_Tr1_NMOSSDWidth'] = _op2_Tr1_NMOSSDWidth
        _Caculation_Parameters['_Tr1_NMOSXVT'] = _op2_Tr1_NMOSXVT
        _Caculation_Parameters['_Tr1_NMOSPCCrit'] = _op2_Tr1_NMOSPCCrit
        _Caculation_Parameters['_Tr1_NMOSSource_Via_TF'] = _op2_Tr1_NMOSSource_Via_TF
        _Caculation_Parameters['_Tr1_NMOSDrain_Via_TF'] = _op2_Tr1_NMOSDrain_Via_TF
        _Caculation_Parameters['_Tr1_NMOSDummy'] = _op2_Tr1_NMOSDummy
        _Caculation_Parameters['_Tr1_NMOSDummy_length'] = _op2_Tr1_NMOSDummy_length
        _Caculation_Parameters['_Tr1_NMOSDummy_placement'] = _op2_Tr1_NMOSDummy_placement

        _Caculation_Parameters['_Tr2_NMOSNumberofGate'] = _op2_Tr2_NMOSNumberofGate
        _Caculation_Parameters['_Tr2_NMOSChannelWidth'] = _op2_Tr2_NMOSChannelWidth
        _Caculation_Parameters['_Tr2_NMOSChannellength'] = _op2_Tr2_NMOSChannellength
        _Caculation_Parameters['_Tr2_NMOSGateSpacing'] = _op2_Tr2_NMOSGateSpacing
        _Caculation_Parameters['_Tr2_NMOSSDWidth'] = _op2_Tr2_NMOSSDWidth
        _Caculation_Parameters['_Tr2_NMOSXVT'] = _op2_Tr2_NMOSXVT
        _Caculation_Parameters['_Tr2_NMOSPCCrit'] = _op2_Tr2_NMOSPCCrit
        _Caculation_Parameters['_Tr2_NMOSSource_Via_TF'] = _op2_Tr2_NMOSSource_Via_TF
        _Caculation_Parameters['_Tr2_NMOSDrain_Via_TF'] = _op2_Tr2_NMOSDrain_Via_TF
        _Caculation_Parameters['_Tr2_NMOSDummy'] = _op2_Tr2_NMOSDummy
        _Caculation_Parameters['_Tr2_NMOSDummy_length'] = _op2_Tr2_NMOSDummy_length
        _Caculation_Parameters['_Tr2_NMOSDummy_placement'] = _op2_Tr2_NMOSDummy_placement

        _Caculation_Parameters['_Tr3_NMOSNumberofGate'] = _op2_Tr3_NMOSNumberofGate
        _Caculation_Parameters['_Tr3_NMOSChannelWidth'] = _op2_Tr3_NMOSChannelWidth
        _Caculation_Parameters['_Tr3_NMOSChannellength'] = _op2_Tr3_NMOSChannellength
        _Caculation_Parameters['_Tr3_NMOSGateSpacing'] = _op2_Tr3_NMOSGateSpacing
        _Caculation_Parameters['_Tr3_NMOSSDWidth'] = _op2_Tr3_NMOSSDWidth
        _Caculation_Parameters['_Tr3_NMOSXVT'] = _op2_Tr3_NMOSXVT
        _Caculation_Parameters['_Tr3_NMOSPCCrit'] = _op2_Tr3_NMOSPCCrit
        _Caculation_Parameters['_Tr3_NMOSSource_Via_TF'] = _op2_Tr3_NMOSSource_Via_TF
        _Caculation_Parameters['_Tr3_NMOSDrain_Via_TF'] = _op2_Tr3_NMOSDrain_Via_TF
        _Caculation_Parameters['_Tr3_NMOSDummy'] = _op2_Tr3_NMOSDummy
        _Caculation_Parameters['_Tr3_NMOSDummy_length'] = _op2_Tr3_NMOSDummy_length
        _Caculation_Parameters['_Tr3_NMOSDummy_placement'] = _op2_Tr3_NMOSDummy_placement

        _Caculation_Parameters['_Tr4_NMOSNumberofGate'] = _op2_Tr4_NMOSNumberofGate
        _Caculation_Parameters['_Tr4_NMOSChannelWidth'] = _op2_Tr4_NMOSChannelWidth
        _Caculation_Parameters['_Tr4_NMOSChannellength'] = _op2_Tr4_NMOSChannellength
        _Caculation_Parameters['_Tr4_NMOSGateSpacing'] = _op2_Tr4_NMOSGateSpacing
        _Caculation_Parameters['_Tr4_NMOSSDWidth'] = _op2_Tr4_NMOSSDWidth
        _Caculation_Parameters['_Tr4_NMOSXVT'] = _op2_Tr4_NMOSXVT
        _Caculation_Parameters['_Tr4_NMOSPCCrit'] = _op2_Tr4_NMOSPCCrit
        _Caculation_Parameters['_Tr4_NMOSSource_Via_TF'] = _op2_Tr4_NMOSSource_Via_TF
        _Caculation_Parameters['_Tr4_NMOSDrain_Via_TF'] = _op2_Tr4_NMOSDrain_Via_TF
        _Caculation_Parameters['_Tr4_NMOSDummy'] = _op2_Tr4_NMOSDummy
        _Caculation_Parameters['_Tr4_NMOSDummy_length'] = _op2_Tr4_NMOSDummy_length
        _Caculation_Parameters['_Tr4_NMOSDummy_placement'] = _op2_Tr4_NMOSDummy_placement

        _Caculation_Parameters['_NumContTop_P1P2P4'] = _op2_NumContTop_P1P2P4
        _Caculation_Parameters['_NumContBottom_P1P2P4'] = _op2_NumContBottom_P1P2P4
        _Caculation_Parameters['_NumContLeft_P1P2P4'] = _op2_NumContLeft_P1P2P4
        _Caculation_Parameters['_NumContRight_P1P2P4'] = _op2_NumContRight_P1P2P4

        _Caculation_Parameters['_NumContTop_P0P3'] = _op2_NumContTop_P0P3
        _Caculation_Parameters['_NumContLeft_P0P3'] = _op2_NumContLeft_P0P3
        _Caculation_Parameters['_NumContRight_P0P3'] = _op2_NumContRight_P0P3

        _Caculation_Parameters['_NumContTop_Pbody'] = _op2_NumContTop_Pbody
        _Caculation_Parameters['_NumContBottom_Pbody'] = _op2_NumContTop_Pbody
        _Caculation_Parameters['_NumContLeft_Pbody'] = _op2_NumContLeft_Pbody
        _Caculation_Parameters['_NumContRight_Pbody'] = _op2_NumContRight_Pbody

        _Caculation_Parameters['_ResWidth_res0'] = _op2_ResWidth_res0
        _Caculation_Parameters['_ResLength_res0'] = _op2_ResLength_res0
        _Caculation_Parameters['_CONUMX_res0'] = _op2_CONUMX_res0
        _Caculation_Parameters['_CONUMY_res0'] = _op2_CONUMY_res0
        _Caculation_Parameters['_SeriesStripes_res0'] = _op2_SeriesStripes_res0
        _Caculation_Parameters['_ParallelStripes_res0'] = _op2_ParallelStripes_res0

        _Caculation_Parameters['_ResWidth_res1'] = _op2_ResWidth_res1
        _Caculation_Parameters['_ResLength_res1'] = _op2_ResLength_res1
        _Caculation_Parameters['_CONUMX_res1'] = _op2_CONUMX_res1
        _Caculation_Parameters['_CONUMY_res1'] = _op2_CONUMY_res1
        _Caculation_Parameters['_SeriesStripes_res1'] = _op2_SeriesStripes_res1
        _Caculation_Parameters['_ParallelStripes_res1'] = _op2_ParallelStripes_res1

        _Caculation_Parameters['_Length_cap0'] = _op2_Length_cap0
        _Caculation_Parameters['_LayoutOption_cap0'] = _op2_LayoutOption_cap0
        _Caculation_Parameters['_NumFigPair_cap0'] = _op2_NumFigPair_cap0
        _Caculation_Parameters['_Array_cap0'] = _op2_Array_cap0
        _Caculation_Parameters['_Cbot_Ctop_metalwidth_cap0'] = _op2_Cbot_Ctop_metalwidth_cap0

        _Caculation_Parameters['_Length_cap1'] = _op2_Length_cap1
        _Caculation_Parameters['_LayoutOption_cap1'] = _op2_LayoutOption_cap1
        _Caculation_Parameters['_NumFigPair_cap1'] = _op2_NumFigPair_cap1
        _Caculation_Parameters['_Array_cap1'] = _op2_Array_cap1
        _Caculation_Parameters['_Cbot_Ctop_metalwidth_cap1'] = _op2_Cbot_Ctop_metalwidth_cap1

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_amp2'] = self._SrefElementDeclaration(
            _DesignObj=A53_TIA_P0P1P2P3P4N0N1N2N3N4_PNbodyring._TIA_P0P1P2P3P4N0N1N2N3N4_PNbodyring_YCH(
                _DesignParameter=None, _Name='{}:SRF_amp2'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_amp2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_amp2']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_amp2']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_amp2']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        # Calculate
        # Target_coord
        tmp11 = self.get_param_KJH4('SRF_amp1','SRF_Pbodyring','SRF_PbodyRight','SRF_PbodyContactPhyLen','BND_Met1Layer')
        tmp12 = self.get_param_KJH4('SRF_ResA', '_PRESLayer')
        target_coordx = tmp12[0][0][0]['_XY_right'][0] + 2500
        target_coordy = tmp11[0][0][0][0][0][0]['_XY_down_right'][1]
        target_coord = [target_coordx, target_coordy]
        # Approaching_coord
        tmp21 = self.get_param_KJH4('SRF_amp2','SRF_Pbodyring', 'SRF_PbodyBottom', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        tmp22 = self.get_param_KJH4('SRF_amp1', 'SRF_Pbodyring', 'SRF_PbodyLeft', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coordx = tmp21[0][0][0][0][0][0]['_XY_left'][0]
        approaching_coordy = tmp22[0][0][0][0][0][0]['_XY_down_left'][1]
        approaching_coord = [approaching_coordx, approaching_coordy]
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_amp2')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_amp2']['_XYCoordinates'] = tmpXY

        # DRC 검증 완료
        # ################################################################################################################### amp2 vinn ResA PortA connect METAL9(IB)
        # Define Boundary_element
        self._DesignParameter['BND_Metal9Layer_Connect_amp2_Vinn_RA_PortA'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL9'][0],
            _Datatype=DesignParameters._LayerMapping['METAL9'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_ResA', '_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_amp2','SRF_Pmos_Tr1Tr2Tr4_Nbodyring','SRF_Pmos_Tr1Tr2Tr4','SRF_Pmos_Tr1','BND_Metal3Layer_Hrz_Gate')
        # print(_SeriesStripes_resA)
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal9Layer_Connect_amp2_Vinn_RA_PortA']['_YWidth'] = 2000

        # Define Boundary_element _XWidth
        if (_SeriesStripes_resA % 2 == 0):
            self._DesignParameter['BND_Metal9Layer_Connect_amp2_Vinn_RA_PortA']['_XWidth'] = abs(
                tmp1[0][2*_SeriesStripes_resA-1][0]['_XY_left'][0] - tmp2[0][0][0][0][0][0]['_XY_right'][0])
        else:
            self._DesignParameter['BND_Metal9Layer_Connect_amp2_Vinn_RA_PortA']['_XWidth'] = abs(
                tmp1[0][_SeriesStripes_resA-1][0]['_XY_left'][0] - tmp2[0][0][0][0][0][0]['_XY_right'][0])


        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal9Layer_Connect_amp2_Vinn_RA_PortA']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_amp2','SRF_Pmos_Tr1Tr2Tr4_Nbodyring','SRF_Pmos_Tr1Tr2Tr4','SRF_Pmos_Tr1','BND_Metal3Layer_Hrz_Gate')
        target_coord = tmp1[0][0][0][0][0][0]['_XY_right']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal9Layer_Connect_amp2_Vinn_RA_PortA')
        approaching_coord = tmp2[0][0]['_XY_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal9Layer_Connect_amp2_Vinn_RA_PortA')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal9Layer_Connect_amp2_Vinn_RA_PortA']['_XYCoordinates'] = tmpXY

        # ################################################################################################################### ResA PortA METAL1 extension
        # Define Boundary_element
        self._DesignParameter['BND_Metal1Layer_RA_PortA_extension'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_ResA', '_Met1Layer')
        tmp2 = self.get_param_KJH4('BND_Metal9Layer_Connect_amp2_Vinn_RA_PortA')
        # print(_SeriesStripes_resA)
        if (_SeriesStripes_resA % 2 ==0):
            # Define Boundary_element _YWidth
            self._DesignParameter['BND_Metal1Layer_RA_PortA_extension']['_YWidth'] = abs(
                tmp1[0][2*_SeriesStripes_resA-1][0]['_XY_up'][1] - tmp2[0][0]['_XY_down'][1])
        else:
            self._DesignParameter['BND_Metal1Layer_RA_PortA_extension']['_YWidth'] = abs(
                tmp1[0][_SeriesStripes_resA-1][0]['_XY_down'][1] - tmp2[0][0]['_XY_up'][1])

        if (_SeriesStripes_resA % 2 ==0):
            # Define Boundary_element _XWidth
            self._DesignParameter['BND_Metal1Layer_RA_PortA_extension']['_XWidth'] = tmp1[0][2*_SeriesStripes_resA-1][0]['_Xwidth']
        else:
            self._DesignParameter['BND_Metal1Layer_RA_PortA_extension']['_XWidth'] = tmp1[0][_SeriesStripes_resA - 1][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal1Layer_RA_PortA_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        if (_SeriesStripes_resA % 2 ==0):
            tmp1 = self.get_param_KJH4('SRF_ResA', '_Met1Layer')
            target_coord = tmp1[0][2*_SeriesStripes_resA-1][0]['_XY_up_left']
        else:
            tmp1 = self.get_param_KJH4('SRF_ResA', '_Met1Layer')
            target_coord = tmp1[0][_SeriesStripes_resA-1][0]['_XY_down_left']

        # Approaching_coord
        if (_SeriesStripes_resA % 2 ==0):
            tmp2 = self.get_param_KJH4('BND_Metal1Layer_RA_PortA_extension')
            approaching_coord = tmp2[0][0]['_XY_up_left']
        else:
            tmp2 = self.get_param_KJH4('BND_Metal1Layer_RA_PortA_extension')
            approaching_coord = tmp2[0][0]['_XY_down_left']

        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal1Layer_RA_PortA_extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal1Layer_RA_PortA_extension']['_XYCoordinates'] = tmpXY

        # ################################################################################################################### ResA PortA METAL7
        # Define Boundary_element
        self._DesignParameter['BND_Metal7Layer_RA_PortA'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL7'][0],
            _Datatype=DesignParameters._LayerMapping['METAL7'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Metal1Layer_RA_PortA_extension')

        # print(_SeriesStripes_resA)
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal7Layer_RA_PortA']['_YWidth'] = tmp1[0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal7Layer_RA_PortA']['_XWidth'] = tmp1[0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal7Layer_RA_PortA']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal1Layer_RA_PortA_extension')
        target_coord = tmp1[0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal7Layer_RA_PortA')
        approaching_coord = tmp2[0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal7Layer_RA_PortA')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal7Layer_RA_PortA']['_XYCoordinates'] = tmpXY

        #DRC 검증 완료
        ## ################################################################################################################### ResA PortA connect ViaM1M7
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 7
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_ResA_PortA_ViaM1M7'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_ResA_PortA_ViaM1M7'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_ResA_PortA_ViaM1M7']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_ResA_PortA_ViaM1M7']['_Angle'] = 0

        # Calcuate _COY
        _Caculation_Parameters['_COY'] = 6

        # Calcuate _COX
        tmp1 = self.get_param_KJH4('BND_Metal7Layer_RA_PortA')
        # tmp2 = self.get_param_KJH4('SRF_amp1_Vout_ViaM7M9', 'SRF_ViaM7M8', 'BND_Met7Layer')
        M3_xwidth = tmp1[0][0]['_Xwidth']
        Num_V1 = int(
            (M3_xwidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COX'] = 2
        else:
            _Caculation_Parameters['_COX'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_ResA_PortA_ViaM1M7']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_ResA_PortA_ViaM1M7']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        if (_SeriesStripes_resA % 2 == 0):
            tmp1 = self.get_param_KJH4('BND_Metal7Layer_RA_PortA')
            target_coord = tmp1[0][0]['_XY_up_left']
        else:
            tmp1 = self.get_param_KJH4('BND_Metal7Layer_RA_PortA')
            target_coord = tmp1[0][0]['_XY_down_left']
        # Approaching_coord
        if (_SeriesStripes_resA % 2 == 0):
            tmp2 = self.get_param_KJH4('SRF_ResA_PortA_ViaM1M7', 'SRF_ViaM6M7', 'BND_Met7Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
        else:
            tmp2 = self.get_param_KJH4('SRF_ResA_PortA_ViaM1M7', 'SRF_ViaM6M7', 'BND_Met7Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_down_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_ResA_PortA_ViaM1M7')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_ResA_PortA_ViaM1M7']['_XYCoordinates'] = tmpXY

        # ################################################################################################################### ResA PortA METAL7
        # Define Boundary_element
        self._DesignParameter['BND_Metal7Layer_RA_PortA_extension'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL7'][0],
            _Datatype=DesignParameters._LayerMapping['METAL7'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Metal9Layer_Connect_amp2_Vinn_RA_PortA')

        # print(_SeriesStripes_resA)
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal7Layer_RA_PortA_extension']['_YWidth'] = tmp1[0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal7Layer_RA_PortA_extension']['_XWidth'] = tmp1[0][0]['_Ywidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal7Layer_RA_PortA_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal9Layer_Connect_amp2_Vinn_RA_PortA')
        target_coord = tmp1[0][0]['_XY_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal7Layer_RA_PortA_extension')
        approaching_coord = tmp2[0][0]['_XY_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal7Layer_RA_PortA_extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal7Layer_RA_PortA_extension']['_XYCoordinates'] = tmpXY

        # ################################################################################################################### ResA PortA METAL8
        # Define Boundary_element
        self._DesignParameter['BND_Metal8Layer_RA_PortA_extension'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL8'][0],
            _Datatype=DesignParameters._LayerMapping['METAL8'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Metal7Layer_RA_PortA_extension')

        # print(_SeriesStripes_resA)
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal8Layer_RA_PortA_extension']['_YWidth'] = tmp1[0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal8Layer_RA_PortA_extension']['_XWidth'] = tmp1[0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal8Layer_RA_PortA_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal7Layer_RA_PortA_extension')
        target_coord = tmp1[0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal8Layer_RA_PortA_extension')
        approaching_coord = tmp2[0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal8Layer_RA_PortA_extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal8Layer_RA_PortA_extension']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### ResA PortA connect ViaM7M9
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 7
        _Caculation_Parameters['_Layer2'] = 9
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_ResA_PortA_ViaM7M9'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_ResA_PortA_ViaM7M9'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_ResA_PortA_ViaM7M9']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_ResA_PortA_ViaM7M9']['_Angle'] = 0

        # Calcuate _COY
        _Caculation_Parameters['_COY'] = 2

        # Calcuate _COX
        # tmp1 = self.get_param_KJH4('BND_Metal7Layer_RA_PortB')
        # # tmp2 = self.get_param_KJH4('SRF_amp1_Vout_ViaM7M9', 'SRF_ViaM7M8', 'BND_Met7Layer')
        # M3_xwidth = tmp1[0][0]['_Xwidth']
        # Num_V1 = int(
        #     (M3_xwidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))
        # # Define Num of COY
        # if Num_V1 < 2:
        #     _Caculation_Parameters['_COX'] = 2
        # else:
        #     _Caculation_Parameters['_COX'] = Num_V1
        _Caculation_Parameters['_COX'] = 2

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_ResA_PortA_ViaM7M9']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_ResA_PortA_ViaM7M9']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal8Layer_RA_PortA_extension')
        target_coord = tmp1[0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_ResA_PortA_ViaM7M9', 'SRF_ViaM7M8', 'BND_Met7Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_ResA_PortA_ViaM7M9')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_ResA_PortA_ViaM7M9']['_XYCoordinates'] = tmpXY

        # DRC 검증 완료 (04/12), 04/13까지 amp 2개랑 사이에 저항 routing 마무리하기 (DRC, LVS)
        # ################################################################################################################### Amp2 Vinn METAL7
        # Define Boundary_element
        self._DesignParameter['BND_Metal7Layer_Amp2_Vinn'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL7'][0],
            _Datatype=DesignParameters._LayerMapping['METAL7'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_amp2','SRF_Pmos_Tr1Tr2Tr4_Nbodyring','SRF_Pmos_Tr1Tr2Tr4','SRF_Pmos_Tr1','BND_Metal4Layer_Hrz_Gate')

        # print(_SeriesStripes_resA)
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal7Layer_Amp2_Vinn']['_YWidth'] = tmp1[0][0][0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal7Layer_Amp2_Vinn']['_XWidth'] = tmp1[0][0][0][0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal7Layer_Amp2_Vinn']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_amp2','SRF_Pmos_Tr1Tr2Tr4_Nbodyring','SRF_Pmos_Tr1Tr2Tr4','SRF_Pmos_Tr1','BND_Metal4Layer_Hrz_Gate')
        target_coord = tmp1[0][0][0][0][0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal7Layer_Amp2_Vinn')
        approaching_coord = tmp2[0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal7Layer_Amp2_Vinn')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal7Layer_Amp2_Vinn']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Amp2 Vinn connect ViaM4M7
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 4
        _Caculation_Parameters['_Layer2'] = 7
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Amp2_Vinn_ViaM4M7'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_Amp2_Vinn_ViaM4M7'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Amp2_Vinn_ViaM4M7']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Amp2_Vinn_ViaM4M7']['_Angle'] = 0

        # Calcuate _COY
        _Caculation_Parameters['_COY'] = 4

        # Calcuate _COX
        # tmp1 = self.get_param_KJH4('BND_Metal7Layer_RA_PortB')
        # # tmp2 = self.get_param_KJH4('SRF_amp1_Vout_ViaM7M9', 'SRF_ViaM7M8', 'BND_Met7Layer')
        # M3_xwidth = tmp1[0][0]['_Xwidth']
        # Num_V1 = int(
        #     (M3_xwidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))
        # # Define Num of COY
        # if Num_V1 < 2:
        #     _Caculation_Parameters['_COX'] = 2
        # else:
        #     _Caculation_Parameters['_COX'] = Num_V1
        _Caculation_Parameters['_COX'] = 8

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Amp2_Vinn_ViaM4M7']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Amp2_Vinn_ViaM4M7']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal7Layer_Amp2_Vinn')
        target_coord = tmp1[0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Amp2_Vinn_ViaM4M7', 'SRF_ViaM6M7', 'BND_Met7Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Amp2_Vinn_ViaM4M7')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Amp2_Vinn_ViaM4M7']['_XYCoordinates'] = tmpXY

        # ################################################################################################################### Amp2 Vinn METAL8
        # Define Boundary_element
        self._DesignParameter['BND_Metal8Layer_Amp2_Vinn'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL8'][0],
            _Datatype=DesignParameters._LayerMapping['METAL8'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Metal9Layer_Connect_amp2_Vinn_RA_PortA')

        # print(_SeriesStripes_resA)
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal8Layer_Amp2_Vinn']['_YWidth'] = tmp1[0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal8Layer_Amp2_Vinn']['_XWidth'] = tmp1[0][0]['_Ywidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal8Layer_Amp2_Vinn']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp11 = self.get_param_KJH4('SRF_Amp2_Vinn_ViaM4M7', 'SRF_ViaM6M7', 'BND_Met7Layer')
        tmp12 = self.get_param_KJH4('BND_Metal9Layer_Connect_amp2_Vinn_RA_PortA')
        target_coordx = tmp11[0][0][0][0]['_XY_left'][0]
        target_coordy = tmp12[0][0]['_XY_cent'][1]
        target_coord = [target_coordx, target_coordy]
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal8Layer_Amp2_Vinn')
        approaching_coord = tmp2[0][0]['_XY_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal8Layer_Amp2_Vinn')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal8Layer_Amp2_Vinn']['_XYCoordinates'] = tmpXY

        # ################################################################################################################### Amp2 Vinn METAL7_extension
        # Define Boundary_element
        self._DesignParameter['BND_Metal7Layer_Amp2_Vinn_extension'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL7'][0],
            _Datatype=DesignParameters._LayerMapping['METAL7'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Metal8Layer_Amp2_Vinn')

        # print(_SeriesStripes_resA)
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal7Layer_Amp2_Vinn_extension']['_YWidth'] = tmp1[0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal7Layer_Amp2_Vinn_extension']['_XWidth'] = tmp1[0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal7Layer_Amp2_Vinn_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal8Layer_Amp2_Vinn')
        target_coord = tmp1[0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal7Layer_Amp2_Vinn_extension')
        approaching_coord = tmp2[0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal7Layer_Amp2_Vinn_extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal7Layer_Amp2_Vinn_extension']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### amp2 Vinn connect ViaM7M9 (ViaM7-IB는 따로 해야함)
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 7
        _Caculation_Parameters['_Layer2'] = 9
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_amp2_Vinn_ViaM7M9'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_amp2_Vinn_ViaM7M9'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_amp2_Vinn_ViaM7M9']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_amp2_Vinn_ViaM7M9']['_Angle'] = 0

        # Calcuate _COY
        _Caculation_Parameters['_COY'] = 2

        # Calcuate _COX
        _Caculation_Parameters['_COX'] = 2

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_amp2_Vinn_ViaM7M9']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_amp2_Vinn_ViaM7M9']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Metal7Layer_Amp2_Vinn_extension')
        target_coord = tmp1[0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_amp2_Vinn_ViaM7M9', 'SRF_ViaM7M8', 'BND_Met7Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_amp2_Vinn_ViaM7M9')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_amp2_Vinn_ViaM7M9']['_XYCoordinates'] = tmpXY

        _Caculation_Parameters = copy.deepcopy(A53_TIA_RCfeedback_2ndstage._TIA_RCfeedback_2ndstage._ParametersForDesignCalculation)
        _Caculation_Parameters['_ResWidth_2nd'] = _ResWidth_2nd
        _Caculation_Parameters['_ResLength_2nd'] = _ResLength_2nd
        _Caculation_Parameters['_CONUMX_2nd'] = _CONUMX_2nd
        _Caculation_Parameters['_CONUMY_2nd'] = _CONUMY_2nd
        _Caculation_Parameters['_SeriesStripes_2nd'] = _SeriesStripes_2nd
        _Caculation_Parameters['_ParallelStripes_2nd'] = _ParallelStripes_2nd
        _Caculation_Parameters['_Res_Port1Layer'] = _Res_Port1Layer
        _Caculation_Parameters['_Res_Port2Layer'] = _Res_Port2Layer

        _Caculation_Parameters['_Length_2nd'] = _Length_2nd
        _Caculation_Parameters['_LayoutOption_2nd'] = _LayoutOption_2nd
        _Caculation_Parameters['_NumFigPair_2nd'] = _NumFigPair_2nd
        _Caculation_Parameters['_Array_2nd_row'] = _Array_2nd_row
        _Caculation_Parameters['_Array_2nd_col'] = _Array_2nd_col
        _Caculation_Parameters['_Cbot_Ctop_metalwidth_2nd'] = _Cbot_Ctop_metalwidth_2nd

        ### 2nd RC Feedback
        # Define Sref Relection
        self._DesignParameter['SRF_2ndFB'] = self._SrefElementDeclaration(
            _DesignObj=A53_TIA_RCfeedback_2ndstage._TIA_RCfeedback_2ndstage(_DesignParameter=None, _Name='{}:SRF_2ndFB'.format(_Name)))[0]

        # Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_2ndFB']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_2ndFB']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_2ndFB']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_2ndFB']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        ## Calculate
        ## Target_coord: _XY_type1
        tmp11 = self.get_param_KJH4('SRF_amp2','SRF_cap0cap1','SRF_cap0','SRF_Pbodyring','SRF_PbodyLeft','SRF_PbodyContactPhyLen','BND_PPLayer')
        tmp12 = self.get_outter_KJH4('SRF_amp2')
        target_coordx = tmp12['_Mostright']['coord'][0]
        target_coordy = tmp11[0][0][0][0][0][0][0][0]['_XY_left'][1] - _DRCObj._PpMinSpace
        target_coord = [target_coordx, target_coordy]

        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_2ndFB','SRF_PbodyTop_Res_2nd','SRF_PbodyContactPhyLen','BND_PPLayer')

        approaching_coord = tmp2[0][0][0][0][0]['_XY_up_right']

        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_2ndFB')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define Coordinates
        self._DesignParameter['SRF_2ndFB']['_XYCoordinates'] = tmpXY

        ### amp2 input - RC feedback connection
        self._DesignParameter['BND_MetalLayer_amp2inn_2ndFB'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}'.format(_Res_Port1Layer)][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}'.format(_Res_Port1Layer)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Amp2_Vinn_ViaM4M7','SRF_ViaM4M5','BND_Met4Layer')
        tmp2 = self.get_param_KJH4('SRF_2ndFB','SRF_Res_2nd', 'SRF_OutputPort1_Via', 'SRF_ViaM1M2', 'BND_Met1Layer')

        self._DesignParameter['BND_MetalLayer_amp2inn_2ndFB']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']
        self._DesignParameter['BND_MetalLayer_amp2inn_2ndFB']['_YWidth'] = tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0][0]['_XY_down'][1]

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_MetalLayer_amp2inn_2ndFB']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        target_coord = tmp1[0][0][0][0]['_XY_up_left']

        tmp3 = self.get_param_KJH4('BND_MetalLayer_amp2inn_2ndFB')
        approaching_coord = tmp3[0][0]['_XY_up_left']

        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define Coordinates
        self._DesignParameter['BND_MetalLayer_amp2inn_2ndFB']['_XYCoordinates'] = tmpXY

        ## 10/17 수정 추가 부분
        ## BND_MetalLayer_amp2inn_2ndFB_extension
        tmp1 = self.get_param_KJH4('BND_MetalLayer_amp2inn_2ndFB')
        tmp2 = self.get_param_KJH4('SRF_2ndFB', 'BND_MetLayer_CBotConn_2')
        if (tmp1[0][0]['_XY_right'][0] < tmp2[0][0][0]['_XY_left'][0]):
            self._DesignParameter['BND_MetalLayer_amp2inn_2ndFB_extension'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL{}'.format(_Res_Port1Layer)][0],
                _Datatype=DesignParameters._LayerMapping['METAL{}'.format(_Res_Port1Layer)][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )

            tmp1 = self.get_param_KJH4('BND_MetalLayer_amp2inn_2ndFB')
            tmp2 = self.get_param_KJH4('SRF_2ndFB', 'BND_MetLayer_CBotConn_2')

            self._DesignParameter['BND_MetalLayer_amp2inn_2ndFB_extension']['_XWidth'] = abs(tmp2[0][0][0]['_XY_right'][0] - tmp1[0][0]['_XY_left'][0])
            self._DesignParameter['BND_MetalLayer_amp2inn_2ndFB_extension']['_YWidth'] = tmp2[0][0][0]['_Ywidth']

            # Calculate Sref XYcoord
            # initialize coordinate
            self._DesignParameter['BND_MetalLayer_amp2inn_2ndFB_extension']['_XYCoordinates'] = [[0, 0]]
            tmpXY = []
            target_coord = tmp1[0][0]['_XY_down_left']

            tmp3 = self.get_param_KJH4('BND_MetalLayer_amp2inn_2ndFB_extension')
            approaching_coord = tmp3[0][0]['_XY_down_left']

            # Sref coord
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

            ## Define Coordinates
            self._DesignParameter['BND_MetalLayer_amp2inn_2ndFB_extension']['_XYCoordinates'] = tmpXY


        ### amp2 output - RC feedback connection
        self._DesignParameter['BND_MetalLayer_amp2out_2ndFB'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}'.format(_LayoutOption_2nd[-1])][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}'.format(_LayoutOption_2nd[-1])][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_amp2', 'SRF_cap0cap1', 'SRF_cap1', 'SRF_Array','BND_CBot_METAL{}'.format(_op2_LayoutOption_cap1[-1]))
        tmp2 = self.get_param_KJH4('SRF_2ndFB', 'BND_MetLayer_CTopConn_2')

        self._DesignParameter['BND_MetalLayer_amp2out_2ndFB']['_XWidth'] = tmp1[0][0][0][0][0][0]['_Xwidth']
        self._DesignParameter['BND_MetalLayer_amp2out_2ndFB']['_YWidth'] = tmp1[0][0][0][0][0][0]['_XY_down_right'][1] - tmp2[0][0][0]['_XY_down'][1]

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_MetalLayer_amp2out_2ndFB']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        target_coord = tmp1[0][0][0][0][0][0]['_XY_down_right']

        tmp3 = self.get_param_KJH4('BND_MetalLayer_amp2out_2ndFB')
        approaching_coord = tmp3[0][0]['_XY_up_right']

        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define Coordinates
        self._DesignParameter['BND_MetalLayer_amp2out_2ndFB']['_XYCoordinates'] = tmpXY

        ### 1st RC Feedback
        _Caculation_Parameters = copy.deepcopy(A53_TIA_RCfeedback_1ststage._TIA_RCfeedback_1ststage._ParametersForDesignCalculation)
        _Caculation_Parameters['_Par_ResWidth'] = _Par_ResWidth
        _Caculation_Parameters['_Par_ResLength'] = _Par_ResLength
        _Caculation_Parameters['_Par_SeriesStripes'] = _Par_SeriesStripes
        _Caculation_Parameters['_Par_ParallelStripes'] = _Par_ParallelStripes

        _Caculation_Parameters['_Ser_ResWidth'] = _Ser_ResWidth
        _Caculation_Parameters['_Ser_ResLength'] = _Ser_ResLength
        _Caculation_Parameters['_Ser_SeriesStripes'] = _Ser_SeriesStripes
        _Caculation_Parameters['_Ser_ParallelStripes'] = _Ser_ParallelStripes

        _Caculation_Parameters['_TG_NumberofGate'] = _TG_NumberofGate
        _Caculation_Parameters['_TG_NMOSChannelWidth'] = _TG_NMOSChannelWidth
        _Caculation_Parameters['_TG_PMOSChannelWidth'] = _TG_PMOSChannelWidth
        _Caculation_Parameters['_TG_Channellength'] = _TG_Channellength
        _Caculation_Parameters['_TG_XVT'] = _TG_XVT
        _Caculation_Parameters['_INV_NumberofGate'] = _INV_NumberofGate
        _Caculation_Parameters['_NMOS_Pbody_NumCont'] = _NMOS_Pbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_NumCont'] = _PMOS_Nbody_NumCont

        _Caculation_Parameters['_Parallel_Stack'] = _Parallel_Stack

        _Caculation_Parameters['_Length_1st'] = _Length_1st
        _Caculation_Parameters['_LayoutOption_1st'] = _LayoutOption_1st
        _Caculation_Parameters['_NumFigPair_1st'] = _NumFigPair_1st
        _Caculation_Parameters['_Array_1st_row'] = _Array_1st_row
        _Caculation_Parameters['_Array_1st_col'] = _Array_1st_col
        _Caculation_Parameters['_Cbot_Ctop_metalwidth_1st'] = _Cbot_Ctop_metalwidth_1st

        # Define Sref Relection
        self._DesignParameter['SRF_1stFB'] = self._SrefElementDeclaration(
            _DesignObj=A53_TIA_RCfeedback_1ststage._TIA_RCfeedback_1ststage(_DesignParameter=None, _Name='{}:SRF_1stFB'.format(_Name)))[0]

        # Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_1stFB']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_1stFB']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_1stFB']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_1stFB']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        ## Calculate
        ## Target_coord: _XY_type1
        tmp11 = self.get_outter_KJH4('SRF_amp1')
        tmp12 = self.get_outter_KJH4('SRF_2ndFB')
        tmp2 = self.get_outter_KJH4('SRF_1stFB')
        target_coordx = tmp12['_Mostleft']['coord'][0] - _DRCObj._PpMinSpace
        target_coordy = tmp11['_Mostdown']['coord'][0] - _DRCObj._PpMinSpace
        target_coord = [target_coordx, target_coordy]

        ## Approaching_coord: _XY_type2

        approaching_coordx = tmp2['_Mostright']['coord'][0]
        approaching_coordy = tmp2['_Mostup']['coord'][0]
        approaching_coord = [approaching_coordx, approaching_coordy]

        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_1stFB')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define Coordinates
        self._DesignParameter['SRF_1stFB']['_XYCoordinates'] = tmpXY

        ### amp1 output - 1st RC feedback connection
        self._DesignParameter['BND_Met6Layer_amp1out_1stFB'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6'][0],
            _Datatype=DesignParameters._LayerMapping['METAL6'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_amp1','BND_Metal6Layer_Connect_C0_C1_PortA_P4_N4_Drain')
        tmp2 = self.get_param_KJH4('SRF_1stFB','SRF_cap_Switch','BND_Metal3Layer_Hrz_PortAB')

        self._DesignParameter['BND_Met6Layer_amp1out_1stFB']['_XWidth'] = tmp1[0][0][0]['_Xwidth']
        self._DesignParameter['BND_Met6Layer_amp1out_1stFB']['_YWidth'] = tmp1[0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1]

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met6Layer_amp1out_1stFB']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        target_coord = tmp1[0][0][0]['_XY_up_left']

        tmp3 = self.get_param_KJH4('BND_Met6Layer_amp1out_1stFB')
        approaching_coord = tmp3[0][0]['_XY_up_left']

        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define Coordinates
        self._DesignParameter['BND_Met6Layer_amp1out_1stFB']['_XYCoordinates'] = tmpXY

        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 6
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_amp1out_1stFB_ViaM3M6'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_amp1out_1stFB_ViaM3M6'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_amp1out_1stFB_ViaM3M6']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_amp1out_1stFB_ViaM3M6']['_Angle'] = 0

        # Calcuate _COX
        tmp1 = self.get_param_KJH4('BND_Met6Layer_amp1out_1stFB')
        tmpWidth = tmp1[0][0]['_Xwidth']
        _Caculation_Parameters['_COX'] = int(max(2,
            (tmpWidth - 2 * _DRCObj._Metal1MinEnclosureVia3 - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2) + 1
        ))

        # Calcuate _COY
        tmp2 = self.get_param_KJH4('SRF_1stFB','SRF_cap_Switch','BND_Metal3Layer_Hrz_PortAB')
        tmpWidth = tmp2[0][0][0][0]['_Ywidth']
        _Caculation_Parameters['_COY'] = int(max(2,
            (tmpWidth - 2 * _DRCObj._Metal1MinEnclosureVia3 - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2) + 1
        ))

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_amp1out_1stFB_ViaM3M6']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_amp1out_1stFB_ViaM3M6']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        target_coord = [tmp1[0][0]['_XY_down'][0], tmp2[0][0][0][0]['_XY_right'][1]]
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_amp1out_1stFB_ViaM3M6', 'SRF_ViaM3M4', 'BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_amp1out_1stFB_ViaM3M6')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_amp1out_1stFB_ViaM3M6']['_XYCoordinates'] = tmpXY


        ### amp1 inn - 1st RC feedback connection
        self._DesignParameter['BND_Met4Layer_amp1inn_1stFB'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_amp1','SRF_Pmos_Tr1Tr2Tr4_Nbodyring','SRF_Pmos_Tr1Tr2Tr4','SRF_Pmos_Tr2','BND_Metal4Layer_Hrz_Gate')
        tmp2 = self.get_param_KJH4('SRF_1stFB','SRF_Res_Series','SRF_TG_Switch','BND_Metal3Layer_Hrz_PortAB')

        self._DesignParameter['BND_Met4Layer_amp1inn_1stFB']['_XWidth'] = tmp1[0][0][0][0][0][0]['_Xwidth']
        self._DesignParameter['BND_Met4Layer_amp1inn_1stFB']['_YWidth'] = tmp1[0][0][0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0]['_XY_up'][1]

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met4Layer_amp1inn_1stFB']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        target_coord = tmp1[0][0][0][0][0][0]['_XY_up_left']

        tmp3 = self.get_param_KJH4('BND_Met4Layer_amp1inn_1stFB')
        approaching_coord = tmp3[0][0]['_XY_up_left']

        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define Coordinates
        self._DesignParameter['BND_Met4Layer_amp1inn_1stFB']['_XYCoordinates'] = tmpXY

        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_amp1inn_1stFB_ViaM3M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_amp1inn_1stFB_ViaM3M4'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_amp1inn_1stFB_ViaM3M4']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_amp1inn_1stFB_ViaM3M4']['_Angle'] = 0

        # Calcuate _COX
        tmp1 = self.get_param_KJH4('BND_Met4Layer_amp1inn_1stFB')
        tmpWidth = tmp1[0][0]['_Xwidth']
        _Caculation_Parameters['_COX'] = int(max(2,
            (tmpWidth - 2 * _DRCObj._Metal1MinEnclosureVia3 - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2) + 1
        ))

        # Calcuate _COY
        tmp2 = self.get_param_KJH4('SRF_1stFB','SRF_Res_Series','SRF_TG_Switch','BND_Metal3Layer_Hrz_PortAB')
        tmpWidth = tmp2[0][0][0][0][0]['_Ywidth']
        _Caculation_Parameters['_COY'] = int(max(2,
            (tmpWidth - 2 * _DRCObj._Metal1MinEnclosureVia3 - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2) + 1
        ))

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_amp1inn_1stFB_ViaM3M4']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_amp1inn_1stFB_ViaM3M4']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        target_coord = [tmp1[0][0]['_XY_down'][0], tmp2[0][0][0][0][0]['_XY_right'][1]]
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_amp1inn_1stFB_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_amp1inn_1stFB_ViaM3M4')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_amp1inn_1stFB_ViaM3M4']['_XYCoordinates'] = tmpXY

        # ##### GND Connection
        # self._DesignParameter['BND_Met1Layer_amp_ResA_GND'] = self._BoundaryElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL1'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        #     _XWidth=None,
        #     _YWidth=None,
        #     _XYCoordinates=[],
        # )
        #
        # tmp11 = self.get_param_KJH4('SRF_amp1','SRF_Pbodyring','BND_ExtenMet1Layer_Right')
        # tmp12 = self.get_param_KJH4('SRF_amp2','SRF_Pbodyring','BND_ExtenMet1Layer_Left')
        # tmp21 = self.get_param_KJH4('SRF_Pbodyring_ResA','BND_ExtenMet1Layer_Top')
        # tmp22 = self.get_param_KJH4('SRF_Pbodyring_ResA','BND_ExtenMet1Layer_Bottom')
        #
        # self._DesignParameter['BND_Met1Layer_amp_ResA_GND']['_XWidth'] = tmp12[0][0][0][0]['_XY_right'][0] - tmp11[0][0][0][0]['_XY_left'][0]
        # self._DesignParameter['BND_Met1Layer_amp_ResA_GND']['_YWidth'] = tmp21[0][0][0]['_Ywidth']
        #
        # # Calculate Sref XYcoord
        # # initialize coordinate
        # self._DesignParameter['BND_Met1Layer_amp_ResA_GND']['_XYCoordinates'] = [[0, 0]]
        # tmpXY = []
        # target_coordx = tmp11[0][0][0][0]['_XY_left'][0]
        # target_coordy = tmp21[0][0][0]['_XY_up'][1]
        # target_coord = [target_coordx, target_coordy]
        #
        # tmp3 = self.get_param_KJH4('BND_Met1Layer_amp_ResA_GND')
        # approaching_coord = tmp3[0][0]['_XY_up_left']
        #
        # # Sref coord
        # Scoord = tmp3[0][0]['_XY_origin']
        # # Cal
        # New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        # tmpXY.append(New_Scoord)
        #
        # target_coordy = tmp22[0][0][0]['_XY_up'][1]
        # target_coord = [target_coordx, target_coordy]
        #
        # # Cal
        # New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        # tmpXY.append(New_Scoord)
        # # Define
        # self._DesignParameter['BND_Met1Layer_amp_ResA_GND']['_XYCoordinates'] = tmpXY
        #
        # self._DesignParameter['BND_Met1Layer_amp1_1stFB_GND'] = self._BoundaryElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL1'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        #     _XWidth=None,
        #     _YWidth=None,
        #     _XYCoordinates=[],
        # )
        #
        # tmp1 = self.get_param_KJH4('SRF_1stFB','SRF_Res_Parallel','SRF_Pbody_Vertical','SRF_PbodyContactPhyLen','BND_Met1Layer')
        # tmp2 = self.get_param_KJH4('SRF_amp1','SRF_cap0cap1','SRF_cap1','SRF_Pbodyring','SRF_PbodyLeft','SRF_PbodyContactPhyLen','BND_Met1Layer')
        #
        # self._DesignParameter['BND_Met1Layer_amp1_1stFB_GND']['_XWidth'] = tmp1[0][0][-1][0][0][0]['_Ywidth']
        # self._DesignParameter['BND_Met1Layer_amp1_1stFB_GND']['_YWidth'] = tmp2[0][0][0][0][0][0][0][0]['_XY_up'][1] - tmp1[0][0][-1][0][0][0]['_XY_down_right'][1]
        #
        # self._DesignParameter['BND_Met1Layer_amp1_1stFB_GND']['_XYCoordinates'] = [[0, 0]]
        #
        # tmpXY = []
        # target_coord = tmp1[0][0][-1][0][0][0]['_XY_down_right']
        # tmp3 = self.get_param_KJH4('BND_Met1Layer_amp1_1stFB_GND')
        # approaching_coord = tmp3[0][0]['_XY_down_right']
        #
        # # Sref coord
        # Scoord = tmp3[0][0]['_XY_origin']
        # # Cal
        # New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        # tmpXY.append(New_Scoord)
        #
        # self._DesignParameter['BND_Met1Layer_amp1_1stFB_GND']['_XYCoordinates'] = tmpXY


        print('##############################')
        print('##     Calculation_End    ##')
        print('##############################')


## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_YCH
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'A55_TIA_6bit_target_ver2_v3'
    cellname = 'A55_TIA'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        # first op-amp
        # PMOS
        _op1_Tr0_PMOSNumberofGate=48,
        _op1_Tr0_PMOSChannelWidth=3000,
        _op1_Tr0_PMOSChannellength=150,
        _op1_Tr0_PMOSGateSpacing=None,
        _op1_Tr0_PMOSSDWidth	= None,
        _op1_Tr0_PMOSXVT			= 'EG',
        _op1_Tr0_PMOSPCCrit			= None,

        # Source_node_ViaM1M2
        _op1_Tr0_PMOSSource_Via_TF= True,

        # Drain_node_ViaM1M2
        _op1_Tr0_PMOSDrain_Via_TF= True,

        # POLY dummy setting
        _op1_Tr0_PMOSDummy= True  , # TF
        # if _PMOSDummy == True
        _op1_Tr0_PMOSDummy_length = None, # None/Value
        _op1_Tr0_PMOSDummy_placement = None, # None/'Up'/'Dn'/

        # PMOS
        _op1_Tr1_PMOSNumberofGate=30,
        _op1_Tr1_PMOSChannelWidth=6000,
        _op1_Tr1_PMOSChannellength=150,
        _op1_Tr1_PMOSGateSpacing=None,
        _op1_Tr1_PMOSSDWidth	= None,
        _op1_Tr1_PMOSXVT			= 'EG',
        _op1_Tr1_PMOSPCCrit			= None,

        # Source_node_ViaM1M2
        _op1_Tr1_PMOSSource_Via_TF= True,

        # Drain_node_ViaM1M2
        _op1_Tr1_PMOSDrain_Via_TF= True,

        # POLY dummy setting
        _op1_Tr1_PMOSDummy= True  , # TF
        # if _PMOSDummy == True
        _op1_Tr1_PMOSDummy_length = None, # None/Value
        _op1_Tr1_PMOSDummy_placement = None, # None/'Up'/'Dn'/

        # PMOS
        _op1_Tr2_PMOSNumberofGate	= 30,
        _op1_Tr2_PMOSChannelWidth	= 6000,
        _op1_Tr2_PMOSChannellength	= 150,
        _op1_Tr2_PMOSGateSpacing		= None,
        _op1_Tr2_PMOSSDWidth			= None,
        _op1_Tr2_PMOSXVT				= 'EG',
        _op1_Tr2_PMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _op1_Tr2_PMOSSource_Via_TF = True,

        # Drain_node_ViaM1M2
        _op1_Tr2_PMOSDrain_Via_TF = True,

        # POLY dummy setting
        _op1_Tr2_PMOSDummy = True, # TF
        # if _PMOSDummy == True
        _op1_Tr2_PMOSDummy_length = None, # None/Value
        _op1_Tr2_PMOSDummy_placement = None, # None/'Up'/'Dn'/

        # PMOS3
        _op1_Tr3_PMOSNumberofGate=1,
        _op1_Tr3_PMOSChannelWidth=3000,
        _op1_Tr3_PMOSChannellength=150,
        _op1_Tr3_PMOSGateSpacing=None,
        _op1_Tr3_PMOSSDWidth	= None,
        _op1_Tr3_PMOSXVT			= 'EG',
        _op1_Tr3_PMOSPCCrit			= None,

        # Source_node_ViaM1M2
        _op1_Tr3_PMOSSource_Via_TF= True,

        # Drain_node_ViaM1M2
        _op1_Tr3_PMOSDrain_Via_TF= True,

        # POLY dummy setting
        _op1_Tr3_PMOSDummy= True  , # TF
        # if _PMOSDummy == True
        _op1_Tr3_PMOSDummy_length = None, # None/Value
        _op1_Tr3_PMOSDummy_placement = None, # None/'Up'/'Dn'/

        # PMOS4
        _op1_Tr4_PMOSNumberofGate=15,
        _op1_Tr4_PMOSChannelWidth=6000,
        _op1_Tr4_PMOSChannellength=150,
        _op1_Tr4_PMOSGateSpacing	= None,
        _op1_Tr4_PMOSSDWidth			= None,
        _op1_Tr4_PMOSXVT				= 'EG',
        _op1_Tr4_PMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _op1_Tr4_PMOSSource_Via_TF = True,

        # Drain_node_ViaM1M2
        _op1_Tr4_PMOSDrain_Via_TF = True,

        # POLY dummy setting
        _op1_Tr4_PMOSDummy = True, # TF
        # if _PMOSDummy == True
        _op1_Tr4_PMOSDummy_length = None, # None/Value
        _op1_Tr4_PMOSDummy_placement = None, # None/'Up'/'Dn'/

        # NMOS Tr0
        _op1_Tr0_NMOSNumberofGate=5,
        _op1_Tr0_NMOSChannelWidth=3000,
        _op1_Tr0_NMOSChannellength=150,
        _op1_Tr0_NMOSGateSpacing=None,
        _op1_Tr0_NMOSSDWidth	= None,
        _op1_Tr0_NMOSXVT			= 'EG',
        _op1_Tr0_NMOSPCCrit			= None,

        # Source_node_ViaM1M2
        _op1_Tr0_NMOSSource_Via_TF= True,

        # Drain_node_ViaM1M2
        _op1_Tr0_NMOSDrain_Via_TF= True,

        # POLY dummy setting
        _op1_Tr0_NMOSDummy= True  , # TF
        # if _PMOSDummy == True
        _op1_Tr0_NMOSDummy_length = None, # None/Value
        _op1_Tr0_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        # NMOS Tr1
        _op1_Tr1_NMOSNumberofGate=5,
        _op1_Tr1_NMOSChannelWidth=3000,
        _op1_Tr1_NMOSChannellength=150,
        _op1_Tr1_NMOSGateSpacing	= None,
        _op1_Tr1_NMOSSDWidth			= None,
        _op1_Tr1_NMOSXVT				= 'EG',
        _op1_Tr1_NMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _op1_Tr1_NMOSSource_Via_TF = True,

        # Drain_node_ViaM1M2
        _op1_Tr1_NMOSDrain_Via_TF = True,

        # POLY dummy setting
        _op1_Tr1_NMOSDummy = True, # TF
        # if _PMOSDummy == True
        _op1_Tr1_NMOSDummy_length = None, # None/Value
        _op1_Tr1_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        # NMOS tr2
        _op1_Tr2_NMOSNumberofGate=5,
        _op1_Tr2_NMOSChannelWidth=3000,
        _op1_Tr2_NMOSChannellength=150,
        _op1_Tr2_NMOSGateSpacing=None,
        _op1_Tr2_NMOSSDWidth	= None,
        _op1_Tr2_NMOSXVT			= 'EG',
        _op1_Tr2_NMOSPCCrit			= None,

        # Source_node_ViaM1M2
        _op1_Tr2_NMOSSource_Via_TF= True,

        # Drain_node_ViaM1M2
        _op1_Tr2_NMOSDrain_Via_TF= True,

        # POLY dummy setting
        _op1_Tr2_NMOSDummy= True  , # TF
        # if _PMOSDummy == True
        _op1_Tr2_NMOSDummy_length = None, # None/Value
        _op1_Tr2_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        # NMOS tr3
        _op1_Tr3_NMOSNumberofGate=1,
        _op1_Tr3_NMOSChannelWidth=3000,
        _op1_Tr3_NMOSChannellength=150,
        _op1_Tr3_NMOSGateSpacing	= None,
        _op1_Tr3_NMOSSDWidth			= None,
        _op1_Tr3_NMOSXVT				= 'EG',
        _op1_Tr3_NMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _op1_Tr3_NMOSSource_Via_TF = True,

        # Drain_node_ViaM1M2
        _op1_Tr3_NMOSDrain_Via_TF = True,

        # POLY dummy setting
        _op1_Tr3_NMOSDummy = True, # TF
        # if _PMOSDummy == True
        _op1_Tr3_NMOSDummy_length = None, # None/Value
        _op1_Tr3_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        # NMOS Tr4
        _op1_Tr4_NMOSNumberofGate=8,
        _op1_Tr4_NMOSChannelWidth=3000,
        _op1_Tr4_NMOSChannellength=150,
        _op1_Tr4_NMOSGateSpacing	= None,
        _op1_Tr4_NMOSSDWidth			= None,
        _op1_Tr4_NMOSXVT				= 'EG',
        _op1_Tr4_NMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _op1_Tr4_NMOSSource_Via_TF = False,

        # Drain_node_ViaM1M2
        _op1_Tr4_NMOSDrain_Via_TF = False,

        # POLY dummy setting
        _op1_Tr4_NMOSDummy = True, # TF
        # if _PMOSDummy == True
        _op1_Tr4_NMOSDummy_length = None, # None/Value
        _op1_Tr4_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        # N body ring(P1P2P4)
        _op1_NumContTop_P1P2P4 = 3,
        _op1_NumContBottom_P1P2P4=3,
        _op1_NumContLeft_P1P2P4=3,
        _op1_NumContRight_P1P2P4=3,

        # N body ring(P0P3)
        _op1_NumContTop_P0P3 = 3,
        _op1_NumContLeft_P0P3 = 3,
        _op1_NumContRight_P0P3 = 3,

        # P body ring
        _op1_NumContTop_Pbody = 3,
        _op1_NumContBottom_Pbody=3,
        _op1_NumContLeft_Pbody=3,
        _op1_NumContRight_Pbody=3,

        # Res0
        _op1_ResWidth_res0 = 600,
        _op1_ResLength_res0 = 800,
        _op1_CONUMX_res0 = None,
        _op1_CONUMY_res0 = None,
        _op1_SeriesStripes_res0 = 1,
        _op1_ParallelStripes_res0 = 1, # 고정

        # Res1
        _op1_ResWidth_res1=600,
        _op1_ResLength_res1=800,
        _op1_CONUMX_res1=None,
        _op1_CONUMY_res1=None,
        _op1_SeriesStripes_res1=1,
        _op1_ParallelStripes_res1=1, # 고정

        # Cap0
        _op1_Length_cap0=4300,
        _op1_LayoutOption_cap0=[2,3,4,5], # 고정
        _op1_NumFigPair_cap0=25,

        _op1_Array_cap0=1,  # number: 1xnumber
        _op1_Cbot_Ctop_metalwidth_cap0=500,  # number

        # Cap1
        _op1_Length_cap1=4300,
        _op1_LayoutOption_cap1=[2,3,4,5], # 고정
        _op1_NumFigPair_cap1=25,

        _op1_Array_cap1=1,  # number: 1xnumber
        _op1_Cbot_Ctop_metalwidth_cap1=500,  # number


        # second op-amp
        # PMOS tr0
        _op2_Tr0_PMOSNumberofGate=48,
        _op2_Tr0_PMOSChannelWidth=3000,
        _op2_Tr0_PMOSChannellength=150,
        _op2_Tr0_PMOSGateSpacing=None,
        _op2_Tr0_PMOSSDWidth=None,
        _op2_Tr0_PMOSXVT	= 'EG',
        _op2_Tr0_PMOSPCCrit		= None,

        # Source_node_ViaM1M2
        _op2_Tr0_PMOSSource_Via_TF= True,

        # Drain_node_ViaM1M2
        _op2_Tr0_PMOSDrain_Via_TF= True,

        # POLY dummy setting
        _op2_Tr0_PMOSDummy= True  , # TF
        # if _PMOSDummy == True
        _op2_Tr0_PMOSDummy_length = None, # None/Value
        _op2_Tr0_PMOSDummy_placement = None, # None/'Up'/'Dn'/

        # PMOS tr1
        _op2_Tr1_PMOSNumberofGate=30,
        _op2_Tr1_PMOSChannelWidth=6000,
        _op2_Tr1_PMOSChannellength=150,
        _op2_Tr1_PMOSGateSpacing=None,
        _op2_Tr1_PMOSSDWidth	= None,
        _op2_Tr1_PMOSXVT			= 'EG',
        _op2_Tr1_PMOSPCCrit			= None,

        # Source_node_ViaM1M2
        _op2_Tr1_PMOSSource_Via_TF= True,

        # Drain_node_ViaM1M2
        _op2_Tr1_PMOSDrain_Via_TF= True,

        # POLY dummy setting
        _op2_Tr1_PMOSDummy= True  , # TF
        # if _PMOSDummy == True
        _op2_Tr1_PMOSDummy_length = None, # None/Value
        _op2_Tr1_PMOSDummy_placement = None, # None/'Up'/'Dn'/

        # PMOS tr2
        _op2_Tr2_PMOSNumberofGate	= 30,
        _op2_Tr2_PMOSChannelWidth	= 6000,
        _op2_Tr2_PMOSChannellength	= 150,
        _op2_Tr2_PMOSGateSpacing		= None,
        _op2_Tr2_PMOSSDWidth			= None,
        _op2_Tr2_PMOSXVT				= 'EG',
        _op2_Tr2_PMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _op2_Tr2_PMOSSource_Via_TF = True,

        # Drain_node_ViaM1M2
        _op2_Tr2_PMOSDrain_Via_TF = True,

        # POLY dummy setting
        _op2_Tr2_PMOSDummy = True, # TF
        # if _PMOSDummy == True
        _op2_Tr2_PMOSDummy_length = None, # None/Value
        _op2_Tr2_PMOSDummy_placement = None, # None/'Up'/'Dn'/

        # PMOS tr3
        _op2_Tr3_PMOSNumberofGate=1,
        _op2_Tr3_PMOSChannelWidth=3000,
        _op2_Tr3_PMOSChannellength=150,
        _op2_Tr3_PMOSGateSpacing=None,
        _op2_Tr3_PMOSSDWidth	= None,
        _op2_Tr3_PMOSXVT			= 'EG',
        _op2_Tr3_PMOSPCCrit			= None,

        # Source_node_ViaM1M2
        _op2_Tr3_PMOSSource_Via_TF= True,

        # Drain_node_ViaM1M2
        _op2_Tr3_PMOSDrain_Via_TF= True,

        # POLY dummy setting
        _op2_Tr3_PMOSDummy= True  , # TF
        # if _PMOSDummy == True
        _op2_Tr3_PMOSDummy_length = None, # None/Value
        _op2_Tr3_PMOSDummy_placement = None, # None/'Up'/'Dn'/

        # PMOS tr4
        _op2_Tr4_PMOSNumberofGate=15,
        _op2_Tr4_PMOSChannelWidth=6000,
        _op2_Tr4_PMOSChannellength=150,
        _op2_Tr4_PMOSGateSpacing	= None,
        _op2_Tr4_PMOSSDWidth			= None,
        _op2_Tr4_PMOSXVT				= 'EG',
        _op2_Tr4_PMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _op2_Tr4_PMOSSource_Via_TF = True,

        # Drain_node_ViaM1M2
        _op2_Tr4_PMOSDrain_Via_TF = True,

        # POLY dummy setting
        _op2_Tr4_PMOSDummy = True, # TF
        # if _PMOSDummy == True
        _op2_Tr4_PMOSDummy_length = None, # None/Value
        _op2_Tr4_PMOSDummy_placement = None, # None/'Up'/'Dn'/

        # NMOS Tr0
        _op2_Tr0_NMOSNumberofGate=5,
        _op2_Tr0_NMOSChannelWidth=3000,
        _op2_Tr0_NMOSChannellength=150,
        _op2_Tr0_NMOSGateSpacing=None,
        _op2_Tr0_NMOSSDWidth	= None,
        _op2_Tr0_NMOSXVT			= 'EG',
        _op2_Tr0_NMOSPCCrit			= None,

        # Source_node_ViaM1M2
        _op2_Tr0_NMOSSource_Via_TF= True,

        # Drain_node_ViaM1M2
        _op2_Tr0_NMOSDrain_Via_TF= True,

        # POLY dummy setting
        _op2_Tr0_NMOSDummy= True  , # TF
        # if _PMOSDummy == True
        _op2_Tr0_NMOSDummy_length = None, # None/Value
        _op2_Tr0_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        # NMOS Tr1
        _op2_Tr1_NMOSNumberofGate=5,
        _op2_Tr1_NMOSChannelWidth=3000,
        _op2_Tr1_NMOSChannellength=150,
        _op2_Tr1_NMOSGateSpacing	= None,
        _op2_Tr1_NMOSSDWidth			= None,
        _op2_Tr1_NMOSXVT				= 'EG',
        _op2_Tr1_NMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _op2_Tr1_NMOSSource_Via_TF = True,

        # Drain_node_ViaM1M2
        _op2_Tr1_NMOSDrain_Via_TF = True,

        # POLY dummy setting
        _op2_Tr1_NMOSDummy = True, # TF
        # if _PMOSDummy == True
        _op2_Tr1_NMOSDummy_length = None, # None/Value
        _op2_Tr1_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        # NMOS tr2
        _op2_Tr2_NMOSNumberofGate=5,
        _op2_Tr2_NMOSChannelWidth=3000,
        _op2_Tr2_NMOSChannellength=150,
        _op2_Tr2_NMOSGateSpacing=None,
        _op2_Tr2_NMOSSDWidth	= None,
        _op2_Tr2_NMOSXVT			= 'EG',
        _op2_Tr2_NMOSPCCrit			= None,

        # Source_node_ViaM1M2
        _op2_Tr2_NMOSSource_Via_TF= True,

        # Drain_node_ViaM1M2
        _op2_Tr2_NMOSDrain_Via_TF= True,

        # POLY dummy setting
        _op2_Tr2_NMOSDummy= True  , # TF
        # if _PMOSDummy == True
        _op2_Tr2_NMOSDummy_length = None, # None/Value
        _op2_Tr2_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        # NMOS tr3
        _op2_Tr3_NMOSNumberofGate=1,
        _op2_Tr3_NMOSChannelWidth=3000,
        _op2_Tr3_NMOSChannellength=150,
        _op2_Tr3_NMOSGateSpacing	= None,
        _op2_Tr3_NMOSSDWidth			= None,
        _op2_Tr3_NMOSXVT				= 'EG',
        _op2_Tr3_NMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _op2_Tr3_NMOSSource_Via_TF = True,

        # Drain_node_ViaM1M2
        _op2_Tr3_NMOSDrain_Via_TF = True,

        # POLY dummy setting
        _op2_Tr3_NMOSDummy = True, # TF
        # if _PMOSDummy == True
        _op2_Tr3_NMOSDummy_length = None, # None/Value
        _op2_Tr3_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        # NMOS Tr4
        _op2_Tr4_NMOSNumberofGate=8,
        _op2_Tr4_NMOSChannelWidth=3000,
        _op2_Tr4_NMOSChannellength=150,
        _op2_Tr4_NMOSGateSpacing	= None,
        _op2_Tr4_NMOSSDWidth			= None,
        _op2_Tr4_NMOSXVT				= 'EG',
        _op2_Tr4_NMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _op2_Tr4_NMOSSource_Via_TF = False,

        # Drain_node_ViaM1M2
        _op2_Tr4_NMOSDrain_Via_TF = False,

        # POLY dummy setting
        _op2_Tr4_NMOSDummy = True, # TF
        # if _PMOSDummy == True
        _op2_Tr4_NMOSDummy_length = None, # None/Value
        _op2_Tr4_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        # N body ring(P1P2P4)
        _op2_NumContTop_P1P2P4 = 3,
        _op2_NumContBottom_P1P2P4=3,
        _op2_NumContLeft_P1P2P4=3,
        _op2_NumContRight_P1P2P4=3,

        # N body ring(P0P3)
        _op2_NumContTop_P0P3 = 3,
        _op2_NumContLeft_P0P3 = 3,
        _op2_NumContRight_P0P3 = 3,

        # P body ring
        _op2_NumContTop_Pbody = 3,
        _op2_NumContBottom_Pbody=3,
        _op2_NumContLeft_Pbody=3,
        _op2_NumContRight_Pbody=3,

        # Res0
        _op2_ResWidth_res0 = 600,
        _op2_ResLength_res0 = 800,
        _op2_CONUMX_res0 = None,
        _op2_CONUMY_res0 = None,
        _op2_SeriesStripes_res0 = 1,
        _op2_ParallelStripes_res0 =  1, # 고정

        # Res1
        _op2_ResWidth_res1=600,
        _op2_ResLength_res1=800,
        _op2_CONUMX_res1=None,
        _op2_CONUMY_res1=None,
        _op2_SeriesStripes_res1=1,
        _op2_ParallelStripes_res1=  1, # 고정

        # Cap0
        _op2_Length_cap0=4300,
        _op2_LayoutOption_cap0 =[2, 3, 4, 5], # 고정
        _op2_NumFigPair_cap0=25,

        _op2_Array_cap0=1,  # number: 1xnumber
        _op2_Cbot_Ctop_metalwidth_cap0=500,  # number

        # Cap1
        _op2_Length_cap1=4300,
        _op2_LayoutOption_cap1= [2, 3, 4, 5], # 고정
        _op2_NumFigPair_cap1=25,

        _op2_Array_cap1=1,  # number: 1xnumber
        _op2_Cbot_Ctop_metalwidth_cap1=500,  # number



        # ResA
        _ResWidth_resA=1000,
        _ResLength_resA=2800,
        _CONUMX_resA=None,
        _CONUMY_resA=None,
        _SeriesStripes_resA=3,
        _ParallelStripes_resA=1,

        ### 2nd Stage FB
        # Res_2nd
        _ResWidth_2nd=500,
        _ResLength_2nd=2000,
        _CONUMX_2nd=None,
        _CONUMY_2nd=None,
        _SeriesStripes_2nd=9,
        _ParallelStripes_2nd=1,
        _Res_Port1Layer=5,
        _Res_Port2Layer=5,

        # Cap_2nd
        _Length_2nd=4300,
        _LayoutOption_2nd=[2, 3, 4],
        _NumFigPair_2nd=10,
        _Array_2nd_row=1,
        _Array_2nd_col=3,
        _Cbot_Ctop_metalwidth_2nd=500,

        ### 1st Feedback
        # Parallel Res
        _Par_ResWidth=150,
        _Par_ResLength=850,
        _Par_SeriesStripes=4,
        _Par_ParallelStripes=1,

        _Ser_ResWidth=150,
        _Ser_ResLength=650,
        _Ser_SeriesStripes=4, # 짝수로 넣기
        _Ser_ParallelStripes=1,

        _TG_NumberofGate=100,  # number
        _TG_NMOSChannelWidth=500,  # number
        _TG_PMOSChannelWidth=1000,
        _TG_Channellength=150,  # number
        _TG_XVT			='EG', # 'XVT' ex)SLVT LVT RVT HVT EG
        _INV_NumberofGate       =2,
        _NMOS_Pbody_NumCont     =2,
        _PMOS_Nbody_NumCont     =2,

        _Parallel_Stack         =6,

        # Cap_1st
        _Length_1st=4300,
        _LayoutOption_1st=[2, 3, 4],
        _NumFigPair_1st=10,
        _Array_1st_row=2,
        _Array_1st_col=2,
        _Cbot_Ctop_metalwidth_1st=500,

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
    LayoutObj = _TIA_YCH(_DesignParameter=None, _Name=cellname)
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

    print(elapsed_time)
    print(h, 'hour')
    print(m, 'min')
    print(s, 'sec')

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
    # # Checker.cell_deletion()
    # Checker.Upload2FTP()
    # Checker.StreamIn(tech=DesignParameters._Technology)
    # # Checker_KJH0.DRCchecker()


    print('#############################      Finished      ################################')
# end of 'main():' ---------------------------------------------------------------------------------------------