from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_ADC.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

import numpy as np
import copy
import math

from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A07_NbodyContactPhyLen_KJH2

## ########################################################################################################################################################## Class_HEADER
class _NbodyRing_KJH2(StickDiagram_KJH1._StickDiagram_KJH):

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
        _DRCObj = DRC.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']


        ## ################################################################################################################################# Calculation_Start
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

            ## ################################################################################################################### Nbody:Top
        #Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy( A07_NbodyContactPhyLen_KJH2._NbodyContactPhyLen_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length']  		=  _XlengthIntn
        _Caculation_Parameters['_NumCont']  	=  _NumContTop
        _Caculation_Parameters['_Vtc_flag']  	=  False

        #Generate Sref
        self._DesignParameter['SRF_NbodyTop'] = self._SrefElementDeclaration(_DesignObj=A07_NbodyContactPhyLen_KJH2._NbodyContactPhyLen_KJH2( _DesignParameter=None, _Name='{}:SRF_NbodyTop'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['SRF_NbodyTop']['_Reflect'] = [0, 0, 0]
        
        #Define Sref Angle
        self._DesignParameter['SRF_NbodyTop']['_Angle'] = 0

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_NbodyTop']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['SRF_NbodyTop']['_XYCoordinates']=[[0, 0]]


            ## ################################################################################################################### Nbody:Bottom
        #Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy( A07_NbodyContactPhyLen_KJH2._NbodyContactPhyLen_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length']  		=  _XlengthIntn
        _Caculation_Parameters['_NumCont']  	=  _NumContBottom
        _Caculation_Parameters['_Vtc_flag']  	=  False

        #Generate Sref
        self._DesignParameter['SRF_NbodyBottom'] = self._SrefElementDeclaration(_DesignObj=A07_NbodyContactPhyLen_KJH2._NbodyContactPhyLen_KJH2( _DesignParameter=None, _Name='{}:SRF_NbodyBottom'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['SRF_NbodyBottom']['_Reflect'] = [0, 0, 0]
        
        #Define Sref Angle
        self._DesignParameter['SRF_NbodyBottom']['_Angle'] = 0

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_NbodyBottom']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['SRF_NbodyBottom']['_XYCoordinates']=[[0, 0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['SRF_NbodyBottom']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH4('SRF_NbodyTop','SRF_NbodyContactPhyLen','BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_down']
                #Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_NbodyBottom','SRF_NbodyContactPhyLen','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                #Sref coord
        tmp3 = self.get_param_KJH4('SRF_NbodyBottom')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)
        New_Scoord[1] = New_Scoord[1] - _YlengthIntn
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['SRF_NbodyBottom']['_XYCoordinates'] = tmpXY

        
            ## ################################################################################################################### Nbody:Left
        #Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy( A07_NbodyContactPhyLen_KJH2._NbodyContactPhyLen_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length']  		=  _YlengthIntn
        _Caculation_Parameters['_NumCont']  	=  _NumContLeft
        _Caculation_Parameters['_Vtc_flag']  	=  True

        #Generate Sref
        self._DesignParameter['SRF_NbodyLeft'] = self._SrefElementDeclaration(_DesignObj=A07_NbodyContactPhyLen_KJH2._NbodyContactPhyLen_KJH2( _DesignParameter=None, _Name='{}:SRF_NbodyLeft'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['SRF_NbodyLeft']['_Reflect'] = [0, 0, 0]
        
        #Define Sref Angle
        self._DesignParameter['SRF_NbodyLeft']['_Angle'] = 0

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_NbodyLeft']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['SRF_NbodyLeft']['_XYCoordinates']=[[0, 0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['SRF_NbodyLeft']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH4('SRF_NbodyTop','SRF_NbodyContactPhyLen','BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_NbodyLeft','SRF_NbodyContactPhyLen','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_right']
                #Sref coord
        tmp3 = self.get_param_KJH4('SRF_NbodyLeft')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['SRF_NbodyLeft']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### Nbody:Right
        #Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy( A07_NbodyContactPhyLen_KJH2._NbodyContactPhyLen_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length']  		=  _YlengthIntn
        _Caculation_Parameters['_NumCont']  	=  _NumContRight
        _Caculation_Parameters['_Vtc_flag']  	=  True

        #Generate Sref
        self._DesignParameter['SRF_NbodyRight'] = self._SrefElementDeclaration(_DesignObj=A07_NbodyContactPhyLen_KJH2._NbodyContactPhyLen_KJH2( _DesignParameter=None, _Name='{}:SRF_NbodyRight'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['SRF_NbodyRight']['_Reflect'] = [0, 0, 0]
        
        #Define Sref Angle
        self._DesignParameter['SRF_NbodyRight']['_Angle'] = 0

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_NbodyRight']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['SRF_NbodyRight']['_XYCoordinates']=[[0, 0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['SRF_NbodyRight']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH4('SRF_NbodyTop','SRF_NbodyContactPhyLen','BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_down_right']
                #Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_NbodyRight','SRF_NbodyContactPhyLen','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH4('SRF_NbodyRight')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['SRF_NbodyRight']['_XYCoordinates'] = tmpXY
        
            ## ################################################################################################################### Extension:Top
                ## ##################################################################################################### Extension:Top:OD
        #Define Boundary_element
        self._DesignParameter['BND_ExtenODLayer_Top'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_NbodyTop','SRF_NbodyContactPhyLen','BND_ODLayer')
        self._DesignParameter['BND_ExtenODLayer_Top']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH4('SRF_NbodyLeft','SRF_NbodyContactPhyLen','BND_ODLayer')
        tmp3 = self.get_param_KJH4('SRF_NbodyRight','SRF_NbodyContactPhyLen','BND_ODLayer')
        self._DesignParameter['BND_ExtenODLayer_Top']['_XWidth'] = abs( tmp3[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0] )

        #Define XYcoord.
        self._DesignParameter['BND_ExtenODLayer_Top']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['BND_ExtenODLayer_Top']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH4('SRF_NbodyLeft','SRF_NbodyContactPhyLen','BND_ODLayer')
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
        tmp1 = self.get_param_KJH4('SRF_NbodyTop','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_ExtenMet1Layer_Top']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH4('SRF_NbodyLeft','SRF_NbodyContactPhyLen','BND_Met1Layer')
        tmp3 = self.get_param_KJH4('SRF_NbodyRight','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_ExtenMet1Layer_Top']['_XWidth'] = abs( tmp3[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0] )

        #Define XYcoord.
        self._DesignParameter['BND_ExtenMet1Layer_Top']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['BND_ExtenMet1Layer_Top']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH4('SRF_NbodyLeft','SRF_NbodyContactPhyLen','BND_Met1Layer')
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
                ## ##################################################################################################### Extension:Top:NW
        #Define Boundary_element
        self._DesignParameter['BND_ExtenNwell_Top'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['NWELL'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[ ],
                                                                                   )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_NbodyTop','SRF_NbodyContactPhyLen','BND_Nwell')
        self._DesignParameter['BND_ExtenNwell_Top']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH4('SRF_NbodyLeft','SRF_NbodyContactPhyLen','BND_Nwell')
        tmp3 = self.get_param_KJH4('SRF_NbodyRight','SRF_NbodyContactPhyLen','BND_Nwell')
        self._DesignParameter['BND_ExtenNwell_Top']['_XWidth'] = abs( tmp3[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0] )

        #Define XYcoord.
        self._DesignParameter['BND_ExtenNwell_Top']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['BND_ExtenNwell_Top']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #Xcoord
        tmp1_1 = self.get_param_KJH4('SRF_NbodyLeft','SRF_NbodyContactPhyLen','BND_Nwell')
        target_coord = tmp1_1[0][0][0][0]['_XY_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ExtenNwell_Top')
        approaching_coord = tmp2[0][0]['_XY_left']
                #Sref coord
        tmp3 = self.get_param_KJH4('BND_ExtenNwell_Top')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoordx = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)

                #Target_coord
                    #Ycoord
        tmp1_1 = self.get_param_KJH4('SRF_NbodyTop','SRF_NbodyContactPhyLen','BND_Nwell')
        target_coord = tmp1_1[0][0][0][0]['_XY_down']
                #Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ExtenNwell_Top')
        approaching_coord = tmp2[0][0]['_XY_down']
                #Sref coord
        tmp3 = self.get_param_KJH4('BND_ExtenNwell_Top')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoordy = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)

        New_Scoord = [ New_Scoordx[0], New_Scoordy[1] ]

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['BND_ExtenNwell_Top']['_XYCoordinates'] = tmpXY
        
            ## ################################################################################################################### Extension:Bottom
                ## ##################################################################################################### Extension:Bottom:OD
        #Define Boundary_element
        self._DesignParameter['BND_ExtenODLayer_Bottom'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_NbodyBottom','SRF_NbodyContactPhyLen','BND_ODLayer')
        self._DesignParameter['BND_ExtenODLayer_Bottom']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH4('SRF_NbodyLeft','SRF_NbodyContactPhyLen','BND_ODLayer')
        tmp3 = self.get_param_KJH4('SRF_NbodyRight','SRF_NbodyContactPhyLen','BND_ODLayer')
        self._DesignParameter['BND_ExtenODLayer_Bottom']['_XWidth'] = abs( tmp3[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0] )

        #Define XYcoord.
        self._DesignParameter['BND_ExtenODLayer_Bottom']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['BND_ExtenODLayer_Bottom']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH4('SRF_NbodyLeft','SRF_NbodyContactPhyLen','BND_ODLayer')
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
        tmp1 = self.get_param_KJH4('SRF_NbodyBottom','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_ExtenMet1Layer_Bottom']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH4('SRF_NbodyLeft','SRF_NbodyContactPhyLen','BND_Met1Layer')
        tmp3 = self.get_param_KJH4('SRF_NbodyRight','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_ExtenMet1Layer_Bottom']['_XWidth'] = abs( tmp3[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0] )

        #Define XYcoord.
        self._DesignParameter['BND_ExtenMet1Layer_Bottom']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['BND_ExtenMet1Layer_Bottom']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH4('SRF_NbodyLeft','SRF_NbodyContactPhyLen','BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ExtenMet1Layer_Bottom')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH4('BND_ExtenMet1Layer_Bottom')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['BND_ExtenMet1Layer_Bottom']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### Extension:Bottom:NW
        #Define Boundary_element
        self._DesignParameter['BND_ExtenNwell_Bottom'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['NWELL'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_NbodyBottom','SRF_NbodyContactPhyLen','BND_Nwell')
        self._DesignParameter['BND_ExtenNwell_Bottom']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH4('SRF_NbodyLeft','SRF_NbodyContactPhyLen','BND_Nwell')
        tmp3 = self.get_param_KJH4('SRF_NbodyRight','SRF_NbodyContactPhyLen','BND_Nwell')
        self._DesignParameter['BND_ExtenNwell_Bottom']['_XWidth'] = abs( tmp3[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0] )

        #Define XYcoord.
        self._DesignParameter['BND_ExtenNwell_Bottom']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['BND_ExtenNwell_Bottom']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #Xcoord
        tmp1_1 = self.get_param_KJH4('SRF_NbodyLeft','SRF_NbodyContactPhyLen','BND_Nwell')
        target_coord = tmp1_1[0][0][0][0]['_XY_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ExtenNwell_Bottom')
        approaching_coord = tmp2[0][0]['_XY_left']
                #Sref coord
        tmp3 = self.get_param_KJH4('BND_ExtenNwell_Bottom')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoordx = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)

                #Target_coord
                    #Ycoord
        tmp1_1 = self.get_param_KJH4('SRF_NbodyBottom','SRF_NbodyContactPhyLen','BND_Nwell')
        target_coord = tmp1_1[0][0][0][0]['_XY_down']
                #Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ExtenNwell_Bottom')
        approaching_coord = tmp2[0][0]['_XY_down']
                #Sref coord
        tmp3 = self.get_param_KJH4('BND_ExtenNwell_Bottom')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoordy = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)

        New_Scoord = [ New_Scoordx[0], New_Scoordy[1] ]

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['BND_ExtenNwell_Bottom']['_XYCoordinates'] = tmpXY
        
            ## ################################################################################################################### Extension:Left
                ## ##################################################################################################### Extension:Left:OD
        #Define Boundary_element
        self._DesignParameter['BND_ExtenODLayer_Left'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_NbodyTop','SRF_NbodyContactPhyLen','BND_ODLayer')
        tmp2 = self.get_param_KJH4('SRF_NbodyBottom','SRF_NbodyContactPhyLen','BND_ODLayer')
        self._DesignParameter['BND_ExtenODLayer_Left']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] )

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH4('SRF_NbodyLeft','SRF_NbodyContactPhyLen','BND_ODLayer')
        self._DesignParameter['BND_ExtenODLayer_Left']['_XWidth'] = tmp3[0][0][0][0]['_Xwidth']

        #Define XYcoord.
        self._DesignParameter['BND_ExtenODLayer_Left']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['BND_ExtenODLayer_Left']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH4('SRF_NbodyTop','SRF_NbodyContactPhyLen','BND_ODLayer')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ExtenODLayer_Left')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                #Sref coord
        tmp3 = self.get_param_KJH4('BND_ExtenODLayer_Left')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)

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
        tmp1 = self.get_param_KJH4('SRF_NbodyTop','SRF_NbodyContactPhyLen','BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_NbodyBottom','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_ExtenMet1Layer_Left']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] )

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH4('SRF_NbodyLeft','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_ExtenMet1Layer_Left']['_XWidth'] = tmp3[0][0][0][0]['_Xwidth']

        #Define XYcoord.
        self._DesignParameter['BND_ExtenMet1Layer_Left']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['BND_ExtenMet1Layer_Left']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH4('SRF_NbodyTop','SRF_NbodyContactPhyLen','BND_Met1Layer')
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

                ## ##################################################################################################### Extension:Left:NW
        #Define Boundary_element
        self._DesignParameter['BND_ExtenNwell_Left'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['NWELL'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_NbodyTop','SRF_NbodyContactPhyLen','BND_Nwell')
        tmp2 = self.get_param_KJH4('SRF_NbodyBottom','SRF_NbodyContactPhyLen','BND_Nwell')
        self._DesignParameter['BND_ExtenNwell_Left']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] )

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH4('SRF_NbodyLeft','SRF_NbodyContactPhyLen','BND_Nwell')
        self._DesignParameter['BND_ExtenNwell_Left']['_XWidth'] = tmp3[0][0][0][0]['_Xwidth']

        #Define XYcoord.
        self._DesignParameter['BND_ExtenNwell_Left']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['BND_ExtenNwell_Left']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #Xcoord
        tmp1_1 = self.get_param_KJH4('BND_ExtenNwell_Top')
        target_coord = tmp1_1[0][0]['_XY_up_left']

                #Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ExtenNwell_Left')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH4('BND_ExtenNwell_Left')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['BND_ExtenNwell_Left']['_XYCoordinates'] = tmpXY
        
            ## ################################################################################################################### Extension:Right
                ## ##################################################################################################### Extension:Right:OD
        #Define Boundary_element
        self._DesignParameter['BND_ExtenODLayer_Right'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_NbodyTop','SRF_NbodyContactPhyLen','BND_ODLayer')
        tmp2 = self.get_param_KJH4('SRF_NbodyBottom','SRF_NbodyContactPhyLen','BND_ODLayer')
        self._DesignParameter['BND_ExtenODLayer_Right']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] )

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH4('SRF_NbodyRight','SRF_NbodyContactPhyLen','BND_ODLayer')
        self._DesignParameter['BND_ExtenODLayer_Right']['_XWidth'] = tmp3[0][0][0][0]['_Xwidth']

        #Define XYcoord.
        self._DesignParameter['BND_ExtenODLayer_Right']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['BND_ExtenODLayer_Right']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH4('SRF_NbodyTop','SRF_NbodyContactPhyLen','BND_ODLayer')
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
        tmp1 = self.get_param_KJH4('SRF_NbodyTop','SRF_NbodyContactPhyLen','BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_NbodyBottom','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_ExtenMet1Layer_Right']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] )

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH4('SRF_NbodyRight','SRF_NbodyContactPhyLen','BND_Met1Layer')
        self._DesignParameter['BND_ExtenMet1Layer_Right']['_XWidth'] = tmp3[0][0][0][0]['_Xwidth']

        #Define XYcoord.
        self._DesignParameter['BND_ExtenMet1Layer_Right']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['BND_ExtenMet1Layer_Right']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH4('SRF_NbodyTop','SRF_NbodyContactPhyLen','BND_Met1Layer')
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
                ## ##################################################################################################### Extension:Right:NW
        #Define Boundary_element
        self._DesignParameter['BND_ExtenNwell_Right'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['NWELL'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_NbodyTop','SRF_NbodyContactPhyLen','BND_Nwell')
        tmp2 = self.get_param_KJH4('SRF_NbodyBottom','SRF_NbodyContactPhyLen','BND_Nwell')
        self._DesignParameter['BND_ExtenNwell_Right']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] )

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH4('SRF_NbodyLeft','SRF_NbodyContactPhyLen','BND_Nwell')
        self._DesignParameter['BND_ExtenNwell_Right']['_XWidth'] = tmp3[0][0][0][0]['_Xwidth']

        #Define XYcoord.
        self._DesignParameter['BND_ExtenNwell_Right']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['BND_ExtenNwell_Right']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #Xcoord
        tmp1_1 = self.get_param_KJH4('BND_ExtenNwell_Top')
        target_coord = tmp1_1[0][0]['_XY_up_right']

                #Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ExtenNwell_Right')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                #Sref coord
        tmp3 = self.get_param_KJH4('BND_ExtenNwell_Right')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['BND_ExtenNwell_Right']['_XYCoordinates'] = tmpXY
        
        
        ## ################################################################################################################################# Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')



## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_ADC_A_building_block_KJH'
    cellname = 'A09_NbodyRing_KJH2_97'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

_XlengthIntn		= 4534,
_YlengthIntn		= 2119,
_NumContTop			= 2,
_NumContBottom		= 2,
_NumContLeft		= 2,
_NumContRight		= 2,


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
    LayoutObj = _NbodyRing_KJH2(_DesignParameter=None, _Name=cellname)
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
    # end of 'main():' ---------------------------------------------------------------------------------------------




