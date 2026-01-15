
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
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A10_PbodyRing_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A09_NbodyRing_KJH3

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.C07_Tr12Tr3Tr10_Fixed import C07_03_Tr12Tr3Tr10_v2


## Define Class
class _Guardring(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
# TR12
    # Physical dimension
    _Tr12_NumberofGate	            = 4,       # Number
    _Tr12_ChannelWidth	            = 1500,     # Number
    _Tr12_ChannelLength	            = 30,       # Number
    _Tr12_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
# TR3
    # Physical dimension
    _Tr3_NumberofGate	            = 2,       # Number
    _Tr3_ChannelWidth	            = 100,     # Number
    _Tr3_ChannelLength	            = 30,       # Number
    _Tr3_XVT				        = 'LVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
# TR10
    # Physical dimension
    _Tr10_NumberofGate	            = 8,       # Number
    _Tr10_ChannelWidth	            = 780,     # Number
    _Tr10_ChannelLength	            = 30,       # Number
    _Tr10_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

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
# TR12
    # Physical dimension
    _Tr12_NumberofGate	            = 4,       # Number
    _Tr12_ChannelWidth	            = 1500,     # Number
    _Tr12_ChannelLength	            = 30,       # Number
    _Tr12_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
# TR3
    # Physical dimension
    _Tr3_NumberofGate	            = 2,       # Number
    _Tr3_ChannelWidth	            = 100,     # Number
    _Tr3_ChannelLength	            = 30,       # Number
    _Tr3_XVT				        = 'LVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
# TR10
    # Physical dimension
    _Tr10_NumberofGate	            = 8,       # Number
    _Tr10_ChannelWidth	            = 780,     # Number
    _Tr10_ChannelLength	            = 30,       # Number
    _Tr10_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
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


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr12Tr3Tr10
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C07_03_Tr12Tr3Tr10_v2._Tr12Tr3Tr10._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr12_NumberofGate']     =   _Tr12_NumberofGate
        _Caculation_Parameters['_Tr12_ChannelWidth']     =   _Tr12_ChannelWidth
        _Caculation_Parameters['_Tr12_ChannelLength']    =   _Tr12_ChannelLength
        _Caculation_Parameters['_Tr12_XVT']              =   _Tr12_XVT

        _Caculation_Parameters['_Tr3_NumberofGate']     =   _Tr3_NumberofGate
        _Caculation_Parameters['_Tr3_ChannelWidth']     =   _Tr3_ChannelWidth
        _Caculation_Parameters['_Tr3_ChannelLength']    =   _Tr3_ChannelLength
        _Caculation_Parameters['_Tr3_XVT']              =   _Tr3_XVT

        _Caculation_Parameters['_Tr10_NumberofGate']     =   _Tr10_NumberofGate
        _Caculation_Parameters['_Tr10_ChannelWidth']     =   _Tr10_ChannelWidth
        _Caculation_Parameters['_Tr10_ChannelLength']    =   _Tr10_ChannelLength
        _Caculation_Parameters['_Tr10_XVT']              =   _Tr10_XVT

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Tr12Tr3Tr10'] = self._SrefElementDeclaration(_DesignObj=C07_03_Tr12Tr3Tr10_v2._Tr12Tr3Tr10(_DesignParameter=None, _Name='{}:SRF_Tr12Tr3Tr10'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Tr12Tr3Tr10']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr12Tr3Tr10']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr12Tr3Tr10']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr12Tr3Tr10']['_XYCoordinates'] = [[0, 0]]


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Guardring
        _Tr12Tr3Tr10_Guardring_NumCont =3

        ## Guardring
            ## Pre-defined
        _right_margin   = 300
        _left_margin = 300
        _up_margin = 150
        _down_margin = 150

            ## Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A10_PbodyRing_KJH3._PbodyRing._ParametersForDesignCalculation)
        _Caculation_Parameters['_XlengthIntn']      = None
        _Caculation_Parameters['_YlengthIntn']      = None
        _Caculation_Parameters['_NumContTop']       = _Tr12Tr3Tr10_Guardring_NumCont
        _Caculation_Parameters['_NumContBottom']    = _Tr12Tr3Tr10_Guardring_NumCont
        _Caculation_Parameters['_NumContLeft']      = _Tr12Tr3Tr10_Guardring_NumCont
        _Caculation_Parameters['_NumContRight']     = _Tr12Tr3Tr10_Guardring_NumCont
        #_Caculation_Parameters['_NwellWidth']       = _NwellWidth ## used only for DeepNwell

            ## Find Outter boundary
        tmp = self.get_outter_KJH4('SRF_Tr12Tr3Tr10')

            ## Define _XlengthIntn
        _Caculation_Parameters['_XlengthIntn'] = abs(tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0]) + _right_margin + _left_margin # option: + _NwellWidth

            ## Define _YlengthIntn
        _Caculation_Parameters['_YlengthIntn'] = abs(tmp['_Mostup']['coord'][0] - tmp['_Mostdown']['coord'][0]) + _up_margin + _down_margin # option + _NwellWidth

            ## Generate Sref
        self._DesignParameter['SRF_Pbodyring'] = self._SrefElementDeclaration(_DesignObj=A10_PbodyRing_KJH3._PbodyRing(_DesignParameter=None, _Name='{}:_Pbodyring'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Pbodyring']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Pbodyring']['_Angle'] = 0

            ## Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_Pbodyring']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            ## Define Sref _XYcoordinate
        self._DesignParameter['SRF_Pbodyring']['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Pbodyring']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        target_coord = [tmp['_Mostleft']['coord'][0], tmp['_Mostdown']['coord'][0]]
                    ## Approaching_coord
                        ## x
        tmp2_1 = self.get_param_KJH4('SRF_Pbodyring', 'SRF_PbodyLeft', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coordx = tmp2_1[0][0][0][0][0]['_XY_right'][0]
                        ## y
        tmp2_2 = self.get_param_KJH4('SRF_Pbodyring', 'SRF_PbodyBottom', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coordy = tmp2_2[0][0][0][0][0]['_XY_up'][1]

        approaching_coord = [approaching_coordx, approaching_coordy]
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pbodyring')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] - _left_margin # option: - _NwellWidth
        New_Scoord[1] = New_Scoord[1] - _down_margin # option: - _NwellWidth
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Pbodyring']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr12Tr3Tr10 Drain and Pbody connection
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr12Tr3Tr10 Drain and Pbody connection: M2
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Tr12Tr3Tr10_Drain_Hrz_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('SRF_Tr12Tr3Tr10','SRF_Tr12','BND_Drain_Hrz_M2')
        self._DesignParameter['BND_Tr12Tr3Tr10_Drain_Hrz_M2']['_YWidth'] = tmp[0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Pbodyring','SRF_PbodyLeft','SRF_PbodyContactPhyLen','BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_Pbodyring','SRF_PbodyRight','SRF_PbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_Tr12Tr3Tr10_Drain_Hrz_M2']['_XWidth'] = abs (tmp2[0][0][0][0][0]['_XY_left'][0] - tmp1[0][0][0][0][0]['_XY_right'][0] )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Tr12Tr3Tr10_Drain_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Tr12Tr3Tr10_Drain_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ## x
        tmp1_1 =self.get_param_KJH4('SRF_Pbodyring','SRF_PbodyLeft','SRF_PbodyContactPhyLen','BND_Met1Layer')
        target_coordx = tmp1_1[0][0][0][0][0]['_XY_right'][0]
                                ## y
        tmp1_2 =self.get_param_KJH4('SRF_Tr12Tr3Tr10','SRF_Tr12','BND_Drain_Hrz_M2')
        target_coordy = tmp1_2[0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Tr12Tr3Tr10_Drain_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Tr12Tr3Tr10_Drain_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Tr12Tr3Tr10_Drain_Hrz_M2']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr12Tr3Tr10 Drain and Pbody connection: M1
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Tr12Tr3Tr10_Drain_Hrz_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('BND_Tr12Tr3Tr10_Drain_Hrz_M2')
        self._DesignParameter['BND_Tr12Tr3Tr10_Drain_Hrz_M1']['_YWidth'] = tmp[0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('BND_Tr12Tr3Tr10_Drain_Hrz_M2')
        self._DesignParameter['BND_Tr12Tr3Tr10_Drain_Hrz_M1']['_XWidth'] = tmp[0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
        tmp = self.get_param_KJH4('BND_Tr12Tr3Tr10_Drain_Hrz_M2')
        self._DesignParameter['BND_Tr12Tr3Tr10_Drain_Hrz_M1']['_XYCoordinates'] = [tmp[0][0]['_XY_origin']]


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr12Tr3Tr10 Drain and Pbody connection: ViaM1M2
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        ## Sref ViaX declaration
        self._DesignParameter['SRF_Tr12Tr3Tr10_Drain_ViaM1M2'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,_Name='{}:SRF_Tr12Tr3Tr10_Drain_ViaM1M2'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_Tr12Tr3Tr10_Drain_ViaM1M2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_Tr12Tr3Tr10_Drain_ViaM1M2']['_Angle'] = 0

        ## Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH4('BND_Tr12Tr3Tr10_Drain_Hrz_M1')
        tmp2 = self.get_param_KJH4('BND_Tr12Tr3Tr10_Drain_Hrz_M2')
        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

        ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

        ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Tr12Tr3Tr10_Drain_ViaM1M2']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_Tr12Tr3Tr10_Drain_ViaM1M2']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_Tr12Tr3Tr10_Drain_Hrz_M1')
        target_coord = tmp1[0][0]['_XY_cent']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Tr12Tr3Tr10_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Tr12Tr3Tr10_Drain_ViaM1M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_Tr12Tr3Tr10_Drain_ViaM1M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr12Tr3Tr10 Gate connet : M2
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Tr12Tr3Tr10_Gate_Hrz_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('SRF_Tr12Tr3Tr10','SRF_Tr12','BND_Gate_Hrz_Mx')
        self._DesignParameter['BND_Tr12Tr3Tr10_Gate_Hrz_M2']['_YWidth'] = tmp[0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Tr12Tr3Tr10','SRF_Tr12','BND_Gate_Hrz_Mx')
        tmp2 = self.get_param_KJH4('SRF_Tr12Tr3Tr10', 'SRF_Tr10', 'BND_Gate_Hrz_Mx')
        self._DesignParameter['BND_Tr12Tr3Tr10_Gate_Hrz_M2']['_XWidth'] = abs( tmp2[0][0][0][0]['_XY_right'][0] - tmp1[0][0][0][0]['_XY_left'][0] )

                ## Define Boundary_element _XYCoordinates

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Tr12Tr3Tr10_Gate_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('SRF_Tr12Tr3Tr10','SRF_Tr12','BND_Gate_Hrz_Mx')
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Tr12Tr3Tr10_Gate_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Tr12Tr3Tr10_Gate_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['BND_Tr12Tr3Tr10_Gate_Hrz_M2']['_XYCoordinates'] = tmpXY


        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ZZ01_C07_04_Guardring_Fixed'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'C07_04_Guardring_v0_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
# TR12
    # Physical dimension
    _Tr12_NumberofGate	            = 4,       # Number
    _Tr12_ChannelWidth	            = 1500,     # Number
    _Tr12_ChannelLength	            = 30,       # Number
    _Tr12_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
# TR3
    # Physical dimension
    _Tr3_NumberofGate	            = 2,       # Number
    _Tr3_ChannelWidth	            = 100,     # Number
    _Tr3_ChannelLength	            = 30,       # Number
    _Tr3_XVT				        = 'LVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
# TR10
    # Physical dimension
    _Tr10_NumberofGate	            = 8,       # Number
    _Tr10_ChannelWidth	            = 780,     # Number
    _Tr10_ChannelLength	            = 30,       # Number
    _Tr10_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

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
    LayoutObj = _Guardring(_DesignParameter=None, _Name=cellname)
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
    Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()

    print('#############################      Finished      ################################')
    print('{} Hours   {} minutes   {} seconds'.format(h, m, s))
# end of 'main():' ---------------------------------------------------------------------------------------------
