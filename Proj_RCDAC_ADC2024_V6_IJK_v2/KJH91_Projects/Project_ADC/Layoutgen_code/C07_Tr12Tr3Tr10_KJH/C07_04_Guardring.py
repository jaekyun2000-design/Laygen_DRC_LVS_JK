
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
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A10_PbodyRing_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A09_NbodyRing_KJH3

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.C07_Tr12Tr3Tr10_KJH import C07_03_Tr12Tr3Tr10_v2


## Define Class
class _Guardring(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(

        # Tr4
        _Tr12_NMOSNumberofGate    =   4,     #number
        _Tr12_NMOSChannelWidth    =   500,   #number
        _Tr12_NMOSChannellength   =   30,     #number
        _Tr12_GateSpacing         =   80,   #None/number
        _Tr12_SDWidth             =   None,   #None/number
        _Tr12_XVT                 =   'RVT',  #'XVT' ex)SLVT LVT RVT HVT
        _Tr12_PCCrit              =   True,   #None/True

            # Source_node_ViaM1M2
        _Tr12_Source_Via_TF       =   True,  #True/False

            # Drain_node_ViaM1M2
        _Tr12_Drain_Via_TF        =   True,  #True/False

            # POLY dummy setting
        _Tr12_NMOSDummy           =   True,  # TF
                # if _PMOSDummy == True
        _Tr12_NMOSDummy_length    =   None,  # None/Value
        _Tr12_NMOSDummy_placement =   None,  # None/'Up'/'Dn'/

        # Tr3
        _Tr3_NMOSNumberofGate=4,  # number
        _Tr3_NMOSChannelWidth=500,  # number
        _Tr3_NMOSChannellength=30,  # number
        _Tr3_GateSpacing=None,  # None/number
        _Tr3_SDWidth=None,  # None/number
        _Tr3_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Tr3_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _Tr3_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _Tr3_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _Tr3_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Tr3_NMOSDummy_length=None,  # None/Value
        _Tr3_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr10
        _Tr10_NMOSNumberofGate=4,  # number
        _Tr10_NMOSChannelWidth=500,  # number
        _Tr10_NMOSChannellength=30,  # number
        _Tr10_GateSpacing=None,  # None/number
        _Tr10_SDWidth=None,  # None/number
        _Tr10_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Tr10_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _Tr10_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _Tr10_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _Tr10_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Tr10_NMOSDummy_length=None,  # None/Value
        _Tr10_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr12Tr3Tr10 Guardring
        _Tr12Tr3Tr10_Guardring_NumCont=3,  # Number
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

                                  # Tr12
                                  _Tr12_NMOSNumberofGate=4,  # number
                                  _Tr12_NMOSChannelWidth=500,  # number
                                  _Tr12_NMOSChannellength=30,  # number
                                  _Tr12_GateSpacing=80,  # None/number
                                  _Tr12_SDWidth=None,  # None/number
                                  _Tr12_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Tr12_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _Tr12_Source_Via_TF=True,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Tr12_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _Tr12_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tr12_NMOSDummy_length=None,  # None/Value
                                  _Tr12_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Tr3
                                  _Tr3_NMOSNumberofGate=4,  # number
                                  _Tr3_NMOSChannelWidth=500,  # number
                                  _Tr3_NMOSChannellength=30,  # number
                                  _Tr3_GateSpacing=None,  # None/number
                                  _Tr3_SDWidth=None,  # None/number
                                  _Tr3_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Tr3_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _Tr3_Source_Via_TF=True,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Tr3_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _Tr3_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tr3_NMOSDummy_length=None,  # None/Value
                                  _Tr3_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Tr10
                                  _Tr10_NMOSNumberofGate=4,  # number
                                  _Tr10_NMOSChannelWidth=500,  # number
                                  _Tr10_NMOSChannellength=30,  # number
                                  _Tr10_GateSpacing=None,  # None/number
                                  _Tr10_SDWidth=None,  # None/number
                                  _Tr10_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Tr10_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _Tr10_Source_Via_TF=True,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Tr10_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _Tr10_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tr10_NMOSDummy_length=None,  # None/Value
                                  _Tr10_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                  # Tr12Tr3Tr10 Guardring
                                  _Tr12Tr3Tr10_Guardring_NumCont=3,  # Number

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
        _Caculation_Parameters['_Tr12_NMOSNumberofGate']     =   _Tr12_NMOSNumberofGate
        _Caculation_Parameters['_Tr12_NMOSChannelWidth']     =   _Tr12_NMOSChannelWidth
        _Caculation_Parameters['_Tr12_NMOSChannellength']    =   _Tr12_NMOSChannellength
        _Caculation_Parameters['_Tr12_GateSpacing']          =   _Tr12_GateSpacing
        _Caculation_Parameters['_Tr12_SDWidth']              =   _Tr12_SDWidth
        _Caculation_Parameters['_Tr12_XVT']                  =   _Tr12_XVT
        _Caculation_Parameters['_Tr12_PCCrit']               =   _Tr12_PCCrit
        _Caculation_Parameters['_Tr12_Source_Via_TF']        =   _Tr12_Source_Via_TF
        _Caculation_Parameters['_Tr12_Drain_Via_TF']         =   _Tr12_Drain_Via_TF
        _Caculation_Parameters['_Tr12_NMOSDummy']            =   _Tr12_NMOSDummy
        _Caculation_Parameters['_Tr12_NMOSDummy_length']     =   _Tr12_NMOSDummy_length
        _Caculation_Parameters['_Tr12_NMOSDummy_placement']  =   _Tr12_NMOSDummy_placement

        _Caculation_Parameters['_Tr3_NMOSNumberofGate']     =   _Tr3_NMOSNumberofGate
        _Caculation_Parameters['_Tr3_NMOSChannelWidth']     =   _Tr3_NMOSChannelWidth
        _Caculation_Parameters['_Tr3_NMOSChannellength']    =   _Tr3_NMOSChannellength
        _Caculation_Parameters['_Tr3_GateSpacing']          =   _Tr3_GateSpacing
        _Caculation_Parameters['_Tr3_SDWidth']              =   _Tr3_SDWidth
        _Caculation_Parameters['_Tr3_XVT']                  =   _Tr3_XVT
        _Caculation_Parameters['_Tr3_PCCrit']               =   _Tr3_PCCrit
        _Caculation_Parameters['_Tr3_Source_Via_TF']        =   _Tr3_Source_Via_TF
        _Caculation_Parameters['_Tr3_Drain_Via_TF']         =   _Tr3_Drain_Via_TF
        _Caculation_Parameters['_Tr3_NMOSDummy']            =   _Tr3_NMOSDummy
        _Caculation_Parameters['_Tr3_NMOSDummy_length']     =   _Tr3_NMOSDummy_length
        _Caculation_Parameters['_Tr3_NMOSDummy_placement']  =   _Tr3_NMOSDummy_placement

        _Caculation_Parameters['_Tr10_NMOSNumberofGate']     =   _Tr10_NMOSNumberofGate
        _Caculation_Parameters['_Tr10_NMOSChannelWidth']     =   _Tr10_NMOSChannelWidth
        _Caculation_Parameters['_Tr10_NMOSChannellength']    =   _Tr10_NMOSChannellength
        _Caculation_Parameters['_Tr10_GateSpacing']          =   _Tr10_GateSpacing
        _Caculation_Parameters['_Tr10_SDWidth']              =   _Tr10_SDWidth
        _Caculation_Parameters['_Tr10_XVT']                  =   _Tr10_XVT
        _Caculation_Parameters['_Tr10_PCCrit']               =   _Tr10_PCCrit
        _Caculation_Parameters['_Tr10_Source_Via_TF']        =   _Tr10_Source_Via_TF
        _Caculation_Parameters['_Tr10_Drain_Via_TF']         =   _Tr10_Drain_Via_TF
        _Caculation_Parameters['_Tr10_NMOSDummy']            =   _Tr10_NMOSDummy
        _Caculation_Parameters['_Tr10_NMOSDummy_length']     =   _Tr10_NMOSDummy_length
        _Caculation_Parameters['_Tr10_NMOSDummy_placement']  =   _Tr10_NMOSDummy_placement

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
        tmp = self.get_param_KJH4('SRF_Tr12Tr3Tr10','SRF_Tr12','BND_NMOS_Drain_Hrz_M2')
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
        tmp1_2 =self.get_param_KJH4('SRF_Tr12Tr3Tr10','SRF_Tr12','BND_NMOS_Drain_Hrz_M2')
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
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        ## Sref ViaX declaration
        self._DesignParameter['SRF_Tr12Tr3Tr10_Drain_ViaM1M2'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(
            _DesignParameter=None,
            _Name='{}:SRF_Tr12Tr3Tr10_Drain_ViaM1M2'.format(_Name)))[0]

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
    libname = 'Proj_RcdacSar_C07_Tr12Tr3Tr10'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'C07_04_Guardring_v0_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

        # Tr12
        _Tr12_NMOSNumberofGate    =   4,     #number
        _Tr12_NMOSChannelWidth    =   500,   #number
        _Tr12_NMOSChannellength   =   30,     #number
        _Tr12_GateSpacing         =   None,   #None/number
        _Tr12_SDWidth             =   None,   #None/number
        _Tr12_XVT                 =   'RVT',  #'XVT' ex)SLVT LVT RVT HVT
        _Tr12_PCCrit              =   True,   #None/True

            # Source_node_ViaM1M2
        _Tr12_Source_Via_TF       =   True,  #True/False

            # Drain_node_ViaM1M2
        _Tr12_Drain_Via_TF        =   True,  #True/False

            # POLY dummy setting
        _Tr12_NMOSDummy           =   True,  # TF
                # if _PMOSDummy == True
        _Tr12_NMOSDummy_length    =   None,  # None/Value
        _Tr12_NMOSDummy_placement =   None,  # None/'Up'/'Dn'/

        # Tr3
        _Tr3_NMOSNumberofGate=2,  # number
        _Tr3_NMOSChannelWidth=400,  # number
        _Tr3_NMOSChannellength=30,  # number
        _Tr3_GateSpacing=None,  # None/number
        _Tr3_SDWidth=None,  # None/number
        _Tr3_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Tr3_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _Tr3_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _Tr3_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _Tr3_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Tr3_NMOSDummy_length=None,  # None/Value
        _Tr3_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr10
        _Tr10_NMOSNumberofGate=8,  # number
        _Tr10_NMOSChannelWidth=700,  # number
        _Tr10_NMOSChannellength=30,  # number
        _Tr10_GateSpacing=None,  # None/number
        _Tr10_SDWidth=None,  # None/number
        _Tr10_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _Tr10_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _Tr10_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _Tr10_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _Tr10_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _Tr10_NMOSDummy_length=None,  # None/Value
        _Tr10_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

        # Tr12Tr3Tr10 Guardring
        _Tr12Tr3Tr10_Guardring_NumCont = 3, #Number
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
