
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
from KJH91_Projects.Project_ADC.Layoutgen_code.C02_Tr5Tr7Tr9_Ctop_KJH import C02_00_Tr5
from KJH91_Projects.Project_ADC.Layoutgen_code.C02_Tr5Tr7Tr9_Ctop_KJH import C02_01_Tr7
from KJH91_Projects.Project_ADC.Layoutgen_code.C02_Tr5Tr7Tr9_Ctop_KJH import C02_02_Tr9


## Define Class
class _Tr5Tr7Tr9(StickDiagram_KJH1._StickDiagram_KJH):

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
        _Caculation_Parameters = copy.deepcopy(C02_00_Tr5._Tr5._ParametersForDesignCalculation)
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

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Tr5'] = self._SrefElementDeclaration(_DesignObj=C02_00_Tr5._Tr5(_DesignParameter=None, _Name='{}:SRF_Tr5'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Tr5']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr5']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr5']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr5']['_XYCoordinates'] = [[0, 0]]


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr7, slvtpfet+np
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr7, slvtpfet+np: SRF gen.
            ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C02_01_Tr7._Tr7._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
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

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Tr7'] = self._SrefElementDeclaration(_DesignObj=C02_01_Tr7._Tr7(_DesignParameter=None, _Name='{}:SRF_Tr7'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Tr7']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr7']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr7']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr7']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Tr7']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##x
        tmp1_1 = self.get_param_KJH4('SRF_Tr5','SRF_Pmos','BND_PODummyLayer')
        target_coordx = tmp1_1[0][0][-1][0]['_XY_right'][0]
                                ##y
        tmp1_2 = self.get_param_KJH4('SRF_Tr5','BND_Pmos_Gate_Hrz_poly')
        target_coordy = tmp1_2[0][0][0]['_XY_up'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##x
        tmp2_1 = self.get_param_KJH4('SRF_Tr7','SRF_Pmos','BND_PODummyLayer')
        approaching_coordx = tmp2_1[0][0][0][0]['_XY_left'][0]
                                ##y
        tmp2_2 = self.get_param_KJH4('SRF_Tr7','BND_Pmos_Gate_Hrz_poly')
        approaching_coordy = tmp2_2[0][0][0]['_XY_up'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Tr7')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] + _DRCobj._PolygateMinSpace2 + 30 #30 for slvtlayer DRC
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Tr7']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr9, rvtpfet+np
            ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C02_02_Tr9._Tr9._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
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
        self._DesignParameter['SRF_Tr9'] = self._SrefElementDeclaration(_DesignObj=C02_02_Tr9._Tr9(_DesignParameter=None, _Name='{}:SRF_Tr9'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Tr9']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr9']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr9']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr9']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Tr9']['_XYCoordinates'] = [[0, 0]]

                            ## Calculate
                                ## Target_coord: _XY_type1
                                    ##x
        tmp1_1 = self.get_param_KJH4('SRF_Tr7','SRF_Pmos','BND_PODummyLayer')
        target_coordx = tmp1_1[0][0][-1][0]['_XY_right'][0]
                                    ##y
        tmp1_2 = self.get_param_KJH4('SRF_Tr7', 'BND_Pmos_Source_Hrz_M2')
        target_coordy = tmp1_2[0][0][0]['_XY_down'][1]

        target_coord = [target_coordx, target_coordy]
                                ## Approaching_coord: _XY_type2
                                    ##x
        tmp2_1 = self.get_param_KJH4('SRF_Tr9','SRF_Pmos','BND_PODummyLayer')
        approaching_coordx = tmp2_1[0][0][0][0]['_XY_left'][0]
                                    ##y
        tmp2_2 = self.get_param_KJH4('SRF_Tr9', 'BND_Pmos_Gate_Hrz_poly')
        approaching_coordy = tmp2_2[0][0][0]['_XY_down'][1]

        approaching_coord = [approaching_coordx,approaching_coordy]
                                ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Tr9')
        Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] + _DRCobj._PolygateMinSpace2 + 30  # 30 for slvtlayer DRC
        tmpXY.append(New_Scoord)
                                ## Define Coordinates
        self._DesignParameter['SRF_Tr9']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr5Tr7Tr9, BP covering
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PPcovering'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['PIMP'][0],
        _Datatype=DesignParameters._LayerMapping['PIMP'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Tr5','SRF_Pmos','BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_Tr7','SRF_Pmos','BND_PPLayer')
        tmp3 = self.get_param_KJH4('SRF_Tr9','SRF_Pmos','BND_PPLayer')

        ymax = max(tmp1[0][0][0][0]['_XY_up'][1],tmp2[0][0][0][0]['_XY_up'][1],tmp3[0][0][0][0]['_XY_up'][1])
        ymin = min(tmp1[0][0][0][0]['_XY_down'][1], tmp2[0][0][0][0]['_XY_down'][1], tmp3[0][0][0][0]['_XY_down'][1])

        self._DesignParameter['BND_PPcovering']['_YWidth'] = abs(ymax-ymin)

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Tr5','SRF_Pmos','BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_Tr9','SRF_Pmos','BND_PPLayer')
        self._DesignParameter['BND_PPcovering']['_XWidth'] = abs( tmp2[0][0][0][0]['_XY_right'][0] - tmp1[0][0][0][0]['_XY_left'][0] )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PPcovering']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_PPcovering']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ## coordx
        tmp1 = self.get_param_KJH4('SRF_Tr5','SRF_Pmos','BND_PPLayer')
        target_coordx = tmp1[0][0][0][0]['_XY_left'][0]
                                ## coordy
        target_coordy = ymin
        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PPcovering')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PPcovering')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_PPcovering']['_XYCoordinates'] = tmpXY




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
    libname = 'Proj_ADC_C02_Tr5Tr7Tr9_KJH'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'C02_03_Tr5Tr7Tr9_v0_97'
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
    LayoutObj = _Tr5Tr7Tr9(_DesignParameter=None, _Name=cellname)
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
