
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
from KJH91_Projects.Project_ADC.Layoutgen_code.D00_SARLogic_Inverter_KJH1 import D00_00_Inverter_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.D01_SARLogic_XmissionGate_KJH1 import D01_00_Xgate_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.D02_SARLogic_Nor_KJH1 import D02_02_Nor_KJH0


## Define Class
class _SetRstDFF_Nor_Placement(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(

        _Test_distance = 150,

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

        _Test_distance = 150,

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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## MST
        ## Pre-defined
        XvtTop2Pbody = 0
        XvtDown2Nbody = 0

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Mst: Xgate1
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D01_00_Xgate_KJH._Xgate._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOS_NumberofGate']                 = _Mst_Xgate1_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth']                 = _Mst_Xgate1_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength']                = _Mst_Xgate1_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing']                  = None
        _Caculation_Parameters['_NMOS_SDWidth']                      = None
        _Caculation_Parameters['_NMOS_XVT']                          = _Mst_Xgate1_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit']                       = True

        _Caculation_Parameters['_NMOS_Source_Via_TF']                = True
        _Caculation_Parameters['_NMOS_Source_Via_Close2POpin_TF']    = True
        _Caculation_Parameters['_NMOS_Source_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOS_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_NMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOS_Drain_Comb_Length']            = None

        _Caculation_Parameters['_NMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOS_PODummy_Length']               = None
        _Caculation_Parameters['_NMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOS_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_POGate_Comb_length']           = _Mst_Xgate1_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOS_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOS_NumberofGate']                 = _Mst_Xgate1_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth']                 = _Mst_Xgate1_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength']                = _Mst_Xgate1_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing']                  = None
        _Caculation_Parameters['_PMOS_SDWidth']                      = None
        _Caculation_Parameters['_PMOS_XVT']                          = _Mst_Xgate1_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit']                       = True

        _Caculation_Parameters['_PMOS_Source_Via_TF']                = True
        _Caculation_Parameters['_PMOS_Source_Via_Close2POpin_TF']    = True
        _Caculation_Parameters['_PMOS_Source_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOS_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_PMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOS_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOS_PODummy_Length']               = None
        _Caculation_Parameters['_PMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOS_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_POGate_Comb_length']           = _Mst_Xgate1_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx']               = [0,1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']           = _DFF_XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody']          = _DFF_Xvtdown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                   = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Mst_Xgate1'] = self._SrefElementDeclaration(_DesignObj=D01_00_Xgate_KJH._Xgate(_DesignParameter=None, _Name='{}:SRF_Mst_Xgate1'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Mst_Xgate1']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Xgate1']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Xgate1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Xgate1']['_XYCoordinates'] = [[0, 0]]

        ## Find XvtTop2Pbody_tmp and XvtDown2Nbody_tmp
        tmp1 = self.get_param_KJH4('SRF_Mst_Xgate1','SRF_PMOS','BND_{}Layer'.format(_Mst_Xgate1_PMOS_XVT))
        tmp2 = self.get_param_KJH4('SRF_Mst_Xgate1','SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        XvtDown2Nbody_tmp = abs( tmp2[0][0][0][0][0]['_XY_down'][1] - tmp1[0][0][0][0]['_XY_down'][1] )

        if XvtDown2Nbody_tmp > XvtDown2Nbody:
            XvtDown2Nbody = XvtDown2Nbody_tmp

        tmp3 =  self.get_param_KJH4('SRF_Mst_Xgate1','SRF_NMOS','BND_{}Layer'.format(_Mst_Xgate1_NMOS_XVT))
        tmp4 =  self.get_param_KJH4('SRF_Mst_Xgate1', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        XvtTop2Pbody_tmp = abs( tmp3[0][0][0][0]['_XY_up'][1] - tmp4[0][0][0][0][0]['_XY_up'][1]  )

        if XvtTop2Pbody_tmp > XvtTop2Pbody:
            XvtTop2Pbody = XvtTop2Pbody_tmp

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Mst: Xgate2
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D01_00_Xgate_KJH._Xgate._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOS_NumberofGate']                 = _Mst_Xgate2_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth']                 = _Mst_Xgate2_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength']                = _Mst_Xgate2_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing']                  = None
        _Caculation_Parameters['_NMOS_SDWidth']                      = None
        _Caculation_Parameters['_NMOS_XVT']                          = _Mst_Xgate2_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit']                       = True

        _Caculation_Parameters['_NMOS_Source_Via_TF']                = True
        _Caculation_Parameters['_NMOS_Source_Via_Close2POpin_TF']    = True
        _Caculation_Parameters['_NMOS_Source_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOS_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_NMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOS_Drain_Comb_Length']            = None

        _Caculation_Parameters['_NMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOS_PODummy_Length']               = None
        _Caculation_Parameters['_NMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOS_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_POGate_Comb_length']           = _Mst_Xgate2_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOS_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOS_NumberofGate']                 = _Mst_Xgate2_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth']                 = _Mst_Xgate2_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength']                = _Mst_Xgate2_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing']                  = None
        _Caculation_Parameters['_PMOS_SDWidth']                      = None
        _Caculation_Parameters['_PMOS_XVT']                          = _Mst_Xgate2_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit']                       = True

        _Caculation_Parameters['_PMOS_Source_Via_TF']                = True
        _Caculation_Parameters['_PMOS_Source_Via_Close2POpin_TF']    = True
        _Caculation_Parameters['_PMOS_Source_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOS_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_PMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOS_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOS_PODummy_Length']               = None
        _Caculation_Parameters['_PMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOS_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_POGate_Comb_length']           = _Mst_Xgate2_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx']               = [0,1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']           = _DFF_XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody']          = _DFF_Xvtdown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                   = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Mst_Xgate2'] = self._SrefElementDeclaration(_DesignObj=D01_00_Xgate_KJH._Xgate(_DesignParameter=None, _Name='{}:SRF_Mst_Xgate2'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Mst_Xgate2']['_Reflect'] = [1, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Xgate2']['_Angle'] = 180

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Xgate2']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Xgate2']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Mst_Xgate2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        tmp1_1 = self.get_param_KJH4('SRF_Mst_Xgate1','SRF_PMOS','BND_PODummyLayer')
        target_coordx = tmp1_1[0][0][-1][0]['_XY_right'][0]
                                ##y
        tmp1_2 = self.get_param_KJH4('SRF_Mst_Xgate1','SRF_PMOS','BND_{}Layer'.format(_Mst_Xgate1_PMOS_XVT))
        target_coordy = tmp1_2[0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##X
        tmp2_1 = self.get_param_KJH4('SRF_Mst_Xgate2','SRF_PMOS','BND_PODummyLayer')
        approaching_coordx = tmp2_1[0][0][-1][0]['_XY_right'][0]
                                ##Y
        tmp2_2 = self.get_param_KJH4('SRF_Mst_Xgate2','SRF_PMOS','BND_{}Layer'.format(_Mst_Xgate2_PMOS_XVT))
        approaching_coordy = tmp2_2[0][0][0][0]['_XY_down'][1]

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

        ## Find XvtTop2Pbody_tmp and XvtDown2Nbody_tmp
        tmp1 = self.get_param_KJH4('SRF_Mst_Xgate2','SRF_PMOS','BND_{}Layer'.format(_Mst_Xgate2_PMOS_XVT))
        tmp2 = self.get_param_KJH4('SRF_Mst_Xgate2','SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        XvtDown2Nbody_tmp = abs( tmp2[0][0][0][0][0]['_XY_down'][1] - tmp1[0][0][0][0]['_XY_down'][1] )

        if XvtDown2Nbody_tmp > XvtDown2Nbody:
            XvtDown2Nbody = XvtDown2Nbody_tmp

        tmp3 =  self.get_param_KJH4('SRF_Mst_Xgate2','SRF_NMOS','BND_{}Layer'.format(_Mst_Xgate2_NMOS_XVT))
        tmp4 =  self.get_param_KJH4('SRF_Mst_Xgate2', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        XvtTop2Pbody_tmp = abs( tmp3[0][0][0][0]['_XY_up'][1] - tmp4[0][0][0][0][0]['_XY_up'][1]  )

        if XvtTop2Pbody_tmp > XvtTop2Pbody:
            XvtTop2Pbody = XvtTop2Pbody_tmp

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Mst: Nor1
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D02_02_Nor_KJH0._Nor._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOSA_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOSA_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOSA_NumberofGate']                 = _Mst_Nor1_NMOSA_NumberofGate
        _Caculation_Parameters['_NMOSA_ChannelWidth']                 = _Mst_Nor1_NMOSA_ChannelWidth
        _Caculation_Parameters['_NMOSA_ChannelLength']                = _Mst_Nor1_NMOSA_ChannelLength
        _Caculation_Parameters['_NMOSA_GateSpacing']                  = None
        _Caculation_Parameters['_NMOSA_SDWidth']                      = None
        _Caculation_Parameters['_NMOSA_XVT']                          = _Mst_Nor1_NMOS_XVT
        _Caculation_Parameters['_NMOSA_PCCrit']                       = True

        _Caculation_Parameters['_NMOSA_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOSA_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOSA_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOSA_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOSA_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOSA_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOSA_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOSA_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOSA_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOSA_Drain_Comb_Length']            = None

        _Caculation_Parameters['_NMOSA_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOSA_PODummy_Length']               = None
        _Caculation_Parameters['_NMOSA_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOSA_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOSA_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOSA_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOSA_POGate_Comb_length']           = _Mst_Nor1_NMOSA_POGate_Comb_length
        _Caculation_Parameters['_NMOSA_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOSA_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_NMOSB_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOSB_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOSB_NumberofGate']                 = _Mst_Nor1_NMOSB_NumberofGate
        _Caculation_Parameters['_NMOSB_ChannelWidth']                 = _Mst_Nor1_NMOSB_ChannelWidth
        _Caculation_Parameters['_NMOSB_ChannelLength']                = _Mst_Nor1_NMOSB_ChannelLength
        _Caculation_Parameters['_NMOSB_GateSpacing']                  = None
        _Caculation_Parameters['_NMOSB_SDWidth']                      = None
        _Caculation_Parameters['_NMOSB_XVT']                          = _Mst_Nor1_NMOS_XVT
        _Caculation_Parameters['_NMOSB_PCCrit']                       = True

        _Caculation_Parameters['_NMOSB_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOSB_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOSB_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOSB_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOSB_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOSB_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOSB_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOSB_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOSB_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOSB_Drain_Comb_Length']            = None

        _Caculation_Parameters['_NMOSB_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOSB_PODummy_Length']               = None
        _Caculation_Parameters['_NMOSB_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOSB_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOSB_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOSB_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOSB_POGate_Comb_length']           = _Mst_Nor1_NMOSB_POGate_Comb_length
        _Caculation_Parameters['_NMOSB_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOSB_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOSA_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOSA_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOSA_NumberofGate']                 = _Mst_Nor1_PMOSA_NumberofGate
        _Caculation_Parameters['_PMOSA_ChannelWidth']                 = _Mst_Nor1_PMOSA_ChannelWidth
        _Caculation_Parameters['_PMOSA_ChannelLength']                = _Mst_Nor1_PMOSA_ChannelLength
        _Caculation_Parameters['_PMOSA_GateSpacing']                  = None
        _Caculation_Parameters['_PMOSA_SDWidth']                      = None
        _Caculation_Parameters['_PMOSA_XVT']                          = _Mst_Nor1_PMOS_XVT
        _Caculation_Parameters['_PMOSA_PCCrit']                       = True

        _Caculation_Parameters['_PMOSA_Source_Via_TF']                = False
        _Caculation_Parameters['_PMOSA_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_PMOSA_Source_Comb_TF']               = False
        _Caculation_Parameters['_PMOSA_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOSA_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOSA_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOSA_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_PMOSA_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOSA_Drain_Comb_POpinward_TF']      = False
        _Caculation_Parameters['_PMOSA_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PMOSA_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOSA_PODummy_Length']               = None
        _Caculation_Parameters['_PMOSA_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOSA_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOSA_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOSA_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOSA_POGate_Comb_length']           = _Mst_Nor1_PMOSA_POGate_Comb_length
        _Caculation_Parameters['_PMOSA_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOSA_POGate_ViaMxMx']               = [0,1]



        _Caculation_Parameters['_PMOSB_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOSB_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOSB_NumberofGate']                 = _Mst_Nor1_PMOSB_NumberofGate
        _Caculation_Parameters['_PMOSB_ChannelWidth']                 = _Mst_Nor1_PMOSB_ChannelWidth
        _Caculation_Parameters['_PMOSB_ChannelLength']                = _Mst_Nor1_PMOSB_ChannelLength
        _Caculation_Parameters['_PMOSB_GateSpacing']                  = None
        _Caculation_Parameters['_PMOSB_SDWidth']                      = None
        _Caculation_Parameters['_PMOSB_XVT']                          = _Mst_Nor1_PMOS_XVT
        _Caculation_Parameters['_PMOSB_PCCrit']                       = True

        _Caculation_Parameters['_PMOSB_Source_Via_TF']                = True
        _Caculation_Parameters['_PMOSB_Source_Via_Close2POpin_TF']    = True
        _Caculation_Parameters['_PMOSB_Source_Comb_TF']               = True
        _Caculation_Parameters['_PMOSB_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOSB_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOSB_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOSB_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_PMOSB_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOSB_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOSB_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PMOSB_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOSB_PODummy_Length']               = None
        _Caculation_Parameters['_PMOSB_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOSB_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOSB_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOSB_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOSB_POGate_Comb_length']           = _Mst_Nor1_PMOSB_POGate_Comb_length
        _Caculation_Parameters['_PMOSB_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOSB_POGate_ViaMxMx']               = [0,1]



        _Caculation_Parameters['_NMOSAB_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOSAB_Pbody_XvtTop2Pbody']           = _DFF_XvtTop2Pbody
        _Caculation_Parameters['_PMOSAB_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOSAB_Nbody_Xvtdown2Nbody']          = _DFF_Xvtdown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                   = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Mst_Nor1'] = self._SrefElementDeclaration(_DesignObj=D02_02_Nor_KJH0._Nor(_DesignParameter=None, _Name='{}:SRF_Mst_Nor1'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Mst_Nor1']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Nor1']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Nor1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Nor1']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Mst_Nor1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        tmp1_1 = self.get_param_KJH4('SRF_Mst_Xgate2','SRF_PMOS','BND_PODummyLayer')
        target_coordx = tmp1_1[0][0][0][0]['_XY_left'][0]
                                ##y
        tmp1_2 = self.get_param_KJH4('SRF_Mst_Xgate2','SRF_PMOS','BND_{}Layer'.format(_Mst_Xgate2_PMOS_XVT))
        target_coordy = tmp1_2[0][0][0][0]['_XY_down'][1]

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

        ## Find XvtTop2Pbody_tmp and XvtDown2Nbody_tmp
        tmp1 = self.get_param_KJH4('SRF_Mst_Nor1','SRF_Pullup','SRF_PMOSA','BND_{}Layer'.format(_Mst_Nor1_PMOS_XVT))
        tmp2 = self.get_param_KJH4('SRF_Mst_Nor1','SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        XvtDown2Nbody_tmp = abs( tmp2[0][0][0][0][0]['_XY_down'][1] - tmp1[0][0][0][0][0]['_XY_down'][1] )

        if XvtDown2Nbody_tmp > XvtDown2Nbody:
            XvtDown2Nbody = XvtDown2Nbody_tmp

        tmp3 =  self.get_param_KJH4('SRF_Mst_Nor1','SRF_Pulldown','SRF_NMOSA','BND_{}Layer'.format(_Mst_Nor1_NMOS_XVT))
        tmp4 =  self.get_param_KJH4('SRF_Mst_Nor1', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')

        XvtTop2Pbody_tmp = abs( tmp3[0][0][0][0][0]['_XY_up'][1] - tmp4[0][0][0][0][0]['_XY_up'][1]  )

        if XvtTop2Pbody_tmp > XvtTop2Pbody:
            XvtTop2Pbody = XvtTop2Pbody_tmp

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Mst: Nor2
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D02_02_Nor_KJH0._Nor._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOSA_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOSA_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOSA_NumberofGate']                 = _Mst_Nor2_NMOSA_NumberofGate
        _Caculation_Parameters['_NMOSA_ChannelWidth']                 = _Mst_Nor2_NMOSA_ChannelWidth
        _Caculation_Parameters['_NMOSA_ChannelLength']                = _Mst_Nor2_NMOSA_ChannelLength
        _Caculation_Parameters['_NMOSA_GateSpacing']                  = None
        _Caculation_Parameters['_NMOSA_SDWidth']                      = None
        _Caculation_Parameters['_NMOSA_XVT']                          = _Mst_Nor2_NMOS_XVT
        _Caculation_Parameters['_NMOSA_PCCrit']                       = True

        _Caculation_Parameters['_NMOSA_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOSA_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOSA_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOSA_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOSA_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOSA_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOSA_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOSA_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOSA_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOSA_Drain_Comb_Length']            = None

        _Caculation_Parameters['_NMOSA_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOSA_PODummy_Length']               = None
        _Caculation_Parameters['_NMOSA_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOSA_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOSA_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOSA_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOSA_POGate_Comb_length']           = _Mst_Nor2_NMOSA_POGate_Comb_length
        _Caculation_Parameters['_NMOSA_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOSA_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_NMOSB_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOSB_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOSB_NumberofGate']                 = _Mst_Nor2_NMOSB_NumberofGate
        _Caculation_Parameters['_NMOSB_ChannelWidth']                 = _Mst_Nor2_NMOSB_ChannelWidth
        _Caculation_Parameters['_NMOSB_ChannelLength']                = _Mst_Nor2_NMOSB_ChannelLength
        _Caculation_Parameters['_NMOSB_GateSpacing']                  = None
        _Caculation_Parameters['_NMOSB_SDWidth']                      = None
        _Caculation_Parameters['_NMOSB_XVT']                          = _Mst_Nor2_NMOS_XVT
        _Caculation_Parameters['_NMOSB_PCCrit']                       = True

        _Caculation_Parameters['_NMOSB_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOSB_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOSB_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOSB_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOSB_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOSB_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOSB_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOSB_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOSB_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOSB_Drain_Comb_Length']            = None

        _Caculation_Parameters['_NMOSB_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOSB_PODummy_Length']               = None
        _Caculation_Parameters['_NMOSB_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOSB_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOSB_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOSB_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOSB_POGate_Comb_length']           = _Mst_Nor2_NMOSB_POGate_Comb_length
        _Caculation_Parameters['_NMOSB_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOSB_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOSA_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOSA_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOSA_NumberofGate']                 = _Mst_Nor2_PMOSA_NumberofGate
        _Caculation_Parameters['_PMOSA_ChannelWidth']                 = _Mst_Nor2_PMOSA_ChannelWidth
        _Caculation_Parameters['_PMOSA_ChannelLength']                = _Mst_Nor2_PMOSA_ChannelLength
        _Caculation_Parameters['_PMOSA_GateSpacing']                  = None
        _Caculation_Parameters['_PMOSA_SDWidth']                      = None
        _Caculation_Parameters['_PMOSA_XVT']                          = _Mst_Nor2_PMOS_XVT
        _Caculation_Parameters['_PMOSA_PCCrit']                       = True

        _Caculation_Parameters['_PMOSA_Source_Via_TF']                = False
        _Caculation_Parameters['_PMOSA_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_PMOSA_Source_Comb_TF']               = False
        _Caculation_Parameters['_PMOSA_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOSA_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOSA_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOSA_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_PMOSA_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOSA_Drain_Comb_POpinward_TF']      = False
        _Caculation_Parameters['_PMOSA_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PMOSA_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOSA_PODummy_Length']               = None
        _Caculation_Parameters['_PMOSA_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOSA_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOSA_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOSA_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOSA_POGate_Comb_length']           = _Mst_Nor2_PMOSA_POGate_Comb_length
        _Caculation_Parameters['_PMOSA_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOSA_POGate_ViaMxMx']               = [0,1]



        _Caculation_Parameters['_PMOSB_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOSB_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOSB_NumberofGate']                 = _Mst_Nor2_PMOSB_NumberofGate
        _Caculation_Parameters['_PMOSB_ChannelWidth']                 = _Mst_Nor2_PMOSB_ChannelWidth
        _Caculation_Parameters['_PMOSB_ChannelLength']                = _Mst_Nor2_PMOSB_ChannelLength
        _Caculation_Parameters['_PMOSB_GateSpacing']                  = None
        _Caculation_Parameters['_PMOSB_SDWidth']                      = None
        _Caculation_Parameters['_PMOSB_XVT']                          = _Mst_Nor2_PMOS_XVT
        _Caculation_Parameters['_PMOSB_PCCrit']                       = True

        _Caculation_Parameters['_PMOSB_Source_Via_TF']                = True
        _Caculation_Parameters['_PMOSB_Source_Via_Close2POpin_TF']    = True
        _Caculation_Parameters['_PMOSB_Source_Comb_TF']               = True
        _Caculation_Parameters['_PMOSB_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOSB_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOSB_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOSB_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_PMOSB_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOSB_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOSB_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PMOSB_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOSB_PODummy_Length']               = None
        _Caculation_Parameters['_PMOSB_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOSB_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOSB_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOSB_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOSB_POGate_Comb_length']           = _Mst_Nor2_PMOSB_POGate_Comb_length
        _Caculation_Parameters['_PMOSB_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOSB_POGate_ViaMxMx']               = [0,1]



        _Caculation_Parameters['_NMOSAB_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOSAB_Pbody_XvtTop2Pbody']           = _DFF_XvtTop2Pbody
        _Caculation_Parameters['_PMOSAB_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOSAB_Nbody_Xvtdown2Nbody']          = _DFF_Xvtdown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                     = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Mst_Nor2'] = self._SrefElementDeclaration(_DesignObj=D02_02_Nor_KJH0._Nor(_DesignParameter=None, _Name='{}:SRF_Mst_Nor2'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Mst_Nor2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Nor2']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Nor2']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
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

        ## Find XvtTop2Pbody_tmp and XvtDown2Nbody_tmp
        tmp1 = self.get_param_KJH4('SRF_Mst_Nor2','SRF_Pullup','SRF_PMOSA','BND_{}Layer'.format(_Mst_Nor2_PMOS_XVT))
        tmp2 = self.get_param_KJH4('SRF_Mst_Nor2','SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        XvtDown2Nbody_tmp = abs( tmp2[0][0][0][0][0]['_XY_down'][1] - tmp1[0][0][0][0][0]['_XY_down'][1] )

        if XvtDown2Nbody_tmp > XvtDown2Nbody_tmp:
            XvtDown2Nbody = XvtDown2Nbody_tmp

        tmp3 =  self.get_param_KJH4('SRF_Mst_Nor2','SRF_Pulldown','SRF_NMOSA','BND_{}Layer'.format(_Mst_Nor2_NMOS_XVT))
        tmp4 =  self.get_param_KJH4('SRF_Mst_Nor2', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        XvtTop2Pbody_tmp = abs( tmp3[0][0][0][0][0]['_XY_up'][1] - tmp4[0][0][0][0][0]['_XY_up'][1]  )

        if XvtTop2Pbody_tmp > XvtTop2Pbody:
            XvtTop2Pbody = XvtTop2Pbody_tmp


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Mst: Inv1: Set pre-driver
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D00_00_Inverter_KJH._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOS_NumberofGate']                 = _Mst_Inv1_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth']                 = _Mst_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength']                = _Mst_Inv1_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing']                  = None
        _Caculation_Parameters['_NMOS_SDWidth']                      = None
        _Caculation_Parameters['_NMOS_XVT']                          = _Mst_Inv1_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit']                       = True

        _Caculation_Parameters['_NMOS_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOS_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOS_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOS_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOS_Drain_Comb_Length']            = 0

        _Caculation_Parameters['_NMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOS_PODummy_Length']               = None
        _Caculation_Parameters['_NMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOS_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_POGate_Comb_length']           = _Mst_Inv1_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOS_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOS_NumberofGate']                 = _Mst_Inv1_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth']                 = _Mst_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength']                = _Mst_Inv1_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing']                  = None
        _Caculation_Parameters['_PMOS_SDWidth']                      = None
        _Caculation_Parameters['_PMOS_XVT']                          = _Mst_Inv1_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit']                       = True

        _Caculation_Parameters['_PMOS_Source_Via_TF']                = False
        _Caculation_Parameters['_PMOS_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_PMOS_Source_Comb_TF']               = False
        _Caculation_Parameters['_PMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOS_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_PMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOS_Drain_Comb_Length']            = 0

        _Caculation_Parameters['_PMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOS_PODummy_Length']               = None
        _Caculation_Parameters['_PMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOS_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_POGate_Comb_length']           = _Mst_Inv1_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx']               = [0,1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']           = _DFF_XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody']          = _DFF_Xvtdown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                   = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Mst_Inv1'] = self._SrefElementDeclaration(_DesignObj=D00_00_Inverter_KJH._Inverter(_DesignParameter=None, _Name='{}:SRF_Mst_Inv1'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Mst_Inv1']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Inv1']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Inv1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
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

        ## Find XvtTop2Pbody_tmp and XvtDown2Nbody_tmp
        tmp1 = self.get_param_KJH4('SRF_Mst_Inv1','SRF_PMOS','BND_{}Layer'.format(_Mst_Inv1_PMOS_XVT))
        tmp2 = self.get_param_KJH4('SRF_Mst_Inv1','SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        XvtDown2Nbody_tmp = abs( tmp2[0][0][0][0][0]['_XY_down'][1] - tmp1[0][0][0][0]['_XY_down'][1] )

        if XvtDown2Nbody_tmp > XvtDown2Nbody:
            XvtDown2Nbody = XvtDown2Nbody_tmp

        tmp3 =  self.get_param_KJH4('SRF_Mst_Inv1','SRF_NMOS','BND_{}Layer'.format(_Mst_Inv1_NMOS_XVT))
        tmp4 =  self.get_param_KJH4('SRF_Mst_Inv1', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')

        XvtTop2Pbody_tmp = abs( tmp3[0][0][0][0]['_XY_up'][1] - tmp4[0][0][0][0][0]['_XY_up'][1]  )

        if XvtTop2Pbody_tmp > XvtTop2Pbody:
            XvtTop2Pbody = XvtTop2Pbody_tmp


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Mst: Inv2: Set driver
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D00_00_Inverter_KJH._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOS_NumberofGate']                 = _Mst_Inv2_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth']                 = _Mst_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength']                = _Mst_Inv2_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing']                  = None
        _Caculation_Parameters['_NMOS_SDWidth']                      = None
        _Caculation_Parameters['_NMOS_XVT']                          = _Mst_Inv2_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit']                       = True

        _Caculation_Parameters['_NMOS_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOS_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOS_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOS_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOS_Drain_Comb_Length']            = 0

        _Caculation_Parameters['_NMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOS_PODummy_Length']               = None
        _Caculation_Parameters['_NMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOS_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_POGate_Comb_length']           = _Mst_Inv2_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOS_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOS_NumberofGate']                 = _Mst_Inv2_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth']                 = _Mst_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength']                = _Mst_Inv2_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing']                  = None
        _Caculation_Parameters['_PMOS_SDWidth']                      = None
        _Caculation_Parameters['_PMOS_XVT']                          = _Mst_Inv2_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit']                       = True

        _Caculation_Parameters['_PMOS_Source_Via_TF']                = False
        _Caculation_Parameters['_PMOS_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_PMOS_Source_Comb_TF']               = False
        _Caculation_Parameters['_PMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOS_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_PMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOS_Drain_Comb_Length']            = 0

        _Caculation_Parameters['_PMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOS_PODummy_Length']               = None
        _Caculation_Parameters['_PMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOS_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_POGate_Comb_length']           = _Mst_Inv2_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx']               = [0,1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']           = _DFF_XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody']          = _DFF_Xvtdown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                   = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Mst_Inv2'] = self._SrefElementDeclaration(_DesignObj=D00_00_Inverter_KJH._Inverter(_DesignParameter=None, _Name='{}:SRF_Mst_Inv2'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Mst_Inv2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Inv2']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Inv2']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
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

        ## Find XvtTop2Pbody_tmp and XvtDown2Nbody_tmp
        tmp1 = self.get_param_KJH4('SRF_Mst_Inv2','SRF_PMOS','BND_{}Layer'.format(_Mst_Inv2_PMOS_XVT))
        tmp2 = self.get_param_KJH4('SRF_Mst_Inv2','SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        XvtDown2Nbody_tmp = abs( tmp2[0][0][0][0][0]['_XY_down'][1] - tmp1[0][0][0][0]['_XY_down'][1] )

        if XvtDown2Nbody_tmp > XvtDown2Nbody:
            XvtDown2Nbody = XvtDown2Nbody_tmp

        tmp3 =  self.get_param_KJH4('SRF_Mst_Inv2','SRF_NMOS','BND_{}Layer'.format(_Mst_Inv2_NMOS_XVT))
        tmp4 =  self.get_param_KJH4('SRF_Mst_Inv2', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')

        XvtTop2Pbody_tmp = abs( tmp3[0][0][0][0]['_XY_up'][1] - tmp4[0][0][0][0][0]['_XY_up'][1]  )

        if XvtTop2Pbody_tmp > XvtTop2Pbody:
            XvtTop2Pbody = XvtTop2Pbody_tmp

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Mst: Inv3: Clock driver
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D00_00_Inverter_KJH._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOS_NumberofGate']                 = _Mst_Inv3_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth']                 = _Mst_Inv3_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength']                = _Mst_Inv3_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing']                  = None
        _Caculation_Parameters['_NMOS_SDWidth']                      = None
        _Caculation_Parameters['_NMOS_XVT']                          = _Mst_Inv3_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit']                       = True

        _Caculation_Parameters['_NMOS_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOS_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOS_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOS_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOS_Drain_Comb_Length']            = 0

        _Caculation_Parameters['_NMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOS_PODummy_Length']               = None
        _Caculation_Parameters['_NMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOS_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_POGate_Comb_length']           = _Mst_Inv3_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOS_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOS_NumberofGate']                 = _Mst_Inv3_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth']                 = _Mst_Inv3_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength']                = _Mst_Inv3_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing']                  = None
        _Caculation_Parameters['_PMOS_SDWidth']                      = None
        _Caculation_Parameters['_PMOS_XVT']                          = _Mst_Inv3_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit']                       = True

        _Caculation_Parameters['_PMOS_Source_Via_TF']                = False
        _Caculation_Parameters['_PMOS_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_PMOS_Source_Comb_TF']               = False
        _Caculation_Parameters['_PMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOS_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_PMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOS_Drain_Comb_Length']            = 0

        _Caculation_Parameters['_PMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOS_PODummy_Length']               = None
        _Caculation_Parameters['_PMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOS_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_POGate_Comb_length']           = _Mst_Inv3_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx']               = [0,1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']           = _DFF_XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody']          = _DFF_Xvtdown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                   = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Mst_Inv3'] = self._SrefElementDeclaration(_DesignObj=D00_00_Inverter_KJH._Inverter(_DesignParameter=None, _Name='{}:SRF_Mst_Inv3'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Mst_Inv3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Inv3']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Inv3']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Inv3']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Mst_Inv3']['_XYCoordinates'] = [[0, 0]]
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
        tmp2_1 = self.get_param_KJH4('SRF_Mst_Inv3','SRF_PMOS','BND_PODummyLayer')
        approaching_coordx = tmp2_1[0][0][0][0]['_XY_left'][0]
                                ##Y
        tmp2_2 = self.get_param_KJH4('SRF_Mst_Inv3','SRF_PMOS','BND_{}Layer'.format(_Mst_Inv2_PMOS_XVT))
        approaching_coordy = tmp2_2[0][0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Mst_Inv3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] +  _Test_distance
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Mst_Inv3']['_XYCoordinates'] = tmpXY


        ## Find XvtTop2Pbody_tmp and XvtDown2Nbody_tmp
        tmp1 = self.get_param_KJH4('SRF_Mst_Inv3','SRF_PMOS','BND_{}Layer'.format(_Mst_Inv3_PMOS_XVT))
        tmp2 = self.get_param_KJH4('SRF_Mst_Inv3','SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        XvtDown2Nbody_tmp = abs( tmp2[0][0][0][0][0]['_XY_down'][1] - tmp1[0][0][0][0]['_XY_down'][1] )

        if XvtDown2Nbody_tmp > XvtDown2Nbody:
            XvtDown2Nbody = XvtDown2Nbody_tmp

        tmp3 =  self.get_param_KJH4('SRF_Mst_Inv3','SRF_NMOS','BND_{}Layer'.format(_Mst_Inv3_NMOS_XVT))
        tmp4 =  self.get_param_KJH4('SRF_Mst_Inv3','SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        XvtTop2Pbody_tmp = abs( tmp3[0][0][0][0]['_XY_up'][1] - tmp4[0][0][0][0][0]['_XY_up'][1]  )

        if XvtTop2Pbody_tmp > XvtTop2Pbody:
            XvtTop2Pbody = XvtTop2Pbody_tmp



        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## SLV
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  SLV: Xgate1
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D01_00_Xgate_KJH._Xgate._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOS_NumberofGate']                 = _Slv_Xgate1_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth']                 = _Slv_Xgate1_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength']                = _Slv_Xgate1_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing']                  = None
        _Caculation_Parameters['_NMOS_SDWidth']                      = None
        _Caculation_Parameters['_NMOS_XVT']                          = _Slv_Xgate1_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit']                       = True

        _Caculation_Parameters['_NMOS_Source_Via_TF']                = True
        _Caculation_Parameters['_NMOS_Source_Via_Close2POpin_TF']    = True
        _Caculation_Parameters['_NMOS_Source_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOS_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_NMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOS_Drain_Comb_Length']            = None

        _Caculation_Parameters['_NMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOS_PODummy_Length']               = None
        _Caculation_Parameters['_NMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOS_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_POGate_Comb_length']           = _Slv_Xgate1_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOS_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOS_NumberofGate']                 = _Slv_Xgate1_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth']                 = _Slv_Xgate1_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength']                = _Slv_Xgate1_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing']                  = None
        _Caculation_Parameters['_PMOS_SDWidth']                      = None
        _Caculation_Parameters['_PMOS_XVT']                          = _Slv_Xgate1_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit']                       = True

        _Caculation_Parameters['_PMOS_Source_Via_TF']                = True
        _Caculation_Parameters['_PMOS_Source_Via_Close2POpin_TF']    = True
        _Caculation_Parameters['_PMOS_Source_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOS_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_PMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOS_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOS_PODummy_Length']               = None
        _Caculation_Parameters['_PMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOS_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_POGate_Comb_length']           = _Slv_Xgate1_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx']               = [0,1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']           = _DFF_XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody']          = _DFF_Xvtdown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                   = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Slv_Xgate1'] = self._SrefElementDeclaration(_DesignObj=D01_00_Xgate_KJH._Xgate(_DesignParameter=None, _Name='{}:SRF_Slv_Xgate1'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Slv_Xgate1']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Xgate1']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Xgate1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Xgate1']['_XYCoordinates'] = [[0, 0]]


                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Slv_Xgate1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        tmp1_1 = self.get_param_KJH4('SRF_Mst_Inv3','SRF_PMOS','BND_PODummyLayer')
        target_coordx = tmp1_1[0][0][-1][0]['_XY_right'][0]
                                ##y
        tmp1_2 = self.get_param_KJH4('SRF_Mst_Inv3','SRF_PMOS','BND_{}Layer'.format(_Mst_Inv3_PMOS_XVT))
        target_coordy = tmp1_2[0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##X
        tmp2_1 = self.get_param_KJH4('SRF_Slv_Xgate1','SRF_PMOS','BND_PODummyLayer')
        approaching_coordx = tmp2_1[0][0][0][0]['_XY_left'][0]
                                ##Y
        tmp2_2 = self.get_param_KJH4('SRF_Slv_Xgate1','SRF_PMOS','BND_{}Layer'.format(_Slv_Xgate1_PMOS_XVT))
        approaching_coordy = tmp2_2[0][0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Slv_Xgate1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] +  _Test_distance
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Slv_Xgate1']['_XYCoordinates'] = tmpXY

        ## Find XvtTop2Pbody_tmp and XvtDown2Nbody_tmp
        tmp1 = self.get_param_KJH4('SRF_Slv_Xgate1','SRF_PMOS','BND_{}Layer'.format(_Slv_Xgate1_PMOS_XVT))
        tmp2 = self.get_param_KJH4('SRF_Slv_Xgate1','SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        XvtDown2Nbody_tmp = abs( tmp2[0][0][0][0][0]['_XY_down'][1] - tmp1[0][0][0][0]['_XY_down'][1] )

        if XvtDown2Nbody_tmp > XvtDown2Nbody:
            XvtDown2Nbody = XvtDown2Nbody_tmp

        tmp3 =  self.get_param_KJH4('SRF_Slv_Xgate1','SRF_NMOS','BND_{}Layer'.format(_Slv_Xgate1_NMOS_XVT))
        tmp4 =  self.get_param_KJH4('SRF_Slv_Xgate1', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        XvtTop2Pbody_tmp = abs( tmp3[0][0][0][0]['_XY_up'][1] - tmp4[0][0][0][0][0]['_XY_up'][1]  )

        if XvtTop2Pbody_tmp > XvtTop2Pbody:
            XvtTop2Pbody = XvtTop2Pbody_tmp

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Slv: Xgate2
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D01_00_Xgate_KJH._Xgate._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOS_NumberofGate']                 = _Slv_Xgate2_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth']                 = _Slv_Xgate2_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength']                = _Slv_Xgate2_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing']                  = None
        _Caculation_Parameters['_NMOS_SDWidth']                      = None
        _Caculation_Parameters['_NMOS_XVT']                          = _Slv_Xgate2_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit']                       = True

        _Caculation_Parameters['_NMOS_Source_Via_TF']                = True
        _Caculation_Parameters['_NMOS_Source_Via_Close2POpin_TF']    = True
        _Caculation_Parameters['_NMOS_Source_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOS_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_NMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOS_Drain_Comb_Length']            = None

        _Caculation_Parameters['_NMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOS_PODummy_Length']               = None
        _Caculation_Parameters['_NMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOS_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_POGate_Comb_length']           = _Slv_Xgate2_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOS_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOS_NumberofGate']                 = _Slv_Xgate2_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth']                 = _Slv_Xgate2_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength']                = _Slv_Xgate2_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing']                  = None
        _Caculation_Parameters['_PMOS_SDWidth']                      = None
        _Caculation_Parameters['_PMOS_XVT']                          = _Slv_Xgate2_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit']                       = True

        _Caculation_Parameters['_PMOS_Source_Via_TF']                = True
        _Caculation_Parameters['_PMOS_Source_Via_Close2POpin_TF']    = True
        _Caculation_Parameters['_PMOS_Source_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOS_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_PMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOS_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOS_PODummy_Length']               = None
        _Caculation_Parameters['_PMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOS_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_POGate_Comb_length']           = _Slv_Xgate2_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx']               = [0,1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']           = _DFF_XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody']          = _DFF_Xvtdown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                   = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Slv_Xgate2'] = self._SrefElementDeclaration(_DesignObj=D01_00_Xgate_KJH._Xgate(_DesignParameter=None, _Name='{}:SRF_Slv_Xgate2'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Slv_Xgate2']['_Reflect'] = [1, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Xgate2']['_Angle'] = 180

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Xgate2']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Xgate2']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Slv_Xgate2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        tmp1_1 = self.get_param_KJH4('SRF_Slv_Xgate1','SRF_PMOS','BND_PODummyLayer')
        target_coordx = tmp1_1[0][0][-1][0]['_XY_right'][0]
                                ##y
        tmp1_2 = self.get_param_KJH4('SRF_Slv_Xgate1','SRF_PMOS','BND_{}Layer'.format(_Slv_Xgate1_PMOS_XVT))
        target_coordy = tmp1_2[0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##X
        tmp2_1 = self.get_param_KJH4('SRF_Slv_Xgate2','SRF_PMOS','BND_PODummyLayer')
        approaching_coordx = tmp2_1[0][0][-1][0]['_XY_right'][0]
                                ##Y
        tmp2_2 = self.get_param_KJH4('SRF_Slv_Xgate2','SRF_PMOS','BND_{}Layer'.format(_Slv_Xgate2_PMOS_XVT))
        approaching_coordy = tmp2_2[0][0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Slv_Xgate2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] +  _Test_distance
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Slv_Xgate2']['_XYCoordinates'] = tmpXY

        ## Find XvtTop2Pbody_tmp and XvtDown2Nbody_tmp
        tmp1 = self.get_param_KJH4('SRF_Slv_Xgate2','SRF_PMOS','BND_{}Layer'.format(_Slv_Xgate2_PMOS_XVT))
        tmp2 = self.get_param_KJH4('SRF_Slv_Xgate2','SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        XvtDown2Nbody_tmp = abs( tmp2[0][0][0][0][0]['_XY_down'][1] - tmp1[0][0][0][0]['_XY_down'][1] )

        if XvtDown2Nbody_tmp > XvtDown2Nbody:
            XvtDown2Nbody = XvtDown2Nbody_tmp

        tmp3 =  self.get_param_KJH4('SRF_Slv_Xgate2','SRF_NMOS','BND_{}Layer'.format(_Slv_Xgate2_NMOS_XVT))
        tmp4 =  self.get_param_KJH4('SRF_Slv_Xgate2', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        XvtTop2Pbody_tmp = abs( tmp3[0][0][0][0]['_XY_up'][1] - tmp4[0][0][0][0][0]['_XY_up'][1]  )

        if XvtTop2Pbody_tmp > XvtTop2Pbody:
            XvtTop2Pbody = XvtTop2Pbody_tmp

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Slv: Nor1
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D02_02_Nor_KJH0._Nor._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOSA_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOSA_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOSA_NumberofGate']                 = _Slv_Nor1_NMOSA_NumberofGate
        _Caculation_Parameters['_NMOSA_ChannelWidth']                 = _Slv_Nor1_NMOSA_ChannelWidth
        _Caculation_Parameters['_NMOSA_ChannelLength']                = _Slv_Nor1_NMOSA_ChannelLength
        _Caculation_Parameters['_NMOSA_GateSpacing']                  = None
        _Caculation_Parameters['_NMOSA_SDWidth']                      = None
        _Caculation_Parameters['_NMOSA_XVT']                          = _Slv_Nor1_NMOS_XVT
        _Caculation_Parameters['_NMOSA_PCCrit']                       = True

        _Caculation_Parameters['_NMOSA_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOSA_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOSA_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOSA_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOSA_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOSA_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOSA_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOSA_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOSA_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOSA_Drain_Comb_Length']            = None

        _Caculation_Parameters['_NMOSA_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOSA_PODummy_Length']               = None
        _Caculation_Parameters['_NMOSA_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOSA_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOSA_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOSA_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOSA_POGate_Comb_length']           = _Slv_Nor1_NMOSA_POGate_Comb_length
        _Caculation_Parameters['_NMOSA_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOSA_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_NMOSB_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOSB_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOSB_NumberofGate']                 = _Slv_Nor1_NMOSB_NumberofGate
        _Caculation_Parameters['_NMOSB_ChannelWidth']                 = _Slv_Nor1_NMOSB_ChannelWidth
        _Caculation_Parameters['_NMOSB_ChannelLength']                = _Slv_Nor1_NMOSB_ChannelLength
        _Caculation_Parameters['_NMOSB_GateSpacing']                  = None
        _Caculation_Parameters['_NMOSB_SDWidth']                      = None
        _Caculation_Parameters['_NMOSB_XVT']                          = _Slv_Nor1_NMOS_XVT
        _Caculation_Parameters['_NMOSB_PCCrit']                       = True

        _Caculation_Parameters['_NMOSB_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOSB_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOSB_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOSB_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOSB_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOSB_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOSB_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOSB_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOSB_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOSB_Drain_Comb_Length']            = None

        _Caculation_Parameters['_NMOSB_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOSB_PODummy_Length']               = None
        _Caculation_Parameters['_NMOSB_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOSB_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOSB_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOSB_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOSB_POGate_Comb_length']           = _Slv_Nor1_NMOSB_POGate_Comb_length
        _Caculation_Parameters['_NMOSB_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOSB_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOSA_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOSA_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOSA_NumberofGate']                 = _Slv_Nor1_PMOSA_NumberofGate
        _Caculation_Parameters['_PMOSA_ChannelWidth']                 = _Slv_Nor1_PMOSA_ChannelWidth
        _Caculation_Parameters['_PMOSA_ChannelLength']                = _Slv_Nor1_PMOSA_ChannelLength
        _Caculation_Parameters['_PMOSA_GateSpacing']                  = None
        _Caculation_Parameters['_PMOSA_SDWidth']                      = None
        _Caculation_Parameters['_PMOSA_XVT']                          = _Slv_Nor1_PMOS_XVT
        _Caculation_Parameters['_PMOSA_PCCrit']                       = True

        _Caculation_Parameters['_PMOSA_Source_Via_TF']                = False
        _Caculation_Parameters['_PMOSA_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_PMOSA_Source_Comb_TF']               = False
        _Caculation_Parameters['_PMOSA_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOSA_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOSA_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOSA_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_PMOSA_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOSA_Drain_Comb_POpinward_TF']      = False
        _Caculation_Parameters['_PMOSA_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PMOSA_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOSA_PODummy_Length']               = None
        _Caculation_Parameters['_PMOSA_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOSA_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOSA_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOSA_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOSA_POGate_Comb_length']           = _Slv_Nor1_PMOSA_POGate_Comb_length
        _Caculation_Parameters['_PMOSA_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOSA_POGate_ViaMxMx']               = [0,1]



        _Caculation_Parameters['_PMOSB_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOSB_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOSB_NumberofGate']                 = _Slv_Nor1_PMOSB_NumberofGate
        _Caculation_Parameters['_PMOSB_ChannelWidth']                 = _Slv_Nor1_PMOSB_ChannelWidth
        _Caculation_Parameters['_PMOSB_ChannelLength']                = _Slv_Nor1_PMOSB_ChannelLength
        _Caculation_Parameters['_PMOSB_GateSpacing']                  = None
        _Caculation_Parameters['_PMOSB_SDWidth']                      = None
        _Caculation_Parameters['_PMOSB_XVT']                          = _Slv_Nor1_PMOS_XVT
        _Caculation_Parameters['_PMOSB_PCCrit']                       = True

        _Caculation_Parameters['_PMOSB_Source_Via_TF']                = True
        _Caculation_Parameters['_PMOSB_Source_Via_Close2POpin_TF']    = True
        _Caculation_Parameters['_PMOSB_Source_Comb_TF']               = True
        _Caculation_Parameters['_PMOSB_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOSB_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOSB_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOSB_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_PMOSB_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOSB_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOSB_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PMOSB_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOSB_PODummy_Length']               = None
        _Caculation_Parameters['_PMOSB_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOSB_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOSB_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOSB_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOSB_POGate_Comb_length']           = _Slv_Nor1_PMOSB_POGate_Comb_length
        _Caculation_Parameters['_PMOSB_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOSB_POGate_ViaMxMx']               = [0,1]



        _Caculation_Parameters['_NMOSAB_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOSAB_Pbody_XvtTop2Pbody']           = _DFF_XvtTop2Pbody
        _Caculation_Parameters['_PMOSAB_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOSAB_Nbody_Xvtdown2Nbody']          = _DFF_Xvtdown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                   = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Slv_Nor1'] = self._SrefElementDeclaration(_DesignObj=D02_02_Nor_KJH0._Nor(_DesignParameter=None, _Name='{}:SRF_Slv_Nor1'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Slv_Nor1']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Nor1']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Nor1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Nor1']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Slv_Nor1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        tmp1_1 = self.get_param_KJH4('SRF_Slv_Xgate2','SRF_PMOS','BND_PODummyLayer')
        target_coordx = tmp1_1[0][0][0][0]['_XY_left'][0]
                                ##y
        tmp1_2 = self.get_param_KJH4('SRF_Slv_Xgate2','SRF_PMOS','BND_{}Layer'.format(_Slv_Xgate2_PMOS_XVT))
        target_coordy = tmp1_2[0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##X
        tmp2_1 = self.get_param_KJH4('SRF_Slv_Nor1','SRF_Pullup','SRF_PMOSA','BND_PODummyLayer')
        approaching_coordx = tmp2_1[0][0][0][0][0]['_XY_left'][0]
                                ##Y
        tmp2_2 = self.get_param_KJH4('SRF_Slv_Nor1','SRF_Pullup','SRF_PMOSA','BND_{}Layer'.format(_Slv_Nor1_PMOS_XVT))
        approaching_coordy = tmp2_2[0][0][0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Slv_Nor1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] +  _Test_distance
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Slv_Nor1']['_XYCoordinates'] = tmpXY

        ## Find XvtTop2Pbody_tmp and XvtDown2Nbody_tmp
        tmp1 = self.get_param_KJH4('SRF_Slv_Nor1','SRF_Pullup','SRF_PMOSA','BND_{}Layer'.format(_Slv_Nor1_PMOS_XVT))
        tmp2 = self.get_param_KJH4('SRF_Slv_Nor1','SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        XvtDown2Nbody_tmp = abs( tmp2[0][0][0][0][0]['_XY_down'][1] - tmp1[0][0][0][0][0]['_XY_down'][1] )

        if XvtDown2Nbody_tmp > XvtDown2Nbody:
            XvtDown2Nbody = XvtDown2Nbody_tmp

        tmp3 =  self.get_param_KJH4('SRF_Slv_Nor1','SRF_Pulldown','SRF_NMOSA','BND_{}Layer'.format(_Slv_Nor1_NMOS_XVT))
        tmp4 =  self.get_param_KJH4('SRF_Slv_Nor1', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        XvtTop2Pbody_tmp= abs( tmp3[0][0][0][0][0]['_XY_up'][1] - tmp4[0][0][0][0][0]['_XY_up'][1]  )

        if XvtTop2Pbody_tmp > XvtTop2Pbody:
            XvtTop2Pbody = XvtTop2Pbody_tmp

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Slv: Nor2
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D02_02_Nor_KJH0._Nor._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOSA_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOSA_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOSA_NumberofGate']                 = _Slv_Nor2_NMOSA_NumberofGate
        _Caculation_Parameters['_NMOSA_ChannelWidth']                 = _Slv_Nor2_NMOSA_ChannelWidth
        _Caculation_Parameters['_NMOSA_ChannelLength']                = _Slv_Nor2_NMOSA_ChannelLength
        _Caculation_Parameters['_NMOSA_GateSpacing']                  = None
        _Caculation_Parameters['_NMOSA_SDWidth']                      = None
        _Caculation_Parameters['_NMOSA_XVT']                          = _Slv_Nor2_NMOS_XVT
        _Caculation_Parameters['_NMOSA_PCCrit']                       = True

        _Caculation_Parameters['_NMOSA_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOSA_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOSA_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOSA_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOSA_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOSA_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOSA_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOSA_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOSA_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOSA_Drain_Comb_Length']            = None

        _Caculation_Parameters['_NMOSA_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOSA_PODummy_Length']               = None
        _Caculation_Parameters['_NMOSA_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOSA_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOSA_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOSA_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOSA_POGate_Comb_length']           = _Slv_Nor2_NMOSA_POGate_Comb_length
        _Caculation_Parameters['_NMOSA_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOSA_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_NMOSB_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOSB_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOSB_NumberofGate']                 = _Slv_Nor2_NMOSB_NumberofGate
        _Caculation_Parameters['_NMOSB_ChannelWidth']                 = _Slv_Nor2_NMOSB_ChannelWidth
        _Caculation_Parameters['_NMOSB_ChannelLength']                = _Slv_Nor2_NMOSB_ChannelLength
        _Caculation_Parameters['_NMOSB_GateSpacing']                  = None
        _Caculation_Parameters['_NMOSB_SDWidth']                      = None
        _Caculation_Parameters['_NMOSB_XVT']                          = _Slv_Nor2_NMOS_XVT
        _Caculation_Parameters['_NMOSB_PCCrit']                       = True

        _Caculation_Parameters['_NMOSB_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOSB_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOSB_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOSB_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOSB_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOSB_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOSB_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOSB_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOSB_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOSB_Drain_Comb_Length']            = None

        _Caculation_Parameters['_NMOSB_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOSB_PODummy_Length']               = None
        _Caculation_Parameters['_NMOSB_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOSB_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOSB_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOSB_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOSB_POGate_Comb_length']           = _Slv_Nor2_NMOSB_POGate_Comb_length
        _Caculation_Parameters['_NMOSB_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOSB_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOSA_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOSA_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOSA_NumberofGate']                 = _Slv_Nor2_PMOSA_NumberofGate
        _Caculation_Parameters['_PMOSA_ChannelWidth']                 = _Slv_Nor2_PMOSA_ChannelWidth
        _Caculation_Parameters['_PMOSA_ChannelLength']                = _Slv_Nor2_PMOSA_ChannelLength
        _Caculation_Parameters['_PMOSA_GateSpacing']                  = None
        _Caculation_Parameters['_PMOSA_SDWidth']                      = None
        _Caculation_Parameters['_PMOSA_XVT']                          = _Slv_Nor2_PMOS_XVT
        _Caculation_Parameters['_PMOSA_PCCrit']                       = True

        _Caculation_Parameters['_PMOSA_Source_Via_TF']                = False
        _Caculation_Parameters['_PMOSA_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_PMOSA_Source_Comb_TF']               = False
        _Caculation_Parameters['_PMOSA_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOSA_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOSA_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOSA_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_PMOSA_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOSA_Drain_Comb_POpinward_TF']      = False
        _Caculation_Parameters['_PMOSA_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PMOSA_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOSA_PODummy_Length']               = None
        _Caculation_Parameters['_PMOSA_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOSA_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOSA_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOSA_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOSA_POGate_Comb_length']           = _Slv_Nor2_PMOSA_POGate_Comb_length
        _Caculation_Parameters['_PMOSA_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOSA_POGate_ViaMxMx']               = [0,1]



        _Caculation_Parameters['_PMOSB_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOSB_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOSB_NumberofGate']                 = _Slv_Nor2_PMOSB_NumberofGate
        _Caculation_Parameters['_PMOSB_ChannelWidth']                 = _Slv_Nor2_PMOSB_ChannelWidth
        _Caculation_Parameters['_PMOSB_ChannelLength']                = _Slv_Nor2_PMOSB_ChannelLength
        _Caculation_Parameters['_PMOSB_GateSpacing']                  = None
        _Caculation_Parameters['_PMOSB_SDWidth']                      = None
        _Caculation_Parameters['_PMOSB_XVT']                          = _Slv_Nor2_PMOS_XVT
        _Caculation_Parameters['_PMOSB_PCCrit']                       = True

        _Caculation_Parameters['_PMOSB_Source_Via_TF']                = True
        _Caculation_Parameters['_PMOSB_Source_Via_Close2POpin_TF']    = True
        _Caculation_Parameters['_PMOSB_Source_Comb_TF']               = True
        _Caculation_Parameters['_PMOSB_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOSB_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOSB_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOSB_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_PMOSB_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOSB_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOSB_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PMOSB_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOSB_PODummy_Length']               = None
        _Caculation_Parameters['_PMOSB_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOSB_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOSB_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOSB_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOSB_POGate_Comb_length']           = _Slv_Nor2_PMOSB_POGate_Comb_length
        _Caculation_Parameters['_PMOSB_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOSB_POGate_ViaMxMx']               = [0,1]



        _Caculation_Parameters['_NMOSAB_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOSAB_Pbody_XvtTop2Pbody']           = _DFF_XvtTop2Pbody
        _Caculation_Parameters['_PMOSAB_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOSAB_Nbody_Xvtdown2Nbody']          = _DFF_Xvtdown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                     = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Slv_Nor2'] = self._SrefElementDeclaration(_DesignObj=D02_02_Nor_KJH0._Nor(_DesignParameter=None, _Name='{}:SRF_Slv_Nor2'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Slv_Nor2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Nor2']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Nor2']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Nor2']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Slv_Nor2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        tmp1_1 = self.get_param_KJH4('SRF_Slv_Nor1','SRF_Pullup','SRF_PMOSB','BND_PODummyLayer')
        target_coordx = tmp1_1[0][0][0][-1][0]['_XY_right'][0]
                                ##y
        tmp1_2 = self.get_param_KJH4('SRF_Slv_Nor1','SRF_Pullup','SRF_PMOSB','BND_{}Layer'.format(_Slv_Nor1_PMOS_XVT))
        target_coordy = tmp1_2[0][0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##X
        tmp2_1 = self.get_param_KJH4('SRF_Slv_Nor2','SRF_Pullup','SRF_PMOSA','BND_PODummyLayer')
        approaching_coordx = tmp2_1[0][0][0][0][0]['_XY_left'][0]
                                ##Y
        tmp2_2 = self.get_param_KJH4('SRF_Slv_Nor2','SRF_Pullup','SRF_PMOSA','BND_{}Layer'.format(_Slv_Nor2_PMOS_XVT))
        approaching_coordy = tmp2_2[0][0][0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Slv_Nor2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] +  _Test_distance
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Slv_Nor2']['_XYCoordinates'] = tmpXY


        ## Find XvtTop2Pbody_tmp and XvtDown2Nbody_tmp
        tmp1 = self.get_param_KJH4('SRF_Slv_Nor2','SRF_Pullup','SRF_PMOSA','BND_{}Layer'.format(_Slv_Nor2_PMOS_XVT))
        tmp2 = self.get_param_KJH4('SRF_Slv_Nor2','SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        XvtDown2Nbody_tmp = abs( tmp2[0][0][0][0][0]['_XY_down'][1] - tmp1[0][0][0][0][0]['_XY_down'][1] )

        if XvtDown2Nbody_tmp > XvtDown2Nbody:
            XvtDown2Nbody = XvtDown2Nbody_tmp

        tmp3 =  self.get_param_KJH4('SRF_Slv_Nor2','SRF_Pulldown','SRF_NMOSA','BND_{}Layer'.format(_Slv_Nor2_NMOS_XVT))
        tmp4 =  self.get_param_KJH4('SRF_Slv_Nor2', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        XvtTop2Pbody_tmp = abs( tmp3[0][0][0][0][0]['_XY_up'][1] - tmp4[0][0][0][0][0]['_XY_up'][1]  )

        if XvtTop2Pbody_tmp > XvtTop2Pbody:
            XvtTop2Pbody = XvtTop2Pbody_tmp


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Slv: Inv1: Set pre-driver
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D00_00_Inverter_KJH._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOS_NumberofGate']                 = _Slv_Inv1_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth']                 = _Slv_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength']                = _Slv_Inv1_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing']                  = None
        _Caculation_Parameters['_NMOS_SDWidth']                      = None
        _Caculation_Parameters['_NMOS_XVT']                          = _Slv_Inv1_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit']                       = True

        _Caculation_Parameters['_NMOS_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOS_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOS_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOS_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOS_Drain_Comb_Length']            = 0

        _Caculation_Parameters['_NMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOS_PODummy_Length']               = None
        _Caculation_Parameters['_NMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOS_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_POGate_Comb_length']           = _Slv_Inv1_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOS_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOS_NumberofGate']                 = _Slv_Inv1_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth']                 = _Slv_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength']                = _Slv_Inv1_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing']                  = None
        _Caculation_Parameters['_PMOS_SDWidth']                      = None
        _Caculation_Parameters['_PMOS_XVT']                          = _Slv_Inv1_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit']                       = True

        _Caculation_Parameters['_PMOS_Source_Via_TF']                = False
        _Caculation_Parameters['_PMOS_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_PMOS_Source_Comb_TF']               = False
        _Caculation_Parameters['_PMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOS_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_PMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOS_Drain_Comb_Length']            = 0

        _Caculation_Parameters['_PMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOS_PODummy_Length']               = None
        _Caculation_Parameters['_PMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOS_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_POGate_Comb_length']           = _Slv_Inv1_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx']               = [0,1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']           = _DFF_XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody']          = _DFF_Xvtdown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                   = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Slv_Inv1'] = self._SrefElementDeclaration(_DesignObj=D00_00_Inverter_KJH._Inverter(_DesignParameter=None, _Name='{}:SRF_Slv_Inv1'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Slv_Inv1']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Inv1']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Inv1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Inv1']['_XYCoordinates'] = [[0, 0]]


                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Slv_Inv1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        tmp1_1 = self.get_param_KJH4('SRF_Slv_Nor2','SRF_Pullup','SRF_PMOSB','BND_PODummyLayer')
        target_coordx = tmp1_1[0][0][0][-1][0]['_XY_right'][0]
                                ##y
        tmp1_2 = self.get_param_KJH4('SRF_Slv_Nor2','SRF_Pullup','SRF_PMOSB','BND_{}Layer'.format(_Slv_Nor2_PMOS_XVT))
        target_coordy = tmp1_2[0][0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##X
        tmp2_1 = self.get_param_KJH4('SRF_Slv_Inv1','SRF_PMOS','BND_PODummyLayer')
        approaching_coordx = tmp2_1[0][0][0][0]['_XY_left'][0]
                                ##Y
        tmp2_2 = self.get_param_KJH4('SRF_Slv_Inv1','SRF_PMOS','BND_{}Layer'.format(_Slv_Inv1_PMOS_XVT))
        approaching_coordy = tmp2_2[0][0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Slv_Inv1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] +  _Test_distance
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Slv_Inv1']['_XYCoordinates'] = tmpXY

        ## Find XvtTop2Pbody_tmp and XvtDown2Nbody_tmp
        tmp1 = self.get_param_KJH4('SRF_Slv_Inv1','SRF_PMOS','BND_{}Layer'.format(_Slv_Inv1_PMOS_XVT))
        tmp2 = self.get_param_KJH4('SRF_Slv_Inv1','SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        XvtDown2Nbody_tmp = abs( tmp2[0][0][0][0][0]['_XY_down'][1] - tmp1[0][0][0][0]['_XY_down'][1] )

        if XvtDown2Nbody_tmp > XvtDown2Nbody:
            XvtDown2Nbody = XvtDown2Nbody_tmp

        tmp3 =  self.get_param_KJH4('SRF_Slv_Inv1','SRF_NMOS','BND_{}Layer'.format(_Slv_Inv1_NMOS_XVT))
        tmp4 =  self.get_param_KJH4('SRF_Slv_Inv1', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        XvtTop2Pbody_tmp = abs( tmp3[0][0][0][0]['_XY_up'][1] - tmp4[0][0][0][0][0]['_XY_up'][1]  )

        if XvtTop2Pbody_tmp > XvtTop2Pbody:
            XvtTop2Pbody = XvtTop2Pbody_tmp


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Slv: Inv2: ReSet driver
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D00_00_Inverter_KJH._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOS_NumberofGate']                 = _Slv_Inv2_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth']                 = _Slv_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength']                = _Slv_Inv2_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing']                  = None
        _Caculation_Parameters['_NMOS_SDWidth']                      = None
        _Caculation_Parameters['_NMOS_XVT']                          = _Slv_Inv2_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit']                       = True

        _Caculation_Parameters['_NMOS_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOS_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOS_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOS_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOS_Drain_Comb_Length']            = 0

        _Caculation_Parameters['_NMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOS_PODummy_Length']               = None
        _Caculation_Parameters['_NMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOS_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_POGate_Comb_length']           = _Slv_Inv2_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOS_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOS_NumberofGate']                 = _Slv_Inv2_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth']                 = _Slv_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength']                = _Slv_Inv2_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing']                  = None
        _Caculation_Parameters['_PMOS_SDWidth']                      = None
        _Caculation_Parameters['_PMOS_XVT']                          = _Slv_Inv2_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit']                       = True

        _Caculation_Parameters['_PMOS_Source_Via_TF']                = False
        _Caculation_Parameters['_PMOS_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_PMOS_Source_Comb_TF']               = False
        _Caculation_Parameters['_PMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOS_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_PMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOS_Drain_Comb_Length']            = 0

        _Caculation_Parameters['_PMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOS_PODummy_Length']               = None
        _Caculation_Parameters['_PMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOS_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_POGate_Comb_length']           = _Slv_Inv2_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx']               = [0,1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']           = _DFF_XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody']          = _DFF_Xvtdown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                   = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Slv_Inv2'] = self._SrefElementDeclaration(_DesignObj=D00_00_Inverter_KJH._Inverter(_DesignParameter=None, _Name='{}:SRF_Slv_Inv2'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Slv_Inv2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Inv2']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Inv2']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Inv2']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Slv_Inv2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        tmp1_1 = self.get_param_KJH4('SRF_Slv_Inv1','SRF_PMOS','BND_PODummyLayer')
        target_coordx = tmp1_1[0][0][-1][0]['_XY_right'][0]
                                ##y
        tmp1_2 = self.get_param_KJH4('SRF_Slv_Inv1','SRF_PMOS','BND_{}Layer'.format(_Slv_Inv1_PMOS_XVT))
        target_coordy = tmp1_2[0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##X
        tmp2_1 = self.get_param_KJH4('SRF_Slv_Inv2','SRF_PMOS','BND_PODummyLayer')
        approaching_coordx = tmp2_1[0][0][0][0]['_XY_left'][0]
                                ##Y
        tmp2_2 = self.get_param_KJH4('SRF_Slv_Inv2','SRF_PMOS','BND_{}Layer'.format(_Slv_Inv2_PMOS_XVT))
        approaching_coordy = tmp2_2[0][0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Slv_Inv2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] +  _Test_distance
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Slv_Inv2']['_XYCoordinates'] = tmpXY

        ## Find XvtTop2Pbody_tmp and XvtDown2Nbody_tmp
        tmp1 = self.get_param_KJH4('SRF_Slv_Inv2','SRF_PMOS','BND_{}Layer'.format(_Slv_Inv2_PMOS_XVT))
        tmp2 = self.get_param_KJH4('SRF_Slv_Inv2','SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        XvtDown2Nbody_tmp = abs( tmp2[0][0][0][0][0]['_XY_down'][1] - tmp1[0][0][0][0]['_XY_down'][1] )

        if XvtDown2Nbody_tmp > XvtDown2Nbody:
            XvtDown2Nbody = XvtDown2Nbody_tmp

        tmp3 =  self.get_param_KJH4('SRF_Slv_Inv2','SRF_NMOS','BND_{}Layer'.format(_Slv_Inv2_NMOS_XVT))
        tmp4 =  self.get_param_KJH4('SRF_Slv_Inv2', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        XvtTop2Pbody_tmp = abs( tmp3[0][0][0][0]['_XY_up'][1] - tmp4[0][0][0][0][0]['_XY_up'][1]  )

        if XvtTop2Pbody_tmp > XvtTop2Pbody:
            XvtTop2Pbody = XvtTop2Pbody_tmp

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Slv: Inv3: Qb driver
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D00_00_Inverter_KJH._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOS_NumberofGate']                 = _Slv_Inv3_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth']                 = _Slv_Inv3_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength']                = _Slv_Inv3_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing']                  = None
        _Caculation_Parameters['_NMOS_SDWidth']                      = None
        _Caculation_Parameters['_NMOS_XVT']                          = _Slv_Inv3_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit']                       = True

        _Caculation_Parameters['_NMOS_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOS_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOS_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOS_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOS_Drain_Comb_Length']            = 0

        _Caculation_Parameters['_NMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOS_PODummy_Length']               = None
        _Caculation_Parameters['_NMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOS_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_POGate_Comb_length']           = _Slv_Inv3_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOS_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOS_NumberofGate']                 = _Slv_Inv3_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth']                 = _Slv_Inv3_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength']                = _Slv_Inv3_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing']                  = None
        _Caculation_Parameters['_PMOS_SDWidth']                      = None
        _Caculation_Parameters['_PMOS_XVT']                          = _Slv_Inv3_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit']                       = True

        _Caculation_Parameters['_PMOS_Source_Via_TF']                = False
        _Caculation_Parameters['_PMOS_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_PMOS_Source_Comb_TF']               = False
        _Caculation_Parameters['_PMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOS_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_PMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOS_Drain_Comb_Length']            = 0

        _Caculation_Parameters['_PMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOS_PODummy_Length']               = None
        _Caculation_Parameters['_PMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOS_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_POGate_Comb_length']           = _Slv_Inv3_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx']               = [0,1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']           = _DFF_XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody']          = _DFF_Xvtdown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                   = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Slv_Inv3'] = self._SrefElementDeclaration(_DesignObj=D00_00_Inverter_KJH._Inverter(_DesignParameter=None, _Name='{}:SRF_Slv_Inv3'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Slv_Inv3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Inv3']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Inv3']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Inv3']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Slv_Inv3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        tmp1_1 = self.get_param_KJH4('SRF_Slv_Inv2','SRF_PMOS','BND_PODummyLayer')
        target_coordx = tmp1_1[0][0][-1][0]['_XY_right'][0]
                                ##y
        tmp1_2 = self.get_param_KJH4('SRF_Slv_Inv2','SRF_PMOS','BND_{}Layer'.format(_Slv_Inv1_PMOS_XVT))
        target_coordy = tmp1_2[0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##X
        tmp2_1 = self.get_param_KJH4('SRF_Slv_Inv3','SRF_PMOS','BND_PODummyLayer')
        approaching_coordx = tmp2_1[0][0][0][0]['_XY_left'][0]
                                ##Y
        tmp2_2 = self.get_param_KJH4('SRF_Slv_Inv3','SRF_PMOS','BND_{}Layer'.format(_Slv_Inv2_PMOS_XVT))
        approaching_coordy = tmp2_2[0][0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Slv_Inv3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] +  _Test_distance
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Slv_Inv3']['_XYCoordinates'] = tmpXY

        ## Find XvtTop2Pbody_tmp and XvtDown2Nbody_tmp
        tmp1 = self.get_param_KJH4('SRF_Slv_Inv3','SRF_PMOS','BND_{}Layer'.format(_Slv_Inv3_PMOS_XVT))
        tmp2 = self.get_param_KJH4('SRF_Slv_Inv3','SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        XvtDown2Nbody_tmp = abs( tmp2[0][0][0][0][0]['_XY_down'][1] - tmp1[0][0][0][0]['_XY_down'][1] )

        if XvtDown2Nbody_tmp > XvtDown2Nbody:
            XvtDown2Nbody = XvtDown2Nbody_tmp

        tmp3 =  self.get_param_KJH4('SRF_Slv_Inv3','SRF_NMOS','BND_{}Layer'.format(_Slv_Inv3_NMOS_XVT))
        tmp4 =  self.get_param_KJH4('SRF_Slv_Inv3', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        XvtTop2Pbody_tmp = abs( tmp3[0][0][0][0]['_XY_up'][1] - tmp4[0][0][0][0][0]['_XY_up'][1]  )

        if XvtTop2Pbody_tmp > XvtTop2Pbody:
            XvtTop2Pbody = XvtTop2Pbody_tmp















































































        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Apply XvtDown2Nbody XvtTop2Pbody
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## MST
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Mst: Xgate1
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D01_00_Xgate_KJH._Xgate._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOS_NumberofGate']                 = _Mst_Xgate1_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth']                 = _Mst_Xgate1_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength']                = _Mst_Xgate1_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing']                  = None
        _Caculation_Parameters['_NMOS_SDWidth']                      = None
        _Caculation_Parameters['_NMOS_XVT']                          = _Mst_Xgate1_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit']                       = True

        _Caculation_Parameters['_NMOS_Source_Via_TF']                = True
        _Caculation_Parameters['_NMOS_Source_Via_Close2POpin_TF']    = True
        _Caculation_Parameters['_NMOS_Source_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOS_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_NMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOS_Drain_Comb_Length']            = None

        _Caculation_Parameters['_NMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOS_PODummy_Length']               = None
        _Caculation_Parameters['_NMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOS_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_POGate_Comb_length']           = _Mst_Xgate1_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOS_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOS_NumberofGate']                 = _Mst_Xgate1_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth']                 = _Mst_Xgate1_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength']                = _Mst_Xgate1_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing']                  = None
        _Caculation_Parameters['_PMOS_SDWidth']                      = None
        _Caculation_Parameters['_PMOS_XVT']                          = _Mst_Xgate1_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit']                       = True

        _Caculation_Parameters['_PMOS_Source_Via_TF']                = True
        _Caculation_Parameters['_PMOS_Source_Via_Close2POpin_TF']    = True
        _Caculation_Parameters['_PMOS_Source_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOS_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_PMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOS_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOS_PODummy_Length']               = None
        _Caculation_Parameters['_PMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOS_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_POGate_Comb_length']           = _Mst_Xgate1_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx']               = [0,1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']           = XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody']          = XvtDown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                   = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Mst_Xgate1'] = self._SrefElementDeclaration(_DesignObj=D01_00_Xgate_KJH._Xgate(_DesignParameter=None, _Name='{}:SRF_Mst_Xgate1'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Mst_Xgate1']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Xgate1']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Xgate1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Xgate1']['_XYCoordinates'] = [[0, 0]]


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Mst: Xgate2
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D01_00_Xgate_KJH._Xgate._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOS_NumberofGate']                 = _Mst_Xgate2_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth']                 = _Mst_Xgate2_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength']                = _Mst_Xgate2_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing']                  = None
        _Caculation_Parameters['_NMOS_SDWidth']                      = None
        _Caculation_Parameters['_NMOS_XVT']                          = _Mst_Xgate2_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit']                       = True

        _Caculation_Parameters['_NMOS_Source_Via_TF']                = True
        _Caculation_Parameters['_NMOS_Source_Via_Close2POpin_TF']    = True
        _Caculation_Parameters['_NMOS_Source_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOS_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_NMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOS_Drain_Comb_Length']            = None

        _Caculation_Parameters['_NMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOS_PODummy_Length']               = None
        _Caculation_Parameters['_NMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOS_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_POGate_Comb_length']           = _Mst_Xgate2_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOS_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOS_NumberofGate']                 = _Mst_Xgate2_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth']                 = _Mst_Xgate2_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength']                = _Mst_Xgate2_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing']                  = None
        _Caculation_Parameters['_PMOS_SDWidth']                      = None
        _Caculation_Parameters['_PMOS_XVT']                          = _Mst_Xgate2_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit']                       = True

        _Caculation_Parameters['_PMOS_Source_Via_TF']                = True
        _Caculation_Parameters['_PMOS_Source_Via_Close2POpin_TF']    = True
        _Caculation_Parameters['_PMOS_Source_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOS_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_PMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOS_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOS_PODummy_Length']               = None
        _Caculation_Parameters['_PMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOS_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_POGate_Comb_length']           = _Mst_Xgate2_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx']               = [0,1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']           = XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody']          = XvtDown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                   = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Mst_Xgate2'] = self._SrefElementDeclaration(_DesignObj=D01_00_Xgate_KJH._Xgate(_DesignParameter=None, _Name='{}:SRF_Mst_Xgate2'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Mst_Xgate2']['_Reflect'] = [1, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Xgate2']['_Angle'] = 180

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Xgate2']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Xgate2']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Mst_Xgate2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        tmp1_1 = self.get_param_KJH4('SRF_Mst_Xgate1','SRF_PMOS','BND_PODummyLayer')
        tmp1_2 = self.get_param_KJH4('SRF_Mst_Xgate1','SRF_NMOS','BND_PODummyLayer')
        target_coordx = max(tmp1_1[0][0][-1][0]['_XY_right'][0], tmp1_2[0][0][-1][0]['_XY_right'][0])
                                ##y
        tmp1_3 = self.get_param_KJH4('SRF_Mst_Xgate1','SRF_PMOS','BND_{}Layer'.format(_Mst_Xgate1_PMOS_XVT))
        target_coordy = tmp1_3[0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##X
        tmp2_1 = self.get_param_KJH4('SRF_Mst_Xgate2','SRF_PMOS','BND_PODummyLayer')
        tmp2_2 = self.get_param_KJH4('SRF_Mst_Xgate2','SRF_NMOS','BND_PODummyLayer')
        approaching_coordx = min(tmp2_1[0][0][-1][0]['_XY_right'][0],tmp2_2[0][0][-1][0]['_XY_right'][0])
                                ##Y
        tmp2_3 = self.get_param_KJH4('SRF_Mst_Xgate2','SRF_PMOS','BND_{}Layer'.format(_Mst_Xgate2_PMOS_XVT))
        approaching_coordy = tmp2_3[0][0][0][0]['_XY_down'][1]

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


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Mst: Nor1
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D02_02_Nor_KJH0._Nor._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOSA_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOSA_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOSA_NumberofGate']                 = _Mst_Nor1_NMOSA_NumberofGate
        _Caculation_Parameters['_NMOSA_ChannelWidth']                 = _Mst_Nor1_NMOSA_ChannelWidth
        _Caculation_Parameters['_NMOSA_ChannelLength']                = _Mst_Nor1_NMOSA_ChannelLength
        _Caculation_Parameters['_NMOSA_GateSpacing']                  = None
        _Caculation_Parameters['_NMOSA_SDWidth']                      = None
        _Caculation_Parameters['_NMOSA_XVT']                          = _Mst_Nor1_NMOS_XVT
        _Caculation_Parameters['_NMOSA_PCCrit']                       = True

        _Caculation_Parameters['_NMOSA_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOSA_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOSA_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOSA_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOSA_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOSA_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOSA_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOSA_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOSA_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOSA_Drain_Comb_Length']            = None

        _Caculation_Parameters['_NMOSA_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOSA_PODummy_Length']               = None
        _Caculation_Parameters['_NMOSA_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOSA_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOSA_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOSA_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOSA_POGate_Comb_length']           = _Mst_Nor1_NMOSA_POGate_Comb_length
        _Caculation_Parameters['_NMOSA_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOSA_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_NMOSB_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOSB_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOSB_NumberofGate']                 = _Mst_Nor1_NMOSB_NumberofGate
        _Caculation_Parameters['_NMOSB_ChannelWidth']                 = _Mst_Nor1_NMOSB_ChannelWidth
        _Caculation_Parameters['_NMOSB_ChannelLength']                = _Mst_Nor1_NMOSB_ChannelLength
        _Caculation_Parameters['_NMOSB_GateSpacing']                  = None
        _Caculation_Parameters['_NMOSB_SDWidth']                      = None
        _Caculation_Parameters['_NMOSB_XVT']                          = _Mst_Nor1_NMOS_XVT
        _Caculation_Parameters['_NMOSB_PCCrit']                       = True

        _Caculation_Parameters['_NMOSB_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOSB_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOSB_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOSB_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOSB_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOSB_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOSB_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOSB_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOSB_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOSB_Drain_Comb_Length']            = None

        _Caculation_Parameters['_NMOSB_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOSB_PODummy_Length']               = None
        _Caculation_Parameters['_NMOSB_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOSB_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOSB_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOSB_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOSB_POGate_Comb_length']           = _Mst_Nor1_NMOSB_POGate_Comb_length
        _Caculation_Parameters['_NMOSB_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOSB_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOSA_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOSA_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOSA_NumberofGate']                 = _Mst_Nor1_PMOSA_NumberofGate
        _Caculation_Parameters['_PMOSA_ChannelWidth']                 = _Mst_Nor1_PMOSA_ChannelWidth
        _Caculation_Parameters['_PMOSA_ChannelLength']                = _Mst_Nor1_PMOSA_ChannelLength
        _Caculation_Parameters['_PMOSA_GateSpacing']                  = None
        _Caculation_Parameters['_PMOSA_SDWidth']                      = None
        _Caculation_Parameters['_PMOSA_XVT']                          = _Mst_Nor1_PMOS_XVT
        _Caculation_Parameters['_PMOSA_PCCrit']                       = True

        _Caculation_Parameters['_PMOSA_Source_Via_TF']                = False
        _Caculation_Parameters['_PMOSA_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_PMOSA_Source_Comb_TF']               = False
        _Caculation_Parameters['_PMOSA_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOSA_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOSA_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOSA_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_PMOSA_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOSA_Drain_Comb_POpinward_TF']      = False
        _Caculation_Parameters['_PMOSA_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PMOSA_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOSA_PODummy_Length']               = None
        _Caculation_Parameters['_PMOSA_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOSA_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOSA_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOSA_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOSA_POGate_Comb_length']           = _Mst_Nor1_PMOSA_POGate_Comb_length
        _Caculation_Parameters['_PMOSA_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOSA_POGate_ViaMxMx']               = [0,1]



        _Caculation_Parameters['_PMOSB_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOSB_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOSB_NumberofGate']                 = _Mst_Nor1_PMOSB_NumberofGate
        _Caculation_Parameters['_PMOSB_ChannelWidth']                 = _Mst_Nor1_PMOSB_ChannelWidth
        _Caculation_Parameters['_PMOSB_ChannelLength']                = _Mst_Nor1_PMOSB_ChannelLength
        _Caculation_Parameters['_PMOSB_GateSpacing']                  = None
        _Caculation_Parameters['_PMOSB_SDWidth']                      = None
        _Caculation_Parameters['_PMOSB_XVT']                          = _Mst_Nor1_PMOS_XVT
        _Caculation_Parameters['_PMOSB_PCCrit']                       = True

        _Caculation_Parameters['_PMOSB_Source_Via_TF']                = True
        _Caculation_Parameters['_PMOSB_Source_Via_Close2POpin_TF']    = True
        _Caculation_Parameters['_PMOSB_Source_Comb_TF']               = True
        _Caculation_Parameters['_PMOSB_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOSB_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOSB_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOSB_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_PMOSB_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOSB_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOSB_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PMOSB_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOSB_PODummy_Length']               = None
        _Caculation_Parameters['_PMOSB_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOSB_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOSB_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOSB_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOSB_POGate_Comb_length']           = _Mst_Nor1_PMOSB_POGate_Comb_length
        _Caculation_Parameters['_PMOSB_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOSB_POGate_ViaMxMx']               = [0,1]



        _Caculation_Parameters['_NMOSAB_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOSAB_Pbody_XvtTop2Pbody']           = XvtTop2Pbody
        _Caculation_Parameters['_PMOSAB_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOSAB_Nbody_Xvtdown2Nbody']          = XvtDown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                     = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Mst_Nor1'] = self._SrefElementDeclaration(_DesignObj=D02_02_Nor_KJH0._Nor(_DesignParameter=None, _Name='{}:SRF_Mst_Nor1'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Mst_Nor1']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Nor1']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Nor1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Nor1']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Mst_Nor1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        tmp1_1 = self.get_param_KJH4('SRF_Mst_Xgate2','SRF_PMOS','BND_PODummyLayer')
        tmp1_2 = self.get_param_KJH4('SRF_Mst_Xgate2','SRF_NMOS','BND_PODummyLayer')
        target_coordx = max(tmp1_1[0][0][0][0]['_XY_left'][0],tmp1_2[0][0][0][0]['_XY_left'][0])
                                ##y
        tmp1_3 = self.get_param_KJH4('SRF_Mst_Xgate2','SRF_PMOS','BND_{}Layer'.format(_Mst_Xgate2_PMOS_XVT))
        target_coordy = tmp1_3[0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##X
        tmp2_1 = self.get_param_KJH4('SRF_Mst_Nor1','SRF_Pullup','SRF_PMOSA','BND_PODummyLayer')
        tmp2_2 = self.get_param_KJH4('SRF_Mst_Nor1','SRF_Pulldown','SRF_NMOSA','BND_PODummyLayer')
        approaching_coordx = min(tmp2_1[0][0][0][0][0]['_XY_left'][0],tmp2_2[0][0][0][0][0]['_XY_left'][0])
                                ##Y
        tmp2_3 = self.get_param_KJH4('SRF_Mst_Nor1','SRF_Pullup','SRF_PMOSA','BND_{}Layer'.format(_Mst_Nor1_PMOS_XVT))
        approaching_coordy = tmp2_3[0][0][0][0][0]['_XY_down'][1]

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


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Mst: Nor2
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D02_02_Nor_KJH0._Nor._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOSA_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOSA_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOSA_NumberofGate']                 = _Mst_Nor2_NMOSA_NumberofGate
        _Caculation_Parameters['_NMOSA_ChannelWidth']                 = _Mst_Nor2_NMOSA_ChannelWidth
        _Caculation_Parameters['_NMOSA_ChannelLength']                = _Mst_Nor2_NMOSA_ChannelLength
        _Caculation_Parameters['_NMOSA_GateSpacing']                  = None
        _Caculation_Parameters['_NMOSA_SDWidth']                      = None
        _Caculation_Parameters['_NMOSA_XVT']                          = _Mst_Nor2_NMOS_XVT
        _Caculation_Parameters['_NMOSA_PCCrit']                       = True

        _Caculation_Parameters['_NMOSA_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOSA_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOSA_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOSA_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOSA_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOSA_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOSA_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOSA_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOSA_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOSA_Drain_Comb_Length']            = None

        _Caculation_Parameters['_NMOSA_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOSA_PODummy_Length']               = None
        _Caculation_Parameters['_NMOSA_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOSA_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOSA_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOSA_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOSA_POGate_Comb_length']           = _Mst_Nor2_NMOSA_POGate_Comb_length
        _Caculation_Parameters['_NMOSA_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOSA_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_NMOSB_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOSB_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOSB_NumberofGate']                 = _Mst_Nor2_NMOSB_NumberofGate
        _Caculation_Parameters['_NMOSB_ChannelWidth']                 = _Mst_Nor2_NMOSB_ChannelWidth
        _Caculation_Parameters['_NMOSB_ChannelLength']                = _Mst_Nor2_NMOSB_ChannelLength
        _Caculation_Parameters['_NMOSB_GateSpacing']                  = None
        _Caculation_Parameters['_NMOSB_SDWidth']                      = None
        _Caculation_Parameters['_NMOSB_XVT']                          = _Mst_Nor2_NMOS_XVT
        _Caculation_Parameters['_NMOSB_PCCrit']                       = True

        _Caculation_Parameters['_NMOSB_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOSB_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOSB_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOSB_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOSB_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOSB_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOSB_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOSB_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOSB_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOSB_Drain_Comb_Length']            = None

        _Caculation_Parameters['_NMOSB_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOSB_PODummy_Length']               = None
        _Caculation_Parameters['_NMOSB_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOSB_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOSB_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOSB_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOSB_POGate_Comb_length']           = _Mst_Nor2_NMOSB_POGate_Comb_length
        _Caculation_Parameters['_NMOSB_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOSB_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOSA_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOSA_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOSA_NumberofGate']                 = _Mst_Nor2_PMOSA_NumberofGate
        _Caculation_Parameters['_PMOSA_ChannelWidth']                 = _Mst_Nor2_PMOSA_ChannelWidth
        _Caculation_Parameters['_PMOSA_ChannelLength']                = _Mst_Nor2_PMOSA_ChannelLength
        _Caculation_Parameters['_PMOSA_GateSpacing']                  = None
        _Caculation_Parameters['_PMOSA_SDWidth']                      = None
        _Caculation_Parameters['_PMOSA_XVT']                          = _Mst_Nor2_PMOS_XVT
        _Caculation_Parameters['_PMOSA_PCCrit']                       = True

        _Caculation_Parameters['_PMOSA_Source_Via_TF']                = False
        _Caculation_Parameters['_PMOSA_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_PMOSA_Source_Comb_TF']               = False
        _Caculation_Parameters['_PMOSA_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOSA_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOSA_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOSA_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_PMOSA_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOSA_Drain_Comb_POpinward_TF']      = False
        _Caculation_Parameters['_PMOSA_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PMOSA_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOSA_PODummy_Length']               = None
        _Caculation_Parameters['_PMOSA_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOSA_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOSA_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOSA_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOSA_POGate_Comb_length']           = _Mst_Nor2_PMOSA_POGate_Comb_length
        _Caculation_Parameters['_PMOSA_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOSA_POGate_ViaMxMx']               = [0,1]



        _Caculation_Parameters['_PMOSB_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOSB_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOSB_NumberofGate']                 = _Mst_Nor2_PMOSB_NumberofGate
        _Caculation_Parameters['_PMOSB_ChannelWidth']                 = _Mst_Nor2_PMOSB_ChannelWidth
        _Caculation_Parameters['_PMOSB_ChannelLength']                = _Mst_Nor2_PMOSB_ChannelLength
        _Caculation_Parameters['_PMOSB_GateSpacing']                  = None
        _Caculation_Parameters['_PMOSB_SDWidth']                      = None
        _Caculation_Parameters['_PMOSB_XVT']                          = _Mst_Nor2_PMOS_XVT
        _Caculation_Parameters['_PMOSB_PCCrit']                       = True

        _Caculation_Parameters['_PMOSB_Source_Via_TF']                = True
        _Caculation_Parameters['_PMOSB_Source_Via_Close2POpin_TF']    = True
        _Caculation_Parameters['_PMOSB_Source_Comb_TF']               = True
        _Caculation_Parameters['_PMOSB_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOSB_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOSB_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOSB_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_PMOSB_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOSB_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOSB_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PMOSB_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOSB_PODummy_Length']               = None
        _Caculation_Parameters['_PMOSB_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOSB_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOSB_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOSB_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOSB_POGate_Comb_length']           = _Mst_Nor2_PMOSB_POGate_Comb_length
        _Caculation_Parameters['_PMOSB_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOSB_POGate_ViaMxMx']               = [0,1]



        _Caculation_Parameters['_NMOSAB_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOSAB_Pbody_XvtTop2Pbody']           = XvtTop2Pbody
        _Caculation_Parameters['_PMOSAB_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOSAB_Nbody_Xvtdown2Nbody']          = XvtDown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                     = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Mst_Nor2'] = self._SrefElementDeclaration(_DesignObj=D02_02_Nor_KJH0._Nor(_DesignParameter=None, _Name='{}:SRF_Mst_Nor2'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Mst_Nor2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Nor2']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Nor2']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
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
        tmp1_2 = self.get_param_KJH4('SRF_Mst_Nor1','SRF_Pulldown','SRF_NMOSB','BND_PODummyLayer')
        target_coordx = max(tmp1_1[0][0][0][-1][0]['_XY_right'][0],tmp1_2[0][0][0][-1][0]['_XY_right'][0])
                                ##y
        tmp1_3 = self.get_param_KJH4('SRF_Mst_Nor1','SRF_Pullup','SRF_PMOSB','BND_{}Layer'.format(_Mst_Nor1_PMOS_XVT))
        target_coordy = tmp1_3[0][0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##X
        tmp2_1 = self.get_param_KJH4('SRF_Mst_Nor2','SRF_Pullup','SRF_PMOSA','BND_PODummyLayer')
        tmp2_2 = self.get_param_KJH4('SRF_Mst_Nor2','SRF_Pulldown','SRF_NMOSA','BND_PODummyLayer')
        approaching_coordx = min(tmp2_1[0][0][0][0][0]['_XY_left'][0],tmp2_2[0][0][0][0][0]['_XY_left'][0])
                                ##Y
        tmp2_3 = self.get_param_KJH4('SRF_Mst_Nor2','SRF_Pullup','SRF_PMOSA','BND_{}Layer'.format(_Mst_Nor2_PMOS_XVT))
        approaching_coordy = tmp2_3[0][0][0][0][0]['_XY_down'][1]

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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Mst: Inv1: Set pre-driver
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D00_00_Inverter_KJH._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOS_NumberofGate']                 = _Mst_Inv1_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth']                 = _Mst_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength']                = _Mst_Inv1_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing']                  = None
        _Caculation_Parameters['_NMOS_SDWidth']                      = None
        _Caculation_Parameters['_NMOS_XVT']                          = _Mst_Inv1_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit']                       = True

        _Caculation_Parameters['_NMOS_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOS_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOS_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOS_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOS_Drain_Comb_Length']            = 0

        _Caculation_Parameters['_NMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOS_PODummy_Length']               = None
        _Caculation_Parameters['_NMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOS_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_POGate_Comb_length']           = _Mst_Inv1_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOS_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOS_NumberofGate']                 = _Mst_Inv1_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth']                 = _Mst_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength']                = _Mst_Inv1_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing']                  = None
        _Caculation_Parameters['_PMOS_SDWidth']                      = None
        _Caculation_Parameters['_PMOS_XVT']                          = _Mst_Inv1_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit']                       = True

        _Caculation_Parameters['_PMOS_Source_Via_TF']                = False
        _Caculation_Parameters['_PMOS_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_PMOS_Source_Comb_TF']               = False
        _Caculation_Parameters['_PMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOS_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_PMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOS_Drain_Comb_Length']            = 0

        _Caculation_Parameters['_PMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOS_PODummy_Length']               = None
        _Caculation_Parameters['_PMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOS_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_POGate_Comb_length']           = _Mst_Inv1_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx']               = [0,1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']           = XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody']          = XvtDown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                   = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Mst_Inv1'] = self._SrefElementDeclaration(_DesignObj=D00_00_Inverter_KJH._Inverter(_DesignParameter=None, _Name='{}:SRF_Mst_Inv1'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Mst_Inv1']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Inv1']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Inv1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
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
        tmp1_2 = self.get_param_KJH4('SRF_Mst_Nor2','SRF_Pulldown','SRF_NMOSB','BND_PODummyLayer')
        target_coordx = max(tmp1_1[0][0][0][-1][0]['_XY_right'][0],tmp1_2[0][0][0][-1][0]['_XY_right'][0])
                                ##y
        tmp1_3 = self.get_param_KJH4('SRF_Mst_Nor2','SRF_Pullup','SRF_PMOSB','BND_{}Layer'.format(_Mst_Nor2_PMOS_XVT))
        target_coordy = tmp1_3[0][0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##X
        tmp2_1 = self.get_param_KJH4('SRF_Mst_Inv1','SRF_PMOS','BND_PODummyLayer')
        tmp2_2 = self.get_param_KJH4('SRF_Mst_Inv1','SRF_NMOS','BND_PODummyLayer')
        approaching_coordx = min(tmp2_1[0][0][0][0]['_XY_left'][0],tmp2_2[0][0][0][0]['_XY_left'][0])
                                ##Y
        tmp2_3 = self.get_param_KJH4('SRF_Mst_Inv1','SRF_PMOS','BND_{}Layer'.format(_Mst_Inv1_PMOS_XVT))
        approaching_coordy = tmp2_3[0][0][0][0]['_XY_down'][1]

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


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Mst: Inv2: Set driver
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D00_00_Inverter_KJH._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOS_NumberofGate']                 = _Mst_Inv2_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth']                 = _Mst_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength']                = _Mst_Inv2_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing']                  = None
        _Caculation_Parameters['_NMOS_SDWidth']                      = None
        _Caculation_Parameters['_NMOS_XVT']                          = _Mst_Inv2_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit']                       = True

        _Caculation_Parameters['_NMOS_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOS_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOS_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOS_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOS_Drain_Comb_Length']            = 0

        _Caculation_Parameters['_NMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOS_PODummy_Length']               = None
        _Caculation_Parameters['_NMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOS_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_POGate_Comb_length']           = _Mst_Inv2_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOS_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOS_NumberofGate']                 = _Mst_Inv2_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth']                 = _Mst_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength']                = _Mst_Inv2_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing']                  = None
        _Caculation_Parameters['_PMOS_SDWidth']                      = None
        _Caculation_Parameters['_PMOS_XVT']                          = _Mst_Inv2_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit']                       = True

        _Caculation_Parameters['_PMOS_Source_Via_TF']                = False
        _Caculation_Parameters['_PMOS_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_PMOS_Source_Comb_TF']               = False
        _Caculation_Parameters['_PMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOS_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_PMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOS_Drain_Comb_Length']            = 0

        _Caculation_Parameters['_PMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOS_PODummy_Length']               = None
        _Caculation_Parameters['_PMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOS_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_POGate_Comb_length']           = _Mst_Inv2_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx']               = [0,1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']           = XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody']          = XvtDown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                   = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Mst_Inv2'] = self._SrefElementDeclaration(_DesignObj=D00_00_Inverter_KJH._Inverter(_DesignParameter=None, _Name='{}:SRF_Mst_Inv2'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Mst_Inv2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Inv2']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Inv2']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
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
        tmp1_2 = self.get_param_KJH4('SRF_Mst_Inv1','SRF_NMOS','BND_PODummyLayer')
        target_coordx = max(tmp1_1[0][0][-1][0]['_XY_right'][0],tmp1_2[0][0][-1][0]['_XY_right'][0])
                                ##y
        tmp1_3 = self.get_param_KJH4('SRF_Mst_Inv1','SRF_PMOS','BND_{}Layer'.format(_Mst_Inv1_PMOS_XVT))
        target_coordy = tmp1_3[0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##X
        tmp2_1 = self.get_param_KJH4('SRF_Mst_Inv2','SRF_PMOS','BND_PODummyLayer')
        tmp2_2 = self.get_param_KJH4('SRF_Mst_Inv2','SRF_NMOS','BND_PODummyLayer')
        approaching_coordx = min(tmp2_1[0][0][0][0]['_XY_left'][0],tmp2_2[0][0][0][0]['_XY_left'][0])
                                ##Y
        tmp2_3 = self.get_param_KJH4('SRF_Mst_Inv2','SRF_PMOS','BND_{}Layer'.format(_Mst_Inv2_PMOS_XVT))
        approaching_coordy = tmp2_3[0][0][0][0]['_XY_down'][1]

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


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Mst: Inv3: Clock driver
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D00_00_Inverter_KJH._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOS_NumberofGate']                 = _Mst_Inv3_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth']                 = _Mst_Inv3_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength']                = _Mst_Inv3_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing']                  = None
        _Caculation_Parameters['_NMOS_SDWidth']                      = None
        _Caculation_Parameters['_NMOS_XVT']                          = _Mst_Inv3_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit']                       = True

        _Caculation_Parameters['_NMOS_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOS_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOS_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOS_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOS_Drain_Comb_Length']            = 0

        _Caculation_Parameters['_NMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOS_PODummy_Length']               = None
        _Caculation_Parameters['_NMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOS_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_POGate_Comb_length']           = _Mst_Inv3_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOS_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOS_NumberofGate']                 = _Mst_Inv3_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth']                 = _Mst_Inv3_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength']                = _Mst_Inv3_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing']                  = None
        _Caculation_Parameters['_PMOS_SDWidth']                      = None
        _Caculation_Parameters['_PMOS_XVT']                          = _Mst_Inv3_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit']                       = True

        _Caculation_Parameters['_PMOS_Source_Via_TF']                = False
        _Caculation_Parameters['_PMOS_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_PMOS_Source_Comb_TF']               = False
        _Caculation_Parameters['_PMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOS_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_PMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOS_Drain_Comb_Length']            = 0

        _Caculation_Parameters['_PMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOS_PODummy_Length']               = None
        _Caculation_Parameters['_PMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOS_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_POGate_Comb_length']           = _Mst_Inv3_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx']               = [0,1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']           = XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody']          = XvtDown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                   = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Mst_Inv3'] = self._SrefElementDeclaration(_DesignObj=D00_00_Inverter_KJH._Inverter(_DesignParameter=None, _Name='{}:SRF_Mst_Inv3'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Mst_Inv3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Inv3']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Inv3']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Mst_Inv3']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Mst_Inv3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        tmp1_1 = self.get_param_KJH4('SRF_Mst_Inv2','SRF_PMOS','BND_PODummyLayer')
        tmp1_2 = self.get_param_KJH4('SRF_Mst_Inv2','SRF_NMOS','BND_PODummyLayer')
        target_coordx = max(tmp1_1[0][0][-1][0]['_XY_right'][0],tmp1_2[0][0][-1][0]['_XY_right'][0])
                                ##y
        tmp1_3 = self.get_param_KJH4('SRF_Mst_Inv2','SRF_PMOS','BND_{}Layer'.format(_Mst_Inv1_PMOS_XVT))
        target_coordy = tmp1_3[0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##X
        tmp2_1 = self.get_param_KJH4('SRF_Mst_Inv3','SRF_PMOS','BND_PODummyLayer')
        tmp2_2 = self.get_param_KJH4('SRF_Mst_Inv3','SRF_NMOS','BND_PODummyLayer')
        approaching_coordx = min(tmp2_1[0][0][0][0]['_XY_left'][0],tmp2_2[0][0][0][0]['_XY_left'][0])
                                ##Y
        tmp2_3 = self.get_param_KJH4('SRF_Mst_Inv3','SRF_PMOS','BND_{}Layer'.format(_Mst_Inv2_PMOS_XVT))
        approaching_coordy = tmp2_3[0][0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Mst_Inv3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] +  _Test_distance
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Mst_Inv3']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## SLV
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  SLV: Xgate1
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D01_00_Xgate_KJH._Xgate._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOS_NumberofGate']                 = _Slv_Xgate1_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth']                 = _Slv_Xgate1_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength']                = _Slv_Xgate1_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing']                  = None
        _Caculation_Parameters['_NMOS_SDWidth']                      = None
        _Caculation_Parameters['_NMOS_XVT']                          = _Slv_Xgate1_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit']                       = True

        _Caculation_Parameters['_NMOS_Source_Via_TF']                = True
        _Caculation_Parameters['_NMOS_Source_Via_Close2POpin_TF']    = True
        _Caculation_Parameters['_NMOS_Source_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOS_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_NMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOS_Drain_Comb_Length']            = None

        _Caculation_Parameters['_NMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOS_PODummy_Length']               = None
        _Caculation_Parameters['_NMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOS_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_POGate_Comb_length']           = _Slv_Xgate1_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOS_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOS_NumberofGate']                 = _Slv_Xgate1_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth']                 = _Slv_Xgate1_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength']                = _Slv_Xgate1_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing']                  = None
        _Caculation_Parameters['_PMOS_SDWidth']                      = None
        _Caculation_Parameters['_PMOS_XVT']                          = _Slv_Xgate1_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit']                       = True

        _Caculation_Parameters['_PMOS_Source_Via_TF']                = True
        _Caculation_Parameters['_PMOS_Source_Via_Close2POpin_TF']    = True
        _Caculation_Parameters['_PMOS_Source_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOS_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_PMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOS_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOS_PODummy_Length']               = None
        _Caculation_Parameters['_PMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOS_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_POGate_Comb_length']           = _Slv_Xgate1_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx']               = [0,1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']           = XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody']          = XvtDown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                   = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Slv_Xgate1'] = self._SrefElementDeclaration(_DesignObj=D01_00_Xgate_KJH._Xgate(_DesignParameter=None, _Name='{}:SRF_Slv_Xgate1'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Slv_Xgate1']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Xgate1']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Xgate1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Xgate1']['_XYCoordinates'] = [[0, 0]]


                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Slv_Xgate1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        tmp1_1 = self.get_param_KJH4('SRF_Mst_Inv3','SRF_PMOS','BND_PODummyLayer')
        tmp1_2 = self.get_param_KJH4('SRF_Mst_Inv3','SRF_NMOS','BND_PODummyLayer')
        target_coordx = max(tmp1_1[0][0][-1][0]['_XY_right'][0],tmp1_2[0][0][-1][0]['_XY_right'][0])
                                ##y
        tmp1_3 = self.get_param_KJH4('SRF_Mst_Inv3','SRF_PMOS','BND_{}Layer'.format(_Mst_Inv3_PMOS_XVT))
        target_coordy = tmp1_3[0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##X
        tmp2_1 = self.get_param_KJH4('SRF_Slv_Xgate1','SRF_PMOS','BND_PODummyLayer')
        tmp2_2 = self.get_param_KJH4('SRF_Slv_Xgate1','SRF_NMOS','BND_PODummyLayer')
        approaching_coordx = min(tmp2_1[0][0][0][0]['_XY_left'][0],tmp2_2[0][0][0][0]['_XY_left'][0])
                                ##Y
        tmp2_3 = self.get_param_KJH4('SRF_Slv_Xgate1','SRF_PMOS','BND_{}Layer'.format(_Slv_Xgate1_PMOS_XVT))
        approaching_coordy = tmp2_3[0][0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Slv_Xgate1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] +  _Test_distance
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Slv_Xgate1']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Slv: Xgate2
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D01_00_Xgate_KJH._Xgate._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOS_NumberofGate']                 = _Slv_Xgate2_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth']                 = _Slv_Xgate2_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength']                = _Slv_Xgate2_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing']                  = None
        _Caculation_Parameters['_NMOS_SDWidth']                      = None
        _Caculation_Parameters['_NMOS_XVT']                          = _Slv_Xgate2_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit']                       = True

        _Caculation_Parameters['_NMOS_Source_Via_TF']                = True
        _Caculation_Parameters['_NMOS_Source_Via_Close2POpin_TF']    = True
        _Caculation_Parameters['_NMOS_Source_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOS_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_NMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOS_Drain_Comb_Length']            = None

        _Caculation_Parameters['_NMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOS_PODummy_Length']               = None
        _Caculation_Parameters['_NMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOS_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_POGate_Comb_length']           = _Slv_Xgate2_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOS_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOS_NumberofGate']                 = _Slv_Xgate2_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth']                 = _Slv_Xgate2_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength']                = _Slv_Xgate2_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing']                  = None
        _Caculation_Parameters['_PMOS_SDWidth']                      = None
        _Caculation_Parameters['_PMOS_XVT']                          = _Slv_Xgate2_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit']                       = True

        _Caculation_Parameters['_PMOS_Source_Via_TF']                = True
        _Caculation_Parameters['_PMOS_Source_Via_Close2POpin_TF']    = True
        _Caculation_Parameters['_PMOS_Source_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOS_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_PMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOS_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOS_PODummy_Length']               = None
        _Caculation_Parameters['_PMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOS_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_POGate_Comb_length']           = _Slv_Xgate2_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx']               = [0,1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']           = XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody']          = XvtDown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                   = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Slv_Xgate2'] = self._SrefElementDeclaration(_DesignObj=D01_00_Xgate_KJH._Xgate(_DesignParameter=None, _Name='{}:SRF_Slv_Xgate2'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Slv_Xgate2']['_Reflect'] = [1, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Xgate2']['_Angle'] = 180

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Xgate2']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Xgate2']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Slv_Xgate2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        tmp1_1 = self.get_param_KJH4('SRF_Slv_Xgate1','SRF_PMOS','BND_PODummyLayer')
        tmp1_2 = self.get_param_KJH4('SRF_Slv_Xgate1','SRF_NMOS','BND_PODummyLayer')
        target_coordx = max(tmp1_1[0][0][-1][0]['_XY_right'][0],tmp1_2[0][0][-1][0]['_XY_right'][0])
                                ##y
        tmp1_3 = self.get_param_KJH4('SRF_Slv_Xgate1','SRF_PMOS','BND_{}Layer'.format(_Slv_Xgate1_PMOS_XVT))
        target_coordy = tmp1_3[0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##X
        tmp2_1 = self.get_param_KJH4('SRF_Slv_Xgate2','SRF_PMOS','BND_PODummyLayer')
        tmp2_2 = self.get_param_KJH4('SRF_Slv_Xgate2','SRF_NMOS','BND_PODummyLayer')
        approaching_coordx = min(tmp2_1[0][0][-1][0]['_XY_right'][0],tmp2_2[0][0][-1][0]['_XY_right'][0])
                                ##Y
        tmp2_3 = self.get_param_KJH4('SRF_Slv_Xgate2','SRF_PMOS','BND_{}Layer'.format(_Slv_Xgate2_PMOS_XVT))
        approaching_coordy = tmp2_3[0][0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Slv_Xgate2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] +  _Test_distance
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Slv_Xgate2']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Slv: Nor1
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D02_02_Nor_KJH0._Nor._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOSA_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOSA_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOSA_NumberofGate']                 = _Slv_Nor1_NMOSA_NumberofGate
        _Caculation_Parameters['_NMOSA_ChannelWidth']                 = _Slv_Nor1_NMOSA_ChannelWidth
        _Caculation_Parameters['_NMOSA_ChannelLength']                = _Slv_Nor1_NMOSA_ChannelLength
        _Caculation_Parameters['_NMOSA_GateSpacing']                  = None
        _Caculation_Parameters['_NMOSA_SDWidth']                      = None
        _Caculation_Parameters['_NMOSA_XVT']                          = _Slv_Nor1_NMOS_XVT
        _Caculation_Parameters['_NMOSA_PCCrit']                       = True

        _Caculation_Parameters['_NMOSA_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOSA_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOSA_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOSA_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOSA_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOSA_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOSA_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOSA_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOSA_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOSA_Drain_Comb_Length']            = None

        _Caculation_Parameters['_NMOSA_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOSA_PODummy_Length']               = None
        _Caculation_Parameters['_NMOSA_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOSA_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOSA_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOSA_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOSA_POGate_Comb_length']           = _Slv_Nor1_NMOSA_POGate_Comb_length
        _Caculation_Parameters['_NMOSA_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOSA_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_NMOSB_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOSB_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOSB_NumberofGate']                 = _Slv_Nor1_NMOSB_NumberofGate
        _Caculation_Parameters['_NMOSB_ChannelWidth']                 = _Slv_Nor1_NMOSB_ChannelWidth
        _Caculation_Parameters['_NMOSB_ChannelLength']                = _Slv_Nor1_NMOSB_ChannelLength
        _Caculation_Parameters['_NMOSB_GateSpacing']                  = None
        _Caculation_Parameters['_NMOSB_SDWidth']                      = None
        _Caculation_Parameters['_NMOSB_XVT']                          = _Slv_Nor1_NMOS_XVT
        _Caculation_Parameters['_NMOSB_PCCrit']                       = True

        _Caculation_Parameters['_NMOSB_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOSB_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOSB_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOSB_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOSB_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOSB_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOSB_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOSB_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOSB_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOSB_Drain_Comb_Length']            = None

        _Caculation_Parameters['_NMOSB_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOSB_PODummy_Length']               = None
        _Caculation_Parameters['_NMOSB_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOSB_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOSB_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOSB_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOSB_POGate_Comb_length']           = _Slv_Nor1_NMOSB_POGate_Comb_length
        _Caculation_Parameters['_NMOSB_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOSB_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOSA_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOSA_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOSA_NumberofGate']                 = _Slv_Nor1_PMOSA_NumberofGate
        _Caculation_Parameters['_PMOSA_ChannelWidth']                 = _Slv_Nor1_PMOSA_ChannelWidth
        _Caculation_Parameters['_PMOSA_ChannelLength']                = _Slv_Nor1_PMOSA_ChannelLength
        _Caculation_Parameters['_PMOSA_GateSpacing']                  = None
        _Caculation_Parameters['_PMOSA_SDWidth']                      = None
        _Caculation_Parameters['_PMOSA_XVT']                          = _Slv_Nor1_PMOS_XVT
        _Caculation_Parameters['_PMOSA_PCCrit']                       = True

        _Caculation_Parameters['_PMOSA_Source_Via_TF']                = False
        _Caculation_Parameters['_PMOSA_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_PMOSA_Source_Comb_TF']               = False
        _Caculation_Parameters['_PMOSA_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOSA_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOSA_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOSA_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_PMOSA_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOSA_Drain_Comb_POpinward_TF']      = False
        _Caculation_Parameters['_PMOSA_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PMOSA_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOSA_PODummy_Length']               = None
        _Caculation_Parameters['_PMOSA_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOSA_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOSA_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOSA_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOSA_POGate_Comb_length']           = _Slv_Nor1_PMOSA_POGate_Comb_length
        _Caculation_Parameters['_PMOSA_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOSA_POGate_ViaMxMx']               = [0,1]



        _Caculation_Parameters['_PMOSB_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOSB_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOSB_NumberofGate']                 = _Slv_Nor1_PMOSB_NumberofGate
        _Caculation_Parameters['_PMOSB_ChannelWidth']                 = _Slv_Nor1_PMOSB_ChannelWidth
        _Caculation_Parameters['_PMOSB_ChannelLength']                = _Slv_Nor1_PMOSB_ChannelLength
        _Caculation_Parameters['_PMOSB_GateSpacing']                  = None
        _Caculation_Parameters['_PMOSB_SDWidth']                      = None
        _Caculation_Parameters['_PMOSB_XVT']                          = _Slv_Nor1_PMOS_XVT
        _Caculation_Parameters['_PMOSB_PCCrit']                       = True

        _Caculation_Parameters['_PMOSB_Source_Via_TF']                = True
        _Caculation_Parameters['_PMOSB_Source_Via_Close2POpin_TF']    = True
        _Caculation_Parameters['_PMOSB_Source_Comb_TF']               = True
        _Caculation_Parameters['_PMOSB_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOSB_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOSB_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOSB_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_PMOSB_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOSB_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOSB_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PMOSB_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOSB_PODummy_Length']               = None
        _Caculation_Parameters['_PMOSB_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOSB_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOSB_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOSB_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOSB_POGate_Comb_length']           = _Slv_Nor1_PMOSB_POGate_Comb_length
        _Caculation_Parameters['_PMOSB_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOSB_POGate_ViaMxMx']               = [0,1]



        _Caculation_Parameters['_NMOSAB_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOSAB_Pbody_XvtTop2Pbody']           = XvtTop2Pbody
        _Caculation_Parameters['_PMOSAB_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOSAB_Nbody_Xvtdown2Nbody']          = XvtDown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                   = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Slv_Nor1'] = self._SrefElementDeclaration(_DesignObj=D02_02_Nor_KJH0._Nor(_DesignParameter=None, _Name='{}:SRF_Slv_Nor1'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Slv_Nor1']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Nor1']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Nor1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Nor1']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Slv_Nor1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        tmp1_1 = self.get_param_KJH4('SRF_Slv_Xgate2','SRF_PMOS','BND_PODummyLayer')
        tmp1_2 = self.get_param_KJH4('SRF_Slv_Xgate2','SRF_NMOS','BND_PODummyLayer')
        target_coordx = max(tmp1_1[0][0][0][0]['_XY_left'][0],tmp1_2[0][0][0][0]['_XY_left'][0])
                                ##y
        tmp1_3 = self.get_param_KJH4('SRF_Slv_Xgate2','SRF_PMOS','BND_{}Layer'.format(_Slv_Xgate2_PMOS_XVT))
        target_coordy = tmp1_3[0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##X
        tmp2_1 = self.get_param_KJH4('SRF_Slv_Nor1','SRF_Pullup','SRF_PMOSA','BND_PODummyLayer')
        tmp2_2 = self.get_param_KJH4('SRF_Slv_Nor1','SRF_Pulldown','SRF_NMOSA','BND_PODummyLayer')
        approaching_coordx = min(tmp2_1[0][0][0][0][0]['_XY_left'][0],tmp2_2[0][0][0][0][0]['_XY_left'][0])
                                ##Y
        tmp2_3 = self.get_param_KJH4('SRF_Slv_Nor1','SRF_Pullup','SRF_PMOSA','BND_{}Layer'.format(_Slv_Nor1_PMOS_XVT))
        approaching_coordy = tmp2_3[0][0][0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Slv_Nor1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] +  _Test_distance
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Slv_Nor1']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Slv: Nor2
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D02_02_Nor_KJH0._Nor._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOSA_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOSA_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOSA_NumberofGate']                 = _Slv_Nor2_NMOSA_NumberofGate
        _Caculation_Parameters['_NMOSA_ChannelWidth']                 = _Slv_Nor2_NMOSA_ChannelWidth
        _Caculation_Parameters['_NMOSA_ChannelLength']                = _Slv_Nor2_NMOSA_ChannelLength
        _Caculation_Parameters['_NMOSA_GateSpacing']                  = None
        _Caculation_Parameters['_NMOSA_SDWidth']                      = None
        _Caculation_Parameters['_NMOSA_XVT']                          = _Slv_Nor2_NMOS_XVT
        _Caculation_Parameters['_NMOSA_PCCrit']                       = True

        _Caculation_Parameters['_NMOSA_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOSA_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOSA_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOSA_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOSA_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOSA_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOSA_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOSA_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOSA_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOSA_Drain_Comb_Length']            = None

        _Caculation_Parameters['_NMOSA_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOSA_PODummy_Length']               = None
        _Caculation_Parameters['_NMOSA_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOSA_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOSA_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOSA_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOSA_POGate_Comb_length']           = _Slv_Nor2_NMOSA_POGate_Comb_length
        _Caculation_Parameters['_NMOSA_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOSA_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_NMOSB_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOSB_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOSB_NumberofGate']                 = _Slv_Nor2_NMOSB_NumberofGate
        _Caculation_Parameters['_NMOSB_ChannelWidth']                 = _Slv_Nor2_NMOSB_ChannelWidth
        _Caculation_Parameters['_NMOSB_ChannelLength']                = _Slv_Nor2_NMOSB_ChannelLength
        _Caculation_Parameters['_NMOSB_GateSpacing']                  = None
        _Caculation_Parameters['_NMOSB_SDWidth']                      = None
        _Caculation_Parameters['_NMOSB_XVT']                          = _Slv_Nor2_NMOS_XVT
        _Caculation_Parameters['_NMOSB_PCCrit']                       = True

        _Caculation_Parameters['_NMOSB_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOSB_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOSB_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOSB_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOSB_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOSB_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOSB_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOSB_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOSB_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOSB_Drain_Comb_Length']            = None

        _Caculation_Parameters['_NMOSB_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOSB_PODummy_Length']               = None
        _Caculation_Parameters['_NMOSB_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOSB_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOSB_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOSB_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOSB_POGate_Comb_length']           = _Slv_Nor2_NMOSB_POGate_Comb_length
        _Caculation_Parameters['_NMOSB_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOSB_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOSA_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOSA_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOSA_NumberofGate']                 = _Slv_Nor2_PMOSA_NumberofGate
        _Caculation_Parameters['_PMOSA_ChannelWidth']                 = _Slv_Nor2_PMOSA_ChannelWidth
        _Caculation_Parameters['_PMOSA_ChannelLength']                = _Slv_Nor2_PMOSA_ChannelLength
        _Caculation_Parameters['_PMOSA_GateSpacing']                  = None
        _Caculation_Parameters['_PMOSA_SDWidth']                      = None
        _Caculation_Parameters['_PMOSA_XVT']                          = _Slv_Nor2_PMOS_XVT
        _Caculation_Parameters['_PMOSA_PCCrit']                       = True

        _Caculation_Parameters['_PMOSA_Source_Via_TF']                = False
        _Caculation_Parameters['_PMOSA_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_PMOSA_Source_Comb_TF']               = False
        _Caculation_Parameters['_PMOSA_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOSA_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOSA_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOSA_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_PMOSA_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOSA_Drain_Comb_POpinward_TF']      = False
        _Caculation_Parameters['_PMOSA_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PMOSA_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOSA_PODummy_Length']               = None
        _Caculation_Parameters['_PMOSA_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOSA_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOSA_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOSA_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOSA_POGate_Comb_length']           = _Slv_Nor2_PMOSA_POGate_Comb_length
        _Caculation_Parameters['_PMOSA_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOSA_POGate_ViaMxMx']               = [0,1]



        _Caculation_Parameters['_PMOSB_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOSB_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOSB_NumberofGate']                 = _Slv_Nor2_PMOSB_NumberofGate
        _Caculation_Parameters['_PMOSB_ChannelWidth']                 = _Slv_Nor2_PMOSB_ChannelWidth
        _Caculation_Parameters['_PMOSB_ChannelLength']                = _Slv_Nor2_PMOSB_ChannelLength
        _Caculation_Parameters['_PMOSB_GateSpacing']                  = None
        _Caculation_Parameters['_PMOSB_SDWidth']                      = None
        _Caculation_Parameters['_PMOSB_XVT']                          = _Slv_Nor2_PMOS_XVT
        _Caculation_Parameters['_PMOSB_PCCrit']                       = True

        _Caculation_Parameters['_PMOSB_Source_Via_TF']                = True
        _Caculation_Parameters['_PMOSB_Source_Via_Close2POpin_TF']    = True
        _Caculation_Parameters['_PMOSB_Source_Comb_TF']               = True
        _Caculation_Parameters['_PMOSB_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOSB_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOSB_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOSB_Drain_Via_Close2POpin_TF']     = False
        _Caculation_Parameters['_PMOSB_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOSB_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOSB_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PMOSB_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOSB_PODummy_Length']               = None
        _Caculation_Parameters['_PMOSB_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOSB_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOSB_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOSB_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOSB_POGate_Comb_length']           = _Slv_Nor2_PMOSB_POGate_Comb_length
        _Caculation_Parameters['_PMOSB_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOSB_POGate_ViaMxMx']               = [0,1]



        _Caculation_Parameters['_NMOSAB_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOSAB_Pbody_XvtTop2Pbody']           = XvtTop2Pbody
        _Caculation_Parameters['_PMOSAB_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOSAB_Nbody_Xvtdown2Nbody']          = XvtDown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                     = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Slv_Nor2'] = self._SrefElementDeclaration(_DesignObj=D02_02_Nor_KJH0._Nor(_DesignParameter=None, _Name='{}:SRF_Slv_Nor2'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Slv_Nor2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Nor2']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Nor2']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Nor2']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Slv_Nor2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        tmp1_1 = self.get_param_KJH4('SRF_Slv_Nor1','SRF_Pullup','SRF_PMOSB','BND_PODummyLayer')
        tmp1_2 = self.get_param_KJH4('SRF_Slv_Nor1','SRF_Pulldown','SRF_NMOSB','BND_PODummyLayer')
        target_coordx = max(tmp1_1[0][0][0][-1][0]['_XY_right'][0],tmp1_2[0][0][0][-1][0]['_XY_right'][0])
                                ##y
        tmp1_3 = self.get_param_KJH4('SRF_Slv_Nor1','SRF_Pullup','SRF_PMOSB','BND_{}Layer'.format(_Slv_Nor1_PMOS_XVT))
        target_coordy = tmp1_3[0][0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##X
        tmp2_1 = self.get_param_KJH4('SRF_Slv_Nor2','SRF_Pullup','SRF_PMOSA','BND_PODummyLayer')
        tmp2_2 = self.get_param_KJH4('SRF_Slv_Nor2','SRF_Pulldown','SRF_NMOSA','BND_PODummyLayer')
        approaching_coordx = min(tmp2_1[0][0][0][0][0]['_XY_left'][0],tmp2_2[0][0][0][0][0]['_XY_left'][0])
                                ##Y
        tmp2_3 = self.get_param_KJH4('SRF_Slv_Nor2','SRF_Pullup','SRF_PMOSA','BND_{}Layer'.format(_Slv_Nor2_PMOS_XVT))
        approaching_coordy = tmp2_3[0][0][0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Slv_Nor2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] +  _Test_distance
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Slv_Nor2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Slv: Inv1: Set pre-driver
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D00_00_Inverter_KJH._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOS_NumberofGate']                 = _Slv_Inv1_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth']                 = _Slv_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength']                = _Slv_Inv1_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing']                  = None
        _Caculation_Parameters['_NMOS_SDWidth']                      = None
        _Caculation_Parameters['_NMOS_XVT']                          = _Slv_Inv1_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit']                       = True

        _Caculation_Parameters['_NMOS_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOS_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOS_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOS_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOS_Drain_Comb_Length']            = 0

        _Caculation_Parameters['_NMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOS_PODummy_Length']               = None
        _Caculation_Parameters['_NMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOS_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_POGate_Comb_length']           = _Slv_Inv1_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOS_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOS_NumberofGate']                 = _Slv_Inv1_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth']                 = _Slv_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength']                = _Slv_Inv1_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing']                  = None
        _Caculation_Parameters['_PMOS_SDWidth']                      = None
        _Caculation_Parameters['_PMOS_XVT']                          = _Slv_Inv1_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit']                       = True

        _Caculation_Parameters['_PMOS_Source_Via_TF']                = False
        _Caculation_Parameters['_PMOS_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_PMOS_Source_Comb_TF']               = False
        _Caculation_Parameters['_PMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOS_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_PMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOS_Drain_Comb_Length']            = 0

        _Caculation_Parameters['_PMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOS_PODummy_Length']               = None
        _Caculation_Parameters['_PMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOS_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_POGate_Comb_length']           = _Slv_Inv1_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx']               = [0,1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']           = XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody']          = XvtDown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                   = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Slv_Inv1'] = self._SrefElementDeclaration(_DesignObj=D00_00_Inverter_KJH._Inverter(_DesignParameter=None, _Name='{}:SRF_Slv_Inv1'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Slv_Inv1']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Inv1']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Inv1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Inv1']['_XYCoordinates'] = [[0, 0]]


                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Slv_Inv1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        tmp1_1 = self.get_param_KJH4('SRF_Slv_Nor2','SRF_Pullup','SRF_PMOSB','BND_PODummyLayer')
        tmp1_2 = self.get_param_KJH4('SRF_Slv_Nor2','SRF_Pulldown','SRF_NMOSB','BND_PODummyLayer')
        target_coordx = max(tmp1_1[0][0][0][-1][0]['_XY_right'][0],tmp1_2[0][0][0][-1][0]['_XY_right'][0])
                                ##y
        tmp1_3 = self.get_param_KJH4('SRF_Slv_Nor2','SRF_Pullup','SRF_PMOSB','BND_{}Layer'.format(_Slv_Nor2_PMOS_XVT))
        target_coordy = tmp1_3[0][0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##X
        tmp2_1 = self.get_param_KJH4('SRF_Slv_Inv1','SRF_PMOS','BND_PODummyLayer')
        tmp2_2 = self.get_param_KJH4('SRF_Slv_Inv1','SRF_NMOS','BND_PODummyLayer')
        approaching_coordx = min(tmp2_1[0][0][0][0]['_XY_left'][0],tmp2_2[0][0][0][0]['_XY_left'][0])
                                ##Y
        tmp2_3 = self.get_param_KJH4('SRF_Slv_Inv1','SRF_PMOS','BND_{}Layer'.format(_Slv_Inv1_PMOS_XVT))
        approaching_coordy = tmp2_3[0][0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Slv_Inv1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] +  _Test_distance
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Slv_Inv1']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Slv: Inv2: ReSet driver
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D00_00_Inverter_KJH._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOS_NumberofGate']                 = _Slv_Inv2_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth']                 = _Slv_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength']                = _Slv_Inv2_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing']                  = None
        _Caculation_Parameters['_NMOS_SDWidth']                      = None
        _Caculation_Parameters['_NMOS_XVT']                          = _Slv_Inv2_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit']                       = True

        _Caculation_Parameters['_NMOS_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOS_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOS_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOS_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOS_Drain_Comb_Length']            = 0

        _Caculation_Parameters['_NMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOS_PODummy_Length']               = None
        _Caculation_Parameters['_NMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOS_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_POGate_Comb_length']           = _Slv_Inv2_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOS_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOS_NumberofGate']                 = _Slv_Inv2_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth']                 = _Slv_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength']                = _Slv_Inv2_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing']                  = None
        _Caculation_Parameters['_PMOS_SDWidth']                      = None
        _Caculation_Parameters['_PMOS_XVT']                          = _Slv_Inv2_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit']                       = True

        _Caculation_Parameters['_PMOS_Source_Via_TF']                = False
        _Caculation_Parameters['_PMOS_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_PMOS_Source_Comb_TF']               = False
        _Caculation_Parameters['_PMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOS_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_PMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOS_Drain_Comb_Length']            = 0

        _Caculation_Parameters['_PMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOS_PODummy_Length']               = None
        _Caculation_Parameters['_PMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOS_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_POGate_Comb_length']           = _Slv_Inv2_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx']               = [0,1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']           = XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody']          = XvtDown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                   = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Slv_Inv2'] = self._SrefElementDeclaration(_DesignObj=D00_00_Inverter_KJH._Inverter(_DesignParameter=None, _Name='{}:SRF_Slv_Inv2'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Slv_Inv2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Inv2']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Inv2']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Inv2']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Slv_Inv2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        tmp1_1 = self.get_param_KJH4('SRF_Slv_Inv1','SRF_PMOS','BND_PODummyLayer')
        tmp1_2 = self.get_param_KJH4('SRF_Slv_Inv1','SRF_NMOS','BND_PODummyLayer')
        target_coordx = max(tmp1_1[0][0][-1][0]['_XY_right'][0],tmp1_2[0][0][-1][0]['_XY_right'][0])
                                ##y
        tmp1_3 = self.get_param_KJH4('SRF_Slv_Inv1','SRF_PMOS','BND_{}Layer'.format(_Slv_Inv1_PMOS_XVT))
        target_coordy = tmp1_3[0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##X
        tmp2_1 = self.get_param_KJH4('SRF_Slv_Inv2','SRF_PMOS','BND_PODummyLayer')
        tmp2_2 = self.get_param_KJH4('SRF_Slv_Inv2','SRF_NMOS','BND_PODummyLayer')
        approaching_coordx = min(tmp2_1[0][0][0][0]['_XY_left'][0],tmp2_2[0][0][0][0]['_XY_left'][0])
                                ##Y
        tmp2_3 = self.get_param_KJH4('SRF_Slv_Inv2','SRF_PMOS','BND_{}Layer'.format(_Slv_Inv2_PMOS_XVT))
        approaching_coordy = tmp2_3[0][0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Slv_Inv2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] +  _Test_distance
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Slv_Inv2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Slv: Inv3: Qb driver
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D00_00_Inverter_KJH._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType']                      = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NMOS_NumberofGate']                 = _Slv_Inv3_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth']                 = _Slv_Inv3_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength']                = _Slv_Inv3_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing']                  = None
        _Caculation_Parameters['_NMOS_SDWidth']                      = None
        _Caculation_Parameters['_NMOS_XVT']                          = _Slv_Inv3_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit']                       = True

        _Caculation_Parameters['_NMOS_Source_Via_TF']                = False
        _Caculation_Parameters['_NMOS_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_NMOS_Source_Comb_TF']               = False
        _Caculation_Parameters['_NMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_NMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_NMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_NMOS_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_NMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_NMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_NMOS_Drain_Comb_Length']            = 0

        _Caculation_Parameters['_NMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_NMOS_PODummy_Length']               = None
        _Caculation_Parameters['_NMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_NMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_NMOS_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_NMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_NMOS_POGate_Comb_length']           = _Slv_Inv3_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx']               = [0,1]


        _Caculation_Parameters['_PMOS_MosType']                      = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_PMOS_NumberofGate']                 = _Slv_Inv3_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth']                 = _Slv_Inv3_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength']                = _Slv_Inv3_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing']                  = None
        _Caculation_Parameters['_PMOS_SDWidth']                      = None
        _Caculation_Parameters['_PMOS_XVT']                          = _Slv_Inv3_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit']                       = True

        _Caculation_Parameters['_PMOS_Source_Via_TF']                = False
        _Caculation_Parameters['_PMOS_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_PMOS_Source_Comb_TF']               = False
        _Caculation_Parameters['_PMOS_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_PMOS_Source_Comb_Length']           = None

        _Caculation_Parameters['_PMOS_Drain_Via_TF']                 = True
        _Caculation_Parameters['_PMOS_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_PMOS_Drain_Comb_TF']                = True
        _Caculation_Parameters['_PMOS_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_PMOS_Drain_Comb_Length']            = 0

        _Caculation_Parameters['_PMOS_PODummy_TF']                   = True
        _Caculation_Parameters['_PMOS_PODummy_Length']               = None
        _Caculation_Parameters['_PMOS_PODummy_Placement']            = None

        _Caculation_Parameters['_PMOS_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_PMOS_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_PMOS_POGate_Comb_TF']               = True
        _Caculation_Parameters['_PMOS_POGate_Comb_length']           = _Slv_Inv3_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF']                = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx']               = [0,1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont']                = _DFF_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']           = XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_NumCont']                = _DFF_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody']          = XvtDown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt']                   = _DFF_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Slv_Inv3'] = self._SrefElementDeclaration(_DesignObj=D00_00_Inverter_KJH._Inverter(_DesignParameter=None, _Name='{}:SRF_Slv_Inv3'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Slv_Inv3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Inv3']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Inv3']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slv_Inv3']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Slv_Inv3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        tmp1_1 = self.get_param_KJH4('SRF_Slv_Inv2','SRF_PMOS','BND_PODummyLayer')
        tmp1_2 = self.get_param_KJH4('SRF_Slv_Inv2','SRF_NMOS','BND_PODummyLayer')
        target_coordx = max(tmp1_1[0][0][-1][0]['_XY_right'][0],tmp1_2[0][0][-1][0]['_XY_right'][0])
                                ##y
        tmp1_3 = self.get_param_KJH4('SRF_Slv_Inv2','SRF_PMOS','BND_{}Layer'.format(_Slv_Inv1_PMOS_XVT))
        target_coordy = tmp1_3[0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##X
        tmp2_1 = self.get_param_KJH4('SRF_Slv_Inv3','SRF_PMOS','BND_PODummyLayer')
        tmp2_2 = self.get_param_KJH4('SRF_Slv_Inv3','SRF_NMOS','BND_PODummyLayer')
        approaching_coordx = min(tmp2_1[0][0][0][0]['_XY_left'][0],tmp2_2[0][0][0][0]['_XY_left'][0])
                                ##Y
        tmp2_3 = self.get_param_KJH4('SRF_Slv_Inv3','SRF_PMOS','BND_{}Layer'.format(_Slv_Inv2_PMOS_XVT))
        approaching_coordy = tmp2_3[0][0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Slv_Inv3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] +  _Test_distance
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Slv_Inv3']['_XYCoordinates'] = tmpXY


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
    libname = 'Proj_ZZ00_RcdacSar_D04_00_SetRstDFF_Nor_Placement'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'D04_00_SetRstDFF_Nor_Placement_v0_96'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

        _Test_distance = 500,

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

    ## Master Inv1 : Set pre-driver
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
    LayoutObj = _SetRstDFF_Nor_Placement(_DesignParameter=None, _Name=cellname)
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
