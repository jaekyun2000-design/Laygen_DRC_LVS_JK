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

from KJH91_Projects.Project_ADC.Layoutgen_code.F00_CLKBufferTree_Fixed import F00_02_CLKBufferTree_v3
from KJH91_Projects.Project_ADC.Layoutgen_code.K00_SARLogicWtBuffers_YJH import K00_00_SARLogic_KJH1_v2
from KJH91_Projects.Project_ADC.Layoutgen_code.K00_SARLogicWtBuffers_RCHybrid_Fixed               import K00_01_SARLogicWtCLKBufTree
from KJH91_Projects.Project_ADC.Layoutgen_code.J00_CDACPreDriver_InvBuffer_KJH0_RCHybrid_Fixed    import J00_02_CDAC_PreDriver_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.D00_SARLogic_Inverter_Fixed       import D00_00_Inverter_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.D03_SARLogic_And_Fixed        import D03_03_And_KJH0


## Define Class
class _SARLogicWtCDACPreDriver(StickDiagram_KJH1._StickDiagram_KJH):
    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
_NumofBit = 12,

## SAR Logic
    ## Clock Tree (Driving SAR Logic)
        ## Clock Tree Updward (CLK Source Tree, CLK Samp Tree)
            ## CLK Buffer Unit
                ## Common
                _CLKBufTreeTop_UnitBuf_XVT='SLVT',
                ## Nmos
                _CLKBufTreeTop_UnitBuf_NMOS_NumberofGate=1,  # Number
                _CLKBufTreeTop_UnitBuf_NMOS_ChannelWidth=400,  # Number
                _CLKBufTreeTop_UnitBuf_NMOS_ChannelLength=30,  # Number
                ## Pmos
                _CLKBufTreeTop_UnitBuf_PMOS_NumberofGate=1,  # Number
                _CLKBufTreeTop_UnitBuf_PMOS_ChannelWidth=800,  # Number
                _CLKBufTreeTop_UnitBuf_PMOS_ChannelLength=30,  # Number
                # Height
                _CLKBufTreeTop_UnitBuf_PMOSXvt2NMOSXvt=446,  # number
            ## Clock Buffer Tree structure
            _CLKBufTreeTop_BufTree1and2_NumOfStage=4,  # len[Buf0, Buf1, ... ] 스테이지 수 (아래 버퍼 사이즈 리스트의 길이와 같아야 함.)
            _CLKBufTreeTop_BufTree1_SizeofEachStage=[1, 2, 4, 8],  # CLKSampBuf: [Buf0, Buf1, Buf2 ...]
            _CLKBufTreeTop_BufTree2_SizeofEachStage=[1, 2, 4, 8],  # CLKSrcBuf: [Buf0, Buf1, Buf2 ...]
            _CLKBufTreeTop_XOffSet=0,
        ## Clock Tree Dnward (CLK Source Tree, CLK Samp Tree)
            ## CLK Buffer Unit
                ## Common
                _CLKBufTreeBot_UnitBuf_XVT='SLVT',
                ## Nmos
                _CLKBufTreeBot_UnitBuf_NMOS_NumberofGate=1,  # Number
                _CLKBufTreeBot_UnitBuf_NMOS_ChannelWidth=400,  # Number
                _CLKBufTreeBot_UnitBuf_NMOS_ChannelLength=30,  # Number
                ## Pmos
                _CLKBufTreeBot_UnitBuf_PMOS_NumberofGate=1,  # Number
                _CLKBufTreeBot_UnitBuf_PMOS_ChannelWidth=800,  # Number
                _CLKBufTreeBot_UnitBuf_PMOS_ChannelLength=30,  # Number
                # Height
                _CLKBufTreeBot_UnitBuf_PMOSXvt2NMOSXvt=446,  # number
            ## Clock Buffer Tree structure
            _CLKBufTreeBot_BufTree1and2_NumOfStage=4,  # len[Buf0, Buf1, ... ] 스테이지 수 (아래 버퍼 사이즈 리스트의 길이와 같아야 함.)
            _CLKBufTreeBot_BufTree1_SizeofEachStage=[1, 2, 4, 8],  # CompOutBuf: [Buf0, Buf1, Buf2 ...]
            _CLKBufTreeBot_BufTree2_SizeofEachStage=[1, 2, 4, 8],  # CLKDoutBuf: [Buf0, Buf1, Buf2 ...]
            _CLKBufTreeBot_XOffSet=0,

    ## Clock Spine (Physical demension)
        ## CLK Source: upward, 1st floor
        _YWidthOfCLKSrc=100,
        ## CLK Samp: upward, 2nd floor
        _SpaceBtwCLKSrcAndCLKSamp=100,
        _YWidthOfCLKSamp=100,
        ## Comparator Output: downward, Basement1
        _YWidthOfCompOut=100,
        ## CLK Dout: downward, basement2
        _SpaceBtwCompOutAndCLKDout=100,
        _YWidthOfCLKDout=100,

    ## SetResetDFF
        ## DFF Common
        _Test_distance=320,
        _DFF_PMOSXvt2NMOSXvt    = 1150, # number

        ## Master Xgate1
            ## Xgate common
            _Mst_Xgate1_XVT='SLVT',
            ## Xgate NMOS
            _Mst_Xgate1_NMOS_NumberofGate=1,
            _Mst_Xgate1_NMOS_ChannelWidth=300,
            _Mst_Xgate1_NMOS_ChannelLength=30,
            ## Xgate PMOS
            _Mst_Xgate1_PMOS_NumberofGate=3,
            _Mst_Xgate1_PMOS_ChannelWidth=500,
            _Mst_Xgate1_PMOS_ChannelLength=30,

        ## Master Xgate2
            ## Xgate common
            _Mst_Xgate2_XVT='SLVT',
            ## Xgate NMOS
            _Mst_Xgate2_NMOS_NumberofGate           = 2,
            _Mst_Xgate2_NMOS_ChannelWidth           = 800,
            _Mst_Xgate2_NMOS_ChannelLength          = 30,
            ## Xgate PMOS
            _Mst_Xgate2_PMOS_NumberofGate           = 3,
            _Mst_Xgate2_PMOS_ChannelWidth           = 200,
            _Mst_Xgate2_PMOS_ChannelLength          = 30,

        ## Master Nor1
            ## Nor1 common
            _Mst_Nor1_XVT='SLVT',
            ## NMOS
                ## NMOSA
                _Mst_Nor1_NMOSA_NumberofGate           = 2,
                _Mst_Nor1_NMOSA_ChannelWidth           = 800,
                _Mst_Nor1_NMOSA_ChannelLength          = 30,
                ## NMOSB
                _Mst_Nor1_NMOSB_NumberofGate           = 3,
                _Mst_Nor1_NMOSB_ChannelWidth           = 200,
                _Mst_Nor1_NMOSB_ChannelLength          = 30,
            ## PMOS
                ## PMOSA
                _Mst_Nor1_PMOSA_NumberofGate            = 2,
                _Mst_Nor1_PMOSA_ChannelWidth            = 800,
                _Mst_Nor1_PMOSA_ChannelLength           = 30,
                ## PMOSB
                _Mst_Nor1_PMOSB_NumberofGate            = 3,
                _Mst_Nor1_PMOSB_ChannelWidth            = 200,
                _Mst_Nor1_PMOSB_ChannelLength           = 30,

        ## Master Nor2
            ## Nor2 common
            _Mst_Nor2_XVT='SLVT',
            ## NMOS
                ## NMOSA
                _Mst_Nor2_NMOSA_NumberofGate           = 2,
                _Mst_Nor2_NMOSA_ChannelWidth           = 800,
                _Mst_Nor2_NMOSA_ChannelLength          = 30,
                ## NMOSB
                _Mst_Nor2_NMOSB_NumberofGate           = 3,
                _Mst_Nor2_NMOSB_ChannelWidth           = 200,
                _Mst_Nor2_NMOSB_ChannelLength          = 30,
            ## PMOS
                ## PMOSA
                _Mst_Nor2_PMOSA_NumberofGate            = 2,
                _Mst_Nor2_PMOSA_ChannelWidth            = 800,
                _Mst_Nor2_PMOSA_ChannelLength           = 30,
                ## PMOSB
                _Mst_Nor2_PMOSB_NumberofGate            = 3,
                _Mst_Nor2_PMOSB_ChannelWidth            = 200,
                _Mst_Nor2_PMOSB_ChannelLength           = 30,

        ## Master Inv1 : Set pre-driver
            ## Inv1 common
            _Mst_Inv1_XVT='SLVT',
            ## Inv1 NMOS
            _Mst_Inv1_NMOS_NumberofGate           = 1,
            _Mst_Inv1_NMOS_ChannelWidth           = 300,
            _Mst_Inv1_NMOS_ChannelLength          = 30,
            ## Inv1 PMOS
            _Mst_Inv1_PMOS_NumberofGate           = 3,
            _Mst_Inv1_PMOS_ChannelWidth           = 500,
            _Mst_Inv1_PMOS_ChannelLength          = 30,

        ## Master Inv2 : Set driver
            ## Inv2 common
            _Mst_Inv2_XVT='SLVT',
            ## Inv2 NMOS
            _Mst_Inv2_NMOS_NumberofGate           = 1,
            _Mst_Inv2_NMOS_ChannelWidth           = 300,
            _Mst_Inv2_NMOS_ChannelLength          = 30,
            ## Inv2 PMOS
            _Mst_Inv2_PMOS_NumberofGate           = 3,
            _Mst_Inv2_PMOS_ChannelWidth           = 500,
            _Mst_Inv2_PMOS_ChannelLength          = 30,

        ## Master Inv3 : Clock driver
            ## Inv3 common
            _Mst_Inv3_XVT='SLVT',
            ## Inv3 NMOS
            _Mst_Inv3_NMOS_NumberofGate           = 1,
            _Mst_Inv3_NMOS_ChannelWidth           = 300,
            _Mst_Inv3_NMOS_ChannelLength          = 30,
            ## Inv3 PMOS
            _Mst_Inv3_PMOS_NumberofGate           = 3,
            _Mst_Inv3_PMOS_ChannelWidth           = 500,
            _Mst_Inv3_PMOS_ChannelLength          = 30,

        ## Slave Xgate1
            ## Xgate common
            _Slv_Xgate1_XVT='SLVT',
            ## Xgate NMOS
            _Slv_Xgate1_NMOS_NumberofGate           = 1,
            _Slv_Xgate1_NMOS_ChannelWidth           = 300,
            _Slv_Xgate1_NMOS_ChannelLength          = 30,
            ## Xgate PMOS
            _Slv_Xgate1_PMOS_NumberofGate           = 3,
            _Slv_Xgate1_PMOS_ChannelWidth           = 500,
            _Slv_Xgate1_PMOS_ChannelLength          = 30,

        ## Slave Xgate2
            ## Xgate common
            _Slv_Xgate2_XVT='SLVT',
            ## Xgate NMOS
            _Slv_Xgate2_NMOS_NumberofGate           = 2,
            _Slv_Xgate2_NMOS_ChannelWidth           = 800,
            _Slv_Xgate2_NMOS_ChannelLength          = 30,
            ## Xgate PMOS
            _Slv_Xgate2_PMOS_NumberofGate           = 3,
            _Slv_Xgate2_PMOS_ChannelWidth           = 200,
            _Slv_Xgate2_PMOS_ChannelLength          = 30,

        ## Slave Nor1
            ## Nor1 common
            _Slv_Nor1_XVT='SLVT',
            ## NMOS
                ## NMOSA
                _Slv_Nor1_NMOSA_NumberofGate           = 2,
                _Slv_Nor1_NMOSA_ChannelWidth           = 800,
                _Slv_Nor1_NMOSA_ChannelLength          = 30,
                ## NMOSB
                _Slv_Nor1_NMOSB_NumberofGate           = 3,
                _Slv_Nor1_NMOSB_ChannelWidth           = 200,
                _Slv_Nor1_NMOSB_ChannelLength          = 30,
            ## PMOS
                ## PMOSA
                _Slv_Nor1_PMOSA_NumberofGate            = 2,
                _Slv_Nor1_PMOSA_ChannelWidth            = 800,
                _Slv_Nor1_PMOSA_ChannelLength           = 30,
                ## PMOSB
                _Slv_Nor1_PMOSB_NumberofGate            = 3,
                _Slv_Nor1_PMOSB_ChannelWidth            = 200,
                _Slv_Nor1_PMOSB_ChannelLength           = 30,

        ## Slave Nor2
            ## Nor2 common
            _Slv_Nor2_XVT='SLVT',
            ## NMOS
                ## NMOSA
                _Slv_Nor2_NMOSA_NumberofGate           = 2,
                _Slv_Nor2_NMOSA_ChannelWidth           = 800,
                _Slv_Nor2_NMOSA_ChannelLength          = 30,
                ## NMOSB
                _Slv_Nor2_NMOSB_NumberofGate           = 3,
                _Slv_Nor2_NMOSB_ChannelWidth           = 200,
                _Slv_Nor2_NMOSB_ChannelLength          = 30,
            ## PMOS
                ## PMOSA
                _Slv_Nor2_PMOSA_NumberofGate            = 2,
                _Slv_Nor2_PMOSA_ChannelWidth            = 800,
                _Slv_Nor2_PMOSA_ChannelLength           = 30,
                ## PMOSB
                _Slv_Nor2_PMOSB_NumberofGate            = 3,
                _Slv_Nor2_PMOSB_ChannelWidth            = 200,
                _Slv_Nor2_PMOSB_ChannelLength           = 30,

        ## Slave Inv1 : ReSet pre-driver
            ## Inv1 common
            _Slv_Inv1_XVT='SLVT',
            ## Inv1 NMOS
            _Slv_Inv1_NMOS_NumberofGate           = 1,
            _Slv_Inv1_NMOS_ChannelWidth           = 300,
            _Slv_Inv1_NMOS_ChannelLength          = 30,
            ## Inv1 PMOS
            _Slv_Inv1_PMOS_NumberofGate           = 3,
            _Slv_Inv1_PMOS_ChannelWidth           = 500,
            _Slv_Inv1_PMOS_ChannelLength          = 30,

        ## Slave Inv2 : ReSet driver
            ## Inv2 common
            _Slv_Inv2_XVT='SLVT',
            ## Inv2 NMOS
            _Slv_Inv2_NMOS_NumberofGate           = 1,
            _Slv_Inv2_NMOS_ChannelWidth           = 300,
            _Slv_Inv2_NMOS_ChannelLength          = 30,
            ## Inv2 PMOS
            _Slv_Inv2_PMOS_NumberofGate           = 3,
            _Slv_Inv2_PMOS_ChannelWidth           = 500,
            _Slv_Inv2_PMOS_ChannelLength          = 30,

        ## Slave Inv3 : Qb driver
            ## Inv3 common
            _Slv_Inv3_XVT='SLVT',
            ## Inv3 NMOS
            _Slv_Inv3_NMOS_NumberofGate           = 1,
            _Slv_Inv3_NMOS_ChannelWidth           = 300,
            _Slv_Inv3_NMOS_ChannelLength          = 30,
            ## Inv3 PMOS
            _Slv_Inv3_PMOS_NumberofGate           = 3,
            _Slv_Inv3_PMOS_ChannelWidth           = 500,
            _Slv_Inv3_PMOS_ChannelLength          = 30,
## DAC PreDriver
    ## Inverter Chain
        ## InvChain Common
        _DACPreDrv_PMOSXvt2NMOSXvt=500,  # number
        ## Inverter Chain
            ## Inv1 common
        _DACPreDrv_NumberofGate=[[1, 2, 4, 8], [1, 2, 4, 8], [1, 2, 4, 8], [2, 2, 2, 2, 2]],  # Vector
        _DACPreDrv_ChannelLength=30,  # Scalar
        _DACPreDrv_XVT='SLVT',  # 'SLVT'
            ## Inv1 NMOS
        _DACPreDrv_Inv_NMOS_ChannelWidth=400,  # Scalar
            ## Inv1 PMOS
        _DACPreDrv_Inv_PMOS_ChannelWidth=800,  # Scalar
