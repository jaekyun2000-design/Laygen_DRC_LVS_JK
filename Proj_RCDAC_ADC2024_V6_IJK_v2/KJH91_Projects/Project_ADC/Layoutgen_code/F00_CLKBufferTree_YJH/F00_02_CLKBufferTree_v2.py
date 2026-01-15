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
from KJH91_Projects.Project_ADC.Layoutgen_code.F00_CLKBufferTree_YJH import F00_00_Inverter_v2
from KJH91_Projects.Project_ADC.Layoutgen_code.J00_CDACPreDriver_InvBuffer_KJH0 import J00_02_CDAC_PreDriver_KJH



## Define Class
class _CLKBufferTree(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
        # TreeSize
        _CLKBufTree_TotalLength=None,  # 양 끝 Poly gate dummy의 Physical한 크기
        _CLKBufTree_NumOfStage=None,  # 스테이지 수 (아래 버퍼 사이즈 리스트의 길이와 같아야 함.)
        _CLKBufTree_Buf1_SizeByStage=None,
        _CLKBufTree_Buf2_SizeByStage=None,  # 스테이지에 따른 버퍼 사이즈(UnitBuffer의 배수로 각 스테이지의 크기가 결정 됨.)
        _CLKBufTree_OutputVia=4, # None이면 비아 생성 안함.(-> default: M2)

        ## CLK Buffer Unit
        # Inverter Sizing
        _CLKBufTree_Inv_NMOS_ChannelWidth=None,  # Number
        _CLKBufTree_Inv_NMOS_ChannelLength=None,  # Number
        _CLKBufTree_Inv_NMOS_NumberofGate=None,  # Number
        _CLKBufTree_Inv_NMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _CLKBufTree_Inv_NMOS_POGate_Comb_length=None,  # None/Number

        _CLKBufTree_Inv_PMOS_ChannelWidth=None,  # Number
        _CLKBufTree_Inv_PMOS_ChannelLength=None,  # Number
        _CLKBufTree_Inv_PMOS_NumberofGate=None,  # Number
        _CLKBufTree_Inv_PMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _CLKBufTree_Inv_PMOS_POGate_Comb_length=None,  # None/Number

        # PowerRail Size
        _CLKBufTree_NMOS_Pbody_NumCont=None,
        _CLKBufTree_NMOS_Pbody_XvtTop2Pbody=None,
        _CLKBufTree_PMOS_Nbody_NumCont=None,
        _CLKBufTree_PMOS_Nbody_Xvtdown2Nbody=None,
        _CLKBufTree_PMOSXvt2NMOSXvt=None,
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
                                  # TreeSize
                                  _CLKBufTree_TotalLength=None,  # 양 끝 Poly gate dummy의 Physical한 크기
                                  _CLKBufTree_NumOfStage=None,  # 스테이지 수 (아래 버퍼 사이즈 리스트의 길이와 같아야 함.)
                                  _CLKBufTree_Buf1_SizeByStage=None,
                                  _CLKBufTree_Buf2_SizeByStage=None,
                                  # 스테이지에 따른 버퍼 사이즈(UnitBuffer의 배수로 각 스테이지의 크기가 결정 됨.)
                                  _CLKBufTree_OutputPlacement=None,
                                  _CLKBufTree_OutputVia=None,  # None이면 비아 생성 안함.(-> default: M2)

                                  ## CLK Buffer Unit
                                  # Inverter
                                  _CLKBufTree_Inv_NMOS_ChannelWidth=None,  # Number
                                  _CLKBufTree_Inv_NMOS_ChannelLength=None,  # Number
                                  _CLKBufTree_Inv_NMOS_NumberofGate=None,  # Number
                                  _CLKBufTree_Inv_NMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _CLKBufTree_Inv_NMOS_POGate_Comb_length=None,  # None/Number

                                  _CLKBufTree_Inv_PMOS_ChannelWidth=None,  # Number
                                  _CLKBufTree_Inv_PMOS_ChannelLength=None,  # Number
                                  _CLKBufTree_Inv_PMOS_NumberofGate=None,  # Number
                                  _CLKBufTree_Inv_PMOS_XVT=None,  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _CLKBufTree_Inv_PMOS_POGate_Comb_length=None,  # None/Number

                                  # PowerRail Size
                                  _CLKBufTree_NMOS_Pbody_NumCont=None,
                                  _CLKBufTree_NMOS_Pbody_XvtTop2Pbody=None,
                                  _CLKBufTree_PMOS_Nbody_NumCont=None,
                                  _CLKBufTree_PMOS_Nbody_Xvtdown2Nbody=None,
                                  _CLKBufTree_PMOSXvt2NMOSXvt=None,
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

        if (len(_CLKBufTree_Buf1_SizeByStage)) != (len(_CLKBufTree_Buf2_SizeByStage)):
            raise Exception("버퍼 스테이지의 수와 스테이지에 따른 사이즈 입력 수가 일치하지 않음.")

        if (len(_CLKBufTree_Buf2_SizeByStage)) != _CLKBufTree_NumOfStage:
            raise Exception("버퍼1의 스테이지 수와 2의 스테이지 수가 일치하지 않음.")

        Buf1MaxNMOSSpaceBtwXVT2Body = 0
        Buf1MaxPMOSSpaceBtwXVT2Body = 0
        Buf2MaxNMOSSpaceBtwXVT2Body = 0
        Buf2MaxPMOSSpaceBtwXVT2Body = 0
        Buf1InvByStgWidthList = [-1] # stage와 BufferWidthList의 인덱스를 맞추려고 -1를 임의로 그냥 넣어놓음.
        Buf2InvByStgWidthList = [-1] # stage와 BufferWidthList의 인덱스를 맞추려고 -1를 임의로 그냥 넣어놓음.

        for i in range(_CLKBufTree_NumOfStage):
            _Caculation_Parameters = copy.deepcopy(F00_00_Inverter_v2._Inverter._ParametersForDesignCalculation)
            ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
            _Caculation_Parameters['_NMOS_MosType'] = 'NMOS'
            _Caculation_Parameters['_NMOS_MosUpDn'] = 'Up'
            _Caculation_Parameters['_NMOS_NumberofGate'] = _CLKBufTree_Inv_NMOS_NumberofGate * _CLKBufTree_Buf1_SizeByStage[i]
            _Caculation_Parameters['_NMOS_ChannelWidth'] = _CLKBufTree_Inv_NMOS_ChannelWidth
            _Caculation_Parameters['_NMOS_ChannelLength'] = _CLKBufTree_Inv_NMOS_ChannelLength
            _Caculation_Parameters['_NMOS_GateSpacing'] = None
            _Caculation_Parameters['_NMOS_SDWidth'] = None
            _Caculation_Parameters['_NMOS_XVT'] = _CLKBufTree_Inv_NMOS_XVT
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
            _Caculation_Parameters['_NMOS_Xvt_MinExten_TF'] = True
            _Caculation_Parameters['_NMOS_Xvt_Placement'] = 'Up'
            _Caculation_Parameters['_NMOS_POGate_Comb_TF'] = True
            _Caculation_Parameters['_NMOS_POGate_Comb_length'] = _CLKBufTree_Inv_NMOS_POGate_Comb_length
            _Caculation_Parameters['_NMOS_POGate_Via_TF'] = True
            _Caculation_Parameters['_NMOS_POGate_ViaMxMx'] = [0, 1]

            _Caculation_Parameters['_PMOS_MosType'] = 'PMOS'
            _Caculation_Parameters['_PMOS_MosUpDn'] = 'Dn'
            _Caculation_Parameters['_PMOS_NumberofGate'] = _CLKBufTree_Inv_PMOS_NumberofGate * _CLKBufTree_Buf1_SizeByStage[i]
            _Caculation_Parameters['_PMOS_ChannelWidth'] = _CLKBufTree_Inv_PMOS_ChannelWidth
            _Caculation_Parameters['_PMOS_ChannelLength'] = _CLKBufTree_Inv_PMOS_ChannelLength
            _Caculation_Parameters['_PMOS_GateSpacing'] = None
            _Caculation_Parameters['_PMOS_SDWidth'] = None
            _Caculation_Parameters['_PMOS_XVT'] = _CLKBufTree_Inv_PMOS_XVT
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
            _Caculation_Parameters['_PMOS_Xvt_MinExten_TF'] = True
            _Caculation_Parameters['_PMOS_Xvt_Placement'] = None
            _Caculation_Parameters['_PMOS_POGate_Comb_TF'] = True
            _Caculation_Parameters['_PMOS_POGate_Comb_length'] = _CLKBufTree_Inv_PMOS_POGate_Comb_length
            _Caculation_Parameters['_PMOS_POGate_Via_TF'] = True
            _Caculation_Parameters['_PMOS_POGate_ViaMxMx'] = [0, 1]

            _Caculation_Parameters['_NMOS_Pbody_NumCont'] = _CLKBufTree_NMOS_Pbody_NumCont
            _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody'] = _CLKBufTree_NMOS_Pbody_XvtTop2Pbody
            _Caculation_Parameters['_PMOS_Nbody_NumCont'] = _CLKBufTree_PMOS_Nbody_NumCont
            _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody'] = _CLKBufTree_PMOS_Nbody_Xvtdown2Nbody
            _Caculation_Parameters['_PMOSXvt2NMOSXvt'] = _CLKBufTree_PMOSXvt2NMOSXvt

            ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
            self._DesignParameter['SRF_CLKBuf1Inv_Stage{}'.format(i+1)] = self._SrefElementDeclaration(
                _DesignObj=F00_00_Inverter_v2._Inverter(_DesignParameter=None,
                                                 _Name='{}:SRF_CLKInv_Stage{}'.format(_Name, i+1)))[0]

            ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
            self._DesignParameter['SRF_CLKBuf1Inv_Stage{}'.format(i+1)]['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CLKBuf1Inv_Stage{}'.format(i+1)]['_Angle'] = 0

            ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CLKBuf1Inv_Stage{}'.format(i+1)]['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CLKBuf1Inv_Stage{}'.format(i+1)]['_XYCoordinates'] = [[0,0]]

            tmp1 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(i+1),'SRF_NMOS', 'BND_PODummyLayer')
            tmp2 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(i+1),'SRF_NMOS', 'BND_PODummyLayer')
            NMOSWidth = abs(tmp1[0][0][0][0]['_XY_left'][0] - tmp2[0][0][-1][0]['_XY_right'][0])

            tmp1 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(i+1),'SRF_PMOS', 'BND_PODummyLayer')
            tmp2 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(i+1),'SRF_PMOS', 'BND_PODummyLayer')
            PMOSWidth = abs(tmp1[0][0][0][0]['_XY_left'][0] - tmp2[0][0][-1][0]['_XY_right'][0])

            Buf1InvWidthOfThisStage = max(NMOSWidth, PMOSWidth)
            Buf1InvByStgWidthList.append(Buf1InvWidthOfThisStage)

            tmp1 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(i+1),'SRF_NMOS', 'BND_{}Layer'.format(_CLKBufTree_Inv_NMOS_XVT))
            tmp2 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(i+1),'SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
            NMOSSpaceBtwXVT2Body = abs(tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0]['_XY_up'][1])
            if Buf1MaxNMOSSpaceBtwXVT2Body < NMOSSpaceBtwXVT2Body:
                Buf1MaxNMOSSpaceBtwXVT2Body = NMOSSpaceBtwXVT2Body

            tmp1 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(i+1),'SRF_PMOS', 'BND_{}Layer'.format(_CLKBufTree_Inv_PMOS_XVT))
            tmp2 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(i+1),'SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
            PMOSSpaceBtwXVT2Body = abs(tmp1[0][0][0][0]['_XY_down'][1] - tmp2[0][0][0][0][0]['_XY_down'][1])
            if Buf1MaxPMOSSpaceBtwXVT2Body < PMOSSpaceBtwXVT2Body:
                Buf1MaxPMOSSpaceBtwXVT2Body = PMOSSpaceBtwXVT2Body


 ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
        for i in range(_CLKBufTree_NumOfStage):
            _Caculation_Parameters = copy.deepcopy(F00_00_Inverter_v2._Inverter._ParametersForDesignCalculation)
            ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
            _Caculation_Parameters['_NMOS_MosType'] = 'NMOS'
            _Caculation_Parameters['_NMOS_MosUpDn'] = 'Up'
            _Caculation_Parameters['_NMOS_NumberofGate'] = _CLKBufTree_Inv_NMOS_NumberofGate * \
                                                           _CLKBufTree_Buf2_SizeByStage[i]
            _Caculation_Parameters['_NMOS_ChannelWidth'] = _CLKBufTree_Inv_NMOS_ChannelWidth
            _Caculation_Parameters['_NMOS_ChannelLength'] = _CLKBufTree_Inv_NMOS_ChannelLength
            _Caculation_Parameters['_NMOS_GateSpacing'] = None
            _Caculation_Parameters['_NMOS_SDWidth'] = None
            _Caculation_Parameters['_NMOS_XVT'] = _CLKBufTree_Inv_NMOS_XVT
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
            _Caculation_Parameters['_NMOS_Xvt_MinExten_TF'] = True
            _Caculation_Parameters['_NMOS_Xvt_Placement'] = 'Up'
            _Caculation_Parameters['_NMOS_POGate_Comb_TF'] = True
            _Caculation_Parameters['_NMOS_POGate_Comb_length'] = _CLKBufTree_Inv_NMOS_POGate_Comb_length
            _Caculation_Parameters['_NMOS_POGate_Via_TF'] = True
            _Caculation_Parameters['_NMOS_POGate_ViaMxMx'] = [0, 1]

            _Caculation_Parameters['_PMOS_MosType'] = 'PMOS'
            _Caculation_Parameters['_PMOS_MosUpDn'] = 'Dn'
            _Caculation_Parameters['_PMOS_NumberofGate'] = _CLKBufTree_Inv_PMOS_NumberofGate * \
                                                           _CLKBufTree_Buf2_SizeByStage[i]
            _Caculation_Parameters['_PMOS_ChannelWidth'] = _CLKBufTree_Inv_PMOS_ChannelWidth
            _Caculation_Parameters['_PMOS_ChannelLength'] = _CLKBufTree_Inv_PMOS_ChannelLength
            _Caculation_Parameters['_PMOS_GateSpacing'] = None
            _Caculation_Parameters['_PMOS_SDWidth'] = None
            _Caculation_Parameters['_PMOS_XVT'] = _CLKBufTree_Inv_PMOS_XVT
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
            _Caculation_Parameters['_PMOS_Xvt_MinExten_TF'] = True
            _Caculation_Parameters['_PMOS_Xvt_Placement'] = None
            _Caculation_Parameters['_PMOS_POGate_Comb_TF'] = True
            _Caculation_Parameters['_PMOS_POGate_Comb_length'] = _CLKBufTree_Inv_PMOS_POGate_Comb_length
            _Caculation_Parameters['_PMOS_POGate_Via_TF'] = True
            _Caculation_Parameters['_PMOS_POGate_ViaMxMx'] = [0, 1]

            _Caculation_Parameters['_NMOS_Pbody_NumCont'] = _CLKBufTree_NMOS_Pbody_NumCont
            _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody'] = _CLKBufTree_NMOS_Pbody_XvtTop2Pbody
            _Caculation_Parameters['_PMOS_Nbody_NumCont'] = _CLKBufTree_PMOS_Nbody_NumCont
            _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody'] = _CLKBufTree_PMOS_Nbody_Xvtdown2Nbody
            _Caculation_Parameters['_PMOSXvt2NMOSXvt'] = _CLKBufTree_PMOSXvt2NMOSXvt

            ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
            self._DesignParameter['SRF_CLKBuf2Inv_Stage{}'.format(i + 1)] = self._SrefElementDeclaration(
                _DesignObj=F00_00_Inverter_v2._Inverter(_DesignParameter=None,
                                                     _Name='{}:SRF_CLKBuf2Inv_Stage{}'.format(_Name, i + 1)))[0]

            ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
            self._DesignParameter['SRF_CLKBuf2Inv_Stage{}'.format(i + 1)]['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CLKBuf2Inv_Stage{}'.format(i + 1)]['_Angle'] = 0

            ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CLKBuf2Inv_Stage{}'.format(i + 1)]['_DesignObj']._CalculateDesignParameter(
                **_Caculation_Parameters)

            ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CLKBuf2Inv_Stage{}'.format(i + 1)]['_XYCoordinates'] = [[0, 0]]

            tmp1 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(i + 1), 'SRF_NMOS', 'BND_PODummyLayer')
            tmp2 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(i + 1), 'SRF_NMOS', 'BND_PODummyLayer')
            NMOSWidth = abs(tmp1[0][0][0][0]['_XY_left'][0] - tmp2[0][0][-1][0]['_XY_right'][0])

            tmp1 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(i + 1), 'SRF_PMOS', 'BND_PODummyLayer')
            tmp2 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(i + 1), 'SRF_PMOS', 'BND_PODummyLayer')
            PMOSWidth = abs(tmp1[0][0][0][0]['_XY_left'][0] - tmp2[0][0][-1][0]['_XY_right'][0])

            Buf2InvWidthOfThisStage = max(NMOSWidth, PMOSWidth)
            Buf2InvByStgWidthList.append(Buf2InvWidthOfThisStage)

            tmp1 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(i + 1), 'SRF_NMOS',
                                       'BND_{}Layer'.format(_CLKBufTree_Inv_NMOS_XVT))
            tmp2 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(i + 1), 'SRF_Pbody', 'SRF_PbodyContactPhyLen',
                                       'BND_Met1Layer')
            NMOSSpaceBtwXVT2Body = abs(tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0]['_XY_up'][1])
            if Buf2MaxNMOSSpaceBtwXVT2Body < NMOSSpaceBtwXVT2Body:
                Buf2MaxNMOSSpaceBtwXVT2Body = NMOSSpaceBtwXVT2Body

            tmp1 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(i + 1), 'SRF_PMOS',
                                       'BND_{}Layer'.format(_CLKBufTree_Inv_PMOS_XVT))
            tmp2 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(i + 1), 'SRF_Nbody', 'SRF_NbodyContactPhyLen',
                                       'BND_Met1Layer')
            PMOSSpaceBtwXVT2Body = abs(tmp1[0][0][0][0]['_XY_down'][1] - tmp2[0][0][0][0][0]['_XY_down'][1])
            if Buf2MaxPMOSSpaceBtwXVT2Body < PMOSSpaceBtwXVT2Body:
                Buf2MaxPMOSSpaceBtwXVT2Body = PMOSSpaceBtwXVT2Body

        MaxNMOSSpaceBtwXVT2Body = max(Buf1MaxNMOSSpaceBtwXVT2Body,Buf2MaxNMOSSpaceBtwXVT2Body)
        MaxPMOSSpaceBtwXVT2Body = max(Buf1MaxPMOSSpaceBtwXVT2Body,Buf2MaxPMOSSpaceBtwXVT2Body)


        ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
        ##################################################################################
        # CLK Buffer Tree가 생성 가능한지 검증하는 절차.
        MinGeneratedTreeLength = 0  # 초기화
        MinimumSpaceBtwPodummy = 96 # DRC
        NumOfTotalBufs = 2*( (2 ** _CLKBufTree_NumOfStage) - 1)
        for i in range(_CLKBufTree_NumOfStage, 0, -1):    # _CLKBufTree_NumOfStage==3 이면, i = 3, 2, 1이 되도록 설정.
            NumOfBufByStage = (2 ** (i - 1))
            MinGeneratedTreeLength = MinGeneratedTreeLength + NumOfBufByStage * (Buf1InvByStgWidthList[i] + Buf2InvByStgWidthList[i])

        MinGeneratedTreeLength = MinGeneratedTreeLength + (NumOfTotalBufs - 1) * MinimumSpaceBtwPodummy
        if _CLKBufTree_TotalLength != None:
            if _CLKBufTree_TotalLength < MinGeneratedTreeLength:
                raise Exception("생성될 트리의 길이가 입력받은 '_CLKBufTree_TotalLength'의 길이보다 길어, 레이아웃을 생성할 수 없습니다.")
            else:
                SpaceBtwBuffers = int((_CLKBufTree_TotalLength - MinGeneratedTreeLength) / (NumOfTotalBufs-1)) + MinimumSpaceBtwPodummy
        else:
            _CLKBufTree_TotalLength = MinGeneratedTreeLength
            SpaceBtwBuffers = MinimumSpaceBtwPodummy

        for i in range(1,_CLKBufTree_NumOfStage+1):
            del(self._DesignParameter['SRF_CLKBuf1Inv_Stage{}'.format(i)])
            del(self._DesignParameter['SRF_CLKBuf2Inv_Stage{}'.format(i)])

        ##################################################################################
        ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###


        #### SRF_CLKBuf1Inv_Stage, SRF_CLKBuf2Inv_Stage SRF 재 생성
        for i in range(_CLKBufTree_NumOfStage):
            _Caculation_Parameters['_NMOS_NumberofGate'] = _CLKBufTree_Inv_NMOS_NumberofGate * _CLKBufTree_Buf1_SizeByStage[i]
            _Caculation_Parameters['_PMOS_NumberofGate'] = _CLKBufTree_Inv_PMOS_NumberofGate * _CLKBufTree_Buf1_SizeByStage[i]
            _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody'] = MaxNMOSSpaceBtwXVT2Body
            _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody'] = MaxPMOSSpaceBtwXVT2Body
            _Caculation_Parameters['_PMOSXvt2NMOSXvt'] = _CLKBufTree_PMOSXvt2NMOSXvt
    
            ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
            self._DesignParameter['SRF_CLKBuf1Inv_Stage{}'.format(i + 1)] = self._SrefElementDeclaration(
                _DesignObj=F00_00_Inverter_v2._Inverter(_DesignParameter=None,
                                                     _Name='{}:SRF_CLKBuf1Inv_Stage{}'.format(_Name, i + 1)))[0]
    
            ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
            self._DesignParameter['SRF_CLKBuf1Inv_Stage{}'.format(i + 1)]['_Reflect'] = [0, 0, 0]
    
            ## Define Sref Angle: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CLKBuf1Inv_Stage{}'.format(i + 1)]['_Angle'] = 0
    
            ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CLKBuf1Inv_Stage{}'.format(i + 1)]['_DesignObj']._CalculateDesignParameter(
                **_Caculation_Parameters)

            self._DesignParameter['SRF_CLKBuf1Inv_Stage{}'.format(i + 1)]['_XYCoordinates'] = [[0, 0]]


            #### SRF_CLKBuf1Inv_Stage, SRF_CLKBuf2Inv_Stage SRF 재 생성
            ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
            _Caculation_Parameters['_NMOS_NumberofGate'] = _CLKBufTree_Inv_NMOS_NumberofGate * _CLKBufTree_Buf2_SizeByStage[i]
            _Caculation_Parameters['_PMOS_NumberofGate'] = _CLKBufTree_Inv_PMOS_NumberofGate * _CLKBufTree_Buf2_SizeByStage[i]

            ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
            self._DesignParameter['SRF_CLKBuf2Inv_Stage{}'.format(i + 1)] = self._SrefElementDeclaration(
                _DesignObj=F00_00_Inverter_v2._Inverter(_DesignParameter=None,
                                                     _Name='{}:SRF_CLKBuf2Inv_Stage{}'.format(_Name, i + 1)))[0]

            ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
            self._DesignParameter['SRF_CLKBuf2Inv_Stage{}'.format(i + 1)]['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CLKBuf2Inv_Stage{}'.format(i + 1)]['_Angle'] = 0

            ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CLKBuf2Inv_Stage{}'.format(i + 1)]['_DesignObj']._CalculateDesignParameter(
                **_Caculation_Parameters)

            ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
            self._DesignParameter['SRF_CLKBuf2Inv_Stage{}'.format(i + 1)]['_XYCoordinates'] = [[0, 0]]



        ### ### 좌표 계산 알고리즘 ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
        # Stage = 3 이면 InverterPlacementTmp = [3, 2 ,3, 1, 3, 2, 3, 1]이 되도록 하는 코드
        # InverterPlacementTmp = list(range(NumOfTotalBufs)) # 초기화
        InverterPlacementTmp = [0 for i in range(int(NumOfTotalBufs/2))] # 초기화
        k = 0
        for i in range(_CLKBufTree_NumOfStage, 0, -1):    # _CLKBufTree_NumOfStage==3 이면, for loop i = 3, 2, 1이 되도록 설정.
            for j in range(int(NumOfTotalBufs/2)):
                if j % (2 ** (k+1)) == (2 ** k) - 1:
                    InverterPlacementTmp[j] = i
            k = k+1

        InverterPlacement = [0 for i in range(NumOfTotalBufs)]
        for i in range(int(NumOfTotalBufs/2)):
            InverterPlacement[2*i] = InverterPlacementTmp[i]
            InverterPlacement[2*i+1] = InverterPlacementTmp[i]


        rows = NumOfTotalBufs
        cols = 2
        tmpXYs = [[0 for j in range(cols)] for i in range(rows)]
        for i in range(1,NumOfTotalBufs):
            if i % 2 == 1:
                tmpXYs[i][0] = tmpXYs[i-1][0] + Buf1InvByStgWidthList[InverterPlacement[i - 1]] + SpaceBtwBuffers
            else:
                tmpXYs[i][0] = tmpXYs[i-1][0] + Buf2InvByStgWidthList[InverterPlacement[i - 1]] + SpaceBtwBuffers

        for i in range(_CLKBufTree_NumOfStage):
            self._DesignParameter['SRF_CLKBuf1Inv_Stage{}'.format(i + 1)]['_XYCoordinates'] = []
            self._DesignParameter['SRF_CLKBuf2Inv_Stage{}'.format(i + 1)]['_XYCoordinates'] = []

        for i in range(NumOfTotalBufs):
            if i % 2 == 0:
                self._DesignParameter['SRF_CLKBuf1Inv_Stage{}'.format(InverterPlacement[i])]['_XYCoordinates'].append(tmpXYs[i])
            else:
                self._DesignParameter['SRF_CLKBuf2Inv_Stage{}'.format(InverterPlacement[i])]['_XYCoordinates'].append(tmpXYs[i])
        ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
        ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###



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
            for i in range(_CLKBufTree_NumOfStage,1,-1):    # Stage Index
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
                    MetalLineYOffset = int((_CLKBufTree_NumOfStage-i) / 2) * (InternalRoutingPath_Width + InternalRoutingPath_Space) + 400
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
                self._DesignParameter['SRF_Buf{}Stg{}In_ViaM2M{}'.format(j, i, Met)][
                    '_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

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
                self._DesignParameter['SRF_Buf{}Stg{}Out_ViaM2M{}'.format(j, i-1, Met)] = self._SrefElementDeclaration(
                    _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                           _Name='{}:SRF_Buf{}Stg{}Out_ViaM2M{}'.format(_Name, j, i-1, Met)))[0]

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
                if _CLKBufTree_OutputPlacement == 'Up':
                    tmp1 = self.get_param_KJH4('SRF_CLKBuf{}Inv_Stage{}'.format(j, _CLKBufTree_NumOfStage),
                                               'SRF_PMOS', 'BND_Drain_M1')
                elif _CLKBufTree_OutputPlacement == 'Dn':
                    tmp1 = self.get_param_KJH4('SRF_CLKBuf{}Inv_Stage{}'.format(j, _CLKBufTree_NumOfStage),
                                               'SRF_NMOS', 'BND_Drain_M1')
                self._DesignParameter['BND_Buf{}_Output_M2'.format(j)]['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
                self._DesignParameter['BND_Buf{}_Output_M2'.format(j)]['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
                self._DesignParameter['BND_Buf{}_Output_M2'.format(j)]['_XYCoordinates'] = [[0, 0]]

                ## Calculate Sref XYcoord
                tmpXY = []
                ## Calculate
                for k in range(2 ** (_CLKBufTree_NumOfStage - 1)):
                    if _CLKBufTree_OutputPlacement == 'Up':
                        ## Target_coord: _XY_type1
                        tmp1 = self.get_param_KJH4('SRF_CLKBuf{}Inv_Stage{}'.format(j, _CLKBufTree_NumOfStage),
                                                   'SRF_PMOS', 'BND_Drain_M1')
                        target_coord = tmp1[k][0][-1][0]['_XY_up']
                        ## Approaching_coord: _XY_type2
                        tmp2 = self.get_param_KJH4('BND_Buf{}_Output_M2'.format(j))
                        approaching_coord = tmp2[0][0]['_XY_up']

                    elif _CLKBufTree_OutputPlacement == 'Dn':
                        ## Target_coord: _XY_type1
                        tmp1 = self.get_param_KJH4('SRF_CLKBuf{}Inv_Stage{}'.format(j, _CLKBufTree_NumOfStage),
                                                   'SRF_NMOS', 'BND_Drain_M1')
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
            if _CLKBufTree_OutputVia != None and _CLKBufTree_OutputVia > 2:
                _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
                _Caculation_Parameters['_Layer1'] = 2
                _Caculation_Parameters['_Layer2'] = _CLKBufTree_OutputVia
                _Caculation_Parameters['_COX'] = 1
                _Caculation_Parameters['_COY'] = 2

                ## Sref ViaX declaration
                self._DesignParameter['SRF_Buf{}Output_ViaM2M{}'.format(j,_CLKBufTree_OutputVia)] = \
                self._SrefElementDeclaration(
                    _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                           _Name='{}:SRF_Buf{}Output_ViaM2M{}'.format(_Name,
                                                                                                 j,_CLKBufTree_OutputVia)))[0]

                ## Define Sref Relection
                self._DesignParameter['SRF_Buf{}Output_ViaM2M{}'.format(j,_CLKBufTree_OutputVia)]['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle
                self._DesignParameter['SRF_Buf{}Output_ViaM2M{}'.format(j,_CLKBufTree_OutputVia)]['_Angle'] = 0

                ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
                self._DesignParameter['SRF_Buf{}Output_ViaM2M{}'.format(j,_CLKBufTree_OutputVia)]['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

                ## Calculate Sref XYcoord
                tmpXY = []
                ## initialized Sref coordinate
                self._DesignParameter['SRF_Buf{}Output_ViaM2M{}'.format(j,_CLKBufTree_OutputVia)]['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                ## Target_coord
                for k in range(2 ** (_CLKBufTree_NumOfStage - 1)):
                    if _CLKBufTree_OutputPlacement == 'Up':
                        tmp1 = self.get_param_KJH4('BND_Buf{}_Output_M2'.format(j))
                        target_coord = tmp1[k][0]['_XY_up']
                        tmp2 = self.get_param_KJH4('SRF_Buf{}Output_ViaM2M{}'.format(j, _CLKBufTree_OutputVia),'SRF_ViaM2M3', 'BND_Met2Layer')
                        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    elif _CLKBufTree_OutputPlacement == 'Dn':
                        tmp1 = self.get_param_KJH4('BND_Buf{}_Output_M2'.format(j))
                        target_coord = tmp1[k][0]['_XY_down']
                        tmp2 = self.get_param_KJH4('SRF_Buf{}Output_ViaM2M{}'.format(j, _CLKBufTree_OutputVia),'SRF_ViaM2M3', 'BND_Met2Layer')
                        approaching_coord = tmp2[0][0][0][0]['_XY_down']

                    ## Sref coord
                    tmp3 = self.get_param_KJH4('SRF_Buf{}Output_ViaM2M{}'.format(j,_CLKBufTree_OutputVia))
                    Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
                    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                    tmpXY.append(New_Scoord)

                self._DesignParameter['SRF_Buf{}Output_ViaM2M{}'.format(j,_CLKBufTree_OutputVia)]['_XYCoordinates'] = tmpXY


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
        tmp1 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(_CLKBufTree_NumOfStage), 'SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(_CLKBufTree_NumOfStage), 'SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
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
        tmp1 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(_CLKBufTree_NumOfStage), 'SRF_Nbody','SRF_NbodyContactPhyLen','BND_ODLayer')
        tmp2 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(_CLKBufTree_NumOfStage), 'SRF_Nbody','SRF_NbodyContactPhyLen','BND_ODLayer')
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
        tmp1 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(_CLKBufTree_NumOfStage), 'SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(_CLKBufTree_NumOfStage), 'SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
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
        tmp1 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(_CLKBufTree_NumOfStage), 'SRF_Pbody','SRF_PbodyContactPhyLen','BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(_CLKBufTree_NumOfStage), 'SRF_Pbody','SRF_PbodyContactPhyLen','BND_PPLayer')
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
        tmp1 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(_CLKBufTree_NumOfStage), 'SRF_Pbody','SRF_PbodyContactPhyLen','BND_ODLayer')
        tmp2 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(_CLKBufTree_NumOfStage), 'SRF_Pbody','SRF_PbodyContactPhyLen','BND_ODLayer')
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
        tmp1 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(_CLKBufTree_NumOfStage), 'BND_PMOS_NellExten')
        tmp2 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(_CLKBufTree_NumOfStage), 'BND_PMOS_NellExten')
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
        tmp1 = self.get_param_KJH4('SRF_CLKBuf1Inv_Stage{}'.format(_CLKBufTree_NumOfStage), 'SRF_PMOS','BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_CLKBuf2Inv_Stage{}'.format(_CLKBufTree_NumOfStage), 'SRF_PMOS','BND_PPLayer')
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




