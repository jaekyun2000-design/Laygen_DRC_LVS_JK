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

from KJH91_Projects.Project_ADC.Layoutgen_code.K00_SARLogicWtBuffers_RCHybrid_Fixed                     import K00_02_SARLogicWtCDACPreDriver_YJH
from KJH91_Projects.Project_ADC.Layoutgen_code.E01_ComparatorWtLatch_Fixed                              import E01_05_StrongArmWtSRLatch
from KJH91_Projects.Project_ADC.Layoutgen_code.J00_CDACPreDriver_InvBuffer_KJH0_RCHybrid_Fixed          import J00_01_InverterChain_KJH


## Define Class
class _SARLogicWtComparator(StickDiagram_KJH1._StickDiagram_KJH):
    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
_NumofBit = 12,

## SAR Logic
    ## Clock Tree (Driving SAR Logic)
        ## Clock Tree Updward (CLK Source Tree, CLK Samp Tree)
            ## CLK Buffer Unit
                ## Common
                _LOGIC_CLKBufTreeTop_UnitBuf_XVT='SLVT',
                ## Nmos
                _LOGIC_CLKBufTreeTop_UnitBuf_NMOS_NumberofGate=1,  # Number
                _LOGIC_CLKBufTreeTop_UnitBuf_NMOS_ChannelWidth=400,  # Number
                _LOGIC_CLKBufTreeTop_UnitBuf_NMOS_ChannelLength=30,  # Number
                ## Pmos
                _LOGIC_CLKBufTreeTop_UnitBuf_PMOS_NumberofGate=1,  # Number
                _LOGIC_CLKBufTreeTop_UnitBuf_PMOS_ChannelWidth=800,  # Number
                _LOGIC_CLKBufTreeTop_UnitBuf_PMOS_ChannelLength=30,  # Number
                # Height
                _LOGIC_CLKBufTreeTop_UnitBuf_PMOSXvt2NMOSXvt=446,  # number
            ## Clock Buffer Tree structure
            _LOGIC_CLKBufTreeTop_BufTree1and2_NumOfStage=4,  # len[Buf0, Buf1, ... ] 스테이지 수 (아래 버퍼 사이즈 리스트의 길이와 같아야 함.)
            _LOGIC_CLKBufTreeTop_BufTree1_SizeofEachStage=[1, 2, 4, 8],  # CLKSampBuf: [Buf0, Buf1, Buf2 ...]
            _LOGIC_CLKBufTreeTop_BufTree2_SizeofEachStage=[1, 2, 4, 8],  # CLKSrcBuf: [Buf0, Buf1, Buf2 ...]
            _LOGIC_CLKBufTreeTop_XOffSet=0,
        ## Clock Tree Dnward (CLK Source Tree, CLK Samp Tree)
            ## CLK Buffer Unit
                ## Common
                _LOGIC_CLKBufTreeBot_UnitBuf_XVT='SLVT',
                ## Nmos
                _LOGIC_CLKBufTreeBot_UnitBuf_NMOS_NumberofGate=1,  # Number
                _LOGIC_CLKBufTreeBot_UnitBuf_NMOS_ChannelWidth=400,  # Number
                _LOGIC_CLKBufTreeBot_UnitBuf_NMOS_ChannelLength=30,  # Number
                ## Pmos
                _LOGIC_CLKBufTreeBot_UnitBuf_PMOS_NumberofGate=1,  # Number
                _LOGIC_CLKBufTreeBot_UnitBuf_PMOS_ChannelWidth=800,  # Number
                _LOGIC_CLKBufTreeBot_UnitBuf_PMOS_ChannelLength=30,  # Number
                # Height
                _LOGIC_CLKBufTreeBot_UnitBuf_PMOSXvt2NMOSXvt=446,  # number
            ## Clock Buffer Tree structure
            _LOGIC_CLKBufTreeBot_BufTree1and2_NumOfStage=4,  # len[Buf0, Buf1, ... ] 스테이지 수 (아래 버퍼 사이즈 리스트의 길이와 같아야 함.)
            _LOGIC_CLKBufTreeBot_BufTree1_SizeofEachStage=[1, 2, 4, 8],  # CompOutBuf: [Buf0, Buf1, Buf2 ...]
            _LOGIC_CLKBufTreeBot_BufTree2_SizeofEachStage=[1, 2, 4, 8],  # CLKDoutBuf: [Buf0, Buf1, Buf2 ...]
            _LOGIC_CLKBufTreeBot_XOffSet=0,

    ## Clock Spine (Physical demension)
        ## CLK Source: upward, 1st floor
        _LOGIC_YWidthOfCLKSrc=100,
        ## CLK Samp: upward, 2nd floor
        _LOGIC_SpaceBtwCLKSrcAndCLKSamp=100,
        _LOGIC_YWidthOfCLKSamp=100,
        ## Comparator Output: downward, Basement1
        _LOGIC_YWidthOfCompOut=100,
        ## CLK Dout: downward, basement2
        _LOGIC_SpaceBtwCompOutAndCLKDout=100,
        _LOGIC_YWidthOfCLKDout=100,

    ## SetResetDFF
        ## DFF Common
        _LOGIC_Test_distance=320,
        _LOGIC_DFF_PMOSXvt2NMOSXvt    = 1150, # number

        ## Master Xgate1
            ## Xgate common
            _LOGIC_Mst_Xgate1_XVT='SLVT',
            ## Xgate NMOS
            _LOGIC_Mst_Xgate1_NMOS_NumberofGate=1,
            _LOGIC_Mst_Xgate1_NMOS_ChannelWidth=300,
            _LOGIC_Mst_Xgate1_NMOS_ChannelLength=30,
            ## Xgate PMOS
            _LOGIC_Mst_Xgate1_PMOS_NumberofGate=3,
            _LOGIC_Mst_Xgate1_PMOS_ChannelWidth=500,
            _LOGIC_Mst_Xgate1_PMOS_ChannelLength=30,

        ## Master Xgate2
            ## Xgate common
            _LOGIC_Mst_Xgate2_XVT='SLVT',
            ## Xgate NMOS
            _LOGIC_Mst_Xgate2_NMOS_NumberofGate           = 2,
            _LOGIC_Mst_Xgate2_NMOS_ChannelWidth           = 800,
            _LOGIC_Mst_Xgate2_NMOS_ChannelLength          = 30,
            ## Xgate PMOS
            _LOGIC_Mst_Xgate2_PMOS_NumberofGate           = 3,
            _LOGIC_Mst_Xgate2_PMOS_ChannelWidth           = 200,
            _LOGIC_Mst_Xgate2_PMOS_ChannelLength          = 30,

        ## Master Nor1
            ## Nor1 common
            _LOGIC_Mst_Nor1_XVT='SLVT',
            ## NMOS
                ## NMOSA
                _LOGIC_Mst_Nor1_NMOSA_NumberofGate           = 2,
                _LOGIC_Mst_Nor1_NMOSA_ChannelWidth           = 800,
                _LOGIC_Mst_Nor1_NMOSA_ChannelLength          = 30,
                ## NMOSB
                _LOGIC_Mst_Nor1_NMOSB_NumberofGate           = 3,
                _LOGIC_Mst_Nor1_NMOSB_ChannelWidth           = 200,
                _LOGIC_Mst_Nor1_NMOSB_ChannelLength          = 30,
            ## PMOS
                ## PMOSA
                _LOGIC_Mst_Nor1_PMOSA_NumberofGate            = 2,
                _LOGIC_Mst_Nor1_PMOSA_ChannelWidth            = 800,
                _LOGIC_Mst_Nor1_PMOSA_ChannelLength           = 30,
                ## PMOSB
                _LOGIC_Mst_Nor1_PMOSB_NumberofGate            = 3,
                _LOGIC_Mst_Nor1_PMOSB_ChannelWidth            = 200,
                _LOGIC_Mst_Nor1_PMOSB_ChannelLength           = 30,

        ## Master Nor2
            ## Nor2 common
            _LOGIC_Mst_Nor2_XVT='SLVT',
            ## NMOS
                ## NMOSA
                _LOGIC_Mst_Nor2_NMOSA_NumberofGate           = 2,
                _LOGIC_Mst_Nor2_NMOSA_ChannelWidth           = 800,
                _LOGIC_Mst_Nor2_NMOSA_ChannelLength          = 30,
                ## NMOSB
                _LOGIC_Mst_Nor2_NMOSB_NumberofGate           = 3,
                _LOGIC_Mst_Nor2_NMOSB_ChannelWidth           = 200,
                _LOGIC_Mst_Nor2_NMOSB_ChannelLength          = 30,
            ## PMOS
                ## PMOSA
                _LOGIC_Mst_Nor2_PMOSA_NumberofGate            = 2,
                _LOGIC_Mst_Nor2_PMOSA_ChannelWidth            = 800,
                _LOGIC_Mst_Nor2_PMOSA_ChannelLength           = 30,
                ## PMOSB
                _LOGIC_Mst_Nor2_PMOSB_NumberofGate            = 3,
                _LOGIC_Mst_Nor2_PMOSB_ChannelWidth            = 200,
                _LOGIC_Mst_Nor2_PMOSB_ChannelLength           = 30,

        ## Master Inv1 : Set pre-driver
            ## Inv1 common
            _LOGIC_Mst_Inv1_XVT='SLVT',
            ## Inv1 NMOS
            _LOGIC_Mst_Inv1_NMOS_NumberofGate           = 1,
            _LOGIC_Mst_Inv1_NMOS_ChannelWidth           = 300,
            _LOGIC_Mst_Inv1_NMOS_ChannelLength          = 30,
            ## Inv1 PMOS
            _LOGIC_Mst_Inv1_PMOS_NumberofGate           = 3,
            _LOGIC_Mst_Inv1_PMOS_ChannelWidth           = 500,
            _LOGIC_Mst_Inv1_PMOS_ChannelLength          = 30,

        ## Master Inv2 : Set driver
            ## Inv2 common
            _LOGIC_Mst_Inv2_XVT='SLVT',
            ## Inv2 NMOS
            _LOGIC_Mst_Inv2_NMOS_NumberofGate           = 1,
            _LOGIC_Mst_Inv2_NMOS_ChannelWidth           = 300,
            _LOGIC_Mst_Inv2_NMOS_ChannelLength          = 30,
            ## Inv2 PMOS
            _LOGIC_Mst_Inv2_PMOS_NumberofGate           = 3,
            _LOGIC_Mst_Inv2_PMOS_ChannelWidth           = 500,
            _LOGIC_Mst_Inv2_PMOS_ChannelLength          = 30,

        ## Master Inv3 : Clock driver
            ## Inv3 common
            _LOGIC_Mst_Inv3_XVT='SLVT',
            ## Inv3 NMOS
            _LOGIC_Mst_Inv3_NMOS_NumberofGate           = 1,
            _LOGIC_Mst_Inv3_NMOS_ChannelWidth           = 300,
            _LOGIC_Mst_Inv3_NMOS_ChannelLength          = 30,
            ## Inv3 PMOS
            _LOGIC_Mst_Inv3_PMOS_NumberofGate           = 3,
            _LOGIC_Mst_Inv3_PMOS_ChannelWidth           = 500,
            _LOGIC_Mst_Inv3_PMOS_ChannelLength          = 30,

        ## Slave Xgate1
            ## Xgate common
            _LOGIC_Slv_Xgate1_XVT='SLVT',
            ## Xgate NMOS
            _LOGIC_Slv_Xgate1_NMOS_NumberofGate           = 1,
            _LOGIC_Slv_Xgate1_NMOS_ChannelWidth           = 300,
            _LOGIC_Slv_Xgate1_NMOS_ChannelLength          = 30,
            ## Xgate PMOS
            _LOGIC_Slv_Xgate1_PMOS_NumberofGate           = 3,
            _LOGIC_Slv_Xgate1_PMOS_ChannelWidth           = 500,
            _LOGIC_Slv_Xgate1_PMOS_ChannelLength          = 30,

        ## Slave Xgate2
            ## Xgate common
            _LOGIC_Slv_Xgate2_XVT='SLVT',
            ## Xgate NMOS
            _LOGIC_Slv_Xgate2_NMOS_NumberofGate           = 2,
            _LOGIC_Slv_Xgate2_NMOS_ChannelWidth           = 800,
            _LOGIC_Slv_Xgate2_NMOS_ChannelLength          = 30,
            ## Xgate PMOS
            _LOGIC_Slv_Xgate2_PMOS_NumberofGate           = 3,
            _LOGIC_Slv_Xgate2_PMOS_ChannelWidth           = 200,
            _LOGIC_Slv_Xgate2_PMOS_ChannelLength          = 30,

        ## Slave Nor1
            ## Nor1 common
            _LOGIC_Slv_Nor1_XVT='SLVT',
            ## NMOS
                ## NMOSA
                _LOGIC_Slv_Nor1_NMOSA_NumberofGate           = 2,
                _LOGIC_Slv_Nor1_NMOSA_ChannelWidth           = 800,
                _LOGIC_Slv_Nor1_NMOSA_ChannelLength          = 30,
                ## NMOSB
                _LOGIC_Slv_Nor1_NMOSB_NumberofGate           = 3,
                _LOGIC_Slv_Nor1_NMOSB_ChannelWidth           = 200,
                _LOGIC_Slv_Nor1_NMOSB_ChannelLength          = 30,
            ## PMOS
                ## PMOSA
                _LOGIC_Slv_Nor1_PMOSA_NumberofGate            = 2,
                _LOGIC_Slv_Nor1_PMOSA_ChannelWidth            = 800,
                _LOGIC_Slv_Nor1_PMOSA_ChannelLength           = 30,
                ## PMOSB
                _LOGIC_Slv_Nor1_PMOSB_NumberofGate            = 3,
                _LOGIC_Slv_Nor1_PMOSB_ChannelWidth            = 200,
                _LOGIC_Slv_Nor1_PMOSB_ChannelLength           = 30,

        ## Slave Nor2
            ## Nor2 common
            _LOGIC_Slv_Nor2_XVT='SLVT',
            ## NMOS
                ## NMOSA
                _LOGIC_Slv_Nor2_NMOSA_NumberofGate           = 2,
                _LOGIC_Slv_Nor2_NMOSA_ChannelWidth           = 800,
                _LOGIC_Slv_Nor2_NMOSA_ChannelLength          = 30,
                ## NMOSB
                _LOGIC_Slv_Nor2_NMOSB_NumberofGate           = 3,
                _LOGIC_Slv_Nor2_NMOSB_ChannelWidth           = 200,
                _LOGIC_Slv_Nor2_NMOSB_ChannelLength          = 30,
            ## PMOS
                ## PMOSA
                _LOGIC_Slv_Nor2_PMOSA_NumberofGate            = 2,
                _LOGIC_Slv_Nor2_PMOSA_ChannelWidth            = 800,
                _LOGIC_Slv_Nor2_PMOSA_ChannelLength           = 30,
                ## PMOSB
                _LOGIC_Slv_Nor2_PMOSB_NumberofGate            = 3,
                _LOGIC_Slv_Nor2_PMOSB_ChannelWidth            = 200,
                _LOGIC_Slv_Nor2_PMOSB_ChannelLength           = 30,

        ## Slave Inv1 : ReSet pre-driver
            ## Inv1 common
            _LOGIC_Slv_Inv1_XVT='SLVT',
            ## Inv1 NMOS
            _LOGIC_Slv_Inv1_NMOS_NumberofGate           = 1,
            _LOGIC_Slv_Inv1_NMOS_ChannelWidth           = 300,
            _LOGIC_Slv_Inv1_NMOS_ChannelLength          = 30,
            ## Inv1 PMOS
            _LOGIC_Slv_Inv1_PMOS_NumberofGate           = 3,
            _LOGIC_Slv_Inv1_PMOS_ChannelWidth           = 500,
            _LOGIC_Slv_Inv1_PMOS_ChannelLength          = 30,

        ## Slave Inv2 : ReSet driver
            ## Inv2 common
            _LOGIC_Slv_Inv2_XVT='SLVT',
            ## Inv2 NMOS
            _LOGIC_Slv_Inv2_NMOS_NumberofGate           = 1,
            _LOGIC_Slv_Inv2_NMOS_ChannelWidth           = 300,
            _LOGIC_Slv_Inv2_NMOS_ChannelLength          = 30,
            ## Inv2 PMOS
            _LOGIC_Slv_Inv2_PMOS_NumberofGate           = 3,
            _LOGIC_Slv_Inv2_PMOS_ChannelWidth           = 500,
            _LOGIC_Slv_Inv2_PMOS_ChannelLength          = 30,

        ## Slave Inv3 : Qb driver
            ## Inv3 common
            _LOGIC_Slv_Inv3_XVT='SLVT',
            ## Inv3 NMOS
            _LOGIC_Slv_Inv3_NMOS_NumberofGate           = 1,
            _LOGIC_Slv_Inv3_NMOS_ChannelWidth           = 300,
            _LOGIC_Slv_Inv3_NMOS_ChannelLength          = 30,
            ## Inv3 PMOS
            _LOGIC_Slv_Inv3_PMOS_NumberofGate           = 3,
            _LOGIC_Slv_Inv3_PMOS_ChannelWidth           = 500,
            _LOGIC_Slv_Inv3_PMOS_ChannelLength          = 30,
## DAC PreDriver
    ## Inverter Chain
        ## InvChain Common
        _LOGIC_DACPreDrv_PMOSXvt2NMOSXvt=500,  # number
        ## Inverter Chain
            ## Inv1 common
        _LOGIC_DACPreDrv_NumberofGate=[[1, 2, 4, 8], [1, 2, 4, 8], [1, 2, 4, 8], [2, 2, 2, 2, 2]],  # Vector
        _LOGIC_DACPreDrv_ChannelLength=30,  # Scalar
        _LOGIC_DACPreDrv_XVT='SLVT',  # 'SLVT'
            ## Inv1 NMOS
        _LOGIC_DACPreDrv_Inv_NMOS_ChannelWidth=400,  # Scalar
            ## Inv1 PMOS
        _LOGIC_DACPreDrv_Inv_PMOS_ChannelWidth=800,  # Scalar
## CLKOutSamp(!=ClkSamp)
    ## Common
        # XVT
        _LOGIC_CLKoutSamp_XVT = 'SLVT',
        # Height
        # _CLKOutSamp_PMOSXvt2NMOSXvt=1800,  # number, = _DFF_PMOSXvt2NMOSXvt
    ## Inverter
        # Nmos
        _LOGIC_CLKoutSamp_Inv_NMOS_NumberofGate=1,  # Number
        _LOGIC_CLKoutSamp_Inv_NMOS_ChannelWidth=100,  # Number
        _LOGIC_CLKoutSamp_Inv_NMOS_ChannelLength=30,  # Number
        # Pmos
        _LOGIC_CLKoutSamp_Inv_PMOS_NumberofGate=1,  # Number
        _LOGIC_CLKoutSamp_Inv_PMOS_ChannelWidth=100,  # Number
        _LOGIC_CLKoutSamp_Inv_PMOS_ChannelLength=30,  # Number
    ## AND
        ## AND Common
        ## Nand
            # NmosA
            _LOGIC_CLKoutSamp_And_Nand_NMOSA_NumberofGate=1,  # Number
            _LOGIC_CLKoutSamp_And_Nand_NMOSA_ChannelWidth=100,  # Number
            _LOGIC_CLKoutSamp_And_Nand_NMOSA_ChannelLength=30,  # Number
            # NMOSB
            _LOGIC_CLKoutSamp_And_Nand_NMOSB_NumberofGate=2,  # Number
            _LOGIC_CLKoutSamp_And_Nand_NMOSB_ChannelWidth=750,  # Number
            _LOGIC_CLKoutSamp_And_Nand_NMOSB_ChannelLength=30,  # Number
            # PMOSA
            _LOGIC_CLKoutSamp_And_Nand_PMOSA_NumberofGate=1,  # Number
            _LOGIC_CLKoutSamp_And_Nand_PMOSA_ChannelWidth=300,  # Number
            _LOGIC_CLKoutSamp_And_Nand_PMOSA_ChannelLength=30,  # Number
            # PMOSB
            _LOGIC_CLKoutSamp_And_Nand_PMOSB_NumberofGate=3,  # Number
            _LOGIC_CLKoutSamp_And_Nand_PMOSB_ChannelWidth=750,  # Number
            _LOGIC_CLKoutSamp_And_Nand_PMOSB_ChannelLength=30,  # Number
        ## Inverter
            # Nmos
            _LOGIC_CLKoutSamp_And_Inv_NMOS_NumberofGate=1,  # Number
            _LOGIC_CLKoutSamp_And_Inv_NMOS_ChannelWidth=100,  # Number
            _LOGIC_CLKoutSamp_And_Inv_NMOS_ChannelLength=30,  # Number
            # Pmos
            _LOGIC_CLKoutSamp_And_Inv_PMOS_NumberofGate=1,  # Number
            _LOGIC_CLKoutSamp_And_Inv_PMOS_ChannelWidth=200,  # Number
            _LOGIC_CLKoutSamp_And_Inv_PMOS_ChannelLength=30,  # Number
