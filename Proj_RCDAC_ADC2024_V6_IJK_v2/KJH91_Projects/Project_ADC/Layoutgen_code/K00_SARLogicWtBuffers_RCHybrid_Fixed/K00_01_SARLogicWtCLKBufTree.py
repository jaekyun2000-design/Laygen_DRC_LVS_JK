## Import Basic Modules
    ## Engine
#from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import StickDiagram
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
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block           import A02_ViaStack_KJH3

from KJH91_Projects.Project_ADC.Layoutgen_code.K00_SARLogicWtBuffers_RCHybrid_Fixed   import K00_00_SARLogic_KJH1_v2
from KJH91_Projects.Project_ADC.Layoutgen_code.F00_CLKBufferTree_Fixed            import F00_02_CLKBufferTree_v3


## Define Class
class _SARLogicWtCLKBufTree(StickDiagram_KJH1._StickDiagram_KJH):
    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
        ## SAR Logic
        _NumofBit=5,
        ## Clock Tree
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
        _DFF_PMOSXvt2NMOSXvt=1150,  # number

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
        _Mst_Xgate2_NMOS_NumberofGate=2,
        _Mst_Xgate2_NMOS_ChannelWidth=800,
        _Mst_Xgate2_NMOS_ChannelLength=30,
        ## Xgate PMOS
        _Mst_Xgate2_PMOS_NumberofGate=3,
        _Mst_Xgate2_PMOS_ChannelWidth=200,
        _Mst_Xgate2_PMOS_ChannelLength=30,

        ## Master Nor1
        ## Nor1 common
        _Mst_Nor1_XVT='SLVT',
        ## NMOS
        ## NMOSA
        _Mst_Nor1_NMOSA_NumberofGate=2,
        _Mst_Nor1_NMOSA_ChannelWidth=800,
        _Mst_Nor1_NMOSA_ChannelLength=30,
        ## NMOSB
        _Mst_Nor1_NMOSB_NumberofGate=3,
        _Mst_Nor1_NMOSB_ChannelWidth=200,
        _Mst_Nor1_NMOSB_ChannelLength=30,
        ## PMOS
        ## PMOSA
        _Mst_Nor1_PMOSA_NumberofGate=2,
        _Mst_Nor1_PMOSA_ChannelWidth=800,
        _Mst_Nor1_PMOSA_ChannelLength=30,
        ## PMOSB
        _Mst_Nor1_PMOSB_NumberofGate=3,
        _Mst_Nor1_PMOSB_ChannelWidth=200,
        _Mst_Nor1_PMOSB_ChannelLength=30,

        ## Master Nor2
        ## Nor2 common
        _Mst_Nor2_XVT='SLVT',
        ## NMOS
        ## NMOSA
        _Mst_Nor2_NMOSA_NumberofGate=2,
        _Mst_Nor2_NMOSA_ChannelWidth=800,
        _Mst_Nor2_NMOSA_ChannelLength=30,
        ## NMOSB
        _Mst_Nor2_NMOSB_NumberofGate=3,
        _Mst_Nor2_NMOSB_ChannelWidth=200,
        _Mst_Nor2_NMOSB_ChannelLength=30,
        ## PMOS
        ## PMOSA
        _Mst_Nor2_PMOSA_NumberofGate=2,
        _Mst_Nor2_PMOSA_ChannelWidth=800,
        _Mst_Nor2_PMOSA_ChannelLength=30,
        ## PMOSB
        _Mst_Nor2_PMOSB_NumberofGate=3,
        _Mst_Nor2_PMOSB_ChannelWidth=200,
        _Mst_Nor2_PMOSB_ChannelLength=30,

        ## Master Inv1 : Set pre-driver
        ## Inv1 common
        _Mst_Inv1_XVT='SLVT',
        ## Inv1 NMOS
        _Mst_Inv1_NMOS_NumberofGate=1,
        _Mst_Inv1_NMOS_ChannelWidth=300,
        _Mst_Inv1_NMOS_ChannelLength=30,
        ## Inv1 PMOS
        _Mst_Inv1_PMOS_NumberofGate=3,
        _Mst_Inv1_PMOS_ChannelWidth=500,
        _Mst_Inv1_PMOS_ChannelLength=30,

        ## Master Inv2 : Set driver
        ## Inv2 common
        _Mst_Inv2_XVT='SLVT',
        ## Inv2 NMOS
        _Mst_Inv2_NMOS_NumberofGate=1,
        _Mst_Inv2_NMOS_ChannelWidth=300,
        _Mst_Inv2_NMOS_ChannelLength=30,
        ## Inv2 PMOS
        _Mst_Inv2_PMOS_NumberofGate=3,
        _Mst_Inv2_PMOS_ChannelWidth=500,
        _Mst_Inv2_PMOS_ChannelLength=30,

        ## Master Inv3 : Clock driver
        ## Inv3 common
        _Mst_Inv3_XVT='SLVT',
        ## Inv3 NMOS
        _Mst_Inv3_NMOS_NumberofGate=1,
        _Mst_Inv3_NMOS_ChannelWidth=300,
        _Mst_Inv3_NMOS_ChannelLength=30,
        ## Inv3 PMOS
        _Mst_Inv3_PMOS_NumberofGate=3,
        _Mst_Inv3_PMOS_ChannelWidth=500,
        _Mst_Inv3_PMOS_ChannelLength=30,

        ## Slave Xgate1
        ## Xgate common
        _Slv_Xgate1_XVT='SLVT',
        ## Xgate NMOS
        _Slv_Xgate1_NMOS_NumberofGate=1,
        _Slv_Xgate1_NMOS_ChannelWidth=300,
        _Slv_Xgate1_NMOS_ChannelLength=30,
        ## Xgate PMOS
        _Slv_Xgate1_PMOS_NumberofGate=3,
        _Slv_Xgate1_PMOS_ChannelWidth=500,
        _Slv_Xgate1_PMOS_ChannelLength=30,

        ## Slave Xgate2
        ## Xgate common
        _Slv_Xgate2_XVT='SLVT',
        ## Xgate NMOS
        _Slv_Xgate2_NMOS_NumberofGate=2,
        _Slv_Xgate2_NMOS_ChannelWidth=800,
        _Slv_Xgate2_NMOS_ChannelLength=30,
        ## Xgate PMOS
        _Slv_Xgate2_PMOS_NumberofGate=3,
        _Slv_Xgate2_PMOS_ChannelWidth=200,
        _Slv_Xgate2_PMOS_ChannelLength=30,

        ## Slave Nor1
        ## Nor1 common
        _Slv_Nor1_XVT='SLVT',
        ## NMOS
        ## NMOSA
        _Slv_Nor1_NMOSA_NumberofGate=2,
        _Slv_Nor1_NMOSA_ChannelWidth=800,
        _Slv_Nor1_NMOSA_ChannelLength=30,
        ## NMOSB
        _Slv_Nor1_NMOSB_NumberofGate=3,
        _Slv_Nor1_NMOSB_ChannelWidth=200,
        _Slv_Nor1_NMOSB_ChannelLength=30,
        ## PMOS
        ## PMOSA
        _Slv_Nor1_PMOSA_NumberofGate=2,
        _Slv_Nor1_PMOSA_ChannelWidth=800,
        _Slv_Nor1_PMOSA_ChannelLength=30,
        ## PMOSB
        _Slv_Nor1_PMOSB_NumberofGate=3,
        _Slv_Nor1_PMOSB_ChannelWidth=200,
        _Slv_Nor1_PMOSB_ChannelLength=30,

        ## Slave Nor2
        ## Nor2 common
        _Slv_Nor2_XVT='SLVT',
        ## NMOS
        ## NMOSA
        _Slv_Nor2_NMOSA_NumberofGate=2,
        _Slv_Nor2_NMOSA_ChannelWidth=800,
        _Slv_Nor2_NMOSA_ChannelLength=30,
        ## NMOSB
        _Slv_Nor2_NMOSB_NumberofGate=3,
        _Slv_Nor2_NMOSB_ChannelWidth=200,
        _Slv_Nor2_NMOSB_ChannelLength=30,
        ## PMOS
        ## PMOSA
        _Slv_Nor2_PMOSA_NumberofGate=2,
        _Slv_Nor2_PMOSA_ChannelWidth=800,
        _Slv_Nor2_PMOSA_ChannelLength=30,
        ## PMOSB
        _Slv_Nor2_PMOSB_NumberofGate=3,
        _Slv_Nor2_PMOSB_ChannelWidth=200,
        _Slv_Nor2_PMOSB_ChannelLength=30,

        ## Slave Inv1 : ReSet pre-driver
        ## Inv1 common
        _Slv_Inv1_XVT='SLVT',
        ## Inv1 NMOS
        _Slv_Inv1_NMOS_NumberofGate=1,
        _Slv_Inv1_NMOS_ChannelWidth=300,
        _Slv_Inv1_NMOS_ChannelLength=30,
        ## Inv1 PMOS
        _Slv_Inv1_PMOS_NumberofGate=3,
        _Slv_Inv1_PMOS_ChannelWidth=500,
        _Slv_Inv1_PMOS_ChannelLength=30,

        ## Slave Inv2 : ReSet driver
        ## Inv2 common
        _Slv_Inv2_XVT='SLVT',
        ## Inv2 NMOS
        _Slv_Inv2_NMOS_NumberofGate=1,
        _Slv_Inv2_NMOS_ChannelWidth=300,
        _Slv_Inv2_NMOS_ChannelLength=30,
        ## Inv2 PMOS
        _Slv_Inv2_PMOS_NumberofGate=3,
        _Slv_Inv2_PMOS_ChannelWidth=500,
        _Slv_Inv2_PMOS_ChannelLength=30,

        ## Slave Inv3 : Qb driver
        ## Inv3 common
        _Slv_Inv3_XVT='SLVT',
        ## Inv3 NMOS
        _Slv_Inv3_NMOS_NumberofGate=1,
        _Slv_Inv3_NMOS_ChannelWidth=300,
        _Slv_Inv3_NMOS_ChannelLength=30,
        ## Inv3 PMOS
        _Slv_Inv3_PMOS_NumberofGate=3,
        _Slv_Inv3_PMOS_ChannelWidth=500,
        _Slv_Inv3_PMOS_ChannelLength=30,

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
        ## SAR Logic
        _NumofBit=5,
        ## Clock Tree
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
        _DFF_PMOSXvt2NMOSXvt=1150,  # number

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
        _Mst_Xgate2_NMOS_NumberofGate=2,
        _Mst_Xgate2_NMOS_ChannelWidth=800,
        _Mst_Xgate2_NMOS_ChannelLength=30,
        ## Xgate PMOS
        _Mst_Xgate2_PMOS_NumberofGate=3,
        _Mst_Xgate2_PMOS_ChannelWidth=200,
        _Mst_Xgate2_PMOS_ChannelLength=30,

        ## Master Nor1
        ## Nor1 common
        _Mst_Nor1_XVT='SLVT',
        ## NMOS
        ## NMOSA
        _Mst_Nor1_NMOSA_NumberofGate=2,
        _Mst_Nor1_NMOSA_ChannelWidth=800,
        _Mst_Nor1_NMOSA_ChannelLength=30,
        ## NMOSB
        _Mst_Nor1_NMOSB_NumberofGate=3,
        _Mst_Nor1_NMOSB_ChannelWidth=200,
        _Mst_Nor1_NMOSB_ChannelLength=30,
        ## PMOS
        ## PMOSA
        _Mst_Nor1_PMOSA_NumberofGate=2,
        _Mst_Nor1_PMOSA_ChannelWidth=800,
        _Mst_Nor1_PMOSA_ChannelLength=30,
        ## PMOSB
        _Mst_Nor1_PMOSB_NumberofGate=3,
        _Mst_Nor1_PMOSB_ChannelWidth=200,
        _Mst_Nor1_PMOSB_ChannelLength=30,

        ## Master Nor2
        ## Nor2 common
        _Mst_Nor2_XVT='SLVT',
        ## NMOS
        ## NMOSA
        _Mst_Nor2_NMOSA_NumberofGate=2,
        _Mst_Nor2_NMOSA_ChannelWidth=800,
        _Mst_Nor2_NMOSA_ChannelLength=30,
        ## NMOSB
        _Mst_Nor2_NMOSB_NumberofGate=3,
        _Mst_Nor2_NMOSB_ChannelWidth=200,
        _Mst_Nor2_NMOSB_ChannelLength=30,
        ## PMOS
        ## PMOSA
        _Mst_Nor2_PMOSA_NumberofGate=2,
        _Mst_Nor2_PMOSA_ChannelWidth=800,
        _Mst_Nor2_PMOSA_ChannelLength=30,
        ## PMOSB
        _Mst_Nor2_PMOSB_NumberofGate=3,
        _Mst_Nor2_PMOSB_ChannelWidth=200,
        _Mst_Nor2_PMOSB_ChannelLength=30,

        ## Master Inv1 : Set pre-driver
        ## Inv1 common
        _Mst_Inv1_XVT='SLVT',
        ## Inv1 NMOS
        _Mst_Inv1_NMOS_NumberofGate=1,
        _Mst_Inv1_NMOS_ChannelWidth=300,
        _Mst_Inv1_NMOS_ChannelLength=30,
        ## Inv1 PMOS
        _Mst_Inv1_PMOS_NumberofGate=3,
        _Mst_Inv1_PMOS_ChannelWidth=500,
        _Mst_Inv1_PMOS_ChannelLength=30,

        ## Master Inv2 : Set driver
        ## Inv2 common
        _Mst_Inv2_XVT='SLVT',
        ## Inv2 NMOS
        _Mst_Inv2_NMOS_NumberofGate=1,
        _Mst_Inv2_NMOS_ChannelWidth=300,
        _Mst_Inv2_NMOS_ChannelLength=30,
        ## Inv2 PMOS
        _Mst_Inv2_PMOS_NumberofGate=3,
        _Mst_Inv2_PMOS_ChannelWidth=500,
        _Mst_Inv2_PMOS_ChannelLength=30,

        ## Master Inv3 : Clock driver
        ## Inv3 common
        _Mst_Inv3_XVT='SLVT',
        ## Inv3 NMOS
        _Mst_Inv3_NMOS_NumberofGate=1,
        _Mst_Inv3_NMOS_ChannelWidth=300,
        _Mst_Inv3_NMOS_ChannelLength=30,
        ## Inv3 PMOS
        _Mst_Inv3_PMOS_NumberofGate=3,
        _Mst_Inv3_PMOS_ChannelWidth=500,
        _Mst_Inv3_PMOS_ChannelLength=30,

        ## Slave Xgate1
        ## Xgate common
        _Slv_Xgate1_XVT='SLVT',
        ## Xgate NMOS
        _Slv_Xgate1_NMOS_NumberofGate=1,
        _Slv_Xgate1_NMOS_ChannelWidth=300,
        _Slv_Xgate1_NMOS_ChannelLength=30,
        ## Xgate PMOS
        _Slv_Xgate1_PMOS_NumberofGate=3,
        _Slv_Xgate1_PMOS_ChannelWidth=500,
        _Slv_Xgate1_PMOS_ChannelLength=30,

        ## Slave Xgate2
        ## Xgate common
        _Slv_Xgate2_XVT='SLVT',
        ## Xgate NMOS
        _Slv_Xgate2_NMOS_NumberofGate=2,
        _Slv_Xgate2_NMOS_ChannelWidth=800,
        _Slv_Xgate2_NMOS_ChannelLength=30,
        ## Xgate PMOS
        _Slv_Xgate2_PMOS_NumberofGate=3,
        _Slv_Xgate2_PMOS_ChannelWidth=200,
        _Slv_Xgate2_PMOS_ChannelLength=30,

        ## Slave Nor1
        ## Nor1 common
        _Slv_Nor1_XVT='SLVT',
        ## NMOS
        ## NMOSA
        _Slv_Nor1_NMOSA_NumberofGate=2,
        _Slv_Nor1_NMOSA_ChannelWidth=800,
        _Slv_Nor1_NMOSA_ChannelLength=30,
        ## NMOSB
        _Slv_Nor1_NMOSB_NumberofGate=3,
        _Slv_Nor1_NMOSB_ChannelWidth=200,
        _Slv_Nor1_NMOSB_ChannelLength=30,
        ## PMOS
        ## PMOSA
        _Slv_Nor1_PMOSA_NumberofGate=2,
        _Slv_Nor1_PMOSA_ChannelWidth=800,
        _Slv_Nor1_PMOSA_ChannelLength=30,
        ## PMOSB
        _Slv_Nor1_PMOSB_NumberofGate=3,
        _Slv_Nor1_PMOSB_ChannelWidth=200,
        _Slv_Nor1_PMOSB_ChannelLength=30,

        ## Slave Nor2
        ## Nor2 common
        _Slv_Nor2_XVT='SLVT',
        ## NMOS
        ## NMOSA
        _Slv_Nor2_NMOSA_NumberofGate=2,
        _Slv_Nor2_NMOSA_ChannelWidth=800,
        _Slv_Nor2_NMOSA_ChannelLength=30,
        ## NMOSB
        _Slv_Nor2_NMOSB_NumberofGate=3,
        _Slv_Nor2_NMOSB_ChannelWidth=200,
        _Slv_Nor2_NMOSB_ChannelLength=30,
        ## PMOS
        ## PMOSA
        _Slv_Nor2_PMOSA_NumberofGate=2,
        _Slv_Nor2_PMOSA_ChannelWidth=800,
        _Slv_Nor2_PMOSA_ChannelLength=30,
        ## PMOSB
        _Slv_Nor2_PMOSB_NumberofGate=3,
        _Slv_Nor2_PMOSB_ChannelWidth=200,
        _Slv_Nor2_PMOSB_ChannelLength=30,

        ## Slave Inv1 : ReSet pre-driver
        ## Inv1 common
        _Slv_Inv1_XVT='SLVT',
        ## Inv1 NMOS
        _Slv_Inv1_NMOS_NumberofGate=1,
        _Slv_Inv1_NMOS_ChannelWidth=300,
        _Slv_Inv1_NMOS_ChannelLength=30,
        ## Inv1 PMOS
        _Slv_Inv1_PMOS_NumberofGate=3,
        _Slv_Inv1_PMOS_ChannelWidth=500,
        _Slv_Inv1_PMOS_ChannelLength=30,

        ## Slave Inv2 : ReSet driver
        ## Inv2 common
        _Slv_Inv2_XVT='SLVT',
        ## Inv2 NMOS
        _Slv_Inv2_NMOS_NumberofGate=1,
        _Slv_Inv2_NMOS_ChannelWidth=300,
        _Slv_Inv2_NMOS_ChannelLength=30,
        ## Inv2 PMOS
        _Slv_Inv2_PMOS_NumberofGate=3,
        _Slv_Inv2_PMOS_ChannelWidth=500,
        _Slv_Inv2_PMOS_ChannelLength=30,

        ## Slave Inv3 : Qb driver
        ## Inv3 common
        _Slv_Inv3_XVT='SLVT',
        ## Inv3 NMOS
        _Slv_Inv3_NMOS_NumberofGate=1,
        _Slv_Inv3_NMOS_ChannelWidth=300,
        _Slv_Inv3_NMOS_ChannelLength=30,
        ## Inv3 PMOS
        _Slv_Inv3_PMOS_NumberofGate=3,
        _Slv_Inv3_PMOS_ChannelWidth=500,
        _Slv_Inv3_PMOS_ChannelLength=30,

                                  ):

        ## Class_HEADER: Pre Defined Parameter Before Calculation
        ## Load DRC library
        _DRCobj = DRC.DRC()
        ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ## CALCULATION START
        start_time = time.time()
        # end_time = time.time()
        # self.elapsed_time = end_time - start_time
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

        ####### Revision1: 기존(Logic gen --> buf1,2 --> Logic regen) , 변경(Buf1,2 gen --> Logic gen --> buf1,2 regen)
        ####### Top CLK Buffer Tree2 SRF Generation: Fake Generation to get _SpaceBtwPbodyAndCLKSrc and _SpaceBtwNbody2AndCompOut
        PbodyXWidthSARLogic = 100000 # any number ok

        _Caculation_Parameters = copy.deepcopy(F00_02_CLKBufferTree_v3._CLKBufferTree._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_UnitBuf_XVT'] = _CLKBufTreeTop_UnitBuf_XVT

        _Caculation_Parameters['_UnitBuf_NMOS_NumberofGate'] = _CLKBufTreeTop_UnitBuf_NMOS_NumberofGate
        _Caculation_Parameters['_UnitBuf_NMOS_ChannelWidth'] = _CLKBufTreeTop_UnitBuf_NMOS_ChannelWidth
        _Caculation_Parameters['_UnitBuf_NMOS_ChannelLength'] = _CLKBufTreeTop_UnitBuf_NMOS_ChannelLength

        _Caculation_Parameters['_UnitBuf_PMOS_NumberofGate'] = _CLKBufTreeTop_UnitBuf_PMOS_NumberofGate
        _Caculation_Parameters['_UnitBuf_PMOS_ChannelWidth'] = _CLKBufTreeTop_UnitBuf_PMOS_ChannelWidth
        _Caculation_Parameters['_UnitBuf_PMOS_ChannelLength'] = _CLKBufTreeTop_UnitBuf_PMOS_ChannelLength

        _Caculation_Parameters['_UnitBuf_PMOSXvt2NMOSXvt'] = _CLKBufTreeTop_UnitBuf_PMOSXvt2NMOSXvt

        _Caculation_Parameters['_BufTree_TotalLength']      = PbodyXWidthSARLogic
        _Caculation_Parameters['_BufTree1and2_NumOfStage']  = _CLKBufTreeTop_BufTree1and2_NumOfStage
        _Caculation_Parameters['_BufTree1_SizeofEachStage'] = _CLKBufTreeTop_BufTree1_SizeofEachStage
        _Caculation_Parameters['_BufTree2_SizeofEachStage'] = _CLKBufTreeTop_BufTree2_SizeofEachStage
        _Caculation_Parameters['_BufTree_OutputPlacement']  = 'Dn'
        _Caculation_Parameters['_BufTree_OutputVia']        = None

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_CLKBufferTree_Top'] = self._SrefElementDeclaration(_DesignObj=F00_02_CLKBufferTree_v3._CLKBufferTree(_DesignParameter=None,_Name='{}:SRF_CLKBufferTree_Top'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_CLKBufferTree_Top']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CLKBufferTree_Top']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CLKBufferTree_Top']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKBufferTree_Top']['_XYCoordinates'] = [[0, 0]]





        ####### Bot CLK Buffer Tree2 SRF Generation : Fake generation to get _SpaceBtwPbodyAndCLKSrc and _SpaceBtwNbody2AndCompOut
        # PbodyXWidthSARLogic = 1000000 # Any number

        _Caculation_Parameters = copy.deepcopy(F00_02_CLKBufferTree_v3._CLKBufferTree._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_UnitBuf_XVT'] = _CLKBufTreeBot_UnitBuf_XVT

        _Caculation_Parameters['_UnitBuf_NMOS_NumberofGate'] = _CLKBufTreeBot_UnitBuf_NMOS_NumberofGate
        _Caculation_Parameters['_UnitBuf_NMOS_ChannelWidth'] = _CLKBufTreeBot_UnitBuf_NMOS_ChannelWidth
        _Caculation_Parameters['_UnitBuf_NMOS_ChannelLength'] = _CLKBufTreeBot_UnitBuf_NMOS_ChannelLength

        _Caculation_Parameters['_UnitBuf_PMOS_NumberofGate'] = _CLKBufTreeBot_UnitBuf_PMOS_NumberofGate
        _Caculation_Parameters['_UnitBuf_PMOS_ChannelWidth'] = _CLKBufTreeBot_UnitBuf_PMOS_ChannelWidth
        _Caculation_Parameters['_UnitBuf_PMOS_ChannelLength'] = _CLKBufTreeBot_UnitBuf_PMOS_ChannelLength

        _Caculation_Parameters['_UnitBuf_PMOSXvt2NMOSXvt'] = _CLKBufTreeBot_UnitBuf_PMOSXvt2NMOSXvt

        _Caculation_Parameters['_BufTree_TotalLength']      = PbodyXWidthSARLogic
        _Caculation_Parameters['_BufTree1and2_NumOfStage']  = _CLKBufTreeBot_BufTree1and2_NumOfStage
        _Caculation_Parameters['_BufTree1_SizeofEachStage'] = _CLKBufTreeBot_BufTree1_SizeofEachStage
        _Caculation_Parameters['_BufTree2_SizeofEachStage'] = _CLKBufTreeBot_BufTree2_SizeofEachStage
        _Caculation_Parameters['_BufTree_OutputPlacement']  = 'Up'
        _Caculation_Parameters['_BufTree_OutputVia']        = None

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_CLKBufferTree_Bot'] = self._SrefElementDeclaration(_DesignObj=F00_02_CLKBufferTree_v3._CLKBufferTree(_DesignParameter=None,_Name='{}:SRF_CLKBufferTree_Bot'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_CLKBufferTree_Bot']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CLKBufferTree_Bot']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CLKBufferTree_Bot']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKBufferTree_Bot']['_XYCoordinates'] = [[0, 0]]




        ### Calculate _SpaceBtwPbodyAndCLKSrc and _SpaceBtwNbody2AndCompOut
        ### routing rules CLK Buf
        LowerMetLayer = 3
        UpperMetLayer = 5
        SpaceBtwCLKSampAndCLKBufInternalPath = 100
        SpaceBtwCLKDoutAndCLKBufInternalPath = 100
        tmp1 = self.get_param_KJH4('SRF_CLKBufferTree_Top', 'BND_Pbody_M1')
        tmp2 = self.get_param_KJH4('SRF_CLKBufferTree_Top', 'BND_Buf{}Stg{}to{}_Hrz_M{}'.format(1, 2, 1, LowerMetLayer))
        _SpaceBtwPbodyAndCLKSrc = abs(tmp1[0][0][0]['_XY_up'][1] - tmp2[0][0][0]['_XY_down'][1]) - _YWidthOfCLKSrc - _SpaceBtwCLKSrcAndCLKSamp - _YWidthOfCLKSamp - SpaceBtwCLKSampAndCLKBufInternalPath

        tmp1 = self.get_param_KJH4('SRF_CLKBufferTree_Bot', 'BND_Nbody_M1')
        tmp2 = self.get_param_KJH4('SRF_CLKBufferTree_Bot', 'BND_Buf{}Stg{}to{}_Hrz_M{}'.format(2, 2, 1, LowerMetLayer))
        _SpaceBtwNbody2AndCompOut = abs(tmp1[0][0][0]['_XY_down'][1] - tmp2[0][0][0]['_XY_up'][1]) - _YWidthOfCompOut - _SpaceBtwCompOutAndCLKDout - _YWidthOfCLKDout - SpaceBtwCLKDoutAndCLKBufInternalPath





        ####### SAR LOGIC SRF Generation: use pre-cal information of _SpaceBtwPbodyAndCLKSrc/_SpaceBtwNbody2AndCompOut
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(K00_00_SARLogic_KJH1_v2._SARLogic._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters1['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NumofBit'] = _NumofBit

        _Caculation_Parameters['_SpaceBtwPbodyAndCLKSrc'] = _SpaceBtwPbodyAndCLKSrc
        _Caculation_Parameters['_YWidthOfCLKSrc'] = _YWidthOfCLKSrc
        _Caculation_Parameters['_SpaceBtwCLKSrcAndCLKSamp'] = _SpaceBtwCLKSrcAndCLKSamp
        _Caculation_Parameters['_YWidthOfCLKSamp'] = _YWidthOfCLKSamp
        _Caculation_Parameters['_SpaceBtwNbody2AndCompOut'] = _SpaceBtwNbody2AndCompOut
        _Caculation_Parameters['_YWidthOfCompOut'] = _YWidthOfCompOut
        _Caculation_Parameters['_SpaceBtwCompOutAndCLKDout'] = _SpaceBtwCompOutAndCLKDout
        _Caculation_Parameters['_YWidthOfCLKDout'] = _YWidthOfCLKDout

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


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## DAC Controller Gen.
        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_SARLogic'] = self._SrefElementDeclaration(_DesignObj=K00_00_SARLogic_KJH1_v2._SARLogic(_DesignParameter=None, _Name='{}:SRF_SARLogic'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_SARLogic']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SARLogic']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SARLogic']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SARLogic']['_XYCoordinates'] = [[0, 0]]

        ## Pre_Calculated Value 4 generate CLK Buffers
        tmp1 = self.get_param_KJH4('SRF_SARLogic', 'BND_Pbody_M1Exten')
        PbodyXWidthSARLogic = tmp1[0][0][0]['_Xwidth']

        ####### Deletion before real generation
        del (self._DesignParameter['SRF_CLKBufferTree_Top'])
        del (self._DesignParameter['SRF_CLKBufferTree_Bot'])

        ####### Top CLK Buffer Tree2 SRF Generation: Fake Generation to get _SpaceBtwPbodyAndCLKSrc and _SpaceBtwNbody2AndCompOut
        _Caculation_Parameters = copy.deepcopy(F00_02_CLKBufferTree_v3._CLKBufferTree._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_UnitBuf_XVT'] = _CLKBufTreeTop_UnitBuf_XVT

        _Caculation_Parameters['_UnitBuf_NMOS_NumberofGate'] = _CLKBufTreeTop_UnitBuf_NMOS_NumberofGate
        _Caculation_Parameters['_UnitBuf_NMOS_ChannelWidth'] = _CLKBufTreeTop_UnitBuf_NMOS_ChannelWidth
        _Caculation_Parameters['_UnitBuf_NMOS_ChannelLength'] = _CLKBufTreeTop_UnitBuf_NMOS_ChannelLength

        _Caculation_Parameters['_UnitBuf_PMOS_NumberofGate'] = _CLKBufTreeTop_UnitBuf_PMOS_NumberofGate
        _Caculation_Parameters['_UnitBuf_PMOS_ChannelWidth'] = _CLKBufTreeTop_UnitBuf_PMOS_ChannelWidth
        _Caculation_Parameters['_UnitBuf_PMOS_ChannelLength'] = _CLKBufTreeTop_UnitBuf_PMOS_ChannelLength

        _Caculation_Parameters['_UnitBuf_PMOSXvt2NMOSXvt'] = _CLKBufTreeTop_UnitBuf_PMOSXvt2NMOSXvt

        _Caculation_Parameters['_BufTree_TotalLength'] = PbodyXWidthSARLogic
        _Caculation_Parameters['_BufTree1and2_NumOfStage'] = _CLKBufTreeTop_BufTree1and2_NumOfStage
        _Caculation_Parameters['_BufTree1_SizeofEachStage'] = _CLKBufTreeTop_BufTree1_SizeofEachStage
        _Caculation_Parameters['_BufTree2_SizeofEachStage'] = _CLKBufTreeTop_BufTree2_SizeofEachStage
        _Caculation_Parameters['_BufTree_OutputPlacement'] = 'Dn'
        _Caculation_Parameters['_BufTree_OutputVia'] = None

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_CLKBufferTree_Top'] = \
        self._SrefElementDeclaration(_DesignObj=F00_02_CLKBufferTree_v3._CLKBufferTree(_DesignParameter=None, _Name='{}:SRF_CLKBufferTree_Top'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_CLKBufferTree_Top']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CLKBufferTree_Top']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CLKBufferTree_Top']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKBufferTree_Top']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKBufferTree_Top']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1x = self.get_param_KJH4('SRF_SARLogic', 'BND_Pbody_M1Exten')
        # tmp1y = self.get_param_KJH4('SRF_SARLogic','BND_Pbody_M1Exten')
        target_coord = tmp1x[0][0][0]['_XY_down']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_CLKBufferTree_Top', 'BND_Pbody_M1')
        approaching_coord = tmp2[0][0][0]['_XY_down']
        ## Sref coord
        TopCLKBufferBody2SARLogicBody = 0
        # _CLKBufTreeTop_XOffSet = 0
        tmp3 = self.get_param_KJH4('SRF_CLKBufferTree_Top')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[1] = Scoord[1] + TopCLKBufferBody2SARLogicBody
        Scoord[0] = Scoord[0] + _CLKBufTreeTop_XOffSet
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['SRF_CLKBufferTree_Top']['_XYCoordinates'] = tmpXY




        ####### Bot CLK Buffer Tree2 SRF Generation : Fake generation to get _SpaceBtwPbodyAndCLKSrc and _SpaceBtwNbody2AndCompOut
        _Caculation_Parameters = copy.deepcopy(F00_02_CLKBufferTree_v3._CLKBufferTree._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_UnitBuf_XVT'] = _CLKBufTreeBot_UnitBuf_XVT

        _Caculation_Parameters['_UnitBuf_NMOS_NumberofGate'] = _CLKBufTreeBot_UnitBuf_NMOS_NumberofGate
        _Caculation_Parameters['_UnitBuf_NMOS_ChannelWidth'] = _CLKBufTreeBot_UnitBuf_NMOS_ChannelWidth
        _Caculation_Parameters['_UnitBuf_NMOS_ChannelLength'] = _CLKBufTreeBot_UnitBuf_NMOS_ChannelLength

        _Caculation_Parameters['_UnitBuf_PMOS_NumberofGate'] = _CLKBufTreeBot_UnitBuf_PMOS_NumberofGate
        _Caculation_Parameters['_UnitBuf_PMOS_ChannelWidth'] = _CLKBufTreeBot_UnitBuf_PMOS_ChannelWidth
        _Caculation_Parameters['_UnitBuf_PMOS_ChannelLength'] = _CLKBufTreeBot_UnitBuf_PMOS_ChannelLength

        _Caculation_Parameters['_UnitBuf_PMOSXvt2NMOSXvt'] = _CLKBufTreeBot_UnitBuf_PMOSXvt2NMOSXvt

        _Caculation_Parameters['_BufTree_TotalLength']      = PbodyXWidthSARLogic
        _Caculation_Parameters['_BufTree1and2_NumOfStage']  = _CLKBufTreeBot_BufTree1and2_NumOfStage
        _Caculation_Parameters['_BufTree1_SizeofEachStage'] = _CLKBufTreeBot_BufTree1_SizeofEachStage
        _Caculation_Parameters['_BufTree2_SizeofEachStage'] = _CLKBufTreeBot_BufTree2_SizeofEachStage
        _Caculation_Parameters['_BufTree_OutputPlacement']  = 'Up'
        _Caculation_Parameters['_BufTree_OutputVia']        = None

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_CLKBufferTree_Bot'] = self._SrefElementDeclaration(_DesignObj=F00_02_CLKBufferTree_v3._CLKBufferTree(_DesignParameter=None,_Name='{}:SRF_CLKBufferTree_Bot'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_CLKBufferTree_Bot']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CLKBufferTree_Bot']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CLKBufferTree_Bot']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKBufferTree_Bot']['_XYCoordinates'] = [[0, 0]]


        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKBufferTree_Bot']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        # tmp1x = self.get_param_KJH4('BND_SARLogic_CLK_DoutIn_Hrz_M3')
        tmp1x = self.get_param_KJH4('SRF_SARLogic', 'BND_Pbody_M1Exten')
        tmp1y = self.get_param_KJH4('SRF_SARLogic', 'BND_Nbody2_M1Exten')
        target_coord = [tmp1x[0][0][0]['_XY_cent'][0], tmp1y[0][0][0]['_XY_up'][1]]
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_CLKBufferTree_Bot', 'BND_Nbody_M1')
        approaching_coord = tmp2[0][0][0]['_XY_up']
        ## Sref coord
        BottomCLKBufferBody2SARLogicBody = 0
        # _CLKBufTreeBot_XOffSet = 0
        tmp3 = self.get_param_KJH4('SRF_CLKBufferTree_Bot')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[1] = Scoord[1] - BottomCLKBufferBody2SARLogicBody
        Scoord[0] = Scoord[0] + _CLKBufTreeBot_XOffSet
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['SRF_CLKBufferTree_Bot']['_XYCoordinates'] = tmpXY





        ## BND_SARLogic_CLK_SampInExten_Hrz_M3
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_SARLogic_CLK_SampIn_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmpA = self.get_param_KJH4('SRF_SARLogic', 'BND_Therm0_Set_Hrz_M3')
        tmpB = self.get_param_KJH4('SRF_SARLogic', 'BND_ThermDACCtrl_Rst_Hrz_M3')
        tmpC = self.get_param_KJH4('SRF_SARLogic', 'BND_Therm_Clk_Hrz_M3')
        tmpD = self.get_param_KJH4('SRF_CLKBufferTree_Top', 'BND_Buf{}_Output_M2'.format(1))
        self._DesignParameter['BND_SARLogic_CLK_SampIn_Hrz_M3']['_YWidth'] = tmpA[0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1_1 = min(tmpA[0][0][0]['_XY_left'][0], tmpB[0][0][0]['_XY_left'][0], tmpC[0][0][0]['_XY_left'][0], tmpD[0][0][0]['_XY_left'][0])
        tmp1_2 = max(tmpA[0][0][0]['_XY_right'][0], tmpB[0][0][0]['_XY_right'][0], tmpC[0][0][0]['_XY_right'][0], tmpD[0][-1][0]['_XY_right'][0])
        M3UpperLogicClkInXWidth = abs(tmp1_1 - tmp1_2) + 244  # Via Size
        self._DesignParameter['BND_SARLogic_CLK_SampIn_Hrz_M3']['_XWidth'] = M3UpperLogicClkInXWidth

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_SARLogic_CLK_SampIn_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = [tmp1_1, tmpA[0][0][0]['_XY_down'][1]]
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_SARLogic_CLK_SampIn_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_SARLogic_CLK_SampIn_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_SARLogic_CLK_SampIn_Hrz_M3']['_XYCoordinates'] = tmpXY





        ## BND_SARLogic_CLK_SrcIn_Hrz_M3
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_SARLogic_CLK_SrcIn_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmpC = self.get_param_KJH4('SRF_SARLogic', 'BND_Therm_Clk_Hrz_M3')
        tmpD = self.get_param_KJH4('SRF_CLKBufferTree_Top', 'BND_Buf{}_Output_M2'.format(2))
        self._DesignParameter['BND_SARLogic_CLK_SrcIn_Hrz_M3']['_YWidth'] = tmpC[0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1_1 = min(tmpC[0][0][0]['_XY_left'][0], tmpD[0][0][0]['_XY_left'][0])
        tmp1_2 = max(tmpC[0][0][0]['_XY_right'][0], tmpD[0][-1][0]['_XY_right'][0])
        self._DesignParameter['BND_SARLogic_CLK_SrcIn_Hrz_M3']['_XWidth'] = abs(tmp1_1 - tmp1_2) + 244  # Via Size

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_SARLogic_CLK_SrcIn_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1

        target_coord = [tmp1_1, tmpC[0][0][0]['_XY_down'][1]]
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_SARLogic_CLK_SrcIn_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_SARLogic_CLK_SrcIn_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_SARLogic_CLK_SrcIn_Hrz_M3']['_XYCoordinates'] = tmpXY







        ## BND_CompOutput_Hrz_M3 Generation
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CompOutput_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_SARLogic', 'BND_DACCtrl_D_Hrz_M3')
        tmp2 = self.get_param_KJH4('SRF_CLKBufferTree_Bot', 'BND_Buf{}_Output_M2'.format(1))
        self._DesignParameter['BND_CompOutput_Hrz_M3']['_YWidth'] = tmp1[0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1_1 = min(tmp1[0][0][0]['_XY_left'][0], tmp2[0][0][0]['_XY_left'][0])
        tmp1_2 = max(tmp1[0][0][0]['_XY_right'][0], tmp2[0][-1][0]['_XY_right'][0])
        self._DesignParameter['BND_CompOutput_Hrz_M3']['_XWidth'] = abs(tmp1_1 - tmp1_2) + 244  # Via Size

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CompOutput_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = [tmp1_1, tmp1[0][0][0]['_XY_down'][1]]
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CompOutput_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CompOutput_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CompOutput_Hrz_M3']['_XYCoordinates'] = tmpXY







        ## BND_SARLogic_CLK_DoutIn_Hrz_M3
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_SARLogic_CLK_DoutIn_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_SARLogic', 'BND_DoutSamp_Clk_Hrz_M3')
        tmp2 = self.get_param_KJH4('SRF_CLKBufferTree_Bot', 'BND_Buf{}_Output_M2'.format(2))
        self._DesignParameter['BND_SARLogic_CLK_DoutIn_Hrz_M3']['_YWidth'] = tmp1[0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1_1 = min(tmp1[0][0][0]['_XY_left'][0], tmp2[0][0][0]['_XY_left'][0])
        tmp1_2 = max(tmp1[0][0][0]['_XY_right'][0], tmp2[0][-1][0]['_XY_right'][0])
        self._DesignParameter['BND_SARLogic_CLK_DoutIn_Hrz_M3']['_XWidth'] = abs(tmp1_1 - tmp1_2) + 244  # Via Size

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_SARLogic_CLK_DoutIn_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = [tmp1_1, tmp1[0][0][0]['_XY_down'][1]]
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_SARLogic_CLK_DoutIn_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_SARLogic_CLK_DoutIn_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_SARLogic_CLK_DoutIn_Hrz_M3']['_XYCoordinates'] = tmpXY






        ## BND_CLKSampBuf_Vtc_M2 Generation
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CLKSampBuf_Vtc_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_SARLogic_CLK_SampIn_Hrz_M3')
        tmp2 = self.get_param_KJH4('SRF_CLKBufferTree_Top', 'BND_Buf{}_Output_M2'.format(1))
        self._DesignParameter['BND_CLKSampBuf_Vtc_M2']['_YWidth'] = tmp1[0][0]['_XY_cent'][1] - tmp2[0][0][0]['_XY_down'][1]

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CLKSampBuf_Vtc_M2']['_XWidth'] = tmp2[0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CLKSampBuf_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_CLKSampBuf_Vtc_M2')
        tmp4 = self.get_param_KJH4('BND_CLKSampBuf_Vtc_M2')
        approaching_coord = tmp3[0][0]['_XY_down_left']
        for i in range(2 ** (_CLKBufTreeTop_BufTree1and2_NumOfStage - 1)):
            ## Target_coord: _XY_type1
            target_coord = tmp2[0][i][0]['_XY_down_left']
            ## Sref coord
            # tmp4 = self.get_param_KJH4('BND_CLKSampBuf_Vtc_M2') # to sepd up
            Scoord = tmp4[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CLKSampBuf_Vtc_M2']['_XYCoordinates'] = tmpXY

        ###### SRF_CLKSrcBuf_ViaM2M3
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKSampBuf_ViaM2M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_CLKSampBuf_ViaM2M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKSampBuf_ViaM2M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKSampBuf_ViaM2M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKSampBuf_ViaM2M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKSampBuf_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        tmp1 = self.get_param_KJH4('BND_CLKSampBuf_Vtc_M2')
        tmp1y = self.get_param_KJH4('BND_SARLogic_CLK_SampIn_Hrz_M3')
        tmp2 = self.get_param_KJH4('SRF_CLKSampBuf_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met3Layer')
        tmp3 = self.get_param_KJH4('SRF_CLKSampBuf_ViaM2M3')
        for i in range(2 ** (_CLKBufTreeBot_BufTree1and2_NumOfStage - 1)):
            ## Target_coord
            # tmp1 = self.get_param_KJH4('BND_CLKSampBuf_Vtc_M2') # to sped up
            # tmp1y = self.get_param_KJH4('BND_SARLogic_CLK_SampIn_Hrz_M3') # to sped up
            target_coord = [tmp1[i][0]['_XY_up_left'][0], tmp1y[0][0]['_XY_cent'][1]]
            ## Approaching_coord
            # tmp2 = self.get_param_KJH4('SRF_CLKSampBuf_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met3Layer') # to sped up
            approaching_coord = tmp2[0][0][0][0]['_XY_left']
            ## Sref coord
            # tmp3 = self.get_param_KJH4('SRF_CLKSampBuf_ViaM2M3') # to sped up
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKSampBuf_ViaM2M3']['_XYCoordinates'] = tmpXY

        ## BND_CLKSrcBuf_Vtc_M2 Generation
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CLKSrcBuf_Vtc_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_SARLogic_CLK_SrcIn_Hrz_M3')
        tmp2 = self.get_param_KJH4('SRF_CLKBufferTree_Top', 'BND_Buf{}_Output_M2'.format(2))
        self._DesignParameter['BND_CLKSrcBuf_Vtc_M2']['_YWidth'] = tmp1[0][0]['_XY_cent'][1] - tmp2[0][0][0]['_XY_down'][1]

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CLKSrcBuf_Vtc_M2']['_XWidth'] = tmp2[0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CLKSrcBuf_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_CLKSrcBuf_Vtc_M2')
        approaching_coord = tmp3[0][0]['_XY_down_left']
        # tmp4 = self.get_param_KJH4('BND_CLKSrcBuf_Vtc_M2')
        for i in range(2 ** (_CLKBufTreeTop_BufTree1and2_NumOfStage - 1)):
            ## Target_coord: _XY_type1
            target_coord = tmp2[0][i][0]['_XY_down_left']
            ## Sref coord
            # tmp4 = self.get_param_KJH4('BND_CLKSrcBuf_Vtc_M2') # to sped up
            Scoord = tmp4[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CLKSrcBuf_Vtc_M2']['_XYCoordinates'] = tmpXY

        ###### SRF_CLKSrcBuf_ViaM2M3
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKSrcBuf_ViaM2M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_CLKSrcBuf_ViaM2M3'.format(_Name)))[0]

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
        tmp2 = self.get_param_KJH4('SRF_CLKSrcBuf_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met3Layer')
        tmp3 = self.get_param_KJH4('SRF_CLKSrcBuf_ViaM2M3')

        for i in range(2 ** (_CLKBufTreeBot_BufTree1and2_NumOfStage - 1)):
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_CLKSrcBuf_Vtc_M2')
            tmp1y = self.get_param_KJH4('BND_SARLogic_CLK_SrcIn_Hrz_M3')
            target_coord = [tmp1[i][0]['_XY_up_left'][0], tmp1y[0][0]['_XY_cent'][1]]
            ## Approaching_coord
            # tmp2 = self.get_param_KJH4('SRF_CLKSrcBuf_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met3Layer') # to sped up
            approaching_coord = tmp2[0][0][0][0]['_XY_left']
            ## Sref coord
            # tmp3 = self.get_param_KJH4('SRF_CLKSrcBuf_ViaM2M3') # to sped up
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKSrcBuf_ViaM2M3']['_XYCoordinates'] = tmpXY

        ## BND_CompOutBuf_Vtc_M2 Generation
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CompOutBuf_Vtc_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_CompOutput_Hrz_M3')
        tmp2 = self.get_param_KJH4('SRF_CLKBufferTree_Bot', 'BND_Buf{}_Output_M2'.format(1))
        self._DesignParameter['BND_CompOutBuf_Vtc_M2']['_YWidth'] = tmp2[0][0][0]['_XY_up'][1] - tmp1[0][0]['_XY_cent'][1]

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CompOutBuf_Vtc_M2']['_XWidth'] = tmp2[0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CompOutBuf_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_CompOutBuf_Vtc_M2')
        approaching_coord = tmp3[0][0]['_XY_up_left']
        tmp4 = self.get_param_KJH4('BND_CompOutBuf_Vtc_M2')
        for i in range(2 ** (_CLKBufTreeBot_BufTree1and2_NumOfStage - 1)):
            ## Target_coord: _XY_type1
            target_coord = tmp2[0][i][0]['_XY_up_left']
            ## Sref coord
            # tmp4 = self.get_param_KJH4('BND_CompOutBuf_Vtc_M2') # to sped up
            Scoord = tmp4[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CompOutBuf_Vtc_M2']['_XYCoordinates'] = tmpXY

        ###### SRF_CompOutBuf_ViaM2M3
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CompOutBuf_ViaM2M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_CompOutBuf_ViaM2M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CompOutBuf_ViaM2M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CompOutBuf_ViaM2M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CompOutBuf_ViaM2M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CompOutBuf_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        tmp2 = self.get_param_KJH4('SRF_CompOutBuf_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met3Layer')
        tmp3 = self.get_param_KJH4('SRF_CompOutBuf_ViaM2M3')

        for i in range(2 ** (_CLKBufTreeBot_BufTree1and2_NumOfStage - 1)):
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_CompOutBuf_Vtc_M2')
            tmp1y = self.get_param_KJH4('BND_CompOutput_Hrz_M3')
            target_coord = [tmp1[i][0]['_XY_left'][0], tmp1y[0][0]['_XY_cent'][1]]
            ## Approaching_coord
            # tmp2 = self.get_param_KJH4('SRF_CompOutBuf_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met3Layer') # to sped up
            approaching_coord = tmp2[0][0][0][0]['_XY_left']
            ## Sref coord
            # tmp3 = self.get_param_KJH4('SRF_CompOutBuf_ViaM2M3') # to sped up
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CompOutBuf_ViaM2M3']['_XYCoordinates'] = tmpXY

        ## BND_CLKDoutOutBuf_Vtc_M2 Generation
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CLKDoutOutBuf_Vtc_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_SARLogic_CLK_DoutIn_Hrz_M3')
        tmp2 = self.get_param_KJH4('SRF_CLKBufferTree_Bot', 'BND_Buf{}_Output_M2'.format(2))
        self._DesignParameter['BND_CLKDoutOutBuf_Vtc_M2']['_YWidth'] = tmp2[0][0][0]['_XY_up'][1] - tmp1[0][0]['_XY_cent'][1]

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CLKDoutOutBuf_Vtc_M2']['_XWidth'] = tmp2[0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CLKDoutOutBuf_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_CLKDoutOutBuf_Vtc_M2')
        approaching_coord = tmp3[0][0]['_XY_up_left']

        tmp4 = self.get_param_KJH4('BND_CLKDoutOutBuf_Vtc_M2')
        for i in range(2 ** (_CLKBufTreeBot_BufTree1and2_NumOfStage - 1)):
            ## Target_coord: _XY_type1
            target_coord = tmp2[0][i][0]['_XY_up_left']
            ## Sref coord
            # tmp4 = self.get_param_KJH4('BND_CLKDoutOutBuf_Vtc_M2') # to sped up
            Scoord = tmp4[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_CLKDoutOutBuf_Vtc_M2']['_XYCoordinates'] = tmpXY

        ###### SRF_CLKDoutOutBuf_ViaM2M3
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKDoutOutBuf_ViaM2M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_CLKDoutOutBuf_ViaM2M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKDoutOutBuf_ViaM2M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKDoutOutBuf_ViaM2M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKDoutOutBuf_ViaM2M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKDoutOutBuf_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        tmp2 = self.get_param_KJH4('SRF_CLKDoutOutBuf_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met3Layer')
        tmp3 = self.get_param_KJH4('SRF_CLKDoutOutBuf_ViaM2M3')

        for i in range(2 ** (_CLKBufTreeBot_BufTree1and2_NumOfStage - 1)):
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_CLKDoutOutBuf_Vtc_M2')
            tmp1y = self.get_param_KJH4('BND_SARLogic_CLK_DoutIn_Hrz_M3')
            target_coord = [tmp1[i][0]['_XY_left'][0], tmp1y[0][0]['_XY_cent'][1]]
            ## Approaching_coord
            # tmp2 = self.get_param_KJH4('SRF_CLKDoutOutBuf_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met3Layer') # to sped up
            approaching_coord = tmp2[0][0][0][0]['_XY_left']
            ## Sref coord
            # tmp3 = self.get_param_KJH4('SRF_CLKDoutOutBuf_ViaM2M3') # to sped up
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKDoutOutBuf_ViaM2M3']['_XYCoordinates'] = tmpXY

        for j in range(1, 3):
            for i in range(1, _CLKBufTreeTop_BufTree1and2_NumOfStage + 1):
                del (self._DesignParameter['SRF_CLKBufferTree_Top']['_DesignObj']._DesignParameter['SRF_CLKBuf{}Inv_Stage{}'.format(j, i)]['_DesignObj']._DesignParameter['SRF_Pbody']['_DesignObj']._DesignParameter['SRF_PbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_COLayer'])
                del (self._DesignParameter['SRF_CLKBufferTree_Top']['_DesignObj']._DesignParameter['SRF_CLKBuf{}Inv_Stage{}'.format(j, i)]['_DesignObj']._DesignParameter['SRF_Nbody']['_DesignObj']._DesignParameter['SRF_NbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_COLayer'])
            for i in range(1, _CLKBufTreeBot_BufTree1and2_NumOfStage + 1):
                del (self._DesignParameter['SRF_CLKBufferTree_Bot']['_DesignObj']._DesignParameter['SRF_CLKBuf{}Inv_Stage{}'.format(j, i)]['_DesignObj']._DesignParameter['SRF_Pbody']['_DesignObj']._DesignParameter['SRF_PbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_COLayer'])
                del (self._DesignParameter['SRF_CLKBufferTree_Bot']['_DesignObj']._DesignParameter['SRF_CLKBuf{}Inv_Stage{}'.format(j, i)]['_DesignObj']._DesignParameter['SRF_Nbody']['_DesignObj']._DesignParameter['SRF_NbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_COLayer'])


        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')
        # start_time = time.time()
        end_time = time.time()
        self.elapsed_time = end_time - start_time

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ZZ01_K00_01_SARLogicWtBufTree_Fixed'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'K00_01_SARLogicWtCLKBufTree_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
## SAR Logic
    _NumofBit = 12,
    ## Clock Tree
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
    LayoutObj = _SARLogicWtCLKBufTree(_DesignParameter=None, _Name=cellname)
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
    Checker.lib_deletion()
    # Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()


    print('#############################      Finished      ################################')
    print('{} Hours   {} minutes   {} seconds'.format(h, m, s))
# end of 'main():' ---------------------------------------------------------------------------------------------
