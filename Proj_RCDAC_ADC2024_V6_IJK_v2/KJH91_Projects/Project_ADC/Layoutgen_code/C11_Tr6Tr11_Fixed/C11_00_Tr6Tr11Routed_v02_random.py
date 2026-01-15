## Import Basic Modules
    ## Engine
from Proj_RCDAC_ADC2024_V6_IJK.KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_ADC.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC
#from KJH91_Projects.Project_ADC.Library_and_Engine import DRCv2

    ## Library
import copy
import math
import numpy as np
import time

    ## KJH91 Basic Building Blocks
from Proj_RCDAC_ADC2024_V6_IJK.KJH91_Projects.Project_ADC.Layoutgen_code.C08_Tr11_Fixed import C08_01_Guardring_random
from Proj_RCDAC_ADC2024_V6_IJK.KJH91_Projects.Project_ADC.Layoutgen_code.C09_Tr6_Fixed import C09_01_Guardring


############################################################################################################################################################ Class_HEADER

class _Tr4Tr6Routed(StickDiagram_KJH1._StickDiagram_KJH):

    ##########################################################################################################################
    # Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(
# TR6
    # Physical dimension
    _Tr6_NumberofGate	            = 1,       # Number
    _Tr6_ChannelWidth	            = 500,     # Number
    _Tr6_ChannelLength	            = 30,       # Number
    _Tr6_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR11
    # Physical dimension
    _Tr11_NumberofGate	            = 1,       # Number
    _Tr11_ChannelWidth	            = 500,     # Number
    _Tr11_ChannelLength	            = 30,       # Number
    _Tr11_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
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
# TR6
    # Physical dimension
    _Tr6_NumberofGate	            = 1,       # Number
    _Tr6_ChannelWidth	            = 500,     # Number
    _Tr6_ChannelLength	            = 30,       # Number
    _Tr6_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

