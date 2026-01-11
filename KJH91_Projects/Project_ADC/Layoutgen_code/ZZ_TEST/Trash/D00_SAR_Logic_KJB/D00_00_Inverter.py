## Import Basic Modules
## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC
# from KJH91_Projects.Project_ADC.Library_and_Engine import DRCv2

## Library
import copy
import time

## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A03_NmosWithDummy_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A04_PmosWithDummy_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2



############################################################################################################################################################ Class_HEADER
class _Inverter(StickDiagram_KJH1._StickDiagram_KJH):
    ##########################################################################################################################
    # Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

            # Driver(Inverter) NMOS
        _INV_NMOS_NumberofGate = None,  # number
        _INV_NMOS_ChannelWidth = None,  # number
        _INV_NMOS_Channellength = None,  # number
        _INV_NMOS_GateSpacing = None,  # None/number
        _INV_NMOS_SDWidth = None,  # None/number
        _INV_NMOS_XVT = 'SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _INV_NMOS_PCCrit = None,  # None/True

            # Source_node_ViaM1M2
        _INV_NMOS_Source_Via_TF = None,  # True/False

            # Drain_node_ViaM1M2
        _INV_NMOS_Drain_Via_TF = None,  # True/False

            # POLY dummy setting
        _INV_NMOS_Dummy = True,  # TF
            # if _PMOSDummy == True
        _INV_NMOS_Dummy_length = None,  # None/Value
        _INV_NMOS_Dummy_placement = None,  # None/'Up'/'Dn'/

        # Driver(Inverter) PMOS
        _INV_PMOS_NumberofGate=None,  # number
        _INV_PMOS_ChannelWidth=None,  # number
        _INV_PMOS_Channellength=None,  # number
        _INV_PMOS_GateSpacing=None,  # None/number
        _INV_PMOS_SDWidth=None,  # None/number
        _INV_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _INV_PMOS_PCCrit=None,  # None/True

        # Source_node_ViaM1M2
        _INV_PMOS_Source_Via_TF=None,  # True/False

        # Drain_node_ViaM1M2
        _INV_PMOS_Drain_Via_TF=None,  # True/False

        # POLY dummy setting
        _INV_PMOS_Dummy=True,  # TF
        # if _PMOSDummy == True
        _INV_PMOS_Dummy_length=None,  # None/Value
        _INV_PMOS_Dummy_placement=None,  # None/'Up'/'Dn'/
    )


    ## Initially Generated _DesignParameter
    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _Name=self._NameDeclaration(_Name=_Name),
                _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
            )


    ## DesignParameter Calculation
    def _CalculateDesignParameter(self,
                                  # NumOfDriverUnitsInDriverArray = 2^(_NumOfBits) - 1

                                  # Driver(Inverter) NMOS
                                  _INV_NMOS_NumberofGate=None,  # number
                                  _INV_NMOS_ChannelWidth=None,  # number
                                  _INV_NMOS_Channellength=None,  # number
                                  _INV_NMOS_GateSpacing=None,  # None/number
                                  _INV_NMOS_SDWidth=None,  # None/number
                                  _INV_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _INV_NMOS_PCCrit=None,  # None/True

                                  # Source_node_ViaM1M2
                                  _INV_NMOS_Source_Via_TF=None,  # True/False

                                  # Drain_node_ViaM1M2
                                  _INV_NMOS_Drain_Via_TF=None,  # True/False

                                  # POLY dummy setting
                                  _INV_NMOS_Dummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _INV_NMOS_Dummy_length=None,  # None/Value
                                  _INV_NMOS_Dummy_placement=None,  # None/'Up'/'Dn'/

                                  # Driver(Inverter) PMOS
                                  _INV_PMOS_NumberofGate=2,  # number
                                  _INV_PMOS_ChannelWidth=1000,  # number
                                  _INV_PMOS_Channellength=30,  # number
                                  _INV_PMOS_GateSpacing=None,  # None/number
                                  _INV_PMOS_SDWidth=None,  # None/number
                                  _INV_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _INV_PMOS_PCCrit=None,  # None/True

                                  # Source_node_ViaM1M2
                                  _INV_PMOS_Source_Via_TF=None,  # True/False

                                  # Drain_node_ViaM1M2
                                  _INV_PMOS_Drain_Via_TF=None,  # True/False

                                  # POLY dummy setting
                                  _INV_PMOS_Dummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _INV_PMOS_Dummy_length=None,  # None/Value
                                  _INV_PMOS_Dummy_placement=None,  # None/'Up'/'Dn'/
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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS,PMOS Sref gen:
        ## A03_NMOSwithDummy (SREF) Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A03_NmosWithDummy_KJH2._NmosWithDummy_KJH2._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOSNumberofGate'] = _INV_NMOS_NumberofGate
        _Caculation_Parameters['_NMOSChannelWidth'] =_INV_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOSChannellength'] =_INV_NMOS_Channellength
        _Caculation_Parameters['_GateSpacing'] =_INV_NMOS_GateSpacing
        _Caculation_Parameters['_SDWidth'] =_INV_NMOS_SDWidth
        _Caculation_Parameters['_XVT'] =_INV_NMOS_XVT
        _Caculation_Parameters['_PCCrit'] =_INV_NMOS_PCCrit
        _Caculation_Parameters['_Source_Via_TF'] =False #default
        _Caculation_Parameters['_Drain_Via_TF'] =True
        _Caculation_Parameters['_NMOSDummy'] = True #default
        _Caculation_Parameters['_NMOSDummy_length'] =_INV_NMOS_Dummy_length
        _Caculation_Parameters['_NMOSDummy_placement'] =_INV_NMOS_Dummy_length

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_INV_NMOS'] = self._SrefElementDeclaration(
            _DesignObj=A03_NmosWithDummy_KJH2._NmosWithDummy_KJH2(_DesignParameter=None,
                                                                  _Name='{}:SRF_INV_NMOS'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_INV_NMOS']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_INV_NMOS']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_INV_NMOS']['_DesignObj']._CalculateDesignParameter(
            **_Caculation_Parameters)

        ## initialize Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_INV_NMOS']['_XYCoordinates'] = [[0, 0]]


        ######
        ## A04_PMOSwithDummy (SREF) Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_PMOS_power_v2._PMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A04_PmosWithDummy_KJH2._PmosWithDummy_KJH2._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_PMOSPOWER_PbodyContact_1_Length']  = _PMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_PMOSNumberofGate'] = _INV_PMOS_NumberofGate
        _Caculation_Parameters['_PMOSChannelWidth'] =_INV_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOSChannellength'] =_INV_PMOS_Channellength
        _Caculation_Parameters['_GateSpacing'] =_INV_PMOS_GateSpacing
        _Caculation_Parameters['_SDWidth'] =_INV_PMOS_SDWidth
        _Caculation_Parameters['_XVT'] =_INV_PMOS_XVT
        _Caculation_Parameters['_PCCrit'] =_INV_PMOS_PCCrit
        _Caculation_Parameters['_Source_Via_TF'] =False #default
        _Caculation_Parameters['_Drain_Via_TF'] =True
        _Caculation_Parameters['_PMOSDummy'] = True #default
        _Caculation_Parameters['_PMOSDummy_length'] =_INV_PMOS_Dummy_length
        _Caculation_Parameters['_PMOSDummy_placement'] =_INV_PMOS_Dummy_length

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_INV_PMOS'] = self._SrefElementDeclaration(
            _DesignObj=A04_PmosWithDummy_KJH2._PmosWithDummy_KJH2(_DesignParameter=None,
                                                                  _Name='{}:SRF_INV_PMOS'.format(_Name)))[0]
                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_INV_PMOS']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_INV_PMOS']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_INV_PMOS']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## initialize Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_INV_PMOS']['_XYCoordinates'] = [[0, 0]]

                ##Calculate each gate coordinates
        tmpXY = []
                    ## Calculate
                        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_INV_NMOS', 'BND_{}Layer'.format(_INV_NMOS_XVT))
        target_coord = tmp1[0][0][0]['_XY_up']
                        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_INV_PMOS', 'BND_{}Layer'.format(_INV_PMOS_XVT))
        approaching_coord = tmp2[0][0][0]['_XY_down']

                        ## Sref coord
        SpaceBtwNPMOS = 460    # NAND DRC Check하면서 더 늘려보기.
        tmp3 = self.get_param_KJH4('SRF_INV_PMOS')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[1] = Scoord[1] + SpaceBtwNPMOS

                        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                        ## Define coordinates
        self._DesignParameter['SRF_INV_PMOS']['_XYCoordinates'] = tmpXY

        ### ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## N, PMOS Gate Generation :

            ## ########## ########## ########## ########## ########## NMOS Gate generation & Routing

                # ###### NMOS Poly Gate Exten Vtc poly(M0)

        NMOSPolyGateExten = 100 ##Constant
        ## Boundary_element Generation
        self._DesignParameter['BND_INV_NMOS_GateExten_Vtc_M0'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_INV_NMOS_GateExten_Vtc_M0']['_YWidth'] = NMOSPolyGateExten

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_INV_NMOS', 'BND_POLayer')
        self._DesignParameter['BND_INV_NMOS_GateExten_Vtc_M0']['_XWidth'] = tmp[0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_INV_NMOS_GateExten_Vtc_M0']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        for k in range(_INV_NMOS_NumberofGate):
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_INV_NMOS', 'BND_POLayer')
            target_coord = tmp1[0][k][0]['_XY_up_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_INV_NMOS_GateExten_Vtc_M0')
            approaching_coord = tmp2[0][0]['_XY_down_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_INV_NMOS_GateExten_Vtc_M0')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        ## Define coordinates
        self._DesignParameter['BND_INV_NMOS_GateExten_Vtc_M0']['_XYCoordinates'] = tmpXY

        if _INV_NMOS_NumberofGate > 1:

                    # ########## NMOS Gate_combine: Gate Hrz M0

            ## Boundary_element Generation
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_INV_NMOS_Gate_Hrz_M0'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )
            ## Define Boundary_element _YWidth
            self._DesignParameter['BND_INV_NMOS_Gate_Hrz_M0']['_YWidth'] = 50

            ## Define Boundary_element _XWidth
            tmp = self.get_param_KJH4('SRF_INV_NMOS', 'BND_POLayer')
            self._DesignParameter['BND_INV_NMOS_Gate_Hrz_M0']['_XWidth'] = max(abs(tmp[0][-1][0]['_XY_right'][0] - tmp[0][0][0]['_XY_left'][0]), 200)

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_INV_NMOS_Gate_Hrz_M0']['_XYCoordinates'] = [[0, 0]]

            tmpXY = []
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_INV_NMOS', 'BND_POLayer')
            tmp1_1 = self.get_param_KJH4('BND_INV_NMOS_GateExten_Vtc_M0')

            target_coord = [(tmp1[0][0][0]['_XY_left'][0] + tmp1[0][-1][0]['_XY_right'][0]) / 2, tmp1_1[0][0]['_XY_up'][1]]
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_INV_NMOS_Gate_Hrz_M0')
            approaching_coord = tmp2[0][0]['_XY_down']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_INV_NMOS_Gate_Hrz_M0')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

            ## Define coordinates
            self._DesignParameter['BND_INV_NMOS_Gate_Hrz_M0']['_XYCoordinates'] = tmpXY

                    # ########## NMOS Gate_combine: ViaM0M1

            ## Sref generation: ViaX
            ## Define ViaX Parameter
            _Caculation_Parameters0 = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
            _Caculation_Parameters0['_Layer1'] = 0
            _Caculation_Parameters0['_Layer2'] = 1
            _Caculation_Parameters0['_COX'] = None
            _Caculation_Parameters0['_COY'] = None

            self._DesignParameter['SRF_INV_NMOS_Gate_ViaM0M1'] = \
                self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None,
                                                                                         _Name='{}:SRF_INV_NMOS_Gate_ViaM0M1'.format(
                                                                                             _Name)))[0]

            ## Define Sref Relection
            self._DesignParameter['SRF_INV_NMOS_Gate_ViaM0M1']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
            self._DesignParameter['SRF_INV_NMOS_Gate_ViaM0M1']['_Angle'] = 0

            ## Calcuate Overlapped XYcoord
            tmp1 = self.get_param_KJH4('BND_INV_NMOS_Gate_Hrz_M0')
            tmp2 = self.get_param_KJH4('BND_INV_NMOS_Gate_Hrz_M0')
            Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
            _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'],
                                                        'MinEnclosureY')

            ## Define _COX and _COY
            _Caculation_Parameters0['_COX'] = max(_COX, 2)
            _Caculation_Parameters0['_COY'] = _COY

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
            self._DesignParameter['SRF_INV_NMOS_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameterYmin(
                **_Caculation_Parameters0)

            ## Calculate Sref XYcoord
            ## initialized Sref coordinate
            self._DesignParameter['SRF_INV_NMOS_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]

            tmpXY = []
            ## Calculate
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_INV_NMOS_Gate_Hrz_M0')
            target_coord = tmp1[0][0]['_XY_cent']

            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_INV_NMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']

            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_INV_NMOS_Gate_ViaM0M1')
            Scoord = tmp3[0][0]['_XY_origin']

            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

            ## Define
            self._DesignParameter['SRF_INV_NMOS_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY

        elif _INV_NMOS_NumberofGate == 1:
            tmpXY = []
            ## Sref generation: ViaX
            ## Define ViaX Parameter
            _Caculation_Parameters0 = copy.deepcopy(
                A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
            _Caculation_Parameters0['_Layer1'] = 0
            _Caculation_Parameters0['_Layer2'] = 1
            _Caculation_Parameters0['_COX'] = 1
            _Caculation_Parameters0['_COY'] = 2

            self._DesignParameter['SRF_INV_NMOS_Gate_ViaM0M1'] = \
                self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None,
                                                                                         _Name='{}:SRF_INV_NMOS_Gate_ViaM0M1'.format(
                                                                                             _Name)))[0]

            ## Define Sref Relection
            self._DesignParameter['SRF_INV_NMOS_Gate_ViaM0M1']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
            self._DesignParameter['SRF_INV_NMOS_Gate_ViaM0M1']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
            self._DesignParameter['SRF_INV_NMOS_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameterXmin(
                **_Caculation_Parameters0)

            ## Calculate Sref XYcoord
            ## initialized Sref coordinate
            self._DesignParameter['SRF_INV_NMOS_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]

            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_INV_NMOS_GateExten_Vtc_M0')
            target_coord = tmp1[0][0]['_XY_up']

            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_INV_NMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']

            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_INV_NMOS_Gate_ViaM0M1')
            Scoord = tmp3[0][0]['_XY_origin']

            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

            ## Define
            self._DesignParameter['SRF_INV_NMOS_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY

                ## ########## ########## ########## ########## ########## PMOS Gate generation & Routing

                    # PMOS Poly Gate Extension Vtc M0(poly)

        PMOSPolyGateExtension = 100
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_INV_PMOS_GateExten_Vtc_M0'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_INV_PMOS_GateExten_Vtc_M0']['_YWidth'] = PMOSPolyGateExtension

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_INV_PMOS', 'BND_POLayer')
        self._DesignParameter['BND_INV_PMOS_GateExten_Vtc_M0']['_XWidth'] = tmp[0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_INV_PMOS_GateExten_Vtc_M0']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        for k in range(_INV_PMOS_NumberofGate):
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_INV_PMOS', 'BND_POLayer')
            target_coord = tmp1[0][k][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_INV_PMOS_GateExten_Vtc_M0')
            approaching_coord = tmp2[0][0]['_XY_up_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_INV_PMOS_GateExten_Vtc_M0')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        ## Define coordinates
        self._DesignParameter['BND_INV_PMOS_GateExten_Vtc_M0']['_XYCoordinates'] = tmpXY


        if _INV_PMOS_NumberofGate > 1:

                    # ########## PMOS Gate_combine: Gate Hrz M0

                # PMOS Gate Horizontal M0
            ## Boundary_element Generation
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_INV_PMOS_Gate_Hrz_M0'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )
            ## Define Boundary_element _YWidth
            self._DesignParameter['BND_INV_PMOS_Gate_Hrz_M0']['_YWidth'] = 50

            ## Define Boundary_element _XWidth
            tmp = self.get_param_KJH4('SRF_INV_PMOS', 'BND_POLayer')
            self._DesignParameter['BND_INV_PMOS_Gate_Hrz_M0']['_XWidth'] = max(abs(tmp[0][-1][0]['_XY_right'][0] - tmp[0][0][0]['_XY_left'][0]), 200)

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_INV_PMOS_Gate_Hrz_M0']['_XYCoordinates'] = [[0, 0]]

            tmpXY = []
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_INV_PMOS', 'BND_POLayer')
            tmp1_1 = self.get_param_KJH4('BND_INV_PMOS_GateExten_Vtc_M0')

            target_coord = [(tmp1[0][0][0]['_XY_left'][0] + tmp1[0][-1][0]['_XY_right'][0]) / 2, tmp1_1[0][0]['_XY_down'][1]]
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_INV_PMOS_Gate_Hrz_M0')
            approaching_coord = tmp2[0][0]['_XY_up']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_INV_PMOS_Gate_Hrz_M0')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

            ## Define coordinates
            self._DesignParameter['BND_INV_PMOS_Gate_Hrz_M0']['_XYCoordinates'] = tmpXY


            ## ########## PMOS Gate_combine: Gate Hrz M1
            ## Boundary_element Generation
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_INV_PMOS_Gate_Hrz_M1'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )
            ## Define Boundary_element _YWidth
            self._DesignParameter['BND_INV_PMOS_Gate_Hrz_M1']['_YWidth'] = 50

            ## Define Boundary_element _XWidth
            tmp = self.get_param_KJH4('BND_INV_PMOS_Gate_Hrz_M0')
            self._DesignParameter['BND_INV_PMOS_Gate_Hrz_M1']['_XWidth'] = tmp[0][0]['_Xwidth']

            ## Define Boundary_element _XYCoordinates
            tmp = self.get_param_KJH4('BND_INV_PMOS_Gate_Hrz_M0')
            self._DesignParameter['BND_INV_PMOS_Gate_Hrz_M1']['_XYCoordinates'] = tmpXY


            ## ########## PMOS Gate_combine: ViaM0M1
            ## Sref generation: ViaX
            ## Define ViaX Parameter
            _Caculation_Parameters0 = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
            _Caculation_Parameters0['_Layer1'] = 0
            _Caculation_Parameters0['_Layer2'] = 1
            _Caculation_Parameters0['_COX'] = None
            _Caculation_Parameters0['_COY'] = None

            self._DesignParameter['SRF_INV_PMOS_Gate_ViaM0M1'] = \
                self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None,
                                                                                         _Name='{}:SRF_INV_PMOS_Gate_ViaM0M1'.format(_Name)))[0]

            ## Define Sref Relection
            self._DesignParameter['SRF_INV_PMOS_Gate_ViaM0M1']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
            self._DesignParameter['SRF_INV_PMOS_Gate_ViaM0M1']['_Angle'] = 0

            ## Calcuate Overlapped XYcoord
            tmp1 = self.get_param_KJH4('BND_INV_PMOS_Gate_Hrz_M0')
            tmp2 = self.get_param_KJH4('BND_INV_PMOS_Gate_Hrz_M1')
            Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
            _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'],'MinEnclosureY')

            ## Define _COX and _COY
            _Caculation_Parameters0['_COX'] = max(_COX, 2)
            _Caculation_Parameters0['_COY'] = _COY

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
            self._DesignParameter['SRF_INV_PMOS_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters0)

            ## Calculate Sref XYcoord
            ## initialized Sref coordinate
            self._DesignParameter['SRF_INV_PMOS_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]

            tmpXY = []
            ## Calculate
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_INV_PMOS_Gate_Hrz_M0')
            target_coord = tmp1[0][0]['_XY_cent']

            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_INV_PMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_POLayer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']

            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_INV_PMOS_Gate_ViaM0M1')
            Scoord = tmp3[0][0]['_XY_origin']

            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

            ## Define
            self._DesignParameter['SRF_INV_PMOS_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY

        elif _INV_PMOS_NumberofGate == 1:
            tmpXY = []
            ## Sref generation: ViaX
            ## Define ViaX Parameter
            _Caculation_Parameters0 = copy.deepcopy(
                A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
            _Caculation_Parameters0['_Layer1'] = 0
            _Caculation_Parameters0['_Layer2'] = 1
            _Caculation_Parameters0['_COX'] = 1
            _Caculation_Parameters0['_COY'] = 2

            self._DesignParameter['SRF_INV_PMOS_Gate_ViaM0M1'] = \
                self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None,
                                                                                         _Name='{}:SRF_INV_PMOS_Gate_ViaM0M1'.format(_Name)))[0]

            ## Define Sref Relection
            self._DesignParameter['SRF_INV_PMOS_Gate_ViaM0M1']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
            self._DesignParameter['SRF_INV_PMOS_Gate_ViaM0M1']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
            self._DesignParameter['SRF_INV_PMOS_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters0)

            ## Calculate Sref XYcoord
            ## initialized Sref coordinate
            self._DesignParameter['SRF_INV_PMOS_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]

            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_INV_PMOS_GateExten_Vtc_M0')
            target_coord = tmp1[0][0]['_XY_down']

            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_INV_PMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_POLayer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']

            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_INV_PMOS_Gate_ViaM0M1')
            Scoord = tmp3[0][0]['_XY_origin']

            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

            ## Define
            self._DesignParameter['SRF_INV_PMOS_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY

        ### ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## N, PMOS Gate roughting :

                ## NMOS, PMOS Gate roughting Path M1

        ## Boundary_element Generation
        self._DesignParameter['BND_INV_Gate_Vtc_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_INV_PMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_INV_NMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
        self._DesignParameter['BND_INV_Gate_Vtc_M1']['_YWidth'] = abs(
            tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1])

        ## Define Boundary_element _XWidth
        GateVtcPathWidth = 50
        self._DesignParameter['BND_INV_Gate_Vtc_M1']['_XWidth'] = GateVtcPathWidth

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_INV_Gate_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp2[0][0][0][0]['_XY_down']

        ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_INV_Gate_Vtc_M1')
        approaching_coord = tmp3[0][0]['_XY_down']

        ## Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define coordinates
        self._DesignParameter['BND_INV_Gate_Vtc_M1']['_XYCoordinates'] = tmpXY

                ## NMOS, PMOS Drain roughting Path M2 Vtc & Hrz
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        if _INV_NMOS_NumberofGate <= 2 :
            self._DesignParameter['BND_INV_Drain_Vtc_M2'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )

            ## Define Boundary_element _YWidth
            tmp1 = self.get_param_KJH4('SRF_INV_PMOS','SRF_Drain_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
            tmp2 = self.get_param_KJH4('SRF_INV_NMOS','SRF_Drain_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
            self._DesignParameter['BND_INV_Drain_Vtc_M2']['_YWidth'] = abs(tmp1[0][0][0][0][0]['_XY_down'][1] - tmp2[0][0][0][0][0]['_XY_up'][1])

            ## Define Boundary_element _XWidth
            self._DesignParameter['BND_INV_Drain_Vtc_M2']['_XWidth'] = 50

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_INV_Drain_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
            tmpXY = []
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_INV_NMOS','SRF_Drain_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
            target_coord = tmp1[0][0][0][0][0]['_XY_up_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_INV_Drain_Vtc_M2')
            approaching_coord = tmp2[0][0]['_XY_down_left']

            Scoord = tmp2[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_INV_Drain_Vtc_M2']['_XYCoordinates'] = tmpXY
        else :
            # NMOS & PMOS Drain Roughting Vertical M2
            self._DesignParameter['BND_INV_Drain_Vtc_M2'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )

            ## Define Boundary_element _YWidth
            tmp1 = self.get_param_KJH4('SRF_INV_PMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
            tmp2 = self.get_param_KJH4('SRF_INV_NMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
            self._DesignParameter['BND_INV_Drain_Vtc_M2']['_YWidth'] = abs(tmp1[0][0][0][0][0]['_XY_down'][1] - tmp2[0][0][0][0][0]['_XY_up'][1])

            ## Define Boundary_element _XWidth
            self._DesignParameter['BND_INV_Drain_Vtc_M2']['_XWidth'] = 50

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_INV_Drain_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
            tmpXY = []
            tmpnum= self.get_param_KJH4('SRF_INV_NMOS','SRF_Drain_ViaM1M2')
            num=len(tmpnum[0])
            for i in range(num) :

                self._DesignParameter['BND_INV_Drain_Vtc_M2']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                ## Target_coord: _XY_type1
                tmp1 = self.get_param_KJH4('SRF_INV_NMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                target_coord = tmp1[0][i][0][0][0]['_XY_up_left']
                ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('BND_INV_Drain_Vtc_M2')
                approaching_coord = tmp2[0][0]['_XY_down_left']

                Scoord = tmp2[0][0]['_XY_origin']
                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)

            ## Define coordinates
            self._DesignParameter['BND_INV_Drain_Vtc_M2']['_XYCoordinates'] = tmpXY

            # NMOS Drain Roughting Horizental M2
            self._DesignParameter['BND_INV_NmosDrain_Hrz_M2'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )

            ## Define Boundary_element _YWidth
            self._DesignParameter['BND_INV_NmosDrain_Hrz_M2']['_YWidth'] = 50

            ## Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH4('SRF_INV_NMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
            self._DesignParameter['BND_INV_NmosDrain_Hrz_M2']['_XWidth'] = abs(tmp1[0][0][0][0][0]['_XY_left'][0] - tmp1[0][-1][0][0][0]['_XY_right'][0])

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_INV_NmosDrain_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
            tmpXY = []
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_INV_NMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
            target_coord = tmp1[0][0][0][0][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_INV_NmosDrain_Hrz_M2')
            approaching_coord = tmp2[0][0]['_XY_down_left']

            Scoord = tmp2[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

            ## Define coordinates
            self._DesignParameter['BND_INV_NmosDrain_Hrz_M2']['_XYCoordinates'] = tmpXY

            # PMOS Drain Roughting Horizental M2
            self._DesignParameter['BND_INV_PmosDrain_Hrz_M2'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )

            ## Define Boundary_element _YWidth
            self._DesignParameter['BND_INV_PmosDrain_Hrz_M2']['_YWidth'] = 50

            ## Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH4('SRF_INV_PMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
            self._DesignParameter['BND_INV_PmosDrain_Hrz_M2']['_XWidth'] = abs(tmp1[0][0][0][0][0]['_XY_left'][0] - tmp1[0][-1][0][0][0]['_XY_right'][0])

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_INV_PmosDrain_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
            tmpXY = []
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_INV_PMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
            target_coord = tmp1[0][0][0][0][0]['_XY_up_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_INV_PmosDrain_Hrz_M2')
            approaching_coord = tmp2[0][0]['_XY_up_left']

            Scoord = tmp2[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

            ## Define coordinates
            self._DesignParameter['BND_INV_PmosDrain_Hrz_M2']['_XYCoordinates'] = tmpXY

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ADC_D00_SARLogic_Inverter'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'D00_00_Inverter_v0_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
            # Driver(Inverter) NMOS
        _INV_NMOS_NumberofGate = 5,  # number
        _INV_NMOS_ChannelWidth = 340,  # number
        _INV_NMOS_Channellength = 30,  # number
        _INV_NMOS_GateSpacing = None,  # None/number
        _INV_NMOS_SDWidth = None,  # None/number
        _INV_NMOS_XVT = 'SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _INV_NMOS_PCCrit = None,  # None/True

            # Source_node_ViaM1M2
        _INV_NMOS_Source_Via_TF = False,  # True/False

            # Drain_node_ViaM1M2
        _INV_NMOS_Drain_Via_TF = True,  # True/False

            # POLY dummy setting
        _INV_NMOS_Dummy = True,  # TF
            # if _PMOSDummy == True
        _INV_NMOS_Dummy_length = None,  # None/Value
        _INV_NMOS_Dummy_placement = None,  # None/'Up'/'Dn'/

        # Driver(Inverter) PMOS
        _INV_PMOS_NumberofGate = 5,  # number
        _INV_PMOS_ChannelWidth=900,  # number
        _INV_PMOS_Channellength=30,  # number
        _INV_PMOS_GateSpacing=None,  # None/number
        _INV_PMOS_SDWidth=None,  # None/number
        _INV_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _INV_PMOS_PCCrit=None,  # None/True

        # Source_node_ViaM1M2
        _INV_PMOS_Source_Via_TF=False,  # True/False

        # Drain_node_ViaM1M2
        _INV_PMOS_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _INV_PMOS_Dummy=True,  # TF
        # if _PMOSDummy == True
        _INV_PMOS_Dummy_length=None,  # None/Value
        _INV_PMOS_Dummy_placement=None,  # None/'Up'/'Dn'/
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
    LayoutObj = _Inverter(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    #testStreamFile = open('./{}'.format(_fileName), 'wb')
    testStreamFile = open('./gdsfiles/{}'.format(_fileName), 'wb')
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
