
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
from Proj_RCDAC_ADC2024_V6_IJK.KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A14_Mosfet_KJH3

    ## KJH91 Basic Building Blocks
# from KJH91_Projects.Project_ADC.Layoutgen_code.C07_Tr12Tr3Tr10_Fixed import C07_00_Tr12
# from KJH91_Projects.Project_ADC.Layoutgen_code.C07_Tr12Tr3Tr10_Fixed import C07_01_Tr3
# from KJH91_Projects.Project_ADC.Layoutgen_code.C07_Tr12Tr3Tr10_Fixed import C07_02_Tr10

## Define Class
class _Tr12Tr3Tr10(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
# TR12
    # Physical dimension
    _Tr12_NumberofGate	            = 4,       # Number
    _Tr12_ChannelWidth	            = 500,     # Number
    _Tr12_ChannelLength	            = 30,       # Number
    _Tr12_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
# TR3
    # Physical dimension
    _Tr3_NumberofGate	            = 2,       # Number
    _Tr3_ChannelWidth	            = 400,     # Number
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
    _Tr12_ChannelWidth	            = 500,     # Number
    _Tr12_ChannelLength	            = 30,       # Number
    _Tr12_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
# TR3
    # Physical dimension
    _Tr3_NumberofGate	            = 2,       # Number
    _Tr3_ChannelWidth	            = 400,     # Number
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
        start_time = time.time()
        # end_time = time.time()
        # self.elapsed_time = end_time - start_time
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

        ## Pre-defined
        Drain_Length = 100
        Gate_Length = 200

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr12, nfet
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A14_Mosfet_KJH3._Mosfet._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_MosType'] = 'NMOS'
        _Caculation_Parameters['_MosUpDn'] = 'Up'

        _Caculation_Parameters['_NumberofGate']     = _Tr12_NumberofGate
        _Caculation_Parameters['_ChannelWidth']     = _Tr12_ChannelWidth
        _Caculation_Parameters['_ChannelLength']    = _Tr12_ChannelLength
        _Caculation_Parameters['_GateSpacing']      = None
        _Caculation_Parameters['_SDWidth']          = None
        _Caculation_Parameters['_XVT']              = _Tr12_XVT
        _Caculation_Parameters['_PCCrit']           = True

        _Caculation_Parameters['_Source_Via_TF']                = True
        _Caculation_Parameters['_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_Source_Comb_TF']               = True
        _Caculation_Parameters['_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_Source_Comb_Length']           = None

        _Caculation_Parameters['_Drain_Via_TF']                 = True
        _Caculation_Parameters['_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_Drain_Comb_TF']                = True
        _Caculation_Parameters['_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_Drain_Comb_Length']            = Drain_Length

        _Caculation_Parameters['_PODummy_TF']                   = True
        _Caculation_Parameters['_PODummy_Length']               = None
        _Caculation_Parameters['_PODummy_Placement']            = 'Up'

        _Caculation_Parameters['_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_POGate_Comb_TF']               = True
        _Caculation_Parameters['_POGate_Comb_length']           = Gate_Length
        _Caculation_Parameters['_POGate_Via_TF']                = True
        _Caculation_Parameters['_POGate_ViaMxMx']               = [0,2]

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Tr12'] = self._SrefElementDeclaration(_DesignObj=A14_Mosfet_KJH3._Mosfet(_DesignParameter=None, _Name='{}:SRF_Tr12'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Tr12']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr12']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr12']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr12']['_XYCoordinates'] = [[0, 0]]


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr3, nfet
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A14_Mosfet_KJH3._Mosfet._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_MosType'] = 'NMOS'
        _Caculation_Parameters['_MosUpDn'] = 'Up'

        _Caculation_Parameters['_NumberofGate']     = _Tr3_NumberofGate
        _Caculation_Parameters['_ChannelWidth']     = _Tr3_ChannelWidth
        _Caculation_Parameters['_ChannelLength']    = _Tr3_ChannelLength
        _Caculation_Parameters['_GateSpacing']      = None
        _Caculation_Parameters['_SDWidth']          = None
        _Caculation_Parameters['_XVT']              = _Tr3_XVT
        _Caculation_Parameters['_PCCrit']           = True

        _Caculation_Parameters['_Source_Via_TF']                = True
        _Caculation_Parameters['_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_Source_Comb_TF']               = True
        _Caculation_Parameters['_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_Source_Comb_Length']           = None

        _Caculation_Parameters['_Drain_Via_TF']                 = True
        _Caculation_Parameters['_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_Drain_Comb_TF']                = True
        _Caculation_Parameters['_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PODummy_TF']                   = True
        _Caculation_Parameters['_PODummy_Length']               = None
        _Caculation_Parameters['_PODummy_Placement']            = 'Up'

        _Caculation_Parameters['_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_POGate_Comb_TF']               = True
        _Caculation_Parameters['_POGate_Comb_length']           = Gate_Length
        _Caculation_Parameters['_POGate_Via_TF']                = True
        _Caculation_Parameters['_POGate_ViaMxMx']               = [0,2]


        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Tr3'] = self._SrefElementDeclaration(_DesignObj=A14_Mosfet_KJH3._Mosfet(_DesignParameter=None, _Name='{}:SRF_Tr3'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Tr3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr3']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr3']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr3']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Tr3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Tr12','BND_PODummyLayer')
        target_coord = tmp1[0][-1][0]['_XY_up_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_Tr3','BND_PODummyLayer')
        approaching_coord = tmp2[0][0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Tr3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] + _DRCobj._XvtMinSpace
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Tr3']['_XYCoordinates'] = tmpXY

        ## Cal Drain comb length
        tmp1 = self.get_param_KJH4('SRF_Tr12','BND_Drain_Vtc_M2')
        tmp2 = self.get_param_KJH4('SRF_Tr3','BND_Drain_Vtc_M2')
        Drain_length1 = tmp1[0][0][0]['_XY_up'][1] - tmp2[0][0][0]['_XY_down'][1]
        _Caculation_Parameters['_Drain_Comb_Length'] = Drain_length1

        del self._DesignParameter['SRF_Tr3']

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Tr3'] = self._SrefElementDeclaration(_DesignObj=A14_Mosfet_KJH3._Mosfet(_DesignParameter=None, _Name='{}:SRF_Tr3'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Tr3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr3']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr3']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr3']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Tr3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Tr12','BND_PODummyLayer')
        target_coord = tmp1[0][-1][0]['_XY_up_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_Tr3','BND_PODummyLayer')
        approaching_coord = tmp2[0][0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Tr3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] + _DRCobj._XvtMinSpace
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Tr3']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr10, nfet
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A14_Mosfet_KJH3._Mosfet._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_MosType'] = 'NMOS'
        _Caculation_Parameters['_MosUpDn'] = 'Up'

        _Caculation_Parameters['_NumberofGate']     = _Tr10_NumberofGate
        _Caculation_Parameters['_ChannelWidth']     = _Tr10_ChannelWidth
        _Caculation_Parameters['_ChannelLength']    = _Tr10_ChannelLength
        _Caculation_Parameters['_GateSpacing']      = None
        _Caculation_Parameters['_SDWidth']          = None
        _Caculation_Parameters['_XVT']              = _Tr10_XVT
        _Caculation_Parameters['_PCCrit']           = True

        _Caculation_Parameters['_Source_Via_TF']                = True
        _Caculation_Parameters['_Source_Via_Close2POpin_TF']    = False
        _Caculation_Parameters['_Source_Comb_TF']               = True
        _Caculation_Parameters['_Source_Comb_POpinward_TF']     = False
        _Caculation_Parameters['_Source_Comb_Length']           = None

        _Caculation_Parameters['_Drain_Via_TF']                 = True
        _Caculation_Parameters['_Drain_Via_Close2POpin_TF']     = True
        _Caculation_Parameters['_Drain_Comb_TF']                = True
        _Caculation_Parameters['_Drain_Comb_POpinward_TF']      = True
        _Caculation_Parameters['_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PODummy_TF']                   = True
        _Caculation_Parameters['_PODummy_Length']               = None
        _Caculation_Parameters['_PODummy_Placement']            = 'Up'

        _Caculation_Parameters['_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_POGate_Comb_TF']               = True
        _Caculation_Parameters['_POGate_Comb_length']           = Gate_Length
        _Caculation_Parameters['_POGate_Via_TF']                = True
        _Caculation_Parameters['_POGate_ViaMxMx']               = [0,2]

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Tr10'] = self._SrefElementDeclaration(_DesignObj=A14_Mosfet_KJH3._Mosfet(_DesignParameter=None, _Name='{}:SRF_Tr10'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Tr10']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr10']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr10']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr10']['_XYCoordinates'] = [[0, 0]]

        ## Get_Scoord_v4.
        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_Tr10']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Tr3', 'BND_PODummyLayer')
        target_coord = tmp1[0][-1][0]['_XY_up_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_Tr10','BND_PODummyLayer')
        approaching_coord = tmp2[0][0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Tr10')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] + _DRCobj._XvtMinSpace
        tmpXY.append(New_Scoord)
        ## Define Coordinates
        self._DesignParameter['SRF_Tr10']['_XYCoordinates'] = tmpXY

        ## Cal Drain comb length
        tmp1 = self.get_param_KJH4('SRF_Tr12','BND_Drain_Vtc_M2')
        tmp2 = self.get_param_KJH4('SRF_Tr10','BND_Drain_Vtc_M2')
        Drain_length1 = tmp1[0][0][0]['_XY_up'][1] - tmp2[0][0][0]['_XY_down'][1]
        _Caculation_Parameters['_Drain_Comb_Length'] = Drain_length1

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Tr10'] = self._SrefElementDeclaration(_DesignObj=A14_Mosfet_KJH3._Mosfet(_DesignParameter=None, _Name='{}:SRF_Tr10'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Tr10']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr10']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr10']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr10']['_XYCoordinates'] = [[0, 0]]

        ## Get_Scoord_v4.
        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_Tr10']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Tr3', 'BND_PODummyLayer')
        target_coord = tmp1[0][-1][0]['_XY_up_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_Tr10','BND_PODummyLayer')
        approaching_coord = tmp2[0][0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Tr10')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] + _DRCobj._XvtMinSpace
        tmpXY.append(New_Scoord)
        ## Define Coordinates
        self._DesignParameter['SRF_Tr10']['_XYCoordinates'] = tmpXY


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
    libname = 'Proj_ZZ01_C07_03_Tr12Tr3Tr10_Fixed'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'C07_03_Tr12Tr3Tr10_v0_84'
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
    LayoutObj = _Tr12Tr3Tr10(_DesignParameter=None, _Name=cellname)
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