# TR11
    # Physical dimension
    _Tr11_NumberofGate	            = 1,       # Number
    _Tr11_ChannelWidth	            = 500,     # Number
    _Tr11_ChannelLength	            = 30,       # Number
    _Tr11_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  ):

        ## Class_HEADER: Pre Defined Parameter Before Calculation
        Tr6Tr11GateRoutePathWidth = 250
        Tr6Tr11DrainRoutePathWidth = 250
        LeftExtensionTr6Drain_Hrz_M4 = 1500

        ## Load DRC library
        _DRCObj = DRC.DRC()
        ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']
        ## CALCULATION START
        start_time = time.time()
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

        ## Tr11 SREF Generation
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C08_01_Guardring_random._Guardring._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr11_NumberofGate'] = _Tr11_NumberofGate
        _Caculation_Parameters['_Tr11_ChannelWidth'] = _Tr11_ChannelWidth
        _Caculation_Parameters['_Tr11_ChannelLength'] = _Tr11_ChannelLength
        _Caculation_Parameters['_Tr11_XVT'] = _Tr11_XVT

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Tr11'] = self._SrefElementDeclaration(_DesignObj=C08_01_Guardring_random._Guardring(_DesignParameter=None, _Name='{}:SRF_Tr11'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Tr11']['_Reflect'] = [1, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr11']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr11']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr11']['_XYCoordinates'] = [[0, 0]]

        ## Tr6 SREF Generation
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C09_01_Guardring._Guardring._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr6_NumberofGate'] = _Tr6_NumberofGate
        _Caculation_Parameters['_Tr6_ChannelWidth'] = _Tr6_ChannelWidth
        _Caculation_Parameters['_Tr6_ChannelLength'] = _Tr6_ChannelLength
        _Caculation_Parameters['_Tr6_XVT'] = _Tr6_XVT

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Tr6'] = self._SrefElementDeclaration(_DesignObj=C09_01_Guardring._Guardring(_DesignParameter=None, _Name='{}:SRF_Tr6'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Tr6']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr6']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr6']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr6']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Tr6 Sref XYcoord
        tmpXY = []

        tmp1_1 = self.get_param_KJH4('SRF_Tr11','BND_Nwellcovering')
        target_coordy = tmp1_1[0][0][0]['_XY_up'][1]     #Tr11 맨 아래 가운데 좌표
        tmp1_2 = self.get_param_KJH4('SRF_Tr11','SRF_Tr11','SRF_Pmos','BND_Gate_Hrz_Mx')
        target_coordx = tmp1_2[0][0][0][0][0]['_XY_right'][0]
        target_coord = [target_coordx, target_coordy]

        tmp2 = self.get_param_KJH4('SRF_Tr6','SRF_Tr6','SRF_Nmos','BND_Gate_Hrz_Mx')
        approaching_coordx = tmp2[0][0][0][0][0]['_XY_right'][0]
        approaching_coordy = self.get_outter_KJH4('SRF_Tr6')['_Mostup']['coord'][0]   #Tr6맨 위 가운데 좌표
        approaching_coord = [approaching_coordx,approaching_coordy]

        tmp3 = self.get_param_KJH4('SRF_Tr6')
        Scoord = tmp3[0][0]['_XY_origin']

        tmp4_1 = self.get_param_KJH4('SRF_Tr11', 'SRF_Nbodyring', 'SRF_NbodyTop', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')[0][0][0][0][0][0]['_XY_up'][1]
        tmp4_2 = target_coord[1]
        tmp5_1 = self.get_param_KJH4('SRF_Tr6', 'SRF_Pbodyring', 'SRF_PbodyTop', 'SRF_PbodyContactPhyLen','BND_PPLayer')[0][0][0][0][0][0]['_XY_up'][1]
        tmp5_2 = self.get_param_KJH4('SRF_Tr6', 'SRF_Pbodyring', 'SRF_PbodyTop', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')[0][0][0][0][0][0]['_XY_up'][1]
        # a= abs(tmp4_1 - tmp4_2)
        # b=abs(tmp5_1 - tmp5_2)
        Tr6Tr11MinSpace = _DRCObj._Metal1MinSpace3 - abs(tmp4_1 - tmp4_2) - abs(tmp5_1 - tmp5_2) # Tr6Tr11MinSpace=63
        Tr6Tr11Space = 40
        Scoord[1] = Scoord[1] - max(Tr6Tr11MinSpace, Tr6Tr11Space)

        # c= self.get_outter_KJH4('SRF_Tr6')['_Mostup']['coord'][0]

                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['SRF_Tr6']['_XYCoordinates'] = tmpXY




        ## Tr6 - Tr11 Gate routing (M3)
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Tr6Tr11GateRouting_Vtc_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Tr11','SRF_Tr11','SRF_Pmos','BND_Gate_Hrz_Mx')
        tmp2 = self.get_param_KJH4('SRF_Tr6', 'SRF_Tr6','SRF_Nmos','BND_Gate_Hrz_Mx')
        self._DesignParameter['BND_Tr6Tr11GateRouting_Vtc_M2']['_YWidth'] = tmp1[0][0][0][0][0]['_XY_down_right'][1] - tmp2[0][0][0][0][0]['_XY_down_right'][1]

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Tr6Tr11GateRouting_Vtc_M2']['_XWidth'] = Tr6Tr11GateRoutePathWidth

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Tr6Tr11GateRouting_Vtc_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = [0, tmp1[0][0][0][0][0]['_XY_down'][1]]
        target_coord[0] = min([tmp1[0][0][0][0][0]['_XY_up_right'][0], tmp2[0][0][0][0][0]['_XY_down_right'][0]]) #더 왼쪽에 있는 좌표 리턴
                            ## Approaching_coord: _XY_type2
        tmp = self.get_param_KJH4('BND_Tr6Tr11GateRouting_Vtc_M2')
        approaching_coord = tmp[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Tr6Tr11GateRouting_Vtc_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Tr6Tr11GateRouting_Vtc_M2']['_XYCoordinates'] = tmpXY



        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Path_element Generation 2
        ## Path Name:
        Path_name = 'Tr6Tr11DrainRouting_M3'

        ## Path Width: ***** must be even number ***
        Path_width = Tr6Tr11DrainRoutePathWidth

        ## tmp
        tmpXY = []
        tmpMetal = []
        tmpViaTF = []
        tmpViaDir = []
        tmpViaWid = []

        ## coord1
        ## P1 calculation
        tmp = self.get_param_KJH4('SRF_Tr11','SRF_Tr11','SRF_Source_ViaM2M3','SRF_ViaM2M3','BND_Met3Layer')
        P1 = tmp[0][0][0][0][0][0]['_XY_left']
        ## P2 calculation
        tmp1_2 = self.get_param_KJH4('SRF_Tr6','SRF_Tr6','SRF_Source_ViaM2M3','SRF_ViaM2M3','BND_Met3Layer')
        P2 = [tmp1_2[0][0][0][0][0][0]['_XY_left'][0],tmp[0][0][0][0][0][0]['_XY_left'][1]]
        ## Metal Layer
        Metal = 3
        ## Via: True=1/False=0
        ViaTF = 0
        ## Via: Vtc=1/Hrz=0/Ovl=2
        ViaDir = 1
        ## Via width: None/[1,3]
        ViaWid = None

        tmpXY.append([P1, P2])
        tmpMetal.append(Metal)
        tmpViaTF.append(ViaTF)
        tmpViaDir.append(ViaDir)
        tmpViaWid.append(ViaWid)

        ## coord2
        ## P1 calculation
        P1 = copy.deepcopy(P2)
        ## P2 calculation
        tmp = self.get_param_KJH4('SRF_Tr6','SRF_Tr6','SRF_Source_ViaM2M3','SRF_ViaM2M3','BND_Met3Layer')
        P2 = tmp[0][0][0][0][0][0]['_XY_down_left']
        ## Metal Layer
        Metal = 3
        ## Via True=1/False=0
        ViaTF = 0
        ## Via Vtc=1/Hrz=0/Ovl=2
        ViaDir = 2
        ## Via width: None/[1,3]
        ViaWid = None

        tmpXY.append([P1, P2])
        tmpMetal.append(Metal)
        tmpViaTF.append(ViaTF)
        tmpViaDir.append(ViaDir)
        tmpViaWid.append(ViaWid)


        tmpXY = self.get_PTH_KJH2(Path_name, Path_width, tmpXY, tmpMetal, tmpViaTF, tmpViaDir, tmpViaWid, _Name)


        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')
        end_time = time.time()
        self.elapsed_time = end_time - start_time


############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    Start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0
    import random
    ## LibraryName: ex)Proj_ADC_A_my_building_block
    # libname = 'Proj_ZZ01_C11_00_Tr6Tr11Routed_Fixed'
    for _iter in range(5):
        cellname = 'Proj_C11_00_Tr6Tr11Routed_v{}'.format(_iter + 2 )
        _fileName = cellname + '.gds'
        Gate = random.randrange(1, 5, 1)
        Width = random.randrange(400, 1000, 100)

        ''' Input Parameters for Layout Object '''
        InputParams = dict(
    # TR6
        # Physical dimension
        _Tr6_NumberofGate	            = Gate,       # Number
        _Tr6_ChannelWidth	            = Width,     # Number
        _Tr6_ChannelLength	            = 30,       # Number
        _Tr6_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

    # TR11
        # Physical dimension
        _Tr11_NumberofGate	            = Gate,       # Number
        _Tr11_ChannelWidth	            = Width,     # Number
        _Tr11_ChannelLength	            = 30,       # Number
        _Tr11_XVT				        = 'SLVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

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
        LayoutObj = _Tr4Tr6Routed(_DesignParameter=None, _Name=cellname)
        LayoutObj._CalculateDesignParameter(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
        testStreamFile = open('./{}'.format(_fileName), 'wb')
        # testStreamFile = open('./gdsfile/{}'.format(_fileName), 'wb')
        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

    ''' Check Time'''
    elapsed_time = time.time() - Start_time
    m, s = divmod(elapsed_time, 60)
    h, m = divmod(m, 60)

    # print('###############      Sending to FTP Server...      ##################')
    # My = MyInfo.USER(DesignParameters._Technology)
    # Checker = DRCchecker_KJH0.DRCchecker_KJH0(
    # username=My.ID,
    # password=My.PW,
    # WorkDir=My.Dir_Work,
    # DRCrunDir=My.Dir_DRCrun,
    # libname=libname,
    # cellname=cellname,
    # GDSDir=My.Dir_GDS
    # )
    # Checker.lib_deletion()
    # # Checker.cell_deletion()
    # Checker.Upload2FTP()
    # Checker.StreamIn(tech=DesignParameters._Technology)
    # # Checker_KJH0.DRCchecker()

    print('#############################      Finished      ################################')
    print('{} Hours   {} minutes   {} seconds'.format(h, m, s))
# end of 'main():' ---------------------------------------------------------------------------------------------
