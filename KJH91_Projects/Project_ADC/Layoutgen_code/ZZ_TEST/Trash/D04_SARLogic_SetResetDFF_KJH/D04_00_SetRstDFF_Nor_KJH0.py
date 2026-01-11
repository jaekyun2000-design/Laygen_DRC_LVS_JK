
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
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A08_PbodyContactPhyLen_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A07_NbodyContactPhyLen_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.ZZ_TEST.Trash.D00_SARLogic_Inverter_KJH import D00_00_Inverter_KJH1
from KJH91_Projects.Project_ADC.Layoutgen_code.ZZ_TEST.Trash.D01_SARLogic_XmissionGate_KJH import D01_02_Xgate_KJH1
from KJH91_Projects.Project_ADC.Layoutgen_code.ZZ_TEST.Trash.D02_SARLogic_Nor_KJH import D02_02_Nor_KJH0


## Define Class
class _SetRstDFF_Nor(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
        _Test_distance=500,

        ## DFF Common
        _DFF_Pbody_NumCont=2,  # number
        _DFF_Nbody_NumCont=2,  # number
        _DFF_PMOSXvt2NMOSXvt=1500,  # number
        _DFF_XlvtTop2Pdoby=None,  # number/None(Minimum)
        _DFF_Xlvtdown2Ndoby=None,  # number/None(Minimum)

        ## Master Xgate1
        ## PMOS NMOS common
        _Mst_Xgate1_NumberofGate=1,  # number
        _Mst_Xgate1_Channel_Length=30,  # number
        _Mst_Xgate1_GateSpacing=None,  # number/None
        _Mst_Xgate1_SDWidth=None,  # number/None
        _Mst_Xgate1_PCCrit=True,  # None/True

        ## NMOS
        _Mst_Xgate1_NMOSChannel_Width=100,  # number
        _Mst_Xgate1_NMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Mst_Xgate1_NMOSDummy_Length=None,  # None/number
        _Mst_Xgate1_NMOSDummy_Placement=None,  # None/'Up'/'Dn'

        ## PMOS
        _Mst_Xgate1_PMOSChannel_Width=200,  # number
        _Mst_Xgate1_PMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Mst_Xgate1_PMOSDummy_Length=None,  # None/number
        _Mst_Xgate1_PMOSDummy_Placement=None,  # None/'Up'/'Dn'

        ## Master Xgate2
        ## PMOS NMOS common
        _Mst_Xgate2_NumberofGate=1,  # number
        _Mst_Xgate2_Channel_Length=30,  # number
        _Mst_Xgate2_GateSpacing=None,  # number/None
        _Mst_Xgate2_SDWidth=None,  # number/None
        _Mst_Xgate2_PCCrit=True,  # None/True

        ## NMOS
        _Mst_Xgate2_NMOSChannel_Width=100,  # number
        _Mst_Xgate2_NMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Mst_Xgate2_NMOSDummy_Length=None,  # None/number
        _Mst_Xgate2_NMOSDummy_Placement=None,  # None/'Up'/'Dn'

        ## PMOS
        _Mst_Xgate2_PMOSChannel_Width=200,  # number
        _Mst_Xgate2_PMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Mst_Xgate2_PMOSDummy_Length=None,  # None/number
        _Mst_Xgate2_PMOSDummy_Placement=None,  # None/'Up'/'Dn'

        ## Master Nor1
        ## PMOS NMOS Common
        # _Mst_Nor1_NumberofGate = 2, # number
        _Mst_Nor1_Channel_Length=30,  # number
        _Mst_Nor1_GateSpacing=None,  # number/None
        _Mst_Nor1_SDWidth=None,  # number/None
        _Mst_Nor1_PCCrit=True,  # None/True

        ## NMOS
        _Mst_Nor1_NMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
        ## NMOSA
        _Mst_Nor1_NMOSA_NumberofGate=2,
        _Mst_Nor1_NMOSA_Channel_Width=200,  # number
        _Mst_Nor1_NMOSA_Dummy_Length=None,  # None/number
        _Mst_Nor1_NMOSA_Dummy_Placement=None,  # None/'Up'/'Dn'
        ## NMOSB
        _Mst_Nor1_NMOSB_NumberofGate=2,
        _Mst_Nor1_NMOSB_Channel_Width=200,  # number
        _Mst_Nor1_NMOSB_Dummy_Length=None,  # None/number
        _Mst_Nor1_NMOSB_Dummy_Placement=None,  # None/'Up'/'Dn'

        ## PMOS
        _Mst_Nor1_PMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
        ## PMOSA
        _Mst_Nor1_PMOSA_NumberofGate=2,
        _Mst_Nor1_PMOSA_Channel_Width=800,  # number
        _Mst_Nor1_PMOSA_Dummy_Length=None,  # None/number
        _Mst_Nor1_PMOSA_Dummy_Placement=None,  # None/'Up'/'Dn'
        ## PMOSB
        _Mst_Nor1_PMOSB_NumberofGate=2,
        _Mst_Nor1_PMOSB_Channel_Width=800,  # number
        _Mst_Nor1_PMOSB_Dummy_Length=None,  # None/number
        _Mst_Nor1_PMOSB_Dummy_Placement=None,  # None/'Up'/'Dn'

        ## Master Nor2
        ## PMOS NMOS Common
        # _Mst_Nor2_NumberofGate = 2, # number
        _Mst_Nor2_Channel_Length=30,  # number
        _Mst_Nor2_GateSpacing=None,  # number/None
        _Mst_Nor2_SDWidth=None,  # number/None
        _Mst_Nor2_PCCrit=True,  # None/True

        ## NMOS
        _Mst_Nor2_NMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
        ## NMOSA
        _Mst_Nor2_NMOSA_NumberofGate=2,
        _Mst_Nor2_NMOSA_Channel_Width=200,  # number
        _Mst_Nor2_NMOSA_Dummy_Length=None,  # None/number
        _Mst_Nor2_NMOSA_Dummy_Placement=None,  # None/'Up'/'Dn'
        ## NMOSB
        _Mst_Nor2_NMOSB_NumberofGate=2,
        _Mst_Nor2_NMOSB_Channel_Width=200,  # number
        _Mst_Nor2_NMOSB_Dummy_Length=None,  # None/number
        _Mst_Nor2_NMOSB_Dummy_Placement=None,  # None/'Up'/'Dn'

        ## PMOS
        _Mst_Nor2_PMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
        ## PMOSA
        _Mst_Nor2_PMOSA_NumberofGate=2,
        _Mst_Nor2_PMOSA_Channel_Width=800,  # number
        _Mst_Nor2_PMOSA_Dummy_Length=None,  # None/number
        _Mst_Nor2_PMOSA_Dummy_Placement=None,  # None/'Up'/'Dn'
        ## PMOSB
        _Mst_Nor2_PMOSB_NumberofGate=2,
        _Mst_Nor2_PMOSB_Channel_Width=800,  # number
        _Mst_Nor2_PMOSB_Dummy_Length=None,  # None/number
        _Mst_Nor2_PMOSB_Dummy_Placement=None,  # None/'Up'/'Dn'

        ## Master Inv1: Set Pre-driver
        ## PMOS NMOS Common
        _Mst_Inv1_NumberofGate=2,  # number
        _Mst_Inv1_Channel_Length=30,  # number
        _Mst_Inv1_GateSpacing=None,  # number/None
        _Mst_Inv1_SDWidth=None,  # number/None
        _Mst_Inv1_PCCrit=True,  # None/True

        ## NMOS
        _Mst_Inv1_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Mst_Inv1_NMOS_Channel_Width=200,  # number
        _Mst_Inv1_NMOS_Dummy_Length=None,  # None/number
        _Mst_Inv1_NMOS_Dummy_Placement=None,  # None/'Up'/'Dn'

        ## PMOS
        _Mst_Inv1_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Mst_Inv1_PMOS_Channel_Width=400,  # number
        _Mst_Inv1_PMOS_Dummy_Length=None,  # None/number
        _Mst_Inv1_PMOS_Dummy_Placement=None,  # None/'Up'/'Dn'

        ## Master Inv2: Set driver
        ## PMOS NMOS Common
        _Mst_Inv2_NumberofGate=1,  # number
        _Mst_Inv2_Channel_Length=30,  # number
        _Mst_Inv2_GateSpacing=None,  # number/None
        _Mst_Inv2_SDWidth=None,  # number/None
        _Mst_Inv2_PCCrit=True,  # None/True

        ## NMOS
        _Mst_Inv2_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Mst_Inv2_NMOS_Channel_Width=200,  # number
        _Mst_Inv2_NMOS_Dummy_Length=None,  # None/number
        _Mst_Inv2_NMOS_Dummy_Placement=None,  # None/'Up'/'Dn'

        ## PMOS
        _Mst_Inv2_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Mst_Inv2_PMOS_Channel_Width=400,  # number
        _Mst_Inv2_PMOS_Dummy_Length=None,  # None/number
        _Mst_Inv2_PMOS_Dummy_Placement=None,  # None/'Up'/'Dn'

        ## Inv3: Clock Buffer
        ## PMOS NMOS Common
        _Clk_Inv3_NumberofGate=1,  # number
        _Clk_Inv3_Channel_Length=30,  # number
        _Clk_Inv3_GateSpacing=None,  # number/None
        _Clk_Inv3_SDWidth=None,  # number/None
        _Clk_Inv3_PCCrit=True,  # None/True

        ## NMOS
        _Clk_Inv3_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Clk_Inv3_NMOS_Channel_Width=200,  # number
        _Clk_Inv3_NMOS_Dummy_Length=None,  # None/number
        _Clk_Inv3_NMOS_Dummy_Placement=None,  # None/'Up'/'Dn'

        ## PMOS
        _Clk_Inv3_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Clk_Inv3_PMOS_Channel_Width=400,  # number
        _Clk_Inv3_PMOS_Dummy_Length=None,  # None/number
        _Clk_Inv3_PMOS_Dummy_Placement=None,  # None/'Up'/'Dn'

        ## Slave Xgate1
        ## PMOS NMOS common
        _Slv_Xgate1_NumberofGate=1,  # number
        _Slv_Xgate1_Channel_Length=30,  # number
        _Slv_Xgate1_GateSpacing=None,  # number/None
        _Slv_Xgate1_SDWidth=None,  # number/None
        _Slv_Xgate1_PCCrit=True,  # None/True

        ## NMOS
        _Slv_Xgate1_NMOSChannel_Width=100,  # number
        _Slv_Xgate1_NMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Slv_Xgate1_NMOSDummy_Length=None,  # None/number
        _Slv_Xgate1_NMOSDummy_Placement=None,  # None/'Up'/'Dn'

        ## PMOS
        _Slv_Xgate1_PMOSChannel_Width=200,  # number
        _Slv_Xgate1_PMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Slv_Xgate1_PMOSDummy_Length=None,  # None/number
        _Slv_Xgate1_PMOSDummy_Placement=None,  # None/'Up'/'Dn'

        ## Slave Xgate2
        ## PMOS NMOS common
        _Slv_Xgate2_NumberofGate=1,  # number
        _Slv_Xgate2_Channel_Length=30,  # number
        _Slv_Xgate2_GateSpacing=None,  # number/None
        _Slv_Xgate2_SDWidth=None,  # number/None
        _Slv_Xgate2_PCCrit=True,  # None/True

        ## NMOS
        _Slv_Xgate2_NMOSChannel_Width=100,  # number
        _Slv_Xgate2_NMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Slv_Xgate2_NMOSDummy_Length=None,  # None/number
        _Slv_Xgate2_NMOSDummy_Placement=None,  # None/'Up'/'Dn'

        ## PMOS
        _Slv_Xgate2_PMOSChannel_Width=200,  # number
        _Slv_Xgate2_PMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Slv_Xgate2_PMOSDummy_Length=None,  # None/number
        _Slv_Xgate2_PMOSDummy_Placement=None,  # None/'Up'/'Dn'

        ## Slave Nor1
        ## PMOS NMOS Common
        # _Slv_Nor1_NumberofGate = 2, # number
        _Slv_Nor1_Channel_Length=30,  # number
        _Slv_Nor1_GateSpacing=None,  # number/None
        _Slv_Nor1_SDWidth=None,  # number/None
        _Slv_Nor1_PCCrit=True,  # None/True

        ## NMOS
        _Slv_Nor1_NMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
        ## NMOSA
        _Slv_Nor1_NMOSA_NumberofGate=2,
        _Slv_Nor1_NMOSA_Channel_Width=200,  # number
        _Slv_Nor1_NMOSA_Dummy_Length=None,  # None/number
        _Slv_Nor1_NMOSA_Dummy_Placement=None,  # None/'Up'/'Dn'
        ## NMOSB
        _Slv_Nor1_NMOSB_NumberofGate=2,
        _Slv_Nor1_NMOSB_Channel_Width=200,  # number
        _Slv_Nor1_NMOSB_Dummy_Length=None,  # None/number
        _Slv_Nor1_NMOSB_Dummy_Placement=None,  # None/'Up'/'Dn'

        ## PMOS
        _Slv_Nor1_PMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
        ## PMOSA
        _Slv_Nor1_PMOSA_NumberofGate=2,
        _Slv_Nor1_PMOSA_Channel_Width=800,  # number
        _Slv_Nor1_PMOSA_Dummy_Length=None,  # None/number
        _Slv_Nor1_PMOSA_Dummy_Placement=None,  # None/'Up'/'Dn'
        ## PMOSB
        _Slv_Nor1_PMOSB_NumberofGate=2,
        _Slv_Nor1_PMOSB_Channel_Width=800,  # number
        _Slv_Nor1_PMOSB_Dummy_Length=None,  # None/number
        _Slv_Nor1_PMOSB_Dummy_Placement=None,  # None/'Up'/'Dn'

        ## Slave Nor2
        ## PMOS NMOS Common
        # _Slv_Nor2_NumberofGate = 2, # number
        _Slv_Nor2_Channel_Length=30,  # number
        _Slv_Nor2_GateSpacing=None,  # number/None
        _Slv_Nor2_SDWidth=None,  # number/None
        _Slv_Nor2_PCCrit=True,  # None/True

        ## NMOS
        _Slv_Nor2_NMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
        ## NMOSA
        _Slv_Nor2_NMOSA_NumberofGate=2,
        _Slv_Nor2_NMOSA_Channel_Width=200,  # number
        _Slv_Nor2_NMOSA_Dummy_Length=None,  # None/number
        _Slv_Nor2_NMOSA_Dummy_Placement=None,  # None/'Up'/'Dn'
        ## NMOSB
        _Slv_Nor2_NMOSB_NumberofGate=2,
        _Slv_Nor2_NMOSB_Channel_Width=200,  # number
        _Slv_Nor2_NMOSB_Dummy_Length=None,  # None/number
        _Slv_Nor2_NMOSB_Dummy_Placement=None,  # None/'Up'/'Dn'

        ## PMOS
        _Slv_Nor2_PMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
        ## PMOSA
        _Slv_Nor2_PMOSA_NumberofGate=2,
        _Slv_Nor2_PMOSA_Channel_Width=800,  # number
        _Slv_Nor2_PMOSA_Dummy_Length=None,  # None/number
        _Slv_Nor2_PMOSA_Dummy_Placement=None,  # None/'Up'/'Dn'
        ## PMOSB
        _Slv_Nor2_PMOSB_NumberofGate=2,
        _Slv_Nor2_PMOSB_Channel_Width=800,  # number
        _Slv_Nor2_PMOSB_Dummy_Length=None,  # None/number
        _Slv_Nor2_PMOSB_Dummy_Placement=None,  # None/'Up'/'Dn'

        ## Slave Inv1: Reset Pre-driver
        ## PMOS NMOS Common
        _Slv_Inv1_NumberofGate=2,  # number
        _Slv_Inv1_Channel_Length=30,  # number
        _Slv_Inv1_GateSpacing=None,  # number/None
        _Slv_Inv1_SDWidth=None,  # number/None
        _Slv_Inv1_PCCrit=True,  # None/True

        ## NMOS
        _Slv_Inv1_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Slv_Inv1_NMOS_Channel_Width=200,  # number
        _Slv_Inv1_NMOS_Dummy_Length=None,  # None/number
        _Slv_Inv1_NMOS_Dummy_Placement=None,  # None/'Up'/'Dn'

        ## PMOS
        _Slv_Inv1_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Slv_Inv1_PMOS_Channel_Width=400,  # number
        _Slv_Inv1_PMOS_Dummy_Length=None,  # None/number
        _Slv_Inv1_PMOS_Dummy_Placement=None,  # None/'Up'/'Dn'

        ## Slave Inv2: Reset driver
        ## PMOS NMOS Common
        _Slv_Inv2_NumberofGate=1,  # number
        _Slv_Inv2_Channel_Length=30,  # number
        _Slv_Inv2_GateSpacing=None,  # number/None
        _Slv_Inv2_SDWidth=None,  # number/None
        _Slv_Inv2_PCCrit=True,  # None/True

        ## NMOS
        _Slv_Inv2_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Slv_Inv2_NMOS_Channel_Width=200,  # number
        _Slv_Inv2_NMOS_Dummy_Length=None,  # None/number
        _Slv_Inv2_NMOS_Dummy_Placement=None,  # None/'Up'/'Dn'

        ## PMOS
        _Slv_Inv2_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Slv_Inv2_PMOS_Channel_Width=400,  # number
        _Slv_Inv2_PMOS_Dummy_Length=None,  # None/number
        _Slv_Inv2_PMOS_Dummy_Placement=None,  # None/'Up'/'Dn'

        ## Inv3: QB
        ## PMOS NMOS Common
        _Qb_Inv3_NumberofGate=1,  # number
        _Qb_Inv3_Channel_Length=30,  # number
        _Qb_Inv3_GateSpacing=None,  # number/None
        _Qb_Inv3_SDWidth=None,  # number/None
        _Qb_Inv3_PCCrit=True,  # None/True

        ## NMOS
        _Qb_Inv3_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Qb_Inv3_NMOS_Channel_Width=200,  # number
        _Qb_Inv3_NMOS_Dummy_Length=None,  # None/number
        _Qb_Inv3_NMOS_Dummy_Placement=None,  # None/'Up'/'Dn'

        ## PMOS
        _Qb_Inv3_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Qb_Inv3_PMOS_Channel_Width=400,  # number
        _Qb_Inv3_PMOS_Dummy_Length=None,  # None/number
        _Qb_Inv3_PMOS_Dummy_Placement=None,  # None/'Up'/'Dn'
    )

    ## Initially Generated _DesignParameter
    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
            _Name=self._NameDeclaration(_Name=_Name),
            _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
            )

    ## DesignParameter Calculation
    def _CalculateDesignParameter(self,
                                  _Test_distance=500,

                                  ## DFF Common
                                  _DFF_Pbody_NumCont=2,  # number
                                  _DFF_Nbody_NumCont=2,  # number
                                  _DFF_PMOSXvt2NMOSXvt=1500,  # number
                                  _DFF_XlvtTop2Pdoby=None,  # number/None(Minimum)
                                  _DFF_Xlvtdown2Ndoby=None,  # number/None(Minimum)

                                  ## Master Xgate1
                                  ## PMOS NMOS common
                                  _Mst_Xgate1_NumberofGate=1,  # number
                                  _Mst_Xgate1_Channel_Length=30,  # number
                                  _Mst_Xgate1_GateSpacing=None,  # number/None
                                  _Mst_Xgate1_SDWidth=None,  # number/None
                                  _Mst_Xgate1_PCCrit=True,  # None/True

                                  ## NMOS
                                  _Mst_Xgate1_NMOSChannel_Width=100,  # number
                                  _Mst_Xgate1_NMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Mst_Xgate1_NMOSDummy_Length=None,  # None/number
                                  _Mst_Xgate1_NMOSDummy_Placement=None,  # None/'Up'/'Dn'

                                  ## PMOS
                                  _Mst_Xgate1_PMOSChannel_Width=200,  # number
                                  _Mst_Xgate1_PMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Mst_Xgate1_PMOSDummy_Length=None,  # None/number
                                  _Mst_Xgate1_PMOSDummy_Placement=None,  # None/'Up'/'Dn'

                                  ## Master Xgate2
                                  ## PMOS NMOS common
                                  _Mst_Xgate2_NumberofGate=1,  # number
                                  _Mst_Xgate2_Channel_Length=30,  # number
                                  _Mst_Xgate2_GateSpacing=None,  # number/None
                                  _Mst_Xgate2_SDWidth=None,  # number/None
                                  _Mst_Xgate2_PCCrit=True,  # None/True

                                  ## NMOS
                                  _Mst_Xgate2_NMOSChannel_Width=100,  # number
                                  _Mst_Xgate2_NMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Mst_Xgate2_NMOSDummy_Length=None,  # None/number
                                  _Mst_Xgate2_NMOSDummy_Placement=None,  # None/'Up'/'Dn'

                                  ## PMOS
                                  _Mst_Xgate2_PMOSChannel_Width=200,  # number
                                  _Mst_Xgate2_PMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Mst_Xgate2_PMOSDummy_Length=None,  # None/number
                                  _Mst_Xgate2_PMOSDummy_Placement=None,  # None/'Up'/'Dn'

                                  ## Master Nor1
                                  ## PMOS NMOS Common
                                  # _Mst_Nor1_NumberofGate = 2, # number
                                  _Mst_Nor1_Channel_Length=30,  # number
                                  _Mst_Nor1_GateSpacing=None,  # number/None
                                  _Mst_Nor1_SDWidth=None,  # number/None
                                  _Mst_Nor1_PCCrit=True,  # None/True

                                  ## NMOS
                                  _Mst_Nor1_NMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  ## NMOSA
                                  _Mst_Nor1_NMOSA_NumberofGate=2,
                                  _Mst_Nor1_NMOSA_Channel_Width=200,  # number
                                  _Mst_Nor1_NMOSA_Dummy_Length=None,  # None/number
                                  _Mst_Nor1_NMOSA_Dummy_Placement=None,  # None/'Up'/'Dn'
                                  ## NMOSB
                                  _Mst_Nor1_NMOSB_NumberofGate=2,
                                  _Mst_Nor1_NMOSB_Channel_Width=200,  # number
                                  _Mst_Nor1_NMOSB_Dummy_Length=None,  # None/number
                                  _Mst_Nor1_NMOSB_Dummy_Placement=None,  # None/'Up'/'Dn'

                                  ## PMOS
                                  _Mst_Nor1_PMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  ## PMOSA
                                  _Mst_Nor1_PMOSA_NumberofGate=2,
                                  _Mst_Nor1_PMOSA_Channel_Width=800,  # number
                                  _Mst_Nor1_PMOSA_Dummy_Length=None,  # None/number
                                  _Mst_Nor1_PMOSA_Dummy_Placement=None,  # None/'Up'/'Dn'
                                  ## PMOSB
                                  _Mst_Nor1_PMOSB_NumberofGate=2,
                                  _Mst_Nor1_PMOSB_Channel_Width=800,  # number
                                  _Mst_Nor1_PMOSB_Dummy_Length=None,  # None/number
                                  _Mst_Nor1_PMOSB_Dummy_Placement=None,  # None/'Up'/'Dn'

                                  ## Master Nor2
                                  ## PMOS NMOS Common
                                  # _Mst_Nor2_NumberofGate = 2, # number
                                  _Mst_Nor2_Channel_Length=30,  # number
                                  _Mst_Nor2_GateSpacing=None,  # number/None
                                  _Mst_Nor2_SDWidth=None,  # number/None
                                  _Mst_Nor2_PCCrit=True,  # None/True

                                  ## NMOS
                                  _Mst_Nor2_NMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  ## NMOSA
                                  _Mst_Nor2_NMOSA_NumberofGate=2,
                                  _Mst_Nor2_NMOSA_Channel_Width=200,  # number
                                  _Mst_Nor2_NMOSA_Dummy_Length=None,  # None/number
                                  _Mst_Nor2_NMOSA_Dummy_Placement=None,  # None/'Up'/'Dn'
                                  ## NMOSB
                                  _Mst_Nor2_NMOSB_NumberofGate=2,
                                  _Mst_Nor2_NMOSB_Channel_Width=200,  # number
                                  _Mst_Nor2_NMOSB_Dummy_Length=None,  # None/number
                                  _Mst_Nor2_NMOSB_Dummy_Placement=None,  # None/'Up'/'Dn'

                                  ## PMOS
                                  _Mst_Nor2_PMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  ## PMOSA
                                  _Mst_Nor2_PMOSA_NumberofGate=2,
                                  _Mst_Nor2_PMOSA_Channel_Width=800,  # number
                                  _Mst_Nor2_PMOSA_Dummy_Length=None,  # None/number
                                  _Mst_Nor2_PMOSA_Dummy_Placement=None,  # None/'Up'/'Dn'
                                  ## PMOSB
                                  _Mst_Nor2_PMOSB_NumberofGate=2,
                                  _Mst_Nor2_PMOSB_Channel_Width=800,  # number
                                  _Mst_Nor2_PMOSB_Dummy_Length=None,  # None/number
                                  _Mst_Nor2_PMOSB_Dummy_Placement=None,  # None/'Up'/'Dn'

                                  ## Master Inv1: Set Pre-driver
                                  ## PMOS NMOS Common
                                  _Mst_Inv1_NumberofGate=2,  # number
                                  _Mst_Inv1_Channel_Length=30,  # number
                                  _Mst_Inv1_GateSpacing=None,  # number/None
                                  _Mst_Inv1_SDWidth=None,  # number/None
                                  _Mst_Inv1_PCCrit=True,  # None/True

                                  ## NMOS
                                  _Mst_Inv1_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Mst_Inv1_NMOS_Channel_Width=200,  # number
                                  _Mst_Inv1_NMOS_Dummy_Length=None,  # None/number
                                  _Mst_Inv1_NMOS_Dummy_Placement=None,  # None/'Up'/'Dn'

                                  ## PMOS
                                  _Mst_Inv1_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Mst_Inv1_PMOS_Channel_Width=400,  # number
                                  _Mst_Inv1_PMOS_Dummy_Length=None,  # None/number
                                  _Mst_Inv1_PMOS_Dummy_Placement=None,  # None/'Up'/'Dn'

                                  ## Master Inv2: Set driver
                                  ## PMOS NMOS Common
                                  _Mst_Inv2_NumberofGate=1,  # number
                                  _Mst_Inv2_Channel_Length=30,  # number
                                  _Mst_Inv2_GateSpacing=None,  # number/None
                                  _Mst_Inv2_SDWidth=None,  # number/None
                                  _Mst_Inv2_PCCrit=True,  # None/True

                                  ## NMOS
                                  _Mst_Inv2_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Mst_Inv2_NMOS_Channel_Width=200,  # number
                                  _Mst_Inv2_NMOS_Dummy_Length=None,  # None/number
                                  _Mst_Inv2_NMOS_Dummy_Placement=None,  # None/'Up'/'Dn'

                                  ## PMOS
                                  _Mst_Inv2_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Mst_Inv2_PMOS_Channel_Width=400,  # number
                                  _Mst_Inv2_PMOS_Dummy_Length=None,  # None/number
                                  _Mst_Inv2_PMOS_Dummy_Placement=None,  # None/'Up'/'Dn'

                                  ## Inv3: Clock Buffer
                                  ## PMOS NMOS Common
                                  _Clk_Inv3_NumberofGate=1,  # number
                                  _Clk_Inv3_Channel_Length=30,  # number
                                  _Clk_Inv3_GateSpacing=None,  # number/None
                                  _Clk_Inv3_SDWidth=None,  # number/None
                                  _Clk_Inv3_PCCrit=True,  # None/True

                                  ## NMOS
                                  _Clk_Inv3_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Clk_Inv3_NMOS_Channel_Width=200,  # number
                                  _Clk_Inv3_NMOS_Dummy_Length=None,  # None/number
                                  _Clk_Inv3_NMOS_Dummy_Placement=None,  # None/'Up'/'Dn'

                                  ## PMOS
                                  _Clk_Inv3_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Clk_Inv3_PMOS_Channel_Width=400,  # number
                                  _Clk_Inv3_PMOS_Dummy_Length=None,  # None/number
                                  _Clk_Inv3_PMOS_Dummy_Placement=None,  # None/'Up'/'Dn'

                                  ## Slave Xgate1
                                  ## PMOS NMOS common
                                  _Slv_Xgate1_NumberofGate=1,  # number
                                  _Slv_Xgate1_Channel_Length=30,  # number
                                  _Slv_Xgate1_GateSpacing=None,  # number/None
                                  _Slv_Xgate1_SDWidth=None,  # number/None
                                  _Slv_Xgate1_PCCrit=True,  # None/True

                                  ## NMOS
                                  _Slv_Xgate1_NMOSChannel_Width=100,  # number
                                  _Slv_Xgate1_NMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Slv_Xgate1_NMOSDummy_Length=None,  # None/number
                                  _Slv_Xgate1_NMOSDummy_Placement=None,  # None/'Up'/'Dn'

                                  ## PMOS
                                  _Slv_Xgate1_PMOSChannel_Width=200,  # number
                                  _Slv_Xgate1_PMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Slv_Xgate1_PMOSDummy_Length=None,  # None/number
                                  _Slv_Xgate1_PMOSDummy_Placement=None,  # None/'Up'/'Dn'

                                  ## Slave Xgate2
                                  ## PMOS NMOS common
                                  _Slv_Xgate2_NumberofGate=1,  # number
                                  _Slv_Xgate2_Channel_Length=30,  # number
                                  _Slv_Xgate2_GateSpacing=None,  # number/None
                                  _Slv_Xgate2_SDWidth=None,  # number/None
                                  _Slv_Xgate2_PCCrit=True,  # None/True

                                  ## NMOS
                                  _Slv_Xgate2_NMOSChannel_Width=100,  # number
                                  _Slv_Xgate2_NMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Slv_Xgate2_NMOSDummy_Length=None,  # None/number
                                  _Slv_Xgate2_NMOSDummy_Placement=None,  # None/'Up'/'Dn'

                                  ## PMOS
                                  _Slv_Xgate2_PMOSChannel_Width=200,  # number
                                  _Slv_Xgate2_PMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Slv_Xgate2_PMOSDummy_Length=None,  # None/number
                                  _Slv_Xgate2_PMOSDummy_Placement=None,  # None/'Up'/'Dn'

                                  ## Slave Nor1
                                  ## PMOS NMOS Common
                                  # _Slv_Nor1_NumberofGate = 2, # number
                                  _Slv_Nor1_Channel_Length=30,  # number
                                  _Slv_Nor1_GateSpacing=None,  # number/None
                                  _Slv_Nor1_SDWidth=None,  # number/None
                                  _Slv_Nor1_PCCrit=True,  # None/True

                                  ## NMOS
                                  _Slv_Nor1_NMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  ## NMOSA
                                  _Slv_Nor1_NMOSA_NumberofGate=2,
                                  _Slv_Nor1_NMOSA_Channel_Width=200,  # number
                                  _Slv_Nor1_NMOSA_Dummy_Length=None,  # None/number
                                  _Slv_Nor1_NMOSA_Dummy_Placement=None,  # None/'Up'/'Dn'
                                  ## NMOSB
                                  _Slv_Nor1_NMOSB_NumberofGate=2,
                                  _Slv_Nor1_NMOSB_Channel_Width=200,  # number
                                  _Slv_Nor1_NMOSB_Dummy_Length=None,  # None/number
                                  _Slv_Nor1_NMOSB_Dummy_Placement=None,  # None/'Up'/'Dn'

                                  ## PMOS
                                  _Slv_Nor1_PMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  ## PMOSA
                                  _Slv_Nor1_PMOSA_NumberofGate=2,
                                  _Slv_Nor1_PMOSA_Channel_Width=800,  # number
                                  _Slv_Nor1_PMOSA_Dummy_Length=None,  # None/number
                                  _Slv_Nor1_PMOSA_Dummy_Placement=None,  # None/'Up'/'Dn'
                                  ## PMOSB
                                  _Slv_Nor1_PMOSB_NumberofGate=2,
                                  _Slv_Nor1_PMOSB_Channel_Width=800,  # number
                                  _Slv_Nor1_PMOSB_Dummy_Length=None,  # None/number
                                  _Slv_Nor1_PMOSB_Dummy_Placement=None,  # None/'Up'/'Dn'

                                  ## Slave Nor2
                                  ## PMOS NMOS Common
                                  # _Slv_Nor2_NumberofGate = 2, # number
                                  _Slv_Nor2_Channel_Length=30,  # number
                                  _Slv_Nor2_GateSpacing=None,  # number/None
                                  _Slv_Nor2_SDWidth=None,  # number/None
                                  _Slv_Nor2_PCCrit=True,  # None/True

                                  ## NMOS
                                  _Slv_Nor2_NMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  ## NMOSA
                                  _Slv_Nor2_NMOSA_NumberofGate=2,
                                  _Slv_Nor2_NMOSA_Channel_Width=200,  # number
                                  _Slv_Nor2_NMOSA_Dummy_Length=None,  # None/number
                                  _Slv_Nor2_NMOSA_Dummy_Placement=None,  # None/'Up'/'Dn'
                                  ## NMOSB
                                  _Slv_Nor2_NMOSB_NumberofGate=2,
                                  _Slv_Nor2_NMOSB_Channel_Width=200,  # number
                                  _Slv_Nor2_NMOSB_Dummy_Length=None,  # None/number
                                  _Slv_Nor2_NMOSB_Dummy_Placement=None,  # None/'Up'/'Dn'

                                  ## PMOS
                                  _Slv_Nor2_PMOS_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  ## PMOSA
                                  _Slv_Nor2_PMOSA_NumberofGate=2,
                                  _Slv_Nor2_PMOSA_Channel_Width=800,  # number
                                  _Slv_Nor2_PMOSA_Dummy_Length=None,  # None/number
                                  _Slv_Nor2_PMOSA_Dummy_Placement=None,  # None/'Up'/'Dn'
                                  ## PMOSB
                                  _Slv_Nor2_PMOSB_NumberofGate=2,
                                  _Slv_Nor2_PMOSB_Channel_Width=800,  # number
                                  _Slv_Nor2_PMOSB_Dummy_Length=None,  # None/number
                                  _Slv_Nor2_PMOSB_Dummy_Placement=None,  # None/'Up'/'Dn'

                                  ## Slave Inv1: Reset Pre-driver
                                  ## PMOS NMOS Common
                                  _Slv_Inv1_NumberofGate=2,  # number
                                  _Slv_Inv1_Channel_Length=30,  # number
                                  _Slv_Inv1_GateSpacing=None,  # number/None
                                  _Slv_Inv1_SDWidth=None,  # number/None
                                  _Slv_Inv1_PCCrit=True,  # None/True

                                  ## NMOS
                                  _Slv_Inv1_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Slv_Inv1_NMOS_Channel_Width=200,  # number
                                  _Slv_Inv1_NMOS_Dummy_Length=None,  # None/number
                                  _Slv_Inv1_NMOS_Dummy_Placement=None,  # None/'Up'/'Dn'

                                  ## PMOS
                                  _Slv_Inv1_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Slv_Inv1_PMOS_Channel_Width=400,  # number
                                  _Slv_Inv1_PMOS_Dummy_Length=None,  # None/number
                                  _Slv_Inv1_PMOS_Dummy_Placement=None,  # None/'Up'/'Dn'

                                  ## Slave Inv2: Reset driver
                                  ## PMOS NMOS Common
                                  _Slv_Inv2_NumberofGate=1,  # number
                                  _Slv_Inv2_Channel_Length=30,  # number
                                  _Slv_Inv2_GateSpacing=None,  # number/None
                                  _Slv_Inv2_SDWidth=None,  # number/None
                                  _Slv_Inv2_PCCrit=True,  # None/True

                                  ## NMOS
                                  _Slv_Inv2_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Slv_Inv2_NMOS_Channel_Width=200,  # number
                                  _Slv_Inv2_NMOS_Dummy_Length=None,  # None/number
                                  _Slv_Inv2_NMOS_Dummy_Placement=None,  # None/'Up'/'Dn'

                                  ## PMOS
                                  _Slv_Inv2_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Slv_Inv2_PMOS_Channel_Width=400,  # number
                                  _Slv_Inv2_PMOS_Dummy_Length=None,  # None/number
                                  _Slv_Inv2_PMOS_Dummy_Placement=None,  # None/'Up'/'Dn'

                                  ## Inv3: QB
                                  ## PMOS NMOS Common
                                  _Qb_Inv3_NumberofGate=1,  # number
                                  _Qb_Inv3_Channel_Length=30,  # number
                                  _Qb_Inv3_GateSpacing=None,  # number/None
                                  _Qb_Inv3_SDWidth=None,  # number/None
                                  _Qb_Inv3_PCCrit=True,  # None/True

                                  ## NMOS
                                  _Qb_Inv3_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Qb_Inv3_NMOS_Channel_Width=200,  # number
                                  _Qb_Inv3_NMOS_Dummy_Length=None,  # None/number
                                  _Qb_Inv3_NMOS_Dummy_Placement=None,  # None/'Up'/'Dn'

                                  ## PMOS
                                  _Qb_Inv3_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Qb_Inv3_PMOS_Channel_Width=400,  # number
                                  _Qb_Inv3_PMOS_Dummy_Length=None,  # None/number
                                  _Qb_Inv3_PMOS_Dummy_Placement=None,  # None/'Up'/'Dn'

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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Cal PMOS XvtTop2Pbody and NMOS XvtDown2Nbody
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Cal PMOS XvtTop2Pbody and NMOS XvtDown2Nbody : Master Xgate1
        ## Pre-defined
        XvtTop2Pbody_tmp = 0
        XvtDown2Nbody_tmp = 0

        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_PMOSA_power_v2._PMOSA_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D01_02_Xgate_KJH1._Xgate._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_PMOSAPOWER_PbodyContact_1_Length']  = _PMOSAPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_NMOSNumberofGate']        = _Mst_Xgate1_NumberofGate
        _Caculation_Parameters['_NMOS_NMOSChannelWidth']        = _Mst_Xgate1_NMOSChannel_Width
        _Caculation_Parameters['_NMOS_NMOSChannellength']       = _Mst_Xgate1_Channel_Length
        _Caculation_Parameters['_NMOS_GateSpacing']             = _Mst_Xgate1_GateSpacing
        _Caculation_Parameters['_NMOS_SDWidth']                 = _Mst_Xgate1_SDWidth
        _Caculation_Parameters['_NMOS_XVT']                     = _Mst_Xgate1_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit']                  = _Mst_Xgate1_PCCrit
        _Caculation_Parameters['_NMOS_Source_Via_TF']           = True
        _Caculation_Parameters['_NMOS_Drain_Via_TF']            = True
        _Caculation_Parameters['_NMOS_NMOSDummy']               = True
        _Caculation_Parameters['_NMOS_NMOSDummy_length']        = _Mst_Xgate1_NMOSDummy_Length
        _Caculation_Parameters['_NMOS_NMOSDummy_placement']     = _Mst_Xgate1_NMOSDummy_Placement
        _Caculation_Parameters['_NMOS_Pbody_NumCont']           = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XlvtTop2Pdoby']     = _DFF_XlvtTop2Pdoby

        _Caculation_Parameters['_PMOS_PMOSNumberofGate']        = _Mst_Xgate1_NumberofGate
        _Caculation_Parameters['_PMOS_PMOSChannelWidth']        = _Mst_Xgate1_PMOSChannel_Width
        _Caculation_Parameters['_PMOS_PMOSChannellength']       = _Mst_Xgate1_Channel_Length
        _Caculation_Parameters['_PMOS_GateSpacing']             = _Mst_Xgate1_GateSpacing
        _Caculation_Parameters['_PMOS_SDWidth']                 = _Mst_Xgate1_SDWidth
        _Caculation_Parameters['_PMOS_XVT']                     = _Mst_Xgate1_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit']                  = _Mst_Xgate1_PCCrit
        _Caculation_Parameters['_PMOS_Source_Via_TF']           = True
        _Caculation_Parameters['_PMOS_Drain_Via_TF']            = True
        _Caculation_Parameters['_PMOS_PMOSDummy']               = True
        _Caculation_Parameters['_PMOS_PMOSDummy_length']        = _Mst_Xgate1_PMOSDummy_Length
        _Caculation_Parameters['_PMOS_PMOSDummy_placement']     = _Mst_Xgate1_PMOSDummy_Placement
        _Caculation_Parameters['_PMOS_Nbody_NumCont']           = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xlvtdown2Ndoby']    = _DFF_Xlvtdown2Ndoby

        _Caculation_Parameters['_PMOSXvt2NMOSXvt']              = _DFF_PMOSXvt2NMOSXvt


        ## Generate Sref: ex)self._DesignParameter['_PMOSA_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_PMOSA_power_v2._PMOSA_POWER( _DesignParameter=None, _Name='{}:PMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Mst_Xgate1'] = self._SrefElementDeclaration(_DesignObj=D01_02_Xgate_KJH1._Xgate(_DesignParameter=None, _Name='{}:SRF_Mst_Xgate1'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_PMOSA_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Mst_Xgate1']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_Mst_Xgate1']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_Mst_Xgate1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_Mst_Xgate1']['_XYCoordinates'] = [[0, 0]]

        ## Find XvtTop2Pbody_tmp and XvtDown2Nbody_tmp
        #tmp = self.get_param_KJH4('')


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Xgate2
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_PMOSA_power_v2._PMOSA_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D01_02_Xgate_KJH1._Xgate._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_PMOSAPOWER_PbodyContact_1_Length']  = _PMOSAPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_NMOSNumberofGate']        = _Mst_Xgate2_NumberofGate
        _Caculation_Parameters['_NMOS_NMOSChannelWidth']        = _Mst_Xgate2_NMOSChannel_Width
        _Caculation_Parameters['_NMOS_NMOSChannellength']       = _Mst_Xgate2_Channel_Length
        _Caculation_Parameters['_NMOS_GateSpacing']             = _Mst_Xgate2_GateSpacing
        _Caculation_Parameters['_NMOS_SDWidth']                 = _Mst_Xgate2_SDWidth
        _Caculation_Parameters['_NMOS_XVT']                     = _Mst_Xgate2_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit']                  = _Mst_Xgate2_PCCrit
        _Caculation_Parameters['_NMOS_Source_Via_TF']           = True
        _Caculation_Parameters['_NMOS_Drain_Via_TF']            = True
        _Caculation_Parameters['_NMOS_NMOSDummy']               = True
        _Caculation_Parameters['_NMOS_NMOSDummy_length']        = _Mst_Xgate2_NMOSDummy_Length
        _Caculation_Parameters['_NMOS_NMOSDummy_placement']     = _Mst_Xgate2_NMOSDummy_Placement
        _Caculation_Parameters['_NMOS_Pbody_NumCont']           = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XlvtTop2Pdoby']     = _DFF_XlvtTop2Pdoby

        _Caculation_Parameters['_PMOS_PMOSNumberofGate']        = _Mst_Xgate2_NumberofGate
        _Caculation_Parameters['_PMOS_PMOSChannelWidth']        = _Mst_Xgate2_PMOSChannel_Width
        _Caculation_Parameters['_PMOS_PMOSChannellength']       = _Mst_Xgate2_Channel_Length
        _Caculation_Parameters['_PMOS_GateSpacing']             = _Mst_Xgate2_GateSpacing
        _Caculation_Parameters['_PMOS_SDWidth']                 = _Mst_Xgate2_SDWidth
        _Caculation_Parameters['_PMOS_XVT']                     = _Mst_Xgate2_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit']                  = _Mst_Xgate2_PCCrit
        _Caculation_Parameters['_PMOS_Source_Via_TF']           = True
        _Caculation_Parameters['_PMOS_Drain_Via_TF']            = True
        _Caculation_Parameters['_PMOS_PMOSDummy']               = True
        _Caculation_Parameters['_PMOS_PMOSDummy_length']        = _Mst_Xgate2_PMOSDummy_Length
        _Caculation_Parameters['_PMOS_PMOSDummy_placement']     = _Mst_Xgate2_PMOSDummy_Placement
        _Caculation_Parameters['_PMOS_Nbody_NumCont']           = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xlvtdown2Ndoby']    = _DFF_Xlvtdown2Ndoby

        _Caculation_Parameters['_PMOSXvt2NMOSXvt']              = _DFF_PMOSXvt2NMOSXvt


        ## Generate Sref: ex)self._DesignParameter['_PMOSA_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_PMOSA_power_v2._PMOSA_POWER( _DesignParameter=None, _Name='{}:PMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Mst_Xgate2'] = self._SrefElementDeclaration(_DesignObj=D01_02_Xgate_KJH1._Xgate(_DesignParameter=None, _Name='{}:SRF_Mst_Xgate2'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_PMOSA_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Mst_Xgate2']['_Reflect'] = [1, 0, 0]

        ## Define Sref Angle: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_Mst_Xgate2']['_Angle'] = 180

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_Mst_Xgate2']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_Mst_Xgate2']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Mst_Xgate2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        tmp1_1 = self.get_param_KJH4('SRF_Mst_Xgate1','SRF_PMOS','SRF_PMOS','BND_PODummyLayer')
        target_coordx = tmp1_1[0][0][0][-1][0]['_XY_right'][0]
                                ##y
        tmp1_2 = self.get_param_KJH4('SRF_Mst_Xgate1','SRF_PMOS','SRF_PMOS','BND_{}Layer'.format(_Mst_Xgate1_PMOS_XVT))
        target_coordy = tmp1_2[0][0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##X
        tmp2_1 = self.get_param_KJH4('SRF_Mst_Xgate2','SRF_PMOS','SRF_PMOS','BND_PODummyLayer')
        approaching_coordx = tmp2_1[0][0][0][-1][0]['_XY_right'][0]
                                ##Y
        tmp2_2 = self.get_param_KJH4('SRF_Mst_Xgate2','SRF_PMOS','SRF_PMOS','BND_{}Layer'.format(_Mst_Xgate2_PMOS_XVT))
        approaching_coordy = tmp2_2[0][0][0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Mst_Xgate2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] +  _Test_distance
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Mst_Xgate2']['_XYCoordinates'] = tmpXY



        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Nor1
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_PMOSA_power_v2._PMOSA_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D02_02_Nor_KJH0._Nor._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_PMOSAPOWER_PbodyContact_1_Length']  = _PMOSAPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOSA_NMOSNumberofGate']        = _Mst_Nor1_NMOSA_NumberofGate
        _Caculation_Parameters['_NMOSA_NMOSChannelWidth']        = _Mst_Nor1_NMOSA_Channel_Width
        _Caculation_Parameters['_NMOSA_NMOSChannellength']       = _Mst_Nor1_Channel_Length
        _Caculation_Parameters['_NMOSA_GateSpacing']             = _Mst_Nor1_GateSpacing
        _Caculation_Parameters['_NMOSA_SDWidth']                 = _Mst_Nor1_SDWidth
        _Caculation_Parameters['_NMOSA_XVT']                     = _Mst_Nor1_NMOS_XVT
        _Caculation_Parameters['_NMOSA_PCCrit']                  = _Mst_Nor1_PCCrit
        _Caculation_Parameters['_NMOSA_Source_Via_TF']           = False
        _Caculation_Parameters['_NMOSA_Drain_Via_TF']            = True
        _Caculation_Parameters['_NMOSA_NMOSDummy']               = True
        _Caculation_Parameters['_NMOSA_NMOSDummy_length']        = _Mst_Nor1_NMOSA_Dummy_Length
        _Caculation_Parameters['_NMOSA_NMOSDummy_placement']     = _Mst_Nor1_NMOSA_Dummy_Placement

        _Caculation_Parameters['_NMOSB_NMOSNumberofGate']        = _Mst_Nor1_NMOSB_NumberofGate
        _Caculation_Parameters['_NMOSB_NMOSChannelWidth']        = _Mst_Nor1_NMOSB_Channel_Width
        _Caculation_Parameters['_NMOSB_NMOSChannellength']       = _Mst_Nor1_Channel_Length
        _Caculation_Parameters['_NMOSB_GateSpacing']             = _Mst_Nor1_GateSpacing
        _Caculation_Parameters['_NMOSB_SDWidth']                 = _Mst_Nor1_SDWidth
        _Caculation_Parameters['_NMOSB_XVT']                     = _Mst_Nor1_NMOS_XVT
        _Caculation_Parameters['_NMOSB_PCCrit']                  = _Mst_Nor1_PCCrit
        _Caculation_Parameters['_NMOSB_Source_Via_TF']           = False
        _Caculation_Parameters['_NMOSB_Drain_Via_TF']            = True
        _Caculation_Parameters['_NMOSB_NMOSDummy']               = True
        _Caculation_Parameters['_NMOSB_NMOSDummy_length']        = _Mst_Nor1_NMOSB_Dummy_Length
        _Caculation_Parameters['_NMOSB_NMOSDummy_placement']     = _Mst_Nor1_NMOSB_Dummy_Placement

        _Caculation_Parameters['_NMOSAB_Pbody_NumCont']           = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOSAB_Pbody_XlvtTop2Pdoby']     = _DFF_XlvtTop2Pdoby

        _Caculation_Parameters['_PMOSA_PMOSNumberofGate']        = _Mst_Nor1_PMOSA_NumberofGate
        _Caculation_Parameters['_PMOSA_PMOSChannelWidth']        = _Mst_Nor1_PMOSA_Channel_Width
        _Caculation_Parameters['_PMOSA_PMOSChannellength']       = _Mst_Nor1_Channel_Length
        _Caculation_Parameters['_PMOSA_GateSpacing']             = _Mst_Nor1_GateSpacing
        _Caculation_Parameters['_PMOSA_SDWidth']                 = _Mst_Nor1_SDWidth
        _Caculation_Parameters['_PMOSA_XVT']                     = _Mst_Nor1_PMOS_XVT
        _Caculation_Parameters['_PMOSA_PCCrit']                  = _Mst_Nor1_PCCrit
        _Caculation_Parameters['_PMOSA_Source_Via_TF']           = False
        _Caculation_Parameters['_PMOSA_Drain_Via_TF']            = True
        _Caculation_Parameters['_PMOSA_PMOSDummy']               = True
        _Caculation_Parameters['_PMOSA_PMOSDummy_length']        = _Mst_Nor1_PMOSA_Dummy_Length
        _Caculation_Parameters['_PMOSA_PMOSDummy_placement']     = _Mst_Nor1_PMOSA_Dummy_Placement

        _Caculation_Parameters['_PMOSB_PMOSNumberofGate']        = _Mst_Nor1_PMOSB_NumberofGate
        _Caculation_Parameters['_PMOSB_PMOSChannelWidth']        = _Mst_Nor1_PMOSB_Channel_Width
        _Caculation_Parameters['_PMOSB_PMOSChannellength']       = _Mst_Nor1_Channel_Length
        _Caculation_Parameters['_PMOSB_GateSpacing']             = _Mst_Nor1_GateSpacing
        _Caculation_Parameters['_PMOSB_SDWidth']                 = _Mst_Nor1_SDWidth
        _Caculation_Parameters['_PMOSB_XVT']                     = _Mst_Nor1_PMOS_XVT
        _Caculation_Parameters['_PMOSB_PCCrit']                  = _Mst_Nor1_PCCrit
        _Caculation_Parameters['_PMOSB_Source_Via_TF']           = True
        _Caculation_Parameters['_PMOSB_Drain_Via_TF']            = True
        _Caculation_Parameters['_PMOSB_PMOSDummy']               = True
        _Caculation_Parameters['_PMOSB_PMOSDummy_length']        = _Mst_Nor1_PMOSB_Dummy_Length
        _Caculation_Parameters['_PMOSB_PMOSDummy_placement']     = _Mst_Nor1_PMOSB_Dummy_Placement

        _Caculation_Parameters['_PMOSAB_Nbody_NumCont']          = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOSAB_Nbody_Xlvtdown2Ndoby']   = _DFF_Xlvtdown2Ndoby

        _Caculation_Parameters['_PMOSXvt2NMOSXvt']               = _DFF_PMOSXvt2NMOSXvt


        ## Generate Sref: ex)self._DesignParameter['_PMOSA_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_PMOSA_power_v2._PMOSA_POWER( _DesignParameter=None, _Name='{}:PMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Mst_Nor1'] = self._SrefElementDeclaration(_DesignObj=D02_02_Nor_KJH0._Nor(_DesignParameter=None, _Name='{}:SRF_Mst_Nor1'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_PMOSA_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Mst_Nor1']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_Mst_Nor1']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_Mst_Nor1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_Mst_Nor1']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Mst_Nor1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        tmp1_1 = self.get_param_KJH4('SRF_Mst_Xgate2','SRF_PMOS','SRF_PMOS','BND_PODummyLayer')
        target_coordx = tmp1_1[0][0][0][0][0]['_XY_left'][0]
                                ##y
        tmp1_2 = self.get_param_KJH4('SRF_Mst_Xgate2','SRF_PMOS','SRF_PMOS','BND_{}Layer'.format(_Mst_Xgate2_PMOS_XVT))
        target_coordy = tmp1_2[0][0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##X
        tmp2_1 = self.get_param_KJH4('SRF_Mst_Nor1','SRF_Pullup','SRF_PMOSA','BND_PODummyLayer')
        approaching_coordx = tmp2_1[0][0][0][0][0]['_XY_left'][0]
                                ##Y
        tmp2_2 = self.get_param_KJH4('SRF_Mst_Nor1','SRF_Pullup','SRF_PMOSA','BND_{}Layer'.format(_Mst_Nor1_PMOS_XVT))
        approaching_coordy = tmp2_2[0][0][0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Mst_Nor1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] +  _Test_distance
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Mst_Nor1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Master Nor2
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_PMOSA_power_v2._PMOSA_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D02_02_Nor_KJH0._Nor._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_PMOSAPOWER_PbodyContact_1_Length']  = _PMOSAPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOSA_NMOSNumberofGate'] = _Mst_Nor2_NMOSA_NumberofGate
        _Caculation_Parameters['_NMOSA_NMOSChannelWidth'] = _Mst_Nor2_NMOSA_Channel_Width
        _Caculation_Parameters['_NMOSA_NMOSChannellength'] = _Mst_Nor2_Channel_Length
        _Caculation_Parameters['_NMOSA_GateSpacing'] = _Mst_Nor2_GateSpacing
        _Caculation_Parameters['_NMOSA_SDWidth'] = _Mst_Nor2_SDWidth
        _Caculation_Parameters['_NMOSA_XVT'] = _Mst_Nor2_NMOS_XVT
        _Caculation_Parameters['_NMOSA_PCCrit'] = _Mst_Nor2_PCCrit
        _Caculation_Parameters['_NMOSA_Source_Via_TF'] = False
        _Caculation_Parameters['_NMOSA_Drain_Via_TF'] = True
        _Caculation_Parameters['_NMOSA_NMOSDummy'] = True
        _Caculation_Parameters['_NMOSA_NMOSDummy_length'] = _Mst_Nor2_NMOSA_Dummy_Length
        _Caculation_Parameters['_NMOSA_NMOSDummy_placement'] = _Mst_Nor2_NMOSA_Dummy_Placement

        _Caculation_Parameters['_NMOSB_NMOSNumberofGate'] = _Mst_Nor2_NMOSB_NumberofGate
        _Caculation_Parameters['_NMOSB_NMOSChannelWidth'] = _Mst_Nor2_NMOSB_Channel_Width
        _Caculation_Parameters['_NMOSB_NMOSChannellength'] = _Mst_Nor2_Channel_Length
        _Caculation_Parameters['_NMOSB_GateSpacing'] = _Mst_Nor2_GateSpacing
        _Caculation_Parameters['_NMOSB_SDWidth'] = _Mst_Nor2_SDWidth
        _Caculation_Parameters['_NMOSB_XVT'] = _Mst_Nor2_NMOS_XVT
        _Caculation_Parameters['_NMOSB_PCCrit'] = _Mst_Nor2_PCCrit
        _Caculation_Parameters['_NMOSB_Source_Via_TF'] = False
        _Caculation_Parameters['_NMOSB_Drain_Via_TF'] = True
        _Caculation_Parameters['_NMOSB_NMOSDummy'] = True
        _Caculation_Parameters['_NMOSB_NMOSDummy_length'] = _Mst_Nor2_NMOSB_Dummy_Length
        _Caculation_Parameters['_NMOSB_NMOSDummy_placement'] = _Mst_Nor2_NMOSB_Dummy_Placement

        _Caculation_Parameters['_NMOSAB_Pbody_NumCont'] = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOSAB_Pbody_XlvtTop2Pdoby'] = _DFF_XlvtTop2Pdoby

        _Caculation_Parameters['_PMOSA_PMOSNumberofGate'] = _Mst_Nor2_PMOSA_NumberofGate
        _Caculation_Parameters['_PMOSA_PMOSChannelWidth'] = _Mst_Nor2_PMOSA_Channel_Width
        _Caculation_Parameters['_PMOSA_PMOSChannellength'] = _Mst_Nor2_Channel_Length
        _Caculation_Parameters['_PMOSA_GateSpacing'] = _Mst_Nor2_GateSpacing
        _Caculation_Parameters['_PMOSA_SDWidth'] = _Mst_Nor2_SDWidth
        _Caculation_Parameters['_PMOSA_XVT'] = _Mst_Nor2_PMOS_XVT
        _Caculation_Parameters['_PMOSA_PCCrit'] = _Mst_Nor2_PCCrit
        _Caculation_Parameters['_PMOSA_Source_Via_TF'] = False
        _Caculation_Parameters['_PMOSA_Drain_Via_TF'] = True
        _Caculation_Parameters['_PMOSA_PMOSDummy'] = True
        _Caculation_Parameters['_PMOSA_PMOSDummy_length'] = _Mst_Nor2_PMOSA_Dummy_Length
        _Caculation_Parameters['_PMOSA_PMOSDummy_placement'] = _Mst_Nor2_PMOSA_Dummy_Placement

        _Caculation_Parameters['_PMOSB_PMOSNumberofGate'] = _Mst_Nor2_PMOSB_NumberofGate
        _Caculation_Parameters['_PMOSB_PMOSChannelWidth'] = _Mst_Nor2_PMOSB_Channel_Width
        _Caculation_Parameters['_PMOSB_PMOSChannellength'] = _Mst_Nor2_Channel_Length
        _Caculation_Parameters['_PMOSB_GateSpacing'] = _Mst_Nor2_GateSpacing
        _Caculation_Parameters['_PMOSB_SDWidth'] = _Mst_Nor2_SDWidth
        _Caculation_Parameters['_PMOSB_XVT'] = _Mst_Nor2_PMOS_XVT
        _Caculation_Parameters['_PMOSB_PCCrit'] = _Mst_Nor2_PCCrit
        _Caculation_Parameters['_PMOSB_Source_Via_TF'] = True
        _Caculation_Parameters['_PMOSB_Drain_Via_TF'] = True
        _Caculation_Parameters['_PMOSB_PMOSDummy'] = True
        _Caculation_Parameters['_PMOSB_PMOSDummy_length'] = _Mst_Nor2_PMOSB_Dummy_Length
        _Caculation_Parameters['_PMOSB_PMOSDummy_placement'] = _Mst_Nor2_PMOSB_Dummy_Placement

        _Caculation_Parameters['_PMOSAB_Nbody_NumCont'] = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOSAB_Nbody_Xlvtdown2Ndoby'] = _DFF_Xlvtdown2Ndoby

        _Caculation_Parameters['_PMOSXvt2NMOSXvt'] = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_PMOSA_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_PMOSA_power_v2._PMOSA_POWER( _DesignParameter=None, _Name='{}:PMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Mst_Nor2'] = self._SrefElementDeclaration(_DesignObj=D02_02_Nor_KJH0._Nor(_DesignParameter=None, _Name='{}:SRF_Mst_Nor2'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_PMOSA_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Mst_Nor2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_Mst_Nor2']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_Mst_Nor2']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_Mst_Nor2']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Mst_Nor2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        tmp1_1 = self.get_param_KJH4('SRF_Mst_Nor1','SRF_Pullup','SRF_PMOSB','BND_PODummyLayer')
        target_coordx = tmp1_1[0][0][0][-1][0]['_XY_right'][0]
                                ##y
        tmp1_2 = self.get_param_KJH4('SRF_Mst_Nor1','SRF_Pullup','SRF_PMOSB','BND_{}Layer'.format(_Mst_Nor1_PMOS_XVT))
        target_coordy = tmp1_2[0][0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##X
        tmp2_1 = self.get_param_KJH4('SRF_Mst_Nor2','SRF_Pullup','SRF_PMOSA','BND_PODummyLayer')
        approaching_coordx = tmp2_1[0][0][0][0][0]['_XY_left'][0]
                                ##Y
        tmp2_2 = self.get_param_KJH4('SRF_Mst_Nor2','SRF_Pullup','SRF_PMOSA','BND_{}Layer'.format(_Mst_Nor2_PMOS_XVT))
        approaching_coordy = tmp2_2[0][0][0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Mst_Nor2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] +  _Test_distance
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Mst_Nor2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Inv1: Set pre-driver
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_PMOSA_power_v2._PMOSA_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D00_00_Inverter_KJH1._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_PMOSAPOWER_PbodyContact_1_Length']  = _PMOSAPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_NMOSNumberofGate']        = _Mst_Inv1_NumberofGate
        _Caculation_Parameters['_NMOS_NMOSChannelWidth']        = _Mst_Inv1_NMOS_Channel_Width
        _Caculation_Parameters['_NMOS_NMOSChannellength']       = _Mst_Inv1_Channel_Length
        _Caculation_Parameters['_NMOS_GateSpacing']             = _Mst_Inv1_GateSpacing
        _Caculation_Parameters['_NMOS_SDWidth']                 = _Mst_Inv1_SDWidth
        _Caculation_Parameters['_NMOS_XVT']                     = _Mst_Inv1_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit']                  = _Mst_Inv1_PCCrit
        _Caculation_Parameters['_NMOS_Source_Via_TF']           = False
        _Caculation_Parameters['_NMOS_Drain_Via_TF']            = True
        _Caculation_Parameters['_NMOS_NMOSDummy']               = True
        _Caculation_Parameters['_NMOS_NMOSDummy_length']        = _Mst_Inv1_NMOS_Dummy_Length
        _Caculation_Parameters['_NMOS_NMOSDummy_placement']     = _Mst_Inv1_NMOS_Dummy_Placement

        _Caculation_Parameters['_NMOS_Pbody_NumCont']           = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XlvtTop2Pdoby']     = _DFF_XlvtTop2Pdoby

        _Caculation_Parameters['_PMOS_NMOSNumberofGate']        = _Mst_Inv1_NumberofGate
        _Caculation_Parameters['_PMOS_NMOSChannelWidth']        = _Mst_Inv1_PMOS_Channel_Width
        _Caculation_Parameters['_PMOS_NMOSChannellength']       = _Mst_Inv1_Channel_Length
        _Caculation_Parameters['_PMOS_GateSpacing']             = _Mst_Inv1_GateSpacing
        _Caculation_Parameters['_PMOS_SDWidth']                 = _Mst_Inv1_SDWidth
        _Caculation_Parameters['_PMOS_XVT']                     = _Mst_Inv1_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit']                  = _Mst_Inv1_PCCrit
        _Caculation_Parameters['_PMOS_Source_Via_TF']           = False
        _Caculation_Parameters['_PMOS_Drain_Via_TF']            = True
        _Caculation_Parameters['_PMOS_NMOSDummy']               = True
        _Caculation_Parameters['_PMOS_NMOSDummy_length']        = _Mst_Inv1_PMOS_Dummy_Length
        _Caculation_Parameters['_PMOS_NMOSDummy_placement']     = _Mst_Inv1_PMOS_Dummy_Placement

        _Caculation_Parameters['_PMOS_Nbody_NumCont']           = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xlvtdown2Ndoby']    = _DFF_Xlvtdown2Ndoby

        _Caculation_Parameters['_PMOSXvt2NMOSXvt']              = _DFF_PMOSXvt2NMOSXvt


        ## Generate Sref: ex)self._DesignParameter['_PMOSA_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_PMOSA_power_v2._PMOSA_POWER( _DesignParameter=None, _Name='{}:PMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Mst_Inv1'] = self._SrefElementDeclaration(_DesignObj=D00_00_Inverter_KJH1._Inverter(_DesignParameter=None, _Name='{}:SRF_Mst_Inv1'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_PMOSA_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Mst_Inv1']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_Mst_Inv1']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_Mst_Inv1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_Mst_Inv1']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Mst_Inv1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        tmp1_1 = self.get_param_KJH4('SRF_Mst_Nor2','SRF_Pullup','SRF_PMOSB','BND_PODummyLayer')
        target_coordx = tmp1_1[0][0][0][-1][0]['_XY_right'][0]
                                ##y
        tmp1_2 = self.get_param_KJH4('SRF_Mst_Nor2','SRF_Pullup','SRF_PMOSB','BND_{}Layer'.format(_Mst_Nor2_PMOS_XVT))
        target_coordy = tmp1_2[0][0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##X
        tmp2_1 = self.get_param_KJH4('SRF_Mst_Inv1','SRF_PMOS','BND_PODummyLayer')
        approaching_coordx = tmp2_1[0][0][0][0]['_XY_left'][0]
                                ##Y
        tmp2_2 = self.get_param_KJH4('SRF_Mst_Inv1','SRF_PMOS','BND_{}Layer'.format(_Mst_Inv1_PMOS_XVT))
        approaching_coordy = tmp2_2[0][0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Mst_Inv1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] +  _Test_distance
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Mst_Inv1']['_XYCoordinates'] = tmpXY



        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Inv2: Set driver
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_PMOSA_power_v2._PMOSA_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D00_00_Inverter_KJH1._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_PMOSAPOWER_PbodyContact_1_Length']  = _PMOSAPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_NMOSNumberofGate']        = _Mst_Inv2_NumberofGate
        _Caculation_Parameters['_NMOS_NMOSChannelWidth']        = _Mst_Inv2_NMOS_Channel_Width
        _Caculation_Parameters['_NMOS_NMOSChannellength']       = _Mst_Inv2_Channel_Length
        _Caculation_Parameters['_NMOS_GateSpacing']             = _Mst_Inv2_GateSpacing
        _Caculation_Parameters['_NMOS_SDWidth']                 = _Mst_Inv2_SDWidth
        _Caculation_Parameters['_NMOS_XVT']                     = _Mst_Inv2_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit']                  = _Mst_Inv2_PCCrit
        _Caculation_Parameters['_NMOS_Source_Via_TF']           = False
        _Caculation_Parameters['_NMOS_Drain_Via_TF']            = True
        _Caculation_Parameters['_NMOS_NMOSDummy']               = True
        _Caculation_Parameters['_NMOS_NMOSDummy_length']        = _Mst_Inv2_NMOS_Dummy_Length
        _Caculation_Parameters['_NMOS_NMOSDummy_placement']     = _Mst_Inv2_NMOS_Dummy_Placement

        _Caculation_Parameters['_NMOS_Pbody_NumCont']           = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XlvtTop2Pdoby']     = _DFF_XlvtTop2Pdoby

        _Caculation_Parameters['_PMOS_NMOSNumberofGate']        = _Mst_Inv2_NumberofGate
        _Caculation_Parameters['_PMOS_NMOSChannelWidth']        = _Mst_Inv2_PMOS_Channel_Width
        _Caculation_Parameters['_PMOS_NMOSChannellength']       = _Mst_Inv2_Channel_Length
        _Caculation_Parameters['_PMOS_GateSpacing']             = _Mst_Inv2_GateSpacing
        _Caculation_Parameters['_PMOS_SDWidth']                 = _Mst_Inv2_SDWidth
        _Caculation_Parameters['_PMOS_XVT']                     = _Mst_Inv2_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit']                  = _Mst_Inv2_PCCrit
        _Caculation_Parameters['_PMOS_Source_Via_TF']           = False
        _Caculation_Parameters['_PMOS_Drain_Via_TF']            = True
        _Caculation_Parameters['_PMOS_NMOSDummy']               = True
        _Caculation_Parameters['_PMOS_NMOSDummy_length']        = _Mst_Inv2_PMOS_Dummy_Length
        _Caculation_Parameters['_PMOS_NMOSDummy_placement']     = _Mst_Inv2_PMOS_Dummy_Placement

        _Caculation_Parameters['_PMOS_Nbody_NumCont']           = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xlvtdown2Ndoby']    = _DFF_Xlvtdown2Ndoby

        _Caculation_Parameters['_PMOSXvt2NMOSXvt']              = _DFF_PMOSXvt2NMOSXvt


        ## Generate Sref: ex)self._DesignParameter['_PMOSA_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_PMOSA_power_v2._PMOSA_POWER( _DesignParameter=None, _Name='{}:PMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Mst_Inv2'] = self._SrefElementDeclaration(_DesignObj=D00_00_Inverter_KJH1._Inverter(_DesignParameter=None, _Name='{}:SRF_Mst_Inv2'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_PMOSA_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Mst_Inv2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_Mst_Inv2']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_Mst_Inv2']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_Mst_Inv2']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Mst_Inv2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        tmp1_1 = self.get_param_KJH4('SRF_Mst_Inv1','SRF_PMOS','BND_PODummyLayer')
        target_coordx = tmp1_1[0][0][-1][0]['_XY_right'][0]
                                ##y
        tmp1_2 = self.get_param_KJH4('SRF_Mst_Inv1','SRF_PMOS','BND_{}Layer'.format(_Mst_Inv1_PMOS_XVT))
        target_coordy = tmp1_2[0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##X
        tmp2_1 = self.get_param_KJH4('SRF_Mst_Inv2','SRF_PMOS','BND_PODummyLayer')
        approaching_coordx = tmp2_1[0][0][0][0]['_XY_left'][0]
                                ##Y
        tmp2_2 = self.get_param_KJH4('SRF_Mst_Inv2','SRF_PMOS','BND_{}Layer'.format(_Mst_Inv2_PMOS_XVT))
        approaching_coordy = tmp2_2[0][0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Mst_Inv2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] +  _Test_distance
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Mst_Inv2']['_XYCoordinates'] = tmpXY




        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Inv3: Clock driver
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_PMOSA_power_v2._PMOSA_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D00_00_Inverter_KJH1._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_PMOSAPOWER_PbodyContact_1_Length']  = _PMOSAPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_NMOSNumberofGate']        = _Clk_Inv3_NumberofGate
        _Caculation_Parameters['_NMOS_NMOSChannelWidth']        = _Clk_Inv3_NMOS_Channel_Width
        _Caculation_Parameters['_NMOS_NMOSChannellength']       = _Clk_Inv3_Channel_Length
        _Caculation_Parameters['_NMOS_GateSpacing']             = _Clk_Inv3_GateSpacing
        _Caculation_Parameters['_NMOS_SDWidth']                 = _Clk_Inv3_SDWidth
        _Caculation_Parameters['_NMOS_XVT']                     = _Clk_Inv3_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit']                  = _Clk_Inv3_PCCrit
        _Caculation_Parameters['_NMOS_Source_Via_TF']           = False
        _Caculation_Parameters['_NMOS_Drain_Via_TF']            = True
        _Caculation_Parameters['_NMOS_NMOSDummy']               = True
        _Caculation_Parameters['_NMOS_NMOSDummy_length']        = _Clk_Inv3_NMOS_Dummy_Length
        _Caculation_Parameters['_NMOS_NMOSDummy_placement']     = _Clk_Inv3_NMOS_Dummy_Placement

        _Caculation_Parameters['_NMOS_Pbody_NumCont']           = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XlvtTop2Pdoby']     = _DFF_XlvtTop2Pdoby

        _Caculation_Parameters['_PMOS_NMOSNumberofGate']        = _Clk_Inv3_NumberofGate
        _Caculation_Parameters['_PMOS_NMOSChannelWidth']        = _Clk_Inv3_PMOS_Channel_Width
        _Caculation_Parameters['_PMOS_NMOSChannellength']       = _Clk_Inv3_Channel_Length
        _Caculation_Parameters['_PMOS_GateSpacing']             = _Clk_Inv3_GateSpacing
        _Caculation_Parameters['_PMOS_SDWidth']                 = _Clk_Inv3_SDWidth
        _Caculation_Parameters['_PMOS_XVT']                     = _Clk_Inv3_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit']                  = _Clk_Inv3_PCCrit
        _Caculation_Parameters['_PMOS_Source_Via_TF']           = False
        _Caculation_Parameters['_PMOS_Drain_Via_TF']            = True
        _Caculation_Parameters['_PMOS_NMOSDummy']               = True
        _Caculation_Parameters['_PMOS_NMOSDummy_length']        = _Clk_Inv3_PMOS_Dummy_Length
        _Caculation_Parameters['_PMOS_NMOSDummy_placement']     = _Clk_Inv3_PMOS_Dummy_Placement

        _Caculation_Parameters['_PMOS_Nbody_NumCont']           = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xlvtdown2Ndoby']    = _DFF_Xlvtdown2Ndoby

        _Caculation_Parameters['_PMOSXvt2NMOSXvt']              = _DFF_PMOSXvt2NMOSXvt


        ## Generate Sref: ex)self._DesignParameter['_PMOSA_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_PMOSA_power_v2._PMOSA_POWER( _DesignParameter=None, _Name='{}:PMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Clk_Inv3'] = self._SrefElementDeclaration(_DesignObj=D00_00_Inverter_KJH1._Inverter(_DesignParameter=None, _Name='{}:SRF_Clk_Inv3'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_PMOSA_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Clk_Inv3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_Clk_Inv3']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_Clk_Inv3']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_Clk_Inv3']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Clk_Inv3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        tmp1_1 = self.get_param_KJH4('SRF_Mst_Inv2','SRF_PMOS','BND_PODummyLayer')
        target_coordx = tmp1_1[0][0][-1][0]['_XY_right'][0]
                                ##y
        tmp1_2 = self.get_param_KJH4('SRF_Mst_Inv2','SRF_PMOS','BND_{}Layer'.format(_Mst_Inv1_PMOS_XVT))
        target_coordy = tmp1_2[0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##X
        tmp2_1 = self.get_param_KJH4('SRF_Clk_Inv3','SRF_PMOS','BND_PODummyLayer')
        approaching_coordx = tmp2_1[0][0][0][0]['_XY_left'][0]
                                ##Y
        tmp2_2 = self.get_param_KJH4('SRF_Clk_Inv3','SRF_PMOS','BND_{}Layer'.format(_Mst_Inv2_PMOS_XVT))
        approaching_coordy = tmp2_2[0][0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Clk_Inv3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] +  _Test_distance
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Clk_Inv3']['_XYCoordinates'] = tmpXY

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
    libname = 'Proj_ADC_D04_SARLogic_SetRstDFF_KJH'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'D04_00_SetRstDFF_v0_81'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        _Test_distance = 500,

    ## DFF Common
        _DFF_Pbody_NumCont = 2, # number
        _DFF_Nbody_NumCont = 2, # number
        _DFF_PMOSXvt2NMOSXvt = 1500, # number
        _DFF_XlvtTop2Pdoby = None, # number/None(Minimum)
        _DFF_Xlvtdown2Ndoby = None, # number/None(Minimum)

    ## Master Xgate1
        ## PMOS NMOS common
        _Mst_Xgate1_NumberofGate = 1, # number
        _Mst_Xgate1_Channel_Length = 30, # number
        _Mst_Xgate1_GateSpacing = None, # number/None
        _Mst_Xgate1_SDWidth = None, # number/None
        _Mst_Xgate1_PCCrit = True, # None/True

        ## NMOS
        _Mst_Xgate1_NMOSChannel_Width = 100, # number
        _Mst_Xgate1_NMOS_XVT = 'HVT', #'XVT' ex)SLVT LVT RVT HVT
        _Mst_Xgate1_NMOSDummy_Length = None, # None/number
        _Mst_Xgate1_NMOSDummy_Placement = None, # None/'Up'/'Dn'

        ## PMOS
        _Mst_Xgate1_PMOSChannel_Width = 200, # number
        _Mst_Xgate1_PMOS_XVT = 'HVT', #'XVT' ex)SLVT LVT RVT HVT
        _Mst_Xgate1_PMOSDummy_Length = None, # None/number
        _Mst_Xgate1_PMOSDummy_Placement = None, # None/'Up'/'Dn'

    ## Master Xgate2
        ## PMOS NMOS common
        _Mst_Xgate2_NumberofGate = 1, # number
        _Mst_Xgate2_Channel_Length = 30, # number
        _Mst_Xgate2_GateSpacing = None, # number/None
        _Mst_Xgate2_SDWidth = None, # number/None
        _Mst_Xgate2_PCCrit = True, # None/True

        ## NMOS
        _Mst_Xgate2_NMOSChannel_Width = 100, # number
        _Mst_Xgate2_NMOS_XVT = 'HVT', #'XVT' ex)SLVT LVT RVT HVT
        _Mst_Xgate2_NMOSDummy_Length = None, # None/number
        _Mst_Xgate2_NMOSDummy_Placement = None, # None/'Up'/'Dn'

        ## PMOS
        _Mst_Xgate2_PMOSChannel_Width = 200, # number
        _Mst_Xgate2_PMOS_XVT = 'HVT', #'XVT' ex)SLVT LVT RVT HVT
        _Mst_Xgate2_PMOSDummy_Length = None, # None/number
        _Mst_Xgate2_PMOSDummy_Placement = None, # None/'Up'/'Dn'

    ## Master Nor1
        ## PMOS NMOS Common
        #_Mst_Nor1_NumberofGate = 2, # number
        _Mst_Nor1_Channel_Length = 30, # number
        _Mst_Nor1_GateSpacing = None, # number/None
        _Mst_Nor1_SDWidth = None, # number/None
        _Mst_Nor1_PCCrit = True, # None/True

        ## NMOS
        _Mst_Nor1_NMOS_XVT = 'HVT', #'XVT' ex)SLVT LVT RVT HVT
            ## NMOSA
        _Mst_Nor1_NMOSA_NumberofGate = 2,
        _Mst_Nor1_NMOSA_Channel_Width = 200, # number
        _Mst_Nor1_NMOSA_Dummy_Length = None, # None/number
        _Mst_Nor1_NMOSA_Dummy_Placement = None, # None/'Up'/'Dn'
            ## NMOSB
        _Mst_Nor1_NMOSB_NumberofGate=2,
        _Mst_Nor1_NMOSB_Channel_Width = 200, # number
        _Mst_Nor1_NMOSB_Dummy_Length = None, # None/number
        _Mst_Nor1_NMOSB_Dummy_Placement = None, # None/'Up'/'Dn'

        ## PMOS
        _Mst_Nor1_PMOS_XVT = 'HVT', #'XVT' ex)SLVT LVT RVT HVT
            ## PMOSA
        _Mst_Nor1_PMOSA_NumberofGate = 2,
        _Mst_Nor1_PMOSA_Channel_Width = 800, # number
        _Mst_Nor1_PMOSA_Dummy_Length = None, # None/number
        _Mst_Nor1_PMOSA_Dummy_Placement = None, # None/'Up'/'Dn'
            ## PMOSB
        _Mst_Nor1_PMOSB_NumberofGate=2,
        _Mst_Nor1_PMOSB_Channel_Width = 800, # number
        _Mst_Nor1_PMOSB_Dummy_Length = None, # None/number
        _Mst_Nor1_PMOSB_Dummy_Placement = None, # None/'Up'/'Dn'

    ## Master Nor2
        ## PMOS NMOS Common
        #_Mst_Nor2_NumberofGate = 2, # number
        _Mst_Nor2_Channel_Length = 30, # number
        _Mst_Nor2_GateSpacing = None, # number/None
        _Mst_Nor2_SDWidth = None, # number/None
        _Mst_Nor2_PCCrit = True, # None/True

        ## NMOS
        _Mst_Nor2_NMOS_XVT = 'HVT', #'XVT' ex)SLVT LVT RVT HVT
            ## NMOSA
        _Mst_Nor2_NMOSA_NumberofGate=2,
        _Mst_Nor2_NMOSA_Channel_Width = 200, # number
        _Mst_Nor2_NMOSA_Dummy_Length = None, # None/number
        _Mst_Nor2_NMOSA_Dummy_Placement = None, # None/'Up'/'Dn'
            ## NMOSB
        _Mst_Nor2_NMOSB_NumberofGate=2,
        _Mst_Nor2_NMOSB_Channel_Width = 200, # number
        _Mst_Nor2_NMOSB_Dummy_Length = None, # None/number
        _Mst_Nor2_NMOSB_Dummy_Placement = None, # None/'Up'/'Dn'

        ## PMOS
        _Mst_Nor2_PMOS_XVT = 'HVT', #'XVT' ex)SLVT LVT RVT HVT
            ## PMOSA
        _Mst_Nor2_PMOSA_NumberofGate=2,
        _Mst_Nor2_PMOSA_Channel_Width = 800, # number
        _Mst_Nor2_PMOSA_Dummy_Length = None, # None/number
        _Mst_Nor2_PMOSA_Dummy_Placement = None, # None/'Up'/'Dn'
            ## PMOSB
        _Mst_Nor2_PMOSB_NumberofGate=2,
        _Mst_Nor2_PMOSB_Channel_Width = 800, # number
        _Mst_Nor2_PMOSB_Dummy_Length = None, # None/number
        _Mst_Nor2_PMOSB_Dummy_Placement = None, # None/'Up'/'Dn'

    ## Master Inv1: Set Pre-driver
        ## PMOS NMOS Common
        _Mst_Inv1_NumberofGate = 2, # number
        _Mst_Inv1_Channel_Length = 30, # number
        _Mst_Inv1_GateSpacing = None, # number/None
        _Mst_Inv1_SDWidth = None, # number/None
        _Mst_Inv1_PCCrit = True, # None/True

        ## NMOS
        _Mst_Inv1_NMOS_XVT = 'SLVT', #'XVT' ex)SLVT LVT RVT HVT
        _Mst_Inv1_NMOS_Channel_Width = 200, # number
        _Mst_Inv1_NMOS_Dummy_Length = None, # None/number
        _Mst_Inv1_NMOS_Dummy_Placement = None, # None/'Up'/'Dn'

        ## PMOS
        _Mst_Inv1_PMOS_XVT = 'SLVT', #'XVT' ex)SLVT LVT RVT HVT
        _Mst_Inv1_PMOS_Channel_Width = 400, # number
        _Mst_Inv1_PMOS_Dummy_Length = None, # None/number
        _Mst_Inv1_PMOS_Dummy_Placement = None, # None/'Up'/'Dn'

    ## Master Inv2: Set driver
        ## PMOS NMOS Common
        _Mst_Inv2_NumberofGate = 1, # number
        _Mst_Inv2_Channel_Length = 30, # number
        _Mst_Inv2_GateSpacing = None, # number/None
        _Mst_Inv2_SDWidth = None, # number/None
        _Mst_Inv2_PCCrit = True, # None/True

        ## NMOS
        _Mst_Inv2_NMOS_XVT = 'SLVT', #'XVT' ex)SLVT LVT RVT HVT
        _Mst_Inv2_NMOS_Channel_Width = 200, # number
        _Mst_Inv2_NMOS_Dummy_Length = None, # None/number
        _Mst_Inv2_NMOS_Dummy_Placement = None, # None/'Up'/'Dn'

        ## PMOS
        _Mst_Inv2_PMOS_XVT = 'SLVT', #'XVT' ex)SLVT LVT RVT HVT
        _Mst_Inv2_PMOS_Channel_Width = 400, # number
        _Mst_Inv2_PMOS_Dummy_Length = None, # None/number
        _Mst_Inv2_PMOS_Dummy_Placement = None, # None/'Up'/'Dn'

    ## Inv3: Clock Buffer
        ## PMOS NMOS Common
        _Clk_Inv3_NumberofGate = 1, # number
        _Clk_Inv3_Channel_Length = 30, # number
        _Clk_Inv3_GateSpacing = None, # number/None
        _Clk_Inv3_SDWidth = None, # number/None
        _Clk_Inv3_PCCrit = True, # None/True

        ## NMOS
        _Clk_Inv3_NMOS_XVT = 'SLVT', #'XVT' ex)SLVT LVT RVT HVT
        _Clk_Inv3_NMOS_Channel_Width = 200, # number
        _Clk_Inv3_NMOS_Dummy_Length = None, # None/number
        _Clk_Inv3_NMOS_Dummy_Placement = None, # None/'Up'/'Dn'

        ## PMOS
        _Clk_Inv3_PMOS_XVT = 'SLVT', #'XVT' ex)SLVT LVT RVT HVT
        _Clk_Inv3_PMOS_Channel_Width = 400, # number
        _Clk_Inv3_PMOS_Dummy_Length = None, # None/number
        _Clk_Inv3_PMOS_Dummy_Placement = None, # None/'Up'/'Dn'


    ## Slave Xgate1
        ## PMOS NMOS common
        _Slv_Xgate1_NumberofGate = 1, # number
        _Slv_Xgate1_Channel_Length = 30, # number
        _Slv_Xgate1_GateSpacing = None, # number/None
        _Slv_Xgate1_SDWidth = None, # number/None
        _Slv_Xgate1_PCCrit = True, # None/True

        ## NMOS
        _Slv_Xgate1_NMOSChannel_Width = 100, # number
        _Slv_Xgate1_NMOS_XVT = 'HVT', #'XVT' ex)SLVT LVT RVT HVT
        _Slv_Xgate1_NMOSDummy_Length = None, # None/number
        _Slv_Xgate1_NMOSDummy_Placement = None, # None/'Up'/'Dn'

        ## PMOS
        _Slv_Xgate1_PMOSChannel_Width = 200, # number
        _Slv_Xgate1_PMOS_XVT = 'HVT', #'XVT' ex)SLVT LVT RVT HVT
        _Slv_Xgate1_PMOSDummy_Length = None, # None/number
        _Slv_Xgate1_PMOSDummy_Placement = None, # None/'Up'/'Dn'

    ## Slave Xgate2
        ## PMOS NMOS common
        _Slv_Xgate2_NumberofGate = 1, # number
        _Slv_Xgate2_Channel_Length = 30, # number
        _Slv_Xgate2_GateSpacing = None, # number/None
        _Slv_Xgate2_SDWidth = None, # number/None
        _Slv_Xgate2_PCCrit = True, # None/True

        ## NMOS
        _Slv_Xgate2_NMOSChannel_Width = 100, # number
        _Slv_Xgate2_NMOS_XVT = 'HVT', #'XVT' ex)SLVT LVT RVT HVT
        _Slv_Xgate2_NMOSDummy_Length = None, # None/number
        _Slv_Xgate2_NMOSDummy_Placement = None, # None/'Up'/'Dn'

        ## PMOS
        _Slv_Xgate2_PMOSChannel_Width = 200, # number
        _Slv_Xgate2_PMOS_XVT = 'HVT', #'XVT' ex)SLVT LVT RVT HVT
        _Slv_Xgate2_PMOSDummy_Length = None, # None/number
        _Slv_Xgate2_PMOSDummy_Placement = None, # None/'Up'/'Dn'

    ## Slave Nor1
        ## PMOS NMOS Common
        #_Slv_Nor1_NumberofGate = 2, # number
        _Slv_Nor1_Channel_Length = 30, # number
        _Slv_Nor1_GateSpacing = None, # number/None
        _Slv_Nor1_SDWidth = None, # number/None
        _Slv_Nor1_PCCrit = True, # None/True

        ## NMOS
        _Slv_Nor1_NMOS_XVT = 'HVT', #'XVT' ex)SLVT LVT RVT HVT
            ## NMOSA
        _Slv_Nor1_NMOSA_NumberofGate = 2,
        _Slv_Nor1_NMOSA_Channel_Width = 200, # number
        _Slv_Nor1_NMOSA_Dummy_Length = None, # None/number
        _Slv_Nor1_NMOSA_Dummy_Placement = None, # None/'Up'/'Dn'
            ## NMOSB
        _Slv_Nor1_NMOSB_NumberofGate=2,
        _Slv_Nor1_NMOSB_Channel_Width = 200, # number
        _Slv_Nor1_NMOSB_Dummy_Length = None, # None/number
        _Slv_Nor1_NMOSB_Dummy_Placement = None, # None/'Up'/'Dn'

        ## PMOS
        _Slv_Nor1_PMOS_XVT = 'HVT', #'XVT' ex)SLVT LVT RVT HVT
            ## PMOSA
        _Slv_Nor1_PMOSA_NumberofGate = 2,
        _Slv_Nor1_PMOSA_Channel_Width = 800, # number
        _Slv_Nor1_PMOSA_Dummy_Length = None, # None/number
        _Slv_Nor1_PMOSA_Dummy_Placement = None, # None/'Up'/'Dn'
            ## PMOSB
        _Slv_Nor1_PMOSB_NumberofGate=2,
        _Slv_Nor1_PMOSB_Channel_Width = 800, # number
        _Slv_Nor1_PMOSB_Dummy_Length = None, # None/number
        _Slv_Nor1_PMOSB_Dummy_Placement = None, # None/'Up'/'Dn'

    ## Slave Nor2
        ## PMOS NMOS Common
        #_Slv_Nor2_NumberofGate = 2, # number
        _Slv_Nor2_Channel_Length = 30, # number
        _Slv_Nor2_GateSpacing = None, # number/None
        _Slv_Nor2_SDWidth = None, # number/None
        _Slv_Nor2_PCCrit = True, # None/True

        ## NMOS
        _Slv_Nor2_NMOS_XVT = 'HVT', #'XVT' ex)SLVT LVT RVT HVT
            ## NMOSA
        _Slv_Nor2_NMOSA_NumberofGate=2,
        _Slv_Nor2_NMOSA_Channel_Width = 200, # number
        _Slv_Nor2_NMOSA_Dummy_Length = None, # None/number
        _Slv_Nor2_NMOSA_Dummy_Placement = None, # None/'Up'/'Dn'
            ## NMOSB
        _Slv_Nor2_NMOSB_NumberofGate=2,
        _Slv_Nor2_NMOSB_Channel_Width = 200, # number
        _Slv_Nor2_NMOSB_Dummy_Length = None, # None/number
        _Slv_Nor2_NMOSB_Dummy_Placement = None, # None/'Up'/'Dn'

        ## PMOS
        _Slv_Nor2_PMOS_XVT = 'HVT', #'XVT' ex)SLVT LVT RVT HVT
            ## PMOSA
        _Slv_Nor2_PMOSA_NumberofGate=2,
        _Slv_Nor2_PMOSA_Channel_Width = 800, # number
        _Slv_Nor2_PMOSA_Dummy_Length = None, # None/number
        _Slv_Nor2_PMOSA_Dummy_Placement = None, # None/'Up'/'Dn'
            ## PMOSB
        _Slv_Nor2_PMOSB_NumberofGate=2,
        _Slv_Nor2_PMOSB_Channel_Width = 800, # number
        _Slv_Nor2_PMOSB_Dummy_Length = None, # None/number
        _Slv_Nor2_PMOSB_Dummy_Placement = None, # None/'Up'/'Dn'

    ## Slave Inv1: Reset Pre-driver
        ## PMOS NMOS Common
        _Slv_Inv1_NumberofGate = 2, # number
        _Slv_Inv1_Channel_Length = 30, # number
        _Slv_Inv1_GateSpacing = None, # number/None
        _Slv_Inv1_SDWidth = None, # number/None
        _Slv_Inv1_PCCrit = True, # None/True

        ## NMOS
        _Slv_Inv1_NMOS_XVT = 'SLVT', #'XVT' ex)SLVT LVT RVT HVT
        _Slv_Inv1_NMOS_Channel_Width = 200, # number
        _Slv_Inv1_NMOS_Dummy_Length = None, # None/number
        _Slv_Inv1_NMOS_Dummy_Placement = None, # None/'Up'/'Dn'

        ## PMOS
        _Slv_Inv1_PMOS_XVT = 'SLVT', #'XVT' ex)SLVT LVT RVT HVT
        _Slv_Inv1_PMOS_Channel_Width = 400, # number
        _Slv_Inv1_PMOS_Dummy_Length = None, # None/number
        _Slv_Inv1_PMOS_Dummy_Placement = None, # None/'Up'/'Dn'

    ## Slave Inv2: Reset driver
        ## PMOS NMOS Common
        _Slv_Inv2_NumberofGate = 1, # number
        _Slv_Inv2_Channel_Length = 30, # number
        _Slv_Inv2_GateSpacing = None, # number/None
        _Slv_Inv2_SDWidth = None, # number/None
        _Slv_Inv2_PCCrit = True, # None/True

        ## NMOS
        _Slv_Inv2_NMOS_XVT = 'SLVT', #'XVT' ex)SLVT LVT RVT HVT
        _Slv_Inv2_NMOS_Channel_Width = 200, # number
        _Slv_Inv2_NMOS_Dummy_Length = None, # None/number
        _Slv_Inv2_NMOS_Dummy_Placement = None, # None/'Up'/'Dn'

        ## PMOS
        _Slv_Inv2_PMOS_XVT = 'SLVT', #'XVT' ex)SLVT LVT RVT HVT
        _Slv_Inv2_PMOS_Channel_Width = 400, # number
        _Slv_Inv2_PMOS_Dummy_Length = None, # None/number
        _Slv_Inv2_PMOS_Dummy_Placement = None, # None/'Up'/'Dn'

    ## Inv3: QB
        ## PMOS NMOS Common
        _Qb_Inv3_NumberofGate = 1, # number
        _Qb_Inv3_Channel_Length = 30, # number
        _Qb_Inv3_GateSpacing = None, # number/None
        _Qb_Inv3_SDWidth = None, # number/None
        _Qb_Inv3_PCCrit = True, # None/True

        ## NMOS
        _Qb_Inv3_NMOS_XVT = 'SLVT', #'XVT' ex)SLVT LVT RVT HVT
        _Qb_Inv3_NMOS_Channel_Width = 200, # number
        _Qb_Inv3_NMOS_Dummy_Length = None, # None/number
        _Qb_Inv3_NMOS_Dummy_Placement = None, # None/'Up'/'Dn'

        ## PMOS
        _Qb_Inv3_PMOS_XVT = 'SLVT', #'XVT' ex)SLVT LVT RVT HVT
        _Qb_Inv3_PMOS_Channel_Width = 400, # number
        _Qb_Inv3_PMOS_Dummy_Length = None, # None/number
        _Qb_Inv3_PMOS_Dummy_Placement = None, # None/'Up'/'Dn'
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
    LayoutObj = _SetRstDFF_Nor(_DesignParameter=None, _Name=cellname)
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
    Checker.lib_deletion()
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
