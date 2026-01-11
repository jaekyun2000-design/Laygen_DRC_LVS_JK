from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC_EGFET

import numpy as np
import copy
import math

# from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A04_PmosWithDummy_KJH3_EG
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A03_NmosWithDummy_KJH4_EG
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2_YCH

from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A08_PbodyContactPhyLen_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A07_NbodyContactPhyLen_KJH3

## ########################################################################################################################################################## Class_HEADER
class _TG_Switch(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

        ### TG NMOS PMOS
        _TG_NumberofGate        =None,  # number
        _TG_NMOSChannelWidth    =None,  # number
        _TG_PMOSChannelWidth    =None,
        _TG_Channellength       =None,  # number
        _TG_XVT			        =None, # 'XVT' ex)SLVT LVT RVT HVT EG
        _INV_NumberofGate       =None,
        _NMOS_Pbody_NumCont     =None,  # NMOS body
        _PMOS_Nbody_NumCont     =None,

        ### INV NMOS PMOS

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

                                  ### TG NMOS PMOS
                                  _TG_NumberofGate=None,  # number
                                  _TG_NMOSChannelWidth=None,  # number
                                  _TG_PMOSChannelWidth=None,
                                  _TG_Channellength=None,  # number
                                  _TG_XVT				= None, # 'XVT' ex)SLVT LVT RVT HVT EG
                                  _INV_NumberofGate=None,
                                  _NMOS_Pbody_NumCont=None,
                                  _PMOS_Nbody_NumCont=None,

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

        ## SREF Generation

            ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A03_NmosWithDummy_KJH4_EG._NmosWithDummy._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOSNumberofGate'] = _TG_NumberofGate
        _Caculation_Parameters['_NMOSChannelWidth'] = _TG_NMOSChannelWidth
        _Caculation_Parameters['_NMOSChannellength'] = _TG_Channellength
        _Caculation_Parameters['_GateSpacing'] = None
        _Caculation_Parameters['_SDWidth'] = None
        _Caculation_Parameters['_XVT'] = _TG_XVT
        _Caculation_Parameters['_PCCrit'] = None
        _Caculation_Parameters['_Source_Via_TF'] = True
        _Caculation_Parameters['_Drain_Via_TF'] = True
        _Caculation_Parameters['_NMOSDummy'] = True
        _Caculation_Parameters['_NMOSDummy_length'] = None
        _Caculation_Parameters['_NMOSDummy_placement'] = None
        _Caculation_Parameters['_NMOSXvt_Minexten'] = True
        _Caculation_Parameters['_NMOSXvt_placement'] = None

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_TG_Nmos'] = self._SrefElementDeclaration(
            _DesignObj=A03_NmosWithDummy_KJH4_EG._NmosWithDummy(_DesignParameter=None,_Name='{}:SRF_TG_Nmos'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_TG_Nmos']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_TG_Nmos']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_TG_Nmos']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_TG_Nmos']['_XYCoordinates'] = [[0, 0]]

        ## ################################################################################################################### Poly_M1_Gate

        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 0
        _Caculation_Parameters['_Layer2'] = 1
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Gate_CONT'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_Gate_CONT'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Gate_CONT']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Gate_CONT']['_Angle'] = 0

        # Calcuate _COY
        _Caculation_Parameters['_COY'] = 2

        # Calcuate _COX
        tmp1 = self.get_param_KJH4('SRF_TG_Nmos', 'BND_POLayer')
        tmpWidth = tmp1[0][-1][0]['_XY_right'][0] - tmp1[0][0][0]['_XY_left'][0]
        _Caculation_Parameters['_COX'] = int(
            (tmpWidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
        )

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Gate_CONT']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Gate_CONT']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        target_coord = (tmp1[0][-1][0]['_XY_up_right'] + tmp1[0][0][0]['_XY_up_left']) / 2
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Gate_CONT', 'SRF_ViaM0M1', 'BND_POLayer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Gate_CONT')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        tmp1 = self.get_param_KJH4('SRF_Gate_CONT','SRF_ViaM0M1','BND_POLayer')
        tmpdY = tmp1[0][0][0][0]['_Ywidth']
        tmpXY.append(New_Scoord + [0, tmpdY + _DRCObj._PolygateMinSpace2])
        # Define
        self._DesignParameter['SRF_Gate_CONT']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### POLY_Layer_Gate
        # Define Boundary_element
        self._DesignParameter['BND_POLayer_Hrz_Gate'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_POLayer_Hrz_Gate']['_YWidth'] = tmp2[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_TG_Nmos', 'BND_POLayer')

        self._DesignParameter['BND_POLayer_Hrz_Gate']['_XWidth'] = abs(
            tmp[0][-1][0]['_XY_right'][0] - tmp[0][0][0]['_XY_left'][0])

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_POLayer_Hrz_Gate']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_TG_Nmos', 'BND_POLayer')
        target_coord = tmp1[0][0][0]['_XY_up_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_POLayer_Hrz_Gate')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_POLayer_Hrz_Gate')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        tmpXY.append(New_Scoord + [0,tmpdY+_DRCObj._PolygateMinSpace2])
        # Define
        self._DesignParameter['BND_POLayer_Hrz_Gate']['_XYCoordinates'] = tmpXY

        ## SREF Generation

            ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A04_PmosWithDummy_KJH3_EG._PmosWithDummy._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_PMOSNumberofGate'] = _TG_NumberofGate
        _Caculation_Parameters['_PMOSChannelWidth'] = _TG_PMOSChannelWidth
        _Caculation_Parameters['_PMOSChannellength'] = _TG_Channellength
        _Caculation_Parameters['_GateSpacing'] = None
        _Caculation_Parameters['_SDWidth'] = None
        _Caculation_Parameters['_XVT'] = _TG_XVT
        _Caculation_Parameters['_PCCrit'] = None
        _Caculation_Parameters['_Source_Via_TF'] = True
        _Caculation_Parameters['_Drain_Via_TF'] = True
        _Caculation_Parameters['_PMOSDummy'] = True
        _Caculation_Parameters['_PMOSDummy_length'] = None
        _Caculation_Parameters['_PMOSDummy_placement'] = None
        _Caculation_Parameters['_PMOSXvt_Minexten'] = True
        _Caculation_Parameters['_PMOSXvt_placement'] = None

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_TG_Pmos'] = self._SrefElementDeclaration(
            _DesignObj=A04_PmosWithDummy_KJH3_EG._PmosWithDummy(_DesignParameter=None,_Name='{}:SRF_TG_Pmos'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_TG_Pmos']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_TG_Pmos']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_TG_Pmos']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_TG_Pmos']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        tmp1 = self.get_param_KJH4('BND_POLayer_Hrz_Gate')
        target_coord = tmp1[1][0]['_XY_up_left']
        tmp2 = self.get_param_KJH4('SRF_TG_Pmos','BND_POLayer')
        approaching_coord = tmp2[0][0][0]['_XY_down_left']
        tmp3 = self.get_param_KJH4('SRF_TG_Pmos')
        Scoord = tmp3[0][0]['_XY_origin']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        self._DesignParameter['SRF_TG_Pmos']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Metal2_NP_Connection

        # Define Boundary_element
        self._DesignParameter['BND_Metal2Layer_NP_SDconnect'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[],
        )

        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_TG_Nmos', 'BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_TG_Pmos', 'BND_Met1Layer')

        self._DesignParameter['BND_Metal2Layer_NP_SDconnect']['_YWidth'] = tmp2[0][0][0]['_XY_up_left'][1] - tmp1[0][0][0]['_XY_down_left'][1]

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal2Layer_NP_SDconnect']['_XWidth'] = tmp2[0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal2Layer_NP_SDconnect']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        tmp3 = self.get_param_KJH4('BND_Metal2Layer_NP_SDconnect')
        approaching_coord = tmp3[0][0]['_XY_down_left']
        for i in range(0, _TG_NumberofGate+1):
            target_coord = tmp1[0][i][0]['_XY_down_left']
            Scoord = tmp3[0][0]['_XY_origin']
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
        self._DesignParameter['BND_Metal2Layer_NP_SDconnect']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Metal3_Layer_PortABconnect
        # Define Boundary_element
        self._DesignParameter['BND_Metal3Layer_Hrz_PortAB'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[],
        )

        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_TG_Nmos', 'BND_Met1Layer')
        tmpwidth = tmp1[0][0][0]['_Ywidth']
        if tmpwidth < 300:
            self._DesignParameter['BND_Metal3Layer_Hrz_PortAB']['_YWidth'] = tmp1[0][0][0]['_Ywidth']
        elif tmpwidth < 500:
            self._DesignParameter['BND_Metal3Layer_Hrz_PortAB']['_YWidth'] = 300
        else:
            self._DesignParameter['BND_Metal3Layer_Hrz_PortAB']['_YWidth'] = 500

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal3Layer_Hrz_PortAB']['_XWidth'] = abs(tmp1[0][-1][0]['_XY_right'][0] - tmp1[0][0][0]['_XY_left'][0])

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal3Layer_Hrz_PortAB']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        target_coord = tmp1[0][0][0]['_XY_left']
        tmp3 = self.get_param_KJH4('BND_Metal3Layer_Hrz_PortAB')
        approaching_coord = tmp3[0][0]['_XY_left']
        Scoord = tmp3[0][0]['_XY_origin']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        tmp2 = self.get_param_KJH4('SRF_TG_Pmos','BND_Met1Layer')
        target_coord = tmp2[0][0][0]['_XY_left']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        self._DesignParameter['BND_Metal3Layer_Hrz_PortAB']['_XYCoordinates'] = tmpXY

