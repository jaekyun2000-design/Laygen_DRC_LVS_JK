
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
from KJH91_Projects.Project_ADC.Layoutgen_code.E01_ComparatorWtLatch_YJH import E01_02_NAND_YJH
from KJH91_Projects.Project_ADC.Layoutgen_code.E01_ComparatorWtLatch_YJH import E01_00_Inverter
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3


## Define Class
class _AND(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
        _AND_NAND_NMOS_ChannelWidth=None,
        _AND_NAND_NMOS_ChannelLength=None,
        _AND_NAND_NMOS_NumberofGate=None,
        _AND_NAND_NMOS_XVT=None,

        _AND_NAND_PMOS_ChannelWidth=None,
        _AND_NAND_PMOS_ChannelLength=None,
        _AND_NAND_PMOS_NumberofGate=None,
        _AND_NAND_PMOS_XVT=None,

        _AND_Inv_NMOS_ChannelWidth=None,
        _AND_Inv_NMOS_ChannelLength=None,
        _AND_Inv_NMOS_NumberofGate=None,
        _AND_Inv_NMOS_XVT=None,
        _AND_Inv_NMOS_POGate_Comb_length=None,

        _AND_Inv_PMOS_ChannelWidth=None,
        _AND_Inv_PMOS_ChannelLength=None,
        _AND_Inv_PMOS_NumberofGate=None,
        _AND_Inv_PMOS_XVT=None,
        _AND_Inv_PMOS_POGate_Comb_length=None,

        # PowerRail Placement
        _AND_NMOS_Pbody_NumCont=None,
        _AND_NMOS_Pbody_XvtTop2Pbody=None,
        _AND_PMOS_Nbody_NumCont=None,
        _AND_PMOS_Nbody_Xvtdown2Nbody=None,
        _AND_PMOSXvt2NMOSXvt=None,
    )

    ## Initially Generated _DesignParameter
    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
            _Name=self._NameDeclaration(_Name=_Name),
            _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
            _XYcoordAsCent=dict(_XYcoordAsCent=0),  # downleft_coordination == 0
            )

    ## DesignParameter Calculation
    def _CalculateDesignParameter(self,
                                  _AND_NAND_NMOS_ChannelWidth=None,
                                  _AND_NAND_NMOS_ChannelLength=None,
                                  _AND_NAND_NMOS_NumberofGate=None,
                                  _AND_NAND_NMOS_XVT=None,

                                  _AND_NAND_PMOS_ChannelWidth=None,
                                  _AND_NAND_PMOS_ChannelLength=None,
                                  _AND_NAND_PMOS_NumberofGate=None,
                                  _AND_NAND_PMOS_XVT=None,

                                  _AND_Inv_NMOS_ChannelWidth=None,
                                  _AND_Inv_NMOS_ChannelLength=None,
                                  _AND_Inv_NMOS_NumberofGate=None,
                                  _AND_Inv_NMOS_XVT=None,
                                  _AND_Inv_NMOS_POGate_Comb_length=None,

                                  _AND_Inv_PMOS_ChannelWidth=None,
                                  _AND_Inv_PMOS_ChannelLength=None,
                                  _AND_Inv_PMOS_NumberofGate=None,
                                  _AND_Inv_PMOS_XVT=None,
                                  _AND_Inv_PMOS_POGate_Comb_length=None,

                                  # PowerRail Placement
                                  _AND_NMOS_Pbody_NumCont=None,
                                  _AND_NMOS_Pbody_XvtTop2Pbody=None,
                                  _AND_PMOS_Nbody_NumCont=None,
                                  _AND_PMOS_Nbody_Xvtdown2Nbody=None,
                                  _AND_PMOSXvt2NMOSXvt=None,
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


        ######
        ## NAND SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_PMOS_power_v2._PMOS_POWER._ParametersForDesignCalculation)
        _Calculation_Parameters = copy.deepcopy(E01_02_NAND_YJH._NAND._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_PMOSPOWER_PbodyContact_1_Length']  = _PMOSPOWER_PbodyContact_1_Length

        _Calculation_Parameters['_NMOSA_NMOSNumberofGate'] = _AND_NAND_NMOS_NumberofGate
        _Calculation_Parameters['_NMOSA_NMOSChannelWidth'] = _AND_NAND_NMOS_ChannelWidth
        _Calculation_Parameters['_NMOSA_NMOSChannellength'] = _AND_NAND_NMOS_ChannelLength
        _Calculation_Parameters['_NMOSA_GateSpacing'] = None
        _Calculation_Parameters['_NMOSA_SDWidth'] = None
        _Calculation_Parameters['_NMOSA_XVT'] = _AND_NAND_NMOS_XVT
        _Calculation_Parameters['_NMOSA_PCCrit'] = True
        _Calculation_Parameters['_NMOSA_Source_Via_TF'] = True
        _Calculation_Parameters['_NMOSA_Drain_Via_TF'] = True
        _Calculation_Parameters['_NMOSA_NMOSDummy'] = True
        _Calculation_Parameters['_NMOSA_NMOSDummy_length'] = None
        _Calculation_Parameters['_NMOSA_NMOSDummy_placement'] = None
        _Calculation_Parameters['_NMOSB_NMOSNumberofGate'] = _AND_NAND_NMOS_NumberofGate
        _Calculation_Parameters['_NMOSB_NMOSChannelWidth'] = _AND_NAND_NMOS_ChannelWidth
        _Calculation_Parameters['_NMOSB_NMOSChannellength'] = _AND_NAND_NMOS_ChannelLength
        _Calculation_Parameters['_NMOSB_GateSpacing'] = None
        _Calculation_Parameters['_NMOSB_SDWidth'] = None
        _Calculation_Parameters['_NMOSB_XVT'] = _AND_NAND_NMOS_XVT
        _Calculation_Parameters['_NMOSB_PCCrit'] = True
        _Calculation_Parameters['_NMOSB_Source_Via_TF'] = False
        _Calculation_Parameters['_NMOSB_Drain_Via_TF'] = True
        _Calculation_Parameters['_NMOSB_NMOSDummy'] = True
        _Calculation_Parameters['_NMOSB_NMOSDummy_length'] = None
        _Calculation_Parameters['_NMOSB_NMOSDummy_placement'] = None
        _Calculation_Parameters['_NMOSAB_Pbody_NumCont'] = _AND_NMOS_Pbody_NumCont
        _Calculation_Parameters['_NMOSAB_Pbody_XlvtTop2Pdoby'] = _AND_NMOS_Pbody_XvtTop2Pbody

        _Calculation_Parameters['_PMOSA_PMOSNumberofGate'] = _AND_NAND_PMOS_NumberofGate
        _Calculation_Parameters['_PMOSA_PMOSChannelWidth'] = _AND_NAND_PMOS_ChannelWidth
        _Calculation_Parameters['_PMOSA_PMOSChannellength'] = _AND_NAND_PMOS_ChannelLength
        _Calculation_Parameters['_PMOSA_GateSpacing'] = None
        _Calculation_Parameters['_PMOSA_SDWidth'] = None
        _Calculation_Parameters['_PMOSA_XVT'] = _AND_NAND_PMOS_XVT
        _Calculation_Parameters['_PMOSA_PCCrit'] = True
        _Calculation_Parameters['_PMOSA_Source_Via_TF'] = False # default
        _Calculation_Parameters['_PMOSA_Drain_Via_TF'] = True
        _Calculation_Parameters['_PMOSA_PMOSDummy'] = True
        _Calculation_Parameters['_PMOSA_PMOSDummy_length'] = None
        _Calculation_Parameters['_PMOSA_PMOSDummy_placement'] = None
        _Calculation_Parameters['_PMOSB_PMOSNumberofGate'] = _AND_NAND_PMOS_NumberofGate
        _Calculation_Parameters['_PMOSB_PMOSChannelWidth'] = _AND_NAND_PMOS_ChannelWidth
        _Calculation_Parameters['_PMOSB_PMOSChannellength'] = _AND_NAND_PMOS_ChannelLength
        _Calculation_Parameters['_PMOSB_GateSpacing'] = None
        _Calculation_Parameters['_PMOSB_SDWidth'] = None
        _Calculation_Parameters['_PMOSB_XVT'] = _AND_NAND_PMOS_XVT
        _Calculation_Parameters['_PMOSB_PCCrit'] = True
        _Calculation_Parameters['_PMOSB_Source_Via_TF'] = False # default
        _Calculation_Parameters['_PMOSB_Drain_Via_TF'] = True
        _Calculation_Parameters['_PMOSB_PMOSDummy'] = True
        _Calculation_Parameters['_PMOSB_PMOSDummy_length'] = None
        _Calculation_Parameters['_PMOSB_PMOSDummy_placement'] = None
        _Calculation_Parameters['_PMOSAB_Nbody_NumCont'] = _AND_PMOS_Nbody_NumCont
        _Calculation_Parameters['_PMOSAB_Nbody_Xlvtdown2Ndoby'] = _AND_PMOS_Nbody_Xvtdown2Nbody
        _Calculation_Parameters['_PMOSXvt2NMOSXvt'] = _AND_PMOSXvt2NMOSXvt

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_NAND'] = self._SrefElementDeclaration(_DesignObj=E01_02_NAND_YJH._NAND(_DesignParameter=None, _Name='{}:SRF_NAND'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_NAND']['_Reflect'] = [1, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NAND']['_Angle'] = 180

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NAND']['_DesignObj']._CalculateDesignParameter(**_Calculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NAND']['_XYCoordinates'] = [[0, 0]]


        _Caculation_Parameters = copy.deepcopy(E01_00_Inverter._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType'] = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn'] = 'Up'
        _Caculation_Parameters['_NMOS_NumberofGate'] = _AND_Inv_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth'] = _AND_Inv_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength'] = _AND_Inv_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing'] = None
        _Caculation_Parameters['_NMOS_SDWidth'] = None
        _Caculation_Parameters['_NMOS_XVT'] = _AND_Inv_NMOS_XVT
        _Caculation_Parameters['_NMOS_PCCrit'] = True
        _Caculation_Parameters['_NMOS_Source_Via_TF'] = False
        _Caculation_Parameters['_NMOS_Source_Via_Close2POpin_TF'] = False
        _Caculation_Parameters['_NMOS_Source_Comb_TF'] = False
        _Caculation_Parameters['_NMOS_Source_Comb_POpinward_TF'] = False
        _Caculation_Parameters['_NMOS_Source_Comb_Length'] = None
        _Caculation_Parameters['_NMOS_Drain_Via_TF'] = True
        _Caculation_Parameters['_NMOS_Drain_Via_Close2POpin_TF'] = True
        _Caculation_Parameters['_NMOS_Drain_Comb_TF'] = True
        _Caculation_Parameters['_NMOS_Drain_Comb_POpinward_TF'] = True
        _Caculation_Parameters['_NMOS_Drain_Comb_Length'] = 0
        _Caculation_Parameters['_NMOS_PODummy_TF'] = True
        _Caculation_Parameters['_NMOS_PODummy_Length'] = None
        _Caculation_Parameters['_NMOS_PODummy_Placement'] = None
        _Caculation_Parameters['_NMOS_Xvt_MinExten_TF'] = False
        _Caculation_Parameters['_NMOS_Xvt_Placement'] = None
        _Caculation_Parameters['_NMOS_POGate_Comb_TF'] = True
        _Caculation_Parameters['_NMOS_POGate_Comb_length'] = _AND_Inv_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF'] = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx'] = [0, 1]

        _Caculation_Parameters['_PMOS_MosType'] = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn'] = 'Dn'
        _Caculation_Parameters['_PMOS_NumberofGate'] = _AND_Inv_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth'] = _AND_Inv_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength'] = _AND_Inv_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing'] = None
        _Caculation_Parameters['_PMOS_SDWidth'] = None
        _Caculation_Parameters['_PMOS_XVT'] = _AND_Inv_PMOS_XVT
        _Caculation_Parameters['_PMOS_PCCrit'] = True
        _Caculation_Parameters['_PMOS_Source_Via_TF'] = False
        _Caculation_Parameters['_PMOS_Source_Via_Close2POpin_TF'] = False
        _Caculation_Parameters['_PMOS_Source_Comb_TF'] = False
        _Caculation_Parameters['_PMOS_Source_Comb_POpinward_TF'] = False
        _Caculation_Parameters['_PMOS_Source_Comb_Length'] = None
        _Caculation_Parameters['_PMOS_Drain_Via_TF'] = True
        _Caculation_Parameters['_PMOS_Drain_Via_Close2POpin_TF'] = True
        _Caculation_Parameters['_PMOS_Drain_Comb_TF'] = True
        _Caculation_Parameters['_PMOS_Drain_Comb_POpinward_TF'] = True
        _Caculation_Parameters['_PMOS_Drain_Comb_Length'] = 0
        _Caculation_Parameters['_PMOS_PODummy_TF'] = True
        _Caculation_Parameters['_PMOS_PODummy_Length'] = None
        _Caculation_Parameters['_PMOS_PODummy_Placement'] = None
        _Caculation_Parameters['_PMOS_Xvt_MinExten_TF'] = False
        _Caculation_Parameters['_PMOS_Xvt_Placement'] = None
        _Caculation_Parameters['_PMOS_POGate_Comb_TF'] = True
        _Caculation_Parameters['_PMOS_POGate_Comb_length'] = _AND_Inv_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF'] = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx'] = [0,1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont'] = _AND_NMOS_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody'] = _AND_NMOS_Pbody_XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_NumCont'] = _AND_PMOS_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody'] = _AND_PMOS_Nbody_Xvtdown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt'] = _AND_PMOSXvt2NMOSXvt

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Inverter'] = self._SrefElementDeclaration(_DesignObj=E01_00_Inverter._Inverter(_DesignParameter=None, _Name='{}:SRF_Inverter'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Inverter']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inverter']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inverter']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Inverter']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1x = self.get_param_KJH4('SRF_NAND', 'SRF_Pullup', 'SRF_PMOSA', 'BND_PODummyLayer')
        tmp1y = self.get_param_KJH4('SRF_NAND','SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        target_coord = [tmp1x[0][0][0][0][0]['_XY_left'][0], tmp1y[0][0][0][0][0]['_XY_up'][1]]
                            ## Approaching_coord: _XY_type2
        tmp2x = self.get_param_KJH4('SRF_Inverter', 'SRF_NMOS', 'BND_PODummyLayer')
        tmp2y = self.get_param_KJH4('SRF_Inverter', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = [tmp2x[0][0][0][0]['_XY_left'][0], tmp2y[0][0][0][0][0]['_XY_up'][1]]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Inverter')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[0] = Scoord[0] + 96
        # Scoord[0] = Scoord[0] + 140
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['SRF_Inverter']['_XYCoordinates'] = tmpXY


        ######## NAND Output -> Inverter Routing
        #### SRF CLKBuf_Input_ViaM1M2
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

            ## Sref ViaX declaration
        self._DesignParameter['SRF_AND2Inv_ViaM1M2'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_AND2Inv_ViaM1M2'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_AND2Inv_ViaM1M2']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_AND2Inv_ViaM1M2']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_AND2Inv_ViaM1M2']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_AND2Inv_ViaM1M2']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        tmp1 = self.get_param_KJH4('SRF_Inverter','BND_Input_Vtc_M1')
        target_coord = tmp1[0][0][0]['_XY_up_left']
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_AND2Inv_ViaM1M2','SRF_ViaM1M2','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_AND2Inv_ViaM1M2')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_AND2Inv_ViaM1M2']['_XYCoordinates'] = tmpXY


        #### BND_NANDOut_Hrz_M2
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NANDOut_Hrz_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_AND2Inv_ViaM1M2','SRF_ViaM1M2', 'BND_Met2Layer')
        tmp2 = self.get_param_KJH4('SRF_NAND','BND_Out_Vtc_M2')
        self._DesignParameter['BND_NANDOut_Hrz_M2']['_YWidth'] = 50

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_NANDOut_Hrz_M2']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0]['_XY_right'][0])

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_NANDOut_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        # tmp1 = self.get_param_KJH4('SRF_CLKSampInvOut_ViaM2M3','SRF_ViaM2M3', 'BND_Met3Layer')
        target_coord = tmp1[0][0][0][0]['_XY_up_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NANDOut_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NANDOut_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_NANDOut_Hrz_M2']['_XYCoordinates'] = tmpXY







        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')



