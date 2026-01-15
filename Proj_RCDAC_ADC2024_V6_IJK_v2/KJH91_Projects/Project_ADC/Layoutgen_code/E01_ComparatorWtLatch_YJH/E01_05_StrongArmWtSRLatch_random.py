## Import Basic Modules
    ## Engine
#from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import StickDiagram
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import DesignParameters
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import DRC

    ## Library
import copy
import time

    ## KJH91 Basic Building Blocks
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import Slicer
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E01_ComparatorWtLatch_YJH import E01_03_AND_YJH_random
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E01_ComparatorWtLatch_YJH import E01_04_SRLatch_random
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E01_ComparatorWtLatch_YJH import E01_01_Buffer
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E01_ComparatorWtLatch_YJH import E01_00_Inverter

############################################################################################################################################################ Class_HEADER
class _StrongArmWtSRLatch(StickDiagram_KJH1._StickDiagram_KJH):

    # XYcoord as center coordination
    #_XYcoordAsCent = dict(_XYcoordAsCent=1)

    # Initially Defined design_parameter
    _ParametersForDesignCalculation = dict(
        ## StrongARM Latch
        _SALatch_CLKinputPMOSFinger1=None,  # 6
        _SALatch_CLKinputPMOSFinger2=None,  # 3
        _SALatch_PMOSFinger=None,  # 3
        _SALatch_PMOSChannelWidth=None,  # 500
        _SALatch_DATAinputNMOSFinger=None,  # 12
        _SALatch_NMOSFinger=None,  # 2
        _SALatch_CLKinputNMOSFinger=None,  # 8
        _SALatch_NMOSChannelWidth=None,  # 500
        _SALatch_CLKinputNMOSChannelWidth=None,  # 800
        _SALatch_ChannelLength=None,  # 30
        _SALatch_Dummy=True,
        _SALatch_XVT=None,
        _SALatch_GuardringWidth=None,
        _SALatch_Guardring=True,
        _SALatch_SlicerGuardringWidth=None,
        _SALatch_SlicerGuardring=None,
        _SALatch_NumSupplyCOY=None,
        _SALatch_NumSupplyCOX=None,
        _SALatch_SupplyMet1XWidth=None,
        _SALatch_SupplyMet1YWidth=None,
        _SALatch_VDD2VSSHeight=None,
        _SALatch_NumVIAPoly2Met1COX=None,
        _SALatch_NumVIAPoly2Met1COY=None,
        _SALatch_NumVIAMet12COX=None,
        _SALatch_NumVIAMet12COY=None,
        _SALatch_PowerLine=False,

        ## StrongARMLatch Output Buffer Sizing
        # Inverter1
        _SAOutBuf_Inv1_NMOS_ChannelWidth=None,  # Number
        _SAOutBuf_Inv1_NMOS_ChannelLength=None,  # Number
        _SAOutBuf_Inv1_NMOS_NumberofGate=None,  # Number
        _SAOutBuf_Inv1_NMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _SAOutBuf_Inv1_NMOS_POGate_Comb_length=None,  # None/Number

        _SAOutBuf_Inv1_PMOS_ChannelWidth=None,  # Number
        _SAOutBuf_Inv1_PMOS_ChannelLength=None,  # Number
        _SAOutBuf_Inv1_PMOS_NumberofGate=None,  # Number
        _SAOutBuf_Inv1_PMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _SAOutBuf_Inv1_PMOS_POGate_Comb_length=None,  # None/Number

        # Inverter2
        _SAOutBuf_Inv2_NMOS_ChannelWidth=None,  # Number
        _SAOutBuf_Inv2_NMOS_ChannelLength=None,  # Number
        _SAOutBuf_Inv2_NMOS_NumberofGate=None,  # Number
        _SAOutBuf_Inv2_NMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _SAOutBuf_Inv2_NMOS_POGate_Comb_length=None,  # None/Number

        _SAOutBuf_Inv2_PMOS_ChannelWidth=None,  # Number
        _SAOutBuf_Inv2_PMOS_ChannelLength=None,  # Number
        _SAOutBuf_Inv2_PMOS_NumberofGate=None,  # Number
        _SAOutBuf_Inv2_PMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _SAOutBuf_Inv2_PMOS_POGate_Comb_length=None,  # None/Number

        ## SR Latch Sizing
        _SRLatch_NAND_NMOS_ChannelWidth=None,  # Number
        _SRLatch_NAND_NMOS_ChannelLength=None,  # Number
        _SRLatch_NAND_NMOS_NumberofGate=None,  # Number
        _SRLatch_NAND_NMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _SRLatch_NAND_NMOS_POGate_Comb_length=None,  # None/Number

        _SRLatch_NAND_PMOS_ChannelWidth=None,  # Number
        _SRLatch_NAND_PMOS_ChannelLength=None,  # Number
        _SRLatch_NAND_PMOS_NumberofGate=None,  # Number
        _SRLatch_NAND_PMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _SRLatch_NAND_PMOS_POGate_Comb_length=None,  # None/Number

        # CLK Input Logic Gates
        _CLKSamp_Inv_NMOS_ChannelWidth=None,
        _CLKSamp_Inv_NMOS_ChannelLength=None,
        _CLKSamp_Inv_NMOS_NumberofGate=None,
        _CLKSamp_Inv_NMOS_XVT=None,
        _CLKSamp_Inv_NMOS_POGate_Comb_length=None,

        _CLKSamp_Inv_PMOS_ChannelWidth=None,
        _CLKSamp_Inv_PMOS_ChannelLength=None,
        _CLKSamp_Inv_PMOS_NumberofGate=None,
        _CLKSamp_Inv_PMOS_XVT=None,
        _CLKSamp_Inv_PMOS_POGate_Comb_length=None,

        _CLKSrc_Inv_NMOS_ChannelWidth=None,
        _CLKSrc_Inv_NMOS_ChannelLength=None,
        _CLKSrc_Inv_NMOS_NumberofGate=None,
        _CLKSrc_Inv_NMOS_XVT=None,
        _CLKSrc_Inv_NMOS_POGate_Comb_length=None,

        _CLKSrc_Inv_PMOS_ChannelWidth=None,
        _CLKSrc_Inv_PMOS_ChannelLength=None,
        _CLKSrc_Inv_PMOS_NumberofGate=None,
        _CLKSrc_Inv_PMOS_XVT=None,
        _CLKSrc_Inv_PMOS_POGate_Comb_length=None,

        ## CLKSrc & CLKSample AND Gate
        _AND_NAND_NMOS_ChannelWidth=None,
        _AND_NAND_NMOS_ChannelLength=None,
        _AND_NAND_NMOS_NumberofGate=None,
        _AND_NAND_NMOS_XVT=None,

        _AND_NAND_PMOS_ChannelWidth=None,
        _AND_NAND_PMOS_ChannelLength=None,
        _AND_NAND_PMOS_NumberofGate=None,
        _AND_NAND_PMOS_XVT=None,

        _AND_Inv_NMOS_ChannelWidth=None,
        _AND_Inv_NMOS_ChannelLength=None,
        _AND_Inv_NMOS_NumberofGate=None,
        _AND_Inv_NMOS_XVT=None,
        _AND_Inv_NMOS_POGate_Comb_length=None,

        _AND_Inv_PMOS_ChannelWidth=None,
        _AND_Inv_PMOS_ChannelLength=None,
        _AND_Inv_PMOS_NumberofGate=None,
        _AND_Inv_PMOS_XVT=None,
        _AND_Inv_PMOS_POGate_Comb_length=None,

        ## CLK Buffer
        # Inverter1
        _CLKBuf_Inv1_NMOS_ChannelWidth=None,  # Number
        _CLKBuf_Inv1_NMOS_ChannelLength=None,  # Number
        _CLKBuf_Inv1_NMOS_NumberofGate=None,  # Number
        _CLKBuf_Inv1_NMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _CLKBuf_Inv1_NMOS_POGate_Comb_length=None,  # None/Number

        _CLKBuf_Inv1_PMOS_ChannelWidth=None,  # Number
        _CLKBuf_Inv1_PMOS_ChannelLength=None,  # Number
        _CLKBuf_Inv1_PMOS_NumberofGate=None,  # Number
        _CLKBuf_Inv1_PMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _CLKBuf_Inv1_PMOS_POGate_Comb_length=None,  # None/Number

        # Inverter2
        _CLKBuf_Inv2_NMOS_ChannelWidth=None,  # Number
        _CLKBuf_Inv2_NMOS_ChannelLength=None,  # Number
        _CLKBuf_Inv2_NMOS_NumberofGate=None,  # Number
        _CLKBuf_Inv2_NMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _CLKBuf_Inv2_NMOS_POGate_Comb_length=None,  # None/Number

        _CLKBuf_Inv2_PMOS_ChannelWidth=None,  # Number
        _CLKBuf_Inv2_PMOS_ChannelLength=None,  # Number
        _CLKBuf_Inv2_PMOS_NumberofGate=None,  # Number
        _CLKBuf_Inv2_PMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _CLKBuf_Inv2_PMOS_POGate_Comb_length=None,  # None/Number

        # PowerRail Placement
        _BufSR_NMOS_Pbody_NumCont=None,
        _BufSR_NMOS_Pbody_XvtTop2Pbody=None,
        _BufSR_PMOS_Nbody_NumCont=None,
        _BufSR_PMOS_Nbody_Xvtdown2Nbody=None,
        _BufSR_PMOSXvt2NMOSXvt=None,

        _CLKInLogic_NMOS_Pbody_Xvtdown2Pbody=None,
        _CLKInLogic_PMOS_Nbody_NumCont=None,
        _CLKInLogic_PMOS_Nbody_Xvtdown2Nbody=None,
        _CLKInLogic_PMOSXvt2NMOSXvt=None,
    )

    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _Name=self._NameDeclaration(_Name=_Name),
                _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                _XYcoordAsCent=dict(_XYcoordAsCent=0),
            )

    ##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
    def _CalculateDesignParameter(self,
                                  ## StrongArm Latch
                                  _SALatch_CLKinputPMOSFinger1=None,  # 6
                                  _SALatch_CLKinputPMOSFinger2=None,  # 3
                                  _SALatch_PMOSFinger=None,  # 3
                                  _SALatch_PMOSChannelWidth=None,  # 500
                                  _SALatch_DATAinputNMOSFinger=None,  # 12
                                  _SALatch_NMOSFinger=None,  # 2
                                  _SALatch_CLKinputNMOSFinger=None,  # 8
                                  _SALatch_NMOSChannelWidth=None,  # 500
                                  _SALatch_CLKinputNMOSChannelWidth=None,  # 800
                                  _SALatch_ChannelLength=None,  # 30
                                  _SALatch_Dummy=True,
                                  _SALatch_XVT=None,
                                  _SALatch_GuardringWidth=None,
                                  _SALatch_Guardring=True,
                                  _SALatch_SlicerGuardringWidth=None,
                                  _SALatch_SlicerGuardring=None,
                                  _SALatch_NumSupplyCOY=None,
                                  _SALatch_NumSupplyCOX=None,
                                  _SALatch_SupplyMet1XWidth=None,
                                  _SALatch_SupplyMet1YWidth=None,
                                  _SALatch_VDD2VSSHeight=None,
                                  _SALatch_NumVIAPoly2Met1COX=None,
                                  _SALatch_NumVIAPoly2Met1COY=None,
                                  _SALatch_NumVIAMet12COX=None,
                                  _SALatch_NumVIAMet12COY=None,
                                  _SALatch_PowerLine=False,

                                  ## StrongARMLatch Output Buffer Sizing
                                  # Inverter1
                                  _SAOutBuf_Inv1_NMOS_ChannelWidth=None,  # Number
                                  _SAOutBuf_Inv1_NMOS_ChannelLength=None,  # Number
                                  _SAOutBuf_Inv1_NMOS_NumberofGate=None,  # Number
                                  _SAOutBuf_Inv1_NMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _SAOutBuf_Inv1_NMOS_POGate_Comb_length=None,  # None/Number

                                  _SAOutBuf_Inv1_PMOS_ChannelWidth=None,  # Number
                                  _SAOutBuf_Inv1_PMOS_ChannelLength=None,  # Number
                                  _SAOutBuf_Inv1_PMOS_NumberofGate=None,  # Number
                                  _SAOutBuf_Inv1_PMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _SAOutBuf_Inv1_PMOS_POGate_Comb_length=None,  # None/Number

                                  # Inverter2
                                  _SAOutBuf_Inv2_NMOS_ChannelWidth=None,  # Number
                                  _SAOutBuf_Inv2_NMOS_ChannelLength=None,  # Number
                                  _SAOutBuf_Inv2_NMOS_NumberofGate=None,  # Number
                                  _SAOutBuf_Inv2_NMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _SAOutBuf_Inv2_NMOS_POGate_Comb_length=None,  # None/Number

                                  _SAOutBuf_Inv2_PMOS_ChannelWidth=None,  # Number
                                  _SAOutBuf_Inv2_PMOS_ChannelLength=None,  # Number
                                  _SAOutBuf_Inv2_PMOS_NumberofGate=None,  # Number
                                  _SAOutBuf_Inv2_PMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _SAOutBuf_Inv2_PMOS_POGate_Comb_length=None,  # None/Number

                                  ## SR Latch Sizing
                                  _SRLatch_NAND_NMOS_ChannelWidth=None,  # Number
                                  _SRLatch_NAND_NMOS_ChannelLength=None,  # Number
                                  _SRLatch_NAND_NMOS_NumberofGate=None,  # Number
                                  _SRLatch_NAND_NMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _SRLatch_NAND_NMOS_POGate_Comb_length=None,  # None/Number

                                  _SRLatch_NAND_PMOS_ChannelWidth=None,  # Number
                                  _SRLatch_NAND_PMOS_ChannelLength=None,  # Number
                                  _SRLatch_NAND_PMOS_NumberofGate=None,  # Number
                                  _SRLatch_NAND_PMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _SRLatch_NAND_PMOS_POGate_Comb_length=None,  # None/Number

                                  # CLK Input Logic Gates
                                  _CLKSamp_Inv_NMOS_ChannelWidth=None,
                                  _CLKSamp_Inv_NMOS_ChannelLength=None,
                                  _CLKSamp_Inv_NMOS_NumberofGate=None,
                                  _CLKSamp_Inv_NMOS_XVT=None,
                                  _CLKSamp_Inv_NMOS_POGate_Comb_length=None,

                                  _CLKSamp_Inv_PMOS_ChannelWidth=None,
                                  _CLKSamp_Inv_PMOS_ChannelLength=None,
                                  _CLKSamp_Inv_PMOS_NumberofGate=None,
                                  _CLKSamp_Inv_PMOS_XVT=None,
                                  _CLKSamp_Inv_PMOS_POGate_Comb_length=None,

                                  _CLKSrc_Inv_NMOS_ChannelWidth=None,
                                  _CLKSrc_Inv_NMOS_ChannelLength=None,
                                  _CLKSrc_Inv_NMOS_NumberofGate=None,
                                  _CLKSrc_Inv_NMOS_XVT=None,
                                  _CLKSrc_Inv_NMOS_POGate_Comb_length=None,

                                  _CLKSrc_Inv_PMOS_ChannelWidth=None,
                                  _CLKSrc_Inv_PMOS_ChannelLength=None,
                                  _CLKSrc_Inv_PMOS_NumberofGate=None,
                                  _CLKSrc_Inv_PMOS_XVT=None,
                                  _CLKSrc_Inv_PMOS_POGate_Comb_length=None,

                                  ## CLKSrc & CLKSample AND Gate
                                  _AND_NAND_NMOS_ChannelWidth=None,
                                  _AND_NAND_NMOS_ChannelLength=None,
                                  _AND_NAND_NMOS_NumberofGate=None,
                                  _AND_NAND_NMOS_XVT=None,

                                  _AND_NAND_PMOS_ChannelWidth=None,
                                  _AND_NAND_PMOS_ChannelLength=None,
                                  _AND_NAND_PMOS_NumberofGate=None,
                                  _AND_NAND_PMOS_XVT=None,

                                  _AND_Inv_NMOS_ChannelWidth=None,
                                  _AND_Inv_NMOS_ChannelLength=None,
                                  _AND_Inv_NMOS_NumberofGate=None,
                                  _AND_Inv_NMOS_XVT=None,
                                  _AND_Inv_NMOS_POGate_Comb_length=None,

                                  _AND_Inv_PMOS_ChannelWidth=None,
                                  _AND_Inv_PMOS_ChannelLength=None,
                                  _AND_Inv_PMOS_NumberofGate=None,
                                  _AND_Inv_PMOS_XVT=None,
                                  _AND_Inv_PMOS_POGate_Comb_length=None,

                                  ## CLK Buffer
                                  # Inverter1
                                  _CLKBuf_Inv1_NMOS_ChannelWidth=None,  # Number
                                  _CLKBuf_Inv1_NMOS_ChannelLength=None,  # Number
                                  _CLKBuf_Inv1_NMOS_NumberofGate=None,  # Number
                                  _CLKBuf_Inv1_NMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _CLKBuf_Inv1_NMOS_POGate_Comb_length=None,  # None/Number

                                  _CLKBuf_Inv1_PMOS_ChannelWidth=None,  # Number
                                  _CLKBuf_Inv1_PMOS_ChannelLength=None,  # Number
                                  _CLKBuf_Inv1_PMOS_NumberofGate=None,  # Number
                                  _CLKBuf_Inv1_PMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _CLKBuf_Inv1_PMOS_POGate_Comb_length=None,  # None/Number

                                  # Inverter2
                                  _CLKBuf_Inv2_NMOS_ChannelWidth=None,  # Number
                                  _CLKBuf_Inv2_NMOS_ChannelLength=None,  # Number
                                  _CLKBuf_Inv2_NMOS_NumberofGate=None,  # Number
                                  _CLKBuf_Inv2_NMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _CLKBuf_Inv2_NMOS_POGate_Comb_length=None,  # None/Number

                                  _CLKBuf_Inv2_PMOS_ChannelWidth=None,  # Number
                                  _CLKBuf_Inv2_PMOS_ChannelLength=None,  # Number
                                  _CLKBuf_Inv2_PMOS_NumberofGate=None,  # Number
                                  _CLKBuf_Inv2_PMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _CLKBuf_Inv2_PMOS_POGate_Comb_length=None,  # None/Number

                                  # PowerRail Placement
                                  _BufSR_NMOS_Pbody_NumCont=None,
                                  _BufSR_NMOS_Pbody_XvtTop2Pbody=None,
                                  _BufSR_PMOS_Nbody_NumCont=None,
                                  _BufSR_PMOS_Nbody_Xvtdown2Nbody=None,
                                  _BufSR_PMOSXvt2NMOSXvt=None,

                                  _CLKInLogic_NMOS_Pbody_Xvtdown2Pbody=None,
                                  _CLKInLogic_PMOS_Nbody_NumCont=None,
                                  _CLKInLogic_PMOS_Nbody_Xvtdown2Nbody=None,
                                  _CLKInLogic_PMOSXvt2NMOSXvt=None,
                                  ):


        ################################################################################################################################################## Class_HEADER: Pre Defined Parameter Before Calculation
        # Load DRC library
        _DRCobj = DRC.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']
        # Predefined variable

        E01_05_StrongArmWtSRLatch_start_time = time.time()
        ############################################################################################################################################################ CALCULATION START
        print( '#########################################################################################################')
        print( '                                      Calculation Start                                                  ')
        print( '#########################################################################################################')


            ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Calculation_Parameters = copy.deepcopy(Slicer._Slicer._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Calculation_Parameters['_CLKinputPMOSFinger1'] = _SALatch_CLKinputPMOSFinger1
        _Calculation_Parameters['_CLKinputPMOSFinger2'] = _SALatch_CLKinputPMOSFinger2
        _Calculation_Parameters['_PMOSFinger'] = _SALatch_PMOSFinger
        _Calculation_Parameters['_PMOSChannelWidth'] = _SALatch_PMOSChannelWidth
        _Calculation_Parameters['_DATAinputNMOSFinger'] = _SALatch_DATAinputNMOSFinger
        _Calculation_Parameters['_NMOSFinger'] = _SALatch_NMOSFinger
        _Calculation_Parameters['_CLKinputNMOSFinger'] = _SALatch_CLKinputNMOSFinger
        _Calculation_Parameters['_NMOSChannelWidth'] = _SALatch_NMOSChannelWidth
        _Calculation_Parameters['_CLKinputNMOSChannelWidth'] = _SALatch_CLKinputNMOSChannelWidth
        _Calculation_Parameters['_ChannelLength'] = _SALatch_ChannelLength
        _Calculation_Parameters['_Dummy'] = _SALatch_Dummy
        _Calculation_Parameters['_XVT'] = _SALatch_XVT
        _Calculation_Parameters['_GuardringWidth'] = _SALatch_GuardringWidth
        _Calculation_Parameters['_Guardring'] = _SALatch_Guardring
        _Calculation_Parameters['_SlicerGuardringWidth'] = _SALatch_SlicerGuardringWidth
        _Calculation_Parameters['_SlicerGuardring'] = _SALatch_SlicerGuardring
        _Calculation_Parameters['_NumSupplyCOY'] = _SALatch_NumSupplyCOY
        _Calculation_Parameters['_NumSupplyCOX'] = _SALatch_NumSupplyCOX
        _Calculation_Parameters['_SupplyMet1XWidth'] = _SALatch_SupplyMet1XWidth
        _Calculation_Parameters['_SupplyMet1YWidth'] = _SALatch_SupplyMet1YWidth
        _Calculation_Parameters['_VDD2VSSHeight'] = _SALatch_VDD2VSSHeight
        _Calculation_Parameters['_NumVIAPoly2Met1COX'] = _SALatch_NumVIAPoly2Met1COX
        _Calculation_Parameters['_NumVIAPoly2Met1COY'] = _SALatch_NumVIAPoly2Met1COY
        _Calculation_Parameters['_NumVIAMet12COX'] = _SALatch_NumVIAMet12COX
        _Calculation_Parameters['_NumVIAMet12COY'] = _SALatch_NumVIAMet12COY
        _Calculation_Parameters['_PowerLine'] = _SALatch_PowerLine

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Slicer'] = self._SrefElementDeclaration(_DesignObj=Slicer._Slicer(_DesignParameter=None, _Name='{}:SRF_Slicer'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Slicer']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slicer']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slicer']['_DesignObj']._CalculateDesignParameter(**_Calculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slicer']['_XYCoordinates'] = [[0, 0]]


        ######## SAOutput 'X' Boundary Element Generation
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_SAOutputNodeX_Hrz_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        BND_SAOutput_Hrz_M3_pathwidth = 50
        self._DesignParameter['BND_SAOutputNodeX_Hrz_M3']['_YWidth'] = BND_SAOutput_Hrz_M3_pathwidth

                ## Define Boundary_element _XWidth
        self._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_VIAPMOSMet23forRouting']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_VIAPMOSMet23forRouting']['_Angle'] = 0

        tmp1 = self.get_param_KJH3('SRF_Slicer','_VIAPMOSMet23forRouting','_Met3Layer')
        self._DesignParameter['BND_SAOutputNodeX_Hrz_M3']['_XWidth'] = 10000

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_SAOutputNodeX_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_SAOutputNodeX_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_SAOutputNodeX_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_SAOutputNodeX_Hrz_M3']['_XYCoordinates'] = tmpXY


        ######## SAOutput 'Y' Boundary Element Generation
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_SAOutputNodeY_Hrz_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_SAOutputNodeY_Hrz_M3']['_YWidth'] = BND_SAOutput_Hrz_M3_pathwidth

                ## Define Boundary_element _XWidth
        self._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_VIANMOSMet34forRouting']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_VIANMOSMet34forRouting']['_Angle'] = 0

        tmp1 = self.get_param_KJH3('SRF_Slicer','_VIANMOSMet34forRouting','_Met3Layer')
        # tmp2 = self.get_param_KJH4('SRF_SRLatch','SRF_InputS_ViaM1M3','SRF_ViaM1M2', 'BND_Met1Layer')
        # self._DesignParameter['BND_SAOutputNodeY_Hrz_M3']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0][0]['_XY_right'][0])
        self._DesignParameter['BND_SAOutputNodeY_Hrz_M3']['_XWidth'] = 10000
                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_SAOutputNodeY_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_SAOutputNodeY_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_SAOutputNodeY_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_SAOutputNodeY_Hrz_M3']['_XYCoordinates'] = tmpXY


        # save routing point
        SAOutputX_YcentCoord = self.get_param_KJH4('BND_SAOutputNodeX_Hrz_M3')[0][0]['_XY_cent'][1]
        SAOutputY_YcentCoord = self.get_param_KJH4('BND_SAOutputNodeY_Hrz_M3')[0][0]['_XY_cent'][1]


        ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
        #################### Buffers Generation
        ########### SA Output Node X -> Buffer X Generation
        _Caculation_Parameters = copy.deepcopy(E01_01_Buffer._Buffer._ParametersForDesignCalculation)
        _Caculation_Parameters['_Buf_Inv1_NMOS_ChannelWidth'] = _SAOutBuf_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters['_Buf_Inv1_NMOS_ChannelLength'] = _SAOutBuf_Inv1_NMOS_ChannelLength
        _Caculation_Parameters['_Buf_Inv1_NMOS_NumberofGate'] = _SAOutBuf_Inv1_NMOS_NumberofGate
        _Caculation_Parameters['_Buf_Inv1_NMOS_XVT'] = _SAOutBuf_Inv1_NMOS_XVT
        _Caculation_Parameters['_Buf_Inv1_NMOS_POGate_Comb_length'] = _SAOutBuf_Inv1_NMOS_POGate_Comb_length

        _Caculation_Parameters['_Buf_Inv1_PMOS_ChannelWidth'] = _SAOutBuf_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters['_Buf_Inv1_PMOS_ChannelLength'] = _SAOutBuf_Inv1_PMOS_ChannelLength
        _Caculation_Parameters['_Buf_Inv1_PMOS_NumberofGate'] = _SAOutBuf_Inv1_PMOS_NumberofGate
        _Caculation_Parameters['_Buf_Inv1_PMOS_XVT'] = _SAOutBuf_Inv1_PMOS_XVT
        _Caculation_Parameters['_Buf_Inv1_PMOS_POGate_Comb_length'] = _SAOutBuf_Inv1_PMOS_POGate_Comb_length

        _Caculation_Parameters['_Buf_Inv2_NMOS_ChannelWidth'] = _SAOutBuf_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters['_Buf_Inv2_NMOS_ChannelLength'] = _SAOutBuf_Inv2_NMOS_ChannelLength
        _Caculation_Parameters['_Buf_Inv2_NMOS_NumberofGate'] = _SAOutBuf_Inv2_NMOS_NumberofGate
        _Caculation_Parameters['_Buf_Inv2_NMOS_XVT'] = _SAOutBuf_Inv2_NMOS_XVT
        _Caculation_Parameters['_Buf_Inv2_NMOS_POGate_Comb_length'] = _SAOutBuf_Inv2_NMOS_POGate_Comb_length

        _Caculation_Parameters['_Buf_Inv2_PMOS_ChannelWidth'] = _SAOutBuf_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters['_Buf_Inv2_PMOS_ChannelLength'] = _SAOutBuf_Inv2_PMOS_ChannelLength
        _Caculation_Parameters['_Buf_Inv2_PMOS_NumberofGate'] = _SAOutBuf_Inv2_PMOS_NumberofGate
        _Caculation_Parameters['_Buf_Inv2_PMOS_XVT'] = _SAOutBuf_Inv2_PMOS_XVT
        _Caculation_Parameters['_Buf_Inv2_PMOS_POGate_Comb_length'] = _SAOutBuf_Inv2_PMOS_POGate_Comb_length

        _Caculation_Parameters['_Buf_NMOS_Pbody_NumCont'] = _BufSR_NMOS_Pbody_NumCont
        _Caculation_Parameters['_Buf_NMOS_Pbody_XvtTop2Pbody'] = _BufSR_NMOS_Pbody_XvtTop2Pbody
        _Caculation_Parameters['_Buf_PMOS_Nbody_NumCont'] = _BufSR_PMOS_Nbody_NumCont
        _Caculation_Parameters['_Buf_PMOS_Nbody_Xvtdown2Nbody'] = _BufSR_PMOS_Nbody_Xvtdown2Nbody
        _Caculation_Parameters['_Buf_PMOSXvt2NMOSXvt'] = _BufSR_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_BufferX'] = self._SrefElementDeclaration(
            _DesignObj=E01_01_Buffer._Buffer(_DesignParameter=None,
                                                             _Name='{}:SRF_BufferX'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_BufferX']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_BufferX']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_BufferX']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_BufferX']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        ## Target_coord: _XY_type1
        ##X
        self._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_VIAPMOSMet23forRouting']['_Reflect'] = [0,0,0]
        self._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_VIAPMOSMet23forRouting']['_Angle'] = 0

        tmp1x = self.get_param_KJH3('SRF_Slicer', '_GuardringVSS')
        tmpy = int((SAOutputX_YcentCoord + SAOutputY_YcentCoord)/2)
        target_coord = [tmp1x[0][0][0]['_XY_right'][0], tmpy]

        ## Approaching_coord: _XY_type2
        tmp2x = self.get_param_KJH4('SRF_BufferX', 'SRF_Inverter1', 'SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        tmp2y = self.get_param_KJH4('SRF_BufferX', 'SRF_Inverter1','BND_Input_Vtc_M1')
        approaching_coord = [tmp2x[0][0][0][0][0][0]['_XY_left'][0], tmp2y[0][0][0][0]['_XY_cent'][1]]

        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_BufferX')
        Scoord = tmp3[0][0]['_XY_origin']

        SpaceBtwSAandBuffer = 500
        Scoord[0] = Scoord[0] + SpaceBtwSAandBuffer

        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['SRF_BufferX']['_XYCoordinates'] = tmpXY


        ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
        ########### SA Output Node X -> Buffer X Generation
                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_BufferY'] = self._SrefElementDeclaration(_DesignObj=E01_01_Buffer._Buffer(_DesignParameter=None, _Name='{}:SRF_BufferY'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_BufferY']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_BufferY']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_BufferY']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_BufferY']['_XYCoordinates'] = [[0, 0]]

        tmpXY=[]
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_BufferX','SRF_Inverter2','SRF_NMOS', 'BND_PODummyLayer')
        target_coord = tmp1[0][0][0][-1][0]['_XY_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_BufferY','SRF_Inverter1','SRF_NMOS', 'BND_PODummyLayer')
        approaching_coord = tmp2[0][0][0][0][0]['_XY_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_BufferY')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[0] = Scoord[0] + 96
        # Scoord[0] = Scoord[0] + 140
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['SRF_BufferY']['_XYCoordinates'] = tmpXY


        ##### SA Output X <-> Buffer X inverter1 input Routing
        ###### Update Via Ycoord for routing
        del(self._DesignParameter['SRF_BufferX']['_DesignObj']._DesignParameter['SRF_Inv1Input_ViaM1M2'])
        del(self._DesignParameter['SRF_BufferX']['_DesignObj']._DesignParameter['SRF_Inv1Out2Inv2In_ViaM1M2'])
        del(self._DesignParameter['SRF_BufferX']['_DesignObj']._DesignParameter['BND_Inv1Out2Inv2In_Hrz_M1'])
        del(self._DesignParameter['SRF_BufferX']['_DesignObj']._DesignParameter['BND_Inv1Out2Inv2In_Hrz_M2'])
        del(self._DesignParameter['SRF_BufferX']['_DesignObj']._DesignParameter['SRF_Inv2Output_ViaM1M3'])

        ##### SA Output Y <-> Buffer Y inverter1 input Routing
        ###### Update Via Ycoord for routing
        del(self._DesignParameter['SRF_BufferY']['_DesignObj']._DesignParameter['SRF_Inv1Input_ViaM1M2'])
        del(self._DesignParameter['SRF_BufferY']['_DesignObj']._DesignParameter['SRF_Inv1Out2Inv2In_ViaM1M2'])
        del(self._DesignParameter['SRF_BufferY']['_DesignObj']._DesignParameter['BND_Inv1Out2Inv2In_Hrz_M1'])
        del(self._DesignParameter['SRF_BufferY']['_DesignObj']._DesignParameter['BND_Inv1Out2Inv2In_Hrz_M2'])
        del(self._DesignParameter['SRF_BufferY']['_DesignObj']._DesignParameter['SRF_Inv2Output_ViaM1M3'])

        ### Update BND_SAOutputNodeX_Hrz_M3 Xwidth
        tmp1 = self.get_param_KJH4('SRF_BufferX','SRF_Inverter1', 'BND_Input_Vtc_M1')
        tmp2 = self.get_param_KJH3('SRF_Slicer','_VIAPMOSMet23forRouting','_Met3Layer')
        self._DesignParameter['BND_SAOutputNodeX_Hrz_M3']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0])

        tmp1 = self.get_param_KJH4('SRF_BufferY','SRF_Inverter1', 'BND_Input_Vtc_M1')
        tmp2 = self.get_param_KJH3('SRF_Slicer','_VIANMOSMet34forRouting','_Met3Layer')
        self._DesignParameter['BND_SAOutputNodeY_Hrz_M3']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0])


        ##### SA Output X <-> Buffer X Routing
        ## Sref generation: Input S ViaM1M3
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_BufferXInput_ViaM1M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_BufferXInput_ViaM1M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_BufferXInput_ViaM1M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_BufferXInput_ViaM1M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_BufferXInput_ViaM1M3']['_DesignObj']._CalculateDesignParameterYmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_BufferXInput_ViaM1M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp = self.get_param_KJH4('BND_SAOutputNodeX_Hrz_M3')
        target_coord = tmp[0][0]['_XY_up_right']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_BufferXInput_ViaM1M3', 'SRF_ViaM1M2', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_BufferXInput_ViaM1M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_BufferXInput_ViaM1M3']['_XYCoordinates'] = tmpXY


        ######## Buffer X Inverter1 Out -> Inverter2 In Routing
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_BufX_Inv1Out2Inv2In_ViaM1M2'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_BufX_Inv1Out2Inv2In_ViaM1M2'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_BufX_Inv1Out2Inv2In_ViaM1M2']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_BufX_Inv1Out2Inv2In_ViaM1M2']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_BufX_Inv1Out2Inv2In_ViaM1M2']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_BufX_Inv1Out2Inv2In_ViaM1M2']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        tmp1x = self.get_param_KJH4('SRF_BufferX','SRF_Inverter1','BND_Out_Vtc_M2')
        tmp1y = SAOutputX_YcentCoord
        target_coord = [tmp1x[0][0][0][0]['_XY_left'][0], tmp1y]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_BufX_Inv1Out2Inv2In_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_left']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_BufX_Inv1Out2Inv2In_ViaM1M2')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_BufX_Inv1Out2Inv2In_ViaM1M2']['_XYCoordinates'] = tmpXY


        ## BND_Inv1Out2Inv2In_Hrz_M1 generation
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_BufX_Inv1Out2Inv2In_Hrz_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_BufX_Inv1Out2Inv2In_Hrz_M1']['_YWidth'] = 50

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_BufX_Inv1Out2Inv2In_ViaM1M2','SRF_ViaM1M2','BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_BufferX','SRF_Inverter2','BND_Input_Vtc_M1')
        self._DesignParameter['BND_BufX_Inv1Out2Inv2In_Hrz_M1']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_BufX_Inv1Out2Inv2In_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_BufX_Inv1Out2Inv2In_ViaM1M2','SRF_ViaM1M2','BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_BufX_Inv1Out2Inv2In_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_BufX_Inv1Out2Inv2In_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_BufX_Inv1Out2Inv2In_Hrz_M1']['_XYCoordinates'] = tmpXY


        ##### Buffer Y <-> SR Latch Input Routing
        ## Sref generation: Input S ViaM1M3
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_BufXOutput2SRInput_ViaM2M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_BufXOutput2SRInput_ViaM2M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_BufXOutput2SRInput_ViaM2M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_BufXOutput2SRInput_ViaM2M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_BufXOutput2SRInput_ViaM2M3']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_BufXOutput2SRInput_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp = self.get_param_KJH4('SRF_BufferX','SRF_Inverter2','BND_Out_Vtc_M2')
        target_coord = [tmp[0][0][0][0]['_XY_right'][0], SAOutputX_YcentCoord]
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_BufXOutput2SRInput_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_BufXOutput2SRInput_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_BufXOutput2SRInput_ViaM2M3']['_XYCoordinates'] = tmpXY


        ##### SA Output Y <-> Buffer Y Routing
        ## Sref generation: Input S ViaM1M3
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_BufferYInput_ViaM1M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_BufferYInput_ViaM1M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_BufferYInput_ViaM1M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_BufferYInput_ViaM1M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_BufferYInput_ViaM1M3']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_BufferYInput_ViaM1M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp = self.get_param_KJH4('BND_SAOutputNodeY_Hrz_M3')
        target_coord = tmp[0][0]['_XY_up_right']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_BufferYInput_ViaM1M3', 'SRF_ViaM1M2', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_BufferYInput_ViaM1M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_BufferYInput_ViaM1M3']['_XYCoordinates'] = tmpXY


        ######## Buffer Y Inverter1 Out -> Inverter2 In Routing
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_BufY_Inv1Out2Inv2In_ViaM1M2'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_BufY_Inv1Out2Inv2In_ViaM1M2'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_BufY_Inv1Out2Inv2In_ViaM1M2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_BufY_Inv1Out2Inv2In_ViaM1M2']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_BufY_Inv1Out2Inv2In_ViaM1M2']['_DesignObj']._CalculateDesignParameterYmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_BufY_Inv1Out2Inv2In_ViaM1M2']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1x = self.get_param_KJH4('SRF_BufferY', 'SRF_Inverter1', 'BND_Out_Vtc_M2')
        tmp1y = SAOutputY_YcentCoord
        target_coord = [tmp1x[0][0][0][0]['_XY_left'][0], tmp1y]
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_BufY_Inv1Out2Inv2In_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_BufY_Inv1Out2Inv2In_ViaM1M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_BufY_Inv1Out2Inv2In_ViaM1M2']['_XYCoordinates'] = tmpXY


        ## BND_Inv1Out2Inv2In_Hrz_M1 generation
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_BufY_Inv1Out2Inv2In_Hrz_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_BufY_Inv1Out2Inv2In_Hrz_M1']['_YWidth'] = 50

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_BufY_Inv1Out2Inv2In_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_BufferY', 'SRF_Inverter2', 'BND_Input_Vtc_M1')
        self._DesignParameter['BND_BufY_Inv1Out2Inv2In_Hrz_M1']['_XWidth'] = abs(
            tmp1[0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_BufY_Inv1Out2Inv2In_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_BufY_Inv1Out2Inv2In_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_BufY_Inv1Out2Inv2In_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_BufY_Inv1Out2Inv2In_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_BufY_Inv1Out2Inv2In_Hrz_M1']['_XYCoordinates'] = tmpXY


        ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
        ## NAND wt input 'R' SREF Generation
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_PMOS_power_v2._PMOS_POWER._ParametersForDesignCalculation)
        _Calculation_Parameters = copy.deepcopy(E01_04_SRLatch_random._SRLatch._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_PMOSPOWER_PbodyContact_1_Length']  = _PMOSPOWER_PbodyContact_1_Length

        _Calculation_Parameters['_NANDR_NMOSA_NMOSNumberofGate'] = _SRLatch_NAND_NMOS_NumberofGate
        _Calculation_Parameters['_NANDR_NMOSA_NMOSChannelWidth'] = _SRLatch_NAND_NMOS_ChannelWidth
        _Calculation_Parameters['_NANDR_NMOSA_NMOSChannellength'] = _SRLatch_NAND_NMOS_ChannelLength
        _Calculation_Parameters['_NANDR_NMOSA_GateSpacing'] = None
        _Calculation_Parameters['_NANDR_NMOSA_SDWidth'] = None
        _Calculation_Parameters['_NANDR_NMOSA_XVT'] = _SRLatch_NAND_NMOS_XVT
        _Calculation_Parameters['_NANDR_NMOSA_PCCrit'] = False
        _Calculation_Parameters['_NANDR_NMOSA_Source_Via_TF'] = True
        _Calculation_Parameters['_NANDR_NMOSA_Drain_Via_TF'] = True
        _Calculation_Parameters['_NANDR_NMOSA_NMOSDummy'] = True
        _Calculation_Parameters['_NANDR_NMOSA_NMOSDummy_length'] = None
        _Calculation_Parameters['_NANDR_NMOSA_NMOSDummy_placement'] = None
        _Calculation_Parameters['_NANDR_NMOSB_NMOSNumberofGate'] = _SRLatch_NAND_NMOS_NumberofGate
        _Calculation_Parameters['_NANDR_NMOSB_NMOSChannelWidth'] = _SRLatch_NAND_NMOS_ChannelWidth
        _Calculation_Parameters['_NANDR_NMOSB_NMOSChannellength'] = _SRLatch_NAND_NMOS_ChannelLength
        _Calculation_Parameters['_NANDR_NMOSB_GateSpacing'] = None
        _Calculation_Parameters['_NANDR_NMOSB_SDWidth'] = None
        _Calculation_Parameters['_NANDR_NMOSB_XVT'] = _SRLatch_NAND_NMOS_XVT
        _Calculation_Parameters['_NANDR_NMOSB_PCCrit'] = False
        _Calculation_Parameters['_NANDR_NMOSB_Source_Via_TF'] = False
        _Calculation_Parameters['_NANDR_NMOSB_Drain_Via_TF'] = True
        _Calculation_Parameters['_NANDR_NMOSB_NMOSDummy'] = True
        _Calculation_Parameters['_NANDR_NMOSB_NMOSDummy_length'] = None
        _Calculation_Parameters['_NANDR_NMOSB_NMOSDummy_placement'] = None
        _Calculation_Parameters['_NANDR_NMOSAB_Pbody_NumCont'] = _BufSR_NMOS_Pbody_NumCont
        _Calculation_Parameters['_NANDR_NMOSAB_Pbody_XlvtTop2Pdoby'] = _BufSR_NMOS_Pbody_XvtTop2Pbody

        _Calculation_Parameters['_NANDR_PMOSA_PMOSNumberofGate'] = _SRLatch_NAND_PMOS_NumberofGate
        _Calculation_Parameters['_NANDR_PMOSA_PMOSChannelWidth'] = _SRLatch_NAND_PMOS_ChannelWidth
        _Calculation_Parameters['_NANDR_PMOSA_PMOSChannellength'] = _SRLatch_NAND_PMOS_ChannelLength
        _Calculation_Parameters['_NANDR_PMOSA_GateSpacing'] = None
        _Calculation_Parameters['_NANDR_PMOSA_SDWidth'] = None
        _Calculation_Parameters['_NANDR_PMOSA_XVT'] = _SRLatch_NAND_PMOS_XVT
        _Calculation_Parameters['_NANDR_PMOSA_PCCrit'] = False
        _Calculation_Parameters['_NANDR_PMOSA_Source_Via_TF'] = False  # default
        _Calculation_Parameters['_NANDR_PMOSA_Drain_Via_TF'] = True
        _Calculation_Parameters['_NANDR_PMOSA_PMOSDummy'] = True
        _Calculation_Parameters['_NANDR_PMOSA_PMOSDummy_length'] = None
        _Calculation_Parameters['_NANDR_PMOSA_PMOSDummy_placement'] = None
        _Calculation_Parameters['_NANDR_PMOSB_PMOSNumberofGate'] = _SRLatch_NAND_PMOS_NumberofGate
        _Calculation_Parameters['_NANDR_PMOSB_PMOSChannelWidth'] = _SRLatch_NAND_PMOS_ChannelWidth
        _Calculation_Parameters['_NANDR_PMOSB_PMOSChannellength'] = _SRLatch_NAND_PMOS_ChannelLength
        _Calculation_Parameters['_NANDR_PMOSB_GateSpacing'] = None
        _Calculation_Parameters['_NANDR_PMOSB_SDWidth'] = None
        _Calculation_Parameters['_NANDR_PMOSB_XVT'] = _SRLatch_NAND_PMOS_XVT
        _Calculation_Parameters['_NANDR_PMOSB_PCCrit'] = False
        _Calculation_Parameters['_NANDR_PMOSB_Source_Via_TF'] = False  # default
        _Calculation_Parameters['_NANDR_PMOSB_Drain_Via_TF'] = True
        _Calculation_Parameters['_NANDR_PMOSB_PMOSDummy'] = True
        _Calculation_Parameters['_NANDR_PMOSB_PMOSDummy_length'] = None
        _Calculation_Parameters['_NANDR_PMOSB_PMOSDummy_placement'] = None
        _Calculation_Parameters['_NANDR_PMOSAB_Nbody_NumCont'] = _BufSR_PMOS_Nbody_NumCont
        _Calculation_Parameters['_NANDR_PMOSAB_Nbody_Xlvtdown2Ndoby'] = _BufSR_PMOS_Nbody_Xvtdown2Nbody
        _Calculation_Parameters['_NANDR_PMOSXvt2NMOSXvt'] = _BufSR_PMOSXvt2NMOSXvt

        _Calculation_Parameters['_NANDS_NMOSA_NMOSNumberofGate'] = _SRLatch_NAND_NMOS_NumberofGate
        _Calculation_Parameters['_NANDS_NMOSA_NMOSChannelWidth'] = _SRLatch_NAND_NMOS_ChannelWidth
        _Calculation_Parameters['_NANDS_NMOSA_NMOSChannellength'] = _SRLatch_NAND_NMOS_ChannelLength
        _Calculation_Parameters['_NANDS_NMOSA_GateSpacing'] =None
        _Calculation_Parameters['_NANDS_NMOSA_SDWidth'] =None
        _Calculation_Parameters['_NANDS_NMOSA_XVT'] = _SRLatch_NAND_NMOS_XVT
        _Calculation_Parameters['_NANDS_NMOSA_PCCrit'] =False
        _Calculation_Parameters['_NANDS_NMOSA_Source_Via_TF'] =True
        _Calculation_Parameters['_NANDS_NMOSA_Drain_Via_TF'] =True
        _Calculation_Parameters['_NANDS_NMOSA_NMOSDummy'] =True
        _Calculation_Parameters['_NANDS_NMOSA_NMOSDummy_length'] =None
        _Calculation_Parameters['_NANDS_NMOSA_NMOSDummy_placement'] =None
        _Calculation_Parameters['_NANDS_NMOSB_NMOSNumberofGate'] = _SRLatch_NAND_NMOS_NumberofGate
        _Calculation_Parameters['_NANDS_NMOSB_NMOSChannelWidth'] = _SRLatch_NAND_NMOS_ChannelWidth
        _Calculation_Parameters['_NANDS_NMOSB_NMOSChannellength'] = _SRLatch_NAND_NMOS_ChannelLength
        _Calculation_Parameters['_NANDS_NMOSB_GateSpacing'] =None
        _Calculation_Parameters['_NANDS_NMOSB_SDWidth'] =None
        _Calculation_Parameters['_NANDS_NMOSB_XVT'] = _SRLatch_NAND_NMOS_XVT
        _Calculation_Parameters['_NANDS_NMOSB_PCCrit'] =False
        _Calculation_Parameters['_NANDS_NMOSB_Source_Via_TF'] =False
        _Calculation_Parameters['_NANDS_NMOSB_Drain_Via_TF'] =True
        _Calculation_Parameters['_NANDS_NMOSB_NMOSDummy'] =True
        _Calculation_Parameters['_NANDS_NMOSB_NMOSDummy_length'] =None
        _Calculation_Parameters['_NANDS_NMOSB_NMOSDummy_placement'] =None
        _Calculation_Parameters['_NANDS_NMOSAB_Pbody_NumCont'] =_BufSR_NMOS_Pbody_NumCont
        _Calculation_Parameters['_NANDS_NMOSAB_Pbody_XlvtTop2Pdoby'] =_BufSR_NMOS_Pbody_XvtTop2Pbody

        _Calculation_Parameters['_NANDS_PMOSA_PMOSNumberofGate'] = _SRLatch_NAND_PMOS_NumberofGate
        _Calculation_Parameters['_NANDS_PMOSA_PMOSChannelWidth'] = _SRLatch_NAND_PMOS_ChannelWidth
        _Calculation_Parameters['_NANDS_PMOSA_PMOSChannellength'] = _SRLatch_NAND_PMOS_ChannelLength
        _Calculation_Parameters['_NANDS_PMOSA_GateSpacing'] =None
        _Calculation_Parameters['_NANDS_PMOSA_SDWidth'] =None
        _Calculation_Parameters['_NANDS_PMOSA_XVT'] = _SRLatch_NAND_PMOS_XVT
        _Calculation_Parameters['_NANDS_PMOSA_PCCrit'] =False
        _Calculation_Parameters['_NANDS_PMOSA_Source_Via_TF'] = False  # default
        _Calculation_Parameters['_NANDS_PMOSA_Drain_Via_TF'] =True
        _Calculation_Parameters['_NANDS_PMOSA_PMOSDummy'] =True
        _Calculation_Parameters['_NANDS_PMOSA_PMOSDummy_length'] =None
        _Calculation_Parameters['_NANDS_PMOSA_PMOSDummy_placement'] =None
        _Calculation_Parameters['_NANDS_PMOSB_PMOSNumberofGate'] = _SRLatch_NAND_PMOS_NumberofGate
        _Calculation_Parameters['_NANDS_PMOSB_PMOSChannelWidth'] = _SRLatch_NAND_PMOS_ChannelWidth
        _Calculation_Parameters['_NANDS_PMOSB_PMOSChannellength'] = _SRLatch_NAND_PMOS_ChannelLength
        _Calculation_Parameters['_NANDS_PMOSB_GateSpacing'] =None
        _Calculation_Parameters['_NANDS_PMOSB_SDWidth'] =None
        _Calculation_Parameters['_NANDS_PMOSB_XVT'] = _SRLatch_NAND_PMOS_XVT
        _Calculation_Parameters['_NANDS_PMOSB_PCCrit'] =False
        _Calculation_Parameters['_NANDS_PMOSB_Source_Via_TF'] = False  # default
        _Calculation_Parameters['_NANDS_PMOSB_Drain_Via_TF'] =True
        _Calculation_Parameters['_NANDS_PMOSB_PMOSDummy'] =True
        _Calculation_Parameters['_NANDS_PMOSB_PMOSDummy_length'] =None
        _Calculation_Parameters['_NANDS_PMOSB_PMOSDummy_placement'] =None
        _Calculation_Parameters['_NANDS_PMOSAB_Nbody_NumCont'] =_BufSR_PMOS_Nbody_NumCont
        _Calculation_Parameters['_NANDS_PMOSAB_Nbody_Xlvtdown2Ndoby'] =_BufSR_PMOS_Nbody_Xvtdown2Nbody
        _Calculation_Parameters['_NANDS_PMOSXvt2NMOSXvt'] =_BufSR_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_SRLatch'] = self._SrefElementDeclaration(
            _DesignObj=E01_04_SRLatch_random._SRLatch(_DesignParameter=None, _Name='{}:SRF_SRLatch'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_SRLatch']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SRLatch']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SRLatch']['_DesignObj']._CalculateDesignParameter(**_Calculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SRLatch']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        ## Target_coord: _XY_type1
                            ## Target_coord: _XY_type1
        tmp1x = self.get_param_KJH4('SRF_BufferY','SRF_Inverter2','SRF_NMOS', 'BND_PODummyLayer')
        tmp1y = self.get_param_KJH4('SRF_BufferY','SRF_Inverter2','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        target_coord = [tmp1x[0][0][0][-1][0]['_XY_right'][0], tmp1y[0][0][0][0][0][0]['_XY_down'][1]]

        ## Approaching_coord: _XY_type2
        tmp2x = self.get_param_KJH4('SRF_SRLatch','SRF_NANDS', 'SRF_Pulldown', 'SRF_NMOSB', 'BND_PODummyLayer')
        tmp2y = self.get_param_KJH4('SRF_SRLatch','BND_M1_NMOS_PBody_SRLatch')
        approaching_coord = [tmp2x[0][0][0][0][-1][0]['_XY_right'][0], tmp2y[0][0][0]['_XY_down'][1]]

        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_SRLatch')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[0] = Scoord[0] + 96
        # Scoord[0] = Scoord[0] + 140

        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['SRF_SRLatch']['_XYCoordinates'] = tmpXY


        ## SRF_SRLatch - BND_InputS_Hrz_M3 길이 연장 & Y 위치 조정
        tmp1 = self.get_param_KJH4('SRF_SRLatch', 'BND_InputR_Hrz_M3')
        tmp2 = self.get_param_KJH4('SRF_BufferX', 'SRF_Inverter2', 'BND_Out_Vtc_M2')
        ExtendLength = tmp1[0][0][0]['_XY_left'][0] - tmp2[0][0][0][0]['_XY_left'][0]
        YShiftAmount = SAOutputX_YcentCoord - tmp1[0][0][0]['_XY_cent'][1]
        self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['BND_InputR_Hrz_M3']['_XWidth'] = self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['BND_InputR_Hrz_M3']['_XWidth'] + ExtendLength

        self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['BND_InputR_Hrz_M3']['_XYCoordinates'][0][0] = self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['BND_InputR_Hrz_M3']['_XYCoordinates'][0][0] - ExtendLength

        self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['BND_InputR_Hrz_M3']['_XYCoordinates'][0][1] = self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['BND_InputR_Hrz_M3']['_XYCoordinates'][0][1] + YShiftAmount
        self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['SRF_InputR_ViaM1M3']['_XYCoordinates'][0][1] = self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['SRF_InputR_ViaM1M3']['_XYCoordinates'][0][1] + YShiftAmount


        ## SRF_SRLatch - BND_InputS_Hrz_M3 길이 연장 & Y 위치 조정
        tmp1 = self.get_param_KJH4('SRF_SRLatch', 'BND_InputS_Hrz_M3')
        tmp2 = self.get_param_KJH4('SRF_BufferY', 'SRF_Inverter2', 'BND_Out_Vtc_M2')
        ExtendLength = tmp1[0][0][0]['_XY_left'][0] - tmp2[0][0][0][0]['_XY_left'][0]
        YShiftAmount = SAOutputY_YcentCoord - tmp1[0][0][0]['_XY_cent'][1]
        self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['BND_InputS_Hrz_M3']['_XWidth'] = \
        self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['BND_InputS_Hrz_M3']['_XWidth'] + ExtendLength

        self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['BND_InputS_Hrz_M3']['_XYCoordinates'][0][0] = \
        self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['BND_InputS_Hrz_M3']['_XYCoordinates'][0][0] - ExtendLength

        self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['BND_InputS_Hrz_M3']['_XYCoordinates'][0][1] = \
        self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['BND_InputS_Hrz_M3']['_XYCoordinates'][0][1] + YShiftAmount

        self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['SRF_InputS_ViaM1M3']['_XYCoordinates'][0][1] = \
        self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['SRF_InputS_ViaM1M3']['_XYCoordinates'][0][1] + YShiftAmount

        # BufY -> SR Latch Routing Metal 변경 (M3 -> M2)
        self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['BND_InputS_Hrz_M3']['_Layer'] = 17  # M2로 변경, ViaM2M3 삭제
        del(self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['SRF_InputS_ViaM1M3']['_DesignObj']._DesignParameter['SRF_ViaM2M3'])


        ################################################################################################################
        ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
        ### CLK(Samp/Source) Input Logic(CLK Buffer, AND, 2 Inverters)
        ## CLK Buffer Generation
        ########### SA Output Node X -> Buffer X Generation
        _Caculation_Parameters = copy.deepcopy(E01_01_Buffer._Buffer._ParametersForDesignCalculation)
        _Caculation_Parameters['_Buf_Inv1_NMOS_ChannelWidth'] = _CLKBuf_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters['_Buf_Inv1_NMOS_ChannelLength'] = _CLKBuf_Inv1_NMOS_ChannelLength
        _Caculation_Parameters['_Buf_Inv1_NMOS_NumberofGate'] = _CLKBuf_Inv1_NMOS_NumberofGate
        _Caculation_Parameters['_Buf_Inv1_NMOS_XVT'] = _CLKBuf_Inv1_NMOS_XVT
        _Caculation_Parameters['_Buf_Inv1_NMOS_POGate_Comb_length'] = _CLKBuf_Inv1_NMOS_POGate_Comb_length

        _Caculation_Parameters['_Buf_Inv1_PMOS_ChannelWidth'] = _CLKBuf_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters['_Buf_Inv1_PMOS_ChannelLength'] = _CLKBuf_Inv1_PMOS_ChannelLength
        _Caculation_Parameters['_Buf_Inv1_PMOS_NumberofGate'] = _CLKBuf_Inv1_PMOS_NumberofGate
        _Caculation_Parameters['_Buf_Inv1_PMOS_XVT'] = _CLKBuf_Inv1_PMOS_XVT
        _Caculation_Parameters['_Buf_Inv1_PMOS_POGate_Comb_length'] = _CLKBuf_Inv1_PMOS_POGate_Comb_length

        _Caculation_Parameters['_Buf_Inv2_NMOS_ChannelWidth'] = _CLKBuf_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters['_Buf_Inv2_NMOS_ChannelLength'] = _CLKBuf_Inv2_NMOS_ChannelLength
        _Caculation_Parameters['_Buf_Inv2_NMOS_NumberofGate'] = _CLKBuf_Inv2_NMOS_NumberofGate
        _Caculation_Parameters['_Buf_Inv2_NMOS_XVT'] = _CLKBuf_Inv2_NMOS_XVT
        _Caculation_Parameters['_Buf_Inv2_NMOS_POGate_Comb_length'] = _CLKBuf_Inv2_NMOS_POGate_Comb_length

        _Caculation_Parameters['_Buf_Inv2_PMOS_ChannelWidth'] = _CLKBuf_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters['_Buf_Inv2_PMOS_ChannelLength'] = _CLKBuf_Inv2_PMOS_ChannelLength
        _Caculation_Parameters['_Buf_Inv2_PMOS_NumberofGate'] = _CLKBuf_Inv2_PMOS_NumberofGate
        _Caculation_Parameters['_Buf_Inv2_PMOS_XVT'] = _CLKBuf_Inv2_PMOS_XVT
        _Caculation_Parameters['_Buf_Inv2_PMOS_POGate_Comb_length'] = _CLKBuf_Inv2_PMOS_POGate_Comb_length

        _Caculation_Parameters['_Buf_NMOS_Pbody_NumCont'] =_BufSR_NMOS_Pbody_NumCont
        _Caculation_Parameters['_Buf_NMOS_Pbody_XvtTop2Pbody'] =_CLKInLogic_NMOS_Pbody_Xvtdown2Pbody
        _Caculation_Parameters['_Buf_PMOS_Nbody_NumCont'] =_CLKInLogic_PMOS_Nbody_NumCont
        _Caculation_Parameters['_Buf_PMOS_Nbody_Xvtdown2Nbody'] =_CLKInLogic_PMOS_Nbody_Xvtdown2Nbody
        _Caculation_Parameters['_Buf_PMOSXvt2NMOSXvt'] =_CLKInLogic_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_CLKBuffer'] = self._SrefElementDeclaration(
            _DesignObj=E01_01_Buffer._Buffer(_DesignParameter=None,
                                                             _Name='{}:SRF_CLKBuffer'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_CLKBuffer']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CLKBuffer']['_Angle'] = 180

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CLKBuffer']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CLKBuffer']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_BufferX','SRF_Inverter1','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        target_coord = tmp1[0][0][0][0][0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_CLKBuffer', 'SRF_Inverter2','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0][0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKBuffer')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['SRF_CLKBuffer']['_XYCoordinates'] = tmpXY


        ### AND Gate SREF Generation
        _Caculation_Parameters = copy.deepcopy(E01_03_AND_YJH_random._AND._ParametersForDesignCalculation)
        _Caculation_Parameters['_AND_NAND_NMOS_ChannelWidth'] = _AND_NAND_NMOS_ChannelWidth
        _Caculation_Parameters['_AND_NAND_NMOS_ChannelLength'] = _AND_NAND_NMOS_ChannelLength
        _Caculation_Parameters['_AND_NAND_NMOS_NumberofGate'] = _AND_NAND_NMOS_NumberofGate
        _Caculation_Parameters['_AND_NAND_NMOS_XVT'] = _AND_NAND_NMOS_XVT

        _Caculation_Parameters['_AND_NAND_PMOS_ChannelWidth'] = _AND_NAND_PMOS_ChannelWidth
        _Caculation_Parameters['_AND_NAND_PMOS_ChannelLength'] = _AND_NAND_PMOS_ChannelLength
        _Caculation_Parameters['_AND_NAND_PMOS_NumberofGate'] = _AND_NAND_PMOS_NumberofGate
        _Caculation_Parameters['_AND_NAND_PMOS_XVT'] = _AND_NAND_PMOS_XVT

        _Caculation_Parameters['_AND_Inv_NMOS_ChannelWidth'] = _AND_Inv_NMOS_ChannelWidth
        _Caculation_Parameters['_AND_Inv_NMOS_ChannelLength'] = _AND_Inv_NMOS_ChannelLength
        _Caculation_Parameters['_AND_Inv_NMOS_NumberofGate'] = _AND_Inv_NMOS_NumberofGate
        _Caculation_Parameters['_AND_Inv_NMOS_XVT'] = _AND_Inv_NMOS_XVT
        _Caculation_Parameters['_AND_Inv_NMOS_POGate_Comb_length'] = _AND_Inv_NMOS_POGate_Comb_length

        _Caculation_Parameters['_AND_Inv_PMOS_ChannelWidth'] = _AND_Inv_PMOS_ChannelWidth
        _Caculation_Parameters['_AND_Inv_PMOS_ChannelLength'] = _AND_Inv_PMOS_ChannelLength
        _Caculation_Parameters['_AND_Inv_PMOS_NumberofGate'] = _AND_Inv_PMOS_NumberofGate
        _Caculation_Parameters['_AND_Inv_PMOS_XVT'] = _AND_Inv_PMOS_XVT
        _Caculation_Parameters['_AND_Inv_PMOS_POGate_Comb_length'] = _AND_Inv_PMOS_POGate_Comb_length

        _Caculation_Parameters['_AND_NMOS_Pbody_NumCont'] = _BufSR_NMOS_Pbody_NumCont
        _Caculation_Parameters['_AND_NMOS_Pbody_XvtTop2Pbody'] = _CLKInLogic_NMOS_Pbody_Xvtdown2Pbody
        _Caculation_Parameters['_AND_PMOS_Nbody_NumCont'] = _CLKInLogic_PMOS_Nbody_NumCont
        _Caculation_Parameters['_AND_PMOS_Nbody_Xvtdown2Nbody'] = _CLKInLogic_PMOS_Nbody_Xvtdown2Nbody
        _Caculation_Parameters['_AND_PMOSXvt2NMOSXvt'] = _CLKInLogic_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_AND_CLKIn'] = self._SrefElementDeclaration(
            _DesignObj=E01_03_AND_YJH_random._AND(_DesignParameter=None, _Name='{}:SRF_AND_CLKIn'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_AND_CLKIn']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_AND_CLKIn']['_Angle'] = 180

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_AND_CLKIn']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_AND_CLKIn']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate
        ## Target_coord: _XY_type1
        tmp1x = self.get_param_KJH4('SRF_CLKBuffer', 'SRF_Inverter1','SRF_NMOS', 'BND_PODummyLayer')
        tmp1y = self.get_param_KJH4('SRF_CLKBuffer', 'SRF_Inverter1','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        target_coord = [tmp1x[0][0][0][0][0]['_XY_left'][0], tmp1y[0][0][0][0][0][0]['_XY_up'][1]]
        ## Approaching_coord: _XY_type2
        tmp2x = self.get_param_KJH4('SRF_AND_CLKIn','SRF_Inverter', 'SRF_NMOS', 'BND_PODummyLayer')
        tmp2y = self.get_param_KJH4('SRF_AND_CLKIn','SRF_Inverter', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = [tmp2x[0][0][0][-1][0]['_XY_right'][0], tmp2y[0][0][0][0][0][0]['_XY_up'][1]]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_AND_CLKIn')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[0] = Scoord[0] + 96
        # Scoord[0] = Scoord[0] + 140
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['SRF_AND_CLKIn']['_XYCoordinates'] = tmpXY


        ## CLK Samp Inverter SREF Generation
        _Caculation_Parameters = copy.deepcopy(E01_00_Inverter._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType'] = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn'] = 'Up'
        _Caculation_Parameters['_NMOS_NumberofGate'] = _CLKSrc_Inv_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth'] = _CLKSrc_Inv_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength'] = _CLKSrc_Inv_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing'] = None
        _Caculation_Parameters['_NMOS_SDWidth'] = None
        _Caculation_Parameters['_NMOS_XVT'] = _CLKSamp_Inv_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit'] = False
        _Caculation_Parameters['_NMOS_Source_Via_TF'] = False
        _Caculation_Parameters['_NMOS_Source_Via_Close2POpin_TF'] = False
        _Caculation_Parameters['_NMOS_Source_Comb_TF'] = False
        _Caculation_Parameters['_NMOS_Source_Comb_POpinward_TF'] = False
        _Caculation_Parameters['_NMOS_Source_Comb_Length'] = None
        _Caculation_Parameters['_NMOS_Drain_Via_TF'] = True
        _Caculation_Parameters['_NMOS_Drain_Via_Close2POpin_TF'] = True
        _Caculation_Parameters['_NMOS_Drain_Comb_TF'] = True
        _Caculation_Parameters['_NMOS_Drain_Comb_POpinward_TF'] = True
        _Caculation_Parameters['_NMOS_Drain_Comb_Length'] = 0
        _Caculation_Parameters['_NMOS_PODummy_TF'] = True
        _Caculation_Parameters['_NMOS_PODummy_Length'] = None
        _Caculation_Parameters['_NMOS_PODummy_Placement'] = None
        _Caculation_Parameters['_NMOS_Xvt_MinExten_TF'] = False
        _Caculation_Parameters['_NMOS_Xvt_Placement'] = None
        _Caculation_Parameters['_NMOS_POGate_Comb_TF'] = True
        _Caculation_Parameters['_NMOS_POGate_Comb_length'] = _CLKSrc_Inv_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF'] = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx'] = [0, 1]

        _Caculation_Parameters['_PMOS_MosType'] = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn'] = 'Dn'
        _Caculation_Parameters['_PMOS_NumberofGate'] = _CLKSrc_Inv_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth'] = _CLKSrc_Inv_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength'] = _CLKSrc_Inv_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing'] = None
        _Caculation_Parameters['_PMOS_SDWidth'] = None
        _Caculation_Parameters['_PMOS_XVT'] = _CLKSrc_Inv_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit'] = False
        _Caculation_Parameters['_PMOS_Source_Via_TF'] = False
        _Caculation_Parameters['_PMOS_Source_Via_Close2POpin_TF'] = False
        _Caculation_Parameters['_PMOS_Source_Comb_TF'] = False
        _Caculation_Parameters['_PMOS_Source_Comb_POpinward_TF'] = False
        _Caculation_Parameters['_PMOS_Source_Comb_Length'] = None
        _Caculation_Parameters['_PMOS_Drain_Via_TF'] = True
        _Caculation_Parameters['_PMOS_Drain_Via_Close2POpin_TF'] = True
        _Caculation_Parameters['_PMOS_Drain_Comb_TF'] = True
        _Caculation_Parameters['_PMOS_Drain_Comb_POpinward_TF'] = True
        _Caculation_Parameters['_PMOS_Drain_Comb_Length'] = 0
        _Caculation_Parameters['_PMOS_PODummy_TF'] = True
        _Caculation_Parameters['_PMOS_PODummy_Length'] = None
        _Caculation_Parameters['_PMOS_PODummy_Placement'] = None
        _Caculation_Parameters['_PMOS_Xvt_MinExten_TF'] = False
        _Caculation_Parameters['_PMOS_Xvt_Placement'] = None
        _Caculation_Parameters['_PMOS_POGate_Comb_TF'] = True
        _Caculation_Parameters['_PMOS_POGate_Comb_length'] = _CLKSrc_Inv_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF'] = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx'] = [0, 1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont'] = _BufSR_NMOS_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody'] = _CLKInLogic_NMOS_Pbody_Xvtdown2Pbody
        _Caculation_Parameters['_PMOS_Nbody_NumCont'] = _CLKInLogic_PMOS_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody'] = _CLKInLogic_PMOS_Nbody_Xvtdown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt'] = _CLKInLogic_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Inv_CLKSrc'] = self._SrefElementDeclaration(
            _DesignObj=E01_00_Inverter._Inverter(_DesignParameter=None, _Name='{}:SRF_Inv_CLKSrc'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Inv_CLKSrc']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inv_CLKSrc']['_Angle'] = 180

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inv_CLKSrc']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inv_CLKSrc']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate
        ## Target_coord: _XY_type1
        tmp1x = self.get_param_KJH4('SRF_AND_CLKIn','SRF_NAND','SRF_Pulldown', 'SRF_NMOSB', 'BND_PODummyLayer')
        tmp1y = self.get_param_KJH4('SRF_AND_CLKIn','SRF_Inverter', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        target_coord = [tmp1x[0][0][0][0][-1][0]['_XY_right'][0], tmp1y[0][0][0][0][0][0]['_XY_up'][1]]
        ## Approaching_coord: _XY_type2
        tmp2x = self.get_param_KJH4('SRF_Inv_CLKSrc', 'SRF_NMOS', 'BND_PODummyLayer')
        tmp2y = self.get_param_KJH4('SRF_Inv_CLKSrc', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = [tmp2x[0][0][-1][0]['_XY_right'][0], tmp2y[0][0][0][0][0]['_XY_up'][1]]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Inv_CLKSrc')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[0] = Scoord[0] + 96
        # Scoord[0] = Scoord[0] + 140
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['SRF_Inv_CLKSrc']['_XYCoordinates'] = tmpXY


        ## CLK Src Inverter SREF Generation
        _Caculation_Parameters = copy.deepcopy(E01_00_Inverter._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType'] = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn'] = 'Up'
        _Caculation_Parameters['_NMOS_NumberofGate'] = _CLKSamp_Inv_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth'] = _CLKSamp_Inv_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength'] = _CLKSamp_Inv_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing'] = None
        _Caculation_Parameters['_NMOS_SDWidth'] = None
        _Caculation_Parameters['_NMOS_XVT'] = _CLKSamp_Inv_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit'] = False
        _Caculation_Parameters['_NMOS_Source_Via_TF'] = False
        _Caculation_Parameters['_NMOS_Source_Via_Close2POpin_TF'] = False
        _Caculation_Parameters['_NMOS_Source_Comb_TF'] = False
        _Caculation_Parameters['_NMOS_Source_Comb_POpinward_TF'] = False
        _Caculation_Parameters['_NMOS_Source_Comb_Length'] = None
        _Caculation_Parameters['_NMOS_Drain_Via_TF'] = True
        _Caculation_Parameters['_NMOS_Drain_Via_Close2POpin_TF'] = True
        _Caculation_Parameters['_NMOS_Drain_Comb_TF'] = True
        _Caculation_Parameters['_NMOS_Drain_Comb_POpinward_TF'] = True
        _Caculation_Parameters['_NMOS_Drain_Comb_Length'] = 0
        _Caculation_Parameters['_NMOS_PODummy_TF'] = True
        _Caculation_Parameters['_NMOS_PODummy_Length'] = None
        _Caculation_Parameters['_NMOS_PODummy_Placement'] = None
        _Caculation_Parameters['_NMOS_Xvt_MinExten_TF'] = False
        _Caculation_Parameters['_NMOS_Xvt_Placement'] = None
        _Caculation_Parameters['_NMOS_POGate_Comb_TF'] = True
        _Caculation_Parameters['_NMOS_POGate_Comb_length'] = _CLKSamp_Inv_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF'] = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx'] = [0, 1]

        _Caculation_Parameters['_PMOS_MosType'] = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn'] = 'Dn'
        _Caculation_Parameters['_PMOS_NumberofGate'] = _CLKSamp_Inv_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth'] = _CLKSamp_Inv_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength'] = _CLKSamp_Inv_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing'] = None
        _Caculation_Parameters['_PMOS_SDWidth'] = None
        _Caculation_Parameters['_PMOS_XVT'] = _CLKSamp_Inv_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit'] = False
        _Caculation_Parameters['_PMOS_Source_Via_TF'] = False
        _Caculation_Parameters['_PMOS_Source_Via_Close2POpin_TF'] = False
        _Caculation_Parameters['_PMOS_Source_Comb_TF'] = False
        _Caculation_Parameters['_PMOS_Source_Comb_POpinward_TF'] = False
        _Caculation_Parameters['_PMOS_Source_Comb_Length'] = None
        _Caculation_Parameters['_PMOS_Drain_Via_TF'] = True
        _Caculation_Parameters['_PMOS_Drain_Via_Close2POpin_TF'] = True
        _Caculation_Parameters['_PMOS_Drain_Comb_TF'] = True
        _Caculation_Parameters['_PMOS_Drain_Comb_POpinward_TF'] = True
        _Caculation_Parameters['_PMOS_Drain_Comb_Length'] = 0
        _Caculation_Parameters['_PMOS_PODummy_TF'] = True
        _Caculation_Parameters['_PMOS_PODummy_Length'] = None
        _Caculation_Parameters['_PMOS_PODummy_Placement'] = None
        _Caculation_Parameters['_PMOS_Xvt_MinExten_TF'] = False
        _Caculation_Parameters['_PMOS_Xvt_Placement'] = None
        _Caculation_Parameters['_PMOS_POGate_Comb_TF'] = True
        _Caculation_Parameters['_PMOS_POGate_Comb_length'] = _CLKSamp_Inv_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF'] = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx'] = [0, 1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont'] = _BufSR_NMOS_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody'] = _CLKInLogic_NMOS_Pbody_Xvtdown2Pbody
        _Caculation_Parameters['_PMOS_Nbody_NumCont'] = _CLKInLogic_PMOS_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody'] = _CLKInLogic_PMOS_Nbody_Xvtdown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt'] = _CLKInLogic_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Inv_CLKSamp'] = self._SrefElementDeclaration(
            _DesignObj=E01_00_Inverter._Inverter(_DesignParameter=None, _Name='{}:SRF_Inv_CLKSamp'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Inv_CLKSamp']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inv_CLKSamp']['_Angle'] = 180

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inv_CLKSamp']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inv_CLKSamp']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1x = self.get_param_KJH4('SRF_Inv_CLKSrc', 'SRF_NMOS', 'BND_PODummyLayer')
        tmp1y = self.get_param_KJH4('SRF_Inv_CLKSrc', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        target_coord = [tmp1x[0][0][0][0]['_XY_left'][0], tmp1y[0][0][0][0][0]['_XY_up'][1]]
        ## Approaching_coord: _XY_type2
        tmp2x = self.get_param_KJH4('SRF_Inv_CLKSamp', 'SRF_NMOS', 'BND_PODummyLayer')
        tmp2y = self.get_param_KJH4('SRF_Inv_CLKSamp', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = [tmp2x[0][0][-1][0]['_XY_right'][0], tmp2y[0][0][0][0][0]['_XY_up'][1]]
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Inv_CLKSamp')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[0] = Scoord[0] + 96
        # Scoord[0] = Scoord[0] + 140
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['SRF_Inv_CLKSamp']['_XYCoordinates'] = tmpXY


        #### SRF Inv_CLKSamp_Input_ViaM1M4
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

            ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKSampInv_Input_ViaM1M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_CLKSampInv_Input_ViaM1M4'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_CLKSampInv_Input_ViaM1M4']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_CLKSampInv_Input_ViaM1M4']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKSampInv_Input_ViaM1M4']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKSampInv_Input_ViaM1M4']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        tmp1 = self.get_param_KJH4('SRF_Inv_CLKSamp','BND_Input_Vtc_M1')
        target_coord = tmp1[0][0][0]['_XY_left']
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CLKSampInv_Input_ViaM1M4','SRF_ViaM1M2','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_right']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKSampInv_Input_ViaM1M4')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_CLKSampInv_Input_ViaM1M4']['_XYCoordinates'] = tmpXY


        #### CLK_Samp Inverter -> AND gate routing
        #### SRF Inv_CLKSrc_Input_ViaM1M4
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

            ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKSrcInv_Input_ViaM1M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_CLKSrcInv_Input_ViaM1M4'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_CLKSrcInv_Input_ViaM1M4']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_CLKSrcInv_Input_ViaM1M4']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKSrcInv_Input_ViaM1M4']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKSrcInv_Input_ViaM1M4']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        tmp1 = self.get_param_KJH4('SRF_Inv_CLKSrc','BND_Input_Vtc_M1')
        target_coord = tmp1[0][0][0]['_XY_left']
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CLKSrcInv_Input_ViaM1M4','SRF_ViaM1M2','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_right']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKSrcInv_Input_ViaM1M4')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_CLKSrcInv_Input_ViaM1M4']['_XYCoordinates'] = tmpXY


        ###### CLK_Sample Inverter Output ViaM2M3
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKSampInvOut_ViaM2M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_CLKSampInvOut_ViaM2M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKSampInvOut_ViaM2M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKSampInvOut_ViaM2M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKSampInvOut_ViaM2M3']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKSampInvOut_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1x = self.get_param_KJH4('SRF_Inv_CLKSamp','BND_Out_Vtc_M2')
        tmp1y = self.get_param_KJH4('SRF_Inv_CLKSamp','SRF_PMOS', 'BND_Gate_Hrz_Mx')
        target_coord = [tmp1x[0][0][0]['_XY_right'][0], tmp1y[0][0][0][0]['_XY_down'][1]]
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CLKSampInvOut_ViaM2M3','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKSampInvOut_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKSampInvOut_ViaM2M3']['_XYCoordinates'] = tmpXY


        ###### CLK_Sample Inverter Output ViaM2M3
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_ANDInCLKSamp_ViaM1M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_ANDInCLKSamp_ViaM1M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_ANDInCLKSamp_ViaM1M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_ANDInCLKSamp_ViaM1M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_ANDInCLKSamp_ViaM1M3']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_ANDInCLKSamp_ViaM1M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1x = self.get_param_KJH4('SRF_AND_CLKIn','SRF_NAND','BND_InputB_Vtc_M1')
        tmp1y = self.get_param_KJH4('SRF_CLKSampInvOut_ViaM2M3','SRF_ViaM2M3', 'BND_Met3Layer')
        target_coord = [tmp1x[0][0][0][0]['_XY_left'][0], tmp1y[0][0][0][0]['_XY_down'][1]]
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_ANDInCLKSamp_ViaM1M3','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_ANDInCLKSamp_ViaM1M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_ANDInCLKSamp_ViaM1M3']['_XYCoordinates'] = tmpXY


        #### CLK_Samp Inverter -> AND gate routing
        #### BND_CLKSamp2AND_Hrz_M3
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CLKSamp2AND_Hrz_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKSampInvOut_ViaM2M3','SRF_ViaM2M3', 'BND_Met3Layer')
        tmp2 = self.get_param_KJH4('SRF_ANDInCLKSamp_ViaM1M3','SRF_ViaM2M3', 'BND_Met3Layer')
        self._DesignParameter['BND_CLKSamp2AND_Hrz_M3']['_YWidth'] = 50

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CLKSamp2AND_Hrz_M3']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0])

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_CLKSamp2AND_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_CLKSampInvOut_ViaM2M3','SRF_ViaM2M3', 'BND_Met3Layer')
        target_coord = tmp1[0][0][0][0]['_XY_down_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CLKSamp2AND_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_down_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CLKSamp2AND_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_CLKSamp2AND_Hrz_M3']['_XYCoordinates'] = tmpXY


        # pre-defined routing point(coordY)
        tmp = self.get_param_KJH4('SRF_CLKBuffer','SRF_Inverter1', 'BND_Input_Vtc_M1')
        upperroutepnty_CLKInLogic = max(int(tmp[0][0][0][0]['_XY_down'][1]*0.333 + tmp[0][0][0][0]['_XY_up'][1]*0.666),int(tmp[0][0][0][0]['_XY_down'][1]*0.666 + tmp[0][0][0][0]['_XY_up'][1]*0.333))
        # lowerroutepnty_CLKInLogic = min(int(tmp[0][0][0][0]['_XY_down'][1]*0.333 + tmp[0][0][0][0]['_XY_up'][1]*0.666),int(tmp[0][0][0][0]['_XY_down'][1]*0.666 + tmp[0][0][0][0]['_XY_up'][1]*0.333))


        #### CLK_Src Inverter -> AND gate routing
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKSrcOut2ANDIn_ViaM1M2'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_CLKSrcOut2ANDIn_ViaM1M2'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKSrcOut2ANDIn_ViaM1M2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKSrcOut2ANDIn_ViaM1M2']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKSrcOut2ANDIn_ViaM1M2']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKSrcOut2ANDIn_ViaM1M2']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1x_1 = self.get_param_KJH4('SRF_AND_CLKIn','SRF_NAND','BND_Out_Vtc_M2')
        tmp1x_2 = self.get_param_KJH4('SRF_AND_CLKIn','SRF_NAND','BND_InputB_Vtc_M1')
        tmp1x = int((tmp1x_1[0][0][0][0]['_XY_left'][0] + tmp1x_2[0][0][0][0]['_XY_right'][0])/2)
        tmp1y = upperroutepnty_CLKInLogic
        target_coord = [tmp1x, tmp1y]
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CLKSrcOut2ANDIn_ViaM1M2','SRF_ViaM1M2','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKSrcOut2ANDIn_ViaM1M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKSrcOut2ANDIn_ViaM1M2']['_XYCoordinates'] = tmpXY


        #### CLK_Src Inverter -> AND gate routing
        #### BND_CLKSrcOut_Hrz_M2
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CLKSrcOut_Hrz_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKSrcOut2ANDIn_ViaM1M2','SRF_ViaM1M2', 'BND_Met2Layer')
        tmp2 = self.get_param_KJH4('SRF_Inv_CLKSrc','BND_Out_Vtc_M2')
        self._DesignParameter['BND_CLKSrcOut_Hrz_M2']['_YWidth'] = 50

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CLKSrcOut_Hrz_M2']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_left'][0] - tmp2[0][0][0]['_XY_left'][0])

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_CLKSrcOut_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        # tmp1 = self.get_param_KJH4('SRF_CLKSampInvOut_ViaM2M3','SRF_ViaM2M3', 'BND_Met3Layer')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CLKSrcOut_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CLKSrcOut_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_CLKSrcOut_Hrz_M2']['_XYCoordinates'] = tmpXY


        #### CLK_Src Inverter -> AND gate routing
        #### BND_ANDIn_CLKSrc_Hrz_M1
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_ANDIn_CLKSrc_Hrz_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKSrcOut2ANDIn_ViaM1M2','SRF_ViaM1M2', 'BND_Met2Layer')
        tmp2 = self.get_param_KJH4('SRF_AND_CLKIn','SRF_NAND','BND_InputA_Vtc_M1')
        self._DesignParameter['BND_ANDIn_CLKSrc_Hrz_M1']['_YWidth'] = 50

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_ANDIn_CLKSrc_Hrz_M1']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0])

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_ANDIn_CLKSrc_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        # tmp1 = self.get_param_KJH4('SRF_CLKSampInvOut_ViaM2M3','SRF_ViaM2M3', 'BND_Met3Layer')
        target_coord = tmp1[0][0][0][0]['_XY_down_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_ANDIn_CLKSrc_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_down_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_ANDIn_CLKSrc_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_ANDIn_CLKSrc_Hrz_M1']['_XYCoordinates'] = tmpXY


        #### AND Output -> CLK Buffer Input
        #### BND_ANDIn_CLKSrc_Hrz_M1
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_AND_Out_Hrz_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKBuffer','SRF_Inv1Input_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        tmp2 = self.get_param_KJH4('SRF_AND_CLKIn','SRF_Inverter','BND_Out_Vtc_M2')
        self._DesignParameter['BND_AND_Out_Hrz_M2']['_YWidth'] = 50

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_AND_Out_Hrz_M2']['_XWidth'] = abs(tmp1[0][0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0])

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_AND_Out_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        # tmp1 = self.get_param_KJH4('SRF_CLKSampInvOut_ViaM2M3','SRF_ViaM2M3', 'BND_Met3Layer')
        target_coord = tmp1[0][0][0][0][0]['_XY_up_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_AND_Out_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_AND_Out_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_AND_Out_Hrz_M2']['_XYCoordinates'] = tmpXY


        # Calculate Power Rail Size
        tmp1 = self.get_param_KJH4('SRF_BufferX', 'SRF_Inverter1', 'SRF_Pbody', 'SRF_PbodyContactPhyLen','BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_BufferX', 'SRF_Inverter1', 'SRF_Nbody', 'SRF_NbodyContactPhyLen','BND_Met1Layer')
        SpaceBtwUpperRail = abs(tmp1[0][0][0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0][0]['_XY_up'][1])

        tmp3 =  self.get_param_KJH4('SRF_Inv_CLKSamp', 'SRF_Nbody', 'SRF_NbodyContactPhyLen','BND_Met1Layer')
        SpaceBtwLowerRail = abs(tmp1[0][0][0][0][0][0]['_XY_up'][1] - tmp3[0][0][0][0][0]['_XY_down'][1])


        ####### Metal 1 Layer Extension Pbody & Nbody
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Pbody_Hrz_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_BufferX', 'SRF_Inverter1', 'SRF_Pbody', 'SRF_PbodyContactPhyLen','BND_Met1Layer')
        tmp2_1 = self.get_param_KJH4('SRF_Inv_CLKSamp', 'SRF_Pbody', 'SRF_PbodyContactPhyLen','BND_Met1Layer')
        tmp2_2 = self.get_param_KJH4('SRF_SRLatch', 'BND_M1_NMOS_PBody_SRLatch')
        tmp2 = max(tmp2_1[0][0][0][0][0]['_XY_left'][0], tmp2_2[0][0][0]['_XY_right'][0])
        self._DesignParameter['BND_Pbody_Hrz_M1']['_YWidth'] = max(tmp2_2[0][0][0]['_Ywidth'], tmp2_1[0][0][0][0][0]['_Ywidth'])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Pbody_Hrz_M1']['_XWidth'] = abs(tmp1[0][0][0][0][0][0]['_XY_left'][0] - tmp2)
        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Pbody_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Pbody_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Pbody_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ScoordLower = copy.deepcopy(Scoord)
        ScoordLower[1] = ScoordLower[1] - SpaceBtwLowerRail
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, ScoordLower)
        tmpXY.append(New_Scoord)

        ScoordUpper = copy.deepcopy(Scoord)
        ScoordUpper[1] = ScoordUpper[1] + SpaceBtwUpperRail
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, ScoordUpper)
        tmpXY.append(New_Scoord)

        ## Define coordinates
        self._DesignParameter['BND_Pbody_Hrz_M1']['_XYCoordinates'] = tmpXY


        ####### RX Layer Extension On Pbody
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Pbody_Hrz_RX'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0],
            _Datatype=DesignParameters._LayerMapping['DIFF'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_BufferX', 'SRF_Inverter1', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_ODLayer')
        tmp2_1 = self.get_param_KJH4('SRF_Inv_CLKSamp', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_ODLayer')
        tmp2_2 = self.get_param_KJH4('SRF_SRLatch', 'BND_M1_NMOS_PBody_SRLatch')
        tmp2 = max(tmp2_1[0][0][0][0][0]['_XY_left'][0], tmp2_2[0][0][0]['_XY_right'][0])
        self._DesignParameter['BND_Pbody_Hrz_RX']['_YWidth'] = max(tmp2_2[0][0][0]['_Ywidth'],
                                                                   tmp2_1[0][0][0][0][0]['_Ywidth'])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Pbody_Hrz_RX']['_XWidth'] = abs(tmp1[0][0][0][0][0][0]['_XY_left'][0] - tmp2)
        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Pbody_Hrz_RX']['_XYCoordinates'] = [[0, 0]]
        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Pbody_Hrz_RX')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Pbody_Hrz_RX')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ScoordLower = copy.deepcopy(Scoord)
        ScoordLower[1] = ScoordLower[1] - SpaceBtwLowerRail
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, ScoordLower)
        tmpXY.append(New_Scoord)

        ScoordUpper = copy.deepcopy(Scoord)
        ScoordUpper[1] = ScoordUpper[1] + SpaceBtwUpperRail
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, ScoordUpper)
        tmpXY.append(New_Scoord)

        ## Define coordinates
        self._DesignParameter['BND_Pbody_Hrz_RX']['_XYCoordinates'] = tmpXY


        ####### PP Layer Extension On Pbody
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Pbody_Hrz_PP'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_BufferX', 'SRF_Inverter1', 'SRF_Pbody', 'SRF_PbodyContactPhyLen','BND_PPLayer')
        tmp2_1 = self.get_param_KJH4('SRF_Inv_CLKSamp', 'SRF_Pbody', 'SRF_PbodyContactPhyLen','BND_PPLayer')
        tmp2_2 = self.get_param_KJH4('SRF_SRLatch', 'BND_PPLayer_NMOS_PBody_SRLatch')
        tmp2 = max(tmp2_1[0][0][0][0][0]['_XY_left'][0], tmp2_2[0][0][0]['_XY_right'][0])
        self._DesignParameter['BND_Pbody_Hrz_PP']['_YWidth'] = max(tmp2_2[0][0][0]['_Ywidth'], tmp2_1[0][0][0][0][0]['_Ywidth'])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Pbody_Hrz_PP']['_XWidth'] = abs(tmp1[0][0][0][0][0][0]['_XY_left'][0] - tmp2)
        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Pbody_Hrz_PP']['_XYCoordinates'] = [[0, 0]]
        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Pbody_Hrz_PP')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Pbody_Hrz_PP')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Pbody_Hrz_PP']['_XYCoordinates'] = tmpXY


        ####### PP Layer Extension On PMOS
        #### PP Extension on PMOSs of CLKLogic
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PPOnCLKInLogic'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKBuffer', 'SRF_Inverter2', 'SRF_PMOS', 'BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_Inv_CLKSamp', 'SRF_PMOS', 'BND_PPLayer')
        self._DesignParameter['BND_PPOnCLKInLogic']['_YWidth'] = max(tmp1[0][0][0][0][0]['_Ywidth'], tmp2[0][0][0][0]['_Ywidth'])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_PPOnCLKInLogic']['_XWidth'] = abs(
            tmp1[0][0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0])
        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PPOnCLKInLogic']['_XYCoordinates'] = [[0, 0]]
        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0]['_XY_down_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PPOnCLKInLogic')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PPOnCLKInLogic')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_PPOnCLKInLogic']['_XYCoordinates'] = tmpXY


        ####### PP Layer Extension On PMOS
        #### PP Extension on PMOSs of SRLatch & SA Output Buffer
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PPOnSRLatchAndBuffer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_BufferX', 'SRF_Inverter1', 'SRF_PMOS', 'BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_SRLatch', 'SRF_NANDR', 'SRF_Pullup', 'SRF_PMOSB', 'BND_PPLayer')
        self._DesignParameter['BND_PPOnSRLatchAndBuffer']['_YWidth'] = max(tmp1[0][0][0][0][0]['_Ywidth'], tmp2[0][0][0][0][0][0]['_Ywidth'])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_PPOnSRLatchAndBuffer']['_XWidth'] = abs(
            tmp1[0][0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0][0][0]['_XY_right'][0])
        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PPOnSRLatchAndBuffer']['_XYCoordinates'] = [[0, 0]]
        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PPOnSRLatchAndBuffer')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PPOnSRLatchAndBuffer')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_PPOnSRLatchAndBuffer']['_XYCoordinates'] = tmpXY


        ####### XVT Layer Extension On MOSFET
        #### XVT Extension on PMOSs of SRLatch and SA Output Buffers
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_XVTExten_PMOSOnSRLatchAndBuffer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[_SRLatch_NAND_PMOS_XVT][0],
            _Datatype=DesignParameters._LayerMapping[_SRLatch_NAND_PMOS_XVT][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_BufferX', 'SRF_Inverter1', 'SRF_PMOS', 'BND_{}Layer'.format(_SAOutBuf_Inv1_PMOS_XVT))
        tmp2 = self.get_param_KJH4('SRF_SRLatch', 'SRF_NANDR', 'SRF_Pullup', 'SRF_PMOSB', 'BND_{}Layer'.format(_SRLatch_NAND_PMOS_XVT))
        self._DesignParameter['BND_XVTExten_PMOSOnSRLatchAndBuffer']['_YWidth'] = max(tmp1[0][0][0][0][0]['_Ywidth'],
                                                                     tmp2[0][0][0][0][0][0]['_Ywidth'])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_XVTExten_PMOSOnSRLatchAndBuffer']['_XWidth'] = abs(
            tmp1[0][0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0][0][0]['_XY_right'][0])
        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_XVTExten_PMOSOnSRLatchAndBuffer']['_XYCoordinates'] = [[0, 0]]
        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_XVTExten_PMOSOnSRLatchAndBuffer')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_XVTExten_PMOSOnSRLatchAndBuffer')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_XVTExten_PMOSOnSRLatchAndBuffer']['_XYCoordinates'] = tmpXY


        ####### XVT Layer Extension On MOSFET
        #### XVT Extension on PMOSs of SRLatch and SA Output Buffers
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_XVTExten_NMOSOnSRLatchAndBuffer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[_SRLatch_NAND_NMOS_XVT][0],
            _Datatype=DesignParameters._LayerMapping[_SRLatch_NAND_NMOS_XVT][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_BufferX', 'SRF_Inverter1', 'SRF_NMOS', 'BND_{}Layer'.format(_SAOutBuf_Inv1_NMOS_XVT))
        tmp2 = self.get_param_KJH4('SRF_SRLatch', 'SRF_NANDR', 'SRF_Pulldown', 'SRF_NMOSB', 'BND_{}Layer'.format(_SRLatch_NAND_NMOS_XVT))
        self._DesignParameter['BND_XVTExten_NMOSOnSRLatchAndBuffer']['_YWidth'] = max(tmp1[0][0][0][0][0]['_Ywidth'],
                                                                     tmp2[0][0][0][0][0][0]['_Ywidth'])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_XVTExten_NMOSOnSRLatchAndBuffer']['_XWidth'] = abs(
            tmp1[0][0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0][0][0]['_XY_right'][0])
        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_XVTExten_NMOSOnSRLatchAndBuffer']['_XYCoordinates'] = [[0, 0]]
        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_XVTExten_NMOSOnSRLatchAndBuffer')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_XVTExten_NMOSOnSRLatchAndBuffer')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_XVTExten_NMOSOnSRLatchAndBuffer']['_XYCoordinates'] = tmpXY


        ####### XVT Layer Extension On MOSFET
        #### XVT Extension on PMOSs of CLKLogic
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_XVTExten_PMOSOnCLKInLogic'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[_AND_NAND_PMOS_XVT][0],
            _Datatype=DesignParameters._LayerMapping[_AND_NAND_PMOS_XVT][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKBuffer', 'SRF_Inverter2', 'SRF_PMOS', 'BND_{}Layer'.format(_CLKBuf_Inv2_NMOS_XVT))
        tmp2 = self.get_param_KJH4('SRF_Inv_CLKSamp', 'SRF_PMOS', 'BND_{}Layer'.format(_CLKSamp_Inv_PMOS_XVT))
        self._DesignParameter['BND_XVTExten_PMOSOnCLKInLogic']['_YWidth'] = max(tmp1[0][0][0][0][0]['_Ywidth'],
                                                                     tmp2[0][0][0][0]['_Ywidth'])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_XVTExten_PMOSOnCLKInLogic']['_XWidth'] = abs(
            tmp1[0][0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0])
        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_XVTExten_PMOSOnCLKInLogic']['_XYCoordinates'] = [[0, 0]]
        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0]['_XY_down_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_XVTExten_PMOSOnCLKInLogic')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_XVTExten_PMOSOnCLKInLogic')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_XVTExten_PMOSOnCLKInLogic']['_XYCoordinates'] = tmpXY


        #### XVT Extension on NMOSs of CLKLogic
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_XVTExten_NMOSOnCLKInLogic'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[_AND_NAND_NMOS_XVT][0],
            _Datatype=DesignParameters._LayerMapping[_AND_NAND_NMOS_XVT][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKBuffer', 'SRF_Inverter2', 'SRF_NMOS', 'BND_{}Layer'.format(_CLKBuf_Inv2_NMOS_XVT))
        tmp2 = self.get_param_KJH4('SRF_Inv_CLKSamp', 'SRF_NMOS', 'BND_{}Layer'.format(_CLKSamp_Inv_NMOS_XVT))
        self._DesignParameter['BND_XVTExten_NMOSOnCLKInLogic']['_YWidth'] = max(tmp1[0][0][0][0][0]['_Ywidth'],tmp2[0][0][0][0]['_Ywidth'])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_XVTExten_NMOSOnCLKInLogic']['_XWidth'] = abs(tmp1[0][0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0])
        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_XVTExten_NMOSOnCLKInLogic']['_XYCoordinates'] = [[0, 0]]
        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0]['_XY_down_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_XVTExten_NMOSOnCLKInLogic')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_XVTExten_NMOSOnCLKInLogic')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_XVTExten_NMOSOnCLKInLogic']['_XYCoordinates'] = tmpXY



        ####### NW Layer Extension On PMOS
        #### NW Extension on PMOSs of CLK Input logic
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NWellOnCLKInLogic'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKBuffer', 'SRF_Inverter2', 'BND_PMOS_NellExten')
        tmp2 = self.get_param_KJH4('SRF_Inv_CLKSamp', 'BND_PMOS_NellExten')
        self._DesignParameter['BND_NWellOnCLKInLogic']['_YWidth'] = max(tmp1[0][0][0][0]['_Ywidth'], tmp2[0][0][0]['_Ywidth'])

        ## Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH4('BND_Pbody_Hrz_RX')
        self._DesignParameter['BND_NWellOnCLKInLogic']['_XWidth'] = tmp3[0][0]['_Xwidth'] + 3*_DRCobj._NwMinEnclosureNactive + 30
        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NWellOnCLKInLogic']['_XYCoordinates'] = [[0, 0]]
        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0]['_XY_down_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NWellOnCLKInLogic')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NWellOnCLKInLogic')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_NWellOnCLKInLogic']['_XYCoordinates'] = tmpXY


        ####### NW Layer Extension On PMOS
        #### NW Extension on PMOSs of SRLatch & SA Output Buffer
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NWellOnSRLatchAndBuffer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_BufferX', 'SRF_Inverter1', 'BND_PMOS_NellExten')
        tmp2 = self.get_param_KJH4('SRF_Inv_CLKSamp', 'BND_PMOS_NellExten')
        self._DesignParameter['BND_NWellOnSRLatchAndBuffer']['_YWidth'] = max(tmp1[0][0][0][0]['_Ywidth'], tmp2[0][0][0]['_Ywidth'])

        ## Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH4('BND_NWellOnCLKInLogic')
        self._DesignParameter['BND_NWellOnSRLatchAndBuffer']['_XWidth'] = tmp3[0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NWellOnSRLatchAndBuffer']['_XYCoordinates'] = [[0, 0]]
        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NWellOnSRLatchAndBuffer')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NWellOnSRLatchAndBuffer')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_NWellOnSRLatchAndBuffer']['_XYCoordinates'] = tmpXY


        ##### Slicer CLK Input Via M4 -> M6 Left & RightSide
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 4
        _Caculation_Parameters['_Layer2'] = 6
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

            ## Sref ViaX declaration
        self._DesignParameter['SRF_SlicerCLKInput_ViaM4M6'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_CLKInput_ViaM4M6'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_SlicerCLKInput_ViaM4M6']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_SlicerCLKInput_ViaM4M6']['_Angle'] = 0


            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_SlicerCLKInput_ViaM4M6']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_SlicerCLKInput_ViaM4M6']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        self._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_VIAMet32Met4OnforCLKPNRouting']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_VIAMet32Met4OnforCLKPNRouting']['_Angle'] = 0
        tmp1 = self.get_param_KJH3('SRF_Slicer','_VIAMet32Met4OnforCLKPNRouting')
        target_coord = tmp1[0][1][0]['_XY_cent']
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_SlicerCLKInput_ViaM4M6','SRF_ViaM4M5','BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_SlicerCLKInput_ViaM4M6')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate1
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Calculate2
        target_coord = tmp1[0][3][0]['_XY_cent']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_SlicerCLKInput_ViaM4M6']['_XYCoordinates'] = tmpXY


        ##### BND_SlicerCLKInput_Vtc_M6
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_SlicerCLKInput_Vtc_M6'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6'][0],
            _Datatype=DesignParameters._LayerMapping['METAL6'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('SRF_Slicer','_GuardringVSS')
        tmp2 = self.get_param_KJH4('SRF_SlicerCLKInput_ViaM4M6','SRF_ViaM4M5','BND_Met4Layer')
        self._DesignParameter['BND_SlicerCLKInput_Vtc_M6']['_YWidth'] = abs(tmp1[0][0][0]['_XY_cent'][1] - tmp2[0][0][0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_SlicerCLKInput_Vtc_M6']['_XWidth'] = tmp2[0][0][0][0]['_Xwidth']

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_SlicerCLKInput_Vtc_M6']['_XYCoordinates'] = [[0, 0]]
        ## Calculate1
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_SlicerCLKInput_ViaM4M6','SRF_ViaM4M5','BND_Met4Layer')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_SlicerCLKInput_Vtc_M6')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_SlicerCLKInput_Vtc_M6')
        Scoord = tmp3[0][0]['_XY_origin']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Calculate2
        target_coord = tmp1[1][0][0][0]['_XY_up_left']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_SlicerCLKInput_Vtc_M6']['_XYCoordinates'] = tmpXY


        ##### Slicer CLK Input Via M6 -> M5
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 5
        _Caculation_Parameters['_Layer2'] = 6
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_SlicerCLKInput_ViaM5M6'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_SlicerCLKInput_ViaM5M6'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_SlicerCLKInput_ViaM5M6']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_SlicerCLKInput_ViaM5M6']['_Angle'] = 0


            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_SlicerCLKInput_ViaM5M6']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_SlicerCLKInput_ViaM5M6']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        tmp1 = self.get_param_KJH4('BND_SlicerCLKInput_Vtc_M6')
        target_coord = tmp1[0][0]['_XY_down_left']
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_SlicerCLKInput_ViaM5M6','SRF_ViaM5M6','BND_Met5Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down_left']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_SlicerCLKInput_ViaM5M6')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate1
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Calculate2
        target_coord = tmp1[1][0]['_XY_down_right']
        approaching_coord = tmp2[0][0][0][0]['_XY_down_right']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_SlicerCLKInput_ViaM5M6']['_XYCoordinates'] = tmpXY


        ##### BND_SlicerCLKInput_Hrz_M5
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_SlicerCLKInput_Hrz_M5'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5'][0],
            _Datatype=DesignParameters._LayerMapping['METAL5'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_SlicerCLKInput_ViaM5M6','SRF_ViaM5M6','BND_Met5Layer')
        self._DesignParameter['BND_SlicerCLKInput_Hrz_M5']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_SlicerCLKInput_Hrz_M5']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_left'][0] - tmp1[1][0][0][0]['_XY_right'][0])

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_SlicerCLKInput_Hrz_M5']['_XYCoordinates'] = [[0, 0]]
        ## Calculate1
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_SlicerCLKInput_Hrz_M5')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_SlicerCLKInput_Hrz_M5')
        Scoord = tmp3[0][0]['_XY_origin']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_SlicerCLKInput_Hrz_M5']['_XYCoordinates'] = tmpXY


        ##### Slicer CLK Input Via M5 -> M3
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 5
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_SlicerCLKInput_ViaM3M5'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_SlicerCLKInput_ViaM3M5'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_SlicerCLKInput_ViaM3M5']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_SlicerCLKInput_ViaM3M5']['_Angle'] = 0


            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_SlicerCLKInput_ViaM3M5']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_SlicerCLKInput_ViaM3M5']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        tmp1 = self.get_param_KJH4('BND_SlicerCLKInput_Hrz_M5')
        target_coord = tmp1[0][0]['_XY_cent']
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_SlicerCLKInput_ViaM3M5','SRF_ViaM3M4','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_SlicerCLKInput_ViaM3M5')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate1
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_SlicerCLKInput_ViaM3M5']['_XYCoordinates'] = tmpXY


        ##### BND_SlicerCLKInput_Hrz_M3
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_SlicerCLKInput_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_SlicerCLKInput_ViaM3M5','SRF_ViaM3M4','BND_Met3Layer')
        self._DesignParameter['BND_SlicerCLKInput_Hrz_M3']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH4('SRF_CLKBuffer','SRF_Inverter2','BND_Out_Vtc_M2')
        self._DesignParameter['BND_SlicerCLKInput_Hrz_M3']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0]['_XY_left'][0])

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_SlicerCLKInput_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate1
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_SlicerCLKInput_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_SlicerCLKInput_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_SlicerCLKInput_Hrz_M3']['_XYCoordinates'] = tmpXY


        ##### Slicer CLK Input Via M3 -> M2
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

            ## Sref ViaX declaration
        self._DesignParameter['SRF_SlicerCLKInput_ViaM2M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_SlicerCLKInput_ViaM2M3'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_SlicerCLKInput_ViaM2M3']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_SlicerCLKInput_ViaM2M3']['_Angle'] = 0


            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_SlicerCLKInput_ViaM2M3']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_SlicerCLKInput_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        tmp1 = self.get_param_KJH4('BND_SlicerCLKInput_Hrz_M3')
        target_coord = tmp1[0][0]['_XY_down_right']
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_SlicerCLKInput_ViaM2M3','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down_right']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_SlicerCLKInput_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate1
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_SlicerCLKInput_ViaM2M3']['_XYCoordinates'] = tmpXY




        ## Body 공유로 인한 삭제 (삭제하지 않으면 CA가 겹쳐 DRC 발생 우려 있음.)
        del(self._DesignParameter['SRF_Inv_CLKSamp']['_DesignObj']._DesignParameter['SRF_Pbody'])
        del(self._DesignParameter['SRF_Inv_CLKSrc']['_DesignObj']._DesignParameter['SRF_Pbody'])
        del(self._DesignParameter['SRF_CLKBuffer']['_DesignObj']._DesignParameter['SRF_Inverter1']['_DesignObj']._DesignParameter['SRF_Pbody'])
        del(self._DesignParameter['SRF_CLKBuffer']['_DesignObj']._DesignParameter['SRF_Inverter2']['_DesignObj']._DesignParameter['SRF_Pbody'])
        del(self._DesignParameter['SRF_AND_CLKIn']['_DesignObj']._DesignParameter['SRF_NAND']['_DesignObj']._DesignParameter['SRF_Pbody'])
        del(self._DesignParameter['SRF_AND_CLKIn']['_DesignObj']._DesignParameter['SRF_Inverter']['_DesignObj']._DesignParameter['SRF_Pbody'])

        ## Via 위치 재 조정 후 생성하였기에 삭제.
        # del (self._DesignParameter['SRF_CLKBuffer']['_DesignObj']._DesignParameter['SRF_Inverter2']['_DesignObj']._DesignParameter['SRF_Inv2Output_ViaM1M2'])
        del (self._DesignParameter['SRF_CLKBuffer']['_DesignObj']._DesignParameter['SRF_Inv2Output_ViaM1M3'])

        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')

        ## CALCULATION END
        print('##############################################')
        print('##    CDAC With Driver (Unfolded) Calculation_END    ##')
        print('##############################################')
        E01_05_StrongArmWtSRLatch_end_time = time.time()
        self.E01_05_StrongArmWtSRLatch_elapsed_time = E01_05_StrongArmWtSRLatch_end_time - E01_05_StrongArmWtSRLatch_start_time

        # 1/14 clear
