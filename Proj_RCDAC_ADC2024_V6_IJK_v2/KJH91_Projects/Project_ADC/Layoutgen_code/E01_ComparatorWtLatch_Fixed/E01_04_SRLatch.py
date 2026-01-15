
## Import Basic Modules
    ## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_ADC.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

    ## Library
import copy
import math
import numpy as np
import time

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.E02_Comparator_And_Fixed import E02_02_Nand_KJH0

## Define Class
class _SRLatch(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
## SRLatch
    ## Common
        # XVT
        _SRLatch_XVT='SLVT',
        # Body
        _SRLatch_NMOSAB_Pbody_XvtTop2Pbody=None,  # Number/None(Minimum)
        _SRLatch_PMOSAB_Nbody_Xvtdown2Nbody=None,  # Number/None(Minimum)
        # Height
        _SRLatch_PMOSXvt2NMOSXvt=1150,  # number
    ## Nand(Set,Rst same)
        # NmosA
        _SRLatch_Nand_NMOSA_NumberofGate=1,  # Number
        _SRLatch_Nand_NMOSA_ChannelWidth=100,  # Number
        _SRLatch_Nand_NMOSA_ChannelLength=30,  # Number
        # NMOSB
        _SRLatch_Nand_NMOSB_NumberofGate=2,  # Number
        _SRLatch_Nand_NMOSB_ChannelWidth=750,  # Number
        _SRLatch_Nand_NMOSB_ChannelLength=30,  # Number
        # PMOSA
        _SRLatch_Nand_PMOSA_NumberofGate=2,  # Number
        _SRLatch_Nand_PMOSA_ChannelWidth=100,  # Number
        _SRLatch_Nand_PMOSA_ChannelLength=30,  # Number
        # PMOSB
        _SRLatch_Nand_PMOSB_NumberofGate=3,  # Number
        _SRLatch_Nand_PMOSB_ChannelWidth=750,  # Number
        _SRLatch_Nand_PMOSB_ChannelLength=30,  # Number

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
## SRLatch
    ## Common
        # XVT
        _SRLatch_XVT='SLVT',
        # Body
        _SRLatch_NMOSAB_Pbody_XvtTop2Pbody=None,  # Number/None(Minimum)
        _SRLatch_PMOSAB_Nbody_Xvtdown2Nbody=None,  # Number/None(Minimum)
        # Height
        _SRLatch_PMOSXvt2NMOSXvt=1150,  # number
    ## Nand(Set,Rst same)
        # NmosA
        _SRLatch_Nand_NMOSA_NumberofGate=1,  # Number
        _SRLatch_Nand_NMOSA_ChannelWidth=100,  # Number
        _SRLatch_Nand_NMOSA_ChannelLength=30,  # Number
        # NMOSB
        _SRLatch_Nand_NMOSB_NumberofGate=2,  # Number
        _SRLatch_Nand_NMOSB_ChannelWidth=750,  # Number
        _SRLatch_Nand_NMOSB_ChannelLength=30,  # Number
        # PMOSA
        _SRLatch_Nand_PMOSA_NumberofGate=2,  # Number
        _SRLatch_Nand_PMOSA_ChannelWidth=100,  # Number
        _SRLatch_Nand_PMOSA_ChannelLength=30,  # Number
        # PMOSB
        _SRLatch_Nand_PMOSB_NumberofGate=3,  # Number
        _SRLatch_Nand_PMOSB_ChannelWidth=750,  # Number
        _SRLatch_Nand_PMOSB_ChannelLength=30,  # Number

                                  ):

        ## Class_HEADER: Pre Defined Parameter Before Calculation
            ## Load DRC library
        _DRCobj = DRC.DRC()
            ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ## CALCULATION START
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

        #####################################################################################################################################
        ######
        ## NAND wt input 'S' SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_PMOS_power_v2._PMOS_POWER._ParametersForDesignCalculation)
        _Calculation_Parameters = copy.deepcopy(E02_02_Nand_KJH0._Nand._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_PMOSPOWER_PbodyContact_1_Length']  = _PMOSPOWER_PbodyContact_1_Length
        _Calculation_Parameters['_XVT']                 = _SRLatch_XVT

        _Calculation_Parameters['_NMOSA_NumberofGate']  = _SRLatch_Nand_NMOSA_NumberofGate
        _Calculation_Parameters['_NMOSA_ChannelWidth']  = _SRLatch_Nand_NMOSA_ChannelWidth
        _Calculation_Parameters['_NMOSA_ChannelLength'] = _SRLatch_Nand_NMOSA_ChannelLength

        _Calculation_Parameters['_NMOSB_NumberofGate']  = _SRLatch_Nand_NMOSB_NumberofGate
        _Calculation_Parameters['_NMOSB_ChannelWidth']  = _SRLatch_Nand_NMOSB_ChannelWidth
        _Calculation_Parameters['_NMOSB_ChannelLength'] = _SRLatch_Nand_NMOSB_ChannelLength

        _Calculation_Parameters['_PMOSA_NumberofGate']  = _SRLatch_Nand_PMOSA_NumberofGate
        _Calculation_Parameters['_PMOSA_ChannelWidth']  = _SRLatch_Nand_PMOSA_ChannelWidth
        _Calculation_Parameters['_PMOSA_ChannelLength'] = _SRLatch_Nand_PMOSA_ChannelLength

        _Calculation_Parameters['_PMOSB_NumberofGate']  = _SRLatch_Nand_PMOSB_NumberofGate
        _Calculation_Parameters['_PMOSB_ChannelWidth']  = _SRLatch_Nand_PMOSB_ChannelWidth
        _Calculation_Parameters['_PMOSB_ChannelLength'] = _SRLatch_Nand_PMOSB_ChannelLength

        _Calculation_Parameters['_NMOSAB_Pbody_XvtTop2Pbody']   = _SRLatch_NMOSAB_Pbody_XvtTop2Pbody
        _Calculation_Parameters['_PMOSAB_Nbody_Xvtdown2Nbody']  = _SRLatch_PMOSAB_Nbody_Xvtdown2Nbody

        _Calculation_Parameters['_PMOSXvt2NMOSXvt']             = _SRLatch_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_NANDS'] = self._SrefElementDeclaration(_DesignObj=E02_02_Nand_KJH0._Nand(_DesignParameter=None,_Name='{}:SRF_NANDS'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_NANDS']['_Reflect'] = [1, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NANDS']['_Angle'] = 180

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NANDS']['_DesignObj']._CalculateDesignParameter(**_Calculation_Parameters)

        ## initialize Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NANDS']['_XYCoordinates'] = [[0, 0]]

        #####################################################################################################################################
        ######
        ## NAND wt input 'R' SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_PMOS_power_v2._PMOS_POWER._ParametersForDesignCalculation)
        _Calculation_Parameters = copy.deepcopy(E02_02_Nand_KJH0._Nand._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_PMOSPOWER_PbodyContact_1_Length']  = _PMOSPOWER_PbodyContact_1_Length
        _Calculation_Parameters['_XVT']                 = _SRLatch_XVT

        _Calculation_Parameters['_NMOSA_NumberofGate']  = _SRLatch_Nand_NMOSA_NumberofGate
        _Calculation_Parameters['_NMOSA_ChannelWidth']  = _SRLatch_Nand_NMOSA_ChannelWidth
        _Calculation_Parameters['_NMOSA_ChannelLength'] = _SRLatch_Nand_NMOSA_ChannelLength

        _Calculation_Parameters['_NMOSB_NumberofGate']  = _SRLatch_Nand_NMOSB_NumberofGate
        _Calculation_Parameters['_NMOSB_ChannelWidth']  = _SRLatch_Nand_NMOSB_ChannelWidth
        _Calculation_Parameters['_NMOSB_ChannelLength'] = _SRLatch_Nand_NMOSB_ChannelLength

        _Calculation_Parameters['_PMOSA_NumberofGate']  = _SRLatch_Nand_PMOSA_NumberofGate
        _Calculation_Parameters['_PMOSA_ChannelWidth']  = _SRLatch_Nand_PMOSA_ChannelWidth
        _Calculation_Parameters['_PMOSA_ChannelLength'] = _SRLatch_Nand_PMOSA_ChannelLength

        _Calculation_Parameters['_PMOSB_NumberofGate']  = _SRLatch_Nand_PMOSB_NumberofGate
        _Calculation_Parameters['_PMOSB_ChannelWidth']  = _SRLatch_Nand_PMOSB_ChannelWidth
        _Calculation_Parameters['_PMOSB_ChannelLength'] = _SRLatch_Nand_PMOSB_ChannelLength

        _Calculation_Parameters['_NMOSAB_Pbody_XvtTop2Pbody']   = _SRLatch_NMOSAB_Pbody_XvtTop2Pbody
        _Calculation_Parameters['_PMOSAB_Nbody_Xvtdown2Nbody']  = _SRLatch_PMOSAB_Nbody_Xvtdown2Nbody

        _Calculation_Parameters['_PMOSXvt2NMOSXvt']             = _SRLatch_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_NANDR'] = self._SrefElementDeclaration(_DesignObj=E02_02_Nand_KJH0._Nand(_DesignParameter=None,_Name='{}:SRF_NANDR'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_NANDR']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NANDR']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NANDR']['_DesignObj']._CalculateDesignParameter(**_Calculation_Parameters)

        ## initialize Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NANDR']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1_1 = self.get_outter_KJH4('SRF_NANDS')
        target_coordx = tmp1_1['_Mostright']['coord'][0]
        tmp1_2 = self.get_param_KJH4('SRF_NANDS', 'SRF_Pullup', 'SRF_PMOSB', 'BND_PODummyLayer')
        target_coordy = tmp1_2[0][0][0][-1][0]['_XY_down'][1]
        target_coord = [target_coordx, target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2_1 = self.get_outter_KJH4('SRF_NANDR')
        approaching_coordx = tmp2_1['_Mostleft']['coord'][0]
        tmp2_2 = self.get_param_KJH4('SRF_NANDR', 'SRF_Pullup', 'SRF_PMOSA', 'BND_PODummyLayer')
        approaching_coordy = tmp2_2[0][0][0][0][0]['_XY_down'][1]
        approaching_coord = [approaching_coordx, approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_NANDR')
        Scoord = tmp3[0][0]['_XY_origin']

        SpaceBtwNANDSnRPOdummy = 120
        Scoord[0] = Scoord[0] + max(SpaceBtwNANDSnRPOdummy, _DRCobj._PolygateMinSpace)
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['SRF_NANDR']['_XYCoordinates'] = tmpXY

        #####################################################################################################################################
        # pre-defined routing point(coordY)
        tmpSy1 = self.get_param_KJH4('SRF_NANDS', 'SRF_Pullup', 'SRF_PMOSA', 'SRF_Gate_ViaM0Mx','SRF_ViaM0M1', 'BND_Met1Layer')
        tmpSy2 = self.get_param_KJH4('SRF_NANDS', 'SRF_Pulldown', 'SRF_NMOSA','SRF_Gate_ViaM0Mx','SRF_ViaM0M1', 'BND_Met1Layer')
        tmpRy1 = self.get_param_KJH4('SRF_NANDR', 'SRF_Pullup', 'SRF_PMOSA','SRF_Gate_ViaM0Mx','SRF_ViaM0M1', 'BND_Met1Layer')
        tmpRy2 = self.get_param_KJH4('SRF_NANDR', 'SRF_Pulldown', 'SRF_NMOSA','SRF_Gate_ViaM0Mx','SRF_ViaM0M1', 'BND_Met1Layer')
        upperroutepnty = min(int(tmpSy1[0][0][0][0][0][0][0]['_XY_down'][1]*0.666 + tmpSy2[0][0][0][0][0][0][0]['_XY_up'][1]*0.333),\
                             int(tmpSy1[0][0][0][0][0][0][0]['_XY_down'][1]*0.666 + tmpSy2[0][0][0][0][0][0][0]['_XY_up'][1]*0.333))
        lowerroutepnty = max(int(tmpRy1[0][0][0][0][0][0][0]['_XY_down'][1]*0.333 + tmpRy2[0][0][0][0][0][0][0]['_XY_up'][1]*0.666), \
                             int(tmpRy1[0][0][0][0][0][0][0]['_XY_down'][1]*0.333 + tmpRy2[0][0][0][0][0][0][0]['_XY_up'][1]*0.666))

        #####################################################################################################################################
        ###### NAND S gate <-> R drain Routing
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_SGateRDrain_ViaM1M2'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_SGateRDrain_ViaM1M2'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_SGateRDrain_ViaM1M2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_SGateRDrain_ViaM1M2']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_SGateRDrain_ViaM1M2']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_SGateRDrain_ViaM1M2']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmpx = self.get_param_KJH4('SRF_NANDS', 'BND_InputB_Vtc_M1')
        target_coord = [tmpx[0][0][0]['_XY_left'][0], upperroutepnty]
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_SGateRDrain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_SGateRDrain_ViaM1M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_SGateRDrain_ViaM1M2']['_XYCoordinates'] = tmpXY

        #####################################################################################################################################
        ####### NAND S gate <-> R drain Routing/ M2 Metal Bnd element gen.
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_SGateRDrain_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_SGateRDrain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        self._DesignParameter['BND_SGateRDrain_M2']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp2_1 = self.get_param_KJH4('SRF_SGateRDrain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        tmp2_2 = self.get_param_KJH4('SRF_NANDR', 'BND_Out_Vtc_M2')
        self._DesignParameter['BND_SGateRDrain_M2']['_XWidth'] = abs(tmp2_1[0][0][0][0]['_XY_left'][0] - tmp2_2[0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_SGateRDrain_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_SGateRDrain_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_SGateRDrain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        target_coord = [tmp1[0][0][0][0]['_XY_left'][0], upperroutepnty]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_SGateRDrain_M2')
        approaching_coord = tmp2[0][0]['_XY_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_SGateRDrain_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_SGateRDrain_M2']['_XYCoordinates'] = tmpXY

        #####################################################################################################################################
        ###### NAND R gate <-> S drain Routing
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_RGateSDrain_ViaM1M2'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_RGateSDrain_ViaM1M2'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_RGateSDrain_ViaM1M2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_RGateSDrain_ViaM1M2']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_RGateSDrain_ViaM1M2']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_RGateSDrain_ViaM1M2']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmpx = self.get_param_KJH4('SRF_NANDR', 'BND_InputB_Vtc_M1')
        target_coord = [tmpx[0][0][0]['_XY_left'][0], lowerroutepnty]
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_RGateSDrain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_RGateSDrain_ViaM1M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_RGateSDrain_ViaM1M2']['_XYCoordinates'] = tmpXY

        #####################################################################################################################################
        ####### NAND S gate <-> R drain Routing/ M2 Metal Bnd element gen.
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_RGateSDrain_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_RGateSDrain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        self._DesignParameter['BND_RGateSDrain_M2']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp2_1 = self.get_param_KJH4('SRF_RGateSDrain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        tmp2_2 = self.get_param_KJH4('SRF_NANDS', 'BND_Out_Vtc_M2')
        self._DesignParameter['BND_RGateSDrain_M2']['_XWidth'] = abs(tmp2_1[0][0][0][0]['_XY_right'][0] - tmp2_2[0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_RGateSDrain_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_RGateSDrain_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_RGateSDrain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        target_coord = [tmp1[0][0][0][0]['_XY_right'][0], lowerroutepnty]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_RGateSDrain_M2')
        approaching_coord = tmp2[0][0]['_XY_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_RGateSDrain_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_RGateSDrain_M2']['_XYCoordinates'] = tmpXY

        #####################################################################################################################################
        ##### Input S <-> NAND S Routing
        ## Sref generation: Input S ViaM1M3
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_InputS_ViaM1M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,_Name='{}:SRF_InputS_ViaM1M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_InputS_ViaM1M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_InputS_ViaM1M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_InputS_ViaM1M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_InputS_ViaM1M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmpx = self.get_param_KJH4('SRF_NANDS', 'BND_InputA_Vtc_M1')
        target_coord = [tmpx[0][0][0]['_XY_left'][0], lowerroutepnty-100]
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_InputS_ViaM1M3', 'SRF_ViaM1M2', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_InputS_ViaM1M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_InputS_ViaM1M3']['_XYCoordinates'] = tmpXY

        ##################################################################################################################################### no use
        ########## Input S <-> NAND S routing boundary element gen.
           ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_InputS_Hrz_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        InputS_Hrz_M3_pathwidth = 50
        self._DesignParameter['BND_InputS_Hrz_M3']['_YWidth'] = InputS_Hrz_M3_pathwidth

                ## Define Boundary_element _XWidth
        tmp2_1 = self.get_param_KJH4('SRF_InputS_ViaM1M3', 'SRF_ViaM1M2', 'BND_Met1Layer')
        self._DesignParameter['BND_InputS_Hrz_M3']['_XWidth'] = abs(tmp2_1[0][0][0][0]['_Xwidth'])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_InputS_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_InputS_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmpx = self.get_param_KJH4('SRF_InputS_ViaM1M3', 'SRF_ViaM1M2', 'BND_Met1Layer')
        target_coord = tmpx[0][0][0][0]['_XY_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_InputS_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_InputS_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_InputS_Hrz_M3']['_XYCoordinates'] = tmpXY

        #####################################################################################################################################
        ##### Input R <-> NAND R Routing
        ## Sref generation: Input R ViaM1M3
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_InputR_ViaM1M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,_Name='{}:SRF_InputR_ViaM1M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_InputR_ViaM1M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_InputR_ViaM1M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_InputR_ViaM1M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_InputR_ViaM1M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmpx = self.get_param_KJH4('SRF_NANDR', 'BND_InputA_Vtc_M1')
        target_coord = [tmpx[0][0][0]['_XY_left'][0], upperroutepnty+100]
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_InputR_ViaM1M3', 'SRF_ViaM1M2', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_InputR_ViaM1M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_InputR_ViaM1M3']['_XYCoordinates'] = tmpXY

        #####################################################################################################################################
        ########## Input R <-> NAND R routing boundary element gen.
           ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_InputR_Hrz_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        InputR_Hrz_M3_pathwidth = 50
        self._DesignParameter['BND_InputR_Hrz_M3']['_YWidth'] = InputR_Hrz_M3_pathwidth

                ## Define Boundary_element _XWidth
        tmp2_1 = self.get_param_KJH4('SRF_InputR_ViaM1M3', 'SRF_ViaM1M2', 'BND_Met1Layer')
        self._DesignParameter['BND_InputR_Hrz_M3']['_XWidth'] = abs(tmp2_1[0][0][0][0]['_Xwidth'])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_InputR_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_InputR_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmpx = self.get_param_KJH4('SRF_InputR_ViaM1M3', 'SRF_ViaM1M2', 'BND_Met1Layer')
        target_coord = tmpx[0][0][0][0]['_XY_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_InputR_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_InputR_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_InputR_Hrz_M3']['_XYCoordinates'] = tmpXY

        #####################################################################################################################################
        ##### OUTPUT Q <-> NAND S Routing
        ## Sref generation: Output S ViaM2M3
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_OutputQ_ViaM2M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_OutputQ_ViaM2M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_OutputQ_ViaM2M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_OutputQ_ViaM2M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_OutputQ_ViaM2M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_OutputQ_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp = self.get_param_KJH4('SRF_NANDS', 'SRF_Pullup', 'BND_PMOSABDrain_Hrz_M2')
        target_coord = tmp[0][0][0][0]['_XY_left']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_OutputQ_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_OutputQ_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_OutputQ_ViaM2M3']['_XYCoordinates'] = tmpXY

        #####################################################################################################################################
        ##### OUTPUT QB <-> NAND R Routing
        ## Sref generation: Output S ViaM2M3
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_OutputQB_ViaM2M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,_Name='{}:SRF_OutputQB_ViaM2M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_OutputQB_ViaM2M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_OutputQB_ViaM2M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_OutputQB_ViaM2M3']['_DesignObj']._CalculateDesignParameterYmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_OutputQB_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp = self.get_param_KJH4('SRF_NANDR', 'SRF_Pulldown','SRF_NMOSA', 'BND_Drain_Hrz_M2')
        target_coord = tmp[0][0][0][0][0]['_XY_left']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_OutputQB_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_OutputQB_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_OutputQB_ViaM2M3']['_XYCoordinates'] = tmpXY

        #####################################################################################################################################
        ##### NWell BND Element Declaration
          ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NWell_SRLatch'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['NWELL'][0],
        _Datatype=DesignParameters._LayerMapping['NWELL'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_NANDS', 'BND_PMOSAB_NellExten')
        self._DesignParameter['BND_NWell_SRLatch']['_YWidth'] = tmp1[0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH4('SRF_NANDR', 'BND_PMOSAB_NellExten')
        self._DesignParameter['BND_NWell_SRLatch']['_XWidth'] = abs(tmp1[0][0][0]['_XY_right'][0] - tmp2[0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NWell_SRLatch']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_NWell_SRLatch']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp2[0][0][0]['_XY_up_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NWell_SRLatch')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NWell_SRLatch')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_NWell_SRLatch']['_XYCoordinates'] = tmpXY

        #####################################################################################################################################
        ##### PMOS XVT BND Element Declaration
        # if  (_SRLatch_XVT == _SRLatch_XVT and _SRLatch_XVT == _SRLatch_XVT and _SRLatch_XVT== _SRLatch_XVT) != 1:
        #     raise Exception(f"PMOS XVT Layers are not same")
          ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_{}_PMOS_SRLatch'.format(_SRLatch_XVT)] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping[_SRLatch_XVT][0],
        _Datatype=DesignParameters._LayerMapping[_SRLatch_XVT][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp2_1 = self.get_param_KJH4('SRF_NANDS', 'SRF_Pullup', 'SRF_PMOSB','BND_{}Layer'.format(_SRLatch_XVT))
        self._DesignParameter['BND_{}_PMOS_SRLatch'.format(_SRLatch_XVT)]['_YWidth'] = tmp2_1[0][0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp2_2 = self.get_param_KJH4('SRF_NANDR', 'SRF_Pullup', 'SRF_PMOSB','BND_{}Layer'.format(_SRLatch_XVT))
        self._DesignParameter['BND_{}_PMOS_SRLatch'.format(_SRLatch_XVT)]['_XWidth'] = \
            abs(tmp2_1[0][0][0][0][0]['_XY_right'][0] - tmp2_2[0][0][0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_{}_PMOS_SRLatch'.format(_SRLatch_XVT)]['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_{}_PMOS_SRLatch'.format(_SRLatch_XVT)]['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp2_2[0][0][0][0][0]['_XY_up_right']
                            ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_{}_PMOS_SRLatch'.format(_SRLatch_XVT))
        approaching_coord = tmp3[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_{}_PMOS_SRLatch'.format(_SRLatch_XVT))
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_{}_PMOS_SRLatch'.format(_SRLatch_XVT)]['_XYCoordinates'] = tmpXY

        #####################################################################################################################################
        # ##### NMOS XVT BND Element Declaration
        # if  (_NANDS_NMOSA_XVT == _NANDS_NMOSB_XVT and _NANDR_NMOSA_XVT == _NANDR_NMOSA_XVT and _NANDS_NMOSA_XVT== _NANDR_NMOSA_XVT) != 1:
        #     raise Exception(f"NMOS XVT Layers are not same")
          ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_{}_NMOS_SRLatch'.format(_SRLatch_XVT)] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping[_SRLatch_XVT][0],
        _Datatype=DesignParameters._LayerMapping[_SRLatch_XVT][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp2_1 = self.get_param_KJH4('SRF_NANDS', 'SRF_Pulldown', 'SRF_NMOSB','BND_{}Layer'.format(_SRLatch_XVT))
        self._DesignParameter['BND_{}_NMOS_SRLatch'.format(_SRLatch_XVT)]['_YWidth'] = tmp2_1[0][0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp2_2 = self.get_param_KJH4('SRF_NANDR', 'SRF_Pulldown', 'SRF_NMOSB','BND_{}Layer'.format(_SRLatch_XVT))
        self._DesignParameter['BND_{}_NMOS_SRLatch'.format(_SRLatch_XVT)]['_XWidth'] = \
            abs(tmp2_1[0][0][0][0][0]['_XY_right'][0] - tmp2_2[0][0][0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_{}_NMOS_SRLatch'.format(_SRLatch_XVT)]['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_{}_NMOS_SRLatch'.format(_SRLatch_XVT)]['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp2_2[0][0][0][0][0]['_XY_up_right']
                            ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_{}_NMOS_SRLatch'.format(_SRLatch_XVT))
        approaching_coord = tmp3[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_{}_NMOS_SRLatch'.format(_SRLatch_XVT))
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_{}_NMOS_SRLatch'.format(_SRLatch_XVT)]['_XYCoordinates'] = tmpXY

        #####################################################################################################################################
        ##### PMOS BP BND Element Declaration
          ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PPLayer_PMOS_SRLatch'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['PIMP'][0],
        _Datatype=DesignParameters._LayerMapping['PIMP'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp2_1 = self.get_param_KJH4('SRF_NANDS', 'SRF_Pullup', 'SRF_PMOSB','BND_PPLayer')
        self._DesignParameter['BND_PPLayer_PMOS_SRLatch']['_YWidth'] = tmp2_1[0][0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp2_2 = self.get_param_KJH4('SRF_NANDR', 'SRF_Pullup', 'SRF_PMOSB','BND_PPLayer')
        self._DesignParameter['BND_PPLayer_PMOS_SRLatch']['_XWidth'] = abs(tmp2_2[0][0][0][0][0]['_XY_right'][0] - tmp2_1[0][0][0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PPLayer_PMOS_SRLatch']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_PPLayer_PMOS_SRLatch']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp2_2[0][0][0][0][0]['_XY_up_right']
                            ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_PPLayer_PMOS_SRLatch')
        approaching_coord = tmp3[0][0]['_XY_up_right']
                            ## Sref coord
        tmp4 = self.get_param_KJH4('BND_PPLayer_PMOS_SRLatch')
        Scoord = tmp4[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_PPLayer_PMOS_SRLatch']['_XYCoordinates'] = tmpXY

        #####################################################################################################################################
        ##### NMOS Pbody BP Extension BND Element Declaration
          ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PPLayer_NMOS_PBody_SRLatch'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['PIMP'][0],
        _Datatype=DesignParameters._LayerMapping['PIMP'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp2_1 = self.get_param_KJH4('SRF_NANDS', 'SRF_Pbody','SRF_PbodyContactPhyLen','BND_PPLayer')
        self._DesignParameter['BND_PPLayer_NMOS_PBody_SRLatch']['_YWidth'] = tmp2_1[0][0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp2_2 = self.get_param_KJH4('SRF_NANDR', 'SRF_Pbody','SRF_PbodyContactPhyLen','BND_PPLayer')
        self._DesignParameter['BND_PPLayer_NMOS_PBody_SRLatch']['_XWidth'] = abs(tmp2_2[0][0][0][0][0]['_XY_right'][0] - tmp2_1[0][0][0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PPLayer_NMOS_PBody_SRLatch']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_PPLayer_NMOS_PBody_SRLatch']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp2_2[0][0][0][0][0]['_XY_up_right']
                            ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_PPLayer_NMOS_PBody_SRLatch')
        approaching_coord = tmp3[0][0]['_XY_up_right']
                            ## Sref coord
        tmp4 = self.get_param_KJH4('BND_PPLayer_NMOS_PBody_SRLatch')
        Scoord = tmp4[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_PPLayer_NMOS_PBody_SRLatch']['_XYCoordinates'] = tmpXY

        #####################################################################################################################################
        ##### Pbody M1 Extension BND Element Declaration
          ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_M1_NMOS_PBody_SRLatch'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp2_1 = self.get_param_KJH4('SRF_NANDS', 'SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_M1_NMOS_PBody_SRLatch']['_YWidth'] = tmp2_1[0][0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp2_2 = self.get_param_KJH4('SRF_NANDR', 'SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_M1_NMOS_PBody_SRLatch']['_XWidth'] = abs(tmp2_2[0][0][0][0][0]['_XY_right'][0] - tmp2_1[0][0][0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_M1_NMOS_PBody_SRLatch']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_M1_NMOS_PBody_SRLatch']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp2_2[0][0][0][0][0]['_XY_up_right']
                            ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_M1_NMOS_PBody_SRLatch')
        approaching_coord = tmp3[0][0]['_XY_up_right']
                            ## Sref coord
        tmp4 = self.get_param_KJH4('BND_M1_NMOS_PBody_SRLatch')
        Scoord = tmp4[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_M1_NMOS_PBody_SRLatch']['_XYCoordinates'] = tmpXY

        #####################################################################################################################################
        ##### Nbody M1 Extension BND Element Declaration
          ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_M1_PMOS_NBody_SRLatch'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp2_1 = self.get_param_KJH4('SRF_NANDS', 'SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_M1_PMOS_NBody_SRLatch']['_YWidth'] = tmp2_1[0][0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp2_2 = self.get_param_KJH4('SRF_NANDR', 'SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_M1_PMOS_NBody_SRLatch']['_XWidth'] = abs(tmp2_2[0][0][0][0][0]['_XY_right'][0] - tmp2_1[0][0][0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_M1_PMOS_NBody_SRLatch']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_M1_PMOS_NBody_SRLatch']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp2_2[0][0][0][0][0]['_XY_up_right']
                            ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_M1_PMOS_NBody_SRLatch')
        approaching_coord = tmp3[0][0]['_XY_up_right']
                            ## Sref coord
        tmp4 = self.get_param_KJH4('BND_M1_PMOS_NBody_SRLatch')
        Scoord = tmp4[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_M1_PMOS_NBody_SRLatch']['_XYCoordinates'] = tmpXY

        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')
        #####################################################################################################################################

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    Start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ZZ01_E01_04_SRLatch_Fixed'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'E01_01_SRLatch_v0'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
## SRLatch
    ## Common
        # XVT
        _SRLatch_XVT='SLVT',
        # Body
        _SRLatch_NMOSAB_Pbody_XvtTop2Pbody=None,  # Number/None(Minimum)
        _SRLatch_PMOSAB_Nbody_Xvtdown2Nbody=None,  # Number/None(Minimum)
        # Height
        _SRLatch_PMOSXvt2NMOSXvt=1150,  # number
    ## Nand(Set,Rst same)
        # NmosA
        _SRLatch_Nand_NMOSA_NumberofGate=1,  # Number
        _SRLatch_Nand_NMOSA_ChannelWidth=100,  # Number
        _SRLatch_Nand_NMOSA_ChannelLength=30,  # Number
        # NMOSB
        _SRLatch_Nand_NMOSB_NumberofGate=2,  # Number
        _SRLatch_Nand_NMOSB_ChannelWidth=750,  # Number
        _SRLatch_Nand_NMOSB_ChannelLength=30,  # Number
        # PMOSA
        _SRLatch_Nand_PMOSA_NumberofGate=2,  # Number
        _SRLatch_Nand_PMOSA_ChannelWidth=100,  # Number
        _SRLatch_Nand_PMOSA_ChannelLength=30,  # Number
        # PMOSB
        _SRLatch_Nand_PMOSB_NumberofGate=1,  # Number
        _SRLatch_Nand_PMOSB_ChannelWidth=750,  # Number
        _SRLatch_Nand_PMOSB_ChannelLength=30,  # Number

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
    LayoutObj = _SRLatch(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    ''' Check Time'''
    elapsed_time = time.time() - Start_time
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
