## Import Basic Modules
    ## Engine
from Proj_RCDAC_ADC2024_V6_IJK.KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_ADC.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC
#from KJH91_Projects.Project_ADC.Library_and_Engine import DRCv2

    ## Library
import copy
import math
import numpy as np
import time

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A05_NbodyContact_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A06_PbodyContact_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A07_NbodyContactPhyLen_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A08_PbodyContactPhyLen_KJH3

from Proj_RCDAC_ADC2024_V6_IJK.KJH91_Projects.Project_ADC.Layoutgen_code.C04_Tiecell_Fixed import C04_00_PmosRoute
from Proj_RCDAC_ADC2024_V6_IJK.KJH91_Projects.Project_ADC.Layoutgen_code.C04_Tiecell_Fixed import C04_01_NmosRoute


############################################################################################################################################################ Class_HEADER
class _TieCell4(StickDiagram_KJH1._StickDiagram_KJH):

    ##########################################################################################################################
    # Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(
# Tie4N
    # Physical dimension
    _Tie4N_NumberofGate	            = 4,       # Number
    _Tie4N_ChannelWidth	            = 250,     # Number
    _Tie4N_ChannelLength	        = 30,       # Number
    _Tie4N_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# Tie4P
    # Physical dimension
    _Tie4P_NumberofGate	            = 4,       # Number
    _Tie4P_ChannelWidth	            = 500,     # Number
    _Tie4P_ChannelLength	        = 30,       # Number
    _Tie4P_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

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
# Tie4N
    # Physical dimension
    _Tie4N_NumberofGate	            = 4,       # Number
    _Tie4N_ChannelWidth	            = 250,     # Number
    _Tie4N_ChannelLength	        = 30,       # Number
    _Tie4N_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# Tie4P
    # Physical dimension
    _Tie4P_NumberofGate	            = 4,       # Number
    _Tie4P_ChannelWidth	            = 500,     # Number
    _Tie4P_ChannelLength	        = 30,       # Number
    _Tie4P_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

                                  ):

        ## Class_HEADER: Pre Defined Parameter Before Calculation
            ## Load DRC library
        _DRCObj = DRC.DRC()
            ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']


        ## CALCULATION START
        start_time = time.time()
        # end_time = time.time()
        # self.elapsed_time = end_time - start_time
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')


        # Pre-defined Design Value
        SpacingODBtwPmosAndNBody = 180
        SpacingODBtwNmosAndPBody = 180
        SpacingHrzPolyBtwNmosRouteAndPmosRoute = 180

        ## ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## C04_01_NMOSRoute(SREF) Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C04_01_NmosRoute._NmosRoute._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_TieN_NumberofGate'] = _Tie4N_NumberofGate
        _Caculation_Parameters['_TieN_ChannelWidth'] = _Tie4N_ChannelWidth
        _Caculation_Parameters['_TieN_ChannelLength'] = _Tie4N_ChannelLength
        _Caculation_Parameters['_TieN_XVT'] = _Tie4N_XVT

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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## C04_00_PMOSRoute(SREF) Generation
        _Caculation_Parameters = copy.deepcopy(C04_00_PmosRoute._PmosRoute._ParametersForDesignCalculation)
        _Caculation_Parameters['_TieP_NumberofGate'] = _Tie4P_NumberofGate
        _Caculation_Parameters['_TieP_ChannelWidth'] = _Tie4P_ChannelWidth
        _Caculation_Parameters['_TieP_ChannelLength'] = _Tie4P_ChannelLength
        _Caculation_Parameters['_TieP_XVT'] = _Tie4P_XVT

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
        tmp1 = self.get_param_KJH4('SRF_TieCellNMOSRouted','SRF_Nmos','BND_Gate_Hrz_poly')
        target_coord = tmp1[0][0][0][0]['_XY_up']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_TieCellPMOSRouted','SRF_Pmos','BND_Gate_Hrz_poly')
        approaching_coord = tmp2[0][0][0][0]['_XY_down']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_TieCellPMOSRouted')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[1] = Scoord[1] + SpacingHrzPolyBtwNmosRouteAndPmosRoute
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define Coordinates
        self._DesignParameter['SRF_TieCellPMOSRouted']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Path_element Generation 2
        ## Path Name:
        Path_name = 'NPMOSRouting_VTC_M1'

        ## Path Width: ***** must be even number ***
        tmpN = self.get_param_KJH4('SRF_TieCellNMOSRouted','SRF_Nmos','BND_PODummyLayer')
        LengthN = abs(tmpN[0][0][-1][0]['_XY_right'][0] - tmpN[0][0][0][0]['_XY_left'][0])
        tmpP = self.get_param_KJH4('SRF_TieCellPMOSRouted', 'SRF_Pmos','BND_PODummyLayer')
        LengthP = abs(tmpP[0][0][-1][0]['_XY_right'][0] - tmpP[0][0][0][0]['_XY_left'][0])
        # gate를 묶은 M1 boundary XWidth가 N,PMOS 중 더 큰 쪽을 Routing path의 width로 선택
        if LengthN > LengthP:
            Path_width = LengthN
        else:
            Path_width = LengthP

        ## tmp
        tmpXY = []
        tmpMetal = []
        tmpViaTF = []
        tmpViaDir = []
        tmpViaWid = []

        ## coord1
        ## P1 calculation
        tmp = self.get_param_KJH4('SRF_TieCellPMOSRouted', 'SRF_Pmos','BND_Gate_Hrz_Mx')
        P1 = tmp[0][0][0][0]['_XY_up']
        ## P2 calculation
        tmp = self.get_param_KJH4('SRF_TieCellNMOSRouted','SRF_Nmos','BND_Gate_Hrz_Mx')
        P2 = tmp[0][0][0][0]['_XY_down']
        ## Metal Layer
        Metal = 1
        ## Via: True=1/False=0
        ViaTF = 0
        ## Via: Vtc=1/Hrz=0/Ovl=2
        ViaDir = 1
        ## Via width: None/[1,3]
        ViaWid = None

        tmpXY.append([P1, P2])
        tmpMetal.append(Metal)
        tmpViaTF.append(ViaTF)
        tmpViaDir.append(ViaDir)
        tmpViaWid.append(ViaWid)

        tmpXY = self.get_PTH_KJH2(Path_name, Path_width, tmpXY, tmpMetal, tmpViaTF, tmpViaDir, tmpViaWid, _Name)


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  NBody Contact
        _NumContTop =3

        # Cal Length
        tmp =self.get_outter_KJH5('SRF_TieCellPMOSRouted','SRF_Pmos')
        _XlengthIntn = abs(tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0])

        # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A07_NbodyContactPhyLen_KJH3._NbodyContactPhyLen._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length'] = _XlengthIntn
        _Caculation_Parameters['_NumCont'] = _NumContTop
        _Caculation_Parameters['_Vtc_flag'] = False

        # Generate Sref
        self._DesignParameter['SRF_PMOS_Body_Contact'] = self._SrefElementDeclaration(_DesignObj=A07_NbodyContactPhyLen_KJH3._NbodyContactPhyLen(_DesignParameter=None, _Name='{}:SRF_PMOS_Body_Contact'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_PMOS_Body_Contact']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_PMOS_Body_Contact']['_Angle'] = 0

        # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_PMOS_Body_Contact']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        # Define Sref _XYcoordinate
        self._DesignParameter['SRF_PMOS_Body_Contact']['_XYCoordinates'] = [[0, 0]]

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_PMOS_Body_Contact']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_TieCellPMOSRouted', 'SRF_Pmos', 'BND_ODLayer')
        target_coord = tmp1[0][0][0][0]['_XY_up']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_PMOS_Body_Contact','SRF_NbodyContactPhyLen','BND_ODLayer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_PMOS_Body_Contact')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[1] = Scoord[1] + SpacingODBtwPmosAndNBody
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define Coordinates
        self._DesignParameter['SRF_PMOS_Body_Contact']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  PBody Contact
            ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length']   = None
        _Caculation_Parameters['_NumCont']  = 3
        _Caculation_Parameters['_Vtc_flag'] = False

                ## Cal length
        tmp =self.get_outter_KJH5('SRF_TieCellNMOSRouted','SRF_Nmos')
        _Length2 = abs(tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0])
        _Caculation_Parameters['_Length']   = _Length2

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_NMOS_Body_Contact'] = self._SrefElementDeclaration(_DesignObj=A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen(_DesignParameter=None, _Name='{}:SRF_NMOS_Body_Contact'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_NMOS_Body_Contact']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NMOS_Body_Contact']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NMOS_Body_Contact']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NMOS_Body_Contact']['_XYCoordinates'] = [[0, 0]]

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_NMOS_Body_Contact']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_TieCellNMOSRouted', 'SRF_Nmos', 'BND_ODLayer')
        target_coord = tmp1[0][0][0][0]['_XY_down']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_NMOS_Body_Contact','SRF_PbodyContactPhyLen','BND_ODLayer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_NMOS_Body_Contact')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[1] = Scoord[1] - SpacingODBtwNmosAndPBody
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define Coordinates
        self._DesignParameter['SRF_NMOS_Body_Contact']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Body-NMOS Routing
        # Boundary_element Generation
        self._DesignParameter['BND_NMOS_BodyRouting_Vtc_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_TieCellNMOSRouted','SRF_Nmos', 'BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_NMOS_Body_Contact','SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        self._DesignParameter['BND_NMOS_BodyRouting_Vtc_M1']['_YWidth'] = abs(tmp1[0][0][0][0]['_XY_down'][1]-tmp2[0][0][0][0]['_XY_up'][1])

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_TieCellNMOSRouted','SRF_Nmos', 'BND_Met1Layer')
        self._DesignParameter['BND_NMOS_BodyRouting_Vtc_M1']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_NMOS_BodyRouting_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1

        for i in range(0, int(_Tie4N_NumberofGate/2) + 1):
            tmp0 = self.get_param_KJH4('SRF_TieCellNMOSRouted','SRF_Nmos', 'BND_Met1Layer')
            tmp1 = self.get_param_KJH4('SRF_NMOS_Body_Contact','SRF_PbodyContactPhyLen', 'BND_Met1Layer')
            target_coord = [tmp0[0][0][2*i][0]['_XY_left'][0], tmp1[0][0][0][0]['_XY_up'][1]]
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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Body-PMOS Routing
        # Boundary_element Generation
        self._DesignParameter['BND_PMOS_BodyRouting_Vtc_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 =  self.get_param_KJH4('SRF_PMOS_Body_Contact','SRF_NbodyContactPhyLen','BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_TieCellPMOSRouted', 'SRF_Pmos', 'BND_Met1Layer')
        self._DesignParameter['BND_PMOS_BodyRouting_Vtc_M1']['_YWidth'] = abs(tmp1[0][0][0][0]['_XY_down'][1]-tmp2[0][0][0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        tmp =  self.get_param_KJH4('SRF_TieCellPMOSRouted', 'SRF_Pmos', 'BND_Met1Layer')
        self._DesignParameter['BND_PMOS_BodyRouting_Vtc_M1']['_XWidth'] =tmp[0][0][0][0]['_Xwidth']

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_PMOS_BodyRouting_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1

        for i in range(0, int(_Tie4P_NumberofGate / 2) + 1):
            tmp0 = self.get_param_KJH4('SRF_TieCellPMOSRouted', 'SRF_Pmos', 'BND_Met1Layer')
            tmp1 = self.get_param_KJH4('SRF_PMOS_Body_Contact', 'SRF_NbodyContactPhyLen','BND_Met1Layer')
            target_coord = [tmp0[0][0][2 * i][0]['_XY_left'][0], tmp1[0][0][0][0]['_XY_down'][1]]
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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS Gate-Drain Routing(Diode Connection)
        # Boundary_element Generation
        self._DesignParameter['BND_NMOS_DiodeConnection_Vtc_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_TieCellNMOSRouted', 'SRF_Nmos', 'BND_Gate_Hrz_Mx')
        tmp2 = self.get_param_KJH4('SRF_TieCellNMOSRouted', 'SRF_Nmos', 'BND_Met1Layer')
        self._DesignParameter['BND_NMOS_DiodeConnection_Vtc_M1']['_YWidth'] =  abs(tmp1[0][0][0][0]['_XY_down'][1]-tmp2[0][0][0][0]['_XY_up'][1])


        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_TieCellNMOSRouted', 'SRF_Nmos', 'BND_Met1Layer')
        self._DesignParameter['BND_NMOS_DiodeConnection_Vtc_M1']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_NMOS_DiodeConnection_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1

        tmp = self.get_param_KJH4('SRF_TieCellNMOSRouted', 'SRF_Nmos', 'BND_Drain_M1')
        for i in range(0, len(tmp[0][0])):
            tmp0 = self.get_param_KJH4('SRF_TieCellNMOSRouted', 'SRF_Nmos', 'BND_Met1Layer')
            tmp1 = self.get_param_KJH4('SRF_TieCellNMOSRouted', 'SRF_Nmos', 'BND_Gate_Hrz_Mx')
            target_coord = [tmp0[0][0][2 * i + 1][0]['_XY_left'][0], tmp1[0][0][0][0]['_XY_down'][1]]
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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS NWell Boundary Generation
        self._DesignParameter['BND_PMOS_NWell'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp0 = self.get_param_KJH4('SRF_PMOS_Body_Contact', 'SRF_NbodyContactPhyLen','BND_Nwell')
        tmp1 = self.get_param_KJH4('SRF_TieCellPMOSRouted', 'SRF_Pmos', 'BND_PPLayer')
        self._DesignParameter['BND_PMOS_NWell']['_YWidth'] = abs(tmp0[0][0][0][0]['_XY_down'][1] - tmp1[0][0][0][0]['_XY_down'][1]) + _DRCObj._NwMinEnclosurePactive2

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_PMOS_NWell']['_XWidth'] = tmp0[0][0][0][0]['_Xwidth']

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_PMOS_NWell']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_PMOS_Body_Contact','SRF_NbodyContactPhyLen','BND_Nwell')
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS NWell Extension Boundary Generation (GR134a_M2)
        # Boundary_element Generation
        self._DesignParameter['BND_Nwell_Extension'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp0 = self.get_param_KJH4('SRF_PMOS_Body_Contact', 'SRF_NbodyContactPhyLen','BND_Nwell')
        tmp1 = self.get_param_KJH4('BND_PMOS_NWell')
        self._DesignParameter['BND_Nwell_Extension']['_YWidth'] = 2 * (tmp0[0][0][0][0]['_Ywidth'] + tmp1[0][0]['_Ywidth'])

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

        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')
        # start_time = time.time()
        end_time = time.time()
        self.elapsed_time = end_time - start_time

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0
    import random

    # libname = 'Proj_ZZ01_C06_00_VddTieCell_Fixed'
    for _iter in range(5):
        cellname = 'C06_01_VddTieCell_v{}'.format(_iter + 1)
        _fileName = cellname + '.gds'

        _Tie4_Gate = random.randrange(1, 5, 1)
        _Tie4_Width = random.randrange(400, 1000, 100)

        ''' Input Parameters for Layout Object ''' ############################################################### ^^^^^^^^^^^^^^^^^^^^^
        InputParams = dict(
    # Tie4N
        # Physical dimension
        _Tie4N_NumberofGate	            = _Tie4_Gate,       # Number
        _Tie4N_ChannelWidth	            = _Tie4_Width,     # Number
        _Tie4N_ChannelLength	        = 30,       # Number
        _Tie4N_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

    # Tie4P
        # Physical dimension
        _Tie4P_NumberofGate	            = _Tie4_Gate,       # Number
        _Tie4P_ChannelWidth	            = _Tie4_Width,     # Number
        _Tie4P_ChannelLength	        = 30,       # Number
        _Tie4P_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT


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

    ''' Check Time'''
    elapsed_time = time.time() - start_time
    m, s = divmod(elapsed_time,60)
    h, m = divmod(m, 60)

    # print('###############      Sending to FTP Server...      ##################')
    # My = MyInfo.USER(DesignParameters._Technology)
    # Checker = DRCchecker_KJH0.DRCchecker_KJH0(
    #     username=My.ID,
    #     password=My.PW,
    #     WorkDir=My.Dir_Work,
    #     DRCrunDir=My.Dir_DRCrun,
    #     libname=libname,
    #     cellname=cellname,
    #     GDSDir=My.Dir_GDS
    # )
    # Checker.lib_deletion()
    # #Checker.cell_deletion()
    # Checker.Upload2FTP()
    # Checker.StreamIn(tech=DesignParameters._Technology)
    # #Checker_KJH0.DRCchecker()


    print ('#############################      Finished      ################################')
    print('{} Hours   {} minutes   {} seconds'.format(h, m, s))

# end of 'main():' ---------------------------------------------------------------------------------------------