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
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaM8toM9_YJH
from KJH91_Projects.Project_ADC.Layoutgen_code.H05_CDACWtDriver_Unfold_Arranged_Fixed import H05_00_CDACWtDriver_Unfold_Arrange


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
        ## Option(Arragned Only)
        _CDACDrv_DesignatedEachSize = [8,4,2], # Vector, designates each driver size(multiples of Unit Drv size)
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
        ## Option(Arragned Only)
        _CDACDrv_DesignatedEachSize = [8,4,2], # Vector, designates each driver size(multiples of Unit Drv size)
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
        ################################################################################################################### Error
        ## Error Raise1
        # if len(_CDACDrv_DesignatedEachSize) != _NumOfBits:
        #     raise NotImplementedError(f"_CDACDrv_DesignatedEachSize != _NumOfBits !!!")

        ## Error Raise2
        if _NumOfBits<2:
            raise NotImplementedError(f"CapDAC folding NumOfBits > 2")

        ###################################################################################################################

        ## H02_00_CDACWDriver (SREF) Generation
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters0 = copy.deepcopy(H05_00_CDACWtDriver_Unfold_Arrange._CDACWtDriver._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters0['_NumOfBits'] = _NumOfBits
        ## CDAC
            ## CDAC Drv
                ## Unit DRv
                    ## Common
        _Caculation_Parameters0['_CDACDrv_XVT'] = _CDACDrv_XVT
                ## NMOS
        _Caculation_Parameters0['_CDACDrv_NMOS_NumberofGate'] = _CDACDrv_NMOS_NumberofGate
        _Caculation_Parameters0['_CDACDrv_NMOS_ChannelWidth'] = _CDACDrv_NMOS_ChannelWidth
        _Caculation_Parameters0['_CDACDrv_NMOS_ChannelLength'] = _CDACDrv_NMOS_ChannelLength
                ## PMOS
        _Caculation_Parameters0['_CDACDrv_PMOS_NumberofGate'] = _CDACDrv_PMOS_NumberofGate
        _Caculation_Parameters0['_CDACDrv_PMOS_ChannelWidth'] = _CDACDrv_PMOS_ChannelWidth
        _Caculation_Parameters0['_CDACDrv_PMOS_ChannelLength'] = _CDACDrv_PMOS_ChannelLength
                ## Option(Arranged Only)
        _Caculation_Parameters0['_CDACDrv_DesignatedEachSize'] = _CDACDrv_DesignatedEachSize
            ## CDAC
                ## Element CDAC
        _Caculation_Parameters0['_CDAC_LayoutOption'] = _CDAC_LayoutOption
        _Caculation_Parameters0['_CDAC_MetalWidth'] = _CDAC_MetalWidth
        _Caculation_Parameters0['_CDAC_MetalLength'] = _CDAC_MetalLength
        _Caculation_Parameters0['_CDAC_MetalSpacing'] = _CDAC_MetalSpacing
                ## Unit Cap
        _Caculation_Parameters0['_CDAC_NumOfElement'] = _CDAC_NumOfElement
                ## Shield
        _Caculation_Parameters0['_CDAC_ShieldingLayer'] = _CDAC_ShieldingLayer
        _Caculation_Parameters0['_CDAC_ConnectLength'] = _CDAC_ConnectLength
        _Caculation_Parameters0['_CDAC_ExtendLength'] = _CDAC_ExtendLength
                ## Dummy Cap Option
        _Caculation_Parameters0['_CDAC_NumOfDummyCaps'] = _CDAC_NumOfDummyCaps
        _Caculation_Parameters0['_CDAC_DummyCap_TopBottomShort'] = _CDAC_DummyCap_TopBottomShort
                ## CommonCentroid With Driving node
        _Caculation_Parameters0['_CDAC_CapArrayWDrivingNodeDistance'] = _CDAC_CapArrayWDrivingNodeDistance
        _Caculation_Parameters0['_CDAC_DriveNodeDistance'] = _CDAC_DriveNodeDistance
        _Caculation_Parameters0['_CDAC_YWidth_Bottom_Hrz'] = _CDAC_YWidth_Bottom_Hrz
        _Caculation_Parameters0['_CDAC_BotNodeVtcExtensionMetalLayer'] = _CDAC_BotNodeVtcExtensionMetalLayer

        #############
        ## Upper CDAC (Cap, Driver Array) Generation
        self._DesignParameter['SRF_CDACWtDriver'] = self._SrefElementDeclaration(_DesignObj=H05_00_CDACWtDriver_Unfold_Arrange._CDACWtDriver(_DesignParameter=None,_Name='{}:SRF_CDAC_LowerHalf'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_CDACWtDriver']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CDACWtDriver']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CDACWtDriver']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters0)

        ## initialize Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CDACWtDriver']['_XYCoordinates'] = [[0, 0]]

        ###################################################################################################################

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
        ###################################################################################################################

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
        ###################################################################################################################

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
    libname = 'Proj_ZZ01_H05_01_CDACWtDriver_UnFold_Arranged'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'H05_01_CDACWtDriver_UnFold_Arranged'
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
            _CDACDrv_NMOS_NumberofGate=1,  # Number
            _CDACDrv_NMOS_ChannelWidth = 145, #Number
            _CDACDrv_NMOS_ChannelLength = 30, #Number
            ## PMOS
            _CDACDrv_PMOS_NumberofGate=1,  # Number
            _CDACDrv_PMOS_ChannelWidth = 879, #Number
            _CDACDrv_PMOS_ChannelLength = 30, #Number
        ## Option(Arragned Only)
        _CDACDrv_DesignatedEachSize = [8,4,3,3,], # Vector, designates each driver size(multiples of Unit Drv size)
    ## CDAC
            ## Element CDAC
            _CDAC_LayoutOption=[3],  # Vector, Consecutive Number [3,4,5]
            _CDAC_MetalWidth=50,  # Number
            _CDAC_MetalLength=1410,  # Number (8bit size: 1414/ 10bit size: 2800/ 12bit size: 4200)
            _CDAC_MetalSpacing=50,  # Number

            ## Unit Cap
            _CDAC_NumOfElement=2,  # Number

            ## Shield
            _CDAC_ShieldingLayer=1,  # Poly:0, M1:1, M2:2 ...
            _CDAC_ConnectLength=411,  # Number
            _CDAC_ExtendLength=400,  # Number

            ## Dummy Cap Option
            _CDAC_NumOfDummyCaps=5,  # Number, Number of dummy cap(one side)
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
    # Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()

    print('#############################      Finished      ################################')
    print('{} Hours   {} minutes   {} seconds'.format(h, m, s))
# end of 'main():' ---------------------------------------------------------------------------------------------
