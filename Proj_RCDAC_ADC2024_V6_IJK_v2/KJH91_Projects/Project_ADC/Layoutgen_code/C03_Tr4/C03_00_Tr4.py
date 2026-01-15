
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


## Define Class
class _Tr4(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(

        # Tr4
        _Tr4_NMOSNumberofGate    =   4,     #number
        _Tr4_NMOSChannelWidth    =   500,   #number
        _Tr4_NMOSChannellength   =   30,     #number
        _Tr4_GateSpacing         =   80,   #None/number
        _Tr4_SDWidth             =   None,   #None/number
        _Tr4_XVT                 =   'RVT',  #'XVT' ex)SLVT LVT RVT HVT
        _Tr4_PCCrit              =   True,   #None/True

            # Source_node_ViaM1M2
        _Tr4_Source_Via_TF       =   True,  #True/False

            # Drain_node_ViaM1M2
        _Tr4_Drain_Via_TF        =   True,  #True/False

            # POLY dummy setting
        _Tr4_NMOSDummy           =   True,  # TF
                # if _PMOSDummy == True
        _Tr4_NMOSDummy_length    =   None,  # None/Value
        _Tr4_NMOSDummy_placement =   None,  # None/'Up'/'Dn'/

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

                                  # Tr4
                                  _Tr4_NMOSNumberofGate=4,  # number
                                  _Tr4_NMOSChannelWidth=500,  # number
                                  _Tr4_NMOSChannellength=30,  # number
                                  _Tr4_GateSpacing=80,  # None/number
                                  _Tr4_SDWidth=None,  # None/number
                                  _Tr4_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Tr4_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _Tr4_Source_Via_TF=True,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Tr4_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _Tr4_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tr4_NMOSDummy_length=None,  # None/Value
                                  _Tr4_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

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


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr4, nfettw
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  M4, nfettw: Sref Gen.
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A03_NmosWithDummy_KJH2._NmosWithDummy_KJH2._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOSNumberofGate']     =   _Tr4_NMOSNumberofGate
        _Caculation_Parameters['_NMOSChannelWidth']     =   _Tr4_NMOSChannelWidth
        _Caculation_Parameters['_NMOSChannellength']    =   _Tr4_NMOSChannellength
        _Caculation_Parameters['_GateSpacing']          =   _Tr4_GateSpacing
        _Caculation_Parameters['_SDWidth']              =   _Tr4_SDWidth
        _Caculation_Parameters['_XVT']                  =   _Tr4_XVT
        _Caculation_Parameters['_PCCrit']               =   _Tr4_PCCrit
        _Caculation_Parameters['_Source_Via_TF']        =   _Tr4_Source_Via_TF
        _Caculation_Parameters['_Drain_Via_TF']         =   _Tr4_Drain_Via_TF
        _Caculation_Parameters['_NMOSDummy']            =   _Tr4_NMOSDummy
        _Caculation_Parameters['_NMOSDummy_length']     =   _Tr4_NMOSDummy_length
        _Caculation_Parameters['_NMOSDummy_placement']  =   _Tr4_NMOSDummy_placement

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_NMOS'] = self._SrefElementDeclaration(_DesignObj=A03_NmosWithDummy_KJH2._NmosWithDummy_KJH2(_DesignParameter=None, _Name='{}:SRF_NMOS'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_NMOS']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NMOS']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NMOS']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NMOS']['_XYCoordinates'] = [[0, 0]]

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Tr4, nfettw: Source M2 up connection
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr4, nfettw: Source M2 up connection: Vtc
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NMOS_Source_Vtc_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_NMOS', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
            ## Get_Outter : tmp['_Most--']['coord'] ex) down, left, right, up
        tmp = self.get_outter_KJH4('SRF_NMOS')
        output_element = tmp['_Mostup']['index']
        output_elementname = tmp['_Layercoord'][output_element[0]][1]
        outter_coord = tmp['_Mostup']['coord']

        self._DesignParameter['BND_NMOS_Source_Vtc_M2']['_YWidth'] = _DRCobj._MetalxMinSpace41 + abs(tmp1[0][0][0][0][0]['_XY_up'][1] - outter_coord[1])

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_NMOS','BND_Met1Layer_Source')
        self._DesignParameter['BND_NMOS_Source_Vtc_M2']['_XWidth'] = tmp[0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NMOS_Source_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

        tmp = self.get_param_KJH4('SRF_NMOS', 'BND_Met1Layer_Source')
        tmpXY = []
        for i in range(0, len(tmp[0])):
            ## Calculate Sref XYcoord
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_NMOS', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
            target_coord = tmp1[0][i][0][0][0]['_XY_up_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_NMOS_Source_Vtc_M2')
            approaching_coord = tmp2[0][0]['_XY_down_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_NMOS_Source_Vtc_M2')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_NMOS_Source_Vtc_M2']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr4, nfettw: Source M2 up connection: Hrz
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NMOS_Source_Hrz_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth : ViaYmin 기준
        self._DesignParameter['BND_NMOS_Source_Hrz_M2']['_YWidth'] = _DRCobj._VIAxMinWidth + + 2 * max([_DRCobj._Metal1MinEnclosureVia1, _DRCobj._MetalxMinEnclosureCO])

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_NMOS', 'BND_Met1Layer_Source')
        self._DesignParameter['BND_NMOS_Source_Hrz_M2']['_XWidth'] = abs(tmp[0][-1][0]['_XY_right'][0] - tmp[0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NMOS_Source_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        ## Calculate Sref XYcoord
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_NMOS_Source_Vtc_M2')
        target_coord = tmp1[0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NMOS_Source_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NMOS_Source_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_NMOS_Source_Hrz_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Tr4, nfettw: Drain M2 down connection
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr4, nfettw: Drain M2 down connection: Vtc
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NMOS_Drain_Vtc_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_NMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        ## Get_Outter : tmp['_Most--']['coord'] ex) down, left, right, up
        tmp = self.get_outter_KJH4('SRF_NMOS')
        output_element = tmp['_Mostdown']['index']
        output_elementname = tmp['_Layercoord'][output_element[0]][1]
        outter_coord = tmp['_Mostdown']['coord']

        self._DesignParameter['BND_NMOS_Drain_Vtc_M2']['_YWidth'] = _DRCobj._MetalxMinSpace41 + abs(tmp1[0][0][0][0][0]['_XY_down'][1] - outter_coord[1])

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_NMOS', 'BND_Met1Layer_Drain')
        self._DesignParameter['BND_NMOS_Drain_Vtc_M2']['_XWidth'] = tmp[0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NMOS_Drain_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

        tmp = self.get_param_KJH4('SRF_NMOS', 'BND_Met1Layer_Drain')
        tmpXY = []
        for i in range(0, len(tmp[0])):
            ## Calculate Sref XYcoord
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_NMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
            target_coord = tmp1[0][i][0][0][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_NMOS_Drain_Vtc_M2')
            approaching_coord = tmp2[0][0]['_XY_up_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_NMOS_Drain_Vtc_M2')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_NMOS_Drain_Vtc_M2']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr4, nfettw: Drain M2 down connection: Hrz
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NMOS_Drain_Hrz_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth : ViaYmin 기준
        self._DesignParameter['BND_NMOS_Drain_Hrz_M2']['_YWidth'] = _DRCobj._VIAxMinWidth + + 2 * max([_DRCobj._Metal1MinEnclosureVia1, _DRCobj._MetalxMinEnclosureCO])

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_NMOS', 'BND_Met1Layer_Drain')
        self._DesignParameter['BND_NMOS_Drain_Hrz_M2']['_XWidth'] = abs(tmp[0][-1][0]['_XY_right'][0] - tmp[0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NMOS_Drain_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        ## Calculate Sref XYcoord
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_NMOS_Drain_Vtc_M2')
        target_coord = tmp1[0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NMOS_Drain_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NMOS_Drain_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_NMOS_Drain_Hrz_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Tr4, nfettw: Gate Poly up connection
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr4, nfettw: Gate Poly up connection: Vtc
        ## Pre-defined
        margin = 100

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NMOS_Gate_Vtc_poly'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_NMOS_Source_Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_NMOS','BND_POLayer')
        self._DesignParameter['BND_NMOS_Gate_Vtc_poly']['_YWidth'] = _DRCobj._MetalxMinSpace41 + abs(tmp1[0][0]['_XY_up'][1] - tmp2[0][0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_NMOS', 'BND_POLayer')
        self._DesignParameter['BND_NMOS_Gate_Vtc_poly']['_XWidth'] = tmp[0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NMOS_Gate_Vtc_poly']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_NMOS_Gate_Vtc_poly']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        tmp = self.get_param_KJH4('SRF_NMOS','BND_POLayer')
        for i in range(0, len(tmp[0])):
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_NMOS','BND_POLayer')
            target_coord = tmp1[0][i][0]['_XY_up_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_NMOS_Gate_Vtc_poly')
            approaching_coord = tmp2[0][0]['_XY_down_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_NMOS_Gate_Vtc_poly')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_NMOS_Gate_Vtc_poly']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr4, nfettw: Gate Poly up connection: Hrz
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NMOS_Gate_Hrz_poly'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_NMOS_Gate_Hrz_poly']['_YWidth'] = 50

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_NMOS','BND_POLayer')
        self._DesignParameter['BND_NMOS_Gate_Hrz_poly']['_XWidth'] = max(abs(tmp1[0][0][0]['_XY_left'][0] - tmp1[0][-1][0]['_XY_right'][0]),200)

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NMOS_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_NMOS_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_NMOS_Gate_Vtc_poly')
        tmp1_1 = int((tmp1[0][0]['_XY_left'][0] + tmp1[-1][0]['_XY_right'][0])/2)
        target_coord = [tmp1_1, tmp1[0][0]['_XY_up'][1]]
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NMOS_Gate_Hrz_poly')
        approaching_coord = tmp2[0][0]['_XY_down']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NMOS_Gate_Hrz_poly')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_NMOS_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY





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
    libname = 'Proj_ADC_C03_Tr4'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'C03_00_Tr4_v0_97'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

        # Tr4
        _Tr4_NMOSNumberofGate    =   4,     #number
        _Tr4_NMOSChannelWidth    =   500,   #number
        _Tr4_NMOSChannellength   =   30,     #number
        _Tr4_GateSpacing         =   None,   #None/number
        _Tr4_SDWidth             =   None,   #None/number
        _Tr4_XVT                 =   'RVT',  #'XVT' ex)SLVT LVT RVT HVT
        _Tr4_PCCrit              =   True,   #None/True

            # Source_node_ViaM1M2
        _Tr4_Source_Via_TF       =   True,  #True/False

            # Drain_node_ViaM1M2
        _Tr4_Drain_Via_TF        =   True,  #True/False

            # POLY dummy setting
        _Tr4_NMOSDummy           =   True,  # TF
                # if _PMOSDummy == True
        _Tr4_NMOSDummy_length    =   None,  # None/Value
        _Tr4_NMOSDummy_placement =   None,  # None/'Up'/'Dn'/

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
    LayoutObj = _Tr4(_DesignParameter=None, _Name=cellname)
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
