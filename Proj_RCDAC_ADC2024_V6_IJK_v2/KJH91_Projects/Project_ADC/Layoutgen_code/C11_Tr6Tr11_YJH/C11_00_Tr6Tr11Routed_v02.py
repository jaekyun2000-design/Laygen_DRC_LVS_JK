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
from KJH91_Projects.Project_ADC.Layoutgen_code.C08_Tr11_KJH import C08_01_Guardring
from KJH91_Projects.Project_ADC.Layoutgen_code.C09_Tr6_KJH import C09_01_Guardring


############################################################################################################################################################ Class_HEADER

class _Tr4Tr6Routed(StickDiagram_KJH1._StickDiagram_KJH):

    ##########################################################################################################################
    # Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

        ## Tr6
        _Tr6_NMOSNumberofGate=6,  # number
        _Tr6_NMOSChannelWidth=1000,  # number
        _Tr6_NMOSChannellength=30,  # number
        _Tr6_GateSpacing=100,  # None/number
        _Tr6_SDWidth=None,  # None/number
        _Tr6_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Tr6_PCCrit=True,  # None/True

        # Tr6 Source_node_ViaM1M2
        _Tr6_Source_Via_TF=False,  # True/False

        # Tr6 Drain_node_ViaM1M2
        _Tr6_Drain_Via_TF=False,  # True/False

        # Tr6 POLY dummy setting
        _Tr6_NMOSDummy=True,  # TF
        # Tr6 if _PMOSDummy == True
        _Tr6_NMOSDummy_length=None,  # None/Value
        _Tr6_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr6 Vp node
        _Tr6_Vp_node_width=280,  # Number
        _Tr6_Vp_node_metal_Layer=4,  # number

        # Tr6 Guardring
        # Pbody: number of contact
        # Nbody
        _Tr6_NwellWidth=850,  # number

        # PMOS: Tr11
        _Tr11_PMOSNumberofGate=2,
        _Tr11_PMOSChannelWidth=1000,
        _Tr11_PMOSChannellength=30,
        _Tr11_GateSpacing=None,
        _Tr11_SDWidth=None,
        _Tr11_XVT='SLVT',
        _Tr11_PCCrit=None,

        # Source_node_ViaM1M2
        _Tr11_Source_Via_TF=True,

        # Drain_node_ViaM1M2
        _Tr11_Drain_Via_TF=True,

        # POLY dummy setting
        _Tr11_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Tr11_PMOSDummy_length=None,  # None/Value
        _Tr11_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Nbodyring(Guardring)
        _Tr11_Guardring_NumCont=3,  # number
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

                                  ## Tr6
                                  _Tr6_NMOSNumberofGate=6,  # number
                                  _Tr6_NMOSChannelWidth=1000,  # number
                                  _Tr6_NMOSChannellength=30,  # number
                                  _Tr6_GateSpacing=100,  # None/number
                                  _Tr6_SDWidth=None,  # None/number
                                  _Tr6_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Tr6_PCCrit=True,  # None/True

                                  # Tr6 Source_node_ViaM1M2
                                  _Tr6_Source_Via_TF=False,  # True/False

                                  # Tr6 Drain_node_ViaM1M2
                                  _Tr6_Drain_Via_TF=False,  # True/False

                                  # Tr6 POLY dummy setting
                                  _Tr6_NMOSDummy=True,  # TF
                                  # Tr6 if _PMOSDummy == True
                                  _Tr6_NMOSDummy_length=None,  # None/Value
                                  _Tr6_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Tr6 Vp node
                                  _Tr6_Vp_node_width=280,  # Number
                                  _Tr6_Vp_node_metal_Layer=4,  # number

                                  # Tr6 Guardring
                                  # Pbody: number of contact
                                  # Nbody
                                  _Tr6_NwellWidth=850,  # number

                                  # PMOS: Tr11
                                  _Tr11_PMOSNumberofGate=2,
                                  _Tr11_PMOSChannelWidth=1000,
                                  _Tr11_PMOSChannellength=30,
                                  _Tr11_GateSpacing=None,
                                  _Tr11_SDWidth=None,
                                  _Tr11_XVT='SLVT',
                                  _Tr11_PCCrit=None,

                                  # Source_node_ViaM1M2
                                  _Tr11_Source_Via_TF=True,

                                  # Drain_node_ViaM1M2
                                  _Tr11_Drain_Via_TF=True,

                                  # POLY dummy setting
                                  _Tr11_PMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tr11_PMOSDummy_length=None,  # None/Value
                                  _Tr11_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Nbodyring(Guardring)
                                  _Tr11_Guardring_NumCont=3,  # number
                                  ):

        ## Class_HEADER: Pre Defined Parameter Before Calculation
        Tr6Tr11GateRoutePathWidth = 250
        Tr6Tr11DrainRoutePathWidth = 250
        LeftExtensionTr6Drain_Hrz_M4 = 1500

        ## Load DRC library
        _DRCObj = DRC.DRC()
        ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']
        ## CALCULATION START
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

        ## Tr11 SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C08_01_Guardring._Guardring._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr11_PMOSNumberofGate'] = _Tr11_PMOSNumberofGate
        _Caculation_Parameters['_Tr11_PMOSChannelWidth'] = _Tr11_PMOSChannelWidth
        _Caculation_Parameters['_Tr11_PMOSChannellength'] = _Tr11_PMOSChannellength
        _Caculation_Parameters['_Tr11_GateSpacing'] = _Tr11_GateSpacing
        _Caculation_Parameters['_Tr11_SDWidth'] = _Tr11_SDWidth
        _Caculation_Parameters['_Tr11_XVT'] = _Tr11_XVT
        _Caculation_Parameters['_Tr11_PCCrit'] = _Tr11_PCCrit
        _Caculation_Parameters['_Tr11_Source_Via_TF'] = _Tr11_Source_Via_TF
        _Caculation_Parameters['_Tr11_Drain_Via_TF'] = _Tr11_Drain_Via_TF
        _Caculation_Parameters['_Tr11_PMOSDummy'] = _Tr11_PMOSDummy
        _Caculation_Parameters['_Tr11_PMOSDummy_length'] = _Tr11_PMOSDummy_length
        _Caculation_Parameters['_Tr11_PMOSDummy_placement'] = _Tr11_PMOSDummy_placement
        _Caculation_Parameters['_Tr11_Guardring_NumCont'] = _Tr11_Guardring_NumCont

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Tr11'] = self._SrefElementDeclaration(_DesignObj=C08_01_Guardring._Guardring(_DesignParameter=None, _Name='{}:SRF_Tr11'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Tr11']['_Reflect'] = [1, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr11']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr11']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr11']['_XYCoordinates'] = [[0, 0]]

        ## TR6 SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C09_01_Guardring._Guardring._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr6_NMOSNumberofGate'] = _Tr6_NMOSNumberofGate
        _Caculation_Parameters['_Tr6_NMOSChannelWidth'] = _Tr6_NMOSChannelWidth
        _Caculation_Parameters['_Tr6_NMOSChannellength'] = _Tr6_NMOSChannellength
        _Caculation_Parameters['_Tr6_GateSpacing'] = _Tr6_GateSpacing
        _Caculation_Parameters['_Tr6_SDWidth'] = _Tr6_SDWidth
        _Caculation_Parameters['_Tr6_XVT'] = _Tr6_XVT
        _Caculation_Parameters['_Tr6_PCCrit'] = _Tr6_PCCrit
        _Caculation_Parameters['_Tr6_Source_Via_TF'] = _Tr6_Source_Via_TF
        _Caculation_Parameters['_Tr6_Drain_Via_TF'] = _Tr6_Drain_Via_TF
        _Caculation_Parameters['_Tr6_NMOSDummy'] = _Tr6_NMOSDummy
        _Caculation_Parameters['_Tr6_NMOSDummy_length'] = _Tr6_NMOSDummy_length
        _Caculation_Parameters['_Tr6_NMOSDummy_placement'] = _Tr6_NMOSDummy_placement
        _Caculation_Parameters['_Vp_node_width'] = _Tr6_Vp_node_width
        _Caculation_Parameters['_Vp_node_metal_Layer'] = _Tr6_Vp_node_metal_Layer
        _Caculation_Parameters['_NwellWidth'] = _Tr6_NwellWidth

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Tr6'] = self._SrefElementDeclaration(_DesignObj=C09_01_Guardring._Guardring(_DesignParameter=None, _Name='{}:SRF_Tr6'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Tr6']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr6']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr6']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                    ## Calculate Tr6 Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Tr6']['_XYCoordinates'] = [[0, 0]]

        tmp1 = self.get_param_KJH4('SRF_Tr11','BND_Nwellcovering')
        target_coord = tmp1[0][0][0]['_XY_up']      #Tr11 맨 아래 가운데 좌표

        tmp2 = self.get_param_KJH4('SRF_Tr6','BND_Deepnwell')
        approaching_coord = tmp2[0][0][0]['_XY_cent']
        approaching_coord[1] = self.get_outter_KJH4('SRF_Tr6')['_Mostup']['coord'][0]   #Tr6맨 위 가운데 좌표

        tmp3 = self.get_param_KJH4('SRF_Tr6')
        Scoord = tmp3[0][0]['_XY_origin']

        tmp4_1 = self.get_param_KJH4('SRF_Tr11', 'SRF_Nbodyring', 'SRF_NbodyTop', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')[0][0][0][0][0][0]['_XY_up'][1]
        tmp4_2 = target_coord[1]
        tmp5_1 = self.get_param_KJH4('SRF_Tr6', 'SRF_Pbodyring', 'SRF_PbodyTop', 'SRF_PbodyContactPhyLen','BND_PPLayer')[0][0][0][0][0][0]['_XY_up'][1]
        tmp5_2 = self.get_param_KJH4('SRF_Tr6', 'SRF_Pbodyring', 'SRF_PbodyTop', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')[0][0][0][0][0][0]['_XY_up'][1]
        a= abs(tmp4_1 - tmp4_2)
        b=abs(tmp5_1 - tmp5_2)
        Tr6Tr11MinSpace = _DRCObj._Metal1MinSpace3 - abs(tmp4_1 - tmp4_2) - abs(tmp5_1 - tmp5_2) # Tr6Tr11MinSpace=63
        Tr6Tr11Space = 40
        Scoord[1] = Scoord[1] - max(Tr6Tr11MinSpace, Tr6Tr11Space)

        c= self.get_outter_KJH4('SRF_Tr6')['_Mostup']['coord'][0]

                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['SRF_Tr6']['_XYCoordinates'] = tmpXY


        ## Tr6 - Tr11 Gate routing (M3)
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Tr6Tr11GateRouting_Vtc_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Tr11', 'BND_Gate_Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_Tr6', 'SRF_Tr6', 'BND_Gate_Hrz_M2')
        self._DesignParameter['BND_Tr6Tr11GateRouting_Vtc_M2']['_YWidth'] = tmp1[0][0][0]['_XY_down_right'][1] - tmp2[0][0][0][0]['_XY_down_right'][1]

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Tr6Tr11GateRouting_Vtc_M2']['_XWidth'] = Tr6Tr11GateRoutePathWidth

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Tr6Tr11GateRouting_Vtc_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = [0, tmp1[0][0][0]['_XY_down'][1]]
        target_coord[0] = min([tmp1[0][0][0]['_XY_up_right'][0], tmp2[0][0][0][0]['_XY_down_right'][0]]) #더 왼쪽에 있는 좌표 리턴
                            ## Approaching_coord: _XY_type2
        tmp = self.get_param_KJH4('BND_Tr6Tr11GateRouting_Vtc_M2')
        approaching_coord = tmp[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Tr6Tr11GateRouting_Vtc_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Tr6Tr11GateRouting_Vtc_M2']['_XYCoordinates'] = tmpXY


        ## Tr6 Drain Short시키는 M4 Boundary(Hrz)
        self._DesignParameter['BND_Tr6Drain_Hrz_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('SRF_Tr6', 'SRF_Tr6', 'SRF_Tr6_Source_ViaM1Mx','SRF_ViaM1M2','BND_Met2Layer')
        self._DesignParameter['BND_Tr6Drain_Hrz_M3']['_YWidth'] = abs(tmp[0][0][0][0][0][0]['_XY_up_right'][1] - tmp[0][0][0][0][0][0]['_XY_down_right'][1])

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Tr6Drain_Hrz_M3']['_XWidth'] = abs(tmp[0][0][0][0][0][0]['_XY_down_left'][0] - tmp[0][0][-1][0][0][0]['_XY_down_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Tr6Drain_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Tr6Drain_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Tr6', 'SRF_Tr6', 'SRF_Tr6_Source_ViaM1Mx','SRF_ViaM1M2','BND_Met2Layer')
        target_coord = tmp1[0][0][-1][0][0][0]['_XY_down_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Tr6Drain_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_down_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Tr6Drain_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Tr6Drain_Hrz_M3']['_XYCoordinates'] = tmpXY


        ## Tr6 - Tr11 Drain routing (M4)
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Tr6Tr11DrainRouting_Vtc_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Tr11', 'BND_Source_Hrz_M3')
        tmp2 = self.get_param_KJH4('BND_Tr6Drain_Hrz_M3')
        self._DesignParameter['BND_Tr6Tr11DrainRouting_Vtc_M3']['_YWidth'] = abs(tmp1[0][0][0]['_XY_down_right'][1] - tmp2[0][0]['_XY_down_right'][1])

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Tr6Tr11DrainRouting_Vtc_M3']['_XWidth'] = Tr6Tr11DrainRoutePathWidth

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Tr6Tr11DrainRouting_Vtc_M3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = [0, tmp1[0][0][0]['_XY_down'][1]]
        target_coord[0] = max([tmp1[0][0][0]['_XY_up_left'][0], tmp2[0][0]['_XY_down_left'][0]]) #더 오른쪽에 있는 좌표 리턴
                            ## Approaching_coord: _XY_type2
        tmp = self.get_param_KJH4('BND_Tr6Tr11DrainRouting_Vtc_M3')
        approaching_coord = tmp[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Tr6Tr11DrainRouting_Vtc_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Tr6Tr11DrainRouting_Vtc_M3']['_XYCoordinates'] = tmpXY











############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    Start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_RcdacSar_C11_Tr6Tr11_YJH'
    cellname = 'Proj_C11_01_Tr6Tr11Routed_YJ_v02_94'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        ## Tr6
        _Tr6_NMOSNumberofGate=4,  # number
        _Tr6_NMOSChannelWidth=500,  # number
        _Tr6_NMOSChannellength=30,  # number
        _Tr6_GateSpacing=100,  # None/number
        _Tr6_SDWidth=None,  # None/number
        _Tr6_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Tr6_PCCrit=True,  # None/True

        # Tr6 Source_node_ViaM1M2
        _Tr6_Source_Via_TF=False,  # True/False

        # Tr6 Drain_node_ViaM1M2
        _Tr6_Drain_Via_TF=False,  # True/False

        # Tr6 POLY dummy setting
        _Tr6_NMOSDummy=True,  # TF
        # Tr6 if _PMOSDummy == True
        _Tr6_NMOSDummy_length=None,  # None/Value
        _Tr6_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr6 Vp node
        _Tr6_Vp_node_width=280,  # Number
        _Tr6_Vp_node_metal_Layer=4,  # number

        # Tr6 Guardring
        # Pbody: number of contact
        # Nbody
        _Tr6_NwellWidth=850,  # number

        # PMOS: Tr11
        _Tr11_PMOSNumberofGate=4,
        _Tr11_PMOSChannelWidth=1000,
        _Tr11_PMOSChannellength=30,
        _Tr11_GateSpacing=100,
        _Tr11_SDWidth=None,
        _Tr11_XVT='SLVT',
        _Tr11_PCCrit=None,

        # Source_node_ViaM1M2
        _Tr11_Source_Via_TF=True,

        # Drain_node_ViaM1M2
        _Tr11_Drain_Via_TF=True,

        # POLY dummy setting
        _Tr11_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Tr11_PMOSDummy_length=None,  # None/Value
        _Tr11_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Nbodyring(Guardring)
        _Tr11_Guardring_NumCont=3,  # number
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
    LayoutObj = _Tr4Tr6Routed(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    # testStreamFile = open('./gdsfile/{}'.format(_fileName), 'wb')
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
    elapsed_time = time.time() - Start_time
    m, s = divmod(elapsed_time, 60)
    h, m = divmod(m, 60)

    print('#############################      Finished      ################################')
# end of 'main():' ---------------------------------------------------------------------------------------------
