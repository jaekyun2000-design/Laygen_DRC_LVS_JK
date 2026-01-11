
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
class _Pmos(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(

        # NMOS
        _PMOS_PMOSNumberofGate=5,  # number
        _PMOS_PMOSChannelWidth=300,  # number
        _PMOS_PMOSChannellength=30,  # number
        _PMOS_GateSpacing=None,  # None/number
        _PMOS_SDWidth=None,  # None/number
        _PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _PMOS_PCCrit=True,  # None/True

            # Source_node_ViaM1M2
        _PMOS_Source_Via_TF=False,  # True/False

            # Drain_node_ViaM1M2
        _PMOS_Drain_Via_TF=True,  # True/False

            # POLY dummy setting
        _PMOS_PMOSDummy=True,  # TF
            # if _PMOSDummy == True
        _PMOS_PMOSDummy_length=None,  # None/Value
        _PMOS_PMOSDummy_placement=None,  # None/'Up'/'Dn'/


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

                                  # PMOS
                                  _PMOS_PMOSNumberofGate=5,  # number
                                  _PMOS_PMOSChannelWidth=300,  # number
                                  _PMOS_PMOSChannellength=30,  # number
                                  _PMOS_GateSpacing=None,  # None/number
                                  _PMOS_SDWidth=None,  # None/number
                                  _PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _PMOS_PCCrit=True,  # None/True

                                    # Source_node_ViaM1M2
                                  _PMOS_Source_Via_TF=False,  # True/False

                                    # Drain_node_ViaM1M2
                                  _PMOS_Drain_Via_TF=True,  # True/False

                                    # POLY dummy setting
                                  _PMOS_PMOSDummy=True,  # TF
                                    # if _PMOSDummy == True
                                  _PMOS_PMOSDummy_length=None,  # None/Value
                                  _PMOS_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

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
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_PMOS_power_v2._PMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A04_PmosWithDummy_KJH3._PmosWithDummy_KJH3._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_PMOSPOWER_PbodyContact_1_Length']  = _PMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_PMOSNumberofGate']     = _PMOS_PMOSNumberofGate
        _Caculation_Parameters['_PMOSChannelWidth']     = _PMOS_PMOSChannelWidth
        _Caculation_Parameters['_PMOSChannellength']    = _PMOS_PMOSChannellength
        _Caculation_Parameters['_GateSpacing']          = _PMOS_GateSpacing
        _Caculation_Parameters['_SDWidth']              = _PMOS_SDWidth
        _Caculation_Parameters['_XVT']                  = _PMOS_XVT
        _Caculation_Parameters['_PCCrit']               = _PMOS_PCCrit
        _Caculation_Parameters['_Source_Via_TF']        = _PMOS_Source_Via_TF
        _Caculation_Parameters['_Drain_Via_TF']         = _PMOS_Drain_Via_TF
        _Caculation_Parameters['_PMOSDummy']            = _PMOS_PMOSDummy
        _Caculation_Parameters['_PMOSDummy_length']     = _PMOS_PMOSDummy_length
        _Caculation_Parameters['_PMOSDummy_placement']  = _PMOS_PMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_PMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_PMOS_power_v2._PMOS_POWER( _DesignParameter=None, _Name='{}:PMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_PMOS'] = self._SrefElementDeclaration(_DesignObj=A04_PmosWithDummy_KJH3._PmosWithDummy_KJH3(_DesignParameter=None, _Name='{}:SRF_PMOS'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_PMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_PMOS']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_PMOS_POWER'
        self._DesignParameter['SRF_PMOS']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_PMOS_POWER'
        self._DesignParameter['SRF_PMOS']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_PMOS_POWER'
        self._DesignParameter['SRF_PMOS']['_XYCoordinates'] = [[0, 0]]

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Drain Combine Upward
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Drain Vtc M2
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOS_Drain_Vtc_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth : ViaYmin 기준
        tmp1 = self.get_param_KJH4('SRF_PMOS','SRF_Source_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
        tmp2 = self.get_param_KJH4('SRF_PMOS','SRF_Drain_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
        self._DesignParameter['BND_PMOS_Drain_Vtc_M2']['_YWidth'] = _DRCobj._MetalxMinSpace41 + abs( tmp1[0][0][0][0][0]['_XY_down'][1] - tmp2[0][0][0][0][0]['_XY_down'][1] )

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_PMOS','SRF_Drain_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
        self._DesignParameter['BND_PMOS_Drain_Vtc_M2']['_XWidth'] = tmp[0][0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOS_Drain_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        tmp = self.get_param_KJH4('SRF_PMOS','BND_Met1Layer_Drain')
        for i in range(0,len(tmp[0])):
            ## Calculate Sref XYcoord
                ## Calculate
                    ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_PMOS','SRF_Drain_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
            target_coord = tmp1[0][i][0][0][0]['_XY_down_left']
                    ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_PMOS_Drain_Vtc_M2')
            approaching_coord = tmp2[0][0]['_XY_up_left']
                    ## Sref coord
            tmp3 = self.get_param_KJH4('BND_PMOS_Drain_Vtc_M2')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_PMOS_Drain_Vtc_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Drain Hrz M2
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOS_Drain_Hrz_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth : ViaYmin 기준
        self._DesignParameter['BND_PMOS_Drain_Hrz_M2']['_YWidth'] = _DRCobj._VIAxMinWidth + + 2 * max([_DRCobj._Metal1MinEnclosureVia1, _DRCobj._MetalxMinEnclosureCO])

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_PMOS', 'BND_Met1Layer_Drain')
        self._DesignParameter['BND_PMOS_Drain_Hrz_M2']['_XWidth'] = abs(tmp[0][-1][0]['_XY_right'][0] - tmp[0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOS_Drain_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        ## Calculate Sref XYcoord
            ## Calculate
                ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_PMOS_Drain_Vtc_M2')
        target_coord = tmp1[0][0]['_XY_down_left']
                ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOS_Drain_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOS_Drain_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_PMOS_Drain_Hrz_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Source Combine Downward
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Source Vtc M2
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOS_Source_Vtc_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth : ViaYmin 기준
        tmp1 = self.get_param_KJH4('SRF_PMOS', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        tmp2 = self.get_param_KJH4('SRF_PMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        self._DesignParameter['BND_PMOS_Source_Vtc_M2']['_YWidth'] = _DRCobj._MetalxMinSpace41 + abs( tmp1[0][0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_PMOS', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        self._DesignParameter['BND_PMOS_Source_Vtc_M2']['_XWidth'] = tmp[0][0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOS_Source_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        tmp = self.get_param_KJH4('SRF_PMOS', 'BND_Met1Layer_Source')
        for i in range(0, len(tmp[0])):
            ## Calculate Sref XYcoord
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_PMOS', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
            target_coord = tmp1[0][i][0][0][0]['_XY_up_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_PMOS_Source_Vtc_M2')
            approaching_coord = tmp2[0][0]['_XY_down_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_PMOS_Source_Vtc_M2')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_PMOS_Source_Vtc_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Source Hrz M2
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOS_Source_Hrz_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth : ViaYmin 기준
        self._DesignParameter['BND_PMOS_Source_Hrz_M2']['_YWidth'] = _DRCobj._VIAxMinWidth + + 2 * max( [_DRCobj._Metal1MinEnclosureVia1, _DRCobj._MetalxMinEnclosureCO])

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_PMOS', 'BND_Met1Layer_Source')
        self._DesignParameter['BND_PMOS_Source_Hrz_M2']['_XWidth'] = abs( tmp[0][-1][0]['_XY_right'][0] - tmp[0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOS_Source_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        ## Calculate Sref XYcoord
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_PMOS_Source_Vtc_M2')
        target_coord = tmp1[0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOS_Source_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOS_Source_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_PMOS_Source_Hrz_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  PMOS: Poly combine
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Poly combine : Vtc
        ## Pre-defined
        Ywidth_0 = 150

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOS_Gate_Vtc_poly'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_PMOS_Gate_Vtc_poly']['_YWidth'] = Ywidth_0

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_PMOS', 'BND_POLayer')
        self._DesignParameter['BND_PMOS_Gate_Vtc_poly']['_XWidth'] = tmp[0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOS_Gate_Vtc_poly']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_PMOS_Gate_Vtc_poly']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        tmp = self.get_param_KJH4('SRF_PMOS', 'BND_POLayer')
        for i in range(0, len(tmp[0])):
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_PMOS', 'BND_POLayer')
            target_coord = tmp1[0][i][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_PMOS_Gate_Vtc_poly')
            approaching_coord = tmp2[0][0]['_XY_up_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_PMOS_Gate_Vtc_poly')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_PMOS_Gate_Vtc_poly']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Poly combine : Hrz
        ## Pre-defined
        Ywidth_1 = 50

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOS_Gate_Hrz_poly'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_YWidth'] = Ywidth_1

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_PMOS', 'BND_POLayer')
        self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_XWidth'] = abs( tmp1[0][0][0]['_XY_left'][0] - tmp1[0][-1][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
            ## initialized Sref coordinate
        self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
                ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_PMOS_Gate_Vtc_poly')
        target_coord = tmp1[0][0]['_XY_down_left']
                ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_poly')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_poly')
        Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  PMOS: Gate _ViaM0M1
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : Metal1

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOS_Gate_Hrz_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('BND_PMOS_Gate_Hrz_poly')
        self._DesignParameter['BND_PMOS_Gate_Hrz_M1']['_YWidth'] = tmp[0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('BND_PMOS_Gate_Hrz_poly')
        self._DesignParameter['BND_PMOS_Gate_Hrz_M1']['_XWidth'] = tmp[0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOS_Gate_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
            ## initialized Sref coordinate
        self._DesignParameter['BND_PMOS_Gate_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
                ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_poly')
        target_coord = tmp1[0][0]['_XY_down_left']
                ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_PMOS_Gate_Hrz_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : _ViaM0M1
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 0
        _Caculation_Parameters['_Layer2'] = 1
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

            ## Sref ViaX declaration
        self._DesignParameter['SRF_PMOS_Gate_ViaM0M1'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None, _Name='{}:SRF_PMOS_Gate_ViaM0M1'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_PMOS_Gate_ViaM0M1']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_PMOS_Gate_ViaM0M1']['_Angle'] = 0

            ## Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_M1')
        tmp2 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_poly')
        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

        ## Define _COX and _COY
        ## Define _COX
        if _COX < 2:
            if _PMOS_PMOSNumberofGate == 1:
                _Caculation_Parameters['_COX'] = 2
                _Caculation_Parameters['_COY'] = 1
                flag = 1
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
            self._DesignParameter['SRF_PMOS_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameterYmin( **_Caculation_Parameters)

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['SRF_PMOS_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_M1')
            target_coord = tmp1[0][0]['_XY_cent']
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_PMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_PMOS_Gate_ViaM0M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define
            self._DesignParameter['SRF_PMOS_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY

        if flag == 1:
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : _ViaM0M1 : Ymin
            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin,
            self._DesignParameter['SRF_PMOS_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameterYmin( **_Caculation_Parameters)

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['SRF_PMOS_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_M1')
            target_coord = tmp1[0][0]['_XY_cent']
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_PMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_PMOS_Gate_ViaM0M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define
            self._DesignParameter['SRF_PMOS_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : _ViaM0M1 : Poly Exten
            ## Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH4('SRF_PMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord: _XY_type1
            ## X
            tmp1_1 = self.get_param_KJH4('SRF_PMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            target_coordx = tmp1_1[0][0][0][0]['_XY_left'][0]
            ## Y
            tmp1_2 = self.get_param_KJH4('BND_PMOS_Gate_Vtc_poly')
            target_coordy = tmp1_2[0][0]['_XY_down'][1]

            target_coord = [target_coordx, target_coordy]
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_poly')
            approaching_coord = tmp2[0][0]['_XY_down_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_poly')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : _ViaM0M1 : M1 Exten
            ## Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_poly')
            self._DesignParameter['BND_PMOS_Gate_Hrz_M1']['_XWidth'] = tmp1[0][0]['_Xwidth']

            ## Define Boundary_element _XYCoordinates
            tmp1 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_poly')
            self._DesignParameter['BND_PMOS_Gate_Hrz_M1']['_XYCoordinates'] = [tmp1[0][0]['_XY_down_left']]

        if flag == 2:
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : _ViaM0M1 : Xmin
            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin,
            self._DesignParameter['SRF_PMOS_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameterXmin( **_Caculation_Parameters)

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['SRF_PMOS_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_M1')
            target_coord = tmp1[0][0]['_XY_down']
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_PMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_PMOS_Gate_ViaM0M1')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define
            self._DesignParameter['SRF_PMOS_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : _ViaM0M1 : Poly Exten
            ## Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH4('SRF_PMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_POLayer')
            self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']

            ## Define Boundary_element _YWidth
            tmp1 = self.get_param_KJH4('SRF_PMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_POLayer')
            self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1_1 = self.get_param_KJH4('SRF_PMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_POLayer')
            target_coord = tmp1_1[0][0][0][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_poly')
            approaching_coord = tmp2[0][0]['_XY_down_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_poly')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : _ViaM0M1 : M1 Exten
            ## Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH4('SRF_PMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            self._DesignParameter['BND_PMOS_Gate_Hrz_M1']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']

            ## Define Boundary_element _YWidth
            tmp1 = self.get_param_KJH4('SRF_PMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            self._DesignParameter['BND_PMOS_Gate_Hrz_M1']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

            ## Define Boundary_element _XYCoordinates
            tmp1 = self.get_param_KJH4('SRF_PMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            self._DesignParameter['BND_PMOS_Gate_Hrz_M1']['_XYCoordinates'] = [tmp1[0][0][0][0]['_XY_down_left']]


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
    libname = 'Proj_ADC_D01_SARLogic_XmissionGate_KJH'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'D01_01_PMOS_v0_98'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

        # PMOS
        _PMOS_PMOSNumberofGate=1,  # number
        _PMOS_PMOSChannelWidth=700,  # number
        _PMOS_PMOSChannellength=30,  # number
        _PMOS_GateSpacing=None,  # None/number
        _PMOS_SDWidth=None,  # None/number
        _PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _PMOS_PCCrit=True,  # None/True

            # Source_node_ViaM1M2
        _PMOS_Source_Via_TF=True,  # True/False

            # Drain_node_ViaM1M2
        _PMOS_Drain_Via_TF=True,  # True/False

            # POLY dummy setting
        _PMOS_PMOSDummy=True,  # TF
            # if _PMOSDummy == True
        _PMOS_PMOSDummy_length=None,  # None/Value
        _PMOS_PMOSDummy_placement=None,  # None/'Up'/'Dn'/


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
    LayoutObj = _Pmos(_DesignParameter=None, _Name=cellname)
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
