from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC_EGFET

import numpy as np
import copy
import math

from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A51_TIA_P1P2P4_random
# from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_TIA_Pbodyring
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_TIA_Nbodyring





## ########################################################################################################################################################## Class_HEADER
class _TIA_P1P2P4_Nbodyring_YCH(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

        # PMOS
        _Tr1_PMOSNumberofGate=45,
        _Tr1_PMOSChannelWidth=6000,
        _Tr1_PMOSChannellength=150,
        _Tr1_GateSpacing	= None,
        _Tr1_SDWidth			= None,
        _Tr1_XVT				= 'EG',
        _Tr1_PCCrit				= None,

        # Source_node_ViaM1M2
        _Tr1_Source_Via_TF = True,

        # Drain_node_ViaM1M2
        _Tr1_Drain_Via_TF = True,

        # POLY dummy setting
        _Tr1_PMOSDummy = True, # TF
        # if _PMOSDummy == True
        _Tr1_PMOSDummy_length = None, # None/Value
        _Tr1_PMOSDummy_placement = None, # None/'Up'/'Dn'/

        # PMOS
        _Tr2_PMOSNumberofGate=None,
        _Tr2_PMOSChannelWidth=None,
        _Tr2_PMOSChannellength=None,
        _Tr2_GateSpacing	= None,
        _Tr2_SDWidth			= None,
        _Tr2_XVT				= None,
        _Tr2_PCCrit				= None,

        # Source_node_ViaM1M2
        _Tr2_Source_Via_TF = None,

        # Drain_node_ViaM1M2
        _Tr2_Drain_Via_TF = None,

        # POLY dummy setting
        _Tr2_PMOSDummy = None, # TF
        # if _PMOSDummy == True
        _Tr2_PMOSDummy_length = None, # None/Value
        _Tr2_PMOSDummy_placement = None, # None/Up/Dn/

        #PMOS
        _Tr4_PMOSNumberofGate	= None,
        _Tr4_PMOSChannelWidth	= None,
        _Tr4_PMOSChannellength	= None,
        _Tr4_GateSpacing		= None,
        _Tr4_SDWidth			= None,
        _Tr4_XVT				= None,
        _Tr4_PCCrit				= None,

        #Source_node_ViaM1M2
        _Tr4_Source_Via_TF = None,

        #Drain_node_ViaM1M2
        _Tr4_Drain_Via_TF = None,

        #POLY dummy setting
        _Tr4_PMOSDummy = None, #TF
            #if _PMOSDummy == True
        _Tr4_PMOSDummy_length = None, #None/Value
        _Tr4_PMOSDummy_placement = None, #None/Up/Dn/

        _NumContTop = 3,
        _NumContBottom = 3,
        _NumContLeft = 3,
        _NumContRight = 3,

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


    ## ################################################################################################################################################ _CalculateDesignParameter
    def _CalculateDesignParameter(self,

                                  # PMOS
                                  _Tr1_PMOSNumberofGate=None,
                                  _Tr1_PMOSChannelWidth=None,
                                  _Tr1_PMOSChannellength=None,
                                  _Tr1_GateSpacing=None,
                                  _Tr1_SDWidth	= None,
                                  _Tr1_XVT			= None,
                                  _Tr1_PCCrit			= None,

                                  # Source_node_ViaM1M2
                                  _Tr1_Source_Via_TF= None,

                                  # Drain_node_ViaM1M2
                                  _Tr1_Drain_Via_TF= None,

                                  # POLY dummy setting
                                  _Tr1_PMOSDummy= None  , # TF
                                  # if _PMOSDummy == True
                                  _Tr1_PMOSDummy_length = None, # None/Value
                                  _Tr1_PMOSDummy_placement = None, # None/Up/Dn/

                                  # PMOS
                                  _Tr2_PMOSNumberofGate=None,
                                  _Tr2_PMOSChannelWidth=None,
                                  _Tr2_PMOSChannellength=None,
                                  _Tr2_GateSpacing=None,
                                  _Tr2_SDWidth	= None,
                                  _Tr2_XVT			= None,
                                  _Tr2_PCCrit			= None,

                                  # Source_node_ViaM1M2
                                  _Tr2_Source_Via_TF= None,

                                  # Drain_node_ViaM1M2
                                  _Tr2_Drain_Via_TF= None,

                                  # POLY dummy setting
                                  _Tr2_PMOSDummy= None  , # TF
                                  # if _PMOSDummy == True
                                  _Tr2_PMOSDummy_length = None, # None/Value
                                  _Tr2_PMOSDummy_placement = None, # None/Up/Dn/

                                  # PMOS
                                  _Tr4_PMOSNumberofGate=None,
                                  _Tr4_PMOSChannelWidth=None,
                                  _Tr4_PMOSChannellength=None,
                                  _Tr4_GateSpacing=None,
                                  _Tr4_SDWidth	= None,
                                  _Tr4_XVT			= None,
                                  _Tr4_PCCrit			= None,

                                  # Source_node_ViaM1M2
                                  _Tr4_Source_Via_TF= None,

                                  # Drain_node_ViaM1M2
                                  _Tr4_Drain_Via_TF= None,

                                  # POLY dummy setting
                                  _Tr4_PMOSDummy= None  , # TF
                                  # if _PMOSDummy == True
                                  _Tr4_PMOSDummy_length = None, # None/Value
                                  _Tr4_PMOSDummy_placement = None, # None/Up/Dn/


                                  _NumContTop=3,
                                  _NumContBottom=3,
                                  _NumContLeft=3,
                                  _NumContRight=3,

                                  ):



        ## ################################################################################################################################# Class_HEADER: Pre Defined Parameter Before Calculation
        # Load DRC library
        _DRCObj = DRC_EGFET.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']


        ## ################################################################################################################################# Calculation_Start
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

        ## SREF Generation Tr1Tr2Tr4
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A51_TIA_P1P2P4_random._TIA_P1P2P4_YCH._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr1_PMOSNumberofGate'] = _Tr1_PMOSNumberofGate
        _Caculation_Parameters['_Tr1_PMOSChannelWidth'] = _Tr1_PMOSChannelWidth
        _Caculation_Parameters['_Tr1_PMOSChannellength'] = _Tr1_PMOSChannellength
        _Caculation_Parameters['_Tr1_GateSpacing'] = _Tr1_GateSpacing
        _Caculation_Parameters['_Tr1_SDWidth'] = _Tr1_SDWidth
        _Caculation_Parameters['_Tr1_XVT'] = _Tr1_XVT
        _Caculation_Parameters['_Tr1_PCCrit'] = _Tr1_PCCrit
        _Caculation_Parameters['_Tr1_Source_Via_TF'] = _Tr1_Source_Via_TF
        _Caculation_Parameters['_Tr1_Drain_Via_TF'] = _Tr1_Drain_Via_TF
        _Caculation_Parameters['_Tr1_PMOSDummy'] = _Tr1_PMOSDummy
        _Caculation_Parameters['_Tr1_PMOSDummy_length'] = _Tr1_PMOSDummy_length
        _Caculation_Parameters['_Tr1_PMOSDummy_placement'] = _Tr1_PMOSDummy_placement

        _Caculation_Parameters['_Tr2_PMOSNumberofGate'] = _Tr2_PMOSNumberofGate
        _Caculation_Parameters['_Tr2_PMOSChannelWidth'] = _Tr2_PMOSChannelWidth
        _Caculation_Parameters['_Tr2_PMOSChannellength'] = _Tr2_PMOSChannellength
        _Caculation_Parameters['_Tr2_GateSpacing'] = _Tr2_GateSpacing
        _Caculation_Parameters['_Tr2_SDWidth'] = _Tr2_SDWidth
        _Caculation_Parameters['_Tr2_XVT'] = _Tr2_XVT
        _Caculation_Parameters['_Tr2_PCCrit'] = _Tr2_PCCrit
        _Caculation_Parameters['_Tr2_Source_Via_TF'] = _Tr2_Source_Via_TF
        _Caculation_Parameters['_Tr2_Drain_Via_TF'] = _Tr2_Drain_Via_TF
        _Caculation_Parameters['_Tr2_PMOSDummy'] = _Tr2_PMOSDummy
        _Caculation_Parameters['_Tr2_PMOSDummy_length'] = _Tr2_PMOSDummy_length
        _Caculation_Parameters['_Tr2_PMOSDummy_placement'] = _Tr2_PMOSDummy_placement

        _Caculation_Parameters['_Tr4_PMOSNumberofGate'] = _Tr4_PMOSNumberofGate
        _Caculation_Parameters['_Tr4_PMOSChannelWidth'] = _Tr4_PMOSChannelWidth
        _Caculation_Parameters['_Tr4_PMOSChannellength'] = _Tr4_PMOSChannellength
        _Caculation_Parameters['_Tr4_GateSpacing'] = _Tr4_GateSpacing
        _Caculation_Parameters['_Tr4_SDWidth'] = _Tr4_SDWidth
        _Caculation_Parameters['_Tr4_XVT'] = _Tr4_XVT
        _Caculation_Parameters['_Tr4_PCCrit'] = _Tr4_PCCrit
        _Caculation_Parameters['_Tr4_Source_Via_TF'] = _Tr4_Source_Via_TF
        _Caculation_Parameters['_Tr4_Drain_Via_TF'] = _Tr4_Drain_Via_TF
        _Caculation_Parameters['_Tr4_PMOSDummy'] = _Tr4_PMOSDummy
        _Caculation_Parameters['_Tr4_PMOSDummy_length'] = _Tr4_PMOSDummy_length
        _Caculation_Parameters['_Tr4_PMOSDummy_placement'] = _Tr4_PMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Pmos_Tr1Tr2Tr4'] = self._SrefElementDeclaration(
                             _DesignObj=A51_TIA_P1P2P4_random._TIA_P1P2P4_YCH(_DesignParameter=None, _Name='{}:SRF_Pmos_Tr1Tr2Tr4'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Pmos_Tr1Tr2Tr4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_Tr1Tr2Tr4']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_Tr1Tr2Tr4']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_Tr1Tr2Tr4']['_XYCoordinates'] = [[0, 0]]



        ## SREF Generation Pbodyring
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A50_TIA_Nbodyring._NbodyRing._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_XlengthIntn'] = None
        _Caculation_Parameters['_YlengthIntn'] = None
        _Caculation_Parameters['_NumContTop'] = _NumContTop
        _Caculation_Parameters['_NumContBottom'] = _NumContBottom
        _Caculation_Parameters['_NumContLeft'] = _NumContLeft
        _Caculation_Parameters['_NumContRight'] = _NumContRight

        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4', 'SRF_Pmos_Tr2', 'SRF_Pmos', 'BND_EGLayer')
        tmp2 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4', 'SRF_Pmos_Tr1', 'SRF_Pmos', 'BND_EGLayer')

        target_coordx = tmp1[0][0][0][0][0]['_XY_right'][0]
        target_coordy = tmp2[0][0][0][0][0]['_XY_left'][0]
        target_length_x = target_coordx - target_coordy
        _Caculation_Parameters['_XlengthIntn'] = target_length_x + 1000

        target_coordx = tmp1[0][0][0][0][0]['_XY_up'][1]
        target_coordy = tmp2[0][0][0][0][0]['_XY_down'][1]
        target_length_y = target_coordx - target_coordy
        _Caculation_Parameters['_YlengthIntn'] = target_length_y + 1000

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Nbodyring'] = self._SrefElementDeclaration(
                                _DesignObj=A50_TIA_Nbodyring._NbodyRing(_DesignParameter=None,_Name='{}:SRF_Nbodyring'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Nbodyring']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nbodyring']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nbodyring']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nbodyring']['_XYCoordinates'] = [[0, 0]]


        tmpXY = []
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4','SRF_Pmos_Tr4', 'SRF_Pmos', 'BND_EGLayer')
        target_coord = tmp1[0][0][0][0][0]['_XY_up']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Nbodyring','SRF_NbodyTop','SRF_NbodyContactPhyLen','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0][0]['_XY_down']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Nbodyring')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)

        New_Scoord[1] = New_Scoord[1] + 500
        tmpXY.append(New_Scoord)

        self._DesignParameter['SRF_Nbodyring']['_XYCoordinates'] = tmpXY


