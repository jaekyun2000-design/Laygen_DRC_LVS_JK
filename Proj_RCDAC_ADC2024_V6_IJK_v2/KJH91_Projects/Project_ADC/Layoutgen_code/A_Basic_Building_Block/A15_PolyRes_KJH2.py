from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_ADC.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

import numpy as np
import copy
import math
#from SthPack import CoordCalc

from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3


## ########################################################################################################################################################## Class_HEADER
class _PolyRes_KJH(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

_ResWidth	=	2500,
_ResLength	=	1500,
_CONUMX		=	None,
_CONUMY		=	None,

                                        )

    ## Initially Defined design_parameter
    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                                            _Name=self._NameDeclaration(_Name=_Name),
                                            _GDSFile=self._GDSObjDeclaration(_GDSFile=None),_XYcoordAsCent=dict(_XYcoordAsCent=0),
                                        )

    ## ################################################################################################################################################ _CalculateDesignParameter
    def _CalculateDesignParameter(self,

_ResWidth	=	2500,
_ResLength	=	1500,
_CONUMX		=	None,
_CONUMY		=	None,

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

            ## ################################################################################################################### Pre-defined
        #Cent coordinates
        _XYCoordinateOfOP = [[0,0]]

            ## ################################################################################################################### OPLayer
        #Define Boundary_element
        self._DesignParameter['BND_OPLayer'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['OP'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['OP'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Not implemented condition
        if _ResLength < _DRCObj._PolyoverOPlayer :
            raise NotImplementedError

        #Define Boundary_element _YWidth
        self._DesignParameter['BND_OPLayer']['_YWidth'] = _ResLength

        #Define Boundary_element _XWidth
        self._DesignParameter['BND_OPLayer']['_XWidth'] = _ResWidth + _DRCObj._OPlayeroverPoly * 2

        #Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_OPLayer']['_XYCoordinates'] = _XYCoordinateOfOP


            ## ################################################################################################################### POLY Layer
        #Define Boundary_element
        self._DesignParameter['BND_POLayer'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Define Boundary_element _YWidth
        self._DesignParameter['BND_POLayer']['_YWidth'] = _ResLength + _DRCObj._PolyoverOPlayer * 2

        #Define Boundary_element _XWidth
        self._DesignParameter['BND_POLayer']['_XWidth'] = _ResWidth

        self._DesignParameter['BND_POLayer']['_XYCoordinates'] =  [[0,0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_POLayer']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_OPLayer')
        target_coord = tmp1[0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_POLayer')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_POLayer')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        New_Scoord[0] = New_Scoord[0] + _DRCObj._OPlayeroverPoly
        New_Scoord[1] = New_Scoord[1] - _DRCObj._PolyoverOPlayer
                    ## Define Coordinates
        self._DesignParameter['BND_POLayer']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### PRES Layer
        #Define Boundary_element
        self._DesignParameter['BND_PRESLayer'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['PRES'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['PRES'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('BND_POLayer')
        self._DesignParameter['BND_PRESLayer']['_YWidth'] = tmp[0][0]['_Ywidth'] + _DRCObj._PRESlayeroverPoly * 2

        #Define Boundary_element _XWidth
        self._DesignParameter['BND_PRESLayer']['_XWidth'] = _ResWidth + _DRCObj._PRESlayeroverPoly * 2

        #Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PRESLayer']['_XYCoordinates'] =  [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_PRESLayer']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                ## x
        tmp1_1 = self.get_param_KJH4('BND_POLayer')
        target_coordx = tmp1_1[0][0]['_XY_left'][0]
                                ## y
        tmp1_2 = self.get_param_KJH4('BND_POLayer')
        target_coordy = tmp1_2[0][0]['_XY_down'][1]

        target_coord=[target_coordx,target_coordy]

                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PRESLayer')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PRESLayer')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        New_Scoord[0] = New_Scoord[0] - _DRCObj._PRESlayeroverPoly
        New_Scoord[1] = New_Scoord[1] - _DRCObj._PRESlayeroverPoly
                    ## Define Coordinates
        self._DesignParameter['BND_PRESLayer']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### PIMP Layer
        #Define Boundary_element
        self._DesignParameter['BND_PPLayer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                               )

        #Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('BND_PRESLayer')
        self._DesignParameter['BND_PPLayer']['_YWidth'] = tmp[0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('BND_PRESLayer')
        self._DesignParameter['BND_PPLayer']['_XWidth'] = tmp[0][0]['_Xwidth']

        #Define Boundary_element _XYCoordinates
        tmp = self.get_param_KJH4('BND_PRESLayer')
        self._DesignParameter['BND_PPLayer']['_XYCoordinates'] =  [tmp[0][0]['_XY_origin']]

        ## ################################################################################################################### CONT Layer
        ## Pre-defined
        Op_to_M1_distance = 188

        #Calculate Num of CONT
            #Number of Contact
                #MaxnNum of Contact
        _CONUMXmax = int((self._DesignParameter['BND_POLayer']['_XWidth'] - _DRCObj._CoMinEnclosureByPO2 * 2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 1
        _CONUMYmax = int((int((self._DesignParameter['BND_POLayer']['_YWidth'] - self._DesignParameter['BND_OPLayer']['_YWidth'] - 2*_DRCObj._CoMinSpace2OP - 2*_DRCObj._CoMinEnclosureByPO2) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)) + 1) // 2)

                #Default num of contact
        if _CONUMX == None :
            _CONUMX = _CONUMXmax
        if _CONUMY == None :
            _CONUMY = _CONUMYmax

                #If _CONUMY > 1 then, _CONUMX is defined
        if _CONUMY > 1 :
            _CONUMX = int((self._DesignParameter['BND_POLayer']['_XWidth'] - _DRCObj._CoMinEnclosureByPO2 * 2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)) + 1

                #Not implemented
        if _CONUMX > _CONUMXmax or _CONUMY > _CONUMYmax :
            raise NotImplementedError

        ## ######################################################################################################### CONT Layer: PinA ViaM0M1
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 0
        _Caculation_Parameters['_Layer2'] = 1
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

            ## Sref ViaX declaration
        self._DesignParameter['SRF_PinA_ViaM0M1'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_PinA_ViaM0M1'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_PinA_ViaM0M1']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_PinA_ViaM0M1']['_Angle'] = 0

            ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _CONUMX
        _Caculation_Parameters['_COY'] = _CONUMY

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_PinA_ViaM0M1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_PinA_ViaM0M1']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        tmp1 = self.get_param_KJH4('BND_OPLayer')
        target_coord = tmp1[0][0]['_XY_up']
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_PinA_ViaM0M1','SRF_ViaM0M1','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_PinA_ViaM0M1')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[1] = New_Scoord[1] + Op_to_M1_distance
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_PinA_ViaM0M1']['_XYCoordinates'] = tmpXY

        ## ######################################################################################################### CONT Layer: PinB ViaM0M1
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 0
        _Caculation_Parameters['_Layer2'] = 1
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

            ## Sref ViaX declaration
        self._DesignParameter['SRF_PinB_ViaM0M1'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_PinB_ViaM0M1'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_PinB_ViaM0M1']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_PinB_ViaM0M1']['_Angle'] = 0

            ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _CONUMX
        _Caculation_Parameters['_COY'] = _CONUMY

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_PinB_ViaM0M1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_PinB_ViaM0M1']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        tmp1 = self.get_param_KJH4('BND_OPLayer')
        target_coord = tmp1[0][0]['_XY_down']
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_PinB_ViaM0M1','SRF_ViaM0M1','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_PinB_ViaM0M1')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[1] = New_Scoord[1] - Op_to_M1_distance
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_PinB_ViaM0M1']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### PinA M1
        #Define Boundary_element
        self._DesignParameter['BND_PinA_M1'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                               )

        #Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('SRF_PinA_ViaM0M1','SRF_ViaM0M1','BND_Met1Layer')
        self._DesignParameter['BND_PinA_M1']['_YWidth'] = tmp[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        self._DesignParameter['BND_PinA_M1']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

        #Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PinA_M1']['_XYCoordinates'] =  [tmp[0][0][0][0]['_XY_origin']]

            ## ################################################################################################################### PinB M1
        #Define Boundary_element
        self._DesignParameter['BND_PinB_M1'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                               )

        #Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('SRF_PinB_ViaM0M1','SRF_ViaM0M1','BND_Met1Layer')
        self._DesignParameter['BND_PinB_M1']['_YWidth'] = tmp[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        self._DesignParameter['BND_PinB_M1']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

        #Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PinB_M1']['_XYCoordinates'] =  [tmp[0][0][0][0]['_XY_origin']]

        ## ################################################################################################################################# Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')

## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_ZZ01_A15_PolyResKJH2'
    cellname = 'A15_PolyRes_KJH2_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

_ResWidth	=	1300,
_ResLength	=	1500,
_CONUMX		=	None,
_CONUMY		=	None,

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
    LayoutObj = _PolyRes_KJH(_DesignParameter=None, _Name=cellname)
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
    # Checker.lib_deletion()
    Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()
    print('#############################      Finished      ################################')
    # end of 'main():' ---------------------------------------------------------------------------------------------




