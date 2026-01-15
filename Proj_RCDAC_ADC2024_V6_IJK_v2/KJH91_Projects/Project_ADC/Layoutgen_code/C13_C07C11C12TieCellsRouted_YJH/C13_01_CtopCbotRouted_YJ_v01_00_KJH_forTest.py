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
from KJH91_Projects.Project_ADC.Layoutgen_code.C13_C07C11C12TieCellsRouted_YJH import C13_00_C07C11C12TieCellsRouted_YJ_v01_00
from KJH91_Projects.Project_ADC.Layoutgen_code.C01_HDVNCAP_Array import C01_04_Guardring
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3

## Define Class
class _CtopCbotRouted(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(

        # Tr1 and Tr2
        # Tr1
        _Tr1Tr2_Tr1_NMOSNumberofGate=12,  # number
        _Tr1Tr2_Tr1_NMOSChannelWidth=1000,  # number
        _Tr1Tr2_Tr1_NMOSChannellength=30,  # number
        _Tr1Tr2_Tr1_GateSpacing=222,  # None/number
        _Tr1Tr2_Tr1_SDWidth=None,  # None/number
        _Tr1Tr2_Tr1_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Tr1Tr2_Tr1_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _Tr1Tr2_Tr1_Source_Via_TF=False,  # True/False

        # Drain_node_ViaM1M2
        _Tr1Tr2_Tr1_Drain_Via_TF=False,  # True/False

        # POLY dummy setting
        _Tr1Tr2_Tr1_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Tr1Tr2_Tr1_NMOSDummy_length=None,  # None/Value
        _Tr1Tr2_Tr1_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr2
        _Tr1Tr2_Tr2_NMOSNumberofGate=5,  # number
        _Tr1Tr2_Tr2_NMOSChannelWidth=1000,  # number
        _Tr1Tr2_Tr2_NMOSChannellength=30,  # number
        _Tr1Tr2_Tr2_GateSpacing=100,  # None/number
        _Tr1Tr2_Tr2_SDWidth=None,  # None/number
        _Tr1Tr2_Tr2_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Tr1Tr2_Tr2_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _Tr1Tr2_Tr2_Source_Via_TF=False,  # True/False

        # Drain_node_ViaM1M2
        _Tr1Tr2_Tr2_Drain_Via_TF=False,  # True/False

        # POLY dummy setting
        _Tr1Tr2_Tr2_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Tr1Tr2_Tr2_NMOSDummy_length=None,  # None/Value
        _Tr1Tr2_Tr2_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Input/Output node
        # INPUT node
        _Tr1Tr2_Inputnode_Metal_layer=6,  # number
        _Tr1Tr2_Inputnode_width=600,  # number

        # OUTPUT node
        _Tr1Tr2_Outputnode_Metal_layer=6,  # number
        _Tr1Tr2_Outputnode_width=600,  # number

        # Guardring
        # Pbody: number of contact
        # Nbody
        _Tr1Tr2_NwellWidth=850,  # number

        # Tr4
        _Tr4_NMOSNumberofGate=4,  # number
        _Tr4_NMOSChannelWidth=500,  # number
        _Tr4_NMOSChannellength=30,  # number
        _Tr4_GateSpacing=None,  # None/number
        _Tr4_SDWidth=None,  # None/number
        _Tr4_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Tr4_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _Tr4_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _Tr4_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _Tr4_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Tr4_NMOSDummy_length=None,  # None/Value
        _Tr4_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr5 Tr7 Tr9
        # PMOS: Tr5
        _Tr5_PMOSNumberofGate=2,
        _Tr5_PMOSChannelWidth=1000,  # ref=1000
        _Tr5_PMOSChannellength=30,
        _Tr5_GateSpacing=100,
        _Tr5_SDWidth=None,
        _Tr5_XVT='SLVT',
        _Tr5_PCCrit=None,

        # Source_node_ViaM1M2
        _Tr5_Source_Via_TF=True,

        # Drain_node_ViaM1M2
        _Tr5_Drain_Via_TF=True,

        # POLY dummy setting
        _Tr5_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Tr5_PMOSDummy_length=None,  # None/Value
        _Tr5_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # PMOS: Tr7
        _Tr7_PMOSNumberofGate=4,
        _Tr7_PMOSChannelWidth=1000,
        _Tr7_PMOSChannellength=30,
        _Tr7_GateSpacing=100,
        _Tr7_SDWidth=None,
        _Tr7_XVT='SLVT',
        _Tr7_PCCrit=None,

        # Source_node_ViaM1M2
        _Tr7_Source_Via_TF=True,

        # Drain_node_ViaM1M2
        _Tr7_Drain_Via_TF=True,

        # POLY dummy setting
        _Tr7_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Tr7_PMOSDummy_length=None,  # None/Value
        _Tr7_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # PMOS: Tr9
        _Tr9_PMOSNumberofGate=8,
        _Tr9_PMOSChannelWidth=1000,  # ref = 1000
        _Tr9_PMOSChannellength=30,
        _Tr9_GateSpacing=100,
        _Tr9_SDWidth=None,
        _Tr9_XVT='SLVT',
        _Tr9_PCCrit=None,

        # Source_node_ViaM1M2
        _Tr9_Source_Via_TF=True,

        # Drain_node_ViaM1M2
        _Tr9_Drain_Via_TF=True,

        # POLY dummy setting
        _Tr9_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Tr9_PMOSDummy_length=None,  # None/Value
        _Tr9_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr8
        _Tr8_NMOSNumberofGate=12,  # number (ref:4)
        _Tr8_NMOSChannelWidth=500,  # number (ref:500)
        _Tr8_NMOSChannellength=30,  # number (ref:30)
        _Tr8_GateSpacing=None,  # None/number
        _Tr8_SDWidth=None,  # None/number
        _Tr8_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Tr8_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _Tr8_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _Tr8_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _Tr8_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Tr8_NMOSDummy_length=None,  # None/Value
        _Tr8_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        ## Tr6
        _Tr6_NMOSNumberofGate=6,  # number
        _Tr6_NMOSChannelWidth=1000,  # number
        _Tr6_NMOSChannellength=30,  # number
        _Tr6_GateSpacing=None,  # None/number
        _Tr6_SDWidth=None,  # None/number
        _Tr6_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Tr6_PCCrit=True,  # None/True

        # Tr6 Source_node_ViaM1M2
        _Tr6_Source_Via_TF=False,  # True/False

        # Tr6 Drain_node_ViaM1M2
        _Tr6_Drain_Via_TF=False,  # True/False

        # Tr6 POLY dummy setting
        _Tr6_NMOSDummy=True,  # TF
        # Tr6 if _PMOSDummy == True
        _Tr6_NMOSDummy_length=None,  # None/Value
        _Tr6_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr6 Vp node
        _Tr6_Vp_node_width=280,  # Number
        _Tr6_Vp_node_metal_Layer=3,  # number

        # Tr6 Guardring
        # Pbody: number of contact
        # Nbody
        _Tr6_NwellWidth=850,  # number

        # PMOS: Tr11
        _Tr11_PMOSNumberofGate=8,
        _Tr11_PMOSChannelWidth=500,
        _Tr11_PMOSChannellength=30,
        _Tr11_GateSpacing=100,
        _Tr11_SDWidth=None,
        _Tr11_XVT='SLVT',
        _Tr11_PCCrit=None,

        # Source_node_ViaM1M2
        _Tr11_Source_Via_TF=True,

        # Drain_node_ViaM1M2
        _Tr11_Drain_Via_TF=True,

        # POLY dummy setting
        _Tr11_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Tr11_PMOSDummy_length=None,  # None/Value
        _Tr11_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Nbodyring(Guardring)
        _Tr11_Guardring_NumCont=3,  # number

        ## VddTieCell4
        # VddTieCell4 NMOS
        _Tie4N_NMOSNumberofGate=4,  # number
        _Tie4N_NMOSChannelWidth=250,  # number
        _Tie4N_NMOSChannellength=30,  # number
        _Tie4N_GateSpacing=100,  # None/number
        _Tie4N_SDWidth=None,  # None/number
        _Tie4N_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Tie4N_PCCrit=True,  # None/True

        # VddTieCell4 Source_node_ViaM1M2
        _Tie4N_Source_Via_TF=False,  # True/False

        # VddTieCell4 Drain_node_ViaM1M2
        _Tie4N_Drain_Via_TF=False,  # True/False

        # POLY dummy setting
        _Tie4N_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Tie4N_NMOSDummy_length=400,  # None/Value
        _Tie4N_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # VddTieCell4 PMOS
        _Tie4P_PMOSNumberofGate=4,  # number
        _Tie4P_PMOSChannelWidth=500,  # number
        _Tie4P_PMOSChannellength=30,  # number
        _Tie4P_GateSpacing=100,  # None/number
        _Tie4P_SDWidth=None,  # None/number
        _Tie4P_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Tie4P_PCCrit=True,  # None/True

        # VddTieCell4 PMOS Source_node_ViaM1M2
        _Tie4P_Source_Via_TF=False,  # True/False

        # VddTieCell4 PMOS Drain_node_ViaM1M2
        _Tie4P_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _Tie4P_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Tie4P_PMOSDummy_length=None,  # None/Value
        _Tie4P_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # VddTieCell4 Number of Body Contact
        _Tie4_NBodyCOX=15,
        _Tie4_NBodyCOY=3,
        _Tie4_PBodyCOX=15,
        _Tie4_PBodyCOY=3,

        ## VddTieCell8
        # VddTieCell8 NMOS
        _Tie8N_NMOSNumberofGate=4,  # number
        _Tie8N_NMOSChannelWidth=250,  # number
        _Tie8N_NMOSChannellength=30,  # number
        _Tie8N_GateSpacing=100,  # None/number
        _Tie8N_SDWidth=None,  # None/number
        _Tie8N_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Tie8N_PCCrit=True,  # None/True

        # VddTieCell8 Source_node_ViaM1M2
        _Tie8N_Source_Via_TF=False,  # True/False

        # VddTieCell8 Drain_node_ViaM1M2
        _Tie8N_Drain_Via_TF=False,  # True/False

        # POLY dummy setting
        _Tie8N_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Tie8N_NMOSDummy_length=400,  # None/Value
        _Tie8N_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # VddTieCell8 PMOS
        _Tie8P_PMOSNumberofGate=4,  # number
        _Tie8P_PMOSChannelWidth=500,  # number
        _Tie8P_PMOSChannellength=30,  # number
        _Tie8P_GateSpacing=100,  # None/number
        _Tie8P_SDWidth=None,  # None/number
        _Tie8P_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Tie8P_PCCrit=True,  # None/True

        # VddTieCell8 PMOS Source_node_ViaM1M2
        _Tie8P_Source_Via_TF=False,  # True/False

        # VddTieCell8 PMOS Drain_node_ViaM1M2
        _Tie8P_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _Tie8P_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Tie8P_PMOSDummy_length=None,  # None/Value
        _Tie8P_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # VddTieCell8 Number of Body Contact
        _Tie8_NBodyCOX=15,
        _Tie8_NBodyCOY=3,
        _Tie8_PBodyCOX=15,
        _Tie8_PBodyCOY=3,

        # Tr12
        _Tr12_NMOSNumberofGate=4,  # number
        _Tr12_NMOSChannelWidth=1000,  # number
        _Tr12_NMOSChannellength=30,  # number
        _Tr12_GateSpacing=None,  # None/number
        _Tr12_SDWidth=None,  # None/number
        _Tr12_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Tr12_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _Tr12_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _Tr12_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _Tr12_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Tr12_NMOSDummy_length=None,  # None/Value
        _Tr12_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr3
        _Tr3_NMOSNumberofGate=4,  # number
        _Tr3_NMOSChannelWidth=500,  # number
        _Tr3_NMOSChannellength=30,  # number
        _Tr3_GateSpacing=None,  # None/number
        _Tr3_SDWidth=None,  # None/number
        _Tr3_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Tr3_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _Tr3_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _Tr3_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _Tr3_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Tr3_NMOSDummy_length=None,  # None/Value
        _Tr3_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr10
        _Tr10_NMOSNumberofGate=8,  # number
        _Tr10_NMOSChannelWidth=1000,  # number
        _Tr10_NMOSChannellength=30,  # number
        _Tr10_GateSpacing=None,  # None/number
        _Tr10_SDWidth=None,  # None/number
        _Tr10_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Tr10_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _Tr10_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _Tr10_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _Tr10_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Tr10_NMOSDummy_length=None,  # None/Value
        _Tr10_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr12Tr3Tr10 Guardring
        _Tr12Tr3Tr10_Guardring_NumCont=3,  # Number

        # HDVNCAP_Array
        _HDVNCAP_Length=5000,
        _HDVNCAP_LayoutOption=[3, 4, 5, 6],
        _HDVNCAP_NumFigPair=75,
        _HDVNCAP_Array=3,  # number: 1xnumber
        _HDVNCAP_Cbot_Ctop_metalwidth=1000,  # number
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

                                  # Tr1 and Tr2
                                  # Tr1
                                  _Tr1Tr2_Tr1_NMOSNumberofGate=12,  # number
                                  _Tr1Tr2_Tr1_NMOSChannelWidth=1000,  # number
                                  _Tr1Tr2_Tr1_NMOSChannellength=30,  # number
                                  _Tr1Tr2_Tr1_GateSpacing=222,  # None/number
                                  _Tr1Tr2_Tr1_SDWidth=None,  # None/number
                                  _Tr1Tr2_Tr1_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Tr1Tr2_Tr1_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _Tr1Tr2_Tr1_Source_Via_TF=False,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Tr1Tr2_Tr1_Drain_Via_TF=False,  # True/False

                                  # POLY dummy setting
                                  _Tr1Tr2_Tr1_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tr1Tr2_Tr1_NMOSDummy_length=None,  # None/Value
                                  _Tr1Tr2_Tr1_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Tr2
                                  _Tr1Tr2_Tr2_NMOSNumberofGate=5,  # number
                                  _Tr1Tr2_Tr2_NMOSChannelWidth=1000,  # number
                                  _Tr1Tr2_Tr2_NMOSChannellength=30,  # number
                                  _Tr1Tr2_Tr2_GateSpacing=100,  # None/number
                                  _Tr1Tr2_Tr2_SDWidth=None,  # None/number
                                  _Tr1Tr2_Tr2_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Tr1Tr2_Tr2_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _Tr1Tr2_Tr2_Source_Via_TF=False,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Tr1Tr2_Tr2_Drain_Via_TF=False,  # True/False

                                  # POLY dummy setting
                                  _Tr1Tr2_Tr2_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tr1Tr2_Tr2_NMOSDummy_length=None,  # None/Value
                                  _Tr1Tr2_Tr2_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Input/Output node
                                  # INPUT node
                                  _Tr1Tr2_Inputnode_Metal_layer=6,  # number
                                  _Tr1Tr2_Inputnode_width=600,  # number

                                  # OUTPUT node
                                  _Tr1Tr2_Outputnode_Metal_layer=6,  # number
                                  _Tr1Tr2_Outputnode_width=600,  # number

                                  # Guardring
                                  # Pbody: number of contact
                                  # Nbody
                                  _Tr1Tr2_NwellWidth=850,  # number

                                  # Tr4
                                  _Tr4_NMOSNumberofGate=4,  # number
                                  _Tr4_NMOSChannelWidth=500,  # number
                                  _Tr4_NMOSChannellength=30,  # number
                                  _Tr4_GateSpacing=None,  # None/number
                                  _Tr4_SDWidth=None,  # None/number
                                  _Tr4_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Tr4_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _Tr4_Source_Via_TF=True,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Tr4_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _Tr4_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tr4_NMOSDummy_length=None,  # None/Value
                                  _Tr4_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Tr5 Tr7 Tr9
                                  # PMOS: Tr5
                                  _Tr5_PMOSNumberofGate=2,
                                  _Tr5_PMOSChannelWidth=1000,  # ref=1000
                                  _Tr5_PMOSChannellength=30,
                                  _Tr5_GateSpacing=100,
                                  _Tr5_SDWidth=None,
                                  _Tr5_XVT='SLVT',
                                  _Tr5_PCCrit=None,

                                  # Source_node_ViaM1M2
                                  _Tr5_Source_Via_TF=True,

                                  # Drain_node_ViaM1M2
                                  _Tr5_Drain_Via_TF=True,

                                  # POLY dummy setting
                                  _Tr5_PMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tr5_PMOSDummy_length=None,  # None/Value
                                  _Tr5_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # PMOS: Tr7
                                  _Tr7_PMOSNumberofGate=4,
                                  _Tr7_PMOSChannelWidth=1000,
                                  _Tr7_PMOSChannellength=30,
                                  _Tr7_GateSpacing=100,
                                  _Tr7_SDWidth=None,
                                  _Tr7_XVT='SLVT',
                                  _Tr7_PCCrit=None,

                                  # Source_node_ViaM1M2
                                  _Tr7_Source_Via_TF=True,

                                  # Drain_node_ViaM1M2
                                  _Tr7_Drain_Via_TF=True,

                                  # POLY dummy setting
                                  _Tr7_PMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tr7_PMOSDummy_length=None,  # None/Value
                                  _Tr7_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # PMOS: Tr9
                                  _Tr9_PMOSNumberofGate=8,
                                  _Tr9_PMOSChannelWidth=1000,  # ref = 1000
                                  _Tr9_PMOSChannellength=30,
                                  _Tr9_GateSpacing=100,
                                  _Tr9_SDWidth=None,
                                  _Tr9_XVT='SLVT',
                                  _Tr9_PCCrit=None,

                                  # Source_node_ViaM1M2
                                  _Tr9_Source_Via_TF=True,

                                  # Drain_node_ViaM1M2
                                  _Tr9_Drain_Via_TF=True,

                                  # POLY dummy setting
                                  _Tr9_PMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tr9_PMOSDummy_length=None,  # None/Value
                                  _Tr9_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Tr8
                                  _Tr8_NMOSNumberofGate=12,  # number (ref:4)
                                  _Tr8_NMOSChannelWidth=500,  # number (ref:500)
                                  _Tr8_NMOSChannellength=30,  # number (ref:30)
                                  _Tr8_GateSpacing=None,  # None/number
                                  _Tr8_SDWidth=None,  # None/number
                                  _Tr8_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Tr8_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _Tr8_Source_Via_TF=True,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Tr8_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _Tr8_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tr8_NMOSDummy_length=None,  # None/Value
                                  _Tr8_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  ## Tr6
                                  _Tr6_NMOSNumberofGate=6,  # number
                                  _Tr6_NMOSChannelWidth=1000,  # number
                                  _Tr6_NMOSChannellength=30,  # number
                                  _Tr6_GateSpacing=None,  # None/number
                                  _Tr6_SDWidth=None,  # None/number
                                  _Tr6_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Tr6_PCCrit=True,  # None/True

                                  # Tr6 Source_node_ViaM1M2
                                  _Tr6_Source_Via_TF=False,  # True/False

                                  # Tr6 Drain_node_ViaM1M2
                                  _Tr6_Drain_Via_TF=False,  # True/False

                                  # Tr6 POLY dummy setting
                                  _Tr6_NMOSDummy=True,  # TF
                                  # Tr6 if _PMOSDummy == True
                                  _Tr6_NMOSDummy_length=None,  # None/Value
                                  _Tr6_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Tr6 Vp node
                                  _Tr6_Vp_node_width=280,  # Number
                                  _Tr6_Vp_node_metal_Layer=3,  # number

                                  # Tr6 Guardring
                                  # Pbody: number of contact
                                  # Nbody
                                  _Tr6_NwellWidth=850,  # number

                                  # PMOS: Tr11
                                  _Tr11_PMOSNumberofGate=8,
                                  _Tr11_PMOSChannelWidth=500,
                                  _Tr11_PMOSChannellength=30,
                                  _Tr11_GateSpacing=100,
                                  _Tr11_SDWidth=None,
                                  _Tr11_XVT='SLVT',
                                  _Tr11_PCCrit=None,

                                  # Source_node_ViaM1M2
                                  _Tr11_Source_Via_TF=True,

                                  # Drain_node_ViaM1M2
                                  _Tr11_Drain_Via_TF=True,

                                  # POLY dummy setting
                                  _Tr11_PMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tr11_PMOSDummy_length=None,  # None/Value
                                  _Tr11_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Nbodyring(Guardring)
                                  _Tr11_Guardring_NumCont=3,  # number

                                  ## VddTieCell4
                                  # VddTieCell4 NMOS
                                  _Tie4N_NMOSNumberofGate=4,  # number
                                  _Tie4N_NMOSChannelWidth=250,  # number
                                  _Tie4N_NMOSChannellength=30,  # number
                                  _Tie4N_GateSpacing=100,  # None/number
                                  _Tie4N_SDWidth=None,  # None/number
                                  _Tie4N_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Tie4N_PCCrit=True,  # None/True

                                  # VddTieCell4 Source_node_ViaM1M2
                                  _Tie4N_Source_Via_TF=False,  # True/False

                                  # VddTieCell4 Drain_node_ViaM1M2
                                  _Tie4N_Drain_Via_TF=False,  # True/False

                                  # POLY dummy setting
                                  _Tie4N_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tie4N_NMOSDummy_length=400,  # None/Value
                                  _Tie4N_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # VddTieCell4 PMOS
                                  _Tie4P_PMOSNumberofGate=4,  # number
                                  _Tie4P_PMOSChannelWidth=500,  # number
                                  _Tie4P_PMOSChannellength=30,  # number
                                  _Tie4P_GateSpacing=100,  # None/number
                                  _Tie4P_SDWidth=None,  # None/number
                                  _Tie4P_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Tie4P_PCCrit=True,  # None/True

                                  # VddTieCell4 PMOS Source_node_ViaM1M2
                                  _Tie4P_Source_Via_TF=False,  # True/False

                                  # VddTieCell4 PMOS Drain_node_ViaM1M2
                                  _Tie4P_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _Tie4P_PMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tie4P_PMOSDummy_length=None,  # None/Value
                                  _Tie4P_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # VddTieCell4 Number of Body Contact
                                  _Tie4_NBodyCOX=15,
                                  _Tie4_NBodyCOY=3,
                                  _Tie4_PBodyCOX=15,
                                  _Tie4_PBodyCOY=3,

                                  ## VddTieCell8
                                  # VddTieCell8 NMOS
                                  _Tie8N_NMOSNumberofGate=4,  # number
                                  _Tie8N_NMOSChannelWidth=250,  # number
                                  _Tie8N_NMOSChannellength=30,  # number
                                  _Tie8N_GateSpacing=100,  # None/number
                                  _Tie8N_SDWidth=None,  # None/number
                                  _Tie8N_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Tie8N_PCCrit=True,  # None/True

                                  # VddTieCell8 Source_node_ViaM1M2
                                  _Tie8N_Source_Via_TF=False,  # True/False

                                  # VddTieCell8 Drain_node_ViaM1M2
                                  _Tie8N_Drain_Via_TF=False,  # True/False

                                  # POLY dummy setting
                                  _Tie8N_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tie8N_NMOSDummy_length=400,  # None/Value
                                  _Tie8N_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # VddTieCell8 PMOS
                                  _Tie8P_PMOSNumberofGate=4,  # number
                                  _Tie8P_PMOSChannelWidth=500,  # number
                                  _Tie8P_PMOSChannellength=30,  # number
                                  _Tie8P_GateSpacing=100,  # None/number
                                  _Tie8P_SDWidth=None,  # None/number
                                  _Tie8P_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Tie8P_PCCrit=True,  # None/True

                                  # VddTieCell8 PMOS Source_node_ViaM1M2
                                  _Tie8P_Source_Via_TF=False,  # True/False

                                  # VddTieCell8 PMOS Drain_node_ViaM1M2
                                  _Tie8P_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _Tie8P_PMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tie8P_PMOSDummy_length=None,  # None/Value
                                  _Tie8P_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # VddTieCell8 Number of Body Contact
                                  _Tie8_NBodyCOX=15,
                                  _Tie8_NBodyCOY=3,
                                  _Tie8_PBodyCOX=15,
                                  _Tie8_PBodyCOY=3,

                                  # Tr12
                                  _Tr12_NMOSNumberofGate=4,  # number
                                  _Tr12_NMOSChannelWidth=1000,  # number
                                  _Tr12_NMOSChannellength=30,  # number
                                  _Tr12_GateSpacing=None,  # None/number
                                  _Tr12_SDWidth=None,  # None/number
                                  _Tr12_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Tr12_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _Tr12_Source_Via_TF=True,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Tr12_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _Tr12_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tr12_NMOSDummy_length=None,  # None/Value
                                  _Tr12_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Tr3
                                  _Tr3_NMOSNumberofGate=4,  # number
                                  _Tr3_NMOSChannelWidth=500,  # number
                                  _Tr3_NMOSChannellength=30,  # number
                                  _Tr3_GateSpacing=None,  # None/number
                                  _Tr3_SDWidth=None,  # None/number
                                  _Tr3_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Tr3_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _Tr3_Source_Via_TF=True,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Tr3_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _Tr3_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tr3_NMOSDummy_length=None,  # None/Value
                                  _Tr3_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Tr10
                                  _Tr10_NMOSNumberofGate=8,  # number
                                  _Tr10_NMOSChannelWidth=1000,  # number
                                  _Tr10_NMOSChannellength=30,  # number
                                  _Tr10_GateSpacing=None,  # None/number
                                  _Tr10_SDWidth=None,  # None/number
                                  _Tr10_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Tr10_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _Tr10_Source_Via_TF=True,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Tr10_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _Tr10_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tr10_NMOSDummy_length=None,  # None/Value
                                  _Tr10_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Tr12Tr3Tr10 Guardring
                                  _Tr12Tr3Tr10_Guardring_NumCont=3,  # Number

                                  # HDVNCAP_Array
                                  _HDVNCAP_Length = 5000,
                                  _HDVNCAP_LayoutOption = [3,4,5,6],
                                  _HDVNCAP_NumFigPair = 75,
                                  _HDVNCAP_Array = 3, #number: 1xnumber
                                  _HDVNCAP_Cbot_Ctop_metalwidth = 1000, #number
                                  ):

        ## Class_HEADER: Pre Defined Parameter Before Calculation
        CTop_Hrz_M5_PathWidth = 1000
            ## Load DRC library
        _DRCobj = DRC.DRC()
            ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ## CALCULATION START
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')


            ## C13_00(C07C11C12TieCellsRouted) SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C13_00_C07C11C12TieCellsRouted_YJ_v01_00._C07C11C12TieCellsRouted._ParametersForDesignCalculation)

        _Caculation_Parameters['_Tr1Tr2_Tr1_NMOSNumberofGate'] = _Tr1Tr2_Tr1_NMOSNumberofGate
        _Caculation_Parameters['_Tr1Tr2_Tr1_NMOSChannelWidth'] =_Tr1Tr2_Tr1_NMOSChannelWidth
        _Caculation_Parameters['_Tr1Tr2_Tr1_NMOSChannellength'] = _Tr1Tr2_Tr1_NMOSChannellength
        _Caculation_Parameters['_Tr1Tr2_Tr1_GateSpacing'] = _Tr1Tr2_Tr1_GateSpacing
        _Caculation_Parameters['_Tr1Tr2_Tr1_SDWidth'] = _Tr1Tr2_Tr1_SDWidth
        _Caculation_Parameters['_Tr1Tr2_Tr1_XVT'] = _Tr1Tr2_Tr1_XVT
        _Caculation_Parameters['_Tr1Tr2_Tr1_PCCrit'] = _Tr1Tr2_Tr1_PCCrit
        _Caculation_Parameters['_Tr1Tr2_Tr1_Source_Via_TF'] = _Tr1Tr2_Tr1_Source_Via_TF
        _Caculation_Parameters['_Tr1Tr2_Tr1_Drain_Via_TF'] = _Tr1Tr2_Tr1_Drain_Via_TF
        _Caculation_Parameters['_Tr1Tr2_Tr1_NMOSDummy'] = _Tr1Tr2_Tr1_NMOSDummy
        _Caculation_Parameters['_Tr1Tr2_Tr1_NMOSDummy_length'] = _Tr1Tr2_Tr1_NMOSDummy_length

        _Caculation_Parameters['_Tr1Tr2_Tr2_NMOSNumberofGate'] = _Tr1Tr2_Tr2_NMOSNumberofGate
        _Caculation_Parameters['_Tr1Tr2_Tr2_NMOSChannelWidth'] = _Tr1Tr2_Tr2_NMOSChannelWidth
        _Caculation_Parameters['_Tr1Tr2_Tr2_NMOSChannellength'] = _Tr1Tr2_Tr2_NMOSChannellength
        _Caculation_Parameters['_Tr1Tr2_Tr2_GateSpacing'] = _Tr1Tr2_Tr2_GateSpacing
        _Caculation_Parameters['_Tr1Tr2_Tr2_SDWidth'] = _Tr1Tr2_Tr2_SDWidth
        _Caculation_Parameters['_Tr1Tr2_Tr2_XVT'] = _Tr1Tr2_Tr2_XVT
        _Caculation_Parameters['_Tr1Tr2_Tr2_PCCrit'] =_Tr1Tr2_Tr2_PCCrit
        _Caculation_Parameters['_Tr1Tr2_Tr2_Source_Via_TF'] = _Tr1Tr2_Tr2_Source_Via_TF
        _Caculation_Parameters['_Tr1Tr2_Tr2_Drain_Via_TF'] = _Tr1Tr2_Tr2_Drain_Via_TF
        _Caculation_Parameters['_Tr1Tr2_Tr2_NMOSDummy'] = _Tr1Tr2_Tr2_NMOSDummy
        _Caculation_Parameters['_Tr1Tr2_Tr2_NMOSDummy_length'] = _Tr1Tr2_Tr2_NMOSDummy_length
        _Caculation_Parameters['_Tr1Tr2_Tr2_NMOSDummy_placement'] = _Tr1Tr2_Tr2_NMOSDummy_placement
        _Caculation_Parameters['_Tr1Tr2_Inputnode_Metal_layer'] = _Tr1Tr2_Inputnode_Metal_layer
        _Caculation_Parameters['_Tr1Tr2_Inputnode_width'] = _Tr1Tr2_Inputnode_width
        _Caculation_Parameters['_Tr1Tr2_Outputnode_Metal_layer'] = _Tr1Tr2_Outputnode_Metal_layer
        _Caculation_Parameters['_Tr1Tr2_Outputnode_width'] = _Tr1Tr2_Outputnode_width
        _Caculation_Parameters['_Tr1Tr2_NwellWidth'] = _Tr1Tr2_NwellWidth

        _Caculation_Parameters['_Tr4_NMOSNumberofGate']     = _Tr4_NMOSNumberofGate
        _Caculation_Parameters['_Tr4_NMOSChannelWidth']     = _Tr4_NMOSChannelWidth
        _Caculation_Parameters['_Tr4_NMOSChannellength']    = _Tr4_NMOSChannellength
        _Caculation_Parameters['_Tr4_GateSpacing']          = _Tr4_GateSpacing
        _Caculation_Parameters['_Tr4_SDWidth']              = _Tr4_SDWidth
        _Caculation_Parameters['_Tr4_XVT']                  = _Tr4_XVT
        _Caculation_Parameters['_Tr4_PCCrit']               = _Tr4_PCCrit
        _Caculation_Parameters['_Tr4_Source_Via_TF']        = _Tr4_Source_Via_TF
        _Caculation_Parameters['_Tr4_Drain_Via_TF']         = _Tr4_Drain_Via_TF
        _Caculation_Parameters['_Tr4_NMOSDummy']            = _Tr4_NMOSDummy
        _Caculation_Parameters['_Tr4_NMOSDummy_length']     = _Tr4_NMOSDummy_length
        _Caculation_Parameters['_Tr4_NMOSDummy_placement']  = _Tr4_NMOSDummy_placement

        _Caculation_Parameters['_Tr5_PMOSNumberofGate']     = _Tr5_PMOSNumberofGate
        _Caculation_Parameters['_Tr5_PMOSChannelWidth']     = _Tr5_PMOSChannelWidth
        _Caculation_Parameters['_Tr5_PMOSChannellength']    = _Tr5_PMOSChannellength
        _Caculation_Parameters['_Tr5_GateSpacing']          = _Tr5_GateSpacing
        _Caculation_Parameters['_Tr5_SDWidth']              = _Tr5_SDWidth
        _Caculation_Parameters['_Tr5_XVT']                  = _Tr5_XVT
        _Caculation_Parameters['_Tr5_PCCrit']               = _Tr5_PCCrit
        _Caculation_Parameters['_Tr5_Source_Via_TF']        = _Tr5_Source_Via_TF
        _Caculation_Parameters['_Tr5_Drain_Via_TF']         = _Tr5_Drain_Via_TF
        _Caculation_Parameters['_Tr5_PMOSDummy']            = _Tr5_PMOSDummy
        _Caculation_Parameters['_Tr5_PMOSDummy_length']     = _Tr5_PMOSDummy_length
        _Caculation_Parameters['_Tr5_PMOSDummy_placement']  = _Tr5_PMOSDummy_placement

        _Caculation_Parameters['_Tr7_PMOSNumberofGate']     = _Tr7_PMOSNumberofGate
        _Caculation_Parameters['_Tr7_PMOSChannelWidth']     = _Tr7_PMOSChannelWidth
        _Caculation_Parameters['_Tr7_PMOSChannellength']    = _Tr7_PMOSChannellength
        _Caculation_Parameters['_Tr7_GateSpacing']          = _Tr7_GateSpacing
        _Caculation_Parameters['_Tr7_SDWidth']              = _Tr7_SDWidth
        _Caculation_Parameters['_Tr7_XVT']                  = _Tr7_XVT
        _Caculation_Parameters['_Tr7_PCCrit']               = _Tr7_PCCrit
        _Caculation_Parameters['_Tr7_Source_Via_TF']        = _Tr7_Source_Via_TF
        _Caculation_Parameters['_Tr7_Drain_Via_TF']         = _Tr7_Drain_Via_TF
        _Caculation_Parameters['_Tr7_PMOSDummy']            = _Tr7_PMOSDummy
        _Caculation_Parameters['_Tr7_PMOSDummy_length']     = _Tr7_PMOSDummy_length
        _Caculation_Parameters['_Tr7_PMOSDummy_placement']  = _Tr7_PMOSDummy_placement

        _Caculation_Parameters['_Tr9_PMOSNumberofGate']     = _Tr9_PMOSNumberofGate
        _Caculation_Parameters['_Tr9_PMOSChannelWidth']     = _Tr9_PMOSChannelWidth
        _Caculation_Parameters['_Tr9_PMOSChannellength']    = _Tr9_PMOSChannellength
        _Caculation_Parameters['_Tr9_GateSpacing']          = _Tr9_GateSpacing
        _Caculation_Parameters['_Tr9_SDWidth']              = _Tr9_SDWidth
        _Caculation_Parameters['_Tr9_XVT']                  = _Tr9_XVT
        _Caculation_Parameters['_Tr9_PCCrit']               = _Tr9_PCCrit
        _Caculation_Parameters['_Tr9_Source_Via_TF']        = _Tr9_Source_Via_TF
        _Caculation_Parameters['_Tr9_Drain_Via_TF']         = _Tr9_Drain_Via_TF
        _Caculation_Parameters['_Tr9_PMOSDummy']            = _Tr9_PMOSDummy
        _Caculation_Parameters['_Tr9_PMOSDummy_length']     = _Tr9_PMOSDummy_length
        _Caculation_Parameters['_Tr9_PMOSDummy_placement']  = _Tr9_PMOSDummy_placement

        _Caculation_Parameters['_Tr8_NMOSNumberofGate']     = _Tr8_NMOSNumberofGate
        _Caculation_Parameters['_Tr8_NMOSChannelWidth']     = _Tr8_NMOSChannelWidth
        _Caculation_Parameters['_Tr8_NMOSChannellength']    = _Tr8_NMOSChannellength
        _Caculation_Parameters['_Tr8_GateSpacing']          = _Tr8_GateSpacing
        _Caculation_Parameters['_Tr8_SDWidth']              = _Tr8_SDWidth
        _Caculation_Parameters['_Tr8_XVT']                  = _Tr8_XVT
        _Caculation_Parameters['_Tr8_PCCrit']               = _Tr8_PCCrit
        _Caculation_Parameters['_Tr8_Source_Via_TF']        = _Tr8_Source_Via_TF
        _Caculation_Parameters['_Tr8_Drain_Via_TF']         = _Tr8_Drain_Via_TF
        _Caculation_Parameters['_Tr8_NMOSDummy']            = _Tr8_NMOSDummy
        _Caculation_Parameters['_Tr8_NMOSDummy_length']     = _Tr8_NMOSDummy_length
        _Caculation_Parameters['_Tr8_NMOSDummy_placement']  = _Tr8_NMOSDummy_placement

        _Caculation_Parameters['_Tr6_NMOSNumberofGate'] = _Tr6_NMOSNumberofGate
        _Caculation_Parameters['_Tr6_NMOSChannelWidth'] = _Tr6_NMOSChannelWidth
        _Caculation_Parameters['_Tr6_NMOSChannellength'] = _Tr6_NMOSChannellength
        _Caculation_Parameters['_Tr6_GateSpacing'] = _Tr6_GateSpacing
        _Caculation_Parameters['_Tr6_SDWidth'] = _Tr6_SDWidth
        _Caculation_Parameters['_Tr6_XVT'] = _Tr6_XVT
        _Caculation_Parameters['_Tr6_PCCrit'] = _Tr6_PCCrit
        _Caculation_Parameters['_Tr6_Source_Via_TF'] = _Tr6_Source_Via_TF
        _Caculation_Parameters['_Tr6_Drain_Via_TF'] = _Tr6_Drain_Via_TF
        _Caculation_Parameters['_Tr6_NMOSDummy'] = _Tr6_NMOSDummy
        _Caculation_Parameters['_Tr6_NMOSDummy_length'] = _Tr6_NMOSDummy_length
        _Caculation_Parameters['_Tr6_NMOSDummy_placement'] = _Tr6_NMOSDummy_placement
        _Caculation_Parameters['_Tr6_Vp_node_width'] = _Tr6_Vp_node_width
        _Caculation_Parameters['_Tr6_Vp_node_metal_Layer'] = _Tr6_Vp_node_metal_Layer
        _Caculation_Parameters['_Tr6_NwellWidth'] = _Tr6_NwellWidth

        _Caculation_Parameters['_Tr11_PMOSNumberofGate'] = _Tr11_PMOSNumberofGate
        _Caculation_Parameters['_Tr11_PMOSChannelWidth'] = _Tr11_PMOSChannelWidth
        _Caculation_Parameters['_Tr11_PMOSChannellength'] = _Tr11_PMOSChannellength
        _Caculation_Parameters['_Tr11_GateSpacing'] = _Tr11_GateSpacing
        _Caculation_Parameters['_Tr11_SDWidth'] = _Tr11_SDWidth
        _Caculation_Parameters['_Tr11_XVT'] = _Tr11_XVT
        _Caculation_Parameters['_Tr11_PCCrit'] = _Tr11_PCCrit
        _Caculation_Parameters['_Tr11_Source_Via_TF'] = _Tr11_Source_Via_TF
        _Caculation_Parameters['_Tr11_Drain_Via_TF'] = _Tr11_Drain_Via_TF
        _Caculation_Parameters['_Tr11_PMOSDummy'] = _Tr11_PMOSDummy
        _Caculation_Parameters['_Tr11_PMOSDummy_length'] = _Tr11_PMOSDummy_length
        _Caculation_Parameters['_Tr11_PMOSDummy_placement'] = _Tr11_PMOSDummy_placement
        _Caculation_Parameters['_Tr11_Guardring_NumCont'] = _Tr11_Guardring_NumCont

        _Caculation_Parameters['_Tie4N_NMOSNumberofGate'] = _Tie4N_NMOSNumberofGate
        _Caculation_Parameters['_Tie4N_NMOSChannelWidth'] = _Tie4N_NMOSChannelWidth
        _Caculation_Parameters['_Tie4N_NMOSChannellength'] = _Tie4N_NMOSChannellength
        _Caculation_Parameters['_Tie4N_GateSpacing'] = _Tie4N_GateSpacing
        _Caculation_Parameters['_Tie4N_SDWidth'] = _Tie4N_SDWidth
        _Caculation_Parameters['_Tie4N_XVT'] = _Tie4N_XVT
        _Caculation_Parameters['_Tie4N_PCCrit'] = _Tie4N_PCCrit
        _Caculation_Parameters['_Tie4N_Source_Via_TF'] = _Tie4N_Source_Via_TF
        _Caculation_Parameters['_Tie4N_Drain_Via_TF'] = _Tie4N_Drain_Via_TF
        _Caculation_Parameters['_Tie4N_NMOSDummy'] = _Tie4N_NMOSDummy
        _Caculation_Parameters['_Tie4N_NMOSDummy_length'] = _Tie4N_NMOSDummy_length
        _Caculation_Parameters['_Tie4N_NMOSDummy_placement'] = _Tie4N_NMOSDummy_placement
        _Caculation_Parameters['_Tie4P_PMOSNumberofGate'] = _Tie4P_PMOSNumberofGate
        _Caculation_Parameters['_Tie4P_PMOSChannelWidth'] = _Tie4P_PMOSChannelWidth
        _Caculation_Parameters['_Tie4P_PMOSChannellength'] = _Tie4P_PMOSChannellength
        _Caculation_Parameters['_Tie4P_GateSpacing'] = _Tie4P_GateSpacing
        _Caculation_Parameters['_Tie4P_SDWidth'] = _Tie4P_SDWidth
        _Caculation_Parameters['_Tie4P_XVT'] = _Tie4P_XVT
        _Caculation_Parameters['_Tie4P_PCCrit'] = _Tie4P_PCCrit
        _Caculation_Parameters['_Tie4P_Source_Via_TF'] = _Tie4P_Source_Via_TF
        _Caculation_Parameters['_Tie4P_Drain_Via_TF'] = _Tie4P_Drain_Via_TF
        _Caculation_Parameters['_Tie4P_PMOSDummy'] = _Tie4P_PMOSDummy
        _Caculation_Parameters['_Tie4P_PMOSDummy_length'] = _Tie4P_PMOSDummy_length
        _Caculation_Parameters['_Tie4P_PMOSDummy_placement'] = _Tie4P_PMOSDummy_placement
        _Caculation_Parameters['_Tie4_NBodyCOX'] = _Tie4_NBodyCOX
        _Caculation_Parameters['_Tie4_NBodyCOY'] = _Tie4_NBodyCOY
        _Caculation_Parameters['_Tie4_PBodyCOX'] = _Tie4_PBodyCOX
        _Caculation_Parameters['_Tie4_PBodyCOY'] = _Tie4_PBodyCOY

        _Caculation_Parameters['_Tie8N_NMOSNumberofGate'] = _Tie8N_NMOSNumberofGate
        _Caculation_Parameters['_Tie8N_NMOSChannelWidth'] = _Tie8N_NMOSChannelWidth
        _Caculation_Parameters['_Tie8N_NMOSChannellength'] = _Tie8N_NMOSChannellength
        _Caculation_Parameters['_Tie8N_GateSpacing'] = _Tie8N_GateSpacing
        _Caculation_Parameters['_Tie8N_SDWidth'] = _Tie8N_SDWidth
        _Caculation_Parameters['_Tie8N_XVT'] = _Tie8N_XVT
        _Caculation_Parameters['_Tie8N_PCCrit'] = _Tie8N_PCCrit
        _Caculation_Parameters['_Tie8N_Source_Via_TF'] = _Tie8N_Source_Via_TF
        _Caculation_Parameters['_Tie8N_Drain_Via_TF'] = _Tie8N_Drain_Via_TF
        _Caculation_Parameters['_Tie8N_NMOSDummy'] = _Tie8N_NMOSDummy
        _Caculation_Parameters['_Tie8N_NMOSDummy_length'] = _Tie8N_NMOSDummy_length
        _Caculation_Parameters['_Tie8N_NMOSDummy_placement'] = _Tie8N_NMOSDummy_placement
        _Caculation_Parameters['_Tie8P_PMOSNumberofGate'] = _Tie8P_PMOSNumberofGate
        _Caculation_Parameters['_Tie8P_PMOSChannelWidth'] = _Tie8P_PMOSChannelWidth
        _Caculation_Parameters['_Tie8P_PMOSChannellength'] = _Tie8P_PMOSChannellength
        _Caculation_Parameters['_Tie8P_GateSpacing'] = _Tie8P_GateSpacing
        _Caculation_Parameters['_Tie8P_SDWidth'] = _Tie8P_SDWidth
        _Caculation_Parameters['_Tie8P_XVT'] = _Tie8P_XVT
        _Caculation_Parameters['_Tie8P_PCCrit'] = _Tie8P_PCCrit
        _Caculation_Parameters['_Tie8P_Source_Via_TF'] = _Tie8P_Source_Via_TF
        _Caculation_Parameters['_Tie8P_Drain_Via_TF'] = _Tie8P_Drain_Via_TF
        _Caculation_Parameters['_Tie8P_PMOSDummy'] = _Tie8P_PMOSDummy
        _Caculation_Parameters['_Tie8P_PMOSDummy_length'] = _Tie8P_PMOSDummy_length
        _Caculation_Parameters['_Tie8P_PMOSDummy_placement'] = _Tie8P_PMOSDummy_placement
        _Caculation_Parameters['_Tie8_NBodyCOX'] = _Tie8_NBodyCOX
        _Caculation_Parameters['_Tie8_NBodyCOY'] = _Tie8_NBodyCOY
        _Caculation_Parameters['_Tie8_PBodyCOX'] = _Tie8_PBodyCOX
        _Caculation_Parameters['_Tie8_PBodyCOY'] = _Tie8_PBodyCOY

        _Caculation_Parameters['_Tr12_NMOSNumberofGate'] = _Tr12_NMOSNumberofGate
        _Caculation_Parameters['_Tr12_NMOSChannelWidth'] = _Tr12_NMOSChannelWidth
        _Caculation_Parameters['_Tr12_NMOSChannellength'] = _Tr12_NMOSChannellength
        _Caculation_Parameters['_Tr12_GateSpacing'] = _Tr12_GateSpacing
        _Caculation_Parameters['_Tr12_SDWidth'] = _Tr12_SDWidth
        _Caculation_Parameters['_Tr12_XVT'] = _Tr12_XVT
        _Caculation_Parameters['_Tr12_PCCrit'] = _Tr12_PCCrit
        _Caculation_Parameters['_Tr12_Source_Via_TF'] = _Tr12_Source_Via_TF
        _Caculation_Parameters['_Tr12_Drain_Via_TF'] = _Tr12_Drain_Via_TF
        _Caculation_Parameters['_Tr12_NMOSDummy'] = _Tr12_NMOSDummy
        _Caculation_Parameters['_Tr12_NMOSDummy_length'] = _Tr12_NMOSDummy_length
        _Caculation_Parameters['_Tr12_NMOSDummy_placement'] = _Tr12_NMOSDummy_placement

        _Caculation_Parameters['_Tr3_NMOSNumberofGate'] = _Tr3_NMOSNumberofGate
        _Caculation_Parameters['_Tr3_NMOSChannelWidth'] = _Tr3_NMOSChannelWidth
        _Caculation_Parameters['_Tr3_NMOSChannellength'] = _Tr3_NMOSChannellength
        _Caculation_Parameters['_Tr3_GateSpacing'] = _Tr3_GateSpacing
        _Caculation_Parameters['_Tr3_SDWidth'] = _Tr3_SDWidth
        _Caculation_Parameters['_Tr3_XVT'] = _Tr3_XVT
        _Caculation_Parameters['_Tr3_XVT'] = _Tr3_XVT
        _Caculation_Parameters['_Tr3_PCCrit'] = _Tr3_PCCrit
        _Caculation_Parameters['_Tr3_Source_Via_TF'] = _Tr3_Source_Via_TF
        _Caculation_Parameters['_Tr3_Drain_Via_TF'] = _Tr3_Drain_Via_TF
        _Caculation_Parameters['_Tr3_NMOSDummy'] = _Tr3_NMOSDummy
        _Caculation_Parameters['_Tr3_NMOSDummy_length'] = _Tr3_NMOSDummy_length
        _Caculation_Parameters['_Tr3_NMOSDummy_placement'] = _Tr3_NMOSDummy_placement

        _Caculation_Parameters['_Tr10_NMOSNumberofGate'] = _Tr10_NMOSNumberofGate
        _Caculation_Parameters['_Tr10_NMOSChannelWidth'] = _Tr10_NMOSChannelWidth
        _Caculation_Parameters['_Tr10_NMOSChannellength'] = _Tr10_NMOSChannellength
        _Caculation_Parameters['_Tr10_GateSpacing'] = _Tr10_GateSpacing
        _Caculation_Parameters['_Tr10_SDWidth'] = _Tr10_SDWidth
        _Caculation_Parameters['_Tr10_XVT'] = _Tr10_XVT
        _Caculation_Parameters['_Tr10_PCCrit'] = _Tr10_PCCrit
        _Caculation_Parameters['_Tr10_Source_Via_TF'] = _Tr10_Source_Via_TF
        _Caculation_Parameters['_Tr10_Drain_Via_TF'] = _Tr10_Drain_Via_TF
        _Caculation_Parameters['_Tr10_NMOSDummy'] = _Tr10_NMOSDummy
        _Caculation_Parameters['_Tr10_NMOSDummy_length'] = _Tr10_NMOSDummy_length
        _Caculation_Parameters['_Tr10_NMOSDummy_placement'] = _Tr10_NMOSDummy_placement

        _Caculation_Parameters['_Tr12Tr3Tr10_Guardring_NumCont'] = _Tr12Tr3Tr10_Guardring_NumCont

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_C13_00'] = self._SrefElementDeclaration(_DesignObj=C13_00_C07C11C12TieCellsRouted_YJ_v01_00._C07C11C12TieCellsRouted(_DesignParameter=None, _Name='{}:SRF_C13_00'.format(_Name)))[0]

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
        _Caculation_Parameters = copy.deepcopy(C01_04_Guardring._Guardring._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length'] = _HDVNCAP_Length
        _Caculation_Parameters['_LayoutOption'] = _HDVNCAP_LayoutOption
        _Caculation_Parameters['_NumFigPair'] = _HDVNCAP_NumFigPair
        _Caculation_Parameters['_Array'] = _HDVNCAP_Array
        _Caculation_Parameters['_Cbot_Ctop_metalwidth'] = _HDVNCAP_Cbot_Ctop_metalwidth

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_HDVNCAP'] = self._SrefElementDeclaration(_DesignObj=C01_04_Guardring._Guardring(_DesignParameter=None, _Name='{}:SRF_HDVNCAP'.format(_Name)))[0]

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
        target_coord = tmp1[0][0][0][0][0][0][0][0]['_XY_down']
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
        tmp0 = self.get_param_KJH4('SRF_C13_00', 'SRF_C12', 'SRF_C02_04_Guardring', 'SRF_Nbodyring', 'SRF_NbodyTop',
                                   'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        tmp1 = tmp0[0][0][0][0][0][0][0][0]['_XY_up'][1]
        tmp2 = self.get_outter_KJH4('SRF_C13_00', 'SRF_C12', 'SRF_C00_03_Guardring')
        self._DesignParameter['BND_Ctop_Vtc_M5']['_YWidth'] = int(abs(tmp1 - tmp2['_Mostdown']['coord'][0]) + (C01C13_00Space + CTop_Hrz_M5_PathWidth)/2)

                ## Define Boundary_element _XWidth
        Ctop_Vtc_M4_PathWidth = 1000
        self._DesignParameter['BND_Ctop_Vtc_M5']['_XWidth'] = Ctop_Vtc_M4_PathWidth

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Ctop_Vtc_M5']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1_1 = self.get_param_KJH4('SRF_C13_00', 'SRF_Tie8', 'SRF_PMOS_Body_Contact','BND_Nwell')
        tmp1_2 = tmp1
        target_coord = [tmp1_1[0][0][0][0][0]['_XY_right'][0], tmp1_2]
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
        tmp2 = self.get_param_KJH4('SRF_C13_00', 'SRF_C12', 'SRF_C02_04_Guardring', 'SRF_Tr5Tr7Tr9', 'SRF_Tr9', 'BND_Pmos_Gate_Hrz_poly')
        tmp2_1 = tmp2[0][0][0][0][0][0][0]['_XY_left'][0]
        self._DesignParameter['BND_CtopC12Nbodyring_Hrz_M4']['_XWidth'] = abs(tmp1[0][0]['_XY_right'][0] - tmp2_1)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_CtopC12Nbodyring_Hrz_M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp3 = self.get_param_KJH4('SRF_C13_00', 'SRF_C12', 'SRF_C02_04_Guardring','SRF_Nbodyring', 'SRF_NbodyTop', 'SRF_NbodyContactPhyLen','BND_Met1Layer')
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
        self._DesignParameter['SRF_CtopNode_ViaM4M5'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(
                _DesignParameter=None,
                _Name='{}:SRF_Ctop_ViaM4M5'.format(_Name)))[0]

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
        self._DesignParameter['SRF_CtopNode_ViaM4M5']['_DesignObj']._CalculateDesignParameterYmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CtopNode_ViaM4M5']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1_1 = self.get_param_KJH4('BND_CtopC12Nbodyring_Hrz_M4')
        tmp1_2 = self.get_param_KJH4('BND_Ctop_Vtc_M5')
        target_coord = [tmp1_2[0][0]['_XY_cent'][0], tmp1_1[0][0]['_XY_cent'][1]]
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
        self._DesignParameter['SRF_CtopC02Guardring_ViaM1M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(
                _DesignParameter=None,
                _Name='{}:SRF_CtopC02Guardring_ViaM1M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CtopC02Guardring_ViaM1M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CtopC02Guardring_ViaM1M4']['_Angle'] = 0

        ## Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH4('BND_CtopC12Nbodyring_Hrz_M4')
        tmp2 = self.get_param_KJH4('SRF_C13_00', 'SRF_C12', 'SRF_C02_04_Guardring','SRF_Nbodyring', 'SRF_NbodyTop', 'SRF_NbodyContactPhyLen','BND_Met1Layer')
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
        tmp2 = self.get_param_KJH4('SRF_HDVNCAP', 'SRF_Array', 'BND_CTop_METAL{}'.format(_HDVNCAP_LayoutOption[-1]))
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
        tmp1_1 = self.get_param_KJH4('SRF_HDVNCAP', 'SRF_Array', 'BND_CTop_METAL{}'.format(_HDVNCAP_LayoutOption[-1]))
        tmp1_2 = self.get_param_KJH4('BND_CtopNode_Hrz_M5')
        self._DesignParameter['BND_CtopHDVNCap_Vtc_M7']['_YWidth'] = abs(
            tmp1_2[0][0]['_XY_up'][1] - tmp1_1[0][0][0][0]['_XY_down'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CtopHDVNCap_Vtc_M7']['_XWidth'] = _HDVNCAP_Cbot_Ctop_metalwidth

        ## initialized Sref coordinate
        self._DesignParameter['BND_CtopHDVNCap_Vtc_M7']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        for i in range(int((_HDVNCAP_Array+1)/2)):
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
        tmp1_1 = self.get_param_KJH4('SRF_C13_00', 'SRF_Tie4', 'SRF_PMOS_Body_Contact','BND_Nwell')[0][0][0][0][0]['_XY_left'][0]
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
        tmp1 = self.get_param_KJH4('BND_CbotTr6Pbodyring_Hrz_M4')
        target_coord = tmp1[0][0]['_XY_up_right']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CbotTr6Pbodyring_ViaM1M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_right']
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
        tmp2 = self.get_param_KJH4('SRF_C13_00', 'SRF_C07', 'SRF_Tr12Tr3Tr10', 'SRF_Tr12', 'BND_NMOS_Source_Hrz_M2')
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
        self._DesignParameter['SRF_CbotTr12Source_ViaM2M4']['_DesignObj']._CalculateDesignParameterYmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CbotTr12Source_ViaM2M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1_1 = self.get_param_KJH4('BND_Cbot_Vtc_M4')
        tmp1_2 = self.get_param_KJH4('BND_CbotTr12Source_Hrz_M2')
        target_coord = [tmp1_1[0][0]['_XY_cent'][0], tmp1_2[0][0]['_XY_cent'][1]]
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
        tmp1_1 = self.get_param_KJH4('SRF_C13_00', 'SRF_C12', 'SRF_C00_03_Guardring', 'SRF_Pbodyring', 'SRF_PbodyBottom', 'SRF_PbodyContactPhyLen',
                                     'BND_Met1Layer')
        self._DesignParameter['BND_CbotC00Pbodyring_Vtc_M4']['_YWidth'] = abs(
            tmp1_1[0][0][0][0][0][0][0][0]['_XY_up'][1] - tmp1_2[0][0]['_XY_down'][1])

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
        tmp5 = self.get_param_KJH4 ('BND_CbotC00Pbodyring_Vtc_M4')
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
        tmp2 = self.get_param_KJH4('SRF_HDVNCAP', 'SRF_Array', 'BND_CBot_METAL{}'.format(_HDVNCAP_LayoutOption[-1]))
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
        self._DesignParameter['SRF_CbotC00Pbodyring_ViaM1M4']['_DesignObj']._CalculateDesignParameterYmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CbotC00Pbodyring_ViaM1M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1_2 = self.get_param_KJH4('SRF_C13_00', 'SRF_C12', 'SRF_C00_03_Guardring', 'SRF_Pbodyring', 'SRF_PbodyBottom', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        target_coord = [tmp2[0][0]['_XY_cent'][0], tmp1_2[0][0][0][0][0][0][0][0]['_XY_cent'][1]]
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
        tmp1_1 = self.get_param_KJH4('SRF_HDVNCAP', 'SRF_Array', 'BND_CBot_METAL{}'.format(_HDVNCAP_LayoutOption[-1]))
        tmp1_2 = self.get_param_KJH4('BND_CbotNode_Hrz_M4')
        self._DesignParameter['BND_CbotHDVNCap_Vtc_M7']['_YWidth'] = abs(tmp1_2[0][0]['_XY_up'][1] - tmp1_1[0][0][0][0]['_XY_down'][1])

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CbotHDVNCap_Vtc_M7']['_XWidth'] = _HDVNCAP_Cbot_Ctop_metalwidth

        ## initialized Sref coordinate
        self._DesignParameter['BND_CbotHDVNCap_Vtc_M7']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        for i in range(math.ceil((_HDVNCAP_Array+1)/2)):
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
        for i in range(math.ceil((_HDVNCAP_Array+1)/2)):
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

        tmp1 = self.get_param_KJH4('SRF_HDVNCAP', 'SRF_Array', 'BND_CBot_METAL{}'.format(_HDVNCAP_LayoutOption[-1]))
        tmp2 = self.get_param_KJH4('BND_CbotHDVNCap_Vtc_M7')

        ## Calculate Sref XYcoord
        tmpXY = []
        for i in range(int((_HDVNCAP_Array + 1) / 2)):
            ## Calcuate Overlapped XYcoord
            Ovlpcoord = self.get_ovlp_KJH2(tmp2[i][0], tmp1[0][0][i][0])

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
            _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'],
                                                        'MinEnclosureY')

            ## Define _COX and _COY
            _Caculation_Parameters['_COX'] = _COX
            _Caculation_Parameters['_COY'] = _COY

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
            self._DesignParameter['SRF_HDVNCapCbotHrzPath_ViaM6M7']['_DesignObj']._CalculateDesignParameterYmin(
                **_Caculation_Parameters)

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
        for i in range(int((_HDVNCAP_Array+1)/2)):
            ## Calcuate Overlapped XYcoord
            Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[i][0])

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
            _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'],
                                                        'MinEnclosureY')

            ## Define _COX and _COY
            _Caculation_Parameters['_COX'] = _COX
            _Caculation_Parameters['_COY'] = _COY

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
            self._DesignParameter['SRF_HDVNCapCtopHrzPath_ViaM4M7']['_DesignObj']._CalculateDesignParameterYmin(
                **_Caculation_Parameters)

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

        tmp1 = self.get_param_KJH4('SRF_HDVNCAP', 'SRF_Array', 'BND_CTop_METAL{}'.format(_HDVNCAP_LayoutOption[-1]))
        tmp2 = self.get_param_KJH4('BND_CtopHDVNCap_Vtc_M7')

        ## Calculate Sref XYcoord
        tmpXY = []
        for i in range(int((_HDVNCAP_Array+1)/2)):
            ## Calcuate Overlapped XYcoord
            Ovlpcoord = self.get_ovlp_KJH2(tmp2[i][0], tmp1[0][0][i][0])

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
            _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'],
                                                        'MinEnclosureY')

            ## Define _COX and _COY
            _Caculation_Parameters['_COX'] = _COX
            _Caculation_Parameters['_COY'] = _COY

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
            self._DesignParameter['SRF_HDVNCapCtopHrzPath_ViaM6M7']['_DesignObj']._CalculateDesignParameterYmin(
                **_Caculation_Parameters)

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
        tmp1_1 = self.get_param_KJH4('SRF_C13_00', 'SRF_C12', 'SRF_C00_03_Guardring','SRF_Tr1Tr2','SRF_Tr1','SRF_Tr1_Source_ViaM1Mx','SRF_ViaM1M2','BND_Met1Layer')
        tmp1_2 = self.get_param_KJH4('SRF_C13_00', 'SRF_C12', 'SRF_C00_03_Guardring','SRF_Tr1Tr2','SRF_Tr2','SRF_Tr2_Drain_ViaM1Mx','SRF_ViaM1M2','BND_Met1Layer')
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
        tmp1 = self.get_param_KJH4('SRF_C13_00', 'SRF_C12', 'SRF_C00_03_Guardring','SRF_Tr1Tr2','SRF_Tr1','SRF_Tr1_Drain_ViaM1Mx','SRF_ViaM1M2','BND_Met1Layer')
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





############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    Start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_Samsung_Bootstrapped'
    cellname = 'C13_01_CtopCbotRouted_YJ_v2'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
	    
	    #### Bootstrap Sampler
	    # Tr1 and Tr2
	    # Tr1
	    _Tr1Tr2_Tr1_NMOSNumberofGate=2,  # number
	    _Tr1Tr2_Tr1_NMOSChannelWidth=3000,  # number
	    _Tr1Tr2_Tr1_NMOSChannellength=30,  # number
	    _Tr1Tr2_Tr1_GateSpacing=222,  # None/number
	    _Tr1Tr2_Tr1_SDWidth=None,  # None/number
	    _Tr1Tr2_Tr1_XVT='LVT',  # 'XVT' ex)SLVT LVT RVT HVT
	    _Tr1Tr2_Tr1_PCCrit=True,  # None/True
	    
	    # Source_node_ViaM1M2
	    _Tr1Tr2_Tr1_Source_Via_TF=False,  # True/False
	    
	    # Drain_node_ViaM1M2
	    _Tr1Tr2_Tr1_Drain_Via_TF=False,  # True/False
	    
	    # POLY dummy setting
	    _Tr1Tr2_Tr1_NMOSDummy=True,  # TF
	    # if _PMOSDummy == True
	    _Tr1Tr2_Tr1_NMOSDummy_length=None,  # None/Value
	    _Tr1Tr2_Tr1_NMOSDummy_placement=None,  # None/'Up'/'Dn'/
	    
	    # Tr2
	    _Tr1Tr2_Tr2_NMOSNumberofGate=8,  # number
	    _Tr1Tr2_Tr2_NMOSChannelWidth=3000,  # number
	    _Tr1Tr2_Tr2_NMOSChannellength=30,  # number
	    _Tr1Tr2_Tr2_GateSpacing=100,  # None/number
	    _Tr1Tr2_Tr2_SDWidth=None,  # None/number
	    _Tr1Tr2_Tr2_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
	    _Tr1Tr2_Tr2_PCCrit=True,  # None/True
	    
	    # Source_node_ViaM1M2
	    _Tr1Tr2_Tr2_Source_Via_TF=False,  # True/False
	    
	    # Drain_node_ViaM1M2
	    _Tr1Tr2_Tr2_Drain_Via_TF=False,  # True/False
	    
	    # POLY dummy setting
	    _Tr1Tr2_Tr2_NMOSDummy=True,  # TF
	    # if _PMOSDummy == True
	    _Tr1Tr2_Tr2_NMOSDummy_length=None,  # None/Value
	    _Tr1Tr2_Tr2_NMOSDummy_placement=None,  # None/'Up'/'Dn'/
	    
	    # Input/Output node
	    # INPUT node
	    _Tr1Tr2_Inputnode_Metal_layer=6,  # number
	    _Tr1Tr2_Inputnode_width=600,  # number
	    
	    # OUTPUT node
	    _Tr1Tr2_Outputnode_Metal_layer=6,  # number
	    _Tr1Tr2_Outputnode_width=600,  # number
	    
	    # Guardring
	    # Pbody: number of contact
	    # Nbody
	    _Tr1Tr2_NwellWidth=850,  # number
	    
	    # Tr4
	    _Tr4_NMOSNumberofGate=4,  # number
	    _Tr4_NMOSChannelWidth=1000,  # number
	    _Tr4_NMOSChannellength=30,  # number
	    _Tr4_GateSpacing=None,  # None/number
	    _Tr4_SDWidth=None,  # None/number
	    _Tr4_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
	    _Tr4_PCCrit=True,  # None/True
	    
	    # Source_node_ViaM1M2
	    _Tr4_Source_Via_TF=True,  # True/False
	    
	    # Drain_node_ViaM1M2
	    _Tr4_Drain_Via_TF=True,  # True/False
	    
	    # POLY dummy setting
	    _Tr4_NMOSDummy=True,  # TF
	    # if _PMOSDummy == True
	    _Tr4_NMOSDummy_length=None,  # None/Value
	    _Tr4_NMOSDummy_placement=None,  # None/'Up'/'Dn'/
	    
	    # Tr5 Tr7 Tr9
	    # PMOS: Tr5
	    _Tr5_PMOSNumberofGate=2,
	    _Tr5_PMOSChannelWidth=1000,  # ref=1000
	    _Tr5_PMOSChannellength=30,
	    _Tr5_GateSpacing=100,
	    _Tr5_SDWidth=None,
	    _Tr5_XVT='SLVT',
	    _Tr5_PCCrit=None,
	    
	    # Source_node_ViaM1M2
	    _Tr5_Source_Via_TF=True,
	    
	    # Drain_node_ViaM1M2
	    _Tr5_Drain_Via_TF=True,
	    
	    # POLY dummy setting
	    _Tr5_PMOSDummy=True,  # TF
	    # if _PMOSDummy == True
	    _Tr5_PMOSDummy_length=None,  # None/Value
	    _Tr5_PMOSDummy_placement=None,  # None/'Up'/'Dn'/
	    
	    # PMOS: Tr7
	    _Tr7_PMOSNumberofGate=2,
	    _Tr7_PMOSChannelWidth=1000,
	    _Tr7_PMOSChannellength=30,
	    _Tr7_GateSpacing=100,
	    _Tr7_SDWidth=None,
	    _Tr7_XVT='SLVT',
	    _Tr7_PCCrit=None,
	    
	    # Source_node_ViaM1M2
	    _Tr7_Source_Via_TF=True,
	    
	    # Drain_node_ViaM1M2
	    _Tr7_Drain_Via_TF=True,
	    
	    # POLY dummy setting
	    _Tr7_PMOSDummy=True,  # TF
	    # if _PMOSDummy == True
	    _Tr7_PMOSDummy_length=None,  # None/Value
	    _Tr7_PMOSDummy_placement=None,  # None/'Up'/'Dn'/
	    
	    # PMOS: Tr9
	    _Tr9_PMOSNumberofGate=4,
	    _Tr9_PMOSChannelWidth=1000,  # ref = 1000
	    _Tr9_PMOSChannellength=30,
	    _Tr9_GateSpacing=100,
	    _Tr9_SDWidth=None,
	    _Tr9_XVT='SLVT',
	    _Tr9_PCCrit=None,
	    
	    # Source_node_ViaM1M2
	    _Tr9_Source_Via_TF=True,
	    
	    # Drain_node_ViaM1M2
	    _Tr9_Drain_Via_TF=True,
	    
	    # POLY dummy setting
	    _Tr9_PMOSDummy=True,  # TF
	    # if _PMOSDummy == True
	    _Tr9_PMOSDummy_length=None,  # None/Value
	    _Tr9_PMOSDummy_placement=None,  # None/'Up'/'Dn'/
	    
	    # Tr8
	    _Tr8_NMOSNumberofGate=4,  # number (ref:4)
	    _Tr8_NMOSChannelWidth=1000,  # number (ref:500)
	    _Tr8_NMOSChannellength=30,  # number (ref:30)
	    _Tr8_GateSpacing=None,  # None/number
	    _Tr8_SDWidth=None,  # None/number
	    _Tr8_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
	    _Tr8_PCCrit=True,  # None/True
	    
	    # Source_node_ViaM1M2
	    _Tr8_Source_Via_TF=True,  # True/False
	    
	    # Drain_node_ViaM1M2
	    _Tr8_Drain_Via_TF=True,  # True/False
	    
	    # POLY dummy setting
	    _Tr8_NMOSDummy=True,  # TF
	    # if _PMOSDummy == True
	    _Tr8_NMOSDummy_length=None,  # None/Value
	    _Tr8_NMOSDummy_placement=None,  # None/'Up'/'Dn'/
	    
	    ## Tr6
	    _Tr6_NMOSNumberofGate=1,  # number
	    _Tr6_NMOSChannelWidth=1000,  # number
	    _Tr6_NMOSChannellength=30,  # number
	    _Tr6_GateSpacing=None,  # None/number
	    _Tr6_SDWidth=None,  # None/number
	    _Tr6_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
	    _Tr6_PCCrit=True,  # None/True
	    
	    # Tr6 Source_node_ViaM1M2
	    _Tr6_Source_Via_TF=False,  # True/False
	    
	    # Tr6 Drain_node_ViaM1M2
	    _Tr6_Drain_Via_TF=False,  # True/False
	    
	    # Tr6 POLY dummy setting
	    _Tr6_NMOSDummy=True,  # TF
	    # Tr6 if _PMOSDummy == True
	    _Tr6_NMOSDummy_length=None,  # None/Value
	    _Tr6_NMOSDummy_placement=None,  # None/'Up'/'Dn'/
	    
	    # Tr6 Vp node
	    _Tr6_Vp_node_width=280,  # Number
	    _Tr6_Vp_node_metal_Layer=3,  # number
	    
	    # Tr6 Guardring
	    # Pbody: number of contact
	    # Nbody
	    _Tr6_NwellWidth=850,  # number
	    
	    # PMOS: Tr11
	    _Tr11_PMOSNumberofGate=1,
	    _Tr11_PMOSChannelWidth=1000,
	    _Tr11_PMOSChannellength=30,
	    _Tr11_GateSpacing=None,
	    _Tr11_SDWidth=None,
	    _Tr11_XVT='SLVT',
	    _Tr11_PCCrit=None,
	    
	    # Source_node_ViaM1M2
	    _Tr11_Source_Via_TF=True,
	    
	    # Drain_node_ViaM1M2
	    _Tr11_Drain_Via_TF=True,
	    
	    # POLY dummy setting
	    _Tr11_PMOSDummy=True,  # TF
	    # if _PMOSDummy == True
	    _Tr11_PMOSDummy_length=None,  # None/Value
	    _Tr11_PMOSDummy_placement=None,  # None/'Up'/'Dn'/
	    
	    # Nbodyring(Guardring)
	    _Tr11_Guardring_NumCont=3,  # number
	    
	    ## VddTieCell4
	    # VddTieCell4 NMOS
	    _Tie4N_NMOSNumberofGate=4,  # number
	    _Tie4N_NMOSChannelWidth=250,  # number
	    _Tie4N_NMOSChannellength=30,  # number
	    _Tie4N_GateSpacing=100,  # None/number
	    _Tie4N_SDWidth=None,  # None/number
	    _Tie4N_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
	    _Tie4N_PCCrit=True,  # None/True
	    
	    # VddTieCell4 Source_node_ViaM1M2
	    _Tie4N_Source_Via_TF=False,  # True/False
	    
	    # VddTieCell4 Drain_node_ViaM1M2
	    _Tie4N_Drain_Via_TF=False,  # True/False
	    
	    # POLY dummy setting
	    _Tie4N_NMOSDummy=True,  # TF
	    # if _PMOSDummy == True
	    _Tie4N_NMOSDummy_length=400,  # None/Value
	    _Tie4N_NMOSDummy_placement=None,  # None/'Up'/'Dn'/
	    
	    # VddTieCell4 PMOS
	    _Tie4P_PMOSNumberofGate=4,  # number
	    _Tie4P_PMOSChannelWidth=500,  # number
	    _Tie4P_PMOSChannellength=30,  # number
	    _Tie4P_GateSpacing=100,  # None/number
	    _Tie4P_SDWidth=None,  # None/number
	    _Tie4P_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
	    _Tie4P_PCCrit=True,  # None/True
	    
	    # VddTieCell4 PMOS Source_node_ViaM1M2
	    _Tie4P_Source_Via_TF=False,  # True/False
	    
	    # VddTieCell4 PMOS Drain_node_ViaM1M2
	    _Tie4P_Drain_Via_TF=True,  # True/False
	    
	    # POLY dummy setting
	    _Tie4P_PMOSDummy=True,  # TF
	    # if _PMOSDummy == True
	    _Tie4P_PMOSDummy_length=None,  # None/Value
	    _Tie4P_PMOSDummy_placement=None,  # None/'Up'/'Dn'/
	    
	    # VddTieCell4 Number of Body Contact
	    _Tie4_NBodyCOX=15,
	    _Tie4_NBodyCOY=3,
	    _Tie4_PBodyCOX=15,
	    _Tie4_PBodyCOY=3,
	    
	    ## VddTieCell8
	    # VddTieCell8 NMOS
	    _Tie8N_NMOSNumberofGate=4,  # number
	    _Tie8N_NMOSChannelWidth=250,  # number
	    _Tie8N_NMOSChannellength=30,  # number
	    _Tie8N_GateSpacing=100,  # None/number
	    _Tie8N_SDWidth=None,  # None/number
	    _Tie8N_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
	    _Tie8N_PCCrit=True,  # None/True
	    
	    # VddTieCell8 Source_node_ViaM1M2
	    _Tie8N_Source_Via_TF=False,  # True/False
	    
	    # VddTieCell8 Drain_node_ViaM1M2
	    _Tie8N_Drain_Via_TF=False,  # True/False
	    
	    # POLY dummy setting
	    _Tie8N_NMOSDummy=True,  # TF
	    # if _PMOSDummy == True
	    _Tie8N_NMOSDummy_length=400,  # None/Value
	    _Tie8N_NMOSDummy_placement=None,  # None/'Up'/'Dn'/
	    
	    # VddTieCell8 PMOS
	    _Tie8P_PMOSNumberofGate=4,  # number
	    _Tie8P_PMOSChannelWidth=500,  # number
	    _Tie8P_PMOSChannellength=30,  # number
	    _Tie8P_GateSpacing=100,  # None/number
	    _Tie8P_SDWidth=None,  # None/number
	    _Tie8P_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
	    _Tie8P_PCCrit=True,  # None/True
	    
	    # VddTieCell8 PMOS Source_node_ViaM1M2
	    _Tie8P_Source_Via_TF=False,  # True/False
	    
	    # VddTieCell8 PMOS Drain_node_ViaM1M2
	    _Tie8P_Drain_Via_TF=True,  # True/False
	    
	    # POLY dummy setting
	    _Tie8P_PMOSDummy=True,  # TF
	    # if _PMOSDummy == True
	    _Tie8P_PMOSDummy_length=None,  # None/Value
	    _Tie8P_PMOSDummy_placement=None,  # None/'Up'/'Dn'/
	    
	    # VddTieCell8 Number of Body Contact
	    _Tie8_NBodyCOX=15,
	    _Tie8_NBodyCOY=3,
	    _Tie8_PBodyCOX=15,
	    _Tie8_PBodyCOY=3,
	    
	    # Tr12
	    _Tr12_NMOSNumberofGate=1,  # number
	    _Tr12_NMOSChannelWidth=1000,  # number
	    _Tr12_NMOSChannellength=30,  # number
	    _Tr12_GateSpacing=None,  # None/number
	    _Tr12_SDWidth=None,  # None/number
	    _Tr12_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
	    _Tr12_PCCrit=True,  # None/True
	    
	    # Source_node_ViaM1M2
	    _Tr12_Source_Via_TF=True,  # True/False
	    
	    # Drain_node_ViaM1M2
	    _Tr12_Drain_Via_TF=True,  # True/False
	    
	    # POLY dummy setting
	    _Tr12_NMOSDummy=True,  # TF
	    # if _PMOSDummy == True
	    _Tr12_NMOSDummy_length=None,  # None/Value
	    _Tr12_NMOSDummy_placement=None,  # None/'Up'/'Dn'/
	    
	    # Tr3
	    _Tr3_NMOSNumberofGate=15,  # number
	    _Tr3_NMOSChannelWidth=3000,  # number
	    _Tr3_NMOSChannellength=40,  # number
	    _Tr3_GateSpacing=None,  # None/number
	    _Tr3_SDWidth=None,  # None/number
	    _Tr3_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
	    _Tr3_PCCrit=True,  # None/True
	    
	    # Source_node_ViaM1M2
	    _Tr3_Source_Via_TF=True,  # True/False
	    
	    # Drain_node_ViaM1M2
	    _Tr3_Drain_Via_TF=True,  # True/False
	    
	    # POLY dummy setting
	    _Tr3_NMOSDummy=True,  # TF
	    # if _PMOSDummy == True
	    _Tr3_NMOSDummy_length=None,  # None/Value
	    _Tr3_NMOSDummy_placement=None,  # None/'Up'/'Dn'/
	    
	    # Tr10
	    _Tr10_NMOSNumberofGate=4,  # number
	    _Tr10_NMOSChannelWidth=1000,  # number
	    _Tr10_NMOSChannellength=30,  # number
	    _Tr10_GateSpacing=None,  # None/number
	    _Tr10_SDWidth=None,  # None/number
	    _Tr10_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
	    _Tr10_PCCrit=True,  # None/True
	    
	    # Source_node_ViaM1M2
	    _Tr10_Source_Via_TF=True,  # True/False
	    
	    # Drain_node_ViaM1M2
	    _Tr10_Drain_Via_TF=True,  # True/False
	    
	    # POLY dummy setting
	    _Tr10_NMOSDummy=True,  # TF
	    # if _PMOSDummy == True
	    _Tr10_NMOSDummy_length=None,  # None/Value
	    _Tr10_NMOSDummy_placement=None,  # None/'Up'/'Dn'/
	    
	    # Tr12Tr3Tr10 Guardring
	    _Tr12Tr3Tr10_Guardring_NumCont=3,  # Number
	    
	    # HDVNCAP_Array
	    _HDVNCAP_Length=22000,
	    _HDVNCAP_LayoutOption=[5, 6],
	    _HDVNCAP_NumFigPair=80,
	    _HDVNCAP_Array=3,  # number: 1xnumber
	    _HDVNCAP_Cbot_Ctop_metalwidth=1000,  # number
	    
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
    elapsed_time = time.time() - Start_time
    m, s = divmod(elapsed_time, 60)
    h, m = divmod(m, 60)

    print('#############################      Finished      ################################')
# end of 'main():' ---------------------------------------------------------------------------------------------

















