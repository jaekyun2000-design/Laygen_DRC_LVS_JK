## Import Basic Modules
    ## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC
#from KJH91_Projects.Project_ADC.Library_and_Engine import DRCv2

    ## Library
import copy
import time

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.C11_Tr6Tr11_YJH import C11_00_Tr6Tr11Routed_v02
from KJH91_Projects.Project_ADC.Layoutgen_code.C12_Tr1Tr2_Tr5Tr7Tr9_Tr4_Tr8_KJH import C12_00_Tr1Tr2_Tr5Tr7Tr9_Tr4_Tr8
from KJH91_Projects.Project_ADC.Layoutgen_code.C06_Tie4_YJH import C06_00_VddTieCell
from KJH91_Projects.Project_ADC.Layoutgen_code.C10_Tie8_YJH import C10_00_VddTieCell
from KJH91_Projects.Project_ADC.Layoutgen_code.C07_Tr12Tr3Tr10_KJH import C07_04_Guardring


## Define Class
class _C07C11C12TieCellsRouted(StickDiagram_KJH1._StickDiagram_KJH):

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
        _Tr1Tr2_Tr2_GateSpacing=222,  # None/number
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
        _Tr5_GateSpacing=None,
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
        _Tr7_GateSpacing=None,
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
        _Tr9_GateSpacing=None,
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
        _Tr8_NMOSNumberofGate=10,  # number (ref:4)
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
        _Tr6_NMOSNumberofGate=4,  # number
        _Tr6_NMOSChannelWidth=500,  # number
        _Tr6_NMOSChannellength=30,  # number
        _Tr6_GateSpacing=100,  # None/number
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
        _Tr6_Vp_node_metal_Layer=4,  # number

        # Tr6 Guardring
        # Pbody: number of contact
        # Nbody
        _Tr6_NwellWidth=850,  # number

        # PMOS: Tr11
        _Tr11_PMOSNumberofGate=4,
        _Tr11_PMOSChannelWidth=1000,
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
        _Tie4N_NMOSNumberofGate = 4,  # number
        _Tie4N_NMOSChannelWidth = 250,  # number
        _Tie4N_NMOSChannellength = 30,  # number
        _Tie4N_GateSpacing = 100,  # None/number
        _Tie4N_SDWidth = None,  # None/number
        _Tie4N_XVT = 'SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Tie4N_PCCrit = True,  # None/True

        # VddTieCell4 Source_node_ViaM1M2
        _Tie4N_Source_Via_TF = False,  # True/False

        # VddTieCell4 Drain_node_ViaM1M2
        _Tie4N_Drain_Via_TF = False,  # True/False

        # POLY dummy setting
        _Tie4N_NMOSDummy = True,  # TF
        # if _PMOSDummy == True
        _Tie4N_NMOSDummy_length = None,  # None/Value
        _Tie4N_NMOSDummy_placement = None,  # None/'Up'/'Dn'/

        # VddTieCell4 PMOS
        _Tie4P_PMOSNumberofGate = 4,  # number
        _Tie4P_PMOSChannelWidth = 500,  # number
        _Tie4P_PMOSChannellength = 30,  # number
        _Tie4P_GateSpacing = 100,  # None/number
        _Tie4P_SDWidth = None,  # None/number
        _Tie4P_XVT = 'SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Tie4P_PCCrit = True,  # None/True

        # VddTieCell4 PMOS Source_node_ViaM1M2
        _Tie4P_Source_Via_TF = False,  # True/False

        # VddTieCell4 PMOS Drain_node_ViaM1M2
        _Tie4P_Drain_Via_TF = True,  # True/False

        # POLY dummy setting
        _Tie4P_PMOSDummy = True,  # TF
        # if _PMOSDummy == True
        _Tie4P_PMOSDummy_length = None,  # None/Value
        _Tie4P_PMOSDummy_placement = None,  # None/'Up'/'Dn'/

        # VddTieCell4 Number of Body Contact
        _Tie4_NBodyCOX = 15,
        _Tie4_NBodyCOY = 3,
        _Tie4_PBodyCOX = 15,
        _Tie4_PBodyCOY = 3,

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
        _Tie8N_NMOSDummy_length=None,  # None/Value
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
        _Tr12_NMOSChannelWidth=500,  # number
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
        _Tr10_NMOSNumberofGate=4,  # number
        _Tr10_NMOSChannelWidth=500,  # number
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
                                  _Tr1Tr2_Tr2_GateSpacing=222,  # None/number
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
                                  _Tr5_GateSpacing=None,
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
                                  _Tr7_GateSpacing=None,
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
                                  _Tr9_GateSpacing=None,
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
                                  _Tr8_NMOSNumberofGate=10,  # number (ref:4)
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
                                  _Tr6_NMOSNumberofGate=4,  # number
                                  _Tr6_NMOSChannelWidth=500,  # number
                                  _Tr6_NMOSChannellength=30,  # number
                                  _Tr6_GateSpacing=100,  # None/number
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
                                  _Tr6_Vp_node_metal_Layer=4,  # number

                                  # Tr6 Guardring
                                  # Pbody: number of contact
                                  # Nbody
                                  _Tr6_NwellWidth=850,  # number

                                  # PMOS: Tr11
                                  _Tr11_PMOSNumberofGate=4,
                                  _Tr11_PMOSChannelWidth=1000,
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
                                  _Tie4N_NMOSDummy_length=None,  # None/Value
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
                                  _Tie8N_NMOSDummy_length=None,  # None/Value
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
                                  _Tr12_NMOSChannelWidth=500,  # number
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
                                  _Tr10_NMOSNumberofGate=4,  # number
                                  _Tr10_NMOSChannelWidth=500,  # number
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


            ## C12(Tr(1,2) - Tr(5,7,9) Routed) SREF Generation
        _Caculation_Parameters = copy.deepcopy(C12_00_Tr1Tr2_Tr5Tr7Tr9_Tr4_Tr8._Tr1Tr2_Tr5Tr7Tr9_Tr4_Tr8._ParametersForDesignCalculation)

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


            ## _C11(Tr6 - Tr11 Routed) SREF Generation
        _Caculation_Parameters = copy.deepcopy(C11_00_Tr6Tr11Routed_v02._Tr4Tr6Routed._ParametersForDesignCalculation)

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
        tmp1_1 = self.get_outter_KJH4('SRF_C12','SRF_C05_02_Pin')['_Mostright']['coord'][0]
        tmp1_2 = self.get_param_KJH4('SRF_C12','SRF_C02_04_Guardring','BND_Deepnwell')
        target_coord = [tmp1_1, tmp1_2[0][0][0][0]['_XY_up'][1]]
        ## Approaching_coord: _XY_type2
        tmp2_1 = self.get_outter_KJH4('SRF_C11')['_Mostright']['coord'][0]
        tmp2_2 = self.get_param_KJH4('SRF_C11', 'SRF_Tr6','SRF_Nbodyring', 'SRF_NbodyBottom', 'SRF_NbodyContactPhyLen', 'BND_Nwell')
        approaching_coord = [tmp2_1, tmp2_2[0][0][0][0][0][0][0]['_XY_down'][1]]
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

        tmp3_1 = self.get_outter_KJH4('SRF_C12','SRF_C05_02_Pin')['_Mostup']['coord'][0]
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



        ## Vp node M4 HrzRoute Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_VpNode_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_C11', 'BND_Tr6Drain_Hrz_M3')
        tmp2 = self.get_param_KJH4('SRF_C12', 'SRF_C02_04_Guardring', 'BND_Tr5Tr7_Gate_Hrz_M3')
        if tmp1[0][0][0]['_XY_down_right'][0] - tmp2[0][0][0][0]['_XY_down_right'][0] < 0:
            raise Exception(f"BND_VpNode_Hrz_M3 is not routable")       # 0이 아니라 『 에서 hrz 부분 최소 길이 DRC로 확인 필요
        self._DesignParameter['BND_VpNode_Hrz_M3']['_YWidth'] = abs(tmp1[0][0][0]['_Ywidth'])

                ## Define Boundary_element _XWidth
        C11Tr5GateM4VtcRoutePathWidth = 300
        self._DesignParameter['BND_VpNode_Hrz_M3']['_XWidth'] = abs(tmp1[0][0][0]['_XY_down_right'][0] - tmp2[0][0][0][0]['_XY_down_right'][0]) + C11Tr5GateM4VtcRoutePathWidth

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_VpNode_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_VpNode_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0]['_XY_down_right']
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


        ## Vp node M4 VtcRoute Boundary_element Generation
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
        self._DesignParameter['BND_VpNode_Vtc_M3']['_YWidth'] = abs(tmp1[0][0]['_XY_up_left'][1] - tmp1_2[0][0][0][0]['_XY_down_right'][1])

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_VpNode_Vtc_M3']['_XWidth'] = C11Tr5GateM4VtcRoutePathWidth

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
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_VpNode_Vtc_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_VpNode_Vtc_M3']['_XYCoordinates'] = tmpXY


        ## Tie4 Sref generation
        _Caculation_Parameters = copy.deepcopy(C06_00_VddTieCell._TieCell4._ParametersForDesignCalculation)

        _Caculation_Parameters['_TieN_NMOSNumberofGate'] = _Tie4N_NMOSNumberofGate
        _Caculation_Parameters['_TieN_NMOSChannelWidth'] = _Tie4N_NMOSChannelWidth
        _Caculation_Parameters['_TieN_NMOSChannellength'] = _Tie4N_NMOSChannellength
        _Caculation_Parameters['_TieN_GateSpacing'] = _Tie4N_GateSpacing
        _Caculation_Parameters['_TieN_SDWidth'] = _Tie4N_SDWidth
        _Caculation_Parameters['_TieN_XVT'] = _Tie4N_XVT
        _Caculation_Parameters['_TieN_PCCrit'] = _Tie4N_PCCrit
        _Caculation_Parameters['_TieN_Source_Via_TF'] = _Tie4N_Source_Via_TF
        _Caculation_Parameters['_TieN_Drain_Via_TF'] = _Tie4N_Drain_Via_TF
        _Caculation_Parameters['_TieN_NMOSDummy'] = _Tie4N_NMOSDummy
        _Caculation_Parameters['_TieN_NMOSDummy_length'] = _Tie4N_NMOSDummy_length
        _Caculation_Parameters['_TieN_NMOSDummy_placement'] = _Tie4N_NMOSDummy_placement
        _Caculation_Parameters['_TieP_PMOSNumberofGate'] = _Tie4P_PMOSNumberofGate
        _Caculation_Parameters['_TieP_PMOSChannelWidth'] = _Tie4P_PMOSChannelWidth
        _Caculation_Parameters['_TieP_PMOSChannellength'] = _Tie4P_PMOSChannellength
        _Caculation_Parameters['_TieP_GateSpacing'] = _Tie4P_GateSpacing
        _Caculation_Parameters['_TieP_SDWidth'] = _Tie4P_SDWidth
        _Caculation_Parameters['_TieP_XVT'] = _Tie4P_XVT
        _Caculation_Parameters['_TieP_PCCrit'] = _Tie4P_PCCrit
        _Caculation_Parameters['_TieP_Source_Via_TF'] = _Tie4P_Source_Via_TF
        _Caculation_Parameters['_TieP_Drain_Via_TF'] = _Tie4P_Drain_Via_TF
        _Caculation_Parameters['_TieP_PMOSDummy'] = _Tie4P_PMOSDummy
        _Caculation_Parameters['_TieP_PMOSDummy_length'] = _Tie4P_PMOSDummy_length
        _Caculation_Parameters['_TieP_PMOSDummy_placement'] = _Tie4P_PMOSDummy_placement
        _Caculation_Parameters['_NBodyCOX'] = _Tie4_NBodyCOX
        _Caculation_Parameters['_NBodyCOY'] = _Tie4_NBodyCOY
        _Caculation_Parameters['_PBodyCOX'] = _Tie4_PBodyCOX
        _Caculation_Parameters['_PBodyCOY'] = _Tie4_PBodyCOY

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
        tmp1_1 = self.get_outter_KJH4('SRF_C12','SRF_C03_02_Pin')['_Mostleft']['coord'][0]
        tmp1_2 = self.get_outter_KJH4('SRF_C12','SRF_C03_02_Pin')['_Mostup']['coord'][0]
        target_coord = [tmp1_1, tmp1_2]
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_Tie4', 'SRF_PMOS_Body_Contact','BND_Nwell')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_right']
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
        tmp1 = self.get_param_KJH4('SRF_Tie4', 'SRF_TieCellPMOSRouted', 'BND_PMOS_Drain_Hrz_M2')
        Tie4Tr4Route_Tie4HrzPathWidth = 150
        self._DesignParameter['BND_Tie4Tr4Route_Tie4Hrz_M2']['_YWidth'] = max(tmp1[0][0][0][0]['_Ywidth'], Tie4Tr4Route_Tie4HrzPathWidth)

                ## Define Boundary_element _XWidth
        tmp2_1 = tmp1[0][0][0][0]['_XY_up_left'][0]
        tmp2_2 = self.get_param_KJH4('SRF_C12', 'SRF_C03_02_Pin','BND_Gate_Hrz_M2')[0][0][0][0]['_XY_up_right'][0]
        tmp2 = int((tmp2_1 + tmp2_2) / 2)
        self._DesignParameter['BND_Tie4Tr4Route_Tie4Hrz_M2']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_up_left'][0] - tmp2)

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Tie4Tr4Route_Tie4Hrz_M2']['_XYCoordinates'] = [[0, 0]]

                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
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
        tmp2 = self.get_param_KJH4('SRF_C12', 'SRF_C03_02_Pin','BND_Gate_Hrz_M2')
        self._DesignParameter['BND_Tie4Tr4Route_Vtc_M2']['_YWidth'] = abs(tmp1[0][0]['_XY_up_right'][1] - tmp2[0][0][0][0]['_XY_down_right'][1])

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
        tmp2 = self.get_param_KJH4('SRF_C12', 'SRF_C03_02_Pin','BND_Gate_Hrz_M2')
        self._DesignParameter['BND_Tie4Tr4Route_Tr4Hrz_M2']['_YWidth'] = tmp2[0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth

        self._DesignParameter['BND_Tie4Tr4Route_Tr4Hrz_M2']['_XWidth'] = abs(tmp1[0][0]['_XY_up_left'][0] - tmp2[0][0][0][0]['_XY_up_right'][0])

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

        _Caculation_Parameters['_TieN_NMOSNumberofGate'] = _Tie8N_NMOSNumberofGate
        _Caculation_Parameters['_TieN_NMOSChannelWidth'] = _Tie8N_NMOSChannelWidth
        _Caculation_Parameters['_TieN_NMOSChannellength'] = _Tie8N_NMOSChannellength
        _Caculation_Parameters['_TieN_GateSpacing'] = _Tie8N_GateSpacing
        _Caculation_Parameters['_TieN_SDWidth'] = _Tie8N_SDWidth
        _Caculation_Parameters['_TieN_XVT'] = _Tie8N_XVT
        _Caculation_Parameters['_TieN_PCCrit'] = _Tie8N_PCCrit
        _Caculation_Parameters['_TieN_Source_Via_TF'] = _Tie8N_Source_Via_TF
        _Caculation_Parameters['_TieN_Drain_Via_TF'] = _Tie8N_Drain_Via_TF
        _Caculation_Parameters['_TieN_NMOSDummy'] = _Tie8N_NMOSDummy
        _Caculation_Parameters['_TieN_NMOSDummy_length'] = _Tie8N_NMOSDummy_length
        _Caculation_Parameters['_TieN_NMOSDummy_placement'] = _Tie8N_NMOSDummy_placement
        _Caculation_Parameters['_TieP_PMOSNumberofGate'] = _Tie8P_PMOSNumberofGate
        _Caculation_Parameters['_TieP_PMOSChannelWidth'] = _Tie8P_PMOSChannelWidth
        _Caculation_Parameters['_TieP_PMOSChannellength'] = _Tie8P_PMOSChannellength
        _Caculation_Parameters['_TieP_GateSpacing'] = _Tie8P_GateSpacing
        _Caculation_Parameters['_TieP_SDWidth'] = _Tie8P_SDWidth
        _Caculation_Parameters['_TieP_XVT'] = _Tie8P_XVT
        _Caculation_Parameters['_TieP_PCCrit'] = _Tie8P_PCCrit
        _Caculation_Parameters['_TieP_Source_Via_TF'] = _Tie8P_Source_Via_TF
        _Caculation_Parameters['_TieP_Drain_Via_TF'] = _Tie8P_Drain_Via_TF
        _Caculation_Parameters['_TieP_PMOSDummy'] = _Tie8P_PMOSDummy
        _Caculation_Parameters['_TieP_PMOSDummy_length'] = _Tie8P_PMOSDummy_length
        _Caculation_Parameters['_TieP_PMOSDummy_placement'] = _Tie8P_PMOSDummy_placement
        _Caculation_Parameters['_NBodyCOX'] = _Tie8_NBodyCOX
        _Caculation_Parameters['_NBodyCOY'] = _Tie8_NBodyCOY
        _Caculation_Parameters['_PBodyCOX'] = _Tie8_PBodyCOX
        _Caculation_Parameters['_PBodyCOY'] = _Tie8_PBodyCOY

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
        tmp1_1 = self.get_outter_KJH4('SRF_C12','SRF_C05_02_Pin')['_Mostright']['coord'][0]
        tmp1_2 = self.get_outter_KJH4('SRF_C12','SRF_C05_02_Pin')['_Mostup']['coord'][0]
        target_coord = [tmp1_1, tmp1_2]
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_Tie8', 'SRF_PMOS_Body_Contact','BND_Nwell')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
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
        tmp1 = self.get_param_KJH4('SRF_Tie8', 'SRF_TieCellPMOSRouted', 'BND_PMOS_Drain_Hrz_M2')
        Tie8Tr8Route_Tie8HrzPathWidth = 150
        self._DesignParameter['BND_Tie8Tr8Route_Tie8Hrz_M2']['_YWidth'] = max(tmp1[0][0][0][0]['_Ywidth'], Tie8Tr8Route_Tie8HrzPathWidth)

                ## Define Boundary_element _XWidth
        tmp2_1 = tmp1[0][0][0][0]['_XY_up_right'][0]
        tmp2_2 = self.get_param_KJH4('SRF_C12', 'SRF_C05_02_Pin', 'BND_Gate_Hrz_M2')[0][0][0][0]['_XY_up_left'][0]
        tmp2 = int((tmp2_1 + tmp2_2) / 2)
        self._DesignParameter['BND_Tie8Tr8Route_Tie8Hrz_M2']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_up_left'][0] - tmp2)

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Tie8Tr8Route_Tie8Hrz_M2']['_XYCoordinates'] = [[0, 0]]

                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0]['_XY_down_right']
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
        tmp2 = self.get_param_KJH4('SRF_C12', 'SRF_C05_02_Pin','BND_Gate_Hrz_M2')
        self._DesignParameter['BND_Tie8Tr8Route_Vtc_M2']['_YWidth'] = abs(tmp1[0][0]['_XY_up_left'][1] - tmp2[0][0][0][0]['_XY_down_left'][1])

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
        tmp2 = self.get_param_KJH4('SRF_C12', 'SRF_C05_02_Pin','BND_Gate_Hrz_M2')
        self._DesignParameter['BND_Tie8Tr8Route_Tr8Hrz_M2']['_YWidth'] = tmp2[0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Tie8Tr8Route_Tr8Hrz_M2']['_XWidth'] = abs(tmp1[0][0]['_XY_up_right'][0] - tmp2[0][0][0][0]['_XY_down_left'][0])

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
        tmp1_1 = self.get_outter_KJH4('SRF_C12', 'SRF_C03_02_Pin')['_Mostright']['coord'][0]
        tmp1_2 = self.get_outter_KJH4('SRF_C12', 'SRF_C03_02_Pin')['_Mostup']['coord'][0]
        target_coord = [tmp1_1, tmp1_2]
        ## Approaching_coord: _XY_type2
        tmp2_1 = self.get_param_KJH4('SRF_C07', 'SRF_Tr12Tr3Tr10', 'SRF_Tr3','BND_NMOS_Source_Hrz_M2')[0][0][0][0][0]['_XY_down_right'][0]
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

        tmp1 = self.get_param_KJH4('SRF_C07', 'SRF_Tr12Tr3Tr10', 'SRF_Tr3','BND_NMOS_Source_Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_C12', 'SRF_C03_02_Pin', 'SRF_Guardring', 'SRF_Tr4', 'BND_NMOS_Source_Hrz_M2')
        self._DesignParameter['BND_Tr3Tr4Route_Vtc_M2']['_YWidth'] = abs(tmp1[0][0][0][0][0]['_XY_up_right'][1] - tmp2[0][0][0][0][0][0]['_XY_down_right'][1])

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
        tmp2 = self.get_param_KJH4('SRF_C12', 'SRF_C03_02_Pin', 'SRF_Guardring', 'SRF_Tr4', 'BND_NMOS_Source_Hrz_M2')
        self._DesignParameter['BND_Tr3Tr4Route_Hrz_M2']['_YWidth'] = tmp2[0][0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        Tr3Tr4Route_VtcRoutePathWidth = 300
        self._DesignParameter['BND_Tr3Tr4Route_Hrz_M2']['_XWidth'] = abs(tmp1[0][0]['_XY_down_right'][0] - tmp2[0][0][0][0][0][0]['_XY_down_left'][0])

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
        tmp2 = self.get_param_KJH4('SRF_C07', 'SRF_Tr12Tr3Tr10', 'SRF_Tr10', 'BND_NMOS_Source_Hrz_M2')
        self._DesignParameter['BND_Tr8Tr10Route_Tr10Hrz_M2']['_XWidth'] = abs(tmp2[0][0][0][0][0]['_XY_up_left'][0] - tmp1) + \
                                                                                                Tr8Tr10Route_Tr10HrzRoutePathWidth

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
        tmp2 = self.get_param_KJH4('SRF_C12', 'SRF_C05_02_Pin', 'SRF_Guardring','SRF_Tr8','BND_NMOS_Source_Hrz_M2')
        self._DesignParameter['BND_Tr8Tr10Route_Vtc_M2']['_YWidth'] = abs(tmp1[0][0]['_XY_up_right'][1] - tmp2[0][0][0][0][0][0]['_XY_down_left'][1])

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
        tmp2 = self.get_param_KJH4('SRF_C12', 'SRF_C05_02_Pin', 'SRF_Guardring', 'SRF_Tr8', 'BND_NMOS_Source_Hrz_M2')
        self._DesignParameter['BND_Tr8Tr10Route_Tr8Hrz_M2']['_YWidth'] = tmp2[0][0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Tr8Tr10Route_Tr8Hrz_M2']['_XWidth'] = abs(tmp1[0][0]['_XY_down_left'][0] - tmp2[0][0][0][0][0][0]['_XY_down_right'][0])

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Tr8Tr10Route_Tr8Hrz_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp2[0][0][0][0][0][0]['_XY_up_right']
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






############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    Start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_YJH
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ADC_C07C11C12TieCellsRouted_YJH'
    cellname = 'C13_00_C07C11C12TieCellsRouted_YJ_v01_97'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

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
    # testStreamFile = open('./{}'.format(_fileName), 'wb')
    testStreamFile = open('./gdsfile/{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('###############      Sending to FTP Server...      ##################')
    My = MyInfo_YJH.USER(DesignParameters._Technology)
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