## Import Basic Modules
    ## Engine
#from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import StickDiagram
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import DesignParameters
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import DRC

    ## Library
import copy
import time
import numpy as np

    ## KJH91 Basic Building Blocks
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import Slicer
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A14_Mosfet_KJH2
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.K00_SARLogicWtBuffers_YJH import K00_00_SARLogic_KJH1_v2_random
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.F00_CLKBufferTree_YJH import F00_02_CLKBufferTree_v2


## Define Class
class _SARLogicWtCLKBufTree(StickDiagram_KJH1._StickDiagram_KJH):
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
                                  # _CLKBufTreeTop_TotalLength=50000,
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
                                  # _CLKBufTreeBot_TotalLength=50000,
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

        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters1 = copy.deepcopy(K00_00_SARLogic_KJH1_v2_random._SARLogic._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters1['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters1['_NumofBit'] = _NumofBit
        _Caculation_Parameters1['_Test_distance'] = _Test_distance
        _Caculation_Parameters1['_Routing_width'] = _Routing_width
        _Caculation_Parameters1['_Routing_distance'] = _Routing_distance

        _Caculation_Parameters1['_SpaceBtwPbodyAndCLKSrc'] = 100
        _Caculation_Parameters1['_YWidthOfCLKSrc'] = _YWidthOfCLKSrc
        _Caculation_Parameters1['_SpaceBtwCLKSrcAndCLKSamp'] = _SpaceBtwCLKSrcAndCLKSamp
        _Caculation_Parameters1['_YWidthOfCLKSamp'] = _YWidthOfCLKSamp
        _Caculation_Parameters1['_SpaceBtwNbody2AndCompOut'] = 100
        _Caculation_Parameters1['_YWidthOfCompOut'] = _YWidthOfCompOut
        _Caculation_Parameters1['_SpaceBtwCompOutAndCLKDout'] = _SpaceBtwCompOutAndCLKDout
        _Caculation_Parameters1['_YWidthOfCLKDout'] = _YWidthOfCLKDout

        ## DFF Common
        _Caculation_Parameters1['_DFF_Pbody_NumCont'] = _DFF_Pbody_NumCont
        _Caculation_Parameters1['_DFF_Nbody_NumCont'] = _DFF_Nbody_NumCont
        _Caculation_Parameters1['_DFF_PMOSXvt2NMOSXvt'] = _DFF_PMOSXvt2NMOSXvt
        _Caculation_Parameters1['_DFF_XvtTop2Pbody'] = _DFF_XvtTop2Pbody
        _Caculation_Parameters1['_DFF_Xvtdown2Nbody'] = _DFF_Xvtdown2Nbody

        ## Master Xgate1
        ## Xgate NMOS
        _Caculation_Parameters1['_Mst_Xgate1_NMOS_NumberofGate'] = _Mst_Xgate1_NMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Xgate1_NMOS_ChannelWidth'] = _Mst_Xgate1_NMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Xgate1_NMOS_ChannelLength'] = _Mst_Xgate1_NMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Xgate1_NMOS_XVT'] = _Mst_Xgate1_NMOS_XVT
        _Caculation_Parameters1['_Mst_Xgate1_NMOS_POGate_Comb_length'] = _Mst_Xgate1_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_Mst_Xgate1_PMOS_NumberofGate'] = _Mst_Xgate1_PMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Xgate1_PMOS_ChannelWidth'] = _Mst_Xgate1_PMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Xgate1_PMOS_ChannelLength'] = _Mst_Xgate1_PMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Xgate1_PMOS_XVT'] = _Mst_Xgate1_PMOS_XVT
        _Caculation_Parameters1['_Mst_Xgate1_PMOS_POGate_Comb_length'] = _Mst_Xgate1_PMOS_POGate_Comb_length

        ## Master Xgate2
        ## Xgate NMOS
        _Caculation_Parameters1['_Mst_Xgate2_NMOS_NumberofGate'] = _Mst_Xgate2_NMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Xgate2_NMOS_ChannelWidth'] = _Mst_Xgate2_NMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Xgate2_NMOS_ChannelLength'] = _Mst_Xgate2_NMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Xgate2_NMOS_XVT'] = _Mst_Xgate2_NMOS_XVT
        _Caculation_Parameters1['_Mst_Xgate2_NMOS_POGate_Comb_length'] = _Mst_Xgate2_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_Mst_Xgate2_PMOS_NumberofGate'] = _Mst_Xgate2_PMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Xgate2_PMOS_ChannelWidth'] = _Mst_Xgate2_PMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Xgate2_PMOS_ChannelLength'] = _Mst_Xgate2_PMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Xgate2_PMOS_XVT'] = _Mst_Xgate2_PMOS_XVT
        _Caculation_Parameters1['_Mst_Xgate2_PMOS_POGate_Comb_length'] = _Mst_Xgate2_PMOS_POGate_Comb_length

        ## Master Nor1
        ## NMOS common
        _Caculation_Parameters1['_Mst_Nor1_NMOS_XVT'] = _Mst_Nor1_NMOS_XVT

        ## Nor1 NMOSA
        _Caculation_Parameters1['_Mst_Nor1_NMOSA_NumberofGate'] = _Mst_Nor1_NMOSA_NumberofGate
        _Caculation_Parameters1['_Mst_Nor1_NMOSA_ChannelWidth'] = _Mst_Nor1_NMOSA_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor1_NMOSA_ChannelLength'] = _Mst_Nor1_NMOSA_ChannelLength
        _Caculation_Parameters1['_Mst_Nor1_NMOSA_POGate_Comb_length'] = _Mst_Nor1_NMOSA_POGate_Comb_length

        ## Nor1 NMOSB
        _Caculation_Parameters1['_Mst_Nor1_NMOSB_NumberofGate'] = _Mst_Nor1_NMOSB_NumberofGate
        _Caculation_Parameters1['_Mst_Nor1_NMOSB_ChannelWidth'] = _Mst_Nor1_NMOSB_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor1_NMOSB_ChannelLength'] = _Mst_Nor1_NMOSB_ChannelLength
        _Caculation_Parameters1['_Mst_Nor1_NMOSB_POGate_Comb_length'] = _Mst_Nor1_NMOSB_POGate_Comb_length

        ## PMOS common
        _Caculation_Parameters1['_Mst_Nor1_PMOS_XVT'] = _Mst_Nor1_PMOS_XVT

        ## Nor1 PMOSA
        _Caculation_Parameters1['_Mst_Nor1_PMOSA_NumberofGate'] = _Mst_Nor1_PMOSA_NumberofGate
        _Caculation_Parameters1['_Mst_Nor1_PMOSA_ChannelWidth'] = _Mst_Nor1_PMOSA_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor1_PMOSA_ChannelLength'] = _Mst_Nor1_PMOSA_ChannelLength
        _Caculation_Parameters1['_Mst_Nor1_PMOSA_POGate_Comb_length'] = _Mst_Nor1_PMOSA_POGate_Comb_length

        ## Nor1 PMOSB
        _Caculation_Parameters1['_Mst_Nor1_PMOSB_NumberofGate'] = _Mst_Nor1_PMOSB_NumberofGate
        _Caculation_Parameters1['_Mst_Nor1_PMOSB_ChannelWidth'] = _Mst_Nor1_PMOSB_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor1_PMOSB_ChannelLength'] = _Mst_Nor1_PMOSB_ChannelLength
        _Caculation_Parameters1['_Mst_Nor1_PMOSB_POGate_Comb_length'] = _Mst_Nor1_PMOSB_POGate_Comb_length

        ## Master Nor2
        ## NMOS common
        _Caculation_Parameters1['_Mst_Nor2_NMOS_XVT'] = _Mst_Nor2_NMOS_XVT

        ## Nor2 NMOSA
        _Caculation_Parameters1['_Mst_Nor2_NMOSA_NumberofGate'] = _Mst_Nor2_NMOSA_NumberofGate
        _Caculation_Parameters1['_Mst_Nor2_NMOSA_ChannelWidth'] = _Mst_Nor2_NMOSA_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor2_NMOSA_ChannelLength'] = _Mst_Nor2_NMOSA_ChannelLength
        _Caculation_Parameters1['_Mst_Nor2_NMOSA_POGate_Comb_length'] = _Mst_Nor2_NMOSA_POGate_Comb_length

        ## Nor2 NMOSB
        _Caculation_Parameters1['_Mst_Nor2_NMOSB_NumberofGate'] = _Mst_Nor2_NMOSB_NumberofGate
        _Caculation_Parameters1['_Mst_Nor2_NMOSB_ChannelWidth'] = _Mst_Nor2_NMOSB_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor2_NMOSB_ChannelLength'] = _Mst_Nor2_NMOSB_ChannelLength
        _Caculation_Parameters1['_Mst_Nor2_NMOSB_POGate_Comb_length'] = _Mst_Nor2_NMOSB_POGate_Comb_length

        ## PMOS common
        _Caculation_Parameters1['_Mst_Nor2_PMOS_XVT'] = _Mst_Nor2_PMOS_XVT

        ## Nor2 PMOSA
        _Caculation_Parameters1['_Mst_Nor2_PMOSA_NumberofGate'] = _Mst_Nor2_PMOSA_NumberofGate
        _Caculation_Parameters1['_Mst_Nor2_PMOSA_ChannelWidth'] = _Mst_Nor2_PMOSA_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor2_PMOSA_ChannelLength'] = _Mst_Nor2_PMOSA_ChannelLength
        _Caculation_Parameters1['_Mst_Nor2_PMOSA_POGate_Comb_length'] = _Mst_Nor2_PMOSA_POGate_Comb_length

        ## Nor2 PMOSB
        _Caculation_Parameters1['_Mst_Nor2_PMOSB_NumberofGate'] = _Mst_Nor2_PMOSB_NumberofGate
        _Caculation_Parameters1['_Mst_Nor2_PMOSB_ChannelWidth'] = _Mst_Nor2_PMOSB_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor2_PMOSB_ChannelLength'] = _Mst_Nor2_PMOSB_ChannelLength
        _Caculation_Parameters1['_Mst_Nor2_PMOSB_POGate_Comb_length'] = _Mst_Nor2_PMOSB_POGate_Comb_length

        ## Master Inv1
        ## Xgate NMOS
        _Caculation_Parameters1['_Mst_Inv1_NMOS_NumberofGate'] = _Mst_Inv1_NMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Inv1_NMOS_ChannelWidth'] = _Mst_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Inv1_NMOS_ChannelLength'] = _Mst_Inv1_NMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Inv1_NMOS_XVT'] = _Mst_Inv1_NMOS_XVT
        _Caculation_Parameters1['_Mst_Inv1_NMOS_POGate_Comb_length'] = _Mst_Inv1_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_Mst_Inv1_PMOS_NumberofGate'] = _Mst_Inv1_PMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Inv1_PMOS_ChannelWidth'] = _Mst_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Inv1_PMOS_ChannelLength'] = _Mst_Inv1_PMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Inv1_PMOS_XVT'] = _Mst_Inv1_PMOS_XVT
        _Caculation_Parameters1['_Mst_Inv1_PMOS_POGate_Comb_length'] = _Mst_Inv1_PMOS_POGate_Comb_length

        ## Master Inv2 : Set driver
        ## Xgate NMOS
        _Caculation_Parameters1['_Mst_Inv2_NMOS_NumberofGate'] = _Mst_Inv2_NMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Inv2_NMOS_ChannelWidth'] = _Mst_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Inv2_NMOS_ChannelLength'] = _Mst_Inv2_NMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Inv2_NMOS_XVT'] = _Mst_Inv2_NMOS_XVT
        _Caculation_Parameters1['_Mst_Inv2_NMOS_POGate_Comb_length'] = _Mst_Inv2_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_Mst_Inv2_PMOS_NumberofGate'] = _Mst_Inv2_PMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Inv2_PMOS_ChannelWidth'] = _Mst_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Inv2_PMOS_ChannelLength'] = _Mst_Inv2_PMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Inv2_PMOS_XVT'] = _Mst_Inv2_PMOS_XVT
        _Caculation_Parameters1['_Mst_Inv2_PMOS_POGate_Comb_length'] = _Mst_Inv2_PMOS_POGate_Comb_length

        ## Master Inv3 : Clock driver
        ## Xgate NMOS
        _Caculation_Parameters1['_Mst_Inv3_NMOS_NumberofGate'] = _Mst_Inv3_NMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Inv3_NMOS_ChannelWidth'] = _Mst_Inv3_NMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Inv3_NMOS_ChannelLength'] = _Mst_Inv3_NMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Inv3_NMOS_XVT'] = _Mst_Inv3_NMOS_XVT
        _Caculation_Parameters1['_Mst_Inv3_NMOS_POGate_Comb_length'] = _Mst_Inv3_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_Mst_Inv3_PMOS_NumberofGate'] = _Mst_Inv3_PMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Inv3_PMOS_ChannelWidth'] = _Mst_Inv3_PMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Inv3_PMOS_ChannelLength'] = _Mst_Inv3_PMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Inv3_PMOS_XVT'] = _Mst_Inv3_PMOS_XVT
        _Caculation_Parameters1['_Mst_Inv3_PMOS_POGate_Comb_length'] = _Mst_Inv3_PMOS_POGate_Comb_length

        ## Slave Xgate1
        ## Xgate NMOS
        _Caculation_Parameters1['_Slv_Xgate1_NMOS_NumberofGate'] = _Slv_Xgate1_NMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Xgate1_NMOS_ChannelWidth'] = _Slv_Xgate1_NMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Xgate1_NMOS_ChannelLength'] = _Slv_Xgate1_NMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Xgate1_NMOS_XVT'] = _Slv_Xgate1_NMOS_XVT
        _Caculation_Parameters1['_Slv_Xgate1_NMOS_POGate_Comb_length'] = _Slv_Xgate1_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_Slv_Xgate1_PMOS_NumberofGate'] = _Slv_Xgate1_PMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Xgate1_PMOS_ChannelWidth'] = _Slv_Xgate1_PMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Xgate1_PMOS_ChannelLength'] = _Slv_Xgate1_PMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Xgate1_PMOS_XVT'] = _Slv_Xgate1_PMOS_XVT
        _Caculation_Parameters1['_Slv_Xgate1_PMOS_POGate_Comb_length'] = _Slv_Xgate1_PMOS_POGate_Comb_length

        ## Slave Xgate2
        ## Xgate NMOS
        _Caculation_Parameters1['_Slv_Xgate2_NMOS_NumberofGate'] = _Slv_Xgate2_NMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Xgate2_NMOS_ChannelWidth'] = _Slv_Xgate2_NMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Xgate2_NMOS_ChannelLength'] = _Slv_Xgate2_NMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Xgate2_NMOS_XVT'] = _Slv_Xgate2_NMOS_XVT
        _Caculation_Parameters1['_Slv_Xgate2_NMOS_POGate_Comb_length'] = _Slv_Xgate2_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_Slv_Xgate2_PMOS_NumberofGate'] = _Slv_Xgate2_PMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Xgate2_PMOS_ChannelWidth'] = _Slv_Xgate2_PMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Xgate2_PMOS_ChannelLength'] = _Slv_Xgate2_PMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Xgate2_PMOS_XVT'] = _Slv_Xgate2_PMOS_XVT
        _Caculation_Parameters1['_Slv_Xgate2_PMOS_POGate_Comb_length'] = _Slv_Xgate2_PMOS_POGate_Comb_length

        ## Slave Nor1
        ## NMOS common
        _Caculation_Parameters1['_Slv_Nor1_NMOS_XVT'] = _Slv_Nor1_NMOS_XVT

        ## Nor1 NMOSA
        _Caculation_Parameters1['_Slv_Nor1_NMOSA_NumberofGate'] = _Slv_Nor1_NMOSA_NumberofGate
        _Caculation_Parameters1['_Slv_Nor1_NMOSA_ChannelWidth'] = _Slv_Nor1_NMOSA_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor1_NMOSA_ChannelLength'] = _Slv_Nor1_NMOSA_ChannelLength
        _Caculation_Parameters1['_Slv_Nor1_NMOSA_POGate_Comb_length'] = _Slv_Nor1_NMOSA_POGate_Comb_length

        ## Nor1 NMOSB
        _Caculation_Parameters1['_Slv_Nor1_NMOSB_NumberofGate'] = _Slv_Nor1_NMOSB_NumberofGate
        _Caculation_Parameters1['_Slv_Nor1_NMOSB_ChannelWidth'] = _Slv_Nor1_NMOSB_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor1_NMOSB_ChannelLength'] = _Slv_Nor1_NMOSB_ChannelLength
        _Caculation_Parameters1['_Slv_Nor1_NMOSB_POGate_Comb_length'] = _Slv_Nor1_NMOSB_POGate_Comb_length

        ## PMOS common
        _Caculation_Parameters1['_Slv_Nor1_PMOS_XVT'] = _Slv_Nor1_PMOS_XVT

        ## Nor1 PMOSA
        _Caculation_Parameters1['_Slv_Nor1_PMOSA_NumberofGate'] = _Slv_Nor1_PMOSA_NumberofGate
        _Caculation_Parameters1['_Slv_Nor1_PMOSA_ChannelWidth'] = _Slv_Nor1_PMOSA_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor1_PMOSA_ChannelLength'] = _Slv_Nor1_PMOSA_ChannelLength
        _Caculation_Parameters1['_Slv_Nor1_PMOSA_POGate_Comb_length'] = _Slv_Nor1_PMOSA_POGate_Comb_length

        ## Nor1 PMOSB
        _Caculation_Parameters1['_Slv_Nor1_PMOSB_NumberofGate'] = _Slv_Nor1_PMOSB_NumberofGate
        _Caculation_Parameters1['_Slv_Nor1_PMOSB_ChannelWidth'] = _Slv_Nor1_PMOSB_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor1_PMOSB_ChannelLength'] = _Slv_Nor1_PMOSB_ChannelLength
        _Caculation_Parameters1['_Slv_Nor1_PMOSB_POGate_Comb_length'] = _Slv_Nor1_PMOSB_POGate_Comb_length

        ## Slave Nor2
        ## NMOS common
        _Caculation_Parameters1['_Slv_Nor2_NMOS_XVT'] = _Slv_Nor2_NMOS_XVT

        ## Nor2 NMOSA
        _Caculation_Parameters1['_Slv_Nor2_NMOSA_NumberofGate'] = _Slv_Nor2_NMOSA_NumberofGate
        _Caculation_Parameters1['_Slv_Nor2_NMOSA_ChannelWidth'] = _Slv_Nor2_NMOSA_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor2_NMOSA_ChannelLength'] = _Slv_Nor2_NMOSA_ChannelLength
        _Caculation_Parameters1['_Slv_Nor2_NMOSA_POGate_Comb_length'] = _Slv_Nor2_NMOSA_POGate_Comb_length

        ## Nor2 NMOSB
        _Caculation_Parameters1['_Slv_Nor2_NMOSB_NumberofGate'] = _Slv_Nor2_NMOSB_NumberofGate
        _Caculation_Parameters1['_Slv_Nor2_NMOSB_ChannelWidth'] = _Slv_Nor2_NMOSB_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor2_NMOSB_ChannelLength'] = _Slv_Nor2_NMOSB_ChannelLength
        _Caculation_Parameters1['_Slv_Nor2_NMOSB_POGate_Comb_length'] = _Slv_Nor2_NMOSB_POGate_Comb_length

        ## PMOS common
        _Caculation_Parameters1['_Slv_Nor2_PMOS_XVT'] = _Slv_Nor2_PMOS_XVT

        ## Nor2 PMOSA
        _Caculation_Parameters1['_Slv_Nor2_PMOSA_NumberofGate'] = _Slv_Nor2_PMOSA_NumberofGate
        _Caculation_Parameters1['_Slv_Nor2_PMOSA_ChannelWidth'] = _Slv_Nor2_PMOSA_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor2_PMOSA_ChannelLength'] = _Slv_Nor2_PMOSA_ChannelLength
        _Caculation_Parameters1['_Slv_Nor2_PMOSA_POGate_Comb_length'] = _Slv_Nor2_PMOSA_POGate_Comb_length

        ## Nor2 PMOSB
        _Caculation_Parameters1['_Slv_Nor2_PMOSB_NumberofGate'] = _Slv_Nor2_PMOSB_NumberofGate
        _Caculation_Parameters1['_Slv_Nor2_PMOSB_ChannelWidth'] = _Slv_Nor2_PMOSB_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor2_PMOSB_ChannelLength'] = _Slv_Nor2_PMOSB_ChannelLength
        _Caculation_Parameters1['_Slv_Nor2_PMOSB_POGate_Comb_length'] = _Slv_Nor2_PMOSB_POGate_Comb_length

        ## Slave Inv1 : ReSet pre-driver
        ## Xgate NMOS
        _Caculation_Parameters1['_Slv_Inv1_NMOS_NumberofGate'] = _Slv_Inv1_NMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Inv1_NMOS_ChannelWidth'] = _Slv_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Inv1_NMOS_ChannelLength'] = _Slv_Inv1_NMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Inv1_NMOS_XVT'] = _Slv_Inv1_NMOS_XVT
        _Caculation_Parameters1['_Slv_Inv1_NMOS_POGate_Comb_length'] = _Slv_Inv1_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_Slv_Inv1_PMOS_NumberofGate'] = _Slv_Inv1_PMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Inv1_PMOS_ChannelWidth'] = _Slv_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Inv1_PMOS_ChannelLength'] = _Slv_Inv1_PMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Inv1_PMOS_XVT'] = _Slv_Inv1_PMOS_XVT
        _Caculation_Parameters1['_Slv_Inv1_PMOS_POGate_Comb_length'] = _Slv_Inv1_PMOS_POGate_Comb_length

        ## Slave Inv2 : ReSet driver
        ## Xgate NMOS
        _Caculation_Parameters1['_Slv_Inv2_NMOS_NumberofGate'] = _Slv_Inv2_NMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Inv2_NMOS_ChannelWidth'] = _Slv_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Inv2_NMOS_ChannelLength'] = _Slv_Inv2_NMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Inv2_NMOS_XVT'] = _Slv_Inv2_NMOS_XVT
        _Caculation_Parameters1['_Slv_Inv2_NMOS_POGate_Comb_length'] = _Slv_Inv2_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_Slv_Inv2_PMOS_NumberofGate'] = _Slv_Inv2_PMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Inv2_PMOS_ChannelWidth'] = _Slv_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Inv2_PMOS_ChannelLength'] = _Slv_Inv2_PMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Inv2_PMOS_XVT'] = _Slv_Inv2_PMOS_XVT
        _Caculation_Parameters1['_Slv_Inv2_PMOS_POGate_Comb_length'] = _Slv_Inv2_PMOS_POGate_Comb_length

        ## Slave Inv3 : Qb driver
        ## Xgate NMOS
        _Caculation_Parameters1['_Slv_Inv3_NMOS_NumberofGate'] = _Slv_Inv3_NMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Inv3_NMOS_ChannelWidth'] = _Slv_Inv3_NMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Inv3_NMOS_ChannelLength'] = _Slv_Inv3_NMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Inv3_NMOS_XVT'] = _Slv_Inv3_NMOS_XVT
        _Caculation_Parameters1['_Slv_Inv3_NMOS_POGate_Comb_length'] = _Slv_Inv3_NMOS_POGate_Comb_length

        ## Xgate PMOS
        _Caculation_Parameters1['_Slv_Inv3_PMOS_NumberofGate'] = _Slv_Inv3_PMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Inv3_PMOS_ChannelWidth'] = _Slv_Inv3_PMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Inv3_PMOS_ChannelLength'] = _Slv_Inv3_PMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Inv3_PMOS_XVT'] = _Slv_Inv3_PMOS_XVT
        _Caculation_Parameters1['_Slv_Inv3_PMOS_POGate_Comb_length'] = _Slv_Inv3_PMOS_POGate_Comb_length

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## DAC Controller Gen.
        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_SARLogic'] = self._SrefElementDeclaration(_DesignObj=K00_00_SARLogic_KJH1_v2_random._SARLogic(_DesignParameter=None, _Name='{}:SRF_SARLogic'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_SARLogic']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SARLogic']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SARLogic']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters1)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SARLogic']['_XYCoordinates'] = [[0, 0]]

        ## Pre_Calculated Value 4 generate CLK Buffers
        tmp1 = self.get_param_KJH4('SRF_SARLogic', 'BND_Pbody_M1Exten')
        PbodyXWidthSARLogic = tmp1[0][0][0]['_Xwidth']

        ####### Top CLK Buffer Tree2 SRF Generation
        _Caculation_Parameters = copy.deepcopy(F00_02_CLKBufferTree_v2._CLKBufferTree._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_CLKBufTree_TotalLength'] = PbodyXWidthSARLogic
        _Caculation_Parameters['_CLKBufTree_NumOfStage'] = _CLKBufTreeTop_NumOfStage
        _Caculation_Parameters['_CLKBufTree_Buf1_SizeByStage'] = _CLKBufTreeTop_CLKSampBuf_SizeByStage
        _Caculation_Parameters['_CLKBufTree_Buf2_SizeByStage'] = _CLKBufTreeTop_CLKSampBuf_SizeByStage
        _Caculation_Parameters['_CLKBufTree_OutputVia'] = None
        _Caculation_Parameters['_CLKBufTree_OutputPlacement'] = 'Dn'

        _Caculation_Parameters['_CLKBufTree_Inv_NMOS_ChannelWidth'] = _CLKBufTreeTop_Inv_NMOS_ChannelWidth
        _Caculation_Parameters['_CLKBufTree_Inv_NMOS_ChannelLength'] = _CLKBufTreeTop_Inv_NMOS_ChannelLength
        _Caculation_Parameters['_CLKBufTree_Inv_NMOS_NumberofGate'] = _CLKBufTreeTop_Inv_NMOS_NumberofGate
        _Caculation_Parameters['_CLKBufTree_Inv_NMOS_XVT'] = _CLKBufTreeTop_Inv_NMOS_XVT
        _Caculation_Parameters['_CLKBufTree_Inv_NMOS_POGate_Comb_length'] = _CLKBufTreeTop_Inv_NMOS_POGate_Comb_length

        _Caculation_Parameters['_CLKBufTree_Inv_PMOS_ChannelWidth'] = _CLKBufTreeTop_Inv_PMOS_ChannelWidth
        _Caculation_Parameters['_CLKBufTree_Inv_PMOS_ChannelLength'] = _CLKBufTreeTop_Inv_PMOS_ChannelLength
        _Caculation_Parameters['_CLKBufTree_Inv_PMOS_NumberofGate'] = _CLKBufTreeTop_Inv_PMOS_NumberofGate
        _Caculation_Parameters['_CLKBufTree_Inv_PMOS_XVT'] = _CLKBufTreeTop_Inv_PMOS_XVT
        _Caculation_Parameters['_CLKBufTree_Inv_PMOS_POGate_Comb_length'] = _CLKBufTreeTop_Inv_PMOS_POGate_Comb_length

        _Caculation_Parameters['_CLKBufTree_NMOS_Pbody_NumCont'] = _CLKBufTreeTop_NMOS_Pbody_NumCont
        _Caculation_Parameters['_CLKBufTree_NMOS_Pbody_XvtTop2Pbody'] = _CLKBufTreeTop_NMOS_Pbody_XvtTop2Pbody
        _Caculation_Parameters['_CLKBufTree_PMOS_Nbody_NumCont'] = _CLKBufTreeTop_PMOS_Nbody_NumCont
        _Caculation_Parameters['_CLKBufTree_PMOS_Nbody_Xvtdown2Nbody'] = _CLKBufTreeTop_PMOS_Nbody_Xvtdown2Nbody
        _Caculation_Parameters['_CLKBufTree_PMOSXvt2NMOSXvt'] = _CLKBufTreeTop_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_CLKBufferTree_Top'] = self._SrefElementDeclaration(
            _DesignObj=F00_02_CLKBufferTree_v2._CLKBufferTree(_DesignParameter=None,
                                                              _Name='{}:SRF_CLKBufferTree_Top'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_CLKBufferTree_Top']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CLKBufferTree_Top']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CLKBufferTree_Top']['_DesignObj']._CalculateDesignParameter(
            **_Caculation_Parameters)

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

        ####### Bot CLK Buffer Tree2 SRF Generation
        _Caculation_Parameters = copy.deepcopy(F00_02_CLKBufferTree_v2._CLKBufferTree._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_CLKBufTree_TotalLength'] = PbodyXWidthSARLogic
        _Caculation_Parameters['_CLKBufTree_NumOfStage'] = _CLKBufTreeBot_NumOfStage
        _Caculation_Parameters['_CLKBufTree_Buf1_SizeByStage'] = _CLKBufTreeBot_CompOutBuf_SizeByStage
        _Caculation_Parameters['_CLKBufTree_Buf2_SizeByStage'] = _CLKBufTreeBot_CLKDoutBuf_SizeByStage
        _Caculation_Parameters['_CLKBufTree_OutputVia'] = None
        _Caculation_Parameters['_CLKBufTree_OutputPlacement'] = 'Up'

        _Caculation_Parameters['_CLKBufTree_Inv_NMOS_ChannelWidth'] = _CLKBufTreeBot_Inv_NMOS_ChannelWidth
        _Caculation_Parameters['_CLKBufTree_Inv_NMOS_ChannelLength'] = _CLKBufTreeBot_Inv_NMOS_ChannelLength
        _Caculation_Parameters['_CLKBufTree_Inv_NMOS_NumberofGate'] = _CLKBufTreeBot_Inv_NMOS_NumberofGate
        _Caculation_Parameters['_CLKBufTree_Inv_NMOS_XVT'] = _CLKBufTreeBot_Inv_NMOS_XVT
        _Caculation_Parameters['_CLKBufTree_Inv_NMOS_POGate_Comb_length'] = _CLKBufTreeBot_Inv_NMOS_POGate_Comb_length

        _Caculation_Parameters['_CLKBufTree_Inv_PMOS_ChannelWidth'] = _CLKBufTreeBot_Inv_PMOS_ChannelWidth
        _Caculation_Parameters['_CLKBufTree_Inv_PMOS_ChannelLength'] = _CLKBufTreeBot_Inv_PMOS_ChannelLength
        _Caculation_Parameters['_CLKBufTree_Inv_PMOS_NumberofGate'] = _CLKBufTreeBot_Inv_PMOS_NumberofGate
        _Caculation_Parameters['_CLKBufTree_Inv_PMOS_XVT'] = _CLKBufTreeBot_Inv_PMOS_XVT
        _Caculation_Parameters['_CLKBufTree_Inv_PMOS_POGate_Comb_length'] = _CLKBufTreeBot_Inv_PMOS_POGate_Comb_length

        _Caculation_Parameters['_CLKBufTree_NMOS_Pbody_NumCont'] = _CLKBufTreeBot_NMOS_Pbody_NumCont
        _Caculation_Parameters['_CLKBufTree_NMOS_Pbody_XvtTop2Pbody'] = _CLKBufTreeBot_NMOS_Pbody_XvtTop2Pbody
        _Caculation_Parameters['_CLKBufTree_PMOS_Nbody_NumCont'] = _CLKBufTreeBot_PMOS_Nbody_NumCont
        _Caculation_Parameters['_CLKBufTree_PMOS_Nbody_Xvtdown2Nbody'] = _CLKBufTreeBot_PMOS_Nbody_Xvtdown2Nbody
        _Caculation_Parameters['_CLKBufTree_PMOSXvt2NMOSXvt'] = _CLKBufTreeBot_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_CLKBufferTree_Bot'] = self._SrefElementDeclaration(
            _DesignObj=F00_02_CLKBufferTree_v2._CLKBufferTree(_DesignParameter=None,
                                                              _Name='{}:SRF_CLKBufferTree_Bot'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_CLKBufferTree_Bot']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CLKBufferTree_Bot']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CLKBufferTree_Bot']['_DesignObj']._CalculateDesignParameter(
            **_Caculation_Parameters)

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

        ##### 계산한 _SpaceBtwPbodyAndCLKSrc, _SpaceBtwNbody2AndCompOut을 반영하여 SRF_SARLogic를 재생성
        del (self._DesignParameter['SRF_SARLogic'])

        _Caculation_Parameters1['_SpaceBtwPbodyAndCLKSrc'] = _SpaceBtwPbodyAndCLKSrc
        _Caculation_Parameters1['_SpaceBtwNbody2AndCompOut'] = _SpaceBtwNbody2AndCompOut

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## DAC Controller Gen.
        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_SARLogic'] = self._SrefElementDeclaration(_DesignObj=K00_00_SARLogic_KJH1_v2_random._SARLogic(_DesignParameter=None, _Name='{}:SRF_SARLogic'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_SARLogic']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SARLogic']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SARLogic']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters1)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SARLogic']['_XYCoordinates'] = [[0, 0]]

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
        approaching_coord = tmp3[0][0]['_XY_down_left']
        for i in range(2 ** (_CLKBufTreeTop_NumOfStage - 1)):
            ## Target_coord: _XY_type1
            target_coord = tmp2[0][i][0]['_XY_down_left']
            ## Sref coord
            tmp4 = self.get_param_KJH4('BND_CLKSampBuf_Vtc_M2')
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
        for i in range(2 ** (_CLKBufTreeBot_NumOfStage - 1)):
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_CLKSampBuf_Vtc_M2')
            tmp1y = self.get_param_KJH4('BND_SARLogic_CLK_SampIn_Hrz_M3')
            target_coord = [tmp1[i][0]['_XY_up_left'][0], tmp1y[0][0]['_XY_cent'][1]]
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_CLKSampBuf_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met3Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_CLKSampBuf_ViaM2M3')
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
        for i in range(2 ** (_CLKBufTreeTop_NumOfStage - 1)):
            ## Target_coord: _XY_type1
            target_coord = tmp2[0][i][0]['_XY_down_left']
            ## Sref coord
            tmp4 = self.get_param_KJH4('BND_CLKSrcBuf_Vtc_M2')
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
        for i in range(2 ** (_CLKBufTreeBot_NumOfStage - 1)):
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_CLKSrcBuf_Vtc_M2')
            tmp1y = self.get_param_KJH4('BND_SARLogic_CLK_SrcIn_Hrz_M3')
            target_coord = [tmp1[i][0]['_XY_up_left'][0], tmp1y[0][0]['_XY_cent'][1]]
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_CLKSrcBuf_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met3Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_CLKSrcBuf_ViaM2M3')
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
        for i in range(2 ** (_CLKBufTreeBot_NumOfStage - 1)):
            ## Target_coord: _XY_type1
            target_coord = tmp2[0][i][0]['_XY_up_left']
            ## Sref coord
            tmp4 = self.get_param_KJH4('BND_CompOutBuf_Vtc_M2')
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
        for i in range(2 ** (_CLKBufTreeBot_NumOfStage - 1)):
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_CompOutBuf_Vtc_M2')
            tmp1y = self.get_param_KJH4('BND_CompOutput_Hrz_M3')
            target_coord = [tmp1[i][0]['_XY_left'][0], tmp1y[0][0]['_XY_cent'][1]]
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_CompOutBuf_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met3Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_CompOutBuf_ViaM2M3')
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
        for i in range(2 ** (_CLKBufTreeBot_NumOfStage - 1)):
            ## Target_coord: _XY_type1
            target_coord = tmp2[0][i][0]['_XY_up_left']
            ## Sref coord
            tmp4 = self.get_param_KJH4('BND_CLKDoutOutBuf_Vtc_M2')
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
        for i in range(2 ** (_CLKBufTreeBot_NumOfStage - 1)):
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_CLKDoutOutBuf_Vtc_M2')
            tmp1y = self.get_param_KJH4('BND_SARLogic_CLK_DoutIn_Hrz_M3')
            target_coord = [tmp1[i][0]['_XY_left'][0], tmp1y[0][0]['_XY_cent'][1]]
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_CLKDoutOutBuf_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met3Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_CLKDoutOutBuf_ViaM2M3')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKDoutOutBuf_ViaM2M3']['_XYCoordinates'] = tmpXY

        for j in range(1, 3):
            for i in range(1, _CLKBufTreeTop_NumOfStage + 1):
                del (self._DesignParameter['SRF_CLKBufferTree_Top']['_DesignObj']._DesignParameter['SRF_CLKBuf{}Inv_Stage{}'.format(j, i)]['_DesignObj']._DesignParameter['SRF_Pbody']['_DesignObj']._DesignParameter['SRF_PbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_COLayer'])
                del (self._DesignParameter['SRF_CLKBufferTree_Top']['_DesignObj']._DesignParameter['SRF_CLKBuf{}Inv_Stage{}'.format(j, i)]['_DesignObj']._DesignParameter['SRF_Nbody']['_DesignObj']._DesignParameter['SRF_NbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_COLayer'])
            for i in range(1, _CLKBufTreeBot_NumOfStage + 1):
                del (self._DesignParameter['SRF_CLKBufferTree_Bot']['_DesignObj']._DesignParameter['SRF_CLKBuf{}Inv_Stage{}'.format(j, i)]['_DesignObj']._DesignParameter['SRF_Pbody']['_DesignObj']._DesignParameter['SRF_PbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_COLayer'])
                del (self._DesignParameter['SRF_CLKBufferTree_Bot']['_DesignObj']._DesignParameter['SRF_CLKBuf{}Inv_Stage{}'.format(j, i)]['_DesignObj']._DesignParameter['SRF_Nbody']['_DesignObj']._DesignParameter['SRF_NbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_COLayer'])

        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')


