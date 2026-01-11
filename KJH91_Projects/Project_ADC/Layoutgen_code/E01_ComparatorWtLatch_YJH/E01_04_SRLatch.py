
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
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.E01_ComparatorWtLatch_YJH import E01_02_NAND_YJH

## Define Class
class _SRLatch(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
        ##########
        ## NANDS Design parameters
        # NMOSA
        _NANDS_NMOSA_NMOSNumberofGate=None,  # number
        _NANDS_NMOSA_NMOSChannelWidth=None,  # number
        _NANDS_NMOSA_NMOSChannellength=None,  # number
        _NANDS_NMOSA_GateSpacing=None,  # None/number
        _NANDS_NMOSA_SDWidth=None,  # None/number
        _NANDS_NMOSA_XVT=None,  # 'XVT' ex)SLVT LVT RVT HVT
        _NANDS_NMOSA_PCCrit=None,  # None/True

        # Source_node_ViaM1M2
        _NANDS_NMOSA_Source_Via_TF=None,  # True/False

        # Drain_node_ViaM1M2
        _NANDS_NMOSA_Drain_Via_TF=None,  # True/False

        # POLY dummy setting
        _NANDS_NMOSA_NMOSDummy=None,  # TF
        # if _PMOSDummy == True
        _NANDS_NMOSA_NMOSDummy_length=None,  # None/Value
        _NANDS_NMOSA_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # NMOSB
        _NANDS_NMOSB_NMOSNumberofGate=None,  # number
        _NANDS_NMOSB_NMOSChannelWidth=None,  # number
        _NANDS_NMOSB_NMOSChannellength=None,  # number
        _NANDS_NMOSB_GateSpacing=None,  # None/number
        _NANDS_NMOSB_SDWidth=None,  # None/number
        _NANDS_NMOSB_XVT=None,  # 'XVT' ex)SLVT LVT RVT HVT
        _NANDS_NMOSB_PCCrit=None,  # None/True

        # Source_node_ViaM1M2
        _NANDS_NMOSB_Source_Via_TF=None,  # True/False

        # Drain_node_ViaM1M2
        _NANDS_NMOSB_Drain_Via_TF=None,  # True/False

        # POLY dummy setting
        _NANDS_NMOSB_NMOSDummy=None,  # TF
        # if _PMOSDummy == True
        _NANDS_NMOSB_NMOSDummy_length=None,  # None/Value
        _NANDS_NMOSB_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # NMOSAB Pbody
        _NANDS_NMOSAB_Pbody_NumCont=None,  # Number
        _NANDS_NMOSAB_Pbody_XlvtTop2Pdoby=None,  # Number/None(Minimum)

        # PMOSA
        _NANDS_PMOSA_PMOSNumberofGate=None,  # number
        _NANDS_PMOSA_PMOSChannelWidth=None,  # number
        _NANDS_PMOSA_PMOSChannellength=None,  # number
        _NANDS_PMOSA_GateSpacing=None,  # None/number
        _NANDS_PMOSA_SDWidth=None,  # None/number
        _NANDS_PMOSA_XVT=None,  # 'XVT' ex)SLVT LVT RVT HVT
        _NANDS_PMOSA_PCCrit=None,  # None/True

        # Source_node_ViaM1M2
        _NANDS_PMOSA_Source_Via_TF=None,  # True/False

        # Drain_node_ViaM1M2
        _NANDS_PMOSA_Drain_Via_TF=None,  # True/False

        # POLY dummy setting
        _NANDS_PMOSA_PMOSDummy=None,  # TF
        # if _PMOSDummy == True
        _NANDS_PMOSA_PMOSDummy_length=None,  # None/Value
        _NANDS_PMOSA_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # PMOSB
        _NANDS_PMOSB_PMOSNumberofGate=None,  # number
        _NANDS_PMOSB_PMOSChannelWidth=None,  # number
        _NANDS_PMOSB_PMOSChannellength=None,  # number
        _NANDS_PMOSB_GateSpacing=None,  # None/number
        _NANDS_PMOSB_SDWidth=None,  # None/number
        _NANDS_PMOSB_XVT=None,  # 'XVT' ex)SLVT LVT RVT HVT
        _NANDS_PMOSB_PCCrit=None,  # None/True

        # Source_node_ViaM1M2
        _NANDS_PMOSB_Source_Via_TF=None,  # True/False

        # Drain_node_ViaM1M2
        _NANDS_PMOSB_Drain_Via_TF=None,  # True/False

        # POLY dummy setting
        _NANDS_PMOSB_PMOSDummy=None,  # TF
        # if _PMOSDummy == True
        _NANDS_PMOSB_PMOSDummy_length=None,  # None/Value
        _NANDS_PMOSB_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Nbody
        _NANDS_PMOSAB_Nbody_NumCont=None,  # Number
        _NANDS_PMOSAB_Nbody_Xlvtdown2Ndoby=None,  # Number/None(Minimum)

        # PMOS and NMOS Height
        _NANDS_PMOSXvt2NMOSXvt=None,  # number

        ##########
        ## NANDR Design parameters
        # NMOSA
        _NANDR_NMOSA_NMOSNumberofGate=None,  # number
        _NANDR_NMOSA_NMOSChannelWidth=None,  # number
        _NANDR_NMOSA_NMOSChannellength=None,  # number
        _NANDR_NMOSA_GateSpacing=None,  # None/number
        _NANDR_NMOSA_SDWidth=None,  # None/number
        _NANDR_NMOSA_XVT=None,  # 'XVT' ex)SLVT LVT RVT HVT
        _NANDR_NMOSA_PCCrit=None,  # None/True

        # Source_node_ViaM1M2
        _NANDR_NMOSA_Source_Via_TF=None,  # True/False

        # Drain_node_ViaM1M2
        _NANDR_NMOSA_Drain_Via_TF=None,  # True/False

        # POLY dummy setting
        _NANDR_NMOSA_NMOSDummy=None,  # TF
        # if _PMOSDummy == True
        _NANDR_NMOSA_NMOSDummy_length=None,  # None/Value
        _NANDR_NMOSA_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # NMOSB
        _NANDR_NMOSB_NMOSNumberofGate=None,  # number
        _NANDR_NMOSB_NMOSChannelWidth=None,  # number
        _NANDR_NMOSB_NMOSChannellength=None,  # number
        _NANDR_NMOSB_GateSpacing=None,  # None/number
        _NANDR_NMOSB_SDWidth=None,  # None/number
        _NANDR_NMOSB_XVT=None,  # 'XVT' ex)SLVT LVT RVT HVT
        _NANDR_NMOSB_PCCrit=None,  # None/True

        # Source_node_ViaM1M2
        _NANDR_NMOSB_Source_Via_TF=None,  # True/False

        # Drain_node_ViaM1M2
        _NANDR_NMOSB_Drain_Via_TF=None,  # True/False

        # POLY dummy setting
        _NANDR_NMOSB_NMOSDummy=None,  # TF
        # if _PMOSDummy == True
        _NANDR_NMOSB_NMOSDummy_length=None,  # None/Value
        _NANDR_NMOSB_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # NMOSAB Pbody
        _NANDR_NMOSAB_Pbody_NumCont=None,  # Number
        _NANDR_NMOSAB_Pbody_XlvtTop2Pdoby=None,  # Number/None(Minimum)

        # PMOSA
        _NANDR_PMOSA_PMOSNumberofGate=None,  # number
        _NANDR_PMOSA_PMOSChannelWidth=None,  # number
        _NANDR_PMOSA_PMOSChannellength=None,  # number
        _NANDR_PMOSA_GateSpacing=None,  # None/number
        _NANDR_PMOSA_SDWidth=None,  # None/number
        _NANDR_PMOSA_XVT=None,  # 'XVT' ex)SLVT LVT RVT HVT
        _NANDR_PMOSA_PCCrit=None,  # None/True

        # Source_node_ViaM1M2
        _NANDR_PMOSA_Source_Via_TF=None,  # True/False

        # Drain_node_ViaM1M2
        _NANDR_PMOSA_Drain_Via_TF=None,  # True/False

        # POLY dummy setting
        _NANDR_PMOSA_PMOSDummy=None,  # TF
        # if _PMOSDummy == True
        _NANDR_PMOSA_PMOSDummy_length=None,  # None/Value
        _NANDR_PMOSA_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # PMOSB
        _NANDR_PMOSB_PMOSNumberofGate=None,  # number
        _NANDR_PMOSB_PMOSChannelWidth=None,  # number
        _NANDR_PMOSB_PMOSChannellength=None,  # number
        _NANDR_PMOSB_GateSpacing=None,  # None/number
        _NANDR_PMOSB_SDWidth=None,  # None/number
        _NANDR_PMOSB_XVT=None,  # 'XVT' ex)SLVT LVT RVT HVT
        _NANDR_PMOSB_PCCrit=None,  # None/True

        # Source_node_ViaM1M2
        _NANDR_PMOSB_Source_Via_TF=None,  # True/False

        # Drain_node_ViaM1M2
        _NANDR_PMOSB_Drain_Via_TF=None,  # True/False

        # POLY dummy setting
        _NANDR_PMOSB_PMOSDummy=None,  # TF
        # if _PMOSDummy == True
        _NANDR_PMOSB_PMOSDummy_length=None,  # None/Value
        _NANDR_PMOSB_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Nbody
        _NANDR_PMOSAB_Nbody_NumCont=None,  # Number
        _NANDR_PMOSAB_Nbody_Xlvtdown2Ndoby=None,  # Number/None(Minimum)

        # PMOS and NMOS Height
        _NANDR_PMOSXvt2NMOSXvt=None,  # number
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
                                  ##########
                                  ## NANDS Design parameters
                                  # NMOSA
                                  _NANDS_NMOSA_NMOSNumberofGate=None,  # number
                                  _NANDS_NMOSA_NMOSChannelWidth=None,  # number
                                  _NANDS_NMOSA_NMOSChannellength=None,  # number
                                  _NANDS_NMOSA_GateSpacing=None,  # None/number
                                  _NANDS_NMOSA_SDWidth=None,  # None/number
                                  _NANDS_NMOSA_XVT=None,  # 'XVT' ex)SLVT LVT RVT HVT
                                  _NANDS_NMOSA_PCCrit=None,  # None/True

                                  # Source_node_ViaM1M2
                                  _NANDS_NMOSA_Source_Via_TF=None,  # True/False

                                  # Drain_node_ViaM1M2
                                  _NANDS_NMOSA_Drain_Via_TF=None,  # True/False

                                  # POLY dummy setting
                                  _NANDS_NMOSA_NMOSDummy=None,  # TF
                                  # if _PMOSDummy == True
                                  _NANDS_NMOSA_NMOSDummy_length=None,  # None/Value
                                  _NANDS_NMOSA_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # NMOSB
                                  _NANDS_NMOSB_NMOSNumberofGate=None,  # number
                                  _NANDS_NMOSB_NMOSChannelWidth=None,  # number
                                  _NANDS_NMOSB_NMOSChannellength=None,  # number
                                  _NANDS_NMOSB_GateSpacing=None,  # None/number
                                  _NANDS_NMOSB_SDWidth=None,  # None/number
                                  _NANDS_NMOSB_XVT=None,  # 'XVT' ex)SLVT LVT RVT HVT
                                  _NANDS_NMOSB_PCCrit=None,  # None/True

                                  # Source_node_ViaM1M2
                                  _NANDS_NMOSB_Source_Via_TF=None,  # True/False

                                  # Drain_node_ViaM1M2
                                  _NANDS_NMOSB_Drain_Via_TF=None,  # True/False

                                  # POLY dummy setting
                                  _NANDS_NMOSB_NMOSDummy=None,  # TF
                                  # if _PMOSDummy == True
                                  _NANDS_NMOSB_NMOSDummy_length=None,  # None/Value
                                  _NANDS_NMOSB_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # NMOSAB Pbody
                                  _NANDS_NMOSAB_Pbody_NumCont=None,  # Number
                                  _NANDS_NMOSAB_Pbody_XlvtTop2Pdoby=None,  # Number/None(Minimum)

                                  # PMOSA
                                  _NANDS_PMOSA_PMOSNumberofGate=None,  # number
                                  _NANDS_PMOSA_PMOSChannelWidth=None,  # number
                                  _NANDS_PMOSA_PMOSChannellength=None,  # number
                                  _NANDS_PMOSA_GateSpacing=None,  # None/number
                                  _NANDS_PMOSA_SDWidth=None,  # None/number
                                  _NANDS_PMOSA_XVT=None,  # 'XVT' ex)SLVT LVT RVT HVT
                                  _NANDS_PMOSA_PCCrit=None,  # None/True

                                  # Source_node_ViaM1M2
                                  _NANDS_PMOSA_Source_Via_TF=None,  # True/False

                                  # Drain_node_ViaM1M2
                                  _NANDS_PMOSA_Drain_Via_TF=None,  # True/False

                                  # POLY dummy setting
                                  _NANDS_PMOSA_PMOSDummy=None,  # TF
                                  # if _PMOSDummy == True
                                  _NANDS_PMOSA_PMOSDummy_length=None,  # None/Value
                                  _NANDS_PMOSA_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # PMOSB
                                  _NANDS_PMOSB_PMOSNumberofGate=None,  # number
                                  _NANDS_PMOSB_PMOSChannelWidth=None,  # number
                                  _NANDS_PMOSB_PMOSChannellength=None,  # number
                                  _NANDS_PMOSB_GateSpacing=None,  # None/number
                                  _NANDS_PMOSB_SDWidth=None,  # None/number
                                  _NANDS_PMOSB_XVT=None,  # 'XVT' ex)SLVT LVT RVT HVT
                                  _NANDS_PMOSB_PCCrit=None,  # None/True

                                  # Source_node_ViaM1M2
                                  _NANDS_PMOSB_Source_Via_TF=None,  # True/False

                                  # Drain_node_ViaM1M2
                                  _NANDS_PMOSB_Drain_Via_TF=None,  # True/False

                                  # POLY dummy setting
                                  _NANDS_PMOSB_PMOSDummy=None,  # TF
                                  # if _PMOSDummy == True
                                  _NANDS_PMOSB_PMOSDummy_length=None,  # None/Value
                                  _NANDS_PMOSB_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Nbody
                                  _NANDS_PMOSAB_Nbody_NumCont=None,  # Number
                                  _NANDS_PMOSAB_Nbody_Xlvtdown2Ndoby=None,  # Number/None(Minimum)

                                  # PMOS and NMOS Height
                                  _NANDS_PMOSXvt2NMOSXvt=None,  # number

                                  ##########
                                  ## NANDR Design parameters
                                  # NMOSA
                                  _NANDR_NMOSA_NMOSNumberofGate=None,  # number
                                  _NANDR_NMOSA_NMOSChannelWidth=None,  # number
                                  _NANDR_NMOSA_NMOSChannellength=None,  # number
                                  _NANDR_NMOSA_GateSpacing=None,  # None/number
                                  _NANDR_NMOSA_SDWidth=None,  # None/number
                                  _NANDR_NMOSA_XVT=None,  # 'XVT' ex)SLVT LVT RVT HVT
                                  _NANDR_NMOSA_PCCrit=None,  # None/True

                                  # Source_node_ViaM1M2
                                  _NANDR_NMOSA_Source_Via_TF=None,  # True/False

                                  # Drain_node_ViaM1M2
                                  _NANDR_NMOSA_Drain_Via_TF=None,  # True/False

                                  # POLY dummy setting
                                  _NANDR_NMOSA_NMOSDummy=None,  # TF
                                  # if _PMOSDummy == True
                                  _NANDR_NMOSA_NMOSDummy_length=None,  # None/Value
                                  _NANDR_NMOSA_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # NMOSB
                                  _NANDR_NMOSB_NMOSNumberofGate=None,  # number
                                  _NANDR_NMOSB_NMOSChannelWidth=None,  # number
                                  _NANDR_NMOSB_NMOSChannellength=None,  # number
                                  _NANDR_NMOSB_GateSpacing=None,  # None/number
                                  _NANDR_NMOSB_SDWidth=None,  # None/number
                                  _NANDR_NMOSB_XVT=None,  # 'XVT' ex)SLVT LVT RVT HVT
                                  _NANDR_NMOSB_PCCrit=None,  # None/True

                                  # Source_node_ViaM1M2
                                  _NANDR_NMOSB_Source_Via_TF=None,  # True/False

                                  # Drain_node_ViaM1M2
                                  _NANDR_NMOSB_Drain_Via_TF=None,  # True/False

                                  # POLY dummy setting
                                  _NANDR_NMOSB_NMOSDummy=None,  # TF
                                  # if _PMOSDummy == True
                                  _NANDR_NMOSB_NMOSDummy_length=None,  # None/Value
                                  _NANDR_NMOSB_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # NMOSAB Pbody
                                  _NANDR_NMOSAB_Pbody_NumCont=None,  # Number
                                  _NANDR_NMOSAB_Pbody_XlvtTop2Pdoby=None,  # Number/None(Minimum)

                                  # PMOSA
                                  _NANDR_PMOSA_PMOSNumberofGate=None,  # number
                                  _NANDR_PMOSA_PMOSChannelWidth=None,  # number
                                  _NANDR_PMOSA_PMOSChannellength=None,  # number
                                  _NANDR_PMOSA_GateSpacing=None,  # None/number
                                  _NANDR_PMOSA_SDWidth=None,  # None/number
                                  _NANDR_PMOSA_XVT=None,  # 'XVT' ex)SLVT LVT RVT HVT
                                  _NANDR_PMOSA_PCCrit=None,  # None/True

                                  # Source_node_ViaM1M2
                                  _NANDR_PMOSA_Source_Via_TF=None,  # True/False

                                  # Drain_node_ViaM1M2
                                  _NANDR_PMOSA_Drain_Via_TF=None,  # True/False

                                  # POLY dummy setting
                                  _NANDR_PMOSA_PMOSDummy=None,  # TF
                                  # if _PMOSDummy == True
                                  _NANDR_PMOSA_PMOSDummy_length=None,  # None/Value
                                  _NANDR_PMOSA_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # PMOSB
                                  _NANDR_PMOSB_PMOSNumberofGate=None,  # number
                                  _NANDR_PMOSB_PMOSChannelWidth=None,  # number
                                  _NANDR_PMOSB_PMOSChannellength=None,  # number
                                  _NANDR_PMOSB_GateSpacing=None,  # None/number
                                  _NANDR_PMOSB_SDWidth=None,  # None/number
                                  _NANDR_PMOSB_XVT=None,  # 'XVT' ex)SLVT LVT RVT HVT
                                  _NANDR_PMOSB_PCCrit=None,  # None/True

                                  # Source_node_ViaM1M2
                                  _NANDR_PMOSB_Source_Via_TF=None,  # True/False

                                  # Drain_node_ViaM1M2
                                  _NANDR_PMOSB_Drain_Via_TF=None,  # True/False

                                  # POLY dummy setting
                                  _NANDR_PMOSB_PMOSDummy=None,  # TF
                                  # if _PMOSDummy == True
                                  _NANDR_PMOSB_PMOSDummy_length=None,  # None/Value
                                  _NANDR_PMOSB_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Nbody
                                  _NANDR_PMOSAB_Nbody_NumCont=None,  # Number
                                  _NANDR_PMOSAB_Nbody_Xlvtdown2Ndoby=None,  # Number/None(Minimum)

                                  # PMOS and NMOS Height
                                  _NANDR_PMOSXvt2NMOSXvt=None,  # number
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

        ######
        ## NAND wt input 'S' SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_PMOS_power_v2._PMOS_POWER._ParametersForDesignCalculation)
        _Calculation_Parameters = copy.deepcopy(E01_02_NAND_YJH._NAND._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_PMOSPOWER_PbodyContact_1_Length']  = _PMOSPOWER_PbodyContact_1_Length

        _Calculation_Parameters['_NMOSA_NMOSNumberofGate'] = _NANDS_NMOSA_NMOSNumberofGate
        _Calculation_Parameters['_NMOSA_NMOSChannelWidth'] = _NANDS_NMOSA_NMOSChannelWidth
        _Calculation_Parameters['_NMOSA_NMOSChannellength'] = _NANDS_NMOSA_NMOSChannellength
        _Calculation_Parameters['_NMOSA_GateSpacing'] = _NANDS_NMOSA_GateSpacing
        _Calculation_Parameters['_NMOSA_SDWidth'] = _NANDS_NMOSA_SDWidth
        _Calculation_Parameters['_NMOSA_XVT'] = _NANDS_NMOSA_XVT
        _Calculation_Parameters['_NMOSA_PCCrit'] = _NANDS_NMOSA_PCCrit
        _Calculation_Parameters['_NMOSA_Source_Via_TF'] = _NANDS_NMOSA_Source_Via_TF
        _Calculation_Parameters['_NMOSA_Drain_Via_TF'] = _NANDS_NMOSA_Drain_Via_TF
        _Calculation_Parameters['_NMOSA_NMOSDummy'] = _NANDS_NMOSA_NMOSDummy
        _Calculation_Parameters['_NMOSA_NMOSDummy_length'] = _NANDS_NMOSA_NMOSDummy_length
        _Calculation_Parameters['_NMOSA_NMOSDummy_placement'] = _NANDS_NMOSA_NMOSDummy_placement
        _Calculation_Parameters['_NMOSB_NMOSNumberofGate'] = _NANDS_NMOSB_NMOSNumberofGate
        _Calculation_Parameters['_NMOSB_NMOSChannelWidth'] = _NANDS_NMOSB_NMOSChannelWidth
        _Calculation_Parameters['_NMOSB_NMOSChannellength'] = _NANDS_NMOSB_NMOSChannellength
        _Calculation_Parameters['_NMOSB_GateSpacing'] = _NANDS_NMOSB_GateSpacing
        _Calculation_Parameters['_NMOSB_SDWidth'] = _NANDS_NMOSB_SDWidth
        _Calculation_Parameters['_NMOSB_XVT'] = _NANDS_NMOSB_XVT
        _Calculation_Parameters['_NMOSB_PCCrit'] = _NANDS_NMOSB_PCCrit
        _Calculation_Parameters['_NMOSB_Source_Via_TF'] = _NANDS_NMOSB_Source_Via_TF
        _Calculation_Parameters['_NMOSB_Drain_Via_TF'] = _NANDS_NMOSB_Drain_Via_TF
        _Calculation_Parameters['_NMOSB_NMOSDummy'] = _NANDS_NMOSB_NMOSDummy
        _Calculation_Parameters['_NMOSB_NMOSDummy_length'] = _NANDS_NMOSB_NMOSDummy_length
        _Calculation_Parameters['_NMOSB_NMOSDummy_placement'] = _NANDS_NMOSB_NMOSDummy_placement
        _Calculation_Parameters['_NMOSAB_Pbody_NumCont'] = _NANDS_NMOSAB_Pbody_NumCont
        _Calculation_Parameters['_NMOSAB_Pbody_XlvtTop2Pdoby'] = _NANDS_NMOSAB_Pbody_XlvtTop2Pdoby

        _Calculation_Parameters['_PMOSA_PMOSNumberofGate'] = _NANDS_PMOSA_PMOSNumberofGate
        _Calculation_Parameters['_PMOSA_PMOSChannelWidth'] = _NANDS_PMOSA_PMOSChannelWidth
        _Calculation_Parameters['_PMOSA_PMOSChannellength'] = _NANDS_PMOSA_PMOSChannellength
        _Calculation_Parameters['_PMOSA_GateSpacing'] = _NANDS_PMOSA_GateSpacing
        _Calculation_Parameters['_PMOSA_SDWidth'] = _NANDS_PMOSA_SDWidth
        _Calculation_Parameters['_PMOSA_XVT'] = _NANDS_PMOSA_XVT
        _Calculation_Parameters['_PMOSA_PCCrit'] = _NANDS_PMOSA_PCCrit
        _Calculation_Parameters['_PMOSA_Source_Via_TF'] = False # default
        _Calculation_Parameters['_PMOSA_Drain_Via_TF'] = _NANDS_PMOSA_Drain_Via_TF
        _Calculation_Parameters['_PMOSA_PMOSDummy'] = _NANDS_PMOSA_PMOSDummy
        _Calculation_Parameters['_PMOSA_PMOSDummy_length'] = _NANDS_PMOSA_PMOSDummy_length
        _Calculation_Parameters['_PMOSA_PMOSDummy_placement'] = _NANDS_PMOSA_PMOSDummy_placement
        _Calculation_Parameters['_PMOSB_PMOSNumberofGate'] = _NANDS_PMOSB_PMOSNumberofGate
        _Calculation_Parameters['_PMOSB_PMOSChannelWidth'] = _NANDS_PMOSB_PMOSChannelWidth
        _Calculation_Parameters['_PMOSB_PMOSChannellength'] = _NANDS_PMOSB_PMOSChannellength
        _Calculation_Parameters['_PMOSB_GateSpacing'] = _NANDS_PMOSB_GateSpacing
        _Calculation_Parameters['_PMOSB_SDWidth'] = _NANDS_PMOSB_SDWidth
        _Calculation_Parameters['_PMOSB_XVT'] = _NANDS_PMOSB_XVT
        _Calculation_Parameters['_PMOSB_PCCrit'] = _NANDS_PMOSB_PCCrit
        _Calculation_Parameters['_PMOSB_Source_Via_TF'] = False # default
        _Calculation_Parameters['_PMOSB_Drain_Via_TF'] = _NANDS_PMOSB_Drain_Via_TF
        _Calculation_Parameters['_PMOSB_PMOSDummy'] = _NANDS_PMOSB_PMOSDummy
        _Calculation_Parameters['_PMOSB_PMOSDummy_length'] = _NANDS_PMOSB_PMOSDummy_length
        _Calculation_Parameters['_PMOSB_PMOSDummy_placement'] = _NANDS_PMOSB_PMOSDummy_placement
        _Calculation_Parameters['_PMOSAB_Nbody_NumCont'] = _NANDS_PMOSAB_Nbody_NumCont
        _Calculation_Parameters['_PMOSAB_Nbody_Xlvtdown2Ndoby'] = _NANDS_PMOSAB_Nbody_Xlvtdown2Ndoby
        _Calculation_Parameters['_PMOSXvt2NMOSXvt'] = _NANDS_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_NANDS'] = self._SrefElementDeclaration(
            _DesignObj=E01_02_NAND_YJH._NAND(_DesignParameter=None,
                                                                  _Name='{}:SRF_NANDS'.format(_Name)))[0]
        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_NANDS']['_Reflect'] = [1, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NANDS']['_Angle'] = 180

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NANDS']['_DesignObj']._CalculateDesignParameter(**_Calculation_Parameters)

        ## initialize Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NANDS']['_XYCoordinates'] = [[0, 0]]


        ######
        ## NAND wt input 'R' SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_PMOS_power_v2._PMOS_POWER._ParametersForDesignCalculation)
        _Calculation_Parameters = copy.deepcopy(E01_02_NAND_YJH._NAND._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_PMOSPOWER_PbodyContact_1_Length']  = _PMOSPOWER_PbodyContact_1_Length

        _Calculation_Parameters['_NMOSA_NMOSNumberofGate'] = _NANDR_NMOSA_NMOSNumberofGate
        _Calculation_Parameters['_NMOSA_NMOSChannelWidth'] = _NANDR_NMOSA_NMOSChannelWidth
        _Calculation_Parameters['_NMOSA_NMOSChannellength'] = _NANDR_NMOSA_NMOSChannellength
        _Calculation_Parameters['_NMOSA_GateSpacing'] = _NANDR_NMOSA_GateSpacing
        _Calculation_Parameters['_NMOSA_SDWidth'] = _NANDR_NMOSA_SDWidth
        _Calculation_Parameters['_NMOSA_XVT'] = _NANDR_NMOSA_XVT
        _Calculation_Parameters['_NMOSA_PCCrit'] = _NANDR_NMOSA_PCCrit
        _Calculation_Parameters['_NMOSA_Source_Via_TF'] = _NANDR_NMOSA_Source_Via_TF
        _Calculation_Parameters['_NMOSA_Drain_Via_TF'] = _NANDR_NMOSA_Drain_Via_TF
        _Calculation_Parameters['_NMOSA_NMOSDummy'] = _NANDR_NMOSA_NMOSDummy
        _Calculation_Parameters['_NMOSA_NMOSDummy_length'] = _NANDR_NMOSA_NMOSDummy_length
        _Calculation_Parameters['_NMOSA_NMOSDummy_placement'] = _NANDR_NMOSA_NMOSDummy_placement
        _Calculation_Parameters['_NMOSB_NMOSNumberofGate'] = _NANDR_NMOSB_NMOSNumberofGate
        _Calculation_Parameters['_NMOSB_NMOSChannelWidth'] = _NANDR_NMOSB_NMOSChannelWidth
        _Calculation_Parameters['_NMOSB_NMOSChannellength'] = _NANDR_NMOSB_NMOSChannellength
        _Calculation_Parameters['_NMOSB_GateSpacing'] = _NANDR_NMOSB_GateSpacing
        _Calculation_Parameters['_NMOSB_SDWidth'] = _NANDR_NMOSB_SDWidth
        _Calculation_Parameters['_NMOSB_XVT'] = _NANDR_NMOSB_XVT
        _Calculation_Parameters['_NMOSB_PCCrit'] = _NANDR_NMOSB_PCCrit
        _Calculation_Parameters['_NMOSB_Source_Via_TF'] = _NANDR_NMOSB_Source_Via_TF
        _Calculation_Parameters['_NMOSB_Drain_Via_TF'] = _NANDR_NMOSB_Drain_Via_TF
        _Calculation_Parameters['_NMOSB_NMOSDummy'] = _NANDR_NMOSB_NMOSDummy
        _Calculation_Parameters['_NMOSB_NMOSDummy_length'] = _NANDR_NMOSB_NMOSDummy_length
        _Calculation_Parameters['_NMOSB_NMOSDummy_placement'] = _NANDR_NMOSB_NMOSDummy_placement
        _Calculation_Parameters['_NMOSAB_Pbody_NumCont'] = _NANDR_NMOSAB_Pbody_NumCont
        _Calculation_Parameters['_NMOSAB_Pbody_XlvtTop2Pdoby'] = _NANDR_NMOSAB_Pbody_XlvtTop2Pdoby

        _Calculation_Parameters['_PMOSA_PMOSNumberofGate'] = _NANDR_PMOSA_PMOSNumberofGate
        _Calculation_Parameters['_PMOSA_PMOSChannelWidth'] = _NANDR_PMOSA_PMOSChannelWidth
        _Calculation_Parameters['_PMOSA_PMOSChannellength'] = _NANDR_PMOSA_PMOSChannellength
        _Calculation_Parameters['_PMOSA_GateSpacing'] = _NANDR_PMOSA_GateSpacing
        _Calculation_Parameters['_PMOSA_SDWidth'] = _NANDR_PMOSA_SDWidth
        _Calculation_Parameters['_PMOSA_XVT'] = _NANDR_PMOSA_XVT
        _Calculation_Parameters['_PMOSA_PCCrit'] = _NANDR_PMOSA_PCCrit
        _Calculation_Parameters['_PMOSA_Source_Via_TF'] = False # default
        _Calculation_Parameters['_PMOSA_Drain_Via_TF'] = _NANDR_PMOSA_Drain_Via_TF
        _Calculation_Parameters['_PMOSA_PMOSDummy'] = _NANDR_PMOSA_PMOSDummy
        _Calculation_Parameters['_PMOSA_PMOSDummy_length'] = _NANDR_PMOSA_PMOSDummy_length
        _Calculation_Parameters['_PMOSA_PMOSDummy_placement'] = _NANDR_PMOSA_PMOSDummy_placement
        _Calculation_Parameters['_PMOSB_PMOSNumberofGate'] = _NANDR_PMOSB_PMOSNumberofGate
        _Calculation_Parameters['_PMOSB_PMOSChannelWidth'] = _NANDR_PMOSB_PMOSChannelWidth
        _Calculation_Parameters['_PMOSB_PMOSChannellength'] = _NANDR_PMOSB_PMOSChannellength
        _Calculation_Parameters['_PMOSB_GateSpacing'] = _NANDR_PMOSB_GateSpacing
        _Calculation_Parameters['_PMOSB_SDWidth'] = _NANDR_PMOSB_SDWidth
        _Calculation_Parameters['_PMOSB_XVT'] = _NANDR_PMOSB_XVT
        _Calculation_Parameters['_PMOSB_PCCrit'] = _NANDR_PMOSB_PCCrit
        _Calculation_Parameters['_PMOSB_Source_Via_TF'] = False # default
        _Calculation_Parameters['_PMOSB_Drain_Via_TF'] = _NANDR_PMOSB_Drain_Via_TF
        _Calculation_Parameters['_PMOSB_PMOSDummy'] = _NANDR_PMOSB_PMOSDummy
        _Calculation_Parameters['_PMOSB_PMOSDummy_length'] = _NANDR_PMOSB_PMOSDummy_length
        _Calculation_Parameters['_PMOSB_PMOSDummy_placement'] = _NANDR_PMOSB_PMOSDummy_placement
        _Calculation_Parameters['_PMOSAB_Nbody_NumCont'] = _NANDR_PMOSAB_Nbody_NumCont
        _Calculation_Parameters['_PMOSAB_Nbody_Xlvtdown2Ndoby'] = _NANDR_PMOSAB_Nbody_Xlvtdown2Ndoby
        _Calculation_Parameters['_PMOSXvt2NMOSXvt'] = _NANDR_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_NANDR'] = self._SrefElementDeclaration(
            _DesignObj=E01_02_NAND_YJH._NAND(_DesignParameter=None,
                                                                  _Name='{}:SRF_NANDR'.format(_Name)))[0]
        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_NANDR']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NANDR']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NANDR']['_DesignObj']._CalculateDesignParameter(**_Calculation_Parameters)

        ## initialize Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NANDR']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_NANDS', 'SRF_Pullup', 'SRF_PMOSA', 'BND_PODummyLayer')
        target_coord = tmp1[0][0][0][0][0]['_XY_up_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_NANDR', 'SRF_Pullup', 'SRF_PMOSA', 'BND_PODummyLayer')
        approaching_coord = tmp2[0][0][0][0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_NANDR')
        Scoord = tmp3[0][0]['_XY_origin']

        SpaceBtwNANDSnRPOdummy = 120
        Scoord[0] = Scoord[0] + max(SpaceBtwNANDSnRPOdummy, _DRCobj._PolygateMinSpace)
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['SRF_NANDR']['_XYCoordinates'] = tmpXY

        # pre-defined routing point(coordY)
        tmpSy1 = self.get_param_KJH4('SRF_NANDS', 'SRF_Pullup', 'SRF_PMOSA_Gate_ViaM0M1','SRF_ViaM0M1', 'BND_Met1Layer')
        tmpSy2 = self.get_param_KJH4('SRF_NANDS', 'SRF_Pulldown', 'SRF_NMOSA_Gate_ViaM0M1','SRF_ViaM0M1', 'BND_Met1Layer')
        tmpRy1 = self.get_param_KJH4('SRF_NANDR', 'SRF_Pullup', 'SRF_PMOSA_Gate_ViaM0M1','SRF_ViaM0M1', 'BND_Met1Layer')
        tmpRy2 = self.get_param_KJH4('SRF_NANDR', 'SRF_Pulldown', 'SRF_NMOSA_Gate_ViaM0M1','SRF_ViaM0M1', 'BND_Met1Layer')
        upperroutepnty = min(int(tmpSy1[0][0][0][0][0][0]['_XY_down'][1]*0.666 + tmpSy2[0][0][0][0][0][0]['_XY_up'][1]*0.333),\
                             int(tmpSy1[0][0][0][0][0][0]['_XY_down'][1]*0.666 + tmpSy2[0][0][0][0][0][0]['_XY_up'][1]*0.333))
        lowerroutepnty = max(int(tmpRy1[0][0][0][0][0][0]['_XY_down'][1]*0.333 + tmpRy2[0][0][0][0][0][0]['_XY_up'][1]*0.666), \
                             int(tmpRy1[0][0][0][0][0][0]['_XY_down'][1]*0.333 + tmpRy2[0][0][0][0][0][0]['_XY_up'][1]*0.666))


        ###### NAND S gate <-> R drain Routing
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_SGateRDrain_ViaM1M2'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_SGateRDrain_ViaM1M2'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_SGateRDrain_ViaM1M2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_SGateRDrain_ViaM1M2']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_SGateRDrain_ViaM1M2']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_SGateRDrain_ViaM1M2']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmpx = self.get_param_KJH4('SRF_NANDS', 'BND_InputA_Vtc_M1')
        target_coord = [tmpx[0][0][0]['_XY_left'][0], upperroutepnty]
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_SGateRDrain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_SGateRDrain_ViaM1M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_SGateRDrain_ViaM1M2']['_XYCoordinates'] = tmpXY


        ####### NAND S gate <-> R drain Routing/ M2 Metal Bnd element gen.
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_SGateRDrain_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_SGateRDrain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        self._DesignParameter['BND_SGateRDrain_M2']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp2_1 = self.get_param_KJH4('SRF_SGateRDrain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        tmp2_2 = self.get_param_KJH4('SRF_NANDR', 'BND_Out_Vtc_M2')
        self._DesignParameter['BND_SGateRDrain_M2']['_XWidth'] = abs(tmp2_1[0][0][0][0]['_XY_left'][0] - tmp2_2[0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_SGateRDrain_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_SGateRDrain_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_SGateRDrain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        target_coord = [tmp1[0][0][0][0]['_XY_left'][0], upperroutepnty]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_SGateRDrain_M2')
        approaching_coord = tmp2[0][0]['_XY_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_SGateRDrain_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_SGateRDrain_M2']['_XYCoordinates'] = tmpXY


        ###### NAND R gate <-> S drain Routing
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_RGateSDrain_ViaM1M2'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_RGateSDrain_ViaM1M2'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_RGateSDrain_ViaM1M2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_RGateSDrain_ViaM1M2']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_RGateSDrain_ViaM1M2']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_RGateSDrain_ViaM1M2']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmpx = self.get_param_KJH4('SRF_NANDR', 'BND_InputA_Vtc_M1')
        target_coord = [tmpx[0][0][0]['_XY_left'][0], lowerroutepnty]
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_RGateSDrain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_RGateSDrain_ViaM1M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_RGateSDrain_ViaM1M2']['_XYCoordinates'] = tmpXY


        ####### NAND S gate <-> R drain Routing/ M2 Metal Bnd element gen.
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_RGateSDrain_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_RGateSDrain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        self._DesignParameter['BND_RGateSDrain_M2']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp2_1 = self.get_param_KJH4('SRF_RGateSDrain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        tmp2_2 = self.get_param_KJH4('SRF_NANDS', 'BND_Out_Vtc_M2')
        self._DesignParameter['BND_RGateSDrain_M2']['_XWidth'] = abs(tmp2_1[0][0][0][0]['_XY_right'][0] - tmp2_2[0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_RGateSDrain_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_RGateSDrain_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_RGateSDrain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        target_coord = [tmp1[0][0][0][0]['_XY_right'][0], lowerroutepnty]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_RGateSDrain_M2')
        approaching_coord = tmp2[0][0]['_XY_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_RGateSDrain_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_RGateSDrain_M2']['_XYCoordinates'] = tmpXY


        ##### Input S <-> NAND S Routing
        ## Sref generation: Input S ViaM1M3
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_InputS_ViaM1M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_InputS_ViaM1M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_InputS_ViaM1M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_InputS_ViaM1M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_InputS_ViaM1M3']['_DesignObj']._CalculateDesignParameterYmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_InputS_ViaM1M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmpx = self.get_param_KJH4('SRF_NANDS', 'BND_InputB_Vtc_M1')
        target_coord = [tmpx[0][0][0]['_XY_left'][0], lowerroutepnty]
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_InputS_ViaM1M3', 'SRF_ViaM1M2', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_InputS_ViaM1M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_InputS_ViaM1M3']['_XYCoordinates'] = tmpXY


        ########## Input S <-> NAND S routing boundary element gen.
           ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_InputS_Hrz_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        InputS_Hrz_M3_pathwidth = 50
        self._DesignParameter['BND_InputS_Hrz_M3']['_YWidth'] = InputS_Hrz_M3_pathwidth

                ## Define Boundary_element _XWidth
        tmp2_1 = self.get_param_KJH4('SRF_InputS_ViaM1M3', 'SRF_ViaM1M2', 'BND_Met1Layer')
        tmp2_2 = self.get_param_KJH4('SRF_NANDS', 'BND_InputB_Vtc_M1')
        self._DesignParameter['BND_InputS_Hrz_M3']['_XWidth'] = abs(tmp2_1[0][0][0][0]['_XY_left'][0] - tmp2_2[0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_InputS_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_InputS_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmpx = self.get_param_KJH4('SRF_NANDS', 'BND_InputB_Vtc_M1')
        target_coord = [tmpx[0][0][0]['_XY_right'][0], lowerroutepnty]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_InputS_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_InputS_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_InputS_Hrz_M3']['_XYCoordinates'] = tmpXY


        ##### Input R <-> NAND R Routing
        ## Sref generation: Input R ViaM1M3
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_InputR_ViaM1M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_InputR_ViaM1M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_InputR_ViaM1M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_InputR_ViaM1M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_InputR_ViaM1M3']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_InputR_ViaM1M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmpx = self.get_param_KJH4('SRF_NANDR', 'BND_InputB_Vtc_M1')
        target_coord = [tmpx[0][0][0]['_XY_right'][0], upperroutepnty]
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_InputR_ViaM1M3', 'SRF_ViaM1M2', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_InputR_ViaM1M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_InputR_ViaM1M3']['_XYCoordinates'] = tmpXY


        ########## Input R <-> NAND R routing boundary element gen.
           ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_InputR_Hrz_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        InputR_Hrz_M3_pathwidth = 50
        self._DesignParameter['BND_InputR_Hrz_M3']['_YWidth'] = InputR_Hrz_M3_pathwidth

                ## Define Boundary_element _XWidth
        tmp2_1 = self.get_param_KJH4('SRF_InputS_ViaM1M3', 'SRF_ViaM1M2', 'BND_Met1Layer')
        tmp2_2 = self.get_param_KJH4('SRF_NANDR', 'BND_InputB_Vtc_M1')
        self._DesignParameter['BND_InputR_Hrz_M3']['_XWidth'] = abs(tmp2_1[0][0][0][0]['_XY_left'][0] - tmp2_2[0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_InputR_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_InputR_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmpx = self.get_param_KJH4('SRF_NANDR', 'BND_InputB_Vtc_M1')
        target_coord = [tmpx[0][0][0]['_XY_right'][0], upperroutepnty]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_InputR_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_InputR_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_InputR_Hrz_M3']['_XYCoordinates'] = tmpXY


        ##### OUTPUT Q <-> NAND S Routing
        ## Sref generation: Output S ViaM2M3
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_OutputQ_ViaM2M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_OutputQ_ViaM2M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_OutputQ_ViaM2M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_OutputQ_ViaM2M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_OutputQ_ViaM2M3']['_DesignObj']._CalculateDesignParameterYmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_OutputQ_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp = self.get_param_KJH4('SRF_NANDS', 'SRF_Pullup', 'BND_PMOSA_Drain_Hrz_M2')
        target_coord = tmp[0][0][0][0]['_XY_left']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_OutputQ_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_OutputQ_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_OutputQ_ViaM2M3']['_XYCoordinates'] = tmpXY


        # ########## OutputQ <-> NAND S routing boundary element gen.
        #    ## Boundary_element Generation
        #         ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        # self._DesignParameter['BND_OutputQ_Hrz_M3'] = self._BoundaryElementDeclaration(
        # _Layer=DesignParameters._LayerMapping['METAL3'][0],
        # _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        # _XWidth=None,
        # _YWidth=None,
        # _XYCoordinates=[],
        # )
        #         ## Define Boundary_element _YWidth
        # OutputQ_Hrz_M3_pathwidth = 50
        # self._DesignParameter['BND_OutputQ_Hrz_M3']['_YWidth'] = OutputQ_Hrz_M3_pathwidth
        #
        #         ## Define Boundary_element _XWidth
        # tmp2_1 = self.get_param_KJH4('SRF_OutputQ_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met2Layer')
        # tmp2_2 = self.get_param_KJH4('SRF_NANDR', 'BND_PMOSAB_NellExten')
        # self._DesignParameter['BND_OutputQ_Hrz_M3']['_XWidth'] = abs(tmp2_1[0][0][0][0]['_XY_left'][0] - tmp2_2[0][0][0]['_XY_right'][0])
        #
        #         ## Define Boundary_element _XYCoordinates
        # self._DesignParameter['BND_OutputQ_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
        #
        #             ## Calculate Sref XYcoord
        # tmpXY = []
        #                 ## initialized Sref coordinate
        # self._DesignParameter['BND_OutputQ_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
        #                 ## Calculate
        #                     ## Target_coord: _XY_type1
        # tmpx = self.get_param_KJH4('SRF_OutputQ_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met2Layer')
        # target_coord = tmpx[0][0][0][0]['_XY_left']
        #                     ## Approaching_coord: _XY_type2
        # tmp2 = self.get_param_KJH4('BND_OutputQ_Hrz_M3')
        # approaching_coord = tmp2[0][0]['_XY_left']
        #                     ## Sref coord
        # tmp3 = self.get_param_KJH4('BND_OutputQ_Hrz_M3')
        # Scoord = tmp3[0][0]['_XY_origin']
        #                     ## Cal
        # New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        # tmpXY.append(New_Scoord)
        #                     ## Define coordinates
        # self._DesignParameter['BND_OutputQ_Hrz_M3']['_XYCoordinates'] = tmpXY


        ##### OUTPUT QB <-> NAND R Routing
        ## Sref generation: Output S ViaM2M3
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_OutputQB_ViaM2M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_OutputQB_ViaM2M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_OutputQB_ViaM2M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_OutputQB_ViaM2M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_OutputQB_ViaM2M3']['_DesignObj']._CalculateDesignParameterYmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_OutputQB_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp = self.get_param_KJH4('SRF_NANDR', 'SRF_Pulldown', 'BND_NMOSA_Drain_Hrz_M2')
        target_coord = tmp[0][0][0][0]['_XY_left']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_OutputQB_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_OutputQB_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_OutputQB_ViaM2M3']['_XYCoordinates'] = tmpXY


        # ########## OutputQB <-> NAND R routing boundary element gen.
        #    ## Boundary_element Generation
        #         ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        # self._DesignParameter['BND_OutputQB_Hrz_M3'] = self._BoundaryElementDeclaration(
        # _Layer=DesignParameters._LayerMapping['METAL3'][0],
        # _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        # _XWidth=None,
        # _YWidth=None,
        # _XYCoordinates=[],
        # )
        #         ## Define Boundary_element _YWidth
        # OutputQB_Hrz_M3_pathwidth = 50
        # self._DesignParameter['BND_OutputQB_Hrz_M3']['_YWidth'] = OutputQB_Hrz_M3_pathwidth
        #
        #         ## Define Boundary_element _XWidth
        # tmp2_1 = self.get_param_KJH4('SRF_OutputQB_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met2Layer')
        # tmp2_2 = self.get_param_KJH4('SRF_NANDR', 'BND_PMOSAB_NellExten')
        # self._DesignParameter['BND_OutputQB_Hrz_M3']['_XWidth'] = abs(tmp2_1[0][0][0][0]['_XY_left'][0] - tmp2_2[0][0][0]['_XY_right'][0])
        #
        #         ## Define Boundary_element _XYCoordinates
        # self._DesignParameter['BND_OutputQB_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
        #
        #             ## Calculate Sref XYcoord
        # tmpXY = []
        #                 ## initialized Sref coordinate
        # self._DesignParameter['BND_OutputQB_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
        #                 ## Calculate
        #                     ## Target_coord: _XY_type1
        # tmpx = self.get_param_KJH4('SRF_OutputQB_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met2Layer')
        # target_coord = tmpx[0][0][0][0]['_XY_left']
        #                     ## Approaching_coord: _XY_type2
        # tmp2 = self.get_param_KJH4('BND_OutputQB_Hrz_M3')
        # approaching_coord = tmp2[0][0]['_XY_left']
        #                     ## Sref coord
        # tmp3 = self.get_param_KJH4('BND_OutputQB_Hrz_M3')
        # Scoord = tmp3[0][0]['_XY_origin']
        #                     ## Cal
        # New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        # tmpXY.append(New_Scoord)
        #                     ## Define coordinates
        # self._DesignParameter['BND_OutputQB_Hrz_M3']['_XYCoordinates'] = tmpXY


        ##### NWell BND Element Declaration
          ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NWell_SRLatch'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['NWELL'][0],
        _Datatype=DesignParameters._LayerMapping['NWELL'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_NANDS', 'BND_PMOSAB_NellExten')
        self._DesignParameter['BND_NWell_SRLatch']['_YWidth'] = tmp1[0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH4('SRF_NANDR', 'BND_PMOSAB_NellExten')
        self._DesignParameter['BND_NWell_SRLatch']['_XWidth'] = abs(tmp1[0][0][0]['_XY_right'][0] - tmp2[0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NWell_SRLatch']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_NWell_SRLatch']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp2[0][0][0]['_XY_up_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NWell_SRLatch')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NWell_SRLatch')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_NWell_SRLatch']['_XYCoordinates'] = tmpXY


        ##### PMOS XVT BND Element Declaration
        if  (_NANDS_PMOSA_XVT == _NANDS_PMOSB_XVT and _NANDR_PMOSA_XVT == _NANDR_PMOSA_XVT and _NANDS_PMOSA_XVT== _NANDR_PMOSA_XVT) != 1:
            raise Exception(f"PMOS XVT Layers are not same")
          ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_{}_PMOS_SRLatch'.format(_NANDS_PMOSA_XVT)] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping[_NANDS_PMOSA_XVT][0],
        _Datatype=DesignParameters._LayerMapping[_NANDS_PMOSA_XVT][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp2_1 = self.get_param_KJH4('SRF_NANDS', 'SRF_Pullup', 'SRF_PMOSB','BND_{}Layer'.format(_NANDS_PMOSB_XVT))
        self._DesignParameter['BND_{}_PMOS_SRLatch'.format(_NANDS_PMOSA_XVT)]['_YWidth'] = tmp2_1[0][0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp2_2 = self.get_param_KJH4('SRF_NANDR', 'SRF_Pullup', 'SRF_PMOSB','BND_{}Layer'.format(_NANDR_PMOSB_XVT))
        self._DesignParameter['BND_{}_PMOS_SRLatch'.format(_NANDS_PMOSA_XVT)]['_XWidth'] = \
            abs(tmp2_1[0][0][0][0][0]['_XY_right'][0] - tmp2_2[0][0][0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_{}_PMOS_SRLatch'.format(_NANDS_PMOSA_XVT)]['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_{}_PMOS_SRLatch'.format(_NANDS_PMOSA_XVT)]['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp2_2[0][0][0][0][0]['_XY_up_right']
                            ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_{}_PMOS_SRLatch'.format(_NANDS_PMOSA_XVT))
        approaching_coord = tmp3[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_{}_PMOS_SRLatch'.format(_NANDS_PMOSA_XVT))
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_{}_PMOS_SRLatch'.format(_NANDS_PMOSA_XVT)]['_XYCoordinates'] = tmpXY


        ##### NMOS XVT BND Element Declaration
        if  (_NANDS_NMOSA_XVT == _NANDS_NMOSB_XVT and _NANDR_NMOSA_XVT == _NANDR_NMOSA_XVT and _NANDS_NMOSA_XVT== _NANDR_NMOSA_XVT) != 1:
            raise Exception(f"NMOS XVT Layers are not same")
          ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_{}_NMOS_SRLatch'.format(_NANDS_NMOSA_XVT)] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping[_NANDS_NMOSA_XVT][0],
        _Datatype=DesignParameters._LayerMapping[_NANDS_NMOSA_XVT][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp2_1 = self.get_param_KJH4('SRF_NANDS', 'SRF_Pulldown', 'SRF_NMOSB','BND_{}Layer'.format(_NANDS_NMOSA_XVT))
        self._DesignParameter['BND_{}_NMOS_SRLatch'.format(_NANDS_NMOSA_XVT)]['_YWidth'] = tmp2_1[0][0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp2_2 = self.get_param_KJH4('SRF_NANDR', 'SRF_Pulldown', 'SRF_NMOSB','BND_{}Layer'.format(_NANDR_NMOSA_XVT))
        self._DesignParameter['BND_{}_NMOS_SRLatch'.format(_NANDS_NMOSA_XVT)]['_XWidth'] = \
            abs(tmp2_1[0][0][0][0][0]['_XY_right'][0] - tmp2_2[0][0][0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_{}_NMOS_SRLatch'.format(_NANDS_NMOSA_XVT)]['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_{}_NMOS_SRLatch'.format(_NANDS_NMOSA_XVT)]['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp2_2[0][0][0][0][0]['_XY_up_right']
                            ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_{}_NMOS_SRLatch'.format(_NANDS_NMOSA_XVT))
        approaching_coord = tmp3[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_{}_NMOS_SRLatch'.format(_NANDS_NMOSA_XVT))
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_{}_NMOS_SRLatch'.format(_NANDS_NMOSA_XVT)]['_XYCoordinates'] = tmpXY


        ##### PMOS BP BND Element Declaration
          ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PPLayer_PMOS_SRLatch'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['PIMP'][0],
        _Datatype=DesignParameters._LayerMapping['PIMP'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp2_1 = self.get_param_KJH4('SRF_NANDS', 'SRF_Pullup', 'SRF_PMOSB','BND_PPLayer')
        self._DesignParameter['BND_PPLayer_PMOS_SRLatch']['_YWidth'] = tmp2_1[0][0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp2_2 = self.get_param_KJH4('SRF_NANDR', 'SRF_Pullup', 'SRF_PMOSB','BND_PPLayer')
        self._DesignParameter['BND_PPLayer_PMOS_SRLatch']['_XWidth'] = abs(tmp2_2[0][0][0][0][0]['_XY_right'][0] - tmp2_1[0][0][0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PPLayer_PMOS_SRLatch']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_PPLayer_PMOS_SRLatch']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp2_2[0][0][0][0][0]['_XY_up_right']
                            ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_PPLayer_PMOS_SRLatch')
        approaching_coord = tmp3[0][0]['_XY_up_right']
                            ## Sref coord
        tmp4 = self.get_param_KJH4('BND_PPLayer_PMOS_SRLatch')
        Scoord = tmp4[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_PPLayer_PMOS_SRLatch']['_XYCoordinates'] = tmpXY


        ##### NMOS Pbody BP Extension BND Element Declaration
          ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PPLayer_NMOS_PBody_SRLatch'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['PIMP'][0],
        _Datatype=DesignParameters._LayerMapping['PIMP'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp2_1 = self.get_param_KJH4('SRF_NANDS', 'SRF_Pbody','SRF_PbodyContactPhyLen','BND_PPLayer')
        self._DesignParameter['BND_PPLayer_NMOS_PBody_SRLatch']['_YWidth'] = tmp2_1[0][0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp2_2 = self.get_param_KJH4('SRF_NANDR', 'SRF_Pbody','SRF_PbodyContactPhyLen','BND_PPLayer')
        self._DesignParameter['BND_PPLayer_NMOS_PBody_SRLatch']['_XWidth'] = abs(tmp2_2[0][0][0][0][0]['_XY_right'][0] - tmp2_1[0][0][0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PPLayer_NMOS_PBody_SRLatch']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_PPLayer_NMOS_PBody_SRLatch']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp2_2[0][0][0][0][0]['_XY_up_right']
                            ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_PPLayer_NMOS_PBody_SRLatch')
        approaching_coord = tmp3[0][0]['_XY_up_right']
                            ## Sref coord
        tmp4 = self.get_param_KJH4('BND_PPLayer_NMOS_PBody_SRLatch')
        Scoord = tmp4[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_PPLayer_NMOS_PBody_SRLatch']['_XYCoordinates'] = tmpXY


        ##### Pbody M1 Extension BND Element Declaration
          ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_M1_NMOS_PBody_SRLatch'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp2_1 = self.get_param_KJH4('SRF_NANDS', 'SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_M1_NMOS_PBody_SRLatch']['_YWidth'] = tmp2_1[0][0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp2_2 = self.get_param_KJH4('SRF_NANDR', 'SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_M1_NMOS_PBody_SRLatch']['_XWidth'] = abs(tmp2_2[0][0][0][0][0]['_XY_right'][0] - tmp2_1[0][0][0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_M1_NMOS_PBody_SRLatch']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_M1_NMOS_PBody_SRLatch']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp2_2[0][0][0][0][0]['_XY_up_right']
                            ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_M1_NMOS_PBody_SRLatch')
        approaching_coord = tmp3[0][0]['_XY_up_right']
                            ## Sref coord
        tmp4 = self.get_param_KJH4('BND_M1_NMOS_PBody_SRLatch')
        Scoord = tmp4[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_M1_NMOS_PBody_SRLatch']['_XYCoordinates'] = tmpXY


        ##### Nbody M1 Extension BND Element Declaration
          ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_M1_PMOS_NBody_SRLatch'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp2_1 = self.get_param_KJH4('SRF_NANDS', 'SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_M1_PMOS_NBody_SRLatch']['_YWidth'] = tmp2_1[0][0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp2_2 = self.get_param_KJH4('SRF_NANDR', 'SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_M1_PMOS_NBody_SRLatch']['_XWidth'] = abs(tmp2_2[0][0][0][0][0]['_XY_right'][0] - tmp2_1[0][0][0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_M1_PMOS_NBody_SRLatch']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_M1_PMOS_NBody_SRLatch']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp2_2[0][0][0][0][0]['_XY_up_right']
                            ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_M1_PMOS_NBody_SRLatch')
        approaching_coord = tmp3[0][0]['_XY_up_right']
                            ## Sref coord
        tmp4 = self.get_param_KJH4('BND_M1_PMOS_NBody_SRLatch')
        Scoord = tmp4[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_M1_PMOS_NBody_SRLatch']['_XYCoordinates'] = tmpXY


        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')


############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    Start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_YJH
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ADC_E01_ComparatorWtLatch_YJH_v1'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'E01_01_SRLatch_v0'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        ##########
        ## NANDS Design parameters
        # NMOSA
        _NANDS_NMOSA_NMOSNumberofGate=2,  # number
        _NANDS_NMOSA_NMOSChannelWidth=400,  # number
        _NANDS_NMOSA_NMOSChannellength=30,  # number
        _NANDS_NMOSA_GateSpacing=None,  # None/number
        _NANDS_NMOSA_SDWidth=None,  # None/number
        _NANDS_NMOSA_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _NANDS_NMOSA_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _NANDS_NMOSA_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _NANDS_NMOSA_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _NANDS_NMOSA_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _NANDS_NMOSA_NMOSDummy_length=None,  # None/Value
        _NANDS_NMOSA_NMOSDummy_placement='Up',  # None/'Up'/'Dn'/

        # NMOSB
        _NANDS_NMOSB_NMOSNumberofGate=2,  # number
        _NANDS_NMOSB_NMOSChannelWidth=400,  # number
        _NANDS_NMOSB_NMOSChannellength=30,  # number
        _NANDS_NMOSB_GateSpacing=None,  # None/number
        _NANDS_NMOSB_SDWidth=None,  # None/number
        _NANDS_NMOSB_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _NANDS_NMOSB_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _NANDS_NMOSB_Source_Via_TF=False,  # True/False

        # Drain_node_ViaM1M2
        _NANDS_NMOSB_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _NANDS_NMOSB_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _NANDS_NMOSB_NMOSDummy_length=None,  # None/Value
        _NANDS_NMOSB_NMOSDummy_placement='Up',  # None/'Up'/'Dn'/

        # NMOSAB Pbody
        _NANDS_NMOSAB_Pbody_NumCont=3,  # Number
        _NANDS_NMOSAB_Pbody_XlvtTop2Pdoby=None,  # Number/None(Minimum)

        # PMOSA
        _NANDS_PMOSA_PMOSNumberofGate=1,  # number
        _NANDS_PMOSA_PMOSChannelWidth=800,  # number
        _NANDS_PMOSA_PMOSChannellength=30,  # number
        _NANDS_PMOSA_GateSpacing=None,  # None/number
        _NANDS_PMOSA_SDWidth=None,  # None/number
        _NANDS_PMOSA_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _NANDS_PMOSA_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _NANDS_PMOSA_Source_Via_TF=False,  # True/False

        # Drain_node_ViaM1M2
        _NANDS_PMOSA_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _NANDS_PMOSA_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _NANDS_PMOSA_PMOSDummy_length=None,  # None/Value
        _NANDS_PMOSA_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # PMOSB
        _NANDS_PMOSB_PMOSNumberofGate=1,  # number
        _NANDS_PMOSB_PMOSChannelWidth=800,  # number
        _NANDS_PMOSB_PMOSChannellength=30,  # number
        _NANDS_PMOSB_GateSpacing=None,  # None/number
        _NANDS_PMOSB_SDWidth=None,  # None/number
        _NANDS_PMOSB_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _NANDS_PMOSB_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _NANDS_PMOSB_Source_Via_TF=False,  # True/False

        # Drain_node_ViaM1M2
        _NANDS_PMOSB_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _NANDS_PMOSB_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _NANDS_PMOSB_PMOSDummy_length=None,  # None/Value
        _NANDS_PMOSB_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Nbody
        _NANDS_PMOSAB_Nbody_NumCont=2,  # Number
        _NANDS_PMOSAB_Nbody_Xlvtdown2Ndoby=None,  # Number/None(Minimum)

        # PMOS and NMOS Height
        _NANDS_PMOSXvt2NMOSXvt=1000,  # number

        ##########
        ## NANDR Design parameters
        # NMOSA
        _NANDR_NMOSA_NMOSNumberofGate=2,  # number
        _NANDR_NMOSA_NMOSChannelWidth=400,  # number
        _NANDR_NMOSA_NMOSChannellength=30,  # number
        _NANDR_NMOSA_GateSpacing=None,  # None/number
        _NANDR_NMOSA_SDWidth=None,  # None/number
        _NANDR_NMOSA_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _NANDR_NMOSA_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _NANDR_NMOSA_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _NANDR_NMOSA_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _NANDR_NMOSA_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _NANDR_NMOSA_NMOSDummy_length=None,  # None/Value
        _NANDR_NMOSA_NMOSDummy_placement='Up',  # None/'Up'/'Dn'/

        # NMOSB
        _NANDR_NMOSB_NMOSNumberofGate=2,  # number
        _NANDR_NMOSB_NMOSChannelWidth=400,  # number
        _NANDR_NMOSB_NMOSChannellength=30,  # number
        _NANDR_NMOSB_GateSpacing=None,  # None/number
        _NANDR_NMOSB_SDWidth=None,  # None/number
        _NANDR_NMOSB_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _NANDR_NMOSB_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _NANDR_NMOSB_Source_Via_TF=False,  # True/False

        # Drain_node_ViaM1M2
        _NANDR_NMOSB_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _NANDR_NMOSB_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _NANDR_NMOSB_NMOSDummy_length=None,  # None/Value
        _NANDR_NMOSB_NMOSDummy_placement='Up',  # None/'Up'/'Dn'/

        # NMOSAB Pbody
        _NANDR_NMOSAB_Pbody_NumCont=3,  # Number
        _NANDR_NMOSAB_Pbody_XlvtTop2Pdoby=None,  # Number/None(Minimum)

        # PMOSA
        _NANDR_PMOSA_PMOSNumberofGate=1,  # number
        _NANDR_PMOSA_PMOSChannelWidth=700,  # number
        _NANDR_PMOSA_PMOSChannellength=30,  # number
        _NANDR_PMOSA_GateSpacing=None,  # None/number
        _NANDR_PMOSA_SDWidth=None,  # None/number
        _NANDR_PMOSA_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _NANDR_PMOSA_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _NANDR_PMOSA_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _NANDR_PMOSA_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _NANDR_PMOSA_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _NANDR_PMOSA_PMOSDummy_length=None,  # None/Value
        _NANDR_PMOSA_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # PMOSB
        _NANDR_PMOSB_PMOSNumberofGate=1,  # number
        _NANDR_PMOSB_PMOSChannelWidth=700,  # number
        _NANDR_PMOSB_PMOSChannellength=30,  # number
        _NANDR_PMOSB_GateSpacing=None,  # None/number
        _NANDR_PMOSB_SDWidth=None,  # None/number
        _NANDR_PMOSB_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _NANDR_PMOSB_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _NANDR_PMOSB_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _NANDR_PMOSB_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _NANDR_PMOSB_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _NANDR_PMOSB_PMOSDummy_length=None,  # None/Value
        _NANDR_PMOSB_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Nbody
        _NANDR_PMOSAB_Nbody_NumCont=2,  # Number
        _NANDR_PMOSAB_Nbody_Xlvtdown2Ndoby=None,  # Number/None(Minimum)

        # PMOS and NMOS Height
        _NANDR_PMOSXvt2NMOSXvt=1000,  # number
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
    LayoutObj = _SRLatch(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
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
