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

from KJH91_Projects.Project_ADC.Layoutgen_code.K00_SARLogicWtBuffers_YJH import K00_02_SARLogicWtCDACPreDriver_YJH
from KJH91_Projects.Project_ADC.Layoutgen_code.E01_ComparatorWtLatch_YJH import E01_05_StrongArmWtSRLatch
from KJH91_Projects.Project_ADC.Layoutgen_code.J00_CDACPreDriver_InvBuffer_KJH0 import J00_01_InverterChain_KJH

# 1/12 ~

## Define Class
class _SARLogicWtComparator(StickDiagram_KJH1._StickDiagram_KJH):
    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
        _NumofBit=8,

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
                                  _NumofBit=8,

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

        _Caculation_Parameters1 = copy.deepcopy(
            K00_02_SARLogicWtCDACPreDriver_YJH._SARLogicWtCDACPreDriver._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters1['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters1['_NumofBit'] = _NumofBit
        _Caculation_Parameters1['_Test_distance'] = _Test_distance
        _Caculation_Parameters1['_Routing_width'] = _Routing_width
        _Caculation_Parameters1['_Routing_distance'] = _Routing_distance

        _Caculation_Parameters1['_YWidthOfCLKSrc'] = _SARLogic_YWidthOfCLKSrc
        _Caculation_Parameters1['_SpaceBtwCLKSrcAndCLKSamp'] = _SARLogic_SpaceBtwCLKSrcAndCLKSamp
        _Caculation_Parameters1['_YWidthOfCLKSamp'] = _SARLogic_YWidthOfCLKSamp
        _Caculation_Parameters1['_YWidthOfCompOut'] = _SARLogic_YWidthOfCompOut
        _Caculation_Parameters1['_SpaceBtwCompOutAndCLKDout'] = _SARLogic_SpaceBtwCompOutAndCLKDout
        _Caculation_Parameters1['_YWidthOfCLKDout'] = _SARLogic_YWidthOfCLKDout
        ## DFF Common
        _Caculation_Parameters1['_DFF_Pbody_NumCont'] = _SARLogic_DFF_Pbody_NumCont
        _Caculation_Parameters1['_DFF_Nbody_NumCont'] = _SARLogic_DFF_Nbody_NumCont
        _Caculation_Parameters1['_DFF_PMOSXvt2NMOSXvt'] = _SARLogic_DFF_PMOSXvt2NMOSXvt
        _Caculation_Parameters1['_DFF_XvtTop2Pbody'] = _SARLogic_DFF_XvtTop2Pbody
        _Caculation_Parameters1['_DFF_Xvtdown2Nbody'] = _SARLogic_DFF_Xvtdown2Nbody

        ## Master Xgate1
        ## Xgate NMOS
        _Caculation_Parameters1['_Mst_Xgate1_NMOS_NumberofGate'] = _SARLogic_Mst_Xgate1_NMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Xgate1_NMOS_ChannelWidth'] = _SARLogic_Mst_Xgate1_NMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Xgate1_NMOS_ChannelLength'] = _SARLogic_Mst_Xgate1_NMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Xgate1_NMOS_XVT'] = _SARLogic_Mst_Xgate1_NMOS_XVT
        _Caculation_Parameters1['_Mst_Xgate1_NMOS_POGate_Comb_length'] = _SARLogic_Mst_Xgate1_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_Mst_Xgate1_PMOS_NumberofGate'] = _SARLogic_Mst_Xgate1_PMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Xgate1_PMOS_ChannelWidth'] = _SARLogic_Mst_Xgate1_PMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Xgate1_PMOS_ChannelLength'] = _SARLogic_Mst_Xgate1_PMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Xgate1_PMOS_XVT'] = _SARLogic_Mst_Xgate1_PMOS_XVT
        _Caculation_Parameters1['_Mst_Xgate1_PMOS_POGate_Comb_length'] = _SARLogic_Mst_Xgate1_PMOS_POGate_Comb_length

        ## Master Xgate2
        ## Xgate NMOS
        _Caculation_Parameters1['_Mst_Xgate2_NMOS_NumberofGate'] = _SARLogic_Mst_Xgate2_NMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Xgate2_NMOS_ChannelWidth'] = _SARLogic_Mst_Xgate2_NMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Xgate2_NMOS_ChannelLength'] = _SARLogic_Mst_Xgate2_NMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Xgate2_NMOS_XVT'] = _SARLogic_Mst_Xgate2_NMOS_XVT
        _Caculation_Parameters1['_Mst_Xgate2_NMOS_POGate_Comb_length'] = _SARLogic_Mst_Xgate2_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_Mst_Xgate2_PMOS_NumberofGate'] = _SARLogic_Mst_Xgate2_PMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Xgate2_PMOS_ChannelWidth'] = _SARLogic_Mst_Xgate2_PMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Xgate2_PMOS_ChannelLength'] = _SARLogic_Mst_Xgate2_PMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Xgate2_PMOS_XVT'] = _SARLogic_Mst_Xgate2_PMOS_XVT
        _Caculation_Parameters1['_Mst_Xgate2_PMOS_POGate_Comb_length'] = _SARLogic_Mst_Xgate2_PMOS_POGate_Comb_length

        ## Master Nor1
        ## NMOS common
        _Caculation_Parameters1['_Mst_Nor1_NMOS_XVT'] = _SARLogic_Mst_Nor1_NMOS_XVT

        ## Nor1 NMOSA
        _Caculation_Parameters1['_Mst_Nor1_NMOSA_NumberofGate'] = _SARLogic_Mst_Nor1_NMOSA_NumberofGate
        _Caculation_Parameters1['_Mst_Nor1_NMOSA_ChannelWidth'] = _SARLogic_Mst_Nor1_NMOSA_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor1_NMOSA_ChannelLength'] = _SARLogic_Mst_Nor1_NMOSA_ChannelLength
        _Caculation_Parameters1['_Mst_Nor1_NMOSA_POGate_Comb_length'] = _SARLogic_Mst_Nor1_NMOSA_POGate_Comb_length

        ## Nor1 NMOSB
        _Caculation_Parameters1['_Mst_Nor1_NMOSB_NumberofGate'] = _SARLogic_Mst_Nor1_NMOSB_NumberofGate
        _Caculation_Parameters1['_Mst_Nor1_NMOSB_ChannelWidth'] = _SARLogic_Mst_Nor1_NMOSB_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor1_NMOSB_ChannelLength'] = _SARLogic_Mst_Nor1_NMOSB_ChannelLength
        _Caculation_Parameters1['_Mst_Nor1_NMOSB_POGate_Comb_length'] = _SARLogic_Mst_Nor1_NMOSB_POGate_Comb_length

        ## PMOS common
        _Caculation_Parameters1['_Mst_Nor1_PMOS_XVT'] = _SARLogic_Mst_Nor1_PMOS_XVT

        ## Nor1 PMOSA
        _Caculation_Parameters1['_Mst_Nor1_PMOSA_NumberofGate'] = _SARLogic_Mst_Nor1_PMOSA_NumberofGate
        _Caculation_Parameters1['_Mst_Nor1_PMOSA_ChannelWidth'] = _SARLogic_Mst_Nor1_PMOSA_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor1_PMOSA_ChannelLength'] = _SARLogic_Mst_Nor1_PMOSA_ChannelLength
        _Caculation_Parameters1['_Mst_Nor1_PMOSA_POGate_Comb_length'] = _SARLogic_Mst_Nor1_PMOSA_POGate_Comb_length

        ## Nor1 PMOSB
        _Caculation_Parameters1['_Mst_Nor1_PMOSB_NumberofGate'] = _SARLogic_Mst_Nor1_PMOSB_NumberofGate
        _Caculation_Parameters1['_Mst_Nor1_PMOSB_ChannelWidth'] = _SARLogic_Mst_Nor1_PMOSB_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor1_PMOSB_ChannelLength'] = _SARLogic_Mst_Nor1_PMOSB_ChannelLength
        _Caculation_Parameters1['_Mst_Nor1_PMOSB_POGate_Comb_length'] = _SARLogic_Mst_Nor1_PMOSB_POGate_Comb_length

        ## Master Nor2
        ## NMOS common
        _Caculation_Parameters1['_Mst_Nor2_NMOS_XVT'] = _SARLogic_Mst_Nor2_NMOS_XVT

        ## Nor2 NMOSA
        _Caculation_Parameters1['_Mst_Nor2_NMOSA_NumberofGate'] = _SARLogic_Mst_Nor2_NMOSA_NumberofGate
        _Caculation_Parameters1['_Mst_Nor2_NMOSA_ChannelWidth'] = _SARLogic_Mst_Nor2_NMOSA_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor2_NMOSA_ChannelLength'] = _SARLogic_Mst_Nor2_NMOSA_ChannelLength
        _Caculation_Parameters1['_Mst_Nor2_NMOSA_POGate_Comb_length'] = _SARLogic_Mst_Nor2_NMOSA_POGate_Comb_length

        ## Nor2 NMOSB
        _Caculation_Parameters1['_Mst_Nor2_NMOSB_NumberofGate'] = _SARLogic_Mst_Nor2_NMOSB_NumberofGate
        _Caculation_Parameters1['_Mst_Nor2_NMOSB_ChannelWidth'] = _SARLogic_Mst_Nor2_NMOSB_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor2_NMOSB_ChannelLength'] = _SARLogic_Mst_Nor2_NMOSB_ChannelLength
        _Caculation_Parameters1['_Mst_Nor2_NMOSB_POGate_Comb_length'] = _SARLogic_Mst_Nor2_NMOSB_POGate_Comb_length

        ## PMOS common
        _Caculation_Parameters1['_Mst_Nor2_PMOS_XVT'] = _SARLogic_Mst_Nor2_PMOS_XVT

        ## Nor2 PMOSA
        _Caculation_Parameters1['_Mst_Nor2_PMOSA_NumberofGate'] = _SARLogic_Mst_Nor2_PMOSA_NumberofGate
        _Caculation_Parameters1['_Mst_Nor2_PMOSA_ChannelWidth'] = _SARLogic_Mst_Nor2_PMOSA_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor2_PMOSA_ChannelLength'] = _SARLogic_Mst_Nor2_PMOSA_ChannelLength
        _Caculation_Parameters1['_Mst_Nor2_PMOSA_POGate_Comb_length'] = _SARLogic_Mst_Nor2_PMOSA_POGate_Comb_length

        ## Nor2 PMOSB
        _Caculation_Parameters1['_Mst_Nor2_PMOSB_NumberofGate'] = _SARLogic_Mst_Nor2_PMOSB_NumberofGate
        _Caculation_Parameters1['_Mst_Nor2_PMOSB_ChannelWidth'] = _SARLogic_Mst_Nor2_PMOSB_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor2_PMOSB_ChannelLength'] = _SARLogic_Mst_Nor2_PMOSB_ChannelLength
        _Caculation_Parameters1['_Mst_Nor2_PMOSB_POGate_Comb_length'] = _SARLogic_Mst_Nor2_PMOSB_POGate_Comb_length

        ## Master Inv1
        ## Xgate NMOS
        _Caculation_Parameters1['_Mst_Inv1_NMOS_NumberofGate'] = _SARLogic_Mst_Inv1_NMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Inv1_NMOS_ChannelWidth'] = _SARLogic_Mst_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Inv1_NMOS_ChannelLength'] = _SARLogic_Mst_Inv1_NMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Inv1_NMOS_XVT'] = _SARLogic_Mst_Inv1_NMOS_XVT
        _Caculation_Parameters1['_Mst_Inv1_NMOS_POGate_Comb_length'] = _SARLogic_Mst_Inv1_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_Mst_Inv1_PMOS_NumberofGate'] = _SARLogic_Mst_Inv1_PMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Inv1_PMOS_ChannelWidth'] = _SARLogic_Mst_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Inv1_PMOS_ChannelLength'] = _SARLogic_Mst_Inv1_PMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Inv1_PMOS_XVT'] = _SARLogic_Mst_Inv1_PMOS_XVT
        _Caculation_Parameters1['_Mst_Inv1_PMOS_POGate_Comb_length'] = _SARLogic_Mst_Inv1_PMOS_POGate_Comb_length

        ## Master Inv2 : Set driver
        ## Xgate NMOS
        _Caculation_Parameters1['_Mst_Inv2_NMOS_NumberofGate'] = _SARLogic_Mst_Inv2_NMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Inv2_NMOS_ChannelWidth'] = _SARLogic_Mst_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Inv2_NMOS_ChannelLength'] = _SARLogic_Mst_Inv2_NMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Inv2_NMOS_XVT'] = _SARLogic_Mst_Inv2_NMOS_XVT
        _Caculation_Parameters1['_Mst_Inv2_NMOS_POGate_Comb_length'] = _SARLogic_Mst_Inv2_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_Mst_Inv2_PMOS_NumberofGate'] = _SARLogic_Mst_Inv2_PMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Inv2_PMOS_ChannelWidth'] = _SARLogic_Mst_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Inv2_PMOS_ChannelLength'] = _SARLogic_Mst_Inv2_PMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Inv2_PMOS_XVT'] = _SARLogic_Mst_Inv2_PMOS_XVT
        _Caculation_Parameters1['_Mst_Inv2_PMOS_POGate_Comb_length'] = _SARLogic_Mst_Inv2_PMOS_POGate_Comb_length

        ## Master Inv3 : Clock driver
        ## Xgate NMOS
        _Caculation_Parameters1['_Mst_Inv3_NMOS_NumberofGate'] = _SARLogic_Mst_Inv3_NMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Inv3_NMOS_ChannelWidth'] = _SARLogic_Mst_Inv3_NMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Inv3_NMOS_ChannelLength'] = _SARLogic_Mst_Inv3_NMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Inv3_NMOS_XVT'] = _SARLogic_Mst_Inv3_NMOS_XVT
        _Caculation_Parameters1['_Mst_Inv3_NMOS_POGate_Comb_length'] = _SARLogic_Mst_Inv3_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_Mst_Inv3_PMOS_NumberofGate'] = _SARLogic_Mst_Inv3_PMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Inv3_PMOS_ChannelWidth'] = _SARLogic_Mst_Inv3_PMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Inv3_PMOS_ChannelLength'] = _SARLogic_Mst_Inv3_PMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Inv3_PMOS_XVT'] = _SARLogic_Mst_Inv3_PMOS_XVT
        _Caculation_Parameters1['_Mst_Inv3_PMOS_POGate_Comb_length'] = _SARLogic_Mst_Inv3_PMOS_POGate_Comb_length

        ## Slave Xgate1
        ## Xgate NMOS
        _Caculation_Parameters1['_Slv_Xgate1_NMOS_NumberofGate'] = _SARLogic_Slv_Xgate1_NMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Xgate1_NMOS_ChannelWidth'] = _SARLogic_Slv_Xgate1_NMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Xgate1_NMOS_ChannelLength'] = _SARLogic_Slv_Xgate1_NMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Xgate1_NMOS_XVT'] = _SARLogic_Slv_Xgate1_NMOS_XVT
        _Caculation_Parameters1['_Slv_Xgate1_NMOS_POGate_Comb_length'] = _SARLogic_Slv_Xgate1_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_Slv_Xgate1_PMOS_NumberofGate'] = _SARLogic_Slv_Xgate1_PMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Xgate1_PMOS_ChannelWidth'] = _SARLogic_Slv_Xgate1_PMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Xgate1_PMOS_ChannelLength'] = _SARLogic_Slv_Xgate1_PMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Xgate1_PMOS_XVT'] = _SARLogic_Slv_Xgate1_PMOS_XVT
        _Caculation_Parameters1['_Slv_Xgate1_PMOS_POGate_Comb_length'] = _SARLogic_Slv_Xgate1_PMOS_POGate_Comb_length

        ## Slave Xgate2
        ## Xgate NMOS
        _Caculation_Parameters1['_Slv_Xgate2_NMOS_NumberofGate'] = _SARLogic_Slv_Xgate2_NMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Xgate2_NMOS_ChannelWidth'] = _SARLogic_Slv_Xgate2_NMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Xgate2_NMOS_ChannelLength'] = _SARLogic_Slv_Xgate2_NMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Xgate2_NMOS_XVT'] = _SARLogic_Slv_Xgate2_NMOS_XVT
        _Caculation_Parameters1['_Slv_Xgate2_NMOS_POGate_Comb_length'] = _SARLogic_Slv_Xgate2_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_Slv_Xgate2_PMOS_NumberofGate'] = _SARLogic_Slv_Xgate2_PMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Xgate2_PMOS_ChannelWidth'] = _SARLogic_Slv_Xgate2_PMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Xgate2_PMOS_ChannelLength'] = _SARLogic_Slv_Xgate2_PMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Xgate2_PMOS_XVT'] = _SARLogic_Slv_Xgate2_PMOS_XVT
        _Caculation_Parameters1['_Slv_Xgate2_PMOS_POGate_Comb_length'] = _SARLogic_Slv_Xgate2_PMOS_POGate_Comb_length

        ## Slave Nor1
        ## NMOS common
        _Caculation_Parameters1['_Slv_Nor1_NMOS_XVT'] = _SARLogic_Slv_Nor1_NMOS_XVT

        ## Nor1 NMOSA
        _Caculation_Parameters1['_Slv_Nor1_NMOSA_NumberofGate'] = _SARLogic_Slv_Nor1_NMOSA_NumberofGate
        _Caculation_Parameters1['_Slv_Nor1_NMOSA_ChannelWidth'] = _SARLogic_Slv_Nor1_NMOSA_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor1_NMOSA_ChannelLength'] = _SARLogic_Slv_Nor1_NMOSA_ChannelLength
        _Caculation_Parameters1['_Slv_Nor1_NMOSA_POGate_Comb_length'] = _SARLogic_Slv_Nor1_NMOSA_POGate_Comb_length

        ## Nor1 NMOSB
        _Caculation_Parameters1['_Slv_Nor1_NMOSB_NumberofGate'] = _SARLogic_Slv_Nor1_NMOSB_NumberofGate
        _Caculation_Parameters1['_Slv_Nor1_NMOSB_ChannelWidth'] = _SARLogic_Slv_Nor1_NMOSB_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor1_NMOSB_ChannelLength'] = _SARLogic_Slv_Nor1_NMOSB_ChannelLength
        _Caculation_Parameters1['_Slv_Nor1_NMOSB_POGate_Comb_length'] = _SARLogic_Slv_Nor1_NMOSB_POGate_Comb_length

        ## PMOS common
        _Caculation_Parameters1['_Slv_Nor1_PMOS_XVT'] = _SARLogic_Slv_Nor1_PMOS_XVT

        ## Nor1 PMOSA
        _Caculation_Parameters1['_Slv_Nor1_PMOSA_NumberofGate'] = _SARLogic_Slv_Nor1_PMOSA_NumberofGate
        _Caculation_Parameters1['_Slv_Nor1_PMOSA_ChannelWidth'] = _SARLogic_Slv_Nor1_PMOSA_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor1_PMOSA_ChannelLength'] = _SARLogic_Slv_Nor1_PMOSA_ChannelLength
        _Caculation_Parameters1['_Slv_Nor1_PMOSA_POGate_Comb_length'] = _SARLogic_Slv_Nor1_PMOSA_POGate_Comb_length

        ## Nor1 PMOSB
        _Caculation_Parameters1['_Slv_Nor1_PMOSB_NumberofGate'] = _SARLogic_Slv_Nor1_PMOSB_NumberofGate
        _Caculation_Parameters1['_Slv_Nor1_PMOSB_ChannelWidth'] = _SARLogic_Slv_Nor1_PMOSB_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor1_PMOSB_ChannelLength'] = _SARLogic_Slv_Nor1_PMOSB_ChannelLength
        _Caculation_Parameters1['_Slv_Nor1_PMOSB_POGate_Comb_length'] = _SARLogic_Slv_Nor1_PMOSB_POGate_Comb_length

        ## Slave Nor2
        ## NMOS common
        _Caculation_Parameters1['_Slv_Nor2_NMOS_XVT'] = _SARLogic_Slv_Nor2_NMOS_XVT

        ## Nor2 NMOSA
        _Caculation_Parameters1['_Slv_Nor2_NMOSA_NumberofGate'] = _SARLogic_Slv_Nor2_NMOSA_NumberofGate
        _Caculation_Parameters1['_Slv_Nor2_NMOSA_ChannelWidth'] = _SARLogic_Slv_Nor2_NMOSA_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor2_NMOSA_ChannelLength'] = _SARLogic_Slv_Nor2_NMOSA_ChannelLength
        _Caculation_Parameters1['_Slv_Nor2_NMOSA_POGate_Comb_length'] = _SARLogic_Slv_Nor2_NMOSA_POGate_Comb_length

        ## Nor2 NMOSB
        _Caculation_Parameters1['_Slv_Nor2_NMOSB_NumberofGate'] = _SARLogic_Slv_Nor2_NMOSB_NumberofGate
        _Caculation_Parameters1['_Slv_Nor2_NMOSB_ChannelWidth'] = _SARLogic_Slv_Nor2_NMOSB_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor2_NMOSB_ChannelLength'] = _SARLogic_Slv_Nor2_NMOSB_ChannelLength
        _Caculation_Parameters1['_Slv_Nor2_NMOSB_POGate_Comb_length'] = _SARLogic_Slv_Nor2_NMOSB_POGate_Comb_length

        ## PMOS common
        _Caculation_Parameters1['_Slv_Nor2_PMOS_XVT'] = _SARLogic_Slv_Nor2_PMOS_XVT

        ## Nor2 PMOSA
        _Caculation_Parameters1['_Slv_Nor2_PMOSA_NumberofGate'] = _SARLogic_Slv_Nor2_PMOSA_NumberofGate
        _Caculation_Parameters1['_Slv_Nor2_PMOSA_ChannelWidth'] = _SARLogic_Slv_Nor2_PMOSA_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor2_PMOSA_ChannelLength'] = _SARLogic_Slv_Nor2_PMOSA_ChannelLength
        _Caculation_Parameters1['_Slv_Nor2_PMOSA_POGate_Comb_length'] = _SARLogic_Slv_Nor2_PMOSA_POGate_Comb_length

        ## Nor2 PMOSB
        _Caculation_Parameters1['_Slv_Nor2_PMOSB_NumberofGate'] = _SARLogic_Slv_Nor2_PMOSB_NumberofGate
        _Caculation_Parameters1['_Slv_Nor2_PMOSB_ChannelWidth'] = _SARLogic_Slv_Nor2_PMOSB_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor2_PMOSB_ChannelLength'] = _SARLogic_Slv_Nor2_PMOSB_ChannelLength
        _Caculation_Parameters1['_Slv_Nor2_PMOSB_POGate_Comb_length'] = _SARLogic_Slv_Nor2_PMOSB_POGate_Comb_length

        ## Slave Inv1 : ReSet pre-driver
        ## Xgate NMOS
        _Caculation_Parameters1['_Slv_Inv1_NMOS_NumberofGate'] = _SARLogic_Slv_Inv1_NMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Inv1_NMOS_ChannelWidth'] = _SARLogic_Slv_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Inv1_NMOS_ChannelLength'] = _SARLogic_Slv_Inv1_NMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Inv1_NMOS_XVT'] = _SARLogic_Slv_Inv1_NMOS_XVT
        _Caculation_Parameters1['_Slv_Inv1_NMOS_POGate_Comb_length'] = _SARLogic_Slv_Inv1_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_Slv_Inv1_PMOS_NumberofGate'] = _SARLogic_Slv_Inv1_PMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Inv1_PMOS_ChannelWidth'] = _SARLogic_Slv_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Inv1_PMOS_ChannelLength'] = _SARLogic_Slv_Inv1_PMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Inv1_PMOS_XVT'] = _SARLogic_Slv_Inv1_PMOS_XVT
        _Caculation_Parameters1['_Slv_Inv1_PMOS_POGate_Comb_length'] = _SARLogic_Slv_Inv1_PMOS_POGate_Comb_length

        ## Slave Inv2 : ReSet driver
        ## Xgate NMOS
        _Caculation_Parameters1['_Slv_Inv2_NMOS_NumberofGate'] = _SARLogic_Slv_Inv2_NMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Inv2_NMOS_ChannelWidth'] = _SARLogic_Slv_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Inv2_NMOS_ChannelLength'] = _SARLogic_Slv_Inv2_NMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Inv2_NMOS_XVT'] = _SARLogic_Slv_Inv2_NMOS_XVT
        _Caculation_Parameters1['_Slv_Inv2_NMOS_POGate_Comb_length'] = _SARLogic_Slv_Inv2_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_Slv_Inv2_PMOS_NumberofGate'] = _SARLogic_Slv_Inv2_PMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Inv2_PMOS_ChannelWidth'] = _SARLogic_Slv_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Inv2_PMOS_ChannelLength'] = _SARLogic_Slv_Inv2_PMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Inv2_PMOS_XVT'] = _SARLogic_Slv_Inv2_PMOS_XVT
        _Caculation_Parameters1['_Slv_Inv2_PMOS_POGate_Comb_length'] = _SARLogic_Slv_Inv2_PMOS_POGate_Comb_length

        ## Slave Inv3 : Qb driver
        ## Xgate NMOS
        _Caculation_Parameters1['_Slv_Inv3_NMOS_NumberofGate'] = _SARLogic_Slv_Inv3_NMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Inv3_NMOS_ChannelWidth'] = _SARLogic_Slv_Inv3_NMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Inv3_NMOS_ChannelLength'] = _SARLogic_Slv_Inv3_NMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Inv3_NMOS_XVT'] = _SARLogic_Slv_Inv3_NMOS_XVT
        _Caculation_Parameters1['_Slv_Inv3_NMOS_POGate_Comb_length'] = _SARLogic_Slv_Inv3_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_Slv_Inv3_PMOS_NumberofGate'] = _SARLogic_Slv_Inv3_PMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Inv3_PMOS_ChannelWidth'] = _SARLogic_Slv_Inv3_PMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Inv3_PMOS_ChannelLength'] = _SARLogic_Slv_Inv3_PMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Inv3_PMOS_XVT'] = _SARLogic_Slv_Inv3_PMOS_XVT
        _Caculation_Parameters1['_Slv_Inv3_PMOS_POGate_Comb_length'] = _SARLogic_Slv_Inv3_PMOS_POGate_Comb_length

        ## CLK Buf Tree Top
        _Caculation_Parameters1['_CLKBufTreeTop_NumOfStage'] = _SARLogic_CLKBufTreeTop_NumOfStage
        _Caculation_Parameters1['_CLKBufTreeTop_CLKSampBuf_SizeByStage'] = _SARLogic_CLKBufTreeTop_CLKSampBuf_SizeByStage
        _Caculation_Parameters1['_CLKBufTreeTop_CLKSrcBuf_SizeByStage'] = _SARLogic_CLKBufTreeTop_CLKSrcBuf_SizeByStage
        _Caculation_Parameters1['_CLKBufTreeTop_XOffSet'] = _SARLogic_CLKBufTreeTop_XOffSet

        _Caculation_Parameters1['_CLKBufTreeTop_Inv_NMOS_ChannelWidth'] = _SARLogic_CLKBufTreeTop_Inv_NMOS_ChannelWidth
        _Caculation_Parameters1['_CLKBufTreeTop_Inv_NMOS_ChannelLength'] = _SARLogic_CLKBufTreeTop_Inv_NMOS_ChannelLength
        _Caculation_Parameters1['_CLKBufTreeTop_Inv_NMOS_NumberofGate'] = _SARLogic_CLKBufTreeTop_Inv_NMOS_NumberofGate
        _Caculation_Parameters1['_CLKBufTreeTop_Inv_NMOS_XVT'] = _SARLogic_CLKBufTreeTop_Inv_NMOS_XVT
        _Caculation_Parameters1['_CLKBufTreeTop_Inv_NMOS_POGate_Comb_length'] = _SARLogic_CLKBufTreeTop_Inv_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_CLKBufTreeTop_Inv_PMOS_ChannelWidth'] = _SARLogic_CLKBufTreeTop_Inv_PMOS_ChannelWidth
        _Caculation_Parameters1['_CLKBufTreeTop_Inv_PMOS_ChannelLength'] = _SARLogic_CLKBufTreeTop_Inv_PMOS_ChannelLength
        _Caculation_Parameters1['_CLKBufTreeTop_Inv_PMOS_NumberofGate'] = _SARLogic_CLKBufTreeTop_Inv_PMOS_NumberofGate
        _Caculation_Parameters1['_CLKBufTreeTop_Inv_PMOS_XVT'] = _SARLogic_CLKBufTreeTop_Inv_PMOS_XVT
        _Caculation_Parameters1['_CLKBufTreeTop_Inv_PMOS_POGate_Comb_length'] = _SARLogic_CLKBufTreeTop_Inv_PMOS_POGate_Comb_length

        _Caculation_Parameters1['_CLKBufTreeTop_NMOS_Pbody_NumCont'] = _SARLogic_CLKBufTreeTop_NMOS_Pbody_NumCont
        _Caculation_Parameters1['_CLKBufTreeTop_NMOS_Pbody_XvtTop2Pbody'] = _SARLogic_CLKBufTreeTop_NMOS_Pbody_XvtTop2Pbody
        _Caculation_Parameters1['_CLKBufTreeTop_PMOS_Nbody_NumCont'] = _SARLogic_CLKBufTreeTop_PMOS_Nbody_NumCont
        _Caculation_Parameters1['_CLKBufTreeTop_PMOS_Nbody_Xvtdown2Nbody'] = _SARLogic_CLKBufTreeTop_PMOS_Nbody_Xvtdown2Nbody
        _Caculation_Parameters1['_CLKBufTreeTop_PMOSXvt2NMOSXvt'] = _SARLogic_CLKBufTreeTop_PMOSXvt2NMOSXvt

        ## CLK Buf Tree Bot
        _Caculation_Parameters1['_CLKBufTreeBot_NumOfStage'] = _SARLogic_CLKBufTreeBot_NumOfStage
        _Caculation_Parameters1['_CLKBufTreeBot_CompOutBuf_SizeByStage'] = _SARLogic_CLKBufTreeBot_CompOutBuf_SizeByStage
        _Caculation_Parameters1['_CLKBufTreeBot_CLKDoutBuf_SizeByStage'] = _SARLogic_CLKBufTreeBot_CLKDoutBuf_SizeByStage
        _Caculation_Parameters1['_CLKBufTreeBot_XOffSet'] = _SARLogic_CLKBufTreeBot_XOffSet

        _Caculation_Parameters1['_CLKBufTreeBot_Inv_NMOS_ChannelWidth'] = _SARLogic_CLKBufTreeBot_Inv_NMOS_ChannelWidth
        _Caculation_Parameters1['_CLKBufTreeBot_Inv_NMOS_ChannelLength'] = _SARLogic_CLKBufTreeBot_Inv_NMOS_ChannelLength
        _Caculation_Parameters1['_CLKBufTreeBot_Inv_NMOS_NumberofGate'] = _SARLogic_CLKBufTreeBot_Inv_NMOS_NumberofGate
        _Caculation_Parameters1['_CLKBufTreeBot_Inv_NMOS_XVT'] = _SARLogic_CLKBufTreeBot_Inv_NMOS_XVT
        _Caculation_Parameters1['_CLKBufTreeBot_Inv_NMOS_POGate_Comb_length'] = _SARLogic_CLKBufTreeBot_Inv_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_CLKBufTreeBot_Inv_PMOS_ChannelWidth'] = _SARLogic_CLKBufTreeBot_Inv_PMOS_ChannelWidth
        _Caculation_Parameters1['_CLKBufTreeBot_Inv_PMOS_ChannelLength'] = _SARLogic_CLKBufTreeBot_Inv_PMOS_ChannelLength
        _Caculation_Parameters1['_CLKBufTreeBot_Inv_PMOS_NumberofGate'] = _SARLogic_CLKBufTreeBot_Inv_PMOS_NumberofGate
        _Caculation_Parameters1['_CLKBufTreeBot_Inv_PMOS_XVT'] = _SARLogic_CLKBufTreeBot_Inv_PMOS_XVT
        _Caculation_Parameters1['_CLKBufTreeBot_Inv_PMOS_POGate_Comb_length'] = _SARLogic_CLKBufTreeBot_Inv_PMOS_POGate_Comb_length

        _Caculation_Parameters1['_CLKBufTreeBot_NMOS_Pbody_NumCont'] = _SARLogic_CLKBufTreeBot_NMOS_Pbody_NumCont
        _Caculation_Parameters1['_CLKBufTreeBot_NMOS_Pbody_XvtTop2Pbody'] = _SARLogic_CLKBufTreeBot_NMOS_Pbody_XvtTop2Pbody
        _Caculation_Parameters1['_CLKBufTreeBot_PMOS_Nbody_NumCont'] = _SARLogic_CLKBufTreeBot_PMOS_Nbody_NumCont
        _Caculation_Parameters1['_CLKBufTreeBot_PMOS_Nbody_Xvtdown2Nbody'] = _SARLogic_CLKBufTreeBot_PMOS_Nbody_Xvtdown2Nbody
        _Caculation_Parameters1['_CLKBufTreeBot_PMOSXvt2NMOSXvt'] = _SARLogic_CLKBufTreeBot_PMOSXvt2NMOSXvt

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

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_SARLogicWtBuffers'] = self._SrefElementDeclaration(_DesignObj=K00_02_SARLogicWtCDACPreDriver_YJH._SARLogicWtCDACPreDriver(_DesignParameter=None, _Name='{}:SRF_SARLogicWtBuffers'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_SARLogicWtBuffers']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SARLogicWtBuffers']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SARLogicWtBuffers']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters1)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SARLogicWtBuffers']['_XYCoordinates'] = [[0, 0]]

        print('###############################################')
        print('##                Comparator                 ##')
        print('##            Calculation_Start!!            ##')
        print('###############################################')

        #### Comparator With SR Latch And Clock In Logic SREF Generation
        ## StrongARM Latch
        _Caculation_Parameters1 = copy.deepcopy(
            E01_05_StrongArmWtSRLatch._StrongArmWtSRLatch._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters1['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length

        _Caculation_Parameters1['_SALatch_CLKinputPMOSFinger1'] = _Comp_SALatch_CLKinputPMOSFinger1
        _Caculation_Parameters1['_SALatch_CLKinputPMOSFinger2'] = _Comp_SALatch_CLKinputPMOSFinger2
        _Caculation_Parameters1['_SALatch_PMOSFinger'] = _Comp_SALatch_PMOSFinger
        _Caculation_Parameters1['_SALatch_PMOSChannelWidth'] = _Comp_SALatch_PMOSChannelWidth
        _Caculation_Parameters1['_SALatch_DATAinputNMOSFinger'] = _Comp_SALatch_DATAinputNMOSFinger
        _Caculation_Parameters1['_SALatch_NMOSFinger'] = _Comp_SALatch_NMOSFinger
        _Caculation_Parameters1['_SALatch_CLKinputNMOSFinger'] = _Comp_SALatch_CLKinputNMOSFinger
        _Caculation_Parameters1['_SALatch_NMOSChannelWidth'] = _Comp_SALatch_NMOSChannelWidth
        _Caculation_Parameters1['_SALatch_CLKinputNMOSChannelWidth'] = _Comp_SALatch_CLKinputNMOSChannelWidth
        _Caculation_Parameters1['_SALatch_ChannelLength'] = _Comp_SALatch_ChannelLength
        _Caculation_Parameters1['_SALatch_Dummy'] = _Comp_SALatch_Dummy
        _Caculation_Parameters1['_SALatch_XVT'] = _Comp_SALatch_XVT
        _Caculation_Parameters1['_SALatch_GuardringWidth'] = _Comp_SALatch_GuardringWidth
        _Caculation_Parameters1['_SALatch_Guardring'] = _Comp_SALatch_Guardring
        _Caculation_Parameters1['_SALatch_SlicerGuardringWidth'] = _Comp_SALatch_SlicerGuardringWidth
        _Caculation_Parameters1['_SALatch_SlicerGuardring'] = _Comp_SALatch_SlicerGuardring
        _Caculation_Parameters1['_SALatch_NumSupplyCOY'] = _Comp_SALatch_NumSupplyCOY
        _Caculation_Parameters1['_SALatch_NumSupplyCOX'] = _Comp_SALatch_NumSupplyCOX
        _Caculation_Parameters1['_SALatch_SupplyMet1XWidth'] = _Comp_SALatch_SupplyMet1XWidth
        _Caculation_Parameters1['_SALatch_SupplyMet1YWidth'] = _Comp_SALatch_SupplyMet1YWidth
        _Caculation_Parameters1['_SALatch_VDD2VSSHeight'] = _Comp_SALatch_VDD2VSSHeight
        _Caculation_Parameters1['_SALatch_NumVIAPoly2Met1COX'] = _Comp_SALatch_NumVIAPoly2Met1COX
        _Caculation_Parameters1['_SALatch_NumVIAPoly2Met1COY'] = _Comp_SALatch_NumVIAPoly2Met1COY
        _Caculation_Parameters1['_SALatch_NumVIAMet12COX'] = _Comp_SALatch_NumVIAMet12COX
        _Caculation_Parameters1['_SALatch_NumVIAMet12COY'] = _Comp_SALatch_NumVIAMet12COY
        _Caculation_Parameters1['_SALatch_PowerLine'] = _Comp_SALatch_PowerLine

        ## StrongARMLatch Output Buffer Sizing
        # Inverter1
        _Caculation_Parameters1['_SAOutBuf_Inv1_NMOS_ChannelWidth'] = _Comp_SAOutBuf_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters1['_SAOutBuf_Inv1_NMOS_ChannelLength'] = _Comp_SAOutBuf_Inv1_NMOS_ChannelLength
        _Caculation_Parameters1['_SAOutBuf_Inv1_NMOS_NumberofGate'] = _Comp_SAOutBuf_Inv1_NMOS_NumberofGate
        _Caculation_Parameters1['_SAOutBuf_Inv1_NMOS_XVT'] = _Comp_SAOutBuf_Inv1_NMOS_XVT
        _Caculation_Parameters1['_SAOutBuf_Inv1_NMOS_POGate_Comb_length'] = _Comp_SAOutBuf_Inv1_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_SAOutBuf_Inv1_PMOS_ChannelWidth'] = _Comp_SAOutBuf_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters1['_SAOutBuf_Inv1_PMOS_ChannelLength'] = _Comp_SAOutBuf_Inv1_PMOS_ChannelLength
        _Caculation_Parameters1['_SAOutBuf_Inv1_PMOS_NumberofGate'] = _Comp_SAOutBuf_Inv1_PMOS_NumberofGate
        _Caculation_Parameters1['_SAOutBuf_Inv1_PMOS_XVT'] = _Comp_SAOutBuf_Inv1_PMOS_XVT
        _Caculation_Parameters1['_SAOutBuf_Inv1_PMOS_POGate_Comb_length'] = _Comp_SAOutBuf_Inv1_PMOS_POGate_Comb_length

        # Inverter2
        _Caculation_Parameters1['_SAOutBuf_Inv2_NMOS_ChannelWidth'] = _Comp_SAOutBuf_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters1['_SAOutBuf_Inv2_NMOS_ChannelLength'] = _Comp_SAOutBuf_Inv2_NMOS_ChannelLength
        _Caculation_Parameters1['_SAOutBuf_Inv2_NMOS_NumberofGate'] = _Comp_SAOutBuf_Inv2_NMOS_NumberofGate
        _Caculation_Parameters1['_SAOutBuf_Inv2_NMOS_XVT'] = _Comp_SAOutBuf_Inv2_NMOS_XVT
        _Caculation_Parameters1['_SAOutBuf_Inv2_NMOS_POGate_Comb_length'] = _Comp_SAOutBuf_Inv2_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_SAOutBuf_Inv2_PMOS_ChannelWidth'] = _Comp_SAOutBuf_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters1['_SAOutBuf_Inv2_PMOS_ChannelLength'] = _Comp_SAOutBuf_Inv2_PMOS_ChannelLength
        _Caculation_Parameters1['_SAOutBuf_Inv2_PMOS_NumberofGate'] = _Comp_SAOutBuf_Inv2_PMOS_NumberofGate
        _Caculation_Parameters1['_SAOutBuf_Inv2_PMOS_XVT'] = _Comp_SAOutBuf_Inv2_PMOS_XVT
        _Caculation_Parameters1['_SAOutBuf_Inv2_PMOS_POGate_Comb_length'] = _Comp_SAOutBuf_Inv2_PMOS_POGate_Comb_length

        ## SR Latch Sizing
        _Caculation_Parameters1['_SRLatch_NAND_NMOS_ChannelWidth'] = _Comp_SRLatch_NAND_NMOS_ChannelWidth
        _Caculation_Parameters1['_SRLatch_NAND_NMOS_ChannelLength'] = _Comp_SRLatch_NAND_NMOS_ChannelLength
        _Caculation_Parameters1['_SRLatch_NAND_NMOS_NumberofGate'] = _Comp_SRLatch_NAND_NMOS_NumberofGate
        _Caculation_Parameters1['_SRLatch_NAND_NMOS_XVT'] = _Comp_SRLatch_NAND_NMOS_XVT
        _Caculation_Parameters1['_SRLatch_NAND_NMOS_POGate_Comb_length'] = _Comp_SRLatch_NAND_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_SRLatch_NAND_PMOS_ChannelWidth'] = _Comp_SRLatch_NAND_PMOS_ChannelWidth
        _Caculation_Parameters1['_SRLatch_NAND_PMOS_ChannelLength'] = _Comp_SRLatch_NAND_PMOS_ChannelLength
        _Caculation_Parameters1['_SRLatch_NAND_PMOS_NumberofGate'] = _Comp_SRLatch_NAND_PMOS_NumberofGate
        _Caculation_Parameters1['_SRLatch_NAND_PMOS_XVT'] = _Comp_SRLatch_NAND_PMOS_XVT
        _Caculation_Parameters1['_SRLatch_NAND_PMOS_POGate_Comb_length'] = _Comp_SRLatch_NAND_PMOS_POGate_Comb_length

        # CLK Input Logic Gates
        _Caculation_Parameters1['_CLKSamp_Inv_NMOS_ChannelWidth'] = _Comp_CLKSamp_Inv_NMOS_ChannelWidth
        _Caculation_Parameters1['_CLKSamp_Inv_NMOS_ChannelLength'] = _Comp_CLKSamp_Inv_NMOS_ChannelLength
        _Caculation_Parameters1['_CLKSamp_Inv_NMOS_NumberofGate'] = _Comp_CLKSamp_Inv_NMOS_NumberofGate
        _Caculation_Parameters1['_CLKSamp_Inv_NMOS_XVT'] = _Comp_CLKSamp_Inv_NMOS_XVT
        _Caculation_Parameters1['_CLKSamp_Inv_NMOS_POGate_Comb_length'] = _Comp_CLKSamp_Inv_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_CLKSamp_Inv_PMOS_ChannelWidth'] = _Comp_CLKSamp_Inv_PMOS_ChannelWidth
        _Caculation_Parameters1['_CLKSamp_Inv_PMOS_ChannelLength'] = _Comp_CLKSamp_Inv_PMOS_ChannelLength
        _Caculation_Parameters1['_CLKSamp_Inv_PMOS_NumberofGate'] = _Comp_CLKSamp_Inv_PMOS_NumberofGate
        _Caculation_Parameters1['_CLKSamp_Inv_PMOS_XVT'] = _Comp_CLKSamp_Inv_PMOS_XVT
        _Caculation_Parameters1['_CLKSamp_Inv_PMOS_POGate_Comb_length'] = _Comp_CLKSamp_Inv_PMOS_POGate_Comb_length

        _Caculation_Parameters1['_CLKSrc_Inv_NMOS_ChannelWidth'] = _Comp_CLKSrc_Inv_NMOS_ChannelWidth
        _Caculation_Parameters1['_CLKSrc_Inv_NMOS_ChannelLength'] = _Comp_CLKSrc_Inv_NMOS_ChannelLength
        _Caculation_Parameters1['_CLKSrc_Inv_NMOS_NumberofGate'] = _Comp_CLKSrc_Inv_NMOS_NumberofGate
        _Caculation_Parameters1['_CLKSrc_Inv_NMOS_XVT'] = _Comp_CLKSrc_Inv_NMOS_XVT
        _Caculation_Parameters1['_CLKSrc_Inv_NMOS_POGate_Comb_length'] = _Comp_CLKSrc_Inv_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_CLKSrc_Inv_PMOS_ChannelWidth'] = _Comp_CLKSrc_Inv_PMOS_ChannelWidth
        _Caculation_Parameters1['_CLKSrc_Inv_PMOS_ChannelLength'] = _Comp_CLKSrc_Inv_PMOS_ChannelLength
        _Caculation_Parameters1['_CLKSrc_Inv_PMOS_NumberofGate'] = _Comp_CLKSrc_Inv_PMOS_NumberofGate
        _Caculation_Parameters1['_CLKSrc_Inv_PMOS_XVT'] = _Comp_CLKSrc_Inv_PMOS_XVT
        _Caculation_Parameters1['_CLKSrc_Inv_PMOS_POGate_Comb_length'] = _Comp_CLKSrc_Inv_PMOS_POGate_Comb_length

        ## CLKSrc & CLKSample AND Gate
        _Caculation_Parameters1['_AND_NAND_NMOS_ChannelWidth'] = _Comp_AND_NAND_NMOS_ChannelWidth
        _Caculation_Parameters1['_AND_NAND_NMOS_ChannelLength'] = _Comp_AND_NAND_NMOS_ChannelLength
        _Caculation_Parameters1['_AND_NAND_NMOS_NumberofGate'] = _Comp_AND_NAND_NMOS_NumberofGate
        _Caculation_Parameters1['_AND_NAND_NMOS_XVT'] = _Comp_AND_NAND_NMOS_XVT

        _Caculation_Parameters1['_AND_NAND_PMOS_ChannelWidth'] = _Comp_AND_NAND_PMOS_ChannelWidth
        _Caculation_Parameters1['_AND_NAND_PMOS_ChannelLength'] = _Comp_AND_NAND_PMOS_ChannelLength
        _Caculation_Parameters1['_AND_NAND_PMOS_NumberofGate'] = _Comp_AND_NAND_PMOS_NumberofGate
        _Caculation_Parameters1['_AND_NAND_PMOS_XVT'] = _Comp_AND_NAND_PMOS_XVT

        _Caculation_Parameters1['_AND_Inv_NMOS_ChannelWidth'] = _Comp_AND_Inv_NMOS_ChannelWidth
        _Caculation_Parameters1['_AND_Inv_NMOS_ChannelLength'] = _Comp_AND_Inv_NMOS_ChannelLength
        _Caculation_Parameters1['_AND_Inv_NMOS_NumberofGate'] = _Comp_AND_Inv_NMOS_NumberofGate
        _Caculation_Parameters1['_AND_Inv_NMOS_XVT'] = _Comp_AND_Inv_NMOS_XVT
        _Caculation_Parameters1['_AND_Inv_NMOS_POGate_Comb_length'] = _Comp_AND_Inv_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_AND_Inv_PMOS_ChannelWidth'] = _Comp_AND_Inv_PMOS_ChannelWidth
        _Caculation_Parameters1['_AND_Inv_PMOS_ChannelLength'] = _Comp_AND_Inv_PMOS_ChannelLength
        _Caculation_Parameters1['_AND_Inv_PMOS_NumberofGate'] = _Comp_AND_Inv_PMOS_NumberofGate
        _Caculation_Parameters1['_AND_Inv_PMOS_XVT'] = _Comp_AND_Inv_PMOS_XVT
        _Caculation_Parameters1['_AND_Inv_PMOS_POGate_Comb_length'] = _Comp_AND_Inv_PMOS_POGate_Comb_length

        ## CLK Buffer
        # Inverter1
        _Caculation_Parameters1['_CLKBuf_Inv1_NMOS_ChannelWidth'] = _Comp_CLKBuf_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters1['_CLKBuf_Inv1_NMOS_ChannelLength'] = _Comp_CLKBuf_Inv1_NMOS_ChannelLength
        _Caculation_Parameters1['_CLKBuf_Inv1_NMOS_NumberofGate'] = _Comp_CLKBuf_Inv1_NMOS_NumberofGate
        _Caculation_Parameters1['_CLKBuf_Inv1_NMOS_XVT'] = _Comp_CLKBuf_Inv1_NMOS_XVT
        _Caculation_Parameters1['_CLKBuf_Inv1_NMOS_POGate_Comb_length'] = _Comp_CLKBuf_Inv1_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_CLKBuf_Inv1_PMOS_ChannelWidth'] = _Comp_CLKBuf_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters1['_CLKBuf_Inv1_PMOS_ChannelLength'] = _Comp_CLKBuf_Inv1_PMOS_ChannelLength
        _Caculation_Parameters1['_CLKBuf_Inv1_PMOS_NumberofGate'] = _Comp_CLKBuf_Inv1_PMOS_NumberofGate
        _Caculation_Parameters1['_CLKBuf_Inv1_PMOS_XVT'] = _Comp_CLKBuf_Inv1_PMOS_XVT
        _Caculation_Parameters1['_CLKBuf_Inv1_PMOS_POGate_Comb_length'] = _Comp_CLKBuf_Inv1_PMOS_POGate_Comb_length

        # Inverter2
        _Caculation_Parameters1['_CLKBuf_Inv2_NMOS_ChannelWidth'] = _Comp_CLKBuf_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters1['_CLKBuf_Inv2_NMOS_ChannelLength'] = _Comp_CLKBuf_Inv2_NMOS_ChannelLength
        _Caculation_Parameters1['_CLKBuf_Inv2_NMOS_NumberofGate'] = _Comp_CLKBuf_Inv2_NMOS_NumberofGate
        _Caculation_Parameters1['_CLKBuf_Inv2_NMOS_XVT'] = _Comp_CLKBuf_Inv2_NMOS_XVT
        _Caculation_Parameters1['_CLKBuf_Inv2_NMOS_POGate_Comb_length'] = _Comp_CLKBuf_Inv2_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_CLKBuf_Inv2_PMOS_ChannelWidth'] = _Comp_CLKBuf_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters1['_CLKBuf_Inv2_PMOS_ChannelLength'] = _Comp_CLKBuf_Inv2_PMOS_ChannelLength
        _Caculation_Parameters1['_CLKBuf_Inv2_PMOS_NumberofGate'] = _Comp_CLKBuf_Inv2_PMOS_NumberofGate
        _Caculation_Parameters1['_CLKBuf_Inv2_PMOS_XVT'] = _Comp_CLKBuf_Inv2_PMOS_XVT
        _Caculation_Parameters1['_CLKBuf_Inv2_PMOS_POGate_Comb_length'] = _Comp_CLKBuf_Inv2_PMOS_POGate_Comb_length

        # PowerRail Placement
        _Caculation_Parameters1['_BufSR_NMOS_Pbody_NumCont'] = _Comp_BufSR_NMOS_Pbody_NumCont
        _Caculation_Parameters1['_BufSR_NMOS_Pbody_XvtTop2Pbody'] = _Comp_BufSR_NMOS_Pbody_XvtTop2Pbody
        _Caculation_Parameters1['_BufSR_PMOS_Nbody_NumCont'] = _Comp_BufSR_PMOS_Nbody_NumCont
        _Caculation_Parameters1['_BufSR_PMOS_Nbody_Xvtdown2Nbody'] = _Comp_BufSR_PMOS_Nbody_Xvtdown2Nbody
        _Caculation_Parameters1['_BufSR_PMOSXvt2NMOSXvt'] = _Comp_BufSR_PMOSXvt2NMOSXvt

        _Caculation_Parameters1['_CLKInLogic_NMOS_Pbody_Xvtdown2Pbody'] = _Comp_CLKInLogic_NMOS_Pbody_Xvtdown2Pbody
        _Caculation_Parameters1['_CLKInLogic_PMOS_Nbody_NumCont'] = _Comp_CLKInLogic_PMOS_Nbody_NumCont
        _Caculation_Parameters1['_CLKInLogic_PMOS_Nbody_Xvtdown2Nbody'] = _Comp_CLKInLogic_PMOS_Nbody_Xvtdown2Nbody
        _Caculation_Parameters1['_CLKInLogic_PMOSXvt2NMOSXvt'] = _Comp_CLKInLogic_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Comparator'] = self._SrefElementDeclaration(_DesignObj=E01_05_StrongArmWtSRLatch._StrongArmWtSRLatch(_DesignParameter=None, _Name='{}:SRF_Comparator'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Comparator']['_Reflect'] = [1, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Comparator']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Comparator']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters1)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_Comparator']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1x = self.get_param_KJH4('SRF_SARLogicWtBuffers', 'SRF_SARLogicWtCLKTree', 'SRF_SARLogic', 'BND_Nbody_M1Exten')
        tmp1_1 = self.get_param_KJH4('SRF_SARLogicWtBuffers', 'SRF_LowerCDACPreDriver', 'BND_Nbody_M1Exten')
        tmp1_2 = self.get_param_KJH4('SRF_SARLogicWtBuffers', 'SRF_UpperCDACPreDriver', 'BND_Pbody_M1Exten')
        tmp1y = int((tmp1_1[0][0][0][0]['_XY_cent'][1] + tmp1_2[0][0][0][0]['_XY_cent'][1]) / 2)
        target_coord = [tmp1x[0][0][0][0][0]['_XY_left'][0], tmp1y]
        ## Approaching_coord: _XY_type2
        ## Define Boundary_element _XWidth
        self._DesignParameter['SRF_Comparator']['_DesignObj']._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Comparator']['_DesignObj']._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_Angle'] = 0
        self._DesignParameter['SRF_Comparator']['_DesignObj']._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_Angle'] = 0
        self._DesignParameter['SRF_Comparator']['_DesignObj']._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Comparator']['_DesignObj']._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_Angle'] = 0
        self._DesignParameter['SRF_Comparator']['_DesignObj']._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Comparator']['_DesignObj']._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_Angle'] = 0
        self._DesignParameter['SRF_Comparator']['_DesignObj']._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_Reflect'] = [0, 0, 0]

        tmp2y = self.get_param_KJH3('SRF_Comparator', 'SRF_Slicer', '_NMOSSET', '_VIANMOSPoly2Met1NMOS1', '_Met1Layer')
        tmp2x = self.get_param_KJH4('SRF_Comparator', 'BND_Pbody_Hrz_M1')
        CompInputPNViaYLength = 219
        approaching_coord = [tmp2x[0][0][0]['_XY_right'][0], tmp2y[0][0][0][0][0][0]['_XY_cent'][1] + CompInputPNViaYLength]
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Comparator')
        Scoord = tmp3[0][0]['_XY_origin']
        SpaceBtwComparatorAndSARLogic = 600
        Scoord[0] = Scoord[0] - SpaceBtwComparatorAndSARLogic
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['SRF_Comparator']['_XYCoordinates'] = tmpXY

        ########## Pre-Defined Values for Calculation
        ### (CLKSamp, CLKSrc) SARLogic -> Comparator
        CLKSrcInHrzMetalWidth = 100
        SpaceBtwTreeInternalRoutePathAndCLKSampInHrz = 100
        CLKSampInHrzMetalWidth = 100
        CLKSampInVtcM4MetalWidth = 50
        CLKSampInVtcM4MetalSpaceBtwMSB0VtcM4 = 100
        CLKSrcInVtcM4MetalWidth = 50
        SpaceBtwCLKSampInHrzAndCLKSrcInHrz = 100
        SpaceBtwCLKSampBufAndCLKSrcBuf = 1000

        CLKSampBufOutHrzMetalWidth = 50
        CLKSrcBufOutHrzMetalWidth = 50
        SpaceBtwCLKSrcBufOutHrzAndCLKSampBufOutHrz = 50

        CLKSampANDInVtcMetalWidth = 50
        CLKSrcANDInVtcMetalWidth = 50
        CompOutVtcM4MetalWidth = 50
        CompOutBufInHrzM3MetalWidth = 50

        ### (CompOut) Comparator -> SARLogic
        SpaceBtwM4VtcPathAndCompOutBufOut = 100
        CompSRLatchOutputQHrzM3MetalWidth = 50
        CompOutSARLogicTreeBufInHrzMetalWidth = 100
        SpaceBtwTreeInternalRoutePathAndCompOut = 100
        CompOutBufOutputVtcM4Width = 50

        # CLKSrcInVtcM4MetalSpace = 100
        CLKDoutMetalWidth = 100
        SpaceBtwCompOutAndCLKDout = 100

        ################## CLK_Samp Routing #################################
        ##### BND_SARCLKSampIn_Vtc_M2
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_SARCLKSampIn_Vtc_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_SARLogicWtBuffers', 'SRF_SARLogicWtCLKTree', 'SRF_CLKBufferTree_Top',
                                   'SRF_CLKBuf1Inv_Stage1', 'SRF_InputViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        tmp2 = self.get_param_KJH4('SRF_SARLogicWtBuffers', 'SRF_SARLogicWtCLKTree', 'SRF_CLKBufferTree_Top', 'BND_Buf2Stg2to1_Hrz_M3')
        self._DesignParameter['BND_SARCLKSampIn_Vtc_M2']['_YWidth'] = abs(
            tmp2[0][0][0][0][0]['_XY_up'][1] - tmp1[0][0][0][0][0][0][0][0]['_XY_down'][1]) + CLKSampInHrzMetalWidth + SpaceBtwTreeInternalRoutePathAndCLKSampInHrz + CLKSrcInHrzMetalWidth + SpaceBtwCLKSampInHrzAndCLKSrcInHrz

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_SARCLKSampIn_Vtc_M2']['_XWidth'] = tmp1[0][0][0][0][0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_SARCLKSampIn_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_SARCLKSampIn_Vtc_M2')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_SARCLKSampIn_Vtc_M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_SARCLKSampIn_Vtc_M2']['_XYCoordinates'] = tmpXY

        ###### BND_SARCLKSampIn_Vtc_M2 -> BND_CLKSampIn_Hrz_M3 ViaM2M3
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKSampBuf_ViaM2M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_CLKSampBuf_ViaM2M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKSampBuf_ViaM2M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKSampBuf_ViaM2M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKSampBuf_ViaM2M3']['_DesignObj']._CalculateDesignParameterYmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKSampBuf_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_SARCLKSampIn_Vtc_M2')
        target_coord = tmp1[0][0]['_XY_up_right']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CLKSampBuf_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKSampBuf_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKSampBuf_ViaM2M3']['_XYCoordinates'] = tmpXY

        ##### BND_CLKSampIn_Hrz_M3
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CLKSampIn_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        tmp1 = self.get_param_KJH4('SRF_SARLogicWtBuffers', 'BND_UpperCDACPreDrvIn_Vtc_M4')
        tmp2 = self.get_param_KJH4('SRF_CLKSampBuf_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met2Layer')
        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_CLKSampIn_Hrz_M3']['_YWidth'] = CLKSampInHrzMetalWidth

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CLKSampIn_Hrz_M3']['_XWidth'] = abs(tmp1[0][0][0]['_XY_left'][0] - tmp2[0][0][0][0]['_XY_right'][0]) + CLKSampInVtcM4MetalSpaceBtwMSB0VtcM4

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CLKSampIn_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp2[0][0][0][0]['_XY_up_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CLKSampIn_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CLKSampIn_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CLKSampIn_Hrz_M3']['_XYCoordinates'] = tmpXY

        ####################################################################################################
        # # Additional Buffer Between CLK_Sample Input of Comparator And Output of Tree Buffer
        _Caculation_Parameters = copy.deepcopy(
            J00_01_InverterChain_KJH._InverterChain._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Pbody_NumCont'] = _Buf_CLKSamp_Pbody_NumCont
        _Caculation_Parameters['_Nbody_NumCont'] = _Buf_CLKSamp_Nbody_NumCont
        _Caculation_Parameters['_PMOSXvt2NMOSXvt'] = _Buf_CLKSamp_PMOSXvt2NMOSXvt
        _Caculation_Parameters['_XvtTop2Pbody'] = _Buf_CLKSamp_XvtTop2Pbody
        _Caculation_Parameters['_Xvtdown2Nbody'] = _Buf_CLKSamp_Xvtdown2Nbody

        _Caculation_Parameters['_NumberofGate'] = _Buf_CLKSamp_NumberofGate
        _Caculation_Parameters['_ChannelLength'] = _Buf_CLKSamp_ChannelLength
        _Caculation_Parameters['_XVT'] = _Buf_CLKSamp_XVT

        _Caculation_Parameters['_Inv_NMOS_ChannelWidth'] = _Buf_CLKSamp_Inv_NMOS_ChannelWidth
        _Caculation_Parameters['_Inv_NMOS_POGate_Comb_length'] = _Buf_CLKSamp_Inv_NMOS_POGate_Comb_length
        _Caculation_Parameters['_Inv_PMOS_ChannelWidth'] = _Buf_CLKSamp_Inv_PMOS_ChannelWidth
        _Caculation_Parameters['_Inv_PMOS_POGate_Comb_length'] = _Buf_CLKSamp_Inv_PMOS_POGate_Comb_length

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Buf_CLKSamp'] = self._SrefElementDeclaration(
            _DesignObj=J00_01_InverterChain_KJH._InverterChain(_DesignParameter=None,
                                                               _Name='{}:SRF_Buf_CLKSamp'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Buf_CLKSamp']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Buf_CLKSamp']['_Angle'] = 180

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Buf_CLKSamp']['_DesignObj']._CalculateDesignParameter(
            **_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Buf_CLKSamp']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord
        tmp1x = self.get_param_KJH4('BND_CLKSampIn_Hrz_M3')
        tmp1y = self.get_param_KJH4('SRF_SARLogicWtBuffers', 'SRF_SARLogicWtCLKTree', 'SRF_CLKBufferTree_Top', 'BND_Nbody_M1')
        target_coord = [tmp1x[0][0]['_XY_left'][0], tmp1y[0][0][0][0][0]['_XY_up'][1]]
        ## Approaching_coord
        tmp2x = self.get_param_KJH4('SRF_Buf_CLKSamp', 'SRF_Input_ViaM1Mx', 'SRF_ViaM1M2', 'BND_Met2Layer')
        tmp2y = self.get_param_KJH4('SRF_Buf_CLKSamp', 'SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = [tmp2x[0][0][0][0][0]['_XY_left'][0], tmp2y[0][0][0][0][0]['_XY_down'][1]]
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Buf_CLKSamp')
        Scoord = tmp3[0][0]['_XY_origin']

        Scoord[0] = Scoord[0] - CLKSampInVtcM4MetalWidth
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_Buf_CLKSamp']['_XYCoordinates'] = tmpXY

        ####################################################################################################
        # # Additional Buffer Between CLK_Src Input of Comparator And Output of Tree Buffer
        _Caculation_Parameters = copy.deepcopy(
            J00_01_InverterChain_KJH._InverterChain._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Pbody_NumCont'] = _Buf_CLKSrc_Pbody_NumCont
        _Caculation_Parameters['_Nbody_NumCont'] = _Buf_CLKSrc_Nbody_NumCont
        _Caculation_Parameters['_PMOSXvt2NMOSXvt'] = _Buf_CLKSrc_PMOSXvt2NMOSXvt
        _Caculation_Parameters['_XvtTop2Pbody'] = _Buf_CLKSrc_XvtTop2Pbody
        _Caculation_Parameters['_Xvtdown2Nbody'] = _Buf_CLKSrc_Xvtdown2Nbody

        _Caculation_Parameters['_NumberofGate'] = _Buf_CLKSrc_NumberofGate
        _Caculation_Parameters['_ChannelLength'] = _Buf_CLKSrc_ChannelLength
        _Caculation_Parameters['_XVT'] = _Buf_CLKSrc_XVT

        _Caculation_Parameters['_Inv_NMOS_ChannelWidth'] = _Buf_CLKSrc_Inv_NMOS_ChannelWidth
        _Caculation_Parameters['_Inv_NMOS_POGate_Comb_length'] = _Buf_CLKSrc_Inv_NMOS_POGate_Comb_length
        _Caculation_Parameters['_Inv_PMOS_ChannelWidth'] = _Buf_CLKSrc_Inv_PMOS_ChannelWidth
        _Caculation_Parameters['_Inv_PMOS_POGate_Comb_length'] = _Buf_CLKSrc_Inv_PMOS_POGate_Comb_length

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Buf_CLKSrc'] = self._SrefElementDeclaration(
            _DesignObj=J00_01_InverterChain_KJH._InverterChain(_DesignParameter=None,
                                                               _Name='{}:SRF_Buf_CLKSrc'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Buf_CLKSrc']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Buf_CLKSrc']['_Angle'] = 180

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Buf_CLKSrc']['_DesignObj']._CalculateDesignParameter(
            **_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Buf_CLKSrc']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord
        tmp2 = self.get_param_KJH4('SRF_Buf_CLKSamp', 'SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        # tmp2x = self.get_param_KJH4('SRF_SARLogicWtBuffers', 'BND_UpperCDACPreDrvIn_Vtc_M4')
        target_coord = tmp2[0][0][0][0][0]['_XY_up_right']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Buf_CLKSrc', 'SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Buf_CLKSrc')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[0] = Scoord[0] - SpaceBtwCLKSampBufAndCLKSrcBuf
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_Buf_CLKSrc']['_XYCoordinates'] = tmpXY

        ### Output Path Metal을 3으로 쓰기 위해 삭제
        del (self._DesignParameter['SRF_Buf_CLKSrc']['_DesignObj']._DesignParameter['SRF_Output_ViaM2Mx']['_DesignObj']._DesignParameter['SRF_ViaM3M4'])

        ###### BND_CLKSampIn_Hrz_M3 ViaM2M3 -> BND_BufCLKSampIn_Vtc_M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKSampBuf_ViaM3M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_CLKSampBuf_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKSampBuf_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKSampBuf_ViaM3M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKSampBuf_ViaM3M4']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKSampBuf_ViaM3M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_CLKSampIn_Hrz_M3')
        target_coord = tmp1[0][0]['_XY_down_left']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CLKSampBuf_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKSampBuf_ViaM3M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKSampBuf_ViaM3M4']['_XYCoordinates'] = tmpXY

        ##### BND_BufCLKSampIn_Vtc_M4
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_BufCLKSampIn_Vtc_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        tmp1 = self.get_param_KJH4('SRF_Buf_CLKSamp', 'SRF_Input_ViaM1Mx', 'SRF_ViaM1M2', 'BND_Met2Layer')
        tmp2 = self.get_param_KJH4('BND_CLKSampIn_Hrz_M3')
        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_BufCLKSampIn_Vtc_M4']['_XWidth'] = CLKSampInVtcM4MetalWidth

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_BufCLKSampIn_Vtc_M4']['_YWidth'] = abs(tmp1[0][0][0][0][0]['_XY_down'][1] - tmp2[0][0]['_XY_down'][1])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_BufCLKSampIn_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp2[0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_BufCLKSampIn_Vtc_M4')
        approaching_coord = tmp2[0][0]['_XY_down_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_BufCLKSampIn_Vtc_M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_BufCLKSampIn_Vtc_M4']['_XYCoordinates'] = tmpXY

        ###################### CLKSamp_Buf -> Comparator AND Gate Input Routing
        ### SRF_CLKSamp Output Via를 아래로 조정
        self._DesignParameter['SRF_Buf_CLKSamp']['_DesignObj']._DesignParameter['SRF_Output_ViaM2Mx']['_XYCoordinates'][0][1] = SpaceBtwCLKSrcBufOutHrzAndCLKSampBufOutHrz + CLKSampBufOutHrzMetalWidth + self._DesignParameter['SRF_Buf_CLKSamp']['_DesignObj']._DesignParameter['SRF_Output_ViaM2Mx']['_XYCoordinates'][0][1]

        ### Output Path Metal을 3으로 쓰기 위해 삭제
        del (self._DesignParameter['SRF_Buf_CLKSamp']['_DesignObj']._DesignParameter['SRF_Output_ViaM2Mx']['_DesignObj']._DesignParameter['SRF_ViaM3M4'])

        ##### BND_CLKSampBufOut_Hrz_M3
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CLKSampBufOut_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        tmp1 = self.get_param_KJH4('SRF_Buf_CLKSamp', 'SRF_Output_ViaM2Mx', 'SRF_ViaM2M3', 'BND_Met2Layer')
        tmp2 = self.get_param_KJH4('SRF_Comparator', 'SRF_CLKSampInv_Input_ViaM1M4', 'SRF_ViaM1M2', 'BND_Met2Layer')
        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_CLKSampBufOut_Hrz_M3']['_YWidth'] = CLKSampBufOutHrzMetalWidth

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CLKSampBufOut_Hrz_M3']['_XWidth'] = abs(
            tmp1[0][0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CLKSampBufOut_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_CLKSampBufOut_Hrz_M3')
        approaching_coord = tmp3[0][0]['_XY_up_right']
        ## Sref coord
        tmp4 = self.get_param_KJH4('BND_CLKSampBufOut_Hrz_M3')
        Scoord = tmp4[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CLKSampBufOut_Hrz_M3']['_XYCoordinates'] = tmpXY

        ###### Via BND_CLKSampBufOut_Hrz_M3 -> BND_CLKSampANDIn_Vtc_M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKSampANDIn_ViaM3M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_CLKSampANDIn_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKSampANDIn_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKSampANDIn_ViaM3M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKSampANDIn_ViaM3M4']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKSampANDIn_ViaM3M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_CLKSampBufOut_Hrz_M3')
        target_coord = tmp1[0][0]['_XY_up_left']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CLKSampANDIn_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKSampANDIn_ViaM3M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKSampANDIn_ViaM3M4']['_XYCoordinates'] = tmpXY

        ##### BND_CLKSampANDIn_Vtc_M4
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CLKSampANDIn_Vtc_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        tmp1 = self.get_param_KJH4('SRF_CLKSampANDIn_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met3Layer')
        tmp2 = self.get_param_KJH4('SRF_Comparator', 'SRF_CLKSampInv_Input_ViaM1M4', 'SRF_ViaM1M2', 'BND_Met2Layer')
        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_CLKSampANDIn_Vtc_M4']['_XWidth'] = CLKSampANDInVtcMetalWidth

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CLKSampANDIn_Vtc_M4']['_YWidth'] = abs(
            tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0]['_XY_down'][1])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CLKSampANDIn_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_CLKSampANDIn_Vtc_M4')
        approaching_coord = tmp3[0][0]['_XY_up_left']
        ## Sref coord
        tmp4 = self.get_param_KJH4('BND_CLKSampANDIn_Vtc_M4')
        Scoord = tmp4[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CLKSampANDIn_Vtc_M4']['_XYCoordinates'] = tmpXY

        ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
        ########################### CLK_Src Routing #################################
        ##### BND_SARCLKSrcIn_Vtc_M2
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_SARCLKSrcIn_Vtc_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_SARLogicWtBuffers', 'SRF_SARLogicWtCLKTree', 'SRF_CLKBufferTree_Top',
                                   'SRF_CLKBuf2Inv_Stage1', 'SRF_InputViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        tmp2 = self.get_param_KJH4('SRF_SARLogicWtBuffers', 'SRF_SARLogicWtCLKTree', 'SRF_CLKBufferTree_Top', 'BND_Buf2Stg2to1_Hrz_M3')

        self._DesignParameter['BND_SARCLKSrcIn_Vtc_M2']['_YWidth'] = abs(
            tmp2[0][0][0][0][0]['_XY_up'][1] - tmp1[0][0][0][0][0][0][0][0]['_XY_down'][1]) + CLKSrcInHrzMetalWidth + SpaceBtwCLKSampInHrzAndCLKSrcInHrz

        ## Define Boundary_element _XWidth

        self._DesignParameter['BND_SARCLKSrcIn_Vtc_M2']['_XWidth'] = tmp1[0][0][0][0][0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_SARCLKSrcIn_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_SARCLKSrcIn_Vtc_M2')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_SARCLKSrcIn_Vtc_M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_SARCLKSrcIn_Vtc_M2']['_XYCoordinates'] = tmpXY

        ###### BND_SARCLKSrcIn_Vtc_M2 -> BND_CompCLKSrcIn_Hrz_M3 ViaM2M3
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKSrcBuf_ViaM2M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_CLKSrcBuf_ViaM2M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKSrcBuf_ViaM2M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKSrcBuf_ViaM2M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKSrcBuf_ViaM2M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKSrcBuf_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_SARCLKSrcIn_Vtc_M2')
        target_coord = tmp1[0][0]['_XY_up_right']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CLKSrcBuf_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKSrcBuf_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKSrcBuf_ViaM2M3']['_XYCoordinates'] = tmpXY

        ##### BND_CLKSrcIn_Hrz_M3
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CLKSrcIn_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        tmp1 = self.get_param_KJH4('SRF_Buf_CLKSrc', 'SRF_Input_ViaM1Mx', 'SRF_ViaM1M2', 'BND_Met2Layer')
        tmp2 = self.get_param_KJH4('SRF_CLKSrcBuf_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met2Layer')
        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_CLKSrcIn_Hrz_M3']['_YWidth'] = CLKSrcInHrzMetalWidth

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CLKSrcIn_Hrz_M3']['_XWidth'] = abs(
            tmp1[0][0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CLKSrcIn_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp2[0][0][0][0]['_XY_up_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CLKSrcIn_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CLKSrcIn_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CLKSrcIn_Hrz_M3']['_XYCoordinates'] = tmpXY

        ###### BND_CLKSrcIn_Hrz_M3 ViaM2M3 -> BND_BufCLKSrcIn_Vtc_M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKSrcBuf_ViaM3M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_CLKSrcBuf_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKSrcBuf_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKSrcBuf_ViaM3M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKSrcBuf_ViaM3M4']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKSrcBuf_ViaM3M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_CLKSrcIn_Hrz_M3')
        target_coord = tmp1[0][0]['_XY_down_left']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CLKSrcBuf_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKSrcBuf_ViaM3M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKSrcBuf_ViaM3M4']['_XYCoordinates'] = tmpXY

        ##### BND_BufCLKSrcIn_Vtc_M4
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_BufCLKSrcIn_Vtc_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        tmp1 = self.get_param_KJH4('SRF_Buf_CLKSrc', 'SRF_Input_ViaM1Mx', 'SRF_ViaM1M2', 'BND_Met2Layer')
        tmp2 = self.get_param_KJH4('BND_CLKSrcIn_Hrz_M3')
        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_BufCLKSrcIn_Vtc_M4']['_XWidth'] = CLKSrcInVtcM4MetalWidth

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_BufCLKSrcIn_Vtc_M4']['_YWidth'] = abs(
            tmp1[0][0][0][0][0]['_XY_down'][1] - tmp2[0][0]['_XY_down'][1])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_BufCLKSrcIn_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp2[0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_BufCLKSrcIn_Vtc_M4')
        approaching_coord = tmp2[0][0]['_XY_down_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_BufCLKSrcIn_Vtc_M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_BufCLKSrcIn_Vtc_M4']['_XYCoordinates'] = tmpXY

        ##### CLKSrc_Buf -> Comparator AND Gate Input Routing
        ##### BND_CLKSrcBufOut_Hrz_M3
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CLKSrcBufOut_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        tmp1 = self.get_param_KJH4('SRF_Buf_CLKSrc', 'SRF_Output_ViaM2Mx', 'SRF_ViaM2M3', 'BND_Met2Layer')
        tmp2 = self.get_param_KJH4('SRF_Comparator', 'SRF_CLKSrcInv_Input_ViaM1M4', 'SRF_ViaM1M2', 'BND_Met2Layer')
        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_CLKSrcBufOut_Hrz_M3']['_YWidth'] = CLKSrcBufOutHrzMetalWidth

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CLKSrcBufOut_Hrz_M3']['_XWidth'] = abs(
            tmp1[0][0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CLKSrcBufOut_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_CLKSrcBufOut_Hrz_M3')
        approaching_coord = tmp3[0][0]['_XY_up_right']
        ## Sref coord
        tmp4 = self.get_param_KJH4('BND_CLKSrcBufOut_Hrz_M3')
        Scoord = tmp4[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CLKSrcBufOut_Hrz_M3']['_XYCoordinates'] = tmpXY

        ###### BND_CLKSrcBufOut_Hrz_M3 -> BND_CLKSrcANDIn_Vtc_M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKSrcANDIn_ViaM3M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_CLKSrcANDIn_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKSrcANDIn_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKSrcANDIn_ViaM3M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKSrcANDIn_ViaM3M4']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKSrcANDIn_ViaM3M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_CLKSrcBufOut_Hrz_M3')
        target_coord = tmp1[0][0]['_XY_up_left']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CLKSrcANDIn_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKSrcANDIn_ViaM3M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKSrcANDIn_ViaM3M4']['_XYCoordinates'] = tmpXY

        ##### BND_CLKSrcANDIn_Vtc_M4
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CLKSrcANDIn_Vtc_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        tmp1 = self.get_param_KJH4('SRF_CLKSrcANDIn_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met3Layer')
        tmp2 = self.get_param_KJH4('SRF_Comparator', 'SRF_CLKSrcInv_Input_ViaM1M4', 'SRF_ViaM1M2', 'BND_Met2Layer')
        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_CLKSrcANDIn_Vtc_M4']['_XWidth'] = CLKSrcANDInVtcMetalWidth

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CLKSrcANDIn_Vtc_M4']['_YWidth'] = abs(
            tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0]['_XY_down'][1])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CLKSrcANDIn_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_CLKSrcANDIn_Vtc_M4')
        approaching_coord = tmp3[0][0]['_XY_up_left']
        ## Sref coord
        tmp4 = self.get_param_KJH4('BND_CLKSrcANDIn_Vtc_M4')
        Scoord = tmp4[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CLKSrcANDIn_Vtc_M4']['_XYCoordinates'] = tmpXY

        ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
        ######################### CompOut Routing ##########################################
        # # Additional Buffer Between <CompOut> Input of Comparator And Output of Tree Buffer
        _Caculation_Parameters = copy.deepcopy(
            J00_01_InverterChain_KJH._InverterChain._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Pbody_NumCont'] = _Buf_CompOut_Pbody_NumCont
        _Caculation_Parameters['_Nbody_NumCont'] = _Buf_CompOut_Nbody_NumCont
        _Caculation_Parameters['_PMOSXvt2NMOSXvt'] = _Buf_CompOut_PMOSXvt2NMOSXvt
        _Caculation_Parameters['_XvtTop2Pbody'] = _Buf_CompOut_XvtTop2Pbody
        _Caculation_Parameters['_Xvtdown2Nbody'] = _Buf_CompOut_Xvtdown2Nbody

        _Caculation_Parameters['_NumberofGate'] = _Buf_CompOut_NumberofGate
        _Caculation_Parameters['_ChannelLength'] = _Buf_CompOut_ChannelLength
        _Caculation_Parameters['_XVT'] = _Buf_CompOut_XVT

        _Caculation_Parameters['_Inv_NMOS_ChannelWidth'] = _Buf_CompOut_Inv_NMOS_ChannelWidth
        _Caculation_Parameters['_Inv_NMOS_POGate_Comb_length'] = _Buf_CompOut_Inv_NMOS_POGate_Comb_length
        _Caculation_Parameters['_Inv_PMOS_ChannelWidth'] = _Buf_CompOut_Inv_PMOS_ChannelWidth
        _Caculation_Parameters['_Inv_PMOS_POGate_Comb_length'] = _Buf_CompOut_Inv_PMOS_POGate_Comb_length

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Buf_CompOut'] = self._SrefElementDeclaration(
            _DesignObj=J00_01_InverterChain_KJH._InverterChain(_DesignParameter=None,
                                                               _Name='{}:SRF_Buf_CompOut'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Buf_CompOut']['_Reflect'] = [1, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Buf_CompOut']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Buf_CompOut']['_DesignObj']._CalculateDesignParameter(
            **_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Buf_CompOut']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord
        tmp2y = self.get_param_KJH4('SRF_SARLogicWtBuffers', 'SRF_SARLogicWtCLKTree', 'SRF_CLKBufferTree_Bot',
                                    'BND_Pbody_M1')
        tmp2x = self.get_param_KJH4('SRF_SARLogicWtBuffers', 'BND_LowerCDACPreDrvIn_Vtc_M4')
        target_coord = [tmp2x[0][0][0]['_XY_left'][0], tmp2y[0][0][0][0][0]['_XY_up'][1]]
        ## Approaching_coord
        tmp2y = self.get_param_KJH4('SRF_Buf_CompOut', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        tmp2x = self.get_param_KJH4('SRF_Buf_CompOut', 'SRF_Output_ViaM2Mx', 'SRF_ViaM2M3', 'BND_Met2Layer')
        approaching_coord = [tmp2x[0][0][0][0][0]['_XY_right'][0], tmp2y[0][0][0][0][0]['_XY_down'][1]]
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Buf_CompOut')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[0] = Scoord[0] - SpaceBtwM4VtcPathAndCompOutBufOut
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_Buf_CompOut']['_XYCoordinates'] = tmpXY

        ### Input Path Metal을 3으로 쓰기 위해 삭제
        del (self._DesignParameter['SRF_Buf_CompOut']['_DesignObj']._DesignParameter['SRF_Input_ViaM1Mx']['_DesignObj']._DesignParameter['SRF_ViaM3M4'])

        ##### BND_CompOut_Hrz_M3
        ########## OutputQ <-> NAND S routing boundary element gen.
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CompOut_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_CompOut_Hrz_M3']['_YWidth'] = CompSRLatchOutputQHrzM3MetalWidth

        ## Define Boundary_element _XWidth
        tmp2_1 = self.get_param_KJH4('SRF_Comparator', 'SRF_SRLatch', 'SRF_OutputQ_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met2Layer')
        tmp2_2 = self.get_param_KJH4('SRF_Comparator', 'BND_NWellOnSRLatchAndBuffer')
        self._DesignParameter['BND_CompOut_Hrz_M3']['_XWidth'] = abs(
            tmp2_1[0][0][0][0][0][0]['_XY_left'][0] - tmp2_2[0][0][0]['_XY_right'][0])

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_CompOut_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmpx = self.get_param_KJH4('SRF_Comparator', 'SRF_SRLatch', 'SRF_OutputQ_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met2Layer')
        target_coord = tmpx[0][0][0][0][0][0]['_XY_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CompOut_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CompOut_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CompOut_Hrz_M3']['_XYCoordinates'] = tmpXY

        # ###### Via BND_CompOut_Hrz_M3 -> BND_CompOut_Vtc_M4
        # ## Sref generation: ViaX
        # ## Define ViaX Parameter
        # _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        # _Caculation_Parameters['_Layer1'] = 3
        # _Caculation_Parameters['_Layer2'] = 4
        # _Caculation_Parameters['_COX'] = 1
        # _Caculation_Parameters['_COY'] = 2
        #
        # ## Sref ViaX declaration
        # self._DesignParameter['SRF_CompOut_ViaM3M4'] = self._SrefElementDeclaration(
        #   _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
        #                                          _Name='{}:SRF_CompOut_ViaM3M4'.format(_Name)))[0]
        #
        # ## Define Sref Relection
        # self._DesignParameter['SRF_CompOut_ViaM3M4']['_Reflect'] = [0, 0, 0]
        #
        # ## Define Sref Angle
        # self._DesignParameter['SRF_CompOut_ViaM3M4']['_Angle'] = 0
        #
        # ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        # self._DesignParameter['SRF_CompOut_ViaM3M4']['_DesignObj']._CalculateDesignParameterXmin(
        #   **_Caculation_Parameters)
        # uu
        # ## Calculate Sref XYcoord
        # tmpXY = []
        # ## initialized Sref coordinate
        # self._DesignParameter['SRF_CompOut_ViaM3M4']['_XYCoordinates'] = [[0, 0]]
        # ## Calculate
        # ## Target_coord
        # tmp1 = self.get_param_KJH4('BND_CompOut_Hrz_M3')
        # target_coord = tmp1[0][0]['_XY_up_right']
        # ## Approaching_coord
        # tmp2 = self.get_param_KJH4('SRF_CompOut_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met3Layer')
        # approaching_coord = tmp2[0][0][0][0]['_XY_up_right']
        # ## Sref coord
        # tmp3 = self.get_param_KJH4('SRF_CompOut_ViaM3M4')
        # Scoord = tmp3[0][0]['_XY_origin']
        # ## Calculate
        # New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        # tmpXY.append(New_Scoord)
        # ## Define
        # self._DesignParameter['SRF_CompOut_ViaM3M4']['_XYCoordinates'] = tmpXY

        ##### BND_CompOut_Vtc_M4
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CompOut_Vtc_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_CompOut_Vtc_M4']['_XWidth'] = CompOutVtcM4MetalWidth

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Buf_CompOut', 'SRF_Input_ViaM1Mx', 'SRF_ViaM1M2', 'BND_Met2Layer')
        tmp2 = self.get_param_KJH4('BND_CompOut_Hrz_M3')
        self._DesignParameter['BND_CompOut_Vtc_M4']['_YWidth'] = abs(
            tmp1[0][0][0][0][0]['_XY_up'][1] - tmp2[0][0]['_XY_up'][1])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CompOut_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp2[0][0]['_XY_up_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CompOut_Vtc_M4')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CompOut_Vtc_M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CompOut_Vtc_M4']['_XYCoordinates'] = tmpXY

        ###### Via BND_CompOut_Vtc_M4 -> BND_CompOutBufIn_Hrz_M3
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CompOut_ViaM3M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_CompOut_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CompOut_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CompOut_ViaM3M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CompOut_ViaM3M4']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CompOut_ViaM3M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_CompOut_Vtc_M4')
        target_coord = tmp1[0][0]['_XY_down_left']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CompOut_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CompOut_ViaM3M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate1
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Calculate2
        target_coord = tmp1[0][0]['_XY_up_left']
        approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CompOut_ViaM3M4']['_XYCoordinates'] = tmpXY

        ##### BND_CompOutBufIn_Hrz_M3
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CompOutBufIn_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_CompOutBufIn_Hrz_M3']['_YWidth'] = CompOutBufInHrzM3MetalWidth

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('BND_CompOut_Vtc_M4')
        tmp2 = self.get_param_KJH4('SRF_Buf_CompOut', 'SRF_Input_ViaM1Mx', 'SRF_ViaM1M2', 'BND_Met2Layer')
        self._DesignParameter['BND_CompOutBufIn_Hrz_M3']['_XWidth'] = abs(
            tmp1[0][0]['_XY_right'][0] - tmp2[0][0][0][0][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CompOutBufIn_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CompOutBufIn_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CompOutBufIn_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CompOutBufIn_Hrz_M3']['_XYCoordinates'] = tmpXY

        ##### BND_CompOut_Vtc_M2
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CompOutTreeBufIn_Vtc_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_SARLogicWtBuffers', 'SRF_SARLogicWtCLKTree', 'SRF_CLKBufferTree_Bot',
                                   'SRF_CLKBuf1Inv_Stage1', 'SRF_InputViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        tmp2 = self.get_param_KJH4('SRF_SARLogicWtBuffers', 'SRF_SARLogicWtCLKTree', 'SRF_CLKBufferTree_Bot',
                                   'BND_Buf1Stg2to1_Hrz_M3')
        self._DesignParameter['BND_CompOutTreeBufIn_Vtc_M2']['_YWidth'] = abs(
            tmp2[0][0][0][0][0]['_XY_down'][1] - tmp1[0][0][0][0][0][0][0][0]['_XY_up'][1]) + CompOutSARLogicTreeBufInHrzMetalWidth + SpaceBtwTreeInternalRoutePathAndCompOut

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CompOutTreeBufIn_Vtc_M2']['_XWidth'] = tmp1[0][0][0][0][0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CompOutTreeBufIn_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CompOutTreeBufIn_Vtc_M2')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CompOutTreeBufIn_Vtc_M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CompOutTreeBufIn_Vtc_M2']['_XYCoordinates'] = tmpXY

        ###### BND_CompOutTreeBufIn_Vtc_M2 -> BND_CompOutTreeBufIn_Hrz_M3 ViaM2M3
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CompOutTreeBufIn_ViaM2M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_CompOutTreeBufIn_ViaM2M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CompOutTreeBufIn_ViaM2M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CompOutTreeBufIn_ViaM2M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CompOutTreeBufIn_ViaM2M3']['_DesignObj']._CalculateDesignParameterYmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CompOutTreeBufIn_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_CompOutTreeBufIn_Vtc_M2')
        target_coord = tmp1[0][0]['_XY_down_right']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CompOutTreeBufIn_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CompOutTreeBufIn_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CompOutTreeBufIn_ViaM2M3']['_XYCoordinates'] = tmpXY

        ##### BND_CompOutTreeBufIn_Hrz_M3
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CompOutTreeBufIn_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('BND_CompOutTreeBufIn_Vtc_M2')
        tmp2 = self.get_param_KJH4('SRF_Buf_CompOut', 'SRF_Output_ViaM2Mx', 'SRF_ViaM2M3',
                                   'BND_Met2Layer')
        self._DesignParameter['BND_CompOutTreeBufIn_Hrz_M3']['_XWidth'] = abs(
            tmp1[0][0]['_XY_right'][0] - tmp2[0][0][0][0][0]['_XY_right'][0])

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_CompOutTreeBufIn_Hrz_M3']['_YWidth'] = CompOutSARLogicTreeBufInHrzMetalWidth

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CompOutTreeBufIn_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0]['_XY_down_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CompOutTreeBufIn_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_down_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CompOutTreeBufIn_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CompOutTreeBufIn_Hrz_M3']['_XYCoordinates'] = tmpXY

        ###### SRF_BufCompOutBufOutput_ViaM3M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_BufCompOutBufOutput_ViaM3M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_BufCompOutBufOutput_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_BufCompOutBufOutput_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_BufCompOutBufOutput_ViaM3M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_BufCompOutBufOutput_ViaM3M4']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_BufCompOutBufOutput_ViaM3M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_CompOutTreeBufIn_Hrz_M3')
        target_coord = tmp1[0][0]['_XY_up_left']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_BufCompOutBufOutput_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_BufCompOutBufOutput_ViaM3M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_BufCompOutBufOutput_ViaM3M4']['_XYCoordinates'] = tmpXY

        ##### BND_BufCompOutBufOutput_Vtc_M4
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_BufCompOutBufOutput_Vtc_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_CompOutTreeBufIn_Hrz_M3')
        tmp2 = self.get_param_KJH4('SRF_Buf_CompOut', 'SRF_Output_ViaM2Mx', 'SRF_ViaM2M3', 'BND_Met2Layer')
        self._DesignParameter['BND_BufCompOutBufOutput_Vtc_M4']['_YWidth'] = abs(
            tmp2[0][0][0][0][0]['_XY_up'][1] - tmp1[0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_BufCompOutBufOutput_Vtc_M4']['_XWidth'] = CompOutBufOutputVtcM4Width

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_BufCompOutBufOutput_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_BufCompOutBufOutput_Vtc_M4')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_BufCompOutBufOutput_Vtc_M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_BufCompOutBufOutput_Vtc_M4']['_XYCoordinates'] = tmpXY

        ##################################### CLKDout Routing #######################
        ##### BND_CLKDOut_Vtc_M2
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CLKDOut_Vtc_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_SARLogicWtBuffers', 'SRF_SARLogicWtCLKTree', 'SRF_CLKBufferTree_Bot',
                                   'SRF_CLKBuf2Inv_Stage1', 'SRF_InputViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        tmp2 = self.get_param_KJH4('SRF_SARLogicWtBuffers', 'SRF_SARLogicWtCLKTree', 'SRF_CLKBufferTree_Bot',
                                   'BND_Buf1Stg2to1_Hrz_M3')
        self._DesignParameter['BND_CLKDOut_Vtc_M2']['_YWidth'] = abs(
            tmp2[0][0][0][0][0]['_XY_down'][1] - tmp1[0][0][0][0][0][0][0][0]['_XY_up'][1]) + CompOutSARLogicTreeBufInHrzMetalWidth + SpaceBtwTreeInternalRoutePathAndCompOut + CLKDoutMetalWidth + SpaceBtwCompOutAndCLKDout

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CLKDOut_Vtc_M2']['_XWidth'] = tmp1[0][0][0][0][0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CLKDOut_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CLKDOut_Vtc_M2')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CLKDOut_Vtc_M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CLKDOut_Vtc_M2']['_XYCoordinates'] = tmpXY

        ### BND_CLKDoutANDOut_Vtc_M4
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CLKDoutANDOut_Vtc_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_SARLogicWtBuffers', 'SRF_CLKDoutANDOut_ViaM2M4', 'SRF_ViaM2M3', 'BND_Met2Layer')
        tmp2 = self.get_param_KJH4('BND_CLKDOut_Vtc_M2')
        self._DesignParameter['BND_CLKDoutANDOut_Vtc_M4']['_YWidth'] = abs(
            tmp1[0][0][0][0][0]['_XY_up'][1] - tmp2[0][0]['_XY_down'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CLKDoutANDOut_Vtc_M4']['_XWidth'] = 50

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CLKDoutANDOut_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0]['_XY_up_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CLKDoutANDOut_Vtc_M4')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CLKDoutANDOut_Vtc_M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CLKDoutANDOut_Vtc_M4']['_XYCoordinates'] = tmpXY

        ##### SRF_CLKDoutTreeBufIn_Vtc_M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 3

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKDoutTreeBufIn_ViaM3M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_CLKDoutTreeBufIn_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKDoutTreeBufIn_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKDoutTreeBufIn_ViaM3M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKDoutTreeBufIn_ViaM3M4']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKDoutTreeBufIn_ViaM3M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_CLKDoutANDOut_Vtc_M4')
        target_coord = tmp1[0][0]['_XY_down']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CLKDoutTreeBufIn_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKDoutTreeBufIn_ViaM3M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKDoutTreeBufIn_ViaM3M4']['_XYCoordinates'] = tmpXY

        ### BND_CLKDoutANDOut_Hrz_M3
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CLKDoutANDOut_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('BND_CLKDoutANDOut_Vtc_M4')
        tmp2 = self.get_param_KJH4('BND_CLKDOut_Vtc_M2')
        self._DesignParameter['BND_CLKDoutANDOut_Hrz_M3']['_XWidth'] = abs(
            tmp1[0][0]['_XY_right'][0] - tmp2[0][0]['_XY_left'][0])

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_CLKDoutANDOut_Hrz_M3']['_YWidth'] = 100

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CLKDoutANDOut_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0]['_XY_down_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CLKDoutANDOut_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_down_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CLKDoutANDOut_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CLKDoutANDOut_Hrz_M3']['_XYCoordinates'] = tmpXY

        ##### SRF_CLKDoutANDOut_ViaM2M3
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKDoutANDOut_ViaM2M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_CLKDoutANDOut_ViaM2M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKDoutANDOut_ViaM2M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKDoutANDOut_ViaM2M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKDoutANDOut_ViaM2M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKDoutANDOut_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_CLKDoutANDOut_Hrz_M3')
        target_coord = tmp1[0][0]['_XY_down_left']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CLKDoutANDOut_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKDoutANDOut_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKDoutANDOut_ViaM2M3']['_XYCoordinates'] = tmpXY

        ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
        ###### BND Nwell Extension
        ## NWELL Extension On CompOut Buffer
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NWellOnCompOutBuf'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Buf_CompOut', 'SRF_INV0', 'BND_PMOS_NellExten')
        tmp2 = self.get_param_KJH4('SRF_SARLogicWtBuffers', 'SRF_LowerCDACPreDriver', 'BND_Nbody_NwellExten')
        self._DesignParameter['BND_NWellOnCompOutBuf']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_NWellOnCompOutBuf']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NWellOnCompOutBuf']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NWellOnCompOutBuf')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NWellOnCompOutBuf')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_NWellOnCompOutBuf']['_XYCoordinates'] = tmpXY

        ## NWELL Extension On CLKSamp Buffer And CLKSrc Buffer
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NWellOnCLKSampBuf'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Buf_CLKSrc', 'SRF_INV2', 'BND_PMOS_NellExten')
        tmp2 = self.get_param_KJH4('SRF_SARLogicWtBuffers', 'SRF_UpperCDACPreDriver', 'BND_Nbody_NwellExten')
        self._DesignParameter['BND_NWellOnCLKSampBuf']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_NWellOnCLKSampBuf']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NWellOnCLKSampBuf']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NWellOnCLKSampBuf')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NWellOnCLKSampBuf')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_NWellOnCLKSampBuf']['_XYCoordinates'] = tmpXY

        # # SARLogic & Comparator 가운데 Nwell 전체를 덮는 NWELL
        # ## NWELL Extension On CLKSamp Buffer And CLKSrc Buffer
        #     ## Boundary_element Generation
        #         ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        # self._DesignParameter['BND_NWellOnComparatorAndSARLogic'] = self._BoundaryElementDeclaration(
        # _Layer=DesignParameters._LayerMapping['NWELL'][0],
        # _Datatype=DesignParameters._LayerMapping['NWELL'][1],
        # _XWidth=None,
        # _YWidth=None,
        # _XYCoordinates=[],
        # )
        #         ## Define Boundary_element _YWidth
        # tmp1 = self.get_param_KJH4('SRF_Comparator','BND_NWellOnCLKInLogic')
        # tmp2 = self.get_param_KJH4('SRF_SARLogicWtBuffers','BND_NWellOnCLKDoutANDInv')
        # tmpUp = max(tmp1[0][0][0]['_XY_up'][1], tmp2[0][0][0]['_XY_up'][1])
        # tmpDn = min(tmp1[0][0][0]['_XY_down'][1], tmp2[0][0][0]['_XY_down'][1])
        # self._DesignParameter['BND_NWellOnComparatorAndSARLogic']['_YWidth'] = abs(tmpUp - tmpDn)
        #
        #         ## Define Boundary_element _XWidth
        # self._DesignParameter['BND_NWellOnComparatorAndSARLogic']['_XWidth'] = abs(tmp1[0][0][0]['_XY_left'][0] - tmp2[0][0][0]['_XY_right'][0])
        #
        #         ## Define Boundary_element _XYCoordinates
        # self._DesignParameter['BND_NWellOnComparatorAndSARLogic']['_XYCoordinates'] = [[0, 0]]
        #
        #             ## Calculate Sref XYcoord
        # tmpXY = []
        #                 ## Calculate
        #                     ## Target_coord: _XY_type1
        # target_coord = [tmp1[0][0][0]['_XY_left'][0], tmpUp]
        #                     ## Approaching_coord: _XY_type2
        # tmp2 = self.get_param_KJH4('BND_NWellOnComparatorAndSARLogic')
        # approaching_coord = tmp2[0][0]['_XY_up_left']
        #                     ## Sref coord
        # tmp3 = self.get_param_KJH4('BND_NWellOnComparatorAndSARLogic')
        # Scoord = tmp3[0][0]['_XY_origin']
        #                     ## Cal
        # New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        # tmpXY.append(New_Scoord)
        #                     ## Define coordinates
        # self._DesignParameter['BND_NWellOnComparatorAndSARLogic']['_XYCoordinates'] = tmpXY

        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')


