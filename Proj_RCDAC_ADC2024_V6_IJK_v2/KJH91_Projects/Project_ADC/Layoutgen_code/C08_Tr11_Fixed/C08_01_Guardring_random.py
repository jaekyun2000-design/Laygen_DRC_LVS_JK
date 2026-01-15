
## Import Basic Modules
    ## Engine
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_ADC.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

    ## Library
import copy
import math
import numpy as np
import time

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A03_NmosWithDummy_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A04_PmosWithDummy_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A05_NbodyContact_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A06_PbodyContact_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A07_NbodyContactPhyLen_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A08_PbodyContactPhyLen_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A09_NbodyRing_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A10_PbodyRing_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A11_NbodyContactforDeepNwell_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A12_NbodyContactPhyLenforDeepNwell_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A13_NbodyRingforDeepNwell_KJH
    ##
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.C08_Tr11_Fixed import C08_00_Tr11_random



## Define Class
class _Guardring(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
# TR11
    # Physical dimension
    _Tr11_NumberofGate	            = 4,       # Number
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
# TR11
    # Physical dimension
    _Tr11_NumberofGate	            = 4,       # Number
    _Tr11_ChannelWidth	            = 500,     # Number
    _Tr11_ChannelLength	            = 30,       # Number
    _Tr11_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT

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

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr11
        ## SREF Generation
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C08_00_Tr11_random._Tr11._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr11_NumberofGate'] = _Tr11_NumberofGate
        _Caculation_Parameters['_Tr11_ChannelWidth'] = _Tr11_ChannelWidth
        _Caculation_Parameters['_Tr11_ChannelLength'] = _Tr11_ChannelLength
        _Caculation_Parameters['_Tr11_XVT'] = _Tr11_XVT

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Tr11'] = self._SrefElementDeclaration(_DesignObj=C08_00_Tr11_random._Tr11(_DesignParameter=None, _Name='{}:SRF_Tr11'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Tr11']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr11']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr11']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Tr11']['_XYCoordinates'] = [[0, 0]]


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Nbodyring
        _Tr11_Guardring_NumCont =3

        ## Guardring
            ## Pre-defined
        _right_margin = 150
        _left_margin = 150
        _up_margin = 150
        _down_margin = 150

            ## Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A09_NbodyRing_KJH3._NbodyRing._ParametersForDesignCalculation)
        _Caculation_Parameters['_XlengthIntn']      = None
        _Caculation_Parameters['_YlengthIntn']      = None
        _Caculation_Parameters['_NumContTop']       = _Tr11_Guardring_NumCont
        _Caculation_Parameters['_NumContBottom']    = _Tr11_Guardring_NumCont
        _Caculation_Parameters['_NumContLeft']      = _Tr11_Guardring_NumCont
        _Caculation_Parameters['_NumContRight']     = _Tr11_Guardring_NumCont
        #_Caculation_Parameters['_NwellWidth']       = _NwellWidth ## used only for DeepNwell

            ## Find Outter boundary
        tmp = self.get_outter_KJH4('SRF_Tr11')

            ## Define _XlengthIntn
        _Caculation_Parameters['_XlengthIntn'] = abs(tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0]) + _right_margin + _left_margin # option: + _NwellWidth

            ## Define _YlengthIntn
        _Caculation_Parameters['_YlengthIntn'] = abs(tmp['_Mostup']['coord'][0] - tmp['_Mostdown']['coord'][0]) + _up_margin + _down_margin # option + _NwellWidth

            ## Generate Sref
        self._DesignParameter['SRF_Nbodyring'] = self._SrefElementDeclaration(_DesignObj=A09_NbodyRing_KJH3._NbodyRing(_DesignParameter=None, _Name='{}:_Nbodyring'.format(_Name)))[0]

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


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Nwell Covering
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Nwellcovering'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['NWELL'][0],
        _Datatype=DesignParameters._LayerMapping['NWELL'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Nbodyring','BND_ExtenNwell_Top')
        tmp2 = self.get_param_KJH4('SRF_Nbodyring','BND_ExtenNwell_Bottom')

        self._DesignParameter['BND_Nwellcovering']['_YWidth'] = abs( tmp1[0][0][0]['_XY_up'][1] - tmp2[0][0][0]['_XY_down'][1] )

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Nbodyring','BND_ExtenNwell_Left')
        tmp2 = self.get_param_KJH4('SRF_Nbodyring','BND_ExtenNwell_Right')

        self._DesignParameter['BND_Nwellcovering']['_XWidth'] = abs( tmp2[0][0][0]['_XY_right'][0] - tmp1[0][0][0]['_XY_left'][0] )

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Nwellcovering']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Nwellcovering']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Nbodyring','BND_ExtenNwell_Bottom')
        target_coord = tmp1[0][0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Nwellcovering')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Nwellcovering')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Nwellcovering']['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Drain and Guardring M1 connection.
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Drain_Vtc_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Tr11','SRF_Pmos','BND_Drain_M1')
        tmp2 = self.get_param_KJH4('SRF_Nbodyring','SRF_NbodyBottom','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_Drain_Vtc_M1']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_down'][1] - tmp2[0][0][0][0][0]['_XY_up'][1] )

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Tr11','SRF_Pmos','BND_Drain_M1')
        self._DesignParameter['BND_Drain_Vtc_M1']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Drain_Vtc_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
        tmp = self.get_param_KJH4('SRF_Tr11','SRF_Pmos','BND_Drain_M1')
        for i in range(0,len(tmp[0][0])):
                            ## initialized Sref coordinate
            self._DesignParameter['BND_Drain_Vtc_M1']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_Tr11','SRF_Pmos','BND_Drain_M1')
            target_coord = tmp1[0][0][i][0]['_XY_down_left']
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Drain_Vtc_M1')
            approaching_coord = tmp2[0][0]['_XY_up_left']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Drain_Vtc_M1')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Drain_Vtc_M1']['_XYCoordinates'] = tmpXY

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
    import random
    ## LibraryName: ex)Proj_ADC_A_my_building_block
    # libname = 'Proj_ZZ01_C08_01_Guardring_Fixed'
    ## CellName: ex)C01_cap_array_v2_84
    for _iter in range(5):
        cellname = 'C08_01_Guardring_v{}'.format(_iter + 1)
        _fileName = cellname + '.gds'

        ''' Input Parameters for Layout Object '''
        InputParams = dict(
    # TR11
        # Physical dimension
        _Tr11_NumberofGate	            = random.randrange(1, 10, 1),       # Number
        _Tr11_ChannelWidth	            = random.randrange(500, 2000, 100),     # Number
        _Tr11_ChannelLength	            = 30,       # Number
        _Tr11_XVT				        = 'RVT',    # 'XVT' ex)SLVT/LVT/RVT/HVT
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
        LayoutObj = _Guardring(_DesignParameter=None, _Name=cellname)
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
    # # Checker.lib_deletion()
    # Checker.cell_deletion()
    # Checker.Upload2FTP()
    # Checker.StreamIn(tech=DesignParameters._Technology)
    # # Checker_KJH0.DRCchecker()

    print('#############################      Finished      ################################')
    print('{} Hours   {} minutes   {} seconds'.format(h, m, s))
# end of 'main():' ---------------------------------------------------------------------------------------------
