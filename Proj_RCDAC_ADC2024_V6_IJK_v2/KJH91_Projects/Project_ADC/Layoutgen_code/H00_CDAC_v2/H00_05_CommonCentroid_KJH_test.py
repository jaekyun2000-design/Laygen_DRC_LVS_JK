## Import Basic Modules
    ## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_ADC.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

    ## Library
import copy
import time
import numpy as np

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.H00_CDAC_v2 import H00_04_CommonArray_KJH_test
from KJH91_Projects.Project_ADC.Layoutgen_code.H00_CDAC_v2 import H00_02_CapWithShield_KJH_test
from KJH91_Projects.Project_ADC.Layoutgen_code.H00_CDAC_v2 import H00_03_DummyCapUnit_KJH_test


############################################################################################################################################################ Class_HEADER
class _CommonCentroid(StickDiagram_KJH1._StickDiagram_KJH):
    # Initially Defined design_parameter
    _ParametersForDesignCalculation = dict(
        # # Element CDAC
        _LayoutOption=None,
        _ShieldingLayer=None,  # Poly:0, M1:1, M2:2 ...
        _MetalWidth=None,
        _MetalLength=None,
        _MetalSpacing=None,

        # #Unit Cap
        _NumOfElement=None,

        # # Shielding & Top Connect node
        _ConnectLength=None,
        _ExtendLength=None,

        # # CommonCentroid
        _Bitsize=None,

        # # Dummy Cap Option
        _DummyCap_TopBottomShort=None,
        _NumOfDummyCaps=None,  # Number of dummy cap(one side)

        # # CommonCentroid With Driving node
        _CapArrayWDrivingNodeDistance=None,  # DRC Rule
        _DriveNodeDistance=None,  #
        #_MetalWidth=None,
        _YWidth_Bottom_Hrz=None,
    )

    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _Name=self._NameDeclaration(_Name=_Name),
                _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                _XYcoordAsCent=dict(_XYcoordAsCent=0),
            )

    ##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
    def _CalculateDesignParameter(self,
                                  # # Element Capacitor (0.27fF)
                                  _LayoutOption=None,
                                  _ShieldingLayer=None,  # Poly:0, M1:1, M2:2 ...
                                  _MetalWidth=None,
                                  _MetalLength=None,
                                  _MetalSpacing=None,

                                  # #Unit Cap
                                  _NumOfElement=None,

                                  # # Shielding & Top Connect node
                                  _ConnectLength=None,
                                  _ExtendLength=None,

                                  # # CommonCentroid Array
                                  _Bitsize=None,

                                  # # Dummy Cap Option
                                  _DummyCap_TopBottomShort=None,
                                  _NumOfDummyCaps=None,  # Number of dummy cap(one side)

                                  # # CommonCentroid With Driving node
                                  _CapArrayWDrivingNodeDistance=None,  # DRC Rule
                                  _DriveNodeDistance=None,  #
                                  #_MetalWidth=None,
                                  _YWidth_Bottom_Hrz=None,
                                  ):

        ################################################################################################################################################## Class_HEADER: Pre Defined Parameter Before Calculation
        print('##     Pre Defined Parameter Before Calculation    ##')
        CDACBotVtcExtMetalType = 6
        CDACBotHrzMetalType = 5
        # Load DRC library
        _DRCobj = DRC.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']


        ## CALCULATION START
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

        ############################################################################################################################################################ CALCULATION START

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Sref Gen: CommonArrary
            ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(H00_04_CommonArray._CommonArray._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_LayoutOption']    = _LayoutOption
        _Caculation_Parameters['_ShieldingLayer']    = _ShieldingLayer
        _Caculation_Parameters['_MetalWidth']   = _MetalWidth
        _Caculation_Parameters['_MetalLength']  = _MetalLength
        _Caculation_Parameters['_MetalSpacing']      = _MetalSpacing
        _Caculation_Parameters['_NumOfElement']      = _NumOfElement
        _Caculation_Parameters['_ConnectLength']      = _ConnectLength
        _Caculation_Parameters['_ExtendLength']      = _ExtendLength
        _Caculation_Parameters['_Bitsize']      = _Bitsize
        _Caculation_Parameters['_DummyCap_TopBottomShort'] = _DummyCap_TopBottomShort
        _Caculation_Parameters['_NumOfDummyCaps'] = _NumOfDummyCaps


                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_CommonArray'] = self._SrefElementDeclaration(_DesignObj=H00_04_CommonArray._CommonArray(_DesignParameter=None, _Name='{}:SRF_CommonArray'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_CommonArray']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CommonArray']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CommonArray']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CommonArray']['_XYCoordinates'] = [[0, 0]]

        for i in range(0,_Bitsize):
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## BND Gen: VtcExten
            ## Boundary_element Generation

                    ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_B{}_BotExten_VTC'.format(_Bitsize-i-1)] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}'.format(CDACBotVtcExtMetalType)][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}'.format(CDACBotVtcExtMetalType)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
            )
            ## Define Boundary_element _YWidth
            if i == 0:
                tmp = _CapArrayWDrivingNodeDistance + 79  # DRC
            else:
                tmp4 = self.get_param_KJH4('SRF_CommonArray', 'SRF_CDAC_B{}'.format(_Bitsize - i - 1), 'SRF_UCAP',
                                           'SRF_ECAP', 'BND_ECAP_Bot_VTC_M{}'.format(CDACBotVtcExtMetalType))
                tmp5 = self.get_param_KJH4('BND_B{}_BotExten_VTC'.format(_Bitsize - i))
                tmp = abs(tmp4[0][0][0][0][0][0]['_XY_down'][1] - tmp5[0][0]['_XY_down'][1]) + _DriveNodeDistance
            self._DesignParameter['BND_B{}_BotExten_VTC'.format(_Bitsize - i - 1)]['_YWidth'] = tmp + _YWidth_Bottom_Hrz

            ## Define Boundary_element _XWidth
            self._DesignParameter['BND_B{}_BotExten_VTC'.format(_Bitsize - i - 1)]['_XWidth'] = _MetalWidth

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_B{}_BotExten_VTC'.format(_Bitsize - i - 1)]['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
            tmpXY = []
            for k in range(0, 2 ** (_Bitsize - i - 1)):
                for j in range(_NumOfElement):
                    ## Calculate
                    ## Target_coord: _XY_type1
                    tmp1 = self.get_param_KJH4('SRF_CommonArray', 'SRF_CDAC_B{}'.format(_Bitsize - i - 1),
                                               'SRF_UCAP', 'SRF_ECAP',
                                               'BND_ECAP_Bot_VTC_M{}'.format(CDACBotVtcExtMetalType))
                    target_coord = tmp1[0][k][0][j][0][0]['_XY_down_left']
                    ## Approaching_coord: _XY_type2
                    tmp2 = self.get_param_KJH4('BND_B{}_BotExten_VTC'.format(_Bitsize - i - 1))
                    approaching_coord = tmp2[0][0]['_XY_up_left']
                    ## Sref coord
                    tmp3 = self.get_param_KJH4('BND_B{}_BotExten_VTC'.format(_Bitsize - i - 1))
                    Scoord = tmp3[0][0]['_XY_origin']
                    ## Cal
                    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                    tmpXY.append(New_Scoord)

                    ## Define coordinates
            self._DesignParameter['BND_B{}_BotExten_VTC'.format(_Bitsize - i - 1)]['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## BND Gen: Hrz
            ## Boundary_element Generation
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_B{}_Bottom_Hrz'.format(_Bitsize - i - 1)] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL{}'.format(CDACBotHrzMetalType)][0],
                _Datatype=DesignParameters._LayerMapping['METAL{}'.format(CDACBotHrzMetalType)][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )
            ## Define Boundary_element _YWidth
            self._DesignParameter['BND_B{}_Bottom_Hrz'.format(_Bitsize - i - 1)]['_YWidth'] = _YWidth_Bottom_Hrz

            ## Define Boundary_element _XWidth
            tmp = self.get_param_KJH4('BND_B{}_BotExten_VTC'.format(_Bitsize - i - 1))
            self._DesignParameter['BND_B{}_Bottom_Hrz'.format(_Bitsize - i - 1)]['_XWidth'] = abs(
                tmp[0][0]['_XY_left'][0] - tmp[-1][0]['_XY_right'][0])
            #
            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_B{}_Bottom_Hrz'.format(_Bitsize - i - 1)]['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['BND_B{}_Bottom_Hrz'.format(_Bitsize - i - 1)]['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('BND_B{}_BotExten_VTC'.format(_Bitsize - i - 1))
            target_coord = tmp1[0][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_B{}_Bottom_Hrz'.format(_Bitsize - i - 1))
            approaching_coord = tmp2[0][0]['_XY_down_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_B{}_Bottom_Hrz'.format(_Bitsize - i - 1))
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_B{}_Bottom_Hrz'.format(_Bitsize - i - 1)]['_XYCoordinates'] = tmpXY


        for i in range(0, _Bitsize):
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Bottom node Via Gen:
            if _NumOfElement != 1:
                ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Bottom node Via Gen:
                ## Sref generation: ViaX
                ## Define ViaX Parameter
                _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
                _Caculation_Parameters['_Layer1'] = CDACBotHrzMetalType
                _Caculation_Parameters['_Layer2'] = CDACBotVtcExtMetalType
                _Caculation_Parameters['_COX'] = None
                _Caculation_Parameters['_COY'] = None

                ## Sref ViaX declaration
                self._DesignParameter[
                    'SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize - i - 1, CDACBotHrzMetalType, CDACBotVtcExtMetalType)] = \
                    self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None,
                                                                                             _Name='{}:SRF_B{}_Bottom_ViaM{}M{}'.format(
                                                                                                 _Name,
                                                                                                 _Bitsize - i - 1,
                                                                                                 CDACBotHrzMetalType,
                                                                                                 CDACBotVtcExtMetalType)))[0]

                ## Define Sref Relection
                self._DesignParameter['SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize - i - 1, CDACBotHrzMetalType, CDACBotVtcExtMetalType)]['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle
                self._DesignParameter['SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize - i - 1, CDACBotHrzMetalType, CDACBotVtcExtMetalType)]['_Angle'] = 0

                tmp1 = self.get_param_KJH4('BND_B{}_BotExten_VTC'.format(_Bitsize - i - 1))
                ViaXwidth = abs(tmp1[0][0]['_XY_left'][0] - tmp1[_NumOfElement - 1][0]['_XY_right'][0])

                ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
                _COX, _COY = self._CalculateNumViaByXYWidth(ViaXwidth, _YWidth_Bottom_Hrz, 'MinEnclosureY')
                _Caculation_Parameters['_COX'] = max(_COX, 2)
                _Caculation_Parameters['_COY'] = _COY
                ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
                self._DesignParameter['SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize - i - 1, CDACBotHrzMetalType, CDACBotVtcExtMetalType)]['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

                ## Calculate Sref XYcoord
                ## initialized Sref coordinate
                self._DesignParameter['SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize - i - 1, CDACBotHrzMetalType, CDACBotVtcExtMetalType)]['_XYCoordinates'] = [[0, 0]]

            elif _NumOfElement == 1:
                _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
                _Caculation_Parameters['_Layer1'] = CDACBotHrzMetalType
                _Caculation_Parameters['_Layer2'] = CDACBotVtcExtMetalType
                _Caculation_Parameters['_COX'] = 1
                _Caculation_Parameters['_COY'] = 2

                ## Sref ViaX declaration
                self._DesignParameter[
                    'SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize - i - 1, CDACBotHrzMetalType, CDACBotVtcExtMetalType)] = \
                self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None,
                                                                                         _Name='{}:SRF_B{}_Bottom_ViaM{}M{}'.format(
                                                                                             _Name, _Bitsize - i - 1,
                                                                                             CDACBotHrzMetalType,
                                                                                             CDACBotVtcExtMetalType)))[0]

                ## Define Sref Relection
                self._DesignParameter['SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize - i - 1, CDACBotHrzMetalType, CDACBotVtcExtMetalType)]['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle
                self._DesignParameter['SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize - i - 1, CDACBotHrzMetalType, CDACBotVtcExtMetalType)]['_Angle'] = 0

                ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
                self._DesignParameter['SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize - i - 1, CDACBotHrzMetalType, CDACBotVtcExtMetalType)]['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

                ## Calculate Sref XYcoord
                ## initialized Sref coordinate
                self._DesignParameter['SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize - i - 1, CDACBotHrzMetalType, CDACBotVtcExtMetalType)]['_XYCoordinates'] = [[0, 0]]

            tmpXY = []
            for j in range(2 ** (_Bitsize - i - 1)):
                ## Calculate
                ## Target_coord
                tmp1 = self.get_param_KJH4('BND_B{}_Bottom_Hrz'.format(_Bitsize - i - 1))
                tmp2 = self.get_param_KJH4('BND_B{}_BotExten_VTC'.format(_Bitsize - i - 1))
                BotExtenCentX = int((abs(
                    tmp2[j * _NumOfElement][0]['_XY_cent'][0] + tmp2[(j + 1) * _NumOfElement - 1][0]['_XY_cent'][
                        0])) / 2)
                ## Approaching_coord
                tmp2 = self.get_param_KJH4(
                    'SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize - i - 1, CDACBotHrzMetalType, CDACBotVtcExtMetalType),
                    'SRF_ViaM{}M{}'.format(CDACBotHrzMetalType, CDACBotHrzMetalType + 1),
                    'BND_Met{}Layer'.format(CDACBotHrzMetalType))
                if _NumOfElement != 1:
                    target_coord = [BotExtenCentX, tmp1[0][0]['_XY_cent'][1]]
                    approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                elif _NumOfElement == 1:
                    target_coord = [BotExtenCentX, tmp1[0][0]['_XY_down'][1]]
                    approaching_coord = tmp2[0][0][0][0]['_XY_down']
                    ## Sref coord
                tmp3 = self.get_param_KJH4(
                    'SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize - i - 1, CDACBotHrzMetalType, CDACBotVtcExtMetalType))
                Scoord = tmp3[0][0]['_XY_origin']
                ## Calculate
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
                ## Define
            self._DesignParameter[
                'SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize - i - 1, CDACBotHrzMetalType, CDACBotVtcExtMetalType)][
                '_XYCoordinates'] = tmpXY


            ##################### Generate Sref: Dummy Capacitor Array
            _Caculation_Parameters = copy.deepcopy(H00_03_DummyCapUnit._DummyCapUnit._ParametersForDesignCalculation)
            _Caculation_Parameters['_LayoutOption'] = _LayoutOption
            _Caculation_Parameters['_ShieldingLayer'] = _ShieldingLayer
            _Caculation_Parameters['_MetalWidth'] = _MetalWidth
            _Caculation_Parameters['_MetalLength'] = _MetalLength
            _Caculation_Parameters['_MetalSpacing'] = _MetalSpacing

            _Caculation_Parameters['_NumOfElement'] = _NumOfElement

            _Caculation_Parameters['_ConnectLength'] = _ConnectLength
            _Caculation_Parameters['_ExtendLength'] = _ExtendLength
            _Caculation_Parameters['_DummyCap_TopBottomShort'] = _DummyCap_TopBottomShort

            self._DesignParameter['SRF_DummyCaps'] = \
                self._SrefElementDeclaration(_DesignObj=H00_03_DummyCapUnit.
                                             _DummyCapUnit(_DesignParameter=None,
                                                           _Name='{}:SRF_DummyCaps'.format(_Name)))[0]

            ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
            self._DesignParameter['SRF_DummyCaps']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_DummyCaps']['_Angle'] = 0

            ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_DummyCaps']['_DesignObj']._CalculateDesignParameter(
                **_Caculation_Parameters)

            ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_DummyCaps']['_XYCoordinates'] = [[0, 0]]

            tmpXY = []
            ## Calculate left side dummy caps
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_CommonArray','SRF_CDAC_B{}'.format(_Bitsize - 1), 'SRF_UCAP', 'SRF_ECAP','BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
            target_coord = tmp1[0][0][0][0][0][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_DummyCaps', 'SRF_CapWtShield4DCAP', 'SRF_UCAP', 'SRF_ECAP',
                                       'BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
            approaching_coord = tmp2[0][0][0][0][0][0]['_XY_down_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_DummyCaps')
            Scoord = tmp3[0][0]['_XY_origin']

            tmp1 = self.get_param_KJH4('SRF_CommonArray', 'SRF_CDAC_B{}'.format(_Bitsize - 1), 'SRF_UCAP', 'SRF_ECAP','BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
            _CapLength = abs(tmp1[0][0][0][-1][-1][0]['_XY_right'][0] - tmp1[0][0][0][0][0][0]['_XY_right'][0])
            Scoord[0] = Scoord[0] - _CapLength * _NumOfDummyCaps
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['SRF_DummyCaps']['_XYCoordinates'] = tmpXY
            for i in range(1, _NumOfDummyCaps):
                # 시작점 : ((2 ** i) * DistanceBtwTr)
                tmp = tmpXY[0] + [_CapLength * (i), 0]
                tmpXY.append(tmp)
            ## Calculate right side dummy caps
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_CommonArray', 'SRF_CDAC_B{}'.format(_Bitsize - 1), 'SRF_UCAP', 'SRF_ECAP',
                                       'BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
            target_coord = tmp1[0][-1][0][-1][-1][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_DummyCaps', 'SRF_CapWtShield4DCAP', 'SRF_UCAP', 'SRF_ECAP',
                                       'BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
            approaching_coord = tmp2[0][0][0][0][0][0]['_XY_down_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_DummyCaps')
            Scoord = tmp3[0][0]['_XY_origin']
            # Scoord[0] = Scoord[0] - _CapLength * _NumOfDummyCaps
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            for i in range(1, _NumOfDummyCaps):
                tmp = tmpXY[_NumOfDummyCaps] + [_CapLength * (i), 0]
                tmpXY.append(tmp)
            ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_DummyCaps']['_XYCoordinates'] = tmpXY


        if (_NumOfElement == 1) and (CDACBotHrzMetalType in _LayoutOption):
            ## MSB Bottom Node M5 Vtc Extension for satisfying Design Rule (M5 Minimum Space)
            ## Boundary Element Generation
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_MSBBotExtension_Vtc_M5'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL5'][0],
                _Datatype=DesignParameters._LayerMapping['METAL5'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )
            ## Define Boundary_element _YWidth
            tmp1 = self.get_param_KJH4('SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize-1,CDACBotHrzMetalType,CDACBotVtcExtMetalType),'SRF_ViaM{}M{}'.format(CDACBotHrzMetalType,CDACBotHrzMetalType+1),'BND_Met{}Layer'.format(CDACBotHrzMetalType))
            tmp2 = self.get_param_KJH4('SRF_CommonArray','SRF_CDAC_B{}'.format(_Bitsize-1),'SRF_UCAP','SRF_ECAP','SRF_Bot_Vtc_ViaM{}M{}'.format(_LayoutOption[0],_LayoutOption[-1]),'SRF_ViaM{}M{}'.format(_LayoutOption[0],_LayoutOption[0]+1),'BND_Met{}Layer'.format(_LayoutOption[0]))
            self._DesignParameter['BND_MSBBotExtension_Vtc_M5']['_YWidth'] = abs(tmp1[0][0][0][0]['_XY_down'][1] - tmp2[0][0][0][0][0][0][0][0]['_XY_up'][1])

            ## Define Boundary_element _XWidth
            self._DesignParameter['BND_MSBBotExtension_Vtc_M5']['_XWidth'] = tmp2[0][0][0][0][0][0][0][0]['_Xwidth']

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_MSBBotExtension_Vtc_M5']['_XYCoordinates'] = [[0, 0]]
            ## Calculate Sref XYcoord
            tmpXY = []
            ## Calculate
            ## Approaching_coord: _XY_type2
            tmp3 = self.get_param_KJH4('BND_MSBBotExtension_Vtc_M5')
            approaching_coord = tmp3[0][0]['_XY_up']
            ## Sref coord
            tmp4 = self.get_param_KJH4('BND_MSBBotExtension_Vtc_M5')
            Scoord = tmp4[0][0]['_XY_origin']
            for i in range(2 ** (_Bitsize-1)):
            ## Target_coord: _XY_type1
                target_coord = tmp2[0][i][0][0][0][0][0][0]['_XY_up']
                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_MSBBotExtension_Vtc_M5']['_XYCoordinates'] = tmpXY


        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')


    ##########################################################################################################################################################################################
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
    def _CalculateDesignParameterFold1(self,
                                  _LayoutOption=None,
                                  _ShieldingLayer=None,  # Poly:0, M1:1, M2:2 ...
                                  _MetalWidth=None,
                                  _MetalLength=None,
                                  _MetalSpacing=None,

                                  # #Unit Cap
                                  _NumOfElement=None,

                                  # # Shielding & Top Connect node
                                  _ConnectLength=None,
                                  _ExtendLength=None,

                                  # # CommonCentroid Array
                                  _Bitsize=None,

                                   # # Dummy Cap Option
                                   _DummyCap_TopBottomShort=True,
                                   _NumOfDummyCaps=3,  # Number of dummy cap(one side)

                                   # # CommonCentroid With Driving node
                                  _CapArrayWDrivingNodeDistance=None,  # DRC Rule
                                  _DriveNodeDistance=None,  #
                                  #_MetalWidth=None,
                                  _YWidth_Bottom_Hrz=None,
                                  ):

        ################################################################################################################################################## Class_HEADER: Pre Defined Parameter Before Calculation
        CDACBotVtcExtMetalType = 5
        CDACBotHrzMetalType = 6
        # Load DRC library
        _DRCobj = DRC.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ## CALCULATION START
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

        ############################################################################################################################################################ CALCULATION START

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Sref Gen: CommonArrary
        ## SREF Generation
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(H00_04_CommonArray_KJH_test._CommonArray._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_LayoutOption'] = _LayoutOption
        _Caculation_Parameters['_ShieldingLayer'] = _ShieldingLayer
        _Caculation_Parameters['_MetalWidth'] = _MetalWidth
        _Caculation_Parameters['_MetalLength'] = _MetalLength
        _Caculation_Parameters['_MetalSpacing'] = _MetalSpacing
        _Caculation_Parameters['_NumOfElement'] = _NumOfElement
        _Caculation_Parameters['_ConnectLength'] = _ConnectLength
        _Caculation_Parameters['_ExtendLength'] = _ExtendLength
        _Caculation_Parameters['_Bitsize'] = _Bitsize
        _Caculation_Parameters['_DummyCap_TopBottomShort'] = _DummyCap_TopBottomShort
        _Caculation_Parameters['_NumOfDummyCaps'] = _NumOfDummyCaps

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_CommonArray'] = self._SrefElementDeclaration(
            _DesignObj=H00_04_CommonArray_KJH_test._CommonArray(_DesignParameter=None,
                                                       _Name='{}:SRF_CommonArray'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_CommonArray']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CommonArray']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CommonArray']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CommonArray']['_XYCoordinates'] = [[0, 0]]

        for i in range(0, _Bitsize):
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## BND Gen: VtcExten
            ## Boundary_element Generation
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter[
                'BND_B{}_BotExten_VTC'.format(_Bitsize - i - 1)] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL{}'.format(CDACBotVtcExtMetalType)][0],
                _Datatype=DesignParameters._LayerMapping['METAL{}'.format(CDACBotVtcExtMetalType)][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )
            ## Define Boundary_element _YWidth
            if i == 0:
                tmp = _CapArrayWDrivingNodeDistance + 79   # DRC
            else:
                tmp4 = self.get_param_KJH4('SRF_CommonArray', 'SRF_CDAC_B{}'.format(_Bitsize - i - 1), 'SRF_UCAP',
                                           'SRF_ECAP', 'BND_ECAP_Bot_VTC_M{}'.format(_LayoutOption[0]))
                tmp5 = self.get_param_KJH4('BND_B{}_BotExten_VTC'.format(_Bitsize - i))
                tmp = abs(tmp4[0][0][0][0][0][0]['_XY_down'][1] - tmp5[0][0]['_XY_down'][1]) + _DriveNodeDistance
            self._DesignParameter['BND_B{}_BotExten_VTC'.format(_Bitsize - i - 1)]['_YWidth'] = tmp + _YWidth_Bottom_Hrz

            ## Define Boundary_element _XWidth
            self._DesignParameter['BND_B{}_BotExten_VTC'.format(_Bitsize - i - 1)]['_XWidth'] = _MetalWidth

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_B{}_BotExten_VTC'.format(_Bitsize - i - 1)]['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
            tmpXY = []
            for k in range(0, 2 ** (_Bitsize - i - 1)):
                for j in range(_NumOfElement):
                    ## Calculate
                    ## Target_coord: _XY_type1
                    tmp1 = self.get_param_KJH4('SRF_CommonArray', 'SRF_CDAC_B{}'.format(_Bitsize - i - 1),
                                               'SRF_UCAP', 'SRF_ECAP', 'BND_ECAP_Bot_VTC_M{}'.format(_LayoutOption[0]))
                    target_coord = tmp1[0][k][0][j][0][0]['_XY_down_left']
                    ## Approaching_coord: _XY_type2
                    tmp2 = self.get_param_KJH4('BND_B{}_BotExten_VTC'.format(_Bitsize - i - 1))
                    approaching_coord = tmp2[0][0]['_XY_up_left']
                    ## Sref coord
                    tmp3 = self.get_param_KJH4('BND_B{}_BotExten_VTC'.format(_Bitsize - i - 1))
                    Scoord = tmp3[0][0]['_XY_origin']
                    ## Cal
                    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                    tmpXY.append(New_Scoord)

                    ## Define coordinates
            self._DesignParameter['BND_B{}_BotExten_VTC'.format(_Bitsize - i - 1)]['_XYCoordinates'] = tmpXY


            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## BND Gen: Hrz
            ## Boundary_element Generation
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_B{}_Bottom_Hrz'.format(_Bitsize - i - 1)] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL{}'.format(CDACBotHrzMetalType)][0],
                _Datatype=DesignParameters._LayerMapping['METAL{}'.format(CDACBotHrzMetalType)][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )
            ## Define Boundary_element _YWidth
            self._DesignParameter['BND_B{}_Bottom_Hrz'.format(_Bitsize - i - 1)]['_YWidth'] = _YWidth_Bottom_Hrz

            ## Define Boundary_element _XWidth
            tmp = self.get_param_KJH4('BND_B{}_BotExten_VTC'.format(_Bitsize - i - 1))
            self._DesignParameter['BND_B{}_Bottom_Hrz'.format(_Bitsize - i - 1)]['_XWidth'] = abs(
                tmp[0][0]['_XY_left'][0] - tmp[-1][0]['_XY_right'][0])
            #
            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_B{}_Bottom_Hrz'.format(_Bitsize - i - 1)]['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['BND_B{}_Bottom_Hrz'.format(_Bitsize - i - 1)]['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('BND_B{}_BotExten_VTC'.format(_Bitsize - i - 1))
            target_coord = tmp1[0][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_B{}_Bottom_Hrz'.format(_Bitsize - i - 1))
            approaching_coord = tmp2[0][0]['_XY_down_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_B{}_Bottom_Hrz'.format(_Bitsize - i - 1))
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_B{}_Bottom_Hrz'.format(_Bitsize - i - 1)]['_XYCoordinates'] = tmpXY


        for i in range(0,_Bitsize):
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Bottom node Via Gen:
            if _NumOfElement != 1:
                ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Bottom node Via Gen:
                ## Sref generation: ViaX
                ## Define ViaX Parameter
                _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
                _Caculation_Parameters['_Layer1'] = CDACBotVtcExtMetalType
                _Caculation_Parameters['_Layer2'] = CDACBotHrzMetalType
                _Caculation_Parameters['_COX'] = None
                _Caculation_Parameters['_COY'] = None

                ## Sref ViaX declaration
                self._DesignParameter['SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize - i - 1, CDACBotVtcExtMetalType, CDACBotHrzMetalType )] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_B{}_Bottom_ViaM{}M{}'.format( _Name, _Bitsize - i - 1,  CDACBotVtcExtMetalType, CDACBotHrzMetalType)))[0]

                ## Define Sref Relection
                self._DesignParameter['SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize - i - 1, CDACBotVtcExtMetalType, CDACBotHrzMetalType)]['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle
                self._DesignParameter['SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize - i - 1, CDACBotVtcExtMetalType, CDACBotHrzMetalType)]['_Angle'] = 0

                tmp1 = self.get_param_KJH4('BND_B{}_BotExten_VTC'.format(_Bitsize - i - 1))
                ViaXwidth = abs(tmp1[0][0]['_XY_left'][0] - tmp1[_NumOfElement - 1][0]['_XY_right'][0])

                ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
                _COX, _COY = self._CalculateNumViaByXYWidth(ViaXwidth, _YWidth_Bottom_Hrz, 'MinEnclosureY')
                _Caculation_Parameters['_COX'] = max(_COX, 2)
                _Caculation_Parameters['_COY'] = _COY
                ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
                self._DesignParameter['SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize - i - 1, CDACBotVtcExtMetalType, CDACBotHrzMetalType)]['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

                ## Calculate Sref XYcoord
                ## initialized Sref coordinate
                self._DesignParameter['SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize - i - 1, CDACBotVtcExtMetalType, CDACBotHrzMetalType)]['_XYCoordinates'] = [[0, 0]]

            elif _NumOfElement == 1:
                _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
                _Caculation_Parameters['_Layer1'] = CDACBotVtcExtMetalType
                _Caculation_Parameters['_Layer2'] = CDACBotHrzMetalType
                _Caculation_Parameters['_COX'] = 1
                _Caculation_Parameters['_COY'] = 2

                    ## Sref ViaX declaration
                self._DesignParameter['SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize-i-1,CDACBotVtcExtMetalType,CDACBotHrzMetalType)] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_B{}_Bottom_ViaM{}M{}'.format(_Name,_Bitsize-i-1,CDACBotVtcExtMetalType,CDACBotHrzMetalType)))[0]

                    ## Define Sref Relection
                self._DesignParameter['SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize-i-1,CDACBotVtcExtMetalType,CDACBotHrzMetalType)]['_Reflect'] = [0, 0, 0]

                    ## Define Sref Angle
                self._DesignParameter['SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize-i-1,CDACBotVtcExtMetalType,CDACBotHrzMetalType)]['_Angle'] = 0

                    ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
                self._DesignParameter['SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize-i-1,CDACBotVtcExtMetalType,CDACBotHrzMetalType)]['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

                    ## Calculate Sref XYcoord
                        ## initialized Sref coordinate
                self._DesignParameter['SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize-i-1,CDACBotVtcExtMetalType,CDACBotHrzMetalType)]['_XYCoordinates'] = [[0, 0]]

            tmpXY = []
            for j in range(2 ** (_Bitsize - i - 1)):
                        ## Calculate
                            ## Target_coord
                tmp1 = self.get_param_KJH4('BND_B{}_Bottom_Hrz'.format(_Bitsize-i-1))
                tmp2 = self.get_param_KJH4('BND_B{}_BotExten_VTC'.format(_Bitsize-i-1))
                BotExtenCentX = int((abs(tmp2[j*_NumOfElement][0]['_XY_cent'][0] + tmp2[(j+1)*_NumOfElement-1][0]['_XY_cent'][0]))/2)
                            ## Approaching_coord
                tmp2 = self.get_param_KJH4('SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize-i-1,CDACBotVtcExtMetalType,CDACBotHrzMetalType),'SRF_ViaM{}M{}'.format(CDACBotVtcExtMetalType,CDACBotVtcExtMetalType+1),'BND_Met{}Layer'.format(CDACBotHrzMetalType))
                if _NumOfElement != 1:
                    target_coord = [BotExtenCentX, tmp1[0][0]['_XY_cent'][1]]
                    approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                elif _NumOfElement == 1:
                    target_coord = [BotExtenCentX, tmp1[0][0]['_XY_down'][1]]
                    approaching_coord = tmp2[0][0][0][0]['_XY_down']
                            ## Sref coord
                tmp3 = self.get_param_KJH4('SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize-i-1,CDACBotVtcExtMetalType,CDACBotHrzMetalType))
                Scoord = tmp3[0][0]['_XY_origin']
                            ## Calculate
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
                ## Define
            self._DesignParameter['SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize-i-1,CDACBotVtcExtMetalType,CDACBotHrzMetalType)]['_XYCoordinates'] = tmpXY


        ## Dummy UCAP SRF Generation
        _Caculation_Parameters = copy.deepcopy(H00_02_CapWithShield_KJH_test._CapWithShield._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_LayoutOption'] = _LayoutOption
        _Caculation_Parameters['_ShieldingLayer'] = _ShieldingLayer
        _Caculation_Parameters['_MetalWidth'] = _MetalWidth
        _Caculation_Parameters['_MetalLength'] = _MetalLength
        _Caculation_Parameters['_MetalSpacing'] = _MetalSpacing
        _Caculation_Parameters['_NumOfElement'] = _NumOfElement
        _Caculation_Parameters['_ConnectLength'] = _ConnectLength
        _Caculation_Parameters['_ExtendLength'] = _ExtendLength

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Dummy_UCAP'] = self._SrefElementDeclaration(
            _DesignObj=H00_02_CapWithShield_KJH_test._CapWithShield(_DesignParameter=None,
                                                       _Name='{}:SRF_Dummy_UCAP'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Dummy_UCAP']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Dummy_UCAP']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Dummy_UCAP']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Dummy_UCAP']['_XYCoordinates'] = [[0, 0]]

        ## Calculate
        ## Target_coord
        tmpXY = []
        tmp1 = self.get_param_KJH4('SRF_CommonArray', 'SRF_CDAC_B{}'.format(_Bitsize - 1), 'SRF_Shield_ViaM{}M{}'.format(_ShieldingLayer,_LayoutOption[-1]+1), 'SRF_ViaM{}M{}'.format(_ShieldingLayer,_ShieldingLayer+1), 'BND_Met{}Layer'.format(_ShieldingLayer))
        tmp2 = self.get_param_KJH4('SRF_CommonArray', 'SRF_CDAC_B{}'.format(_Bitsize - 1), 'BND_Shield_Extend_VTC_M5')
        target_coord = [tmp1[0][-1][-1][0][0][0]['_XY_left'][0], tmp2[0][0][0][0]['_XY_up'][1]]

        ## Approaching_coord
        tmp3 = self.get_param_KJH4('SRF_Dummy_UCAP', 'BND_Shield_Extend_VTC_M5')
        approaching_coord = tmp3[0][0][0]['_XY_up_left']

        ## Sref coord
        tmp4 = self.get_param_KJH4('SRF_Dummy_UCAP')
        Scoord = tmp4[0][0]['_XY_origin']

        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define
        self._DesignParameter['SRF_Dummy_UCAP']['_XYCoordinates'] = tmpXY


        ####################################### Dummy UCAP Bottom Node Extension
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_DummyUCAP_BotExten_VTC'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}'.format(CDACBotVtcExtMetalType)][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}'.format(CDACBotVtcExtMetalType)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('BND_B{}_BotExten_VTC'.format(0))
        self._DesignParameter['BND_DummyUCAP_BotExten_VTC']['_YWidth'] = tmp[0][0]['_Ywidth'] + _DriveNodeDistance + _YWidth_Bottom_Hrz

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_DummyUCAP_BotExten_VTC']['_XWidth'] = _MetalWidth

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_DummyUCAP_BotExten_VTC']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        for i in range(_NumOfElement):
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Dummy_UCAP','SRF_UCAP', 'SRF_ECAP', 'BND_ECAP_Bot_VTC_M{}'.format(_LayoutOption[0]))
            target_coord = tmp1[0][0][i][0][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_DummyUCAP_BotExten_VTC')
            approaching_coord = tmp2[0][0]['_XY_up_left']
            ## Sref coord
            Scoord = tmp2[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_DummyUCAP_BotExten_VTC']['_XYCoordinates'] = tmpXY


        ####################################### Dummy UCAP Bottom Node Hrz
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_DummyUCAP_Bot_Hrz'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}'.format(CDACBotHrzMetalType)][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}'.format(CDACBotHrzMetalType)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_DummyUCAP_Bot_Hrz']['_YWidth'] = _YWidth_Bottom_Hrz

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('BND_DummyUCAP_BotExten_VTC')
        self._DesignParameter['BND_DummyUCAP_Bot_Hrz']['_XWidth'] = abs(tmp[-1][0]['_XY_cent'][0] - tmp[0][0]['_XY_cent'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_DummyUCAP_Bot_Hrz']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp[0][0]['_XY_down']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_DummyUCAP_Bot_Hrz')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        Scoord = tmp2[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_DummyUCAP_Bot_Hrz']['_XYCoordinates'] = tmpXY


        ## ########## Dummy Cap Bottom Node Via
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = CDACBotVtcExtMetalType
        _Caculation_Parameters['_Layer2'] = CDACBotHrzMetalType
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        ## Sref ViaX declaration
        self._DesignParameter['SRF_DummyUCAP_Bottom_ViaM{}M{}'.format(CDACBotVtcExtMetalType,CDACBotHrzMetalType)] = \
            self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                                                     _Name='{}:SRF_DummyUCAP_Bottom_ViaM{}M{}'.format(
                                                                                         _Name,
                                                                                         CDACBotVtcExtMetalType,CDACBotHrzMetalType)))[0]
        ## Define Sref Relection
        self._DesignParameter['SRF_DummyUCAP_Bottom_ViaM{}M{}'.format(CDACBotVtcExtMetalType,CDACBotHrzMetalType)]['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_DummyUCAP_Bottom_ViaM{}M{}'.format(CDACBotVtcExtMetalType,CDACBotHrzMetalType)]['_Angle'] = 0

        ## Define _COX and _COY
        tmp1 = self.get_param_KJH4('BND_B{}_BotExten_VTC'.format(_Bitsize - 1))
        ViaXwidth = abs(tmp1[0][0]['_XY_left'][0] - tmp1[_NumOfElement - 1][0]['_XY_right'][0])

        _COX, _COY = self._CalculateNumViaByXYWidth(ViaXwidth, _YWidth_Bottom_Hrz, 'MinEnclosureY')
        _Caculation_Parameters['_COX'] = max(_COX, 2)
        _Caculation_Parameters['_COY'] = _COY

        ## initialized Sref coordinate
        self._DesignParameter['SRF_DummyUCAP_Bottom_ViaM{}M{}'.format(CDACBotVtcExtMetalType,CDACBotHrzMetalType)]['_XYCoordinates'] = [[0, 0]]

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_DummyUCAP_Bottom_ViaM{}M{}'.format(CDACBotVtcExtMetalType,CDACBotHrzMetalType)]['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        for i in range(_NumOfElement):
            ## Calculate
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_DummyUCAP_Bot_Hrz')
            tmp2 = self.get_param_KJH4('BND_DummyUCAP_BotExten_VTC')
            BotExtenCentX = int((abs(tmp2[0][0]['_XY_cent'][0] + tmp2[-1][0]['_XY_cent'][0])) / 2)
            target_coord = [BotExtenCentX, tmp1[0][0]['_XY_cent'][1]]
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_DummyUCAP_Bottom_ViaM{}M{}'.format(CDACBotVtcExtMetalType,CDACBotHrzMetalType),
                                       'SRF_ViaM{}M{}'.format(CDACBotVtcExtMetalType, CDACBotVtcExtMetalType + 1),
                                       'BND_Met{}Layer'.format(CDACBotVtcExtMetalType))
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_DummyUCAP_Bottom_ViaM{}M{}'.format(CDACBotVtcExtMetalType,CDACBotHrzMetalType))
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define
        self._DesignParameter['SRF_DummyUCAP_Bottom_ViaM{}M{}'.format(CDACBotVtcExtMetalType,CDACBotHrzMetalType)]['_XYCoordinates'] = tmpXY


        ##################### Generate Sref: Dummy Capacitor Array
        _Caculation_Parameters = copy.deepcopy(H00_03_DummyCapUnit_KJH_test._DummyCapUnit._ParametersForDesignCalculation)
        _Caculation_Parameters['_LayoutOption'] = _LayoutOption
        _Caculation_Parameters['_ShieldingLayer'] = _ShieldingLayer
        _Caculation_Parameters['_MetalWidth'] = _MetalWidth
        _Caculation_Parameters['_MetalLength'] = _MetalLength
        _Caculation_Parameters['_MetalSpacing'] = _MetalSpacing

        _Caculation_Parameters['_NumOfElement'] = _NumOfElement

        _Caculation_Parameters['_ConnectLength'] = _ConnectLength
        _Caculation_Parameters['_ExtendLength'] = _ExtendLength
        _Caculation_Parameters['_DummyCap_TopBottomShort'] = _DummyCap_TopBottomShort

        self._DesignParameter['SRF_DummyCaps'] = \
            self._SrefElementDeclaration(_DesignObj=H00_03_DummyCapUnit_KJH_test.
                                         _DummyCapUnit(_DesignParameter=None,
                                                       _Name='{}:SRF_DummyCaps'))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_DummyCaps']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DummyCaps']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DummyCaps']['_DesignObj']._CalculateDesignParameter(
            **_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DummyCaps']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        ## Calculate left side dummy caps
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_CommonArray', 'SRF_CDAC_B{}'.format(_Bitsize - 1), 'SRF_UCAP', 'SRF_ECAP',
                                   'BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
        target_coord = tmp1[0][0][0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_DummyCaps', 'SRF_CapWtShield4DCAP', 'SRF_UCAP', 'SRF_ECAP',
                                   'BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
        approaching_coord = tmp2[0][0][0][0][0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_DummyCaps')
        Scoord = tmp3[0][0]['_XY_origin']

        tmp1 = self.get_param_KJH4('SRF_CommonArray', 'SRF_CDAC_B{}'.format(_Bitsize - 1), 'SRF_UCAP', 'SRF_ECAP',
                                   'BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
        _CapLength = abs(tmp1[0][0][0][-1][-1][0]['_XY_right'][0] - tmp1[0][0][0][0][0][0]['_XY_right'][0])
        Scoord[0] = Scoord[0] - _CapLength * _NumOfDummyCaps
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['SRF_DummyCaps']['_XYCoordinates'] = tmpXY
        for i in range(1, _NumOfDummyCaps):
            # 시작점 : ((2 ** i) * DistanceBtwTr)
            tmp = tmpXY[0] + [_CapLength * (i), 0]
            tmpXY.append(tmp)
        ## Calculate right side dummy caps
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_CommonArray', 'SRF_CDAC_B{}'.format(_Bitsize - 1), 'SRF_UCAP', 'SRF_ECAP',
                                   'BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
        target_coord = tmp1[0][-1][0][-1][-1][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_DummyCaps', 'SRF_CapWtShield4DCAP', 'SRF_UCAP', 'SRF_ECAP',
                                   'BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
        approaching_coord = tmp2[0][0][0][0][0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_DummyCaps')
        Scoord = tmp3[0][0]['_XY_origin']
        # Scoord[0] = Scoord[0] - _CapLength * _NumOfDummyCaps
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        for i in range(1, _NumOfDummyCaps):
            tmp = tmpXY[_NumOfDummyCaps] + [_CapLength * (i), 0]
            tmpXY.append(tmp)
        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DummyCaps']['_XYCoordinates'] = tmpXY

        ##################### Generate Sref: Dummy Capacitor Array
        _Caculation_Parameters = copy.deepcopy(H00_03_DummyCapUnit_KJH_test._DummyCapUnit._ParametersForDesignCalculation)
        _Caculation_Parameters['_LayoutOption'] = _LayoutOption
        _Caculation_Parameters['_ShieldingLayer'] = _ShieldingLayer
        _Caculation_Parameters['_MetalWidth'] = _MetalWidth
        _Caculation_Parameters['_MetalLength'] = _MetalLength
        _Caculation_Parameters['_MetalSpacing'] = _MetalSpacing

        _Caculation_Parameters['_NumOfElement'] = _NumOfElement

        _Caculation_Parameters['_ConnectLength'] = _ConnectLength
        _Caculation_Parameters['_ExtendLength'] = _ExtendLength
        _Caculation_Parameters['_DummyCap_TopBottomShort'] = _DummyCap_TopBottomShort

        self._DesignParameter['SRF_DummyCaps'] = \
            self._SrefElementDeclaration(_DesignObj=H00_03_DummyCapUnit_KJH_test.
                                         _DummyCapUnit(_DesignParameter=None,
                                                       _Name='{}:SRF_DummyCaps'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_DummyCaps']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DummyCaps']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DummyCaps']['_DesignObj']._CalculateDesignParameter(
            **_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DummyCaps']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        ## Calculate left side dummy caps
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_CommonArray', 'SRF_CDAC_B{}'.format(_Bitsize - 1), 'SRF_UCAP', 'SRF_ECAP',
                                   'BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
        target_coord = tmp1[0][0][0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_DummyCaps', 'SRF_CapWtShield4DCAP', 'SRF_UCAP', 'SRF_ECAP',
                                   'BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
        approaching_coord = tmp2[0][0][0][0][0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_DummyCaps')
        Scoord = tmp3[0][0]['_XY_origin']

        tmp1 = self.get_param_KJH4('SRF_CommonArray', 'SRF_CDAC_B{}'.format(_Bitsize - 1), 'SRF_UCAP', 'SRF_ECAP',
                                   'BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
        _CapLength = abs(tmp1[0][0][0][-1][-1][0]['_XY_right'][0] - tmp1[0][0][0][0][0][0]['_XY_right'][0])
        Scoord[0] = Scoord[0] - _CapLength * _NumOfDummyCaps
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['SRF_DummyCaps']['_XYCoordinates'] = tmpXY
        for i in range(1, _NumOfDummyCaps):
            # 시작점 : ((2 ** i) * DistanceBtwTr)
            tmp = tmpXY[0] + [_CapLength * (i), 0]
            tmpXY.append(tmp)
        ## Calculate right side dummy caps
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Dummy_UCAP', 'SRF_UCAP', 'SRF_ECAP',
                                   'BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
        target_coord = tmp1[0][0][-1][-1][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_DummyCaps', 'SRF_CapWtShield4DCAP', 'SRF_UCAP', 'SRF_ECAP',
                                   'BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
        approaching_coord = tmp2[0][0][0][0][0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_DummyCaps')
        Scoord = tmp3[0][0]['_XY_origin']
        # Scoord[0] = Scoord[0] - _CapLength * _NumOfDummyCaps
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        for i in range(1, _NumOfDummyCaps):
            tmp = tmpXY[_NumOfDummyCaps] + [_CapLength * (i), 0]
            tmpXY.append(tmp)
        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_DummyCaps']['_XYCoordinates'] = tmpXY


        if (_NumOfElement == 1) and (CDACBotVtcExtMetalType in _LayoutOption):
            ## MSB Bottom Node M5 Vtc Extension for satisfying Design Rule (M5 Minimum Space)
            ## Boundary Element Generation
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_MSBBotExtension_Vtc_M5'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL5'][0],
                _Datatype=DesignParameters._LayerMapping['METAL5'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )
            ## Define Boundary_element _YWidth
            tmp1 = self.get_param_KJH4('SRF_B{}_Bottom_ViaM{}M{}'.format(_Bitsize-1,CDACBotVtcExtMetalType,CDACBotHrzMetalType),'SRF_ViaM{}M{}'.format(CDACBotVtcExtMetalType,CDACBotVtcExtMetalType+1),'BND_Met{}Layer'.format(CDACBotVtcExtMetalType))
            tmp2 = self.get_param_KJH4('SRF_CommonArray','SRF_CDAC_B{}'.format(_Bitsize-1),'SRF_UCAP','SRF_ECAP','SRF_Bot_Vtc_ViaM{}M{}'.format(_LayoutOption[0],_LayoutOption[-1]),'SRF_ViaM{}M{}'.format(_LayoutOption[0],_LayoutOption[0]+1),'BND_Met{}Layer'.format(_LayoutOption[0]))
            self._DesignParameter['BND_MSBBotExtension_Vtc_M5']['_YWidth'] = abs(tmp1[0][0][0][0]['_XY_down'][1] - tmp2[0][0][0][0][0][0][0][0]['_XY_up'][1])

            ## Define Boundary_element _XWidth
            self._DesignParameter['BND_MSBBotExtension_Vtc_M5']['_XWidth'] = tmp2[0][0][0][0][0][0][0][0]['_Xwidth']

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_MSBBotExtension_Vtc_M5']['_XYCoordinates'] = [[0, 0]]
            ## Calculate Sref XYcoord
            tmpXY = []
            ## Calculate
            ## Approaching_coord: _XY_type2
            tmp3 = self.get_param_KJH4('BND_MSBBotExtension_Vtc_M5')
            approaching_coord = tmp3[0][0]['_XY_up']
            ## Sref coord
            tmp4 = self.get_param_KJH4('BND_MSBBotExtension_Vtc_M5')
            Scoord = tmp4[0][0]['_XY_origin']
            for i in range(2 ** (_Bitsize-1)):
            ## Target_coord: _XY_type1
                target_coord = tmp2[0][i][0][0][0][0][0][0]['_XY_up']
                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_MSBBotExtension_Vtc_M5']['_XYCoordinates'] = tmpXY






        ########################################### M7 Ctop
        ## pre_defined
        M7_YWidth = 500
        
        ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Ctop_Hrz_M7'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL7'][0],
        _Datatype=DesignParameters._LayerMapping['METAL7'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Ctop_Hrz_M7']['_YWidth'] = M7_YWidth

                ## Define Boundary_element _XWidth
        #tmp = self.get_param_KJH4('SRF_DummyCaps')
        tmp = self.get_outter_KJH4('SRF_DummyCaps')
        self._DesignParameter['BND_Ctop_Hrz_M7']['_XWidth'] = ( tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0] )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Ctop_Hrz_M7']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Ctop_Hrz_M7']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##x
        #tmp1_1 = self.get_param_KJH4('SRF_DummyCaps','SRF_CapWtShield4DCAP','SRF_UCAP','SRF_ECAP','BND_ECAP_Top_VTC_M7')
        #target_coordx = np.round(0.5*(tmp1_1[-1][0][0][0][-1][-1]['_XY_right'][0] + tmp1_1[0][0][0][0][0][0]['_XY_left'][0]))
        target_coordx = np.round(0.5*( tmp['_Mostright']['coord'][0] + tmp['_Mostleft']['coord'][0] ))
                                ##y
        tmp1_2 = self.get_param_KJH4('SRF_DummyCaps','SRF_CapWtShield4DCAP','SRF_UCAP','SRF_ECAP','BND_ECAP_Top_VTC_M7')
        target_coordy = np.round(0.5*(tmp1_2[0][0][0][0][0][0]['_XY_up'][1] + tmp1_2[0][0][0][0][0][0]['_XY_down'][1]))
        
        target_coord= [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Ctop_Hrz_M7')
        approaching_coord = tmp2[0][0]['_XY_cent']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Ctop_Hrz_M7')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Ctop_Hrz_M7']['_XYCoordinates'] = tmpXY



        
        ## Labeling: ex)METAL1PIN, METAL2PIN, METAL3PIN, METAL4PIN, METAL5PIN, METAL6PIN, METAL7PIN, METAL8PIN(IA), METAL9PIN(IB),
        self._DesignParameter['TXT_Ctop'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL7PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL7PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.1, _Angle=0, _TEXT=None,
            _XYCoordinates=None,
        )

            # Portname
        self._DesignParameter['TXT_Ctop']['_TEXT'] = 'Ctop'

            ## Calculate Sref XYcoord
        tmp = self.get_param_KJH4('BND_Ctop_Hrz_M7')
        tmpXY = tmp[0][0]['_XY_cent']
        self._DesignParameter['TXT_Ctop']['_XYCoordinates'] = [tmpXY]
        
        ## Labeling: ex)METAL1PIN, METAL2PIN, METAL3PIN, METAL4PIN, METAL5PIN, METAL6PIN, METAL7PIN, METAL8PIN(IA), METAL9PIN(IB),
        self._DesignParameter['TXT_CDummy'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL6PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.1, _Angle=0, _TEXT=None,
            _XYCoordinates=None,
        )

            # Portname
        self._DesignParameter['TXT_CDummy']['_TEXT'] = 'Cbot_dummy'

            ## Calculate Sref XYcoord
        tmp = self.get_param_KJH4('BND_DummyUCAP_Bot_Hrz')
        tmpXY = tmp[0][0]['_XY_cent']
        self._DesignParameter['TXT_CDummy']['_XYCoordinates'] = [tmpXY]
        
        for i in range(0,_Bitsize):
            ## Labeling: ex)METAL1PIN, METAL2PIN, METAL3PIN, METAL4PIN, METAL5PIN, METAL6PIN, METAL7PIN, METAL8PIN(IA), METAL9PIN(IB),
            self._DesignParameter['Cbot_{}'.format(i)] = self._TextElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL6PIN'][0],
                _Datatype=DesignParameters._LayerMapping['METAL6PIN'][1],
                _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.1, _Angle=0, _TEXT=None,
                _XYCoordinates=None,
            )
    
                # Portname
            self._DesignParameter['Cbot_{}'.format(i)]['_TEXT'] = 'Cbot_{}'.format(i)
    
                ## Calculate Sref XYcoord
            tmp = self.get_param_KJH4('BND_B{}_Bottom_Hrz'.format(i))
            tmpXY = tmp[0][0]['_XY_cent']
            self._DesignParameter['Cbot_{}'.format(i)]['_XYCoordinates'] = [tmpXY]
        

        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')



############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_ADC_H00_CDAC_v98'
    cellname = 'H00_00_CommonCentroid_v5_472'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object ''' ############################################################### ^^^^^^^^^^^^^^^^^^^^^
    InputParams = dict(
        # # Element CDAC
        _LayoutOption=[5,6],
        _ShieldingLayer=4,  # Poly:0, M1:1, M2:2 ...
        _MetalWidth=50,
        _MetalLength=1414,
        _MetalSpacing=50,

        # #Unit Cap
        _NumOfElement=2,

        # # Shielding & Top Connect node
        _ConnectLength=400,
        _ExtendLength=400,

        # # CommonCentroid Array
        _Bitsize=8, # Total bit size of CDAC

        # # Dummy Cap Option
        _DummyCap_TopBottomShort=None,
        _NumOfDummyCaps=10,  # Number of dummy cap(one side)

        # # CommonCentroid With Driving node
        _CapArrayWDrivingNodeDistance = 2000, # DRC Rule
        _DriveNodeDistance = 500, #
        _YWidth_Bottom_Hrz =50,
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
    LayoutObj = _CommonCentroid(_DesignParameter=None, _Name=cellname)
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