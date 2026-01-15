
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
class _NmosRoute(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(

        # TieN
        _TieN_NMOSNumberofGate    =   4,     #number
        _TieN_NMOSChannelWidth    =   250,   #number
        _TieN_NMOSChannellength   =   30,     #number
        _TieN_GateSpacing         =   100,   #None/number
        _TieN_SDWidth             =   None,   #None/number
        _TieN_XVT                 =   'SLVT',  #'XVT' ex)SLVT LVT RVT HVT
        _TieN_PCCrit              =   True,   #None/True

            # Source_node_ViaM1M2
        _TieN_Source_Via_TF       =   True,  #True/False

            # Drain_node_ViaM1M2
        _TieN_Drain_Via_TF        =   True,  #True/False

            # POLY dummy setting
        _TieN_NMOSDummy           =   True,  # TF
                # if _PMOSDummy == True
        _TieN_NMOSDummy_length    =   None,  # None/Value
        _TieN_NMOSDummy_placement =   None,  # None/'Up'/'Dn'/

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

                                  # TieN
                                  _TieN_NMOSNumberofGate=4,  # number
                                  _TieN_NMOSChannelWidth=250,  # number
                                  _TieN_NMOSChannellength=30,  # number
                                  _TieN_GateSpacing=100,  # None/number
                                  _TieN_SDWidth=None,  # None/number
                                  _TieN_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _TieN_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _TieN_Source_Via_TF=True,  # True/False

                                  # Drain_node_ViaM1M2
                                  _TieN_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _TieN_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _TieN_NMOSDummy_length=None,  # None/Value
                                  _TieN_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

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


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## TieN, slvtnfet
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  TieN, slvtnfet: Sref Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A03_NmosWithDummy_KJH2._NmosWithDummy_KJH2._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOSNumberofGate']     = _TieN_NMOSNumberofGate
        _Caculation_Parameters['_NMOSChannelWidth']     = _TieN_NMOSChannelWidth
        _Caculation_Parameters['_NMOSChannellength']    = _TieN_NMOSChannellength
        _Caculation_Parameters['_GateSpacing']          = _TieN_GateSpacing
        _Caculation_Parameters['_SDWidth']              = _TieN_SDWidth
        _Caculation_Parameters['_XVT']                  = _TieN_XVT
        _Caculation_Parameters['_PCCrit']               = _TieN_PCCrit
        _Caculation_Parameters['_Source_Via_TF']        = _TieN_Source_Via_TF
        _Caculation_Parameters['_Drain_Via_TF']         = _TieN_Drain_Via_TF
        _Caculation_Parameters['_NMOSDummy']            = _TieN_NMOSDummy
        _Caculation_Parameters['_NMOSDummy_length']     = _TieN_NMOSDummy_length
        _Caculation_Parameters['_NMOSDummy_placement']  = _TieN_NMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_NMOS'] = self._SrefElementDeclaration(_DesignObj=A03_NmosWithDummy_KJH2._NmosWithDummy_KJH2(_DesignParameter=None,_Name='{}:SRF_NMOS'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_NMOS']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NMOS']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NMOS']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NMOS']['_XYCoordinates'] = [[0, 0]]

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  TieN, slvtnfet: Gate upward binding Poly
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## TieN, slvtnfet: Gate upward binding Poly: Vtc
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
        tmp1 = self.get_outter_KJH4('SRF_NMOS')
        tmp2 = self.get_param_KJH4('SRF_NMOS', 'BND_POLayer')
        self._DesignParameter['BND_NMOS_Gate_Vtc_poly']['_YWidth'] = _DRCobj._MetalxMinSpace41 + abs(tmp1['_Mostup']['coord'][0] - tmp2[0][0][0]['_XY_up'][1])

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
        tmp = self.get_param_KJH4('SRF_NMOS', 'BND_POLayer')
        for i in range(0, len(tmp[0])):
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_NMOS', 'BND_POLayer')
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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## TieN, slvtnfet: Gate upward binding Poly: Hrz
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
        self._DesignParameter['BND_NMOS_Gate_Hrz_poly']['_YWidth'] = 60

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_NMOS', 'BND_POLayer')
        self._DesignParameter['BND_NMOS_Gate_Hrz_poly']['_XWidth'] = abs(tmp1[0][0][0]['_XY_left'][0] - tmp1[0][-1][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NMOS_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_NMOS_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_NMOS_Gate_Vtc_poly')
        target_coord = tmp1[0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NMOS_Gate_Hrz_poly')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NMOS_Gate_Hrz_poly')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_NMOS_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  TieN, slvtnfet: Gate poly to M1 via
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 0
        _Caculation_Parameters['_Layer2'] = 1
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

            ## Sref ViaX declaration
        self._DesignParameter['SRF_NMOS_Gate_ViaM0M1'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None, _Name='{}:SRF_NMOS_Gate_ViaM0M1'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_NMOS_Gate_ViaM0M1']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_NMOS_Gate_ViaM0M1']['_Angle'] = 0

            ## Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH4('BND_NMOS_Gate_Hrz_poly')

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(tmp1[0][0]['_Xwidth'], tmp1[0][0]['_Ywidth'], 'MinEnclosureY')

            ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_NMOS_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_NMOS_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        tmp1 = self.get_param_KJH4('BND_NMOS_Gate_Hrz_poly')
        target_coord = tmp1[0][0]['_XY_cent']
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_NMOS_Gate_ViaM0M1','SRF_ViaM0M1','BND_POLayer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_NMOS_Gate_ViaM0M1')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_NMOS_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  TieN, slvtnfet: Gate upward binding Poly M1 extension
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NMOS_Gate_Hrz_Exten_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('SRF_NMOS_Gate_ViaM0M1','SRF_ViaM0M1','BND_Met1Layer')
        self._DesignParameter['BND_NMOS_Gate_Hrz_Exten_M1']['_YWidth'] = tmp[0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_NMOS', 'BND_Met1Layer_Drain')
        self._DesignParameter['BND_NMOS_Gate_Hrz_Exten_M1']['_XWidth'] = abs(tmp1[0][0][0]['_XY_left'][0] - tmp1[0][-1][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NMOS_Gate_Hrz_Exten_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_NMOS_Gate_Hrz_Exten_M1']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_NMOS_Gate_ViaM0M1','SRF_ViaM0M1','BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_cent']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NMOS_Gate_Hrz_Exten_M1')
        approaching_coord = tmp2[0][0]['_XY_cent']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NMOS_Gate_Hrz_Exten_M1')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_NMOS_Gate_Hrz_Exten_M1']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Source and Gate upward binding Poly M1 extension


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
    libname = 'Proj_RcdacSar_C04_TieCell'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'C03_00_TieN_v0_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

        # TieN
        _TieN_NMOSNumberofGate    =   4,     #number
        _TieN_NMOSChannelWidth    =   250,   #number
        _TieN_NMOSChannellength   =   30,     #number
        _TieN_GateSpacing         =   100,   #None/number
        _TieN_SDWidth             =   None,   #None/number
        _TieN_XVT                 =   'SLVT',  #'XVT' ex)SLVT LVT RVT HVT
        _TieN_PCCrit              =   True,   #None/True

            # Source_node_ViaM1M2
        _TieN_Source_Via_TF       =   True,  #True/False

            # Drain_node_ViaM1M2
        _TieN_Drain_Via_TF        =   True,  #True/False

            # POLY dummy setting
        _TieN_NMOSDummy           =   True,  # TF
                # if _PMOSDummy == True
        _TieN_NMOSDummy_length    =   None,  # None/Value
        _TieN_NMOSDummy_placement =   None,  # None/'Up'/'Dn'/

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
    LayoutObj = _NmosRoute(_DesignParameter=None, _Name=cellname)
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
