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
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A08_PbodyContactPhyLen_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A03_NmosWithDummy_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A04_PmosWithDummy_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A14_Mosfet_KJH3



############################################################################################################################################################ Class_HEADER
class _DriverCell(StickDiagram_KJH1._StickDiagram_KJH):
    ##########################################################################################################################
    # Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(
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
        _CDACDrv_PMOS_NumberofGate=5,  # Number
        _CDACDrv_PMOS_ChannelWidth = 879, #Number
        _CDACDrv_PMOS_ChannelLength = 30, #Number

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
        _CDACDrv_PMOS_NumberofGate=5,  # Number
        _CDACDrv_PMOS_ChannelWidth = 879, #Number
        _CDACDrv_PMOS_ChannelLength = 30, #Number

                                  ):

        ## Class_HEADER: Pre Defined Parameter Before Calculation
        ## Load DRC library
        _DRCObj = DRC.DRC()
        ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']
        ## CALCULATION START
        DriverCell_start_time = time.time()
        print('##################################')
        print('##      Calculation_Start       ##')
        print('##################################')
        ## Pre-defined
        PolyGateCombineLength = 100


        ##################################################################################################################
        ## A03_NMOSwithDummy (SREF) Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A14_Mosfet_KJH3._Mosfet._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_MosType']                      = 'NMOS'
        _Caculation_Parameters['_MosUpDn']                      = 'Up'

        _Caculation_Parameters['_NumberofGate']                 = _CDACDrv_NMOS_NumberofGate
        _Caculation_Parameters['_ChannelWidth']                 = _CDACDrv_NMOS_ChannelWidth
        _Caculation_Parameters['_ChannelLength']                = _CDACDrv_NMOS_ChannelLength
        _Caculation_Parameters['_GateSpacing']                  = None
        _Caculation_Parameters['_SDWidth']                      = None
        _Caculation_Parameters['_XVT']                          = _CDACDrv_XVT
        _Caculation_Parameters['_PCCrit']                       = True

        _Caculation_Parameters['_Source_Via_TF']                = True
        _Caculation_Parameters['_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_Source_Comb_TF']               = None
        _Caculation_Parameters['_Source_Comb_POpinward_TF']     = None
        _Caculation_Parameters['_Source_Comb_Length']           = None

        _Caculation_Parameters['_Drain_Via_TF']                 = True
        _Caculation_Parameters['_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_Drain_Comb_TF']                = False
        _Caculation_Parameters['_Drain_Comb_POpinward_TF']      = False
        _Caculation_Parameters['_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PODummy_TF']                   = True
        _Caculation_Parameters['_PODummy_Length']               = None
        _Caculation_Parameters['_PODummy_Placement']            = 'Up'

        _Caculation_Parameters['_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_POGate_Comb_TF']               = True
        _Caculation_Parameters['_POGate_Comb_length']           = PolyGateCombineLength
        _Caculation_Parameters['_POGate_Via_TF']                = True
        _Caculation_Parameters['_POGate_ViaMxMx']               = [0,2]

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Driver_NMOS'] = self._SrefElementDeclaration(_DesignObj=A14_Mosfet_KJH3._Mosfet(_DesignParameter=None,_Name='{}:SRF_Driver_NMOS'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Driver_NMOS']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Driver_NMOS']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Driver_NMOS']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## initialize Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Driver_NMOS']['_XYCoordinates'] = [[0, 0]]

        ##################################################################################################################
        ######
        ## A04_PMOSwithDummy (SREF) Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_PMOS_power_v2._PMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A14_Mosfet_KJH3._Mosfet._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_PMOSPOWER_PbodyContact_1_Length']  = _PMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_MosType']                      = 'PMOS'
        _Caculation_Parameters['_MosUpDn']                      = 'Dn'

        _Caculation_Parameters['_NumberofGate']                 = _CDACDrv_PMOS_NumberofGate
        _Caculation_Parameters['_ChannelWidth']                 = _CDACDrv_PMOS_ChannelWidth
        _Caculation_Parameters['_ChannelLength']                = _CDACDrv_PMOS_ChannelLength
        _Caculation_Parameters['_GateSpacing']                  = None
        _Caculation_Parameters['_SDWidth']                      = None
        _Caculation_Parameters['_XVT']                          = _CDACDrv_XVT
        _Caculation_Parameters['_PCCrit']                       = True

        _Caculation_Parameters['_Source_Via_TF']                = True
        _Caculation_Parameters['_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_Source_Comb_TF']               = None
        _Caculation_Parameters['_Source_Comb_POpinward_TF']     = None
        _Caculation_Parameters['_Source_Comb_Length']           = None

        _Caculation_Parameters['_Drain_Via_TF']                 = True
        _Caculation_Parameters['_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_Drain_Comb_TF']                = False
        _Caculation_Parameters['_Drain_Comb_POpinward_TF']      = False
        _Caculation_Parameters['_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PODummy_TF']                   = True
        _Caculation_Parameters['_PODummy_Length']               = None
        _Caculation_Parameters['_PODummy_Placement']            = 'Dn'

        _Caculation_Parameters['_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_Xvt_Placement']                = 'Up'

        _Caculation_Parameters['_POGate_Comb_TF']               = True
        _Caculation_Parameters['_POGate_Comb_length']           = PolyGateCombineLength
        _Caculation_Parameters['_POGate_Via_TF']                = True
        _Caculation_Parameters['_POGate_ViaMxMx']               = [0,1]

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Driver_PMOS'] = self._SrefElementDeclaration(_DesignObj=A14_Mosfet_KJH3._Mosfet(_DesignParameter=None,_Name='{}:SRF_Driver_PMOS'.format(_Name)))[0]

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
        tmp1 = self.get_param_KJH4('SRF_Driver_NMOS', 'BND_{}Layer'.format(_CDACDrv_XVT))
        target_coord = tmp1[0][0][0]['_XY_up']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_Driver_PMOS', 'BND_{}Layer'.format(_CDACDrv_XVT))
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

        ##################################################################################################################
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
        tmp = self.get_param_KJH4('SRF_Driver_NMOS','BND_Gate_Hrz_Mx')
        self._DesignParameter['BND_Driver_NMOS_Gate_Hrz_M2']['_XWidth'] = tmp[0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Driver_NMOS_Gate_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Driver_NMOS', 'BND_Gate_Hrz_Mx')
        target_coord = tmp1[0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Driver_NMOS_Gate_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Driver_NMOS_Gate_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define coordinates
        self._DesignParameter['BND_Driver_NMOS_Gate_Hrz_M2']['_XYCoordinates'] = tmpXY
        ##################################################################################################################

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
        tmp1 = self.get_param_KJH4('SRF_Driver_NMOS', 'BND_Gate_Hrz_Mx')
        tmp2 = self.get_param_KJH4('SRF_Driver_PMOS', 'BND_Gate_Hrz_Mx')
        self._DesignParameter['BND_Driver_Gate_Vtc_M1']['_YWidth'] = abs(tmp1[0][0][0]['_XY_down'][1] - tmp2[0][0][0]['_XY_up'][1])

        spaceBtwgateHrzM1 = 500

        gateHrzWidth = min(tmp1[0][0][0]['_Xwidth'], tmp2[0][0][0]['_Xwidth'])
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
        target_coord = tmp2[0][0][0]['_XY_up']

        ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_Driver_Gate_Vtc_M1')
        approaching_coord = tmp3[0][0]['_XY_up']

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

        ##################################################################################################################
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
        self._DesignParameter['SRF_NMOS_Drain_ViaM2M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,_Name='{}:SRF_NMOS_Drain_ViaM2M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_NMOS_Drain_ViaM2M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_NMOS_Drain_ViaM2M3']['_Angle'] = 0

        tmp1 = self.get_param_KJH4('SRF_Driver_NMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
        ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(tmp1[0][0][0][0][0]['_Xwidth'], tmp1[0][0][0][0][0]['_Ywidth'],'MinEnclosureX')

        ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_NMOS_Drain_ViaM2M3']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

        ## initialized Sref coordinate
        self._DesignParameter['SRF_NMOS_Drain_ViaM2M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        NumOfDrainPerTr = int((_CDACDrv_NMOS_NumberofGate + 1) / 2)
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

        ##################################################################################################################
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
        self._DesignParameter['SRF_PMOS_Drain_ViaM2M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,_Name='{}:SRF_PMOS_Drain_ViaM2M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_PMOS_Drain_ViaM2M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_PMOS_Drain_ViaM2M3']['_Angle'] = 0

        tmp1 = self.get_param_KJH4('SRF_Driver_PMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
        ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(tmp1[0][0][0][0][0]['_Xwidth'], tmp1[0][0][0][0][0]['_Ywidth'],'MinEnclosureX')

        ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_PMOS_Drain_ViaM2M3']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

        ## initialized Sref coordinate
        self._DesignParameter['SRF_PMOS_Drain_ViaM2M3']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        NumOfDrainPerTr = int((_CDACDrv_PMOS_NumberofGate + 1) / 2)
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
        ##################################################################################################################

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
        tmp1 =  self.get_param_KJH4('SRF_Driver_PMOS','BND_Gate_Hrz_Mx')

        self._DesignParameter['BND_Driver_PMOS_DrainExtension_Vtc_M3']['_YWidth'] = abs(tmp1[0][0][0]['_XY_down'][1] - tmp[0][0][0][0]['_XY_down'][1])
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

        ##################################################################################################################
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
        tmp1 = self.get_param_KJH4('SRF_Driver_NMOS', 'BND_Drain_M1')
        tmp2 = self.get_param_KJH4('SRF_Driver_PMOS', 'BND_Drain_M1')
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
        approaching_coord = tmp4[0][0]['_XY_down_left']
        ## Sref coord
        Scoord = tmp4[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define coordinates
        self._DesignParameter['BND_Driver_Drain_Hrz_M3']['_XYCoordinates'] = tmpXY

        ##################################################################################################################

        ## Output Node Viastack (M3~M4)
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        ## Sref ViaX declaration
        self._DesignParameter['SRF_DrainOutput_ViaM3M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,_Name='{}:SRF_DrainOutput_ViaM3M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_DrainOutput_ViaM3M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_DrainOutput_ViaM3M4']['_Angle'] = 0

        if _CDACDrv_NMOS_NumberofGate == _CDACDrv_PMOS_NumberofGate and (_CDACDrv_NMOS_NumberofGate == 1 or _CDACDrv_NMOS_NumberofGate == 2):
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

        ##################################################################################################################
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

        ##################################################################################################################
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
        self._DesignParameter['BND_Driver_NMOS_DrainExtension_Vtc_M3']['_YWidth'] = abs(tmp1[0][0]['_XY_down'][1] - tmp[0][0][0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Driver_NMOS_DrainExtension_Vtc_M3']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Driver_NMOS_DrainExtension_Vtc_M3']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        NumOfDrainPerTr = int((_CDACDrv_NMOS_NumberofGate + 1) / 2)
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

        ##################################################################################################################

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
        self._DesignParameter['SRF_NMOSSourceVREFN_ViaM2M6'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,_Name='{}:SRF_NMOSSourceVREFN_ViaM2M6'.format(_Name)))[0]

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
        NumOfSourcePerTr = math.ceil((_CDACDrv_NMOS_NumberofGate+1)/2)
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

        ##################################################################################################################
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
        self._DesignParameter['SRF_PMOSSourceVREFP_ViaM2M6'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,_Name='{}:SRF_PMOSSourceVREFP_ViaM2M6'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_PMOSSourceVREFP_ViaM2M6']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_PMOSSourceVREFP_ViaM2M6']['_Angle'] = 0

        tmp1 = self.get_param_KJH4('SRF_Driver_PMOS', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(tmp1[0][0][0][0][0]['_Xwidth'], tmp1[0][0][0][0][0]['_Ywidth'],'MinEnclosureX')

        ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_PMOSSourceVREFP_ViaM2M6']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

        ## initialized Sref coordinate
        self._DesignParameter['SRF_PMOSSourceVREFP_ViaM2M6']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        NumOfSourcePerTr = math.ceil((_CDACDrv_PMOS_NumberofGate + 1) / 2)
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
        ##################################################################################################################

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
        ## Define Boundary_element _XWidth
        if _CDACDrv_NMOS_NumberofGate == 1:
            tmp1 = self.get_param_KJH4('SRF_Driver_NMOS','SRF_Gate_ViaM0Mx','SRF_ViaM0M1', 'BND_Met1Layer')
            tmp2 = self.get_param_KJH4('SRF_Driver_NMOS', 'BND_PODummyLayer')
            self._DesignParameter['BND_Input_Node_Hrz_M2']['_XWidth'] = abs(tmp1[0][0][0][0][0]['_XY_right'][0] - tmp2[0][0][0]['_XY_left'][0]) + 53
        else:
            tmp1 = self.get_param_KJH4('BND_Driver_NMOS_Gate_Hrz_M2')
            tmp2 = self.get_param_KJH4('SRF_Driver_NMOS', 'BND_PODummyLayer')
            self._DesignParameter['BND_Input_Node_Hrz_M2']['_XWidth'] = abs(tmp1[0][0]['_XY_right'][0] - tmp2[0][0][0]['_XY_left'][0]) + 53

        ## Define Boundary_element _YWidth
        InputHrzPathWidth = 50
        self._DesignParameter['BND_Input_Node_Hrz_M2']['_YWidth'] = InputHrzPathWidth

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Input_Node_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        if _CDACDrv_NMOS_NumberofGate == 1:
            target_coord = [tmp2[0][0][0]['_XY_left'][0] - 53, tmp1[0][0][0][0][0]['_XY_down'][1]]
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

        ##################################################################################################################
        ##################################################################################################################
        ##################################################################################################################
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')
        DriverCell_end_time = time.time()
        self.DriverCell_elapsed_time = DriverCell_end_time - DriverCell_start_time
        ##################################################################################################################

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ZZ01_H01_00_DriverCell_Fixed'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'H01_01_DriverUnit_v0_92'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
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
    # Checker.lib_deletion()
    Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()

    print('#############################      Finished      ################################')
    print('{} Hours   {} minutes   {} seconds'.format(h, m, s))
# end of 'main():' ---------------------------------------------------------------------------------------------