## CLKOutSamp(!=ClkSamp)
    ## Common
        # XVT
        _CLKoutSamp_XVT = 'SLVT',
        # Height
        # _CLKOutSamp_PMOSXvt2NMOSXvt=1800,  # number, = _DFF_PMOSXvt2NMOSXvt
    ## Inverter
        # Nmos
        _CLKoutSamp_Inv_NMOS_NumberofGate=1,  # Number
        _CLKoutSamp_Inv_NMOS_ChannelWidth=100,  # Number
        _CLKoutSamp_Inv_NMOS_ChannelLength=30,  # Number
        # Pmos
        _CLKoutSamp_Inv_PMOS_NumberofGate=1,  # Number
        _CLKoutSamp_Inv_PMOS_ChannelWidth=100,  # Number
        _CLKoutSamp_Inv_PMOS_ChannelLength=30,  # Number
    ## AND
        ## AND Common
        ## Nand
            # NmosA
            _CLKoutSamp_And_Nand_NMOSA_NumberofGate=1,  # Number
            _CLKoutSamp_And_Nand_NMOSA_ChannelWidth=100,  # Number
            _CLKoutSamp_And_Nand_NMOSA_ChannelLength=30,  # Number
            # NMOSB
            _CLKoutSamp_And_Nand_NMOSB_NumberofGate=2,  # Number
            _CLKoutSamp_And_Nand_NMOSB_ChannelWidth=750,  # Number
            _CLKoutSamp_And_Nand_NMOSB_ChannelLength=30,  # Number
            # PMOSA
            _CLKoutSamp_And_Nand_PMOSA_NumberofGate=1,  # Number
            _CLKoutSamp_And_Nand_PMOSA_ChannelWidth=300,  # Number
            _CLKoutSamp_And_Nand_PMOSA_ChannelLength=30,  # Number
            # PMOSB
            _CLKoutSamp_And_Nand_PMOSB_NumberofGate=3,  # Number
            _CLKoutSamp_And_Nand_PMOSB_ChannelWidth=750,  # Number
            _CLKoutSamp_And_Nand_PMOSB_ChannelLength=30,  # Number
        ## Inverter
            # Nmos
            _CLKoutSamp_And_Inv_NMOS_NumberofGate=1,  # Number
            _CLKoutSamp_And_Inv_NMOS_ChannelWidth=100,  # Number
            _CLKoutSamp_And_Inv_NMOS_ChannelLength=30,  # Number
            # Pmos
            _CLKoutSamp_And_Inv_PMOS_NumberofGate=1,  # Number
            _CLKoutSamp_And_Inv_PMOS_ChannelWidth=200,  # Number
            _CLKoutSamp_And_Inv_PMOS_ChannelLength=30,  # Number


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
                _CLKBufTreeTop_UnitBuf_XVT='SLVT',
                ## Nmos
                _CLKBufTreeTop_UnitBuf_NMOS_NumberofGate=1,  # Number
                _CLKBufTreeTop_UnitBuf_NMOS_ChannelWidth=400,  # Number
                _CLKBufTreeTop_UnitBuf_NMOS_ChannelLength=30,  # Number
                ## Pmos
                _CLKBufTreeTop_UnitBuf_PMOS_NumberofGate=1,  # Number
                _CLKBufTreeTop_UnitBuf_PMOS_ChannelWidth=800,  # Number
                _CLKBufTreeTop_UnitBuf_PMOS_ChannelLength=30,  # Number
                # Height
                _CLKBufTreeTop_UnitBuf_PMOSXvt2NMOSXvt=446,  # number
            ## Clock Buffer Tree structure
            _CLKBufTreeTop_BufTree1and2_NumOfStage=4,  # len[Buf0, Buf1, ... ] 스테이지 수 (아래 버퍼 사이즈 리스트의 길이와 같아야 함.)
            _CLKBufTreeTop_BufTree1_SizeofEachStage=[1, 2, 4, 8],  # CLKSampBuf: [Buf0, Buf1, Buf2 ...]
            _CLKBufTreeTop_BufTree2_SizeofEachStage=[1, 2, 4, 8],  # CLKSrcBuf: [Buf0, Buf1, Buf2 ...]
            _CLKBufTreeTop_XOffSet=0,
        ## Clock Tree Dnward (CLK Source Tree, CLK Samp Tree)
            ## CLK Buffer Unit
                ## Common
                _CLKBufTreeBot_UnitBuf_XVT='SLVT',
                ## Nmos
                _CLKBufTreeBot_UnitBuf_NMOS_NumberofGate=1,  # Number
                _CLKBufTreeBot_UnitBuf_NMOS_ChannelWidth=400,  # Number
                _CLKBufTreeBot_UnitBuf_NMOS_ChannelLength=30,  # Number
                ## Pmos
                _CLKBufTreeBot_UnitBuf_PMOS_NumberofGate=1,  # Number
                _CLKBufTreeBot_UnitBuf_PMOS_ChannelWidth=800,  # Number
                _CLKBufTreeBot_UnitBuf_PMOS_ChannelLength=30,  # Number
                # Height
                _CLKBufTreeBot_UnitBuf_PMOSXvt2NMOSXvt=446,  # number
            ## Clock Buffer Tree structure
            _CLKBufTreeBot_BufTree1and2_NumOfStage=4,  # len[Buf0, Buf1, ... ] 스테이지 수 (아래 버퍼 사이즈 리스트의 길이와 같아야 함.)
            _CLKBufTreeBot_BufTree1_SizeofEachStage=[1, 2, 4, 8],  # CompOutBuf: [Buf0, Buf1, Buf2 ...]
            _CLKBufTreeBot_BufTree2_SizeofEachStage=[1, 2, 4, 8],  # CLKDoutBuf: [Buf0, Buf1, Buf2 ...]
            _CLKBufTreeBot_XOffSet=0,

    ## Clock Spine (Physical demension)
        ## CLK Source: upward, 1st floor
        _YWidthOfCLKSrc=100,
        ## CLK Samp: upward, 2nd floor
        _SpaceBtwCLKSrcAndCLKSamp=100,
        _YWidthOfCLKSamp=100,
        ## Comparator Output: downward, Basement1
        _YWidthOfCompOut=100,
        ## CLK Dout: downward, basement2
        _SpaceBtwCompOutAndCLKDout=100,
        _YWidthOfCLKDout=100,

    ## SetResetDFF
        ## DFF Common
        _Test_distance=320,
        _DFF_PMOSXvt2NMOSXvt    = 1150, # number

        ## Master Xgate1
            ## Xgate common
            _Mst_Xgate1_XVT='SLVT',
            ## Xgate NMOS
            _Mst_Xgate1_NMOS_NumberofGate=1,
            _Mst_Xgate1_NMOS_ChannelWidth=300,
            _Mst_Xgate1_NMOS_ChannelLength=30,
            ## Xgate PMOS
            _Mst_Xgate1_PMOS_NumberofGate=3,
            _Mst_Xgate1_PMOS_ChannelWidth=500,
            _Mst_Xgate1_PMOS_ChannelLength=30,

        ## Master Xgate2
            ## Xgate common
            _Mst_Xgate2_XVT='SLVT',
            ## Xgate NMOS
            _Mst_Xgate2_NMOS_NumberofGate           = 2,
            _Mst_Xgate2_NMOS_ChannelWidth           = 800,
            _Mst_Xgate2_NMOS_ChannelLength          = 30,
            ## Xgate PMOS
            _Mst_Xgate2_PMOS_NumberofGate           = 3,
            _Mst_Xgate2_PMOS_ChannelWidth           = 200,
            _Mst_Xgate2_PMOS_ChannelLength          = 30,

        ## Master Nor1
            ## Nor1 common
            _Mst_Nor1_XVT='SLVT',
            ## NMOS
                ## NMOSA
                _Mst_Nor1_NMOSA_NumberofGate           = 2,
                _Mst_Nor1_NMOSA_ChannelWidth           = 800,
                _Mst_Nor1_NMOSA_ChannelLength          = 30,
                ## NMOSB
                _Mst_Nor1_NMOSB_NumberofGate           = 3,
                _Mst_Nor1_NMOSB_ChannelWidth           = 200,
                _Mst_Nor1_NMOSB_ChannelLength          = 30,
            ## PMOS
                ## PMOSA
                _Mst_Nor1_PMOSA_NumberofGate            = 2,
                _Mst_Nor1_PMOSA_ChannelWidth            = 800,
                _Mst_Nor1_PMOSA_ChannelLength           = 30,
                ## PMOSB
                _Mst_Nor1_PMOSB_NumberofGate            = 3,
                _Mst_Nor1_PMOSB_ChannelWidth            = 200,
                _Mst_Nor1_PMOSB_ChannelLength           = 30,

        ## Master Nor2
            ## Nor2 common
            _Mst_Nor2_XVT='SLVT',
            ## NMOS
                ## NMOSA
                _Mst_Nor2_NMOSA_NumberofGate           = 2,
                _Mst_Nor2_NMOSA_ChannelWidth           = 800,
                _Mst_Nor2_NMOSA_ChannelLength          = 30,
                ## NMOSB
                _Mst_Nor2_NMOSB_NumberofGate           = 3,
                _Mst_Nor2_NMOSB_ChannelWidth           = 200,
                _Mst_Nor2_NMOSB_ChannelLength          = 30,
            ## PMOS
                ## PMOSA
                _Mst_Nor2_PMOSA_NumberofGate            = 2,
                _Mst_Nor2_PMOSA_ChannelWidth            = 800,
                _Mst_Nor2_PMOSA_ChannelLength           = 30,
                ## PMOSB
                _Mst_Nor2_PMOSB_NumberofGate            = 3,
                _Mst_Nor2_PMOSB_ChannelWidth            = 200,
                _Mst_Nor2_PMOSB_ChannelLength           = 30,

        ## Master Inv1 : Set pre-driver
            ## Inv1 common
            _Mst_Inv1_XVT='SLVT',
            ## Inv1 NMOS
            _Mst_Inv1_NMOS_NumberofGate           = 1,
            _Mst_Inv1_NMOS_ChannelWidth           = 300,
            _Mst_Inv1_NMOS_ChannelLength          = 30,
            ## Inv1 PMOS
            _Mst_Inv1_PMOS_NumberofGate           = 3,
            _Mst_Inv1_PMOS_ChannelWidth           = 500,
            _Mst_Inv1_PMOS_ChannelLength          = 30,

        ## Master Inv2 : Set driver
            ## Inv2 common
            _Mst_Inv2_XVT='SLVT',
            ## Inv2 NMOS
            _Mst_Inv2_NMOS_NumberofGate           = 1,
            _Mst_Inv2_NMOS_ChannelWidth           = 300,
            _Mst_Inv2_NMOS_ChannelLength          = 30,
            ## Inv2 PMOS
            _Mst_Inv2_PMOS_NumberofGate           = 3,
            _Mst_Inv2_PMOS_ChannelWidth           = 500,
            _Mst_Inv2_PMOS_ChannelLength          = 30,

        ## Master Inv3 : Clock driver
            ## Inv3 common
            _Mst_Inv3_XVT='SLVT',
            ## Inv3 NMOS
            _Mst_Inv3_NMOS_NumberofGate           = 1,
            _Mst_Inv3_NMOS_ChannelWidth           = 300,
            _Mst_Inv3_NMOS_ChannelLength          = 30,
            ## Inv3 PMOS
            _Mst_Inv3_PMOS_NumberofGate           = 3,
            _Mst_Inv3_PMOS_ChannelWidth           = 500,
            _Mst_Inv3_PMOS_ChannelLength          = 30,

        ## Slave Xgate1
            ## Xgate common
            _Slv_Xgate1_XVT='SLVT',
            ## Xgate NMOS
            _Slv_Xgate1_NMOS_NumberofGate           = 1,
            _Slv_Xgate1_NMOS_ChannelWidth           = 300,
            _Slv_Xgate1_NMOS_ChannelLength          = 30,
            ## Xgate PMOS
            _Slv_Xgate1_PMOS_NumberofGate           = 3,
            _Slv_Xgate1_PMOS_ChannelWidth           = 500,
            _Slv_Xgate1_PMOS_ChannelLength          = 30,

        ## Slave Xgate2
            ## Xgate common
            _Slv_Xgate2_XVT='SLVT',
            ## Xgate NMOS
            _Slv_Xgate2_NMOS_NumberofGate           = 2,
            _Slv_Xgate2_NMOS_ChannelWidth           = 800,
            _Slv_Xgate2_NMOS_ChannelLength          = 30,
            ## Xgate PMOS
            _Slv_Xgate2_PMOS_NumberofGate           = 3,
            _Slv_Xgate2_PMOS_ChannelWidth           = 200,
            _Slv_Xgate2_PMOS_ChannelLength          = 30,

        ## Slave Nor1
            ## Nor1 common
            _Slv_Nor1_XVT='SLVT',
            ## NMOS
                ## NMOSA
                _Slv_Nor1_NMOSA_NumberofGate           = 2,
                _Slv_Nor1_NMOSA_ChannelWidth           = 800,
                _Slv_Nor1_NMOSA_ChannelLength          = 30,
                ## NMOSB
                _Slv_Nor1_NMOSB_NumberofGate           = 3,
                _Slv_Nor1_NMOSB_ChannelWidth           = 200,
                _Slv_Nor1_NMOSB_ChannelLength          = 30,
            ## PMOS
                ## PMOSA
                _Slv_Nor1_PMOSA_NumberofGate            = 2,
                _Slv_Nor1_PMOSA_ChannelWidth            = 800,
                _Slv_Nor1_PMOSA_ChannelLength           = 30,
                ## PMOSB
                _Slv_Nor1_PMOSB_NumberofGate            = 3,
                _Slv_Nor1_PMOSB_ChannelWidth            = 200,
                _Slv_Nor1_PMOSB_ChannelLength           = 30,

        ## Slave Nor2
            ## Nor2 common
            _Slv_Nor2_XVT='SLVT',
            ## NMOS
                ## NMOSA
                _Slv_Nor2_NMOSA_NumberofGate           = 2,
                _Slv_Nor2_NMOSA_ChannelWidth           = 800,
                _Slv_Nor2_NMOSA_ChannelLength          = 30,
                ## NMOSB
                _Slv_Nor2_NMOSB_NumberofGate           = 3,
                _Slv_Nor2_NMOSB_ChannelWidth           = 200,
                _Slv_Nor2_NMOSB_ChannelLength          = 30,
            ## PMOS
                ## PMOSA
                _Slv_Nor2_PMOSA_NumberofGate            = 2,
                _Slv_Nor2_PMOSA_ChannelWidth            = 800,
                _Slv_Nor2_PMOSA_ChannelLength           = 30,
                ## PMOSB
                _Slv_Nor2_PMOSB_NumberofGate            = 3,
                _Slv_Nor2_PMOSB_ChannelWidth            = 200,
                _Slv_Nor2_PMOSB_ChannelLength           = 30,

        ## Slave Inv1 : ReSet pre-driver
            ## Inv1 common
            _Slv_Inv1_XVT='SLVT',
            ## Inv1 NMOS
            _Slv_Inv1_NMOS_NumberofGate           = 1,
            _Slv_Inv1_NMOS_ChannelWidth           = 300,
            _Slv_Inv1_NMOS_ChannelLength          = 30,
            ## Inv1 PMOS
            _Slv_Inv1_PMOS_NumberofGate           = 3,
            _Slv_Inv1_PMOS_ChannelWidth           = 500,
            _Slv_Inv1_PMOS_ChannelLength          = 30,

        ## Slave Inv2 : ReSet driver
            ## Inv2 common
            _Slv_Inv2_XVT='SLVT',
            ## Inv2 NMOS
            _Slv_Inv2_NMOS_NumberofGate           = 1,
            _Slv_Inv2_NMOS_ChannelWidth           = 300,
            _Slv_Inv2_NMOS_ChannelLength          = 30,
            ## Inv2 PMOS
            _Slv_Inv2_PMOS_NumberofGate           = 3,
            _Slv_Inv2_PMOS_ChannelWidth           = 500,
            _Slv_Inv2_PMOS_ChannelLength          = 30,

        ## Slave Inv3 : Qb driver
            ## Inv3 common
            _Slv_Inv3_XVT='SLVT',
            ## Inv3 NMOS
            _Slv_Inv3_NMOS_NumberofGate           = 1,
            _Slv_Inv3_NMOS_ChannelWidth           = 300,
            _Slv_Inv3_NMOS_ChannelLength          = 30,
            ## Inv3 PMOS
            _Slv_Inv3_PMOS_NumberofGate           = 3,
            _Slv_Inv3_PMOS_ChannelWidth           = 500,
            _Slv_Inv3_PMOS_ChannelLength          = 30,
