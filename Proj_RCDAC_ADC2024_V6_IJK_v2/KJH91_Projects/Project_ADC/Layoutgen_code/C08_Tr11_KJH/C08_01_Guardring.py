
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
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A03_NmosWithDummy_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A04_PmosWithDummy_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A05_NbodyContact_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A06_PbodyContact_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A07_NbodyContactPhyLen_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A08_PbodyContactPhyLen_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A09_NbodyRing_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A10_PbodyRing_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A11_NbodyContactforDeepNwell_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A12_NbodyContactPhyLenforDeepNwell_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A13_NbodyRingforDeepNwell_KJH
    ##
from KJH91_Projects.Project_ADC.Layoutgen_code.C08_Tr11_KJH import C08_00_Tr11



## Define Class
class _Guardring(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(

        # PMOS: Tr11
        _Tr11_PMOSNumberofGate       =2,
        _Tr11_PMOSChannelWidth       =1000,
        _Tr11_PMOSChannellength      =30,
        _Tr11_GateSpacing            =None,
        _Tr11_SDWidth                =None,
        _Tr11_XVT                    ='SLVT',
        _Tr11_PCCrit                 =None,

            # Source_node_ViaM1M2
        _Tr11_Source_Via_TF          =True,

            # Drain_node_ViaM1M2
        _Tr11_Drain_Via_TF           =True,

            # POLY dummy setting
        _Tr11_PMOSDummy              =True,  # TF
                # if _PMOSDummy == True
        _Tr11_PMOSDummy_length       =None,  # None/Value
        _Tr11_PMOSDummy_placement    =None,  # None/'Up'/'Dn'/

        # Nbodyring(Guardring)
        _Tr11_Guardring_NumCont=3,  # number

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

                                  # PMOS: Tr11
                                  _Tr11_PMOSNumberofGate=2,
                                  _Tr11_PMOSChannelWidth=1000,
                                  _Tr11_PMOSChannellength=30,
                                  _Tr11_GateSpacing=None,
                                  _Tr11_SDWidth=None,
                                  _Tr11_XVT='SLVT',
                                  _Tr11_PCCrit=None,

                                  # Source_node_ViaM1M2
                                  _Tr11_Source_Via_TF=True,

                                  # Drain_node_ViaM1M2
                                  _Tr11_Drain_Via_TF=True,

                                  # POLY dummy setting
                                  _Tr11_PMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tr11_PMOSDummy_length=None,  # None/Value
                                  _Tr11_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Nbodyring(Guardring)
                                  _Tr11_Guardring_NumCont=3,  # number

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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr11
            ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C08_00_Tr11._Tr11._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr11_PMOSNumberofGate']     = _Tr11_PMOSNumberofGate
        _Caculation_Parameters['_Tr11_PMOSChannelWidth']     = _Tr11_PMOSChannelWidth
        _Caculation_Parameters['_Tr11_PMOSChannellength']    = _Tr11_PMOSChannellength
        _Caculation_Parameters['_Tr11_GateSpacing']          = _Tr11_GateSpacing
        _Caculation_Parameters['_Tr11_SDWidth']              = _Tr11_SDWidth
        _Caculation_Parameters['_Tr11_XVT']                  = _Tr11_XVT
        _Caculation_Parameters['_Tr11_PCCrit']               = _Tr11_PCCrit
        _Caculation_Parameters['_Tr11_Source_Via_TF']        = _Tr11_Source_Via_TF
        _Caculation_Parameters['_Tr11_Drain_Via_TF']         = _Tr11_Drain_Via_TF
        _Caculation_Parameters['_Tr11_PMOSDummy']            = _Tr11_PMOSDummy
        _Caculation_Parameters['_Tr11_PMOSDummy_length']     = _Tr11_PMOSDummy_length
        _Caculation_Parameters['_Tr11_PMOSDummy_placement']  = _Tr11_PMOSDummy_placement

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Tr11'] = self._SrefElementDeclaration(_DesignObj=C08_00_Tr11._Tr11(_DesignParameter=None, _Name='{}:SRF_Tr11'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Tr11']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr11']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr11']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr11']['_XYCoordinates'] = [[0, 0]]

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Nbodyring
        ## Guardring
            ## Pre-defined
        _right_margin = 150
        _left_margin = 150
        _up_margin = 150
        _down_margin = 150

            ## Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A09_NbodyRing_KJH3._NbodyRing._ParametersForDesignCalculation)
        _Caculation_Parameters['_XlengthIntn']      = None
        _Caculation_Parameters['_YlengthIntn']      = None
        _Caculation_Parameters['_NumContTop']       = _Tr11_Guardring_NumCont
        _Caculation_Parameters['_NumContBottom']    = _Tr11_Guardring_NumCont
        _Caculation_Parameters['_NumContLeft']      = _Tr11_Guardring_NumCont
        _Caculation_Parameters['_NumContRight']     = _Tr11_Guardring_NumCont
        #_Caculation_Parameters['_NwellWidth']       = _NwellWidth ## used only for DeepNwell

            ## Find Outter boundary
        tmp = self.get_outter_KJH4('SRF_Tr11')

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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Nwell Covering
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
        tmp1 = self.get_param_KJH4('SRF_Nbodyring','BND_ExtenNwell_Top')
        tmp2 = self.get_param_KJH4('SRF_Nbodyring','BND_ExtenNwell_Bottom')

        self._DesignParameter['BND_Nwellcovering']['_YWidth'] = abs( tmp1[0][0][0]['_XY_up'][1] - tmp2[0][0][0]['_XY_down'][1] )

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Nbodyring','BND_ExtenNwell_Left')
        tmp2 = self.get_param_KJH4('SRF_Nbodyring','BND_ExtenNwell_Right')

        self._DesignParameter['BND_Nwellcovering']['_XWidth'] = abs( tmp2[0][0][0]['_XY_right'][0] - tmp1[0][0][0]['_XY_left'][0] )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Nwellcovering']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Nwellcovering']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Nbodyring','BND_ExtenNwell_Bottom')
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


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Drain and Guardring M1 connection.
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Drain_Vtc_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Tr11','SRF_Pmos','BND_Met1Layer_Drain')
        tmp2 = self.get_param_KJH4('SRF_Nbodyring','SRF_NbodyBottom','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_Drain_Vtc_M1']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_down'][1] - tmp2[0][0][0][0][0]['_XY_up'][1] )

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Tr11','SRF_Pmos','BND_Met1Layer_Drain')
        self._DesignParameter['BND_Drain_Vtc_M1']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Drain_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
        tmp = self.get_param_KJH4('SRF_Tr11','SRF_Pmos','BND_Met1Layer_Drain')
        for i in range(0,len(tmp[0][0])):
                            ## initialized Sref coordinate
            self._DesignParameter['BND_Drain_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Tr11','SRF_Pmos','BND_Met1Layer_Drain')
            target_coord = tmp1[0][0][i][0]['_XY_down_left']
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Drain_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_up_left']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Drain_Vtc_M1')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Drain_Vtc_M1']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Gate: M4
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Gate: M4 metal Gen.
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Gate_Hrz_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('SRF_Tr11','BND_Pmos_Gate_Hrz_poly')
        self._DesignParameter['BND_Gate_Hrz_M2']['_YWidth'] = tmp[0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Tr11','BND_Pmos_Gate_Hrz_poly')
        self._DesignParameter['BND_Gate_Hrz_M2']['_XWidth'] = tmp[0][0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Gate_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Gate_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Tr11','BND_Pmos_Gate_Hrz_poly')
        target_coord = tmp1[0][0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Gate_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Gate_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Gate_Hrz_M2']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Gate: ViaM0M4.
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 0
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Gate_ViaM0M2'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None, _Name='{}:SRF_Gate_ViaM0M2'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Gate_ViaM0M2']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Gate_ViaM0M2']['_Angle'] = 0

            ## Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH4('BND_Gate_Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_Tr11','BND_Pmos_Gate_Hrz_poly')
        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0][0])

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

            ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = max(_COX, 2)
        _Caculation_Parameters['_COY'] = _COY

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Gate_ViaM0M2']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Gate_ViaM0M2']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        tmp1 = self.get_param_KJH4('BND_Gate_Hrz_M2')
        target_coord = tmp1[0][0]['_XY_cent']
                    ## Approaching_coord
        if _COX == 1:
            tmp2 = self.get_param_KJH4('SRF_Gate_ViaM0M2','SRF_ViaM0M1','BND_COLayer')
        else:
            tmp2 = self.get_param_KJH4('SRF_Gate_ViaM0M2', 'SRF_ViaM0M1', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Gate_ViaM0M2')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Gate_ViaM0M2']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Source: M4
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Source: M4 metal Gen.
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Source_Hrz_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('SRF_Tr11','BND_Pmos_Source_Hrz_M2')
        self._DesignParameter['BND_Source_Hrz_M3']['_YWidth'] = tmp[0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Tr11','BND_Pmos_Source_Hrz_M2')
        self._DesignParameter['BND_Source_Hrz_M3']['_XWidth'] = tmp[0][0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Source_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Source_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Tr11','BND_Pmos_Source_Hrz_M2')
        target_coord = tmp1[0][0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Source_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Source_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Source_Hrz_M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Source: ViaM2M3 Gen.
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Source_ViaM2M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None, _Name='{}:SRF_Source_ViaM2M3'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Source_ViaM2M3']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Source_ViaM2M3']['_Angle'] = 0

            ## Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH4('BND_Source_Hrz_M3')
        tmp2 = self.get_param_KJH4('SRF_Tr11','BND_Pmos_Source_Hrz_M2')
        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0][0])

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

            ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = max(2,_COX)
        _Caculation_Parameters['_COY'] = max(1,_COY)

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Source_ViaM2M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Source_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        tmp1 = self.get_param_KJH4('BND_Source_Hrz_M3')
        target_coord = tmp1[0][0]['_XY_cent']
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Source_ViaM2M3','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Source_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Source_ViaM2M3']['_XYCoordinates'] = tmpXY

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
    libname = 'Proj_RcdacSar_C08_Tr11'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'C08_01_Guardring_v0_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

        # PMOS: Tr11
        _Tr11_PMOSNumberofGate       =8,
        _Tr11_PMOSChannelWidth       =1000,
        _Tr11_PMOSChannellength      =30,
        _Tr11_GateSpacing            =None,
        _Tr11_SDWidth                =None,
        _Tr11_XVT                    ='SLVT',
        _Tr11_PCCrit                 =None,

            # Source_node_ViaM1M2
        _Tr11_Source_Via_TF          =True,

            # Drain_node_ViaM1M2
        _Tr11_Drain_Via_TF           =True,

            # POLY dummy setting
        _Tr11_PMOSDummy              =True,  # TF
                # if _PMOSDummy == True
        _Tr11_PMOSDummy_length       =None,  # None/Value
        _Tr11_PMOSDummy_placement    =None,  # None/'Up'/'Dn'/

        # Nbodyring(Guardring)
        _Tr11_Guardring_NumCont = 3, #number

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