## Comparator
    ## StrongARM Latch
        # Common
        _COMP_SALatch_ChannelLength=30,  # random.randrange(30, 60, 2),  # 30
        _COMP_SALatch_XVT='HVT',

        # PMOS
        _COMP_SALatch_CLKinputPMOSFinger1=1,  #PMOS Reset Sw1 # random.randint(1, 15),  # 6
        _COMP_SALatch_CLKinputPMOSFinger2=1,  #PMOS Reset Sw2 # random.randint(1, 15),  # 3
        _COMP_SALatch_PMOSFinger=1,  		  #PMOS Latch	  # random.randint(1, 15),  # 3
        _COMP_SALatch_PMOSChannelWidth=1000,  #All PMOS width # random.randrange(200, 1050, 2),  # 500

        # NMOS
        _COMP_SALatch_DATAinputNMOSFinger=3,  #NMOS Input Tr # random.randint(3, 15),  # 12
        _COMP_SALatch_NMOSFinger=2,  		  #NMOS at Latch # random.randint(1, 15),  # 2
        _COMP_SALatch_CLKinputNMOSFinger=1,  #NMOS Tail # random.randint(1, 15),  # 8
        _COMP_SALatch_NMOSChannelWidth=330,  #Nmos width # random.randrange(200, 1050, 2),  # 500
        _COMP_SALatch_CLKinputNMOSChannelWidth=200,  # random.randrange(200, 1050, 2),  # 800

    ## StrongArmOutBuffer and SRLatch
        ## Common
            # XVT
            _COMP_SAOutBufAndSRLatch_XVT='SLVT',
            # Body
            _COMP_SAOutBufAndSRLatch_NMOS_Pbody_XvtTop2Pbody=None,  # Number/None(Minimum)
            _COMP_SAOutBufAndSRLatch_PMOS_Nbody_Xvtdown2Nbody=None,  # Number/None(Minimum)
            # Height
            _COMP_SAOutBufAndSRLatch_PMOSXvt2NMOSXvt=1800,  # number
        ## StronArm Output Buffer
            ## Inverter1(pre)
                    #Nmos
                _COMP_SAOutBuf_Buf_Inv1_NMOS_NumberofGate          = 1,        # Number
                _COMP_SAOutBuf_Buf_Inv1_NMOS_ChannelWidth          = 400,      # Number
                _COMP_SAOutBuf_Buf_Inv1_NMOS_ChannelLength         = 30,       # Number
                    #Pmos
                _COMP_SAOutBuf_Buf_Inv1_PMOS_NumberofGate          = 1,        # Number
                _COMP_SAOutBuf_Buf_Inv1_PMOS_ChannelWidth          = 800,      # Number
                _COMP_SAOutBuf_Buf_Inv1_PMOS_ChannelLength         = 30,       # Number
            ## Inverter2
                    #Nmos
                _COMP_SAOutBuf_Buf_Inv2_NMOS_NumberofGate          = 2,        # Number
                _COMP_SAOutBuf_Buf_Inv2_NMOS_ChannelWidth          = 400,      # Number
                _COMP_SAOutBuf_Buf_Inv2_NMOS_ChannelLength         = 30,       # Number
                    #Pmos
                _COMP_SAOutBuf_Buf_Inv2_PMOS_NumberofGate          = 2,        # Number
                _COMP_SAOutBuf_Buf_Inv2_PMOS_ChannelWidth          = 800,      # Number
                _COMP_SAOutBuf_Buf_Inv2_PMOS_ChannelLength         = 30,       # Number
        ## SRLatch
            ## Nand(Set,Rst same)
                # NmosA
                _COMP_SRLatch_Nand_NMOSA_NumberofGate=1,  # Number
                _COMP_SRLatch_Nand_NMOSA_ChannelWidth=100,  # Number
                _COMP_SRLatch_Nand_NMOSA_ChannelLength=30,  # Number
                # NMOSB
                _COMP_SRLatch_Nand_NMOSB_NumberofGate=2,  # Number
                _COMP_SRLatch_Nand_NMOSB_ChannelWidth=750,  # Number
                _COMP_SRLatch_Nand_NMOSB_ChannelLength=30,  # Number
                # PMOSA
                _COMP_SRLatch_Nand_PMOSA_NumberofGate=2,  # Number
                _COMP_SRLatch_Nand_PMOSA_ChannelWidth=100,  # Number
                _COMP_SRLatch_Nand_PMOSA_ChannelLength=30,  # Number
                # PMOSB
                _COMP_SRLatch_Nand_PMOSB_NumberofGate=1,  # Number
                _COMP_SRLatch_Nand_PMOSB_ChannelWidth=750,  # Number
                _COMP_SRLatch_Nand_PMOSB_ChannelLength=30,  # Number

    ## Comp clock Gen Logic: Clk_Samp Inv, Clk_Source Inv, AND Gate, CompClockBuff
        ## Common
            # XVT
            _COMP_CompClkLogic_XVT='SLVT',
            # Body
            _COMP_CompClkLogic_NMOS_Pbody_XvtTop2Pbody=None,  # Number/None(Minimum)
            _COMP_CompClkLogic_PMOS_Nbody_Xvtdown2Nbody=None,  # Number/None(Minimum)
            # Height
            _COMP_CompClkLogic_PMOSXvt2NMOSXvt=1800,  # number
        ## StronArm Output Buffer
            ## Inverter1(pre)
                    #Nmos
                _COMP_CompClkLogic_Buf_Inv1_NMOS_NumberofGate          = 2,        # Number
                _COMP_CompClkLogic_Buf_Inv1_NMOS_ChannelWidth          = 400,      # Number
                _COMP_CompClkLogic_Buf_Inv1_NMOS_ChannelLength         = 30,       # Number
                    #Pmos
                _COMP_CompClkLogic_Buf_Inv1_PMOS_NumberofGate          = 2,        # Number
                _COMP_CompClkLogic_Buf_Inv1_PMOS_ChannelWidth          = 800,      # Number
                _COMP_CompClkLogic_Buf_Inv1_PMOS_ChannelLength         = 30,       # Number
            ## Inverter2
                    #Nmos
                _COMP_CompClkLogic_Buf_Inv2_NMOS_NumberofGate          = 4,        # Number
                _COMP_CompClkLogic_Buf_Inv2_NMOS_ChannelWidth          = 400,      # Number
                _COMP_CompClkLogic_Buf_Inv2_NMOS_ChannelLength         = 30,       # Number
                    #Pmos
                _COMP_CompClkLogic_Buf_Inv2_PMOS_NumberofGate          = 4,        # Number
                _COMP_CompClkLogic_Buf_Inv2_PMOS_ChannelWidth          = 800,      # Number
                _COMP_CompClkLogic_Buf_Inv2_PMOS_ChannelLength         = 30,       # Number
        ## AND
            ## Nand
                # NmosA
                _COMP_CompClkLogic_Nand_NMOSA_NumberofGate=1,  # Number
                _COMP_CompClkLogic_Nand_NMOSA_ChannelWidth=100,  # Number
                _COMP_CompClkLogic_Nand_NMOSA_ChannelLength=30,  # Number
                # NMOSB
                _COMP_CompClkLogic_Nand_NMOSB_NumberofGate=2,  # Number
                _COMP_CompClkLogic_Nand_NMOSB_ChannelWidth=750,  # Number
                _COMP_CompClkLogic_Nand_NMOSB_ChannelLength=30,  # Number
                # PMOSA
                _COMP_CompClkLogic_Nand_PMOSA_NumberofGate=1,  # Number
                _COMP_CompClkLogic_Nand_PMOSA_ChannelWidth=300,  # Number
                _COMP_CompClkLogic_Nand_PMOSA_ChannelLength=30,  # Number
                # PMOSB
                _COMP_CompClkLogic_Nand_PMOSB_NumberofGate=3,  # Number
                _COMP_CompClkLogic_Nand_PMOSB_ChannelWidth=750,  # Number
                _COMP_CompClkLogic_Nand_PMOSB_ChannelLength=30,  # Number
            ## Inverter
                # Nmos
                _COMP_CompClkLogic_Inv_NMOS_NumberofGate=1,  # Number
                _COMP_CompClkLogic_Inv_NMOS_ChannelWidth=100,  # Number
                _COMP_CompClkLogic_Inv_NMOS_ChannelLength=30,  # Number
                # Pmos
                _COMP_CompClkLogic_Inv_PMOS_NumberofGate=1,  # Number
                _COMP_CompClkLogic_Inv_PMOS_ChannelWidth=200,  # Number
                _COMP_CompClkLogic_Inv_PMOS_ChannelLength=30,  # Number

        ## Clk_Source Inv
                #Nmos
            _COMP_CompClkLogic_ClkSrc_NMOS_NumberofGate          = 1,        # Number
            _COMP_CompClkLogic_ClkSrc_NMOS_ChannelWidth          = 400,      # Number
            _COMP_CompClkLogic_ClkSrc_NMOS_ChannelLength         = 30,       # Number
                #Pmos
            _COMP_CompClkLogic_ClkSrc_PMOS_NumberofGate          = 1,        # Number
            _COMP_CompClkLogic_ClkSrc_PMOS_ChannelWidth          = 800,      # Number
            _COMP_CompClkLogic_ClkSrc_PMOS_ChannelLength         = 30,       # Number
        ## Clk_Samp Inv
                #Nmos
            _COMP_CompClkLogic_ClkSmp_NMOS_NumberofGate          = 1,        # Number
            _COMP_CompClkLogic_ClkSmp_NMOS_ChannelWidth          = 400,      # Number
            _COMP_CompClkLogic_ClkSmp_NMOS_ChannelLength         = 30,       # Number
                #Pmos
            _COMP_CompClkLogic_ClkSmp_PMOS_NumberofGate          = 1,        # Number
            _COMP_CompClkLogic_ClkSmp_PMOS_ChannelWidth          = 800,      # Number
            _COMP_CompClkLogic_ClkSmp_PMOS_ChannelLength         = 30,       # Number


## CLOCK AND DATA BUF : Comparator Dout Buf for driving Logic, CLKSamp and CLKScr Buff for Driving Sampler and Comparator
    ## Top placed
        ## CLK Samp
            ## InvChain Common
                ## Height
        _BUF_CLKSamp_PMOSXvt2NMOSXvt = 500,  # number
            ## Inverter Chain
                ## Inv1 common
        _BUF_CLKSamp_XVT='SLVT',
        _BUF_CLKSamp_NumberofGate = 3,
        _BUF_CLKSamp_ChanneLength = 30,
                ## NMOS
        _BUF_CLKSamp_NMOSChannelWidth = 784,
                ## PMOS
        _BUF_CLKSamp_PMOSChannelWidth = 833,
        ## CLK Scr
            ## InvChain Common
                ## Height
        _BUF_CLKScr_PMOSXvt2NMOSXvt = 500,  # number
            ## Inverter Chain
                ## Inv1 common
        _BUF_CLKScr_XVT='SLVT',
        _BUF_CLKScr_NumberofGate = 3,
        _BUF_CLKScr_ChanneLength = 30,
                ## NMOS
        _BUF_CLKScr_NMOSChannelWidth = 784,
                ## PMOS
        _BUF_CLKScr_PMOSChannelWidth = 833,
    ## Bottom Placed
        ## CompOut
            ## InvChain Common
                ## Height
        _BUF_CompOut_PMOSXvt2NMOSXvt = 500,  # number
            ## Inverter Chain
                ## Inv1 common
        _BUF_CompOut_XVT='SLVT',
        _BUF_CompOut_NumberofGate = 3,
        _BUF_CompOut_ChanneLength = 30,
                ## NMOS
        _BUF_CompOut_NMOSChannelWidth = 784,
                ## PMOS
        _BUF_CompOut_PMOSChannelWidth = 833,


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
_NumofBit = 12,

