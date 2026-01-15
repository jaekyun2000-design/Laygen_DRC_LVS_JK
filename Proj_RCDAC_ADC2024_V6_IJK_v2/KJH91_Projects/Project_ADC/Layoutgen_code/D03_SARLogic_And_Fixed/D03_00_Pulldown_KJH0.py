
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
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A03_NmosWithDummy_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A04_PmosWithDummy_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A08_PbodyContactPhyLen_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A07_NbodyContactPhyLen_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A14_Mosfet_KJH3



## Define Class
class _Pulldown(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
## Nand(Pulldown,Nmos)
        #Common
    _XVT                         = 'SLVT',
        #Nmos
    _NMOSA_NumberofGate          = 3,        # Number
    _NMOSA_ChannelWidth          = 100,      # Number
    _NMOSA_ChannelLength         = 30,       # Number
        #Pmos
    _NMOSB_NumberofGate          = 5,        # Number
    _NMOSB_ChannelWidth          = 750,      # Number
    _NMOSB_ChannelLength         = 30,       # Number
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
## Nand(Pulldown,Nmos)
        #Common
    _XVT                         = 'SLVT',
        #Nmos
    _NMOSA_NumberofGate          = 3,        # Number
    _NMOSA_ChannelWidth          = 100,      # Number
    _NMOSA_ChannelLength         = 30,       # Number
        #Pmos
    _NMOSB_NumberofGate          = 5,        # Number
    _NMOSB_ChannelWidth          = 750,      # Number
    _NMOSB_ChannelLength         = 30,       # Number
                                  ):

        ## Class_HEADER: Pre Defined Parameter Before Calculation
            ## Load DRC library
        _DRCobj = DRC.DRC()
            ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ## CALCULATION START
        start_time = time.time()
        # end_time = time.time()
        # self.elapsed_time = end_time - start_time
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')
        PolyGateCombineLength = 100

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOSA
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  NMOSA: Sref Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_NMOSA_power_v2._NMOSA_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters1 = copy.deepcopy(A14_Mosfet_KJH3._Mosfet._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters1['_MosType'] = 'NMOS'
        _Caculation_Parameters1['_MosUpDn'] = 'Up'

        _Caculation_Parameters1['_NumberofGate'] = _NMOSA_NumberofGate
        _Caculation_Parameters1['_ChannelWidth'] = _NMOSA_ChannelWidth
        _Caculation_Parameters1['_ChannelLength'] = _NMOSA_ChannelLength
        _Caculation_Parameters1['_GateSpacing'] = None
        _Caculation_Parameters1['_SDWidth'] = None
        _Caculation_Parameters1['_XVT'] = _XVT
        _Caculation_Parameters1['_PCCrit'] = True

        _Caculation_Parameters1['_Source_Via_TF'] = True
        _Caculation_Parameters1['_Source_Via_Close2POpin_TF'] = True
        _Caculation_Parameters1['_Source_Comb_TF'] = True
        _Caculation_Parameters1['_Source_Comb_POpinward_TF'] = False
        _Caculation_Parameters1['_Source_Comb_Length'] = None

        _Caculation_Parameters1['_Drain_Via_TF'] = True
        _Caculation_Parameters1['_Drain_Via_Close2POpin_TF'] = False
        _Caculation_Parameters1['_Drain_Comb_TF'] = True
        _Caculation_Parameters1['_Drain_Comb_POpinward_TF'] = True
        _Caculation_Parameters1['_Drain_Comb_Length'] = None

        _Caculation_Parameters1['_PODummy_TF'] = True
        _Caculation_Parameters1['_PODummy_Length'] = None
        _Caculation_Parameters1['_PODummy_Placement'] = 'Up'

        _Caculation_Parameters1['_Xvt_MinExten_TF'] = True
        _Caculation_Parameters1['_Xvt_Placement'] = 'Dn'

        _Caculation_Parameters1['_POGate_Comb_TF'] = True
        _Caculation_Parameters1['_POGate_Comb_length'] = PolyGateCombineLength
        _Caculation_Parameters1['_POGate_Via_TF'] = True
        _Caculation_Parameters1['_POGate_ViaMxMx'] = [0, 1]

        ## Generate Sref: ex)self._DesignParameter['_NMOSA_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_NMOSA_power_v2._NMOSA_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_NMOSA'] = self._SrefElementDeclaration(_DesignObj=A14_Mosfet_KJH3._Mosfet(_DesignParameter=None, _Name='{}:SRF_NMOSA'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOSA_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_NMOSA']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOSA_POWER'
        self._DesignParameter['SRF_NMOSA']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOSA_POWER'
        self._DesignParameter['SRF_NMOSA']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters1)

        ## Define Sref _XYcoordinate: ex)'_NMOSA_POWER'
        self._DesignParameter['SRF_NMOSA']['_XYCoordinates'] = [[0, 0]]



        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOSB
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  NMOSB: Sref Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_NMOSB_power_v2._NMOSB_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters2 = copy.deepcopy(A14_Mosfet_KJH3._Mosfet._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters2['_MosType'] = 'NMOS'
        _Caculation_Parameters2['_MosUpDn'] = 'Up'

        _Caculation_Parameters2['_NumberofGate'] = _NMOSB_NumberofGate
        _Caculation_Parameters2['_ChannelWidth'] = _NMOSB_ChannelWidth
        _Caculation_Parameters2['_ChannelLength'] = _NMOSB_ChannelLength
        _Caculation_Parameters2['_GateSpacing'] = None
        _Caculation_Parameters2['_SDWidth'] = None
        _Caculation_Parameters2['_XVT'] = _XVT
        _Caculation_Parameters2['_PCCrit'] = True

        _Caculation_Parameters2['_Source_Via_TF'] = False
        _Caculation_Parameters2['_Source_Via_Close2POpin_TF'] = None
        _Caculation_Parameters2['_Source_Comb_TF'] = None
        _Caculation_Parameters2['_Source_Comb_POpinward_TF'] = None
        _Caculation_Parameters2['_Source_Comb_Length'] = None

        _Caculation_Parameters2['_Drain_Via_TF'] = True
        _Caculation_Parameters2['_Drain_Via_Close2POpin_TF'] = True
        _Caculation_Parameters2['_Drain_Comb_TF'] = True
        _Caculation_Parameters2['_Drain_Comb_POpinward_TF'] = False
        _Caculation_Parameters2['_Drain_Comb_Length'] = None

        _Caculation_Parameters2['_PODummy_TF'] = True
        _Caculation_Parameters2['_PODummy_Length'] = None
        _Caculation_Parameters2['_PODummy_Placement'] = 'Up'

        _Caculation_Parameters2['_Xvt_MinExten_TF'] = True
        _Caculation_Parameters2['_Xvt_Placement'] = 'Dn'

        _Caculation_Parameters2['_POGate_Comb_TF'] = True
        _Caculation_Parameters2['_POGate_Comb_length'] = PolyGateCombineLength
        _Caculation_Parameters2['_POGate_Via_TF'] = True
        _Caculation_Parameters2['_POGate_ViaMxMx'] = [0, 1]

        ## Generate Sref: ex)self._DesignParameter['_NMOSB_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_NMOSB_power_v2._NMOSB_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_NMOSB'] = self._SrefElementDeclaration(_DesignObj=A14_Mosfet_KJH3._Mosfet(_DesignParameter=None, _Name='{}:SRF_NMOSB'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOSB_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_NMOSB']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOSB_POWER'
        self._DesignParameter['SRF_NMOSB']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOSB_POWER'
        self._DesignParameter['SRF_NMOSB']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters2)

        ## Define Sref _XYcoordinate: ex)'_NMOSB_POWER'
        self._DesignParameter['SRF_NMOSB']['_XYCoordinates'] = [[0, 0]]

        if _NMOSA_NumberofGate == 1 and _NMOSB_NumberofGate == 1:
                   ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_NMOSB']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
                                    ## x
            tmp1_1 = self.get_param_KJH4('SRF_NMOSA','BND_PODummyLayer')
            target_coordx = tmp1_1[0][-1][0]['_XY_right'][0]
                                    ## y
            tmp1_2 = self.get_param_KJH4('SRF_NMOSA','BND_{}Layer'.format(_XVT))
            target_coordy = tmp1_2[0][0][0]['_XY_up'][1]

            target_coord = [target_coordx,target_coordy]
                                ## Approaching_coord: _XY_type2
                                    ## x
            tmp2_1 = self.get_param_KJH4('SRF_NMOSB','BND_PODummyLayer')
            approaching_coordx = tmp2_1[0][0][0]['_XY_left'][0]
                                    ## y
            tmp2_2 = self.get_param_KJH4('SRF_NMOSB','BND_{}Layer'.format(_XVT))
            approaching_coordy = tmp2_2[0][0][0]['_XY_up'][1]

            approaching_coord = [approaching_coordx,approaching_coordy]
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_NMOSB')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[0] = New_Scoord[0] + 150
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_NMOSB']['_XYCoordinates'] = tmpXY

        else:
                   ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_NMOSB']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
                                    ## x
            tmp1_1 = self.get_param_KJH4('SRF_NMOSA','BND_PODummyLayer')
            target_coordx = tmp1_1[0][-1][0]['_XY_left'][0]
                                    ## y
            tmp1_2 = self.get_param_KJH4('SRF_NMOSA','BND_{}Layer'.format(_XVT))
            target_coordy = tmp1_2[0][0][0]['_XY_up'][1]

            target_coord = [target_coordx,target_coordy]
                                ## Approaching_coord: _XY_type2
                                    ## x
            tmp2_1 = self.get_param_KJH4('SRF_NMOSB','BND_PODummyLayer')
            approaching_coordx = tmp2_1[0][0][0]['_XY_left'][0]
                                    ## y
            tmp2_2 = self.get_param_KJH4('SRF_NMOSB','BND_{}Layer'.format(_XVT))
            approaching_coordy = tmp2_2[0][0][0]['_XY_up'][1]

            approaching_coord = [approaching_coordx,approaching_coordy]
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_NMOSB')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_NMOSB']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Length Cal
        tmp1 = self.get_param_KJH4('SRF_NMOSA','BND_Source_Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_NMOSB','BND_Drain_Hrz_M2')

        tmp3 = self.get_param_KJH4('SRF_NMOSA','BND_Source_Vtc_M2')
        tmp4 = self.get_param_KJH4('SRF_NMOSB','BND_Drain_Vtc_M2')

        if tmp1[0][0][0]['_XY_down'][1] > tmp2[0][0][0]['_XY_down'][1]:
            NMOSA_length = tmp3[0][0][0]['_XY_up'][1] - tmp4[0][0][0]['_XY_down'][1]
            NMOSB_length = None
        else:
            NMOSB_length = tmp4[0][0][0]['_XY_up'][1] - tmp3[0][0][0]['_XY_down'][1]
            NMOSA_length = None

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOSA
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  NMOSA: Sref Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_NMOSA_power_v2._NMOSA_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters1['_Source_Comb_Length'] = NMOSA_length

        ## Generate Sref: ex)self._DesignParameter['_NMOSA_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_NMOSA_power_v2._NMOSA_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_NMOSA'] = self._SrefElementDeclaration(_DesignObj=A14_Mosfet_KJH3._Mosfet(_DesignParameter=None, _Name='{}:SRF_NMOSA'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOSA_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_NMOSA']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOSA_POWER'
        self._DesignParameter['SRF_NMOSA']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOSA_POWER'
        self._DesignParameter['SRF_NMOSA']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters1)

        ## Define Sref _XYcoordinate: ex)'_NMOSA_POWER'
        self._DesignParameter['SRF_NMOSA']['_XYCoordinates'] = [[0, 0]]


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOSB
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  NMOSB: Sref Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_NMOSB_power_v2._NMOSB_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters2['_Drain_Comb_Length'] = NMOSB_length

        ## Generate Sref: ex)self._DesignParameter['_NMOSB_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_NMOSB_power_v2._NMOSB_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_NMOSB'] = self._SrefElementDeclaration(_DesignObj=A14_Mosfet_KJH3._Mosfet(_DesignParameter=None, _Name='{}:SRF_NMOSB'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOSB_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_NMOSB']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOSB_POWER'
        self._DesignParameter['SRF_NMOSB']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOSB_POWER'
        self._DesignParameter['SRF_NMOSB']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters2)

        ## Define Sref _XYcoordinate: ex)'_NMOSB_POWER'
        self._DesignParameter['SRF_NMOSB']['_XYCoordinates'] = [[0, 0]]

        if _NMOSA_NumberofGate == 1 and _NMOSB_NumberofGate == 1:
                   ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_NMOSB']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
                                    ## x
            tmp1_1 = self.get_param_KJH4('SRF_NMOSA','BND_PODummyLayer')
            target_coordx = tmp1_1[0][-1][0]['_XY_right'][0]
                                    ## y
            tmp1_2 = self.get_param_KJH4('SRF_NMOSA','BND_{}Layer'.format(_XVT))
            target_coordy = tmp1_2[0][0][0]['_XY_up'][1]

            target_coord = [target_coordx,target_coordy]
                                ## Approaching_coord: _XY_type2
                                    ## x
            tmp2_1 = self.get_param_KJH4('SRF_NMOSB','BND_PODummyLayer')
            approaching_coordx = tmp2_1[0][0][0]['_XY_left'][0]
                                    ## y
            tmp2_2 = self.get_param_KJH4('SRF_NMOSB','BND_{}Layer'.format(_XVT))
            approaching_coordy = tmp2_2[0][0][0]['_XY_up'][1]

            approaching_coord = [approaching_coordx,approaching_coordy]
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_NMOSB')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[0] = New_Scoord[0] + 150
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_NMOSB']['_XYCoordinates'] = tmpXY

        else:
                   ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_NMOSB']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
                                    ## x
            tmp1_1 = self.get_param_KJH4('SRF_NMOSA','BND_PODummyLayer')
            target_coordx = tmp1_1[0][-1][0]['_XY_left'][0]
                                    ## y
            tmp1_2 = self.get_param_KJH4('SRF_NMOSA','BND_{}Layer'.format(_XVT))
            target_coordy = tmp1_2[0][0][0]['_XY_up'][1]

            target_coord = [target_coordx,target_coordy]
                                ## Approaching_coord: _XY_type2
                                    ## x
            tmp2_1 = self.get_param_KJH4('SRF_NMOSB','BND_PODummyLayer')
            approaching_coordx = tmp2_1[0][0][0]['_XY_left'][0]
                                    ## y
            tmp2_2 = self.get_param_KJH4('SRF_NMOSB','BND_{}Layer'.format(_XVT))
            approaching_coordy = tmp2_2[0][0][0]['_XY_up'][1]

            approaching_coord = [approaching_coordx,approaching_coordy]
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_NMOSB')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_NMOSB']['_XYCoordinates'] = tmpXY



        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOSB NMOSA Drain Connection
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NMOSASource_NMOSBDrain_Hrz_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('SRF_NMOSA','BND_Drain_Hrz_M2')
        self._DesignParameter['BND_NMOSASource_NMOSBDrain_Hrz_M2']['_YWidth'] = tmp[0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_NMOSA','BND_Source_Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_NMOSB','BND_Drain_Hrz_M2')
        self._DesignParameter['BND_NMOSASource_NMOSBDrain_Hrz_M2']['_XWidth'] = abs( tmp2[0][0][0]['_XY_right'][0] - tmp1[0][0][0]['_XY_left'][0] )

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NMOSASource_NMOSBDrain_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
            ## initialized Sref coordinate
        self._DesignParameter['BND_NMOSASource_NMOSBDrain_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
                ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_NMOSB','BND_Drain_Hrz_M2')
        target_coord = tmp1[0][0][0]['_XY_down_right']
                ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NMOSASource_NMOSBDrain_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_down_right']
                ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NMOSASource_NMOSBDrain_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_NMOSASource_NMOSBDrain_Hrz_M2']['_XYCoordinates'] = tmpXY


        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')
        # start_time = time.time()
        end_time = time.time()
        self.elapsed_time = end_time - start_time

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ZZ01_D03_00_Pulldown_Fixed'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'D03_00_Pulldown_v0_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
## Nand(Pulldown,Nmos)
        #Common
    _XVT                         = 'SLVT',
        #Nmos
    _NMOSA_NumberofGate          = 3,        # Number
    _NMOSA_ChannelWidth          = 100,      # Number
    _NMOSA_ChannelLength         = 30,       # Number
        #Pmos
    _NMOSB_NumberofGate          = 5,        # Number
    _NMOSB_ChannelWidth          = 750,      # Number
    _NMOSB_ChannelLength         = 30,       # Number


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
    LayoutObj = _Pulldown(_DesignParameter=None, _Name=cellname)
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
