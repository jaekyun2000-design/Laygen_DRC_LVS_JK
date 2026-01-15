
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
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A03_NmosWithDummy_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A04_PmosWithDummy_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A08_PbodyContactPhyLen_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A07_NbodyContactPhyLen_KJH2


## Define Class
class _Pullup(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(

        # PMOSA
        _PMOSA_PMOSNumberofGate=7,  # number
        _PMOSA_PMOSChannelWidth=700,  # number
        _PMOSA_PMOSChannellength=30,  # number
        _PMOSA_GateSpacing=None,  # None/number
        _PMOSA_SDWidth=None,  # None/number
        _PMOSA_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _PMOSA_PCCrit=True,  # None/True

            # Source_node_ViaM1M2
        _PMOSA_Source_Via_TF=True,  # True/False

            # Drain_node_ViaM1M2
        _PMOSA_Drain_Via_TF=True,  # True/False

            # POLY dummy setting
        _PMOSA_PMOSDummy=True,  # TF
            # if _PMOSDummy == True
        _PMOSA_PMOSDummy_length=None,  # None/Value
        _PMOSA_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # PMOSB
        _PMOSB_PMOSNumberofGate=7,  # number
        _PMOSB_PMOSChannelWidth=700,  # number
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
        _PMOSB_PMOSDummy_placement=None,  # None/'Up'/'Dn'/


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

                                  # PMOSA
                                  _PMOSA_PMOSNumberofGate=7,  # number
                                  _PMOSA_PMOSChannelWidth=700,  # number
                                  _PMOSA_PMOSChannellength=30,  # number
                                  _PMOSA_GateSpacing=None,  # None/number
                                  _PMOSA_SDWidth=None,  # None/number
                                  _PMOSA_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _PMOSA_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _PMOSA_Source_Via_TF=True,  # True/False

                                  # Drain_node_ViaM1M2
                                  _PMOSA_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _PMOSA_PMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _PMOSA_PMOSDummy_length=None,  # None/Value
                                  _PMOSA_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # PMOSB
                                  _PMOSB_PMOSNumberofGate=7,  # number
                                  _PMOSB_PMOSChannelWidth=700,  # number
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
                                  _PMOSB_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  PMOS: Sref Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_PMOSA_power_v2._PMOSA_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A04_PmosWithDummy_KJH3._PmosWithDummy_KJH3._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_PMOSAPOWER_PbodyContact_1_Length']  = _PMOSAPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_PMOSNumberofGate']     = _PMOSA_PMOSNumberofGate
        _Caculation_Parameters['_PMOSChannelWidth']     = _PMOSA_PMOSChannelWidth
        _Caculation_Parameters['_PMOSChannellength']    = _PMOSA_PMOSChannellength
        _Caculation_Parameters['_GateSpacing']          = _PMOSA_GateSpacing
        _Caculation_Parameters['_SDWidth']              = _PMOSA_SDWidth
        _Caculation_Parameters['_XVT']                  = _PMOSA_XVT
        _Caculation_Parameters['_PCCrit']               = _PMOSA_PCCrit
        _Caculation_Parameters['_Source_Via_TF']        = _PMOSA_Source_Via_TF
        _Caculation_Parameters['_Drain_Via_TF']         = _PMOSA_Drain_Via_TF
        _Caculation_Parameters['_PMOSDummy']            = _PMOSA_PMOSDummy
        _Caculation_Parameters['_PMOSDummy_length']     = _PMOSA_PMOSDummy_length
        _Caculation_Parameters['_PMOSDummy_placement']  = _PMOSA_PMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_PMOSA_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_PMOSA_power_v2._PMOSA_POWER( _DesignParameter=None, _Name='{}:PMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_PMOSA'] = self._SrefElementDeclaration(_DesignObj=A04_PmosWithDummy_KJH3._PmosWithDummy_KJH3(_DesignParameter=None, _Name='{}:SRF_PMOSA'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_PMOSA_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_PMOSA']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_PMOSA']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_PMOSA']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_PMOSA_POWER'
        self._DesignParameter['SRF_PMOSA']['_XYCoordinates'] = [[0, 0]]

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOSA: Drain Combine DNward
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOSA: Drain Vtc M2
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOSA_Drain_Vtc_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth : ViaYmin 기준
        tmp1 = self.get_param_KJH4('SRF_PMOSA','BND_Met1Layer_Drain')
        tmp2 = self.get_param_KJH4('SRF_PMOSA','SRF_Drain_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
        self._DesignParameter['BND_PMOSA_Drain_Vtc_M2']['_YWidth'] = abs( tmp2[0][0][0][0][0]['_XY_down'][1] - tmp1[0][0][0]['_XY_down'][1] )

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_PMOSA','SRF_Drain_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
        self._DesignParameter['BND_PMOSA_Drain_Vtc_M2']['_XWidth'] = tmp[0][0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOSA_Drain_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        tmp = self.get_param_KJH4('SRF_PMOSA','BND_Met1Layer_Drain')
        for i in range(0,len(tmp[0])):
            ## Calculate Sref XYcoord
                ## Calculate
                    ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_PMOSA','SRF_Drain_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
            target_coord = tmp1[0][i][0][0][0]['_XY_down_left']
                    ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_PMOSA_Drain_Vtc_M2')
            approaching_coord = tmp2[0][0]['_XY_up_left']
                    ## Sref coord
            tmp3 = self.get_param_KJH4('BND_PMOSA_Drain_Vtc_M2')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_PMOSA_Drain_Vtc_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Drain Hrz M2
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOSA_Drain_Hrz_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth : ViaYmin 기준
        self._DesignParameter['BND_PMOSA_Drain_Hrz_M2']['_YWidth'] = _DRCobj._VIAxMinWidth + + 2 * max([_DRCobj._Metal1MinEnclosureVia1, _DRCobj._MetalxMinEnclosureCO])

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_PMOSA', 'BND_Met1Layer_Drain')
        self._DesignParameter['BND_PMOSA_Drain_Hrz_M2']['_XWidth'] = abs(tmp[0][-1][0]['_XY_right'][0] - tmp[0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOSA_Drain_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        ## Calculate Sref XYcoord
            ## Calculate
                ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_PMOSA_Drain_Vtc_M2')
        target_coord = tmp1[0][0]['_XY_down_left']
                ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOSA_Drain_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOSA_Drain_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_PMOSA_Drain_Hrz_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  PMOS: Poly combine
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Poly combine : Vtc
        ## Pre-defined
        Ywidth_0 = 150

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOSA_Gate_Vtc_poly'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_PMOSA_Gate_Vtc_poly']['_YWidth'] = Ywidth_0

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_PMOSA', 'BND_POLayer')
        self._DesignParameter['BND_PMOSA_Gate_Vtc_poly']['_XWidth'] = tmp[0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOSA_Gate_Vtc_poly']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_PMOSA_Gate_Vtc_poly']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        tmp = self.get_param_KJH4('SRF_PMOSA', 'BND_POLayer')
        for i in range(0, len(tmp[0])):
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_PMOSA', 'BND_POLayer')
            target_coord = tmp1[0][i][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_PMOSA_Gate_Vtc_poly')
            approaching_coord = tmp2[0][0]['_XY_up_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_PMOSA_Gate_Vtc_poly')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_PMOSA_Gate_Vtc_poly']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Poly combine : Hrz
        ## Pre-defined
        Ywidth_1 = 70

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOSA_Gate_Hrz_poly'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_PMOSA_Gate_Hrz_poly']['_YWidth'] = Ywidth_1

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_PMOSA', 'BND_POLayer')
        self._DesignParameter['BND_PMOSA_Gate_Hrz_poly']['_XWidth'] = abs( tmp1[0][0][0]['_XY_left'][0] - tmp1[0][-1][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOSA_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
            ## initialized Sref coordinate
        self._DesignParameter['BND_PMOSA_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
                ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_PMOSA_Gate_Vtc_poly')
        target_coord = tmp1[0][0]['_XY_down_left']
                ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOSA_Gate_Hrz_poly')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOSA_Gate_Hrz_poly')
        Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_PMOSA_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  PMOS: Gate _ViaM0M1
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : Metal1

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOSA_Gate_Hrz_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('BND_PMOSA_Gate_Hrz_poly')
        self._DesignParameter['BND_PMOSA_Gate_Hrz_M1']['_YWidth'] = tmp[0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('BND_PMOSA_Gate_Hrz_poly')
        self._DesignParameter['BND_PMOSA_Gate_Hrz_M1']['_XWidth'] = tmp[0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOSA_Gate_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
            ## initialized Sref coordinate
        self._DesignParameter['BND_PMOSA_Gate_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
                ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_PMOSA_Gate_Hrz_poly')
        target_coord = tmp1[0][0]['_XY_down_left']
                ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOSA_Gate_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOSA_Gate_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_PMOSA_Gate_Hrz_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : _ViaM0M1
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 0
        _Caculation_Parameters['_Layer2'] = 1
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

            ## Sref ViaX declaration
        self._DesignParameter['SRF_PMOSA_Gate_ViaM0M1'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None, _Name='{}:SRF_PMOSA_Gate_ViaM0M1'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_PMOSA_Gate_ViaM0M1']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_PMOSA_Gate_ViaM0M1']['_Angle'] = 0

            ## Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH4('BND_PMOSA_Gate_Hrz_M1')
        tmp2 = self.get_param_KJH4('BND_PMOSA_Gate_Hrz_poly')
        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

        ## Define _COX and _COY
        ## Define _COX
        if _COX < 2:
            if _PMOSA_PMOSNumberofGate == 1:
                _Caculation_Parameters['_COX'] = 1
                _Caculation_Parameters['_COY'] = 2
                flag = 2
            else:
                _Caculation_Parameters['_COX'] = 2
                _Caculation_Parameters['_COY'] = _COY
                flag = 1
        else:
            _Caculation_Parameters['_COX'] = _COX
            _Caculation_Parameters['_COY'] = _COY
            flag = 0
            ## Define _COY

        if flag == 0:
            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin,
            self._DesignParameter['SRF_PMOSA_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameterYmin(
                **_Caculation_Parameters)

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['SRF_PMOSA_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_PMOSA_Gate_Hrz_M1')
            target_coord = tmp1[0][0]['_XY_cent']
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_PMOSA_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_PMOSA_Gate_ViaM0M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define
            self._DesignParameter['SRF_PMOSA_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY

        if flag == 1:
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : _ViaM0M1 : Ymin
            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin,
            self._DesignParameter['SRF_PMOSA_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameterYmin(
                **_Caculation_Parameters)

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['SRF_PMOSA_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_PMOSA_Gate_Hrz_M1')
            target_coord = tmp1[0][0]['_XY_cent']
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_PMOSA_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_PMOSA_Gate_ViaM0M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define
            self._DesignParameter['SRF_PMOSA_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : _ViaM0M1 : Poly Exten
            ## Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH4('SRF_PMOSA_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            self._DesignParameter['BND_PMOSA_Gate_Hrz_poly']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_PMOSA_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['BND_PMOSA_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord: _XY_type1
            ## X
            tmp1_1 = self.get_param_KJH4('SRF_PMOSA_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            target_coordx = tmp1_1[0][0][0][0]['_XY_left'][0]
            ## Y
            tmp1_2 = self.get_param_KJH4('BND_PMOSA_Gate_Vtc_poly')
            target_coordy = tmp1_2[0][0]['_XY_down'][1]

            target_coord = [target_coordx, target_coordy]
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_PMOSA_Gate_Hrz_poly')
            approaching_coord = tmp2[0][0]['_XY_down_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_PMOSA_Gate_Hrz_poly')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_PMOSA_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : _ViaM0M1 : M1 Exten
            ## Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH4('BND_PMOSA_Gate_Hrz_poly')
            self._DesignParameter['BND_PMOSA_Gate_Hrz_M1']['_XWidth'] = tmp1[0][0]['_Xwidth']

            ## Define Boundary_element _XYCoordinates
            tmp1 = self.get_param_KJH4('BND_PMOSA_Gate_Hrz_poly')
            self._DesignParameter['BND_PMOSA_Gate_Hrz_M1']['_XYCoordinates'] = [tmp1[0][0]['_XY_down_left']]

        if flag == 2:
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : _ViaM0M1 : Xmin
            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin,
            self._DesignParameter['SRF_PMOSA_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameter( **_Caculation_Parameters)

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['SRF_PMOSA_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_PMOSA_Gate_Hrz_M1')
            target_coord = tmp1[0][0]['_XY_down']
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_PMOSA_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_PMOSA_Gate_ViaM0M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define
            self._DesignParameter['SRF_PMOSA_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : _ViaM0M1 : Poly Exten
            ## Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH4('SRF_PMOSA_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_POLayer')
            self._DesignParameter['BND_PMOSA_Gate_Hrz_poly']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']

            ## Define Boundary_element _YWidth
            tmp1 = self.get_param_KJH4('SRF_PMOSA_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_POLayer')
            self._DesignParameter['BND_PMOSA_Gate_Hrz_poly']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_PMOSA_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['BND_PMOSA_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1_1 = self.get_param_KJH4('SRF_PMOSA_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_POLayer')
            target_coord = tmp1_1[0][0][0][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_PMOSA_Gate_Hrz_poly')
            approaching_coord = tmp2[0][0]['_XY_down_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_PMOSA_Gate_Hrz_poly')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_PMOSA_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : _ViaM0M1 : M1 Exten
            ## Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH4('SRF_PMOSA_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            self._DesignParameter['BND_PMOSA_Gate_Hrz_M1']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']

            ## Define Boundary_element _YWidth
            tmp1 = self.get_param_KJH4('SRF_PMOSA_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            self._DesignParameter['BND_PMOSA_Gate_Hrz_M1']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

            ## Define Boundary_element _XYCoordinates
            tmp1 = self.get_param_KJH4('SRF_PMOSA_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            self._DesignParameter['BND_PMOSA_Gate_Hrz_M1']['_XYCoordinates'] = [tmp1[0][0][0][0]['_XY_down_left']]














        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOSB
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  PMOSB: Sref Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_PMOS_power_v2._PMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A04_PmosWithDummy_KJH3._PmosWithDummy_KJH3._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_PMOSPOWER_PbodyContact_1_Length']  = _PMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_PMOSNumberofGate']     = _PMOSB_PMOSNumberofGate
        _Caculation_Parameters['_PMOSChannelWidth']     = _PMOSB_PMOSChannelWidth
        _Caculation_Parameters['_PMOSChannellength']    = _PMOSB_PMOSChannellength
        _Caculation_Parameters['_GateSpacing']          = _PMOSB_GateSpacing
        _Caculation_Parameters['_SDWidth']              = _PMOSB_SDWidth
        _Caculation_Parameters['_XVT']                  = _PMOSB_XVT
        _Caculation_Parameters['_PCCrit']               = _PMOSB_PCCrit
        _Caculation_Parameters['_Source_Via_TF']        = _PMOSB_Source_Via_TF
        _Caculation_Parameters['_Drain_Via_TF']         = _PMOSB_Drain_Via_TF
        _Caculation_Parameters['_PMOSDummy']            = _PMOSB_PMOSDummy
        _Caculation_Parameters['_PMOSDummy_length']     = _PMOSB_PMOSDummy_length
        _Caculation_Parameters['_PMOSDummy_placement']  = _PMOSB_PMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_PMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_PMOS_power_v2._PMOS_POWER( _DesignParameter=None, _Name='{}:PMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_PMOSB'] = self._SrefElementDeclaration(_DesignObj=A04_PmosWithDummy_KJH3._PmosWithDummy_KJH3(_DesignParameter=None, _Name='{}:SRF_PMOSB'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_PMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_PMOSB']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_PMOS_POWER'
        self._DesignParameter['SRF_PMOSB']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_PMOS_POWER'
        self._DesignParameter['SRF_PMOSB']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_PMOS_POWER'
        self._DesignParameter['SRF_PMOSB']['_XYCoordinates'] = [[0, 0]]

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


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Drain Combine DNward
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOSA: Drain Vtc M2
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOSB_Drain_Vtc_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth : ViaYmin 기준
        tmp1 = self.get_param_KJH4('SRF_PMOSB','BND_Met1Layer_Drain')
        tmp2 = self.get_param_KJH4('SRF_PMOSB','SRF_Drain_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
        self._DesignParameter['BND_PMOSB_Drain_Vtc_M2']['_YWidth'] = abs( tmp2[0][0][0][0][0]['_XY_down'][1] - tmp1[0][0][0]['_XY_down'][1] )

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_PMOSB','SRF_Drain_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
        self._DesignParameter['BND_PMOSB_Drain_Vtc_M2']['_XWidth'] = tmp[0][0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOSB_Drain_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        tmp = self.get_param_KJH4('SRF_PMOSB','BND_Met1Layer_Drain')
        for i in range(0,len(tmp[0])):
            ## Calculate Sref XYcoord
                ## Calculate
                    ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_PMOSB','SRF_Drain_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
            target_coord = tmp1[0][i][0][0][0]['_XY_down_left']
                    ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_PMOSB_Drain_Vtc_M2')
            approaching_coord = tmp2[0][0]['_XY_up_left']
                    ## Sref coord
            tmp3 = self.get_param_KJH4('BND_PMOSB_Drain_Vtc_M2')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_PMOSB_Drain_Vtc_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Drain Hrz M2
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOSB_Drain_Hrz_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth : ViaYmin 기준
        self._DesignParameter['BND_PMOSB_Drain_Hrz_M2']['_YWidth'] = _DRCobj._VIAxMinWidth + + 2 * max([_DRCobj._Metal1MinEnclosureVia1, _DRCobj._MetalxMinEnclosureCO])

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_PMOSB', 'BND_Met1Layer_Drain')
        self._DesignParameter['BND_PMOSB_Drain_Hrz_M2']['_XWidth'] = abs(tmp[0][-1][0]['_XY_right'][0] - tmp[0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOSB_Drain_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        ## Calculate Sref XYcoord
            ## Calculate
                ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_PMOSB_Drain_Vtc_M2')
        target_coord = tmp1[0][0]['_XY_down_left']
                ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOSB_Drain_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOSB_Drain_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_PMOSB_Drain_Hrz_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  PMOS: Poly combine
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Poly combine : Vtc
        ## Pre-defined
        Ywidth_0 = 150

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOSB_Gate_Vtc_poly'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_PMOSB_Gate_Vtc_poly']['_YWidth'] = Ywidth_0

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_PMOSB', 'BND_POLayer')
        self._DesignParameter['BND_PMOSB_Gate_Vtc_poly']['_XWidth'] = tmp[0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOSB_Gate_Vtc_poly']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_PMOSB_Gate_Vtc_poly']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        tmp = self.get_param_KJH4('SRF_PMOSB', 'BND_POLayer')
        for i in range(0, len(tmp[0])):
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_PMOSB', 'BND_POLayer')
            target_coord = tmp1[0][i][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_PMOSB_Gate_Vtc_poly')
            approaching_coord = tmp2[0][0]['_XY_up_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_PMOSB_Gate_Vtc_poly')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_PMOSB_Gate_Vtc_poly']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Poly combine : Hrz
        ## Pre-defined
        Ywidth_1 = 70

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOSB_Gate_Hrz_poly'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_PMOSB_Gate_Hrz_poly']['_YWidth'] = Ywidth_1

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_PMOSB', 'BND_POLayer')
        self._DesignParameter['BND_PMOSB_Gate_Hrz_poly']['_XWidth'] = abs( tmp1[0][0][0]['_XY_left'][0] - tmp1[0][-1][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOSB_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
            ## initialized Sref coordinate
        self._DesignParameter['BND_PMOSB_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
                ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_PMOSB_Gate_Vtc_poly')
        target_coord = tmp1[0][0]['_XY_down_left']
                ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOSB_Gate_Hrz_poly')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOSB_Gate_Hrz_poly')
        Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_PMOSB_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  PMOS: Gate _ViaM0M1
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : Metal1

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOSB_Gate_Hrz_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('BND_PMOSB_Gate_Hrz_poly')
        self._DesignParameter['BND_PMOSB_Gate_Hrz_M1']['_YWidth'] = tmp[0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('BND_PMOSB_Gate_Hrz_poly')
        self._DesignParameter['BND_PMOSB_Gate_Hrz_M1']['_XWidth'] = tmp[0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOSB_Gate_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
            ## initialized Sref coordinate
        self._DesignParameter['BND_PMOSB_Gate_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
                ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_PMOSB_Gate_Hrz_poly')
        target_coord = tmp1[0][0]['_XY_down_left']
                ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOSB_Gate_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOSB_Gate_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_PMOSB_Gate_Hrz_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : _ViaM0M1
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 0
        _Caculation_Parameters['_Layer2'] = 1
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

            ## Sref ViaX declaration
        self._DesignParameter['SRF_PMOSB_Gate_ViaM0M1'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None, _Name='{}:SRF_PMOSB_Gate_ViaM0M1'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_PMOSB_Gate_ViaM0M1']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_PMOSB_Gate_ViaM0M1']['_Angle'] = 0

            ## Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH4('BND_PMOSB_Gate_Hrz_M1')
        tmp2 = self.get_param_KJH4('BND_PMOSB_Gate_Hrz_poly')
        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

        ## Define _COX and _COY
        ## Define _COX
        if _COX < 2:
            if _PMOSB_PMOSNumberofGate == 1:
                _Caculation_Parameters['_COX'] = 1
                _Caculation_Parameters['_COY'] = 2
                flag = 2
            else:
                _Caculation_Parameters['_COX'] = 2
                _Caculation_Parameters['_COY'] = _COY
                flag = 1
        else:
            _Caculation_Parameters['_COX'] = _COX
            _Caculation_Parameters['_COY'] = _COY
            flag = 0
            ## Define _COY

        if flag == 0:
            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin,
            self._DesignParameter['SRF_PMOSB_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameterYmin(
                **_Caculation_Parameters)

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['SRF_PMOSB_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_PMOSB_Gate_Hrz_M1')
            target_coord = tmp1[0][0]['_XY_cent']
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_PMOSB_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_PMOSB_Gate_ViaM0M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define
            self._DesignParameter['SRF_PMOSB_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY

        if flag == 1:
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : _ViaM0M1 : Ymin
            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin,
            self._DesignParameter['SRF_PMOSB_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameterYmin(
                **_Caculation_Parameters)

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['SRF_PMOSB_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_PMOSB_Gate_Hrz_M1')
            target_coord = tmp1[0][0]['_XY_cent']
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_PMOSB_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_PMOSB_Gate_ViaM0M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define
            self._DesignParameter['SRF_PMOSB_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : _ViaM0M1 : Poly Exten
            ## Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH4('SRF_PMOSB_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            self._DesignParameter['BND_PMOSB_Gate_Hrz_poly']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_PMOSB_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['BND_PMOSB_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord: _XY_type1
            ## X
            tmp1_1 = self.get_param_KJH4('SRF_PMOSB_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            target_coordx = tmp1_1[0][0][0][0]['_XY_left'][0]
            ## Y
            tmp1_2 = self.get_param_KJH4('BND_PMOSB_Gate_Vtc_poly')
            target_coordy = tmp1_2[0][0]['_XY_down'][1]

            target_coord = [target_coordx, target_coordy]
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_PMOSB_Gate_Hrz_poly')
            approaching_coord = tmp2[0][0]['_XY_down_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_PMOSB_Gate_Hrz_poly')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_PMOSB_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : _ViaM0M1 : M1 Exten
            ## Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH4('BND_PMOSB_Gate_Hrz_poly')
            self._DesignParameter['BND_PMOSB_Gate_Hrz_M1']['_XWidth'] = tmp1[0][0]['_Xwidth']

            ## Define Boundary_element _XYCoordinates
            tmp1 = self.get_param_KJH4('BND_PMOSB_Gate_Hrz_poly')
            self._DesignParameter['BND_PMOSB_Gate_Hrz_M1']['_XYCoordinates'] = [tmp1[0][0]['_XY_down_left']]

        if flag == 2:
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : _ViaM0M1 : Xmin
            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin,
            self._DesignParameter['SRF_PMOSB_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameter( **_Caculation_Parameters)

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['SRF_PMOSB_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_PMOSB_Gate_Hrz_M1')
            target_coord = tmp1[0][0]['_XY_down']
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_PMOSB_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_PMOSB_Gate_ViaM0M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define
            self._DesignParameter['SRF_PMOSB_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : _ViaM0M1 : Poly Exten
            ## Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH4('SRF_PMOSB_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_POLayer')
            self._DesignParameter['BND_PMOSB_Gate_Hrz_poly']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']

            ## Define Boundary_element _YWidth
            tmp1 = self.get_param_KJH4('SRF_PMOSB_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_POLayer')
            self._DesignParameter['BND_PMOSB_Gate_Hrz_poly']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_PMOSB_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['BND_PMOSB_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1_1 = self.get_param_KJH4('SRF_PMOSB_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_POLayer')
            target_coord = tmp1_1[0][0][0][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_PMOSB_Gate_Hrz_poly')
            approaching_coord = tmp2[0][0]['_XY_down_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_PMOSB_Gate_Hrz_poly')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_PMOSB_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : _ViaM0M1 : M1 Exten
            ## Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH4('SRF_PMOSB_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            self._DesignParameter['BND_PMOSB_Gate_Hrz_M1']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']

            ## Define Boundary_element _YWidth
            tmp1 = self.get_param_KJH4('SRF_PMOSB_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            self._DesignParameter['BND_PMOSB_Gate_Hrz_M1']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

            ## Define Boundary_element _XYCoordinates
            tmp1 = self.get_param_KJH4('SRF_PMOSB_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            self._DesignParameter['BND_PMOSB_Gate_Hrz_M1']['_XYCoordinates'] = [tmp1[0][0][0][0]['_XY_down_left']]




        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  PMOSA Drain PMOSB Drain connection M2
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOSADrain_PMOSBDrain_Hrz_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('BND_PMOSB_Drain_Hrz_M2')
        self._DesignParameter['BND_PMOSADrain_PMOSBDrain_Hrz_M2']['_YWidth'] = tmp[0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('BND_PMOSB_Drain_Hrz_M2')
        tmp2 = self.get_param_KJH4('BND_PMOSA_Drain_Hrz_M2')
        self._DesignParameter['BND_PMOSADrain_PMOSBDrain_Hrz_M2']['_XWidth'] = abs( tmp1[0][0]['_XY_right'][0] - tmp2[0][0]['_XY_left'][0]  )

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOSADrain_PMOSBDrain_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
            ## initialized Sref coordinate
        self._DesignParameter['BND_PMOSADrain_PMOSBDrain_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
                ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_PMOSB_Drain_Hrz_M2')
        target_coord = tmp1[0][0]['_XY_down_right']
                ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOSADrain_PMOSBDrain_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_down_right']
                ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOSADrain_PMOSBDrain_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_PMOSADrain_PMOSBDrain_Hrz_M2']['_XYCoordinates'] = tmpXY


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
    libname = 'Proj_ADC_D03_SARLogic_Nand_KJH'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'D03_01_Pullup_v0_95'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

        # NMOSA
        _PMOSA_PMOSNumberofGate=3,  # number
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
        _PMOSB_PMOSNumberofGate=3,  # number
        _PMOSB_PMOSChannelWidth=200,  # number
        _PMOSB_PMOSChannellength=30,  # number
        _PMOSB_GateSpacing=None,  # None/number
        _PMOSB_SDWidth=None,  # None/number
        _PMOSB_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _PMOSB_PCCrit=True,  # None/True

            # Source_node_ViaM1M2
        _PMOSB_Source_Via_TF=False,  # True/False

            # Drain_node_ViaM1M2
        _PMOSB_Drain_Via_TF=True,  # True/False

            # POLY dummy setting
        _PMOSB_PMOSDummy=True,  # TF
            # if _PMOSDummy == True
        _PMOSB_PMOSDummy_length=None,  # None/Value
        _PMOSB_PMOSDummy_placement='Up',  # None/'Up'/'Dn'/

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