## ################################################################################################################### Metal3_Layer_Connect_P1P2_Source
        # Define Boundary_element
        self._DesignParameter['BND_Metal3Layer_Connect_P1P2_Source'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4', 'SRF_Pmos_Tr1', 'BND_Metal3Layer_Hrz_Source')
        tmp2 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4', 'SRF_Pmos_Tr2', 'BND_Metal3Layer_Hrz_Source')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal3Layer_Connect_P1P2_Source']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth'] / 3

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal3Layer_Connect_P1P2_Source']['_XWidth'] = abs (tmp2[0][0][-1][0]['_XY_right'][0]-tmp1[0][0][0][0]['_XY_left'][0])

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal3Layer_Connect_P1P2_Source']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4', 'SRF_Pmos_Tr1', 'BND_Metal3Layer_Hrz_Source')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal3Layer_Connect_P1P2_Source')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal3Layer_Connect_P1P2_Source')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal3Layer_Connect_P1P2_Source']['_XYCoordinates'] = tmpXY



## ################################################################################################################### Metal3_Layer_Connect_P1_Drain
        # Define Boundary_element
        self._DesignParameter['BND_Metal3Layer_Connect_P1_Drain'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4', 'SRF_Pmos_Tr1', 'BND_Metal3Layer_Hrz_Drain')


        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal3Layer_Connect_P1_Drain']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth'] / 3 + 100 # 12/31 수정

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal3Layer_Connect_P1_Drain']['_XWidth'] = abs(tmp1[0][0][-1][0]['_XY_right'][0] - tmp1[0][0][0][0]['_XY_left'][0])

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal3Layer_Connect_P1_Drain']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4', 'SRF_Pmos_Tr1', 'BND_Metal3Layer_Hrz_Drain')
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal3Layer_Connect_P1_Drain')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal3Layer_Connect_P1_Drain')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal3Layer_Connect_P1_Drain']['_XYCoordinates'] = tmpXY
## ################################################################################################################### Metal3_Layer_Connect_P2_Drain
        # Define Boundary_element
        self._DesignParameter['BND_Metal3Layer_Connect_P2_Drain'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4', 'SRF_Pmos_Tr2', 'BND_Metal3Layer_Hrz_Drain')


        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal3Layer_Connect_P2_Drain']['_YWidth'] = min (tmp1[0][0][0][0]['_Ywidth'] / 3 + 100, 1000) # 12/31 수정

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal3Layer_Connect_P2_Drain']['_XWidth'] = abs(tmp1[0][0][-1][0]['_XY_right'][0] - tmp1[0][0][0][0]['_XY_left'][0])

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal3Layer_Connect_P2_Drain']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4', 'SRF_Pmos_Tr2', 'BND_Metal3Layer_Hrz_Drain')
        target_coordx = tmp1[0][0][0][0]['_XY_down_left'][0]
        target_coordy = tmp1[0][0][0][0]['_XY_down_left'][1] + 100  # 12/30 수정
        target_coord = [target_coordx, target_coordy]
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal3Layer_Connect_P2_Drain')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal3Layer_Connect_P2_Drain')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal3Layer_Connect_P2_Drain']['_XYCoordinates'] = tmpXY