############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ZZ00_RcdacSar_F00_02_CLKBufferTree'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'F00_02_CLKBufferTree_v2'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        # TreeSize
        _CLKBufTree_TotalLength=50000,  # 양 끝 Poly gate dummy의 Physical한 크기
        _CLKBufTree_NumOfStage=4,  # 스테이지 수 (아래 버퍼 사이즈 리스트의 길이와 같아야 함.)
        _CLKBufTree_Buf1_SizeByStage=[1,2,4,8],
        _CLKBufTree_Buf2_SizeByStage=[1,2,4,8],  # 스테이지에 따른 버퍼 사이즈(UnitBuffer의 배수로 각 스테이지의 크기가 결정 됨.)
        _CLKBufTree_OutputVia=4,  # None이면 비아 생성 안함.(-> default: M2)
        _CLKBufTree_OutputPlacement='Up',

        ## CLK Buffer
        # Inverter
        _CLKBufTree_Inv_NMOS_ChannelWidth=400,  # Number
        _CLKBufTree_Inv_NMOS_ChannelLength=30,  # Number
        _CLKBufTree_Inv_NMOS_NumberofGate=1,  # Number
        _CLKBufTree_Inv_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _CLKBufTree_Inv_NMOS_POGate_Comb_length=100,  # None/Number

        _CLKBufTree_Inv_PMOS_ChannelWidth=800,  # Number
        _CLKBufTree_Inv_PMOS_ChannelLength=30,  # Number
        _CLKBufTree_Inv_PMOS_NumberofGate=1,  # Number
        _CLKBufTree_Inv_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
        _CLKBufTree_Inv_PMOS_POGate_Comb_length=100,  # None/Number

        # PowerRail Size
        _CLKBufTree_NMOS_Pbody_NumCont=2,
        _CLKBufTree_NMOS_Pbody_XvtTop2Pbody=None,
        _CLKBufTree_PMOS_Nbody_NumCont=2,
        _CLKBufTree_PMOS_Nbody_Xvtdown2Nbody=None,
        _CLKBufTree_PMOSXvt2NMOSXvt=446,
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
