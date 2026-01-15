
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
from KJH91_Projects.Project_ADC.Layoutgen_code.J00_CDACPreDriver_InvBuffer_KJH0_RCHybrid import J00_01_InverterChain_KJH


## Define Class
class _CDAC_PreDriver(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
        ## Distance
        _Distance           = 12096,     # Number
        ## Number of Bit
        _NumBit             = 12,       #Number
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
                                  ## Distance
                                  _Distance           = 12096,     # Number
                                  ## Number of Bit
                                  _NumBit             = 12,       #Number
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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## INV
        for j in range(0,len(_NumberofGate)):
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  INV: Sref Gen.
            SRF_Name = 'SRF_InvChain{}'.format(j)
            ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
            _Caculation_Parameters = copy.deepcopy(J00_01_InverterChain_KJH._InverterChain._ParametersForDesignCalculation)
            ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
            _Caculation_Parameters['_Pbody_NumCont']                = _Pbody_NumCont
            _Caculation_Parameters['_Nbody_NumCont']                = _Nbody_NumCont
            _Caculation_Parameters['_PMOSXvt2NMOSXvt']              = _PMOSXvt2NMOSXvt
            _Caculation_Parameters['_XvtTop2Pbody']                 = _XvtTop2Pbody
            _Caculation_Parameters['_Xvtdown2Nbody']                = _Xvtdown2Nbody

            _Caculation_Parameters['_NumberofGate']                 = _NumberofGate[j]
            _Caculation_Parameters['_ChannelLength']                = _ChannelLength
            _Caculation_Parameters['_XVT']                          = _XVT

            _Caculation_Parameters['_Inv_NMOS_ChannelWidth']        = _Inv_NMOS_ChannelWidth
            _Caculation_Parameters['_Inv_NMOS_POGate_Comb_length']  = _Inv_NMOS_POGate_Comb_length
            _Caculation_Parameters['_Inv_PMOS_ChannelWidth']        = _Inv_PMOS_ChannelWidth
            _Caculation_Parameters['_Inv_PMOS_POGate_Comb_length']  = _Inv_PMOS_POGate_Comb_length

            ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
            self._DesignParameter[SRF_Name] = self._SrefElementDeclaration(_DesignObj=J00_01_InverterChain_KJH._InverterChain(_DesignParameter=None, _Name='{}:{}'.format(_Name,SRF_Name)))[0]

            ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
            self._DesignParameter[SRF_Name]['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle: ex)'_NMOS_POWER'
            self._DesignParameter[SRF_Name]['_Angle'] = 0

            ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
            self._DesignParameter[SRF_Name]['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
            self._DesignParameter[SRF_Name]['_XYCoordinates'] = [[0, 0]]

            if j ==0:
                tmpXY = [[0,0]]
                                ## Define coordinates
                self._DesignParameter[SRF_Name]['_XYCoordinates'] = tmpXY
            else:
                                ## Calculate
                tmpXY =[]
                                    ## Target_coord: _XY_type1
                                    ##X
                tmp1_1 = self.get_param_KJH4('SRF_InvChain{}'.format(j-1),'SRF_Input_ViaM1Mx','SRF_ViaM1M2','BND_Met1Layer')
                target_coord = tmp1_1[0][0][0][0][0]['_XY_left']
                                    ## Approaching_coord: _XY_type2
                tmp2 = self.get_param_KJH4(SRF_Name,'SRF_Input_ViaM1Mx','SRF_ViaM1M2','BND_Met1Layer')
                approaching_coord = tmp2[0][0][0][0][0]['_XY_left']
                                    ## Sref coord
                tmp3 = self.get_param_KJH4(SRF_Name)
                Scoord = tmp3[0][0]['_XY_origin']
                                    ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                New_Scoord[0] = New_Scoord[0] + _Distance
                tmpXY.append(New_Scoord)
                                ## Define coordinates
                self._DesignParameter[SRF_Name]['_XYCoordinates'] = tmpXY














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
        tmp1 = self.get_param_KJH4('SRF_InvChain0','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_Pbody_M1Exten']['_YWidth'] = tmp1[0][0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_InvChain0','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_InvChain{}'.format(len(_NumberofGate)-1),'SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_Pbody_M1Exten']['_XWidth'] = abs( tmp2[0][0][0][0][0]['_XY_right'][0]- tmp1[0][0][0][0][0]['_XY_left'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Pbody_M1Exten']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Pbody_M1Exten']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_InvChain0','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
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
        tmp1 = self.get_param_KJH4('SRF_InvChain0', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_ODLayer')
        self._DesignParameter['BND_Pbody_RXExten']['_YWidth'] = tmp1[0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_InvChain0', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_ODLayer')
        tmp2 = self.get_param_KJH4('SRF_InvChain{}'.format(len(_NumberofGate) - 1), 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_ODLayer')
        self._DesignParameter['BND_Pbody_RXExten']['_XWidth'] = abs( tmp2[0][0][0][0][0]['_XY_right'][0] - tmp1[0][0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Pbody_RXExten']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Pbody_RXExten']['_XYCoordinates'] = [[0, 0]]

        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_InvChain0','SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_ODLayer')
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
        tmp1 = self.get_param_KJH4('SRF_InvChain0','SRF_Pbody','SRF_PbodyContactPhyLen', 'BND_PPLayer')
        self._DesignParameter['BND_Pbody_PPExten']['_YWidth'] = tmp1[0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_InvChain0','SRF_Pbody','SRF_PbodyContactPhyLen', 'BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_InvChain{}'.format(len(_NumberofGate) - 1), 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_PPLayer')
        self._DesignParameter['BND_Pbody_PPExten']['_XWidth'] = abs( tmp2[0][0][0][0][0]['_XY_right'][0] - tmp1[0][0][0][0][0]['_XY_left'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Pbody_PPExten']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_Pbody_PPExten']['_XYCoordinates'] = [[0, 0]]

        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_InvChain0','SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_PPLayer')
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
        tmp1 = self.get_param_KJH4('SRF_InvChain0','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_Nbody_M1Exten']['_YWidth'] = tmp1[0][0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_InvChain0','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_InvChain{}'.format(len(_NumberofGate) - 1), 'SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        self._DesignParameter['BND_Nbody_M1Exten']['_XWidth'] = abs( tmp2[0][0][0][0][0]['_XY_right'][0]- tmp1[0][0][0][0][0]['_XY_left'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Nbody_M1Exten']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Nbody_M1Exten']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_InvChain0','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
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
        tmp1 = self.get_param_KJH4('SRF_InvChain0','SRF_Nbody','SRF_NbodyContactPhyLen','BND_ODLayer')
        self._DesignParameter['BND_Nbody_RXExten']['_YWidth'] = tmp1[0][0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_InvChain0','SRF_Nbody','SRF_NbodyContactPhyLen','BND_ODLayer')
        tmp2 = self.get_param_KJH4('SRF_InvChain{}'.format(len(_NumberofGate) - 1), 'SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_ODLayer')

        self._DesignParameter['BND_Nbody_RXExten']['_XWidth'] = abs( tmp2[0][0][0][0][0]['_XY_right'][0]- tmp1[0][0][0][0][0]['_XY_left'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Nbody_RXExten']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Nbody_RXExten']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_InvChain0','SRF_Nbody','SRF_NbodyContactPhyLen','BND_ODLayer')
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
        tmp1 = self.get_param_KJH4('SRF_InvChain0','SRF_INV0','BND_PMOS_NellExten')
        self._DesignParameter['BND_Nbody_NwellExten']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_InvChain0','SRF_INV0','BND_PMOS_NellExten')
        tmp2 = self.get_param_KJH4('SRF_InvChain{}'.format(len(_NumberofGate) - 1),'SRF_INV{}'.format(len(_NumberofGate[-1])-1),'BND_PMOS_NellExten')

        self._DesignParameter['BND_Nbody_NwellExten']['_XWidth'] = abs( tmp2[0][0][0][0]['_XY_right'][0]- tmp1[0][0][0][0]['_XY_left'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Nbody_NwellExten']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Nbody_NwellExten']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_InvChain0','SRF_INV0','BND_PMOS_NellExten')
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
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

        # ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Body_Cover.
        # ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Body_Cover.: Nbody
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Nbody Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A07_NbodyContactPhyLen_KJH3._NbodyContactPhyLen._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length'] = None
        _Caculation_Parameters['_NumCont'] = _Nbody_NumCont
        _Caculation_Parameters['_Vtc_flag'] = False

        ## Calculate '_Length'
        # tmp = self.get_outter_KJH4('SRF_NMOS')
        tmp = self.get_param_KJH4('BND_Nbody_M1Exten')
        _Caculation_Parameters['_Length'] = tmp[0][0]['_Xwidth']

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
        tmp1 = self.get_param_KJH4('BND_Nbody_M1Exten')
        target_coord = tmp1[0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_Nbody', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Nbody')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['SRF_Nbody']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Pbody Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length'] = None
        _Caculation_Parameters['_NumCont'] = _Pbody_NumCont
        _Caculation_Parameters['_Vtc_flag'] = False

        ## Calculate '_Length'
        tmp = self.get_param_KJH4('BND_Pbody_M1Exten')
        _Caculation_Parameters['_Length'] = tmp[0][0]['_Xwidth']

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
        tmp1 = self.get_param_KJH4('BND_Pbody_M1Exten')
        target_coord = tmp1[0][0]['_XY_down_left']

        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pbody')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['SRF_Pbody']['_XYCoordinates'] = tmpXY

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
    libname = 'Proj_ZZ00_RcdacSar_J00_02_CDAC_PreDriver_KJH'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'J00_02_CDAC_PreDriver_v0_466'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

    ## Distance of buf2buf
        _Distance           = 12096,     # Number

    ## InvChain Common
        _Pbody_NumCont      = 2,        # number
        _Nbody_NumCont      = 2,        # number
        _PMOSXvt2NMOSXvt    = 400,      # number
        _XvtTop2Pbody       = None,     # number/None(Minimum)
        _Xvtdown2Nbody      = None,     # number/None(Minimum)

    ## Inverter Chain
        ## Inv1 common
        _NumberofGate   =   [ [1,2,4,8], [1,2,4,8], [1,2,4,8], [2,2,2,2,2] ],  # Vector
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
    LayoutObj = _CDAC_PreDriver(_DesignParameter=None, _Name=cellname)
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
