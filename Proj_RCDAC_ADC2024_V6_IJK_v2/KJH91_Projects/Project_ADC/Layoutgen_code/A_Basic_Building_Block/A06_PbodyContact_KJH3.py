from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Library_and_Engine import DesignParameters
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Library_and_Engine import DRC

import numpy as np
import copy
import math

## ########################################################################################################################################################## Class_HEADER
class _PbodyContact(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

_COX	= None,
_COY	= None,

                                        )

    ## Initially Defined design_parameter
    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                                            _Name=self._NameDeclaration(_Name=_Name),
                                            _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                                            _XYcoordAsCent=dict(_XYcoordAsCent=0),
                                        )

    ## ################################################################################################################################################ _CalculateDesignParameter
    def _CalculateDesignParameter(self,

_COX	= None,
_COY	= None,

                                  ):

        ## ################################################################################################################################# Class_HEADER: Pre Defined Parameter Before Calculation
        # Load DRC library
        _DRCObj = DRC.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']


        ## ################################################################################################################################# Calculation_Start
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

        ##  Pre-defined: Coordination
        _XYOrigin = [[0, 0]]

            ## ################################################################################################################### CONT_Layer
        #Define Boundary_element
        self._DesignParameter['BND_COLayer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['CONT'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['CONT'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                               )

        #Define Boundary_element _YWidth
        self._DesignParameter['BND_COLayer']['_YWidth'] = _DRCObj._CoMinWidth

        #Define Boundary_element _XWidth
        self._DesignParameter['BND_COLayer']['_XWidth'] = _DRCObj._CoMinWidth

        #Define XYcoord.
            #Define Distance between CONT
        _LengthNbodyBtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_COX,NumOfCOY=_COY )

        # Define Boundary_element Coordinates
        # Initialized coordinate
        self._DesignParameter['BND_COLayer']['_XYCoordinates'] = _XYOrigin
        tmp = []
        for i in range(0, _COY):
            for j in range(0, _COX):
                if j == 0:
                    if i == 0:
                        _xycoordinatetmp = [0, 0]
                    else:
                        refcoord = _xycoordinatetmp - (_COX -1 ) * np.array([_LengthNbodyBtwCO, 0])
                        _xycoordinatetmp = np.array(refcoord) - np.array([0, _LengthNbodyBtwCO])
                else:
                    refcoord = _xycoordinatetmp
                    _xycoordinatetmp = np.array(refcoord) + np.array([_LengthNbodyBtwCO, 0])
                tmp.append(_xycoordinatetmp)
                self._DesignParameter['BND_COLayer']['_XYCoordinates'] = tmp
                # Define coordinates
        self._DesignParameter['BND_COLayer']['_XYCoordinates'] = tmp

            ## ################################################################################################################### DIFF(OD/RX)_Dummy_Layer
        #Define Boundary_element
        self._DesignParameter['BND_ODLayer'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Calculate _LengthNbodyBtwCO for Ywidth and Xwidth
        _LengthNbodyBtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_COX,NumOfCOY=_COY )

        #Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('BND_COLayer')
        _Via_YWidth = abs(tmp[0][0]['_XY_up'][1] - tmp[-1][0]['_XY_down'][1])
        self._DesignParameter['BND_ODLayer']['_YWidth'] = _Via_YWidth + 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide

        #Define Boundary_element _XWidth
        _Via_XWidth = abs(tmp[-1][0]['_XY_right'][0] - tmp[0][0]['_XY_left'][0])
        self._DesignParameter['BND_ODLayer']['_XWidth'] = _Via_XWidth + 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide

        #Define XYcoord.
        self._DesignParameter['BND_ODLayer']['_XYCoordinates'] = [[0, 0]]

        ## Get_Scoord_v4.
            ## Calculate Sref XYcoord
        tmpXY = []
            ## initialized Sref coordinate
        self._DesignParameter['BND_ODLayer']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
                ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_COLayer')
        target_coord = tmp1[0][0]['_XY_up_left']
                ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_ODLayer')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                ## Sref coord
        tmp3 = self.get_param_KJH4('BND_ODLayer')
        Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] - _DRCObj._CoMinEnclosureByODAtLeastTwoSide
        New_Scoord[1] = New_Scoord[1] + _DRCObj._CoMinEnclosureByODAtLeastTwoSide

        tmpXY.append(New_Scoord)
        ## Define Coordinates
        self._DesignParameter['BND_ODLayer']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### PIMP_Layer
        # Define Boundary_element
        self._DesignParameter['BND_PPLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_PPLayer']['_YWidth'] = self._DesignParameter['BND_ODLayer']['_YWidth'] + 2 * _DRCObj._PpMinExtensiononPactive2

        if self._DesignParameter['BND_PPLayer']['_YWidth'] < 170:
            self._DesignParameter['BND_PPLayer']['_YWidth'] = self._DesignParameter['BND_ODLayer']['_YWidth'] + 2 * _DRCObj._PpMinExtensiononPactive2 + 28

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_PPLayer']['_XWidth'] = self._DesignParameter['BND_ODLayer']['_XWidth'] + 2 * _DRCObj._PpMinExtensiononPactive2

        # Define XYcoord.
        self._DesignParameter['BND_PPLayer']['_XYCoordinates'] = self._DesignParameter['BND_ODLayer']['_XYCoordinates']

        ## Get_Scoord_v4.
            ## Calculate Sref XYcoord
        tmpXY = []
            ## initialized Sref coordinate
        self._DesignParameter['BND_PPLayer']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
                ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_ODLayer')
        target_coord = tmp1[0][0]['_XY_up_left']
                ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PPLayer')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PPLayer')
        Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] - _DRCObj._PpMinExtensiononPactive2
        New_Scoord[1] = New_Scoord[1] + _DRCObj._PpMinExtensiononPactive2
        if self._DesignParameter['BND_PPLayer']['_YWidth'] < 170:
            New_Scoord[1] = New_Scoord[1] + ( _DRCObj._PpMinExtensiononPactive2 + 14)

        tmpXY.append(New_Scoord)
        ## Define Coordinates
        self._DesignParameter['BND_PPLayer']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### METAL1_Layer
        #Define Boundary_element
        self._DesignParameter['BND_Met1Layer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                               )

        #Define Boundary_element _YWidth
        self._DesignParameter['BND_Met1Layer']['_YWidth'] = self._DesignParameter['BND_ODLayer']['_YWidth']

        #Define Boundary_element _XWidth
        self._DesignParameter['BND_Met1Layer']['_XWidth'] = self._DesignParameter['BND_ODLayer']['_XWidth']

        #Define XYcoord.
        self._DesignParameter['BND_Met1Layer']['_XYCoordinates'] = self._DesignParameter['BND_ODLayer']['_XYCoordinates']


        ## ################################################################################################################################# Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')

## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_ADC_A_building_block_KJH'
    cellname = 'A06_PbodyContact_KJH2_98'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

_COX=30,
_COY=2,


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
    LayoutObj = _PbodyContact(_DesignParameter=None, _Name=cellname)
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
    #Checker.lib_deletion()
    Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()
    print('#############################      Finished      ################################')
    print('####### I am not Babo ########')
    # end of 'main():' ---------------------------------------------------------------------------------------------




