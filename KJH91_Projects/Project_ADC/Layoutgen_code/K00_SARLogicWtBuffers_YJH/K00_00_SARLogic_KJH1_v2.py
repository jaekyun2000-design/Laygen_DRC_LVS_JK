## Import Basic Modules
## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

## Library
import copy
import numpy as np
import time

## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.D04_SARLogic_SetResetDFF_KJH1 import D04_01_SetRstDFF_Nor_Routing_KJH1


## Define Class
class _SARLogic(StickDiagram_KJH1._StickDiagram_KJH):
    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
        _NumofBit=3,

        _Test_distance=500,
        _Routing_width=50,
        _Routing_distance=100,

        _SpaceBtwPbodyAndCLKSrc=100,
        _YWidthOfCLKSrc=100,
        _SpaceBtwCLKSrcAndCLKSamp=100,
        _YWidthOfCLKSamp=100,
        _SpaceBtwNbody2AndCompOut=100,
        _YWidthOfCompOut=100,
        _SpaceBtwCompOutAndCLKDout=100,
        _YWidthOfCLKDout=100,

        ## DFF Common
        _DFF_Pbody_NumCont=2,  # number
        _DFF_Nbody_NumCont=2,  # number
        _DFF_PMOSXvt2NMOSXvt=500,  # number
        _DFF_XvtTop2Pbody=None,  # number/None(Minimum)
        _DFF_Xvtdown2Nbody=None,  # number/None(Minimum)

        ## Master Xgate1
        ## Xgate common

        ## Xgate NMOS
        _Mst_Xgate1_NMOS_NumberofGate=1,
        _Mst_Xgate1_NMOS_ChannelWidth=300,
        _Mst_Xgate1_NMOS_ChannelLength=30,
        _Mst_Xgate1_NMOS_XVT='SLVT',
        _Mst_Xgate1_NMOS_POGate_Comb_length=100,

        ## Xgate NMOS
        _Mst_Xgate1_PMOS_NumberofGate=3,
        _Mst_Xgate1_PMOS_ChannelWidth=500,
        _Mst_Xgate1_PMOS_ChannelLength=30,
        _Mst_Xgate1_PMOS_XVT='SLVT',
        _Mst_Xgate1_PMOS_POGate_Comb_length=100,

        ## Master Xgate2
        ## Xgate common

        ## Xgate NMOS
        _Mst_Xgate2_NMOS_NumberofGate=2,
        _Mst_Xgate2_NMOS_ChannelWidth=800,
        _Mst_Xgate2_NMOS_ChannelLength=30,
        _Mst_Xgate2_NMOS_XVT='SLVT',
        _Mst_Xgate2_NMOS_POGate_Comb_length=100,

        ## Xgate NMOS
        _Mst_Xgate2_PMOS_NumberofGate=3,
        _Mst_Xgate2_PMOS_ChannelWidth=200,
        _Mst_Xgate2_PMOS_ChannelLength=30,
        _Mst_Xgate2_PMOS_XVT='SLVT',
        _Mst_Xgate2_PMOS_POGate_Comb_length=100,

        ## Master Nor1
        ## Nor1 common

        ## NMOS
        ## NMOS common
        _Mst_Nor1_NMOS_XVT='SLVT',

        ## NMOSA
        _Mst_Nor1_NMOSA_NumberofGate=2,
        _Mst_Nor1_NMOSA_ChannelWidth=800,
        _Mst_Nor1_NMOSA_ChannelLength=30,
        _Mst_Nor1_NMOSA_POGate_Comb_length=100,

        ## NMOSB
        _Mst_Nor1_NMOSB_NumberofGate=3,
        _Mst_Nor1_NMOSB_ChannelWidth=200,
        _Mst_Nor1_NMOSB_ChannelLength=30,
        _Mst_Nor1_NMOSB_POGate_Comb_length=100,

        ## PMOS
        ## PMOS common
        _Mst_Nor1_PMOS_XVT='SLVT',

        ## PMOSA
        _Mst_Nor1_PMOSA_NumberofGate=2,
        _Mst_Nor1_PMOSA_ChannelWidth=800,
        _Mst_Nor1_PMOSA_ChannelLength=30,
        _Mst_Nor1_PMOSA_POGate_Comb_length=100,

        ## PMOSB
        _Mst_Nor1_PMOSB_NumberofGate=3,
        _Mst_Nor1_PMOSB_ChannelWidth=200,
        _Mst_Nor1_PMOSB_ChannelLength=30,
        _Mst_Nor1_PMOSB_POGate_Comb_length=100,

        ## Master Nor2
        ## Nor2 common

        ## NMOS
        ## NMOS common
        _Mst_Nor2_NMOS_XVT='SLVT',

        ## NMOSA
        _Mst_Nor2_NMOSA_NumberofGate=2,
        _Mst_Nor2_NMOSA_ChannelWidth=800,
        _Mst_Nor2_NMOSA_ChannelLength=30,
        _Mst_Nor2_NMOSA_POGate_Comb_length=100,

        ## NMOSB
        _Mst_Nor2_NMOSB_NumberofGate=3,
        _Mst_Nor2_NMOSB_ChannelWidth=200,
        _Mst_Nor2_NMOSB_ChannelLength=30,
        _Mst_Nor2_NMOSB_POGate_Comb_length=100,

        ## PMOS
        ## PMOS common
        _Mst_Nor2_PMOS_XVT='SLVT',

        ## PMOSA
        _Mst_Nor2_PMOSA_NumberofGate=2,
        _Mst_Nor2_PMOSA_ChannelWidth=800,
        _Mst_Nor2_PMOSA_ChannelLength=30,
        _Mst_Nor2_PMOSA_POGate_Comb_length=100,

        ## PMOSB
        _Mst_Nor2_PMOSB_NumberofGate=3,
        _Mst_Nor2_PMOSB_ChannelWidth=200,
        _Mst_Nor2_PMOSB_ChannelLength=30,
        _Mst_Nor2_PMOSB_POGate_Comb_length=100,

        ## Master Inv1
        ## Inv1 common

        ## Inv1 NMOS
        _Mst_Inv1_NMOS_NumberofGate=1,
        _Mst_Inv1_NMOS_ChannelWidth=300,
        _Mst_Inv1_NMOS_ChannelLength=30,
        _Mst_Inv1_NMOS_XVT='SLVT',
        _Mst_Inv1_NMOS_POGate_Comb_length=100,

        ## Inv1 PMOS
        _Mst_Inv1_PMOS_NumberofGate=3,
        _Mst_Inv1_PMOS_ChannelWidth=500,
        _Mst_Inv1_PMOS_ChannelLength=30,
        _Mst_Inv1_PMOS_XVT='SLVT',
        _Mst_Inv1_PMOS_POGate_Comb_length=100,

        ## Master Inv2 : Set driver
        ## Inv2 common

        ## Inv2 NMOS
        _Mst_Inv2_NMOS_NumberofGate=1,
        _Mst_Inv2_NMOS_ChannelWidth=300,
        _Mst_Inv2_NMOS_ChannelLength=30,
        _Mst_Inv2_NMOS_XVT='SLVT',
        _Mst_Inv2_NMOS_POGate_Comb_length=100,

        ## Inv2 PMOS
        _Mst_Inv2_PMOS_NumberofGate=3,
        _Mst_Inv2_PMOS_ChannelWidth=500,
        _Mst_Inv2_PMOS_ChannelLength=30,
        _Mst_Inv2_PMOS_XVT='SLVT',
        _Mst_Inv2_PMOS_POGate_Comb_length=100,

        ## Master Inv3 : Clock driver
        ## Inv3 common

        ## Inv3 NMOS
        _Mst_Inv3_NMOS_NumberofGate=1,
        _Mst_Inv3_NMOS_ChannelWidth=300,
        _Mst_Inv3_NMOS_ChannelLength=30,
        _Mst_Inv3_NMOS_XVT='SLVT',
        _Mst_Inv3_NMOS_POGate_Comb_length=100,

        ## Inv3 PMOS
        _Mst_Inv3_PMOS_NumberofGate=3,
        _Mst_Inv3_PMOS_ChannelWidth=500,
        _Mst_Inv3_PMOS_ChannelLength=30,
        _Mst_Inv3_PMOS_XVT='SLVT',
        _Mst_Inv3_PMOS_POGate_Comb_length=100,

        ## Slave Xgate1
        ## Xgate common

        ## Xgate NMOS
        _Slv_Xgate1_NMOS_NumberofGate=1,
        _Slv_Xgate1_NMOS_ChannelWidth=300,
        _Slv_Xgate1_NMOS_ChannelLength=30,
        _Slv_Xgate1_NMOS_XVT='SLVT',
        _Slv_Xgate1_NMOS_POGate_Comb_length=100,

        ## Xgate NMOS
        _Slv_Xgate1_PMOS_NumberofGate=3,
        _Slv_Xgate1_PMOS_ChannelWidth=500,
        _Slv_Xgate1_PMOS_ChannelLength=30,
        _Slv_Xgate1_PMOS_XVT='SLVT',
        _Slv_Xgate1_PMOS_POGate_Comb_length=100,

        ## Slave Xgate2
        ## Xgate common

        ## Xgate NMOS
        _Slv_Xgate2_NMOS_NumberofGate=2,
        _Slv_Xgate2_NMOS_ChannelWidth=800,
        _Slv_Xgate2_NMOS_ChannelLength=30,
        _Slv_Xgate2_NMOS_XVT='SLVT',
        _Slv_Xgate2_NMOS_POGate_Comb_length=100,

        ## Xgate NMOS
        _Slv_Xgate2_PMOS_NumberofGate=3,
        _Slv_Xgate2_PMOS_ChannelWidth=200,
        _Slv_Xgate2_PMOS_ChannelLength=30,
        _Slv_Xgate2_PMOS_XVT='SLVT',
        _Slv_Xgate2_PMOS_POGate_Comb_length=100,

        ## Slave Nor1
        ## Nor1 common

        ## NMOS
        ## NMOS common
        _Slv_Nor1_NMOS_XVT='SLVT',

        ## NMOSA
        _Slv_Nor1_NMOSA_NumberofGate=2,
        _Slv_Nor1_NMOSA_ChannelWidth=800,
        _Slv_Nor1_NMOSA_ChannelLength=30,
        _Slv_Nor1_NMOSA_POGate_Comb_length=100,

        ## NMOSB
        _Slv_Nor1_NMOSB_NumberofGate=3,
        _Slv_Nor1_NMOSB_ChannelWidth=200,
        _Slv_Nor1_NMOSB_ChannelLength=30,
        _Slv_Nor1_NMOSB_POGate_Comb_length=100,

        ## PMOS
        ## PMOS common
        _Slv_Nor1_PMOS_XVT='SLVT',

        ## PMOSA
        _Slv_Nor1_PMOSA_NumberofGate=2,
        _Slv_Nor1_PMOSA_ChannelWidth=800,
        _Slv_Nor1_PMOSA_ChannelLength=30,
        _Slv_Nor1_PMOSA_POGate_Comb_length=100,

        ## PMOSB
        _Slv_Nor1_PMOSB_NumberofGate=3,
        _Slv_Nor1_PMOSB_ChannelWidth=200,
        _Slv_Nor1_PMOSB_ChannelLength=30,
        _Slv_Nor1_PMOSB_POGate_Comb_length=100,

        ## Slave Nor2
        ## Nor2 common

        ## NMOS
        ## NMOS common
        _Slv_Nor2_NMOS_XVT='SLVT',

        ## NMOSA
        _Slv_Nor2_NMOSA_NumberofGate=2,
        _Slv_Nor2_NMOSA_ChannelWidth=800,
        _Slv_Nor2_NMOSA_ChannelLength=30,
        _Slv_Nor2_NMOSA_POGate_Comb_length=100,

        ## NMOSB
        _Slv_Nor2_NMOSB_NumberofGate=3,
        _Slv_Nor2_NMOSB_ChannelWidth=200,
        _Slv_Nor2_NMOSB_ChannelLength=30,
        _Slv_Nor2_NMOSB_POGate_Comb_length=100,

        ## PMOS
        ## PMOS common
        _Slv_Nor2_PMOS_XVT='SLVT',

        ## PMOSA
        _Slv_Nor2_PMOSA_NumberofGate=2,
        _Slv_Nor2_PMOSA_ChannelWidth=800,
        _Slv_Nor2_PMOSA_ChannelLength=30,
        _Slv_Nor2_PMOSA_POGate_Comb_length=100,

        ## PMOSB
        _Slv_Nor2_PMOSB_NumberofGate=3,
        _Slv_Nor2_PMOSB_ChannelWidth=200,
        _Slv_Nor2_PMOSB_ChannelLength=30,
        _Slv_Nor2_PMOSB_POGate_Comb_length=100,

        ## Slave Inv1 : ReSet pre-driver
        ## Inv1 common

        ## Inv1 NMOS
        _Slv_Inv1_NMOS_NumberofGate=1,
        _Slv_Inv1_NMOS_ChannelWidth=300,
        _Slv_Inv1_NMOS_ChannelLength=30,
        _Slv_Inv1_NMOS_XVT='SLVT',
        _Slv_Inv1_NMOS_POGate_Comb_length=100,

        ## Inv1 PMOS
        _Slv_Inv1_PMOS_NumberofGate=3,
        _Slv_Inv1_PMOS_ChannelWidth=500,
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
        _Slv_Inv2_PMOS_NumberofGate=3,
        _Slv_Inv2_PMOS_ChannelWidth=500,
        _Slv_Inv2_PMOS_ChannelLength=30,
        _Slv_Inv2_PMOS_XVT='SLVT',
        _Slv_Inv2_PMOS_POGate_Comb_length=100,

        ## Slave Inv3 : Qb driver
        ## Inv3 common

        ## Inv3 NMOS
        _Slv_Inv3_NMOS_NumberofGate=1,
        _Slv_Inv3_NMOS_ChannelWidth=300,
        _Slv_Inv3_NMOS_ChannelLength=30,
        _Slv_Inv3_NMOS_XVT='SLVT',
        _Slv_Inv3_NMOS_POGate_Comb_length=100,

        ## Inv3 PMOS
        _Slv_Inv3_PMOS_NumberofGate=3,
        _Slv_Inv3_PMOS_ChannelWidth=500,
        _Slv_Inv3_PMOS_ChannelLength=30,
        _Slv_Inv3_PMOS_XVT='SLVT',
        _Slv_Inv3_PMOS_POGate_Comb_length=100,

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

                                  _NumofBit=3,

                                  _Test_distance=500,
                                  _Routing_width=50,
                                  _Routing_distance=100,

                                  _SpaceBtwPbodyAndCLKSrc=100,
                                  _YWidthOfCLKSrc=100,
                                  _SpaceBtwCLKSrcAndCLKSamp=100,
                                  _YWidthOfCLKSamp=100,
                                  _SpaceBtwNbody2AndCompOut=100,
                                  _YWidthOfCompOut=100,
                                  _SpaceBtwCompOutAndCLKDout=100,
                                  _YWidthOfCLKDout=100,

                                  ## DFF Common
                                  _DFF_Pbody_NumCont=2,  # number
                                  _DFF_Nbody_NumCont=2,  # number
                                  _DFF_PMOSXvt2NMOSXvt=500,  # number
                                  _DFF_XvtTop2Pbody=None,  # number/None(Minimum)
                                  _DFF_Xvtdown2Nbody=None,  # number/None(Minimum)

                                  ## Master Xgate1
                                  ## Xgate common

                                  ## Xgate NMOS
                                  _Mst_Xgate1_NMOS_NumberofGate=1,
                                  _Mst_Xgate1_NMOS_ChannelWidth=300,
                                  _Mst_Xgate1_NMOS_ChannelLength=30,
                                  _Mst_Xgate1_NMOS_XVT='SLVT',
                                  _Mst_Xgate1_NMOS_POGate_Comb_length=100,

                                  ## Xgate NMOS
                                  _Mst_Xgate1_PMOS_NumberofGate=3,
                                  _Mst_Xgate1_PMOS_ChannelWidth=500,
                                  _Mst_Xgate1_PMOS_ChannelLength=30,
                                  _Mst_Xgate1_PMOS_XVT='SLVT',
                                  _Mst_Xgate1_PMOS_POGate_Comb_length=100,

                                  ## Master Xgate2
                                  ## Xgate common

                                  ## Xgate NMOS
                                  _Mst_Xgate2_NMOS_NumberofGate=2,
                                  _Mst_Xgate2_NMOS_ChannelWidth=800,
                                  _Mst_Xgate2_NMOS_ChannelLength=30,
                                  _Mst_Xgate2_NMOS_XVT='SLVT',
                                  _Mst_Xgate2_NMOS_POGate_Comb_length=100,

                                  ## Xgate NMOS
                                  _Mst_Xgate2_PMOS_NumberofGate=3,
                                  _Mst_Xgate2_PMOS_ChannelWidth=200,
                                  _Mst_Xgate2_PMOS_ChannelLength=30,
                                  _Mst_Xgate2_PMOS_XVT='SLVT',
                                  _Mst_Xgate2_PMOS_POGate_Comb_length=100,

                                  ## Master Nor1
                                  ## Nor1 common

                                  ## NMOS
                                  ## NMOS common
                                  _Mst_Nor1_NMOS_XVT='SLVT',

                                  ## NMOSA
                                  _Mst_Nor1_NMOSA_NumberofGate=2,
                                  _Mst_Nor1_NMOSA_ChannelWidth=800,
                                  _Mst_Nor1_NMOSA_ChannelLength=30,
                                  _Mst_Nor1_NMOSA_POGate_Comb_length=100,

                                  ## NMOSB
                                  _Mst_Nor1_NMOSB_NumberofGate=3,
                                  _Mst_Nor1_NMOSB_ChannelWidth=200,
                                  _Mst_Nor1_NMOSB_ChannelLength=30,
                                  _Mst_Nor1_NMOSB_POGate_Comb_length=100,

                                  ## PMOS
                                  ## PMOS common
                                  _Mst_Nor1_PMOS_XVT='SLVT',

                                  ## PMOSA
                                  _Mst_Nor1_PMOSA_NumberofGate=2,
                                  _Mst_Nor1_PMOSA_ChannelWidth=800,
                                  _Mst_Nor1_PMOSA_ChannelLength=30,
                                  _Mst_Nor1_PMOSA_POGate_Comb_length=100,

                                  ## PMOSB
                                  _Mst_Nor1_PMOSB_NumberofGate=3,
                                  _Mst_Nor1_PMOSB_ChannelWidth=200,
                                  _Mst_Nor1_PMOSB_ChannelLength=30,
                                  _Mst_Nor1_PMOSB_POGate_Comb_length=100,

                                  ## Master Nor2
                                  ## Nor2 common

                                  ## NMOS
                                  ## NMOS common
                                  _Mst_Nor2_NMOS_XVT='SLVT',

                                  ## NMOSA
                                  _Mst_Nor2_NMOSA_NumberofGate=2,
                                  _Mst_Nor2_NMOSA_ChannelWidth=800,
                                  _Mst_Nor2_NMOSA_ChannelLength=30,
                                  _Mst_Nor2_NMOSA_POGate_Comb_length=100,

                                  ## NMOSB
                                  _Mst_Nor2_NMOSB_NumberofGate=3,
                                  _Mst_Nor2_NMOSB_ChannelWidth=200,
                                  _Mst_Nor2_NMOSB_ChannelLength=30,
                                  _Mst_Nor2_NMOSB_POGate_Comb_length=100,

                                  ## PMOS
                                  ## PMOS common
                                  _Mst_Nor2_PMOS_XVT='SLVT',

                                  ## PMOSA
                                  _Mst_Nor2_PMOSA_NumberofGate=2,
                                  _Mst_Nor2_PMOSA_ChannelWidth=800,
                                  _Mst_Nor2_PMOSA_ChannelLength=30,
                                  _Mst_Nor2_PMOSA_POGate_Comb_length=100,

                                  ## PMOSB
                                  _Mst_Nor2_PMOSB_NumberofGate=3,
                                  _Mst_Nor2_PMOSB_ChannelWidth=200,
                                  _Mst_Nor2_PMOSB_ChannelLength=30,
                                  _Mst_Nor2_PMOSB_POGate_Comb_length=100,

                                  ## Master Inv1
                                  ## Inv1 common

                                  ## Inv1 NMOS
                                  _Mst_Inv1_NMOS_NumberofGate=1,
                                  _Mst_Inv1_NMOS_ChannelWidth=300,
                                  _Mst_Inv1_NMOS_ChannelLength=30,
                                  _Mst_Inv1_NMOS_XVT='SLVT',
                                  _Mst_Inv1_NMOS_POGate_Comb_length=100,

                                  ## Inv1 PMOS
                                  _Mst_Inv1_PMOS_NumberofGate=3,
                                  _Mst_Inv1_PMOS_ChannelWidth=500,
                                  _Mst_Inv1_PMOS_ChannelLength=30,
                                  _Mst_Inv1_PMOS_XVT='SLVT',
                                  _Mst_Inv1_PMOS_POGate_Comb_length=100,

                                  ## Master Inv2 : Set driver
                                  ## Inv2 common

                                  ## Inv2 NMOS
                                  _Mst_Inv2_NMOS_NumberofGate=1,
                                  _Mst_Inv2_NMOS_ChannelWidth=300,
                                  _Mst_Inv2_NMOS_ChannelLength=30,
                                  _Mst_Inv2_NMOS_XVT='SLVT',
                                  _Mst_Inv2_NMOS_POGate_Comb_length=100,

                                  ## Inv2 PMOS
                                  _Mst_Inv2_PMOS_NumberofGate=3,
                                  _Mst_Inv2_PMOS_ChannelWidth=500,
                                  _Mst_Inv2_PMOS_ChannelLength=30,
                                  _Mst_Inv2_PMOS_XVT='SLVT',
                                  _Mst_Inv2_PMOS_POGate_Comb_length=100,

                                  ## Master Inv3 : Clock driver
                                  ## Inv3 common

                                  ## Inv3 NMOS
                                  _Mst_Inv3_NMOS_NumberofGate=1,
                                  _Mst_Inv3_NMOS_ChannelWidth=300,
                                  _Mst_Inv3_NMOS_ChannelLength=30,
                                  _Mst_Inv3_NMOS_XVT='SLVT',
                                  _Mst_Inv3_NMOS_POGate_Comb_length=100,

                                  ## Inv3 PMOS
                                  _Mst_Inv3_PMOS_NumberofGate=3,
                                  _Mst_Inv3_PMOS_ChannelWidth=500,
                                  _Mst_Inv3_PMOS_ChannelLength=30,
                                  _Mst_Inv3_PMOS_XVT='SLVT',
                                  _Mst_Inv3_PMOS_POGate_Comb_length=100,

                                  ## Slave Xgate1
                                  ## Xgate common

                                  ## Xgate NMOS
                                  _Slv_Xgate1_NMOS_NumberofGate=1,
                                  _Slv_Xgate1_NMOS_ChannelWidth=300,
                                  _Slv_Xgate1_NMOS_ChannelLength=30,
                                  _Slv_Xgate1_NMOS_XVT='SLVT',
                                  _Slv_Xgate1_NMOS_POGate_Comb_length=100,

                                  ## Xgate NMOS
                                  _Slv_Xgate1_PMOS_NumberofGate=3,
                                  _Slv_Xgate1_PMOS_ChannelWidth=500,
                                  _Slv_Xgate1_PMOS_ChannelLength=30,
                                  _Slv_Xgate1_PMOS_XVT='SLVT',
                                  _Slv_Xgate1_PMOS_POGate_Comb_length=100,

                                  ## Slave Xgate2
                                  ## Xgate common

                                  ## Xgate NMOS
                                  _Slv_Xgate2_NMOS_NumberofGate=2,
                                  _Slv_Xgate2_NMOS_ChannelWidth=800,
                                  _Slv_Xgate2_NMOS_ChannelLength=30,
                                  _Slv_Xgate2_NMOS_XVT='SLVT',
                                  _Slv_Xgate2_NMOS_POGate_Comb_length=100,

                                  ## Xgate NMOS
                                  _Slv_Xgate2_PMOS_NumberofGate=3,
                                  _Slv_Xgate2_PMOS_ChannelWidth=200,
                                  _Slv_Xgate2_PMOS_ChannelLength=30,
                                  _Slv_Xgate2_PMOS_XVT='SLVT',
                                  _Slv_Xgate2_PMOS_POGate_Comb_length=100,

                                  ## Slave Nor1
                                  ## Nor1 common

                                  ## NMOS
                                  ## NMOS common
                                  _Slv_Nor1_NMOS_XVT='SLVT',

                                  ## NMOSA
                                  _Slv_Nor1_NMOSA_NumberofGate=2,
                                  _Slv_Nor1_NMOSA_ChannelWidth=800,
                                  _Slv_Nor1_NMOSA_ChannelLength=30,
                                  _Slv_Nor1_NMOSA_POGate_Comb_length=100,

                                  ## NMOSB
                                  _Slv_Nor1_NMOSB_NumberofGate=3,
                                  _Slv_Nor1_NMOSB_ChannelWidth=200,
                                  _Slv_Nor1_NMOSB_ChannelLength=30,
                                  _Slv_Nor1_NMOSB_POGate_Comb_length=100,

                                  ## PMOS
                                  ## PMOS common
                                  _Slv_Nor1_PMOS_XVT='SLVT',

                                  ## PMOSA
                                  _Slv_Nor1_PMOSA_NumberofGate=2,
                                  _Slv_Nor1_PMOSA_ChannelWidth=800,
                                  _Slv_Nor1_PMOSA_ChannelLength=30,
                                  _Slv_Nor1_PMOSA_POGate_Comb_length=100,

                                  ## PMOSB
                                  _Slv_Nor1_PMOSB_NumberofGate=3,
                                  _Slv_Nor1_PMOSB_ChannelWidth=200,
                                  _Slv_Nor1_PMOSB_ChannelLength=30,
                                  _Slv_Nor1_PMOSB_POGate_Comb_length=100,

                                  ## Slave Nor2
                                  ## Nor2 common

                                  ## NMOS
                                  ## NMOS common
                                  _Slv_Nor2_NMOS_XVT='SLVT',

                                  ## NMOSA
                                  _Slv_Nor2_NMOSA_NumberofGate=2,
                                  _Slv_Nor2_NMOSA_ChannelWidth=800,
                                  _Slv_Nor2_NMOSA_ChannelLength=30,
                                  _Slv_Nor2_NMOSA_POGate_Comb_length=100,

                                  ## NMOSB
                                  _Slv_Nor2_NMOSB_NumberofGate=3,
                                  _Slv_Nor2_NMOSB_ChannelWidth=200,
                                  _Slv_Nor2_NMOSB_ChannelLength=30,
                                  _Slv_Nor2_NMOSB_POGate_Comb_length=100,

                                  ## PMOS
                                  ## PMOS common
                                  _Slv_Nor2_PMOS_XVT='SLVT',

                                  ## PMOSA
                                  _Slv_Nor2_PMOSA_NumberofGate=2,
                                  _Slv_Nor2_PMOSA_ChannelWidth=800,
                                  _Slv_Nor2_PMOSA_ChannelLength=30,
                                  _Slv_Nor2_PMOSA_POGate_Comb_length=100,

                                  ## PMOSB
                                  _Slv_Nor2_PMOSB_NumberofGate=3,
                                  _Slv_Nor2_PMOSB_ChannelWidth=200,
                                  _Slv_Nor2_PMOSB_ChannelLength=30,
                                  _Slv_Nor2_PMOSB_POGate_Comb_length=100,

                                  ## Slave Inv1 : ReSet pre-driver
                                  ## Inv1 common

                                  ## Inv1 NMOS
                                  _Slv_Inv1_NMOS_NumberofGate=1,
                                  _Slv_Inv1_NMOS_ChannelWidth=300,
                                  _Slv_Inv1_NMOS_ChannelLength=30,
                                  _Slv_Inv1_NMOS_XVT='SLVT',
                                  _Slv_Inv1_NMOS_POGate_Comb_length=100,

                                  ## Inv1 PMOS
                                  _Slv_Inv1_PMOS_NumberofGate=3,
                                  _Slv_Inv1_PMOS_ChannelWidth=500,
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
                                  _Slv_Inv2_PMOS_NumberofGate=3,
                                  _Slv_Inv2_PMOS_ChannelWidth=500,
                                  _Slv_Inv2_PMOS_ChannelLength=30,
                                  _Slv_Inv2_PMOS_XVT='SLVT',
                                  _Slv_Inv2_PMOS_POGate_Comb_length=100,

                                  ## Slave Inv3 : Qb driver
                                  ## Inv3 common

                                  ## Inv3 NMOS
                                  _Slv_Inv3_NMOS_NumberofGate=1,
                                  _Slv_Inv3_NMOS_ChannelWidth=300,
                                  _Slv_Inv3_NMOS_ChannelLength=30,
                                  _Slv_Inv3_NMOS_XVT='SLVT',
                                  _Slv_Inv3_NMOS_POGate_Comb_length=100,

                                  ## Inv3 PMOS
                                  _Slv_Inv3_PMOS_NumberofGate=3,
                                  _Slv_Inv3_PMOS_ChannelWidth=500,
                                  _Slv_Inv3_PMOS_ChannelLength=30,
                                  _Slv_Inv3_PMOS_XVT='SLVT',
                                  _Slv_Inv3_PMOS_POGate_Comb_length=100,

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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Thermometer Counter Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters1 = copy.deepcopy(
            D04_01_SetRstDFF_Nor_Routing_KJH1._SetRstDFF_Nor_Routing._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters1['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters1['_Test_distance'] = _Test_distance
        ## DFF Common
        _Caculation_Parameters1['_DFF_Pbody_NumCont'] = _DFF_Pbody_NumCont
        _Caculation_Parameters1['_DFF_Nbody_NumCont'] = _DFF_Nbody_NumCont
        _Caculation_Parameters1['_DFF_PMOSXvt2NMOSXvt'] = _DFF_PMOSXvt2NMOSXvt
        _Caculation_Parameters1['_DFF_XvtTop2Pbody'] = _DFF_XvtTop2Pbody
        _Caculation_Parameters1['_DFF_Xvtdown2Nbody'] = _DFF_Xvtdown2Nbody
        ## Master Xgate1
        _Caculation_Parameters1['_Mst_Xgate1_NMOS_NumberofGate'] = _Mst_Xgate1_NMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Xgate1_NMOS_ChannelWidth'] = _Mst_Xgate1_NMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Xgate1_NMOS_ChannelLength'] = _Mst_Xgate1_NMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Xgate1_NMOS_XVT'] = _Mst_Xgate1_NMOS_XVT
        _Caculation_Parameters1['_Mst_Xgate1_NMOS_POGate_Comb_length'] = _Mst_Xgate1_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_Mst_Xgate1_PMOS_NumberofGate'] = _Mst_Xgate1_PMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Xgate1_PMOS_ChannelWidth'] = _Mst_Xgate1_PMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Xgate1_PMOS_ChannelLength'] = _Mst_Xgate1_PMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Xgate1_PMOS_XVT'] = _Mst_Xgate1_PMOS_XVT
        _Caculation_Parameters1['_Mst_Xgate1_PMOS_POGate_Comb_length'] = _Mst_Xgate1_PMOS_POGate_Comb_length
        ## Master Xgate2
        _Caculation_Parameters1['_Mst_Xgate2_NMOS_NumberofGate'] = _Mst_Xgate2_NMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Xgate2_NMOS_ChannelWidth'] = _Mst_Xgate2_NMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Xgate2_NMOS_ChannelLength'] = _Mst_Xgate2_NMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Xgate2_NMOS_XVT'] = _Mst_Xgate2_NMOS_XVT
        _Caculation_Parameters1['_Mst_Xgate2_NMOS_POGate_Comb_length'] = _Mst_Xgate2_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_Mst_Xgate2_PMOS_NumberofGate'] = _Mst_Xgate2_PMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Xgate2_PMOS_ChannelWidth'] = _Mst_Xgate2_PMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Xgate2_PMOS_ChannelLength'] = _Mst_Xgate2_PMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Xgate2_PMOS_XVT'] = _Mst_Xgate2_PMOS_XVT
        _Caculation_Parameters1['_Mst_Xgate2_PMOS_POGate_Comb_length'] = _Mst_Xgate2_PMOS_POGate_Comb_length
        ## Master Nor1
        _Caculation_Parameters1['_Mst_Nor1_NMOS_XVT'] = _Mst_Nor1_NMOS_XVT

        _Caculation_Parameters1['_Mst_Nor1_NMOSA_NumberofGate'] = _Mst_Nor1_NMOSA_NumberofGate
        _Caculation_Parameters1['_Mst_Nor1_NMOSA_ChannelWidth'] = _Mst_Nor1_NMOSA_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor1_NMOSA_ChannelLength'] = _Mst_Nor1_NMOSA_ChannelLength
        _Caculation_Parameters1['_Mst_Nor1_NMOSA_POGate_Comb_length'] = _Mst_Nor1_NMOSA_POGate_Comb_length

        _Caculation_Parameters1['_Mst_Nor1_NMOSB_NumberofGate'] = _Mst_Nor1_NMOSB_NumberofGate
        _Caculation_Parameters1['_Mst_Nor1_NMOSB_ChannelWidth'] = _Mst_Nor1_NMOSB_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor1_NMOSB_ChannelLength'] = _Mst_Nor1_NMOSB_ChannelLength
        _Caculation_Parameters1['_Mst_Nor1_NMOSB_POGate_Comb_length'] = _Mst_Nor1_NMOSB_POGate_Comb_length

        _Caculation_Parameters1['_Mst_Nor1_PMOS_XVT'] = _Mst_Nor1_PMOS_XVT

        _Caculation_Parameters1['_Mst_Nor1_PMOSA_NumberofGate'] = _Mst_Nor1_PMOSA_NumberofGate
        _Caculation_Parameters1['_Mst_Nor1_PMOSA_ChannelWidth'] = _Mst_Nor1_PMOSA_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor1_PMOSA_ChannelLength'] = _Mst_Nor1_PMOSA_ChannelLength
        _Caculation_Parameters1['_Mst_Nor1_PMOSA_POGate_Comb_length'] = _Mst_Nor1_PMOSA_POGate_Comb_length

        _Caculation_Parameters1['_Mst_Nor1_PMOSB_NumberofGate'] = _Mst_Nor1_PMOSB_NumberofGate
        _Caculation_Parameters1['_Mst_Nor1_PMOSB_ChannelWidth'] = _Mst_Nor1_PMOSB_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor1_PMOSB_ChannelLength'] = _Mst_Nor1_PMOSB_ChannelLength
        _Caculation_Parameters1['_Mst_Nor1_PMOSB_POGate_Comb_length'] = _Mst_Nor1_PMOSB_POGate_Comb_length
        ## Master Nor2
        _Caculation_Parameters1['_Mst_Nor2_NMOS_XVT'] = _Mst_Nor2_NMOS_XVT

        _Caculation_Parameters1['_Mst_Nor2_NMOSA_NumberofGate'] = _Mst_Nor2_NMOSA_NumberofGate
        _Caculation_Parameters1['_Mst_Nor2_NMOSA_ChannelWidth'] = _Mst_Nor2_NMOSA_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor2_NMOSA_ChannelLength'] = _Mst_Nor2_NMOSA_ChannelLength
        _Caculation_Parameters1['_Mst_Nor2_NMOSA_POGate_Comb_length'] = _Mst_Nor2_NMOSA_POGate_Comb_length

        _Caculation_Parameters1['_Mst_Nor2_NMOSB_NumberofGate'] = _Mst_Nor2_NMOSB_NumberofGate
        _Caculation_Parameters1['_Mst_Nor2_NMOSB_ChannelWidth'] = _Mst_Nor2_NMOSB_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor2_NMOSB_ChannelLength'] = _Mst_Nor2_NMOSB_ChannelLength
        _Caculation_Parameters1['_Mst_Nor2_NMOSB_POGate_Comb_length'] = _Mst_Nor2_NMOSB_POGate_Comb_length

        _Caculation_Parameters1['_Mst_Nor2_PMOS_XVT'] = _Mst_Nor2_PMOS_XVT

        _Caculation_Parameters1['_Mst_Nor2_PMOSA_NumberofGate'] = _Mst_Nor2_PMOSA_NumberofGate
        _Caculation_Parameters1['_Mst_Nor2_PMOSA_ChannelWidth'] = _Mst_Nor2_PMOSA_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor2_PMOSA_ChannelLength'] = _Mst_Nor2_PMOSA_ChannelLength
        _Caculation_Parameters1['_Mst_Nor2_PMOSA_POGate_Comb_length'] = _Mst_Nor2_PMOSA_POGate_Comb_length

        _Caculation_Parameters1['_Mst_Nor2_PMOSB_NumberofGate'] = _Mst_Nor2_PMOSB_NumberofGate
        _Caculation_Parameters1['_Mst_Nor2_PMOSB_ChannelWidth'] = _Mst_Nor2_PMOSB_ChannelWidth
        _Caculation_Parameters1['_Mst_Nor2_PMOSB_ChannelLength'] = _Mst_Nor2_PMOSB_ChannelLength
        _Caculation_Parameters1['_Mst_Nor2_PMOSB_POGate_Comb_length'] = _Mst_Nor2_PMOSB_POGate_Comb_length
        ## Master Inv1
        _Caculation_Parameters1['_Mst_Inv1_NMOS_NumberofGate'] = _Mst_Inv1_NMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Inv1_NMOS_ChannelWidth'] = _Mst_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Inv1_NMOS_ChannelLength'] = _Mst_Inv1_NMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Inv1_NMOS_XVT'] = _Mst_Inv1_NMOS_XVT
        _Caculation_Parameters1['_Mst_Inv1_NMOS_POGate_Comb_length'] = _Mst_Inv1_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_Mst_Inv1_PMOS_NumberofGate'] = _Mst_Inv1_PMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Inv1_PMOS_ChannelWidth'] = _Mst_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Inv1_PMOS_ChannelLength'] = _Mst_Inv1_PMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Inv1_PMOS_XVT'] = _Mst_Inv1_PMOS_XVT
        _Caculation_Parameters1['_Mst_Inv1_PMOS_POGate_Comb_length'] = _Mst_Inv1_PMOS_POGate_Comb_length
        ## Master Inv2
        _Caculation_Parameters1['_Mst_Inv2_NMOS_NumberofGate'] = _Mst_Inv2_NMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Inv2_NMOS_ChannelWidth'] = _Mst_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Inv2_NMOS_ChannelLength'] = _Mst_Inv2_NMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Inv2_NMOS_XVT'] = _Mst_Inv2_NMOS_XVT
        _Caculation_Parameters1['_Mst_Inv2_NMOS_POGate_Comb_length'] = _Mst_Inv2_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_Mst_Inv2_PMOS_NumberofGate'] = _Mst_Inv2_PMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Inv2_PMOS_ChannelWidth'] = _Mst_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Inv2_PMOS_ChannelLength'] = _Mst_Inv2_PMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Inv2_PMOS_XVT'] = _Mst_Inv2_PMOS_XVT
        _Caculation_Parameters1['_Mst_Inv2_PMOS_POGate_Comb_length'] = _Mst_Inv2_PMOS_POGate_Comb_length
        ## Master Inv3
        _Caculation_Parameters1['_Mst_Inv3_NMOS_NumberofGate'] = _Mst_Inv3_NMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Inv3_NMOS_ChannelWidth'] = _Mst_Inv3_NMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Inv3_NMOS_ChannelLength'] = _Mst_Inv3_NMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Inv3_NMOS_XVT'] = _Mst_Inv3_NMOS_XVT
        _Caculation_Parameters1['_Mst_Inv3_NMOS_POGate_Comb_length'] = _Mst_Inv3_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_Mst_Inv3_PMOS_NumberofGate'] = _Mst_Inv3_PMOS_NumberofGate
        _Caculation_Parameters1['_Mst_Inv3_PMOS_ChannelWidth'] = _Mst_Inv3_PMOS_ChannelWidth
        _Caculation_Parameters1['_Mst_Inv3_PMOS_ChannelLength'] = _Mst_Inv3_PMOS_ChannelLength
        _Caculation_Parameters1['_Mst_Inv3_PMOS_XVT'] = _Mst_Inv3_PMOS_XVT
        _Caculation_Parameters1['_Mst_Inv3_PMOS_POGate_Comb_length'] = _Mst_Inv3_PMOS_POGate_Comb_length

        ## Slave Xgate1
        _Caculation_Parameters1['_Slv_Xgate1_NMOS_NumberofGate'] = _Slv_Xgate1_NMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Xgate1_NMOS_ChannelWidth'] = _Slv_Xgate1_NMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Xgate1_NMOS_ChannelLength'] = _Slv_Xgate1_NMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Xgate1_NMOS_XVT'] = _Slv_Xgate1_NMOS_XVT
        _Caculation_Parameters1['_Slv_Xgate1_NMOS_POGate_Comb_length'] = _Slv_Xgate1_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_Slv_Xgate1_PMOS_NumberofGate'] = _Slv_Xgate1_PMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Xgate1_PMOS_ChannelWidth'] = _Slv_Xgate1_PMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Xgate1_PMOS_ChannelLength'] = _Slv_Xgate1_PMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Xgate1_PMOS_XVT'] = _Slv_Xgate1_PMOS_XVT
        _Caculation_Parameters1['_Slv_Xgate1_PMOS_POGate_Comb_length'] = _Slv_Xgate1_PMOS_POGate_Comb_length
        ## Slave Xgate2
        _Caculation_Parameters1['_Slv_Xgate2_NMOS_NumberofGate'] = _Slv_Xgate2_NMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Xgate2_NMOS_ChannelWidth'] = _Slv_Xgate2_NMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Xgate2_NMOS_ChannelLength'] = _Slv_Xgate2_NMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Xgate2_NMOS_XVT'] = _Slv_Xgate2_NMOS_XVT
        _Caculation_Parameters1['_Slv_Xgate2_NMOS_POGate_Comb_length'] = _Slv_Xgate2_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_Slv_Xgate2_PMOS_NumberofGate'] = _Slv_Xgate2_PMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Xgate2_PMOS_ChannelWidth'] = _Slv_Xgate2_PMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Xgate2_PMOS_ChannelLength'] = _Slv_Xgate2_PMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Xgate2_PMOS_XVT'] = _Slv_Xgate2_PMOS_XVT
        _Caculation_Parameters1['_Slv_Xgate2_PMOS_POGate_Comb_length'] = _Slv_Xgate2_PMOS_POGate_Comb_length
        ## Slave Nor1
        _Caculation_Parameters1['_Slv_Nor1_NMOS_XVT'] = _Slv_Nor1_NMOS_XVT

        _Caculation_Parameters1['_Slv_Nor1_NMOSA_NumberofGate'] = _Slv_Nor1_NMOSA_NumberofGate
        _Caculation_Parameters1['_Slv_Nor1_NMOSA_ChannelWidth'] = _Slv_Nor1_NMOSA_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor1_NMOSA_ChannelLength'] = _Slv_Nor1_NMOSA_ChannelLength
        _Caculation_Parameters1['_Slv_Nor1_NMOSA_POGate_Comb_length'] = _Slv_Nor1_NMOSA_POGate_Comb_length

        _Caculation_Parameters1['_Slv_Nor1_NMOSB_NumberofGate'] = _Slv_Nor1_NMOSB_NumberofGate
        _Caculation_Parameters1['_Slv_Nor1_NMOSB_ChannelWidth'] = _Slv_Nor1_NMOSB_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor1_NMOSB_ChannelLength'] = _Slv_Nor1_NMOSB_ChannelLength
        _Caculation_Parameters1['_Slv_Nor1_NMOSB_POGate_Comb_length'] = _Slv_Nor1_NMOSB_POGate_Comb_length

        _Caculation_Parameters1['_Slv_Nor1_PMOS_XVT'] = _Slv_Nor1_PMOS_XVT

        _Caculation_Parameters1['_Slv_Nor1_PMOSA_NumberofGate'] = _Slv_Nor1_PMOSA_NumberofGate
        _Caculation_Parameters1['_Slv_Nor1_PMOSA_ChannelWidth'] = _Slv_Nor1_PMOSA_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor1_PMOSA_ChannelLength'] = _Slv_Nor1_PMOSA_ChannelLength
        _Caculation_Parameters1['_Slv_Nor1_PMOSA_POGate_Comb_length'] = _Slv_Nor1_PMOSA_POGate_Comb_length

        _Caculation_Parameters1['_Slv_Nor1_PMOSB_NumberofGate'] = _Slv_Nor1_PMOSB_NumberofGate
        _Caculation_Parameters1['_Slv_Nor1_PMOSB_ChannelWidth'] = _Slv_Nor1_PMOSB_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor1_PMOSB_ChannelLength'] = _Slv_Nor1_PMOSB_ChannelLength
        _Caculation_Parameters1['_Slv_Nor1_PMOSB_POGate_Comb_length'] = _Slv_Nor1_PMOSB_POGate_Comb_length
        ## Slave Nor2
        _Caculation_Parameters1['_Slv_Nor2_NMOS_XVT'] = _Slv_Nor2_NMOS_XVT

        _Caculation_Parameters1['_Slv_Nor2_NMOSA_NumberofGate'] = _Slv_Nor2_NMOSA_NumberofGate
        _Caculation_Parameters1['_Slv_Nor2_NMOSA_ChannelWidth'] = _Slv_Nor2_NMOSA_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor2_NMOSA_ChannelLength'] = _Slv_Nor2_NMOSA_ChannelLength
        _Caculation_Parameters1['_Slv_Nor2_NMOSA_POGate_Comb_length'] = _Slv_Nor2_NMOSA_POGate_Comb_length

        _Caculation_Parameters1['_Slv_Nor2_NMOSB_NumberofGate'] = _Slv_Nor2_NMOSB_NumberofGate
        _Caculation_Parameters1['_Slv_Nor2_NMOSB_ChannelWidth'] = _Slv_Nor2_NMOSB_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor2_NMOSB_ChannelLength'] = _Slv_Nor2_NMOSB_ChannelLength
        _Caculation_Parameters1['_Slv_Nor2_NMOSB_POGate_Comb_length'] = _Slv_Nor2_NMOSB_POGate_Comb_length

        _Caculation_Parameters1['_Slv_Nor2_PMOS_XVT'] = _Slv_Nor2_PMOS_XVT

        _Caculation_Parameters1['_Slv_Nor2_PMOSA_NumberofGate'] = _Slv_Nor2_PMOSA_NumberofGate
        _Caculation_Parameters1['_Slv_Nor2_PMOSA_ChannelWidth'] = _Slv_Nor2_PMOSA_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor2_PMOSA_ChannelLength'] = _Slv_Nor2_PMOSA_ChannelLength
        _Caculation_Parameters1['_Slv_Nor2_PMOSA_POGate_Comb_length'] = _Slv_Nor2_PMOSA_POGate_Comb_length

        _Caculation_Parameters1['_Slv_Nor2_PMOSB_NumberofGate'] = _Slv_Nor2_PMOSB_NumberofGate
        _Caculation_Parameters1['_Slv_Nor2_PMOSB_ChannelWidth'] = _Slv_Nor2_PMOSB_ChannelWidth
        _Caculation_Parameters1['_Slv_Nor2_PMOSB_ChannelLength'] = _Slv_Nor2_PMOSB_ChannelLength
        _Caculation_Parameters1['_Slv_Nor2_PMOSB_POGate_Comb_length'] = _Slv_Nor2_PMOSB_POGate_Comb_length
        ## Slave Inv1
        _Caculation_Parameters1['_Slv_Inv1_NMOS_NumberofGate'] = _Slv_Inv1_NMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Inv1_NMOS_ChannelWidth'] = _Slv_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Inv1_NMOS_ChannelLength'] = _Slv_Inv1_NMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Inv1_NMOS_XVT'] = _Slv_Inv1_NMOS_XVT
        _Caculation_Parameters1['_Slv_Inv1_NMOS_POGate_Comb_length'] = _Slv_Inv1_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_Slv_Inv1_PMOS_NumberofGate'] = _Slv_Inv1_PMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Inv1_PMOS_ChannelWidth'] = _Slv_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Inv1_PMOS_ChannelLength'] = _Slv_Inv1_PMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Inv1_PMOS_XVT'] = _Slv_Inv1_PMOS_XVT
        _Caculation_Parameters1['_Slv_Inv1_PMOS_POGate_Comb_length'] = _Slv_Inv1_PMOS_POGate_Comb_length
        ## Slave Inv2
        _Caculation_Parameters1['_Slv_Inv2_NMOS_NumberofGate'] = _Slv_Inv2_NMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Inv2_NMOS_ChannelWidth'] = _Slv_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Inv2_NMOS_ChannelLength'] = _Slv_Inv2_NMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Inv2_NMOS_XVT'] = _Slv_Inv2_NMOS_XVT
        _Caculation_Parameters1['_Slv_Inv2_NMOS_POGate_Comb_length'] = _Slv_Inv2_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_Slv_Inv2_PMOS_NumberofGate'] = _Slv_Inv2_PMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Inv2_PMOS_ChannelWidth'] = _Slv_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Inv2_PMOS_ChannelLength'] = _Slv_Inv2_PMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Inv2_PMOS_XVT'] = _Slv_Inv2_PMOS_XVT
        _Caculation_Parameters1['_Slv_Inv2_PMOS_POGate_Comb_length'] = _Slv_Inv2_PMOS_POGate_Comb_length
        ## Slave Inv3
        _Caculation_Parameters1['_Slv_Inv3_NMOS_NumberofGate'] = _Slv_Inv3_NMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Inv3_NMOS_ChannelWidth'] = _Slv_Inv3_NMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Inv3_NMOS_ChannelLength'] = _Slv_Inv3_NMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Inv3_NMOS_XVT'] = _Slv_Inv3_NMOS_XVT
        _Caculation_Parameters1['_Slv_Inv3_NMOS_POGate_Comb_length'] = _Slv_Inv3_NMOS_POGate_Comb_length

        _Caculation_Parameters1['_Slv_Inv3_PMOS_NumberofGate'] = _Slv_Inv3_PMOS_NumberofGate
        _Caculation_Parameters1['_Slv_Inv3_PMOS_ChannelWidth'] = _Slv_Inv3_PMOS_ChannelWidth
        _Caculation_Parameters1['_Slv_Inv3_PMOS_ChannelLength'] = _Slv_Inv3_PMOS_ChannelLength
        _Caculation_Parameters1['_Slv_Inv3_PMOS_XVT'] = _Slv_Inv3_PMOS_XVT
        _Caculation_Parameters1['_Slv_Inv3_PMOS_POGate_Comb_length'] = _Slv_Inv3_PMOS_POGate_Comb_length

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Thermo_Cnt'] = self._SrefElementDeclaration(
            _DesignObj=D04_01_SetRstDFF_Nor_Routing_KJH1._SetRstDFF_Nor_Routing(_DesignParameter=None,
                                                                                _Name='{}:SRF_Thermo_Cnt'.format(
                                                                                    _Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Thermo_Cnt']['_Reflect'] = [1, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Thermo_Cnt']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Thermo_Cnt']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters1)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Thermo_Cnt']['_XYCoordinates'] = [[0, 0]]

        ## Get_Scoord_v4.
        ## Calculate Sref XYcoord
        tmpXY = [[0, 0]]
        for i in range(0, _NumofBit):
            ## Calculate
            ## Target_coord: _XY_type1
            ##X
            tmp1_1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'SRF_NMOS',
                                         'BND_PODummyLayer')
            tmp1_2 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'SRF_PMOS',
                                         'BND_PODummyLayer')
            if tmp1_1[i][0][0][0][-1][0]['_XY_right'][0] > tmp1_2[i][0][0][0][-1][0]['_XY_right'][0]:
                target_coordx = tmp1_1[i][0][0][0][-1][0]['_XY_right'][0]
            else:
                target_coordx = tmp1_2[i][0][0][0][-1][0]['_XY_right'][0]
                ##Y
            tmp1_3 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'SRF_PMOS',
                                         'BND_{}Layer'.format(_Slv_Inv3_PMOS_XVT))
            target_coordy = tmp1_3[i][0][0][0][0][0]['_XY_down'][1]

            target_coord = [target_coordx, target_coordy]
            ## Approaching_coord: _XY_type2
            ##X
            tmp2_1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_NMOS',
                                         'BND_PODummyLayer')
            tmp2_2 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_PMOS',
                                         'BND_PODummyLayer')
            if tmp2_1[0][0][0][0][0][0]['_XY_left'][0] > tmp2_2[0][0][0][0][0][0]['_XY_left'][0]:
                approaching_coordx = tmp2_2[0][0][0][0][0][0]['_XY_left'][0]
            else:
                approaching_coordx = tmp2_1[0][0][0][0][0][0]['_XY_left'][0]
                ##Y
            tmp2_3 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_PMOS',
                                         'BND_{}Layer'.format(_Mst_Xgate1_PMOS_XVT))
            approaching_coordy = tmp2_3[0][0][0][0][0][0]['_XY_down'][1]
            approaching_coord = [approaching_coordx, approaching_coordy]
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Thermo_Cnt')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[0] = New_Scoord[0] + _Test_distance
            tmpXY.append(New_Scoord)

            ## Define Coordinates
            self._DesignParameter['SRF_Thermo_Cnt']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## DAC Controller Gen.
        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_DAC_Ctrl'] = self._SrefElementDeclaration(
            _DesignObj=D04_01_SetRstDFF_Nor_Routing_KJH1._SetRstDFF_Nor_Routing(_DesignParameter=None,
                                                                                _Name='{}:SRF_DAC_Ctrl'.format(_Name)))[
            0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_DAC_Ctrl']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DAC_Ctrl']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DAC_Ctrl']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters1)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DAC_Ctrl']['_XYCoordinates'] = [[0, 0]]

        ## Get_Scoord_v4.
        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'BND_Nbody_M1Exten')
        target_coord = tmp1[0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_DAC_Ctrl', 'BND_Nbody_M1Exten')
        approaching_coord = tmp2[0][0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_DAC_Ctrl')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define Coordinates
        self._DesignParameter['SRF_DAC_Ctrl']['_XYCoordinates'] = tmpXY

        ## Get_Scoord_v4.
        ## Calculate Sref XYcoord
        tmpXY = self._DesignParameter['SRF_DAC_Ctrl']['_XYCoordinates']
        for i in range(0, _NumofBit):
            ## Calculate
            ## Target_coord: _XY_type1
            ##X
            tmp1_1 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'SRF_NMOS',
                                         'BND_PODummyLayer')
            tmp1_2 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'SRF_PMOS',
                                         'BND_PODummyLayer')
            if tmp1_1[i][0][0][0][-1][0]['_XY_right'][0] > tmp1_2[i][0][0][0][-1][0]['_XY_right'][0]:
                target_coordx = tmp1_1[i][0][0][0][-1][0]['_XY_right'][0]
            else:
                target_coordx = tmp1_2[i][0][0][0][-1][0]['_XY_right'][0]
                ##Y
            tmp1_3 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'SRF_PMOS',
                                         'BND_{}Layer'.format(_Slv_Inv3_PMOS_XVT))
            target_coordy = tmp1_3[i][0][0][0][0][0]['_XY_down'][1]

            target_coord = [target_coordx, target_coordy]
            ## Approaching_coord: _XY_type2
            ##X
            tmp2_1 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_NMOS',
                                         'BND_PODummyLayer')
            tmp2_2 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_PMOS',
                                         'BND_PODummyLayer')
            if tmp2_1[0][0][0][0][0][0]['_XY_right'][0] > tmp2_2[0][0][0][0][0][0]['_XY_right'][0]:
                approaching_coordx = tmp2_1[0][0][0][0][0][0]['_XY_left'][0]
            else:
                approaching_coordx = tmp2_2[0][0][0][0][0][0]['_XY_left'][0]
                ##Y
            tmp2_3 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_PMOS',
                                         'BND_{}Layer'.format(_Mst_Xgate1_PMOS_XVT))
            approaching_coordy = tmp2_3[0][0][0][0][0][0]['_XY_down'][1]
            approaching_coord = [approaching_coordx, approaching_coordy]
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_DAC_Ctrl')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[0] = New_Scoord[0] + _Test_distance
            tmpXY.append(New_Scoord)

            ## Define Coordinates
            self._DesignParameter['SRF_DAC_Ctrl']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Body Cover.
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Body Cover: PBody
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Body Cover: PBody: M1 Exten
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Pbody_M1Exten'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_Pbody',
                                   'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        self._DesignParameter['BND_Pbody_M1Exten']['_YWidth'] = tmp1[0][0][0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_Pbody',
                                   'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'SRF_Pbody',
                                   'SRF_PbodyContactPhyLen', 'BND_Met1Layer')

        self._DesignParameter['BND_Pbody_M1Exten']['_XWidth'] = abs(
            tmp2[-1][0][0][0][0][0][0]['_XY_right'][0] - tmp1[0][0][0][0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Pbody_M1Exten']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Pbody_M1Exten']['_XYCoordinates'] = [[0, 0]]
        for i in range(0, 2):
            if i == 0:
                ## Calculate
                ## Target_coord: _XY_type1
                tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_Pbody',
                                           'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
                target_coord = tmp1[0][0][0][0][0][0][0]['_XY_down_left']
                ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('BND_Pbody_M1Exten')
                approaching_coord = tmp2[0][0]['_XY_up_left']
                ## Sref coord
                tmp3 = self.get_param_KJH4('BND_Pbody_M1Exten')
                Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
            else:
                ## Calculate
                ## Target_coord: _XY_type1
                tmp1 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_Pbody',
                                           'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
                target_coord = tmp1[0][0][0][0][0][0][0]['_XY_down_left']
                ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('BND_Pbody_M1Exten')
                approaching_coord = tmp2[0][0]['_XY_down_left']
                ## Sref coord
                tmp3 = self.get_param_KJH4('BND_Pbody_M1Exten')
                Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
                ## Define coordinates
        self._DesignParameter['BND_Pbody_M1Exten']['_XYCoordinates'] = tmpXY
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Body Cover: PBody: RX Exten
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Pbody_RXExten'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0],
            _Datatype=DesignParameters._LayerMapping['DIFF'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_Pbody',
                                   'SRF_PbodyContactPhyLen', 'BND_ODLayer')
        self._DesignParameter['BND_Pbody_RXExten']['_YWidth'] = tmp1[0][0][0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_Pbody',
                                   'SRF_PbodyContactPhyLen', 'BND_ODLayer')
        tmp2 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'SRF_Pbody',
                                   'SRF_PbodyContactPhyLen', 'BND_ODLayer')

        self._DesignParameter['BND_Pbody_RXExten']['_XWidth'] = abs(
            tmp2[-1][0][0][0][0][0][0]['_XY_right'][0] - tmp1[0][0][0][0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Pbody_RXExten']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Pbody_RXExten']['_XYCoordinates'] = [[0, 0]]
        for i in range(0, 2):
            if i == 0:
                ## Calculate
                ## Target_coord: _XY_type1
                tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_Pbody',
                                           'SRF_PbodyContactPhyLen', 'BND_ODLayer')
                target_coord = tmp1[0][0][0][0][0][0][0]['_XY_down_left']
                ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('BND_Pbody_RXExten')
                approaching_coord = tmp2[0][0]['_XY_up_left']
                ## Sref coord
                tmp3 = self.get_param_KJH4('BND_Pbody_RXExten')
                Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
            else:
                ## Calculate
                ## Target_coord: _XY_type1
                tmp1 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_Pbody',
                                           'SRF_PbodyContactPhyLen', 'BND_ODLayer')
                target_coord = tmp1[0][0][0][0][0][0][0]['_XY_down_left']
                ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('BND_Pbody_RXExten')
                approaching_coord = tmp2[0][0]['_XY_down_left']
                ## Sref coord
                tmp3 = self.get_param_KJH4('BND_Pbody_RXExten')
                Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
                ## Define coordinates
        self._DesignParameter['BND_Pbody_RXExten']['_XYCoordinates'] = tmpXY
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Body Cover: PBody: Bp Exten
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Pbody_PPExten'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_Pbody',
                                   'SRF_PbodyContactPhyLen', 'BND_PPLayer')
        self._DesignParameter['BND_Pbody_PPExten']['_YWidth'] = tmp1[0][0][0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_Pbody',
                                   'SRF_PbodyContactPhyLen', 'BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'SRF_Pbody',
                                   'SRF_PbodyContactPhyLen', 'BND_PPLayer')

        self._DesignParameter['BND_Pbody_PPExten']['_XWidth'] = abs(
            tmp2[-1][0][0][0][0][0][0]['_XY_right'][0] - tmp1[0][0][0][0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Pbody_PPExten']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Pbody_PPExten']['_XYCoordinates'] = [[0, 0]]
        for i in range(0, 2):
            if i == 0:
                ## Calculate
                ## Target_coord: _XY_type1
                tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_Pbody',
                                           'SRF_PbodyContactPhyLen', 'BND_PPLayer')
                target_coord = tmp1[0][0][0][0][0][0][0]['_XY_down_left']
                ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('BND_Pbody_PPExten')
                approaching_coord = tmp2[0][0]['_XY_up_left']
                ## Sref coord
                tmp3 = self.get_param_KJH4('BND_Pbody_PPExten')
                Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
            else:
                ## Calculate
                ## Target_coord: _XY_type1
                tmp1 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_Pbody',
                                           'SRF_PbodyContactPhyLen', 'BND_PPLayer')
                target_coord = tmp1[0][0][0][0][0][0][0]['_XY_down_left']
                ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('BND_Pbody_PPExten')
                approaching_coord = tmp2[0][0]['_XY_down_left']
                ## Sref coord
                tmp3 = self.get_param_KJH4('BND_Pbody_PPExten')
                Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)

                ## Define coordinates
        self._DesignParameter['BND_Pbody_PPExten']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Body Cover: NBody
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Body Cover: NBody: M1 Exten
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Nbody_M1Exten'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_Nbody',
                                   'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        self._DesignParameter['BND_Nbody_M1Exten']['_YWidth'] = tmp1[0][0][0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_Nbody',
                                   'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'SRF_Nbody',
                                   'SRF_NbodyContactPhyLen', 'BND_Met1Layer')

        self._DesignParameter['BND_Nbody_M1Exten']['_XWidth'] = abs(
            tmp2[-1][0][0][0][0][0][0]['_XY_right'][0] - tmp1[0][0][0][0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Nbody_M1Exten']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Nbody_M1Exten']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_Nbody',
                                   'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        target_coord = tmp1[0][0][0][0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Nbody_M1Exten')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Nbody_M1Exten')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Nbody_M1Exten']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Body Cover: NBody: RX Exten
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Nbody_RXExten'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0],
            _Datatype=DesignParameters._LayerMapping['DIFF'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_Nbody',
                                   'SRF_NbodyContactPhyLen', 'BND_ODLayer')
        self._DesignParameter['BND_Nbody_RXExten']['_YWidth'] = tmp1[0][0][0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_Nbody',
                                   'SRF_NbodyContactPhyLen', 'BND_ODLayer')
        tmp2 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'SRF_Nbody',
                                   'SRF_NbodyContactPhyLen', 'BND_ODLayer')

        self._DesignParameter['BND_Nbody_RXExten']['_XWidth'] = abs(
            tmp2[-1][0][0][0][0][0][0]['_XY_right'][0] - tmp1[0][0][0][0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Nbody_RXExten']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Nbody_RXExten']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_Nbody',
                                   'SRF_NbodyContactPhyLen', 'BND_ODLayer')
        target_coord = tmp1[0][0][0][0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Nbody_RXExten')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Nbody_RXExten')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Nbody_RXExten']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Body Cover: NBody: Nwell Exten
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Nbody_NwellExten'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'BND_PMOS_NellExten')
        tmp2 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'BND_PMOS_NellExten')
        self._DesignParameter['BND_Nbody_NwellExten']['_YWidth'] = abs(
            tmp1[0][0][0][0][0]['_XY_down'][1] - tmp2[0][0][0][0][0]['_XY_down'][1])

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'BND_PMOS_NellExten')
        tmp2 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'BND_PMOS_NellExten')

        self._DesignParameter['BND_Nbody_NwellExten']['_XWidth'] = abs(
            tmp2[-1][0][0][0][0]['_XY_right'][0] - tmp1[0][0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Nbody_NwellExten']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Nbody_NwellExten']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'BND_PMOS_NellExten')
        target_coord = tmp1[0][0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Nbody_NwellExten')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Nbody_NwellExten')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Nbody_NwellExten']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## SRF_Thermo_Counter [1]~[-1] : Set--VSS
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## SRF_Thermo_Counter [1]~[-1] : Set--VSS : M1 Hrz
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Thermo_Cnt_Set_Hrz_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Thermo_Cnt_Set_Hrz_M1']['_YWidth'] = _Routing_width

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Inv1', 'SRF_NMOS',
                                   'BND_Gate_Hrz_Mx')
        tmp2 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_Net8_ViaM1M4', 'SRF_ViaM1M2', 'BND_Met2Layer')

        self._DesignParameter['BND_Thermo_Cnt_Set_Hrz_M1']['_XWidth'] = abs(
            tmp2[0][0][0][0][0]['_XY_cent'][0] - tmp1[0][0][0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Thermo_Cnt_Set_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Thermo_Cnt_Set_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
        for i in range(1, _NumofBit + 1):
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Inv1', 'SRF_NMOS',
                                       'BND_Gate_Hrz_Mx')
            target_coord = tmp1[i][0][0][0][0][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Thermo_Cnt_Set_Hrz_M1')
            approaching_coord = tmp2[0][0]['_XY_up_right']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Thermo_Cnt_Set_Hrz_M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_Thermo_Cnt_Set_Hrz_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## SRF_Thermo_Counter [1]~[-1] : Set--VSS : M1 Vtc
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Thermo_Cnt_Set_Vtc_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_Thermo_Cnt_Set_Hrz_M1')
        tmp2 = self.get_param_KJH4('SRF_Thermo_Cnt', 'BND_Pbody_M1Exten')
        self._DesignParameter['BND_Thermo_Cnt_Set_Vtc_M1']['_YWidth'] = abs(
            tmp1[0][0]['_XY_down'][1] - tmp2[0][0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Thermo_Cnt_Set_Vtc_M1']['_XWidth'] = _Routing_width

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Thermo_Cnt_Set_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Thermo_Cnt_Set_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
        for i in range(0, _NumofBit):
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('BND_Thermo_Cnt_Set_Hrz_M1')
            target_coord = tmp1[i][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Thermo_Cnt_Set_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_down']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Thermo_Cnt_Set_Vtc_M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_Thermo_Cnt_Set_Vtc_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## SRF_Thermo_Counter [0] input to VSS
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Thermo_Cnt0_Input_Vtc_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_NMOS',
                                   'BND_Source_M1')
        tmp2 = self.get_param_KJH4('SRF_Thermo_Cnt', 'BND_Pbody_M1Exten')
        self._DesignParameter['BND_Thermo_Cnt0_Input_Vtc_M1']['_YWidth'] = abs(
            tmp1[0][0][0][0][0][0]['_XY_up'][1] - tmp2[0][0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Thermo_Cnt0_Input_Vtc_M1']['_XWidth'] = _Routing_width

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Thermo_Cnt0_Input_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Thermo_Cnt0_Input_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_NMOS',
                                   'BND_Source_M1')
        target_coord = tmp1[0][0][0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Thermo_Cnt0_Input_Vtc_M1')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Thermo_Cnt0_Input_Vtc_M1')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Thermo_Cnt0_Input_Vtc_M1']['_XYCoordinates'] = tmpXY

        ## 10/23 수정한 부분 -> 주석 처리
        # ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## SRF_DAC_Ctrl [-1] input to VSS
        # ## Boundary_element Generation
        # ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        # self._DesignParameter['BND_DAC_Ctrlend_Input_Vtc_M1'] = self._BoundaryElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL1'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        #     _XWidth=None,
        #     _YWidth=None,
        #     _XYCoordinates=[],
        # )
        #
        # ## Define Boundary_element _YWidth
        # tmp1 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_NMOS',
        #                            'BND_Source_M1')
        # tmp2 = self.get_param_KJH4('SRF_DAC_Ctrl', 'BND_Pbody_M1Exten')
        # self._DesignParameter['BND_DAC_Ctrlend_Input_Vtc_M1']['_YWidth'] = abs(
        #     tmp1[0][0][0][0][0][0]['_XY_up'][1] - tmp2[0][0][0]['_XY_up'][1])
        #
        # ## Define Boundary_element _XWidth
        # self._DesignParameter['BND_DAC_Ctrlend_Input_Vtc_M1']['_XWidth'] = _Routing_width
        #
        # ## Define Boundary_element _XYCoordinates
        # self._DesignParameter['BND_DAC_Ctrlend_Input_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
        #
        # ## Calculate Sref XYcoord
        # tmpXY = []
        # ## initialized Sref coordinate
        # self._DesignParameter['BND_DAC_Ctrlend_Input_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
        # ## Calculate
        # ## Target_coord: _XY_type1
        # tmp1 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_NMOS',
        #                            'BND_Source_M1')
        # target_coord = tmp1[-1][0][0][0][0][0]['_XY_up_left']
        # ## Approaching_coord: _XY_type2
        # tmp2 = self.get_param_KJH4('BND_DAC_Ctrlend_Input_Vtc_M1')
        # approaching_coord = tmp2[0][0]['_XY_up_left']
        # ## Sref coord
        # tmp3 = self.get_param_KJH4('BND_DAC_Ctrlend_Input_Vtc_M1')
        # Scoord = tmp3[0][0]['_XY_origin']
        # ## Cal
        # New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        # tmpXY.append(New_Scoord)
        # ## Define coordinates
        # self._DesignParameter['BND_DAC_Ctrlend_Input_Vtc_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## SRF_Thermo_Cnt [0] RST to VSS
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## SRF_Thermo_Cnt [0] RST to VSS : M1 Hrz
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Thermo_Cnt0_RST_Hrz_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Thermo_Cnt0_RST_Hrz_M1']['_YWidth'] = _Routing_width

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Slv_Inv1', 'SRF_NMOS',
                                   'BND_Gate_Hrz_Mx')
        tmp2 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_Net12_ViaM1M4', 'SRF_ViaM1M2', 'BND_Met2Layer')

        self._DesignParameter['BND_Thermo_Cnt0_RST_Hrz_M1']['_XWidth'] = abs(
            tmp2[0][0][0][0][0]['_XY_cent'][0] - tmp1[0][0][0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Thermo_Cnt0_RST_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Thermo_Cnt0_RST_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Slv_Inv1', 'SRF_NMOS',
                                   'BND_Gate_Hrz_Mx')
        target_coord = tmp1[0][0][0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Thermo_Cnt0_RST_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Thermo_Cnt0_RST_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Thermo_Cnt0_RST_Hrz_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## SRF_Thermo_Cnt [0] RST to VSS : M1 Vtc
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Thermo_Cnt0_RST_Vtc_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_Thermo_Cnt_Set_Hrz_M1')
        tmp2 = self.get_param_KJH4('SRF_Thermo_Cnt', 'BND_Pbody_M1Exten')
        self._DesignParameter['BND_Thermo_Cnt0_RST_Vtc_M1']['_YWidth'] = abs(
            tmp1[0][0]['_XY_down'][1] - tmp2[0][0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Thermo_Cnt0_RST_Vtc_M1']['_XWidth'] = _Routing_width

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Thermo_Cnt0_RST_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Thermo_Cnt0_RST_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_Thermo_Cnt0_RST_Hrz_M1')
        target_coord = tmp1[0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Thermo_Cnt0_RST_Vtc_M1')
        approaching_coord = tmp2[0][0]['_XY_down']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Thermo_Cnt0_RST_Vtc_M1')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Thermo_Cnt0_RST_Vtc_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## SRF_DAC_ctrl [0] RST to VSS
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## SRF_DAC_ctrl [0] RST to VSS : M1 Hrz
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_DAC_ctrl0_RST_Hrz_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_DAC_ctrl0_RST_Hrz_M1']['_YWidth'] = _Routing_width

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_SetRst_Placement', 'SRF_Slv_Inv1', 'SRF_NMOS',
                                   'BND_Gate_Hrz_Mx')
        tmp2 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_Net12_ViaM1M4', 'SRF_ViaM1M2', 'BND_Met2Layer')

        self._DesignParameter['BND_DAC_ctrl0_RST_Hrz_M1']['_XWidth'] = abs(
            tmp2[0][0][0][0][0]['_XY_cent'][0] - tmp1[0][0][0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_DAC_ctrl0_RST_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_DAC_ctrl0_RST_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_SetRst_Placement', 'SRF_Slv_Inv1', 'SRF_NMOS',
                                   'BND_Gate_Hrz_Mx')
        target_coord = tmp1[0][0][0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_DAC_ctrl0_RST_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_down_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_DAC_ctrl0_RST_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_DAC_ctrl0_RST_Hrz_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## SRF_DAC_ctrl [0] RST to VSS : M1 Vtc
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_DAC_ctrl0_RST_Vtc_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_Thermo_Cnt_Set_Hrz_M1')
        tmp2 = self.get_param_KJH4('SRF_Thermo_Cnt', 'BND_Pbody_M1Exten')
        self._DesignParameter['BND_DAC_ctrl0_RST_Vtc_M1']['_YWidth'] = abs(
            tmp1[0][0]['_XY_down'][1] - tmp2[0][0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_DAC_ctrl0_RST_Vtc_M1']['_XWidth'] = _Routing_width

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_DAC_ctrl0_RST_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_DAC_ctrl0_RST_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_DAC_ctrl0_RST_Hrz_M1')
        target_coord = tmp1[0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_DAC_ctrl0_RST_Vtc_M1')
        approaching_coord = tmp2[0][0]['_XY_up']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_DAC_ctrl0_RST_Vtc_M1')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_DAC_ctrl0_RST_Vtc_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Thermo Cnt Q - D
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Thermo Cnt Q - D : M1 Hrz
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Thermo_QD_Hrz_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Thermo_QD_Hrz_M1']['_YWidth'] = _Routing_width

        ## Define Boundary_element _XWidth
        tmp1_1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'BND_Input_Vtc_M1')
        tmp1_2 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_NMOS',
                                     'BND_PODummyLayer')
        tmp1_3 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_PMOS',
                                     'BND_PODummyLayer')
        tmp1_4 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'SRF_NMOS',
                                     'BND_PODummyLayer')
        tmp1_5 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'SRF_PMOS',
                                     'BND_PODummyLayer')

        if tmp1_2[1][0][0][0][0][0]['_XY_left'][0] > tmp1_3[1][0][0][0][0][0]['_XY_left'][0]:
            tmp_left = tmp1_3[1][0][0][0][0][0]['_XY_left'][0]
        else:
            tmp_left = tmp1_2[1][0][0][0][0][0]['_XY_left'][0]

        if tmp1_4[0][0][0][0][-1][0]['_XY_right'][0] > tmp1_5[0][0][0][0][-1][0]['_XY_right'][0]:
            tmp_right = tmp1_4[0][0][0][0][-1][0]['_XY_right'][0]
        else:
            tmp_right = tmp1_5[0][0][0][0][-1][0]['_XY_right'][0]

        self._DesignParameter['BND_Thermo_QD_Hrz_M1']['_XWidth'] = abs(
            np.round(0.5 * (tmp_left + tmp_right)) - tmp1_1[0][0][0][0][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Thermo_QD_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Thermo_QD_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
        for i in range(0, _NumofBit):
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'BND_Net21_Hrz1_M1')
            target_coord = tmp1[i][0][0]['_XY_down_right']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Thermo_QD_Hrz_M1')
            approaching_coord = tmp2[0][0]['_XY_up_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Thermo_QD_Hrz_M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_Thermo_QD_Hrz_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Thermo Cnt Q - D : ViaM1M2
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_Thermo_QD_ViaM1M2'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_Thermo_QD_ViaM1M2'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_Thermo_QD_ViaM1M2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_Thermo_QD_ViaM1M2']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Thermo_QD_ViaM1M2']['_DesignObj']._CalculateDesignParameterYmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_Thermo_QD_ViaM1M2']['_XYCoordinates'] = [[0, 0]]
        for i in range(0, _NumofBit):
            ## Calculate
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_Thermo_QD_Hrz_M1')
            target_coord = tmp1[i][0]['_XY_right']
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_Thermo_QD_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Thermo_QD_ViaM1M2')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define
        self._DesignParameter['SRF_Thermo_QD_ViaM1M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Thermo Cnt Q - D : M2 Hrz
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Thermo_QD_Hrz2_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Thermo_QD_Hrz2_M2']['_YWidth'] = _Routing_width

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('BND_Thermo_QD_Hrz_M1')
        tmp2 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'BND_Input_Vtc_M2')
        self._DesignParameter['BND_Thermo_QD_Hrz2_M2']['_XWidth'] = abs(
            tmp1[0][0]['_XY_right'][0] - tmp2[1][0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Thermo_QD_Hrz2_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Thermo_QD_Hrz2_M2']['_XYCoordinates'] = [[0, 0]]
        for i in range(0, _NumofBit):
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('BND_Thermo_QD_Hrz_M1')
            target_coord = tmp1[i][0]['_XY_down_right']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Thermo_QD_Hrz2_M2')
            approaching_coord = tmp2[0][0]['_XY_down_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Thermo_QD_Hrz2_M2')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_Thermo_QD_Hrz2_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Thermo Cnt Q -- DAC ctrl Set
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Thermo Cnt Q -- DAC ctrl Set : ViaM3M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_TherQ_DACCtrlSet_ViaM3M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_TherQ_DACCtrlSet_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_TherQ_DACCtrlSet_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_TherQ_DACCtrlSet_ViaM3M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_TherQ_DACCtrlSet_ViaM3M4']['_DesignObj']._CalculateDesignParameterYmin(
            **_Caculation_Parameters)

        ## Define
        tmpXY = []
        for i in range(0, _NumofBit + 1):
            tmp = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_Net18_1_ViaM2M3')
            tmpXY.append(tmp[i][0][0]['_XY_origin'])
        self._DesignParameter['SRF_TherQ_DACCtrlSet_ViaM3M4']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Thermo Cnt Q -- DAC ctrl Set : M4 Vtc
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_TherQ_DACCtrlSet_Vtc_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_TherQ_DACCtrlSet_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        tmp2 = self.get_param_KJH4('BND_Nbody_NwellExten')
        self._DesignParameter['BND_TherQ_DACCtrlSet_Vtc_M4']['_YWidth'] = abs(
            tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0]['_XY_down'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_TherQ_DACCtrlSet_Vtc_M4']['_XWidth'] = _Routing_width

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_TherQ_DACCtrlSet_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_TherQ_DACCtrlSet_Vtc_M4']['_XYCoordinates'] = [[0, 0]]
        for i in range(0, _NumofBit + 1):
            ## Calculate
            ## Target_coord: _XY_type1
            ##X
            tmp1_1 = self.get_param_KJH4('SRF_TherQ_DACCtrlSet_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
            target_coord = tmp1_1[i][0][0][0]['_XY_up']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_TherQ_DACCtrlSet_Vtc_M4')
            approaching_coord = tmp2[0][0]['_XY_up']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_TherQ_DACCtrlSet_Vtc_M4')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_TherQ_DACCtrlSet_Vtc_M4']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Thermo Cnt Q -- DAC ctrl Set : ViaM3M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_TherQ_DACCtrlSet_ViaM3M4_1'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_TherQ_DACCtrlSet_ViaM3M4_1'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_TherQ_DACCtrlSet_ViaM3M4_1']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_TherQ_DACCtrlSet_ViaM3M4_1']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_TherQ_DACCtrlSet_ViaM3M4_1']['_DesignObj']._CalculateDesignParameterYmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_TherQ_DACCtrlSet_ViaM3M4_1']['_XYCoordinates'] = [[0, 0]]
        for i in range(0, _NumofBit + 1):
            ## Calculate
            ## Target_coord
            ## X
            tmp1_1 = self.get_param_KJH4('SRF_TherQ_DACCtrlSet_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
            target_coordx = tmp1_1[i][0][0][0]['_XY_left'][0]
            ## Y
            tmp1_2 = self.get_param_KJH4('BND_TherQ_DACCtrlSet_Vtc_M4')
            target_coordy = tmp1_2[i][0]['_XY_down'][1]

            target_coord = [target_coordx, target_coordy]
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_TherQ_DACCtrlSet_ViaM3M4_1', 'SRF_ViaM3M4', 'BND_Met4Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_down_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_TherQ_DACCtrlSet_ViaM3M4_1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        self._DesignParameter['SRF_TherQ_DACCtrlSet_ViaM3M4_1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Thermo Cnt Q -- DAC ctrl Set : M3 Hrz
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_TherQ_DACCtrlSet_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_TherQ_DACCtrlSet_Hrz_M3']['_YWidth'] = _Routing_width

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('BND_TherQ_DACCtrlSet_Vtc_M4')
        tmp2 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_Net8_ViaM1M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        self._DesignParameter['BND_TherQ_DACCtrlSet_Hrz_M3']['_XWidth'] = abs(
            tmp1[0][0]['_XY_right'][0] - tmp2[0][0][0][0][0]['_XY_cent'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_TherQ_DACCtrlSet_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_TherQ_DACCtrlSet_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
        for i in range(0, _NumofBit + 1):
            ## Calculate
            ## Target_coord: _XY_type1
            ##X
            tmp1_1 = self.get_param_KJH4('BND_TherQ_DACCtrlSet_Vtc_M4')
            target_coord = tmp1_1[i][0]['_XY_down_right']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_TherQ_DACCtrlSet_Hrz_M3')
            approaching_coord = tmp2[0][0]['_XY_down_right']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_TherQ_DACCtrlSet_Hrz_M3')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_TherQ_DACCtrlSet_Hrz_M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Thermo Cnt Q -- DAC ctrl Set : M3 Hrz
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_TherQ_DACCtrlSet_Vtc_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_TherQ_DACCtrlSet_Hrz_M3')
        tmp2 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_Net8_ViaM1M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        self._DesignParameter['BND_TherQ_DACCtrlSet_Vtc_M3']['_YWidth'] = abs(
            tmp1[0][0]['_XY_up'][1] - tmp2[0][0][0][0][0]['_XY_down'][1])

        ## Define Boundary_element _XWidth

        self._DesignParameter['BND_TherQ_DACCtrlSet_Vtc_M3']['_XWidth'] = _Routing_width

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_TherQ_DACCtrlSet_Vtc_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_TherQ_DACCtrlSet_Vtc_M3']['_XYCoordinates'] = [[0, 0]]
        for i in range(0, _NumofBit + 1):
            ## Calculate
            ## Target_coord: _XY_type1
            ##X
            tmp1_1 = self.get_param_KJH4('BND_TherQ_DACCtrlSet_Hrz_M3')
            target_coord = tmp1_1[i][0]['_XY_up_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_TherQ_DACCtrlSet_Vtc_M3')
            approaching_coord = tmp2[0][0]['_XY_up']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_TherQ_DACCtrlSet_Vtc_M3')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_TherQ_DACCtrlSet_Vtc_M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## DAC Ctrl Q -- Clk
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## DAC Ctrl Q -- Clk : ViaM3M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_DACCtrl_QClk_ViaM3M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_DACCtrl_QClk_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_DACCtrl_QClk_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_DACCtrl_QClk_ViaM3M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_DACCtrl_QClk_ViaM3M4']['_DesignObj']._CalculateDesignParameterYmin(
            **_Caculation_Parameters)

        ## Define
        tmpXY = []
        for i in range(1, _NumofBit + 1):
            tmp = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_Net18_1_ViaM2M3')
            tmpXY.append(tmp[i][0][0]['_XY_origin'])
        self._DesignParameter['SRF_DACCtrl_QClk_ViaM3M4']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## DAC Ctrl Q -- Clk : M4 Vtc odd
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_DACCtrl_QClk_Odd_Vtc_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_DACCtrl_QClk_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        tmp2 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_NMOS',
                                   'BND_{}Layer'.format(_Mst_Xgate1_NMOS_XVT))
        self._DesignParameter['BND_DACCtrl_QClk_Odd_Vtc_M4']['_YWidth'] = abs(
            tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_DACCtrl_QClk_Odd_Vtc_M4']['_XWidth'] = _Routing_width

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_DACCtrl_QClk_Odd_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_DACCtrl_QClk_Odd_Vtc_M4']['_XYCoordinates'] = [[0, 0]]
        for i in range(0, _NumofBit):
            if i % 2 == 0:
                ## Calculate
                ## Target_coord: _XY_type1
                ##X
                tmp1_1 = self.get_param_KJH4('SRF_DACCtrl_QClk_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
                target_coord = tmp1_1[i][0][0][0]['_XY_up']
                ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('BND_DACCtrl_QClk_Odd_Vtc_M4')
                approaching_coord = tmp2[0][0]['_XY_up']
                ## Sref coord
                tmp3 = self.get_param_KJH4('BND_DACCtrl_QClk_Odd_Vtc_M4')
                Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
                ## Define coordinates
        self._DesignParameter['BND_DACCtrl_QClk_Odd_Vtc_M4']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## DAC Ctrl Q -- Clk : M4 Vtc even
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_DACCtrl_QClk_Even_Vtc_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_DACCtrl_QClk_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        tmp2 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_NMOS',
                                   'BND_{}Layer'.format(_Mst_Xgate1_NMOS_XVT))
        self._DesignParameter['BND_DACCtrl_QClk_Even_Vtc_M4']['_YWidth'] = abs(
            tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0][0]['_XY_up'][1]) + _Routing_distance + _Routing_width

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_DACCtrl_QClk_Even_Vtc_M4']['_XWidth'] = _Routing_width

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_DACCtrl_QClk_Even_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_DACCtrl_QClk_Even_Vtc_M4']['_XYCoordinates'] = [[0, 0]]
        for i in range(0, _NumofBit):
            if i % 2 != 0:
                ## Calculate
                ## Target_coord: _XY_type1
                ##X
                tmp1_1 = self.get_param_KJH4('SRF_DACCtrl_QClk_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
                target_coord = tmp1_1[i][0][0][0]['_XY_up']
                ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('BND_DACCtrl_QClk_Even_Vtc_M4')
                approaching_coord = tmp2[0][0]['_XY_up']
                ## Sref coord
                tmp3 = self.get_param_KJH4('BND_DACCtrl_QClk_Even_Vtc_M4')
                Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
                ## Define coordinates
        self._DesignParameter['BND_DACCtrl_QClk_Even_Vtc_M4']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## DAC Ctrl Q -- Clk : ViaM3M4 : Odd
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_DACCtrl_QClk_Odd_ViaM3M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_DACCtrl_QClk_Odd_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_DACCtrl_QClk_Odd_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_DACCtrl_QClk_Odd_ViaM3M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_DACCtrl_QClk_Odd_ViaM3M4']['_DesignObj']._CalculateDesignParameterYmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_DACCtrl_QClk_Odd_ViaM3M4']['_XYCoordinates'] = [[0, 0]]

        tmp = self.get_param_KJH4('BND_DACCtrl_QClk_Odd_Vtc_M4')
        for i in range(0, len(tmp)):
            ## Calculate
            ## Target_coord
            ## X
            tmp1_1 = self.get_param_KJH4('BND_DACCtrl_QClk_Odd_Vtc_M4')
            target_coordx = tmp1_1[i][0]['_XY_down'][0]
            ## Y
            tmp1_2 = self.get_param_KJH4('BND_DACCtrl_QClk_Odd_Vtc_M4')
            target_coordy = tmp1_2[i][0]['_XY_down'][1]

            target_coord = [target_coordx, target_coordy]
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_DACCtrl_QClk_Odd_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_up']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_DACCtrl_QClk_Odd_ViaM3M4')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        self._DesignParameter['SRF_DACCtrl_QClk_Odd_ViaM3M4']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## DAC Ctrl Q -- Clk : ViaM3M4 : Even
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 4
        _Caculation_Parameters['_Layer2'] = 5
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_DACCtrl_QClk_Even_ViaM4M5'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_DACCtrl_QClk_Even_ViaM4M5'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_DACCtrl_QClk_Even_ViaM4M5']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_DACCtrl_QClk_Even_ViaM4M5']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_DACCtrl_QClk_Even_ViaM4M5']['_DesignObj']._CalculateDesignParameterYmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_DACCtrl_QClk_Even_ViaM4M5']['_XYCoordinates'] = [[0, 0]]

        tmp = self.get_param_KJH4('BND_DACCtrl_QClk_Even_Vtc_M4')
        for i in range(0, len(tmp)):
            ## Calculate
            ## Target_coord
            ## X
            tmp1_1 = self.get_param_KJH4('BND_DACCtrl_QClk_Even_Vtc_M4')
            target_coordx = tmp1_1[i][0]['_XY_down'][0]
            ## Y
            tmp1_2 = self.get_param_KJH4('BND_DACCtrl_QClk_Even_Vtc_M4')
            target_coordy = tmp1_2[i][0]['_XY_down'][1]

            target_coord = [target_coordx, target_coordy]
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_DACCtrl_QClk_Even_ViaM4M5', 'SRF_ViaM4M5', 'BND_Met5Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_up']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_DACCtrl_QClk_Even_ViaM4M5')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        self._DesignParameter['SRF_DACCtrl_QClk_Even_ViaM4M5']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## DAC Ctrl Q -- Clk : M3 Hrz odd
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_DACCtrl_QClk_Odd_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_DACCtrl_QClk_Odd_Hrz_M3']['_YWidth'] = _Routing_width

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('BND_DACCtrl_QClk_Odd_Vtc_M4')
        tmp2 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_Net3_ViaM1M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        self._DesignParameter['BND_DACCtrl_QClk_Odd_Hrz_M3']['_XWidth'] = abs(
            tmp1[0][0]['_XY_right'][0] - tmp2[0][0][0][0][0]['_XY_cent'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_DACCtrl_QClk_Odd_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_DACCtrl_QClk_Odd_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
        tmp = self.get_param_KJH4('BND_DACCtrl_QClk_Odd_Vtc_M4')
        for i in range(0, len(tmp)):
            ## Calculate
            ## Target_coord: _XY_type1
            ##X
            tmp1_1 = self.get_param_KJH4('BND_DACCtrl_QClk_Odd_Vtc_M4')
            target_coord = tmp1_1[i][0]['_XY_down_right']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_DACCtrl_QClk_Odd_Hrz_M3')
            approaching_coord = tmp2[0][0]['_XY_up_right']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_DACCtrl_QClk_Odd_Hrz_M3')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_DACCtrl_QClk_Odd_Hrz_M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## DAC Ctrl Q -- Clk : M4 Hrz odd
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_DACCtrl_QClk_Even_Hrz_M5'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5'][0],
            _Datatype=DesignParameters._LayerMapping['METAL5'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_DACCtrl_QClk_Even_Hrz_M5']['_YWidth'] = _Routing_width

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('BND_DACCtrl_QClk_Even_Vtc_M4')
        tmp2 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_Net3_ViaM1M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        self._DesignParameter['BND_DACCtrl_QClk_Even_Hrz_M5']['_XWidth'] = abs(
            tmp1[0][0]['_XY_right'][0] - tmp2[1][0][0][0][0]['_XY_cent'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_DACCtrl_QClk_Even_Hrz_M5']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_DACCtrl_QClk_Even_Hrz_M5']['_XYCoordinates'] = [[0, 0]]
        tmp = self.get_param_KJH4('BND_DACCtrl_QClk_Even_Vtc_M4')
        for i in range(0, len(tmp)):
            ## Calculate
            ## Target_coord: _XY_type1
            ##X
            tmp1_1 = self.get_param_KJH4('BND_DACCtrl_QClk_Even_Vtc_M4')
            target_coord = tmp1_1[i][0]['_XY_down_right']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_DACCtrl_QClk_Even_Hrz_M5')
            approaching_coord = tmp2[0][0]['_XY_up_right']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_DACCtrl_QClk_Even_Hrz_M5')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_DACCtrl_QClk_Even_Hrz_M5']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## DAC Ctrl Q -- Clk : M3 vtc odd
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_DACCtrl_QClk_Odd_Vtc_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_DACCtrl_QClk_Odd_Hrz_M3')
        tmp2 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_Net7_ViaM1M3_1', 'SRF_ViaM2M3', 'BND_Met3Layer')
        self._DesignParameter['BND_DACCtrl_QClk_Odd_Vtc_M3']['_YWidth'] = abs(
            tmp1[0][0]['_XY_down'][1] - tmp2[0][0][0][0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_DACCtrl_QClk_Odd_Vtc_M3']['_XWidth'] = _Routing_width

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_DACCtrl_QClk_Odd_Vtc_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_DACCtrl_QClk_Odd_Vtc_M3']['_XYCoordinates'] = [[0, 0]]
        tmp = self.get_param_KJH4('BND_DACCtrl_QClk_Odd_Hrz_M3')
        for i in range(0, len(tmp)):
            ## Calculate
            ## Target_coord: _XY_type1
            ##X
            tmp1_1 = self.get_param_KJH4('BND_DACCtrl_QClk_Odd_Hrz_M3')
            target_coord = tmp1_1[i][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_DACCtrl_QClk_Odd_Vtc_M3')
            approaching_coord = tmp2[0][0]['_XY_down']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_DACCtrl_QClk_Odd_Vtc_M3')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_DACCtrl_QClk_Odd_Vtc_M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## DAC Ctrl Q -- Clk : ViaM1M5 : Even
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 5
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_DACCtrl_QClk_Even_ViaM1M5'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_DACCtrl_QClk_Even_ViaM1M5'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_DACCtrl_QClk_Even_ViaM1M5']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_DACCtrl_QClk_Even_ViaM1M5']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_DACCtrl_QClk_Even_ViaM1M5']['_DesignObj']._CalculateDesignParameterYmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_DACCtrl_QClk_Even_ViaM1M5']['_XYCoordinates'] = [[0, 0]]

        tmp = self.get_param_KJH4('BND_DACCtrl_QClk_Even_Hrz_M5')
        for i in range(0, len(tmp)):
            ## Calculate
            ## Target_coord
            ## X
            tmp1_1 = self.get_param_KJH4('BND_DACCtrl_QClk_Even_Hrz_M5')
            target_coordx = tmp1_1[i][0]['_XY_down_left'][0]
            ## Y
            tmp1_2 = self.get_param_KJH4('BND_DACCtrl_QClk_Even_Hrz_M5')
            target_coordy = tmp1_2[i][0]['_XY_down_left'][1]

            target_coord = [target_coordx, target_coordy]
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_DACCtrl_QClk_Even_ViaM1M5', 'SRF_ViaM4M5', 'BND_Met5Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_down']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_DACCtrl_QClk_Even_ViaM1M5')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        self._DesignParameter['SRF_DACCtrl_QClk_Even_ViaM1M5']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## DAC Ctrl Q -- Clk : M1 vtc Even
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_DACCtrl_QClk_Even_Vtc_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_DACCtrl_QClk_Even_Hrz_M5')
        tmp2 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_Net7_ViaM1M3_1', 'SRF_ViaM2M3', 'BND_Met3Layer')
        self._DesignParameter['BND_DACCtrl_QClk_Even_Vtc_M1']['_YWidth'] = abs(
            tmp1[0][0]['_XY_down'][1] - tmp2[1][0][0][0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_DACCtrl_QClk_Even_Vtc_M1']['_XWidth'] = _Routing_width

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_DACCtrl_QClk_Even_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_DACCtrl_QClk_Even_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        tmp = self.get_param_KJH4('BND_DACCtrl_QClk_Even_Hrz_M5')
        for i in range(0, len(tmp)):
            ## Calculate
            ## Target_coord: _XY_type1
            ##X
            tmp1_1 = self.get_param_KJH4('BND_DACCtrl_QClk_Even_Hrz_M5')
            target_coord = tmp1_1[i][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_DACCtrl_QClk_Even_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_down']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_DACCtrl_QClk_Even_Vtc_M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_DACCtrl_QClk_Even_Vtc_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Thermometer CLK
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Thermometer CLK : Vtc M4

        ## Pre-defined
        Ylegnth = _SpaceBtwPbodyAndCLKSrc
        Xwidth = 50

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Therm_Clk_Vtc_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_Net3_ViaM1M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        tmp2 = self.get_param_KJH4('SRF_Thermo_Cnt', 'BND_Pbody_M1Exten')
        self._DesignParameter['BND_Therm_Clk_Vtc_M4']['_YWidth'] = abs(
            tmp1[0][0][0][0][0]['_XY_up'][1] - tmp2[0][0][0]['_XY_down'][1]) + Ylegnth

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Therm_Clk_Vtc_M4']['_XWidth'] = Xwidth

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Therm_Clk_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Therm_Clk_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

        tmp = self.get_param_KJH4('SRF_Thermo_Cnt')
        for i in range(0, len(tmp)):
            ## Calculate
            ## Target_coord: _XY_type1
            ##X
            tmp1_1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_Net3_ViaM1M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
            target_coord = tmp1_1[i][0][0][0][0]['_XY_up']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Therm_Clk_Vtc_M4')
            approaching_coord = tmp2[0][0]['_XY_down']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Therm_Clk_Vtc_M4')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_Therm_Clk_Vtc_M4']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Thermometer CLK : ViaM3M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_Therm_Clk_ViaM3M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_Therm_Clk_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_Therm_Clk_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_Therm_Clk_ViaM3M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Therm_Clk_ViaM3M4']['_DesignObj']._CalculateDesignParameterYmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_Therm_Clk_ViaM3M4']['_XYCoordinates'] = [[0, 0]]

        tmp = self.get_param_KJH4('SRF_Thermo_Cnt')
        for i in range(0, len(tmp)):
            ## Calculate
            ## Target_coord: _XY_type1
            ##X
            tmp1_1 = self.get_param_KJH4('BND_Therm_Clk_Vtc_M4')
            target_coord = tmp1_1[i][0]['_XY_up']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_Therm_Clk_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_down']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Therm_Clk_ViaM3M4')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['SRF_Therm_Clk_ViaM3M4']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Thermometer CLK : HrzM3
        ## Pre-defined
        Ywidth = _YWidthOfCLKSrc

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Therm_Clk_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Therm_Clk_Hrz_M3']['_YWidth'] = Ywidth

        ## Define Boundary_element _XWidth BND_Therm_Clk_Vtc_M4
        tmp = self.get_param_KJH4('BND_Therm_Clk_Vtc_M4')
        self._DesignParameter['BND_Therm_Clk_Hrz_M3']['_XWidth'] = abs(
            tmp[-1][0]['_XY_right'][0] - tmp[0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Therm_Clk_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Therm_Clk_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        ##X
        tmp1_1 = self.get_param_KJH4('BND_Therm_Clk_Vtc_M4')
        target_coord = tmp1_1[0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Therm_Clk_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Therm_Clk_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Therm_Clk_Hrz_M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ThermDACCtrl_Rst(CLK_Samp)
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ThermDACCtrl_Rst(CLK_Samp) : Vtc M4

        ## Pre-defined
        Ylength1 = _SpaceBtwCLKSrcAndCLKSamp
        Xwidth1 = 50

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_ThermDACCtrl_Rst_Vtc_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_Net12_ViaM1M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        tmp2 = self.get_param_KJH4('BND_Therm_Clk_Hrz_M3')
        self._DesignParameter['BND_ThermDACCtrl_Rst_Vtc_M4']['_YWidth'] = abs(
            tmp1[0][0][0][0][0]['_XY_down'][1] - tmp2[0][0]['_XY_up'][1]) + Ylength1

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_ThermDACCtrl_Rst_Vtc_M4']['_XWidth'] = Xwidth1

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_ThermDACCtrl_Rst_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_ThermDACCtrl_Rst_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

        tmp = self.get_param_KJH4('SRF_Thermo_Cnt')
        for i in range(1, len(tmp)):
            ## Calculate
            ## Target_coord: _XY_type1
            ##X
            tmp1_1 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_Net12_ViaM1M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
            target_coord = tmp1_1[i][0][0][0][0]['_XY_down']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_ThermDACCtrl_Rst_Vtc_M4')
            approaching_coord = tmp2[0][0]['_XY_down']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_ThermDACCtrl_Rst_Vtc_M4')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_ThermDACCtrl_Rst_Vtc_M4']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ThermDACCtrl_Rst(CLK_Samp) : Vtc M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_ThermDACCtrl_Rst_ViaM3M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_ThermDACCtrl_Rst_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_ThermDACCtrl_Rst_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_ThermDACCtrl_Rst_ViaM3M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_ThermDACCtrl_Rst_ViaM3M4']['_DesignObj']._CalculateDesignParameterYmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_ThermDACCtrl_Rst_ViaM3M4']['_XYCoordinates'] = [[0, 0]]

        tmp = self.get_param_KJH4('SRF_Thermo_Cnt')
        for i in range(0, len(tmp) - 1):
            ## Calculate
            ## Target_coord: _XY_type1
            ##X
            tmp1_1 = self.get_param_KJH4('BND_ThermDACCtrl_Rst_Vtc_M4')
            target_coord = tmp1_1[i][0]['_XY_up']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_ThermDACCtrl_Rst_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_down']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_ThermDACCtrl_Rst_ViaM3M4')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['SRF_ThermDACCtrl_Rst_ViaM3M4']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ThermDACCtrl_Rst(CLK_Samp) : Hrz M3
        ## Pre-defined
        Ywidth = _YWidthOfCLKSamp

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_ThermDACCtrl_Rst_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_ThermDACCtrl_Rst_Hrz_M3']['_YWidth'] = Ywidth

        ## Define Boundary_element _XWidth BND_Therm_Clk_Vtc_M4
        tmp = self.get_param_KJH4('BND_ThermDACCtrl_Rst_Vtc_M4')
        self._DesignParameter['BND_ThermDACCtrl_Rst_Hrz_M3']['_XWidth'] = abs(
            tmp[-1][0]['_XY_right'][0] - tmp[0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_ThermDACCtrl_Rst_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_ThermDACCtrl_Rst_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        ##X
        tmp1_1 = self.get_param_KJH4('BND_ThermDACCtrl_Rst_Vtc_M4')
        target_coord = tmp1_1[0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_ThermDACCtrl_Rst_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_ThermDACCtrl_Rst_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_ThermDACCtrl_Rst_Hrz_M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ThermDACCtrl_Rst(CLK_Samp) : Therm Cnt[0] Set Vtc M4
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Therm0_Set_Vtc_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_Net8_ViaM1M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        tmp2 = self.get_param_KJH4('BND_ThermDACCtrl_Rst_Vtc_M4')
        self._DesignParameter['BND_Therm0_Set_Vtc_M4']['_YWidth'] = abs(
            tmp1[0][0][0][0][0]['_XY_up'][1] - tmp2[0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('BND_ThermDACCtrl_Rst_Vtc_M4')
        self._DesignParameter['BND_Therm0_Set_Vtc_M4']['_XWidth'] = tmp[0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Therm0_Set_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        ##X
        tmp1_1 = self.get_param_KJH4('SRF_Thermo_Cnt', 'SRF_Net8_ViaM1M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        target_coord = tmp1_1[0][0][0][0][0]['_XY_up']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Therm0_Set_Vtc_M4')
        approaching_coord = tmp2[0][0]['_XY_down']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Therm0_Set_Vtc_M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Therm0_Set_Vtc_M4']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ThermDACCtrl_Rst(CLK_Samp) : Therm Cnt[0] Set Vtc M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_Therm0_Set_ViaM3M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_Therm0_Set_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_Therm0_Set_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_Therm0_Set_ViaM3M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Therm0_Set_ViaM3M4']['_DesignObj']._CalculateDesignParameterYmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_Therm0_Set_ViaM3M4']['_XYCoordinates'] = [[0, 0]]

        ## Calculate
        ## Target_coord: _XY_type1
        ##X
        tmp1_1 = self.get_param_KJH4('BND_Therm0_Set_Vtc_M4')
        target_coord = tmp1_1[0][0]['_XY_up']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_Therm0_Set_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Therm0_Set_ViaM3M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['SRF_Therm0_Set_ViaM3M4']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ThermDACCtrl_Rst(CLK_Samp) : Therm Cnt[0] Set Vtc M4
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Therm0_Set_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('BND_ThermDACCtrl_Rst_Hrz_M3')
        self._DesignParameter['BND_Therm0_Set_Hrz_M3']['_YWidth'] = tmp[0][0]['_Ywidth']

        ## Define Boundary_element _XWidth BND_Therm_Clk_Vtc_M4
        tmp1 = self.get_param_KJH4('BND_ThermDACCtrl_Rst_Hrz_M3')
        tmp2 = self.get_param_KJH4('BND_Therm0_Set_Vtc_M4')
        self._DesignParameter['BND_Therm0_Set_Hrz_M3']['_XWidth'] = abs(
            tmp1[0][0]['_XY_left'][0] - tmp2[0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Therm0_Set_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Therm0_Set_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        ##X
        tmp1_1 = self.get_param_KJH4('BND_ThermDACCtrl_Rst_Hrz_M3')
        target_coord = tmp1_1[0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Therm0_Set_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_down_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Therm0_Set_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Therm0_Set_Hrz_M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Dout Sampler Gen.
        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Dout_Samp'] = self._SrefElementDeclaration(
            _DesignObj=D04_01_SetRstDFF_Nor_Routing_KJH1._SetRstDFF_Nor_Routing(_DesignParameter=None,
                                                                                _Name='{}:SRF_Dout_Samp'.format(
                                                                                    _Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Dout_Samp']['_Reflect'] = [1, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Dout_Samp']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Dout_Samp']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters1)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Dout_Samp']['_XYCoordinates'] = [[0, 0]]

        ## Get_Scoord_v4.
        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_DAC_Ctrl', 'BND_Pbody_M1Exten')
        target_coord = tmp1[1][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_Dout_Samp', 'BND_Pbody_M1Exten')
        approaching_coord = tmp2[0][0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Dout_Samp')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define Coordinates
        self._DesignParameter['SRF_Dout_Samp']['_XYCoordinates'] = tmpXY

        ## Get_Scoord_v4.
        ## Calculate Sref XYcoord
        tmpXY = self._DesignParameter['SRF_Dout_Samp']['_XYCoordinates']
        for i in range(0, _NumofBit - 1):
            ## Calculate
            ## Target_coord: _XY_type1
            ##X
            tmp1_1 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'SRF_NMOS',
                                         'BND_PODummyLayer')
            tmp1_2 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'SRF_PMOS',
                                         'BND_PODummyLayer')
            if tmp1_1[i][0][0][0][-1][0]['_XY_right'][0] > tmp1_2[i][0][0][0][-1][0]['_XY_right'][0]:
                target_coordx = tmp1_1[i][0][0][0][-1][0]['_XY_right'][0]
            else:
                target_coordx = tmp1_2[i][0][0][0][-1][0]['_XY_right'][0]
                ##Y
            tmp1_3 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'SRF_PMOS',
                                         'BND_{}Layer'.format(_Slv_Inv3_PMOS_XVT))
            target_coordy = tmp1_3[i][0][0][0][0][0]['_XY_down'][1]

            target_coord = [target_coordx, target_coordy]
            ## Approaching_coord: _XY_type2
            ##X
            tmp2_1 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_NMOS',
                                         'BND_PODummyLayer')
            tmp2_2 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_PMOS',
                                         'BND_PODummyLayer')
            if tmp2_1[0][0][0][0][0][0]['_XY_right'][0] > tmp2_2[0][0][0][0][0][0]['_XY_right'][0]:
                approaching_coordx = tmp2_1[0][0][0][0][0][0]['_XY_left'][0]
            else:
                approaching_coordx = tmp2_2[0][0][0][0][0][0]['_XY_left'][0]
                ##Y
            tmp2_3 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_PMOS',
                                         'BND_{}Layer'.format(_Mst_Xgate1_PMOS_XVT))
            approaching_coordy = tmp2_3[0][0][0][0][0][0]['_XY_down'][1]
            approaching_coord = [approaching_coordx, approaching_coordy]
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Dout_Samp')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[0] = New_Scoord[0] + _Test_distance
            tmpXY.append(New_Scoord)

            ## Define Coordinates
            self._DesignParameter['SRF_Dout_Samp']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Body Cover2(Dout_Samp) : NBody
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Body Cover2(Dout_Samp): NBody: M1 Exten
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Nbody2_M1Exten'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_Nbody',
                                   'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        self._DesignParameter['BND_Nbody2_M1Exten']['_YWidth'] = tmp1[0][0][0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_Nbody',
                                   'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'SRF_Nbody',
                                   'SRF_NbodyContactPhyLen', 'BND_Met1Layer')

        self._DesignParameter['BND_Nbody2_M1Exten']['_XWidth'] = abs(
            tmp2[-1][0][0][0][0][0][0]['_XY_right'][0] - tmp1[0][0][0][0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Nbody2_M1Exten']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Nbody2_M1Exten']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_Nbody',
                                   'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        target_coord = tmp1[0][0][0][0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Nbody2_M1Exten')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Nbody2_M1Exten')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Nbody2_M1Exten']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Body Cover2(Dout_Samp): NBody: RX Exten
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Nbody2_RXExten'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0],
            _Datatype=DesignParameters._LayerMapping['DIFF'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_Nbody',
                                   'SRF_NbodyContactPhyLen', 'BND_ODLayer')
        self._DesignParameter['BND_Nbody2_RXExten']['_YWidth'] = tmp1[0][0][0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_Nbody',
                                   'SRF_NbodyContactPhyLen', 'BND_ODLayer')
        tmp2 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'SRF_Nbody',
                                   'SRF_NbodyContactPhyLen', 'BND_ODLayer')

        self._DesignParameter['BND_Nbody2_RXExten']['_XWidth'] = abs(
            tmp2[-1][0][0][0][0][0][0]['_XY_right'][0] - tmp1[0][0][0][0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Nbody2_RXExten']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Nbody2_RXExten']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_Nbody',
                                   'SRF_NbodyContactPhyLen', 'BND_ODLayer')
        target_coord = tmp1[0][0][0][0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Nbody2_RXExten')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Nbody2_RXExten')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Nbody2_RXExten']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Body Cover2(Dout_Samp): NBody: Nwell Exten
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Nbody2_NwellExten'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'BND_PMOS_NellExten')
        self._DesignParameter['BND_Nbody2_NwellExten']['_YWidth'] = tmp1[0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'BND_PMOS_NellExten')
        tmp2 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'BND_PMOS_NellExten')

        self._DesignParameter['BND_Nbody2_NwellExten']['_XWidth'] = abs(
            tmp2[-1][0][0][0][0]['_XY_right'][0] - tmp1[0][0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Nbody2_NwellExten']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Nbody2_NwellExten']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'BND_PMOS_NellExten')
        target_coord = tmp1[0][0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Nbody2_NwellExten')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Nbody2_NwellExten')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Nbody2_NwellExten']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## DAC Ctrl QB - Dout_Samp D
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## DAC Ctrl QB - Dout_Samp D : M2 Hrz
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_DACCtrl_QB_DoutSamp_D_Hrz_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_DACCtrl_QB_DoutSamp_D_Hrz_M2']['_YWidth'] = _Routing_width

        ## Define Boundary_element _XWidth
        tmp1_1 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'BND_Out_Vtc_M2')
        tmp1_2 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_NMOS',
                                     'BND_PODummyLayer')
        tmp1_3 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'SRF_PMOS',
                                     'BND_PODummyLayer')
        tmp1_4 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'SRF_NMOS',
                                     'BND_PODummyLayer')
        tmp1_5 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'SRF_PMOS',
                                     'BND_PODummyLayer')

        if tmp1_2[1][0][0][0][0][0]['_XY_left'][0] > tmp1_3[1][0][0][0][0][0]['_XY_left'][0]:
            tmp_left = tmp1_3[1][0][0][0][0][0]['_XY_left'][0]
        else:
            tmp_left = tmp1_2[1][0][0][0][0][0]['_XY_left'][0]

        if tmp1_4[0][0][0][0][-1][0]['_XY_right'][0] > tmp1_5[0][0][0][0][-1][0]['_XY_right'][0]:
            tmp_right = tmp1_4[0][0][0][0][-1][0]['_XY_right'][0]
        else:
            tmp_right = tmp1_5[0][0][0][0][-1][0]['_XY_right'][0]

        self._DesignParameter['BND_DACCtrl_QB_DoutSamp_D_Hrz_M2']['_XWidth'] = abs(
            np.round(0.5 * (tmp_left + tmp_right)) - tmp1_1[0][0][0][0][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_DACCtrl_QB_DoutSamp_D_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_DACCtrl_QB_DoutSamp_D_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
        for i in range(0, _NumofBit):
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'BND_Out_Vtc_M2')
            target_coord = tmp1[i][0][0][0][0]['_XY_right']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_DACCtrl_QB_DoutSamp_D_Hrz_M2')
            approaching_coord = tmp2[0][0]['_XY_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_DACCtrl_QB_DoutSamp_D_Hrz_M2')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_DACCtrl_QB_DoutSamp_D_Hrz_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## DAC Ctrl QB - Dout_Samp D : ViaM2M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_DACCtrl_QB_DoutSamp_D_ViaM2M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_DACCtrl_QB_DoutSamp_D_ViaM2M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_DACCtrl_QB_DoutSamp_D_ViaM2M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_DACCtrl_QB_DoutSamp_D_ViaM2M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_DACCtrl_QB_DoutSamp_D_ViaM2M4']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_DACCtrl_QB_DoutSamp_D_ViaM2M4']['_XYCoordinates'] = [[0, 0]]
        for i in range(0, _NumofBit):
            ## Calculate
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_DACCtrl_QB_DoutSamp_D_Hrz_M2')
            target_coord = tmp1[i][0]['_XY_up_right']
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_DACCtrl_QB_DoutSamp_D_ViaM2M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_up']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_DACCtrl_QB_DoutSamp_D_ViaM2M4')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define
        self._DesignParameter['SRF_DACCtrl_QB_DoutSamp_D_ViaM2M4']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## DAC Ctrl QB - Dout_Samp D : VtcM4
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['SRF_DACCtrl_QB_DoutSamp_D_Vtc_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_SetRst_Placement', 'SRF_Slv_Inv3', 'BND_Out_Vtc_M2')
        tmp2 = self.get_param_KJH4('SRF_DACCtrl_QB_DoutSamp_D_ViaM2M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        self._DesignParameter['SRF_DACCtrl_QB_DoutSamp_D_Vtc_M4']['_YWidth'] = (
                    tmp2[0][0][0][0]['_XY_up'][1] - tmp1[0][0][0][0][0]['_XY_right'][1])

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_DACCtrl_QB_DoutSamp_D_ViaM2M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        self._DesignParameter['SRF_DACCtrl_QB_DoutSamp_D_Vtc_M4']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['SRF_DACCtrl_QB_DoutSamp_D_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_DACCtrl_QB_DoutSamp_D_Vtc_M4']['_XYCoordinates'] = [[0, 0]]
        for i in range(0, _NumofBit):
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_DACCtrl_QB_DoutSamp_D_ViaM2M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
            target_coord = tmp1[i][0][0][0]['_XY_up']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_DACCtrl_QB_DoutSamp_D_Vtc_M4')
            approaching_coord = tmp2[0][0]['_XY_up']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_DACCtrl_QB_DoutSamp_D_Vtc_M4')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['SRF_DACCtrl_QB_DoutSamp_D_Vtc_M4']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## DAC Ctrl QB - Dout_Samp D : ViaM2M4_2
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_DACCtrl_QB_DoutSamp_D_ViaM2M4_2'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_DACCtrl_QB_DoutSamp_D_ViaM2M4_2'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_DACCtrl_QB_DoutSamp_D_ViaM2M4_2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_DACCtrl_QB_DoutSamp_D_ViaM2M4_2']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_DACCtrl_QB_DoutSamp_D_ViaM2M4_2']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_DACCtrl_QB_DoutSamp_D_ViaM2M4_2']['_XYCoordinates'] = [[0, 0]]
        for i in range(0, _NumofBit):
            ## Calculate
            ## Target_coord
            tmp1 = self.get_param_KJH4('SRF_DACCtrl_QB_DoutSamp_D_Vtc_M4')
            target_coord = tmp1[i][0]['_XY_down']
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_DACCtrl_QB_DoutSamp_D_ViaM2M4_2', 'SRF_ViaM3M4', 'BND_Met4Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_down']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_DACCtrl_QB_DoutSamp_D_ViaM2M4_2')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define
        self._DesignParameter['SRF_DACCtrl_QB_DoutSamp_D_ViaM2M4_2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## DAC Ctrl QB - Dout_Samp D : HrzM2
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['SRF_DACCtrl_QB_DoutSamp_D_Hrz_M2_2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['SRF_DACCtrl_QB_DoutSamp_D_Hrz_M2_2']['_YWidth'] = _Routing_width

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_DACCtrl_QB_DoutSamp_D_ViaM2M4_2', 'SRF_ViaM2M3', 'BND_Met2Layer')
        tmp2 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'BND_Input_Vtc_M2')
        self._DesignParameter['SRF_DACCtrl_QB_DoutSamp_D_Hrz_M2_2']['_XWidth'] = abs(
            tmp2[0][0][0][0][0]['_XY_right'][0] - tmp1[0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['SRF_DACCtrl_QB_DoutSamp_D_Hrz_M2_2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_DACCtrl_QB_DoutSamp_D_Hrz_M2_2']['_XYCoordinates'] = [[0, 0]]
        for i in range(0, _NumofBit):
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_DACCtrl_QB_DoutSamp_D_ViaM2M4_2', 'SRF_ViaM2M3', 'BND_Met2Layer')
            target_coord = tmp1[i][0][0][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_DACCtrl_QB_DoutSamp_D_Hrz_M2_2')
            approaching_coord = tmp2[0][0]['_XY_down_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_DACCtrl_QB_DoutSamp_D_Hrz_M2_2')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['SRF_DACCtrl_QB_DoutSamp_D_Hrz_M2_2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## SRF_Dout_Samp [0]~[-1] : Set--VSS
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## SRF_Dout_Samp [0]~[-1] : Set--VSS : M1 Hrz
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Dout_Samp_Set_Hrz_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Dout_Samp_Set_Hrz_M1']['_YWidth'] = _Routing_width

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_SetRst_Placement', 'SRF_Mst_Inv1', 'SRF_NMOS',
                                   'BND_Gate_Hrz_Mx')
        tmp2 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_Net8_ViaM1M4', 'SRF_ViaM1M2', 'BND_Met2Layer')

        self._DesignParameter['BND_Dout_Samp_Set_Hrz_M1']['_XWidth'] = abs(
            tmp2[0][0][0][0][0]['_XY_cent'][0] - tmp1[0][0][0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Dout_Samp_Set_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Dout_Samp_Set_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
        for i in range(0, _NumofBit):
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_SetRst_Placement', 'SRF_Mst_Inv1', 'SRF_NMOS',
                                       'BND_Gate_Hrz_Mx')
            target_coord = tmp1[i][0][0][0][0][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Dout_Samp_Set_Hrz_M1')
            approaching_coord = tmp2[0][0]['_XY_up_right']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Dout_Samp_Set_Hrz_M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_Dout_Samp_Set_Hrz_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## SRF_Dout_Samp [0]~[-1] : Set--VSS : M1 Vtc
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Dout_Samp_Set_Vtc_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_Dout_Samp_Set_Hrz_M1')
        tmp2 = self.get_param_KJH4('SRF_Dout_Samp', 'BND_Pbody_M1Exten')
        self._DesignParameter['BND_Dout_Samp_Set_Vtc_M1']['_YWidth'] = abs(
            tmp1[0][0]['_XY_down'][1] - tmp2[0][0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Dout_Samp_Set_Vtc_M1']['_XWidth'] = _Routing_width

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Dout_Samp_Set_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Dout_Samp_Set_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
        for i in range(0, _NumofBit):
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('BND_Dout_Samp_Set_Hrz_M1')
            target_coord = tmp1[i][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Dout_Samp_Set_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_down']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Dout_Samp_Set_Vtc_M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_Dout_Samp_Set_Vtc_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## SRF_Dout_Samp [0]~[-1] : RST--VSS
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## SRF_Dout_Samp [0]~[-1] : Rst--VSS : M1 Hrz
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Dout_Samp_Rst_Hrz_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Dout_Samp_Rst_Hrz_M1']['_YWidth'] = _Routing_width

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_SetRst_Placement', 'SRF_Slv_Inv1', 'SRF_NMOS',
                                   'BND_Gate_Hrz_Mx')
        tmp2 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_Net12_ViaM1M4', 'SRF_ViaM1M2', 'BND_Met2Layer')

        self._DesignParameter['BND_Dout_Samp_Rst_Hrz_M1']['_XWidth'] = abs(
            tmp2[0][0][0][0][0]['_XY_cent'][0] - tmp1[0][0][0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Dout_Samp_Rst_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Dout_Samp_Rst_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
        for i in range(0, _NumofBit):
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_SetRst_Placement', 'SRF_Slv_Inv1', 'SRF_NMOS',
                                       'BND_Gate_Hrz_Mx')
            target_coord = tmp1[i][0][0][0][0][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Dout_Samp_Rst_Hrz_M1')
            approaching_coord = tmp2[0][0]['_XY_up_right']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Dout_Samp_Rst_Hrz_M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_Dout_Samp_Rst_Hrz_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## SRF_Dout_Samp [0]~[-1] : Rst--VSS : M1 Vtc
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Dout_Samp_Rst_Vtc_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_Dout_Samp_Rst_Hrz_M1')
        tmp2 = self.get_param_KJH4('SRF_Dout_Samp', 'BND_Pbody_M1Exten')
        self._DesignParameter['BND_Dout_Samp_Rst_Vtc_M1']['_YWidth'] = abs(
            tmp1[0][0]['_XY_down'][1] - tmp2[0][0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Dout_Samp_Rst_Vtc_M1']['_XWidth'] = _Routing_width

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Dout_Samp_Rst_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Dout_Samp_Rst_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
        for i in range(0, _NumofBit):
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('BND_Dout_Samp_Rst_Hrz_M1')
            target_coord = tmp1[i][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Dout_Samp_Rst_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_down']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Dout_Samp_Rst_Vtc_M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_Dout_Samp_Rst_Vtc_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## SRF_Dout_Samp [0]~[-1] : Compout
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  SRF_Dout_Samp [0]~[-1] : Compout : ViaM2M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_DACCtrl_D_ViaM2M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_DACCtrl_D_ViaM2M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_DACCtrl_D_ViaM2M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_DACCtrl_D_ViaM2M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_DACCtrl_D_ViaM2M4']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_DACCtrl_D_ViaM2M4']['_XYCoordinates'] = [[0, 0]]
        ## 10/23 수정한 부분 numofbit + 1
        for i in range(0, _NumofBit + 1):
            ## Calculate
            ## Target_coord
            tmp1 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'BND_Input_Vtc_M2')
            target_coord = tmp1[i][0][0][0][0]['_XY_cent']
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_DACCtrl_D_ViaM2M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_DACCtrl_D_ViaM2M4')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define
        self._DesignParameter['SRF_DACCtrl_D_ViaM2M4']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  SRF_Dout_Samp [0]~[-1] : Compout : VtcM4
        ## Pre-defined
        Ylength1 = _SpaceBtwNbody2AndCompOut
        Xwidth1 = 50

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_DACCtrl_D_Vtc_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_DACCtrl_D_ViaM2M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        tmp2 = self.get_param_KJH4('BND_Nbody2_M1Exten')
        self._DesignParameter['BND_DACCtrl_D_Vtc_M4']['_YWidth'] = abs(
            tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0]['_XY_down'][1]) + Ylength1

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_DACCtrl_D_Vtc_M4']['_XWidth'] = Xwidth1

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_DACCtrl_D_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_DACCtrl_D_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

        tmp = self.get_param_KJH4('SRF_DACCtrl_D_ViaM2M4')
        for i in range(0, len(tmp)):
            ## Calculate
            ## Target_coord: _XY_type1
            ##X
            tmp1_1 = self.get_param_KJH4('SRF_DACCtrl_D_ViaM2M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
            target_coord = tmp1_1[i][0][0][0]['_XY_up']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_DACCtrl_D_Vtc_M4')
            approaching_coord = tmp2[0][0]['_XY_up']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_DACCtrl_D_Vtc_M4')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_DACCtrl_D_Vtc_M4']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## SRF_Dout_Samp [0]~[-1] : Compout : ViaM3M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_DACCtrl_D_ViaM3M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_DACCtrl_D_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_DACCtrl_D_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_DACCtrl_D_ViaM3M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_DACCtrl_D_ViaM3M4']['_DesignObj']._CalculateDesignParameterYmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_DACCtrl_D_ViaM3M4']['_XYCoordinates'] = [[0, 0]]

        tmp = self.get_param_KJH4('SRF_DACCtrl_D_ViaM2M4')
        for i in range(0, len(tmp)):
            ## Calculate
            ## Target_coord: _XY_type1
            ##X
            tmp1_1 = self.get_param_KJH4('BND_DACCtrl_D_Vtc_M4')
            target_coord = tmp1_1[i][0]['_XY_down']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_DACCtrl_D_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_up']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_DACCtrl_D_ViaM3M4')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['SRF_DACCtrl_D_ViaM3M4']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## SRF_Dout_Samp [0]~[-1] : Compout : Hrz M3
        ## Pre-defined
        Ywidth = _YWidthOfCompOut

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_DACCtrl_D_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_DACCtrl_D_Hrz_M3']['_YWidth'] = Ywidth

        ## Define Boundary_element _XWidth BND_Therm_Clk_Vtc_M4
        tmp = self.get_param_KJH4('BND_DACCtrl_D_Vtc_M4')
        self._DesignParameter['BND_DACCtrl_D_Hrz_M3']['_XWidth'] = abs(
            tmp[-1][0]['_XY_right'][0] - tmp[0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_DACCtrl_D_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_DACCtrl_D_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        ##X
        tmp1_1 = self.get_param_KJH4('BND_DACCtrl_D_Vtc_M4')
        target_coord = tmp1_1[0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_DACCtrl_D_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_DACCtrl_D_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_DACCtrl_D_Hrz_M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Dout_Samp CLK
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Dout_Samp CLK : Vtc M4

        ## Pre-defined
        Ylength1 = _SpaceBtwCompOutAndCLKDout
        Xwidth1 = 50

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_DoutSamp_Clk_Vtc_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_Net3_ViaM1M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        tmp2 = self.get_param_KJH4('BND_DACCtrl_D_Hrz_M3')
        self._DesignParameter['BND_DoutSamp_Clk_Vtc_M4']['_YWidth'] = abs(
            tmp1[0][0][0][0][0]['_XY_up'][1] - tmp2[0][0]['_XY_down'][1]) + Ylength1

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_DoutSamp_Clk_Vtc_M4']['_XWidth'] = Xwidth1

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_DoutSamp_Clk_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_DoutSamp_Clk_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

        tmp = self.get_param_KJH4('SRF_Dout_Samp')
        for i in range(0, len(tmp)):
            ## Calculate
            ## Target_coord: _XY_type1
            ##X
            tmp1_1 = self.get_param_KJH4('SRF_Dout_Samp', 'SRF_Net3_ViaM1M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
            target_coord = tmp1_1[i][0][0][0][0]['_XY_up']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_DoutSamp_Clk_Vtc_M4')
            approaching_coord = tmp2[0][0]['_XY_up']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_DoutSamp_Clk_Vtc_M4')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_DoutSamp_Clk_Vtc_M4']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Dout_Samp CLK : ViaM3M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_DoutSamp_Clk_ViaM3M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_DoutSamp_Clk_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_DoutSamp_Clk_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_DoutSamp_Clk_ViaM3M4']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_DoutSamp_Clk_ViaM3M4']['_DesignObj']._CalculateDesignParameterYmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_DoutSamp_Clk_ViaM3M4']['_XYCoordinates'] = [[0, 0]]

        tmp = self.get_param_KJH4('SRF_Dout_Samp')
        for i in range(0, len(tmp)):
            ## Calculate
            ## Target_coord: _XY_type1
            ##X
            tmp1_1 = self.get_param_KJH4('BND_DoutSamp_Clk_Vtc_M4')
            target_coord = tmp1_1[i][0]['_XY_down']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_DoutSamp_Clk_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_up']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_DoutSamp_Clk_ViaM3M4')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['SRF_DoutSamp_Clk_ViaM3M4']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Dout_Samp CLK : Hrz M3
        ## Pre-defined
        Ywidth = _YWidthOfCLKDout

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_DoutSamp_Clk_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_DoutSamp_Clk_Hrz_M3']['_YWidth'] = Ywidth

        ## Define Boundary_element _XWidth BND_Therm_Clk_Vtc_M4
        tmp = self.get_param_KJH4('BND_DoutSamp_Clk_Vtc_M4')
        self._DesignParameter['BND_DoutSamp_Clk_Hrz_M3']['_XWidth'] = abs(
            tmp[-1][0]['_XY_right'][0] - tmp[0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_DoutSamp_Clk_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_DoutSamp_Clk_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        ##X
        tmp1_1 = self.get_param_KJH4('BND_DoutSamp_Clk_Vtc_M4')
        target_coord = tmp1_1[0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_DoutSamp_Clk_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_DoutSamp_Clk_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_DoutSamp_Clk_Hrz_M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## DACCtrl[-1] CLK -- VSS
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_DACCtrlend_Clk_Vtc_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_Net7_ViaM1M3_1', 'SRF_ViaM1M2', 'BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_DAC_Ctrl', 'BND_Pbody_M1Exten')
        self._DesignParameter['BND_DACCtrlend_Clk_Vtc_M1']['_YWidth'] = abs(
            tmp1[0][0][0][0][0]['_XY_up'][1] - tmp2[0][0][0]['_XY_down'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_DACCtrlend_Clk_Vtc_M1']['_XWidth'] = 50

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_DACCtrlend_Clk_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_DACCtrlend_Clk_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate
        ## Target_coord: _XY_type1
        ##X
        tmp1_1 = self.get_param_KJH4('SRF_DAC_Ctrl', 'SRF_Net7_ViaM1M3_1', 'SRF_ViaM1M2', 'BND_Met1Layer')
        target_coord = tmp1_1[-1][0][0][0][0]['_XY_up']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_DACCtrlend_Clk_Vtc_M1')
        approaching_coord = tmp2[0][0]['_XY_up']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_DACCtrlend_Clk_Vtc_M1')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_DACCtrlend_Clk_Vtc_M1']['_XYCoordinates'] = tmpXY

        '''



        '''
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
    libname = 'Proj_ADC_K00_SARLogicWtBuffers'
    ## CellName: ex)C01_cap_array_v2_84l
    cellname = 'K00_00_SARLogic'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        _NumofBit=3,

        _Test_distance=330,
        _Routing_width=50,
        _Routing_distance=80,

        _SpaceBtwPbodyAndCLKSrc=100,
        _YWidthOfCLKSrc=100,
        _SpaceBtwCLKSrcAndCLKSamp=100,
        _YWidthOfCLKSamp=100,
        _SpaceBtwNbody2AndCompOut=100,
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
        _Mst_Xgate1_NMOS_XVT='SLVT',
        _Mst_Xgate1_NMOS_POGate_Comb_length=100,

        ## Xgate PMOS
        _Mst_Xgate1_PMOS_NumberofGate=1,  # 1
        _Mst_Xgate1_PMOS_ChannelWidth=400,  # 200
        _Mst_Xgate1_PMOS_ChannelLength=30,
        _Mst_Xgate1_PMOS_XVT='SLVT',
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
        _Mst_Xgate2_PMOS_NumberofGate=1,  # 2
        _Mst_Xgate2_PMOS_ChannelWidth=400,
        _Mst_Xgate2_PMOS_ChannelLength=30,
        _Mst_Xgate2_PMOS_XVT='SLVT',
        _Mst_Xgate2_PMOS_POGate_Comb_length=100,

        ## Master Nor1
        ## Nor1 common

        ## NMOS
        ## NMOS common
        _Mst_Nor1_NMOS_XVT='SLVT',

        ## NMOSA
        _Mst_Nor1_NMOSA_NumberofGate=2,
        _Mst_Nor1_NMOSA_ChannelWidth=400,
        _Mst_Nor1_NMOSA_ChannelLength=30,
        _Mst_Nor1_NMOSA_POGate_Comb_length=100,

        ## NMOSB
        _Mst_Nor1_NMOSB_NumberofGate=2,
        _Mst_Nor1_NMOSB_ChannelWidth=400,
        _Mst_Nor1_NMOSB_ChannelLength=30,
        _Mst_Nor1_NMOSB_POGate_Comb_length=100,

        ## PMOS
        ## PMOS common
        _Mst_Nor1_PMOS_XVT='SLVT',

        ## PMOSA
        _Mst_Nor1_PMOSA_NumberofGate=4,
        _Mst_Nor1_PMOSA_ChannelWidth=800,
        _Mst_Nor1_PMOSA_ChannelLength=30,
        _Mst_Nor1_PMOSA_POGate_Comb_length=100,

        ## PMOSB
        _Mst_Nor1_PMOSB_NumberofGate=4,
        _Mst_Nor1_PMOSB_ChannelWidth=800,
        _Mst_Nor1_PMOSB_ChannelLength=30,
        _Mst_Nor1_PMOSB_POGate_Comb_length=100,

        ## Master Nor2
        ## Nor2 common

        ## NMOS
        ## NMOS common
        _Mst_Nor2_NMOS_XVT='SLVT',

        ## NMOSA
        _Mst_Nor2_NMOSA_NumberofGate=1,
        _Mst_Nor2_NMOSA_ChannelWidth=100,
        _Mst_Nor2_NMOSA_ChannelLength=30,
        _Mst_Nor2_NMOSA_POGate_Comb_length=100,

        ## NMOSB
        _Mst_Nor2_NMOSB_NumberofGate=1,
        _Mst_Nor2_NMOSB_ChannelWidth=100,
        _Mst_Nor2_NMOSB_ChannelLength=30,
        _Mst_Nor2_NMOSB_POGate_Comb_length=100,

        ## PMOS
        ## PMOS common
        _Mst_Nor2_PMOS_XVT='SLVT',

        ## PMOSA
        _Mst_Nor2_PMOSA_NumberofGate=2,
        _Mst_Nor2_PMOSA_ChannelWidth=200,
        _Mst_Nor2_PMOSA_ChannelLength=30,
        _Mst_Nor2_PMOSA_POGate_Comb_length=100,

        ## PMOSB
        _Mst_Nor2_PMOSB_NumberofGate=2,
        _Mst_Nor2_PMOSB_ChannelWidth=200,
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
        _Mst_Inv2_NMOS_ChannelWidth=400,
        _Mst_Inv2_NMOS_ChannelLength=30,
        _Mst_Inv2_NMOS_XVT='SLVT',
        _Mst_Inv2_NMOS_POGate_Comb_length=100,

        ## Inv2 PMOS
        _Mst_Inv2_PMOS_NumberofGate=1,
        _Mst_Inv2_PMOS_ChannelWidth=800,
        _Mst_Inv2_PMOS_ChannelLength=30,
        _Mst_Inv2_PMOS_XVT='SLVT',
        _Mst_Inv2_PMOS_POGate_Comb_length=100,

        ## Master Inv3 : Clock driver
        ## Inv3 common

        ## Inv3 NMOS
        _Mst_Inv3_NMOS_NumberofGate=1,
        _Mst_Inv3_NMOS_ChannelWidth=400,
        _Mst_Inv3_NMOS_ChannelLength=30,
        _Mst_Inv3_NMOS_XVT='SLVT',
        _Mst_Inv3_NMOS_POGate_Comb_length=100,

        ## Inv3 PMOS
        _Mst_Inv3_PMOS_NumberofGate=1,
        _Mst_Inv3_PMOS_ChannelWidth=800,
        _Mst_Inv3_PMOS_ChannelLength=30,
        _Mst_Inv3_PMOS_XVT='SLVT',
        _Mst_Inv3_PMOS_POGate_Comb_length=100,

        ## Slave Xgate1
        ## Xgate common

        ## Xgate NMOS
        _Slv_Xgate1_NMOS_NumberofGate=1,
        _Slv_Xgate1_NMOS_ChannelWidth=400,
        _Slv_Xgate1_NMOS_ChannelLength=30,
        _Slv_Xgate1_NMOS_XVT='SLVT',
        _Slv_Xgate1_NMOS_POGate_Comb_length=100,

        ## Xgate NMOS
        _Slv_Xgate1_PMOS_NumberofGate=1,
        _Slv_Xgate1_PMOS_ChannelWidth=800,
        _Slv_Xgate1_PMOS_ChannelLength=30,
        _Slv_Xgate1_PMOS_XVT='SLVT',
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
        _Slv_Xgate2_PMOS_NumberofGate=1,
        _Slv_Xgate2_PMOS_ChannelWidth=400,
        _Slv_Xgate2_PMOS_ChannelLength=30,
        _Slv_Xgate2_PMOS_XVT='SLVT',
        _Slv_Xgate2_PMOS_POGate_Comb_length=100,

        ## Slave Nor1
        ## Nor1 common

        ## NMOS
        ## NMOS common
        _Slv_Nor1_NMOS_XVT='SLVT',

        ## NMOSA
        _Slv_Nor1_NMOSA_NumberofGate=3,
        _Slv_Nor1_NMOSA_ChannelWidth=400,
        _Slv_Nor1_NMOSA_ChannelLength=30,
        _Slv_Nor1_NMOSA_POGate_Comb_length=100,

        ## NMOSB
        _Slv_Nor1_NMOSB_NumberofGate=3,
        _Slv_Nor1_NMOSB_ChannelWidth=400,
        _Slv_Nor1_NMOSB_ChannelLength=30,
        _Slv_Nor1_NMOSB_POGate_Comb_length=100,

        ## PMOS
        ## PMOS common
        _Slv_Nor1_PMOS_XVT='SLVT',

        ## PMOSA
        _Slv_Nor1_PMOSA_NumberofGate=6,
        _Slv_Nor1_PMOSA_ChannelWidth=800,
        _Slv_Nor1_PMOSA_ChannelLength=30,
        _Slv_Nor1_PMOSA_POGate_Comb_length=100,

        ## PMOSB
        _Slv_Nor1_PMOSB_NumberofGate=6,
        _Slv_Nor1_PMOSB_ChannelWidth=800,
        _Slv_Nor1_PMOSB_ChannelLength=30,
        _Slv_Nor1_PMOSB_POGate_Comb_length=100,

        ## Slave Nor2
        ## Nor2 common

        ## NMOS
        ## NMOS common
        _Slv_Nor2_NMOS_XVT='SLVT',

        ## NMOSA
        _Slv_Nor2_NMOSA_NumberofGate=1,
        _Slv_Nor2_NMOSA_ChannelWidth=100,
        _Slv_Nor2_NMOSA_ChannelLength=30,
        _Slv_Nor2_NMOSA_POGate_Comb_length=100,

        ## NMOSB
        _Slv_Nor2_NMOSB_NumberofGate=1,
        _Slv_Nor2_NMOSB_ChannelWidth=100,
        _Slv_Nor2_NMOSB_ChannelLength=30,
        _Slv_Nor2_NMOSB_POGate_Comb_length=100,

        ## PMOS
        ## PMOS common
        _Slv_Nor2_PMOS_XVT='SLVT',

        ## PMOSA
        _Slv_Nor2_PMOSA_NumberofGate=2,
        _Slv_Nor2_PMOSA_ChannelWidth=200,
        _Slv_Nor2_PMOSA_ChannelLength=30,
        _Slv_Nor2_PMOSA_POGate_Comb_length=100,

        ## PMOSB
        _Slv_Nor2_PMOSB_NumberofGate=2,
        _Slv_Nor2_PMOSB_ChannelWidth=200,
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
        _Slv_Inv2_NMOS_ChannelWidth=400,
        _Slv_Inv2_NMOS_ChannelLength=30,
        _Slv_Inv2_NMOS_XVT='SLVT',
        _Slv_Inv2_NMOS_POGate_Comb_length=100,

        ## Inv2 PMOS
        _Slv_Inv2_PMOS_NumberofGate=1,
        _Slv_Inv2_PMOS_ChannelWidth=800,
        _Slv_Inv2_PMOS_ChannelLength=30,
        _Slv_Inv2_PMOS_XVT='SLVT',
        _Slv_Inv2_PMOS_POGate_Comb_length=100,

        ## Slave Inv3 : Qb driver
        ## Inv3 common

        ## Inv3 NMOS
        _Slv_Inv3_NMOS_NumberofGate=1,  # 1
        _Slv_Inv3_NMOS_ChannelWidth=200,
        _Slv_Inv3_NMOS_ChannelLength=30,
        _Slv_Inv3_NMOS_XVT='SLVT',
        _Slv_Inv3_NMOS_POGate_Comb_length=100,

        ## Inv3 PMOS
        _Slv_Inv3_PMOS_NumberofGate=1,  # 1
        _Slv_Inv3_PMOS_ChannelWidth=400,
        _Slv_Inv3_PMOS_ChannelLength=30,
        _Slv_Inv3_PMOS_XVT='SLVT',
        _Slv_Inv3_PMOS_POGate_Comb_length=100,

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
    LayoutObj = _SARLogic(_DesignParameter=None, _Name=cellname)
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
