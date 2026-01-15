
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
from KJH91_Projects.Project_ADC.Layoutgen_code.C02_Tr5Tr7Tr9_Ctop_KJH import C02_03_Tr5Tr7Tr9


## Define Class
class _Guardring(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(

        # PMOS: Tr5
        _Tr5_PMOSNumberofGate=None,
        _Tr5_PMOSChannelWidth=None,
        _Tr5_PMOSChannellength=None,
        _Tr5_GateSpacing=None,
        _Tr5_SDWidth=None,
        _Tr5_XVT=None,
        _Tr5_PCCrit=None,

        # Source_node_ViaM1M2
        _Tr5_Source_Via_TF=None,

        # Drain_node_ViaM1M2
        _Tr5_Drain_Via_TF=None,

        # POLY dummy setting
        _Tr5_PMOSDummy=None,  # TF
        # if _PMOSDummy == True
        _Tr5_PMOSDummy_length=None,  # None/Value
        _Tr5_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # PMOS: Tr7
        _Tr7_PMOSNumberofGate=None,
        _Tr7_PMOSChannelWidth=None,
        _Tr7_PMOSChannellength=None,
        _Tr7_GateSpacing=None,
        _Tr7_SDWidth=None,
        _Tr7_XVT=None,
        _Tr7_PCCrit=None,

        # Source_node_ViaM1M2
        _Tr7_Source_Via_TF=None,

        # Drain_node_ViaM1M2
        _Tr7_Drain_Via_TF=None,

        # POLY dummy setting
        _Tr7_PMOSDummy=None,  # TF
        # if _PMOSDummy == True
        _Tr7_PMOSDummy_length=None,  # None/Value
        _Tr7_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # PMOS: Tr9
        _Tr9_PMOSNumberofGate=None,
        _Tr9_PMOSChannelWidth=None,
        _Tr9_PMOSChannellength=None,
        _Tr9_GateSpacing=None,
        _Tr9_SDWidth=None,
        _Tr9_XVT=None,
        _Tr9_PCCrit=None,

        # Source_node_ViaM1M2
        _Tr9_Source_Via_TF=None,

        # Drain_node_ViaM1M2
        _Tr9_Drain_Via_TF=None,

        # POLY dummy setting
        _Tr9_PMOSDummy=None,  # TF
        # if _PMOSDummy == True
        _Tr9_PMOSDummy_length=None,  # None/Value
        _Tr9_PMOSDummy_placement=None,  # None/'Up'/'Dn'/


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

                                  # PMOS: Tr5
                                  _Tr5_PMOSNumberofGate=None,
                                  _Tr5_PMOSChannelWidth=None,
                                  _Tr5_PMOSChannellength=None,
                                  _Tr5_GateSpacing=None,
                                  _Tr5_SDWidth=None,
                                  _Tr5_XVT=None,
                                  _Tr5_PCCrit=None,

                                  # Source_node_ViaM1M2
                                  _Tr5_Source_Via_TF=None,

                                  # Drain_node_ViaM1M2
                                  _Tr5_Drain_Via_TF=None,

                                  # POLY dummy setting
                                  _Tr5_PMOSDummy=None,  # TF
                                  # if _PMOSDummy == True
                                  _Tr5_PMOSDummy_length=None,  # None/Value
                                  _Tr5_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # PMOS: Tr7
                                  _Tr7_PMOSNumberofGate=None,
                                  _Tr7_PMOSChannelWidth=None,
                                  _Tr7_PMOSChannellength=None,
                                  _Tr7_GateSpacing=None,
                                  _Tr7_SDWidth=None,
                                  _Tr7_XVT=None,
                                  _Tr7_PCCrit=None,

                                  # Source_node_ViaM1M2
                                  _Tr7_Source_Via_TF=None,

                                  # Drain_node_ViaM1M2
                                  _Tr7_Drain_Via_TF=None,

                                  # POLY dummy setting
                                  _Tr7_PMOSDummy=None,  # TF
                                  # if _PMOSDummy == True
                                  _Tr7_PMOSDummy_length=None,  # None/Value
                                  _Tr7_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # PMOS: Tr9
                                  _Tr9_PMOSNumberofGate=None,
                                  _Tr9_PMOSChannelWidth=None,
                                  _Tr9_PMOSChannellength=None,
                                  _Tr9_GateSpacing=None,
                                  _Tr9_SDWidth=None,
                                  _Tr9_XVT=None,
                                  _Tr9_PCCrit=None,

                                  # Source_node_ViaM1M2
                                  _Tr9_Source_Via_TF=None,

                                  # Drain_node_ViaM1M2
                                  _Tr9_Drain_Via_TF=None,

                                  # POLY dummy setting
                                  _Tr9_PMOSDummy=None,  # TF
                                  # if _PMOSDummy == True
                                  _Tr9_PMOSDummy_length=None,  # None/Value
                                  _Tr9_PMOSDummy_placement=None,  # None/'Up'/'Dn'/


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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr5, slvtpfet+np
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr5, slvtpfet+np: Sref Gen

            ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C02_03_Tr5Tr7Tr9._Tr5Tr7Tr9._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr5_PMOSNumberofGate']     = _Tr5_PMOSNumberofGate
        _Caculation_Parameters['_Tr5_PMOSChannelWidth']     = _Tr5_PMOSChannelWidth
        _Caculation_Parameters['_Tr5_PMOSChannellength']    = _Tr5_PMOSChannellength
        _Caculation_Parameters['_Tr5_GateSpacing']          = _Tr5_GateSpacing
        _Caculation_Parameters['_Tr5_SDWidth']              = _Tr5_SDWidth
        _Caculation_Parameters['_Tr5_XVT']                  = _Tr5_XVT
        _Caculation_Parameters['_Tr5_PCCrit']               = _Tr5_PCCrit
        _Caculation_Parameters['_Tr5_Source_Via_TF']        = _Tr5_Source_Via_TF
        _Caculation_Parameters['_Tr5_Drain_Via_TF']         = _Tr5_Drain_Via_TF
        _Caculation_Parameters['_Tr5_PMOSDummy']            = _Tr5_PMOSDummy
        _Caculation_Parameters['_Tr5_PMOSDummy_length']     = _Tr5_PMOSDummy_length
        _Caculation_Parameters['_Tr5_PMOSDummy_placement']  = _Tr5_PMOSDummy_placement

        _Caculation_Parameters['_Tr7_PMOSNumberofGate']     = _Tr7_PMOSNumberofGate
        _Caculation_Parameters['_Tr7_PMOSChannelWidth']     = _Tr7_PMOSChannelWidth
        _Caculation_Parameters['_Tr7_PMOSChannellength']    = _Tr7_PMOSChannellength
        _Caculation_Parameters['_Tr7_GateSpacing']          = _Tr7_GateSpacing
        _Caculation_Parameters['_Tr7_SDWidth']              = _Tr7_SDWidth
        _Caculation_Parameters['_Tr7_XVT']                  = _Tr7_XVT
        _Caculation_Parameters['_Tr7_PCCrit']               = _Tr7_PCCrit
        _Caculation_Parameters['_Tr7_Source_Via_TF']        = _Tr7_Source_Via_TF
        _Caculation_Parameters['_Tr7_Drain_Via_TF']         = _Tr7_Drain_Via_TF
        _Caculation_Parameters['_Tr7_PMOSDummy']            = _Tr7_PMOSDummy
        _Caculation_Parameters['_Tr7_PMOSDummy_length']     = _Tr7_PMOSDummy_length
        _Caculation_Parameters['_Tr7_PMOSDummy_placement']  = _Tr7_PMOSDummy_placement

        _Caculation_Parameters['_Tr9_PMOSNumberofGate']     = _Tr9_PMOSNumberofGate
        _Caculation_Parameters['_Tr9_PMOSChannelWidth']     = _Tr9_PMOSChannelWidth
        _Caculation_Parameters['_Tr9_PMOSChannellength']    = _Tr9_PMOSChannellength
        _Caculation_Parameters['_Tr9_GateSpacing']          = _Tr9_GateSpacing
        _Caculation_Parameters['_Tr9_SDWidth']              = _Tr9_SDWidth
        _Caculation_Parameters['_Tr9_XVT']                  = _Tr9_XVT
        _Caculation_Parameters['_Tr9_PCCrit']               = _Tr9_PCCrit
        _Caculation_Parameters['_Tr9_Source_Via_TF']        = _Tr9_Source_Via_TF
        _Caculation_Parameters['_Tr9_Drain_Via_TF']         = _Tr9_Drain_Via_TF
        _Caculation_Parameters['_Tr9_PMOSDummy']            = _Tr9_PMOSDummy
        _Caculation_Parameters['_Tr9_PMOSDummy_length']     = _Tr9_PMOSDummy_length
        _Caculation_Parameters['_Tr9_PMOSDummy_placement']  = _Tr9_PMOSDummy_placement

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
        tmp1 = self.get_param_KJH4('SRF_Tr5Tr7Tr9','SRF_Tr5','SRF_Pmos','BND_Met1Layer_Source')
        tmp2 = self.get_param_KJH4('SRF_Nbodyring','SRF_NbodyBottom','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_Tr5_Source_Vtc_M1']['_YWidth'] = abs( tmp1[0][0][0][0][0]['_XY_down'][1] - tmp2[0][0][0][0][0]['_XY_up'][1] )

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr5', 'SRF_Pmos', 'BND_Met1Layer_Source')
        self._DesignParameter['BND_Tr5_Source_Vtc_M1']['_XWidth'] = tmp[0][0][0][0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Tr5_Source_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []

        tmp = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr5', 'SRF_Pmos', 'BND_Met1Layer_Source')
        for i in range(0,len(tmp[0][0][0])):
                            ## Calculate
                                ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr5', 'SRF_Pmos', 'BND_Met1Layer_Source')
            target_coord = tmp1[0][0][0][i][0]['_XY_down_left']
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
        tmp1 = self.get_param_KJH4('SRF_Tr5Tr7Tr9','SRF_Tr7','SRF_Pmos','BND_Met1Layer_Drain')
        tmp2 = self.get_param_KJH4('SRF_Nbodyring','SRF_NbodyBottom','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_Tr7_Drain_Vtc_M1']['_YWidth'] = abs( tmp1[0][0][0][0][0]['_XY_down'][1] - tmp2[0][0][0][0][0]['_XY_up'][1] )

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr7', 'SRF_Pmos', 'BND_Met1Layer_Drain')
        self._DesignParameter['BND_Tr7_Drain_Vtc_M1']['_XWidth'] = tmp[0][0][0][0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Tr7_Drain_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []

        tmp = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr7', 'SRF_Pmos', 'BND_Met1Layer_Drain')
        for i in range(0,len(tmp[0][0][0])):
                            ## Calculate
                                ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr7', 'SRF_Pmos', 'BND_Met1Layer_Drain')
            target_coord = tmp1[0][0][0][i][0]['_XY_down_left']
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
        tmp1 = self.get_param_KJH4('SRF_Tr5Tr7Tr9','SRF_Tr9','SRF_Pmos','BND_Met1Layer_Source')
        tmp2 = self.get_param_KJH4('SRF_Nbodyring','SRF_NbodyTop','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_Tr9_Source_Vtc_M1']['_YWidth'] = abs( tmp1[0][0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0]['_XY_down'][1] )

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr9', 'SRF_Pmos', 'BND_Met1Layer_Source')
        self._DesignParameter['BND_Tr9_Source_Vtc_M1']['_XWidth'] = tmp[0][0][0][0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Tr9_Source_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []

        tmp = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr9', 'SRF_Pmos', 'BND_Met1Layer_Source')
        for i in range(0,len(tmp[0][0][0])):
                            ## Calculate
                                ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr9', 'SRF_Pmos', 'BND_Met1Layer_Source')
            target_coord = tmp1[0][0][0][i][0]['_XY_up_left']
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
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr5 gate and Tr7 gate combine: Hrz poly
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Tr5Tr7_Gate_Hrz_Poly'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['POLY'][0],
        _Datatype=DesignParameters._LayerMapping['POLY'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Tr5Tr7_Gate_Hrz_Poly']['_YWidth'] = 60

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr5','BND_Pmos_Gate_Hrz_poly')
        tmp2 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr7','BND_Pmos_Gate_Hrz_poly')

        self._DesignParameter['BND_Tr5Tr7_Gate_Hrz_Poly']['_XWidth'] = abs( tmp1[0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0]['_XY_right'][0] )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Tr5Tr7_Gate_Hrz_Poly']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Tr5Tr7_Gate_Hrz_Poly']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr5','BND_Pmos_Gate_Hrz_poly')
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Tr5Tr7_Gate_Hrz_Poly')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Tr5Tr7_Gate_Hrz_Poly')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Tr5Tr7_Gate_Hrz_Poly']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr5 gate and Tr7 gate combine: Hrz Mx(M4)
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
        self._DesignParameter['BND_Tr5Tr7_Gate_Hrz_M3']['_YWidth'] = self._DesignParameter['BND_Tr5Tr7_Gate_Hrz_Poly']['_YWidth']

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Tr5Tr7_Gate_Hrz_M3']['_XWidth'] = self._DesignParameter['BND_Tr5Tr7_Gate_Hrz_Poly']['_XWidth']

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Tr5Tr7_Gate_Hrz_M3']['_XYCoordinates'] = self._DesignParameter['BND_Tr5Tr7_Gate_Hrz_Poly']['_XYCoordinates']
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr5 gate and Tr7 gate combine: ViaM0M3

        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 0
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Tr5Tr7_Gate_ViaM0M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Tr5Tr7_Gate_ViaM0M3'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Tr5Tr7_Gate_ViaM0M3']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Tr5Tr7_Gate_ViaM0M3']['_Angle'] = 0

            ## Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH4('BND_Tr5Tr7_Gate_Hrz_M3')
        tmp2 = self.get_param_KJH4('BND_Tr5Tr7_Gate_Hrz_Poly')
        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

            ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = max(2,_COX)
        _Caculation_Parameters['_COY'] = max(1,_COY)

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Tr5Tr7_Gate_ViaM0M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Tr5Tr7_Gate_ViaM0M3']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        tmp1 = self.get_param_KJH4('BND_Tr5Tr7_Gate_Hrz_Poly')
        target_coord = tmp1[0][0]['_XY_cent']
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Tr5Tr7_Gate_ViaM0M3','SRF_ViaM0M1','BND_POLayer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Tr5Tr7_Gate_ViaM0M3')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Tr5Tr7_Gate_ViaM0M3']['_XYCoordinates'] = tmpXY



        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr5 gate and Tr7 gate combine
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr5 gate and Tr7 gate combine: Hrz M2
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
        tmp1 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr7', 'BND_Pmos_Source_Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr9', 'BND_Pmos_Gate_Hrz_poly')

        self._DesignParameter['BND_Tr7_Source_Tr9_Gate_Hrz_M2']['_XWidth'] = abs( tmp1[0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0]['_XY_right'][0] )

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Tr7_Source_Tr9_Gate_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Tr7_Source_Tr9_Gate_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr7', 'BND_Pmos_Source_Hrz_M2')
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Tr7_Source_Tr9_Gate_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Tr7_Source_Tr9_Gate_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Tr7_Source_Tr9_Gate_Hrz_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr5 gate and Tr7 gate combine: Hrz Mx(M4)
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Tr7_Source_Tr9_Gate_Hrz_M4'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('SRF_Tr5Tr7Tr9','SRF_Tr9','BND_Pmos_Gate_Hrz_poly')
        self._DesignParameter['BND_Tr7_Source_Tr9_Gate_Hrz_M4']['_YWidth'] = tmp[0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr9', 'BND_Pmos_Gate_Hrz_poly')
        self._DesignParameter['BND_Tr7_Source_Tr9_Gate_Hrz_M4']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        tmp = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr9', 'BND_Pmos_Gate_Hrz_poly')
        self._DesignParameter['BND_Tr7_Source_Tr9_Gate_Hrz_M4']['_XYCoordinates'] = [tmp[0][0][0][0]['_XY_origin']]

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr5 gate and Tr7 gate combine: ViaM0M3

        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 0
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        ## Sref ViaX declaration
        self._DesignParameter['BND_Tr7_Source_Tr9_Gate_ViaM0M4'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
            _Name='{}:BND_Tr7_Source_Tr9_Gate_ViaM0M4'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['BND_Tr7_Source_Tr9_Gate_ViaM0M4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['BND_Tr7_Source_Tr9_Gate_ViaM0M4']['_Angle'] = 0

        ## Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr9', 'BND_Pmos_Gate_Hrz_poly')
        tmp2 = self.get_param_KJH4('BND_Tr7_Source_Tr9_Gate_Hrz_M4')
        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0][0][0], tmp2[0][0])

        ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

        ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = max(3, _COX)   # DRC 612b1 At Least 3 Via Required
        _Caculation_Parameters['_COY'] = max(1, _COY)

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['BND_Tr7_Source_Tr9_Gate_ViaM0M4']['_DesignObj']._CalculateDesignParameterYmin( **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Tr7_Source_Tr9_Gate_ViaM0M4']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'SRF_Tr9', 'BND_Pmos_Gate_Hrz_poly')
        target_coord = tmp1[0][0][0][0]['_XY_cent']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Tr7_Source_Tr9_Gate_ViaM0M4', 'SRF_ViaM0M1', 'BND_POLayer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Tr7_Source_Tr9_Gate_ViaM0M4')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['BND_Tr7_Source_Tr9_Gate_ViaM0M4']['_XYCoordinates'] = tmpXY

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
        self._DesignParameter['SRF_Pbodyring'] = self._SrefElementDeclaration(
            _DesignObj=A10_PbodyRing_KJH3._PbodyRing(_DesignParameter=None,
            _Name='{}:SRF_Pbodyring'.format(_Name)))[0]

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

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_RcdacSar_C02_Tr5Tr7Tr9_KJH'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'C02_04_Guardring_v0_98'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

        # PMOS: Tr5
        _Tr5_PMOSNumberofGate       =2,
        _Tr5_PMOSChannelWidth       =1000,
        _Tr5_PMOSChannellength      =30,
        _Tr5_GateSpacing            =None,
        _Tr5_SDWidth                =None,
        _Tr5_XVT                    ='SLVT',
        _Tr5_PCCrit                 =None,

            # Source_node_ViaM1M2
        _Tr5_Source_Via_TF          =True,

            # Drain_node_ViaM1M2
        _Tr5_Drain_Via_TF           =True,

            # POLY dummy setting
        _Tr5_PMOSDummy              =True,  # TF
                # if _PMOSDummy == True
        _Tr5_PMOSDummy_length       =None,  # None/Value
        _Tr5_PMOSDummy_placement    =None,  # None/'Up'/'Dn'/

        # PMOS: Tr7
        _Tr7_PMOSNumberofGate       =4,
        _Tr7_PMOSChannelWidth       =1000,
        _Tr7_PMOSChannellength      =30,
        _Tr7_GateSpacing            =None,
        _Tr7_SDWidth                =None,
        _Tr7_XVT                    ='SLVT',
        _Tr7_PCCrit                 =None,

            # Source_node_ViaM1M2
        _Tr7_Source_Via_TF          =True,

            # Drain_node_ViaM1M2
        _Tr7_Drain_Via_TF           =True,

            # POLY dummy setting
        _Tr7_PMOSDummy              =True,  # TF
                # if _PMOSDummy == True
        _Tr7_PMOSDummy_length       =None,  # None/Value
        _Tr7_PMOSDummy_placement    =None,  # None/'Up'/'Dn'/

        # PMOS: Tr9
        _Tr9_PMOSNumberofGate       =8,
        _Tr9_PMOSChannelWidth       =1000,
        _Tr9_PMOSChannellength      =30,
        _Tr9_GateSpacing            =None,
        _Tr9_SDWidth                =None,
        _Tr9_XVT                    ='RVT',
        _Tr9_PCCrit                 =None,

            # Source_node_ViaM1M2
        _Tr9_Source_Via_TF          =True,

            # Drain_node_ViaM1M2
        _Tr9_Drain_Via_TF           =True,

            # POLY dummy setting
        _Tr9_PMOSDummy              =True,  # TF
                # if _PMOSDummy == True
        _Tr9_PMOSDummy_length       =None,  # None/Value
        _Tr9_PMOSDummy_placement    =None,  # None/'Up'/'Dn'/


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