## SAR Logic
    ## Clock Tree (Driving SAR Logic)
        ## Clock Tree Updward (CLK Source Tree, CLK Samp Tree)
            ## CLK Buffer Unit
                ## Common
                _LOGIC_CLKBufTreeTop_UnitBuf_XVT='SLVT',
                ## Nmos
                _LOGIC_CLKBufTreeTop_UnitBuf_NMOS_NumberofGate=1,  # Number
                _LOGIC_CLKBufTreeTop_UnitBuf_NMOS_ChannelWidth=400,  # Number
                _LOGIC_CLKBufTreeTop_UnitBuf_NMOS_ChannelLength=30,  # Number
                ## Pmos
                _LOGIC_CLKBufTreeTop_UnitBuf_PMOS_NumberofGate=1,  # Number
                _LOGIC_CLKBufTreeTop_UnitBuf_PMOS_ChannelWidth=800,  # Number
                _LOGIC_CLKBufTreeTop_UnitBuf_PMOS_ChannelLength=30,  # Number
                # Height
                _LOGIC_CLKBufTreeTop_UnitBuf_PMOSXvt2NMOSXvt=446,  # number
            ## Clock Buffer Tree structure
            _LOGIC_CLKBufTreeTop_BufTree1and2_NumOfStage=4,  # len[Buf0, Buf1, ... ] 스테이지 수 (아래 버퍼 사이즈 리스트의 길이와 같아야 함.)
            _LOGIC_CLKBufTreeTop_BufTree1_SizeofEachStage=[1, 2, 4, 8],  # CLKSampBuf: [Buf0, Buf1, Buf2 ...]
            _LOGIC_CLKBufTreeTop_BufTree2_SizeofEachStage=[1, 2, 4, 8],  # CLKSrcBuf: [Buf0, Buf1, Buf2 ...]
            _LOGIC_CLKBufTreeTop_XOffSet=0,
        ## Clock Tree Dnward (CLK Source Tree, CLK Samp Tree)
            ## CLK Buffer Unit
                ## Common
                _LOGIC_CLKBufTreeBot_UnitBuf_XVT='SLVT',
                ## Nmos
                _LOGIC_CLKBufTreeBot_UnitBuf_NMOS_NumberofGate=1,  # Number
                _LOGIC_CLKBufTreeBot_UnitBuf_NMOS_ChannelWidth=400,  # Number
                _LOGIC_CLKBufTreeBot_UnitBuf_NMOS_ChannelLength=30,  # Number
                ## Pmos
                _LOGIC_CLKBufTreeBot_UnitBuf_PMOS_NumberofGate=1,  # Number
                _LOGIC_CLKBufTreeBot_UnitBuf_PMOS_ChannelWidth=800,  # Number
                _LOGIC_CLKBufTreeBot_UnitBuf_PMOS_ChannelLength=30,  # Number
                # Height
                _LOGIC_CLKBufTreeBot_UnitBuf_PMOSXvt2NMOSXvt=446,  # number
            ## Clock Buffer Tree structure
            _LOGIC_CLKBufTreeBot_BufTree1and2_NumOfStage=4,  # len[Buf0, Buf1, ... ] 스테이지 수 (아래 버퍼 사이즈 리스트의 길이와 같아야 함.)
            _LOGIC_CLKBufTreeBot_BufTree1_SizeofEachStage=[1, 2, 4, 8],  # CompOutBuf: [Buf0, Buf1, Buf2 ...]
            _LOGIC_CLKBufTreeBot_BufTree2_SizeofEachStage=[1, 2, 4, 8],  # CLKDoutBuf: [Buf0, Buf1, Buf2 ...]
            _LOGIC_CLKBufTreeBot_XOffSet=0,

    ## Clock Spine (Physical demension)
        ## CLK Source: upward, 1st floor
        _LOGIC_YWidthOfCLKSrc=100,
        ## CLK Samp: upward, 2nd floor
        _LOGIC_SpaceBtwCLKSrcAndCLKSamp=100,
        _LOGIC_YWidthOfCLKSamp=100,
        ## Comparator Output: downward, Basement1
        _LOGIC_YWidthOfCompOut=100,
        ## CLK Dout: downward, basement2
        _LOGIC_SpaceBtwCompOutAndCLKDout=100,
        _LOGIC_YWidthOfCLKDout=100,

    ## SetResetDFF
        ## DFF Common
        _LOGIC_Test_distance=320,
        _LOGIC_DFF_PMOSXvt2NMOSXvt    = 1150, # number

        ## Master Xgate1
            ## Xgate common
            _LOGIC_Mst_Xgate1_XVT='SLVT',
            ## Xgate NMOS
            _LOGIC_Mst_Xgate1_NMOS_NumberofGate=1,
            _LOGIC_Mst_Xgate1_NMOS_ChannelWidth=300,
            _LOGIC_Mst_Xgate1_NMOS_ChannelLength=30,
            ## Xgate PMOS
            _LOGIC_Mst_Xgate1_PMOS_NumberofGate=3,
            _LOGIC_Mst_Xgate1_PMOS_ChannelWidth=500,
            _LOGIC_Mst_Xgate1_PMOS_ChannelLength=30,

        ## Master Xgate2
            ## Xgate common
            _LOGIC_Mst_Xgate2_XVT='SLVT',
            ## Xgate NMOS
            _LOGIC_Mst_Xgate2_NMOS_NumberofGate           = 2,
            _LOGIC_Mst_Xgate2_NMOS_ChannelWidth           = 800,
            _LOGIC_Mst_Xgate2_NMOS_ChannelLength          = 30,
            ## Xgate PMOS
            _LOGIC_Mst_Xgate2_PMOS_NumberofGate           = 3,
            _LOGIC_Mst_Xgate2_PMOS_ChannelWidth           = 200,
            _LOGIC_Mst_Xgate2_PMOS_ChannelLength          = 30,

        ## Master Nor1
            ## Nor1 common
            _LOGIC_Mst_Nor1_XVT='SLVT',
            ## NMOS
                ## NMOSA
                _LOGIC_Mst_Nor1_NMOSA_NumberofGate           = 2,
                _LOGIC_Mst_Nor1_NMOSA_ChannelWidth           = 800,
                _LOGIC_Mst_Nor1_NMOSA_ChannelLength          = 30,
                ## NMOSB
                _LOGIC_Mst_Nor1_NMOSB_NumberofGate           = 3,
                _LOGIC_Mst_Nor1_NMOSB_ChannelWidth           = 200,
                _LOGIC_Mst_Nor1_NMOSB_ChannelLength          = 30,
            ## PMOS
                ## PMOSA
                _LOGIC_Mst_Nor1_PMOSA_NumberofGate            = 2,
                _LOGIC_Mst_Nor1_PMOSA_ChannelWidth            = 800,
                _LOGIC_Mst_Nor1_PMOSA_ChannelLength           = 30,
                ## PMOSB
                _LOGIC_Mst_Nor1_PMOSB_NumberofGate            = 3,
                _LOGIC_Mst_Nor1_PMOSB_ChannelWidth            = 200,
                _LOGIC_Mst_Nor1_PMOSB_ChannelLength           = 30,

        ## Master Nor2
            ## Nor2 common
            _LOGIC_Mst_Nor2_XVT='SLVT',
            ## NMOS
                ## NMOSA
                _LOGIC_Mst_Nor2_NMOSA_NumberofGate           = 2,
                _LOGIC_Mst_Nor2_NMOSA_ChannelWidth           = 800,
                _LOGIC_Mst_Nor2_NMOSA_ChannelLength          = 30,
                ## NMOSB
                _LOGIC_Mst_Nor2_NMOSB_NumberofGate           = 3,
                _LOGIC_Mst_Nor2_NMOSB_ChannelWidth           = 200,
                _LOGIC_Mst_Nor2_NMOSB_ChannelLength          = 30,
            ## PMOS
                ## PMOSA
                _LOGIC_Mst_Nor2_PMOSA_NumberofGate            = 2,
                _LOGIC_Mst_Nor2_PMOSA_ChannelWidth            = 800,
                _LOGIC_Mst_Nor2_PMOSA_ChannelLength           = 30,
                ## PMOSB
                _LOGIC_Mst_Nor2_PMOSB_NumberofGate            = 3,
                _LOGIC_Mst_Nor2_PMOSB_ChannelWidth            = 200,
                _LOGIC_Mst_Nor2_PMOSB_ChannelLength           = 30,

        ## Master Inv1 : Set pre-driver
            ## Inv1 common
            _LOGIC_Mst_Inv1_XVT='SLVT',
            ## Inv1 NMOS
            _LOGIC_Mst_Inv1_NMOS_NumberofGate           = 1,
            _LOGIC_Mst_Inv1_NMOS_ChannelWidth           = 300,
            _LOGIC_Mst_Inv1_NMOS_ChannelLength          = 30,
            ## Inv1 PMOS
            _LOGIC_Mst_Inv1_PMOS_NumberofGate           = 3,
            _LOGIC_Mst_Inv1_PMOS_ChannelWidth           = 500,
            _LOGIC_Mst_Inv1_PMOS_ChannelLength          = 30,

        ## Master Inv2 : Set driver
            ## Inv2 common
            _LOGIC_Mst_Inv2_XVT='SLVT',
            ## Inv2 NMOS
            _LOGIC_Mst_Inv2_NMOS_NumberofGate           = 1,
            _LOGIC_Mst_Inv2_NMOS_ChannelWidth           = 300,
            _LOGIC_Mst_Inv2_NMOS_ChannelLength          = 30,
            ## Inv2 PMOS
            _LOGIC_Mst_Inv2_PMOS_NumberofGate           = 3,
            _LOGIC_Mst_Inv2_PMOS_ChannelWidth           = 500,
            _LOGIC_Mst_Inv2_PMOS_ChannelLength          = 30,

        ## Master Inv3 : Clock driver
            ## Inv3 common
            _LOGIC_Mst_Inv3_XVT='SLVT',
            ## Inv3 NMOS
            _LOGIC_Mst_Inv3_NMOS_NumberofGate           = 1,
            _LOGIC_Mst_Inv3_NMOS_ChannelWidth           = 300,
            _LOGIC_Mst_Inv3_NMOS_ChannelLength          = 30,
            ## Inv3 PMOS
            _LOGIC_Mst_Inv3_PMOS_NumberofGate           = 3,
            _LOGIC_Mst_Inv3_PMOS_ChannelWidth           = 500,
            _LOGIC_Mst_Inv3_PMOS_ChannelLength          = 30,

        ## Slave Xgate1
            ## Xgate common
            _LOGIC_Slv_Xgate1_XVT='SLVT',
            ## Xgate NMOS
            _LOGIC_Slv_Xgate1_NMOS_NumberofGate           = 1,
            _LOGIC_Slv_Xgate1_NMOS_ChannelWidth           = 300,
            _LOGIC_Slv_Xgate1_NMOS_ChannelLength          = 30,
            ## Xgate PMOS
            _LOGIC_Slv_Xgate1_PMOS_NumberofGate           = 3,
            _LOGIC_Slv_Xgate1_PMOS_ChannelWidth           = 500,
            _LOGIC_Slv_Xgate1_PMOS_ChannelLength          = 30,

        ## Slave Xgate2
            ## Xgate common
            _LOGIC_Slv_Xgate2_XVT='SLVT',
            ## Xgate NMOS
            _LOGIC_Slv_Xgate2_NMOS_NumberofGate           = 2,
            _LOGIC_Slv_Xgate2_NMOS_ChannelWidth           = 800,
            _LOGIC_Slv_Xgate2_NMOS_ChannelLength          = 30,
            ## Xgate PMOS
            _LOGIC_Slv_Xgate2_PMOS_NumberofGate           = 3,
            _LOGIC_Slv_Xgate2_PMOS_ChannelWidth           = 200,
            _LOGIC_Slv_Xgate2_PMOS_ChannelLength          = 30,

        ## Slave Nor1
            ## Nor1 common
            _LOGIC_Slv_Nor1_XVT='SLVT',
            ## NMOS
                ## NMOSA
                _LOGIC_Slv_Nor1_NMOSA_NumberofGate           = 2,
                _LOGIC_Slv_Nor1_NMOSA_ChannelWidth           = 800,
                _LOGIC_Slv_Nor1_NMOSA_ChannelLength          = 30,
                ## NMOSB
                _LOGIC_Slv_Nor1_NMOSB_NumberofGate           = 3,
                _LOGIC_Slv_Nor1_NMOSB_ChannelWidth           = 200,
                _LOGIC_Slv_Nor1_NMOSB_ChannelLength          = 30,
            ## PMOS
                ## PMOSA
                _LOGIC_Slv_Nor1_PMOSA_NumberofGate            = 2,
                _LOGIC_Slv_Nor1_PMOSA_ChannelWidth            = 800,
                _LOGIC_Slv_Nor1_PMOSA_ChannelLength           = 30,
                ## PMOSB
                _LOGIC_Slv_Nor1_PMOSB_NumberofGate            = 3,
                _LOGIC_Slv_Nor1_PMOSB_ChannelWidth            = 200,
                _LOGIC_Slv_Nor1_PMOSB_ChannelLength           = 30,

        ## Slave Nor2
            ## Nor2 common
            _LOGIC_Slv_Nor2_XVT='SLVT',
            ## NMOS
                ## NMOSA
                _LOGIC_Slv_Nor2_NMOSA_NumberofGate           = 2,
                _LOGIC_Slv_Nor2_NMOSA_ChannelWidth           = 800,
                _LOGIC_Slv_Nor2_NMOSA_ChannelLength          = 30,
                ## NMOSB
                _LOGIC_Slv_Nor2_NMOSB_NumberofGate           = 3,
                _LOGIC_Slv_Nor2_NMOSB_ChannelWidth           = 200,
                _LOGIC_Slv_Nor2_NMOSB_ChannelLength          = 30,
            ## PMOS
                ## PMOSA
                _LOGIC_Slv_Nor2_PMOSA_NumberofGate            = 2,
                _LOGIC_Slv_Nor2_PMOSA_ChannelWidth            = 800,
                _LOGIC_Slv_Nor2_PMOSA_ChannelLength           = 30,
                ## PMOSB
                _LOGIC_Slv_Nor2_PMOSB_NumberofGate            = 3,
                _LOGIC_Slv_Nor2_PMOSB_ChannelWidth            = 200,
                _LOGIC_Slv_Nor2_PMOSB_ChannelLength           = 30,

        ## Slave Inv1 : ReSet pre-driver
            ## Inv1 common
            _LOGIC_Slv_Inv1_XVT='SLVT',
            ## Inv1 NMOS
            _LOGIC_Slv_Inv1_NMOS_NumberofGate           = 1,
            _LOGIC_Slv_Inv1_NMOS_ChannelWidth           = 300,
            _LOGIC_Slv_Inv1_NMOS_ChannelLength          = 30,
            ## Inv1 PMOS
            _LOGIC_Slv_Inv1_PMOS_NumberofGate           = 3,
            _LOGIC_Slv_Inv1_PMOS_ChannelWidth           = 500,
            _LOGIC_Slv_Inv1_PMOS_ChannelLength          = 30,

        ## Slave Inv2 : ReSet driver
            ## Inv2 common
            _LOGIC_Slv_Inv2_XVT='SLVT',
            ## Inv2 NMOS
            _LOGIC_Slv_Inv2_NMOS_NumberofGate           = 1,
            _LOGIC_Slv_Inv2_NMOS_ChannelWidth           = 300,
            _LOGIC_Slv_Inv2_NMOS_ChannelLength          = 30,
            ## Inv2 PMOS
            _LOGIC_Slv_Inv2_PMOS_NumberofGate           = 3,
            _LOGIC_Slv_Inv2_PMOS_ChannelWidth           = 500,
            _LOGIC_Slv_Inv2_PMOS_ChannelLength          = 30,

        ## Slave Inv3 : Qb driver
            ## Inv3 common
            _LOGIC_Slv_Inv3_XVT='SLVT',
            ## Inv3 NMOS
            _LOGIC_Slv_Inv3_NMOS_NumberofGate           = 1,
            _LOGIC_Slv_Inv3_NMOS_ChannelWidth           = 300,
            _LOGIC_Slv_Inv3_NMOS_ChannelLength          = 30,
            ## Inv3 PMOS
            _LOGIC_Slv_Inv3_PMOS_NumberofGate           = 3,
            _LOGIC_Slv_Inv3_PMOS_ChannelWidth           = 500,
            _LOGIC_Slv_Inv3_PMOS_ChannelLength          = 30,
## DAC PreDriver
    ## Inverter Chain
        ## InvChain Common
        _LOGIC_DACPreDrv_PMOSXvt2NMOSXvt=500,  # number
        ## Inverter Chain
            ## Inv1 common
        _LOGIC_DACPreDrv_NumberofGate=[[1, 2, 4, 8], [1, 2, 4, 8], [1, 2, 4, 8], [2, 2, 2, 2, 2]],  # Vector
        _LOGIC_DACPreDrv_ChannelLength=30,  # Scalar
        _LOGIC_DACPreDrv_XVT='SLVT',  # 'SLVT'
            ## Inv1 NMOS
        _LOGIC_DACPreDrv_Inv_NMOS_ChannelWidth=400,  # Scalar
            ## Inv1 PMOS
        _LOGIC_DACPreDrv_Inv_PMOS_ChannelWidth=800,  # Scalar
## CLKOutSamp(!=ClkSamp)
    ## Common
        # XVT
        _LOGIC_CLKoutSamp_XVT = 'SLVT',
        # Height
        # _CLKOutSamp_PMOSXvt2NMOSXvt=1800,  # number, = _DFF_PMOSXvt2NMOSXvt
    ## Inverter
        # Nmos
        _LOGIC_CLKoutSamp_Inv_NMOS_NumberofGate=1,  # Number
        _LOGIC_CLKoutSamp_Inv_NMOS_ChannelWidth=100,  # Number
        _LOGIC_CLKoutSamp_Inv_NMOS_ChannelLength=30,  # Number
        # Pmos
        _LOGIC_CLKoutSamp_Inv_PMOS_NumberofGate=1,  # Number
        _LOGIC_CLKoutSamp_Inv_PMOS_ChannelWidth=100,  # Number
        _LOGIC_CLKoutSamp_Inv_PMOS_ChannelLength=30,  # Number
    ## AND
        ## AND Common
        ## Nand
            # NmosA
            _LOGIC_CLKoutSamp_And_Nand_NMOSA_NumberofGate=1,  # Number
            _LOGIC_CLKoutSamp_And_Nand_NMOSA_ChannelWidth=100,  # Number
            _LOGIC_CLKoutSamp_And_Nand_NMOSA_ChannelLength=30,  # Number
            # NMOSB
            _LOGIC_CLKoutSamp_And_Nand_NMOSB_NumberofGate=2,  # Number
            _LOGIC_CLKoutSamp_And_Nand_NMOSB_ChannelWidth=750,  # Number
            _LOGIC_CLKoutSamp_And_Nand_NMOSB_ChannelLength=30,  # Number
            # PMOSA
            _LOGIC_CLKoutSamp_And_Nand_PMOSA_NumberofGate=1,  # Number
            _LOGIC_CLKoutSamp_And_Nand_PMOSA_ChannelWidth=300,  # Number
            _LOGIC_CLKoutSamp_And_Nand_PMOSA_ChannelLength=30,  # Number
            # PMOSB
            _LOGIC_CLKoutSamp_And_Nand_PMOSB_NumberofGate=3,  # Number
            _LOGIC_CLKoutSamp_And_Nand_PMOSB_ChannelWidth=750,  # Number
            _LOGIC_CLKoutSamp_And_Nand_PMOSB_ChannelLength=30,  # Number
        ## Inverter
            # Nmos
            _LOGIC_CLKoutSamp_And_Inv_NMOS_NumberofGate=1,  # Number
            _LOGIC_CLKoutSamp_And_Inv_NMOS_ChannelWidth=100,  # Number
            _LOGIC_CLKoutSamp_And_Inv_NMOS_ChannelLength=30,  # Number
            # Pmos
            _LOGIC_CLKoutSamp_And_Inv_PMOS_NumberofGate=1,  # Number
            _LOGIC_CLKoutSamp_And_Inv_PMOS_ChannelWidth=200,  # Number
            _LOGIC_CLKoutSamp_And_Inv_PMOS_ChannelLength=30,  # Number
## Comparator
    ## StrongARM Latch
        # Common
        _COMP_SALatch_ChannelLength=30,  # random.randrange(30, 60, 2),  # 30
        _COMP_SALatch_XVT='HVT',

        # PMOS
        _COMP_SALatch_CLKinputPMOSFinger1=1,  #PMOS Reset Sw1 # random.randint(1, 15),  # 6
        _COMP_SALatch_CLKinputPMOSFinger2=1,  #PMOS Reset Sw2 # random.randint(1, 15),  # 3
        _COMP_SALatch_PMOSFinger=1,  		  #PMOS Latch	  # random.randint(1, 15),  # 3
        _COMP_SALatch_PMOSChannelWidth=1000,  #All PMOS width # random.randrange(200, 1050, 2),  # 500

        # NMOS
        _COMP_SALatch_DATAinputNMOSFinger=3,  #NMOS Input Tr # random.randint(3, 15),  # 12
        _COMP_SALatch_NMOSFinger=2,  		  #NMOS at Latch # random.randint(1, 15),  # 2
        _COMP_SALatch_CLKinputNMOSFinger=1,  #NMOS Tail # random.randint(1, 15),  # 8
        _COMP_SALatch_NMOSChannelWidth=330,  #Nmos width # random.randrange(200, 1050, 2),  # 500
        _COMP_SALatch_CLKinputNMOSChannelWidth=200,  # random.randrange(200, 1050, 2),  # 800

    ## StrongArmOutBuffer and SRLatch
        ## Common
            # XVT
            _COMP_SAOutBufAndSRLatch_XVT='SLVT',
            # Body
            _COMP_SAOutBufAndSRLatch_NMOS_Pbody_XvtTop2Pbody=None,  # Number/None(Minimum)
            _COMP_SAOutBufAndSRLatch_PMOS_Nbody_Xvtdown2Nbody=None,  # Number/None(Minimum)
            # Height
            _COMP_SAOutBufAndSRLatch_PMOSXvt2NMOSXvt=1800,  # number
        ## StronArm Output Buffer
            ## Inverter1(pre)
                    #Nmos
                _COMP_SAOutBuf_Buf_Inv1_NMOS_NumberofGate          = 1,        # Number
                _COMP_SAOutBuf_Buf_Inv1_NMOS_ChannelWidth          = 400,      # Number
                _COMP_SAOutBuf_Buf_Inv1_NMOS_ChannelLength         = 30,       # Number
                    #Pmos
                _COMP_SAOutBuf_Buf_Inv1_PMOS_NumberofGate          = 1,        # Number
                _COMP_SAOutBuf_Buf_Inv1_PMOS_ChannelWidth          = 800,      # Number
                _COMP_SAOutBuf_Buf_Inv1_PMOS_ChannelLength         = 30,       # Number
            ## Inverter2
                    #Nmos
                _COMP_SAOutBuf_Buf_Inv2_NMOS_NumberofGate          = 2,        # Number
                _COMP_SAOutBuf_Buf_Inv2_NMOS_ChannelWidth          = 400,      # Number
                _COMP_SAOutBuf_Buf_Inv2_NMOS_ChannelLength         = 30,       # Number
                    #Pmos
                _COMP_SAOutBuf_Buf_Inv2_PMOS_NumberofGate          = 2,        # Number
                _COMP_SAOutBuf_Buf_Inv2_PMOS_ChannelWidth          = 800,      # Number
                _COMP_SAOutBuf_Buf_Inv2_PMOS_ChannelLength         = 30,       # Number
        ## SRLatch
            ## Nand(Set,Rst same)
                # NmosA
                _COMP_SRLatch_Nand_NMOSA_NumberofGate=1,  # Number
                _COMP_SRLatch_Nand_NMOSA_ChannelWidth=100,  # Number
                _COMP_SRLatch_Nand_NMOSA_ChannelLength=30,  # Number
                # NMOSB
                _COMP_SRLatch_Nand_NMOSB_NumberofGate=2,  # Number
                _COMP_SRLatch_Nand_NMOSB_ChannelWidth=750,  # Number
                _COMP_SRLatch_Nand_NMOSB_ChannelLength=30,  # Number
                # PMOSA
                _COMP_SRLatch_Nand_PMOSA_NumberofGate=2,  # Number
                _COMP_SRLatch_Nand_PMOSA_ChannelWidth=100,  # Number
                _COMP_SRLatch_Nand_PMOSA_ChannelLength=30,  # Number
                # PMOSB
                _COMP_SRLatch_Nand_PMOSB_NumberofGate=1,  # Number
                _COMP_SRLatch_Nand_PMOSB_ChannelWidth=750,  # Number
                _COMP_SRLatch_Nand_PMOSB_ChannelLength=30,  # Number

    ## Comp clock Gen Logic: Clk_Samp Inv, Clk_Source Inv, AND Gate, CompClockBuff
        ## Common
            # XVT
            _COMP_CompClkLogic_XVT='SLVT',
            # Body
            _COMP_CompClkLogic_NMOS_Pbody_XvtTop2Pbody=None,  # Number/None(Minimum)
            _COMP_CompClkLogic_PMOS_Nbody_Xvtdown2Nbody=None,  # Number/None(Minimum)
            # Height
            _COMP_CompClkLogic_PMOSXvt2NMOSXvt=1800,  # number
        ## StronArm Output Buffer
            ## Inverter1(pre)
                    #Nmos
                _COMP_CompClkLogic_Buf_Inv1_NMOS_NumberofGate          = 2,        # Number
                _COMP_CompClkLogic_Buf_Inv1_NMOS_ChannelWidth          = 400,      # Number
                _COMP_CompClkLogic_Buf_Inv1_NMOS_ChannelLength         = 30,       # Number
                    #Pmos
                _COMP_CompClkLogic_Buf_Inv1_PMOS_NumberofGate          = 2,        # Number
                _COMP_CompClkLogic_Buf_Inv1_PMOS_ChannelWidth          = 800,      # Number
                _COMP_CompClkLogic_Buf_Inv1_PMOS_ChannelLength         = 30,       # Number
            ## Inverter2
                    #Nmos
                _COMP_CompClkLogic_Buf_Inv2_NMOS_NumberofGate          = 4,        # Number
                _COMP_CompClkLogic_Buf_Inv2_NMOS_ChannelWidth          = 400,      # Number
                _COMP_CompClkLogic_Buf_Inv2_NMOS_ChannelLength         = 30,       # Number
                    #Pmos
                _COMP_CompClkLogic_Buf_Inv2_PMOS_NumberofGate          = 4,        # Number
                _COMP_CompClkLogic_Buf_Inv2_PMOS_ChannelWidth          = 800,      # Number
                _COMP_CompClkLogic_Buf_Inv2_PMOS_ChannelLength         = 30,       # Number
        ## AND
            ## Nand
                # NmosA
                _COMP_CompClkLogic_Nand_NMOSA_NumberofGate=1,  # Number
                _COMP_CompClkLogic_Nand_NMOSA_ChannelWidth=100,  # Number
                _COMP_CompClkLogic_Nand_NMOSA_ChannelLength=30,  # Number
                # NMOSB
                _COMP_CompClkLogic_Nand_NMOSB_NumberofGate=2,  # Number
                _COMP_CompClkLogic_Nand_NMOSB_ChannelWidth=750,  # Number
                _COMP_CompClkLogic_Nand_NMOSB_ChannelLength=30,  # Number
                # PMOSA
                _COMP_CompClkLogic_Nand_PMOSA_NumberofGate=1,  # Number
                _COMP_CompClkLogic_Nand_PMOSA_ChannelWidth=300,  # Number
                _COMP_CompClkLogic_Nand_PMOSA_ChannelLength=30,  # Number
                # PMOSB
                _COMP_CompClkLogic_Nand_PMOSB_NumberofGate=3,  # Number
                _COMP_CompClkLogic_Nand_PMOSB_ChannelWidth=750,  # Number
                _COMP_CompClkLogic_Nand_PMOSB_ChannelLength=30,  # Number
            ## Inverter
                # Nmos
                _COMP_CompClkLogic_Inv_NMOS_NumberofGate=1,  # Number
                _COMP_CompClkLogic_Inv_NMOS_ChannelWidth=100,  # Number
                _COMP_CompClkLogic_Inv_NMOS_ChannelLength=30,  # Number
                # Pmos
                _COMP_CompClkLogic_Inv_PMOS_NumberofGate=1,  # Number
                _COMP_CompClkLogic_Inv_PMOS_ChannelWidth=200,  # Number
                _COMP_CompClkLogic_Inv_PMOS_ChannelLength=30,  # Number

        ## Clk_Source Inv
                #Nmos
            _COMP_CompClkLogic_ClkSrc_NMOS_NumberofGate          = 1,        # Number
            _COMP_CompClkLogic_ClkSrc_NMOS_ChannelWidth          = 400,      # Number
            _COMP_CompClkLogic_ClkSrc_NMOS_ChannelLength         = 30,       # Number
                #Pmos
            _COMP_CompClkLogic_ClkSrc_PMOS_NumberofGate          = 1,        # Number
            _COMP_CompClkLogic_ClkSrc_PMOS_ChannelWidth          = 800,      # Number
            _COMP_CompClkLogic_ClkSrc_PMOS_ChannelLength         = 30,       # Number
        ## Clk_Samp Inv
                #Nmos
            _COMP_CompClkLogic_ClkSmp_NMOS_NumberofGate          = 1,        # Number
            _COMP_CompClkLogic_ClkSmp_NMOS_ChannelWidth          = 400,      # Number
            _COMP_CompClkLogic_ClkSmp_NMOS_ChannelLength         = 30,       # Number
                #Pmos
            _COMP_CompClkLogic_ClkSmp_PMOS_NumberofGate          = 1,        # Number
            _COMP_CompClkLogic_ClkSmp_PMOS_ChannelWidth          = 800,      # Number
            _COMP_CompClkLogic_ClkSmp_PMOS_ChannelLength         = 30,       # Number

