
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
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A03_NmosWithDummy_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A04_PmosWithDummy_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A05_NbodyContact_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A06_PbodyContact_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A07_NbodyContactPhyLen_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A08_PbodyContactPhyLen_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A09_NbodyRing_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A10_PbodyRing_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A11_NbodyContactforDeepNwell_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A12_NbodyContactPhyLenforDeepNwell_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A13_NbodyRingforDeepNwell_KJH

    ##
from Proj_RCDAC_ADC2024_V6_IJK.KJH91_Projects.Project_ADC.Layoutgen_code.C02_Tr5Tr7Tr9_Ctop_Fixed import C02_03_Tr5Tr7Tr9


## Define Class
class _Guardring(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
# TR5
    # Physical dimension
    _Tr5_NumberofGate	            = 2,       # Number
    _Tr5_ChannelWidth	            = 1000,     # Number
    _Tr5_ChannelLength	            = 30,       # Number
    _Tr5_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR7
    # Physical dimension
    _Tr7_NumberofGate               = 3,  # Number
    _Tr7_ChannelWidth	            = 233,     # Number
    _Tr7_ChannelLength	            = 30,       # Number
    _Tr7_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR9
    # Physical dimension
    _Tr9_NumberofGate               = 3,  # Number
    _Tr9_ChannelWidth	            = 500,     # Number
    _Tr9_ChannelLength	            = 30,       # Number
    _Tr9_XVT				        = 'LVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT



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

# TR5
    # Physical dimension
    _Tr5_NumberofGate	            = 2,       # Number
    _Tr5_ChannelWidth	            = 1000,     # Number
    _Tr5_ChannelLength	            = 30,       # Number
    _Tr5_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR7
    # Physical dimension
    _Tr7_NumberofGate               = 3,  # Number
    _Tr7_ChannelWidth	            = 233,     # Number
    _Tr7_ChannelLength	            = 30,       # Number
    _Tr7_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR9
    # Physical dimension
    _Tr9_NumberofGate               = 3,  # Number
    _Tr9_ChannelWidth	            = 500,     # Number
    _Tr9_ChannelLength	            = 30,       # Number
    _Tr9_XVT				        = 'LVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT


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


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr5 Tr7 Tr9
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr5 Tr7 Tr9: Sref Gen

            ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C02_03_Tr5Tr7Tr9._Tr5Tr7Tr9._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr5_NumberofGate']     = _Tr5_NumberofGate
        _Caculation_Parameters['_Tr5_ChannelWidth']     = _Tr5_ChannelWidth
        _Caculation_Parameters['_Tr5_ChannelLength']    = _Tr5_ChannelLength
        _Caculation_Parameters['_Tr5_XVT']              = _Tr5_XVT

        _Caculation_Parameters['_Tr7_NumberofGate']     = _Tr7_NumberofGate
        _Caculation_Parameters['_Tr7_ChannelWidth']     = _Tr7_ChannelWidth
        _Caculation_Parameters['_Tr7_ChannelLength']    = _Tr7_ChannelLength
        _Caculation_Parameters['_Tr7_XVT']              = _Tr7_XVT

        _Caculation_Parameters['_Tr9_NumberofGate']     = _Tr9_NumberofGate
        _Caculation_Parameters['_Tr9_ChannelWidth']     = _Tr9_ChannelWidth
        _Caculation_Parameters['_Tr9_ChannelLength']    = _Tr9_ChannelLength
        _Caculation_Parameters['_Tr9_XVT']              = _Tr9_XVT

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Tr5Tr7Tr9'] = self._SrefElementDeclaration(_DesignObj=C02_03_Tr5Tr7Tr9._Tr5Tr7Tr9(_DesignParameter=None, _Name='{}:SRF_Tr5Tr7Tr9'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Tr5Tr7Tr9']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr5Tr7Tr9']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr5Tr7Tr9']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr5Tr7Tr9']['_XYCoordinates'] = [[0, 0]]


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Guardring
        ## Pre-defined
        _NumCont = 2

        _right_margin = 300
        _left_margin = 300
        _up_margin = 300
        _down_margin = 300

        ## Guardring
            ## Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A09_NbodyRing_KJH3._NbodyRing._ParametersForDesignCalculation)
        _Caculation_Parameters['_XlengthIntn']      = None
        _Caculation_Parameters['_YlengthIntn']      = None
        _Caculation_Parameters['_NumContTop']       = _NumCont
        _Caculation_Parameters['_NumContBottom']    = _NumCont
        _Caculation_Parameters['_NumContLeft']      = _NumCont
        _Caculation_Parameters['_NumContRight']     = _NumCont

            ## Find Outter boundary
        tmp = self.get_outter_KJH4('SRF_Tr5Tr7Tr9')

            ## Define _XlengthIntn
        _Caculation_Parameters['_XlengthIntn'] = abs(tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0]) + _right_margin + _left_margin # option: + _NwellWidth

            ## Define _YlengthIntn
        _Caculation_Parameters['_YlengthIntn'] = abs(tmp['_Mostup']['coord'][0] - tmp['_Mostdown']['coord'][0]) + _up_margin + _down_margin # option + _NwellWidth

            ## Generate Sref
        self._DesignParameter['SRF_Nbodyring'] = self._SrefElementDeclaration(_DesignObj=A09_NbodyRing_KJH3._NbodyRing(_DesignParameter=None, _Name='{}:_Nbodyring'.format(_Name)))[0]

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
        tmp2_1 = self.get_param_KJH4('SRF_Nbodyring', 'SRF_NbodyLeft', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coordx = tmp2_1[0][0][0][0][0]['_XY_right'][0]
                        ## y
        tmp2_2 = self.get_param_KJH4('SRF_Nbodyring', 'SRF_NbodyBottom', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coordy = tmp2_2[0][0][0][0][0]['_XY_up'][1]

        approaching_coord = [approaching_coordx, approaching_coordy]
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Nbodyring')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] - _left_margin # option: - _NwellWidth
        New_Scoord[1] = New_Scoord[1] - _down_margin # option: - _NwellWidth
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Nbodyring']['_XYCoordinates'] = tmpXY



        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Nwell covering
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Nwellcovering'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['NWELL'][0],
        _Datatype=DesignParameters._LayerMapping['NWELL'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Nbodyring', 'SRF_NbodyTop', 'SRF_NbodyContactPhyLen', 'BND_Nwell')
        tmp2 = self.get_param_KJH4('SRF_Nbodyring', 'SRF_NbodyBottom', 'SRF_NbodyContactPhyLen', 'BND_Nwell')

        self._DesignParameter['BND_Nwellcovering']['_YWidth'] = abs( tmp1[0][0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0]['_XY_down'][1] )

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Nbodyring', 'SRF_NbodyRight', 'SRF_NbodyContactPhyLen', 'BND_Nwell')
        tmp2 = self.get_param_KJH4('SRF_Nbodyring', 'SRF_NbodyLeft', 'SRF_NbodyContactPhyLen', 'BND_Nwell')
        self._DesignParameter['BND_Nwellcovering']['_XWidth'] = abs( tmp1[0][0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0][0]['_XY_left'][0] )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Nwellcovering']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Nwellcovering']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Nbodyring', 'BND_ExtenNwell_Bottom')
        target_coord = tmp1[0][0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Nwellcovering')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Nwellcovering')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Nwellcovering']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## DeepNwell
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
        self._DesignParameter['BND_Deepnwell']['_YWidth'] = abs( tmp1[0][0][0]['_XY_up'][1] - tmp2[0][0][0]['_XY_down'][1] ) #+ _DRCobj._T3NwellOverlap * 2

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Nbodyring','BND_ExtenNwell_Right')
        tmp2 = self.get_param_KJH4('SRF_Nbodyring','BND_ExtenNwell_Left')
        self._DesignParameter['BND_Deepnwell']['_XWidth'] = abs( tmp1[0][0][0]['_XY_right'][0] - tmp2[0][0][0]['_XY_left'][0] ) #+ _DRCobj._T3NwellOverlap * 2

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
        target_coordx = tmp2[0][0][0]['_XY_left'][0]
        target_coordy = tmp1[0][0][0]['_XY_down'][1]
        target_coord = [ target_coordx, target_coordy ]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Deepnwell')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Deepnwell')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] #- _DRCobj._T3NwellOverlap
        New_Scoord[1] = New_Scoord[1] #- _DRCobj._T3NwellOverlap
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Deepnwell']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr5 Drain and Guardring M1 connection.
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Tr5_Source_Vtc_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Tr5Tr7Tr9','SRF_Tr5','BND_Source_M1')
        tmp2 = self.get_param_KJH4('SRF_Nbodyring','SRF_NbodyBottom','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_Tr5_Source_Vtc_M1']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_down'][1] - tmp2[0][0][0][0][0]['_XY_up'][1] )

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr5', 'BND_Source_M1')
        self._DesignParameter['BND_Tr5_Source_Vtc_M1']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Tr5_Source_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []

        tmp = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr5', 'BND_Source_M1')
        for i in range(0,len(tmp[0][0])):
                            ## Calculate
                                ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr5', 'BND_Source_M1')
            target_coord = tmp1[0][0][i][0]['_XY_down_left']
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Tr5_Source_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_up_left']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Tr5_Source_Vtc_M1')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Tr5_Source_Vtc_M1']['_XYCoordinates'] = tmpXY

        
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr7 Drain and Guardring M1 connection.
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Tr7_Drain_Vtc_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Tr5Tr7Tr9','SRF_Tr7','BND_Drain_M1')
        tmp2 = self.get_param_KJH4('SRF_Nbodyring','SRF_NbodyBottom','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_Tr7_Drain_Vtc_M1']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_down'][1] - tmp2[0][0][0][0][0]['_XY_up'][1] )

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr7', 'BND_Drain_M1')
        self._DesignParameter['BND_Tr7_Drain_Vtc_M1']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Tr7_Drain_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []

        tmp = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr7', 'BND_Drain_M1')
        for i in range(0,len(tmp[0][0])):
                            ## Calculate
                                ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr7', 'BND_Drain_M1')
            target_coord = tmp1[0][0][i][0]['_XY_down_left']
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Tr7_Drain_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_up_left']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Tr7_Drain_Vtc_M1')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Tr7_Drain_Vtc_M1']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr9 Drain and Guardring M1 connection.
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Tr9_Source_Vtc_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Tr5Tr7Tr9','SRF_Tr9','BND_Source_M1')
        tmp2 = self.get_param_KJH4('SRF_Nbodyring','SRF_NbodyTop','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_Tr9_Source_Vtc_M1']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0]['_XY_down'][1] )

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr9', 'BND_Source_M1')
        self._DesignParameter['BND_Tr9_Source_Vtc_M1']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Tr9_Source_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []

        tmp = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr9', 'BND_Source_M1')
        for i in range(0,len(tmp[0][0])):
                            ## Calculate
                                ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr9', 'BND_Source_M1')
            target_coord = tmp1[0][0][i][0]['_XY_up_left']
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Tr9_Source_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_down_left']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Tr9_Source_Vtc_M1')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Tr9_Source_Vtc_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr5 gate and Tr7 gate combine
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr5 gate and Tr7 gate combine: Hrz M3
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Tr5Tr7_Gate_Hrz_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Tr5Tr7_Gate_Hrz_M3']['_YWidth'] = 60

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr5','BND_Gate_Hrz_Mx')
        tmp2 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr7','BND_Gate_Hrz_Mx')

        self._DesignParameter['BND_Tr5Tr7_Gate_Hrz_M3']['_XWidth'] = abs( tmp1[0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0]['_XY_right'][0] )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Tr5Tr7_Gate_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Tr5Tr7_Gate_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr5','BND_Gate_Hrz_Mx')
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Tr5Tr7_Gate_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Tr5Tr7_Gate_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Tr5Tr7_Gate_Hrz_M3']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr7 Source and Tr9 gate combine
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr7 Source and Tr9 gate combine: Hrz M2
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Tr7_Source_Tr9_Gate_Hrz_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Tr7_Source_Tr9_Gate_Hrz_M2']['_YWidth'] = 50

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr7', 'BND_Source_Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr9', 'BND_Gate_Hrz_Mx')

        self._DesignParameter['BND_Tr7_Source_Tr9_Gate_Hrz_M2']['_XWidth'] = abs( tmp1[0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0]['_XY_right'][0] )

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Tr7_Source_Tr9_Gate_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Tr7_Source_Tr9_Gate_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr7', 'BND_Source_Hrz_M2')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Tr7_Source_Tr9_Gate_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Tr7_Source_Tr9_Gate_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Tr7_Source_Tr9_Gate_Hrz_M2']['_XYCoordinates'] = tmpXY



        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Guardring: Pbody
        ## Guardring
        ## Pre-defined DRC
        _right_margin = 550
        _left_margin = 550
        _up_margin = 550
        _down_margin = 550

        _NumCont = 3

        ## Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A10_PbodyRing_KJH3._PbodyRing._ParametersForDesignCalculation)
        _Caculation_Parameters['_XlengthIntn'] = None
        _Caculation_Parameters['_YlengthIntn'] = None
        _Caculation_Parameters['_NumContTop'] = _NumCont
        _Caculation_Parameters['_NumContBottom'] = _NumCont
        _Caculation_Parameters['_NumContLeft'] = _NumCont
        _Caculation_Parameters['_NumContRight'] = _NumCont

        ## Find Outter boundary
        tmp = self.get_outter_KJH4('SRF_Nbodyring')

        ## Define _XlengthIntn
        _Caculation_Parameters['_XlengthIntn'] = abs( tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0]) + _right_margin + _left_margin

        ## Define _YlengthIntn
        _Caculation_Parameters['_YlengthIntn'] = abs( tmp['_Mostup']['coord'][0] - tmp['_Mostdown']['coord'][0]) + _up_margin + _down_margin

        ## Generate Sref
        self._DesignParameter['SRF_Pbodyring'] = self._SrefElementDeclaration(_DesignObj=A10_PbodyRing_KJH3._PbodyRing(_DesignParameter=None,_Name='{}:SRF_Pbodyring'.format(_Name)))[0]

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



        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## LVS1 Drawing8 Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_LVS1DRW8'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['LVS1_dr8'][0],
        _Datatype=DesignParameters._LayerMapping['LVS1_dr8'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Nbodyring', 'SRF_NbodyTop', 'SRF_NbodyContactPhyLen', 'BND_Nwell')
        tmp2 = self.get_param_KJH4('SRF_Nbodyring', 'SRF_NbodyLeft', 'SRF_NbodyContactPhyLen', 'BND_Nwell')
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
        tmp1_2 = tmp2[0][0][0][0][0]['_XY_up'][1]
        target_coord = [tmp1_1, tmp1_2]
                            ## Approaching_coord: _XY_type2
        tmp3 = self.get_param_KJH4('BND_LVS1DRW8')
        approaching_coord = tmp3[0][0]['_XY_up_left']
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
    libname = 'Proj_ZZ01_C02_04_Guardring_Fixed'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'C02_04_Guardring_v0_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

# TR5
    # Physical dimension
    _Tr5_NumberofGate	            = 2,       # Number
    _Tr5_ChannelWidth	            = 1000,     # Number
    _Tr5_ChannelLength	            = 30,       # Number
    _Tr5_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR7
    # Physical dimension
    _Tr7_NumberofGate               = 3,  # Number
    _Tr7_ChannelWidth	            = 233,     # Number
    _Tr7_ChannelLength	            = 30,       # Number
    _Tr7_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR9
    # Physical dimension
    _Tr9_NumberofGate               = 3,  # Number
    _Tr9_ChannelWidth	            = 500,     # Number
    _Tr9_ChannelLength	            = 30,       # Number
    _Tr9_XVT				        = 'LVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT


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
