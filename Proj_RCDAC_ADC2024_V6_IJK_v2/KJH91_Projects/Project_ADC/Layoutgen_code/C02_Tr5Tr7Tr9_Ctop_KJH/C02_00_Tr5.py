
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


## Define Class
class _Tr5(StickDiagram_KJH1._StickDiagram_KJH):

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
        _Caculation_Parameters = copy.deepcopy(A04_PmosWithDummy_KJH2._PmosWithDummy_KJH2._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_PMOSNumberofGate']     = _Tr5_PMOSNumberofGate
        _Caculation_Parameters['_PMOSChannelWidth']     = _Tr5_PMOSChannelWidth
        _Caculation_Parameters['_PMOSChannellength']    = _Tr5_PMOSChannellength
        _Caculation_Parameters['_GateSpacing']          = _Tr5_GateSpacing
        _Caculation_Parameters['_SDWidth']              = _Tr5_SDWidth
        _Caculation_Parameters['_XVT']                  = _Tr5_XVT
        _Caculation_Parameters['_PCCrit']               = _Tr5_PCCrit
        _Caculation_Parameters['_Source_Via_TF']        = _Tr5_Source_Via_TF
        _Caculation_Parameters['_Drain_Via_TF']         = _Tr5_Drain_Via_TF
        _Caculation_Parameters['_PMOSDummy']            = _Tr5_PMOSDummy
        _Caculation_Parameters['_PMOSDummy_length']     = _Tr5_PMOSDummy_length
        _Caculation_Parameters['_PMOSDummy_placement']  = _Tr5_PMOSDummy_placement

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Pmos'] = self._SrefElementDeclaration(_DesignObj=A04_PmosWithDummy_KJH2._PmosWithDummy_KJH2(_DesignParameter=None, _Name='{}:SRF_Pmos'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Pmos']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos']['_XYCoordinates'] = [[0, 0]]

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Tr5, pfet: Drain M2 down connection
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr5, pfet: Drain M2 down connection: Vtc
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Pmos_Drain_Vtc_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Pmos', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
            ## Get_Outter : tmp['_Most--']['coord'] ex) down, left, right, up
        tmp = self.get_outter_KJH4('SRF_Pmos')
        output_element = tmp['_Mostdown']['index']
        output_elementname = tmp['_Layercoord'][output_element[0]][1]
        outter_coord = tmp['_Mostdown']['coord']

        self._DesignParameter['BND_Pmos_Drain_Vtc_M2']['_YWidth'] = _DRCobj._MetalxMinSpace41 + abs(tmp1[0][0][0][0][0]['_XY_down'][1] - outter_coord[1])

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Pmos','BND_Met1Layer_Drain')
        self._DesignParameter['BND_Pmos_Drain_Vtc_M2']['_XWidth'] = tmp[0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Pmos_Drain_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

        tmp = self.get_param_KJH4('SRF_Pmos', 'BND_Met1Layer_Drain')
        tmpXY = []
        for i in range(0, len(tmp[0])):
            ## Calculate Sref XYcoord
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Pmos', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
            target_coord = tmp1[0][i][0][0][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Pmos_Drain_Vtc_M2')
            approaching_coord = tmp2[0][0]['_XY_up_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Pmos_Drain_Vtc_M2')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_Pmos_Drain_Vtc_M2']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr5, pfetnp: Drain M2 up connection: Hrz
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Pmos_Drain_Hrz_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth : ViaYmin 기준
        self._DesignParameter['BND_Pmos_Drain_Hrz_M2']['_YWidth'] = _DRCobj._VIAxMinWidth + + 2 * max([_DRCobj._Metal1MinEnclosureVia1, _DRCobj._MetalxMinEnclosureCO])

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Pmos', 'BND_Met1Layer_Drain')
        self._DesignParameter['BND_Pmos_Drain_Hrz_M2']['_XWidth'] = abs(tmp[0][-1][0]['_XY_right'][0] - tmp[0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Pmos_Drain_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        ## Calculate Sref XYcoord
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_Pmos_Drain_Vtc_M2')
        target_coord = tmp1[0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Pmos_Drain_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Pmos_Drain_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Pmos_Drain_Hrz_M2']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Tr5, nfettw: Gate Poly up connection
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr5, nfettw: Gate Poly up connection: Vtc
        ## Pre-defined
        margin = 100

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Pmos_Gate_Vtc_poly'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Pmos_Gate_Vtc_poly']['_YWidth'] = margin

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Pmos', 'BND_POLayer')
        self._DesignParameter['BND_Pmos_Gate_Vtc_poly']['_XWidth'] = tmp[0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Pmos_Gate_Vtc_poly']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Pmos_Gate_Vtc_poly']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        tmp = self.get_param_KJH4('SRF_Pmos','BND_POLayer')
        for i in range(0, len(tmp[0])):
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Pmos','BND_POLayer')
            target_coord = tmp1[0][i][0]['_XY_up_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Pmos_Gate_Vtc_poly')
            approaching_coord = tmp2[0][0]['_XY_down_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Pmos_Gate_Vtc_poly')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_Pmos_Gate_Vtc_poly']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr12, nfettw: Gate Poly up connection: Hrz
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Pmos_Gate_Hrz_poly'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Pmos_Gate_Hrz_poly']['_YWidth'] = 50

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Pmos','BND_POLayer')
        self._DesignParameter['BND_Pmos_Gate_Hrz_poly']['_XWidth'] = max(abs(tmp1[0][0][0]['_XY_left'][0] - tmp1[0][-1][0]['_XY_right'][0]),200)

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Pmos_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Pmos_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_Pmos_Gate_Vtc_poly')
        tmp1_1 = int((tmp1[0][0]['_XY_left'][0] + tmp1[-1][0]['_XY_right'][0])/2)
        target_coord = [tmp1_1, tmp1[0][0]['_XY_up'][1]]
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Pmos_Gate_Hrz_poly')
        approaching_coord = tmp2[0][0]['_XY_down']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Pmos_Gate_Hrz_poly')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Pmos_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY


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
    cellname = 'C02_00_Tr5_v0_97'
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
    LayoutObj = _Tr5(_DesignParameter=None, _Name=cellname)
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
