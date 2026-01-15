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
from KJH91_Projects.Project_ADC.Layoutgen_code.H00_CDAC_v2 import H00_00_ECAP
from KJH91_Projects.Project_ADC.Layoutgen_code.H00_CDAC_v2 import H00_02_CapWithShield
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3


############################################################################################################################################################ Class_HEADER
class _DummyCapUnit(StickDiagram_KJH1._StickDiagram_KJH):

    _ParametersForDesignCalculation = dict(
        # # Unit CDAC
        _LayoutOption=None,
        _ShieldingLayer=None,  # Poly:0, M1:1, M2:2 ...
        _MetalWidth=None,
        _MetalLength=None,
        _MetalSpacing=None,

        # #Unit Cap
        _NumOfElement=None,

        # # Shielding & Top Connect node
        _ConnectLength=None,
        _ExtendLength=None,

        # Dummy Cap Option
        _DummyCap_TopBottomShort=None
    )
    # Initially Defined design_parameter
    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _Name=self._NameDeclaration(_Name=_Name),
                _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                _XYcoordAsCent=dict(_XYcoordAsCent=0),
            )

    ##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
    def _CalculateDesignParameter(self,
                                  # # Unit CDAC
                                  _LayoutOption=None,
                                  _ShieldingLayer=None,  # Poly:0, M1:1, M2:2 ...
                                  _MetalWidth=None,
                                  _MetalLength=None,
                                  _MetalSpacing=None,

                                  # #Unit Cap
                                  _NumOfElement=None,

                                  # # Shielding & Top Connect node
                                  _ConnectLength=None,
                                  _ExtendLength=None,

                                  # Dummy Cap Option
                                  _DummyCap_TopBottomShort=None
                                  ):

        ################################################################################################################################################## Class_HEADER: Pre Defined Parameter Before Calculation
        # Load DRC library
        _DRCobj = DRC.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ############################################################################################################################################################ CALCULATION START
        DummyCapUnit_start_time = time.time()
        print('#########################################################################################################')
        print( '                                      Calculation Start                                                  ')
        print('#########################################################################################################')

        ## Generation of Top Shielding Metal
            ## SREF Generation
            ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(H00_02_CapWithShield._CapWithShield._ParametersForDesignCalculation)
        _Caculation_Parameters['_LayoutOption'] = _LayoutOption
        _Caculation_Parameters['_ShieldingLayer'] = _ShieldingLayer
        _Caculation_Parameters['_MetalWidth'] = _MetalWidth
        _Caculation_Parameters['_MetalLength'] = _MetalLength
        _Caculation_Parameters['_MetalSpacing'] = _MetalSpacing
        _Caculation_Parameters['_NumOfElement'] = _NumOfElement
        _Caculation_Parameters['_ConnectLength'] = _ConnectLength
        _Caculation_Parameters['_ExtendLength'] = _ExtendLength

        self._DesignParameter['SRF_CapWtShield4DCAP'] = \
        self._SrefElementDeclaration(_DesignObj=H00_02_CapWithShield.
                                     _CapWithShield(_DesignParameter=None,
                                                    _Name='{}:SRF_CapWtShield4DCAP'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_CapWtShield4DCAP']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CapWtShield4DCAP']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CapWtShield4DCAP']['_DesignObj']._CalculateDesignParameter(
            **_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CapWtShield4DCAP']['_XYCoordinates'] = [[0, 0]]


        if _DummyCap_TopBottomShort == True:
                # Bottom plate를 Top Plate에 연결하는 방식에서 DRC 에러 발생하여 수정 필요.
            # ## Sref generation: ViaX
            # ## Define ViaX Parameter
            # _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
            # _Caculation_Parameters['_Layer1'] = _LayoutOption[0]
            # _Caculation_Parameters['_Layer2'] = 7
            # _Caculation_Parameters['_COX'] = None
            # _Caculation_Parameters['_COY'] = None
            #
            # ## Sref ViaX declaration
            # self._DesignParameter['SRF_DummyBotViaM{}M{}'.format(_LayoutOption[0], 7)] = self._SrefElementDeclaration(
            #     _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_DummyBotViaM{}M{}'.format(_Name,_LayoutOption[0], 7)))[0]
            #
            # ## Define Sref Relection
            # self._DesignParameter['SRF_DummyBotViaM{}M{}'.format(_LayoutOption[0], 7)]['_Reflect'] = [0, 0, 0]
            #
            # ## Define Sref Angle
            # self._DesignParameter['SRF_DummyBotViaM{}M{}'.format(_LayoutOption[0], 7)]['_Angle'] = 0
            #
            # ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY' or 'SameEnclosure'
            # tmp = self.get_param_KJH4('SRF_CapWtShield4DCAP','SRF_UCAP','SRF_ECAP','BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
            # _COX, _COY = self._CalculateNumViaByXYWidth(tmp[0][0][0][0][0]['_Xwidth'], tmp[0][0][0][0][0]['_Ywidth'], 'MinEnclosureX')
            #
            # ## Define _COX and _COY
            # _Caculation_Parameters['_COX'] = _COX
            # _Caculation_Parameters['_COY'] = _COY
            #
            # ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
            # self._DesignParameter['SRF_DummyBotViaM{}M{}'.format(_LayoutOption[0], 7)]['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)
            #
            # ## Calculate Sref XYcoord
            # tmpXY = []
            # ## initialized Sref coordinate
            # self._DesignParameter['SRF_DummyBotViaM{}M{}'.format(_LayoutOption[0], 7)]['_XYCoordinates'] = [[0, 0]]
            # ## Calculate
            # ## Target_coord
            # tmp1 = self.get_param_KJH4('SRF_CapWtShield4DCAP','SRF_UCAP','SRF_ECAP','BND_ECAP_Bot_VTC_M{}'.format(_LayoutOption[0]))
            # tmp1y = self.get_param_KJH4('SRF_CapWtShield4DCAP','SRF_UCAP','SRF_ECAP','BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
            # target_coord = [tmp1[0][0][0][0][0]['_XY_cent'][0], tmp1y[0][0][0][0][0]['_XY_cent'][1]]
            # ## Approaching_coord
            # tmp2 = self.get_param_KJH4('SRF_DummyBotViaM{}M{}'.format(_LayoutOption[0], 7), 'SRF_ViaM{}M{}'.format(_LayoutOption[0], _LayoutOption[0]+1), 'BND_Met{}Layer'.format(_LayoutOption[0]))
            # approaching_coord = tmp2[0][0][0][0]['_XY_cent']
            # ## Sref coord
            # tmp3 = self.get_param_KJH4('SRF_DummyBotViaM{}M{}'.format(_LayoutOption[0], 7))
            # Scoord = tmp3[0][0]['_XY_origin']
            # ## Calculate
            # New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            # tmpXY.append(New_Scoord)
            #
            # for i in range(_NumOfElement-1):
            #     CentBtwTopNode = 2*(_MetalWidth+_MetalSpacing)
            #     tmp = tmpXY[i] + [CentBtwTopNode * (i+1), 0]
            #     tmpXY.append(tmp)

            ## Boundary_element Generation
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_TopBottom_Short_Hrz_M{}'.format(_LayoutOption[-1])] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL{}'.format(_LayoutOption[-1])][0],
                _Datatype=DesignParameters._LayerMapping['METAL{}'.format(_LayoutOption[-1])][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )
            ## Define Boundary_element _YWidth
            TopBottomShortPathWidth = 200
            self._DesignParameter['BND_TopBottom_Short_Hrz_M{}'.format(_LayoutOption[-1])]['_YWidth'] = TopBottomShortPathWidth

            ## Define Boundary_element _XWidth
            tmp = self.get_param_KJH4('SRF_CapWtShield4DCAP', 'BND_Shield_Hrz_M{}'.format(_ShieldingLayer))
            self._DesignParameter['BND_TopBottom_Short_Hrz_M{}'.format(_LayoutOption[-1])]['_XWidth'] = tmp[0][0][0]['_Xwidth']

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['BND_TopBottom_Short_Hrz_M{}'.format(_LayoutOption[-1])]['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_CapWtShield4DCAP', 'SRF_UCAP', 'SRF_ECAP',
                                       'BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
            target_coord = tmp1[0][0][0][0][0]['_XY_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_TopBottom_Short_Hrz_M{}'.format(_LayoutOption[-1]))
            approaching_coord = tmp2[0][0]['_XY_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_TopBottom_Short_Hrz_M{}'.format(_LayoutOption[-1]))
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_TopBottom_Short_Hrz_M{}'.format(_LayoutOption[-1])]['_XYCoordinates'] = tmpXY

        elif _DummyCap_TopBottomShort == False: ## Bottom == Ground
            print("Dummy Caps Top, Bottom Node Setting; Top == Common, Bottom == GND")
            ## Sref generation: ViaX
            ## Define ViaX Parameter
            _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
            _Caculation_Parameters['_Layer1'] = _ShieldingLayer
            _Caculation_Parameters['_Layer2'] = _LayoutOption[0]
            _Caculation_Parameters['_COX'] = None
            _Caculation_Parameters['_COY'] = None

            ## Sref ViaX declaration
            self._DesignParameter['SRF_DummyBotViaM{}M{}'.format(_ShieldingLayer, _LayoutOption[0])] = self._SrefElementDeclaration(
                _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_DummyBotViaM{}M{}'.format(_Name,_ShieldingLayer, _LayoutOption[0])))[0]

            ## Define Sref Relection
            self._DesignParameter['SRF_DummyBotViaM{}M{}'.format(_ShieldingLayer, _LayoutOption[0])]['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
            self._DesignParameter['SRF_DummyBotViaM{}M{}'.format(_ShieldingLayer, _LayoutOption[0])]['_Angle'] = 0

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY' or 'SameEnclosure'
            tmp = self.get_param_KJH4('SRF_CapWtShield4DCAP','SRF_UCAP','SRF_ECAP','BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
            _COX, _COY = self._CalculateNumViaByXYWidth(tmp[0][0][0][0][0]['_Xwidth'], tmp[0][0][0][0][0]['_Ywidth'], 'MinEnclosureX')

            ## Define _COX and _COY
            _Caculation_Parameters['_COX'] = _COX
            _Caculation_Parameters['_COY'] = _COY

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
            self._DesignParameter['SRF_DummyBotViaM{}M{}'.format(_ShieldingLayer, _LayoutOption[0])]['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['SRF_DummyBotViaM{}M{}'.format(_ShieldingLayer, _LayoutOption[0])]['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord
            tmp1 = self.get_param_KJH4('SRF_CapWtShield4DCAP','SRF_UCAP','SRF_ECAP','BND_ECAP_Bot_VTC_M{}'.format(_LayoutOption[0]))
            tmp1y = self.get_param_KJH4('SRF_CapWtShield4DCAP','SRF_UCAP','SRF_ECAP','BND_ECAP_Top_VTC_M{}'.format(_LayoutOption[0]))
            target_coord = [tmp1[0][0][0][0][0]['_XY_cent'][0], tmp1y[0][0][0][0][0]['_XY_cent'][1]]
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_DummyBotViaM{}M{}'.format(_ShieldingLayer, _LayoutOption[0]), 'SRF_ViaM{}M{}'.format(_ShieldingLayer, _ShieldingLayer+1), 'BND_Met{}Layer'.format(_ShieldingLayer))
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_DummyBotViaM{}M{}'.format(_ShieldingLayer, _LayoutOption[0]))
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

            for i in range(_NumOfElement-1):
                CentBtwTopNode = 2*(_MetalWidth+_MetalSpacing)
                tmp = tmpXY[i] + [CentBtwTopNode * (i+1), 0]
                tmpXY.append(tmp)

            ## Define
            self._DesignParameter['SRF_DummyBotViaM{}M{}'.format(_ShieldingLayer, _LayoutOption[0])]['_XYCoordinates'] = tmpXY
        else:
            ## None == Floating Bottom Node
            print("Dummy Caps Top, Bottom Node Setting; Top == Common, Bottom == Floating")



        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')
        DummyCapUnit_end_time = time.time()
        self.DummyCapUnit_elapsed_time = DummyCapUnit_end_time - DummyCapUnit_start_time

if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_ZZ00_RcdacSar_H00_03_DummyCapUnit_None'
    cellname = 'H00_00_DummyCapUnit_'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object ''' ############################################################### ^^^^^^^^^^^^^^^^^^^^^
    InputParams = dict(
        # # Unit CDAC
        _LayoutOption=[4,5],        # Poly:0, M1:1, M2:2 ...
        _ShieldingLayer=2,
        _MetalWidth=50,
        _MetalLength=1414,
        _MetalSpacing=50,

        # #Unit Cap
        _NumOfElement=2,

        # # Shielding & Top Connect node
        _ConnectLength=400,
        _ExtendLength=400,

        # Dummy Cap Option
        _DummyCap_TopBottomShort=None
     )

    '''Mode_DRCCHECK '''

    Mode_DRCCheck = False
    Num_DRCCheck =1

    for ii in range(0, Num_DRCCheck if Mode_DRCCheck else 1):
        if Mode_DRCCheck:
            ''' Input Parameters for Layout Object '''
        else:
            pass

    ''' Generate Layout Object '''
    LayoutObj = _DummyCapUnit(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    ''' Check Time'''
    elapsed_time = time.time() - start_time
    m, s = divmod(elapsed_time,60)
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
    #Checker.lib_deletion()
    #Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    #Checker_KJH0.DRCchecker()


    print ('#############################      Finished      ################################')
    print('{} Hours   {} minutes   {} seconds'.format(h, m, s))

    # end of 'main():' ---------------------------------------------------------------------------------------------