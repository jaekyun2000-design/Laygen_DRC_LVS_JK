
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
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A03_NmosWithDummy_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A04_PmosWithDummy_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A05_NbodyContact_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A06_PbodyContact_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A07_NbodyContactPhyLen_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A08_PbodyContactPhyLen_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A09_NbodyRing_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A10_PbodyRing_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A11_NbodyContactforDeepNwell_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A12_NbodyContactPhyLenforDeepNwell_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A13_NbodyRingforDeepNwell_KJH
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A14_Mosfet_KJH3


## Define Class
class _Tr11(StickDiagram_KJH1._StickDiagram_KJH):

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
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  M4, nfettw: Sref Gen.
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A14_Mosfet_KJH3._Mosfet._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_MosType'] = 'PMOS'
        _Caculation_Parameters['_MosUpDn'] = 'Up'

        _Caculation_Parameters['_NumberofGate'] = _Tr11_NumberofGate
        _Caculation_Parameters['_ChannelWidth'] = _Tr11_ChannelWidth
        _Caculation_Parameters['_ChannelLength'] = _Tr11_ChannelLength
        _Caculation_Parameters['_GateSpacing'] = None
        _Caculation_Parameters['_SDWidth'] = None
        _Caculation_Parameters['_XVT'] = _Tr11_XVT
        _Caculation_Parameters['_PCCrit'] = None

        _Caculation_Parameters['_Source_Via_TF'] = True
        _Caculation_Parameters['_Source_Via_Close2POpin_TF'] = True
        _Caculation_Parameters['_Source_Comb_TF'] = True
        _Caculation_Parameters['_Source_Comb_POpinward_TF'] = True
        _Caculation_Parameters['_Source_Comb_Length'] = None

        _Caculation_Parameters['_Drain_Via_TF'] = False
        _Caculation_Parameters['_Drain_Via_Close2POpin_TF'] = None
        _Caculation_Parameters['_Drain_Comb_TF'] = None
        _Caculation_Parameters['_Drain_Comb_POpinward_TF'] = None
        _Caculation_Parameters['_Drain_Comb_Length'] = None

        _Caculation_Parameters['_PODummy_TF'] = True
        _Caculation_Parameters['_PODummy_Length'] = None
        _Caculation_Parameters['_PODummy_Placement'] = 'Up'

        _Caculation_Parameters['_Xvt_MinExten_TF'] = True
        _Caculation_Parameters['_Xvt_Placement'] = 'Dn'

        _Caculation_Parameters['_POGate_Comb_TF'] = True
        _Caculation_Parameters['_POGate_Comb_length'] = 200
        _Caculation_Parameters['_POGate_Via_TF'] = True
        _Caculation_Parameters['_POGate_ViaMxMx'] = [0, 2]

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Pmos'] = self._SrefElementDeclaration(_DesignObj=A14_Mosfet_KJH3._Mosfet(_DesignParameter=None, _Name='{}:SRF_Pmos'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Pmos']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos']['_XYCoordinates'] = [[0, 0]]


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Source: M4
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Source: M4 metal Gen.
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Source_Hrz_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('SRF_Pmos','BND_Source_Hrz_M2')
        self._DesignParameter['BND_Source_Hrz_M3']['_YWidth'] = tmp[0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Pmos','BND_Source_Hrz_M2')
        self._DesignParameter['BND_Source_Hrz_M3']['_XWidth'] = tmp[0][0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Source_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Source_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_Pmos','BND_Source_Hrz_M2')
        target_coord = tmp1[0][0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Source_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Source_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_Source_Hrz_M3']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Source: ViaM2M3 Gen.
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

            ## Sref ViaX declaration
        self._DesignParameter['SRF_Source_ViaM2M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Source_ViaM2M3'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_Source_ViaM2M3']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_Source_ViaM2M3']['_Angle'] = 0

            ## Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH4('BND_Source_Hrz_M3')
        tmp2 = self.get_param_KJH4('SRF_Pmos','BND_Source_Hrz_M2')
        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0][0])

            ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

            ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = max(2,_COX)
        _Caculation_Parameters['_COY'] = max(1,_COY)

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Source_ViaM2M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_Source_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        tmp1 = self.get_param_KJH4('BND_Source_Hrz_M3')
        target_coord = tmp1[0][0]['_XY_cent']
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Source_ViaM2M3','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Source_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_Source_ViaM2M3']['_XYCoordinates'] = tmpXY


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
    libname = 'Proj_ZZ01_C08_00_Tr11_Fixed'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'C08_00_Tr11_v0_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
# TR11
    # Physical dimension
    _Tr11_NumberofGate	            = 1,       # Number
    _Tr11_ChannelWidth	            = 500,     # Number
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
    LayoutObj = _Tr11(_DesignParameter=None, _Name=cellname)
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
    # Checker.lib_deletion()
    Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()

    print('#############################      Finished      ################################')
    print('{} Hours   {} minutes   {} seconds'.format(h, m, s))

# end of 'main():' ---------------------------------------------------------------------------------------------
