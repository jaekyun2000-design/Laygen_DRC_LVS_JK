
start_time = time.time()
end_time = time.time()
self.elapsed_time = end_time - start_time

print('{} Hours   {} minutes   {} seconds'.format(h, m, s))

## Import Basic Modules
    ## Engine
from KJH91_Projects."-Project_name-".Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects."-Project_name-".Library_and_Engine import DesignParameters
from KJH91_Projects."-Project_name-".Library_and_Engine import DRC

    ## Library
import copy
import math
import numpy as np
import time

    ## KJH91 Basic Building Blocks
from KJH91_Projects."-Project_name-".Layoutgen_code.A_Building_block_KJH import A00_NmosWithDummy_KJH
from KJH91_Projects."-Project_name-".Layoutgen_code.A_Building_block_KJH import A01_PmosWithDummy_KJH


## Define Class
class "-Classname-"(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(

    )

    ## Initially Generated _DesignParameter
    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
            _Name=self._NameDeclaration(_Name=_Name),
            _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
            _XYcoordAsCent=dict(_XYcoordAsCent=0),  # downleft_coordination == 0
            )

    ## DesignParameter Calculation
    def _CalculateDesignParameter(self,

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





            ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy('-filename-'.'-classname-'._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['--Internally_defined_parameter_list--'] = '-Currently_defined_parameter_list-'

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['--elementname--'] = self._SrefElementDeclaration(_DesignObj='-filename-'.'-classname-'(_DesignParameter=None, _Name='{}:--elementname--'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['--elementname--']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['--elementname--']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['--elementname--']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['--elementname--']['_XYCoordinates'] = [[0, 0]]





		

            ## Boundary_element Generation
        Element_name = ''
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter[Element_name] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['--LayerName--'][0],
        _Datatype=DesignParameters._LayerMapping['--LayerName--'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter[Element_name]['_YWidth'] = '?'

                ## Define Boundary_element _XWidth
        self._DesignParameter[Element_name]['_XWidth'] = '?'

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter[Element_name]['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter[Element_name]['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('--elementname_Target--')
        target_coord = tmp1[?][?][0]['_XY_type1']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4(Element_name)
        approaching_coord = tmp2[0][0]['_XY_type2']
                            ## Sref coord
        tmp3 = self.get_param_KJH4(Element_name)
        Scoord = tmp3[?][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter[Element_name]['_XYCoordinates'] = tmpXY







        ## Path_element Generation 1
            ## Define Path_element ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['--pathelementname--'] = self._PathElementDeclaration(
        _Layer=DesignParameters._LayerMapping['--LayerName--'][0],
        _Datatype=DesignParameters._LayerMapping['--LayerName--'][1],
        _XYCoordinates=[],
        _Width=None,
        )

        ## Path Width: ***** must be even number ***
        Path_width = '??'
        self._DesignParameter['--pathelementname--']['_Width'] = Path_width

        tmpXY = []
            ## P1--P2 coordiantes
                ## P1 calculation
        P1 = ['?','?']
                ## P2 calculation
        P2 = ['?','?']
                ## P1_P2
        P1_P2 = [P1, P2]
        tmpXY.append(P1_P2)

            ## P3--P4 coordiantes
                ## P3 calculation
        P3 = ['?','?']
                ## P4 calculation
        P4 = ['?','?']
                ## P1_P2
        P3_P4 = [P3, P4]
        tmpXY.append(P3_P4)

            ## Define Coordinates
        tmpXY = self.get_PTHcoord_KJH(tmpXY, Path_width)
        self._DesignParameter['pathelementname']['_XYCoordinates'] = tmpXY
        
        
        
        
        
        
        
        
        
        
        
        ###### Path_element Generation 2
        ## Path Name:
        Path_name = 'A'
        
        ## Path Width: ***** must be even number ***
        Path_width = 150
        
        ## tmp
        tmpXY = []
        tmpMetal = []
        tmpViaTF = []
        tmpViaDir = []
        tmpViaWid = []
        
        ## coord1
        ## P1 calculation
        P1 = [0, 5000]
        ## P2 calculation
        P2 = [0, -1000]
        ## Metal Layer
        Metal = 1
        ## Via: True=1/False=0
        ViaTF = 0
        ## Via: Vtc=1/Hrz=0/Ovl=2
        ViaDir = 2
        ## Via width: None/[1,3]
        ViaWid = None
        
        tmpXY.append([P1, P2])
        tmpMetal.append(Metal)
        tmpViaTF.append(ViaTF)
        tmpViaDir.append(ViaDir)
        tmpViaWid.append(ViaWid)
        
        ## coord2
        ## P1 calculation
        P1 = copy.deepcopy(P1) # = [0, -1000]
        ## P2 calculation
        P2 = [5000, -1000]
        ## Metal Layer
        Metal = 1
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
        
        ## coord3
        ## P1 calculation
        P1 = [5000, -1000]
        ## P2 calculation
        P2 = [5000, -8000]
        ## Metal Layer
        Metal = 4
        ## Via True=1/False=0
        ViaTF = 1
        ## Via Vtc=1/Hrz=0/Ovl=2
        ViaDir = 1
        ## Via width: None/[1,3]
        ViaWid = None
        
        tmpXY.append([P1, P2])
        tmpMetal.append(Metal)
        tmpViaTF.append(ViaTF)
        tmpViaDir.append(ViaDir)
        tmpViaWid.append(ViaWid)
        
        tmpXY = self.get_PTH_KJH2(Path_name, Path_width, tmpXY, tmpMetal, tmpViaTF, tmpViaDir, tmpViaWid,_Name)
        





        ## Sref generation: ViaX
        ViaName = ''
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = None
        _Caculation_Parameters['_Layer2'] = None
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

            ## Sref ViaX declaration
        self._DesignParameter[ViaName] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:{}'.format(_Name,ViaName)))[0]

            ## Define Sref Relection
        self._DesignParameter[ViaName]['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter[ViaName]['_Angle'] = 0

            ## Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH4('--Metalx--')
        tmp2 = self.get_param_KJH4('--Metaly--')
        Ovlpcoord = self.get_ovlp_KJH2(tmp1['?']['?'], tmp2['?']['?'])

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY' or 'SameEnclosure'
        _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], None)

            ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter[ViaName]['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter[ViaName]['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        tmp1 = self.get_param_KJH4('--TargetElementName--')
        target_coord = tmp1[?][?]['_XYtype1']
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('--Elementname_Approaching--')
        approaching_coord = tmp2[?][?]['_XYtype2']
                    ## Sref coord
        tmp3 = self.get_param_KJH4(ViaName)
        Scoord = tmp3[?][?]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter[ViaName]['_XYCoordinates'] = tmpXY







        ## Guardring
            ## Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A09_NbodyRing_KJH2._NbodyRing_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_XlengthIntn']      = None
        _Caculation_Parameters['_YlengthIntn']      = None
        _Caculation_Parameters['_NumContTop']       = _NumCont
        _Caculation_Parameters['_NumContBottom']    = _NumCont
        _Caculation_Parameters['_NumContLeft']      = _NumCont
        _Caculation_Parameters['_NumContRight']     = _NumCont
        #_Caculation_Parameters['_NwellWidth']       = _NwellWidth ## used only for DeepNwell

            ## Find Outter boundary
        tmp = self.get_outter_KJH4('--TargetSRF--')

            ## Define _XlengthIntn
        _Caculation_Parameters['_XlengthIntn'] = abs(tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0]) + _right_margin + _left_margin # option: + _NwellWidth

            ## Define _YlengthIntn
        _Caculation_Parameters['_YlengthIntn'] = abs(tmp['_Mostup']['coord'][0] - tmp['_Mostdown']['coord'][0]) + _up_margin + _down_margin # option + _NwellWidth

            ## Generate Sref
        self._DesignParameter['SRF_Nbodyring'] = self._SrefElementDeclaration(_DesignObj=A09_NbodyRing_KJH2._NbodyRing_KJH2(_DesignParameter=None, _Name='{}:_Nbodyring'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Nbodyring']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Nbodyring']['_Angle'] = 0

            ## Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_Nbodyring']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            ## Define Sref _XYcoordinate
        self._DesignParameter['SRF_Nbodyring']['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Nbodyring']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        target_coord = [tmp['_Mostleft']['coord'][0], tmp['_Mostdown']['coord'][0]]
                    ## Approaching_coord
                        ## x
        tmp2_1 = self.get_param_KJH4('SRF_Nbodyring', 'SRF_NbodyLeft', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coordx = tmp2_1[0][0][0][0][0]['_XY_right'][0]
                        ## y
        tmp2_2 = self.get_param_KJH4('SRF_Nbodyring', 'SRF_NbodyBottom', 'SRF_NbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coordy = tmp2_2[0][0][0][0][0]['_XY_up'][1]

        approaching_coord = [approaching_coordx, approaching_coordy]
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Nbodyring')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] - _left_margin # option: - _NwellWidth
        New_Scoord[1] = New_Scoord[1] - _down_margin # option: - _NwellWidth
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Nbodyring']['_XYCoordinates'] = tmpXY









        ## Labeling: ex)METAL1PIN, METAL2PIN, METAL3PIN, METAL4PIN, METAL5PIN, METAL6PIN, METAL7PIN, METAL8PIN(IA), METAL9PIN(IB),
        self._DesignParameter['--TXT_portname--'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['--Label--'][0],
            _Datatype=DesignParameters._LayerMapping['--Label--'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT=None,
            _XYCoordinates=None,
        )

            # Portname
        self._DesignParameter['--TXT_portname--']['_TEXT'] = '--Portname--'

            ## Calculate Sref XYcoord
        tmp = self.get_param_KJH4('--TargetElement--')
        tmpXY = tmp[?][?][0]['_XY_cent']
        self._DesignParameter['--TXT_portname--']['_XYCoordinates'] = [tmpXY]








                ## Get_Outter : tmp['_Most--']['coord'] ex) down, left, right, up
        tmp = self.get_outter_KJH4('--elementname--')
        output_element = tmp['_Most-']['index']
        output_elementname = tmp['_Layercoord'][output_element[0]][1]
        outter_coord = tmp['_Most-']['coord']






                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['--elementname_MovingSref--']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('--elementname_Target--')
        target_coord = tmp1[?][?][0]['_XY_type1']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('--elementname_Approaching--')
        approaching_coord = tmp2[?][?][0]['_XY_type2']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('--elementname_MovingSref--')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['--elementname_MovingSref--']['_XYCoordinates'] = tmpXY



        ## Get_ovlp_coord.
        # Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH2('elementname_A-----')  ##########^^^^^^^^^^^^^^^^^^^^^
        tmp2 = self.get_param_KJH2('elementname_B-----')  ##########^^^^^^^^^^^^^^^^^^^^^

        Ovlpcoord = self.get_ovlp_coord_KJH(tmp1['____number1'], tmp2['____number2'])  ##########2^^^^^^^^^^^^^^^^^^^^^ number: choose num from multiple_object


        ## Rename : example기 SRF_Thermo_Cnt를 SRF_DAC_Ctrl로 바꿈.
        #self._DesignParameter['SRF_DAC_Ctrl'] = copy.deepcopy(self._DesignParameter['SRF_Thermo_Cnt'])
        #self.rename_srf_prefix(self._DesignParameter['SRF_DAC_Ctrl'], 'SRF_Thermo_Cnt', 'SRF_DAC_Ctrl')

        self._DesignParameter['--SRF_new--'] = copy.deepcopy(self._DesignParameter['--SRF_old--'])
        self.rename_srf_prefix(self._DesignParameter['--SRF_new--'], '--SRF_old--', '--SRF_new--')




        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    Start_time = time.time()

    from KJH91_Projects."-Project_name-".Library_and_Engine.Private import MyInfo
    from KJH91_Projects."-Project_name-".Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = '--LibaryName--'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = '--CellName--'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

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
    LayoutObj = '-ClassName-'(_DesignParameter=None, _Name=cellname)
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
    elapsed_time = time.time() - Start_time
    m, s = divmod(elapsed_time, 60)
    h, m = divmod(m, 60)

    print('#############################      Finished      ################################')
# end of 'main():' ---------------------------------------------------------------------------------------------
