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
from KJH91_Projects.Project_ADC.Layoutgen_code.H00_CDAC_v2 import H00_05_CommonCentroid
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.H01_CDAC_Driver_v2_YJH import H01_01_DriverArray
from KJH91_Projects.Project_ADC.Layoutgen_code.H01_CDAC_Driver_v2_YJH import H01_01_DriverArray_Arranged



############################################################################################################################################################ Class_HEADER
class _CDACWtDriver(StickDiagram_KJH1._StickDiagram_KJH):
    ##########################################################################################################################
    # Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(
        # # CommonCentroid Array
        _NumOfBits=None,

        # # Element CDAC
        _CDAC_LayoutOption=None,
        _CDAC_ShieldingLayer=None,
        _CDAC_BotNodeVtcExtensionMetalLayer=None,
        # Poly:0, M1:1, M2:2 ...
        _CDAC_MetalWidth=None,
        _CDAC_MetalLength=None,
        _CDAC_MetalSpacing=None,

        # #Unit Cap
        _CDAC_NumOfElement=None,

        # # Shielding & Top Connect node
        _CDAC_ConnectLength=None,
        _CDAC_ExtendLength=None,

        # # Dummy Cap Option
        _CDAC_DummyCap_TopBottomShort=None,
        _CDAC_NumOfDummyCaps=None,  # Number of dummy cap(one side)

        # # CommonCentroid With Driving node
        _CDAC_CapArrayWDrivingNodeDistance=0,  # DRC Rule
        _CDAC_DriveNodeDistance=None,  #
        _CDAC_YWidth_Bottom_Hrz=None,

        # Driver(Inverter) Sizing Option
        _Driver_SizeByBit=None,

        # Driver(Inverter) NMOS
        _Driver_NMOS_NumberofGate = None,  # number
        _Driver_NMOS_ChannelWidth = None,  # number
        _Driver_NMOS_Channellength = None,  # number
        _Driver_NMOS_GateSpacing = None,  # None/number
        _Driver_NMOS_SDWidth = None,  # None/number
        _Driver_NMOS_XVT = 'SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Driver_NMOS_PCCrit = None,  # None/True

            # Source_node_ViaM1M2
        _Driver_NMOS_Source_Via_TF = None,  # True/False

            # Drain_node_ViaM1M2
        _Driver_NMOS_Drain_Via_TF = None,  # True/False

            # POLY dummy setting
        _Driver_NMOS_Dummy = True,  # TF
            # if _PMOSDummy == True
        _Driver_NMOS_Dummy_length = None,  # None/Value
        _Driver_NMOS_Dummy_placement = None,  # None/'Up'/'Dn'/

        # Driver(Inverter) PMOS
        _Driver_PMOS_NumberofGate=None,  # number
        _Driver_PMOS_ChannelWidth=None,  # number
        _Driver_PMOS_Channellength=None,  # number
        _Driver_PMOS_GateSpacing=None,  # None/number
        _Driver_PMOS_SDWidth=None,  # None/number
        _Driver_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Driver_PMOS_PCCrit=None,  # None/True

        # Source_node_ViaM1M2
        _Driver_PMOS_Source_Via_TF=None,  # True/False

        # Drain_node_ViaM1M2
        _Driver_PMOS_Drain_Via_TF=None,  # True/False

        # POLY dummy setting
        _Driver_PMOS_Dummy=True,  # TF
        # if _PMOSDummy == True
        _Driver_PMOS_Dummy_length=None,  # None/Value
        _Driver_PMOS_Dummy_placement=None,  # None/'Up'/'Dn'/
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
                                  # # CommonCentroid Array
                                  _NumOfBits=None,

                                  # # Element CDAC
                                  _CDAC_LayoutOption=None,
                                  _CDAC_ShieldingLayer=None,  # Poly:0, M1:1, M2:2 ...
                                  _CDAC_BotNodeVtcExtensionMetalLayer=None,
                                  _CDAC_MetalWidth=None,
                                  _CDAC_MetalLength=None,
                                  _CDAC_MetalSpacing=None,

                                  # #Unit Cap
                                  _CDAC_NumOfElement=None,

                                  # # Shielding & Top Connect node
                                  _CDAC_ConnectLength=None,
                                  _CDAC_ExtendLength=None,

                                  # # Dummy Cap Option
                                  _CDAC_DummyCap_TopBottomShort=None,
                                  _CDAC_NumOfDummyCaps=None,  # Number of dummy cap(one side)

                                  # # CommonCentroid With Driving node
                                  _CDAC_CapArrayWDrivingNodeDistance=0,  # DRC Rule
                                  _CDAC_DriveNodeDistance=None,  #
                                  _CDAC_YWidth_Bottom_Hrz=None,

                                  # Driver(Inverter) Sizing Option
                                  _Driver_SizeByBit=None,

                                  # Driver(Inverter) NMOS
                                  _Driver_NMOS_NumberofGate=None,  # number
                                  _Driver_NMOS_ChannelWidth=None,  # number
                                  _Driver_NMOS_Channellength=None,  # number
                                  _Driver_NMOS_GateSpacing=None,  # None/number
                                  _Driver_NMOS_SDWidth=None,  # None/number
                                  _Driver_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Driver_NMOS_PCCrit=None,  # None/True

                                  # Source_node_ViaM1M2
                                  _Driver_NMOS_Source_Via_TF=None,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Driver_NMOS_Drain_Via_TF=None,  # True/False

                                  # POLY dummy setting
                                  _Driver_NMOS_Dummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Driver_NMOS_Dummy_length=None,  # None/Value
                                  _Driver_NMOS_Dummy_placement=None,  # None/'Up'/'Dn'/

                                  # Driver(Inverter) PMOS
                                  _Driver_PMOS_NumberofGate=None,  # number
                                  _Driver_PMOS_ChannelWidth=None,  # number
                                  _Driver_PMOS_Channellength=None,  # number
                                  _Driver_PMOS_GateSpacing=None,  # None/number
                                  _Driver_PMOS_SDWidth=None,  # None/number
                                  _Driver_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Driver_PMOS_PCCrit=None,  # None/True

                                  # Source_node_ViaM1M2
                                  _Driver_PMOS_Source_Via_TF=None,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Driver_PMOS_Drain_Via_TF=None,  # True/False

                                  # POLY dummy setting
                                  _Driver_PMOS_Dummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Driver_PMOS_Dummy_length=None,  # None/Value
                                  _Driver_PMOS_Dummy_placement=None,  # None/'Up'/'Dn'/
                                  ):


        ## Class_HEADER: Pre Defined Parameter Before Calculation
        ## Load DRC library
        _DRCObj = DRC.DRC()
        ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']
        ## CALCULATION START
        print('##############################################')
        print('##    CDAC With Driver Calculation_Start    ##')
        print('##############################################')

        # Pre-defined Design Value
        DriverOutputM4VtcPathWidth = 50


        ## H01_00_DriverCell (SREF) Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters0 = copy.deepcopy(H01_01_DriverArray._DriverArray._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters0['_NumOfBits'] = _NumOfBits
        _Caculation_Parameters0['_Driver_NMOS_NumberofGate'] = _Driver_NMOS_NumberofGate
        _Caculation_Parameters0['_Driver_NMOS_ChannelWidth'] =_Driver_NMOS_ChannelWidth
        _Caculation_Parameters0['_Driver_NMOS_Channellength'] =_Driver_NMOS_Channellength
        _Caculation_Parameters0['_Driver_NMOS_GateSpacing'] =_Driver_NMOS_GateSpacing
        _Caculation_Parameters0['_Driver_NMOS_SDWidth'] =_Driver_NMOS_SDWidth
        _Caculation_Parameters0['_Driver_NMOS_XVT'] =_Driver_NMOS_XVT
        _Caculation_Parameters0['_Driver_NMOS_PCCrit'] =_Driver_NMOS_PCCrit
        _Caculation_Parameters0['_Driver_NMOS_Source_Via_TF'] =True #default
        _Caculation_Parameters0['_Driver_NMOS_Drain_Via_TF'] =True
        _Caculation_Parameters0['_Driver_NMOS_Dummy'] = True #default
        _Caculation_Parameters0['_Driver_NMOS_Dummy_length'] =_Driver_NMOS_Dummy_length
        _Caculation_Parameters0['_Driver_NMOS_Dummy_placement'] =_Driver_NMOS_Dummy_length
        _Caculation_Parameters0['_Driver_PMOS_NumberofGate'] = _Driver_PMOS_NumberofGate
        _Caculation_Parameters0['_Driver_PMOS_ChannelWidth'] =_Driver_PMOS_ChannelWidth
        _Caculation_Parameters0['_Driver_PMOS_Channellength'] =_Driver_PMOS_Channellength
        _Caculation_Parameters0['_Driver_PMOS_GateSpacing'] =_Driver_PMOS_GateSpacing
        _Caculation_Parameters0['_Driver_PMOS_SDWidth'] =_Driver_PMOS_SDWidth
        _Caculation_Parameters0['_Driver_PMOS_XVT'] =_Driver_PMOS_XVT
        _Caculation_Parameters0['_Driver_PMOS_PCCrit'] =_Driver_PMOS_PCCrit
        _Caculation_Parameters0['_Driver_PMOS_Source_Via_TF'] =True #default
        _Caculation_Parameters0['_Driver_PMOS_Drain_Via_TF'] =True
        _Caculation_Parameters0['_Driver_PMOS_Dummy'] = True #default
        _Caculation_Parameters0['_Driver_PMOS_Dummy_length'] =_Driver_PMOS_Dummy_length
        _Caculation_Parameters0['_Driver_PMOS_Dummy_placement'] =_Driver_PMOS_Dummy_placement

        self._DesignParameter['SRF_DriverArray'] = self._SrefElementDeclaration(
            _DesignObj=H01_01_DriverArray._DriverArray(_DesignParameter=None,
                                                     _Name='{}:SRF_DriverArray'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_DriverArray']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DriverArray']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DriverArray']['_DesignObj']._CalculateDesignParameter(
            **_Caculation_Parameters0)

        ## initialize Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DriverArray']['_XYCoordinates'] = [[0, 0]]


        ## SRF Capacitor Array Generation
        _Caculation_Parameters0 = copy.deepcopy(H00_05_CommonCentroid._CommonCentroid._ParametersForDesignCalculation)
        _Caculation_Parameters0['_LayoutOption'] =_CDAC_LayoutOption
        _Caculation_Parameters0['_ShieldingLayer'] =_CDAC_ShieldingLayer
        _Caculation_Parameters0['_BotNodeVtcExtensionMetalLayer'] =_CDAC_BotNodeVtcExtensionMetalLayer
        _Caculation_Parameters0['_MetalWidth'] =_CDAC_MetalWidth
        _Caculation_Parameters0['_MetalLength'] =_CDAC_MetalLength
        _Caculation_Parameters0['_MetalSpacing'] =_CDAC_MetalSpacing
        _Caculation_Parameters0['_NumOfElement'] =_CDAC_NumOfElement
        _Caculation_Parameters0['_ConnectLength'] =_CDAC_ConnectLength
        _Caculation_Parameters0['_ExtendLength'] =_CDAC_ExtendLength
        _Caculation_Parameters0['_Bitsize'] =_NumOfBits
        _Caculation_Parameters0['_CapArrayWDrivingNodeDistance'] =_CDAC_CapArrayWDrivingNodeDistance
        _Caculation_Parameters0['_DriveNodeDistance'] =_CDAC_DriveNodeDistance
        _Caculation_Parameters0['_YWidth_Bottom_Hrz'] =_CDAC_YWidth_Bottom_Hrz
        _Caculation_Parameters0['_DummyCap_TopBottomShort'] = _CDAC_DummyCap_TopBottomShort
        _Caculation_Parameters0['_NumOfDummyCaps'] = _CDAC_NumOfDummyCaps

        self._DesignParameter['SRF_CapArray'] = self._SrefElementDeclaration(
            _DesignObj=H00_05_CommonCentroid._CommonCentroid(_DesignParameter=None,
                                                     _Name='{}:SRF_CapArray'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_CapArray']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CapArray']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CapArray']['_DesignObj']._CalculateDesignParameterFold1(
            **_Caculation_Parameters0)

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
                self._DesignParameter['BND_{}C_BottomNode_Hrz_M3'.format(CapSize)]['_XWidth'] = max(DriverArrayXlength, CapArrayXlength) # + DriverOutputM4VtcPathWidth

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

                # Dummy Driver Cell Output Node Viastack M4M5 generation
                ## ViaM1M2 (PMOS Array Vtc Path M1 <-> Gate Hrz Path M2)
                ## Sref generation: ViaX
                ## Define ViaX Parameter
                _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
                _Caculation_Parameters['_Layer1'] = 3
                _Caculation_Parameters['_Layer2'] = 4
                _Caculation_Parameters['_COX'] = 2
                _Caculation_Parameters['_COY'] = 1

                self._DesignParameter['SRF_Dummy_Driver_OutputNode_ViaM3M4'] = \
                    self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                                                        _Name='{}:SRF_Dummy_Driver_OutputNode_ViaM3M4'.format(
                                                                                            _Name)))[0]
                ## Define Sref Relection
                self._DesignParameter['SRF_Dummy_Driver_OutputNode_ViaM3M4']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle
                self._DesignParameter['SRF_Dummy_Driver_OutputNode_ViaM3M4']['_Angle'] = 0

                self._DesignParameter['SRF_Dummy_Driver_OutputNode_ViaM3M4'][
                    '_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

                tmpXY = []
                ## Calculate Sref XYcoord
                ## initialized Sref coordinate
                self._DesignParameter['SRF_Dummy_Driver_OutputNode_ViaM3M4']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                ## Target_coord
                tmp1 = self.get_param_KJH4('BND_Dummy_Driver_Drain_Vtc_M4')
                target_coord = tmp1[0][0]['_XY_up_right']

                ## Approaching_coord
                tmp2 = self.get_param_KJH4('SRF_Dummy_Driver_OutputNode_ViaM3M4', 'SRF_ViaM3M4',
                                           'BND_Met4Layer')
                approaching_coord = tmp2[0][0][0][0]['_XY_up_right']

                ## Sref coord
                tmp3 = self.get_param_KJH4('SRF_Dummy_Driver_OutputNode_ViaM3M4')
                Scoord = tmp3[0][0]['_XY_origin']

                ## Calculate
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)

                ## Define
                self._DesignParameter['SRF_Dummy_Driver_OutputNode_ViaM3M4']['_XYCoordinates'] = tmpXY

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
                self._DesignParameter['BND_DummyUCAP_BottomNode_Hrz_M3']['_XWidth'] = tmp3[0][0][0]['_XY_right'][0] - \
                                                                                      tmp2[0][0]['_XY_left'][0]

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




    ##########################################################################################################################################################################
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
    # Folded CC Drv. 버전 : 좌측에 더미 CDAC Cell(Cap+Driver) 하나가 더 붙음.
    def _CalculateDesignParameterFold1(self,
                                       # # CommonCentroid Array
                                       _NumOfBits=None,

                                       # # Element CDAC
                                       _CDAC_LayoutOption=None,
                                       _CDAC_ShieldingLayer=None,  # Poly:0, M1:1, M2:2 ...
                                       _CDAC_BotNodeVtcExtensionMetalLayer=None,
                                       _CDAC_MetalWidth=None,
                                       _CDAC_MetalLength=None,
                                       _CDAC_MetalSpacing=None,

                                       # #Unit Cap
                                       _CDAC_NumOfElement=None,

                                       # # Shielding & Top Connect node
                                       _CDAC_ConnectLength=None,
                                       _CDAC_ExtendLength=None,

                                       # # Dummy Cap Option
                                       _CDAC_DummyCap_TopBottomShort=None,
                                       _CDAC_NumOfDummyCaps=None,  # Number of dummy cap(one side)

                                       # # CommonCentroid With Driving node
                                       _CDAC_CapArrayWDrivingNodeDistance=0,  # DRC Rule
                                       _CDAC_DriveNodeDistance=None,  #
                                       _CDAC_YWidth_Bottom_Hrz=None,

                                       # Driver(Inverter) Sizing Option
                                       _Driver_SizeByBit=None,

                                       # Driver(Inverter) NMOS
                                       _Driver_NMOS_NumberofGate=None,  # number
                                       _Driver_NMOS_ChannelWidth=None,  # number
                                       _Driver_NMOS_Channellength=None,  # number
                                       _Driver_NMOS_GateSpacing=None,  # None/number
                                       _Driver_NMOS_SDWidth=None,  # None/number
                                       _Driver_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                       _Driver_NMOS_PCCrit=None,  # None/True

                                       # Source_node_ViaM1M2
                                       _Driver_NMOS_Source_Via_TF=None,  # True/False

                                       # Drain_node_ViaM1M2
                                       _Driver_NMOS_Drain_Via_TF=None,  # True/False

                                       # POLY dummy setting
                                       _Driver_NMOS_Dummy=True,  # TF
                                       # if _PMOSDummy == True
                                       _Driver_NMOS_Dummy_length=None,  # None/Value
                                       _Driver_NMOS_Dummy_placement=None,  # None/'Up'/'Dn'/

                                       # Driver(Inverter) PMOS
                                       _Driver_PMOS_NumberofGate=None,  # number
                                       _Driver_PMOS_ChannelWidth=None,  # number
                                       _Driver_PMOS_Channellength=None,  # number
                                       _Driver_PMOS_GateSpacing=None,  # None/number
                                       _Driver_PMOS_SDWidth=None,  # None/number
                                       _Driver_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                       _Driver_PMOS_PCCrit=None,  # None/True

                                       # Source_node_ViaM1M2
                                       _Driver_PMOS_Source_Via_TF=None,  # True/False

                                       # Drain_node_ViaM1M2
                                       _Driver_PMOS_Drain_Via_TF=None,  # True/False

                                       # POLY dummy setting
                                       _Driver_PMOS_Dummy=True,  # TF
                                       # if _PMOSDummy == True
                                       _Driver_PMOS_Dummy_length=None,  # None/Value
                                       _Driver_PMOS_Dummy_placement=None,  # None/'Up'/'Dn'/
                                       ):

        ## Class_HEADER: Pre Defined Parameter Before Calculation
        ## Load DRC library
        _DRCObj = DRC.DRC()
        ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']
        ## CALCULATION START
        print('##############################################')
        print('##    CDAC With Driver Calculation_Start    ##')
        print('##############################################')

        # Pre-defined Design Value
        DriverOutputM4VtcPathWidth = 50


        ## H01_00_DriverCell (SREF) Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters0 = copy.deepcopy(H01_01_DriverArray._DriverArray._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters0['_NumOfBits'] = _NumOfBits
        _Caculation_Parameters0['_Driver_NMOS_NumberofGate'] = _Driver_NMOS_NumberofGate
        _Caculation_Parameters0['_Driver_NMOS_ChannelWidth'] =_Driver_NMOS_ChannelWidth
        _Caculation_Parameters0['_Driver_NMOS_Channellength'] =_Driver_NMOS_Channellength
        _Caculation_Parameters0['_Driver_NMOS_GateSpacing'] =_Driver_NMOS_GateSpacing
        _Caculation_Parameters0['_Driver_NMOS_SDWidth'] =_Driver_NMOS_SDWidth
        _Caculation_Parameters0['_Driver_NMOS_XVT'] =_Driver_NMOS_XVT
        _Caculation_Parameters0['_Driver_NMOS_PCCrit'] =_Driver_NMOS_PCCrit
        _Caculation_Parameters0['_Driver_NMOS_Source_Via_TF'] =True #default
        _Caculation_Parameters0['_Driver_NMOS_Drain_Via_TF'] =True
        _Caculation_Parameters0['_Driver_NMOS_Dummy'] = True #default
        _Caculation_Parameters0['_Driver_NMOS_Dummy_length'] =_Driver_NMOS_Dummy_length
        _Caculation_Parameters0['_Driver_NMOS_Dummy_placement'] =_Driver_NMOS_Dummy_length
        _Caculation_Parameters0['_Driver_PMOS_NumberofGate'] = _Driver_PMOS_NumberofGate
        _Caculation_Parameters0['_Driver_PMOS_ChannelWidth'] =_Driver_PMOS_ChannelWidth
        _Caculation_Parameters0['_Driver_PMOS_Channellength'] =_Driver_PMOS_Channellength
        _Caculation_Parameters0['_Driver_PMOS_GateSpacing'] =_Driver_PMOS_GateSpacing
        _Caculation_Parameters0['_Driver_PMOS_SDWidth'] =_Driver_PMOS_SDWidth
        _Caculation_Parameters0['_Driver_PMOS_XVT'] =_Driver_PMOS_XVT
        _Caculation_Parameters0['_Driver_PMOS_PCCrit'] =_Driver_PMOS_PCCrit
        _Caculation_Parameters0['_Driver_PMOS_Source_Via_TF'] =True #default
        _Caculation_Parameters0['_Driver_PMOS_Drain_Via_TF'] =True
        _Caculation_Parameters0['_Driver_PMOS_Dummy'] = True #default
        _Caculation_Parameters0['_Driver_PMOS_Dummy_length'] =_Driver_PMOS_Dummy_length
        _Caculation_Parameters0['_Driver_PMOS_Dummy_placement'] =_Driver_PMOS_Dummy_placement

        self._DesignParameter['SRF_DriverArray'] = self._SrefElementDeclaration(
            _DesignObj=H01_01_DriverArray._DriverArray(_DesignParameter=None,
                                                     _Name='{}:SRF_DriverArray'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_DriverArray']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DriverArray']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DriverArray']['_DesignObj']._CalculateDesignParameterFold1(
            **_Caculation_Parameters0)

        ## initialize Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DriverArray']['_XYCoordinates'] = [[0, 0]]


        ## SRF Capacitor Array Generation
        _Caculation_Parameters0 = copy.deepcopy(H00_05_CommonCentroid._CommonCentroid._ParametersForDesignCalculation)
        _Caculation_Parameters0['_LayoutOption'] =_CDAC_LayoutOption
        _Caculation_Parameters0['_ShieldingLayer'] =_CDAC_ShieldingLayer
        _Caculation_Parameters0['_BotNodeVtcExtensionMetalLayer'] =_CDAC_BotNodeVtcExtensionMetalLayer
        _Caculation_Parameters0['_MetalWidth'] =_CDAC_MetalWidth
        _Caculation_Parameters0['_MetalLength'] =_CDAC_MetalLength
        _Caculation_Parameters0['_MetalSpacing'] =_CDAC_MetalSpacing
        _Caculation_Parameters0['_NumOfElement'] =_CDAC_NumOfElement
        _Caculation_Parameters0['_ConnectLength'] =_CDAC_ConnectLength
        _Caculation_Parameters0['_ExtendLength'] =_CDAC_ExtendLength
        _Caculation_Parameters0['_Bitsize'] =_NumOfBits
        _Caculation_Parameters0['_CapArrayWDrivingNodeDistance'] =_CDAC_CapArrayWDrivingNodeDistance
        _Caculation_Parameters0['_DriveNodeDistance'] =_CDAC_DriveNodeDistance
        _Caculation_Parameters0['_YWidth_Bottom_Hrz'] =_CDAC_YWidth_Bottom_Hrz
        _Caculation_Parameters0['_DummyCap_TopBottomShort'] = _CDAC_DummyCap_TopBottomShort
        _Caculation_Parameters0['_NumOfDummyCaps'] = _CDAC_NumOfDummyCaps

        self._DesignParameter['SRF_CapArray'] = self._SrefElementDeclaration(
            _DesignObj=H00_05_CommonCentroid._CommonCentroid(_DesignParameter=None,
                                                     _Name='{}:SRF_CapArray'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_CapArray']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CapArray']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CapArray']['_DesignObj']._CalculateDesignParameterFold1(
            **_Caculation_Parameters0)

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


            # Driver Output Node Viastack M3M4 generation
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
                tmp2 = self.get_param_KJH4('SRF_DriverArray', 'SRF_{}C_DriverCell'.format(CapSize),'BND_Output_Node_Hrz_M4')
                CapArrayXlength = tmp1[0][0][0]['_Xwidth']
                DriverArrayXlength = abs(tmp2[0][0][0][0]['_XY_right'][0] - tmp2[0][-1][0][0]['_XY_right'][0])
                self._DesignParameter['BND_{}C_BottomNode_Hrz_M3'.format(CapSize)]['_XWidth'] = max(DriverArrayXlength, CapArrayXlength) # + DriverOutputM4VtcPathWidth

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


        # Dummy Driver Cell Output Node Viastack M3M4 generation
        ## ViaM1M2 (PMOS Array Vtc Path M1 <-> Gate Hrz Path M2)
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        self._DesignParameter['SRF_Dummy_Driver_OutputNode_ViaM3M4'] = \
        self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                                                 _Name='{}:SRF_Dummy_Driver_OutputNode_ViaM3M4'.format(
                                                                                     _Name)))[0]
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
        tmp2 = self.get_param_KJH4('SRF_Dummy_Driver_OutputNode_ViaM3M4', 'SRF_ViaM3M4',
                                   'BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_right']

        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Dummy_Driver_OutputNode_ViaM3M4')
        Scoord = tmp3[0][0]['_XY_origin']

        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define
        self._DesignParameter['SRF_Dummy_Driver_OutputNode_ViaM3M4']['_XYCoordinates'] = tmpXY


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


