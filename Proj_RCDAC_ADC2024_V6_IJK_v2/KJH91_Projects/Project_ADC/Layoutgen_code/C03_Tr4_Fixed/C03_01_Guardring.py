
## Import Basic Modules
    ## Engine
from Proj_RCDAC_ADC2024_V6_IJK.KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_ADC.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

    ## Library
import copy
import math
import numpy as np
import time

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A03_NmosWithDummy_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A04_PmosWithDummy_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A05_NbodyContact_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A06_PbodyContact_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A07_NbodyContactPhyLen_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A08_PbodyContactPhyLen_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A09_NbodyRing_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A10_PbodyRing_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A11_NbodyContactforDeepNwell_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A12_NbodyContactPhyLenforDeepNwell_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A13_NbodyRingforDeepNwell_KJH

    ##
from Proj_RCDAC_ADC2024_V6_IJK.KJH91_Projects.Project_ADC.Layoutgen_code.C03_Tr4_Fixed import C03_00_Tr4


## Define Class
class _Guardring(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
#TR4
    # Physical dimension
    _Tr4_NumberofGate	            = 4,       # Number
    _Tr4_ChannelWidth	            = 500,     # Number
    _Tr4_ChannelLength	            = 30,       # Number
    _Tr4_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
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
#TR4
    # Physical dimension
    _Tr4_NumberofGate	            = 4,       # Number
    _Tr4_ChannelWidth	            = 500,     # Number
    _Tr4_ChannelLength	            = 30,       # Number
    _Tr4_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
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


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr4, nfettw
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  M4, nfettw: Sref Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C03_00_Tr4._Tr4._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr4_NumberofGate'] = _Tr4_NumberofGate
        _Caculation_Parameters['_Tr4_ChannelWidth'] = _Tr4_ChannelWidth
        _Caculation_Parameters['_Tr4_ChannelLength'] = _Tr4_ChannelLength
        _Caculation_Parameters['_Tr4_XVT'] = _Tr4_XVT

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Tr4'] = self._SrefElementDeclaration(_DesignObj=C03_00_Tr4._Tr4(_DesignParameter=None, _Name='{}:SRF_Tr4'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Tr4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr4']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr4']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr4']['_XYCoordinates'] = [[0, 0]]


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Guardring: Pbody
        ## Guardring
            ## Pre-defined DRC
        _right_margin   = 150
        _left_margin    = 150
        _up_margin      = 150
        _down_margin    = 150

        _NumCont = 2

            ## Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A10_PbodyRing_KJH3._PbodyRing._ParametersForDesignCalculation)
        _Caculation_Parameters['_XlengthIntn']      = None
        _Caculation_Parameters['_YlengthIntn']      = None
        _Caculation_Parameters['_NumContTop']       = _NumCont
        _Caculation_Parameters['_NumContBottom']    = _NumCont
        _Caculation_Parameters['_NumContLeft']      = _NumCont
        _Caculation_Parameters['_NumContRight']     = _NumCont

            ## Find Outter boundary
        tmp = self.get_outter_KJH4('SRF_Tr4')

            ## Define _XlengthIntn
        _Caculation_Parameters['_XlengthIntn'] = abs(tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0]) + _right_margin + _left_margin

            ## Define _YlengthIntn
        _Caculation_Parameters['_YlengthIntn'] = abs(tmp['_Mostup']['coord'][0] - tmp['_Mostdown']['coord'][0]) + _up_margin + _down_margin

            ## Generate Sref
        self._DesignParameter['SRF_Pbodyring'] = self._SrefElementDeclaration(_DesignObj=A10_PbodyRing_KJH3._PbodyRing(_DesignParameter=None, _Name='{}:SRF_Pbodyring'.format(_Name)))[0]

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
        New_Scoord[0] = New_Scoord[0] - _left_margin
        New_Scoord[1] = New_Scoord[1] - _down_margin
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Pbodyring']['_XYCoordinates'] = tmpXY



        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Guardring: Nbody
        ## Pre-defined
        _right_margin2 = 50
        _left_margin2 = 50
        _up_margin2 = 350
        _down_margin2 = 50
        _NumCont2 = 3
        _NwellWidth = 350

        ## Guardring
        ## Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A13_NbodyRingforDeepNwell_KJH._NbodyRingforDeepNwell_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_XlengthIntn']      = None
        _Caculation_Parameters['_YlengthIntn']      = None
        _Caculation_Parameters['_NumContTop']       = _NumCont2
        _Caculation_Parameters['_NumContBottom']    = _NumCont2
        _Caculation_Parameters['_NumContLeft']      = _NumCont2
        _Caculation_Parameters['_NumContRight']     = _NumCont2
        _Caculation_Parameters['_NwellWidth']       = _NwellWidth

        ## Find Outter boundary
        tmp = self.get_outter_KJH4('SRF_Pbodyring')

        ## Define _XlengthIntn
        _Caculation_Parameters['_XlengthIntn'] = abs(tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0]) + 2 * _NwellWidth + _right_margin2 + _left_margin2

        ## Define _YlengthIntn
        _Caculation_Parameters['_YlengthIntn'] = abs(tmp['_Mostup']['coord'][0] - tmp['_Mostdown']['coord'][0]) + 2 * _NwellWidth + _up_margin2 + _down_margin2

        ## Generate Sref
        self._DesignParameter['SRF_Nbodyring'] = self._SrefElementDeclaration(_DesignObj=A13_NbodyRingforDeepNwell_KJH._NbodyRingforDeepNwell_KJH(_DesignParameter=None,_Name='{}:SRF_Nbodyring'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_Nbodyring']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_Nbodyring']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_Nbodyring']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate
        self._DesignParameter['SRF_Nbodyring']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_Nbodyring']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        target_coord = [tmp['_Mostleft']['coord'][0], tmp['_Mostdown']['coord'][0]]
        ## Approaching_coord
        ## x
        tmp2_1 = self.get_param_KJH4('SRF_Nbodyring', 'SRF_NbodyLeft', 'SRF_NbodyContactPhyLen', 'BND_Nwell')
        approaching_coordx = tmp2_1[0][0][0][0][0]['_XY_right'][0]
        ## y
        tmp2_2 = self.get_param_KJH4('SRF_Nbodyring', 'SRF_NbodyBottom', 'SRF_NbodyContactPhyLen', 'BND_Nwell')
        approaching_coordy = tmp2_2[0][0][0][0][0]['_XY_up'][1]

        approaching_coord = [approaching_coordx, approaching_coordy]
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Nbodyring')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] - _left_margin2
        New_Scoord[1] = New_Scoord[1] - _down_margin2
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_Nbodyring']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Guardring: T3(DeepNwell)
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT / DEEPNWELL
        self._DesignParameter['BND_Deepnwell'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['DEEPNWELL'][0],
        _Datatype=DesignParameters._LayerMapping['DEEPNWELL'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Nbodyring','BND_ExtenNwell_Top')
        tmp2 = self.get_param_KJH4('SRF_Nbodyring','BND_ExtenNwell_Bottom')
        self._DesignParameter['BND_Deepnwell']['_YWidth'] = abs( tmp1[0][0][0]['_XY_down'][1] - tmp2[0][0][0]['_XY_up'][1] ) + _DRCobj._T3NwellOverlap * 2

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Nbodyring','BND_ExtenNwell_Right')
        tmp2 = self.get_param_KJH4('SRF_Nbodyring','BND_ExtenNwell_Left')
        self._DesignParameter['BND_Deepnwell']['_XWidth'] = abs( tmp1[0][0][0]['_XY_left'][0] - tmp2[0][0][0]['_XY_right'][0] ) + _DRCobj._T3NwellOverlap * 2

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Deepnwell']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Deepnwell']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Nbodyring', 'BND_ExtenNwell_Bottom')
        tmp2 = self.get_param_KJH4('SRF_Nbodyring', 'BND_ExtenNwell_Left')
        target_coordx = tmp2[0][0][0]['_XY_right'][0]
        target_coordy = tmp1[0][0][0]['_XY_up'][1]
        target_coord = [ target_coordx, target_coordy ]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Deepnwell')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Deepnwell')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] - _DRCobj._T3NwellOverlap
        New_Scoord[1] = New_Scoord[1] - _DRCobj._T3NwellOverlap
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Deepnwell']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr4 Source and pbody M1 connection
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Tr4_Source_Vtc_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Tr4','SRF_Nmos','BND_Source_M1')
        tmp2 = self.get_param_KJH4('SRF_Pbodyring','SRF_PbodyBottom','SRF_PbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_Tr4_Source_Vtc_M1']['_YWidth'] = abs(tmp1[0][0][0][0]['_XY_down'][1] - tmp2[0][0][0][0][0]['_XY_up'][1])

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Tr4','SRF_Nmos','BND_Source_M1')
        self._DesignParameter['BND_Tr4_Source_Vtc_M1']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Tr4_Source_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Tr4_Source_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
        tmp = self.get_param_KJH4('SRF_Tr4','SRF_Nmos','BND_Source_M1')
        for i in range(0,len(tmp[0][0])):
                                ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Tr4','SRF_Nmos','BND_Source_M1')
            target_coord = tmp1[0][0][i][0]['_XY_down_left']
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Tr4_Source_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_up_left']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Tr4_Source_Vtc_M1')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord,Scoord)
            tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Tr4_Source_Vtc_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## GR135 DRC
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## GR135 DRC: delete Pbody top
        del self._DesignParameter['SRF_Pbodyring']['_DesignObj']._DesignParameter['SRF_PbodyTop']
        del self._DesignParameter['SRF_Pbodyring']['_DesignObj']._DesignParameter['BND_ExtenODLayer_Top']
        del self._DesignParameter['SRF_Pbodyring']['_DesignObj']._DesignParameter['BND_ExtenMet1Layer_Top']
        del self._DesignParameter['SRF_Pbodyring']['_DesignObj']._DesignParameter['BND_ExtenPPLayer_Top']


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## GR135 DRC: RX P+ within T3
        ## Pre-defined

            ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length']   = None
        _Caculation_Parameters['_NumCont']  = 1
        _Caculation_Parameters['_Vtc_flag'] = False

                ## Cal length
        tmp1 = self.get_outter_KJH4('SRF_Pbodyring','SRF_PbodyLeft')
        tmp2 = self.get_outter_KJH4('SRF_Pbodyring','SRF_PbodyRight')
        Intlength = abs( tmp2['_Mostleft']['coord'][0] - tmp1['_Mostright']['coord'][0] )
        _Caculation_Parameters['_Length']   = Intlength

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Pbody_withinT3'] = self._SrefElementDeclaration(_DesignObj=A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen(_DesignParameter=None, _Name='{}:SRF_Pbody_withinT3'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Pbody_withinT3']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbody_withinT3']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbody_withinT3']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbody_withinT3']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Pbody_withinT3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##y
        tmp1_1 = self.get_param_KJH4('SRF_Nbodyring', 'SRF_NbodyTop', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        target_coordy = tmp1_1[0][0][0][0][0]['_XY_down'][1]
                                ##x
        tmp1_2 = self.get_param_KJH4('SRF_Pbodyring', 'SRF_PbodyLeft', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        tmp1_3 = self.get_param_KJH4('SRF_Pbodyring', 'SRF_PbodyRight', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        target_coordx = np.round(0.5 * (tmp1_3[0][0][0][0][0]['_XY_left'][0] + tmp1_2[0][0][0][0][0]['_XY_right'][0] ))

        target_coord = [ target_coordx, target_coordy ]

                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_outter_KJH4('SRF_Pbody_withinT3')
        approaching_coordy = tmp2['_Mostup']['coord'][0]
        approaching_coordx = np.round(0.5*( tmp2['_Mostright']['coord'][0] + tmp2['_Mostleft']['coord'][0] ))
        approaching_coord = [ approaching_coordx, approaching_coordy]

                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pbody_withinT3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[1] = New_Scoord[1] - _DRCobj._MetalxMinSpace41
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Pbody_withinT3']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## GR135 DRC: RX P+ within T3: DRC Straddle Bp >0.56
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Pbody_withinT3_ExtenPP'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['PIMP'][0],
        _Datatype=DesignParameters._LayerMapping['PIMP'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_outter_KJH4('SRF_Pbody_withinT3','SRF_PbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_Pbody_withinT3_ExtenPP']['_YWidth'] = abs(tmp1['_Mostup']['coord'][0] - tmp1['_Mostdown']['coord'][0]) + _DRCobj._GR353 * 2

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Pbody_withinT3','SRF_PbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_Pbody_withinT3_ExtenPP']['_XWidth'] = tmp[0][0][0][0]['_Xwidth'] + _DRCobj._GR353 * 2

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Pbody_withinT3_ExtenPP']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Pbody_withinT3_ExtenPP']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Pbody_withinT3','SRF_PbodyContactPhyLen','BND_PPLayer')
        target_coord = tmp1[0][0][0][0]['_XY_cent']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Pbody_withinT3_ExtenPP')
        approaching_coord = tmp2[0][0]['_XY_cent']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Pbody_withinT3_ExtenPP')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['BND_Pbody_withinT3_ExtenPP']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## GR135 DRC: RX N+ within T3
            ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A07_NbodyContactPhyLen_KJH3._NbodyContactPhyLen._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length']   = None
        _Caculation_Parameters['_NumCont']  = 1
        _Caculation_Parameters['_Vtc_flag'] = False

                ## Cal length
        tmp1 = self.get_outter_KJH4('SRF_Pbodyring','SRF_PbodyLeft')
        tmp2 = self.get_outter_KJH4('SRF_Pbodyring','SRF_PbodyRight')
        Intlength = abs( tmp2['_Mostleft']['coord'][0] - tmp1['_Mostright']['coord'][0] )
        _Caculation_Parameters['_Length']   = Intlength

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Nbody_withinT3'] = self._SrefElementDeclaration(_DesignObj=A07_NbodyContactPhyLen_KJH3._NbodyContactPhyLen(_DesignParameter=None, _Name='{}:SRF_Nbody_withinT3'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Nbody_withinT3']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nbody_withinT3']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nbody_withinT3']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nbody_withinT3']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Nbody_withinT3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##Y
        tmp1_1 = self.get_param_KJH4('SRF_Nbodyring', 'BND_ExtenNwell_Top')
        target_coordy = tmp1_1[0][0][0]['_XY_down'][1]
                                ##X
        tmp1_2 = self.get_param_KJH4('SRF_Pbody_withinT3','SRF_PbodyContactPhyLen','BND_Met1Layer')
        target_coordx = tmp1_2[0][0][0][0]['_XY_cent'][0]

        target_coord = [target_coordx, target_coordy]

                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_outter_KJH4('SRF_Nbody_withinT3')
        approaching_coordy = tmp2['_Mostup']['coord'][0]
        approaching_coordx = np.round(0.5*( tmp2['_Mostright']['coord'][0] + tmp2['_Mostleft']['coord'][0] ))
        approaching_coord = [ approaching_coordx, approaching_coordy]

                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Nbody_withinT3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[1] = New_Scoord[1] - _DRCobj._MetalxMinSpace41
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Nbody_withinT3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## GR135 DRC: RX N+ within T3: delete Nwell
        del self._DesignParameter['SRF_Nbody_withinT3']['_DesignObj']._DesignParameter['SRF_NbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_Nwell']


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## GR135 DRC: RX P+ and RX N+ M1 connection
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Pbody_Nbody_withinT3_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Pbody_withinT3','SRF_PbodyContactPhyLen','BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_Nbody_withinT3','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_Pbody_Nbody_withinT3_M1']['_YWidth'] = abs(tmp1[0][0][0][0]['_XY_down'][1] - tmp2[0][0][0][0]['_XY_up'][1])

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Pbody_Nbody_withinT3_M1']['_XWidth'] = 50

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Pbody_Nbody_withinT3_M1']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Pbody_Nbody_withinT3_M1']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Nbody_withinT3','SRF_NbodyContactPhyLen','BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_up']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Pbody_Nbody_withinT3_M1')
        approaching_coord = tmp2[0][0]['_XY_down']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Pbody_Nbody_withinT3_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['BND_Pbody_Nbody_withinT3_M1']['_XYCoordinates'] = tmpXY


        ## LVS1 Drawing8 Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_LVS1DRW8'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['LVS1_dr8'][0],
        _Datatype=DesignParameters._LayerMapping['LVS1_dr8'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Pbodyring', 'SRF_PbodyBottom', 'SRF_PbodyContactPhyLen', 'BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_Pbodyring', 'SRF_PbodyLeft', 'SRF_PbodyContactPhyLen', 'BND_PPLayer')
        self._DesignParameter['BND_LVS1DRW8']['_YWidth'] = tmp2[0][0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_LVS1DRW8']['_XWidth'] = tmp1[0][0][0][0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_LVS1DRW8']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1_1 = tmp1[0][0][0][0][0]['_XY_left'][0]
        tmp1_2 = tmp2[0][0][0][0][0]['_XY_down'][1]
        target_coord = [tmp1_1, tmp1_2]
                            ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_LVS1DRW8')
        approaching_coord = tmp3[0][0]['_XY_down_left']
                            ## Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_LVS1DRW8']['_XYCoordinates'] = tmpXY

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
    libname = 'Proj_ZZ01_C03_01_Guardring_Fixed'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'C03_01_Guardring_v0_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
#TR4
    # Physical dimension
    _Tr4_NumberofGate	            = 4,       # Number
    _Tr4_ChannelWidth	            = 500,     # Number
    _Tr4_ChannelLength	            = 30,       # Number
    _Tr4_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT



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
