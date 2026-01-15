
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
from Proj_RCDAC_ADC2024_V6_IJK.KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A14_Mosfet_KJH3


## Define Class
class _Tr2(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
#TR1
    # Physical dimension
    _Tr2_NumberofGate	            = 5,       # Number
    _Tr2_ChannelWidth	            = 100,     # Number
    _Tr2_ChannelLength	            = 30,       # Number
    _Tr2_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# Input/Output node
    # INPUT node
    _Inputnode_width = 500,  # number


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
#TR1
    # Physical dimension
    _Tr2_NumberofGate	            = 5,       # Number
    _Tr2_ChannelWidth	            = 100,     # Number
    _Tr2_ChannelLength	            = 30,       # Number
    _Tr2_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# Input/Output node
    # INPUT node
    _Inputnode_width = 500,  # number

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


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr2, nfettw
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Tr2, nfettw: Sref Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A14_Mosfet_KJH3._Mosfet._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_MosType'] = 'NMOS'
        _Caculation_Parameters['_MosUpDn'] = 'Up'

        _Caculation_Parameters['_NumberofGate']     = _Tr2_NumberofGate
        _Caculation_Parameters['_ChannelWidth']     = _Tr2_ChannelWidth
        _Caculation_Parameters['_ChannelLength']    = _Tr2_ChannelLength
        _Caculation_Parameters['_GateSpacing']      = 100
        _Caculation_Parameters['_SDWidth']          = None
        _Caculation_Parameters['_XVT']              = _Tr2_XVT
        _Caculation_Parameters['_PCCrit']           = True

        _Caculation_Parameters['_Source_Via_TF']                = False
        _Caculation_Parameters['_Source_Via_Close2POpin_TF']    = None
        _Caculation_Parameters['_Source_Comb_TF']               = None
        _Caculation_Parameters['_Source_Comb_POpinward_TF']     = None
        _Caculation_Parameters['_Source_Comb_Length']           = None

        _Caculation_Parameters['_Drain_Via_TF']                 = False
        _Caculation_Parameters['_Drain_Via_Close2POpin_TF']     = None
        _Caculation_Parameters['_Drain_Comb_TF']                = None
        _Caculation_Parameters['_Drain_Comb_POpinward_TF']      = None
        _Caculation_Parameters['_Drain_Comb_Length']            = None

        _Caculation_Parameters['_PODummy_TF']                   = True
        _Caculation_Parameters['_PODummy_Length']               = None
        _Caculation_Parameters['_PODummy_Placement']            = 'Up'

        _Caculation_Parameters['_Xvt_MinExten_TF']              = True
        _Caculation_Parameters['_Xvt_Placement']                = 'Dn'

        _Caculation_Parameters['_POGate_Comb_TF']               = False
        _Caculation_Parameters['_POGate_Comb_length']           = None
        _Caculation_Parameters['_POGate_Via_TF']                = None
        _Caculation_Parameters['_POGate_ViaMxMx']               = None

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Nmos'] = self._SrefElementDeclaration(_DesignObj=A14_Mosfet_KJH3._Mosfet(_DesignParameter=None, _Name='{}:SRF_Nmos'.format(_Name)))[0]

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
        self._DesignParameter['BND_Tr2_Drain_Vtc_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Nmos','BND_Drain_M1')
        tmp_Outter_Nmos = self.get_outter_KJH4('SRF_Nmos')
        output_element = tmp_Outter_Nmos['_Mostup']['index']
        output_elementname = tmp_Outter_Nmos['_Layercoord'][output_element[0]][1]
        outter_coord = tmp_Outter_Nmos['_Mostup']['coord']

        self._DesignParameter['BND_Tr2_Drain_Vtc_M1']['_YWidth'] = _Inputnode_width + abs( outter_coord[1] - tmp1[0][0][0]['_XY_up'][1] )

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Nmos','BND_Drain_M1')
        self._DesignParameter['BND_Tr2_Drain_Vtc_M1']['_XWidth'] = tmp[0][0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Tr2_Drain_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Tr2_Drain_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

        tmp = self.get_param_KJH4('SRF_Nmos','BND_Drain_M1')
        tmp2 = self.get_param_KJH4('BND_Tr2_Drain_Vtc_M1')
        tmp3 = self.get_param_KJH4('BND_Tr2_Drain_Vtc_M1')
        for i in range(0,len(tmp[0])):
                            ## Calculate
                                ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Nmos','BND_Drain_M1')
            target_coord = tmp1[0][i][0]['_XY_up_left']
                                ## Approaching_coord: _XY_type2
            # tmp2 = self.get_param_KJH4('BND_Tr2_Drain_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_down_left']
                                ## Sref coord
            # tmp3 = self.get_param_KJH4('BND_Tr2_Drain_Vtc_M1')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Tr2_Drain_Vtc_M1']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Input_node: ViaM1Mx
        _Inputnode_Metal_layer = 6
        ## Sref generation: ViaX
        ViaName = 'SRF_Tr2_Drain_ViaM1Mx'
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = _Inputnode_Metal_layer
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

            ## Sref ViaX declaration
        self._DesignParameter[ViaName] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:{}'.format(_Name,ViaName)))[0]

            ## Define Sref Relection
        self._DesignParameter[ViaName]['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter[ViaName]['_Angle'] = 0

            ## Calcuate Overlapped XYcoord
        tmp = self.get_param_KJH4('SRF_Nmos','BND_Drain_M1')
        _COX, _COY = self._CalculateNumViaByXYWidth( tmp[0][0][0]['_Xwidth'], _Inputnode_width , 'MinEnclosureX')

            ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter[ViaName]['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter[ViaName]['_XYCoordinates'] = [[0, 0]]

        tmp = self.get_param_KJH4('BND_Tr2_Drain_Vtc_M1')
        tmp2 = self.get_param_KJH4('SRF_Tr2_Drain_ViaM1Mx', 'SRF_ViaM1M2', 'BND_Met1Layer')
        for i in range(0,len(tmp)):
                    ## Calculate
                        ## Target_coord
            tmp1 = self.get_param_KJH4('BND_Tr2_Drain_Vtc_M1')
            target_coord = tmp1[i][0]['_XY_up']
                        ## Approaching_coord
            # tmp2 = self.get_param_KJH4('SRF_Tr2_Drain_ViaM1Mx','SRF_ViaM1M2','BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_up']
                        ## Sref coord
            tmp3 = self.get_param_KJH4(ViaName)
            Scoord = tmp3[0][0]['_XY_origin']
                        ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter[ViaName]['_XYCoordinates'] = tmpXY



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
        tmp1 = self.get_param_KJH4('BND_Tr2_Drain_Vtc_M1')
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
        tmp2 = self.get_param_KJH4('BND_Gate_Vtc_M0')
        tmp3 = self.get_param_KJH4('BND_Gate_Vtc_M0')

        for i in range(0,len(tmp[0])):
                            ## Calculate
                                ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Nmos', 'BND_POLayer')
            target_coord = tmp1[0][i][0]['_XY_up_left']
                                ## Approaching_coord: _XY_type2
            # tmp2 = self.get_param_KJH4('BND_Gate_Vtc_M0')
            approaching_coord = tmp2[0][0]['_XY_down_left']
                                ## Sref coord
            # tmp3 = self.get_param_KJH4('BND_Gate_Vtc_M0')
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
        ViaName = 'SRF_Gate_ViaM0M3'
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 0
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

            ## Sref ViaX declaration
        self._DesignParameter[ViaName] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:{}'.format(_Name,ViaName)))[0]

            ## Define Sref Relection
        self._DesignParameter[ViaName]['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter[ViaName]['_Angle'] = 0

            ## Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH4('BND_Gate_Hrz_M0')
        tmp2 = self.get_param_KJH4('BND_Gate_Hrz_M3')
        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY' or 'SameEnclosure'
        _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

            ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = max(2,_COX)
        _Caculation_Parameters['_COY'] = _COY

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter[ViaName]['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter[ViaName]['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        tmp1 = self.get_param_KJH4('BND_Gate_Hrz_M0')
        target_coord = tmp1[0][0]['_XY_cent']
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Gate_ViaM0M3','SRF_ViaM0M1','BND_POLayer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                    ## Sref coord
        tmp3 = self.get_param_KJH4(ViaName)
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter[ViaName]['_XYCoordinates'] = tmpXY

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
    libname = 'Proj_ZZ01_C00_01_Tr2_fixed'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'C00_01_Tr2_v0_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

#TR2
    # Physical dimension
    _Tr2_NumberofGate	            = 5,       # Number
    _Tr2_ChannelWidth	            = 700,     # Number
    _Tr2_ChannelLength	            = 30,       # Number
    _Tr2_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# Input/Output node
    # INPUT node
    _Inputnode_width = 500,  # number

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
    LayoutObj = _Tr2(_DesignParameter=None, _Name=cellname)
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
    Checker.lib_deletion()
    Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()

    print('#############################      Finished      ################################')
    print('{} Hours   {} minutes   {} seconds'.format(h, m, s))
# end of 'main():' ---------------------------------------------------------------------------------------------
