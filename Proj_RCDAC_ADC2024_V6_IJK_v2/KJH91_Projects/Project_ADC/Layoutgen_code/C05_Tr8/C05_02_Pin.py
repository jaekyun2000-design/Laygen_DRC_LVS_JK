
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
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A09_NbodyRing_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A10_PbodyRing_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A11_NbodyContactforDeepNwell_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A12_NbodyContactPhyLenforDeepNwell_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A13_NbodyRingforDeepNwell_KJH

    ##
from KJH91_Projects.Project_ADC.Layoutgen_code.C05_Tr8 import C05_00_Tr8
from KJH91_Projects.Project_ADC.Layoutgen_code.C05_Tr8 import C05_01_Guardring


## Define Class
class _Pin(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(

        # Tr8
        _Tr8_NMOSNumberofGate    =   4,     #number
        _Tr8_NMOSChannelWidth    =   500,   #number
        _Tr8_NMOSChannellength   =   30,     #number
        _Tr8_GateSpacing         =   80,   #None/number
        _Tr8_SDWidth             =   None,   #None/number
        _Tr8_XVT                 =   'RVT',  #'XVT' ex)SLVT LVT RVT HVT
        _Tr8_PCCrit              =   True,   #None/True

            # Source_node_ViaM1M2
        _Tr8_Source_Via_TF       =   True,  #True/False

            # Drain_node_ViaM1M2
        _Tr8_Drain_Via_TF        =   True,  #True/False

            # POLY dummy setting
        _Tr8_NMOSDummy           =   True,  # TF
                # if _PMOSDummy == True
        _Tr8_NMOSDummy_length    =   None,  # None/Value
        _Tr8_NMOSDummy_placement =   None,  # None/'Up'/'Dn'/

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

                                  # Tr8
                                  _Tr8_NMOSNumberofGate=4,  # number
                                  _Tr8_NMOSChannelWidth=500,  # number
                                  _Tr8_NMOSChannellength=30,  # number
                                  _Tr8_GateSpacing=80,  # None/number
                                  _Tr8_SDWidth=None,  # None/number
                                  _Tr8_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Tr8_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _Tr8_Source_Via_TF=True,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Tr8_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _Tr8_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tr8_NMOSDummy_length=None,  # None/Value
                                  _Tr8_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

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


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr8, nfettw
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  M4, nfettw: Sref Gen.
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C05_01_Guardring._Guardring._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr8_NMOSNumberofGate']     =   _Tr8_NMOSNumberofGate
        _Caculation_Parameters['_Tr8_NMOSChannelWidth']     =   _Tr8_NMOSChannelWidth
        _Caculation_Parameters['_Tr8_NMOSChannellength']    =   _Tr8_NMOSChannellength
        _Caculation_Parameters['_Tr8_GateSpacing']          =   _Tr8_GateSpacing
        _Caculation_Parameters['_Tr8_SDWidth']              =   _Tr8_SDWidth
        _Caculation_Parameters['_Tr8_XVT']                  =   _Tr8_XVT
        _Caculation_Parameters['_Tr8_PCCrit']               =   _Tr8_PCCrit
        _Caculation_Parameters['_Tr8_Source_Via_TF']        =   _Tr8_Source_Via_TF
        _Caculation_Parameters['_Tr8_Drain_Via_TF']         =   _Tr8_Drain_Via_TF
        _Caculation_Parameters['_Tr8_NMOSDummy']            =   _Tr8_NMOSDummy
        _Caculation_Parameters['_Tr8_NMOSDummy_length']     =   _Tr8_NMOSDummy_length
        _Caculation_Parameters['_Tr8_NMOSDummy_placement']  =   _Tr8_NMOSDummy_placement

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Guardring'] = self._SrefElementDeclaration(_DesignObj=C05_01_Guardring._Guardring(_DesignParameter=None, _Name='{}:SRF_Guardring'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Guardring']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Guardring']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Guardring']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Guardring']['_XYCoordinates'] = [[0, 0]]


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Gate: M2
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Gate: M2 metal Gen.
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
        tmp = self.get_param_KJH4('SRF_Guardring','SRF_Tr8','BND_NMOS_Gate_Hrz_poly')
        self._DesignParameter['BND_Gate_Hrz_M2']['_YWidth'] = tmp[0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Guardring','SRF_Tr8','BND_NMOS_Gate_Hrz_poly')
        self._DesignParameter['BND_Gate_Hrz_M2']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Gate_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Gate_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Guardring','SRF_Tr8','BND_NMOS_Gate_Hrz_poly')
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Gate: M2 metal Gen.
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
        tmp2 = self.get_param_KJH4('SRF_Guardring','SRF_Tr8','BND_NMOS_Gate_Hrz_poly')
        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0][0][0])

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

            ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = max(2,_COX)
        _Caculation_Parameters['_COY'] = max(1,_COY)

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
        tmp2 = self.get_param_KJH4('SRF_Gate_ViaM0M2','SRF_ViaM1M2','BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Gate_ViaM0M2')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Gate_ViaM0M2']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Source: M3
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Source: M3 metal Gen.
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
        tmp = self.get_param_KJH4('SRF_Guardring','SRF_Tr8','BND_NMOS_Source_Hrz_M2')
        self._DesignParameter['BND_Source_Hrz_M3']['_YWidth'] = tmp[0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Guardring','SRF_Tr8','BND_NMOS_Source_Hrz_M2')
        self._DesignParameter['BND_Source_Hrz_M3']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Source_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Source_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Guardring','SRF_Tr8','BND_NMOS_Source_Hrz_M2')
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
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
        tmp2 = self.get_param_KJH4('SRF_Guardring','SRF_Tr8','BND_NMOS_Source_Hrz_M2')
        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0][0][0])

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

            ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Drain: M4
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Drain: M4 metal Gen.
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Drain_Hrz_M4'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL4'][0],
        _Datatype=DesignParameters._LayerMapping['METAL4'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('SRF_Guardring','SRF_Tr8','BND_NMOS_Drain_Hrz_M2')
        self._DesignParameter['BND_Drain_Hrz_M4']['_YWidth'] = tmp[0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Guardring','SRF_Tr8','BND_NMOS_Drain_Hrz_M2')
        self._DesignParameter['BND_Drain_Hrz_M4']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Drain_Hrz_M4']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Drain_Hrz_M4']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Guardring','SRF_Tr8','BND_NMOS_Drain_Hrz_M2')
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Drain_Hrz_M4')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Drain_Hrz_M4')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Drain_Hrz_M4']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Source: ViaM2M3 Gen.
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Drain_ViaM2M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None, _Name='{}:SRF_Drain_ViaM2M4'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Drain_ViaM2M4']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Drain_ViaM2M4']['_Angle'] = 0

            ## Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH4('BND_Drain_Hrz_M4')
        tmp2 = self.get_param_KJH4('SRF_Guardring','SRF_Tr8','BND_NMOS_Drain_Hrz_M2')
        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0][0][0])

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

        ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = max(_COX, 2)
        _Caculation_Parameters['_COY'] = max(_COY, 1)

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Drain_ViaM2M4']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Drain_ViaM2M4']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        tmp1 = self.get_param_KJH4('BND_Drain_Hrz_M4')
        target_coord = tmp1[0][0]['_XY_cent']
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Drain_ViaM2M4','SRF_ViaM3M4','BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Drain_ViaM2M4')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Drain_ViaM2M4']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Guardring: Pbody2
        ## Guardring
        ## Pre-defined DRC
        _right_margin = 550
        _left_margin = 550
        _up_margin = 550
        _down_margin = 550

        _NumCont = 3

        ## Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A10_PbodyRing_KJH2._PbodyRing_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_XlengthIntn'] = None
        _Caculation_Parameters['_YlengthIntn'] = None
        _Caculation_Parameters['_NumContTop'] = _NumCont
        _Caculation_Parameters['_NumContBottom'] = _NumCont
        _Caculation_Parameters['_NumContLeft'] = _NumCont
        _Caculation_Parameters['_NumContRight'] = _NumCont

        ## Find Outter boundary
        tmp = self.get_outter_KJH4('SRF_Guardring')

        ## Define _XlengthIntn
        _Caculation_Parameters['_XlengthIntn'] = abs( tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0]) + _right_margin + _left_margin

        ## Define _YlengthIntn
        _Caculation_Parameters['_YlengthIntn'] = abs( tmp['_Mostup']['coord'][0] - tmp['_Mostdown']['coord'][0]) + _up_margin + _down_margin

        ## Generate Sref
        self._DesignParameter['SRF_Pbodyring2'] = self._SrefElementDeclaration(
            _DesignObj=A10_PbodyRing_KJH2._PbodyRing_KJH2(_DesignParameter=None,
            _Name='{}:SRF_Pbodyring2'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_Pbodyring2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_Pbodyring2']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_Pbodyring2']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate
        self._DesignParameter['SRF_Pbodyring2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_Pbodyring2']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        target_coord = [tmp['_Mostleft']['coord'][0], tmp['_Mostdown']['coord'][0]]
        ## Approaching_coord
        ## x
        tmp2_1 = self.get_param_KJH4('SRF_Pbodyring2', 'SRF_PbodyLeft', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coordx = tmp2_1[0][0][0][0][0]['_XY_right'][0]
        ## y
        tmp2_2 = self.get_param_KJH4('SRF_Pbodyring2', 'SRF_PbodyBottom', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coordy = tmp2_2[0][0][0][0][0]['_XY_up'][1]

        approaching_coord = [approaching_coordx, approaching_coordy]
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pbodyring2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] - _left_margin
        New_Scoord[1] = New_Scoord[1] - _down_margin
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_Pbodyring2']['_XYCoordinates'] = tmpXY


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
    libname = 'Proj_ZZ00_RcdacSar_C05_Tr8'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'C05_02_Pin_v0_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

        # Tr8
        _Tr8_NMOSNumberofGate    =   10,     #number (ref:4)
        _Tr8_NMOSChannelWidth    =   1000,   #number (ref:500)
        _Tr8_NMOSChannellength   =   30,     #number (ref:30)
        _Tr8_GateSpacing         =   None,   #None/number
        _Tr8_SDWidth             =   None,   #None/number
        _Tr8_XVT                 =   'RVT',  #'XVT' ex)SLVT LVT RVT HVT
        _Tr8_PCCrit              =   True,   #None/True

            # Source_node_ViaM1M2
        _Tr8_Source_Via_TF       =   True,  #True/False

            # Drain_node_ViaM1M2
        _Tr8_Drain_Via_TF        =   True,  #True/False

            # POLY dummy setting
        _Tr8_NMOSDummy           =   True,  # TF
                # if _PMOSDummy == True
        _Tr8_NMOSDummy_length    =   None,  # None/Value
        _Tr8_NMOSDummy_placement =   None,  # None/'Up'/'Dn'/

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
    LayoutObj = _Pin(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    # testStreamFile = open('./gdsfile/{}'.format(_fileName), 'wb')
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
