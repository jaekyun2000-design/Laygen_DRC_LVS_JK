
## Import Basic Modules
    ## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

    ## Library
import copy
import time

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A04_PmosWithDummy_KJH3


## Define Class
class _PmosRoute(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(

        # Tr4
        _TieP_PMOSNumberofGate    =   4,     #number
        _TieP_PMOSChannelWidth    =   500,   #number
        _TieP_PMOSChannellength   =   30,     #number
        _TieP_GateSpacing         =   100,   #None/number
        _TieP_SDWidth             =   None,   #None/number
        _TieP_XVT                 =   'SLVT',  #'XVT' ex)SLVT LVT RVT HVT
        _TieP_PCCrit              =   True,   #None/True

            # Source_node_ViaM1M2
        _TieP_Source_Via_TF       =   True,  #True/False

            # Drain_node_ViaM1M2
        _TieP_Drain_Via_TF        =   True,  #True/False

            # POLY dummy setting
        _TieP_PMOSDummy           =   True,  # TF
                # if _PMOSDummy == True
        _TieP_PMOSDummy_length    =   None,  # None/Value
        _TieP_PMOSDummy_placement =   None,  # None/'Up'/'Dn'/

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
                                  _TieP_PMOSNumberofGate=4,  # number
                                  _TieP_PMOSChannelWidth=500,  # number
                                  _TieP_PMOSChannellength=30,  # number
                                  _TieP_GateSpacing=100,  # None/number
                                  _TieP_SDWidth=None,  # None/number
                                  _TieP_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _TieP_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _TieP_Source_Via_TF=True,  # True/False

                                  # Drain_node_ViaM1M2
                                  _TieP_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _TieP_PMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _TieP_PMOSDummy_length=None,  # None/Value
                                  _TieP_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

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


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## TieP, slvtpfet
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  TieP, slvtpfet: Sref Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A04_PmosWithDummy_KJH3._PmosWithDummy_KJH3._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_PMOSNumberofGate']     = _TieP_PMOSNumberofGate
        _Caculation_Parameters['_PMOSChannelWidth']     = _TieP_PMOSChannelWidth
        _Caculation_Parameters['_PMOSChannellength']    = _TieP_PMOSChannellength
        _Caculation_Parameters['_GateSpacing']          = _TieP_GateSpacing
        _Caculation_Parameters['_SDWidth']              = _TieP_SDWidth
        _Caculation_Parameters['_XVT']                  = _TieP_XVT
        _Caculation_Parameters['_PCCrit']               = _TieP_PCCrit
        _Caculation_Parameters['_Source_Via_TF']        = _TieP_Source_Via_TF
        _Caculation_Parameters['_Drain_Via_TF']         = _TieP_Drain_Via_TF
        _Caculation_Parameters['_PMOSDummy']            = _TieP_PMOSDummy
        _Caculation_Parameters['_PMOSDummy_length']     = _TieP_PMOSDummy_length
        _Caculation_Parameters['_PMOSDummy_placement']  = _TieP_PMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_PMOS'] = self._SrefElementDeclaration(_DesignObj=A04_PmosWithDummy_KJH3._PmosWithDummy_KJH3(_DesignParameter=None,_Name='{}:SRF_PMOS'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_PMOS']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_PMOS']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_PMOS']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_PMOS']['_XYCoordinates'] = [[0, 0]]

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  TieP, slvtpfet: Drain Upward binding M2
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## TieP, slvtpfet: Drain Upward binding M2: Vtc
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOS_Drain_Vtc_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_PMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        ## Get_Outter : tmp['_Most--']['coord'] ex) down, left, right, up
        tmp = self.get_outter_KJH4('SRF_PMOS')
        output_element = tmp['_Mostup']['index']
        output_elementname = tmp['_Layercoord'][output_element[0]][1]
        outter_coord = tmp['_Mostup']['coord']

        self._DesignParameter['BND_PMOS_Drain_Vtc_M2']['_YWidth'] = _DRCobj._MetalxMinSpace41 + abs(tmp1[0][0][0][0][0]['_XY_up'][1] - outter_coord[1])

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_PMOS', 'BND_Met1Layer_Drain')
        self._DesignParameter['BND_PMOS_Drain_Vtc_M2']['_XWidth'] = tmp[0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOS_Drain_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

        tmp = self.get_param_KJH4('SRF_PMOS', 'BND_Met1Layer_Drain')
        tmpXY = []
        for i in range(0, len(tmp[0])):
            ## Calculate Sref XYcoord
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_PMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
            target_coord = tmp1[0][i][0][0][0]['_XY_up_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_PMOS_Drain_Vtc_M2')
            approaching_coord = tmp2[0][0]['_XY_down_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_PMOS_Drain_Vtc_M2')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_PMOS_Drain_Vtc_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## TieP, slvtpfet: Drain Upward binding M2: Hrz
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOS_Drain_Hrz_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth : ViaYmin 기준
        self._DesignParameter['BND_PMOS_Drain_Hrz_M2']['_YWidth'] = _DRCobj._VIAxMinWidth + + 2 * max(
            [_DRCobj._Metal1MinEnclosureVia1, _DRCobj._MetalxMinEnclosureCO])

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_PMOS', 'BND_Met1Layer_Drain')
        self._DesignParameter['BND_PMOS_Drain_Hrz_M2']['_XWidth'] = abs(tmp[0][-1][0]['_XY_right'][0] - tmp[0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOS_Drain_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        ## Calculate Sref XYcoord
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_PMOS_Drain_Vtc_M2')
        target_coord = tmp1[0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOS_Drain_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOS_Drain_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_PMOS_Drain_Hrz_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  TieP, slvtpfet: Gate downward binding Poly
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## TieP, slvtpfet: Gate downward binding Poly: Vtc
        ## Pre-defined
        margin = 100

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOS_Gate_Vtc_poly'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_outter_KJH4('SRF_PMOS')
        tmp2 = self.get_param_KJH4('SRF_PMOS', 'BND_POLayer')
        self._DesignParameter['BND_PMOS_Gate_Vtc_poly']['_YWidth'] = _DRCobj._MetalxMinSpace41 + abs(tmp1['_Mostdown']['coord'][0] - tmp2[0][0][0]['_XY_down'][1])

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_PMOS', 'BND_POLayer')
        self._DesignParameter['BND_PMOS_Gate_Vtc_poly']['_XWidth'] = tmp[0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOS_Gate_Vtc_poly']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_PMOS_Gate_Vtc_poly']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        tmp = self.get_param_KJH4('SRF_PMOS', 'BND_POLayer')
        for i in range(0, len(tmp[0])):
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_PMOS', 'BND_POLayer')
            target_coord = tmp1[0][i][0]['_XY_down_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_PMOS_Gate_Vtc_poly')
            approaching_coord = tmp2[0][0]['_XY_up_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_PMOS_Gate_Vtc_poly')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_PMOS_Gate_Vtc_poly']['_XYCoordinates'] = tmpXY
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## TieP, slvtpfet: Gate downward binding Poly: Hrz
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOS_Gate_Hrz_poly'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_YWidth'] = 60

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_PMOS', 'BND_POLayer')
        self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_XWidth'] = abs(tmp1[0][0][0]['_XY_left'][0] - tmp1[0][-1][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_PMOS_Gate_Vtc_poly')
        target_coord = tmp1[0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_poly')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_poly')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  TieP, slvtpfet: Gate poly to M1 via
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 0
        _Caculation_Parameters['_Layer2'] = 1
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

            ## Sref ViaX declaration
        self._DesignParameter['SRF_PMOS_Gate_ViaM0M1'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None, _Name='{}:SRF_PMOS_Gate_ViaM0M1'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_PMOS_Gate_ViaM0M1']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_PMOS_Gate_ViaM0M1']['_Angle'] = 0

            ## Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_poly')

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(tmp1[0][0]['_Xwidth'], tmp1[0][0]['_Ywidth'], 'MinEnclosureY')

            ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_PMOS_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_PMOS_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        tmp1 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_poly')
        target_coord = tmp1[0][0]['_XY_cent']
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_PMOS_Gate_ViaM0M1','SRF_ViaM0M1','BND_POLayer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_PMOS_Gate_ViaM0M1')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_PMOS_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY



        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_YCH
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ADC_C04_TieCell_v1'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'C03_00_TieP_v0_94'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

        # Tr4
        _TieP_PMOSNumberofGate    =   4,     #number (Ref:4)
        _TieP_PMOSChannelWidth    =   500,   #number
        _TieP_PMOSChannellength   =   30,     #number
        _TieP_GateSpacing         =   100,   #None/number
        _TieP_SDWidth             =   None,   #None/number
        _TieP_XVT                 =   'SLVT',  #'XVT' ex)SLVT LVT RVT HVT
        _TieP_PCCrit              =   True,   #None/True

            # Source_node_ViaM1M2
        _TieP_Source_Via_TF       =   True,  #True/False

            # Drain_node_ViaM1M2
        _TieP_Drain_Via_TF        =   True,  #True/False

            # POLY dummy setting
        _TieP_PMOSDummy           =   True,  # TF
                # if _PMOSDummy == True
        _TieP_PMOSDummy_length    =   None,  # None/Value
        _TieP_PMOSDummy_placement =   None,  # None/'Up'/'Dn'/

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
    LayoutObj = _PmosRoute(_DesignParameter=None, _Name=cellname)
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