## DAC PreDriver
    ## Inverter Chain
        ## InvChain Common
        _DACPreDrv_PMOSXvt2NMOSXvt=500,  # number
        ## Inverter Chain
            ## Inv1 common
        _DACPreDrv_NumberofGate=[[1, 2, 4, 8], [1, 2, 4, 8], [1, 2, 4, 8], [2, 2, 2, 2, 2]],  # Vector
        _DACPreDrv_ChannelLength=30,  # Scalar
        _DACPreDrv_XVT='SLVT',  # 'SLVT'
            ## Inv1 NMOS
        _DACPreDrv_Inv_NMOS_ChannelWidth=400,  # Scalar
            ## Inv1 PMOS
        _DACPreDrv_Inv_PMOS_ChannelWidth=800,  # Scalar

# ## CLKOutSamp(!=ClkSamp)
    ## Common
        # XVT
        _CLKoutSamp_XVT = 'SLVT',
        # Height
        # _CLKOutSamp_PMOSXvt2NMOSXvt=1800,  # number
    ## Inverter
        # Nmos
        _CLKoutSamp_Inv_NMOS_NumberofGate=1,  # Number
        _CLKoutSamp_Inv_NMOS_ChannelWidth=100,  # Number
        _CLKoutSamp_Inv_NMOS_ChannelLength=30,  # Number
        # Pmos
        _CLKoutSamp_Inv_PMOS_NumberofGate=1,  # Number
        _CLKoutSamp_Inv_PMOS_ChannelWidth=100,  # Number
        _CLKoutSamp_Inv_PMOS_ChannelLength=30,  # Number
    ## AND
        ## AND Common
        ## Nand
            # NmosA
            _CLKoutSamp_And_Nand_NMOSA_NumberofGate=1,  # Number
            _CLKoutSamp_And_Nand_NMOSA_ChannelWidth=100,  # Number
            _CLKoutSamp_And_Nand_NMOSA_ChannelLength=30,  # Number
            # NMOSB
            _CLKoutSamp_And_Nand_NMOSB_NumberofGate=2,  # Number
            _CLKoutSamp_And_Nand_NMOSB_ChannelWidth=750,  # Number
            _CLKoutSamp_And_Nand_NMOSB_ChannelLength=30,  # Number
            # PMOSA
            _CLKoutSamp_And_Nand_PMOSA_NumberofGate=1,  # Number
            _CLKoutSamp_And_Nand_PMOSA_ChannelWidth=300,  # Number
            _CLKoutSamp_And_Nand_PMOSA_ChannelLength=30,  # Number
            # PMOSB
            _CLKoutSamp_And_Nand_PMOSB_NumberofGate=3,  # Number
            _CLKoutSamp_And_Nand_PMOSB_ChannelWidth=750,  # Number
            _CLKoutSamp_And_Nand_PMOSB_ChannelLength=30,  # Number
        ## Inverter
            # Nmos
            _CLKoutSamp_And_Inv_NMOS_NumberofGate=1,  # Number
            _CLKoutSamp_And_Inv_NMOS_ChannelWidth=100,  # Number
            _CLKoutSamp_And_Inv_NMOS_ChannelLength=30,  # Number
            # Pmos
            _CLKoutSamp_And_Inv_PMOS_NumberofGate=1,  # Number
            _CLKoutSamp_And_Inv_PMOS_ChannelWidth=200,  # Number
            _CLKoutSamp_And_Inv_PMOS_ChannelLength=30,  # Number



                                  ):

        ## Class_HEADER: Pre Defined Parameter Before Calculation
        ## Load DRC library
        _DRCobj = DRC.DRC()
        ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ## CALCULATION START
        SARLogicWtCDACPreDRiver_start_time = time.time()
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')


        ###########################################################################################################################################################
        ## SRF_SARLogicWtCLKBufTree Generation
        _Caculation_Parameters = copy.deepcopy(K00_01_SARLogicWtCLKBufTree._SARLogicWtCLKBufTree._ParametersForDesignCalculation)
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)

        _Caculation_Parameters['_NumofBit'] = _NumofBit
        ## Clock Tree
            ## Clock Tree Updward (CLK Source Tree, CLK Samp Tree)
                ## CLK Buffer Unit
                    ## Common
        _Caculation_Parameters['_CLKBufTreeTop_UnitBuf_XVT'] = _CLKBufTreeTop_UnitBuf_XVT
                    ## Nmos
        _Caculation_Parameters['_CLKBufTreeTop_UnitBuf_NMOS_NumberofGate'] = _CLKBufTreeTop_UnitBuf_NMOS_NumberofGate
        _Caculation_Parameters['_CLKBufTreeTop_UnitBuf_NMOS_ChannelWidth'] = _CLKBufTreeTop_UnitBuf_NMOS_ChannelWidth
        _Caculation_Parameters['_CLKBufTreeTop_UnitBuf_NMOS_ChannelLength'] = _CLKBufTreeTop_UnitBuf_NMOS_ChannelLength
                    ## Pmos
        _Caculation_Parameters['_CLKBufTreeTop_UnitBuf_PMOS_NumberofGate'] = _CLKBufTreeTop_UnitBuf_PMOS_NumberofGate
        _Caculation_Parameters['_CLKBufTreeTop_UnitBuf_PMOS_ChannelWidth'] = _CLKBufTreeTop_UnitBuf_PMOS_ChannelWidth
        _Caculation_Parameters['_CLKBufTreeTop_UnitBuf_PMOS_ChannelLength'] = _CLKBufTreeTop_UnitBuf_PMOS_ChannelLength
                    # Height
        _Caculation_Parameters['_CLKBufTreeTop_UnitBuf_PMOSXvt2NMOSXvt'] = _CLKBufTreeTop_UnitBuf_PMOSXvt2NMOSXvt
                ## Clock Buffer Tree structure
        _Caculation_Parameters['_CLKBufTreeTop_BufTree1and2_NumOfStage'] = _CLKBufTreeTop_BufTree1and2_NumOfStage
        _Caculation_Parameters['_CLKBufTreeTop_BufTree1_SizeofEachStage'] = _CLKBufTreeTop_BufTree1_SizeofEachStage
        _Caculation_Parameters['_CLKBufTreeTop_BufTree2_SizeofEachStage'] = _CLKBufTreeTop_BufTree2_SizeofEachStage
        _Caculation_Parameters['_CLKBufTreeTop_XOffSet'] = _CLKBufTreeTop_XOffSet
            ## Clock Tree Dnward (CLK Source Tree, CLK Samp Tree)
                ## CLK Buffer Unit
                    ## Common
        _Caculation_Parameters['_CLKBufTreeBot_UnitBuf_XVT'] = _CLKBufTreeBot_UnitBuf_XVT
                    ## Nmos
        _Caculation_Parameters['_CLKBufTreeBot_UnitBuf_NMOS_NumberofGate'] = _CLKBufTreeBot_UnitBuf_NMOS_NumberofGate
        _Caculation_Parameters['_CLKBufTreeBot_UnitBuf_NMOS_ChannelWidth'] = _CLKBufTreeBot_UnitBuf_NMOS_ChannelWidth
        _Caculation_Parameters['_CLKBufTreeBot_UnitBuf_NMOS_ChannelLength'] = _CLKBufTreeBot_UnitBuf_NMOS_ChannelLength
                    ## Pmos
        _Caculation_Parameters['_CLKBufTreeBot_UnitBuf_PMOS_NumberofGate'] = _CLKBufTreeBot_UnitBuf_PMOS_NumberofGate
        _Caculation_Parameters['_CLKBufTreeBot_UnitBuf_PMOS_ChannelWidth'] = _CLKBufTreeBot_UnitBuf_PMOS_ChannelWidth
        _Caculation_Parameters['_CLKBufTreeBot_UnitBuf_PMOS_ChannelLength'] = _CLKBufTreeBot_UnitBuf_PMOS_ChannelLength
                    # Height
        _Caculation_Parameters['_CLKBufTreeBot_UnitBuf_PMOSXvt2NMOSXvt'] = _CLKBufTreeBot_UnitBuf_PMOSXvt2NMOSXvt
                ## Clock Buffer Tree structure
        _Caculation_Parameters['_CLKBufTreeBot_BufTree1and2_NumOfStage'] = _CLKBufTreeBot_BufTree1and2_NumOfStage
        _Caculation_Parameters['_CLKBufTreeBot_BufTree1_SizeofEachStage'] = _CLKBufTreeBot_BufTree1_SizeofEachStage
        _Caculation_Parameters['_CLKBufTreeBot_BufTree2_SizeofEachStage'] = _CLKBufTreeBot_BufTree2_SizeofEachStage
        _Caculation_Parameters['_CLKBufTreeBot_XOffSet'] = _CLKBufTreeBot_XOffSet


        ## Clock Spine (Physical demension)
            ## CLK Source: upward, 1st floor
        _Caculation_Parameters['_YWidthOfCLKSrc'] = _YWidthOfCLKSrc
            ## CLK Samp: upward, 2nd floor
        _Caculation_Parameters['_SpaceBtwCLKSrcAndCLKSamp'] = _SpaceBtwCLKSrcAndCLKSamp
        _Caculation_Parameters['_YWidthOfCLKSamp'] = _YWidthOfCLKSamp
            ## Comparator Output: downward, Basement1
        _Caculation_Parameters['_YWidthOfCompOut'] = _YWidthOfCompOut
            ## CLK Dout: downward, basement2
        _Caculation_Parameters['_SpaceBtwCompOutAndCLKDout'] = _SpaceBtwCompOutAndCLKDout
        _Caculation_Parameters['_YWidthOfCLKDout'] = _YWidthOfCLKDout

        ## SetResetDFF
            ## DFF Common
        _Caculation_Parameters['_Test_distance'] = _Test_distance
        _Caculation_Parameters['_DFF_PMOSXvt2NMOSXvt'] = _DFF_PMOSXvt2NMOSXvt

            ## Master Xgate1
        _Caculation_Parameters['_Mst_Xgate1_XVT'] = _Mst_Xgate1_XVT
        _Caculation_Parameters['_Mst_Xgate1_NMOS_NumberofGate'] = _Mst_Xgate1_NMOS_NumberofGate
        _Caculation_Parameters['_Mst_Xgate1_NMOS_ChannelWidth'] = _Mst_Xgate1_NMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Xgate1_NMOS_ChannelLength'] = _Mst_Xgate1_NMOS_ChannelLength
        _Caculation_Parameters['_Mst_Xgate1_PMOS_NumberofGate'] = _Mst_Xgate1_PMOS_NumberofGate
        _Caculation_Parameters['_Mst_Xgate1_PMOS_ChannelWidth'] = _Mst_Xgate1_PMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Xgate1_PMOS_ChannelLength'] = _Mst_Xgate1_PMOS_ChannelLength
            ## Master Xgate2
        _Caculation_Parameters['_Mst_Xgate2_XVT'] = _Mst_Xgate2_XVT
        _Caculation_Parameters['_Mst_Xgate2_NMOS_NumberofGate'] = _Mst_Xgate2_NMOS_NumberofGate
        _Caculation_Parameters['_Mst_Xgate2_NMOS_ChannelWidth'] = _Mst_Xgate2_NMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Xgate2_NMOS_ChannelLength'] = _Mst_Xgate2_NMOS_ChannelLength
        _Caculation_Parameters['_Mst_Xgate2_PMOS_NumberofGate'] = _Mst_Xgate2_PMOS_NumberofGate
        _Caculation_Parameters['_Mst_Xgate2_PMOS_ChannelWidth'] = _Mst_Xgate2_PMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Xgate2_PMOS_ChannelLength'] = _Mst_Xgate2_PMOS_ChannelLength
            ## Master Nor1
        _Caculation_Parameters['_Mst_Nor1_XVT'] = _Mst_Nor1_XVT
        _Caculation_Parameters['_Mst_Nor1_NMOSA_NumberofGate'] = _Mst_Nor1_NMOSA_NumberofGate
        _Caculation_Parameters['_Mst_Nor1_NMOSA_ChannelWidth'] = _Mst_Nor1_NMOSA_ChannelWidth
        _Caculation_Parameters['_Mst_Nor1_NMOSA_ChannelLength'] = _Mst_Nor1_NMOSA_ChannelLength
        _Caculation_Parameters['_Mst_Nor1_NMOSB_NumberofGate'] = _Mst_Nor1_NMOSB_NumberofGate
        _Caculation_Parameters['_Mst_Nor1_NMOSB_ChannelWidth'] = _Mst_Nor1_NMOSB_ChannelWidth
        _Caculation_Parameters['_Mst_Nor1_NMOSB_ChannelLength'] = _Mst_Nor1_NMOSB_ChannelLength
        _Caculation_Parameters['_Mst_Nor1_PMOSA_NumberofGate'] = _Mst_Nor1_PMOSA_NumberofGate
        _Caculation_Parameters['_Mst_Nor1_PMOSA_ChannelWidth'] = _Mst_Nor1_PMOSA_ChannelWidth
        _Caculation_Parameters['_Mst_Nor1_PMOSA_ChannelLength'] = _Mst_Nor1_PMOSA_ChannelLength
        _Caculation_Parameters['_Mst_Nor1_PMOSB_NumberofGate'] = _Mst_Nor1_PMOSB_NumberofGate
        _Caculation_Parameters['_Mst_Nor1_PMOSB_ChannelWidth'] = _Mst_Nor1_PMOSB_ChannelWidth
        _Caculation_Parameters['_Mst_Nor1_PMOSB_ChannelLength'] = _Mst_Nor1_PMOSB_ChannelLength
            ## Master Nor2
        _Caculation_Parameters['_Mst_Nor2_XVT'] = _Mst_Nor2_XVT
        _Caculation_Parameters['_Mst_Nor2_NMOSA_NumberofGate'] = _Mst_Nor2_NMOSA_NumberofGate
        _Caculation_Parameters['_Mst_Nor2_NMOSA_ChannelWidth'] = _Mst_Nor2_NMOSA_ChannelWidth
        _Caculation_Parameters['_Mst_Nor2_NMOSA_ChannelLength'] = _Mst_Nor2_NMOSA_ChannelLength
        _Caculation_Parameters['_Mst_Nor2_NMOSB_NumberofGate'] = _Mst_Nor2_NMOSB_NumberofGate
        _Caculation_Parameters['_Mst_Nor2_NMOSB_ChannelWidth'] = _Mst_Nor2_NMOSB_ChannelWidth
        _Caculation_Parameters['_Mst_Nor2_NMOSB_ChannelLength'] = _Mst_Nor2_NMOSB_ChannelLength
        _Caculation_Parameters['_Mst_Nor2_PMOSA_NumberofGate'] = _Mst_Nor2_PMOSA_NumberofGate
        _Caculation_Parameters['_Mst_Nor2_PMOSA_ChannelWidth'] = _Mst_Nor2_PMOSA_ChannelWidth
        _Caculation_Parameters['_Mst_Nor2_PMOSA_ChannelLength'] = _Mst_Nor2_PMOSA_ChannelLength
        _Caculation_Parameters['_Mst_Nor2_PMOSB_NumberofGate'] = _Mst_Nor2_PMOSB_NumberofGate
        _Caculation_Parameters['_Mst_Nor2_PMOSB_ChannelWidth'] = _Mst_Nor2_PMOSB_ChannelWidth
        _Caculation_Parameters['_Mst_Nor2_PMOSB_ChannelLength'] = _Mst_Nor2_PMOSB_ChannelLength
            ## Master Inv1
        _Caculation_Parameters['_Mst_Inv1_XVT'] = _Mst_Inv1_XVT
        _Caculation_Parameters['_Mst_Inv1_NMOS_NumberofGate'] = _Mst_Inv1_NMOS_NumberofGate
        _Caculation_Parameters['_Mst_Inv1_NMOS_ChannelWidth'] = _Mst_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Inv1_NMOS_ChannelLength'] = _Mst_Inv1_NMOS_ChannelLength
        _Caculation_Parameters['_Mst_Inv1_PMOS_NumberofGate'] = _Mst_Inv1_PMOS_NumberofGate
        _Caculation_Parameters['_Mst_Inv1_PMOS_ChannelWidth'] = _Mst_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Inv1_PMOS_ChannelLength'] = _Mst_Inv1_PMOS_ChannelLength
            ## Master Inv2
        _Caculation_Parameters['_Mst_Inv2_XVT'] = _Mst_Inv2_XVT
        _Caculation_Parameters['_Mst_Inv2_NMOS_NumberofGate'] = _Mst_Inv2_NMOS_NumberofGate
        _Caculation_Parameters['_Mst_Inv2_NMOS_ChannelWidth'] = _Mst_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Inv2_NMOS_ChannelLength'] = _Mst_Inv2_NMOS_ChannelLength
        _Caculation_Parameters['_Mst_Inv2_PMOS_NumberofGate'] = _Mst_Inv2_PMOS_NumberofGate
        _Caculation_Parameters['_Mst_Inv2_PMOS_ChannelWidth'] = _Mst_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Inv2_PMOS_ChannelLength'] = _Mst_Inv2_PMOS_ChannelLength
            ## Master Inv3
        _Caculation_Parameters['_Mst_Inv3_XVT'] = _Mst_Inv3_XVT
        _Caculation_Parameters['_Mst_Inv3_NMOS_NumberofGate'] = _Mst_Inv3_NMOS_NumberofGate
        _Caculation_Parameters['_Mst_Inv3_NMOS_ChannelWidth'] = _Mst_Inv3_NMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Inv3_NMOS_ChannelLength'] = _Mst_Inv3_NMOS_ChannelLength
        _Caculation_Parameters['_Mst_Inv3_PMOS_NumberofGate'] = _Mst_Inv3_PMOS_NumberofGate
        _Caculation_Parameters['_Mst_Inv3_PMOS_ChannelWidth'] = _Mst_Inv3_PMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Inv3_PMOS_ChannelLength'] = _Mst_Inv3_PMOS_ChannelLength
            ## Slave Xgate1
        _Caculation_Parameters['_Slv_Xgate1_XVT'] = _Slv_Xgate1_XVT
        _Caculation_Parameters['_Slv_Xgate1_NMOS_NumberofGate'] = _Slv_Xgate1_NMOS_NumberofGate
        _Caculation_Parameters['_Slv_Xgate1_NMOS_ChannelWidth'] = _Slv_Xgate1_NMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Xgate1_NMOS_ChannelLength'] = _Slv_Xgate1_NMOS_ChannelLength
        _Caculation_Parameters['_Slv_Xgate1_PMOS_NumberofGate'] = _Slv_Xgate1_PMOS_NumberofGate
        _Caculation_Parameters['_Slv_Xgate1_PMOS_ChannelWidth'] = _Slv_Xgate1_PMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Xgate1_PMOS_ChannelLength'] = _Slv_Xgate1_PMOS_ChannelLength
            ## Slave Xgate2
        _Caculation_Parameters['_Slv_Xgate2_XVT'] = _Slv_Xgate2_XVT
        _Caculation_Parameters['_Slv_Xgate2_NMOS_NumberofGate'] = _Slv_Xgate2_NMOS_NumberofGate
        _Caculation_Parameters['_Slv_Xgate2_NMOS_ChannelWidth'] = _Slv_Xgate2_NMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Xgate2_NMOS_ChannelLength'] = _Slv_Xgate2_NMOS_ChannelLength
        _Caculation_Parameters['_Slv_Xgate2_PMOS_NumberofGate'] = _Slv_Xgate2_PMOS_NumberofGate
        _Caculation_Parameters['_Slv_Xgate2_PMOS_ChannelWidth'] = _Slv_Xgate2_PMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Xgate2_PMOS_ChannelLength'] = _Slv_Xgate2_PMOS_ChannelLength
            ## Slave Nor1
        _Caculation_Parameters['_Slv_Nor1_XVT'] = _Slv_Nor1_XVT
        _Caculation_Parameters['_Slv_Nor1_NMOSA_NumberofGate'] = _Slv_Nor1_NMOSA_NumberofGate
        _Caculation_Parameters['_Slv_Nor1_NMOSA_ChannelWidth'] = _Slv_Nor1_NMOSA_ChannelWidth
        _Caculation_Parameters['_Slv_Nor1_NMOSA_ChannelLength'] = _Slv_Nor1_NMOSA_ChannelLength
        _Caculation_Parameters['_Slv_Nor1_NMOSB_NumberofGate'] = _Slv_Nor1_NMOSB_NumberofGate
        _Caculation_Parameters['_Slv_Nor1_NMOSB_ChannelWidth'] = _Slv_Nor1_NMOSB_ChannelWidth
        _Caculation_Parameters['_Slv_Nor1_NMOSB_ChannelLength'] = _Slv_Nor1_NMOSB_ChannelLength
        _Caculation_Parameters['_Slv_Nor1_PMOSA_NumberofGate'] = _Slv_Nor1_PMOSA_NumberofGate
        _Caculation_Parameters['_Slv_Nor1_PMOSA_ChannelWidth'] = _Slv_Nor1_PMOSA_ChannelWidth
        _Caculation_Parameters['_Slv_Nor1_PMOSA_ChannelLength'] = _Slv_Nor1_PMOSA_ChannelLength
        _Caculation_Parameters['_Slv_Nor1_PMOSB_NumberofGate'] = _Slv_Nor1_PMOSB_NumberofGate
        _Caculation_Parameters['_Slv_Nor1_PMOSB_ChannelWidth'] = _Slv_Nor1_PMOSB_ChannelWidth
        _Caculation_Parameters['_Slv_Nor1_PMOSB_ChannelLength'] = _Slv_Nor1_PMOSB_ChannelLength
            ## Slave Nor2
        _Caculation_Parameters['_Slv_Nor2_XVT'] = _Slv_Nor2_XVT
        _Caculation_Parameters['_Slv_Nor2_NMOSA_NumberofGate'] = _Slv_Nor2_NMOSA_NumberofGate
        _Caculation_Parameters['_Slv_Nor2_NMOSA_ChannelWidth'] = _Slv_Nor2_NMOSA_ChannelWidth
        _Caculation_Parameters['_Slv_Nor2_NMOSA_ChannelLength'] = _Slv_Nor2_NMOSA_ChannelLength
        _Caculation_Parameters['_Slv_Nor2_NMOSB_NumberofGate'] = _Slv_Nor2_NMOSB_NumberofGate
        _Caculation_Parameters['_Slv_Nor2_NMOSB_ChannelWidth'] = _Slv_Nor2_NMOSB_ChannelWidth
        _Caculation_Parameters['_Slv_Nor2_NMOSB_ChannelLength'] = _Slv_Nor2_NMOSB_ChannelLength
        _Caculation_Parameters['_Slv_Nor2_PMOSA_NumberofGate'] = _Slv_Nor2_PMOSA_NumberofGate
        _Caculation_Parameters['_Slv_Nor2_PMOSA_ChannelWidth'] = _Slv_Nor2_PMOSA_ChannelWidth
        _Caculation_Parameters['_Slv_Nor2_PMOSA_ChannelLength'] = _Slv_Nor2_PMOSA_ChannelLength
        _Caculation_Parameters['_Slv_Nor2_PMOSB_NumberofGate'] = _Slv_Nor2_PMOSB_NumberofGate
        _Caculation_Parameters['_Slv_Nor2_PMOSB_ChannelWidth'] = _Slv_Nor2_PMOSB_ChannelWidth
        _Caculation_Parameters['_Slv_Nor2_PMOSB_ChannelLength'] = _Slv_Nor2_PMOSB_ChannelLength
            ## Slave Inv1
        _Caculation_Parameters['_Slv_Inv1_XVT'] = _Slv_Inv1_XVT
        _Caculation_Parameters['_Slv_Inv1_NMOS_NumberofGate'] = _Slv_Inv1_NMOS_NumberofGate
        _Caculation_Parameters['_Slv_Inv1_NMOS_ChannelWidth'] = _Slv_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Inv1_NMOS_ChannelLength'] = _Slv_Inv1_NMOS_ChannelLength
        _Caculation_Parameters['_Slv_Inv1_PMOS_NumberofGate'] = _Slv_Inv1_PMOS_NumberofGate
        _Caculation_Parameters['_Slv_Inv1_PMOS_ChannelWidth'] = _Slv_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Inv1_PMOS_ChannelLength'] = _Slv_Inv1_PMOS_ChannelLength
            ## Slave Inv2
        _Caculation_Parameters['_Slv_Inv2_XVT'] = _Slv_Inv2_XVT
        _Caculation_Parameters['_Slv_Inv2_NMOS_NumberofGate'] = _Slv_Inv2_NMOS_NumberofGate
        _Caculation_Parameters['_Slv_Inv2_NMOS_ChannelWidth'] = _Slv_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Inv2_NMOS_ChannelLength'] = _Slv_Inv2_NMOS_ChannelLength
        _Caculation_Parameters['_Slv_Inv2_PMOS_NumberofGate'] = _Slv_Inv2_PMOS_NumberofGate
        _Caculation_Parameters['_Slv_Inv2_PMOS_ChannelWidth'] = _Slv_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Inv2_PMOS_ChannelLength'] = _Slv_Inv2_PMOS_ChannelLength
            ## Slave Inv3
        _Caculation_Parameters['_Slv_Inv3_XVT'] = _Slv_Inv3_XVT
        _Caculation_Parameters['_Slv_Inv3_NMOS_NumberofGate'] = _Slv_Inv3_NMOS_NumberofGate
        _Caculation_Parameters['_Slv_Inv3_NMOS_ChannelWidth'] = _Slv_Inv3_NMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Inv3_NMOS_ChannelLength'] = _Slv_Inv3_NMOS_ChannelLength
        _Caculation_Parameters['_Slv_Inv3_PMOS_NumberofGate'] = _Slv_Inv3_PMOS_NumberofGate
        _Caculation_Parameters['_Slv_Inv3_PMOS_ChannelWidth'] = _Slv_Inv3_PMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Inv3_PMOS_ChannelLength'] = _Slv_Inv3_PMOS_ChannelLength

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_SARLogicWtCLKTree'] = self._SrefElementDeclaration(_DesignObj=K00_01_SARLogicWtCLKBufTree._SARLogicWtCLKBufTree(_DesignParameter=None, _Name='{}:SRF_SARLogicWtCLKTree'.format(_Name)))[0]

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SARLogicWtCLKTree']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_SARLogicWtCLKTree']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SARLogicWtCLKTree']['_Angle'] = 0

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SARLogicWtCLKTree']['_XYCoordinates'] = [[0, 0]]

        ## Pre-Calculated Design Parameter ('_CDACPreDriver_Distance')
        tmp = self.get_param_KJH4('SRF_SARLogicWtCLKTree', 'SRF_SARLogic', 'SRF_DAC_Ctrl', 'SRF_Net21_ViaM1M3', 'SRF_ViaM2M3', 'BND_Met2Layer')
        CDACPreDriver_Distance = abs(tmp[0][0][0][0][0][0][0]['_XY_left'][0] - tmp[0][0][1][0][0][0][0]['_XY_left'][0])
        XCoordOfFF0Out_cent = tmp[0][0][0][0][0][0][0]['_XY_cent'][0]
        tmp = self.get_param_KJH4('SRF_SARLogicWtCLKTree', 'SRF_SARLogic', 'SRF_DACCtrl_QB_DoutSamp_D_ViaM2M4', 'SRF_ViaM2M3', 'BND_Met2Layer')
        XCoordOfFF0OutBar_cent = tmp[0][0][0][0][0][0]['_XY_cent'][0]


        ###########################################################################################################################################################
        ## SRF_UpperCDACPreDriver Generation
        _Caculation_Parameters = copy.deepcopy(J00_02_CDAC_PreDriver_KJH._CDAC_PreDriver._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        ## DAC PreDriver
            ## Buf to Buf distance
        _Caculation_Parameters['_Buf2BufDistance']          = CDACPreDriver_Distance
            ## InvChain Common
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']          = _DACPreDrv_PMOSXvt2NMOSXvt
            ## Inverter Chain
        _Caculation_Parameters['_NumberofGate']             = _DACPreDrv_NumberofGate
        _Caculation_Parameters['_ChannelLength']            = _DACPreDrv_ChannelLength
        _Caculation_Parameters['_XVT']                      = _DACPreDrv_XVT
        _Caculation_Parameters['_Inv_NMOS_ChannelWidth']    = _DACPreDrv_Inv_NMOS_ChannelWidth
        _Caculation_Parameters['_Inv_PMOS_ChannelWidth']    = _DACPreDrv_Inv_PMOS_ChannelWidth


        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_UpperCDACPreDriver'] = self._SrefElementDeclaration(_DesignObj=J00_02_CDAC_PreDriver_KJH._CDAC_PreDriver(_DesignParameter=None, _Name='{}:SRF_UpperCDACPreDriver'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_UpperCDACPreDriver']['_Reflect'] = [1, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_UpperCDACPreDriver']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_UpperCDACPreDriver']['_DesignObj']._CalculateDesignParameter(
            **_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_UpperCDACPreDriver']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord
        tmp2x = XCoordOfFF0Out_cent
        tmp2y = self.get_param_KJH4('SRF_SARLogicWtCLKTree', 'SRF_CLKBufferTree_Top', 'BND_Nbody_M1')
        target_coord = [tmp2x, tmp2y[0][0][0][0]['_XY_down_left'][1]]
        ## Approaching_coord
        tmp1x = self.get_param_KJH4('SRF_UpperCDACPreDriver', 'SRF_InvChain0', 'SRF_Input_ViaM1Mx', 'SRF_ViaM1M2', 'BND_Met1Layer')
        tmp1y = self.get_param_KJH4('SRF_UpperCDACPreDriver', 'BND_Nbody_M1Exten')
        approaching_coord = [tmp1x[0][0][0][0][0][0]['_XY_left'][0], tmp1y[0][0][0]['_XY_up'][1]]
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_UpperCDACPreDriver')
        Scoord = tmp3[0][0]['_XY_origin']
        Xoffset = 0
        Scoord[0] = Scoord[0] + Xoffset
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_UpperCDACPreDriver']['_XYCoordinates'] = tmpXY



        ###########################################################################################################################################################
        ## SRF_LowerCDACPreDriver Generation
        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_LowerCDACPreDriver'] = self._SrefElementDeclaration(_DesignObj=J00_02_CDAC_PreDriver_KJH._CDAC_PreDriver(_DesignParameter=None, _Name='{}:SRF_LowerCDACPreDriver'.format(_Name)))[0]

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        # self._DesignParameter['SRF_LowerCDACPreDriver']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters) # to reduce time
        self._DesignParameter['SRF_LowerCDACPreDriver'] = copy.deepcopy(self._DesignParameter['SRF_UpperCDACPreDriver'])
        self.rename_srf_prefix(self._DesignParameter['SRF_LowerCDACPreDriver'], 'SRF_UpperCDACPreDriver','SRF_LowerCDACPreDriver')

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_LowerCDACPreDriver']['_Reflect'] = [1, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_LowerCDACPreDriver']['_Angle'] = 0

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_LowerCDACPreDriver']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord
        tmp2x = XCoordOfFF0OutBar_cent
        tmp2y = self.get_param_KJH4('SRF_SARLogicWtCLKTree', 'SRF_CLKBufferTree_Bot', 'BND_Pbody_M1')
        target_coord = [tmp2x, tmp2y[0][0][0][0]['_XY_down_left'][1]]
        ## Approaching_coord
        tmp1x = self.get_param_KJH4('SRF_LowerCDACPreDriver', 'SRF_InvChain0', 'SRF_Input_ViaM1Mx', 'SRF_ViaM1M2', 'BND_Met1Layer')
        tmp1y = self.get_param_KJH4('SRF_LowerCDACPreDriver', 'BND_Pbody_M1Exten')
        approaching_coord = [tmp1x[0][0][0][0][0][0]['_XY_left'][0], tmp1y[0][0][0]['_XY_up'][1]]
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_LowerCDACPreDriver')
        Scoord = tmp3[0][0]['_XY_origin']
        Xoffset = 0
        Scoord[0] = Scoord[0] + Xoffset
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_LowerCDACPreDriver']['_XYCoordinates'] = tmpXY



        ###########################################################################################################################################################
        ######## DACCtrl F/F Out(Q) -> Upper CDAC Pre-Driver
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_UpperCDACPreDrvIn_ViaM3M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_UpperCDACPreDrvIn_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_UpperCDACPreDrvIn_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_UpperCDACPreDrvIn_ViaM3M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_UpperCDACPreDrvIn_ViaM3M4']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_UpperCDACPreDrvIn_ViaM3M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_UpperCDACPreDrvIn_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_UpperCDACPreDrvIn_ViaM3M4')
        Scoord = tmp3[0][0]['_XY_origin']

        ## Target_coord
        tmp = self.get_param_KJH4('SRF_SARLogicWtCLKTree', 'SRF_SARLogic', 'SRF_DAC_Ctrl', 'SRF_Net21_ViaM1M3','SRF_ViaM2M3', 'BND_Met2Layer')
        for i in range(_NumofBit):
            target_coord = tmp[0][0][i][0][0][0][0]['_XY_cent']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define
        self._DesignParameter['SRF_UpperCDACPreDrvIn_ViaM3M4']['_XYCoordinates'] = tmpXY

        ###########################################################################################################################################################
        ######## DACCtrl F/F Out(QB) -> Lower CDAC Pre-Driver
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_LowerCDACPreDrvIn_Vtc_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('SRF_SARLogicWtCLKTree', 'SRF_SARLogic', 'SRF_DACCtrl_QB_DoutSamp_D_ViaM2M4', 'SRF_ViaM2M3', 'BND_Met2Layer')
        tmp1 = self.get_param_KJH4('SRF_LowerCDACPreDriver', 'SRF_InvChain0', 'SRF_Input_ViaM1Mx', 'SRF_ViaM1M2', 'BND_Met1Layer')
        self._DesignParameter['BND_LowerCDACPreDrvIn_Vtc_M4']['_YWidth'] = abs(tmp[0][0][0][0][0][0]['_XY_up'][1] - tmp1[0][0][0][0][0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_LowerCDACPreDrvIn_Vtc_M4']['_XWidth'] = tmp[0][0][0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_LowerCDACPreDrvIn_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        tmp2 = self.get_param_KJH4('BND_LowerCDACPreDrvIn_Vtc_M4')
        approaching_coord = tmp2[0][0]['_XY_up']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_LowerCDACPreDrvIn_Vtc_M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        for i in range(_NumofBit):
            target_coord = tmp[0][0][i][0][0][0]['_XY_up']
            ## Approaching_coord: _XY_type2
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_LowerCDACPreDrvIn_Vtc_M4']['_XYCoordinates'] = tmpXY


        ###########################################################################################################################################################

        ######## DACCtrl F/F Out(Q) -> Upper CDAC Pre-Driver
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_UpperCDACPreDrvIn_Vtc_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('SRF_SARLogicWtCLKTree', 'SRF_SARLogic', 'SRF_DAC_Ctrl', 'SRF_Net21_ViaM1M3', 'SRF_ViaM2M3', 'BND_Met2Layer')
        tmp1 = self.get_param_KJH4('SRF_UpperCDACPreDriver', 'SRF_InvChain0', 'SRF_Input_ViaM1Mx', 'SRF_ViaM1M2', 'BND_Met1Layer')
        self._DesignParameter['BND_UpperCDACPreDrvIn_Vtc_M4']['_YWidth'] = abs(tmp[0][0][0][0][0][0][0]['_XY_down'][1] - tmp1[0][0][0][0][0][0]['_XY_down'][1])

        ## Define Boundary_element _XWidth
        BND_UpperCDACPreDrvIn_Vtc_M4_PathWidth = 50
        self._DesignParameter['BND_UpperCDACPreDrvIn_Vtc_M4']['_XWidth'] = BND_UpperCDACPreDrvIn_Vtc_M4_PathWidth

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_UpperCDACPreDrvIn_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        tmp2 = self.get_param_KJH4('BND_UpperCDACPreDrvIn_Vtc_M4')
        approaching_coord = tmp2[0][0]['_XY_down']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_UpperCDACPreDrvIn_Vtc_M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        for i in range(_NumofBit):
            target_coord = tmp[0][0][i][0][0][0][0]['_XY_down']
            ## Approaching_coord: _XY_type2
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_UpperCDACPreDrvIn_Vtc_M4']['_XYCoordinates'] = tmpXY

        ########################################################################################################################################################### CLKDout
        _CLKOutSamp_PMOSXvt2NMOSXvt = _DFF_PMOSXvt2NMOSXvt
        ## SRF_CLKDout_Inv First Gen
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## INV
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  INV: Sref Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D00_00_Inverter_KJH._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_XVT'] = _CLKoutSamp_XVT

        _Caculation_Parameters['_NMOS_NumberofGate'] = _CLKoutSamp_Inv_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth'] = _CLKoutSamp_Inv_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength'] = _CLKoutSamp_Inv_NMOS_ChannelLength

        _Caculation_Parameters['_PMOS_NumberofGate'] = _CLKoutSamp_Inv_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth'] = _CLKoutSamp_Inv_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength'] = _CLKoutSamp_Inv_PMOS_ChannelLength

        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody'] = None
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody'] = None

        _Caculation_Parameters['_PMOSXvt2NMOSXvt'] = _CLKOutSamp_PMOSXvt2NMOSXvt

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKDout_Inv'] = self._SrefElementDeclaration(_DesignObj=D00_00_Inverter_KJH._Inverter(_DesignParameter=None, _Name='{}:SRF_CLKDout_Inv'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKDout_Inv']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKDout_Inv']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CLKDout_Inv']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKDout_Inv']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1x = self.get_param_KJH4('SRF_SARLogicWtCLKTree', 'SRF_SARLogic', 'SRF_DAC_Ctrl', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'SRF_PMOS', 'BND_{}Layer'.format(_Slv_Inv3_XVT))
        tmp1y = self.get_param_KJH4('SRF_SARLogicWtCLKTree', 'SRF_SARLogic', 'BND_Nbody_M1Exten')
        target_coord = [tmp1x[0][0][-1][0][0][0][0][0]['_XY_right'][0], tmp1y[0][0][0][0]['_XY_up'][1]]
        ## Approaching_coord
        tmp2x = self.get_param_KJH4('SRF_CLKDout_Inv', 'SRF_PMOS', 'BND_{}Layer'.format(_CLKoutSamp_XVT))
        tmp2y = self.get_param_KJH4('SRF_CLKDout_Inv', 'SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = [tmp2x[0][0][0][0]['_XY_left'][0], tmp2y[0][0][0][0][0]['_XY_up'][1]]
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKDout_Inv')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[0] = Scoord[0] + 360
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKDout_Inv']['_XYCoordinates'] = tmpXY

        ###########################################################################################################################################################
        ## SRF_CLKDOut_AND First gen
        ### AND Gate SREF Generation
        _Caculation_Parameters = copy.deepcopy(D03_03_And_KJH0._And._ParametersForDesignCalculation)
        ## AND
            ## AND Common
                # XVT
        _Caculation_Parameters['_AND_XVT'] = _CLKoutSamp_XVT
                # Height
        _Caculation_Parameters['_And_PMOSXvt2NMOSXvt'] = _CLKOutSamp_PMOSXvt2NMOSXvt
            ## Nand
                # NmosA
        _Caculation_Parameters['_Nand_NMOSA_NumberofGate'] = _CLKoutSamp_And_Nand_NMOSA_NumberofGate
        _Caculation_Parameters['_Nand_NMOSA_ChannelWidth'] = _CLKoutSamp_And_Nand_NMOSA_ChannelWidth
        _Caculation_Parameters['_Nand_NMOSA_ChannelLength'] = _CLKoutSamp_And_Nand_NMOSA_ChannelLength
                # NMOSB
        _Caculation_Parameters['_Nand_NMOSB_NumberofGate'] = _CLKoutSamp_And_Nand_NMOSB_NumberofGate
        _Caculation_Parameters['_Nand_NMOSB_ChannelWidth'] = _CLKoutSamp_And_Nand_NMOSB_ChannelWidth
        _Caculation_Parameters['_Nand_NMOSB_ChannelLength'] = _CLKoutSamp_And_Nand_NMOSB_ChannelLength
                # PMOSA
        _Caculation_Parameters['_Nand_PMOSA_NumberofGate'] = _CLKoutSamp_And_Nand_PMOSA_NumberofGate
        _Caculation_Parameters['_Nand_PMOSA_ChannelWidth'] = _CLKoutSamp_And_Nand_PMOSA_ChannelWidth
        _Caculation_Parameters['_Nand_PMOSA_ChannelLength'] = _CLKoutSamp_And_Nand_PMOSA_ChannelLength
                # PMOSB
        _Caculation_Parameters['_Nand_PMOSB_NumberofGate'] = _CLKoutSamp_And_Nand_PMOSB_NumberofGate
        _Caculation_Parameters['_Nand_PMOSB_ChannelWidth'] = _CLKoutSamp_And_Nand_PMOSB_ChannelWidth
        _Caculation_Parameters['_Nand_PMOSB_ChannelLength'] = _CLKoutSamp_And_Nand_PMOSB_ChannelLength
                # Body
        _Caculation_Parameters['_Nand_NMOSAB_Pbody_XvtTop2Pbody'] = None
        _Caculation_Parameters['_Nand_PMOSAB_Nbody_Xvtdown2Nbody'] = None
            ## Inverter
                # Nmos
        _Caculation_Parameters['_Inv_NMOS_NumberofGate'] = _CLKoutSamp_And_Inv_NMOS_NumberofGate
        _Caculation_Parameters['_Inv_NMOS_ChannelWidth'] = _CLKoutSamp_And_Inv_NMOS_ChannelWidth
        _Caculation_Parameters['_Inv_NMOS_ChannelLength'] = _CLKoutSamp_And_Inv_NMOS_ChannelLength
                # Pmos
        _Caculation_Parameters['_Inv_PMOS_NumberofGate'] = _CLKoutSamp_And_Inv_PMOS_NumberofGate
        _Caculation_Parameters['_Inv_PMOS_ChannelWidth'] = _CLKoutSamp_And_Inv_PMOS_ChannelWidth
        _Caculation_Parameters['_Inv_PMOS_ChannelLength'] = _CLKoutSamp_And_Inv_PMOS_ChannelLength
                # Body
        _Caculation_Parameters['_Inv_NMOS_Pbody_XvtTop2Pbody'] = None
        _Caculation_Parameters['_Inv_PMOS_Nbody_Xvtdown2Nbody'] = None

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKDout_AND'] = self._SrefElementDeclaration(_DesignObj=D03_03_And_KJH0._And(_DesignParameter=None, _Name='{}:SRF_CLKDout_AND'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKDout_AND']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKDout_AND']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CLKDout_AND']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKDout_AND']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1x = self.get_param_KJH4('SRF_CLKDout_Inv', 'SRF_PMOS', 'BND_{}Layer'.format(_CLKoutSamp_XVT))
        tmp1y = self.get_param_KJH4('SRF_CLKDout_Inv', 'SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        target_coord = [tmp1x[0][0][0][0]['_XY_right'][0], tmp1y[0][0][0][0][0]['_XY_up'][1]]
        ## Approaching_coord
        tmp2x = self.get_param_KJH4('SRF_CLKDout_AND', 'SRF_NAND', 'SRF_Pulldown', 'SRF_NMOSB', 'BND_{}Layer'.format(_CLKoutSamp_XVT))
        tmp2y = self.get_param_KJH4('SRF_CLKDout_AND', 'SRF_Inverter', 'SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = [tmp2x[0][0][0][0][0][0]['_XY_right'][0], tmp2y[0][0][0][0][0][0]['_XY_up'][1]]
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKDout_AND')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[0] = Scoord[0] + 126  # Dummy Poly간 최소 거리 DRC: 96 + 폴리 두께
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKDout_AND']['_XYCoordinates'] = tmpXY

        ###########################################################################################################################################################
        ## Cal: _CLKOutSamp_PMOSXvt2NMOSXvt :SRF_SARLogicWtCLKTree:SRF_SARLogic:SRF_DAC_Ctrl:SRF_SetRst_Placement:SRF_Slv_Inv3
        tmp1 = self.get_param_KJH4('SRF_SARLogicWtCLKTree','SRF_SARLogic','SRF_DAC_Ctrl','SRF_SetRst_Placement','SRF_Slv_Inv3','SRF_NMOS','BND_{}Layer'.format(_Slv_Inv3_XVT))
        tmp2 = self.get_param_KJH4('SRF_SARLogicWtCLKTree','SRF_SARLogic','SRF_DAC_Ctrl','SRF_SetRst_Placement','SRF_Slv_Inv3','SRF_PMOS','BND_{}Layer'.format(_Slv_Inv3_XVT))
        tmp3 = self.get_param_KJH4('SRF_SARLogicWtCLKTree','SRF_SARLogic','SRF_DAC_Ctrl','SRF_SetRst_Placement','SRF_Slv_Inv3','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        tmp4 = self.get_param_KJH4('SRF_SARLogicWtCLKTree','SRF_SARLogic','SRF_DAC_Ctrl','SRF_SetRst_Placement','SRF_Slv_Inv3','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')

        Logic_Xvt2Xvt = abs(tmp1[0][0][0][0][0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0][0][0][0]['_XY_down'][1])
        Logic_XvtTop2Pbody = abs(tmp1[0][0][0][0][0][0][0][0]['_XY_up'][1] - tmp3[0][0][0][0][0][0][0][0][0]['_XY_up'][1])
        Logic_Xvtdown2Nbody = abs(tmp4[0][0][0][0][0][0][0][0][0]['_XY_down'][1]-tmp2[0][0][0][0][0][0][0][0]['_XY_down'][1])
        Logic_Height = abs(tmp3[0][0][0][0][0][0][0][0][0]['_XY_up'][1]-tmp4[0][0][0][0][0][0][0][0][0]['_XY_down'][1])

        tmp5 = self.get_param_KJH4('SRF_CLKDout_Inv','SRF_NMOS','BND_{}Layer'.format(_CLKoutSamp_XVT))
        tmp6 = self.get_param_KJH4('SRF_CLKDout_Inv','SRF_PMOS', 'BND_{}Layer'.format(_CLKoutSamp_XVT))
        tmp7 = self.get_param_KJH4('SRF_CLKDout_Inv','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        tmp8 = self.get_param_KJH4('SRF_CLKDout_Inv', 'SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')

        Inv_Xvt2Xvt = abs(tmp5[0][0][0][0]['_XY_up'][1] - tmp6[0][0][0][0]['_XY_down'][1])
        Inv_XvtTop2Pbody = abs(tmp5[0][0][0][0]['_XY_up'][1] - tmp7[0][0][0][0][0]['_XY_up'][1])
        Inv_Xvtdown2Nbody = abs(tmp8[0][0][0][0][0]['_XY_down'][1] - tmp6[0][0][0][0]['_XY_down'][1])
        Inv_Height = abs(tmp7[0][0][0][0][0]['_XY_up'][1]-tmp8[0][0][0][0][0]['_XY_down'][1])

        tmp9 = self.get_param_KJH4('SRF_CLKDout_AND','SRF_Inverter','SRF_NMOS','BND_{}Layer'.format(_CLKoutSamp_XVT))
        tmp10 = self.get_param_KJH4('SRF_CLKDout_AND','SRF_Inverter','SRF_PMOS','BND_{}Layer'.format(_CLKoutSamp_XVT))
        tmp11 = self.get_param_KJH4('SRF_CLKDout_AND','SRF_Inverter','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        tmp12 = self.get_param_KJH4('SRF_CLKDout_AND','SRF_Inverter','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')

        Nand_Xvt2Xvt = abs(tmp9[0][0][0][0][0]['_XY_up'][1] - tmp10[0][0][0][0][0]['_XY_down'][1])
        Nand_XvtTop2Pbody = abs(tmp9[0][0][0][0][0]['_XY_up'][1] - tmp11[0][0][0][0][0][0]['_XY_up'][1])
        Nand_Xvtdown2Nbody = abs(tmp12[0][0][0][0][0][0]['_XY_down'][1] - tmp10[0][0][0][0][0]['_XY_down'][1])
        Nand_Height = abs(tmp11[0][0][0][0][0][0]['_XY_up'][1]-tmp12[0][0][0][0][0][0]['_XY_down'][1])

        Sampout_XvtTop2Pbody  = max(Inv_XvtTop2Pbody,Nand_XvtTop2Pbody)
        Sampout_Xvtdown2Nbody = max(Inv_Xvtdown2Nbody,Nand_Xvtdown2Nbody)

        if Logic_XvtTop2Pbody>Sampout_XvtTop2Pbody and Logic_Xvtdown2Nbody>Sampout_Xvtdown2Nbody:
            Tmp_Sampout_XvtTop2Pbody = Logic_XvtTop2Pbody
            Tmp_Sampout_Xvtdown2Nbody = Logic_Xvtdown2Nbody
        else:
            Tmp_Sampout_XvtTop2Pbody = Sampout_XvtTop2Pbody
            Tmp_Sampout_Xvtdown2Nbody =Sampout_Xvtdown2Nbody

        ###########################################################################################################################################################
        ## SRF_CLKDout_Inv Re-Gen
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## INV
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  INV: Sref Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D00_00_Inverter_KJH._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_XVT'] = _CLKoutSamp_XVT

        _Caculation_Parameters['_NMOS_NumberofGate'] = _CLKoutSamp_Inv_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth'] = _CLKoutSamp_Inv_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength'] = _CLKoutSamp_Inv_NMOS_ChannelLength

        _Caculation_Parameters['_PMOS_NumberofGate'] = _CLKoutSamp_Inv_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth'] = _CLKoutSamp_Inv_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength'] = _CLKoutSamp_Inv_PMOS_ChannelLength

        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody'] = Tmp_Sampout_XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody'] = Tmp_Sampout_Xvtdown2Nbody

        _Caculation_Parameters['_PMOSXvt2NMOSXvt'] = _CLKOutSamp_PMOSXvt2NMOSXvt

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKDout_Inv'] = self._SrefElementDeclaration(_DesignObj=D00_00_Inverter_KJH._Inverter(_DesignParameter=None, _Name='{}:SRF_CLKDout_Inv'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKDout_Inv']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKDout_Inv']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CLKDout_Inv']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKDout_Inv']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1x = self.get_param_KJH4('SRF_SARLogicWtCLKTree', 'SRF_SARLogic', 'SRF_DAC_Ctrl', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'SRF_PMOS', 'BND_{}Layer'.format(_Slv_Inv3_XVT))
        tmp1y = self.get_param_KJH4('SRF_SARLogicWtCLKTree', 'SRF_SARLogic', 'BND_Nbody_M1Exten')
        target_coord = [tmp1x[0][0][-1][0][0][0][0][0]['_XY_right'][0], tmp1y[0][0][0][0]['_XY_up'][1]]
        ## Approaching_coord
        tmp2x = self.get_param_KJH4('SRF_CLKDout_Inv', 'SRF_PMOS', 'BND_{}Layer'.format(_CLKoutSamp_XVT))
        tmp2y = self.get_param_KJH4('SRF_CLKDout_Inv', 'SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = [tmp2x[0][0][0][0]['_XY_left'][0], tmp2y[0][0][0][0][0]['_XY_up'][1]]
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKDout_Inv')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[0] = Scoord[0] + 360
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKDout_Inv']['_XYCoordinates'] = tmpXY

        ###########################################################################################################################################################
        ## SRF_CLKDOut_AND Re-gen
        ### AND Gate SREF Generation
        _Caculation_Parameters = copy.deepcopy(D03_03_And_KJH0._And._ParametersForDesignCalculation)
        ## AND
            ## AND Common
                # XVT
        _Caculation_Parameters['_AND_XVT'] = _CLKoutSamp_XVT
                # Height
        _Caculation_Parameters['_And_PMOSXvt2NMOSXvt'] = _CLKOutSamp_PMOSXvt2NMOSXvt
            ## Nand
                # NmosA
        _Caculation_Parameters['_Nand_NMOSA_NumberofGate'] = _CLKoutSamp_And_Nand_NMOSA_NumberofGate
        _Caculation_Parameters['_Nand_NMOSA_ChannelWidth'] = _CLKoutSamp_And_Nand_NMOSA_ChannelWidth
        _Caculation_Parameters['_Nand_NMOSA_ChannelLength'] = _CLKoutSamp_And_Nand_NMOSA_ChannelLength
                # NMOSB
        _Caculation_Parameters['_Nand_NMOSB_NumberofGate'] = _CLKoutSamp_And_Nand_NMOSB_NumberofGate
        _Caculation_Parameters['_Nand_NMOSB_ChannelWidth'] = _CLKoutSamp_And_Nand_NMOSB_ChannelWidth
        _Caculation_Parameters['_Nand_NMOSB_ChannelLength'] = _CLKoutSamp_And_Nand_NMOSB_ChannelLength
                # PMOSA
        _Caculation_Parameters['_Nand_PMOSA_NumberofGate'] = _CLKoutSamp_And_Nand_PMOSA_NumberofGate
        _Caculation_Parameters['_Nand_PMOSA_ChannelWidth'] = _CLKoutSamp_And_Nand_PMOSA_ChannelWidth
        _Caculation_Parameters['_Nand_PMOSA_ChannelLength'] = _CLKoutSamp_And_Nand_PMOSA_ChannelLength
                # PMOSB
        _Caculation_Parameters['_Nand_PMOSB_NumberofGate'] = _CLKoutSamp_And_Nand_PMOSB_NumberofGate
        _Caculation_Parameters['_Nand_PMOSB_ChannelWidth'] = _CLKoutSamp_And_Nand_PMOSB_ChannelWidth
        _Caculation_Parameters['_Nand_PMOSB_ChannelLength'] = _CLKoutSamp_And_Nand_PMOSB_ChannelLength
                # Body
        _Caculation_Parameters['_Nand_NMOSAB_Pbody_XvtTop2Pbody'] = Tmp_Sampout_XvtTop2Pbody
        _Caculation_Parameters['_Nand_PMOSAB_Nbody_Xvtdown2Nbody'] = Tmp_Sampout_Xvtdown2Nbody
            ## Inverter
                # Nmos
        _Caculation_Parameters['_Inv_NMOS_NumberofGate'] = _CLKoutSamp_And_Inv_NMOS_NumberofGate
        _Caculation_Parameters['_Inv_NMOS_ChannelWidth'] = _CLKoutSamp_And_Inv_NMOS_ChannelWidth
        _Caculation_Parameters['_Inv_NMOS_ChannelLength'] = _CLKoutSamp_And_Inv_NMOS_ChannelLength
                # Pmos
        _Caculation_Parameters['_Inv_PMOS_NumberofGate'] = _CLKoutSamp_And_Inv_PMOS_NumberofGate
        _Caculation_Parameters['_Inv_PMOS_ChannelWidth'] = _CLKoutSamp_And_Inv_PMOS_ChannelWidth
        _Caculation_Parameters['_Inv_PMOS_ChannelLength'] = _CLKoutSamp_And_Inv_PMOS_ChannelLength
                # Body
        _Caculation_Parameters['_Inv_NMOS_Pbody_XvtTop2Pbody'] = Tmp_Sampout_XvtTop2Pbody
        _Caculation_Parameters['_Inv_PMOS_Nbody_Xvtdown2Nbody'] = Tmp_Sampout_Xvtdown2Nbody

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKDout_AND'] = self._SrefElementDeclaration(_DesignObj=D03_03_And_KJH0._And(_DesignParameter=None, _Name='{}:SRF_CLKDout_AND'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKDout_AND']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKDout_AND']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CLKDout_AND']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKDout_AND']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1x = self.get_outter_KJH4('SRF_CLKDout_Inv')
        tmp1y = self.get_param_KJH4('SRF_CLKDout_Inv', 'SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        target_coord = [tmp1x['_Mostright']['coord'][0], tmp1y[0][0][0][0][0]['_XY_up'][1]]
        ## Approaching_coord
        tmp2x = self.get_outter_KJH4('SRF_CLKDout_AND')
        tmp2y = self.get_param_KJH4('SRF_CLKDout_AND', 'SRF_Inverter', 'SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = [tmp2x['_Mostleft']['coord'][0], tmp2y[0][0][0][0][0][0]['_XY_up'][1]]
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKDout_AND')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[0] = Scoord[0] + 126  # Dummy Poly간 최소 거리 DRC: 96 + 폴리 두께
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKDout_AND']['_XYCoordinates'] = tmpXY

        ###########################################################################################################################################################

        ## BND_CLKSrc_CLKDoutANDIn_Hrz_M3
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CLKSrc_CLKDoutANDIn_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CLKSrc_CLKDoutANDIn_Hrz_M3']['_YWidth'] = 50

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_SARLogicWtCLKTree', 'SRF_SARLogic', 'SRF_Thermo_Cnt', 'SRF_Net21_ViaM1M3', 'SRF_ViaM1M2', 'BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_CLKDout_AND', 'SRF_NAND', 'BND_InputB_Vtc_M1')
        self._DesignParameter['BND_CLKSrc_CLKDoutANDIn_Hrz_M3']['_XWidth'] = abs(tmp1[0][0][-1][0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CLKSrc_CLKDoutANDIn_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][-1][0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CLKSrc_CLKDoutANDIn_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CLKSrc_CLKDoutANDIn_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CLKSrc_CLKDoutANDIn_Hrz_M3']['_XYCoordinates'] = tmpXY

        ###########################################################################################################################################################

        # SRF_CLKSrc_CLKDoutANDIn_ViaM3M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKSrc_CLKDoutANDIn_ViaM3M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_CLKSrc_CLKDoutANDIn_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKSrc_CLKDoutANDIn_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKSrc_CLKDoutANDIn_ViaM3M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKSrc_CLKDoutANDIn_ViaM3M4']['_DesignObj']._CalculateDesignParameterXmin( **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKSrc_CLKDoutANDIn_ViaM3M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_CLKSrc_CLKDoutANDIn_Hrz_M3')
        target_coord = tmp1[0][0]['_XY_up_right']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CLKSrc_CLKDoutANDIn_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
        ## Sref coordf
        tmp3 = self.get_param_KJH4('SRF_CLKSrc_CLKDoutANDIn_ViaM3M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKSrc_CLKDoutANDIn_ViaM3M4']['_XYCoordinates'] = tmpXY

        ###########################################################################################################################################################
        ## BND_CLKSrc_CLKDoutInvIn_Vtc_M4
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CLKDoutANDIn_Vtc_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CLKDoutANDIn_Vtc_M4']['_XWidth'] = 50

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_CLKSrc_CLKDoutANDIn_Hrz_M3')
        tmp2 = self.get_param_KJH4('SRF_CLKDout_Inv', 'BND_Input_Vtc_M1')
        self._DesignParameter['BND_CLKDoutANDIn_Vtc_M4']['_YWidth'] = abs(tmp1[0][0]['_XY_up'][1] - tmp2[0][0][0]['_XY_cent'][1])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CLKDoutANDIn_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0]['_XY_up_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CLKDoutANDIn_Vtc_M4')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CLKDoutANDIn_Vtc_M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CLKDoutANDIn_Vtc_M4']['_XYCoordinates'] = tmpXY

        ###########################################################################################################################################################
        # SRF_CLKDoutANDIn_ViaM1M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKDoutANDIn_ViaM1M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_CLKDoutANDIn_ViaM1M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKDoutANDIn_ViaM1M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKDoutANDIn_ViaM1M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKDoutANDIn_ViaM1M4']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKDoutANDIn_ViaM1M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_CLKDoutANDIn_Vtc_M4')
        target_coord = tmp1[0][0]['_XY_down']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CLKDoutANDIn_ViaM1M4', 'SRF_ViaM1M2', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
        ## Sref coordf
        tmp3 = self.get_param_KJH4('SRF_CLKDoutANDIn_ViaM1M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKDoutANDIn_ViaM1M4']['_XYCoordinates'] = tmpXY

        ###########################################################################################################################################################
        #### SRF_CLKSrcInvOut_ViaM2M1
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKSrcInvOut_ViaM1M2'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,_Name='{}:SRF_CLKSrcInvOut_ViaM1M2'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKSrcInvOut_ViaM1M2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKSrcInvOut_ViaM1M2']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKSrcInvOut_ViaM1M2']['_DesignObj']._CalculateDesignParameterYmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKSrcInvOut_ViaM1M2']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('SRF_CLKDout_Inv', 'BND_Out_Vtc_M2')
        target_coord = tmp1[0][0][0]['_XY_right']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CLKSrcInvOut_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKSrcInvOut_ViaM1M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKSrcInvOut_ViaM1M2']['_XYCoordinates'] = tmpXY

        ###########################################################################################################################################################
        ## BND_CLKSrc_CLKDoutInvIn_Hrz_M1
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CLKSrc_CLKDoutInvIn_Hrz_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_CLKSrc_CLKDoutInvIn_Hrz_M1']['_YWidth'] = 50

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_CLKSrcInvOut_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_CLKDout_AND', 'SRF_NAND', 'BND_InputA_Vtc_M1')
        self._DesignParameter['BND_CLKSrc_CLKDoutInvIn_Hrz_M1']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CLKSrc_CLKDoutInvIn_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CLKSrc_CLKDoutInvIn_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CLKSrc_CLKDoutInvIn_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CLKSrc_CLKDoutInvIn_Hrz_M1']['_XYCoordinates'] = tmpXY

        ##########################################################################################################################################################
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_SARLogic_CLK_SrcIn_HrzExten_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_SARLogicWtCLKTree', 'BND_SARLogic_CLK_SrcIn_Hrz_M3')
        self._DesignParameter['BND_SARLogic_CLK_SrcIn_HrzExten_M3']['_YWidth'] = tmp1[0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH4('SRF_CLKDout_Inv', 'BND_Input_Vtc_M1')
        self._DesignParameter['BND_SARLogic_CLK_SrcIn_HrzExten_M3']['_XWidth'] = abs(tmp1[0][0][0]['_XY_right'][0] - tmp2[0][0][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_SARLogic_CLK_SrcIn_HrzExten_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0]['_XY_up_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_SARLogic_CLK_SrcIn_HrzExten_M3')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_SARLogic_CLK_SrcIn_HrzExten_M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_SARLogic_CLK_SrcIn_HrzExten_M3']['_XYCoordinates'] = tmpXY

        ##########################################################################################################################################################
        ## SRF_CLKSrcTreeBufOut_ViaM3M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 3

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKSrcTreeBufOut_ViaM3M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_CLKSrcTreeBufOut_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKSrcTreeBufOut_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKSrcTreeBufOut_ViaM3M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKSrcTreeBufOut_ViaM3M4']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKSrcTreeBufOut_ViaM3M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_SARLogic_CLK_SrcIn_HrzExten_M3')
        target_coord = tmp1[0][0]['_XY_up_right']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CLKSrcTreeBufOut_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKSrcTreeBufOut_ViaM3M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKSrcTreeBufOut_ViaM3M4']['_XYCoordinates'] = tmpXY

        ##########################################################################################################################################################
        ### BND_CLKSrcTreeBufOut_Vtc_M4
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CLKSrcTreeBufOut_Vtc_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKDout_Inv', 'BND_Input_Vtc_M1')
        tmp2 = self.get_param_KJH4('SRF_CLKSrcTreeBufOut_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met3Layer')
        self._DesignParameter['BND_CLKSrcTreeBufOut_Vtc_M4']['_YWidth'] = abs(tmp1[0][0][0]['_XY_cent'][1] - tmp2[0][0][0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CLKSrcTreeBufOut_Vtc_M4']['_XWidth'] = 50

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CLKSrcTreeBufOut_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp2[0][0][0][0]['_XY_up_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CLKSrcTreeBufOut_Vtc_M4')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CLKSrcTreeBufOut_Vtc_M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CLKSrcTreeBufOut_Vtc_M4']['_XYCoordinates'] = tmpXY

        ##########################################################################################################################################################
        ## SRF_CLKDoutInvIn_ViaM1M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKDoutInvIn_ViaM1M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_CLKDoutInvIn_ViaM1M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKDoutInvIn_ViaM1M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKDoutInvIn_ViaM1M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKDoutInvIn_ViaM1M4']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKDoutInvIn_ViaM1M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_CLKSrcTreeBufOut_Vtc_M4')
        target_coord = tmp1[0][0]['_XY_down']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CLKDoutInvIn_ViaM1M4', 'SRF_ViaM1M2', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKDoutInvIn_ViaM1M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKDoutInvIn_ViaM1M4']['_XYCoordinates'] = tmpXY

        ##########################################################################################################################################################
        ## SRF_CLKDoutANDOut_ViaM2M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKDoutANDOut_ViaM2M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_CLKDoutANDOut_ViaM2M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKDoutANDOut_ViaM2M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKDoutANDOut_ViaM2M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKDoutANDOut_ViaM2M4']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKDoutANDOut_ViaM2M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('SRF_CLKDout_AND', 'SRF_Inverter', 'BND_Out_Vtc_M2')
        target_coord = tmp1[0][0][0][0]['_XY_cent']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CLKDoutANDOut_ViaM2M4', 'SRF_ViaM2M3', 'BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKDoutANDOut_ViaM2M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKDoutANDOut_ViaM2M4']['_XYCoordinates'] = tmpXY

        ##########################################################################################################################################################
        ## BND_Nwell Extension on CLKDoutAndInv
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NWellOnCLKDoutANDInv'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKDout_Inv', 'BND_PMOS_NellExten')
        tmp2 = self.get_param_KJH4('SRF_CLKDout_AND', 'SRF_Inverter', 'BND_PMOS_NellExten')
        tmp3 = self.get_param_KJH4('SRF_SARLogicWtCLKTree', 'SRF_SARLogic', 'BND_Nbody_NwellExten')
        tmpUp = max(tmp1[0][0][0]['_XY_up'][1], tmp2[0][0][0][0]['_XY_up'][1], tmp3[0][0][0][0]['_XY_up'][1])
        tmpDn = min(tmp1[0][0][0]['_XY_down'][1], tmp2[0][0][0][0]['_XY_down'][1], tmp3[0][0][0][0]['_XY_down'][1])
        self._DesignParameter['BND_NWellOnCLKDoutANDInv']['_YWidth'] = abs(tmpUp - tmpDn)

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_NWellOnCLKDoutANDInv']['_XWidth'] = abs(tmp2[0][0][0][0]['_XY_right'][0] - tmp3[0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NWellOnCLKDoutANDInv']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = [tmp2[0][0][0][0]['_XY_right'][0], tmpUp]
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NWellOnCLKDoutANDInv')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NWellOnCLKDoutANDInv')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_NWellOnCLKDoutANDInv']['_XYCoordinates'] = tmpXY

        ##########################################################################################################################################################
        ## BND_M1ExtenOn CLKDout AND, Inverter
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NbodyM1ExtenOnCLKDoutANDInv'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKDout_AND', 'SRF_Inverter', 'SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        # tmp2 = self.get_param_KJH4('SRF_CLKDout_Inv','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        tmp3 = self.get_param_KJH4('SRF_SARLogicWtCLKTree', 'SRF_SARLogic', 'BND_Nbody_M1Exten')
        # tmpUp = max(tmp1[0][0][0]['_XY_up'][1], tmp2[0][0][0][0]['_XY_up'][1], tmp3[0][0][0][0]['_XY_up'][1])
        # tmpDn = min(tmp1[0][0][0]['_XY_down'][1], tmp2[0][0][0][0]['_XY_down'][1], tmp3[0][0][0][0]['_XY_down'][1])
        self._DesignParameter['BND_NbodyM1ExtenOnCLKDoutANDInv']['_YWidth'] = tmp1[0][0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_NbodyM1ExtenOnCLKDoutANDInv']['_XWidth'] = abs(tmp1[0][0][0][0][0][0]['_XY_right'][0] - tmp3[0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NbodyM1ExtenOnCLKDoutANDInv']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0][0]['_XY_up_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NbodyM1ExtenOnCLKDoutANDInv')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NbodyM1ExtenOnCLKDoutANDInv')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_NbodyM1ExtenOnCLKDoutANDInv']['_XYCoordinates'] = tmpXY

        ##########################################################################################################################################################
        ## BND_M1ExtenOn CLKDout AND, Inverter (Pbody)
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PbodyM1ExtenOnCLKDoutANDInv'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKDout_AND', 'SRF_Inverter', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_CLKDout_Inv', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        # tmp3 = self.get_param_KJH4('SRF_SARLogicWtCLKTree','SRF_SARLogic','BND_Pbody_M1Exten')
        # tmpUp = max(tmp1[0][0][0]['_XY_up'][1], tmp2[0][0][0][0]['_XY_up'][1], tmp3[0][0][0][0]['_XY_up'][1])
        # tmpDn = min(tmp1[0][0][0]['_XY_down'][1], tmp2[0][0][0][0]['_XY_down'][1], tmp3[0][0][0][0]['_XY_down'][1])
        self._DesignParameter['BND_PbodyM1ExtenOnCLKDoutANDInv']['_YWidth'] = tmp1[0][0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_PbodyM1ExtenOnCLKDoutANDInv']['_XWidth'] = abs(tmp1[0][0][0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PbodyM1ExtenOnCLKDoutANDInv']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0][0]['_XY_up_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PbodyM1ExtenOnCLKDoutANDInv')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PbodyM1ExtenOnCLKDoutANDInv')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_PbodyM1ExtenOnCLKDoutANDInv']['_XYCoordinates'] = tmpXY


        ##########################################################################################################################################################
        ## BND_BPExtenOn CLKDout AND, Inverter (Pbody)
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PbodyBPExtenOnCLKDoutANDInv'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKDout_AND', 'SRF_Inverter', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_CLKDout_Inv', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_PPLayer')
        # tmp3 = self.get_param_KJH4('SRF_SARLogicWtCLKTree','SRF_SARLogic','BND_Pbody_M1Exten')
        # tmpUp = max(tmp1[0][0][0]['_XY_up'][1], tmp2[0][0][0][0]['_XY_up'][1], tmp3[0][0][0][0]['_XY_up'][1])
        # tmpDn = min(tmp1[0][0][0]['_XY_down'][1], tmp2[0][0][0][0]['_XY_down'][1], tmp3[0][0][0][0]['_XY_down'][1])
        self._DesignParameter['BND_PbodyBPExtenOnCLKDoutANDInv']['_YWidth'] = tmp1[0][0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_PbodyBPExtenOnCLKDoutANDInv']['_XWidth'] = abs(tmp1[0][0][0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PbodyBPExtenOnCLKDoutANDInv']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0][0]['_XY_up_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PbodyBPExtenOnCLKDoutANDInv')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PbodyBPExtenOnCLKDoutANDInv')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_PbodyBPExtenOnCLKDoutANDInv']['_XYCoordinates'] = tmpXY

        ##########################################################################################################################################################
        #
        ## BND_PMOSBPExtenOnCLKDoutANDInv for CLKDout AND, Inverter (PMOS)
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOSBPExtenOnCLKDoutANDInv'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKDout_AND', 'SRF_Inverter', 'SRF_PMOS', 'BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_CLKDout_Inv', 'SRF_PMOS', 'BND_PPLayer')
        self._DesignParameter['BND_PMOSBPExtenOnCLKDoutANDInv']['_YWidth'] = tmp1[0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_PMOSBPExtenOnCLKDoutANDInv']['_XWidth'] = abs(tmp1[0][0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOSBPExtenOnCLKDoutANDInv']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0]['_XY_up_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOSBPExtenOnCLKDoutANDInv')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOSBPExtenOnCLKDoutANDInv')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_PMOSBPExtenOnCLKDoutANDInv']['_XYCoordinates'] = tmpXY

        ##########################################################################################################################################################
        ## BND_XVTExtenOn CLKDout AND, Inverter (PMOS)
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOSXVTExtenOnCLKDoutANDInv'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[_CLKoutSamp_XVT][0],
            _Datatype=DesignParameters._LayerMapping[_CLKoutSamp_XVT][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKDout_AND', 'SRF_Inverter', 'SRF_PMOS', 'BND_{}Layer'.format(_CLKoutSamp_XVT))
        tmp2 = self.get_param_KJH4('SRF_CLKDout_Inv', 'SRF_PMOS', 'BND_{}Layer'.format(_CLKoutSamp_XVT))
        self._DesignParameter['BND_PMOSXVTExtenOnCLKDoutANDInv']['_YWidth'] = tmp1[0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_PMOSXVTExtenOnCLKDoutANDInv']['_XWidth'] = abs(tmp1[0][0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOSXVTExtenOnCLKDoutANDInv']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0]['_XY_up_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOSXVTExtenOnCLKDoutANDInv')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOSXVTExtenOnCLKDoutANDInv')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_PMOSXVTExtenOnCLKDoutANDInv']['_XYCoordinates'] = tmpXY

        ##########################################################################################################################################################
        ## BND_XVTExtenOn CLKDout AND, Inverter (NMOS)
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NMOSXVTExtenOnCLKDoutANDInv'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[_CLKoutSamp_XVT][0],
            _Datatype=DesignParameters._LayerMapping[_CLKoutSamp_XVT][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKDout_AND', 'SRF_Inverter', 'SRF_NMOS', 'BND_{}Layer'.format(_CLKoutSamp_XVT))
        tmp2 = self.get_param_KJH4('SRF_CLKDout_Inv', 'SRF_NMOS', 'BND_{}Layer'.format(_CLKoutSamp_XVT))
        self._DesignParameter['BND_NMOSXVTExtenOnCLKDoutANDInv']['_YWidth'] = tmp1[0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_NMOSXVTExtenOnCLKDoutANDInv']['_XWidth'] = abs(tmp1[0][0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NMOSXVTExtenOnCLKDoutANDInv']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0]['_XY_up_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NMOSXVTExtenOnCLKDoutANDInv')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NMOSXVTExtenOnCLKDoutANDInv')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_NMOSXVTExtenOnCLKDoutANDInv']['_XYCoordinates'] = tmpXY

        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')
        SARLogicWtCDACPreDriver_end_time = time.time()
        self.SARLogicWtCDACPreDriver_elapsed_time = SARLogicWtCDACPreDriver_end_time - SARLogicWtCDACPreDRiver_start_time

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ZZ01_K00_02_SARLogicWtCDACPreDriver_Fixed'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'K00_02_SARLogicWtCDACPreDriver_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
_NumofBit = 6,

