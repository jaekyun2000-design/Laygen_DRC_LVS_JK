
## Import Basic Modules
    ## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

    ## Library
import copy
import time

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A03_NmosWithDummy_KJH4


## Define Class
class _Tr1(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(

        # Tr1
        _Tr1_NMOSNumberofGate    =   12,     #number
        _Tr1_NMOSChannelWidth    =   1000,   #number
        _Tr1_NMOSChannellength   =   30,     #number
        _Tr1_GateSpacing         =   222,   #None/number
        _Tr1_SDWidth             =   None,   #None/number
        _Tr1_XVT                 =   'RVT',  #'XVT' ex)SLVT LVT RVT HVT
        _Tr1_PCCrit              =   True,   #None/True

            # Source_node_ViaM1M2
        _Tr1_Source_Via_TF       =   False,  #True/False

            # Drain_node_ViaM1M2
        _Tr1_Drain_Via_TF        =   False,  #True/False

            # POLY dummy setting
        _Tr1_NMOSDummy           =   True,  # TF
                # if _PMOSDummy == True
        _Tr1_NMOSDummy_length    =   None,  # None/Value
        _Tr1_NMOSDummy_placement =   None,  # None/'Up'/'Dn'/

        # Input/Output node
        # INPUT node
        _Inputnode_Metal_layer=6,  # number
        _Inputnode_width=600,  # number

        # OUTPUT node
        _Outputnode_Metal_layer=6,  # number
        _Outputnode_width=600,  # number

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

                                  # Tr1 : Ref Design
                                  _Tr1_NMOSNumberofGate=12,  # number
                                  _Tr1_NMOSChannelWidth=1000,  # number
                                  _Tr1_NMOSChannellength=30,  # number
                                  _Tr1_GateSpacing=222,  # None/number
                                  _Tr1_SDWidth=None,  # None/number
                                  _Tr1_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
                                  _Tr1_PCCrit=True,  # None/True

                                  # Source_node_ViaM1M2
                                  _Tr1_Source_Via_TF=False,  # True/False

                                  # Drain_node_ViaM1M2
                                  _Tr1_Drain_Via_TF=False,  # True/False

                                  # POLY dummy setting
                                  _Tr1_NMOSDummy=True,  # TF
                                  # if _PMOSDummy == True
                                  _Tr1_NMOSDummy_length=None,  # None/Value
                                  _Tr1_NMOSDummy_placement=None,  # None/'Up'/'Dn'/


                                  # Input/Output node
                                    # INPUT node
                                  _Inputnode_Metal_layer=6,  # number
                                  _Inputnode_width=600,  # number

                                    # OUTPUT node
                                  _Outputnode_Metal_layer=6,  # number
                                  _Outputnode_width=600,  # number

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


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr1, nfettw
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Tr1, nfettw: Sref Gen.
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A03_NmosWithDummy_KJH4._NmosWithDummy_KJH3._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOSNumberofGate']     =   _Tr1_NMOSNumberofGate
        _Caculation_Parameters['_NMOSChannelWidth']     =   _Tr1_NMOSChannelWidth
        _Caculation_Parameters['_NMOSChannellength']    =   _Tr1_NMOSChannellength
        _Caculation_Parameters['_GateSpacing']          =   _Tr1_GateSpacing
        _Caculation_Parameters['_SDWidth']              =   _Tr1_SDWidth
        _Caculation_Parameters['_XVT']                  =   _Tr1_XVT
        _Caculation_Parameters['_PCCrit']               =   _Tr1_PCCrit

        _Caculation_Parameters['_Source_Via_TF']        =   _Tr1_Source_Via_TF

        _Caculation_Parameters['_Drain_Via_TF']         =   _Tr1_Drain_Via_TF

        _Caculation_Parameters['_NMOSDummy']            =   _Tr1_NMOSDummy

        _Caculation_Parameters['_NMOSDummy_length']     =   _Tr1_NMOSDummy_length
        _Caculation_Parameters['_NMOSDummy_placement']  =   _Tr1_NMOSDummy_placement

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Nmos'] = self._SrefElementDeclaration(_DesignObj=A03_NmosWithDummy_KJH4._NmosWithDummy_KJH3(_DesignParameter=None, _Name='{}:SRF_Nmos'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Nmos']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos']['_XYCoordinates'] = [[0, 0]]




        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Input_node
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Input_node: M1 Vtc
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Tr1_Source_Vtc_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Nmos','BND_Met1Layer_Source')
        tmp2 = self.get_outter_KJH4('SRF_Nmos')
        output_element = tmp2['_Mostup']['index']
        output_elementname = tmp2['_Layercoord'][output_element[0]][1]
        outter_coord = tmp2['_Mostup']['coord']

        self._DesignParameter['BND_Tr1_Source_Vtc_M1']['_YWidth'] = _Inputnode_width + abs( outter_coord[0] - tmp1[0][0][0]['_XY_up'][1] )

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Nmos','BND_Met1Layer_Source')
        self._DesignParameter['BND_Tr1_Source_Vtc_M1']['_XWidth'] = tmp[0][0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Tr1_Source_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Tr1_Source_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        tmp = self.get_param_KJH4('SRF_Nmos','BND_Met1Layer_Source')
        for i in range(0,len(tmp[0])):
                            ## Calculate
                                ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Nmos','BND_Met1Layer_Source')
            target_coord = tmp1[0][i][0]['_XY_up_left']
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Tr1_Source_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_down_left']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Tr1_Source_Vtc_M1')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Tr1_Source_Vtc_M1']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Input_node: ViaM1Mx
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = _Inputnode_Metal_layer
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Tr1_Source_ViaM1Mx'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None, _Name='{}:SRF_Tr1_Source_ViaM1Mx'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Tr1_Source_ViaM1Mx']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Tr1_Source_ViaM1Mx']['_Angle'] = 0

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        tmp = self.get_param_KJH4('SRF_Nmos','BND_Met1Layer_Source')
        _COX, _COY = self._CalculateNumViaByXYWidth( tmp[0][0][0]['_Xwidth'], _Inputnode_width , 'MinEnclosureX')

            ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Tr1_Source_ViaM1Mx']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Tr1_Source_ViaM1Mx']['_XYCoordinates'] = [[0, 0]]

        tmp = self.get_param_KJH4('BND_Tr1_Source_Vtc_M1')
        for i in range(0,len(tmp)):
                    ## Calculate
                        ## Target_coord
            tmp1 = self.get_param_KJH4('BND_Tr1_Source_Vtc_M1')
            target_coord = tmp1[i][0]['_XY_up']
                        ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_Tr1_Source_ViaM1Mx','SRF_ViaM1M2','BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_up']
                        ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Tr1_Source_ViaM1Mx')
            Scoord = tmp3[0][0]['_XY_origin']
                        ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Tr1_Source_ViaM1Mx']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr1 Source and Drain ground shielding
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr1 Source and Drain ground shielding: Vtc
            ## Boundary_element Generation
        ## Pre-defined
        ground_vtc_last_layer = 3  # 1 to last layer
        ground_vtc_length_margin = 100

        for i in range(1,ground_vtc_last_layer+1):
                    ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_Ground_Vtc_M{}'.format(i)] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}'.format(i)][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}'.format(i)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
            )

                    ## Define Boundary_element _YWidth
            tmp1 = self.get_param_KJH4('BND_Tr1_Source_Vtc_M1')
            tmp2 = self.get_param_KJH4('SRF_Nmos','BND_POLayer')
            self._DesignParameter['BND_Ground_Vtc_M{}'.format(i)]['_YWidth'] = abs( tmp1[0][0]['_XY_up'][1] - tmp2[0][0][0]['_XY_down'][1] ) + 2 * ground_vtc_length_margin

                    ## Define Boundary_element _XWidth
            self._DesignParameter['BND_Ground_Vtc_M{}'.format(i)]['_XWidth'] = 50

                    ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_Ground_Vtc_M{}'.format(i)]['_XYCoordinates'] = [[0, 0]]

                        ## Calculate Sref XYcoord
            tmpXY = []

            tmp = self.get_param_KJH4('SRF_Nmos','BND_POLayer')
            for j in range(0,len(tmp[0])):
                                ## Calculate
                                    ## Target_coord: _XY_type1
                                        ## x
                tmp1_1 = self.get_param_KJH4('SRF_Nmos','BND_POLayer')
                target_coordx = tmp1_1[0][j][0]['_XY_cent'][0]
                                        ## y
                tmp1_2 = self.get_param_KJH4('BND_Tr1_Source_Vtc_M1')
                target_coordy = tmp1_2[0][0]['_XY_up'][1]

                target_coord = [target_coordx,target_coordy]

                                    ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('BND_Ground_Vtc_M{}'.format(i))
                approaching_coord = tmp2[0][0]['_XY_up']
                                    ## Sref coord
                tmp3 = self.get_param_KJH4('BND_Ground_Vtc_M{}'.format(i))
                Scoord = tmp3[0][0]['_XY_origin']
                                    ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                New_Scoord[1] = New_Scoord[1] + ground_vtc_length_margin
                tmpXY.append(New_Scoord)
                                ## Define coordinates
            self._DesignParameter['BND_Ground_Vtc_M{}'.format(i)]['_XYCoordinates'] = tmpXY
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr1 Source and Drain ground shielding: Hrz

        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        ## Pre-defined
        Hrz_metal_last_layer = 4
        Hrz_metal_Layer = [1, Hrz_metal_last_layer]

        for i in Hrz_metal_Layer:
            self._DesignParameter['BND_Ground_Hrz_M{}'.format(i)] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL{}'.format(i)][0],
                _Datatype=DesignParameters._LayerMapping['METAL{}'.format(i)][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )

            ## Define Boundary_element _YWidth
            self._DesignParameter['BND_Ground_Hrz_M{}'.format(i)]['_YWidth'] = 50

            ## Define Boundary_element _XWidth
            tmp = self.get_outter_KJH4('SRF_Nmos')
            self._DesignParameter['BND_Ground_Hrz_M{}'.format(i)]['_XWidth'] = abs(tmp['_Mostleft']['coord'][0] - tmp['_Mostright']['coord'][0])

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_Ground_Hrz_M{}'.format(i)]['_XYCoordinates'] = [[0, 0]]

            tmpXY =[]
                ## Calculate
                    ## Target_coord: _XY_type1
                                    ## x
            tmp1_1 = tmp = self.get_outter_KJH4('SRF_Nmos')
            target_coordx = tmp1_1['_Mostleft']['coord'][0]
                                    ## y
            tmp1_2 = self.get_param_KJH4('BND_Ground_Vtc_M1')
            target_coordy = tmp1_2[0][0]['_XY_up'][1]

            target_coord = [target_coordx,target_coordy]

                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Ground_Hrz_M{}'.format(i))
            approaching_coord = tmp2[0][0]['_XY_down_left']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Ground_Hrz_M{}'.format(i))
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                            ## Define coordinates
            self._DesignParameter['BND_Ground_Hrz_M{}'.format(i)]['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr1 Source and Drain ground shielding: ViaM1M4
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = Hrz_metal_Layer[0]
        _Caculation_Parameters['_Layer2'] = Hrz_metal_Layer[1]
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        ## Sref ViaX declaration
        self._DesignParameter['SRF_Ground_ViaM1Mx'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None,
            _Name='{}:SRF_Ground_ViaM1Mx'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_Ground_ViaM1Mx']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_Ground_ViaM1Mx']['_Angle'] = 0

        ## Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH4('BND_Ground_Hrz_M{}'.format(Hrz_metal_Layer[0]))
        tmp2 = self.get_param_KJH4('BND_Ground_Hrz_M{}'.format(Hrz_metal_Layer[1]))
        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

        ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

        ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Ground_ViaM1Mx']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_Ground_ViaM1Mx']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_Ground_Hrz_M1')
        target_coord = tmp1[0][0]['_XY_cent']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Ground_ViaM1Mx','SRF_ViaM1M2','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Ground_ViaM1Mx')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_Ground_ViaM1Mx']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Gate_combine
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Gate_combine: Vtc
            ##Pre-defined
        Poly_vtc_margin = 100

            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Gate_Vtc_M0'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['POLY'][0],
        _Datatype=DesignParameters._LayerMapping['POLY'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_Ground_Hrz_M1')
        tmp2= self.get_param_KJH4('SRF_Nmos','BND_POLayer')
        self._DesignParameter['BND_Gate_Vtc_M0']['_YWidth'] = abs( tmp1[0][0]['_XY_up'][1] - tmp2[0][0][0]['_XY_up'][1]  ) + Poly_vtc_margin

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Nmos', 'BND_POLayer')
        self._DesignParameter['BND_Gate_Vtc_M0']['_XWidth'] = tmp[0][0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Gate_Vtc_M0']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []

        tmp = self.get_param_KJH4('SRF_Nmos', 'BND_POLayer')
        for i in range(0,len(tmp[0])):
                            ## Calculate
                                ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Nmos', 'BND_POLayer')
            target_coord = tmp1[0][i][0]['_XY_up_left']
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Gate_Vtc_M0')
            approaching_coord = tmp2[0][0]['_XY_down_left']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Gate_Vtc_M0')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Gate_Vtc_M0']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Gate_combine: POLY Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Gate_Hrz_M0'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['POLY'][0],
        _Datatype=DesignParameters._LayerMapping['POLY'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Gate_Hrz_M0']['_YWidth'] = 50

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('BND_Gate_Vtc_M0')
        print(_Tr1_NMOSNumberofGate)
        print(_Tr1_NMOSChannelWidth)
        if (_Tr1_NMOSNumberofGate == 1 and _Tr1_NMOSChannelWidth < 201) :
            self._DesignParameter['BND_Gate_Hrz_M0']['_XWidth'] = 300
        else :
            self._DesignParameter['BND_Gate_Hrz_M0']['_XWidth'] = max(abs( tmp[-1][0]['_XY_right'][0] - tmp[0][0]['_XY_left'][0] ),200)

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Gate_Hrz_M0']['_XYCoordinates'] = [[0, 0]]

        tmpXY=[]
                    ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_Gate_Vtc_M0')
        tmp1_1 = int((tmp1[0][0]['_XY_left'][0] + tmp1[-1][0]['_XY_right'][0])/2)
        target_coord = [tmp1_1, tmp1[0][0]['_XY_up'][1]]
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Gate_Hrz_M0')
        approaching_coord = tmp2[0][0]['_XY_down']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Gate_Hrz_M0')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Gate_Hrz_M0']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Gate_combine: M3Hrz
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Gate_Hrz_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Gate_Hrz_M3']['_YWidth'] = 50

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('BND_Gate_Hrz_M0')
        self._DesignParameter['BND_Gate_Hrz_M3']['_XWidth'] = tmp[0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
        tmp = self.get_param_KJH4('BND_Gate_Hrz_M0')
        self._DesignParameter['BND_Gate_Hrz_M3']['_XYCoordinates'] = [tmp[0][0]['_XY_origin']]

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Gate_combine: ViaM0M3
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 0
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        ## Sref ViaX declaration
        self._DesignParameter['SRF_Gate_ViaM0M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None,
            _Name='{}:SRF_Gate_ViaM0M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_Gate_ViaM0M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_Gate_ViaM0M3']['_Angle'] = 0

        ## Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH4('BND_Gate_Hrz_M0')
        tmp2 = self.get_param_KJH4('BND_Gate_Hrz_M3')
        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

        ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

        ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Gate_ViaM0M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_Gate_ViaM0M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1 = self.get_param_KJH4('BND_Gate_Hrz_M0')
        target_coord = tmp1[0][0]['_XY_cent']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Gate_ViaM0M3','SRF_ViaM0M1','BND_POLayer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Gate_ViaM0M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_Gate_ViaM0M3']['_XYCoordinates'] = tmpXY



        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Output_node
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Output_node: M1 Vtc
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Tr1_Drain_Vtc_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Nmos','BND_Met1Layer_Drain')
        tmp2 = self.get_outter_KJH4('SRF_Nmos')
        output_element = tmp2['_Mostdown']['index']
        output_elementname = tmp2['_Layercoord'][output_element[0]][1]
        outter_coord = tmp2['_Mostdown']['coord']

        self._DesignParameter['BND_Tr1_Drain_Vtc_M1']['_YWidth'] = _Outputnode_width + abs( outter_coord[0] - tmp1[0][0][0]['_XY_down'][1] )

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Nmos','BND_Met1Layer_Drain')
        self._DesignParameter['BND_Tr1_Drain_Vtc_M1']['_XWidth'] = tmp[0][0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Tr1_Drain_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Tr1_Drain_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        tmp = self.get_param_KJH4('SRF_Nmos','BND_Met1Layer_Drain')
        for i in range(0,len(tmp[0])):
                            ## Calculate
                                ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Nmos','BND_Met1Layer_Drain')
            target_coord = tmp1[0][i][0]['_XY_down_left']
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Tr1_Drain_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_up_left']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Tr1_Drain_Vtc_M1')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Tr1_Drain_Vtc_M1']['_XYCoordinates'] = tmpXY
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Output_node: ViaM1Mx
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = _Outputnode_Metal_layer
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Tr1_Drain_ViaM1Mx'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None, _Name='{}:SRF_Tr1_Drain_ViaM1Mx'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Tr1_Drain_ViaM1Mx']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Tr1_Drain_ViaM1Mx']['_Angle'] = 0

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        tmp = self.get_param_KJH4('SRF_Nmos','BND_Met1Layer_Drain')
        _COX, _COY = self._CalculateNumViaByXYWidth( tmp[0][0][0]['_Xwidth'], _Inputnode_width , 'MinEnclosureX')

            ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Tr1_Drain_ViaM1Mx']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Tr1_Drain_ViaM1Mx']['_XYCoordinates'] = [[0, 0]]

        tmp = self.get_param_KJH4('BND_Tr1_Drain_Vtc_M1')
        for i in range(0,len(tmp)):
                    ## Calculate
                        ## Target_coord
            tmp1 = self.get_param_KJH4('BND_Tr1_Drain_Vtc_M1')
            target_coord = tmp1[i][0]['_XY_down']
                        ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_Tr1_Drain_ViaM1Mx','SRF_ViaM1M2','BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_down']
                        ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Tr1_Drain_ViaM1Mx')
            Scoord = tmp3[0][0]['_XY_origin']
                        ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Tr1_Drain_ViaM1Mx']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Delete
        #del self._DesignParameter['BND_Inputnode']
        #del self._DesignParameter['BND_Outputnode']


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
    libname = 'Proj_ADC_C00_Tr1Tr2_tr1_test6'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'C00_00_Tr1_v0_76'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

        # Tr1
        _Tr1_NMOSNumberofGate    =   3,     #number
        _Tr1_NMOSChannelWidth    =   100,   #number
        _Tr1_NMOSChannellength   =   30,     #number
        _Tr1_GateSpacing         =   222,    #None/number
        _Tr1_SDWidth             =   None,   #None/number
        _Tr1_XVT                 =   'HVT',  #'XVT' ex)SLVT LVT RVT HVT
        _Tr1_PCCrit              =   True,   #None/True

            # Source_node_ViaM1M2
        _Tr1_Source_Via_TF       =   False,  #True/False

            # Drain_node_ViaM1M2
        _Tr1_Drain_Via_TF        =   False,  #True/False

            # POLY dummy setting
        _Tr1_NMOSDummy           =   True,  # TF
                # if _PMOSDummy == True
        _Tr1_NMOSDummy_length    =   None,  # None/Value
        _Tr1_NMOSDummy_placement =   'Dn',  # None/'Up'/'Dn'/

        # Input/Output node
            #INPUT node
            _Inputnode_Metal_layer = 6, # number
            _Inputnode_width = 600, # number

            # OUTPUT node
            _Outputnode_Metal_layer = 6,  # number
            _Outputnode_width = 600,  # number
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
    LayoutObj = _Tr1(_DesignParameter=None, _Name=cellname)
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

    ''' Check Time'''
    elapsed_time = time.time() - start_time
    m, s = divmod(elapsed_time, 60)
    h, m = divmod(m, 60)

    print('#############################      Finished      ################################')
# end of 'main():' ---------------------------------------------------------------------------------------------
