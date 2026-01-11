## Import Basic Modules
## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC
# from KJH91_Projects.Project_ADC.Library_and_Engine import DRCv2

## Library
import copy
import math
import time

## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A03_NmosWithDummy_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A04_PmosWithDummy_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3



############################################################################################################################################################ Class_HEADER
class _DriverCell(StickDiagram_KJH1._StickDiagram_KJH):
    ##########################################################################################################################
    # Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

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
        print('##################################')
        print('##      Calculation_Start       ##')
        print('##################################')

        # Pre-defined Design Value


        ## A03_NMOSwithDummy (SREF) Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A03_NmosWithDummy_KJH2._NmosWithDummy_KJH2._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOSNumberofGate'] = _Driver_NMOS_NumberofGate
        _Caculation_Parameters['_NMOSChannelWidth'] =_Driver_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOSChannellength'] =_Driver_NMOS_Channellength
        _Caculation_Parameters['_GateSpacing'] =_Driver_NMOS_GateSpacing
        _Caculation_Parameters['_SDWidth'] =_Driver_NMOS_SDWidth
        _Caculation_Parameters['_XVT'] =_Driver_NMOS_XVT
        _Caculation_Parameters['_PCCrit'] =_Driver_NMOS_PCCrit
        _Caculation_Parameters['_Source_Via_TF'] =True #default
        _Caculation_Parameters['_Drain_Via_TF'] =True
        _Caculation_Parameters['_NMOSDummy'] = True #default
        _Caculation_Parameters['_NMOSDummy_length'] =_Driver_NMOS_Dummy_length
        _Caculation_Parameters['_NMOSDummy_placement'] =_Driver_NMOS_Dummy_length

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Driver_NMOS'] = self._SrefElementDeclaration(
            _DesignObj=A03_NmosWithDummy_KJH2._NmosWithDummy_KJH2(_DesignParameter=None,
                                                                  _Name='{}:SRF_Driver_NMOS'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Driver_NMOS']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Driver_NMOS']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Driver_NMOS']['_DesignObj']._CalculateDesignParameter(
            **_Caculation_Parameters)

        ## initialize Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Driver_NMOS']['_XYCoordinates'] = [[0, 0]]


        ######
        ## A04_PMOSwithDummy (SREF) Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_PMOS_power_v2._PMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A04_PmosWithDummy_KJH2._PmosWithDummy_KJH2._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_PMOSPOWER_PbodyContact_1_Length']  = _PMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_PMOSNumberofGate'] = _Driver_PMOS_NumberofGate
        _Caculation_Parameters['_PMOSChannelWidth'] =_Driver_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOSChannellength'] =_Driver_PMOS_Channellength
        _Caculation_Parameters['_GateSpacing'] =_Driver_PMOS_GateSpacing
        _Caculation_Parameters['_SDWidth'] =_Driver_PMOS_SDWidth
        _Caculation_Parameters['_XVT'] =_Driver_PMOS_XVT
        _Caculation_Parameters['_PCCrit'] =_Driver_PMOS_PCCrit
        _Caculation_Parameters['_Source_Via_TF'] =True #default
        _Caculation_Parameters['_Drain_Via_TF'] =True
        _Caculation_Parameters['_PMOSDummy'] = True #default
        _Caculation_Parameters['_PMOSDummy_length'] =_Driver_PMOS_Dummy_length
        _Caculation_Parameters['_PMOSDummy_placement'] =_Driver_PMOS_Dummy_length

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Driver_PMOS'] = self._SrefElementDeclaration(
            _DesignObj=A04_PmosWithDummy_KJH2._PmosWithDummy_KJH2(_DesignParameter=None,
                                                                  _Name='{}:SRF_Driver_PMOS'.format(_Name)))[0]
        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Driver_PMOS']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Driver_PMOS']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Driver_PMOS']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## initialize Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Driver_PMOS']['_XYCoordinates'] = [[0, 0]]


        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Driver_NMOS', 'BND_{}Layer'.format(_Driver_NMOS_XVT))
        target_coord = tmp1[0][0][0]['_XY_up']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_Driver_PMOS', 'BND_{}Layer'.format(_Driver_PMOS_XVT))
        approaching_coord = tmp2[0][0][0]['_XY_down']

        ## Sref coord
        SpaceBtwNPMOS = 500    # drc margin
        tmp3 = self.get_param_KJH4('SRF_Driver_PMOS')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[1] = Scoord[1] + SpaceBtwNPMOS

        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['SRF_Driver_PMOS']['_XYCoordinates'] = tmpXY


        ##### N, PMOS Gate Routing
        # NMOS Poly Gate Extension Vtc M0
        NMOSPolyGateExtension = 120
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Driver_NMOS_GateExtension_Vtc_M0'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Driver_NMOS_GateExtension_Vtc_M0']['_YWidth'] = NMOSPolyGateExtension

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Driver_NMOS', 'BND_POLayer')
        self._DesignParameter['BND_Driver_NMOS_GateExtension_Vtc_M0']['_XWidth'] = tmp[0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Driver_NMOS_GateExtension_Vtc_M0']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        for k in range(_Driver_NMOS_NumberofGate):
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Driver_NMOS', 'BND_POLayer')
            target_coord = tmp1[0][k][0]['_XY_up_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Driver_NMOS_GateExtension_Vtc_M0')
            approaching_coord = tmp2[0][0]['_XY_down_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Driver_NMOS_GateExtension_Vtc_M0')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        ## Define coordinates
        self._DesignParameter['BND_Driver_NMOS_GateExtension_Vtc_M0']['_XYCoordinates'] = tmpXY


        if _Driver_NMOS_NumberofGate > 1:
            ## ########## NMOS Gate_combine: Gate Hrz M0
            # NMOS Gate Horizontal M0
            ## Boundary_element Generation
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_Driver_NMOS_Gate_Hrz_M0'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )
            ## Define Boundary_element _YWidth
            self._DesignParameter['BND_Driver_NMOS_Gate_Hrz_M0']['_YWidth'] = 50

            ## Define Boundary_element _XWidth
            tmp = self.get_param_KJH4('SRF_Driver_NMOS', 'BND_POLayer')
            self._DesignParameter['BND_Driver_NMOS_Gate_Hrz_M0']['_XWidth'] = max(abs(tmp[0][-1][0]['_XY_right'][0] - tmp[0][0][0]['_XY_left'][0]), 200)

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_Driver_NMOS_Gate_Hrz_M0']['_XYCoordinates'] = [[0, 0]]

            tmpXY = []
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Driver_NMOS', 'BND_POLayer')
            tmp1_1 = self.get_param_KJH4('BND_Driver_NMOS_GateExtension_Vtc_M0')

            target_coord = [(tmp1[0][0][0]['_XY_left'][0] + tmp1[0][-1][0]['_XY_right'][0]) / 2, tmp1_1[0][0]['_XY_up'][1]]
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Driver_NMOS_Gate_Hrz_M0')
            approaching_coord = tmp2[0][0]['_XY_down']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Driver_NMOS_Gate_Hrz_M0')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

            ## Define coordinates
            self._DesignParameter['BND_Driver_NMOS_Gate_Hrz_M0']['_XYCoordinates'] = tmpXY


            ## ########## Gate_combine: Gate Hrz M3
            ## Boundary_element Generation
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_Driver_NMOS_Gate_Hrz_M2'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )
            ## Define Boundary_element _YWidth
            self._DesignParameter['BND_Driver_NMOS_Gate_Hrz_M2']['_YWidth'] = 50

            ## Define Boundary_element _XWidth
            tmp = self.get_param_KJH4('BND_Driver_NMOS_Gate_Hrz_M0')
            self._DesignParameter['BND_Driver_NMOS_Gate_Hrz_M2']['_XWidth'] = tmp[0][0]['_Xwidth']

            ## Define Boundary_element _XYCoordinates
            tmp = self.get_param_KJH4('BND_Driver_NMOS_Gate_Hrz_M2')
            self._DesignParameter['BND_Driver_NMOS_Gate_Hrz_M2']['_XYCoordinates'] = tmpXY


            ## ########## NMOS Gate_combine: ViaM0M1
            ## Sref generation: ViaX
            ## Define ViaX Parameter
            _Caculation_Parameters0 = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
            _Caculation_Parameters0['_Layer1'] = 0
            _Caculation_Parameters0['_Layer2'] = 1
            _Caculation_Parameters0['_COX'] = None
            _Caculation_Parameters0['_COY'] = None

            self._DesignParameter['SRF_Driver_NMOS_Gate_ViaM0M1'] = \
                self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                                                         _Name='{}:SRF_Driver_NMOS_Gate_ViaM0M1'.format(_Name)))[0]

            ## Define Sref Relection
            self._DesignParameter['SRF_Driver_NMOS_Gate_ViaM0M1']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
            self._DesignParameter['SRF_Driver_NMOS_Gate_ViaM0M1']['_Angle'] = 0

            ## Calcuate Overlapped XYcoord
            tmp1 = self.get_param_KJH4('BND_Driver_NMOS_Gate_Hrz_M0')
            tmp2 = self.get_param_KJH4('BND_Driver_NMOS_Gate_Hrz_M2')
            Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
            _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'],'MinEnclosureY')

            ## Define _COX and _COY
            _Caculation_Parameters0['_COX'] = max(_COX, 2)
            _Caculation_Parameters0['_COY'] = _COY

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
            self._DesignParameter['SRF_Driver_NMOS_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters0)

            ## Calculate Sref XYcoord
            ## initialized Sref coordinate
            self._DesignParameter['SRF_Driver_NMOS_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]

            tmpXY = []
            ## Calculate
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_Driver_NMOS_Gate_Hrz_M2')
            target_coord = tmp1[0][0]['_XY_cent']

            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_Driver_NMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']

            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Driver_NMOS_Gate_ViaM0M1')
            Scoord = tmp3[0][0]['_XY_origin']

            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

            ## Define
            self._DesignParameter['SRF_Driver_NMOS_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY

        elif _Driver_NMOS_NumberofGate == 1:
            tmpXY = []
            ## Sref generation: ViaX
            ## Define ViaX Parameter
            _Caculation_Parameters0 = copy.deepcopy(
                A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
            _Caculation_Parameters0['_Layer1'] = 0
            _Caculation_Parameters0['_Layer2'] = 1
            _Caculation_Parameters0['_COX'] = 1
            _Caculation_Parameters0['_COY'] = 2

            self._DesignParameter['SRF_Driver_NMOS_Gate_ViaM0M1'] = \
                self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                                                         _Name='{}:SRF_Driver_NMOS_Gate_ViaM0M1'.format(_Name)))[0]

            ## Define Sref Relection
            self._DesignParameter['SRF_Driver_NMOS_Gate_ViaM0M1']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
            self._DesignParameter['SRF_Driver_NMOS_Gate_ViaM0M1']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
            self._DesignParameter['SRF_Driver_NMOS_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters0)

            ## Calculate Sref XYcoord
            ## initialized Sref coordinate
            self._DesignParameter['SRF_Driver_NMOS_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]

            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_Driver_NMOS_GateExtension_Vtc_M0')
            target_coord = tmp1[0][0]['_XY_up']

            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_Driver_NMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']

            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Driver_NMOS_Gate_ViaM0M1')
            Scoord = tmp3[0][0]['_XY_origin']

            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

            ## Define
            self._DesignParameter['SRF_Driver_NMOS_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY


        ## PMOS Poly Gate Extension Vtc M0
        PMOSPolyGateExtension = 120
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Driver_PMOS_GateExtension_Vtc_M0'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Driver_PMOS_GateExtension_Vtc_M0']['_YWidth'] = PMOSPolyGateExtension

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Driver_PMOS', 'BND_POLayer')
        self._DesignParameter['BND_Driver_PMOS_GateExtension_Vtc_M0']['_XWidth'] = tmp[0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Driver_PMOS_GateExtension_Vtc_M0']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        for k in range(_Driver_PMOS_NumberofGate):
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Driver_PMOS', 'BND_POLayer')
            target_coord = tmp1[0][k][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Driver_PMOS_GateExtension_Vtc_M0')
            approaching_coord = tmp2[0][0]['_XY_up_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Driver_PMOS_GateExtension_Vtc_M0')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        ## Define coordinates
        self._DesignParameter['BND_Driver_PMOS_GateExtension_Vtc_M0']['_XYCoordinates'] = tmpXY


        if _Driver_PMOS_NumberofGate > 1:
            ## ########## PMOS Gate_combine: Gate Hrz M0
            # PMOS Gate Horizontal M0
            ## Boundary_element Generation
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_Driver_PMOS_Gate_Hrz_M0'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )
            ## Define Boundary_element _YWidth
            self._DesignParameter['BND_Driver_PMOS_Gate_Hrz_M0']['_YWidth'] = 50

            ## Define Boundary_element _XWidth
            tmp = self.get_param_KJH4('SRF_Driver_PMOS', 'BND_POLayer')
            self._DesignParameter['BND_Driver_PMOS_Gate_Hrz_M0']['_XWidth'] = max(abs(tmp[0][-1][0]['_XY_right'][0] - tmp[0][0][0]['_XY_left'][0]), 200)

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_Driver_PMOS_Gate_Hrz_M0']['_XYCoordinates'] = [[0, 0]]

            tmpXY = []
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Driver_PMOS', 'BND_POLayer')
            tmp1_1 = self.get_param_KJH4('BND_Driver_PMOS_GateExtension_Vtc_M0')

            target_coord = [(tmp1[0][0][0]['_XY_left'][0] + tmp1[0][-1][0]['_XY_right'][0]) / 2, tmp1_1[0][0]['_XY_down'][1]]
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Driver_PMOS_Gate_Hrz_M0')
            approaching_coord = tmp2[0][0]['_XY_up']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Driver_PMOS_Gate_Hrz_M0')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

            ## Define coordinates
            self._DesignParameter['BND_Driver_PMOS_Gate_Hrz_M0']['_XYCoordinates'] = tmpXY


            ## ########## PMOS Gate_combine: Gate Hrz M1
            ## Boundary_element Generation
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_Driver_PMOS_Gate_Hrz_M1'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )
            ## Define Boundary_element _YWidth
            self._DesignParameter['BND_Driver_PMOS_Gate_Hrz_M1']['_YWidth'] = 50

            ## Define Boundary_element _XWidth
            tmp = self.get_param_KJH4('BND_Driver_PMOS_Gate_Hrz_M0')
            self._DesignParameter['BND_Driver_PMOS_Gate_Hrz_M1']['_XWidth'] = tmp[0][0]['_Xwidth']

            ## Define Boundary_element _XYCoordinates
            tmp = self.get_param_KJH4('BND_Driver_PMOS_Gate_Hrz_M0')
            self._DesignParameter['BND_Driver_PMOS_Gate_Hrz_M1']['_XYCoordinates'] = tmpXY


            ## ########## PMOS Gate_combine: ViaM0M1
            ## Sref generation: ViaX
            ## Define ViaX Parameter
            _Caculation_Parameters0 = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
            _Caculation_Parameters0['_Layer1'] = 0
            _Caculation_Parameters0['_Layer2'] = 1
            _Caculation_Parameters0['_COX'] = None
            _Caculation_Parameters0['_COY'] = None

            self._DesignParameter['SRF_Driver_PMOS_Gate_ViaM0M1'] = \
                self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                                                         _Name='{}:SRF_Driver_PMOS_Gate_ViaM0M1'.format(_Name)))[0]

            ## Define Sref Relection
            self._DesignParameter['SRF_Driver_PMOS_Gate_ViaM0M1']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
            self._DesignParameter['SRF_Driver_PMOS_Gate_ViaM0M1']['_Angle'] = 0

            ## Calcuate Overlapped XYcoord
            tmp1 = self.get_param_KJH4('BND_Driver_PMOS_Gate_Hrz_M0')
            tmp2 = self.get_param_KJH4('BND_Driver_PMOS_Gate_Hrz_M1')
            Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
            _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'],'MinEnclosureY')

            ## Define _COX and _COY
            _Caculation_Parameters0['_COX'] = max(_COX, 2)
            _Caculation_Parameters0['_COY'] = _COY

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
            self._DesignParameter['SRF_Driver_PMOS_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters0)

            ## Calculate Sref XYcoord
            ## initialized Sref coordinate
            self._DesignParameter['SRF_Driver_PMOS_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]

            tmpXY = []
            ## Calculate
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_Driver_PMOS_Gate_Hrz_M0')
            target_coord = tmp1[0][0]['_XY_cent']

            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_Driver_PMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_POLayer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']

            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Driver_PMOS_Gate_ViaM0M1')
            Scoord = tmp3[0][0]['_XY_origin']

            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

            ## Define
            self._DesignParameter['SRF_Driver_PMOS_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY

        elif _Driver_PMOS_NumberofGate == 1:
            tmpXY = []
            ## Sref generation: ViaX
            ## Define ViaX Parameter
            _Caculation_Parameters0 = copy.deepcopy(
                A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
            _Caculation_Parameters0['_Layer1'] = 0
            _Caculation_Parameters0['_Layer2'] = 1
            _Caculation_Parameters0['_COX'] = 1
            _Caculation_Parameters0['_COY'] = 2

            self._DesignParameter['SRF_Driver_PMOS_Gate_ViaM0M1'] = \
                self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                                                         _Name='{}:SRF_Driver_PMOS_Gate_ViaM0M1'.format(_Name)))[0]

            ## Define Sref Relection
            self._DesignParameter['SRF_Driver_PMOS_Gate_ViaM0M1']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
            self._DesignParameter['SRF_Driver_PMOS_Gate_ViaM0M1']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
            self._DesignParameter['SRF_Driver_PMOS_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters0)

            ## Calculate Sref XYcoord
            ## initialized Sref coordinate
            self._DesignParameter['SRF_Driver_PMOS_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]

            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_Driver_PMOS_GateExtension_Vtc_M0')
            target_coord = tmp1[0][0]['_XY_down']

            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_Driver_PMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_POLayer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']

            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Driver_PMOS_Gate_ViaM0M1')
            Scoord = tmp3[0][0]['_XY_origin']

            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

            ## Define
            self._DesignParameter['SRF_Driver_PMOS_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY


        ## NMOS, PMOS Gate routing Path M1
        ## Boundary_element Generation
        self._DesignParameter['BND_Driver_Gate_Vtc_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Driver_PMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_Driver_NMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
        self._DesignParameter['BND_Driver_Gate_Vtc_M1']['_YWidth'] = abs(tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1])

        spaceBtwgateHrzM1 = 500

        gateHrzWidth = min(tmp1[0][0][0][0]['_Xwidth'], tmp2[0][0][0][0]['_Xwidth'])
        numOfgateHrzM1 = int(gateHrzWidth/spaceBtwgateHrzM1) - 3
        if numOfgateHrzM1 < 0:
            numOfgateHrzM1 = 0
        OneSideNumOfgateHrzM1 = int(numOfgateHrzM1/2)

        ## Define Boundary_element _XWidth
        GateVtcPathWidth = 50
        self._DesignParameter['BND_Driver_Gate_Vtc_M1']['_XWidth'] =GateVtcPathWidth

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Driver_Gate_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp2[0][0][0][0]['_XY_down']

        ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_Driver_Gate_Vtc_M1')
        approaching_coord = tmp3[0][0]['_XY_down']

        ## Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        Cent_Scoord = New_Scoord

        for i in range(OneSideNumOfgateHrzM1):
            New_Scoord = copy.deepcopy(Cent_Scoord)
            New_Scoord[0] = Cent_Scoord[0] + spaceBtwgateHrzM1 * (i+1)
            tmpXY.append(New_Scoord)

        for i in range(OneSideNumOfgateHrzM1):
            New_Scoord = copy.deepcopy(Cent_Scoord)
            New_Scoord[0] = Cent_Scoord[0] - spaceBtwgateHrzM1 * (i+1)
            tmpXY.append(New_Scoord)

        ## Define coordinates
        self._DesignParameter['BND_Driver_Gate_Vtc_M1']['_XYCoordinates'] = tmpXY
#################################################################################


        ##### N, PMOS Drain Routing
        ## NMOS Drain M2 <-> M3 Viastack generation
        ## Source Viastack (M2~M3)
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        ## Sref ViaX declaration
        self._DesignParameter['SRF_NMOS_Drain_ViaM2M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                        _Name='{}:SRF_NMOS_Drain_ViaM2M3'.format(_Name)))[0]
        ## Define Sref Relection
        self._DesignParameter['SRF_NMOS_Drain_ViaM2M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_NMOS_Drain_ViaM2M3']['_Angle'] = 0

        tmp1 = self.get_param_KJH4('SRF_Driver_NMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
        ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(tmp1[0][0][0][0][0]['_Xwidth'], tmp1[0][0][0][0][0]['_Ywidth'],
                                                    'MinEnclosureX')

        ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_NMOS_Drain_ViaM2M3']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

        ## initialized Sref coordinate
        self._DesignParameter['SRF_NMOS_Drain_ViaM2M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        NumOfDrainPerTr = int((_Driver_NMOS_NumberofGate + 1) / 2)
        for i in range(NumOfDrainPerTr):
            ## Target_coord
            tmp1 = self.get_param_KJH4('SRF_Driver_NMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
            target_coord = tmp1[0][i][0][0][0]['_XY_cent']

            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_NMOS_Drain_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met3Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']

            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_NMOS_Drain_ViaM2M3')
            Scoord = tmp3[0][0]['_XY_origin']

            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        ## Define
        self._DesignParameter['SRF_NMOS_Drain_ViaM2M3']['_XYCoordinates'] = tmpXY


        ## PMOS Source M2 <-> M6 Viastack generation
        ## Source Viastack (M2~M6) (PMOS Source <-> VREFN M6)
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        ## Sref ViaX declaration
        self._DesignParameter['SRF_PMOS_Drain_ViaM2M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                        _Name='{}:SRF_PMOS_Drain_ViaM2M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_PMOS_Drain_ViaM2M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_PMOS_Drain_ViaM2M3']['_Angle'] = 0

        tmp1 = self.get_param_KJH4('SRF_Driver_PMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
        ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(tmp1[0][0][0][0][0]['_Xwidth'], tmp1[0][0][0][0][0]['_Ywidth'],
                                                    'MinEnclosureX')

        ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_PMOS_Drain_ViaM2M3']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

        ## initialized Sref coordinate
        self._DesignParameter['SRF_PMOS_Drain_ViaM2M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        NumOfDrainPerTr = int((_Driver_PMOS_NumberofGate + 1) / 2)
        for i in range(NumOfDrainPerTr):
            ## Target_coord
            tmp1 = self.get_param_KJH4('SRF_Driver_PMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
            target_coord = tmp1[0][i][0][0][0]['_XY_cent']

            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_PMOS_Drain_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met3Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']

            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_PMOS_Drain_ViaM2M3')
            Scoord = tmp3[0][0]['_XY_origin']

            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        ## Define
        self._DesignParameter['SRF_PMOS_Drain_ViaM2M3']['_XYCoordinates'] = tmpXY


        ## PMOS Drain Extension Vtc M3
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Driver_PMOS_DrainExtension_Vtc_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('SRF_PMOS_Drain_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met3Layer')
        tmp1 =  self.get_param_KJH4('BND_Driver_PMOS_GateExtension_Vtc_M0')

        self._DesignParameter['BND_Driver_PMOS_DrainExtension_Vtc_M3']['_YWidth'] = abs(tmp1[0][0]['_XY_down'][1] - tmp[0][0][0][0]['_XY_down'][1])
        # PMOSDrainExtension = 100
        #self._DesignParameter['BND_Driver_PMOS_DrainExtension_Vtc_M3']['_YWidth'] = PMOSDrainExtension

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Driver_PMOS_DrainExtension_Vtc_M3']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Driver_PMOS_DrainExtension_Vtc_M3']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        for k in range(NumOfDrainPerTr):
            ## Calculate
            ## Target_coord: _XY_type1
            target_coord = tmp[k][0][0][0]['_XY_down_left']

            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Driver_PMOS_DrainExtension_Vtc_M3')
            approaching_coord = tmp2[0][0]['_XY_up_left']

            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Driver_PMOS_DrainExtension_Vtc_M3')
            Scoord = tmp3[0][0]['_XY_origin']

            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        ## Define coordinates
        self._DesignParameter['BND_Driver_PMOS_DrainExtension_Vtc_M3']['_XYCoordinates'] = tmpXY


        ## ########## N, PMOS Drain_combine: Drain Hrz M3
        # PMOS Gate Horizontal M0
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Driver_Drain_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        DrainHrzM4PathWidth = 50
        self._DesignParameter['BND_Driver_Drain_Hrz_M3']['_YWidth'] = DrainHrzM4PathWidth

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Driver_NMOS', 'BND_Met1Layer_Drain')
        tmp2 = self.get_param_KJH4('SRF_Driver_PMOS', 'BND_Met1Layer_Drain')
        MostRightSide = max(tmp1[0][-1][0]['_XY_right'][0], tmp2[0][-1][0]['_XY_right'][0])
        MostLeftSide = min(tmp1[0][0][0]['_XY_left'][0], tmp2[0][0][0]['_XY_left'][0])
        self._DesignParameter['BND_Driver_Drain_Hrz_M3']['_XWidth'] = MostRightSide - MostLeftSide

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Driver_Drain_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        tmp3 = self.get_param_KJH4('BND_Driver_PMOS_DrainExtension_Vtc_M3')
        target_coord = [min(tmp1[0][0][0]['_XY_left'][0], tmp2[0][0][0]['_XY_left'][0]), tmp3[0][0]['_XY_down'][1]]

        ## Approaching_coord: _XY_type2
        tmp4 = self.get_param_KJH4('BND_Driver_Drain_Hrz_M3')
        approaching_coord = tmp4[0][0]['_XY_up_left']
        ## Sref coord
        Scoord = tmp4[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define coordinates
        self._DesignParameter['BND_Driver_Drain_Hrz_M3']['_XYCoordinates'] = tmpXY


        ## Output Node Viastack (M3~M4)
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        ## Sref ViaX declaration
        self._DesignParameter['SRF_DrainOutput_ViaM3M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                        _Name='{}:SRF_DrainOutput_ViaM3M4'.format(_Name)))[0]
        ## Define Sref Relection
        self._DesignParameter['SRF_DrainOutput_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_DrainOutput_ViaM3M4']['_Angle'] = 0

        if _Driver_NMOS_NumberofGate == _Driver_PMOS_NumberofGate and (_Driver_NMOS_NumberofGate == 1 or _Driver_NMOS_NumberofGate == 2):
            _Caculation_Parameters['_COX'] = 1
            _Caculation_Parameters['_COY'] = 2

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
            self._DesignParameter['SRF_DrainOutput_ViaM3M4']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

        else:
            tmp1 = self.get_param_KJH4('BND_Driver_Drain_Hrz_M3')
            tmp2 = self.get_param_KJH4('BND_Driver_Drain_Hrz_M3')   # M3 면적 안에 최대한 박고 이후 M4 생성
            Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
            _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

            ## Define _COX and _COY
            _Caculation_Parameters['_COX'] = max(_COX, 2)
            _Caculation_Parameters['_COY'] = max(_COY, 1)

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
            self._DesignParameter['SRF_DrainOutput_ViaM3M4']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## initialized Sref coordinate
        self._DesignParameter['SRF_DrainOutput_ViaM3M4']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_Driver_Drain_Hrz_M3')
        target_coord = tmp1[0][0]['_XY_cent']

        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_DrainOutput_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']

        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_DrainOutput_ViaM3M4')
        Scoord = tmp3[0][0]['_XY_origin']

        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define
        self._DesignParameter['SRF_DrainOutput_ViaM3M4']['_XYCoordinates'] = tmpXY


#######################################
        ############################
        ## Driver output Node Hrz M4
        ## Boundary_element Generation
        self._DesignParameter['BND_Output_Node_Hrz_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        tmp1 = self.get_param_KJH4('BND_Driver_Drain_Hrz_M3')
        tmp2 = self.get_param_KJH4('SRF_Driver_PMOS', 'BND_PODummyLayer')
        self._DesignParameter['BND_Output_Node_Hrz_M4']['_XWidth'] = abs(tmp1[0][0]['_XY_left'][0] - tmp2[0][-1][0]['_XY_right'][0]) + 53

        ## Define Boundary_element _XWidth
        OutputHrzPathWidth = 50
        self._DesignParameter['BND_Output_Node_Hrz_M4']['_YWidth'] = OutputHrzPathWidth

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Output_Node_Hrz_M4']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        tmp3 = self.get_param_KJH4('SRF_DrainOutput_ViaM3M4', 'SRF_ViaM3M4', 'BND_Met4Layer')
        target_coord = [tmp1[0][0]['_XY_left'][0], tmp3[0][0][0][0]['_XY_up'][1]]

        ## Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Output_Node_Hrz_M4')
        approaching_coord = tmp2[0][0]['_XY_up_left']

        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Output_Node_Hrz_M4')
        Scoord = tmp3[0][0]['_XY_origin']

        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)


        ## Define
        self._DesignParameter['BND_Output_Node_Hrz_M4']['_XYCoordinates'] = tmpXY


        ## NMOS Drain Extension Vtc M3
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Driver_NMOS_DrainExtension_Vtc_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('SRF_NMOS_Drain_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met3Layer')
        tmp1 = self.get_param_KJH4('BND_Driver_Drain_Hrz_M3')
        self._DesignParameter['BND_Driver_NMOS_DrainExtension_Vtc_M3']['_YWidth'] = abs(
            tmp1[0][0]['_XY_down'][1] - tmp[0][0][0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Driver_NMOS_DrainExtension_Vtc_M3']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Driver_NMOS_DrainExtension_Vtc_M3']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        NumOfDrainPerTr = int((_Driver_NMOS_NumberofGate + 1) / 2)
        for k in range(NumOfDrainPerTr):
            ## Calculate
            ## Target_coord: _XY_type1
            target_coord = tmp[k][0][0][0]['_XY_up_left']

            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Driver_NMOS_DrainExtension_Vtc_M3')
            approaching_coord = tmp2[0][0]['_XY_down_left']

            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Driver_NMOS_DrainExtension_Vtc_M3')
            Scoord = tmp3[0][0]['_XY_origin']

            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        ## Define coordinates
        self._DesignParameter['BND_Driver_NMOS_DrainExtension_Vtc_M3']['_XYCoordinates'] = tmpXY


        ############################비아까지만 올려놓고 Array에서 한번에 VREF(M6)로 묶을 예정#################################
        ## NMOS Source M2 <-> M6 Viastack generation
        ## Source Viastack (M2~M6) (NMOS Source <-> VREFN M6)
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 6
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        ## Sref ViaX declaration
        self._DesignParameter['SRF_NMOSSourceVREFN_ViaM2M6'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                        _Name='{}:SRF_NMOSSourceVREFN_ViaM2M6'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_NMOSSourceVREFN_ViaM2M6']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_NMOSSourceVREFN_ViaM2M6']['_Angle'] = 0

        tmp1 = self.get_param_KJH4('SRF_Driver_NMOS', 'SRF_Source_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
        ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(tmp1[0][0][0][0][0]['_Xwidth'], tmp1[0][0][0][0][0]['_Ywidth'], 'MinEnclosureX')

        ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_NMOSSourceVREFN_ViaM2M6']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)

        ## initialized Sref coordinate
        self._DesignParameter['SRF_NMOSSourceVREFN_ViaM2M6']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        NumOfSourcePerTr = math.ceil((_Driver_NMOS_NumberofGate+1)/2)
        for i in range(NumOfSourcePerTr):
            ## Target_coord
            tmp1 = self.get_param_KJH4('SRF_Driver_NMOS', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2','BND_Met2Layer')
            target_coord = tmp1[0][i][0][0][0]['_XY_cent']

            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_NMOSSourceVREFN_ViaM2M6', 'SRF_ViaM5M6', 'BND_Met6Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']

            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_NMOSSourceVREFN_ViaM2M6')
            Scoord = tmp3[0][0]['_XY_origin']

            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        ## Define
        self._DesignParameter['SRF_NMOSSourceVREFN_ViaM2M6']['_XYCoordinates'] = tmpXY


        ## PMOS Source M2 <-> M6 Viastack generation
        ## Source Viastack (M2~M6) (PMOS Source <-> VREFP M6)
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 6
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        ## Sref ViaX declaration
        self._DesignParameter['SRF_PMOSSourceVREFP_ViaM2M6'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                        _Name='{}:SRF_PMOSSourceVREFP_ViaM2M6'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_PMOSSourceVREFP_ViaM2M6']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_PMOSSourceVREFP_ViaM2M6']['_Angle'] = 0

        tmp1 = self.get_param_KJH4('SRF_Driver_PMOS', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(tmp1[0][0][0][0][0]['_Xwidth'], tmp1[0][0][0][0][0]['_Ywidth'],
                                                    'MinEnclosureX')

        ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_PMOSSourceVREFP_ViaM2M6']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)

        ## initialized Sref coordinate
        self._DesignParameter['SRF_PMOSSourceVREFP_ViaM2M6']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        NumOfSourcePerTr = math.ceil((_Driver_PMOS_NumberofGate + 1) / 2)
        for i in range(NumOfSourcePerTr):
            ## Target_coord
            tmp1 = self.get_param_KJH4('SRF_Driver_PMOS', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
            target_coord = tmp1[0][i][0][0][0]['_XY_cent']

            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_PMOSSourceVREFP_ViaM2M6', 'SRF_ViaM5M6', 'BND_Met6Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']

            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_PMOSSourceVREFP_ViaM2M6')
            Scoord = tmp3[0][0]['_XY_origin']

            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        ## Define
        self._DesignParameter['SRF_PMOSSourceVREFP_ViaM2M6']['_XYCoordinates'] = tmpXY


        ############################
        ## Driver input Node Hrz M2
        ## Boundary_element Generation
        self._DesignParameter['BND_Input_Node_Hrz_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        if _Driver_NMOS_NumberofGate == 1:
            tmp1 = self.get_param_KJH4('SRF_Driver_NMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            tmp2 = self.get_param_KJH4('SRF_Driver_NMOS', 'BND_PODummyLayer')
            self._DesignParameter['BND_Input_Node_Hrz_M2']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0]['_XY_left'][0]) + 53
        else:
            tmp1 = self.get_param_KJH4('BND_Driver_NMOS_Gate_Hrz_M2')
            tmp2 = self.get_param_KJH4('SRF_Driver_NMOS', 'BND_PODummyLayer')
            self._DesignParameter['BND_Input_Node_Hrz_M2']['_XWidth'] = abs(tmp1[0][0]['_XY_right'][0] - tmp2[0][0][0]['_XY_left'][0]) + 53

        ## Define Boundary_element _XWidth
        InputHrzPathWidth = 50
        self._DesignParameter['BND_Input_Node_Hrz_M2']['_YWidth'] = InputHrzPathWidth

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Input_Node_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        if _Driver_NMOS_NumberofGate == 1:
            target_coord = [tmp2[0][0][0]['_XY_left'][0] - 53, tmp1[0][0][0][0]['_XY_down'][1]]
        else:
            target_coord = [tmp2[0][0][0]['_XY_left'][0] - 53, tmp1[0][0]['_XY_down'][1]]
        ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_Input_Node_Hrz_M2')
        approaching_coord = tmp3[0][0]['_XY_down_left']

        ## Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define coordinates
        self._DesignParameter['BND_Input_Node_Hrz_M2']['_XYCoordinates'] = tmpXY


        ## ########## Gate Node <->Input Node Via ViaM1M2
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters0 = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters0['_Layer1'] = 1
        _Caculation_Parameters0['_Layer2'] = 2
        if _Driver_NMOS_NumberofGate == 1:
            _Caculation_Parameters0['_COX'] = 1
            _Caculation_Parameters0['_COY'] = 2
        else:
            tmp1 = self.get_param_KJH4('SRF_Driver_NMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            _COX, _COY = self._CalculateNumViaByXYWidth(tmp1[0][0][0][0]['_Xwidth'], tmp1[0][0][0][0]['_Ywidth'], None)
            _Caculation_Parameters0['_COX'] = _COX
            _Caculation_Parameters0['_COY'] = 1

        self._DesignParameter['SRF_Driver_GateInput_ViaM1M2'] = \
            self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                                                     _Name='{}:SRF_Driver_GateInput_ViaM1M2'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_Driver_GateInput_ViaM1M2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_Driver_GateInput_ViaM1M2']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        if _Driver_NMOS_NumberofGate == 1:
            self._DesignParameter['SRF_Driver_GateInput_ViaM1M2']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters0)
        else:
            self._DesignParameter['SRF_Driver_GateInput_ViaM1M2']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters0)

        ## Calculate Sref XYcoord
        ## initialized Sref coordinate
        self._DesignParameter['SRF_Driver_GateInput_ViaM1M2']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        ## Calculate
        if _Driver_NMOS_NumberofGate == 1:
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_Input_Node_Hrz_M2')
            target_coord = tmp1[0][0]['_XY_up_right']

            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_Driver_GateInput_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_down_right']

        else:
            ## Target_coord
            tmp1 = self.get_param_KJH4('SRF_Driver_NMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            target_coord = tmp1[0][0][0][0]['_XY_down']

            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_Driver_GateInput_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_down']

        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Driver_GateInput_ViaM1M2')
        Scoord = tmp3[0][0]['_XY_origin']

        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define
        self._DesignParameter['SRF_Driver_GateInput_ViaM1M2']['_XYCoordinates'] = tmpXY






############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_YJH
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ADC_H01_CDAC_Driver_YJH'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'H01_01_DriverUnit_v0_92'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
            # Driver(Inverter) NMOS
        _Driver_NMOS_NumberofGate = 64,  # number
        _Driver_NMOS_ChannelWidth = 3600,  # number
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
        _Driver_NMOS_Dummy_placement = None,  # None/'Up'/'Dn'/

        # Driver(Inverter) PMOS
        _Driver_PMOS_NumberofGate = 64,  # number
        _Driver_PMOS_ChannelWidth=8100,  # number
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
    LayoutObj = _DriverCell(_DesignParameter=None, _Name=cellname)
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
