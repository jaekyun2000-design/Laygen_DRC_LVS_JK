## Import Basic Modules
    ## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_ADC.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC
#from KJH91_Projects.Project_ADC.Library_and_Engine import DRCv2

    ## Library
import copy
import math
import numpy as np
import time

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A05_NbodyContact_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A06_PbodyContact_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.C04_Tiecell import C04_00_PmosRoute
from KJH91_Projects.Project_ADC.Layoutgen_code.C04_Tiecell import C04_01_NmosRoute


############################################################################################################################################################ Class_HEADER
class _TieCell4(StickDiagram_KJH1._StickDiagram_KJH):

    ##########################################################################################################################
    # Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(
        # TieN
        _TieN_NMOSNumberofGate=4,  # number
        _TieN_NMOSChannelWidth=250,  # number
        _TieN_NMOSChannellength=30,  # number
        _TieN_GateSpacing=100,  # None/number
        _TieN_SDWidth=None,  # None/number
        _TieN_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _TieN_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _TieN_Source_Via_TF=False,  # True/False

        # Drain_node_ViaM1M2
        _TieN_Drain_Via_TF=False,  # True/False

        # POLY dummy setting
        _TieN_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _TieN_NMOSDummy_length=None,  # None/Value
        _TieN_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr4
        _TieP_PMOSNumberofGate=4,  # number
        _TieP_PMOSChannelWidth=500,  # number
        _TieP_PMOSChannellength=30,  # number
        _TieP_GateSpacing=100,  # None/number
        _TieP_SDWidth=None,  # None/number
        _TieP_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _TieP_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _TieP_Source_Via_TF=False,  # True/False

        # Drain_node_ViaM1M2
        _TieP_Drain_Via_TF=False,  # True/False

        # POLY dummy setting
        _TieP_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _TieP_PMOSDummy_length=None,  # None/Value
        _TieP_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Body Contact
        _NBodyCOX = 10,
        _NBodyCOY = 2,
        _PBodyCOX = 10,
        _PBodyCOY = 2,
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
                                  # TieN
                                  _TieN_NMOSNumberofGate=4,  # number
                                  _TieN_NMOSChannelWidth=250,  # number
                                  _TieN_NMOSChannellength=30,  # number
                                  _TieN_GateSpacing=100,  # None/number
                                  _TieN_SDWidth=None,  # None/number
                                  _TieN_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _TieN_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _TieN_Source_Via_TF=True,  # True/False

                                  # Drain_node_ViaM1M2
                                  _TieN_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _TieN_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _TieN_NMOSDummy_length=None,  # None/Value
                                  _TieN_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Tr4
                                  _TieP_PMOSNumberofGate=4,  # number
                                  _TieP_PMOSChannelWidth=500,  # number
                                  _TieP_PMOSChannellength=30,  # number
                                  _TieP_GateSpacing=100,  # None/number
                                  _TieP_SDWidth=None,  # None/number
                                  _TieP_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _TieP_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _TieP_Source_Via_TF=True,  # True/False

                                  # Drain_node_ViaM1M2
                                  _TieP_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _TieP_PMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _TieP_PMOSDummy_length=None,  # None/Value
                                  _TieP_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                    # Body Contact
                                    _NBodyCOX = 10,
                                    _NBodyCOY = 2,
                                    _PBodyCOX = 10,
                                    _PBodyCOY = 2
                                  ):

        ## Class_HEADER: Pre Defined Parameter Before Calculation
            ## Load DRC library
        _DRCObj = DRC.DRC()
            ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']
        ## CALCULATION START
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')


        # Pre-defined Design Value
        SpacingODBtwPmosAndNBody = 180
        SpacingODBtwNmosAndPBody = 180
        SpacingHrzPolyBtwNmosRouteAndPmosRoute = 180


        ## C04_01_NMOSRoute(SREF) Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C04_01_NmosRoute._NmosRoute._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_TieN_NMOSNumberofGate'] = _TieN_NMOSNumberofGate
        _Caculation_Parameters['_TieN_NMOSChannelWidth'] = _TieN_NMOSChannelWidth
        _Caculation_Parameters['_TieN_NMOSChannellength'] = _TieN_NMOSChannellength
        _Caculation_Parameters['_TieN_GateSpacing'] = _TieN_GateSpacing
        _Caculation_Parameters['_TieN_SDWidth'] = _TieN_SDWidth
        _Caculation_Parameters['_TieN_XVT'] = _TieN_XVT
        _Caculation_Parameters['_TieN_PCCrit'] = _TieN_PCCrit
        _Caculation_Parameters['_TieN_Source_Via_TF'] = _TieN_Source_Via_TF
        _Caculation_Parameters['_TieN_Drain_Via_TF'] = _TieN_Drain_Via_TF
        _Caculation_Parameters['_TieN_NMOSDummy'] = _TieN_NMOSDummy
        _Caculation_Parameters['_TieN_NMOSDummy_length'] = _TieN_NMOSDummy_length
        _Caculation_Parameters['_TieN_NMOSDummy_placement'] = _TieN_NMOSDummy_placement

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_TieCellNMOSRouted'] = self._SrefElementDeclaration(_DesignObj=C04_01_NmosRoute._NmosRoute(_DesignParameter=None, _Name='{}:SRF_TieCellNMOSRouted'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_TieCellNMOSRouted']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_TieCellNMOSRouted']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_TieCellNMOSRouted']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_TieCellNMOSRouted']['_XYCoordinates'] = [[0, 0]]


        ## C04_00_PMOSRoute(SREF) Generation
        _Caculation_Parameters = copy.deepcopy(C04_00_PmosRoute._PmosRoute._ParametersForDesignCalculation)
        _Caculation_Parameters['_TieP_PMOSNumberofGate'] = _TieP_PMOSNumberofGate
        _Caculation_Parameters['_TieP_PMOSChannelWidth'] = _TieP_PMOSChannelWidth
        _Caculation_Parameters['_TieP_PMOSChannellength'] = _TieP_PMOSChannellength
        _Caculation_Parameters['_TieP_GateSpacing'] = _TieP_GateSpacing
        _Caculation_Parameters['_TieP_SDWidth'] = _TieP_SDWidth
        _Caculation_Parameters['_TieP_XVT'] = _TieP_XVT
        _Caculation_Parameters['_TieP_PCCrit'] = _TieP_PCCrit
        _Caculation_Parameters['_TieP_Source_Via_TF'] = _TieP_Source_Via_TF
        _Caculation_Parameters['_TieP_Drain_Via_TF'] = _TieP_Drain_Via_TF
        _Caculation_Parameters['_TieP_PMOSDummy'] = _TieP_PMOSDummy
        _Caculation_Parameters['_TieP_PMOSDummy_length'] = _TieP_PMOSDummy_length
        _Caculation_Parameters['_TieP_PMOSDummy_placement'] = _TieP_PMOSDummy_placement

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_TieCellPMOSRouted'] = self._SrefElementDeclaration(_DesignObj=C04_00_PmosRoute._PmosRoute(_DesignParameter=None, _Name='{}:SRF_TieCellPMOSRouted'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_TieCellPMOSRouted']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_TieCellPMOSRouted']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_TieCellPMOSRouted']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_TieCellPMOSRouted']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_TieCellNMOSRouted','BND_NMOS_Gate_Hrz_poly')
        target_coord = tmp1[0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_TieCellPMOSRouted', 'BND_PMOS_Gate_Hrz_poly')
        approaching_coord = tmp2[0][0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_TieCellPMOSRouted')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[1] = Scoord[1] + SpacingHrzPolyBtwNmosRouteAndPmosRoute
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define Coordinates
        self._DesignParameter['SRF_TieCellPMOSRouted']['_XYCoordinates'] = tmpXY


        ## Path_element Generation
            ## Define Path_element ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['PTH_NPMOSRouting_VTC_M1'] = self._PathElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XYCoordinates=[],
        _Width=None,
        )
            ## Path Width: must be even number
        tmpN = self.get_param_KJH4('SRF_TieCellNMOSRouted','BND_NMOS_Gate_Hrz_Exten_M1')
        tmpP = self.get_param_KJH4('SRF_TieCellPMOSRouted', 'SRF_PMOS_Gate_ViaM0M1','SRF_ViaM0M1', 'BND_Met1Layer')
        # gate를 묶은 M1 boundary XWidth가 N,PMOS 중 더 큰 쪽을 Routing path의 width로 선택
        self._DesignParameter['PTH_NPMOSRouting_VTC_M1']['_Width'] = tmpN[0][0][0]['_Xwidth'] if tmpN[0][0][0]['_Xwidth'] >= tmpP[0][0][0][0][0]['_Xwidth'] \
                                                                                              else tmpP[0][0][0][0][0]['_Xwidth']

            ## P1--P2 coordiantes
        PTHX = tmpN[0][0][0]['_XY_down'][0] \
                    if tmpN[0][0][0]['_Xwidth'] >= tmpP[0][0][0][0][0]['_Xwidth'] \
                    else tmpP[0][0][0][0][0]['_XY_up'][0]
                ## P1 calculation
        PTHCoord1 = [PTHX, tmpN[0][0][0]['_XY_down'][1]]
                ## P2 calculation
        PTHCoord2 = [PTHX, tmpP[0][0][0][0][0]['_XY_up'][1]]
                ## P1<->P2
        PTHCoord12 = [[PTHCoord1, PTHCoord2]]

            ## Define Coordinates
        self._DesignParameter['PTH_NPMOSRouting_VTC_M1']['_XYCoordinates'] = PTHCoord12


        ### Body Contact
        ## N Body - PMOS Contact
        _Caculation_Parameters = copy.deepcopy(A05_NbodyContact_KJH2._NbodyContact_KJH2._ParametersForDesignCalculation)

        _Caculation_Parameters['_COX'] = _NBodyCOX
        _Caculation_Parameters['_COY'] = _NBodyCOY

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_PMOS_Body_Contact'] = self._SrefElementDeclaration(_DesignObj=A05_NbodyContact_KJH2._NbodyContact_KJH2(_DesignParameter=None, _Name='{}:SRF_PMOS_Body_Contact'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_PMOS_Body_Contact']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_PMOS_Body_Contact']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_PMOS_Body_Contact']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_PMOS_Body_Contact']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_TieCellPMOSRouted', 'SRF_PMOS', 'BND_ODLayer')
        target_coord = tmp1[0][0][0][0]['_XY_up']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_PMOS_Body_Contact', 'BND_ODLayer')
        approaching_coord = tmp2[0][0][0]['_XY_down']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_PMOS_Body_Contact')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[1] = Scoord[1] + SpacingODBtwPmosAndNBody
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define Coordinates
        self._DesignParameter['SRF_PMOS_Body_Contact']['_XYCoordinates'] = tmpXY


        ## P Body - NMOS Contact
        _Caculation_Parameters = copy.deepcopy(A06_PbodyContact_KJH2._PbodyContact_KJH2._ParametersForDesignCalculation)

        _Caculation_Parameters['_COX'] = _PBodyCOX
        _Caculation_Parameters['_COY'] = _PBodyCOY

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_NMOS_Body_Contact'] = self._SrefElementDeclaration(_DesignObj=A06_PbodyContact_KJH2._PbodyContact_KJH2(_DesignParameter=None, _Name='{}:SRF_NMOS_Body_Contact'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_NMOS_Body_Contact']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NMOS_Body_Contact']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NMOS_Body_Contact']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_NMOS_Body_Contact']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_TieCellNMOSRouted', 'SRF_NMOS', 'BND_ODLayer')
        target_coord = tmp1[0][0][0][0]['_XY_down']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_NMOS_Body_Contact', 'BND_ODLayer')
        approaching_coord = tmp2[0][0][0]['_XY_up']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_NMOS_Body_Contact')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[1] = Scoord[1] - SpacingODBtwNmosAndPBody
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define Coordinates
        self._DesignParameter['SRF_NMOS_Body_Contact']['_XYCoordinates'] = tmpXY


        ##Body-NMOS Routing
        # Boundary_element Generation
        self._DesignParameter['BND_NMOS_BodyRouting_Vtc_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_NMOS_BodyRouting_Vtc_M1']['_YWidth'] = self.get_param_KJH4('SRF_TieCellNMOSRouted','SRF_NMOS', 'BND_Met1Layer')[0][0][0][0]['_XY_down'][1] \
                                                                        - self.get_param_KJH4('SRF_NMOS_Body_Contact', 'BND_Met1Layer')[0][0][0]['_XY_up'][1]

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_NMOS_BodyRouting_Vtc_M1']['_XWidth'] = self.get_param_KJH4('SRF_TieCellNMOSRouted','SRF_NMOS', 'BND_Met1Layer')[0][0][0][0]['_Xwidth']

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_NMOS_BodyRouting_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1

        for i in range(0, int(_TieN_NMOSNumberofGate/2) + 1):
            tmp0 = self.get_param_KJH4('SRF_TieCellNMOSRouted','SRF_NMOS', 'BND_Met1Layer')
            tmp1 = self.get_param_KJH4('SRF_NMOS_Body_Contact', 'BND_Met1Layer')
            target_coord = [tmp0[0][0][2*i][0]['_XY_left'][0], tmp1[0][0][0]['_XY_up'][1]]
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_NMOS_BodyRouting_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_down_left']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('BND_NMOS_BodyRouting_Vtc_M1')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                            ## Define coordinates

        self._DesignParameter['BND_NMOS_BodyRouting_Vtc_M1']['_XYCoordinates'] = tmpXY


        ##Body-PMOS Routing
        # Boundary_element Generation
        self._DesignParameter['BND_PMOS_BodyRouting_Vtc_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_PMOS_BodyRouting_Vtc_M1']['_YWidth'] = self.get_param_KJH4('SRF_PMOS_Body_Contact', 'BND_Met1Layer')[0][0][0]['_XY_down'][1] - \
                                                                          self.get_param_KJH4('SRF_TieCellPMOSRouted','SRF_PMOS', 'BND_Met1Layer')[0][0][0][0]['_XY_up'][1]
                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_PMOS_BodyRouting_Vtc_M1']['_XWidth'] = self.get_param_KJH4('SRF_TieCellPMOSRouted','SRF_PMOS', 'BND_Met1Layer')[0][0][0][0]['_Xwidth']

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_PMOS_BodyRouting_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1

        for i in range(0, int(_TieP_PMOSNumberofGate/2) + 1):
            tmp0 = self.get_param_KJH4('SRF_TieCellPMOSRouted','SRF_PMOS', 'BND_Met1Layer')
            tmp1 = self.get_param_KJH4('SRF_PMOS_Body_Contact', 'BND_Met1Layer')
            target_coord = [tmp0[0][0][2*i][0]['_XY_left'][0], tmp1[0][0][0]['_XY_down'][1]]
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_PMOS_BodyRouting_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_up_left']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('BND_PMOS_BodyRouting_Vtc_M1')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                            ## Define coordinates

        self._DesignParameter['BND_PMOS_BodyRouting_Vtc_M1']['_XYCoordinates'] = tmpXY


        ## NMOS Gate-Drain Routing(Diode Connection)
        # Boundary_element Generation
        self._DesignParameter['BND_NMOS_DiodeConnection_Vtc_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_NMOS_DiodeConnection_Vtc_M1']['_YWidth'] = self.get_param_KJH4('SRF_TieCellNMOSRouted', 'BND_NMOS_Gate_Hrz_Exten_M1')[0][0][0]['_XY_down'][1] - \
                                                                              self.get_param_KJH4('SRF_TieCellNMOSRouted','SRF_NMOS', 'BND_Met1Layer')[0][0][0][0]['_XY_up'][1]


                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_NMOS_DiodeConnection_Vtc_M1']['_XWidth'] = self.get_param_KJH4('SRF_TieCellNMOSRouted','SRF_NMOS', 'BND_Met1Layer')[0][0][0][0]['_Xwidth']

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_NMOS_DiodeConnection_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1

        for i in range(0, int(_TieP_PMOSNumberofGate/2)):
            tmp0 = self.get_param_KJH4('SRF_TieCellNMOSRouted','SRF_NMOS', 'BND_Met1Layer')
            tmp1 = self.get_param_KJH4('SRF_TieCellNMOSRouted', 'BND_NMOS_Gate_Hrz_Exten_M1')
            target_coord = [tmp0[0][0][2*i+1][0]['_XY_left'][0], tmp1[0][0][0]['_XY_down'][1]]
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_NMOS_DiodeConnection_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_up_left']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('BND_NMOS_DiodeConnection_Vtc_M1')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                            ## Define coordinates

        self._DesignParameter['BND_NMOS_DiodeConnection_Vtc_M1']['_XYCoordinates'] = tmpXY


        ## PMOS NWell Boundary Generation
        self._DesignParameter['BND_PMOS_NWell'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['NWELL'][0],
        _Datatype=DesignParameters._LayerMapping['NWELL'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp0 = self.get_param_KJH4('SRF_PMOS_Body_Contact','BND_Nwell')
        tmp1 = self.get_param_KJH4('SRF_TieCellPMOSRouted','SRF_PMOS', 'BND_PPLayer')
        self._DesignParameter['BND_PMOS_NWell']['_YWidth'] = abs(tmp0[0][0][0]['_XY_down'][1] - tmp1[0][0][0][0]['_XY_down'][1]) + _DRCObj._NwMinEnclosurePactive2

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_PMOS_NWell']['_XWidth'] = tmp0[0][0][0]['_Xwidth']

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_PMOS_NWell']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_PMOS_Body_Contact','BND_Nwell')
        target_coord = tmp1[0][0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOS_NWell')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOS_NWell')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_PMOS_NWell']['_XYCoordinates'] = tmpXY


        ## PMOS NWell Extension Boundary Generation (GR134a_M2)
        # Boundary_element Generation
        self._DesignParameter['BND_Nwell_Extension'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp0 = self.get_param_KJH4('SRF_PMOS_Body_Contact', 'BND_Nwell')
        tmp1 = self.get_param_KJH4('BND_PMOS_NWell')
        self._DesignParameter['BND_Nwell_Extension']['_YWidth'] = 2 * (tmp0[0][0][0]['_Ywidth'] + tmp1[0][0]['_Ywidth'])
        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Nwell_Extension']['_XWidth'] = tmp1[0][0]['_Xwidth']

        ## Calculate XYcoord
        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Nwell_Extension']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_PMOS_NWell')
        target_coord = tmp1[0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Nwell_Extension')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Nwell_Extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Scoord[1] = Scoord[1] - SpacingODBtwNmosAndPBody
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define Coordinates
        self._DesignParameter['BND_Nwell_Extension']['_XYCoordinates'] = tmpXY


############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_RcdacSar_C06_VddTieCell6_YJ'
    cellname = 'C06_01_VddTieCell6_YJ_v01'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object ''' ############################################################### ^^^^^^^^^^^^^^^^^^^^^
    InputParams = dict(
        # TieN
        _TieN_NMOSNumberofGate=6,  # number
        _TieN_NMOSChannelWidth=250,  # number
        _TieN_NMOSChannellength=30,  # number
        _TieN_GateSpacing=100,  # None/number
        _TieN_SDWidth=None,  # None/number
        _TieN_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _TieN_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _TieN_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _TieN_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _TieN_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _TieN_NMOSDummy_length=None,  # None/Value
        _TieN_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # TieP
        _TieP_PMOSNumberofGate=6,  # number
        _TieP_PMOSChannelWidth=500,  # number
        _TieP_PMOSChannellength=30,  # number
        _TieP_GateSpacing=100,  # None/number
        _TieP_SDWidth=None,  # None/number
        _TieP_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _TieP_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _TieP_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _TieP_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _TieP_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _TieP_PMOSDummy_length=None,  # None/Value
        _TieP_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Body Contact
        _NBodyCOX=10,
        _NBodyCOY=2,
        _PBodyCOX=10,
        _PBodyCOY=2,
    )

    '''Mode_DRCCHECK '''
    Mode_DRCCheck = False
    Num_DRCCheck =1

    for ii in range(0, Num_DRCCheck if Mode_DRCCheck else 1):
        if Mode_DRCCheck:
            ''' Input Parameters for Layout Object '''
        else:
            pass

    ''' Generate Layout Object '''
    LayoutObj = _TieCell4(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    # testStreamFile = open('./gdsfile/{}'.format(_fileName), 'wb')
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
    #Checker.lib_deletion()
    #Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    #Checker_KJH0.DRCchecker()

    ''' Check Time'''
    elapsed_time = time.time() - start_time
    m, s = divmod(elapsed_time,60)
    h, m = divmod(m, 60)

    print ('#############################      Finished      ################################')
# end of 'main():' ---------------------------------------------------------------------------------------------