
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



## Define Class
class _FingerPair(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(

    _Length = None,
    _LayoutOption = None,

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

    _Length = None,
    _LayoutOption = None,

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


        for i in _LayoutOption:
            ## Port A
                # Define Boundary_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_PortA_METAL{}'.format(i)] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}'.format(i)][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}'.format(i)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
            )
                # Define Boundary_element _YWidth
            self._DesignParameter['BND_PortA_METAL{}'.format(i)]['_YWidth'] = _Length - _DRCobj._PortABZigzag

                # Define Boundary_element _XWidth
            self._DesignParameter['BND_PortA_METAL{}'.format(i)]['_XWidth'] = 50

                # Define Boundary_element _XYCoordinates: down left
            self._DesignParameter['BND_PortA_METAL{}'.format(i)]['_XYCoordinates'] = [[0,0]]

            ## Port B
                # Define Boundary_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_PortB_METAL{}'.format(i)] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}'.format(i)][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}'.format(i)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
            )
                # Define Boundary_element _YWidth
            self._DesignParameter['BND_PortB_METAL{}'.format(i)]['_YWidth'] = _Length - _DRCobj._PortABZigzag

                # Define Boundary_element _XWidth
            self._DesignParameter['BND_PortB_METAL{}'.format(i)]['_XWidth'] = 50

                # Define Boundary_element _XYCoordinates: down left
            self._DesignParameter['BND_PortB_METAL{}'.format(i)]['_XYCoordinates'] = [[0,0]]

                    ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['BND_PortB_METAL{}'.format(i)]['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('BND_PortA_METAL{}'.format(i))
            target_coord = tmp1[0][0]['_XY_down_right']
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_PortB_METAL{}'.format(i))
            approaching_coord = tmp2[0][0]['_XY_down_left']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('BND_PortB_METAL{}'.format(i))
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[0] = New_Scoord[0] + _DRCobj._PortABSpace
            New_Scoord[1] = New_Scoord[1] - _DRCobj._PortABZigzag
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['BND_PortB_METAL{}'.format(i)]['_XYCoordinates'] = tmpXY



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
    libname = 'Proj_ZZ01_C01_00_FingerPair'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'C01_00_FingerPair_v0_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

    _Length = 5000,
    _LayoutOption = [1, 2, 3],

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
    LayoutObj = _FingerPair(_DesignParameter=None, _Name=cellname)
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
