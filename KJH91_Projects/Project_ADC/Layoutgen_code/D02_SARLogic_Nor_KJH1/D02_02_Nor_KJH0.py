
## Import Basic Modules
    ## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

    ## Library
import copy
import math
import numpy as np
import time

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A03_NmosWithDummy_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A04_PmosWithDummy_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A08_PbodyContactPhyLen_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A07_NbodyContactPhyLen_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.D02_SARLogic_Nor_KJH1 import D02_00_Pulldown_KJH0
from KJH91_Projects.Project_ADC.Layoutgen_code.D02_SARLogic_Nor_KJH1 import D02_01_Pullup_KJH0



## Define Class
class _Nor(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
    ## Pbody
        # NMOSAB Pbody
        _NMOSAB_Pbody_NumCont=3,  # Number
        _NMOSAB_Pbody_XvtTop2Pbody=None,  # Number/None(Minimum)

    ## Nbody
        # Nbody
        _PMOSAB_Nbody_NumCont=2,  # Number
        _PMOSAB_Nbody_Xvtdown2Nbody=None,  # Number/None(Minimum)

    # PMOS and NMOS Height
        _PMOSXvt2NMOSXvt=1000,  # number

    # NMosfetA
        # PMOS/NMOS
        _NMOSA_MosType                   = 'NMOS',   # 'NMOS'/'PMOS'
        # MOS Up/Dn
        _NMOSA_MosUpDn                   = 'Up',     # 'Up'/'Dn'
        # Physical dimension
        _NMOSA_NumberofGate	            = 1,        # Number
        _NMOSA_ChannelWidth	            = 200,      # Number
        _NMOSA_ChannelLength	        = 30,       # Number
        _NMOSA_GateSpacing		        = None,     # None/Number
        _NMOSA_SDWidth			        = None,     # None/Number
        _NMOSA_XVT				        = 'SLVT',   # 'XVT' ex)SLVT/LVT/RVT/HVT
        _NMOSA_PCCrit				    = True,     # None/True
        # Source_node setting
            # Via setting
        _NMOSA_Source_Via_TF              = False,     # True/False
                # Via close to POpin
        _NMOSA_Source_Via_Close2POpin_TF  = False,     # True/False
            # Comb setting: If Via is True
        _NMOSA_Source_Comb_TF             = False,     # True/False
                # Comb POPinward
        _NMOSA_Source_Comb_POpinward_TF   = False,     # True/False
                # Comb vertical_length
        _NMOSA_Source_Comb_Length         = None,     # None/Number

        # Drain_node_setting
            # Via setting
        _NMOSA_Drain_Via_TF               = True,     # True/False
                # Via close to POpin
        _NMOSA_Drain_Via_Close2POpin_TF   = True,     # True/False
            # Comb setting: If Via is True
        _NMOSA_Drain_Comb_TF              = True,     # True/False
                # Comb POPinward
        _NMOSA_Drain_Comb_POpinward_TF    = True,     # True/False
                # Comb vertical_length
        _NMOSA_Drain_Comb_Length          = None,     # None/Number

        # POLY dummy setting
        _NMOSA_PODummy_TF                 = True,  # TF
            # if _NMOSADummy == True
        _NMOSA_PODummy_Length             = None,  # None/Value
        _NMOSA_PODummy_Placement          = None,  # None/'Up'/'Dn'/

        # XVT setting
            # XVT setting : Exten XVT area if area is min
        _NMOSA_Xvt_MinExten_TF            = True,     # True/False
            # XVT setting : None(Cent), Up, Dn
        _NMOSA_Xvt_Placement              = 'Up',     # None/'Up'/'Dn'/

        # Poly Gate setting
        _NMOSA_POGate_Comb_TF             = True,     # True/False
            # Poly Gate setting : vertical length
        _NMOSA_POGate_Comb_length         = 100,     # None/Number
            # Poly Gate Via setting
        _NMOSA_POGate_Via_TF              = True,     # True/False
            # Poly Gate Via setting :
        _NMOSA_POGate_ViaMxMx             = [0 ,1],     # Ex) [1,5] -> ViaM1M5


    # NMosfetB
        # PMOS/NMOS
        _NMOSB_MosType                   = 'NMOS',   # 'NMOS'/'PMOS'
        # MOS Up/Dn
        _NMOSB_MosUpDn                   = 'Up',     # 'Up'/'Dn'
        # Physical dimension
        _NMOSB_NumberofGate	            = 1,        # Number
        _NMOSB_ChannelWidth	            = 852,      # Number
        _NMOSB_ChannelLength	        = 30,       # Number
        _NMOSB_GateSpacing		        = None,     # None/Number
        _NMOSB_SDWidth			        = None,     # None/Number
        _NMOSB_XVT				        = 'SLVT',   # 'XVT' ex)SLVT/LVT/RVT/HVT
        _NMOSB_PCCrit				    = True,     # None/True
        # Source_node setting
            # Via setting
        _NMOSB_Source_Via_TF              = False,     # True/False
                # Via close to POpin
        _NMOSB_Source_Via_Close2POpin_TF  = False,     # True/False
            # Comb setting: If Via is True
        _NMOSB_Source_Comb_TF             = False,     # True/False
                # Comb POPinward
        _NMOSB_Source_Comb_POpinward_TF   = False,     # True/False
                # Comb vertical_length
        _NMOSB_Source_Comb_Length         = None,     # None/Number

        # Drain_node_setting
            # Via setting
        _NMOSB_Drain_Via_TF               = True,     # True/False
                # Via close to POpin
        _NMOSB_Drain_Via_Close2POpin_TF   = True,     # True/False
            # Comb setting: If Via is True
        _NMOSB_Drain_Comb_TF              = True,     # True/False
                # Comb POPinward
        _NMOSB_Drain_Comb_POpinward_TF    = True,     # True/False
                # Comb vertical_length
        _NMOSB_Drain_Comb_Length          = None,     # None/Number

        # POLY dummy setting
        _NMOSB_PODummy_TF                 = True,  # TF
            # if _NMOSBDummy == True
        _NMOSB_PODummy_Length             = None,  # None/Value
        _NMOSB_PODummy_Placement          = None,  # None/'Up'/'Dn'/

        # XVT setting
            # XVT setting : Exten XVT area if area is min
        _NMOSB_Xvt_MinExten_TF            = True,     # True/False
            # XVT setting : None(Cent), Up, Dn
        _NMOSB_Xvt_Placement              = 'Up',     # None/'Up'/'Dn'/

        # Poly Gate setting
        _NMOSB_POGate_Comb_TF             = True,     # True/False
            # Poly Gate setting : vertical length
        _NMOSB_POGate_Comb_length         = 100,     # None/Number
            # Poly Gate Via setting
        _NMOSB_POGate_Via_TF              = True,     # None/'Up'/'Dn'/
            # Poly Gate Via setting :
        _NMOSB_POGate_ViaMxMx             = [0 ,1],     # Ex) [1,5] -> ViaM1M5



    # PMosfetA
        # PMOS/NMOS
        _PMOSA_MosType                   = 'PMOS',   # 'NMOS'/'PMOS'
        # MOS Up/Dn
        _PMOSA_MosUpDn                   = 'Dn',     # 'Up'/'Dn'
        # Physical dimension
        _PMOSA_NumberofGate	            = 5,        # Number
        _PMOSA_ChannelWidth	            = 811,      # Number
        _PMOSA_ChannelLength	        = 30,       # Number
        _PMOSA_GateSpacing		        = None,     # None/Number
        _PMOSA_SDWidth			        = None,     # None/Number
        _PMOSA_XVT				        = 'SLVT',   # 'XVT' ex)SLVT/LVT/RVT/HVT
        _PMOSA_PCCrit				    = True,     # None/True
        # Source_node setting
            # Via setting
        _PMOSA_Source_Via_TF              = False,     # True/False
                # Via close to POpin
        _PMOSA_Source_Via_Close2POpin_TF  = False,     # True/False
            # Comb setting: If Via is True
        _PMOSA_Source_Comb_TF             = False,     # True/False
                # Comb POPinward
        _PMOSA_Source_Comb_POpinward_TF   = False,     # True/False
                # Comb vertical_length
        _PMOSA_Source_Comb_Length         = None,     # None/Number

        # Drain_node_setting
            # Via setting
        _PMOSA_Drain_Via_TF               = True,     # True/False
                # Via close to POpin
        _PMOSA_Drain_Via_Close2POpin_TF   = False,     # True/False
            # Comb setting: If Via is True
        _PMOSA_Drain_Comb_TF              = True,     # True/False
                # Comb POPinward
        _PMOSA_Drain_Comb_POpinward_TF    = False,     # True/False
                # Comb vertical_length
        _PMOSA_Drain_Comb_Length          = None,     # None/Number

        # POLY dummy setting
        _PMOSA_PODummy_TF                 = True,  # TF
            # if _PMOSADummy == True
        _PMOSA_PODummy_Length             = None,  # None/Value
        _PMOSA_PODummy_Placement          = None,  # None/'Up'/'Dn'/

        # XVT setting
            # XVT setting : Exten XVT area if area is min
        _PMOSA_Xvt_MinExten_TF            = True,     # True/False
            # XVT setting : None(Cent), Up, Dn
        _PMOSA_Xvt_Placement              = 'Dn',     # None/'Up'/'Dn'/

        # Poly Gate setting
        _PMOSA_POGate_Comb_TF             = True,     # True/False
            # Poly Gate setting : vertical length
        _PMOSA_POGate_Comb_length         = 100,     # None/Number
            # Poly Gate Via setting
        _PMOSA_POGate_Via_TF              = True,     # True/False
            # Poly Gate Via setting :
        _PMOSA_POGate_ViaMxMx             = [0 ,1],     # Ex) [1,5] -> ViaM1M5


    # PMosfetB
        # PMOS/NMOS
        _PMOSB_MosType                   = 'PMOS',   # 'NMOS'/'PMOS'
        # MOS Up/Dn
        _PMOSB_MosUpDn                   = 'Dn',     # 'Up'/'Dn'
        # Physical dimension
        _PMOSB_NumberofGate	            = 4,        # Number
        _PMOSB_ChannelWidth	            = 350,      # Number
        _PMOSB_ChannelLength	        = 30,       # Number
        _PMOSB_GateSpacing		        = None,     # None/Number
        _PMOSB_SDWidth			        = None,     # None/Number
        _PMOSB_XVT				        = 'SLVT',   # 'XVT' ex)SLVT/LVT/RVT/HVT
        _PMOSB_PCCrit				    = True,     # None/True
        # Source_node setting
            # Via setting
        _PMOSB_Source_Via_TF              = True,     # True/False
                # Via close to POpin
        _PMOSB_Source_Via_Close2POpin_TF  = False,     # True/False
            # Comb setting: If Via is True
        _PMOSB_Source_Comb_TF             = True,     # True/False
                # Comb POPinward
        _PMOSB_Source_Comb_POpinward_TF   = False,     # True/False
                # Comb vertical_length
        _PMOSB_Source_Comb_Length         = None,     # None/Number

        # Drain_node_setting
            # Via setting
        _PMOSB_Drain_Via_TF               = True,     # True/False
                # Via close to POpin
        _PMOSB_Drain_Via_Close2POpin_TF   = True,     # True/False
            # Comb setting: If Via is True
        _PMOSB_Drain_Comb_TF              = True,     # True/False
                # Comb POPinward
        _PMOSB_Drain_Comb_POpinward_TF    = True,     # True/False
                # Comb vertical_length
        _PMOSB_Drain_Comb_Length          = None,     # None/Number

        # POLY dummy setting
        _PMOSB_PODummy_TF                 = True,  # TF
            # if _PMOSBDummy == True
        _PMOSB_PODummy_Length             = None,  # None/Value
        _PMOSB_PODummy_Placement          = None,  # None/'Up'/'Dn'/

        # XVT setting
            # XVT setting : Exten XVT area if area is min
        _PMOSB_Xvt_MinExten_TF            = True,     # True/False
            # XVT setting : None(Cent), Up, Dn
        _PMOSB_Xvt_Placement              = 'Dn',     # None/'Up'/'Dn'/

        # Poly Gate setting
        _PMOSB_POGate_Comb_TF             = True,     # True/False
            # Poly Gate setting : vertical length
        _PMOSB_POGate_Comb_length         = 100,     # None/Number
            # Poly Gate Via setting
        _PMOSB_POGate_Via_TF              = True,     # None/'Up'/'Dn'/
            # Poly Gate Via setting :
        _PMOSB_POGate_ViaMxMx             = [0 ,1],     # Ex) [1,5] -> ViaM1M5



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

    ## Pbody
        # NMOSAB Pbody
        _NMOSAB_Pbody_NumCont=3,  # Number
        _NMOSAB_Pbody_XvtTop2Pbody=None,  # Number/None(Minimum)

    ## Nbody
        # Nbody
        _PMOSAB_Nbody_NumCont=2,  # Number
        _PMOSAB_Nbody_Xvtdown2Nbody=None,  # Number/None(Minimum)

    # PMOS and NMOS Height
        _PMOSXvt2NMOSXvt=1000,  # number

    # NMosfetA
        # PMOS/NMOS
        _NMOSA_MosType                   = 'NMOS',   # 'NMOS'/'PMOS'
        # MOS Up/Dn
        _NMOSA_MosUpDn                   = 'Up',     # 'Up'/'Dn'
        # Physical dimension
        _NMOSA_NumberofGate	            = 1,        # Number
        _NMOSA_ChannelWidth	            = 200,      # Number
        _NMOSA_ChannelLength	        = 30,       # Number
        _NMOSA_GateSpacing		        = None,     # None/Number
        _NMOSA_SDWidth			        = None,     # None/Number
        _NMOSA_XVT				        = 'SLVT',   # 'XVT' ex)SLVT/LVT/RVT/HVT
        _NMOSA_PCCrit				    = True,     # None/True
        # Source_node setting
            # Via setting
        _NMOSA_Source_Via_TF              = False,     # True/False
                # Via close to POpin
        _NMOSA_Source_Via_Close2POpin_TF  = False,     # True/False
            # Comb setting: If Via is True
        _NMOSA_Source_Comb_TF             = False,     # True/False
                # Comb POPinward
        _NMOSA_Source_Comb_POpinward_TF   = False,     # True/False
                # Comb vertical_length
        _NMOSA_Source_Comb_Length         = None,     # None/Number

        # Drain_node_setting
            # Via setting
        _NMOSA_Drain_Via_TF               = True,     # True/False
                # Via close to POpin
        _NMOSA_Drain_Via_Close2POpin_TF   = True,     # True/False
            # Comb setting: If Via is True
        _NMOSA_Drain_Comb_TF              = True,     # True/False
                # Comb POPinward
        _NMOSA_Drain_Comb_POpinward_TF    = True,     # True/False
                # Comb vertical_length
        _NMOSA_Drain_Comb_Length          = None,     # None/Number

        # POLY dummy setting
        _NMOSA_PODummy_TF                 = True,  # TF
            # if _NMOSADummy == True
        _NMOSA_PODummy_Length             = None,  # None/Value
        _NMOSA_PODummy_Placement          = None,  # None/'Up'/'Dn'/

        # XVT setting
            # XVT setting : Exten XVT area if area is min
        _NMOSA_Xvt_MinExten_TF            = True,     # True/False
            # XVT setting : None(Cent), Up, Dn
        _NMOSA_Xvt_Placement              = 'Up',     # None/'Up'/'Dn'/

        # Poly Gate setting
        _NMOSA_POGate_Comb_TF             = True,     # True/False
            # Poly Gate setting : vertical length
        _NMOSA_POGate_Comb_length         = 100,     # None/Number
            # Poly Gate Via setting
        _NMOSA_POGate_Via_TF              = True,     # True/False
            # Poly Gate Via setting :
        _NMOSA_POGate_ViaMxMx             = [0 ,1],     # Ex) [1,5] -> ViaM1M5


    # NMosfetB
        # PMOS/NMOS
        _NMOSB_MosType                   = 'NMOS',   # 'NMOS'/'PMOS'
        # MOS Up/Dn
        _NMOSB_MosUpDn                   = 'Up',     # 'Up'/'Dn'
        # Physical dimension
        _NMOSB_NumberofGate	            = 1,        # Number
        _NMOSB_ChannelWidth	            = 852,      # Number
        _NMOSB_ChannelLength	        = 30,       # Number
        _NMOSB_GateSpacing		        = None,     # None/Number
        _NMOSB_SDWidth			        = None,     # None/Number
        _NMOSB_XVT				        = 'SLVT',   # 'XVT' ex)SLVT/LVT/RVT/HVT
        _NMOSB_PCCrit				    = True,     # None/True
        # Source_node setting
            # Via setting
        _NMOSB_Source_Via_TF              = False,     # True/False
                # Via close to POpin
        _NMOSB_Source_Via_Close2POpin_TF  = False,     # True/False
            # Comb setting: If Via is True
        _NMOSB_Source_Comb_TF             = False,     # True/False
                # Comb POPinward
        _NMOSB_Source_Comb_POpinward_TF   = False,     # True/False
                # Comb vertical_length
        _NMOSB_Source_Comb_Length         = None,     # None/Number

        # Drain_node_setting
            # Via setting
        _NMOSB_Drain_Via_TF               = True,     # True/False
                # Via close to POpin
        _NMOSB_Drain_Via_Close2POpin_TF   = True,     # True/False
            # Comb setting: If Via is True
        _NMOSB_Drain_Comb_TF              = True,     # True/False
                # Comb POPinward
        _NMOSB_Drain_Comb_POpinward_TF    = True,     # True/False
                # Comb vertical_length
        _NMOSB_Drain_Comb_Length          = None,     # None/Number

        # POLY dummy setting
        _NMOSB_PODummy_TF                 = True,  # TF
            # if _NMOSBDummy == True
        _NMOSB_PODummy_Length             = None,  # None/Value
        _NMOSB_PODummy_Placement          = None,  # None/'Up'/'Dn'/

        # XVT setting
            # XVT setting : Exten XVT area if area is min
        _NMOSB_Xvt_MinExten_TF            = True,     # True/False
            # XVT setting : None(Cent), Up, Dn
        _NMOSB_Xvt_Placement              = 'Up',     # None/'Up'/'Dn'/

        # Poly Gate setting
        _NMOSB_POGate_Comb_TF             = True,     # True/False
            # Poly Gate setting : vertical length
        _NMOSB_POGate_Comb_length         = 100,     # None/Number
            # Poly Gate Via setting
        _NMOSB_POGate_Via_TF              = True,     # None/'Up'/'Dn'/
            # Poly Gate Via setting :
        _NMOSB_POGate_ViaMxMx             = [0 ,1],     # Ex) [1,5] -> ViaM1M5



    # PMosfetA
        # PMOS/NMOS
        _PMOSA_MosType                   = 'PMOS',   # 'NMOS'/'PMOS'
        # MOS Up/Dn
        _PMOSA_MosUpDn                   = 'Dn',     # 'Up'/'Dn'
        # Physical dimension
        _PMOSA_NumberofGate	            = 5,        # Number
        _PMOSA_ChannelWidth	            = 811,      # Number
        _PMOSA_ChannelLength	        = 30,       # Number
        _PMOSA_GateSpacing		        = None,     # None/Number
        _PMOSA_SDWidth			        = None,     # None/Number
        _PMOSA_XVT				        = 'SLVT',   # 'XVT' ex)SLVT/LVT/RVT/HVT
        _PMOSA_PCCrit				    = True,     # None/True
        # Source_node setting
            # Via setting
        _PMOSA_Source_Via_TF              = False,     # True/False
                # Via close to POpin
        _PMOSA_Source_Via_Close2POpin_TF  = False,     # True/False
            # Comb setting: If Via is True
        _PMOSA_Source_Comb_TF             = False,     # True/False
                # Comb POPinward
        _PMOSA_Source_Comb_POpinward_TF   = False,     # True/False
                # Comb vertical_length
        _PMOSA_Source_Comb_Length         = None,     # None/Number

        # Drain_node_setting
            # Via setting
        _PMOSA_Drain_Via_TF               = True,     # True/False
                # Via close to POpin
        _PMOSA_Drain_Via_Close2POpin_TF   = False,     # True/False
            # Comb setting: If Via is True
        _PMOSA_Drain_Comb_TF              = True,     # True/False
                # Comb POPinward
        _PMOSA_Drain_Comb_POpinward_TF    = False,     # True/False
                # Comb vertical_length
        _PMOSA_Drain_Comb_Length          = None,     # None/Number

        # POLY dummy setting
        _PMOSA_PODummy_TF                 = True,  # TF
            # if _PMOSADummy == True
        _PMOSA_PODummy_Length             = None,  # None/Value
        _PMOSA_PODummy_Placement          = None,  # None/'Up'/'Dn'/

        # XVT setting
            # XVT setting : Exten XVT area if area is min
        _PMOSA_Xvt_MinExten_TF            = True,     # True/False
            # XVT setting : None(Cent), Up, Dn
        _PMOSA_Xvt_Placement              = 'Dn',     # None/'Up'/'Dn'/

        # Poly Gate setting
        _PMOSA_POGate_Comb_TF             = True,     # True/False
            # Poly Gate setting : vertical length
        _PMOSA_POGate_Comb_length         = 100,     # None/Number
            # Poly Gate Via setting
        _PMOSA_POGate_Via_TF              = True,     # True/False
            # Poly Gate Via setting :
        _PMOSA_POGate_ViaMxMx             = [0 ,1],     # Ex) [1,5] -> ViaM1M5


    # PMosfetB
        # PMOS/NMOS
        _PMOSB_MosType                   = 'PMOS',   # 'NMOS'/'PMOS'
        # MOS Up/Dn
        _PMOSB_MosUpDn                   = 'Dn',     # 'Up'/'Dn'
        # Physical dimension
        _PMOSB_NumberofGate	            = 4,        # Number
        _PMOSB_ChannelWidth	            = 350,      # Number
        _PMOSB_ChannelLength	        = 30,       # Number
        _PMOSB_GateSpacing		        = None,     # None/Number
        _PMOSB_SDWidth			        = None,     # None/Number
        _PMOSB_XVT				        = 'SLVT',   # 'XVT' ex)SLVT/LVT/RVT/HVT
        _PMOSB_PCCrit				    = True,     # None/True
        # Source_node setting
            # Via setting
        _PMOSB_Source_Via_TF              = True,     # True/False
                # Via close to POpin
        _PMOSB_Source_Via_Close2POpin_TF  = False,     # True/False
            # Comb setting: If Via is True
        _PMOSB_Source_Comb_TF             = True,     # True/False
                # Comb POPinward
        _PMOSB_Source_Comb_POpinward_TF   = False,     # True/False
                # Comb vertical_length
        _PMOSB_Source_Comb_Length         = None,     # None/Number

        # Drain_node_setting
            # Via setting
        _PMOSB_Drain_Via_TF               = True,     # True/False
                # Via close to POpin
        _PMOSB_Drain_Via_Close2POpin_TF   = True,     # True/False
            # Comb setting: If Via is True
        _PMOSB_Drain_Comb_TF              = True,     # True/False
                # Comb POPinward
        _PMOSB_Drain_Comb_POpinward_TF    = True,     # True/False
                # Comb vertical_length
        _PMOSB_Drain_Comb_Length          = None,     # None/Number

        # POLY dummy setting
        _PMOSB_PODummy_TF                 = True,  # TF
            # if _PMOSBDummy == True
        _PMOSB_PODummy_Length             = None,  # None/Value
        _PMOSB_PODummy_Placement          = None,  # None/'Up'/'Dn'/

        # XVT setting
            # XVT setting : Exten XVT area if area is min
        _PMOSB_Xvt_MinExten_TF            = True,     # True/False
            # XVT setting : None(Cent), Up, Dn
        _PMOSB_Xvt_Placement              = 'Dn',     # None/'Up'/'Dn'/

        # Poly Gate setting
        _PMOSB_POGate_Comb_TF             = True,     # True/False
            # Poly Gate setting : vertical length
        _PMOSB_POGate_Comb_length         = 100,     # None/Number
            # Poly Gate Via setting
        _PMOSB_POGate_Via_TF              = True,     # None/'Up'/'Dn'/
            # Poly Gate Via setting :
        _PMOSB_POGate_ViaMxMx             = [0 ,1],     # Ex) [1,5] -> ViaM1M5



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


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Pulldown
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Pulldown: Sref Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D02_00_Pulldown_KJH0._Pulldown._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOSA_MosType']                      = _NMOSA_MosType
        _Caculation_Parameters['_NMOSA_MosUpDn']                      = _NMOSA_MosUpDn

        _Caculation_Parameters['_NMOSA_NumberofGate']                 = _NMOSA_NumberofGate
        _Caculation_Parameters['_NMOSA_ChannelWidth']                 = _NMOSA_ChannelWidth
        _Caculation_Parameters['_NMOSA_ChannelLength']                = _NMOSA_ChannelLength
        _Caculation_Parameters['_NMOSA_GateSpacing']                  = _NMOSA_GateSpacing
        _Caculation_Parameters['_NMOSA_SDWidth']                      = _NMOSA_SDWidth
        _Caculation_Parameters['_NMOSA_XVT']                          = _NMOSA_XVT
        _Caculation_Parameters['_NMOSA_PCCrit']                       = _NMOSA_PCCrit

        _Caculation_Parameters['_NMOSA_Source_Via_TF']                = _NMOSA_Source_Via_TF
        _Caculation_Parameters['_NMOSA_Source_Via_Close2POpin_TF']    = _NMOSA_Source_Via_Close2POpin_TF
        _Caculation_Parameters['_NMOSA_Source_Comb_TF']               = _NMOSA_Source_Comb_TF
        _Caculation_Parameters['_NMOSA_Source_Comb_POpinward_TF']     = _NMOSA_Source_Comb_POpinward_TF
        _Caculation_Parameters['_NMOSA_Source_Comb_Length']           = _NMOSA_Source_Comb_Length

        _Caculation_Parameters['_NMOSA_Drain_Via_TF']                 = _NMOSA_Drain_Via_TF
        _Caculation_Parameters['_NMOSA_Drain_Via_Close2POpin_TF']     = _NMOSA_Drain_Via_Close2POpin_TF
        _Caculation_Parameters['_NMOSA_Drain_Comb_TF']                = _NMOSA_Drain_Comb_TF
        _Caculation_Parameters['_NMOSA_Drain_Comb_POpinward_TF']      = _NMOSA_Drain_Comb_POpinward_TF
        _Caculation_Parameters['_NMOSA_Drain_Comb_Length']            = _NMOSA_Drain_Comb_Length

        _Caculation_Parameters['_NMOSA_PODummy_TF']                   = _NMOSA_PODummy_TF
        _Caculation_Parameters['_NMOSA_PODummy_Length']               = _NMOSA_PODummy_Length
        _Caculation_Parameters['_NMOSA_PODummy_Placement']            = _NMOSA_PODummy_Placement

        _Caculation_Parameters['_NMOSA_Xvt_MinExten_TF']              = _NMOSA_Xvt_MinExten_TF
        _Caculation_Parameters['_NMOSA_Xvt_Placement']                = _NMOSA_Xvt_Placement

        _Caculation_Parameters['_NMOSA_POGate_Comb_TF']               = _NMOSA_POGate_Comb_TF
        _Caculation_Parameters['_NMOSA_POGate_Comb_length']           = _NMOSA_POGate_Comb_length
        _Caculation_Parameters['_NMOSA_POGate_Via_TF']                = _NMOSA_POGate_Via_TF
        _Caculation_Parameters['_NMOSA_POGate_ViaMxMx']               = _NMOSA_POGate_ViaMxMx


        _Caculation_Parameters['_NMOSB_MosType']                      = _NMOSB_MosType
        _Caculation_Parameters['_NMOSB_MosUpDn']                      = _NMOSB_MosUpDn

        _Caculation_Parameters['_NMOSB_NumberofGate']                 = _NMOSB_NumberofGate
        _Caculation_Parameters['_NMOSB_ChannelWidth']                 = _NMOSB_ChannelWidth
        _Caculation_Parameters['_NMOSB_ChannelLength']                = _NMOSB_ChannelLength
        _Caculation_Parameters['_NMOSB_GateSpacing']                  = _NMOSB_GateSpacing
        _Caculation_Parameters['_NMOSB_SDWidth']                      = _NMOSB_SDWidth
        _Caculation_Parameters['_NMOSB_XVT']                          = _NMOSB_XVT
        _Caculation_Parameters['_NMOSB_PCCrit']                       = _NMOSB_PCCrit

        _Caculation_Parameters['_NMOSB_Source_Via_TF']                = _NMOSB_Source_Via_TF
        _Caculation_Parameters['_NMOSB_Source_Via_Close2POpin_TF']    = _NMOSB_Source_Via_Close2POpin_TF
        _Caculation_Parameters['_NMOSB_Source_Comb_TF']               = _NMOSB_Source_Comb_TF
        _Caculation_Parameters['_NMOSB_Source_Comb_POpinward_TF']     = _NMOSB_Source_Comb_POpinward_TF
        _Caculation_Parameters['_NMOSB_Source_Comb_Length']           = _NMOSB_Source_Comb_Length

        _Caculation_Parameters['_NMOSB_Drain_Via_TF']                 = _NMOSB_Drain_Via_TF
        _Caculation_Parameters['_NMOSB_Drain_Via_Close2POpin_TF']     = _NMOSB_Drain_Via_Close2POpin_TF
        _Caculation_Parameters['_NMOSB_Drain_Comb_TF']                = _NMOSB_Drain_Comb_TF
        _Caculation_Parameters['_NMOSB_Drain_Comb_POpinward_TF']      = _NMOSB_Drain_Comb_POpinward_TF
        _Caculation_Parameters['_NMOSB_Drain_Comb_Length']            = _NMOSB_Drain_Comb_Length

        _Caculation_Parameters['_NMOSB_PODummy_TF']                   = _NMOSB_PODummy_TF
        _Caculation_Parameters['_NMOSB_PODummy_Length']               = _NMOSB_PODummy_Length
        _Caculation_Parameters['_NMOSB_PODummy_Placement']            = _NMOSB_PODummy_Placement

        _Caculation_Parameters['_NMOSB_Xvt_MinExten_TF']              = _NMOSB_Xvt_MinExten_TF
        _Caculation_Parameters['_NMOSB_Xvt_Placement']                = _NMOSB_Xvt_Placement

        _Caculation_Parameters['_NMOSB_POGate_Comb_TF']               = _NMOSB_POGate_Comb_TF
        _Caculation_Parameters['_NMOSB_POGate_Comb_length']           = _NMOSB_POGate_Comb_length
        _Caculation_Parameters['_NMOSB_POGate_Via_TF']                = _NMOSB_POGate_Via_TF
        _Caculation_Parameters['_NMOSB_POGate_ViaMxMx']               = _NMOSB_POGate_ViaMxMx


        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Pulldown'] = self._SrefElementDeclaration(_DesignObj=D02_00_Pulldown_KJH0._Pulldown(_DesignParameter=None, _Name='{}:SRF_Pulldown'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOSA_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Pulldown']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOSA_POWER'
        self._DesignParameter['SRF_Pulldown']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOSA_POWER'
        self._DesignParameter['SRF_Pulldown']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOSA_POWER'
        self._DesignParameter['SRF_Pulldown']['_XYCoordinates'] = [[0, 0]]

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Pulldown: Pbody
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Pulldown: Pbody : Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length'] = None
        _Caculation_Parameters['_NumCont'] = _NMOSAB_Pbody_NumCont
        _Caculation_Parameters['_Vtc_flag'] = False

        ## Calculate '_Length'
        tmp = self.get_outter_KJH4('SRF_Pulldown')
        _Caculation_Parameters['_Length'] = abs(tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0])

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Pbody'] = self._SrefElementDeclaration( _DesignObj=A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen(_DesignParameter=None,_Name='{}:SRF_Pbody'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Pbody']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbody']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbody']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbody']['_XYCoordinates'] = [[0, 0]]

        ## Get_Scoord_v4.
        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_Pbody']['_XYCoordinates'] = [[0, 0]]

        if _NMOSAB_Pbody_XvtTop2Pbody == None:
            ## Calculate
                ## Target_coord: _XY_type1
                    ## X
            tmp1_1 = self.get_outter_KJH4('SRF_Pulldown')
            target_coordx = np.round(0.5 * ( tmp1_1['_Mostright']['coord'][0] + tmp1_1['_Mostleft']['coord'][0] ))
                    ## Y
            target_coordy = tmp1_1['_Mostdown']['coord'][0]

            target_coord = [target_coordx, target_coordy]
                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_up']
                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Pbody')
            Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[1] = New_Scoord[1] - 50
            tmpXY.append(New_Scoord)
                ## Define Coordinates
            self._DesignParameter['SRF_Pbody']['_XYCoordinates'] = tmpXY

        else:
            ## Calculate
                ## Target_coord: _XY_type1
                    #X
            tmp1_1 = self.get_outter_KJH4('SRF_Pulldown')
            target_coordx = np.round(0.5 * ( tmp1_1['_Mostright']['coord'][0] + tmp1_1['_Mostleft']['coord'][0] ))
                    #Y
            tmp1_2 = self.get_param_KJH4('SRF_Pulldown', 'SRF_NMOSA', 'BND_{}Layer'.format(_NMOSA_XVT))
            target_coordy = tmp1_2[0][0][0][0]['_XY_up'][1]

            target_coord = [target_coordx,target_coordy]

                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_up']
                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Pbody')
            Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[1] = New_Scoord[1] - _NMOSAB_Pbody_XvtTop2Pbody
            tmpXY.append(New_Scoord)
            ## Define Coordinates
            self._DesignParameter['SRF_Pbody']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Pulldown: Pbody : NMOSA source and Pbody connection
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NMOSA_Source2Pbody_Vtc_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth : ViaYmin 기준
        tmp1 = self.get_param_KJH4('SRF_Pulldown', 'SRF_NMOSA', 'BND_Source_M1')
        tmp2 = self.get_param_KJH4('SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        self._DesignParameter['BND_NMOSA_Source2Pbody_Vtc_M1']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1])

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Pulldown', 'SRF_NMOSA', 'BND_Source_M1')
        self._DesignParameter['BND_NMOSA_Source2Pbody_Vtc_M1']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NMOSA_Source2Pbody_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        tmp = self.get_param_KJH4('SRF_Pulldown', 'SRF_NMOSA', 'BND_Source_M1')
        for i in range(0, len(tmp[0][0])):
            ## Calculate Sref XYcoord
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Pulldown', 'SRF_NMOSA', 'BND_Source_M1')
            target_coord = tmp1[0][0][i][0]['_XY_up_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_NMOSA_Source2Pbody_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_up_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_NMOSA_Source2Pbody_Vtc_M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_NMOSA_Source2Pbody_Vtc_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Pulldown: Pbody : NMOSB source and Pbody connection
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NMOSB_Source2Pbody_Vtc_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth : ViaYmin 기준
        tmp1 = self.get_param_KJH4('SRF_Pulldown', 'SRF_NMOSB', 'BND_Source_M1')
        tmp2 = self.get_param_KJH4('SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        self._DesignParameter['BND_NMOSB_Source2Pbody_Vtc_M1']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1])

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Pulldown', 'SRF_NMOSB', 'BND_Source_M1')
        self._DesignParameter['BND_NMOSB_Source2Pbody_Vtc_M1']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NMOSB_Source2Pbody_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        tmp = self.get_param_KJH4('SRF_Pulldown', 'SRF_NMOSB', 'BND_Source_M1')
        for i in range(0, len(tmp[0][0])):
            ## Calculate Sref XYcoord
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Pulldown', 'SRF_NMOSB', 'BND_Source_M1')
            target_coord = tmp1[0][0][i][0]['_XY_up_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_NMOSB_Source2Pbody_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_up_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_NMOSB_Source2Pbody_Vtc_M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_NMOSB_Source2Pbody_Vtc_M1']['_XYCoordinates'] = tmpXY





        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Pullup
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Pullup: Sref Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D02_01_Pullup_KJH0._Pullup._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_PMOSA_MosType']                      = _PMOSA_MosType
        _Caculation_Parameters['_PMOSA_MosUpDn']                      = _PMOSA_MosUpDn

        _Caculation_Parameters['_PMOSA_NumberofGate']                 = _PMOSA_NumberofGate
        _Caculation_Parameters['_PMOSA_ChannelWidth']                 = _PMOSA_ChannelWidth
        _Caculation_Parameters['_PMOSA_ChannelLength']                = _PMOSA_ChannelLength
        _Caculation_Parameters['_PMOSA_GateSpacing']                  = _PMOSA_GateSpacing
        _Caculation_Parameters['_PMOSA_SDWidth']                      = _PMOSA_SDWidth
        _Caculation_Parameters['_PMOSA_XVT']                          = _PMOSA_XVT
        _Caculation_Parameters['_PMOSA_PCCrit']                       = _PMOSA_PCCrit

        _Caculation_Parameters['_PMOSA_Source_Via_TF']                = _PMOSA_Source_Via_TF
        _Caculation_Parameters['_PMOSA_Source_Via_Close2POpin_TF']    = _PMOSA_Source_Via_Close2POpin_TF
        _Caculation_Parameters['_PMOSA_Source_Comb_TF']               = _PMOSA_Source_Comb_TF
        _Caculation_Parameters['_PMOSA_Source_Comb_POpinward_TF']     = _PMOSA_Source_Comb_POpinward_TF
        _Caculation_Parameters['_PMOSA_Source_Comb_Length']           = _PMOSA_Source_Comb_Length

        _Caculation_Parameters['_PMOSA_Drain_Via_TF']                 = _PMOSA_Drain_Via_TF
        _Caculation_Parameters['_PMOSA_Drain_Via_Close2POpin_TF']     = _PMOSA_Drain_Via_Close2POpin_TF
        _Caculation_Parameters['_PMOSA_Drain_Comb_TF']                = _PMOSA_Drain_Comb_TF
        _Caculation_Parameters['_PMOSA_Drain_Comb_POpinward_TF']      = _PMOSA_Drain_Comb_POpinward_TF
        _Caculation_Parameters['_PMOSA_Drain_Comb_Length']            = _PMOSA_Drain_Comb_Length

        _Caculation_Parameters['_PMOSA_PODummy_TF']                   = _PMOSA_PODummy_TF
        _Caculation_Parameters['_PMOSA_PODummy_Length']               = _PMOSA_PODummy_Length
        _Caculation_Parameters['_PMOSA_PODummy_Placement']            = _PMOSA_PODummy_Placement

        _Caculation_Parameters['_PMOSA_Xvt_MinExten_TF']              = _PMOSA_Xvt_MinExten_TF
        _Caculation_Parameters['_PMOSA_Xvt_Placement']                = _PMOSA_Xvt_Placement

        _Caculation_Parameters['_PMOSA_POGate_Comb_TF']               = _PMOSA_POGate_Comb_TF
        _Caculation_Parameters['_PMOSA_POGate_Comb_length']           = _PMOSA_POGate_Comb_length
        _Caculation_Parameters['_PMOSA_POGate_Via_TF']                = _PMOSA_POGate_Via_TF
        _Caculation_Parameters['_PMOSA_POGate_ViaMxMx']               = _PMOSA_POGate_ViaMxMx


        _Caculation_Parameters['_PMOSB_MosType']                      = _PMOSB_MosType
        _Caculation_Parameters['_PMOSB_MosUpDn']                      = _PMOSB_MosUpDn

        _Caculation_Parameters['_PMOSB_NumberofGate']                 = _PMOSB_NumberofGate
        _Caculation_Parameters['_PMOSB_ChannelWidth']                 = _PMOSB_ChannelWidth
        _Caculation_Parameters['_PMOSB_ChannelLength']                = _PMOSB_ChannelLength
        _Caculation_Parameters['_PMOSB_GateSpacing']                  = _PMOSB_GateSpacing
        _Caculation_Parameters['_PMOSB_SDWidth']                      = _PMOSB_SDWidth
        _Caculation_Parameters['_PMOSB_XVT']                          = _PMOSB_XVT
        _Caculation_Parameters['_PMOSB_PCCrit']                       = _PMOSB_PCCrit

        _Caculation_Parameters['_PMOSB_Source_Via_TF']                = _PMOSB_Source_Via_TF
        _Caculation_Parameters['_PMOSB_Source_Via_Close2POpin_TF']    = _PMOSB_Source_Via_Close2POpin_TF
        _Caculation_Parameters['_PMOSB_Source_Comb_TF']               = _PMOSB_Source_Comb_TF
        _Caculation_Parameters['_PMOSB_Source_Comb_POpinward_TF']     = _PMOSB_Source_Comb_POpinward_TF
        _Caculation_Parameters['_PMOSB_Source_Comb_Length']           = _PMOSB_Source_Comb_Length

        _Caculation_Parameters['_PMOSB_Drain_Via_TF']                 = _PMOSB_Drain_Via_TF
        _Caculation_Parameters['_PMOSB_Drain_Via_Close2POpin_TF']     = _PMOSB_Drain_Via_Close2POpin_TF
        _Caculation_Parameters['_PMOSB_Drain_Comb_TF']                = _PMOSB_Drain_Comb_TF
        _Caculation_Parameters['_PMOSB_Drain_Comb_POpinward_TF']      = _PMOSB_Drain_Comb_POpinward_TF
        _Caculation_Parameters['_PMOSB_Drain_Comb_Length']            = _PMOSB_Drain_Comb_Length

        _Caculation_Parameters['_PMOSB_PODummy_TF']                   = _PMOSB_PODummy_TF
        _Caculation_Parameters['_PMOSB_PODummy_Length']               = _PMOSB_PODummy_Length
        _Caculation_Parameters['_PMOSB_PODummy_Placement']            = _PMOSB_PODummy_Placement

        _Caculation_Parameters['_PMOSB_Xvt_MinExten_TF']              = _PMOSB_Xvt_MinExten_TF
        _Caculation_Parameters['_PMOSB_Xvt_Placement']                = _PMOSB_Xvt_Placement

        _Caculation_Parameters['_PMOSB_POGate_Comb_TF']               = _PMOSB_POGate_Comb_TF
        _Caculation_Parameters['_PMOSB_POGate_Comb_length']           = _PMOSB_POGate_Comb_length
        _Caculation_Parameters['_PMOSB_POGate_Via_TF']                = _PMOSB_POGate_Via_TF
        _Caculation_Parameters['_PMOSB_POGate_ViaMxMx']               = _PMOSB_POGate_ViaMxMx


        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Pullup'] = self._SrefElementDeclaration(_DesignObj=D02_01_Pullup_KJH0._Pullup(_DesignParameter=None, _Name='{}:SRF_Pullup'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOSA_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Pullup']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOSA_POWER'
        self._DesignParameter['SRF_Pullup']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOSA_POWER'
        self._DesignParameter['SRF_Pullup']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOSA_POWER'
        self._DesignParameter['SRF_Pullup']['_XYCoordinates'] = [[0, 0]]

              ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Pullup']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ## X
        tmp1_1 = self.get_outter_KJH4('SRF_Pulldown')
        target_coordx = np.round(0.5*(tmp1_1['_Mostright']['coord'][0] + tmp1_1['_Mostleft']['coord'][0]))
                                ## Y
        tmp1_2 = self.get_param_KJH4('SRF_Pulldown','SRF_NMOSA','BND_{}Layer'.format(_NMOSA_XVT))
        target_coordy = tmp1_2[0][0][0][0]['_XY_up'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ## X
        tmp2_1 = self.get_outter_KJH4('SRF_Pullup')
        approaching_coordx = np.round (0.5*(tmp2_1['_Mostright']['coord'][0] + tmp2_1['_Mostleft']['coord'][0]))
                                ## Y
        tmp2 = self.get_param_KJH4('SRF_Pullup','SRF_PMOSA','BND_{}Layer'.format(_PMOSA_XVT))
        approaching_coordy = tmp2[0][0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pullup')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[1] = New_Scoord[1] + _PMOSXvt2NMOSXvt
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Pullup']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Pullup: Nbody
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Pullup: Nbody: Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A07_NbodyContactPhyLen_KJH3._NbodyContactPhyLen._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length'] = None
        _Caculation_Parameters['_NumCont'] = _PMOSAB_Nbody_NumCont
        _Caculation_Parameters['_Vtc_flag'] = False

        ## Calculate '_Length'
        tmp = self.get_outter_KJH4('SRF_Pullup')
        _Caculation_Parameters['_Length'] = abs(tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0])

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Nbody'] = self._SrefElementDeclaration(_DesignObj=A07_NbodyContactPhyLen_KJH3._NbodyContactPhyLen(_DesignParameter=None,_Name='{}:SRF_Nbody'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Nbody']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nbody']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nbody']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nbody']['_XYCoordinates'] = [[0, 0]]

        ## Get_Scoord_v4.
        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_Nbody']['_XYCoordinates'] = [[0, 0]]

        if _PMOSAB_Nbody_Xvtdown2Nbody == None:
            ## Calculate
            ## Target_coord: _XY_type1
            ## X
            tmp1_1 = self.get_outter_KJH4('SRF_Pullup')
            target_coordx = np.round( 0.5 * (tmp1_1['_Mostright']['coord'][0] + tmp1_1['_Mostleft']['coord'][0]) )
            ## Y
            target_coordy = tmp1_1['_Mostup']['coord'][0]

            target_coord = [target_coordx, target_coordy]
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_down']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Nbody')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[1] = New_Scoord[1] + 50
            tmpXY.append(New_Scoord)
            ## Define Coordinates
            self._DesignParameter['SRF_Nbody']['_XYCoordinates'] = tmpXY

        else:
            ## Calculate
                ## Target_coord: _XY_type1
                    ##x
            tmp1_1 = self.get_outter_KJH4('SRF_Pullup')
            target_coordx = np.round( 0.5 * (tmp1_1['_Mostright']['coord'][0] + tmp1_1['_Mostleft']['coord'][0]) )
                    ##y
            tmp1 = self.get_param_KJH4('SRF_Pullup', 'SRF_PMOSA', 'BND_{}Layer'.format(_PMOSA_XVT))
            target_coordy = tmp1[0][0][0][0]['_XY_down'][1]
            target_coord = [target_coordx,target_coordy]

                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_down'
            ]
                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Nbody')
            Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[1] = New_Scoord[1] + _PMOSAB_Nbody_Xvtdown2Nbody
            tmpXY.append(New_Scoord)
            ## Define Coordinates
            self._DesignParameter['SRF_Nbody']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Pullup: PMOSA source and Nbody connection
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOSA_Source2Nbody_Vtc_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth : ViaYmin 기준
        tmp1 = self.get_param_KJH4('SRF_Pullup','SRF_PMOSA','BND_Source_M1')
        tmp2 = self.get_param_KJH4('SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_PMOSA_Source2Nbody_Vtc_M1']['_YWidth'] = abs (tmp1[0][0][0][0]['_XY_down'][1] - tmp2[0][0][0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Pullup','SRF_PMOSA','BND_Source_M1')
        self._DesignParameter['BND_PMOSA_Source2Nbody_Vtc_M1']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOSA_Source2Nbody_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        tmp = self.get_param_KJH4('SRF_Pullup','SRF_PMOSA','BND_Source_M1')
        for i in range(0,len(tmp[0][0])):
            ## Calculate Sref XYcoord
                ## Calculate
                    ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Pullup','SRF_PMOSA','BND_Source_M1')
            target_coord = tmp1[0][0][i][0]['_XY_down_left']
                    ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_PMOSA_Source2Nbody_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_down_left']
                    ## Sref coord
            tmp3 = self.get_param_KJH4('BND_PMOSA_Source2Nbody_Vtc_M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_PMOSA_Source2Nbody_Vtc_M1']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Pullup: NWELL Exten
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOSAB_NellExten'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Nbody','SRF_NbodyContactPhyLen','BND_Nwell')
        tmp2 = self.get_param_KJH4('SRF_Pullup','SRF_PMOSA','BND_{}Layer'.format(_PMOSA_XVT))
        self._DesignParameter['BND_PMOSAB_NellExten']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] )

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Nbody','SRF_NbodyContactPhyLen','BND_Nwell')
        self._DesignParameter['BND_PMOSAB_NellExten']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOSAB_NellExten']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
            ## initialized Sref coordinate
        self._DesignParameter['BND_PMOSAB_NellExten']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
                ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Nbody','SRF_NbodyContactPhyLen','BND_Nwell')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
                ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOSAB_NellExten')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOSAB_NellExten')
        Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_PMOSAB_NellExten']['_XYCoordinates'] = tmpXY





        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  IN/OUT
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########   IN/OUT : InputA
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## IN/OUT : InputA : Hrz M1
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_InputA_Hrz_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Pulldown','SRF_NMOSA', 'BND_Gate_Hrz_Mx')
        tmp2 = self.get_param_KJH4('SRF_Pullup','SRF_PMOSA', 'BND_Gate_Hrz_Mx')
        self._DesignParameter['BND_InputA_Hrz_M1']['_XWidth'] = abs( tmp2[0][0][0][0]['_XY_left'][0] - tmp1[0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_InputA_Hrz_M1']['_YWidth'] = 50

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_InputA_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_InputA_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Pulldown','SRF_NMOSA', 'BND_Gate_Hrz_Mx')
        tmp2 = self.get_param_KJH4('SRF_Pullup','SRF_PMOSA', 'BND_Gate_Hrz_Mx')

        if tmp2[0][0][0][0]['_XY_left'][0] > tmp1[0][0][0][0]['_XY_left'][0]:
            tmp1_1 = self.get_param_KJH4('SRF_Pullup','SRF_PMOSA', 'BND_Gate_Hrz_Mx')
            target_coord = tmp1_1[0][0][0][0]['_XY_down_left']
        else:
            tmp1_1 = self.get_param_KJH4('SRF_Pulldown','SRF_NMOSA', 'BND_Gate_Hrz_Mx')
            target_coord = tmp1_1[0][0][0][0]['_XY_down_left']

        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_InputA_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_down_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_InputA_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_InputA_Hrz_M1']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## IN/OUT : InputA : Vtc M1
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_InputA_Vtc_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Pulldown','SRF_NMOSA', 'BND_Gate_Hrz_Mx')
        tmp2 = self.get_param_KJH4('SRF_Pullup','SRF_PMOSA', 'BND_Gate_Hrz_Mx')
        self._DesignParameter['BND_InputA_Vtc_M1']['_YWidth'] = abs( tmp2[0][0][0][0]['_XY_up'][1] - tmp1[0][0][0][0]['_XY_down'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_InputA_Vtc_M1']['_XWidth'] = 50

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_InputA_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_InputA_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Pulldown','SRF_NMOSA', 'BND_Gate_Hrz_Mx')
        tmp2 = self.get_param_KJH4('SRF_Pullup','SRF_PMOSA', 'BND_Gate_Hrz_Mx')

        if tmp2[0][0][0][0]['_XY_left'][0] > tmp1[0][0][0][0]['_XY_left'][0]:
            tmp1_1 = self.get_param_KJH4('BND_InputA_Hrz_M1')
            target_coord = tmp1_1[0][0]['_XY_up_left']

        else:
            tmp1_1 = self.get_param_KJH4('BND_InputA_Hrz_M1')
            target_coord = tmp1_1[0][0]['_XY_down_left']

        ## Approaching_coord: _XY_type2
        tmp1 = self.get_param_KJH4('SRF_Pulldown','SRF_NMOSA', 'BND_Gate_Hrz_Mx')
        tmp2 = self.get_param_KJH4('SRF_Pullup','SRF_PMOSA', 'BND_Gate_Hrz_Mx')

        if tmp2[0][0][0][0]['_XY_left'][0] > tmp1[0][0][0][0]['_XY_left'][0]:
            tmp2 = self.get_param_KJH4('BND_InputA_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_up_left']

        else:
            tmp2 = self.get_param_KJH4('BND_InputA_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_down_left']

        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_InputA_Vtc_M1')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_InputA_Vtc_M1']['_XYCoordinates'] = tmpXY





        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########   IN/OUT : InputB
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## IN/OUT : InputB : Hrz M1
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_InputB_Hrz_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Pulldown','SRF_NMOSB','BND_Gate_Hrz_Mx')
        tmp2 = self.get_param_KJH4('SRF_Pullup','SRF_PMOSB','BND_Gate_Hrz_Mx')
        self._DesignParameter['BND_InputB_Hrz_M1']['_XWidth'] = abs( tmp2[0][0][0][0]['_XY_right'][0] - tmp1[0][0][0][0]['_XY_right'][0])

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_InputB_Hrz_M1']['_YWidth'] = 50

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_InputB_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_InputB_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Pulldown','SRF_NMOSB','BND_Gate_Hrz_Mx')
        tmp2 = self.get_param_KJH4('SRF_Pullup','SRF_PMOSB','BND_Gate_Hrz_Mx')

        if tmp2[0][0][0][0]['_XY_right'][0] < tmp1[0][0][0][0]['_XY_right'][0]:
            tmp1_1 = self.get_param_KJH4('SRF_Pullup','SRF_PMOSB','BND_Gate_Hrz_Mx')
            target_coord = tmp1_1[0][0][0][0]['_XY_down_right']
        else:
            tmp1_1 = self.get_param_KJH4('SRF_Pulldown','SRF_NMOSB','BND_Gate_Hrz_Mx')
            target_coord = tmp1_1[0][0][0][0]['_XY_down_right']

        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_InputB_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_InputB_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_InputB_Hrz_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## IN/OUT : InputB : Vtc M1
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_InputB_Vtc_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Pulldown','SRF_NMOSB','BND_Gate_Hrz_Mx')
        tmp2 = self.get_param_KJH4('SRF_Pullup','SRF_PMOSB','BND_Gate_Hrz_Mx')
        self._DesignParameter['BND_InputB_Vtc_M1']['_YWidth'] = abs( tmp2[0][0][0][0]['_XY_up'][1] - tmp1[0][0][0][0]['_XY_down'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_InputB_Vtc_M1']['_XWidth'] = 50

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_InputB_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_InputB_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Pulldown','SRF_NMOSB','BND_Gate_Hrz_Mx')
        tmp2 = self.get_param_KJH4('SRF_Pullup','SRF_PMOSB','BND_Gate_Hrz_Mx')

        if tmp2[0][0][0][0]['_XY_right'][0] < tmp1[0][0][0][0]['_XY_right'][0]:
            tmp1_1 = self.get_param_KJH4('BND_InputB_Hrz_M1')
            target_coord = tmp1_1[0][0]['_XY_up_right']

        else:
            tmp1_1 = self.get_param_KJH4('BND_InputB_Hrz_M1')
            target_coord = tmp1_1[0][0]['_XY_down_right']

        ## Approaching_coord: _XY_type2
        tmp1 = self.get_param_KJH4('SRF_Pulldown','SRF_NMOSB','BND_Gate_Hrz_Mx')
        tmp2 = self.get_param_KJH4('SRF_Pullup','SRF_PMOSB','BND_Gate_Hrz_Mx')

        if tmp2[0][0][0][0]['_XY_right'][0] < tmp1[0][0][0][0]['_XY_right'][0]:
            tmp2 = self.get_param_KJH4('BND_InputB_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_up_right']

        else:
            tmp2 = self.get_param_KJH4('BND_InputB_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_down_right']

        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_InputB_Vtc_M1')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_InputB_Vtc_M1']['_XYCoordinates'] = tmpXY






        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########   IN/OUT : Out
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## IN/OUT : PMOSB Drain M2 Exten
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOSB_Drain_M2_Exten'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _XWidth
            # Most right
        tmp1 = self.get_param_KJH4('SRF_Pulldown','SRF_NMOSB','BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_Pullup','SRF_PMOSB','BND_Met1Layer')

        if tmp1[0][0][-1][0]['_XY_right'][0] > tmp2[0][0][-1][0]['_XY_right'][0]:
            most_right = tmp1[0][0][-1][0]['_XY_right'][0]
        else:
            most_right = tmp2[0][0][-1][0]['_XY_right'][0]

            # Xwidth
        tmp = self.get_param_KJH4('SRF_Pullup','SRF_PMOSB','BND_Drain_Hrz_M2')
        self._DesignParameter['BND_PMOSB_Drain_M2_Exten']['_XWidth'] = abs(most_right - tmp[0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_PMOSB_Drain_M2_Exten']['_YWidth'] = 50

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOSB_Drain_M2_Exten']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_PMOSB_Drain_M2_Exten']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Pullup','SRF_PMOSB','BND_Drain_Hrz_M2')
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOSB_Drain_M2_Exten')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOSB_Drain_M2_Exten')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['BND_PMOSB_Drain_M2_Exten']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## IN/OUT : NMOSB Drain M2 Exten
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NMOSB_Drain_M2_Exten'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _XWidth
            # Most right
        tmp1 = self.get_param_KJH4('SRF_Pulldown','SRF_NMOSB','BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_Pullup','SRF_PMOSB','BND_Met1Layer')

        if tmp1[0][0][-1][0]['_XY_right'][0] > tmp2[0][0][-1][0]['_XY_right'][0]:
            most_right = tmp1[0][0][-1][0]['_XY_right'][0]
        else:
            most_right = tmp2[0][0][-1][0]['_XY_right'][0]

            # Xwidth
        tmp = self.get_param_KJH4('SRF_Pulldown','SRF_NMOSB','BND_Drain_Hrz_M2')
        self._DesignParameter['BND_NMOSB_Drain_M2_Exten']['_XWidth'] = abs(most_right - tmp[0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_NMOSB_Drain_M2_Exten']['_YWidth'] = 50

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NMOSB_Drain_M2_Exten']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_NMOSB_Drain_M2_Exten']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Pulldown','SRF_NMOSB','BND_Drain_Hrz_M2')
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NMOSB_Drain_M2_Exten')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NMOSB_Drain_M2_Exten')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['BND_NMOSB_Drain_M2_Exten']['_XYCoordinates'] = tmpXY





        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## IN/OUT : Out : Vtc M2
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Out_Vtc_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Out_Vtc_M2']['_XWidth'] = 50

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_NMOSB_Drain_M2_Exten')
        tmp2 = self.get_param_KJH4('BND_PMOSB_Drain_M2_Exten')
        self._DesignParameter['BND_Out_Vtc_M2']['_YWidth'] = abs( tmp2[0][0]['_XY_up'][1] - tmp1[0][0]['_XY_down'][1] )

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Out_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Out_Vtc_M2']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_NMOSB_Drain_M2_Exten')
        target_coord = tmp1[0][0]['_XY_down_right']

        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Out_Vtc_M2')
        approaching_coord = tmp2[0][0]['_XY_down_right']

        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Out_Vtc_M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Out_Vtc_M2']['_XYCoordinates'] = tmpXY

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
    libname = 'Proj_ADC_D02_SARLogic_Nor_KJH1'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'D02_02_Nor_v1_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

    ## Pbody
        # NMOSAB Pbody
        _NMOSAB_Pbody_NumCont=2,  # Number
        _NMOSAB_Pbody_XvtTop2Pbody=None,  # Number/None(Minimum)

    ## Nbody
        # Nbody
        _PMOSAB_Nbody_NumCont=2,  # Number
        _PMOSAB_Nbody_Xvtdown2Nbody=None,  # Number/None(Minimum)

    # PMOS and NMOS Height
        _PMOSXvt2NMOSXvt=1150,  # number

    # NMosfetA
        # PMOS/NMOS
        _NMOSA_MosType                   = 'NMOS',   # 'NMOS'/'PMOS'
        # MOS Up/Dn
        _NMOSA_MosUpDn                   = 'Up',     # 'Up'/'Dn'
        # Physical dimension
        _NMOSA_NumberofGate	            = 2,        # Number
        _NMOSA_ChannelWidth	            = 200,      # Number
        _NMOSA_ChannelLength	        = 30,       # Number
        _NMOSA_GateSpacing		        = None,     # None/Number
        _NMOSA_SDWidth			        = None,     # None/Number
        _NMOSA_XVT				        = 'HVT',   # 'XVT' ex)SLVT/LVT/RVT/HVT
        _NMOSA_PCCrit				    = True,     # None/True
        # Source_node setting
            # Via setting
        _NMOSA_Source_Via_TF              = False,     # True/False
                # Via close to POpin
        _NMOSA_Source_Via_Close2POpin_TF  = False,     # True/False
            # Comb setting: If Via is True
        _NMOSA_Source_Comb_TF             = False,     # True/False
                # Comb POPinward
        _NMOSA_Source_Comb_POpinward_TF   = False,     # True/False
                # Comb vertical_length
        _NMOSA_Source_Comb_Length         = None,     # None/Number

        # Drain_node_setting
            # Via setting
        _NMOSA_Drain_Via_TF               = True,     # True/False
                # Via close to POpin
        _NMOSA_Drain_Via_Close2POpin_TF   = True,     # True/False
            # Comb setting: If Via is True
        _NMOSA_Drain_Comb_TF              = True,     # True/False
                # Comb POPinward
        _NMOSA_Drain_Comb_POpinward_TF    = True,     # True/False
                # Comb vertical_length
        _NMOSA_Drain_Comb_Length          = None,     # None/Number

        # POLY dummy setting
        _NMOSA_PODummy_TF                 = True,  # TF
            # if _NMOSADummy == True
        _NMOSA_PODummy_Length             = None,  # None/Value
        _NMOSA_PODummy_Placement          = None,  # None/'Up'/'Dn'/

        # XVT setting
            # XVT setting : Exten XVT area if area is min
        _NMOSA_Xvt_MinExten_TF            = True,     # True/False
            # XVT setting : None(Cent), Up, Dn
        _NMOSA_Xvt_Placement              = 'Up',     # None/'Up'/'Dn'/

        # Poly Gate setting
        _NMOSA_POGate_Comb_TF             = True,     # True/False
            # Poly Gate setting : vertical length
        _NMOSA_POGate_Comb_length         = 100,     # None/Number
            # Poly Gate Via setting
        _NMOSA_POGate_Via_TF              = True,     # True/False
            # Poly Gate Via setting :
        _NMOSA_POGate_ViaMxMx             = [0 ,1],     # Ex) [1,5] -> ViaM1M5


    # NMosfetB
        # PMOS/NMOS
        _NMOSB_MosType                   = 'NMOS',   # 'NMOS'/'PMOS'
        # MOS Up/Dn
        _NMOSB_MosUpDn                   = 'Up',     # 'Up'/'Dn'
        # Physical dimension
        _NMOSB_NumberofGate	            = 2,        # Number
        _NMOSB_ChannelWidth	            = 200,      # Number
        _NMOSB_ChannelLength	        = 30,       # Number
        _NMOSB_GateSpacing		        = None,     # None/Number
        _NMOSB_SDWidth			        = None,     # None/Number
        _NMOSB_XVT				        = 'HVT',   # 'XVT' ex)SLVT/LVT/RVT/HVT
        _NMOSB_PCCrit				    = True,     # None/True
        # Source_node setting
            # Via setting
        _NMOSB_Source_Via_TF              = False,     # True/False
                # Via close to POpin
        _NMOSB_Source_Via_Close2POpin_TF  = False,     # True/False
            # Comb setting: If Via is True
        _NMOSB_Source_Comb_TF             = False,     # True/False
                # Comb POPinward
        _NMOSB_Source_Comb_POpinward_TF   = False,     # True/False
                # Comb vertical_length
        _NMOSB_Source_Comb_Length         = None,     # None/Number

        # Drain_node_setting
            # Via setting
        _NMOSB_Drain_Via_TF               = True,     # True/False
                # Via close to POpin
        _NMOSB_Drain_Via_Close2POpin_TF   = True,     # True/False
            # Comb setting: If Via is True
        _NMOSB_Drain_Comb_TF              = True,     # True/False
                # Comb POPinward
        _NMOSB_Drain_Comb_POpinward_TF    = True,     # True/False
                # Comb vertical_length
        _NMOSB_Drain_Comb_Length          = None,     # None/Number

        # POLY dummy setting
        _NMOSB_PODummy_TF                 = True,  # TF
            # if _NMOSBDummy == True
        _NMOSB_PODummy_Length             = None,  # None/Value
        _NMOSB_PODummy_Placement          = None,  # None/'Up'/'Dn'/

        # XVT setting
            # XVT setting : Exten XVT area if area is min
        _NMOSB_Xvt_MinExten_TF            = True,     # True/False
            # XVT setting : None(Cent), Up, Dn
        _NMOSB_Xvt_Placement              = 'Up',     # None/'Up'/'Dn'/

        # Poly Gate setting
        _NMOSB_POGate_Comb_TF             = True,     # True/False
            # Poly Gate setting : vertical length
        _NMOSB_POGate_Comb_length         = 100,     # None/Number
            # Poly Gate Via setting
        _NMOSB_POGate_Via_TF              = True,     # None/'Up'/'Dn'/
            # Poly Gate Via setting :
        _NMOSB_POGate_ViaMxMx             = [0 ,1],     # Ex) [1,5] -> ViaM1M5


    # PMosfetA
        # PMOS/NMOS
        _PMOSA_MosType                   = 'PMOS',   # 'NMOS'/'PMOS'
        # MOS Up/Dn
        _PMOSA_MosUpDn                   = 'Dn',     # 'Up'/'Dn'
        # Physical dimension
        _PMOSA_NumberofGate	            = 4,        # Number
        _PMOSA_ChannelWidth	            = 400,      # Number
        _PMOSA_ChannelLength	        = 30,       # Number
        _PMOSA_GateSpacing		        = None,     # None/Number
        _PMOSA_SDWidth			        = None,     # None/Number
        _PMOSA_XVT				        = 'HVT',   # 'XVT' ex)SLVT/LVT/RVT/HVT
        _PMOSA_PCCrit				    = True,     # None/True
        # Source_node setting
            # Via setting
        _PMOSA_Source_Via_TF              = False,     # True/False
                # Via close to POpin
        _PMOSA_Source_Via_Close2POpin_TF  = False,     # True/False
            # Comb setting: If Via is True
        _PMOSA_Source_Comb_TF             = False,     # True/False
                # Comb POPinward
        _PMOSA_Source_Comb_POpinward_TF   = False,     # True/False
                # Comb vertical_length
        _PMOSA_Source_Comb_Length         = None,     # None/Number

        # Drain_node_setting
            # Via setting
        _PMOSA_Drain_Via_TF               = True,     # True/False
                # Via close to POpin
        _PMOSA_Drain_Via_Close2POpin_TF   = False,     # True/False
            # Comb setting: If Via is True
        _PMOSA_Drain_Comb_TF              = True,     # True/False
                # Comb POPinward
        _PMOSA_Drain_Comb_POpinward_TF    = False,     # True/False
                # Comb vertical_length
        _PMOSA_Drain_Comb_Length          = None,     # None/Number

        # POLY dummy setting
        _PMOSA_PODummy_TF                 = True,  # TF
            # if _PMOSADummy == True
        _PMOSA_PODummy_Length             = None,  # None/Value
        _PMOSA_PODummy_Placement          = None,  # None/'Up'/'Dn'/

        # XVT setting
            # XVT setting : Exten XVT area if area is min
        _PMOSA_Xvt_MinExten_TF            = True,     # True/False
            # XVT setting : None(Cent), Up, Dn
        _PMOSA_Xvt_Placement              = 'Dn',     # None/'Up'/'Dn'/

        # Poly Gate setting
        _PMOSA_POGate_Comb_TF             = True,     # True/False
            # Poly Gate setting : vertical length
        _PMOSA_POGate_Comb_length         = 100,     # None/Number
            # Poly Gate Via setting
        _PMOSA_POGate_Via_TF              = True,     # True/False
            # Poly Gate Via setting :
        _PMOSA_POGate_ViaMxMx             = [0 ,1],     # Ex) [1,5] -> ViaM1M5


    # PMosfetB
        # PMOS/NMOS
        _PMOSB_MosType                   = 'PMOS',   # 'NMOS'/'PMOS'
        # MOS Up/Dn
        _PMOSB_MosUpDn                   = 'Dn',     # 'Up'/'Dn'
        # Physical dimension
        _PMOSB_NumberofGate	            = 4,        # Number
        _PMOSB_ChannelWidth	            = 400,      # Number
        _PMOSB_ChannelLength	        = 30,       # Number
        _PMOSB_GateSpacing		        = None,     # None/Number
        _PMOSB_SDWidth			        = None,     # None/Number
        _PMOSB_XVT				        = 'HVT',   # 'XVT' ex)SLVT/LVT/RVT/HVT
        _PMOSB_PCCrit				    = True,     # None/True
        # Source_node setting
            # Via setting
        _PMOSB_Source_Via_TF              = True,     # True/False
                # Via close to POpin
        _PMOSB_Source_Via_Close2POpin_TF  = True,     # True/False
            # Comb setting: If Via is True
        _PMOSB_Source_Comb_TF             = True,     # True/False
                # Comb POPinward
        _PMOSB_Source_Comb_POpinward_TF   = False,     # True/False
                # Comb vertical_length
        _PMOSB_Source_Comb_Length         = None,     # None/Number

        # Drain_node_setting
            # Via setting
        _PMOSB_Drain_Via_TF               = True,     # True/False
                # Via close to POpin
        _PMOSB_Drain_Via_Close2POpin_TF   = False,     # True/False
            # Comb setting: If Via is True
        _PMOSB_Drain_Comb_TF              = True,     # True/False
                # Comb POPinward
        _PMOSB_Drain_Comb_POpinward_TF    = True,     # True/False
                # Comb vertical_length
        _PMOSB_Drain_Comb_Length          = None,     # None/Number

        # POLY dummy setting
        _PMOSB_PODummy_TF                 = True,  # TF
            # if _PMOSBDummy == True
        _PMOSB_PODummy_Length             = None,  # None/Value
        _PMOSB_PODummy_Placement          = None,  # None/'Up'/'Dn'/

        # XVT setting
            # XVT setting : Exten XVT area if area is min
        _PMOSB_Xvt_MinExten_TF            = True,     # True/False
            # XVT setting : None(Cent), Up, Dn
        _PMOSB_Xvt_Placement              = 'Dn',     # None/'Up'/'Dn'/

        # Poly Gate setting
        _PMOSB_POGate_Comb_TF             = True,     # True/False
            # Poly Gate setting : vertical length
        _PMOSB_POGate_Comb_length         = 100,     # None/Number
            # Poly Gate Via setting
        _PMOSB_POGate_Via_TF              = True,     # None/'Up'/'Dn'/
            # Poly Gate Via setting :
        _PMOSB_POGate_ViaMxMx             = [0 ,1],     # Ex) [1,5] -> ViaM1M5



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
    LayoutObj = _Nor(_DesignParameter=None, _Name=cellname)
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
    # Checker.lib_deletion()
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
