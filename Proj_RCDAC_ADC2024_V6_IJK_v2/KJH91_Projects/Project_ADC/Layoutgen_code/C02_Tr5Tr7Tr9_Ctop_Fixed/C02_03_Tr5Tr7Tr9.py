
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
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A07_NbodyContactPhyLen_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A08_PbodyContactPhyLen_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A09_NbodyRing_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A10_PbodyRing_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A11_NbodyContactforDeepNwell_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A12_NbodyContactPhyLenforDeepNwell_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A13_NbodyRingforDeepNwell_KJH
from Proj_RCDAC_ADC2024_V6_IJK.KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A14_Mosfet_KJH3

    ##


## Define Class
class _Tr5Tr7Tr9(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
# TR5
    # Physical dimension
    _Tr5_NumberofGate	            = 1,       # Number
    _Tr5_ChannelWidth	            = 1000,     # Number
    _Tr5_ChannelLength	            = 30,       # Number
    _Tr5_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR7
    # Physical dimension
    _Tr7_NumberofGate               = 1,  # Number
    _Tr7_ChannelWidth	            = 100,     # Number
    _Tr7_ChannelLength	            = 30,       # Number
    _Tr7_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR9
        # Physical dimension
        _Tr9_NumberofGate=3,  # Number
        _Tr9_ChannelWidth	= 500,     # Number
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
    _Tr5_NumberofGate	            = 1,       # Number
    _Tr5_ChannelWidth	            = 1000,     # Number
    _Tr5_ChannelLength	            = 30,       # Number
    _Tr5_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR7
    # Physical dimension
    _Tr7_NumberofGate               = 1,  # Number
    _Tr7_ChannelWidth	            = 100,     # Number
    _Tr7_ChannelLength	            = 30,       # Number
    _Tr7_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR9
    # Physical dimension
    _Tr9_NumberofGate=3,  # Number
    _Tr9_ChannelWidth	= 500,     # Number
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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr5, slvtpfet+np
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr5, slvtpfet+np: Sref Gen
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A14_Mosfet_KJH3._Mosfet._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_MosType'] = 'PMOS'
        _Caculation_Parameters['_MosUpDn'] = 'Up'

        _Caculation_Parameters['_NumberofGate'] = _Tr5_NumberofGate
        _Caculation_Parameters['_ChannelWidth'] = _Tr5_ChannelWidth
        _Caculation_Parameters['_ChannelLength'] = _Tr5_ChannelLength
        _Caculation_Parameters['_GateSpacing'] = None
        _Caculation_Parameters['_SDWidth'] = None
        _Caculation_Parameters['_XVT'] = _Tr5_XVT
        _Caculation_Parameters['_PCCrit'] = True

        _Caculation_Parameters['_Source_Via_TF'] = False
        _Caculation_Parameters['_Source_Via_Close2POpin_TF'] = None
        _Caculation_Parameters['_Source_Comb_TF'] = None
        _Caculation_Parameters['_Source_Comb_POpinward_TF'] = None
        _Caculation_Parameters['_Source_Comb_Length'] = None

        _Caculation_Parameters['_Drain_Via_TF'] = True
        _Caculation_Parameters['_Drain_Via_Close2POpin_TF'] = False
        _Caculation_Parameters['_Drain_Comb_TF'] = True
        _Caculation_Parameters['_Drain_Comb_POpinward_TF'] = False
        _Caculation_Parameters['_Drain_Comb_Length'] = None

        _Caculation_Parameters['_PODummy_TF'] = True
        _Caculation_Parameters['_PODummy_Length'] = None
        _Caculation_Parameters['_PODummy_Placement'] = 'Up'

        _Caculation_Parameters['_Xvt_MinExten_TF'] = True
        _Caculation_Parameters['_Xvt_Placement'] = 'Dn'

        _Caculation_Parameters['_POGate_Comb_TF'] = True
        _Caculation_Parameters['_POGate_Comb_length'] = None
        _Caculation_Parameters['_POGate_Via_TF'] = True
        _Caculation_Parameters['_POGate_ViaMxMx'] = [0,3]

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Tr5'] = self._SrefElementDeclaration(_DesignObj=A14_Mosfet_KJH3._Mosfet(_DesignParameter=None, _Name='{}:SRF_Tr5'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Tr5']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr5']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr5']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr5']['_XYCoordinates'] = [[0, 0]]

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr7,
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr7: Sref Gen
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A14_Mosfet_KJH3._Mosfet._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_MosType'] = 'PMOS'
        _Caculation_Parameters['_MosUpDn'] = 'Up'

        _Caculation_Parameters['_NumberofGate'] = _Tr7_NumberofGate
        _Caculation_Parameters['_ChannelWidth'] = _Tr7_ChannelWidth
        _Caculation_Parameters['_ChannelLength'] = _Tr7_ChannelLength
        _Caculation_Parameters['_GateSpacing'] = None
        _Caculation_Parameters['_SDWidth'] = None
        _Caculation_Parameters['_XVT'] = _Tr7_XVT
        _Caculation_Parameters['_PCCrit'] = True

        _Caculation_Parameters['_Source_Via_TF'] = True
        _Caculation_Parameters['_Source_Via_Close2POpin_TF'] = False
        _Caculation_Parameters['_Source_Comb_TF'] = True
        _Caculation_Parameters['_Source_Comb_POpinward_TF'] = False
        _Caculation_Parameters['_Source_Comb_Length'] = None

        _Caculation_Parameters['_Drain_Via_TF'] = False
        _Caculation_Parameters['_Drain_Via_Close2POpin_TF'] = None
        _Caculation_Parameters['_Drain_Comb_TF'] = None
        _Caculation_Parameters['_Drain_Comb_POpinward_TF'] = None
        _Caculation_Parameters['_Drain_Comb_Length'] = None

        _Caculation_Parameters['_PODummy_TF'] = True
        _Caculation_Parameters['_PODummy_Length'] = None
        _Caculation_Parameters['_PODummy_Placement'] = 'Up'

        _Caculation_Parameters['_Xvt_MinExten_TF'] = True
        _Caculation_Parameters['_Xvt_Placement'] = 'Dn'

        _Caculation_Parameters['_POGate_Comb_TF'] = True
        _Caculation_Parameters['_POGate_Comb_length'] = None
        _Caculation_Parameters['_POGate_Via_TF'] = True
        _Caculation_Parameters['_POGate_ViaMxMx'] = [0,3]

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Tr7'] = self._SrefElementDeclaration(_DesignObj=A14_Mosfet_KJH3._Mosfet(_DesignParameter=None, _Name='{}:SRF_Tr7'.format(_Name)))[0]

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
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##x
        tmp1_1 = self.get_param_KJH4('SRF_Tr5','BND_PODummyLayer')
        target_coordx = tmp1_1[0][-1][0]['_XY_right'][0]
                                ##y
        tmp1_2 = self.get_param_KJH4('SRF_Tr5','BND_Gate_Hrz_poly')
        target_coordy = tmp1_2[0][0][0]['_XY_up'][1]

        target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
                                ##x
        tmp2_1 = self.get_param_KJH4('SRF_Tr7','BND_PODummyLayer')
        approaching_coordx = tmp2_1[0][0][0]['_XY_left'][0]
                                ##y
        tmp2_2 = self.get_param_KJH4('SRF_Tr7','BND_Gate_Hrz_poly')
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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr9,
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr9: Sref Gen
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A14_Mosfet_KJH3._Mosfet._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_MosType'] = 'PMOS'
        _Caculation_Parameters['_MosUpDn'] = 'Dn'

        _Caculation_Parameters['_NumberofGate'] = _Tr9_NumberofGate
        _Caculation_Parameters['_ChannelWidth'] = _Tr9_ChannelWidth
        _Caculation_Parameters['_ChannelLength'] = _Tr9_ChannelLength
        _Caculation_Parameters['_GateSpacing'] = None
        _Caculation_Parameters['_SDWidth'] = None
        _Caculation_Parameters['_XVT'] = _Tr9_XVT
        _Caculation_Parameters['_PCCrit'] = True

        _Caculation_Parameters['_Source_Via_TF'] = False
        _Caculation_Parameters['_Source_Via_Close2POpin_TF'] = None
        _Caculation_Parameters['_Source_Comb_TF'] = None
        _Caculation_Parameters['_Source_Comb_POpinward_TF'] = False
        _Caculation_Parameters['_Source_Comb_Length'] = None

        _Caculation_Parameters['_Drain_Via_TF'] = True
        _Caculation_Parameters['_Drain_Via_Close2POpin_TF'] = False
        _Caculation_Parameters['_Drain_Comb_TF'] = True
        _Caculation_Parameters['_Drain_Comb_POpinward_TF'] = False
        _Caculation_Parameters['_Drain_Comb_Length'] = _Tr9_ChannelWidth + 100

        _Caculation_Parameters['_PODummy_TF'] = True
        _Caculation_Parameters['_PODummy_Length'] = None
        _Caculation_Parameters['_PODummy_Placement'] = 'Dn'

        _Caculation_Parameters['_Xvt_MinExten_TF'] = True
        _Caculation_Parameters['_Xvt_Placement'] = 'Up'

        _Caculation_Parameters['_POGate_Comb_TF'] = True
        _Caculation_Parameters['_POGate_Comb_length'] = None
        _Caculation_Parameters['_POGate_Via_TF'] = True
        _Caculation_Parameters['_POGate_ViaMxMx'] = [0,2]

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Tr9'] = self._SrefElementDeclaration(_DesignObj=A14_Mosfet_KJH3._Mosfet(_DesignParameter=None, _Name='{}:SRF_Tr9'.format(_Name)))[0]

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
                            ## Calculate
                                ## Target_coord: _XY_type1
                                    ##x
        tmp1_1 = self.get_param_KJH4('SRF_Tr7','BND_PODummyLayer')
        target_coordx = tmp1_1[0][-1][0]['_XY_right'][0]
                                    ##y
        tmp1_2 = self.get_param_KJH4('SRF_Tr7', 'BND_Source_Hrz_M2')
        target_coordy = tmp1_2[0][0][0]['_XY_down'][1]

        target_coord = [target_coordx, target_coordy]
                                ## Approaching_coord: _XY_type2
                                    ##x
        tmp2_1 = self.get_param_KJH4('SRF_Tr9','BND_PODummyLayer')
        approaching_coordx = tmp2_1[0][0][0]['_XY_left'][0]
                                    ##y
        tmp2_2 = self.get_param_KJH4('SRF_Tr9', 'BND_Gate_Hrz_poly')
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
        tmp1 = self.get_param_KJH4('SRF_Tr5','BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_Tr7','BND_PPLayer')
        tmp3 = self.get_param_KJH4('SRF_Tr9','BND_PPLayer')

        ymax = max(tmp1[0][0][0]['_XY_up'][1],tmp2[0][0][0]['_XY_up'][1],tmp3[0][0][0]['_XY_up'][1])
        ymin = min(tmp1[0][0][0]['_XY_down'][1], tmp2[0][0][0]['_XY_down'][1], tmp3[0][0][0]['_XY_down'][1])

        self._DesignParameter['BND_PPcovering']['_YWidth'] = abs(ymax-ymin)

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Tr5','BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_Tr9','BND_PPLayer')
        self._DesignParameter['BND_PPcovering']['_XWidth'] = abs( tmp2[0][0][0]['_XY_right'][0] - tmp1[0][0][0]['_XY_left'][0] )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PPcovering']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_PPcovering']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ## coordx
        tmp1 = self.get_param_KJH4('SRF_Tr5','BND_PPLayer')
        target_coordx = tmp1[0][0][0]['_XY_left'][0]
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
    libname = 'Proj_ZZ01_C02_03_Tr5Tr7Tr9_Fixed'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'C02_03_Tr5Tr7Tr9_v0_99'
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
    LayoutObj = _Tr5Tr7Tr9(_DesignParameter=None, _Name=cellname)
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
    # Checker.lib_deletion()
    Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()

    print('#############################      Finished      ################################')
    print('{} Hours   {} minutes   {} seconds'.format(h, m, s))

# end of 'main():' ---------------------------------------------------------------------------------------------