## SAR Logic
    ## Clock Tree (Driving SAR Logic)
        ## Clock Tree Updward (CLK Source Tree, CLK Samp Tree)
            ## CLK Buffer Unit
                ## Common
                _CLKBufTreeTop_UnitBuf_XVT='SLVT',
                ## Nmos
                _CLKBufTreeTop_UnitBuf_NMOS_NumberofGate=1,  # Number
                _CLKBufTreeTop_UnitBuf_NMOS_ChannelWidth=400,  # Number
                _CLKBufTreeTop_UnitBuf_NMOS_ChannelLength=30,  # Number
                ## Pmos
                _CLKBufTreeTop_UnitBuf_PMOS_NumberofGate=1,  # Number
                _CLKBufTreeTop_UnitBuf_PMOS_ChannelWidth=800,  # Number
                _CLKBufTreeTop_UnitBuf_PMOS_ChannelLength=30,  # Number
                # Height
                _CLKBufTreeTop_UnitBuf_PMOSXvt2NMOSXvt=446,  # number
            ## Clock Buffer Tree structure
            _CLKBufTreeTop_BufTree1and2_NumOfStage=4,  # len[Buf0, Buf1, ... ] 스테이지 수 (아래 버퍼 사이즈 리스트의 길이와 같아야 함.)
            _CLKBufTreeTop_BufTree1_SizeofEachStage=[1, 2, 4, 8],  # CLKSampBuf: [Buf0, Buf1, Buf2 ...]
            _CLKBufTreeTop_BufTree2_SizeofEachStage=[1, 2, 4, 8],  # CLKSrcBuf: [Buf0, Buf1, Buf2 ...]
            _CLKBufTreeTop_XOffSet=0,
        ## Clock Tree Dnward (CLK Source Tree, CLK Samp Tree)
            ## CLK Buffer Unit
                ## Common
                _CLKBufTreeBot_UnitBuf_XVT='SLVT',
                ## Nmos
                _CLKBufTreeBot_UnitBuf_NMOS_NumberofGate=1,  # Number
                _CLKBufTreeBot_UnitBuf_NMOS_ChannelWidth=400,  # Number
                _CLKBufTreeBot_UnitBuf_NMOS_ChannelLength=30,  # Number
                ## Pmos
                _CLKBufTreeBot_UnitBuf_PMOS_NumberofGate=1,  # Number
                _CLKBufTreeBot_UnitBuf_PMOS_ChannelWidth=800,  # Number
                _CLKBufTreeBot_UnitBuf_PMOS_ChannelLength=30,  # Number
                # Height
                _CLKBufTreeBot_UnitBuf_PMOSXvt2NMOSXvt=446,  # number
            ## Clock Buffer Tree structure
            _CLKBufTreeBot_BufTree1and2_NumOfStage=4,  # len[Buf0, Buf1, ... ] 스테이지 수 (아래 버퍼 사이즈 리스트의 길이와 같아야 함.)
            _CLKBufTreeBot_BufTree1_SizeofEachStage=[1, 2, 4, 8],  # CompOutBuf: [Buf0, Buf1, Buf2 ...]
            _CLKBufTreeBot_BufTree2_SizeofEachStage=[1, 2, 4, 8],  # CLKDoutBuf: [Buf0, Buf1, Buf2 ...]
            _CLKBufTreeBot_XOffSet=0,

    ## Clock Spine (Physical demension)
        ## CLK Source: upward, 1st floor
        _YWidthOfCLKSrc=100,
        ## CLK Samp: upward, 2nd floor
        _SpaceBtwCLKSrcAndCLKSamp=100,
        _YWidthOfCLKSamp=100,
        ## Comparator Output: downward, Basement1
        _YWidthOfCompOut=100,
        ## CLK Dout: downward, basement2
        _SpaceBtwCompOutAndCLKDout=100,
        _YWidthOfCLKDout=100,

    ## SetResetDFF
        ## DFF Common
        _Test_distance=320,
        _DFF_PMOSXvt2NMOSXvt    = 1150, # number

        ## Master Xgate1
            ## Xgate common
            _Mst_Xgate1_XVT='SLVT',
            ## Xgate NMOS
            _Mst_Xgate1_NMOS_NumberofGate=1,
            _Mst_Xgate1_NMOS_ChannelWidth=300,
            _Mst_Xgate1_NMOS_ChannelLength=30,
            ## Xgate PMOS
            _Mst_Xgate1_PMOS_NumberofGate=3,
            _Mst_Xgate1_PMOS_ChannelWidth=500,
            _Mst_Xgate1_PMOS_ChannelLength=30,

        ## Master Xgate2
            ## Xgate common
            _Mst_Xgate2_XVT='SLVT',
            ## Xgate NMOS
            _Mst_Xgate2_NMOS_NumberofGate           = 2,
            _Mst_Xgate2_NMOS_ChannelWidth           = 800,
            _Mst_Xgate2_NMOS_ChannelLength          = 30,
            ## Xgate PMOS
            _Mst_Xgate2_PMOS_NumberofGate           = 3,
            _Mst_Xgate2_PMOS_ChannelWidth           = 200,
            _Mst_Xgate2_PMOS_ChannelLength          = 30,

        ## Master Nor1
            ## Nor1 common
            _Mst_Nor1_XVT='SLVT',
            ## NMOS
                ## NMOSA
                _Mst_Nor1_NMOSA_NumberofGate           = 2,
                _Mst_Nor1_NMOSA_ChannelWidth           = 800,
                _Mst_Nor1_NMOSA_ChannelLength          = 30,
                ## NMOSB
                _Mst_Nor1_NMOSB_NumberofGate           = 3,
                _Mst_Nor1_NMOSB_ChannelWidth           = 200,
                _Mst_Nor1_NMOSB_ChannelLength          = 30,
            ## PMOS
                ## PMOSA
                _Mst_Nor1_PMOSA_NumberofGate            = 2,
                _Mst_Nor1_PMOSA_ChannelWidth            = 800,
                _Mst_Nor1_PMOSA_ChannelLength           = 30,
                ## PMOSB
                _Mst_Nor1_PMOSB_NumberofGate            = 3,
                _Mst_Nor1_PMOSB_ChannelWidth            = 200,
                _Mst_Nor1_PMOSB_ChannelLength           = 30,

        ## Master Nor2
            ## Nor2 common
            _Mst_Nor2_XVT='SLVT',
            ## NMOS
                ## NMOSA
                _Mst_Nor2_NMOSA_NumberofGate           = 2,
                _Mst_Nor2_NMOSA_ChannelWidth           = 800,
                _Mst_Nor2_NMOSA_ChannelLength          = 30,
                ## NMOSB
                _Mst_Nor2_NMOSB_NumberofGate           = 3,
                _Mst_Nor2_NMOSB_ChannelWidth           = 200,
                _Mst_Nor2_NMOSB_ChannelLength          = 30,
            ## PMOS
                ## PMOSA
                _Mst_Nor2_PMOSA_NumberofGate            = 2,
                _Mst_Nor2_PMOSA_ChannelWidth            = 800,
                _Mst_Nor2_PMOSA_ChannelLength           = 30,
                ## PMOSB
                _Mst_Nor2_PMOSB_NumberofGate            = 3,
                _Mst_Nor2_PMOSB_ChannelWidth            = 200,
                _Mst_Nor2_PMOSB_ChannelLength           = 30,

        ## Master Inv1 : Set pre-driver
            ## Inv1 common
            _Mst_Inv1_XVT='SLVT',
            ## Inv1 NMOS
            _Mst_Inv1_NMOS_NumberofGate           = 1,
            _Mst_Inv1_NMOS_ChannelWidth           = 300,
            _Mst_Inv1_NMOS_ChannelLength          = 30,
            ## Inv1 PMOS
            _Mst_Inv1_PMOS_NumberofGate           = 3,
            _Mst_Inv1_PMOS_ChannelWidth           = 500,
            _Mst_Inv1_PMOS_ChannelLength          = 30,

        ## Master Inv2 : Set driver
            ## Inv2 common
            _Mst_Inv2_XVT='SLVT',
            ## Inv2 NMOS
            _Mst_Inv2_NMOS_NumberofGate           = 1,
            _Mst_Inv2_NMOS_ChannelWidth           = 300,
            _Mst_Inv2_NMOS_ChannelLength          = 30,
            ## Inv2 PMOS
            _Mst_Inv2_PMOS_NumberofGate           = 3,
            _Mst_Inv2_PMOS_ChannelWidth           = 500,
            _Mst_Inv2_PMOS_ChannelLength          = 30,

        ## Master Inv3 : Clock driver
            ## Inv3 common
            _Mst_Inv3_XVT='SLVT',
            ## Inv3 NMOS
            _Mst_Inv3_NMOS_NumberofGate           = 1,
            _Mst_Inv3_NMOS_ChannelWidth           = 300,
            _Mst_Inv3_NMOS_ChannelLength          = 30,
            ## Inv3 PMOS
            _Mst_Inv3_PMOS_NumberofGate           = 3,
            _Mst_Inv3_PMOS_ChannelWidth           = 500,
            _Mst_Inv3_PMOS_ChannelLength          = 30,

        ## Slave Xgate1
            ## Xgate common
            _Slv_Xgate1_XVT='SLVT',
            ## Xgate NMOS
            _Slv_Xgate1_NMOS_NumberofGate           = 1,
            _Slv_Xgate1_NMOS_ChannelWidth           = 300,
            _Slv_Xgate1_NMOS_ChannelLength          = 30,
            ## Xgate PMOS
            _Slv_Xgate1_PMOS_NumberofGate           = 3,
            _Slv_Xgate1_PMOS_ChannelWidth           = 500,
            _Slv_Xgate1_PMOS_ChannelLength          = 30,

        ## Slave Xgate2
            ## Xgate common
            _Slv_Xgate2_XVT='SLVT',
            ## Xgate NMOS
            _Slv_Xgate2_NMOS_NumberofGate           = 2,
            _Slv_Xgate2_NMOS_ChannelWidth           = 800,
            _Slv_Xgate2_NMOS_ChannelLength          = 30,
            ## Xgate PMOS
            _Slv_Xgate2_PMOS_NumberofGate           = 3,
            _Slv_Xgate2_PMOS_ChannelWidth           = 200,
            _Slv_Xgate2_PMOS_ChannelLength          = 30,

        ## Slave Nor1
            ## Nor1 common
            _Slv_Nor1_XVT='SLVT',
            ## NMOS
                ## NMOSA
                _Slv_Nor1_NMOSA_NumberofGate           = 2,
                _Slv_Nor1_NMOSA_ChannelWidth           = 800,
                _Slv_Nor1_NMOSA_ChannelLength          = 30,
                ## NMOSB
                _Slv_Nor1_NMOSB_NumberofGate           = 3,
                _Slv_Nor1_NMOSB_ChannelWidth           = 200,
                _Slv_Nor1_NMOSB_ChannelLength          = 30,
            ## PMOS
                ## PMOSA
                _Slv_Nor1_PMOSA_NumberofGate            = 2,
                _Slv_Nor1_PMOSA_ChannelWidth            = 800,
                _Slv_Nor1_PMOSA_ChannelLength           = 30,
                ## PMOSB
                _Slv_Nor1_PMOSB_NumberofGate            = 3,
                _Slv_Nor1_PMOSB_ChannelWidth            = 200,
                _Slv_Nor1_PMOSB_ChannelLength           = 30,

        ## Slave Nor2
            ## Nor2 common
            _Slv_Nor2_XVT='SLVT',
            ## NMOS
                ## NMOSA
                _Slv_Nor2_NMOSA_NumberofGate           = 2,
                _Slv_Nor2_NMOSA_ChannelWidth           = 800,
                _Slv_Nor2_NMOSA_ChannelLength          = 30,
                ## NMOSB
                _Slv_Nor2_NMOSB_NumberofGate           = 3,
                _Slv_Nor2_NMOSB_ChannelWidth           = 200,
                _Slv_Nor2_NMOSB_ChannelLength          = 30,
            ## PMOS
                ## PMOSA
                _Slv_Nor2_PMOSA_NumberofGate            = 2,
                _Slv_Nor2_PMOSA_ChannelWidth            = 800,
                _Slv_Nor2_PMOSA_ChannelLength           = 30,
                ## PMOSB
                _Slv_Nor2_PMOSB_NumberofGate            = 3,
                _Slv_Nor2_PMOSB_ChannelWidth            = 200,
                _Slv_Nor2_PMOSB_ChannelLength           = 30,

        ## Slave Inv1 : ReSet pre-driver
            ## Inv1 common
            _Slv_Inv1_XVT='SLVT',
            ## Inv1 NMOS
            _Slv_Inv1_NMOS_NumberofGate           = 1,
            _Slv_Inv1_NMOS_ChannelWidth           = 300,
            _Slv_Inv1_NMOS_ChannelLength          = 30,
            ## Inv1 PMOS
            _Slv_Inv1_PMOS_NumberofGate           = 3,
            _Slv_Inv1_PMOS_ChannelWidth           = 500,
            _Slv_Inv1_PMOS_ChannelLength          = 30,

        ## Slave Inv2 : ReSet driver
            ## Inv2 common
            _Slv_Inv2_XVT='SLVT',
            ## Inv2 NMOS
            _Slv_Inv2_NMOS_NumberofGate           = 1,
            _Slv_Inv2_NMOS_ChannelWidth           = 300,
            _Slv_Inv2_NMOS_ChannelLength          = 30,
            ## Inv2 PMOS
            _Slv_Inv2_PMOS_NumberofGate           = 3,
            _Slv_Inv2_PMOS_ChannelWidth           = 500,
            _Slv_Inv2_PMOS_ChannelLength          = 30,

        ## Slave Inv3 : Qb driver
            ## Inv3 common
            _Slv_Inv3_XVT='SLVT',
            ## Inv3 NMOS
            _Slv_Inv3_NMOS_NumberofGate           = 1,
            _Slv_Inv3_NMOS_ChannelWidth           = 300,
            _Slv_Inv3_NMOS_ChannelLength          = 30,
            ## Inv3 PMOS
            _Slv_Inv3_PMOS_NumberofGate           = 3,
            _Slv_Inv3_PMOS_ChannelWidth           = 500,
            _Slv_Inv3_PMOS_ChannelLength          = 30,

