
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
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A08_PbodyContactPhyLen_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A07_NbodyContactPhyLen_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A14_Mosfet_KJH2


## Define Class
class _Inverter(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(

    # NMosfet
        # PMOS/NMOS
        _NMOS_MosType                   = 'NMOS',   # 'NMOS'/'PMOS'
        # MOS Up/Dn
        _NMOS_MosUpDn                   = 'Up',     # 'Up'/'Dn'
        # Physical dimension
        _NMOS_NumberofGate	            = 3,        # Number
        _NMOS_ChannelWidth	            = 200,      # Number
        _NMOS_ChannelLength	            = 30,       # Number
        _NMOS_GateSpacing		        = None,     # None/Number
        _NMOS_SDWidth			        = None,     # None/Number
        _NMOS_XVT				        = 'SLVT',   # 'XVT' ex)SLVT/LVT/RVT/HVT
        _NMOS_PCCrit				    = True,     # None/True
        # Source_node setting
            # Via setting
        _NMOS_Source_Via_TF              = False,     # True/False
                # Via close to POpin
        _NMOS_Source_Via_Close2POpin_TF  = False,     # True/False
            # Comb setting: If Via is True
        _NMOS_Source_Comb_TF             = False,     # True/False
                # Comb POPinward
        _NMOS_Source_Comb_POpinward_TF   = False,     # True/False
                # Comb vertical_length
        _NMOS_Source_Comb_Length         = None,     # None/Number

        # Drain_node_setting
            # Via setting
        _NMOS_Drain_Via_TF               = True,     # True/False
                # Via close to POpin
        _NMOS_Drain_Via_Close2POpin_TF   = True,     # True/False
            # Comb setting: If Via is True
        _NMOS_Drain_Comb_TF              = True,     # True/False
                # Comb POPinward
        _NMOS_Drain_Comb_POpinward_TF    = True,     # True/False
                # Comb vertical_length
        _NMOS_Drain_Comb_Length          = 0,     # None/Number

        # POLY dummy setting
        _NMOS_PODummy_TF                 = True,  # TF
            # if _NMOSDummy == True
        _NMOS_PODummy_Length             = None,  # None/Value
        _NMOS_PODummy_Placement          = None,  # None/'Up'/'Dn'/

        # XVT setting
            # XVT setting : Exten XVT area if area is min
        _NMOS_Xvt_MinExten_TF            = True,     # True/False
            # XVT setting : None(Cent), Up, Dn
        _NMOS_Xvt_Placement              = 'Up',     # None/'Up'/'Dn'/

        # Poly Gate setting
        _NMOS_POGate_Comb_TF             = True,     # True/False
            # Poly Gate setting : vertical length
        _NMOS_POGate_Comb_length         = 100,     # None/Number
            # Poly Gate Via setting
        _NMOS_POGate_Via_TF              = True,     # None/'Up'/'Dn'/
            # Poly Gate Via setting :
        _NMOS_POGate_ViaMxMx             = [0 ,1],     # Ex) [1,5] -> ViaM1M5

    # PMosfet
        # PMOS/NMOS
        _PMOS_MosType                   = 'PMOS',   # 'NMOS'/'PMOS'
        # MOS Up/Dn
        _PMOS_MosUpDn                   = 'Dn',     # 'Up'/'Dn'
        # Physical dimension
        _PMOS_NumberofGate	            = 8,        # Number
        _PMOS_ChannelWidth	            = 200,      # Number
        _PMOS_ChannelLength	            = 30,       # Number
        _PMOS_GateSpacing		        = None,     # None/Number
        _PMOS_SDWidth			        = None,     # None/Number
        _PMOS_XVT				        = 'SLVT',   # 'XVT' ex)SLVT/LVT/RVT/HVT
        _PMOS_PCCrit				    = True,     # None/True
        # Source_node setting
            # Via setting
        _PMOS_Source_Via_TF              = False,     # True/False
                # Via close to POpin
        _PMOS_Source_Via_Close2POpin_TF  = False,     # True/False
            # Comb setting: If Via is True
        _PMOS_Source_Comb_TF             = False,     # True/False
                # Comb POPinward
        _PMOS_Source_Comb_POpinward_TF   = False,     # True/False
                # Comb vertical_length
        _PMOS_Source_Comb_Length         = None,     # None/Number

        # Drain_node_setting
            # Via setting
        _PMOS_Drain_Via_TF               = True,     # True/False
                # Via close to POpin
        _PMOS_Drain_Via_Close2POpin_TF   = True,     # True/False
            # Comb setting: If Via is True
        _PMOS_Drain_Comb_TF              = True,     # True/False
                # Comb POPinward
        _PMOS_Drain_Comb_POpinward_TF    = True,     # True/False
                # Comb vertical_length
        _PMOS_Drain_Comb_Length          = 0,       # None/Number

        # POLY dummy setting
        _PMOS_PODummy_TF                 = True,    # TF
            # if _PMOSDummy == True
        _PMOS_PODummy_Length             = None,  # None/Value
        _PMOS_PODummy_Placement          = None,  # None/'Up'/'Dn'/

        # XVT setting
            # XVT setting : Exten XVT area if area is min
        _PMOS_Xvt_MinExten_TF            = True,     # True/False
            # XVT setting : None(Cent), Up, Dn
        _PMOS_Xvt_Placement              = 'Dn',     # None/'Up'/'Dn'/

        # Poly Gate setting
        _PMOS_POGate_Comb_TF             = True,     # True/False
            # Poly Gate setting : vertical length
        _PMOS_POGate_Comb_length         = 100,     # None/Number
            # Poly Gate Via setting
        _PMOS_POGate_Via_TF              = True,     # None/'Up'/'Dn'/
            # Poly Gate Via setting :
        _PMOS_POGate_ViaMxMx             = [0 ,1],     # Ex) [1,5] -> ViaM1M5


    # Pbody
    _NMOS_Pbody_NumCont         = 2,  # Number
    _NMOS_Pbody_XvtTop2Pbody   = None,  # Number/None(Minimum)

    # Nbody
    _PMOS_Nbody_NumCont=2,  # Number
    _PMOS_Nbody_Xvtdown2Nbody=700,  # Number/None(Minimum)

    # PMOS and NMOS Height
    _PMOSXvt2NMOSXvt=1500,                  # number
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
    # NMosfet
        # PMOS/NMOS
        _NMOS_MosType                   = 'NMOS',   # 'NMOS'/'PMOS'
        # MOS Up/Dn
        _NMOS_MosUpDn                   = 'Up',     # 'Up'/'Dn'
        # Physical dimension
        _NMOS_NumberofGate	            = 3,        # Number
        _NMOS_ChannelWidth	            = 200,      # Number
        _NMOS_ChannelLength	            = 30,       # Number
        _NMOS_GateSpacing		        = None,     # None/Number
        _NMOS_SDWidth			        = None,     # None/Number
        _NMOS_XVT				        = 'SLVT',   # 'XVT' ex)SLVT/LVT/RVT/HVT
        _NMOS_PCCrit				    = True,     # None/True
        # Source_node setting
            # Via setting
        _NMOS_Source_Via_TF              = False,     # True/False
                # Via close to POpin
        _NMOS_Source_Via_Close2POpin_TF  = False,     # True/False
            # Comb setting: If Via is True
        _NMOS_Source_Comb_TF             = False,     # True/False
                # Comb POPinward
        _NMOS_Source_Comb_POpinward_TF   = False,     # True/False
                # Comb vertical_length
        _NMOS_Source_Comb_Length         = None,     # None/Number

        # Drain_node_setting
            # Via setting
        _NMOS_Drain_Via_TF               = True,     # True/False
                # Via close to POpin
        _NMOS_Drain_Via_Close2POpin_TF   = True,     # True/False
            # Comb setting: If Via is True
        _NMOS_Drain_Comb_TF              = True,     # True/False
                # Comb POPinward
        _NMOS_Drain_Comb_POpinward_TF    = True,     # True/False
                # Comb vertical_length
        _NMOS_Drain_Comb_Length          = 0,     # None/Number

        # POLY dummy setting
        _NMOS_PODummy_TF                 = True,  # TF
            # if _NMOSDummy == True
        _NMOS_PODummy_Length             = None,  # None/Value
        _NMOS_PODummy_Placement          = None,  # None/'Up'/'Dn'/

        # XVT setting
            # XVT setting : Exten XVT area if area is min
        _NMOS_Xvt_MinExten_TF            = True,     # True/False
            # XVT setting : None(Cent), Up, Dn
        _NMOS_Xvt_Placement              = 'Up',     # None/'Up'/'Dn'/

        # Poly Gate setting
        _NMOS_POGate_Comb_TF             = True,     # True/False
            # Poly Gate setting : vertical length
        _NMOS_POGate_Comb_length         = 100,     # None/Number
            # Poly Gate Via setting
        _NMOS_POGate_Via_TF              = True,     # None/'Up'/'Dn'/
            # Poly Gate Via setting :
        _NMOS_POGate_ViaMxMx             = [0 ,1],     # Ex) [1,5] -> ViaM1M5

    # PMosfet
        # PMOS/NMOS
        _PMOS_MosType                   = 'PMOS',   # 'NMOS'/'PMOS'
        # MOS Up/Dn
        _PMOS_MosUpDn                   = 'Dn',     # 'Up'/'Dn'
        # Physical dimension
        _PMOS_NumberofGate	            = 8,        # Number
        _PMOS_ChannelWidth	            = 200,      # Number
        _PMOS_ChannelLength	            = 30,       # Number
        _PMOS_GateSpacing		        = None,     # None/Number
        _PMOS_SDWidth			        = None,     # None/Number
        _PMOS_XVT				        = 'SLVT',   # 'XVT' ex)SLVT/LVT/RVT/HVT
        _PMOS_PCCrit				    = True,     # None/True
        # Source_node setting
            # Via setting
        _PMOS_Source_Via_TF              = False,     # True/False
                # Via close to POpin
        _PMOS_Source_Via_Close2POpin_TF  = False,     # True/False
            # Comb setting: If Via is True
        _PMOS_Source_Comb_TF             = False,     # True/False
                # Comb POPinward
        _PMOS_Source_Comb_POpinward_TF   = False,     # True/False
                # Comb vertical_length
        _PMOS_Source_Comb_Length         = None,     # None/Number

        # Drain_node_setting
            # Via setting
        _PMOS_Drain_Via_TF               = True,     # True/False
                # Via close to POpin
        _PMOS_Drain_Via_Close2POpin_TF   = True,     # True/False
            # Comb setting: If Via is True
        _PMOS_Drain_Comb_TF              = True,     # True/False
                # Comb POPinward
        _PMOS_Drain_Comb_POpinward_TF    = True,     # True/False
                # Comb vertical_length
        _PMOS_Drain_Comb_Length          = 0,       # None/Number

        # POLY dummy setting
        _PMOS_PODummy_TF                 = True,    # TF
            # if _PMOSDummy == True
        _PMOS_PODummy_Length             = None,  # None/Value
        _PMOS_PODummy_Placement          = None,  # None/'Up'/'Dn'/

        # XVT setting
            # XVT setting : Exten XVT area if area is min
        _PMOS_Xvt_MinExten_TF            = True,     # True/False
            # XVT setting : None(Cent), Up, Dn
        _PMOS_Xvt_Placement              = 'Dn',     # None/'Up'/'Dn'/

        # Poly Gate setting
        _PMOS_POGate_Comb_TF             = True,     # True/False
            # Poly Gate setting : vertical length
        _PMOS_POGate_Comb_length         = 100,     # None/Number
            # Poly Gate Via setting
        _PMOS_POGate_Via_TF              = True,     # None/'Up'/'Dn'/
            # Poly Gate Via setting :
        _PMOS_POGate_ViaMxMx             = [0 ,1],     # Ex) [1,5] -> ViaM1M5


    # Pbody
    _NMOS_Pbody_NumCont         = 2,  # Number
    _NMOS_Pbody_XvtTop2Pbody   = None,  # Number/None(Minimum)

    # Nbody
    _PMOS_Nbody_NumCont=2,  # Number
    _PMOS_Nbody_Xvtdown2Nbody=700,  # Number/None(Minimum)

    # PMOS and NMOS Height
    _PMOSXvt2NMOSXvt=1500,                  # number

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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  NMOS: Sref Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A14_Mosfet_KJH2._Mosfet._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_MosType']                      = _NMOS_MosType
        _Caculation_Parameters['_MosUpDn']                      = _NMOS_MosUpDn

        _Caculation_Parameters['_NumberofGate']                 = _NMOS_NumberofGate
        _Caculation_Parameters['_ChannelWidth']                 = _NMOS_ChannelWidth
        _Caculation_Parameters['_ChannelLength']                = _NMOS_ChannelLength
        _Caculation_Parameters['_GateSpacing']                  = _NMOS_GateSpacing
        _Caculation_Parameters['_SDWidth']                      = _NMOS_SDWidth
        _Caculation_Parameters['_XVT']                          = _NMOS_XVT
        _Caculation_Parameters['_PCCrit']                       = _NMOS_PCCrit

        _Caculation_Parameters['_Source_Via_TF']                = _NMOS_Source_Via_TF
        _Caculation_Parameters['_Source_Via_Close2POpin_TF']    = _NMOS_Source_Via_Close2POpin_TF
        _Caculation_Parameters['_Source_Comb_TF']               = _NMOS_Source_Comb_TF
        _Caculation_Parameters['_Source_Comb_POpinward_TF']     = _NMOS_Source_Comb_POpinward_TF
        _Caculation_Parameters['_Source_Comb_Length']           = _NMOS_Source_Comb_Length

        _Caculation_Parameters['_Drain_Via_TF']                 = _NMOS_Drain_Via_TF
        _Caculation_Parameters['_Drain_Via_Close2POpin_TF']     = _NMOS_Drain_Via_Close2POpin_TF
        _Caculation_Parameters['_Drain_Comb_TF']                = _NMOS_Drain_Comb_TF
        _Caculation_Parameters['_Drain_Comb_POpinward_TF']      = _NMOS_Drain_Comb_POpinward_TF
        _Caculation_Parameters['_Drain_Comb_Length']            = _NMOS_Drain_Comb_Length

        _Caculation_Parameters['_PODummy_TF']                   = _NMOS_PODummy_TF
        _Caculation_Parameters['_PODummy_Length']               = _NMOS_PODummy_Length
        _Caculation_Parameters['_PODummy_Placement']            = _NMOS_PODummy_Placement

        _Caculation_Parameters['_Xvt_MinExten_TF']              = _NMOS_Xvt_MinExten_TF
        _Caculation_Parameters['_Xvt_Placement']                = _NMOS_Xvt_Placement

        _Caculation_Parameters['_POGate_Comb_TF']               = _NMOS_POGate_Comb_TF
        _Caculation_Parameters['_POGate_Comb_length']           = _NMOS_POGate_Comb_length
        _Caculation_Parameters['_POGate_Via_TF']                = _NMOS_POGate_Via_TF
        _Caculation_Parameters['_POGate_ViaMxMx']               = _NMOS_POGate_ViaMxMx

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_NMOS'] = self._SrefElementDeclaration(_DesignObj=A14_Mosfet_KJH2._Mosfet(_DesignParameter=None, _Name='{}:SRF_NMOS'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_NMOS']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NMOS']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NMOS']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NMOS']['_XYCoordinates'] = [[0, 0]]





        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  NMOS: Pbody Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length']      = None
        _Caculation_Parameters['_NumCont']     = _NMOS_Pbody_NumCont
        _Caculation_Parameters['_Vtc_flag']    = False

        ## Calculate '_Length'
        tmp = self.get_outter_KJH4('SRF_NMOS')
        _Caculation_Parameters['_Length'] = abs(tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0])

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Pbody'] = self._SrefElementDeclaration(_DesignObj=A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen(_DesignParameter=None, _Name='{}:SRF_Pbody'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Pbody']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbody']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbody']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbody']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Pbody']['_XYCoordinates'] = [[0, 0]]

        if _NMOS_Pbody_XvtTop2Pbody == None:
                            ## Calculate
                                ## Target_coord: _XY_type1
                                    ## X
            tmp1 = self.get_outter_KJH4('SRF_NMOS')
            target_coordx = np.round( 0.5 * (tmp1['_Mostright']['coord'][0] + tmp1['_Mostleft']['coord'][0]) )
                                    ## Y
            target_coordy = tmp1['_Mostdown']['coord'][0]

            target_coord = [target_coordx,target_coordy]

                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_up']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Pbody')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[1] = New_Scoord[1] - 70
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_Pbody']['_XYCoordinates'] = tmpXY

        else:
                            ## Calculate
                                ## Target_coord: _XY_type1
                                    ## X
            tmp1_1 = self.get_outter_KJH4('SRF_NMOS')
            target_coordx = np.round( 0.5 * (tmp1_1['_Mostright']['coord'][0] + tmp1_1['_Mostleft']['coord'][0]) )
                                    ## Y
            tmp1_2 = self.get_param_KJH4('SRF_NMOS','BND_{}Layer'.format(_NMOS_XVT))
            target_coordy = tmp1_2[0][0][0]['_XY_up'][1]

            target_coord = [target_coordx,target_coordy]
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_up']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Pbody')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[1] = New_Scoord[1] - _NMOS_Pbody_XvtTop2Pbody
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_Pbody']['_XYCoordinates'] = tmpXY





        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  NMOS: Pbody Nmos source M1 connection.
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NMOS_Source2PBody_Vtc_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_NMOS','BND_Source_M1')
        tmp2 = self.get_param_KJH4('SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_NMOS_Source2PBody_Vtc_M1']['_YWidth'] = tmp1[0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1]

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_NMOS','BND_Source_M1')
        self._DesignParameter['BND_NMOS_Source2PBody_Vtc_M1']['_XWidth'] = tmp[0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NMOS_Source2PBody_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        tmp = self.get_param_KJH4('SRF_NMOS','BND_Source_M1')
        for i in range(0,len(tmp[0])):
                ## Calculate
                    ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_NMOS','BND_Source_M1')
            target_coord = tmp1[0][i][0]['_XY_up_left']
                    ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_NMOS_Source2PBody_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_up_left']
                    ## Sref coord
            tmp3 = self.get_param_KJH4('BND_NMOS_Source2PBody_Vtc_M1')
            Scoord = tmp3[0][0]['_XY_origin']
                    ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_NMOS_Source2PBody_Vtc_M1']['_XYCoordinates'] = tmpXY





        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  PMOS: Sref Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A14_Mosfet_KJH2._Mosfet._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_MosType']                      = _PMOS_MosType
        _Caculation_Parameters['_MosUpDn']                      = _PMOS_MosUpDn

        _Caculation_Parameters['_NumberofGate']                 = _PMOS_NumberofGate
        _Caculation_Parameters['_ChannelWidth']                 = _PMOS_ChannelWidth
        _Caculation_Parameters['_ChannelLength']                = _PMOS_ChannelLength
        _Caculation_Parameters['_GateSpacing']                  = _PMOS_GateSpacing
        _Caculation_Parameters['_SDWidth']                      = _PMOS_SDWidth
        _Caculation_Parameters['_XVT']                          = _PMOS_XVT
        _Caculation_Parameters['_PCCrit']                       = _PMOS_PCCrit

        _Caculation_Parameters['_Source_Via_TF']                = _PMOS_Source_Via_TF
        _Caculation_Parameters['_Source_Via_Close2POpin_TF']    = _PMOS_Source_Via_Close2POpin_TF
        _Caculation_Parameters['_Source_Comb_TF']               = _PMOS_Source_Comb_TF
        _Caculation_Parameters['_Source_Comb_POpinward_TF']     = _PMOS_Source_Comb_POpinward_TF
        _Caculation_Parameters['_Source_Comb_Length']           = _PMOS_Source_Comb_Length

        _Caculation_Parameters['_Drain_Via_TF']                 = _PMOS_Drain_Via_TF
        _Caculation_Parameters['_Drain_Via_Close2POpin_TF']     = _PMOS_Drain_Via_Close2POpin_TF
        _Caculation_Parameters['_Drain_Comb_TF']                = _PMOS_Drain_Comb_TF
        _Caculation_Parameters['_Drain_Comb_POpinward_TF']      = _PMOS_Drain_Comb_POpinward_TF
        _Caculation_Parameters['_Drain_Comb_Length']            = _PMOS_Drain_Comb_Length

        _Caculation_Parameters['_PODummy_TF']                   = _PMOS_PODummy_TF
        _Caculation_Parameters['_PODummy_Length']               = _PMOS_PODummy_Length
        _Caculation_Parameters['_PODummy_Placement']            = _PMOS_PODummy_Placement

        _Caculation_Parameters['_Xvt_MinExten_TF']              = _PMOS_Xvt_MinExten_TF
        _Caculation_Parameters['_Xvt_Placement']                = _PMOS_Xvt_Placement

        _Caculation_Parameters['_POGate_Comb_TF']               = _PMOS_POGate_Comb_TF
        _Caculation_Parameters['_POGate_Comb_length']           = _PMOS_POGate_Comb_length
        _Caculation_Parameters['_POGate_Via_TF']                = _PMOS_POGate_Via_TF
        _Caculation_Parameters['_POGate_ViaMxMx']               = _PMOS_POGate_ViaMxMx

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_PMOS'] = self._SrefElementDeclaration(_DesignObj=A14_Mosfet_KJH2._Mosfet(_DesignParameter=None, _Name='{}:SRF_PMOS'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_PMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_PMOS']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_PMOS_POWER'
        self._DesignParameter['SRF_PMOS']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_PMOS_POWER'
        self._DesignParameter['SRF_PMOS']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_PMOS_POWER'
        self._DesignParameter['SRF_PMOS']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_PMOS']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_NMOS','BND_{}Layer'.format(_NMOS_XVT))
        target_coord = tmp1[0][0][0]['_XY_up']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_PMOS','BND_{}Layer'.format(_PMOS_XVT))
        approaching_coord = tmp2[0][0][0]['_XY_down']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_PMOS')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[1] = New_Scoord[1] +  _PMOSXvt2NMOSXvt
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_PMOS']['_XYCoordinates'] = tmpXY





        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  PMOS: Nbody Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A07_NbodyContactPhyLen_KJH3._NbodyContactPhyLen._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length']      = None
        _Caculation_Parameters['_NumCont']     = _PMOS_Nbody_NumCont
        _Caculation_Parameters['_Vtc_flag']    = False

        ## Calculate '_Length'
        tmp = self.get_outter_KJH4('SRF_PMOS')
        _Caculation_Parameters['_Length']      = abs(tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0])

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Nbody'] = self._SrefElementDeclaration(_DesignObj=A07_NbodyContactPhyLen_KJH3._NbodyContactPhyLen(_DesignParameter=None, _Name='{}:SRF_Nbody'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Nbody']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nbody']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nbody']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nbody']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Nbody']['_XYCoordinates'] = [[0, 0]]

        if _PMOS_Nbody_Xvtdown2Nbody == None:
                            ## Calculate
                                ## Target_coord: _XY_type1
                                    ## X
            tmp1_1 = self.get_param_KJH4('SRF_PMOS', 'BND_{}Layer'.format(_PMOS_XVT))
            target_coordx = tmp1_1[0][0][0]['_XY_cent'][0]
                                    ## Y
            tmp1_2 = self.get_outter_KJH4('SRF_PMOS')
            target_coordy = tmp1_2['_Mostup']['coord'][0]

            target_coord = [target_coordx,target_coordy]
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_down']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Nbody')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[1] = New_Scoord[1] + 70
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_Nbody']['_XYCoordinates'] = tmpXY

        else:
                            ## Calculate
                                ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_PMOS','BND_{}Layer'.format(_PMOS_XVT))
            target_coord = tmp1[0][0][0]['_XY_down']
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_down']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Nbody')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[1] = New_Scoord[1] + _PMOS_Nbody_Xvtdown2Nbody
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_Nbody']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  PMOS: Nbody Pmos source M1 connection.
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOS_Source2NBody_Vtc_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_PMOS','BND_Source_M1')
        tmp2 = self.get_param_KJH4('SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_PMOS_Source2NBody_Vtc_M1']['_YWidth'] = abs( tmp1[0][0][0]['_XY_down'][1] - tmp2[0][0][0][0]['_XY_up'][1] )

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_PMOS','BND_Source_M1')
        self._DesignParameter['BND_PMOS_Source2NBody_Vtc_M1']['_XWidth'] = tmp[0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOS_Source2NBody_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        tmp = self.get_param_KJH4('SRF_PMOS','BND_Source_M1')
        for i in range(0,len(tmp[0])):
                ## Calculate
                    ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_PMOS','BND_Source_M1')
            target_coord = tmp1[0][i][0]['_XY_down_left']
                    ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_PMOS_Source2NBody_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_down_left']
                    ## Sref coord
            tmp3 = self.get_param_KJH4('BND_PMOS_Source2NBody_Vtc_M1')
            Scoord = tmp3[0][0]['_XY_origin']
                    ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_PMOS_Source2NBody_Vtc_M1']['_XYCoordinates'] = tmpXY



        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  PMOS: NWELL Exten
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOS_NellExten'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Nbody','SRF_NbodyContactPhyLen','BND_Nwell')
        tmp2 = self.get_param_KJH4('SRF_PMOS','BND_{}Layer'.format(_PMOS_XVT))
        self._DesignParameter['BND_PMOS_NellExten']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0]['_XY_down'][1] )

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Nbody','SRF_NbodyContactPhyLen','BND_Nwell')
        self._DesignParameter['BND_PMOS_NellExten']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOS_NellExten']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
            ## initialized Sref coordinate
        self._DesignParameter['BND_PMOS_NellExten']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
                ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Nbody','SRF_NbodyContactPhyLen','BND_Nwell')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
                ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOS_NellExten')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOS_NellExten')
        Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_PMOS_NellExten']['_XYCoordinates'] = tmpXY





        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  IN/OUT
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########   IN/OUT : Input
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## IN/OUT : Input : Hrz M1
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Input_Hrz_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_NMOS', 'BND_Gate_Hrz_Mx')
        tmp2 = self.get_param_KJH4('SRF_PMOS', 'BND_Gate_Hrz_Mx')
        self._DesignParameter['BND_Input_Hrz_M1']['_XWidth'] = abs( tmp2[0][0][0]['_XY_left'][0] - tmp1[0][0][0]['_XY_left'][0])

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Input_Hrz_M1']['_YWidth'] = 50

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Input_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Input_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_NMOS', 'BND_Gate_Hrz_Mx')
        tmp2 = self.get_param_KJH4('SRF_PMOS', 'BND_Gate_Hrz_Mx')

        if tmp2[0][0][0]['_XY_left'][0] > tmp1[0][0][0]['_XY_left'][0]:
            tmp1_1 = self.get_param_KJH4('SRF_PMOS', 'BND_Gate_Hrz_Mx')
            target_coord = tmp1_1[0][0][0]['_XY_down_left']
        else:
            tmp1_1 = self.get_param_KJH4('SRF_NMOS', 'BND_Gate_Hrz_Mx')
            target_coord = tmp1_1[0][0][0]['_XY_down_left']

        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Input_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_down_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Input_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Input_Hrz_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## IN/OUT : Input : Vtc M1
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Input_Vtc_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_NMOS', 'BND_Gate_Hrz_Mx')
        tmp2 = self.get_param_KJH4('SRF_PMOS', 'BND_Gate_Hrz_Mx')
        self._DesignParameter['BND_Input_Vtc_M1']['_YWidth'] = abs( tmp2[0][0][0]['_XY_up'][1] - tmp1[0][0][0]['_XY_down'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Input_Vtc_M1']['_XWidth'] = 50

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Input_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Input_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_NMOS', 'BND_Gate_Hrz_Mx')
        tmp2 = self.get_param_KJH4('SRF_PMOS', 'BND_Gate_Hrz_Mx')

        if tmp2[0][0][0]['_XY_left'][0] > tmp1[0][0][0]['_XY_left'][0]:
            tmp1_1 = self.get_param_KJH4('BND_Input_Hrz_M1')
            target_coord = tmp1_1[0][0]['_XY_up_left']

        else:
            tmp1_1 = self.get_param_KJH4('BND_Input_Hrz_M1')
            target_coord = tmp1_1[0][0]['_XY_down_left']

        ## Approaching_coord: _XY_type2
        tmp1 = self.get_param_KJH4('SRF_NMOS', 'BND_Gate_Hrz_Mx')
        tmp2 = self.get_param_KJH4('SRF_PMOS', 'BND_Gate_Hrz_Mx')

        if tmp2[0][0][0]['_XY_left'][0] > tmp1[0][0][0]['_XY_left'][0]:
            tmp2 = self.get_param_KJH4('BND_Input_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_up_left']

        else:
            tmp2 = self.get_param_KJH4('BND_Input_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_down_left']

        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Input_Vtc_M1')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Input_Vtc_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########   IN/OUT : Out
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## IN/OUT : Out : Hrz M2
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Out_Hrz_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_NMOS', 'BND_Drain_Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_PMOS', 'BND_Drain_Hrz_M2')
        self._DesignParameter['BND_Out_Hrz_M2']['_XWidth'] = abs( tmp2[0][0][0]['_XY_right'][0] - tmp1[0][0][0]['_XY_right'][0])

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Out_Hrz_M2']['_YWidth'] = 50

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Out_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Out_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_NMOS', 'BND_Drain_Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_PMOS', 'BND_Drain_Hrz_M2')

        if tmp2[0][0][0]['_XY_right'][0] < tmp1[0][0][0]['_XY_right'][0]:
            tmp1_1 = self.get_param_KJH4('SRF_PMOS', 'BND_Drain_Hrz_M2')
            target_coord = tmp1_1[0][0][0]['_XY_down_right']
        else:
            tmp1_1 = self.get_param_KJH4('SRF_NMOS', 'BND_Drain_Hrz_M2')
            target_coord = tmp1_1[0][0][0]['_XY_down_right']

        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Out_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Out_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Out_Hrz_M2']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## IN/OUT : Out : Vtc M2
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Out_Vtc_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Out_Vtc_M3']['_XWidth'] = 50

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_NMOS', 'BND_Drain_Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_PMOS', 'BND_Drain_Hrz_M2')
        self._DesignParameter['BND_Out_Vtc_M3']['_YWidth'] = abs( tmp2[0][0][0]['_XY_up'][1] - tmp1[0][0][0]['_XY_down'][1] )

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Out_Vtc_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Out_Vtc_M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_NMOS', 'BND_Drain_Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_PMOS', 'BND_Drain_Hrz_M2')

        if tmp2[0][0][0]['_XY_right'][0] < tmp1[0][0][0]['_XY_right'][0]:
            tmp1_1 = self.get_param_KJH4('BND_Out_Hrz_M2')
            target_coord = tmp1_1[0][0]['_XY_up_right']
        else:
            tmp1_1 = self.get_param_KJH4('BND_Out_Hrz_M2')
            target_coord = tmp1_1[0][0]['_XY_down_right']

        ## Approaching_coord: _XY_type2
        tmp1 = self.get_param_KJH4('SRF_NMOS', 'BND_Drain_Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_PMOS', 'BND_Drain_Hrz_M2')

        if tmp2[0][0][0]['_XY_right'][0] < tmp1[0][0][0]['_XY_right'][0]:
            tmp1_1 = self.get_param_KJH4('BND_Out_Vtc_M3')
            approaching_coord = tmp1_1[0][0]['_XY_up_right']
        else:
            tmp1_1 = self.get_param_KJH4('BND_Out_Vtc_M3')
            approaching_coord = tmp1_1[0][0]['_XY_down_right']

        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Out_Vtc_M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Out_Vtc_M3']['_XYCoordinates'] = tmpXY


        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

            ## Sref ViaX declaration
        self._DesignParameter['SRF_OutputViaM2M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_OutputViaM2M3'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_OutputViaM2M3']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_OutputViaM2M3']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_OutputViaM2M3']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_OutputViaM2M3']['_XYCoordinates'] = [[0, 0]]
                ## Calculate1
                    ## Target_coord
        tmp1 = self.get_param_KJH4('BND_Out_Vtc_M3')
        target_coord = tmp1[0][0]['_XY_down']
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_OutputViaM2M3','SRF_ViaM2M3','BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_OutputViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

                ## Calculate2
                    ## Target_coord
        tmp1 = self.get_param_KJH4('BND_Out_Vtc_M3')
        target_coord = tmp1[0][0]['_XY_up']
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_OutputViaM2M3','SRF_ViaM2M3','BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_OutputViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_OutputViaM2M3']['_XYCoordinates'] = tmpXY













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
    libname = 'Proj_ADC_F00_SARLogic_Inverter'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'D00_00_Inverter_v2_92'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

    # NMosfet
        # PMOS/NMOS
        _NMOS_MosType                   = 'NMOS',   # 'NMOS'/'PMOS'
        # MOS Up/Dn
        _NMOS_MosUpDn                   = 'Up',     # 'Up'/'Dn'
        # Physical dimension
        _NMOS_NumberofGate	            = 1,        # Number
        _NMOS_ChannelWidth	            = 400,      # Number
        _NMOS_ChannelLength	            = 30,       # Number
        _NMOS_GateSpacing		        = None,     # None/Number
        _NMOS_SDWidth			        = None,     # None/Number
        _NMOS_XVT				        = 'SLVT',   # 'XVT' ex)SLVT/LVT/RVT/HVT
        _NMOS_PCCrit				    = True,     # None/True
        # Source_node setting
            # Via setting
        _NMOS_Source_Via_TF              = False,     # True/False
                # Via close to POpin
        _NMOS_Source_Via_Close2POpin_TF  = False,     # True/False
            # Comb setting: If Via is True
        _NMOS_Source_Comb_TF             = False,     # True/False
                # Comb POPinward
        _NMOS_Source_Comb_POpinward_TF   = False,     # True/False
                # Comb vertical_length
        _NMOS_Source_Comb_Length         = None,     # None/Number

        # Drain_node_setting
            # Via setting
        _NMOS_Drain_Via_TF               = True,     # True/False
                # Via close to POpin
        _NMOS_Drain_Via_Close2POpin_TF   = True,     # True/False
            # Comb setting: If Via is True
        _NMOS_Drain_Comb_TF              = True,     # True/False
                # Comb POPinward
        _NMOS_Drain_Comb_POpinward_TF    = True,     # True/False
                # Comb vertical_length
        _NMOS_Drain_Comb_Length          = 0,     # None/Number

        # POLY dummy setting
        _NMOS_PODummy_TF                 = True,  # TF
            # if _NMOSDummy == True
        _NMOS_PODummy_Length             = None,  # None/Value
        _NMOS_PODummy_Placement          = None,  # None/'Up'/'Dn'/

        # XVT setting
            # XVT setting : Exten XVT area if area is min
        _NMOS_Xvt_MinExten_TF            = True,     # True/False
            # XVT setting : None(Cent), Up, Dn
        _NMOS_Xvt_Placement              = 'Up',     # None/'Up'/'Dn'/

        # Poly Gate setting
        _NMOS_POGate_Comb_TF             = True,     # True/False
            # Poly Gate setting : vertical length
        _NMOS_POGate_Comb_length         = 100,     # None/Number
            # Poly Gate Via setting
        _NMOS_POGate_Via_TF              = True,     # None/'Up'/'Dn'/
            # Poly Gate Via setting :
        _NMOS_POGate_ViaMxMx             = [0 ,1],     # Ex) [1,5] -> ViaM1M5

    # PMosfet
        # PMOS/NMOS
        _PMOS_MosType                   = 'PMOS',   # 'NMOS'/'PMOS'
        # MOS Up/Dn
        _PMOS_MosUpDn                   = 'Dn',     # 'Up'/'Dn'
        # Physical dimension
        _PMOS_NumberofGate	            = 1,        # Number
        _PMOS_ChannelWidth	            = 800,      # Number
        _PMOS_ChannelLength	            = 30,       # Number
        _PMOS_GateSpacing		        = None,     # None/Number
        _PMOS_SDWidth			        = None,     # None/Number
        _PMOS_XVT				        = 'SLVT',   # 'XVT' ex)SLVT/LVT/RVT/HVT
        _PMOS_PCCrit				    = True,     # None/True
        # Source_node setting
            # Via setting
        _PMOS_Source_Via_TF              = False,     # True/False
                # Via close to POpin
        _PMOS_Source_Via_Close2POpin_TF  = False,     # True/False
            # Comb setting: If Via is True
        _PMOS_Source_Comb_TF             = False,     # True/False
                # Comb POPinward
        _PMOS_Source_Comb_POpinward_TF   = False,     # True/False
                # Comb vertical_length
        _PMOS_Source_Comb_Length         = None,     # None/Number

        # Drain_node_setting
            # Via setting
        _PMOS_Drain_Via_TF               = True,     # True/False
                # Via close to POpin
        _PMOS_Drain_Via_Close2POpin_TF   = True,     # True/False
            # Comb setting: If Via is True
        _PMOS_Drain_Comb_TF              = True,     # True/False
                # Comb POPinward
        _PMOS_Drain_Comb_POpinward_TF    = True,     # True/False
                # Comb vertical_length
        _PMOS_Drain_Comb_Length          = 0,       # None/Number

        # POLY dummy setting
        _PMOS_PODummy_TF                 = True,    # TF
            # if _PMOSDummy == True
        _PMOS_PODummy_Length             = None,  # None/Value
        _PMOS_PODummy_Placement          = None,  # None/'Up'/'Dn'/

        # XVT setting
            # XVT setting : Exten XVT area if area is min
        _PMOS_Xvt_MinExten_TF            = True,     # True/False
            # XVT setting : None(Cent), Up, Dn
        _PMOS_Xvt_Placement              = 'Dn',     # None/'Up'/'Dn'/

        # Poly Gate setting
        _PMOS_POGate_Comb_TF             = True,     # True/False
            # Poly Gate setting : vertical length
        _PMOS_POGate_Comb_length         = 100,     # None/Number
            # Poly Gate Via setting
        _PMOS_POGate_Via_TF              = True,     # None/'Up'/'Dn'/
            # Poly Gate Via setting :
        _PMOS_POGate_ViaMxMx             = [0 ,1],     # Ex) [1,5] -> ViaM1M5


    # Pbody
    _NMOS_Pbody_NumCont         = 3,  # Number
    _NMOS_Pbody_XvtTop2Pbody    = None,  # Number/None(Minimum)

    # Nbody
    _PMOS_Nbody_NumCont         = 3,  # Number
    _PMOS_Nbody_Xvtdown2Nbody   = None,  # Number/None(Minimum)

    # PMOS and NMOS Height
    _PMOSXvt2NMOSXvt            =1000,                  # number
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
    LayoutObj = _Inverter(_DesignParameter=None, _Name=cellname)
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