## CLOCK AND DATA BUF : Comparator Dout Buf for driving Logic, CLKSamp and CLKScr Buff for Driving Sampler and Comparator
    ## Top placed
        ## CLK Samp
            ## InvChain Common
                ## Height
        _BUF_CLKSamp_PMOSXvt2NMOSXvt = 500,  # number
            ## Inverter Chain
                ## Inv1 common
        _BUF_CLKSamp_XVT='SLVT',
        _BUF_CLKSamp_NumberofGate = 3,
        _BUF_CLKSamp_ChanneLength = 30,
                ## NMOS
        _BUF_CLKSamp_NMOSChannelWidth = 784,
                ## PMOS
        _BUF_CLKSamp_PMOSChannelWidth = 833,
        ## CLK Scr
            ## InvChain Common
                ## Height
        _BUF_CLKScr_PMOSXvt2NMOSXvt = 500,  # number
            ## Inverter Chain
                ## Inv1 common
        _BUF_CLKScr_XVT='SLVT',
        _BUF_CLKScr_NumberofGate = 3,
        _BUF_CLKScr_ChanneLength = 30,
                ## NMOS
        _BUF_CLKScr_NMOSChannelWidth = 784,
                ## PMOS
        _BUF_CLKScr_PMOSChannelWidth = 833,
    ## Bottom Placed
        ## CompOut
            ## InvChain Common
                ## Height
        _BUF_CompOut_PMOSXvt2NMOSXvt = 500,  # number
            ## Inverter Chain
                ## Inv1 common
        _BUF_CompOut_XVT='SLVT',
        _BUF_CompOut_NumberofGate = 3,
        _BUF_CompOut_ChanneLength = 30,
                ## NMOS
        _BUF_CompOut_NMOSChannelWidth = 784,
                ## PMOS
        _BUF_CompOut_PMOSChannelWidth = 833,


                                  ):

        ## Class_HEADER: Pre Defined Parameter Before Calculation
        ## Load DRC library
        _DRCobj = DRC.DRC()
        ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ## CALCULATION START
        SARLogicWtComparator_start_time = time.time()
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')
        ## Error
        if len(_LOGIC_DACPreDrv_NumberofGate) != _NumofBit:
            raise NotImplementedError(f"_LOGIC_DACPreDrv_NumberofGate != _NumofBit")

        ############################################################################################################################################################

        _Caculation_Parameters1 = copy.deepcopy(K00_02_SARLogicWtCDACPreDriver_YJH._SARLogicWtCDACPreDriver._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters1['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters1['_NumofBit'] = _NumofBit
        ## SAR Logic
            ## Clock Tree (Driving SAR Logic)
                ## Clock Tree Updward (CLK Source Tree, CLK Samp Tree)
                    ## CLK Buffer Unit
                        ## Common
        _Caculation_Parameters1['_CLKBufTreeTop_UnitBuf_XVT'] = _LOGIC_CLKBufTreeTop_UnitBuf_XVT
                        ## Nmos
        _Caculation_Parameters1['_CLKBufTreeTop_UnitBuf_NMOS_NumberofGate'] = _LOGIC_CLKBufTreeTop_UnitBuf_NMOS_NumberofGate
        _Caculation_Parameters1['_CLKBufTreeTop_UnitBuf_NMOS_ChannelWidth'] = _LOGIC_CLKBufTreeTop_UnitBuf_NMOS_ChannelWidth
        _Caculation_Parameters1['_CLKBufTreeTop_UnitBuf_NMOS_ChannelLength'] = _LOGIC_CLKBufTreeTop_UnitBuf_NMOS_ChannelLength
                        ## Pmos
        _Caculation_Parameters1['_CLKBufTreeTop_UnitBuf_PMOS_NumberofGate'] = _LOGIC_CLKBufTreeTop_UnitBuf_PMOS_NumberofGate
        _Caculation_Parameters1['_CLKBufTreeTop_UnitBuf_PMOS_ChannelWidth'] = _LOGIC_CLKBufTreeTop_UnitBuf_PMOS_ChannelWidth
        _Caculation_Parameters1['_CLKBufTreeTop_UnitBuf_PMOS_ChannelLength'] = _LOGIC_CLKBufTreeTop_UnitBuf_PMOS_ChannelLength
                        ## Height
        _Caculation_Parameters1['_CLKBufTreeTop_UnitBuf_PMOSXvt2NMOSXvt'] = _LOGIC_CLKBufTreeTop_UnitBuf_PMOSXvt2NMOSXvt
                    ## Clock Buffer Tree structure
        _Caculation_Parameters1['_CLKBufTreeTop_BufTree1and2_NumOfStage'] = _LOGIC_CLKBufTreeTop_BufTree1and2_NumOfStage
        _Caculation_Parameters1['_CLKBufTreeTop_BufTree1_SizeofEachStage'] = _LOGIC_CLKBufTreeTop_BufTree1_SizeofEachStage
        _Caculation_Parameters1['_CLKBufTreeTop_BufTree2_SizeofEachStage'] = _LOGIC_CLKBufTreeTop_BufTree2_SizeofEachStage
        _Caculation_Parameters1['_CLKBufTreeTop_XOffSet'] = _LOGIC_CLKBufTreeTop_XOffSet
                ## Clock Tree Dnward (CLK Source Tree, CLK Samp Tree)
                    ## CLK Buffer Unit
                        ## Common
        _Caculation_Parameters1['_CLKBufTreeBot_UnitBuf_XVT'] = _LOGIC_CLKBufTreeBot_UnitBuf_XVT
                        ## Nmos
        _Caculation_Parameters1['_CLKBufTreeBot_UnitBuf_NMOS_NumberofGate'] = _LOGIC_CLKBufTreeBot_UnitBuf_NMOS_NumberofGate
        _Caculation_Parameters1['_CLKBufTreeBot_UnitBuf_NMOS_ChannelWidth'] = _LOGIC_CLKBufTreeBot_UnitBuf_NMOS_ChannelWidth
        _Caculation_Parameters1['_CLKBufTreeBot_UnitBuf_NMOS_ChannelLength'] = _LOGIC_CLKBufTreeBot_UnitBuf_NMOS_ChannelLength
                        ## Pmos
        _Caculation_Parameters1['_CLKBufTreeBot_UnitBuf_PMOS_NumberofGate'] = _LOGIC_CLKBufTreeBot_UnitBuf_PMOS_NumberofGate
        _Caculation_Parameters1['_CLKBufTreeBot_UnitBuf_PMOS_ChannelWidth'] = _LOGIC_CLKBufTreeBot_UnitBuf_PMOS_ChannelWidth
        _Caculation_Parameters1['_CLKBufTreeBot_UnitBuf_PMOS_ChannelLength'] = _LOGIC_CLKBufTreeBot_UnitBuf_PMOS_ChannelLength
                        ## Height
        _Caculation_Parameters1['_CLKBufTreeBot_UnitBuf_PMOSXvt2NMOSXvt'] = _LOGIC_CLKBufTreeBot_UnitBuf_PMOSXvt2NMOSXvt
                    ## Clock Buffer Tree structure
        _Caculation_Parameters1['_CLKBufTreeBot_BufTree1and2_NumOfStage'] = _LOGIC_CLKBufTreeBot_BufTree1and2_NumOfStage
        _Caculation_Parameters1['_CLKBufTreeBot_BufTree1_SizeofEachStage'] = _LOGIC_CLKBufTreeBot_BufTree1_SizeofEachStage
        _Caculation_Parameters1['_CLKBufTreeBot_BufTree2_SizeofEachStage'] = _LOGIC_CLKBufTreeBot_BufTree2_SizeofEachStage
        _Caculation_Parameters1['_CLKBufTreeBot_XOffSet'] = _LOGIC_CLKBufTreeBot_XOffSet
            ## Clock Spine (Physical demension)
                ## CLK Source: upward, 1st floor
        _Caculation_Parameters1['_YWidthOfCLKSrc'] = _LOGIC_YWidthOfCLKSrc
                ## CLK Samp: upward, 2nd floor
        _Caculation_Parameters1['_SpaceBtwCLKSrcAndCLKSamp'] = _LOGIC_SpaceBtwCLKSrcAndCLKSamp
        _Caculation_Parameters1['_YWidthOfCLKSamp'] = _LOGIC_YWidthOfCLKSamp
                ## Comparator Output: downward, Basement1
        _Caculation_Parameters1['_YWidthOfCompOut'] = _LOGIC_YWidthOfCompOut
                ## CLK Dout: downward, basement2
        _Caculation_Parameters1['_SpaceBtwCompOutAndCLKDout'] = _LOGIC_SpaceBtwCompOutAndCLKDout
        _Caculation_Parameters1['_YWidthOfCLKDout'] = _LOGIC_YWidthOfCLKDout

            ## SetResetDFF
                ## DFF Common
        _Caculation_Parameters1['_Test_distance'] = _LOGIC_Test_distance
        _Caculation_Parameters1['_DFF_PMOSXvt2NMOSXvt'] = _LOGIC_DFF_PMOSXvt2NMOSXvt
                ## Master Xgate1
                    ## Xgate common
        _Caculation_Parameters1['_Mst_Xgate1_XVT'] = _LOGIC_Mst_Xgate1_XVT
                    ## Xgate NMOS
        _Caculation_Parameters1['_Mst_Xgate1_NMOS_NumberofGate'] = _LOGIC_Mst_Xgate1_NMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Xgate1_NMOS_ChannelWidth'] = _LOGIC_Mst_Xgate1_NMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Xgate1_NMOS_ChannelLength'] = _LOGIC_Mst_Xgate1_NMOS_ChannelLength
                    ## Xgate PMOS
        _Caculation_Parameters1['_Mst_Xgate1_PMOS_NumberofGate'] = _LOGIC_Mst_Xgate1_PMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Xgate1_PMOS_ChannelWidth'] = _LOGIC_Mst_Xgate1_PMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Xgate1_PMOS_ChannelLength'] = _LOGIC_Mst_Xgate1_PMOS_ChannelLength
                ## Master Xgate2
                    ## Xgate common
        _Caculation_Parameters1['_Mst_Xgate2_XVT'] = _LOGIC_Mst_Xgate2_XVT
                    ## Xgate NMOS
        _Caculation_Parameters1['_Mst_Xgate2_NMOS_NumberofGate'] = _LOGIC_Mst_Xgate2_NMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Xgate2_NMOS_ChannelWidth'] = _LOGIC_Mst_Xgate2_NMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Xgate2_NMOS_ChannelLength'] = _LOGIC_Mst_Xgate2_NMOS_ChannelLength
                    ## Xgate PMOS
        _Caculation_Parameters1['_Mst_Xgate2_PMOS_NumberofGate'] = _LOGIC_Mst_Xgate2_PMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Xgate2_PMOS_ChannelWidth'] = _LOGIC_Mst_Xgate2_PMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Xgate2_PMOS_ChannelLength'] = _LOGIC_Mst_Xgate2_PMOS_ChannelLength
                ## Master Nor1
                    ## Nor1 common
        _Caculation_Parameters1['_Mst_Nor1_XVT'] = _LOGIC_Mst_Nor1_XVT
                    ## NMOS
                        ## NMOSA
        _Caculation_Parameters1['_Mst_Nor1_NMOSA_NumberofGate'] = _LOGIC_Mst_Nor1_NMOSA_NumberofGate
        _Caculation_Parameters1['_Mst_Nor1_NMOSA_ChannelWidth'] = _LOGIC_Mst_Nor1_NMOSA_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor1_NMOSA_ChannelLength'] = _LOGIC_Mst_Nor1_NMOSA_ChannelLength
                        ## NMOSB
        _Caculation_Parameters1['_Mst_Nor1_NMOSB_NumberofGate'] = _LOGIC_Mst_Nor1_NMOSB_NumberofGate
        _Caculation_Parameters1['_Mst_Nor1_NMOSB_ChannelWidth'] = _LOGIC_Mst_Nor1_NMOSB_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor1_NMOSB_ChannelLength'] = _LOGIC_Mst_Nor1_NMOSB_ChannelLength
                    ## PMOS
                        ## PMOSA
        _Caculation_Parameters1['_Mst_Nor1_PMOSA_NumberofGate'] = _LOGIC_Mst_Nor1_PMOSA_NumberofGate
        _Caculation_Parameters1['_Mst_Nor1_PMOSA_ChannelWidth'] = _LOGIC_Mst_Nor1_PMOSA_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor1_PMOSA_ChannelLength'] = _LOGIC_Mst_Nor1_PMOSA_ChannelLength
                        ## PMOSB
        _Caculation_Parameters1['_Mst_Nor1_PMOSB_NumberofGate'] = _LOGIC_Mst_Nor1_PMOSB_NumberofGate
        _Caculation_Parameters1['_Mst_Nor1_PMOSB_ChannelWidth'] = _LOGIC_Mst_Nor1_PMOSB_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor1_PMOSB_ChannelLength'] = _LOGIC_Mst_Nor1_PMOSB_ChannelLength
                ## Master Nor2
                    ## Nor2 common
        _Caculation_Parameters1['_Mst_Nor2_XVT'] = _LOGIC_Mst_Nor2_XVT
                    ## NMOS
                        ## NMOSA
        _Caculation_Parameters1['_Mst_Nor2_NMOSA_NumberofGate'] = _LOGIC_Mst_Nor2_NMOSA_NumberofGate
        _Caculation_Parameters1['_Mst_Nor2_NMOSA_ChannelWidth'] = _LOGIC_Mst_Nor2_NMOSA_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor2_NMOSA_ChannelLength'] = _LOGIC_Mst_Nor2_NMOSA_ChannelLength
                        ## NMOSB
        _Caculation_Parameters1['_Mst_Nor2_NMOSB_NumberofGate'] = _LOGIC_Mst_Nor2_NMOSB_NumberofGate
        _Caculation_Parameters1['_Mst_Nor2_NMOSB_ChannelWidth'] = _LOGIC_Mst_Nor2_NMOSB_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor2_NMOSB_ChannelLength'] = _LOGIC_Mst_Nor2_NMOSB_ChannelLength
                    ## PMOS
                        ## PMOSA
        _Caculation_Parameters1['_Mst_Nor2_PMOSA_NumberofGate'] = _LOGIC_Mst_Nor2_PMOSA_NumberofGate
        _Caculation_Parameters1['_Mst_Nor2_PMOSA_ChannelWidth'] = _LOGIC_Mst_Nor2_PMOSA_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor2_PMOSA_ChannelLength'] = _LOGIC_Mst_Nor2_PMOSA_ChannelLength
                        ## PMOSB
        _Caculation_Parameters1['_Mst_Nor2_PMOSB_NumberofGate'] = _LOGIC_Mst_Nor2_PMOSB_NumberofGate
        _Caculation_Parameters1['_Mst_Nor2_PMOSB_ChannelWidth'] = _LOGIC_Mst_Nor2_PMOSB_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor2_PMOSB_ChannelLength'] = _LOGIC_Mst_Nor2_PMOSB_ChannelLength
                ## Master Inv1 : Set pre-driver
                    ## Inv1 common
        _Caculation_Parameters1['_Mst_Inv1_XVT'] = _LOGIC_Mst_Inv1_XVT
                    ## Inv1 NMOS
        _Caculation_Parameters1['_Mst_Inv1_NMOS_NumberofGate'] = _LOGIC_Mst_Inv1_NMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Inv1_NMOS_ChannelWidth'] = _LOGIC_Mst_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Inv1_NMOS_ChannelLength'] = _LOGIC_Mst_Inv1_NMOS_ChannelLength
                    ## Inv1 PMOS
        _Caculation_Parameters1['_Mst_Inv1_PMOS_NumberofGate'] = _LOGIC_Mst_Inv1_PMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Inv1_PMOS_ChannelWidth'] = _LOGIC_Mst_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Inv1_PMOS_ChannelLength'] = _LOGIC_Mst_Inv1_PMOS_ChannelLength
                ## Master Inv2 : Set driver
                    ## Inv2 common
        _Caculation_Parameters1['_Mst_Inv2_XVT'] = _LOGIC_Mst_Inv2_XVT
                    ## Inv2 NMOS
        _Caculation_Parameters1['_Mst_Inv2_NMOS_NumberofGate'] = _LOGIC_Mst_Inv2_NMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Inv2_NMOS_ChannelWidth'] = _LOGIC_Mst_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Inv2_NMOS_ChannelLength'] = _LOGIC_Mst_Inv2_NMOS_ChannelLength
                    ## Inv2 PMOS
        _Caculation_Parameters1['_Mst_Inv2_PMOS_NumberofGate'] = _LOGIC_Mst_Inv2_PMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Inv2_PMOS_ChannelWidth'] = _LOGIC_Mst_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Inv2_PMOS_ChannelLength'] = _LOGIC_Mst_Inv2_PMOS_ChannelLength
                ## Master Inv3 : Clock driver
                    ## Inv3 common
        _Caculation_Parameters1['_Mst_Inv3_XVT'] = _LOGIC_Mst_Inv3_XVT
                    ## Inv3 NMOS
        _Caculation_Parameters1['_Mst_Inv3_NMOS_NumberofGate'] = _LOGIC_Mst_Inv3_NMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Inv3_NMOS_ChannelWidth'] = _LOGIC_Mst_Inv3_NMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Inv3_NMOS_ChannelLength'] = _LOGIC_Mst_Inv3_NMOS_ChannelLength
                    ## Inv3 PMOS
        _Caculation_Parameters1['_Mst_Inv3_PMOS_NumberofGate'] = _LOGIC_Mst_Inv3_PMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Inv3_PMOS_ChannelWidth'] = _LOGIC_Mst_Inv3_PMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Inv3_PMOS_ChannelLength'] = _LOGIC_Mst_Inv3_PMOS_ChannelLength

                ## Slave Xgate1
                    ## Xgate common
        _Caculation_Parameters1['_Slv_Xgate1_XVT'] = _LOGIC_Slv_Xgate1_XVT
                    ## Xgate NMOS
        _Caculation_Parameters1['_Slv_Xgate1_NMOS_NumberofGate'] = _LOGIC_Slv_Xgate1_NMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Xgate1_NMOS_ChannelWidth'] = _LOGIC_Slv_Xgate1_NMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Xgate1_NMOS_ChannelLength'] = _LOGIC_Slv_Xgate1_NMOS_ChannelLength
                    ## Xgate PMOS
        _Caculation_Parameters1['_Slv_Xgate1_PMOS_NumberofGate'] = _LOGIC_Slv_Xgate1_PMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Xgate1_PMOS_ChannelWidth'] = _LOGIC_Slv_Xgate1_PMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Xgate1_PMOS_ChannelLength'] = _LOGIC_Slv_Xgate1_PMOS_ChannelLength
                ## Slave Xgate2
                    ## Xgate common
        _Caculation_Parameters1['_Slv_Xgate2_XVT'] = _LOGIC_Slv_Xgate2_XVT
                    ## Xgate NMOS
        _Caculation_Parameters1['_Slv_Xgate2_NMOS_NumberofGate'] = _LOGIC_Slv_Xgate2_NMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Xgate2_NMOS_ChannelWidth'] = _LOGIC_Slv_Xgate2_NMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Xgate2_NMOS_ChannelLength'] = _LOGIC_Slv_Xgate2_NMOS_ChannelLength
                    ## Xgate PMOS
        _Caculation_Parameters1['_Slv_Xgate2_PMOS_NumberofGate'] = _LOGIC_Slv_Xgate2_PMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Xgate2_PMOS_ChannelWidth'] = _LOGIC_Slv_Xgate2_PMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Xgate2_PMOS_ChannelLength'] = _LOGIC_Slv_Xgate2_PMOS_ChannelLength
                ## Slave Nor1
                    ## Nor1 common
        _Caculation_Parameters1['_Slv_Nor1_XVT'] = _LOGIC_Slv_Nor1_XVT
                    ## NMOS
                        ## NMOSA
        _Caculation_Parameters1['_Slv_Nor1_NMOSA_NumberofGate'] = _LOGIC_Slv_Nor1_NMOSA_NumberofGate
        _Caculation_Parameters1['_Slv_Nor1_NMOSA_ChannelWidth'] = _LOGIC_Slv_Nor1_NMOSA_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor1_NMOSA_ChannelLength'] = _LOGIC_Slv_Nor1_NMOSA_ChannelLength
                        ## NMOSB
        _Caculation_Parameters1['_Slv_Nor1_NMOSB_NumberofGate'] = _LOGIC_Slv_Nor1_NMOSB_NumberofGate
        _Caculation_Parameters1['_Slv_Nor1_NMOSB_ChannelWidth'] = _LOGIC_Slv_Nor1_NMOSB_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor1_NMOSB_ChannelLength'] = _LOGIC_Slv_Nor1_NMOSB_ChannelLength
                    ## PMOS
                        ## PMOSA
        _Caculation_Parameters1['_Slv_Nor1_PMOSA_NumberofGate'] = _LOGIC_Slv_Nor1_PMOSA_NumberofGate
        _Caculation_Parameters1['_Slv_Nor1_PMOSA_ChannelWidth'] = _LOGIC_Slv_Nor1_PMOSA_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor1_PMOSA_ChannelLength'] = _LOGIC_Slv_Nor1_PMOSA_ChannelLength
                        ## PMOSB
        _Caculation_Parameters1['_Slv_Nor1_PMOSB_NumberofGate'] = _LOGIC_Slv_Nor1_PMOSB_NumberofGate
        _Caculation_Parameters1['_Slv_Nor1_PMOSB_ChannelWidth'] = _LOGIC_Slv_Nor1_PMOSB_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor1_PMOSB_ChannelLength'] = _LOGIC_Slv_Nor1_PMOSB_ChannelLength
                ## Slave Nor2
                    ## Nor2 common
        _Caculation_Parameters1['_Slv_Nor2_XVT'] = _LOGIC_Slv_Nor2_XVT
                    ## NMOS
                        ## NMOSA
        _Caculation_Parameters1['_Slv_Nor2_NMOSA_NumberofGate'] = _LOGIC_Slv_Nor2_NMOSA_NumberofGate
        _Caculation_Parameters1['_Slv_Nor2_NMOSA_ChannelWidth'] = _LOGIC_Slv_Nor2_NMOSA_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor2_NMOSA_ChannelLength'] = _LOGIC_Slv_Nor2_NMOSA_ChannelLength
                        ## NMOSB
        _Caculation_Parameters1['_Slv_Nor2_NMOSB_NumberofGate'] = _LOGIC_Slv_Nor2_NMOSB_NumberofGate
        _Caculation_Parameters1['_Slv_Nor2_NMOSB_ChannelWidth'] = _LOGIC_Slv_Nor2_NMOSB_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor2_NMOSB_ChannelLength'] = _LOGIC_Slv_Nor2_NMOSB_ChannelLength
                    ## PMOS
                        ## PMOSA
        _Caculation_Parameters1['_Slv_Nor2_PMOSA_NumberofGate'] = _LOGIC_Slv_Nor2_PMOSA_NumberofGate
        _Caculation_Parameters1['_Slv_Nor2_PMOSA_ChannelWidth'] = _LOGIC_Slv_Nor2_PMOSA_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor2_PMOSA_ChannelLength'] = _LOGIC_Slv_Nor2_PMOSA_ChannelLength
                        ## PMOSB
        _Caculation_Parameters1['_Slv_Nor2_PMOSB_NumberofGate'] = _LOGIC_Slv_Nor2_PMOSB_NumberofGate
        _Caculation_Parameters1['_Slv_Nor2_PMOSB_ChannelWidth'] = _LOGIC_Slv_Nor2_PMOSB_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor2_PMOSB_ChannelLength'] = _LOGIC_Slv_Nor2_PMOSB_ChannelLength
                ## Slave Inv1 : ReSet pre-driver
                    ## Inv1 common
        _Caculation_Parameters1['_Slv_Inv1_XVT'] = _LOGIC_Slv_Inv1_XVT
                    ## Inv1 NMOS
        _Caculation_Parameters1['_Slv_Inv1_NMOS_NumberofGate'] = _LOGIC_Slv_Inv1_NMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Inv1_NMOS_ChannelWidth'] = _LOGIC_Slv_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Inv1_NMOS_ChannelLength'] = _LOGIC_Slv_Inv1_NMOS_ChannelLength
                    ## Inv1 PMOS
        _Caculation_Parameters1['_Slv_Inv1_PMOS_NumberofGate'] = _LOGIC_Slv_Inv1_PMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Inv1_PMOS_ChannelWidth'] = _LOGIC_Slv_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Inv1_PMOS_ChannelLength'] = _LOGIC_Slv_Inv1_PMOS_ChannelLength
                ## Slave Inv2 : ReSet driver
                    ## Inv2 common
        _Caculation_Parameters1['_Slv_Inv2_XVT'] = _LOGIC_Slv_Inv2_XVT
                    ## Inv2 NMOS
        _Caculation_Parameters1['_Slv_Inv2_NMOS_NumberofGate'] = _LOGIC_Slv_Inv2_NMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Inv2_NMOS_ChannelWidth'] = _LOGIC_Slv_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Inv2_NMOS_ChannelLength'] = _LOGIC_Slv_Inv2_NMOS_ChannelLength
                    ## Inv2 PMOS
        _Caculation_Parameters1['_Slv_Inv2_PMOS_NumberofGate'] = _LOGIC_Slv_Inv2_PMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Inv2_PMOS_ChannelWidth'] = _LOGIC_Slv_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Inv2_PMOS_ChannelLength'] = _LOGIC_Slv_Inv2_PMOS_ChannelLength
                ## Slave Inv3 : Qb driver
                    ## Inv3 common
        _Caculation_Parameters1['_Slv_Inv3_XVT'] = _LOGIC_Slv_Inv3_XVT
                    ## Inv3 NMOS
        _Caculation_Parameters1['_Slv_Inv3_NMOS_NumberofGate'] = _LOGIC_Slv_Inv3_NMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Inv3_NMOS_ChannelWidth'] = _LOGIC_Slv_Inv3_NMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Inv3_NMOS_ChannelLength'] = _LOGIC_Slv_Inv3_NMOS_ChannelLength
                    ## Inv3 PMOS
        _Caculation_Parameters1['_Slv_Inv3_PMOS_NumberofGate'] = _LOGIC_Slv_Inv3_PMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Inv3_PMOS_ChannelWidth'] = _LOGIC_Slv_Inv3_PMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Inv3_PMOS_ChannelLength'] = _LOGIC_Slv_Inv3_PMOS_ChannelLength

            ## DAC PreDriver
                ## Inverter Chain
                    ## InvChain Common
        _Caculation_Parameters1['_DACPreDrv_PMOSXvt2NMOSXvt'] = _LOGIC_DACPreDrv_PMOSXvt2NMOSXvt
                ## Inverter Chain
                    ## Inv1 common
        _Caculation_Parameters1['_DACPreDrv_NumberofGate'] = _LOGIC_DACPreDrv_NumberofGate
        _Caculation_Parameters1['_DACPreDrv_ChannelLength'] = _LOGIC_DACPreDrv_ChannelLength
        _Caculation_Parameters1['_DACPreDrv_XVT'] = _LOGIC_DACPreDrv_XVT
                    ## Inv1 NMOS
        _Caculation_Parameters1['_DACPreDrv_Inv_NMOS_ChannelWidth'] = _LOGIC_DACPreDrv_Inv_NMOS_ChannelWidth
                    ## Inv1 PMOS
        _Caculation_Parameters1['_DACPreDrv_Inv_PMOS_ChannelWidth'] = _LOGIC_DACPreDrv_Inv_PMOS_ChannelWidth
            ## CLKOutSamp(!=ClkSamp)
                ## Common
                    # XVT
        _Caculation_Parameters1['_CLKoutSamp_XVT'] = _LOGIC_CLKoutSamp_XVT
                ## Inverter
                    # Nmos
        _Caculation_Parameters1['_CLKoutSamp_Inv_NMOS_NumberofGate'] = _LOGIC_CLKoutSamp_Inv_NMOS_NumberofGate
        _Caculation_Parameters1['_CLKoutSamp_Inv_NMOS_ChannelWidth'] = _LOGIC_CLKoutSamp_Inv_NMOS_ChannelWidth
        _Caculation_Parameters1['_CLKoutSamp_Inv_NMOS_ChannelLength'] = _LOGIC_CLKoutSamp_Inv_NMOS_ChannelLength
                    # Pmos
        _Caculation_Parameters1['_CLKoutSamp_Inv_PMOS_NumberofGate'] = _LOGIC_CLKoutSamp_Inv_PMOS_NumberofGate
        _Caculation_Parameters1['_CLKoutSamp_Inv_PMOS_ChannelWidth'] = _LOGIC_CLKoutSamp_Inv_PMOS_ChannelWidth
        _Caculation_Parameters1['_CLKoutSamp_Inv_PMOS_ChannelLength'] = _LOGIC_CLKoutSamp_Inv_PMOS_ChannelLength
                ## AND
                    ## AND Common
                    ## Nand
                        # NmosA
        _Caculation_Parameters1['_CLKoutSamp_And_Nand_NMOSA_NumberofGate'] = _LOGIC_CLKoutSamp_And_Nand_NMOSA_NumberofGate
        _Caculation_Parameters1['_CLKoutSamp_And_Nand_NMOSA_ChannelWidth'] = _LOGIC_CLKoutSamp_And_Nand_NMOSA_ChannelWidth
        _Caculation_Parameters1['_CLKoutSamp_And_Nand_NMOSA_ChannelLength'] = _LOGIC_CLKoutSamp_And_Nand_NMOSA_ChannelLength
                        # NMOSB
        _Caculation_Parameters1['_CLKoutSamp_And_Nand_NMOSB_NumberofGate'] = _LOGIC_CLKoutSamp_And_Nand_NMOSB_NumberofGate
        _Caculation_Parameters1['_CLKoutSamp_And_Nand_NMOSB_ChannelWidth'] = _LOGIC_CLKoutSamp_And_Nand_NMOSB_ChannelWidth
        _Caculation_Parameters1['_CLKoutSamp_And_Nand_NMOSB_ChannelLength'] = _LOGIC_CLKoutSamp_And_Nand_NMOSB_ChannelLength
                        # PMOSA
        _Caculation_Parameters1['_CLKoutSamp_And_Nand_PMOSA_NumberofGate'] = _LOGIC_CLKoutSamp_And_Nand_PMOSA_NumberofGate
        _Caculation_Parameters1['_CLKoutSamp_And_Nand_PMOSA_ChannelWidth'] = _LOGIC_CLKoutSamp_And_Nand_PMOSA_ChannelWidth
        _Caculation_Parameters1['_CLKoutSamp_And_Nand_PMOSA_ChannelLength'] = _LOGIC_CLKoutSamp_And_Nand_PMOSA_ChannelLength
                        # PMOSB
        _Caculation_Parameters1['_CLKoutSamp_And_Nand_PMOSB_NumberofGate'] = _LOGIC_CLKoutSamp_And_Nand_PMOSB_NumberofGate
        _Caculation_Parameters1['_CLKoutSamp_And_Nand_PMOSB_ChannelWidth'] = _LOGIC_CLKoutSamp_And_Nand_PMOSB_ChannelWidth
        _Caculation_Parameters1['_CLKoutSamp_And_Nand_PMOSB_ChannelLength'] = _LOGIC_CLKoutSamp_And_Nand_PMOSB_ChannelLength
                    ## Inverter
                        # Nmos
        _Caculation_Parameters1['_CLKoutSamp_And_Inv_NMOS_NumberofGate'] = _LOGIC_CLKoutSamp_And_Inv_NMOS_NumberofGate
        _Caculation_Parameters1['_CLKoutSamp_And_Inv_NMOS_ChannelWidth'] = _LOGIC_CLKoutSamp_And_Inv_NMOS_ChannelWidth
        _Caculation_Parameters1['_CLKoutSamp_And_Inv_NMOS_ChannelLength'] = _LOGIC_CLKoutSamp_And_Inv_NMOS_ChannelLength
                        # Pmos
        _Caculation_Parameters1['_CLKoutSamp_And_Inv_PMOS_NumberofGate'] = _LOGIC_CLKoutSamp_And_Inv_PMOS_NumberofGate
        _Caculation_Parameters1['_CLKoutSamp_And_Inv_PMOS_ChannelWidth'] = _LOGIC_CLKoutSamp_And_Inv_PMOS_ChannelWidth
        _Caculation_Parameters1['_CLKoutSamp_And_Inv_PMOS_ChannelLength'] = _LOGIC_CLKoutSamp_And_Inv_PMOS_ChannelLength

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



        ############################################################################################################################################################
        #### Comparator With SR Latch And Clock In Logic SREF Generation
        ## StrongARM Latch
        _Caculation_Parameters2 = copy.deepcopy(E01_05_StrongArmWtSRLatch._StrongArmWtSRLatch._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters1['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length

        ## Comparator
            ## StrongARM Latch
                # Common
        _Caculation_Parameters2['_SALatch_ChannelLength'] = _COMP_SALatch_ChannelLength
        _Caculation_Parameters2['_SALatch_XVT'] = _COMP_SALatch_XVT
                # PMOS
        _Caculation_Parameters2['_SALatch_CLKinputPMOSFinger1'] = _COMP_SALatch_CLKinputPMOSFinger1
        _Caculation_Parameters2['_SALatch_CLKinputPMOSFinger2'] = _COMP_SALatch_CLKinputPMOSFinger2
        _Caculation_Parameters2['_SALatch_PMOSFinger'] = _COMP_SALatch_PMOSFinger
        _Caculation_Parameters2['_SALatch_PMOSChannelWidth'] = _COMP_SALatch_PMOSChannelWidth
                # NMOS
        _Caculation_Parameters2['_SALatch_DATAinputNMOSFinger'] = _COMP_SALatch_DATAinputNMOSFinger
        _Caculation_Parameters2['_SALatch_NMOSFinger'] = _COMP_SALatch_NMOSFinger
        _Caculation_Parameters2['_SALatch_CLKinputNMOSFinger'] = _COMP_SALatch_CLKinputNMOSFinger
        _Caculation_Parameters2['_SALatch_NMOSChannelWidth'] = _COMP_SALatch_NMOSChannelWidth
        _Caculation_Parameters2['_SALatch_CLKinputNMOSChannelWidth'] = _COMP_SALatch_CLKinputNMOSChannelWidth
            ## StrongArmOutBuffer and SRLatch
                ## Common
                    # XVT
        _Caculation_Parameters2['_SAOutBufAndSRLatch_XVT'] = _COMP_SAOutBufAndSRLatch_XVT
                    # Body
        _Caculation_Parameters2['_SAOutBufAndSRLatch_NMOS_Pbody_XvtTop2Pbody'] = _COMP_SAOutBufAndSRLatch_NMOS_Pbody_XvtTop2Pbody
        _Caculation_Parameters2['_SAOutBufAndSRLatch_PMOS_Nbody_Xvtdown2Nbody'] = _COMP_SAOutBufAndSRLatch_PMOS_Nbody_Xvtdown2Nbody
                    # Height
        _Caculation_Parameters2['_SAOutBufAndSRLatch_PMOSXvt2NMOSXvt'] = _COMP_SAOutBufAndSRLatch_PMOSXvt2NMOSXvt
                ## StronArm Output Buffer
                    ## Inverter1(pre)
                        # Nmos
        _Caculation_Parameters2['_SAOutBuf_Buf_Inv1_NMOS_NumberofGate'] = _COMP_SAOutBuf_Buf_Inv1_NMOS_NumberofGate
        _Caculation_Parameters2['_SAOutBuf_Buf_Inv1_NMOS_ChannelWidth'] = _COMP_SAOutBuf_Buf_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters2['_SAOutBuf_Buf_Inv1_NMOS_ChannelLength'] = _COMP_SAOutBuf_Buf_Inv1_NMOS_ChannelLength
                        # Pmos
        _Caculation_Parameters2['_SAOutBuf_Buf_Inv1_PMOS_NumberofGate'] = _COMP_SAOutBuf_Buf_Inv1_PMOS_NumberofGate
        _Caculation_Parameters2['_SAOutBuf_Buf_Inv1_PMOS_ChannelWidth'] = _COMP_SAOutBuf_Buf_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters2['_SAOutBuf_Buf_Inv1_PMOS_ChannelLength'] = _COMP_SAOutBuf_Buf_Inv1_PMOS_ChannelLength
                    ## Inverter2
                        # Nmos
        _Caculation_Parameters2['_SAOutBuf_Buf_Inv2_NMOS_NumberofGate'] = _COMP_SAOutBuf_Buf_Inv2_NMOS_NumberofGate
        _Caculation_Parameters2['_SAOutBuf_Buf_Inv2_NMOS_ChannelWidth'] = _COMP_SAOutBuf_Buf_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters2['_SAOutBuf_Buf_Inv2_NMOS_ChannelLength'] = _COMP_SAOutBuf_Buf_Inv2_NMOS_ChannelLength
                        # Pmos
        _Caculation_Parameters2['_SAOutBuf_Buf_Inv2_PMOS_NumberofGate'] = _COMP_SAOutBuf_Buf_Inv2_PMOS_NumberofGate
        _Caculation_Parameters2['_SAOutBuf_Buf_Inv2_PMOS_ChannelWidth'] = _COMP_SAOutBuf_Buf_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters2['_SAOutBuf_Buf_Inv2_PMOS_ChannelLength'] = _COMP_SAOutBuf_Buf_Inv2_PMOS_ChannelLength
                ## SRLatch
                    ## Nand(Set,Rst same)
                        # NmosA
        _Caculation_Parameters2['_SRLatch_Nand_NMOSA_NumberofGate'] = _COMP_SRLatch_Nand_NMOSA_NumberofGate
        _Caculation_Parameters2['_SRLatch_Nand_NMOSA_ChannelWidth'] = _COMP_SRLatch_Nand_NMOSA_ChannelWidth
        _Caculation_Parameters2['_SRLatch_Nand_NMOSA_ChannelLength'] = _COMP_SRLatch_Nand_NMOSA_ChannelLength
                        # NMOSB
        _Caculation_Parameters2['_SRLatch_Nand_NMOSB_NumberofGate'] = _COMP_SRLatch_Nand_NMOSB_NumberofGate
        _Caculation_Parameters2['_SRLatch_Nand_NMOSB_ChannelWidth'] = _COMP_SRLatch_Nand_NMOSB_ChannelWidth
        _Caculation_Parameters2['_SRLatch_Nand_NMOSB_ChannelLength'] = _COMP_SRLatch_Nand_NMOSB_ChannelLength
                        # PMOSA
        _Caculation_Parameters2['_SRLatch_Nand_PMOSA_NumberofGate'] = _COMP_SRLatch_Nand_PMOSA_NumberofGate
        _Caculation_Parameters2['_SRLatch_Nand_PMOSA_ChannelWidth'] = _COMP_SRLatch_Nand_PMOSA_ChannelWidth
        _Caculation_Parameters2['_SRLatch_Nand_PMOSA_ChannelLength'] = _COMP_SRLatch_Nand_PMOSA_ChannelLength
                        # PMOSB
        _Caculation_Parameters2['_SRLatch_Nand_PMOSB_NumberofGate'] = _COMP_SRLatch_Nand_PMOSB_NumberofGate
        _Caculation_Parameters2['_SRLatch_Nand_PMOSB_ChannelWidth'] = _COMP_SRLatch_Nand_PMOSB_ChannelWidth
        _Caculation_Parameters2['_SRLatch_Nand_PMOSB_ChannelLength'] = _COMP_SRLatch_Nand_PMOSB_ChannelLength
            ## Comp clock Gen Logic: Clk_Samp Inv, Clk_Source Inv, AND Gate, CompClockBuff
                ## Common
                    # XVT
        _Caculation_Parameters2['_CompClkLogic_XVT'] = _COMP_CompClkLogic_XVT
                    # Body
        _Caculation_Parameters2['_CompClkLogic_NMOS_Pbody_XvtTop2Pbody'] = _COMP_CompClkLogic_NMOS_Pbody_XvtTop2Pbody
        _Caculation_Parameters2['_CompClkLogic_PMOS_Nbody_Xvtdown2Nbody'] = _COMP_CompClkLogic_PMOS_Nbody_Xvtdown2Nbody
                    # Height
        _Caculation_Parameters2['_CompClkLogic_PMOSXvt2NMOSXvt'] = _COMP_CompClkLogic_PMOSXvt2NMOSXvt
                ## StronArm Output Buffer
                    ## Inverter1(pre)
                        #Nmos
        _Caculation_Parameters2['_CompClkLogic_Buf_Inv1_NMOS_NumberofGate'] = _COMP_CompClkLogic_Buf_Inv1_NMOS_NumberofGate
        _Caculation_Parameters2['_CompClkLogic_Buf_Inv1_NMOS_ChannelWidth'] = _COMP_CompClkLogic_Buf_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters2['_CompClkLogic_Buf_Inv1_NMOS_ChannelLength'] = _COMP_CompClkLogic_Buf_Inv1_NMOS_ChannelLength
                        # Pmos
        _Caculation_Parameters2['_CompClkLogic_Buf_Inv1_PMOS_NumberofGate'] = _COMP_CompClkLogic_Buf_Inv1_PMOS_NumberofGate
        _Caculation_Parameters2['_CompClkLogic_Buf_Inv1_PMOS_ChannelWidth'] = _COMP_CompClkLogic_Buf_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters2['_CompClkLogic_Buf_Inv1_PMOS_ChannelLength'] = _COMP_CompClkLogic_Buf_Inv1_PMOS_ChannelLength
                    ## Inverter2
                        # Nmos
        _Caculation_Parameters2['_CompClkLogic_Buf_Inv2_NMOS_NumberofGate'] = _COMP_CompClkLogic_Buf_Inv2_NMOS_NumberofGate
        _Caculation_Parameters2['_CompClkLogic_Buf_Inv2_NMOS_ChannelWidth'] = _COMP_CompClkLogic_Buf_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters2['_CompClkLogic_Buf_Inv2_NMOS_ChannelLength'] = _COMP_CompClkLogic_Buf_Inv2_NMOS_ChannelLength
                        # Pmos
        _Caculation_Parameters2['_CompClkLogic_Buf_Inv2_PMOS_NumberofGate'] = _COMP_CompClkLogic_Buf_Inv2_PMOS_NumberofGate
        _Caculation_Parameters2['_CompClkLogic_Buf_Inv2_PMOS_ChannelWidth'] = _COMP_CompClkLogic_Buf_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters2['_CompClkLogic_Buf_Inv2_PMOS_ChannelLength'] = _COMP_CompClkLogic_Buf_Inv2_PMOS_ChannelLength
                ## AND
                    ## Nand
                        # NmosA
        _Caculation_Parameters2['_CompClkLogic_Nand_NMOSA_NumberofGate'] = _COMP_CompClkLogic_Nand_NMOSA_NumberofGate
        _Caculation_Parameters2['_CompClkLogic_Nand_NMOSA_ChannelWidth'] = _COMP_CompClkLogic_Nand_NMOSA_ChannelWidth
        _Caculation_Parameters2['_CompClkLogic_Nand_NMOSA_ChannelLength'] = _COMP_CompClkLogic_Nand_NMOSA_ChannelLength
                        # NMOSB
        _Caculation_Parameters2['_CompClkLogic_Nand_NMOSB_NumberofGate'] = _COMP_CompClkLogic_Nand_NMOSB_NumberofGate
        _Caculation_Parameters2['_CompClkLogic_Nand_NMOSB_ChannelWidth'] = _COMP_CompClkLogic_Nand_NMOSB_ChannelWidth
        _Caculation_Parameters2['_CompClkLogic_Nand_NMOSB_ChannelLength'] = _COMP_CompClkLogic_Nand_NMOSB_ChannelLength
                        # PMOSA
        _Caculation_Parameters2['_CompClkLogic_Nand_PMOSA_NumberofGate'] = _COMP_CompClkLogic_Nand_PMOSA_NumberofGate
        _Caculation_Parameters2['_CompClkLogic_Nand_PMOSA_ChannelWidth'] = _COMP_CompClkLogic_Nand_PMOSA_ChannelWidth
        _Caculation_Parameters2['_CompClkLogic_Nand_PMOSA_ChannelLength'] = _COMP_CompClkLogic_Nand_PMOSA_ChannelLength
                        # PMOSB
        _Caculation_Parameters2['_CompClkLogic_Nand_PMOSB_NumberofGate'] = _COMP_CompClkLogic_Nand_PMOSB_NumberofGate
        _Caculation_Parameters2['_CompClkLogic_Nand_PMOSB_ChannelWidth'] = _COMP_CompClkLogic_Nand_PMOSB_ChannelWidth
        _Caculation_Parameters2['_CompClkLogic_Nand_PMOSB_ChannelLength'] = _COMP_CompClkLogic_Nand_PMOSB_ChannelLength
                    ## Inverter
                        # Nmos
        _Caculation_Parameters2['_CompClkLogic_Inv_NMOS_NumberofGate'] = _COMP_CompClkLogic_Inv_NMOS_NumberofGate
        _Caculation_Parameters2['_CompClkLogic_Inv_NMOS_ChannelWidth'] = _COMP_CompClkLogic_Inv_NMOS_ChannelWidth
        _Caculation_Parameters2['_CompClkLogic_Inv_NMOS_ChannelLength'] = _COMP_CompClkLogic_Inv_NMOS_ChannelLength
                        # Pmos
        _Caculation_Parameters2['_CompClkLogic_Inv_PMOS_NumberofGate'] = _COMP_CompClkLogic_Inv_PMOS_NumberofGate
        _Caculation_Parameters2['_CompClkLogic_Inv_PMOS_ChannelWidth'] = _COMP_CompClkLogic_Inv_PMOS_ChannelWidth
        _Caculation_Parameters2['_CompClkLogic_Inv_PMOS_ChannelLength'] = _COMP_CompClkLogic_Inv_PMOS_ChannelLength
                ## Clk_Source Inv
                        # Nmos
        _Caculation_Parameters2['_CompClkLogic_ClkSrc_NMOS_NumberofGate'] = _COMP_CompClkLogic_ClkSrc_NMOS_NumberofGate
        _Caculation_Parameters2['_CompClkLogic_ClkSrc_NMOS_ChannelWidth'] = _COMP_CompClkLogic_ClkSrc_NMOS_ChannelWidth
        _Caculation_Parameters2['_CompClkLogic_ClkSrc_NMOS_ChannelLength'] = _COMP_CompClkLogic_ClkSrc_NMOS_ChannelLength
                        # Pmos
        _Caculation_Parameters2['_CompClkLogic_ClkSrc_PMOS_NumberofGate'] = _COMP_CompClkLogic_ClkSrc_PMOS_NumberofGate
        _Caculation_Parameters2['_CompClkLogic_ClkSrc_PMOS_ChannelWidth'] = _COMP_CompClkLogic_ClkSrc_PMOS_ChannelWidth
        _Caculation_Parameters2['_CompClkLogic_ClkSrc_PMOS_ChannelLength'] = _COMP_CompClkLogic_ClkSrc_PMOS_ChannelLength
                ## Clk_Samp Inv
                        #Nmos
        _Caculation_Parameters2['_CompClkLogic_ClkSmp_NMOS_NumberofGate'] = _COMP_CompClkLogic_ClkSmp_NMOS_NumberofGate
        _Caculation_Parameters2['_CompClkLogic_ClkSmp_NMOS_ChannelWidth'] = _COMP_CompClkLogic_ClkSmp_NMOS_ChannelWidth
        _Caculation_Parameters2['_CompClkLogic_ClkSmp_NMOS_ChannelLength'] = _COMP_CompClkLogic_ClkSmp_NMOS_ChannelLength
                        # Pmos
        _Caculation_Parameters2['_CompClkLogic_ClkSmp_PMOS_NumberofGate'] = _COMP_CompClkLogic_ClkSmp_PMOS_NumberofGate
        _Caculation_Parameters2['_CompClkLogic_ClkSmp_PMOS_ChannelWidth'] = _COMP_CompClkLogic_ClkSmp_PMOS_ChannelWidth
        _Caculation_Parameters2['_CompClkLogic_ClkSmp_PMOS_ChannelLength'] = _COMP_CompClkLogic_ClkSmp_PMOS_ChannelLength


        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Comparator'] = self._SrefElementDeclaration(_DesignObj=E01_05_StrongArmWtSRLatch._StrongArmWtSRLatch(_DesignParameter=None, _Name='{}:SRF_Comparator'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Comparator']['_Reflect'] = [1, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Comparator']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Comparator']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters2)

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

        ############################################################################################################################################################
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

        ############################################################################################################################################################

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
        tmp1 = self.get_param_KJH4('SRF_SARLogicWtBuffers', 'SRF_SARLogicWtCLKTree', 'SRF_CLKBufferTree_Top', 'SRF_CLKBuf1Inv_Stage1', 'SRF_InputViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        tmp2 = self.get_param_KJH4('SRF_SARLogicWtBuffers', 'SRF_SARLogicWtCLKTree', 'SRF_CLKBufferTree_Top', 'BND_Buf2Stg2to1_Hrz_M3')
        self._DesignParameter['BND_SARCLKSampIn_Vtc_M2']['_YWidth'] = abs(tmp2[0][0][0][0][0]['_XY_up'][1] - tmp1[0][0][0][0][0][0][0][0]['_XY_down'][1]) + CLKSampInHrzMetalWidth + SpaceBtwTreeInternalRoutePathAndCLKSampInHrz + CLKSrcInHrzMetalWidth + SpaceBtwCLKSampInHrzAndCLKSrcInHrz

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

        ############################################################################################################################################################

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

        ############################################################################################################################################################

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

        ############################################################################################################################################################

        ####################################################################################################
        # # Additional Buffer Between CLK_Sample Input of Comparator And Output of Tree Buffer
        _Caculation_Parameters = copy.deepcopy(J00_01_InverterChain_KJH._InverterChain._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']  = _BUF_CLKSamp_PMOSXvt2NMOSXvt

        _Caculation_Parameters['_NumberofGate']     = _BUF_CLKSamp_NumberofGate
        _Caculation_Parameters['_ChannelLength']    = _BUF_CLKSamp_ChanneLength
        _Caculation_Parameters['_XVT']              = _BUF_CLKSamp_XVT

        _Caculation_Parameters['_Inv_NMOS_ChannelWidth'] = _BUF_CLKSamp_NMOSChannelWidth

        _Caculation_Parameters['_Inv_PMOS_ChannelWidth'] = _BUF_CLKSamp_PMOSChannelWidth

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Buf_CLKSamp'] = self._SrefElementDeclaration(_DesignObj=J00_01_InverterChain_KJH._InverterChain(_DesignParameter=None,_Name='{}:SRF_Buf_CLKSamp'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Buf_CLKSamp']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Buf_CLKSamp']['_Angle'] = 180

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Buf_CLKSamp']['_DesignObj']._CalculateDesignParameter( **_Caculation_Parameters)

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

        ############################################################################################################################################################
        ####################################################################################################
        # # Additional Buffer Between CLK_Src Input of Comparator And Output of Tree Buffer
        _Caculation_Parameters = copy.deepcopy(J00_01_InverterChain_KJH._InverterChain._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']  = _BUF_CLKScr_PMOSXvt2NMOSXvt

        _Caculation_Parameters['_NumberofGate']     = _BUF_CLKScr_NumberofGate
        _Caculation_Parameters['_ChannelLength']    = _BUF_CLKScr_ChanneLength
        _Caculation_Parameters['_XVT']              = _BUF_CLKScr_XVT

        _Caculation_Parameters['_Inv_NMOS_ChannelWidth'] = _BUF_CLKScr_NMOSChannelWidth

        _Caculation_Parameters['_Inv_PMOS_ChannelWidth'] = _BUF_CLKScr_PMOSChannelWidth

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Buf_CLKSrc'] = self._SrefElementDeclaration(_DesignObj=J00_01_InverterChain_KJH._InverterChain(_DesignParameter=None,_Name='{}:SRF_Buf_CLKSrc'.format(_Name)))[0]

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

        ############################################################################################################################################################
        ### Output Path Metal을 3으로 쓰기 위해 삭제
        del (self._DesignParameter['SRF_Buf_CLKSrc']['_DesignObj']._DesignParameter['SRF_Output_ViaM2Mx']['_DesignObj']._DesignParameter['SRF_ViaM3M4'])

        ############################################################################################################################################################

        ###### BND_CLKSampIn_Hrz_M3 ViaM2M3 -> BND_BufCLKSampIn_Vtc_M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKSampBuf_ViaM3M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,_Name='{}:SRF_CLKSampBuf_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKSampBuf_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKSampBuf_ViaM3M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKSampBuf_ViaM3M4']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

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

        ############################################################################################################################################################
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
        ############################################################################################################################################################
        ###################### CLKSamp_Buf -> Comparator AND Gate Input Routing
        ### SRF_CLKSamp Output Via를 아래로 조정
        self._DesignParameter['SRF_Buf_CLKSamp']['_DesignObj']._DesignParameter['SRF_Output_ViaM2Mx']['_XYCoordinates'][0][1] = SpaceBtwCLKSrcBufOutHrzAndCLKSampBufOutHrz + CLKSampBufOutHrzMetalWidth + self._DesignParameter['SRF_Buf_CLKSamp']['_DesignObj']._DesignParameter['SRF_Output_ViaM2Mx']['_XYCoordinates'][0][1]

        ############################################################################################################################################################
        ### Output Path Metal을 3으로 쓰기 위해 삭제
        del (self._DesignParameter['SRF_Buf_CLKSamp']['_DesignObj']._DesignParameter['SRF_Output_ViaM2Mx']['_DesignObj']._DesignParameter['SRF_ViaM3M4'])

        ############################################################################################################################################################

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
        self._DesignParameter['BND_CLKSampBufOut_Hrz_M3']['_XWidth'] = (tmp1[0][0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0][0]['_XY_left'][0])

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
        ############################################################################################################################################################

        ###### Via BND_CLKSampBufOut_Hrz_M3 -> BND_CLKSampANDIn_Vtc_M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKSampANDIn_ViaM3M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,_Name='{}:SRF_CLKSampANDIn_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKSampANDIn_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKSampANDIn_ViaM3M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKSampANDIn_ViaM3M4']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

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
        ############################################################################################################################################################

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
        self._DesignParameter['BND_CLKSampANDIn_Vtc_M4']['_YWidth'] = abs(tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0]['_XY_down'][1])

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
        ############################################################################################################################################################

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
        tmp1 = self.get_param_KJH4('SRF_SARLogicWtBuffers', 'SRF_SARLogicWtCLKTree', 'SRF_CLKBufferTree_Top','SRF_CLKBuf2Inv_Stage1', 'SRF_InputViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        tmp2 = self.get_param_KJH4('SRF_SARLogicWtBuffers', 'SRF_SARLogicWtCLKTree', 'SRF_CLKBufferTree_Top', 'BND_Buf2Stg2to1_Hrz_M3')

        self._DesignParameter['BND_SARCLKSrcIn_Vtc_M2']['_YWidth'] = abs(tmp2[0][0][0][0][0]['_XY_up'][1] - tmp1[0][0][0][0][0][0][0][0]['_XY_down'][1]) + CLKSrcInHrzMetalWidth + SpaceBtwCLKSampInHrzAndCLKSrcInHrz

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
        ############################################################################################################################################################

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
        ############################################################################################################################################################

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
        self._DesignParameter['BND_CLKSrcIn_Hrz_M3']['_XWidth'] = abs(tmp1[0][0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0]['_XY_right'][0])

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


        ############################################################################################################################################################

        ###### BND_CLKSrcIn_Hrz_M3 ViaM2M3 -> BND_BufCLKSrcIn_Vtc_M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKSrcBuf_ViaM2M3_2'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_CLKSrcBuf_ViaM2M3_2'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKSrcBuf_ViaM2M3_2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKSrcBuf_ViaM2M3_2']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKSrcBuf_ViaM2M3_2']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKSrcBuf_ViaM2M3_2']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_CLKSrcIn_Hrz_M3')
        target_coord = tmp1[0][0]['_XY_down_left']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CLKSrcBuf_ViaM2M3_2', 'SRF_ViaM2M3', 'BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKSrcBuf_ViaM2M3_2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKSrcBuf_ViaM2M3_2']['_XYCoordinates'] = tmpXY
        ############################################################################################################################################################

        ##### BND_BufCLKSrcIn_Vtc_M2
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_BufCLKSrcIn_Vtc_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        tmp1 = self.get_param_KJH4('SRF_Buf_CLKSrc', 'SRF_Input_ViaM1Mx', 'SRF_ViaM1M2', 'BND_Met2Layer')
        tmp2 = self.get_param_KJH4('BND_CLKSrcIn_Hrz_M3')
        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_BufCLKSrcIn_Vtc_M2']['_XWidth'] = CLKSrcInVtcM4MetalWidth

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_BufCLKSrcIn_Vtc_M2']['_YWidth'] = abs(
            tmp1[0][0][0][0][0]['_XY_down'][1] - tmp2[0][0]['_XY_down'][1])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_BufCLKSrcIn_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp2[0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_BufCLKSrcIn_Vtc_M2')
        approaching_coord = tmp2[0][0]['_XY_down_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_BufCLKSrcIn_Vtc_M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_BufCLKSrcIn_Vtc_M2']['_XYCoordinates'] = tmpXY
        ############################################################################################################################################################

        del (self._DesignParameter['SRF_Buf_CLKSrc']['_DesignObj']._DesignParameter['SRF_Input_ViaM1Mx']['_DesignObj']._DesignParameter['SRF_ViaM3M4'])
        del (self._DesignParameter['SRF_Buf_CLKSrc']['_DesignObj']._DesignParameter['SRF_Input_ViaM1Mx']['_DesignObj']._DesignParameter['SRF_ViaM2M3'])

        ############################################################################################################################################################

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
        self._DesignParameter['BND_CLKSrcBufOut_Hrz_M3']['_XWidth'] = (tmp1[0][0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0][0]['_XY_right'][0])

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
        ############################################################################################################################################################

        ###### BND_CLKSrcBufOut_Hrz_M3 -> BND_CLKSrcANDIn_Vtc_M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKSrcANDIn_ViaM3M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,_Name='{}:SRF_CLKSrcANDIn_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKSrcANDIn_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKSrcANDIn_ViaM3M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKSrcANDIn_ViaM3M4']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

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
        approaching_coord = tmp2[0][0][0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKSrcANDIn_ViaM3M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKSrcANDIn_ViaM3M4']['_XYCoordinates'] = tmpXY
        ############################################################################################################################################################

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
        target_coord = tmp1[0][0][0][0]['_XY_up_right']
        ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_CLKSrcANDIn_Vtc_M4')
        approaching_coord = tmp3[0][0]['_XY_up_right']
        ## Sref coord
        tmp4 = self.get_param_KJH4('BND_CLKSrcANDIn_Vtc_M4')
        Scoord = tmp4[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CLKSrcANDIn_Vtc_M4']['_XYCoordinates'] = tmpXY


        ############################################################################################################################################################
        ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
        ######################### CompOut Routing ##########################################
        # # Additional Buffer Between <CompOut> Input of Comparator And Output of Tree Buffer
        _Caculation_Parameters = copy.deepcopy(J00_01_InverterChain_KJH._InverterChain._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']  = _BUF_CompOut_PMOSXvt2NMOSXvt

        _Caculation_Parameters['_NumberofGate']     = _BUF_CompOut_NumberofGate
        _Caculation_Parameters['_ChannelLength']    = _BUF_CompOut_ChanneLength
        _Caculation_Parameters['_XVT']              = _BUF_CompOut_XVT

        _Caculation_Parameters['_Inv_NMOS_ChannelWidth'] = _BUF_CompOut_NMOSChannelWidth

        _Caculation_Parameters['_Inv_PMOS_ChannelWidth'] = _BUF_CompOut_PMOSChannelWidth

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Buf_CompOut'] = self._SrefElementDeclaration(_DesignObj=J00_01_InverterChain_KJH._InverterChain(_DesignParameter=None,_Name='{}:SRF_Buf_CompOut'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Buf_CompOut']['_Reflect'] = [1, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Buf_CompOut']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Buf_CompOut']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

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
        ############################################################################################################################################################
        ### Input Path Metal을 3으로 쓰기 위해 삭제
        del (self._DesignParameter['SRF_Buf_CompOut']['_DesignObj']._DesignParameter['SRF_Input_ViaM1Mx']['_DesignObj']._DesignParameter['SRF_ViaM3M4'])

        ############################################################################################################################################################

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
        self._DesignParameter['BND_CompOut_Hrz_M3']['_XWidth'] = abs(tmp2_1[0][0][0][0][0][0]['_XY_left'][0] - tmp2_2[0][0][0]['_XY_right'][0])

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
        ############################################################################################################################################################

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
        ############################################################################################################################################################

        ###### Via BND_CompOut_Vtc_M4 -> BND_CompOutBufIn_Hrz_M3
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CompOut_ViaM3M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,_Name='{}:SRF_CompOut_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CompOut_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CompOut_ViaM3M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CompOut_ViaM3M4']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

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
        ############################################################################################################################################################

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
        ############################################################################################################################################################

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
        ############################################################################################################################################################

        ###### BND_CompOutTreeBufIn_Vtc_M2 -> BND_CompOutTreeBufIn_Hrz_M3 ViaM2M3
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CompOutTreeBufIn_ViaM2M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,_Name='{}:SRF_CompOutTreeBufIn_ViaM2M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CompOutTreeBufIn_ViaM2M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CompOutTreeBufIn_ViaM2M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CompOutTreeBufIn_ViaM2M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

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
        ############################################################################################################################################################

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
        self._DesignParameter['BND_CompOutTreeBufIn_Hrz_M3']['_XWidth'] = abs(tmp1[0][0]['_XY_right'][0] - tmp2[0][0][0][0][0]['_XY_right'][0])

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
        ############################################################################################################################################################

        ###### SRF_BufCompOutBufOutput_ViaM3M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_BufCompOutBufOutput_ViaM3M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,_Name='{}:SRF_BufCompOutBufOutput_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_BufCompOutBufOutput_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_BufCompOutBufOutput_ViaM3M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_BufCompOutBufOutput_ViaM3M4']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

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

        ############################################################################################################################################################

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
        self._DesignParameter['BND_BufCompOutBufOutput_Vtc_M4']['_YWidth'] = abs(tmp2[0][0][0][0][0]['_XY_up'][1] - tmp1[0][0]['_XY_up'][1])

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
        ############################################################################################################################################################

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
        tmp1 = self.get_param_KJH4('SRF_SARLogicWtBuffers', 'SRF_SARLogicWtCLKTree', 'SRF_CLKBufferTree_Bot','SRF_CLKBuf2Inv_Stage1', 'SRF_InputViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        tmp2 = self.get_param_KJH4('SRF_SARLogicWtBuffers', 'SRF_SARLogicWtCLKTree', 'SRF_CLKBufferTree_Bot','BND_Buf1Stg2to1_Hrz_M3')
        self._DesignParameter['BND_CLKDOut_Vtc_M2']['_YWidth'] = abs(tmp2[0][0][0][0][0]['_XY_down'][1] - tmp1[0][0][0][0][0][0][0][0]['_XY_up'][1]) + CompOutSARLogicTreeBufInHrzMetalWidth + SpaceBtwTreeInternalRoutePathAndCompOut + CLKDoutMetalWidth + SpaceBtwCompOutAndCLKDout

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
        ############################################################################################################################################################

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
        self._DesignParameter['BND_CLKDoutANDOut_Vtc_M4']['_YWidth'] = abs(tmp1[0][0][0][0][0]['_XY_up'][1] - tmp2[0][0]['_XY_down'][1])

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
        ############################################################################################################################################################

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
        ############################################################################################################################################################

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
        ############################################################################################################################################################

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
        ############################################################################################################################################################

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
        ############################################################################################################################################################

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
        ############################################################################################################################################################
        ############################################################################################################################################################
        ############################################################################################################################################################
        ############################################################################################################################################################
        ############################################################################################################################################################
        ############################################################################################################################################################
        ############################################################################################################################################################
        ############################################################################################################################################################
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')
        SARLogicWtComparator_end_time = time.time()
        self.SARLogicWtComparator_elapsed_time = SARLogicWtComparator_end_time - SARLogicWtComparator_start_time
        ############################################################################################################################################################



############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ZZ01_L00_SARLogicWtConmparator_Fixed'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'L00_00_SARLogicWtComparator_RCHybrid'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
_NumofBit = 5,

## SAR Logic
    ## Clock Tree (Driving SAR Logic)
        ## Clock Tree Updward (CLK Source Tree, CLK Samp Tree)
            ## CLK Buffer Unit
                ## Common
                _LOGIC_CLKBufTreeTop_UnitBuf_XVT='SLVT',
                ## Nmos
                _LOGIC_CLKBufTreeTop_UnitBuf_NMOS_NumberofGate=1,  # Number
                _LOGIC_CLKBufTreeTop_UnitBuf_NMOS_ChannelWidth=400,  # Number
                _LOGIC_CLKBufTreeTop_UnitBuf_NMOS_ChannelLength=30,  # Number
                ## Pmos
                _LOGIC_CLKBufTreeTop_UnitBuf_PMOS_NumberofGate=1,  # Number
                _LOGIC_CLKBufTreeTop_UnitBuf_PMOS_ChannelWidth=800,  # Number
                _LOGIC_CLKBufTreeTop_UnitBuf_PMOS_ChannelLength=30,  # Number
                # Height
                _LOGIC_CLKBufTreeTop_UnitBuf_PMOSXvt2NMOSXvt=446,  # number
            ## Clock Buffer Tree structure
            _LOGIC_CLKBufTreeTop_BufTree1and2_NumOfStage=4,  # len[Buf0, Buf1, ... ] 스테이지 수 (아래 버퍼 사이즈 리스트의 길이와 같아야 함.)
            _LOGIC_CLKBufTreeTop_BufTree1_SizeofEachStage=[1, 2, 4, 8],  # CLKSampBuf: [Buf0, Buf1, Buf2 ...]
            _LOGIC_CLKBufTreeTop_BufTree2_SizeofEachStage=[1, 2, 4, 8],  # CLKSrcBuf: [Buf0, Buf1, Buf2 ...]
            _LOGIC_CLKBufTreeTop_XOffSet=0,
        ## Clock Tree Dnward (CLK Source Tree, CLK Samp Tree)
            ## CLK Buffer Unit
                ## Common
                _LOGIC_CLKBufTreeBot_UnitBuf_XVT='SLVT',
                ## Nmos
                _LOGIC_CLKBufTreeBot_UnitBuf_NMOS_NumberofGate=1,  # Number
                _LOGIC_CLKBufTreeBot_UnitBuf_NMOS_ChannelWidth=400,  # Number
                _LOGIC_CLKBufTreeBot_UnitBuf_NMOS_ChannelLength=30,  # Number
                ## Pmos
                _LOGIC_CLKBufTreeBot_UnitBuf_PMOS_NumberofGate=1,  # Number
                _LOGIC_CLKBufTreeBot_UnitBuf_PMOS_ChannelWidth=800,  # Number
                _LOGIC_CLKBufTreeBot_UnitBuf_PMOS_ChannelLength=30,  # Number
                # Height
                _LOGIC_CLKBufTreeBot_UnitBuf_PMOSXvt2NMOSXvt=446,  # number
            ## Clock Buffer Tree structure
            _LOGIC_CLKBufTreeBot_BufTree1and2_NumOfStage=4,  # len[Buf0, Buf1, ... ] 스테이지 수 (아래 버퍼 사이즈 리스트의 길이와 같아야 함.)
            _LOGIC_CLKBufTreeBot_BufTree1_SizeofEachStage=[1, 2, 4, 8],  # CompOutBuf: [Buf0, Buf1, Buf2 ...]
            _LOGIC_CLKBufTreeBot_BufTree2_SizeofEachStage=[1, 2, 4, 8],  # CLKDoutBuf: [Buf0, Buf1, Buf2 ...]
            _LOGIC_CLKBufTreeBot_XOffSet=0,

    ## Clock Spine (Physical demension)
        ## CLK Source: upward, 1st floor
        _LOGIC_YWidthOfCLKSrc=100,
        ## CLK Samp: upward, 2nd floor
        _LOGIC_SpaceBtwCLKSrcAndCLKSamp=100,
        _LOGIC_YWidthOfCLKSamp=100,
        ## Comparator Output: downward, Basement1
        _LOGIC_YWidthOfCompOut=100,
        ## CLK Dout: downward, basement2
        _LOGIC_SpaceBtwCompOutAndCLKDout=100,
        _LOGIC_YWidthOfCLKDout=100,

    ## SetResetDFF
        ## DFF Common
        _LOGIC_Test_distance=320,
        _LOGIC_DFF_PMOSXvt2NMOSXvt    = 1150, # number

        ## Master Xgate1
            ## Xgate common
            _LOGIC_Mst_Xgate1_XVT='SLVT',
            ## Xgate NMOS
            _LOGIC_Mst_Xgate1_NMOS_NumberofGate=1,
            _LOGIC_Mst_Xgate1_NMOS_ChannelWidth=300,
            _LOGIC_Mst_Xgate1_NMOS_ChannelLength=30,
            ## Xgate PMOS
            _LOGIC_Mst_Xgate1_PMOS_NumberofGate=3,
            _LOGIC_Mst_Xgate1_PMOS_ChannelWidth=500,
            _LOGIC_Mst_Xgate1_PMOS_ChannelLength=30,

        ## Master Xgate2
            ## Xgate common
            _LOGIC_Mst_Xgate2_XVT='SLVT',
            ## Xgate NMOS
            _LOGIC_Mst_Xgate2_NMOS_NumberofGate           = 2,
            _LOGIC_Mst_Xgate2_NMOS_ChannelWidth           = 800,
            _LOGIC_Mst_Xgate2_NMOS_ChannelLength          = 30,
            ## Xgate PMOS
            _LOGIC_Mst_Xgate2_PMOS_NumberofGate           = 3,
            _LOGIC_Mst_Xgate2_PMOS_ChannelWidth           = 200,
            _LOGIC_Mst_Xgate2_PMOS_ChannelLength          = 30,

        ## Master Nor1
            ## Nor1 common
            _LOGIC_Mst_Nor1_XVT='SLVT',
            ## NMOS
                ## NMOSA
                _LOGIC_Mst_Nor1_NMOSA_NumberofGate           = 2,
                _LOGIC_Mst_Nor1_NMOSA_ChannelWidth           = 800,
                _LOGIC_Mst_Nor1_NMOSA_ChannelLength          = 30,
                ## NMOSB
                _LOGIC_Mst_Nor1_NMOSB_NumberofGate           = 3,
                _LOGIC_Mst_Nor1_NMOSB_ChannelWidth           = 200,
                _LOGIC_Mst_Nor1_NMOSB_ChannelLength          = 30,
            ## PMOS
                ## PMOSA
                _LOGIC_Mst_Nor1_PMOSA_NumberofGate            = 2,
                _LOGIC_Mst_Nor1_PMOSA_ChannelWidth            = 800,
                _LOGIC_Mst_Nor1_PMOSA_ChannelLength           = 30,
                ## PMOSB
                _LOGIC_Mst_Nor1_PMOSB_NumberofGate            = 3,
                _LOGIC_Mst_Nor1_PMOSB_ChannelWidth            = 200,
                _LOGIC_Mst_Nor1_PMOSB_ChannelLength           = 30,

        ## Master Nor2
            ## Nor2 common
            _LOGIC_Mst_Nor2_XVT='SLVT',
            ## NMOS
                ## NMOSA
                _LOGIC_Mst_Nor2_NMOSA_NumberofGate           = 2,
                _LOGIC_Mst_Nor2_NMOSA_ChannelWidth           = 800,
                _LOGIC_Mst_Nor2_NMOSA_ChannelLength          = 30,
                ## NMOSB
                _LOGIC_Mst_Nor2_NMOSB_NumberofGate           = 3,
                _LOGIC_Mst_Nor2_NMOSB_ChannelWidth           = 200,
                _LOGIC_Mst_Nor2_NMOSB_ChannelLength          = 30,
            ## PMOS
                ## PMOSA
                _LOGIC_Mst_Nor2_PMOSA_NumberofGate            = 2,
                _LOGIC_Mst_Nor2_PMOSA_ChannelWidth            = 800,
                _LOGIC_Mst_Nor2_PMOSA_ChannelLength           = 30,
                ## PMOSB
                _LOGIC_Mst_Nor2_PMOSB_NumberofGate            = 3,
                _LOGIC_Mst_Nor2_PMOSB_ChannelWidth            = 200,
                _LOGIC_Mst_Nor2_PMOSB_ChannelLength           = 30,

        ## Master Inv1 : Set pre-driver
            ## Inv1 common
            _LOGIC_Mst_Inv1_XVT='SLVT',
            ## Inv1 NMOS
            _LOGIC_Mst_Inv1_NMOS_NumberofGate           = 1,
            _LOGIC_Mst_Inv1_NMOS_ChannelWidth           = 300,
            _LOGIC_Mst_Inv1_NMOS_ChannelLength          = 30,
            ## Inv1 PMOS
            _LOGIC_Mst_Inv1_PMOS_NumberofGate           = 3,
            _LOGIC_Mst_Inv1_PMOS_ChannelWidth           = 500,
            _LOGIC_Mst_Inv1_PMOS_ChannelLength          = 30,

        ## Master Inv2 : Set driver
            ## Inv2 common
            _LOGIC_Mst_Inv2_XVT='SLVT',
            ## Inv2 NMOS
            _LOGIC_Mst_Inv2_NMOS_NumberofGate           = 1,
            _LOGIC_Mst_Inv2_NMOS_ChannelWidth           = 300,
            _LOGIC_Mst_Inv2_NMOS_ChannelLength          = 30,
            ## Inv2 PMOS
            _LOGIC_Mst_Inv2_PMOS_NumberofGate           = 3,
            _LOGIC_Mst_Inv2_PMOS_ChannelWidth           = 500,
            _LOGIC_Mst_Inv2_PMOS_ChannelLength          = 30,

        ## Master Inv3 : Clock driver
            ## Inv3 common
            _LOGIC_Mst_Inv3_XVT='SLVT',
            ## Inv3 NMOS
            _LOGIC_Mst_Inv3_NMOS_NumberofGate           = 1,
            _LOGIC_Mst_Inv3_NMOS_ChannelWidth           = 300,
            _LOGIC_Mst_Inv3_NMOS_ChannelLength          = 30,
            ## Inv3 PMOS
            _LOGIC_Mst_Inv3_PMOS_NumberofGate           = 3,
            _LOGIC_Mst_Inv3_PMOS_ChannelWidth           = 500,
            _LOGIC_Mst_Inv3_PMOS_ChannelLength          = 30,

        ## Slave Xgate1
            ## Xgate common
            _LOGIC_Slv_Xgate1_XVT='SLVT',
            ## Xgate NMOS
            _LOGIC_Slv_Xgate1_NMOS_NumberofGate           = 1,
            _LOGIC_Slv_Xgate1_NMOS_ChannelWidth           = 300,
            _LOGIC_Slv_Xgate1_NMOS_ChannelLength          = 30,
            ## Xgate PMOS
            _LOGIC_Slv_Xgate1_PMOS_NumberofGate           = 3,
            _LOGIC_Slv_Xgate1_PMOS_ChannelWidth           = 500,
            _LOGIC_Slv_Xgate1_PMOS_ChannelLength          = 30,

        ## Slave Xgate2
            ## Xgate common
            _LOGIC_Slv_Xgate2_XVT='SLVT',
            ## Xgate NMOS
            _LOGIC_Slv_Xgate2_NMOS_NumberofGate           = 2,
            _LOGIC_Slv_Xgate2_NMOS_ChannelWidth           = 800,
            _LOGIC_Slv_Xgate2_NMOS_ChannelLength          = 30,
            ## Xgate PMOS
            _LOGIC_Slv_Xgate2_PMOS_NumberofGate           = 3,
            _LOGIC_Slv_Xgate2_PMOS_ChannelWidth           = 200,
            _LOGIC_Slv_Xgate2_PMOS_ChannelLength          = 30,

        ## Slave Nor1
            ## Nor1 common
            _LOGIC_Slv_Nor1_XVT='SLVT',
            ## NMOS
                ## NMOSA
                _LOGIC_Slv_Nor1_NMOSA_NumberofGate           = 2,
                _LOGIC_Slv_Nor1_NMOSA_ChannelWidth           = 800,
                _LOGIC_Slv_Nor1_NMOSA_ChannelLength          = 30,
                ## NMOSB
                _LOGIC_Slv_Nor1_NMOSB_NumberofGate           = 3,
                _LOGIC_Slv_Nor1_NMOSB_ChannelWidth           = 200,
                _LOGIC_Slv_Nor1_NMOSB_ChannelLength          = 30,
            ## PMOS
                ## PMOSA
                _LOGIC_Slv_Nor1_PMOSA_NumberofGate            = 2,
                _LOGIC_Slv_Nor1_PMOSA_ChannelWidth            = 800,
                _LOGIC_Slv_Nor1_PMOSA_ChannelLength           = 30,
                ## PMOSB
                _LOGIC_Slv_Nor1_PMOSB_NumberofGate            = 3,
                _LOGIC_Slv_Nor1_PMOSB_ChannelWidth            = 200,
                _LOGIC_Slv_Nor1_PMOSB_ChannelLength           = 30,

        ## Slave Nor2
            ## Nor2 common
            _LOGIC_Slv_Nor2_XVT='SLVT',
            ## NMOS
                ## NMOSA
                _LOGIC_Slv_Nor2_NMOSA_NumberofGate           = 2,
                _LOGIC_Slv_Nor2_NMOSA_ChannelWidth           = 800,
                _LOGIC_Slv_Nor2_NMOSA_ChannelLength          = 30,
                ## NMOSB
                _LOGIC_Slv_Nor2_NMOSB_NumberofGate           = 3,
                _LOGIC_Slv_Nor2_NMOSB_ChannelWidth           = 200,
                _LOGIC_Slv_Nor2_NMOSB_ChannelLength          = 30,
            ## PMOS
                ## PMOSA
                _LOGIC_Slv_Nor2_PMOSA_NumberofGate            = 2,
                _LOGIC_Slv_Nor2_PMOSA_ChannelWidth            = 800,
                _LOGIC_Slv_Nor2_PMOSA_ChannelLength           = 30,
                ## PMOSB
                _LOGIC_Slv_Nor2_PMOSB_NumberofGate            = 3,
                _LOGIC_Slv_Nor2_PMOSB_ChannelWidth            = 200,
                _LOGIC_Slv_Nor2_PMOSB_ChannelLength           = 30,

        ## Slave Inv1 : ReSet pre-driver
            ## Inv1 common
            _LOGIC_Slv_Inv1_XVT='SLVT',
            ## Inv1 NMOS
            _LOGIC_Slv_Inv1_NMOS_NumberofGate           = 1,
            _LOGIC_Slv_Inv1_NMOS_ChannelWidth           = 300,
            _LOGIC_Slv_Inv1_NMOS_ChannelLength          = 30,
            ## Inv1 PMOS
            _LOGIC_Slv_Inv1_PMOS_NumberofGate           = 3,
            _LOGIC_Slv_Inv1_PMOS_ChannelWidth           = 500,
            _LOGIC_Slv_Inv1_PMOS_ChannelLength          = 30,

        ## Slave Inv2 : ReSet driver
            ## Inv2 common
            _LOGIC_Slv_Inv2_XVT='SLVT',
            ## Inv2 NMOS
            _LOGIC_Slv_Inv2_NMOS_NumberofGate           = 1,
            _LOGIC_Slv_Inv2_NMOS_ChannelWidth           = 300,
            _LOGIC_Slv_Inv2_NMOS_ChannelLength          = 30,
            ## Inv2 PMOS
            _LOGIC_Slv_Inv2_PMOS_NumberofGate           = 3,
            _LOGIC_Slv_Inv2_PMOS_ChannelWidth           = 500,
            _LOGIC_Slv_Inv2_PMOS_ChannelLength          = 30,

        ## Slave Inv3 : Qb driver
            ## Inv3 common
            _LOGIC_Slv_Inv3_XVT='SLVT',
            ## Inv3 NMOS
            _LOGIC_Slv_Inv3_NMOS_NumberofGate           = 1,
            _LOGIC_Slv_Inv3_NMOS_ChannelWidth           = 300,
            _LOGIC_Slv_Inv3_NMOS_ChannelLength          = 30,
            ## Inv3 PMOS
            _LOGIC_Slv_Inv3_PMOS_NumberofGate           = 3,
            _LOGIC_Slv_Inv3_PMOS_ChannelWidth           = 500,
            _LOGIC_Slv_Inv3_PMOS_ChannelLength          = 30,
    ## DAC PreDriver
        ## Inverter Chain
            ## InvChain Common
            _LOGIC_DACPreDrv_PMOSXvt2NMOSXvt=500,  # number
            ## Inverter Chain
                ## Inv1 common
            _LOGIC_DACPreDrv_NumberofGate=[[1, 2, 4, 8], [1, 2, 4, 8], [1, 2, 4, 8], [2, 2, 2, 2, 2]],  # Vector
            _LOGIC_DACPreDrv_ChannelLength=30,  # Scalar
            _LOGIC_DACPreDrv_XVT='SLVT',  # 'SLVT'
                ## Inv1 NMOS
            _LOGIC_DACPreDrv_Inv_NMOS_ChannelWidth=400,  # Scalar
                ## Inv1 PMOS
            _LOGIC_DACPreDrv_Inv_PMOS_ChannelWidth=800,  # Scalar
    ## CLKOutSamp(!=ClkSamp)
        ## Common
            # XVT
            _LOGIC_CLKoutSamp_XVT = 'SLVT',
            # Height
            # _CLKOutSamp_PMOSXvt2NMOSXvt=1800,  # number, = _DFF_PMOSXvt2NMOSXvt
        ## Inverter
            # Nmos
            _LOGIC_CLKoutSamp_Inv_NMOS_NumberofGate=1,  # Number
            _LOGIC_CLKoutSamp_Inv_NMOS_ChannelWidth=100,  # Number
            _LOGIC_CLKoutSamp_Inv_NMOS_ChannelLength=30,  # Number
            # Pmos
            _LOGIC_CLKoutSamp_Inv_PMOS_NumberofGate=1,  # Number
            _LOGIC_CLKoutSamp_Inv_PMOS_ChannelWidth=100,  # Number
            _LOGIC_CLKoutSamp_Inv_PMOS_ChannelLength=30,  # Number
        ## AND
            ## AND Common
            ## Nand
                # NmosA
                _LOGIC_CLKoutSamp_And_Nand_NMOSA_NumberofGate=1,  # Number
                _LOGIC_CLKoutSamp_And_Nand_NMOSA_ChannelWidth=100,  # Number
                _LOGIC_CLKoutSamp_And_Nand_NMOSA_ChannelLength=30,  # Number
                # NMOSB
                _LOGIC_CLKoutSamp_And_Nand_NMOSB_NumberofGate=2,  # Number
                _LOGIC_CLKoutSamp_And_Nand_NMOSB_ChannelWidth=750,  # Number
                _LOGIC_CLKoutSamp_And_Nand_NMOSB_ChannelLength=30,  # Number
                # PMOSA
                _LOGIC_CLKoutSamp_And_Nand_PMOSA_NumberofGate=1,  # Number
                _LOGIC_CLKoutSamp_And_Nand_PMOSA_ChannelWidth=300,  # Number
                _LOGIC_CLKoutSamp_And_Nand_PMOSA_ChannelLength=30,  # Number
                # PMOSB
                _LOGIC_CLKoutSamp_And_Nand_PMOSB_NumberofGate=3,  # Number
                _LOGIC_CLKoutSamp_And_Nand_PMOSB_ChannelWidth=750,  # Number
                _LOGIC_CLKoutSamp_And_Nand_PMOSB_ChannelLength=30,  # Number
            ## Inverter
                # Nmos
                _LOGIC_CLKoutSamp_And_Inv_NMOS_NumberofGate=1,  # Number
                _LOGIC_CLKoutSamp_And_Inv_NMOS_ChannelWidth=100,  # Number
                _LOGIC_CLKoutSamp_And_Inv_NMOS_ChannelLength=30,  # Number
                # Pmos
                _LOGIC_CLKoutSamp_And_Inv_PMOS_NumberofGate=1,  # Number
                _LOGIC_CLKoutSamp_And_Inv_PMOS_ChannelWidth=200,  # Number
                _LOGIC_CLKoutSamp_And_Inv_PMOS_ChannelLength=30,  # Number


## Comparator
    ## StrongARM Latch
        # Common
        _COMP_SALatch_ChannelLength=30,  # random.randrange(30, 60, 2),  # 30
        _COMP_SALatch_XVT='HVT',

        # PMOS
        _COMP_SALatch_CLKinputPMOSFinger1=1,  #PMOS Reset Sw1 # random.randint(1, 15),  # 6
        _COMP_SALatch_CLKinputPMOSFinger2=1,  #PMOS Reset Sw2 # random.randint(1, 15),  # 3
        _COMP_SALatch_PMOSFinger=1,  		  #PMOS Latch	  # random.randint(1, 15),  # 3
        _COMP_SALatch_PMOSChannelWidth=1000,  #All PMOS width # random.randrange(200, 1050, 2),  # 500

        # NMOS
        _COMP_SALatch_DATAinputNMOSFinger=3,  #NMOS Input Tr # random.randint(3, 15),  # 12
        _COMP_SALatch_NMOSFinger=2,  		  #NMOS at Latch # random.randint(1, 15),  # 2
        _COMP_SALatch_CLKinputNMOSFinger=1,  #NMOS Tail # random.randint(1, 15),  # 8
        _COMP_SALatch_NMOSChannelWidth=330,  #Nmos width # random.randrange(200, 1050, 2),  # 500
        _COMP_SALatch_CLKinputNMOSChannelWidth=200,  # random.randrange(200, 1050, 2),  # 800

    ## StrongArmOutBuffer and SRLatch
        ## Common
            # XVT
            _COMP_SAOutBufAndSRLatch_XVT='SLVT',
            # Body
            _COMP_SAOutBufAndSRLatch_NMOS_Pbody_XvtTop2Pbody=None,  # Number/None(Minimum)
            _COMP_SAOutBufAndSRLatch_PMOS_Nbody_Xvtdown2Nbody=None,  # Number/None(Minimum)
            # Height
            _COMP_SAOutBufAndSRLatch_PMOSXvt2NMOSXvt=1800,  # number
        ## StronArm Output Buffer
            ## Inverter1(pre)
                    #Nmos
                _COMP_SAOutBuf_Buf_Inv1_NMOS_NumberofGate          = 1,        # Number
                _COMP_SAOutBuf_Buf_Inv1_NMOS_ChannelWidth          = 400,      # Number
                _COMP_SAOutBuf_Buf_Inv1_NMOS_ChannelLength         = 30,       # Number
                    #Pmos
                _COMP_SAOutBuf_Buf_Inv1_PMOS_NumberofGate          = 1,        # Number
                _COMP_SAOutBuf_Buf_Inv1_PMOS_ChannelWidth          = 800,      # Number
                _COMP_SAOutBuf_Buf_Inv1_PMOS_ChannelLength         = 30,       # Number
            ## Inverter2
                    #Nmos
                _COMP_SAOutBuf_Buf_Inv2_NMOS_NumberofGate          = 2,        # Number
                _COMP_SAOutBuf_Buf_Inv2_NMOS_ChannelWidth          = 400,      # Number
                _COMP_SAOutBuf_Buf_Inv2_NMOS_ChannelLength         = 30,       # Number
                    #Pmos
                _COMP_SAOutBuf_Buf_Inv2_PMOS_NumberofGate          = 2,        # Number
                _COMP_SAOutBuf_Buf_Inv2_PMOS_ChannelWidth          = 800,      # Number
                _COMP_SAOutBuf_Buf_Inv2_PMOS_ChannelLength         = 30,       # Number
        ## SRLatch
            ## Nand(Set,Rst same)
                # NmosA
                _COMP_SRLatch_Nand_NMOSA_NumberofGate=1,  # Number
                _COMP_SRLatch_Nand_NMOSA_ChannelWidth=100,  # Number
                _COMP_SRLatch_Nand_NMOSA_ChannelLength=30,  # Number
                # NMOSB
                _COMP_SRLatch_Nand_NMOSB_NumberofGate=2,  # Number
                _COMP_SRLatch_Nand_NMOSB_ChannelWidth=750,  # Number
                _COMP_SRLatch_Nand_NMOSB_ChannelLength=30,  # Number
                # PMOSA
                _COMP_SRLatch_Nand_PMOSA_NumberofGate=2,  # Number
                _COMP_SRLatch_Nand_PMOSA_ChannelWidth=100,  # Number
                _COMP_SRLatch_Nand_PMOSA_ChannelLength=30,  # Number
                # PMOSB
                _COMP_SRLatch_Nand_PMOSB_NumberofGate=1,  # Number
                _COMP_SRLatch_Nand_PMOSB_ChannelWidth=750,  # Number
                _COMP_SRLatch_Nand_PMOSB_ChannelLength=30,  # Number

    ## Comp clock Gen Logic: Clk_Samp Inv, Clk_Source Inv, AND Gate, CompClockBuff
        ## Common
            # XVT
            _COMP_CompClkLogic_XVT='SLVT',
            # Body
            _COMP_CompClkLogic_NMOS_Pbody_XvtTop2Pbody=None,  # Number/None(Minimum)
            _COMP_CompClkLogic_PMOS_Nbody_Xvtdown2Nbody=None,  # Number/None(Minimum)
            # Height
            _COMP_CompClkLogic_PMOSXvt2NMOSXvt=1800,  # number
        ## StronArm Output Buffer
            ## Inverter1(pre)
                    #Nmos
                _COMP_CompClkLogic_Buf_Inv1_NMOS_NumberofGate          = 2,        # Number
                _COMP_CompClkLogic_Buf_Inv1_NMOS_ChannelWidth          = 400,      # Number
                _COMP_CompClkLogic_Buf_Inv1_NMOS_ChannelLength         = 30,       # Number
                    #Pmos
                _COMP_CompClkLogic_Buf_Inv1_PMOS_NumberofGate          = 2,        # Number
                _COMP_CompClkLogic_Buf_Inv1_PMOS_ChannelWidth          = 800,      # Number
                _COMP_CompClkLogic_Buf_Inv1_PMOS_ChannelLength         = 30,       # Number
            ## Inverter2
                    #Nmos
                _COMP_CompClkLogic_Buf_Inv2_NMOS_NumberofGate          = 4,        # Number
                _COMP_CompClkLogic_Buf_Inv2_NMOS_ChannelWidth          = 400,      # Number
                _COMP_CompClkLogic_Buf_Inv2_NMOS_ChannelLength         = 30,       # Number
                    #Pmos
                _COMP_CompClkLogic_Buf_Inv2_PMOS_NumberofGate          = 4,        # Number
                _COMP_CompClkLogic_Buf_Inv2_PMOS_ChannelWidth          = 800,      # Number
                _COMP_CompClkLogic_Buf_Inv2_PMOS_ChannelLength         = 30,       # Number
        ## AND
            ## Nand
                # NmosA
                _COMP_CompClkLogic_Nand_NMOSA_NumberofGate=1,  # Number
                _COMP_CompClkLogic_Nand_NMOSA_ChannelWidth=100,  # Number
                _COMP_CompClkLogic_Nand_NMOSA_ChannelLength=30,  # Number
                # NMOSB
                _COMP_CompClkLogic_Nand_NMOSB_NumberofGate=2,  # Number
                _COMP_CompClkLogic_Nand_NMOSB_ChannelWidth=750,  # Number
                _COMP_CompClkLogic_Nand_NMOSB_ChannelLength=30,  # Number
                # PMOSA
                _COMP_CompClkLogic_Nand_PMOSA_NumberofGate=1,  # Number
                _COMP_CompClkLogic_Nand_PMOSA_ChannelWidth=300,  # Number
                _COMP_CompClkLogic_Nand_PMOSA_ChannelLength=30,  # Number
                # PMOSB
                _COMP_CompClkLogic_Nand_PMOSB_NumberofGate=3,  # Number
                _COMP_CompClkLogic_Nand_PMOSB_ChannelWidth=750,  # Number
                _COMP_CompClkLogic_Nand_PMOSB_ChannelLength=30,  # Number
            ## Inverter
                # Nmos
                _COMP_CompClkLogic_Inv_NMOS_NumberofGate=1,  # Number
                _COMP_CompClkLogic_Inv_NMOS_ChannelWidth=100,  # Number
                _COMP_CompClkLogic_Inv_NMOS_ChannelLength=30,  # Number
                # Pmos
                _COMP_CompClkLogic_Inv_PMOS_NumberofGate=1,  # Number
                _COMP_CompClkLogic_Inv_PMOS_ChannelWidth=200,  # Number
                _COMP_CompClkLogic_Inv_PMOS_ChannelLength=30,  # Number

        ## Clk_Source Inv
                #Nmos
            _COMP_CompClkLogic_ClkSrc_NMOS_NumberofGate          = 1,        # Number
            _COMP_CompClkLogic_ClkSrc_NMOS_ChannelWidth          = 400,      # Number
            _COMP_CompClkLogic_ClkSrc_NMOS_ChannelLength         = 30,       # Number
                #Pmos
            _COMP_CompClkLogic_ClkSrc_PMOS_NumberofGate          = 1,        # Number
            _COMP_CompClkLogic_ClkSrc_PMOS_ChannelWidth          = 800,      # Number
            _COMP_CompClkLogic_ClkSrc_PMOS_ChannelLength         = 30,       # Number
        ## Clk_Samp Inv
                #Nmos
            _COMP_CompClkLogic_ClkSmp_NMOS_NumberofGate          = 1,        # Number
            _COMP_CompClkLogic_ClkSmp_NMOS_ChannelWidth          = 400,      # Number
            _COMP_CompClkLogic_ClkSmp_NMOS_ChannelLength         = 30,       # Number
                #Pmos
            _COMP_CompClkLogic_ClkSmp_PMOS_NumberofGate          = 1,        # Number
            _COMP_CompClkLogic_ClkSmp_PMOS_ChannelWidth          = 800,      # Number
            _COMP_CompClkLogic_ClkSmp_PMOS_ChannelLength         = 30,       # Number

## CLOCK AND DATA BUF : Comparator Dout Buf for driving Logic, CLKSamp and CLKScr Buff for Driving Sampler and Comparator
    ## Top placed
        ## CLK Samp
            ## InvChain Common
                ## Height
        _BUF_CLKSamp_PMOSXvt2NMOSXvt = 500,  # number
            ## Inverter Chain
                ## Inv1 common
        _BUF_CLKSamp_XVT='SLVT',
        _BUF_CLKSamp_NumberofGate = [1,2,4,8],  # Vector,
        _BUF_CLKSamp_ChanneLength = 30,
                ## NMOS
        _BUF_CLKSamp_NMOSChannelWidth = 784,
                ## PMOS
        _BUF_CLKSamp_PMOSChannelWidth = 833,
        ## CLK Scr
            ## InvChain Common
                ## Height
        _BUF_CLKScr_PMOSXvt2NMOSXvt = 500,  # number
            ## Inverter Chain
                ## Inv1 common
        _BUF_CLKScr_XVT='SLVT',
        _BUF_CLKScr_NumberofGate = [1,2,4,8],  # Vector,
        _BUF_CLKScr_ChanneLength = 30,
                ## NMOS
        _BUF_CLKScr_NMOSChannelWidth = 784,
                ## PMOS
        _BUF_CLKScr_PMOSChannelWidth = 833,
    ## Bottom Placed
        ## CompOut
            ## InvChain Common
                ## Height
        _BUF_CompOut_PMOSXvt2NMOSXvt = 500,  # number
            ## Inverter Chain
                ## Inv1 common
        _BUF_CompOut_XVT='SLVT',
        _BUF_CompOut_NumberofGate = [1,2,4,8],  # Vector,
        _BUF_CompOut_ChanneLength = 30,
                ## NMOS
        _BUF_CompOut_NMOSChannelWidth = 784,
                ## PMOS
        _BUF_CompOut_PMOSChannelWidth = 833,




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

    ''' Check Time'''
    elapsed_time = time.time() - start_time
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
    # Checker.lib_deletion()
    Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()


    print('#############################      Finished      ################################')
    print('{} Hours   {} minutes   {} seconds'.format(h, m, s))
# end of 'main():' ---------------------------------------------------------------------------------------------