## ################################################################################################################### NMOS_Drain_ViaM2M3
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Drain_ViaM2M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None,_Name='{}:SRF_Drain_ViaM2M3'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Drain_ViaM2M3']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Drain_ViaM2M3']['_Angle'] = 0

        # Calcuate _COX
        _Caculation_Parameters['_COX'] = 1

        # Calcuate _COY
        tmp = self.get_param_KJH4('SRF_TG_Nmos','SRF_Drain_ViaM1M2','SRF_ViaM1M2','BND_Met1Layer')
        M3_ywidth = tmp[0][0][0][0][0]['_Ywidth']
        Num_V1 = int((M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COY'] = 2
        else:
            _Caculation_Parameters['_COY'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Drain_ViaM2M3']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Drain_ViaM2M3']['_XYCoordinates'] = [[0, 0]]

        tmp2 = self.get_param_KJH4('SRF_Drain_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met3Layer')
        tmp3 = self.get_param_KJH4('SRF_Drain_ViaM2M3')
        if (_TG_NumberofGate % 2 == 1):
            for i in range(0, int(_TG_NumberofGate / 2) + 1):
                # Calculate
                # Target_coord
                target_coord = tmp[0][i][0][0][0]['_XY_up_left']
                # Approaching_coord
                approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
                # Sref coord
                Scoord = tmp3[0][0]['_XY_origin']
                # Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)

        else:
            for i in range(0, int(_TG_NumberofGate / 2)):
                # Calculate
                # Target_coord
                target_coord = tmp[0][i][0][0][0]['_XY_up_left']
                # Approaching_coord
                approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
                # Sref coord
                Scoord = tmp3[0][0]['_XY_origin']
                # Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)

        # Define
        self._DesignParameter['SRF_Drain_ViaM2M3']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### PMOS_Source_ViaM2M3
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Source_ViaM2M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None,
                                                        _Name='{}:SRF_Source_ViaM2M3'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Source_ViaM2M3']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Source_ViaM2M3']['_Angle'] = 0

        # Calcuate _COX
        _Caculation_Parameters['_COX'] = 1

        # Calcuate _COY
        tmp = self.get_param_KJH4('SRF_TG_Pmos', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
        M3_ywidth = tmp[0][0][0][0][0]['_Ywidth']
        Num_V1 = int((M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COY'] = 2
        else:
            _Caculation_Parameters['_COY'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Source_ViaM2M3']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Source_ViaM2M3']['_XYCoordinates'] = [[0, 0]]

        tmp2 = self.get_param_KJH4('SRF_Source_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met3Layer')
        tmp3 = self.get_param_KJH4('SRF_Source_ViaM2M3')

        for i in range(0, int(_TG_NumberofGate / 2) + 1):
            # Calculate
            # Target_coord
            target_coord = tmp[0][i][0][0][0]['_XY_up_left']
            # Approaching_coord
            approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
            # Sref coord
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        # Define
        self._DesignParameter['SRF_Source_ViaM2M3']['_XYCoordinates'] = tmpXY

        # ## ################################################################################################################### Inverter
        ########### NMOS
            ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A03_NmosWithDummy_KJH4_EG._NmosWithDummy._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOSNumberofGate'] = _INV_NumberofGate
        _Caculation_Parameters['_NMOSChannelWidth'] = _TG_NMOSChannelWidth
        _Caculation_Parameters['_NMOSChannellength'] = _TG_Channellength
        _Caculation_Parameters['_GateSpacing'] = None
        _Caculation_Parameters['_SDWidth'] = None
        _Caculation_Parameters['_XVT'] = _TG_XVT
        _Caculation_Parameters['_PCCrit'] = None
        _Caculation_Parameters['_Source_Via_TF'] = True
        _Caculation_Parameters['_Drain_Via_TF'] = True
        _Caculation_Parameters['_NMOSDummy'] = True
        _Caculation_Parameters['_NMOSDummy_length'] = None
        _Caculation_Parameters['_NMOSDummy_placement'] = None
        _Caculation_Parameters['_NMOSXvt_Minexten'] = True
        _Caculation_Parameters['_NMOSXvt_placement'] = None

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_INV_Nmos'] = self._SrefElementDeclaration(
            _DesignObj=A03_NmosWithDummy_KJH4_EG._NmosWithDummy(_DesignParameter=None,_Name='{}:SRF_INV_Nmos'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_INV_Nmos']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_INV_Nmos']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_INV_Nmos']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_INV_Nmos']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        tmp1 = self.get_param_KJH4('SRF_TG_Nmos','BND_PODummyLayer')
        target_coord = tmp1[0][1][0]['_XY_up_left']
        tmp2 = self.get_param_KJH4('SRF_INV_Nmos','BND_PODummyLayer')
        approaching_coord = tmp2[0][0][0]['_XY_up_left']
        tmp3 = self.get_param_KJH4('SRF_INV_Nmos')
        Scoord = tmp3[0][0]['_XY_origin']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        self._DesignParameter['SRF_INV_Nmos']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Poly_M1_Gate

        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 0
        _Caculation_Parameters['_Layer2'] = 1
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_INV_Gate_CONT'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_INV_Gate_CONT'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_INV_Gate_CONT']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_INV_Gate_CONT']['_Angle'] = 0

        # Calcuate _COY
        _Caculation_Parameters['_COY'] = 2

        # Calcuate _COX
        tmp1 = self.get_param_KJH4('SRF_INV_Nmos', 'BND_POLayer')
        tmpWidth = tmp1[0][-1][0]['_XY_right'][0] - tmp1[0][0][0]['_XY_left'][0]
        _Caculation_Parameters['_COX'] = int(
            (tmpWidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
        )

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_INV_Gate_CONT']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_INV_Gate_CONT']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        target_coord = (tmp1[0][-1][0]['_XY_up_right'] + tmp1[0][0][0]['_XY_up_left']) / 2
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_INV_Gate_CONT', 'SRF_ViaM0M1', 'BND_POLayer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_INV_Gate_CONT')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        tmp1 = self.get_param_KJH4('SRF_INV_Gate_CONT','SRF_ViaM0M1','BND_POLayer')
        tmpdY = tmp1[0][0][0][0]['_Ywidth']
        tmpXY.append(New_Scoord + [0, tmpdY + _DRCObj._PolygateMinSpace2])
        # Define
        self._DesignParameter['SRF_INV_Gate_CONT']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### POLY_Layer_Gate
        # Define Boundary_element
        self._DesignParameter['BND_POLayer_Hrz_Gate_INV'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_POLayer_Hrz_Gate_INV']['_YWidth'] = tmp2[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_INV_Nmos', 'BND_POLayer')

        self._DesignParameter['BND_POLayer_Hrz_Gate_INV']['_XWidth'] = abs(
            tmp[0][-1][0]['_XY_right'][0] - tmp[0][0][0]['_XY_left'][0])

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_POLayer_Hrz_Gate_INV']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_INV_Nmos', 'BND_POLayer')
        target_coord = tmp1[0][0][0]['_XY_up_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_POLayer_Hrz_Gate_INV')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_POLayer_Hrz_Gate_INV')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        tmpXY.append(New_Scoord + [0,tmpdY+_DRCObj._PolygateMinSpace2])
        # Define
        self._DesignParameter['BND_POLayer_Hrz_Gate_INV']['_XYCoordinates'] = tmpXY

        ## SREF Generation

            ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A04_PmosWithDummy_KJH3_EG._PmosWithDummy._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_PMOSNumberofGate'] = _INV_NumberofGate
        _Caculation_Parameters['_PMOSChannelWidth'] = _TG_PMOSChannelWidth
        _Caculation_Parameters['_PMOSChannellength'] = _TG_Channellength
        _Caculation_Parameters['_GateSpacing'] = None
        _Caculation_Parameters['_SDWidth'] = None
        _Caculation_Parameters['_XVT'] = _TG_XVT
        _Caculation_Parameters['_PCCrit'] = None
        _Caculation_Parameters['_Source_Via_TF'] = True
        _Caculation_Parameters['_Drain_Via_TF'] = True
        _Caculation_Parameters['_PMOSDummy'] = True
        _Caculation_Parameters['_PMOSDummy_length'] = None
        _Caculation_Parameters['_PMOSDummy_placement'] = None
        _Caculation_Parameters['_PMOSXvt_Minexten'] = True
        _Caculation_Parameters['_PMOSXvt_placement'] = None

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_INV_Pmos'] = self._SrefElementDeclaration(
            _DesignObj=A04_PmosWithDummy_KJH3_EG._PmosWithDummy(_DesignParameter=None,_Name='{}:SRF_INV_Pmos'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_INV_Pmos']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_INV_Pmos']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_INV_Pmos']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_INV_Pmos']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        tmp1 = self.get_param_KJH4('BND_POLayer_Hrz_Gate_INV')
        target_coord = tmp1[1][0]['_XY_up_left']
        tmp2 = self.get_param_KJH4('SRF_INV_Pmos','BND_POLayer')
        approaching_coord = tmp2[0][0][0]['_XY_down_left']
        tmp3 = self.get_param_KJH4('SRF_INV_Pmos')
        Scoord = tmp3[0][0]['_XY_origin']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        self._DesignParameter['SRF_INV_Pmos']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### PMOS_Source_ViaM2M3
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Source_ViaM2M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None,
                                                        _Name='{}:SRF_Source_ViaM2M3'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Source_ViaM2M3']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Source_ViaM2M3']['_Angle'] = 0

        # Calcuate _COX
        _Caculation_Parameters['_COX'] = 1

        # Calcuate _COY
        tmp = self.get_param_KJH4('SRF_TG_Pmos', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
        M3_ywidth = tmp[0][0][0][0][0]['_Ywidth']
        Num_V1 = int((M3_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
        # Define Num of COY
        if Num_V1 < 2:
            _Caculation_Parameters['_COY'] = 2
        else:
            _Caculation_Parameters['_COY'] = Num_V1

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Source_ViaM2M3']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Source_ViaM2M3']['_XYCoordinates'] = [[0, 0]]

        tmp2 = self.get_param_KJH4('SRF_Source_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met3Layer')
        tmp3 = self.get_param_KJH4('SRF_Source_ViaM2M3')

        for i in range(0, int(_TG_NumberofGate / 2) + 1):
            # Calculate
            # Target_coord
            target_coord = tmp[0][i][0][0][0]['_XY_up_left']
            # Approaching_coord
            approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
            # Sref coord
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        # Define
        self._DesignParameter['SRF_Source_ViaM2M3']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Metal2_INV_Drain_Connection

        # Define Boundary_element
        self._DesignParameter['BND_Metal2Layer_INV_Drain'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[],
        )

        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_INV_Nmos', 'BND_Met1Layer_Drain')
        tmp2 = self.get_param_KJH4('SRF_INV_Pmos', 'BND_Met1Layer_Drain')

        self._DesignParameter['BND_Metal2Layer_INV_Drain']['_YWidth'] = tmp2[0][0][0]['_XY_up_left'][1] - tmp1[0][0][0]['_XY_down_left'][1]

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal2Layer_INV_Drain']['_XWidth'] = tmp2[0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal2Layer_INV_Drain']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        tmp3 = self.get_param_KJH4('BND_Metal2Layer_INV_Drain')
        approaching_coord = tmp3[0][0]['_XY_down_left']
        for i in range(0, (_INV_NumberofGate+1)//2):
            target_coord = tmp1[0][i][0]['_XY_down_left']
            Scoord = tmp3[0][0]['_XY_origin']
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
        self._DesignParameter['BND_Metal2Layer_INV_Drain']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### PASSB_ViaM1M2
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 2

        # Sref ViaX declaration
        self._DesignParameter['SRF_PASSB_ViaM1M2'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None,
                                                        _Name='{}:SRF_PASSB_ViaM1M2'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_PASSB_ViaM1M2']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_PASSB_ViaM1M2']['_Angle'] = 0

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_PASSB_ViaM1M2']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_PASSB_ViaM1M2']['_XYCoordinates'] = [[0, 0]]

        tmp11 = self.get_param_KJH4('SRF_TG_Pmos','BND_PODummyLayer')
        tmp12 = self.get_param_KJH4('SRF_Gate_CONT', 'SRF_ViaM0M1', 'BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_PASSB_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
        tmp3 = self.get_param_KJH4('SRF_PASSB_ViaM1M2')

        # Calculate
        # Target_coord
        target_coordx = tmp11[0][1][0]['_XY_down'][0]
        target_coordy = tmp12[1][0][0][0]['_XY_right'][1]
        target_coord = [target_coordx, target_coordy]
        # Approaching_coord
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        # Define
        self._DesignParameter['SRF_PASSB_ViaM1M2']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Gate-Via Met1 connect
        # Define Boundary_element
        self._DesignParameter['BND_Met1Layer_PASSB'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met1Layer_PASSB']['_YWidth'] = tmp12[1][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH4('SRF_PASSB_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
        self._DesignParameter['BND_Met1Layer_PASSB']['_XWidth'] = abs(
            tmp2[0][0][0][0]['_XY_right'][0] - tmp12[1][0][0][0]['_XY_right'][0])

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met1Layer_PASSB']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        target_coord = tmp12[1][0][0][0]['_XY_down_right']
        # Approaching_coord
        tmp3 = self.get_param_KJH4('BND_Met1Layer_PASSB')
        approaching_coord = tmp3[0][0]['_XY_down_left']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Met1Layer_PASSB']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Gate-Via Met2 connect
        # Define Boundary_element
        self._DesignParameter['BND_Met2Layer_PASSB'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_PASSB_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        self._DesignParameter['BND_Met2Layer_PASSB']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH4('BND_Metal2Layer_INV_Drain')
        self._DesignParameter['BND_Met2Layer_PASSB']['_XWidth'] = abs(
            tmp2[-1][0]['_XY_right'][0] - tmp1[0][0][0][0]['_XY_right'][0])

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met2Layer_PASSB']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        target_coord = tmp1[0][0][0][0]['_XY_down_right']
        # Approaching_coord
        tmp3 = self.get_param_KJH4('BND_Met2Layer_PASSB')
        approaching_coord = tmp3[0][0]['_XY_down_left']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Met2Layer_PASSB']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Gate-Via Met1 connect
        # Define Boundary_element
        self._DesignParameter['BND_Met1Layer_PASS'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        # tmp12 = self.get_param_KJH4('SRF_Gate_CONT', 'SRF_ViaM0M1', 'BND_Met1Layer') 참고용
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met1Layer_PASS']['_YWidth'] = tmp12[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH4('SRF_INV_Nmos', 'BND_PODummyLayer')
        self._DesignParameter['BND_Met1Layer_PASS']['_XWidth'] = tmp2[0][-1][0]['_XY_right'][0] - tmp12[1][0][0][0]['_XY_right'][0] + 50

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met1Layer_PASS']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        target_coord = tmp12[0][0][0][0]['_XY_down_right']
        # Approaching_coord
        tmp3 = self.get_param_KJH4('BND_Met1Layer_PASS')
        approaching_coord = tmp3[0][0]['_XY_down_left']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Met1Layer_PASS']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_Met1Layer_PASS_gate'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        # Define Boundary_element _YWidth
        tmp2 = self.get_param_KJH4('SRF_INV_Gate_CONT', 'SRF_ViaM0M1', 'BND_Met1Layer')
        self._DesignParameter['BND_Met1Layer_PASS_gate']['_YWidth'] = tmp2[1][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1]

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met1Layer_PASS_gate']['_XWidth'] = _TG_Channellength

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met1Layer_PASS_gate']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        target_coord = tmp2[0][0][0][0]['_XY_down']
        # Approaching_coord
        tmp3 = self.get_param_KJH4('BND_Met1Layer_PASS_gate')
        approaching_coord = tmp3[0][0]['_XY_down']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Met1Layer_PASS_gate']['_XYCoordinates'] = tmpXY


        ## Power: XbodyContactPhyLen 사용
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length']      = None
        _Caculation_Parameters['_NumCont']     = _NMOS_Pbody_NumCont
        _Caculation_Parameters['_Vtc_flag']    = False

        ## Calculate '_Length'
        tmp11 = self.get_outter_KJH4('SRF_TG_Nmos')
        tmp12 = self.get_outter_KJH4('SRF_INV_Nmos')
        _Caculation_Parameters['_Length'] = abs(tmp12['_Mostright']['coord'][0] - tmp11['_Mostleft']['coord'][0])

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Pbody'] = self._SrefElementDeclaration(_DesignObj=A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen(_DesignParameter=None, _Name='{}:SRF_Pbody'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Pbody']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbody']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbody']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbody']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        ## Calculate
        ## Target_coord: _XY_type1
        ## X
        target_coordx = np.round(0.5 * (tmp12['_Mostright']['coord'][0] + tmp11['_Mostleft']['coord'][0]))
        ## Y
        target_coordy = tmp11['_Mostdown']['coord'][0]

        target_coord = [target_coordx, target_coordy]

        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pbody')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[1] = New_Scoord[1] - 70
        tmpXY.append(New_Scoord)
        ## Define Coordinates
        self._DesignParameter['SRF_Pbody']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  PMOS: Nbody Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A07_NbodyContactPhyLen_KJH3._NbodyContactPhyLen._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length']      = None
        _Caculation_Parameters['_NumCont']     = _PMOS_Nbody_NumCont
        _Caculation_Parameters['_Vtc_flag']    = False

        ## Calculate '_Length'
        tmp11 = self.get_outter_KJH4('SRF_TG_Pmos')
        tmp12 = self.get_outter_KJH4('SRF_INV_Pmos')
        _Caculation_Parameters['_Length']      = abs(tmp12['_Mostright']['coord'][0] - tmp11['_Mostleft']['coord'][0])

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Nbody'] = self._SrefElementDeclaration(_DesignObj=A07_NbodyContactPhyLen_KJH3._NbodyContactPhyLen(_DesignParameter=None, _Name='{}:SRF_Nbody'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Nbody']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nbody']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nbody']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nbody']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Nbody']['_XYCoordinates'] = [[0, 0]]

                        ## Calculate
                            ## Target_coord: _XY_type1
        ## X
        target_coordx = np.round(0.5 * (tmp12['_Mostright']['coord'][0] + tmp11['_Mostleft']['coord'][0]))
        ## Y
        target_coordy = tmp11['_Mostup']['coord'][0]

        target_coord = [target_coordx, target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Nbody')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[1] = New_Scoord[1] + 70
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Nbody']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### Metal1_Power_Source_Connection

        # Define Boundary_element
        self._DesignParameter['BND_Metal1Layer_INV_NMOS_Source'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[],
        )

        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_INV_Nmos', 'BND_Met1Layer_Source')
        tmp2 = self.get_param_KJH4('SRF_Pbody', 'SRF_PbodyContactPhyLen','BND_Met1Layer')

        self._DesignParameter['BND_Metal1Layer_INV_NMOS_Source']['_YWidth'] = tmp1[0][0][0]['_XY_up_left'][1] - tmp2[0][0][0][0]['_XY_down_left'][1]

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal1Layer_INV_NMOS_Source']['_XWidth'] = tmp1[0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal1Layer_INV_NMOS_Source']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        tmp3 = self.get_param_KJH4('BND_Metal1Layer_INV_NMOS_Source')
        approaching_coord = tmp3[0][0]['_XY_up_left']
        Scoord = tmp3[0][0]['_XY_origin']

        for i in range(0, _INV_NumberofGate//2 + 1):
            target_coord = tmp1[0][i][0]['_XY_up_left']
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
        self._DesignParameter['BND_Metal1Layer_INV_NMOS_Source']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_Metal1Layer_INV_PMOS_Source'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[],
        )

        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_INV_Pmos', 'BND_Met1Layer_Source')
        tmp2 = self.get_param_KJH4('SRF_Nbody', 'SRF_NbodyContactPhyLen','BND_Met1Layer')

        self._DesignParameter['BND_Metal1Layer_INV_PMOS_Source']['_YWidth'] = tmp2[0][0][0][0]['_XY_up_left'][1] - tmp1[0][0][0]['_XY_down_left'][1]

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal1Layer_INV_PMOS_Source']['_XWidth'] = tmp1[0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal1Layer_INV_PMOS_Source']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []
        tmp3 = self.get_param_KJH4('BND_Metal1Layer_INV_PMOS_Source')
        approaching_coord = tmp3[0][0]['_XY_down_left']
        Scoord = tmp3[0][0]['_XY_origin']

        for i in range(0, _INV_NumberofGate//2 + 1):
            target_coord = tmp1[0][i][0]['_XY_down_left']
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
        self._DesignParameter['BND_Metal1Layer_INV_PMOS_Source']['_XYCoordinates'] = tmpXY

        ############## Extension: Nwell, PPLayer, XVTLayer

        # Define Boundary_element
        self._DesignParameter['BND_NWell_Ext'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp11 = self.get_param_KJH4('SRF_TG_Pmos','BND_PMOS_NWell')
        tmp12 = self.get_param_KJH4('SRF_Nbody','SRF_NbodyContactPhyLen','BND_Nwell')
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_NWell_Ext']['_YWidth'] = tmp12[0][0][0][0]['_XY_up'][1] - tmp11[0][0][0]['_XY_down'][1]

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_NWell_Ext']['_XWidth'] = (max(tmp12[0][0][0][0]['_XY_right'][0], tmp11[0][0][0]['_XY_right'][0])
                                                             - min(tmp12[0][0][0][0]['_XY_left'][0], tmp11[0][0][0]['_XY_left'][0]))

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_NWell_Ext']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        target_coord = tmp12[0][0][0][0]['_XY_up']
        # Approaching_coord
        tmp3 = self.get_param_KJH4('BND_NWell_Ext')
        approaching_coord = tmp3[0][0]['_XY_up']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_NWell_Ext']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_PPLayer_Ext'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp11 = self.get_param_KJH4('SRF_TG_Pmos','BND_PPLayer')
        tmp12 = self.get_param_KJH4('SRF_INV_Pmos','BND_PPLayer')
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_PPLayer_Ext']['_YWidth'] = tmp11[0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_PPLayer_Ext']['_XWidth'] = tmp12[0][0][0]['_XY_right'][0] - tmp11[0][0][0]['_XY_left'][0]

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_PPLayer_Ext']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        target_coord = tmp11[0][0][0]['_XY_down_left']
        # Approaching_coord
        tmp3 = self.get_param_KJH4('BND_PPLayer_Ext')
        approaching_coord = tmp3[0][0]['_XY_down_left']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_PPLayer_Ext']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        if (DesignParameters._Technology == '028nm') and _TG_XVT in ('SLVT', 'LVT', 'RVT', 'HVT', 'EG'):
            _XVTLayer = 'BND_' + _TG_XVT + 'Layer'
            _XVTLayerMappingName = _TG_XVT

        elif DesignParameters._Technology in ('028nm'):
            raise NotImplementedError(f"Invalid '_XVT' argument({_TG_XVT}) for {DesignParameters._Technology}")

        else:
            raise NotImplementedError(f"Not Yet Implemented in other technology : {DesignParameters._Technology}")

        if _XVTLayer != None:
            # Define Boundary_element
            self._DesignParameter[_XVTLayer] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping[_XVTLayerMappingName][0],
                _Datatype=DesignParameters._LayerMapping[_XVTLayerMappingName][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )

        tmp11 = self.get_param_KJH4('SRF_TG_Nmos',_XVTLayer)
        tmp12 = self.get_param_KJH4('SRF_INV_Pmos',_XVTLayer)
        tmp21 = self.get_param_KJH4('SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        tmp22 = self.get_param_KJH4('SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        # Define Boundary_element _YWidth
        self._DesignParameter[_XVTLayer]['_YWidth'] = tmp22[0][0][0][0]['_XY_up'][1] - tmp21[0][0][0][0]['_XY_down'][1]

        # Define Boundary_element _XWidth
        self._DesignParameter[_XVTLayer]['_XWidth'] = tmp12[0][0][0]['_XY_right'][0] - tmp11[0][0][0]['_XY_left'][0]

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter[_XVTLayer]['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        target_coordx = tmp11[0][0][0]['_XY_down_left'][0]
        target_coordy = tmp21[0][0][0][0]['_XY_down'][1]
        target_coord = [target_coordx, target_coordy]
        # Approaching_coord
        tmp3 = self.get_param_KJH4(_XVTLayer)
        approaching_coord = tmp3[0][0]['_XY_down_left']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter[_XVTLayer]['_XYCoordinates'] = tmpXY


## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_AJH
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_A50_TG_Switch'
    cellname = 'A50_TG_Switch'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

        ### TG NMOS PMOS
        _TG_NumberofGate        =100,  # number
        _TG_NMOSChannelWidth    =500,  # number
        _TG_PMOSChannelWidth    =1000,
        _TG_Channellength       =150,  # number
        _TG_XVT			        ='EG', # 'XVT' ex)SLVT LVT RVT HVT EG
        _INV_NumberofGate       =2,
        _NMOS_Pbody_NumCont     =2,
        _PMOS_Nbody_NumCont     =2,

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
    LayoutObj = _TG_Switch(_DesignParameter=None, _Name=cellname)
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

