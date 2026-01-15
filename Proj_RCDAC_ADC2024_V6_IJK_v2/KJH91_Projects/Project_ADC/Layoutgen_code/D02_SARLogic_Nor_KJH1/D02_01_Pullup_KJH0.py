
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
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A14_Mosfet_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A08_PbodyContactPhyLen_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A07_NbodyContactPhyLen_KJH3


## Define Class
class _Pullup(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(


    # PMosfetA
        # PMOS/NMOS
        _PMOSA_MosType                   = 'NMOS',   # 'NMOS'/'PMOS'
        # MOS Up/Dn
        _PMOSA_MosUpDn                   = 'Up',     # 'Up'/'Dn'
        # Physical dimension
        _PMOSA_NumberofGate	            = 1,        # Number
        _PMOSA_ChannelWidth	            = 200,      # Number
        _PMOSA_ChannelLength	        = 30,       # Number
        _PMOSA_GateSpacing		        = None,     # None/Number
        _PMOSA_SDWidth			        = None,     # None/Number
        _PMOSA_XVT				        = 'SLVT',   # 'XVT' ex)SLVT/LVT/RVT/HVT
        _PMOSA_PCCrit				    = True,     # None/True
        # Source_node setting
            # Via setting
        _PMOSA_Source_Via_TF              = False,     # True/False
                # Via close to POpin
        _PMOSA_Source_Via_Close2POpin_TF  = False,     # True/False
            # Comb setting: If Via is True
        _PMOSA_Source_Comb_TF             = False,     # True/False
                # Comb POPinward
        _PMOSA_Source_Comb_POpinward_TF   = False,     # True/False
                # Comb vertical_length
        _PMOSA_Source_Comb_Length         = None,     # None/Number

        # Drain_node_setting
            # Via setting
        _PMOSA_Drain_Via_TF               = True,     # True/False
                # Via close to POpin
        _PMOSA_Drain_Via_Close2POpin_TF   = True,     # True/False
            # Comb setting: If Via is True
        _PMOSA_Drain_Comb_TF              = True,     # True/False
                # Comb POPinward
        _PMOSA_Drain_Comb_POpinward_TF    = True,     # True/False
                # Comb vertical_length
        _PMOSA_Drain_Comb_Length          = None,     # None/Number

        # POLY dummy setting
        _PMOSA_PODummy_TF                 = True,  # TF
            # if _PMOSADummy == True
        _PMOSA_PODummy_Length             = None,  # None/Value
        _PMOSA_PODummy_Placement          = None,  # None/'Up'/'Dn'/

        # XVT setting
            # XVT setting : Exten XVT area if area is min
        _PMOSA_Xvt_MinExten_TF            = True,     # True/False
            # XVT setting : None(Cent), Up, Dn
        _PMOSA_Xvt_Placement              = 'Up',     # None/'Up'/'Dn'/

        # Poly Gate setting
        _PMOSA_POGate_Comb_TF             = True,     # True/False
            # Poly Gate setting : vertical length
        _PMOSA_POGate_Comb_length         = 100,     # None/Number
            # Poly Gate Via setting
        _PMOSA_POGate_Via_TF              = True,     # True/False
            # Poly Gate Via setting :
        _PMOSA_POGate_ViaMxMx             = [0 ,1],     # Ex) [1,5] -> ViaM1M5


    # PMosfetB
        # PMOS/NMOS
        _PMOSB_MosType                   = 'NMOS',   # 'NMOS'/'PMOS'
        # MOS Up/Dn
        _PMOSB_MosUpDn                   = 'Up',     # 'Up'/'Dn'
        # Physical dimension
        _PMOSB_NumberofGate	            = 1,        # Number
        _PMOSB_ChannelWidth	            = 852,      # Number
        _PMOSB_ChannelLength	        = 30,       # Number
        _PMOSB_GateSpacing		        = None,     # None/Number
        _PMOSB_SDWidth			        = None,     # None/Number
        _PMOSB_XVT				        = 'SLVT',   # 'XVT' ex)SLVT/LVT/RVT/HVT
        _PMOSB_PCCrit				    = True,     # None/True
        # Source_node setting
            # Via setting
        _PMOSB_Source_Via_TF              = False,     # True/False
                # Via close to POpin
        _PMOSB_Source_Via_Close2POpin_TF  = False,     # True/False
            # Comb setting: If Via is True
        _PMOSB_Source_Comb_TF             = False,     # True/False
                # Comb POPinward
        _PMOSB_Source_Comb_POpinward_TF   = False,     # True/False
                # Comb vertical_length
        _PMOSB_Source_Comb_Length         = None,     # None/Number

        # Drain_node_setting
            # Via setting
        _PMOSB_Drain_Via_TF               = True,     # True/False
                # Via close to POpin
        _PMOSB_Drain_Via_Close2POpin_TF   = True,     # True/False
            # Comb setting: If Via is True
        _PMOSB_Drain_Comb_TF              = True,     # True/False
                # Comb POPinward
        _PMOSB_Drain_Comb_POpinward_TF    = True,     # True/False
                # Comb vertical_length
        _PMOSB_Drain_Comb_Length          = None,     # None/Number

        # POLY dummy setting
        _PMOSB_PODummy_TF                 = True,  # TF
            # if _PMOSBDummy == True
        _PMOSB_PODummy_Length             = None,  # None/Value
        _PMOSB_PODummy_Placement          = None,  # None/'Up'/'Dn'/

        # XVT setting
            # XVT setting : Exten XVT area if area is min
        _PMOSB_Xvt_MinExten_TF            = True,     # True/False
            # XVT setting : None(Cent), Up, Dn
        _PMOSB_Xvt_Placement              = 'Up',     # None/'Up'/'Dn'/

        # Poly Gate setting
        _PMOSB_POGate_Comb_TF             = True,     # True/False
            # Poly Gate setting : vertical length
        _PMOSB_POGate_Comb_length         = 100,     # None/Number
            # Poly Gate Via setting
        _PMOSB_POGate_Via_TF              = True,     # None/'Up'/'Dn'/
            # Poly Gate Via setting :
        _PMOSB_POGate_ViaMxMx             = [0 ,1],     # Ex) [1,5] -> ViaM1M5


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


    # PMosfetA
        # PMOS/NMOS
        _PMOSA_MosType                   = 'NMOS',   # 'NMOS'/'PMOS'
        # MOS Up/Dn
        _PMOSA_MosUpDn                   = 'Up',     # 'Up'/'Dn'
        # Physical dimension
        _PMOSA_NumberofGate	            = 1,        # Number
        _PMOSA_ChannelWidth	            = 200,      # Number
        _PMOSA_ChannelLength	        = 30,       # Number
        _PMOSA_GateSpacing		        = None,     # None/Number
        _PMOSA_SDWidth			        = None,     # None/Number
        _PMOSA_XVT				        = 'SLVT',   # 'XVT' ex)SLVT/LVT/RVT/HVT
        _PMOSA_PCCrit				    = True,     # None/True
        # Source_node setting
            # Via setting
        _PMOSA_Source_Via_TF              = False,     # True/False
                # Via close to POpin
        _PMOSA_Source_Via_Close2POpin_TF  = False,     # True/False
            # Comb setting: If Via is True
        _PMOSA_Source_Comb_TF             = False,     # True/False
                # Comb POPinward
        _PMOSA_Source_Comb_POpinward_TF   = False,     # True/False
                # Comb vertical_length
        _PMOSA_Source_Comb_Length         = None,     # None/Number

        # Drain_node_setting
            # Via setting
        _PMOSA_Drain_Via_TF               = True,     # True/False
                # Via close to POpin
        _PMOSA_Drain_Via_Close2POpin_TF   = True,     # True/False
            # Comb setting: If Via is True
        _PMOSA_Drain_Comb_TF              = True,     # True/False
                # Comb POPinward
        _PMOSA_Drain_Comb_POpinward_TF    = True,     # True/False
                # Comb vertical_length
        _PMOSA_Drain_Comb_Length          = None,     # None/Number

        # POLY dummy setting
        _PMOSA_PODummy_TF                 = True,  # TF
            # if _PMOSADummy == True
        _PMOSA_PODummy_Length             = None,  # None/Value
        _PMOSA_PODummy_Placement          = None,  # None/'Up'/'Dn'/

        # XVT setting
            # XVT setting : Exten XVT area if area is min
        _PMOSA_Xvt_MinExten_TF            = True,     # True/False
            # XVT setting : None(Cent), Up, Dn
        _PMOSA_Xvt_Placement              = 'Up',     # None/'Up'/'Dn'/

        # Poly Gate setting
        _PMOSA_POGate_Comb_TF             = True,     # True/False
            # Poly Gate setting : vertical length
        _PMOSA_POGate_Comb_length         = 100,     # None/Number
            # Poly Gate Via setting
        _PMOSA_POGate_Via_TF              = True,     # True/False
            # Poly Gate Via setting :
        _PMOSA_POGate_ViaMxMx             = [0 ,1],     # Ex) [1,5] -> ViaM1M5


    # PMosfetB
        # PMOS/NMOS
        _PMOSB_MosType                   = 'NMOS',   # 'NMOS'/'PMOS'
        # MOS Up/Dn
        _PMOSB_MosUpDn                   = 'Up',     # 'Up'/'Dn'
        # Physical dimension
        _PMOSB_NumberofGate	            = 1,        # Number
        _PMOSB_ChannelWidth	            = 852,      # Number
        _PMOSB_ChannelLength	        = 30,       # Number
        _PMOSB_GateSpacing		        = None,     # None/Number
        _PMOSB_SDWidth			        = None,     # None/Number
        _PMOSB_XVT				        = 'SLVT',   # 'XVT' ex)SLVT/LVT/RVT/HVT
        _PMOSB_PCCrit				    = True,     # None/True
        # Source_node setting
            # Via setting
        _PMOSB_Source_Via_TF              = False,     # True/False
                # Via close to POpin
        _PMOSB_Source_Via_Close2POpin_TF  = False,     # True/False
            # Comb setting: If Via is True
        _PMOSB_Source_Comb_TF             = False,     # True/False
                # Comb POPinward
        _PMOSB_Source_Comb_POpinward_TF   = False,     # True/False
                # Comb vertical_length
        _PMOSB_Source_Comb_Length         = None,     # None/Number

        # Drain_node_setting
            # Via setting
        _PMOSB_Drain_Via_TF               = True,     # True/False
                # Via close to POpin
        _PMOSB_Drain_Via_Close2POpin_TF   = True,     # True/False
            # Comb setting: If Via is True
        _PMOSB_Drain_Comb_TF              = True,     # True/False
                # Comb POPinward
        _PMOSB_Drain_Comb_POpinward_TF    = True,     # True/False
                # Comb vertical_length
        _PMOSB_Drain_Comb_Length          = None,     # None/Number

        # POLY dummy setting
        _PMOSB_PODummy_TF                 = True,  # TF
            # if _PMOSBDummy == True
        _PMOSB_PODummy_Length             = None,  # None/Value
        _PMOSB_PODummy_Placement          = None,  # None/'Up'/'Dn'/

        # XVT setting
            # XVT setting : Exten XVT area if area is min
        _PMOSB_Xvt_MinExten_TF            = True,     # True/False
            # XVT setting : None(Cent), Up, Dn
        _PMOSB_Xvt_Placement              = 'Up',     # None/'Up'/'Dn'/

        # Poly Gate setting
        _PMOSB_POGate_Comb_TF             = True,     # True/False
            # Poly Gate setting : vertical length
        _PMOSB_POGate_Comb_length         = 100,     # None/Number
            # Poly Gate Via setting
        _PMOSB_POGate_Via_TF              = True,     # None/'Up'/'Dn'/
            # Poly Gate Via setting :
        _PMOSB_POGate_ViaMxMx             = [0 ,1],     # Ex) [1,5] -> ViaM1M5


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



        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOSA
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  PMOSA: Sref Fake Gen. for Cal
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A14_Mosfet_KJH2._Mosfet._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_MosType']                      = _PMOSA_MosType
        _Caculation_Parameters['_MosUpDn']                      = _PMOSA_MosUpDn

        _Caculation_Parameters['_NumberofGate']                 = _PMOSA_NumberofGate
        _Caculation_Parameters['_ChannelWidth']                 = _PMOSA_ChannelWidth
        _Caculation_Parameters['_ChannelLength']                = _PMOSA_ChannelLength
        _Caculation_Parameters['_GateSpacing']                  = _PMOSA_GateSpacing
        _Caculation_Parameters['_SDWidth']                      = _PMOSA_SDWidth
        _Caculation_Parameters['_XVT']                          = _PMOSA_XVT
        _Caculation_Parameters['_PCCrit']                       = _PMOSA_PCCrit

        _Caculation_Parameters['_Source_Via_TF']                = _PMOSA_Source_Via_TF
        _Caculation_Parameters['_Source_Via_Close2POpin_TF']    = _PMOSA_Source_Via_Close2POpin_TF
        _Caculation_Parameters['_Source_Comb_TF']               = _PMOSA_Source_Comb_TF
        _Caculation_Parameters['_Source_Comb_POpinward_TF']     = _PMOSA_Source_Comb_POpinward_TF
        _Caculation_Parameters['_Source_Comb_Length']           = _PMOSA_Source_Comb_Length

        _Caculation_Parameters['_Drain_Via_TF']                 = _PMOSA_Drain_Via_TF
        _Caculation_Parameters['_Drain_Via_Close2POpin_TF']     = _PMOSA_Drain_Via_Close2POpin_TF
        _Caculation_Parameters['_Drain_Comb_TF']                = _PMOSA_Drain_Comb_TF
        _Caculation_Parameters['_Drain_Comb_POpinward_TF']      = _PMOSA_Drain_Comb_POpinward_TF
        _Caculation_Parameters['_Drain_Comb_Length']            = _PMOSA_Drain_Comb_Length

        _Caculation_Parameters['_PODummy_TF']                   = _PMOSA_PODummy_TF
        _Caculation_Parameters['_PODummy_Length']               = _PMOSA_PODummy_Length
        _Caculation_Parameters['_PODummy_Placement']            = _PMOSA_PODummy_Placement

        _Caculation_Parameters['_Xvt_MinExten_TF']              = _PMOSA_Xvt_MinExten_TF
        _Caculation_Parameters['_Xvt_Placement']                = _PMOSA_Xvt_Placement

        _Caculation_Parameters['_POGate_Comb_TF']               = _PMOSA_POGate_Comb_TF
        _Caculation_Parameters['_POGate_Comb_length']           = _PMOSA_POGate_Comb_length
        _Caculation_Parameters['_POGate_Via_TF']                = _PMOSA_POGate_Via_TF
        _Caculation_Parameters['_POGate_ViaMxMx']               = _PMOSA_POGate_ViaMxMx

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_PMOSA'] = self._SrefElementDeclaration(_DesignObj=A14_Mosfet_KJH2._Mosfet(_DesignParameter=None, _Name='{}:SRF_PMOSA'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_PMOSA_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_PMOSA']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_PMOSA']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_PMOSA']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_PMOSA']['_XYCoordinates'] = [[0, 0]]


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOSB
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  PMOSB: Sref Fake Gen. for Cal
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A14_Mosfet_KJH2._Mosfet._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_MosType']                      = _PMOSB_MosType
        _Caculation_Parameters['_MosUpDn']                      = _PMOSB_MosUpDn

        _Caculation_Parameters['_NumberofGate']                 = _PMOSB_NumberofGate
        _Caculation_Parameters['_ChannelWidth']                 = _PMOSB_ChannelWidth
        _Caculation_Parameters['_ChannelLength']                = _PMOSB_ChannelLength
        _Caculation_Parameters['_GateSpacing']                  = _PMOSB_GateSpacing
        _Caculation_Parameters['_SDWidth']                      = _PMOSB_SDWidth
        _Caculation_Parameters['_XVT']                          = _PMOSB_XVT
        _Caculation_Parameters['_PCCrit']                       = _PMOSB_PCCrit

        _Caculation_Parameters['_Source_Via_TF']                = _PMOSB_Source_Via_TF
        _Caculation_Parameters['_Source_Via_Close2POpin_TF']    = _PMOSB_Source_Via_Close2POpin_TF
        _Caculation_Parameters['_Source_Comb_TF']               = _PMOSB_Source_Comb_TF
        _Caculation_Parameters['_Source_Comb_POpinward_TF']     = _PMOSB_Source_Comb_POpinward_TF
        _Caculation_Parameters['_Source_Comb_Length']           = _PMOSB_Source_Comb_Length

        _Caculation_Parameters['_Drain_Via_TF']                 = _PMOSB_Drain_Via_TF
        _Caculation_Parameters['_Drain_Via_Close2POpin_TF']     = _PMOSB_Drain_Via_Close2POpin_TF
        _Caculation_Parameters['_Drain_Comb_TF']                = _PMOSB_Drain_Comb_TF
        _Caculation_Parameters['_Drain_Comb_POpinward_TF']      = _PMOSB_Drain_Comb_POpinward_TF
        _Caculation_Parameters['_Drain_Comb_Length']            = _PMOSB_Drain_Comb_Length

        _Caculation_Parameters['_PODummy_TF']                   = _PMOSB_PODummy_TF
        _Caculation_Parameters['_PODummy_Length']               = _PMOSB_PODummy_Length
        _Caculation_Parameters['_PODummy_Placement']            = _PMOSB_PODummy_Placement

        _Caculation_Parameters['_Xvt_MinExten_TF']              = _PMOSB_Xvt_MinExten_TF
        _Caculation_Parameters['_Xvt_Placement']                = _PMOSB_Xvt_Placement

        _Caculation_Parameters['_POGate_Comb_TF']               = _PMOSB_POGate_Comb_TF
        _Caculation_Parameters['_POGate_Comb_length']           = _PMOSB_POGate_Comb_length
        _Caculation_Parameters['_POGate_Via_TF']                = _PMOSB_POGate_Via_TF
        _Caculation_Parameters['_POGate_ViaMxMx']               = _PMOSB_POGate_ViaMxMx

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_PMOSB'] = self._SrefElementDeclaration(_DesignObj=A14_Mosfet_KJH2._Mosfet(_DesignParameter=None, _Name='{}:SRF_PMOSB'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_PMOSB_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_PMOSB']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_PMOSB_POWER'
        self._DesignParameter['SRF_PMOSB']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_PMOSB_POWER'
        self._DesignParameter['SRF_PMOSB']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_PMOSB_POWER'
        self._DesignParameter['SRF_PMOSB']['_XYCoordinates'] = [[0, 0]]


        if _PMOSA_NumberofGate == 1 and _PMOSB_NumberofGate == 1:
                   ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_PMOSB']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
                                    ## x
            tmp1_1 = self.get_param_KJH4('SRF_PMOSA','BND_PODummyLayer')
            target_coordx = tmp1_1[0][-1][0]['_XY_right'][0]
                                    ## y
            tmp1_2 = self.get_param_KJH4('SRF_PMOSA','BND_{}Layer'.format(_PMOSA_XVT))
            target_coordy = tmp1_2[0][0][0]['_XY_down'][1]

            target_coord = [target_coordx,target_coordy]
                                ## Approaching_coord: _XY_type2
                                    ## x
            tmp2_1 = self.get_param_KJH4('SRF_PMOSB','BND_PODummyLayer')
            approaching_coordx = tmp2_1[0][0][0]['_XY_left'][0]
                                    ## y
            tmp2_2 = self.get_param_KJH4('SRF_PMOSB','BND_{}Layer'.format(_PMOSA_XVT))
            approaching_coordy = tmp2_2[0][0][0]['_XY_down'][1]

            approaching_coord = [approaching_coordx,approaching_coordy]
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_PMOSB')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[0] = New_Scoord[0] + 150
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_PMOSB']['_XYCoordinates'] = tmpXY

        else:
                   ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_PMOSB']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
                                    ## x
            tmp1_1 = self.get_param_KJH4('SRF_PMOSA','BND_PODummyLayer')
            target_coordx = tmp1_1[0][-1][0]['_XY_left'][0]
                                    ## y
            tmp1_2 = self.get_param_KJH4('SRF_PMOSA','BND_{}Layer'.format(_PMOSA_XVT))
            target_coordy = tmp1_2[0][0][0]['_XY_down'][1]

            target_coord = [target_coordx,target_coordy]
                                ## Approaching_coord: _XY_type2
                                    ## x
            tmp2_1 = self.get_param_KJH4('SRF_PMOSB','BND_PODummyLayer')
            approaching_coordx = tmp2_1[0][0][0]['_XY_left'][0]
                                    ## y
            tmp2_2 = self.get_param_KJH4('SRF_PMOSB','BND_{}Layer'.format(_PMOSA_XVT))
            approaching_coordy = tmp2_2[0][0][0]['_XY_down'][1]

            approaching_coord = [approaching_coordx,approaching_coordy]
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_PMOSB')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_PMOSB']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Length Cal
        tmp1 = self.get_param_KJH4('SRF_PMOSA','BND_Drain_Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_PMOSB','BND_Source_Hrz_M2')

        if tmp1[0][0][0]['_XY_down'][1] > tmp2[0][0][0]['_XY_down'][1]:
            tmp = self.get_param_KJH4('SRF_PMOSB','SRF_Source_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
            PMOSB_length = tmp1[0][0][0]['_XY_down'][1] - tmp[0][0][0][0][0]['_XY_down'][1]
            PMOSA_length = _PMOSA_Drain_Comb_Length
        else:
            tmp = self.get_param_KJH4('SRF_PMOSA','SRF_Drain_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
            PMOSA_length = tmp2[0][0][0]['_XY_down'][1] - tmp[0][0][0][0][0]['_XY_down'][1]
            PMOSB_length = _PMOSB_Source_Comb_Length

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOSA
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  PMOSA: Sref Fake Gen. for Cal
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A14_Mosfet_KJH2._Mosfet._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_MosType']                      = _PMOSA_MosType
        _Caculation_Parameters['_MosUpDn']                      = _PMOSA_MosUpDn

        _Caculation_Parameters['_NumberofGate']                 = _PMOSA_NumberofGate
        _Caculation_Parameters['_ChannelWidth']                 = _PMOSA_ChannelWidth
        _Caculation_Parameters['_ChannelLength']                = _PMOSA_ChannelLength
        _Caculation_Parameters['_GateSpacing']                  = _PMOSA_GateSpacing
        _Caculation_Parameters['_SDWidth']                      = _PMOSA_SDWidth
        _Caculation_Parameters['_XVT']                          = _PMOSA_XVT
        _Caculation_Parameters['_PCCrit']                       = _PMOSA_PCCrit

        _Caculation_Parameters['_Source_Via_TF']                = _PMOSA_Source_Via_TF
        _Caculation_Parameters['_Source_Via_Close2POpin_TF']    = _PMOSA_Source_Via_Close2POpin_TF
        _Caculation_Parameters['_Source_Comb_TF']               = _PMOSA_Source_Comb_TF
        _Caculation_Parameters['_Source_Comb_POpinward_TF']     = _PMOSA_Source_Comb_POpinward_TF
        _Caculation_Parameters['_Source_Comb_Length']           = _PMOSA_Source_Comb_Length

        _Caculation_Parameters['_Drain_Via_TF']                 = _PMOSA_Drain_Via_TF
        _Caculation_Parameters['_Drain_Via_Close2POpin_TF']     = _PMOSA_Drain_Via_Close2POpin_TF
        _Caculation_Parameters['_Drain_Comb_TF']                = _PMOSA_Drain_Comb_TF
        _Caculation_Parameters['_Drain_Comb_POpinward_TF']      = _PMOSA_Drain_Comb_POpinward_TF
        _Caculation_Parameters['_Drain_Comb_Length']            = PMOSA_length

        _Caculation_Parameters['_PODummy_TF']                   = _PMOSA_PODummy_TF
        _Caculation_Parameters['_PODummy_Length']               = _PMOSA_PODummy_Length
        _Caculation_Parameters['_PODummy_Placement']            = _PMOSA_PODummy_Placement

        _Caculation_Parameters['_Xvt_MinExten_TF']              = _PMOSA_Xvt_MinExten_TF
        _Caculation_Parameters['_Xvt_Placement']                = _PMOSA_Xvt_Placement

        _Caculation_Parameters['_POGate_Comb_TF']               = _PMOSA_POGate_Comb_TF
        _Caculation_Parameters['_POGate_Comb_length']           = _PMOSA_POGate_Comb_length
        _Caculation_Parameters['_POGate_Via_TF']                = _PMOSA_POGate_Via_TF
        _Caculation_Parameters['_POGate_ViaMxMx']               = _PMOSA_POGate_ViaMxMx

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_PMOSA'] = self._SrefElementDeclaration(_DesignObj=A14_Mosfet_KJH2._Mosfet(_DesignParameter=None, _Name='{}:SRF_PMOSA'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_PMOSA_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_PMOSA']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_PMOSA']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_PMOSA']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_PMOSA']['_XYCoordinates'] = [[0, 0]]


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOSB
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  PMOSB: Sref Fake Gen. for Cal
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A14_Mosfet_KJH2._Mosfet._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_MosType']                      = _PMOSB_MosType
        _Caculation_Parameters['_MosUpDn']                      = _PMOSB_MosUpDn

        _Caculation_Parameters['_NumberofGate']                 = _PMOSB_NumberofGate
        _Caculation_Parameters['_ChannelWidth']                 = _PMOSB_ChannelWidth
        _Caculation_Parameters['_ChannelLength']                = _PMOSB_ChannelLength
        _Caculation_Parameters['_GateSpacing']                  = _PMOSB_GateSpacing
        _Caculation_Parameters['_SDWidth']                      = _PMOSB_SDWidth
        _Caculation_Parameters['_XVT']                          = _PMOSB_XVT
        _Caculation_Parameters['_PCCrit']                       = _PMOSB_PCCrit

        _Caculation_Parameters['_Source_Via_TF']                = _PMOSB_Source_Via_TF
        _Caculation_Parameters['_Source_Via_Close2POpin_TF']    = _PMOSB_Source_Via_Close2POpin_TF
        _Caculation_Parameters['_Source_Comb_TF']               = _PMOSB_Source_Comb_TF
        _Caculation_Parameters['_Source_Comb_POpinward_TF']     = _PMOSB_Source_Comb_POpinward_TF
        _Caculation_Parameters['_Source_Comb_Length']           = PMOSB_length

        _Caculation_Parameters['_Drain_Via_TF']                 = _PMOSB_Drain_Via_TF
        _Caculation_Parameters['_Drain_Via_Close2POpin_TF']     = _PMOSB_Drain_Via_Close2POpin_TF
        _Caculation_Parameters['_Drain_Comb_TF']                = _PMOSB_Drain_Comb_TF
        _Caculation_Parameters['_Drain_Comb_POpinward_TF']      = _PMOSB_Drain_Comb_POpinward_TF
        _Caculation_Parameters['_Drain_Comb_Length']            = _PMOSB_Drain_Comb_Length

        _Caculation_Parameters['_PODummy_TF']                   = _PMOSB_PODummy_TF
        _Caculation_Parameters['_PODummy_Length']               = _PMOSB_PODummy_Length
        _Caculation_Parameters['_PODummy_Placement']            = _PMOSB_PODummy_Placement

        _Caculation_Parameters['_Xvt_MinExten_TF']              = _PMOSB_Xvt_MinExten_TF
        _Caculation_Parameters['_Xvt_Placement']                = _PMOSB_Xvt_Placement

        _Caculation_Parameters['_POGate_Comb_TF']               = _PMOSB_POGate_Comb_TF
        _Caculation_Parameters['_POGate_Comb_length']           = _PMOSB_POGate_Comb_length
        _Caculation_Parameters['_POGate_Via_TF']                = _PMOSB_POGate_Via_TF
        _Caculation_Parameters['_POGate_ViaMxMx']               = _PMOSB_POGate_ViaMxMx

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_PMOSB'] = self._SrefElementDeclaration(_DesignObj=A14_Mosfet_KJH2._Mosfet(_DesignParameter=None, _Name='{}:SRF_PMOSB'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_PMOSB_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_PMOSB']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_PMOSB_POWER'
        self._DesignParameter['SRF_PMOSB']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_PMOSB_POWER'
        self._DesignParameter['SRF_PMOSB']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_PMOSB_POWER'
        self._DesignParameter['SRF_PMOSB']['_XYCoordinates'] = [[0, 0]]


        if _PMOSA_NumberofGate == 1 and _PMOSB_NumberofGate == 1:
                   ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_PMOSB']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
                                    ## x
            tmp1_1 = self.get_param_KJH4('SRF_PMOSA','BND_PODummyLayer')
            target_coordx = tmp1_1[0][-1][0]['_XY_right'][0]
                                    ## y
            tmp1_2 = self.get_param_KJH4('SRF_PMOSA','BND_{}Layer'.format(_PMOSA_XVT))
            target_coordy = tmp1_2[0][0][0]['_XY_down'][1]

            target_coord = [target_coordx,target_coordy]
                                ## Approaching_coord: _XY_type2
                                    ## x
            tmp2_1 = self.get_param_KJH4('SRF_PMOSB','BND_PODummyLayer')
            approaching_coordx = tmp2_1[0][0][0]['_XY_left'][0]
                                    ## y
            tmp2_2 = self.get_param_KJH4('SRF_PMOSB','BND_{}Layer'.format(_PMOSA_XVT))
            approaching_coordy = tmp2_2[0][0][0]['_XY_down'][1]

            approaching_coord = [approaching_coordx,approaching_coordy]
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_PMOSB')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[0] = New_Scoord[0] + 150
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_PMOSB']['_XYCoordinates'] = tmpXY

        else:
                   ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_PMOSB']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
                                    ## x
            tmp1_1 = self.get_param_KJH4('SRF_PMOSA','BND_PODummyLayer')
            target_coordx = tmp1_1[0][-1][0]['_XY_left'][0]
                                    ## y
            tmp1_2 = self.get_param_KJH4('SRF_PMOSA','BND_{}Layer'.format(_PMOSA_XVT))
            target_coordy = tmp1_2[0][0][0]['_XY_down'][1]

            target_coord = [target_coordx,target_coordy]
                                ## Approaching_coord: _XY_type2
                                    ## x
            tmp2_1 = self.get_param_KJH4('SRF_PMOSB','BND_PODummyLayer')
            approaching_coordx = tmp2_1[0][0][0]['_XY_left'][0]
                                    ## y
            tmp2_2 = self.get_param_KJH4('SRF_PMOSB','BND_{}Layer'.format(_PMOSA_XVT))
            approaching_coordy = tmp2_2[0][0][0]['_XY_down'][1]

            approaching_coord = [approaching_coordx,approaching_coordy]
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_PMOSB')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_PMOSB']['_XYCoordinates'] = tmpXY




        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOSA drain PMOSB source connection M2
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOSADrain_PMOSBSource_Hrz_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('SRF_PMOSA','BND_Drain_Hrz_M2')
        self._DesignParameter['BND_PMOSADrain_PMOSBSource_Hrz_M2']['_YWidth'] = tmp[0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_PMOSA','BND_Drain_Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_PMOSB','BND_Source_Hrz_M2')
        self._DesignParameter['BND_PMOSADrain_PMOSBSource_Hrz_M2']['_XWidth'] = abs( tmp2[0][0][0]['_XY_right'][0] - tmp1[0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOSADrain_PMOSBSource_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
            ## initialized Sref coordinate
        self._DesignParameter['BND_PMOSADrain_PMOSBSource_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
                ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_PMOSA','BND_Drain_Hrz_M2')
        target_coord = tmp1[0][0][0]['_XY_down_left']
                ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOSADrain_PMOSBSource_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOSADrain_PMOSBSource_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_PMOSADrain_PMOSBSource_Hrz_M2']['_XYCoordinates'] = tmpXY



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
    libname = 'Proj_ADC_D02_SARLogic_Nor_KJH1'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'D02_01_Pullup_v0_78'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

    # PMosfetA
        # PMOS/NMOS
        _PMOSA_MosType                   = 'PMOS',   # 'NMOS'/'PMOS'
        # MOS Up/Dn
        _PMOSA_MosUpDn                   = 'Dn',     # 'Up'/'Dn'
        # Physical dimension
        _PMOSA_NumberofGate	            = 5,        # Number
        _PMOSA_ChannelWidth	            = 811,      # Number
        _PMOSA_ChannelLength	        = 30,       # Number
        _PMOSA_GateSpacing		        = None,     # None/Number
        _PMOSA_SDWidth			        = None,     # None/Number
        _PMOSA_XVT				        = 'SLVT',   # 'XVT' ex)SLVT/LVT/RVT/HVT
        _PMOSA_PCCrit				    = True,     # None/True
        # Source_node setting
            # Via setting
        _PMOSA_Source_Via_TF              = False,     # True/False
                # Via close to POpin
        _PMOSA_Source_Via_Close2POpin_TF  = False,     # True/False
            # Comb setting: If Via is True
        _PMOSA_Source_Comb_TF             = False,     # True/False
                # Comb POPinward
        _PMOSA_Source_Comb_POpinward_TF   = False,     # True/False
                # Comb vertical_length
        _PMOSA_Source_Comb_Length         = None,     # None/Number

        # Drain_node_setting
            # Via setting
        _PMOSA_Drain_Via_TF               = True,     # True/False
                # Via close to POpin
        _PMOSA_Drain_Via_Close2POpin_TF   = False,     # True/False
            # Comb setting: If Via is True
        _PMOSA_Drain_Comb_TF              = True,     # True/False
                # Comb POPinward
        _PMOSA_Drain_Comb_POpinward_TF    = False,     # True/False
                # Comb vertical_length
        _PMOSA_Drain_Comb_Length          = None,     # None/Number

        # POLY dummy setting
        _PMOSA_PODummy_TF                 = True,  # TF
            # if _PMOSADummy == True
        _PMOSA_PODummy_Length             = None,  # None/Value
        _PMOSA_PODummy_Placement          = None,  # None/'Up'/'Dn'/

        # XVT setting
            # XVT setting : Exten XVT area if area is min
        _PMOSA_Xvt_MinExten_TF            = True,     # True/False
            # XVT setting : None(Cent), Up, Dn
        _PMOSA_Xvt_Placement              = 'Dn',     # None/'Up'/'Dn'/

        # Poly Gate setting
        _PMOSA_POGate_Comb_TF             = True,     # True/False
            # Poly Gate setting : vertical length
        _PMOSA_POGate_Comb_length         = 100,     # None/Number
            # Poly Gate Via setting
        _PMOSA_POGate_Via_TF              = True,     # True/False
            # Poly Gate Via setting :
        _PMOSA_POGate_ViaMxMx             = [0 ,1],     # Ex) [1,5] -> ViaM1M5


    # PMosfetB
        # PMOS/NMOS
        _PMOSB_MosType                   = 'PMOS',   # 'NMOS'/'PMOS'
        # MOS Up/Dn
        _PMOSB_MosUpDn                   = 'Dn',     # 'Up'/'Dn'
        # Physical dimension
        _PMOSB_NumberofGate	            = 4,        # Number
        _PMOSB_ChannelWidth	            = 350,      # Number
        _PMOSB_ChannelLength	        = 30,       # Number
        _PMOSB_GateSpacing		        = None,     # None/Number
        _PMOSB_SDWidth			        = None,     # None/Number
        _PMOSB_XVT				        = 'SLVT',   # 'XVT' ex)SLVT/LVT/RVT/HVT
        _PMOSB_PCCrit				    = True,     # None/True
        # Source_node setting
            # Via setting
        _PMOSB_Source_Via_TF              = True,     # True/False
                # Via close to POpin
        _PMOSB_Source_Via_Close2POpin_TF  = False,     # True/False
            # Comb setting: If Via is True
        _PMOSB_Source_Comb_TF             = True,     # True/False
                # Comb POPinward
        _PMOSB_Source_Comb_POpinward_TF   = False,     # True/False
                # Comb vertical_length
        _PMOSB_Source_Comb_Length         = None,     # None/Number

        # Drain_node_setting
            # Via setting
        _PMOSB_Drain_Via_TF               = True,     # True/False
                # Via close to POpin
        _PMOSB_Drain_Via_Close2POpin_TF   = True,     # True/False
            # Comb setting: If Via is True
        _PMOSB_Drain_Comb_TF              = True,     # True/False
                # Comb POPinward
        _PMOSB_Drain_Comb_POpinward_TF    = True,     # True/False
                # Comb vertical_length
        _PMOSB_Drain_Comb_Length          = None,     # None/Number

        # POLY dummy setting
        _PMOSB_PODummy_TF                 = True,  # TF
            # if _PMOSBDummy == True
        _PMOSB_PODummy_Length             = None,  # None/Value
        _PMOSB_PODummy_Placement          = None,  # None/'Up'/'Dn'/

        # XVT setting
            # XVT setting : Exten XVT area if area is min
        _PMOSB_Xvt_MinExten_TF            = True,     # True/False
            # XVT setting : None(Cent), Up, Dn
        _PMOSB_Xvt_Placement              = 'Dn',     # None/'Up'/'Dn'/

        # Poly Gate setting
        _PMOSB_POGate_Comb_TF             = True,     # True/False
            # Poly Gate setting : vertical length
        _PMOSB_POGate_Comb_length         = 100,     # None/Number
            # Poly Gate Via setting
        _PMOSB_POGate_Via_TF              = True,     # None/'Up'/'Dn'/
            # Poly Gate Via setting :
        _PMOSB_POGate_ViaMxMx             = [0 ,1],     # Ex) [1,5] -> ViaM1M5


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
    LayoutObj = _Pullup(_DesignParameter=None, _Name=cellname)
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
