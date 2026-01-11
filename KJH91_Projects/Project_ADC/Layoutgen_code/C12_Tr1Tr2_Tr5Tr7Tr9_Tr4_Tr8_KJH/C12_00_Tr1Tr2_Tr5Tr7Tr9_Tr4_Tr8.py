
## Import Basic Modules
    ## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

    ## Library
import copy
import time

    ## KJH91 Basic Building Blocks

##
from KJH91_Projects.Project_ADC.Layoutgen_code.C00_Tr1Tr2_VinVout_KJH import C00_03_Guardring
from KJH91_Projects.Project_ADC.Layoutgen_code.C02_Tr5Tr7Tr9_Ctop_KJH import C02_04_Guardring
from KJH91_Projects.Project_ADC.Layoutgen_code.C03_Tr4 import C03_02_Pin
from KJH91_Projects.Project_ADC.Layoutgen_code.C05_Tr8 import C05_02_Pin



## Define Class
class _Tr1Tr2_Tr5Tr7Tr9_Tr4_Tr8(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(

        # Tr1 and Tr2
        # Tr1 and Tr2
            # Tr1
        _Tr1Tr2_Tr1_NMOSNumberofGate    =   12,     #number
        _Tr1Tr2_Tr1_NMOSChannelWidth    =   1000,   #number
        _Tr1Tr2_Tr1_NMOSChannellength   =   30,     #number
        _Tr1Tr2_Tr1_GateSpacing         =   222,   #None/number
        _Tr1Tr2_Tr1_SDWidth             =   None,   #None/number
        _Tr1Tr2_Tr1_XVT                 =   'RVT',  #'XVT' ex)SLVT LVT RVT HVT
        _Tr1Tr2_Tr1_PCCrit              =   True,   #None/True

                # Source_node_ViaM1M2
        _Tr1Tr2_Tr1_Source_Via_TF       =   False,  #True/False

                # Drain_node_ViaM1M2
        _Tr1Tr2_Tr1_Drain_Via_TF        =   False,  #True/False

                # POLY dummy setting
        _Tr1Tr2_Tr1_NMOSDummy           =   True,  # TF
                    # if _PMOSDummy == True
        _Tr1Tr2_Tr1_NMOSDummy_length    =   None,  # None/Value
        _Tr1Tr2_Tr1_NMOSDummy_placement =   None,  # None/'Up'/'Dn'/

            # Tr2
        _Tr1Tr2_Tr2_NMOSNumberofGate=5,  # number
        _Tr1Tr2_Tr2_NMOSChannelWidth=1000,  # number
        _Tr1Tr2_Tr2_NMOSChannellength=30,  # number
        _Tr1Tr2_Tr2_GateSpacing=222,  # None/number
        _Tr1Tr2_Tr2_SDWidth=None,  # None/number
        _Tr1Tr2_Tr2_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Tr1Tr2_Tr2_PCCrit=True,  # None/True

            # Source_node_ViaM1M2
        _Tr1Tr2_Tr2_Source_Via_TF=False,  # True/False

            # Drain_node_ViaM1M2
        _Tr1Tr2_Tr2_Drain_Via_TF=False,  # True/False

            # POLY dummy setting
        _Tr1Tr2_Tr2_NMOSDummy=True,  # TF
                # if _PMOSDummy == True
        _Tr1Tr2_Tr2_NMOSDummy_length=None,  # None/Value
        _Tr1Tr2_Tr2_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

            # Input/Output node
                # INPUT node
        _Tr1Tr2_Inputnode_Metal_layer=6,  # number
        _Tr1Tr2_Inputnode_width=600,  # number

                # OUTPUT node
        _Tr1Tr2_Outputnode_Metal_layer=6,  # number
        _Tr1Tr2_Outputnode_width=600,  # number

            # Guardring
                # Pbody: number of contact
                # Nbody
        _Tr1Tr2_NwellWidth=850,  # number

        # Tr4
        _Tr4_NMOSNumberofGate=4,  # number
        _Tr4_NMOSChannelWidth=500,  # number
        _Tr4_NMOSChannellength=30,  # number
        _Tr4_GateSpacing=80,  # None/number
        _Tr4_SDWidth=None,  # None/number
        _Tr4_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Tr4_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _Tr4_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _Tr4_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _Tr4_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Tr4_NMOSDummy_length=None,  # None/Value
        _Tr4_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr5 Tr7 Tr9
        # PMOS: Tr5
        _Tr5_PMOSNumberofGate=2,
        _Tr5_PMOSChannelWidth=1000,  # ref=1000
        _Tr5_PMOSChannellength=30,
        _Tr5_GateSpacing=None,
        _Tr5_SDWidth=None,
        _Tr5_XVT='SLVT',
        _Tr5_PCCrit=None,

        # Source_node_ViaM1M2
        _Tr5_Source_Via_TF=True,

        # Drain_node_ViaM1M2
        _Tr5_Drain_Via_TF=True,

        # POLY dummy setting
        _Tr5_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Tr5_PMOSDummy_length=None,  # None/Value
        _Tr5_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # PMOS: Tr7
        _Tr7_PMOSNumberofGate=4,
        _Tr7_PMOSChannelWidth=1000,
        _Tr7_PMOSChannellength=30,
        _Tr7_GateSpacing=None,
        _Tr7_SDWidth=None,
        _Tr7_XVT='SLVT',
        _Tr7_PCCrit=None,

        # Source_node_ViaM1M2
        _Tr7_Source_Via_TF=True,

        # Drain_node_ViaM1M2
        _Tr7_Drain_Via_TF=True,

        # POLY dummy setting
        _Tr7_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Tr7_PMOSDummy_length=None,  # None/Value
        _Tr7_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # PMOS: Tr9
        _Tr9_PMOSNumberofGate=8,
        _Tr9_PMOSChannelWidth=1000,  # ref = 1000
        _Tr9_PMOSChannellength=30,
        _Tr9_GateSpacing=None,
        _Tr9_SDWidth=None,
        _Tr9_XVT='RVT',
        _Tr9_PCCrit=None,

        # Source_node_ViaM1M2
        _Tr9_Source_Via_TF=True,

        # Drain_node_ViaM1M2
        _Tr9_Drain_Via_TF=True,

        # POLY dummy setting
        _Tr9_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Tr9_PMOSDummy_length=None,  # None/Value
        _Tr9_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr8
        _Tr8_NMOSNumberofGate=10,  # number (ref:4)
        _Tr8_NMOSChannelWidth=500,  # number (ref:500)
        _Tr8_NMOSChannellength=30,  # number (ref:30)
        _Tr8_GateSpacing=None,  # None/number
        _Tr8_SDWidth=None,  # None/number
        _Tr8_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Tr8_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _Tr8_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _Tr8_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _Tr8_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Tr8_NMOSDummy_length=None,  # None/Value
        _Tr8_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

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

                                  # Tr1 and Tr2
                                  # Tr1
                                  _Tr1Tr2_Tr1_NMOSNumberofGate=12,  # number
                                  _Tr1Tr2_Tr1_NMOSChannelWidth=1000,  # number
                                  _Tr1Tr2_Tr1_NMOSChannellength=30,  # number
                                  _Tr1Tr2_Tr1_GateSpacing=222,  # None/number
                                  _Tr1Tr2_Tr1_SDWidth=None,  # None/number
                                  _Tr1Tr2_Tr1_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Tr1Tr2_Tr1_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _Tr1Tr2_Tr1_Source_Via_TF=False,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Tr1Tr2_Tr1_Drain_Via_TF=False,  # True/False

                                  # POLY dummy setting
                                  _Tr1Tr2_Tr1_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tr1Tr2_Tr1_NMOSDummy_length=None,  # None/Value
                                  _Tr1Tr2_Tr1_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Tr2
                                  _Tr1Tr2_Tr2_NMOSNumberofGate=5,  # number
                                  _Tr1Tr2_Tr2_NMOSChannelWidth=1000,  # number
                                  _Tr1Tr2_Tr2_NMOSChannellength=30,  # number
                                  _Tr1Tr2_Tr2_GateSpacing=222,  # None/number
                                  _Tr1Tr2_Tr2_SDWidth=None,  # None/number
                                  _Tr1Tr2_Tr2_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Tr1Tr2_Tr2_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _Tr1Tr2_Tr2_Source_Via_TF=False,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Tr1Tr2_Tr2_Drain_Via_TF=False,  # True/False

                                  # POLY dummy setting
                                  _Tr1Tr2_Tr2_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tr1Tr2_Tr2_NMOSDummy_length=None,  # None/Value
                                  _Tr1Tr2_Tr2_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Input/Output node
                                  # INPUT node
                                  _Tr1Tr2_Inputnode_Metal_layer=6,  # number
                                  _Tr1Tr2_Inputnode_width=600,  # number

                                  # OUTPUT node
                                  _Tr1Tr2_Outputnode_Metal_layer=6,  # number
                                  _Tr1Tr2_Outputnode_width=600,  # number

                                  # Guardring
                                  # Pbody: number of contact
                                  # Nbody
                                  _Tr1Tr2_NwellWidth=850,  # number

                                  # Tr4
                                  _Tr4_NMOSNumberofGate=4,  # number
                                  _Tr4_NMOSChannelWidth=500,  # number
                                  _Tr4_NMOSChannellength=30,  # number
                                  _Tr4_GateSpacing=80,  # None/number
                                  _Tr4_SDWidth=None,  # None/number
                                  _Tr4_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Tr4_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _Tr4_Source_Via_TF=True,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Tr4_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _Tr4_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tr4_NMOSDummy_length=None,  # None/Value
                                  _Tr4_NMOSDummy_placement=None,  # None/'Up'/'Dn'/


                                  # Tr5 Tr7 Tr9
                                  # PMOS: Tr5
                                  _Tr5_PMOSNumberofGate=2,
                                  _Tr5_PMOSChannelWidth=1000,  # ref=1000
                                  _Tr5_PMOSChannellength=30,
                                  _Tr5_GateSpacing=None,
                                  _Tr5_SDWidth=None,
                                  _Tr5_XVT='SLVT',
                                  _Tr5_PCCrit=None,

                                  # Source_node_ViaM1M2
                                  _Tr5_Source_Via_TF=True,

                                  # Drain_node_ViaM1M2
                                  _Tr5_Drain_Via_TF=True,

                                  # POLY dummy setting
                                  _Tr5_PMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tr5_PMOSDummy_length=None,  # None/Value
                                  _Tr5_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # PMOS: Tr7
                                  _Tr7_PMOSNumberofGate=4,
                                  _Tr7_PMOSChannelWidth=1000,
                                  _Tr7_PMOSChannellength=30,
                                  _Tr7_GateSpacing=None,
                                  _Tr7_SDWidth=None,
                                  _Tr7_XVT='SLVT',
                                  _Tr7_PCCrit=None,

                                  # Source_node_ViaM1M2
                                  _Tr7_Source_Via_TF=True,

                                  # Drain_node_ViaM1M2
                                  _Tr7_Drain_Via_TF=True,

                                  # POLY dummy setting
                                  _Tr7_PMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tr7_PMOSDummy_length=None,  # None/Value
                                  _Tr7_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # PMOS: Tr9
                                  _Tr9_PMOSNumberofGate=8,
                                  _Tr9_PMOSChannelWidth=1000,  # ref = 1000
                                  _Tr9_PMOSChannellength=30,
                                  _Tr9_GateSpacing=None,
                                  _Tr9_SDWidth=None,
                                  _Tr9_XVT='RVT',
                                  _Tr9_PCCrit=None,

                                  # Source_node_ViaM1M2
                                  _Tr9_Source_Via_TF=True,

                                  # Drain_node_ViaM1M2
                                  _Tr9_Drain_Via_TF=True,

                                  # POLY dummy setting
                                  _Tr9_PMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tr9_PMOSDummy_length=None,  # None/Value
                                  _Tr9_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Tr8
                                  _Tr8_NMOSNumberofGate=10,  # number (ref:4)
                                  _Tr8_NMOSChannelWidth=500,  # number (ref:500)
                                  _Tr8_NMOSChannellength=30,  # number (ref:30)
                                  _Tr8_GateSpacing=None,  # None/number
                                  _Tr8_SDWidth=None,  # None/number
                                  _Tr8_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Tr8_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _Tr8_Source_Via_TF=True,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Tr8_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _Tr8_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tr8_NMOSDummy_length=None,  # None/Value
                                  _Tr8_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

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



        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr4
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr4: Sref Gen
            ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C03_02_Pin._Pin._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr4_NMOSNumberofGate']     = _Tr4_NMOSNumberofGate
        _Caculation_Parameters['_Tr4_NMOSChannelWidth']     = _Tr4_NMOSChannelWidth
        _Caculation_Parameters['_Tr4_NMOSChannellength']    = _Tr4_NMOSChannellength
        _Caculation_Parameters['_Tr4_GateSpacing']          = _Tr4_GateSpacing
        _Caculation_Parameters['_Tr4_SDWidth']              = _Tr4_SDWidth
        _Caculation_Parameters['_Tr4_XVT']                  = _Tr4_XVT
        _Caculation_Parameters['_Tr4_PCCrit']               = _Tr4_PCCrit
        _Caculation_Parameters['_Tr4_Source_Via_TF']        = _Tr4_Source_Via_TF
        _Caculation_Parameters['_Tr4_Drain_Via_TF']         = _Tr4_Drain_Via_TF
        _Caculation_Parameters['_Tr4_NMOSDummy']            = _Tr4_NMOSDummy
        _Caculation_Parameters['_Tr4_NMOSDummy_length']     = _Tr4_NMOSDummy_length
        _Caculation_Parameters['_Tr4_NMOSDummy_placement']  = _Tr4_NMOSDummy_placement

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_C03_02_Pin'] = self._SrefElementDeclaration(_DesignObj=C03_02_Pin._Pin(_DesignParameter=None, _Name='{}:SRF_C03_02_Pin'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_C03_02_Pin']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C03_02_Pin']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C03_02_Pin']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C03_02_Pin']['_XYCoordinates'] = [[0, 0]]



        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr5Tr7Tr9
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr5Tr7Tr9: Sref Gen
            ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C02_04_Guardring._Guardring._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr5_PMOSNumberofGate']     = _Tr5_PMOSNumberofGate
        _Caculation_Parameters['_Tr5_PMOSChannelWidth']     = _Tr5_PMOSChannelWidth
        _Caculation_Parameters['_Tr5_PMOSChannellength']    = _Tr5_PMOSChannellength
        _Caculation_Parameters['_Tr5_GateSpacing']          = _Tr5_GateSpacing
        _Caculation_Parameters['_Tr5_SDWidth']              = _Tr5_SDWidth
        _Caculation_Parameters['_Tr5_XVT']                  = _Tr5_XVT
        _Caculation_Parameters['_Tr5_PCCrit']               = _Tr5_PCCrit
        _Caculation_Parameters['_Tr5_Source_Via_TF']        = _Tr5_Source_Via_TF
        _Caculation_Parameters['_Tr5_Drain_Via_TF']         = _Tr5_Drain_Via_TF
        _Caculation_Parameters['_Tr5_PMOSDummy']            = _Tr5_PMOSDummy
        _Caculation_Parameters['_Tr5_PMOSDummy_length']     = _Tr5_PMOSDummy_length
        _Caculation_Parameters['_Tr5_PMOSDummy_placement']  = _Tr5_PMOSDummy_placement

        _Caculation_Parameters['_Tr7_PMOSNumberofGate']     = _Tr7_PMOSNumberofGate
        _Caculation_Parameters['_Tr7_PMOSChannelWidth']     = _Tr7_PMOSChannelWidth
        _Caculation_Parameters['_Tr7_PMOSChannellength']    = _Tr7_PMOSChannellength
        _Caculation_Parameters['_Tr7_GateSpacing']          = _Tr7_GateSpacing
        _Caculation_Parameters['_Tr7_SDWidth']              = _Tr7_SDWidth
        _Caculation_Parameters['_Tr7_XVT']                  = _Tr7_XVT
        _Caculation_Parameters['_Tr7_PCCrit']               = _Tr7_PCCrit
        _Caculation_Parameters['_Tr7_Source_Via_TF']        = _Tr7_Source_Via_TF
        _Caculation_Parameters['_Tr7_Drain_Via_TF']         = _Tr7_Drain_Via_TF
        _Caculation_Parameters['_Tr7_PMOSDummy']            = _Tr7_PMOSDummy
        _Caculation_Parameters['_Tr7_PMOSDummy_length']     = _Tr7_PMOSDummy_length
        _Caculation_Parameters['_Tr7_PMOSDummy_placement']  = _Tr7_PMOSDummy_placement

        _Caculation_Parameters['_Tr9_PMOSNumberofGate']     = _Tr9_PMOSNumberofGate
        _Caculation_Parameters['_Tr9_PMOSChannelWidth']     = _Tr9_PMOSChannelWidth
        _Caculation_Parameters['_Tr9_PMOSChannellength']    = _Tr9_PMOSChannellength
        _Caculation_Parameters['_Tr9_GateSpacing']          = _Tr9_GateSpacing
        _Caculation_Parameters['_Tr9_SDWidth']              = _Tr9_SDWidth
        _Caculation_Parameters['_Tr9_XVT']                  = _Tr9_XVT
        _Caculation_Parameters['_Tr9_PCCrit']               = _Tr9_PCCrit
        _Caculation_Parameters['_Tr9_Source_Via_TF']        = _Tr9_Source_Via_TF
        _Caculation_Parameters['_Tr9_Drain_Via_TF']         = _Tr9_Drain_Via_TF
        _Caculation_Parameters['_Tr9_PMOSDummy']            = _Tr9_PMOSDummy
        _Caculation_Parameters['_Tr9_PMOSDummy_length']     = _Tr9_PMOSDummy_length
        _Caculation_Parameters['_Tr9_PMOSDummy_placement']  = _Tr9_PMOSDummy_placement

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_C02_04_Guardring'] = self._SrefElementDeclaration(_DesignObj=C02_04_Guardring._Guardring(_DesignParameter=None, _Name='{}:SRF_C02_04_Guardring'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_C02_04_Guardring']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C02_04_Guardring']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C02_04_Guardring']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C02_04_Guardring']['_XYCoordinates'] = [[0, 0]]


                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_C02_04_Guardring']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##x
        tmp1_1 = self.get_outter_KJH4('SRF_C03_02_Pin','SRF_Pbodyring2')
        target_coordx = tmp1_1['_Mostright']['coord'][0]
                                ##y
        tmp1_2 = self.get_param_KJH4('SRF_C03_02_Pin','SRF_Guardring','SRF_Tr4','BND_NMOS_Drain_Hrz_M2')
        target_coordy = tmp1_2[0][0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##x
        tmp2_1 = self.get_outter_KJH4('SRF_C02_04_Guardring','SRF_Pbodyring')
        approaching_coordx = tmp2_1['_Mostleft']['coord'][0]
                                ##y
        tmp2_2 = self.get_param_KJH4('SRF_C02_04_Guardring','SRF_Tr5Tr7Tr9','SRF_Tr5','BND_Pmos_Drain_Hrz_M2')
        approaching_coordy = tmp2_2[0][0][0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_C02_04_Guardring')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        tmp4_1 = target_coordx
        tmp4_2 = self.get_param_KJH4('SRF_C03_02_Pin','SRF_Guardring', 'BND_Deepnwell')[0][0][0][0]['_XY_right'][0]
        tmp5_1 = self.get_param_KJH4('SRF_C02_04_Guardring','BND_Deepnwell')[0][0][0]['_XY_left'][0]
        tmp5_2 = approaching_coordx
        C02C03MinSpace = _DRCobj._T3toT3minspace - (tmp4_1 - tmp4_2) - (tmp5_1 - tmp5_2)
        C02C03space = 1200
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] + max(C02C03MinSpace, C02C03space)
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_C02_04_Guardring']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr8
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr8: Sref Gen
            ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C05_02_Pin._Pin._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr8_NMOSNumberofGate']     = _Tr8_NMOSNumberofGate
        _Caculation_Parameters['_Tr8_NMOSChannelWidth']     = _Tr8_NMOSChannelWidth
        _Caculation_Parameters['_Tr8_NMOSChannellength']    = _Tr8_NMOSChannellength
        _Caculation_Parameters['_Tr8_GateSpacing']          = _Tr8_GateSpacing
        _Caculation_Parameters['_Tr8_SDWidth']              = _Tr8_SDWidth
        _Caculation_Parameters['_Tr8_XVT']                  = _Tr8_XVT
        _Caculation_Parameters['_Tr8_PCCrit']               = _Tr8_PCCrit
        _Caculation_Parameters['_Tr8_Source_Via_TF']        = _Tr8_Source_Via_TF
        _Caculation_Parameters['_Tr8_Drain_Via_TF']         = _Tr8_Drain_Via_TF
        _Caculation_Parameters['_Tr8_NMOSDummy']            = _Tr8_NMOSDummy
        _Caculation_Parameters['_Tr8_NMOSDummy_length']     = _Tr8_NMOSDummy_length
        _Caculation_Parameters['_Tr8_NMOSDummy_placement']  = _Tr8_NMOSDummy_placement

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_C05_02_Pin'] = self._SrefElementDeclaration(_DesignObj=C05_02_Pin._Pin(_DesignParameter=None, _Name='{}:SRF_C05_02_Pin'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_C05_02_Pin']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C05_02_Pin']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C05_02_Pin']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C05_02_Pin']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_C05_02_Pin']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##x
        tmp1_1 = self.get_outter_KJH4('SRF_C02_04_Guardring','SRF_Pbodyring')
        target_coordx = tmp1_1['_Mostright']['coord'][0]
                                ##y
        tmp1_2 = self.get_param_KJH4('SRF_C02_04_Guardring','BND_Tr7_Source_Tr9_Gate_Hrz_M2')
        target_coordy = tmp1_2[0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##x
        tmp2_1 = self.get_outter_KJH4('SRF_C05_02_Pin','SRF_Pbodyring2')
        approaching_coordx = tmp2_1['_Mostleft']['coord'][0]
                                ##y
        tmp2_2 = self.get_param_KJH4('SRF_C05_02_Pin','BND_Drain_Hrz_M4')
        approaching_coordy = tmp2_2[0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_C05_02_Pin')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        tmp4_1 = target_coordx
        tmp4_2 = self.get_param_KJH4('SRF_C02_04_Guardring', 'BND_Deepnwell')[0][0][0]['_XY_right'][0]
        tmp5_1 = self.get_param_KJH4('SRF_C05_02_Pin', 'SRF_Guardring', 'BND_Deepnwell')[0][0][0][0]['_XY_left'][0]
        tmp5_2 = approaching_coordx
        C02C05MinSpace = _DRCobj._T3toT3minspace - abs(tmp4_1 - tmp4_2) - abs(tmp5_1 - tmp5_2)
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        C02C05space = 1200
        New_Scoord[0] = New_Scoord[0] + max(C02C05MinSpace, C02C05space)
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_C05_02_Pin']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr1Tr2
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr1Tr2: Sref Gen
            ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C00_03_Guardring._Guardring._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr1_NMOSNumberofGate']     = _Tr1Tr2_Tr1_NMOSNumberofGate
        _Caculation_Parameters['_Tr1_NMOSChannelWidth']     = _Tr1Tr2_Tr1_NMOSChannelWidth
        _Caculation_Parameters['_Tr1_NMOSChannellength']    = _Tr1Tr2_Tr1_NMOSChannellength
        _Caculation_Parameters['_Tr1_GateSpacing']          = _Tr1Tr2_Tr1_GateSpacing
        _Caculation_Parameters['_Tr1_SDWidth']              = _Tr1Tr2_Tr1_SDWidth
        _Caculation_Parameters['_Tr1_XVT']                  = _Tr1Tr2_Tr1_XVT
        _Caculation_Parameters['_Tr1_PCCrit']               = _Tr1Tr2_Tr1_PCCrit
        _Caculation_Parameters['_Tr1_Source_Via_TF']        = _Tr1Tr2_Tr1_Source_Via_TF
        _Caculation_Parameters['_Tr1_Drain_Via_TF']         = _Tr1Tr2_Tr1_Drain_Via_TF
        _Caculation_Parameters['_Tr1_NMOSDummy']            = _Tr1Tr2_Tr1_NMOSDummy
        _Caculation_Parameters['_Tr1_NMOSDummy_length']     = _Tr1Tr2_Tr1_NMOSDummy_length
        _Caculation_Parameters['_Tr1_NMOSDummy_placement']  = _Tr1Tr2_Tr1_NMOSDummy_placement

        _Caculation_Parameters['_Tr2_NMOSNumberofGate']     = _Tr1Tr2_Tr2_NMOSNumberofGate
        _Caculation_Parameters['_Tr2_NMOSChannelWidth']     = _Tr1Tr2_Tr2_NMOSChannelWidth
        _Caculation_Parameters['_Tr2_NMOSChannellength']    = _Tr1Tr2_Tr2_NMOSChannellength
        _Caculation_Parameters['_Tr2_GateSpacing']          = _Tr1Tr2_Tr2_GateSpacing
        _Caculation_Parameters['_Tr2_SDWidth']              = _Tr1Tr2_Tr2_SDWidth
        _Caculation_Parameters['_Tr2_XVT']                  = _Tr1Tr2_Tr2_XVT
        _Caculation_Parameters['_Tr2_PCCrit']               = _Tr1Tr2_Tr2_PCCrit
        _Caculation_Parameters['_Tr2_Source_Via_TF']        = _Tr1Tr2_Tr2_Source_Via_TF
        _Caculation_Parameters['_Tr2_Drain_Via_TF']         = _Tr1Tr2_Tr2_Drain_Via_TF
        _Caculation_Parameters['_Tr2_NMOSDummy']            = _Tr1Tr2_Tr2_NMOSDummy
        _Caculation_Parameters['_Tr2_NMOSDummy_length']     = _Tr1Tr2_Tr2_NMOSDummy_length
        _Caculation_Parameters['_Tr2_NMOSDummy_placement']  = _Tr1Tr2_Tr2_NMOSDummy_placement

        _Caculation_Parameters['_Inputnode_Metal_layer']    = _Tr1Tr2_Inputnode_Metal_layer
        _Caculation_Parameters['_Inputnode_width']          = _Tr1Tr2_Inputnode_width
        _Caculation_Parameters['_Outputnode_Metal_layer']   = _Tr1Tr2_Outputnode_Metal_layer
        _Caculation_Parameters['_Outputnode_width']         = _Tr1Tr2_Outputnode_width

        _Caculation_Parameters['_NwellWidth']               = _Tr1Tr2_NwellWidth

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_C00_03_Guardring'] = self._SrefElementDeclaration(_DesignObj=C00_03_Guardring._Guardring(_DesignParameter=None, _Name='{}:SRF_C00_03_Guardring'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_C00_03_Guardring']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C00_03_Guardring']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C00_03_Guardring']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_C00_03_Guardring']['_XYCoordinates'] = [[0, 0]]


                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_C00_03_Guardring']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##x
        tmp1_1 = self.get_param_KJH4('SRF_C02_04_Guardring','SRF_Tr5Tr7Tr9','SRF_Tr5','BND_Pmos_Drain_Hrz_M2')
        target_coordx = tmp1_1[0][0][0][0][0]['_XY_right'][0]
                                ##y
        tmp1_2 = self.get_outter_KJH4('SRF_C05_02_Pin','SRF_Pbodyring2')
        tmp1_3 = self.get_outter_KJH4('SRF_C02_04_Guardring', 'SRF_Pbodyring')
        tmp1_4 = self.get_outter_KJH4('SRF_C03_02_Pin', 'SRF_Pbodyring2')
        tmp1_5 = min(tmp1_2['_Mostdown']['coord'][0],tmp1_3['_Mostdown']['coord'][0],tmp1_4['_Mostdown']['coord'][0])
        target_coordy = tmp1_5

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##x
        tmp2_1 = self.get_param_KJH4('SRF_C00_03_Guardring','SRF_Tr1Tr2','SRF_Tr2','BND_Gate_Hrz_M3')
        approaching_coordx = tmp2_1[0][0][0][0][0]['_XY_right'][0]
                                ##y
        tmp2_2 = self.get_outter_KJH4('SRF_C00_03_Guardring','SRF_Pbodyring2')
        approaching_coordy = tmp2_2['_Mostup']['coord'][0]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_C00_03_Guardring')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        C00C03space = 150
        New_Scoord[1] = New_Scoord[1] - max(_DRCobj._PpMinSpace, C00C03space)
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_C00_03_Guardring']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## VN node
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Vn node: M2 Vtc
            ## pre-defined
        Vn_vtc_metal_width = 300

            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Vn_Vtc_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_C00_03_Guardring','SRF_Tr1Tr2','SRF_Tr2','SRF_Gate_ViaM0M3','SRF_ViaM1M2','BND_Met2Layer')
        tmp2 =self.get_param_KJH4('SRF_C02_04_Guardring','SRF_Tr5Tr7Tr9','SRF_Tr5','BND_Pmos_Drain_Hrz_M2')

        self._DesignParameter['BND_Vn_Vtc_M2']['_YWidth'] = abs( tmp2[0][0][0][0][0]['_XY_down'][1] - tmp1[0][0][0][0][0][0][0]['_XY_down'][1] )

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Vn_Vtc_M2']['_XWidth'] = Vn_vtc_metal_width

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Vn_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Vn_Vtc_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_C00_03_Guardring','SRF_Tr1Tr2','SRF_Tr2','SRF_Gate_ViaM0M3','SRF_ViaM1M2','BND_Met2Layer')
        target_coord = tmp1[0][0][0][0][0][0][0]['_XY_down_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Vn_Vtc_M2')
        approaching_coord = tmp2[0][0]['_XY_down_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Vn_Vtc_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Vn_Vtc_M2']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Vn node: M2 Hrz
            ## pre-defined
        Vn_vtc_metal_width = 300

            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Vn_Hrz_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Vn_Hrz_M2']['_YWidth'] = Vn_vtc_metal_width

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_C03_02_Pin','SRF_Guardring','SRF_Tr4','BND_NMOS_Drain_Hrz_M2')
        tmp2 =self.get_param_KJH4('SRF_C02_04_Guardring','SRF_Tr5Tr7Tr9','SRF_Tr5','BND_Pmos_Drain_Hrz_M2')

        self._DesignParameter['BND_Vn_Hrz_M2']['_XWidth'] = abs( tmp2[0][0][0][0][0]['_XY_right'][0] - tmp1[0][0][0][0][0]['_XY_left'][0] )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Vn_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Vn_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_C02_04_Guardring','SRF_Tr5Tr7Tr9','SRF_Tr5','BND_Pmos_Drain_Hrz_M2')
        target_coord = tmp1[0][0][0][0][0]['_XY_down_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Vn_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Vn_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Vn_Hrz_M2']['_XYCoordinates'] = tmpXY
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## VG node
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## VG node: M2 Hrz
            ## pre-defined
        Vg_hrz_metal_width = 300

            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Vg_Hrz_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Vg_Hrz_M2']['_YWidth'] = Vg_hrz_metal_width

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_C05_02_Pin','SRF_Guardring','SRF_Tr8','BND_NMOS_Drain_Hrz_M2')
        tmp2 =self.get_param_KJH4('SRF_C02_04_Guardring','SRF_Tr5Tr7Tr9','SRF_Tr7','BND_Pmos_Source_Hrz_M2')

        self._DesignParameter['BND_Vg_Hrz_M2']['_XWidth'] = abs( tmp1[0][0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0][0]['_XY_left'][0] )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Vg_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Vg_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_C05_02_Pin','SRF_Guardring','SRF_Tr8','BND_NMOS_Drain_Hrz_M2')
        target_coord = tmp1[0][0][0][0][0]['_XY_down_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Vg_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Vg_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Vg_Hrz_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## VG node: M2 Vtc
            ## pre-defined
        Vg_vtc_metal_width = 300

            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Vg_Vtc_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Check Routability
        tmp1 = self.get_param_KJH4('BND_Vg_Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_C00_03_Guardring','SRF_Tr1Tr2','SRF_Tr1','SRF_Gate_ViaM0M3','SRF_ViaM1M2','BND_Met2Layer')
        if tmp1[0][0]['_XY_right'][0] < tmp2[0][0][0][0][0][0][0]['_XY_right'][0]:
            raise Exception(f"BND_Vg_Vtc_M2 is not routable")

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_Vg_Hrz_M2')
        tmp2 =self.get_param_KJH4('SRF_C00_03_Guardring','SRF_Tr1Tr2','SRF_Tr1','SRF_Gate_ViaM0M3','SRF_ViaM1M2','BND_Met2Layer')

        self._DesignParameter['BND_Vg_Vtc_M2']['_YWidth'] = abs( tmp1[0][0]['_XY_up'][1] - tmp2[0][0][0][0][0][0][0]['_XY_down'][1] )

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Vg_Vtc_M2']['_XWidth'] =Vg_vtc_metal_width

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Vg_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Vg_Vtc_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_C00_03_Guardring','SRF_Tr1Tr2','SRF_Tr1','SRF_Gate_ViaM0M3','SRF_ViaM1M2','BND_Met2Layer')
        target_coord = tmp1[0][0][0][0][0][0][0]['_XY_down_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Vg_Vtc_M2')
        approaching_coord = tmp2[0][0]['_XY_down_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Vg_Vtc_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Vg_Vtc_M2']['_XYCoordinates'] = tmpXY

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
    libname = 'Proj_ADC_C12'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'C12_00_Tr1Tr2_Tr5Tr7Tr9_Tr4_Tr8_v0_82'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(


        # Tr1 and Tr2
            # Tr1
        _Tr1Tr2_Tr1_NMOSNumberofGate    =   12,     #number
        _Tr1Tr2_Tr1_NMOSChannelWidth    =   1000,   #number
        _Tr1Tr2_Tr1_NMOSChannellength   =   30,     #number
        _Tr1Tr2_Tr1_GateSpacing         =   222,   #None/number
        _Tr1Tr2_Tr1_SDWidth             =   None,   #None/number
        _Tr1Tr2_Tr1_XVT                 =   'RVT',  #'XVT' ex)SLVT LVT RVT HVT
        _Tr1Tr2_Tr1_PCCrit              =   True,   #None/True

                # Source_node_ViaM1M2
        _Tr1Tr2_Tr1_Source_Via_TF       =   False,  #True/False

                # Drain_node_ViaM1M2
        _Tr1Tr2_Tr1_Drain_Via_TF        =   False,  #True/False

                # POLY dummy setting
        _Tr1Tr2_Tr1_NMOSDummy           =   True,  # TF
                    # if _PMOSDummy == True
        _Tr1Tr2_Tr1_NMOSDummy_length    =   None,  # None/Value
        _Tr1Tr2_Tr1_NMOSDummy_placement =   None,  # None/'Up'/'Dn'/

            # Tr2
        _Tr1Tr2_Tr2_NMOSNumberofGate=5,  # number
        _Tr1Tr2_Tr2_NMOSChannelWidth=1000,  # number
        _Tr1Tr2_Tr2_NMOSChannellength=30,  # number
        _Tr1Tr2_Tr2_GateSpacing=100,  # None/number
        _Tr1Tr2_Tr2_SDWidth=None,  # None/number
        _Tr1Tr2_Tr2_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Tr1Tr2_Tr2_PCCrit=True,  # None/True

            # Source_node_ViaM1M2
        _Tr1Tr2_Tr2_Source_Via_TF=False,  # True/False

            # Drain_node_ViaM1M2
        _Tr1Tr2_Tr2_Drain_Via_TF=False,  # True/False

            # POLY dummy setting
        _Tr1Tr2_Tr2_NMOSDummy=True,  # TF
                # if _PMOSDummy == True
        _Tr1Tr2_Tr2_NMOSDummy_length=None,  # None/Value
        _Tr1Tr2_Tr2_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

            # Input/Output node
                # INPUT node
        _Tr1Tr2_Inputnode_Metal_layer=6,  # number
        _Tr1Tr2_Inputnode_width=600,  # number

                # OUTPUT node
        _Tr1Tr2_Outputnode_Metal_layer=6,  # number
        _Tr1Tr2_Outputnode_width=600,  # number

            # Guardring
                # Pbody: number of contact
                # Nbody
        _Tr1Tr2_NwellWidth=850,  # number

        # Tr4
        _Tr4_NMOSNumberofGate    =   10,     #number (ref:4)
        _Tr4_NMOSChannelWidth    =   500,   #number (ref:500)
        _Tr4_NMOSChannellength   =   30,     #number (ref:30)
        _Tr4_GateSpacing         =   None,   #None/number
        _Tr4_SDWidth             =   None,   #None/number
        _Tr4_XVT                 =   'RVT',  #'XVT' ex)SLVT LVT RVT HVT
        _Tr4_PCCrit              =   True,   #None/True

            # Source_node_ViaM1M2
        _Tr4_Source_Via_TF       =   True,  #True/False

            # Drain_node_ViaM1M2
        _Tr4_Drain_Via_TF        =   True,  #True/False

            # POLY dummy setting
        _Tr4_NMOSDummy           =   True,  # TF
                # if _PMOSDummy == True
        _Tr4_NMOSDummy_length    =   None,  # None/Value
        _Tr4_NMOSDummy_placement =   None,  # None/'Up'/'Dn'/

        # Tr5 Tr7 Tr9
            # PMOS: Tr5
        _Tr5_PMOSNumberofGate=2,
        _Tr5_PMOSChannelWidth=1000,  # ref=1000
        _Tr5_PMOSChannellength=30,
        _Tr5_GateSpacing=None,
        _Tr5_SDWidth=None,
        _Tr5_XVT='SLVT',
        _Tr5_PCCrit=None,

                # Source_node_ViaM1M2
        _Tr5_Source_Via_TF=True,

                # Drain_node_ViaM1M2
        _Tr5_Drain_Via_TF=True,

                # POLY dummy setting
        _Tr5_PMOSDummy=True,  # TF
                    # if _PMOSDummy == True
        _Tr5_PMOSDummy_length=None,  # None/Value
        _Tr5_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

            # PMOS: Tr7
        _Tr7_PMOSNumberofGate=4,
        _Tr7_PMOSChannelWidth=1200, #Ref = 1000
        _Tr7_PMOSChannellength=30,
        _Tr7_GateSpacing=None,
        _Tr7_SDWidth=None,
        _Tr7_XVT='SLVT',
        _Tr7_PCCrit=None,

                # Source_node_ViaM1M2
        _Tr7_Source_Via_TF=True,

                # Drain_node_ViaM1M2
        _Tr7_Drain_Via_TF=True,

                # POLY dummy setting
        _Tr7_PMOSDummy=True,  # TF
                    # if _PMOSDummy == True
        _Tr7_PMOSDummy_length=None,  # None/Value
        _Tr7_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

            # PMOS: Tr9
        _Tr9_PMOSNumberofGate=8,
        _Tr9_PMOSChannelWidth=1000,  # ref = 1000
        _Tr9_PMOSChannellength=30,
        _Tr9_GateSpacing=None,
        _Tr9_SDWidth=None,
        _Tr9_XVT='RVT',
        _Tr9_PCCrit=None,

                # Source_node_ViaM1M2
        _Tr9_Source_Via_TF=True,

                # Drain_node_ViaM1M2
        _Tr9_Drain_Via_TF=True,

                # POLY dummy setting
        _Tr9_PMOSDummy=True,  # TF
                # if _PMOSDummy == True
        _Tr9_PMOSDummy_length=None,  # None/Value
        _Tr9_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr8
        _Tr8_NMOSNumberofGate=10,  # number (ref:4)
        _Tr8_NMOSChannelWidth=500,  # number (ref:500)
        _Tr8_NMOSChannellength=30,  # number (ref:30)
        _Tr8_GateSpacing=None,  # None/number
        _Tr8_SDWidth=None,  # None/number
        _Tr8_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Tr8_PCCrit=True,  # None/True

            # Source_node_ViaM1M2
        _Tr8_Source_Via_TF=True,  # True/False

            # Drain_node_ViaM1M2
        _Tr8_Drain_Via_TF=True,  # True/False

            # POLY dummy setting
        _Tr8_NMOSDummy=True,  # TF
                # if _PMOSDummy == True
        _Tr8_NMOSDummy_length=None,  # None/Value
        _Tr8_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

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
    LayoutObj = _Tr1Tr2_Tr5Tr7Tr9_Tr4_Tr8(_DesignParameter=None, _Name=cellname)
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
    Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()

    ''' Check Time'''
    elapsed_time = time.time() - start_time
    m, s = divmod(elapsed_time, 60)
    h, m = divmod(m, 60)

    print('#############################      Finished      ################################')
# end of 'main():' ---------------------------------------------------------------------------------------------
