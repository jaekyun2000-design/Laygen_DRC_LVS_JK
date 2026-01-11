
## Import Basic Modules
    ## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

    ## Library
import copy
import time

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A08_PbodyContactPhyLen_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A07_NbodyContactPhyLen_KJH2

from KJH91_Projects.Project_ADC.Layoutgen_code.ZZ_TEST.Trash.D01_SARLogic_XmissionGate_KJH import D01_00_Nmos_KJH1, \
    D01_01_Pmos_KJH1


## Define Class
class _Xgate(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
        # NMOS
        _NMOS_NMOSNumberofGate=7,  # number
        _NMOS_NMOSChannelWidth=700,  # number
        _NMOS_NMOSChannellength=30,  # number
        _NMOS_GateSpacing=None,  # None/number
        _NMOS_SDWidth=None,  # None/number
        _NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _NMOS_PCCrit=True,  # None/True

        # Source_node_ViaM1M2
        _NMOS_Source_Via_TF=True,  # True/False

        # Drain_node_ViaM1M2
        _NMOS_Drain_Via_TF=True,  # True/False

        # POLY dummy setting
        _NMOS_NMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _NMOS_NMOSDummy_length=None,  # None/Value
        _NMOS_NMOSDummy_placement=None,  # None/'Up'/'Dn'/
        # Pbody
        _NMOS_Pbody_NumCont=3,  # Number
        _NMOS_Pbody_XlvtTop2Pdoby=None,  # Number/None(Minimum)



        # PMOS
        _PMOS_PMOSNumberofGate=5,  # number
        _PMOS_PMOSChannelWidth=300,  # number
        _PMOS_PMOSChannellength=30,  # number
        _PMOS_GateSpacing=None,  # None/number
        _PMOS_SDWidth=None,  # None/number
        _PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _PMOS_PCCrit=True,  # None/True

            # Source_node_ViaM1M2
        _PMOS_Source_Via_TF=False,  # True/False

            # Drain_node_ViaM1M2
        _PMOS_Drain_Via_TF=True,  # True/False

            # POLY dummy setting
        _PMOS_PMOSDummy=True,  # TF
            # if _PMOSDummy == True
        _PMOS_PMOSDummy_length=None,  # None/Value
        _PMOS_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

            # Nbody
        _PMOS_Nbody_NumCont=2,  # Number
        _PMOS_Nbody_Xlvtdown2Ndoby=None,  # Number/None(Minimum)

        # PMOS and NMOS Height
        _PMOSXvt2NMOSXvt=500,  # number

    )

    ## Initially Generated _DesignParameter
    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
            _Name=self._NameDeclaration(_Name=_Name),
            _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
            )

    ## DesignParameter Calculation
    def _CalculateDesignParameter(self,

                                  # NMOS
                                  _NMOS_NMOSNumberofGate=7,  # number
                                  _NMOS_NMOSChannelWidth=700,  # number
                                  _NMOS_NMOSChannellength=30,  # number
                                  _NMOS_GateSpacing=None,  # None/number
                                  _NMOS_SDWidth=None,  # None/number
                                  _NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _NMOS_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _NMOS_Source_Via_TF=True,  # True/False

                                  # Drain_node_ViaM1M2
                                  _NMOS_Drain_Via_TF=True,  # True/False

                                  # POLY dummy setting
                                  _NMOS_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _NMOS_NMOSDummy_length=None,  # None/Value
                                  _NMOS_NMOSDummy_placement=None,  # None/'Up'/'Dn'/
                                  # Pbody
                                  _NMOS_Pbody_NumCont=3,  # Number
                                  _NMOS_Pbody_XlvtTop2Pdoby=None,  # Number/None(Minimum)

                                  # PMOS
                                  _PMOS_PMOSNumberofGate=5,  # number
                                  _PMOS_PMOSChannelWidth=300,  # number
                                  _PMOS_PMOSChannellength=30,  # number
                                  _PMOS_GateSpacing=None,  # None/number
                                  _PMOS_SDWidth=None,  # None/number
                                  _PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _PMOS_PCCrit=True,  # None/True

                                    # Source_node_ViaM1M2
                                  _PMOS_Source_Via_TF=False,  # True/False

                                    # Drain_node_ViaM1M2
                                  _PMOS_Drain_Via_TF=True,  # True/False

                                    # POLY dummy setting
                                  _PMOS_PMOSDummy=True,  # TF
                                    # if _PMOSDummy == True
                                  _PMOS_PMOSDummy_length=None,  # None/Value
                                  _PMOS_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

                                    # Nbody
                                  _PMOS_Nbody_NumCont=2,  # Number
                                  _PMOS_Nbody_Xlvtdown2Ndoby=None,  # Number/None(Minimum)

                                  # PMOS and NMOS Height
                                  _PMOSXvt2NMOSXvt=500,  # number

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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  NMOS: Sref Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D01_00_Nmos_KJH1._Nmos._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_NMOSNumberofGate']     = _NMOS_NMOSNumberofGate
        _Caculation_Parameters['_NMOS_NMOSChannelWidth']     = _NMOS_NMOSChannelWidth
        _Caculation_Parameters['_NMOS_NMOSChannellength']    = _NMOS_NMOSChannellength
        _Caculation_Parameters['_NMOS_GateSpacing']          = _NMOS_GateSpacing
        _Caculation_Parameters['_NMOS_SDWidth']              = _NMOS_SDWidth
        _Caculation_Parameters['_NMOS_XVT']                  = _NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit']               = _NMOS_PCCrit
        _Caculation_Parameters['_NMOS_Source_Via_TF']        = _NMOS_Source_Via_TF
        _Caculation_Parameters['_NMOS_Drain_Via_TF']         = _NMOS_Drain_Via_TF
        _Caculation_Parameters['_NMOS_NMOSDummy']            = _NMOS_NMOSDummy
        _Caculation_Parameters['_NMOS_NMOSDummy_length']     = _NMOS_NMOSDummy_length
        _Caculation_Parameters['_NMOS_NMOSDummy_placement']  = _NMOS_NMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_NMOS'] = self._SrefElementDeclaration(_DesignObj=D01_00_Nmos_KJH1._Nmos(_DesignParameter=None, _Name='{}:SRF_NMOS'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_NMOS']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NMOS']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NMOS']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NMOS']['_XYCoordinates'] = [[0, 0]]

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  PMOS: Sref Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_PMOS_power_v2._PMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(D01_01_Pmos_KJH1._Pmos._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_PMOSPOWER_PbodyContact_1_Length']  = _PMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_PMOS_PMOSNumberofGate']     = _PMOS_PMOSNumberofGate
        _Caculation_Parameters['_PMOS_PMOSChannelWidth']     = _PMOS_PMOSChannelWidth
        _Caculation_Parameters['_PMOS_PMOSChannellength']    = _PMOS_PMOSChannellength
        _Caculation_Parameters['_PMOS_GateSpacing']          = _PMOS_GateSpacing
        _Caculation_Parameters['_PMOS_SDWidth']              = _PMOS_SDWidth
        _Caculation_Parameters['_PMOS_XVT']                  = _PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit']               = _PMOS_PCCrit
        _Caculation_Parameters['_PMOS_Source_Via_TF']        = _PMOS_Source_Via_TF
        _Caculation_Parameters['_PMOS_Drain_Via_TF']         = _PMOS_Drain_Via_TF
        _Caculation_Parameters['_PMOS_PMOSDummy']            = _PMOS_PMOSDummy
        _Caculation_Parameters['_PMOS_PMOSDummy_length']     = _PMOS_PMOSDummy_length
        _Caculation_Parameters['_PMOS_PMOSDummy_placement']  = _PMOS_PMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_PMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_PMOS_power_v2._PMOS_POWER( _DesignParameter=None, _Name='{}:PMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_PMOS'] = self._SrefElementDeclaration(_DesignObj=D01_01_Pmos_KJH1._Pmos(_DesignParameter=None, _Name='{}:SRF_PMOS'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_PMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_PMOS']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_PMOS_POWER'
        self._DesignParameter['SRF_PMOS']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_PMOS_POWER'
        self._DesignParameter['SRF_PMOS']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_PMOS_POWER'
        self._DesignParameter['SRF_PMOS']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_PMOS']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_NMOS','SRF_NMOS','BND_{}Layer'.format(_NMOS_XVT) )
        target_coord = tmp1[0][0][0][0]['_XY_up']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_PMOS','SRF_PMOS','BND_{}Layer'.format(_PMOS_XVT) )
        approaching_coord = tmp2[0][0][0][0]['_XY_down']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_PMOS')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[1] = New_Scoord[1] + _PMOSXvt2NMOSXvt
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_PMOS']['_XYCoordinates'] = tmpXY





        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## IN/OUT
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## IN: Metal2
        # Pre-defined
        Xwidth_0 = 50

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Input_Vtc_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_PMOS','BND_PMOS_Source_Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_NMOS','BND_NMOS_Source_Hrz_M2')
        self._DesignParameter['BND_Input_Vtc_M2']['_YWidth'] = abs( tmp1[0][0][0]['_XY_up'][1] - tmp2[0][0][0]['_XY_down'][1] )

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Input_Vtc_M2']['_XWidth'] = Xwidth_0

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Input_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
            ## initialized Sref coordinate
        self._DesignParameter['BND_Input_Vtc_M2']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
                ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_PMOS','BND_PMOS_Source_Hrz_M2')
        target_coord = tmp1[0][0][0]['_XY_up_left']
                ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Input_Vtc_M2')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Input_Vtc_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_Input_Vtc_M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Out: Metal2
        # Pre-defined
        Xwidth_1 = 50

        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Output_Vtc_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_PMOS','BND_PMOS_Drain_Hrz_M2')
        tmp2 = self.get_param_KJH4('SRF_NMOS','BND_NMOS_Drain_Hrz_M2')
        self._DesignParameter['BND_Output_Vtc_M2']['_YWidth'] = abs( tmp1[0][0][0]['_XY_up'][1] - tmp2[0][0][0]['_XY_down'][1] )

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Output_Vtc_M2']['_XWidth'] = Xwidth_1

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Output_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
            ## initialized Sref coordinate
        self._DesignParameter['BND_Output_Vtc_M2']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
                ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_PMOS','BND_PMOS_Drain_Hrz_M2')
        target_coord = tmp1[0][0][0]['_XY_up_right']
                ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Output_Vtc_M2')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Output_Vtc_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_Output_Vtc_M2']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  NMOS: Pbody Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A08_PbodyContactPhyLen_KJH2._PbodyContactPhyLen_KJH2._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length']      = None
        _Caculation_Parameters['_NumCont']     = _NMOS_Pbody_NumCont
        _Caculation_Parameters['_Vtc_flag']    = False

        ## Calculate '_Length'
        tmp = self.get_outter_KJH4('SRF_NMOS')
        _Caculation_Parameters['_Length']      = abs(tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0])

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Pbody'] = self._SrefElementDeclaration(_DesignObj=A08_PbodyContactPhyLen_KJH2._PbodyContactPhyLen_KJH2(_DesignParameter=None, _Name='{}:SRF_Pbody'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Pbody']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbody']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbody']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pbody']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Pbody']['_XYCoordinates'] = [[0, 0]]

        if _NMOS_Pbody_XlvtTop2Pdoby == None:
                            ## Calculate
                                ## Target_coord: _XY_type1
                                    ## X
            tmp1_1 = self.get_param_KJH4('SRF_NMOS','SRF_NMOS', 'BND_{}Layer'.format(_NMOS_XVT))
            target_coordx = tmp1_1[0][0][0][0]['_XY_left'][0]
                                    ## Y
            tmp1_2 = self.get_outter_KJH4('SRF_NMOS')
            target_coordy = tmp1_2['_Mostdown']['coord'][0]

            target_coord = [target_coordx,target_coordy]
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Pbody')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[1] = New_Scoord[1] - 50
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_Pbody']['_XYCoordinates'] = tmpXY

        else:
                            ## Calculate
                                ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_NMOS','SRF_NMOS','BND_{}Layer'.format(_NMOS_XVT))
            target_coord = tmp1[0][0][0][0]['_XY_up_left']
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Pbody')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[1] = New_Scoord[1] - _NMOS_Pbody_XlvtTop2Pdoby
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_Pbody']['_XYCoordinates'] = tmpXY




        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  PMOS: Nbody Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A07_NbodyContactPhyLen_KJH2._NbodyContactPhyLen_KJH2._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length']      = None
        _Caculation_Parameters['_NumCont']     = _PMOS_Nbody_NumCont
        _Caculation_Parameters['_Vtc_flag']    = False

        ## Calculate '_Length'
        tmp = self.get_outter_KJH4('SRF_PMOS')
        _Caculation_Parameters['_Length']      = abs(tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0])

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Nbody'] = self._SrefElementDeclaration(_DesignObj=A07_NbodyContactPhyLen_KJH2._NbodyContactPhyLen_KJH2(_DesignParameter=None, _Name='{}:SRF_Nbody'.format(_Name)))[0]

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

        if _PMOS_Nbody_Xlvtdown2Ndoby == None:
                            ## Calculate
                                ## Target_coord: _XY_type1
                                    ## X
            tmp1_1 = self.get_param_KJH4('SRF_PMOS', 'SRF_PMOS', 'BND_{}Layer'.format(_PMOS_XVT))
            target_coordx = tmp1_1[0][0][0][0]['_XY_left'][0]
                                    ## Y
            tmp1_2 = self.get_outter_KJH4('SRF_PMOS')
            target_coordy = tmp1_2['_Mostup']['coord'][0]

            target_coord = [target_coordx,target_coordy]
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_down_left']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Nbody')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[1] = New_Scoord[1] + 50
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_Nbody']['_XYCoordinates'] = tmpXY

        else:
                            ## Calculate
                                ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_PMOS','SRF_PMOS','BND_{}Layer'.format(_PMOS_XVT))
            target_coord = tmp1[0][0][0][0]['_XY_down_left']
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_down_left']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Nbody')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[1] = New_Scoord[1] + _PMOS_Nbody_Xlvtdown2Ndoby
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_Nbody']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  PMOS: NWELL Exten
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOS_NellExten'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Nbody','SRF_NbodyContactPhyLen','BND_Nwell')
        tmp2 = self.get_param_KJH4('SRF_PMOS','SRF_PMOS','BND_{}Layer'.format(_PMOS_XVT))
        self._DesignParameter['BND_PMOS_NellExten']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] )

        ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Nbody','SRF_NbodyContactPhyLen','BND_Nwell')
        self._DesignParameter['BND_PMOS_NellExten']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOS_NellExten']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
            ## initialized Sref coordinate
        self._DesignParameter['BND_PMOS_NellExten']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
                ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Nbody','SRF_NbodyContactPhyLen','BND_Nwell')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
                ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOS_NellExten')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOS_NellExten')
        Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
            ## Define coordinates
        self._DesignParameter['BND_PMOS_NellExten']['_XYCoordinates'] = tmpXY

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
    libname = 'Proj_ADC_D01_SARLogic_XmissionGate_KJH'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'D01_02_Xgate_v1_80'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

        # NMOS
        _NMOS_NMOSNumberofGate=4,  # number
        _NMOS_NMOSChannelWidth=100,  # number
        _NMOS_NMOSChannellength=30,  # number
        _NMOS_GateSpacing=None,  # None/number
        _NMOS_SDWidth=None,  # None/number
        _NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _NMOS_PCCrit=True,  # None/True

            # Source_node_ViaM1M2
        _NMOS_Source_Via_TF=True,  # True/False

            # Drain_node_ViaM1M2
        _NMOS_Drain_Via_TF=True,  # True/False

            # POLY dummy setting
        _NMOS_NMOSDummy=True,  # TF
            # if _PMOSDummy == True
        _NMOS_NMOSDummy_length=None,  # None/Value
        _NMOS_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

            # Pbody
        _NMOS_Pbody_NumCont=3,  # Number
        _NMOS_Pbody_XlvtTop2Pdoby=None,  # Number/None(Minimum)

        # PMOS
        _PMOS_PMOSNumberofGate=4,  # number
        _PMOS_PMOSChannelWidth=200,  # number
        _PMOS_PMOSChannellength=30,  # number
        _PMOS_GateSpacing=None,  # None/number
        _PMOS_SDWidth=None,  # None/number
        _PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
        _PMOS_PCCrit=True,  # None/True

            # Source_node_ViaM1M2
        _PMOS_Source_Via_TF=True,  # True/False

            # Drain_node_ViaM1M2
        _PMOS_Drain_Via_TF=True,  # True/False

            # POLY dummy setting
        _PMOS_PMOSDummy=True,  # TF
            # if _PMOSDummy == True
        _PMOS_PMOSDummy_length=None,  # None/Value
        _PMOS_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

            # Nbody
        _PMOS_Nbody_NumCont=2,  # Number
        _PMOS_Nbody_Xlvtdown2Ndoby=None,  # Number/None(Minimum)

        # PMOS and NMOS Height
        _PMOSXvt2NMOSXvt=1000,  # number

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
    LayoutObj = _Xgate(_DesignParameter=None, _Name=cellname)
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
    Checker.lib_deletion()
    # Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()

    ''' Check Time'''
    elapsed_time = time.time() - start_time
    m, s = divmod(elapsed_time, 60)
    h, m = divmod(m, 60)

    print('#############################      Finished      ################################')
# end of 'main():' ---------------------------------------------------------------------------------------------
