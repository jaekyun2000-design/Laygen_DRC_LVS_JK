from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC_EGFET

import numpy as np
import copy
import math

from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A51_Runit_Switch
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A08_PbodyContactPhyLen_KJH3




## ########################################################################################################################################################## Class_HEADER
class _Res_Parallel(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(
        # Res
        _ResWidth=None,
        _ResLength=None,
        _CONUMX=None,
        _CONUMY=None,
        _SeriesStripes=None,
        _ParallelStripes=None,

        ### TG NMOS PMOS
        _TG_NumberofGate=None,  # number
        _TG_NMOSChannelWidth=None,  # number
        _TG_PMOSChannelWidth=None,
        _TG_Channellength=None,  # number
        _TG_XVT			= None, # 'XVT' ex)SLVT LVT RVT HVT EG
        _INV_NumberofGate=None,
        _NMOS_Pbody_NumCont=None,
        _PMOS_Nbody_NumCont=None,

        _Parallel_Stack=None,
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
                                  _ResWidth=None,
                                  _ResLength=None,
                                  _CONUMX=None,
                                  _CONUMY=None,
                                  _SeriesStripes=None,
                                  _ParallelStripes=None,

                                  ### TG NMOS PMOS
                                  _TG_NumberofGate=None,  # number
                                  _TG_NMOSChannelWidth=None,  # number
                                  _TG_PMOSChannelWidth=None,
                                  _TG_Channellength=None,  # number
                                  _TG_XVT			= None, # 'XVT' ex)SLVT LVT RVT HVT EG
                                  _INV_NumberofGate=None,
                                  _NMOS_Pbody_NumCont=None,
                                  _PMOS_Nbody_NumCont=None,

                                  _Parallel_Stack=None,

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

        tmpXY1 = []
        tmpXY2 = []
        for i in range(0,_Parallel_Stack):
            if i == 0:
                ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
                _Caculation_Parameters = copy.deepcopy(A51_Runit_Switch._Runit_Switch._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
                _Caculation_Parameters['_ResWidth'] = _ResWidth
                _Caculation_Parameters['_ResLength'] = _ResLength
                _Caculation_Parameters['_CONUMX'] = _CONUMX
                _Caculation_Parameters['_CONUMY'] = _CONUMY
                _Caculation_Parameters['_SeriesStripes'] = _SeriesStripes
                _Caculation_Parameters['_ParallelStripes'] = _ParallelStripes

                _Caculation_Parameters['_TG_NumberofGate'] = _TG_NumberofGate
                _Caculation_Parameters['_TG_NMOSChannelWidth'] = _TG_NMOSChannelWidth
                _Caculation_Parameters['_TG_PMOSChannelWidth'] = _TG_PMOSChannelWidth
                _Caculation_Parameters['_TG_Channellength'] = _TG_Channellength
                _Caculation_Parameters['_TG_XVT'] = _TG_XVT
                _Caculation_Parameters['_INV_NumberofGate'] = _INV_NumberofGate
                _Caculation_Parameters['_NMOS_Pbody_NumCont'] = _NMOS_Pbody_NumCont
                _Caculation_Parameters['_PMOS_Nbody_NumCont'] = _PMOS_Nbody_NumCont

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
                self._DesignParameter['SRF_Runit_Switch'] = self._SrefElementDeclaration(
                    _DesignObj=A51_Runit_Switch._Runit_Switch(_DesignParameter=None,
                                                              _Name='{}:SRF_Runit_Switch'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
                self._DesignParameter['SRF_Runit_Switch']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_Runit_Switch']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_Runit_Switch']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_Runit_Switch']['_XYCoordinates'] = [[0, 0]]
                tmpXY1.append([0, 0])

            elif i == 1:
                ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
                _Caculation_Parameters = copy.deepcopy(A51_Runit_Switch._Runit_Switch._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
                _Caculation_Parameters['_ResWidth'] = _ResWidth
                _Caculation_Parameters['_ResLength'] = _ResLength
                _Caculation_Parameters['_CONUMX'] = _CONUMX
                _Caculation_Parameters['_CONUMY'] = _CONUMY
                _Caculation_Parameters['_SeriesStripes'] = _SeriesStripes
                _Caculation_Parameters['_ParallelStripes'] = _ParallelStripes

                _Caculation_Parameters['_TG_NumberofGate'] = _TG_NumberofGate
                _Caculation_Parameters['_TG_NMOSChannelWidth'] = _TG_NMOSChannelWidth
                _Caculation_Parameters['_TG_PMOSChannelWidth'] = _TG_PMOSChannelWidth
                _Caculation_Parameters['_TG_Channellength'] = _TG_Channellength
                _Caculation_Parameters['_TG_XVT'] = _TG_XVT
                _Caculation_Parameters['_INV_NumberofGate'] = _INV_NumberofGate
                _Caculation_Parameters['_NMOS_Pbody_NumCont'] = _NMOS_Pbody_NumCont
                _Caculation_Parameters['_PMOS_Nbody_NumCont'] = _PMOS_Nbody_NumCont

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
                self._DesignParameter['SRF_Runit_Switch_flip'] = self._SrefElementDeclaration(
                    _DesignObj=A51_Runit_Switch._Runit_Switch(_DesignParameter=None,
                                                              _Name='{}:SRF_Runit_Switch_flip'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
                self._DesignParameter['SRF_Runit_Switch_flip']['_Reflect'] = [1, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_Runit_Switch_flip']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_Runit_Switch_flip']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_Runit_Switch_flip']['_XYCoordinates'] = [[0, 0]]

                tmp1 = self.get_param_KJH4('SRF_Runit_Switch','SRF_TG_Switch','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
                target_coord = tmp1[-1][0][0][0][0][0]['_XY_up_left']
                tmp2 = self.get_param_KJH4('SRF_Runit_Switch_flip','SRF_TG_Switch','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
                approaching_coord = tmp2[0][0][0][0][0][0]['_XY_down_left']
                tmp3 = self.get_param_KJH4('SRF_Runit_Switch_flip')
                Scoord = tmp3[0][0]['_XY_origin']
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY2.append(New_Scoord)
                self._DesignParameter['SRF_Runit_Switch_flip']['_XYCoordinates'] = tmpXY2


            elif i % 2 == 0:
                tmp1 = self.get_param_KJH4('SRF_Runit_Switch_flip','SRF_TG_Switch','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
                target_coord = tmp1[-1][0][0][0][0][0]['_XY_down_left']
                tmp2 = self.get_param_KJH4('SRF_Runit_Switch','SRF_TG_Switch','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
                approaching_coord = tmp2[0][0][0][0][0][0]['_XY_up_left']
                tmp3 = self.get_param_KJH4('SRF_Runit_Switch')
                Scoord = tmp3[0][0]['_XY_origin']
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY1.append(New_Scoord)
                self._DesignParameter['SRF_Runit_Switch']['_XYCoordinates'] = tmpXY1

            else:
                tmp1 = self.get_param_KJH4('SRF_Runit_Switch','SRF_TG_Switch','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
                target_coord = tmp1[-1][0][0][0][0][0]['_XY_up_left']
                tmp2 = self.get_param_KJH4('SRF_Runit_Switch_flip','SRF_TG_Switch','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
                approaching_coord = tmp2[0][0][0][0][0][0]['_XY_down_left']
                tmp3 = self.get_param_KJH4('SRF_Runit_Switch_flip')
                Scoord = tmp3[0][0]['_XY_origin']
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY2.append(New_Scoord)
                self._DesignParameter['SRF_Runit_Switch_flip']['_XYCoordinates'] = tmpXY2


        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length']      = None
        _Caculation_Parameters['_NumCont']     = _NMOS_Pbody_NumCont
        _Caculation_Parameters['_Vtc_flag']    = False

        ## Calculate '_Length'
        tmp1 = self.get_param_KJH4('SRF_Runit_Switch','SRF_Res','_PPLayer')
        _Caculation_Parameters['_Length'] = tmp1[0][0][0][0]['_Xwidth']

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Pbody_Runit'] = self._SrefElementDeclaration(_DesignObj=A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen(_DesignParameter=None, _Name='{}:SRF_Pbody_Runit'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Pbody_Runit']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbody_Runit']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbody_Runit']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbody_Runit']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        ## Calculate
        ## Target_coord: _XY_type1
        ## X
        tmp2 = self.get_param_KJH4('SRF_Pbody_Runit','SRF_PbodyContactPhyLen','BND_ODLayer')
        target_coordx = tmp1[0][0][0][0]['_XY_down_left'][0]
        ## Y
        target_coordy = tmp1[0][0][0][0]['_XY_down_left'][1] - _DRCObj._RXMinSpacetoPRES

        target_coord = [target_coordx, target_coordy]

        ## Approaching_coord: _XY_type2
        approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pbody_Runit')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        if _Parallel_Stack % 2 == 0:
            tmp1 = self.get_param_KJH4('SRF_Runit_Switch_flip', 'SRF_Res', '_PPLayer')
            target_coordx = tmp1[-1][0][0][0]['_XY_down_left'][0]
            ## Y
            target_coordy = tmp1[-1][0][0][0]['_XY_down_left'][1] + _DRCObj._RXMinSpacetoPRES
            target_coord = [target_coordx, target_coordy]

        else:
            target_coordx = tmp1[-1][0][0][0]['_XY_up_left'][0]
            ## Y
            target_coordy = tmp1[-1][0][0][0]['_XY_up_left'][1] + _DRCObj._RXMinSpacetoPRES
            target_coord = [target_coordx, target_coordy]

        ## Approaching_coord: _XY_type2
        approaching_coord = tmp2[0][0][0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pbody_Runit')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define Coordinates
        self._DesignParameter['SRF_Pbody_Runit']['_XYCoordinates'] = tmpXY

        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length']      = None
        _Caculation_Parameters['_NumCont']     = _NMOS_Pbody_NumCont
        _Caculation_Parameters['_Vtc_flag']    = True

        ## Calculate '_Length'
        tmp1 = self.get_param_KJH4('SRF_Pbody_Runit','SRF_PbodyContactPhyLen','BND_ODLayer')
        _Caculation_Parameters['_Length'] = tmp1[1][0][0][0]['_XY_up'][1] - tmp1[0][0][0][0]['_XY_down'][1]

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Pbody_Vertical'] = self._SrefElementDeclaration(_DesignObj=A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen(_DesignParameter=None, _Name='{}:SRF_Pbody_Vertical'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Pbody_Vertical']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbody_Vertical']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbody_Vertical']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbody_Vertical']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        # target_coordx = tmp1[0][0][0][0]['_XY_down_left'][0] - _DRCObj._RXMinSpacetoPRES
        # target_coordy = tmp1[0][0][0][0]['_XY_down_left'][1]
        # target_coord = [target_coordx, target_coordy]
        #
        # tmp2 = self.get_param_KJH4('SRF_Pbody_Vertical','SRF_PbodyContactPhyLen','BND_ODLayer')
        # approaching_coord = tmp2[0][0][0][0]['_XY_down_left']
        #
        # tmp3 = self.get_param_KJH4('SRF_Pbody_Vertical')
        # Scoord = tmp3[0][0]['_XY_origin']
        # New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        # tmpXY.append(New_Scoord)

        target_coordx = tmp1[0][0][0][0]['_XY_down_right'][0] + _DRCObj._RXMinSpacetoPRES
        target_coordy = tmp1[0][0][0][0]['_XY_down_right'][1]
        target_coord = [target_coordx, target_coordy]

        tmp2 = self.get_param_KJH4('SRF_Pbody_Vertical','SRF_PbodyContactPhyLen','BND_ODLayer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down_left']

        tmp3 = self.get_param_KJH4('SRF_Pbody_Vertical')
        Scoord = tmp3[0][0]['_XY_origin']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define Coordinates
        self._DesignParameter['SRF_Pbody_Vertical']['_XYCoordinates'] = tmpXY


        # Define Boundary_element
        self._DesignParameter['BND_Met1Layer_ResGuardRing'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Pbody_Runit','SRF_PbodyContactPhyLen','BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_Pbody_Vertical','SRF_PbodyContactPhyLen','BND_Met1Layer')
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met1Layer_ResGuardRing']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met1Layer_ResGuardRing']['_XWidth'] = tmp2[0][0][0][0]['_XY_down_right'][0] - tmp1[0][0][0][0]['_XY_down_right'][0]

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met1Layer_ResGuardRing']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        target_coord = tmp2[0][0][0][0]['_XY_down_right']
        # Approaching_coord
        tmp3 = self.get_param_KJH4('BND_Met1Layer_ResGuardRing')
        approaching_coord = tmp3[0][0]['_XY_down_right']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        target_coord = tmp2[0][0][0][0]['_XY_up_right']
        approaching_coord = tmp3[0][0]['_XY_up_right']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        # Define
        self._DesignParameter['BND_Met1Layer_ResGuardRing']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_PPLayer_ResGuardRing'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Pbody_Runit','SRF_PbodyContactPhyLen','BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_Pbody_Vertical','SRF_PbodyContactPhyLen','BND_PPLayer')
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_PPLayer_ResGuardRing']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_PPLayer_ResGuardRing']['_XWidth'] = tmp2[0][0][0][0]['_XY_down_right'][0] - tmp1[0][0][0][0]['_XY_down_right'][0]

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_PPLayer_ResGuardRing']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        target_coord = tmp2[0][0][0][0]['_XY_down_right']
        # Approaching_coord
        tmp3 = self.get_param_KJH4('BND_PPLayer_ResGuardRing')
        approaching_coord = tmp3[0][0]['_XY_down_right']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        target_coord = tmp2[0][0][0][0]['_XY_up_right']
        approaching_coord = tmp3[0][0]['_XY_up_right']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        # Define
        self._DesignParameter['BND_PPLayer_ResGuardRing']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_ODLayer_ResGuardRing'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0],
            _Datatype=DesignParameters._LayerMapping['DIFF'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Pbody_Runit','SRF_PbodyContactPhyLen','BND_ODLayer')
        tmp2 = self.get_param_KJH4('SRF_Pbody_Vertical','SRF_PbodyContactPhyLen','BND_ODLayer')
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_ODLayer_ResGuardRing']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_ODLayer_ResGuardRing']['_XWidth'] = tmp2[0][0][0][0]['_XY_down_right'][0] - tmp1[0][0][0][0]['_XY_down_right'][0]

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_ODLayer_ResGuardRing']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        target_coord = tmp2[0][0][0][0]['_XY_down_right']
        # Approaching_coord
        tmp3 = self.get_param_KJH4('BND_ODLayer_ResGuardRing')
        approaching_coord = tmp3[0][0]['_XY_down_right']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        target_coord = tmp2[0][0][0][0]['_XY_up_right']
        approaching_coord = tmp3[0][0]['_XY_up_right']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        # Define
        self._DesignParameter['BND_ODLayer_ResGuardRing']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_Met1Layer_TGGuardRing'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Runit_Switch','SRF_TG_Switch','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_Pbody_Vertical','SRF_PbodyContactPhyLen','BND_Met1Layer')
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met1Layer_TGGuardRing']['_YWidth'] = tmp1[0][0][0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met1Layer_TGGuardRing']['_XWidth'] = tmp1[0][0][0][0][0][0]['_XY_down_left'][0] - tmp2[-1][0][0][0]['_XY_down_left'][0]

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met1Layer_TGGuardRing']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        tmp3 = self.get_param_KJH4('BND_Met1Layer_TGGuardRing')
        for i in range(_Parallel_Stack//2):

            target_coord = tmp1[i][0][0][0][0][0]['_XY_down_left']

            approaching_coord = tmp3[0][0]['_XY_down_right']
            # Sref coord
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        tmp1 = self.get_param_KJH4('SRF_Runit_Switch_flip','SRF_TG_Switch','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        target_coord = tmp1[-1][0][0][0][0][0]['_XY_down_left']

        approaching_coord = tmp3[0][0]['_XY_up_right']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['BND_Met1Layer_TGGuardRing']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_PPLayer_TGGuardRing'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('SRF_Runit_Switch','SRF_TG_Switch','SRF_Pbody','SRF_PbodyContactPhyLen','BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_Pbody_Vertical','SRF_PbodyContactPhyLen','BND_PPLayer')
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_PPLayer_TGGuardRing']['_YWidth'] = tmp1[0][0][0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_PPLayer_TGGuardRing']['_XWidth'] = tmp1[0][0][0][0][0][0]['_XY_down_left'][0] - tmp2[-1][0][0][0]['_XY_down_left'][0]

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_PPLayer_TGGuardRing']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        tmp3 = self.get_param_KJH4('BND_PPLayer_TGGuardRing')
        for i in range(_Parallel_Stack//2):

            target_coord = tmp1[i][0][0][0][0][0]['_XY_down_left']

            approaching_coord = tmp3[0][0]['_XY_down_right']
            # Sref coord
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        tmp1 = self.get_param_KJH4('SRF_Runit_Switch_flip','SRF_TG_Switch','SRF_Pbody','SRF_PbodyContactPhyLen','BND_PPLayer')
        target_coord = tmp1[-1][0][0][0][0][0]['_XY_down_left']

        approaching_coord = tmp3[0][0]['_XY_up_right']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['BND_PPLayer_TGGuardRing']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_ODLayer_TGGuardRing'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0],
            _Datatype=DesignParameters._LayerMapping['DIFF'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        tmp1 = self.get_param_KJH4('SRF_Runit_Switch','SRF_TG_Switch','SRF_Pbody','SRF_PbodyContactPhyLen','BND_ODLayer')
        tmp2 = self.get_param_KJH4('SRF_Pbody_Vertical','SRF_PbodyContactPhyLen','BND_ODLayer')
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_ODLayer_TGGuardRing']['_YWidth'] = tmp1[0][0][0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_ODLayer_TGGuardRing']['_XWidth'] = tmp1[0][0][0][0][0][0]['_XY_down_left'][0] - tmp2[-1][0][0][0]['_XY_down_left'][0]

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_ODLayer_TGGuardRing']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        tmp3 = self.get_param_KJH4('BND_ODLayer_TGGuardRing')
        for i in range(_Parallel_Stack//2):

            target_coord = tmp1[i][0][0][0][0][0]['_XY_down_left']

            approaching_coord = tmp3[0][0]['_XY_down_right']
            # Sref coord
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        tmp1 = self.get_param_KJH4('SRF_Runit_Switch_flip','SRF_TG_Switch','SRF_Pbody','SRF_PbodyContactPhyLen','BND_ODLayer')
        target_coord = tmp1[-1][0][0][0][0][0]['_XY_down_left']

        approaching_coord = tmp3[0][0]['_XY_up_right']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['BND_ODLayer_TGGuardRing']['_XYCoordinates'] = tmpXY


## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_AJH
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_A52_Res_Parallel'
    cellname = 'A52_Res_Parallel'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        _ResWidth=160,
        _ResLength=1300,
        _CONUMX=None,
        _CONUMY=None,
        _SeriesStripes=50,
        _ParallelStripes=1,

        _TG_NumberofGate=100,  # number
        _TG_NMOSChannelWidth=500,  # number
        _TG_PMOSChannelWidth=1000,
        _TG_Channellength=150,  # number
        _TG_XVT			='EG', # 'XVT' ex)SLVT LVT RVT HVT EG
        _INV_NumberofGate       =2,
        _NMOS_Pbody_NumCont     =2,
        _PMOS_Nbody_NumCont     =2,

        _Parallel_Stack         =8,
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
    LayoutObj = _Res_Parallel(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('###############      Sending to FTP Server...      ##################')
    My = MyInfo_AJH.USER(DesignParameters._Technology)
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
