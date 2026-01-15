
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
from KJH91_Projects.Project_ADC.Layoutgen_code.J00_CDACPreDriver_InvBuffer_KJH0_RCHybrid_Fixed import J00_00_Inverter_KJH


## Define Class
class _InverterChain(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
## Inverter Chain
    ## InvChain Common
        _PMOSXvt2NMOSXvt    = 500,      # number

    ## Inverter Chain
        ## Inv1 common
        _NumberofGate   =   [1,2,4,8],  # Vector
        _ChannelLength  =   30,         # Scalar
        _XVT            =   'SLVT',     # 'SLVT'

        ## Inv1 NMOS
        _Inv_NMOS_ChannelWidth           = 400,     # Scalar

        ## Inv1 PMOS
        _Inv_PMOS_ChannelWidth           = 800,     # Scalar
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
## Inverter Chain
    ## InvChain Common
        _PMOSXvt2NMOSXvt    = 500,      # number

    ## Inverter Chain
        ## Inv1 common
        _NumberofGate   =   [1,2,4,8],  # Vector
        _ChannelLength  =   30,         # Scalar
        _XVT            =   'SLVT',     # 'SLVT'

        ## Inv1 NMOS
        _Inv_NMOS_ChannelWidth           = 400,     # Scalar

        ## Inv1 PMOS
        _Inv_PMOS_ChannelWidth           = 800,     # Scalar
                                  ):

        ## Class_HEADER: Pre Defined Parameter Before Calculation
            ## Load DRC library
        _DRCobj = DRC.DRC()
            ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ## CALCULATION START
        InverterChain_KJH_start_time = time.time()
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## INV gen for XVT to body
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  INV: Sref Gen.
        tmp_XVTTop2Pbody = []
        tmp_XVTdown2Nbody = []
        for i in range(0,len(_NumberofGate)):
            ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
            _Caculation_Parameters = copy.deepcopy(J00_00_Inverter_KJH._Inverter._ParametersForDesignCalculation)
            ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
            _Caculation_Parameters['_XVT']                               = _XVT

            _Caculation_Parameters['_NMOS_NumberofGate']                 = _NumberofGate[i]
            _Caculation_Parameters['_NMOS_ChannelWidth']                 = _Inv_NMOS_ChannelWidth
            _Caculation_Parameters['_NMOS_ChannelLength']                = _ChannelLength

            _Caculation_Parameters['_PMOS_NumberofGate']                 = _NumberofGate[i]
            _Caculation_Parameters['_PMOS_ChannelWidth']                 = _Inv_PMOS_ChannelWidth
            _Caculation_Parameters['_PMOS_ChannelLength']                = _ChannelLength

            _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']           = None
            _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody']          = None

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
                New_Scoord[0] = New_Scoord[0] + 150
                tmpXY.append(New_Scoord)
                            ## Define Coordinates
                self._DesignParameter['SRF_INV{}'.format(i)]['_XYCoordinates'] = tmpXY

            tmp1 = self.get_param_KJH4('SRF_INV{}'.format(i),'SRF_NMOS','BND_{}Layer'.format(_XVT))
            tmp2 = self.get_param_KJH4('SRF_INV{}'.format(i),'SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
            tmp_tmp_XVTTOP2Pbody =  abs(tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0]['_XY_up'][1])

            tmp3 = self.get_param_KJH4('SRF_INV{}'.format(i),'SRF_PMOS','BND_{}Layer'.format(_XVT))
            tmp4 = self.get_param_KJH4('SRF_INV{}'.format(i),'SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
            tmp_tmp_XVTdown2Nbody = abs(tmp3[0][0][0][0]['_XY_down'][1] - tmp4[0][0][0][0][0]['_XY_down'][1])

            tmp_XVTTop2Pbody.append(tmp_tmp_XVTTOP2Pbody)
            tmp_XVTdown2Nbody.append(tmp_tmp_XVTdown2Nbody)


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## INV Regen
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  INV: Sref Gen.
        _XvtTop2Pbody = max(tmp_XVTTop2Pbody)
        _Xvtdown2Nbody = max(tmp_XVTdown2Nbody)

        for i in range(0,len(_NumberofGate)):
            ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
            _Caculation_Parameters = copy.deepcopy(J00_00_Inverter_KJH._Inverter._ParametersForDesignCalculation)
            ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
            _Caculation_Parameters['_XVT']                               = _XVT

            _Caculation_Parameters['_NMOS_NumberofGate']                 = _NumberofGate[i]
            _Caculation_Parameters['_NMOS_ChannelWidth']                 = _Inv_NMOS_ChannelWidth
            _Caculation_Parameters['_NMOS_ChannelLength']                = _ChannelLength

            _Caculation_Parameters['_PMOS_NumberofGate']                 = _NumberofGate[i]
            _Caculation_Parameters['_PMOS_ChannelWidth']                 = _Inv_PMOS_ChannelWidth
            _Caculation_Parameters['_PMOS_ChannelLength']                = _ChannelLength

            _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']           = _XvtTop2Pbody
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
                New_Scoord[0] = New_Scoord[0] + 150
                tmpXY.append(New_Scoord)
                            ## Define Coordinates
                self._DesignParameter['SRF_INV{}'.format(i)]['_XYCoordinates'] = tmpXY



        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Pbody Gen.
        _Pbody_NumCont =2
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
        _Nbody_NumCont=2
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
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_IntConn_ViaM1M2'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_IntConn_ViaM1M2'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_IntConn_ViaM1M2']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_IntConn_ViaM1M2']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_IntConn_ViaM1M2']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)


                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_IntConn_ViaM1M2']['_XYCoordinates'] = [[0, 0]]

        for i in range(0,len(_NumberofGate)-1):
                            ## Calculate
                                ## Target_coord: _XY_type1
                                ##X
            tmp1_1 = self.get_param_KJH4('SRF_INV{}'.format(i),'BND_Out_Vtc_M2')
            target_coord = tmp1_1[0][0][0]['_XY_right']
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_IntConn_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
            approaching_coord = tmp2[0][0][0][0]['_XY_left']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_IntConn_ViaM1M2')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['SRF_IntConn_ViaM1M2']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Interconnects : Hrz M1
        for i in range(0, len(_NumberofGate)-1):
            ## Boundary_element Generation
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_IntConn_Hrz_M1_{}'.format(i)] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )

            ## Define Boundary_element _YWidth
            self._DesignParameter['BND_IntConn_Hrz_M1_{}'.format(i)]['_YWidth'] = 50

            ## Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH4('SRF_INV{}'.format(i+1),'BND_Input_Vtc_M1')
            tmp2 = self.get_param_KJH4('SRF_INV{}'.format(i),'BND_Out_Vtc_M2')
            self._DesignParameter['BND_IntConn_Hrz_M1_{}'.format(i)]['_XWidth'] = abs( tmp1[0][0][0]['_XY_right'][0] - tmp2[0][0][0]['_XY_right'][0] )

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_IntConn_Hrz_M1_{}'.format(i)]['_XYCoordinates'] = [[0, 0]]

                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['BND_IntConn_Hrz_M1_{}'.format(i)]['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
                                ##X
            tmp1_1 = self.get_param_KJH4('SRF_INV{}'.format(i),'BND_Out_Vtc_M2')
            target_coord = tmp1_1[0][0][0]['_XY_right']
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_IntConn_Hrz_M1_{}'.format(i))
            approaching_coord = tmp2[0][0]['_XY_left']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('BND_IntConn_Hrz_M1_{}'.format(i))
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                                ## Define coordinates
            self._DesignParameter['BND_IntConn_Hrz_M1_{}'.format(i)]['_XYCoordinates'] = tmpXY







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








        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Covering
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Covering: PMOS
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## Covering: PMOS: _XVT
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOS_XVTExten'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['{}'.format(_XVT)][0],
            _Datatype=DesignParameters._LayerMapping['{}'.format(_XVT)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_INV0','SRF_PMOS','BND_{}Layer'.format(_XVT))
        self._DesignParameter['BND_PMOS_XVTExten']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_INV0','SRF_PMOS','BND_{}Layer'.format(_XVT))
        tmp2 = self.get_param_KJH4('SRF_INV{}'.format(len(_NumberofGate)-1),'SRF_PMOS','BND_{}Layer'.format(_XVT))

        self._DesignParameter['BND_PMOS_XVTExten']['_XWidth'] = abs( tmp2[0][0][0][0]['_XY_right'][0] - tmp1[0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOS_XVTExten']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_PMOS_XVTExten']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_INV0','SRF_PMOS','BND_{}Layer'.format(_XVT))
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOS_XVTExten')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOS_XVTExten')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_PMOS_XVTExten']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## Covering: PMOS: Bp
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOS_BpExten'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_INV0','SRF_PMOS','BND_PPLayer')
        self._DesignParameter['BND_PMOS_BpExten']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_INV0','SRF_PMOS','BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_INV{}'.format(len(_NumberofGate)-1),'SRF_PMOS','BND_PPLayer')

        self._DesignParameter['BND_PMOS_BpExten']['_XWidth'] = abs( tmp2[0][0][0][0]['_XY_right'][0] - tmp1[0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOS_BpExten']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_PMOS_BpExten']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_INV0','SRF_PMOS','BND_PPLayer')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOS_BpExten')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOS_BpExten')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_PMOS_BpExten']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## Covering: PMOS: Nwell
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PMOS_NwellExten'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_INV0','BND_PMOS_NellExten')
        self._DesignParameter['BND_PMOS_NwellExten']['_YWidth'] = tmp1[0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_INV0','BND_PMOS_NellExten')
        tmp2 = self.get_param_KJH4('SRF_INV{}'.format(len(_NumberofGate)-1),'BND_PMOS_NellExten')

        self._DesignParameter['BND_PMOS_NwellExten']['_XWidth'] = abs( tmp2[0][0][0]['_XY_right'][0] - tmp1[0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOS_NwellExten']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_PMOS_NwellExten']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_INV0','BND_PMOS_NellExten')
        target_coord = tmp1[0][0][0]['_XY_up_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOS_NwellExten')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOS_NwellExten')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_PMOS_NwellExten']['_XYCoordinates'] = tmpXY







        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Covering: NMOS
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## Covering: NMOS: SLVT
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NMOS_XVTExten'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['{}'.format(_XVT)][0],
            _Datatype=DesignParameters._LayerMapping['{}'.format(_XVT)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_INV0','SRF_NMOS','BND_{}Layer'.format(_XVT))
        self._DesignParameter['BND_NMOS_XVTExten']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_INV0','SRF_NMOS','BND_{}Layer'.format(_XVT))
        tmp2 = self.get_param_KJH4('SRF_INV{}'.format(len(_NumberofGate)-1),'SRF_NMOS','BND_{}Layer'.format(_XVT))

        self._DesignParameter['BND_NMOS_XVTExten']['_XWidth'] = abs( tmp2[0][0][0][0]['_XY_right'][0] - tmp1[0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NMOS_XVTExten']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_NMOS_XVTExten']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_INV0','SRF_NMOS','BND_{}Layer'.format(_XVT))
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NMOS_XVTExten')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NMOS_XVTExten')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_NMOS_XVTExten']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Erase Cont
        del self._DesignParameter['SRF_Pbody']['_DesignObj']._DesignParameter['SRF_PbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_COLayer']
        del self._DesignParameter['SRF_Nbody']['_DesignObj']._DesignParameter['SRF_NbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_COLayer']

        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')
        InverterChain_end_time = time.time()
        self.InverterChain_elapsed_time = InverterChain_end_time - InverterChain_KJH_start_time

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ZZ01_J00_01_InverterChain_Fixed'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'J00_01_InverterChain_PAD_Buffer2'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
## Inverter Chain
    ## InvChain Common
        _PMOSXvt2NMOSXvt    = 500,      # number

    ## Inverter Chain
        ## Inv1 common
        _NumberofGate   =   [1,2,4,8],  # Vector
        _ChannelLength  =   30,         # Scalar
        _XVT            =   'SLVT',     # 'SLVT'

        ## Inv1 NMOS
        _Inv_NMOS_ChannelWidth           = 400,     # Scalar

        ## Inv1 PMOS
        _Inv_PMOS_ChannelWidth           = 800,     # Scalar

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
