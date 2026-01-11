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

from KJH91_Projects.Project_ADC.Layoutgen_code.F00_CLKBufferTree_YJH import F00_02_CLKBufferTree_v2
from KJH91_Projects.Project_ADC.Layoutgen_code.K00_SARLogicWtBuffers_YJH import K00_00_SARLogic_KJH1_v2
from KJH91_Projects.Project_ADC.Layoutgen_code.K00_SARLogicWtBuffers_YJH import K00_01_SARLogicWtCLKBufTree
from KJH91_Projects.Project_ADC.Layoutgen_code.J00_CDACPreDriver_InvBuffer_KJH0 import J00_02_CDAC_PreDriver_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.D00_SARLogic_Inverter_KJH1 import D00_00_Inverter_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.E01_ComparatorWtLatch_YJH import E01_03_AND_YJH


## Define Class
class _SARLogicWtCDACPreDriver(StickDiagram_KJH1._StickDiagram_KJH):
    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
        _NumofBit=8,

        _Test_distance=330,
        _Routing_width=50,
        _Routing_distance=80,

        _YWidthOfCLKSrc=100,
        _SpaceBtwCLKSrcAndCLKSamp=100,
        _YWidthOfCLKSamp=100,

        _YWidthOfCompOut=100,
        _SpaceBtwCompOutAndCLKDout=100,
        _YWidthOfCLKDout=100,

        ## DFF Common
        _DFF_Pbody_NumCont=2,  # number
        _DFF_Nbody_NumCont=2,  # number
        _DFF_PMOSXvt2NMOSXvt=1150,  # number
        _DFF_XvtTop2Pbody=None,  # number/None(Minimum)
        _DFF_Xvtdown2Nbody=None,  # number/None(Minimum)

        ## Master Xgate1
        ## Xgate common

        ## Xgate NMOS
        _Mst_Xgate1_NMOS_NumberofGate=1,  # 1
        _Mst_Xgate1_NMOS_ChannelWidth=200,  # 100
        _Mst_Xgate1_NMOS_ChannelLength=30,
        _Mst_Xgate1_NMOS_XVT='HVT',
        _Mst_Xgate1_NMOS_POGate_Comb_length=100,

        ## Xgate PMOS
        _Mst_Xgate1_PMOS_NumberofGate=1,  # 1
        _Mst_Xgate1_PMOS_ChannelWidth=400,  # 200
        _Mst_Xgate1_PMOS_ChannelLength=30,
        _Mst_Xgate1_PMOS_XVT='HVT',
        _Mst_Xgate1_PMOS_POGate_Comb_length=100,

        ## Master Xgate2
        ## Xgate common

        ## Xgate NMOS
        _Mst_Xgate2_NMOS_NumberofGate=1,
        _Mst_Xgate2_NMOS_ChannelWidth=200,
        _Mst_Xgate2_NMOS_ChannelLength=30,
        _Mst_Xgate2_NMOS_XVT='SLVT',
        _Mst_Xgate2_NMOS_POGate_Comb_length=100,

        ## Xgate PMOS
        _Mst_Xgate2_PMOS_NumberofGate=2,  # 2
        _Mst_Xgate2_PMOS_ChannelWidth=200,
        _Mst_Xgate2_PMOS_ChannelLength=30,
        _Mst_Xgate2_PMOS_XVT='SLVT',
        _Mst_Xgate2_PMOS_POGate_Comb_length=100,

        ## Master Nor1
        ## Nor1 common

        ## NMOS
        ## NMOS common
        _Mst_Nor1_NMOS_XVT='HVT',

        ## NMOSA
        _Mst_Nor1_NMOSA_NumberofGate=2,
        _Mst_Nor1_NMOSA_ChannelWidth=200,
        _Mst_Nor1_NMOSA_ChannelLength=30,
        _Mst_Nor1_NMOSA_POGate_Comb_length=100,

        ## NMOSB
        _Mst_Nor1_NMOSB_NumberofGate=2,
        _Mst_Nor1_NMOSB_ChannelWidth=200,
        _Mst_Nor1_NMOSB_ChannelLength=30,
        _Mst_Nor1_NMOSB_POGate_Comb_length=100,

        ## PMOS
        ## PMOS common
        _Mst_Nor1_PMOS_XVT='HVT',

        ## PMOSA
        _Mst_Nor1_PMOSA_NumberofGate=4,
        _Mst_Nor1_PMOSA_ChannelWidth=400,
        _Mst_Nor1_PMOSA_ChannelLength=30,
        _Mst_Nor1_PMOSA_POGate_Comb_length=100,

        ## PMOSB
        _Mst_Nor1_PMOSB_NumberofGate=4,
        _Mst_Nor1_PMOSB_ChannelWidth=400,
        _Mst_Nor1_PMOSB_ChannelLength=30,
        _Mst_Nor1_PMOSB_POGate_Comb_length=100,

        ## Master Nor2
        ## Nor2 common

        ## NMOS
        ## NMOS common
        _Mst_Nor2_NMOS_XVT='HVT',

        ## NMOSA
        _Mst_Nor2_NMOSA_NumberofGate=2,
        _Mst_Nor2_NMOSA_ChannelWidth=200,
        _Mst_Nor2_NMOSA_ChannelLength=30,
        _Mst_Nor2_NMOSA_POGate_Comb_length=100,

        ## NMOSB
        _Mst_Nor2_NMOSB_NumberofGate=2,
        _Mst_Nor2_NMOSB_ChannelWidth=200,
        _Mst_Nor2_NMOSB_ChannelLength=30,
        _Mst_Nor2_NMOSB_POGate_Comb_length=100,

        ## PMOS
        ## PMOS common
        _Mst_Nor2_PMOS_XVT='HVT',

        ## PMOSA
        _Mst_Nor2_PMOSA_NumberofGate=4,
        _Mst_Nor2_PMOSA_ChannelWidth=400,
        _Mst_Nor2_PMOSA_ChannelLength=30,
        _Mst_Nor2_PMOSA_POGate_Comb_length=100,

        ## PMOSB
        _Mst_Nor2_PMOSB_NumberofGate=4,
        _Mst_Nor2_PMOSB_ChannelWidth=400,
        _Mst_Nor2_PMOSB_ChannelLength=30,
        _Mst_Nor2_PMOSB_POGate_Comb_length=100,

        ## Master Inv1 : Set pre-driver
        ## Inv1 common

        ## Inv1 NMOS
        _Mst_Inv1_NMOS_NumberofGate=1,
        _Mst_Inv1_NMOS_ChannelWidth=200,
        _Mst_Inv1_NMOS_ChannelLength=30,
        _Mst_Inv1_NMOS_XVT='SLVT',
        _Mst_Inv1_NMOS_POGate_Comb_length=100,

        ## Inv1 PMOS
        _Mst_Inv1_PMOS_NumberofGate=1,
        _Mst_Inv1_PMOS_ChannelWidth=400,
        _Mst_Inv1_PMOS_ChannelLength=30,
        _Mst_Inv1_PMOS_XVT='SLVT',
        _Mst_Inv1_PMOS_POGate_Comb_length=100,

        ## Master Inv2 : Set driver
        ## Inv2 common

        ## Inv2 NMOS
        _Mst_Inv2_NMOS_NumberofGate=1,
        _Mst_Inv2_NMOS_ChannelWidth=200,
        _Mst_Inv2_NMOS_ChannelLength=30,
        _Mst_Inv2_NMOS_XVT='SLVT',
        _Mst_Inv2_NMOS_POGate_Comb_length=100,

        ## Inv2 PMOS
        _Mst_Inv2_PMOS_NumberofGate=1,
        _Mst_Inv2_PMOS_ChannelWidth=400,
        _Mst_Inv2_PMOS_ChannelLength=30,
        _Mst_Inv2_PMOS_XVT='SLVT',
        _Mst_Inv2_PMOS_POGate_Comb_length=100,

        ## Master Inv3 : Clock driver
        ## Inv3 common

        ## Inv3 NMOS
        _Mst_Inv3_NMOS_NumberofGate=1,
        _Mst_Inv3_NMOS_ChannelWidth=200,
        _Mst_Inv3_NMOS_ChannelLength=30,
        _Mst_Inv3_NMOS_XVT='SLVT',
        _Mst_Inv3_NMOS_POGate_Comb_length=100,

        ## Inv3 PMOS
        _Mst_Inv3_PMOS_NumberofGate=1,
        _Mst_Inv3_PMOS_ChannelWidth=400,
        _Mst_Inv3_PMOS_ChannelLength=30,
        _Mst_Inv3_PMOS_XVT='SLVT',
        _Mst_Inv3_PMOS_POGate_Comb_length=100,

        ## Slave Xgate1
        ## Xgate common

        ## Xgate NMOS
        _Slv_Xgate1_NMOS_NumberofGate=1,
        _Slv_Xgate1_NMOS_ChannelWidth=200,
        _Slv_Xgate1_NMOS_ChannelLength=30,
        _Slv_Xgate1_NMOS_XVT='HVT',
        _Slv_Xgate1_NMOS_POGate_Comb_length=100,

        ## Xgate NMOS
        _Slv_Xgate1_PMOS_NumberofGate=1,
        _Slv_Xgate1_PMOS_ChannelWidth=400,
        _Slv_Xgate1_PMOS_ChannelLength=30,
        _Slv_Xgate1_PMOS_XVT='HVT',
        _Slv_Xgate1_PMOS_POGate_Comb_length=100,

        ## Slave Xgate2
        ## Xgate common

        ## Xgate NMOS
        _Slv_Xgate2_NMOS_NumberofGate=1,
        _Slv_Xgate2_NMOS_ChannelWidth=200,
        _Slv_Xgate2_NMOS_ChannelLength=30,
        _Slv_Xgate2_NMOS_XVT='SLVT',
        _Slv_Xgate2_NMOS_POGate_Comb_length=100,

        ## Xgate NMOS
        _Slv_Xgate2_PMOS_NumberofGate=2,
        _Slv_Xgate2_PMOS_ChannelWidth=200,
        _Slv_Xgate2_PMOS_ChannelLength=30,
        _Slv_Xgate2_PMOS_XVT='SLVT',
        _Slv_Xgate2_PMOS_POGate_Comb_length=100,

        ## Slave Nor1
        ## Nor1 common

        ## NMOS
        ## NMOS common
        _Slv_Nor1_NMOS_XVT='HVT',

        ## NMOSA
        _Slv_Nor1_NMOSA_NumberofGate=2,
        _Slv_Nor1_NMOSA_ChannelWidth=200,
        _Slv_Nor1_NMOSA_ChannelLength=30,
        _Slv_Nor1_NMOSA_POGate_Comb_length=100,

        ## NMOSB
        _Slv_Nor1_NMOSB_NumberofGate=2,
        _Slv_Nor1_NMOSB_ChannelWidth=200,
        _Slv_Nor1_NMOSB_ChannelLength=30,
        _Slv_Nor1_NMOSB_POGate_Comb_length=100,

        ## PMOS
        ## PMOS common
        _Slv_Nor1_PMOS_XVT='HVT',

        ## PMOSA
        _Slv_Nor1_PMOSA_NumberofGate=4,
        _Slv_Nor1_PMOSA_ChannelWidth=400,
        _Slv_Nor1_PMOSA_ChannelLength=30,
        _Slv_Nor1_PMOSA_POGate_Comb_length=100,

        ## PMOSB
        _Slv_Nor1_PMOSB_NumberofGate=4,
        _Slv_Nor1_PMOSB_ChannelWidth=400,
        _Slv_Nor1_PMOSB_ChannelLength=30,
        _Slv_Nor1_PMOSB_POGate_Comb_length=100,

        ## Slave Nor2
        ## Nor2 common

        ## NMOS
        ## NMOS common
        _Slv_Nor2_NMOS_XVT='HVT',

        ## NMOSA
        _Slv_Nor2_NMOSA_NumberofGate=2,
        _Slv_Nor2_NMOSA_ChannelWidth=200,
        _Slv_Nor2_NMOSA_ChannelLength=30,
        _Slv_Nor2_NMOSA_POGate_Comb_length=100,

        ## NMOSB
        _Slv_Nor2_NMOSB_NumberofGate=2,
        _Slv_Nor2_NMOSB_ChannelWidth=200,
        _Slv_Nor2_NMOSB_ChannelLength=30,
        _Slv_Nor2_NMOSB_POGate_Comb_length=100,

        ## PMOS
        ## PMOS common
        _Slv_Nor2_PMOS_XVT='HVT',

        ## PMOSA
        _Slv_Nor2_PMOSA_NumberofGate=4,
        _Slv_Nor2_PMOSA_ChannelWidth=400,
        _Slv_Nor2_PMOSA_ChannelLength=30,
        _Slv_Nor2_PMOSA_POGate_Comb_length=100,

        ## PMOSB
        _Slv_Nor2_PMOSB_NumberofGate=4,
        _Slv_Nor2_PMOSB_ChannelWidth=400,
        _Slv_Nor2_PMOSB_ChannelLength=30,
        _Slv_Nor2_PMOSB_POGate_Comb_length=100,

        ## Slave Inv1 : ReSet pre-driver
        ## Inv1 common

        ## Inv1 NMOS
        _Slv_Inv1_NMOS_NumberofGate=1,
        _Slv_Inv1_NMOS_ChannelWidth=200,
        _Slv_Inv1_NMOS_ChannelLength=30,
        _Slv_Inv1_NMOS_XVT='SLVT',
        _Slv_Inv1_NMOS_POGate_Comb_length=100,

        ## Inv1 PMOS
        _Slv_Inv1_PMOS_NumberofGate=1,
        _Slv_Inv1_PMOS_ChannelWidth=400,
        _Slv_Inv1_PMOS_ChannelLength=30,
        _Slv_Inv1_PMOS_XVT='SLVT',
        _Slv_Inv1_PMOS_POGate_Comb_length=100,

        ## Slave Inv2 : ReSet driver
        ## Inv2 common

        ## Inv2 NMOS
        _Slv_Inv2_NMOS_NumberofGate=1,
        _Slv_Inv2_NMOS_ChannelWidth=300,
        _Slv_Inv2_NMOS_ChannelLength=30,
        _Slv_Inv2_NMOS_XVT='SLVT',
        _Slv_Inv2_NMOS_POGate_Comb_length=100,

        ## Inv2 PMOS
        _Slv_Inv2_PMOS_NumberofGate=1,
        _Slv_Inv2_PMOS_ChannelWidth=400,
        _Slv_Inv2_PMOS_ChannelLength=30,
        _Slv_Inv2_PMOS_XVT='SLVT',
        _Slv_Inv2_PMOS_POGate_Comb_length=100,

        ## Slave Inv3 : Qb driver
        ## Inv3 common

        ## Inv3 NMOS
        _Slv_Inv3_NMOS_NumberofGate=5,  # 1
        _Slv_Inv3_NMOS_ChannelWidth=200,
        _Slv_Inv3_NMOS_ChannelLength=30,
        _Slv_Inv3_NMOS_XVT='SLVT',
        _Slv_Inv3_NMOS_POGate_Comb_length=100,

        ## Inv3 PMOS
        _Slv_Inv3_PMOS_NumberofGate=5,  # 1
        _Slv_Inv3_PMOS_ChannelWidth=400,
        _Slv_Inv3_PMOS_ChannelLength=30,
        _Slv_Inv3_PMOS_XVT='SLVT',
        _Slv_Inv3_PMOS_POGate_Comb_length=100,

        # Top Clock  Tree Size
        # _CLKBufTreeTop_TotalLength=50000,
        _CLKBufTreeTop_NumOfStage=4,
        _CLKBufTreeTop_CLKSampBuf_SizeByStage=None,
        _CLKBufTreeTop_CLKSrcBuf_SizeByStage=None,  # 스테이지에 따른 버퍼 사이즈(UnitBuffer의 배수로 각 스테이지의 크기가 결정 됨.)
        _CLKBufTreeTop_XOffSet=0,

        ## Top CLK Buffer Size
        _CLKBufTreeTop_Inv_NMOS_ChannelWidth=400,  # Number
        _CLKBufTreeTop_Inv_NMOS_ChannelLength=30,  # Number
        _CLKBufTreeTop_Inv_NMOS_NumberofGate=1,  # Number
        _CLKBufTreeTop_Inv_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _CLKBufTreeTop_Inv_NMOS_POGate_Comb_length=100,  # None/Number

        _CLKBufTreeTop_Inv_PMOS_ChannelWidth=800,  # Number
        _CLKBufTreeTop_Inv_PMOS_ChannelLength=30,  # Number
        _CLKBufTreeTop_Inv_PMOS_NumberofGate=1,  # Number
        _CLKBufTreeTop_Inv_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _CLKBufTreeTop_Inv_PMOS_POGate_Comb_length=100,  # None/Number

        # Top CLK BufferPowerRail Size
        _CLKBufTreeTop_NMOS_Pbody_NumCont=2,
        _CLKBufTreeTop_NMOS_Pbody_XvtTop2Pbody=None,
        _CLKBufTreeTop_PMOS_Nbody_NumCont=2,
        _CLKBufTreeTop_PMOS_Nbody_Xvtdown2Nbody=None,
        _CLKBufTreeTop_PMOSXvt2NMOSXvt=700,

        # Bottom Clock  Tree Size
        # _CLKBufTreeBot_TotalLength=50000,
        _CLKBufTreeBot_NumOfStage=4,
        _CLKBufTreeBot_CompOutBuf_SizeByStage=None,
        _CLKBufTreeBot_CLKDoutBuf_SizeByStage=None,  # 스테이지에 따른 버퍼 사이즈(UnitBuffer의 배수로 각 스테이지의 크기가 결정 됨.)
        _CLKBufTreeBot_XOffSet=0,

        ## Bottom CLK Buffer Size
        _CLKBufTreeBot_Inv_NMOS_ChannelWidth=400,  # Number
        _CLKBufTreeBot_Inv_NMOS_ChannelLength=30,  # Number
        _CLKBufTreeBot_Inv_NMOS_NumberofGate=1,  # Number
        _CLKBufTreeBot_Inv_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _CLKBufTreeBot_Inv_NMOS_POGate_Comb_length=100,  # None/Number

        _CLKBufTreeBot_Inv_PMOS_ChannelWidth=800,  # Number
        _CLKBufTreeBot_Inv_PMOS_ChannelLength=30,  # Number
        _CLKBufTreeBot_Inv_PMOS_NumberofGate=1,  # Number
        _CLKBufTreeBot_Inv_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _CLKBufTreeBot_Inv_PMOS_POGate_Comb_length=100,  # None/Number

        # Bottom CLK Buffer PowerRail Size
        _CLKBufTreeBot_NMOS_Pbody_NumCont=2,
        _CLKBufTreeBot_NMOS_Pbody_XvtTop2Pbody=None,
        _CLKBufTreeBot_PMOS_Nbody_NumCont=2,
        _CLKBufTreeBot_PMOS_Nbody_Xvtdown2Nbody=None,
        _CLKBufTreeBot_PMOSXvt2NMOSXvt=446,

        #### CDAC Pre-Driver Sizing
        # _CDACPreDriver_Distance=12096,  # Number
        ## Number of Bit
        # _CDACPreDriver_NumBit=12,  # Number
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

        ## CLKDout Signal을 만드는 AND, Inverter
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
        _CLKDout_AND_NAND_NMOS_ChannelWidth=None,
        _CLKDout_AND_NAND_NMOS_ChannelLength=None,
        _CLKDout_AND_NAND_NMOS_NumberofGate=None,

        _CLKDout_AND_NAND_PMOS_ChannelWidth=None,
        _CLKDout_AND_NAND_PMOS_ChannelLength=None,
        _CLKDout_AND_NAND_PMOS_NumberofGate=None,

        _CLKDout_AND_Inv_NMOS_ChannelWidth=None,
        _CLKDout_AND_Inv_NMOS_ChannelLength=None,
        _CLKDout_AND_Inv_NMOS_NumberofGate=None,
        _CLKDout_AND_Inv_NMOS_POGate_Comb_length=None,

        _CLKDout_AND_Inv_PMOS_ChannelWidth=None,
        _CLKDout_AND_Inv_PMOS_ChannelLength=None,
        _CLKDout_AND_Inv_PMOS_NumberofGate=None,
        _CLKDout_AND_Inv_PMOS_POGate_Comb_length=None,

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

                                  _YWidthOfCLKSrc=100,
                                  _SpaceBtwCLKSrcAndCLKSamp=100,
                                  _YWidthOfCLKSamp=100,

                                  _YWidthOfCompOut=100,
                                  _SpaceBtwCompOutAndCLKDout=100,
                                  _YWidthOfCLKDout=100,

                                  ## DFF Common
                                  _DFF_Pbody_NumCont=2,  # number
                                  _DFF_Nbody_NumCont=2,  # number
                                  _DFF_PMOSXvt2NMOSXvt=1150,  # number
                                  _DFF_XvtTop2Pbody=None,  # number/None(Minimum)
                                  _DFF_Xvtdown2Nbody=None,  # number/None(Minimum)

                                  ## Master Xgate1
                                  ## Xgate common

                                  ## Xgate NMOS
                                  _Mst_Xgate1_NMOS_NumberofGate=1,  # 1
                                  _Mst_Xgate1_NMOS_ChannelWidth=200,  # 100
                                  _Mst_Xgate1_NMOS_ChannelLength=30,
                                  _Mst_Xgate1_NMOS_XVT='HVT',
                                  _Mst_Xgate1_NMOS_POGate_Comb_length=100,

                                  ## Xgate PMOS
                                  _Mst_Xgate1_PMOS_NumberofGate=1,  # 1
                                  _Mst_Xgate1_PMOS_ChannelWidth=400,  # 200
                                  _Mst_Xgate1_PMOS_ChannelLength=30,
                                  _Mst_Xgate1_PMOS_XVT='HVT',
                                  _Mst_Xgate1_PMOS_POGate_Comb_length=100,

                                  ## Master Xgate2
                                  ## Xgate common

                                  ## Xgate NMOS
                                  _Mst_Xgate2_NMOS_NumberofGate=1,
                                  _Mst_Xgate2_NMOS_ChannelWidth=200,
                                  _Mst_Xgate2_NMOS_ChannelLength=30,
                                  _Mst_Xgate2_NMOS_XVT='SLVT',
                                  _Mst_Xgate2_NMOS_POGate_Comb_length=100,

                                  ## Xgate PMOS
                                  _Mst_Xgate2_PMOS_NumberofGate=2,  # 2
                                  _Mst_Xgate2_PMOS_ChannelWidth=200,
                                  _Mst_Xgate2_PMOS_ChannelLength=30,
                                  _Mst_Xgate2_PMOS_XVT='SLVT',
                                  _Mst_Xgate2_PMOS_POGate_Comb_length=100,

                                  ## Master Nor1
                                  ## Nor1 common

                                  ## NMOS
                                  ## NMOS common
                                  _Mst_Nor1_NMOS_XVT='HVT',

                                  ## NMOSA
                                  _Mst_Nor1_NMOSA_NumberofGate=2,
                                  _Mst_Nor1_NMOSA_ChannelWidth=200,
                                  _Mst_Nor1_NMOSA_ChannelLength=30,
                                  _Mst_Nor1_NMOSA_POGate_Comb_length=100,

                                  ## NMOSB
                                  _Mst_Nor1_NMOSB_NumberofGate=2,
                                  _Mst_Nor1_NMOSB_ChannelWidth=200,
                                  _Mst_Nor1_NMOSB_ChannelLength=30,
                                  _Mst_Nor1_NMOSB_POGate_Comb_length=100,

                                  ## PMOS
                                  ## PMOS common
                                  _Mst_Nor1_PMOS_XVT='HVT',

                                  ## PMOSA
                                  _Mst_Nor1_PMOSA_NumberofGate=4,
                                  _Mst_Nor1_PMOSA_ChannelWidth=400,
                                  _Mst_Nor1_PMOSA_ChannelLength=30,
                                  _Mst_Nor1_PMOSA_POGate_Comb_length=100,

                                  ## PMOSB
                                  _Mst_Nor1_PMOSB_NumberofGate=4,
                                  _Mst_Nor1_PMOSB_ChannelWidth=400,
                                  _Mst_Nor1_PMOSB_ChannelLength=30,
                                  _Mst_Nor1_PMOSB_POGate_Comb_length=100,

                                  ## Master Nor2
                                  ## Nor2 common

                                  ## NMOS
                                  ## NMOS common
                                  _Mst_Nor2_NMOS_XVT='HVT',

                                  ## NMOSA
                                  _Mst_Nor2_NMOSA_NumberofGate=2,
                                  _Mst_Nor2_NMOSA_ChannelWidth=200,
                                  _Mst_Nor2_NMOSA_ChannelLength=30,
                                  _Mst_Nor2_NMOSA_POGate_Comb_length=100,

                                  ## NMOSB
                                  _Mst_Nor2_NMOSB_NumberofGate=2,
                                  _Mst_Nor2_NMOSB_ChannelWidth=200,
                                  _Mst_Nor2_NMOSB_ChannelLength=30,
                                  _Mst_Nor2_NMOSB_POGate_Comb_length=100,

                                  ## PMOS
                                  ## PMOS common
                                  _Mst_Nor2_PMOS_XVT='HVT',

                                  ## PMOSA
                                  _Mst_Nor2_PMOSA_NumberofGate=4,
                                  _Mst_Nor2_PMOSA_ChannelWidth=400,
                                  _Mst_Nor2_PMOSA_ChannelLength=30,
                                  _Mst_Nor2_PMOSA_POGate_Comb_length=100,

                                  ## PMOSB
                                  _Mst_Nor2_PMOSB_NumberofGate=4,
                                  _Mst_Nor2_PMOSB_ChannelWidth=400,
                                  _Mst_Nor2_PMOSB_ChannelLength=30,
                                  _Mst_Nor2_PMOSB_POGate_Comb_length=100,

                                  ## Master Inv1 : Set pre-driver
                                  ## Inv1 common

                                  ## Inv1 NMOS
                                  _Mst_Inv1_NMOS_NumberofGate=1,
                                  _Mst_Inv1_NMOS_ChannelWidth=200,
                                  _Mst_Inv1_NMOS_ChannelLength=30,
                                  _Mst_Inv1_NMOS_XVT='SLVT',
                                  _Mst_Inv1_NMOS_POGate_Comb_length=100,

                                  ## Inv1 PMOS
                                  _Mst_Inv1_PMOS_NumberofGate=1,
                                  _Mst_Inv1_PMOS_ChannelWidth=400,
                                  _Mst_Inv1_PMOS_ChannelLength=30,
                                  _Mst_Inv1_PMOS_XVT='SLVT',
                                  _Mst_Inv1_PMOS_POGate_Comb_length=100,

                                  ## Master Inv2 : Set driver
                                  ## Inv2 common

                                  ## Inv2 NMOS
                                  _Mst_Inv2_NMOS_NumberofGate=1,
                                  _Mst_Inv2_NMOS_ChannelWidth=200,
                                  _Mst_Inv2_NMOS_ChannelLength=30,
                                  _Mst_Inv2_NMOS_XVT='SLVT',
                                  _Mst_Inv2_NMOS_POGate_Comb_length=100,

                                  ## Inv2 PMOS
                                  _Mst_Inv2_PMOS_NumberofGate=1,
                                  _Mst_Inv2_PMOS_ChannelWidth=400,
                                  _Mst_Inv2_PMOS_ChannelLength=30,
                                  _Mst_Inv2_PMOS_XVT='SLVT',
                                  _Mst_Inv2_PMOS_POGate_Comb_length=100,

                                  ## Master Inv3 : Clock driver
                                  ## Inv3 common

                                  ## Inv3 NMOS
                                  _Mst_Inv3_NMOS_NumberofGate=1,
                                  _Mst_Inv3_NMOS_ChannelWidth=200,
                                  _Mst_Inv3_NMOS_ChannelLength=30,
                                  _Mst_Inv3_NMOS_XVT='SLVT',
                                  _Mst_Inv3_NMOS_POGate_Comb_length=100,

                                  ## Inv3 PMOS
                                  _Mst_Inv3_PMOS_NumberofGate=1,
                                  _Mst_Inv3_PMOS_ChannelWidth=400,
                                  _Mst_Inv3_PMOS_ChannelLength=30,
                                  _Mst_Inv3_PMOS_XVT='SLVT',
                                  _Mst_Inv3_PMOS_POGate_Comb_length=100,

                                  ## Slave Xgate1
                                  ## Xgate common

                                  ## Xgate NMOS
                                  _Slv_Xgate1_NMOS_NumberofGate=1,
                                  _Slv_Xgate1_NMOS_ChannelWidth=200,
                                  _Slv_Xgate1_NMOS_ChannelLength=30,
                                  _Slv_Xgate1_NMOS_XVT='HVT',
                                  _Slv_Xgate1_NMOS_POGate_Comb_length=100,

                                  ## Xgate NMOS
                                  _Slv_Xgate1_PMOS_NumberofGate=1,
                                  _Slv_Xgate1_PMOS_ChannelWidth=400,
                                  _Slv_Xgate1_PMOS_ChannelLength=30,
                                  _Slv_Xgate1_PMOS_XVT='HVT',
                                  _Slv_Xgate1_PMOS_POGate_Comb_length=100,

                                  ## Slave Xgate2
                                  ## Xgate common

                                  ## Xgate NMOS
                                  _Slv_Xgate2_NMOS_NumberofGate=1,
                                  _Slv_Xgate2_NMOS_ChannelWidth=200,
                                  _Slv_Xgate2_NMOS_ChannelLength=30,
                                  _Slv_Xgate2_NMOS_XVT='SLVT',
                                  _Slv_Xgate2_NMOS_POGate_Comb_length=100,

                                  ## Xgate NMOS
                                  _Slv_Xgate2_PMOS_NumberofGate=2,
                                  _Slv_Xgate2_PMOS_ChannelWidth=200,
                                  _Slv_Xgate2_PMOS_ChannelLength=30,
                                  _Slv_Xgate2_PMOS_XVT='SLVT',
                                  _Slv_Xgate2_PMOS_POGate_Comb_length=100,

                                  ## Slave Nor1
                                  ## Nor1 common

                                  ## NMOS
                                  ## NMOS common
                                  _Slv_Nor1_NMOS_XVT='HVT',

                                  ## NMOSA
                                  _Slv_Nor1_NMOSA_NumberofGate=2,
                                  _Slv_Nor1_NMOSA_ChannelWidth=200,
                                  _Slv_Nor1_NMOSA_ChannelLength=30,
                                  _Slv_Nor1_NMOSA_POGate_Comb_length=100,

                                  ## NMOSB
                                  _Slv_Nor1_NMOSB_NumberofGate=2,
                                  _Slv_Nor1_NMOSB_ChannelWidth=200,
                                  _Slv_Nor1_NMOSB_ChannelLength=30,
                                  _Slv_Nor1_NMOSB_POGate_Comb_length=100,

                                  ## PMOS
                                  ## PMOS common
                                  _Slv_Nor1_PMOS_XVT='HVT',

                                  ## PMOSA
                                  _Slv_Nor1_PMOSA_NumberofGate=4,
                                  _Slv_Nor1_PMOSA_ChannelWidth=400,
                                  _Slv_Nor1_PMOSA_ChannelLength=30,
                                  _Slv_Nor1_PMOSA_POGate_Comb_length=100,

                                  ## PMOSB
                                  _Slv_Nor1_PMOSB_NumberofGate=4,
                                  _Slv_Nor1_PMOSB_ChannelWidth=400,
                                  _Slv_Nor1_PMOSB_ChannelLength=30,
                                  _Slv_Nor1_PMOSB_POGate_Comb_length=100,

                                  ## Slave Nor2
                                  ## Nor2 common

                                  ## NMOS
                                  ## NMOS common
                                  _Slv_Nor2_NMOS_XVT='HVT',

                                  ## NMOSA
                                  _Slv_Nor2_NMOSA_NumberofGate=2,
                                  _Slv_Nor2_NMOSA_ChannelWidth=200,
                                  _Slv_Nor2_NMOSA_ChannelLength=30,
                                  _Slv_Nor2_NMOSA_POGate_Comb_length=100,

                                  ## NMOSB
                                  _Slv_Nor2_NMOSB_NumberofGate=2,
                                  _Slv_Nor2_NMOSB_ChannelWidth=200,
                                  _Slv_Nor2_NMOSB_ChannelLength=30,
                                  _Slv_Nor2_NMOSB_POGate_Comb_length=100,

                                  ## PMOS
                                  ## PMOS common
                                  _Slv_Nor2_PMOS_XVT='HVT',

                                  ## PMOSA
                                  _Slv_Nor2_PMOSA_NumberofGate=4,
                                  _Slv_Nor2_PMOSA_ChannelWidth=400,
                                  _Slv_Nor2_PMOSA_ChannelLength=30,
                                  _Slv_Nor2_PMOSA_POGate_Comb_length=100,

                                  ## PMOSB
                                  _Slv_Nor2_PMOSB_NumberofGate=4,
                                  _Slv_Nor2_PMOSB_ChannelWidth=400,
                                  _Slv_Nor2_PMOSB_ChannelLength=30,
                                  _Slv_Nor2_PMOSB_POGate_Comb_length=100,

                                  ## Slave Inv1 : ReSet pre-driver
                                  ## Inv1 common

                                  ## Inv1 NMOS
                                  _Slv_Inv1_NMOS_NumberofGate=1,
                                  _Slv_Inv1_NMOS_ChannelWidth=200,
                                  _Slv_Inv1_NMOS_ChannelLength=30,
                                  _Slv_Inv1_NMOS_XVT='SLVT',
                                  _Slv_Inv1_NMOS_POGate_Comb_length=100,

                                  ## Inv1 PMOS
                                  _Slv_Inv1_PMOS_NumberofGate=1,
                                  _Slv_Inv1_PMOS_ChannelWidth=400,
                                  _Slv_Inv1_PMOS_ChannelLength=30,
                                  _Slv_Inv1_PMOS_XVT='SLVT',
                                  _Slv_Inv1_PMOS_POGate_Comb_length=100,

                                  ## Slave Inv2 : ReSet driver
                                  ## Inv2 common

                                  ## Inv2 NMOS
                                  _Slv_Inv2_NMOS_NumberofGate=1,
                                  _Slv_Inv2_NMOS_ChannelWidth=300,
                                  _Slv_Inv2_NMOS_ChannelLength=30,
                                  _Slv_Inv2_NMOS_XVT='SLVT',
                                  _Slv_Inv2_NMOS_POGate_Comb_length=100,

                                  ## Inv2 PMOS
                                  _Slv_Inv2_PMOS_NumberofGate=1,
                                  _Slv_Inv2_PMOS_ChannelWidth=400,
                                  _Slv_Inv2_PMOS_ChannelLength=30,
                                  _Slv_Inv2_PMOS_XVT='SLVT',
                                  _Slv_Inv2_PMOS_POGate_Comb_length=100,

                                  ## Slave Inv3 : Qb driver
                                  ## Inv3 common

                                  ## Inv3 NMOS
                                  _Slv_Inv3_NMOS_NumberofGate=5,  # 1
                                  _Slv_Inv3_NMOS_ChannelWidth=200,
                                  _Slv_Inv3_NMOS_ChannelLength=30,
                                  _Slv_Inv3_NMOS_XVT='SLVT',
                                  _Slv_Inv3_NMOS_POGate_Comb_length=100,

                                  ## Inv3 PMOS
                                  _Slv_Inv3_PMOS_NumberofGate=5,  # 1
                                  _Slv_Inv3_PMOS_ChannelWidth=400,
                                  _Slv_Inv3_PMOS_ChannelLength=30,
                                  _Slv_Inv3_PMOS_XVT='SLVT',
                                  _Slv_Inv3_PMOS_POGate_Comb_length=100,

                                  # Top Clock  Tree Size
                                  _CLKBufTreeTop_NumOfStage=4,
                                  _CLKBufTreeTop_CLKSampBuf_SizeByStage=None,
                                  _CLKBufTreeTop_CLKSrcBuf_SizeByStage=None,
                                  # 스테이지에 따른 버퍼 사이즈(UnitBuffer의 배수로 각 스테이지의 크기가 결정 됨.)
                                  _CLKBufTreeTop_XOffSet=0,

                                  ## Top CLK Buffer Size
                                  _CLKBufTreeTop_Inv_NMOS_ChannelWidth=400,  # Number
                                  _CLKBufTreeTop_Inv_NMOS_ChannelLength=30,  # Number
                                  _CLKBufTreeTop_Inv_NMOS_NumberofGate=1,  # Number
                                  _CLKBufTreeTop_Inv_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _CLKBufTreeTop_Inv_NMOS_POGate_Comb_length=100,  # None/Number

                                  _CLKBufTreeTop_Inv_PMOS_ChannelWidth=800,  # Number
                                  _CLKBufTreeTop_Inv_PMOS_ChannelLength=30,  # Number
                                  _CLKBufTreeTop_Inv_PMOS_NumberofGate=1,  # Number
                                  _CLKBufTreeTop_Inv_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _CLKBufTreeTop_Inv_PMOS_POGate_Comb_length=100,  # None/Number

                                  # Top CLK BufferPowerRail Size
                                  _CLKBufTreeTop_NMOS_Pbody_NumCont=2,
                                  _CLKBufTreeTop_NMOS_Pbody_XvtTop2Pbody=None,
                                  _CLKBufTreeTop_PMOS_Nbody_NumCont=2,
                                  _CLKBufTreeTop_PMOS_Nbody_Xvtdown2Nbody=None,
                                  _CLKBufTreeTop_PMOSXvt2NMOSXvt=700,

                                  # Bottom Clock  Tree Size
                                  _CLKBufTreeBot_NumOfStage=4,
                                  _CLKBufTreeBot_CompOutBuf_SizeByStage=None,
                                  _CLKBufTreeBot_CLKDoutBuf_SizeByStage=None,
                                  # 스테이지에 따른 버퍼 사이즈(UnitBuffer의 배수로 각 스테이지의 크기가 결정 됨.)
                                  _CLKBufTreeBot_XOffSet=0,

                                  ## Bottom CLK Buffer Size
                                  _CLKBufTreeBot_Inv_NMOS_ChannelWidth=400,  # Number
                                  _CLKBufTreeBot_Inv_NMOS_ChannelLength=30,  # Number
                                  _CLKBufTreeBot_Inv_NMOS_NumberofGate=1,  # Number
                                  _CLKBufTreeBot_Inv_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _CLKBufTreeBot_Inv_NMOS_POGate_Comb_length=100,  # None/Number

                                  _CLKBufTreeBot_Inv_PMOS_ChannelWidth=800,  # Number
                                  _CLKBufTreeBot_Inv_PMOS_ChannelLength=30,  # Number
                                  _CLKBufTreeBot_Inv_PMOS_NumberofGate=1,  # Number
                                  _CLKBufTreeBot_Inv_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _CLKBufTreeBot_Inv_PMOS_POGate_Comb_length=100,  # None/Number

                                  # Bottom CLK Buffer PowerRail Size
                                  _CLKBufTreeBot_NMOS_Pbody_NumCont=2,
                                  _CLKBufTreeBot_NMOS_Pbody_XvtTop2Pbody=None,
                                  _CLKBufTreeBot_PMOS_Nbody_NumCont=2,
                                  _CLKBufTreeBot_PMOS_Nbody_Xvtdown2Nbody=None,
                                  _CLKBufTreeBot_PMOSXvt2NMOSXvt=700,

                                  #### CDAC Pre-Driver Sizing
                                  ## Number of Bit
                                  # _CDACPreDriver_NumBit=12,  # Number
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

                                  ## CLKDout Signal을 만드는 AND, Inverter
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
                                  _CLKDout_AND_NAND_NMOS_ChannelWidth=None,
                                  _CLKDout_AND_NAND_NMOS_ChannelLength=None,
                                  _CLKDout_AND_NAND_NMOS_NumberofGate=None,

                                  _CLKDout_AND_NAND_PMOS_ChannelWidth=None,
                                  _CLKDout_AND_NAND_PMOS_ChannelLength=None,
                                  _CLKDout_AND_NAND_PMOS_NumberofGate=None,

                                  _CLKDout_AND_Inv_NMOS_ChannelWidth=None,
                                  _CLKDout_AND_Inv_NMOS_ChannelLength=None,
                                  _CLKDout_AND_Inv_NMOS_NumberofGate=None,
                                  _CLKDout_AND_Inv_NMOS_POGate_Comb_length=None,

                                  _CLKDout_AND_Inv_PMOS_ChannelWidth=None,
                                  _CLKDout_AND_Inv_PMOS_ChannelLength=None,
                                  _CLKDout_AND_Inv_PMOS_NumberofGate=None,
                                  _CLKDout_AND_Inv_PMOS_POGate_Comb_length=None,

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

        ###############################
        ## SRF_SARLogicWtCLKBufTree Generation
        _Caculation_Parameters = copy.deepcopy(
            K00_01_SARLogicWtCLKBufTree._SARLogicWtCLKBufTree._ParametersForDesignCalculation)
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters['_NumofBit'] = _NumofBit
        _Caculation_Parameters['_Test_distance'] = _Test_distance
        _Caculation_Parameters['_Routing_width'] = _Routing_width
        _Caculation_Parameters['_Routing_distance'] = _Routing_distance

        _Caculation_Parameters['_YWidthOfCLKSrc'] = _YWidthOfCLKSrc
        _Caculation_Parameters['_SpaceBtwCLKSrcAndCLKSamp'] = _SpaceBtwCLKSrcAndCLKSamp
        _Caculation_Parameters['_YWidthOfCLKSamp'] = _YWidthOfCLKSamp
        _Caculation_Parameters['_YWidthOfCompOut'] = _YWidthOfCompOut
        _Caculation_Parameters['_SpaceBtwCompOutAndCLKDout'] = _SpaceBtwCompOutAndCLKDout
        _Caculation_Parameters['_YWidthOfCLKDout'] = _YWidthOfCLKDout

        ## DFF Common
        _Caculation_Parameters['_DFF_Pbody_NumCont'] = _DFF_Pbody_NumCont
        _Caculation_Parameters['_DFF_Nbody_NumCont'] = _DFF_Nbody_NumCont
        _Caculation_Parameters['_DFF_PMOSXvt2NMOSXvt'] = _DFF_PMOSXvt2NMOSXvt
        _Caculation_Parameters['_DFF_XvtTop2Pbody'] = _DFF_XvtTop2Pbody
        _Caculation_Parameters['_DFF_Xvtdown2Nbody'] = _DFF_Xvtdown2Nbody

        ## Master Xgate1
        ## Xgate NMOS
        _Caculation_Parameters['_Mst_Xgate1_NMOS_NumberofGate'] = _Mst_Xgate1_NMOS_NumberofGate
        _Caculation_Parameters['_Mst_Xgate1_NMOS_ChannelWidth'] = _Mst_Xgate1_NMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Xgate1_NMOS_ChannelLength'] = _Mst_Xgate1_NMOS_ChannelLength
        _Caculation_Parameters['_Mst_Xgate1_NMOS_XVT'] = _Mst_Xgate1_NMOS_XVT
        _Caculation_Parameters['_Mst_Xgate1_NMOS_POGate_Comb_length'] = _Mst_Xgate1_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters['_Mst_Xgate1_PMOS_NumberofGate'] = _Mst_Xgate1_PMOS_NumberofGate
        _Caculation_Parameters['_Mst_Xgate1_PMOS_ChannelWidth'] = _Mst_Xgate1_PMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Xgate1_PMOS_ChannelLength'] = _Mst_Xgate1_PMOS_ChannelLength
        _Caculation_Parameters['_Mst_Xgate1_PMOS_XVT'] = _Mst_Xgate1_PMOS_XVT
        _Caculation_Parameters['_Mst_Xgate1_PMOS_POGate_Comb_length'] = _Mst_Xgate1_PMOS_POGate_Comb_length

        ## Master Xgate2
        ## Xgate NMOS
        _Caculation_Parameters['_Mst_Xgate2_NMOS_NumberofGate'] = _Mst_Xgate2_NMOS_NumberofGate
        _Caculation_Parameters['_Mst_Xgate2_NMOS_ChannelWidth'] = _Mst_Xgate2_NMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Xgate2_NMOS_ChannelLength'] = _Mst_Xgate2_NMOS_ChannelLength
        _Caculation_Parameters['_Mst_Xgate2_NMOS_XVT'] = _Mst_Xgate2_NMOS_XVT
        _Caculation_Parameters['_Mst_Xgate2_NMOS_POGate_Comb_length'] = _Mst_Xgate2_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters['_Mst_Xgate2_PMOS_NumberofGate'] = _Mst_Xgate2_PMOS_NumberofGate
        _Caculation_Parameters['_Mst_Xgate2_PMOS_ChannelWidth'] = _Mst_Xgate2_PMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Xgate2_PMOS_ChannelLength'] = _Mst_Xgate2_PMOS_ChannelLength
        _Caculation_Parameters['_Mst_Xgate2_PMOS_XVT'] = _Mst_Xgate2_PMOS_XVT
        _Caculation_Parameters['_Mst_Xgate2_PMOS_POGate_Comb_length'] = _Mst_Xgate2_PMOS_POGate_Comb_length

        ## Master Nor1
        ## NMOS common
        _Caculation_Parameters['_Mst_Nor1_NMOS_XVT'] = _Mst_Nor1_NMOS_XVT

        ## Nor1 NMOSA
        _Caculation_Parameters['_Mst_Nor1_NMOSA_NumberofGate'] = _Mst_Nor1_NMOSA_NumberofGate
        _Caculation_Parameters['_Mst_Nor1_NMOSA_ChannelWidth'] = _Mst_Nor1_NMOSA_ChannelWidth
        _Caculation_Parameters['_Mst_Nor1_NMOSA_ChannelLength'] = _Mst_Nor1_NMOSA_ChannelLength
        _Caculation_Parameters['_Mst_Nor1_NMOSA_POGate_Comb_length'] = _Mst_Nor1_NMOSA_POGate_Comb_length

        ## Nor1 NMOSB
        _Caculation_Parameters['_Mst_Nor1_NMOSB_NumberofGate'] = _Mst_Nor1_NMOSB_NumberofGate
        _Caculation_Parameters['_Mst_Nor1_NMOSB_ChannelWidth'] = _Mst_Nor1_NMOSB_ChannelWidth
        _Caculation_Parameters['_Mst_Nor1_NMOSB_ChannelLength'] = _Mst_Nor1_NMOSB_ChannelLength
        _Caculation_Parameters['_Mst_Nor1_NMOSB_POGate_Comb_length'] = _Mst_Nor1_NMOSB_POGate_Comb_length

        ## PMOS common
        _Caculation_Parameters['_Mst_Nor1_PMOS_XVT'] = _Mst_Nor1_PMOS_XVT

        ## Nor1 PMOSA
        _Caculation_Parameters['_Mst_Nor1_PMOSA_NumberofGate'] = _Mst_Nor1_PMOSA_NumberofGate
        _Caculation_Parameters['_Mst_Nor1_PMOSA_ChannelWidth'] = _Mst_Nor1_PMOSA_ChannelWidth
        _Caculation_Parameters['_Mst_Nor1_PMOSA_ChannelLength'] = _Mst_Nor1_PMOSA_ChannelLength
        _Caculation_Parameters['_Mst_Nor1_PMOSA_POGate_Comb_length'] = _Mst_Nor1_PMOSA_POGate_Comb_length

        ## Nor1 PMOSB
        _Caculation_Parameters['_Mst_Nor1_PMOSB_NumberofGate'] = _Mst_Nor1_PMOSB_NumberofGate
        _Caculation_Parameters['_Mst_Nor1_PMOSB_ChannelWidth'] = _Mst_Nor1_PMOSB_ChannelWidth
        _Caculation_Parameters['_Mst_Nor1_PMOSB_ChannelLength'] = _Mst_Nor1_PMOSB_ChannelLength
        _Caculation_Parameters['_Mst_Nor1_PMOSB_POGate_Comb_length'] = _Mst_Nor1_PMOSB_POGate_Comb_length

        ## Master Nor2
        ## NMOS common
        _Caculation_Parameters['_Mst_Nor2_NMOS_XVT'] = _Mst_Nor2_NMOS_XVT

        ## Nor2 NMOSA
        _Caculation_Parameters['_Mst_Nor2_NMOSA_NumberofGate'] = _Mst_Nor2_NMOSA_NumberofGate
        _Caculation_Parameters['_Mst_Nor2_NMOSA_ChannelWidth'] = _Mst_Nor2_NMOSA_ChannelWidth
        _Caculation_Parameters['_Mst_Nor2_NMOSA_ChannelLength'] = _Mst_Nor2_NMOSA_ChannelLength
        _Caculation_Parameters['_Mst_Nor2_NMOSA_POGate_Comb_length'] = _Mst_Nor2_NMOSA_POGate_Comb_length

        ## Nor2 NMOSB
        _Caculation_Parameters['_Mst_Nor2_NMOSB_NumberofGate'] = _Mst_Nor2_NMOSB_NumberofGate
        _Caculation_Parameters['_Mst_Nor2_NMOSB_ChannelWidth'] = _Mst_Nor2_NMOSB_ChannelWidth
        _Caculation_Parameters['_Mst_Nor2_NMOSB_ChannelLength'] = _Mst_Nor2_NMOSB_ChannelLength
        _Caculation_Parameters['_Mst_Nor2_NMOSB_POGate_Comb_length'] = _Mst_Nor2_NMOSB_POGate_Comb_length

        ## PMOS common
        _Caculation_Parameters['_Mst_Nor2_PMOS_XVT'] = _Mst_Nor2_PMOS_XVT

        ## Nor2 PMOSA
        _Caculation_Parameters['_Mst_Nor2_PMOSA_NumberofGate'] = _Mst_Nor2_PMOSA_NumberofGate
        _Caculation_Parameters['_Mst_Nor2_PMOSA_ChannelWidth'] = _Mst_Nor2_PMOSA_ChannelWidth
        _Caculation_Parameters['_Mst_Nor2_PMOSA_ChannelLength'] = _Mst_Nor2_PMOSA_ChannelLength
        _Caculation_Parameters['_Mst_Nor2_PMOSA_POGate_Comb_length'] = _Mst_Nor2_PMOSA_POGate_Comb_length

        ## Nor2 PMOSB
        _Caculation_Parameters['_Mst_Nor2_PMOSB_NumberofGate'] = _Mst_Nor2_PMOSB_NumberofGate
        _Caculation_Parameters['_Mst_Nor2_PMOSB_ChannelWidth'] = _Mst_Nor2_PMOSB_ChannelWidth
        _Caculation_Parameters['_Mst_Nor2_PMOSB_ChannelLength'] = _Mst_Nor2_PMOSB_ChannelLength
        _Caculation_Parameters['_Mst_Nor2_PMOSB_POGate_Comb_length'] = _Mst_Nor2_PMOSB_POGate_Comb_length

        ## Master Inv1
        ## Xgate NMOS
        _Caculation_Parameters['_Mst_Inv1_NMOS_NumberofGate'] = _Mst_Inv1_NMOS_NumberofGate
        _Caculation_Parameters['_Mst_Inv1_NMOS_ChannelWidth'] = _Mst_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Inv1_NMOS_ChannelLength'] = _Mst_Inv1_NMOS_ChannelLength
        _Caculation_Parameters['_Mst_Inv1_NMOS_XVT'] = _Mst_Inv1_NMOS_XVT
        _Caculation_Parameters['_Mst_Inv1_NMOS_POGate_Comb_length'] = _Mst_Inv1_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters['_Mst_Inv1_PMOS_NumberofGate'] = _Mst_Inv1_PMOS_NumberofGate
        _Caculation_Parameters['_Mst_Inv1_PMOS_ChannelWidth'] = _Mst_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Inv1_PMOS_ChannelLength'] = _Mst_Inv1_PMOS_ChannelLength
        _Caculation_Parameters['_Mst_Inv1_PMOS_XVT'] = _Mst_Inv1_PMOS_XVT
        _Caculation_Parameters['_Mst_Inv1_PMOS_POGate_Comb_length'] = _Mst_Inv1_PMOS_POGate_Comb_length

        ## Master Inv2 : Set driver
        ## Xgate NMOS
        _Caculation_Parameters['_Mst_Inv2_NMOS_NumberofGate'] = _Mst_Inv2_NMOS_NumberofGate
        _Caculation_Parameters['_Mst_Inv2_NMOS_ChannelWidth'] = _Mst_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Inv2_NMOS_ChannelLength'] = _Mst_Inv2_NMOS_ChannelLength
        _Caculation_Parameters['_Mst_Inv2_NMOS_XVT'] = _Mst_Inv2_NMOS_XVT
        _Caculation_Parameters['_Mst_Inv2_NMOS_POGate_Comb_length'] = _Mst_Inv2_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters['_Mst_Inv2_PMOS_NumberofGate'] = _Mst_Inv2_PMOS_NumberofGate
        _Caculation_Parameters['_Mst_Inv2_PMOS_ChannelWidth'] = _Mst_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Inv2_PMOS_ChannelLength'] = _Mst_Inv2_PMOS_ChannelLength
        _Caculation_Parameters['_Mst_Inv2_PMOS_XVT'] = _Mst_Inv2_PMOS_XVT
        _Caculation_Parameters['_Mst_Inv2_PMOS_POGate_Comb_length'] = _Mst_Inv2_PMOS_POGate_Comb_length

        ## Master Inv3 : Clock driver
        ## Xgate NMOS
        _Caculation_Parameters['_Mst_Inv3_NMOS_NumberofGate'] = _Mst_Inv3_NMOS_NumberofGate
        _Caculation_Parameters['_Mst_Inv3_NMOS_ChannelWidth'] = _Mst_Inv3_NMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Inv3_NMOS_ChannelLength'] = _Mst_Inv3_NMOS_ChannelLength
        _Caculation_Parameters['_Mst_Inv3_NMOS_XVT'] = _Mst_Inv3_NMOS_XVT
        _Caculation_Parameters['_Mst_Inv3_NMOS_POGate_Comb_length'] = _Mst_Inv3_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters['_Mst_Inv3_PMOS_NumberofGate'] = _Mst_Inv3_PMOS_NumberofGate
        _Caculation_Parameters['_Mst_Inv3_PMOS_ChannelWidth'] = _Mst_Inv3_PMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Inv3_PMOS_ChannelLength'] = _Mst_Inv3_PMOS_ChannelLength
        _Caculation_Parameters['_Mst_Inv3_PMOS_XVT'] = _Mst_Inv3_PMOS_XVT
        _Caculation_Parameters['_Mst_Inv3_PMOS_POGate_Comb_length'] = _Mst_Inv3_PMOS_POGate_Comb_length

        ## Slave Xgate1
        ## Xgate NMOS
        _Caculation_Parameters['_Slv_Xgate1_NMOS_NumberofGate'] = _Slv_Xgate1_NMOS_NumberofGate
        _Caculation_Parameters['_Slv_Xgate1_NMOS_ChannelWidth'] = _Slv_Xgate1_NMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Xgate1_NMOS_ChannelLength'] = _Slv_Xgate1_NMOS_ChannelLength
        _Caculation_Parameters['_Slv_Xgate1_NMOS_XVT'] = _Slv_Xgate1_NMOS_XVT
        _Caculation_Parameters['_Slv_Xgate1_NMOS_POGate_Comb_length'] = _Slv_Xgate1_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters['_Slv_Xgate1_PMOS_NumberofGate'] = _Slv_Xgate1_PMOS_NumberofGate
        _Caculation_Parameters['_Slv_Xgate1_PMOS_ChannelWidth'] = _Slv_Xgate1_PMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Xgate1_PMOS_ChannelLength'] = _Slv_Xgate1_PMOS_ChannelLength
        _Caculation_Parameters['_Slv_Xgate1_PMOS_XVT'] = _Slv_Xgate1_PMOS_XVT
        _Caculation_Parameters['_Slv_Xgate1_PMOS_POGate_Comb_length'] = _Slv_Xgate1_PMOS_POGate_Comb_length

        ## Slave Xgate2
        ## Xgate NMOS
        _Caculation_Parameters['_Slv_Xgate2_NMOS_NumberofGate'] = _Slv_Xgate2_NMOS_NumberofGate
        _Caculation_Parameters['_Slv_Xgate2_NMOS_ChannelWidth'] = _Slv_Xgate2_NMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Xgate2_NMOS_ChannelLength'] = _Slv_Xgate2_NMOS_ChannelLength
        _Caculation_Parameters['_Slv_Xgate2_NMOS_XVT'] = _Slv_Xgate2_NMOS_XVT
        _Caculation_Parameters['_Slv_Xgate2_NMOS_POGate_Comb_length'] = _Slv_Xgate2_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters['_Slv_Xgate2_PMOS_NumberofGate'] = _Slv_Xgate2_PMOS_NumberofGate
        _Caculation_Parameters['_Slv_Xgate2_PMOS_ChannelWidth'] = _Slv_Xgate2_PMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Xgate2_PMOS_ChannelLength'] = _Slv_Xgate2_PMOS_ChannelLength
        _Caculation_Parameters['_Slv_Xgate2_PMOS_XVT'] = _Slv_Xgate2_PMOS_XVT
        _Caculation_Parameters['_Slv_Xgate2_PMOS_POGate_Comb_length'] = _Slv_Xgate2_PMOS_POGate_Comb_length

        ## Slave Nor1
        ## NMOS common
        _Caculation_Parameters['_Slv_Nor1_NMOS_XVT'] = _Slv_Nor1_NMOS_XVT

        ## Nor1 NMOSA
        _Caculation_Parameters['_Slv_Nor1_NMOSA_NumberofGate'] = _Slv_Nor1_NMOSA_NumberofGate
        _Caculation_Parameters['_Slv_Nor1_NMOSA_ChannelWidth'] = _Slv_Nor1_NMOSA_ChannelWidth
        _Caculation_Parameters['_Slv_Nor1_NMOSA_ChannelLength'] = _Slv_Nor1_NMOSA_ChannelLength
        _Caculation_Parameters['_Slv_Nor1_NMOSA_POGate_Comb_length'] = _Slv_Nor1_NMOSA_POGate_Comb_length

        ## Nor1 NMOSB
        _Caculation_Parameters['_Slv_Nor1_NMOSB_NumberofGate'] = _Slv_Nor1_NMOSB_NumberofGate
        _Caculation_Parameters['_Slv_Nor1_NMOSB_ChannelWidth'] = _Slv_Nor1_NMOSB_ChannelWidth
        _Caculation_Parameters['_Slv_Nor1_NMOSB_ChannelLength'] = _Slv_Nor1_NMOSB_ChannelLength
        _Caculation_Parameters['_Slv_Nor1_NMOSB_POGate_Comb_length'] = _Slv_Nor1_NMOSB_POGate_Comb_length

        ## PMOS common
        _Caculation_Parameters['_Slv_Nor1_PMOS_XVT'] = _Slv_Nor1_PMOS_XVT

        ## Nor1 PMOSA
        _Caculation_Parameters['_Slv_Nor1_PMOSA_NumberofGate'] = _Slv_Nor1_PMOSA_NumberofGate
        _Caculation_Parameters['_Slv_Nor1_PMOSA_ChannelWidth'] = _Slv_Nor1_PMOSA_ChannelWidth
        _Caculation_Parameters['_Slv_Nor1_PMOSA_ChannelLength'] = _Slv_Nor1_PMOSA_ChannelLength
        _Caculation_Parameters['_Slv_Nor1_PMOSA_POGate_Comb_length'] = _Slv_Nor1_PMOSA_POGate_Comb_length

        ## Nor1 PMOSB
        _Caculation_Parameters['_Slv_Nor1_PMOSB_NumberofGate'] = _Slv_Nor1_PMOSB_NumberofGate
        _Caculation_Parameters['_Slv_Nor1_PMOSB_ChannelWidth'] = _Slv_Nor1_PMOSB_ChannelWidth
        _Caculation_Parameters['_Slv_Nor1_PMOSB_ChannelLength'] = _Slv_Nor1_PMOSB_ChannelLength
        _Caculation_Parameters['_Slv_Nor1_PMOSB_POGate_Comb_length'] = _Slv_Nor1_PMOSB_POGate_Comb_length

        ## Slave Nor2
        ## NMOS common
        _Caculation_Parameters['_Slv_Nor2_NMOS_XVT'] = _Slv_Nor2_NMOS_XVT

        ## Nor2 NMOSA
        _Caculation_Parameters['_Slv_Nor2_NMOSA_NumberofGate'] = _Slv_Nor2_NMOSA_NumberofGate
        _Caculation_Parameters['_Slv_Nor2_NMOSA_ChannelWidth'] = _Slv_Nor2_NMOSA_ChannelWidth
        _Caculation_Parameters['_Slv_Nor2_NMOSA_ChannelLength'] = _Slv_Nor2_NMOSA_ChannelLength
        _Caculation_Parameters['_Slv_Nor2_NMOSA_POGate_Comb_length'] = _Slv_Nor2_NMOSA_POGate_Comb_length

        ## Nor2 NMOSB
        _Caculation_Parameters['_Slv_Nor2_NMOSB_NumberofGate'] = _Slv_Nor2_NMOSB_NumberofGate
        _Caculation_Parameters['_Slv_Nor2_NMOSB_ChannelWidth'] = _Slv_Nor2_NMOSB_ChannelWidth
        _Caculation_Parameters['_Slv_Nor2_NMOSB_ChannelLength'] = _Slv_Nor2_NMOSB_ChannelLength
        _Caculation_Parameters['_Slv_Nor2_NMOSB_POGate_Comb_length'] = _Slv_Nor2_NMOSB_POGate_Comb_length

        ## PMOS common
        _Caculation_Parameters['_Slv_Nor2_PMOS_XVT'] = _Slv_Nor2_PMOS_XVT

        ## Nor2 PMOSA
        _Caculation_Parameters['_Slv_Nor2_PMOSA_NumberofGate'] = _Slv_Nor2_PMOSA_NumberofGate
        _Caculation_Parameters['_Slv_Nor2_PMOSA_ChannelWidth'] = _Slv_Nor2_PMOSA_ChannelWidth
        _Caculation_Parameters['_Slv_Nor2_PMOSA_ChannelLength'] = _Slv_Nor2_PMOSA_ChannelLength
        _Caculation_Parameters['_Slv_Nor2_PMOSA_POGate_Comb_length'] = _Slv_Nor2_PMOSA_POGate_Comb_length

        ## Nor2 PMOSB
        _Caculation_Parameters['_Slv_Nor2_PMOSB_NumberofGate'] = _Slv_Nor2_PMOSB_NumberofGate
        _Caculation_Parameters['_Slv_Nor2_PMOSB_ChannelWidth'] = _Slv_Nor2_PMOSB_ChannelWidth
        _Caculation_Parameters['_Slv_Nor2_PMOSB_ChannelLength'] = _Slv_Nor2_PMOSB_ChannelLength
        _Caculation_Parameters['_Slv_Nor2_PMOSB_POGate_Comb_length'] = _Slv_Nor2_PMOSB_POGate_Comb_length

        ## Slave Inv1 : ReSet pre-driver
        ## Xgate NMOS
        _Caculation_Parameters['_Slv_Inv1_NMOS_NumberofGate'] = _Slv_Inv1_NMOS_NumberofGate
        _Caculation_Parameters['_Slv_Inv1_NMOS_ChannelWidth'] = _Slv_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Inv1_NMOS_ChannelLength'] = _Slv_Inv1_NMOS_ChannelLength
        _Caculation_Parameters['_Slv_Inv1_NMOS_XVT'] = _Slv_Inv1_NMOS_XVT
        _Caculation_Parameters['_Slv_Inv1_NMOS_POGate_Comb_length'] = _Slv_Inv1_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters['_Slv_Inv1_PMOS_NumberofGate'] = _Slv_Inv1_PMOS_NumberofGate
        _Caculation_Parameters['_Slv_Inv1_PMOS_ChannelWidth'] = _Slv_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Inv1_PMOS_ChannelLength'] = _Slv_Inv1_PMOS_ChannelLength
        _Caculation_Parameters['_Slv_Inv1_PMOS_XVT'] = _Slv_Inv1_PMOS_XVT
        _Caculation_Parameters['_Slv_Inv1_PMOS_POGate_Comb_length'] = _Slv_Inv1_PMOS_POGate_Comb_length

        ## Slave Inv2 : ReSet driver
        ## Xgate NMOS
        _Caculation_Parameters['_Slv_Inv2_NMOS_NumberofGate'] = _Slv_Inv2_NMOS_NumberofGate
        _Caculation_Parameters['_Slv_Inv2_NMOS_ChannelWidth'] = _Slv_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Inv2_NMOS_ChannelLength'] = _Slv_Inv2_NMOS_ChannelLength
        _Caculation_Parameters['_Slv_Inv2_NMOS_XVT'] = _Slv_Inv2_NMOS_XVT
        _Caculation_Parameters['_Slv_Inv2_NMOS_POGate_Comb_length'] = _Slv_Inv2_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters['_Slv_Inv2_PMOS_NumberofGate'] = _Slv_Inv2_PMOS_NumberofGate
        _Caculation_Parameters['_Slv_Inv2_PMOS_ChannelWidth'] = _Slv_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Inv2_PMOS_ChannelLength'] = _Slv_Inv2_PMOS_ChannelLength
        _Caculation_Parameters['_Slv_Inv2_PMOS_XVT'] = _Slv_Inv2_PMOS_XVT
        _Caculation_Parameters['_Slv_Inv2_PMOS_POGate_Comb_length'] = _Slv_Inv2_PMOS_POGate_Comb_length

        ## Slave Inv3 : Qb driver
        ## Xgate NMOS
        _Caculation_Parameters['_Slv_Inv3_NMOS_NumberofGate'] = _Slv_Inv3_NMOS_NumberofGate
        _Caculation_Parameters['_Slv_Inv3_NMOS_ChannelWidth'] = _Slv_Inv3_NMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Inv3_NMOS_ChannelLength'] = _Slv_Inv3_NMOS_ChannelLength
        _Caculation_Parameters['_Slv_Inv3_NMOS_XVT'] = _Slv_Inv3_NMOS_XVT
        _Caculation_Parameters['_Slv_Inv3_NMOS_POGate_Comb_length'] = _Slv_Inv3_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters['_Slv_Inv3_PMOS_NumberofGate'] = _Slv_Inv3_PMOS_NumberofGate
        _Caculation_Parameters['_Slv_Inv3_PMOS_ChannelWidth'] = _Slv_Inv3_PMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Inv3_PMOS_ChannelLength'] = _Slv_Inv3_PMOS_ChannelLength
        _Caculation_Parameters['_Slv_Inv3_PMOS_XVT'] = _Slv_Inv3_PMOS_XVT
        _Caculation_Parameters['_Slv_Inv3_PMOS_POGate_Comb_length'] = _Slv_Inv3_PMOS_POGate_Comb_length

        ## CLK Buf Tree Bot
        _Caculation_Parameters['_CLKBufTreeBot_NumOfStage'] = _CLKBufTreeBot_NumOfStage
        _Caculation_Parameters['_CLKBufTreeBot_CompOutBuf_SizeByStage'] = _CLKBufTreeBot_CompOutBuf_SizeByStage
        _Caculation_Parameters['_CLKBufTreeBot_CLKDoutBuf_SizeByStage'] = _CLKBufTreeBot_CLKDoutBuf_SizeByStage
        _Caculation_Parameters['_CLKBufTreeBot_XOffSet'] = _CLKBufTreeBot_XOffSet

        _Caculation_Parameters['_CLKBufTreeBot_Inv_NMOS_ChannelWidth'] = _CLKBufTreeBot_Inv_NMOS_ChannelWidth
        _Caculation_Parameters['_CLKBufTreeBot_Inv_NMOS_ChannelLength'] = _CLKBufTreeBot_Inv_NMOS_ChannelLength
        _Caculation_Parameters['_CLKBufTreeBot_Inv_NMOS_NumberofGate'] = _CLKBufTreeBot_Inv_NMOS_NumberofGate
        _Caculation_Parameters['_CLKBufTreeBot_Inv_NMOS_XVT'] = _CLKBufTreeBot_Inv_NMOS_XVT
        _Caculation_Parameters['_CLKBufTreeBot_Inv_NMOS_POGate_Comb_length'] = _CLKBufTreeBot_Inv_NMOS_POGate_Comb_length

        _Caculation_Parameters['_CLKBufTreeBot_Inv_PMOS_ChannelWidth'] = _CLKBufTreeBot_Inv_PMOS_ChannelWidth
        _Caculation_Parameters['_CLKBufTreeBot_Inv_PMOS_ChannelLength'] = _CLKBufTreeBot_Inv_PMOS_ChannelLength
        _Caculation_Parameters['_CLKBufTreeBot_Inv_PMOS_NumberofGate'] = _CLKBufTreeBot_Inv_PMOS_NumberofGate
        _Caculation_Parameters['_CLKBufTreeBot_Inv_PMOS_XVT'] = _CLKBufTreeBot_Inv_PMOS_XVT
        _Caculation_Parameters['_CLKBufTreeBot_Inv_PMOS_POGate_Comb_length'] = _CLKBufTreeBot_Inv_PMOS_POGate_Comb_length

        _Caculation_Parameters['_CLKBufTreeBot_NMOS_Pbody_NumCont'] = _CLKBufTreeBot_NMOS_Pbody_NumCont
        _Caculation_Parameters['_CLKBufTreeBot_NMOS_Pbody_XvtTop2Pbody'] = _CLKBufTreeBot_NMOS_Pbody_XvtTop2Pbody
        _Caculation_Parameters['_CLKBufTreeBot_PMOS_Nbody_NumCont'] = _CLKBufTreeBot_PMOS_Nbody_NumCont
        _Caculation_Parameters['_CLKBufTreeBot_PMOS_Nbody_Xvtdown2Nbody'] = _CLKBufTreeBot_PMOS_Nbody_Xvtdown2Nbody
        _Caculation_Parameters['_CLKBufTreeBot_PMOSXvt2NMOSXvt'] = _CLKBufTreeBot_PMOSXvt2NMOSXvt

        ## CLK Buf Tree Top
        _Caculation_Parameters['_CLKBufTreeTop_NumOfStage'] = _CLKBufTreeTop_NumOfStage
        _Caculation_Parameters['_CLKBufTreeTop_CLKSampBuf_SizeByStage'] = _CLKBufTreeTop_CLKSampBuf_SizeByStage
        _Caculation_Parameters['_CLKBufTreeTop_CLKSrcBuf_SizeByStage'] = _CLKBufTreeTop_CLKSrcBuf_SizeByStage
        _Caculation_Parameters['_CLKBufTreeTop_XOffSet'] = _CLKBufTreeTop_XOffSet

        _Caculation_Parameters['_CLKBufTreeTop_Inv_NMOS_ChannelWidth'] = _CLKBufTreeTop_Inv_NMOS_ChannelWidth
        _Caculation_Parameters['_CLKBufTreeTop_Inv_NMOS_ChannelLength'] = _CLKBufTreeTop_Inv_NMOS_ChannelLength
        _Caculation_Parameters['_CLKBufTreeTop_Inv_NMOS_NumberofGate'] = _CLKBufTreeTop_Inv_NMOS_NumberofGate
        _Caculation_Parameters['_CLKBufTreeTop_Inv_NMOS_XVT'] = _CLKBufTreeTop_Inv_NMOS_XVT
        _Caculation_Parameters['_CLKBufTreeTop_Inv_NMOS_POGate_Comb_length'] = _CLKBufTreeTop_Inv_NMOS_POGate_Comb_length

        _Caculation_Parameters['_CLKBufTreeTop_Inv_PMOS_ChannelWidth'] = _CLKBufTreeTop_Inv_PMOS_ChannelWidth
        _Caculation_Parameters['_CLKBufTreeTop_Inv_PMOS_ChannelLength'] = _CLKBufTreeTop_Inv_PMOS_ChannelLength
        _Caculation_Parameters['_CLKBufTreeTop_Inv_PMOS_NumberofGate'] = _CLKBufTreeTop_Inv_PMOS_NumberofGate
        _Caculation_Parameters['_CLKBufTreeTop_Inv_PMOS_XVT'] = _CLKBufTreeTop_Inv_PMOS_XVT
        _Caculation_Parameters['_CLKBufTreeTop_Inv_PMOS_POGate_Comb_length'] = _CLKBufTreeTop_Inv_PMOS_POGate_Comb_length

        _Caculation_Parameters['_CLKBufTreeTop_NMOS_Pbody_NumCont'] = _CLKBufTreeTop_NMOS_Pbody_NumCont
        _Caculation_Parameters['_CLKBufTreeTop_NMOS_Pbody_XvtTop2Pbody'] = _CLKBufTreeTop_NMOS_Pbody_XvtTop2Pbody
        _Caculation_Parameters['_CLKBufTreeTop_PMOS_Nbody_NumCont'] = _CLKBufTreeTop_PMOS_Nbody_NumCont
        _Caculation_Parameters['_CLKBufTreeTop_PMOS_Nbody_Xvtdown2Nbody'] = _CLKBufTreeTop_PMOS_Nbody_Xvtdown2Nbody
        _Caculation_Parameters['_CLKBufTreeTop_PMOSXvt2NMOSXvt'] = _CLKBufTreeTop_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_SARLogicWtCLKTree'] = self._SrefElementDeclaration(_DesignObj=K00_01_SARLogicWtCLKBufTree._SARLogicWtCLKBufTree(_DesignParameter=None, _Name='{}:SRF_SARLogicWtCLKTree'.format(_Name)))[0]

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SARLogicWtCLKTree']['_DesignObj']._CalculateDesignParameter(
            **_Caculation_Parameters)

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

        ###############################
        ## SRF_UpperCDACPreDriver Generation
        _Caculation_Parameters = copy.deepcopy(J00_02_CDAC_PreDriver_KJH._CDAC_PreDriver._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Distance'] = CDACPreDriver_Distance
        _Caculation_Parameters['_NumBit'] = _NumofBit
        _Caculation_Parameters['_Pbody_NumCont'] = _CDACPreDriver_Pbody_NumCont
        _Caculation_Parameters['_Nbody_NumCont'] = _CDACPreDriver_Nbody_NumCont
        _Caculation_Parameters['_PMOSXvt2NMOSXvt'] = _CDACPreDriver_PMOSXvt2NMOSXvt
        _Caculation_Parameters['_XvtTop2Pbody'] = _CDACPreDriver_XvtTop2Pbody
        _Caculation_Parameters['_Xvtdown2Nbody'] = _CDACPreDriver_Xvtdown2Nbody

        _Caculation_Parameters['_NumberofGate'] = _CDACPreDriver_NumberofGate
        _Caculation_Parameters['_ChannelLength'] = _CDACPreDriver_ChannelLength
        _Caculation_Parameters['_XVT'] = _CDACPreDriver_XVT

        _Caculation_Parameters['_Inv_NMOS_ChannelWidth'] = _CDACPreDriver_Inv_NMOS_ChannelWidth
        _Caculation_Parameters['_Inv_NMOS_POGate_Comb_length'] = _CDACPreDriver_Inv_NMOS_POGate_Comb_length
        _Caculation_Parameters['_Inv_PMOS_ChannelWidth'] = _CDACPreDriver_Inv_PMOS_ChannelWidth
        _Caculation_Parameters['_Inv_PMOS_POGate_Comb_length'] = _CDACPreDriver_Inv_PMOS_POGate_Comb_length

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
        tmp1x = self.get_param_KJH4('SRF_UpperCDACPreDriver', 'SRF_InvChain', 'SRF_Input_ViaM1Mx', 'SRF_ViaM1M2', 'BND_Met1Layer')
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

        ###############################
        ## SRF_LowerCDACPreDriver Generation
        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_LowerCDACPreDriver'] = self._SrefElementDeclaration(_DesignObj=J00_02_CDAC_PreDriver_KJH._CDAC_PreDriver(_DesignParameter=None, _Name='{}:SRF_LowerCDACPreDriver'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_LowerCDACPreDriver']['_Reflect'] = [1, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_LowerCDACPreDriver']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_LowerCDACPreDriver']['_DesignObj']._CalculateDesignParameter(
            **_Caculation_Parameters)

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
        tmp1x = self.get_param_KJH4('SRF_LowerCDACPreDriver', 'SRF_InvChain', 'SRF_Input_ViaM1Mx', 'SRF_ViaM1M2', 'BND_Met1Layer')
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
        tmp = self.get_param_KJH4('SRF_SARLogicWtCLKTree', 'SRF_SARLogic', 'SRF_DAC_Ctrl', 'SRF_Net21_ViaM1M3',
                                  'SRF_ViaM2M3', 'BND_Met2Layer')
        for i in range(_NumofBit):
            target_coord = tmp[0][0][i][0][0][0][0]['_XY_cent']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define
        self._DesignParameter['SRF_UpperCDACPreDrvIn_ViaM3M4']['_XYCoordinates'] = tmpXY

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
        tmp1 = self.get_param_KJH4('SRF_LowerCDACPreDriver', 'SRF_InvChain', 'SRF_Input_ViaM1Mx', 'SRF_ViaM1M2', 'BND_Met1Layer')
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
        tmp1 = self.get_param_KJH4('SRF_UpperCDACPreDriver', 'SRF_InvChain', 'SRF_Input_ViaM1Mx', 'SRF_ViaM1M2', 'BND_Met1Layer')
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

        ## SRF_CLKDout_Inv
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## INV
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  INV: Sref Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D00_00_Inverter_KJH._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType'] = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn'] = 'Up'

        _Caculation_Parameters['_NMOS_NumberofGate'] = _CLKDout_Inv_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth'] = _CLKDout_Inv_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength'] = _CLKDout_Inv_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing'] = None
        _Caculation_Parameters['_NMOS_SDWidth'] = None
        _Caculation_Parameters['_NMOS_XVT'] = _CLKDout_XVT_Common
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
        _Caculation_Parameters['_NMOS_POGate_Comb_length'] = _CLKDout_Inv_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF'] = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx'] = [0, 1]

        _Caculation_Parameters['_PMOS_MosType'] = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn'] = 'Dn'

        _Caculation_Parameters['_PMOS_NumberofGate'] = _CLKDout_Inv_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth'] = _CLKDout_Inv_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength'] = _CLKDout_Inv_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing'] = None
        _Caculation_Parameters['_PMOS_SDWidth'] = None
        _Caculation_Parameters['_PMOS_XVT'] = _CLKDout_XVT_Common
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
        _Caculation_Parameters['_PMOS_POGate_Comb_length'] = _CLKDout_Inv_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF'] = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx'] = [0, 1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont'] = 2
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody'] = 600
        _Caculation_Parameters['_PMOS_Nbody_NumCont'] = 2
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody'] = 1000
        _Caculation_Parameters['_PMOSXvt2NMOSXvt'] = 1000

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
        tmp1x = self.get_param_KJH4('SRF_SARLogicWtCLKTree', 'SRF_SARLogic', 'SRF_DAC_Ctrl', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'SRF_PMOS', 'BND_{}Layer'.format(_Slv_Inv3_PMOS_XVT))
        tmp1y = self.get_param_KJH4('SRF_SARLogicWtCLKTree', 'SRF_SARLogic', 'BND_Nbody_M1Exten')
        target_coord = [tmp1x[0][0][-1][0][0][0][0][0]['_XY_right'][0], tmp1y[0][0][0][0]['_XY_up'][1]]
        ## Approaching_coord
        tmp2x = self.get_param_KJH4('SRF_CLKDout_Inv', 'SRF_PMOS', 'BND_{}Layer'.format(_CLKDout_XVT_Common))
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

        ## SRF_CLKDOut_AND
        ### AND Gate SREF Generation
        _Caculation_Parameters = copy.deepcopy(E01_03_AND_YJH._AND._ParametersForDesignCalculation)
        _Caculation_Parameters['_AND_NAND_NMOS_ChannelWidth'] = _CLKDout_AND_NAND_NMOS_ChannelWidth
        _Caculation_Parameters['_AND_NAND_NMOS_ChannelLength'] = _CLKDout_AND_NAND_NMOS_ChannelLength
        _Caculation_Parameters['_AND_NAND_NMOS_NumberofGate'] = _CLKDout_AND_NAND_NMOS_NumberofGate
        _Caculation_Parameters['_AND_NAND_NMOS_XVT'] = _CLKDout_XVT_Common

        _Caculation_Parameters['_AND_NAND_PMOS_ChannelWidth'] = _CLKDout_AND_NAND_PMOS_ChannelWidth
        _Caculation_Parameters['_AND_NAND_PMOS_ChannelLength'] = _CLKDout_AND_NAND_PMOS_ChannelLength
        _Caculation_Parameters['_AND_NAND_PMOS_NumberofGate'] = _CLKDout_AND_NAND_PMOS_NumberofGate
        _Caculation_Parameters['_AND_NAND_PMOS_XVT'] = _CLKDout_XVT_Common

        _Caculation_Parameters['_AND_Inv_NMOS_ChannelWidth'] = _CLKDout_AND_Inv_NMOS_ChannelWidth
        _Caculation_Parameters['_AND_Inv_NMOS_ChannelLength'] = _CLKDout_AND_Inv_NMOS_ChannelLength
        _Caculation_Parameters['_AND_Inv_NMOS_NumberofGate'] = _CLKDout_AND_Inv_NMOS_NumberofGate
        _Caculation_Parameters['_AND_Inv_NMOS_XVT'] = _CLKDout_XVT_Common
        _Caculation_Parameters['_AND_Inv_NMOS_POGate_Comb_length'] = _CLKDout_AND_Inv_NMOS_POGate_Comb_length

        _Caculation_Parameters['_AND_Inv_PMOS_ChannelWidth'] = _CLKDout_AND_Inv_PMOS_ChannelWidth
        _Caculation_Parameters['_AND_Inv_PMOS_ChannelLength'] = _CLKDout_AND_Inv_PMOS_ChannelLength
        _Caculation_Parameters['_AND_Inv_PMOS_NumberofGate'] = _CLKDout_AND_Inv_PMOS_NumberofGate
        _Caculation_Parameters['_AND_Inv_PMOS_XVT'] = _CLKDout_XVT_Common
        _Caculation_Parameters['_AND_Inv_PMOS_POGate_Comb_length'] = _CLKDout_AND_Inv_PMOS_POGate_Comb_length

        _Caculation_Parameters['_AND_NMOS_Pbody_NumCont'] = 2
        _Caculation_Parameters['_AND_NMOS_Pbody_XvtTop2Pbody'] = 600
        _Caculation_Parameters['_AND_PMOS_Nbody_NumCont'] = 2
        _Caculation_Parameters['_AND_PMOS_Nbody_Xvtdown2Nbody'] = 1000
        _Caculation_Parameters['_AND_PMOSXvt2NMOSXvt'] = 1000

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKDout_AND'] = self._SrefElementDeclaration(_DesignObj=E01_03_AND_YJH._AND(_DesignParameter=None, _Name='{}:SRF_CLKDout_AND'.format(_Name)))[0]

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
        tmp1x = self.get_param_KJH4('SRF_CLKDout_Inv', 'SRF_PMOS', 'BND_{}Layer'.format(_CLKDout_XVT_Common))
        tmp1y = self.get_param_KJH4('SRF_CLKDout_Inv', 'SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        target_coord = [tmp1x[0][0][0][0]['_XY_right'][0], tmp1y[0][0][0][0][0]['_XY_up'][1]]
        ## Approaching_coord
        tmp2x = self.get_param_KJH4('SRF_CLKDout_AND', 'SRF_NAND', 'SRF_Pulldown', 'SRF_NMOSB', 'BND_{}Layer'.format(_CLKDout_XVT_Common))
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

        # ## BND_CLKSrc_CLKDoutInvIn_Hrz_M3
        #     ## Boundary_element Generation
        #         ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        # self._DesignParameter['BND_CLKSrc_CLKDoutInvIn_Hrz_M3'] = self._BoundaryElementDeclaration(
        # _Layer=DesignParameters._LayerMapping['METAL3'][0],
        # _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        # _XWidth=None,
        # _YWidth=None,
        # _XYCoordinates=[],
        # )
        #         ## Define Boundary_element _YWidth
        # self._DesignParameter['BND_CLKSrc_CLKDoutInvIn_Hrz_M3']['_YWidth'] = 50
        #
        #         ## Define Boundary_element _XWidth
        # tmp1 = self.get_param_KJH4('SRF_SARLogicWtCLKTree','SRF_SARLogic','SRF_DAC_Ctrl','SRF_Net12_ViaM1M4','SRF_ViaM2M3','BND_Met3Layer')
        # tmp2 = self.get_param_KJH4('SRF_CLKDout_AND','SRF_NAND','BND_InputA_Vtc_M1')
        # self._DesignParameter['BND_CLKSrc_CLKDoutInvIn_Hrz_M3']['_XWidth'] = abs(tmp1[0][0][-1][0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0]['_XY_left'][0])
        #
        #         ## Define Boundary_element _XYCoordinates
        # self._DesignParameter['BND_CLKSrc_CLKDoutInvIn_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
        #
        #             ## Calculate Sref XYcoord
        # tmpXY = []
        #                 ## Calculate
        #                     ## Target_coord: _XY_type1
        # target_coord = tmp1[0][0][-1][0][0][0][0]['_XY_up_left']
        #                     ## Approaching_coord: _XY_type2
        # tmp2 = self.get_param_KJH4('BND_CLKSrc_CLKDoutInvIn_Hrz_M3')
        # approaching_coord = tmp2[0][0]['_XY_up_left']
        #                     ## Sref coord
        # tmp3 = self.get_param_KJH4('BND_CLKSrc_CLKDoutInvIn_Hrz_M3')
        # Scoord = tmp3[0][0]['_XY_origin']
        #                     ## Cal
        # New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        # tmpXY.append(New_Scoord)
        #                     ## Define coordinates
        # self._DesignParameter['BND_CLKSrc_CLKDoutInvIn_Hrz_M3']['_XYCoordinates'] = tmpXY

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
        tmp2 = self.get_param_KJH4('SRF_CLKDout_AND', 'SRF_NAND', 'BND_InputA_Vtc_M1')
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
        self._DesignParameter['SRF_CLKSrc_CLKDoutANDIn_ViaM3M4']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)

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

        #### SRF_CLKSrcInvOut_ViaM2M1
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKSrcInvOut_ViaM1M2'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_CLKSrcInvOut_ViaM1M2'.format(_Name)))[0]

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
        tmp2 = self.get_param_KJH4('SRF_CLKDout_AND', 'SRF_NAND', 'BND_InputB_Vtc_M1')
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

        ## BND_XVTExtenOn CLKDout AND, Inverter (PMOS)
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOSXVTExtenOnCLKDoutANDInv'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[_CLKDout_XVT_Common][0],
            _Datatype=DesignParameters._LayerMapping[_CLKDout_XVT_Common][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKDout_AND', 'SRF_Inverter', 'SRF_PMOS', 'BND_{}Layer'.format(_CLKDout_XVT_Common))
        tmp2 = self.get_param_KJH4('SRF_CLKDout_Inv', 'SRF_PMOS', 'BND_{}Layer'.format(_CLKDout_XVT_Common))
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

        ## BND_XVTExtenOn CLKDout AND, Inverter (NMOS)
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NMOSXVTExtenOnCLKDoutANDInv'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[_CLKDout_XVT_Common][0],
            _Datatype=DesignParameters._LayerMapping[_CLKDout_XVT_Common][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKDout_AND', 'SRF_Inverter', 'SRF_NMOS', 'BND_{}Layer'.format(_CLKDout_XVT_Common))
        tmp2 = self.get_param_KJH4('SRF_CLKDout_Inv', 'SRF_NMOS', 'BND_{}Layer'.format(_CLKDout_XVT_Common))
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


############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_YJH
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ADC_K00_SARLogicWtCLKBufTree'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'K00_02_SARLogicWtCDACPreDriver'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        _NumofBit=3,

        _Test_distance=330,
        _Routing_width=50,
        _Routing_distance=80,

        _YWidthOfCLKSrc=100,
        _SpaceBtwCLKSrcAndCLKSamp=100,
        _YWidthOfCLKSamp=100,

        _YWidthOfCompOut=100,
        _SpaceBtwCompOutAndCLKDout=100,
        _YWidthOfCLKDout=100,

        ## DFF Common
        _DFF_Pbody_NumCont=2,  # number
        _DFF_Nbody_NumCont=2,  # number
        _DFF_PMOSXvt2NMOSXvt=1150,  # number
        _DFF_XvtTop2Pbody=None,  # number/None(Minimum)
        _DFF_Xvtdown2Nbody=None,  # number/None(Minimum)

        ## Master Xgate1
        ## Xgate common

        ## Xgate NMOS
        _Mst_Xgate1_NMOS_NumberofGate=1,  # 1
        _Mst_Xgate1_NMOS_ChannelWidth=200,  # 100
        _Mst_Xgate1_NMOS_ChannelLength=30,
        _Mst_Xgate1_NMOS_XVT='HVT',
        _Mst_Xgate1_NMOS_POGate_Comb_length=100,

        ## Xgate PMOS
        _Mst_Xgate1_PMOS_NumberofGate=1,  # 1
        _Mst_Xgate1_PMOS_ChannelWidth=400,  # 200
        _Mst_Xgate1_PMOS_ChannelLength=30,
        _Mst_Xgate1_PMOS_XVT='HVT',
        _Mst_Xgate1_PMOS_POGate_Comb_length=100,

        ## Master Xgate2
        ## Xgate common

        ## Xgate NMOS
        _Mst_Xgate2_NMOS_NumberofGate=1,
        _Mst_Xgate2_NMOS_ChannelWidth=200,
        _Mst_Xgate2_NMOS_ChannelLength=30,
        _Mst_Xgate2_NMOS_XVT='SLVT',
        _Mst_Xgate2_NMOS_POGate_Comb_length=100,

        ## Xgate PMOS
        _Mst_Xgate2_PMOS_NumberofGate=2,  # 2
        _Mst_Xgate2_PMOS_ChannelWidth=200,
        _Mst_Xgate2_PMOS_ChannelLength=30,
        _Mst_Xgate2_PMOS_XVT='SLVT',
        _Mst_Xgate2_PMOS_POGate_Comb_length=100,

        ## Master Nor1
        ## Nor1 common

        ## NMOS
        ## NMOS common
        _Mst_Nor1_NMOS_XVT='HVT',

        ## NMOSA
        _Mst_Nor1_NMOSA_NumberofGate=2,
        _Mst_Nor1_NMOSA_ChannelWidth=200,
        _Mst_Nor1_NMOSA_ChannelLength=30,
        _Mst_Nor1_NMOSA_POGate_Comb_length=100,

        ## NMOSB
        _Mst_Nor1_NMOSB_NumberofGate=2,
        _Mst_Nor1_NMOSB_ChannelWidth=200,
        _Mst_Nor1_NMOSB_ChannelLength=30,
        _Mst_Nor1_NMOSB_POGate_Comb_length=100,

        ## PMOS
        ## PMOS common
        _Mst_Nor1_PMOS_XVT='HVT',

        ## PMOSA
        _Mst_Nor1_PMOSA_NumberofGate=4,
        _Mst_Nor1_PMOSA_ChannelWidth=400,
        _Mst_Nor1_PMOSA_ChannelLength=30,
        _Mst_Nor1_PMOSA_POGate_Comb_length=100,

        ## PMOSB
        _Mst_Nor1_PMOSB_NumberofGate=4,
        _Mst_Nor1_PMOSB_ChannelWidth=400,
        _Mst_Nor1_PMOSB_ChannelLength=30,
        _Mst_Nor1_PMOSB_POGate_Comb_length=100,

        ## Master Nor2
        ## Nor2 common

        ## NMOS
        ## NMOS common
        _Mst_Nor2_NMOS_XVT='HVT',

        ## NMOSA
        _Mst_Nor2_NMOSA_NumberofGate=2,
        _Mst_Nor2_NMOSA_ChannelWidth=200,
        _Mst_Nor2_NMOSA_ChannelLength=30,
        _Mst_Nor2_NMOSA_POGate_Comb_length=100,

        ## NMOSB
        _Mst_Nor2_NMOSB_NumberofGate=2,
        _Mst_Nor2_NMOSB_ChannelWidth=200,
        _Mst_Nor2_NMOSB_ChannelLength=30,
        _Mst_Nor2_NMOSB_POGate_Comb_length=100,

        ## PMOS
        ## PMOS common
        _Mst_Nor2_PMOS_XVT='HVT',

        ## PMOSA
        _Mst_Nor2_PMOSA_NumberofGate=4,
        _Mst_Nor2_PMOSA_ChannelWidth=400,
        _Mst_Nor2_PMOSA_ChannelLength=30,
        _Mst_Nor2_PMOSA_POGate_Comb_length=100,

        ## PMOSB
        _Mst_Nor2_PMOSB_NumberofGate=4,
        _Mst_Nor2_PMOSB_ChannelWidth=400,
        _Mst_Nor2_PMOSB_ChannelLength=30,
        _Mst_Nor2_PMOSB_POGate_Comb_length=100,

        ## Master Inv1 : Set pre-driver
        ## Inv1 common

        ## Inv1 NMOS
        _Mst_Inv1_NMOS_NumberofGate=1,
        _Mst_Inv1_NMOS_ChannelWidth=200,
        _Mst_Inv1_NMOS_ChannelLength=30,
        _Mst_Inv1_NMOS_XVT='SLVT',
        _Mst_Inv1_NMOS_POGate_Comb_length=100,

        ## Inv1 PMOS
        _Mst_Inv1_PMOS_NumberofGate=1,
        _Mst_Inv1_PMOS_ChannelWidth=400,
        _Mst_Inv1_PMOS_ChannelLength=30,
        _Mst_Inv1_PMOS_XVT='SLVT',
        _Mst_Inv1_PMOS_POGate_Comb_length=100,

        ## Master Inv2 : Set driver
        ## Inv2 common

        ## Inv2 NMOS
        _Mst_Inv2_NMOS_NumberofGate=1,
        _Mst_Inv2_NMOS_ChannelWidth=200,
        _Mst_Inv2_NMOS_ChannelLength=30,
        _Mst_Inv2_NMOS_XVT='SLVT',
        _Mst_Inv2_NMOS_POGate_Comb_length=100,

        ## Inv2 PMOS
        _Mst_Inv2_PMOS_NumberofGate=1,
        _Mst_Inv2_PMOS_ChannelWidth=400,
        _Mst_Inv2_PMOS_ChannelLength=30,
        _Mst_Inv2_PMOS_XVT='SLVT',
        _Mst_Inv2_PMOS_POGate_Comb_length=100,

        ## Master Inv3 : Clock driver
        ## Inv3 common

        ## Inv3 NMOS
        _Mst_Inv3_NMOS_NumberofGate=1,
        _Mst_Inv3_NMOS_ChannelWidth=200,
        _Mst_Inv3_NMOS_ChannelLength=30,
        _Mst_Inv3_NMOS_XVT='SLVT',
        _Mst_Inv3_NMOS_POGate_Comb_length=100,

        ## Inv3 PMOS
        _Mst_Inv3_PMOS_NumberofGate=1,
        _Mst_Inv3_PMOS_ChannelWidth=400,
        _Mst_Inv3_PMOS_ChannelLength=30,
        _Mst_Inv3_PMOS_XVT='SLVT',
        _Mst_Inv3_PMOS_POGate_Comb_length=100,

        ## Slave Xgate1
        ## Xgate common

        ## Xgate NMOS
        _Slv_Xgate1_NMOS_NumberofGate=1,
        _Slv_Xgate1_NMOS_ChannelWidth=200,
        _Slv_Xgate1_NMOS_ChannelLength=30,
        _Slv_Xgate1_NMOS_XVT='HVT',
        _Slv_Xgate1_NMOS_POGate_Comb_length=100,

        ## Xgate NMOS
        _Slv_Xgate1_PMOS_NumberofGate=1,
        _Slv_Xgate1_PMOS_ChannelWidth=400,
        _Slv_Xgate1_PMOS_ChannelLength=30,
        _Slv_Xgate1_PMOS_XVT='HVT',
        _Slv_Xgate1_PMOS_POGate_Comb_length=100,

        ## Slave Xgate2
        ## Xgate common

        ## Xgate NMOS
        _Slv_Xgate2_NMOS_NumberofGate=1,
        _Slv_Xgate2_NMOS_ChannelWidth=200,
        _Slv_Xgate2_NMOS_ChannelLength=30,
        _Slv_Xgate2_NMOS_XVT='SLVT',
        _Slv_Xgate2_NMOS_POGate_Comb_length=100,

        ## Xgate NMOS
        _Slv_Xgate2_PMOS_NumberofGate=2,
        _Slv_Xgate2_PMOS_ChannelWidth=200,
        _Slv_Xgate2_PMOS_ChannelLength=30,
        _Slv_Xgate2_PMOS_XVT='SLVT',
        _Slv_Xgate2_PMOS_POGate_Comb_length=100,

        ## Slave Nor1
        ## Nor1 common

        ## NMOS
        ## NMOS common
        _Slv_Nor1_NMOS_XVT='HVT',

        ## NMOSA
        _Slv_Nor1_NMOSA_NumberofGate=2,
        _Slv_Nor1_NMOSA_ChannelWidth=200,
        _Slv_Nor1_NMOSA_ChannelLength=30,
        _Slv_Nor1_NMOSA_POGate_Comb_length=100,

        ## NMOSB
        _Slv_Nor1_NMOSB_NumberofGate=2,
        _Slv_Nor1_NMOSB_ChannelWidth=200,
        _Slv_Nor1_NMOSB_ChannelLength=30,
        _Slv_Nor1_NMOSB_POGate_Comb_length=100,

        ## PMOS
        ## PMOS common
        _Slv_Nor1_PMOS_XVT='HVT',

        ## PMOSA
        _Slv_Nor1_PMOSA_NumberofGate=4,
        _Slv_Nor1_PMOSA_ChannelWidth=400,
        _Slv_Nor1_PMOSA_ChannelLength=30,
        _Slv_Nor1_PMOSA_POGate_Comb_length=100,

        ## PMOSB
        _Slv_Nor1_PMOSB_NumberofGate=4,
        _Slv_Nor1_PMOSB_ChannelWidth=400,
        _Slv_Nor1_PMOSB_ChannelLength=30,
        _Slv_Nor1_PMOSB_POGate_Comb_length=100,

        ## Slave Nor2
        ## Nor2 common

        ## NMOS
        ## NMOS common
        _Slv_Nor2_NMOS_XVT='HVT',

        ## NMOSA
        _Slv_Nor2_NMOSA_NumberofGate=2,
        _Slv_Nor2_NMOSA_ChannelWidth=200,
        _Slv_Nor2_NMOSA_ChannelLength=30,
        _Slv_Nor2_NMOSA_POGate_Comb_length=100,

        ## NMOSB
        _Slv_Nor2_NMOSB_NumberofGate=2,
        _Slv_Nor2_NMOSB_ChannelWidth=200,
        _Slv_Nor2_NMOSB_ChannelLength=30,
        _Slv_Nor2_NMOSB_POGate_Comb_length=100,

        ## PMOS
        ## PMOS common
        _Slv_Nor2_PMOS_XVT='HVT',

        ## PMOSA
        _Slv_Nor2_PMOSA_NumberofGate=4,
        _Slv_Nor2_PMOSA_ChannelWidth=400,
        _Slv_Nor2_PMOSA_ChannelLength=30,
        _Slv_Nor2_PMOSA_POGate_Comb_length=100,

        ## PMOSB
        _Slv_Nor2_PMOSB_NumberofGate=4,
        _Slv_Nor2_PMOSB_ChannelWidth=400,
        _Slv_Nor2_PMOSB_ChannelLength=30,
        _Slv_Nor2_PMOSB_POGate_Comb_length=100,

        ## Slave Inv1 : ReSet pre-driver
        ## Inv1 common

        ## Inv1 NMOS
        _Slv_Inv1_NMOS_NumberofGate=1,
        _Slv_Inv1_NMOS_ChannelWidth=200,
        _Slv_Inv1_NMOS_ChannelLength=30,
        _Slv_Inv1_NMOS_XVT='SLVT',
        _Slv_Inv1_NMOS_POGate_Comb_length=100,

        ## Inv1 PMOS
        _Slv_Inv1_PMOS_NumberofGate=1,
        _Slv_Inv1_PMOS_ChannelWidth=400,
        _Slv_Inv1_PMOS_ChannelLength=30,
        _Slv_Inv1_PMOS_XVT='SLVT',
        _Slv_Inv1_PMOS_POGate_Comb_length=100,

        ## Slave Inv2 : ReSet driver
        ## Inv2 common

        ## Inv2 NMOS
        _Slv_Inv2_NMOS_NumberofGate=1,
        _Slv_Inv2_NMOS_ChannelWidth=300,
        _Slv_Inv2_NMOS_ChannelLength=30,
        _Slv_Inv2_NMOS_XVT='SLVT',
        _Slv_Inv2_NMOS_POGate_Comb_length=100,

        ## Inv2 PMOS
        _Slv_Inv2_PMOS_NumberofGate=1,
        _Slv_Inv2_PMOS_ChannelWidth=400,
        _Slv_Inv2_PMOS_ChannelLength=30,
        _Slv_Inv2_PMOS_XVT='SLVT',
        _Slv_Inv2_PMOS_POGate_Comb_length=100,

        ## Slave Inv3 : Qb driver
        ## Inv3 common

        ## Inv3 NMOS
        _Slv_Inv3_NMOS_NumberofGate=5,  # 1
        _Slv_Inv3_NMOS_ChannelWidth=200,
        _Slv_Inv3_NMOS_ChannelLength=30,
        _Slv_Inv3_NMOS_XVT='SLVT',
        _Slv_Inv3_NMOS_POGate_Comb_length=100,

        ## Inv3 PMOS
        _Slv_Inv3_PMOS_NumberofGate=5,  # 1
        _Slv_Inv3_PMOS_ChannelWidth=400,
        _Slv_Inv3_PMOS_ChannelLength=30,
        _Slv_Inv3_PMOS_XVT='SLVT',
        _Slv_Inv3_PMOS_POGate_Comb_length=100,

        # Top Clock  Tree Size
        _CLKBufTreeTop_NumOfStage=4,
        _CLKBufTreeTop_CLKSampBuf_SizeByStage=[1, 2, 4, 8],
        _CLKBufTreeTop_CLKSrcBuf_SizeByStage=[1, 2, 4, 8],  # 스테이지에 따른 버퍼 사이즈(UnitBuffer의 배수로 각 스테이지의 크기가 결정 됨.)
        _CLKBufTreeTop_XOffSet=-0,

        ## Top CLK Buffer Size
        _CLKBufTreeTop_Inv_NMOS_ChannelWidth=400,  # Number
        _CLKBufTreeTop_Inv_NMOS_ChannelLength=30,  # Number
        _CLKBufTreeTop_Inv_NMOS_NumberofGate=1,  # Number
        _CLKBufTreeTop_Inv_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _CLKBufTreeTop_Inv_NMOS_POGate_Comb_length=100,  # None/Number

        _CLKBufTreeTop_Inv_PMOS_ChannelWidth=800,  # Number
        _CLKBufTreeTop_Inv_PMOS_ChannelLength=30,  # Number
        _CLKBufTreeTop_Inv_PMOS_NumberofGate=1,  # Number
        _CLKBufTreeTop_Inv_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _CLKBufTreeTop_Inv_PMOS_POGate_Comb_length=100,  # None/Number

        # Top CLK BufferPowerRail Size
        _CLKBufTreeTop_NMOS_Pbody_NumCont=2,
        _CLKBufTreeTop_NMOS_Pbody_XvtTop2Pbody=None,
        _CLKBufTreeTop_PMOS_Nbody_NumCont=2,
        _CLKBufTreeTop_PMOS_Nbody_Xvtdown2Nbody=None,
        _CLKBufTreeTop_PMOSXvt2NMOSXvt=446,

        # Bottom Clock  Tree Size
        _CLKBufTreeBot_NumOfStage=4,
        _CLKBufTreeBot_CompOutBuf_SizeByStage=[1, 2, 4, 8],
        _CLKBufTreeBot_CLKDoutBuf_SizeByStage=[1, 2, 4, 8],  # 스테이지에 따른 버퍼 사이즈(UnitBuffer의 배수로 각 스테이지의 크기가 결정 됨.)
        _CLKBufTreeBot_XOffSet=0,

        ## Bottom CLK Buffer Size
        _CLKBufTreeBot_Inv_NMOS_ChannelWidth=400,  # Number
        _CLKBufTreeBot_Inv_NMOS_ChannelLength=30,  # Number
        _CLKBufTreeBot_Inv_NMOS_NumberofGate=1,  # Number
        _CLKBufTreeBot_Inv_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _CLKBufTreeBot_Inv_NMOS_POGate_Comb_length=100,  # None/Number

        _CLKBufTreeBot_Inv_PMOS_ChannelWidth=800,  # Number
        _CLKBufTreeBot_Inv_PMOS_ChannelLength=30,  # Number
        _CLKBufTreeBot_Inv_PMOS_NumberofGate=1,  # Number
        _CLKBufTreeBot_Inv_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _CLKBufTreeBot_Inv_PMOS_POGate_Comb_length=100,  # None/Number

        # Bottom CLK Buffer PowerRail Size
        _CLKBufTreeBot_NMOS_Pbody_NumCont=2,
        _CLKBufTreeBot_NMOS_Pbody_XvtTop2Pbody=None,
        _CLKBufTreeBot_PMOS_Nbody_NumCont=2,
        _CLKBufTreeBot_PMOS_Nbody_Xvtdown2Nbody=None,
        _CLKBufTreeBot_PMOSXvt2NMOSXvt=446,

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