############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    import random
    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    Dinput_tg_MOSFinger = random.randrange(1, 5, 1)
    master_tg_MOSFinger = random.randrange(1, 5, 1)
    master_nor1_MOSFinger = random.randrange(1, 5, 1)
    master_nor2_MOSFinger = random.randrange(1, 5, 1)
    SET_inv1_MOSFinger = random.randrange(1, 5, 1)
    SET_inv2_MOSFinger = random.randrange(1, 5, 1)
    CLK_inv_MOSFinger = random.randrange(1, 5, 1)

    Center_tg_MOSFinger = random.randrange(1, 5, 1)
    slave_tg_MOSFinger = random.randrange(1, 5, 1)
    slave_nor1_MOSFinger = random.randrange(1, 5, 1)
    slave_nor2_MOSFinger = random.randrange(1, 5, 1)
    RESET_inv1_MOSFinger = random.randrange(1, 5, 1)
    RESET_inv2_MOSFinger = random.randrange(1, 5, 1)
    qb_out_inv_MOSFinger = random.randrange(1, 5, 1)

    DFF_MOSWidth = random.randrange(200, 601, 50)
    TreeBuf_MOSWidth = random.randrange(200, 601, 50)

    SizeByStage1 = random.randrange(1,5,1)
    SizeByStage2 = random.randrange(1, 5, 1)
    SizeByStage3 = random.randrange(1, 5, 1)
    SizeByStage4 = random.randrange(1, 5, 1)

    DFF_XVT_list = ['RVT', 'SLVT', 'LVT', 'HVT']
    # DFF_XVT_list = ['SLVT']
    DFF_Selected_XVT = random.choice(DFF_XVT_list)

    TreeBuf_XVT_list = ['RVT', 'SLVT', 'LVT', 'HVT']
    # TreeBuf_XVT_list = ['SLVT']
    TreeBuf_Selected_XVT = random.choice(TreeBuf_XVT_list)

    for _iter in range(5):
        ## LibraryName: ex)Proj_ADC_A_my_building_block
        libname = 'Proj_ADC_K00_SARLogicWtCLKBufTree_random_v{}'.format(_iter + 6)
        ## CellName: ex)C01_cap_array_v2_84
        cellname = 'K00_00_SARLogicWtCLKBufTree'
        _fileName = cellname + '.gds'

        ''' Input Parameters for Layout Object '''
        InputParams = dict(
            _NumofBit = 6,

            _Test_distance = 330,
            _Routing_width =  50,
            _Routing_distance = 80,

            _YWidthOfCLKSrc=100,
            _SpaceBtwCLKSrcAndCLKSamp=100,
            _YWidthOfCLKSamp=100,

            _YWidthOfCompOut=100,
            _SpaceBtwCompOutAndCLKDout=100,
            _YWidthOfCLKDout=100,

            ## DFF Common
            _DFF_Pbody_NumCont      = 2, # number
            _DFF_Nbody_NumCont      = 2, # number
            _DFF_PMOSXvt2NMOSXvt    = 1150, # number
            _DFF_XvtTop2Pbody       = None, # number/None(Minimum)
            _DFF_Xvtdown2Nbody      = None, # number/None(Minimum)

            ## Master Xgate1
            ## Xgate common

            ## Xgate NMOS
            _Mst_Xgate1_NMOS_NumberofGate=Dinput_tg_MOSFinger,  # 1
            _Mst_Xgate1_NMOS_ChannelWidth=DFF_MOSWidth,  # 100
            _Mst_Xgate1_NMOS_ChannelLength=30,
            _Mst_Xgate1_NMOS_XVT=DFF_Selected_XVT,
            _Mst_Xgate1_NMOS_POGate_Comb_length=100,

            ## Xgate PMOS
            _Mst_Xgate1_PMOS_NumberofGate=Dinput_tg_MOSFinger,  # 1
            _Mst_Xgate1_PMOS_ChannelWidth=2 * DFF_MOSWidth,  # 200
            _Mst_Xgate1_PMOS_ChannelLength=30,
            _Mst_Xgate1_PMOS_XVT=DFF_Selected_XVT,
            _Mst_Xgate1_PMOS_POGate_Comb_length=100,

            ## Master Xgate2
            ## Xgate common

            ## Xgate NMOS
            _Mst_Xgate2_NMOS_NumberofGate=master_tg_MOSFinger,
            _Mst_Xgate2_NMOS_ChannelWidth=DFF_MOSWidth,
            _Mst_Xgate2_NMOS_ChannelLength=30,
            _Mst_Xgate2_NMOS_XVT=DFF_Selected_XVT,
            _Mst_Xgate2_NMOS_POGate_Comb_length=100,

            ## Xgate PMOS
            _Mst_Xgate2_PMOS_NumberofGate=master_tg_MOSFinger,  # 2
            _Mst_Xgate2_PMOS_ChannelWidth=2 * DFF_MOSWidth,
            _Mst_Xgate2_PMOS_ChannelLength=30,
            _Mst_Xgate2_PMOS_XVT=DFF_Selected_XVT,
            _Mst_Xgate2_PMOS_POGate_Comb_length=100,


            ## Master Nor1
            ## Nor1 common

            ## NMOS
                ## NMOS common
            _Mst_Nor1_NMOS_XVT=DFF_Selected_XVT,

            ## NMOSA
            _Mst_Nor1_NMOSA_NumberofGate=master_nor1_MOSFinger,
            _Mst_Nor1_NMOSA_ChannelWidth=DFF_MOSWidth,
            _Mst_Nor1_NMOSA_ChannelLength=30,
            _Mst_Nor1_NMOSA_POGate_Comb_length=100,

            ## NMOSB
            _Mst_Nor1_NMOSB_NumberofGate=master_nor1_MOSFinger,
            _Mst_Nor1_NMOSB_ChannelWidth=DFF_MOSWidth,
            _Mst_Nor1_NMOSB_ChannelLength=30,
            _Mst_Nor1_NMOSB_POGate_Comb_length=100,

            ## PMOS
                ## PMOS common
            _Mst_Nor1_PMOS_XVT=DFF_Selected_XVT,

            ## PMOSA
            _Mst_Nor1_PMOSA_NumberofGate=2 * master_nor1_MOSFinger,
            _Mst_Nor1_PMOSA_ChannelWidth=2 * DFF_MOSWidth,
            _Mst_Nor1_PMOSA_ChannelLength=30,
            _Mst_Nor1_PMOSA_POGate_Comb_length=100,

            ## PMOSB
            _Mst_Nor1_PMOSB_NumberofGate=2 * master_nor1_MOSFinger,
            _Mst_Nor1_PMOSB_ChannelWidth=2 * DFF_MOSWidth,
            _Mst_Nor1_PMOSB_ChannelLength=30,
            _Mst_Nor1_PMOSB_POGate_Comb_length=100,

            ## Master Nor2
            ## Nor2 common

            ## NMOS
            ## NMOS common
            _Mst_Nor2_NMOS_XVT=DFF_Selected_XVT,

            ## NMOSA
            _Mst_Nor2_NMOSA_NumberofGate=master_nor2_MOSFinger,
            _Mst_Nor2_NMOSA_ChannelWidth=DFF_MOSWidth,
            _Mst_Nor2_NMOSA_ChannelLength=30,
            _Mst_Nor2_NMOSA_POGate_Comb_length=100,

            ## NMOSB
            _Mst_Nor2_NMOSB_NumberofGate=master_nor2_MOSFinger,
            _Mst_Nor2_NMOSB_ChannelWidth=DFF_MOSWidth,
            _Mst_Nor2_NMOSB_ChannelLength=30,
            _Mst_Nor2_NMOSB_POGate_Comb_length=100,

            ## PMOS
            ## PMOS common
            _Mst_Nor2_PMOS_XVT=DFF_Selected_XVT,

            ## PMOSA
            _Mst_Nor2_PMOSA_NumberofGate=2 * master_nor2_MOSFinger,
            _Mst_Nor2_PMOSA_ChannelWidth=2 * DFF_MOSWidth,
            _Mst_Nor2_PMOSA_ChannelLength=30,
            _Mst_Nor2_PMOSA_POGate_Comb_length=100,

            ## PMOSB
            _Mst_Nor2_PMOSB_NumberofGate=2 * master_nor2_MOSFinger,
            _Mst_Nor2_PMOSB_ChannelWidth=2 * DFF_MOSWidth,
            _Mst_Nor2_PMOSB_ChannelLength=30,
            _Mst_Nor2_PMOSB_POGate_Comb_length=100,

            ## Master Inv1 : Set pre-driver
            ## Inv1 common

            ## Inv1 NMOS
            _Mst_Inv1_NMOS_NumberofGate=SET_inv1_MOSFinger,
            _Mst_Inv1_NMOS_ChannelWidth=DFF_MOSWidth,
            _Mst_Inv1_NMOS_ChannelLength=30,
            _Mst_Inv1_NMOS_XVT=DFF_Selected_XVT,
            _Mst_Inv1_NMOS_POGate_Comb_length=100,

            ## Inv1 PMOS
            _Mst_Inv1_PMOS_NumberofGate=SET_inv1_MOSFinger,
            _Mst_Inv1_PMOS_ChannelWidth=2 * DFF_MOSWidth,
            _Mst_Inv1_PMOS_ChannelLength=30,
            _Mst_Inv1_PMOS_XVT=DFF_Selected_XVT,
            _Mst_Inv1_PMOS_POGate_Comb_length=100,

            ## Master Inv2 : Set driver
            ## Inv2 common

            ## Inv2 NMOS
            _Mst_Inv2_NMOS_NumberofGate=SET_inv2_MOSFinger,
            _Mst_Inv2_NMOS_ChannelWidth=DFF_MOSWidth,
            _Mst_Inv2_NMOS_ChannelLength=30,
            _Mst_Inv2_NMOS_XVT=DFF_Selected_XVT,
            _Mst_Inv2_NMOS_POGate_Comb_length=100,

            ## Inv2 PMOS
            _Mst_Inv2_PMOS_NumberofGate=SET_inv2_MOSFinger,
            _Mst_Inv2_PMOS_ChannelWidth=2 * DFF_MOSWidth,
            _Mst_Inv2_PMOS_ChannelLength=30,
            _Mst_Inv2_PMOS_XVT=DFF_Selected_XVT,
            _Mst_Inv2_PMOS_POGate_Comb_length=100,


            ## Master Inv3 : Clock driver
            ## Inv3 common

            ## Inv3 NMOS
            _Mst_Inv3_NMOS_NumberofGate=CLK_inv_MOSFinger,
            _Mst_Inv3_NMOS_ChannelWidth=DFF_MOSWidth,
            _Mst_Inv3_NMOS_ChannelLength=30,
            _Mst_Inv3_NMOS_XVT=DFF_Selected_XVT,
            _Mst_Inv3_NMOS_POGate_Comb_length=100,

            ## Inv3 PMOS
            _Mst_Inv3_PMOS_NumberofGate=CLK_inv_MOSFinger,
            _Mst_Inv3_PMOS_ChannelWidth=2 * DFF_MOSWidth,
            _Mst_Inv3_PMOS_ChannelLength=30,
            _Mst_Inv3_PMOS_XVT=DFF_Selected_XVT,
            _Mst_Inv3_PMOS_POGate_Comb_length=100,

            ## Slave Xgate1
            ## Xgate common

            ## Xgate NMOS
            _Slv_Xgate1_NMOS_NumberofGate=Center_tg_MOSFinger,
            _Slv_Xgate1_NMOS_ChannelWidth=DFF_MOSWidth,
            _Slv_Xgate1_NMOS_ChannelLength=30,
            _Slv_Xgate1_NMOS_XVT=DFF_Selected_XVT,
            _Slv_Xgate1_NMOS_POGate_Comb_length=100,

            ## Xgate NMOS
            _Slv_Xgate1_PMOS_NumberofGate=Center_tg_MOSFinger,
            _Slv_Xgate1_PMOS_ChannelWidth=2 * DFF_MOSWidth,
            _Slv_Xgate1_PMOS_ChannelLength=30,
            _Slv_Xgate1_PMOS_XVT=DFF_Selected_XVT,
            _Slv_Xgate1_PMOS_POGate_Comb_length=100,

            ## Slave Xgate2
            ## Xgate common

            ## Xgate NMOS
            _Slv_Xgate2_NMOS_NumberofGate=slave_tg_MOSFinger,
            _Slv_Xgate2_NMOS_ChannelWidth=DFF_MOSWidth,
            _Slv_Xgate2_NMOS_ChannelLength=30,
            _Slv_Xgate2_NMOS_XVT=DFF_Selected_XVT,
            _Slv_Xgate2_NMOS_POGate_Comb_length=100,

            ## Xgate NMOS
            _Slv_Xgate2_PMOS_NumberofGate=slave_tg_MOSFinger,
            _Slv_Xgate2_PMOS_ChannelWidth=2 * DFF_MOSWidth,
            _Slv_Xgate2_PMOS_ChannelLength=30,
            _Slv_Xgate2_PMOS_XVT=DFF_Selected_XVT,
            _Slv_Xgate2_PMOS_POGate_Comb_length=100,


            ## Slave Nor1
            ## Nor1 common

            ## NMOS
            ## NMOS common
            _Slv_Nor1_NMOS_XVT=DFF_Selected_XVT,

            ## NMOSA
            _Slv_Nor1_NMOSA_NumberofGate=slave_nor1_MOSFinger,
            _Slv_Nor1_NMOSA_ChannelWidth=DFF_MOSWidth,
            _Slv_Nor1_NMOSA_ChannelLength=30,
            _Slv_Nor1_NMOSA_POGate_Comb_length=100,

            ## NMOSB
            _Slv_Nor1_NMOSB_NumberofGate=slave_nor1_MOSFinger,
            _Slv_Nor1_NMOSB_ChannelWidth=DFF_MOSWidth,
            _Slv_Nor1_NMOSB_ChannelLength=30,
            _Slv_Nor1_NMOSB_POGate_Comb_length=100,

            ## PMOS
            ## PMOS common
            _Slv_Nor1_PMOS_XVT=DFF_Selected_XVT,

            ## PMOSA
            _Slv_Nor1_PMOSA_NumberofGate=2 * slave_nor1_MOSFinger,
            _Slv_Nor1_PMOSA_ChannelWidth=2 * DFF_MOSWidth,
            _Slv_Nor1_PMOSA_ChannelLength=30,
            _Slv_Nor1_PMOSA_POGate_Comb_length=100,

            ## PMOSB
            _Slv_Nor1_PMOSB_NumberofGate=2 * slave_nor1_MOSFinger,
            _Slv_Nor1_PMOSB_ChannelWidth=2 * DFF_MOSWidth,
            _Slv_Nor1_PMOSB_ChannelLength=30,
            _Slv_Nor1_PMOSB_POGate_Comb_length=100,

            ## Slave Nor2
            ## Nor2 common

            ## NMOS
            ## NMOS common
            _Slv_Nor2_NMOS_XVT=DFF_Selected_XVT,

            ## NMOSA
            _Slv_Nor2_NMOSA_NumberofGate=slave_nor2_MOSFinger,
            _Slv_Nor2_NMOSA_ChannelWidth=DFF_MOSWidth,
            _Slv_Nor2_NMOSA_ChannelLength=30,
            _Slv_Nor2_NMOSA_POGate_Comb_length=100,

            ## NMOSB
            _Slv_Nor2_NMOSB_NumberofGate=slave_nor2_MOSFinger,
            _Slv_Nor2_NMOSB_ChannelWidth=DFF_MOSWidth,
            _Slv_Nor2_NMOSB_ChannelLength=30,
            _Slv_Nor2_NMOSB_POGate_Comb_length=100,

            ## PMOS
            ## PMOS common
            _Slv_Nor2_PMOS_XVT=DFF_Selected_XVT,

            ## PMOSA
            _Slv_Nor2_PMOSA_NumberofGate=2 * slave_nor2_MOSFinger,
            _Slv_Nor2_PMOSA_ChannelWidth=2 * DFF_MOSWidth,
            _Slv_Nor2_PMOSA_ChannelLength=30,
            _Slv_Nor2_PMOSA_POGate_Comb_length=100,

            ## PMOSB
            _Slv_Nor2_PMOSB_NumberofGate=2 * slave_nor2_MOSFinger,
            _Slv_Nor2_PMOSB_ChannelWidth=2 * DFF_MOSWidth,
            _Slv_Nor2_PMOSB_ChannelLength=30,
            _Slv_Nor2_PMOSB_POGate_Comb_length=100,

            ## Slave Inv1 : ReSet pre-driver
            ## Inv1 common

            ## Inv1 NMOS
            _Slv_Inv1_NMOS_NumberofGate=RESET_inv1_MOSFinger,
            _Slv_Inv1_NMOS_ChannelWidth=DFF_MOSWidth,
            _Slv_Inv1_NMOS_ChannelLength=30,
            _Slv_Inv1_NMOS_XVT=DFF_Selected_XVT,
            _Slv_Inv1_NMOS_POGate_Comb_length=100,

            ## Inv1 PMOS
            _Slv_Inv1_PMOS_NumberofGate=RESET_inv1_MOSFinger,
            _Slv_Inv1_PMOS_ChannelWidth=2 * DFF_MOSWidth,
            _Slv_Inv1_PMOS_ChannelLength=30,
            _Slv_Inv1_PMOS_XVT=DFF_Selected_XVT,
            _Slv_Inv1_PMOS_POGate_Comb_length=100,

            ## Slave Inv2 : ReSet driver
            ## Inv2 common

            ## Inv2 NMOS
            _Slv_Inv2_NMOS_NumberofGate=RESET_inv2_MOSFinger,
            _Slv_Inv2_NMOS_ChannelWidth=DFF_MOSWidth,
            _Slv_Inv2_NMOS_ChannelLength=30,
            _Slv_Inv2_NMOS_XVT=DFF_Selected_XVT,
            _Slv_Inv2_NMOS_POGate_Comb_length=100,

            ## Inv2 PMOS
            _Slv_Inv2_PMOS_NumberofGate=RESET_inv2_MOSFinger,
            _Slv_Inv2_PMOS_ChannelWidth=2 * DFF_MOSWidth,
            _Slv_Inv2_PMOS_ChannelLength=30,
            _Slv_Inv2_PMOS_XVT=DFF_Selected_XVT,
            _Slv_Inv2_PMOS_POGate_Comb_length=100,


            ## Slave Inv3 : Qb driver
            ## Inv3 common

            ## Inv3 NMOS
            _Slv_Inv3_NMOS_NumberofGate=qb_out_inv_MOSFinger,
            _Slv_Inv3_NMOS_ChannelWidth=DFF_MOSWidth,
            _Slv_Inv3_NMOS_ChannelLength=30,
            _Slv_Inv3_NMOS_XVT=DFF_Selected_XVT,
            _Slv_Inv3_NMOS_POGate_Comb_length=100,

            ## Inv3 PMOS
            _Slv_Inv3_PMOS_NumberofGate=qb_out_inv_MOSFinger,
            _Slv_Inv3_PMOS_ChannelWidth=2 * DFF_MOSWidth,
            _Slv_Inv3_PMOS_ChannelLength=30,
            _Slv_Inv3_PMOS_XVT=DFF_Selected_XVT,
            _Slv_Inv3_PMOS_POGate_Comb_length=100,

            # Top Clock  Tree Size
            # _CLKBufTreeTop_TotalLength=50000,
            _CLKBufTreeTop_NumOfStage=4,
            _CLKBufTreeTop_CLKSampBuf_SizeByStage=[SizeByStage1, SizeByStage2, SizeByStage3, SizeByStage4],
            _CLKBufTreeTop_CLKSrcBuf_SizeByStage=[SizeByStage1, SizeByStage2, SizeByStage3, SizeByStage4],  # 스테이지에 따른 버퍼 사이즈(UnitBuffer의 배수로 각 스테이지의 크기가 결정 됨.)
            _CLKBufTreeTop_XOffSet = 0,

            ## Top CLK Buffer Size
            _CLKBufTreeTop_Inv_NMOS_ChannelWidth=TreeBuf_MOSWidth,  # Number
            _CLKBufTreeTop_Inv_NMOS_ChannelLength=30,  # Number
            _CLKBufTreeTop_Inv_NMOS_NumberofGate=1,  # Number
            _CLKBufTreeTop_Inv_NMOS_XVT=TreeBuf_Selected_XVT,  # 'XVT' ex)SLVT/LVT/RVT/HVT
            _CLKBufTreeTop_Inv_NMOS_POGate_Comb_length=100,  # None/Number

            _CLKBufTreeTop_Inv_PMOS_ChannelWidth=2*TreeBuf_MOSWidth,  # Number
            _CLKBufTreeTop_Inv_PMOS_ChannelLength=30,  # Number
            _CLKBufTreeTop_Inv_PMOS_NumberofGate=1,  # Number
            _CLKBufTreeTop_Inv_PMOS_XVT=TreeBuf_Selected_XVT,  # 'XVT' ex)SLVT/LVT/RVT/HVT
            _CLKBufTreeTop_Inv_PMOS_POGate_Comb_length=100,  # None/Number

            # Top CLK BufferPowerRail Size
            _CLKBufTreeTop_NMOS_Pbody_NumCont=2,
            _CLKBufTreeTop_NMOS_Pbody_XvtTop2Pbody=None,
            _CLKBufTreeTop_PMOS_Nbody_NumCont=2,
            _CLKBufTreeTop_PMOS_Nbody_Xvtdown2Nbody=None,
            _CLKBufTreeTop_PMOSXvt2NMOSXvt=446,

            # Bottom Clock  Tree Size
            # _CLKBufTreeBot_TotalLength=50000,
            _CLKBufTreeBot_NumOfStage=4,
            _CLKBufTreeBot_CompOutBuf_SizeByStage=[SizeByStage1, SizeByStage2, SizeByStage3, SizeByStage4],
            _CLKBufTreeBot_CLKDoutBuf_SizeByStage=[SizeByStage1, SizeByStage2, SizeByStage3, SizeByStage4],  # 스테이지에 따른 버퍼 사이즈(UnitBuffer의 배수로 각 스테이지의 크기가 결정 됨.)
            _CLKBufTreeBot_XOffSet = 0,

            ## Bottom CLK Buffer Size
            _CLKBufTreeBot_Inv_NMOS_ChannelWidth=TreeBuf_MOSWidth,  # Number
            _CLKBufTreeBot_Inv_NMOS_ChannelLength=30,  # Number
            _CLKBufTreeBot_Inv_NMOS_NumberofGate=1,  # Number
            _CLKBufTreeBot_Inv_NMOS_XVT=TreeBuf_Selected_XVT,  # 'XVT' ex)SLVT/LVT/RVT/HVT
            _CLKBufTreeBot_Inv_NMOS_POGate_Comb_length=100,  # None/Number

            _CLKBufTreeBot_Inv_PMOS_ChannelWidth=2*TreeBuf_MOSWidth,  # Number
            _CLKBufTreeBot_Inv_PMOS_ChannelLength=30,  # Number
            _CLKBufTreeBot_Inv_PMOS_NumberofGate=1,  # Number
            _CLKBufTreeBot_Inv_PMOS_XVT=TreeBuf_Selected_XVT,  # 'XVT' ex)SLVT/LVT/RVT/HVT
            _CLKBufTreeBot_Inv_PMOS_POGate_Comb_length=100,  # None/Number

            # Bottom CLK Buffer PowerRail Size
            _CLKBufTreeBot_NMOS_Pbody_NumCont=2,
            _CLKBufTreeBot_NMOS_Pbody_XvtTop2Pbody=None,
            _CLKBufTreeBot_PMOS_Nbody_NumCont=2,
            _CLKBufTreeBot_PMOS_Nbody_Xvtdown2Nbody=None,
            _CLKBufTreeBot_PMOSXvt2NMOSXvt=446,
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