############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    Start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_YJH
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ADC_E01_ComparatorWtLatch_YJH_v1'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'E01_00_AND_v1'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
    # CLK Input Logic Gates
    _AND_NAND_NMOS_ChannelWidth=400,
    _AND_NAND_NMOS_ChannelLength=30,
    _AND_NAND_NMOS_NumberofGate=2,
    _AND_NAND_NMOS_XVT='SLVT',

    _AND_NAND_PMOS_ChannelWidth=800,
    _AND_NAND_PMOS_ChannelLength=30,
    _AND_NAND_PMOS_NumberofGate=1,
    _AND_NAND_PMOS_XVT='SLVT',

    _AND_Inv_NMOS_ChannelWidth=400,
    _AND_Inv_NMOS_ChannelLength=30,
    _AND_Inv_NMOS_NumberofGate=1,
    _AND_Inv_NMOS_XVT='SLVT',
    _AND_Inv_NMOS_POGate_Comb_length=100,

    _AND_Inv_PMOS_ChannelWidth=800,
    _AND_Inv_PMOS_ChannelLength=30,
    _AND_Inv_PMOS_NumberofGate=1,
    _AND_Inv_PMOS_XVT='SLVT',
    _AND_Inv_PMOS_POGate_Comb_length=100,

    # PowerRail Placement
    _AND_NMOS_Pbody_NumCont=2,
    _AND_NMOS_Pbody_XvtTop2Pbody=600,
    _AND_PMOS_Nbody_NumCont=2,
    _AND_PMOS_Nbody_Xvtdown2Nbody=1000,
    _AND_PMOSXvt2NMOSXvt=1000,
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
    LayoutObj = _AND(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('###############      Sending to FTP Server...      ##################')
    My = MyInfo_YJH.USER(DesignParameters._Technology)
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
