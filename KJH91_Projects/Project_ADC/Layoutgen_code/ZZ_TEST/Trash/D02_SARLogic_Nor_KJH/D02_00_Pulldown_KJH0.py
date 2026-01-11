
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


## Define Class
class _Pulldown(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(

        # NMOSA
        _NMOSA_NMOSNumberofGate=7,  # number
        _NMOSA_NMOSChannelWidth=700,  # number
        _NMOSA_NMOSChannellength=30,  # number
        _NMOSA_GateSpacing=None,  # None/number
        _NMOSA_SDWidth=None,  # None/number
        _NMOSA_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _NMOSA_PCCrit=True,  # None/True

            # Source_node_ViaM1M2
        _NMOSA_Source_Via_TF=True,  # True/False

            # Drain_node_ViaM1M2
        _NMOSA_Drain_Via_TF=True,  # True/False

            # POLY dummy setting
        _NMOSA_NMOSDummy=True,  # TF
            # if _PMOSDummy == True
        _NMOSA_NMOSDummy_length=None,  # None/Value
        _NMOSA_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # NMOSB
        _NMOSB_NMOSNumberofGate=7,  # number
        _NMOSB_NMOSChannelWidth=700,  # number
        _NMOSB_NMOSChannellength=30,  # number
        _NMOSB_GateSpacing=None,  # None/number
        _NMOSB_SDWidth=None,  # None/number
        _NMOSB_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _NMOSB_PCCrit=True,  # None/True

            # Source_node_ViaM1M2
        _NMOSB_Source_Via_TF=True,  # True/False

            # Drain_node_ViaM1M2
        _NMOSB_Drain_Via_TF=True,  # True/False

            # POLY dummy setting
        _NMOSB_NMOSDummy=True,  # TF
            # if _PMOSDummy == True
        _NMOSB_NMOSDummy_length=None,  # None/Value
        _NMOSB_NMOSDummy_placement=None,  # None/'Up'/'Dn'/


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
                                  _NMOSA_NMOSNumberofGate=7,  # number
                                  _NMOSA_NMOSChannelWidth=700,  # number
                                  _NMOSA_NMOSChannellength=30,  # number
                                  _NMOSA_GateSpacing=None,  # None/number
                                  _NMOSA_SDWidth=None,  # None/number
                                  _NMOSA_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _NMOSA_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _NMOSA_Source_Via_TF=True,  # True/False

                                  # Drain_node_ViaM1M2
                                  _NMOSA_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _NMOSA_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _NMOSA_NMOSDummy_length=None,  # None/Value
                                  _NMOSA_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # NMOSB
                                  _NMOSB_NMOSNumberofGate=7,  # number
                                  _NMOSB_NMOSChannelWidth=700,  # number
                                  _NMOSB_NMOSChannellength=30,  # number
                                  _NMOSB_GateSpacing=None,  # None/number
                                  _NMOSB_SDWidth=None,  # None/number
                                  _NMOSB_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _NMOSB_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _NMOSB_Source_Via_TF=True,  # True/False

                                  # Drain_node_ViaM1M2
                                  _NMOSB_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _NMOSB_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _NMOSB_NMOSDummy_length=None,  # None/Value
                                  _NMOSB_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

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
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_NMOSA_power_v2._NMOSA_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A03_NmosWithDummy_KJH3._NmosWithDummy_KJH3._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOSNumberofGate']     = _NMOSA_NMOSNumberofGate
        _Caculation_Parameters['_NMOSChannelWidth']     = _NMOSA_NMOSChannelWidth
        _Caculation_Parameters['_NMOSChannellength']    = _NMOSA_NMOSChannellength
        _Caculation_Parameters['_GateSpacing']          = _NMOSA_GateSpacing
        _Caculation_Parameters['_SDWidth']              = _NMOSA_SDWidth
        _Caculation_Parameters['_XVT']                  = _NMOSA_XVT
        _Caculation_Parameters['_PCCrit']               = _NMOSA_PCCrit
        _Caculation_Parameters['_Source_Via_TF']        = _NMOSA_Source_Via_TF
        _Caculation_Parameters['_Drain_Via_TF']         = _NMOSA_Drain_Via_TF
        _Caculation_Parameters['_NMOSDummy']            = _NMOSA_NMOSDummy
        _Caculation_Parameters['_NMOSDummy_length']     = _NMOSA_NMOSDummy_length
        _Caculation_Parameters['_NMOSDummy_placement']  = _NMOSA_NMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_NMOSA_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_NMOSA_power_v2._NMOSA_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_NMOSA'] = self._SrefElementDeclaration(_DesignObj=A03_NmosWithDummy_KJH3._NmosWithDummy_KJH3(_DesignParameter=None, _Name='{}:SRF_NMOSA'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOSA_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_NMOSA']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOSA_POWER'
        self._DesignParameter['SRF_NMOSA']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOSA_POWER'
        self._DesignParameter['SRF_NMOSA']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOSA_POWER'
        self._DesignParameter['SRF_NMOSA']['_XYCoordinates'] = [[0, 0]]

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Drain Combine Upward
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Drain Hrz M2
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NMOSA_Drain_Hrz_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth : ViaYmin 기준
        self._DesignParameter['BND_NMOSA_Drain_Hrz_M2']['_YWidth'] = _DRCobj._VIAxMinWidth + + 2 * max([_DRCobj._Metal1MinEnclosureVia1, _DRCobj._MetalxMinEnclosureCO])

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_NMOSA', 'BND_Met1Layer_Drain')
        self._DesignParameter['BND_NMOSA_Drain_Hrz_M2']['_XWidth'] = abs(tmp[0][-1][0]['_XY_right'][0] - tmp[0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NMOSA_Drain_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        ## Calculate Sref XYcoord
            ## Calculate
                ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_NMOSA','SRF_Drain_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
        target_coord = tmp1[0][0][0][0][0]['_XY_up_left']
                ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NMOSA_Drain_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NMOSA_Drain_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_NMOSA_Drain_Hrz_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  NMOS: Poly combine
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Poly combine : Vtc
        ## Pre-defined
        Ywidth_0 = 150

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NMOSA_Gate_Vtc_poly'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_NMOSA_Gate_Vtc_poly']['_YWidth'] = Ywidth_0

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_NMOSA', 'BND_POLayer')
        self._DesignParameter['BND_NMOSA_Gate_Vtc_poly']['_XWidth'] = tmp[0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NMOSA_Gate_Vtc_poly']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_NMOSA_Gate_Vtc_poly']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        tmp = self.get_param_KJH4('SRF_NMOSA', 'BND_POLayer')
        for i in range(0, len(tmp[0])):
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_NMOSA', 'BND_POLayer')
            target_coord = tmp1[0][i][0]['_XY_up_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_NMOSA_Gate_Vtc_poly')
            approaching_coord = tmp2[0][0]['_XY_down_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_NMOSA_Gate_Vtc_poly')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_NMOSA_Gate_Vtc_poly']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Poly combine : Hrz
        ## Pre-defined
        Ywidth_1 = 70

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NMOSA_Gate_Hrz_poly'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_NMOSA_Gate_Hrz_poly']['_YWidth'] = Ywidth_1

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_NMOSA', 'BND_POLayer')
        self._DesignParameter['BND_NMOSA_Gate_Hrz_poly']['_XWidth'] = abs( tmp1[0][0][0]['_XY_left'][0] - tmp1[0][-1][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NMOSA_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
            ## initialized Sref coordinate
        self._DesignParameter['BND_NMOSA_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
                ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_NMOSA_Gate_Vtc_poly')
        target_coord = tmp1[0][0]['_XY_up_left']
                ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NMOSA_Gate_Hrz_poly')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NMOSA_Gate_Hrz_poly')
        Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_NMOSA_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  NMOS: Gate _ViaM0M1
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Gate _ViaM0M1 : Metal1

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NMOSA_Gate_Hrz_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('BND_NMOSA_Gate_Hrz_poly')
        self._DesignParameter['BND_NMOSA_Gate_Hrz_M1']['_YWidth'] = tmp[0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('BND_NMOSA_Gate_Hrz_poly')
        self._DesignParameter['BND_NMOSA_Gate_Hrz_M1']['_XWidth'] = tmp[0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NMOSA_Gate_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
            ## initialized Sref coordinate
        self._DesignParameter['BND_NMOSA_Gate_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
                ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_NMOSA_Gate_Hrz_poly')
        target_coord = tmp1[0][0]['_XY_down_left']
                ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NMOSA_Gate_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NMOSA_Gate_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_NMOSA_Gate_Hrz_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Gate _ViaM0M1 : _ViaM0M1
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 0
        _Caculation_Parameters['_Layer2'] = 1
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

            ## Sref ViaX declaration
        self._DesignParameter['SRF_NMOSA_Gate_ViaM0M1'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None, _Name='{}:SRF_NMOSA_Gate_ViaM0M1'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_NMOSA_Gate_ViaM0M1']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_NMOSA_Gate_ViaM0M1']['_Angle'] = 0

            ## Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH4('BND_NMOSA_Gate_Hrz_M1')
        tmp2 = self.get_param_KJH4('BND_NMOSA_Gate_Hrz_poly')
        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

        ## Define _COX and _COY
        if _COX < 2:
            ## Finger = 1
            if _NMOSA_NMOSNumberofGate == 1:
                _Caculation_Parameters['_COX'] = 1
                _Caculation_Parameters['_COY'] = 2
                flag = 2
                ## Finger = 2
            else:
                _Caculation_Parameters['_COX'] = 2
                _Caculation_Parameters['_COY'] = _COY
                flag = 1
        else:
            _Caculation_Parameters['_COX'] = _COX
            _Caculation_Parameters['_COY'] = _COY
            flag = 0

        if flag == 0:
            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin,
            self._DesignParameter['SRF_NMOSA_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameterYmin(
                **_Caculation_Parameters)

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['SRF_NMOSA_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_NMOSA_Gate_Hrz_M1')
            target_coord = tmp1[0][0]['_XY_cent']
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_NMOSA_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_NMOSA_Gate_ViaM0M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define
            self._DesignParameter['SRF_NMOSA_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY

        if flag == 1:
            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin,
            self._DesignParameter['SRF_NMOSA_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameterYmin(
                **_Caculation_Parameters)

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['SRF_NMOSA_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_NMOSA_Gate_Hrz_M1')
            target_coord = tmp1[0][0]['_XY_cent']
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_NMOSA_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_NMOSA_Gate_ViaM0M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define
            self._DesignParameter['SRF_NMOSA_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Gate _ViaM0M1 : _ViaM0M1 : Poly Exten
            ## Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH4('SRF_NMOSA_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            self._DesignParameter['BND_NMOSA_Gate_Hrz_poly']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_NMOSA_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['BND_NMOSA_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord: _XY_type1
            ## X
            tmp1_1 = self.get_param_KJH4('SRF_NMOSA_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            target_coordx = tmp1_1[0][0][0][0]['_XY_left'][0]
            ## Y
            tmp1_2 = self.get_param_KJH4('BND_NMOSA_Gate_Vtc_poly')
            target_coordy = tmp1_2[0][0]['_XY_up'][1]

            target_coord = [target_coordx, target_coordy]
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_NMOSA_Gate_Hrz_poly')
            approaching_coord = tmp2[0][0]['_XY_up_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_NMOSA_Gate_Hrz_poly')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_NMOSA_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Gate _ViaM0M1 : _ViaM0M1 : M1 Exten
            ## Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH4('BND_NMOSA_Gate_Hrz_poly')
            self._DesignParameter['BND_NMOSA_Gate_Hrz_M1']['_XWidth'] = tmp1[0][0]['_Xwidth']

            ## Define Boundary_element _XYCoordinates
            tmp1 = self.get_param_KJH4('BND_NMOSA_Gate_Hrz_poly')
            self._DesignParameter['BND_NMOSA_Gate_Hrz_M1']['_XYCoordinates'] = [tmp1[0][0]['_XY_down_left']]

        if flag == 2:
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Gate _ViaM0M1 : _ViaM0M1 : Xmin
            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin,
            self._DesignParameter['SRF_NMOSA_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameter( **_Caculation_Parameters)

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['SRF_NMOSA_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_NMOSA_Gate_Hrz_M1')
            target_coord = tmp1[0][0]['_XY_up']
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_NMOSA_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_NMOSA_Gate_ViaM0M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define
            self._DesignParameter['SRF_NMOSA_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Gate _ViaM0M1 : _ViaM0M1 : Poly Exten
            ## Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH4('SRF_NMOSA_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_POLayer')
            self._DesignParameter['BND_NMOSA_Gate_Hrz_poly']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']

            ## Define Boundary_element _YWidth
            tmp1 = self.get_param_KJH4('SRF_NMOSA_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_POLayer')
            self._DesignParameter['BND_NMOSA_Gate_Hrz_poly']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_NMOSA_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['BND_NMOSA_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord: _XY_type1
            ## X
            tmp1_1 = self.get_param_KJH4('SRF_NMOSA_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_POLayer')
            target_coord = tmp1_1[0][0][0][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_NMOSA_Gate_Hrz_poly')
            approaching_coord = tmp2[0][0]['_XY_down_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_NMOSA_Gate_Hrz_poly')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_NMOSA_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Gate _ViaM0M1 : _ViaM0M1 : M1 Exten
            ## Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH4('SRF_NMOSA_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            self._DesignParameter['BND_NMOSA_Gate_Hrz_M1']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']

            ## Define Boundary_element _YWidth
            tmp1 = self.get_param_KJH4('SRF_NMOSA_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            self._DesignParameter['BND_NMOSA_Gate_Hrz_M1']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

            ## Define Boundary_element _XYCoordinates
            tmp1 = self.get_param_KJH4('SRF_NMOSA_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            self._DesignParameter['BND_NMOSA_Gate_Hrz_M1']['_XYCoordinates'] = [tmp1[0][0][0][0]['_XY_down_left']]













        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  NMOS: Sref Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_NMOSB_power_v2._NMOSB_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A03_NmosWithDummy_KJH3._NmosWithDummy_KJH3._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOSNumberofGate']     = _NMOSB_NMOSNumberofGate
        _Caculation_Parameters['_NMOSChannelWidth']     = _NMOSB_NMOSChannelWidth
        _Caculation_Parameters['_NMOSChannellength']    = _NMOSB_NMOSChannellength
        _Caculation_Parameters['_GateSpacing']          = _NMOSB_GateSpacing
        _Caculation_Parameters['_SDWidth']              = _NMOSB_SDWidth
        _Caculation_Parameters['_XVT']                  = _NMOSB_XVT
        _Caculation_Parameters['_PCCrit']               = _NMOSB_PCCrit
        _Caculation_Parameters['_Source_Via_TF']        = _NMOSB_Source_Via_TF
        _Caculation_Parameters['_Drain_Via_TF']         = _NMOSB_Drain_Via_TF
        _Caculation_Parameters['_NMOSDummy']            = _NMOSB_NMOSDummy
        _Caculation_Parameters['_NMOSDummy_length']     = _NMOSB_NMOSDummy_length
        _Caculation_Parameters['_NMOSDummy_placement']  = _NMOSB_NMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_NMOSB_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_NMOSB_power_v2._NMOSB_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_NMOSB'] = self._SrefElementDeclaration(_DesignObj=A03_NmosWithDummy_KJH3._NmosWithDummy_KJH3(_DesignParameter=None, _Name='{}:SRF_NMOSB'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOSB_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_NMOSB']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOSB_POWER'
        self._DesignParameter['SRF_NMOSB']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOSB_POWER'
        self._DesignParameter['SRF_NMOSB']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOSB_POWER'
        self._DesignParameter['SRF_NMOSB']['_XYCoordinates'] = [[0, 0]]

               ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_NMOSB']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ## x
        tmp1_1 = self.get_param_KJH4('SRF_NMOSA','BND_PODummyLayer')
        target_coordx = tmp1_1[0][-1][0]['_XY_left'][0]
                                ## y
        tmp1_2 = self.get_param_KJH4('SRF_NMOSA','BND_{}Layer'.format(_NMOSA_XVT))
        target_coordy = tmp1_2[0][0][0]['_XY_up'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ## x
        tmp2_1 = self.get_param_KJH4('SRF_NMOSB','BND_PODummyLayer')
        approaching_coordx = tmp2_1[0][0][0]['_XY_left'][0]
                                ## y
        tmp2_2 = self.get_param_KJH4('SRF_NMOSB','BND_{}Layer'.format(_NMOSA_XVT))
        approaching_coordy = tmp2_2[0][0][0]['_XY_up'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_NMOSB')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_NMOSB']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Drain Combine Upward
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Drain Hrz M2
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NMOSB_Drain_Hrz_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth : ViaYmin 기준
        self._DesignParameter['BND_NMOSB_Drain_Hrz_M2']['_YWidth'] = _DRCobj._VIAxMinWidth + + 2 * max([_DRCobj._Metal1MinEnclosureVia1, _DRCobj._MetalxMinEnclosureCO])

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_NMOSB', 'BND_Met1Layer_Drain')
        self._DesignParameter['BND_NMOSB_Drain_Hrz_M2']['_XWidth'] = abs(tmp[0][-1][0]['_XY_right'][0] - tmp[0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NMOSB_Drain_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        ## Calculate Sref XYcoord
            ## Calculate
                ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_NMOSB','SRF_Drain_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
        target_coord = tmp1[0][0][0][0][0]['_XY_up_left']
                ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NMOSB_Drain_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NMOSB_Drain_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_NMOSB_Drain_Hrz_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  NMOS: Poly combine
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Poly combine : Vtc
        ## Pre-defined
        Ywidth_1 = 150

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NMOSB_Gate_Vtc_poly'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_NMOSB_Gate_Vtc_poly']['_YWidth'] = Ywidth_1

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_NMOSB', 'BND_POLayer')
        self._DesignParameter['BND_NMOSB_Gate_Vtc_poly']['_XWidth'] = tmp[0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NMOSB_Gate_Vtc_poly']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_NMOSB_Gate_Vtc_poly']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        tmp = self.get_param_KJH4('SRF_NMOSB', 'BND_POLayer')
        for i in range(0, len(tmp[0])):
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_NMOSB', 'BND_POLayer')
            target_coord = tmp1[0][i][0]['_XY_up_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_NMOSB_Gate_Vtc_poly')
            approaching_coord = tmp2[0][0]['_XY_down_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_NMOSB_Gate_Vtc_poly')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_NMOSB_Gate_Vtc_poly']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Poly combine : Hrz
        ## Pre-defined
        Ywidth_1 = 70

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NMOSB_Gate_Hrz_poly'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_NMOSB_Gate_Hrz_poly']['_YWidth'] = Ywidth_1

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_NMOSB', 'BND_POLayer')
        self._DesignParameter['BND_NMOSB_Gate_Hrz_poly']['_XWidth'] = abs( tmp1[0][0][0]['_XY_left'][0] - tmp1[0][-1][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NMOSB_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
            ## initialized Sref coordinate
        self._DesignParameter['BND_NMOSB_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
                ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_NMOSB_Gate_Vtc_poly')
        target_coord = tmp1[0][0]['_XY_up_left']
                ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NMOSB_Gate_Hrz_poly')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NMOSB_Gate_Hrz_poly')
        Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_NMOSB_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  NMOS: Gate _ViaM0M1
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Gate _ViaM0M1 : Metal1

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NMOSB_Gate_Hrz_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('BND_NMOSB_Gate_Hrz_poly')
        self._DesignParameter['BND_NMOSB_Gate_Hrz_M1']['_YWidth'] = tmp[0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('BND_NMOSB_Gate_Hrz_poly')
        self._DesignParameter['BND_NMOSB_Gate_Hrz_M1']['_XWidth'] = tmp[0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NMOSB_Gate_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
            ## initialized Sref coordinate
        self._DesignParameter['BND_NMOSB_Gate_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
                ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_NMOSB_Gate_Hrz_poly')
        target_coord = tmp1[0][0]['_XY_down_left']
                ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NMOSB_Gate_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NMOSB_Gate_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_NMOSB_Gate_Hrz_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Gate _ViaM0M1 : _ViaM0M1
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 0
        _Caculation_Parameters['_Layer2'] = 1
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

            ## Sref ViaX declaration
        self._DesignParameter['SRF_NMOSB_Gate_ViaM0M1'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None, _Name='{}:SRF_NMOSB_Gate_ViaM0M1'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_NMOSB_Gate_ViaM0M1']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_NMOSB_Gate_ViaM0M1']['_Angle'] = 0

            ## Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH4('BND_NMOSB_Gate_Hrz_M1')
        tmp2 = self.get_param_KJH4('BND_NMOSB_Gate_Hrz_poly')
        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

        ## Define _COX and _COY
        if _COX < 2:
            ## Finger = 1
            if _NMOSB_NMOSNumberofGate == 1:
                _Caculation_Parameters['_COX'] = 1
                _Caculation_Parameters['_COY'] = 2
                flag = 2
                ## Finger = 2
            else:
                _Caculation_Parameters['_COX'] = 2
                _Caculation_Parameters['_COY'] = _COY
                flag = 1
        else:
            _Caculation_Parameters['_COX'] = _COX
            _Caculation_Parameters['_COY'] = _COY
            flag = 0

        if flag == 0:
            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin,
            self._DesignParameter['SRF_NMOSB_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameterYmin(
                **_Caculation_Parameters)

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['SRF_NMOSB_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_NMOSB_Gate_Hrz_M1')
            target_coord = tmp1[0][0]['_XY_cent']
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_NMOSB_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_NMOSB_Gate_ViaM0M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define
            self._DesignParameter['SRF_NMOSB_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY

        if flag == 1:
            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin,
            self._DesignParameter['SRF_NMOSB_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameterYmin(
                **_Caculation_Parameters)

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['SRF_NMOSB_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_NMOSB_Gate_Hrz_M1')
            target_coord = tmp1[0][0]['_XY_cent']
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_NMOSB_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_NMOSB_Gate_ViaM0M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define
            self._DesignParameter['SRF_NMOSB_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Gate _ViaM0M1 : _ViaM0M1 : Poly Exten
            ## Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH4('SRF_NMOSB_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            self._DesignParameter['BND_NMOSB_Gate_Hrz_poly']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_NMOSB_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['BND_NMOSB_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord: _XY_type1
            ## X
            tmp1_1 = self.get_param_KJH4('SRF_NMOSB_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            target_coordx = tmp1_1[0][0][0][0]['_XY_left'][0]
            ## Y
            tmp1_2 = self.get_param_KJH4('BND_NMOSB_Gate_Vtc_poly')
            target_coordy = tmp1_2[0][0]['_XY_up'][1]

            target_coord = [target_coordx, target_coordy]
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_NMOSB_Gate_Hrz_poly')
            approaching_coord = tmp2[0][0]['_XY_up_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_NMOSB_Gate_Hrz_poly')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_NMOSB_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Gate _ViaM0M1 : _ViaM0M1 : M1 Exten
            ## Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH4('BND_NMOSB_Gate_Hrz_poly')
            self._DesignParameter['BND_NMOSB_Gate_Hrz_M1']['_XWidth'] = tmp1[0][0]['_Xwidth']

            ## Define Boundary_element _XYCoordinates
            tmp1 = self.get_param_KJH4('BND_NMOSB_Gate_Hrz_poly')
            self._DesignParameter['BND_NMOSB_Gate_Hrz_M1']['_XYCoordinates'] = [tmp1[0][0]['_XY_down_left']]

        if flag == 2:
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Gate _ViaM0M1 : _ViaM0M1 : Xmin
            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin,
            self._DesignParameter['SRF_NMOSB_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameter( **_Caculation_Parameters)

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['SRF_NMOSB_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_NMOSB_Gate_Hrz_M1')
            target_coord = tmp1[0][0]['_XY_up']
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_NMOSB_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_NMOSB_Gate_ViaM0M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define
            self._DesignParameter['SRF_NMOSB_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Gate _ViaM0M1 : _ViaM0M1 : Poly Exten
            ## Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH4('SRF_NMOSB_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_POLayer')
            self._DesignParameter['BND_NMOSB_Gate_Hrz_poly']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']

            ## Define Boundary_element _YWidth
            tmp1 = self.get_param_KJH4('SRF_NMOSB_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_POLayer')
            self._DesignParameter['BND_NMOSB_Gate_Hrz_poly']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_NMOSB_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['BND_NMOSB_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord: _XY_type1
            ## X
            tmp1_1 = self.get_param_KJH4('SRF_NMOSB_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_POLayer')
            target_coord = tmp1_1[0][0][0][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_NMOSB_Gate_Hrz_poly')
            approaching_coord = tmp2[0][0]['_XY_down_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_NMOSB_Gate_Hrz_poly')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_NMOSB_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Gate _ViaM0M1 : _ViaM0M1 : M1 Exten
            ## Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH4('SRF_NMOSB_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            self._DesignParameter['BND_NMOSB_Gate_Hrz_M1']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']

            ## Define Boundary_element _YWidth
            tmp1 = self.get_param_KJH4('SRF_NMOSB_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            self._DesignParameter['BND_NMOSB_Gate_Hrz_M1']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

            ## Define Boundary_element _XYCoordinates
            tmp1 = self.get_param_KJH4('SRF_NMOSB_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            self._DesignParameter['BND_NMOSB_Gate_Hrz_M1']['_XYCoordinates'] = [tmp1[0][0][0][0]['_XY_down_left']]











        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOSB NMOSA Drain Connection

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NMOSAB_Drain_Hrz_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('BND_NMOSA_Drain_Hrz_M2')
        self._DesignParameter['BND_NMOSAB_Drain_Hrz_M2']['_YWidth'] = tmp[0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('BND_NMOSA_Drain_Hrz_M2')
        tmp2 = self.get_param_KJH4('BND_NMOSB_Drain_Hrz_M2')
        self._DesignParameter['BND_NMOSAB_Drain_Hrz_M2']['_XWidth'] = abs( tmp2[0][0]['_XY_right'][0] - tmp1[0][0]['_XY_left'][0] )

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NMOSAB_Drain_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
            ## initialized Sref coordinate
        self._DesignParameter['BND_NMOSAB_Drain_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
                ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_NMOSB_Drain_Hrz_M2')
        target_coord = tmp1[0][0]['_XY_down_right']
                ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NMOSAB_Drain_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_down_right']
                ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NMOSAB_Drain_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_NMOSAB_Drain_Hrz_M2']['_XYCoordinates'] = tmpXY




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
    cellname = 'D02_00_Pulldown_v0_81'
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
    LayoutObj = _Pulldown(_DesignParameter=None, _Name=cellname)
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
