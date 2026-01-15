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
from KJH91_Projects.Project_ADC.Layoutgen_code.H02_CDACWtDriver_YJH_RCHybrid import H02_00_CDACWtDriver



############################################################################################################################################################ Class_HEADER
class _CDACWtDriver_Unfolded(StickDiagram_KJH1._StickDiagram_KJH):
    ##########################################################################################################################
    # Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(
        _NumOfBits=5,

        # # Element CDAC
        _CDAC_LayoutOption=[5,6],
        _CDAC_ShieldingLayer=1,  # Poly:0, M1:1, M2:2 ...
        _CDAC_BotNodeVtcExtensionMetalLayer=2,
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

        # Driver Sizing
        _Driver_SizeByBit=[32, 16, 8, 4, 2],

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
                                  _NumOfBits=5,

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
                                  _Driver_SizeByBit=[32, 16, 8, 4, 2],

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
        CDACWtDriver_Unfolded_start_time = time.time()
        print('##############################################')
        print('##    CDAC With Driver Calculation_Start    ##')
        print('##############################################')

        ## H02_00_CDACWDriver (SREF) Generation
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters0 = copy.deepcopy(H02_00_CDACWtDriver._CDACWtDriver._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters0['_NumOfBits'] = _NumOfBits
        _Caculation_Parameters0['_CDAC_LayoutOption'] = _CDAC_LayoutOption
        _Caculation_Parameters0['_CDAC_ShieldingLayer'] = _CDAC_ShieldingLayer
        _Caculation_Parameters0['_CDAC_BotNodeVtcExtensionMetalLayer'] =_CDAC_BotNodeVtcExtensionMetalLayer
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
        self._DesignParameter['SRF_CDACWtDriver'] = self._SrefElementDeclaration(_DesignObj=H02_00_CDACWtDriver._CDACWtDriver(_DesignParameter=None,_Name='{}:SRF_CDACWtDriver'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_CDACWtDriver']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CDACWtDriver']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CDACWtDriver']['_DesignObj']._CalculateDesignParameter(
            **_Caculation_Parameters0)

        ## initialize Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CDACWtDriver']['_XYCoordinates'] = [[0, 0]]



        ### BND_CDACTopPlate_Hrz_M7 (CDAC Top Node) Generation
        ## CTop -> Comp Input Node(Hrz, M7)
        ## Boundary_element Generation
        self._DesignParameter['BND_CDACTopNode_Hrz_M7'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL7'][0],
        _Datatype=DesignParameters._LayerMapping['METAL7'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        CDACTopPlateHrzPathWidth = 400
        self._DesignParameter['BND_CDACTopNode_Hrz_M7']['_YWidth'] = CDACTopPlateHrzPathWidth

                ## Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH4('SRF_CDACWtDriver', 'SRF_CapArray', 'SRF_DummyCaps', 'SRF_CapWtShield4DCAP', 'BND_Shield_VTC_M{}'.format(_CDAC_ShieldingLayer))
        CDACTopPlateHrzPathLength = abs(tmp2[0][0][0][0][0][0]['_XY_left'][0] - tmp2[0][0][-1][0][-1][0]['_XY_right'][0])
        self._DesignParameter['BND_CDACTopNode_Hrz_M7']['_XWidth'] = CDACTopPlateHrzPathLength

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CDACTopNode_Hrz_M7']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate
                            ## Target_coord: _XY_type1
        # tmp1 = self.get_param_KJH4('SRF_CDAC_LowerHalf', 'SRF_CapArray', 'SRF_CommonArray',\
        #                            'SRF_CDAC_B{}'.format(_NumOfBits - 1 - 1), 'BND_Shield_VTC_M{}'.format(_CDAC_ShieldingLayer))
        target_coord = tmp2[0][0][0][0][0][0]['_XY_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CDACTopNode_Hrz_M7')
        approaching_coord = tmp2[0][0]['_XY_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CDACTopNode_Hrz_M7')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_CDACTopNode_Hrz_M7']['_XYCoordinates'] = tmpXY


        ### BND_CDACTopPlate_Hrz_M7 (CDAC Top Node) Generation
        ## CTop -> Comp Input Node(Hrz, M7)
        ## Boundary_element Generation
        self._DesignParameter['BND_CDACTopNode_Hrz_IA'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL8'][0],
        _Datatype=DesignParameters._LayerMapping['METAL8'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('BND_CDACTopNode_Hrz_M7')
        self._DesignParameter['BND_CDACTopNode_Hrz_IA']['_YWidth'] = tmp[0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CDACTopNode_Hrz_IA']['_XWidth'] = tmp[0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_CDACTopNode_Hrz_IA']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp[0][0]['_XY_cent']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CDACTopNode_Hrz_IA')
        approaching_coord = tmp2[0][0]['_XY_cent']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CDACTopNode_Hrz_IA')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_CDACTopNode_Hrz_IA']['_XYCoordinates'] = tmpXY


        #### CDACTopNode Via M7M8
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 7
        _Caculation_Parameters['_Layer2'] = 8
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CDACTopNode_ViaM7M8'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_CDACTopNode_ViaM7M8'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CDACTopNode_ViaM7M8']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CDACTopNode_ViaM7M8']['_Angle'] = 0

        tmp1 = self.get_param_KJH4('BND_CDACTopNode_Hrz_IA')
        _COX = int((tmp1[0][0]['_Xwidth'] - (2 * _DRCObj._VIAzMinEnclosureByMetxOrMetyTwoOppositeSide - _DRCObj._VIAzMinWidth)) / (_DRCObj._VIAzMinWidth + _DRCObj._VIAzMinSpace))
        _COY = int((tmp1[0][0]['_Ywidth'] - (2 * _DRCObj._VIAzMinEnclosureByMetxOrMetyTwoOppositeSide - _DRCObj._VIAzMinWidth)) / (_DRCObj._VIAzMinWidth + _DRCObj._VIAzMinSpace))
        _Caculation_Parameters['_COX'] = max(_COX, 1)
        _Caculation_Parameters['_COY'] = max(_COY, 1)

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CDACTopNode_ViaM7M8']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CDACTopNode_ViaM7M8']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_CDACTopNode_Hrz_IA')
        target_coord = tmp1[0][0]['_XY_cent']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CDACTopNode_ViaM7M8','SRF_ViaM7M8','BND_Met7Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CDACTopNode_ViaM7M8')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CDACTopNode_ViaM7M8']['_XYCoordinates'] = tmpXY



        ## CALCULATION END
        print('##############################################')
        print('##    CDAC With Driver (Unfolded) Calculation_END    ##')
        print('##############################################')
        CDACWtDriver_Unfolded_end_time = time.time()
        self.CDACWtDriver_Unfolded_elapsed_time = CDACWtDriver_Unfolded_end_time - CDACWtDriver_Unfolded_start_time

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ZZ00_RcdacSar_H02_01_CDACWtDriver_Unfolded'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'H02_00_CDACWDriver_unfolded_test99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        _NumOfBits=5,

        # # Element CDAC
        _CDAC_LayoutOption=[3, 4],
        _CDAC_ShieldingLayer=1,  # Poly:0, M1:1, M2:2 ...
        _CDAC_BotNodeVtcExtensionMetalLayer=2,
        _CDAC_MetalWidth=50,
        _CDAC_MetalLength=2920,  # (8bit size: 1414/ 10bit size: 2800/ 12bit size: 4200)
        _CDAC_MetalSpacing=50,

        # #Unit Cap
        _CDAC_NumOfElement=4,

        # # Shielding & Top Connect node
        _CDAC_ConnectLength=400,
        _CDAC_ExtendLength=400,

        # # Dummy Cap Option
        _CDAC_DummyCap_TopBottomShort=None,  # False -> Bottom = GND
        _CDAC_NumOfDummyCaps=10,  # Number of dummy cap(one side)

        # # CommonCentroid With Driving node
        _CDAC_CapArrayWDrivingNodeDistance=2000,
        _CDAC_DriveNodeDistance=279,  #
        _CDAC_YWidth_Bottom_Hrz=50,

        # Driver Sizing
        _Driver_SizeByBit=[],

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
    LayoutObj = _CDACWtDriver_Unfolded(_DesignParameter=None, _Name=cellname)
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
