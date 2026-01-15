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
from KJH91_Projects.Project_ADC.Layoutgen_code.H01_CDAC_Driver_v2_YJH_RCHybrid import H01_00_DriverCell
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A07_NbodyContactPhyLen_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A07_NbodyContactPhyLen_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A08_PbodyContactPhyLen_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A08_PbodyContactPhyLen_KJH3


############################################################################################################################################################ Class_HEADER
class _DriverArray(StickDiagram_KJH1._StickDiagram_KJH):
    ##########################################################################################################################
    # Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(
        # NumOfDriverUnitsInDriverArray = 2^(_NumOfBits) - 1
        _NumOfBits=None,

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
                                  # NumOfDriverUnitsInDriverArray = 2^(_NumOfBits) - 1
                                  _NumOfBits=None,

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
                                  _Driver_PMOS_NumberofGate=2,  # number
                                  _Driver_PMOS_ChannelWidth=1000,  # number
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
                                  ):

        ## Class_HEADER: Pre Defined Parameter Before Calculation
        ## Load DRC library
        _DRCObj = DRC.DRC()
        ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']
        ## CALCULATION START
        DriverArray_start_time = time.time()
        print('#########################################')
        print('##    CDAC Driver Calculation_Start    ##')
        print('#########################################')

        # Pre-defined Design Value


        ## H01_00_DriverCell (SREF) Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters0 = copy.deepcopy(H01_00_DriverCell._DriverCell._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
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

        for i in range(_NumOfBits):
            CapSize = 2 ** (_NumOfBits - i - 1)
            print('#########################################')
            print('##    {}C Driver Calculation_Start     ##'.format(CapSize))
            print('#########################################')

            self._DesignParameter['SRF_{}C_DriverCell'.format(CapSize)] = self._SrefElementDeclaration(
                _DesignObj=H01_00_DriverCell._DriverCell(_DesignParameter=None, _Name='{}:SRF_{}C_DriverCell'.format(_Name, CapSize)))[0]

            ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
            self._DesignParameter['SRF_{}C_DriverCell'.format(CapSize)]['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_{}C_DriverCell'.format(CapSize)]['_Angle'] = 0

            ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_{}C_DriverCell'.format(CapSize)]['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters0)

            ## initialize Sref _XYcoordinate: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_{}C_DriverCell'.format(CapSize)]['_XYCoordinates'] = [[0, 0]]

            tmp1 = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'SRF_Driver_NMOS', 'BND_PODummyLayer')
            tmp2 = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'SRF_Driver_PMOS', 'BND_PODummyLayer')

            NMOSXwidth = abs(tmp1[0][0][-1][0]['_XY_right'][0] - tmp1[0][0][0][0]['_XY_left'][0])
            PMOSXwidth = abs(tmp2[0][0][-1][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0])
            if NMOSXwidth > PMOSXwidth:
                DistanceBtwTr = NMOSXwidth + 96  # DRC GR201 : minimum spacing btw poly dummy layer
            else:
                DistanceBtwTr = PMOSXwidth + 96

            ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
            ## j는 Tr. Index
            #tmp = self.get_param_KJH4('SRF_{}C_Driver_NMOS'.format(CapSize), 'BND_{}Layer'.format(_Driver_NMOS_XVT))
            #DistanceBtwTr = tmp[0][0][0]['_Xwidth']
            NumOfTr = CapSize
            #NumOfTr = 2 ** (_NumOfBits - i - 1)
            tmpXY = []
            for j in range(NumOfTr):
                # 시작점 : ((2 ** i) * DistanceBtwTr)
                # 복사/붙혀넣기 간격 : j * (2 ** (i+1)) * DistanceBtwTr
                tmp = [j * (2 ** (i+1)) * DistanceBtwTr + ((2 ** i) * DistanceBtwTr), 0]
                tmpXY.append(tmp)

            # Define coord
            self._DesignParameter['SRF_{}C_DriverCell'.format(CapSize)]['_XYCoordinates'] = tmpXY
            print('#########################################')
            print('##    {}C Driver Calculation_End       ##'.format(CapSize))
            print('#########################################')

            if i == 0:  #초기 MSB Driver생성 시 Body Contact과 XVT, NWELL, VREF 등 전체적으로 덮는 레이어를 generation함.
                ## Dummy Cell SRF Generation(Folded1 구조에서 Dummy Cell은 2개 나올텐데 그 중 하나는 1C(LSB) 드라이버가 된다!!!!)
                self._DesignParameter['SRF_Dummy_DriverCell'] = self._SrefElementDeclaration(
                    _DesignObj=H01_00_DriverCell._DriverCell(_DesignParameter=None,
                                                             _Name='{}:SRF_Dummy_DriverCell'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
                self._DesignParameter['SRF_Dummy_DriverCell']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_Dummy_DriverCell']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_Dummy_DriverCell']['_DesignObj']._CalculateDesignParameter(
                    **_Caculation_Parameters0)

                ## initialize Sref _XYcoordinate: ex)'_NMOS_POWER'
                tmpXY = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize))[-1][0]['_XY_origin']
                tmpXY[0] = tmpXY[0] + DistanceBtwTr

                ## Define Coordinates
                self._DesignParameter['SRF_Dummy_DriverCell']['_XYCoordinates'] = [tmpXY]


                ## N Body(PMOS Body) SRF Generation
                print('#########################################')
                print('##    PMOS Body Calculation_Start      ##')
                print('#########################################')
                _Caculation_Parameters = copy.deepcopy(A07_NbodyContactPhyLen_KJH3._NbodyContactPhyLen._ParametersForDesignCalculation)

                tmp = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'SRF_Driver_PMOS', 'BND_PODummyLayer')
                tmpDummy = self.get_param_KJH4('SRF_Dummy_DriverCell', 'SRF_Driver_PMOS', 'BND_PODummyLayer')
                _Caculation_Parameters['_Length'] = max(abs(tmp[0][0][0][0]['_XY_left'][0] - tmpDummy[0][-1][-1][0]['_XY_right'][0]), 3300)
                _Caculation_Parameters['_NumCont'] = 2
                _Caculation_Parameters['_Vtc_flag'] = False

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
                self._DesignParameter['SRF_PMOS_Body_Contact'] = self._SrefElementDeclaration(
                    _DesignObj=A07_NbodyContactPhyLen_KJH3._NbodyContactPhyLen(_DesignParameter=None,_Name='{}:SRF_PMOS_Body_Contact'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
                self._DesignParameter['SRF_PMOS_Body_Contact']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_PMOS_Body_Contact']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_PMOS_Body_Contact']['_DesignObj']._CalculateDesignParameter(
                    **_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
                tmpXY = []
                ## initialized Sref coordinate
                self._DesignParameter['SRF_PMOS_Body_Contact']['_XYCoordinates'] = [[0, 0]]

                ## Calculate
                ## Target_coord: _XY_type1
                tmp1 = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'SRF_Driver_PMOS', 'BND_{}Layer'.format(_Driver_PMOS_XVT))
                target_coord = [int((tmp1[0][0][0][0]['_XY_left'][0] + tmpDummy[0][-1][-1][0]['_XY_right'][0])/2), tmp1[0][0][0][0]['_XY_up'][1]]

                ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('SRF_PMOS_Body_Contact', 'SRF_NbodyContactPhyLen', 'BND_ODLayer')
                approaching_coord = tmp2[0][0][0][0]['_XY_down']

                ## Sref coord
                tmp3 = self.get_param_KJH4('SRF_PMOS_Body_Contact')
                Scoord = tmp3[0][0]['_XY_origin']
                SpaceingODBtwNMOSArray = 100
                Scoord[1] = Scoord[1] + max(SpaceingODBtwNMOSArray, _DRCObj._OdMinSpace3)

                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)

                ## Define Coordinates
                self._DesignParameter['SRF_PMOS_Body_Contact']['_XYCoordinates'] = tmpXY


                ## P Body(NMOS Body) SRF Generation
                print('#########################################')
                print('##    NMOS Body Calculation_Start      ##')
                print('#########################################')
                _Caculation_Parameters = copy.deepcopy(A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen._ParametersForDesignCalculation)
                tmp = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'SRF_Driver_NMOS', 'BND_PODummyLayer')
                _Caculation_Parameters['_Length'] = max(abs(tmp[0][0][0][0]['_XY_left'][0] - tmpDummy[0][-1][-1][0]['_XY_right'][0]), 3300)
                _Caculation_Parameters['_NumCont'] = 2
                _Caculation_Parameters['_Vtc_flag'] = False

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
                self._DesignParameter['SRF_NMOS_Body_Contact'] = self._SrefElementDeclaration(
                    _DesignObj=A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen(_DesignParameter=None,_Name='{}:SRF_NMOS_Body_Contact'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
                self._DesignParameter['SRF_NMOS_Body_Contact']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_NMOS_Body_Contact']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_NMOS_Body_Contact']['_DesignObj']._CalculateDesignParameter(
                    **_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
                tmpXY = []
                ## initialized Sref coordinate
                self._DesignParameter['SRF_NMOS_Body_Contact']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                ## Target_coord: _XY_type1
                tmp1 = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'SRF_Driver_NMOS', 'BND_{}Layer'.format(_Driver_PMOS_XVT))
                target_coord = [int((tmp1[0][0][0][0]['_XY_left'][0] + tmpDummy[0][-1][-1][0]['_XY_right'][0])/2), tmp1[0][0][0][0]['_XY_down'][1]]

                ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('SRF_NMOS_Body_Contact', 'SRF_PbodyContactPhyLen', 'BND_ODLayer')
                approaching_coord = tmp2[0][0][0][0]['_XY_up']

                ## Sref coord
                tmp3 = self.get_param_KJH4('SRF_NMOS_Body_Contact')
                Scoord = tmp3[0][0]['_XY_origin']
                SpaceingODBtwNMOSArray = 100
                Scoord[1] = Scoord[1] - max(SpaceingODBtwNMOSArray, _DRCObj._OdMinSpace2Pp)

                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)

                ## Define Coordinates
                self._DesignParameter['SRF_NMOS_Body_Contact']['_XYCoordinates'] = tmpXY


                # NWELL Boundary generation
                print('#########################################')
                print('##      NWELL Calculation_Start        ##')
                print('#########################################')
                ## Boundary_element Generation
                self._DesignParameter['BND_NWELL'] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['NWELL'][0],
                    _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                    _XWidth=None,
                    _YWidth=None,
                    _XYCoordinates=[],
                )
                ## Define Boundary_element _YWidth
                tmp0 = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'SRF_Driver_PMOS', 'BND_{}Layer'.format(_Driver_PMOS_XVT))
                tmp1 = self.get_param_KJH4('SRF_PMOS_Body_Contact', 'SRF_NbodyContactPhyLen', 'BND_Nwell')
                self._DesignParameter['BND_NWELL']['_YWidth'] = abs(
                    tmp1[0][0][0][0]['_XY_up'][1] - tmp0[0][0][0][0]['_XY_down'][1]) + _DRCObj._NwMinEnclosurePactive

                ## Define Boundary_element _XWidth
                self._DesignParameter['BND_NWELL']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']

                ## Calculate Sref XYcoord
                tmpXY = []
                ## initialized Sref coordinate
                self._DesignParameter['BND_NWELL']['_XYCoordinates'] = [[0, 0]]

                ## Calculate
                ## Target_coord: _XY_type1
                target_coord = tmp1[0][0][0][0]['_XY_up_left']

                ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('BND_NWELL')
                approaching_coord = tmp2[0][0]['_XY_up_left']

                ## Sref coord
                Scoord = tmp2[0][0]['_XY_origin']

                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
                ## Define coordinates
                self._DesignParameter['BND_NWELL']['_XYCoordinates'] = tmpXY


                # PMOS PP Layer generation
                print('#############################################')
                print('##     PMOS BP Layer Calculation_Start     ##')
                print('#############################################')
                ## Boundary_element Generation
                self._DesignParameter['BND_PMOSArray_PPLayer'] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['PIMP'][0],
                    _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                    _XWidth=None,
                    _YWidth=None,
                    _XYCoordinates=[],
                )
                ## Define Boundary_element _YWidth
                tmp0 = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'SRF_Driver_PMOS', 'BND_PPLayer')
                tmp1 = self.get_param_KJH4('SRF_Dummy_DriverCell', 'SRF_Driver_PMOS', 'BND_PPLayer')
                self._DesignParameter['BND_PMOSArray_PPLayer']['_YWidth'] = tmp0[0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
                self._DesignParameter['BND_PMOSArray_PPLayer']['_XWidth'] = abs(
                    tmp0[0][0][0][0]['_XY_left'][0] - tmp1[0][0][0][0]['_XY_right'][0])

                ## Calculate Sref XYcoord
                tmpXY = []
                ## initialized Sref coordinate
                self._DesignParameter['BND_PMOSArray_PPLayer']['_XYCoordinates'] = [[0, 0]]

                ## Calculate
                ## Target_coord: _XY_type1
                target_coord = tmp0[0][0][0][0]['_XY_up_left']

                ## Approaching_coord: _XY_type2
                tmp1 = self.get_param_KJH4('BND_PMOSArray_PPLayer')
                approaching_coord = tmp1[0][0]['_XY_up_left']

                ## Sref coord
                Scoord = tmp1[0][0]['_XY_origin']

                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
                ## Define coordinates
                self._DesignParameter['BND_PMOSArray_PPLayer']['_XYCoordinates'] = tmpXY


                # XVT Layer Boundary generation
                print('#########################################')
                print('##  PMOS XVT Layer Calculation_Start   ##')
                print('#########################################')
                # PMOS XVT Layer generation
                ## Boundary_element Generation
                self._DesignParameter['BND_PMOSArray_{}Layer'.format(_Driver_PMOS_XVT)] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping[_Driver_PMOS_XVT][0],
                    _Datatype=DesignParameters._LayerMapping[_Driver_PMOS_XVT][1],
                    _XWidth=None,
                    _YWidth=None,
                    _XYCoordinates=[],
                )
                ## Define Boundary_element _YWidth
                tmp0 = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'SRF_Driver_PMOS', 'BND_{}Layer'.format(_Driver_PMOS_XVT))
                tmp1 = self.get_param_KJH4('SRF_Dummy_DriverCell', 'SRF_Driver_PMOS', 'BND_{}Layer'.format(_Driver_PMOS_XVT))
                self._DesignParameter['BND_PMOSArray_{}Layer'.format(_Driver_PMOS_XVT)]['_YWidth'] = tmp0[0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
                self._DesignParameter['BND_PMOSArray_{}Layer'.format(_Driver_PMOS_XVT)]['_XWidth'] = abs(tmp0[0][0][0][0]['_XY_left'][0] - tmp1[0][0][0][0]['_XY_right'][0])

                ## Calculate Sref XYcoord
                tmpXY = []
                ## initialized Sref coordinate
                self._DesignParameter['BND_PMOSArray_{}Layer'.format(_Driver_PMOS_XVT)]['_XYCoordinates'] = [[0, 0]]

                ## Calculate
                ## Target_coord: _XY_type1
                target_coord = tmp0[0][0][0][0]['_XY_up_left']

                ## Approaching_coord: _XY_type2
                tmp1 = self.get_param_KJH4('BND_PMOSArray_{}Layer'.format(_Driver_PMOS_XVT))
                approaching_coord = tmp1[0][0]['_XY_up_left']

                ## Sref coord
                Scoord = tmp1[0][0]['_XY_origin']

                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
                ## Define coordinates
                self._DesignParameter['BND_PMOSArray_{}Layer'.format(_Driver_PMOS_XVT)]['_XYCoordinates'] = tmpXY


                # NMOS XVT Layer generation
                print('#########################################')
                print('##  NMOS XVT Layer Calculation_Start   ##')
                print('#########################################')
                ## Boundary_element Generation
                self._DesignParameter['BND_NMOSArray_{}Layer'.format(_Driver_NMOS_XVT)] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping[_Driver_NMOS_XVT][0],
                    _Datatype=DesignParameters._LayerMapping[_Driver_NMOS_XVT][1],
                    _XWidth=None,
                    _YWidth=None,
                    _XYCoordinates=[],
                )
                ## Define Boundary_element _YWidth
                tmp0 = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'SRF_Driver_NMOS', 'BND_{}Layer'.format(_Driver_NMOS_XVT))
                tmp1 = self.get_param_KJH4('SRF_Dummy_DriverCell'.format(CapSize), 'SRF_Driver_NMOS', 'BND_{}Layer'.format(_Driver_NMOS_XVT))
                self._DesignParameter['BND_NMOSArray_{}Layer'.format(_Driver_NMOS_XVT)]['_YWidth'] = tmp0[0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
                self._DesignParameter['BND_NMOSArray_{}Layer'.format(_Driver_NMOS_XVT)]['_XWidth'] = abs(tmp0[0][0][0][0]['_XY_left'][0] - tmp1[0][0][0][0]['_XY_right'][0])

                ## Calculate Sref XYcoord
                tmpXY = []
                ## initialized Sref coordinate
                self._DesignParameter['BND_NMOSArray_{}Layer'.format(_Driver_NMOS_XVT)]['_XYCoordinates'] = [[0, 0]]

                ## Calculate
                ## Target_coord: _XY_type1
                target_coord = tmp0[0][0][0][0]['_XY_up_left']

                ## Approaching_coord: _XY_type2
                tmp1 = self.get_param_KJH4('BND_NMOSArray_{}Layer'.format(_Driver_NMOS_XVT))
                approaching_coord = tmp1[0][0]['_XY_up_left']

                ## Sref coord
                Scoord = tmp1[0][0]['_XY_origin']

                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
                ## Define coordinates
                self._DesignParameter['BND_NMOSArray_{}Layer'.format(_Driver_NMOS_XVT)]['_XYCoordinates'] = tmpXY



                ## VREF Hrz Metal (M6) Generation
                print('###################################################')
                print('##   NMOS Source<-> VREFN M6 Calculation_Start   ##')
                print('###################################################')
                # VREFN Boundary generation
                ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
                self._DesignParameter['BND_VREFN_Hrz_M6'] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['METAL6'][0],
                    _Datatype=DesignParameters._LayerMapping['METAL6'][1],
                    _XWidth=None,
                    _YWidth=None,
                    _XYCoordinates=[],
                )
                ## Define Boundary_element _YWidth
                VREFN_Hrz_M6_Minwidth = 244 # 비아당 컨택 두 개 박힐려면 최소 244 Ywidth가 필요함.
                tmp = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'SRF_NMOSSourceVREFN_ViaM2M6', 'SRF_ViaM5M6','BND_Met6Layer')
                tmp1 = self.get_param_KJH4('SRF_Dummy_DriverCell', 'SRF_NMOSSourceVREFN_ViaM2M6', 'SRF_ViaM5M6','BND_Met6Layer')
                self._DesignParameter['BND_VREFN_Hrz_M6']['_YWidth'] = min(max(VREFN_Hrz_M6_Minwidth, int(tmp[0][0][0][0][0]['_Ywidth'])), 4000)

                ## Define Boundary_element _XWidth
                self._DesignParameter['BND_VREFN_Hrz_M6']['_XWidth'] = abs(
                    tmp[0][0][0][0][0]['_XY_left'][0] - tmp1[0][-1][0][0][0]['_XY_right'][0])

                ## Calculate Sref XYcoord
                tmpXY = []

                ## initialized Sref coordinate
                self._DesignParameter['BND_VREFN_Hrz_M6']['_XYCoordinates'] = [[0, 0]]

                ## Calculate
                ## Target_coord: _XY_type1
                target_coord = tmp[0][0][0][0][0]['_XY_down_left']

                ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('BND_VREFN_Hrz_M6')
                approaching_coord = tmp2[0][0]['_XY_down_left']

                ## Sref coord
                Scoord = tmp2[0][0]['_XY_origin']

                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)

                ## Define coordinates
                self._DesignParameter['BND_VREFN_Hrz_M6']['_XYCoordinates'] = tmpXY


                # VREFP Boundary generation
                print('###################################################')
                print('##   PMOS Source<-> VREFP M6 Calculation_Start   ##')
                print('###################################################')
                ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
                self._DesignParameter['BND_VREFP_Hrz_M6'] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['METAL6'][0],
                    _Datatype=DesignParameters._LayerMapping['METAL6'][1],
                    _XWidth=None,
                    _YWidth=None,
                    _XYCoordinates=[],
                )
                ## Define Boundary_element _YWidth
                VREFN_Hrz_M6_Minwidth = 244 # 비아당 컨택 두 개 박힐려면 최소 244 Ywidth가 필요함.
                tmp = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'SRF_PMOSSourceVREFP_ViaM2M6', 'SRF_ViaM5M6','BND_Met6Layer')
                tmp1 = self.get_param_KJH4('SRF_Dummy_DriverCell', 'SRF_PMOSSourceVREFP_ViaM2M6', 'SRF_ViaM5M6','BND_Met6Layer')
                self._DesignParameter['BND_VREFP_Hrz_M6']['_YWidth'] = min(max(VREFN_Hrz_M6_Minwidth, int(tmp[0][0][0][0][0]['_Ywidth'])), 4000)

                ## Define Boundary_element _XWidth
                self._DesignParameter['BND_VREFP_Hrz_M6']['_XWidth'] = abs(
                    tmp[0][0][0][0][0]['_XY_left'][0] - tmp1[0][-1][0][0][0]['_XY_right'][0])

                ## Calculate Sref XYcoord
                tmpXY = []
                ## initialized Sref coordinate
                self._DesignParameter['BND_VREFP_Hrz_M6']['_XYCoordinates'] = [[0, 0]]

                ## Calculate
                ## Target_coord: _XY_type1
                target_coord = tmp[0][0][0][0][0]['_XY_down_left']

                ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('BND_VREFP_Hrz_M6')
                approaching_coord = tmp2[0][0]['_XY_down_left']

                ## Sref coord
                Scoord = tmp2[0][0]['_XY_origin']

                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)

                ## Define coordinates
                self._DesignParameter['BND_VREFP_Hrz_M6']['_XYCoordinates'] = tmpXY


            ## Input Node Horizontal Path (M3)
            print('#################################################')
            print('##      Input Node Path Calculation_Start      ##')
            print('#################################################')
            self._DesignParameter['BND_{}C_Driver_Input_Hrz_M3'.format(CapSize)] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL3'][0],
                _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )
            InputM3HrzPathWidth = 100
            InputM2VtcPathWidth = 50
            SpaceBtwInputHrzM3andNMOS = 300
            SpaceBtwInputHrzPaths = 100
            self._DesignParameter['BND_{}C_Driver_Input_Hrz_M3'.format(CapSize)]['_YWidth'] = InputM3HrzPathWidth

            ## Define Boundary_element _XWidth
            tmp = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'BND_Input_Node_Hrz_M2')

            self._DesignParameter['BND_{}C_Driver_Input_Hrz_M3'.format(CapSize)]['_XWidth'] = \
                max(abs(tmp[0][0][0]['_XY_left'][0] - tmp[-1][0][0]['_XY_left'][0]) + 244, 244) # 244는 컨택 두 개가 박힌 최소 비아 길이

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_{}C_Driver_Input_Hrz_M3'.format(CapSize)]['_XYCoordinates'] = [[0, 0]]

            ## Calculate
            tmpXY = []
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_NMOS_Body_Contact', 'SRF_PbodyContactPhyLen', 'BND_PPLayer')
            target_coord = [tmp[0][0][0]['_XY_left'][0], tmp1[0][0][0][0]['_XY_down'][1]]

            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_{}C_Driver_Input_Hrz_M3'.format(CapSize))
            approaching_coord = tmp2[0][0]['_XY_up_left']

            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_{}C_Driver_Input_Hrz_M3'.format(CapSize))
            Scoord = tmp3[0][0]['_XY_origin']
            Scoord[1] = Scoord[1] - SpaceBtwInputHrzM3andNMOS - (InputM3HrzPathWidth+SpaceBtwInputHrzPaths) * i

            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

            ## Define coordinates
            self._DesignParameter['BND_{}C_Driver_Input_Hrz_M3'.format(CapSize)]['_XYCoordinates'] = tmpXY


            ## Input Node Vertical Path (M2)
            self._DesignParameter['BND_{}C_Driver_Input_Vtc_M2'.format(CapSize)] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )
            tmp1_1 = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'BND_Input_Node_Hrz_M2')
            tmp1_2 = self.get_param_KJH4('BND_{}C_Driver_Input_Hrz_M3'.format(CapSize))
            self._DesignParameter['BND_{}C_Driver_Input_Vtc_M2'.format(CapSize)]['_YWidth'] = abs(tmp1_1[0][0][0]['_XY_up'][1] - tmp1_2[0][0]['_XY_cent'][1])

            ## Define Boundary_element _XWidth
            tmp = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'BND_Input_Node_Hrz_M2')

            self._DesignParameter['BND_{}C_Driver_Input_Vtc_M2'.format(CapSize)]['_XWidth'] = InputM2VtcPathWidth

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_{}C_Driver_Input_Vtc_M2'.format(CapSize)]['_XYCoordinates'] = [[0, 0]]

            ## Calculate
            tmpXY = []
            for i in range(CapSize):
                ## Target_coord: _XY_type1
                tmp1 = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'BND_Input_Node_Hrz_M2')
                target_coord = tmp1[i][0][0]['_XY_up_left']

                ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('BND_{}C_Driver_Input_Vtc_M2'.format(CapSize))
                approaching_coord = tmp2[0][0]['_XY_up_left']

                ## Sref coord
                Scoord = tmp2[0][0]['_XY_origin']

                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)

            ## Define coordinates
            self._DesignParameter['BND_{}C_Driver_Input_Vtc_M2'.format(CapSize)]['_XYCoordinates'] = tmpXY


            # Input Node Viastack M2M3 generation
            ## ViaM1M2 (PMOS Array Vtc Path M1 <-> Gate Hrz Path M2)
            ## Sref generation: ViaX
            ## Define ViaX Parameter
            _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
            _Caculation_Parameters['_Layer1'] = 2
            _Caculation_Parameters['_Layer2'] = 3
            _Caculation_Parameters['_COX'] = 2
            _Caculation_Parameters['_COY'] = 1

            self._DesignParameter['SRF_{}C_Driver_InputNode_ViaM2M3'.format(CapSize)] = \
                self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_{}C_Driver_InputNode_ViaM2M3'.format(_Name, CapSize)))[0]

            ## Define Sref Relection
            self._DesignParameter['SRF_{}C_Driver_InputNode_ViaM2M3'.format(CapSize)]['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
            self._DesignParameter['SRF_{}C_Driver_InputNode_ViaM2M3'.format(CapSize)]['_Angle'] = 0

            self._DesignParameter['SRF_{}C_Driver_InputNode_ViaM2M3'.format(CapSize)]['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            tmpXY = []
            for j in range(CapSize):
                ## Calculate Sref XYcoord
                ## initialized Sref coordinate
                self._DesignParameter['SRF_{}C_Driver_InputNode_ViaM2M3'.format(CapSize)]['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                ## Target_coord
                tmp1 = self.get_param_KJH4('BND_{}C_Driver_Input_Vtc_M2'.format(CapSize))
                target_coord = tmp1[j][0]['_XY_down_left']
                ## Approaching_coord
                tmp2 = self.get_param_KJH4('SRF_{}C_Driver_InputNode_ViaM2M3'.format(CapSize), 'SRF_ViaM2M3', 'BND_Met3Layer')
                approaching_coord = tmp2[0][0][0][0]['_XY_left']
                ## Sref coord
                tmp3 = self.get_param_KJH4('SRF_{}C_Driver_InputNode_ViaM2M3'.format(CapSize))
                Scoord = tmp3[0][0]['_XY_origin']
                ## Calculate
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
            ## Define
            self._DesignParameter['SRF_{}C_Driver_InputNode_ViaM2M3'.format(CapSize)]['_XYCoordinates'] = tmpXY

        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')
        DriverArray_end_time = time.time()
        self.DriverArray_elapsed_time = DriverArray_end_time - DriverArray_start_time

###############################################################################################################################################
########## ########## Fold One time ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########
    ############################################################################################################################################
    def _CalculateDesignParameterFold1(self,
                                  # NumOfDriverUnitsInDriverArray = 2^(_NumOfBits) - 1
                                  _NumOfBits=None,

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
                                  _Driver_PMOS_NumberofGate=2,  # number
                                  _Driver_PMOS_ChannelWidth=1000,  # number
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
                                  ):

        ## Class_HEADER: Pre Defined Parameter Before Calculation
        ## Load DRC library
        _DRCObj = DRC.DRC()
        ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']
        ## CALCULATION START
        DriverArray_start_time = time.time()

        print('#########################################')
        print('##    CDAC Driver Calculation_Start    ##')
        print('#########################################')

        # Pre-defined Design Value

        ## H01_00_DriverCell (SREF) Generation
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters0 = copy.deepcopy(H01_00_DriverCell._DriverCell._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters0['_Driver_NMOS_NumberofGate'] = _Driver_NMOS_NumberofGate
        _Caculation_Parameters0['_Driver_NMOS_ChannelWidth'] = _Driver_NMOS_ChannelWidth
        _Caculation_Parameters0['_Driver_NMOS_Channellength'] = _Driver_NMOS_Channellength
        _Caculation_Parameters0['_Driver_NMOS_GateSpacing'] = _Driver_NMOS_GateSpacing
        _Caculation_Parameters0['_Driver_NMOS_SDWidth'] = _Driver_NMOS_SDWidth
        _Caculation_Parameters0['_Driver_NMOS_XVT'] = _Driver_NMOS_XVT
        _Caculation_Parameters0['_Driver_NMOS_PCCrit'] = _Driver_NMOS_PCCrit
        _Caculation_Parameters0['_Driver_NMOS_Source_Via_TF'] = True  # default
        _Caculation_Parameters0['_Driver_NMOS_Drain_Via_TF'] = True
        _Caculation_Parameters0['_Driver_NMOS_Dummy'] = True  # default
        _Caculation_Parameters0['_Driver_NMOS_Dummy_length'] = _Driver_NMOS_Dummy_length
        _Caculation_Parameters0['_Driver_NMOS_Dummy_placement'] = _Driver_NMOS_Dummy_length
        _Caculation_Parameters0['_Driver_PMOS_NumberofGate'] = _Driver_PMOS_NumberofGate
        _Caculation_Parameters0['_Driver_PMOS_ChannelWidth'] = _Driver_PMOS_ChannelWidth
        _Caculation_Parameters0['_Driver_PMOS_Channellength'] = _Driver_PMOS_Channellength
        _Caculation_Parameters0['_Driver_PMOS_GateSpacing'] = _Driver_PMOS_GateSpacing
        _Caculation_Parameters0['_Driver_PMOS_SDWidth'] = _Driver_PMOS_SDWidth
        _Caculation_Parameters0['_Driver_PMOS_XVT'] = _Driver_PMOS_XVT
        _Caculation_Parameters0['_Driver_PMOS_PCCrit'] = _Driver_PMOS_PCCrit
        _Caculation_Parameters0['_Driver_PMOS_Source_Via_TF'] = True  # default
        _Caculation_Parameters0['_Driver_PMOS_Drain_Via_TF'] = True
        _Caculation_Parameters0['_Driver_PMOS_Dummy'] = True  # default
        _Caculation_Parameters0['_Driver_PMOS_Dummy_length'] = _Driver_PMOS_Dummy_length
        _Caculation_Parameters0['_Driver_PMOS_Dummy_placement'] = _Driver_PMOS_Dummy_placement

        for i in range(_NumOfBits):
            CapSize = 2 ** (_NumOfBits - i - 1)
            print('#########################################')
            print('##    {}C Driver Calculation_Start     ##'.format(CapSize))
            print('#########################################')

            self._DesignParameter['SRF_{}C_DriverCell'.format(CapSize)] = self._SrefElementDeclaration(
                _DesignObj=H01_00_DriverCell._DriverCell(_DesignParameter=None,
                                                         _Name='{}:SRF_{}C_DriverCell'.format(_Name, CapSize)))[0]

            ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
            self._DesignParameter['SRF_{}C_DriverCell'.format(CapSize)]['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_{}C_DriverCell'.format(CapSize)]['_Angle'] = 0

            ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_{}C_DriverCell'.format(CapSize)]['_DesignObj']._CalculateDesignParameter(
                **_Caculation_Parameters0)

            ## initialize Sref _XYcoordinate: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_{}C_DriverCell'.format(CapSize)]['_XYCoordinates'] = [[0, 0]]

            tmp1 = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'SRF_Driver_NMOS', 'BND_PODummyLayer')
            tmp2 = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'SRF_Driver_PMOS', 'BND_PODummyLayer')

            NMOSXwidth = abs(tmp1[0][0][-1][0]['_XY_right'][0] - tmp1[0][0][0][0]['_XY_left'][0])
            PMOSXwidth = abs(tmp2[0][0][-1][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0])
            if NMOSXwidth > PMOSXwidth:
                DistanceBtwTr = NMOSXwidth + 96  # DRC GR201 : minimum spacing btw poly dummy layer
            else:
                DistanceBtwTr = PMOSXwidth + 96

            ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
            ## j는 Tr. Index
            # tmp = self.get_param_KJH4('SRF_{}C_Driver_NMOS'.format(CapSize), 'BND_{}Layer'.format(_Driver_NMOS_XVT))
            # DistanceBtwTr = tmp[0][0][0]['_Xwidth']
            NumOfTr = CapSize
            # NumOfTr = 2 ** (_NumOfBits - i - 1)
            tmpXY = []
            for j in range(NumOfTr):
                # 시작점 : ((2 ** i) * DistanceBtwTr)
                # 복사/붙혀넣기 간격 : j * (2 ** (i+1)) * DistanceBtwTr
                tmp = [j * (2 ** (i + 1)) * DistanceBtwTr + ((2 ** i) * DistanceBtwTr), 0]
                tmpXY.append(tmp)

            # Define coord
            self._DesignParameter['SRF_{}C_DriverCell'.format(CapSize)]['_XYCoordinates'] = tmpXY
            print('#########################################')
            print('##    {}C Driver Calculation_End       ##'.format(CapSize))
            print('#########################################')

            if i == 0:  # 초기 MSB Driver생성 후, 최 좌측 DummyCell하나와 Body Contact과 XVT, NWELL, VREF 등 전체적으로 덮는 레이어를 generation함.
                ## Dummy Cell SRF Generation(Folded1 구조에서 Dummy Cell은 2개 나올텐데 그 중 하나는 1C(LSB) 드라이버가 된다!!!!)
                self._DesignParameter['SRF_Dummy_DriverCell'] = self._SrefElementDeclaration(
                    _DesignObj=H01_00_DriverCell._DriverCell(_DesignParameter=None,
                                                             _Name='{}:SRF_Dummy_DriverCell'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
                self._DesignParameter['SRF_Dummy_DriverCell']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_Dummy_DriverCell']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_Dummy_DriverCell']['_DesignObj']._CalculateDesignParameter(
                    **_Caculation_Parameters0)

                ## initialize Sref _XYcoordinate: ex)'_NMOS_POWER'
                tmpXY = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize))[-1][0]['_XY_origin']
                tmpXY[0] = tmpXY[0] + DistanceBtwTr

                ## Define Coordinates
                self._DesignParameter['SRF_Dummy_DriverCell']['_XYCoordinates'] = [tmpXY]


                ####################
                ## N Body(PMOS Body) SRF Generation
                print('#########################################')
                print('##    PMOS Body Calculation_Start      ##')
                print('#########################################')
                _Caculation_Parameters = copy.deepcopy(
                    A07_NbodyContactPhyLen_KJH3._NbodyContactPhyLen._ParametersForDesignCalculation)
                ## SRF P Body Contact Generation
                tmp = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'SRF_Driver_PMOS', 'BND_PODummyLayer')
                tmp_1 = self.get_param_KJH4('SRF_Dummy_DriverCell', 'SRF_Driver_PMOS', 'BND_PODummyLayer')
                _Caculation_Parameters['_Length'] = max(
                    abs(tmp[0][0][0][0]['_XY_left'][0] - tmp_1[0][0][-1][0]['_XY_right'][0]), 3300)
                _Caculation_Parameters['_NumCont'] = 2
                _Caculation_Parameters['_Vtc_flag'] = False

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
                self._DesignParameter['SRF_PMOS_Body_Contact'] = self._SrefElementDeclaration(
                    _DesignObj=A07_NbodyContactPhyLen_KJH3._NbodyContactPhyLen(_DesignParameter=None,
                                                                                    _Name='{}:SRF_PMOS_Body_Contact'.format(
                                                                                        _Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
                self._DesignParameter['SRF_PMOS_Body_Contact']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_PMOS_Body_Contact']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_PMOS_Body_Contact']['_DesignObj']._CalculateDesignParameter(
                    **_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
                tmpXY = []
                ## initialized Sref coordinate
                self._DesignParameter['SRF_PMOS_Body_Contact']['_XYCoordinates'] = [[0, 0]]

                ## Calculate
                ## Target_coord: _XY_type1
                tmp1 = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'SRF_Driver_PMOS',
                                           'BND_{}Layer'.format(_Driver_PMOS_XVT))
                tmp1_1 = self.get_param_KJH4('SRF_Dummy_DriverCell', 'SRF_Driver_PMOS', 'BND_{}Layer'.format(_Driver_PMOS_XVT))
                target_coord = [int((tmp1[0][0][0][0]['_XY_left'][0] + tmp1_1[-1][0][0][0]['_XY_right'][0]) / 2),
                                tmp1[0][0][0][0]['_XY_up'][1]]

                ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('SRF_PMOS_Body_Contact', 'SRF_NbodyContactPhyLen', 'BND_ODLayer')
                approaching_coord = tmp2[0][0][0][0]['_XY_down']

                ## Sref coord
                tmp3 = self.get_param_KJH4('SRF_PMOS_Body_Contact')
                Scoord = tmp3[0][0]['_XY_origin']
                SpaceingODBtwNMOSArray = 100
                Scoord[1] = Scoord[1] + max(SpaceingODBtwNMOSArray, _DRCObj._OdMinSpace3)

                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)

                ## Define Coordinates
                self._DesignParameter['SRF_PMOS_Body_Contact']['_XYCoordinates'] = tmpXY

                ## P Body(NMOS Body) SRF Generation
                print('#########################################')
                print('##    NMOS Body Calculation_Start      ##')
                print('#########################################')
                _Caculation_Parameters = copy.deepcopy(
                    A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen._ParametersForDesignCalculation)
                tmp = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'SRF_Driver_NMOS', 'BND_PODummyLayer')
                tmp_1 = self.get_param_KJH4('SRF_Dummy_DriverCell', 'SRF_Driver_PMOS', 'BND_PODummyLayer')
                _Caculation_Parameters['_Length'] = max(
                    abs(tmp[0][0][0][0]['_XY_left'][0] - tmp_1[0][0][-1][0]['_XY_right'][0]), 3300)
                _Caculation_Parameters['_NumCont'] = 2
                _Caculation_Parameters['_Vtc_flag'] = False

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
                self._DesignParameter['SRF_NMOS_Body_Contact'] = self._SrefElementDeclaration(
                    _DesignObj=A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen(_DesignParameter=None,
                                                                                    _Name='{}:SRF_NMOS_Body_Contact'.format(
                                                                                        _Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
                self._DesignParameter['SRF_NMOS_Body_Contact']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_NMOS_Body_Contact']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_NMOS_Body_Contact']['_DesignObj']._CalculateDesignParameter(
                    **_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
                tmpXY = []
                ## initialized Sref coordinate
                self._DesignParameter['SRF_NMOS_Body_Contact']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                ## Target_coord: _XY_type1
                tmp1 = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'SRF_Driver_NMOS',
                                           'BND_{}Layer'.format(_Driver_PMOS_XVT))
                tmp1_1 = self.get_param_KJH4('SRF_Dummy_DriverCell', 'SRF_Driver_PMOS', 'BND_PODummyLayer')
                target_coord = [int((tmp1[0][0][0][0]['_XY_left'][0] + tmp1_1[0][0][-1][0]['_XY_right'][0]) / 2),
                                tmp1[0][0][0][0]['_XY_down'][1]]

                ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('SRF_NMOS_Body_Contact', 'SRF_PbodyContactPhyLen', 'BND_ODLayer')
                approaching_coord = tmp2[0][0][0][0]['_XY_up']

                ## Sref coord
                tmp3 = self.get_param_KJH4('SRF_NMOS_Body_Contact')
                Scoord = tmp3[0][0]['_XY_origin']
                SpaceingODBtwNMOSArray = 100
                Scoord[1] = Scoord[1] - max(SpaceingODBtwNMOSArray, _DRCObj._OdMinSpace2Pp)

                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)

                ## Define Coordinates
                self._DesignParameter['SRF_NMOS_Body_Contact']['_XYCoordinates'] = tmpXY

                # NWELL Boundary generation
                print('#########################################')
                print('##      NWELL Calculation_Start        ##')
                print('#########################################')
                ## Boundary_element Generation
                self._DesignParameter['BND_NWELL'] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['NWELL'][0],
                    _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                    _XWidth=None,
                    _YWidth=None,
                    _XYCoordinates=[],
                )
                ## Define Boundary_element _YWidth
                tmp0 = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'SRF_Driver_PMOS',
                                           'BND_{}Layer'.format(_Driver_PMOS_XVT))
                tmp1 = self.get_param_KJH4('SRF_PMOS_Body_Contact', 'SRF_NbodyContactPhyLen', 'BND_Nwell')
                self._DesignParameter['BND_NWELL']['_YWidth'] = abs(
                    tmp1[0][0][0][0]['_XY_up'][1] - tmp0[0][0][0][0]['_XY_down'][1]) + _DRCObj._NwMinEnclosurePactive

                ## Define Boundary_element _XWidth
                self._DesignParameter['BND_NWELL']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']

                ## Calculate Sref XYcoord
                tmpXY = []
                ## initialized Sref coordinate
                self._DesignParameter['BND_NWELL']['_XYCoordinates'] = [[0, 0]]

                ## Calculate
                ## Target_coord: _XY_type1
                target_coord = tmp1[0][0][0][0]['_XY_up_left']

                ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('BND_NWELL')
                approaching_coord = tmp2[0][0]['_XY_up_left']

                ## Sref coord
                Scoord = tmp2[0][0]['_XY_origin']

                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
                ## Define coordinates
                self._DesignParameter['BND_NWELL']['_XYCoordinates'] = tmpXY

                # PMOS PP Layer generation
                print('#############################################')
                print('##     PMOS BP Layer Calculation_Start     ##')
                print('#############################################')
                ## Boundary_element Generation
                self._DesignParameter['BND_PMOSArray_PPLayer'] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['PIMP'][0],
                    _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                    _XWidth=None,
                    _YWidth=None,
                    _XYCoordinates=[],
                )
                ## Define Boundary_element _YWidth
                tmp0 = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'SRF_Driver_PMOS', 'BND_PPLayer')
                tmp1_1 = self.get_param_KJH4('SRF_Dummy_DriverCell', 'SRF_Driver_PMOS', 'BND_PPLayer')
                self._DesignParameter['BND_PMOSArray_PPLayer']['_YWidth'] = tmp0[0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
                self._DesignParameter['BND_PMOSArray_PPLayer']['_XWidth'] = abs(
                    tmp0[0][0][0][0]['_XY_left'][0] - tmp1_1[0][0][0][0]['_XY_right'][0])

                ## Calculate Sref XYcoord
                tmpXY = []
                ## initialized Sref coordinate
                self._DesignParameter['BND_PMOSArray_PPLayer']['_XYCoordinates'] = [[0, 0]]

                ## Calculate
                ## Target_coord: _XY_type1
                target_coord = tmp0[0][0][0][0]['_XY_up_left']

                ## Approaching_coord: _XY_type2
                tmp1 = self.get_param_KJH4('BND_PMOSArray_PPLayer')
                approaching_coord = tmp1[0][0]['_XY_up_left']

                ## Sref coord
                Scoord = tmp1[0][0]['_XY_origin']

                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
                ## Define coordinates
                self._DesignParameter['BND_PMOSArray_PPLayer']['_XYCoordinates'] = tmpXY

                # XVT Layer Boundary generation
                print('#########################################')
                print('##  PMOS XVT Layer Calculation_Start   ##')
                print('#########################################')
                # PMOS XVT Layer generation
                ## Boundary_element Generation
                self._DesignParameter[
                    'BND_PMOSArray_{}Layer'.format(_Driver_PMOS_XVT)] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping[_Driver_PMOS_XVT][0],
                    _Datatype=DesignParameters._LayerMapping[_Driver_PMOS_XVT][1],
                    _XWidth=None,
                    _YWidth=None,
                    _XYCoordinates=[],
                )
                ## Define Boundary_element _YWidth
                tmp0 = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'SRF_Driver_PMOS',
                                           'BND_{}Layer'.format(_Driver_PMOS_XVT))
                tmp1 = self.get_param_KJH4('SRF_Dummy_DriverCell', 'SRF_Driver_PMOS', 'BND_{}Layer'.format(_Driver_PMOS_XVT))
                self._DesignParameter['BND_PMOSArray_{}Layer'.format(_Driver_PMOS_XVT)]['_YWidth'] = tmp0[0][0][0][0][
                    '_Ywidth']

                ## Define Boundary_element _XWidth
                self._DesignParameter['BND_PMOSArray_{}Layer'.format(_Driver_PMOS_XVT)]['_XWidth'] = abs(
                    tmp0[0][0][0][0]['_XY_left'][0] - tmp1[0][0][0][0]['_XY_right'][0])

                ## Calculate Sref XYcoord
                tmpXY = []
                ## initialized Sref coordinate
                self._DesignParameter['BND_PMOSArray_{}Layer'.format(_Driver_PMOS_XVT)]['_XYCoordinates'] = [[0, 0]]

                ## Calculate
                ## Target_coord: _XY_type1
                target_coord = tmp0[0][0][0][0]['_XY_up_left']

                ## Approaching_coord: _XY_type2
                tmp1 = self.get_param_KJH4('BND_PMOSArray_{}Layer'.format(_Driver_PMOS_XVT))
                approaching_coord = tmp1[0][0]['_XY_up_left']

                ## Sref coord
                Scoord = tmp1[0][0]['_XY_origin']

                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
                ## Define coordinates
                self._DesignParameter['BND_PMOSArray_{}Layer'.format(_Driver_PMOS_XVT)]['_XYCoordinates'] = tmpXY

                # NMOS XVT Layer generation
                print('#########################################')
                print('##  NMOS XVT Layer Calculation_Start   ##')
                print('#########################################')
                ## Boundary_element Generation
                self._DesignParameter[
                    'BND_NMOSArray_{}Layer'.format(_Driver_NMOS_XVT)] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping[_Driver_NMOS_XVT][0],
                    _Datatype=DesignParameters._LayerMapping[_Driver_NMOS_XVT][1],
                    _XWidth=None,
                    _YWidth=None,
                    _XYCoordinates=[],
                )
                ## Define Boundary_element _YWidth
                tmp0 = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'SRF_Driver_NMOS',
                                           'BND_{}Layer'.format(_Driver_NMOS_XVT))
                tmp1 = self.get_param_KJH4('SRF_Dummy_DriverCell'.format(CapSize), 'SRF_Driver_NMOS',
                                           'BND_{}Layer'.format(_Driver_NMOS_XVT))
                self._DesignParameter['BND_NMOSArray_{}Layer'.format(_Driver_NMOS_XVT)]['_YWidth'] = tmp0[0][0][0][0][
                    '_Ywidth']

                ## Define Boundary_element _XWidth
                self._DesignParameter['BND_NMOSArray_{}Layer'.format(_Driver_NMOS_XVT)]['_XWidth'] = abs(
                    tmp0[0][0][0][0]['_XY_left'][0] - tmp1[0][0][0][0]['_XY_right'][0])

                ## Calculate Sref XYcoord
                tmpXY = []
                ## initialized Sref coordinate
                self._DesignParameter['BND_NMOSArray_{}Layer'.format(_Driver_NMOS_XVT)]['_XYCoordinates'] = [[0, 0]]

                ## Calculate
                ## Target_coord: _XY_type1
                target_coord = tmp0[0][0][0][0]['_XY_up_left']

                ## Approaching_coord: _XY_type2
                tmp1 = self.get_param_KJH4('BND_NMOSArray_{}Layer'.format(_Driver_NMOS_XVT))
                approaching_coord = tmp1[0][0]['_XY_up_left']

                ## Sref coord
                Scoord = tmp1[0][0]['_XY_origin']

                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
                ## Define coordinates
                self._DesignParameter['BND_NMOSArray_{}Layer'.format(_Driver_NMOS_XVT)]['_XYCoordinates'] = tmpXY

                ## VREF Hrz Metal (M6) Generation
                print('###################################################')
                print('##   NMOS Source<-> VREFN M6 Calculation_Start   ##')
                print('###################################################')
                # VREFN Boundary generation
                ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
                self._DesignParameter['BND_VREFN_Hrz_M6'] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['METAL6'][0],
                    _Datatype=DesignParameters._LayerMapping['METAL6'][1],
                    _XWidth=None,
                    _YWidth=None,
                    _XYCoordinates=[],
                )
                ## Define Boundary_element _YWidth
                VREFN_Hrz_M6_Minwidth = 244  # 비아당 컨택 두 개 박힐려면 최소 244 Ywidth가 필요함.
                tmp = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'SRF_NMOSSourceVREFN_ViaM2M6',
                                          'SRF_ViaM5M6', 'BND_Met6Layer')
                self._DesignParameter['BND_VREFN_Hrz_M6']['_YWidth'] = min(max(VREFN_Hrz_M6_Minwidth,
                                                                           int(tmp[0][0][0][0][0]['_Ywidth'])), 4000)

                ## Define Boundary_element _XWidth
                tmp1 = self.get_param_KJH4('SRF_Dummy_DriverCell'.format(CapSize), 'SRF_NMOSSourceVREFN_ViaM2M6',
                                          'SRF_ViaM5M6', 'BND_Met6Layer')
                self._DesignParameter['BND_VREFN_Hrz_M6']['_XWidth'] = abs(
                    tmp[0][0][0][0][0]['_XY_left'][0] - tmp1[0][-1][0][0][0]['_XY_right'][0])

                ## Calculate Sref XYcoord
                tmpXY = []

                ## initialized Sref coordinate
                self._DesignParameter['BND_VREFN_Hrz_M6']['_XYCoordinates'] = [[0, 0]]

                ## Calculate
                ## Target_coord: _XY_type1
                target_coord = tmp[0][0][0][0][0]['_XY_down_left']

                ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('BND_VREFN_Hrz_M6')
                approaching_coord = tmp2[0][0]['_XY_down_left']

                ## Sref coord
                Scoord = tmp2[0][0]['_XY_origin']

                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)

                ## Define coordinates
                self._DesignParameter['BND_VREFN_Hrz_M6']['_XYCoordinates'] = tmpXY

                # VREFP Boundary generation
                print('###################################################')
                print('##   PMOS Source<-> VREFP M6 Calculation_Start   ##')
                print('###################################################')
                ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
                self._DesignParameter['BND_VREFP_Hrz_M6'] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['METAL6'][0],
                    _Datatype=DesignParameters._LayerMapping['METAL6'][1],
                    _XWidth=None,
                    _YWidth=None,
                    _XYCoordinates=[],
                )
                ## Define Boundary_element _YWidth
                VREFN_Hrz_M6_Minwidth = 244  # 비아당 컨택 두 개 박힐려면 최소 244 Ywidth가 필요함.
                tmp = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'SRF_PMOSSourceVREFP_ViaM2M6',
                                          'SRF_ViaM5M6', 'BND_Met6Layer')
                self._DesignParameter['BND_VREFP_Hrz_M6']['_YWidth'] = min(max(VREFN_Hrz_M6_Minwidth,
                                                                           int(tmp[0][0][0][0][0]['_Ywidth'])), 4000)

                ## Define Boundary_element _XWidth
                tmp1 = self.get_param_KJH4('SRF_Dummy_DriverCell'.format(CapSize), 'SRF_PMOSSourceVREFP_ViaM2M6',
                                          'SRF_ViaM5M6', 'BND_Met6Layer')
                self._DesignParameter['BND_VREFP_Hrz_M6']['_XWidth'] = abs(
                    tmp[0][0][0][0][0]['_XY_left'][0] - tmp1[0][-1][0][0][0]['_XY_right'][0])

                ## Calculate Sref XYcoord
                tmpXY = []
                ## initialized Sref coordinate
                self._DesignParameter['BND_VREFP_Hrz_M6']['_XYCoordinates'] = [[0, 0]]

                ## Calculate
                ## Target_coord: _XY_type1
                target_coord = tmp[0][0][0][0][0]['_XY_down_left']

                ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('BND_VREFP_Hrz_M6')
                approaching_coord = tmp2[0][0]['_XY_down_left']

                ## Sref coord
                Scoord = tmp2[0][0]['_XY_origin']

                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)

                ## Define coordinates
                self._DesignParameter['BND_VREFP_Hrz_M6']['_XYCoordinates'] = tmpXY


            ## Input Node Horizontal Path (M3)
            print('#################################################')
            print('##      Input Node Path Calculation_Start      ##')
            print('#################################################')
            self._DesignParameter['BND_{}C_Driver_Input_Hrz_M3'.format(CapSize)] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL3'][0],
                _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )
            InputM3HrzPathWidth = 100
            InputM2VtcPathWidth = 50
            SpaceBtwInputHrzM3andNMOS = 300
            SpaceBtwInputHrzPaths = 100
            self._DesignParameter['BND_{}C_Driver_Input_Hrz_M3'.format(CapSize)]['_YWidth'] = InputM3HrzPathWidth

            ## Define Boundary_element _XWidthk
            tmp = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'BND_Input_Node_Hrz_M2')

            self._DesignParameter['BND_{}C_Driver_Input_Hrz_M3'.format(CapSize)]['_XWidth'] = \
                max(abs(tmp[0][0][0]['_XY_left'][0] - tmp[-1][0][0]['_XY_left'][0]) + 244,
                    244)  # 244는 컨택 두 개가 박힌 최소 비아 길이

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_{}C_Driver_Input_Hrz_M3'.format(CapSize)]['_XYCoordinates'] = [[0, 0]]

            ## Calculate
            tmpXY = []
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_NMOS_Body_Contact', 'SRF_PbodyContactPhyLen', 'BND_PPLayer')
            target_coord = [tmp[0][0][0]['_XY_left'][0], tmp1[0][0][0][0]['_XY_down'][1]]

            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_{}C_Driver_Input_Hrz_M3'.format(CapSize))
            approaching_coord = tmp2[0][0]['_XY_up_left']

            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_{}C_Driver_Input_Hrz_M3'.format(CapSize))
            Scoord = tmp3[0][0]['_XY_origin']
            Scoord[1] = Scoord[1] - SpaceBtwInputHrzM3andNMOS - (InputM3HrzPathWidth + SpaceBtwInputHrzPaths) * i

            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

            ## Define coordinates
            self._DesignParameter['BND_{}C_Driver_Input_Hrz_M3'.format(CapSize)]['_XYCoordinates'] = tmpXY


            ## Input Node Vertical Path (M2)
            self._DesignParameter['BND_{}C_Driver_Input_Vtc_M2'.format(CapSize)] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )
            tmp1_1 = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'BND_Input_Node_Hrz_M2')
            tmp1_2 = self.get_param_KJH4('BND_{}C_Driver_Input_Hrz_M3'.format(CapSize))
            self._DesignParameter['BND_{}C_Driver_Input_Vtc_M2'.format(CapSize)]['_YWidth'] = abs(
                tmp1_1[0][0][0]['_XY_up'][1] - tmp1_2[0][0]['_XY_cent'][1])

            ## Define Boundary_element _XWidth
            tmp = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'BND_Input_Node_Hrz_M2')

            self._DesignParameter['BND_{}C_Driver_Input_Vtc_M2'.format(CapSize)]['_XWidth'] = InputM2VtcPathWidth

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_{}C_Driver_Input_Vtc_M2'.format(CapSize)]['_XYCoordinates'] = [[0, 0]]

            ## Calculate
            tmpXY = []
            for i in range(CapSize):
                ## Target_coord: _XY_type1
                tmp1 = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'BND_Input_Node_Hrz_M2')
                target_coord = tmp1[i][0][0]['_XY_up_left']

                ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('BND_{}C_Driver_Input_Vtc_M2'.format(CapSize))
                approaching_coord = tmp2[0][0]['_XY_up_left']

                ## Sref coord
                Scoord = tmp2[0][0]['_XY_origin']

                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)

            ## Define coordinates
            self._DesignParameter['BND_{}C_Driver_Input_Vtc_M2'.format(CapSize)]['_XYCoordinates'] = tmpXY

            # Input Node Viastack M2M3 generation
            ## ViaM1M2 (PMOS Array Vtc Path M1 <-> Gate Hrz Path M2)
            ## Sref generation: ViaX
            ## Define ViaX Parameter
            _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
            _Caculation_Parameters['_Layer1'] = 2
            _Caculation_Parameters['_Layer2'] = 3
            _Caculation_Parameters['_COX'] = 2
            _Caculation_Parameters['_COY'] = 1

            self._DesignParameter['SRF_{}C_Driver_InputNode_ViaM2M3'.format(CapSize)] = \
                self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                                                         _Name='{}:SRF_{}C_Driver_InputNode_ViaM2M3'.format(
                                                                                             _Name, CapSize)))[0]

            ## Define Sref Relection
            self._DesignParameter['SRF_{}C_Driver_InputNode_ViaM2M3'.format(CapSize)]['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
            self._DesignParameter['SRF_{}C_Driver_InputNode_ViaM2M3'.format(CapSize)]['_Angle'] = 0

            self._DesignParameter['SRF_{}C_Driver_InputNode_ViaM2M3'.format(CapSize)][
                '_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            tmpXY = []
            for j in range(CapSize):
                ## Calculate Sref XYcoord
                ## initialized Sref coordinate
                self._DesignParameter['SRF_{}C_Driver_InputNode_ViaM2M3'.format(CapSize)]['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                ## Target_coord
                tmp1 = self.get_param_KJH4('BND_{}C_Driver_Input_Vtc_M2'.format(CapSize))
                target_coord = tmp1[j][0]['_XY_down_left']
                ## Approaching_coord
                tmp2 = self.get_param_KJH4('SRF_{}C_Driver_InputNode_ViaM2M3'.format(CapSize), 'SRF_ViaM2M3',
                                           'BND_Met3Layer')
                approaching_coord = tmp2[0][0][0][0]['_XY_left']
                ## Sref coord
                tmp3 = self.get_param_KJH4('SRF_{}C_Driver_InputNode_ViaM2M3'.format(CapSize))
                Scoord = tmp3[0][0]['_XY_origin']
                ## Calculate
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
            ## Define
            self._DesignParameter['SRF_{}C_Driver_InputNode_ViaM2M3'.format(CapSize)]['_XYCoordinates'] = tmpXY


            # Input Node Viastack M2M3 generation
            ## ViaM1M2 (PMOS Array Vtc Path M1 <-> Gate Hrz Path M2)
            ## Sref generation: ViaX
            ## Define ViaX Parameter
            _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
            _Caculation_Parameters['_Layer1'] = 2
            _Caculation_Parameters['_Layer2'] = 3
            _Caculation_Parameters['_COX'] = 2
            _Caculation_Parameters['_COY'] = 1

            self._DesignParameter['SRF_{}C_Driver_InputNode_ViaM2M3'.format(CapSize)] = \
                self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                                                         _Name='{}:SRF_{}C_Driver_InputNode_ViaM2M3'.format(
                                                                                             _Name, CapSize)))[0]

            ## Define Sref Relection
            self._DesignParameter['SRF_{}C_Driver_InputNode_ViaM2M3'.format(CapSize)]['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
            self._DesignParameter['SRF_{}C_Driver_InputNode_ViaM2M3'.format(CapSize)]['_Angle'] = 0

            self._DesignParameter['SRF_{}C_Driver_InputNode_ViaM2M3'.format(CapSize)][
                '_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            tmpXY = []
            for j in range(CapSize):
                ## Calculate Sref XYcoord
                ## initialized Sref coordinate
                self._DesignParameter['SRF_{}C_Driver_InputNode_ViaM2M3'.format(CapSize)]['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                ## Target_coord
                tmp1 = self.get_param_KJH4('BND_{}C_Driver_Input_Vtc_M2'.format(CapSize))
                target_coord = tmp1[j][0]['_XY_down_left']
                ## Approaching_coord
                tmp2 = self.get_param_KJH4('SRF_{}C_Driver_InputNode_ViaM2M3'.format(CapSize), 'SRF_ViaM2M3',
                                           'BND_Met3Layer')
                approaching_coord = tmp2[0][0][0][0]['_XY_left']
                ## Sref coord
                tmp3 = self.get_param_KJH4('SRF_{}C_Driver_InputNode_ViaM2M3'.format(CapSize))
                Scoord = tmp3[0][0]['_XY_origin']
                ## Calculate
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
            ## Define
            self._DesignParameter['SRF_{}C_Driver_InputNode_ViaM2M3'.format(CapSize)]['_XYCoordinates'] = tmpXY


        ## Dummy Cell Input Node Vertical Path (M2)
        self._DesignParameter['BND_Dummy_Driver_Input_Vtc_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        tmp1_1 = self.get_param_KJH4('SRF_Dummy_DriverCell', 'BND_Input_Node_Hrz_M2')
        tmp1_2 = self.get_param_KJH4('BND_{}C_Driver_Input_Hrz_M3'.format(1))
        self._DesignParameter['BND_Dummy_Driver_Input_Vtc_M2']['_YWidth'] = abs(
            tmp1_1[0][0][0]['_XY_up'][1] - tmp1_2[0][0]['_XY_cent'][1]) + (InputM3HrzPathWidth + SpaceBtwInputHrzPaths)

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_{}C_DriverCell'.format(CapSize), 'BND_Input_Node_Hrz_M2')
        self._DesignParameter['BND_Dummy_Driver_Input_Vtc_M2']['_XWidth'] = InputM2VtcPathWidth

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Dummy_Driver_Input_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate
        tmpXY = []
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Dummy_DriverCell'.format(CapSize), 'BND_Input_Node_Hrz_M2')
        target_coord = tmp1[i][0][0]['_XY_up_left']

        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Dummy_Driver_Input_Vtc_M2')
        approaching_coord = tmp2[0][0]['_XY_up_left']

        ## Sref coord
        Scoord = tmp2[0][0]['_XY_origin']

        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define coordinates
        self._DesignParameter['BND_Dummy_Driver_Input_Vtc_M2']['_XYCoordinates'] = tmpXY


        # Dummy Cell Input Node Viastack M2M3 generation
        ## ViaM1M2 (PMOS Array Vtc Path M1 <-> Gate Hrz Path M2)
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        self._DesignParameter['SRF_Dummy_Driver_InputNode_ViaM2M3'] = \
            self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                                                     _Name='{}:SRF_Dummy_Driver_InputNode_ViaM2M3'.format(
                                                                                         _Name, CapSize)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_Dummy_Driver_InputNode_ViaM2M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_Dummy_Driver_InputNode_ViaM2M3']['_Angle'] = 0

        self._DesignParameter['SRF_Dummy_Driver_InputNode_ViaM2M3'][
            '_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        ## initialized Sref coordinate
        self._DesignParameter['SRF_Dummy_Driver_InputNode_ViaM2M3']['_XYCoordinates'] = [[0, 0]]

        tmpXY =[]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_Dummy_Driver_Input_Vtc_M2')
        target_coord = tmp1[j][0]['_XY_down_right']

        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Dummy_Driver_InputNode_ViaM2M3', 'SRF_ViaM2M3',
                                   'BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_right']

        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Dummy_Driver_InputNode_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']

        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_Dummy_Driver_InputNode_ViaM2M3']['_XYCoordinates'] = tmpXY

        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')
        DriverArray_end_time = time.time()
        self.DriverArray_elapsed_time = DriverArray_end_time - DriverArray_start_time

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ZZ01_H01_01_DriverArray_Fold1'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'H01_01_DriverArray_unfold'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        # NumOfDriverUnitsInDriverArray = 2^(_NumOfBits) - 1
        _NumOfBits=3,

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
    LayoutObj = _DriverArray(_DesignParameter=None, _Name=cellname)
    # LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._CalculateDesignParameterFold1(**InputParams)
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
