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
from KJH91_Projects.Project_ADC.Layoutgen_code.F00_CLKBufferTree_Fixed import F00_00_Inverter_v2
from KJH91_Projects.Project_ADC.Layoutgen_code.J00_CDACPreDriver_InvBuffer_KJH0 import J00_02_CDAC_PreDriver_KJH



## Define Class
class _CLKBufferTree(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
## Unit Buffer Size
        #Common
    _UnitBuf_XVT                        = 'SLVT',
        #Nmos
    _UnitBuf_NMOS_NumberofGate          = 1,        # Number
    _UnitBuf_NMOS_ChannelWidth          = 100,      # Number
    _UnitBuf_NMOS_ChannelLength         = 30,       # Number
        #Pmos
    _UnitBuf_PMOS_NumberofGate          = 1,        # Number
    _UnitBuf_PMOS_ChannelWidth          = 100,      # Number
    _UnitBuf_PMOS_ChannelLength         = 30,       # Number
        #Height
    _UnitBuf_PMOSXvt2NMOSXvt            = 1000,     # number

## Buffer Tree structure
    _BufTree_TotalLength        = 50000,
    _BufTree1and2_NumOfStage    = 4,  # len[Buf0, Buf1, ... ] 스테이지 수 (아래 버퍼 사이즈 리스트의 길이와 같아야 함.)
    _BufTree1_SizeofEachStage   = [1, 2, 4, 8],  # [Buf0, Buf1, Buf2 ...]
    _BufTree2_SizeofEachStage   = [1, 3, 4, 17],  # [Buf0, Buf1, Buf2 ...]
    _BufTree_OutputPlacement    = 'Up', #Up/Dn
    _BufTree_OutputVia       = 4,

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
## Unit Buffer Size
        #Common
    _UnitBuf_XVT                        = 'SLVT',
        #Nmos
    _UnitBuf_NMOS_NumberofGate          = 1,        # Number
    _UnitBuf_NMOS_ChannelWidth          = 100,      # Number
    _UnitBuf_NMOS_ChannelLength         = 30,       # Number
        #Pmos
    _UnitBuf_PMOS_NumberofGate          = 1,        # Number
    _UnitBuf_PMOS_ChannelWidth          = 100,      # Number
    _UnitBuf_PMOS_ChannelLength         = 30,       # Number
        #Height
    _UnitBuf_PMOSXvt2NMOSXvt            = 1000,     # number

## Buffer Tree structure
    _BufTree_TotalLength        = 50000,
    _BufTree1and2_NumOfStage    = 4,  # len[Buf0, Buf1, ... ] 스테이지 수 (아래 버퍼 사이즈 리스트의 길이와 같아야 함.)
    _BufTree1_SizeofEachStage   = [1, 2, 4, 8],  # [Buf0, Buf1, Buf2 ...]
    _BufTree2_SizeofEachStage   = [1, 3, 4, 17],  # [Buf0, Buf1, Buf2 ...]
    _BufTree_OutputPlacement    = 'Up', #Up/Dn
    _BufTree_OutputVia       = 4,
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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## Raise Error
        if (len(_BufTree1_SizeofEachStage)) != (len(_BufTree2_SizeofEachStage)):
            raise Exception("버퍼 스테이지의 수와 스테이지에 따른 사이즈 입력 수가 일치하지 않음.")

        if (len(_BufTree2_SizeofEachStage)) != _BufTree1and2_NumOfStage:
            raise Exception("버퍼1의 스테이지 수와 2의 스테이지 수가 일치하지 않음.")

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## Gen BufN_Sequence
        n = _BufTree1and2_NumOfStage-1
        Squence = [[0]]
        for level in range(1, n + 1):
            prev = Squence[-1]
            # 앞쪽 절반: 이전 행의 모든 값에 +1
            first_half = [x + 1 for x in prev]
            # 새로운 행 = first_half + [0] + first_half
            Squence.append(first_half + [0] + first_half)
        BufN_Sequence = Squence[-1]

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## Buf Tree1 Gen for Check BodytoXvt
        XvtTop2Pbody1  =[]
        Xvtdown2Nbody1 =[]
        BufN_width1 = []
        for i in range(_BufTree1and2_NumOfStage):
            _Caculation_Parameters = copy.deepcopy(F00_00_Inverter_v2._Inverter._ParametersForDesignCalculation)
            ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
            _Caculation_Parameters['_XVT']                  = _UnitBuf_XVT
            _Caculation_Parameters['_PMOSXvt2NMOSXvt']      = _UnitBuf_PMOSXvt2NMOSXvt

            _Caculation_Parameters['_NMOS_NumberofGate']    = _UnitBuf_NMOS_NumberofGate * _BufTree1_SizeofEachStage[i]
            _Caculation_Parameters['_NMOS_ChannelWidth']    = _UnitBuf_NMOS_ChannelWidth
            _Caculation_Parameters['_NMOS_ChannelLength']   = _UnitBuf_NMOS_ChannelLength

            _Caculation_Parameters['_PMOS_NumberofGate']    = _UnitBuf_PMOS_NumberofGate * _BufTree1_SizeofEachStage[i]
            _Caculation_Parameters['_PMOS_ChannelWidth']    = _UnitBuf_PMOS_ChannelWidth
            _Caculation_Parameters['_PMOS_ChannelLength']   = _UnitBuf_PMOS_ChannelLength

            _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']  = None
            _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody'] = None

            ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
            self._DesignParameter['SRF_CLKBuf1Inv_Stage{}'.format(i + 1)] = self._SrefElementDeclaration(_DesignObj=F00_00_Inverter_v2._Inverter(_DesignParameter=None,_Name='{}:SRF_CLKBuf1Inv_Stage{}'.format(_Name, i + 1)))[0]

            ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
            self._DesignParameter['SRF_CLKBuf1Inv_Stage{}'.format(i + 1)]['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CLKBuf1Inv_Stage{}'.format(i + 1)]['_Angle'] = 0

            ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CLKBuf1Inv_Stage{}'.format(i + 1)]['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CLKBuf1Inv_Stage{}'.format(i + 1)]['_XYCoordinates'] = [[0, 0]]

            ## Check XVT to body
            tmp1 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(i + 1),'SRF_NMOS', 'BND_{}Layer'.format(_UnitBuf_XVT))
            tmp2 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(i + 1),'SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
            Nmos_distance = abs(tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0]['_XY_up'][1])
            XvtTop2Pbody1.append(Nmos_distance)

            tmp1 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(i + 1),'SRF_PMOS', 'BND_{}Layer'.format(_UnitBuf_XVT))
            tmp2 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(i + 1),'SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
            Pmos_distance = abs(tmp1[0][0][0][0]['_XY_down'][1] - tmp2[0][0][0][0][0]['_XY_down'][1])
            Xvtdown2Nbody1.append(Pmos_distance)

            ## Check Inverter Width
            tmp = self.get_outter_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(i + 1))
            bufWidth = abs(tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0])
            BufN_width1.append(bufWidth)

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## Buf Tree2 Gen for Check BodytoXvt
        XvtTop2Pbody2  =[]
        Xvtdown2Nbody2 =[]
        BufN_width2 = []
        for i in range(_BufTree1and2_NumOfStage):
            _Caculation_Parameters = copy.deepcopy(F00_00_Inverter_v2._Inverter._ParametersForDesignCalculation)
            ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
            _Caculation_Parameters['_XVT']                  = _UnitBuf_XVT
            _Caculation_Parameters['_PMOSXvt2NMOSXvt']      = _UnitBuf_PMOSXvt2NMOSXvt

            _Caculation_Parameters['_NMOS_NumberofGate']    = _UnitBuf_NMOS_NumberofGate * _BufTree2_SizeofEachStage[i]
            _Caculation_Parameters['_NMOS_ChannelWidth']    = _UnitBuf_NMOS_ChannelWidth
            _Caculation_Parameters['_NMOS_ChannelLength']   = _UnitBuf_NMOS_ChannelLength

            _Caculation_Parameters['_PMOS_NumberofGate']    = _UnitBuf_PMOS_NumberofGate * _BufTree2_SizeofEachStage[i]
            _Caculation_Parameters['_PMOS_ChannelWidth']    = _UnitBuf_PMOS_ChannelWidth
            _Caculation_Parameters['_PMOS_ChannelLength']   = _UnitBuf_PMOS_ChannelLength

            _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']  = None
            _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody'] = None

            ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
            self._DesignParameter['SRF_CLKBuf2Inv_Stage{}'.format(i + 1)] = self._SrefElementDeclaration(_DesignObj=F00_00_Inverter_v2._Inverter(_DesignParameter=None,_Name='{}:SRF_CLKBuf2Inv_Stage{}'.format(_Name, i + 1)))[0]

            ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
            self._DesignParameter['SRF_CLKBuf2Inv_Stage{}'.format(i + 1)]['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CLKBuf2Inv_Stage{}'.format(i + 1)]['_Angle'] = 0

            ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CLKBuf2Inv_Stage{}'.format(i + 1)]['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CLKBuf2Inv_Stage{}'.format(i + 1)]['_XYCoordinates'] = [[0, 0]]

            ## Check XVT to body
            tmp1 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(i + 1),'SRF_NMOS', 'BND_{}Layer'.format(_UnitBuf_XVT))
            tmp2 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(i + 1),'SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
            Nmos_distance = abs(tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0]['_XY_up'][1])
            XvtTop2Pbody2.append(Nmos_distance)

            tmp1 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(i + 1),'SRF_PMOS', 'BND_{}Layer'.format(_UnitBuf_XVT))
            tmp2 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(i + 1),'SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
            Pmos_distance = abs(tmp1[0][0][0][0]['_XY_down'][1] - tmp2[0][0][0][0][0]['_XY_down'][1])
            Xvtdown2Nbody2.append(Pmos_distance)

            ## Check Inverter Width
            tmp = self.get_outter_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(i + 1))
            bufWidth = abs(tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0])
            BufN_width2.append(bufWidth)


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## Estimate Buffer tree 1 and 2 total length
        ## Buf Tree1 Width
        tmp_buf_tree1_width = []
        for i in range(len(BufN_width1)):
            tmp = BufN_width1[i] * 2**(i)
            tmp_buf_tree1_width.append(tmp)

        ## Buf Tree2 Width
        tmp_buf_tree2_width = []
        for i in range(len(BufN_width2)):
            tmp = BufN_width2[i] * 2**(i)
            tmp_buf_tree2_width.append(tmp)

        ## Total Width
        Buf_Tree1_Width = sum(tmp_buf_tree1_width)
        Buf_Tree2_Width = sum(tmp_buf_tree2_width)
        Buf_Tree_Total_Width = Buf_Tree1_Width + Buf_Tree2_Width

        NumOfTotalBufs = 2 *len(BufN_Sequence) # Buf tree1 and 2
        MinimumSpaceBtwPodummy = 96

        if _BufTree_TotalLength != None:
            if _BufTree_TotalLength+MinimumSpaceBtwPodummy*len(BufN_Sequence) < Buf_Tree_Total_Width:
                raise Exception("생성될 트리의 길이가 입력받은 '_BufTree_TotalLength'의 길이보다 길어, 레이아웃을 생성할 수 없습니다.")
            else:
                SpaceBtwBuffers = int((_BufTree_TotalLength - Buf_Tree_Total_Width) / (NumOfTotalBufs-1))
        else:
            _CLKBufTree_TotalLength = Buf_Tree_Total_Width
            SpaceBtwBuffers = MinimumSpaceBtwPodummy

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## Cal Xvtdown2Nbody AND XvtTop2Pbody
        Xvtdown2Nbody = max(max(Xvtdown2Nbody1), max(Xvtdown2Nbody2) )
        XvtTop2Pbody = max(max(XvtTop2Pbody1), max(XvtTop2Pbody2) )

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## Buf Tree1 ReGen Applying XVTtoBody
        Tree1_rightmost = []
        Tree1_leftmost = []
        for i in range(_BufTree1and2_NumOfStage):
            _Caculation_Parameters = copy.deepcopy(F00_00_Inverter_v2._Inverter._ParametersForDesignCalculation)
            ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
            _Caculation_Parameters['_XVT']                  = _UnitBuf_XVT
            _Caculation_Parameters['_PMOSXvt2NMOSXvt']      = _UnitBuf_PMOSXvt2NMOSXvt

            _Caculation_Parameters['_NMOS_NumberofGate']    = _UnitBuf_NMOS_NumberofGate * _BufTree1_SizeofEachStage[i]
            _Caculation_Parameters['_NMOS_ChannelWidth']    = _UnitBuf_NMOS_ChannelWidth
            _Caculation_Parameters['_NMOS_ChannelLength']   = _UnitBuf_NMOS_ChannelLength

            _Caculation_Parameters['_PMOS_NumberofGate']    = _UnitBuf_PMOS_NumberofGate * _BufTree1_SizeofEachStage[i]
            _Caculation_Parameters['_PMOS_ChannelWidth']    = _UnitBuf_PMOS_ChannelWidth
            _Caculation_Parameters['_PMOS_ChannelLength']   = _UnitBuf_PMOS_ChannelLength

            _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']  = XvtTop2Pbody
            _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody'] = Xvtdown2Nbody

            ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
            self._DesignParameter['SRF_CLKBuf1Inv_Stage{}'.format(i + 1)] = self._SrefElementDeclaration(_DesignObj=F00_00_Inverter_v2._Inverter(_DesignParameter=None,_Name='{}:SRF_CLKBuf1Inv_Stage{}'.format(_Name, i + 1)))[0]

            ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
            self._DesignParameter['SRF_CLKBuf1Inv_Stage{}'.format(i + 1)]['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CLKBuf1Inv_Stage{}'.format(i + 1)]['_Angle'] = 0

            ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CLKBuf1Inv_Stage{}'.format(i + 1)]['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CLKBuf1Inv_Stage{}'.format(i + 1)]['_XYCoordinates'] = [[0, 0]]

            ## Check outter coord
            tmp = self.get_outter_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(i + 1))

            output_element = tmp['_Mostright']['index']
            output_elementname = tmp['_Layercoord'][output_element[0]][1]
            Tree1_rightmost.append(output_elementname)

            output_element = tmp['_Mostleft']['index']
            output_elementname = tmp['_Layercoord'][output_element[0]][1]
            Tree1_leftmost.append(output_elementname)

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## Buf Tree1 ReGen Applying XVTtoBody
        Tree2_rightmost = []
        Tree2_leftmost = []
        for i in range(_BufTree1and2_NumOfStage):
            _Caculation_Parameters = copy.deepcopy(F00_00_Inverter_v2._Inverter._ParametersForDesignCalculation)
            ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
            _Caculation_Parameters['_XVT']                  = _UnitBuf_XVT
            _Caculation_Parameters['_PMOSXvt2NMOSXvt']      = _UnitBuf_PMOSXvt2NMOSXvt

            _Caculation_Parameters['_NMOS_NumberofGate']    = _UnitBuf_NMOS_NumberofGate * _BufTree2_SizeofEachStage[i]
            _Caculation_Parameters['_NMOS_ChannelWidth']    = _UnitBuf_NMOS_ChannelWidth
            _Caculation_Parameters['_NMOS_ChannelLength']   = _UnitBuf_NMOS_ChannelLength

            _Caculation_Parameters['_PMOS_NumberofGate']    = _UnitBuf_PMOS_NumberofGate * _BufTree2_SizeofEachStage[i]
            _Caculation_Parameters['_PMOS_ChannelWidth']    = _UnitBuf_PMOS_ChannelWidth
            _Caculation_Parameters['_PMOS_ChannelLength']   = _UnitBuf_PMOS_ChannelLength

            _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody']  = XvtTop2Pbody
            _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody'] = Xvtdown2Nbody

            ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
            self._DesignParameter['SRF_CLKBuf2Inv_Stage{}'.format(i + 1)] = self._SrefElementDeclaration(_DesignObj=F00_00_Inverter_v2._Inverter(_DesignParameter=None,_Name='{}:SRF_CLKBuf2Inv_Stage{}'.format(_Name, i + 1)))[0]

            ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
            self._DesignParameter['SRF_CLKBuf2Inv_Stage{}'.format(i + 1)]['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CLKBuf2Inv_Stage{}'.format(i + 1)]['_Angle'] = 0

            ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CLKBuf2Inv_Stage{}'.format(i + 1)]['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CLKBuf2Inv_Stage{}'.format(i + 1)]['_XYCoordinates'] = [[0, 0]]

            ## Check outter coord
            tmp = self.get_outter_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(i + 1))

            output_element = tmp['_Mostright']['index']
            output_elementname = tmp['_Layercoord'][output_element[0]][1]
            Tree2_rightmost.append(output_elementname)

            output_element = tmp['_Mostleft']['index']
            output_elementname = tmp['_Layercoord'][output_element[0]][1]
            Tree2_leftmost.append(output_elementname)

            # wow1 = tuple(Tree2_rightmost[0])
            # test1 = self.get_param_KJH4(*wow1)

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## Cal Tree1 and Tree2 placement
            ## Cal coord
        for i in range(len(BufN_Sequence)):
            Tmp_XYTree1 = []
            Tmp_XYTree2 = []

            BufN    = BufN_Sequence[i]
            BufN_1  = BufN_Sequence[i-1]

            ##Tree1
            if i == 0:
                New_Scoord = [1000, 0]
                self._DesignParameter['SRF_CLKBuf1Inv_Stage{}'.format(BufN+1)]['_XYCoordinates'].append(New_Scoord)
            else:
                ## Target_coord: _XY_type1
                tmpx1_1 = tuple(Tree2_rightmost[BufN_1])
                tmpx1_2 = self.get_param_KJH4(*tmpx1_1)
                tmpx1_3 = self.get_last_chain(tmpx1_2, len(tmpx1_1) + 1)
                target_coordx = tmpx1_3['_XY_right'][0]
                tmpy1_1 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(BufN_1+1), 'SRF_NMOS', 'BND_{}Layer'.format(_UnitBuf_XVT))
                target_coordy = tmpy1_1[0][0][0][0]['_XY_up'][1]
                target_coord = [target_coordx, target_coordy]

                ## Approaching_coord: _XY_type2
                tmpx2_1 = tuple(Tree1_leftmost[BufN])
                tmpx2_2 = self.get_param_KJH4(*tmpx2_1)
                tmpx2_3 = self.get_first_chain(tmpx2_2[0], len(tmpx2_1))
                approaching_coordx = tmpx2_3['_XY_left'][0]
                tmpy2_1 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(BufN+1),'SRF_NMOS','BND_{}Layer'.format(_UnitBuf_XVT))
                approaching_coordy = tmpy2_1[0][0][0][0]['_XY_up'][1]
                approaching_coord = [approaching_coordx, approaching_coordy]

                ## Sref coord
                tmp3 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(BufN+1))
                Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                New_Scoord[0] = New_Scoord[0] + SpaceBtwBuffers
                Tmp_XYTree2.append(New_Scoord)
                ## Define Coordinates
                self._DesignParameter['SRF_CLKBuf1Inv_Stage{}'.format(BufN+1)]['_XYCoordinates'].append(New_Scoord)

            ##Tree2
            ## Calculate
            ## Target_coord: _XY_type1
            tmpx1_1 = tuple(Tree1_rightmost[BufN])
            tmpx1_2 = self.get_param_KJH4(*tmpx1_1)
            tmpx1_3 = self.get_last_chain(tmpx1_2, len(tmpx1_1)+1)
            target_coordx = tmpx1_3['_XY_right'][0]
            tmpy1_1 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(BufN+1),'SRF_NMOS','BND_{}Layer'.format(_UnitBuf_XVT))
            target_coordy = tmpy1_1[0][0][0][0]['_XY_up'][1]
            target_coord = [target_coordx, target_coordy]

            ## Approaching_coord: _XY_type2
            tmpx2_1 = tuple(Tree2_leftmost[BufN])
            tmpx2_2 = self.get_param_KJH4(*tmpx2_1)
            tmpx2_3 = self.get_first_chain(tmpx2_2[0], len(tmpx2_1))
            approaching_coordx = tmpx2_3['_XY_left'][0]
            tmpy2_1 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(BufN+1),'SRF_NMOS','BND_{}Layer'.format(_UnitBuf_XVT))
            approaching_coordy = tmpy2_1[0][0][0][0]['_XY_up'][1]
            approaching_coord = [approaching_coordx, approaching_coordy]

            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(BufN+1))
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[0] = New_Scoord[0] + SpaceBtwBuffers
            Tmp_XYTree2.append(New_Scoord)
            ## Define Coordinates
            self._DesignParameter['SRF_CLKBuf2Inv_Stage{}'.format(BufN+1)]['_XYCoordinates'].append(New_Scoord)

            ## Initialize coordinates
        for i in range(_BufTree1and2_NumOfStage):
            del self._DesignParameter['SRF_CLKBuf1Inv_Stage{}'.format(i + 1)]['_XYCoordinates'][0]
            del self._DesignParameter['SRF_CLKBuf2Inv_Stage{}'.format(i + 1)]['_XYCoordinates'][0]



        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## Routing



        #### Pre-calculated Routing Point (Y Coordination)
        InternalRoutingPath_Width = 50
        InternalRoutingPath_Space = 50
        tmp1 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(1),'BND_Out_Vtc_M2')
        CentY = tmp1[0][0][0]['_XY_cent'][1]
        Buf1Y = int(CentY + InternalRoutingPath_Width + InternalRoutingPath_Space/2)
        # Buf1Y = Buf1Y1 + InternalRoutingPath_Width + InternalRoutingPath_Space
        Buf2Y = int(CentY - InternalRoutingPath_Width - InternalRoutingPath_Space/2)
        # Buf2Y = Buf2Y1 - InternalRoutingPath_Width - InternalRoutingPath_Space
        UpperMetLayer = 5
        LowerMetLayer = 3

        for j in range(1,3):    # Buf Index (-> Buf1 or Buf2)
            for i in range(_BufTree1and2_NumOfStage,1,-1):    # Stage Index
                ### routing rules
                if i % 2 == 0:
                    Met = LowerMetLayer
                else:
                    Met = UpperMetLayer

                    ## Boundary_element Generation
                        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
                self._DesignParameter['BND_Buf{}Stg{}to{}_Hrz_M{}'.format(j, i, i-1, Met)] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL{}'.format(Met)][0],
                _Datatype=DesignParameters._LayerMapping['METAL{}'.format(Met)][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
                )
                        ## Define Boundary_element _YWidth
                self._DesignParameter['BND_Buf{}Stg{}to{}_Hrz_M{}'.format(j, i, i-1, Met)]['_YWidth'] = InternalRoutingPath_Width

                        ## Define Boundary_element _XWidth
                if j == 1:
                    tmp1 = self.get_param_KJH4('SRF_CLKBuf{}Inv_Stage{}'.format(j, i), 'BND_Input_Vtc_M2')
                    # tmp2 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(1), 'BND_Out_Vtc_M2')
                    self._DesignParameter['BND_Buf{}Stg{}to{}_Hrz_M{}'.format(j, i, i-1, Met)]['_XWidth'] = abs(tmp1[0][0][0]['_XY_left'][0] - tmp1[1][0][0]['_XY_right'][0])
                else:
                    tmp1 = self.get_param_KJH4('SRF_CLKBuf{}Inv_Stage{}'.format(j, i), 'BND_Input_Vtc_M2')
                    # tmp2 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(1), 'BND_Out_Vtc_M2')
                    self._DesignParameter['BND_Buf{}Stg{}to{}_Hrz_M{}'.format(j, i, i-1, Met)]['_XWidth'] = abs(
                        tmp1[0][0][0]['_XY_left'][0] - tmp1[1][0][0]['_XY_right'][0])
                        ## Define Boundary_element _XYCoordinates
                self._DesignParameter['BND_Buf{}Stg{}to{}_Hrz_M{}'.format(j, i, i-1, Met)]['_XYCoordinates'] = [[0, 0]]

                            ## Calculate Sref XYcoord
                tmpXY = []
                                ## Calculate
                                    ## Target_coord: _XY_type1
                for k in range(2 ** (i-2)):
                    MetalLineYOffset = int((_BufTree1and2_NumOfStage-i) / 2) * (InternalRoutingPath_Width + InternalRoutingPath_Space) + 400
                    if j == 1:
                        target_coord = [tmp1[2*k][0][0]['_XY_left'][0], Buf1Y - MetalLineYOffset]
                    else:
                        target_coord = [tmp1[2*k][0][0]['_XY_left'][0], Buf2Y + MetalLineYOffset]
                                        ## Approaching_coord: _XY_type2
                    tmp2 = self.get_param_KJH4('BND_Buf{}Stg{}to{}_Hrz_M{}'.format(j, i, i-1, Met))
                    approaching_coord = tmp2[0][0]['_XY_left']
                                        ## Sref coord
                    tmp3 = self.get_param_KJH4('BND_Buf{}Stg{}to{}_Hrz_M{}'.format(j, i, i-1, Met))
                    Scoord = tmp3[0][0]['_XY_origin']
                                        ## Cal
                    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                    tmpXY.append(New_Scoord)
                                        ## Define coordinates
                self._DesignParameter['BND_Buf{}Stg{}to{}_Hrz_M{}'.format(j, i, i-1, Met)]['_XYCoordinates'] = tmpXY


                #### 각 스테이지의 버퍼 Input 생성
                    ## Boundary_element Generation
                        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
                self._DesignParameter['BND_Buf{}Stg{}In_Vtc_M{}'.format(j, i, Met)] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL{}'.format(Met)][0],
                _Datatype=DesignParameters._LayerMapping['METAL{}'.format(Met)][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
                )
                        ## Define Boundary_element _XWidth
                self._DesignParameter['BND_Buf{}Stg{}In_Vtc_M{}'.format(j, i, Met)]['_XWidth'] = InternalRoutingPath_Width

                ## Define Boundary_element _YWidth
                tmp1 = self.get_param_KJH4('BND_Buf{}Stg{}to{}_Hrz_M{}'.format(j, i, i-1, Met))
                tmp2 = self.get_param_KJH4('SRF_CLKBuf{}Inv_Stage{}'.format(j, i), 'BND_Input_Vtc_M2')
                if j == 1:
                    self._DesignParameter['BND_Buf{}Stg{}In_Vtc_M{}'.format(j, i, Met)]['_YWidth'] = abs(tmp1[0][0]['_XY_down'][1] - tmp2[0][0][0]['_XY_up'][1])
                else:
                    self._DesignParameter['BND_Buf{}Stg{}In_Vtc_M{}'.format(j, i, Met)]['_YWidth'] = abs(
                        tmp1[0][0]['_XY_up'][1] - tmp2[0][0][0]['_XY_down'][1])
                ## Define Boundary_element _XYCoordinates
                self._DesignParameter['BND_Buf{}Stg{}In_Vtc_M{}'.format(j, i, Met)]['_XYCoordinates'] = [[0, 0]]

                            ## Calculate Sref XYcoord
                tmpXY = []
                                ## Calculate
                for k in range(2 ** (i - 1)):
                    if j == 1:
                        target_coord = tmp2[k][0][0]['_XY_up_left']
                        ## Approaching_coord: _XY_type2
                        tmp3 = self.get_param_KJH4('BND_Buf{}Stg{}In_Vtc_M{}'.format(j, i, Met))
                        approaching_coord = tmp3[0][0]['_XY_up_left']
                        ## Sref coord
                        tmp4 = self.get_param_KJH4('BND_Buf{}Stg{}In_Vtc_M{}'.format(j, i, Met))
                        Scoord = tmp4[0][0]['_XY_origin']
                        ## Cal
                        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                        tmpXY.append(New_Scoord)
                    else:
                        target_coord = tmp2[k][0][0]['_XY_down_left']
                        ## Approaching_coord: _XY_type2
                        tmp3 = self.get_param_KJH4('BND_Buf{}Stg{}In_Vtc_M{}'.format(j, i, Met))
                        approaching_coord = tmp3[0][0]['_XY_down_left']
                        ## Sref coord
                        tmp4 = self.get_param_KJH4('BND_Buf{}Stg{}In_Vtc_M{}'.format(j, i, Met))
                        Scoord = tmp4[0][0]['_XY_origin']
                        ## Cal
                        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                        tmpXY.append(New_Scoord)
                ## Define coordinates
                self._DesignParameter['BND_Buf{}Stg{}In_Vtc_M{}'.format(j, i, Met)]['_XYCoordinates'] = tmpXY


                #### 각 스테이지의 버퍼의 Input via 생성
                ## Sref generation: ViaX
                ## Define ViaX Parameter
                _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
                _Caculation_Parameters['_Layer1'] = 2
                _Caculation_Parameters['_Layer2'] = Met
                _Caculation_Parameters['_COX'] = 1
                _Caculation_Parameters['_COY'] = 2

                ## Sref ViaX declaration
                self._DesignParameter['SRF_Buf{}Stg{}In_ViaM2M{}'.format(j, i, Met)] = \
                self._SrefElementDeclaration(
                    _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                           _Name='{}:SRF_Buf{}Stg{}In_ViaM2M{}'.format(_Name, j, i,
                                                                                                        Met)))[0]

                ## Define Sref Relection
                self._DesignParameter['SRF_Buf{}Stg{}In_ViaM2M{}'.format(j, i, Met)]['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle
                self._DesignParameter['SRF_Buf{}Stg{}In_ViaM2M{}'.format(j, i, Met)]['_Angle'] = 0

                ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
                self._DesignParameter['SRF_Buf{}Stg{}In_ViaM2M{}'.format(j, i, Met)]['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

                ## Calculate Sref XYcoord
                tmpXY = []
                ## initialized Sref coordinate
                self._DesignParameter['SRF_Buf{}Stg{}In_ViaM2M{}'.format(j, i, Met)]['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                for k in range(2 ** (i - 1)):
                    ## Target_coord
                    tmp2 = self.get_param_KJH4('SRF_CLKBuf{}Inv_Stage{}'.format(j, i), 'BND_Input_Vtc_M2')
                    target_coord = tmp2[k][0][0]['_XY_cent']
                    ## Approaching_coord
                    tmp2 = self.get_param_KJH4('SRF_Buf{}Stg{}In_ViaM2M{}'.format(j, i, Met), 'SRF_ViaM2M3',
                                               'BND_Met2Layer')
                    approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                    ## Sref coord
                    tmp3 = self.get_param_KJH4('SRF_Buf{}Stg{}In_ViaM2M{}'.format(j, i, Met))
                    Scoord = tmp3[0][0]['_XY_origin']
                    Scoord[1] = Scoord[1] + 32
                    ## Calculate
                    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                    tmpXY.append(New_Scoord)
                ## Define
                self._DesignParameter['SRF_Buf{}Stg{}In_ViaM2M{}'.format(j, i, Met)]['_XYCoordinates'] = tmpXY



                #### 각 스테이지의 버퍼 Output 생성
                    ## Boundary_element Generation
                        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
                self._DesignParameter['BND_Buf{}Stg{}Out_Vtc_M{}'.format(j, i-1, Met)] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL{}'.format(Met)][0],
                _Datatype=DesignParameters._LayerMapping['METAL{}'.format(Met)][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
                )
                        ## Define Boundary_element _XWidth
                self._DesignParameter['BND_Buf{}Stg{}Out_Vtc_M{}'.format(j, i-1, Met)]['_XWidth'] = InternalRoutingPath_Width

                ## Define Boundary_element _YWidth
                tmp1 = self.get_param_KJH4('BND_Buf{}Stg{}to{}_Hrz_M{}'.format(j, i, i-1, Met))
                tmp2 = self.get_param_KJH4('SRF_CLKBuf{}Inv_Stage{}'.format(j, i-1), 'BND_Out_Vtc_M2')
                if j == 1:
                    self._DesignParameter['BND_Buf{}Stg{}Out_Vtc_M{}'.format(j, i-1, Met)]['_YWidth'] = abs(tmp1[0][0]['_XY_down'][1] - tmp2[0][0][0]['_XY_cent'][1])
                else:
                    self._DesignParameter['BND_Buf{}Stg{}Out_Vtc_M{}'.format(j, i-1, Met)]['_YWidth'] = abs(tmp1[0][0]['_XY_up'][1] - tmp2[0][0][0]['_XY_cent'][1])

                ## Define Boundary_element _XYCoordinates
                self._DesignParameter['BND_Buf{}Stg{}Out_Vtc_M{}'.format(j, i-1, Met)]['_XYCoordinates'] = [[0, 0]]

                            ## Calculate Sref XYcoord
                tmpXY = []
                                ## Calculate
                for k in range(2 ** (i - 2)):
                    if j == 1:
                        target_coord = tmp2[k][0][0]['_XY_left']
                        ## Approaching_coord: _XY_type2
                        tmp3 = self.get_param_KJH4('BND_Buf{}Stg{}Out_Vtc_M{}'.format(j, i-1, Met))
                        approaching_coord = tmp3[0][0]['_XY_up_left']
                        ## Sref coord
                        tmp4 = self.get_param_KJH4('BND_Buf{}Stg{}Out_Vtc_M{}'.format(j, i-1, Met))
                        Scoord = tmp4[0][0]['_XY_origin']
                        ## Cal
                        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                        tmpXY.append(New_Scoord)
                    else:
                        target_coord = tmp2[k][0][0]['_XY_left']
                        ## Approaching_coord: _XY_type2
                        tmp3 = self.get_param_KJH4('BND_Buf{}Stg{}Out_Vtc_M{}'.format(j, i-1, Met))
                        approaching_coord = tmp3[0][0]['_XY_down_left']
                        ## Sref coord
                        tmp4 = self.get_param_KJH4('BND_Buf{}Stg{}Out_Vtc_M{}'.format(j, i-1, Met))
                        Scoord = tmp4[0][0]['_XY_origin']
                        ## Cal
                        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                        tmpXY.append(New_Scoord)
                ## Define coordinates
                self._DesignParameter['BND_Buf{}Stg{}Out_Vtc_M{}'.format(j, i-1, Met)]['_XYCoordinates'] = tmpXY




                #### 각 스테이지의 버퍼의 Output via 생성
                ## Sref generation: ViaX
                ## Define ViaX Parameter
                _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
                _Caculation_Parameters['_Layer1'] = 2
                _Caculation_Parameters['_Layer2'] = Met
                _Caculation_Parameters['_COX'] = 1
                _Caculation_Parameters['_COY'] = 2

                ## Sref ViaX declaration
                self._DesignParameter['SRF_Buf{}Stg{}Out_ViaM2M{}'.format(j, i-1, Met)] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,_Name='{}:SRF_Buf{}Stg{}Out_ViaM2M{}'.format(_Name, j, i-1, Met)))[0]

                ## Define Sref Relection
                self._DesignParameter['SRF_Buf{}Stg{}Out_ViaM2M{}'.format(j, i-1, Met)]['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle
                self._DesignParameter['SRF_Buf{}Stg{}Out_ViaM2M{}'.format(j, i-1, Met)]['_Angle'] = 0

                ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
                self._DesignParameter['SRF_Buf{}Stg{}Out_ViaM2M{}'.format(j, i-1, Met)]['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

                ## Calculate Sref XYcoord
                tmpXY = []
                ## initialized Sref coordinate
                self._DesignParameter['SRF_Buf{}Stg{}Out_ViaM2M{}'.format(j, i-1, Met)]['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                for k in range(2 ** (i - 2)):
                    ## Target_coord
                    tmp2 = self.get_param_KJH4('SRF_CLKBuf{}Inv_Stage{}'.format(j, i-1), 'BND_Out_Vtc_M2')
                    target_coord = tmp2[k][0][0]['_XY_cent']
                    ## Approaching_coord
                    tmp2 = self.get_param_KJH4('SRF_Buf{}Stg{}Out_ViaM2M{}'.format(j, i-1, Met), 'SRF_ViaM2M3','BND_Met2Layer')
                    approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                    ## Sref coord
                    tmp3 = self.get_param_KJH4('SRF_Buf{}Stg{}Out_ViaM2M{}'.format(j, i-1, Met))
                    Scoord = tmp3[0][0]['_XY_origin']
                    Scoord[1] = Scoord[1] - 32  # 지그재그 비아 배치
                    ## Calculate
                    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                    tmpXY.append(New_Scoord)
                ## Define
                self._DesignParameter['SRF_Buf{}Stg{}Out_ViaM2M{}'.format(j, i-1, Met)]['_XYCoordinates'] = tmpXY





                ## Output 'Pin' for referencing
                    ## Boundary_element Generation
                    ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
                self._DesignParameter['BND_Buf{}_Output_M2'.format(j)] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['METAL2'][0],
                    _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                    _XWidth=None,
                    _YWidth=None,
                    _XYCoordinates=[],
                )

                ## Define Boundary_element _YWidth
                if _BufTree_OutputPlacement == 'Up':
                    tmp1 = self.get_param_KJH4('SRF_CLKBuf{}Inv_Stage{}'.format(j, _BufTree1and2_NumOfStage),'SRF_PMOS', 'BND_Drain_M1')
                elif _BufTree_OutputPlacement == 'Dn':
                    tmp1 = self.get_param_KJH4('SRF_CLKBuf{}Inv_Stage{}'.format(j, _BufTree1and2_NumOfStage),'SRF_NMOS', 'BND_Drain_M1')
                self._DesignParameter['BND_Buf{}_Output_M2'.format(j)]['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
                self._DesignParameter['BND_Buf{}_Output_M2'.format(j)]['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
                self._DesignParameter['BND_Buf{}_Output_M2'.format(j)]['_XYCoordinates'] = [[0, 0]]

                ## Calculate Sref XYcoord
                tmpXY = []
                ## Calculate
                for k in range(2 ** (_BufTree1and2_NumOfStage - 1)):
                    if _BufTree_OutputPlacement == 'Up':
                        ## Target_coord: _XY_type1
                        tmp1 = self.get_param_KJH4('SRF_CLKBuf{}Inv_Stage{}'.format(j, _BufTree1and2_NumOfStage),'SRF_PMOS', 'BND_Drain_M1')
                        target_coord = tmp1[k][0][-1][0]['_XY_up']
                        ## Approaching_coord: _XY_type2
                        tmp2 = self.get_param_KJH4('BND_Buf{}_Output_M2'.format(j))
                        approaching_coord = tmp2[0][0]['_XY_up']

                    elif _BufTree_OutputPlacement == 'Dn':
                        ## Target_coord: _XY_type1
                        tmp1 = self.get_param_KJH4('SRF_CLKBuf{}Inv_Stage{}'.format(j, _BufTree1and2_NumOfStage),'SRF_NMOS', 'BND_Drain_M1')
                        target_coord = tmp1[k][0][-1][0]['_XY_down']
                        ## Approaching_coord: _XY_type2
                        tmp2 = self.get_param_KJH4('BND_Buf{}_Output_M2'.format(j))
                        approaching_coord = tmp2[0][0]['_XY_down']

                    ## Sref coord
                    tmp3 = self.get_param_KJH4('BND_Buf{}_Output_M2'.format(j))
                    Scoord = tmp3[0][0]['_XY_origin']
                    ## Cal
                    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                    tmpXY.append(New_Scoord)
                ## Define coordinates
                self._DesignParameter['BND_Buf{}_Output_M2'.format(j)]['_XYCoordinates'] = tmpXY


            ### ClkTree Output Via Generation
            ## Sref generation: ViaX
            ## Define ViaX Parameter
            if _BufTree_OutputVia != None and _BufTree_OutputVia > 2:
                _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
                _Caculation_Parameters['_Layer1'] = 2
                _Caculation_Parameters['_Layer2'] = _BufTree_OutputVia
                _Caculation_Parameters['_COX'] = 1
                _Caculation_Parameters['_COY'] = 2

                ## Sref ViaX declaration
                self._DesignParameter['SRF_Buf{}Output_ViaM2M{}'.format(j,_BufTree_OutputVia)] = \
                self._SrefElementDeclaration(
                    _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                           _Name='{}:SRF_Buf{}Output_ViaM2M{}'.format(_Name,
                                                                                                 j,_BufTree_OutputVia)))[0]

                ## Define Sref Relection
                self._DesignParameter['SRF_Buf{}Output_ViaM2M{}'.format(j,_BufTree_OutputVia)]['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle
                self._DesignParameter['SRF_Buf{}Output_ViaM2M{}'.format(j,_BufTree_OutputVia)]['_Angle'] = 0

                ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
                self._DesignParameter['SRF_Buf{}Output_ViaM2M{}'.format(j,_BufTree_OutputVia)]['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

                ## Calculate Sref XYcoord
                tmpXY = []
                ## initialized Sref coordinate
                self._DesignParameter['SRF_Buf{}Output_ViaM2M{}'.format(j,_BufTree_OutputVia)]['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                ## Target_coord
                for k in range(2 ** (_BufTree1and2_NumOfStage - 1)):
                    if _BufTree_OutputPlacement == 'Up':
                        tmp1 = self.get_param_KJH4('BND_Buf{}_Output_M2'.format(j))
                        target_coord = tmp1[k][0]['_XY_up']
                        tmp2 = self.get_param_KJH4('SRF_Buf{}Output_ViaM2M{}'.format(j, _BufTree_OutputVia),'SRF_ViaM2M3', 'BND_Met2Layer')
                        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    elif _BufTree_OutputPlacement == 'Dn':
                        tmp1 = self.get_param_KJH4('BND_Buf{}_Output_M2'.format(j))
                        target_coord = tmp1[k][0]['_XY_down']
                        tmp2 = self.get_param_KJH4('SRF_Buf{}Output_ViaM2M{}'.format(j, _BufTree_OutputVia),'SRF_ViaM2M3', 'BND_Met2Layer')
                        approaching_coord = tmp2[0][0][0][0]['_XY_down']

                    ## Sref coord
                    tmp3 = self.get_param_KJH4('SRF_Buf{}Output_ViaM2M{}'.format(j,_BufTree_OutputVia))
                    Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
                    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                    tmpXY.append(New_Scoord)

                self._DesignParameter['SRF_Buf{}Output_ViaM2M{}'.format(j,_BufTree_OutputVia)]['_XYCoordinates'] = tmpXY





        ############### BND Nbody Layer Extension
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Nbody_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(_BufTree1and2_NumOfStage), 'SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(_BufTree1and2_NumOfStage), 'SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_Nbody_M1']['_YWidth'] = tmp2[0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Nbody_M1']['_XWidth'] = abs(tmp1[0][0][0][0][0]['_XY_left'][0] - tmp2[-1][0][0][0][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Nbody_M1']['_XYCoordinates'] = [[0, 0]]

        tmpXY=[]
        target_coord = tmp1[0][0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Nbody_M1')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Nbody_M1')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

                            ## Define coordinates
        self._DesignParameter['BND_Nbody_M1']['_XYCoordinates'] = tmpXY


        ############### BND Nbody Layer Extension
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Nbody_RX'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0],
            _Datatype=DesignParameters._LayerMapping['DIFF'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(_BufTree1and2_NumOfStage), 'SRF_Nbody','SRF_NbodyContactPhyLen','BND_ODLayer')
        tmp2 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(_BufTree1and2_NumOfStage), 'SRF_Nbody','SRF_NbodyContactPhyLen','BND_ODLayer')
        self._DesignParameter['BND_Nbody_RX']['_YWidth'] = tmp2[0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Nbody_RX']['_XWidth'] = abs(tmp1[0][0][0][0][0]['_XY_left'][0] - tmp2[-1][0][0][0][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Nbody_RX']['_XYCoordinates'] = [[0, 0]]

        tmpXY=[]
        target_coord = tmp1[0][0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Nbody_RX')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Nbody_RX')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

                            ## Define coordinates
        self._DesignParameter['BND_Nbody_RX']['_XYCoordinates'] = tmpXY


        ############### BND Pbody M1 Layer Extension
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Pbody_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(_BufTree1and2_NumOfStage), 'SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(_BufTree1and2_NumOfStage), 'SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_Pbody_M1']['_YWidth'] = tmp2[0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Pbody_M1']['_XWidth'] = abs(tmp1[0][0][0][0][0]['_XY_left'][0] - tmp2[-1][0][0][0][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Pbody_M1']['_XYCoordinates'] = [[0, 0]]

        tmpXY=[]
        target_coord = tmp1[0][0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Pbody_M1')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Pbody_M1')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Define coordinates
        self._DesignParameter['BND_Pbody_M1']['_XYCoordinates'] = tmpXY


        ############### BND Pbody PP Layer Extension
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Pbody_PP'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(_BufTree1and2_NumOfStage), 'SRF_Pbody','SRF_PbodyContactPhyLen','BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(_BufTree1and2_NumOfStage), 'SRF_Pbody','SRF_PbodyContactPhyLen','BND_PPLayer')
        self._DesignParameter['BND_Pbody_PP']['_YWidth'] = tmp2[0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Pbody_PP']['_XWidth'] = abs(tmp1[0][0][0][0][0]['_XY_left'][0] - tmp2[-1][0][0][0][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Pbody_PP']['_XYCoordinates'] = [[0, 0]]

        tmpXY=[]
        target_coord = tmp1[0][0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Pbody_PP')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Pbody_PP')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

                            ## Define coordinates
        self._DesignParameter['BND_Pbody_PP']['_XYCoordinates'] = tmpXY


        ############### BND Pbody RX Layer Extension
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Pbody_RX'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0],
            _Datatype=DesignParameters._LayerMapping['DIFF'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(_BufTree1and2_NumOfStage), 'SRF_Pbody','SRF_PbodyContactPhyLen','BND_ODLayer')
        tmp2 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(_BufTree1and2_NumOfStage), 'SRF_Pbody','SRF_PbodyContactPhyLen','BND_ODLayer')
        self._DesignParameter['BND_Pbody_RX']['_YWidth'] = tmp2[0][0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Pbody_RX']['_XWidth'] = abs(tmp1[0][0][0][0][0]['_XY_left'][0] - tmp2[-1][0][0][0][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Pbody_RX']['_XYCoordinates'] = [[0, 0]]

        tmpXY=[]
        target_coord = tmp1[0][0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Pbody_RX')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Pbody_RX')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

                            ## Define coordinates
        self._DesignParameter['BND_Pbody_RX']['_XYCoordinates'] = tmpXY


        ############### BND NWELL Layer Extension
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NWell'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(_BufTree1and2_NumOfStage), 'BND_PMOS_NellExten')
        tmp2 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(_BufTree1and2_NumOfStage), 'BND_PMOS_NellExten')
        self._DesignParameter['BND_NWell']['_YWidth'] = tmp2[0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_NWell']['_XWidth'] = abs(tmp1[0][0][0]['_XY_left'][0] - tmp2[-1][0][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NWell']['_XYCoordinates'] = [[0, 0]]

        tmpXY=[]
        target_coord = tmp1[0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NWell')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NWell')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

                            ## Define coordinates
        self._DesignParameter['BND_NWell']['_XYCoordinates'] = tmpXY


        ############### BND Nbody Layer Extension
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PPExten'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(_BufTree1and2_NumOfStage), 'SRF_PMOS','BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(_BufTree1and2_NumOfStage), 'SRF_PMOS','BND_PPLayer')
        self._DesignParameter['BND_PPExten']['_YWidth'] = tmp2[0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_PPExten']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_left'][0] - tmp2[-1][0][0][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PPExten']['_XYCoordinates'] = [[0, 0]]

        tmpXY=[]
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PPExten')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PPExten')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

                            ## Define coordinates
        self._DesignParameter['BND_PPExten']['_XYCoordinates'] = tmpXY




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
    libname = 'Proj_ZZ01_F00_02_CLKBufferTree_Fixed'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'F00_02_CLKBufferTree_v3_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
## Unit Buffer Size
        #Common
    _UnitBuf_XVT                        = 'SLVT',
        #Nmos
    _UnitBuf_NMOS_NumberofGate          = 1,        # Number
    _UnitBuf_NMOS_ChannelWidth          = 400,      # Number
    _UnitBuf_NMOS_ChannelLength         = 30,       # Number
        #Pmos
    _UnitBuf_PMOS_NumberofGate          = 1,        # Number
    _UnitBuf_PMOS_ChannelWidth          = 800,      # Number
    _UnitBuf_PMOS_ChannelLength         = 30,       # Number
        #Height
    _UnitBuf_PMOSXvt2NMOSXvt            = 446,     # number

## Buffer Tree structure
    _BufTree_TotalLength        = 50000,   # None(minimum)/Number
    _BufTree1and2_NumOfStage    = 4,        # len[Buf0, Buf1, ... ] 스테이지 수 (아래 버퍼 사이즈 리스트의 길이와 같아야 함.)
    _BufTree1_SizeofEachStage   = [1, 2, 4, 8],     # [Buf0, Buf1, Buf2 ...]
    _BufTree2_SizeofEachStage   = [1, 2, 4, 8],  # [Buf0, Buf1, Buf2 ...]
    _BufTree_OutputPlacement    = 'Dn',     #Up/Dn
    _BufTree_OutputVia          = 4,        #None(no via, Just m2 metal)/number(mx via)
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
    LayoutObj = _CLKBufferTree(_DesignParameter=None, _Name=cellname)
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
