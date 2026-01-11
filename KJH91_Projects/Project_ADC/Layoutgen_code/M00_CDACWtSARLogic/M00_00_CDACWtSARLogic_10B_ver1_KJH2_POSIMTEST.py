## Import Basic Modules
## Engine
# from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import StickDiagram
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import DesignParameters
from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import DRC

## Library
import copy
import time
import numpy as np

## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import Slicer
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A14_Mosfet_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3

from KJH91_Projects.Project_ADC.Layoutgen_code.L00_SARLogicWtComparator import L00_SARLogicWtComparator_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.H02_CDACWtDriver_YJH import H02_01_CDACWtDriver_Unfolded
from KJH91_Projects.Project_ADC.Layoutgen_code.H02_CDACWtDriver_YJH import H02_01_CDACWtDriver_Fold1_CC
from KJH91_Projects.Project_ADC.Layoutgen_code.H02_CDACWtDriver_YJH import H02_01_CDACWtDriver_Fold1_DrvArranged
from KJH91_Projects.Project_ADC.Layoutgen_code.C13_C07C11C12TieCellsRouted_YJH import C13_01_CtopCbotRouted_YJ_v01_00
from KJH91_Projects.Project_ADC.Layoutgen_code.D00_SARLogic_Inverter_KJH1 import D00_00_Inverter_KJH

# Update: And 에서 inverter size 기존크기에 4배로

## Define Class
class _CDACWtSARLogic(StickDiagram_KJH1._StickDiagram_KJH):
    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
        _NumofBit=8,
        _CDAC_Folding=None,  # None/True/False
        _Driver_CommonCentroidPlacementIfCDACFolded=False,  # 말 그대로 True이면 CommmonCentroid 배치가 됨.
        _Driver_DecimationIfDriverPlacedInCommonCentroid=True,
        _Driver_DecimationFactor=[2, 0, 0, 0, 0, 0, 0],  # [MSB, MSB-1 ... MSB-x]: 단 X<MSB  # 위 옵션 True시 작동; MSB부터 벡터로 작성; [3,2,2] 시 MSB0 -> 3:1, MSB1 -> 2:1, MSB2 -> 2:1, ... 1은 불가
        _SpaceBtwBootSWPosNeg=None,

        _Test_distance=330,
        _Routing_width=50,
        _Routing_distance=80,

        _SARLogic_YWidthOfCLKSrc=100,
        _SARLogic_SpaceBtwCLKSrcAndCLKSamp=100,
        _SARLogic_YWidthOfCLKSamp=100,

        _SARLogic_YWidthOfCompOut=100,
        _SARLogic_SpaceBtwCompOutAndCLKDout=100,
        _SARLogic_YWidthOfCLKDout=100,

        ## DFF Common
        _SARLogic_DFF_Pbody_NumCont=2,  # number
        _SARLogic_DFF_Nbody_NumCont=2,  # number
        _SARLogic_DFF_PMOSXvt2NMOSXvt=1150,  # number
        _SARLogic_DFF_XvtTop2Pbody=None,  # number/None(Minimum)
        _SARLogic_DFF_Xvtdown2Nbody=None,  # number/None(Minimum)

        ## Master Xgate1
        ## Xgate common

        ## Xgate NMOS
        _SARLogic_Mst_Xgate1_NMOS_NumberofGate=1,  # 1
        _SARLogic_Mst_Xgate1_NMOS_ChannelWidth=200,  # 100
        _SARLogic_Mst_Xgate1_NMOS_ChannelLength=30,
        _SARLogic_Mst_Xgate1_NMOS_XVT='HVT',
        _SARLogic_Mst_Xgate1_NMOS_POGate_Comb_length=100,

        ## Xgate PMOS
        _SARLogic_Mst_Xgate1_PMOS_NumberofGate=1,  # 1
        _SARLogic_Mst_Xgate1_PMOS_ChannelWidth=400,  # 200
        _SARLogic_Mst_Xgate1_PMOS_ChannelLength=30,
        _SARLogic_Mst_Xgate1_PMOS_XVT='HVT',
        _SARLogic_Mst_Xgate1_PMOS_POGate_Comb_length=100,

        ## Master Xgate2
        ## Xgate common

        ## Xgate NMOS
        _SARLogic_Mst_Xgate2_NMOS_NumberofGate=1,
        _SARLogic_Mst_Xgate2_NMOS_ChannelWidth=200,
        _SARLogic_Mst_Xgate2_NMOS_ChannelLength=30,
        _SARLogic_Mst_Xgate2_NMOS_XVT='SLVT',
        _SARLogic_Mst_Xgate2_NMOS_POGate_Comb_length=100,

        ## Xgate PMOS
        _SARLogic_Mst_Xgate2_PMOS_NumberofGate=2,  # 2
        _SARLogic_Mst_Xgate2_PMOS_ChannelWidth=200,
        _SARLogic_Mst_Xgate2_PMOS_ChannelLength=30,
        _SARLogic_Mst_Xgate2_PMOS_XVT='SLVT',
        _SARLogic_Mst_Xgate2_PMOS_POGate_Comb_length=100,

        ## Master Nor1
        ## Nor1 common

        ## NMOS
        ## NMOS common
        _SARLogic_Mst_Nor1_NMOS_XVT='HVT',

        ## NMOSA
        _SARLogic_Mst_Nor1_NMOSA_NumberofGate=2,
        _SARLogic_Mst_Nor1_NMOSA_ChannelWidth=200,
        _SARLogic_Mst_Nor1_NMOSA_ChannelLength=30,
        _SARLogic_Mst_Nor1_NMOSA_POGate_Comb_length=100,

        ## NMOSB
        _SARLogic_Mst_Nor1_NMOSB_NumberofGate=2,
        _SARLogic_Mst_Nor1_NMOSB_ChannelWidth=200,
        _SARLogic_Mst_Nor1_NMOSB_ChannelLength=30,
        _SARLogic_Mst_Nor1_NMOSB_POGate_Comb_length=100,

        ## PMOS
        ## PMOS common
        _SARLogic_Mst_Nor1_PMOS_XVT='HVT',

        ## PMOSA
        _SARLogic_Mst_Nor1_PMOSA_NumberofGate=4,
        _SARLogic_Mst_Nor1_PMOSA_ChannelWidth=400,
        _SARLogic_Mst_Nor1_PMOSA_ChannelLength=30,
        _SARLogic_Mst_Nor1_PMOSA_POGate_Comb_length=100,

        ## PMOSB
        _SARLogic_Mst_Nor1_PMOSB_NumberofGate=4,
        _SARLogic_Mst_Nor1_PMOSB_ChannelWidth=400,
        _SARLogic_Mst_Nor1_PMOSB_ChannelLength=30,
        _SARLogic_Mst_Nor1_PMOSB_POGate_Comb_length=100,

        ## Master Nor2
        ## Nor2 common

        ## NMOS
        ## NMOS common
        _SARLogic_Mst_Nor2_NMOS_XVT='HVT',

        ## NMOSA
        _SARLogic_Mst_Nor2_NMOSA_NumberofGate=2,
        _SARLogic_Mst_Nor2_NMOSA_ChannelWidth=200,
        _SARLogic_Mst_Nor2_NMOSA_ChannelLength=30,
        _SARLogic_Mst_Nor2_NMOSA_POGate_Comb_length=100,

        ## NMOSB
        _SARLogic_Mst_Nor2_NMOSB_NumberofGate=2,
        _SARLogic_Mst_Nor2_NMOSB_ChannelWidth=200,
        _SARLogic_Mst_Nor2_NMOSB_ChannelLength=30,
        _SARLogic_Mst_Nor2_NMOSB_POGate_Comb_length=100,

        ## PMOS
        ## PMOS common
        _SARLogic_Mst_Nor2_PMOS_XVT='HVT',

        ## PMOSA
        _SARLogic_Mst_Nor2_PMOSA_NumberofGate=4,
        _SARLogic_Mst_Nor2_PMOSA_ChannelWidth=400,
        _SARLogic_Mst_Nor2_PMOSA_ChannelLength=30,
        _SARLogic_Mst_Nor2_PMOSA_POGate_Comb_length=100,

        ## PMOSB
        _SARLogic_Mst_Nor2_PMOSB_NumberofGate=4,
        _SARLogic_Mst_Nor2_PMOSB_ChannelWidth=400,
        _SARLogic_Mst_Nor2_PMOSB_ChannelLength=30,
        _SARLogic_Mst_Nor2_PMOSB_POGate_Comb_length=100,

        ## Master Inv1 : Set pre-driver
        ## Inv1 common

        ## Inv1 NMOS
        _SARLogic_Mst_Inv1_NMOS_NumberofGate=1,
        _SARLogic_Mst_Inv1_NMOS_ChannelWidth=200,
        _SARLogic_Mst_Inv1_NMOS_ChannelLength=30,
        _SARLogic_Mst_Inv1_NMOS_XVT='SLVT',
        _SARLogic_Mst_Inv1_NMOS_POGate_Comb_length=100,

        ## Inv1 PMOS
        _SARLogic_Mst_Inv1_PMOS_NumberofGate=1,
        _SARLogic_Mst_Inv1_PMOS_ChannelWidth=400,
        _SARLogic_Mst_Inv1_PMOS_ChannelLength=30,
        _SARLogic_Mst_Inv1_PMOS_XVT='SLVT',
        _SARLogic_Mst_Inv1_PMOS_POGate_Comb_length=100,

        ## Master Inv2 : Set driver
        ## Inv2 common

        ## Inv2 NMOS
        _SARLogic_Mst_Inv2_NMOS_NumberofGate=1,
        _SARLogic_Mst_Inv2_NMOS_ChannelWidth=200,
        _SARLogic_Mst_Inv2_NMOS_ChannelLength=30,
        _SARLogic_Mst_Inv2_NMOS_XVT='SLVT',
        _SARLogic_Mst_Inv2_NMOS_POGate_Comb_length=100,

        ## Inv2 PMOS
        _SARLogic_Mst_Inv2_PMOS_NumberofGate=1,
        _SARLogic_Mst_Inv2_PMOS_ChannelWidth=400,
        _SARLogic_Mst_Inv2_PMOS_ChannelLength=30,
        _SARLogic_Mst_Inv2_PMOS_XVT='SLVT',
        _SARLogic_Mst_Inv2_PMOS_POGate_Comb_length=100,

        ## Master Inv3 : Clock driver
        ## Inv3 common

        ## Inv3 NMOS
        _SARLogic_Mst_Inv3_NMOS_NumberofGate=1,
        _SARLogic_Mst_Inv3_NMOS_ChannelWidth=200,
        _SARLogic_Mst_Inv3_NMOS_ChannelLength=30,
        _SARLogic_Mst_Inv3_NMOS_XVT='SLVT',
        _SARLogic_Mst_Inv3_NMOS_POGate_Comb_length=100,

        ## Inv3 PMOS
        _SARLogic_Mst_Inv3_PMOS_NumberofGate=1,
        _SARLogic_Mst_Inv3_PMOS_ChannelWidth=400,
        _SARLogic_Mst_Inv3_PMOS_ChannelLength=30,
        _SARLogic_Mst_Inv3_PMOS_XVT='SLVT',
        _SARLogic_Mst_Inv3_PMOS_POGate_Comb_length=100,

        ## Slave Xgate1
        ## Xgate common

        ## Xgate NMOS
        _SARLogic_Slv_Xgate1_NMOS_NumberofGate=1,
        _SARLogic_Slv_Xgate1_NMOS_ChannelWidth=200,
        _SARLogic_Slv_Xgate1_NMOS_ChannelLength=30,
        _SARLogic_Slv_Xgate1_NMOS_XVT='HVT',
        _SARLogic_Slv_Xgate1_NMOS_POGate_Comb_length=100,

        ## Xgate NMOS
        _SARLogic_Slv_Xgate1_PMOS_NumberofGate=1,
        _SARLogic_Slv_Xgate1_PMOS_ChannelWidth=400,
        _SARLogic_Slv_Xgate1_PMOS_ChannelLength=30,
        _SARLogic_Slv_Xgate1_PMOS_XVT='HVT',
        _SARLogic_Slv_Xgate1_PMOS_POGate_Comb_length=100,

        ## Slave Xgate2
        ## Xgate common

        ## Xgate NMOS
        _SARLogic_Slv_Xgate2_NMOS_NumberofGate=1,
        _SARLogic_Slv_Xgate2_NMOS_ChannelWidth=200,
        _SARLogic_Slv_Xgate2_NMOS_ChannelLength=30,
        _SARLogic_Slv_Xgate2_NMOS_XVT='SLVT',
        _SARLogic_Slv_Xgate2_NMOS_POGate_Comb_length=100,

        ## Xgate NMOS
        _SARLogic_Slv_Xgate2_PMOS_NumberofGate=2,
        _SARLogic_Slv_Xgate2_PMOS_ChannelWidth=200,
        _SARLogic_Slv_Xgate2_PMOS_ChannelLength=30,
        _SARLogic_Slv_Xgate2_PMOS_XVT='SLVT',
        _SARLogic_Slv_Xgate2_PMOS_POGate_Comb_length=100,

        ## Slave Nor1
        ## Nor1 common

        ## NMOS
        ## NMOS common
        _SARLogic_Slv_Nor1_NMOS_XVT='HVT',

        ## NMOSA
        _SARLogic_Slv_Nor1_NMOSA_NumberofGate=2,
        _SARLogic_Slv_Nor1_NMOSA_ChannelWidth=200,
        _SARLogic_Slv_Nor1_NMOSA_ChannelLength=30,
        _SARLogic_Slv_Nor1_NMOSA_POGate_Comb_length=100,

        ## NMOSB
        _SARLogic_Slv_Nor1_NMOSB_NumberofGate=2,
        _SARLogic_Slv_Nor1_NMOSB_ChannelWidth=200,
        _SARLogic_Slv_Nor1_NMOSB_ChannelLength=30,
        _SARLogic_Slv_Nor1_NMOSB_POGate_Comb_length=100,

        ## PMOS
        ## PMOS common
        _SARLogic_Slv_Nor1_PMOS_XVT='HVT',

        ## PMOSA
        _SARLogic_Slv_Nor1_PMOSA_NumberofGate=4,
        _SARLogic_Slv_Nor1_PMOSA_ChannelWidth=400,
        _SARLogic_Slv_Nor1_PMOSA_ChannelLength=30,
        _SARLogic_Slv_Nor1_PMOSA_POGate_Comb_length=100,

        ## PMOSB
        _SARLogic_Slv_Nor1_PMOSB_NumberofGate=4,
        _SARLogic_Slv_Nor1_PMOSB_ChannelWidth=400,
        _SARLogic_Slv_Nor1_PMOSB_ChannelLength=30,
        _SARLogic_Slv_Nor1_PMOSB_POGate_Comb_length=100,

        ## Slave Nor2
        ## Nor2 common

        ## NMOS
        ## NMOS common
        _SARLogic_Slv_Nor2_NMOS_XVT='HVT',

        ## NMOSA
        _SARLogic_Slv_Nor2_NMOSA_NumberofGate=2,
        _SARLogic_Slv_Nor2_NMOSA_ChannelWidth=200,
        _SARLogic_Slv_Nor2_NMOSA_ChannelLength=30,
        _SARLogic_Slv_Nor2_NMOSA_POGate_Comb_length=100,

        ## NMOSB
        _SARLogic_Slv_Nor2_NMOSB_NumberofGate=2,
        _SARLogic_Slv_Nor2_NMOSB_ChannelWidth=200,
        _SARLogic_Slv_Nor2_NMOSB_ChannelLength=30,
        _SARLogic_Slv_Nor2_NMOSB_POGate_Comb_length=100,

        ## PMOS
        ## PMOS common
        _SARLogic_Slv_Nor2_PMOS_XVT='HVT',

        ## PMOSA
        _SARLogic_Slv_Nor2_PMOSA_NumberofGate=4,
        _SARLogic_Slv_Nor2_PMOSA_ChannelWidth=400,
        _SARLogic_Slv_Nor2_PMOSA_ChannelLength=30,
        _SARLogic_Slv_Nor2_PMOSA_POGate_Comb_length=100,

        ## PMOSB
        _SARLogic_Slv_Nor2_PMOSB_NumberofGate=4,
        _SARLogic_Slv_Nor2_PMOSB_ChannelWidth=400,
        _SARLogic_Slv_Nor2_PMOSB_ChannelLength=30,
        _SARLogic_Slv_Nor2_PMOSB_POGate_Comb_length=100,

        ## Slave Inv1 : ReSet pre-driver
        ## Inv1 common

        ## Inv1 NMOS
        _SARLogic_Slv_Inv1_NMOS_NumberofGate=1,
        _SARLogic_Slv_Inv1_NMOS_ChannelWidth=200,
        _SARLogic_Slv_Inv1_NMOS_ChannelLength=30,
        _SARLogic_Slv_Inv1_NMOS_XVT='SLVT',
        _SARLogic_Slv_Inv1_NMOS_POGate_Comb_length=100,

        ## Inv1 PMOS
        _SARLogic_Slv_Inv1_PMOS_NumberofGate=1,
        _SARLogic_Slv_Inv1_PMOS_ChannelWidth=400,
        _SARLogic_Slv_Inv1_PMOS_ChannelLength=30,
        _SARLogic_Slv_Inv1_PMOS_XVT='SLVT',
        _SARLogic_Slv_Inv1_PMOS_POGate_Comb_length=100,

        ## Slave Inv2 : ReSet driver
        ## Inv2 common

        ## Inv2 NMOS
        _SARLogic_Slv_Inv2_NMOS_NumberofGate=1,
        _SARLogic_Slv_Inv2_NMOS_ChannelWidth=300,
        _SARLogic_Slv_Inv2_NMOS_ChannelLength=30,
        _SARLogic_Slv_Inv2_NMOS_XVT='SLVT',
        _SARLogic_Slv_Inv2_NMOS_POGate_Comb_length=100,

        ## Inv2 PMOS
        _SARLogic_Slv_Inv2_PMOS_NumberofGate=1,
        _SARLogic_Slv_Inv2_PMOS_ChannelWidth=400,
        _SARLogic_Slv_Inv2_PMOS_ChannelLength=30,
        _SARLogic_Slv_Inv2_PMOS_XVT='SLVT',
        _SARLogic_Slv_Inv2_PMOS_POGate_Comb_length=100,

        ## Slave Inv3 : Qb driver
        ## Inv3 common

        ## Inv3 NMOS
        _SARLogic_Slv_Inv3_NMOS_NumberofGate=5,  # 1
        _SARLogic_Slv_Inv3_NMOS_ChannelWidth=200,
        _SARLogic_Slv_Inv3_NMOS_ChannelLength=30,
        _SARLogic_Slv_Inv3_NMOS_XVT='SLVT',
        _SARLogic_Slv_Inv3_NMOS_POGate_Comb_length=100,

        ## Inv3 PMOS
        _SARLogic_Slv_Inv3_PMOS_NumberofGate=5,  # 1
        _SARLogic_Slv_Inv3_PMOS_ChannelWidth=400,
        _SARLogic_Slv_Inv3_PMOS_ChannelLength=30,
        _SARLogic_Slv_Inv3_PMOS_XVT='SLVT',
        _SARLogic_Slv_Inv3_PMOS_POGate_Comb_length=100,

        # Top Clock  Tree Size
        _SARLogic_CLKBufTreeTop_NumOfStage=4,
        _SARLogic_CLKBufTreeTop_CLKSampBuf_SizeByStage=None,
        _SARLogic_CLKBufTreeTop_CLKSrcBuf_SizeByStage=None,
        # 스테이지에 따른 버퍼 사이즈(UnitBuffer의 배수로 각 스테이지의 크기가 결정 됨.)
        _SARLogic_CLKBufTreeTop_XOffSet=0,  # (8Bit DRC check:-79)

        ## Top CLK Buffer Size
        _SARLogic_CLKBufTreeTop_Inv_NMOS_ChannelWidth=400,  # Number
        _SARLogic_CLKBufTreeTop_Inv_NMOS_ChannelLength=30,  # Number
        _SARLogic_CLKBufTreeTop_Inv_NMOS_NumberofGate=1,  # Number
        _SARLogic_CLKBufTreeTop_Inv_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _SARLogic_CLKBufTreeTop_Inv_NMOS_POGate_Comb_length=100,  # None/Number

        _SARLogic_CLKBufTreeTop_Inv_PMOS_ChannelWidth=800,  # Number
        _SARLogic_CLKBufTreeTop_Inv_PMOS_ChannelLength=30,  # Number
        _SARLogic_CLKBufTreeTop_Inv_PMOS_NumberofGate=1,  # Number
        _SARLogic_CLKBufTreeTop_Inv_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _SARLogic_CLKBufTreeTop_Inv_PMOS_POGate_Comb_length=100,  # None/Number

        # Top CLK BufferPowerRail Size
        _SARLogic_CLKBufTreeTop_NMOS_Pbody_NumCont=2,
        _SARLogic_CLKBufTreeTop_NMOS_Pbody_XvtTop2Pbody=None,
        _SARLogic_CLKBufTreeTop_PMOS_Nbody_NumCont=2,
        _SARLogic_CLKBufTreeTop_PMOS_Nbody_Xvtdown2Nbody=None,
        _SARLogic_CLKBufTreeTop_PMOSXvt2NMOSXvt=700,

        # Bottom Clock  Tree Size
        _SARLogic_CLKBufTreeBot_NumOfStage=4,
        _SARLogic_CLKBufTreeBot_CompOutBuf_SizeByStage=None,
        _SARLogic_CLKBufTreeBot_CLKDoutBuf_SizeByStage=None,
        # 스테이지에 따른 버퍼 사이즈(UnitBuffer의 배수로 각 스테이지의 크기가 결정 됨.)
        _SARLogic_CLKBufTreeBot_XOffSet=0,

        ## Bottom CLK Buffer Size
        _SARLogic_CLKBufTreeBot_Inv_NMOS_ChannelWidth=400,  # Number
        _SARLogic_CLKBufTreeBot_Inv_NMOS_ChannelLength=30,  # Number
        _SARLogic_CLKBufTreeBot_Inv_NMOS_NumberofGate=1,  # Number
        _SARLogic_CLKBufTreeBot_Inv_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _SARLogic_CLKBufTreeBot_Inv_NMOS_POGate_Comb_length=100,  # None/Number

        _SARLogic_CLKBufTreeBot_Inv_PMOS_ChannelWidth=800,  # Number
        _SARLogic_CLKBufTreeBot_Inv_PMOS_ChannelLength=30,  # Number
        _SARLogic_CLKBufTreeBot_Inv_PMOS_NumberofGate=1,  # Number
        _SARLogic_CLKBufTreeBot_Inv_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _SARLogic_CLKBufTreeBot_Inv_PMOS_POGate_Comb_length=100,  # None/Number

        # Bottom CLK Buffer PowerRail Size
        _SARLogic_CLKBufTreeBot_NMOS_Pbody_NumCont=2,
        _SARLogic_CLKBufTreeBot_NMOS_Pbody_XvtTop2Pbody=None,
        _SARLogic_CLKBufTreeBot_PMOS_Nbody_NumCont=2,
        _SARLogic_CLKBufTreeBot_PMOS_Nbody_Xvtdown2Nbody=None,
        _SARLogic_CLKBufTreeBot_PMOSXvt2NMOSXvt=700,

        #### CDAC Pre-Driver Sizing
        ## InvChain Common
        _CDACPreDriver_Pbody_NumCont=2,  # number
        _CDACPreDriver_Nbody_NumCont=2,  # number
        _CDACPreDriver_PMOSXvt2NMOSXvt=500,  # number
        _CDACPreDriver_XvtTop2Pbody=None,  # number/None(Minimum)
        _CDACPreDriver_Xvtdown2Nbody=None,  # number/None(Minimum)

        ## Inverter Chain
        ## Inv1 common
        _CDACPreDriver_NumberofGate=[2, 4, 6],  # Vector
        _CDACPreDriver_ChannelLength=30,  # Scalar
        _CDACPreDriver_XVT='SLVT',  # 'SLVT'

        ## Inv1 NMOS
        _CDACPreDriver_Inv_NMOS_ChannelWidth=200,  # Scalar
        _CDACPreDriver_Inv_NMOS_POGate_Comb_length=100,  # Scalar

        ## Inv1 PMOS
        _CDACPreDriver_Inv_PMOS_ChannelWidth=400,  # Scalar
        _CDACPreDriver_Inv_PMOS_POGate_Comb_length=100,  # Scalar

        ## CLKDout(OutSamp) Inverter & AND Common Option
        _CLKDout_XVT_Common='SLVT',

        ## CLKDout(OutSamp) Inverter Size
        _CLKDout_Inv_NMOS_ChannelWidth=400,  # Number
        _CLKDout_Inv_NMOS_ChannelLength=30,  # Number
        _CLKDout_Inv_NMOS_NumberofGate=1,  # Number
        _CLKDout_Inv_NMOS_POGate_Comb_length=100,  # None/Number

        _CLKDout_Inv_PMOS_ChannelWidth=800,  # Number
        _CLKDout_Inv_PMOS_ChannelLength=30,  # Number
        _CLKDout_Inv_PMOS_NumberofGate=1,  # Number
        _CLKDout_Inv_PMOS_POGate_Comb_length=100,  # None/Number

        ## CLKDout(OutSamp) AND Size
        _CLKDout_AND_NAND_NMOS_ChannelWidth=400,
        _CLKDout_AND_NAND_NMOS_ChannelLength=30,
        _CLKDout_AND_NAND_NMOS_NumberofGate=2,

        _CLKDout_AND_NAND_PMOS_ChannelWidth=800,
        _CLKDout_AND_NAND_PMOS_ChannelLength=30,
        _CLKDout_AND_NAND_PMOS_NumberofGate=1,

        _CLKDout_AND_Inv_NMOS_ChannelWidth=400,
        _CLKDout_AND_Inv_NMOS_ChannelLength=30,
        _CLKDout_AND_Inv_NMOS_NumberofGate=1,
        _CLKDout_AND_Inv_NMOS_POGate_Comb_length=100,

        _CLKDout_AND_Inv_PMOS_ChannelWidth=800,
        _CLKDout_AND_Inv_PMOS_ChannelLength=30,
        _CLKDout_AND_Inv_PMOS_NumberofGate=1,
        _CLKDout_AND_Inv_PMOS_POGate_Comb_length=100,

        ## StrongArm Latch
        _Comp_SALatch_CLKinputPMOSFinger1=None,  # 6
        _Comp_SALatch_CLKinputPMOSFinger2=None,  # 3
        _Comp_SALatch_PMOSFinger=None,  # 3
        _Comp_SALatch_PMOSChannelWidth=None,  # 500
        _Comp_SALatch_DATAinputNMOSFinger=None,  # 12
        _Comp_SALatch_NMOSFinger=None,  # 2
        _Comp_SALatch_CLKinputNMOSFinger=None,  # 8
        _Comp_SALatch_NMOSChannelWidth=None,  # 500
        _Comp_SALatch_CLKinputNMOSChannelWidth=None,  # 800
        _Comp_SALatch_ChannelLength=None,  # 30
        _Comp_SALatch_Dummy=True,
        _Comp_SALatch_XVT=None,
        _Comp_SALatch_GuardringWidth=None,
        _Comp_SALatch_Guardring=True,
        _Comp_SALatch_SlicerGuardringWidth=None,
        _Comp_SALatch_SlicerGuardring=None,
        _Comp_SALatch_NumSupplyCOY=None,
        _Comp_SALatch_NumSupplyCOX=None,
        _Comp_SALatch_SupplyMet1XWidth=None,
        _Comp_SALatch_SupplyMet1YWidth=None,
        _Comp_SALatch_VDD2VSSHeight=None,
        _Comp_SALatch_NumVIAPoly2Met1COX=None,
        _Comp_SALatch_NumVIAPoly2Met1COY=None,
        _Comp_SALatch_NumVIAMet12COX=None,
        _Comp_SALatch_NumVIAMet12COY=None,
        _Comp_SALatch_PowerLine=False,

        ## StrongARMLatch Output Buffer Sizing
        # Inverter1
        _Comp_SAOutBuf_Inv1_NMOS_ChannelWidth=None,  # Number
        _Comp_SAOutBuf_Inv1_NMOS_ChannelLength=None,  # Number
        _Comp_SAOutBuf_Inv1_NMOS_NumberofGate=None,  # Number
        _Comp_SAOutBuf_Inv1_NMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_SAOutBuf_Inv1_NMOS_POGate_Comb_length=None,  # None/Number

        _Comp_SAOutBuf_Inv1_PMOS_ChannelWidth=None,  # Number
        _Comp_SAOutBuf_Inv1_PMOS_ChannelLength=None,  # Number
        _Comp_SAOutBuf_Inv1_PMOS_NumberofGate=None,  # Number
        _Comp_SAOutBuf_Inv1_PMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_SAOutBuf_Inv1_PMOS_POGate_Comb_length=None,  # None/Number

        # Inverter2
        _Comp_SAOutBuf_Inv2_NMOS_ChannelWidth=None,  # Number
        _Comp_SAOutBuf_Inv2_NMOS_ChannelLength=None,  # Number
        _Comp_SAOutBuf_Inv2_NMOS_NumberofGate=None,  # Number
        _Comp_SAOutBuf_Inv2_NMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_SAOutBuf_Inv2_NMOS_POGate_Comb_length=None,  # None/Number

        _Comp_SAOutBuf_Inv2_PMOS_ChannelWidth=None,  # Number
        _Comp_SAOutBuf_Inv2_PMOS_ChannelLength=None,  # Number
        _Comp_SAOutBuf_Inv2_PMOS_NumberofGate=None,  # Number
        _Comp_SAOutBuf_Inv2_PMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_SAOutBuf_Inv2_PMOS_POGate_Comb_length=None,  # None/Number

        ## SR Latch Sizing
        _Comp_SRLatch_NAND_NMOS_ChannelWidth=None,  # Number
        _Comp_SRLatch_NAND_NMOS_ChannelLength=None,  # Number
        _Comp_SRLatch_NAND_NMOS_NumberofGate=None,  # Number
        _Comp_SRLatch_NAND_NMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_SRLatch_NAND_NMOS_POGate_Comb_length=None,  # None/Number

        _Comp_SRLatch_NAND_PMOS_ChannelWidth=None,  # Number
        _Comp_SRLatch_NAND_PMOS_ChannelLength=None,  # Number
        _Comp_SRLatch_NAND_PMOS_NumberofGate=None,  # Number
        _Comp_SRLatch_NAND_PMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_SRLatch_NAND_PMOS_POGate_Comb_length=None,  # None/Number

        # CLK Input Logic Gates
        _Comp_CLKSamp_Inv_NMOS_ChannelWidth=None,
        _Comp_CLKSamp_Inv_NMOS_ChannelLength=None,
        _Comp_CLKSamp_Inv_NMOS_NumberofGate=None,
        _Comp_CLKSamp_Inv_NMOS_XVT=None,
        _Comp_CLKSamp_Inv_NMOS_POGate_Comb_length=None,

        _Comp_CLKSamp_Inv_PMOS_ChannelWidth=None,
        _Comp_CLKSamp_Inv_PMOS_ChannelLength=None,
        _Comp_CLKSamp_Inv_PMOS_NumberofGate=None,
        _Comp_CLKSamp_Inv_PMOS_XVT=None,
        _Comp_CLKSamp_Inv_PMOS_POGate_Comb_length=None,

        _Comp_CLKSrc_Inv_NMOS_ChannelWidth=None,
        _Comp_CLKSrc_Inv_NMOS_ChannelLength=None,
        _Comp_CLKSrc_Inv_NMOS_NumberofGate=None,
        _Comp_CLKSrc_Inv_NMOS_XVT=None,
        _Comp_CLKSrc_Inv_NMOS_POGate_Comb_length=None,

        _Comp_CLKSrc_Inv_PMOS_ChannelWidth=None,
        _Comp_CLKSrc_Inv_PMOS_ChannelLength=None,
        _Comp_CLKSrc_Inv_PMOS_NumberofGate=None,
        _Comp_CLKSrc_Inv_PMOS_XVT=None,
        _Comp_CLKSrc_Inv_PMOS_POGate_Comb_length=None,

        ## CLKSrc & CLKSample AND Gate
        _Comp_AND_NAND_NMOS_ChannelWidth=None,
        _Comp_AND_NAND_NMOS_ChannelLength=None,
        _Comp_AND_NAND_NMOS_NumberofGate=None,
        _Comp_AND_NAND_NMOS_XVT=None,

        _Comp_AND_NAND_PMOS_ChannelWidth=None,
        _Comp_AND_NAND_PMOS_ChannelLength=None,
        _Comp_AND_NAND_PMOS_NumberofGate=None,
        _Comp_AND_NAND_PMOS_XVT=None,

        _Comp_AND_Inv_NMOS_ChannelWidth=None,
        _Comp_AND_Inv_NMOS_ChannelLength=None,
        _Comp_AND_Inv_NMOS_NumberofGate=None,
        _Comp_AND_Inv_NMOS_XVT=None,
        _Comp_AND_Inv_NMOS_POGate_Comb_length=None,

        _Comp_AND_Inv_PMOS_ChannelWidth=None,
        _Comp_AND_Inv_PMOS_ChannelLength=None,
        _Comp_AND_Inv_PMOS_NumberofGate=None,
        _Comp_AND_Inv_PMOS_XVT=None,
        _Comp_AND_Inv_PMOS_POGate_Comb_length=None,

        ## CLK Buffer
        # Inverter1
        _Comp_CLKBuf_Inv1_NMOS_ChannelWidth=None,  # Number
        _Comp_CLKBuf_Inv1_NMOS_ChannelLength=None,  # Number
        _Comp_CLKBuf_Inv1_NMOS_NumberofGate=None,  # Number
        _Comp_CLKBuf_Inv1_NMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_CLKBuf_Inv1_NMOS_POGate_Comb_length=None,  # None/Number

        _Comp_CLKBuf_Inv1_PMOS_ChannelWidth=None,  # Number
        _Comp_CLKBuf_Inv1_PMOS_ChannelLength=None,  # Number
        _Comp_CLKBuf_Inv1_PMOS_NumberofGate=None,  # Number
        _Comp_CLKBuf_Inv1_PMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_CLKBuf_Inv1_PMOS_POGate_Comb_length=None,  # None/Number

        # Inverter2
        _Comp_CLKBuf_Inv2_NMOS_ChannelWidth=None,  # Number
        _Comp_CLKBuf_Inv2_NMOS_ChannelLength=None,  # Number
        _Comp_CLKBuf_Inv2_NMOS_NumberofGate=None,  # Number
        _Comp_CLKBuf_Inv2_NMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_CLKBuf_Inv2_NMOS_POGate_Comb_length=None,  # None/Number

        _Comp_CLKBuf_Inv2_PMOS_ChannelWidth=None,  # Number
        _Comp_CLKBuf_Inv2_PMOS_ChannelLength=None,  # Number
        _Comp_CLKBuf_Inv2_PMOS_NumberofGate=None,  # Number
        _Comp_CLKBuf_Inv2_PMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_CLKBuf_Inv2_PMOS_POGate_Comb_length=None,  # None/Number

        # PowerRail Placement
        _Comp_BufSR_NMOS_Pbody_NumCont=None,
        _Comp_BufSR_NMOS_Pbody_XvtTop2Pbody=None,
        _Comp_BufSR_PMOS_Nbody_NumCont=None,
        _Comp_BufSR_PMOS_Nbody_Xvtdown2Nbody=None,
        _Comp_BufSR_PMOSXvt2NMOSXvt=None,

        _Comp_CLKInLogic_NMOS_Pbody_Xvtdown2Pbody=None,
        _Comp_CLKInLogic_PMOS_Nbody_NumCont=None,
        _Comp_CLKInLogic_PMOS_Nbody_Xvtdown2Nbody=None,
        _Comp_CLKInLogic_PMOSXvt2NMOSXvt=None,

        # Additional Buffer Between CLK_Sample Input of Comparator And Output of Tree Buffer
        ## InvChain Common
        _Buf_CLKSamp_Pbody_NumCont=2,  # number
        _Buf_CLKSamp_Nbody_NumCont=2,  # number
        _Buf_CLKSamp_PMOSXvt2NMOSXvt=500,  # number
        _Buf_CLKSamp_XvtTop2Pbody=None,  # number/None(Minimum)
        _Buf_CLKSamp_Xvtdown2Nbody=None,  # number/None(Minimum)

        ## Inverter Chain
        ## Inv1 common
        _Buf_CLKSamp_NumberofGate=[2, 4, 6],  # Vector
        _Buf_CLKSamp_ChannelLength=30,  # Scalar
        _Buf_CLKSamp_XVT='SLVT',  # 'SLVT'

        ## Inv1 NMOS
        _Buf_CLKSamp_Inv_NMOS_ChannelWidth=200,  # Scalar
        _Buf_CLKSamp_Inv_NMOS_POGate_Comb_length=100,  # Scalar

        ## Inv1 PMOS
        _Buf_CLKSamp_Inv_PMOS_ChannelWidth=400,  # Scalar
        _Buf_CLKSamp_Inv_PMOS_POGate_Comb_length=100,  # Scalar

        # Additional Buffer Between CLK_Source Input of Comparator And Output of Tree Buffer
        ## InvChain Common
        _Buf_CLKSrc_Pbody_NumCont=2,  # number
        _Buf_CLKSrc_Nbody_NumCont=2,  # number
        _Buf_CLKSrc_PMOSXvt2NMOSXvt=500,  # number
        _Buf_CLKSrc_XvtTop2Pbody=None,  # number/None(Minimum)
        _Buf_CLKSrc_Xvtdown2Nbody=None,  # number/None(Minimum)

        ## Inverter Chain
        ## Inv1 common
        _Buf_CLKSrc_NumberofGate=[2, 4, 6],  # Vector
        _Buf_CLKSrc_ChannelLength=30,  # Scalar
        _Buf_CLKSrc_XVT='SLVT',  # 'SLVT'

        ## Inv1 NMOS
        _Buf_CLKSrc_Inv_NMOS_ChannelWidth=200,  # Scalar
        _Buf_CLKSrc_Inv_NMOS_POGate_Comb_length=100,  # Scalar

        ## Inv1 PMOS
        _Buf_CLKSrc_Inv_PMOS_ChannelWidth=400,  # Scalar
        _Buf_CLKSrc_Inv_PMOS_POGate_Comb_length=100,  # Scalar

        # Additional Buffer Between Output of Comparator  And Input of Tree Buffer
        ## InvChain Common
        _Buf_CompOut_Pbody_NumCont=2,  # number
        _Buf_CompOut_Nbody_NumCont=2,  # number
        _Buf_CompOut_PMOSXvt2NMOSXvt=500,  # number
        _Buf_CompOut_XvtTop2Pbody=None,  # number/None(Minimum)
        _Buf_CompOut_Xvtdown2Nbody=None,  # number/None(Minimum)

        ## Inv1 common
        _Buf_CompOut_NumberofGate=[2, 4, 6],  # Vector
        _Buf_CompOut_ChannelLength=30,  # Scalar
        _Buf_CompOut_XVT='SLVT',  # 'SLVT'

        ## Inv1 NMOS
        _Buf_CompOut_Inv_NMOS_ChannelWidth=200,  # Scalar
        _Buf_CompOut_Inv_NMOS_POGate_Comb_length=100,  # Scalar

        ## Inv1 PMOS
        _Buf_CompOut_Inv_PMOS_ChannelWidth=400,  # Scalar
        _Buf_CompOut_Inv_PMOS_POGate_Comb_length=100,  # Scalar

        # # Additional Buffer Between Output of CLKDout  And Input of Tree Buffer
        # ## Inv1 common
        # _Buf_CLKDout_NumberofGate=[2, 4, 6],  # Vector
        # _Buf_CLKDout_ChannelLength=30,  # Scalar
        # _Buf_CLKDout_XVT='SLVT',  # 'SLVT'
        #
        # ## Inv1 NMOS
        # _Buf_CLKDout_Inv_NMOS_ChannelWidth=200,  # Scalar
        # _Buf_CLKDout_Inv_NMOS_POGate_Comb_length=100,  # Scalar
        #
        # ## Inv1 PMOS
        # _Buf_CLKDout_Inv_PMOS_ChannelWidth=400,  # Scalar
        # _Buf_CLKDout_Inv_PMOS_POGate_Comb_length=100,  # Scalar

        # # Element CDAC
        _CDAC_LayoutOption=[5, 6],
        _CDAC_ShieldingLayer=2,  # Poly:0, M1:1, M2:2 ...
        _CDAC_MetalWidth=50,
        _CDAC_MetalLength=5840,  # (8bit size: 1414/ 10bit size: 2800/ 12bit size: 4200)
        _CDAC_MetalSpacing=50,

        # #Unit Cap
        _CDAC_NumOfElement=1,

        # # Shielding & Top Connect node
        _CDAC_ConnectLength=400,
        _CDAC_ExtendLength=400,

        # # Dummy Cap Option
        _CDAC_DummyCap_TopBottomShort=False,  # False -> Bottom = GND
        _CDAC_NumOfDummyCaps=3,  # Number of dummy cap(one side)

        # # CommonCentroid With Driving node
        _CDAC_CapArrayWDrivingNodeDistance=300,  # DRC Rule
        _CDAC_DriveNodeDistance=254,  #
        _CDAC_YWidth_Bottom_Hrz=50,

        # Driver Sizing
        _Driver_SizeByBit=[32, 16, 8, 4, 2],

        # Driver(Inverter) NMOS
        _Driver_NMOS_NumberofGate=1,  # number
        _Driver_NMOS_ChannelWidth=340,  # number (8bit size: 340/ 10bit size: 680/ 12bit size: 1020)
        _Driver_NMOS_Channellength=30,  # number
        _Driver_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT

        # Driver(Inverter) PMOS
        _Driver_PMOS_NumberofGate=1,  # number
        _Driver_PMOS_ChannelWidth=900,  # number (8bit size: 900/ 10bit size: 1800/ 12bit size: 2700)
        _Driver_PMOS_Channellength=30,  # number
        _Driver_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT

        # Tr1 and Tr2
        # Tr1
        _Samp_Tr1Tr2_Tr1_NMOSNumberofGate=None,  # number
        _Samp_Tr1Tr2_Tr1_NMOSChannelWidth=None,  # number
        _Samp_Tr1Tr2_Tr1_NMOSChannellength=None,  # number
        _Samp_Tr1Tr2_Tr1_GateSpacing=None,  # None/number
        _Samp_Tr1Tr2_Tr1_SDWidth=None,  # None/number
        _Samp_Tr1Tr2_Tr1_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Samp_Tr1Tr2_Tr1_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _Samp_Tr1Tr2_Tr1_Source_Via_TF=False,  # True/False

        # Drain_node_ViaM1M2
        _Samp_Tr1Tr2_Tr1_Drain_Via_TF=False,  # True/False

        # POLY dummy setting
        _Samp_Tr1Tr2_Tr1_NMOSDummy=None,  # TF
        # if _PMOSDummy == True
        _Samp_Tr1Tr2_Tr1_NMOSDummy_length=None,  # None/Value
        _Samp_Tr1Tr2_Tr1_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr2
        _Samp_Tr1Tr2_Tr2_NMOSNumberofGate=None,  # number
        _Samp_Tr1Tr2_Tr2_NMOSChannelWidth=None,  # number
        _Samp_Tr1Tr2_Tr2_NMOSChannellength=None,  # number
        _Samp_Tr1Tr2_Tr2_GateSpacing=None,  # None/number
        _Samp_Tr1Tr2_Tr2_SDWidth=None,  # None/number
        _Samp_Tr1Tr2_Tr2_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Samp_Tr1Tr2_Tr2_PCCrit=None,  # None/True

        # Source_node_ViaM1M2
        _Samp_Tr1Tr2_Tr2_Source_Via_TF=False,  # True/False

        # Drain_node_ViaM1M2
        _Samp_Tr1Tr2_Tr2_Drain_Via_TF=False,  # True/False

        # POLY dummy setting
        _Samp_Tr1Tr2_Tr2_NMOSDummy=None,  # TF
        # if _PMOSDummy == True
        _Samp_Tr1Tr2_Tr2_NMOSDummy_length=None,  # None/Value
        _Samp_Tr1Tr2_Tr2_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Input/Output node
        # INPUT node
        _Samp_Tr1Tr2_Inputnode_Metal_layer=None,  # number
        _Samp_Tr1Tr2_Inputnode_width=None,  # number

        # OUTPUT node
        _Samp_Tr1Tr2_Outputnode_Metal_layer=None,  # number
        _Samp_Tr1Tr2_Outputnode_width=None,  # number

        # Guardring
        # Pbody: number of contact
        # Nbody
        _Samp_Tr1Tr2_NwellWidth=None,  # number

        # Tr4
        _Samp_Tr4_NMOSNumberofGate=None,  # number
        _Samp_Tr4_NMOSChannelWidth=None,  # number
        _Samp_Tr4_NMOSChannellength=None,  # number
        _Samp_Tr4_GateSpacing=None,  # None/number
        _Samp_Tr4_SDWidth=None,  # None/number
        _Samp_Tr4_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Samp_Tr4_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _Samp_Tr4_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _Samp_Tr4_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _Samp_Tr4_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tr4_NMOSDummy_length=None,  # None/Value
        _Samp_Tr4_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr5 Tr7 Tr9
        # PMOS: Tr5
        _Samp_Tr5_PMOSNumberofGate=None,
        _Samp_Tr5_PMOSChannelWidth=None,  # ref=1000
        _Samp_Tr5_PMOSChannellength=None,
        _Samp_Tr5_GateSpacing=None,
        _Samp_Tr5_SDWidth=None,
        _Samp_Tr5_XVT='SLVT',
        _Samp_Tr5_PCCrit=None,

        # Source_node_ViaM1M2
        _Samp_Tr5_Source_Via_TF=True,

        # Drain_node_ViaM1M2
        _Samp_Tr5_Drain_Via_TF=True,

        # POLY dummy setting
        _Samp_Tr5_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tr5_PMOSDummy_length=None,  # None/Value
        _Samp_Tr5_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # PMOS: Tr7
        _Samp_Tr7_PMOSNumberofGate=None,
        _Samp_Tr7_PMOSChannelWidth=None,
        _Samp_Tr7_PMOSChannellength=None,
        _Samp_Tr7_GateSpacing=None,
        _Samp_Tr7_SDWidth=None,
        _Samp_Tr7_XVT='SLVT',
        _Samp_Tr7_PCCrit=None,

        # Source_node_ViaM1M2
        _Samp_Tr7_Source_Via_TF=True,

        # Drain_node_ViaM1M2
        _Samp_Tr7_Drain_Via_TF=True,

        # POLY dummy setting
        _Samp_Tr7_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tr7_PMOSDummy_length=None,  # None/Value
        _Samp_Tr7_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # PMOS: Tr9
        _Samp_Tr9_PMOSNumberofGate=None,
        _Samp_Tr9_PMOSChannelWidth=None,  # ref = 1000
        _Samp_Tr9_PMOSChannellength=None,
        _Samp_Tr9_GateSpacing=None,
        _Samp_Tr9_SDWidth=None,
        _Samp_Tr9_XVT='SLVT',
        _Samp_Tr9_PCCrit=None,

        # Source_node_ViaM1M2
        _Samp_Tr9_Source_Via_TF=True,

        # Drain_node_ViaM1M2
        _Samp_Tr9_Drain_Via_TF=True,

        # POLY dummy setting
        _Samp_Tr9_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tr9_PMOSDummy_length=None,  # None/Value
        _Samp_Tr9_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr8
        _Samp_Tr8_NMOSNumberofGate=None,  # number (ref:4)
        _Samp_Tr8_NMOSChannelWidth=None,  # number (ref:500)
        _Samp_Tr8_NMOSChannellength=None,  # number (ref:30)
        _Samp_Tr8_GateSpacing=None,  # None/number
        _Samp_Tr8_SDWidth=None,  # None/number
        _Samp_Tr8_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Samp_Tr8_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _Samp_Tr8_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _Samp_Tr8_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _Samp_Tr8_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tr8_NMOSDummy_length=None,  # None/Value
        _Samp_Tr8_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        ## Tr6
        _Samp_Tr6_NMOSNumberofGate=None,  # number
        _Samp_Tr6_NMOSChannelWidth=None,  # number
        _Samp_Tr6_NMOSChannellength=None,  # number
        _Samp_Tr6_GateSpacing=None,  # None/number
        _Samp_Tr6_SDWidth=None,  # None/number
        _Samp_Tr6_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Samp_Tr6_PCCrit=True,  # None/True

        # Tr6 Source_node_ViaM1M2
        _Samp_Tr6_Source_Via_TF=False,  # True/False

        # Tr6 Drain_node_ViaM1M2
        _Samp_Tr6_Drain_Via_TF=False,  # True/False

        # Tr6 POLY dummy setting
        _Samp_Tr6_NMOSDummy=True,  # TF
        # Tr6 if _PMOSDummy == True
        _Samp_Tr6_NMOSDummy_length=None,  # None/Value
        _Samp_Tr6_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr6 Vp node
        _Samp_Tr6_Vp_node_width=None,  # Number
        _Samp_Tr6_Vp_node_metal_Layer=None,  # number

        # Tr6 Guardring
        # Pbody: number of contact
        # Nbody
        _Samp_Tr6_NwellWidth=None,  # number

        # PMOS: Tr11
        _Samp_Tr11_PMOSNumberofGate=None,
        _Samp_Tr11_PMOSChannelWidth=None,
        _Samp_Tr11_PMOSChannellength=None,
        _Samp_Tr11_GateSpacing=None,
        _Samp_Tr11_SDWidth=None,
        _Samp_Tr11_XVT='SLVT',
        _Samp_Tr11_PCCrit=None,

        # Source_node_ViaM1M2
        _Samp_Tr11_Source_Via_TF=True,

        # Drain_node_ViaM1M2
        _Samp_Tr11_Drain_Via_TF=True,

        # POLY dummy setting
        _Samp_Tr11_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tr11_PMOSDummy_length=None,  # None/Value
        _Samp_Tr11_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Nbodyring(Guardring)
        _Samp_Tr11_Guardring_NumCont=None,  # number

        ## VddTieCell4
        # VddTieCell4 NMOS
        _Samp_Tie4N_NMOSNumberofGate=None,  # number
        _Samp_Tie4N_NMOSChannelWidth=None,  # number
        _Samp_Tie4N_NMOSChannellength=None,  # number
        _Samp_Tie4N_GateSpacing=None,  # None/number
        _Samp_Tie4N_SDWidth=None,  # None/number
        _Samp_Tie4N_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Samp_Tie4N_PCCrit=True,  # None/True

        # VddTieCell4 Source_node_ViaM1M2
        _Samp_Tie4N_Source_Via_TF=False,  # True/False

        # VddTieCell4 Drain_node_ViaM1M2
        _Samp_Tie4N_Drain_Via_TF=False,  # True/False

        # POLY dummy setting
        _Samp_Tie4N_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tie4N_NMOSDummy_length=None,  # None/Value
        _Samp_Tie4N_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # VddTieCell4 PMOS
        _Samp_Tie4P_PMOSNumberofGate=None,  # number
        _Samp_Tie4P_PMOSChannelWidth=None,  # number
        _Samp_Tie4P_PMOSChannellength=None,  # number
        _Samp_Tie4P_GateSpacing=None,  # None/number
        _Samp_Tie4P_SDWidth=None,  # None/number
        _Samp_Tie4P_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Samp_Tie4P_PCCrit=True,  # None/True

        # VddTieCell4 PMOS Source_node_ViaM1M2
        _Samp_Tie4P_Source_Via_TF=False,  # True/False

        # VddTieCell4 PMOS Drain_node_ViaM1M2
        _Samp_Tie4P_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _Samp_Tie4P_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tie4P_PMOSDummy_length=None,  # None/Value
        _Samp_Tie4P_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # VddTieCell4 Number of Body Contact
        _Samp_Tie4_NBodyCOX=None,
        _Samp_Tie4_NBodyCOY=None,
        _Samp_Tie4_PBodyCOX=None,
        _Samp_Tie4_PBodyCOY=None,

        ## VddTieCell8
        # VddTieCell8 NMOS
        _Samp_Tie8N_NMOSNumberofGate=None,  # number
        _Samp_Tie8N_NMOSChannelWidth=None,  # number
        _Samp_Tie8N_NMOSChannellength=None,  # number
        _Samp_Tie8N_GateSpacing=None,  # None/number
        _Samp_Tie8N_SDWidth=None,  # None/number
        _Samp_Tie8N_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Samp_Tie8N_PCCrit=True,  # None/True

        # VddTieCell8 Source_node_ViaM1M2
        _Samp_Tie8N_Source_Via_TF=False,  # True/False

        # VddTieCell8 Drain_node_ViaM1M2
        _Samp_Tie8N_Drain_Via_TF=False,  # True/False

        # POLY dummy setting
        _Samp_Tie8N_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tie8N_NMOSDummy_length=None,  # None/Value
        _Samp_Tie8N_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # VddTieCell8 PMOS
        _Samp_Tie8P_PMOSNumberofGate=None,  # number
        _Samp_Tie8P_PMOSChannelWidth=None,  # number
        _Samp_Tie8P_PMOSChannellength=None,  # number
        _Samp_Tie8P_GateSpacing=None,  # None/number
        _Samp_Tie8P_SDWidth=None,  # None/number
        _Samp_Tie8P_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Samp_Tie8P_PCCrit=True,  # None/True

        # VddTieCell8 PMOS Source_node_ViaM1M2
        _Samp_Tie8P_Source_Via_TF=False,  # True/False

        # VddTieCell8 PMOS Drain_node_ViaM1M2
        _Samp_Tie8P_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _Samp_Tie8P_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tie8P_PMOSDummy_length=None,  # None/Value
        _Samp_Tie8P_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # VddTieCell8 Number of Body Contact
        _Samp_Tie8_NBodyCOX=None,
        _Samp_Tie8_NBodyCOY=None,
        _Samp_Tie8_PBodyCOX=None,
        _Samp_Tie8_PBodyCOY=None,

        # Tr12
        _Samp_Tr12_NMOSNumberofGate=None,  # number
        _Samp_Tr12_NMOSChannelWidth=None,  # number
        _Samp_Tr12_NMOSChannellength=None,  # number
        _Samp_Tr12_GateSpacing=None,  # None/number
        _Samp_Tr12_SDWidth=None,  # None/number
        _Samp_Tr12_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Samp_Tr12_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _Samp_Tr12_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _Samp_Tr12_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _Samp_Tr12_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tr12_NMOSDummy_length=None,  # None/Value
        _Samp_Tr12_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr3
        _Samp_Tr3_NMOSNumberofGate=None,  # number
        _Samp_Tr3_NMOSChannelWidth=None,  # number
        _Samp_Tr3_NMOSChannellength=None,  # number
        _Samp_Tr3_GateSpacing=None,  # None/number
        _Samp_Tr3_SDWidth=None,  # None/number
        _Samp_Tr3_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Samp_Tr3_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _Samp_Tr3_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _Samp_Tr3_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _Samp_Tr3_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tr3_NMOSDummy_length=None,  # None/Value
        _Samp_Tr3_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr10
        _Samp_Tr10_NMOSNumberofGate=None,  # number
        _Samp_Tr10_NMOSChannelWidth=None,  # number
        _Samp_Tr10_NMOSChannellength=None,  # number
        _Samp_Tr10_GateSpacing=None,  # None/number
        _Samp_Tr10_SDWidth=None,  # None/number
        _Samp_Tr10_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Samp_Tr10_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _Samp_Tr10_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _Samp_Tr10_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _Samp_Tr10_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tr10_NMOSDummy_length=None,  # None/Value
        _Samp_Tr10_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr12Tr3Tr10 Guardring
        _Samp_Tr12Tr3Tr10_Guardring_NumCont=3,  # Number

        # HDVNCAP_Array
        _Samp_HDVNCAP_Length=None,
        _Samp_HDVNCAP_LayoutOption=None,
        _Samp_HDVNCAP_NumFigPair=None,
        _Samp_HDVNCAP_Array=None,  # number: 1xnumber
        _Samp_HDVNCAP_Cbot_Ctop_metalwidth=None,  # number

        ## BootStrapped Sampler CLKB Inverter
        _CLKBInv_NMOS_NumberofGate=32,
        _CLKBInv_NMOS_ChannelWidth=400,
        _CLKBInv_NMOS_ChannelLength=30,
        _CLKBInv_NMOS_XVT='SLVT',
        _CLKBInv_NMOS_POGate_Comb_length=None,

        _CLKBInv_PMOS_NumberofGate=32,
        _CLKBInv_Inv_PMOS_ChannelWidth=800,
        _CLKBInv_PMOS_ChannelLength=30,
        _CLKBInv_PMOS_XVT='SLVT',
        _CLKBInv_PMOS_POGate_Comb_length=None,

        _CLKBInv_Pbody_NumCont=2,
        _CLKBInv_XvtTop2Pbody=None,
        _CLKBInv_Nbody_NumCont=2,
        _CLKBInv_Xvtdown2Nbody=None,
        _CLKBInv_PMOSXvt2NMOSXvt=None,
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
                                  _NumofBit=None,
                                  _CDAC_Folding=None,  # None/True/False
                                  _Driver_DecimationIfDriverPlacedInCommonCentroid=True,
                                  _Driver_DecimationFactor=[2, 0, 0, 0, 0, 0, 0],  # [MSB, MSB-1 ... MSB-x]: 단 X<MSB  # 위 옵션 True시 작동; MSB부터 벡터로 작성; [3,2,2] 시 MSB0 -> 3:1, MSB1 -> 2:1, MSB2 -> 2:1, ... 1은 불가
                                  _SpaceBtwBootSWPosNeg=None,

                                  _Test_distance=330,
                                  _Routing_width=50,
                                  _Routing_distance=80,

                                  _SARLogic_YWidthOfCLKSrc=100,
                                  _SARLogic_SpaceBtwCLKSrcAndCLKSamp=100,
                                  _SARLogic_YWidthOfCLKSamp=100,

                                  _SARLogic_YWidthOfCompOut=100,
                                  _SARLogic_SpaceBtwCompOutAndCLKDout=100,
                                  _SARLogic_YWidthOfCLKDout=100,

                                  ## DFF Common
                                  _SARLogic_DFF_Pbody_NumCont=2,  # number
                                  _SARLogic_DFF_Nbody_NumCont=2,  # number
                                  _SARLogic_DFF_PMOSXvt2NMOSXvt=1150,  # number
                                  _SARLogic_DFF_XvtTop2Pbody=None,  # number/None(Minimum)
                                  _SARLogic_DFF_Xvtdown2Nbody=None,  # number/None(Minimum)

                                  ## Master Xgate1
                                  ## Xgate common

                                  ## Xgate NMOS
                                  _SARLogic_Mst_Xgate1_NMOS_NumberofGate=1,  # 1
                                  _SARLogic_Mst_Xgate1_NMOS_ChannelWidth=200,  # 100
                                  _SARLogic_Mst_Xgate1_NMOS_ChannelLength=30,
                                  _SARLogic_Mst_Xgate1_NMOS_XVT='HVT',
                                  _SARLogic_Mst_Xgate1_NMOS_POGate_Comb_length=100,

                                  ## Xgate PMOS
                                  _SARLogic_Mst_Xgate1_PMOS_NumberofGate=1,  # 1
                                  _SARLogic_Mst_Xgate1_PMOS_ChannelWidth=400,  # 200
                                  _SARLogic_Mst_Xgate1_PMOS_ChannelLength=30,
                                  _SARLogic_Mst_Xgate1_PMOS_XVT='HVT',
                                  _SARLogic_Mst_Xgate1_PMOS_POGate_Comb_length=100,

                                  ## Master Xgate2
                                  ## Xgate common

                                  ## Xgate NMOS
                                  _SARLogic_Mst_Xgate2_NMOS_NumberofGate=1,
                                  _SARLogic_Mst_Xgate2_NMOS_ChannelWidth=200,
                                  _SARLogic_Mst_Xgate2_NMOS_ChannelLength=30,
                                  _SARLogic_Mst_Xgate2_NMOS_XVT='SLVT',
                                  _SARLogic_Mst_Xgate2_NMOS_POGate_Comb_length=100,

                                  ## Xgate PMOS
                                  _SARLogic_Mst_Xgate2_PMOS_NumberofGate=2,  # 2
                                  _SARLogic_Mst_Xgate2_PMOS_ChannelWidth=200,
                                  _SARLogic_Mst_Xgate2_PMOS_ChannelLength=30,
                                  _SARLogic_Mst_Xgate2_PMOS_XVT='SLVT',
                                  _SARLogic_Mst_Xgate2_PMOS_POGate_Comb_length=100,

                                  ## Master Nor1
                                  ## Nor1 common

                                  ## NMOS
                                  ## NMOS common
                                  _SARLogic_Mst_Nor1_NMOS_XVT='HVT',

                                  ## NMOSA
                                  _SARLogic_Mst_Nor1_NMOSA_NumberofGate=2,
                                  _SARLogic_Mst_Nor1_NMOSA_ChannelWidth=200,
                                  _SARLogic_Mst_Nor1_NMOSA_ChannelLength=30,
                                  _SARLogic_Mst_Nor1_NMOSA_POGate_Comb_length=100,

                                  ## NMOSB
                                  _SARLogic_Mst_Nor1_NMOSB_NumberofGate=2,
                                  _SARLogic_Mst_Nor1_NMOSB_ChannelWidth=200,
                                  _SARLogic_Mst_Nor1_NMOSB_ChannelLength=30,
                                  _SARLogic_Mst_Nor1_NMOSB_POGate_Comb_length=100,

                                  ## PMOS
                                  ## PMOS common
                                  _SARLogic_Mst_Nor1_PMOS_XVT='HVT',

                                  ## PMOSA
                                  _SARLogic_Mst_Nor1_PMOSA_NumberofGate=4,
                                  _SARLogic_Mst_Nor1_PMOSA_ChannelWidth=400,
                                  _SARLogic_Mst_Nor1_PMOSA_ChannelLength=30,
                                  _SARLogic_Mst_Nor1_PMOSA_POGate_Comb_length=100,

                                  ## PMOSB
                                  _SARLogic_Mst_Nor1_PMOSB_NumberofGate=4,
                                  _SARLogic_Mst_Nor1_PMOSB_ChannelWidth=400,
                                  _SARLogic_Mst_Nor1_PMOSB_ChannelLength=30,
                                  _SARLogic_Mst_Nor1_PMOSB_POGate_Comb_length=100,

                                  ## Master Nor2
                                  ## Nor2 common

                                  ## NMOS
                                  ## NMOS common
                                  _SARLogic_Mst_Nor2_NMOS_XVT='HVT',

                                  ## NMOSA
                                  _SARLogic_Mst_Nor2_NMOSA_NumberofGate=2,
                                  _SARLogic_Mst_Nor2_NMOSA_ChannelWidth=200,
                                  _SARLogic_Mst_Nor2_NMOSA_ChannelLength=30,
                                  _SARLogic_Mst_Nor2_NMOSA_POGate_Comb_length=100,

                                  ## NMOSB
                                  _SARLogic_Mst_Nor2_NMOSB_NumberofGate=2,
                                  _SARLogic_Mst_Nor2_NMOSB_ChannelWidth=200,
                                  _SARLogic_Mst_Nor2_NMOSB_ChannelLength=30,
                                  _SARLogic_Mst_Nor2_NMOSB_POGate_Comb_length=100,

                                  ## PMOS
                                  ## PMOS common
                                  _SARLogic_Mst_Nor2_PMOS_XVT='HVT',

                                  ## PMOSA
                                  _SARLogic_Mst_Nor2_PMOSA_NumberofGate=4,
                                  _SARLogic_Mst_Nor2_PMOSA_ChannelWidth=400,
                                  _SARLogic_Mst_Nor2_PMOSA_ChannelLength=30,
                                  _SARLogic_Mst_Nor2_PMOSA_POGate_Comb_length=100,

                                  ## PMOSB
                                  _SARLogic_Mst_Nor2_PMOSB_NumberofGate=4,
                                  _SARLogic_Mst_Nor2_PMOSB_ChannelWidth=400,
                                  _SARLogic_Mst_Nor2_PMOSB_ChannelLength=30,
                                  _SARLogic_Mst_Nor2_PMOSB_POGate_Comb_length=100,

                                  ## Master Inv1 : Set pre-driver
                                  ## Inv1 common

                                  ## Inv1 NMOS
                                  _SARLogic_Mst_Inv1_NMOS_NumberofGate=1,
                                  _SARLogic_Mst_Inv1_NMOS_ChannelWidth=200,
                                  _SARLogic_Mst_Inv1_NMOS_ChannelLength=30,
                                  _SARLogic_Mst_Inv1_NMOS_XVT='SLVT',
                                  _SARLogic_Mst_Inv1_NMOS_POGate_Comb_length=100,

                                  ## Inv1 PMOS
                                  _SARLogic_Mst_Inv1_PMOS_NumberofGate=1,
                                  _SARLogic_Mst_Inv1_PMOS_ChannelWidth=400,
                                  _SARLogic_Mst_Inv1_PMOS_ChannelLength=30,
                                  _SARLogic_Mst_Inv1_PMOS_XVT='SLVT',
                                  _SARLogic_Mst_Inv1_PMOS_POGate_Comb_length=100,

                                  ## Master Inv2 : Set driver
                                  ## Inv2 common

                                  ## Inv2 NMOS
                                  _SARLogic_Mst_Inv2_NMOS_NumberofGate=1,
                                  _SARLogic_Mst_Inv2_NMOS_ChannelWidth=200,
                                  _SARLogic_Mst_Inv2_NMOS_ChannelLength=30,
                                  _SARLogic_Mst_Inv2_NMOS_XVT='SLVT',
                                  _SARLogic_Mst_Inv2_NMOS_POGate_Comb_length=100,

                                  ## Inv2 PMOS
                                  _SARLogic_Mst_Inv2_PMOS_NumberofGate=1,
                                  _SARLogic_Mst_Inv2_PMOS_ChannelWidth=400,
                                  _SARLogic_Mst_Inv2_PMOS_ChannelLength=30,
                                  _SARLogic_Mst_Inv2_PMOS_XVT='SLVT',
                                  _SARLogic_Mst_Inv2_PMOS_POGate_Comb_length=100,

                                  ## Master Inv3 : Clock driver
                                  ## Inv3 common

                                  ## Inv3 NMOS
                                  _SARLogic_Mst_Inv3_NMOS_NumberofGate=1,
                                  _SARLogic_Mst_Inv3_NMOS_ChannelWidth=200,
                                  _SARLogic_Mst_Inv3_NMOS_ChannelLength=30,
                                  _SARLogic_Mst_Inv3_NMOS_XVT='SLVT',
                                  _SARLogic_Mst_Inv3_NMOS_POGate_Comb_length=100,

                                  ## Inv3 PMOS
                                  _SARLogic_Mst_Inv3_PMOS_NumberofGate=1,
                                  _SARLogic_Mst_Inv3_PMOS_ChannelWidth=400,
                                  _SARLogic_Mst_Inv3_PMOS_ChannelLength=30,
                                  _SARLogic_Mst_Inv3_PMOS_XVT='SLVT',
                                  _SARLogic_Mst_Inv3_PMOS_POGate_Comb_length=100,

                                  ## Slave Xgate1
                                  ## Xgate common

                                  ## Xgate NMOS
                                  _SARLogic_Slv_Xgate1_NMOS_NumberofGate=1,
                                  _SARLogic_Slv_Xgate1_NMOS_ChannelWidth=200,
                                  _SARLogic_Slv_Xgate1_NMOS_ChannelLength=30,
                                  _SARLogic_Slv_Xgate1_NMOS_XVT='HVT',
                                  _SARLogic_Slv_Xgate1_NMOS_POGate_Comb_length=100,

                                  ## Xgate NMOS
                                  _SARLogic_Slv_Xgate1_PMOS_NumberofGate=1,
                                  _SARLogic_Slv_Xgate1_PMOS_ChannelWidth=400,
                                  _SARLogic_Slv_Xgate1_PMOS_ChannelLength=30,
                                  _SARLogic_Slv_Xgate1_PMOS_XVT='HVT',
                                  _SARLogic_Slv_Xgate1_PMOS_POGate_Comb_length=100,

                                  ## Slave Xgate2
                                  ## Xgate common

                                  ## Xgate NMOS
                                  _SARLogic_Slv_Xgate2_NMOS_NumberofGate=1,
                                  _SARLogic_Slv_Xgate2_NMOS_ChannelWidth=200,
                                  _SARLogic_Slv_Xgate2_NMOS_ChannelLength=30,
                                  _SARLogic_Slv_Xgate2_NMOS_XVT='SLVT',
                                  _SARLogic_Slv_Xgate2_NMOS_POGate_Comb_length=100,

                                  ## Xgate NMOS
                                  _SARLogic_Slv_Xgate2_PMOS_NumberofGate=2,
                                  _SARLogic_Slv_Xgate2_PMOS_ChannelWidth=200,
                                  _SARLogic_Slv_Xgate2_PMOS_ChannelLength=30,
                                  _SARLogic_Slv_Xgate2_PMOS_XVT='SLVT',
                                  _SARLogic_Slv_Xgate2_PMOS_POGate_Comb_length=100,

                                  ## Slave Nor1
                                  ## Nor1 common

                                  ## NMOS
                                  ## NMOS common
                                  _SARLogic_Slv_Nor1_NMOS_XVT='HVT',

                                  ## NMOSA
                                  _SARLogic_Slv_Nor1_NMOSA_NumberofGate=2,
                                  _SARLogic_Slv_Nor1_NMOSA_ChannelWidth=200,
                                  _SARLogic_Slv_Nor1_NMOSA_ChannelLength=30,
                                  _SARLogic_Slv_Nor1_NMOSA_POGate_Comb_length=100,

                                  ## NMOSB
                                  _SARLogic_Slv_Nor1_NMOSB_NumberofGate=2,
                                  _SARLogic_Slv_Nor1_NMOSB_ChannelWidth=200,
                                  _SARLogic_Slv_Nor1_NMOSB_ChannelLength=30,
                                  _SARLogic_Slv_Nor1_NMOSB_POGate_Comb_length=100,

                                  ## PMOS
                                  ## PMOS common
                                  _SARLogic_Slv_Nor1_PMOS_XVT='HVT',

                                  ## PMOSA
                                  _SARLogic_Slv_Nor1_PMOSA_NumberofGate=4,
                                  _SARLogic_Slv_Nor1_PMOSA_ChannelWidth=400,
                                  _SARLogic_Slv_Nor1_PMOSA_ChannelLength=30,
                                  _SARLogic_Slv_Nor1_PMOSA_POGate_Comb_length=100,

                                  ## PMOSB
                                  _SARLogic_Slv_Nor1_PMOSB_NumberofGate=4,
                                  _SARLogic_Slv_Nor1_PMOSB_ChannelWidth=400,
                                  _SARLogic_Slv_Nor1_PMOSB_ChannelLength=30,
                                  _SARLogic_Slv_Nor1_PMOSB_POGate_Comb_length=100,

                                  ## Slave Nor2
                                  ## Nor2 common

                                  ## NMOS
                                  ## NMOS common
                                  _SARLogic_Slv_Nor2_NMOS_XVT='HVT',

                                  ## NMOSA
                                  _SARLogic_Slv_Nor2_NMOSA_NumberofGate=2,
                                  _SARLogic_Slv_Nor2_NMOSA_ChannelWidth=200,
                                  _SARLogic_Slv_Nor2_NMOSA_ChannelLength=30,
                                  _SARLogic_Slv_Nor2_NMOSA_POGate_Comb_length=100,

                                  ## NMOSB
                                  _SARLogic_Slv_Nor2_NMOSB_NumberofGate=2,
                                  _SARLogic_Slv_Nor2_NMOSB_ChannelWidth=200,
                                  _SARLogic_Slv_Nor2_NMOSB_ChannelLength=30,
                                  _SARLogic_Slv_Nor2_NMOSB_POGate_Comb_length=100,

                                  ## PMOS
                                  ## PMOS common
                                  _SARLogic_Slv_Nor2_PMOS_XVT='HVT',

                                  ## PMOSA
                                  _SARLogic_Slv_Nor2_PMOSA_NumberofGate=4,
                                  _SARLogic_Slv_Nor2_PMOSA_ChannelWidth=400,
                                  _SARLogic_Slv_Nor2_PMOSA_ChannelLength=30,
                                  _SARLogic_Slv_Nor2_PMOSA_POGate_Comb_length=100,

                                  ## PMOSB
                                  _SARLogic_Slv_Nor2_PMOSB_NumberofGate=4,
                                  _SARLogic_Slv_Nor2_PMOSB_ChannelWidth=400,
                                  _SARLogic_Slv_Nor2_PMOSB_ChannelLength=30,
                                  _SARLogic_Slv_Nor2_PMOSB_POGate_Comb_length=100,

                                  ## Slave Inv1 : ReSet pre-driver
                                  ## Inv1 common

                                  ## Inv1 NMOS
                                  _SARLogic_Slv_Inv1_NMOS_NumberofGate=1,
                                  _SARLogic_Slv_Inv1_NMOS_ChannelWidth=200,
                                  _SARLogic_Slv_Inv1_NMOS_ChannelLength=30,
                                  _SARLogic_Slv_Inv1_NMOS_XVT='SLVT',
                                  _SARLogic_Slv_Inv1_NMOS_POGate_Comb_length=100,

                                  ## Inv1 PMOS
                                  _SARLogic_Slv_Inv1_PMOS_NumberofGate=1,
                                  _SARLogic_Slv_Inv1_PMOS_ChannelWidth=400,
                                  _SARLogic_Slv_Inv1_PMOS_ChannelLength=30,
                                  _SARLogic_Slv_Inv1_PMOS_XVT='SLVT',
                                  _SARLogic_Slv_Inv1_PMOS_POGate_Comb_length=100,

                                  ## Slave Inv2 : ReSet driver
                                  ## Inv2 common

                                  ## Inv2 NMOS
                                  _SARLogic_Slv_Inv2_NMOS_NumberofGate=1,
                                  _SARLogic_Slv_Inv2_NMOS_ChannelWidth=300,
                                  _SARLogic_Slv_Inv2_NMOS_ChannelLength=30,
                                  _SARLogic_Slv_Inv2_NMOS_XVT='SLVT',
                                  _SARLogic_Slv_Inv2_NMOS_POGate_Comb_length=100,

                                  ## Inv2 PMOS
                                  _SARLogic_Slv_Inv2_PMOS_NumberofGate=1,
                                  _SARLogic_Slv_Inv2_PMOS_ChannelWidth=400,
                                  _SARLogic_Slv_Inv2_PMOS_ChannelLength=30,
                                  _SARLogic_Slv_Inv2_PMOS_XVT='SLVT',
                                  _SARLogic_Slv_Inv2_PMOS_POGate_Comb_length=100,

                                  ## Slave Inv3 : Qb driver
                                  ## Inv3 common

                                  ## Inv3 NMOS
                                  _SARLogic_Slv_Inv3_NMOS_NumberofGate=5,  # 1
                                  _SARLogic_Slv_Inv3_NMOS_ChannelWidth=200,
                                  _SARLogic_Slv_Inv3_NMOS_ChannelLength=30,
                                  _SARLogic_Slv_Inv3_NMOS_XVT='SLVT',
                                  _SARLogic_Slv_Inv3_NMOS_POGate_Comb_length=100,

                                  ## Inv3 PMOS
                                  _SARLogic_Slv_Inv3_PMOS_NumberofGate=5,  # 1
                                  _SARLogic_Slv_Inv3_PMOS_ChannelWidth=400,
                                  _SARLogic_Slv_Inv3_PMOS_ChannelLength=30,
                                  _SARLogic_Slv_Inv3_PMOS_XVT='SLVT',
                                  _SARLogic_Slv_Inv3_PMOS_POGate_Comb_length=100,

                                  # Top Clock  Tree Size
                                  _SARLogic_CLKBufTreeTop_NumOfStage=4,
                                  _SARLogic_CLKBufTreeTop_CLKSampBuf_SizeByStage=None,
                                  _SARLogic_CLKBufTreeTop_CLKSrcBuf_SizeByStage=None,
                                  # 스테이지에 따른 버퍼 사이즈(UnitBuffer의 배수로 각 스테이지의 크기가 결정 됨.)
                                  _SARLogic_CLKBufTreeTop_XOffSet=0,

                                  ## Top CLK Buffer Size
                                  _SARLogic_CLKBufTreeTop_Inv_NMOS_ChannelWidth=400,  # Number
                                  _SARLogic_CLKBufTreeTop_Inv_NMOS_ChannelLength=30,  # Number
                                  _SARLogic_CLKBufTreeTop_Inv_NMOS_NumberofGate=1,  # Number
                                  _SARLogic_CLKBufTreeTop_Inv_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _SARLogic_CLKBufTreeTop_Inv_NMOS_POGate_Comb_length=100,  # None/Number

                                  _SARLogic_CLKBufTreeTop_Inv_PMOS_ChannelWidth=800,  # Number
                                  _SARLogic_CLKBufTreeTop_Inv_PMOS_ChannelLength=30,  # Number
                                  _SARLogic_CLKBufTreeTop_Inv_PMOS_NumberofGate=1,  # Number
                                  _SARLogic_CLKBufTreeTop_Inv_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _SARLogic_CLKBufTreeTop_Inv_PMOS_POGate_Comb_length=100,  # None/Number

                                  # Top CLK BufferPowerRail Size
                                  _SARLogic_CLKBufTreeTop_NMOS_Pbody_NumCont=2,
                                  _SARLogic_CLKBufTreeTop_NMOS_Pbody_XvtTop2Pbody=None,
                                  _SARLogic_CLKBufTreeTop_PMOS_Nbody_NumCont=2,
                                  _SARLogic_CLKBufTreeTop_PMOS_Nbody_Xvtdown2Nbody=None,
                                  _SARLogic_CLKBufTreeTop_PMOSXvt2NMOSXvt=700,

                                  # Bottom Clock  Tree Size
                                  _SARLogic_CLKBufTreeBot_NumOfStage=4,
                                  _SARLogic_CLKBufTreeBot_CompOutBuf_SizeByStage=None,
                                  _SARLogic_CLKBufTreeBot_CLKDoutBuf_SizeByStage=None,
                                  # 스테이지에 따른 버퍼 사이즈(UnitBuffer의 배수로 각 스테이지의 크기가 결정 됨.)
                                  _SARLogic_CLKBufTreeBot_XOffSet=0,

                                  ## Bottom CLK Buffer Size
                                  _SARLogic_CLKBufTreeBot_Inv_NMOS_ChannelWidth=400,  # Number
                                  _SARLogic_CLKBufTreeBot_Inv_NMOS_ChannelLength=30,  # Number
                                  _SARLogic_CLKBufTreeBot_Inv_NMOS_NumberofGate=1,  # Number
                                  _SARLogic_CLKBufTreeBot_Inv_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _SARLogic_CLKBufTreeBot_Inv_NMOS_POGate_Comb_length=100,  # None/Number

                                  _SARLogic_CLKBufTreeBot_Inv_PMOS_ChannelWidth=800,  # Number
                                  _SARLogic_CLKBufTreeBot_Inv_PMOS_ChannelLength=30,  # Number
                                  _SARLogic_CLKBufTreeBot_Inv_PMOS_NumberofGate=1,  # Number
                                  _SARLogic_CLKBufTreeBot_Inv_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _SARLogic_CLKBufTreeBot_Inv_PMOS_POGate_Comb_length=100,  # None/Number

                                  # Bottom CLK Buffer PowerRail Size
                                  _SARLogic_CLKBufTreeBot_NMOS_Pbody_NumCont=2,
                                  _SARLogic_CLKBufTreeBot_NMOS_Pbody_XvtTop2Pbody=None,
                                  _SARLogic_CLKBufTreeBot_PMOS_Nbody_NumCont=2,
                                  _SARLogic_CLKBufTreeBot_PMOS_Nbody_Xvtdown2Nbody=None,
                                  _SARLogic_CLKBufTreeBot_PMOSXvt2NMOSXvt=700,

                                  #### CDAC Pre-Driver Sizing
                                  ## InvChain Common
                                  _CDACPreDriver_Pbody_NumCont=2,  # number
                                  _CDACPreDriver_Nbody_NumCont=2,  # number
                                  _CDACPreDriver_PMOSXvt2NMOSXvt=500,  # number
                                  _CDACPreDriver_XvtTop2Pbody=None,  # number/None(Minimum)
                                  _CDACPreDriver_Xvtdown2Nbody=None,  # number/None(Minimum)

                                  ## Inverter Chain
                                  ## Inv1 common
                                  _CDACPreDriver_NumberofGate=[2, 4, 6],  # Vector
                                  _CDACPreDriver_ChannelLength=30,  # Scalar
                                  _CDACPreDriver_XVT='SLVT',  # 'SLVT'

                                  ## Inv1 NMOS
                                  _CDACPreDriver_Inv_NMOS_ChannelWidth=200,  # Scalar
                                  _CDACPreDriver_Inv_NMOS_POGate_Comb_length=100,  # Scalar

                                  ## Inv1 PMOS
                                  _CDACPreDriver_Inv_PMOS_ChannelWidth=400,  # Scalar
                                  _CDACPreDriver_Inv_PMOS_POGate_Comb_length=100,  # Scalar

                                  ## CLKDout(OutSamp) Inverter & AND Common Option
                                  _CLKDout_XVT_Common='SLVT',

                                  ## CLKDout(OutSamp) Inverter Size
                                  _CLKDout_Inv_NMOS_ChannelWidth=400,  # Number
                                  _CLKDout_Inv_NMOS_ChannelLength=30,  # Number
                                  _CLKDout_Inv_NMOS_NumberofGate=1,  # Number
                                  _CLKDout_Inv_NMOS_POGate_Comb_length=100,  # None/Number

                                  _CLKDout_Inv_PMOS_ChannelWidth=800,  # Number
                                  _CLKDout_Inv_PMOS_ChannelLength=30,  # Number
                                  _CLKDout_Inv_PMOS_NumberofGate=1,  # Number
                                  _CLKDout_Inv_PMOS_POGate_Comb_length=100,  # None/Number

                                  ## CLKDout(OutSamp) AND Size
                                  _CLKDout_AND_NAND_NMOS_ChannelWidth=400,
                                  _CLKDout_AND_NAND_NMOS_ChannelLength=30,
                                  _CLKDout_AND_NAND_NMOS_NumberofGate=2,

                                  _CLKDout_AND_NAND_PMOS_ChannelWidth=800,
                                  _CLKDout_AND_NAND_PMOS_ChannelLength=30,
                                  _CLKDout_AND_NAND_PMOS_NumberofGate=1,

                                  _CLKDout_AND_Inv_NMOS_ChannelWidth=400,
                                  _CLKDout_AND_Inv_NMOS_ChannelLength=30,
                                  _CLKDout_AND_Inv_NMOS_NumberofGate=1,
                                  _CLKDout_AND_Inv_NMOS_POGate_Comb_length=100,

                                  _CLKDout_AND_Inv_PMOS_ChannelWidth=800,
                                  _CLKDout_AND_Inv_PMOS_ChannelLength=30,
                                  _CLKDout_AND_Inv_PMOS_NumberofGate=1,
                                  _CLKDout_AND_Inv_PMOS_POGate_Comb_length=100,

                                  ## StrongArm Latch
                                  _Comp_SALatch_CLKinputPMOSFinger1=None,  # 6
                                  _Comp_SALatch_CLKinputPMOSFinger2=None,  # 3
                                  _Comp_SALatch_PMOSFinger=None,  # 3
                                  _Comp_SALatch_PMOSChannelWidth=None,  # 500
                                  _Comp_SALatch_DATAinputNMOSFinger=None,  # 12
                                  _Comp_SALatch_NMOSFinger=None,  # 2
                                  _Comp_SALatch_CLKinputNMOSFinger=None,  # 8
                                  _Comp_SALatch_NMOSChannelWidth=None,  # 500
                                  _Comp_SALatch_CLKinputNMOSChannelWidth=None,  # 800
                                  _Comp_SALatch_ChannelLength=None,  # 30
                                  _Comp_SALatch_Dummy=True,
                                  _Comp_SALatch_XVT=None,
                                  _Comp_SALatch_GuardringWidth=None,
                                  _Comp_SALatch_Guardring=True,
                                  _Comp_SALatch_SlicerGuardringWidth=None,
                                  _Comp_SALatch_SlicerGuardring=None,
                                  _Comp_SALatch_NumSupplyCOY=None,
                                  _Comp_SALatch_NumSupplyCOX=None,
                                  _Comp_SALatch_SupplyMet1XWidth=None,
                                  _Comp_SALatch_SupplyMet1YWidth=None,
                                  _Comp_SALatch_VDD2VSSHeight=None,
                                  _Comp_SALatch_NumVIAPoly2Met1COX=None,
                                  _Comp_SALatch_NumVIAPoly2Met1COY=None,
                                  _Comp_SALatch_NumVIAMet12COX=None,
                                  _Comp_SALatch_NumVIAMet12COY=None,
                                  _Comp_SALatch_PowerLine=False,

                                  ## StrongARMLatch Output Buffer Sizing
                                  # Inverter1
                                  _Comp_SAOutBuf_Inv1_NMOS_ChannelWidth=None,  # Number
                                  _Comp_SAOutBuf_Inv1_NMOS_ChannelLength=None,  # Number
                                  _Comp_SAOutBuf_Inv1_NMOS_NumberofGate=None,  # Number
                                  _Comp_SAOutBuf_Inv1_NMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _Comp_SAOutBuf_Inv1_NMOS_POGate_Comb_length=None,  # None/Number

                                  _Comp_SAOutBuf_Inv1_PMOS_ChannelWidth=None,  # Number
                                  _Comp_SAOutBuf_Inv1_PMOS_ChannelLength=None,  # Number
                                  _Comp_SAOutBuf_Inv1_PMOS_NumberofGate=None,  # Number
                                  _Comp_SAOutBuf_Inv1_PMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _Comp_SAOutBuf_Inv1_PMOS_POGate_Comb_length=None,  # None/Number

                                  # Inverter2
                                  _Comp_SAOutBuf_Inv2_NMOS_ChannelWidth=None,  # Number
                                  _Comp_SAOutBuf_Inv2_NMOS_ChannelLength=None,  # Number
                                  _Comp_SAOutBuf_Inv2_NMOS_NumberofGate=None,  # Number
                                  _Comp_SAOutBuf_Inv2_NMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _Comp_SAOutBuf_Inv2_NMOS_POGate_Comb_length=None,  # None/Number

                                  _Comp_SAOutBuf_Inv2_PMOS_ChannelWidth=None,  # Number
                                  _Comp_SAOutBuf_Inv2_PMOS_ChannelLength=None,  # Number
                                  _Comp_SAOutBuf_Inv2_PMOS_NumberofGate=None,  # Number
                                  _Comp_SAOutBuf_Inv2_PMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _Comp_SAOutBuf_Inv2_PMOS_POGate_Comb_length=None,  # None/Number

                                  ## SR Latch Sizing
                                  _Comp_SRLatch_NAND_NMOS_ChannelWidth=None,  # Number
                                  _Comp_SRLatch_NAND_NMOS_ChannelLength=None,  # Number
                                  _Comp_SRLatch_NAND_NMOS_NumberofGate=None,  # Number
                                  _Comp_SRLatch_NAND_NMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _Comp_SRLatch_NAND_NMOS_POGate_Comb_length=None,  # None/Number

                                  _Comp_SRLatch_NAND_PMOS_ChannelWidth=None,  # Number
                                  _Comp_SRLatch_NAND_PMOS_ChannelLength=None,  # Number
                                  _Comp_SRLatch_NAND_PMOS_NumberofGate=None,  # Number
                                  _Comp_SRLatch_NAND_PMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _Comp_SRLatch_NAND_PMOS_POGate_Comb_length=None,  # None/Number

                                  # CLK Input Logic Gates
                                  _Comp_CLKSamp_Inv_NMOS_ChannelWidth=None,
                                  _Comp_CLKSamp_Inv_NMOS_ChannelLength=None,
                                  _Comp_CLKSamp_Inv_NMOS_NumberofGate=None,
                                  _Comp_CLKSamp_Inv_NMOS_XVT=None,
                                  _Comp_CLKSamp_Inv_NMOS_POGate_Comb_length=None,

                                  _Comp_CLKSamp_Inv_PMOS_ChannelWidth=None,
                                  _Comp_CLKSamp_Inv_PMOS_ChannelLength=None,
                                  _Comp_CLKSamp_Inv_PMOS_NumberofGate=None,
                                  _Comp_CLKSamp_Inv_PMOS_XVT=None,
                                  _Comp_CLKSamp_Inv_PMOS_POGate_Comb_length=None,

                                  _Comp_CLKSrc_Inv_NMOS_ChannelWidth=None,
                                  _Comp_CLKSrc_Inv_NMOS_ChannelLength=None,
                                  _Comp_CLKSrc_Inv_NMOS_NumberofGate=None,
                                  _Comp_CLKSrc_Inv_NMOS_XVT=None,
                                  _Comp_CLKSrc_Inv_NMOS_POGate_Comb_length=None,

                                  _Comp_CLKSrc_Inv_PMOS_ChannelWidth=None,
                                  _Comp_CLKSrc_Inv_PMOS_ChannelLength=None,
                                  _Comp_CLKSrc_Inv_PMOS_NumberofGate=None,
                                  _Comp_CLKSrc_Inv_PMOS_XVT=None,
                                  _Comp_CLKSrc_Inv_PMOS_POGate_Comb_length=None,

                                  ## CLKSrc & CLKSample AND Gate
                                  _Comp_AND_NAND_NMOS_ChannelWidth=None,
                                  _Comp_AND_NAND_NMOS_ChannelLength=None,
                                  _Comp_AND_NAND_NMOS_NumberofGate=None,
                                  _Comp_AND_NAND_NMOS_XVT=None,

                                  _Comp_AND_NAND_PMOS_ChannelWidth=None,
                                  _Comp_AND_NAND_PMOS_ChannelLength=None,
                                  _Comp_AND_NAND_PMOS_NumberofGate=None,
                                  _Comp_AND_NAND_PMOS_XVT=None,

                                  _Comp_AND_Inv_NMOS_ChannelWidth=None,
                                  _Comp_AND_Inv_NMOS_ChannelLength=None,
                                  _Comp_AND_Inv_NMOS_NumberofGate=None,
                                  _Comp_AND_Inv_NMOS_XVT=None,
                                  _Comp_AND_Inv_NMOS_POGate_Comb_length=None,

                                  _Comp_AND_Inv_PMOS_ChannelWidth=None,
                                  _Comp_AND_Inv_PMOS_ChannelLength=None,
                                  _Comp_AND_Inv_PMOS_NumberofGate=None,
                                  _Comp_AND_Inv_PMOS_XVT=None,
                                  _Comp_AND_Inv_PMOS_POGate_Comb_length=None,

                                  ## CLK Buffer
                                  # Inverter1
                                  _Comp_CLKBuf_Inv1_NMOS_ChannelWidth=None,  # Number
                                  _Comp_CLKBuf_Inv1_NMOS_ChannelLength=None,  # Number
                                  _Comp_CLKBuf_Inv1_NMOS_NumberofGate=None,  # Number
                                  _Comp_CLKBuf_Inv1_NMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _Comp_CLKBuf_Inv1_NMOS_POGate_Comb_length=None,  # None/Number

                                  _Comp_CLKBuf_Inv1_PMOS_ChannelWidth=None,  # Number
                                  _Comp_CLKBuf_Inv1_PMOS_ChannelLength=None,  # Number
                                  _Comp_CLKBuf_Inv1_PMOS_NumberofGate=None,  # Number
                                  _Comp_CLKBuf_Inv1_PMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _Comp_CLKBuf_Inv1_PMOS_POGate_Comb_length=None,  # None/Number

                                  # Inverter2
                                  _Comp_CLKBuf_Inv2_NMOS_ChannelWidth=None,  # Number
                                  _Comp_CLKBuf_Inv2_NMOS_ChannelLength=None,  # Number
                                  _Comp_CLKBuf_Inv2_NMOS_NumberofGate=None,  # Number
                                  _Comp_CLKBuf_Inv2_NMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _Comp_CLKBuf_Inv2_NMOS_POGate_Comb_length=None,  # None/Number

                                  _Comp_CLKBuf_Inv2_PMOS_ChannelWidth=None,  # Number
                                  _Comp_CLKBuf_Inv2_PMOS_ChannelLength=None,  # Number
                                  _Comp_CLKBuf_Inv2_PMOS_NumberofGate=None,  # Number
                                  _Comp_CLKBuf_Inv2_PMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _Comp_CLKBuf_Inv2_PMOS_POGate_Comb_length=None,  # None/Number

                                  # PowerRail Placement
                                  _Comp_BufSR_NMOS_Pbody_NumCont=None,
                                  _Comp_BufSR_NMOS_Pbody_XvtTop2Pbody=None,
                                  _Comp_BufSR_PMOS_Nbody_NumCont=None,
                                  _Comp_BufSR_PMOS_Nbody_Xvtdown2Nbody=None,
                                  _Comp_BufSR_PMOSXvt2NMOSXvt=None,

                                  _Comp_CLKInLogic_NMOS_Pbody_Xvtdown2Pbody=None,
                                  _Comp_CLKInLogic_PMOS_Nbody_NumCont=None,
                                  _Comp_CLKInLogic_PMOS_Nbody_Xvtdown2Nbody=None,
                                  _Comp_CLKInLogic_PMOSXvt2NMOSXvt=None,

                                  # Additional Buffer Between CLK_Sample Input of Comparator And Output of Tree Buffer
                                  ## InvChain Common
                                  _Buf_CLKSamp_Pbody_NumCont=2,  # number
                                  _Buf_CLKSamp_Nbody_NumCont=2,  # number
                                  _Buf_CLKSamp_PMOSXvt2NMOSXvt=500,  # number
                                  _Buf_CLKSamp_XvtTop2Pbody=None,  # number/None(Minimum)
                                  _Buf_CLKSamp_Xvtdown2Nbody=None,  # number/None(Minimum)

                                  ## Inverter Chain
                                  ## Inv1 common
                                  _Buf_CLKSamp_NumberofGate=[2, 4, 6],  # Vector
                                  _Buf_CLKSamp_ChannelLength=30,  # Scalar
                                  _Buf_CLKSamp_XVT='SLVT',  # 'SLVT'

                                  ## Inv1 NMOS
                                  _Buf_CLKSamp_Inv_NMOS_ChannelWidth=200,  # Scalar
                                  _Buf_CLKSamp_Inv_NMOS_POGate_Comb_length=100,  # Scalar

                                  ## Inv1 PMOS
                                  _Buf_CLKSamp_Inv_PMOS_ChannelWidth=400,  # Scalar
                                  _Buf_CLKSamp_Inv_PMOS_POGate_Comb_length=100,  # Scalar

                                  # Additional Buffer Between CLK_Source Input of Comparator And Output of Tree Buffer
                                  ## InvChain Common
                                  _Buf_CLKSrc_Pbody_NumCont=2,  # number
                                  _Buf_CLKSrc_Nbody_NumCont=2,  # number
                                  _Buf_CLKSrc_PMOSXvt2NMOSXvt=500,  # number
                                  _Buf_CLKSrc_XvtTop2Pbody=None,  # number/None(Minimum)
                                  _Buf_CLKSrc_Xvtdown2Nbody=None,  # number/None(Minimum)

                                  ## Inverter Chain
                                  ## Inv1 common
                                  _Buf_CLKSrc_NumberofGate=[2, 4, 6],  # Vector
                                  _Buf_CLKSrc_ChannelLength=30,  # Scalar
                                  _Buf_CLKSrc_XVT='SLVT',  # 'SLVT'

                                  ## Inv1 NMOS
                                  _Buf_CLKSrc_Inv_NMOS_ChannelWidth=200,  # Scalar
                                  _Buf_CLKSrc_Inv_NMOS_POGate_Comb_length=100,  # Scalar

                                  ## Inv1 PMOS
                                  _Buf_CLKSrc_Inv_PMOS_ChannelWidth=400,  # Scalar
                                  _Buf_CLKSrc_Inv_PMOS_POGate_Comb_length=100,  # Scalar

                                  # Additional Buffer Between Output of Comparator  And Input of Tree Buffer
                                  ## InvChain Common
                                  _Buf_CompOut_Pbody_NumCont=2,  # number
                                  _Buf_CompOut_Nbody_NumCont=2,  # number
                                  _Buf_CompOut_PMOSXvt2NMOSXvt=500,  # number
                                  _Buf_CompOut_XvtTop2Pbody=None,  # number/None(Minimum)
                                  _Buf_CompOut_Xvtdown2Nbody=None,  # number/None(Minimum)

                                  ## Inv1 common
                                  _Buf_CompOut_NumberofGate=[2, 4, 6],  # Vector
                                  _Buf_CompOut_ChannelLength=30,  # Scalar
                                  _Buf_CompOut_XVT='SLVT',  # 'SLVT'

                                  ## Inv1 NMOS
                                  _Buf_CompOut_Inv_NMOS_ChannelWidth=200,  # Scalar
                                  _Buf_CompOut_Inv_NMOS_POGate_Comb_length=100,  # Scalar

                                  ## Inv1 PMOS
                                  _Buf_CompOut_Inv_PMOS_ChannelWidth=400,  # Scalar
                                  _Buf_CompOut_Inv_PMOS_POGate_Comb_length=100,  # Scalar

                                  # # Additional Buffer Between Output of CLKDout  And Input of Tree Buffer
                                  # ## Inv1 common
                                  # _Buf_CLKDout_NumberofGate=[2, 4, 6],  # Vector
                                  # _Buf_CLKDout_ChannelLength=30,  # Scalar
                                  # _Buf_CLKDout_XVT='SLVT',  # 'SLVT'
                                  #
                                  # ## Inv1 NMOS
                                  # _Buf_CLKDout_Inv_NMOS_ChannelWidth=200,  # Scalar
                                  # _Buf_CLKDout_Inv_NMOS_POGate_Comb_length=100,  # Scalar
                                  #
                                  # ## Inv1 PMOS
                                  # _Buf_CLKDout_Inv_PMOS_ChannelWidth=400,  # Scalar
                                  # _Buf_CLKDout_Inv_PMOS_POGate_Comb_length=100,  # Scalar

                                  # # Element CDAC
                                  _CDAC_LayoutOption=[5, 6],
                                  _CDAC_ShieldingLayer=4,  # Poly:0, M1:1, M2:2 ...
                                  _CDAC_MetalWidth=50,
                                  _CDAC_MetalLength=1414,  # (8bit size: 1414/ 10bit size: 2800/ 12bit size: 4200)
                                  _CDAC_MetalSpacing=50,

                                  # #Unit Cap
                                  _CDAC_NumOfElement=2,

                                  # # Shielding & Top Connect node
                                  _CDAC_ConnectLength=400,
                                  _CDAC_ExtendLength=400,

                                  # # Dummy Cap Option
                                  _CDAC_DummyCap_TopBottomShort=False,  # False -> Bottom = GND
                                  _CDAC_NumOfDummyCaps=3,  # Number of dummy cap(one side)

                                  # # CommonCentroid With Driving node
                                  _CDAC_CapArrayWDrivingNodeDistance=0,  # DRC Rule
                                  _CDAC_DriveNodeDistance=400,  #
                                  _CDAC_YWidth_Bottom_Hrz=50,

                                  # Driver Sizing
                                  _Driver_CommonCentroidPlacementIfCDACFolded=None,
                                  _Driver_SizeByBit=[32, 16, 8, 4, 2],

                                  # Driver(Inverter) NMOS
                                  _Driver_NMOS_NumberofGate=1,  # number
                                  _Driver_NMOS_ChannelWidth=340,
                                  # number (8bit size: 340/ 10bit size: 680/ 12bit size: 1020)
                                  _Driver_NMOS_Channellength=30,  # number
                                  _Driver_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT

                                  # Driver(Inverter) PMOS
                                  _Driver_PMOS_NumberofGate=1,  # number
                                  _Driver_PMOS_ChannelWidth=900,
                                  # number (8bit size: 900/ 10bit size: 1800/ 12bit size: 2700)
                                  _Driver_PMOS_Channellength=30,  # number
                                  _Driver_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT

                                  # Tr1 and Tr2
                                  # Tr1
                                  _Samp_Tr1Tr2_Tr1_NMOSNumberofGate=None,  # number
                                  _Samp_Tr1Tr2_Tr1_NMOSChannelWidth=None,  # number
                                  _Samp_Tr1Tr2_Tr1_NMOSChannellength=None,  # number
                                  _Samp_Tr1Tr2_Tr1_GateSpacing=None,  # None/number
                                  _Samp_Tr1Tr2_Tr1_SDWidth=None,  # None/number
                                  _Samp_Tr1Tr2_Tr1_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Samp_Tr1Tr2_Tr1_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _Samp_Tr1Tr2_Tr1_Source_Via_TF=False,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Samp_Tr1Tr2_Tr1_Drain_Via_TF=False,  # True/False

                                  # POLY dummy setting
                                  _Samp_Tr1Tr2_Tr1_NMOSDummy=None,  # TF
                                  # if _PMOSDummy == True
                                  _Samp_Tr1Tr2_Tr1_NMOSDummy_length=None,  # None/Value
                                  _Samp_Tr1Tr2_Tr1_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Tr2
                                  _Samp_Tr1Tr2_Tr2_NMOSNumberofGate=None,  # number
                                  _Samp_Tr1Tr2_Tr2_NMOSChannelWidth=None,  # number
                                  _Samp_Tr1Tr2_Tr2_NMOSChannellength=None,  # number
                                  _Samp_Tr1Tr2_Tr2_GateSpacing=None,  # None/number
                                  _Samp_Tr1Tr2_Tr2_SDWidth=None,  # None/number
                                  _Samp_Tr1Tr2_Tr2_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Samp_Tr1Tr2_Tr2_PCCrit=None,  # None/True

                                  # Source_node_ViaM1M2
                                  _Samp_Tr1Tr2_Tr2_Source_Via_TF=False,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Samp_Tr1Tr2_Tr2_Drain_Via_TF=False,  # True/False

                                  # POLY dummy setting
                                  _Samp_Tr1Tr2_Tr2_NMOSDummy=None,  # TF
                                  # if _PMOSDummy == True
                                  _Samp_Tr1Tr2_Tr2_NMOSDummy_length=None,  # None/Value
                                  _Samp_Tr1Tr2_Tr2_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Input/Output node
                                  # INPUT node
                                  _Samp_Tr1Tr2_Inputnode_Metal_layer=None,  # number
                                  _Samp_Tr1Tr2_Inputnode_width=None,  # number

                                  # OUTPUT node
                                  _Samp_Tr1Tr2_Outputnode_Metal_layer=None,  # number
                                  _Samp_Tr1Tr2_Outputnode_width=None,  # number

                                  # Guardring
                                  # Pbody: number of contact
                                  # Nbody
                                  _Samp_Tr1Tr2_NwellWidth=None,  # number

                                  # Tr4
                                  _Samp_Tr4_NMOSNumberofGate=None,  # number
                                  _Samp_Tr4_NMOSChannelWidth=None,  # number
                                  _Samp_Tr4_NMOSChannellength=None,  # number
                                  _Samp_Tr4_GateSpacing=None,  # None/number
                                  _Samp_Tr4_SDWidth=None,  # None/number
                                  _Samp_Tr4_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Samp_Tr4_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _Samp_Tr4_Source_Via_TF=True,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Samp_Tr4_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _Samp_Tr4_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Samp_Tr4_NMOSDummy_length=None,  # None/Value
                                  _Samp_Tr4_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Tr5 Tr7 Tr9
                                  # PMOS: Tr5
                                  _Samp_Tr5_PMOSNumberofGate=None,
                                  _Samp_Tr5_PMOSChannelWidth=None,  # ref=1000
                                  _Samp_Tr5_PMOSChannellength=None,
                                  _Samp_Tr5_GateSpacing=None,
                                  _Samp_Tr5_SDWidth=None,
                                  _Samp_Tr5_XVT='SLVT',
                                  _Samp_Tr5_PCCrit=None,

                                  # Source_node_ViaM1M2
                                  _Samp_Tr5_Source_Via_TF=True,

                                  # Drain_node_ViaM1M2
                                  _Samp_Tr5_Drain_Via_TF=True,

                                  # POLY dummy setting
                                  _Samp_Tr5_PMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Samp_Tr5_PMOSDummy_length=None,  # None/Value
                                  _Samp_Tr5_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # PMOS: Tr7
                                  _Samp_Tr7_PMOSNumberofGate=None,
                                  _Samp_Tr7_PMOSChannelWidth=None,
                                  _Samp_Tr7_PMOSChannellength=None,
                                  _Samp_Tr7_GateSpacing=None,
                                  _Samp_Tr7_SDWidth=None,
                                  _Samp_Tr7_XVT='SLVT',
                                  _Samp_Tr7_PCCrit=None,

                                  # Source_node_ViaM1M2
                                  _Samp_Tr7_Source_Via_TF=True,

                                  # Drain_node_ViaM1M2
                                  _Samp_Tr7_Drain_Via_TF=True,

                                  # POLY dummy setting
                                  _Samp_Tr7_PMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Samp_Tr7_PMOSDummy_length=None,  # None/Value
                                  _Samp_Tr7_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # PMOS: Tr9
                                  _Samp_Tr9_PMOSNumberofGate=None,
                                  _Samp_Tr9_PMOSChannelWidth=None,  # ref = 1000
                                  _Samp_Tr9_PMOSChannellength=None,
                                  _Samp_Tr9_GateSpacing=None,
                                  _Samp_Tr9_SDWidth=None,
                                  _Samp_Tr9_XVT='SLVT',
                                  _Samp_Tr9_PCCrit=None,

                                  # Source_node_ViaM1M2
                                  _Samp_Tr9_Source_Via_TF=True,

                                  # Drain_node_ViaM1M2
                                  _Samp_Tr9_Drain_Via_TF=True,

                                  # POLY dummy setting
                                  _Samp_Tr9_PMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Samp_Tr9_PMOSDummy_length=None,  # None/Value
                                  _Samp_Tr9_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Tr8
                                  _Samp_Tr8_NMOSNumberofGate=None,  # number (ref:4)
                                  _Samp_Tr8_NMOSChannelWidth=None,  # number (ref:500)
                                  _Samp_Tr8_NMOSChannellength=None,  # number (ref:30)
                                  _Samp_Tr8_GateSpacing=None,  # None/number
                                  _Samp_Tr8_SDWidth=None,  # None/number
                                  _Samp_Tr8_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Samp_Tr8_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _Samp_Tr8_Source_Via_TF=True,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Samp_Tr8_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _Samp_Tr8_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Samp_Tr8_NMOSDummy_length=None,  # None/Value
                                  _Samp_Tr8_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  ## Tr6
                                  _Samp_Tr6_NMOSNumberofGate=None,  # number
                                  _Samp_Tr6_NMOSChannelWidth=None,  # number
                                  _Samp_Tr6_NMOSChannellength=None,  # number
                                  _Samp_Tr6_GateSpacing=None,  # None/number
                                  _Samp_Tr6_SDWidth=None,  # None/number
                                  _Samp_Tr6_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Samp_Tr6_PCCrit=True,  # None/True

                                  # Tr6 Source_node_ViaM1M2
                                  _Samp_Tr6_Source_Via_TF=False,  # True/False

                                  # Tr6 Drain_node_ViaM1M2
                                  _Samp_Tr6_Drain_Via_TF=False,  # True/False

                                  # Tr6 POLY dummy setting
                                  _Samp_Tr6_NMOSDummy=True,  # TF
                                  # Tr6 if _PMOSDummy == True
                                  _Samp_Tr6_NMOSDummy_length=None,  # None/Value
                                  _Samp_Tr6_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Tr6 Vp node
                                  _Samp_Tr6_Vp_node_width=None,  # Number
                                  _Samp_Tr6_Vp_node_metal_Layer=None,  # number

                                  # Tr6 Guardring
                                  # Pbody: number of contact
                                  # Nbody
                                  _Samp_Tr6_NwellWidth=None,  # number

                                  # PMOS: Tr11
                                  _Samp_Tr11_PMOSNumberofGate=None,
                                  _Samp_Tr11_PMOSChannelWidth=None,
                                  _Samp_Tr11_PMOSChannellength=None,
                                  _Samp_Tr11_GateSpacing=None,
                                  _Samp_Tr11_SDWidth=None,
                                  _Samp_Tr11_XVT='SLVT',
                                  _Samp_Tr11_PCCrit=None,

                                  # Source_node_ViaM1M2
                                  _Samp_Tr11_Source_Via_TF=True,

                                  # Drain_node_ViaM1M2
                                  _Samp_Tr11_Drain_Via_TF=True,

                                  # POLY dummy setting
                                  _Samp_Tr11_PMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Samp_Tr11_PMOSDummy_length=None,  # None/Value
                                  _Samp_Tr11_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Nbodyring(Guardring)
                                  _Samp_Tr11_Guardring_NumCont=None,  # number

                                  ## VddTieCell4
                                  # VddTieCell4 NMOS
                                  _Samp_Tie4N_NMOSNumberofGate=None,  # number
                                  _Samp_Tie4N_NMOSChannelWidth=None,  # number
                                  _Samp_Tie4N_NMOSChannellength=None,  # number
                                  _Samp_Tie4N_GateSpacing=None,  # None/number
                                  _Samp_Tie4N_SDWidth=None,  # None/number
                                  _Samp_Tie4N_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Samp_Tie4N_PCCrit=True,  # None/True

                                  # VddTieCell4 Source_node_ViaM1M2
                                  _Samp_Tie4N_Source_Via_TF=False,  # True/False

                                  # VddTieCell4 Drain_node_ViaM1M2
                                  _Samp_Tie4N_Drain_Via_TF=False,  # True/False

                                  # POLY dummy setting
                                  _Samp_Tie4N_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Samp_Tie4N_NMOSDummy_length=None,  # None/Value
                                  _Samp_Tie4N_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # VddTieCell4 PMOS
                                  _Samp_Tie4P_PMOSNumberofGate=None,  # number
                                  _Samp_Tie4P_PMOSChannelWidth=None,  # number
                                  _Samp_Tie4P_PMOSChannellength=None,  # number
                                  _Samp_Tie4P_GateSpacing=None,  # None/number
                                  _Samp_Tie4P_SDWidth=None,  # None/number
                                  _Samp_Tie4P_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Samp_Tie4P_PCCrit=True,  # None/True

                                  # VddTieCell4 PMOS Source_node_ViaM1M2
                                  _Samp_Tie4P_Source_Via_TF=False,  # True/False

                                  # VddTieCell4 PMOS Drain_node_ViaM1M2
                                  _Samp_Tie4P_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _Samp_Tie4P_PMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Samp_Tie4P_PMOSDummy_length=None,  # None/Value
                                  _Samp_Tie4P_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # VddTieCell4 Number of Body Contact
                                  _Samp_Tie4_NBodyCOX=None,
                                  _Samp_Tie4_NBodyCOY=None,
                                  _Samp_Tie4_PBodyCOX=None,
                                  _Samp_Tie4_PBodyCOY=None,

                                  ## VddTieCell8
                                  # VddTieCell8 NMOS
                                  _Samp_Tie8N_NMOSNumberofGate=None,  # number
                                  _Samp_Tie8N_NMOSChannelWidth=None,  # number
                                  _Samp_Tie8N_NMOSChannellength=None,  # number
                                  _Samp_Tie8N_GateSpacing=None,  # None/number
                                  _Samp_Tie8N_SDWidth=None,  # None/number
                                  _Samp_Tie8N_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Samp_Tie8N_PCCrit=True,  # None/True

                                  # VddTieCell8 Source_node_ViaM1M2
                                  _Samp_Tie8N_Source_Via_TF=False,  # True/False

                                  # VddTieCell8 Drain_node_ViaM1M2
                                  _Samp_Tie8N_Drain_Via_TF=False,  # True/False

                                  # POLY dummy setting
                                  _Samp_Tie8N_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Samp_Tie8N_NMOSDummy_length=None,  # None/Value
                                  _Samp_Tie8N_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # VddTieCell8 PMOS
                                  _Samp_Tie8P_PMOSNumberofGate=None,  # number
                                  _Samp_Tie8P_PMOSChannelWidth=None,  # number
                                  _Samp_Tie8P_PMOSChannellength=None,  # number
                                  _Samp_Tie8P_GateSpacing=None,  # None/number
                                  _Samp_Tie8P_SDWidth=None,  # None/number
                                  _Samp_Tie8P_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Samp_Tie8P_PCCrit=True,  # None/True

                                  # VddTieCell8 PMOS Source_node_ViaM1M2
                                  _Samp_Tie8P_Source_Via_TF=False,  # True/False

                                  # VddTieCell8 PMOS Drain_node_ViaM1M2
                                  _Samp_Tie8P_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _Samp_Tie8P_PMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Samp_Tie8P_PMOSDummy_length=None,  # None/Value
                                  _Samp_Tie8P_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # VddTieCell8 Number of Body Contact
                                  _Samp_Tie8_NBodyCOX=None,
                                  _Samp_Tie8_NBodyCOY=None,
                                  _Samp_Tie8_PBodyCOX=None,
                                  _Samp_Tie8_PBodyCOY=None,

                                  # Tr12
                                  _Samp_Tr12_NMOSNumberofGate=None,  # number
                                  _Samp_Tr12_NMOSChannelWidth=None,  # number
                                  _Samp_Tr12_NMOSChannellength=None,  # number
                                  _Samp_Tr12_GateSpacing=None,  # None/number
                                  _Samp_Tr12_SDWidth=None,  # None/number
                                  _Samp_Tr12_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Samp_Tr12_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _Samp_Tr12_Source_Via_TF=True,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Samp_Tr12_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _Samp_Tr12_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Samp_Tr12_NMOSDummy_length=None,  # None/Value
                                  _Samp_Tr12_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Tr3
                                  _Samp_Tr3_NMOSNumberofGate=None,  # number
                                  _Samp_Tr3_NMOSChannelWidth=None,  # number
                                  _Samp_Tr3_NMOSChannellength=None,  # number
                                  _Samp_Tr3_GateSpacing=None,  # None/number
                                  _Samp_Tr3_SDWidth=None,  # None/number
                                  _Samp_Tr3_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Samp_Tr3_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _Samp_Tr3_Source_Via_TF=True,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Samp_Tr3_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _Samp_Tr3_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Samp_Tr3_NMOSDummy_length=None,  # None/Value
                                  _Samp_Tr3_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Tr10
                                  _Samp_Tr10_NMOSNumberofGate=None,  # number
                                  _Samp_Tr10_NMOSChannelWidth=None,  # number
                                  _Samp_Tr10_NMOSChannellength=None,  # number
                                  _Samp_Tr10_GateSpacing=None,  # None/number
                                  _Samp_Tr10_SDWidth=None,  # None/number
                                  _Samp_Tr10_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Samp_Tr10_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _Samp_Tr10_Source_Via_TF=True,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Samp_Tr10_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _Samp_Tr10_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Samp_Tr10_NMOSDummy_length=None,  # None/Value
                                  _Samp_Tr10_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Tr12Tr3Tr10 Guardring
                                  _Samp_Tr12Tr3Tr10_Guardring_NumCont=3,  # Number

                                  # HDVNCAP_Array
                                  _Samp_HDVNCAP_Length=None,
                                  _Samp_HDVNCAP_LayoutOption=None,
                                  _Samp_HDVNCAP_NumFigPair=None,
                                  _Samp_HDVNCAP_Array=None,  # number: 1xnumber
                                  _Samp_HDVNCAP_Cbot_Ctop_metalwidth=None,  # number

                                  ## BootStrapped Sampler CLKB Inverter
                                  _CLKBInv_NMOS_NumberofGate=32,
                                  _CLKBInv_NMOS_ChannelWidth=400,
                                  _CLKBInv_NMOS_ChannelLength=30,
                                  _CLKBInv_NMOS_XVT='SLVT',
                                  _CLKBInv_NMOS_POGate_Comb_length=None,

                                  _CLKBInv_PMOS_NumberofGate=32,
                                  _CLKBInv_Inv_PMOS_ChannelWidth=800,
                                  _CLKBInv_PMOS_ChannelLength=30,
                                  _CLKBInv_PMOS_XVT='SLVT',
                                  _CLKBInv_PMOS_POGate_Comb_length=None,

                                  _CLKBInv_Pbody_NumCont=2,
                                  _CLKBInv_XvtTop2Pbody=None,
                                  _CLKBInv_Nbody_NumCont=2,
                                  _CLKBInv_Xvtdown2Nbody=None,
                                  _CLKBInv_PMOSXvt2NMOSXvt=None,
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

        if _CDAC_Folding == True and _NumofBit < 4:
            raise Exception("현재 ADC Generation code에서 CDAC Folding Option은 4Bit이상에서 사용 가능합니다.")

        print('###############################################')
        print('##                   {}Bit                   ##'.format(_NumofBit))
        print('##                 SAR Logic                 ##')
        print('##            Calculation_Start!!            ##')
        print('###############################################')

        _Caculation_Parameters1 = copy.deepcopy(
            L00_SARLogicWtComparator_KJH._SARLogicWtComparator._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters1['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters1['_NumofBit'] = _NumofBit
        _Caculation_Parameters1['_Test_distance'] = _Test_distance
        _Caculation_Parameters1['_Routing_width'] = _Routing_width
        _Caculation_Parameters1['_Routing_distance'] = _Routing_distance

        _Caculation_Parameters1['_SARLogic_YWidthOfCLKSrc'] = _SARLogic_YWidthOfCLKSrc
        _Caculation_Parameters1['_SARLogic_SpaceBtwCLKSrcAndCLKSamp'] = _SARLogic_SpaceBtwCLKSrcAndCLKSamp
        _Caculation_Parameters1['_SARLogic_YWidthOfCLKSamp'] = _SARLogic_YWidthOfCLKSamp
        _Caculation_Parameters1['_SARLogic_YWidthOfCompOut'] = _SARLogic_YWidthOfCompOut
        _Caculation_Parameters1['_SARLogic_SpaceBtwCompOutAndCLKDout'] = _SARLogic_SpaceBtwCompOutAndCLKDout
        _Caculation_Parameters1['_SARLogic_YWidthOfCLKDout'] = _SARLogic_YWidthOfCLKDout
        ## DFF Common
        _Caculation_Parameters1['_SARLogic_DFF_Pbody_NumCont'] = _SARLogic_DFF_Pbody_NumCont
        _Caculation_Parameters1['_SARLogic_DFF_Nbody_NumCont'] = _SARLogic_DFF_Nbody_NumCont
        _Caculation_Parameters1['_SARLogic_DFF_PMOSXvt2NMOSXvt'] = _SARLogic_DFF_PMOSXvt2NMOSXvt
        _Caculation_Parameters1['_SARLogic_DFF_XvtTop2Pbody'] = _SARLogic_DFF_XvtTop2Pbody
        _Caculation_Parameters1['_SARLogic_DFF_Xvtdown2Nbody'] = _SARLogic_DFF_Xvtdown2Nbody

        ## Master Xgate1
        ## Xgate NMOS
        _Caculation_Parameters1['_SARLogic_Mst_Xgate1_NMOS_NumberofGate'] = _SARLogic_Mst_Xgate1_NMOS_NumberofGate
        _Caculation_Parameters1['_SARLogic_Mst_Xgate1_NMOS_ChannelWidth'] = _SARLogic_Mst_Xgate1_NMOS_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Mst_Xgate1_NMOS_ChannelLength'] = _SARLogic_Mst_Xgate1_NMOS_ChannelLength
        _Caculation_Parameters1['_SARLogic_Mst_Xgate1_NMOS_XVT'] = _SARLogic_Mst_Xgate1_NMOS_XVT
        _Caculation_Parameters1['_SARLogic_Mst_Xgate1_NMOS_POGate_Comb_length'] = _SARLogic_Mst_Xgate1_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_SARLogic_Mst_Xgate1_PMOS_NumberofGate'] = _SARLogic_Mst_Xgate1_PMOS_NumberofGate
        _Caculation_Parameters1['_SARLogic_Mst_Xgate1_PMOS_ChannelWidth'] = _SARLogic_Mst_Xgate1_PMOS_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Mst_Xgate1_PMOS_ChannelLength'] = _SARLogic_Mst_Xgate1_PMOS_ChannelLength
        _Caculation_Parameters1['_SARLogic_Mst_Xgate1_PMOS_XVT'] = _SARLogic_Mst_Xgate1_PMOS_XVT
        _Caculation_Parameters1['_SARLogic_Mst_Xgate1_PMOS_POGate_Comb_length'] = _SARLogic_Mst_Xgate1_PMOS_POGate_Comb_length

        ## Master Xgate2
        ## Xgate NMOS
        _Caculation_Parameters1['_SARLogic_Mst_Xgate2_NMOS_NumberofGate'] = _SARLogic_Mst_Xgate2_NMOS_NumberofGate
        _Caculation_Parameters1['_SARLogic_Mst_Xgate2_NMOS_ChannelWidth'] = _SARLogic_Mst_Xgate2_NMOS_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Mst_Xgate2_NMOS_ChannelLength'] = _SARLogic_Mst_Xgate2_NMOS_ChannelLength
        _Caculation_Parameters1['_SARLogic_Mst_Xgate2_NMOS_XVT'] = _SARLogic_Mst_Xgate2_NMOS_XVT
        _Caculation_Parameters1['_SARLogic_Mst_Xgate2_NMOS_POGate_Comb_length'] = _SARLogic_Mst_Xgate2_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_SARLogic_Mst_Xgate2_PMOS_NumberofGate'] = _SARLogic_Mst_Xgate2_PMOS_NumberofGate
        _Caculation_Parameters1['_SARLogic_Mst_Xgate2_PMOS_ChannelWidth'] = _SARLogic_Mst_Xgate2_PMOS_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Mst_Xgate2_PMOS_ChannelLength'] = _SARLogic_Mst_Xgate2_PMOS_ChannelLength
        _Caculation_Parameters1['_SARLogic_Mst_Xgate2_PMOS_XVT'] = _SARLogic_Mst_Xgate2_PMOS_XVT
        _Caculation_Parameters1['_SARLogic_Mst_Xgate2_PMOS_POGate_Comb_length'] = _SARLogic_Mst_Xgate2_PMOS_POGate_Comb_length

        ## Master Nor1
        ## NMOS common
        _Caculation_Parameters1['_SARLogic_Mst_Nor1_NMOS_XVT'] = _SARLogic_Mst_Nor1_NMOS_XVT

        ## Nor1 NMOSA
        _Caculation_Parameters1['_SARLogic_Mst_Nor1_NMOSA_NumberofGate'] = _SARLogic_Mst_Nor1_NMOSA_NumberofGate
        _Caculation_Parameters1['_SARLogic_Mst_Nor1_NMOSA_ChannelWidth'] = _SARLogic_Mst_Nor1_NMOSA_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Mst_Nor1_NMOSA_ChannelLength'] = _SARLogic_Mst_Nor1_NMOSA_ChannelLength
        _Caculation_Parameters1['_SARLogic_Mst_Nor1_NMOSA_POGate_Comb_length'] = _SARLogic_Mst_Nor1_NMOSA_POGate_Comb_length

        ## Nor1 NMOSB
        _Caculation_Parameters1['_SARLogic_Mst_Nor1_NMOSB_NumberofGate'] = _SARLogic_Mst_Nor1_NMOSB_NumberofGate
        _Caculation_Parameters1['_SARLogic_Mst_Nor1_NMOSB_ChannelWidth'] = _SARLogic_Mst_Nor1_NMOSB_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Mst_Nor1_NMOSB_ChannelLength'] = _SARLogic_Mst_Nor1_NMOSB_ChannelLength
        _Caculation_Parameters1['_SARLogic_Mst_Nor1_NMOSB_POGate_Comb_length'] = _SARLogic_Mst_Nor1_NMOSB_POGate_Comb_length

        ## PMOS common
        _Caculation_Parameters1['_SARLogic_Mst_Nor1_PMOS_XVT'] = _SARLogic_Mst_Nor1_PMOS_XVT

        ## Nor1 PMOSA
        _Caculation_Parameters1['_SARLogic_Mst_Nor1_PMOSA_NumberofGate'] = _SARLogic_Mst_Nor1_PMOSA_NumberofGate
        _Caculation_Parameters1['_SARLogic_Mst_Nor1_PMOSA_ChannelWidth'] = _SARLogic_Mst_Nor1_PMOSA_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Mst_Nor1_PMOSA_ChannelLength'] = _SARLogic_Mst_Nor1_PMOSA_ChannelLength
        _Caculation_Parameters1['_SARLogic_Mst_Nor1_PMOSA_POGate_Comb_length'] = _SARLogic_Mst_Nor1_PMOSA_POGate_Comb_length

        ## Nor1 PMOSB
        _Caculation_Parameters1['_SARLogic_Mst_Nor1_PMOSB_NumberofGate'] = _SARLogic_Mst_Nor1_PMOSB_NumberofGate
        _Caculation_Parameters1['_SARLogic_Mst_Nor1_PMOSB_ChannelWidth'] = _SARLogic_Mst_Nor1_PMOSB_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Mst_Nor1_PMOSB_ChannelLength'] = _SARLogic_Mst_Nor1_PMOSB_ChannelLength
        _Caculation_Parameters1['_SARLogic_Mst_Nor1_PMOSB_POGate_Comb_length'] = _SARLogic_Mst_Nor1_PMOSB_POGate_Comb_length

        ## Master Nor2
        ## NMOS common
        _Caculation_Parameters1['_SARLogic_Mst_Nor2_NMOS_XVT'] = _SARLogic_Mst_Nor2_NMOS_XVT

        ## Nor2 NMOSA
        _Caculation_Parameters1['_SARLogic_Mst_Nor2_NMOSA_NumberofGate'] = _SARLogic_Mst_Nor2_NMOSA_NumberofGate
        _Caculation_Parameters1['_SARLogic_Mst_Nor2_NMOSA_ChannelWidth'] = _SARLogic_Mst_Nor2_NMOSA_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Mst_Nor2_NMOSA_ChannelLength'] = _SARLogic_Mst_Nor2_NMOSA_ChannelLength
        _Caculation_Parameters1['_SARLogic_Mst_Nor2_NMOSA_POGate_Comb_length'] = _SARLogic_Mst_Nor2_NMOSA_POGate_Comb_length

        ## Nor2 NMOSB
        _Caculation_Parameters1['_SARLogic_Mst_Nor2_NMOSB_NumberofGate'] = _SARLogic_Mst_Nor2_NMOSB_NumberofGate
        _Caculation_Parameters1['_SARLogic_Mst_Nor2_NMOSB_ChannelWidth'] = _SARLogic_Mst_Nor2_NMOSB_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Mst_Nor2_NMOSB_ChannelLength'] = _SARLogic_Mst_Nor2_NMOSB_ChannelLength
        _Caculation_Parameters1['_SARLogic_Mst_Nor2_NMOSB_POGate_Comb_length'] = _SARLogic_Mst_Nor2_NMOSB_POGate_Comb_length

        ## PMOS common
        _Caculation_Parameters1['_SARLogic_Mst_Nor2_PMOS_XVT'] = _SARLogic_Mst_Nor2_PMOS_XVT

        ## Nor2 PMOSA
        _Caculation_Parameters1['_SARLogic_Mst_Nor2_PMOSA_NumberofGate'] = _SARLogic_Mst_Nor2_PMOSA_NumberofGate
        _Caculation_Parameters1['_SARLogic_Mst_Nor2_PMOSA_ChannelWidth'] = _SARLogic_Mst_Nor2_PMOSA_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Mst_Nor2_PMOSA_ChannelLength'] = _SARLogic_Mst_Nor2_PMOSA_ChannelLength
        _Caculation_Parameters1['_SARLogic_Mst_Nor2_PMOSA_POGate_Comb_length'] = _SARLogic_Mst_Nor2_PMOSA_POGate_Comb_length

        ## Nor2 PMOSB
        _Caculation_Parameters1['_SARLogic_Mst_Nor2_PMOSB_NumberofGate'] = _SARLogic_Mst_Nor2_PMOSB_NumberofGate
        _Caculation_Parameters1['_SARLogic_Mst_Nor2_PMOSB_ChannelWidth'] = _SARLogic_Mst_Nor2_PMOSB_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Mst_Nor2_PMOSB_ChannelLength'] = _SARLogic_Mst_Nor2_PMOSB_ChannelLength
        _Caculation_Parameters1['_SARLogic_Mst_Nor2_PMOSB_POGate_Comb_length'] = _SARLogic_Mst_Nor2_PMOSB_POGate_Comb_length

        ## Master Inv1
        ## Xgate NMOS
        _Caculation_Parameters1['_SARLogic_Mst_Inv1_NMOS_NumberofGate'] = _SARLogic_Mst_Inv1_NMOS_NumberofGate
        _Caculation_Parameters1['_SARLogic_Mst_Inv1_NMOS_ChannelWidth'] = _SARLogic_Mst_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Mst_Inv1_NMOS_ChannelLength'] = _SARLogic_Mst_Inv1_NMOS_ChannelLength
        _Caculation_Parameters1['_SARLogic_Mst_Inv1_NMOS_XVT'] = _SARLogic_Mst_Inv1_NMOS_XVT
        _Caculation_Parameters1['_SARLogic_Mst_Inv1_NMOS_POGate_Comb_length'] = _SARLogic_Mst_Inv1_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_SARLogic_Mst_Inv1_PMOS_NumberofGate'] = _SARLogic_Mst_Inv1_PMOS_NumberofGate
        _Caculation_Parameters1['_SARLogic_Mst_Inv1_PMOS_ChannelWidth'] = _SARLogic_Mst_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Mst_Inv1_PMOS_ChannelLength'] = _SARLogic_Mst_Inv1_PMOS_ChannelLength
        _Caculation_Parameters1['_SARLogic_Mst_Inv1_PMOS_XVT'] = _SARLogic_Mst_Inv1_PMOS_XVT
        _Caculation_Parameters1['_SARLogic_Mst_Inv1_PMOS_POGate_Comb_length'] = _SARLogic_Mst_Inv1_PMOS_POGate_Comb_length

        ## Master Inv2 : Set driver
        ## Xgate NMOS
        _Caculation_Parameters1['_SARLogic_Mst_Inv2_NMOS_NumberofGate'] = _SARLogic_Mst_Inv2_NMOS_NumberofGate
        _Caculation_Parameters1['_SARLogic_Mst_Inv2_NMOS_ChannelWidth'] = _SARLogic_Mst_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Mst_Inv2_NMOS_ChannelLength'] = _SARLogic_Mst_Inv2_NMOS_ChannelLength
        _Caculation_Parameters1['_SARLogic_Mst_Inv2_NMOS_XVT'] = _SARLogic_Mst_Inv2_NMOS_XVT
        _Caculation_Parameters1['_SARLogic_Mst_Inv2_NMOS_POGate_Comb_length'] = _SARLogic_Mst_Inv2_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_SARLogic_Mst_Inv2_PMOS_NumberofGate'] = _SARLogic_Mst_Inv2_PMOS_NumberofGate
        _Caculation_Parameters1['_SARLogic_Mst_Inv2_PMOS_ChannelWidth'] = _SARLogic_Mst_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Mst_Inv2_PMOS_ChannelLength'] = _SARLogic_Mst_Inv2_PMOS_ChannelLength
        _Caculation_Parameters1['_SARLogic_Mst_Inv2_PMOS_XVT'] = _SARLogic_Mst_Inv2_PMOS_XVT
        _Caculation_Parameters1['_SARLogic_Mst_Inv2_PMOS_POGate_Comb_length'] = _SARLogic_Mst_Inv2_PMOS_POGate_Comb_length

        ## Master Inv3 : Clock driver
        ## Xgate NMOS
        _Caculation_Parameters1['_SARLogic_Mst_Inv3_NMOS_NumberofGate'] = _SARLogic_Mst_Inv3_NMOS_NumberofGate
        _Caculation_Parameters1['_SARLogic_Mst_Inv3_NMOS_ChannelWidth'] = _SARLogic_Mst_Inv3_NMOS_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Mst_Inv3_NMOS_ChannelLength'] = _SARLogic_Mst_Inv3_NMOS_ChannelLength
        _Caculation_Parameters1['_SARLogic_Mst_Inv3_NMOS_XVT'] = _SARLogic_Mst_Inv3_NMOS_XVT
        _Caculation_Parameters1['_SARLogic_Mst_Inv3_NMOS_POGate_Comb_length'] = _SARLogic_Mst_Inv3_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_SARLogic_Mst_Inv3_PMOS_NumberofGate'] = _SARLogic_Mst_Inv3_PMOS_NumberofGate
        _Caculation_Parameters1['_SARLogic_Mst_Inv3_PMOS_ChannelWidth'] = _SARLogic_Mst_Inv3_PMOS_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Mst_Inv3_PMOS_ChannelLength'] = _SARLogic_Mst_Inv3_PMOS_ChannelLength
        _Caculation_Parameters1['_SARLogic_Mst_Inv3_PMOS_XVT'] = _SARLogic_Mst_Inv3_PMOS_XVT
        _Caculation_Parameters1['_SARLogic_Mst_Inv3_PMOS_POGate_Comb_length'] = _SARLogic_Mst_Inv3_PMOS_POGate_Comb_length

        ## Slave Xgate1
        ## Xgate NMOS
        _Caculation_Parameters1['_SARLogic_Slv_Xgate1_NMOS_NumberofGate'] = _SARLogic_Slv_Xgate1_NMOS_NumberofGate
        _Caculation_Parameters1['_SARLogic_Slv_Xgate1_NMOS_ChannelWidth'] = _SARLogic_Slv_Xgate1_NMOS_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Slv_Xgate1_NMOS_ChannelLength'] = _SARLogic_Slv_Xgate1_NMOS_ChannelLength
        _Caculation_Parameters1['_SARLogic_Slv_Xgate1_NMOS_XVT'] = _SARLogic_Slv_Xgate1_NMOS_XVT
        _Caculation_Parameters1['_SARLogic_Slv_Xgate1_NMOS_POGate_Comb_length'] = _SARLogic_Slv_Xgate1_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_SARLogic_Slv_Xgate1_PMOS_NumberofGate'] = _SARLogic_Slv_Xgate1_PMOS_NumberofGate
        _Caculation_Parameters1['_SARLogic_Slv_Xgate1_PMOS_ChannelWidth'] = _SARLogic_Slv_Xgate1_PMOS_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Slv_Xgate1_PMOS_ChannelLength'] = _SARLogic_Slv_Xgate1_PMOS_ChannelLength
        _Caculation_Parameters1['_SARLogic_Slv_Xgate1_PMOS_XVT'] = _SARLogic_Slv_Xgate1_PMOS_XVT
        _Caculation_Parameters1['_SARLogic_Slv_Xgate1_PMOS_POGate_Comb_length'] = _SARLogic_Slv_Xgate1_PMOS_POGate_Comb_length

        ## Slave Xgate2
        ## Xgate NMOS
        _Caculation_Parameters1['_SARLogic_Slv_Xgate2_NMOS_NumberofGate'] = _SARLogic_Slv_Xgate2_NMOS_NumberofGate
        _Caculation_Parameters1['_SARLogic_Slv_Xgate2_NMOS_ChannelWidth'] = _SARLogic_Slv_Xgate2_NMOS_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Slv_Xgate2_NMOS_ChannelLength'] = _SARLogic_Slv_Xgate2_NMOS_ChannelLength
        _Caculation_Parameters1['_SARLogic_Slv_Xgate2_NMOS_XVT'] = _SARLogic_Slv_Xgate2_NMOS_XVT
        _Caculation_Parameters1['_SARLogic_Slv_Xgate2_NMOS_POGate_Comb_length'] = _SARLogic_Slv_Xgate2_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_SARLogic_Slv_Xgate2_PMOS_NumberofGate'] = _SARLogic_Slv_Xgate2_PMOS_NumberofGate
        _Caculation_Parameters1['_SARLogic_Slv_Xgate2_PMOS_ChannelWidth'] = _SARLogic_Slv_Xgate2_PMOS_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Slv_Xgate2_PMOS_ChannelLength'] = _SARLogic_Slv_Xgate2_PMOS_ChannelLength
        _Caculation_Parameters1['_SARLogic_Slv_Xgate2_PMOS_XVT'] = _SARLogic_Slv_Xgate2_PMOS_XVT
        _Caculation_Parameters1['_SARLogic_Slv_Xgate2_PMOS_POGate_Comb_length'] = _SARLogic_Slv_Xgate2_PMOS_POGate_Comb_length

        ## Slave Nor1
        ## NMOS common
        _Caculation_Parameters1['_SARLogic_Slv_Nor1_NMOS_XVT'] = _SARLogic_Slv_Nor1_NMOS_XVT

        ## Nor1 NMOSA
        _Caculation_Parameters1['_SARLogic_Slv_Nor1_NMOSA_NumberofGate'] = _SARLogic_Slv_Nor1_NMOSA_NumberofGate
        _Caculation_Parameters1['_SARLogic_Slv_Nor1_NMOSA_ChannelWidth'] = _SARLogic_Slv_Nor1_NMOSA_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Slv_Nor1_NMOSA_ChannelLength'] = _SARLogic_Slv_Nor1_NMOSA_ChannelLength
        _Caculation_Parameters1['_SARLogic_Slv_Nor1_NMOSA_POGate_Comb_length'] = _SARLogic_Slv_Nor1_NMOSA_POGate_Comb_length

        ## Nor1 NMOSB
        _Caculation_Parameters1['_SARLogic_Slv_Nor1_NMOSB_NumberofGate'] = _SARLogic_Slv_Nor1_NMOSB_NumberofGate
        _Caculation_Parameters1['_SARLogic_Slv_Nor1_NMOSB_ChannelWidth'] = _SARLogic_Slv_Nor1_NMOSB_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Slv_Nor1_NMOSB_ChannelLength'] = _SARLogic_Slv_Nor1_NMOSB_ChannelLength
        _Caculation_Parameters1['_SARLogic_Slv_Nor1_NMOSB_POGate_Comb_length'] = _SARLogic_Slv_Nor1_NMOSB_POGate_Comb_length

        ## PMOS common
        _Caculation_Parameters1['_SARLogic_Slv_Nor1_PMOS_XVT'] = _SARLogic_Slv_Nor1_PMOS_XVT

        ## Nor1 PMOSA
        _Caculation_Parameters1['_SARLogic_Slv_Nor1_PMOSA_NumberofGate'] = _SARLogic_Slv_Nor1_PMOSA_NumberofGate
        _Caculation_Parameters1['_SARLogic_Slv_Nor1_PMOSA_ChannelWidth'] = _SARLogic_Slv_Nor1_PMOSA_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Slv_Nor1_PMOSA_ChannelLength'] = _SARLogic_Slv_Nor1_PMOSA_ChannelLength
        _Caculation_Parameters1['_SARLogic_Slv_Nor1_PMOSA_POGate_Comb_length'] = _SARLogic_Slv_Nor1_PMOSA_POGate_Comb_length

        ## Nor1 PMOSB
        _Caculation_Parameters1['_SARLogic_Slv_Nor1_PMOSB_NumberofGate'] = _SARLogic_Slv_Nor1_PMOSB_NumberofGate
        _Caculation_Parameters1['_SARLogic_Slv_Nor1_PMOSB_ChannelWidth'] = _SARLogic_Slv_Nor1_PMOSB_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Slv_Nor1_PMOSB_ChannelLength'] = _SARLogic_Slv_Nor1_PMOSB_ChannelLength
        _Caculation_Parameters1['_SARLogic_Slv_Nor1_PMOSB_POGate_Comb_length'] = _SARLogic_Slv_Nor1_PMOSB_POGate_Comb_length

        ## Slave Nor2
        ## NMOS common
        _Caculation_Parameters1['_SARLogic_Slv_Nor2_NMOS_XVT'] = _SARLogic_Slv_Nor2_NMOS_XVT

        ## Nor2 NMOSA
        _Caculation_Parameters1['_SARLogic_Slv_Nor2_NMOSA_NumberofGate'] = _SARLogic_Slv_Nor2_NMOSA_NumberofGate
        _Caculation_Parameters1['_SARLogic_Slv_Nor2_NMOSA_ChannelWidth'] = _SARLogic_Slv_Nor2_NMOSA_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Slv_Nor2_NMOSA_ChannelLength'] = _SARLogic_Slv_Nor2_NMOSA_ChannelLength
        _Caculation_Parameters1['_SARLogic_Slv_Nor2_NMOSA_POGate_Comb_length'] = _SARLogic_Slv_Nor2_NMOSA_POGate_Comb_length

        ## Nor2 NMOSB
        _Caculation_Parameters1['_SARLogic_Slv_Nor2_NMOSB_NumberofGate'] = _SARLogic_Slv_Nor2_NMOSB_NumberofGate
        _Caculation_Parameters1['_SARLogic_Slv_Nor2_NMOSB_ChannelWidth'] = _SARLogic_Slv_Nor2_NMOSB_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Slv_Nor2_NMOSB_ChannelLength'] = _SARLogic_Slv_Nor2_NMOSB_ChannelLength
        _Caculation_Parameters1['_SARLogic_Slv_Nor2_NMOSB_POGate_Comb_length'] = _SARLogic_Slv_Nor2_NMOSB_POGate_Comb_length

        ## PMOS common
        _Caculation_Parameters1['_SARLogic_Slv_Nor2_PMOS_XVT'] = _SARLogic_Slv_Nor2_PMOS_XVT

        ## Nor2 PMOSA
        _Caculation_Parameters1['_SARLogic_Slv_Nor2_PMOSA_NumberofGate'] = _SARLogic_Slv_Nor2_PMOSA_NumberofGate
        _Caculation_Parameters1['_SARLogic_Slv_Nor2_PMOSA_ChannelWidth'] = _SARLogic_Slv_Nor2_PMOSA_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Slv_Nor2_PMOSA_ChannelLength'] = _SARLogic_Slv_Nor2_PMOSA_ChannelLength
        _Caculation_Parameters1['_SARLogic_Slv_Nor2_PMOSA_POGate_Comb_length'] = _SARLogic_Slv_Nor2_PMOSA_POGate_Comb_length

        ## Nor2 PMOSB
        _Caculation_Parameters1['_SARLogic_Slv_Nor2_PMOSB_NumberofGate'] = _SARLogic_Slv_Nor2_PMOSB_NumberofGate
        _Caculation_Parameters1['_SARLogic_Slv_Nor2_PMOSB_ChannelWidth'] = _SARLogic_Slv_Nor2_PMOSB_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Slv_Nor2_PMOSB_ChannelLength'] = _SARLogic_Slv_Nor2_PMOSB_ChannelLength
        _Caculation_Parameters1['_SARLogic_Slv_Nor2_PMOSB_POGate_Comb_length'] = _SARLogic_Slv_Nor2_PMOSB_POGate_Comb_length

        ## Slave Inv1 : ReSet pre-driver
        ## Xgate NMOS
        _Caculation_Parameters1['_SARLogic_Slv_Inv1_NMOS_NumberofGate'] = _SARLogic_Slv_Inv1_NMOS_NumberofGate
        _Caculation_Parameters1['_SARLogic_Slv_Inv1_NMOS_ChannelWidth'] = _SARLogic_Slv_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Slv_Inv1_NMOS_ChannelLength'] = _SARLogic_Slv_Inv1_NMOS_ChannelLength
        _Caculation_Parameters1['_SARLogic_Slv_Inv1_NMOS_XVT'] = _SARLogic_Slv_Inv1_NMOS_XVT
        _Caculation_Parameters1['_SARLogic_Slv_Inv1_NMOS_POGate_Comb_length'] = _SARLogic_Slv_Inv1_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_SARLogic_Slv_Inv1_PMOS_NumberofGate'] = _SARLogic_Slv_Inv1_PMOS_NumberofGate
        _Caculation_Parameters1['_SARLogic_Slv_Inv1_PMOS_ChannelWidth'] = _SARLogic_Slv_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Slv_Inv1_PMOS_ChannelLength'] = _SARLogic_Slv_Inv1_PMOS_ChannelLength
        _Caculation_Parameters1['_SARLogic_Slv_Inv1_PMOS_XVT'] = _SARLogic_Slv_Inv1_PMOS_XVT
        _Caculation_Parameters1['_SARLogic_Slv_Inv1_PMOS_POGate_Comb_length'] = _SARLogic_Slv_Inv1_PMOS_POGate_Comb_length

        ## Slave Inv2 : ReSet driver
        ## Xgate NMOS
        _Caculation_Parameters1['_SARLogic_Slv_Inv2_NMOS_NumberofGate'] = _SARLogic_Slv_Inv2_NMOS_NumberofGate
        _Caculation_Parameters1['_SARLogic_Slv_Inv2_NMOS_ChannelWidth'] = _SARLogic_Slv_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Slv_Inv2_NMOS_ChannelLength'] = _SARLogic_Slv_Inv2_NMOS_ChannelLength
        _Caculation_Parameters1['_SARLogic_Slv_Inv2_NMOS_XVT'] = _SARLogic_Slv_Inv2_NMOS_XVT
        _Caculation_Parameters1['_SARLogic_Slv_Inv2_NMOS_POGate_Comb_length'] = _SARLogic_Slv_Inv2_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_SARLogic_Slv_Inv2_PMOS_NumberofGate'] = _SARLogic_Slv_Inv2_PMOS_NumberofGate
        _Caculation_Parameters1['_SARLogic_Slv_Inv2_PMOS_ChannelWidth'] = _SARLogic_Slv_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Slv_Inv2_PMOS_ChannelLength'] = _SARLogic_Slv_Inv2_PMOS_ChannelLength
        _Caculation_Parameters1['_SARLogic_Slv_Inv2_PMOS_XVT'] = _SARLogic_Slv_Inv2_PMOS_XVT
        _Caculation_Parameters1['_SARLogic_Slv_Inv2_PMOS_POGate_Comb_length'] = _SARLogic_Slv_Inv2_PMOS_POGate_Comb_length

        ## Slave Inv3 : Qb driver
        ## Xgate NMOS
        _Caculation_Parameters1['_SARLogic_Slv_Inv3_NMOS_NumberofGate'] = _SARLogic_Slv_Inv3_NMOS_NumberofGate
        _Caculation_Parameters1['_SARLogic_Slv_Inv3_NMOS_ChannelWidth'] = _SARLogic_Slv_Inv3_NMOS_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Slv_Inv3_NMOS_ChannelLength'] = _SARLogic_Slv_Inv3_NMOS_ChannelLength
        _Caculation_Parameters1['_SARLogic_Slv_Inv3_NMOS_XVT'] = _SARLogic_Slv_Inv3_NMOS_XVT
        _Caculation_Parameters1['_SARLogic_Slv_Inv3_NMOS_POGate_Comb_length'] = _SARLogic_Slv_Inv3_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_SARLogic_Slv_Inv3_PMOS_NumberofGate'] = _SARLogic_Slv_Inv3_PMOS_NumberofGate
        _Caculation_Parameters1['_SARLogic_Slv_Inv3_PMOS_ChannelWidth'] = _SARLogic_Slv_Inv3_PMOS_ChannelWidth
        _Caculation_Parameters1['_SARLogic_Slv_Inv3_PMOS_ChannelLength'] = _SARLogic_Slv_Inv3_PMOS_ChannelLength
        _Caculation_Parameters1['_SARLogic_Slv_Inv3_PMOS_XVT'] = _SARLogic_Slv_Inv3_PMOS_XVT
        _Caculation_Parameters1['_SARLogic_Slv_Inv3_PMOS_POGate_Comb_length'] = _SARLogic_Slv_Inv3_PMOS_POGate_Comb_length

        ## CLK Buf Tree Top
        _Caculation_Parameters1['_SARLogic_CLKBufTreeTop_NumOfStage'] = _SARLogic_CLKBufTreeTop_NumOfStage
        _Caculation_Parameters1['_SARLogic_CLKBufTreeTop_CLKSampBuf_SizeByStage'] = _SARLogic_CLKBufTreeTop_CLKSampBuf_SizeByStage
        _Caculation_Parameters1['_SARLogic_CLKBufTreeTop_CLKSrcBuf_SizeByStage'] = _SARLogic_CLKBufTreeTop_CLKSrcBuf_SizeByStage
        _Caculation_Parameters1['_SARLogic_CLKBufTreeTop_XOffSet'] = _SARLogic_CLKBufTreeTop_XOffSet

        _Caculation_Parameters1['_SARLogic_CLKBufTreeTop_Inv_NMOS_ChannelWidth'] = _SARLogic_CLKBufTreeTop_Inv_NMOS_ChannelWidth
        _Caculation_Parameters1['_SARLogic_CLKBufTreeTop_Inv_NMOS_ChannelLength'] = _SARLogic_CLKBufTreeTop_Inv_NMOS_ChannelLength
        _Caculation_Parameters1['_SARLogic_CLKBufTreeTop_Inv_NMOS_NumberofGate'] = _SARLogic_CLKBufTreeTop_Inv_NMOS_NumberofGate
        _Caculation_Parameters1['_SARLogic_CLKBufTreeTop_Inv_NMOS_XVT'] = _SARLogic_CLKBufTreeTop_Inv_NMOS_XVT
        _Caculation_Parameters1['_SARLogic_CLKBufTreeTop_Inv_NMOS_POGate_Comb_length'] = _SARLogic_CLKBufTreeTop_Inv_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_SARLogic_CLKBufTreeTop_Inv_PMOS_ChannelWidth'] = _SARLogic_CLKBufTreeTop_Inv_PMOS_ChannelWidth
        _Caculation_Parameters1['_SARLogic_CLKBufTreeTop_Inv_PMOS_ChannelLength'] = _SARLogic_CLKBufTreeTop_Inv_PMOS_ChannelLength
        _Caculation_Parameters1['_SARLogic_CLKBufTreeTop_Inv_PMOS_NumberofGate'] = _SARLogic_CLKBufTreeTop_Inv_PMOS_NumberofGate
        _Caculation_Parameters1['_SARLogic_CLKBufTreeTop_Inv_PMOS_XVT'] = _SARLogic_CLKBufTreeTop_Inv_PMOS_XVT
        _Caculation_Parameters1['_SARLogic_CLKBufTreeTop_Inv_PMOS_POGate_Comb_length'] = _SARLogic_CLKBufTreeTop_Inv_PMOS_POGate_Comb_length

        _Caculation_Parameters1['_SARLogic_CLKBufTreeTop_NMOS_Pbody_NumCont'] = _SARLogic_CLKBufTreeTop_NMOS_Pbody_NumCont
        _Caculation_Parameters1['_SARLogic_CLKBufTreeTop_NMOS_Pbody_XvtTop2Pbody'] = _SARLogic_CLKBufTreeTop_NMOS_Pbody_XvtTop2Pbody
        _Caculation_Parameters1['_SARLogic_CLKBufTreeTop_PMOS_Nbody_NumCont'] = _SARLogic_CLKBufTreeTop_PMOS_Nbody_NumCont
        _Caculation_Parameters1['_SARLogic_CLKBufTreeTop_PMOS_Nbody_Xvtdown2Nbody'] = _SARLogic_CLKBufTreeTop_PMOS_Nbody_Xvtdown2Nbody
        _Caculation_Parameters1['_SARLogic_CLKBufTreeTop_PMOSXvt2NMOSXvt'] = _SARLogic_CLKBufTreeTop_PMOSXvt2NMOSXvt

        ## CLK Buf Tree Bot
        _Caculation_Parameters1['_SARLogic_CLKBufTreeBot_NumOfStage'] = _SARLogic_CLKBufTreeBot_NumOfStage
        _Caculation_Parameters1['_SARLogic_CLKBufTreeBot_CompOutBuf_SizeByStage'] = _SARLogic_CLKBufTreeBot_CompOutBuf_SizeByStage
        _Caculation_Parameters1['_SARLogic_CLKBufTreeBot_CLKDoutBuf_SizeByStage'] = _SARLogic_CLKBufTreeBot_CLKDoutBuf_SizeByStage
        _Caculation_Parameters1['_SARLogic_CLKBufTreeBot_XOffSet'] = _SARLogic_CLKBufTreeBot_XOffSet

        _Caculation_Parameters1['_SARLogic_CLKBufTreeBot_Inv_NMOS_ChannelWidth'] = _SARLogic_CLKBufTreeBot_Inv_NMOS_ChannelWidth
        _Caculation_Parameters1['_SARLogic_CLKBufTreeBot_Inv_NMOS_ChannelLength'] = _SARLogic_CLKBufTreeBot_Inv_NMOS_ChannelLength
        _Caculation_Parameters1['_SARLogic_CLKBufTreeBot_Inv_NMOS_NumberofGate'] = _SARLogic_CLKBufTreeBot_Inv_NMOS_NumberofGate
        _Caculation_Parameters1['_SARLogic_CLKBufTreeBot_Inv_NMOS_XVT'] = _SARLogic_CLKBufTreeBot_Inv_NMOS_XVT
        _Caculation_Parameters1['_SARLogic_CLKBufTreeBot_Inv_NMOS_POGate_Comb_length'] = _SARLogic_CLKBufTreeBot_Inv_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_SARLogic_CLKBufTreeBot_Inv_PMOS_ChannelWidth'] = _SARLogic_CLKBufTreeBot_Inv_PMOS_ChannelWidth
        _Caculation_Parameters1['_SARLogic_CLKBufTreeBot_Inv_PMOS_ChannelLength'] = _SARLogic_CLKBufTreeBot_Inv_PMOS_ChannelLength
        _Caculation_Parameters1['_SARLogic_CLKBufTreeBot_Inv_PMOS_NumberofGate'] = _SARLogic_CLKBufTreeBot_Inv_PMOS_NumberofGate
        _Caculation_Parameters1['_SARLogic_CLKBufTreeBot_Inv_PMOS_XVT'] = _SARLogic_CLKBufTreeBot_Inv_PMOS_XVT
        _Caculation_Parameters1['_SARLogic_CLKBufTreeBot_Inv_PMOS_POGate_Comb_length'] = _SARLogic_CLKBufTreeBot_Inv_PMOS_POGate_Comb_length

        _Caculation_Parameters1['_SARLogic_CLKBufTreeBot_NMOS_Pbody_NumCont'] = _SARLogic_CLKBufTreeBot_NMOS_Pbody_NumCont
        _Caculation_Parameters1['_SARLogic_CLKBufTreeBot_NMOS_Pbody_XvtTop2Pbody'] = _SARLogic_CLKBufTreeBot_NMOS_Pbody_XvtTop2Pbody
        _Caculation_Parameters1['_SARLogic_CLKBufTreeBot_PMOS_Nbody_NumCont'] = _SARLogic_CLKBufTreeBot_PMOS_Nbody_NumCont
        _Caculation_Parameters1['_SARLogic_CLKBufTreeBot_PMOS_Nbody_Xvtdown2Nbody'] = _SARLogic_CLKBufTreeBot_PMOS_Nbody_Xvtdown2Nbody
        _Caculation_Parameters1['_SARLogic_CLKBufTreeBot_PMOSXvt2NMOSXvt'] = _SARLogic_CLKBufTreeBot_PMOSXvt2NMOSXvt

        _Caculation_Parameters1['_CDACPreDriver_Pbody_NumCont'] = _CDACPreDriver_Pbody_NumCont
        _Caculation_Parameters1['_CDACPreDriver_Nbody_NumCont'] = _CDACPreDriver_Nbody_NumCont
        _Caculation_Parameters1['_CDACPreDriver_PMOSXvt2NMOSXvt'] = _CDACPreDriver_PMOSXvt2NMOSXvt
        _Caculation_Parameters1['_CDACPreDriver_XvtTop2Pbody'] = _CDACPreDriver_XvtTop2Pbody
        _Caculation_Parameters1['_CDACPreDriver_Xvtdown2Nbody'] = _CDACPreDriver_Xvtdown2Nbody

        _Caculation_Parameters1['_CDACPreDriver_NumberofGate'] = _CDACPreDriver_NumberofGate
        _Caculation_Parameters1['_CDACPreDriver_ChannelLength'] = _CDACPreDriver_ChannelLength
        _Caculation_Parameters1['_CDACPreDriver_XVT'] = _CDACPreDriver_XVT

        _Caculation_Parameters1['_CLKDout_XVT_Common'] = _CLKDout_XVT_Common
        _Caculation_Parameters1['_CDACPreDriver_Inv_NMOS_ChannelWidth'] = _CDACPreDriver_Inv_NMOS_ChannelWidth
        _Caculation_Parameters1['_CDACPreDriver_Inv_NMOS_POGate_Comb_length'] = _CDACPreDriver_Inv_NMOS_POGate_Comb_length
        _Caculation_Parameters1['_CDACPreDriver_Inv_PMOS_ChannelWidth'] = _CDACPreDriver_Inv_PMOS_ChannelWidth
        _Caculation_Parameters1['_CDACPreDriver_Inv_PMOS_POGate_Comb_length'] = _CDACPreDriver_Inv_PMOS_POGate_Comb_length

        _Caculation_Parameters1['_CLKDout_Inv_NMOS_ChannelWidth'] = _CLKDout_Inv_NMOS_ChannelWidth
        _Caculation_Parameters1['_CLKDout_Inv_NMOS_ChannelLength'] = _CLKDout_Inv_NMOS_ChannelLength
        _Caculation_Parameters1['_CLKDout_Inv_NMOS_NumberofGate'] = _CLKDout_Inv_NMOS_NumberofGate
        _Caculation_Parameters1['_CLKDout_Inv_NMOS_POGate_Comb_length'] = _CLKDout_Inv_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_CLKDout_Inv_PMOS_ChannelWidth'] = _CLKDout_Inv_PMOS_ChannelWidth
        _Caculation_Parameters1['_CLKDout_Inv_PMOS_ChannelLength'] = _CLKDout_Inv_PMOS_ChannelLength
        _Caculation_Parameters1['_CLKDout_Inv_PMOS_NumberofGate'] = _CLKDout_Inv_PMOS_NumberofGate
        _Caculation_Parameters1['_CLKDout_Inv_PMOS_POGate_Comb_length'] = _CLKDout_Inv_PMOS_POGate_Comb_length

        _Caculation_Parameters1['_CLKDout_AND_NAND_NMOS_ChannelWidth'] = _CLKDout_AND_NAND_NMOS_ChannelWidth
        _Caculation_Parameters1['_CLKDout_AND_NAND_NMOS_ChannelLength'] = _CLKDout_AND_NAND_NMOS_ChannelLength
        _Caculation_Parameters1['_CLKDout_AND_NAND_NMOS_NumberofGate'] = _CLKDout_AND_NAND_NMOS_NumberofGate

        _Caculation_Parameters1['_CLKDout_AND_NAND_PMOS_ChannelWidth'] = _CLKDout_AND_NAND_PMOS_ChannelWidth
        _Caculation_Parameters1['_CLKDout_AND_NAND_PMOS_ChannelLength'] = _CLKDout_AND_NAND_PMOS_ChannelLength
        _Caculation_Parameters1['_CLKDout_AND_NAND_PMOS_NumberofGate'] = _CLKDout_AND_NAND_PMOS_NumberofGate

        _Caculation_Parameters1['_CLKDout_AND_Inv_NMOS_ChannelWidth'] = _CLKDout_AND_Inv_NMOS_ChannelWidth
        _Caculation_Parameters1['_CLKDout_AND_Inv_NMOS_ChannelLength'] = _CLKDout_AND_Inv_NMOS_ChannelLength
        _Caculation_Parameters1['_CLKDout_AND_Inv_NMOS_NumberofGate'] = _CLKDout_AND_Inv_NMOS_NumberofGate
        _Caculation_Parameters1['_CLKDout_AND_Inv_NMOS_POGate_Comb_length'] = _CLKDout_AND_Inv_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_CLKDout_AND_Inv_PMOS_ChannelWidth'] = _CLKDout_AND_Inv_PMOS_ChannelWidth
        _Caculation_Parameters1['_CLKDout_AND_Inv_PMOS_ChannelLength'] = _CLKDout_AND_Inv_PMOS_ChannelLength
        _Caculation_Parameters1['_CLKDout_AND_Inv_PMOS_NumberofGate'] = _CLKDout_AND_Inv_PMOS_NumberofGate
        _Caculation_Parameters1['_CLKDout_AND_Inv_PMOS_POGate_Comb_length'] = _CLKDout_AND_Inv_PMOS_POGate_Comb_length

        _Caculation_Parameters1['_Comp_SALatch_CLKinputPMOSFinger1'] = _Comp_SALatch_CLKinputPMOSFinger1
        _Caculation_Parameters1['_Comp_SALatch_CLKinputPMOSFinger2'] = _Comp_SALatch_CLKinputPMOSFinger2
        _Caculation_Parameters1['_Comp_SALatch_PMOSFinger'] = _Comp_SALatch_PMOSFinger
        _Caculation_Parameters1['_Comp_SALatch_PMOSChannelWidth'] = _Comp_SALatch_PMOSChannelWidth
        _Caculation_Parameters1['_Comp_SALatch_DATAinputNMOSFinger'] = _Comp_SALatch_DATAinputNMOSFinger
        _Caculation_Parameters1['_Comp_SALatch_NMOSFinger'] = _Comp_SALatch_NMOSFinger
        _Caculation_Parameters1['_Comp_SALatch_CLKinputNMOSFinger'] = _Comp_SALatch_CLKinputNMOSFinger
        _Caculation_Parameters1['_Comp_SALatch_NMOSChannelWidth'] = _Comp_SALatch_NMOSChannelWidth
        _Caculation_Parameters1['_Comp_SALatch_CLKinputNMOSChannelWidth'] = _Comp_SALatch_CLKinputNMOSChannelWidth
        _Caculation_Parameters1['_Comp_SALatch_ChannelLength'] = _Comp_SALatch_ChannelLength
        _Caculation_Parameters1['_Comp_SALatch_Dummy'] = _Comp_SALatch_Dummy
        _Caculation_Parameters1['_Comp_SALatch_XVT'] = _Comp_SALatch_XVT
        _Caculation_Parameters1['_Comp_SALatch_GuardringWidth'] = _Comp_SALatch_GuardringWidth
        _Caculation_Parameters1['_Comp_SALatch_Guardring'] = _Comp_SALatch_Guardring
        _Caculation_Parameters1['_Comp_SALatch_SlicerGuardringWidth'] = _Comp_SALatch_SlicerGuardringWidth
        _Caculation_Parameters1['_Comp_SALatch_SlicerGuardring'] = _Comp_SALatch_SlicerGuardring
        _Caculation_Parameters1['_Comp_SALatch_NumSupplyCOY'] = _Comp_SALatch_NumSupplyCOY
        _Caculation_Parameters1['_Comp_SALatch_NumSupplyCOX'] = _Comp_SALatch_NumSupplyCOX
        _Caculation_Parameters1['_Comp_SALatch_SupplyMet1XWidth'] = _Comp_SALatch_SupplyMet1XWidth
        _Caculation_Parameters1['_Comp_SALatch_SupplyMet1YWidth'] = _Comp_SALatch_SupplyMet1YWidth
        _Caculation_Parameters1['_Comp_SALatch_VDD2VSSHeight'] = _Comp_SALatch_VDD2VSSHeight
        _Caculation_Parameters1['_Comp_SALatch_NumVIAPoly2Met1COX'] = _Comp_SALatch_NumVIAPoly2Met1COX
        _Caculation_Parameters1['_Comp_SALatch_NumVIAPoly2Met1COY'] = _Comp_SALatch_NumVIAPoly2Met1COY
        _Caculation_Parameters1['_Comp_SALatch_NumVIAMet12COX'] = _Comp_SALatch_NumVIAMet12COX
        _Caculation_Parameters1['_Comp_SALatch_NumVIAMet12COY'] = _Comp_SALatch_NumVIAMet12COY
        _Caculation_Parameters1['_Comp_SALatch_PowerLine'] = _Comp_SALatch_PowerLine

        ## StrongARMLatch Output Buffer Sizing
        # Inverter1
        _Caculation_Parameters1['_Comp_SAOutBuf_Inv1_NMOS_ChannelWidth'] = _Comp_SAOutBuf_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters1['_Comp_SAOutBuf_Inv1_NMOS_ChannelLength'] = _Comp_SAOutBuf_Inv1_NMOS_ChannelLength
        _Caculation_Parameters1['_Comp_SAOutBuf_Inv1_NMOS_NumberofGate'] = _Comp_SAOutBuf_Inv1_NMOS_NumberofGate
        _Caculation_Parameters1['_Comp_SAOutBuf_Inv1_NMOS_XVT'] = _Comp_SAOutBuf_Inv1_NMOS_XVT
        _Caculation_Parameters1['_Comp_SAOutBuf_Inv1_NMOS_POGate_Comb_length'] = _Comp_SAOutBuf_Inv1_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_Comp_SAOutBuf_Inv1_PMOS_ChannelWidth'] = _Comp_SAOutBuf_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters1['_Comp_SAOutBuf_Inv1_PMOS_ChannelLength'] = _Comp_SAOutBuf_Inv1_PMOS_ChannelLength
        _Caculation_Parameters1['_Comp_SAOutBuf_Inv1_PMOS_NumberofGate'] = _Comp_SAOutBuf_Inv1_PMOS_NumberofGate
        _Caculation_Parameters1['_Comp_SAOutBuf_Inv1_PMOS_XVT'] = _Comp_SAOutBuf_Inv1_PMOS_XVT
        _Caculation_Parameters1['_Comp_SAOutBuf_Inv1_PMOS_POGate_Comb_length'] = _Comp_SAOutBuf_Inv1_PMOS_POGate_Comb_length

        # Inverter2
        _Caculation_Parameters1['_Comp_SAOutBuf_Inv2_NMOS_ChannelWidth'] = _Comp_SAOutBuf_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters1['_Comp_SAOutBuf_Inv2_NMOS_ChannelLength'] = _Comp_SAOutBuf_Inv2_NMOS_ChannelLength
        _Caculation_Parameters1['_Comp_SAOutBuf_Inv2_NMOS_NumberofGate'] = _Comp_SAOutBuf_Inv2_NMOS_NumberofGate
        _Caculation_Parameters1['_Comp_SAOutBuf_Inv2_NMOS_XVT'] = _Comp_SAOutBuf_Inv2_NMOS_XVT
        _Caculation_Parameters1['_Comp_SAOutBuf_Inv2_NMOS_POGate_Comb_length'] = _Comp_SAOutBuf_Inv2_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_Comp_SAOutBuf_Inv2_PMOS_ChannelWidth'] = _Comp_SAOutBuf_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters1['_Comp_SAOutBuf_Inv2_PMOS_ChannelLength'] = _Comp_SAOutBuf_Inv2_PMOS_ChannelLength
        _Caculation_Parameters1['_Comp_SAOutBuf_Inv2_PMOS_NumberofGate'] = _Comp_SAOutBuf_Inv2_PMOS_NumberofGate
        _Caculation_Parameters1['_Comp_SAOutBuf_Inv2_PMOS_XVT'] = _Comp_SAOutBuf_Inv2_PMOS_XVT
        _Caculation_Parameters1['_Comp_SAOutBuf_Inv2_PMOS_POGate_Comb_length'] = _Comp_SAOutBuf_Inv2_PMOS_POGate_Comb_length

        ## SR Latch Sizing
        _Caculation_Parameters1['_Comp_SRLatch_NAND_NMOS_ChannelWidth'] = _Comp_SRLatch_NAND_NMOS_ChannelWidth
        _Caculation_Parameters1['_Comp_SRLatch_NAND_NMOS_ChannelLength'] = _Comp_SRLatch_NAND_NMOS_ChannelLength
        _Caculation_Parameters1['_Comp_SRLatch_NAND_NMOS_NumberofGate'] = _Comp_SRLatch_NAND_NMOS_NumberofGate
        _Caculation_Parameters1['_Comp_SRLatch_NAND_NMOS_XVT'] = _Comp_SRLatch_NAND_NMOS_XVT
        _Caculation_Parameters1['_Comp_SRLatch_NAND_NMOS_POGate_Comb_length'] = _Comp_SRLatch_NAND_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_Comp_SRLatch_NAND_PMOS_ChannelWidth'] = _Comp_SRLatch_NAND_PMOS_ChannelWidth
        _Caculation_Parameters1['_Comp_SRLatch_NAND_PMOS_ChannelLength'] = _Comp_SRLatch_NAND_PMOS_ChannelLength
        _Caculation_Parameters1['_Comp_SRLatch_NAND_PMOS_NumberofGate'] = _Comp_SRLatch_NAND_PMOS_NumberofGate
        _Caculation_Parameters1['_Comp_SRLatch_NAND_PMOS_XVT'] = _Comp_SRLatch_NAND_PMOS_XVT
        _Caculation_Parameters1['_Comp_SRLatch_NAND_PMOS_POGate_Comb_length'] = _Comp_SRLatch_NAND_PMOS_POGate_Comb_length

        # CLK Input Logic Gates
        _Caculation_Parameters1['_Comp_CLKSamp_Inv_NMOS_ChannelWidth'] = _Comp_CLKSamp_Inv_NMOS_ChannelWidth
        _Caculation_Parameters1['_Comp_CLKSamp_Inv_NMOS_ChannelLength'] = _Comp_CLKSamp_Inv_NMOS_ChannelLength
        _Caculation_Parameters1['_Comp_CLKSamp_Inv_NMOS_NumberofGate'] = _Comp_CLKSamp_Inv_NMOS_NumberofGate
        _Caculation_Parameters1['_Comp_CLKSamp_Inv_NMOS_XVT'] = _Comp_CLKSamp_Inv_NMOS_XVT
        _Caculation_Parameters1['_Comp_CLKSamp_Inv_NMOS_POGate_Comb_length'] = _Comp_CLKSamp_Inv_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_Comp_CLKSamp_Inv_PMOS_ChannelWidth'] = _Comp_CLKSamp_Inv_PMOS_ChannelWidth
        _Caculation_Parameters1['_Comp_CLKSamp_Inv_PMOS_ChannelLength'] = _Comp_CLKSamp_Inv_PMOS_ChannelLength
        _Caculation_Parameters1['_Comp_CLKSamp_Inv_PMOS_NumberofGate'] = _Comp_CLKSamp_Inv_PMOS_NumberofGate
        _Caculation_Parameters1['_Comp_CLKSamp_Inv_PMOS_XVT'] = _Comp_CLKSamp_Inv_PMOS_XVT
        _Caculation_Parameters1['_Comp_CLKSamp_Inv_PMOS_POGate_Comb_length'] = _Comp_CLKSamp_Inv_PMOS_POGate_Comb_length

        _Caculation_Parameters1['_Comp_CLKSrc_Inv_NMOS_ChannelWidth'] = _Comp_CLKSrc_Inv_NMOS_ChannelWidth
        _Caculation_Parameters1['_Comp_CLKSrc_Inv_NMOS_ChannelLength'] = _Comp_CLKSrc_Inv_NMOS_ChannelLength
        _Caculation_Parameters1['_Comp_CLKSrc_Inv_NMOS_NumberofGate'] = _Comp_CLKSrc_Inv_NMOS_NumberofGate
        _Caculation_Parameters1['_Comp_CLKSrc_Inv_NMOS_XVT'] = _Comp_CLKSrc_Inv_NMOS_XVT
        _Caculation_Parameters1['_Comp_CLKSrc_Inv_NMOS_POGate_Comb_length'] = _Comp_CLKSrc_Inv_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_Comp_CLKSrc_Inv_PMOS_ChannelWidth'] = _Comp_CLKSrc_Inv_PMOS_ChannelWidth
        _Caculation_Parameters1['_Comp_CLKSrc_Inv_PMOS_ChannelLength'] = _Comp_CLKSrc_Inv_PMOS_ChannelLength
        _Caculation_Parameters1['_Comp_CLKSrc_Inv_PMOS_NumberofGate'] = _Comp_CLKSrc_Inv_PMOS_NumberofGate
        _Caculation_Parameters1['_Comp_CLKSrc_Inv_PMOS_XVT'] = _Comp_CLKSrc_Inv_PMOS_XVT
        _Caculation_Parameters1['_Comp_CLKSrc_Inv_PMOS_POGate_Comb_length'] = _Comp_CLKSrc_Inv_PMOS_POGate_Comb_length

        ## CLKSrc & CLKSample AND Gate
        _Caculation_Parameters1['_Comp_AND_NAND_NMOS_ChannelWidth'] = _Comp_AND_NAND_NMOS_ChannelWidth
        _Caculation_Parameters1['_Comp_AND_NAND_NMOS_ChannelLength'] = _Comp_AND_NAND_NMOS_ChannelLength
        _Caculation_Parameters1['_Comp_AND_NAND_NMOS_NumberofGate'] = _Comp_AND_NAND_NMOS_NumberofGate
        _Caculation_Parameters1['_Comp_AND_NAND_NMOS_XVT'] = _Comp_AND_NAND_NMOS_XVT

        _Caculation_Parameters1['_Comp_AND_NAND_PMOS_ChannelWidth'] = _Comp_AND_NAND_PMOS_ChannelWidth
        _Caculation_Parameters1['_Comp_AND_NAND_PMOS_ChannelLength'] = _Comp_AND_NAND_PMOS_ChannelLength
        _Caculation_Parameters1['_Comp_AND_NAND_PMOS_NumberofGate'] = _Comp_AND_NAND_PMOS_NumberofGate
        _Caculation_Parameters1['_Comp_AND_NAND_PMOS_XVT'] = _Comp_AND_NAND_PMOS_XVT

        _Caculation_Parameters1['_Comp_AND_Inv_NMOS_ChannelWidth'] = _Comp_AND_Inv_NMOS_ChannelWidth
        _Caculation_Parameters1['_Comp_AND_Inv_NMOS_ChannelLength'] = _Comp_AND_Inv_NMOS_ChannelLength
        _Caculation_Parameters1['_Comp_AND_Inv_NMOS_NumberofGate'] = _Comp_AND_Inv_NMOS_NumberofGate
        _Caculation_Parameters1['_Comp_AND_Inv_NMOS_XVT'] = _Comp_AND_Inv_NMOS_XVT
        _Caculation_Parameters1['_Comp_AND_Inv_NMOS_POGate_Comb_length'] = _Comp_AND_Inv_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_Comp_AND_Inv_PMOS_ChannelWidth'] = _Comp_AND_Inv_PMOS_ChannelWidth
        _Caculation_Parameters1['_Comp_AND_Inv_PMOS_ChannelLength'] = _Comp_AND_Inv_PMOS_ChannelLength
        _Caculation_Parameters1['_Comp_AND_Inv_PMOS_NumberofGate'] = _Comp_AND_Inv_PMOS_NumberofGate
        _Caculation_Parameters1['_Comp_AND_Inv_PMOS_XVT'] = _Comp_AND_Inv_PMOS_XVT
        _Caculation_Parameters1['_Comp_AND_Inv_PMOS_POGate_Comb_length'] = _Comp_AND_Inv_PMOS_POGate_Comb_length

        ## CLK Buffer
        # Inverter1
        _Caculation_Parameters1['_Comp_CLKBuf_Inv1_NMOS_ChannelWidth'] = _Comp_CLKBuf_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters1['_Comp_CLKBuf_Inv1_NMOS_ChannelLength'] = _Comp_CLKBuf_Inv1_NMOS_ChannelLength
        _Caculation_Parameters1['_Comp_CLKBuf_Inv1_NMOS_NumberofGate'] = _Comp_CLKBuf_Inv1_NMOS_NumberofGate
        _Caculation_Parameters1['_Comp_CLKBuf_Inv1_NMOS_XVT'] = _Comp_CLKBuf_Inv1_NMOS_XVT
        _Caculation_Parameters1['_Comp_CLKBuf_Inv1_NMOS_POGate_Comb_length'] = _Comp_CLKBuf_Inv1_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_Comp_CLKBuf_Inv1_PMOS_ChannelWidth'] = _Comp_CLKBuf_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters1['_Comp_CLKBuf_Inv1_PMOS_ChannelLength'] = _Comp_CLKBuf_Inv1_PMOS_ChannelLength
        _Caculation_Parameters1['_Comp_CLKBuf_Inv1_PMOS_NumberofGate'] = _Comp_CLKBuf_Inv1_PMOS_NumberofGate
        _Caculation_Parameters1['_Comp_CLKBuf_Inv1_PMOS_XVT'] = _Comp_CLKBuf_Inv1_PMOS_XVT
        _Caculation_Parameters1['_Comp_CLKBuf_Inv1_PMOS_POGate_Comb_length'] = _Comp_CLKBuf_Inv1_PMOS_POGate_Comb_length

        # Inverter2
        _Caculation_Parameters1['_Comp_CLKBuf_Inv2_NMOS_ChannelWidth'] = _Comp_CLKBuf_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters1['_Comp_CLKBuf_Inv2_NMOS_ChannelLength'] = _Comp_CLKBuf_Inv2_NMOS_ChannelLength
        _Caculation_Parameters1['_Comp_CLKBuf_Inv2_NMOS_NumberofGate'] = _Comp_CLKBuf_Inv2_NMOS_NumberofGate
        _Caculation_Parameters1['_Comp_CLKBuf_Inv2_NMOS_XVT'] = _Comp_CLKBuf_Inv2_NMOS_XVT
        _Caculation_Parameters1['_Comp_CLKBuf_Inv2_NMOS_POGate_Comb_length'] = _Comp_CLKBuf_Inv2_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_Comp_CLKBuf_Inv2_PMOS_ChannelWidth'] = _Comp_CLKBuf_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters1['_Comp_CLKBuf_Inv2_PMOS_ChannelLength'] = _Comp_CLKBuf_Inv2_PMOS_ChannelLength
        _Caculation_Parameters1['_Comp_CLKBuf_Inv2_PMOS_NumberofGate'] = _Comp_CLKBuf_Inv2_PMOS_NumberofGate
        _Caculation_Parameters1['_Comp_CLKBuf_Inv2_PMOS_XVT'] = _Comp_CLKBuf_Inv2_PMOS_XVT
        _Caculation_Parameters1['_Comp_CLKBuf_Inv2_PMOS_POGate_Comb_length'] = _Comp_CLKBuf_Inv2_PMOS_POGate_Comb_length

        # PowerRail Placement
        _Caculation_Parameters1['_Comp_BufSR_NMOS_Pbody_NumCont'] = _Comp_BufSR_NMOS_Pbody_NumCont
        _Caculation_Parameters1['_Comp_BufSR_NMOS_Pbody_XvtTop2Pbody'] = _Comp_BufSR_NMOS_Pbody_XvtTop2Pbody
        _Caculation_Parameters1['_Comp_BufSR_PMOS_Nbody_NumCont'] = _Comp_BufSR_PMOS_Nbody_NumCont
        _Caculation_Parameters1['_Comp_BufSR_PMOS_Nbody_Xvtdown2Nbody'] = _Comp_BufSR_PMOS_Nbody_Xvtdown2Nbody
        _Caculation_Parameters1['_Comp_BufSR_PMOSXvt2NMOSXvt'] = _Comp_BufSR_PMOSXvt2NMOSXvt

        _Caculation_Parameters1['_Comp_CLKInLogic_NMOS_Pbody_Xvtdown2Pbody'] = _Comp_CLKInLogic_NMOS_Pbody_Xvtdown2Pbody
        _Caculation_Parameters1['_Comp_CLKInLogic_PMOS_Nbody_NumCont'] = _Comp_CLKInLogic_PMOS_Nbody_NumCont
        _Caculation_Parameters1['_Comp_CLKInLogic_PMOS_Nbody_Xvtdown2Nbody'] = _Comp_CLKInLogic_PMOS_Nbody_Xvtdown2Nbody
        _Caculation_Parameters1['_Comp_CLKInLogic_PMOSXvt2NMOSXvt'] = _Comp_CLKInLogic_PMOSXvt2NMOSXvt

        _Caculation_Parameters1['_Buf_CLKSamp_Pbody_NumCont'] = _Buf_CLKSamp_Pbody_NumCont
        _Caculation_Parameters1['_Buf_CLKSamp_Nbody_NumCont'] = _Buf_CLKSamp_Nbody_NumCont
        _Caculation_Parameters1['_Buf_CLKSamp_PMOSXvt2NMOSXvt'] = _Buf_CLKSamp_PMOSXvt2NMOSXvt
        _Caculation_Parameters1['_Buf_CLKSamp_XvtTop2Pbody'] = _Buf_CLKSamp_XvtTop2Pbody
        _Caculation_Parameters1['_Buf_CLKSamp_Xvtdown2Nbody'] = _Buf_CLKSamp_Xvtdown2Nbody

        _Caculation_Parameters1['_Buf_CLKSamp_NumberofGate'] = _Buf_CLKSamp_NumberofGate
        _Caculation_Parameters1['_Buf_CLKSamp_ChannelLength'] = _Buf_CLKSamp_ChannelLength
        _Caculation_Parameters1['_Buf_CLKSamp_XVT'] = _Buf_CLKSamp_XVT

        _Caculation_Parameters1['_Buf_CLKSamp_Inv_NMOS_ChannelWidth'] = _Buf_CLKSamp_Inv_NMOS_ChannelWidth
        _Caculation_Parameters1['_Buf_CLKSamp_Inv_NMOS_POGate_Comb_length'] = _Buf_CLKSamp_Inv_NMOS_POGate_Comb_length
        _Caculation_Parameters1['_Buf_CLKSamp_Inv_PMOS_ChannelWidth'] = _Buf_CLKSamp_Inv_PMOS_ChannelWidth
        _Caculation_Parameters1['_Buf_CLKSamp_Inv_PMOS_POGate_Comb_length'] = _Buf_CLKSamp_Inv_PMOS_POGate_Comb_length

        _Caculation_Parameters1['_Buf_CLKSrc_Pbody_NumCont'] = _Buf_CLKSrc_Pbody_NumCont
        _Caculation_Parameters1['_Buf_CLKSrc_Nbody_NumCont'] = _Buf_CLKSrc_Nbody_NumCont
        _Caculation_Parameters1['_Buf_CLKSrc_PMOSXvt2NMOSXvt'] = _Buf_CLKSrc_PMOSXvt2NMOSXvt
        _Caculation_Parameters1['_Buf_CLKSrc_XvtTop2Pbody'] = _Buf_CLKSrc_XvtTop2Pbody
        _Caculation_Parameters1['_Buf_CLKSrc_Xvtdown2Nbody'] = _Buf_CLKSrc_Xvtdown2Nbody

        _Caculation_Parameters1['_Buf_CLKSrc_NumberofGate'] = _Buf_CLKSrc_NumberofGate
        _Caculation_Parameters1['_Buf_CLKSrc_ChannelLength'] = _Buf_CLKSrc_ChannelLength
        _Caculation_Parameters1['_Buf_CLKSrc_XVT'] = _Buf_CLKSrc_XVT

        _Caculation_Parameters1['_Buf_CLKSrc_Inv_NMOS_ChannelWidth'] = _Buf_CLKSrc_Inv_NMOS_ChannelWidth
        _Caculation_Parameters1['_Buf_CLKSrc_Inv_NMOS_POGate_Comb_length'] = _Buf_CLKSrc_Inv_NMOS_POGate_Comb_length
        _Caculation_Parameters1['_Buf_CLKSrc_Inv_PMOS_ChannelWidth'] = _Buf_CLKSrc_Inv_PMOS_ChannelWidth
        _Caculation_Parameters1['_Buf_CLKSrc_Inv_PMOS_POGate_Comb_length'] = _Buf_CLKSrc_Inv_PMOS_POGate_Comb_length

        _Caculation_Parameters1['_Buf_CompOut_Pbody_NumCont'] = _Buf_CompOut_Pbody_NumCont
        _Caculation_Parameters1['_Buf_CompOut_Nbody_NumCont'] = _Buf_CompOut_Nbody_NumCont
        _Caculation_Parameters1['_Buf_CompOut_PMOSXvt2NMOSXvt'] = _Buf_CompOut_PMOSXvt2NMOSXvt
        _Caculation_Parameters1['_Buf_CompOut_XvtTop2Pbody'] = _Buf_CompOut_XvtTop2Pbody
        _Caculation_Parameters1['_Buf_CompOut_Xvtdown2Nbody'] = _Buf_CompOut_Xvtdown2Nbody

        _Caculation_Parameters1['_Buf_CompOut_NumberofGate'] = _Buf_CompOut_NumberofGate
        _Caculation_Parameters1['_Buf_CompOut_ChannelLength'] = _Buf_CompOut_ChannelLength
        _Caculation_Parameters1['_Buf_CompOut_XVT'] = _Buf_CompOut_XVT

        _Caculation_Parameters1['_Buf_CompOut_Inv_NMOS_ChannelWidth'] = _Buf_CompOut_Inv_NMOS_ChannelWidth
        _Caculation_Parameters1['_Buf_CompOut_Inv_NMOS_POGate_Comb_length'] = _Buf_CompOut_Inv_NMOS_POGate_Comb_length
        _Caculation_Parameters1['_Buf_CompOut_Inv_PMOS_ChannelWidth'] = _Buf_CompOut_Inv_PMOS_ChannelWidth
        _Caculation_Parameters1['_Buf_CompOut_Inv_PMOS_POGate_Comb_length'] = _Buf_CompOut_Inv_PMOS_POGate_Comb_length

        self._DesignParameter['SRF_SARLogicWtComparator'] = self._SrefElementDeclaration(
            _DesignObj=L00_SARLogicWtComparator_KJH._SARLogicWtComparator(_DesignParameter=None,
                                                                          _Name='{}:SRF_SARLogicWtComparator'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_SARLogicWtComparator']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SARLogicWtComparator']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SARLogicWtComparator']['_DesignObj']._CalculateDesignParameter(
            **_Caculation_Parameters1)

        ## initialize Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SARLogicWtComparator']['_XYCoordinates'] = [[0, 0]]

        ## Pre-Calculated centY coord
        # tmp = self.get_param_KJH4('SRF_SARLogicWtComparator','SRF_SARLogicWtBuffers','SRF_SARLogicWtCLKTree','SRF_SARLogic','BND_Nbody_M1Exten')
        # centY = tmp[0][0][0][0][0][0]['_XY_cent'][1]
        tmp1 = self.get_param_KJH4('SRF_SARLogicWtComparator', 'SRF_SARLogicWtBuffers', 'SRF_UpperCDACPreDriver', 'BND_Nbody_M1Exten')
        tmp1_2 = self.get_param_KJH4('SRF_SARLogicWtComparator', 'SRF_SARLogicWtBuffers', 'SRF_LowerCDACPreDriver', 'BND_Pbody_M1Exten')
        centY = int((tmp1[0][0][0][0][0]['_XY_cent'][1] + tmp1_2[0][0][0][0][0]['_XY_cent'][1]) / 2)

        print('###############################################')
        print('##              CDAC (Positive)              ##')
        print('##            Calculation_Start!!            ##')
        print('###############################################')

        ## CDAC (SREF) Generation
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters0 = copy.deepcopy(H02_01_CDACWtDriver_Unfolded._CDACWtDriver_Unfolded._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters0['_NumOfBits'] = _NumofBit
        _Caculation_Parameters0['_CDAC_LayoutOption'] = _CDAC_LayoutOption
        _Caculation_Parameters0['_CDAC_ShieldingLayer'] = _CDAC_ShieldingLayer
        _Caculation_Parameters0['_CDAC_BotNodeVtcExtensionMetalLayer'] = 2
        _Caculation_Parameters0['_CDAC_MetalWidth'] = _CDAC_MetalWidth
        _Caculation_Parameters0['_CDAC_MetalLength'] = _CDAC_MetalLength
        _Caculation_Parameters0['_CDAC_MetalSpacing'] = _CDAC_MetalSpacing
        _Caculation_Parameters0['_CDAC_NumOfElement'] = _CDAC_NumOfElement
        _Caculation_Parameters0['_CDAC_ConnectLength'] = _CDAC_ConnectLength
        _Caculation_Parameters0['_CDAC_ExtendLength'] = _CDAC_ExtendLength
        _Caculation_Parameters0['_CDAC_CapArrayWDrivingNodeDistance'] = _CDAC_CapArrayWDrivingNodeDistance
        _Caculation_Parameters0['_CDAC_DriveNodeDistance'] = _CDAC_DriveNodeDistance
        _Caculation_Parameters0['_CDAC_YWidth_Bottom_Hrz'] = _CDAC_YWidth_Bottom_Hrz
        _Caculation_Parameters0['_CDAC_DummyCap_TopBottomShort'] = _CDAC_DummyCap_TopBottomShort
        _Caculation_Parameters0['_CDAC_NumOfDummyCaps'] = _CDAC_NumOfDummyCaps
        _Caculation_Parameters0['_Driver_SizeByBit'] = _Driver_SizeByBit
        _Caculation_Parameters0['_Driver_NMOS_NumberofGate'] = _Driver_NMOS_NumberofGate
        _Caculation_Parameters0['_Driver_NMOS_ChannelWidth'] = _Driver_NMOS_ChannelWidth
        _Caculation_Parameters0['_Driver_NMOS_Channellength'] = _Driver_NMOS_Channellength
        _Caculation_Parameters0['_Driver_NMOS_XVT'] = _Driver_NMOS_XVT
        _Caculation_Parameters0['_Driver_PMOS_NumberofGate'] = _Driver_PMOS_NumberofGate
        _Caculation_Parameters0['_Driver_PMOS_ChannelWidth'] = _Driver_PMOS_ChannelWidth
        _Caculation_Parameters0['_Driver_PMOS_Channellength'] = _Driver_PMOS_Channellength
        _Caculation_Parameters0['_Driver_PMOS_XVT'] = _Driver_PMOS_XVT

        ## CDAC (Positive)
        if _CDAC_Folding == True:
            if _Driver_CommonCentroidPlacementIfCDACFolded == True:
                self._DesignParameter['SRF_CDAC_Pos'] = self._SrefElementDeclaration(
                    _DesignObj=H02_01_CDACWtDriver_Fold1_CC._CDACWtDriverFold1(_DesignParameter=None,
                                                                               _Name='{}:SRF_CDAC_Pos'.format(_Name)))[0]
            else:
                self._DesignParameter['SRF_CDAC_Pos'] = self._SrefElementDeclaration(
                    _DesignObj=H02_01_CDACWtDriver_Fold1_DrvArranged._CDACWtDriverFold1(_DesignParameter=None,
                                                                                        _Name='{}:SRF_CDAC_Pos'.format(_Name)))[0]
        else:
            self._DesignParameter['SRF_CDAC_Pos'] = self._SrefElementDeclaration(
                _DesignObj=H02_01_CDACWtDriver_Unfolded._CDACWtDriver_Unfolded(_DesignParameter=None,
                                                                               _Name='{}:SRF_CDAC_Pos'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_CDAC_Pos']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CDAC_Pos']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CDAC_Pos']['_DesignObj']._CalculateDesignParameter(
            **_Caculation_Parameters0)

        ## initialize Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CDAC_Pos']['_XYCoordinates'] = [[0, 0]]
        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        ## Define Boundary_element _XWidth
        self._DesignParameter['SRF_SARLogicWtComparator']['_DesignObj']._DesignParameter['SRF_Comparator']['_DesignObj']._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_SARLogicWtComparator']['_DesignObj']._DesignParameter['SRF_Comparator']['_DesignObj']._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_Angle'] = 0
        tmp1x = self.get_param_KJH3('SRF_SARLogicWtComparator', 'SRF_Comparator', 'SRF_Slicer', '_Guardring', '_Met1Layerx')
        tmp1y = self.get_param_KJH4('SRF_SARLogicWtComparator', 'SRF_Buf_CLKSamp', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        target_coord = [tmp1x[0][0][0][0][0][0]['_XY_left'][0], tmp1y[0][0][0][0][0][0]['_XY_down'][1]]
        ## Approaching_coord: _XY_type2
        if _CDAC_Folding == True:
            if _Driver_CommonCentroidPlacementIfCDACFolded == True:
                tmp2x = self.get_param_KJH4('SRF_CDAC_Pos', 'BND_CDACFold1_B{}_DrvInput_Vtc_M2'.format(_NumofBit - 1))
            else:
                tmp2x = self.get_param_KJH4('SRF_CDAC_Pos', 'BND_CDACFold1_B{}_DrvOutput_Vtc_M2'.format(_NumofBit - 1))
            # tmp2y = self.get_param_KJH4('SRF_CDAC_Pos', 'SRF_CDAC_LowerHalf', 'SRF_DriverArray', 'BND_{}C_Driver_Input_Hrz_M3'.format(1))
            tmp2y_1 = self.get_param_KJH4('SRF_CDAC_Pos', 'BND_CDACFold1_{}B{}_DrvInput_Hrz_M3'.format('Lo', 0))
            # approaching_coord = [tmp2x[0][0][0]['_XY_left'][0], tmp2y[0][0][0][0][0]['_XY_down'][1]]
            approaching_coord = [tmp2x[0][0][0]['_XY_left'][0], tmp2y_1[0][0][0]['_XY_down'][1]]
        else:
            tmp2x = self.get_param_KJH4('SRF_CDAC_Pos', 'BND_CDACTopNode_Hrz_M7')
            tmp2y = self.get_param_KJH4('SRF_CDAC_Pos', 'SRF_CDACWtDriver', 'SRF_DriverArray', 'BND_{}C_Driver_Input_Hrz_M3'.format(1))
            approaching_coord = [tmp2x[0][0][0]['_XY_left'][0], tmp2y[0][0][0][0][0]['_XY_down'][1]]
            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CDAC_Pos')
        Scoord = tmp3[0][0]['_XY_origin']
        XOffset = 2000
        YOffset = 100
        Scoord[0] = Scoord[0] + XOffset
        Scoord[1] = Scoord[1] + YOffset
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['SRF_CDAC_Pos']['_XYCoordinates'] = tmpXY

        print('###############################################')
        print('##              CDAC (Negative)              ##')
        print('##            Calculation_Start!!            ##')
        print('###############################################')

        ## CDAC (Negative)
        if _CDAC_Folding == True:
            if _Driver_CommonCentroidPlacementIfCDACFolded == True:
                self._DesignParameter['SRF_CDAC_Neg'] = self._SrefElementDeclaration(
                    _DesignObj=H02_01_CDACWtDriver_Fold1_CC._CDACWtDriverFold1(_DesignParameter=None,
                                                                               _Name='{}:SRF_CDAC_Neg'.format(_Name)))[0]
            else:
                self._DesignParameter['SRF_CDAC_Neg'] = self._SrefElementDeclaration(
                    _DesignObj=H02_01_CDACWtDriver_Fold1_DrvArranged._CDACWtDriverFold1(_DesignParameter=None,
                                                                                        _Name='{}:SRF_CDAC_Neg'.format(
                                                                                            _Name)))[0]
        else:
            self._DesignParameter['SRF_CDAC_Neg'] = self._SrefElementDeclaration(
                _DesignObj=H02_01_CDACWtDriver_Unfolded._CDACWtDriver_Unfolded(_DesignParameter=None,
                                                                               _Name='{}:SRF_CDAC_Neg'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_CDAC_Neg']['_Reflect'] = [1, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CDAC_Neg']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CDAC_Neg']['_DesignObj']._CalculateDesignParameter(
            **_Caculation_Parameters0)

        ## initialize Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CDAC_Neg']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1x = self.get_param_KJH3('SRF_SARLogicWtComparator', 'SRF_Comparator', 'SRF_Slicer', '_Guardring', '_Met1Layerx')
        tmp1y = self.get_param_KJH4('SRF_SARLogicWtComparator', 'SRF_Buf_CompOut', 'SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        target_coord = [tmp1x[0][0][0][0][0][0]['_XY_left'][0], tmp1y[0][0][0][0][0][0]['_XY_up'][1]]
        ## Approaching_coord: _XY_type2
        if _CDAC_Folding == True:
            if _Driver_CommonCentroidPlacementIfCDACFolded == True:
                tmp2x = self.get_param_KJH4('SRF_CDAC_Neg', 'BND_CDACFold1_B{}_DrvInput_Vtc_M2'.format(_NumofBit - 1))
            else:
                tmp2x = self.get_param_KJH4('SRF_CDAC_Neg', 'BND_CDACFold1_B{}_DrvOutput_Vtc_M2'.format(_NumofBit - 1))
            # tmp2y = self.get_param_KJH4('SRF_CDAC_Neg', 'SRF_CDAC_LowerHalf','SRF_DriverArray', 'BND_{}C_Driver_Input_Hrz_M3'.format(1))
            tmp2y_1 = self.get_param_KJH4('SRF_CDAC_Neg', 'BND_CDACFold1_{}B{}_DrvInput_Hrz_M3'.format('Lo', 0))
            # approaching_coord = [tmp2x[0][0][0]['_XY_left'][0], tmp2y[0][0][0][0][0]['_XY_down'][1]]
            approaching_coord = [tmp2x[0][0][0]['_XY_left'][0], tmp2y_1[0][0][0]['_XY_down'][1]]
        else:
            tmp2x = self.get_param_KJH4('SRF_CDAC_Neg', 'BND_CDACTopNode_Hrz_M7')
            tmp2y = self.get_param_KJH4('SRF_CDAC_Neg', 'SRF_CDACWtDriver', 'SRF_DriverArray', 'BND_{}C_Driver_Input_Hrz_M3'.format(1))
            approaching_coord = [tmp2x[0][0][0]['_XY_left'][0], tmp2y[0][0][0][0][0]['_XY_down'][1]]
            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CDAC_Neg')
        Scoord = tmp3[0][0]['_XY_origin']
        XOffset = 2000
        YOffset = -100
        Scoord[0] = Scoord[0] + XOffset
        Scoord[1] = Scoord[1] + YOffset
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['SRF_CDAC_Neg']['_XYCoordinates'] = tmpXY

        print('###############################################')
        print('##     Bootstrapped Switch (Positive)        ##')
        print('##            Calculation_Start!!            ##')
        print('###############################################')

        ############ BootSW Generation
        ## Bootstrap Sampler SREF Generation
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C13_01_CtopCbotRouted_YJ_v01_00._CtopCbotRouted._ParametersForDesignCalculation)
        _Caculation_Parameters['_Tr1Tr2_Tr1_NMOSNumberofGate'] = _Samp_Tr1Tr2_Tr1_NMOSNumberofGate
        _Caculation_Parameters['_Tr1Tr2_Tr1_NMOSChannelWidth'] = _Samp_Tr1Tr2_Tr1_NMOSChannelWidth
        _Caculation_Parameters['_Tr1Tr2_Tr1_NMOSChannellength'] = _Samp_Tr1Tr2_Tr1_NMOSChannellength
        _Caculation_Parameters['_Tr1Tr2_Tr1_GateSpacing'] = _Samp_Tr1Tr2_Tr1_GateSpacing
        _Caculation_Parameters['_Tr1Tr2_Tr1_SDWidth'] = _Samp_Tr1Tr2_Tr1_SDWidth
        _Caculation_Parameters['_Tr1Tr2_Tr1_XVT'] = _Samp_Tr1Tr2_Tr1_XVT
        _Caculation_Parameters['_Tr1Tr2_Tr1_PCCrit'] = _Samp_Tr1Tr2_Tr1_PCCrit
        _Caculation_Parameters['_Tr1Tr2_Tr1_Source_Via_TF'] = _Samp_Tr1Tr2_Tr1_Source_Via_TF
        _Caculation_Parameters['_Tr1Tr2_Tr1_Drain_Via_TF'] = _Samp_Tr1Tr2_Tr1_Drain_Via_TF
        _Caculation_Parameters['_Tr1Tr2_Tr1_NMOSDummy'] = _Samp_Tr1Tr2_Tr1_NMOSDummy
        _Caculation_Parameters['_Tr1Tr2_Tr1_NMOSDummy_length'] = _Samp_Tr1Tr2_Tr1_NMOSDummy_length

        _Caculation_Parameters['_Tr1Tr2_Tr2_NMOSNumberofGate'] = _Samp_Tr1Tr2_Tr2_NMOSNumberofGate
        _Caculation_Parameters['_Tr1Tr2_Tr2_NMOSChannelWidth'] = _Samp_Tr1Tr2_Tr2_NMOSChannelWidth
        _Caculation_Parameters['_Tr1Tr2_Tr2_NMOSChannellength'] = _Samp_Tr1Tr2_Tr2_NMOSChannellength
        _Caculation_Parameters['_Tr1Tr2_Tr2_GateSpacing'] = _Samp_Tr1Tr2_Tr2_GateSpacing
        _Caculation_Parameters['_Tr1Tr2_Tr2_SDWidth'] = _Samp_Tr1Tr2_Tr2_SDWidth
        _Caculation_Parameters['_Tr1Tr2_Tr2_XVT'] = _Samp_Tr1Tr2_Tr2_XVT
        _Caculation_Parameters['_Tr1Tr2_Tr2_PCCrit'] = _Samp_Tr1Tr2_Tr2_PCCrit
        _Caculation_Parameters['_Tr1Tr2_Tr2_Source_Via_TF'] = _Samp_Tr1Tr2_Tr2_Source_Via_TF
        _Caculation_Parameters['_Tr1Tr2_Tr2_Drain_Via_TF'] = _Samp_Tr1Tr2_Tr2_Drain_Via_TF
        _Caculation_Parameters['_Tr1Tr2_Tr2_NMOSDummy'] = _Samp_Tr1Tr2_Tr2_NMOSDummy
        _Caculation_Parameters['_Tr1Tr2_Tr2_NMOSDummy_length'] = _Samp_Tr1Tr2_Tr2_NMOSDummy_length
        _Caculation_Parameters['_Tr1Tr2_Tr2_NMOSDummy_placement'] = _Samp_Tr1Tr2_Tr2_NMOSDummy_placement
        _Caculation_Parameters['_Tr1Tr2_Inputnode_Metal_layer'] = _Samp_Tr1Tr2_Inputnode_Metal_layer
        _Caculation_Parameters['_Tr1Tr2_Inputnode_width'] = _Samp_Tr1Tr2_Inputnode_width
        _Caculation_Parameters['_Tr1Tr2_Outputnode_Metal_layer'] = _Samp_Tr1Tr2_Outputnode_Metal_layer
        _Caculation_Parameters['_Tr1Tr2_Outputnode_width'] = _Samp_Tr1Tr2_Outputnode_width
        _Caculation_Parameters['_Tr1Tr2_NwellWidth'] = _Samp_Tr1Tr2_NwellWidth

        _Caculation_Parameters['_Tr4_NMOSNumberofGate'] = _Samp_Tr4_NMOSNumberofGate
        _Caculation_Parameters['_Tr4_NMOSChannelWidth'] = _Samp_Tr4_NMOSChannelWidth
        _Caculation_Parameters['_Tr4_NMOSChannellength'] = _Samp_Tr4_NMOSChannellength
        _Caculation_Parameters['_Tr4_GateSpacing'] = _Samp_Tr4_GateSpacing
        _Caculation_Parameters['_Tr4_SDWidth'] = _Samp_Tr4_SDWidth
        _Caculation_Parameters['_Tr4_XVT'] = _Samp_Tr4_XVT
        _Caculation_Parameters['_Tr4_PCCrit'] = _Samp_Tr4_PCCrit
        _Caculation_Parameters['_Tr4_Source_Via_TF'] = _Samp_Tr4_Source_Via_TF
        _Caculation_Parameters['_Tr4_Drain_Via_TF'] = _Samp_Tr4_Drain_Via_TF
        _Caculation_Parameters['_Tr4_NMOSDummy'] = _Samp_Tr4_NMOSDummy
        _Caculation_Parameters['_Tr4_NMOSDummy_length'] = _Samp_Tr4_NMOSDummy_length
        _Caculation_Parameters['_Tr4_NMOSDummy_placement'] = _Samp_Tr4_NMOSDummy_placement

        _Caculation_Parameters['_Tr5_PMOSNumberofGate'] = _Samp_Tr5_PMOSNumberofGate
        _Caculation_Parameters['_Tr5_PMOSChannelWidth'] = _Samp_Tr5_PMOSChannelWidth
        _Caculation_Parameters['_Tr5_PMOSChannellength'] = _Samp_Tr5_PMOSChannellength
        _Caculation_Parameters['_Tr5_GateSpacing'] = _Samp_Tr5_GateSpacing
        _Caculation_Parameters['_Tr5_SDWidth'] = _Samp_Tr5_SDWidth
        _Caculation_Parameters['_Tr5_XVT'] = _Samp_Tr5_XVT
        _Caculation_Parameters['_Tr5_PCCrit'] = _Samp_Tr5_PCCrit
        _Caculation_Parameters['_Tr5_Source_Via_TF'] = _Samp_Tr5_Source_Via_TF
        _Caculation_Parameters['_Tr5_Drain_Via_TF'] = _Samp_Tr5_Drain_Via_TF
        _Caculation_Parameters['_Tr5_PMOSDummy'] = _Samp_Tr5_PMOSDummy
        _Caculation_Parameters['_Tr5_PMOSDummy_length'] = _Samp_Tr5_PMOSDummy_length
        _Caculation_Parameters['_Tr5_PMOSDummy_placement'] = _Samp_Tr5_PMOSDummy_placement

        _Caculation_Parameters['_Tr7_PMOSNumberofGate'] = _Samp_Tr7_PMOSNumberofGate
        _Caculation_Parameters['_Tr7_PMOSChannelWidth'] = _Samp_Tr7_PMOSChannelWidth
        _Caculation_Parameters['_Tr7_PMOSChannellength'] = _Samp_Tr7_PMOSChannellength
        _Caculation_Parameters['_Tr7_GateSpacing'] = _Samp_Tr7_GateSpacing
        _Caculation_Parameters['_Tr7_SDWidth'] = _Samp_Tr7_SDWidth
        _Caculation_Parameters['_Tr7_XVT'] = _Samp_Tr7_XVT
        _Caculation_Parameters['_Tr7_PCCrit'] = _Samp_Tr7_PCCrit
        _Caculation_Parameters['_Tr7_Source_Via_TF'] = _Samp_Tr7_Source_Via_TF
        _Caculation_Parameters['_Tr7_Drain_Via_TF'] = _Samp_Tr7_Drain_Via_TF
        _Caculation_Parameters['_Tr7_PMOSDummy'] = _Samp_Tr7_PMOSDummy
        _Caculation_Parameters['_Tr7_PMOSDummy_length'] = _Samp_Tr7_PMOSDummy_length
        _Caculation_Parameters['_Tr7_PMOSDummy_placement'] = _Samp_Tr7_PMOSDummy_placement

        _Caculation_Parameters['_Tr9_PMOSNumberofGate'] = _Samp_Tr9_PMOSNumberofGate
        _Caculation_Parameters['_Tr9_PMOSChannelWidth'] = _Samp_Tr9_PMOSChannelWidth
        _Caculation_Parameters['_Tr9_PMOSChannellength'] = _Samp_Tr9_PMOSChannellength
        _Caculation_Parameters['_Tr9_GateSpacing'] = _Samp_Tr9_GateSpacing
        _Caculation_Parameters['_Tr9_SDWidth'] = _Samp_Tr9_SDWidth
        _Caculation_Parameters['_Tr9_XVT'] = _Samp_Tr9_XVT
        _Caculation_Parameters['_Tr9_PCCrit'] = _Samp_Tr9_PCCrit
        _Caculation_Parameters['_Tr9_Source_Via_TF'] = _Samp_Tr9_Source_Via_TF
        _Caculation_Parameters['_Tr9_Drain_Via_TF'] = _Samp_Tr9_Drain_Via_TF
        _Caculation_Parameters['_Tr9_PMOSDummy'] = _Samp_Tr9_PMOSDummy
        _Caculation_Parameters['_Tr9_PMOSDummy_length'] = _Samp_Tr9_PMOSDummy_length
        _Caculation_Parameters['_Tr9_PMOSDummy_placement'] = _Samp_Tr9_PMOSDummy_placement

        _Caculation_Parameters['_Tr8_NMOSNumberofGate'] = _Samp_Tr8_NMOSNumberofGate
        _Caculation_Parameters['_Tr8_NMOSChannelWidth'] = _Samp_Tr8_NMOSChannelWidth
        _Caculation_Parameters['_Tr8_NMOSChannellength'] = _Samp_Tr8_NMOSChannellength
        _Caculation_Parameters['_Tr8_GateSpacing'] = _Samp_Tr8_GateSpacing
        _Caculation_Parameters['_Tr8_SDWidth'] = _Samp_Tr8_SDWidth
        _Caculation_Parameters['_Tr8_XVT'] = _Samp_Tr8_XVT
        _Caculation_Parameters['_Tr8_PCCrit'] = _Samp_Tr8_PCCrit
        _Caculation_Parameters['_Tr8_Source_Via_TF'] = _Samp_Tr8_Source_Via_TF
        _Caculation_Parameters['_Tr8_Drain_Via_TF'] = _Samp_Tr8_Drain_Via_TF
        _Caculation_Parameters['_Tr8_NMOSDummy'] = _Samp_Tr8_NMOSDummy
        _Caculation_Parameters['_Tr8_NMOSDummy_length'] = _Samp_Tr8_NMOSDummy_length
        _Caculation_Parameters['_Tr8_NMOSDummy_placement'] = _Samp_Tr8_NMOSDummy_placement

        _Caculation_Parameters['_Tr6_NMOSNumberofGate'] = _Samp_Tr6_NMOSNumberofGate
        _Caculation_Parameters['_Tr6_NMOSChannelWidth'] = _Samp_Tr6_NMOSChannelWidth
        _Caculation_Parameters['_Tr6_NMOSChannellength'] = _Samp_Tr6_NMOSChannellength
        _Caculation_Parameters['_Tr6_GateSpacing'] = _Samp_Tr6_GateSpacing
        _Caculation_Parameters['_Tr6_SDWidth'] = _Samp_Tr6_SDWidth
        _Caculation_Parameters['_Tr6_XVT'] = _Samp_Tr6_XVT
        _Caculation_Parameters['_Tr6_PCCrit'] = _Samp_Tr6_PCCrit
        _Caculation_Parameters['_Tr6_Source_Via_TF'] = _Samp_Tr6_Source_Via_TF
        _Caculation_Parameters['_Tr6_Drain_Via_TF'] = _Samp_Tr6_Drain_Via_TF
        _Caculation_Parameters['_Tr6_NMOSDummy'] = _Samp_Tr6_NMOSDummy
        _Caculation_Parameters['_Tr6_NMOSDummy_length'] = _Samp_Tr6_NMOSDummy_length
        _Caculation_Parameters['_Tr6_NMOSDummy_placement'] = _Samp_Tr6_NMOSDummy_placement
        _Caculation_Parameters['_Tr6_Vp_node_width'] = _Samp_Tr6_Vp_node_width
        _Caculation_Parameters['_Tr6_Vp_node_metal_Layer'] = _Samp_Tr6_Vp_node_metal_Layer
        _Caculation_Parameters['_Tr6_NwellWidth'] = _Samp_Tr6_NwellWidth

        _Caculation_Parameters['_Tr11_PMOSNumberofGate'] = _Samp_Tr11_PMOSNumberofGate
        _Caculation_Parameters['_Tr11_PMOSChannelWidth'] = _Samp_Tr11_PMOSChannelWidth
        _Caculation_Parameters['_Tr11_PMOSChannellength'] = _Samp_Tr11_PMOSChannellength
        _Caculation_Parameters['_Tr11_GateSpacing'] = _Samp_Tr11_GateSpacing
        _Caculation_Parameters['_Tr11_SDWidth'] = _Samp_Tr11_SDWidth
        _Caculation_Parameters['_Tr11_XVT'] = _Samp_Tr11_XVT
        _Caculation_Parameters['_Tr11_PCCrit'] = _Samp_Tr11_PCCrit
        _Caculation_Parameters['_Tr11_Source_Via_TF'] = _Samp_Tr11_Source_Via_TF
        _Caculation_Parameters['_Tr11_Drain_Via_TF'] = _Samp_Tr11_Drain_Via_TF
        _Caculation_Parameters['_Tr11_PMOSDummy'] = _Samp_Tr11_PMOSDummy
        _Caculation_Parameters['_Tr11_PMOSDummy_length'] = _Samp_Tr11_PMOSDummy_length
        _Caculation_Parameters['_Tr11_PMOSDummy_placement'] = _Samp_Tr11_PMOSDummy_placement
        _Caculation_Parameters['_Tr11_Guardring_NumCont'] = _Samp_Tr11_Guardring_NumCont

        _Caculation_Parameters['_Tie4N_NMOSNumberofGate'] = _Samp_Tie4N_NMOSNumberofGate
        _Caculation_Parameters['_Tie4N_NMOSChannelWidth'] = _Samp_Tie4N_NMOSChannelWidth
        _Caculation_Parameters['_Tie4N_NMOSChannellength'] = _Samp_Tie4N_NMOSChannellength
        _Caculation_Parameters['_Tie4N_GateSpacing'] = _Samp_Tie4N_GateSpacing
        _Caculation_Parameters['_Tie4N_SDWidth'] = _Samp_Tie4N_SDWidth
        _Caculation_Parameters['_Tie4N_XVT'] = _Samp_Tie4N_XVT
        _Caculation_Parameters['_Tie4N_PCCrit'] = _Samp_Tie4N_PCCrit
        _Caculation_Parameters['_Tie4N_Source_Via_TF'] = _Samp_Tie4N_Source_Via_TF
        _Caculation_Parameters['_Tie4N_Drain_Via_TF'] = _Samp_Tie4N_Drain_Via_TF
        _Caculation_Parameters['_Tie4N_NMOSDummy'] = _Samp_Tie4N_NMOSDummy
        _Caculation_Parameters['_Tie4N_NMOSDummy_length'] = _Samp_Tie4N_NMOSDummy_length
        _Caculation_Parameters['_Tie4N_NMOSDummy_placement'] = _Samp_Tie4N_NMOSDummy_placement
        _Caculation_Parameters['_Tie4P_PMOSNumberofGate'] = _Samp_Tie4P_PMOSNumberofGate
        _Caculation_Parameters['_Tie4P_PMOSChannelWidth'] = _Samp_Tie4P_PMOSChannelWidth
        _Caculation_Parameters['_Tie4P_PMOSChannellength'] = _Samp_Tie4P_PMOSChannellength
        _Caculation_Parameters['_Tie4P_GateSpacing'] = _Samp_Tie4P_GateSpacing
        _Caculation_Parameters['_Tie4P_SDWidth'] = _Samp_Tie4P_SDWidth
        _Caculation_Parameters['_Tie4P_XVT'] = _Samp_Tie4P_XVT
        _Caculation_Parameters['_Tie4P_PCCrit'] = _Samp_Tie4P_PCCrit
        _Caculation_Parameters['_Tie4P_Source_Via_TF'] = _Samp_Tie4P_Source_Via_TF
        _Caculation_Parameters['_Tie4P_Drain_Via_TF'] = _Samp_Tie4P_Drain_Via_TF
        _Caculation_Parameters['_Tie4P_PMOSDummy'] = _Samp_Tie4P_PMOSDummy
        _Caculation_Parameters['_Tie4P_PMOSDummy_length'] = _Samp_Tie4P_PMOSDummy_length
        _Caculation_Parameters['_Tie4P_PMOSDummy_placement'] = _Samp_Tie4P_PMOSDummy_placement
        _Caculation_Parameters['_Tie4_NBodyCOX'] = _Samp_Tie4_NBodyCOX
        _Caculation_Parameters['_Tie4_NBodyCOY'] = _Samp_Tie4_NBodyCOY
        _Caculation_Parameters['_Tie4_PBodyCOX'] = _Samp_Tie4_PBodyCOX
        _Caculation_Parameters['_Tie4_PBodyCOY'] = _Samp_Tie4_PBodyCOY

        _Caculation_Parameters['_Tie8N_NMOSNumberofGate'] = _Samp_Tie8N_NMOSNumberofGate
        _Caculation_Parameters['_Tie8N_NMOSChannelWidth'] = _Samp_Tie8N_NMOSChannelWidth
        _Caculation_Parameters['_Tie8N_NMOSChannellength'] = _Samp_Tie8N_NMOSChannellength
        _Caculation_Parameters['_Tie8N_GateSpacing'] = _Samp_Tie8N_GateSpacing
        _Caculation_Parameters['_Tie8N_SDWidth'] = _Samp_Tie8N_SDWidth
        _Caculation_Parameters['_Tie8N_XVT'] = _Samp_Tie8N_XVT
        _Caculation_Parameters['_Tie8N_PCCrit'] = _Samp_Tie8N_PCCrit
        _Caculation_Parameters['_Tie8N_Source_Via_TF'] = _Samp_Tie8N_Source_Via_TF
        _Caculation_Parameters['_Tie8N_Drain_Via_TF'] = _Samp_Tie8N_Drain_Via_TF
        _Caculation_Parameters['_Tie8N_NMOSDummy'] = _Samp_Tie8N_NMOSDummy
        _Caculation_Parameters['_Tie8N_NMOSDummy_length'] = _Samp_Tie8N_NMOSDummy_length
        _Caculation_Parameters['_Tie8N_NMOSDummy_placement'] = _Samp_Tie8N_NMOSDummy_placement
        _Caculation_Parameters['_Tie8P_PMOSNumberofGate'] = _Samp_Tie8P_PMOSNumberofGate
        _Caculation_Parameters['_Tie8P_PMOSChannelWidth'] = _Samp_Tie8P_PMOSChannelWidth
        _Caculation_Parameters['_Tie8P_PMOSChannellength'] = _Samp_Tie8P_PMOSChannellength
        _Caculation_Parameters['_Tie8P_GateSpacing'] = _Samp_Tie8P_GateSpacing
        _Caculation_Parameters['_Tie8P_SDWidth'] = _Samp_Tie8P_SDWidth
        _Caculation_Parameters['_Tie8P_XVT'] = _Samp_Tie8P_XVT
        _Caculation_Parameters['_Tie8P_PCCrit'] = _Samp_Tie8P_PCCrit
        _Caculation_Parameters['_Tie8P_Source_Via_TF'] = _Samp_Tie8P_Source_Via_TF
        _Caculation_Parameters['_Tie8P_Drain_Via_TF'] = _Samp_Tie8P_Drain_Via_TF
        _Caculation_Parameters['_Tie8P_PMOSDummy'] = _Samp_Tie8P_PMOSDummy
        _Caculation_Parameters['_Tie8P_PMOSDummy_length'] = _Samp_Tie8P_PMOSDummy_length
        _Caculation_Parameters['_Tie8P_PMOSDummy_placement'] = _Samp_Tie8P_PMOSDummy_placement
        _Caculation_Parameters['_Tie8_NBodyCOX'] = _Samp_Tie8_NBodyCOX
        _Caculation_Parameters['_Tie8_NBodyCOY'] = _Samp_Tie8_NBodyCOY
        _Caculation_Parameters['_Tie8_PBodyCOX'] = _Samp_Tie8_PBodyCOX
        _Caculation_Parameters['_Tie8_PBodyCOY'] = _Samp_Tie8_PBodyCOY

        _Caculation_Parameters['_Tr12_NMOSNumberofGate'] = _Samp_Tr12_NMOSNumberofGate
        _Caculation_Parameters['_Tr12_NMOSChannelWidth'] = _Samp_Tr12_NMOSChannelWidth
        _Caculation_Parameters['_Tr12_NMOSChannellength'] = _Samp_Tr12_NMOSChannellength
        _Caculation_Parameters['_Tr12_GateSpacing'] = _Samp_Tr12_GateSpacing
        _Caculation_Parameters['_Tr12_SDWidth'] = _Samp_Tr12_SDWidth
        _Caculation_Parameters['_Tr12_XVT'] = _Samp_Tr12_XVT
        _Caculation_Parameters['_Tr12_PCCrit'] = _Samp_Tr12_PCCrit
        _Caculation_Parameters['_Tr12_Source_Via_TF'] = _Samp_Tr12_Source_Via_TF
        _Caculation_Parameters['_Tr12_Drain_Via_TF'] = _Samp_Tr12_Drain_Via_TF
        _Caculation_Parameters['_Tr12_NMOSDummy'] = _Samp_Tr12_NMOSDummy
        _Caculation_Parameters['_Tr12_NMOSDummy_length'] = _Samp_Tr12_NMOSDummy_length
        _Caculation_Parameters['_Tr12_NMOSDummy_placement'] = _Samp_Tr12_NMOSDummy_placement

        _Caculation_Parameters['_Tr3_NMOSNumberofGate'] = _Samp_Tr3_NMOSNumberofGate
        _Caculation_Parameters['_Tr3_NMOSChannelWidth'] = _Samp_Tr3_NMOSChannelWidth
        _Caculation_Parameters['_Tr3_NMOSChannellength'] = _Samp_Tr3_NMOSChannellength
        _Caculation_Parameters['_Tr3_GateSpacing'] = _Samp_Tr3_GateSpacing
        _Caculation_Parameters['_Tr3_SDWidth'] = _Samp_Tr3_SDWidth
        _Caculation_Parameters['_Tr3_XVT'] = _Samp_Tr3_XVT
        _Caculation_Parameters['_Tr3_PCCrit'] = _Samp_Tr3_PCCrit
        _Caculation_Parameters['_Tr3_Source_Via_TF'] = _Samp_Tr3_Source_Via_TF
        _Caculation_Parameters['_Tr3_Drain_Via_TF'] = _Samp_Tr3_Drain_Via_TF
        _Caculation_Parameters['_Tr3_NMOSDummy'] = _Samp_Tr3_NMOSDummy
        _Caculation_Parameters['_Tr3_NMOSDummy_length'] = _Samp_Tr3_NMOSDummy_length
        _Caculation_Parameters['_Tr3_NMOSDummy_placement'] = _Samp_Tr3_NMOSDummy_placement

        _Caculation_Parameters['_Tr10_NMOSNumberofGate'] = _Samp_Tr10_NMOSNumberofGate
        _Caculation_Parameters['_Tr10_NMOSChannelWidth'] = _Samp_Tr10_NMOSChannelWidth
        _Caculation_Parameters['_Tr10_NMOSChannellength'] = _Samp_Tr10_NMOSChannellength
        _Caculation_Parameters['_Tr10_GateSpacing'] = _Samp_Tr10_GateSpacing
        _Caculation_Parameters['_Tr10_SDWidth'] = _Samp_Tr10_SDWidth
        _Caculation_Parameters['_Tr10_XVT'] = _Samp_Tr10_XVT
        _Caculation_Parameters['_Tr10_PCCrit'] = _Samp_Tr10_PCCrit
        _Caculation_Parameters['_Tr10_Source_Via_TF'] = _Samp_Tr10_Source_Via_TF
        _Caculation_Parameters['_Tr10_Drain_Via_TF'] = _Samp_Tr10_Drain_Via_TF
        _Caculation_Parameters['_Tr10_NMOSDummy'] = _Samp_Tr10_NMOSDummy
        _Caculation_Parameters['_Tr10_NMOSDummy_length'] = _Samp_Tr10_NMOSDummy_length
        _Caculation_Parameters['_Tr10_NMOSDummy_placement'] = _Samp_Tr10_NMOSDummy_placement

        _Caculation_Parameters['_Tr12Tr3Tr10_Guardring_NumCont'] = _Samp_Tr12Tr3Tr10_Guardring_NumCont

        _Caculation_Parameters['_HDVNCAP_Length'] = _Samp_HDVNCAP_Length
        _Caculation_Parameters['_HDVNCAP_LayoutOption'] = _Samp_HDVNCAP_LayoutOption
        _Caculation_Parameters['_HDVNCAP_NumFigPair'] = _Samp_HDVNCAP_NumFigPair
        _Caculation_Parameters['_HDVNCAP_Array'] = _Samp_HDVNCAP_Array
        _Caculation_Parameters['_HDVNCAP_Cbot_Ctop_metalwidth'] = _Samp_HDVNCAP_Cbot_Ctop_metalwidth

        ## BootSW (Positive) Placement
        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_BootSW_Pos'] = self._SrefElementDeclaration(_DesignObj=C13_01_CtopCbotRouted_YJ_v01_00._CtopCbotRouted(_DesignParameter=None, _Name='{}:SRF_BootSW_Pos'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_BootSW_Pos']['_Reflect'] = [1, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_BootSW_Pos']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_BootSW_Pos']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## initialized Sref coordinate
        self._DesignParameter['SRF_BootSW_Pos']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH3('SRF_SARLogicWtComparator', 'SRF_Comparator', 'SRF_Slicer', '_Guardring', '_Met1Layerx')
        target_coord = [tmp1[0][0][0][0][0][0]['_XY_left'][0], centY + int(_SpaceBtwBootSWPosNeg / 2)]
        ## Approaching_coord: _XY_type2
        tmp2x = self.get_param_KJH4('SRF_BootSW_Pos', 'BND_Ctop_Vtc_M5')
        tmp2y = self.get_param_KJH4('SRF_BootSW_Pos', 'SRF_C13_00', 'SRF_C11', 'SRF_Tr11', 'SRF_Nbodyring', 'SRF_NbodyBottom', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = [tmp2x[0][0][0]['_XY_right'][0], tmp2y[0][0][0][0][0][0][0][0][0]['_XY_down'][1]]
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_BootSW_Pos')
        Scoord = tmp3[0][0]['_XY_origin']
        XOffset = -200
        Scoord[0] = Scoord[0] + XOffset
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['SRF_BootSW_Pos']['_XYCoordinates'] = tmpXY

        print('###############################################')
        print('##     Bootstrapped Switch (Negative)        ##')
        print('##            Calculation_Start!!            ##')
        print('###############################################')

        ## BootSW (Negative) Placement
        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_BootSW_Neg'] = self._SrefElementDeclaration(_DesignObj=C13_01_CtopCbotRouted_YJ_v01_00._CtopCbotRouted(_DesignParameter=None, _Name='{}:SRF_BootSW_Neg'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_BootSW_Neg']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_BootSW_Neg']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_BootSW_Neg']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## initialized Sref coordinate
        self._DesignParameter['SRF_BootSW_Neg']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH3('SRF_SARLogicWtComparator', 'SRF_Comparator', 'SRF_Slicer', '_Guardring', '_Met1Layerx')
        target_coord = [tmp1[0][0][0][0][0][0]['_XY_left'][0], centY - int(_SpaceBtwBootSWPosNeg / 2)]
        ## Approaching_coord: _XY_type2
        tmp2x = self.get_param_KJH4('SRF_BootSW_Neg', 'BND_Ctop_Vtc_M5')
        tmp2y = self.get_param_KJH4('SRF_BootSW_Neg', 'SRF_C13_00', 'SRF_C11', 'SRF_Tr11', 'SRF_Nbodyring', 'SRF_NbodyBottom', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = [tmp2x[0][0][0]['_XY_right'][0], tmp2y[0][0][0][0][0][0][0][0][0]['_XY_down'][1]]
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_BootSW_Neg')
        Scoord = tmp3[0][0]['_XY_origin']
        XOffset = -200
        Scoord[0] = Scoord[0] + XOffset
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['SRF_BootSW_Neg']['_XYCoordinates'] = tmpXY

        ## BND_NWellExtensionOfTr11
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NWellExtensionOfTr11s'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_BootSW_Pos', 'SRF_C13_00', 'SRF_C11', 'SRF_Tr11', 'SRF_Nbodyring', 'BND_ExtenNwell_Bottom')
        tmp2 = self.get_param_KJH4('SRF_BootSW_Neg', 'SRF_C13_00', 'SRF_C11', 'SRF_Tr11', 'SRF_Nbodyring', 'BND_ExtenNwell_Bottom')
        self._DesignParameter['BND_NWellExtensionOfTr11s']['_YWidth'] = abs(tmp1[0][0][0][0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0][0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_NWellExtensionOfTr11s']['_XWidth'] = tmp1[0][0][0][0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NWellExtensionOfTr11s']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NWellExtensionOfTr11s')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NWellExtensionOfTr11s')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_NWellExtensionOfTr11s']['_XYCoordinates'] = tmpXY

        ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
        ## BootSW -> CDAC Top Node Routing
        ##### BND_SampOutput2CDACTop_Pos_Vtc_M6
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_SampOutput2CDACTop_Pos_Vtc_M6'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6'][0],
            _Datatype=DesignParameters._LayerMapping['METAL6'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_BootSW_Pos', 'BND_OutputNode_Hrz_M6')
        if _CDAC_Folding == True:
            tmp2 = self.get_param_KJH4('SRF_CDAC_Pos', 'BND_CDACTopNode_Vtc_M7')
            self._DesignParameter['BND_SampOutput2CDACTop_Pos_Vtc_M6']['_YWidth'] = abs(tmp1[0][0][0]['_XY_cent'][1] - tmp2[0][0][0]['_XY_cent'][1])
        else:
            tmp2 = self.get_param_KJH4('SRF_CDAC_Pos', 'BND_CDACTopNode_Hrz_M7')
            self._DesignParameter['BND_SampOutput2CDACTop_Pos_Vtc_M6']['_YWidth'] = abs(tmp1[0][0][0]['_XY_cent'][1] - tmp2[0][0][0]['_XY_down'][1])

            ## Define Boundary_element _XWidth
        self._DesignParameter['BND_SampOutput2CDACTop_Pos_Vtc_M6']['_XWidth'] = 400

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_SampOutput2CDACTop_Pos_Vtc_M6']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0]['_XY_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_SampOutput2CDACTop_Pos_Vtc_M6')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_SampOutput2CDACTop_Pos_Vtc_M6')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_SampOutput2CDACTop_Pos_Vtc_M6']['_XYCoordinates'] = tmpXY

        ##### BND_SampOutput2CDACTop_Neg_Vtc_M6
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_SampOutput2CDACTop_Neg_Vtc_M6'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6'][0],
            _Datatype=DesignParameters._LayerMapping['METAL6'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_BootSW_Neg', 'BND_OutputNode_Hrz_M6')
        if _CDAC_Folding == True:
            tmp2 = self.get_param_KJH4('SRF_CDAC_Neg', 'BND_CDACTopNode_Vtc_M7')
            self._DesignParameter['BND_SampOutput2CDACTop_Neg_Vtc_M6']['_YWidth'] = abs(tmp1[0][0][0]['_XY_cent'][1] - tmp2[0][0][0]['_XY_cent'][1])
        else:
            tmp2 = self.get_param_KJH4('SRF_CDAC_Neg', 'BND_CDACTopNode_Hrz_M7')
            self._DesignParameter['BND_SampOutput2CDACTop_Neg_Vtc_M6']['_YWidth'] = abs(tmp1[0][0][0]['_XY_cent'][1] - tmp2[0][0][0]['_XY_down'][1])

            ## Define Boundary_element _XWidth
        self._DesignParameter['BND_SampOutput2CDACTop_Neg_Vtc_M6']['_XWidth'] = 400

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_SampOutput2CDACTop_Neg_Vtc_M6']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0]['_XY_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_SampOutput2CDACTop_Neg_Vtc_M6')
        approaching_coord = tmp2[0][0]['_XY_down_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_SampOutput2CDACTop_Neg_Vtc_M6')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_SampOutput2CDACTop_Neg_Vtc_M6']['_XYCoordinates'] = tmpXY

        ##### BND_SampOutput2CDACTop_Hrz_M7
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_SampOutput2CDACTop_Hrz_M7'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL7'][0],
            _Datatype=DesignParameters._LayerMapping['METAL7'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        if _CDAC_Folding == True:
            ## Define Boundary_element _YWidth
            self._DesignParameter['BND_SampOutput2CDACTop_Hrz_M7']['_YWidth'] = 400
            tmp2 = self.get_param_KJH4('SRF_CDAC_Pos', 'BND_CDACTopNode_Vtc_M7')
        else:
            ## Define Boundary_element _YWidth
            tmp2 = self.get_param_KJH4('SRF_CDAC_Pos', 'BND_CDACTopNode_Hrz_M7')
            self._DesignParameter['BND_SampOutput2CDACTop_Hrz_M7']['_YWidth'] = tmp2[0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('BND_SampOutput2CDACTop_Pos_Vtc_M6')
        self._DesignParameter['BND_SampOutput2CDACTop_Hrz_M7']['_XWidth'] = abs(tmp1[0][0]['_XY_left'][0] - tmp2[0][0][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_SampOutput2CDACTop_Hrz_M7']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_SampOutput2CDACTop_Hrz_M7')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_SampOutput2CDACTop_Hrz_M7')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Cal2 (Neg)
        tmp1 = self.get_param_KJH4('BND_SampOutput2CDACTop_Neg_Vtc_M6')
        target_coord = tmp1[0][0]['_XY_up_left']
        approaching_coord = tmp2[0][0]['_XY_up_left']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define coordinates
        self._DesignParameter['BND_SampOutput2CDACTop_Hrz_M7']['_XYCoordinates'] = tmpXY

        #### Via -> BND_SampOutput2CDACTop_Neg_Vtc_M6 -> BND_CDACTopNode
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 6
        _Caculation_Parameters['_Layer2'] = 7
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        ## Sref ViaX declaration
        self._DesignParameter['SRF_SampOut2CDACTop_ViaM6M7'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_SampOut2CDACTop_ViaM6M7'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_SampOut2CDACTop_ViaM6M7']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_SampOut2CDACTop_ViaM6M7']['_Angle'] = 0

        ## Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH4('BND_SampOutput2CDACTop_Hrz_M7')
        tmp2 = self.get_param_KJH4('BND_SampOutput2CDACTop_Pos_Vtc_M6')
        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

        ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY' or 'SameEnclosure'
        _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], None)

        ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_SampOut2CDACTop_ViaM6M7']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_SampOut2CDACTop_ViaM6M7']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        target_coord = [tmp2[0][0]['_XY_cent'][0], tmp1[0][0]['_XY_cent'][1]]
        ## Approaching_coord
        tmp4 = self.get_param_KJH4('SRF_SampOut2CDACTop_ViaM6M7', 'SRF_ViaM6M7', 'BND_Met6Layer')
        approaching_coord = tmp4[0][0][0][0]['_XY_cent']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_SampOut2CDACTop_ViaM6M7')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Cal 2 (Neg)
        target_coord = [tmp2[0][0]['_XY_cent'][0], tmp1[1][0]['_XY_cent'][1]]
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_SampOut2CDACTop_ViaM6M7']['_XYCoordinates'] = tmpXY

        ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
        ## SAR Logic -> CDAC Driver Input Routing
        for j in range(_NumofBit):
            ## BND_CDAC_Pos_DrvIn_Hrz_M3
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_CDAC_Pos_MSB{}DrvIn_Hrz_M3'.format(j)] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL3'][0],
                _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )
            ## Define Boundary_element _YWidth
            if _CDAC_Folding == True:
                tmp1 = self.get_param_KJH4('SRF_CDAC_Pos',
                                           'BND_CDACFold1_{}B{}_DrvInput_Hrz_M3'.format('Lo', _NumofBit - 1 - j))
                self._DesignParameter['BND_CDAC_Pos_MSB{}DrvIn_Hrz_M3'.format(j)]['_YWidth'] = tmp1[0][0][0]['_Ywidth']
            else:
                tmp1 = self.get_param_KJH4('SRF_CDAC_Pos', 'SRF_CDACWtDriver', 'SRF_DriverArray',
                                           'BND_{}C_Driver_Input_Hrz_M3'.format(2 ** (_NumofBit - 1 - j)))
                self._DesignParameter['BND_CDAC_Pos_MSB{}DrvIn_Hrz_M3'.format(j)]['_YWidth'] = tmp1[0][0][0][0][0]['_Ywidth']

            ## Define Boundary_element _XWidth
            if _CDAC_Folding == True:
                tmp2 = self.get_param_KJH4('SRF_SARLogicWtComparator', 'SRF_SARLogicWtBuffers', 'SRF_UpperCDACPreDriver',
                                           'SRF_InvChain', 'SRF_Output_ViaM2Mx', 'SRF_ViaM2M3', 'BND_Met2Layer')
                self._DesignParameter['BND_CDAC_Pos_MSB{}DrvIn_Hrz_M3'.format(j)]['_XWidth'] = \
                    tmp2[0][0][0][j][0][0][0][0]['_XY_right'][0] - tmp1[0][0][0]['_XY_left'][0]
            else:
                tmp2 = self.get_param_KJH4('SRF_SARLogicWtComparator', 'SRF_SARLogicWtBuffers', 'SRF_UpperCDACPreDriver',
                                           'SRF_InvChain', 'SRF_Output_ViaM2Mx', 'SRF_ViaM2M3', 'BND_Met2Layer')
                self._DesignParameter['BND_CDAC_Pos_MSB{}DrvIn_Hrz_M3'.format(j)]['_XWidth'] = \
                    tmp2[0][0][0][j][0][0][0][0]['_XY_right'][0] - tmp1[0][0][0][0][0]['_XY_left'][0]

            if self._DesignParameter['BND_CDAC_Pos_MSB{}DrvIn_Hrz_M3'.format(j)]['_XWidth'] < 0:
                self._DesignParameter['BND_CDAC_Pos_MSB{}DrvIn_Hrz_M3'.format(j)]['_XWidth'] = self._DesignParameter['BND_CDAC_Pos_MSB{}DrvIn_Hrz_M3'.format(j)]['_XWidth'] - 244

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['BND_CDAC_Pos_MSB{}DrvIn_Hrz_M3'.format(j)]['_XYCoordinates'] = [[0, 0]]
            if _CDAC_Folding == True:
                target_coord = tmp1[0][0][0]['_XY_down_left']
            else:
                target_coord = tmp1[0][0][0][0][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_CDAC_Pos_MSB{}DrvIn_Hrz_M3'.format(j))
            approaching_coord = tmp2[0][0]['_XY_down_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_CDAC_Pos_MSB{}DrvIn_Hrz_M3'.format(j))
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_CDAC_Pos_MSB{}DrvIn_Hrz_M3'.format(j)]['_XYCoordinates'] = tmpXY

            ## BND_CDAC_Pos_DrvIn_Vtc_M4
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_CDAC_Pos_MSB{}DrvIn_Vtc_M4'.format(j)] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL4'][0],
                _Datatype=DesignParameters._LayerMapping['METAL4'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )
            ## Define Boundary_element _YWidth
            tmp1 = self.get_param_KJH4('BND_CDAC_Pos_MSB{}DrvIn_Hrz_M3'.format(j))
            tmp2 = self.get_param_KJH4('SRF_SARLogicWtComparator', 'SRF_SARLogicWtBuffers', 'SRF_UpperCDACPreDriver', 'SRF_InvChain', 'SRF_Output_ViaM2Mx', 'SRF_ViaM2M3', 'BND_Met2Layer')
            self._DesignParameter['BND_CDAC_Pos_MSB{}DrvIn_Vtc_M4'.format(j)]['_YWidth'] = abs(tmp1[0][0]['_XY_cent'][1] - tmp2[0][0][0][_NumofBit - 1 - j][0][0][0][0]['_XY_up'][1])

            ## Define Boundary_element _XWidth
            self._DesignParameter['BND_CDAC_Pos_MSB{}DrvIn_Vtc_M4'.format(j)]['_XWidth'] = 50

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['BND_CDAC_Pos_MSB{}DrvIn_Vtc_M4'.format(j)]['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord: _XY_type1
            target_coord = tmp1[0][0]['_XY_right']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_CDAC_Pos_MSB{}DrvIn_Vtc_M4'.format(j))
            approaching_coord = tmp2[0][0]['_XY_up_right']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_CDAC_Pos_MSB{}DrvIn_Vtc_M4'.format(j))
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_CDAC_Pos_MSB{}DrvIn_Vtc_M4'.format(j)]['_XYCoordinates'] = tmpXY

            #####################################################
            ## BND_CDAC_Neg_DrvIn_Hrz_M3
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_CDAC_Neg_MSB{}DrvIn_Hrz_M3'.format(j)] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL3'][0],
                _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )
            ## Define Boundary_element _YWidth
            if _CDAC_Folding == True:
                tmp1 = self.get_param_KJH4('SRF_CDAC_Neg', 'BND_CDACFold1_{}B{}_DrvInput_Hrz_M3'.format('Lo', _NumofBit - 1 - j))
                self._DesignParameter['BND_CDAC_Neg_MSB{}DrvIn_Hrz_M3'.format(j)]['_YWidth'] = tmp1[0][0][0]['_Ywidth']
            else:
                tmp1 = self.get_param_KJH4('SRF_CDAC_Neg', 'SRF_CDACWtDriver', 'SRF_DriverArray', 'BND_{}C_Driver_Input_Hrz_M3'.format(2 ** (_NumofBit - 1 - j)))
                self._DesignParameter['BND_CDAC_Neg_MSB{}DrvIn_Hrz_M3'.format(j)]['_YWidth'] = tmp1[0][0][0][0][0]['_Ywidth']

            ## Define Boundary_element _XWidth
            if _CDAC_Folding == True:
                tmp2 = self.get_param_KJH4('SRF_SARLogicWtComparator', 'SRF_SARLogicWtBuffers', 'SRF_LowerCDACPreDriver', 'SRF_InvChain', 'SRF_Output_ViaM2Mx', 'SRF_ViaM2M3', 'BND_Met2Layer')
                self._DesignParameter['BND_CDAC_Neg_MSB{}DrvIn_Hrz_M3'.format(j)]['_XWidth'] = tmp2[0][0][0][j][0][0][0][0]['_XY_right'][0] - tmp1[0][0][0]['_XY_left'][0]
            else:
                tmp2 = self.get_param_KJH4('SRF_SARLogicWtComparator', 'SRF_SARLogicWtBuffers', 'SRF_LowerCDACPreDriver', 'SRF_InvChain', 'SRF_Output_ViaM2Mx', 'SRF_ViaM2M3', 'BND_Met2Layer')
                self._DesignParameter['BND_CDAC_Neg_MSB{}DrvIn_Hrz_M3'.format(j)]['_XWidth'] = tmp2[0][0][0][j][0][0][0][0]['_XY_right'][0] - tmp1[0][0][0][0][0]['_XY_left'][0]

            if self._DesignParameter['BND_CDAC_Neg_MSB{}DrvIn_Hrz_M3'.format(j)]['_XWidth'] < 0:
                self._DesignParameter['BND_CDAC_Neg_MSB{}DrvIn_Hrz_M3'.format(j)]['_XWidth'] = \
                    self._DesignParameter['BND_CDAC_Neg_MSB{}DrvIn_Hrz_M3'.format(j)]['_XWidth'] - 244

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['BND_CDAC_Neg_MSB{}DrvIn_Hrz_M3'.format(j)]['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord: _XY_type1
            if _CDAC_Folding == True:
                target_coord = tmp1[0][0][0]['_XY_up_left']
            else:
                target_coord = tmp1[0][0][0][0][0]['_XY_up_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_CDAC_Neg_MSB{}DrvIn_Hrz_M3'.format(j))
            approaching_coord = tmp2[0][0]['_XY_down_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_CDAC_Neg_MSB{}DrvIn_Hrz_M3'.format(j))
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_CDAC_Neg_MSB{}DrvIn_Hrz_M3'.format(j)]['_XYCoordinates'] = tmpXY

            ## BND_CDAC_Neg_DrvIn_Vtc_M4
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_CDAC_Neg_MSB{}DrvIn_Vtc_M4'.format(j)] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL4'][0],
                _Datatype=DesignParameters._LayerMapping['METAL4'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )
            ## Define Boundary_element _YWidth
            tmp1 = self.get_param_KJH4('BND_CDAC_Neg_MSB{}DrvIn_Hrz_M3'.format(j))
            tmp2 = self.get_param_KJH4('SRF_SARLogicWtComparator', 'SRF_SARLogicWtBuffers', 'SRF_LowerCDACPreDriver', 'SRF_InvChain', 'SRF_Output_ViaM2Mx', 'SRF_ViaM2M3', 'BND_Met2Layer')
            self._DesignParameter['BND_CDAC_Neg_MSB{}DrvIn_Vtc_M4'.format(j)]['_YWidth'] = abs(tmp1[0][0]['_XY_cent'][1] - tmp2[0][0][0][_NumofBit - 1 - j][0][0][0][0]['_XY_down'][1])

            ## Define Boundary_element _XWidth
            self._DesignParameter['BND_CDAC_Neg_MSB{}DrvIn_Vtc_M4'.format(j)]['_XWidth'] = 50

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['BND_CDAC_Neg_MSB{}DrvIn_Vtc_M4'.format(j)]['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord: _XY_type1
            target_coord = tmp1[0][0]['_XY_right']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_CDAC_Neg_MSB{}DrvIn_Vtc_M4'.format(j))
            approaching_coord = tmp2[0][0]['_XY_down_right']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_CDAC_Neg_MSB{}DrvIn_Vtc_M4'.format(j))
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_CDAC_Neg_MSB{}DrvIn_Vtc_M4'.format(j)]['_XYCoordinates'] = tmpXY

        #### 'BND_CDAC_Neg_MSB#DrvIn_Vtc_M4' <-> 'BND_CDAC_Neg_MSB#DrvIn_Hrz_M3'
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CDAC_Neg_DrvIN_ViaM3M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_CDAC_Neg_DrvIN_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CDAC_Neg_DrvIN_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CDAC_Neg_DrvIN_ViaM3M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CDAC_Neg_DrvIN_ViaM3M4']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## initialized Sref coordinate
        self._DesignParameter['SRF_CDAC_Neg_DrvIN_ViaM3M4']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CDAC_Neg_DrvIN_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CDAC_Neg_DrvIN_ViaM3M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        for i in range(_NumofBit):
            tmp1 = self.get_param_KJH4('BND_CDAC_Neg_MSB{}DrvIn_Vtc_M4'.format(i))
            ## Target_coord
            target_coord = tmp1[0][0]['_XY_down_right']
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define
        self._DesignParameter['SRF_CDAC_Neg_DrvIN_ViaM3M4']['_XYCoordinates'] = tmpXY

        #### 'BND_CDAC_Pos_MSB#DrvIn_Vtc_M4' <-> 'BND_CDAC_Pos_MSB#DrvIn_Hrz_M3'
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CDAC_Pos_DrvIN_ViaM3M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_CDAC_Pos_DrvIN_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CDAC_Pos_DrvIN_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CDAC_Pos_DrvIN_ViaM3M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CDAC_Pos_DrvIN_ViaM3M4']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## initialized Sref coordinate
        self._DesignParameter['SRF_CDAC_Pos_DrvIN_ViaM3M4']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CDAC_Pos_DrvIN_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CDAC_Pos_DrvIN_ViaM3M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        for i in range(_NumofBit):
            tmp1 = self.get_param_KJH4('BND_CDAC_Pos_MSB{}DrvIn_Vtc_M4'.format(i))
            ## Target_coord
            target_coord = tmp1[0][0]['_XY_up_right']
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define
        self._DesignParameter['SRF_CDAC_Pos_DrvIN_ViaM3M4']['_XYCoordinates'] = tmpXY

        # ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
        # ## CDAC Top -> Comparator Input Routing
        ## get_param_KJH3를 사용하기 위해 Angle과 Reflect를 초기화시킴.
        self._DesignParameter['SRF_SARLogicWtComparator']['_DesignObj']._DesignParameter['SRF_Comparator']['_DesignObj']._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_Angle'] = 0
        self._DesignParameter['SRF_SARLogicWtComparator']['_DesignObj']._DesignParameter['SRF_Comparator']['_DesignObj']._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_SARLogicWtComparator']['_DesignObj']._DesignParameter['SRF_Comparator']['_DesignObj']._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_Angle'] = 0
        self._DesignParameter['SRF_SARLogicWtComparator']['_DesignObj']._DesignParameter['SRF_Comparator']['_DesignObj']._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_SARLogicWtComparator']['_DesignObj']._DesignParameter['SRF_Comparator']['_DesignObj']._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_Angle'] = 0
        self._DesignParameter['SRF_SARLogicWtComparator']['_DesignObj']._DesignParameter['SRF_Comparator']['_DesignObj']._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_Reflect'] = [0, 0, 0]

        tmpP = self.get_param_KJH3('SRF_SARLogicWtComparator', 'SRF_Comparator', 'SRF_Slicer', '_NMOSSET', '_VIANMOSPoly2Met1NMOS1', '_Met1Layer')
        tmpN = self.get_param_KJH3('SRF_SARLogicWtComparator', 'SRF_Comparator', 'SRF_Slicer', '_NMOSSET', '_VIANMOSPoly2Met1NMOS2', '_Met1Layer')
        tmpCent = int((tmpP[0][0][0][0][0][0][0]['_XY_right'][0] + tmpN[0][0][0][0][0][0][0]['_XY_left'][0]) / 2)

        #### Comp Input Via M1M6
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 6
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CompInput_ViaM1M6'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_CompInput_ViaM1M6'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CompInput_ViaM1M6']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CompInput_ViaM1M6']['_Angle'] = 0

        ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY' or 'SameEnclosure'
        _COX, _COY = self._CalculateNumViaByXYWidth(tmpP[0][0][0][0][0][0][0]['_Xwidth'], tmpP[0][0][0][0][0][0][0]['_Ywidth'], None)

        ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = max(_COY, 2)

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CompInput_ViaM1M6']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CompInput_ViaM1M6']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        target_coord = tmpP[0][0][0][0][0][0][0]['_XY_down']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CompInput_ViaM1M6', 'SRF_ViaM1M2', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CompInput_ViaM1M6')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Calc 2 (VinN)
        target_coord = tmpN[0][0][0][0][0][0][0]['_XY_down']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CompInput_ViaM1M6']['_XYCoordinates'] = tmpXY

        #### Comp Input P Via M6M7
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 6
        _Caculation_Parameters['_Layer2'] = 7
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CompInputN_ViaM6M7'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_CompInputN_ViaM6M7'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CompInputN_ViaM6M7']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CompInputN_ViaM6M7']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CompInputN_ViaM6M7']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CompInputN_ViaM6M7']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('SRF_CompInput_ViaM1M6', 'SRF_ViaM1M2', 'BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_down']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CompInputN_ViaM6M7', 'SRF_ViaM6M7', 'BND_Met6Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CompInputN_ViaM6M7')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CompInputN_ViaM6M7']['_XYCoordinates'] = tmpXY

        #### Comp Input N Via M6M7
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 6
        _Caculation_Parameters['_Layer2'] = 7
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CompInputP_ViaM6M7'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_CompInputP_ViaM6M7'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CompInputP_ViaM6M7']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CompInputP_ViaM6M7']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CompInputP_ViaM6M7']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CompInputP_ViaM6M7']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('SRF_CompInput_ViaM1M6', 'SRF_ViaM1M2', 'BND_Met1Layer')
        target_coord = tmp1[1][0][0][0]['_XY_up']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CompInputP_ViaM6M7', 'SRF_ViaM6M7', 'BND_Met6Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CompInputP_ViaM6M7')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CompInputP_ViaM6M7']['_XYCoordinates'] = tmpXY

        ## BND_CompInputP_Hrz_M7
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CompInputN_Hrz_M7'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL7'][0],
            _Datatype=DesignParameters._LayerMapping['METAL7'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CompInputN_ViaM6M7', 'SRF_ViaM6M7', 'BND_Met6Layer')
        self._DesignParameter['BND_CompInputN_Hrz_M7']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CompInputN_Hrz_M7']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_left'][0] - tmpCent) + 200

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CompInputN_Hrz_M7']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CompInputN_Hrz_M7')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CompInputN_Hrz_M7')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CompInputN_Hrz_M7']['_XYCoordinates'] = tmpXY

        ## BND_CompInputN_Hrz_M7
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CompInputP_Hrz_M7'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL7'][0],
            _Datatype=DesignParameters._LayerMapping['METAL7'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CompInputP_ViaM6M7', 'SRF_ViaM6M7', 'BND_Met6Layer')
        self._DesignParameter['BND_CompInputP_Hrz_M7']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CompInputP_Hrz_M7']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_right'][0] - tmpCent) + 200

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CompInputP_Hrz_M7']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0]['_XY_up_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CompInputP_Hrz_M7')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CompInputP_Hrz_M7')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CompInputP_Hrz_M7']['_XYCoordinates'] = tmpXY

        ## BND_CompInputP_Vtc_IA
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CompInputP_Vtc_IA'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL8'][0],
            _Datatype=DesignParameters._LayerMapping['METAL8'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_CompInputP_Hrz_M7')
        if _CDAC_Folding == True:
            tmp2 = self.get_param_KJH4('SRF_CDAC_Pos', 'BND_CDACUpperTopNode_Hrz_IA')
        else:
            tmp2 = self.get_param_KJH4('SRF_CDAC_Pos', 'BND_CDACTopNode_Hrz_M7')
        self._DesignParameter['BND_CompInputP_Vtc_IA']['_YWidth'] = abs(tmp1[0][0]['_XY_up'][1] - tmp2[0][0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CompInputP_Vtc_IA']['_XWidth'] = 400

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CompInputP_Vtc_IA']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CompInputP_Vtc_IA')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CompInputP_Vtc_IA')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CompInputP_Vtc_IA']['_XYCoordinates'] = tmpXY

        ## BND_CompInputN_Vtc_IA
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CompInputN_Vtc_IA'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL8'][0],
            _Datatype=DesignParameters._LayerMapping['METAL8'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_CompInputN_Hrz_M7')
        if _CDAC_Folding == True:
            tmp2 = self.get_param_KJH4('SRF_CDAC_Neg', 'BND_CDACUpperTopNode_Hrz_IA')
        else:
            tmp2 = self.get_param_KJH4('SRF_CDAC_Neg', 'BND_CDACTopNode_Hrz_M7')
        self._DesignParameter['BND_CompInputN_Vtc_IA']['_YWidth'] = abs(tmp1[0][0]['_XY_down'][1] - tmp2[0][0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CompInputN_Vtc_IA']['_XWidth'] = 400

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CompInputN_Vtc_IA']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0]['_XY_down_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CompInputN_Vtc_IA')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CompInputN_Vtc_IA')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CompInputN_Vtc_IA']['_XYCoordinates'] = tmpXY

        if _CDAC_Folding == True:
            ## BND_CompInputExten_Hrz_IA
            ## Boundary_element Generation
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_CompInputExten_Hrz_IA'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL8'][0],
                _Datatype=DesignParameters._LayerMapping['METAL8'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )
            ## Define Boundary_element _YWidth
            tmp1_1 = self.get_param_KJH4('SRF_CDAC_Pos', 'BND_CDACLowerTopNode_Hrz_IA')
            tmp1_2 = self.get_param_KJH4('SRF_CDAC_Pos', 'BND_CDACUpperTopNode_Hrz_IA')
            tmp1_3 = self.get_param_KJH4('SRF_CDAC_Neg', 'BND_CDACUpperTopNode_Hrz_IA')
            tmp1_4 = self.get_param_KJH4('SRF_CDAC_Neg', 'BND_CDACLowerTopNode_Hrz_IA')
            tmp2 = self.get_param_KJH4('BND_CompInputN_Vtc_IA')
            self._DesignParameter['BND_CompInputExten_Hrz_IA']['_YWidth'] = tmp1_1[0][0][0]['_Ywidth']

            ## Define Boundary_element _XWidth
            self._DesignParameter['BND_CompInputExten_Hrz_IA']['_XWidth'] = abs(tmp1_1[0][0][0]['_XY_right'][0] - tmp2[0][0]['_XY_left'][0])

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_CompInputExten_Hrz_IA']['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
            tmpXY = []
            ## Calculate
            ## Approaching_coord: _XY_type2
            tmp3 = self.get_param_KJH4('BND_CompInputExten_Hrz_IA')
            approaching_coord = tmp3[0][0]['_XY_down_left']
            ## Sref coord
            tmp4 = self.get_param_KJH4('BND_CompInputExten_Hrz_IA')
            Scoord = tmp4[0][0]['_XY_origin']
            ## Cal
            ## Target_coord1: _XY_type1
            target_coord = [tmp2[0][0]['_XY_left'][0], tmp1_1[0][0][0]['_XY_down'][1]]
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Target_coord2: _XY_type1
            target_coord = [tmp2[0][0]['_XY_left'][0], tmp1_2[0][0][0]['_XY_down'][1]]
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Target_coord3: _XY_type1
            target_coord = [tmp2[0][0]['_XY_left'][0], tmp1_3[0][0][0]['_XY_up'][1]]
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Target_coord4: _XY_type1
            target_coord = [tmp2[0][0]['_XY_left'][0], tmp1_4[0][0][0]['_XY_up'][1]]
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_CompInputExten_Hrz_IA']['_XYCoordinates'] = tmpXY

        ### SRF_CompInput_ViaM7M8
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 7
        _Caculation_Parameters['_Layer2'] = 8
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CompInput_ViaM7M8'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_CompInput_ViaM7M8'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CompInput_ViaM7M8']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CompInput_ViaM7M8']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CompInput_ViaM7M8']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CompInput_ViaM7M8']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1x = self.get_param_KJH4('BND_CompInputP_Vtc_IA')
        tmp1y = self.get_param_KJH4('BND_CompInputP_Hrz_M7')
        target_coord = [tmp1x[0][0]['_XY_right'][0], tmp1y[0][0]['_XY_up'][1]]
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CompInput_ViaM7M8', 'SRF_ViaM7M8', 'BND_Met7Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CompInput_ViaM7M8')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Calc2
        approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
        tmp1x = self.get_param_KJH4('BND_CompInputN_Vtc_IA')
        tmp1y = self.get_param_KJH4('BND_CompInputN_Hrz_M7')
        target_coord = [tmp1x[0][0]['_XY_left'][0], tmp1y[0][0]['_XY_down'][1]]
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define
        self._DesignParameter['SRF_CompInput_ViaM7M8']['_XYCoordinates'] = tmpXY

        ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
        ## BootSW CLK Signal Path Generation
        #### BND_BootSWCLKSignalPath_Hrz_M5
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_BootSWCLKSignalPath_Hrz_M5'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5'][0],
            _Datatype=DesignParameters._LayerMapping['METAL5'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_SARLogicWtComparator', 'BND_CLKSampANDIn_Vtc_M4')
        tmp2 = self.get_param_KJH4('SRF_BootSW_Neg', 'SRF_C13_00', 'SRF_C11', 'BND_Tr6Tr11GateRouting_Vtc_M2')
        self._DesignParameter['BND_BootSWCLKSignalPath_Hrz_M5']['_XWidth'] = abs(
            tmp1[0][0][0]['_XY_right'][0] - tmp2[0][0][0][0][0]['_XY_cent'][0])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_BootSWCLKSignalPath_Hrz_M5']['_YWidth'] = 50

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_BootSWCLKSignalPath_Hrz_M5']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1y = self.get_param_KJH4('SRF_SARLogicWtComparator', 'SRF_Comparator', 'BND_SlicerCLKInput_Hrz_M3')
        target_coord = [tmp1[0][0][0]['_XY_right'][0], tmp1y[0][0][0][0]['_XY_down'][1]]
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_BootSWCLKSignalPath_Hrz_M5')
        approaching_coord = tmp2[0][0]['_XY_down_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_BootSWCLKSignalPath_Hrz_M5')
        Scoord = tmp3[0][0]['_XY_origin']
        SpaceBtwCLKCompInAndCLKBootSWIn = 50
        Scoord[1] = Scoord[1] + SpaceBtwCLKCompInAndCLKBootSWIn
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_BootSWCLKSignalPath_Hrz_M5']['_XYCoordinates'] = tmpXY

        ### SRF_BootSWCLKSignalPath_ViaM4M5
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 4
        _Caculation_Parameters['_Layer2'] = 5
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_BootSWCLKSignalPath_ViaM4M5'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_BootSWCLKSignalPath_ViaM4M5'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_BootSWCLKSignalPath_ViaM4M5']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_BootSWCLKSignalPath_ViaM4M5']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_BootSWCLKSignalPath_ViaM4M5']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_BootSWCLKSignalPath_ViaM4M5']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_BootSWCLKSignalPath_Hrz_M5')
        target_coord = tmp1[0][0]['_XY_down_right']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_BootSWCLKSignalPath_ViaM4M5', 'SRF_ViaM4M5', 'BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_BootSWCLKSignalPath_ViaM4M5')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define
        self._DesignParameter['SRF_BootSWCLKSignalPath_ViaM4M5']['_XYCoordinates'] = tmpXY

        ### BND_Tr6Tr11GateRouteExten_Vtc_M4; Connecting BootSW Neg, Pos and 'BND_BootSWCLKSignalPath_Hrz_M5'
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Tr6Tr11GateRouteExten_Vtc_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_BootSW_Pos', 'SRF_C13_00', 'SRF_C11', 'BND_Tr6Tr11GateRouting_Vtc_M2')
        tmp2 = self.get_param_KJH4('SRF_BootSW_Neg', 'SRF_C13_00', 'SRF_C11', 'BND_Tr6Tr11GateRouting_Vtc_M2')
        overlapAmount = 400
        self._DesignParameter['BND_Tr6Tr11GateRouteExten_Vtc_M4']['_YWidth'] = abs(tmp1[0][0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0]['_XY_up'][1]) + overlapAmount

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Tr6Tr11GateRouteExten_Vtc_M4']['_XWidth'] = tmp1[0][0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Tr6Tr11GateRouteExten_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp2[0][0][0][0][0]['_XY_up_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Tr6Tr11GateRouteExten_Vtc_M4')
        approaching_coord = tmp2[0][0]['_XY_down_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Tr6Tr11GateRouteExten_Vtc_M4')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[1] = Scoord[1] - int(overlapAmount / 2)
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Tr6Tr11GateRouteExten_Vtc_M4']['_XYCoordinates'] = tmpXY

        ### BND_BootSWCLKSignalPath_Vtc_M5; Connecting BootSW Neg, Pos and 'BND_BootSWCLKSignalPath_Hrz_M5'
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_BootSWCLKSignalPath_Vtc_M5'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5'][0],
            _Datatype=DesignParameters._LayerMapping['METAL5'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_Tr6Tr11GateRouteExten_Vtc_M4')
        tmp2 = self.get_param_KJH4('BND_BootSWCLKSignalPath_Hrz_M5')
        self._DesignParameter['BND_BootSWCLKSignalPath_Vtc_M5']['_YWidth'] = abs(tmp1[0][0]['_XY_cent'][1] - tmp2[0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_BootSWCLKSignalPath_Vtc_M5']['_XWidth'] = 50

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_BootSWCLKSignalPath_Vtc_M5']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp2[0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_BootSWCLKSignalPath_Vtc_M5')
        approaching_coord = tmp2[0][0]['_XY_up']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_BootSWCLKSignalPath_Vtc_M5')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_BootSWCLKSignalPath_Vtc_M5']['_XYCoordinates'] = tmpXY

        ### SRF_Tr6Tr11GateRouteExten_ViaM2M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        ## Sref ViaX declaration
        self._DesignParameter['SRF_Tr6Tr11GateRouteExten_ViaM2M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Tr6Tr11GateRouteExten_ViaM2M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_Tr6Tr11GateRouteExten_ViaM2M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_Tr6Tr11GateRouteExten_ViaM2M4']['_Angle'] = 0

        ## Calcuate Overlapped XYcoord
        tmp2 = self.get_param_KJH4('BND_Tr6Tr11GateRouteExten_Vtc_M4')

        ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY' or 'SameEnclosure'
        _COX, _COY = self._CalculateNumViaByXYWidth(tmp2[0][0]['_Xwidth'], int(overlapAmount / 2), None)

        ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Tr6Tr11GateRouteExten_ViaM2M4']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_Tr6Tr11GateRouteExten_ViaM2M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_Tr6Tr11GateRouteExten_Vtc_M4')
        target_coord = tmp1[0][0]['_XY_up']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Tr6Tr11GateRouteExten_ViaM2M4', 'SRF_ViaM2M3', 'BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Tr6Tr11GateRouteExten_ViaM2M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Calc2
        target_coord = tmp1[0][0]['_XY_down']
        approaching_coord = tmp2[0][0][0][0]['_XY_down']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_Tr6Tr11GateRouteExten_ViaM2M4']['_XYCoordinates'] = tmpXY

        ### SRF_BootSWCLKSignalCent_ViaM4M5
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 4
        _Caculation_Parameters['_Layer2'] = 5
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 3

        ## Sref ViaX declaration
        self._DesignParameter['SRF_BootSWCLKSignalCent_ViaM4M5'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_BootSWCLKSignalCent_ViaM4M5'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_BootSWCLKSignalCent_ViaM4M5']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_BootSWCLKSignalCent_ViaM4M5']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_BootSWCLKSignalCent_ViaM4M5']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_BootSWCLKSignalCent_ViaM4M5']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_BootSWCLKSignalPath_Vtc_M5')
        target_coord = tmp1[0][0]['_XY_down']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_BootSWCLKSignalCent_ViaM4M5', 'SRF_ViaM4M5', 'BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_BootSWCLKSignalCent_ViaM4M5')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define
        self._DesignParameter['SRF_BootSWCLKSignalCent_ViaM4M5']['_XYCoordinates'] = tmpXY

        #### Bootstrapped Sampler CLKB Inverter generation
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D00_00_Inverter_KJH._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType'] = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn'] = 'Up'

        _Caculation_Parameters['_NMOS_NumberofGate'] = _CLKBInv_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth'] = _CLKBInv_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength'] = _CLKBInv_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing'] = None
        _Caculation_Parameters['_NMOS_SDWidth'] = None
        _Caculation_Parameters['_NMOS_XVT'] = _CLKBInv_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit'] = True

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
        _Caculation_Parameters['_NMOS_Xvt_Placement'] = 'Up'

        _Caculation_Parameters['_NMOS_POGate_Comb_TF'] = True
        _Caculation_Parameters['_NMOS_POGate_Comb_length'] = _CLKBInv_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF'] = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx'] = [0, 1]

        _Caculation_Parameters['_PMOS_MosType'] = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn'] = 'Dn'

        _Caculation_Parameters['_PMOS_NumberofGate'] = _CLKBInv_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth'] = _CLKBInv_Inv_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength'] = _CLKBInv_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing'] = None
        _Caculation_Parameters['_PMOS_SDWidth'] = None
        _Caculation_Parameters['_PMOS_XVT'] = _CLKBInv_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit'] = True

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
        _Caculation_Parameters['_PMOS_Xvt_Placement'] = 'Dn'

        _Caculation_Parameters['_PMOS_POGate_Comb_TF'] = True
        _Caculation_Parameters['_PMOS_POGate_Comb_length'] = _CLKBInv_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF'] = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx'] = [0, 1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont'] = _CLKBInv_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody'] = _CLKBInv_XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_NumCont'] = _CLKBInv_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody'] = _CLKBInv_Xvtdown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt'] = _CLKBInv_PMOSXvt2NMOSXvt

        ## Sref ViaX declaration
        self._DesignParameter['SRF_SampCLKBInverter'] = self._SrefElementDeclaration(_DesignObj=D00_00_Inverter_KJH._Inverter(_DesignParameter=None, _Name='{}:SRF_SampCLKBInverter'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_SampCLKBInverter']['_Reflect'] = [1, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_SampCLKBInverter']['_Angle'] = 180

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_SampCLKBInverter']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_SampCLKBInverter']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1x = self.get_param_KJH4('SRF_BootSW_Pos', 'SRF_C13_00', 'SRF_C11', 'SRF_Tr11', 'SRF_Nbodyring', 'SRF_NbodyLeft', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        target_coord = [tmp1x[0][0][0][0][0][0][0][0][0]['_XY_left'][0], centY]
        ## Approaching_coord
        tmp2x = self.get_param_KJH4('SRF_SampCLKBInverter', 'SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        tmp2y = self.get_param_KJH4('SRF_SampCLKBInverter', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        tmp2y_1 = int((tmp2y[0][0][0][0][0]['_XY_down'][1] + tmp2x[0][0][0][0][0]['_XY_up'][1]) / 2)
        approaching_coord = [tmp2x[0][0][0][0][0]['_XY_left'][0], tmp2y_1]
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_SampCLKBInverter')
        Scoord = tmp3[0][0]['_XY_origin']
        SpaceBtwInvBodyAndGuardring = 500
        Scoord[0] = Scoord[0] - SpaceBtwInvBodyAndGuardring
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define
        self._DesignParameter['SRF_SampCLKBInverter']['_XYCoordinates'] = tmpXY

        ### BND_BootSWCLKB_Vtc_M2; Connecting Output of SRF_SampCLKBInverter and 'BND_BootSWCLKSignalPath_Hrz_M5'
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_BootSWCLKB_Vtc_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_BootSW_Pos', 'SRF_C13_00', 'SRF_C07', 'SRF_Tr12Tr3Tr10', 'SRF_Tr12Tr3Tr10_Gate_ViaM0M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        tmp2 = self.get_param_KJH4('SRF_BootSW_Neg', 'SRF_C13_00', 'SRF_C07', 'SRF_Tr12Tr3Tr10', 'SRF_Tr12Tr3Tr10_Gate_ViaM0M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        self._DesignParameter['BND_BootSWCLKB_Vtc_M2']['_YWidth'] = abs(tmp1[0][0][0][0][0][0][0][0]['_XY_down'][1] - tmp2[0][0][0][0][0][0][0][0]['_XY_down'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_BootSWCLKB_Vtc_M2']['_XWidth'] = 100

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_BootSWCLKB_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp2[0][0][0][0][0][0][0][0]['_XY_down']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_BootSWCLKB_Vtc_M2')
        approaching_coord = tmp2[0][0]['_XY_down']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_BootSWCLKB_Vtc_M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_BootSWCLKB_Vtc_M2']['_XYCoordinates'] = tmpXY

        ### BND_BootSWCLKBInvIn_Hrz_M3; Connecting Output of SRF_SampCLKBInverter and 'BND_BootSWCLKSignalPath_Hrz_M5'
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_BootSWCLKBInvIn_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _XWidth
        # tmp1 = self.get_param_KJH4('SRF_BootSW_Pos','SRF_C13_00','SRF_C07','SRF_Tr12Tr3Tr10','SRF_Tr12Tr3Tr10_Gate_ViaM0M4','SRF_ViaM3M4','BND_Met4Layer')
        # tmp2 = self.get_param_KJH4('SRF_BootSW_Neg','SRF_C13_00','SRF_C07','SRF_Tr12Tr3Tr10','SRF_Tr12Tr3Tr10_Gate_ViaM0M4','SRF_ViaM3M4','BND_Met4Layer')
        tmp1 = self.get_param_KJH4('BND_BootSWCLKB_Vtc_M2')
        tmp2 = self.get_param_KJH4('SRF_SampCLKBInverter', 'BND_Out_Vtc_M2')
        self._DesignParameter['BND_BootSWCLKBInvIn_Hrz_M3']['_XWidth'] = abs(tmp1[0][0]['_XY_cent'][0] - tmp2[0][0][0]['_XY_cent'][0])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_BootSWCLKBInvIn_Hrz_M3']['_YWidth'] = 50

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_BootSWCLKBInvIn_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0]['_XY_cent']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_BootSWCLKBInvIn_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_BootSWCLKBInvIn_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_BootSWCLKBInvIn_Hrz_M3']['_XYCoordinates'] = tmpXY

        ## SRF_BootSWCLKBInvIn_ViaM2M3
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_BootSWCLKBInvIn_ViaM2M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_BootSWCLKBInvIn_ViaM2M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_BootSWCLKBInvIn_ViaM2M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_BootSWCLKBInvIn_ViaM2M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_BootSWCLKBInvIn_ViaM2M3']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_BootSWCLKBInvIn_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_BootSWCLKBInvIn_Hrz_M3')
        target_coord = tmp1[0][0]['_XY_left']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_BootSWCLKBInvIn_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_BootSWCLKBInvIn_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Calc 2
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        target_coord = tmp1[0][0]['_XY_right']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_BootSWCLKBInvIn_ViaM2M3']['_XYCoordinates'] = tmpXY

        ### BND_BootSWCLKBInvIn_Hrz_M3; Connecting Output of SRF_SampCLKBInverter and 'BND_BootSWCLKSignalPath_Hrz_M5'
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CLKBInvIn_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('BND_Tr6Tr11GateRouteExten_Vtc_M4')
        tmp2 = self.get_param_KJH4('SRF_SampCLKBInverter', 'BND_Input_Vtc_M1')
        self._DesignParameter['BND_CLKBInvIn_Hrz_M3']['_XWidth'] = abs(tmp1[0][0]['_XY_cent'][0] - tmp2[0][0][0]['_XY_cent'][0])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CLKBInvIn_Hrz_M3']['_YWidth'] = 50

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CLKBInvIn_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp2[0][0][0]['_XY_cent']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CLKBInvIn_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CLKBInvIn_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CLKBInvIn_Hrz_M3']['_XYCoordinates'] = tmpXY

        ## SRF_CLKBInvIn_ViaM3M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 3

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKBInvIn_ViaM3M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_CLKBInvIn_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKBInvIn_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKBInvIn_ViaM3M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKBInvIn_ViaM3M4']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKBInvIn_ViaM3M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_CLKBInvIn_Hrz_M3')
        target_coord = tmp1[0][0]['_XY_right']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CLKBInvIn_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKBInvIn_ViaM3M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define
        self._DesignParameter['SRF_CLKBInvIn_ViaM3M4']['_XYCoordinates'] = tmpXY

        ## SRF_CLKBInvIn_ViaM1M3
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKBInvIn_ViaM1M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_CLKBInvIn_ViaM1M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKBInvIn_ViaM1M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKBInvIn_ViaM1M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKBInvIn_ViaM1M3']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKBInvIn_ViaM1M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_CLKBInvIn_Hrz_M3')
        target_coord = tmp1[0][0]['_XY_left']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CLKBInvIn_ViaM1M3', 'SRF_ViaM1M2', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKBInvIn_ViaM1M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define
        self._DesignParameter['SRF_CLKBInvIn_ViaM1M3']['_XYCoordinates'] = tmpXY

        '''
        ### Decimation
        if (_Driver_DecimationIfDriverPlacedInCommonCentroid == True):
            for j in range(0, len(_Driver_DecimationFactor)):
                for i in range(0, 2 ** (_NumofBit - 1 - j), -1):
                    tmp = _Driver_DecimationFactor[j]
                    if tmp == 0:
                        pass
                    else:
                        if i % tmp != 0:
                            del self._DesignParameter['SRF_CDAC_Pos']['_DesignObj']._DesignParameter['SRF_CDACWtDriver']['_DesignObj']._DesignParameter['SRF_DriverArray']['_DesignObj']._DesignParameter['SRF_{}C_DriverCell'.format(2 ** (_NumofBit - 1 - j))]['_XYCoordinates'][i]
                            del self._DesignParameter['SRF_CDAC_Pos']['_DesignObj']._DesignParameter['SRF_CDACWtDriver']['_DesignObj']._DesignParameter['SRF_DriverArray']['_DesignObj']._DesignParameter['BND_{}C_Driver_Input_Vtc_M2'.format(2 ** (_NumofBit - 1 - j))]['_XYCoordinates'][i]
                            del self._DesignParameter['SRF_CDAC_Pos']['_DesignObj']._DesignParameter['SRF_CDACWtDriver']['_DesignObj']._DesignParameter['BND_{}C_Driver_Drain_Vtc_M4'.format(2 ** (_NumofBit - 1 - j))]['_XYCoordinates'][i]

                            del self._DesignParameter['SRF_CDAC_Neg']['_DesignObj']._DesignParameter['SRF_CDACWtDriver']['_DesignObj']._DesignParameter['SRF_DriverArray']['_DesignObj']._DesignParameter['SRF_{}C_DriverCell'.format(2 ** (_NumofBit - 1 - j))]['_XYCoordinates'][i]
                            del self._DesignParameter['SRF_CDAC_Neg']['_DesignObj']._DesignParameter['SRF_CDACWtDriver']['_DesignObj']._DesignParameter['SRF_DriverArray']['_DesignObj']._DesignParameter['BND_{}C_Driver_Input_Vtc_M2'.format(2 ** (_NumofBit - 1 - j))]['_XYCoordinates'][i]
                            del self._DesignParameter['SRF_CDAC_Neg']['_DesignObj']._DesignParameter['SRF_CDACWtDriver']['_DesignObj']._DesignParameter['BND_{}C_Driver_Drain_Vtc_M4'.format(2 ** (_NumofBit - 1 - j))]['_XYCoordinates'][i]
                else:
                    pass
        else:
            pass
        '''

        if (_Driver_DecimationIfDriverPlacedInCommonCentroid == True):
            ## No folding
            if (_CDAC_Folding == False):
                for j in range(0, len(_Driver_DecimationFactor)):
                    for i in reversed(range(0, 2 ** (_NumofBit - 1 - j))):
                        tmp = _Driver_DecimationFactor[j]
                        if tmp == 0:
                            pass
                        else:
                            if i % tmp != 0:
                                del self._DesignParameter['SRF_CDAC_Pos']['_DesignObj']._DesignParameter['SRF_CDACWtDriver']['_DesignObj']._DesignParameter['SRF_DriverArray']['_DesignObj']._DesignParameter['SRF_{}C_DriverCell'.format(2 ** (_NumofBit - 1 - j))]['_XYCoordinates'][i]
                                del self._DesignParameter['SRF_CDAC_Pos']['_DesignObj']._DesignParameter['SRF_CDACWtDriver']['_DesignObj']._DesignParameter['SRF_DriverArray']['_DesignObj']._DesignParameter['BND_{}C_Driver_Input_Vtc_M2'.format(2 ** (_NumofBit - 1 - j))]['_XYCoordinates'][i]
                                del self._DesignParameter['SRF_CDAC_Pos']['_DesignObj']._DesignParameter['SRF_CDACWtDriver']['_DesignObj']._DesignParameter['BND_{}C_Driver_Drain_Vtc_M4'.format(2 ** (_NumofBit - 1 - j))]['_XYCoordinates'][i]

                                del self._DesignParameter['SRF_CDAC_Neg']['_DesignObj']._DesignParameter['SRF_CDACWtDriver']['_DesignObj']._DesignParameter['SRF_DriverArray']['_DesignObj']._DesignParameter['SRF_{}C_DriverCell'.format(2 ** (_NumofBit - 1 - j))]['_XYCoordinates'][i]
                                del self._DesignParameter['SRF_CDAC_Neg']['_DesignObj']._DesignParameter['SRF_CDACWtDriver']['_DesignObj']._DesignParameter['SRF_DriverArray']['_DesignObj']._DesignParameter['BND_{}C_Driver_Input_Vtc_M2'.format(2 ** (_NumofBit - 1 - j))]['_XYCoordinates'][i]
                                del self._DesignParameter['SRF_CDAC_Neg']['_DesignObj']._DesignParameter['SRF_CDACWtDriver']['_DesignObj']._DesignParameter['BND_{}C_Driver_Drain_Vtc_M4'.format(2 ** (_NumofBit - 1 - j))]['_XYCoordinates'][i]
                            else:
                                pass
            ## Folding
            else:
                for j in range(0,len(_Driver_DecimationFactor)):
                    for i in reversed(range(0, 2 ** (_NumofBit - 2 - j))):
                        tmp = _Driver_DecimationFactor[j]
                        if tmp ==0:
                            pass
                        else:
                            if i % tmp != 0:
                                del self._DesignParameter['SRF_CDAC_Pos']['_DesignObj']._DesignParameter['SRF_CDAC_UpperHalf']['_DesignObj']._DesignParameter['SRF_DriverArray']['_DesignObj']._DesignParameter['SRF_{}C_DriverCell'.format(2 ** (_NumofBit - 2 - j))]['_XYCoordinates'][i]
                                del self._DesignParameter['SRF_CDAC_Pos']['_DesignObj']._DesignParameter['SRF_CDAC_UpperHalf']['_DesignObj']._DesignParameter['SRF_DriverArray']['_DesignObj']._DesignParameter['BND_{}C_Driver_Input_Vtc_M2'.format(2 ** (_NumofBit - 2 - j))]['_XYCoordinates'][i]
                                del self._DesignParameter['SRF_CDAC_Pos']['_DesignObj']._DesignParameter['SRF_CDAC_UpperHalf']['_DesignObj']._DesignParameter['BND_{}C_Driver_Drain_Vtc_M4'.format(2 ** (_NumofBit - 2 - j))]['_XYCoordinates'][i]

                                del self._DesignParameter['SRF_CDAC_Pos']['_DesignObj']._DesignParameter['SRF_CDAC_LowerHalf']['_DesignObj']._DesignParameter['SRF_DriverArray']['_DesignObj']._DesignParameter['SRF_{}C_DriverCell'.format(2 ** (_NumofBit - 2 - j))]['_XYCoordinates'][i]
                                del self._DesignParameter['SRF_CDAC_Pos']['_DesignObj']._DesignParameter['SRF_CDAC_LowerHalf']['_DesignObj']._DesignParameter['SRF_DriverArray']['_DesignObj']._DesignParameter['BND_{}C_Driver_Input_Vtc_M2'.format(2 ** (_NumofBit - 2 - j))]['_XYCoordinates'][i]
                                del self._DesignParameter['SRF_CDAC_Pos']['_DesignObj']._DesignParameter['SRF_CDAC_LowerHalf']['_DesignObj']._DesignParameter['BND_{}C_Driver_Drain_Vtc_M4'.format(2 ** (_NumofBit - 2 - j))]['_XYCoordinates'][i]

                                del self._DesignParameter['SRF_CDAC_Neg']['_DesignObj']._DesignParameter['SRF_CDAC_UpperHalf']['_DesignObj']._DesignParameter['SRF_DriverArray']['_DesignObj']._DesignParameter['SRF_{}C_DriverCell'.format(2 ** (_NumofBit - 2 - j))]['_XYCoordinates'][i]
                                del self._DesignParameter['SRF_CDAC_Neg']['_DesignObj']._DesignParameter['SRF_CDAC_UpperHalf']['_DesignObj']._DesignParameter['SRF_DriverArray']['_DesignObj']._DesignParameter['BND_{}C_Driver_Input_Vtc_M2'.format(2 ** (_NumofBit - 2 - j))]['_XYCoordinates'][i]
                                del self._DesignParameter['SRF_CDAC_Neg']['_DesignObj']._DesignParameter['SRF_CDAC_UpperHalf']['_DesignObj']._DesignParameter['BND_{}C_Driver_Drain_Vtc_M4'.format(2 ** (_NumofBit - 2 - j))]['_XYCoordinates'][i]

                                del self._DesignParameter['SRF_CDAC_Neg']['_DesignObj']._DesignParameter['SRF_CDAC_LowerHalf']['_DesignObj']._DesignParameter['SRF_DriverArray']['_DesignObj']._DesignParameter['SRF_{}C_DriverCell'.format(2 ** (_NumofBit - 2 - j))]['_XYCoordinates'][i]
                                del self._DesignParameter['SRF_CDAC_Neg']['_DesignObj']._DesignParameter['SRF_CDAC_LowerHalf']['_DesignObj']._DesignParameter['SRF_DriverArray']['_DesignObj']._DesignParameter['BND_{}C_Driver_Input_Vtc_M2'.format(2 ** (_NumofBit - 2 - j))]['_XYCoordinates'][i]
                                del self._DesignParameter['SRF_CDAC_Neg']['_DesignObj']._DesignParameter['SRF_CDAC_LowerHalf']['_DesignObj']._DesignParameter['BND_{}C_Driver_Drain_Vtc_M4'.format(2 ** (_NumofBit - 2 - j))]['_XYCoordinates'][i]

                            else:
                                pass
        else:
            pass

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
    libname = 'Proj_ADC_B106_ADCCoreLay18'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'M00_00_CDACWtSARLogic_fold10_Decimation_v4'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        _NumofBit=10,
        _CDAC_Folding=True,  # None/True/False
        _Driver_CommonCentroidPlacementIfCDACFolded=True,  # 말 그대로 True이면 CommmonCentroid 배치가 됨.
        _Driver_DecimationIfDriverPlacedInCommonCentroid=True,
        _Driver_DecimationFactor=[4, 2, 0, 0, 0, 0],  # [MSB, MSB-1 ... MSB-x]: 단 X<MSB  # 위 옵션 True시 작동; MSB부터 벡터로 작성; [3,2,2] 시 MSB0 -> 3:1, MSB1 -> 2:1, MSB2 -> 2:1, ... 1은 불가 # upper/or lower 기준으로 decimation됨.
        _SpaceBtwBootSWPosNeg=200,  # Fixed

        ## SAR Logic sizing
        _Test_distance=330,  # Fixed
        _Routing_width=50,  # Fixed
        _Routing_distance=80,  # Fixed

        _SARLogic_YWidthOfCLKSrc=100,  # Fixed (CLK spine)
        _SARLogic_SpaceBtwCLKSrcAndCLKSamp=100,  # Fixed (Dist. CLK spine and CLK_Samp)
        _SARLogic_YWidthOfCLKSamp=100,  # Fixed (CLK spine)

        _SARLogic_YWidthOfCompOut=100,  # Fixed
        _SARLogic_SpaceBtwCompOutAndCLKDout=100,  # Fixed
        _SARLogic_YWidthOfCLKDout=100,  # Fixed

        ## DFF Common
        _SARLogic_DFF_Pbody_NumCont=2,  # number (Fixed)
        _SARLogic_DFF_Nbody_NumCont=2,  # number (Fixed)
        _SARLogic_DFF_PMOSXvt2NMOSXvt=1150,  # number (Fixed)
        _SARLogic_DFF_XvtTop2Pbody=None,  # number/None(Minimum) (Fixed)
        _SARLogic_DFF_Xvtdown2Nbody=None,  # number/None(Minimum) (Fixed)

        ## Master Xgate1
        ## Xgate common

        ## Xgate NMOS
        _SARLogic_Mst_Xgate1_NMOS_NumberofGate=1,  # 1
        _SARLogic_Mst_Xgate1_NMOS_ChannelWidth=400,  # 400
        _SARLogic_Mst_Xgate1_NMOS_ChannelLength=30,  # 30
        _SARLogic_Mst_Xgate1_NMOS_XVT='SLVT',
        _SARLogic_Mst_Xgate1_NMOS_POGate_Comb_length=100,  # (Fixed)

        ## Xgate PMOS
        _SARLogic_Mst_Xgate1_PMOS_NumberofGate=1,  # 1
        _SARLogic_Mst_Xgate1_PMOS_ChannelWidth=800,  # 200
        _SARLogic_Mst_Xgate1_PMOS_ChannelLength=30,
        _SARLogic_Mst_Xgate1_PMOS_XVT='SLVT',
        _SARLogic_Mst_Xgate1_PMOS_POGate_Comb_length=100,  # (Fixed)

        ## Master Xgate2
        ## Xgate common

        ## Xgate NMOS
        _SARLogic_Mst_Xgate2_NMOS_NumberofGate=1,
        _SARLogic_Mst_Xgate2_NMOS_ChannelWidth=400,
        _SARLogic_Mst_Xgate2_NMOS_ChannelLength=30,
        _SARLogic_Mst_Xgate2_NMOS_XVT='SLVT',
        _SARLogic_Mst_Xgate2_NMOS_POGate_Comb_length=100,  # (Fixed)

        ## Xgate PMOS
        _SARLogic_Mst_Xgate2_PMOS_NumberofGate=1,
        _SARLogic_Mst_Xgate2_PMOS_ChannelWidth=800,
        _SARLogic_Mst_Xgate2_PMOS_ChannelLength=30,
        _SARLogic_Mst_Xgate2_PMOS_XVT='SLVT',
        _SARLogic_Mst_Xgate2_PMOS_POGate_Comb_length=100,  # (Fixed)

        ## Master Nor1
        ## Nor1 common

        ## NMOS
        ## NMOS common
        _SARLogic_Mst_Nor1_NMOS_XVT='SLVT',

        ## NMOSA
        _SARLogic_Mst_Nor1_NMOSA_NumberofGate=4,
        _SARLogic_Mst_Nor1_NMOSA_ChannelWidth=400,
        _SARLogic_Mst_Nor1_NMOSA_ChannelLength=30,
        _SARLogic_Mst_Nor1_NMOSA_POGate_Comb_length=100,  # (Fixed)

        ## NMOSB
        _SARLogic_Mst_Nor1_NMOSB_NumberofGate=4,
        _SARLogic_Mst_Nor1_NMOSB_ChannelWidth=400,
        _SARLogic_Mst_Nor1_NMOSB_ChannelLength=30,
        _SARLogic_Mst_Nor1_NMOSB_POGate_Comb_length=100,  # (Fixed)

        ## PMOS
        ## PMOS common
        _SARLogic_Mst_Nor1_PMOS_XVT='SLVT',

        ## PMOSA
        _SARLogic_Mst_Nor1_PMOSA_NumberofGate=8,
        _SARLogic_Mst_Nor1_PMOSA_ChannelWidth=800,
        _SARLogic_Mst_Nor1_PMOSA_ChannelLength=30,
        _SARLogic_Mst_Nor1_PMOSA_POGate_Comb_length=100,  # (Fixed)

        ## PMOSB
        _SARLogic_Mst_Nor1_PMOSB_NumberofGate=8,
        _SARLogic_Mst_Nor1_PMOSB_ChannelWidth=800,
        _SARLogic_Mst_Nor1_PMOSB_ChannelLength=30,
        _SARLogic_Mst_Nor1_PMOSB_POGate_Comb_length=100,  # (Fixed)

        ## Master Nor2
        ## Nor2 common

        ## NMOS
        ## NMOS common
        _SARLogic_Mst_Nor2_NMOS_XVT='SLVT',

        ## NMOSA
        _SARLogic_Mst_Nor2_NMOSA_NumberofGate=1,
        _SARLogic_Mst_Nor2_NMOSA_ChannelWidth=400,
        _SARLogic_Mst_Nor2_NMOSA_ChannelLength=30,
        _SARLogic_Mst_Nor2_NMOSA_POGate_Comb_length=100,  # (Fixed)

        ## NMOSB
        _SARLogic_Mst_Nor2_NMOSB_NumberofGate=1,
        _SARLogic_Mst_Nor2_NMOSB_ChannelWidth=400,
        _SARLogic_Mst_Nor2_NMOSB_ChannelLength=30,
        _SARLogic_Mst_Nor2_NMOSB_POGate_Comb_length=100,  # (Fixed)

        ## PMOS
        ## PMOS common
        _SARLogic_Mst_Nor2_PMOS_XVT='SLVT',

        ## PMOSA
        _SARLogic_Mst_Nor2_PMOSA_NumberofGate=2,
        _SARLogic_Mst_Nor2_PMOSA_ChannelWidth=800,
        _SARLogic_Mst_Nor2_PMOSA_ChannelLength=30,
        _SARLogic_Mst_Nor2_PMOSA_POGate_Comb_length=100,  # (Fixed)

        ## PMOSB
        _SARLogic_Mst_Nor2_PMOSB_NumberofGate=2,
        _SARLogic_Mst_Nor2_PMOSB_ChannelWidth=800,
        _SARLogic_Mst_Nor2_PMOSB_ChannelLength=30,
        _SARLogic_Mst_Nor2_PMOSB_POGate_Comb_length=100,  # (Fixed)

        ## Master Inv1 : Set pre-driver
        ## Inv1 common

        ## Inv1 NMOS
        _SARLogic_Mst_Inv1_NMOS_NumberofGate=1,
        _SARLogic_Mst_Inv1_NMOS_ChannelWidth=400,
        _SARLogic_Mst_Inv1_NMOS_ChannelLength=30,
        _SARLogic_Mst_Inv1_NMOS_XVT='SLVT',
        _SARLogic_Mst_Inv1_NMOS_POGate_Comb_length=100,  # (Fixed)

        ## Inv1 PMOS
        _SARLogic_Mst_Inv1_PMOS_NumberofGate=1,
        _SARLogic_Mst_Inv1_PMOS_ChannelWidth=800,
        _SARLogic_Mst_Inv1_PMOS_ChannelLength=30,
        _SARLogic_Mst_Inv1_PMOS_XVT='SLVT',
        _SARLogic_Mst_Inv1_PMOS_POGate_Comb_length=100,  # (Fixed)

        ## Master Inv2 : Set driver
        ## Inv2 common

        ## Inv2 NMOS
        _SARLogic_Mst_Inv2_NMOS_NumberofGate=2,
        _SARLogic_Mst_Inv2_NMOS_ChannelWidth=400,
        _SARLogic_Mst_Inv2_NMOS_ChannelLength=30,
        _SARLogic_Mst_Inv2_NMOS_XVT='SLVT',
        _SARLogic_Mst_Inv2_NMOS_POGate_Comb_length=100,  # (Fixed)

        ## Inv2 PMOS
        _SARLogic_Mst_Inv2_PMOS_NumberofGate=2,
        _SARLogic_Mst_Inv2_PMOS_ChannelWidth=800,
        _SARLogic_Mst_Inv2_PMOS_ChannelLength=30,
        _SARLogic_Mst_Inv2_PMOS_XVT='SLVT',
        _SARLogic_Mst_Inv2_PMOS_POGate_Comb_length=100,  # (Fixed)

        ## Master Inv3 : Clock driver
        ## Inv3 common

        ## Inv3 NMOS
        _SARLogic_Mst_Inv3_NMOS_NumberofGate=2,
        _SARLogic_Mst_Inv3_NMOS_ChannelWidth=400,
        _SARLogic_Mst_Inv3_NMOS_ChannelLength=30,
        _SARLogic_Mst_Inv3_NMOS_XVT='SLVT',
        _SARLogic_Mst_Inv3_NMOS_POGate_Comb_length=100,  # (Fixed)

        ## Inv3 PMOS
        _SARLogic_Mst_Inv3_PMOS_NumberofGate=2,
        _SARLogic_Mst_Inv3_PMOS_ChannelWidth=800,
        _SARLogic_Mst_Inv3_PMOS_ChannelLength=30,
        _SARLogic_Mst_Inv3_PMOS_XVT='SLVT',
        _SARLogic_Mst_Inv3_PMOS_POGate_Comb_length=100,  # (Fixed)

        ## Slave Xgate1
        ## Xgate common

        ## Xgate NMOS
        _SARLogic_Slv_Xgate1_NMOS_NumberofGate=3,
        _SARLogic_Slv_Xgate1_NMOS_ChannelWidth=400,
        _SARLogic_Slv_Xgate1_NMOS_ChannelLength=30,
        _SARLogic_Slv_Xgate1_NMOS_XVT='SLVT',
        _SARLogic_Slv_Xgate1_NMOS_POGate_Comb_length=100,  # (Fixed)

        ## Xgate PMOS
        _SARLogic_Slv_Xgate1_PMOS_NumberofGate=3,
        _SARLogic_Slv_Xgate1_PMOS_ChannelWidth=800,
        _SARLogic_Slv_Xgate1_PMOS_ChannelLength=30,
        _SARLogic_Slv_Xgate1_PMOS_XVT='SLVT',
        _SARLogic_Slv_Xgate1_PMOS_POGate_Comb_length=100,  # (Fixed)

        ## Slave Xgate2
        ## Xgate common

        ## Xgate NMOS
        _SARLogic_Slv_Xgate2_NMOS_NumberofGate=2,
        _SARLogic_Slv_Xgate2_NMOS_ChannelWidth=400,
        _SARLogic_Slv_Xgate2_NMOS_ChannelLength=30,
        _SARLogic_Slv_Xgate2_NMOS_XVT='SLVT',
        _SARLogic_Slv_Xgate2_NMOS_POGate_Comb_length=100,  # (Fixed)

        ## Xgate PMOS
        _SARLogic_Slv_Xgate2_PMOS_NumberofGate=2,
        _SARLogic_Slv_Xgate2_PMOS_ChannelWidth=800,
        _SARLogic_Slv_Xgate2_PMOS_ChannelLength=30,
        _SARLogic_Slv_Xgate2_PMOS_XVT='SLVT',
        _SARLogic_Slv_Xgate2_PMOS_POGate_Comb_length=100,  # (Fixed)

        ## Slave Nor1
        ## Nor1 common

        ## NMOS
        ## NMOS common
        _SARLogic_Slv_Nor1_NMOS_XVT='SLVT',

        ## NMOSA
        _SARLogic_Slv_Nor1_NMOSA_NumberofGate=6,
        _SARLogic_Slv_Nor1_NMOSA_ChannelWidth=400,
        _SARLogic_Slv_Nor1_NMOSA_ChannelLength=30,
        _SARLogic_Slv_Nor1_NMOSA_POGate_Comb_length=100,  # (Fixed)

        ## NMOSB
        _SARLogic_Slv_Nor1_NMOSB_NumberofGate=6,
        _SARLogic_Slv_Nor1_NMOSB_ChannelWidth=400,
        _SARLogic_Slv_Nor1_NMOSB_ChannelLength=30,
        _SARLogic_Slv_Nor1_NMOSB_POGate_Comb_length=100,  # (Fixed)

        ## PMOS
        ## PMOS common
        _SARLogic_Slv_Nor1_PMOS_XVT='SLVT',

        ## PMOSA
        _SARLogic_Slv_Nor1_PMOSA_NumberofGate=12,
        _SARLogic_Slv_Nor1_PMOSA_ChannelWidth=800,
        _SARLogic_Slv_Nor1_PMOSA_ChannelLength=30,
        _SARLogic_Slv_Nor1_PMOSA_POGate_Comb_length=100,  # (Fixed)

        ## PMOSB
        _SARLogic_Slv_Nor1_PMOSB_NumberofGate=12,
        _SARLogic_Slv_Nor1_PMOSB_ChannelWidth=800,
        _SARLogic_Slv_Nor1_PMOSB_ChannelLength=30,
        _SARLogic_Slv_Nor1_PMOSB_POGate_Comb_length=100,  # (Fixed)

        ## Slave Nor2
        ## Nor2 common

        ## NMOS
        ## NMOS common
        _SARLogic_Slv_Nor2_NMOS_XVT='SLVT',

        ## NMOSA
        _SARLogic_Slv_Nor2_NMOSA_NumberofGate=2,
        _SARLogic_Slv_Nor2_NMOSA_ChannelWidth=400,
        _SARLogic_Slv_Nor2_NMOSA_ChannelLength=30,
        _SARLogic_Slv_Nor2_NMOSA_POGate_Comb_length=100,  # (Fixed)

        ## NMOSB
        _SARLogic_Slv_Nor2_NMOSB_NumberofGate=2,
        _SARLogic_Slv_Nor2_NMOSB_ChannelWidth=400,
        _SARLogic_Slv_Nor2_NMOSB_ChannelLength=30,
        _SARLogic_Slv_Nor2_NMOSB_POGate_Comb_length=100,  # (Fixed)

        ## PMOS
        ## PMOS common
        _SARLogic_Slv_Nor2_PMOS_XVT='SLVT',

        ## PMOSA
        _SARLogic_Slv_Nor2_PMOSA_NumberofGate=4,
        _SARLogic_Slv_Nor2_PMOSA_ChannelWidth=800,
        _SARLogic_Slv_Nor2_PMOSA_ChannelLength=30,
        _SARLogic_Slv_Nor2_PMOSA_POGate_Comb_length=100,  # (Fixed)

        ## PMOSB
        _SARLogic_Slv_Nor2_PMOSB_NumberofGate=4,
        _SARLogic_Slv_Nor2_PMOSB_ChannelWidth=800,
        _SARLogic_Slv_Nor2_PMOSB_ChannelLength=30,
        _SARLogic_Slv_Nor2_PMOSB_POGate_Comb_length=100,  # (Fixed)

        ## Slave Inv1 : ReSet pre-driver
        ## Inv1 common

        ## Inv1 NMOS
        _SARLogic_Slv_Inv1_NMOS_NumberofGate=1,
        _SARLogic_Slv_Inv1_NMOS_ChannelWidth=400,
        _SARLogic_Slv_Inv1_NMOS_ChannelLength=30,
        _SARLogic_Slv_Inv1_NMOS_XVT='SLVT',
        _SARLogic_Slv_Inv1_NMOS_POGate_Comb_length=100,  # (Fixed)

        ## Inv1 PMOS
        _SARLogic_Slv_Inv1_PMOS_NumberofGate=1,
        _SARLogic_Slv_Inv1_PMOS_ChannelWidth=800,
        _SARLogic_Slv_Inv1_PMOS_ChannelLength=30,
        _SARLogic_Slv_Inv1_PMOS_XVT='SLVT',
        _SARLogic_Slv_Inv1_PMOS_POGate_Comb_length=100,  # (Fixed)

        ## Slave Inv2 : ReSet driver
        ## Inv2 common

        ## Inv2 NMOS
        _SARLogic_Slv_Inv2_NMOS_NumberofGate=2,
        _SARLogic_Slv_Inv2_NMOS_ChannelWidth=400,
        _SARLogic_Slv_Inv2_NMOS_ChannelLength=30,
        _SARLogic_Slv_Inv2_NMOS_XVT='SLVT',
        _SARLogic_Slv_Inv2_NMOS_POGate_Comb_length=100,  # (Fixed)

        ## Inv2 PMOS
        _SARLogic_Slv_Inv2_PMOS_NumberofGate=2,
        _SARLogic_Slv_Inv2_PMOS_ChannelWidth=800,
        _SARLogic_Slv_Inv2_PMOS_ChannelLength=30,
        _SARLogic_Slv_Inv2_PMOS_XVT='SLVT',
        _SARLogic_Slv_Inv2_PMOS_POGate_Comb_length=100,  # (Fixed)

        ## Slave Inv3 : Qb driver
        ## Inv3 common

        ## Inv3 NMOS
        _SARLogic_Slv_Inv3_NMOS_NumberofGate=4,
        _SARLogic_Slv_Inv3_NMOS_ChannelWidth=400,
        _SARLogic_Slv_Inv3_NMOS_ChannelLength=30,
        _SARLogic_Slv_Inv3_NMOS_XVT='SLVT',
        _SARLogic_Slv_Inv3_NMOS_POGate_Comb_length=100,  # (Fixed)

        ## Inv3 PMOS
        _SARLogic_Slv_Inv3_PMOS_NumberofGate=4,
        _SARLogic_Slv_Inv3_PMOS_ChannelWidth=800,
        _SARLogic_Slv_Inv3_PMOS_ChannelLength=30,
        _SARLogic_Slv_Inv3_PMOS_XVT='SLVT',
        _SARLogic_Slv_Inv3_PMOS_POGate_Comb_length=100,  # (Fixed)

        # Top Clock  Tree Size
        _SARLogic_CLKBufTreeTop_NumOfStage=4,
        _SARLogic_CLKBufTreeTop_CLKSampBuf_SizeByStage=[1, 2, 4, 8],
        _SARLogic_CLKBufTreeTop_CLKSrcBuf_SizeByStage=[1, 2, 4, 8],  # 스테이지에 따른 버퍼 사이즈(UnitBuffer의 배수로 각 스테이지의 크기가 결정 됨.)
        _SARLogic_CLKBufTreeTop_XOffSet=0,  # (8Bit DRC check:-79, 10Bit DRC Check:0, 12Bit:)

        ## Top CLK Buffer Tree Sizeq
        _SARLogic_CLKBufTreeTop_Inv_NMOS_ChannelWidth=400,  # Number
        _SARLogic_CLKBufTreeTop_Inv_NMOS_ChannelLength=30,  # Number
        _SARLogic_CLKBufTreeTop_Inv_NMOS_NumberofGate=1,  # Number
        _SARLogic_CLKBufTreeTop_Inv_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _SARLogic_CLKBufTreeTop_Inv_NMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

        _SARLogic_CLKBufTreeTop_Inv_PMOS_ChannelWidth=800,  # Number
        _SARLogic_CLKBufTreeTop_Inv_PMOS_ChannelLength=30,  # Number
        _SARLogic_CLKBufTreeTop_Inv_PMOS_NumberofGate=1,  # Number
        _SARLogic_CLKBufTreeTop_Inv_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _SARLogic_CLKBufTreeTop_Inv_PMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

        # Top CLK BufferPowerRail Size
        _SARLogic_CLKBufTreeTop_NMOS_Pbody_NumCont=2,  # (Fixed)
        _SARLogic_CLKBufTreeTop_NMOS_Pbody_XvtTop2Pbody=None,  # (Fixed)
        _SARLogic_CLKBufTreeTop_PMOS_Nbody_NumCont=2,  # (Fixed)
        _SARLogic_CLKBufTreeTop_PMOS_Nbody_Xvtdown2Nbody=None,  # (Fixed)
        _SARLogic_CLKBufTreeTop_PMOSXvt2NMOSXvt=444,  # (Fixed)

        # Bottom Clock  Tree Size
        _SARLogic_CLKBufTreeBot_NumOfStage=4,
        _SARLogic_CLKBufTreeBot_CompOutBuf_SizeByStage=[1, 2, 4, 8],
        _SARLogic_CLKBufTreeBot_CLKDoutBuf_SizeByStage=[1, 2, 4, 8],
        # 스테이지에 따른 버퍼 사이즈(UnitBuffer의 배수로 각 스테이지의 크기가 결정 됨.)
        _SARLogic_CLKBufTreeBot_XOffSet=0,  # (DRC check)

        ## Bottom CLK Buffer Tree Size
        _SARLogic_CLKBufTreeBot_Inv_NMOS_ChannelWidth=400,  # Number
        _SARLogic_CLKBufTreeBot_Inv_NMOS_ChannelLength=30,  # Number
        _SARLogic_CLKBufTreeBot_Inv_NMOS_NumberofGate=1,  # Number
        _SARLogic_CLKBufTreeBot_Inv_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _SARLogic_CLKBufTreeBot_Inv_NMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

        _SARLogic_CLKBufTreeBot_Inv_PMOS_ChannelWidth=800,  # Number
        _SARLogic_CLKBufTreeBot_Inv_PMOS_ChannelLength=30,  # Number
        _SARLogic_CLKBufTreeBot_Inv_PMOS_NumberofGate=1,  # Number
        _SARLogic_CLKBufTreeBot_Inv_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _SARLogic_CLKBufTreeBot_Inv_PMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

        # Bottom CLK Buffer PowerRail Size
        _SARLogic_CLKBufTreeBot_NMOS_Pbody_NumCont=2,  # (Fixed)
        _SARLogic_CLKBufTreeBot_NMOS_Pbody_XvtTop2Pbody=None,  # (Fixed)
        _SARLogic_CLKBufTreeBot_PMOS_Nbody_NumCont=2,  # (Fixed)
        _SARLogic_CLKBufTreeBot_PMOS_Nbody_Xvtdown2Nbody=None,  # (Fixed)
        _SARLogic_CLKBufTreeBot_PMOSXvt2NMOSXvt=444,  # (Fixed)

        #### CDAC Pre-Driver Sizing
        ## InvChain Common
        _CDACPreDriver_Pbody_NumCont=2,  # number #(Fixed)
        _CDACPreDriver_Nbody_NumCont=2,  # number #(Fixed)
        _CDACPreDriver_PMOSXvt2NMOSXvt=500,  # number #(Fixed)
        _CDACPreDriver_XvtTop2Pbody=None,  # number/None(Minimum) #(Fixed)
        _CDACPreDriver_Xvtdown2Nbody=None,  # number/None(Minimum) #(Fixed)

        ## Inverter Chain
        ## Inv1 common
        _CDACPreDriver_NumberofGate=[16, 64],  # Vector
        _CDACPreDriver_ChannelLength=30,  # Scalar
        _CDACPreDriver_XVT='SLVT',  # 'SLVT'

        ## Inv1 NMOS
        _CDACPreDriver_Inv_NMOS_ChannelWidth=400,  # Scalar
        _CDACPreDriver_Inv_NMOS_POGate_Comb_length=100,  # Scalar #(Fixed)

        ## Inv1 PMOS
        _CDACPreDriver_Inv_PMOS_ChannelWidth=800,  # Scalar
        _CDACPreDriver_Inv_PMOS_POGate_Comb_length=100,  # Scalar

        ## CLKDout(OutSamp) Inverter & AND Common Option
        _CLKDout_XVT_Common='SLVT',

        ## CLKDout(OutSamp) Inverter Size
        _CLKDout_Inv_NMOS_ChannelWidth=400,
        # Number (== _CLKDout_AND_NAND_NMOS_ChannelWidth,_CLKDout_AND_Inv_NMOS_ChannelWidth)
        _CLKDout_Inv_NMOS_ChannelLength=30,  # Number
        _CLKDout_Inv_NMOS_NumberofGate=1,  # Number
        _CLKDout_Inv_NMOS_POGate_Comb_length=100,  # None/Number

        _CLKDout_Inv_PMOS_ChannelWidth=800,
        # Number (== _CLKDout_AND_NAND_PMOS_ChannelWidth ,_CLKDout_AND_Inv_PMOS_ChannelWidth )
        _CLKDout_Inv_PMOS_ChannelLength=30,  # Number
        _CLKDout_Inv_PMOS_NumberofGate=1,  # Number
        _CLKDout_Inv_PMOS_POGate_Comb_length=100,  # None/Number

        ## CLKDout(OutSamp) AND Size
        _CLKDout_AND_NAND_NMOS_ChannelWidth=400,
        _CLKDout_AND_NAND_NMOS_ChannelLength=30,
        _CLKDout_AND_NAND_NMOS_NumberofGate=2,

        _CLKDout_AND_NAND_PMOS_ChannelWidth=800,
        _CLKDout_AND_NAND_PMOS_ChannelLength=30,
        _CLKDout_AND_NAND_PMOS_NumberofGate=1,

        _CLKDout_AND_Inv_NMOS_ChannelWidth=400,
        _CLKDout_AND_Inv_NMOS_ChannelLength=30,
        _CLKDout_AND_Inv_NMOS_NumberofGate=4,
        _CLKDout_AND_Inv_NMOS_POGate_Comb_length=100,

        _CLKDout_AND_Inv_PMOS_ChannelWidth=800,
        _CLKDout_AND_Inv_PMOS_ChannelLength=30,
        _CLKDout_AND_Inv_PMOS_NumberofGate=4,
        _CLKDout_AND_Inv_PMOS_POGate_Comb_length=100,

        ## StrongARM Latch
        _Comp_SALatch_CLKinputPMOSFinger1=2,  # random.randint(1, 15),  # 6
        _Comp_SALatch_CLKinputPMOSFinger2=2,  # random.randint(1, 15),  # 3
        _Comp_SALatch_PMOSFinger=4,  # random.randint(1, 15),  # 3
        _Comp_SALatch_PMOSChannelWidth=1000,  # random.randrange(200, 1050, 2),  # 500
        _Comp_SALatch_DATAinputNMOSFinger=15,  # random.randint(3, 15),  # 12
        _Comp_SALatch_NMOSFinger=5,  # random.randint(1, 15),  # 2
        _Comp_SALatch_CLKinputNMOSFinger=5,  # random.randint(1, 15),  # 8
        _Comp_SALatch_NMOSChannelWidth=1000,  # random.randrange(200, 1050, 2),  # 500
        _Comp_SALatch_CLKinputNMOSChannelWidth=1000,  # random.randrange(200, 1050, 2),  # 800
        _Comp_SALatch_ChannelLength=30,  # random.randrange(30, 60, 2),  # 30
        _Comp_SALatch_Dummy=True,  # (Fixed)
        _Comp_SALatch_XVT='LVT',
        _Comp_SALatch_GuardringWidth=200,  # (Fixed)
        _Comp_SALatch_Guardring=True,  # (Fixed)
        _Comp_SALatch_SlicerGuardringWidth=200,  # (Fixed)
        _Comp_SALatch_SlicerGuardring=None,  # (Fixed)
        _Comp_SALatch_NumSupplyCOY=None,  # (Fixed)
        _Comp_SALatch_NumSupplyCOX=None,  # (Fixed)
        _Comp_SALatch_SupplyMet1XWidth=None,  # (Fixed)
        _Comp_SALatch_SupplyMet1YWidth=None,  # (Fixed)
        _Comp_SALatch_VDD2VSSHeight=None,  # (Fixed)
        _Comp_SALatch_NumVIAPoly2Met1COX=None,  # (Fixed)
        _Comp_SALatch_NumVIAPoly2Met1COY=None,  # (Fixed)
        _Comp_SALatch_NumVIAMet12COX=None,  # (Fixed)
        _Comp_SALatch_NumVIAMet12COY=None,  # (Fixed)
        _Comp_SALatch_PowerLine=False,  # (Fixed)

        ## StrongARMLatch Output Buffer Sizing
        # Inverter1
        _Comp_SAOutBuf_Inv1_NMOS_ChannelWidth=1000,  # Number
        _Comp_SAOutBuf_Inv1_NMOS_ChannelLength=30,  # Number
        _Comp_SAOutBuf_Inv1_NMOS_NumberofGate=5,  # Number
        _Comp_SAOutBuf_Inv1_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_SAOutBuf_Inv1_NMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

        _Comp_SAOutBuf_Inv1_PMOS_ChannelWidth=2000,  # Number
        _Comp_SAOutBuf_Inv1_PMOS_ChannelLength=30,  # Number
        _Comp_SAOutBuf_Inv1_PMOS_NumberofGate=5,  # Number
        _Comp_SAOutBuf_Inv1_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_SAOutBuf_Inv1_PMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

        # Inverter2
        _Comp_SAOutBuf_Inv2_NMOS_ChannelWidth=1000,  # Number
        _Comp_SAOutBuf_Inv2_NMOS_ChannelLength=30,  # Number
        _Comp_SAOutBuf_Inv2_NMOS_NumberofGate=1,  # Number
        _Comp_SAOutBuf_Inv2_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_SAOutBuf_Inv2_NMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

        _Comp_SAOutBuf_Inv2_PMOS_ChannelWidth=2000,  # Number
        _Comp_SAOutBuf_Inv2_PMOS_ChannelLength=30,  # Number
        _Comp_SAOutBuf_Inv2_PMOS_NumberofGate=1,  # Number
        _Comp_SAOutBuf_Inv2_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_SAOutBuf_Inv2_PMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

        ## SR Latch Size
        _Comp_SRLatch_NAND_NMOS_ChannelWidth=1000,  # Number
        _Comp_SRLatch_NAND_NMOS_ChannelLength=30,  # Number
        _Comp_SRLatch_NAND_NMOS_NumberofGate=2,  # Number
        _Comp_SRLatch_NAND_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_SRLatch_NAND_NMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

        _Comp_SRLatch_NAND_PMOS_ChannelWidth=2000,  # Number
        _Comp_SRLatch_NAND_PMOS_ChannelLength=30,  # Number
        _Comp_SRLatch_NAND_PMOS_NumberofGate=1,  # Number
        _Comp_SRLatch_NAND_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_SRLatch_NAND_PMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

        # CLK Input Logic Gates
        _Comp_CLKSamp_Inv_NMOS_ChannelWidth=400,
        _Comp_CLKSamp_Inv_NMOS_ChannelLength=30,
        _Comp_CLKSamp_Inv_NMOS_NumberofGate=1,
        _Comp_CLKSamp_Inv_NMOS_XVT='SLVT',
        _Comp_CLKSamp_Inv_NMOS_POGate_Comb_length=100,  # (Fixed)

        _Comp_CLKSamp_Inv_PMOS_ChannelWidth=800,
        _Comp_CLKSamp_Inv_PMOS_ChannelLength=30,
        _Comp_CLKSamp_Inv_PMOS_NumberofGate=1,
        _Comp_CLKSamp_Inv_PMOS_XVT='SLVT',
        _Comp_CLKSamp_Inv_PMOS_POGate_Comb_length=100,  # (Fixed)

        _Comp_CLKSrc_Inv_NMOS_ChannelWidth=400,
        _Comp_CLKSrc_Inv_NMOS_ChannelLength=30,
        _Comp_CLKSrc_Inv_NMOS_NumberofGate=1,
        _Comp_CLKSrc_Inv_NMOS_XVT='SLVT',
        _Comp_CLKSrc_Inv_NMOS_POGate_Comb_length=100,  # (Fixed)

        _Comp_CLKSrc_Inv_PMOS_ChannelWidth=800,
        _Comp_CLKSrc_Inv_PMOS_ChannelLength=30,
        _Comp_CLKSrc_Inv_PMOS_NumberofGate=1,
        _Comp_CLKSrc_Inv_PMOS_XVT='SLVT',
        _Comp_CLKSrc_Inv_PMOS_POGate_Comb_length=100,  # (Fixed)

        ## CLKSrc & CLKSample AND Gate
        _Comp_AND_NAND_NMOS_ChannelWidth=400,
        _Comp_AND_NAND_NMOS_ChannelLength=30,
        _Comp_AND_NAND_NMOS_NumberofGate=2,
        _Comp_AND_NAND_NMOS_XVT='SLVT',

        _Comp_AND_NAND_PMOS_ChannelWidth=800,
        _Comp_AND_NAND_PMOS_ChannelLength=30,
        _Comp_AND_NAND_PMOS_NumberofGate=1,
        _Comp_AND_NAND_PMOS_XVT='SLVT',

        _Comp_AND_Inv_NMOS_ChannelWidth=400,
        _Comp_AND_Inv_NMOS_ChannelLength=30,
        _Comp_AND_Inv_NMOS_NumberofGate=1,
        _Comp_AND_Inv_NMOS_XVT='SLVT',
        _Comp_AND_Inv_NMOS_POGate_Comb_length=100,  # (Fixed)

        _Comp_AND_Inv_PMOS_ChannelWidth=800,
        _Comp_AND_Inv_PMOS_ChannelLength=30,
        _Comp_AND_Inv_PMOS_NumberofGate=1,
        _Comp_AND_Inv_PMOS_XVT='SLVT',
        _Comp_AND_Inv_PMOS_POGate_Comb_length=100,  # (Fixed)

        ## CLK Buffer
        # Inverter1
        _Comp_CLKBuf_Inv1_NMOS_ChannelWidth=400,  # Number
        _Comp_CLKBuf_Inv1_NMOS_ChannelLength=30,  # Number
        _Comp_CLKBuf_Inv1_NMOS_NumberofGate=2,  # Number
        _Comp_CLKBuf_Inv1_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_CLKBuf_Inv1_NMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

        _Comp_CLKBuf_Inv1_PMOS_ChannelWidth=800,  # Number
        _Comp_CLKBuf_Inv1_PMOS_ChannelLength=30,  # Number
        _Comp_CLKBuf_Inv1_PMOS_NumberofGate=2,  # Number
        _Comp_CLKBuf_Inv1_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_CLKBuf_Inv1_PMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

        # Inverter2
        _Comp_CLKBuf_Inv2_NMOS_ChannelWidth=400,  # Number
        _Comp_CLKBuf_Inv2_NMOS_ChannelLength=30,  # Number
        _Comp_CLKBuf_Inv2_NMOS_NumberofGate=4,  # Number
        _Comp_CLKBuf_Inv2_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_CLKBuf_Inv2_NMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

        _Comp_CLKBuf_Inv2_PMOS_ChannelWidth=800,  # Number
        _Comp_CLKBuf_Inv2_PMOS_ChannelLength=30,  # Number
        _Comp_CLKBuf_Inv2_PMOS_NumberofGate=4,  # Number
        _Comp_CLKBuf_Inv2_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_CLKBuf_Inv2_PMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

        # PowerRail Placement
        _Comp_BufSR_NMOS_Pbody_NumCont=2,  # (Fixed)
        _Comp_BufSR_NMOS_Pbody_XvtTop2Pbody=None,  # (Fixed)
        _Comp_BufSR_PMOS_Nbody_NumCont=2,  # (Fixed)
        _Comp_BufSR_PMOS_Nbody_Xvtdown2Nbody=None,  # (Fixed)
        _Comp_BufSR_PMOSXvt2NMOSXvt=1000,

        _Comp_CLKInLogic_NMOS_Pbody_Xvtdown2Pbody=None,  # (Fixed)
        _Comp_CLKInLogic_PMOS_Nbody_NumCont=2,  # (Fixed)
        _Comp_CLKInLogic_PMOS_Nbody_Xvtdown2Nbody=None,  # (Fixed)
        _Comp_CLKInLogic_PMOSXvt2NMOSXvt=1000,

        # Additional Buffer Between CLK_Sample Input of Comparator And Output of Tree Buffer
        ## InvChain Common
        _Buf_CLKSamp_Pbody_NumCont=2,  # number #(Fixed)
        _Buf_CLKSamp_Nbody_NumCont=2,  # number #(Fixed)
        _Buf_CLKSamp_PMOSXvt2NMOSXvt=500,  # number
        _Buf_CLKSamp_XvtTop2Pbody=None,  # number/None(Minimum) #(Fixed)
        _Buf_CLKSamp_Xvtdown2Nbody=None,  # number/None(Minimum) #(Fixed)

        ## Inverter Chain
        ## Inv1 common
        _Buf_CLKSamp_NumberofGate=[1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,      1, 4, 16, 32],  # Vector
        _Buf_CLKSamp_ChannelLength=30,  # Scalar
        _Buf_CLKSamp_XVT='SLVT',  # 'SLVT'

        ## Inv1 NMOS
        _Buf_CLKSamp_Inv_NMOS_ChannelWidth=400,  # Scalar
        _Buf_CLKSamp_Inv_NMOS_POGate_Comb_length=100,  # Scalar #(Fixed)

        ## Inv1 PMOS
        _Buf_CLKSamp_Inv_PMOS_ChannelWidth=800,  # Scalar
        _Buf_CLKSamp_Inv_PMOS_POGate_Comb_length=100,  # Scalar #(Fixed)

        # Additional Buffer Between CLK_Source Input of Comparator And Output of Tree Buffer
        ## InvChain Common
        _Buf_CLKSrc_Pbody_NumCont=2,  # number #(Fixed)
        _Buf_CLKSrc_Nbody_NumCont=2,  # number #(Fixed)
        _Buf_CLKSrc_PMOSXvt2NMOSXvt=500,  # number
        _Buf_CLKSrc_XvtTop2Pbody=None,  # number/None(Minimum) #(Fixed)
        _Buf_CLKSrc_Xvtdown2Nbody=None,  # number/None(Minimum) #(Fixed)

        ## Inverter Chain
        ## Inv1 common
        _Buf_CLKSrc_NumberofGate=[1, 1,   1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,     1, 4],  # Vector
        _Buf_CLKSrc_ChannelLength=30,  # Scalar
        _Buf_CLKSrc_XVT='SLVT',  # 'SLVT'

        ## Inv1 NMOS
        _Buf_CLKSrc_Inv_NMOS_ChannelWidth=400,  # Scalar
        _Buf_CLKSrc_Inv_NMOS_POGate_Comb_length=100,  # Scalar #(Fixed)

        ## Inv1 PMOS
        _Buf_CLKSrc_Inv_PMOS_ChannelWidth=800,  # Scalar
        _Buf_CLKSrc_Inv_PMOS_POGate_Comb_length=100,  # Scalar #(Fixed)

        # Additional Buffer Between Output of Comparator  And Input of Tree Buffer
        ## InvChain Common
        _Buf_CompOut_Pbody_NumCont=2,  # number #(Fixed)
        _Buf_CompOut_Nbody_NumCont=2,  # number #(Fixed)
        _Buf_CompOut_PMOSXvt2NMOSXvt=500,  # number
        _Buf_CompOut_XvtTop2Pbody=None,  # number/None(Minimum) #(Fixed)
        _Buf_CompOut_Xvtdown2Nbody=None,  # number/None(Minimum) #(Fixed)

        ## Inv1 common
        _Buf_CompOut_NumberofGate=[1, 2],  # Vector
        _Buf_CompOut_ChannelLength=30,  # Scalar
        _Buf_CompOut_XVT='SLVT',  # 'SLVT'

        ## Inv1 NMOS
        _Buf_CompOut_Inv_NMOS_ChannelWidth=400,  # Scalar
        _Buf_CompOut_Inv_NMOS_POGate_Comb_length=100,  # Scalar #(Fixed)

        ## Inv1 PMOS
        _Buf_CompOut_Inv_PMOS_ChannelWidth=800,  # Scalar
        _Buf_CompOut_Inv_PMOS_POGate_Comb_length=100,  # Scalar #(Fixed)

        # # Element CDAC
        _CDAC_LayoutOption=[5, 6],
        _CDAC_ShieldingLayer=1,  # Poly:0, M1:1, M2:2 ...
        _CDAC_MetalWidth=50,
        _CDAC_MetalLength=2920,  # (8bit size: 1414/ 10bit size: 2800/ 12bit size: 4200)
        _CDAC_MetalSpacing=50,

        # #Unit Cap
        _CDAC_NumOfElement=2,  # (매우 복잡..) Driver Common Centroid가 아니면 1// 맞으면 2

        # # Shielding & Top Connect node
        _CDAC_ConnectLength=400,
        _CDAC_ExtendLength=400,

        # # Dummy Cap Option
        _CDAC_DummyCap_TopBottomShort=None,
        # True => Top - Bottom Short, False -> Bottom = GND, None => Floating Bottom Node
        _CDAC_NumOfDummyCaps=10,  # Number of dummy cap(one side)

        # # CommonCentroid With Driving node
        _CDAC_CapArrayWDrivingNodeDistance=2000,  # DRC Rule
        _CDAC_DriveNodeDistance=279,  #
        _CDAC_YWidth_Bottom_Hrz=50,

        # Driver Sizing
        _Driver_SizeByBit=[128, 128, 128, 64, 32, 16, 8, 4, 2, 1],  # Drv.CCPlacement == False일때 사용됨.

        # Driver(Inverter) NMOS
        _Driver_NMOS_NumberofGate=1,  # number
        _Driver_NMOS_ChannelWidth=400,  # number (8bit size: 340/ 10bit size: 680/ 12bit size: 1020)
        _Driver_NMOS_Channellength=30,  # number
        _Driver_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT

        # Driver(Inverter) PMOS
        _Driver_PMOS_NumberofGate=1,  # number
        _Driver_PMOS_ChannelWidth=800,  # number (8bit size: 900/ 10bit size: 1800/ 12bit size: 2700)
        _Driver_PMOS_Channellength=30,  # number
        _Driver_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT

        #### Bootstrap Sampler
        # Tr1 and Tr2
        # Tr1
        _Samp_Tr1Tr2_Tr1_NMOSNumberofGate=10,  # number
        _Samp_Tr1Tr2_Tr1_NMOSChannelWidth=2000,  # number
        _Samp_Tr1Tr2_Tr1_NMOSChannellength=30,  # number
        _Samp_Tr1Tr2_Tr1_GateSpacing=222,  # None/number
        _Samp_Tr1Tr2_Tr1_SDWidth=None,  # None/number
        _Samp_Tr1Tr2_Tr1_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Samp_Tr1Tr2_Tr1_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _Samp_Tr1Tr2_Tr1_Source_Via_TF=False,  # True/False

        # Drain_node_ViaM1M2
        _Samp_Tr1Tr2_Tr1_Drain_Via_TF=False,  # True/False

        # POLY dummy setting
        _Samp_Tr1Tr2_Tr1_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tr1Tr2_Tr1_NMOSDummy_length=None,  # None/Value
        _Samp_Tr1Tr2_Tr1_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr2
        _Samp_Tr1Tr2_Tr2_NMOSNumberofGate=2,  # number
        _Samp_Tr1Tr2_Tr2_NMOSChannelWidth=1000,  # number
        _Samp_Tr1Tr2_Tr2_NMOSChannellength=30,  # number
        _Samp_Tr1Tr2_Tr2_GateSpacing=100,  # None/number
        _Samp_Tr1Tr2_Tr2_SDWidth=None,  # None/number
        _Samp_Tr1Tr2_Tr2_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Samp_Tr1Tr2_Tr2_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _Samp_Tr1Tr2_Tr2_Source_Via_TF=False,  # True/False

        # Drain_node_ViaM1M2
        _Samp_Tr1Tr2_Tr2_Drain_Via_TF=False,  # True/False

        # POLY dummy setting
        _Samp_Tr1Tr2_Tr2_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tr1Tr2_Tr2_NMOSDummy_length=None,  # None/Value
        _Samp_Tr1Tr2_Tr2_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Input/Output node
        # INPUT node
        _Samp_Tr1Tr2_Inputnode_Metal_layer=6,  # number
        _Samp_Tr1Tr2_Inputnode_width=600,  # number

        # OUTPUT node
        _Samp_Tr1Tr2_Outputnode_Metal_layer=6,  # number
        _Samp_Tr1Tr2_Outputnode_width=600,  # number

        # Guardring
        # Pbody: number of contact
        # Nbody
        _Samp_Tr1Tr2_NwellWidth=850,  # number

        # Tr4
        _Samp_Tr4_NMOSNumberofGate=4,  # number
        _Samp_Tr4_NMOSChannelWidth=1000,  # number
        _Samp_Tr4_NMOSChannellength=30,  # number
        _Samp_Tr4_GateSpacing=None,  # None/number
        _Samp_Tr4_SDWidth=None,  # None/number
        _Samp_Tr4_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Samp_Tr4_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _Samp_Tr4_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _Samp_Tr4_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _Samp_Tr4_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tr4_NMOSDummy_length=None,  # None/Value
        _Samp_Tr4_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr5 Tr7 Tr9
        # PMOS: Tr5
        _Samp_Tr5_PMOSNumberofGate=2,
        _Samp_Tr5_PMOSChannelWidth=1000,  # ref=1000
        _Samp_Tr5_PMOSChannellength=30,
        _Samp_Tr5_GateSpacing=100,
        _Samp_Tr5_SDWidth=None,
        _Samp_Tr5_XVT='SLVT',
        _Samp_Tr5_PCCrit=None,

        # Source_node_ViaM1M2
        _Samp_Tr5_Source_Via_TF=True,

        # Drain_node_ViaM1M2
        _Samp_Tr5_Drain_Via_TF=True,

        # POLY dummy setting
        _Samp_Tr5_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tr5_PMOSDummy_length=None,  # None/Value
        _Samp_Tr5_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # PMOS: Tr7
        _Samp_Tr7_PMOSNumberofGate=4,
        _Samp_Tr7_PMOSChannelWidth=1000,
        _Samp_Tr7_PMOSChannellength=30,
        _Samp_Tr7_GateSpacing=100,
        _Samp_Tr7_SDWidth=None,
        _Samp_Tr7_XVT='SLVT',
        _Samp_Tr7_PCCrit=None,

        # Source_node_ViaM1M2
        _Samp_Tr7_Source_Via_TF=True,

        # Drain_node_ViaM1M2
        _Samp_Tr7_Drain_Via_TF=True,

        # POLY dummy setting
        _Samp_Tr7_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tr7_PMOSDummy_length=None,  # None/Value
        _Samp_Tr7_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # PMOS: Tr9
        _Samp_Tr9_PMOSNumberofGate=2,
        _Samp_Tr9_PMOSChannelWidth=1000,  # ref = 1000
        _Samp_Tr9_PMOSChannellength=30,
        _Samp_Tr9_GateSpacing=100,
        _Samp_Tr9_SDWidth=None,
        _Samp_Tr9_XVT='SLVT',
        _Samp_Tr9_PCCrit=None,

        # Source_node_ViaM1M2
        _Samp_Tr9_Source_Via_TF=True,

        # Drain_node_ViaM1M2
        _Samp_Tr9_Drain_Via_TF=True,

        # POLY dummy setting
        _Samp_Tr9_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tr9_PMOSDummy_length=None,  # None/Value
        _Samp_Tr9_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr8
        _Samp_Tr8_NMOSNumberofGate=4,  # number (ref:4)
        _Samp_Tr8_NMOSChannelWidth=1000,  # number (ref:500)
        _Samp_Tr8_NMOSChannellength=30,  # number (ref:30)
        _Samp_Tr8_GateSpacing=None,  # None/number
        _Samp_Tr8_SDWidth=None,  # None/number
        _Samp_Tr8_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Samp_Tr8_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _Samp_Tr8_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _Samp_Tr8_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _Samp_Tr8_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tr8_NMOSDummy_length=None,  # None/Value
        _Samp_Tr8_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        ## Tr6
        _Samp_Tr6_NMOSNumberofGate=1,  # number
        _Samp_Tr6_NMOSChannelWidth=1000,  # number
        _Samp_Tr6_NMOSChannellength=30,  # number
        _Samp_Tr6_GateSpacing=None,  # None/number
        _Samp_Tr6_SDWidth=None,  # None/number
        _Samp_Tr6_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Samp_Tr6_PCCrit=True,  # None/True

        # Tr6 Source_node_ViaM1M2
        _Samp_Tr6_Source_Via_TF=False,  # True/False

        # Tr6 Drain_node_ViaM1M2
        _Samp_Tr6_Drain_Via_TF=False,  # True/False

        # Tr6 POLY dummy setting
        _Samp_Tr6_NMOSDummy=True,  # TF
        # Tr6 if _PMOSDummy == True
        _Samp_Tr6_NMOSDummy_length=None,  # None/Value
        _Samp_Tr6_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr6 Vp node
        _Samp_Tr6_Vp_node_width=280,  # Number
        _Samp_Tr6_Vp_node_metal_Layer=3,  # number

        # Tr6 Guardring
        # Pbody: number of contact
        # Nbody
        _Samp_Tr6_NwellWidth=850,  # number

        # PMOS: Tr11
        _Samp_Tr11_PMOSNumberofGate=2,
        _Samp_Tr11_PMOSChannelWidth=1000,
        _Samp_Tr11_PMOSChannellength=30,
        _Samp_Tr11_GateSpacing=None,
        _Samp_Tr11_SDWidth=None,
        _Samp_Tr11_XVT='SLVT',
        _Samp_Tr11_PCCrit=None,

        # Source_node_ViaM1M2
        _Samp_Tr11_Source_Via_TF=True,

        # Drain_node_ViaM1M2
        _Samp_Tr11_Drain_Via_TF=True,

        # POLY dummy setting
        _Samp_Tr11_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tr11_PMOSDummy_length=None,  # None/Value
        _Samp_Tr11_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Nbodyring(Guardring)
        _Samp_Tr11_Guardring_NumCont=3,  # number

        ## VddTieCell4
        # VddTieCell4 NMOS
        _Samp_Tie4N_NMOSNumberofGate=4,  # number
        _Samp_Tie4N_NMOSChannelWidth=250,  # number
        _Samp_Tie4N_NMOSChannellength=30,  # number
        _Samp_Tie4N_GateSpacing=100,  # None/number
        _Samp_Tie4N_SDWidth=None,  # None/number
        _Samp_Tie4N_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Samp_Tie4N_PCCrit=True,  # None/True

        # VddTieCell4 Source_node_ViaM1M2
        _Samp_Tie4N_Source_Via_TF=False,  # True/False

        # VddTieCell4 Drain_node_ViaM1M2
        _Samp_Tie4N_Drain_Via_TF=False,  # True/False

        # POLY dummy setting
        _Samp_Tie4N_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tie4N_NMOSDummy_length=400,  # None/Value
        _Samp_Tie4N_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # VddTieCell4 PMOS
        _Samp_Tie4P_PMOSNumberofGate=4,  # number
        _Samp_Tie4P_PMOSChannelWidth=500,  # number
        _Samp_Tie4P_PMOSChannellength=30,  # number
        _Samp_Tie4P_GateSpacing=100,  # None/number
        _Samp_Tie4P_SDWidth=None,  # None/number
        _Samp_Tie4P_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Samp_Tie4P_PCCrit=True,  # None/True

        # VddTieCell4 PMOS Source_node_ViaM1M2
        _Samp_Tie4P_Source_Via_TF=False,  # True/False

        # VddTieCell4 PMOS Drain_node_ViaM1M2
        _Samp_Tie4P_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _Samp_Tie4P_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tie4P_PMOSDummy_length=None,  # None/Value
        _Samp_Tie4P_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # VddTieCell4 Number of Body Contact
        _Samp_Tie4_NBodyCOX=15,
        _Samp_Tie4_NBodyCOY=3,
        _Samp_Tie4_PBodyCOX=15,
        _Samp_Tie4_PBodyCOY=3,

        ## VddTieCell8
        # VddTieCell8 NMOS
        _Samp_Tie8N_NMOSNumberofGate=4,  # number
        _Samp_Tie8N_NMOSChannelWidth=250,  # number
        _Samp_Tie8N_NMOSChannellength=30,  # number
        _Samp_Tie8N_GateSpacing=100,  # None/number
        _Samp_Tie8N_SDWidth=None,  # None/number
        _Samp_Tie8N_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Samp_Tie8N_PCCrit=True,  # None/True

        # VddTieCell8 Source_node_ViaM1M2
        _Samp_Tie8N_Source_Via_TF=False,  # True/False

        # VddTieCell8 Drain_node_ViaM1M2
        _Samp_Tie8N_Drain_Via_TF=False,  # True/False

        # POLY dummy setting
        _Samp_Tie8N_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tie8N_NMOSDummy_length=400,  # None/Value
        _Samp_Tie8N_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # VddTieCell8 PMOS
        _Samp_Tie8P_PMOSNumberofGate=4,  # number
        _Samp_Tie8P_PMOSChannelWidth=500,  # number
        _Samp_Tie8P_PMOSChannellength=30,  # number
        _Samp_Tie8P_GateSpacing=100,  # None/number
        _Samp_Tie8P_SDWidth=None,  # None/number
        _Samp_Tie8P_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Samp_Tie8P_PCCrit=True,  # None/True

        # VddTieCell8 PMOS Source_node_ViaM1M2
        _Samp_Tie8P_Source_Via_TF=False,  # True/False

        # VddTieCell8 PMOS Drain_node_ViaM1M2
        _Samp_Tie8P_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _Samp_Tie8P_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tie8P_PMOSDummy_length=None,  # None/Value
        _Samp_Tie8P_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # VddTieCell8 Number of Body Contact
        _Samp_Tie8_NBodyCOX=15,
        _Samp_Tie8_NBodyCOY=3,
        _Samp_Tie8_PBodyCOX=15,
        _Samp_Tie8_PBodyCOY=3,

        # Tr12
        _Samp_Tr12_NMOSNumberofGate=1,  # number
        _Samp_Tr12_NMOSChannelWidth=1000,  # number
        _Samp_Tr12_NMOSChannellength=30,  # number
        _Samp_Tr12_GateSpacing=None,  # None/number
        _Samp_Tr12_SDWidth=None,  # None/number
        _Samp_Tr12_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Samp_Tr12_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _Samp_Tr12_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _Samp_Tr12_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _Samp_Tr12_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tr12_NMOSDummy_length=None,  # None/Value
        _Samp_Tr12_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr3
        _Samp_Tr3_NMOSNumberofGate=4,  # number
        _Samp_Tr3_NMOSChannelWidth=1000,  # number
        _Samp_Tr3_NMOSChannellength=30,  # number
        _Samp_Tr3_GateSpacing=None,  # None/number
        _Samp_Tr3_SDWidth=None,  # None/number
        _Samp_Tr3_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Samp_Tr3_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _Samp_Tr3_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _Samp_Tr3_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _Samp_Tr3_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tr3_NMOSDummy_length=None,  # None/Value
        _Samp_Tr3_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr10
        _Samp_Tr10_NMOSNumberofGate=4,  # number
        _Samp_Tr10_NMOSChannelWidth=1000,  # number
        _Samp_Tr10_NMOSChannellength=30,  # number
        _Samp_Tr10_GateSpacing=None,  # None/number
        _Samp_Tr10_SDWidth=None,  # None/number
        _Samp_Tr10_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Samp_Tr10_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _Samp_Tr10_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _Samp_Tr10_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _Samp_Tr10_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Samp_Tr10_NMOSDummy_length=None,  # None/Value
        _Samp_Tr10_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr12Tr3Tr10 Guardring
        _Samp_Tr12Tr3Tr10_Guardring_NumCont=3,  # Number

        # HDVNCAP_Array
        _Samp_HDVNCAP_Length=7000,  # 22u M
        _Samp_HDVNCAP_LayoutOption=[3, 4, 5, 6],
        _Samp_HDVNCAP_NumFigPair=53,  # 9.55u M == 94개
        _Samp_HDVNCAP_Array=3,  # number: 1xnumber
        _Samp_HDVNCAP_Cbot_Ctop_metalwidth=1000,  # number
        # Total HDVNCapSize = 600fF

        ## BootStrapped Sampler CLKB Inverter
        _CLKBInv_NMOS_NumberofGate=32,
        _CLKBInv_NMOS_ChannelWidth=400,
        _CLKBInv_NMOS_ChannelLength=30,
        _CLKBInv_NMOS_XVT='SLVT',
        _CLKBInv_NMOS_POGate_Comb_length=None,

        _CLKBInv_PMOS_NumberofGate=32,
        _CLKBInv_Inv_PMOS_ChannelWidth=800,
        _CLKBInv_PMOS_ChannelLength=30,
        _CLKBInv_PMOS_XVT='SLVT',
        _CLKBInv_PMOS_POGate_Comb_length=None,

        _CLKBInv_Pbody_NumCont=2,
        _CLKBInv_XvtTop2Pbody=None,
        _CLKBInv_Nbody_NumCont=2,
        _CLKBInv_Xvtdown2Nbody=None,
        _CLKBInv_PMOSXvt2NMOSXvt=500,
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
    LayoutObj = _CDACWtSARLogic(_DesignParameter=None, _Name=cellname)
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