## DAC PreDriver
    ## Inverter Chain
        ## InvChain Common
        _DACPreDrv_PMOSXvt2NMOSXvt=500,  # number
        ## Inverter Chain
            ## Inv1 common
        _DACPreDrv_NumberofGate=[[1, 2, 4, 8], [1, 2, 4, 8], [1, 2, 4, 8], [2, 2, 2, 2, 2], [1, 2, 4, 8], [8, 16, 8, 8],],  # Vector
        _DACPreDrv_ChannelLength=30,  # Scalar
        _DACPreDrv_XVT='SLVT',  # 'SLVT'
            ## Inv1 NMOS
        _DACPreDrv_Inv_NMOS_ChannelWidth=400,  # Scalar
            ## Inv1 PMOS
        _DACPreDrv_Inv_PMOS_ChannelWidth=800,  # Scalar

## CLKOutSamp(!=ClkSamp)
    ## Common
        # XVT
        _CLKoutSamp_XVT = 'SLVT',
        # Height
        #_CLKOutSamp_PMOSXvt2NMOSXvt=1800,  # number
    ## Inverter
        # Nmos
        _CLKoutSamp_Inv_NMOS_NumberofGate=1,  # Number
        _CLKoutSamp_Inv_NMOS_ChannelWidth=100,  # Number
        _CLKoutSamp_Inv_NMOS_ChannelLength=30,  # Number
        # Pmos
        _CLKoutSamp_Inv_PMOS_NumberofGate=1,  # Number
        _CLKoutSamp_Inv_PMOS_ChannelWidth=100,  # Number
        _CLKoutSamp_Inv_PMOS_ChannelLength=30,  # Number
    ## AND
        ## AND Common
        ## Nand
            # NmosA
            _CLKoutSamp_And_Nand_NMOSA_NumberofGate=1,  # Number
            _CLKoutSamp_And_Nand_NMOSA_ChannelWidth=100,  # Number
            _CLKoutSamp_And_Nand_NMOSA_ChannelLength=30,  # Number
            # NMOSB
            _CLKoutSamp_And_Nand_NMOSB_NumberofGate=2,  # Number
            _CLKoutSamp_And_Nand_NMOSB_ChannelWidth=750,  # Number
            _CLKoutSamp_And_Nand_NMOSB_ChannelLength=30,  # Number
            # PMOSA
            _CLKoutSamp_And_Nand_PMOSA_NumberofGate=1,  # Number
            _CLKoutSamp_And_Nand_PMOSA_ChannelWidth=300,  # Number
            _CLKoutSamp_And_Nand_PMOSA_ChannelLength=30,  # Number
            # PMOSB
            _CLKoutSamp_And_Nand_PMOSB_NumberofGate=3,  # Number
            _CLKoutSamp_And_Nand_PMOSB_ChannelWidth=750,  # Number
            _CLKoutSamp_And_Nand_PMOSB_ChannelLength=30,  # Number
        ## Inverter
            # Nmos
            _CLKoutSamp_And_Inv_NMOS_NumberofGate=1,  # Number
            _CLKoutSamp_And_Inv_NMOS_ChannelWidth=100,  # Number
            _CLKoutSamp_And_Inv_NMOS_ChannelLength=30,  # Number
            # Pmos
            _CLKoutSamp_And_Inv_PMOS_NumberofGate=1,  # Number
            _CLKoutSamp_And_Inv_PMOS_ChannelWidth=200,  # Number
            _CLKoutSamp_And_Inv_PMOS_ChannelLength=30,  # Number


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
    LayoutObj = _SARLogicWtCDACPreDriver(_DesignParameter=None, _Name=cellname)
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
