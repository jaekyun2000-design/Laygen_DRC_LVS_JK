## Import Basic Modules
    ## Engine
#from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import StickDiagram
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import DesignParameters
from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import DRC

    ## Library
import copy
import time

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import Slicer
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A14_Mosfet_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.E01_ComparatorWtLatch_Fixed import E01_00_Inverter



## Define Class
class _Buffer(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
## Buffer
    ## Common
        # XVT
        _Buf_XVT='SLVT',
        # Body
        _Buf_NMOS_Pbody_XvtTop2Pbody=None,  # Number/None(Minimum)
        _Buf_PMOS_Nbody_Xvtdown2Nbody=None,  # Number/None(Minimum)
        # Height
        _Buf_PMOSXvt2NMOSXvt=1800,  # number
    ## Inverter1
            #Nmos
        _Buf_Inv1_NMOS_NumberofGate          = 1,        # Number
        _Buf_Inv1_NMOS_ChannelWidth          = 400,      # Number
        _Buf_Inv1_NMOS_ChannelLength         = 30,       # Number
            #Pmos
        _Buf_Inv1_PMOS_NumberofGate          = 1,        # Number
        _Buf_Inv1_PMOS_ChannelWidth          = 800,      # Number
        _Buf_Inv1_PMOS_ChannelLength         = 30,       # Number
    ## Inverter2
            #Nmos
        _Buf_Inv2_NMOS_NumberofGate          = 1,        # Number
        _Buf_Inv2_NMOS_ChannelWidth          = 400,      # Number
        _Buf_Inv2_NMOS_ChannelLength         = 30,       # Number
            #Pmos
        _Buf_Inv2_PMOS_NumberofGate          = 1,        # Number
        _Buf_Inv2_PMOS_ChannelWidth          = 800,      # Number
        _Buf_Inv2_PMOS_ChannelLength         = 30,       # Number

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
## Buffer
    ## Common
        # XVT
        _Buf_XVT='SLVT',
        # Body
        _Buf_NMOS_Pbody_XvtTop2Pbody=None,  # Number/None(Minimum)
        _Buf_PMOS_Nbody_Xvtdown2Nbody=None,  # Number/None(Minimum)
        # Height
        _Buf_PMOSXvt2NMOSXvt=1800,  # number
    ## Inverter1
            #Nmos
        _Buf_Inv1_NMOS_NumberofGate          = 1,        # Number
        _Buf_Inv1_NMOS_ChannelWidth          = 400,      # Number
        _Buf_Inv1_NMOS_ChannelLength         = 30,       # Number
            #Pmos
        _Buf_Inv1_PMOS_NumberofGate          = 1,        # Number
        _Buf_Inv1_PMOS_ChannelWidth          = 800,      # Number
        _Buf_Inv1_PMOS_ChannelLength         = 30,       # Number
    ## Inverter2
            #Nmos
        _Buf_Inv2_NMOS_NumberofGate          = 1,        # Number
        _Buf_Inv2_NMOS_ChannelWidth          = 400,      # Number
        _Buf_Inv2_NMOS_ChannelLength         = 30,       # Number
            #Pmos
        _Buf_Inv2_PMOS_NumberofGate          = 1,        # Number
        _Buf_Inv2_PMOS_ChannelWidth          = 800,      # Number
        _Buf_Inv2_PMOS_ChannelLength         = 30,       # Number
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
        ##################################################################################################################################### XVT2body cal
        ############################################################################################## XVT2body cal : Inv1 gen
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(E01_00_Inverter._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        ## Inverter
            #Common
        _Caculation_Parameters['_XVT'] = _Buf_XVT
            # Nmos
        _Caculation_Parameters['_NMOS_NumberofGate'] = _Buf_Inv1_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth'] = _Buf_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength'] = _Buf_Inv1_NMOS_ChannelLength
            # Pmos
        _Caculation_Parameters['_PMOS_NumberofGate'] = _Buf_Inv1_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth'] = _Buf_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength'] = _Buf_Inv1_PMOS_ChannelLength
            # Body
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody'] = _Buf_NMOS_Pbody_XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody'] = _Buf_PMOS_Nbody_Xvtdown2Nbody
            # Height
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
        ############################################################################################## XVT2body cal : Inv2 gen
        _Caculation_Parameters = copy.deepcopy(E01_00_Inverter._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        ## Inverter
            #Common
        _Caculation_Parameters['_XVT'] = _Buf_XVT
            # Nmos
        _Caculation_Parameters['_NMOS_NumberofGate'] = _Buf_Inv2_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth'] = _Buf_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength'] = _Buf_Inv2_NMOS_ChannelLength
            # Pmos
        _Caculation_Parameters['_PMOS_NumberofGate'] = _Buf_Inv2_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth'] = _Buf_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength'] = _Buf_Inv2_PMOS_ChannelLength
            # Body
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody'] = _Buf_NMOS_Pbody_XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody'] = _Buf_PMOS_Nbody_Xvtdown2Nbody
            # Height
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
        ############################################################################################## XVT2body cal : XVT2body Cal
        tmp1 = self.get_param_KJH4('SRF_Inverter1','SRF_NMOS','BND_{}Layer'.format(_Buf_XVT))
        tmp2 = self.get_param_KJH4('SRF_Inverter1','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        Inv1_Xvttop2Pbody = abs(tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0]['_XY_up'][1])
        tmp3 = self.get_param_KJH4('SRF_Inverter1','SRF_PMOS','BND_{}Layer'.format(_Buf_XVT))
        tmp4 = self.get_param_KJH4('SRF_Inverter1','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        Inv1_Xvtdown2Nbody = abs(tmp4[0][0][0][0][0]['_XY_down'][1] - tmp3[0][0][0][0]['_XY_down'][1])

        tmp5 = self.get_param_KJH4('SRF_Inverter2','SRF_NMOS','BND_{}Layer'.format(_Buf_XVT))
        tmp6 = self.get_param_KJH4('SRF_Inverter2','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        Inv2_Xvttop2Pbody = abs(tmp5[0][0][0][0]['_XY_up'][1] - tmp6[0][0][0][0][0]['_XY_up'][1])
        tmp7 = self.get_param_KJH4('SRF_Inverter2','SRF_PMOS','BND_{}Layer'.format(_Buf_XVT))
        tmp8 = self.get_param_KJH4('SRF_Inverter2','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        Inv2_Xvtdown2Nbody = abs(tmp8[0][0][0][0][0]['_XY_down'][1] - tmp7[0][0][0][0]['_XY_down'][1])

        tmp_Xvttop2Pbody = max(Inv1_Xvttop2Pbody,Inv2_Xvttop2Pbody)
        tmp_Xvtdown2Nbody = max(Inv1_Xvtdown2Nbody,Inv2_Xvtdown2Nbody)


        ##################################################################################################################################### Inv1 generation
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(E01_00_Inverter._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        ## Inverter
            #Common
        _Caculation_Parameters['_XVT'] = _Buf_XVT
            # Nmos
        _Caculation_Parameters['_NMOS_NumberofGate'] = _Buf_Inv1_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth'] = _Buf_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength'] = _Buf_Inv1_NMOS_ChannelLength
            # Pmos
        _Caculation_Parameters['_PMOS_NumberofGate'] = _Buf_Inv1_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth'] = _Buf_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength'] = _Buf_Inv1_PMOS_ChannelLength
            # Body
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody'] = tmp_Xvttop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody'] = tmp_Xvtdown2Nbody
            # Height
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


        ##################################################################################################################################### Inv2 generation
        _Caculation_Parameters = copy.deepcopy(E01_00_Inverter._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        ## Inverter
            #Common
        _Caculation_Parameters['_XVT'] = _Buf_XVT
            # Nmos
        _Caculation_Parameters['_NMOS_NumberofGate'] = _Buf_Inv2_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth'] = _Buf_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength'] = _Buf_Inv2_NMOS_ChannelLength
            # Pmos
        _Caculation_Parameters['_PMOS_NumberofGate'] = _Buf_Inv2_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth'] = _Buf_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength'] = _Buf_Inv2_PMOS_ChannelLength
            # Body
        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody'] = tmp_Xvttop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody'] = tmp_Xvtdown2Nbody
            # Height
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

        ##################################################################################################################################### pre-defined routing point(coordY)
        tmp = self.get_param_KJH4('SRF_Inverter1', 'BND_Input_Vtc_M1')
        upperroutepnty = max(int(tmp[0][0][0]['_XY_down'][1]*0.333 + tmp[0][0][0]['_XY_up'][1]*0.666),int(tmp[0][0][0]['_XY_down'][1]*0.666 + tmp[0][0][0]['_XY_up'][1]*0.333))
        lowerroutepnty = min(int(tmp[0][0][0]['_XY_down'][1]*0.333 + tmp[0][0][0]['_XY_up'][1]*0.666),int(tmp[0][0][0]['_XY_down'][1]*0.666 + tmp[0][0][0]['_XY_up'][1]*0.333))

        #####################################################################################################################################
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

        #####################################################################################################################################
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
        #####################################################################################################################################
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

        #####################################################################################################################################
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

        #####################################################################################################################################
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

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ZZ01_E01_01_Buffer_Fixed'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'E01_SAOutputBuffer_v0'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
## Buffer
    ## Common
        # XVT
        _Buf_XVT='SLVT',
        # Body
        _Buf_NMOS_Pbody_XvtTop2Pbody=None,  # Number/None(Minimum)
        _Buf_PMOS_Nbody_Xvtdown2Nbody=None,  # Number/None(Minimum)
        # Height
        _Buf_PMOSXvt2NMOSXvt=1800,  # number
    ## Inverter1
            #Nmos
        _Buf_Inv1_NMOS_NumberofGate          = 1,        # Number
        _Buf_Inv1_NMOS_ChannelWidth          = 400,      # Number
        _Buf_Inv1_NMOS_ChannelLength         = 30,       # Number
            #Pmos
        _Buf_Inv1_PMOS_NumberofGate          = 1,        # Number
        _Buf_Inv1_PMOS_ChannelWidth          = 800,      # Number
        _Buf_Inv1_PMOS_ChannelLength         = 30,       # Number
    ## Inverter2
            #Nmos
        _Buf_Inv2_NMOS_NumberofGate          = 1,        # Number
        _Buf_Inv2_NMOS_ChannelWidth          = 800,      # Number
        _Buf_Inv2_NMOS_ChannelLength         = 30,       # Number
            #Pmos
        _Buf_Inv2_PMOS_NumberofGate          = 1,        # Number
        _Buf_Inv2_PMOS_ChannelWidth          = 1600,      # Number
        _Buf_Inv2_PMOS_ChannelLength         = 30,       # Number

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