############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    import random

    for _iter in range(5):
        ''' Check Time'''
        start_time = time.time()

        from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
        from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

        libname = 'Proj_ZZ00_RcdacSar_E01_ComparatorWtLatch_random_v{}'.format(_iter + 46)
        cellname = 'E01_SALatchWtSRLatch'
        _fileName = cellname + '.gds'

        CLKinputPMOSFinger = random.randrange(4, 10, 2)
        PMOSFinger = random.randrange(3, 10, 1)
        PMOSChannelWidth = random.randrange(350, 1000, 50)
        DATAinputNMOSFinger = random.randrange(3, 10, 1)
        NMOSFinger = random.randrange(3, 10, 1)
        CLKinputNMOSFinger = random.randrange(3, 10, 1)
        NMOSChannelWidth = random.randrange(350, 1000, 50)

        Slicer_XVT_list = ['RVT', 'SLVT', 'LVT', 'HVT']
        # Slicer_XVT_list = ['SLVT']
        Slicer_Selected_XVT = random.choice(Slicer_XVT_list)

        SRinput_XVT_list = ['RVT', 'SLVT', 'LVT', 'HVT']
        # SRinput_XVT_list = ['SLVT']
        SRinput_Selected_XVT = random.choice(SRinput_XVT_list)
        SRinputMOS1Finger = random.choice([i for i in range (1,5) if i != 2])
        SRinputMOS2Finger = random.choice([i for i in range (1,5) if i != 2])
        MOSChannelWidth = random.randrange(300, 1001, 100)

        SRlatch_MOSFinger = random.randrange(2, 5, 1)

        CLK_MOSFinger = random.choice([i for i in range (1,5) if i != 2])
        Bottom_MOSChannelWidth = random.randrange(300, 1001, 100)

        INV_MOSFinger = random.choice([i for i in range (1,5) if i != 2])
        NAND_MOSFinger = random.choice([i for i in range (1,5) if i != 2])

        CompCLK_MOS1Finger = random.choice([i for i in range (1,5) if i != 2])
        CompCLK_MOS2Finger = random.choice([i for i in range (1,5) if i != 2])

        # 1/14 NAND source nmos via false로 바꾸는거부터 시작 ~

        ''' Input Parameters for Layout Object ''' ############################################################### ^^^^^^^^^^^^^^^^^^^^^
        InputParams = dict(
            ## StrongARM Latch
            _SALatch_CLKinputPMOSFinger1=CLKinputPMOSFinger,#random.randint(1, 15),  # 6
            _SALatch_CLKinputPMOSFinger2=CLKinputPMOSFinger,#random.randint(1, 15),  # 3
            _SALatch_PMOSFinger=PMOSFinger,#random.randint(1, 15),  # 3
            _SALatch_PMOSChannelWidth=PMOSChannelWidth,#random.randrange(200, 1050, 2),  # 500
            _SALatch_DATAinputNMOSFinger=DATAinputNMOSFinger,#random.randint(3, 15),  # 12
            _SALatch_NMOSFinger=NMOSFinger,#random.randint(1, 15),  # 2
            _SALatch_CLKinputNMOSFinger=CLKinputNMOSFinger,#random.randint(1, 15),  # 8
            _SALatch_NMOSChannelWidth=NMOSChannelWidth,#random.randrange(200, 1050, 2),  # 500
            _SALatch_CLKinputNMOSChannelWidth=NMOSChannelWidth,#random.randrange(200, 1050, 2),  # 800
            _SALatch_ChannelLength=30,#random.randrange(30, 60, 2),  # 30
            _SALatch_Dummy=True,
            _SALatch_XVT=Slicer_Selected_XVT,
            _SALatch_GuardringWidth=200,
            _SALatch_Guardring=True,
            _SALatch_SlicerGuardringWidth=200,
            _SALatch_SlicerGuardring=None,
            _SALatch_NumSupplyCOY=None,
            _SALatch_NumSupplyCOX=None,
            _SALatch_SupplyMet1XWidth=None,
            _SALatch_SupplyMet1YWidth=None,
            _SALatch_VDD2VSSHeight=None,
            _SALatch_NumVIAPoly2Met1COX=None,
            _SALatch_NumVIAPoly2Met1COY=None,
            _SALatch_NumVIAMet12COX=None,
            _SALatch_NumVIAMet12COY=None,
            _SALatch_PowerLine=False,

            ## StrongARMLatch Output Buffer Sizing
            # Inverter1
            _SAOutBuf_Inv1_NMOS_ChannelWidth=MOSChannelWidth,  # Number
            _SAOutBuf_Inv1_NMOS_ChannelLength=30,  # Number
            _SAOutBuf_Inv1_NMOS_NumberofGate=SRinputMOS1Finger,  # Number
            _SAOutBuf_Inv1_NMOS_XVT=SRinput_Selected_XVT,  # 'XVT' ex)SLVT/LVT/RVT/HVT
            _SAOutBuf_Inv1_NMOS_POGate_Comb_length=100,  # None/Number

            _SAOutBuf_Inv1_PMOS_ChannelWidth=2*MOSChannelWidth,  # Number
            _SAOutBuf_Inv1_PMOS_ChannelLength=30,  # Number
            _SAOutBuf_Inv1_PMOS_NumberofGate=SRinputMOS1Finger,  # Number
            _SAOutBuf_Inv1_PMOS_XVT=SRinput_Selected_XVT,  # 'XVT' ex)SLVT/LVT/RVT/HVT
            _SAOutBuf_Inv1_PMOS_POGate_Comb_length=100,  # None/Number

            # Inverter2
            _SAOutBuf_Inv2_NMOS_ChannelWidth=MOSChannelWidth,  # Number
            _SAOutBuf_Inv2_NMOS_ChannelLength=30,  # Number
            _SAOutBuf_Inv2_NMOS_NumberofGate=SRinputMOS2Finger,  # Number
            _SAOutBuf_Inv2_NMOS_XVT=SRinput_Selected_XVT,  # 'XVT' ex)SLVT/LVT/RVT/HVT
            _SAOutBuf_Inv2_NMOS_POGate_Comb_length=100,  # None/Number

            _SAOutBuf_Inv2_PMOS_ChannelWidth=2*MOSChannelWidth,  # Number
            _SAOutBuf_Inv2_PMOS_ChannelLength=30,  # Number
            _SAOutBuf_Inv2_PMOS_NumberofGate=SRinputMOS2Finger,  # Number
            _SAOutBuf_Inv2_PMOS_XVT=SRinput_Selected_XVT,  # 'XVT' ex)SLVT/LVT/RVT/HVT
            _SAOutBuf_Inv2_PMOS_POGate_Comb_length=100,  # None/Number

            ## SR Latch Size
            _SRLatch_NAND_NMOS_ChannelWidth=MOSChannelWidth,  # Number
            _SRLatch_NAND_NMOS_ChannelLength=30,  # Number
            _SRLatch_NAND_NMOS_NumberofGate=2*SRlatch_MOSFinger,  # Number
            _SRLatch_NAND_NMOS_XVT=SRinput_Selected_XVT,  # 'XVT' ex)SLVT/LVT/RVT/HVT
            _SRLatch_NAND_NMOS_POGate_Comb_length=100,  # None/Number

            _SRLatch_NAND_PMOS_ChannelWidth=2*MOSChannelWidth,  # Number
            _SRLatch_NAND_PMOS_ChannelLength=30,  # Number
            _SRLatch_NAND_PMOS_NumberofGate=SRlatch_MOSFinger,  # Number
            _SRLatch_NAND_PMOS_XVT=SRinput_Selected_XVT,  # 'XVT' ex)SLVT/LVT/RVT/HVT
            _SRLatch_NAND_PMOS_POGate_Comb_length=100,  # None/Number

            # CLK Input Logic Gates
            _CLKSamp_Inv_NMOS_ChannelWidth=Bottom_MOSChannelWidth,
            _CLKSamp_Inv_NMOS_ChannelLength=30,
            _CLKSamp_Inv_NMOS_NumberofGate=CLK_MOSFinger,
            _CLKSamp_Inv_NMOS_XVT=SRinput_Selected_XVT,
            _CLKSamp_Inv_NMOS_POGate_Comb_length=100,

            _CLKSamp_Inv_PMOS_ChannelWidth=2*Bottom_MOSChannelWidth,
            _CLKSamp_Inv_PMOS_ChannelLength=30,
            _CLKSamp_Inv_PMOS_NumberofGate=CLK_MOSFinger,
            _CLKSamp_Inv_PMOS_XVT=SRinput_Selected_XVT,
            _CLKSamp_Inv_PMOS_POGate_Comb_length=100,

            _CLKSrc_Inv_NMOS_ChannelWidth=Bottom_MOSChannelWidth,
            _CLKSrc_Inv_NMOS_ChannelLength=30,
            _CLKSrc_Inv_NMOS_NumberofGate=CLK_MOSFinger,
            _CLKSrc_Inv_NMOS_XVT=SRinput_Selected_XVT,
            _CLKSrc_Inv_NMOS_POGate_Comb_length=100,

            _CLKSrc_Inv_PMOS_ChannelWidth=2*Bottom_MOSChannelWidth,
            _CLKSrc_Inv_PMOS_ChannelLength=30,
            _CLKSrc_Inv_PMOS_NumberofGate=CLK_MOSFinger,
            _CLKSrc_Inv_PMOS_XVT=SRinput_Selected_XVT,
            _CLKSrc_Inv_PMOS_POGate_Comb_length=100,

            ## CLKSrc & CLKSample AND Gate
            _AND_NAND_NMOS_ChannelWidth=Bottom_MOSChannelWidth,
            _AND_NAND_NMOS_ChannelLength=30,
            _AND_NAND_NMOS_NumberofGate=2*NAND_MOSFinger,
            _AND_NAND_NMOS_XVT=SRinput_Selected_XVT,

            _AND_NAND_PMOS_ChannelWidth=2*Bottom_MOSChannelWidth,
            _AND_NAND_PMOS_ChannelLength=30,
            _AND_NAND_PMOS_NumberofGate=NAND_MOSFinger,
            _AND_NAND_PMOS_XVT=SRinput_Selected_XVT,

            _AND_Inv_NMOS_ChannelWidth=Bottom_MOSChannelWidth,
            _AND_Inv_NMOS_ChannelLength=30,
            _AND_Inv_NMOS_NumberofGate=INV_MOSFinger,
            _AND_Inv_NMOS_XVT=SRinput_Selected_XVT,
            _AND_Inv_NMOS_POGate_Comb_length=100,

            _AND_Inv_PMOS_ChannelWidth=2*Bottom_MOSChannelWidth,
            _AND_Inv_PMOS_ChannelLength=30,
            _AND_Inv_PMOS_NumberofGate=INV_MOSFinger,
            _AND_Inv_PMOS_XVT=SRinput_Selected_XVT,
            _AND_Inv_PMOS_POGate_Comb_length=100,

            ## CLK Buffer
            # Inverter1
            _CLKBuf_Inv1_NMOS_ChannelWidth=Bottom_MOSChannelWidth,  # Number
            _CLKBuf_Inv1_NMOS_ChannelLength=30,  # Number
            _CLKBuf_Inv1_NMOS_NumberofGate=CompCLK_MOS1Finger,  # Number
            _CLKBuf_Inv1_NMOS_XVT=SRinput_Selected_XVT,  # 'XVT' ex)SLVT/LVT/RVT/HVT
            _CLKBuf_Inv1_NMOS_POGate_Comb_length=100,  # None/Number

            _CLKBuf_Inv1_PMOS_ChannelWidth=2*Bottom_MOSChannelWidth,  # Number
            _CLKBuf_Inv1_PMOS_ChannelLength=30,  # Number
            _CLKBuf_Inv1_PMOS_NumberofGate=CompCLK_MOS1Finger,  # Number
            _CLKBuf_Inv1_PMOS_XVT=SRinput_Selected_XVT,  # 'XVT' ex)SLVT/LVT/RVT/HVT
            _CLKBuf_Inv1_PMOS_POGate_Comb_length=100,  # None/Number

            # Inverter2
            _CLKBuf_Inv2_NMOS_ChannelWidth=Bottom_MOSChannelWidth,  # Number
            _CLKBuf_Inv2_NMOS_ChannelLength=30,  # Number
            _CLKBuf_Inv2_NMOS_NumberofGate=CompCLK_MOS2Finger,  # Number
            _CLKBuf_Inv2_NMOS_XVT=SRinput_Selected_XVT,  # 'XVT' ex)SLVT/LVT/RVT/HVT
            _CLKBuf_Inv2_NMOS_POGate_Comb_length=100,  # None/Number

            _CLKBuf_Inv2_PMOS_ChannelWidth=2*Bottom_MOSChannelWidth,  # Number
            _CLKBuf_Inv2_PMOS_ChannelLength=30,  # Number
            _CLKBuf_Inv2_PMOS_NumberofGate=CompCLK_MOS2Finger,  # Number
            _CLKBuf_Inv2_PMOS_XVT=SRinput_Selected_XVT,  # 'XVT' ex)SLVT/LVT/RVT/HVT
            _CLKBuf_Inv2_PMOS_POGate_Comb_length=100,  # None/Number

            # PowerRail Placement
            _BufSR_NMOS_Pbody_NumCont=2,
            _BufSR_NMOS_Pbody_XvtTop2Pbody=None,
            _BufSR_PMOS_Nbody_NumCont=2,
            _BufSR_PMOS_Nbody_Xvtdown2Nbody=None,
            _BufSR_PMOSXvt2NMOSXvt=2000,

            _CLKInLogic_NMOS_Pbody_Xvtdown2Pbody=None,
            _CLKInLogic_PMOS_Nbody_NumCont=2,
            _CLKInLogic_PMOS_Nbody_Xvtdown2Nbody=None,
            _CLKInLogic_PMOSXvt2NMOSXvt=2000,
                            )

        '''Mode_DRCCHECK '''

        Mode_DRCCheck = False
        Num_DRCCheck =1

        for ii in range(0, Num_DRCCheck if Mode_DRCCheck else 1):
            if Mode_DRCCheck:
                ''' Input Parameters for Layout Object '''
            else:
                pass

        ''' Generate Layout Object '''
        LayoutObj = _StrongArmWtSRLatch(_DesignParameter=None, _Name=cellname)
        LayoutObj._CalculateDesignParameter(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
        testStreamFile = open('./{}'.format(_fileName), 'wb')
        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        # TestObj = _StrongArmLatch(_DesignParameter=None, _Name=cellname)
        # TestObj._CalculateDesignParameter(**InputParams)
        # print(TestObj._DesignParameter)
        # print(TestObj._DesignParameter)
        # TestObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary={'_Name': {'_DesignParametertype': 5, '_Name': 'E01_SALatch_v0'},
        #  '_GDSFile': {'_DesignParametertype': 4, '_GDSFile': None}, 'BND_test':LayoutObj._DesignParameter.get('BND_test')})
        # testStreamFile = open('./{}'.format(_fileName), 'wb')
        # tmp = TestObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
        # tmp.write_binary_gds_stream(testStreamFile)
        # testStreamFile.close()


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
        #Checker.cell_deletion()
        Checker.Upload2FTP()
        Checker.StreamIn(tech=DesignParameters._Technology)
        #Checker_KJH0.DRCchecker()

        ''' Check Time'''
        elapsed_time = time.time() - start_time
        m, s = divmod(elapsed_time,60)
        h, m = divmod(m, 60)


        print ('#############################      Finished      ################################')
        # end of 'main():' ---------------------------------------------------------------------------------------------

