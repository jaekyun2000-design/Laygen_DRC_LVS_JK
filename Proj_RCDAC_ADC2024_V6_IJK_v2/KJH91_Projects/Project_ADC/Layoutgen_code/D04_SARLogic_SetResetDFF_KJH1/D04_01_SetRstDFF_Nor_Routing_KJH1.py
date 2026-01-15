
## Import Basic Modules
    ## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_ADC.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

    ## Library
import copy
import math
import numpy as np
import time

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A08_PbodyContactPhyLen_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A07_NbodyContactPhyLen_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.D04_SARLogic_SetResetDFF_KJH1 import D04_00_SetRstDFF_Nor_Placement_KJH0


## Define Class
class _SetRstDFF_Nor_Routing(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(

        _Test_distance = 500,
        _Routing_width =  50,
        _Routing_distance = 100,

    ## DFF Common
        _DFF_Pbody_NumCont      = 2, # number
        _DFF_Nbody_NumCont      = 2, # number
        _DFF_PMOSXvt2NMOSXvt    = 500, # number
        _DFF_XvtTop2Pbody       = None, # number/None(Minimum)
        _DFF_Xvtdown2Nbody      = None, # number/None(Minimum)

    ## Master Xgate1
        ## Xgate common

        ## Xgate NMOS
        _Mst_Xgate1_NMOS_NumberofGate           = 1,
        _Mst_Xgate1_NMOS_ChannelWidth           = 300,
        _Mst_Xgate1_NMOS_ChannelLength          = 30,
        _Mst_Xgate1_NMOS_XVT                    = 'SLVT',
        _Mst_Xgate1_NMOS_POGate_Comb_length     = 100,

        ## Xgate NMOS
        _Mst_Xgate1_PMOS_NumberofGate           = 3,
        _Mst_Xgate1_PMOS_ChannelWidth           = 500,
        _Mst_Xgate1_PMOS_ChannelLength          = 30,
        _Mst_Xgate1_PMOS_XVT                    = 'SLVT',
        _Mst_Xgate1_PMOS_POGate_Comb_length     = 100,

    ## Master Xgate2
        ## Xgate common

        ## Xgate NMOS
        _Mst_Xgate2_NMOS_NumberofGate           = 2,
        _Mst_Xgate2_NMOS_ChannelWidth           = 800,
        _Mst_Xgate2_NMOS_ChannelLength          = 30,
        _Mst_Xgate2_NMOS_XVT                    = 'SLVT',
        _Mst_Xgate2_NMOS_POGate_Comb_length     = 100,

        ## Xgate NMOS
        _Mst_Xgate2_PMOS_NumberofGate           = 3,
        _Mst_Xgate2_PMOS_ChannelWidth           = 200,
        _Mst_Xgate2_PMOS_ChannelLength          = 30,
        _Mst_Xgate2_PMOS_XVT                    = 'SLVT',
        _Mst_Xgate2_PMOS_POGate_Comb_length     = 100,


    ## Master Nor1
        ## Nor1 common

        ## NMOS
            ## NMOS common
        _Mst_Nor1_NMOS_XVT='SLVT',

            ## NMOSA
        _Mst_Nor1_NMOSA_NumberofGate           = 2,
        _Mst_Nor1_NMOSA_ChannelWidth           = 800,
        _Mst_Nor1_NMOSA_ChannelLength          = 30,
        _Mst_Nor1_NMOSA_POGate_Comb_length     = 100,

            ## NMOSB
        _Mst_Nor1_NMOSB_NumberofGate           = 3,
        _Mst_Nor1_NMOSB_ChannelWidth           = 200,
        _Mst_Nor1_NMOSB_ChannelLength          = 30,
        _Mst_Nor1_NMOSB_POGate_Comb_length     = 100,

        ## PMOS
            ## PMOS common
        _Mst_Nor1_PMOS_XVT='SLVT',

            ## PMOSA
        _Mst_Nor1_PMOSA_NumberofGate            = 2,
        _Mst_Nor1_PMOSA_ChannelWidth            = 800,
        _Mst_Nor1_PMOSA_ChannelLength           = 30,
        _Mst_Nor1_PMOSA_POGate_Comb_length      = 100,

            ## PMOSB
        _Mst_Nor1_PMOSB_NumberofGate            = 3,
        _Mst_Nor1_PMOSB_ChannelWidth            = 200,
        _Mst_Nor1_PMOSB_ChannelLength           = 30,
        _Mst_Nor1_PMOSB_POGate_Comb_length      = 100,

    ## Master Nor2
        ## Nor2 common

        ## NMOS
            ## NMOS common
        _Mst_Nor2_NMOS_XVT='SLVT',

            ## NMOSA
        _Mst_Nor2_NMOSA_NumberofGate           = 2,
        _Mst_Nor2_NMOSA_ChannelWidth           = 800,
        _Mst_Nor2_NMOSA_ChannelLength          = 30,
        _Mst_Nor2_NMOSA_POGate_Comb_length     = 100,

            ## NMOSB
        _Mst_Nor2_NMOSB_NumberofGate           = 3,
        _Mst_Nor2_NMOSB_ChannelWidth           = 200,
        _Mst_Nor2_NMOSB_ChannelLength          = 30,
        _Mst_Nor2_NMOSB_POGate_Comb_length     = 100,

        ## PMOS
            ## PMOS common
        _Mst_Nor2_PMOS_XVT='SLVT',

            ## PMOSA
        _Mst_Nor2_PMOSA_NumberofGate            = 2,
        _Mst_Nor2_PMOSA_ChannelWidth            = 800,
        _Mst_Nor2_PMOSA_ChannelLength           = 30,
        _Mst_Nor2_PMOSA_POGate_Comb_length      = 100,

            ## PMOSB
        _Mst_Nor2_PMOSB_NumberofGate            = 3,
        _Mst_Nor2_PMOSB_ChannelWidth            = 200,
        _Mst_Nor2_PMOSB_ChannelLength           = 30,
        _Mst_Nor2_PMOSB_POGate_Comb_length      = 100,

    ## Master Inv1
        ## Inv1 common

        ## Inv1 NMOS
        _Mst_Inv1_NMOS_NumberofGate           = 1,
        _Mst_Inv1_NMOS_ChannelWidth           = 300,
        _Mst_Inv1_NMOS_ChannelLength          = 30,
        _Mst_Inv1_NMOS_XVT                    = 'SLVT',
        _Mst_Inv1_NMOS_POGate_Comb_length     = 100,

        ## Inv1 PMOS
        _Mst_Inv1_PMOS_NumberofGate           = 3,
        _Mst_Inv1_PMOS_ChannelWidth           = 500,
        _Mst_Inv1_PMOS_ChannelLength          = 30,
        _Mst_Inv1_PMOS_XVT                    = 'SLVT',
        _Mst_Inv1_PMOS_POGate_Comb_length     = 100,

    ## Master Inv2 : Set driver
        ## Inv2 common

        ## Inv2 NMOS
        _Mst_Inv2_NMOS_NumberofGate           = 1,
        _Mst_Inv2_NMOS_ChannelWidth           = 300,
        _Mst_Inv2_NMOS_ChannelLength          = 30,
        _Mst_Inv2_NMOS_XVT                    = 'SLVT',
        _Mst_Inv2_NMOS_POGate_Comb_length     = 100,

        ## Inv2 PMOS
        _Mst_Inv2_PMOS_NumberofGate           = 3,
        _Mst_Inv2_PMOS_ChannelWidth           = 500,
        _Mst_Inv2_PMOS_ChannelLength          = 30,
        _Mst_Inv2_PMOS_XVT                    = 'SLVT',
        _Mst_Inv2_PMOS_POGate_Comb_length     = 100,



    ## Master Inv3 : Clock driver
        ## Inv3 common

        ## Inv3 NMOS
        _Mst_Inv3_NMOS_NumberofGate           = 1,
        _Mst_Inv3_NMOS_ChannelWidth           = 300,
        _Mst_Inv3_NMOS_ChannelLength          = 30,
        _Mst_Inv3_NMOS_XVT                    = 'SLVT',
        _Mst_Inv3_NMOS_POGate_Comb_length     = 100,

        ## Inv3 PMOS
        _Mst_Inv3_PMOS_NumberofGate           = 3,
        _Mst_Inv3_PMOS_ChannelWidth           = 500,
        _Mst_Inv3_PMOS_ChannelLength          = 30,
        _Mst_Inv3_PMOS_XVT                    = 'SLVT',
        _Mst_Inv3_PMOS_POGate_Comb_length     = 100,




    ## Slave Xgate1
        ## Xgate common

        ## Xgate NMOS
        _Slv_Xgate1_NMOS_NumberofGate           = 1,
        _Slv_Xgate1_NMOS_ChannelWidth           = 300,
        _Slv_Xgate1_NMOS_ChannelLength          = 30,
        _Slv_Xgate1_NMOS_XVT                    = 'SLVT',
        _Slv_Xgate1_NMOS_POGate_Comb_length     = 100,

        ## Xgate NMOS
        _Slv_Xgate1_PMOS_NumberofGate           = 3,
        _Slv_Xgate1_PMOS_ChannelWidth           = 500,
        _Slv_Xgate1_PMOS_ChannelLength          = 30,
        _Slv_Xgate1_PMOS_XVT                    = 'SLVT',
        _Slv_Xgate1_PMOS_POGate_Comb_length     = 100,

    ## Slave Xgate2
        ## Xgate common

        ## Xgate NMOS
        _Slv_Xgate2_NMOS_NumberofGate           = 2,
        _Slv_Xgate2_NMOS_ChannelWidth           = 800,
        _Slv_Xgate2_NMOS_ChannelLength          = 30,
        _Slv_Xgate2_NMOS_XVT                    = 'SLVT',
        _Slv_Xgate2_NMOS_POGate_Comb_length     = 100,

        ## Xgate NMOS
        _Slv_Xgate2_PMOS_NumberofGate           = 3,
        _Slv_Xgate2_PMOS_ChannelWidth           = 200,
        _Slv_Xgate2_PMOS_ChannelLength          = 30,
        _Slv_Xgate2_PMOS_XVT                    = 'SLVT',
        _Slv_Xgate2_PMOS_POGate_Comb_length     = 100,


    ## Slave Nor1
        ## Nor1 common

        ## NMOS
            ## NMOS common
        _Slv_Nor1_NMOS_XVT='SLVT',

            ## NMOSA
        _Slv_Nor1_NMOSA_NumberofGate           = 2,
        _Slv_Nor1_NMOSA_ChannelWidth           = 800,
        _Slv_Nor1_NMOSA_ChannelLength          = 30,
        _Slv_Nor1_NMOSA_POGate_Comb_length     = 100,

            ## NMOSB
        _Slv_Nor1_NMOSB_NumberofGate           = 3,
        _Slv_Nor1_NMOSB_ChannelWidth           = 200,
        _Slv_Nor1_NMOSB_ChannelLength          = 30,
        _Slv_Nor1_NMOSB_POGate_Comb_length     = 100,

        ## PMOS
            ## PMOS common
        _Slv_Nor1_PMOS_XVT='SLVT',

            ## PMOSA
        _Slv_Nor1_PMOSA_NumberofGate            = 2,
        _Slv_Nor1_PMOSA_ChannelWidth            = 800,
        _Slv_Nor1_PMOSA_ChannelLength           = 30,
        _Slv_Nor1_PMOSA_POGate_Comb_length      = 100,

            ## PMOSB
        _Slv_Nor1_PMOSB_NumberofGate            = 3,
        _Slv_Nor1_PMOSB_ChannelWidth            = 200,
        _Slv_Nor1_PMOSB_ChannelLength           = 30,
        _Slv_Nor1_PMOSB_POGate_Comb_length      = 100,

    ## Slave Nor2
        ## Nor2 common

        ## NMOS
            ## NMOS common
        _Slv_Nor2_NMOS_XVT='SLVT',

            ## NMOSA
        _Slv_Nor2_NMOSA_NumberofGate           = 2,
        _Slv_Nor2_NMOSA_ChannelWidth           = 800,
        _Slv_Nor2_NMOSA_ChannelLength          = 30,
        _Slv_Nor2_NMOSA_POGate_Comb_length     = 100,

            ## NMOSB
        _Slv_Nor2_NMOSB_NumberofGate           = 3,
        _Slv_Nor2_NMOSB_ChannelWidth           = 200,
        _Slv_Nor2_NMOSB_ChannelLength          = 30,
        _Slv_Nor2_NMOSB_POGate_Comb_length     = 100,

        ## PMOS
            ## PMOS common
        _Slv_Nor2_PMOS_XVT='SLVT',

            ## PMOSA
        _Slv_Nor2_PMOSA_NumberofGate            = 2,
        _Slv_Nor2_PMOSA_ChannelWidth            = 800,
        _Slv_Nor2_PMOSA_ChannelLength           = 30,
        _Slv_Nor2_PMOSA_POGate_Comb_length      = 100,

            ## PMOSB
        _Slv_Nor2_PMOSB_NumberofGate            = 3,
        _Slv_Nor2_PMOSB_ChannelWidth            = 200,
        _Slv_Nor2_PMOSB_ChannelLength           = 30,
        _Slv_Nor2_PMOSB_POGate_Comb_length      = 100,

    ## Slave Inv1 : ReSet pre-driver
        ## Inv1 common

        ## Inv1 NMOS
        _Slv_Inv1_NMOS_NumberofGate           = 1,
        _Slv_Inv1_NMOS_ChannelWidth           = 300,
        _Slv_Inv1_NMOS_ChannelLength          = 30,
        _Slv_Inv1_NMOS_XVT                    = 'SLVT',
        _Slv_Inv1_NMOS_POGate_Comb_length     = 100,

        ## Inv1 PMOS
        _Slv_Inv1_PMOS_NumberofGate           = 3,
        _Slv_Inv1_PMOS_ChannelWidth           = 500,
        _Slv_Inv1_PMOS_ChannelLength          = 30,
        _Slv_Inv1_PMOS_XVT                    = 'SLVT',
        _Slv_Inv1_PMOS_POGate_Comb_length     = 100,

    ## Slave Inv2 : ReSet driver
        ## Inv2 common

        ## Inv2 NMOS
        _Slv_Inv2_NMOS_NumberofGate           = 1,
        _Slv_Inv2_NMOS_ChannelWidth           = 300,
        _Slv_Inv2_NMOS_ChannelLength          = 30,
        _Slv_Inv2_NMOS_XVT                    = 'SLVT',
        _Slv_Inv2_NMOS_POGate_Comb_length     = 100,

        ## Inv2 PMOS
        _Slv_Inv2_PMOS_NumberofGate           = 3,
        _Slv_Inv2_PMOS_ChannelWidth           = 500,
        _Slv_Inv2_PMOS_ChannelLength          = 30,
        _Slv_Inv2_PMOS_XVT                    = 'SLVT',
        _Slv_Inv2_PMOS_POGate_Comb_length     = 100,


    ## Slave Inv3 : Qb driver
        ## Inv3 common

        ## Inv3 NMOS
        _Slv_Inv3_NMOS_NumberofGate           = 1,
        _Slv_Inv3_NMOS_ChannelWidth           = 300,
        _Slv_Inv3_NMOS_ChannelLength          = 30,
        _Slv_Inv3_NMOS_XVT                    = 'SLVT',
        _Slv_Inv3_NMOS_POGate_Comb_length     = 100,

        ## Inv3 PMOS
        _Slv_Inv3_PMOS_NumberofGate           = 3,
        _Slv_Inv3_PMOS_ChannelWidth           = 500,
        _Slv_Inv3_PMOS_ChannelLength          = 30,
        _Slv_Inv3_PMOS_XVT                    = 'SLVT',
        _Slv_Inv3_PMOS_POGate_Comb_length     = 100,


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

        _Test_distance = 500,
        _Routing_width =  50,
        _Routing_distance = 100,

    ## DFF Common
        _DFF_Pbody_NumCont      = 2, # number
        _DFF_Nbody_NumCont      = 2, # number
        _DFF_PMOSXvt2NMOSXvt    = 500, # number
        _DFF_XvtTop2Pbody       = None, # number/None(Minimum)
        _DFF_Xvtdown2Nbody      = None, # number/None(Minimum)

    ## Master Xgate1
        ## Xgate common

        ## Xgate NMOS
        _Mst_Xgate1_NMOS_NumberofGate           = 1,
        _Mst_Xgate1_NMOS_ChannelWidth           = 300,
        _Mst_Xgate1_NMOS_ChannelLength          = 30,
        _Mst_Xgate1_NMOS_XVT                    = 'SLVT',
        _Mst_Xgate1_NMOS_POGate_Comb_length     = 100,

        ## Xgate NMOS
        _Mst_Xgate1_PMOS_NumberofGate           = 3,
        _Mst_Xgate1_PMOS_ChannelWidth           = 500,
        _Mst_Xgate1_PMOS_ChannelLength          = 30,
        _Mst_Xgate1_PMOS_XVT                    = 'SLVT',
        _Mst_Xgate1_PMOS_POGate_Comb_length     = 100,

    ## Master Xgate2
        ## Xgate common

        ## Xgate NMOS
        _Mst_Xgate2_NMOS_NumberofGate           = 2,
        _Mst_Xgate2_NMOS_ChannelWidth           = 800,
        _Mst_Xgate2_NMOS_ChannelLength          = 30,
        _Mst_Xgate2_NMOS_XVT                    = 'SLVT',
        _Mst_Xgate2_NMOS_POGate_Comb_length     = 100,

        ## Xgate NMOS
        _Mst_Xgate2_PMOS_NumberofGate           = 3,
        _Mst_Xgate2_PMOS_ChannelWidth           = 200,
        _Mst_Xgate2_PMOS_ChannelLength          = 30,
        _Mst_Xgate2_PMOS_XVT                    = 'SLVT',
        _Mst_Xgate2_PMOS_POGate_Comb_length     = 100,


    ## Master Nor1
        ## Nor1 common

        ## NMOS
            ## NMOS common
        _Mst_Nor1_NMOS_XVT='SLVT',

            ## NMOSA
        _Mst_Nor1_NMOSA_NumberofGate           = 2,
        _Mst_Nor1_NMOSA_ChannelWidth           = 800,
        _Mst_Nor1_NMOSA_ChannelLength          = 30,
        _Mst_Nor1_NMOSA_POGate_Comb_length     = 100,

            ## NMOSB
        _Mst_Nor1_NMOSB_NumberofGate           = 3,
        _Mst_Nor1_NMOSB_ChannelWidth           = 200,
        _Mst_Nor1_NMOSB_ChannelLength          = 30,
        _Mst_Nor1_NMOSB_POGate_Comb_length     = 100,

        ## PMOS
            ## PMOS common
        _Mst_Nor1_PMOS_XVT='SLVT',

            ## PMOSA
        _Mst_Nor1_PMOSA_NumberofGate            = 2,
        _Mst_Nor1_PMOSA_ChannelWidth            = 800,
        _Mst_Nor1_PMOSA_ChannelLength           = 30,
        _Mst_Nor1_PMOSA_POGate_Comb_length      = 100,

            ## PMOSB
        _Mst_Nor1_PMOSB_NumberofGate            = 3,
        _Mst_Nor1_PMOSB_ChannelWidth            = 200,
        _Mst_Nor1_PMOSB_ChannelLength           = 30,
        _Mst_Nor1_PMOSB_POGate_Comb_length      = 100,

    ## Master Nor2
        ## Nor2 common

        ## NMOS
            ## NMOS common
        _Mst_Nor2_NMOS_XVT='SLVT',

            ## NMOSA
        _Mst_Nor2_NMOSA_NumberofGate           = 2,
        _Mst_Nor2_NMOSA_ChannelWidth           = 800,
        _Mst_Nor2_NMOSA_ChannelLength          = 30,
        _Mst_Nor2_NMOSA_POGate_Comb_length     = 100,

            ## NMOSB
        _Mst_Nor2_NMOSB_NumberofGate           = 3,
        _Mst_Nor2_NMOSB_ChannelWidth           = 200,
        _Mst_Nor2_NMOSB_ChannelLength          = 30,
        _Mst_Nor2_NMOSB_POGate_Comb_length     = 100,

        ## PMOS
            ## PMOS common
        _Mst_Nor2_PMOS_XVT='SLVT',

            ## PMOSA
        _Mst_Nor2_PMOSA_NumberofGate            = 2,
        _Mst_Nor2_PMOSA_ChannelWidth            = 800,
        _Mst_Nor2_PMOSA_ChannelLength           = 30,
        _Mst_Nor2_PMOSA_POGate_Comb_length      = 100,

            ## PMOSB
        _Mst_Nor2_PMOSB_NumberofGate            = 3,
        _Mst_Nor2_PMOSB_ChannelWidth            = 200,
        _Mst_Nor2_PMOSB_ChannelLength           = 30,
        _Mst_Nor2_PMOSB_POGate_Comb_length      = 100,

    ## Master Inv1
        ## Inv1 common

        ## Inv1 NMOS
        _Mst_Inv1_NMOS_NumberofGate           = 1,
        _Mst_Inv1_NMOS_ChannelWidth           = 300,
        _Mst_Inv1_NMOS_ChannelLength          = 30,
        _Mst_Inv1_NMOS_XVT                    = 'SLVT',
        _Mst_Inv1_NMOS_POGate_Comb_length     = 100,

        ## Inv1 PMOS
        _Mst_Inv1_PMOS_NumberofGate           = 3,
        _Mst_Inv1_PMOS_ChannelWidth           = 500,
        _Mst_Inv1_PMOS_ChannelLength          = 30,
        _Mst_Inv1_PMOS_XVT                    = 'SLVT',
        _Mst_Inv1_PMOS_POGate_Comb_length     = 100,

    ## Master Inv2 : Set driver
        ## Inv2 common

        ## Inv2 NMOS
        _Mst_Inv2_NMOS_NumberofGate           = 1,
        _Mst_Inv2_NMOS_ChannelWidth           = 300,
        _Mst_Inv2_NMOS_ChannelLength          = 30,
        _Mst_Inv2_NMOS_XVT                    = 'SLVT',
        _Mst_Inv2_NMOS_POGate_Comb_length     = 100,

        ## Inv2 PMOS
        _Mst_Inv2_PMOS_NumberofGate           = 3,
        _Mst_Inv2_PMOS_ChannelWidth           = 500,
        _Mst_Inv2_PMOS_ChannelLength          = 30,
        _Mst_Inv2_PMOS_XVT                    = 'SLVT',
        _Mst_Inv2_PMOS_POGate_Comb_length     = 100,

    ## Master Inv3 : Clock driver
        ## Inv3 common

        ## Inv3 NMOS
        _Mst_Inv3_NMOS_NumberofGate           = 1,
        _Mst_Inv3_NMOS_ChannelWidth           = 300,
        _Mst_Inv3_NMOS_ChannelLength          = 30,
        _Mst_Inv3_NMOS_XVT                    = 'SLVT',
        _Mst_Inv3_NMOS_POGate_Comb_length     = 100,

        ## Inv3 PMOS
        _Mst_Inv3_PMOS_NumberofGate           = 3,
        _Mst_Inv3_PMOS_ChannelWidth           = 500,
        _Mst_Inv3_PMOS_ChannelLength          = 30,
        _Mst_Inv3_PMOS_XVT                    = 'SLVT',
        _Mst_Inv3_PMOS_POGate_Comb_length     = 100,




    ## Slave Xgate1
        ## Xgate common

        ## Xgate NMOS
        _Slv_Xgate1_NMOS_NumberofGate           = 1,
        _Slv_Xgate1_NMOS_ChannelWidth           = 300,
        _Slv_Xgate1_NMOS_ChannelLength          = 30,
        _Slv_Xgate1_NMOS_XVT                    = 'SLVT',
        _Slv_Xgate1_NMOS_POGate_Comb_length     = 100,

        ## Xgate NMOS
        _Slv_Xgate1_PMOS_NumberofGate           = 3,
        _Slv_Xgate1_PMOS_ChannelWidth           = 500,
        _Slv_Xgate1_PMOS_ChannelLength          = 30,
        _Slv_Xgate1_PMOS_XVT                    = 'SLVT',
        _Slv_Xgate1_PMOS_POGate_Comb_length     = 100,

    ## Slave Xgate2
        ## Xgate common

        ## Xgate NMOS
        _Slv_Xgate2_NMOS_NumberofGate           = 2,
        _Slv_Xgate2_NMOS_ChannelWidth           = 800,
        _Slv_Xgate2_NMOS_ChannelLength          = 30,
        _Slv_Xgate2_NMOS_XVT                    = 'SLVT',
        _Slv_Xgate2_NMOS_POGate_Comb_length     = 100,

        ## Xgate NMOS
        _Slv_Xgate2_PMOS_NumberofGate           = 3,
        _Slv_Xgate2_PMOS_ChannelWidth           = 200,
        _Slv_Xgate2_PMOS_ChannelLength          = 30,
        _Slv_Xgate2_PMOS_XVT                    = 'SLVT',
        _Slv_Xgate2_PMOS_POGate_Comb_length     = 100,


    ## Slave Nor1
        ## Nor1 common

        ## NMOS
            ## NMOS common
        _Slv_Nor1_NMOS_XVT='SLVT',

            ## NMOSA
        _Slv_Nor1_NMOSA_NumberofGate           = 2,
        _Slv_Nor1_NMOSA_ChannelWidth           = 800,
        _Slv_Nor1_NMOSA_ChannelLength          = 30,
        _Slv_Nor1_NMOSA_POGate_Comb_length     = 100,

            ## NMOSB
        _Slv_Nor1_NMOSB_NumberofGate           = 3,
        _Slv_Nor1_NMOSB_ChannelWidth           = 200,
        _Slv_Nor1_NMOSB_ChannelLength          = 30,
        _Slv_Nor1_NMOSB_POGate_Comb_length     = 100,

        ## PMOS
            ## PMOS common
        _Slv_Nor1_PMOS_XVT='SLVT',

            ## PMOSA
        _Slv_Nor1_PMOSA_NumberofGate            = 2,
        _Slv_Nor1_PMOSA_ChannelWidth            = 800,
        _Slv_Nor1_PMOSA_ChannelLength           = 30,
        _Slv_Nor1_PMOSA_POGate_Comb_length      = 100,

            ## PMOSB
        _Slv_Nor1_PMOSB_NumberofGate            = 3,
        _Slv_Nor1_PMOSB_ChannelWidth            = 200,
        _Slv_Nor1_PMOSB_ChannelLength           = 30,
        _Slv_Nor1_PMOSB_POGate_Comb_length      = 100,

    ## Slave Nor2
        ## Nor2 common

        ## NMOS
            ## NMOS common
        _Slv_Nor2_NMOS_XVT='SLVT',

            ## NMOSA
        _Slv_Nor2_NMOSA_NumberofGate           = 2,
        _Slv_Nor2_NMOSA_ChannelWidth           = 800,
        _Slv_Nor2_NMOSA_ChannelLength          = 30,
        _Slv_Nor2_NMOSA_POGate_Comb_length     = 100,

            ## NMOSB
        _Slv_Nor2_NMOSB_NumberofGate           = 3,
        _Slv_Nor2_NMOSB_ChannelWidth           = 200,
        _Slv_Nor2_NMOSB_ChannelLength          = 30,
        _Slv_Nor2_NMOSB_POGate_Comb_length     = 100,

        ## PMOS
            ## PMOS common
        _Slv_Nor2_PMOS_XVT='SLVT',

            ## PMOSA
        _Slv_Nor2_PMOSA_NumberofGate            = 2,
        _Slv_Nor2_PMOSA_ChannelWidth            = 800,
        _Slv_Nor2_PMOSA_ChannelLength           = 30,
        _Slv_Nor2_PMOSA_POGate_Comb_length      = 100,

            ## PMOSB
        _Slv_Nor2_PMOSB_NumberofGate            = 3,
        _Slv_Nor2_PMOSB_ChannelWidth            = 200,
        _Slv_Nor2_PMOSB_ChannelLength           = 30,
        _Slv_Nor2_PMOSB_POGate_Comb_length      = 100,

    ## Slave Inv1 : ReSet pre-driver
        ## Inv1 common

        ## Inv1 NMOS
        _Slv_Inv1_NMOS_NumberofGate           = 1,
        _Slv_Inv1_NMOS_ChannelWidth           = 300,
        _Slv_Inv1_NMOS_ChannelLength          = 30,
        _Slv_Inv1_NMOS_XVT                    = 'SLVT',
        _Slv_Inv1_NMOS_POGate_Comb_length     = 100,

        ## Inv1 PMOS
        _Slv_Inv1_PMOS_NumberofGate           = 3,
        _Slv_Inv1_PMOS_ChannelWidth           = 500,
        _Slv_Inv1_PMOS_ChannelLength          = 30,
        _Slv_Inv1_PMOS_XVT                    = 'SLVT',
        _Slv_Inv1_PMOS_POGate_Comb_length     = 100,

    ## Slave Inv2 : ReSet driver
        ## Inv2 common

        ## Inv2 NMOS
        _Slv_Inv2_NMOS_NumberofGate           = 1,
        _Slv_Inv2_NMOS_ChannelWidth           = 300,
        _Slv_Inv2_NMOS_ChannelLength          = 30,
        _Slv_Inv2_NMOS_XVT                    = 'SLVT',
        _Slv_Inv2_NMOS_POGate_Comb_length     = 100,

        ## Inv2 PMOS
        _Slv_Inv2_PMOS_NumberofGate           = 3,
        _Slv_Inv2_PMOS_ChannelWidth           = 500,
        _Slv_Inv2_PMOS_ChannelLength          = 30,
        _Slv_Inv2_PMOS_XVT                    = 'SLVT',
        _Slv_Inv2_PMOS_POGate_Comb_length     = 100,


    ## Slave Inv3 : Qb driver
        ## Inv3 common

        ## Inv3 NMOS
        _Slv_Inv3_NMOS_NumberofGate           = 1,
        _Slv_Inv3_NMOS_ChannelWidth           = 300,
        _Slv_Inv3_NMOS_ChannelLength          = 30,
        _Slv_Inv3_NMOS_XVT                    = 'SLVT',
        _Slv_Inv3_NMOS_POGate_Comb_length     = 100,

        ## Inv3 PMOS
        _Slv_Inv3_PMOS_NumberofGate           = 3,
        _Slv_Inv3_PMOS_ChannelWidth           = 500,
        _Slv_Inv3_PMOS_ChannelLength          = 30,
        _Slv_Inv3_PMOS_XVT                    = 'SLVT',
        _Slv_Inv3_PMOS_POGate_Comb_length     = 100,


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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## SetRstDFF_Nor_Height
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D04_00_SetRstDFF_Nor_Placement_KJH0._SetRstDFF_Nor_Placement._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Test_distance']                      = _Test_distance
        ## DFF Common
        _Caculation_Parameters['_DFF_Pbody_NumCont']                 = _DFF_Pbody_NumCont
        _Caculation_Parameters['_DFF_Nbody_NumCont']                 = _DFF_Nbody_NumCont
        _Caculation_Parameters['_DFF_PMOSXvt2NMOSXvt']               = _DFF_PMOSXvt2NMOSXvt
        _Caculation_Parameters['_DFF_XvtTop2Pbody']                  = _DFF_XvtTop2Pbody
        _Caculation_Parameters['_DFF_Xvtdown2Nbody']                 = _DFF_Xvtdown2Nbody
        ## Master Xgate1
        _Caculation_Parameters['_Mst_Xgate1_NMOS_NumberofGate']                 = _Mst_Xgate1_NMOS_NumberofGate
        _Caculation_Parameters['_Mst_Xgate1_NMOS_ChannelWidth']                 = _Mst_Xgate1_NMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Xgate1_NMOS_ChannelLength']                = _Mst_Xgate1_NMOS_ChannelLength
        _Caculation_Parameters['_Mst_Xgate1_NMOS_XVT']                          = _Mst_Xgate1_NMOS_XVT
        _Caculation_Parameters['_Mst_Xgate1_NMOS_POGate_Comb_length']           = _Mst_Xgate1_NMOS_POGate_Comb_length

        _Caculation_Parameters['_Mst_Xgate1_PMOS_NumberofGate']                 = _Mst_Xgate1_PMOS_NumberofGate
        _Caculation_Parameters['_Mst_Xgate1_PMOS_ChannelWidth']                 = _Mst_Xgate1_PMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Xgate1_PMOS_ChannelLength']                = _Mst_Xgate1_PMOS_ChannelLength
        _Caculation_Parameters['_Mst_Xgate1_PMOS_XVT']                          = _Mst_Xgate1_PMOS_XVT
        _Caculation_Parameters['_Mst_Xgate1_PMOS_POGate_Comb_length']           = _Mst_Xgate1_PMOS_POGate_Comb_length
        ## Master Xgate2
        _Caculation_Parameters['_Mst_Xgate2_NMOS_NumberofGate']                 = _Mst_Xgate2_NMOS_NumberofGate
        _Caculation_Parameters['_Mst_Xgate2_NMOS_ChannelWidth']                 = _Mst_Xgate2_NMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Xgate2_NMOS_ChannelLength']                = _Mst_Xgate2_NMOS_ChannelLength
        _Caculation_Parameters['_Mst_Xgate2_NMOS_XVT']                          = _Mst_Xgate2_NMOS_XVT
        _Caculation_Parameters['_Mst_Xgate2_NMOS_POGate_Comb_length']           = _Mst_Xgate2_NMOS_POGate_Comb_length

        _Caculation_Parameters['_Mst_Xgate2_PMOS_NumberofGate']                 = _Mst_Xgate2_PMOS_NumberofGate
        _Caculation_Parameters['_Mst_Xgate2_PMOS_ChannelWidth']                 = _Mst_Xgate2_PMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Xgate2_PMOS_ChannelLength']                = _Mst_Xgate2_PMOS_ChannelLength
        _Caculation_Parameters['_Mst_Xgate2_PMOS_XVT']                          = _Mst_Xgate2_PMOS_XVT
        _Caculation_Parameters['_Mst_Xgate2_PMOS_POGate_Comb_length']           = _Mst_Xgate2_PMOS_POGate_Comb_length
        ## Master Nor1
        _Caculation_Parameters['_Mst_Nor1_NMOS_XVT']                 = _Mst_Nor1_NMOS_XVT

        _Caculation_Parameters['_Mst_Nor1_NMOSA_NumberofGate']                 = _Mst_Nor1_NMOSA_NumberofGate
        _Caculation_Parameters['_Mst_Nor1_NMOSA_ChannelWidth']                 = _Mst_Nor1_NMOSA_ChannelWidth
        _Caculation_Parameters['_Mst_Nor1_NMOSA_ChannelLength']                = _Mst_Nor1_NMOSA_ChannelLength
        _Caculation_Parameters['_Mst_Nor1_NMOSA_POGate_Comb_length']           = _Mst_Nor1_NMOSA_POGate_Comb_length

        _Caculation_Parameters['_Mst_Nor1_NMOSB_NumberofGate']                 = _Mst_Nor1_NMOSB_NumberofGate
        _Caculation_Parameters['_Mst_Nor1_NMOSB_ChannelWidth']                 = _Mst_Nor1_NMOSB_ChannelWidth
        _Caculation_Parameters['_Mst_Nor1_NMOSB_ChannelLength']                = _Mst_Nor1_NMOSB_ChannelLength
        _Caculation_Parameters['_Mst_Nor1_NMOSB_POGate_Comb_length']           = _Mst_Nor1_NMOSB_POGate_Comb_length

        _Caculation_Parameters['_Mst_Nor1_PMOS_XVT']                 = _Mst_Nor1_PMOS_XVT

        _Caculation_Parameters['_Mst_Nor1_PMOSA_NumberofGate']                 = _Mst_Nor1_PMOSA_NumberofGate
        _Caculation_Parameters['_Mst_Nor1_PMOSA_ChannelWidth']                 = _Mst_Nor1_PMOSA_ChannelWidth
        _Caculation_Parameters['_Mst_Nor1_PMOSA_ChannelLength']                = _Mst_Nor1_PMOSA_ChannelLength
        _Caculation_Parameters['_Mst_Nor1_PMOSA_POGate_Comb_length']           = _Mst_Nor1_PMOSA_POGate_Comb_length

        _Caculation_Parameters['_Mst_Nor1_PMOSB_NumberofGate']                 = _Mst_Nor1_PMOSB_NumberofGate
        _Caculation_Parameters['_Mst_Nor1_PMOSB_ChannelWidth']                 = _Mst_Nor1_PMOSB_ChannelWidth
        _Caculation_Parameters['_Mst_Nor1_PMOSB_ChannelLength']                = _Mst_Nor1_PMOSB_ChannelLength
        _Caculation_Parameters['_Mst_Nor1_PMOSB_POGate_Comb_length']           = _Mst_Nor1_PMOSB_POGate_Comb_length
        ## Master Nor2
        _Caculation_Parameters['_Mst_Nor2_NMOS_XVT']                 = _Mst_Nor2_NMOS_XVT

        _Caculation_Parameters['_Mst_Nor2_NMOSA_NumberofGate']                 = _Mst_Nor2_NMOSA_NumberofGate
        _Caculation_Parameters['_Mst_Nor2_NMOSA_ChannelWidth']                 = _Mst_Nor2_NMOSA_ChannelWidth
        _Caculation_Parameters['_Mst_Nor2_NMOSA_ChannelLength']                = _Mst_Nor2_NMOSA_ChannelLength
        _Caculation_Parameters['_Mst_Nor2_NMOSA_POGate_Comb_length']           = _Mst_Nor2_NMOSA_POGate_Comb_length

        _Caculation_Parameters['_Mst_Nor2_NMOSB_NumberofGate']                 = _Mst_Nor2_NMOSB_NumberofGate
        _Caculation_Parameters['_Mst_Nor2_NMOSB_ChannelWidth']                 = _Mst_Nor2_NMOSB_ChannelWidth
        _Caculation_Parameters['_Mst_Nor2_NMOSB_ChannelLength']                = _Mst_Nor2_NMOSB_ChannelLength
        _Caculation_Parameters['_Mst_Nor2_NMOSB_POGate_Comb_length']           = _Mst_Nor2_NMOSB_POGate_Comb_length

        _Caculation_Parameters['_Mst_Nor2_PMOS_XVT']                 = _Mst_Nor2_PMOS_XVT

        _Caculation_Parameters['_Mst_Nor2_PMOSA_NumberofGate']                 = _Mst_Nor2_PMOSA_NumberofGate
        _Caculation_Parameters['_Mst_Nor2_PMOSA_ChannelWidth']                 = _Mst_Nor2_PMOSA_ChannelWidth
        _Caculation_Parameters['_Mst_Nor2_PMOSA_ChannelLength']                = _Mst_Nor2_PMOSA_ChannelLength
        _Caculation_Parameters['_Mst_Nor2_PMOSA_POGate_Comb_length']           = _Mst_Nor2_PMOSA_POGate_Comb_length

        _Caculation_Parameters['_Mst_Nor2_PMOSB_NumberofGate']                 = _Mst_Nor2_PMOSB_NumberofGate
        _Caculation_Parameters['_Mst_Nor2_PMOSB_ChannelWidth']                 = _Mst_Nor2_PMOSB_ChannelWidth
        _Caculation_Parameters['_Mst_Nor2_PMOSB_ChannelLength']                = _Mst_Nor2_PMOSB_ChannelLength
        _Caculation_Parameters['_Mst_Nor2_PMOSB_POGate_Comb_length']           = _Mst_Nor2_PMOSB_POGate_Comb_length
        ## Master Inv1
        _Caculation_Parameters['_Mst_Inv1_NMOS_NumberofGate']                  = _Mst_Inv1_NMOS_NumberofGate
        _Caculation_Parameters['_Mst_Inv1_NMOS_ChannelWidth']                  = _Mst_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Inv1_NMOS_ChannelLength']                 = _Mst_Inv1_NMOS_ChannelLength
        _Caculation_Parameters['_Mst_Inv1_NMOS_XVT']                           = _Mst_Inv1_NMOS_XVT
        _Caculation_Parameters['_Mst_Inv1_NMOS_POGate_Comb_length']            = _Mst_Inv1_NMOS_POGate_Comb_length

        _Caculation_Parameters['_Mst_Inv1_PMOS_NumberofGate']                  = _Mst_Inv1_PMOS_NumberofGate
        _Caculation_Parameters['_Mst_Inv1_PMOS_ChannelWidth']                  = _Mst_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Inv1_PMOS_ChannelLength']                 = _Mst_Inv1_PMOS_ChannelLength
        _Caculation_Parameters['_Mst_Inv1_PMOS_XVT']                           = _Mst_Inv1_PMOS_XVT
        _Caculation_Parameters['_Mst_Inv1_PMOS_POGate_Comb_length']            = _Mst_Inv1_PMOS_POGate_Comb_length
        ## Master Inv2
        _Caculation_Parameters['_Mst_Inv2_NMOS_NumberofGate']                  = _Mst_Inv2_NMOS_NumberofGate
        _Caculation_Parameters['_Mst_Inv2_NMOS_ChannelWidth']                  = _Mst_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Inv2_NMOS_ChannelLength']                 = _Mst_Inv2_NMOS_ChannelLength
        _Caculation_Parameters['_Mst_Inv2_NMOS_XVT']                           = _Mst_Inv2_NMOS_XVT
        _Caculation_Parameters['_Mst_Inv2_NMOS_POGate_Comb_length']            = _Mst_Inv2_NMOS_POGate_Comb_length

        _Caculation_Parameters['_Mst_Inv2_PMOS_NumberofGate']                  = _Mst_Inv2_PMOS_NumberofGate
        _Caculation_Parameters['_Mst_Inv2_PMOS_ChannelWidth']                  = _Mst_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Inv2_PMOS_ChannelLength']                 = _Mst_Inv2_PMOS_ChannelLength
        _Caculation_Parameters['_Mst_Inv2_PMOS_XVT']                           = _Mst_Inv2_PMOS_XVT
        _Caculation_Parameters['_Mst_Inv2_PMOS_POGate_Comb_length']            = _Mst_Inv2_PMOS_POGate_Comb_length
        ## Master Inv3
        _Caculation_Parameters['_Mst_Inv3_NMOS_NumberofGate']                  = _Mst_Inv3_NMOS_NumberofGate
        _Caculation_Parameters['_Mst_Inv3_NMOS_ChannelWidth']                  = _Mst_Inv3_NMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Inv3_NMOS_ChannelLength']                 = _Mst_Inv3_NMOS_ChannelLength
        _Caculation_Parameters['_Mst_Inv3_NMOS_XVT']                           = _Mst_Inv3_NMOS_XVT
        _Caculation_Parameters['_Mst_Inv3_NMOS_POGate_Comb_length']            = _Mst_Inv3_NMOS_POGate_Comb_length

        _Caculation_Parameters['_Mst_Inv3_PMOS_NumberofGate']                  = _Mst_Inv3_PMOS_NumberofGate
        _Caculation_Parameters['_Mst_Inv3_PMOS_ChannelWidth']                  = _Mst_Inv3_PMOS_ChannelWidth
        _Caculation_Parameters['_Mst_Inv3_PMOS_ChannelLength']                 = _Mst_Inv3_PMOS_ChannelLength
        _Caculation_Parameters['_Mst_Inv3_PMOS_XVT']                           = _Mst_Inv3_PMOS_XVT
        _Caculation_Parameters['_Mst_Inv3_PMOS_POGate_Comb_length']            = _Mst_Inv3_PMOS_POGate_Comb_length



        ## Slave Xgate1
        _Caculation_Parameters['_Slv_Xgate1_NMOS_NumberofGate']                 = _Slv_Xgate1_NMOS_NumberofGate
        _Caculation_Parameters['_Slv_Xgate1_NMOS_ChannelWidth']                 = _Slv_Xgate1_NMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Xgate1_NMOS_ChannelLength']                = _Slv_Xgate1_NMOS_ChannelLength
        _Caculation_Parameters['_Slv_Xgate1_NMOS_XVT']                          = _Slv_Xgate1_NMOS_XVT
        _Caculation_Parameters['_Slv_Xgate1_NMOS_POGate_Comb_length']           = _Slv_Xgate1_NMOS_POGate_Comb_length

        _Caculation_Parameters['_Slv_Xgate1_PMOS_NumberofGate']                 = _Slv_Xgate1_PMOS_NumberofGate
        _Caculation_Parameters['_Slv_Xgate1_PMOS_ChannelWidth']                 = _Slv_Xgate1_PMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Xgate1_PMOS_ChannelLength']                = _Slv_Xgate1_PMOS_ChannelLength
        _Caculation_Parameters['_Slv_Xgate1_PMOS_XVT']                          = _Slv_Xgate1_PMOS_XVT
        _Caculation_Parameters['_Slv_Xgate1_PMOS_POGate_Comb_length']           = _Slv_Xgate1_PMOS_POGate_Comb_length
        ## Slave Xgate2
        _Caculation_Parameters['_Slv_Xgate2_NMOS_NumberofGate']                 = _Slv_Xgate2_NMOS_NumberofGate
        _Caculation_Parameters['_Slv_Xgate2_NMOS_ChannelWidth']                 = _Slv_Xgate2_NMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Xgate2_NMOS_ChannelLength']                = _Slv_Xgate2_NMOS_ChannelLength
        _Caculation_Parameters['_Slv_Xgate2_NMOS_XVT']                          = _Slv_Xgate2_NMOS_XVT
        _Caculation_Parameters['_Slv_Xgate2_NMOS_POGate_Comb_length']           = _Slv_Xgate2_NMOS_POGate_Comb_length

        _Caculation_Parameters['_Slv_Xgate2_PMOS_NumberofGate']                 = _Slv_Xgate2_PMOS_NumberofGate
        _Caculation_Parameters['_Slv_Xgate2_PMOS_ChannelWidth']                 = _Slv_Xgate2_PMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Xgate2_PMOS_ChannelLength']                = _Slv_Xgate2_PMOS_ChannelLength
        _Caculation_Parameters['_Slv_Xgate2_PMOS_XVT']                          = _Slv_Xgate2_PMOS_XVT
        _Caculation_Parameters['_Slv_Xgate2_PMOS_POGate_Comb_length']           = _Slv_Xgate2_PMOS_POGate_Comb_length
        ## Slave Nor1
        _Caculation_Parameters['_Slv_Nor1_NMOS_XVT']                 = _Slv_Nor1_NMOS_XVT

        _Caculation_Parameters['_Slv_Nor1_NMOSA_NumberofGate']                 = _Slv_Nor1_NMOSA_NumberofGate
        _Caculation_Parameters['_Slv_Nor1_NMOSA_ChannelWidth']                 = _Slv_Nor1_NMOSA_ChannelWidth
        _Caculation_Parameters['_Slv_Nor1_NMOSA_ChannelLength']                = _Slv_Nor1_NMOSA_ChannelLength
        _Caculation_Parameters['_Slv_Nor1_NMOSA_POGate_Comb_length']           = _Slv_Nor1_NMOSA_POGate_Comb_length

        _Caculation_Parameters['_Slv_Nor1_NMOSB_NumberofGate']                 = _Slv_Nor1_NMOSB_NumberofGate
        _Caculation_Parameters['_Slv_Nor1_NMOSB_ChannelWidth']                 = _Slv_Nor1_NMOSB_ChannelWidth
        _Caculation_Parameters['_Slv_Nor1_NMOSB_ChannelLength']                = _Slv_Nor1_NMOSB_ChannelLength
        _Caculation_Parameters['_Slv_Nor1_NMOSB_POGate_Comb_length']           = _Slv_Nor1_NMOSB_POGate_Comb_length

        _Caculation_Parameters['_Slv_Nor1_PMOS_XVT']                 = _Slv_Nor1_PMOS_XVT

        _Caculation_Parameters['_Slv_Nor1_PMOSA_NumberofGate']                 = _Slv_Nor1_PMOSA_NumberofGate
        _Caculation_Parameters['_Slv_Nor1_PMOSA_ChannelWidth']                 = _Slv_Nor1_PMOSA_ChannelWidth
        _Caculation_Parameters['_Slv_Nor1_PMOSA_ChannelLength']                = _Slv_Nor1_PMOSA_ChannelLength
        _Caculation_Parameters['_Slv_Nor1_PMOSA_POGate_Comb_length']           = _Slv_Nor1_PMOSA_POGate_Comb_length

        _Caculation_Parameters['_Slv_Nor1_PMOSB_NumberofGate']                 = _Slv_Nor1_PMOSB_NumberofGate
        _Caculation_Parameters['_Slv_Nor1_PMOSB_ChannelWidth']                 = _Slv_Nor1_PMOSB_ChannelWidth
        _Caculation_Parameters['_Slv_Nor1_PMOSB_ChannelLength']                = _Slv_Nor1_PMOSB_ChannelLength
        _Caculation_Parameters['_Slv_Nor1_PMOSB_POGate_Comb_length']           = _Slv_Nor1_PMOSB_POGate_Comb_length
        ## Slave Nor2
        _Caculation_Parameters['_Slv_Nor2_NMOS_XVT']                 = _Slv_Nor2_NMOS_XVT

        _Caculation_Parameters['_Slv_Nor2_NMOSA_NumberofGate']                 = _Slv_Nor2_NMOSA_NumberofGate
        _Caculation_Parameters['_Slv_Nor2_NMOSA_ChannelWidth']                 = _Slv_Nor2_NMOSA_ChannelWidth
        _Caculation_Parameters['_Slv_Nor2_NMOSA_ChannelLength']                = _Slv_Nor2_NMOSA_ChannelLength
        _Caculation_Parameters['_Slv_Nor2_NMOSA_POGate_Comb_length']           = _Slv_Nor2_NMOSA_POGate_Comb_length

        _Caculation_Parameters['_Slv_Nor2_NMOSB_NumberofGate']                 = _Slv_Nor2_NMOSB_NumberofGate
        _Caculation_Parameters['_Slv_Nor2_NMOSB_ChannelWidth']                 = _Slv_Nor2_NMOSB_ChannelWidth
        _Caculation_Parameters['_Slv_Nor2_NMOSB_ChannelLength']                = _Slv_Nor2_NMOSB_ChannelLength
        _Caculation_Parameters['_Slv_Nor2_NMOSB_POGate_Comb_length']           = _Slv_Nor2_NMOSB_POGate_Comb_length

        _Caculation_Parameters['_Slv_Nor2_PMOS_XVT']                 = _Slv_Nor2_PMOS_XVT

        _Caculation_Parameters['_Slv_Nor2_PMOSA_NumberofGate']                 = _Slv_Nor2_PMOSA_NumberofGate
        _Caculation_Parameters['_Slv_Nor2_PMOSA_ChannelWidth']                 = _Slv_Nor2_PMOSA_ChannelWidth
        _Caculation_Parameters['_Slv_Nor2_PMOSA_ChannelLength']                = _Slv_Nor2_PMOSA_ChannelLength
        _Caculation_Parameters['_Slv_Nor2_PMOSA_POGate_Comb_length']           = _Slv_Nor2_PMOSA_POGate_Comb_length

        _Caculation_Parameters['_Slv_Nor2_PMOSB_NumberofGate']                 = _Slv_Nor2_PMOSB_NumberofGate
        _Caculation_Parameters['_Slv_Nor2_PMOSB_ChannelWidth']                 = _Slv_Nor2_PMOSB_ChannelWidth
        _Caculation_Parameters['_Slv_Nor2_PMOSB_ChannelLength']                = _Slv_Nor2_PMOSB_ChannelLength
        _Caculation_Parameters['_Slv_Nor2_PMOSB_POGate_Comb_length']           = _Slv_Nor2_PMOSB_POGate_Comb_length
        ## Slave Inv1
        _Caculation_Parameters['_Slv_Inv1_NMOS_NumberofGate']                  = _Slv_Inv1_NMOS_NumberofGate
        _Caculation_Parameters['_Slv_Inv1_NMOS_ChannelWidth']                  = _Slv_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Inv1_NMOS_ChannelLength']                 = _Slv_Inv1_NMOS_ChannelLength
        _Caculation_Parameters['_Slv_Inv1_NMOS_XVT']                           = _Slv_Inv1_NMOS_XVT
        _Caculation_Parameters['_Slv_Inv1_NMOS_POGate_Comb_length']            = _Slv_Inv1_NMOS_POGate_Comb_length

        _Caculation_Parameters['_Slv_Inv1_PMOS_NumberofGate']                  = _Slv_Inv1_PMOS_NumberofGate
        _Caculation_Parameters['_Slv_Inv1_PMOS_ChannelWidth']                  = _Slv_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Inv1_PMOS_ChannelLength']                 = _Slv_Inv1_PMOS_ChannelLength
        _Caculation_Parameters['_Slv_Inv1_PMOS_XVT']                           = _Slv_Inv1_PMOS_XVT
        _Caculation_Parameters['_Slv_Inv1_PMOS_POGate_Comb_length']            = _Slv_Inv1_PMOS_POGate_Comb_length
        ## Slave Inv2
        _Caculation_Parameters['_Slv_Inv2_NMOS_NumberofGate']                  = _Slv_Inv2_NMOS_NumberofGate
        _Caculation_Parameters['_Slv_Inv2_NMOS_ChannelWidth']                  = _Slv_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Inv2_NMOS_ChannelLength']                 = _Slv_Inv2_NMOS_ChannelLength
        _Caculation_Parameters['_Slv_Inv2_NMOS_XVT']                           = _Slv_Inv2_NMOS_XVT
        _Caculation_Parameters['_Slv_Inv2_NMOS_POGate_Comb_length']            = _Slv_Inv2_NMOS_POGate_Comb_length

        _Caculation_Parameters['_Slv_Inv2_PMOS_NumberofGate']                  = _Slv_Inv2_PMOS_NumberofGate
        _Caculation_Parameters['_Slv_Inv2_PMOS_ChannelWidth']                  = _Slv_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Inv2_PMOS_ChannelLength']                 = _Slv_Inv2_PMOS_ChannelLength
        _Caculation_Parameters['_Slv_Inv2_PMOS_XVT']                           = _Slv_Inv2_PMOS_XVT
        _Caculation_Parameters['_Slv_Inv2_PMOS_POGate_Comb_length']            = _Slv_Inv2_PMOS_POGate_Comb_length
        ## Slave Inv3
        _Caculation_Parameters['_Slv_Inv3_NMOS_NumberofGate']                  = _Slv_Inv3_NMOS_NumberofGate
        _Caculation_Parameters['_Slv_Inv3_NMOS_ChannelWidth']                  = _Slv_Inv3_NMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Inv3_NMOS_ChannelLength']                 = _Slv_Inv3_NMOS_ChannelLength
        _Caculation_Parameters['_Slv_Inv3_NMOS_XVT']                           = _Slv_Inv3_NMOS_XVT
        _Caculation_Parameters['_Slv_Inv3_NMOS_POGate_Comb_length']            = _Slv_Inv3_NMOS_POGate_Comb_length

        _Caculation_Parameters['_Slv_Inv3_PMOS_NumberofGate']                  = _Slv_Inv3_PMOS_NumberofGate
        _Caculation_Parameters['_Slv_Inv3_PMOS_ChannelWidth']                  = _Slv_Inv3_PMOS_ChannelWidth
        _Caculation_Parameters['_Slv_Inv3_PMOS_ChannelLength']                 = _Slv_Inv3_PMOS_ChannelLength
        _Caculation_Parameters['_Slv_Inv3_PMOS_XVT']                           = _Slv_Inv3_PMOS_XVT
        _Caculation_Parameters['_Slv_Inv3_PMOS_POGate_Comb_length']            = _Slv_Inv3_PMOS_POGate_Comb_length

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_SetRst_Placement'] = self._SrefElementDeclaration(_DesignObj=D04_00_SetRstDFF_Nor_Placement_KJH0._SetRstDFF_Nor_Placement(_DesignParameter=None, _Name='{}:SRF_SetRst_Placement'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_SetRst_Placement']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SetRst_Placement']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SetRst_Placement']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SetRst_Placement']['_XYCoordinates'] = [[0, 0]]

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Body Cover.
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
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate1','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_Nbody_M1Exten']['_YWidth'] = tmp1[0][0][0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate1','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Inv3','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')

        self._DesignParameter['BND_Nbody_M1Exten']['_XWidth'] = abs( tmp2[0][0][0][0][0][0]['_XY_right'][0]- tmp1[0][0][0][0][0][0]['_XY_left'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Nbody_M1Exten']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Nbody_M1Exten']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate1','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        target_coord = tmp1[0][0][0][0][0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Nbody_M1Exten')
        approaching_coord = tmp2[0][0]['_XY_down_left']
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
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate1','SRF_Nbody','SRF_NbodyContactPhyLen','BND_ODLayer')
        self._DesignParameter['BND_Nbody_RXExten']['_YWidth'] = tmp1[0][0][0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate1','SRF_Nbody','SRF_NbodyContactPhyLen','BND_ODLayer')
        tmp2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Inv3','SRF_Nbody','SRF_NbodyContactPhyLen','BND_ODLayer')

        self._DesignParameter['BND_Nbody_RXExten']['_XWidth'] = abs( tmp2[0][0][0][0][0][0]['_XY_right'][0]- tmp1[0][0][0][0][0][0]['_XY_left'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Nbody_RXExten']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Nbody_RXExten']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate1','SRF_Nbody','SRF_NbodyContactPhyLen','BND_ODLayer')
        target_coord = tmp1[0][0][0][0][0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Nbody_RXExten')
        approaching_coord = tmp2[0][0]['_XY_down_left']
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
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate1','BND_PMOS_NellExten')
        self._DesignParameter['BND_Nbody_NwellExten']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate1','BND_PMOS_NellExten')
        tmp2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Inv3','BND_PMOS_NellExten')

        self._DesignParameter['BND_Nbody_NwellExten']['_XWidth'] = abs( tmp2[0][0][0][0]['_XY_right'][0]- tmp1[0][0][0][0]['_XY_left'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Nbody_NwellExten']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Nbody_NwellExten']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate1','BND_PMOS_NellExten')
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Nbody_NwellExten')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Nbody_NwellExten')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Nbody_NwellExten']['_XYCoordinates'] = tmpXY
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
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate1','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_Pbody_M1Exten']['_YWidth'] = tmp1[0][0][0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate1','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Inv3','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')

        self._DesignParameter['BND_Pbody_M1Exten']['_XWidth'] = abs( tmp2[0][0][0][0][0][0]['_XY_right'][0]- tmp1[0][0][0][0][0][0]['_XY_left'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Pbody_M1Exten']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Pbody_M1Exten']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate1','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        target_coord = tmp1[0][0][0][0][0][0]['_XY_down_left']
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
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate1','SRF_Pbody','SRF_PbodyContactPhyLen','BND_ODLayer')
        self._DesignParameter['BND_Pbody_RXExten']['_YWidth'] = tmp1[0][0][0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate1','SRF_Pbody','SRF_PbodyContactPhyLen','BND_ODLayer')
        tmp2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Inv3','SRF_Pbody','SRF_PbodyContactPhyLen','BND_ODLayer')

        self._DesignParameter['BND_Pbody_RXExten']['_XWidth'] = abs( tmp2[0][0][0][0][0][0]['_XY_right'][0]- tmp1[0][0][0][0][0][0]['_XY_left'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Pbody_RXExten']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Pbody_RXExten']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate1','SRF_Pbody','SRF_PbodyContactPhyLen','BND_ODLayer')
        target_coord = tmp1[0][0][0][0][0][0]['_XY_down_left']
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
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate1','SRF_Pbody','SRF_PbodyContactPhyLen','BND_PPLayer')
        self._DesignParameter['BND_Pbody_PPExten']['_YWidth'] = tmp1[0][0][0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate1','SRF_Pbody','SRF_PbodyContactPhyLen','BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Inv3','SRF_Pbody','SRF_PbodyContactPhyLen','BND_PPLayer')

        self._DesignParameter['BND_Pbody_PPExten']['_XWidth'] = abs( tmp2[0][0][0][0][0][0]['_XY_right'][0]- tmp1[0][0][0][0][0][0]['_XY_left'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Pbody_PPExten']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Pbody_PPExten']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate1','SRF_Pbody','SRF_PbodyContactPhyLen','BND_PPLayer')
        target_coord = tmp1[0][0][0][0][0][0]['_XY_down_left']
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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing.
        # del self._DesignParameter['SRF_SetRst_Height']['_DesignObj']._DesignParameter['SRF_Mst_Xgate1']
        # del self._DesignParameter['SRF_SetRst_Height']['_DesignObj']._DesignParameter['SRF_Mst_Xgate2']
        # del self._DesignParameter['SRF_SetRst_Height']['_DesignObj']._DesignParameter['SRF_Mst_Nor1']
        # del self._DesignParameter['SRF_SetRst_Height']['_DesignObj']._DesignParameter['SRF_Mst_Nor2']
        # del self._DesignParameter['SRF_SetRst_Height']['_DesignObj']._DesignParameter['SRF_Mst_Inv1']
        # del self._DesignParameter['SRF_SetRst_Height']['_DesignObj']._DesignParameter['SRF_Mst_Inv2']
        # del self._DesignParameter['SRF_SetRst_Height']['_DesignObj']._DesignParameter['SRF_Mst_Inv3']
        # del self._DesignParameter['SRF_SetRst_Height']['_DesignObj']._DesignParameter['SRF_Slv_Xgate1']
        # del self._DesignParameter['SRF_SetRst_Height']['_DesignObj']._DesignParameter['SRF_Slv_Xgate2']
        # del self._DesignParameter['SRF_SetRst_Height']['_DesignObj']._DesignParameter['SRF_Slv_Nor1']
        # del self._DesignParameter['SRF_SetRst_Height']['_DesignObj']._DesignParameter['SRF_Slv_Nor2']
        # del self._DesignParameter['SRF_SetRst_Height']['_DesignObj']._DesignParameter['SRF_Slv_Inv1']
        # del self._DesignParameter['SRF_SetRst_Height']['_DesignObj']._DesignParameter['SRF_Slv_Inv2']
        # del self._DesignParameter['SRF_SetRst_Height']['_DesignObj']._DesignParameter['SRF_Slv_Inv3']


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing Grid
        tmp  = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate1','SRF_PMOS','BND_Gate_Hrz_Mx')
        Y_Grid1_up    = tmp[0][0][0][0][0]['_XY_up'][1]
        Y_Grid1_down  = tmp[0][0][0][0][0]['_XY_down'][1]
        Y_Grid2_up    = Y_Grid1_down - _Routing_distance
        Y_Grid2_down  = Y_Grid2_up - _Routing_width
        Y_Grid3_up    = Y_Grid2_down - _Routing_distance
        Y_Grid3_down  = Y_Grid3_up - _Routing_width
        Y_Grid4_up    = Y_Grid3_down - _Routing_distance
        Y_Grid4_down  = Y_Grid4_up - _Routing_width
        Y_Grid5_up    = Y_Grid4_down - _Routing_distance
        Y_Grid5_down  = Y_Grid5_up - _Routing_width
        Y_Grid6_up    = Y_Grid5_down - _Routing_distance
        Y_Grid6_down  = Y_Grid6_up - _Routing_width
        Y_Grid7_up    = Y_Grid6_down - _Routing_distance
        Y_Grid7_down  = Y_Grid7_up - _Routing_width

        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate1','SRF_NMOS','BND_Gate_Hrz_Mx')
        Y_Grid8_up    = tmp1[0][0][0][0][0]['_XY_up'][1]
        Y_Grid8_down  = tmp1[0][0][0][0][0]['_XY_down'][1]

        tmp1_1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate1','SRF_PMOS','BND_PODummyLayer')
        tmp1_2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate1','SRF_NMOS','BND_PODummyLayer')
        target_coordx = max(tmp1_1[0][0][0][-1][0]['_XY_right'][0], tmp1_2[0][0][0][-1][0]['_XY_right'][0])
        tmp2_1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate2','SRF_PMOS','BND_PODummyLayer')
        tmp2_2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate2','SRF_NMOS','BND_PODummyLayer')
        approaching_coordx = min(tmp2_1[0][0][0][-1][0]['_XY_right'][0],tmp2_2[0][0][0][-1][0]['_XY_right'][0])
        X_Grid1 = np.round( 0.5*(target_coordx+approaching_coordx) )

        tmp1_1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate2','SRF_PMOS','BND_PODummyLayer')
        tmp1_2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate2','SRF_NMOS','BND_PODummyLayer')
        target_coordx = max(tmp1_1[0][0][0][0][0]['_XY_left'][0],tmp1_2[0][0][0][0][0]['_XY_left'][0])
        tmp2_1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Nor1','SRF_Pullup','SRF_PMOSA','BND_PODummyLayer')
        tmp2_2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Nor1','SRF_Pulldown','SRF_NMOSA','BND_PODummyLayer')
        approaching_coordx = min(tmp2_1[0][0][0][0][0][0]['_XY_left'][0],tmp2_2[0][0][0][0][0][0]['_XY_left'][0])
        X_Grid2 = np.round( 0.5*(target_coordx+approaching_coordx) )

        tmp1_1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Nor1','SRF_Pullup','SRF_PMOSB','BND_PODummyLayer')
        tmp1_2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Nor1','SRF_Pulldown','SRF_NMOSB','BND_PODummyLayer')
        target_coordx = max(tmp1_1[0][0][0][0][-1][0]['_XY_right'][0],tmp1_2[0][0][0][0][-1][0]['_XY_right'][0])
        tmp2_1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Nor2','SRF_Pullup','SRF_PMOSA','BND_PODummyLayer')
        tmp2_2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Nor2','SRF_Pulldown','SRF_NMOSA','BND_PODummyLayer')
        approaching_coordx = min(tmp2_1[0][0][0][0][0][0]['_XY_left'][0],tmp2_2[0][0][0][0][0][0]['_XY_left'][0])
        X_Grid3 = np.round( 0.5*(target_coordx+approaching_coordx) )

        tmp1_1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Nor2','SRF_Pullup','SRF_PMOSB','BND_PODummyLayer')
        tmp1_2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Nor2','SRF_Pulldown','SRF_NMOSB','BND_PODummyLayer')
        target_coordx = max(tmp1_1[0][0][0][0][-1][0]['_XY_right'][0],tmp1_2[0][0][0][0][-1][0]['_XY_right'][0])
        tmp2_1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Inv1','SRF_PMOS','BND_PODummyLayer')
        tmp2_2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Inv1','SRF_NMOS','BND_PODummyLayer')
        approaching_coordx = min(tmp2_1[0][0][0][0][0]['_XY_left'][0],tmp2_2[0][0][0][0][0]['_XY_left'][0])
        X_Grid4 = np.round( 0.5*(target_coordx+approaching_coordx) )

        tmp1_1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Inv1','SRF_PMOS','BND_PODummyLayer')
        tmp1_2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Inv1','SRF_NMOS','BND_PODummyLayer')
        target_coordx = max(tmp1_1[0][0][0][-1][0]['_XY_right'][0],tmp1_2[0][0][0][-1][0]['_XY_right'][0])
        tmp2_1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Inv2','SRF_PMOS','BND_PODummyLayer')
        tmp2_2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Inv2','SRF_NMOS','BND_PODummyLayer')
        approaching_coordx = min(tmp2_1[0][0][0][0][0]['_XY_left'][0],tmp2_2[0][0][0][0][0]['_XY_left'][0])
        X_Grid5 = np.round( 0.5*(target_coordx+approaching_coordx) )

        tmp1_1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Inv2','SRF_PMOS','BND_PODummyLayer')
        tmp1_2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Inv2','SRF_NMOS','BND_PODummyLayer')
        target_coordx = max(tmp1_1[0][0][0][-1][0]['_XY_right'][0],tmp1_2[0][0][0][-1][0]['_XY_right'][0])
        tmp2_1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Inv3','SRF_PMOS','BND_PODummyLayer')
        tmp2_2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Inv3','SRF_NMOS','BND_PODummyLayer')
        approaching_coordx = min(tmp2_1[0][0][0][0][0]['_XY_left'][0],tmp2_2[0][0][0][0][0]['_XY_left'][0])
        X_Grid6 = np.round( 0.5*(target_coordx+approaching_coordx) )

        tmp1_1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Inv3','SRF_PMOS','BND_PODummyLayer')
        tmp1_2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Inv3','SRF_NMOS','BND_PODummyLayer')
        target_coordx = max(tmp1_1[0][0][0][-1][0]['_XY_right'][0],tmp1_2[0][0][0][-1][0]['_XY_right'][0])
        tmp2_1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Xgate1','SRF_PMOS','BND_PODummyLayer')
        tmp2_2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Xgate1','SRF_NMOS','BND_PODummyLayer')
        approaching_coordx = min(tmp2_1[0][0][0][0][0]['_XY_left'][0],tmp2_2[0][0][0][0][0]['_XY_left'][0])
        X_Grid7 = np.round( 0.5*(target_coordx+approaching_coordx) )

        tmp1_1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Xgate1','SRF_PMOS','BND_PODummyLayer')
        tmp1_2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Xgate1','SRF_NMOS','BND_PODummyLayer')
        target_coordx = max(tmp1_1[0][0][0][-1][0]['_XY_right'][0],tmp1_2[0][0][0][-1][0]['_XY_right'][0])
        tmp2_1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Xgate2','SRF_PMOS','BND_PODummyLayer')
        tmp2_2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Xgate2','SRF_NMOS','BND_PODummyLayer')
        approaching_coordx = min(tmp2_1[0][0][0][-1][0]['_XY_right'][0],tmp2_2[0][0][0][-1][0]['_XY_right'][0])
        X_Grid8 = np.round( 0.5*(target_coordx+approaching_coordx) )

        tmp1_1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Xgate2','SRF_PMOS','BND_PODummyLayer')
        tmp1_2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Xgate2','SRF_NMOS','BND_PODummyLayer')
        target_coordx = max(tmp1_1[0][0][0][0][0]['_XY_left'][0],tmp1_2[0][0][0][0][0]['_XY_left'][0])
        tmp2_1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Nor1','SRF_Pullup','SRF_PMOSA','BND_PODummyLayer')
        tmp2_2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Nor1','SRF_Pulldown','SRF_NMOSA','BND_PODummyLayer')
        approaching_coordx = min(tmp2_1[0][0][0][0][0][0]['_XY_left'][0],tmp2_2[0][0][0][0][0][0]['_XY_left'][0])
        X_Grid9 = np.round( 0.5*(target_coordx+approaching_coordx) )

        tmp1_1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Nor1','SRF_Pullup','SRF_PMOSB','BND_PODummyLayer')
        tmp1_2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Nor1','SRF_Pulldown','SRF_NMOSB','BND_PODummyLayer')
        target_coordx = max(tmp1_1[0][0][0][0][-1][0]['_XY_right'][0],tmp1_2[0][0][0][0][-1][0]['_XY_right'][0])
        tmp2_1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Nor2','SRF_Pullup','SRF_PMOSA','BND_PODummyLayer')
        tmp2_2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Nor2','SRF_Pulldown','SRF_NMOSA','BND_PODummyLayer')
        approaching_coordx = min(tmp2_1[0][0][0][0][0][0]['_XY_left'][0],tmp2_2[0][0][0][0][0][0]['_XY_left'][0])
        X_Grid10 = np.round( 0.5*(target_coordx+approaching_coordx) )

        tmp1_1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Nor2','SRF_Pullup','SRF_PMOSB','BND_PODummyLayer')
        tmp1_2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Nor2','SRF_Pulldown','SRF_NMOSB','BND_PODummyLayer')
        target_coordx = max(tmp1_1[0][0][0][0][-1][0]['_XY_right'][0],tmp1_2[0][0][0][0][-1][0]['_XY_right'][0])
        tmp2_1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Inv1','SRF_PMOS','BND_PODummyLayer')
        tmp2_2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Inv1','SRF_NMOS','BND_PODummyLayer')
        approaching_coordx = min(tmp2_1[0][0][0][0][0]['_XY_left'][0],tmp2_2[0][0][0][0][0]['_XY_left'][0])
        X_Grid11 = np.round( 0.5*(target_coordx+approaching_coordx) )

        tmp1_1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Inv1','SRF_PMOS','BND_PODummyLayer')
        tmp1_2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Inv1','SRF_NMOS','BND_PODummyLayer')
        target_coordx = max(tmp1_1[0][0][0][-1][0]['_XY_right'][0],tmp1_2[0][0][0][-1][0]['_XY_right'][0])
        tmp2_1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Inv2','SRF_PMOS','BND_PODummyLayer')
        tmp2_2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Inv2','SRF_NMOS','BND_PODummyLayer')
        approaching_coordx = min(tmp2_1[0][0][0][0][0]['_XY_left'][0],tmp2_2[0][0][0][0][0]['_XY_left'][0])
        X_Grid12 = np.round( 0.5*(target_coordx+approaching_coordx) )

        tmp1_1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Inv2','SRF_PMOS','BND_PODummyLayer')
        tmp1_2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Inv2','SRF_NMOS','BND_PODummyLayer')
        target_coordx = max(tmp1_1[0][0][0][-1][0]['_XY_right'][0],tmp1_2[0][0][0][-1][0]['_XY_right'][0])
        tmp2_1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Inv3','SRF_PMOS','BND_PODummyLayer')
        tmp2_2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Inv3','SRF_NMOS','BND_PODummyLayer')
        approaching_coordx = min(tmp2_1[0][0][0][0][0]['_XY_left'][0],tmp2_2[0][0][0][0][0]['_XY_left'][0])
        X_Grid13 = np.round( 0.5*(target_coordx+approaching_coordx) )

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net1
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net1 :  Vtc

            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net1_Vtc_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net1_Vtc_M1']['_YWidth'] = abs(Y_Grid1_up - Y_Grid6_down)

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Net1_Vtc_M1']['_XWidth'] = _Routing_width

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net1_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net1_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate1','SRF_PMOS','BND_Gate_Hrz_Mx')
        target_coord = tmp1[0][0][0][0][0]['_XY_up']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net1_Vtc_M1')
        approaching_coord = tmp2[0][0]['_XY_up']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net1_Vtc_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net1_Vtc_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net1 : Hrz

            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net1_Hrz_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net1_Hrz_M1']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('BND_Net1_Vtc_M1')
        tmp2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate2','SRF_NMOS','BND_Gate_Hrz_Mx')

        self._DesignParameter['BND_Net1_Hrz_M1']['_XWidth'] = abs( tmp2[0][0][0][0][0]['_XY_right'][0]- tmp1[0][0]['_XY_left'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net1_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net1_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_Net1_Vtc_M1')
        target_coord = tmp1[0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net1_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net1_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net1_Hrz_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net1 : Vtc1

            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net1_Vtc1_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net1_Vtc1_M1']['_YWidth'] = Y_Grid6_up - Y_Grid8_down

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Net1_Vtc1_M1']['_XWidth'] = 50

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net1_Vtc1_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net1_Vtc1_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_Net1_Hrz_M1')
        target_coord = tmp1[0][0]['_XY_up_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net1_Vtc1_M1')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net1_Vtc1_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net1_Vtc1_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net1_1
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net1_1 :  Vtc

            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net1_1_Vtc_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net1_1_Vtc_M1']['_YWidth'] = Y_Grid1_up - Y_Grid6_down

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Net1_1_Vtc_M1']['_XWidth'] = _Routing_width

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net1_1_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net1_1_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Xgate1','SRF_PMOS','BND_Gate_Hrz_Mx')
        target_coord = tmp1[0][0][0][0][0]['_XY_up']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net1_1_Vtc_M1')
        approaching_coord = tmp2[0][0]['_XY_up']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net1_1_Vtc_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net1_1_Vtc_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : Net1_1_1 : Hrz

            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net1_1_Hrz_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net1_1_Hrz_M1']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('BND_Net1_1_Vtc_M1')
        tmp2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Xgate2','SRF_NMOS','BND_Gate_Hrz_Mx')

        self._DesignParameter['BND_Net1_1_Hrz_M1']['_XWidth'] = abs( tmp2[0][0][0][0][0]['_XY_right'][0]- tmp1[0][0]['_XY_left'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net1_1_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net1_1_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_Net1_1_Vtc_M1')
        target_coord = tmp1[0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net1_1_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net1_1_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net1_1_Hrz_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : Net1_1_1 : Vtc1

            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net1_1_Vtc1_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net1_1_Vtc1_M1']['_YWidth'] = Y_Grid6_up - Y_Grid8_down

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Net1_1_Vtc1_M1']['_XWidth'] = 50

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net1_1_Vtc1_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net1_1_Vtc1_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_Net1_1_Hrz_M1')
        target_coord = tmp1[0][0]['_XY_up_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net1_1_Vtc1_M1')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net1_1_Vtc1_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net1_1_Vtc1_M1']['_XYCoordinates'] = tmpXY






        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net2
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net2 : M1 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net2_Hrz_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net2_Hrz_M1']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate2','SRF_PMOS','BND_Gate_Hrz_Mx')
        self._DesignParameter['BND_Net2_Hrz_M1']['_XWidth'] = abs(X_Grid1 - tmp[0][0][0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net2_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net2_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate2','SRF_PMOS','BND_Gate_Hrz_Mx')
        target_coord = tmp1[0][0][0][0][0]['_XY_up_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net2_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net2_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net2_Hrz_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net2 : ViaM1M4
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net2_ViaM1M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net2_ViaM1M4'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net2_ViaM1M4']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net2_ViaM1M4']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net2_ViaM1M4']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net2_ViaM1M4']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid1
                        ## Y
        target_coordy = Y_Grid1_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net2_ViaM1M4','SRF_ViaM3M4','BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net2_ViaM1M4')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net2_ViaM1M4']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net2 : M4 Vtc
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net2_Vtc_M4'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL4'][0],
        _Datatype=DesignParameters._LayerMapping['METAL4'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net2_Vtc_M4']['_YWidth'] = Y_Grid1_up - Y_Grid8_down

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Net2_Vtc_M4']['_XWidth'] = 50

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net2_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net2_Vtc_M4']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                        ## X
        target_coordx = X_Grid1
                        ## Y
        target_coordy = Y_Grid1_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net2_Vtc_M4')
        approaching_coord = tmp2[0][0]['_XY_up']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net2_Vtc_M4')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net2_Vtc_M4']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net2 : ViaM1M4
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net2_ViaM1M4_1'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net2_ViaM1M4_1'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net2_ViaM1M4_1']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net2_ViaM1M4_1']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net2_ViaM1M4_1']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net2_ViaM1M4_1']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid1
                        ## Y
        target_coordy = Y_Grid8_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net2_ViaM1M4_1','SRF_ViaM3M4','BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net2_ViaM1M4_1')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net2_ViaM1M4_1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net2 : M1 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net2_Hrz1_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net2_Hrz1_M1']['_YWidth'] = 50

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate1','SRF_NMOS','BND_Gate_Hrz_Mx')
        self._DesignParameter['BND_Net2_Hrz1_M1']['_XWidth'] = abs(X_Grid1 - tmp[0][0][0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net2_Hrz1_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net2_Hrz1_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_Net2_Vtc_M4')
        target_coord = tmp1[0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net2_Hrz1_M1')
        approaching_coord = tmp2[0][0]['_XY_down_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net2_Hrz1_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net2_Hrz1_M1']['_XYCoordinates'] = tmpXY




        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : Net2_1
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : Net2_1 : M1 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net2_1_Hrz_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net2_1_Hrz_M1']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Xgate2','SRF_PMOS','BND_Gate_Hrz_Mx')
        self._DesignParameter['BND_Net2_1_Hrz_M1']['_XWidth'] = abs(X_Grid8 - tmp[0][0][0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net2_1_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net2_1_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Xgate2','SRF_PMOS','BND_Gate_Hrz_Mx')
        target_coord = tmp1[0][0][0][0][0]['_XY_up_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net2_1_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net2_1_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net2_1_Hrz_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : Net2_1 : ViaM1M4
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net2_1_ViaM1M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net2_1_ViaM1M4'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net2_1_ViaM1M4']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net2_1_ViaM1M4']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net2_1_ViaM1M4']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net2_1_ViaM1M4']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid8
                        ## Y
        target_coordy = Y_Grid1_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net2_1_ViaM1M4','SRF_ViaM3M4','BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net2_1_ViaM1M4')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net2_1_ViaM1M4']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : Net2_1 : M4 Vtc
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net2_1_Vtc_M4'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL4'][0],
        _Datatype=DesignParameters._LayerMapping['METAL4'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net2_1_Vtc_M4']['_YWidth'] = Y_Grid1_up - Y_Grid8_down

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Net2_1_Vtc_M4']['_XWidth'] = _Routing_width

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net2_1_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net2_1_Vtc_M4']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                        ## X
        target_coordx = X_Grid8
                        ## Y
        target_coordy = Y_Grid1_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net2_1_Vtc_M4')
        approaching_coord = tmp2[0][0]['_XY_up']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net2_1_Vtc_M4')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net2_1_Vtc_M4']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : Net2_1 : ViaM1M4
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net2_1_ViaM1M4_1'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net2_1_ViaM1M4_1'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net2_1_ViaM1M4_1']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net2_1_ViaM1M4_1']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net2_1_ViaM1M4_1']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net2_1_ViaM1M4_1']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid8
                        ## Y
        target_coordy = Y_Grid8_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net2_1_ViaM1M4_1','SRF_ViaM3M4','BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net2_1_ViaM1M4_1')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net2_1_ViaM1M4_1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : Net2_1 : M1 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net2_1_Hrz1_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net2_1_Hrz1_M1']['_YWidth'] = 50

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Xgate1','SRF_NMOS','BND_Gate_Hrz_Mx')
        self._DesignParameter['BND_Net2_1_Hrz1_M1']['_XWidth'] = abs(X_Grid8 - tmp[0][0][0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net2_1_Hrz1_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net2_1_Hrz1_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_Net2_1_Vtc_M4')
        target_coord = tmp1[0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net2_1_Hrz1_M1')
        approaching_coord = tmp2[0][0]['_XY_down_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net2_1_Hrz1_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net2_1_Hrz1_M1']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net3
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net3 : M1 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net3_Hrz_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net3_Hrz_M1']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Inv3','SRF_PMOS','BND_Gate_Hrz_Mx')
        self._DesignParameter['BND_Net3_Hrz_M1']['_XWidth'] = abs(X_Grid6 - tmp[0][0][0][0][0]['_XY_left'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net3_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net3_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Inv3','SRF_PMOS','BND_Gate_Hrz_Mx')
        target_coord = tmp1[0][0][0][0][0]['_XY_up_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net3_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net3_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net3_Hrz_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net3 : ViaM1M4
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net3_ViaM1M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net3_ViaM1M4'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net3_ViaM1M4']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net3_ViaM1M4']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net3_ViaM1M4']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net3_ViaM1M4']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid6
                        ## Y
        target_coordy = Y_Grid1_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net3_ViaM1M4','SRF_ViaM3M4','BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net3_ViaM1M4')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net3_ViaM1M4']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net4
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net4 : M2 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net4_Hrz_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net4_Hrz_M2']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Inv3','BND_Out_Vtc_M2')
        self._DesignParameter['BND_Net4_Hrz_M2']['_XWidth'] = abs( tmp1[0][0][0][0]['_XY_left'][0] - X_Grid7)

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net4_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net4_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        target_coordx = X_Grid7
                                ##y
        target_coordy = Y_Grid1_up
        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net4_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net4_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net4_Hrz_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net4 : ViaM1M2
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net4_ViaM1M2'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net4_ViaM1M2'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net4_ViaM1M2']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net4_ViaM1M2']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net4_ViaM1M2']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net4_ViaM1M2']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid7
                        ## Y
        target_coordy = Y_Grid1_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net4_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net4_ViaM1M2')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net4_ViaM1M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net4 : M1 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net4_Hrz1_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net4_Hrz1_M1']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Xgate1','SRF_PMOS','BND_Gate_Hrz_Mx')
        self._DesignParameter['BND_Net4_Hrz1_M1']['_XWidth'] = abs( tmp1[0][0][0][0][0]['_XY_left'][0] - X_Grid7)

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net4_Hrz1_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net4_Hrz1_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        target_coordx = X_Grid7
                                ##y
        target_coordy = Y_Grid1_up
        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net4_Hrz1_M1')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net4_Hrz1_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net4_Hrz1_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net5
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net5 : M1 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net5_Hrz_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net5_Hrz_M1']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Inv3','BND_Input_Vtc_M1')
        self._DesignParameter['BND_Net5_Hrz_M1']['_XWidth'] = abs(X_Grid7 - tmp[0][0][0][0]['_XY_left'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net5_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net5_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Inv3','BND_Input_Vtc_M1')
        target_coordx = tmp1[0][0][0][0]['_XY_left'][0]
                            ##Y
        target_coordy = Y_Grid7_up
        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net5_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net5_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net5_Hrz_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net5 : M1 Vtc
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net5_Vtc_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net5_Vtc_M1']['_YWidth'] = Y_Grid7_up - Y_Grid8_down

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Net5_Vtc_M1']['_XWidth'] = _Routing_width

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net5_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net5_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        target_coordx = X_Grid7
                                ##Y
        target_coordy = Y_Grid7_up
        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net5_Vtc_M1')
        approaching_coord = tmp2[0][0]['_XY_up']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net5_Vtc_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net5_Vtc_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net5 : M1 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net5_Hrz1_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net5_Hrz1_M1']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Xgate1','SRF_NMOS','BND_Gate_Hrz_Mx')
        self._DesignParameter['BND_Net5_Hrz1_M1']['_XWidth'] = abs(X_Grid7 - tmp[0][0][0][0][0]['_XY_left'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net5_Hrz1_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net5_Hrz1_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        target_coordx = X_Grid7
                                ##Y
        target_coordy = Y_Grid8_up
        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net5_Hrz1_M1')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net5_Hrz1_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net5_Hrz1_M1']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net6
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net6 : M1 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net6_Hrz_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net6_Hrz_M1']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate2','SRF_PMOS','BND_Gate_Hrz_Mx')
        self._DesignParameter['BND_Net6_Hrz_M1']['_XWidth'] = abs(X_Grid2 - tmp[0][0][0][0][0]['_XY_left'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net6_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net6_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate2','SRF_PMOS','BND_Gate_Hrz_Mx')
        target_coord = tmp1[0][0][0][0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net6_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net6_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net6_Hrz_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net6 : M1 Vtc
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net6_Vtc_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net6_Vtc_M1']['_YWidth'] = abs(Y_Grid1_up - Y_Grid2_down)

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Net6_Vtc_M1']['_XWidth'] = _Routing_width

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net6_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net6_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        ## X
        target_coordx = X_Grid2
        ## Y
        target_coordy = Y_Grid1_up

        target_coord = [target_coordx, target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net6_Vtc_M1')
        approaching_coord = tmp2[0][0]['_XY_up']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net6_Vtc_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net6_Vtc_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net6 : ViaM1M3
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net6_ViaM1M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net6_ViaM1M3'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net6_ViaM1M3']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net6_ViaM1M3']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net6_ViaM1M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net6_ViaM1M3']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid2
                        ## Y
        target_coordy = Y_Grid2_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net6_ViaM1M3','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net6_ViaM1M3')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net6_ViaM1M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net6 : M3 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net6_Hrz1_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net6_Hrz1_M3']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Net6_Hrz1_M3']['_XWidth'] = abs(X_Grid2 - X_Grid6)

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net6_Hrz1_M3']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net6_Hrz1_M3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid2
                            ##Y
        target_coordy = Y_Grid2_up
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net6_Hrz1_M3')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net6_Hrz1_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net6_Hrz1_M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net6 : ViaM1M3
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net6_ViaM2M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net6_ViaM2M3'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net6_ViaM2M3']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net6_ViaM2M3']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net6_ViaM2M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net6_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid6
                        ## Y
        target_coordy = Y_Grid2_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net6_ViaM2M3','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net6_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net6_ViaM2M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net6 : M2 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net6_Hrz2_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net6_Hrz2_M2']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Inv3','BND_Out_Vtc_M2')
        self._DesignParameter['BND_Net6_Hrz2_M2']['_XWidth'] = abs(X_Grid6 - tmp[0][0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net6_Hrz2_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net6_Hrz2_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_Net6_Hrz1_M3')
        target_coord = tmp1[0][0]['_XY_down_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net6_Hrz2_M2')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net6_Hrz2_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net6_Hrz2_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net7
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net7 : M1 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net7_Hrz_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net7_Hrz_M1']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate2','SRF_NMOS','BND_Gate_Hrz_Mx')
        self._DesignParameter['BND_Net7_Hrz_M1']['_XWidth'] = abs(X_Grid2 - tmp[0][0][0][0][0]['_XY_left'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net7_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net7_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid2
                            ##Y
        target_coordy = Y_Grid8_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net7_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net7_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net7_Hrz_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net7 : M1 Vtc
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net7_Vtc_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net7_Vtc_M1']['_YWidth'] = abs( Y_Grid7_up - Y_Grid8_down)

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Net7_Vtc_M1']['_XWidth'] = _Routing_width

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net7_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net7_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid2
                            ##Y
        target_coordy = Y_Grid8_down

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net7_Vtc_M1')
        approaching_coord = tmp2[0][0]['_XY_down']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net7_Vtc_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net7_Vtc_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net7 : ViaM1M3
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net7_ViaM1M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net7_ViaM1M3'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net7_ViaM1M3']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net7_ViaM1M3']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net7_ViaM1M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net7_ViaM1M3']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid2
                        ## Y
        target_coordy = Y_Grid7_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net7_ViaM1M3','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net7_ViaM1M3')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net7_ViaM1M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net7 : M3 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net7_Hrz1_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net7_Hrz1_M3']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Net7_Hrz1_M3']['_XWidth'] = abs(X_Grid2 - X_Grid6)

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net7_Hrz1_M3']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net7_Hrz1_M3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid2
                            ##Y
        target_coordy = Y_Grid7_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net7_Hrz1_M3')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net7_Hrz1_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net7_Hrz1_M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net7 : ViaM1M3
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net7_ViaM1M3_1'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net7_ViaM1M3_1'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net7_ViaM1M3_1']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net7_ViaM1M3_1']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net7_ViaM1M3_1']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net7_ViaM1M3_1']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid6
                        ## Y
        target_coordy = Y_Grid7_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net7_ViaM1M3_1','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net7_ViaM1M3_1')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net7_ViaM1M3_1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net7 : M1 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net7_Hrz2_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net7_Hrz2_M1']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Inv3','BND_Input_Vtc_M1')
        self._DesignParameter['BND_Net7_Hrz2_M1']['_XWidth'] = abs(tmp[0][0][0][0]['_XY_right'][0] - X_Grid6)

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net7_Hrz2_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net7_Hrz2_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid6
                            ##Y
        target_coordy = Y_Grid7_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net7_Hrz2_M1')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net7_Hrz2_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net7_Hrz2_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net8
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net8 : M1 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net8_Hrz_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net8_Hrz_M1']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Inv1','SRF_PMOS','BND_Gate_Hrz_Mx')
        self._DesignParameter['BND_Net8_Hrz_M1']['_XWidth'] = abs (X_Grid4 - tmp[0][0][0][0][0]['_XY_left'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net8_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net8_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid4
                            ##Y
        target_coordy = Y_Grid1_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net8_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net8_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net8_Hrz_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net8 : ViaM1M4
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net8_ViaM1M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net8_ViaM1M4'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net8_ViaM1M4']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net8_ViaM1M4']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net8_ViaM1M4']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net8_ViaM1M4']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid4
                        ## Y
        target_coordy = Y_Grid1_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net8_ViaM1M4','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net8_ViaM1M4')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net8_ViaM1M4']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net9
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net9 : M2 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net9_Hrz_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net9_Hrz_M2']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Inv1','BND_Out_Vtc_M2')
        self._DesignParameter['BND_Net9_Hrz_M2']['_XWidth'] = abs (X_Grid5 - tmp[0][0][0][0]['_XY_left'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net9_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net9_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid5
                            ##Y
        target_coordy = Y_Grid1_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net9_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net9_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net9_Hrz_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net9 : ViaM1M2
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net9_ViaM1M2'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net9_ViaM1M2'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net9_ViaM1M2']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net9_ViaM1M2']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net9_ViaM1M2']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net9_ViaM1M2']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid5
                        ## Y
        target_coordy = Y_Grid1_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net9_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net9_ViaM1M2')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net9_ViaM1M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net9 : M1 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net9_Hrz1_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net9_Hrz1_M1']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Inv2','BND_Input_Vtc_M1')
        self._DesignParameter['BND_Net9_Hrz1_M1']['_XWidth'] = abs (X_Grid5 - tmp[0][0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net9_Hrz1_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net9_Hrz1_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid5
                            ##Y
        target_coordy = Y_Grid1_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net9_Hrz1_M1')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net9_Hrz1_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net9_Hrz1_M1']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net10
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net10 : M2 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net10_Hrz_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net10_Hrz_M2']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Inv2','BND_Out_Vtc_M2')
        self._DesignParameter['BND_Net10_Hrz_M2']['_XWidth'] = abs (X_Grid5 - tmp[0][0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net10_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net10_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid5
                            ##Y
        target_coordy = Y_Grid3_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net10_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net10_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net10_Hrz_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net10 : ViaM2M3
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net10_ViaM2M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net10_ViaM2M3'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net10_ViaM2M3']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net10_ViaM2M3']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net10_ViaM2M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net10_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid5
                        ## Y
        target_coordy = Y_Grid3_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net10_ViaM2M3','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net10_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net10_ViaM2M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net10 : M3 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net10_Hrz1_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net10_Hrz1_M3']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Net10_Hrz1_M3']['_XWidth'] = abs (X_Grid5 - X_Grid3)

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net10_Hrz1_M3']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net10_Hrz1_M3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid5
                            ##Y
        target_coordy = Y_Grid3_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net10_Hrz1_M3')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net10_Hrz1_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net10_Hrz1_M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net10 : ViaM1M3
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net10_ViaM1M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net10_ViaM1M3'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net10_ViaM1M3']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net10_ViaM1M3']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net10_ViaM1M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net10_ViaM1M3']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid3
                        ## Y
        target_coordy = Y_Grid3_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net10_ViaM1M3','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net10_ViaM1M3')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net10_ViaM1M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net10 : M1 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net10_Hrz2_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net10_Hrz2_M1']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Nor1','BND_InputB_Vtc_M1')
        self._DesignParameter['BND_Net10_Hrz2_M1']['_XWidth'] = abs(tmp[0][0][0][0]['_XY_left'][0] - X_Grid3)

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net10_Hrz2_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net10_Hrz2_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid3
                            ##Y
        target_coordy = Y_Grid3_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net10_Hrz2_M1')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net10_Hrz2_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net10_Hrz2_M1']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net11
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net11 : M3 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net11_Hrz_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net11_Hrz_M3']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Net11_Hrz_M3']['_XWidth'] = abs (X_Grid5 - X_Grid10)

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net11_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net11_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid5
                            ##Y
        target_coordy = Y_Grid3_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net11_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net11_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net11_Hrz_M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net11 : ViaM1M3
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net11_ViaM1M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net11_ViaM1M3'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net11_ViaM1M3']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net11_ViaM1M3']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net11_ViaM1M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net11_ViaM1M3']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid10
                        ## Y
        target_coordy = Y_Grid3_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net11_ViaM1M3','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net11_ViaM1M3')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net11_ViaM1M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net11 : M1 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net11_Hrz1_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net11_Hrz1_M1']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Nor2','BND_InputA_Vtc_M1')
        self._DesignParameter['BND_Net11_Hrz1_M1']['_XWidth'] = abs (X_Grid10 - tmp[0][0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net11_Hrz1_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net11_Hrz1_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid10
                            ##Y
        target_coordy = Y_Grid3_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net11_Hrz1_M1')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net11_Hrz1_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net11_Hrz1_M1']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net12
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net12 : M1 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net12_Hrz_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net12_Hrz_M1']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Inv1','BND_Input_Vtc_M1')
        self._DesignParameter['BND_Net12_Hrz_M1']['_XWidth'] = abs (tmp[0][0][0][0]['_XY_right'][0] - X_Grid11)

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net12_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net12_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid11
                            ##Y
        target_coordy = Y_Grid1_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net12_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net12_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net12_Hrz_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net12 : ViaM1M4
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net12_ViaM1M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net12_ViaM1M4'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net12_ViaM1M4']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net12_ViaM1M4']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net12_ViaM1M4']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net12_ViaM1M4']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid11
                        ## Y
        target_coordy = Y_Grid1_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net12_ViaM1M4','SRF_ViaM3M4','BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net12_ViaM1M4')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net12_ViaM1M4']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net13
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net13 : M2 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net13_Hrz_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net13_Hrz_M2']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp =self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Inv1','BND_Out_Vtc_M2')
        self._DesignParameter['BND_Net13_Hrz_M2']['_XWidth'] = abs (tmp[0][0][0][0]['_XY_left'][0] - X_Grid12)

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net13_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net13_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid12
                            ##Y
        target_coordy = Y_Grid1_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net13_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net13_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net13_Hrz_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net13 : ViaM1M2
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net13_ViaM1M2'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net13_ViaM1M2'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net13_ViaM1M2']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net13_ViaM1M2']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net13_ViaM1M2']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net13_ViaM1M2']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid12
                        ## Y
        target_coordy = Y_Grid1_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net13_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net13_ViaM1M2')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net13_ViaM1M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net13 : M1 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net13_Hrz1_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net13_Hrz1_M1']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp =self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Inv2','BND_Input_Vtc_M1')
        self._DesignParameter['BND_Net13_Hrz1_M1']['_XWidth'] = abs (tmp[0][0][0][0]['_XY_right'][0] - X_Grid12)

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net13_Hrz1_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net13_Hrz1_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid12
                            ##Y
        target_coordy = Y_Grid1_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net13_Hrz1_M1')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net13_Hrz1_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net13_Hrz1_M1']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net14
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net14 : M2 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net14_Hrz_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net14_Hrz_M2']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp =self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Inv2','BND_Out_Vtc_M2')
        self._DesignParameter['BND_Net14_Hrz_M2']['_XWidth'] = abs (tmp[0][0][0][0]['_XY_right'][0] - X_Grid12)

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net14_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net14_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid12
                            ##Y
        target_coordy = Y_Grid6_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net14_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net14_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net14_Hrz_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net14 : ViaM2M3
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net14_ViaM2M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net14_ViaM2M3'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net14_ViaM2M3']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net14_ViaM2M3']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net14_ViaM2M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net14_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid12
                        ## Y
        target_coordy = Y_Grid6_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net14_ViaM2M3','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net14_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net14_ViaM2M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net14 : M3 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net14_Hrz1_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net14_Hrz1_M3']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Net14_Hrz1_M3']['_XWidth'] = abs (X_Grid10 - X_Grid12)

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net14_Hrz1_M3']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net14_Hrz1_M3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid12
                            ##Y
        target_coordy = Y_Grid6_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net14_Hrz1_M3')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net14_Hrz1_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net14_Hrz1_M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net14 : ViaM1M3
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net14_ViaM1M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net14_ViaM1M3'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net14_ViaM1M3']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net14_ViaM1M3']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net14_ViaM1M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net14_ViaM1M3']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid10
                        ## Y
        target_coordy = Y_Grid6_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net14_ViaM1M3','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net14_ViaM1M3')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net14_ViaM1M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net14 : M1 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net14_Hrz2_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net14_Hrz2_M1']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Nor1','BND_InputB_Vtc_M1')
        self._DesignParameter['BND_Net14_Hrz2_M1']['_XWidth'] = abs (tmp[0][0][0][0]['_XY_left'][0] - X_Grid10)

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net14_Hrz2_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net14_Hrz2_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid10
                            ##Y
        target_coordy = Y_Grid6_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net14_Hrz2_M1')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net14_Hrz2_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net14_Hrz2_M1']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net15
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net15 : M3 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net15_Hrz_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net15_Hrz_M3']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Net15_Hrz_M3']['_XWidth'] = abs (X_Grid10 - X_Grid3)

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net15_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net15_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid10
                            ##Y
        target_coordy = Y_Grid6_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net15_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net15_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net15_Hrz_M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net15 : ViaM1M3
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net15_ViaM1M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net15_ViaM1M3'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net15_ViaM1M3']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net15_ViaM1M3']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net15_ViaM1M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net15_ViaM1M3']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid3
                        ## Y
        target_coordy = Y_Grid6_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net15_ViaM1M3','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net15_ViaM1M3')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net15_ViaM1M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net15 : M1 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net15_Hrz1_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net15_Hrz1_M1']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Nor2','BND_InputA_Vtc_M1')
        self._DesignParameter['BND_Net15_Hrz1_M1']['_XWidth'] = abs (tmp[0][0][0][0]['_XY_right'][0] - X_Grid3)

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net15_Hrz1_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net15_Hrz1_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid3
                            ##Y
        target_coordy = Y_Grid6_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net15_Hrz1_M1')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net15_Hrz1_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net15_Hrz1_M1']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net16
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net16 : M2 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net16_Hrz_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net16_Hrz_M2']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate1','BND_Output_Vtc_M2')
        tmp2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate2','BND_Output_Vtc_M2')
        self._DesignParameter['BND_Net16_Hrz_M2']['_XWidth'] = abs ( tmp1[0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0]['_XY_left'][0]  )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net16_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net16_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement', 'SRF_Mst_Xgate1', 'BND_Output_Vtc_M2')
        target_coordx = tmp1[0][0][0][0]['_XY_left'][0]
                            ##Y
        target_coordy = Y_Grid4_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net16_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net16_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net16_Hrz_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net16_1
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net16 : M2 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net16_1_Hrz_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net16_1_Hrz_M2']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Xgate1','BND_Output_Vtc_M2')
        tmp2 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Xgate2','BND_Output_Vtc_M2')
        self._DesignParameter['BND_Net16_1_Hrz_M2']['_XWidth'] = abs ( tmp1[0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0]['_XY_left'][0]  )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net16_1_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net16_1_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement', 'SRF_Slv_Xgate1', 'BND_Output_Vtc_M2')
        target_coordx = tmp1[0][0][0][0]['_XY_left'][0]
                            ##Y
        target_coordy = Y_Grid4_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net16_1_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net16_1_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net16_1_Hrz_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net17
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net17 : ViaM1M2
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net17_ViaM1M2'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net17_ViaM1M2'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net17_ViaM1M2']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net17_ViaM1M2']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net17_ViaM1M2']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net17_ViaM1M2']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid1
                        ## Y
        target_coordy = Y_Grid4_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net17_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net17_ViaM1M2')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net17_ViaM1M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net17 : M1 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net17_Hrz_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net17_Hrz_M1']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Nor1','BND_InputA_Vtc_M1')
        self._DesignParameter['BND_Net17_Hrz_M1']['_XWidth'] = abs ( tmp1[0][0][0][0]['_XY_right'][0] - X_Grid1  )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net17_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net17_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid1
                            ##Y
        target_coordy = Y_Grid4_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net17_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net17_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net17_Hrz_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net17_1
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net17_1 : ViaM1M2
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net17_1_ViaM1M2'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net17_1_ViaM1M2'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net17_1_ViaM1M2']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net17_1_ViaM1M2']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net17_1_ViaM1M2']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net17_1_ViaM1M2']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid8
                        ## Y
        target_coordy = Y_Grid4_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net17_1_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net17_1_ViaM1M2')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net17_1_ViaM1M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net17_1 : M1 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net17_1_Hrz_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net17_1_Hrz_M1']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Nor1','BND_InputA_Vtc_M1')
        self._DesignParameter['BND_Net17_1_Hrz_M1']['_XWidth'] = abs ( tmp1[0][0][0][0]['_XY_right'][0] - X_Grid8  )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net17_1_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net17_1_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid8
                            ##Y
        target_coordy = Y_Grid4_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net17_1_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net17_1_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net17_1_Hrz_M1']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net18
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net18 : M2 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net18_Hrz_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net18_Hrz_M2']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Nor1','BND_Out_Vtc_M2')
        self._DesignParameter['BND_Net18_Hrz_M2']['_XWidth'] = abs ( tmp1[0][0][0][0]['_XY_left'][0] - X_Grid3  )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net18_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net18_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid3
                            ##Y
        target_coordy = Y_Grid4_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net18_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net18_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net18_Hrz_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net18 : ViaM2M3
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net18_ViaM2M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net18_ViaM2M3'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net18_ViaM2M3']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net18_ViaM2M3']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net18_ViaM2M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net18_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid3
                        ## Y
        target_coordy = Y_Grid4_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net18_ViaM2M3','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net18_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net18_ViaM2M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net18 : M3 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net18_Hrz1_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net18_Hrz1_M3']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Net18_Hrz1_M3']['_XWidth'] = abs ( X_Grid4 - X_Grid3  )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net18_Hrz1_M3']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net18_Hrz1_M3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid3
                            ##Y
        target_coordy = Y_Grid4_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net18_Hrz1_M3')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net18_Hrz1_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net18_Hrz1_M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net18 : ViaM1M3
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net18_ViaM1M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net18_ViaM1M3'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net18_ViaM1M3']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net18_ViaM1M3']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net18_ViaM1M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net18_ViaM1M3']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid4
                        ## Y
        target_coordy = Y_Grid4_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net18_ViaM1M3','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net18_ViaM1M3')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net18_ViaM1M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net18 : M1 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net18_Hrz2_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net18_Hrz2_M1']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Nor2','BND_InputB_Vtc_M1')
        self._DesignParameter['BND_Net18_Hrz2_M1']['_XWidth'] = abs ( X_Grid4 - tmp[0][0][0][0]['_XY_left'][0]  )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net18_Hrz2_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net18_Hrz2_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid4
                            ##Y
        target_coordy = Y_Grid4_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net18_Hrz2_M1')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net18_Hrz2_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net18_Hrz2_M1']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net18_1
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net18_1 : M2 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net18_1_Hrz_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net18_1_Hrz_M2']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Nor1','BND_Out_Vtc_M2')
        self._DesignParameter['BND_Net18_1_Hrz_M2']['_XWidth'] = abs ( tmp1[0][0][0][0]['_XY_left'][0] - X_Grid10  )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net18_1_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net18_1_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid10
                            ##Y
        target_coordy = Y_Grid4_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net18_1_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net18_1_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net18_1_Hrz_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net18 : ViaM2M3
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net18_1_ViaM2M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net18_1_ViaM2M3'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net18_1_ViaM2M3']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net18_1_ViaM2M3']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net18_1_ViaM2M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net18_1_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid10
                        ## Y
        target_coordy = Y_Grid4_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net18_1_ViaM2M3','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net18_1_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net18_1_ViaM2M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net18 : M3 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net18_1_Hrz1_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net18_1_Hrz1_M3']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Net18_1_Hrz1_M3']['_XWidth'] = abs ( X_Grid11- X_Grid10  )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net18_1_Hrz1_M3']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net18_1_Hrz1_M3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid10
                            ##Y
        target_coordy = Y_Grid4_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net18_1_Hrz1_M3')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net18_1_Hrz1_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net18_1_Hrz1_M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net18 : ViaM1M3
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net18_1_ViaM1M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net18_1_ViaM1M3'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net18_1_ViaM1M3']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net18_1_ViaM1M3']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net18_1_ViaM1M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net18_1_ViaM1M3']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid11
                        ## Y
        target_coordy = Y_Grid4_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net18_1_ViaM1M3','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net18_1_ViaM1M3')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net18_1_ViaM1M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net18 : M1 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net18_1_Hrz2_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net18_1_Hrz2_M1']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Nor2','BND_InputB_Vtc_M1')
        self._DesignParameter['BND_Net18_1_Hrz2_M1']['_XWidth'] = abs ( X_Grid11 - tmp[0][0][0][0]['_XY_left'][0]  )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net18_1_Hrz2_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net18_1_Hrz2_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid11
                            ##Y
        target_coordy = Y_Grid4_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net18_1_Hrz2_M1')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net18_1_Hrz2_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net18_1_Hrz2_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net19
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net19 : M2 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net19_Hrz_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net19_Hrz_M2']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Nor2','BND_Out_Vtc_M2')
        self._DesignParameter['BND_Net19_Hrz_M2']['_XWidth'] = abs ( tmp1[0][0][0][0]['_XY_left'][0] - X_Grid4  )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net19_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net19_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid4
                            ##Y
        target_coordy = Y_Grid5_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net19_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net19_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net19_Hrz_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net19 : ViaM2M3
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net19_ViaM2M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net19_ViaM2M3'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net19_ViaM2M3']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net19_ViaM2M3']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net19_ViaM2M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net19_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid4
                        ## Y
        target_coordy = Y_Grid5_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net19_ViaM2M3','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net19_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net19_ViaM2M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net19 : M3 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net19_Hrz1_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net19_Hrz1_M3']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Net19_Hrz1_M3']['_XWidth'] = abs ( X_Grid4 - X_Grid2  )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net19_Hrz1_M3']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net19_Hrz1_M3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid4
                            ##Y
        target_coordy = Y_Grid5_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net19_Hrz1_M3')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net19_Hrz1_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net19_Hrz1_M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net19 : ViaM2M3
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net19_ViaM2M3_1'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net19_ViaM2M3_1'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net19_ViaM2M3_1']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net19_ViaM2M3_1']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net19_ViaM2M3_1']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net19_ViaM2M3_1']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid2
                        ## Y
        target_coordy = Y_Grid5_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net19_ViaM2M3_1','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net19_ViaM2M3_1')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net19_ViaM2M3_1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net19 : M2 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net19_Hrz2_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net19_Hrz2_M2']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Mst_Xgate2','BND_Input_Vtc_M2')
        self._DesignParameter['BND_Net19_Hrz2_M2']['_XWidth'] = abs ( X_Grid2 - tmp[0][0][0][0]['_XY_right'][0]  )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net19_Hrz2_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net19_Hrz2_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid2
                            ##Y
        target_coordy = Y_Grid5_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net19_Hrz2_M2')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net19_Hrz2_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net19_Hrz2_M2']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net19_1
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net19_1 : M2 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net19_1_Hrz_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net19_1_Hrz_M2']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Nor2','BND_Out_Vtc_M2')
        self._DesignParameter['BND_Net19_1_Hrz_M2']['_XWidth'] = abs ( tmp1[0][0][0][0]['_XY_left'][0] - X_Grid11  )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net19_1_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net19_1_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid11
                            ##Y
        target_coordy = Y_Grid5_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net19_1_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net19_1_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net19_1_Hrz_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net19_1 : ViaM2M3
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net19_1_ViaM2M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net19_1_ViaM2M3'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net19_1_ViaM2M3']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net19_1_ViaM2M3']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net19_1_ViaM2M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net19_1_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid11
                        ## Y
        target_coordy = Y_Grid5_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net19_1_ViaM2M3','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net19_1_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net19_1_ViaM2M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net19 : M3 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net19_1_Hrz1_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net19_1_Hrz1_M3']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Net19_1_Hrz1_M3']['_XWidth'] = abs ( X_Grid11 - X_Grid9  )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net19_1_Hrz1_M3']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net19_1_Hrz1_M3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid11
                            ##Y
        target_coordy = Y_Grid5_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net19_1_Hrz1_M3')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net19_1_Hrz1_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net19_1_Hrz1_M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net19 : ViaM2M3
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net19_1_ViaM2M3_1'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net19_1_ViaM2M3_1'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net19_1_ViaM2M3_1']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net19_1_ViaM2M3_1']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net19_1_ViaM2M3_1']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net19_1_ViaM2M3_1']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid9
                        ## Y
        target_coordy = Y_Grid5_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net19_1_ViaM2M3_1','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net19_1_ViaM2M3_1')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net19_1_ViaM2M3_1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net19 : M2 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net19_1_Hrz2_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net19_1_Hrz2_M2']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Xgate2','BND_Input_Vtc_M2')
        self._DesignParameter['BND_Net19_1_Hrz2_M2']['_XWidth'] = abs ( X_Grid9 - tmp[0][0][0][0]['_XY_right'][0]  )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net19_1_Hrz2_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net19_1_Hrz2_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid9
                            ##Y
        target_coordy = Y_Grid5_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net19_1_Hrz2_M2')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net19_1_Hrz2_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net19_1_Hrz2_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net20
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net20 : M3 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net20_Hrz_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net20_Hrz_M3']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Net20_Hrz_M3']['_XWidth'] = abs ( X_Grid7 - X_Grid4  )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net20_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net20_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid4
                            ##Y
        target_coordy = Y_Grid4_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net20_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net20_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net20_Hrz_M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net20 : ViaM2M3
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net20_ViaM2M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net20_ViaM2M3'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net20_ViaM2M3']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net20_ViaM2M3']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net20_ViaM2M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net20_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid7
                        ## Y
        target_coordy = Y_Grid4_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net20_ViaM2M3','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net20_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net20_ViaM2M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net20 : M3 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net20_Hrz1_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net20_Hrz1_M2']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Xgate1','BND_Input_Vtc_M2')
        self._DesignParameter['BND_Net20_Hrz1_M2']['_XWidth'] = abs ( tmp[0][0][0][0]['_XY_right'][0] - X_Grid7  )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net20_Hrz1_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net20_Hrz1_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid7
                            ##Y
        target_coordy = Y_Grid4_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net20_Hrz1_M2')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net20_Hrz1_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net20_Hrz1_M2']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net21
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net21 : M3 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net21_Hrz_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net21_Hrz_M3']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Net21_Hrz_M3']['_XWidth'] = abs ( X_Grid13 - X_Grid11  )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net21_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net21_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid11
                            ##Y
        target_coordy = Y_Grid4_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net21_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net21_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net21_Hrz_M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net20 : ViaM1M3
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Net21_ViaM1M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Net21_ViaM1M3'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Net21_ViaM1M3']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Net21_ViaM1M3']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Net21_ViaM1M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Net21_ViaM1M3']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
                        ## X
        target_coordx = X_Grid13
                        ## Y
        target_coordy = Y_Grid4_up

        target_coord = [target_coordx,target_coordy]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Net21_ViaM1M3','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Net21_ViaM1M3')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Net21_ViaM1M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing : net21 : M1 Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Net21_Hrz1_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Net21_Hrz1_M1']['_YWidth'] = _Routing_width

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_SetRst_Placement','SRF_Slv_Inv3','BND_Input_Vtc_M1')
        self._DesignParameter['BND_Net21_Hrz1_M1']['_XWidth'] = abs ( tmp[0][0][0][0]['_XY_right'][0] - X_Grid13  )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Net21_Hrz1_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Net21_Hrz1_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                            ##X
        target_coordx = X_Grid13
                            ##Y
        target_coordy = Y_Grid4_up

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Net21_Hrz1_M1')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Net21_Hrz1_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Net21_Hrz1_M1']['_XYCoordinates'] = tmpXY



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
    libname = 'Proj_ZZ00_RcdacSar_D04_01_SetRstDFF_Nor_Routing'
    ## CellName: ex)C01_cap_array_v2_84l
    cellname = 'D04_01_SetRstDFF_Nor_Routing_v0_290'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

        _Test_distance = 330, # 350
        _Routing_width =  50,
        _Routing_distance = 80, #80

    ## DFF Common
        _DFF_Pbody_NumCont      = 2, # number
        _DFF_Nbody_NumCont      = 2, # number
        _DFF_PMOSXvt2NMOSXvt    = 1150, # number
        _DFF_XvtTop2Pbody       = None, # number/None(Minimum)
        _DFF_Xvtdown2Nbody      = None, # number/None(Minimum)

    ## Master Xgate1
        ## Xgate common

        ## Xgate NMOS
        _Mst_Xgate1_NMOS_NumberofGate           = 1,    #1
        _Mst_Xgate1_NMOS_ChannelWidth           = 200,  #100
        _Mst_Xgate1_NMOS_ChannelLength          = 30,
        _Mst_Xgate1_NMOS_XVT                    = 'HVT',
        _Mst_Xgate1_NMOS_POGate_Comb_length     = 100,

        ## Xgate PMOS
        _Mst_Xgate1_PMOS_NumberofGate           = 1,    #1
        _Mst_Xgate1_PMOS_ChannelWidth           = 400,  #200
        _Mst_Xgate1_PMOS_ChannelLength          = 30,
        _Mst_Xgate1_PMOS_XVT                    = 'HVT',
        _Mst_Xgate1_PMOS_POGate_Comb_length     = 100,

    ## Master Xgate2
        ## Xgate common

        ## Xgate NMOS
        _Mst_Xgate2_NMOS_NumberofGate           = 1,
        _Mst_Xgate2_NMOS_ChannelWidth           = 200,
        _Mst_Xgate2_NMOS_ChannelLength          = 30,
        _Mst_Xgate2_NMOS_XVT                    = 'SLVT',
        _Mst_Xgate2_NMOS_POGate_Comb_length     = 100,

        ## Xgate PMOS
        _Mst_Xgate2_PMOS_NumberofGate           = 1, #2
        _Mst_Xgate2_PMOS_ChannelWidth           = 400,
        _Mst_Xgate2_PMOS_ChannelLength          = 30,
        _Mst_Xgate2_PMOS_XVT                    = 'SLVT',
        _Mst_Xgate2_PMOS_POGate_Comb_length     = 100,


    ## Master Nor1
        ## Nor1 common

        ## NMOS
            ## NMOS common
        _Mst_Nor1_NMOS_XVT='HVT',

            ## NMOSA
        _Mst_Nor1_NMOSA_NumberofGate           = 2,
        _Mst_Nor1_NMOSA_ChannelWidth           = 200,
        _Mst_Nor1_NMOSA_ChannelLength          = 30,
        _Mst_Nor1_NMOSA_POGate_Comb_length     = 100,

            ## NMOSB
        _Mst_Nor1_NMOSB_NumberofGate           = 2,
        _Mst_Nor1_NMOSB_ChannelWidth           = 200,
        _Mst_Nor1_NMOSB_ChannelLength          = 30,
        _Mst_Nor1_NMOSB_POGate_Comb_length     = 100,

        ## PMOS
            ## PMOS common
        _Mst_Nor1_PMOS_XVT='HVT',

            ## PMOSA
        _Mst_Nor1_PMOSA_NumberofGate            = 4,
        _Mst_Nor1_PMOSA_ChannelWidth            = 400,
        _Mst_Nor1_PMOSA_ChannelLength           = 30,
        _Mst_Nor1_PMOSA_POGate_Comb_length      = 100,

            ## PMOSB
        _Mst_Nor1_PMOSB_NumberofGate            = 4,
        _Mst_Nor1_PMOSB_ChannelWidth            = 400,
        _Mst_Nor1_PMOSB_ChannelLength           = 30,
        _Mst_Nor1_PMOSB_POGate_Comb_length      = 100,

    ## Master Nor2
        ## Nor2 common

        ## NMOS
            ## NMOS common
        _Mst_Nor2_NMOS_XVT='HVT',

            ## NMOSA
        _Mst_Nor2_NMOSA_NumberofGate           = 2,
        _Mst_Nor2_NMOSA_ChannelWidth           = 200,
        _Mst_Nor2_NMOSA_ChannelLength          = 30,
        _Mst_Nor2_NMOSA_POGate_Comb_length     = 100,

            ## NMOSB
        _Mst_Nor2_NMOSB_NumberofGate           = 2,
        _Mst_Nor2_NMOSB_ChannelWidth           = 200,
        _Mst_Nor2_NMOSB_ChannelLength          = 30,
        _Mst_Nor2_NMOSB_POGate_Comb_length     = 100,

        ## PMOS
            ## PMOS common
        _Mst_Nor2_PMOS_XVT='HVT',

            ## PMOSA
        _Mst_Nor2_PMOSA_NumberofGate            = 4,
        _Mst_Nor2_PMOSA_ChannelWidth            = 400,
        _Mst_Nor2_PMOSA_ChannelLength           = 30,
        _Mst_Nor2_PMOSA_POGate_Comb_length      = 100,

            ## PMOSB
        _Mst_Nor2_PMOSB_NumberofGate            = 4,
        _Mst_Nor2_PMOSB_ChannelWidth            = 400,
        _Mst_Nor2_PMOSB_ChannelLength           = 30,
        _Mst_Nor2_PMOSB_POGate_Comb_length      = 100,

    ## Master Inv1 : Set pre-driver
        ## Inv1 common

        ## Inv1 NMOS
        _Mst_Inv1_NMOS_NumberofGate           = 1,
        _Mst_Inv1_NMOS_ChannelWidth           = 200,
        _Mst_Inv1_NMOS_ChannelLength          = 30,
        _Mst_Inv1_NMOS_XVT                    = 'SLVT',
        _Mst_Inv1_NMOS_POGate_Comb_length     = 100,

        ## Inv1 PMOS
        _Mst_Inv1_PMOS_NumberofGate           = 1,
        _Mst_Inv1_PMOS_ChannelWidth           = 400,
        _Mst_Inv1_PMOS_ChannelLength          = 30,
        _Mst_Inv1_PMOS_XVT                    = 'SLVT',
        _Mst_Inv1_PMOS_POGate_Comb_length     = 100,

    ## Master Inv2 : Set driver
        ## Inv2 common

        ## Inv2 NMOS
        _Mst_Inv2_NMOS_NumberofGate           = 1,
        _Mst_Inv2_NMOS_ChannelWidth           = 200,
        _Mst_Inv2_NMOS_ChannelLength          = 30,
        _Mst_Inv2_NMOS_XVT                    = 'SLVT',
        _Mst_Inv2_NMOS_POGate_Comb_length     = 100,

        ## Inv2 PMOS
        _Mst_Inv2_PMOS_NumberofGate           = 1,
        _Mst_Inv2_PMOS_ChannelWidth           = 400,
        _Mst_Inv2_PMOS_ChannelLength          = 30,
        _Mst_Inv2_PMOS_XVT                    = 'SLVT',
        _Mst_Inv2_PMOS_POGate_Comb_length     = 100,


    ## Master Inv3 : Clock driver
        ## Inv3 common

        ## Inv3 NMOS
        _Mst_Inv3_NMOS_NumberofGate           = 1,
        _Mst_Inv3_NMOS_ChannelWidth           = 200,
        _Mst_Inv3_NMOS_ChannelLength          = 30,
        _Mst_Inv3_NMOS_XVT                    = 'SLVT',
        _Mst_Inv3_NMOS_POGate_Comb_length     = 100,

        ## Inv3 PMOS
        _Mst_Inv3_PMOS_NumberofGate           = 1,
        _Mst_Inv3_PMOS_ChannelWidth           = 400,
        _Mst_Inv3_PMOS_ChannelLength          = 30,
        _Mst_Inv3_PMOS_XVT                    = 'SLVT',
        _Mst_Inv3_PMOS_POGate_Comb_length     = 100,







    ## Slave Xgate1
        ## Xgate common

        ## Xgate NMOS
        _Slv_Xgate1_NMOS_NumberofGate           = 1,
        _Slv_Xgate1_NMOS_ChannelWidth           = 200,
        _Slv_Xgate1_NMOS_ChannelLength          = 30,
        _Slv_Xgate1_NMOS_XVT                    = 'HVT',
        _Slv_Xgate1_NMOS_POGate_Comb_length     = 100,

        ## Xgate NMOS
        _Slv_Xgate1_PMOS_NumberofGate           = 1,
        _Slv_Xgate1_PMOS_ChannelWidth           = 400,
        _Slv_Xgate1_PMOS_ChannelLength          = 30,
        _Slv_Xgate1_PMOS_XVT                    = 'HVT',
        _Slv_Xgate1_PMOS_POGate_Comb_length     = 100,

    ## Slave Xgate2
        ## Xgate common

        ## Xgate NMOS
        _Slv_Xgate2_NMOS_NumberofGate           = 1,
        _Slv_Xgate2_NMOS_ChannelWidth           = 200,
        _Slv_Xgate2_NMOS_ChannelLength          = 30,
        _Slv_Xgate2_NMOS_XVT                    = 'SLVT',
        _Slv_Xgate2_NMOS_POGate_Comb_length     = 100,

        ## Xgate NMOS
        _Slv_Xgate2_PMOS_NumberofGate           = 1,
        _Slv_Xgate2_PMOS_ChannelWidth           = 400,
        _Slv_Xgate2_PMOS_ChannelLength          = 30,
        _Slv_Xgate2_PMOS_XVT                    = 'SLVT',
        _Slv_Xgate2_PMOS_POGate_Comb_length     = 100,


    ## Slave Nor1
        ## Nor1 common

        ## NMOS
            ## NMOS common
        _Slv_Nor1_NMOS_XVT='HVT',

            ## NMOSA
        _Slv_Nor1_NMOSA_NumberofGate           = 2,
        _Slv_Nor1_NMOSA_ChannelWidth           = 200,
        _Slv_Nor1_NMOSA_ChannelLength          = 30,
        _Slv_Nor1_NMOSA_POGate_Comb_length     = 100,

            ## NMOSB
        _Slv_Nor1_NMOSB_NumberofGate           = 2,
        _Slv_Nor1_NMOSB_ChannelWidth           = 200,
        _Slv_Nor1_NMOSB_ChannelLength          = 30,
        _Slv_Nor1_NMOSB_POGate_Comb_length     = 100,

        ## PMOS
            ## PMOS common
        _Slv_Nor1_PMOS_XVT='HVT',

            ## PMOSA
        _Slv_Nor1_PMOSA_NumberofGate            = 4,
        _Slv_Nor1_PMOSA_ChannelWidth            = 400,
        _Slv_Nor1_PMOSA_ChannelLength           = 30,
        _Slv_Nor1_PMOSA_POGate_Comb_length      = 100,

            ## PMOSB
        _Slv_Nor1_PMOSB_NumberofGate            = 4,
        _Slv_Nor1_PMOSB_ChannelWidth            = 400,
        _Slv_Nor1_PMOSB_ChannelLength           = 30,
        _Slv_Nor1_PMOSB_POGate_Comb_length      = 100,

    ## Slave Nor2
        ## Nor2 common

        ## NMOS
            ## NMOS common
        _Slv_Nor2_NMOS_XVT='HVT',

            ## NMOSA
        _Slv_Nor2_NMOSA_NumberofGate           = 2,
        _Slv_Nor2_NMOSA_ChannelWidth           = 200,
        _Slv_Nor2_NMOSA_ChannelLength          = 30,
        _Slv_Nor2_NMOSA_POGate_Comb_length     = 100,

            ## NMOSB
        _Slv_Nor2_NMOSB_NumberofGate           = 2,
        _Slv_Nor2_NMOSB_ChannelWidth           = 200,
        _Slv_Nor2_NMOSB_ChannelLength          = 30,
        _Slv_Nor2_NMOSB_POGate_Comb_length     = 100,

        ## PMOS
            ## PMOS common
        _Slv_Nor2_PMOS_XVT='HVT',

            ## PMOSA
        _Slv_Nor2_PMOSA_NumberofGate            = 4,
        _Slv_Nor2_PMOSA_ChannelWidth            = 400,
        _Slv_Nor2_PMOSA_ChannelLength           = 30,
        _Slv_Nor2_PMOSA_POGate_Comb_length      = 100,

            ## PMOSB
        _Slv_Nor2_PMOSB_NumberofGate            = 4,
        _Slv_Nor2_PMOSB_ChannelWidth            = 400,
        _Slv_Nor2_PMOSB_ChannelLength           = 30,
        _Slv_Nor2_PMOSB_POGate_Comb_length      = 100,

    ## Slave Inv1 : ReSet pre-driver
        ## Inv1 common

        ## Inv1 NMOS
        _Slv_Inv1_NMOS_NumberofGate           = 1,
        _Slv_Inv1_NMOS_ChannelWidth           = 200,
        _Slv_Inv1_NMOS_ChannelLength          = 30,
        _Slv_Inv1_NMOS_XVT                    = 'SLVT',
        _Slv_Inv1_NMOS_POGate_Comb_length     = 100,

        ## Inv1 PMOS
        _Slv_Inv1_PMOS_NumberofGate           = 1,
        _Slv_Inv1_PMOS_ChannelWidth           = 400,
        _Slv_Inv1_PMOS_ChannelLength          = 30,
        _Slv_Inv1_PMOS_XVT                    = 'SLVT',
        _Slv_Inv1_PMOS_POGate_Comb_length     = 100,

    ## Slave Inv2 : ReSet driver
        ## Inv2 common

        ## Inv2 NMOS
        _Slv_Inv2_NMOS_NumberofGate           = 1,
        _Slv_Inv2_NMOS_ChannelWidth           = 200,
        _Slv_Inv2_NMOS_ChannelLength          = 30,
        _Slv_Inv2_NMOS_XVT                    = 'SLVT',
        _Slv_Inv2_NMOS_POGate_Comb_length     = 100,

        ## Inv2 PMOS
        _Slv_Inv2_PMOS_NumberofGate           = 1,
        _Slv_Inv2_PMOS_ChannelWidth           = 400,
        _Slv_Inv2_PMOS_ChannelLength          = 30,
        _Slv_Inv2_PMOS_XVT                    = 'SLVT',
        _Slv_Inv2_PMOS_POGate_Comb_length     = 100,


    ## Slave Inv3 : Qb driver
        ## Inv3 common

        ## Inv3 NMOS
        _Slv_Inv3_NMOS_NumberofGate           = 1,
        _Slv_Inv3_NMOS_ChannelWidth           = 200,
        _Slv_Inv3_NMOS_ChannelLength          = 30,
        _Slv_Inv3_NMOS_XVT                    = 'SLVT',
        _Slv_Inv3_NMOS_POGate_Comb_length     = 100,

        ## Inv3 PMOS
        _Slv_Inv3_PMOS_NumberofGate           = 1,
        _Slv_Inv3_PMOS_ChannelWidth           = 400,
        _Slv_Inv3_PMOS_ChannelLength          = 30,
        _Slv_Inv3_PMOS_XVT                    = 'SLVT',
        _Slv_Inv3_PMOS_POGate_Comb_length     = 100,


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
    LayoutObj = _SetRstDFF_Nor_Routing(_DesignParameter=None, _Name=cellname)
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
