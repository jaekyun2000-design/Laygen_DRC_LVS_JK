from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC_EGFET

import numpy as np
import copy
import math

from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A08_PbodyContactPhyLen_KJH3

## ########################################################################################################################################################## Class_HEADER
class _PbodyRing(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(
_XlengthIntn		= None,
_YlengthIntn		= None,
_NumContTop			= None,
_NumContBottom		= None,
_NumContLeft		= None,
_NumContRight		= None,

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
                                    _XlengthIntn		= None,
                                    _YlengthIntn		= None,
                                    _NumContTop			= None,
                                    _NumContBottom		= None,
                                    _NumContLeft		= None,
                                    _NumContRight		= None,
                                  ):

        ## ################################################################################################################################# Class_HEADER: Pre Defined Parameter Before Calculation
        # Load DRC library
        _DRCObj = DRC_EGFET.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']


        ## ################################################################################################################################# Calculation_Start
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

            ## ################################################################################################################### Pbody:Top
        #Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length']  		=  _XlengthIntn
        _Caculation_Parameters['_NumCont']  	=  _NumContTop
        _Caculation_Parameters['_Vtc_flag']  	=  False

        #Generate Sref
        self._DesignParameter['SRF_PbodyTop'] = self._SrefElementDeclaration(_DesignObj=A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen( _DesignParameter=None, _Name='{}:SRF_PbodyTop'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['SRF_PbodyTop']['_Reflect'] = [0, 0, 0]
        
        #Define Sref Angle
        self._DesignParameter['SRF_PbodyTop']['_Angle'] = 0

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_PbodyTop']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['SRF_PbodyTop']['_XYCoordinates']=[[0, 0]]


            ## ################################################################################################################### Pbody:Bottom
        #Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length']  		=  _XlengthIntn
        _Caculation_Parameters['_NumCont']  	=  _NumContBottom
        _Caculation_Parameters['_Vtc_flag']  	=  False

        #Generate Sref
        self._DesignParameter['SRF_PbodyBottom'] = self._SrefElementDeclaration(_DesignObj=A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen( _DesignParameter=None, _Name='{}:SRF_PbodyBottom'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['SRF_PbodyBottom']['_Reflect'] = [0, 0, 0]
        
        #Define Sref Angle
        self._DesignParameter['SRF_PbodyBottom']['_Angle'] = 0

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_PbodyBottom']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['SRF_PbodyBottom']['_XYCoordinates']=[[0, 0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['SRF_PbodyBottom']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH4('SRF_PbodyTop','SRF_PbodyContactPhyLen','BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_down']
                #Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_PbodyBottom','SRF_PbodyContactPhyLen','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                #Sref coord
        tmp3 = self.get_param_KJH4('SRF_PbodyBottom')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)
        New_Scoord[1] = New_Scoord[1] - _YlengthIntn
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['SRF_PbodyBottom']['_XYCoordinates'] = tmpXY


            ## ################################################################################################################### Pbody:Left
        #Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy( A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length']  		=  _YlengthIntn
        _Caculation_Parameters['_NumCont']  	=  _NumContLeft
        _Caculation_Parameters['_Vtc_flag']  	=  True

        #Generate Sref
        self._DesignParameter['SRF_PbodyLeft'] = self._SrefElementDeclaration(_DesignObj=A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen( _DesignParameter=None, _Name='{}:SRF_PbodyLeft'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['SRF_PbodyLeft']['_Reflect'] = [0, 0, 0]
        
        #Define Sref Angle
        self._DesignParameter['SRF_PbodyLeft']['_Angle'] = 0

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_PbodyLeft']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['SRF_PbodyLeft']['_XYCoordinates']=[[0, 0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['SRF_PbodyLeft']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH4('SRF_PbodyTop','SRF_PbodyContactPhyLen','BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_PbodyLeft','SRF_PbodyContactPhyLen','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_right']
                #Sref coord
        tmp3 = self.get_param_KJH4('SRF_PbodyLeft')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['SRF_PbodyLeft']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### Pbody:Right
        #Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy( A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length']  		=  _YlengthIntn
        _Caculation_Parameters['_NumCont']  	=  _NumContRight
        _Caculation_Parameters['_Vtc_flag']  	=  True

        #Generate Sref
        self._DesignParameter['SRF_PbodyRight'] = self._SrefElementDeclaration(_DesignObj=A08_PbodyContactPhyLen_KJH3._PbodyContactPhyLen( _DesignParameter=None, _Name='{}:SRF_PbodyRight'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['SRF_PbodyRight']['_Reflect'] = [0, 0, 0]
        
        #Define Sref Angle
        self._DesignParameter['SRF_PbodyRight']['_Angle'] = 0

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_PbodyRight']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['SRF_PbodyRight']['_XYCoordinates']=[[0, 0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['SRF_PbodyRight']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH4('SRF_PbodyTop','SRF_PbodyContactPhyLen','BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_down_right']
                #Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_PbodyRight','SRF_PbodyContactPhyLen','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH4('SRF_PbodyRight')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['SRF_PbodyRight']['_XYCoordinates'] = tmpXY


            ## ################################################################################################################### Extension:Top
                ## ##################################################################################################### Extension:Top:OD
        #Define Boundary_element
        self._DesignParameter['BND_ExtenODLayer_Top'] = self._BoundaryElementDeclaration(
                                                                            _Layer=
                                                                            DesignParameters._LayerMapping['DIFF'][0],
                                                                            _Datatype=
                                                                            DesignParameters._LayerMapping['DIFF'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_PbodyTop','SRF_PbodyContactPhyLen','BND_ODLayer')
        self._DesignParameter['BND_ExtenODLayer_Top']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH4('SRF_PbodyLeft','SRF_PbodyContactPhyLen','BND_ODLayer')
        tmp3 = self.get_param_KJH4('SRF_PbodyRight','SRF_PbodyContactPhyLen','BND_ODLayer')
        self._DesignParameter['BND_ExtenODLayer_Top']['_XWidth'] = abs( tmp3[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0] )

        # Define Sref _XYcoordinate
        self._DesignParameter['BND_ExtenODLayer_Top']['_XYCoordinates'] = [[0,0]]


        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['BND_ExtenODLayer_Top']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH4('SRF_PbodyLeft','SRF_PbodyContactPhyLen','BND_ODLayer')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ExtenODLayer_Top')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                #Sref coord
        tmp3 = self.get_param_KJH4('BND_ExtenODLayer_Top')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['BND_ExtenODLayer_Top']['_XYCoordinates'] = tmpXY

        
                ## ##################################################################################################### Extension:Top:M1
        #Define Boundary_element
        self._DesignParameter['BND_ExtenMet1Layer_Top'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[ ],
                                                                                   )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_PbodyTop','SRF_PbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_ExtenMet1Layer_Top']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH4('SRF_PbodyLeft','SRF_PbodyContactPhyLen','BND_Met1Layer')
        tmp3 = self.get_param_KJH4('SRF_PbodyRight','SRF_PbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_ExtenMet1Layer_Top']['_XWidth'] = abs( tmp3[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0] )
            
        # Define Sref _XYcoordinate
        self._DesignParameter['BND_ExtenMet1Layer_Top']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['BND_ExtenMet1Layer_Top']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH4('SRF_PbodyLeft','SRF_PbodyContactPhyLen','BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ExtenMet1Layer_Top')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                #Sref coord
        tmp3 = self.get_param_KJH4('BND_ExtenMet1Layer_Top')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['BND_ExtenMet1Layer_Top']['_XYCoordinates'] = tmpXY

        
                ## ##################################################################################################### Extension:Top:PP
        #Define Boundary_element
        self._DesignParameter['BND_ExtenPPLayer_Top'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[ ],
                                                                                           )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_PbodyTop','SRF_PbodyContactPhyLen','BND_PPLayer')
        self._DesignParameter['BND_ExtenPPLayer_Top']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH4('SRF_PbodyLeft','SRF_PbodyContactPhyLen','BND_PPLayer')
        tmp3 = self.get_param_KJH4('SRF_PbodyRight','SRF_PbodyContactPhyLen','BND_PPLayer')
        self._DesignParameter['BND_ExtenPPLayer_Top']['_XWidth']= abs( tmp3[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0] )

        # Define Sref _XYcoordinate
        self._DesignParameter['BND_ExtenPPLayer_Top']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['BND_ExtenPPLayer_Top']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #Xcoord
        tmp1_1 = self.get_param_KJH4('SRF_PbodyLeft','SRF_PbodyContactPhyLen','BND_PPLayer')
        target_coordx = tmp1_1[0][0][0][0]['_XY_left'][0]
                    #Ycoord
        tmp1_2 = self.get_param_KJH4('SRF_PbodyTop','SRF_PbodyContactPhyLen','BND_PPLayer')
        target_coordy = tmp1_2[0][0][0][0]['_XY_up'][1]

        target_coord = [target_coordx, target_coordy]
                #Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ExtenPPLayer_Top')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH4('BND_ExtenPPLayer_Top')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)

        #tmp4 = self.get_param_KJH4('SRF_PbodyTop','SRF_PbodyContactPhyLen','BND_PPLayer')
        #New_Scoord[1] = tmp4[0][0][0][0]['_XY_cent'][1]
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['BND_ExtenPPLayer_Top']['_XYCoordinates'] = tmpXY

        
            ## ################################################################################################################### Extension:Bottom
                ## ##################################################################################################### Extension:Bottom:OD
        #Define Boundary_element
        self._DesignParameter['BND_ExtenODLayer_Bottom'] = self._BoundaryElementDeclaration(
                                                                            _Layer=
                                                                            DesignParameters._LayerMapping['DIFF'][0],
                                                                            _Datatype=
                                                                            DesignParameters._LayerMapping['DIFF'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_PbodyBottom','SRF_PbodyContactPhyLen','BND_ODLayer')
        self._DesignParameter['BND_ExtenODLayer_Bottom']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH4('SRF_PbodyLeft','SRF_PbodyContactPhyLen','BND_ODLayer')
        tmp3 = self.get_param_KJH4('SRF_PbodyRight','SRF_PbodyContactPhyLen','BND_ODLayer')
        self._DesignParameter['BND_ExtenODLayer_Bottom']['_XWidth'] = abs( tmp3[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0] )

        # Define Sref _XYcoordinate
        self._DesignParameter['BND_ExtenODLayer_Bottom']['_XYCoordinates'] = [[0,0]]


        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['BND_ExtenODLayer_Bottom']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH4('SRF_PbodyLeft','SRF_PbodyContactPhyLen','BND_ODLayer')
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ExtenODLayer_Bottom')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH4('BND_ExtenODLayer_Bottom')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['BND_ExtenODLayer_Bottom']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### Extension:Bottom:M1
        #Define Boundary_element
        self._DesignParameter['BND_ExtenMet1Layer_Bottom'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[ ],
                                                                                   )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_PbodyBottom','SRF_PbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_ExtenMet1Layer_Bottom']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH4('SRF_PbodyLeft','SRF_PbodyContactPhyLen','BND_Met1Layer')
        tmp3 = self.get_param_KJH4('SRF_PbodyRight','SRF_PbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_ExtenMet1Layer_Bottom']['_XWidth']= abs( tmp3[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0] )

        # Define Sref _XYcoordinate
        self._DesignParameter['BND_ExtenMet1Layer_Bottom']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['BND_ExtenMet1Layer_Bottom']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH4('SRF_PbodyLeft','SRF_PbodyContactPhyLen','BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ExtenMet1Layer_Bottom')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH4('BND_ExtenMet1Layer_Bottom')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['BND_ExtenMet1Layer_Bottom']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### Extension:Bottom:PP
        #Define Boundary_element
        self._DesignParameter['BND_ExtenPPLayer_Bottom'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[ ],
                                                                                           )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_PbodyBottom','SRF_PbodyContactPhyLen','BND_PPLayer')
        self._DesignParameter['BND_ExtenPPLayer_Bottom']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH4('SRF_PbodyLeft','SRF_PbodyContactPhyLen','BND_PPLayer')
        tmp3 = self.get_param_KJH4('SRF_PbodyRight','SRF_PbodyContactPhyLen','BND_PPLayer')
        self._DesignParameter['BND_ExtenPPLayer_Bottom']['_XWidth']= abs( tmp3[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0] )

        # Define Sref _XYcoordinate
        self._DesignParameter['BND_ExtenPPLayer_Bottom']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['BND_ExtenPPLayer_Bottom']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #Xcoord
        tmp1_1 = self.get_param_KJH4('SRF_PbodyLeft','SRF_PbodyContactPhyLen','BND_PPLayer')
        target_coordx = tmp1_1[0][0][0][0]['_XY_left'][0]
                    #Ycoord
        tmp1_2 = self.get_param_KJH4('SRF_PbodyBottom','SRF_PbodyContactPhyLen','BND_PPLayer')
        target_coordy = tmp1_2[0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                #Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ExtenPPLayer_Bottom')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                #Sref coord
        tmp3 = self.get_param_KJH4('BND_ExtenPPLayer_Bottom')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)

        #tmp4 = self.get_param_KJH4('SRF_PbodyBottom','SRF_PbodyContactPhyLen','BND_PPLayer')
        #New_Scoord[1] = tmp4[0][0][0][0]['_XY_cent'][1]
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['BND_ExtenPPLayer_Bottom']['_XYCoordinates'] = tmpXY

        
            ## ################################################################################################################### Extension:Left
                ## ##################################################################################################### Extension:Left:OD
        #Define Boundary_element
        self._DesignParameter['BND_ExtenODLayer_Left'] = self._BoundaryElementDeclaration(
                                                                            _Layer=
                                                                            DesignParameters._LayerMapping['DIFF'][0],
                                                                            _Datatype=
                                                                            DesignParameters._LayerMapping['DIFF'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_PbodyTop','SRF_PbodyContactPhyLen','BND_ODLayer')
        tmp2 = self.get_param_KJH4('SRF_PbodyBottom','SRF_PbodyContactPhyLen','BND_ODLayer')
        self._DesignParameter['BND_ExtenODLayer_Left']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] )

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH4('SRF_PbodyLeft','SRF_PbodyContactPhyLen','BND_ODLayer')
        self._DesignParameter['BND_ExtenODLayer_Left']['_XWidth'] = tmp3[0][0][0][0]['_Xwidth']

        # Define Sref _XYcoordinate
        self._DesignParameter['BND_ExtenODLayer_Left']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['BND_ExtenODLayer_Left']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH4('SRF_PbodyTop','SRF_PbodyContactPhyLen','BND_ODLayer')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ExtenODLayer_Left')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                #Sref coord
        tmp3 = self.get_param_KJH4('BND_ExtenODLayer_Left')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['BND_ExtenODLayer_Left']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### Extension:Left:M1
        #Define Boundary_element
        self._DesignParameter['BND_ExtenMet1Layer_Left'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[ ],
                                                                                   )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_PbodyTop','SRF_PbodyContactPhyLen','BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_PbodyBottom','SRF_PbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_ExtenMet1Layer_Left']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] )

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH4('SRF_PbodyLeft','SRF_PbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_ExtenMet1Layer_Left']['_XWidth']= tmp3[0][0][0][0]['_Xwidth']

        # Define Sref _XYcoordinate
        self._DesignParameter['BND_ExtenMet1Layer_Left']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['BND_ExtenMet1Layer_Left']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH4('SRF_PbodyTop','SRF_PbodyContactPhyLen','BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ExtenMet1Layer_Left')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                #Sref coord
        tmp3 = self.get_param_KJH4('BND_ExtenMet1Layer_Left')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['BND_ExtenMet1Layer_Left']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### Extension:Left:PP
        #Define Boundary_element
        self._DesignParameter['BND_ExtenPPLayer_Left'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[ ],
                                                                                           )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_PbodyTop','SRF_PbodyContactPhyLen','BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_PbodyBottom','SRF_PbodyContactPhyLen','BND_PPLayer')
        self._DesignParameter['BND_ExtenPPLayer_Left']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] )

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH4('SRF_PbodyLeft','SRF_PbodyContactPhyLen','BND_PPLayer')
        self._DesignParameter['BND_ExtenPPLayer_Left']['_XWidth']= tmp3[0][0][0][0]['_Xwidth']

        # Define Sref _XYcoordinate
        self._DesignParameter['BND_ExtenPPLayer_Left']['_XYCoordinates'] = [[0,0]]


        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['BND_ExtenPPLayer_Left']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #Xcoord
        tmp1_1 = self.get_param_KJH4('BND_ExtenPPLayer_Top')
        target_coord = tmp1_1[0][0]['_XY_up_left']

                #Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ExtenPPLayer_Left')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH4('BND_ExtenPPLayer_Left')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['BND_ExtenPPLayer_Left']['_XYCoordinates'] = tmpXY

        
            ## ################################################################################################################### Extension:Right
                ## ##################################################################################################### Extension:Right:OD
        #Define Boundary_element
        self._DesignParameter['BND_ExtenODLayer_Right'] = self._BoundaryElementDeclaration(
                                                                            _Layer=
                                                                            DesignParameters._LayerMapping['DIFF'][0],
                                                                            _Datatype=
                                                                            DesignParameters._LayerMapping['DIFF'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_PbodyTop','SRF_PbodyContactPhyLen','BND_ODLayer')
        tmp2 = self.get_param_KJH4('SRF_PbodyBottom','SRF_PbodyContactPhyLen','BND_ODLayer')
        self._DesignParameter['BND_ExtenODLayer_Right']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] )

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH4('SRF_PbodyRight','SRF_PbodyContactPhyLen','BND_ODLayer')
        self._DesignParameter['BND_ExtenODLayer_Right']['_XWidth'] = tmp3[0][0][0][0]['_Xwidth']

        # Define Sref _XYcoordinate
        self._DesignParameter['BND_ExtenODLayer_Right']['_XYCoordinates'] = [[0,0]]


        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['BND_ExtenODLayer_Right']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH4('SRF_PbodyTop','SRF_PbodyContactPhyLen','BND_ODLayer')
        target_coord = tmp1[0][0][0][0]['_XY_up_right']
                #Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ExtenODLayer_Right')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH4('BND_ExtenODLayer_Right')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['BND_ExtenODLayer_Right']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### Extension:Right:M1
        #Define Boundary_element
        self._DesignParameter['BND_ExtenMet1Layer_Right'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[ ],
                                                                                   )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_PbodyTop','SRF_PbodyContactPhyLen','BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_PbodyBottom','SRF_PbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_ExtenMet1Layer_Right']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] )

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH4('SRF_PbodyRight','SRF_PbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_ExtenMet1Layer_Right']['_XWidth']= tmp3[0][0][0][0]['_Xwidth']

        # Define Sref _XYcoordinate
        self._DesignParameter['BND_ExtenMet1Layer_Right']['_XYCoordinates'] = [[0,0]]


        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['BND_ExtenMet1Layer_Right']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH4('SRF_PbodyTop','SRF_PbodyContactPhyLen','BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_up_right']
                #Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ExtenMet1Layer_Right')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH4('BND_ExtenMet1Layer_Right')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['BND_ExtenMet1Layer_Right']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### Extension:Right:PP
        #Define Boundary_element
        self._DesignParameter['BND_ExtenPPLayer_Right'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[ ],
                                                                                           )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_PbodyTop','SRF_PbodyContactPhyLen','BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_PbodyBottom','SRF_PbodyContactPhyLen','BND_PPLayer')
        self._DesignParameter['BND_ExtenPPLayer_Right']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] )

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH4('SRF_PbodyRight','SRF_PbodyContactPhyLen','BND_PPLayer')
        self._DesignParameter['BND_ExtenPPLayer_Right']['_XWidth']= tmp3[0][0][0][0]['_Xwidth']

        # Define Sref _XYcoordinate
        self._DesignParameter['BND_ExtenPPLayer_Right']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['BND_ExtenPPLayer_Right']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1_1 = self.get_param_KJH4('BND_ExtenPPLayer_Top')
        target_coord = tmp1_1[0][0]['_XY_up_right']
                #Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ExtenPPLayer_Right')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                #Sref coord
        tmp3 = self.get_param_KJH4('BND_ExtenPPLayer_Right')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['BND_ExtenPPLayer_Right']['_XYCoordinates'] = tmpXY


        ## ################################################################################################################################# Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')



## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from TIA_Proj_YCH.Library_and_Engine.Private import MyInfo_YCH
    from TIA_Proj_YCH.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_A50_TIA_Pbodyring_v1'
    cellname = 'A50_TIA_Pbodyring'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

_XlengthIntn		= 7676,
_YlengthIntn		= 1447,
_NumContTop			= 3,
_NumContBottom		= 3,
_NumContLeft		= 3,
_NumContRight		= 3,


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
    LayoutObj = _PbodyRing(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('###############      Sending to FTP Server...      ##################')
    My = MyInfo_YCH.USER(DesignParameters._Technology)
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
    Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()
    print('#############################      Finished      ################################')
    # end of 'main():' ---------------------------------------------------------------------------------------------




