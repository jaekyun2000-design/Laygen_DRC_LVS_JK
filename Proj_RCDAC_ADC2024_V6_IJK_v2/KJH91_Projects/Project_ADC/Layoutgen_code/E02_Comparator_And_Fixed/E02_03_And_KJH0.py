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
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.E02_Comparator_And_Fixed import E02_02_Nand_KJH0
from KJH91_Projects.Project_ADC.Layoutgen_code.E01_ComparatorWtLatch_Fixed import E01_00_Inverter


## Define Class
class _And(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
## AND
    ## AND Common
        # XVT
        _And_XVT = 'SLVT',
        # Height
        _And_PMOSXvt2NMOSXvt=1150,  # number
        # Body
        _And_Pbody_XvtTop2Pbody=None,  # Number/None(Minimum)
        _And_Nbody_Xvtdown2Nbody=None,  # Number/None(Minimum)
    ## Nand
        # NmosA
        _Nand_NMOSA_NumberofGate=1,  # Number
        _Nand_NMOSA_ChannelWidth=100,  # Number
        _Nand_NMOSA_ChannelLength=30,  # Number
        # NMOSB
        _Nand_NMOSB_NumberofGate=2,  # Number
        _Nand_NMOSB_ChannelWidth=750,  # Number
        _Nand_NMOSB_ChannelLength=30,  # Number
        # PMOSA
        _Nand_PMOSA_NumberofGate=1,  # Number
        _Nand_PMOSA_ChannelWidth=300,  # Number
        _Nand_PMOSA_ChannelLength=30,  # Number
        # PMOSB
        _Nand_PMOSB_NumberofGate=3,  # Number
        _Nand_PMOSB_ChannelWidth=750,  # Number
        _Nand_PMOSB_ChannelLength=30,  # Number
    ## Inverter
        # Nmos
        _Inv_NMOS_NumberofGate=1,  # Number
        _Inv_NMOS_ChannelWidth=100,  # Number
        _Inv_NMOS_ChannelLength=30,  # Number
        # Pmos
        _Inv_PMOS_NumberofGate=1,  # Number
        _Inv_PMOS_ChannelWidth=200,  # Number
        _Inv_PMOS_ChannelLength=30,  # Number
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
## AND
    ## AND Common
        # XVT
        _And_XVT = 'SLVT',
        # Height
        _And_PMOSXvt2NMOSXvt=1150,  # number
        # Body
        _And_Pbody_XvtTop2Pbody=None,  # Number/None(Minimum)
        _And_Nbody_Xvtdown2Nbody=None,  # Number/None(Minimum)
    ## Nand
        # NmosA
        _Nand_NMOSA_NumberofGate=1,  # Number
        _Nand_NMOSA_ChannelWidth=100,  # Number
        _Nand_NMOSA_ChannelLength=30,  # Number
        # NMOSB
        _Nand_NMOSB_NumberofGate=2,  # Number
        _Nand_NMOSB_ChannelWidth=750,  # Number
        _Nand_NMOSB_ChannelLength=30,  # Number
        # PMOSA
        _Nand_PMOSA_NumberofGate=1,  # Number
        _Nand_PMOSA_ChannelWidth=300,  # Number
        _Nand_PMOSA_ChannelLength=30,  # Number
        # PMOSB
        _Nand_PMOSB_NumberofGate=3,  # Number
        _Nand_PMOSB_ChannelWidth=750,  # Number
        _Nand_PMOSB_ChannelLength=30,  # Number
    ## Inverter
        # Nmos
        _Inv_NMOS_NumberofGate=1,  # Number
        _Inv_NMOS_ChannelWidth=100,  # Number
        _Inv_NMOS_ChannelLength=30,  # Number
        # Pmos
        _Inv_PMOS_NumberofGate=1,  # Number
        _Inv_PMOS_ChannelWidth=200,  # Number
        _Inv_PMOS_ChannelLength=30,  # Number

                                  ):

        ## Class_HEADER: Pre Defined Parameter Before Calculation
            ## Load DRC library
        _DRCobj = DRC.DRC()
            ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ## CALCULATION START
        start_time = time.time()
        # end_time = time.time()
        # self.elapsed_time = end_time - start_time
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  NAND SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_PMOS_power_v2._PMOS_POWER._ParametersForDesignCalculation)
        _Calculation_Parameters = copy.deepcopy(E02_02_Nand_KJH0._Nand._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_PMOSPOWER_PbodyContact_1_Length']  = _PMOSPOWER_PbodyContact_1_Length
        _Calculation_Parameters['_XVT'] = _And_XVT

        _Calculation_Parameters['_NMOSA_NumberofGate'] = _Nand_NMOSA_NumberofGate
        _Calculation_Parameters['_NMOSA_ChannelWidth'] = _Nand_NMOSA_ChannelWidth
        _Calculation_Parameters['_NMOSA_ChannelLength'] = _Nand_NMOSA_ChannelLength

        _Calculation_Parameters['_NMOSB_NumberofGate'] = _Nand_NMOSB_NumberofGate
        _Calculation_Parameters['_NMOSB_ChannelWidth'] = _Nand_NMOSB_ChannelWidth
        _Calculation_Parameters['_NMOSB_ChannelLength'] = _Nand_NMOSB_ChannelLength

        _Calculation_Parameters['_PMOSA_NumberofGate'] = _Nand_PMOSA_NumberofGate
        _Calculation_Parameters['_PMOSA_ChannelWidth'] = _Nand_PMOSA_ChannelWidth
        _Calculation_Parameters['_PMOSA_ChannelLength'] = _Nand_PMOSA_ChannelLength

        _Calculation_Parameters['_PMOSB_NumberofGate'] = _Nand_PMOSB_NumberofGate
        _Calculation_Parameters['_PMOSB_ChannelWidth'] = _Nand_PMOSB_ChannelWidth
        _Calculation_Parameters['_PMOSB_ChannelLength'] = _Nand_PMOSB_ChannelLength

        _Calculation_Parameters['_NMOSAB_Pbody_XvtTop2Pbody'] = _And_Pbody_XvtTop2Pbody
        _Calculation_Parameters['_PMOSAB_Nbody_Xvtdown2Nbody'] = _And_Nbody_Xvtdown2Nbody

        _Calculation_Parameters['_PMOSXvt2NMOSXvt'] = _And_PMOSXvt2NMOSXvt

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_NAND'] = self._SrefElementDeclaration(_DesignObj=E02_02_Nand_KJH0._Nand(_DesignParameter=None, _Name='{}:SRF_NAND'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_NAND']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NAND']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NAND']['_DesignObj']._CalculateDesignParameter(**_Calculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NAND']['_XYCoordinates'] = [[0, 0]]


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Inv SREF Generation
        _Calculation_Parameters = copy.deepcopy(E01_00_Inverter._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Calculation_Parameters['_XVT'] = _And_XVT

        _Calculation_Parameters['_NMOS_NumberofGate'] = _Inv_NMOS_NumberofGate
        _Calculation_Parameters['_NMOS_ChannelWidth'] = _Inv_NMOS_ChannelWidth
        _Calculation_Parameters['_NMOS_ChannelLength'] = _Inv_NMOS_ChannelLength

        _Calculation_Parameters['_PMOS_NumberofGate'] = _Inv_PMOS_NumberofGate
        _Calculation_Parameters['_PMOS_ChannelWidth'] = _Inv_PMOS_ChannelWidth
        _Calculation_Parameters['_PMOS_ChannelLength'] = _Inv_PMOS_ChannelLength

        _Calculation_Parameters['_NMOS_Pbody_XvtTop2Pbody'] = _And_Pbody_XvtTop2Pbody
        _Calculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody'] = _And_Nbody_Xvtdown2Nbody

        _Calculation_Parameters['_PMOSXvt2NMOSXvt'] = _And_PMOSXvt2NMOSXvt

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Inverter'] = self._SrefElementDeclaration(_DesignObj=E01_00_Inverter._Inverter(_DesignParameter=None, _Name='{}:SRF_Inverter'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Inverter']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inverter']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inverter']['_DesignObj']._CalculateDesignParameter(**_Calculation_Parameters)

                ## initialized Sref coordinate
        self._DesignParameter['SRF_Inverter']['_XYCoordinates'] = [[0, 0]]

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  cal _XvtTop2Pbody and _Xvtdown2Nbody
        tmp1 = self.get_param_KJH4('SRF_Inverter','SRF_NMOS','BND_{}Layer'.format(_And_XVT))
        tmp2 = self.get_param_KJH4('SRF_Inverter','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        XVTtop2Pbody_Inv = tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0]['_XY_up'][1]

        tmp1 = self.get_param_KJH4('SRF_NAND','SRF_Pulldown','SRF_NMOSB','BND_{}Layer'.format(_And_XVT))
        tmp2 = self.get_param_KJH4('SRF_NAND','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        XVTtop2Pbody_Nand = tmp1[0][0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0]['_XY_up'][1]
        tmp_XVTtop2Pbody = max(XVTtop2Pbody_Nand,XVTtop2Pbody_Inv)

        tmp1 = self.get_param_KJH4('SRF_Inverter','SRF_PMOS','BND_{}Layer'.format(_And_XVT))
        tmp2 = self.get_param_KJH4('SRF_Inverter','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        XVTdown2Nbody_Inv = abs(tmp1[0][0][0][0]['_XY_down'][1] - tmp2[0][0][0][0][0]['_XY_down'][1])

        tmp1 = self.get_param_KJH4('SRF_NAND','SRF_Pullup','SRF_PMOSB','BND_{}Layer'.format(_And_XVT))
        tmp2 = self.get_param_KJH4('SRF_NAND','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        XVTdown2Nbody_Nand = abs( tmp1[0][0][0][0][0]['_XY_down'][1] - tmp2[0][0][0][0][0]['_XY_down'][1] )
        tmp_XVTdown2Nbody = max(XVTdown2Nbody_Inv,XVTdown2Nbody_Nand)

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  NAND SREF Re-Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_PMOS_power_v2._PMOS_POWER._ParametersForDesignCalculation)
        _Calculation_Parameters = copy.deepcopy(E02_02_Nand_KJH0._Nand._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_PMOSPOWER_PbodyContact_1_Length']  = _PMOSPOWER_PbodyContact_1_Length
        _Calculation_Parameters['_XVT'] = _And_XVT

        _Calculation_Parameters['_NMOSA_NumberofGate'] = _Nand_NMOSA_NumberofGate
        _Calculation_Parameters['_NMOSA_ChannelWidth'] = _Nand_NMOSA_ChannelWidth
        _Calculation_Parameters['_NMOSA_ChannelLength'] = _Nand_NMOSA_ChannelLength

        _Calculation_Parameters['_NMOSB_NumberofGate'] = _Nand_NMOSB_NumberofGate
        _Calculation_Parameters['_NMOSB_ChannelWidth'] = _Nand_NMOSB_ChannelWidth
        _Calculation_Parameters['_NMOSB_ChannelLength'] = _Nand_NMOSB_ChannelLength

        _Calculation_Parameters['_PMOSA_NumberofGate'] = _Nand_PMOSA_NumberofGate
        _Calculation_Parameters['_PMOSA_ChannelWidth'] = _Nand_PMOSA_ChannelWidth
        _Calculation_Parameters['_PMOSA_ChannelLength'] = _Nand_PMOSA_ChannelLength

        _Calculation_Parameters['_PMOSB_NumberofGate'] = _Nand_PMOSB_NumberofGate
        _Calculation_Parameters['_PMOSB_ChannelWidth'] = _Nand_PMOSB_ChannelWidth
        _Calculation_Parameters['_PMOSB_ChannelLength'] = _Nand_PMOSB_ChannelLength

        _Calculation_Parameters['_NMOSAB_Pbody_XvtTop2Pbody'] = tmp_XVTtop2Pbody
        _Calculation_Parameters['_PMOSAB_Nbody_Xvtdown2Nbody'] = tmp_XVTdown2Nbody

        _Calculation_Parameters['_PMOSXvt2NMOSXvt'] = _And_PMOSXvt2NMOSXvt

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_NAND'] = self._SrefElementDeclaration(_DesignObj=E02_02_Nand_KJH0._Nand(_DesignParameter=None, _Name='{}:SRF_NAND'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_NAND']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NAND']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NAND']['_DesignObj']._CalculateDesignParameter(**_Calculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_NAND']['_XYCoordinates'] = [[0, 0]]


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Inv SREF Re-Generation
        _Calculation_Parameters = copy.deepcopy(E01_00_Inverter._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Calculation_Parameters['_XVT'] = _And_XVT

        _Calculation_Parameters['_NMOS_NumberofGate'] = _Inv_NMOS_NumberofGate
        _Calculation_Parameters['_NMOS_ChannelWidth'] = _Inv_NMOS_ChannelWidth
        _Calculation_Parameters['_NMOS_ChannelLength'] = _Inv_NMOS_ChannelLength

        _Calculation_Parameters['_PMOS_NumberofGate'] = _Inv_PMOS_NumberofGate
        _Calculation_Parameters['_PMOS_ChannelWidth'] = _Inv_PMOS_ChannelWidth
        _Calculation_Parameters['_PMOS_ChannelLength'] = _Inv_PMOS_ChannelLength

        _Calculation_Parameters['_NMOS_Pbody_XvtTop2Pbody'] = tmp_XVTtop2Pbody
        _Calculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody'] = tmp_XVTdown2Nbody

        _Calculation_Parameters['_PMOSXvt2NMOSXvt'] = _And_PMOSXvt2NMOSXvt

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Inverter'] = self._SrefElementDeclaration(_DesignObj=E01_00_Inverter._Inverter(_DesignParameter=None, _Name='{}:SRF_Inverter'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Inverter']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inverter']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inverter']['_DesignObj']._CalculateDesignParameter(**_Calculation_Parameters)

                ## initialized Sref coordinate
        self._DesignParameter['SRF_Inverter']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Inverter']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1x = self.get_outter_KJH4('SRF_NAND')
        target_coordx = tmp1x['_Mostright']['coord'][0]
        tmp1y = self.get_param_KJH4('SRF_NAND','SRF_Pulldown','SRF_NMOSB','BND_{}Layer'.format(_And_XVT))
        target_coordy = tmp1y[0][0][0][0][0]['_XY_up'][1]
        target_coord = [target_coordx,target_coordy]

                            ## Approaching_coord: _XY_type2
        tmp2x = self.get_outter_KJH4('SRF_Inverter')
        approaching_coordx = tmp2x['_Mostleft']['coord'][0]
        tmp2y = self.get_param_KJH4('SRF_Inverter','SRF_NMOS','BND_{}Layer'.format(_And_XVT))
        approaching_coordy = tmp2y[0][0][0][0]['_XY_up'][1]
        approaching_coord = [approaching_coordx,approaching_coordy]
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



        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Body Cover.
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Body Cover: PBody
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Body Cover: PBody: M1 Exten
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Pbody_M1Exten'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Inverter','SRF_Pbody','SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        self._DesignParameter['BND_Pbody_M1Exten']['_YWidth'] = tmp1[0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Inverter','SRF_Pbody','SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_NAND','SRF_Pbody','SRF_PbodyContactPhyLen', 'BND_Met1Layer')

        self._DesignParameter['BND_Pbody_M1Exten']['_XWidth'] = abs(tmp2[0][0][0][0][0]['_XY_left'][0] - tmp1[0][0][0][0][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Pbody_M1Exten']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Pbody_M1Exten']['_XYCoordinates'] = [[0, 0]]

        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_NAND','SRF_Pbody','SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        target_coord = tmp1[0][0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Pbody_M1Exten')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Pbody_M1Exten')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

                ## Define coordinates
        self._DesignParameter['BND_Pbody_M1Exten']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Body Cover: PBody: RX Exten
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Pbody_RXExten'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0],
            _Datatype=DesignParameters._LayerMapping['DIFF'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Inverter','SRF_Pbody','SRF_PbodyContactPhyLen', 'BND_ODLayer')
        self._DesignParameter['BND_Pbody_RXExten']['_YWidth'] = tmp1[0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Inverter','SRF_Pbody','SRF_PbodyContactPhyLen', 'BND_ODLayer')
        tmp2 = self.get_param_KJH4('SRF_NAND','SRF_Pbody','SRF_PbodyContactPhyLen', 'BND_ODLayer')
        self._DesignParameter['BND_Pbody_RXExten']['_XWidth'] = abs(tmp2[0][0][0][0][0]['_XY_left'][0] - tmp1[0][0][0][0][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Pbody_RXExten']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Pbody_RXExten']['_XYCoordinates'] = [[0, 0]]

        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_NAND','SRF_Pbody','SRF_PbodyContactPhyLen', 'BND_ODLayer')
        target_coord = tmp1[0][0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Pbody_RXExten')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Pbody_RXExten')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define coordinates
        self._DesignParameter['BND_Pbody_RXExten']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Body Cover: PBody: Bp Exten
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Pbody_PPExten'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Inverter','SRF_Pbody','SRF_PbodyContactPhyLen', 'BND_PPLayer')
        self._DesignParameter['BND_Pbody_PPExten']['_YWidth'] = tmp1[0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Inverter','SRF_Pbody','SRF_PbodyContactPhyLen', 'BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_NAND','SRF_Pbody','SRF_PbodyContactPhyLen', 'BND_PPLayer')
        self._DesignParameter['BND_Pbody_PPExten']['_XWidth'] = abs(tmp2[0][0][0][0][0]['_XY_left'][0] - tmp1[0][0][0][0][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Pbody_PPExten']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Pbody_PPExten']['_XYCoordinates'] = [[0, 0]]

        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_NAND','SRF_Pbody','SRF_PbodyContactPhyLen', 'BND_PPLayer')
        target_coord = tmp1[0][0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Pbody_PPExten')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Pbody_PPExten')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

                ## Define coordinates
        self._DesignParameter['BND_Pbody_PPExten']['_XYCoordinates'] = tmpXY






        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Body Cover: NBody
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Body Cover: NBody: M1 Exten
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Nbody_M1Exten'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Inverter','SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        self._DesignParameter['BND_Nbody_M1Exten']['_YWidth'] = tmp1[0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Inverter', 'SRF_Nbody','SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_NAND','SRF_Nbody','SRF_NbodyContactPhyLen', 'BND_Met1Layer')

        self._DesignParameter['BND_Nbody_M1Exten']['_XWidth'] = abs(tmp2[0][0][0][0][0]['_XY_left'][0] - tmp1[0][0][0][0][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Nbody_M1Exten']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Nbody_M1Exten']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_NAND','SRF_Nbody','SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        target_coord = tmp1[0][0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Nbody_M1Exten')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Nbody_M1Exten')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Nbody_M1Exten']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Body Cover: NBody: RX Exten
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Nbody_RXExten'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0],
            _Datatype=DesignParameters._LayerMapping['DIFF'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Inverter','SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_ODLayer')
        self._DesignParameter['BND_Nbody_RXExten']['_YWidth'] = tmp1[0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Inverter', 'SRF_Nbody','SRF_NbodyContactPhyLen', 'BND_ODLayer')
        tmp2 = self.get_param_KJH4('SRF_NAND','SRF_Nbody','SRF_NbodyContactPhyLen', 'BND_ODLayer')
        self._DesignParameter['BND_Nbody_RXExten']['_XWidth'] = abs(tmp2[0][0][0][0][0]['_XY_left'][0] - tmp1[0][0][0][0][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Nbody_RXExten']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Nbody_RXExten']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_NAND','SRF_Nbody','SRF_NbodyContactPhyLen', 'BND_ODLayer')
        target_coord = tmp1[0][0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Nbody_RXExten')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Nbody_RXExten')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Nbody_RXExten']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Body Cover: NBody: Nwell Exten
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Nbody_NwellExten'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_NAND', 'BND_PMOSAB_NellExten')
        self._DesignParameter['BND_Nbody_NwellExten']['_YWidth'] = tmp1[0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_NAND', 'BND_PMOSAB_NellExten')
        tmp2 = self.get_param_KJH4('SRF_Inverter', 'BND_PMOS_NellExten')
        self._DesignParameter['BND_Nbody_NwellExten']['_XWidth'] = abs(tmp2[0][0][0]['_XY_right'][0] - tmp1[0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Nbody_NwellExten']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Nbody_NwellExten']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_NAND', 'BND_PMOSAB_NellExten')
        target_coord = tmp1[0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Nbody_NwellExten')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Nbody_NwellExten')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Nbody_NwellExten']['_XYCoordinates'] = tmpXY


        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')
        # start_time = time.time()
        end_time = time.time()
        self.elapsed_time = end_time - start_time

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ZZ01_E02_03_And_Fixed'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'D03_03_And_v0_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
## AND
    ## AND Common
        # XVT
        _And_XVT = 'SLVT',
        # Height
        _And_PMOSXvt2NMOSXvt=1150,  # number
        # Body
        _And_Pbody_XvtTop2Pbody=None,  # Number/None(Minimum)
        _And_Nbody_Xvtdown2Nbody=None,  # Number/None(Minimum)
    ## Nand
        # NmosA
        _Nand_NMOSA_NumberofGate=1,  # Number
        _Nand_NMOSA_ChannelWidth=100,  # Number
        _Nand_NMOSA_ChannelLength=30,  # Number
        # NMOSB
        _Nand_NMOSB_NumberofGate=2,  # Number
        _Nand_NMOSB_ChannelWidth=750,  # Number
        _Nand_NMOSB_ChannelLength=30,  # Number
        # PMOSA
        _Nand_PMOSA_NumberofGate=1,  # Number
        _Nand_PMOSA_ChannelWidth=300,  # Number
        _Nand_PMOSA_ChannelLength=30,  # Number
        # PMOSB
        _Nand_PMOSB_NumberofGate=3,  # Number
        _Nand_PMOSB_ChannelWidth=750,  # Number
        _Nand_PMOSB_ChannelLength=30,  # Number
    ## Inverter
        # Nmos
        _Inv_NMOS_NumberofGate=1,  # Number
        _Inv_NMOS_ChannelWidth=100,  # Number
        _Inv_NMOS_ChannelLength=30,  # Number
        # Pmos
        _Inv_PMOS_NumberofGate=1,  # Number
        _Inv_PMOS_ChannelWidth=200,  # Number
        _Inv_PMOS_ChannelLength=30,  # Number
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
    LayoutObj = _And(_DesignParameter=None, _Name=cellname)
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
    # Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()

    print('#############################      Finished      ################################')
    print('{} Hours   {} minutes   {} seconds'.format(h, m, s))
# end of 'main():' ---------------------------------------------------------------------------------------------