## ################################################################################################################### Metal1_Layer_Connect_P1toRing_Source

        # Define Boundary_element
        self._DesignParameter['BND_Metal1Layer_Connect_P1toRing_Source'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4', 'SRF_Pmos_Tr4', 'SRF_Pmos', 'BND_Met1Layer_Source')
        tmp2 = self.get_param_KJH4('SRF_Nbodyring','SRF_NbodyBottom','SRF_NbodyContactPhyLen','BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal1Layer_Connect_P1toRing_Source']['_YWidth'] = abs(tmp1[0][0][0][0][0]['_XY_cent'][1]-tmp2[0][0][0][0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal1Layer_Connect_P1toRing_Source']['_XWidth'] = tmp1[0][0][0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal1Layer_Connect_P1toRing_Source']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        if (_Tr4_PMOSNumberofGate % 2 == 1):
            for i in range(0, int(_Tr4_PMOSNumberofGate / 2) + 1):
                # Calculate
                # Target_coord
                tmp1 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4', 'SRF_Pmos_Tr4', 'SRF_Pmos', 'BND_Met1Layer_Source')
                target_coord = tmp1[0][0][0][i][0]['_XY_cent']
                # Approaching_coord
                tmp2 = self.get_param_KJH4('BND_Metal1Layer_Connect_P1toRing_Source')
                approaching_coord = tmp2[0][0]['_XY_up']
                # Sref coord
                tmp3 = self.get_param_KJH4('BND_Metal1Layer_Connect_P1toRing_Source')
                Scoord = tmp3[0][0]['_XY_origin']
                # Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
                # Define
                self._DesignParameter['BND_Metal1Layer_Connect_P1toRing_Source']['_XYCoordinates'] = tmpXY
        else:
            for i in range(0, int(_Tr4_PMOSNumberofGate / 2) + 1):
                # Calculate
                # Target_coord
                tmp1 = self.get_param_KJH4('SRF_Pmos_Tr1Tr2Tr4', 'SRF_Pmos_Tr4', 'SRF_Pmos', 'BND_Met1Layer_Source')
                target_coord = tmp1[0][0][0][i][0]['_XY_cent']
                # Approaching_coord
                tmp2 = self.get_param_KJH4('BND_Metal1Layer_Connect_P1toRing_Source')
                approaching_coord = tmp2[0][0]['_XY_up']
                # Sref coord
                tmp3 = self.get_param_KJH4('BND_Metal1Layer_Connect_P1toRing_Source')
                Scoord = tmp3[0][0]['_XY_origin']
                # Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
                # Define
                self._DesignParameter['BND_Metal1Layer_Connect_P1toRing_Source']['_XYCoordinates'] = tmpXY


## ################################################################################################################### Nwell extension

        self._DesignParameter['BND_Nwell_Extension'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['NWELL'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Nbodyring', 'BND_ExtenODLayer_Top')
        tmp2 = self.get_param_KJH4('SRF_Nbodyring', 'BND_ExtenMet1Layer_Bottom')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Nwell_Extension']['_YWidth'] = abs(tmp1[0][0][0]['_XY_up'][1] - tmp2[0][0][0]['_XY_down'][1]) + 112

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Nwell_Extension']['_XWidth'] = abs(tmp1[0][0][0]['_XY_right'][0] - tmp1[0][0][0]['_XY_left'][0]) + 112

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Nwell_Extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Nbodyring', 'BND_ExtenODLayer_Top')
        target_coord = tmp1[0][0][0]['_XY_up_left']
        target_coord[0] = target_coord[0] - 56
        target_coord[1] = target_coord[1] + 56
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Nwell_Extension')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Nwell_Extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Nwell_Extension']['_XYCoordinates'] = tmpXY



## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_YCH
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0
    import random

    for _iter in range(10):

        libname = 'Proj_A52_TIA_P1P2P4_Nbodyring_v{}'.format(_iter + 11)
        cellname = 'A52_TIA_P1P2P4_Nbodyring'
        _fileName = cellname + '.gds'

        _TR1_2_PMOSNumberofGate = random.randrange(3, 20, 1)
        _TR4_PMOSNumberofGate = random.randrange(2, 10, 1)
        _TR1_2_4_PMOSChannelWidth = random.randrange(1000, 10000, 1000)

        ''' Input Parameters for Layout Object '''
        InputParams = dict(

            #PMOS
            _Tr1_PMOSNumberofGate=_TR1_2_PMOSNumberofGate,
            _Tr1_PMOSChannelWidth=_TR1_2_4_PMOSChannelWidth,
            _Tr1_PMOSChannellength=150,
            _Tr1_GateSpacing	= None,
            _Tr1_SDWidth			= None,
            _Tr1_XVT				= 'EG',
            _Tr1_PCCrit				= None,

            # Source_node_ViaM1M2
            _Tr1_Source_Via_TF = True,

            # Drain_node_ViaM1M2
            _Tr1_Drain_Via_TF = True,

            # POLY dummy setting
            _Tr1_PMOSDummy = True, # TF
            # if _PMOSDummy == True
            _Tr1_PMOSDummy_length = None, # None/Value
            _Tr1_PMOSDummy_placement = None, # None/'Up'/'Dn'/

            #PMOS
            _Tr2_PMOSNumberofGate	= _TR1_2_PMOSNumberofGate,
            _Tr2_PMOSChannelWidth	= _TR1_2_4_PMOSChannelWidth,
            _Tr2_PMOSChannellength	= 150,
            _Tr2_GateSpacing		= None,
            _Tr2_SDWidth			= None,
            _Tr2_XVT				= 'EG',
            _Tr2_PCCrit				= None,

            #Source_node_ViaM1M2
            _Tr2_Source_Via_TF = True,

            #Drain_node_ViaM1M2
            _Tr2_Drain_Via_TF = True,

            #POLY dummy setting
            _Tr2_PMOSDummy = True, #TF
                #if _PMOSDummy == True
            _Tr2_PMOSDummy_length = None, #None/Value
            _Tr2_PMOSDummy_placement = None, #None/'Up'/'Dn'/

            # PMOS
            _Tr4_PMOSNumberofGate=_TR4_PMOSNumberofGate,
            _Tr4_PMOSChannelWidth=_TR1_2_4_PMOSChannelWidth,
            _Tr4_PMOSChannellength=150,
            _Tr4_GateSpacing	= None,
            _Tr4_SDWidth			= None,
            _Tr4_XVT				= 'EG',
            _Tr4_PCCrit				= None,

            # Source_node_ViaM1M2
            _Tr4_Source_Via_TF = True,

            # Drain_node_ViaM1M2
            _Tr4_Drain_Via_TF = True,

            # POLY dummy setting
            _Tr4_PMOSDummy = True, # TF
            # if _PMOSDummy == True
            _Tr4_PMOSDummy_length = None, # None/Value
            _Tr4_PMOSDummy_placement = None, # None/'Up'/'Dn'/


            # P body ring
            _NumContTop = 3,
            _NumContBottom=3,
            _NumContLeft=3,
            _NumContRight=3,

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
        LayoutObj = _TIA_P1P2P4_Nbodyring_YCH(_DesignParameter=None, _Name=cellname)
        LayoutObj._CalculateDesignParameter(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
        testStreamFile = open('./{}'.format(_fileName), 'wb')
        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        print('###############      Sending to FTP Server...      ##################')
        My = MyInfo_YCH.USER(DesignParameters._Technology)
        Checker = DRCchecker_KJH0.DRCchecker_KJH0(
                                                        username=My.ID,
                                                        password=My.PW,
                                                        WorkDir=My.Dir_Work,
                                                        DRCrunDir=My.Dir_DRCrun,
                                                        libname=libname,
                                                        cellname=cellname,
                                                        GDSDir=My.Dir_GDS
                                                 )
        #Checker.lib_deletion()
        Checker.cell_deletion()
        Checker.Upload2FTP()
        Checker.StreamIn(tech=DesignParameters._Technology)
        # Checker_KJH0.DRCchecker()
        print('#############################      Finished      ################################')
    # end of 'main():' ---------------------------------------------------------------------------------------------