############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_YJH
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ADC_L00_SARLogicWtConmparator'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'L00_00_SARLogicWtComparator'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        _NumofBit=3,

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
        _SARLogic_CLKBufTreeTop_CLKSampBuf_SizeByStage=[1, 2, 4, 8],
        _SARLogic_CLKBufTreeTop_CLKSrcBuf_SizeByStage=[1, 2, 4, 8],  # 스테이지에 따른 버퍼 사이즈(UnitBuffer의 배수로 각 스테이지의 크기가 결정 됨.)
        _SARLogic_CLKBufTreeTop_XOffSet=-0,

        ## Top CLK Buffer Tree Size
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
        _SARLogic_CLKBufTreeTop_PMOSXvt2NMOSXvt=446,

        # Bottom Clock  Tree Size
        _SARLogic_CLKBufTreeBot_NumOfStage=4,
        _SARLogic_CLKBufTreeBot_CompOutBuf_SizeByStage=[1, 2, 4, 8],
        _SARLogic_CLKBufTreeBot_CLKDoutBuf_SizeByStage=[1, 2, 4, 8],  # 스테이지에 따른 버퍼 사이즈(UnitBuffer의 배수로 각 스테이지의 크기가 결정 됨.)
        _SARLogic_CLKBufTreeBot_XOffSet=0,

        ## Bottom CLK Buffer Tree Size
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
        _SARLogic_CLKBufTreeBot_PMOSXvt2NMOSXvt=446,

        #### CDAC Pre-Driver Sizing
        ## InvChain Common
        _CDACPreDriver_Pbody_NumCont=2,  # number
        _CDACPreDriver_Nbody_NumCont=2,  # number
        _CDACPreDriver_PMOSXvt2NMOSXvt=500,  # number
        _CDACPreDriver_XvtTop2Pbody=None,  # number/None(Minimum)
        _CDACPreDriver_Xvtdown2Nbody=None,  # number/None(Minimum)

        ## Inverter Chain
        ## Inv1 common
        _CDACPreDriver_NumberofGate=[1, 4, 16, 64],  # Vector
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

        ## StrongARM Latch
        _Comp_SALatch_CLKinputPMOSFinger1=6,  # random.randint(1, 15),  # 6
        _Comp_SALatch_CLKinputPMOSFinger2=3,  # random.randint(1, 15),  # 3
        _Comp_SALatch_PMOSFinger=3,  # random.randint(1, 15),  # 3
        _Comp_SALatch_PMOSChannelWidth=500,  # random.randrange(200, 1050, 2),  # 500
        _Comp_SALatch_DATAinputNMOSFinger=12,  # random.randint(3, 15),  # 12
        _Comp_SALatch_NMOSFinger=2,  # random.randint(1, 15),  # 2
        _Comp_SALatch_CLKinputNMOSFinger=8,  # random.randint(1, 15),  # 8
        _Comp_SALatch_NMOSChannelWidth=500,  # random.randrange(200, 1050, 2),  # 500
        _Comp_SALatch_CLKinputNMOSChannelWidth=800,  # random.randrange(200, 1050, 2),  # 800
        _Comp_SALatch_ChannelLength=30,  # random.randrange(30, 60, 2),  # 30
        _Comp_SALatch_Dummy=True,
        _Comp_SALatch_XVT='SLVT',
        _Comp_SALatch_GuardringWidth=200,
        _Comp_SALatch_Guardring=True,
        _Comp_SALatch_SlicerGuardringWidth=200,
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
        _Comp_SAOutBuf_Inv1_NMOS_ChannelWidth=400,  # Number
        _Comp_SAOutBuf_Inv1_NMOS_ChannelLength=30,  # Number
        _Comp_SAOutBuf_Inv1_NMOS_NumberofGate=1,  # Number
        _Comp_SAOutBuf_Inv1_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_SAOutBuf_Inv1_NMOS_POGate_Comb_length=100,  # None/Number

        _Comp_SAOutBuf_Inv1_PMOS_ChannelWidth=800,  # Number
        _Comp_SAOutBuf_Inv1_PMOS_ChannelLength=30,  # Number
        _Comp_SAOutBuf_Inv1_PMOS_NumberofGate=1,  # Number
        _Comp_SAOutBuf_Inv1_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_SAOutBuf_Inv1_PMOS_POGate_Comb_length=100,  # None/Number

        # Inverter2
        _Comp_SAOutBuf_Inv2_NMOS_ChannelWidth=400,  # Number
        _Comp_SAOutBuf_Inv2_NMOS_ChannelLength=30,  # Number
        _Comp_SAOutBuf_Inv2_NMOS_NumberofGate=1,  # Number
        _Comp_SAOutBuf_Inv2_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_SAOutBuf_Inv2_NMOS_POGate_Comb_length=100,  # None/Number

        _Comp_SAOutBuf_Inv2_PMOS_ChannelWidth=800,  # Number
        _Comp_SAOutBuf_Inv2_PMOS_ChannelLength=30,  # Number
        _Comp_SAOutBuf_Inv2_PMOS_NumberofGate=1,  # Number
        _Comp_SAOutBuf_Inv2_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_SAOutBuf_Inv2_PMOS_POGate_Comb_length=100,  # None/Number

        ## SR Latch Size
        _Comp_SRLatch_NAND_NMOS_ChannelWidth=400,  # Number
        _Comp_SRLatch_NAND_NMOS_ChannelLength=30,  # Number
        _Comp_SRLatch_NAND_NMOS_NumberofGate=2,  # Number
        _Comp_SRLatch_NAND_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_SRLatch_NAND_NMOS_POGate_Comb_length=100,  # None/Number

        _Comp_SRLatch_NAND_PMOS_ChannelWidth=800,  # Number
        _Comp_SRLatch_NAND_PMOS_ChannelLength=30,  # Number
        _Comp_SRLatch_NAND_PMOS_NumberofGate=1,  # Number
        _Comp_SRLatch_NAND_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_SRLatch_NAND_PMOS_POGate_Comb_length=100,  # None/Number

        # CLK Input Logic Gates
        _Comp_CLKSamp_Inv_NMOS_ChannelWidth=400,
        _Comp_CLKSamp_Inv_NMOS_ChannelLength=30,
        _Comp_CLKSamp_Inv_NMOS_NumberofGate=2,
        _Comp_CLKSamp_Inv_NMOS_XVT='SLVT',
        _Comp_CLKSamp_Inv_NMOS_POGate_Comb_length=100,

        _Comp_CLKSamp_Inv_PMOS_ChannelWidth=800,
        _Comp_CLKSamp_Inv_PMOS_ChannelLength=30,
        _Comp_CLKSamp_Inv_PMOS_NumberofGate=1,
        _Comp_CLKSamp_Inv_PMOS_XVT='SLVT',
        _Comp_CLKSamp_Inv_PMOS_POGate_Comb_length=100,

        _Comp_CLKSrc_Inv_NMOS_ChannelWidth=400,
        _Comp_CLKSrc_Inv_NMOS_ChannelLength=30,
        _Comp_CLKSrc_Inv_NMOS_NumberofGate=1,
        _Comp_CLKSrc_Inv_NMOS_XVT='SLVT',
        _Comp_CLKSrc_Inv_NMOS_POGate_Comb_length=100,

        _Comp_CLKSrc_Inv_PMOS_ChannelWidth=800,
        _Comp_CLKSrc_Inv_PMOS_ChannelLength=30,
        _Comp_CLKSrc_Inv_PMOS_NumberofGate=1,
        _Comp_CLKSrc_Inv_PMOS_XVT='SLVT',
        _Comp_CLKSrc_Inv_PMOS_POGate_Comb_length=100,

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
        _Comp_AND_Inv_NMOS_POGate_Comb_length=100,

        _Comp_AND_Inv_PMOS_ChannelWidth=800,
        _Comp_AND_Inv_PMOS_ChannelLength=30,
        _Comp_AND_Inv_PMOS_NumberofGate=1,
        _Comp_AND_Inv_PMOS_XVT='SLVT',
        _Comp_AND_Inv_PMOS_POGate_Comb_length=100,

        ## CLK Buffer
        # Inverter1
        _Comp_CLKBuf_Inv1_NMOS_ChannelWidth=400,  # Number
        _Comp_CLKBuf_Inv1_NMOS_ChannelLength=30,  # Number
        _Comp_CLKBuf_Inv1_NMOS_NumberofGate=2,  # Number
        _Comp_CLKBuf_Inv1_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_CLKBuf_Inv1_NMOS_POGate_Comb_length=100,  # None/Number

        _Comp_CLKBuf_Inv1_PMOS_ChannelWidth=800,  # Number
        _Comp_CLKBuf_Inv1_PMOS_ChannelLength=30,  # Number
        _Comp_CLKBuf_Inv1_PMOS_NumberofGate=2,  # Number
        _Comp_CLKBuf_Inv1_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_CLKBuf_Inv1_PMOS_POGate_Comb_length=100,  # None/Number

        # Inverter2
        _Comp_CLKBuf_Inv2_NMOS_ChannelWidth=400,  # Number
        _Comp_CLKBuf_Inv2_NMOS_ChannelLength=30,  # Number
        _Comp_CLKBuf_Inv2_NMOS_NumberofGate=4,  # Number
        _Comp_CLKBuf_Inv2_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_CLKBuf_Inv2_NMOS_POGate_Comb_length=100,  # None/Number

        _Comp_CLKBuf_Inv2_PMOS_ChannelWidth=800,  # Number
        _Comp_CLKBuf_Inv2_PMOS_ChannelLength=30,  # Number
        _Comp_CLKBuf_Inv2_PMOS_NumberofGate=4,  # Number
        _Comp_CLKBuf_Inv2_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Comp_CLKBuf_Inv2_PMOS_POGate_Comb_length=100,  # None/Number

        # PowerRail Placement
        _Comp_BufSR_NMOS_Pbody_NumCont=2,
        _Comp_BufSR_NMOS_Pbody_XvtTop2Pbody=600,
        _Comp_BufSR_PMOS_Nbody_NumCont=2,
        _Comp_BufSR_PMOS_Nbody_Xvtdown2Nbody=1000,
        _Comp_BufSR_PMOSXvt2NMOSXvt=1000,

        _Comp_CLKInLogic_NMOS_Pbody_Xvtdown2Pbody=1000,
        _Comp_CLKInLogic_PMOS_Nbody_NumCont=2,
        _Comp_CLKInLogic_PMOS_Nbody_Xvtdown2Nbody=1000,
        _Comp_CLKInLogic_PMOSXvt2NMOSXvt=1000,

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
    LayoutObj = _SARLogicWtComparator(_DesignParameter=None, _Name=cellname)
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
