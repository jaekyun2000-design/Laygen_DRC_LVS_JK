
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
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A03_NmosWithDummy_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A04_PmosWithDummy_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A05_NbodyContact_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A06_PbodyContact_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A07_NbodyContactPhyLen_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A08_PbodyContactPhyLen_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A09_NbodyRing_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A10_PbodyRing_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A11_NbodyContactforDeepNwell_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A12_NbodyContactPhyLenforDeepNwell_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A13_NbodyRingforDeepNwell_KJH

    ##
from KJH91_Projects.Project_ADC.Layoutgen_code.C09_Tr6_KJH import C09_00_Tr6


## Define Class
class _Guardring(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(

        # Tr6
        _Tr6_NMOSNumberofGate    =   6,     #number
        _Tr6_NMOSChannelWidth    =   1000,   #number
        _Tr6_NMOSChannellength   =   30,     #number
        _Tr6_GateSpacing         =   100,    #None/number
        _Tr6_SDWidth             =   None,   #None/number
        _Tr6_XVT                 =   'SLVT',  #'XVT' ex)SLVT LVT RVT HVT
        _Tr6_PCCrit              =   True,   #None/True

            # Source_node_ViaM1M2
        _Tr6_Source_Via_TF       =   False,  #True/False

            # Drain_node_ViaM1M2
        _Tr6_Drain_Via_TF        =   False,  #True/False

            # POLY dummy setting
        _Tr6_NMOSDummy           =   True,  # TF
                # if _PMOSDummy == True
        _Tr6_NMOSDummy_length    =   None,  # None/Value
        _Tr6_NMOSDummy_placement =   None,  # None/'Up'/'Dn'/

        # Vp node
        _Vp_node_width = 280, #Number
        _Vp_node_metal_Layer = 3, #number

        # Guardring
            # Pbody: number of contact
            # Nbody
        _NwellWidth=850,  # number

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

                                  # Tr6
                                  _Tr6_NMOSNumberofGate=6,  # number
                                  _Tr6_NMOSChannelWidth=1000,  # number
                                  _Tr6_NMOSChannellength=30,  # number
                                  _Tr6_GateSpacing=100,  # None/number
                                  _Tr6_SDWidth=None,  # None/number
                                  _Tr6_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Tr6_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _Tr6_Source_Via_TF=False,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Tr6_Drain_Via_TF=False,  # True/False

                                  # POLY dummy setting
                                  _Tr6_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tr6_NMOSDummy_length=None,  # None/Value
                                  _Tr6_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Vp node
                                  _Vp_node_width=280,  # Number
                                  _Vp_node_metal_Layer=3,  # number

                                  # Guardring
                                  # Pbody: number of contact
                                  # Nbody
                                  _NwellWidth=850,  # number

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


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr1, nfettw
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Tr1, nfettw: Sref Gen.
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C09_00_Tr6._Tr6._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr6_NMOSNumberofGate']     =   _Tr6_NMOSNumberofGate
        _Caculation_Parameters['_Tr6_NMOSChannelWidth']     =   _Tr6_NMOSChannelWidth
        _Caculation_Parameters['_Tr6_NMOSChannellength']    =   _Tr6_NMOSChannellength
        _Caculation_Parameters['_Tr6_GateSpacing']          =   _Tr6_GateSpacing
        _Caculation_Parameters['_Tr6_SDWidth']              =   _Tr6_SDWidth
        _Caculation_Parameters['_Tr6_XVT']                  =   _Tr6_XVT
        _Caculation_Parameters['_Tr6_PCCrit']               =   _Tr6_PCCrit
        _Caculation_Parameters['_Tr6_Source_Via_TF']        =   _Tr6_Source_Via_TF
        _Caculation_Parameters['_Tr6_Drain_Via_TF']         =   _Tr6_Drain_Via_TF
        _Caculation_Parameters['_Tr6_NMOSDummy']            =   _Tr6_NMOSDummy
        _Caculation_Parameters['_Tr6_NMOSDummy_length']     =   _Tr6_NMOSDummy_length
        _Caculation_Parameters['_Tr6_NMOSDummy_placement']  =   _Tr6_NMOSDummy_placement
        _Caculation_Parameters['_Vp_node_width']     =   _Vp_node_width
        _Caculation_Parameters['_Vp_node_metal_Layer']  =   _Vp_node_metal_Layer

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Tr6'] = self._SrefElementDeclaration(_DesignObj=C09_00_Tr6._Tr6(_DesignParameter=None, _Name='{}:SRF_Tr6'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Tr6']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr6']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr6']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr6']['_XYCoordinates'] = [[0, 0]]

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Guardring: Pbody
        ## Guardring
        ## Pre-defined DRC
        _right_margin = 250
        _left_margin = 180
        _up_margin = 100
        _down_margin = 300

        _NumCont = 2

        ## Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A10_PbodyRing_KJH3._PbodyRing._ParametersForDesignCalculation)
        _Caculation_Parameters['_XlengthIntn'] = None
        _Caculation_Parameters['_YlengthIntn'] = None
        _Caculation_Parameters['_NumContTop'] = _NumCont
        _Caculation_Parameters['_NumContBottom'] = _NumCont
        _Caculation_Parameters['_NumContLeft'] = _NumCont
        _Caculation_Parameters['_NumContRight'] = _NumCont

        ## Find Outter boundary
        tmp = self.get_outter_KJH4('SRF_Tr6')

        ## Define _XlengthIntn
        _Caculation_Parameters['_XlengthIntn'] = abs( tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0]) + _right_margin + _left_margin

        ## Define _YlengthIntn
        _Caculation_Parameters['_YlengthIntn'] = abs( tmp['_Mostup']['coord'][0] - tmp['_Mostdown']['coord'][0]) + _up_margin + _down_margin

        ## Generate Sref
        self._DesignParameter['SRF_Pbodyring'] = self._SrefElementDeclaration(
            _DesignObj=A10_PbodyRing_KJH3._PbodyRing(_DesignParameter=None,
            _Name='{}:SRF_Pbodyring'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_Pbodyring']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_Pbodyring']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_Pbodyring']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate
        self._DesignParameter['SRF_Pbodyring']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_Pbodyring']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        target_coord = [tmp['_Mostleft']['coord'][0], tmp['_Mostdown']['coord'][0]]
        ## Approaching_coord
        ## x
        tmp2_1 = self.get_param_KJH4('SRF_Pbodyring', 'SRF_PbodyLeft', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coordx = tmp2_1[0][0][0][0][0]['_XY_right'][0]
        ## y
        tmp2_2 = self.get_param_KJH4('SRF_Pbodyring', 'SRF_PbodyBottom', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coordy = tmp2_2[0][0][0][0][0]['_XY_up'][1]

        approaching_coord = [approaching_coordx, approaching_coordy]
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pbodyring')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] - _left_margin
        New_Scoord[1] = New_Scoord[1] - _down_margin
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_Pbodyring']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr6_Drain_Pbody_M1connect(Cbot)
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Tr6_Drain_Vtc_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Pbodyring', 'SRF_PbodyBottom', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_Tr6','SRF_Nmos','BND_Met1Layer_Drain')
        self._DesignParameter['BND_Tr6_Drain_Vtc_M1']['_YWidth'] = abs( tmp2[0][0][0][0]['_XY_down'][1] - tmp1[0][0][0][0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Tr6', 'SRF_Nmos', 'BND_Met1Layer_Drain')
        self._DesignParameter['BND_Tr6_Drain_Vtc_M1']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Tr6_Drain_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Tr6_Drain_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
        tmp = self.get_param_KJH4('SRF_Tr6', 'SRF_Nmos', 'BND_Met1Layer_Drain')
        for i in range(0, len(tmp[0][0])):
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Tr6', 'SRF_Nmos','BND_Met1Layer_Drain')
            target_coord = tmp1[0][0][i][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Tr6_Drain_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_up_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Tr6_Drain_Vtc_M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_Tr6_Drain_Vtc_M1']['_XYCoordinates'] = tmpXY


        # N Body Contact(M1, CA, RX) in Isolated PSub for GR135a
        ## SREF Generation
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(
            A07_NbodyContactPhyLen_KJH3._NbodyContactPhyLen._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length'] = None
        _Caculation_Parameters['_NumCont'] = 1
        _Caculation_Parameters['_Vtc_flag'] = False

        ## Cal length
        tmp1 = self.get_param_KJH4('SRF_Pbodyring', 'SRF_PbodyBottom', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        _Caculation_Parameters['_Length'] = tmp1[0][0][0][0][0]['_Xwidth']

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Nbody_withinPIsolated'] = self._SrefElementDeclaration(
            _DesignObj=A07_NbodyContactPhyLen_KJH3._NbodyContactPhyLen(_DesignParameter=None,
                                                                            _Name='{}:SRF_Nbody_withinPIsolated'.format(
                                                                                _Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Nbody_withinPIsolated']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nbody_withinPIsolated']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nbody_withinPIsolated']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Initialize Sref _XYcoordinate:
        self._DesignParameter['SRF_Nbody_withinPIsolated']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        ## Calculate
        ##y
        tmp1_1 = self.get_param_KJH4('SRF_Pbodyring', 'SRF_PbodyBottom', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        target_coord = tmp1_1[0][0][0][0][0]['_XY_down_left']

        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_Nbody_withinPIsolated', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_left']

        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Nbody_withinPIsolated')
        SpaceBtwPbodyRingNbodyContactInT3 = 400
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[1] = Scoord[1] - max(SpaceBtwPbodyRingNbodyContactInT3, _DRCobj._PpMinSpace)

        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define Coordinates
        self._DesignParameter['SRF_Nbody_withinPIsolated']['_XYCoordinates'] = tmpXY

        # T3 위에 RX CA M1 레이어만 까는거라서 NWell은 필요없음.
        del self._DesignParameter['SRF_Nbody_withinPIsolated']['_DesignObj']._DesignParameter['SRF_NbodyContactPhyLen'][
            '_DesignObj']._DesignParameter['BND_Nwell']


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Guardring(Nbody)
        ## Pre-defined
        _right_margin2   = 650
        _left_margin2    = 650
        _up_margin2      = 650
        _down_margin2    = 650
        _NumCont2 = 3

        ## Guardring
        ## Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A13_NbodyRingforDeepNwell_KJH._NbodyRingforDeepNwell_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_XlengthIntn']      = None
        _Caculation_Parameters['_YlengthIntn']      = None
        _Caculation_Parameters['_NumContTop']       = _NumCont2
        _Caculation_Parameters['_NumContBottom']    = _NumCont2
        _Caculation_Parameters['_NumContLeft']      = _NumCont2
        _Caculation_Parameters['_NumContRight']     = _NumCont2
        _Caculation_Parameters['_NwellWidth']       = _NwellWidth

        ## Find Outter boundary
        tmp = self.get_outter_KJH4('SRF_Pbodyring')

        ## Define _XlengthIntn
        _Caculation_Parameters['_XlengthIntn'] = abs( tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0]) + 2*_NwellWidth + _right_margin2 + _left_margin2

        ## Define _YlengthIntn
        _Caculation_Parameters['_YlengthIntn'] = abs( tmp['_Mostup']['coord'][0] - tmp['_Mostdown']['coord'][0]) + 2*_NwellWidth + _up_margin2 + _down_margin2

        ## Generate Sref
        self._DesignParameter['SRF_Nbodyring'] = self._SrefElementDeclaration(_DesignObj=A13_NbodyRingforDeepNwell_KJH._NbodyRingforDeepNwell_KJH(_DesignParameter=None, _Name='{}:SRF_Nbodyring'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_Nbodyring']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_Nbodyring']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_Nbodyring']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate
        self._DesignParameter['SRF_Nbodyring']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_Nbodyring']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        target_coord = [tmp['_Mostleft']['coord'][0], tmp['_Mostdown']['coord'][0]]
        ## Approaching_coord
        ## x
        tmp2_1 = self.get_param_KJH4('SRF_Nbodyring', 'SRF_NbodyLeft', 'SRF_NbodyContactPhyLen', 'BND_Nwell')
        approaching_coordx = tmp2_1[0][0][0][0][0]['_XY_right'][0]
        ## y
        tmp2_2 = self.get_param_KJH4('SRF_Nbodyring', 'SRF_NbodyBottom', 'SRF_NbodyContactPhyLen', 'BND_Nwell')
        approaching_coordy = tmp2_2[0][0][0][0][0]['_XY_up'][1]

        approaching_coord = [approaching_coordx, approaching_coordy]
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Nbodyring')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] - _left_margin2
        New_Scoord[1] = New_Scoord[1] - _down_margin2
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_Nbodyring']['_XYCoordinates'] = tmpXY


        ########################
        # P Body Contact(M1, CA, RX, BP) in NWell for GR135a
        ## SREF Generation
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(
            A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length'] = None
        _Caculation_Parameters['_NumCont'] = 1
        _Caculation_Parameters['_Vtc_flag'] = False

        ## Cal length
        tmp1 = self.get_param_KJH4('SRF_Nbody_withinPIsolated', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        _Caculation_Parameters['_Length'] = tmp1[0][0][0][0]['_Xwidth']

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Pbody_withinNW'] = self._SrefElementDeclaration(
            _DesignObj=A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen(_DesignParameter=None,
                                                                            _Name='{}:SRF_Pbody_withinNW'.format(
                                                                                _Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Pbody_withinNW']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbody_withinNW']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbody_withinNW']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Initialize Sref _XYcoordinate:
        self._DesignParameter['SRF_Pbody_withinNW']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        ## Calculate
        tmp1_1 = self.get_param_KJH4('SRF_Nbody_withinPIsolated', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        tmp1_2 = self.get_param_KJH4('SRF_Nbodyring', 'SRF_NbodyBottom', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        target_coord = [tmp1_1[0][0][0][0]['_XY_left'][0], tmp1_2[0][0][0][0][0]['_XY_up'][1]]

        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_Pbody_withinNW', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down_left']

        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pbody_withinNW')
        SpaceBtwNbodyRingPbodyContactInNW = 500
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[1] = Scoord[1] + max(SpaceBtwNbodyRingPbodyContactInNW, _DRCobj._OdMinSpace2Pp)

        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define Coordinates
        self._DesignParameter['SRF_Pbody_withinNW']['_XYCoordinates'] = tmpXY


        # BP Layer Extension(GR350a : BP Minimum Width for run length > 0, >= 0.17um)
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PPEnclosurePBody_withinNW'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Pbody_withinNW', 'SRF_PbodyContactPhyLen', 'BND_ODLayer')
        self._DesignParameter['BND_PPEnclosurePBody_withinNW']['_YWidth'] = tmp1[0][0][0][0][
                                                                                '_Ywidth'] + 2 * _DRCobj._PpMinExtensiononPactive

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_PPEnclosurePBody_withinNW']['_XWidth'] = tmp1[0][0][0][0][
                                                                                '_Xwidth'] + 2 * _DRCobj._PpMinExtensiononPactive
        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_PPEnclosurePBody_withinNW']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0]['_XY_cent']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PPEnclosurePBody_withinNW')
        approaching_coord = tmp2[0][0]['_XY_cent']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PPEnclosurePBody_withinNW')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_PPEnclosurePBody_withinNW']['_XYCoordinates'] = tmpXY


        # Routing Btw PBodyContact in NW and NBodyContact in T3
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Pbody_Nbody_withinPsub_Hrz_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp2 = self.get_param_KJH4('SRF_Nbody_withinPIsolated', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        tmp3 = self.get_param_KJH4('SRF_Pbody_withinNW', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        self._DesignParameter['BND_Pbody_Nbody_withinPsub_Hrz_M1']['_YWidth'] = abs(tmp2[0][0][0][0]['_XY_up'][1] - tmp3[0][0][0][0]['_XY_down'][1])

        ## Define Boundary_element _XWidth
        Pbody_Nbody_withinPsub_M1HrzPathWidth = 200
        self._DesignParameter['BND_Pbody_Nbody_withinPsub_Hrz_M1']['_XWidth'] = Pbody_Nbody_withinPsub_M1HrzPathWidth

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Pbody_Nbody_withinPsub_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp2[0][0][0][0]['_XY_up']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Pbody_Nbody_withinPsub_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_up']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Pbody_Nbody_withinPsub_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Pbody_Nbody_withinPsub_Hrz_M1']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Guardring(T3)
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT / DEEPNWELL
        self._DesignParameter['BND_Deepnwell'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['DEEPNWELL'][0],
        _Datatype=DesignParameters._LayerMapping['DEEPNWELL'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Nbodyring','BND_ExtenNwell_Top')
        tmp2 = self.get_param_KJH4('SRF_Nbodyring','BND_ExtenNwell_Bottom')
        self._DesignParameter['BND_Deepnwell']['_YWidth'] = abs( tmp1[0][0][0]['_XY_down'][1] - tmp2[0][0][0]['_XY_up'][1] ) + _DRCobj._T3NwellOverlap * 2

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Nbodyring','BND_ExtenNwell_Right')
        tmp2 = self.get_param_KJH4('SRF_Nbodyring','BND_ExtenNwell_Left')
        self._DesignParameter['BND_Deepnwell']['_XWidth'] = abs( tmp1[0][0][0]['_XY_left'][0] - tmp2[0][0][0]['_XY_right'][0] ) + _DRCobj._T3NwellOverlap * 2

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Deepnwell']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Deepnwell']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Nbodyring', 'BND_ExtenNwell_Bottom')
        tmp2 = self.get_param_KJH4('SRF_Nbodyring', 'BND_ExtenNwell_Left')
        target_coordx = tmp2[0][0][0]['_XY_right'][0]
        target_coordy = tmp1[0][0][0]['_XY_up'][1]
        target_coord = [ target_coordx, target_coordy ]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Deepnwell')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Deepnwell')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] - _DRCobj._T3NwellOverlap
        New_Scoord[1] = New_Scoord[1] - _DRCobj._T3NwellOverlap
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Deepnwell']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Guardring: Pbody2
        ## Guardring
        ## Pre-defined DRC
        _right_margin = 550
        _left_margin = 550
        _up_margin = 550
        _down_margin = 550

        _NumCont = 3

        ## Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A10_PbodyRing_KJH3._PbodyRing._ParametersForDesignCalculation)
        _Caculation_Parameters['_XlengthIntn'] = None
        _Caculation_Parameters['_YlengthIntn'] = None
        _Caculation_Parameters['_NumContTop'] = _NumCont
        _Caculation_Parameters['_NumContBottom'] = _NumCont
        _Caculation_Parameters['_NumContLeft'] = _NumCont
        _Caculation_Parameters['_NumContRight'] = _NumCont

        ## Find Outter boundary
        tmp = self.get_outter_KJH4('SRF_Nbodyring')

        ## Define _XlengthIntn
        _Caculation_Parameters['_XlengthIntn'] = abs( tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0]) + _right_margin + _left_margin

        ## Define _YlengthIntn
        _Caculation_Parameters['_YlengthIntn'] = abs( tmp['_Mostup']['coord'][0] - tmp['_Mostdown']['coord'][0]) + _up_margin + _down_margin

        ## Generate Sref
        self._DesignParameter['SRF_Pbodyring2'] = self._SrefElementDeclaration(
            _DesignObj=A10_PbodyRing_KJH3._PbodyRing(_DesignParameter=None,
            _Name='{}:SRF_Pbodyring2'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_Pbodyring2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_Pbodyring2']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_Pbodyring2']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate
        self._DesignParameter['SRF_Pbodyring2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_Pbodyring2']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        target_coord = [tmp['_Mostleft']['coord'][0], tmp['_Mostdown']['coord'][0]]
        ## Approaching_coord
        ## x
        tmp2_1 = self.get_param_KJH4('SRF_Pbodyring2', 'SRF_PbodyLeft', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coordx = tmp2_1[0][0][0][0][0]['_XY_right'][0]
        ## y
        tmp2_2 = self.get_param_KJH4('SRF_Pbodyring2', 'SRF_PbodyBottom', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coordy = tmp2_2[0][0][0][0][0]['_XY_up'][1]

        approaching_coord = [approaching_coordx, approaching_coordy]
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pbodyring2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] - _left_margin
        New_Scoord[1] = New_Scoord[1] - _down_margin
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_Pbodyring2']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Delete
        #del self._DesignParameter['BND_Inputnode']
        #del self._DesignParameter['BND_Outputnode']


        ## LVS1 Drawing8 Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_LVS1DRW8'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['LVS1_dr8'][0],
        _Datatype=DesignParameters._LayerMapping['LVS1_dr8'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Nbodyring', 'SRF_NbodyTop', 'SRF_NbodyContactPhyLen', 'BND_Nwell')
        tmp2 = self.get_param_KJH4('SRF_Nbodyring', 'SRF_NbodyLeft', 'SRF_NbodyContactPhyLen', 'BND_Nwell')
        self._DesignParameter['BND_LVS1DRW8']['_YWidth'] = tmp2[0][0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_LVS1DRW8']['_XWidth'] = tmp1[0][0][0][0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_LVS1DRW8']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1_1 = tmp1[0][0][0][0][0]['_XY_left'][0]
        tmp1_2 = tmp2[0][0][0][0][0]['_XY_up'][1]
        target_coord = [tmp1_1, tmp1_2]
                            ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_LVS1DRW8')
        approaching_coord = tmp3[0][0]['_XY_up_left']
                            ## Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_LVS1DRW8']['_XYCoordinates'] = tmpXY





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
    libname = 'Proj_RcdacSar_C09_Tr6_KJH'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'C09_01_Guardring_v0_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

        # Tr6
        _Tr6_NMOSNumberofGate    =   6,     #number
        _Tr6_NMOSChannelWidth    =   1000,   #number
        _Tr6_NMOSChannellength   =   30,     #number
        _Tr6_GateSpacing         =   100,    #None/number
        _Tr6_SDWidth             =   None,   #None/number
        _Tr6_XVT                 =   'SLVT',  #'XVT' ex)SLVT LVT RVT HVT
        _Tr6_PCCrit              =   True,   #None/True

            # Source_node_ViaM1M2
        _Tr6_Source_Via_TF       =   False,  #True/False

            # Drain_node_ViaM1M2
        _Tr6_Drain_Via_TF        =   False,  #True/False

            # POLY dummy setting
        _Tr6_NMOSDummy           =   True,  # TF
                # if _PMOSDummy == True
        _Tr6_NMOSDummy_length    =   None,  # None/Value
        _Tr6_NMOSDummy_placement =   None,  # None/'Up'/'Dn'/

        # Vp node
        _Vp_node_width = 280, #Number
        _Vp_node_metal_Layer = 3, #number

        # Guardring
        # Pbody: number of contact
        # Nbody
        _NwellWidth=850,  # number
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
    LayoutObj = _Guardring(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    #testStreamFile = open('./gdsfile/{}'.format(_fileName), 'wb')
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
