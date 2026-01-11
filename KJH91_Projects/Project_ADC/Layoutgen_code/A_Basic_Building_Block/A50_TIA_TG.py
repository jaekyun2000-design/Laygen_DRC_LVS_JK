from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC_EGFET

import numpy as np
import copy
import math

from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A04_PmosWithDummy_KJH3_YCH_TIA
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A03_NmosWithDummy_KJH4_YCH_TIA

from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2_YCH

class _TIA_TG_YCH(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

        #NMOS inverter
        _inv_NMOSNumberofGate	= None,
        _inv_NMOSChannelWidth	= None,
        _inv_NMOSChannellength	= None,
        _inv_NMOSGateSpacing		= None,
        _inv_NMOSSDWidth			= None,
        _inv_NMOSXVT				= None,
        _inv_NMOSPCCrit				= None,

        #Source_node_ViaM1M2
        _inv_NMOSSource_Via_TF = None,

        #Drain_node_ViaM1M2
        _inv_NMOSDrain_Via_TF = None,

        #POLY dummy setting
        _inv_NMOSDummy = None, #TF
            #if _NMOSDummy == True
        _inv_NMOSDummy_length = None, #None/Value
        _inv_NMOSDummy_placement = None, #None/Up/Dn/

        # PMOS inverter
        _inv_PMOSNumberofGate = None,
        _inv_PMOSChannelWidth = None,
        _inv_PMOSChannellength = None,
        _inv_PMOSGateSpacing = None,
        _inv_PMOSSDWidth = None,
        _inv_PMOSXVT = None,
        _inv_PMOSPCCrit = None,

            # Source_node_ViaM1M2
        _inv_PMOSSource_Via_TF = None,

            # Drain_node_ViaM1M2
        _inv_PMOSDrain_Via_TF = None,

            # POLY dummy setting
        _inv_PMOSDummy = None,  # TF
            # if _PMOSDummy == True
        _inv_PMOSDummy_length = None,  # None/Value
        _inv_PMOSDummy_placement = None,  # None/Up/Dn/

        # NMOS TG
        _tg_NMOSNumberofGate=None,
        _tg_NMOSChannelWidth=None,
        _tg_NMOSChannellength=None,
        _tg_NMOSGateSpacing	= None,
        _tg_NMOSSDWidth			= None,
        _tg_NMOSXVT				= None,
        _tg_NMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _tg_NMOSSource_Via_TF = None,

        # Drain_node_ViaM1M2
        _tg_NMOSDrain_Via_TF = None,

        # POLY dummy setting
        _tg_NMOSDummy = None, # TF
        # if _NMOSDummy == True
        _tg_NMOSDummy_length = None, # None/Value
        _tg_NMOSDummy_placement = None, # None/Up/Dn/

        # PMOS TG
        _tg_PMOSNumberofGate = None,
        _tg_PMOSChannelWidth = None,
        _tg_PMOSChannellength = None,
        _tg_PMOSGateSpacing = None,
        _tg_PMOSSDWidth = None,
        _tg_PMOSXVT = None,
        _tg_PMOSPCCrit = None,

        # Source_node_ViaM1M2
        _tg_PMOSSource_Via_TF = None,

        # Drain_node_ViaM1M2
        _tg_PMOSDrain_Via_TF = None,

        # POLY dummy setting
        _tg_PMOSDummy = None,  # TF
        # if _PMOSDummy == True
        _tg_PMOSDummy_length = None,  # None/Value
        _tg_PMOSDummy_placement = None,  # None/Up/Dn/
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

                                  # NMOS inverter
                                  _inv_NMOSNumberofGate=None,
                                  _inv_NMOSChannelWidth=None,
                                  _inv_NMOSChannellength=None,
                                  _inv_NMOSGateSpacing=None,
                                  _inv_NMOSSDWidth	= None,
                                  _inv_NMOSXVT			= None,
                                  _inv_NMOSPCCrit			= None,

                                  # Source_node_ViaM1M2
                                  _inv_NMOSSource_Via_TF= None,

                                  # Drain_node_ViaM1M2
                                  _inv_NMOSDrain_Via_TF= None,

                                  # POLY dummy setting
                                  _inv_NMOSDummy= None  , # TF
                                  # if _PMOSDummy == True
                                  _inv_NMOSDummy_length = None, # None/Value
                                  _inv_NMOSDummy_placement = None, # None/Up/Dn/

                                  # PMOS inverter
                                  _inv_PMOSNumberofGate=None,
                                  _inv_PMOSChannelWidth=None,
                                  _inv_PMOSChannellength=None,
                                  _inv_PMOSGateSpacing=None,
                                  _inv_PMOSSDWidth=None,
                                  _inv_PMOSXVT=None,
                                  _inv_PMOSPCCrit=None,

                                  # Source_node_ViaM1M2
                                  _inv_PMOSSource_Via_TF=None,

                                  # Drain_node_ViaM1M2
                                  _inv_PMOSDrain_Via_TF=None,

                                  # POLY dummy setting
                                  _inv_PMOSDummy=None,  # TF
                                  # if _PMOSDummy == True
                                  _inv_PMOSDummy_length=None,  # None/Value
                                  _inv_PMOSDummy_placement=None,  # None/Up/Dn/

                                  # NMOS tg
                                  _tg_NMOSNumberofGate=None,
                                  _tg_NMOSChannelWidth=None,
                                  _tg_NMOSChannellength=None,
                                  _tg_NMOSGateSpacing=None,
                                  _tg_NMOSSDWidth=None,
                                  _tg_NMOSXVT	= None,
                                  _tg_NMOSPCCrit		= None,

                                  # Source_node_ViaM1M2
                                  _tg_NMOSSource_Via_TF= None,

                                  # Drain_node_ViaM1M2
                                  _tg_NMOSDrain_Via_TF= None,

                                  # POLY dummy setting
                                  _tg_NMOSDummy= None  , # TF
                                  # if _PMOSDummy == True
                                  _tg_NMOSDummy_length = None, # None/Value
                                  _tg_NMOSDummy_placement = None, # None/Up/Dn/

                                  # PMOS inverter
                                  _tg_PMOSNumberofGate=None,
                                  _tg_PMOSChannelWidth=None,
                                  _tg_PMOSChannellength=None,
                                  _tg_PMOSGateSpacing=None,
                                  _tg_PMOSSDWidth=None,
                                  _tg_PMOSXVT=None,
                                  _tg_PMOSPCCrit=None,

                                  # Source_node_ViaM1M2
                                  _tg_PMOSSource_Via_TF=None,

                                  # Drain_node_ViaM1M2
                                  _tg_PMOSDrain_Via_TF=None,

                                  # POLY dummy setting
                                  _tg_PMOSDummy=None,  # TF
                                  # if _PMOSDummy == True
                                  _tg_PMOSDummy_length=None,  # None/Value
                                  _tg_PMOSDummy_placement=None,  # None/Up/Dn/

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

        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A03_NmosWithDummy_KJH4_YCH_TIA._NmosWithDummy_KJH3._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOSNumberofGate'] = _inv_NMOSNumberofGate
        _Caculation_Parameters['_NMOSChannelWidth'] = _inv_NMOSChannelWidth
        _Caculation_Parameters['_NMOSChannellength'] = _inv_NMOSChannellength
        _Caculation_Parameters['_GateSpacing'] = _inv_NMOSGateSpacing
        _Caculation_Parameters['_SDWidth'] = _inv_NMOSSDWidth
        _Caculation_Parameters['_XVT'] = _inv_NMOSXVT
        _Caculation_Parameters['_PCCrit'] = _inv_NMOSPCCrit
        _Caculation_Parameters['_Source_Via_TF'] = _inv_NMOSSource_Via_TF
        _Caculation_Parameters['_Drain_Via_TF'] = _inv_NMOSDrain_Via_TF
        _Caculation_Parameters['_NMOSDummy'] = _inv_NMOSDummy
        _Caculation_Parameters['_NMOSDummy_length'] = _inv_NMOSDummy_length
        _Caculation_Parameters['_NMOSDummy_placement'] = _inv_NMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Nmos_inv'] = self._SrefElementDeclaration(
            _DesignObj=A03_NmosWithDummy_KJH4_YCH_TIA._NmosWithDummy_KJH3(_DesignParameter=None,
                                                                          _Name='{}:SRF_Nmos_inv'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Nmos_inv']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos_inv']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos_inv']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos_inv']['_XYCoordinates'] = [[0, 0]]

        ## SREF Generation

        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A04_PmosWithDummy_KJH3_YCH_TIA._PmosWithDummy_KJH3._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_PMOSNumberofGate'] = _inv_PMOSNumberofGate
        _Caculation_Parameters['_PMOSChannelWidth'] = _inv_PMOSChannelWidth
        _Caculation_Parameters['_PMOSChannellength'] = _inv_PMOSChannellength
        _Caculation_Parameters['_GateSpacing'] = _inv_PMOSGateSpacing
        _Caculation_Parameters['_SDWidth'] = _inv_PMOSSDWidth
        _Caculation_Parameters['_XVT'] = _inv_PMOSXVT
        _Caculation_Parameters['_PCCrit'] = _inv_PMOSPCCrit
        _Caculation_Parameters['_Source_Via_TF'] = _inv_PMOSSource_Via_TF
        _Caculation_Parameters['_Drain_Via_TF'] = _inv_PMOSDrain_Via_TF
        _Caculation_Parameters['_PMOSDummy'] = _inv_PMOSDummy
        _Caculation_Parameters['_PMOSDummy_length'] = _inv_PMOSDummy_length
        _Caculation_Parameters['_PMOSDummy_placement'] = _inv_PMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Pmos_inv'] = self._SrefElementDeclaration(
            _DesignObj=A04_PmosWithDummy_KJH3_YCH_TIA._PmosWithDummy_KJH3(_DesignParameter=None, _Name='{}:SRF_Pmos_inv'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Pmos_inv']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_inv']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_inv']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_inv']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        # Calculate
        # Target_coord
        tmp11 = self.get_param_KJH4('SRF_Nmos_inv', 'BND_EGLayer')
        tmp12 = self.get_param_KJH4('SRF_Nmos_inv', 'BND_POLayer')
        target_coordx = tmp11[0][0][0]['_XY_cent'][0]
        target_coordy = tmp12[0][0][0]['_XY_up'][1]
        target_coord = [target_coordx, target_coordy + 700]
        # Approaching_coord
        tmp21 = self.get_param_KJH4('SRF_Pmos_inv', 'BND_EGLayer')
        tmp22 = self.get_param_KJH4('SRF_Pmos_inv', 'BND_POLayer')
        approaching_coordx = tmp21[0][0][0]['_XY_cent'][0]
        approaching_coordy = tmp22[0][0][0]['_XY_down'][1]
        approaching_coord = [approaching_coordx, approaching_coordy]
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pmos_inv')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Pmos_inv']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Metal2_Drain_connect inv
        # Define Boundary_element
        self._DesignParameter['BND_Met2Layer_Drain_connect_inv'] = self._BoundaryElementDeclaration(
                                                                        _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                        _XWidth=None,
                                                                        _YWidth=None,
                                                                        _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Pmos_inv', 'SRF_Drain_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
        tmp2 = self.get_param_KJH4('SRF_Nmos_inv', 'SRF_Drain_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met2Layer_Drain_connect_inv']['_YWidth'] = abs(tmp1[0][0][0][0][0]['_XY_up'][1]-tmp2[0][0][0][0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met2Layer_Drain_connect_inv']['_XWidth'] = tmp1[0][0][0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met2Layer_Drain_connect_inv']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        for i in range(0,len(tmp1[0])):
            # Calculate
            # Target_coord
            tmp1 = self.get_param_KJH4('SRF_Pmos_inv', 'SRF_Drain_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
            target_coord = tmp1[0][i][0][0][0]['_XY_up']
            # Approaching_coord
            tmp2 = self.get_param_KJH4('BND_Met2Layer_Drain_connect_inv')
            approaching_coord = tmp2[0][0]['_XY_up']
            # Sref coord
            tmp3 = self.get_param_KJH4('BND_Met2Layer_Drain_connect_inv')
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            # Define
            self._DesignParameter['BND_Met2Layer_Drain_connect_inv']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### POLY_Layer_Gate pmos
        # Define Boundary_element
        self._DesignParameter['BND_POLayer_Hrz_Gate_Pmos'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Pmos_inv', 'BND_POLayerPINDrawing')
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_POLayer_Hrz_Gate_Pmos']['_YWidth'] = tmp1[0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Pmos_inv', 'BND_POLayer')

        self._DesignParameter['BND_POLayer_Hrz_Gate_Pmos']['_XWidth'] = abs(tmp[0][-1][0]['_XY_right'][0] - tmp[0][0][0]['_XY_left'][0])

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_POLayer_Hrz_Gate_Pmos']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Pmos_inv', 'BND_POLayer')
        target_coord = tmp1[0][0][0]['_XY_down_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_POLayer_Hrz_Gate_Pmos')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_POLayer_Hrz_Gate_Pmos')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_POLayer_Hrz_Gate_Pmos']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### POLY_Layer_Gate nmos
        # Define Boundary_element
        self._DesignParameter['BND_POLayer_Hrz_Gate_Nmos'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Nmos_inv', 'BND_POLayerPINDrawing')
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_POLayer_Hrz_Gate_Nmos']['_YWidth'] = tmp1[0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Nmos_inv', 'BND_POLayer')

        self._DesignParameter['BND_POLayer_Hrz_Gate_Nmos']['_XWidth'] = abs(
            tmp[0][-1][0]['_XY_right'][0] - tmp[0][0][0]['_XY_left'][0])

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_POLayer_Hrz_Gate_Nmos']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Nmos_inv', 'BND_POLayer')
        target_coord = tmp1[0][0][0]['_XY_up_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_POLayer_Hrz_Gate_Nmos')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_POLayer_Hrz_Gate_Nmos')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_POLayer_Hrz_Gate_Nmos']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### POLY_Metal1 CA
        ## ################################################################################################################### _Gate_ViaM0M1 pmos
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 0
        _Caculation_Parameters['_Layer2'] = 1
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Gate_ViaM0M1_Pmos'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_Gate_ViaM0M1_Pmos'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Gate_ViaM0M1_Pmos']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Gate_ViaM0M1_Pmos']['_Angle'] = 0

        # Calculate _COY
        _Caculation_Parameters['_COY'] = 1

        # Calculate _COX
        # Calculate Number of V1
        tmp = self.get_param_KJH4('BND_POLayer_Hrz_Gate_Pmos')
        M1_Xwidth = tmp[0][0]['_Xwidth']
        Num_V1 = int((M1_Xwidth - 2 * 4) / (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))
        # Define Num of V1
        if Num_V1 < 2:
            _Caculation_Parameters['_COX'] = 2
        else:
            _Caculation_Parameters['_COX'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Gate_ViaM0M1_Pmos']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Gate_ViaM0M1_Pmos']['_XYCoordinates'] = [[0, 0]]

        # For num of M1 in Nmos

        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_POLayer_Hrz_Gate_Pmos')
        target_coord = tmp1[0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Gate_ViaM0M1_Pmos', 'SRF_ViaM0M1', 'BND_POLayer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Gate_ViaM0M1_Pmos')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['SRF_Gate_ViaM0M1_Pmos']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### POLY_Metal1 CA
        ## ################################################################################################################### _Gate_ViaM0M1 nmos
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 0
        _Caculation_Parameters['_Layer2'] = 1
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Gate_ViaM0M1_Nmos'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_Gate_ViaM0M1_Nmos'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Gate_ViaM0M1_Nmos']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Gate_ViaM0M1_Nmos']['_Angle'] = 0

        # Calculate _COY
        _Caculation_Parameters['_COY'] = 1

        # Calculate _COX
        # Calculate Number of V1
        tmp = self.get_param_KJH4('BND_POLayer_Hrz_Gate_Nmos')
        M1_Xwidth = tmp[0][0]['_Xwidth']
        Num_V1 = int((M1_Xwidth - 2 * 4) / (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))
        # Define Num of V1
        if Num_V1 < 2:
            _Caculation_Parameters['_COX'] = 2
        else:
            _Caculation_Parameters['_COX'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Gate_ViaM0M1_Nmos']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Gate_ViaM0M1_Nmos']['_XYCoordinates'] = [[0, 0]]

        # For num of M1 in Nmos

        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_POLayer_Hrz_Gate_Nmos')
        target_coord = tmp1[0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Gate_ViaM0M1_Nmos', 'SRF_ViaM0M1', 'BND_POLayer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Gate_ViaM0M1_Nmos')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['SRF_Gate_ViaM0M1_Nmos']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Metal1_Gate_connect
        # Define Boundary_element
        self._DesignParameter['BND_Met1Layer_Gate_connect'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Gate_ViaM0M1_Pmos','SRF_ViaM0M1', 'BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_Gate_ViaM0M1_Nmos', 'SRF_ViaM0M1', 'BND_Met1Layer')
        tmp3 = self.get_param_KJH4('BND_Met2Layer_Drain_connect_inv')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met1Layer_Gate_connect']['_YWidth'] = abs(tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met1Layer_Gate_connect']['_XWidth'] = tmp3[0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met1Layer_Gate_connect']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Gate_ViaM0M1_Pmos', 'SRF_ViaM0M1', 'BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_up']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Met1Layer_Gate_connect')
        approaching_coord = tmp2[0][0]['_XY_up']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Met1Layer_Gate_connect')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Met1Layer_Gate_connect']['_XYCoordinates'] = tmpXY


        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(
            A03_NmosWithDummy_KJH4_YCH_TIA._NmosWithDummy_KJH3._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOSNumberofGate'] = _tg_NMOSNumberofGate
        _Caculation_Parameters['_NMOSChannelWidth'] = _tg_NMOSChannelWidth
        _Caculation_Parameters['_NMOSChannellength'] = _tg_NMOSChannellength
        _Caculation_Parameters['_GateSpacing'] = _tg_NMOSGateSpacing
        _Caculation_Parameters['_SDWidth'] = _tg_NMOSSDWidth
        _Caculation_Parameters['_XVT'] = _tg_NMOSXVT
        _Caculation_Parameters['_PCCrit'] = _tg_NMOSPCCrit
        _Caculation_Parameters['_Source_Via_TF'] = _tg_NMOSSource_Via_TF
        _Caculation_Parameters['_Drain_Via_TF'] = _tg_NMOSDrain_Via_TF
        _Caculation_Parameters['_NMOSDummy'] = _tg_NMOSDummy
        _Caculation_Parameters['_NMOSDummy_length'] = _tg_NMOSDummy_length
        _Caculation_Parameters['_NMOSDummy_placement'] = _tg_NMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Nmos_tg'] = self._SrefElementDeclaration(
            _DesignObj=A03_NmosWithDummy_KJH4_YCH_TIA._NmosWithDummy_KJH3(_DesignParameter=None,
                                                                          _Name='{}:SRF_Nmos_tg'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Nmos_tg']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos_tg']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos_tg']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos_tg']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Nmos_inv', 'BND_POLayer')
        target_coord = tmp1[0][0][0]['_XY_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Nmos_tg', 'BND_POLayer')
        approaching_coord = tmp2[0][-1][0]['_XY_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Nmos_tg')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)

        if (_inv_NMOSGateSpacing == None):
            _inv_NMOSGateSpacing = _DRCObj._PolygateMinSpace2
            _inv_GatetoGate = 2 * _inv_NMOSGateSpacing + _inv_NMOSChannellength
        else:
            _inv_GatetoGate = 2 * _inv_NMOSGateSpacing + _inv_NMOSChannellength

        New_Scoord[0] = New_Scoord[0] - _inv_GatetoGate
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Nmos_tg']['_XYCoordinates'] = tmpXY

        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(
            A04_PmosWithDummy_KJH3_YCH_TIA._PmosWithDummy_KJH3._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_PMOSNumberofGate'] = _tg_PMOSNumberofGate
        _Caculation_Parameters['_PMOSChannelWidth'] = _tg_PMOSChannelWidth
        _Caculation_Parameters['_PMOSChannellength'] = _tg_PMOSChannellength
        _Caculation_Parameters['_GateSpacing'] = _tg_PMOSGateSpacing
        _Caculation_Parameters['_SDWidth'] = _tg_PMOSSDWidth
        _Caculation_Parameters['_XVT'] = _tg_PMOSXVT
        _Caculation_Parameters['_PCCrit'] = _tg_PMOSPCCrit
        _Caculation_Parameters['_Source_Via_TF'] = _tg_PMOSSource_Via_TF
        _Caculation_Parameters['_Drain_Via_TF'] = _tg_PMOSDrain_Via_TF
        _Caculation_Parameters['_PMOSDummy'] = _tg_PMOSDummy
        _Caculation_Parameters['_PMOSDummy_length'] = _tg_PMOSDummy_length
        _Caculation_Parameters['_PMOSDummy_placement'] = _tg_PMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Pmos_tg'] = self._SrefElementDeclaration(
            _DesignObj=A04_PmosWithDummy_KJH3_YCH_TIA._PmosWithDummy_KJH3(_DesignParameter=None,
                                                                          _Name='{}:SRF_Pmos_tg'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Pmos_tg']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_tg']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_tg']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_tg']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Pmos_inv', 'BND_POLayer')
        target_coord = tmp1[0][0][0]['_XY_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Pmos_tg', 'BND_POLayer')
        approaching_coord = tmp2[0][-1][0]['_XY_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pmos_tg')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)

        if (_inv_PMOSGateSpacing == None):
            _inv_PMOSGateSpacing = _DRCObj._PolygateMinSpace2
            _inv_GatetoGate = 2 * _inv_PMOSGateSpacing + _inv_PMOSChannellength
        else:
            _inv_GatetoGate = 2 * _inv_PMOSGateSpacing + _inv_PMOSChannellength

        New_Scoord[0] = New_Scoord[0] - _inv_GatetoGate
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Pmos_tg']['_XYCoordinates'] = tmpXY

        # PP layer 연장 연결
        # Define Boundary_element
        self._DesignParameter['BND_PPLayer_Extension'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[],
            )

        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Pmos_inv', 'BND_PPLayer')

        self._DesignParameter['BND_PPLayer_Extension']['_YWidth'] = tmp1[0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Pmos_inv',  'BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_Pmos_tg',  'BND_PPLayer')

        self._DesignParameter['BND_PPLayer_Extension']['_XWidth'] = abs(tmp1[0][0][0]['_XY_right'][0] - tmp2[0][0][0]['_XY_left'][0])

        # Define coord
        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['BND_PPLayer_Extension']['_XYCoordinates'] = [[0, 0]]

        # Calculate1
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Pmos_inv', 'BND_PPLayer')
        target_coord = tmp1[0][0][0]['_XY_up_right']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_PPLayer_Extension')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_PPLayer_Extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['BND_PPLayer_Extension']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Metal2_Drain_connect tg
        # Define Boundary_element
        self._DesignParameter['BND_Met2Layer_Drain_connect_tg'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Pmos_tg', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        tmp2 = self.get_param_KJH4('SRF_Nmos_tg', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met2Layer_Drain_connect_tg']['_YWidth'] = abs(
            tmp1[0][0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met2Layer_Drain_connect_tg']['_XWidth'] = tmp1[0][0][0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met2Layer_Drain_connect_tg']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        # print(tmp1[0])
        for i in range(0, len(tmp1[0])):
            # Calculate
            # Target_coord
            tmp1 = self.get_param_KJH4('SRF_Pmos_tg', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
            target_coord = tmp1[0][i][0][0][0]['_XY_up']
            # Approaching_coord
            tmp2 = self.get_param_KJH4('BND_Met2Layer_Drain_connect_tg')
            approaching_coord = tmp2[0][0]['_XY_up']
            # Sref coord
            tmp3 = self.get_param_KJH4('BND_Met2Layer_Drain_connect_tg')
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            # Define
            self._DesignParameter['BND_Met2Layer_Drain_connect_tg']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Metal2_Drain_connect tg
        # Define Boundary_element
        self._DesignParameter['BND_Met2Layer_Source_connect_tg'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Pmos_tg', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        tmp2 = self.get_param_KJH4('SRF_Nmos_tg', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met2Layer_Source_connect_tg']['_YWidth'] = abs(
            tmp1[0][0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met2Layer_Source_connect_tg']['_XWidth'] = tmp1[0][0][0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met2Layer_Source_connect_tg']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        for i in range(0, len(tmp1[0])):
            # Calculate
            # Target_coord
            tmp1 = self.get_param_KJH4('SRF_Pmos_tg', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
            target_coord = tmp1[0][i][0][0][0]['_XY_up']
            # Approaching_coord
            tmp2 = self.get_param_KJH4('BND_Met2Layer_Source_connect_tg')
            approaching_coord = tmp2[0][0]['_XY_up']
            # Sref coord
            tmp3 = self.get_param_KJH4('BND_Met2Layer_Source_connect_tg')
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            # Define
            self._DesignParameter['BND_Met2Layer_Source_connect_tg']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### POLY_Layer_Gate pmos tg
        # Define Boundary_element
        self._DesignParameter['BND_POLayer_Hrz_Gate_Pmos_tg'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Pmos_tg', 'BND_POLayerPINDrawing')
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_POLayer_Hrz_Gate_Pmos_tg']['_YWidth'] = tmp1[0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Pmos_tg', 'BND_POLayer')

        self._DesignParameter['BND_POLayer_Hrz_Gate_Pmos_tg']['_XWidth'] = abs(
            tmp[0][-1][0]['_XY_right'][0] - tmp[0][0][0]['_XY_left'][0])

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_POLayer_Hrz_Gate_Pmos_tg']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Pmos_tg', 'BND_POLayer')
        target_coord = tmp1[0][0][0]['_XY_down_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_POLayer_Hrz_Gate_Pmos_tg')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_POLayer_Hrz_Gate_Pmos_tg')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_POLayer_Hrz_Gate_Pmos_tg']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### POLY_Layer_Gate nmos tg
        # Define Boundary_element
        self._DesignParameter['BND_POLayer_Hrz_Gate_Nmos_tg'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Nmos_tg', 'BND_POLayerPINDrawing')
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_POLayer_Hrz_Gate_Nmos_tg']['_YWidth'] = tmp1[0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Nmos_tg', 'BND_POLayer')

        self._DesignParameter['BND_POLayer_Hrz_Gate_Nmos_tg']['_XWidth'] = abs(
            tmp[0][-1][0]['_XY_right'][0] - tmp[0][0][0]['_XY_left'][0])

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_POLayer_Hrz_Gate_Nmos_tg']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Nmos_tg', 'BND_POLayer')
        target_coord = tmp1[0][0][0]['_XY_up_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_POLayer_Hrz_Gate_Nmos_tg')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_POLayer_Hrz_Gate_Nmos_tg')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_POLayer_Hrz_Gate_Nmos_tg']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### POLY_Metal1 CA
        ## ################################################################################################################### _Gate_ViaM0M1 nmos tg
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 0
        _Caculation_Parameters['_Layer2'] = 1
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Gate_ViaM0M1_Nmos_tg'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_Gate_ViaM0M1_Nmos_tg'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Gate_ViaM0M1_Nmos_tg']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Gate_ViaM0M1_Nmos_tg']['_Angle'] = 0

        # Calculate _COY
        _Caculation_Parameters['_COY'] = 1

        # Calculate _COX
        # Calculate Number of V1
        tmp = self.get_param_KJH4('BND_POLayer_Hrz_Gate_Nmos_tg')
        M1_Xwidth = tmp[0][0]['_Xwidth']
        Num_V1 = int((M1_Xwidth - 2 * 4) / (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))
        # Define Num of V1
        if Num_V1 < 2:
            _Caculation_Parameters['_COX'] = 2
        else:
            _Caculation_Parameters['_COX'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Gate_ViaM0M1_Nmos_tg']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Gate_ViaM0M1_Nmos_tg']['_XYCoordinates'] = [[0, 0]]

        # For num of M1 in Nmos

        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_POLayer_Hrz_Gate_Nmos_tg')
        target_coord = tmp1[0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Gate_ViaM0M1_Nmos_tg', 'SRF_ViaM0M1', 'BND_POLayer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Gate_ViaM0M1_Nmos_tg')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['SRF_Gate_ViaM0M1_Nmos_tg']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### POLY_Metal1 CA
        ## ################################################################################################################### _Gate_ViaM0M1 pmos tg
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 0
        _Caculation_Parameters['_Layer2'] = 1
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Gate_ViaM0M1_Pmos_tg'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_Gate_ViaM0M1_Pmos_tg'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Gate_ViaM0M1_Pmos_tg']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Gate_ViaM0M1_Pmos_tg']['_Angle'] = 0

        # Calculate _COY
        _Caculation_Parameters['_COY'] = 1

        # Calculate _COX
        # Calculate Number of V1
        tmp = self.get_param_KJH4('BND_POLayer_Hrz_Gate_Nmos_tg')
        M1_Xwidth = tmp[0][0]['_Xwidth']
        Num_V1 = int((M1_Xwidth - 2 * 4) / (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))
        # Define Num of V1
        if Num_V1 < 2:
            _Caculation_Parameters['_COX'] = 2
        else:
            _Caculation_Parameters['_COX'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Gate_ViaM0M1_Pmos_tg']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Gate_ViaM0M1_Pmos_tg']['_XYCoordinates'] = [[0, 0]]

        # For num of M1 in Nmos

        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_POLayer_Hrz_Gate_Pmos_tg')
        target_coord = tmp1[0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Gate_ViaM0M1_Pmos_tg', 'SRF_ViaM0M1', 'BND_POLayer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Gate_ViaM0M1_Pmos_tg')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['SRF_Gate_ViaM0M1_Pmos_tg']['_XYCoordinates'] = tmpXY

        # DRC 검증 완료
        ## ################################################################################################################### Metal3_Layer_Source tg
        # Define Boundary_element
        self._DesignParameter['BND_Metal3Layer_Hrz_Source_tg'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[],
        )

        # Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('SRF_Pmos_tg', 'BND_Met1Layer_Source')
        self._DesignParameter['BND_Metal3Layer_Hrz_Source_tg']['_YWidth'] = tmp[0][0][0]['_Ywidth'] / 4

        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Pmos_tg', 'BND_Met1Layer_Source')

        self._DesignParameter['BND_Metal3Layer_Hrz_Source_tg']['_XWidth'] = tmp[0][0][0]['_Xwidth']
        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal3Layer_Hrz_Source_tg']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        if (_tg_PMOSNumberofGate % 2 == 1):
            for i in range(0, int(_tg_PMOSNumberofGate / 2) + 1):
                # Calculate
                # Target_coord
                tmp1 = self.get_param_KJH4('SRF_Pmos_tg', 'BND_Met1Layer_Source')
                target_coord = tmp1[0][i][0]['_XY_up_left']
                # Approaching_coord
                tmp2 = self.get_param_KJH4('BND_Metal3Layer_Hrz_Source_tg')
                approaching_coord = tmp2[0][0]['_XY_up_left']
                # Sref coord
                tmp3 = self.get_param_KJH4('BND_Metal3Layer_Hrz_Source_tg')
                Scoord = tmp3[0][0]['_XY_origin']
                # Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
                # Define
                self._DesignParameter['BND_Metal3Layer_Hrz_Source_tg']['_XYCoordinates'] = tmpXY
        else:
            for i in range(0, int(_tg_PMOSNumberofGate / 2) + 1):
                # Calculate
                # Target_coord
                tmp1 = self.get_param_KJH4('SRF_Pmos_tg', 'BND_Met1Layer_Source')
                target_coord = tmp1[0][i][0]['_XY_up_left']
                # Approaching_coord
                tmp2 = self.get_param_KJH4('BND_Metal3Layer_Hrz_Source_tg')
                approaching_coord = tmp2[0][0]['_XY_up_left']
                # Sref coord
                tmp3 = self.get_param_KJH4('BND_Metal3Layer_Hrz_Source_tg')
                Scoord = tmp3[0][0]['_XY_origin']
                # Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
                # Define
                self._DesignParameter['BND_Metal3Layer_Hrz_Source_tg']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Source_ViaM2M3 tg
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Source_ViaM2M3_tg'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                        _Name='{}:SRF_Source_ViaM2M3_tg'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Source_ViaM2M3_tg']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Source_ViaM2M3_tg']['_Angle'] = 0

        # Calcuate _COX
        _Caculation_Parameters['_COX'] = 1

        # Calcuate _COY
        tmp = self.get_param_KJH4('BND_Metal3Layer_Hrz_Source_tg')
        M3_ywidth = tmp[0][0]['_Ywidth']
        Num_V1 = int(
            (M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COY'] = 2
        else:
            _Caculation_Parameters['_COY'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Source_ViaM2M3_tg']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Source_ViaM2M3_tg']['_XYCoordinates'] = [[0, 0]]

        if (_tg_PMOSNumberofGate % 2 == 1):
            for i in range(0, int(_tg_PMOSNumberofGate / 2) + 1):
                # Calculate
                # Target_coord
                tmp1 = self.get_param_KJH4('BND_Metal3Layer_Hrz_Source_tg')
                target_coord = tmp1[i][0]['_XY_up_left']
                # Approaching_coord
                tmp2 = self.get_param_KJH4('SRF_Source_ViaM2M3_tg', 'SRF_ViaM2M3', 'BND_Met3Layer')
                approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
                # Sref coord
                tmp3 = self.get_param_KJH4('SRF_Source_ViaM2M3_tg')
                Scoord = tmp3[0][0]['_XY_origin']
                # Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
                # Define
                self._DesignParameter['SRF_Source_ViaM2M3_tg']['_XYCoordinates'] = tmpXY
        else:
            for i in range(0, int(_tg_PMOSNumberofGate / 2) + 1):
                # Calculate
                # Target_coord
                tmp1 = self.get_param_KJH4('BND_Metal3Layer_Hrz_Source_tg')
                target_coord = tmp1[i][0]['_XY_up_left']
                # Approaching_coord
                tmp2 = self.get_param_KJH4('SRF_Source_ViaM2M3_tg', 'SRF_ViaM2M3', 'BND_Met3Layer')
                approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
                # Sref coord
                tmp3 = self.get_param_KJH4('SRF_Source_ViaM2M3_tg')
                Scoord = tmp3[0][0]['_XY_origin']
                # Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
                # Define
                self._DesignParameter['SRF_Source_ViaM2M3_tg']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Metal3_Layer_Drain tg
        # Define Boundary_element
        self._DesignParameter['BND_Metal3Layer_Hrz_Drain_tg'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        # Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('SRF_Pmos_tg', 'BND_Met1Layer_Drain')
        self._DesignParameter['BND_Metal3Layer_Hrz_Drain_tg']['_YWidth'] = tmp[0][0][0]['_Ywidth'] / 4

        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Pmos_tg', 'BND_Met1Layer_Drain')

        self._DesignParameter['BND_Metal3Layer_Hrz_Drain_tg']['_XWidth'] = tmp[0][0][0]['_Xwidth']
        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal3Layer_Hrz_Drain_tg']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        if (_tg_PMOSNumberofGate % 2 == 1):
            for i in range(0, int(_tg_PMOSNumberofGate / 2) + 1):
                # Calculate
                # Target_coord
                tmp1 = self.get_param_KJH4('SRF_Nmos_tg', 'BND_Met1Layer_Drain')
                target_coord = tmp1[0][i][0]['_XY_down_left']
                # Approaching_coord
                tmp2 = self.get_param_KJH4('BND_Metal3Layer_Hrz_Drain_tg')
                approaching_coord = tmp2[0][0]['_XY_down_left']
                # Sref coord
                tmp3 = self.get_param_KJH4('BND_Metal3Layer_Hrz_Drain_tg')
                Scoord = tmp3[0][0]['_XY_origin']
                # Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
                # Define
                self._DesignParameter['BND_Metal3Layer_Hrz_Drain_tg']['_XYCoordinates'] = tmpXY
        else:
            for i in range(0, int(_tg_PMOSNumberofGate / 2)):
                # Calculate
                # Target_coord
                tmp1 = self.get_param_KJH4('SRF_Pmos_tg', 'BND_Met1Layer_Drain')
                target_coord = tmp1[0][i][0]['_XY_down_left']
                # Approaching_coord
                tmp2 = self.get_param_KJH4('BND_Metal3Layer_Hrz_Drain_tg')
                approaching_coord = tmp2[0][0]['_XY_down_left']
                # Sref coord
                tmp3 = self.get_param_KJH4('BND_Metal3Layer_Hrz_Drain_tg')
                Scoord = tmp3[0][0]['_XY_origin']
                # Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
                # Define
                self._DesignParameter['BND_Metal3Layer_Hrz_Drain_tg']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Drain_ViaM2M3 tg
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(
            A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Drain_ViaM2M3_tg'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_Drain_ViaM2M3_tg'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Drain_ViaM2M3_tg']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Drain_ViaM2M3_tg']['_Angle'] = 0

        # Calcuate _COX
        _Caculation_Parameters['_COX'] = 1

        # Calcuate _COY
        tmp = self.get_param_KJH4('BND_Metal3Layer_Hrz_Drain_tg')
        M3_ywidth = tmp[0][0]['_Ywidth']
        Num_V1 = int(
            (M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COY'] = 2
        else:
            _Caculation_Parameters['_COY'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Drain_ViaM2M3_tg']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Drain_ViaM2M3_tg']['_XYCoordinates'] = [[0, 0]]

        if (_tg_PMOSNumberofGate % 2 == 1):
            for i in range(0, int(_tg_PMOSNumberofGate / 2) + 1):
                # Calculate
                # Target_coord
                tmp1 = self.get_param_KJH4('BND_Metal3Layer_Hrz_Drain_tg')
                target_coord = tmp1[i][0]['_XY_up_left']
                # Approaching_coord
                tmp2 = self.get_param_KJH4('SRF_Drain_ViaM2M3_tg', 'SRF_ViaM2M3', 'BND_Met3Layer')
                approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
                # Sref coord
                tmp3 = self.get_param_KJH4('SRF_Drain_ViaM2M3_tg')
                Scoord = tmp3[0][0]['_XY_origin']
                # Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
                # Define
                self._DesignParameter['SRF_Drain_ViaM2M3_tg']['_XYCoordinates'] = tmpXY
        else:
            for i in range(0, int(_tg_PMOSNumberofGate / 2)):
                # Calculate
                # Target_coord
                tmp1 = self.get_param_KJH4('BND_Metal3Layer_Hrz_Drain_tg')
                target_coord = tmp1[i][0]['_XY_up_left']
                # Approaching_coord
                tmp2 = self.get_param_KJH4('SRF_Drain_ViaM2M3_tg', 'SRF_ViaM2M3', 'BND_Met3Layer')
                approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
                # Sref coord
                tmp3 = self.get_param_KJH4('SRF_Drain_ViaM2M3_tg')
                Scoord = tmp3[0][0]['_XY_origin']
                # Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
                # Define
                self._DesignParameter['SRF_Drain_ViaM2M3_tg']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Metal3_Layer_Source_connect_tg
        # Define Boundary_element
        self._DesignParameter['BND_Metal3Layer_connect_Source_tg'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[],
        )
        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Source_ViaM2M3_tg', 'SRF_ViaM2M3', 'BND_Met3Layer')
        self._DesignParameter['BND_Metal3Layer_connect_Source_tg']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal3Layer_connect_Source_tg']['_XWidth'] = abs(tmp1[-1][0][0][0]['_XY_right'][0]-tmp1[0][0][0][0]['_XY_left'][0])

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal3Layer_connect_Source_tg']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Source_ViaM2M3_tg', 'SRF_ViaM2M3', 'BND_Met3Layer')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal3Layer_connect_Source_tg')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal3Layer_connect_Source_tg')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal3Layer_connect_Source_tg']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Metal3_Layer_Drain_connect_tg
        # Define Boundary_element
        self._DesignParameter['BND_Metal3Layer_connect_Drain_tg'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[],
        )
        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Drain_ViaM2M3_tg', 'SRF_ViaM2M3', 'BND_Met3Layer')
        self._DesignParameter['BND_Metal3Layer_connect_Drain_tg']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal3Layer_connect_Drain_tg']['_XWidth'] = abs(tmp1[-1][0][0][0]['_XY_right'][0] - tmp1[0][0][0][0]['_XY_left'][0])

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal3Layer_connect_Drain_tg']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Drain_ViaM2M3_tg', 'SRF_ViaM2M3', 'BND_Met3Layer')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal3Layer_connect_Drain_tg')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal3Layer_connect_Drain_tg')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal3Layer_connect_Drain_tg']['_XYCoordinates'] = tmpXY

        #DRC 검증 완료
        ## ################################################################################################################### Metal1_tg_nmos_Gate, inv_nmos_gate_connect
        # Define Boundary_element
        self._DesignParameter['BND_Met1Layer_tg_nmos_Gate_inv_nmos_Gate_connect'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Gate_ViaM0M1_Nmos', 'SRF_ViaM0M1', 'BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_Gate_ViaM0M1_Nmos_tg', 'SRF_ViaM0M1', 'BND_Met1Layer')
        tmp3 = self.get_param_KJH4('BND_Met2Layer_Drain_connect_inv')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met1Layer_tg_nmos_Gate_inv_nmos_Gate_connect']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met1Layer_tg_nmos_Gate_inv_nmos_Gate_connect']['_XWidth'] = abs(
            tmp1[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0])

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met1Layer_tg_nmos_Gate_inv_nmos_Gate_connect']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Gate_ViaM0M1_Nmos', 'SRF_ViaM0M1', 'BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_up_right']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Met1Layer_tg_nmos_Gate_inv_nmos_Gate_connect')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Met1Layer_tg_nmos_Gate_inv_nmos_Gate_connect')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Met1Layer_tg_nmos_Gate_inv_nmos_Gate_connect']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Metal1_tg_pmos_Gate, inv_pmos_nmos_drain_connect
        # Define Boundary_element
        self._DesignParameter['BND_Met1Layer_tg_pmos_Gate_inv_pmos_nmos_Drain_connect'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Gate_ViaM0M1_Pmos_tg', 'SRF_ViaM0M1', 'BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_Pmos_inv', 'SRF_Source_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met1Layer_tg_pmos_Gate_inv_pmos_nmos_Drain_connect']['_YWidth'] = 244

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met1Layer_tg_pmos_Gate_inv_pmos_nmos_Drain_connect']['_XWidth'] = abs(
            tmp2[0][0][0][0][0]['_XY_right'][0] - tmp1[0][0][0][0]['_XY_left'][0])

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met1Layer_tg_pmos_Gate_inv_pmos_nmos_Drain_connect']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Gate_ViaM0M1_Pmos_tg', 'SRF_ViaM0M1', 'BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Met1Layer_tg_pmos_Gate_inv_pmos_nmos_Drain_connect')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Met1Layer_tg_pmos_Gate_inv_pmos_nmos_Drain_connect')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Met1Layer_tg_pmos_Gate_inv_pmos_nmos_Drain_connect']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Metal2_inv_pmos_nmos_drain_connect
        # Define Boundary_element
        self._DesignParameter['BND_Met2Layer_inv_pmos_nmos_Drain_connect'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Met2Layer_Drain_connect_inv')
        tmp2 = self.get_param_KJH4('SRF_Pmos_inv', 'BND_POLayer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met2Layer_inv_pmos_nmos_Drain_connect']['_YWidth'] = 244

        if (_inv_PMOSGateSpacing == None):
            _inv_PMOSGateSpacing = _DRCObj._PolygateMinSpace2
        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met2Layer_inv_pmos_nmos_Drain_connect']['_XWidth'] = abs(
            tmp1[-1][0]['_XY_right'][0] - tmp2[0][0][0]['_XY_left'][0] + _inv_PMOSGateSpacing)

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met2Layer_inv_pmos_nmos_Drain_connect']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        # Calculate
        # Target_coord
        tmp11 = self.get_param_KJH4('SRF_Pmos_inv', 'BND_POLayer')
        tmp12 = self.get_param_KJH4('BND_Met1Layer_tg_pmos_Gate_inv_pmos_nmos_Drain_connect')
        target_coordx = tmp11[0][0][0]['_XY_left'][0] - _inv_PMOSGateSpacing
        target_coordy = tmp12[0][0]['_XY_right'][1]
        target_coord = [target_coordx, target_coordy]
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Met2Layer_inv_pmos_nmos_Drain_connect')
        approaching_coord = tmp2[0][0]['_XY_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Met2Layer_inv_pmos_nmos_Drain_connect')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Met2Layer_inv_pmos_nmos_Drain_connect']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### tg_pmos_Gate, inv_pmos_nmos_drain connect ViaM1M2
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_tg_pmos_Gate_inv_pmos_nmos_drain_ViaM1M2'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None, _Name='{}:SRF_tg_pmos_Gate_inv_pmos_nmos_drain_ViaM1M2'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_tg_pmos_Gate_inv_pmos_nmos_drain_ViaM1M2']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_tg_pmos_Gate_inv_pmos_nmos_drain_ViaM1M2']['_Angle'] = 0

        # Calcuate _COY
        _Caculation_Parameters['_COY'] = 2

        # Calcuate _COX
        # tmp = self.get_param_KJH4('SRF_Nmos_Tr2Tr3', 'SRF_Nmos_Tr2', 'BND_Metal1Layer_Connect_Gate_extension')
        # M3_xwidth = tmp[0][0][0][0]['_Xwidth']
        # Num_V1 = int(
        #     (M3_xwidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        # # Define Num of COY
        # if Num_V1 < 2:
        #     _Caculation_Parameters['_COX'] = 2
        # else:
        #     _Caculation_Parameters['_COX'] = Num_V1
        _Caculation_Parameters['_COX'] = 1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_tg_pmos_Gate_inv_pmos_nmos_drain_ViaM1M2']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_tg_pmos_Gate_inv_pmos_nmos_drain_ViaM1M2']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Met2Layer_inv_pmos_nmos_Drain_connect')
        target_coord = tmp1[0][0]['_XY_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_tg_pmos_Gate_inv_pmos_nmos_drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_tg_pmos_Gate_inv_pmos_nmos_drain_ViaM1M2')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_tg_pmos_Gate_inv_pmos_nmos_drain_ViaM1M2']['_XYCoordinates'] = tmpXY

        # 04/23 DRC 검증 완료 LVS는 나중에 합쳐서 한 번에 진행


        print('##############################')
        print('##     Calculation_End    ##')
        print('##############################')

## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from TIA_Proj_YCH.Library_and_Engine.Private import MyInfo_YCH
    from TIA_Proj_YCH.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_A50_TIA_TG_v17'
    cellname = 'A50_TIA_TG'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        # NMOS inverter
        _inv_NMOSNumberofGate=2,
        _inv_NMOSChannelWidth=500,
        _inv_NMOSChannellength=150,
        _inv_NMOSGateSpacing=None,
        _inv_NMOSSDWidth=None,
        _inv_NMOSXVT	= 'EG',
        _inv_NMOSPCCrit		= None,

        # Source_node_ViaM1M2
        _inv_NMOSSource_Via_TF= True,

        # Drain_node_ViaM1M2
        _inv_NMOSDrain_Via_TF= True,

        # POLY dummy setting
        _inv_NMOSDummy= True  , # TF
        # if _PMOSDummy == True
        _inv_NMOSDummy_length = None, # None/Value
        _inv_NMOSDummy_placement = None, # None/Up/Dn/

        # PMOS inverter
        _inv_PMOSNumberofGate=2,
        _inv_PMOSChannelWidth=1000,
        _inv_PMOSChannellength=150,
        _inv_PMOSGateSpacing=None,
        _inv_PMOSSDWidth=None,
        _inv_PMOSXVT='EG',
        _inv_PMOSPCCrit=None,

        # Source_node_ViaM1M2
        _inv_PMOSSource_Via_TF=True,

        # Drain_node_ViaM1M2
        _inv_PMOSDrain_Via_TF=True,

        # POLY dummy setting
        _inv_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _inv_PMOSDummy_length=None,  # None/Value
        _inv_PMOSDummy_placement=None,  # None/Up/Dn/

        # NMOS tg
        _tg_NMOSNumberofGate=100,
        _tg_NMOSChannelWidth=500,
        _tg_NMOSChannellength=150,
        _tg_NMOSGateSpacing=None,
        _tg_NMOSSDWidth=None,
        _tg_NMOSXVT	= 'EG',
        _tg_NMOSPCCrit		= None,

        # Source_node_ViaM1M2
        _tg_NMOSSource_Via_TF= True,

        # Drain_node_ViaM1M2
        _tg_NMOSDrain_Via_TF= True,

        # POLY dummy setting
        _tg_NMOSDummy= True  , # TF
        # if _PMOSDummy == True
        _tg_NMOSDummy_length = None, # None/Value
        _tg_NMOSDummy_placement = None, # None/Up/Dn/

        # PMOS inverter
        _tg_PMOSNumberofGate=100,
        _tg_PMOSChannelWidth=1000,
        _tg_PMOSChannellength=150,
        _tg_PMOSGateSpacing=None,
        _tg_PMOSSDWidth=None,
        _tg_PMOSXVT='EG',
        _tg_PMOSPCCrit=None,

        # Source_node_ViaM1M2
        _tg_PMOSSource_Via_TF=True,

        # Drain_node_ViaM1M2
        _tg_PMOSDrain_Via_TF=True,

        # POLY dummy setting
        _tg_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _tg_PMOSDummy_length=None,  # None/Value
        _tg_PMOSDummy_placement=None,  # None/Up/Dn/

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
    LayoutObj = _TIA_TG_YCH(_DesignParameter=None, _Name=cellname)
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
    # Checker.lib_deletion()
    Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()
    print('#############################      Finished      ################################')
# end of 'main():' ---------------------------------------------------------------------------------------------