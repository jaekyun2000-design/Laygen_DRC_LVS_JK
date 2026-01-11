from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC_EGFET

import numpy as np
import copy
import math

# from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2
# from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A04_PmosWithDummy_KJH3_YCH_TIA
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_TIA_P1
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_TIA_P2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_TIA_P4


## ########################################################################################################################################################## Class_HEADER
class _TIA_P1P2P4_YCH(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

        # PMOS
        _Tr1_PMOSNumberofGate=45,
        _Tr1_PMOSChannelWidth=6000,
        _Tr1_PMOSChannellength=150,
        _Tr1_GateSpacing	= None,
        _Tr1_SDWidth			= None,
        _Tr1_XVT				= 'EG',
        _Tr1_PCCrit				= None,

        # Source_node_ViaM1M2
        _Tr1_Source_Via_TF = True,

        # Drain_node_ViaM1M2
        _Tr1_Drain_Via_TF = True,

        # POLY dummy setting
        _Tr1_PMOSDummy = True, # TF
        # if _PMOSDummy == True
        _Tr1_PMOSDummy_length = None, # None/Value
        _Tr1_PMOSDummy_placement = None, # None/'Up'/'Dn'/

        # PMOS
        _Tr2_PMOSNumberofGate=None,
        _Tr2_PMOSChannelWidth=None,
        _Tr2_PMOSChannellength=None,
        _Tr2_GateSpacing	= None,
        _Tr2_SDWidth			= None,
        _Tr2_XVT				= None,
        _Tr2_PCCrit				= None,

        # Source_node_ViaM1M2
        _Tr2_Source_Via_TF = None,

        # Drain_node_ViaM1M2
        _Tr2_Drain_Via_TF = None,

        # POLY dummy setting
        _Tr2_PMOSDummy = None, # TF
        # if _PMOSDummy == True
        _Tr2_PMOSDummy_length = None, # None/Value
        _Tr2_PMOSDummy_placement = None, # None/Up/Dn/

        #PMOS
        _Tr4_PMOSNumberofGate	= None,
        _Tr4_PMOSChannelWidth	= None,
        _Tr4_PMOSChannellength	= None,
        _Tr4_GateSpacing		= None,
        _Tr4_SDWidth			= None,
        _Tr4_XVT				= None,
        _Tr4_PCCrit				= None,

        #Source_node_ViaM1M2
        _Tr4_Source_Via_TF = None,

        #Drain_node_ViaM1M2
        _Tr4_Drain_Via_TF = None,

        #POLY dummy setting
        _Tr4_PMOSDummy = None, #TF
            #if _PMOSDummy == True
        _Tr4_PMOSDummy_length = None, #None/Value
        _Tr4_PMOSDummy_placement = None #None/Up/Dn/
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

    ## ################################################################################################################################################ _CalculateDesignParameter
    def _CalculateDesignParameter(self,

                                  # PMOS
                                  _Tr1_PMOSNumberofGate=None,
                                  _Tr1_PMOSChannelWidth=None,
                                  _Tr1_PMOSChannellength=None,
                                  _Tr1_GateSpacing=None,
                                  _Tr1_SDWidth	= None,
                                  _Tr1_XVT			= None,
                                  _Tr1_PCCrit			= None,

                                  # Source_node_ViaM1M2
                                  _Tr1_Source_Via_TF= None,

                                  # Drain_node_ViaM1M2
                                  _Tr1_Drain_Via_TF= None,

                                  # POLY dummy setting
                                  _Tr1_PMOSDummy= None  , # TF
                                  # if _PMOSDummy == True
                                  _Tr1_PMOSDummy_length = None, # None/Value
                                  _Tr1_PMOSDummy_placement = None, # None/Up/Dn/

                                  # PMOS
                                  _Tr2_PMOSNumberofGate=None,
                                  _Tr2_PMOSChannelWidth=None,
                                  _Tr2_PMOSChannellength=None,
                                  _Tr2_GateSpacing=None,
                                  _Tr2_SDWidth	= None,
                                  _Tr2_XVT			= None,
                                  _Tr2_PCCrit			= None,

                                  # Source_node_ViaM1M2
                                  _Tr2_Source_Via_TF= None,

                                  # Drain_node_ViaM1M2
                                  _Tr2_Drain_Via_TF= None,

                                  # POLY dummy setting
                                  _Tr2_PMOSDummy= None  , # TF
                                  # if _PMOSDummy == True
                                  _Tr2_PMOSDummy_length = None, # None/Value
                                  _Tr2_PMOSDummy_placement = None, # None/Up/Dn/

                                  # PMOS
                                  _Tr4_PMOSNumberofGate=None,
                                  _Tr4_PMOSChannelWidth=None,
                                  _Tr4_PMOSChannellength=None,
                                  _Tr4_GateSpacing=None,
                                  _Tr4_SDWidth	= None,
                                  _Tr4_XVT			= None,
                                  _Tr4_PCCrit			= None,

                                  # Source_node_ViaM1M2
                                  _Tr4_Source_Via_TF= None,

                                  # Drain_node_ViaM1M2
                                  _Tr4_Drain_Via_TF= None,

                                  # POLY dummy setting
                                  _Tr4_PMOSDummy= None  , # TF
                                  # if _PMOSDummy == True
                                  _Tr4_PMOSDummy_length = None, # None/Value
                                  _Tr4_PMOSDummy_placement = None, # None/Up/Dn/


                                  ):



        ## ################################################################################################################################# Class_HEADER: Pre Defined Parameter Before Calculation
        # Load DRC library
        _DRCObj = DRC_EGFET.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']


        ## ################################################################################################################################# Calculation_Start
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

        ## SREF Generation Tr4
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A50_TIA_P4._TIA_P4_YCH._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr4_PMOSNumberofGate']     = _Tr4_PMOSNumberofGate
        _Caculation_Parameters['_Tr4_PMOSChannelWidth']     = _Tr4_PMOSChannelWidth
        _Caculation_Parameters['_Tr4_PMOSChannellength']    = _Tr4_PMOSChannellength
        _Caculation_Parameters['_Tr4_GateSpacing']          = _Tr4_GateSpacing
        _Caculation_Parameters['_Tr4_SDWidth']              = _Tr4_SDWidth
        _Caculation_Parameters['_Tr4_XVT']                  = _Tr4_XVT
        _Caculation_Parameters['_Tr4_PCCrit']               = _Tr4_PCCrit
        _Caculation_Parameters['_Tr4_Source_Via_TF']        = _Tr4_Source_Via_TF
        _Caculation_Parameters['_Tr4_Drain_Via_TF']         = _Tr4_Drain_Via_TF
        _Caculation_Parameters['_Tr4_PMOSDummy']            = _Tr4_PMOSDummy
        _Caculation_Parameters['_Tr4_PMOSDummy_length']     = _Tr4_PMOSDummy_length
        _Caculation_Parameters['_Tr4_PMOSDummy_placement']  = _Tr4_PMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Pmos_Tr4'] = self._SrefElementDeclaration(_DesignObj=A50_TIA_P4._TIA_P4_YCH(_DesignParameter=None, _Name='{}:SRF_Pmos_Tr4'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Pmos_Tr4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_Tr4']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_Tr4']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_Tr4']['_XYCoordinates'] = [[0, 0]]


        ## SREF Generation Tr1
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A50_TIA_P1._TIA_P1_YCH._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr1_PMOSNumberofGate'] = _Tr1_PMOSNumberofGate
        _Caculation_Parameters['_Tr1_PMOSChannelWidth'] = _Tr1_PMOSChannelWidth
        _Caculation_Parameters['_Tr1_PMOSChannellength'] = _Tr1_PMOSChannellength
        _Caculation_Parameters['_Tr1_GateSpacing'] = _Tr1_GateSpacing
        _Caculation_Parameters['_Tr1_SDWidth'] = _Tr1_SDWidth
        _Caculation_Parameters['_Tr1_XVT'] = _Tr1_XVT
        _Caculation_Parameters['_Tr1_PCCrit'] = _Tr1_PCCrit
        _Caculation_Parameters['_Tr1_Source_Via_TF'] = _Tr1_Source_Via_TF
        _Caculation_Parameters['_Tr1_Drain_Via_TF'] = _Tr1_Drain_Via_TF
        _Caculation_Parameters['_Tr1_PMOSDummy'] = _Tr1_PMOSDummy
        _Caculation_Parameters['_Tr1_PMOSDummy_length'] = _Tr1_PMOSDummy_length
        _Caculation_Parameters['_Tr1_PMOSDummy_placement'] = _Tr1_PMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Pmos_Tr1'] = self._SrefElementDeclaration(_DesignObj=A50_TIA_P1._TIA_P1_YCH(_DesignParameter=None,_Name='{}:SRF_Pmos_Tr1'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Pmos_Tr1']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_Tr1']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_Tr1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_Tr1']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr4','SRF_Pmos','BND_POLayer')
        target_coord = tmp1[0][0][0][0]['_XY_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Pmos_Tr1','SRF_Pmos','BND_POLayer')
        approaching_coord = tmp2[0][0][-1][0]['_XY_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pmos_Tr1','SRF_Pmos','BND_POLayer')
        Scoord = tmp3[0][0][0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        # print(New_Scoord[0])
        # print(_Tr4_GateSpacing)

        if (_Tr4_GateSpacing == None):
            _Tr4_GateSpacing = _DRCObj._PolygateMinSpace2
            _Tr4_GatetoGate = 2 * _Tr4_GateSpacing + _Tr4_PMOSChannellength
        else :
            _Tr4_GatetoGate = 2 * _Tr4_GateSpacing + _Tr4_PMOSChannellength

        New_Scoord[0] = New_Scoord[0] - _Tr4_GatetoGate
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Pmos_Tr1']['_XYCoordinates'] = tmpXY


        # PP layer 연장 연결
        # Define Boundary_element
        self._DesignParameter['BND_PPLayer_Extension'] = self._BoundaryElementDeclaration(      _Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
                )


        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr4','SRF_Pmos','BND_PPLayer')

        self._DesignParameter['BND_PPLayer_Extension']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr4','SRF_Pmos','BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_Pmos_Tr1','SRF_Pmos','BND_PPLayer')

        self._DesignParameter['BND_PPLayer_Extension']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_right'][0]-tmp2[0][0][0][0]['_XY_left'][0])

        # Define coord
        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['BND_PPLayer_Extension']['_XYCoordinates'] = [[0, 0]]

        # Calculate1
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr4','SRF_Pmos','BND_PPLayer')
        target_coord = tmp1[0][0][0][0]['_XY_up_right']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_PPLayer_Extension')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_PPLayer_Extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['BND_PPLayer_Extension']['_XYCoordinates'] = tmpXY


        ## SREF Generation Tr2
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A50_TIA_P2._TIA_P2_YCH._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr2_PMOSNumberofGate'] = _Tr2_PMOSNumberofGate
        _Caculation_Parameters['_Tr2_PMOSChannelWidth'] = _Tr2_PMOSChannelWidth
        _Caculation_Parameters['_Tr2_PMOSChannellength'] = _Tr2_PMOSChannellength
        _Caculation_Parameters['_Tr2_GateSpacing'] = _Tr2_GateSpacing
        _Caculation_Parameters['_Tr2_SDWidth'] = _Tr2_SDWidth
        _Caculation_Parameters['_Tr2_XVT'] = _Tr2_XVT
        _Caculation_Parameters['_Tr2_PCCrit'] = _Tr2_PCCrit
        _Caculation_Parameters['_Tr2_Source_Via_TF'] = _Tr2_Source_Via_TF
        _Caculation_Parameters['_Tr2_Drain_Via_TF'] = _Tr2_Drain_Via_TF
        _Caculation_Parameters['_Tr2_PMOSDummy'] = _Tr2_PMOSDummy
        _Caculation_Parameters['_Tr2_PMOSDummy_length'] = _Tr2_PMOSDummy_length
        _Caculation_Parameters['_Tr2_PMOSDummy_placement'] = _Tr2_PMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Pmos_Tr2'] = self._SrefElementDeclaration(
            _DesignObj=A50_TIA_P2._TIA_P2_YCH(_DesignParameter=None, _Name='{}:SRF_Pmos_Tr2'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Pmos_Tr2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_Tr2']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_Tr2']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_Tr2']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr4', 'SRF_Pmos', 'BND_POLayer')
        target_coord = tmp1[0][0][-1][0]['_XY_right']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Pmos_Tr2', 'SRF_Pmos', 'BND_POLayer')
        approaching_coord = tmp2[0][0][0][0]['_XY_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pmos_Tr2', 'SRF_Pmos', 'BND_POLayer')
        Scoord = tmp3[0][0][0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)


        if (_Tr4_GateSpacing == None):
            _Tr4_GateSpacing = _DRCObj._PolygateMinSpace2
            _Tr4_GatetoGate = 2 * _Tr4_GateSpacing + _Tr4_PMOSChannellength
        else :
            _Tr4_GatetoGate = 2 * _Tr4_GateSpacing + _Tr4_PMOSChannellength

        New_Scoord[0] = New_Scoord[0] + _Tr4_GatetoGate
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Pmos_Tr2']['_XYCoordinates'] = tmpXY

        # PP layer 연장 연결22
        # Define Boundary_element
        self._DesignParameter['BND_PPLayer_Extension2'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
            )

        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr4', 'SRF_Pmos', 'BND_PPLayer')

        self._DesignParameter['BND_PPLayer_Extension2']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr4', 'SRF_Pmos', 'BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_Pmos_Tr2', 'SRF_Pmos', 'BND_PPLayer')

        self._DesignParameter['BND_PPLayer_Extension2']['_XWidth'] = abs(
            tmp1[0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0]['_XY_right'][0])

        # Define coord
        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['BND_PPLayer_Extension2']['_XYCoordinates'] = [[0, 0]]

        # Calculate1
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr4', 'SRF_Pmos', 'BND_PPLayer')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_PPLayer_Extension2')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_PPLayer_Extension2')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['BND_PPLayer_Extension2']['_XYCoordinates'] = tmpXY


        ## ################################################################################################################################# Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')


## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from TIA_Proj_YCH.Library_and_Engine.Private import MyInfo_YCH
    from TIA_Proj_YCH.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_A51_TIA_P1P2P4_v5'
    cellname = 'A51_TIA_P1P2P4'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

        #PMOS
        _Tr1_PMOSNumberofGate=15,
        _Tr1_PMOSChannelWidth=6000,
        _Tr1_PMOSChannellength=150,
        _Tr1_GateSpacing	= None,
        _Tr1_SDWidth			= None,
        _Tr1_XVT				= 'EG',
        _Tr1_PCCrit				= None,

        # Source_node_ViaM1M2
        _Tr1_Source_Via_TF = True,

        # Drain_node_ViaM1M2
        _Tr1_Drain_Via_TF = True,

        # POLY dummy setting
        _Tr1_PMOSDummy = True, # TF
        # if _PMOSDummy == True
        _Tr1_PMOSDummy_length = None, # None/Value
        _Tr1_PMOSDummy_placement = None, # None/'Up'/'Dn'/

        #PMOS
        _Tr2_PMOSNumberofGate	= 15,
        _Tr2_PMOSChannelWidth	= 6000,
        _Tr2_PMOSChannellength	= 150,
        _Tr2_GateSpacing		= None,
        _Tr2_SDWidth			= None,
        _Tr2_XVT				= 'EG',
        _Tr2_PCCrit				= None,

        #Source_node_ViaM1M2
        _Tr2_Source_Via_TF = True,

        #Drain_node_ViaM1M2
        _Tr2_Drain_Via_TF = True,

        #POLY dummy setting
        _Tr2_PMOSDummy = True, #TF
            #if _PMOSDummy == True
        _Tr2_PMOSDummy_length = None, #None/Value
        _Tr2_PMOSDummy_placement = None, #None/'Up'/'Dn'/

        # PMOS
        _Tr4_PMOSNumberofGate=9,
        _Tr4_PMOSChannelWidth=6000,
        _Tr4_PMOSChannellength=150,
        _Tr4_GateSpacing	= None,
        _Tr4_SDWidth			= None,
        _Tr4_XVT				= 'EG',
        _Tr4_PCCrit				= None,

        # Source_node_ViaM1M2
        _Tr4_Source_Via_TF = True,

        # Drain_node_ViaM1M2
        _Tr4_Drain_Via_TF = True,

        # POLY dummy setting
        _Tr4_PMOSDummy = True, # TF
        # if _PMOSDummy == True
        _Tr4_PMOSDummy_length = None, # None/Value
        _Tr4_PMOSDummy_placement = None, # None/'Up'/'Dn'/

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
    LayoutObj = _TIA_P1P2P4_YCH(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('###############      Sending to FTP Server...      ##################')
    My = MyInfo_YCH.USER(DesignParameters._Technology)
    Checker = DRCchecker_KJH0.DRCchecker_KJH0(
                                                    username=My.ID,
                                                    password=My.PW,
                                                    WorkDir=My.Dir_Work,
                                                    DRCrunDir=My.Dir_DRCrun,
                                                    libname=libname,
                                                    cellname=cellname,
                                                    GDSDir=My.Dir_GDS
                                             )
    #Checker.lib_deletion()
    Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()
    print('#############################      Finished      ################################')
# end of 'main():' ---------------------------------------------------------------------------------------------