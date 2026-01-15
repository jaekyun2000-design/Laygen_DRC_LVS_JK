
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
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A08_PbodyContactPhyLen_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A07_NbodyContactPhyLen_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A14_Mosfet_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.J00_CDACPreDriver_InvBuffer_KJH0 import J00_00_Inverter_KJH


## Define Class
class _InverterChain(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(

        ## InvChain Common
        _Pbody_NumCont=2,  # number
        _Nbody_NumCont=2,  # number
        _PMOSXvt2NMOSXvt=500,  # number
        _XvtTop2Pbody=None,  # number/None(Minimum)
        _Xvtdown2Nbody=None,  # number/None(Minimum)

        ## Inverter Chain
        ## Inv1 common
        _NumberofGate=[2, 4, 6],  # Vector
        _ChannelLength=30,  # Scalar
        _XVT='SLVT',  # 'SLVT'

        ## Inv1 NMOS
        _Inv_NMOS_ChannelWidth=200,  # Scalar
        _Inv_NMOS_POGate_Comb_length=100,  # Scalar

        ## Inv1 PMOS
        _Inv_PMOS_ChannelWidth=400,  # Scalar
        _Inv_PMOS_POGate_Comb_length=100,  # Scalar


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

                                  ## InvChain Common
                                  _Pbody_NumCont=2,  # number
                                  _Nbody_NumCont=2,  # number
                                  _PMOSXvt2NMOSXvt=500,  # number
                                  _XvtTop2Pbody=None,  # number/None(Minimum)
                                  _Xvtdown2Nbody=None,  # number/None(Minimum)

                                  ## Inverter Chain
                                  ## Inv1 common
                                  _NumberofGate=[2, 4, 6],  # Vector
                                  _ChannelLength=30,  # Scalar
                                  _XVT='SLVT',  # 'SLVT'

                                  ## Inv1 NMOS
                                  _Inv_NMOS_ChannelWidth=200,  # Scalar
                                  _Inv_NMOS_POGate_Comb_length=100,  # Scalar

                                  ## Inv1 PMOS
                                  _Inv_PMOS_ChannelWidth=400,  # Scalar
                                  _Inv_PMOS_POGate_Comb_length=100,  # Scalar

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

        for i in range(0,len(_NumberofGate)):
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## INV
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  INV: Sref Gen.
            ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
            _Caculation_Parameters = copy.deepcopy(J00_00_Inverter_KJH._Inverter._ParametersForDesignCalculation)
            ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
            _Caculation_Parameters['_NMOS_MosType']                      = 'NMOS'
            _Caculation_Parameters['_NMOS_MosUpDn']                      = 'Up'

            _Caculation_Parameters['_NMOS_NumberofGate']                 = _NumberofGate[i]
            _Caculation_Parameters['_NMOS_ChannelWidth']                 = _Inv_NMOS_ChannelWidth
            _Caculation_Parameters['_NMOS_ChannelLength']                = _ChannelLength
            _Caculation_Parameters['_NMOS_GateSpacing']                  = None
            _Caculation_Parameters['_NMOS_SDWidth']                      = None
            _Caculation_Parameters['_NMOS_XVT']                          = _XVT
            _Caculation_Parameters['_NMOS_PCCrit']                       = True

            _Caculation_Parameters['_NMOS_Source_Via_TF']                = False
            _Caculation_Parameters['_NMOS_Source_Via_Close2POpin_TF']    = False
            _Caculation_Parameters['_NMOS_Source_Comb_TF']               = False
            _Caculation_Parameters['_NMOS_Source_Comb_POpinward_TF']     = False
            _Caculation_Parameters['_NMOS_Source_Comb_Length']           = None

            _Caculation_Parameters['_NMOS_Drain_Via_TF']                 = True
            _Caculation_Parameters['_NMOS_Drain_Via_Close2POpin_TF']     = True
            _Caculation_Parameters['_NMOS_Drain_Comb_TF']                = True
            _Caculation_Parameters['_NMOS_Drain_Comb_POpinward_TF']      = True
            _Caculation_Parameters['_NMOS_Drain_Comb_Length']            = 0

            _Caculation_Parameters['_NMOS_PODummy_TF']                   = True
            _Caculation_Parameters['_NMOS_PODummy_Length']               = None
            _Caculation_Parameters['_NMOS_PODummy_Placement']            = None

            _Caculation_Parameters['_NMOS_Xvt_MinExten_TF']              = False
            _Caculation_Parameters['_NMOS_Xvt_Placement']                = 'Up'

            _Caculation_Parameters['_NMOS_POGate_Comb_TF']               = True
            _Caculation_Parameters['_NMOS_POGate_Comb_length']           = _Inv_NMOS_POGate_Comb_length
            _Caculation_Parameters['_NMOS_POGate_Via_TF']                = True
            _Caculation_Parameters['_NMOS_POGate_ViaMxMx']               = [0,1]


            _Caculation_Parameters['_PMOS_MosType']                      = 'PMOS'
            _Caculation_Parameters['_PMOS_MosUpDn']                      = 'Dn'

            _Caculation_Parameters['_PMOS_NumberofGate']                 = _NumberofGate[i]
            _Caculation_Parameters['_PMOS_ChannelWidth']                 = _Inv_PMOS_ChannelWidth
            _Caculation_Parameters['_PMOS_ChannelLength']                = _ChannelLength
            _Caculation_Parameters['_PMOS_GateSpacing']                  = None
            _Caculation_Parameters['_PMOS_SDWidth']                      = None
            _Caculation_Parameters['_PMOS_XVT']                          = _XVT
            _Caculation_Parameters['_PMOS_PCCrit']                       = True

            _Caculation_Parameters['_PMOS_Source_Via_TF']                = False
            _Caculation_Parameters['_PMOS_Source_Via_Close2POpin_TF']    = False
            _Caculation_Parameters['_PMOS_Source_Comb_TF']               = False
            _Caculation_Parameters['_PMOS_Source_Comb_POpinward_TF']     = False
            _Caculation_Parameters['_PMOS_Source_Comb_Length']           = None

            _Caculation_Parameters['_PMOS_Drain_Via_TF']                 = True
            _Caculation_Parameters['_PMOS_Drain_Via_Close2POpin_TF']     = True
            _Caculation_Parameters['_PMOS_Drain_Comb_TF']                = True
            _Caculation_Parameters['_PMOS_Drain_Comb_POpinward_TF']      = True
            _Caculation_Parameters['_PMOS_Drain_Comb_Length']            = 0

            _Caculation_Parameters['_PMOS_PODummy_TF']                   = True
            _Caculation_Parameters['_PMOS_PODummy_Length']               = None
            _Caculation_Parameters['_PMOS_PODummy_Placement']            = None

            _Caculation_Parameters['_PMOS_Xvt_MinExten_TF']              = False
            _Caculation_Parameters['_PMOS_Xvt_Placement']                = 'Dn'

            _Caculation_Parameters['_PMOS_POGate_Comb_TF']               = True
            _Caculation_Parameters['_PMOS_POGate_Comb_length']           = _Inv_PMOS_POGate_Comb_length
            _Caculation_Parameters['_PMOS_POGate_Via_TF']                = True
            _Caculation_Parameters['_PMOS_POGate_ViaMxMx']               = [0,1]

            _Caculation_Parameters['_NMOS_Pbody_NumCont']                = _Pbody_NumCont
            _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']           = _XvtTop2Pbody
            _Caculation_Parameters['_PMOS_Nbody_NumCont']                = _Nbody_NumCont
            _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody']          = _Xvtdown2Nbody
            _Caculation_Parameters['_PMOSXvt2NMOSXvt']                   = _PMOSXvt2NMOSXvt

            ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
            self._DesignParameter['SRF_INV{}'.format(i)] = self._SrefElementDeclaration(_DesignObj=J00_00_Inverter_KJH._Inverter(_DesignParameter=None, _Name='{}:SRF_INV{}'.format(_Name,i)))[0]

            ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
            self._DesignParameter['SRF_INV{}'.format(i)]['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_INV{}'.format(i)]['_Angle'] = 0

            ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_INV{}'.format(i)]['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_INV{}'.format(i)]['_XYCoordinates'] = [[0, 0]]

            del self._DesignParameter['SRF_INV{}'.format(i)]['_DesignObj']._DesignParameter['SRF_Pbody']['_DesignObj']._DesignParameter['SRF_PbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_COLayer']
            del self._DesignParameter['SRF_INV{}'.format(i)]['_DesignObj']._DesignParameter['SRF_Nbody']['_DesignObj']._DesignParameter['SRF_NbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_COLayer']

            if i == 0:
                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
                self._DesignParameter['SRF_INV{}'.format(i)]['_XYCoordinates'] = [[0, 0]]

            else:
                        ## Get_Scoord_v4.
                            ## Calculate Sref XYcoord
                tmpXY = []
                                ## Calculate
                                    ## Target_coord: _XY_type1
                tmp1 = self.get_param_KJH4('SRF_INV{}'.format(i-1),'SRF_NMOS','BND_PODummyLayer')
                target_coord = tmp1[0][0][-1][0]['_XY_down_left']
                                    ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4('SRF_INV{}'.format(i),'SRF_NMOS','BND_PODummyLayer')
                approaching_coord = tmp2[0][0][0][0]['_XY_down_left']
                                    ## Sref coord
                tmp3 = self.get_param_KJH4('SRF_INV{}'.format(i))
                Scoord = tmp3[0][0]['_XY_origin']
                                    ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
                            ## Define Coordinates
                self._DesignParameter['SRF_INV{}'.format(i)]['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Pbody Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length']                   = None
        _Caculation_Parameters['_NumCont']                  = _Pbody_NumCont
        _Caculation_Parameters['_Vtc_flag']                 = False

        ## Length Calculation
        tmp1 = self.get_param_KJH4('SRF_INV0','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_INV{}'.format(len(_NumberofGate)-1),'SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        _Caculation_Parameters['_Length'] = abs( tmp1[0][0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0][0]['_XY_right'][0] )

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

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Pbody']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ##X
        tmp1_1 = self.get_param_KJH4('SRF_INV0', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        tmp1_2 = self.get_param_KJH4('SRF_INV{}'.format(len(_NumberofGate) - 1), 'SRF_Pbody', 'SRF_PbodyContactPhyLen','BND_Met1Layer')
        target_coordx = np.round(0.5*(tmp1_1[0][0][0][0][0]['_XY_left'][0] + tmp1_2[0][0][0][0][0]['_XY_right'][0]))
                                ##Y
        tmp1_3 = self.get_param_KJH4('SRF_INV0', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        target_coordy = np.round(tmp1_3[0][0][0][0][0]['_XY_cent'][1])

        target_coord = [target_coordx,target_coordy]

                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pbody')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Pbody']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Nbody Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A07_NbodyContactPhyLen_KJH3._NbodyContactPhyLen._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length']                   = None
        _Caculation_Parameters['_NumCont']                  = _Nbody_NumCont
        _Caculation_Parameters['_Vtc_flag']                 = False

        ## Length Calculation
        tmp1 = self.get_param_KJH4('SRF_INV0','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_INV{}'.format(len(_NumberofGate)-1),'SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        _Caculation_Parameters['_Length'] = abs( tmp1[0][0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0][0]['_XY_right'][0] )

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
                                ##X
        tmp1_1 = self.get_param_KJH4('SRF_INV0', 'SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        tmp1_2 = self.get_param_KJH4('SRF_INV{}'.format(len(_NumberofGate) - 1), 'SRF_Nbody', 'SRF_NbodyContactPhyLen','BND_Met1Layer')
        target_coordx = np.round(0.5*(tmp1_1[0][0][0][0][0]['_XY_left'][0] + tmp1_2[0][0][0][0][0]['_XY_right'][0]))
                                ##Y
        tmp1_3 = self.get_param_KJH4('SRF_INV0', 'SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        target_coordy = np.round(tmp1_3[0][0][0][0][0]['_XY_cent'][1])

        target_coord = [target_coordx,target_coordy]

                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Nbody')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_Nbody']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Interconnects
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Interconnects : ViaM1M2
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

            ## Sref ViaX declaration
        self._DesignParameter['SRF_IntConn_ViaM1M2'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_IntConn_ViaM1M2'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_IntConn_ViaM1M2']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_IntConn_ViaM1M2']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_IntConn_ViaM1M2']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)


                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_IntConn_ViaM1M2']['_XYCoordinates'] = [[0, 0]]

        for i in range(1,len(_NumberofGate)):
                            ## Calculate
                                ## Target_coord: _XY_type1
                                ##X
            tmp1_1 = self.get_param_KJH4('SRF_INV{}'.format(i),'BND_Input_Vtc_M1')
            target_coord = tmp1_1[0][0][0]['_XY_cent']
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_IntConn_ViaM1M2','SRF_ViaM1M2','BND_Met1Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_IntConn_ViaM1M2')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['SRF_IntConn_ViaM1M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Interconnects : Hrz M2
        for i in range(0, len(_NumberofGate)-1):
            ## Boundary_element Generation
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_IntConn_Hrz_M2_{}'.format(i)] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )

            ## Define Boundary_element _YWidth
            self._DesignParameter['BND_IntConn_Hrz_M2_{}'.format(i)]['_YWidth'] = 50

            ## Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH4('SRF_IntConn_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
            tmp2 = self.get_param_KJH4('SRF_INV{}'.format(i),'BND_Out_Vtc_M2')
            self._DesignParameter['BND_IntConn_Hrz_M2_{}'.format(i)]['_XWidth'] = abs( tmp1[i][0][0][0]['_XY_right'][0] - tmp2[0][0][0]['_XY_left'][0] )

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_IntConn_Hrz_M2_{}'.format(i)]['_XYCoordinates'] = [[0, 0]]

                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['BND_IntConn_Hrz_M2_{}'.format(i)]['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
                                ##X
            tmp1_1 = self.get_param_KJH4('SRF_IntConn_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
            target_coord = tmp1_1[i][0][0][0]['_XY_right']
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_IntConn_Hrz_M2_{}'.format(i))
            approaching_coord = tmp2[0][0]['_XY_right']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('BND_IntConn_Hrz_M2_{}'.format(i))
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                                ## Define coordinates
            self._DesignParameter['BND_IntConn_Hrz_M2_{}'.format(i)]['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Input
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Input : ViaM1M2
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Input_ViaM1Mx'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Input_ViaM1Mx'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Input_ViaM1Mx']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Input_ViaM1Mx']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Input_ViaM1Mx']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_Input_ViaM1Mx']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
            ## Target_coord: _XY_type1
                ##X
        tmp1_1 = self.get_param_KJH4('SRF_INV0','BND_Input_Vtc_M1')
        target_coord = tmp1_1[0][0][0]['_XY_left']
            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_Input_ViaM1Mx', 'SRF_ViaM1M2', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_right']
            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Input_ViaM1Mx')
        Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define coordinates
        self._DesignParameter['SRF_Input_ViaM1Mx']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Output
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Output : ViaM1M2
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Output_ViaM2Mx'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Output_ViaM2Mx'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Output_ViaM2Mx']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Output_ViaM2Mx']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Output_ViaM2Mx']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_Output_ViaM2Mx']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
            ## Target_coord: _XY_type1
                ##X
        tmp1_1 = self.get_param_KJH4('SRF_INV{}'.format(len(_NumberofGate)-1),'BND_Out_Vtc_M2')
        target_coord = tmp1_1[0][0][0]['_XY_right']
            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_Output_ViaM2Mx', 'SRF_ViaM2M3', 'BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_left']
            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Output_ViaM2Mx')
        Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define coordinates
        self._DesignParameter['SRF_Output_ViaM2Mx']['_XYCoordinates'] = tmpXY


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
    libname = 'Proj_ADC_J00_CDACPreDriver_InvBuffer_KJH'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'J00_01_InverterChain_v0_469'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

    ## InvChain Common
        _Pbody_NumCont      = 2,        # number
        _Nbody_NumCont      = 2,        # number
        _PMOSXvt2NMOSXvt    = 500,      # number
        _XvtTop2Pbody       = None,     # number/None(Minimum)
        _Xvtdown2Nbody      = None,     # number/None(Minimum)

    ## Inverter Chain
        ## Inv1 common
        _NumberofGate   =   [1, 1, 2, 3],  # Vector
        _ChannelLength  =   30,         # Scalar
        _XVT            =   'SLVT',     # 'SLVT'

        ## Inv1 NMOS
        _Inv_NMOS_ChannelWidth           = 200,     # Scalar
        _Inv_NMOS_POGate_Comb_length     = 80,     # Scalar

        ## Inv1 PMOS
        _Inv_PMOS_ChannelWidth           = 400,     # Scalar
        _Inv_PMOS_POGate_Comb_length     = 80,     # Scalar

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
    LayoutObj = _InverterChain(_DesignParameter=None, _Name=cellname)
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
