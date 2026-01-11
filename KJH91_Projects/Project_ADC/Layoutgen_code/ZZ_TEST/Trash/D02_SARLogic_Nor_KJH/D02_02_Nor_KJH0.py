
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
from KJH91_Projects.Project_ADC.Layoutgen_code.ZZ_TEST.Trash.D02_SARLogic_Nor_KJH import D02_01_Pullup_KJH0, \
    D02_00_Pulldown_KJH0


## Define Class
class _Nor(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(

        # NMOSA
        _NMOSA_NMOSNumberofGate=1,  # number
        _NMOSA_NMOSChannelWidth=700,  # number
        _NMOSA_NMOSChannellength=30,  # number
        _NMOSA_GateSpacing=None,  # None/number
        _NMOSA_SDWidth=None,  # None/number
        _NMOSA_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _NMOSA_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _NMOSA_Source_Via_TF=False,  # True/False

        # Drain_node_ViaM1M2
        _NMOSA_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _NMOSA_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _NMOSA_NMOSDummy_length=None,  # None/Value
        _NMOSA_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # NMOSB
        _NMOSB_NMOSNumberofGate=1,  # number
        _NMOSB_NMOSChannelWidth=200,  # number
        _NMOSB_NMOSChannellength=30,  # number
        _NMOSB_GateSpacing=None,  # None/number
        _NMOSB_SDWidth=None,  # None/number
        _NMOSB_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _NMOSB_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _NMOSB_Source_Via_TF=False,  # True/False

        # Drain_node_ViaM1M2
        _NMOSB_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _NMOSB_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _NMOSB_NMOSDummy_length=None,  # None/Value
        _NMOSB_NMOSDummy_placement='Up',  # None/'Up'/'Dn'/

        # NMOSAB Pbody
        _NMOSAB_Pbody_NumCont=3,  # Number
        _NMOSAB_Pbody_XlvtTop2Pdoby=None,  # Number/None(Minimum)



        # PMOSA
        _PMOSA_PMOSNumberofGate=4,  # number
        _PMOSA_PMOSChannelWidth=700,  # number
        _PMOSA_PMOSChannellength=30,  # number
        _PMOSA_GateSpacing=None,  # None/number
        _PMOSA_SDWidth=None,  # None/number
        _PMOSA_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _PMOSA_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _PMOSA_Source_Via_TF=False,  # True/False

        # Drain_node_ViaM1M2
        _PMOSA_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _PMOSA_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _PMOSA_PMOSDummy_length=None,  # None/Value
        _PMOSA_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # PMOSB
        _PMOSB_PMOSNumberofGate=4,  # number
        _PMOSB_PMOSChannelWidth=200,  # number
        _PMOSB_PMOSChannellength=30,  # number
        _PMOSB_GateSpacing=None,  # None/number
        _PMOSB_SDWidth=None,  # None/number
        _PMOSB_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _PMOSB_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _PMOSB_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _PMOSB_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _PMOSB_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _PMOSB_PMOSDummy_length=None,  # None/Value
        _PMOSB_PMOSDummy_placement='Up',  # None/'Up'/'Dn'/

        # Nbody
        _PMOSAB_Nbody_NumCont=2,  # Number
        _PMOSAB_Nbody_Xlvtdown2Ndoby=None,  # Number/None(Minimum)

        # PMOS and NMOS Height
        _PMOSXvt2NMOSXvt=1000,  # number

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

                                  # NMOSA
                                  _NMOSA_NMOSNumberofGate=1,  # number
                                  _NMOSA_NMOSChannelWidth=700,  # number
                                  _NMOSA_NMOSChannellength=30,  # number
                                  _NMOSA_GateSpacing=None,  # None/number
                                  _NMOSA_SDWidth=None,  # None/number
                                  _NMOSA_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _NMOSA_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _NMOSA_Source_Via_TF=False,  # True/False

                                  # Drain_node_ViaM1M2
                                  _NMOSA_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _NMOSA_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _NMOSA_NMOSDummy_length=None,  # None/Value
                                  _NMOSA_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # NMOSB
                                  _NMOSB_NMOSNumberofGate=1,  # number
                                  _NMOSB_NMOSChannelWidth=200,  # number
                                  _NMOSB_NMOSChannellength=30,  # number
                                  _NMOSB_GateSpacing=None,  # None/number
                                  _NMOSB_SDWidth=None,  # None/number
                                  _NMOSB_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _NMOSB_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _NMOSB_Source_Via_TF=False,  # True/False

                                  # Drain_node_ViaM1M2
                                  _NMOSB_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _NMOSB_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _NMOSB_NMOSDummy_length=None,  # None/Value
                                  _NMOSB_NMOSDummy_placement='Up',  # None/'Up'/'Dn'/

                                  # NMOSAB Pbody
                                  _NMOSAB_Pbody_NumCont=3,  # Number
                                  _NMOSAB_Pbody_XlvtTop2Pdoby=None,  # Number/None(Minimum)



                                  # PMOSA
                                  _PMOSA_PMOSNumberofGate=4,  # number
                                  _PMOSA_PMOSChannelWidth=700,  # number
                                  _PMOSA_PMOSChannellength=30,  # number
                                  _PMOSA_GateSpacing=None,  # None/number
                                  _PMOSA_SDWidth=None,  # None/number
                                  _PMOSA_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _PMOSA_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _PMOSA_Source_Via_TF=False,  # True/False

                                  # Drain_node_ViaM1M2
                                  _PMOSA_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _PMOSA_PMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _PMOSA_PMOSDummy_length=None,  # None/Value
                                  _PMOSA_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # PMOSB
                                  _PMOSB_PMOSNumberofGate=4,  # number
                                  _PMOSB_PMOSChannelWidth=200,  # number
                                  _PMOSB_PMOSChannellength=30,  # number
                                  _PMOSB_GateSpacing=None,  # None/number
                                  _PMOSB_SDWidth=None,  # None/number
                                  _PMOSB_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _PMOSB_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _PMOSB_Source_Via_TF=True,  # True/False

                                  # Drain_node_ViaM1M2
                                  _PMOSB_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _PMOSB_PMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _PMOSB_PMOSDummy_length=None,  # None/Value
                                  _PMOSB_PMOSDummy_placement='Up',  # None/'Up'/'Dn'/

                                  # Nbody
                                  _PMOSAB_Nbody_NumCont=2,  # Number
                                  _PMOSAB_Nbody_Xlvtdown2Ndoby=None,  # Number/None(Minimum)



                                  # PMOS and NMOS Height
                                  _PMOSXvt2NMOSXvt=1000,  # number

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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Pulldown Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_PMOSA_power_v2._PMOSA_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D02_00_Pulldown_KJH0._Pulldown._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_PMOSAPOWER_PbodyContact_1_Length']  = _PMOSAPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOSA_NMOSNumberofGate']     = _NMOSA_NMOSNumberofGate
        _Caculation_Parameters['_NMOSA_NMOSChannelWidth']     = _NMOSA_NMOSChannelWidth
        _Caculation_Parameters['_NMOSA_NMOSChannellength']    = _NMOSA_NMOSChannellength
        _Caculation_Parameters['_NMOSA_GateSpacing']          = _NMOSA_GateSpacing
        _Caculation_Parameters['_NMOSA_SDWidth']              = _NMOSA_SDWidth
        _Caculation_Parameters['_NMOSA_XVT']                  = _NMOSA_XVT
        _Caculation_Parameters['_NMOSA_PCCrit']               = _NMOSA_PCCrit
        _Caculation_Parameters['_NMOSA_Source_Via_TF']        = _NMOSA_Source_Via_TF
        _Caculation_Parameters['_NMOSA_Drain_Via_TF']         = _NMOSA_Drain_Via_TF
        _Caculation_Parameters['_NMOSA_NMOSDummy']            = _NMOSA_NMOSDummy
        _Caculation_Parameters['_NMOSA_NMOSDummy_length']     = _NMOSA_NMOSDummy_length
        _Caculation_Parameters['_NMOSA_NMOSDummy_placement']  = _NMOSA_NMOSDummy_placement

        _Caculation_Parameters['_NMOSB_NMOSNumberofGate']     = _NMOSB_NMOSNumberofGate
        _Caculation_Parameters['_NMOSB_NMOSChannelWidth']     = _NMOSB_NMOSChannelWidth
        _Caculation_Parameters['_NMOSB_NMOSChannellength']    = _NMOSB_NMOSChannellength
        _Caculation_Parameters['_NMOSB_GateSpacing']          = _NMOSB_GateSpacing
        _Caculation_Parameters['_NMOSB_SDWidth']              = _NMOSB_SDWidth
        _Caculation_Parameters['_NMOSB_XVT']                  = _NMOSB_XVT
        _Caculation_Parameters['_NMOSB_PCCrit']               = _NMOSB_PCCrit
        _Caculation_Parameters['_NMOSB_Source_Via_TF']        = _NMOSB_Source_Via_TF
        _Caculation_Parameters['_NMOSB_Drain_Via_TF']         = _NMOSB_Drain_Via_TF
        _Caculation_Parameters['_NMOSB_NMOSDummy']            = _NMOSB_NMOSDummy
        _Caculation_Parameters['_NMOSB_NMOSDummy_length']     = _NMOSB_NMOSDummy_length
        _Caculation_Parameters['_NMOSB_NMOSDummy_placement']  = _NMOSB_NMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_PMOSA_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_PMOSA_power_v2._PMOSA_POWER( _DesignParameter=None, _Name='{}:PMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Pulldown'] = self._SrefElementDeclaration(_DesignObj=D02_00_Pulldown_KJH0._Pulldown(_DesignParameter=None, _Name='{}:SRF_Pulldown'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_PMOSA_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Pulldown']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_Pulldown']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_Pulldown']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_Pulldown']['_XYCoordinates'] = [[0, 0]]



        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Pullup Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_PMOSA_power_v2._PMOSA_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D02_01_Pullup_KJH0._Pullup._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_PMOSAPOWER_PbodyContact_1_Length']  = _PMOSAPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_PMOSA_PMOSNumberofGate']     = _PMOSA_PMOSNumberofGate
        _Caculation_Parameters['_PMOSA_PMOSChannelWidth']     = _PMOSA_PMOSChannelWidth
        _Caculation_Parameters['_PMOSA_PMOSChannellength']    = _PMOSA_PMOSChannellength
        _Caculation_Parameters['_PMOSA_GateSpacing']          = _PMOSA_GateSpacing
        _Caculation_Parameters['_PMOSA_SDWidth']              = _PMOSA_SDWidth
        _Caculation_Parameters['_PMOSA_XVT']                  = _PMOSA_XVT
        _Caculation_Parameters['_PMOSA_PCCrit']               = _PMOSA_PCCrit
        _Caculation_Parameters['_PMOSA_Source_Via_TF']        = _PMOSA_Source_Via_TF
        _Caculation_Parameters['_PMOSA_Drain_Via_TF']         = _PMOSA_Drain_Via_TF
        _Caculation_Parameters['_PMOSA_PMOSDummy']            = _PMOSA_PMOSDummy
        _Caculation_Parameters['_PMOSA_PMOSDummy_length']     = _PMOSA_PMOSDummy_length
        _Caculation_Parameters['_PMOSA_PMOSDummy_placement']  = _PMOSA_PMOSDummy_placement

        _Caculation_Parameters['_PMOSB_PMOSNumberofGate']     = _PMOSB_PMOSNumberofGate
        _Caculation_Parameters['_PMOSB_PMOSChannelWidth']     = _PMOSB_PMOSChannelWidth
        _Caculation_Parameters['_PMOSB_PMOSChannellength']    = _PMOSB_PMOSChannellength
        _Caculation_Parameters['_PMOSB_GateSpacing']          = _PMOSB_GateSpacing
        _Caculation_Parameters['_PMOSB_SDWidth']              = _PMOSB_SDWidth
        _Caculation_Parameters['_PMOSB_XVT']                  = _PMOSB_XVT
        _Caculation_Parameters['_PMOSB_PCCrit']               = _PMOSB_PCCrit
        _Caculation_Parameters['_PMOSB_Source_Via_TF']        = _PMOSB_Source_Via_TF
        _Caculation_Parameters['_PMOSB_Drain_Via_TF']         = _PMOSB_Drain_Via_TF
        _Caculation_Parameters['_PMOSB_PMOSDummy']            = _PMOSB_PMOSDummy
        _Caculation_Parameters['_PMOSB_PMOSDummy_length']     = _PMOSB_PMOSDummy_length
        _Caculation_Parameters['_PMOSB_PMOSDummy_placement']  = _PMOSB_PMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_PMOSA_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_PMOSA_power_v2._PMOSA_POWER( _DesignParameter=None, _Name='{}:PMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Pullup'] = self._SrefElementDeclaration(_DesignObj=D02_01_Pullup_KJH0._Pullup(_DesignParameter=None, _Name='{}:SRF_Pullup'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_PMOSA_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Pullup']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_Pullup']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_Pullup']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_Pullup']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Pullup']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ## X
        tmp1_1 = self.get_outter_KJH4('SRF_Pulldown')
        target_coordx = np.round(0.5*(tmp1_1['_Mostright']['coord'][0] + tmp1_1['_Mostleft']['coord'][0]))
                                ## Y
        tmp1_2 = self.get_param_KJH4('SRF_Pulldown','SRF_NMOSA','BND_{}Layer'.format(_NMOSA_XVT))
        target_coordy = tmp1_2[0][0][0][0]['_XY_up'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ## X
        tmp2_1 = self.get_outter_KJH4('SRF_Pullup')
        approaching_coordx = np.round (0.5*(tmp2_1['_Mostright']['coord'][0] + tmp2_1['_Mostleft']['coord'][0]))
                                ## Y
        tmp2 = self.get_param_KJH4('SRF_Pullup','SRF_PMOSA','BND_{}Layer'.format(_PMOSA_XVT))
        approaching_coordy = tmp2[0][0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pullup')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[1] = New_Scoord[1] + _PMOSXvt2NMOSXvt
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Pullup']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS Pbody
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS Pbody : Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A08_PbodyContactPhyLen_KJH2._PbodyContactPhyLen_KJH2._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length'] = None
        _Caculation_Parameters['_NumCont'] = _NMOSAB_Pbody_NumCont
        _Caculation_Parameters['_Vtc_flag'] = False

        ## Calculate '_Length'
        tmp = self.get_outter_KJH4('SRF_Pulldown')
        _Caculation_Parameters['_Length'] = abs(tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0])

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Pbody'] = self._SrefElementDeclaration( _DesignObj=A08_PbodyContactPhyLen_KJH2._PbodyContactPhyLen_KJH2(_DesignParameter=None,
                                                                           _Name='{}:SRF_Pbody'.format(_Name)))[0]

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

        if _NMOSAB_Pbody_XlvtTop2Pdoby == None:
            ## Calculate
            ## Target_coord: _XY_type1
            ## X
            tmp1_1 = self.get_param_KJH4('SRF_Pulldown', 'SRF_NMOSA', 'BND_{}Layer'.format(_NMOSA_XVT))
            target_coordx = tmp1_1[0][0][0][0]['_XY_left'][0]
            ## Y
            tmp1_2 = self.get_outter_KJH4('SRF_Pulldown')
            target_coordy = tmp1_2['_Mostdown']['coord'][0]

            target_coord = [target_coordx, target_coordy]
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Pbody')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[1] = New_Scoord[1] - 50
            tmpXY.append(New_Scoord)
            ## Define Coordinates
            self._DesignParameter['SRF_Pbody']['_XYCoordinates'] = tmpXY

        else:
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Pulldown', 'SRF_NMOSA', 'BND_{}Layer'.format(_NMOSA_XVT))
            target_coord = tmp1[0][0][0][0]['_XY_up_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Pbody')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[1] = New_Scoord[1] - _NMOSAB_Pbody_XlvtTop2Pdoby
            tmpXY.append(New_Scoord)
            ## Define Coordinates
            self._DesignParameter['SRF_Pbody']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS Pbody : NMOSA source and Pbody connection
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NMOSA_Source_Vtc_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth : ViaYmin 기준
        tmp1 = self.get_param_KJH4('SRF_Pulldown', 'SRF_NMOSA', 'BND_Met1Layer_Source')
        tmp2 = self.get_param_KJH4('SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        self._DesignParameter['BND_NMOSA_Source_Vtc_M1']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_down'][1] - tmp2[0][0][0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Pulldown', 'SRF_NMOSA', 'BND_Met1Layer_Source')
        self._DesignParameter['BND_NMOSA_Source_Vtc_M1']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NMOSA_Source_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        tmp = self.get_param_KJH4('SRF_Pulldown', 'SRF_NMOSA', 'BND_Met1Layer_Source')
        for i in range(0, len(tmp[0][0])):
            ## Calculate Sref XYcoord
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Pulldown', 'SRF_NMOSA', 'BND_Met1Layer_Source')
            target_coord = tmp1[0][0][i][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_NMOSA_Source_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_up_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_NMOSA_Source_Vtc_M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_NMOSA_Source_Vtc_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS Pbody : NMOSB source and Pbody connection
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NMOSB_Source_Vtc_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth : ViaYmin 기준
        tmp1 = self.get_param_KJH4('SRF_Pulldown', 'SRF_NMOSB', 'BND_Met1Layer_Source')
        tmp2 = self.get_param_KJH4('SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        self._DesignParameter['BND_NMOSB_Source_Vtc_M1']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_down'][1] - tmp2[0][0][0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Pulldown', 'SRF_NMOSB', 'BND_Met1Layer_Source')
        self._DesignParameter['BND_NMOSB_Source_Vtc_M1']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NMOSB_Source_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        tmp = self.get_param_KJH4('SRF_Pulldown', 'SRF_NMOSB', 'BND_Met1Layer_Source')
        for i in range(0, len(tmp[0][0])):
            ## Calculate Sref XYcoord
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Pulldown', 'SRF_NMOSB', 'BND_Met1Layer_Source')
            target_coord = tmp1[0][0][i][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_NMOSB_Source_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_up_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_NMOSB_Source_Vtc_M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_NMOSB_Source_Vtc_M1']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS Nbody
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  PMOS Nbody: Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A07_NbodyContactPhyLen_KJH2._NbodyContactPhyLen_KJH2._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length']      = None
        _Caculation_Parameters['_NumCont']     = _PMOSAB_Nbody_NumCont
        _Caculation_Parameters['_Vtc_flag']    = False

        ## Calculate '_Length'
        tmp = self.get_outter_KJH4('SRF_Pullup')
        _Caculation_Parameters['_Length']      = abs(tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0])

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Nbody'] = self._SrefElementDeclaration(_DesignObj=A07_NbodyContactPhyLen_KJH2._NbodyContactPhyLen_KJH2(_DesignParameter=None, _Name='{}:SRF_Nbody'.format(_Name)))[0]

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

        if _PMOSAB_Nbody_Xlvtdown2Ndoby == None:
                            ## Calculate
                                ## Target_coord: _XY_type1
                                    ## X
            tmp1_1 = self.get_param_KJH4('SRF_Pullup', 'SRF_PMOSA', 'BND_{}Layer'.format(_PMOSA_XVT))
            target_coordx = tmp1_1[0][0][0][0]['_XY_left'][0]
                                    ## Y
            tmp1_2 = self.get_outter_KJH4('SRF_Pullup')
            target_coordy = tmp1_2['_Mostup']['coord'][0]

            target_coord = [target_coordx,target_coordy]
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_down_left']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Nbody')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[1] = New_Scoord[1] + 50
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_Nbody']['_XYCoordinates'] = tmpXY

        else:
                            ## Calculate
                                ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Pullup','SRF_PMOSA','BND_{}Layer'.format(_PMOSA_XVT))
            target_coord = tmp1[0][0][0][0]['_XY_down_left']
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_down_left']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Nbody')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[1] = New_Scoord[1] + _PMOSAB_Nbody_Xlvtdown2Ndoby
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_Nbody']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS Pbody : PMOSA source and Nbody connection
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOSA_Source_Vtc_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth : ViaYmin 기준
        tmp1 = self.get_param_KJH4('SRF_Pullup','SRF_PMOSA','BND_Met1Layer_Source')
        tmp2 = self.get_param_KJH4('SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_PMOSA_Source_Vtc_M1']['_YWidth'] = abs (tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1])

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Pullup','SRF_PMOSA','BND_Met1Layer_Source')
        self._DesignParameter['BND_PMOSA_Source_Vtc_M1']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOSA_Source_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        tmp = self.get_param_KJH4('SRF_Pullup','SRF_PMOSA','BND_Met1Layer_Source')
        for i in range(0,len(tmp[0][0])):
            ## Calculate Sref XYcoord
                ## Calculate
                    ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Pullup','SRF_PMOSA','BND_Met1Layer_Source')
            target_coord = tmp1[0][0][i][0]['_XY_up_left']
                    ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_PMOSA_Source_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_down_left']
                    ## Sref coord
            tmp3 = self.get_param_KJH4('BND_PMOSA_Source_Vtc_M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_PMOSA_Source_Vtc_M1']['_XYCoordinates'] = tmpXY




        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  PMOS: NWELL Exten
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOSAB_NellExten'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Nbody','SRF_NbodyContactPhyLen','BND_Nwell')
        tmp2 = self.get_param_KJH4('SRF_Pullup','SRF_PMOSA','BND_{}Layer'.format(_PMOSA_XVT))
        self._DesignParameter['BND_PMOSAB_NellExten']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] )

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Nbody','SRF_NbodyContactPhyLen','BND_Nwell')
        self._DesignParameter['BND_PMOSAB_NellExten']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOSAB_NellExten']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
            ## initialized Sref coordinate
        self._DesignParameter['BND_PMOSAB_NellExten']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
                ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Nbody','SRF_NbodyContactPhyLen','BND_Nwell')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
                ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOSAB_NellExten')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOSAB_NellExten')
        Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_PMOSAB_NellExten']['_XYCoordinates'] = tmpXY



        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  IN/OUT
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########   IN/OUT : InputA
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## IN/OUT : InputA : Hrz M1
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_InputA_Hrz_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Pulldown', 'BND_NMOSA_Gate_Hrz_M1')
        tmp2 = self.get_param_KJH4('SRF_Pullup', 'BND_PMOSA_Gate_Hrz_M1')
        self._DesignParameter['BND_InputA_Hrz_M1']['_XWidth'] = abs( tmp2[0][0][0]['_XY_left'][0] - tmp1[0][0][0]['_XY_left'][0])

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_InputA_Hrz_M1']['_YWidth'] = 50

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_InputA_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_InputA_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Pulldown', 'BND_NMOSA_Gate_Hrz_M1')
        tmp2 = self.get_param_KJH4('SRF_Pullup', 'BND_PMOSA_Gate_Hrz_M1')

        if tmp2[0][0][0]['_XY_left'][0] > tmp1[0][0][0]['_XY_left'][0]:
            tmp1_1 = self.get_param_KJH4('SRF_Pullup', 'BND_PMOSA_Gate_Hrz_M1')
            target_coord = tmp1_1[0][0][0]['_XY_down_left']
        else:
            tmp1_1 = self.get_param_KJH4('SRF_Pulldown', 'BND_NMOSA_Gate_Hrz_M1')
            target_coord = tmp1_1[0][0][0]['_XY_down_left']

        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_InputA_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_down_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_InputA_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_InputA_Hrz_M1']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## IN/OUT : InputA : Vtc M1
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_InputA_Vtc_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Pulldown', 'BND_NMOSA_Gate_Hrz_M1')
        tmp2 = self.get_param_KJH4('SRF_Pullup', 'BND_PMOSA_Gate_Hrz_M1')
        self._DesignParameter['BND_InputA_Vtc_M1']['_YWidth'] = abs( tmp2[0][0][0]['_XY_up'][1] - tmp1[0][0][0]['_XY_down'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_InputA_Vtc_M1']['_XWidth'] = 50

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_InputA_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_InputA_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Pulldown', 'BND_NMOSA_Gate_Hrz_M1')
        tmp2 = self.get_param_KJH4('SRF_Pullup', 'BND_PMOSA_Gate_Hrz_M1')

        if tmp2[0][0][0]['_XY_left'][0] > tmp1[0][0][0]['_XY_left'][0]:
            tmp1_1 = self.get_param_KJH4('BND_InputA_Hrz_M1')
            target_coord = tmp1_1[0][0]['_XY_up_left']

        else:
            tmp1_1 = self.get_param_KJH4('BND_InputA_Hrz_M1')
            target_coord = tmp1_1[0][0]['_XY_down_left']

        ## Approaching_coord: _XY_type2
        tmp1 = self.get_param_KJH4('SRF_Pulldown', 'BND_NMOSA_Gate_Hrz_M1')
        tmp2 = self.get_param_KJH4('SRF_Pullup', 'BND_PMOSA_Gate_Hrz_M1')

        if tmp2[0][0][0]['_XY_left'][0] > tmp1[0][0][0]['_XY_left'][0]:
            tmp2 = self.get_param_KJH4('BND_InputA_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_up_left']

        else:
            tmp2 = self.get_param_KJH4('BND_InputA_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_down_left']

        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_InputA_Vtc_M1')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_InputA_Vtc_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########   IN/OUT : InputB
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## IN/OUT : InputB : Hrz M1
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_InputB_Hrz_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Pulldown', 'BND_NMOSB_Gate_Hrz_M1')
        tmp2 = self.get_param_KJH4('SRF_Pullup', 'BND_PMOSB_Gate_Hrz_M1')
        self._DesignParameter['BND_InputB_Hrz_M1']['_XWidth'] = abs( tmp2[0][0][0]['_XY_right'][0] - tmp1[0][0][0]['_XY_right'][0])

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_InputB_Hrz_M1']['_YWidth'] = 50

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_InputB_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_InputB_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Pulldown', 'BND_NMOSB_Gate_Hrz_M1')
        tmp2 = self.get_param_KJH4('SRF_Pullup', 'BND_PMOSB_Gate_Hrz_M1')

        if tmp2[0][0][0]['_XY_right'][0] < tmp1[0][0][0]['_XY_right'][0]:
            tmp1_1 = self.get_param_KJH4('SRF_Pullup', 'BND_PMOSB_Gate_Hrz_M1')
            target_coord = tmp1_1[0][0][0]['_XY_down_right']
        else:
            tmp1_1 = self.get_param_KJH4('SRF_Pulldown', 'BND_NMOSB_Gate_Hrz_M1')
            target_coord = tmp1_1[0][0][0]['_XY_down_right']

        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_InputB_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_InputB_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_InputB_Hrz_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## IN/OUT : InputB : Vtc M1
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_InputB_Vtc_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Pulldown', 'BND_NMOSB_Gate_Hrz_M1')
        tmp2 = self.get_param_KJH4('SRF_Pullup', 'BND_PMOSB_Gate_Hrz_M1')
        self._DesignParameter['BND_InputB_Vtc_M1']['_YWidth'] = abs( tmp2[0][0][0]['_XY_up'][1] - tmp1[0][0][0]['_XY_down'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_InputB_Vtc_M1']['_XWidth'] = 50

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_InputB_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_InputB_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Pulldown', 'BND_NMOSB_Gate_Hrz_M1')
        tmp2 = self.get_param_KJH4('SRF_Pullup', 'BND_PMOSB_Gate_Hrz_M1')

        if tmp2[0][0][0]['_XY_right'][0] < tmp1[0][0][0]['_XY_right'][0]:
            tmp1_1 = self.get_param_KJH4('BND_InputB_Hrz_M1')
            target_coord = tmp1_1[0][0]['_XY_up_right']

        else:
            tmp1_1 = self.get_param_KJH4('BND_InputB_Hrz_M1')
            target_coord = tmp1_1[0][0]['_XY_down_right']

        ## Approaching_coord: _XY_type2
        tmp1 = self.get_param_KJH4('SRF_Pulldown', 'BND_NMOSB_Gate_Hrz_M1')
        tmp2 = self.get_param_KJH4('SRF_Pullup', 'BND_PMOSB_Gate_Hrz_M1')

        if tmp2[0][0][0]['_XY_right'][0] < tmp1[0][0][0]['_XY_right'][0]:
            tmp2 = self.get_param_KJH4('BND_InputB_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_up_right']

        else:
            tmp2 = self.get_param_KJH4('BND_InputB_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_down_right']

        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_InputB_Vtc_M1')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_InputB_Vtc_M1']['_XYCoordinates'] = tmpXY

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
        tmp1 = self.get_param_KJH4('SRF_Pulldown', 'BND_NMOSAB_Drain_Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_Pullup', 'BND_PMOSB_Drain_Hrz_M2')
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
        tmp1 = self.get_param_KJH4('SRF_Pulldown', 'BND_NMOSAB_Drain_Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_Pullup', 'BND_PMOSB_Drain_Hrz_M2')

        if tmp2[0][0][0]['_XY_right'][0] < tmp1[0][0][0]['_XY_right'][0]:
            tmp1_1 = self.get_param_KJH4('SRF_Pullup', 'BND_PMOSB_Drain_Hrz_M2')
            target_coord = tmp1_1[0][0][0]['_XY_down_right']
        else:
            tmp1_1 = self.get_param_KJH4('SRF_Pulldown', 'BND_NMOSAB_Drain_Hrz_M2')
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
        self._DesignParameter['BND_Out_Vtc_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Out_Vtc_M2']['_XWidth'] = 50

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Pulldown', 'BND_NMOSAB_Drain_Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_Pullup', 'BND_PMOSB_Drain_Hrz_M2')
        self._DesignParameter['BND_Out_Vtc_M2']['_YWidth'] = abs( tmp2[0][0][0]['_XY_up'][1] - tmp1[0][0][0]['_XY_down'][1] )

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Out_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Out_Vtc_M2']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Pulldown', 'BND_NMOSAB_Drain_Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_Pullup', 'BND_PMOSB_Drain_Hrz_M2')

        if tmp2[0][0][0]['_XY_right'][0] < tmp1[0][0][0]['_XY_right'][0]:
            tmp1_1 = self.get_param_KJH4('BND_Out_Hrz_M2')
            target_coord = tmp1_1[0][0]['_XY_up_right']
        else:
            tmp1_1 = self.get_param_KJH4('BND_Out_Hrz_M2')
            target_coord = tmp1_1[0][0]['_XY_down_right']

        ## Approaching_coord: _XY_type2
        tmp1 = self.get_param_KJH4('SRF_Pulldown', 'BND_NMOSAB_Drain_Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_Pullup', 'BND_PMOSB_Drain_Hrz_M2')

        if tmp2[0][0][0]['_XY_right'][0] < tmp1[0][0][0]['_XY_right'][0]:
            tmp1_1 = self.get_param_KJH4('BND_Out_Vtc_M2')
            approaching_coord = tmp1_1[0][0]['_XY_up_right']
        else:
            tmp1_1 = self.get_param_KJH4('BND_Out_Vtc_M2')
            approaching_coord = tmp1_1[0][0]['_XY_down_right']

        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Out_Vtc_M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Out_Vtc_M2']['_XYCoordinates'] = tmpXY

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
    libname = 'Proj_ADC_D02_SARLogic_Nor_KJH'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'D02_02_Nor_v0_82'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

        # NMOSA
        _NMOSA_NMOSNumberofGate=1,  # number
        _NMOSA_NMOSChannelWidth=700,  # number
        _NMOSA_NMOSChannellength=30,  # number
        _NMOSA_GateSpacing=None,  # None/number
        _NMOSA_SDWidth=None,  # None/number
        _NMOSA_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _NMOSA_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _NMOSA_Source_Via_TF=False,  # True/False

        # Drain_node_ViaM1M2
        _NMOSA_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _NMOSA_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _NMOSA_NMOSDummy_length=None,  # None/Value
        _NMOSA_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # NMOSB
        _NMOSB_NMOSNumberofGate=1,  # number
        _NMOSB_NMOSChannelWidth=200,  # number
        _NMOSB_NMOSChannellength=30,  # number
        _NMOSB_GateSpacing=None,  # None/number
        _NMOSB_SDWidth=None,  # None/number
        _NMOSB_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _NMOSB_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _NMOSB_Source_Via_TF=False,  # True/False

        # Drain_node_ViaM1M2
        _NMOSB_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _NMOSB_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _NMOSB_NMOSDummy_length=None,  # None/Value
        _NMOSB_NMOSDummy_placement='Up',  # None/'Up'/'Dn'/

        # NMOSAB Pbody
        _NMOSAB_Pbody_NumCont=3,  # Number
        _NMOSAB_Pbody_XlvtTop2Pdoby=None,  # Number/None(Minimum)




        # PMOSA
        _PMOSA_PMOSNumberofGate=4,  # number
        _PMOSA_PMOSChannelWidth=700,  # number
        _PMOSA_PMOSChannellength=30,  # number
        _PMOSA_GateSpacing=None,  # None/number
        _PMOSA_SDWidth=None,  # None/number
        _PMOSA_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _PMOSA_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _PMOSA_Source_Via_TF=False,  # True/False

        # Drain_node_ViaM1M2
        _PMOSA_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _PMOSA_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _PMOSA_PMOSDummy_length=None,  # None/Value
        _PMOSA_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # PMOSB
        _PMOSB_PMOSNumberofGate=4,  # number
        _PMOSB_PMOSChannelWidth=200,  # number
        _PMOSB_PMOSChannellength=30,  # number
        _PMOSB_GateSpacing=None,  # None/number
        _PMOSB_SDWidth=None,  # None/number
        _PMOSB_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _PMOSB_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _PMOSB_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _PMOSB_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _PMOSB_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _PMOSB_PMOSDummy_length=None,  # None/Value
        _PMOSB_PMOSDummy_placement='Up',  # None/'Up'/'Dn'/

        # Nbody
        _PMOSAB_Nbody_NumCont=2,  # Number
        _PMOSAB_Nbody_Xlvtdown2Ndoby=None,  # Number/None(Minimum)

        # PMOS and NMOS Height
        _PMOSXvt2NMOSXvt=1000,  # number

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
    LayoutObj = _Nor(_DesignParameter=None, _Name=cellname)
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