##########################################################################################################################################################################
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
    # CDAC Driver가 MSB부터 일렬로 정렬된 Folded 버전; 좌측에 더미 CDAC Cell(Cap+Driver) 하나가 더 붙음.
    def _CalculateDesignParameter_DrvArranged(self,
                                              # # CommonCentroid Array
                                              _NumOfBits=None,

                                              # # Element CDAC
                                              _CDAC_LayoutOption=None,
                                              _CDAC_ShieldingLayer=None,  # Poly:0, M1:1, M2:2 ...
                                              _CDAC_BotNodeVtcExtensionMetalLayer=None,
                                              _CDAC_MetalWidth=None,
                                              _CDAC_MetalLength=None,
                                              _CDAC_MetalSpacing=None,

                                              # #Unit Cap
                                              _CDAC_NumOfElement=None,

                                              # # Shielding & Top Connect node
                                              _CDAC_ConnectLength=None,
                                              _CDAC_ExtendLength=None,

                                              # # Dummy Cap Option
                                              _CDAC_DummyCap_TopBottomShort=None,
                                              _CDAC_NumOfDummyCaps=None,  # Number of dummy cap(one side)

                                              # # CommonCentroid With Driving node
                                              _CDAC_CapArrayWDrivingNodeDistance=0,  # DRC Rule
                                              _CDAC_DriveNodeDistance=None,  #
                                              _CDAC_YWidth_Bottom_Hrz=None,

                                              # Driver(Inverter) Sizing Option
                                              _Driver_SizeByBit=None,

                                              # Driver(Inverter) NMOS
                                              _Driver_NMOS_NumberofGate=None,  # number
                                              _Driver_NMOS_ChannelWidth=None,  # number
                                              _Driver_NMOS_Channellength=None,  # number
                                              _Driver_NMOS_GateSpacing=None,  # None/number
                                              _Driver_NMOS_SDWidth=None,  # None/number
                                              _Driver_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                              _Driver_NMOS_PCCrit=None,  # None/True

                                              # Source_node_ViaM1M2
                                              _Driver_NMOS_Source_Via_TF=None,  # True/False

                                              # Drain_node_ViaM1M2
                                              _Driver_NMOS_Drain_Via_TF=None,  # True/False

                                              # POLY dummy setting
                                              _Driver_NMOS_Dummy=True,  # TF
                                              # if _PMOSDummy == True
                                              _Driver_NMOS_Dummy_length=None,  # None/Value
                                              _Driver_NMOS_Dummy_placement=None,  # None/'Up'/'Dn'/

                                              # Driver(Inverter) PMOS
                                              _Driver_PMOS_NumberofGate=None,  # number
                                              _Driver_PMOS_ChannelWidth=None,  # number
                                              _Driver_PMOS_Channellength=None,  # number
                                              _Driver_PMOS_GateSpacing=None,  # None/number
                                              _Driver_PMOS_SDWidth=None,  # None/number
                                              _Driver_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                              _Driver_PMOS_PCCrit=None,  # None/True

                                              # Source_node_ViaM1M2
                                              _Driver_PMOS_Source_Via_TF=None,  # True/False

                                              # Drain_node_ViaM1M2
                                              _Driver_PMOS_Drain_Via_TF=None,  # True/False

                                              # POLY dummy setting
                                              _Driver_PMOS_Dummy=True,  # TF
                                              # if _PMOSDummy == True
                                              _Driver_PMOS_Dummy_length=None,  # None/Value
                                              _Driver_PMOS_Dummy_placement=None,  # None/'Up'/'Dn'/
                                              ):

        ## Class_HEADER: Pre Defined Parameter Before Calculation
        ## Load DRC library
        _DRCObj = DRC.DRC()
        ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']
        ## CALCULATION START
        print('##############################################')
        print('##    CDAC With Driver Calculation_Start    ##')
        print('##############################################')

        # Pre-defined Design Value
        DriverOutputM4VtcPathWidth = 50


        ## H01_00_DriverCell (SREF) Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters0 = copy.deepcopy(H01_01_DriverArray_Arranged._DriverArray_Arranged._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters0['_NumOfBits'] = _NumOfBits
        _Caculation_Parameters0['_Driver_SizeByBit'] = _Driver_SizeByBit
        _Caculation_Parameters0['_Driver_NMOS_NumberofGate'] = _Driver_NMOS_NumberofGate
        _Caculation_Parameters0['_Driver_NMOS_ChannelWidth'] =_Driver_NMOS_ChannelWidth
        _Caculation_Parameters0['_Driver_NMOS_Channellength'] =_Driver_NMOS_Channellength
        _Caculation_Parameters0['_Driver_NMOS_GateSpacing'] =_Driver_NMOS_GateSpacing
        _Caculation_Parameters0['_Driver_NMOS_SDWidth'] =_Driver_NMOS_SDWidth
        _Caculation_Parameters0['_Driver_NMOS_XVT'] =_Driver_NMOS_XVT
        _Caculation_Parameters0['_Driver_NMOS_PCCrit'] =_Driver_NMOS_PCCrit
        _Caculation_Parameters0['_Driver_NMOS_Source_Via_TF'] =True #default
        _Caculation_Parameters0['_Driver_NMOS_Drain_Via_TF'] =True
        _Caculation_Parameters0['_Driver_NMOS_Dummy'] = True #default
        _Caculation_Parameters0['_Driver_NMOS_Dummy_length'] =_Driver_NMOS_Dummy_length
        _Caculation_Parameters0['_Driver_NMOS_Dummy_placement'] =_Driver_NMOS_Dummy_length
        _Caculation_Parameters0['_Driver_PMOS_NumberofGate'] = _Driver_PMOS_NumberofGate
        _Caculation_Parameters0['_Driver_PMOS_ChannelWidth'] =_Driver_PMOS_ChannelWidth
        _Caculation_Parameters0['_Driver_PMOS_Channellength'] =_Driver_PMOS_Channellength
        _Caculation_Parameters0['_Driver_PMOS_GateSpacing'] =_Driver_PMOS_GateSpacing
        _Caculation_Parameters0['_Driver_PMOS_SDWidth'] =_Driver_PMOS_SDWidth
        _Caculation_Parameters0['_Driver_PMOS_XVT'] =_Driver_PMOS_XVT
        _Caculation_Parameters0['_Driver_PMOS_PCCrit'] =_Driver_PMOS_PCCrit
        _Caculation_Parameters0['_Driver_PMOS_Source_Via_TF'] =True #default
        _Caculation_Parameters0['_Driver_PMOS_Drain_Via_TF'] =True
        _Caculation_Parameters0['_Driver_PMOS_Dummy'] = True #default
        _Caculation_Parameters0['_Driver_PMOS_Dummy_length'] =_Driver_PMOS_Dummy_length
        _Caculation_Parameters0['_Driver_PMOS_Dummy_placement'] =_Driver_PMOS_Dummy_placement

        self._DesignParameter['SRF_DriverArray'] = self._SrefElementDeclaration(
            _DesignObj=H01_01_DriverArray_Arranged._DriverArray_Arranged(_DesignParameter=None,
                                                     _Name='{}:SRF_DriverArray'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_DriverArray']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DriverArray']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DriverArray']['_DesignObj']._CalculateDesignParameter(
            **_Caculation_Parameters0)

        ## initialize Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DriverArray']['_XYCoordinates'] = [[0, 0]]

        MaxCapSize = 2 ** (_NumOfBits-1)

        ## SRF Capacitor Array Generation
        _Caculation_Parameters0 = copy.deepcopy(H00_05_CommonCentroid._CommonCentroid._ParametersForDesignCalculation)
        _Caculation_Parameters0['_LayoutOption'] =_CDAC_LayoutOption
        _Caculation_Parameters0['_ShieldingLayer'] =_CDAC_ShieldingLayer
        _Caculation_Parameters0['_BotNodeVtcExtensionMetalLayer'] =_CDAC_BotNodeVtcExtensionMetalLayer
        _Caculation_Parameters0['_MetalWidth'] =_CDAC_MetalWidth
        _Caculation_Parameters0['_MetalLength'] =_CDAC_MetalLength
        _Caculation_Parameters0['_MetalSpacing'] =_CDAC_MetalSpacing
        _Caculation_Parameters0['_NumOfElement'] =_CDAC_NumOfElement
        _Caculation_Parameters0['_ConnectLength'] =_CDAC_ConnectLength
        _Caculation_Parameters0['_ExtendLength'] =_CDAC_ExtendLength
        _Caculation_Parameters0['_Bitsize'] =_NumOfBits - 1
        _Caculation_Parameters0['_CapArrayWDrivingNodeDistance'] =_CDAC_CapArrayWDrivingNodeDistance
        _Caculation_Parameters0['_DriveNodeDistance'] =_CDAC_DriveNodeDistance
        _Caculation_Parameters0['_YWidth_Bottom_Hrz'] =_CDAC_YWidth_Bottom_Hrz
        _Caculation_Parameters0['_DummyCap_TopBottomShort'] = _CDAC_DummyCap_TopBottomShort
        _Caculation_Parameters0['_NumOfDummyCaps'] = _CDAC_NumOfDummyCaps

        self._DesignParameter['SRF_CapArray'] = self._SrefElementDeclaration(
            _DesignObj=H00_05_CommonCentroid._CommonCentroid(_DesignParameter=None,
                                                     _Name='{}:SRF_CapArray'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_CapArray']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CapArray']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CapArray']['_DesignObj']._CalculateDesignParameterFold1(
            **_Caculation_Parameters0)

        ## initialize Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CapArray']['_XYCoordinates'] = [[0, 0]]

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_DriverArray', 'SRF_PMOS_Body_Contact', 'SRF_NbodyContactPhyLen', 'BND_ODLayer')
        target_coord = tmp1[0][0][0][0][0]['_XY_up_left']

        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_CapArray', 'SRF_DummyCaps','SRF_CapWtShield4DCAP','BND_Shield_VTC_M{}'.format(_CDAC_ShieldingLayer))
        tmp3 = self.get_param_KJH4('SRF_CapArray', 'BND_DummyUCAP_Bot_Hrz')
        approaching_coord = [tmp2[0][0][0][0][0]['_XY_left'][0], tmp3[0][0][0]['_XY_down'][1]]

        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CapArray')
        Scoord = tmp3[0][0]['_XY_origin']
        SpaceBtwCapNDriver = 100
        Scoord[1] = Scoord[1] + _CDAC_YWidth_Bottom_Hrz + _CDAC_DriveNodeDistance + SpaceBtwCapNDriver

        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define Coordinates
        self._DesignParameter['SRF_CapArray']['_XYCoordinates'] = tmpXY

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
            if j == _NumOfBits-1:
                tmp1_1 = self.get_param_KJH4('SRF_CapArray', 'BND_DummyUCAP_Bot_Hrz')
            else:
                tmp1_1 = self.get_param_KJH4('SRF_CapArray', 'BND_B{}_Bottom_Hrz'.format(_NumOfBits - j - 2))
            tmp1_2 = self.get_param_KJH4('SRF_DriverArray', 'SRF_{}C_DriverCell'.format(CapSize), 'BND_Output_Node_Hrz_M4')
            self._DesignParameter['BND_{}C_Driver_Drain_Vtc_M4'.format(CapSize)]['_YWidth'] = abs(
                tmp1_1[0][0][0]['_XY_up'][1] - tmp1_2[0][0][0][0]['_XY_down'][1])

            ## Define Boundary_element _XWidth
            self._DesignParameter['BND_{}C_Driver_Drain_Vtc_M4'.format(CapSize)]['_XWidth'] = DriverOutputM4VtcPathWidth

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_{}C_Driver_Drain_Vtc_M4'.format(CapSize)]['_XYCoordinates'] = [[0, 0]]

            ## Calculate
            tmpXY = []
            ## Target_coord: _XY_type1
            target_coord = tmp1_2[0][0][0][0]['_XY_down_right']

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


            # Driver Output Node Viastack M4M5 generation
            ## ViaM1M2 (PMOS Array Vtc Path M1 <-> Gate Hrz Path M2)
            ## Sref generation: ViaX
            ## Define ViaX Parameter
            HrzRoutingMetal = 3
            MetUpper = max(4, HrzRoutingMetal)
            MetLower = min(4, HrzRoutingMetal)
            _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
            _Caculation_Parameters['_Layer1'] = MetLower
            _Caculation_Parameters['_Layer2'] = MetUpper
            _Caculation_Parameters['_COX'] = 2
            _Caculation_Parameters['_COY'] = 1
            self._DesignParameter['SRF_{}C_Driver_OutputNode_ViaM{}M{}'.format(CapSize,MetLower,MetUpper)] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                                                         _Name='{}:SRF_{}C_Driver_OutputNode_ViaM{}M{}'.format(
                                                                                             _Name, CapSize,MetLower,MetUpper)))[0]

            ## Define Sref Relection
            self._DesignParameter['SRF_{}C_Driver_OutputNode_ViaM{}M{}'.format(CapSize,MetLower,MetUpper)]['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
            self._DesignParameter['SRF_{}C_Driver_OutputNode_ViaM{}M{}'.format(CapSize,MetLower,MetUpper)]['_Angle'] = 0

            self._DesignParameter['SRF_{}C_Driver_OutputNode_ViaM{}M{}'.format(CapSize,MetLower,MetUpper)]['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            tmpXY = []
            ## Calculate Sref XYcoord
            ## initialized Sref coordinate
            self._DesignParameter['SRF_{}C_Driver_OutputNode_ViaM{}M{}'.format(CapSize,MetLower,MetUpper)]['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_{}C_Driver_Drain_Vtc_M4'.format(CapSize))
            target_coord = tmp1[0][0]['_XY_up']

            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_{}C_Driver_OutputNode_ViaM{}M{}'.format(CapSize,MetLower,MetUpper), 'SRF_ViaM{}M{}'.format(MetLower,MetLower+1),
                                       'BND_Met{}Layer'.format(MetLower))
            approaching_coord = tmp2[0][0][0][0]['_XY_up']

            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_{}C_Driver_OutputNode_ViaM{}M{}'.format(CapSize,MetLower,MetUpper))
            Scoord = tmp3[0][0]['_XY_origin']

            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

            ## Define
            self._DesignParameter['SRF_{}C_Driver_OutputNode_ViaM{}M{}'.format(CapSize,MetLower,MetUpper)]['_XYCoordinates'] = tmpXY


        ## Cap Array Bottom node
        ## Boundary Elemenet generation
        for i in range(_NumOfBits):
            CapSize = 2 ** (_NumOfBits - 1 - i)
            self._DesignParameter['BND_{}C_BottomNode_Hrz_M{}'.format(CapSize,HrzRoutingMetal)] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL{}'.format(HrzRoutingMetal)][0],
                _Datatype=DesignParameters._LayerMapping['METAL{}'.format(HrzRoutingMetal)][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )
            ## Define Boundary_element _YWidth
            self._DesignParameter['BND_{}C_BottomNode_Hrz_M{}'.format(CapSize,HrzRoutingMetal)]['_YWidth'] = 100

                    ## Define Boundary_element _XWidth
            if i == _NumOfBits-1:
                tmp1 = self.get_param_KJH4('SRF_CapArray', 'BND_DummyUCAP_Bot_Hrz')
            else:
                tmp1 = self.get_param_KJH4('SRF_CapArray', 'BND_B{}_Bottom_Hrz'.format(_NumOfBits - i - 2))
            tmp2 = self.get_param_KJH4('BND_{}C_Driver_Drain_Vtc_M4'.format(CapSize))

            if tmp1[0][0][0]['_XY_left'][0] < tmp2[0][0]['_XY_cent'][0]:
                tmpLeft = tmp1[0][0][0]['_XY_left'][0]
                XwidthExtensionL = 25
            else:
                tmpLeft = tmp2[0][0]['_XY_cent'][0]
                XwidthExtensionL = 122

            if tmp1[0][0][0]['_XY_right'][0] > tmp2[0][0]['_XY_cent'][0]:
                tmpRight = tmp1[0][0][0]['_XY_right'][0]
                XwidthExtensionR = 25
            else:
                tmpRight = tmp2[0][0]['_XY_cent'][0]
                XwidthExtensionR = 122
            self._DesignParameter['BND_{}C_BottomNode_Hrz_M{}'.format(CapSize,HrzRoutingMetal)]['_XWidth'] = tmpRight - tmpLeft + XwidthExtensionL + XwidthExtensionR

                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['BND_{}C_BottomNode_Hrz_M{}'.format(CapSize,HrzRoutingMetal)]['_XYCoordinates'] = [[0, 0]]

                            ## Calculate
                                ## Target_coord: _XY_type1
            if i == _NumOfBits-1:
                tmp1 = self.get_param_KJH4('SRF_CapArray', 'BND_DummyUCAP_Bot_Hrz')
            else:
                tmp1 = self.get_param_KJH4('SRF_CapArray', 'BND_B{}_Bottom_Hrz'.format(_NumOfBits - i - 2))
            target_coord = [tmpLeft - XwidthExtensionL, tmp1[0][0][0]['_XY_cent'][1]]

                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_{}C_BottomNode_Hrz_M{}'.format(CapSize,HrzRoutingMetal))
            approaching_coord = tmp2[0][0]['_XY_left']

                                ## Sref coord
            Scoord = tmp2[0][0]['_XY_origin']

                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

                                ## Define coordinates
            self._DesignParameter['BND_{}C_BottomNode_Hrz_M{}'.format(CapSize,HrzRoutingMetal)]['_XYCoordinates'] = tmpXY



        ## Dummy Driver Cell Output Vtc M4
        ## Boundary Elemenet generation
        self._DesignParameter['BND_DummyUCAP_Driver_Drain_Vtc_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        tmp1_1 = self.get_param_KJH4('SRF_CapArray', 'BND_DummyUCAP_Bot_Hrz')
        tmp1_2 = self.get_param_KJH4('SRF_DriverArray', 'SRF_Dummy_DriverCell', 'BND_Output_Node_Hrz_M4')
        self._DesignParameter['BND_DummyUCAP_Driver_Drain_Vtc_M4']['_YWidth'] = abs(
            tmp1_1[0][0][0]['_XY_up'][1] - tmp1_2[0][0][0][0]['_XY_down'][1]) - _CDAC_DriveNodeDistance - _CDAC_YWidth_Bottom_Hrz

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_DummyUCAP_Driver_Drain_Vtc_M4']['_XWidth'] = DriverOutputM4VtcPathWidth

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_DummyUCAP_Driver_Drain_Vtc_M4']['_XYCoordinates'] = [[0, 0]]

        ## Calculate
        tmpXY = []
        ## Target_coord: _XY_type1
        target_coord = tmp1_2[0][0][0][0]['_XY_down_right']

        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_DummyUCAP_Driver_Drain_Vtc_M4')
        approaching_coord = tmp2[0][0]['_XY_down_right']

        ## Sref coord
        Scoord = tmp2[0][0]['_XY_origin']

        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define coordinates
        self._DesignParameter['BND_DummyUCAP_Driver_Drain_Vtc_M4']['_XYCoordinates'] = tmpXY


        # Dummy Driver Output Node Viastack M4M5 generation
        ## ViaM1M2 (PMOS Array Vtc Path M1 <-> Gate Hrz Path M2)
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        # HrzRoutingMetal = 5
        MetUpper = max(4, HrzRoutingMetal)
        MetLower = min(4, HrzRoutingMetal)
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = MetLower
        _Caculation_Parameters['_Layer2'] = MetUpper
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1
        self._DesignParameter['SRF_DummyUCAP_Driver_OutputNode_ViaM{}M{}'.format(MetLower, MetUpper)] = \
        self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                                            _Name='{}:SRF_DummyUCAP_Driver_OutputNode_ViaMM{}M{}'.format(
                                                                                _Name, MetLower, MetUpper)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_DummyUCAP_Driver_OutputNode_ViaM{}M{}'.format(MetLower, MetUpper)]['_Reflect'] = [
            0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_DummyUCAP_Driver_OutputNode_ViaM{}M{}'.format(MetLower, MetUpper)]['_Angle'] = 0

        self._DesignParameter['SRF_DummyUCAP_Driver_OutputNode_ViaM{}M{}'.format(MetLower, MetUpper)][
            '_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        tmpXY = []
        ## Calculate Sref XYcoord
        ## initialized Sref coordinate
        self._DesignParameter['SRF_DummyUCAP_Driver_OutputNode_ViaM{}M{}'.format(MetLower, MetUpper)][
            '_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_DummyUCAP_Driver_Drain_Vtc_M4')
        target_coord = tmp1[0][0]['_XY_up']

        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_DummyUCAP_Driver_OutputNode_ViaM{}M{}'.format(MetLower, MetUpper),
                                   'SRF_ViaM{}M{}'.format(MetLower, MetLower + 1),
                                   'BND_Met{}Layer'.format(MetLower))
        approaching_coord = tmp2[0][0][0][0]['_XY_up']

        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_DummyUCAP_Driver_OutputNode_ViaM{}M{}'.format(MetLower, MetUpper))
        Scoord = tmp3[0][0]['_XY_origin']

        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define
        self._DesignParameter['SRF_DummyUCAP_Driver_OutputNode_ViaM{}M{}'.format(MetLower, MetUpper)][
            '_XYCoordinates'] = tmpXY




############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ZZ01_H02_00_CDACWtDriver_Arranged'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'H02_00_CDACWDriver'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
            # debugging log: 5bit, L 1414, 3000, 5000x, W 50 80 300
        _NumOfBits=4,
        # # Element CDAC
        _CDAC_LayoutOption=[5,6],
        _CDAC_ShieldingLayer=1,  # Poly:0, M1:1, M2:2 ...
        _CDAC_BotNodeVtcExtensionMetalLayer=2,
        _CDAC_MetalWidth=50,
        _CDAC_MetalLength=1414,
        _CDAC_MetalSpacing=50,

        # #Unit Cap
        _CDAC_NumOfElement=2,

        # # Shielding & Top Connect node
        _CDAC_ConnectLength=400,
        _CDAC_ExtendLength=400,

        # # Dummy Cap Option
        _CDAC_DummyCap_TopBottomShort=None,
        _CDAC_NumOfDummyCaps=3,  # Number of dummy cap(one side)

        # # CommonCentroid With Driving node
        _CDAC_CapArrayWDrivingNodeDistance=1500,  # DRC Rule
        _CDAC_DriveNodeDistance=279,  #
        _CDAC_YWidth_Bottom_Hrz=50,

        # Driver(Inverter) Sizing Option
        _Driver_SizeByBit=[8,4,2,1],    # [int, int, ...] (Drv. Arranged Version을 위한 옵션)

        # Driver(Inverter) NMOS
        _Driver_NMOS_NumberofGate = 1,  # number
        _Driver_NMOS_ChannelWidth = 340,  # number
        _Driver_NMOS_Channellength = 30,  # number
        _Driver_NMOS_GateSpacing = None,  # None/number
        _Driver_NMOS_SDWidth = None,  # None/number
        _Driver_NMOS_XVT = 'SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Driver_NMOS_PCCrit = None,  # None/True

            # Source_node_ViaM1M2
        _Driver_NMOS_Source_Via_TF = True,  # True/False

            # Drain_node_ViaM1M2
        _Driver_NMOS_Drain_Via_TF = None,  # True/False

            # POLY dummy setting
        _Driver_NMOS_Dummy = True,  # TF
            # if _PMOSDummy == True
        _Driver_NMOS_Dummy_length = None,  # None/Value
        _Driver_NMOS_Dummy_placement = None,  # None/'Up'/'Dn'/l

        # Driver(Inverter) PMOS
        _Driver_PMOS_NumberofGate = 1,  # number
        _Driver_PMOS_ChannelWidth=900,  # number
        _Driver_PMOS_Channellength=30,  # number
        _Driver_PMOS_GateSpacing=None,  # None/number
        _Driver_PMOS_SDWidth=None,  # None/number
        _Driver_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Driver_PMOS_PCCrit=None,  # None/True

        # Source_node_ViaM1M2
        _Driver_PMOS_Source_Via_TF=None,  # True/False

        # Drain_node_ViaM1M2
        _Driver_PMOS_Drain_Via_TF=None,  # True/False

        # POLY dummy setting
        _Driver_PMOS_Dummy=True,  # TF
        # if _PMOSDummy == True
        _Driver_PMOS_Dummy_length=None,  # None/Value
        _Driver_PMOS_Dummy_placement=None,  # None/'Up'/'Dn'/
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

    # LayoutObj._CalculateDesignParameter(**InputParams)
    # LayoutObj._CalculateDesignParameterFold1(**InputParams)
    LayoutObj._CalculateDesignParameter_DrvArranged(**InputParams)

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
    Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()

    ''' Check Time'''
    elapsed_time = time.time() - start_time
    m, s = divmod(elapsed_time, 60)
    h, m = divmod(m, 60)

    print('#############################      Finished      ################################')
# end of 'main():' ---------------------------------------------------------------------------------------------
