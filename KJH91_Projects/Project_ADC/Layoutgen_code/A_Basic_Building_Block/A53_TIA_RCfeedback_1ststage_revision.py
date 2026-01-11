from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC_EGFET

import numpy as np
import copy
import math

from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A52_Res_Parallel
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A51_Runit_Switch
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_HDVNCAP_Array
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_TG_Switch
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2_YCH

class _TIA_RCfeedback_1ststage(StickDiagram_KJH1._StickDiagram_KJH):

    _ParametersForDesignCalculation = dict(
        # Parallel Res
        _Par_ResWidth=None,
        _Par_ResLength=None,
        _Par_SeriesStripes=None,
        _Par_ParallelStripes=None,

        # Series Res
        _Ser_ResWidth=None,
        _Ser_ResLength=None,
        _Ser_SeriesStripes=None,
        _Ser_ParallelStripes=None,

        ### TG NMOS PMOS
        _TG_NumberofGate=None,  # number
        _TG_NMOSChannelWidth=None,  # number
        _TG_PMOSChannelWidth=None,
        _TG_Channellength=None,  # number
        _TG_XVT			= None, # 'XVT' ex)SLVT LVT RVT HVT EG
        _INV_NumberofGate=None,
        _NMOS_Pbody_NumCont=None,
        _PMOS_Nbody_NumCont=None,

        _Parallel_Stack=None,

        # Cap_1st
        _Length_1st=9000,
        _LayoutOption_1st=[2, 3, 4],
        _NumFigPair_1st=20,
        _Array_1st_row=1,
        _Array_1st_col=1,
        _Cbot_Ctop_metalwidth_1st=500,


    )

    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _Name=self._NameDeclaration(_Name=_Name),
                _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                _XYcoordAsCent=dict(_XYcoordAsCent=0),
                _XYCoordinatePort1Routing=dict(_DesignParametertype=7, _XYCoordinates=[]),
                _XYCoordinatePort2Routing=dict(_DesignParametertype=7, _XYCoordinates=[]),
            )

        ## ################################################################################################################################################ _CalculateDesignParameter

    def _CalculateDesignParameter(self,
                                  # Parallel Res
                                  _Par_ResWidth=None,
                                  _Par_ResLength=None,
                                  _Par_SeriesStripes=None,
                                  _Par_ParallelStripes=None,

                                  # Series Res
                                  _Ser_ResWidth=None,
                                  _Ser_ResLength=None,
                                  _Ser_SeriesStripes=None,
                                  _Ser_ParallelStripes=None,

                                  ### TG NMOS PMOS
                                  _TG_NumberofGate=None,  # number
                                  _TG_NMOSChannelWidth=None,  # number
                                  _TG_PMOSChannelWidth=None,
                                  _TG_Channellength=None,  # number
                                  _TG_XVT	= None  , # 'XVT' ex)SLVT LVT RVT HVT EG
                                  _INV_NumberofGate=None,
                                  _NMOS_Pbody_NumCont=None,
                                  _PMOS_Nbody_NumCont=None,

                                  _Parallel_Stack=None,

                                  # Cap_1st
                                  _Length_1st=9000,
                                  _LayoutOption_1st=[2, 3, 4],
                                  _NumFigPair_1st=20,
                                  _Array_1st_row=1,
                                  _Array_1st_col=1,
                                  _Cbot_Ctop_metalwidth_1st=500,

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

        _Caculation_Parameters = copy.deepcopy(A52_Res_Parallel._Res_Parallel._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_ResWidth'] = _Par_ResWidth
        _Caculation_Parameters['_ResLength'] = _Par_ResLength
        _Caculation_Parameters['_CONUMX'] = None
        _Caculation_Parameters['_CONUMY'] = None
        _Caculation_Parameters['_SeriesStripes'] = _Par_SeriesStripes
        _Caculation_Parameters['_ParallelStripes'] = _Par_ParallelStripes

        _Caculation_Parameters['_TG_NumberofGate'] = _TG_NumberofGate
        _Caculation_Parameters['_TG_NMOSChannelWidth'] = _TG_NMOSChannelWidth
        _Caculation_Parameters['_TG_PMOSChannelWidth'] = _TG_PMOSChannelWidth
        _Caculation_Parameters['_TG_Channellength'] = _TG_Channellength
        _Caculation_Parameters['_TG_XVT'] = _TG_XVT
        _Caculation_Parameters['_INV_NumberofGate'] = _INV_NumberofGate
        _Caculation_Parameters['_NMOS_Pbody_NumCont'] = _NMOS_Pbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_NumCont'] = _PMOS_Nbody_NumCont

        _Caculation_Parameters['_Parallel_Stack'] = _Parallel_Stack

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Res_Parallel'] = self._SrefElementDeclaration(
            _DesignObj=A52_Res_Parallel._Res_Parallel(_DesignParameter=None,
                                                      _Name='{}:SRF_Res_Parallel'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Res_Parallel']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Res_Parallel']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Res_Parallel']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Res_Parallel']['_XYCoordinates'] = [[0, 0]]

        ## Series
        _Caculation_Parameters = copy.deepcopy(A51_Runit_Switch._Runit_Switch._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_ResWidth'] = _Ser_ResWidth
        _Caculation_Parameters['_ResLength'] = _Ser_ResLength
        _Caculation_Parameters['_CONUMX'] = None
        _Caculation_Parameters['_CONUMY'] = None
        _Caculation_Parameters['_SeriesStripes'] = _Ser_SeriesStripes
        _Caculation_Parameters['_ParallelStripes'] = _Ser_ParallelStripes

        _Caculation_Parameters['_TG_NumberofGate'] = _TG_NumberofGate
        _Caculation_Parameters['_TG_NMOSChannelWidth'] = _TG_NMOSChannelWidth
        _Caculation_Parameters['_TG_PMOSChannelWidth'] = _TG_PMOSChannelWidth
        _Caculation_Parameters['_TG_Channellength'] = _TG_Channellength
        _Caculation_Parameters['_TG_XVT'] = _TG_XVT
        _Caculation_Parameters['_INV_NumberofGate'] = _INV_NumberofGate
        _Caculation_Parameters['_NMOS_Pbody_NumCont'] = _NMOS_Pbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_NumCont'] = _PMOS_Nbody_NumCont

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Res_Series'] = self._SrefElementDeclaration(
            _DesignObj=A51_Runit_Switch._Runit_Switch(_DesignParameter=None,
                                                      _Name='{}:SRF_Res_Series'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Res_Series']['_Reflect'] = [1, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Res_Series']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Res_Series']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Res_Series']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        tmp11 = self.get_param_KJH4('SRF_Res_Parallel','BND_PPLayer_ResGuardRing')
        tmp12 = self.get_param_KJH4('SRF_Res_Parallel','BND_Met1Layer_TGGuardRing')

        target_coordy = min(tmp11[0][0][0]['_XY_down'][1], tmp12[0][0][0]['_XY_down'][1]) - _DRCObj._RXMinSpacetoPRES

        tmp21 = self.get_param_KJH4('SRF_Res_Parallel', 'SRF_Runit_Switch', 'SRF_TG_Switch')
        target_coordx = tmp21[0][0][0][0]['_XY_origin'][0]

        target_coord = [target_coordx, target_coordy]

        tmp22 = self.get_param_KJH4('SRF_Res_Series', 'SRF_TG_Switch')
        approaching_coordx = tmp22[0][0][0]['_XY_origin'][0]
        tmp23 = self.get_param_KJH4('SRF_Res_Series', 'SRF_TG_Switch', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_PPLayer')
        approaching_coordy = tmp23[0][0][0][0][0][0]['_XY_down'][1]
        approaching_coord = [approaching_coordx, approaching_coordy]

        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Res_Series')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Res_Series']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_Met1Layer_Pbody'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Res_Parallel','BND_Met1Layer_TGGuardRing')
        tmp2 = self.get_param_KJH4('SRF_Res_Series','SRF_TG_Switch','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met1Layer_Pbody']['_YWidth'] = tmp1[0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0][0]['_XY_up'][1]

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met1Layer_Pbody']['_XWidth'] = tmp1[0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met1Layer_Pbody']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        target_coord = tmp1[0][0][0]['_XY_up_left']

        # Approaching_coord
        tmp3 = self.get_param_KJH4('BND_Met1Layer_Pbody')
        approaching_coord = tmp3[0][0]['_XY_up_left']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Met1Layer_Pbody']['_XYCoordinates'] = tmpXY

        if (DesignParameters._Technology == '028nm') and _TG_XVT in ('SLVT', 'LVT', 'RVT', 'HVT', 'EG'):
            _XVTLayer = 'BND_' + _TG_XVT + 'Layer'
            _XVTLayerMappingName = _TG_XVT

        elif DesignParameters._Technology in ('028nm'):
            raise NotImplementedError(f"Invalid '_XVT' argument({_TG_XVT}) for {DesignParameters._Technology}")

        else:
            raise NotImplementedError(f"Not Yet Implemented in other technology : {DesignParameters._Technology}")

        # Define Boundary_element
        self._DesignParameter[_XVTLayer] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[_XVTLayerMappingName][0],
            _Datatype=DesignParameters._LayerMapping[_XVTLayerMappingName][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Res_Parallel','SRF_Runit_Switch','SRF_TG_Switch',_XVTLayer)
        tmp2 = self.get_param_KJH4('SRF_Res_Series','SRF_TG_Switch',_XVTLayer)
        # Define Boundary_element _YWidth
        self._DesignParameter[_XVTLayer]['_YWidth'] = tmp1[0][0][0][0][0]['_XY_down'][1] - tmp2[0][0][0][0]['_XY_down'][1]

        # Define Boundary_element _XWidth
        self._DesignParameter[_XVTLayer]['_XWidth'] = tmp2[0][0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter[_XVTLayer]['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        target_coord = tmp2[0][0][0][0]['_XY_down_left']

        # Approaching_coord
        tmp3 = self.get_param_KJH4(_XVTLayer)
        approaching_coord = tmp3[0][0]['_XY_down_left']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter[_XVTLayer]['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## HDVCAP cap_2nd
        ## SREF Generation
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A50_HDVNCAP_Array._HDVNCAP_Array._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length'] = _Length_1st
        _Caculation_Parameters['_LayoutOption'] = _LayoutOption_1st
        _Caculation_Parameters['_NumFigPair'] = _NumFigPair_1st
        _Caculation_Parameters['_Array_row'] = _Array_1st_row
        _Caculation_Parameters['_Array_col'] = _Array_1st_col
        _Caculation_Parameters['_Cbot_Ctop_metalwidth'] = _Cbot_Ctop_metalwidth_1st

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_cap_1st'] = self._SrefElementDeclaration(
            _DesignObj=A50_HDVNCAP_Array._HDVNCAP_Array(_DesignParameter=None, _Name='{}:SRF_cap_1st'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_cap_1st']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_cap_1st']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_cap_1st']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_cap_1st']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Res_Parallel', 'SRF_Pbody_Runit', 'SRF_PbodyContactPhyLen', 'BND_ODLayer')
        tmp2 = self.get_param_KJH4('SRF_cap_1st','SRF_Pbodyring','BND_ExtenODLayer_Right')
        target_coord = tmp1[0][0][0][0][0]['_XY_down_left'] - [_DRCObj._RXMinSpacetoPRES, 0]
        # Approaching_coord
        approaching_coord = tmp2[0][0][0][0]['_XY_down_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_cap_1st')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_cap_1st']['_XYCoordinates'] = tmpXY


        # Define Boundary_element
        self._DesignParameter['BND_Met1Layer_ResCapGuardRingConn'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Res_Parallel', 'SRF_Pbody_Runit', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_cap_1st','SRF_Pbodyring','BND_ExtenMet1Layer_Right')
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met1Layer_ResCapGuardRingConn']['_YWidth'] = tmp1[0][0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met1Layer_ResCapGuardRingConn']['_XWidth'] = tmp1[0][0][0][0][0]['_XY_down_left'][0] - tmp2[0][0][0][0]['_XY_down_left'][0]

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met1Layer_ResCapGuardRingConn']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        target_coord = tmp1[0][0][0][0][0]['_XY_down_left']
        # Approaching_coord
        tmp3 = self.get_param_KJH4('BND_Met1Layer_ResCapGuardRingConn')
        approaching_coord = tmp3[0][0]['_XY_down_right']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        target_coord = tmp1[0][-1][0][0][0]['_XY_down_left']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        # Define
        self._DesignParameter['BND_Met1Layer_ResCapGuardRingConn']['_XYCoordinates'] = tmpXY


        # Define Boundary_element
        self._DesignParameter['BND_PPLayer_ResCapGuardRingConn'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Res_Parallel', 'SRF_Pbody_Runit', 'SRF_PbodyContactPhyLen', 'BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_cap_1st','SRF_Pbodyring','BND_ExtenPPLayer_Right')
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_PPLayer_ResCapGuardRingConn']['_YWidth'] = tmp1[0][0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_PPLayer_ResCapGuardRingConn']['_XWidth'] = tmp1[0][0][0][0][0]['_XY_down_left'][0] - tmp2[0][0][0][0]['_XY_down_left'][0]

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_PPLayer_ResCapGuardRingConn']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        target_coord = tmp1[0][0][0][0][0]['_XY_down_left']
        # Approaching_coord
        tmp3 = self.get_param_KJH4('BND_PPLayer_ResCapGuardRingConn')
        approaching_coord = tmp3[0][0]['_XY_down_right']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        target_coord = tmp1[0][-1][0][0][0]['_XY_down_left']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        # Define
        self._DesignParameter['BND_PPLayer_ResCapGuardRingConn']['_XYCoordinates'] = tmpXY


        # Define Boundary_element
        self._DesignParameter['BND_ODLayer_ResCapGuardRingConn'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0],
            _Datatype=DesignParameters._LayerMapping['DIFF'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Res_Parallel', 'SRF_Pbody_Runit', 'SRF_PbodyContactPhyLen', 'BND_ODLayer')
        tmp2 = self.get_param_KJH4('SRF_cap_1st','SRF_Pbodyring','BND_ExtenODLayer_Right')
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_ODLayer_ResCapGuardRingConn']['_YWidth'] = tmp1[0][0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_ODLayer_ResCapGuardRingConn']['_XWidth'] = tmp1[0][0][0][0][0]['_XY_down_left'][0] - tmp2[0][0][0][0]['_XY_down_left'][0]

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_ODLayer_ResCapGuardRingConn']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        target_coord = tmp1[0][0][0][0][0]['_XY_down_left']
        # Approaching_coord
        tmp3 = self.get_param_KJH4('BND_ODLayer_ResCapGuardRingConn')
        approaching_coord = tmp3[0][0]['_XY_down_right']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        target_coord = tmp1[0][-1][0][0][0]['_XY_down_left']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        # Define
        self._DesignParameter['BND_ODLayer_ResCapGuardRingConn']['_XYCoordinates'] = tmpXY

        if tmp1[0][-1][0][0][0]['_XY_up_left'][1] > tmp2[0][0][0][0]['_XY_up_right'][1]:
            # Define Boundary_element
            self._DesignParameter['BND_Met1Layer_CapPbodyExten'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )

            tmp1 = self.get_param_KJH4('BND_Met1Layer_ResCapGuardRingConn')
            tmp2 = self.get_param_KJH4('SRF_cap_1st', 'SRF_Pbodyring', 'BND_ExtenMet1Layer_Right')
            # Define Boundary_element _YWidth
            self._DesignParameter['BND_Met1Layer_CapPbodyExten']['_YWidth'] = tmp1[-1][0]['_XY_up_left'][1] - tmp2[0][0][0][0]['_XY_up_left'][1]

            # Define Boundary_element _XWidth
            self._DesignParameter['BND_Met1Layer_CapPbodyExten']['_XWidth'] = tmp2[0][0][0][0]['_Xwidth']

            # Calculate Sref XYcoord
            # initialize coordinate
            self._DesignParameter['BND_Met1Layer_CapPbodyExten']['_XYCoordinates'] = [[0, 0]]
            tmpXY = []

            # Calculate
            # Target_coord
            target_coord = tmp1[-1][0]['_XY_up_left']
            # Approaching_coord
            tmp3 = self.get_param_KJH4('BND_Met1Layer_CapPbodyExten')
            approaching_coord = tmp3[0][0]['_XY_up_left']
            # Sref coord
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

            # Define
            self._DesignParameter['BND_Met1Layer_CapPbodyExten']['_XYCoordinates'] = tmpXY


            # Define Boundary_element
            self._DesignParameter['BND_PPLayer_CapPbodyExten'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['PIMP'][0],
                _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )

            tmp1 = self.get_param_KJH4('BND_PPLayer_ResCapGuardRingConn')
            tmp2 = self.get_param_KJH4('SRF_cap_1st', 'SRF_Pbodyring', 'BND_ExtenPPLayer_Right')
            # Define Boundary_element _YWidth
            self._DesignParameter['BND_PPLayer_CapPbodyExten']['_YWidth'] = tmp1[-1][0]['_XY_up_left'][1] - tmp2[0][0][0][0]['_XY_up_left'][1]

            # Define Boundary_element _XWidth
            self._DesignParameter['BND_PPLayer_CapPbodyExten']['_XWidth'] = tmp2[0][0][0][0]['_Xwidth']

            # Calculate Sref XYcoord
            # initialize coordinate
            self._DesignParameter['BND_PPLayer_CapPbodyExten']['_XYCoordinates'] = [[0, 0]]
            tmpXY = []

            # Calculate
            # Target_coord
            target_coord = tmp1[-1][0]['_XY_up_left']
            # Approaching_coord
            tmp3 = self.get_param_KJH4('BND_PPLayer_CapPbodyExten')
            approaching_coord = tmp3[0][0]['_XY_up_left']
            # Sref coord
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

            # Define
            self._DesignParameter['BND_PPLayer_CapPbodyExten']['_XYCoordinates'] = tmpXY


            # Define Boundary_element
            self._DesignParameter['BND_ODLayer_CapPbodyExten'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['DIFF'][0],
                _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )

            tmp1 = self.get_param_KJH4('BND_ODLayer_ResCapGuardRingConn')
            tmp2 = self.get_param_KJH4('SRF_cap_1st', 'SRF_Pbodyring', 'BND_ExtenODLayer_Right')
            # Define Boundary_element _YWidth
            self._DesignParameter['BND_ODLayer_CapPbodyExten']['_YWidth'] = tmp1[-1][0]['_XY_up_left'][1] - tmp2[0][0][0][0]['_XY_up_left'][1]

            # Define Boundary_element _XWidth
            self._DesignParameter['BND_ODLayer_CapPbodyExten']['_XWidth'] = tmp2[0][0][0][0]['_Xwidth']

            # Calculate Sref XYcoord
            # initialize coordinate
            self._DesignParameter['BND_ODLayer_CapPbodyExten']['_XYCoordinates'] = [[0, 0]]
            tmpXY = []

            # Calculate
            # Target_coord
            target_coord = tmp1[-1][0]['_XY_up_left']
            # Approaching_coord
            tmp3 = self.get_param_KJH4('BND_ODLayer_CapPbodyExten')
            approaching_coord = tmp3[0][0]['_XY_up_left']
            # Sref coord
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

            # Define
            self._DesignParameter['BND_ODLayer_CapPbodyExten']['_XYCoordinates'] = tmpXY

        ## SREF Generation
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A50_TG_Switch._TG_Switch._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_TG_NumberofGate'] = _TG_NumberofGate
        _Caculation_Parameters['_TG_NMOSChannelWidth'] = _TG_NMOSChannelWidth
        _Caculation_Parameters['_TG_PMOSChannelWidth'] = _TG_PMOSChannelWidth
        _Caculation_Parameters['_TG_Channellength'] = _TG_Channellength
        _Caculation_Parameters['_TG_XVT'] = _TG_XVT
        _Caculation_Parameters['_INV_NumberofGate'] = _INV_NumberofGate
        _Caculation_Parameters['_NMOS_Pbody_NumCont'] = _NMOS_Pbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_NumCont'] = _PMOS_Nbody_NumCont

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_cap_Switch'] = self._SrefElementDeclaration(
            _DesignObj=A50_TG_Switch._TG_Switch(_DesignParameter=None, _Name='{}:SRF_cap_Switch'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_cap_Switch']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_cap_Switch']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_cap_Switch']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_cap_Switch']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        if _Parallel_Stack % 2 == 0:
            tmp1 = self.get_param_KJH4('SRF_Res_Parallel','SRF_Runit_Switch_flip','SRF_TG_Switch','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
            target_coord = tmp1[0][-1][0][0][0][0][0]['_XY_down_left']
            tmp2 = self.get_param_KJH4('SRF_cap_Switch','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0][0]['_XY_up_left']
            # Sref coord
            tmp3 = self.get_param_KJH4('SRF_cap_Switch')
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            # Define
            self._DesignParameter['SRF_cap_Switch']['_XYCoordinates'] = tmpXY

        else:
            self._DesignParameter['SRF_cap_Switch']['_Reflect'] = [1, 0, 0]
            tmp1 = self.get_param_KJH4('SRF_Res_Parallel','SRF_Runit_Switch','SRF_TG_Switch','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
            target_coord = tmp1[0][-1][0][0][0][0][0]['_XY_down_left']
            tmp2 = self.get_param_KJH4('SRF_cap_Switch','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0][0]['_XY_up_left']
            # Sref coord
            tmp3 = self.get_param_KJH4('SRF_cap_Switch')
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            # Define
            self._DesignParameter['SRF_cap_Switch']['_XYCoordinates'] = tmpXY

        ###### Cap Switch Met3 Conn
        # Define Boundary_element
        self._DesignParameter['BND_Met3Layer_cap_Switch_Conn'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_cap_Switch','SRF_Source_ViaM2M3','SRF_ViaM2M3','BND_Met3Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met3Layer_cap_Switch_Conn']['_YWidth'] = tmp1[0][0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met3Layer_cap_Switch_Conn']['_XWidth'] = tmp1[0][0][0][0][0]['_XY_left'][0]

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met3Layer_cap_Switch_Conn']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        tmp3 = self.get_param_KJH4('BND_Met3Layer_cap_Switch_Conn')
        target_coord = tmp1[0][0][0][0][0]['_XY_left']
        approaching_coord = tmp3[0][0]['_XY_right']
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Met3Layer_cap_Switch_Conn']['_XYCoordinates'] = tmpXY

        ###### Cap Switch Met5 Conn
        # Define Boundary_element
        self._DesignParameter['BND_Met5Layer_cap_Switch_Conn'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5'][0],
            _Datatype=DesignParameters._LayerMapping['METAL5'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Met3Layer_cap_Switch_Conn')
        tmp2 = self.get_param_KJH4('SRF_cap_1st','BND_MetLayer_CBotConn')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met5Layer_cap_Switch_Conn']['_YWidth'] = tmp1[0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met5Layer_cap_Switch_Conn']['_XWidth'] = tmp1[0][0]['_Ywidth'] - tmp2[0][0][0]['_XY_down_left'][0]

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met5Layer_cap_Switch_Conn']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        tmp3 = self.get_param_KJH4('BND_Met5Layer_cap_Switch_Conn')
        target_coord = tmp1[0][0]['_XY_down_left'] + [tmp1[0][0]['_Ywidth'], 0]
        approaching_coord = tmp3[0][0]['_XY_down_right']
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Met5Layer_cap_Switch_Conn']['_XYCoordinates'] = tmpXY

        ###### Cap Switch Met4 Conn
        # Define Boundary_element
        self._DesignParameter['BND_Met4Layer_cap_Switch_Conn'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Met5Layer_cap_Switch_Conn')
        tmp2 = self.get_param_KJH4('SRF_cap_1st','BND_MetLayer_CBotConn')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met4Layer_cap_Switch_Conn']['_YWidth'] = tmp1[0][0]['_XY_up_left'][1] - tmp2[0][0][0]['_XY_down_left'][1]

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met4Layer_cap_Switch_Conn']['_XWidth'] = tmp2[0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met4Layer_cap_Switch_Conn']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        tmp3 = self.get_param_KJH4('BND_Met4Layer_cap_Switch_Conn')
        target_coord = tmp1[0][0]['_XY_up_left']
        approaching_coord = tmp3[0][0]['_XY_up_left']
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Met4Layer_cap_Switch_Conn']['_XYCoordinates'] = tmpXY

        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 5
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Cap_Switch_ViaM3M5'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_Cap_Switch_ViaM3M5'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Cap_Switch_ViaM3M5']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Cap_Switch_ViaM3M5']['_Angle'] = 0

        # Calcuate _COY
        tmp1 = self.get_param_KJH4('BND_Met3Layer_cap_Switch_Conn')
        tmpWidth = tmp1[0][0]['_Ywidth']
        _Caculation_Parameters['_COY'] = int(
            (tmpWidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)
        )

        # Calcuate _COX
        _Caculation_Parameters['_COX'] = int(
            (tmpWidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)
        )

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Cap_Switch_ViaM3M5']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Cap_Switch_ViaM3M5']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        tmp2 = self.get_param_KJH4('BND_Met5Layer_cap_Switch_Conn')
        target_coord = (tmp2[0][0]['_XY_right'] + tmp1[0][0]['_XY_left']) // 2
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Cap_Switch_ViaM3M5', 'SRF_ViaM3M4', 'BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Cap_Switch_ViaM3M5')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Cap_Switch_ViaM3M5']['_XYCoordinates'] = tmpXY

        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 4
        _Caculation_Parameters['_Layer2'] = 5
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Cap_Switch_ViaM4M5'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_Cap_Switch_ViaM4M5'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Cap_Switch_ViaM4M5']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Cap_Switch_ViaM4M5']['_Angle'] = 0

        # Calcuate _COX
        tmp1 = self.get_param_KJH4('BND_Met4Layer_cap_Switch_Conn')
        tmpWidth = tmp1[0][0]['_Xwidth']
        _Caculation_Parameters['_COX'] = int(
            (tmpWidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)
        )

        # Calcuate _COY
        tmp2 = self.get_param_KJH4('BND_Met5Layer_cap_Switch_Conn')
        tmpWidth = tmp2[0][0]['_Ywidth']
        _Caculation_Parameters['_COY'] = int(
            (tmpWidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)
        )

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Cap_Switch_ViaM4M5']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Cap_Switch_ViaM4M5']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        target_coord = [tmp1[0][0]['_XY_cent'][0], tmp2[0][0]['_XY_cent'][1]]
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Cap_Switch_ViaM4M5', 'SRF_ViaM4M5', 'BND_Met5Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Cap_Switch_ViaM4M5')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Cap_Switch_ViaM4M5']['_XYCoordinates'] = tmpXY

        ###### PortA cap res switch conn
        # Define Boundary_element
        self._DesignParameter['BND_Met3Layer_Cap_SerRes_Switch'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Res_Series','SRF_TG_Switch','SRF_Drain_ViaM2M3','SRF_ViaM2M3','BND_Met3Layer')
        tmp21 = self.get_param_KJH4('SRF_cap_1st','BND_MetLayer_CTopConn')
        tmp22 = self.get_param_KJH4('SRF_Res_Series','SRF_Res','SRF_OutputPort1_Via','SRF_ViaM3M4','BND_Met4Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met3Layer_Cap_SerRes_Switch']['_YWidth'] = tmp1[0][0][0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met3Layer_Cap_SerRes_Switch']['_XWidth'] = tmp1[0][0][0][0][0][0]['_XY_up_right'][0] - min(tmp21[0][0][0]['_XY_down_left'][0], tmp22[0][0][0][0][0][0]['_XY_down_left'][0])

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met3Layer_Cap_SerRes_Switch']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        tmp3 = self.get_param_KJH4('BND_Met3Layer_Cap_SerRes_Switch')
        target_coord = tmp1[0][0][0][0][0][0]['_XY_up_right']
        approaching_coord = tmp3[0][0]['_XY_down_right']
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Met3Layer_Cap_SerRes_Switch']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_Met4Layer_Cap_SerRes'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Met3Layer_Cap_SerRes_Switch')
        tmp2 = self.get_param_KJH4('SRF_cap_1st','BND_MetLayer_CTopConn')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met4Layer_Cap_SerRes']['_YWidth'] = tmp2[0][0][0]['_XY_up_left'][1] - tmp1[0][0]['_XY_down_left'][1]

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met4Layer_Cap_SerRes']['_XWidth'] = tmp2[0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met4Layer_Cap_SerRes']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        tmp3 = self.get_param_KJH4('BND_Met4Layer_Cap_SerRes')
        target_coord = tmp2[0][0][0]['_XY_up_left']
        approaching_coord = tmp3[0][0]['_XY_up_left']
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Met4Layer_Cap_SerRes']['_XYCoordinates'] = tmpXY


        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Cap_SerRes_ViaM3M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_Cap_SerRes_ViaM3M4'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Cap_SerRes_ViaM3M4']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Cap_SerRes_ViaM3M4']['_Angle'] = 0

        # Calcuate _COX
        tmp1 = self.get_param_KJH4('BND_Met4Layer_Cap_SerRes')
        tmpWidth = tmp1[0][0]['_Xwidth']
        _Caculation_Parameters['_COX'] = int(
            (tmpWidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)
        )

        # Calcuate _COY
        tmp2 = self.get_param_KJH4('BND_Met3Layer_Cap_SerRes_Switch')
        tmpWidth = tmp2[0][0]['_Ywidth']
        _Caculation_Parameters['_COY'] = int(
            (tmpWidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)
        )

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Cap_SerRes_ViaM3M4']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Cap_SerRes_ViaM3M4']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        target_coord = [tmp1[0][0]['_XY_cent'][0], tmp2[0][0]['_XY_cent'][1]]
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Cap_SerRes_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Cap_SerRes_ViaM3M4')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Cap_SerRes_ViaM3M4']['_XYCoordinates'] = tmpXY


        # Define Boundary_element
        self._DesignParameter['BND_Met3Layer_SerRes_Switch'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Met3Layer_Cap_SerRes_Switch')
        tmp2 = self.get_param_KJH4('SRF_Res_Series','SRF_Res','SRF_OutputPort1_Via','SRF_ViaM3M4','BND_Met4Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met3Layer_SerRes_Switch']['_YWidth'] = tmp1[0][0]['_XY_up_left'][1] - tmp2[0][0][0][0][0][0]['_XY_up_left'][1]

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met3Layer_SerRes_Switch']['_XWidth'] = tmp2[0][0][0][0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met3Layer_SerRes_Switch']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        tmp3 = self.get_param_KJH4('BND_Met3Layer_SerRes_Switch')
        target_coord = tmp2[0][0][0][0][0][0]['_XY_up_left']
        approaching_coord = tmp3[0][0]['_XY_down_left']
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Met3Layer_SerRes_Switch']['_XYCoordinates'] = tmpXY


        # # Define ViaX Parameter
        # _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        # _Caculation_Parameters['_Layer1'] = 3
        # _Caculation_Parameters['_Layer2'] = 4
        # _Caculation_Parameters['_COX'] = None
        # _Caculation_Parameters['_COY'] = None
        #
        # # Sref ViaX declaration
        # self._DesignParameter['SRF_SerRes_Switch_ViaM3M4'] = self._SrefElementDeclaration(
        #     _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
        #                                                     _Name='{}:SRF_SerRes_Switch_ViaM3M4'.format(_Name)))[0]
        #
        # # Define Sref Relection
        # self._DesignParameter['SRF_SerRes_Switch_ViaM3M4']['_Reflect'] = [0, 0, 0]
        #
        # # Define Sref Angle
        # self._DesignParameter['SRF_SerRes_Switch_ViaM3M4']['_Angle'] = 0
        #
        # # Calcuate _COX
        # tmp1 = self.get_param_KJH4('BND_Met3Layer_SerRes_Switch')
        # tmpWidth = tmp1[0][0]['_Xwidth']
        # _Caculation_Parameters['_COX'] = int(max(2,
        #     (tmpWidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)
        # ))
        #
        # # Calcuate _COY
        # tmp2 = self.get_param_KJH4('BND_Met3Layer_Cap_SerRes_Switch')
        # tmpWidth = tmp2[0][0]['_Ywidth']
        # _Caculation_Parameters['_COY'] = int(max(2,
        #     (tmpWidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)
        # ))
        #
        # # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        # self._DesignParameter['SRF_SerRes_Switch_ViaM3M4']['_DesignObj']._CalculateDesignParameterXmin(
        #     **_Caculation_Parameters)  ## Option: Xmin, Ymin
        #
        # # Calculate Sref XYcoord
        # tmpXY = []
        # # initialized Sref coordinate
        # self._DesignParameter['SRF_SerRes_Switch_ViaM3M4']['_XYCoordinates'] = [[0, 0]]
        #
        # # Calculate
        # # Target_coord
        # target_coord = [tmp1[0][0]['_XY_cent'][0], tmp2[0][0]['_XY_cent'][1]]
        # # Approaching_coord
        # tmp2 = self.get_param_KJH4('SRF_SerRes_Switch_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        # approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # # Sref coord
        # tmp3 = self.get_param_KJH4('SRF_SerRes_Switch_ViaM3M4')
        # Scoord = tmp3[0][0]['_XY_origin']
        # # Cal
        # New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        # tmpXY.append(New_Scoord)
        # # Define
        # self._DesignParameter['SRF_SerRes_Switch_ViaM3M4']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_Met3Layer_PortX_Ext'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_outter_KJH4('SRF_Res_Parallel','SRF_Runit_Switch')
        tmp21 = self.get_param_KJH4('SRF_Res_Parallel','SRF_Runit_Switch','SRF_TG_Switch','BND_Metal3Layer_Hrz_PortAB')
        tmp22 = self.get_param_KJH4('SRF_Res_Parallel','SRF_Runit_Switch_flip','SRF_TG_Switch','BND_Metal3Layer_Hrz_PortAB')


        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met3Layer_PortX_Ext']['_YWidth'] = tmp21[0][0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met3Layer_PortX_Ext']['_XWidth'] = tmp1['_Mostright']['coord'][0] - tmp21[0][0][0][0][0]['_XY_down_right'][0]

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met3Layer_PortX_Ext']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        tmp3 = self.get_param_KJH4('BND_Met3Layer_PortX_Ext')

        for i in range(_Parallel_Stack):
            if i % 2 == 0:
                target_coord = tmp21[0][i//2][0][0][0]['_XY_down_right']
                approaching_coord = tmp3[0][0]['_XY_down_left']
                Scoord = tmp3[0][0]['_XY_origin']
                # Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)

            else:
                target_coord = tmp22[0][i//2][0][0][0]['_XY_up_right']
                approaching_coord = tmp3[0][0]['_XY_down_left']
                Scoord = tmp3[0][0]['_XY_origin']
                # Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)

        tmp2 = self.get_param_KJH4('SRF_Res_Series','SRF_TG_Switch','BND_Metal3Layer_Hrz_PortAB')
        target_coord = tmp2[0][0][-1][0]['_XY_up_right']
        approaching_coord = tmp3[0][0]['_XY_down_left']
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        # Define
        self._DesignParameter['BND_Met3Layer_PortX_Ext']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_Met4Layer_PortX_Conn'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Met3Layer_PortX_Ext')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met4Layer_PortX_Conn']['_YWidth'] = tmp1[-2][0]['_XY_up_right'][1] - tmp1[-1][0]['_XY_down_right'][1]

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met4Layer_PortX_Conn']['_XWidth'] = 500

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met4Layer_PortX_Conn']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        tmp3 = self.get_param_KJH4('BND_Met4Layer_PortX_Conn')
        target_coord = tmp1[-1][0]['_XY_down_right']
        approaching_coord = tmp3[0][0]['_XY_down_right']
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['BND_Met4Layer_PortX_Conn']['_XYCoordinates'] = tmpXY

        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_PortX_ViaM3M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_PortX_ViaM3M4'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_PortX_ViaM3M4']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_PortX_ViaM3M4']['_Angle'] = 0

        # Calcuate _COX
        tmp1 = self.get_param_KJH4('BND_Met4Layer_PortX_Conn')
        tmpWidth = tmp1[0][0]['_Xwidth']
        _Caculation_Parameters['_COX'] = int(max(2,
            (tmpWidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)
        ))

        # Calcuate _COY
        tmp2 = self.get_param_KJH4('BND_Met3Layer_PortX_Ext')
        tmpWidth = tmp2[0][0]['_Ywidth']
        _Caculation_Parameters['_COY'] = int(max(2,
            (tmpWidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)
        ))

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_PortX_ViaM3M4']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_PortX_ViaM3M4']['_XYCoordinates'] = [[0, 0]]
        tmp21 = self.get_param_KJH4('SRF_PortX_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        tmp3 = self.get_param_KJH4('SRF_PortX_ViaM3M4')

        for i in range(_Parallel_Stack + 1):
            # Calculate
            # Target_coord
            target_coord = [tmp1[0][0]['_XY_down'][0], tmp2[i][0]['_XY_right'][1]]
            # Approaching_coord
            approaching_coord = tmp21[0][0][0][0]['_XY_cent']
            # Sref coord
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        # Define
        self._DesignParameter['SRF_PortX_ViaM3M4']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_Met4Layer_PortB_ResConn'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp11 = self.get_param_KJH4('SRF_Res_Parallel','SRF_Runit_Switch','SRF_Res','SRF_OutputPort1_Via','SRF_ViaM3M4','BND_Met4Layer')
        tmp12 = self.get_param_KJH4('SRF_Res_Parallel','SRF_Runit_Switch_flip','SRF_Res','SRF_OutputPort1_Via','SRF_ViaM3M4','BND_Met4Layer')

        # Define Boundary_element _YWidth
        if _Parallel_Stack % 2 ==0:
            self._DesignParameter['BND_Met4Layer_PortB_ResConn']['_YWidth'] = tmp12[0][-1][0][0][0][0][0]['_XY_down_left'][1] - tmp11[0][0][0][0][0][0][0]['_XY_down_left'][1]
        else:
            self._DesignParameter['BND_Met4Layer_PortB_ResConn']['_YWidth'] = tmp11[0][-1][0][0][0][0][0]['_XY_up_left'][1] - tmp11[0][0][0][0][0][0][0]['_XY_down_left'][1]


        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met4Layer_PortB_ResConn']['_XWidth'] = tmp11[0][0][0][0][0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met4Layer_PortB_ResConn']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        tmp3 = self.get_param_KJH4('BND_Met4Layer_PortB_ResConn')
        target_coord = tmp11[0][0][0][0][0][0][0]['_XY_down_left']
        approaching_coord = tmp3[0][0]['_XY_down_left']
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['BND_Met4Layer_PortB_ResConn']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_Met4Layer_PortB_Res_Cap'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Res_Parallel','SRF_Runit_Switch','SRF_Res','SRF_OutputPort1_Via','SRF_ViaM3M4','BND_Met4Layer')
        tmp2 = self.get_param_KJH4('SRF_cap_1st','BND_MetLayer_CBotConn')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met4Layer_PortB_Res_Cap']['_YWidth'] = tmp1[0][0][0][0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met4Layer_PortB_Res_Cap']['_XWidth'] = tmp1[0][0][0][0][0][0][0]['_XY_down_right'][0] - tmp2[0][-1][0]['_XY_left'][0]

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met4Layer_PortB_Res_Cap']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        tmp3 = self.get_param_KJH4('BND_Met4Layer_PortB_Res_Cap')
        target_coord = tmp1[0][0][0][0][0][0][0]['_XY_down_right']
        approaching_coord = tmp3[0][0]['_XY_down_right']
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['BND_Met4Layer_PortB_Res_Cap']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_Met3Layer_PortB_Switch'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_cap_Switch','BND_Metal3Layer_Hrz_PortAB')
        tmp2 = self.get_param_KJH4('SRF_cap_1st','BND_MetLayer_CBotConn')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met3Layer_PortB_Switch']['_YWidth'] = tmp1[0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met3Layer_PortB_Switch']['_XWidth'] = tmp1[0][0][0]['_XY_left'][0] - tmp2[0][-1][0]['_XY_left'][0]

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met3Layer_PortB_Switch']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        tmp3 = self.get_param_KJH4('BND_Met3Layer_PortB_Switch')
        target_coord = tmp1[0][0][0]['_XY_left']
        approaching_coord = tmp3[0][0]['_XY_right']
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['BND_Met3Layer_PortB_Switch']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_Met4Layer_PortB_Switch_Cap'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Met3Layer_PortB_Switch')
        tmp2 = self.get_param_KJH4('SRF_cap_1st','BND_MetLayer_CBotConn')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met4Layer_PortB_Switch_Cap']['_YWidth'] = tmp1[0][0]['_XY_up_left'][1] - tmp2[0][-1][0]['_XY_up_left'][1]

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met4Layer_PortB_Switch_Cap']['_XWidth'] = tmp2[0][-1][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met4Layer_PortB_Switch_Cap']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        tmp3 = self.get_param_KJH4('BND_Met4Layer_PortB_Switch_Cap')
        target_coord = tmp1[0][0]['_XY_up_left']
        approaching_coord = tmp3[0][0]['_XY_up_left']
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['BND_Met4Layer_PortB_Switch_Cap']['_XYCoordinates'] = tmpXY

        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_PortB_ViaM3M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_PortB_ViaM3M4'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_PortB_ViaM3M4']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_PortB_ViaM3M4']['_Angle'] = 0

        # Calcuate _COX
        tmp1 = self.get_param_KJH4('BND_Met4Layer_PortB_Switch_Cap')
        tmpWidth = tmp1[0][0]['_Xwidth']
        _Caculation_Parameters['_COX'] = int(max(2,
            (tmpWidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)
        ))

        # Calcuate _COY
        tmp2 = self.get_param_KJH4('BND_Met3Layer_PortB_Switch')
        tmpWidth = tmp2[0][0]['_Ywidth']
        _Caculation_Parameters['_COY'] = int(max(2,
            (tmpWidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)
        ))

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_PortB_ViaM3M4']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_PortB_ViaM3M4']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        target_coord = [tmp1[0][0]['_XY_down'][0], tmp2[0][0]['_XY_right'][1]]
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_PortB_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_PortB_ViaM3M4')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_PortB_ViaM3M4']['_XYCoordinates'] = tmpXY


        print('##############################')
        print('##     Calculation_End    ##')
        print('##############################')

## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_AJH
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_A53_TIA_RCfeedback_1ststage_v6'
    cellname = 'A53_TIA_RCfeedback_1ststage_v6'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        # Parallel Res
        _Par_ResWidth=160,
        _Par_ResLength=1300,
        _Par_SeriesStripes=50,
        _Par_ParallelStripes=1,

        _Ser_ResWidth=160,
        _Ser_ResLength=1300,
        _Ser_SeriesStripes=70,
        _Ser_ParallelStripes=1,

        _TG_NumberofGate=100,  # number
        _TG_NMOSChannelWidth=500,  # number
        _TG_PMOSChannelWidth=1000,
        _TG_Channellength=150,  # number
        _TG_XVT			='EG', # 'XVT' ex)SLVT LVT RVT HVT EG
        _INV_NumberofGate       =2,
        _NMOS_Pbody_NumCont     =2,
        _PMOS_Nbody_NumCont     =2,

        _Parallel_Stack         =4,

        # Cap_1st
        _Length_1st=9400,
        _LayoutOption_1st=[2, 3, 4],
        _NumFigPair_1st=25,
        _Array_1st_row=2,
        _Array_1st_col=2,
        _Cbot_Ctop_metalwidth_1st=500,

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
    LayoutObj = _TIA_RCfeedback_1ststage(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('###############      Sending to FTP Server...      ##################')
    My = MyInfo_AJH.USER(DesignParameters._Technology)
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