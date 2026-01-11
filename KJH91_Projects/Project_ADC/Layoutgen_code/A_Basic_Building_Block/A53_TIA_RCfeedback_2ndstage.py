from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC_EGFET

import numpy as np
import copy
import math

from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_opppcres_b_portVia
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_HDVNCAP_Array
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2_YCH
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_TIA_PbodyContactPhyLen

class _TIA_RCfeedback_2ndstage(StickDiagram_KJH1._StickDiagram_KJH):

    _ParametersForDesignCalculation = dict(
        _ResWidth_2nd=None,
        _ResLength_2nd=None,
        _CONUMX_2nd=None,
        _CONUMY_2nd=None,
        _SeriesStripes_2nd=None,
        _ParallelStripes_2nd=None,
        _Res_Port1Layer=None,
        _Res_Port2Layer=None,

        # Cap_2nd
        _Length_2nd=9000,
        _LayoutOption_2nd=[2, 3, 4],
        _NumFigPair_2nd=20,
        _Array_2nd_row=2,
        _Array_2nd_col=3,
        _Cbot_Ctop_metalwidth_2nd=500,


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
                                    _ResWidth_2nd=None,
                                    _ResLength_2nd=None,
                                    _CONUMX_2nd=None,
                                    _CONUMY_2nd=None,
                                    _SeriesStripes_2nd=None,
                                    _ParallelStripes_2nd=None,
                                    _Res_Port1Layer=None,
                                    _Res_Port2Layer=None,

                                  # Cap_2nd
                                  _Length_2nd=9000,
                                  _LayoutOption_2nd=[2, 3, 4],
                                  _NumFigPair_2nd=20,
                                  _Array_2nd_row=2,
                                  _Array_2nd_col=3,
                                  _Cbot_Ctop_metalwidth_2nd=500,


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

        ## ################################################################################################################### resistor0

        ## SREF Generation Resistor0
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A50_opppcres_b_portVia._Opppcres_b._ParametersForDesignCalculation)
        _Caculation_Parameters['_ResWidth'] = _ResWidth_2nd
        _Caculation_Parameters['_ResLength'] = _ResLength_2nd
        _Caculation_Parameters['_CONUMX'] = _CONUMX_2nd
        _Caculation_Parameters['_CONUMY'] = _CONUMY_2nd
        _Caculation_Parameters['_SeriesStripes'] = _SeriesStripes_2nd
        _Caculation_Parameters['_ParallelStripes'] = _ParallelStripes_2nd
        _Caculation_Parameters['_Port1Layer'] = _Res_Port1Layer
        _Caculation_Parameters['_Port2Layer'] = _Res_Port2Layer

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Res_2nd'] = self._SrefElementDeclaration(
            _DesignObj=A50_opppcres_b_portVia._Opppcres_b(_DesignParameter=None, _Name='{}:SRF_Res_2nd'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Res_2nd']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Res_2nd']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Res_2nd']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Res_2nd']['_XYCoordinates'] = [[0, 0]]

        ## ################################################################################################################### Pbodyring_top
        # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A50_TIA_PbodyContactPhyLen._PbodyContactPhyLen._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length'] = None
        _Caculation_Parameters['_NumCont'] = 3
        _Caculation_Parameters['_Vtc_flag'] = False

        tmp1 = self.get_param_KJH4('SRF_Res_2nd', '_PRESLayer')
        # tmp2 = self.get_param_KJH4('SRF_Pmos_Tr0Tr3', 'SRF_Pmos_Tr3', 'SRF_Pmos', 'BND_EGLayer')

        target_coordx = tmp1[0][0][0]['_XY_right'][0]
        target_coordy = tmp1[0][0][0]['_XY_left'][0]
        target_length_x = target_coordx - target_coordy
        _Caculation_Parameters['_Length'] = target_length_x + 500

        # Generate Sref
        self._DesignParameter['SRF_PbodyTop_Res_2nd'] = self._SrefElementDeclaration(
            _DesignObj=A50_TIA_PbodyContactPhyLen._PbodyContactPhyLen(_DesignParameter=None,
                                                                      _Name='{}:SRF_PbodyTop_Res_2nd'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_PbodyTop_Res_2nd']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_PbodyTop_Res_2nd']['_Angle'] = 0

        # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_PbodyTop_Res_2nd']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        # Define Sref _XYcoordinate
        self._DesignParameter['SRF_PbodyTop_Res_2nd']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Res_2nd', '_PRESLayer')
        target_coord = tmp1[0][0][0]['_XY_up']
        target_coord[1] = target_coord[1] + 250
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_PbodyTop_Res_2nd', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_PbodyTop_Res_2nd')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_PbodyTop_Res_2nd']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Pbodyring_left
        # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(
            A50_TIA_PbodyContactPhyLen._PbodyContactPhyLen._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length'] = None
        _Caculation_Parameters['_NumCont'] = 3
        _Caculation_Parameters['_Vtc_flag'] = True

        tmp1 = self.get_param_KJH4('SRF_Res_2nd', '_PRESLayer')

        target_length_y = abs(tmp1[0][0][0]['_XY_up'][1] - tmp1[0][0][0]['_XY_down'][1])
        _Caculation_Parameters['_Length'] = target_length_y + 250

        # Generate Sref
        self._DesignParameter['SRF_PbodyLeft_Res_2nd'] = self._SrefElementDeclaration(
            _DesignObj=A50_TIA_PbodyContactPhyLen._PbodyContactPhyLen(_DesignParameter=None,
                                                                      _Name='{}:SRF_PbodyLeft_Res_2nd'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_PbodyLeft_Res_2nd']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_PbodyLeft_Res_2nd']['_Angle'] = 0

        # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_PbodyLeft_Res_2nd']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        # Define Sref _XYcoordinate
        self._DesignParameter['SRF_PbodyLeft_Res_2nd']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Res_2nd', '_PRESLayer')
        target_coord = tmp1[0][0][0]['_XY_left']
        target_coord[0] = target_coord[0] - 250
        target_coord[1] = target_coord[1] + 125
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_PbodyLeft_Res_2nd', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_PbodyLeft_Res_2nd')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_PbodyLeft_Res_2nd']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Pbodyring_right
        # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(
            A50_TIA_PbodyContactPhyLen._PbodyContactPhyLen._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length'] = None
        _Caculation_Parameters['_NumCont'] = 3
        _Caculation_Parameters['_Vtc_flag'] = True

        tmp1 = self.get_param_KJH4('SRF_Res_2nd', '_PRESLayer')

        target_length_y = abs(tmp1[0][0][0]['_XY_up'][1] - tmp1[0][0][0]['_XY_down'][1])
        _Caculation_Parameters['_Length'] = target_length_y + 250

        # Generate Sref
        self._DesignParameter['SRF_PbodyRight_Res_2nd'] = self._SrefElementDeclaration(
            _DesignObj=A50_TIA_PbodyContactPhyLen._PbodyContactPhyLen(_DesignParameter=None,
                                                                      _Name='{}:SRF_PbodyRight_Res_2nd'.format(_Name)))[
            0]

        # Define Sref Relection
        self._DesignParameter['SRF_PbodyRight_Res_2nd']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_PbodyRight_Res_2nd']['_Angle'] = 0

        # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_PbodyRight_Res_2nd']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        # Define Sref _XYcoordinate
        self._DesignParameter['SRF_PbodyRight_Res_2nd']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Res_2nd', '_PRESLayer')
        target_coord = tmp1[0][0][0]['_XY_right']
        target_coord[0] = target_coord[0] + 250
        target_coord[1] = target_coord[1] + 125
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_PbodyRight_Res_2nd', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_PbodyRight_Res_2nd')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_PbodyRight_Res_2nd']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## HDVCAP cap_2nd
        ## SREF Generation
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A50_HDVNCAP_Array._HDVNCAP_Array._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length'] = _Length_2nd
        _Caculation_Parameters['_LayoutOption'] = _LayoutOption_2nd
        _Caculation_Parameters['_NumFigPair'] = _NumFigPair_2nd
        _Caculation_Parameters['_Array_row'] = _Array_2nd_row
        _Caculation_Parameters['_Array_col'] = _Array_2nd_col
        _Caculation_Parameters['_Cbot_Ctop_metalwidth'] = _Cbot_Ctop_metalwidth_2nd

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_cap_2nd'] = self._SrefElementDeclaration(
            _DesignObj=A50_HDVNCAP_Array._HDVNCAP_Array(_DesignParameter=None, _Name='{}:SRF_cap_2nd'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_cap_2nd']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_cap_2nd']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_cap_2nd']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_cap_2nd']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_PbodyRight_Res_2nd', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_down']
        target_coord[1] = target_coord[1] - 500
        # Approaching_coord
        tmp21 = self.get_param_KJH4('SRF_cap_2nd', 'SRF_Pbodyring', 'SRF_PbodyRight','SRF_PbodyContactPhyLen','BND_Met1Layer')
        tmp22 = self.get_param_KJH4('SRF_cap_2nd', 'SRF_Pbodyring', 'SRF_PbodyTop', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coordx = tmp21[0][0][0][0][0][0]['_XY_up'][0]
        approaching_coordy = tmp22[0][0][0][0][0][0]['_XY_up'][1]
        approaching_coord = [approaching_coordx, approaching_coordy]
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_cap_2nd')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_cap_2nd']['_XYCoordinates'] = tmpXY

        ##### CBot Connection Via
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Layer1 = _LayoutOption_2nd[-1]
        _Layer2 = _LayoutOption_2nd[-1] + 1
        _Caculation_Parameters['_Layer1'] = _Layer1
        _Caculation_Parameters['_Layer2'] = _Layer2
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_CBotConn_Via'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_CBotConn_Via'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_CBotConn_Via']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_CBotConn_Via']['_Angle'] = 0

        # Calcuate _COX
        tmp1 = self.get_param_KJH4('SRF_cap_2nd','BND_MetLayer_CBotConn')
        tmpWidth = tmp1[0][0][0]['_Xwidth']
        _Caculation_Parameters['_COX'] = max(2, int(
            (tmpWidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)
        ))

        # Calcuate _COY
        _Caculation_Parameters['_COY'] = _Caculation_Parameters['_COX']

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_CBotConn_Via']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_CBotConn_Via']['_XYCoordinates'] = [[0, 0]]

        tmp2 = self.get_param_KJH4('SRF_CBotConn_Via', 'SRF_ViaM{}M{}'.format(_Layer1, _Layer2), 'BND_Met{}Layer'.format(_Layer2))
        for i in range(_Array_2nd_col//2 + 1):
            # Calculate
            # Target_coord
            target_coord = tmp1[0][i][0]['_XY_cent']

            # Approaching_coord
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']

            # Sref coord
            tmp3 = self.get_param_KJH4('SRF_CBotConn_Via')
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            # Define
        self._DesignParameter['SRF_CBotConn_Via']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_MetLayer_CBotConn_1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}'.format(_Layer2)][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}'.format(_Layer2)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_CBotConn_Via','SRF_ViaM{}M{}'.format(_Layer1, _Layer2), 'BND_Met{}Layer'.format(_Layer2))
        tmp2 = self.get_param_KJH4('SRF_Res_2nd','SRF_OutputPort1_Via','SRF_ViaM1M2','BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_MetLayer_CBotConn_1']['_YWidth'] = tmp2[0][0][0][0][0]['_XY_up_left'][1] - tmp1[0][0][0][0]['_XY_down_left'][1]

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_MetLayer_CBotConn_1']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_MetLayer_CBotConn_1']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
        # Approaching_coord
        tmp3 = self.get_param_KJH4('BND_MetLayer_CBotConn_1')
        approaching_coord = tmp3[0][0]['_XY_down_left']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['BND_MetLayer_CBotConn_1']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_MetLayer_CBotConn_2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}'.format(_Layer2)][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}'.format(_Layer2)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_MetLayer_CBotConn_2']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_MetLayer_CBotConn_2']['_XWidth'] = tmp1[-1][0][0][0]['_XY_up_right'][0] - tmp1[0][0][0][0]['_XY_up_left'][0]

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_MetLayer_CBotConn_2']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        target_coord = tmp1[0][0][0][0]['_XY_down_left']
        tmp3 = self.get_param_KJH4('BND_MetLayer_CBotConn_2')
        approaching_coord = tmp3[0][0]['_XY_down_left']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['BND_MetLayer_CBotConn_2']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_MetLayer_CBotConn_3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}'.format(_Layer2)][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}'.format(_Layer2)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_MetLayer_CBotConn_1')
        tmp2 = self.get_param_KJH4('SRF_Res_2nd','SRF_OutputPort1_Via','SRF_ViaM1M2','BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_MetLayer_CBotConn_3']['_YWidth'] = tmp2[0][0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_MetLayer_CBotConn_3']['_XWidth'] = tmp2[0][0][0][0][0]['_XY_up_right'][0] - tmp1[0][0]['_XY_up_left'][0]

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_MetLayer_CBotConn_3']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        target_coord = tmp1[0][0]['_XY_up_left']
        # Approaching_coord
        tmp3 = self.get_param_KJH4('BND_MetLayer_CBotConn_3')
        approaching_coord = tmp3[0][0]['_XY_up_left']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['BND_MetLayer_CBotConn_3']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_MetLayer_CTopConn_1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}'.format(_Layer1)][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}'.format(_Layer1)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_cap_2nd','BND_MetLayer_CTopConn')
        tmp2 = self.get_param_KJH4('SRF_Res_2nd','SRF_OutputPort2_Via','SRF_ViaM1M2','BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_MetLayer_CTopConn_1']['_YWidth'] = tmp2[0][0][0][0][0]['_XY_up'][1] - tmp1[0][0][0]['_XY_up'][1]

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_MetLayer_CTopConn_1']['_XWidth'] = tmp1[0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_MetLayer_CTopConn_1']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        for i in range((_Array_2nd_col+1)//2):
            # Calculate
            # Target_coord
            target_coord = tmp1[0][i][0]['_XY_up_left']
            # Approaching_coord
            tmp3 = self.get_param_KJH4('BND_MetLayer_CTopConn_1')
            approaching_coord = tmp3[0][0]['_XY_down_left']
            # Sref coord
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        self._DesignParameter['BND_MetLayer_CTopConn_1']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_MetLayer_CTopConn_2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}'.format(_Layer1)][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}'.format(_Layer1)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_cap_2nd','BND_MetLayer_CTopConn')
        tmp2 = self.get_param_KJH4('SRF_Res_2nd','SRF_OutputPort2_Via','SRF_ViaM1M2','BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_MetLayer_CTopConn_2']['_YWidth'] = tmp2[0][0][0][0][0]['_Ywidth']

        tmpXmax = max(tmp2[0][0][0][0][0]['_XY_right'][0], tmp1[0][-1][0]['_XY_right'][0])
        # Define Boundary_element _XWidth
        self._DesignParameter['BND_MetLayer_CTopConn_2']['_XWidth'] = tmpXmax - tmp1[0][0][0]['_XY_left'][0]

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_MetLayer_CTopConn_2']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        target_coordx = tmp1[0][0][0]['_XY_left'][0]
        target_coordy = tmp2[0][0][0][0][0]['_XY_up'][1]
        target_coord = [target_coordx, target_coordy]
        # Approaching_coord
        tmp3 = self.get_param_KJH4('BND_MetLayer_CTopConn_2')
        approaching_coord = tmp3[0][0]['_XY_up_left']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['BND_MetLayer_CTopConn_2']['_XYCoordinates'] = tmpXY


        tmp1 = self.get_param_KJH4('SRF_cap_2nd','SRF_Pbodyring', 'BND_ExtenMet1Layer_Top')
        tmp2 = self.get_param_KJH4('SRF_PbodyLeft_Res_2nd', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')

        if tmp1[0][0][0][0]['_XY_up_left'][0] > tmp2[0][0][0][0]['_XY_down_left'][0]:

            # Define Boundary_element
            self._DesignParameter['BND_Met1Layer_CapPbodyExten'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )

            tmp1 = self.get_param_KJH4('SRF_cap_2nd', 'SRF_Pbodyring', 'BND_ExtenMet1Layer_Top')
            tmp2 = self.get_param_KJH4('SRF_PbodyLeft_Res_2nd', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
            # Define Boundary_element _YWidth
            self._DesignParameter['BND_Met1Layer_CapPbodyExten']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

            # Define Boundary_element _XWidth
            self._DesignParameter['BND_Met1Layer_CapPbodyExten']['_XWidth'] = tmp1[0][0][0][0]['_XY_up_left'][0] - tmp2[0][0][0][0]['_XY_down_left'][0]

            # Calculate Sref XYcoord
            # initialize coordinate
            self._DesignParameter['BND_Met1Layer_CapPbodyExten']['_XYCoordinates'] = [[0, 0]]
            tmpXY = []

            # Calculate
            # Target_coord
            target_coord = tmp1[0][0][0][0]['_XY_up_left']
            # Approaching_coord
            tmp3 = self.get_param_KJH4('BND_Met1Layer_CapPbodyExten')
            approaching_coord = tmp3[0][0]['_XY_up_right']
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

            tmp1 = self.get_param_KJH4('SRF_cap_2nd', 'SRF_Pbodyring', 'BND_ExtenPPLayer_Top')
            tmp2 = self.get_param_KJH4('SRF_PbodyLeft_Res_2nd', 'SRF_PbodyContactPhyLen', 'BND_PPLayer')
            # Define Boundary_element _YWidth
            self._DesignParameter['BND_PPLayer_CapPbodyExten']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

            # Define Boundary_element _XWidth
            self._DesignParameter['BND_PPLayer_CapPbodyExten']['_XWidth'] = tmp1[0][0][0][0]['_XY_up_left'][0] - tmp2[0][0][0][0]['_XY_down_left'][0]

            # Calculate Sref XYcoord
            # initialize coordinate
            self._DesignParameter['BND_PPLayer_CapPbodyExten']['_XYCoordinates'] = [[0, 0]]
            tmpXY = []

            # Calculate
            # Target_coord
            target_coord = tmp1[0][0][0][0]['_XY_up_left']
            # Approaching_coord
            tmp3 = self.get_param_KJH4('BND_PPLayer_CapPbodyExten')
            approaching_coord = tmp3[0][0]['_XY_up_right']
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

            tmp1 = self.get_param_KJH4('SRF_cap_2nd', 'SRF_Pbodyring', 'BND_ExtenODLayer_Top')
            tmp2 = self.get_param_KJH4('SRF_PbodyLeft_Res_2nd', 'SRF_PbodyContactPhyLen', 'BND_ODLayer')
            # Define Boundary_element _YWidth
            self._DesignParameter['BND_ODLayer_CapPbodyExten']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

            # Define Boundary_element _XWidth
            self._DesignParameter['BND_ODLayer_CapPbodyExten']['_XWidth'] = tmp1[0][0][0][0]['_XY_up_left'][0] - tmp2[0][0][0][0]['_XY_down_left'][0]

            # Calculate Sref XYcoord
            # initialize coordinate
            self._DesignParameter['BND_ODLayer_CapPbodyExten']['_XYCoordinates'] = [[0, 0]]
            tmpXY = []

            # Calculate
            # Target_coord
            target_coord = tmp1[0][0][0][0]['_XY_up_left']
            # Approaching_coord
            tmp3 = self.get_param_KJH4('BND_ODLayer_CapPbodyExten')
            approaching_coord = tmp3[0][0]['_XY_up_right']
            # Sref coord
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

            # Define
            self._DesignParameter['BND_ODLayer_CapPbodyExten']['_XYCoordinates'] = tmpXY


        ## DRC correction -> Extension
        # Define Boundary_element
        self._DesignParameter['BND_Met1Layer_ResLeft'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_PbodyTop_Res_2nd', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_cap_2nd', 'SRF_Pbodyring', 'SRF_PbodyTop', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        tmp3 = self.get_param_KJH4('SRF_PbodyLeft_Res_2nd', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met1Layer_ResLeft']['_YWidth'] = abs(
            tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met1Layer_ResLeft']['_XWidth'] = tmp3[0][0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met1Layer_ResLeft']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord

        target_coordx = tmp3[0][0][0][0]['_XY_up'][0]
        target_coordy = tmp1[0][0][0][0]['_XY_up'][1]
        target_coord = [target_coordx, target_coordy]
        # Approaching_coord
        tmp3 = self.get_param_KJH4('BND_Met1Layer_ResLeft')
        approaching_coord = tmp3[0][0]['_XY_up']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        # Define
        self._DesignParameter['BND_Met1Layer_ResLeft']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_Met1Layer_ResRight'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_PbodyTop_Res_2nd', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_cap_2nd', 'SRF_Pbodyring', 'SRF_PbodyTop', 'SRF_PbodyContactPhyLen',
                                   'BND_Met1Layer')
        tmp3 = self.get_param_KJH4('SRF_PbodyRight_Res_2nd', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met1Layer_ResRight']['_YWidth'] = abs(
            tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met1Layer_ResRight']['_XWidth'] = tmp3[0][0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met1Layer_ResRight']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        target_coordx = tmp3[0][0][0][0]['_XY_up'][0]
        target_coordy = tmp1[0][0][0][0]['_XY_up'][1]
        target_coord = [target_coordx, target_coordy]
        # Approaching_coord
        tmp3 = self.get_param_KJH4('BND_Met1Layer_ResRight')
        approaching_coord = tmp3[0][0]['_XY_up']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        # Define
        self._DesignParameter['BND_Met1Layer_ResRight']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_PPLayer_ResLeft'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_PbodyTop_Res_2nd', 'SRF_PbodyContactPhyLen', 'BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_cap_2nd', 'SRF_Pbodyring', 'SRF_PbodyTop', 'SRF_PbodyContactPhyLen',
                                   'BND_PPLayer')
        tmp3 = self.get_param_KJH4('SRF_PbodyLeft_Res_2nd', 'SRF_PbodyContactPhyLen', 'BND_PPLayer')
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_PPLayer_ResLeft']['_YWidth'] = abs(
            tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_PPLayer_ResLeft']['_XWidth'] = tmp3[0][0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_PPLayer_ResLeft']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord

        target_coordx = tmp3[0][0][0][0]['_XY_up'][0]
        target_coordy = tmp1[0][0][0][0]['_XY_up'][1]
        target_coord = [target_coordx, target_coordy]
        # Approaching_coord
        tmp3 = self.get_param_KJH4('BND_PPLayer_ResLeft')
        approaching_coord = tmp3[0][0]['_XY_up']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        # Define
        self._DesignParameter['BND_PPLayer_ResLeft']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_PPLayer_ResRight'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_PbodyTop_Res_2nd', 'SRF_PbodyContactPhyLen', 'BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_cap_2nd', 'SRF_Pbodyring', 'SRF_PbodyTop', 'SRF_PbodyContactPhyLen',
                                   'BND_PPLayer')
        tmp3 = self.get_param_KJH4('SRF_PbodyRight_Res_2nd', 'SRF_PbodyContactPhyLen', 'BND_PPLayer')
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_PPLayer_ResRight']['_YWidth'] = abs(
            tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_PPLayer_ResRight']['_XWidth'] = tmp3[0][0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_PPLayer_ResRight']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord

        target_coordx = tmp3[0][0][0][0]['_XY_up'][0]
        target_coordy = tmp1[0][0][0][0]['_XY_up'][1]
        target_coord = [target_coordx, target_coordy]
        # Approaching_coord
        tmp3 = self.get_param_KJH4('BND_PPLayer_ResRight')
        approaching_coord = tmp3[0][0]['_XY_up']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        # Define
        self._DesignParameter['BND_PPLayer_ResRight']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_ODLayer_ResLeft'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0],
            _Datatype=DesignParameters._LayerMapping['DIFF'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_PbodyTop_Res_2nd', 'SRF_PbodyContactPhyLen', 'BND_ODLayer')
        tmp2 = self.get_param_KJH4('SRF_cap_2nd', 'SRF_Pbodyring', 'SRF_PbodyTop', 'SRF_PbodyContactPhyLen',
                                   'BND_ODLayer')
        tmp3 = self.get_param_KJH4('SRF_PbodyLeft_Res_2nd', 'SRF_PbodyContactPhyLen', 'BND_ODLayer')
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_ODLayer_ResLeft']['_YWidth'] = abs(
            tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_ODLayer_ResLeft']['_XWidth'] = tmp3[0][0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_ODLayer_ResLeft']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord

        target_coordx = tmp3[0][0][0][0]['_XY_up'][0]
        target_coordy = tmp1[0][0][0][0]['_XY_up'][1]
        target_coord = [target_coordx, target_coordy]
        # Approaching_coord
        tmp3 = self.get_param_KJH4('BND_ODLayer_ResLeft')
        approaching_coord = tmp3[0][0]['_XY_up']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        # Define
        self._DesignParameter['BND_ODLayer_ResLeft']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_ODLayer_ResRight'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0],
            _Datatype=DesignParameters._LayerMapping['DIFF'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_PbodyTop_Res_2nd', 'SRF_PbodyContactPhyLen', 'BND_ODLayer')
        tmp2 = self.get_param_KJH4('SRF_cap_2nd', 'SRF_Pbodyring', 'SRF_PbodyTop', 'SRF_PbodyContactPhyLen',
                                   'BND_ODLayer')
        tmp3 = self.get_param_KJH4('SRF_PbodyRight_Res_2nd', 'SRF_PbodyContactPhyLen', 'BND_ODLayer')
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_ODLayer_ResRight']['_YWidth'] = abs(
            tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_ODLayer_ResRight']['_XWidth'] = tmp3[0][0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_ODLayer_ResRight']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord

        target_coordx = tmp3[0][0][0][0]['_XY_up'][0]
        target_coordy = tmp1[0][0][0][0]['_XY_up'][1]
        target_coord = [target_coordx, target_coordy]
        # Approaching_coord
        tmp3 = self.get_param_KJH4('BND_ODLayer_ResRight')
        approaching_coord = tmp3[0][0]['_XY_up']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        # Define
        self._DesignParameter['BND_ODLayer_ResRight']['_XYCoordinates'] = tmpXY




        print('##############################')
        print('##     Calculation_End    ##')
        print('##############################')


## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_YCH
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    # libname = 'Proj_A53_TIA_RCfeedback_2ndstage_v11'
    cellname = 'A53_TIA_RCfeedback_2ndstage_v15'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        # Res_2nd
        _ResWidth_2nd=1000,
        _ResLength_2nd=5850,
        _CONUMX_2nd=None,
        _CONUMY_2nd=None,
        _SeriesStripes_2nd=3,
        _ParallelStripes_2nd=1,
        _Res_Port1Layer=5,
        _Res_Port2Layer=5,

        # Cap_2nd
        _Length_2nd=9000,
        _LayoutOption_2nd=[2,3,4],
        _NumFigPair_2nd=21,
        _Array_2nd_row=2,
        _Array_2nd_col=3,
        _Cbot_Ctop_metalwidth_2nd=500,

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
    LayoutObj = _TIA_RCfeedback_2ndstage(_DesignParameter=None, _Name=cellname)
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