## Import Basic Modules
## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC
# from KJH91_Projects.Project_ADC.Library_and_Engine import DRCv2

## Library
import copy
import math
import numpy as np
import time

## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.H00_CDAC_v2 import H00_05_CommonCentroid
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaM8toM9_YJH
from KJH91_Projects.Project_ADC.Layoutgen_code.H02_CDACWtDriver_YJH import H02_00_CDACWtDriver



############################################################################################################################################################ Class_HEADER
class _CDACWtDriverFold1(StickDiagram_KJH1._StickDiagram_KJH):
    ##########################################################################################################################
    # Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(
        _NumOfBits=5,   # 5 이상

        # # Element CDAC
        _CDAC_LayoutOption=[5,6],
        _CDAC_ShieldingLayer=4,  # Poly:0, M1:1, M2:2 ...
        _CDAC_BotNodeVtcExtensionMetalLayer=None,
        _CDAC_MetalWidth=50,
        _CDAC_MetalLength=1414, # (8bit size: 1414/ 10bit size: 2800/ 12bit size: 4200)
        _CDAC_MetalSpacing=50,

        # #Unit Cap
        _CDAC_NumOfElement=2,

        # # Shielding & Top Connect node
        _CDAC_ConnectLength=400,
        _CDAC_ExtendLength=400,

        # # Dummy Cap Option
        _CDAC_DummyCap_TopBottomShort=False,    # False -> Bottom = GND
        _CDAC_NumOfDummyCaps=3,  # Number of dummy cap(one side)

        # # CommonCentroid With Driving node
        _CDAC_CapArrayWDrivingNodeDistance=0,  # DRC Rule
        _CDAC_DriveNodeDistance=400,  #
        _CDAC_YWidth_Bottom_Hrz=50,

            # Driver(Inverter) NMOS
        _Driver_NMOS_NumberofGate = 1,  # number
        _Driver_NMOS_ChannelWidth = 340,  # number (8bit size: 340/ 10bit size: 680/ 12bit size: 1020)
        _Driver_NMOS_Channellength = 30,  # number
        _Driver_NMOS_XVT = 'SLVT',  # 'XVT' ex)SLVT LVT RVT HVT

        # Driver(Inverter) PMOS
        _Driver_PMOS_NumberofGate = 1,  # number
        _Driver_PMOS_ChannelWidth=900,  # number (8bit size: 900/ 10bit size: 1800/ 12bit size: 2700)
        _Driver_PMOS_Channellength=30,  # number
        _Driver_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT

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
                                  _NumOfBits=5,  # 5 이상

                                  # # Element CDAC
                                  _CDAC_LayoutOption=[5, 6],
                                  _CDAC_ShieldingLayer=4,  # Poly:0, M1:1, M2:2 ...
                                  _CDAC_BotNodeVtcExtensionMetalLayer=None,
                                  _CDAC_MetalWidth=50,
                                  _CDAC_MetalLength=1414,  # (8bit size: 1414/ 10bit size: 2800/ 12bit size: 4200)
                                  _CDAC_MetalSpacing=50,

                                  # #Unit Cap
                                  _CDAC_NumOfElement=2,

                                  # # Shielding & Top Connect node
                                  _CDAC_ConnectLength=400,
                                  _CDAC_ExtendLength=400,

                                  # # Dummy Cap Option
                                  _CDAC_DummyCap_TopBottomShort=False,  # False -> Bottom = GND
                                  _CDAC_NumOfDummyCaps=3,  # Number of dummy cap(one side)

                                  # # CommonCentroid With Driving node
                                  _CDAC_CapArrayWDrivingNodeDistance=0,  # DRC Rule
                                  _CDAC_DriveNodeDistance=400,  #
                                  _CDAC_YWidth_Bottom_Hrz=50,

                                  # Driver Sizing
                                  _Driver_SizeByBit=None,
                                  # Driver(Inverter) NMOS
                                  _Driver_NMOS_NumberofGate=1,  # number
                                  _Driver_NMOS_ChannelWidth=340,
                                  # number (8bit size: 340/ 10bit size: 680/ 12bit size: 1020)
                                  _Driver_NMOS_Channellength=30,  # number
                                  _Driver_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT

                                  # Driver(Inverter) PMOS
                                  _Driver_PMOS_NumberofGate=1,  # number
                                  _Driver_PMOS_ChannelWidth=900,
                                  # number (8bit size: 900/ 10bit size: 1800/ 12bit size: 2700)
                                  _Driver_PMOS_Channellength=30,  # number
                                  _Driver_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT

                                  ):


        ## Class_HEADER: Pre Defined Parameter Before Calculation
        ## Load DRC library
        _DRCObj = DRC.DRC()
        ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']
        ## CALCULATION START
        print('###############################################################')
        print('##    CDAC With Driver (folded virsion) Calculation_Start    ##')
        print('###############################################################')

        if len(_Driver_SizeByBit) != _NumOfBits:
            raise Exception(f"_Driver_SizeByBit != _NumOfBits !!!")

        ## H02_00_CDACWDriver (SREF) Generation
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters0 = copy.deepcopy(H02_00_CDACWtDriver._CDACWtDriver._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters0['_NumOfBits'] = _NumOfBits
        _Caculation_Parameters0['_CDAC_LayoutOption'] =_CDAC_LayoutOption
        _Caculation_Parameters0['_CDAC_ShieldingLayer'] =_CDAC_ShieldingLayer
        _Caculation_Parameters0['_CDAC_BotNodeVtcExtensionMetalLayer'] = _CDAC_BotNodeVtcExtensionMetalLayer
        _Caculation_Parameters0['_CDAC_MetalWidth'] = _CDAC_MetalWidth
        _Caculation_Parameters0['_CDAC_MetalLength'] = _CDAC_MetalLength
        _Caculation_Parameters0['_CDAC_MetalSpacing'] = _CDAC_MetalSpacing
        _Caculation_Parameters0['_CDAC_NumOfElement'] = _CDAC_NumOfElement
        _Caculation_Parameters0['_CDAC_ConnectLength'] = _CDAC_ConnectLength
        _Caculation_Parameters0['_CDAC_ExtendLength'] = _CDAC_ExtendLength
        _Caculation_Parameters0['_CDAC_CapArrayWDrivingNodeDistance'] = _CDAC_CapArrayWDrivingNodeDistance
        _Caculation_Parameters0['_CDAC_DriveNodeDistance'] = _CDAC_DriveNodeDistance
        _Caculation_Parameters0['_CDAC_YWidth_Bottom_Hrz'] = _CDAC_YWidth_Bottom_Hrz
        _Caculation_Parameters0['_CDAC_DummyCap_TopBottomShort'] = _CDAC_DummyCap_TopBottomShort
        _Caculation_Parameters0['_CDAC_NumOfDummyCaps'] = _CDAC_NumOfDummyCaps
        _Caculation_Parameters0['_Driver_SizeByBit'] = _Driver_SizeByBit
        _Caculation_Parameters0['_Driver_NMOS_NumberofGate'] = _Driver_NMOS_NumberofGate
        _Caculation_Parameters0['_Driver_NMOS_ChannelWidth'] = _Driver_NMOS_ChannelWidth
        _Caculation_Parameters0['_Driver_NMOS_Channellength'] = _Driver_NMOS_Channellength
        _Caculation_Parameters0['_Driver_NMOS_GateSpacing'] = None
        _Caculation_Parameters0['_Driver_NMOS_SDWidth'] = None
        _Caculation_Parameters0['_Driver_NMOS_XVT'] = _Driver_NMOS_XVT
        _Caculation_Parameters0['_Driver_NMOS_PCCrit'] = None
        _Caculation_Parameters0['_Driver_NMOS_Source_Via_TF'] = True  # default
        _Caculation_Parameters0['_Driver_NMOS_Drain_Via_TF'] = True
        _Caculation_Parameters0['_Driver_NMOS_Dummy'] = True  # default
        _Caculation_Parameters0['_Driver_NMOS_Dummy_length'] = None
        _Caculation_Parameters0['_Driver_NMOS_Dummy_placement'] = None
        _Caculation_Parameters0['_Driver_PMOS_NumberofGate'] = _Driver_PMOS_NumberofGate
        _Caculation_Parameters0['_Driver_PMOS_ChannelWidth'] = _Driver_PMOS_ChannelWidth
        _Caculation_Parameters0['_Driver_PMOS_Channellength'] = _Driver_PMOS_Channellength
        _Caculation_Parameters0['_Driver_PMOS_GateSpacing'] = None
        _Caculation_Parameters0['_Driver_PMOS_SDWidth'] = None
        _Caculation_Parameters0['_Driver_PMOS_XVT'] = _Driver_PMOS_XVT
        _Caculation_Parameters0['_Driver_PMOS_PCCrit'] = None
        _Caculation_Parameters0['_Driver_PMOS_Source_Via_TF'] = True  # default
        _Caculation_Parameters0['_Driver_PMOS_Drain_Via_TF'] = True
        _Caculation_Parameters0['_Driver_PMOS_Dummy'] = True  # default
        _Caculation_Parameters0['_Driver_PMOS_Dummy_length'] = None
        _Caculation_Parameters0['_Driver_PMOS_Dummy_placement'] = None


        #############
        ## Upper CDAC (Cap, Driver Array) Generation
        self._DesignParameter['SRF_CDAC_LowerHalf'] = self._SrefElementDeclaration(
            _DesignObj=H02_00_CDACWtDriver._CDACWtDriver(_DesignParameter=None,
                                                     _Name='{}:SRF_CDAC_LowerHalf'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_CDAC_LowerHalf']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CDAC_LowerHalf']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CDAC_LowerHalf']['_DesignObj']._CalculateDesignParameter_DrvArranged(**_Caculation_Parameters0)

        ## initialize Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CDAC_LowerHalf']['_XYCoordinates'] = [[0, 0]]


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

        ## Upper CDAC (Cap, Driver Array) Generation
        self._DesignParameter['SRF_CDAC_UpperHalf'] = self._SrefElementDeclaration(
            _DesignObj=H00_05_CommonCentroid._CommonCentroid(_DesignParameter=None,
                                                         _Name='{}:SRF_CDAC_UpperHalf'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_CDAC_UpperHalf']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CDAC_UpperHalf']['_Angle'] = 180

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CDAC_UpperHalf']['_DesignObj']._CalculateDesignParameterFold1(
            **_Caculation_Parameters0)

        tmpXY = []
        ## Calculate Sref XYcoord
        self._DesignParameter['SRF_CDAC_UpperHalf']['_XYCoordinates'] = [[0, 0]]

        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('SRF_CDAC_LowerHalf', 'SRF_CapArray', \
                                   'SRF_DummyCaps', 'SRF_CapWtShield4DCAP',
                                   'BND_Shield_Extend_VTC_M{}'.format(_CDAC_LayoutOption[-1]))
        target_coord = tmp1[0][0][0][0][0][0]['_XY_up_left']

        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CDAC_UpperHalf',
                                   'SRF_DummyCaps', 'SRF_CapWtShield4DCAP',
                                   'BND_Shield_Extend_VTC_M{}'.format(_CDAC_LayoutOption[-1]))
        approaching_coord = tmp2[0][-1][0][0][0]['_XY_up_right']

        ## Sref coor
        SpaceBtwCapArray = 0  # DRC 확인 필요
        tmp3 = self.get_param_KJH4('SRF_CDAC_UpperHalf')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[1] = Scoord[1] + SpaceBtwCapArray

        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['SRF_CDAC_UpperHalf']['_XYCoordinates'] = tmpXY


        ## CDAC Control Signal Vtc M2
        ## Boundary Element Generation
        for i in range(_NumOfBits):
            self._DesignParameter['BND_CDACFold1_B{}_DrvOutput_Vtc_M2'.format(_NumOfBits - 1 -  i)] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
            )
            DrvOutputVtcPathWidth = 100
            SpaceBtwDrvOutputVtcPath = 100
            ## Define Boundary_element _XWidth
            self._DesignParameter['BND_CDACFold1_B{}_DrvOutput_Vtc_M2'.format(_NumOfBits - 1 - i)]['_XWidth'] = DrvOutputVtcPathWidth

            if i == _NumOfBits - 1:  # 마지막 for loop 사이클 -> Dummy Vtc Output Path (최내측) 생성 "BND_CDACFold1_B-1_DrvOutput_Vtc_M2"
                    ## Define Boundary_element _YWidth
                tmp1 = self.get_param_KJH4('SRF_CDAC_UpperHalf','BND_DummyUCAP_Bot_Hrz')
                tmp2 = self.get_param_KJH4('SRF_CDAC_LowerHalf','SRF_DummyUCAP_Driver_OutputNode_ViaM3M4','SRF_ViaM3M4','BND_Met3Layer')
                self._DesignParameter['BND_CDACFold1_B{}_DrvOutput_Vtc_M2'.format(_NumOfBits - 1 -  i)]['_YWidth'] = \
                    abs(tmp1[0][0][0]['_XY_cent'][1] - tmp2[0][0][0][0][0]['_XY_cent'][1]) + 100   # Hrz_M5_PathWidth

            else:
                    ## Define Boundary_element _YWidth
                # CapSize = 2 ** (_NumOfBits - 2 -  i)    # Folded구조라 -2 임. ex. 4Bit에서 B0_DrivInput_Vtc_M2는 Upper, LowerHalf(두 개의 4C)의 4C_Driver_Input_Hrz와 연결됨.
                tmp1 = self.get_param_KJH4('SRF_CDAC_UpperHalf','BND_B{}_Bottom_Hrz'.format(_NumOfBits - i - 2))
                tmp2 = self.get_param_KJH4('SRF_CDAC_LowerHalf','SRF_CapArray', 'BND_B{}_Bottom_Hrz'.format(_NumOfBits - i - 2))
                self._DesignParameter['BND_CDACFold1_B{}_DrvOutput_Vtc_M2'.format(_NumOfBits - 1 -  i)]['_YWidth'] = \
                    abs(tmp1[0][0][0]['_XY_cent'][1] - tmp2[0][0][0][0]['_XY_cent'][1]) + 100   # Hrz_M5_PathWidth

                    ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_CDACFold1_B{}_DrvOutput_Vtc_M2'.format(_NumOfBits - 1 -  i)]['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
            tmpXY = []
            ## Calculate
            ## Target_coord: _XY_type1
            tmp3 = self.get_param_KJH4('SRF_CDAC_LowerHalf','SRF_CapArray', 'SRF_DummyCaps', 'SRF_CapWtShield4DCAP', 'BND_Shield_Extend_VTC_M5')
            # tmp3 = self.get_param_KJH4('SRF_CDAC_LowerHalf','SRF_DriverArray', 'SRF_PMOS_Body_Contact', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
            if i == _NumOfBits - 1:
                target_coord = [tmp3[0][0][0][0][0][0]['_XY_left'][0], tmp2[0][0][0][0][0]['_XY_cent'][1] - (100)/2]   # Hrz_M5_PathWidth / 2

                ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('BND_CDACFold1_B{}_DrvOutput_Vtc_M2'.format(_NumOfBits - 1 - i))
                approaching_coord = tmp2[0][0]['_XY_down']

            else:
                target_coord = [tmp3[0][0][0][0][0][0]['_XY_left'][0], int((tmp1[0][0][0]['_XY_down'][1]+tmp2[0][0][0][0]['_XY_down'][1])/2)]

                ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('BND_CDACFold1_B{}_DrvOutput_Vtc_M2'.format(_NumOfBits - 1 -  i))
                approaching_coord = tmp2[0][0]['_XY_cent']

            ## Sref coord
            SpaceBtwInputNCapArray = 550
            Scoord = tmp2[0][0]['_XY_origin']
            Scoord[0] = Scoord[0] - SpaceBtwInputNCapArray - (SpaceBtwDrvOutputVtcPath + DrvOutputVtcPathWidth) * (_NumOfBits - 2 -  i) - (SpaceBtwDrvOutputVtcPath + DrvOutputVtcPathWidth)    # Dummy Drv Vtc Path까지 고려하여 추가
            # Scoord[1] = Scoord[1] - 244 # Minimum Via Ywidth

            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

            ## Define coordinates
            self._DesignParameter['BND_CDACFold1_B{}_DrvOutput_Vtc_M2'.format(_NumOfBits - 1 -  i)]['_XYCoordinates'] = tmpXY


        ## CDAC Control Signal Hrz M3 & ViastackM2M3 (Drv Input Hrz M3 Extend <-> Input Vtc M2)
        ## Boundary Element Generation
        tmpXY0 = []
        for i in range(_NumOfBits):
            for j in range(2):
                flag = 'Lo' if j == 0 else 'Upp'
                self._DesignParameter['BND_CDACFold1_{}B{}_DrvOutput_Hrz_M3'.format(flag, _NumOfBits - 1- i)] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL3'][0],
                _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
                )
                if i == _NumOfBits - 1: # 마지막 for loop 사이클
                            ## Define Boundary_element _YWidth
                    # tmp1 = self.get_param_KJH4('SRF_CDAC_UpperHalf','SRF_DriverArray','BND_Dummy_Driver_Input_Vtc_M2')    #UpperHalf는 180도 회전해서 'XY_down'이 가장 높은 지점임.
                    tmp2 = self.get_param_KJH4('SRF_CDAC_LowerHalf','SRF_DummyUCAP_Driver_OutputNode_ViaM3M4','SRF_ViaM3M4','BND_Met3Layer')
                    tmp3 = self.get_param_KJH4('SRF_CDAC_UpperHalf','BND_DummyUCAP_Bot_Hrz')
                    tmp4 = self.get_param_KJH4('BND_CDACFold1_B{}_DrvOutput_Vtc_M2'.format(_NumOfBits -  i - 1))
                else:
                            ## Define Boundary_element _YWidth
                    # tmp1 = self.get_param_KJH4('SRF_CDAC_UpperHalf','SRF_DriverArray','BND_Dummy_Driver_Input_Vtc_M2')    #UpperHalf는 180도 회전해서 'XY_down'이 가장 높은 지점임.
                    tmp2 = self.get_param_KJH4('SRF_CDAC_LowerHalf','SRF_CapArray', 'BND_B{}_Bottom_Hrz'.format(_NumOfBits - i - 2))
                    tmp3 = self.get_param_KJH4('SRF_CDAC_UpperHalf','BND_B{}_Bottom_Hrz'.format(_NumOfBits - i - 2))
                    tmp4 = self.get_param_KJH4('BND_CDACFold1_B{}_DrvOutput_Vtc_M2'.format(_NumOfBits -  i - 1))

                self._DesignParameter['BND_CDACFold1_{}B{}_DrvOutput_Hrz_M3'.format(flag, _NumOfBits - 1- i)]['_YWidth'] = 100

                        ## Define Boundary_element _XWidth

                if flag == 'Lo':
                    if i == _NumOfBits - 1:
                        self._DesignParameter['BND_CDACFold1_{}B{}_DrvOutput_Hrz_M3'.format(flag, _NumOfBits - 1 - i)]['_XWidth'] = abs(tmp2[0][0][0][0][0]['_XY_right'][0] - tmp4[0][0]['_XY_cent'][0])
                    else:
                        self._DesignParameter['BND_CDACFold1_{}B{}_DrvOutput_Hrz_M3'.format(flag, _NumOfBits - 1 - i)]['_XWidth'] = abs(tmp2[0][0][0][0]['_XY_left'][0] - tmp4[0][0]['_XY_cent'][0])

                else:
                    if i == _NumOfBits - 1:
                        self._DesignParameter['BND_CDACFold1_{}B{}_DrvOutput_Hrz_M3'.format(flag, _NumOfBits - 1 - i)]['_XWidth'] = abs(tmp3[0][0][0]['_XY_left'][0] - tmp4[0][0]['_XY_cent'][0]) + 122

                    else:
                        self._DesignParameter['BND_CDACFold1_{}B{}_DrvOutput_Hrz_M3'.format(flag, _NumOfBits - 1 - i)]['_XWidth'] = abs(tmp3[0][0][0]['_XY_left'][0] - tmp4[0][0]['_XY_cent'][0])

                    ## Define Boundary_element _XYCoordinates
                self._DesignParameter['BND_CDACFold1_{}B{}_DrvOutput_Hrz_M3'.format(flag, _NumOfBits - 1- i)]['_XYCoordinates'] = [[0, 0]]

                ## Lower쪽의 Y위치를 타겟으로 한 번, Upper에서 한 번 더 tmpXY에 append하여 두 좌표를 인덱스에 넣음
                ## Calculate Sref XYcoord
                tmpXY = []
                ## Calculate
                if flag == 'Lo':
                    if i == _NumOfBits - 1:
                        ## Target1_coord: _XY_type1
                        target_coord = [tmp4[0][0]['_XY_cent'][0], tmp2[0][0][0][0][0]['_XY_cent'][1]]
                    else:
                        ## Target1_coord: _XY_type1
                        target_coord = [tmp4[0][0]['_XY_cent'][0], tmp2[0][0][0][0]['_XY_cent'][1]]
                else:
                    ## Target2_coord: _XY_type1
                    target_coord = [tmp4[0][0]['_XY_cent'][0], tmp3[0][0][0]['_XY_cent'][1]]

                ## Approaching_coord: _XY_type2
                tmp5 = self.get_param_KJH4('BND_CDACFold1_{}B{}_DrvOutput_Hrz_M3'.format(flag, _NumOfBits - 1- i))
                approaching_coord = tmp5[0][0]['_XY_left']

                ## Sref coord
                Scoord = tmp5[0][0]['_XY_origin']

                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)

                ## Sref coord
                Scoord = tmp5[0][0]['_XY_origin']

                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)

                ## Define coordinates
                self._DesignParameter['BND_CDACFold1_{}B{}_DrvOutput_Hrz_M3'.format(flag, _NumOfBits - 1- i)]['_XYCoordinates'] = tmpXY



                ############ Input Viastack M2M3
                ## Sref generation: ViaX
                ## Define ViaX Parameter
                _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
                _Caculation_Parameters['_Layer1'] = 2
                _Caculation_Parameters['_Layer2'] = 3
                _Caculation_Parameters['_COX'] = 1
                _Caculation_Parameters['_COY'] = 2

                ## Sref ViaX declaration
                self._DesignParameter['SRF_DrvOutputViaM2M3'] = \
                    self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                                                             _Name='{}:SRF_DrvOutputViaM2M3'.format(
                                                                                                 _Name)))[0]
                ## Define Sref Relection
                self._DesignParameter['SRF_DrvOutputViaM2M3']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle
                self._DesignParameter['SRF_DrvOutputViaM2M3']['_Angle'] = 0

                ## Calculate Sref XYcoord
                ## initialized Sref coordinate
                self._DesignParameter['SRF_DrvOutputViaM2M3']['_XYCoordinates'] = [[0, 0]]

                ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
                self._DesignParameter['SRF_DrvOutputViaM2M3']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

                ## Calculate Sref XYcoord
                if flag == 'Lo':
                    ## Calculate
                    ## Target_coord
                    tmp1 = self.get_param_KJH4('BND_CDACFold1_{}B{}_DrvOutput_Hrz_M3'.format(flag, _NumOfBits - 1- i))
                    target_coord = tmp1[0][0]['_XY_down_left']
                    ## Approaching_coord
                    tmp2 = self.get_param_KJH4('SRF_DrvOutputViaM2M3','SRF_ViaM2M3','BND_Met3Layer')
                    approaching_coord = tmp2[0][0][0][0]['_XY_down']
                    ## Sref coord
                    tmp3 = self.get_param_KJH4('SRF_DrvOutputViaM2M3')
                    Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
                    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                    tmpXY0.append(New_Scoord)
                else:
                    ## Calculate
                    ## Target_coord
                    tmp1 = self.get_param_KJH4('BND_CDACFold1_{}B{}_DrvOutput_Hrz_M3'.format(flag, _NumOfBits - 1- i))
                    target_coord = tmp1[0][0]['_XY_up_left']
                    ## Approaching_coord
                    tmp2 = self.get_param_KJH4('SRF_DrvOutputViaM2M3','SRF_ViaM2M3','BND_Met3Layer')
                    approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
                    tmp3 = self.get_param_KJH4('SRF_DrvOutputViaM2M3')
                    Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
                    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                    tmpXY0.append(New_Scoord)
                    ## Define
        self._DesignParameter['SRF_DrvOutputViaM2M3']['_XYCoordinates'] = tmpXY0



        ### BND_CDACTopPlate_Hrz_IA (CDAC Top Node) Generation
        ## Comp Input Lower Half Node(Hrz, IA)
        ## Boundary_element Generation
        self._DesignParameter['BND_CDACLowerTopNode_Hrz_IA'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL8'][0],
        _Datatype=DesignParameters._LayerMapping['METAL8'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        CDACTopPlateHrzPathWidth = 1000
        self._DesignParameter['BND_CDACLowerTopNode_Hrz_IA']['_YWidth'] = CDACTopPlateHrzPathWidth

                ## Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH4('SRF_CDAC_LowerHalf', 'SRF_CapArray', 'SRF_DummyCaps', 'SRF_CapWtShield4DCAP', 'BND_Shield_VTC_M{}'.format(_CDAC_ShieldingLayer))
        CDACTopPlateHrzPathLength = abs(tmp2[0][0][0][0][0][0]['_XY_left'][0] - tmp2[0][0][-1][0][-1][0]['_XY_right'][0])
        self._DesignParameter['BND_CDACLowerTopNode_Hrz_IA']['_XWidth'] = CDACTopPlateHrzPathLength

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CDACLowerTopNode_Hrz_IA']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate
                            ## Target_coord: _XY_type1
        # tmp1 = self.get_param_KJH4('SRF_CDAC_LowerHalf', 'SRF_CapArray', 'SRF_CommonArray',\
        #                            'SRF_CDAC_B{}'.format(_NumOfBits - 1 - 1), 'BND_Shield_VTC_M{}'.format(_CDAC_ShieldingLayer))
        target_coord = tmp2[0][0][0][0][0][0]['_XY_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CDACLowerTopNode_Hrz_IA')
        approaching_coord = tmp2[0][0]['_XY_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CDACLowerTopNode_Hrz_IA')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_CDACLowerTopNode_Hrz_IA']['_XYCoordinates'] = tmpXY



        ### BND_CDACTopPlate_Hrz_M7 (CDAC Top Node) Generation
        ## Comp Input Lower Half Node(Hrz, M7)
        ## Boundary_element Generation
        CDACTopPlateM7HrzPathWidth = 2*_DRCObj._VIAzMinEnclosureByMetxOrMetyTwoOppositeSide + _DRCObj._VIAzMinWidth
        self._DesignParameter['BND_CDACLowerTopNode_Hrz_M7'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL7'][0],
        _Datatype=DesignParameters._LayerMapping['METAL7'][1],
        _XWidth=CDACTopPlateHrzPathLength,
        _YWidth=CDACTopPlateM7HrzPathWidth,
        _XYCoordinates=[[0,0]],
        )
        tmpXY=[]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_CDACLowerTopNode_Hrz_IA')
        target_coord = tmp1[0][0]['_XY_cent']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CDACLowerTopNode_Hrz_M7')
        approaching_coord = tmp2[0][0]['_XY_cent']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CDACLowerTopNode_Hrz_M7')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_CDACLowerTopNode_Hrz_M7']['_XYCoordinates'] = tmpXY


        ## Comp Input Upper Half Node (Hrz, IA)
        ## Boundary_element Generation
        self._DesignParameter['BND_CDACUpperTopNode_Hrz_IA'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL8'][0],
        _Datatype=DesignParameters._LayerMapping['METAL8'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_CDACUpperTopNode_Hrz_IA']['_YWidth'] = CDACTopPlateHrzPathWidth

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CDACUpperTopNode_Hrz_IA']['_XWidth'] = CDACTopPlateHrzPathLength

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CDACUpperTopNode_Hrz_IA']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_CDAC_UpperHalf', 'SRF_DummyCaps', 'SRF_CapWtShield4DCAP', 'BND_Shield_VTC_M{}'.format(_CDAC_ShieldingLayer))
        target_coord = tmp1[0][0][0][0][0]['_XY_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CDACUpperTopNode_Hrz_IA')
        approaching_coord = tmp2[0][0]['_XY_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CDACUpperTopNode_Hrz_IA')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_CDACUpperTopNode_Hrz_IA']['_XYCoordinates'] = tmpXY


        ### BND_CDACTopPlate_Hrz_M7 (CDAC Top Node) Generation
        ## Comp Input Upper Half Node(Hrz, M7)
        ## Boundary_element Generation
        self._DesignParameter['BND_CDACUpperTopNode_Hrz_M7'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL7'][0],
        _Datatype=DesignParameters._LayerMapping['METAL7'][1],
        _XWidth=CDACTopPlateHrzPathLength,
        _YWidth=CDACTopPlateM7HrzPathWidth,
        _XYCoordinates=[[0,0]],
        )
        tmpXY=[]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_CDACUpperTopNode_Hrz_IA')
        target_coord = tmp1[0][0]['_XY_cent']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CDACUpperTopNode_Hrz_M7')
        approaching_coord = tmp2[0][0]['_XY_cent']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CDACUpperTopNode_Hrz_M7')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_CDACUpperTopNode_Hrz_M7']['_XYCoordinates'] = tmpXY


        ######################################################
        ## CDAC Top Node Via M8M9(IA->IB, Upper and Lower Node)
        ## Sref generation: ViaM8M9
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaM8toM9_YJH._ViaM8toM9_YJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CDACTopNode_ViaM8M9'] = \
            self._SrefElementDeclaration(_DesignObj=A02_ViaM8toM9_YJH._ViaM8toM9_YJH(_DesignParameter=None,
                                                                                     _Name='{}:SRF_CDACTopNode_ViaM8M9'.format(_Name)))[0]
        ## Define Sref Relection
        self._DesignParameter['SRF_CDACTopNode_ViaM8M9']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CDACTopNode_ViaM8M9']['_Angle'] = 0

        ## Calculate Sref XYcoord
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CDACTopNode_ViaM8M9']['_XYCoordinates'] = [[0, 0]]

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CDACTopNode_ViaM8M9']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_CDACLowerTopNode_Hrz_IA')
        target_coord = tmp1[0][0]['_XY_cent']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CDACTopNode_ViaM8M9', 'BND_Met9Layer')
        approaching_coord = tmp2[0][0][0]['_XY_cent']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CDACTopNode_ViaM8M9')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_CDACUpperTopNode_Hrz_IA')
        target_coord = tmp1[0][0]['_XY_cent']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CDACTopNode_ViaM8M9')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CDACTopNode_ViaM8M9']['_XYCoordinates'] = tmpXY


        ## Comp Input Vtc IB
        ## Boundary_element Generation
        self._DesignParameter['BND_CDACTopNode_Vtc_IB'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL9'][0],
        _Datatype=DesignParameters._LayerMapping['METAL9'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        CDACTopPlateVtcPathWidth = 2000
        self._DesignParameter['BND_CDACTopNode_Vtc_IB']['_XWidth'] = CDACTopPlateVtcPathWidth

                ## Define Boundary_element _XWidth
        # tmp1 = self.get_param_KJH4('BND_CDACFold1_B{}_DrvOutput_Vtc_M2'.format(1))
        tmp1 = self.get_param_KJH4('SRF_CDACTopNode_ViaM8M9', 'BND_Met9Layer')
        # self._DesignParameter['BND_CDACTopNode_Vtc_IB']['_YWidth'] = tmp1[0][0]['_Ywidth']
        self._DesignParameter['BND_CDACTopNode_Vtc_IB']['_YWidth'] = abs(tmp1[0][0][0]['_XY_down'][1] - tmp1[-1][0][0]['_XY_up'][1])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CDACTopNode_Vtc_IB']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmpX_2 = self.get_param_KJH4('SRF_CDAC_LowerHalf', 'SRF_CapArray', 'SRF_DummyCaps', 'SRF_CapWtShield4DCAP', 'BND_Shield_VTC_M{}'.format(_CDAC_ShieldingLayer))
        tmpY = self.get_param_KJH4('SRF_CDAC_LowerHalf', 'SRF_CapArray', 'SRF_Dummy_UCAP', 'BND_Shield_Extend_VTC_M{}'.format(_CDAC_ShieldingLayer))
        target_coord = tmpY[0][0][0][0][0]['_XY_up']
        target_coord[0] = int((tmpX_2[0][0][0][0][0][0]['_XY_left'][0] + tmpX_2[0][0][-1][0][-1][0]['_XY_right'][0])/2)
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CDACTopNode_Vtc_IB')
        approaching_coord = tmp2[0][0]['_XY_cent']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CDACTopNode_Vtc_IB')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_CDACTopNode_Vtc_IB']['_XYCoordinates'] = tmpXY


        #############################
        ## CDAC Top Node Via M7M8(M7 >IA, Upper and Lower Node)
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 7
        _Caculation_Parameters['_Layer2'] = 8

        tmp1 = self.get_param_KJH4('BND_CDACLowerTopNode_Hrz_IA')
        _COX = int((tmp1[0][0]['_Xwidth'] - (2 * _DRCObj._VIAzMinEnclosureByMetxOrMetyTwoOppositeSide - _DRCObj._VIAzMinWidth)) / (_DRCObj._VIAzMinWidth + _DRCObj._VIAzMinSpace))
        _COY = int((tmp1[0][0]['_Ywidth'] - (2 * _DRCObj._VIAzMinEnclosureByMetxOrMetyTwoOppositeSide - _DRCObj._VIAzMinWidth)) / (_DRCObj._VIAzMinWidth + _DRCObj._VIAzMinSpace))
        _Caculation_Parameters['_COX'] = max(_COX, 1)
        _Caculation_Parameters['_COY'] = max(_COY, 1)

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CDACTopNode_ViaM7M8'] = \
            self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                                                     _Name='{}:SRF_CDACTopNode_ViaM7M8'.format(_Name)))[0]
        ## Define Sref Relection
        self._DesignParameter['SRF_CDACTopNode_ViaM7M8']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CDACTopNode_ViaM7M8']['_Angle'] = 0

        ## Calculate Sref XYcoord
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CDACTopNode_ViaM7M8']['_XYCoordinates'] = [[0, 0]]

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CDACTopNode_ViaM7M8']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_CDACLowerTopNode_Hrz_IA')
        target_coord = tmp1[0][0]['_XY_cent']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CDACTopNode_ViaM7M8', 'SRF_ViaM7M8', 'BND_Met7Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CDACTopNode_ViaM7M8')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_CDACUpperTopNode_Hrz_IA')
        target_coord = tmp1[0][0]['_XY_cent']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CDACTopNode_ViaM7M8')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CDACTopNode_ViaM7M8']['_XYCoordinates'] = tmpXY


        # BND_TopPlateInput_Hrz_M7 generation
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_TopPlateInput_Hrz_M7'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL7'][0],
        _Datatype=DesignParameters._LayerMapping['METAL7'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_TopPlateInput_Hrz_M7']['_YWidth'] = CDACTopPlateM7HrzPathWidth

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('BND_CDACUpperTopNode_Hrz_M7')
        tmp2 = self.get_param_KJH4('BND_CDACFold1_B{}_DrvOutput_Vtc_M2'.format(_NumOfBits - 1))
        self._DesignParameter['BND_TopPlateInput_Hrz_M7']['_XWidth'] = abs(tmp1[0][0]['_XY_right'][0] - tmp2[0][0]['_XY_left'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_TopPlateInput_Hrz_M7']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate1
                            ## Target_coord: _XY_type1
        target_coord = tmp1[0][0]['_XY_up_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_TopPlateInput_Hrz_M7')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_TopPlateInput_Hrz_M7')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

                        ## Calculate2
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_CDACLowerTopNode_Hrz_M7')
        target_coord = tmp1[0][0]['_XY_up_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_TopPlateInput_Hrz_M7')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_TopPlateInput_Hrz_M7')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

                            ## Define coordinates
        self._DesignParameter['BND_TopPlateInput_Hrz_M7']['_XYCoordinates'] = tmpXY


        # BND_TopPlateInput_Vtc_M7 generation
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CDACTopNode_Vtc_M7'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL7'][0],
        _Datatype=DesignParameters._LayerMapping['METAL7'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_TopPlateInput_Hrz_M7')
        self._DesignParameter['BND_CDACTopNode_Vtc_M7']['_YWidth'] = abs(tmp1[0][0]['_XY_up'][1] - tmp1[1][0]['_XY_down'][1])

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CDACTopNode_Vtc_M7']['_XWidth'] = 400

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CDACTopNode_Vtc_M7']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate1
                            ## Target_coord: _XY_type1
        target_coord = tmp1[0][0]['_XY_up_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CDACTopNode_Vtc_M7')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CDACTopNode_Vtc_M7')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

                            ## Define coordinates
        self._DesignParameter['BND_CDACTopNode_Vtc_M7']['_XYCoordinates'] = tmpXY


        ## CDAC Driver Input Node for Routing
        ## Boundary Element Generation
        tmpXY0 = []
        for i in range(_NumOfBits):
            flag = 'Lo'
            self._DesignParameter['BND_CDACFold1_{}B{}_DrvInput_Hrz_M3'.format(flag, _NumOfBits - 1 - i)] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
            )
                    ## Define Boundary_element _YWidth
            CapSize = 2 ** (_NumOfBits - 1 -  i)
            tmp2 = self.get_param_KJH4('SRF_CDAC_LowerHalf','SRF_DriverArray','BND_{}C_Driver_Input_Hrz_M3'.format(CapSize))
            self._DesignParameter['BND_CDACFold1_{}B{}_DrvInput_Hrz_M3'.format(flag, _NumOfBits - 1- i)]['_YWidth'] = tmp2[0][0][0][0]['_Ywidth']

                    ## Define Boundary_element _XWidth
            ## Target1_coord: _XY_type1
            self._DesignParameter['BND_CDACFold1_{}B{}_DrvInput_Hrz_M3'.format(flag, _NumOfBits - 1- i)]['_XWidth'] = tmp2[0][0][0][0]['_Xwidth']


                    ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_CDACFold1_{}B{}_DrvInput_Hrz_M3'.format(flag, _NumOfBits - 1- i)]['_XYCoordinates'] = [[0, 0]]

            ## Lower쪽의 Y위치를 타겟으로 한 번, Upper에서 한 번 더 tmpXY에 append하여 두 좌표를 인덱스에 넣음
            ## Calculate Sref XYcoord
            tmpXY = []
            ## Calculate
            ## Target1_coord: _XY_type1
            target_coord = tmp2[0][0][0][0]['_XY_down_left']

            ## Approaching_coord: _XY_type2
            tmp5 = self.get_param_KJH4('BND_CDACFold1_{}B{}_DrvInput_Hrz_M3'.format(flag, _NumOfBits - 1- i))
            approaching_coord = tmp5[0][0]['_XY_down_left']

            ## Sref coord
            Scoord = tmp5[0][0]['_XY_origin']

            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

            ## Define coordinates
            self._DesignParameter['BND_CDACFold1_{}B{}_DrvInput_Hrz_M3'.format(flag, _NumOfBits - 1- i)]['_XYCoordinates'] = tmpXY


        # del(self._DesignParameter['SRF_CDAC_UpperHalf']['_DesignObj']._DesignParameter['SRF_DummyUCAP_Bottom_ViaM5M6']['_DesignObj']._DesignParameter['SRF_ViaM5M6']['_DesignObj']._DesignParameter['BND_COLayer'])
        # del(self._DesignParameter['SRF_CDAC_UpperHalf']['_DesignObj']._DesignParameter['SRF_DummyUCAP_Bottom_ViaM5M6']['_DesignObj']._DesignParameter['SRF_ViaM5M6']['_DesignObj']._DesignParameter['BND_Met5Layer'])

        ## CALCULATION END
        print('##############################################')
        print('##    CDAC With Driver (folded1, Driver Arranged Ver.) Calculation_END    ##')
        print('##############################################')


############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_YJH
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ADC_H02_CDAC_Driver_Gen4Routing'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'H02_00_CDACWDriver_Fold1_10bit_sh1'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        _NumOfBits=10,   # 5 이상
        _CDAC_BotNodeVtcExtensionMetalLayer=2,
        # # # Element CDAC
        # _CDAC_LayoutOption=[3, 4, 5, 6],
        # _CDAC_ShieldingLayer=2,  # Poly:0, M1:1, M2:2 ...
        # _CDAC_MetalWidth=50,
        # _CDAC_MetalLength=5770,  # (8bit size: 1414/ 10bit size: 2800/ 12bit size: 4200)
        # _CDAC_MetalSpacing=50,
        #
        # # #Unit Cap
        # _CDAC_NumOfElement=1,  # (매우 복잡..) Driver Common Centroid가 아니면 1// 맞으면 2
        #
        # # # Shielding & Top Connect node
        # _CDAC_ConnectLength=400,
        # _CDAC_ExtendLength=400,
        #
        # # # Dummy Cap Option
        # _CDAC_DummyCap_TopBottomShort=None,
        # # True => Top - Bottom Short, False -> Bottom = GND, None => Floating Bottom Node
        # _CDAC_NumOfDummyCaps=10,  # Number of dummy cap(one side)
        #
        # # # CommonCentroid With Driving node
        # _CDAC_CapArrayWDrivingNodeDistance=1500,  # DRC Rule
        # _CDAC_DriveNodeDistance=279,  #
        # _CDAC_YWidth_Bottom_Hrz=50,
        #
        # # Driver Sizing
        # _Driver_SizeByBit=[64, 64, 64, 64, 64, 64, 32, 16, 8, 4, 2, 1],  # Drv.CCPlacement == False일때 사용됨.
        #
        # # Driver(Inverter) NMOS
        # _Driver_NMOS_NumberofGate=1,  # number
        # _Driver_NMOS_ChannelWidth=400,  # number (8bit size: 340/ 10bit size: 680/ 12bit size: 1020)
        # _Driver_NMOS_Channellength=30,  # number
        # _Driver_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        #
        # # Driver(Inverter) PMOS
        # _Driver_PMOS_NumberofGate=1,  # number
        # _Driver_PMOS_ChannelWidth=800,  # number (8bit size: 900/ 10bit size: 1800/ 12bit size: 2700)
        # _Driver_PMOS_Channellength=30,  # number
        # _Driver_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT

        # # Element CDAC
        _CDAC_LayoutOption=[3, 4, 5, 6],
        _CDAC_ShieldingLayer=1,  # Poly:0, M1:1, M2:2 ...
        _CDAC_MetalWidth=50,
        _CDAC_MetalLength=2920,  # (8bit size: 1414/ 10bit size: 2800/ 12bit size: 4200)
        _CDAC_MetalSpacing=50,

        # #Unit Cap
        _CDAC_NumOfElement=1,  # (매우 복잡..) Driver Common Centroid가 아니면 1// 맞으면 2

        # # Shielding & Top Connect node
        _CDAC_ConnectLength=400,
        _CDAC_ExtendLength=400,

        # # Dummy Cap Option
        _CDAC_DummyCap_TopBottomShort=None,
        # True => Top - Bottom Short, False -> Bottom = GND, None => Floating Bottom Node
        _CDAC_NumOfDummyCaps=10,  # Number of dummy cap(one side)

        # # CommonCentroid With Driving node
        _CDAC_CapArrayWDrivingNodeDistance=1500,  # DRC Rule
        _CDAC_DriveNodeDistance=279,  #
        _CDAC_YWidth_Bottom_Hrz=50,

        # Driver Sizing
        _Driver_SizeByBit=[128, 128, 128, 64, 32, 16, 8, 4, 2, 1],  # Drv.CCPlacement == False일때 사용됨.

        # Driver(Inverter) NMOS
        _Driver_NMOS_NumberofGate=1,  # number
        _Driver_NMOS_ChannelWidth=400,  # number (8bit size: 340/ 10bit size: 680/ 12bit size: 1020)
        _Driver_NMOS_Channellength=30,  # number
        _Driver_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT

        # Driver(Inverter) PMOS
        _Driver_PMOS_NumberofGate=1,  # number
        _Driver_PMOS_ChannelWidth=800,  # number (8bit size: 900/ 10bit size: 1800/ 12bit size: 2700)
        _Driver_PMOS_Channellength=30,  # number
        _Driver_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
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
    LayoutObj = _CDACWtDriverFold1(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('###############      Sending to FTP Server...      ##################')
    My = MyInfo_YJH.USER(DesignParameters._Technology)
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
