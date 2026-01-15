## Import Basic Modules
    ## Engine
#from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import StickDiagram
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import DesignParameters
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import DRC

    ## Library
import copy
import time

    ## KJH91 Basic Building Blocks
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import Slicer
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A14_Mosfet_KJH2
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E01_ComparatorWtLatch_YJH import E01_00_Inverter



## Define Class
class _Buffer(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
        ## StrongARMLatch Output Buffer Sizing
        # Inverter1
        _Buf_Inv1_NMOS_ChannelWidth=None,  # Number
        _Buf_Inv1_NMOS_ChannelLength=None,  # Number
        _Buf_Inv1_NMOS_NumberofGate=None,  # Number
        _Buf_Inv1_NMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Buf_Inv1_NMOS_POGate_Comb_length=None,  # None/Number

        _Buf_Inv1_PMOS_ChannelWidth=None,  # Number
        _Buf_Inv1_PMOS_ChannelLength=None,  # Number
        _Buf_Inv1_PMOS_NumberofGate=None,  # Number
        _Buf_Inv1_PMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Buf_Inv1_PMOS_POGate_Comb_length=None,  # None/Number

        # Inverter2
        _Buf_Inv2_NMOS_ChannelWidth=None,  # Number
        _Buf_Inv2_NMOS_ChannelLength=None,  # Number
        _Buf_Inv2_NMOS_NumberofGate=None,  # Number
        _Buf_Inv2_NMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Buf_Inv2_NMOS_POGate_Comb_length=None,  # None/Number

        _Buf_Inv2_PMOS_ChannelWidth=None,  # Number
        _Buf_Inv2_PMOS_ChannelLength=None,  # Number
        _Buf_Inv2_PMOS_NumberofGate=None,  # Number
        _Buf_Inv2_PMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Buf_Inv2_PMOS_POGate_Comb_length=None,  # None/Number

        _Buf_NMOS_Pbody_NumCont=None,
        _Buf_NMOS_Pbody_XvtTop2Pbody=None,
        _Buf_PMOS_Nbody_NumCont=None,
        _Buf_PMOS_Nbody_Xvtdown2Nbody=None,
        _Buf_PMOSXvt2NMOSXvt=None,
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
                                  ## StrongARMLatch Output Buffer Sizing
                                  # Inverter1
                                  _Buf_Inv1_NMOS_ChannelWidth=None,  # Number
                                  _Buf_Inv1_NMOS_ChannelLength=None,  # Number
                                  _Buf_Inv1_NMOS_NumberofGate=None,  # Number
                                  _Buf_Inv1_NMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _Buf_Inv1_NMOS_POGate_Comb_length=None,  # None/Number

                                  _Buf_Inv1_PMOS_ChannelWidth=None,  # Number
                                  _Buf_Inv1_PMOS_ChannelLength=None,  # Number
                                  _Buf_Inv1_PMOS_NumberofGate=None,  # Number
                                  _Buf_Inv1_PMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _Buf_Inv1_PMOS_POGate_Comb_length=None,  # None/Number

                                  # Inverter2
                                  _Buf_Inv2_NMOS_ChannelWidth=None,  # Number
                                  _Buf_Inv2_NMOS_ChannelLength=None,  # Number
                                  _Buf_Inv2_NMOS_NumberofGate=None,  # Number
                                  _Buf_Inv2_NMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _Buf_Inv2_NMOS_POGate_Comb_length=None,  # None/Number

                                  _Buf_Inv2_PMOS_ChannelWidth=None,  # Number
                                  _Buf_Inv2_PMOS_ChannelLength=None,  # Number
                                  _Buf_Inv2_PMOS_NumberofGate=None,  # Number
                                  _Buf_Inv2_PMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _Buf_Inv2_PMOS_POGate_Comb_length=None,  # None/Number

                                  _Buf_NMOS_Pbody_NumCont=None,
                                  _Buf_NMOS_Pbody_XvtTop2Pbody=None,
                                  _Buf_PMOS_Nbody_NumCont=None,
                                  _Buf_PMOS_Nbody_Xvtdown2Nbody=None,
                                  _Buf_PMOSXvt2NMOSXvt=None,
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

        ####### Inv1 generation
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(E01_00_Inverter._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType'] = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn'] = 'Up'
        _Caculation_Parameters['_NMOS_NumberofGate'] = _Buf_Inv1_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth'] = _Buf_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength'] = _Buf_Inv1_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing'] = None
        _Caculation_Parameters['_NMOS_SDWidth'] = None
        _Caculation_Parameters['_NMOS_XVT'] = _Buf_Inv1_NMOS_XVT
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
        _Caculation_Parameters['_NMOS_Xvt_Placement'] = 'Up'
        _Caculation_Parameters['_NMOS_POGate_Comb_TF'] = True
        _Caculation_Parameters['_NMOS_POGate_Comb_length'] = _Buf_Inv1_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF'] = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx'] = [0, 1]

        _Caculation_Parameters['_PMOS_MosType'] = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn'] = 'Dn'
        _Caculation_Parameters['_PMOS_NumberofGate'] = _Buf_Inv1_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth'] = _Buf_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength'] = _Buf_Inv1_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing'] = None
        _Caculation_Parameters['_PMOS_SDWidth'] = None
        _Caculation_Parameters['_PMOS_XVT'] = _Buf_Inv1_PMOS_XVT
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
        _Caculation_Parameters['_PMOS_POGate_Comb_length'] = _Buf_Inv1_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF'] = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx'] = [0,1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont'] = _Buf_NMOS_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody'] = _Buf_NMOS_Pbody_XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_NumCont'] = _Buf_PMOS_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody'] = _Buf_PMOS_Nbody_Xvtdown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt'] = _Buf_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Inverter1'] = self._SrefElementDeclaration(_DesignObj=E01_00_Inverter._Inverter(_DesignParameter=None, _Name='{}:SRF_Inverter1'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Inverter1']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inverter1']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inverter1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inverter1']['_XYCoordinates'] = [[0, 0]]

        _Caculation_Parameters = copy.deepcopy(E01_00_Inverter._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOS_MosType'] = 'NMOS'
        _Caculation_Parameters['_NMOS_MosUpDn'] = 'Up'
        _Caculation_Parameters['_NMOS_NumberofGate'] = _Buf_Inv2_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth'] = _Buf_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength'] = _Buf_Inv2_NMOS_ChannelLength
        _Caculation_Parameters['_NMOS_GateSpacing'] = None
        _Caculation_Parameters['_NMOS_SDWidth'] = None
        _Caculation_Parameters['_NMOS_XVT'] = _Buf_Inv2_NMOS_XVT
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
        _Caculation_Parameters['_NMOS_Xvt_Placement'] = 'Up'
        _Caculation_Parameters['_NMOS_POGate_Comb_TF'] = True
        _Caculation_Parameters['_NMOS_POGate_Comb_length'] = _Buf_Inv2_NMOS_POGate_Comb_length
        _Caculation_Parameters['_NMOS_POGate_Via_TF'] = True
        _Caculation_Parameters['_NMOS_POGate_ViaMxMx'] = [0, 1]

        _Caculation_Parameters['_PMOS_MosType'] = 'PMOS'
        _Caculation_Parameters['_PMOS_MosUpDn'] = 'Dn'
        _Caculation_Parameters['_PMOS_NumberofGate'] = _Buf_Inv2_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth'] = _Buf_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength'] = _Buf_Inv2_PMOS_ChannelLength
        _Caculation_Parameters['_PMOS_GateSpacing'] = None
        _Caculation_Parameters['_PMOS_SDWidth'] = None
        _Caculation_Parameters['_PMOS_XVT'] = _Buf_Inv2_PMOS_XVT
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
        _Caculation_Parameters['_PMOS_POGate_Comb_length'] = _Buf_Inv2_PMOS_POGate_Comb_length
        _Caculation_Parameters['_PMOS_POGate_Via_TF'] = True
        _Caculation_Parameters['_PMOS_POGate_ViaMxMx'] = [0, 1]

        _Caculation_Parameters['_NMOS_Pbody_NumCont'] = _Buf_NMOS_Pbody_NumCont
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody'] = _Buf_NMOS_Pbody_XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_NumCont'] = _Buf_PMOS_Nbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody'] = _Buf_PMOS_Nbody_Xvtdown2Nbody
        _Caculation_Parameters['_PMOSXvt2NMOSXvt'] = _Buf_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Inverter2'] = self._SrefElementDeclaration(_DesignObj=E01_00_Inverter._Inverter(_DesignParameter=None, _Name='{}:SRF_Inverter2'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Inverter2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inverter2']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inverter2']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_Inverter2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Inverter1','SRF_NMOS', 'BND_PODummyLayer')
        target_coord = tmp1[0][0][-1][0]['_XY_up_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_Inverter2','SRF_NMOS', 'BND_PODummyLayer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Inverter2')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[0] = Scoord[0] + 96
        # Scoord[0] = Scoord[0] + 140
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['SRF_Inverter2']['_XYCoordinates'] = tmpXY


        # pre-defined routing point(coordY)
        tmp = self.get_param_KJH4('SRF_Inverter1', 'BND_Input_Vtc_M1')
        upperroutepnty = max(int(tmp[0][0][0]['_XY_down'][1]*0.333 + tmp[0][0][0]['_XY_up'][1]*0.666),int(tmp[0][0][0]['_XY_down'][1]*0.666 + tmp[0][0][0]['_XY_up'][1]*0.333))
        lowerroutepnty = min(int(tmp[0][0][0]['_XY_down'][1]*0.333 + tmp[0][0][0]['_XY_up'][1]*0.666),int(tmp[0][0][0]['_XY_down'][1]*0.666 + tmp[0][0][0]['_XY_up'][1]*0.333))


        ######## Inverter1 Input Via
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Inv1Input_ViaM1M2'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Inv1Input_ViaM1M2'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Inv1Input_ViaM1M2']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Inv1Input_ViaM1M2']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Inv1Input_ViaM1M2']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Inv1Input_ViaM1M2']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        tmp1 = self.get_param_KJH4('SRF_Inverter1','BND_Input_Vtc_M1')
        target_coord = [tmp1[0][0][0]['_XY_left'][0], lowerroutepnty]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Inv1Input_ViaM1M2','SRF_ViaM1M2','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_right']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Inv1Input_ViaM1M2')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Inv1Input_ViaM1M2']['_XYCoordinates'] = tmpXY



        ######## Inverter1 Out -> Inverter2 In Routing
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Inv1Out2Inv2In_ViaM1M2'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Inv1Out2Inv2In_ViaM1M2'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Inv1Out2Inv2In_ViaM1M2']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Inv1Out2Inv2In_ViaM1M2']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Inv1Out2Inv2In_ViaM1M2']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Inv1Out2Inv2In_ViaM1M2']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        tmp1 = self.get_param_KJH4('SRF_Inverter1','BND_Out_Vtc_M2')
        tmp2 = self.get_param_KJH4('SRF_Inverter2','BND_Input_Vtc_M1')
        tmp = int((tmp1[0][0][0]['_XY_left'][0] + tmp2[0][0][0]['_XY_right'][0])/2)
        target_coord = [tmp, upperroutepnty]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Inv1Out2Inv2In_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Inv1Out2Inv2In_ViaM1M2')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Inv1Out2Inv2In_ViaM1M2']['_XYCoordinates'] = tmpXY


        ## BND_Inv1Out2Inv2In_Hrz_M1 generation
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Inv1Out2Inv2In_Hrz_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Inv1Out2Inv2In_Hrz_M1']['_YWidth'] = 50

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Inv1Out2Inv2In_ViaM1M2','SRF_ViaM1M2','BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_Inverter2','BND_Input_Vtc_M1')
        self._DesignParameter['BND_Inv1Out2Inv2In_Hrz_M1']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_left'][0] - tmp2[0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Inv1Out2Inv2In_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Inv1Out2Inv2In_ViaM1M2','SRF_ViaM1M2','BND_Met1Layer')
        target_coord = [tmp1[0][0][0][0]['_XY_left'][0], upperroutepnty]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Inv1Out2Inv2In_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Inv1Out2Inv2In_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Inv1Out2Inv2In_Hrz_M1']['_XYCoordinates'] = tmpXY


        ## BND_Inv1Out2Inv2In_Hrz_M2 generation
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Inv1Out2Inv2In_Hrz_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Inv1Out2Inv2In_Hrz_M2']['_YWidth'] = 50

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Inv1Out2Inv2In_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
        tmp2 = self.get_param_KJH4('SRF_Inverter1','BND_Out_Vtc_M2')
        self._DesignParameter['BND_Inv1Out2Inv2In_Hrz_M2']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0]['_XY_left'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Inv1Out2Inv2In_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Inv1Out2Inv2In_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
        target_coord = [tmp1[0][0][0][0]['_XY_right'][0], upperroutepnty]
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Inv1Out2Inv2In_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Inv1Out2Inv2In_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Inv1Out2Inv2In_Hrz_M2']['_XYCoordinates'] = tmpXY


        ######## Inverter2 Output Via
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Inv2Output_ViaM1M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Inv2Output_ViaM1M3'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Inv2Output_ViaM1M3']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Inv2Output_ViaM1M3']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Inv2Output_ViaM1M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Inv2Output_ViaM1M3']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        tmp1 = self.get_param_KJH4('SRF_Inverter2','BND_Out_Vtc_M2')
        target_coord = [tmp1[0][0][0]['_XY_left'][0], lowerroutepnty]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Inv2Output_ViaM1M3','SRF_ViaM1M2','BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_left']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Inv2Output_ViaM1M3')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Inv2Output_ViaM1M3']['_XYCoordinates'] = tmpXY




        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_YJH
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ADC_E01_ComparatorWtLatch_v0'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'E01_SAOutputBuffer_v0'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        ## StrongARMLatch Output Buffer Sizing
        # Inverter1
        _Buf_Inv1_NMOS_ChannelWidth=600,  # Number
        _Buf_Inv1_NMOS_ChannelLength=30,  # Number
        _Buf_Inv1_NMOS_NumberofGate=42,  # Number
        _Buf_Inv1_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Buf_Inv1_NMOS_POGate_Comb_length=100,  # None/Number

        _Buf_Inv1_PMOS_ChannelWidth=1200,  # Number
        _Buf_Inv1_PMOS_ChannelLength=30,  # Number
        _Buf_Inv1_PMOS_NumberofGate=42,  # Number
        _Buf_Inv1_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Buf_Inv1_PMOS_POGate_Comb_length=100,  # None/Number

        # Inverter2
        _Buf_Inv2_NMOS_ChannelWidth=600,  # Number
        _Buf_Inv2_NMOS_ChannelLength=30,  # Number
        _Buf_Inv2_NMOS_NumberofGate=1,  # Number
        _Buf_Inv2_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Buf_Inv2_NMOS_POGate_Comb_length=100,  # None/Number

        _Buf_Inv2_PMOS_ChannelWidth=1200,  # Number
        _Buf_Inv2_PMOS_ChannelLength=30,  # Number
        _Buf_Inv2_PMOS_NumberofGate=1,  # Number
        _Buf_Inv2_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _Buf_Inv2_PMOS_POGate_Comb_length=100,  # None/Number

        _Buf_NMOS_Pbody_NumCont = 2,
        _Buf_NMOS_Pbody_XvtTop2Pbody=None,
        _Buf_PMOS_Nbody_NumCont=2,
        _Buf_PMOS_Nbody_Xvtdown2Nbody=None,
        _Buf_PMOSXvt2NMOSXvt=1000,
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
    LayoutObj = _Buffer(_DesignParameter=None, _Name=cellname)
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
