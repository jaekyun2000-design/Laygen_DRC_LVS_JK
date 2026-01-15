## Import Basic Modules
## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_ADC.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC
# from KJH91_Projects.Project_ADC.Library_and_Engine import DRCv2

## Library
import copy
import math
import numpy as np
import time

## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.H00_CDAC_v2_Fixed import H00_05_CommonCentroid
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.H01_CDAC_Driver_v2_YJH_RCHybrid_Fixed import H01_01_DriverArray_CommonCentroid
from KJH91_Projects.Project_ADC.Layoutgen_code.H01_CDAC_Driver_v2_YJH_RCHybrid_Fixed import H01_01_DriverArray_Arranged


############################################################################################################################################################ Class_HEADER
class _CDACWtDriver(StickDiagram_KJH1._StickDiagram_KJH):
    ##########################################################################################################################
    # Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(
_NumOfBits = 3,
## CDAC
    #CDAC Drv
        ## Unit DRv
            ## Common
                # XVT
            _CDACDrv_XVT = 'SLVT',
            ## NMOS
            _CDACDrv_NMOS_NumberofGate=1,  # Number
            _CDACDrv_NMOS_ChannelWidth = 145, #Number
            _CDACDrv_NMOS_ChannelLength = 30, #Number
            ## PMOS
            _CDACDrv_PMOS_NumberofGate=1,  # Number
            _CDACDrv_PMOS_ChannelWidth = 879, #Number
            _CDACDrv_PMOS_ChannelLength = 30, #Number
    ## CDAC
        ## Element CDAC
        _CDAC_LayoutOption=[3],  # Vector, Consecutive Number [3,4,5]
        _CDAC_MetalWidth=50,  # Number
        _CDAC_MetalLength=1410,  # Number (8bit size: 1414/ 10bit size: 2800/ 12bit size: 4200)
        _CDAC_MetalSpacing=50,  # Number

        ## Unit Cap
        _CDAC_NumOfElement=1,  # Number

        ## Shield
        _CDAC_ShieldingLayer=1,  # Poly:0, M1:1, M2:2 ...
        _CDAC_ConnectLength=411,  # Number
        _CDAC_ExtendLength=400,  # Number

        ## Dummy Cap Option
        _CDAC_NumOfDummyCaps=3,  # Number, Number of dummy cap(one side)
        _CDAC_DummyCap_TopBottomShort=None,  # True => Top - Bottom Short, False -> Bottom = GND, None => Floating Bottom Node

        ## CommonCentroid With Driving node
        _CDAC_CapArrayWDrivingNodeDistance=1611,  # Number
        _CDAC_DriveNodeDistance=279,  # Number
        _CDAC_YWidth_Bottom_Hrz=55,  # Number
        _CDAC_BotNodeVtcExtensionMetalLayer=1,

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
_NumOfBits = 3,
## CDAC
    #CDAC Drv
        ## Unit DRv
            ## Common
                # XVT
            _CDACDrv_XVT = 'SLVT',
            ## NMOS
            _CDACDrv_NMOS_NumberofGate=1,  # Number
            _CDACDrv_NMOS_ChannelWidth = 145, #Number
            _CDACDrv_NMOS_ChannelLength = 30, #Number
            ## PMOS
            _CDACDrv_PMOS_NumberofGate=1,  # Number
            _CDACDrv_PMOS_ChannelWidth = 879, #Number
            _CDACDrv_PMOS_ChannelLength = 30, #Number
    ## CDAC
        ## Element CDAC
        _CDAC_LayoutOption=[3],  # Vector, Consecutive Number [3,4,5]
        _CDAC_MetalWidth=50,  # Number
        _CDAC_MetalLength=1410,  # Number (8bit size: 1414/ 10bit size: 2800/ 12bit size: 4200)
        _CDAC_MetalSpacing=50,  # Number

        ## Unit Cap
        _CDAC_NumOfElement=1,  # Number

        ## Shield
        _CDAC_ShieldingLayer=1,  # Poly:0, M1:1, M2:2 ...
        _CDAC_ConnectLength=411,  # Number
        _CDAC_ExtendLength=400,  # Number

        ## Dummy Cap Option
        _CDAC_NumOfDummyCaps=3,  # Number, Number of dummy cap(one side)
        _CDAC_DummyCap_TopBottomShort=None,  # True => Top - Bottom Short, False -> Bottom = GND, None => Floating Bottom Node

        ## CommonCentroid With Driving node
        _CDAC_CapArrayWDrivingNodeDistance=1611,  # Number
        _CDAC_DriveNodeDistance=279,  # Number
        _CDAC_YWidth_Bottom_Hrz=55,  # Number
        _CDAC_BotNodeVtcExtensionMetalLayer=1,

                                  ):


        ## Class_HEADER: Pre Defined Parameter Before Calculation
        ## Load DRC library
        _DRCObj = DRC.DRC()
        ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']
        ## CALCULATION START
        CDACWtDriver_start_time = time.time()
        print('##############################################')
        print('##    CDAC With Driver Calculation_Start    ##')
        print('##############################################')
        ###################################################################################################################

        ## H01_00_DriverCell (SREF) Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters0 = copy.deepcopy(H01_01_DriverArray_CommonCentroid._DriverArray._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters0['_NumOfBits'] = _NumOfBits

        _Caculation_Parameters0['_CDACDrv_XVT'] = _CDACDrv_XVT

        _Caculation_Parameters0['_CDACDrv_NMOS_NumberofGate'] = _CDACDrv_NMOS_NumberofGate
        _Caculation_Parameters0['_CDACDrv_NMOS_ChannelWidth'] = _CDACDrv_NMOS_ChannelWidth
        _Caculation_Parameters0['_CDACDrv_NMOS_ChannelLength'] = _CDACDrv_NMOS_ChannelLength

        _Caculation_Parameters0['_CDACDrv_PMOS_NumberofGate'] = _CDACDrv_PMOS_NumberofGate
        _Caculation_Parameters0['_CDACDrv_PMOS_ChannelWidth'] = _CDACDrv_PMOS_ChannelWidth
        _Caculation_Parameters0['_CDACDrv_PMOS_ChannelLength'] = _CDACDrv_PMOS_ChannelLength


        self._DesignParameter['SRF_DriverArray'] = self._SrefElementDeclaration(_DesignObj=H01_01_DriverArray_CommonCentroid._DriverArray(_DesignParameter=None,_Name='{}:SRF_DriverArray'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_DriverArray']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DriverArray']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DriverArray']['_DesignObj']._CalculateDesignParameter( **_Caculation_Parameters0)

        ## initialize Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DriverArray']['_XYCoordinates'] = [[0, 0]]

        ###################################################################################################################
        # Pre-defined Design Value
        DriverOutputM4VtcPathWidth = 50

        ## SRF Capacitor Array Generation
        _Caculation_Parameters0 = copy.deepcopy(H00_05_CommonCentroid._CommonCentroid._ParametersForDesignCalculation)
        _Caculation_Parameters0['_Bitsize'] =_NumOfBits

        _Caculation_Parameters0['_LayoutOption'] =_CDAC_LayoutOption
        _Caculation_Parameters0['_MetalWidth'] =_CDAC_MetalWidth
        _Caculation_Parameters0['_MetalLength'] =_CDAC_MetalLength
        _Caculation_Parameters0['_MetalSpacing'] =_CDAC_MetalSpacing

        _Caculation_Parameters0['_NumOfElement'] =_CDAC_NumOfElement

        _Caculation_Parameters0['_ShieldingLayer'] =_CDAC_ShieldingLayer
        _Caculation_Parameters0['_ConnectLength'] =_CDAC_ConnectLength
        _Caculation_Parameters0['_ExtendLength'] =_CDAC_ExtendLength

        _Caculation_Parameters0['_NumOfDummyCaps'] =_CDAC_NumOfDummyCaps
        _Caculation_Parameters0['_DummyCap_TopBottomShort'] =_CDAC_DummyCap_TopBottomShort

        _Caculation_Parameters0['_CapArrayWDrivingNodeDistance'] =_CDAC_CapArrayWDrivingNodeDistance
        _Caculation_Parameters0['_DriveNodeDistance'] =_CDAC_DriveNodeDistance
        _Caculation_Parameters0['_YWidth_Bottom_Hrz'] = _CDAC_YWidth_Bottom_Hrz
        _Caculation_Parameters0['_BotNodeVtcExtensionMetalLayer'] = _CDAC_BotNodeVtcExtensionMetalLayer

        self._DesignParameter['SRF_CapArray'] = self._SrefElementDeclaration(_DesignObj=H00_05_CommonCentroid._CommonCentroid(_DesignParameter=None,_Name='{}:SRF_CapArray'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_CapArray']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CapArray']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CapArray']['_DesignObj']._CalculateDesignParameterFold1(**_Caculation_Parameters0)

        ## initialize Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CapArray']['_XYCoordinates'] = [[0, 0]]

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_DriverArray', 'SRF_PMOS_Body_Contact', 'SRF_NbodyContactPhyLen', 'BND_Nwell')
        tmp2 = self.get_param_KJH4('SRF_DriverArray', 'SRF_{}C_DriverCell'.format(1), 'BND_Output_Node_Hrz_M4')
        target_coord = [int(tmp2[0][0][0][0]['_XY_right'][0] - DriverOutputM4VtcPathWidth/2), tmp1[0][0][0][0][0]['_XY_up'][1]]

        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_CapArray', 'BND_B{}_BotExten_VTC'.format(0))
        tmp3 = self.get_param_KJH4('SRF_CapArray', 'BND_DummyUCAP_Bot_Hrz')
        approaching_coord = [tmp2[0][0][0]['_XY_cent'][0], tmp3[0][0][0]['_XY_down'][1]]
        if _CDAC_NumOfElement > 1:
            approaching_coord[0] = int((tmp2[0][0][0]['_XY_left'][0] + tmp2[0][-1][0]['_XY_right'][0])/2)

        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CapArray')
        Scoord = tmp3[0][0]['_XY_origin']
        SpaceBtwCapNDriver = 100
        Scoord[1] = Scoord[1] + SpaceBtwCapNDriver

        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define Coordinates
        self._DesignParameter['SRF_CapArray']['_XYCoordinates'] = tmpXY

        ###################################################################################################################

        ### Cap <-> Driver Routing
        ## Driver Output (Drain) Node Vertical Path (M4)
        for j in range(_NumOfBits):
            CapSize = 2 ** (_NumOfBits - j - 1)
            self._DesignParameter['BND_{}C_Driver_Drain_Vtc_M4'.format(CapSize)] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL4'][0],
                _Datatype=DesignParameters._LayerMapping['METAL4'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )
            tmp1_1 = self.get_param_KJH4('SRF_CapArray', 'BND_B{}_Bottom_Hrz'.format(_NumOfBits - j - 1))
            tmp1_2 = self.get_param_KJH4('SRF_DriverArray', 'SRF_{}C_DriverCell'.format(CapSize), 'BND_Output_Node_Hrz_M4')
            self._DesignParameter['BND_{}C_Driver_Drain_Vtc_M4'.format(CapSize)]['_YWidth'] = abs(
                tmp1_1[0][0][0]['_XY_up'][1] - tmp1_2[0][0][0][0]['_XY_down'][1])

            ## Define Boundary_element _XWidth
            self._DesignParameter['BND_{}C_Driver_Drain_Vtc_M4'.format(CapSize)]['_XWidth'] = DriverOutputM4VtcPathWidth

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_{}C_Driver_Drain_Vtc_M4'.format(CapSize)]['_XYCoordinates'] = [[0, 0]]

            ## Calculate
            tmpXY = []
            for i in range(CapSize):
                ## Target_coord: _XY_type1
                target_coord = tmp1_2[0][i][0][0]['_XY_down_right']

                ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('BND_{}C_Driver_Drain_Vtc_M4'.format(CapSize))
                approaching_coord = tmp2[0][0]['_XY_down_right']

                ## Sref coord
                Scoord = tmp2[0][0]['_XY_origin']

                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)

            ## Define coordinates
            self._DesignParameter['BND_{}C_Driver_Drain_Vtc_M4'.format(CapSize)]['_XYCoordinates'] = tmpXY
        ###################################################################################################################

            # Driver Output Node Viastack M2M3 generation
            ## ViaM1M2 (PMOS Array Vtc Path M1 <-> Gate Hrz Path M2)
            ## Sref generation: ViaX
            ## Define ViaX Parameter
            _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
            _Caculation_Parameters['_Layer1'] = 3
            _Caculation_Parameters['_Layer2'] = 4
            _Caculation_Parameters['_COX'] = 2
            _Caculation_Parameters['_COY'] = 1

            self._DesignParameter['SRF_{}C_Driver_OutputNode_ViaM3M4'.format(CapSize)] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                                                                                                                             _Name='{}:SRF_{}C_Driver_OutputNode_ViaM3M4'.format(
                                                                                                                                                                 _Name, CapSize)))[0]

            ## Define Sref Relection
            self._DesignParameter['SRF_{}C_Driver_OutputNode_ViaM3M4'.format(CapSize)]['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
            self._DesignParameter['SRF_{}C_Driver_OutputNode_ViaM3M4'.format(CapSize)]['_Angle'] = 0

            self._DesignParameter['SRF_{}C_Driver_OutputNode_ViaM3M4'.format(CapSize)]['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            tmpXY = []
            for i in range(CapSize):
                ## Calculate Sref XYcoord
                ## initialized Sref coordinate
                self._DesignParameter['SRF_{}C_Driver_OutputNode_ViaM3M4'.format(CapSize)]['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                ## Target_coord
                tmp1 = self.get_param_KJH4('BND_{}C_Driver_Drain_Vtc_M4'.format(CapSize))
                target_coord = tmp1[i][0]['_XY_up']

                ## Approaching_coord
                tmp2 = self.get_param_KJH4('SRF_{}C_Driver_OutputNode_ViaM3M4'.format(CapSize), 'SRF_ViaM3M4',
                                           'BND_Met4Layer')
                approaching_coord = tmp2[0][0][0][0]['_XY_up']

                ## Sref coord
                tmp3 = self.get_param_KJH4('SRF_{}C_Driver_OutputNode_ViaM3M4'.format(CapSize))
                Scoord = tmp3[0][0]['_XY_origin']

                ## Calculate
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)

            ## Define
            self._DesignParameter['SRF_{}C_Driver_OutputNode_ViaM3M4'.format(CapSize)]['_XYCoordinates'] = tmpXY
        ###################################################################################################################

            ## Cap Array Bottom node
            ## Boundary Elemenet generation
            for i in range(_NumOfBits):
                CapSize = 2 ** (_NumOfBits - 1 - i)
                self._DesignParameter['BND_{}C_BottomNode_Hrz_M3'.format(CapSize)] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['METAL3'][0],
                    _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                    _XWidth=None,
                    _YWidth=None,
                    _XYCoordinates=[],
                )

                ## Define Boundary_element _YWidth
                tmp1 = self.get_param_KJH4('SRF_CapArray', 'BND_B{}_Bottom_Hrz'.format(_NumOfBits - i - 1))
                self._DesignParameter['BND_{}C_BottomNode_Hrz_M3'.format(CapSize)]['_YWidth'] = tmp1[0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
                tmp2 = self.get_param_KJH4('SRF_DriverArray', 'SRF_{}C_DriverCell'.format(CapSize),
                                           'BND_Output_Node_Hrz_M4')
                CapArrayXlength = tmp1[0][0][0]['_Xwidth']
                DriverArrayXlength = abs(tmp2[0][0][0][0]['_XY_right'][0] - tmp2[0][-1][0][0]['_XY_right'][0])
                self._DesignParameter['BND_{}C_BottomNode_Hrz_M3'.format(CapSize)]['_XWidth'] = max(DriverArrayXlength, CapArrayXlength)  # + DriverOutputM4VtcPathWidth

                ## Calculate Sref XYcoord
                tmpXY = []
                ## initialized Sref coordinate
                self._DesignParameter['BND_{}C_BottomNode_Hrz_M3'.format(CapSize)]['_XYCoordinates'] = [[0, 0]]

                ## Calculate
                ## Target_coord: _XY_type1
                tmp1 = self.get_param_KJH4('SRF_CapArray', 'BND_B{}_Bottom_Hrz'.format(_NumOfBits - i - 1))
                target_coord = tmp1[0][0][0]['_XY_cent']

                ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('BND_{}C_BottomNode_Hrz_M3'.format(CapSize))
                approaching_coord = tmp2[0][0]['_XY_cent']

                ## Sref coord
                Scoord = tmp2[0][0]['_XY_origin']

                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)

                ## Define coordinates
                self._DesignParameter['BND_{}C_BottomNode_Hrz_M3'.format(CapSize)]['_XYCoordinates'] = tmpXY
        ###################################################################################################################

        ## Dummy Driver Cell <-> Cap Routing
        ## Boundary Element Generation
        self._DesignParameter['BND_Dummy_Driver_Drain_Vtc_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        tmp1_1 = self.get_param_KJH4('SRF_CapArray', 'BND_DummyUCAP_Bot_Hrz')
        tmp1_2 = self.get_param_KJH4('SRF_DriverArray', 'SRF_Dummy_DriverCell', 'BND_Output_Node_Hrz_M4')
        self._DesignParameter['BND_Dummy_Driver_Drain_Vtc_M4']['_YWidth'] = abs(
            tmp1_1[0][0][0]['_XY_up'][1] - tmp1_2[0][0][0][0]['_XY_down'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Dummy_Driver_Drain_Vtc_M4']['_XWidth'] = DriverOutputM4VtcPathWidth

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Dummy_Driver_Drain_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        ## Target_coord: _XY_type1
        target_coord = tmp1_2[0][0][0][0]['_XY_down_right']

        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Dummy_Driver_Drain_Vtc_M4')
        approaching_coord = tmp2[0][0]['_XY_down_right']

        ## Sref coord
        Scoord = tmp2[0][0]['_XY_origin']

        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define coordinates
        self._DesignParameter['BND_Dummy_Driver_Drain_Vtc_M4']['_XYCoordinates'] = tmpXY
        ###################################################################################################################

        # Dummy Driver Cell Output Node Viastack M4M5 generation
        ## ViaM1M2 (PMOS Array Vtc Path M1 <-> Gate Hrz Path M2)
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        self._DesignParameter['SRF_Dummy_Driver_OutputNode_ViaM3M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,_Name='{}:SRF_Dummy_Driver_OutputNode_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_Dummy_Driver_OutputNode_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_Dummy_Driver_OutputNode_ViaM3M4']['_Angle'] = 0

        self._DesignParameter['SRF_Dummy_Driver_OutputNode_ViaM3M4']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        tmpXY = []
        ## Calculate Sref XYcoord
        ## initialized Sref coordinate
        self._DesignParameter['SRF_Dummy_Driver_OutputNode_ViaM3M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_Dummy_Driver_Drain_Vtc_M4')
        target_coord = tmp1[0][0]['_XY_up_right']

        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Dummy_Driver_OutputNode_ViaM3M4', 'SRF_ViaM3M4','BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_right']

        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Dummy_Driver_OutputNode_ViaM3M4')
        Scoord = tmp3[0][0]['_XY_origin']

        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define
        self._DesignParameter['SRF_Dummy_Driver_OutputNode_ViaM3M4']['_XYCoordinates'] = tmpXY
        ###################################################################################################################

        ## Dummy Cap Bottom node
        ## Boundary Elemenet generation
        self._DesignParameter['BND_DummyUCAP_BottomNode_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CapArray', 'BND_B{}_Bottom_Hrz'.format(_NumOfBits - 1))
        self._DesignParameter['BND_DummyUCAP_BottomNode_Hrz_M3']['_YWidth'] = tmp1[0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH4('BND_Dummy_Driver_Drain_Vtc_M4')
        tmp3 = self.get_param_KJH4('SRF_CapArray', 'BND_DummyUCAP_BotExten_VTC')
        self._DesignParameter['BND_DummyUCAP_BottomNode_Hrz_M3']['_XWidth'] = tmp3[0][0][0]['_XY_right'][0] - tmp2[0][0]['_XY_left'][0]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_DummyUCAP_BottomNode_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp2[0][0]['_XY_up_left']

        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_DummyUCAP_BottomNode_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_up_left']

        ## Sref coord
        Scoord = tmp2[0][0]['_XY_origin']

        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define coordinates
        self._DesignParameter['BND_DummyUCAP_BottomNode_Hrz_M3']['_XYCoordinates'] = tmpXY
        ###################################################################################################################
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')
        CDACWtDriver_end_time = time.time()
        self.CDACWtDriver_elapsed_time = CDACWtDriver_end_time - CDACWtDriver_start_time
        ###################################################################################################################
############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ZZ01_H02_00_CDACWtDriver_Unfold_CommonCent'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'H02_00_CDACWDriver_RCHybrid'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
_NumOfBits = 4,
## CDAC
    #CDAC Drv
        ## Unit DRv
            ## Common
                # XVT
            _CDACDrv_XVT = 'SLVT',
            ## NMOS
            _CDACDrv_NMOS_NumberofGate=5,  # Number
            _CDACDrv_NMOS_ChannelWidth = 145, #Number
            _CDACDrv_NMOS_ChannelLength = 30, #Number
            ## PMOS
            _CDACDrv_PMOS_NumberofGate=2,  # Number
            _CDACDrv_PMOS_ChannelWidth = 879, #Number
            _CDACDrv_PMOS_ChannelLength = 30, #Number
    ## CDAC
        ## Element CDAC
        _CDAC_LayoutOption=[3],  # Vector, Consecutive Number [3,4,5]
        _CDAC_MetalWidth=50,  # Number
        _CDAC_MetalLength=1410,  # Number (8bit size: 1414/ 10bit size: 2800/ 12bit size: 4200)
        _CDAC_MetalSpacing=50,  # Number

        ## Unit Cap
        _CDAC_NumOfElement=1,  # Number

        ## Shield
        _CDAC_ShieldingLayer=1,  # Poly:0, M1:1, M2:2 ...
        _CDAC_ConnectLength=411,  # Number
        _CDAC_ExtendLength=400,  # Number

        ## Dummy Cap Option
        _CDAC_NumOfDummyCaps=3,  # Number, Number of dummy cap(one side)
        _CDAC_DummyCap_TopBottomShort=None,  # True => Top - Bottom Short, False -> Bottom = GND, None => Floating Bottom Node

        ## CommonCentroid With Driving node
        _CDAC_CapArrayWDrivingNodeDistance=1611,  # Number
        _CDAC_DriveNodeDistance=279,  # Number
        _CDAC_YWidth_Bottom_Hrz=60,  # Number
        _CDAC_BotNodeVtcExtensionMetalLayer=1,
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
    LayoutObj = _CDACWtDriver(_DesignParameter=None, _Name=cellname)

    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    ''' Check Time'''
    elapsed_time = time.time() - start_time
    m, s = divmod(elapsed_time, 60)
    h, m = divmod(m, 60)

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
    Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()

    print('#############################      Finished      ################################')
    print('{} Hours   {} minutes   {} seconds'.format(h, m, s))
# end of 'main():' ---------------------------------------------------------------------------------------------
