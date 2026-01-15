from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_ADC.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

import numpy as np
import copy
import math
#from SthPack import CoordCalc

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
                                            _GDSFile=self._GDSObjDeclaration(_GDSFile=None),_XYcoordAsCent=dict(_XYcoordAsCent=1),
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
        _XYCoordinateOfOPRES = [[0,0]]


            ## ################################################################################################################### OPLayer
        #Define Boundary_element
        self._DesignParameter['_OPLayer'] = self._BoundaryElementDeclaration(
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
        self._DesignParameter['_OPLayer']['_YWidth'] = _ResLength

        #Define Boundary_element _XWidth
        self._DesignParameter['_OPLayer']['_XWidth'] = _ResWidth + _DRCObj._OPlayeroverPoly * 2

        #Define Boundary_element _XYCoordinates
        self._DesignParameter['_OPLayer']['_XYCoordinates'] = _XYCoordinateOfOPRES

            ## ################################################################################################################### POLY Layer
        #Define Boundary_element
        self._DesignParameter['_POLayer'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['POLY'][1], 
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Define Boundary_element _YWidth
        self._DesignParameter['_POLayer']['_YWidth'] = _ResLength + _DRCObj._PolyoverOPlayer * 2

        #Define Boundary_element _XWidth
        self._DesignParameter['_POLayer']['_XWidth'] = _ResWidth

        #Define Boundary_element _XYCoordinates
        tmp = self.get_param_KJH3('_OPLayer')
        self._DesignParameter['_POLayer']['_XYCoordinates'] =  [tmp[0][0]['_XY_cent'] ]

            ## ################################################################################################################### PRES Layer
        #Define Boundary_element
        self._DesignParameter['_PRESLayer'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['PRES'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['PRES'][1], 
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Define Boundary_element _YWidth
        tmp = self.get_param_KJH3('_POLayer')
        self._DesignParameter['_PRESLayer']['_YWidth'] = tmp[0][0]['_Ywidth'] + _DRCObj._PRESlayeroverPoly * 2

        #Define Boundary_element _XWidth
        self._DesignParameter['_PRESLayer']['_XWidth'] = _ResWidth + _DRCObj._PRESlayeroverPoly * 2

        #Define Boundary_element _XYCoordinates
        tmp = self.get_param_KJH3('_OPLayer')
        self._DesignParameter['_PRESLayer']['_XYCoordinates'] =  [tmp[0][0]['_XY_cent']] 

            ## ################################################################################################################### PIMP Layer
        #Define Boundary_element
        self._DesignParameter['_PPLayer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                               )

        #Define Boundary_element _YWidth
        tmp = self.get_param_KJH3('_PRESLayer')
        self._DesignParameter['_PPLayer']['_YWidth'] = tmp[0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp = self.get_param_KJH3('_PRESLayer')
        self._DesignParameter['_PPLayer']['_XWidth'] = tmp[0][0]['_Xwidth']

        #Define Boundary_element _XYCoordinates
        tmp = self.get_param_KJH3('_OPLayer')
        self._DesignParameter['_PPLayer']['_XYCoordinates'] =  [tmp[0][0]['_XY_cent']] 

            ## ################################################################################################################### CONT Layer
        #Define Boundary_element
        self._DesignParameter['_COLayer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['CONT'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['CONT'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                               )

        #Define Boundary_element _YWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth

        #Define Boundary_element _XWidth
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth
        
        #Define Minsnapspacing
        MinSnapSpacing = _DRCObj._MinSnapSpacing

        #Define Boundary_element _XYCoordinates

            #Number of Contact
                #MaxnNum of Contact
        _CONUMXmax = int((self._DesignParameter['_POLayer']['_XWidth'] - _DRCObj._CoMinEnclosureByPO2 * 2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 1
        _CONUMYmax = int((int((self._DesignParameter['_POLayer']['_YWidth'] - self._DesignParameter['_OPLayer']['_YWidth'] - 2*_DRCObj._CoMinSpace2OP - 2*_DRCObj._CoMinEnclosureByPO2) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)) + 1) // 2)

                #Default num of contact
        if _CONUMX == None :
            _CONUMX = _CONUMXmax
        if _CONUMY == None :
            _CONUMY = _CONUMYmax

                #If _CONUMY > 1 then, _CONUMX is defined
        if _CONUMY > 1 :
            _CONUMX = int((self._DesignParameter['_POLayer']['_XWidth'] - _DRCObj._CoMinEnclosureByPO2 * 2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)) + 1

                #Not implemented
        if _CONUMX > _CONUMXmax or _CONUMY > _CONUMYmax :
            raise NotImplementedError

            #Calcuate Coordinates
                #If _CONUMY == 1
        tmp = []
        if _CONUMY == 1 :
            if _ResWidth % 2 == 0 and _ResLength % 2 == 0 :
                for i in range (0, _CONUMX) :
                    for j in range (0, _CONUMY) :
                        if (_CONUMX % 2 == 0) :
                            tmp.append([_XYCoordinateOfOPRES[0][0]- (_CONUMX//2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                        _XYCoordinateOfOPRES[0][1]- (self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                            tmp.append([_XYCoordinateOfOPRES[0][0]- (_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                        _XYCoordinateOfOPRES[0][1]+ (self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                        else :
                            tmp.append([_XYCoordinateOfOPRES[0][0] - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                        _XYCoordinateOfOPRES[0][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                            tmp.append([_XYCoordinateOfOPRES[0][0] - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                        _XYCoordinateOfOPRES[0][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])

            elif _ResWidth % 2 == 0 and _ResLength % 2 == 1 :
                for i in range (0, _CONUMX) :
                    for j in range (0, _CONUMY) :
                        if (_CONUMX % 2 == 0) :
                            tmp.append([_XYCoordinateOfOPRES[0][0]-(_CONUMX//2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                        _XYCoordinateOfOPRES[0][1] - MinSnapSpacing/2.0 -(self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                            tmp.append([_XYCoordinateOfOPRES[0][0]-(_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                        _XYCoordinateOfOPRES[0][1] + MinSnapSpacing/2.0 +(self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                        else :
                            tmp.append([_XYCoordinateOfOPRES[0][0] - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                        _XYCoordinateOfOPRES[0][1] - MinSnapSpacing/2.0 - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                            tmp.append([_XYCoordinateOfOPRES[0][0] - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                        _XYCoordinateOfOPRES[0][1] + MinSnapSpacing/2.0 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
            
            elif _ResWidth % 2 == 1 and _ResLength % 2 == 0 :
                for i in range (0, _CONUMX) :
                    for j in range (0, _CONUMY) :
                        if (_CONUMX % 2 == 0) :
                            tmp.append([_XYCoordinateOfOPRES[0][0] + MinSnapSpacing/2.0 -(_CONUMX//2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                        _XYCoordinateOfOPRES[0][1]-(self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                            tmp.append([_XYCoordinateOfOPRES[0][0] + MinSnapSpacing/2.0 -(_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                        _XYCoordinateOfOPRES[0][1]+(self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                        else :
                            tmp.append([_XYCoordinateOfOPRES[0][0] + MinSnapSpacing/2.0 - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                        _XYCoordinateOfOPRES[0][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                            tmp.append([_XYCoordinateOfOPRES[0][0] + MinSnapSpacing/2.0 - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                        _XYCoordinateOfOPRES[0][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
            
            elif _ResWidth % 2 == 1 and _ResLength % 2 == 1 :
                for i in range (0, _CONUMX) :
                    for j in range (0, _CONUMY) :
                        if (_CONUMX % 2 == 0) :
                            tmp.append([_XYCoordinateOfOPRES[0][0] + MinSnapSpacing/2.0 - (_CONUMX//2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                        _XYCoordinateOfOPRES[0][1] - self.CeilMinSnapSpacing((self._DesignParameter['_OPLayer']['_YWidth']/2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth), MinSnapSpacing / 2) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                            tmp.append([_XYCoordinateOfOPRES[0][0] + MinSnapSpacing/2.0 - (_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                        _XYCoordinateOfOPRES[0][1] + self.CeilMinSnapSpacing((self._DesignParameter['_OPLayer']['_YWidth']/2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth), MinSnapSpacing / 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                        else :
                            tmp.append([_XYCoordinateOfOPRES[0][0] + MinSnapSpacing/2.0 - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                        _XYCoordinateOfOPRES[0][1] - self.CeilMinSnapSpacing((self._DesignParameter['_OPLayer']['_YWidth'] / 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth), MinSnapSpacing / 2) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                            tmp.append([_XYCoordinateOfOPRES[0][0] + MinSnapSpacing/2.0 - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                        _XYCoordinateOfOPRES[0][1] + self.CeilMinSnapSpacing((self._DesignParameter['_OPLayer']['_YWidth'] / 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth), MinSnapSpacing / 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                #If _CONUMY != 1
        else :
            if _ResWidth % 2 == 0 and _ResLength % 2 == 0 :
                for i in range (0, _CONUMX) :
                    for j in range (0, _CONUMY) :
                        if (_CONUMX % 2 == 0) :
                            tmp.append([_XYCoordinateOfOPRES[0][0]-(_CONUMX//2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                        _XYCoordinateOfOPRES[0][1]-(self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                            tmp.append([_XYCoordinateOfOPRES[0][0]-(_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                        _XYCoordinateOfOPRES[0][1]+(self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                        else :
                            tmp.append([_XYCoordinateOfOPRES[0][0] - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                        _XYCoordinateOfOPRES[0][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                            tmp.append([_XYCoordinateOfOPRES[0][0] - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                        _XYCoordinateOfOPRES[0][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])

            elif _ResWidth % 2 == 0 and _ResLength % 2 == 1 :
                for i in range (0, _CONUMX) :
                    for j in range (0, _CONUMY) :
                        if (_CONUMX % 2 == 0) :
                            tmp.append([_XYCoordinateOfOPRES[0][0] - (_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                        _XYCoordinateOfOPRES[0][1] - 0.5 -(self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                            tmp.append([_XYCoordinateOfOPRES[0][0] - (_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                        _XYCoordinateOfOPRES[0][1] + 0.5 +(self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                        else :
                            tmp.append([_XYCoordinateOfOPRES[0][0] - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                        _XYCoordinateOfOPRES[0][1] - 0.5 - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                            tmp.append([_XYCoordinateOfOPRES[0][0] - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                        _XYCoordinateOfOPRES[0][1] + 0.5 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
            
            elif _ResWidth % 2 == 1 and _ResLength % 2 == 0 :
                for i in range (0, _CONUMX) :
                    for j in range (0, _CONUMY) :
                        if (_CONUMX % 2 == 0) :
                            tmp.append([_XYCoordinateOfOPRES[0][0] + 0.5 -(_CONUMX//2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                        _XYCoordinateOfOPRES[0][1]-(self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                            tmp.append([_XYCoordinateOfOPRES[0][0] + 0.5-(_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                        _XYCoordinateOfOPRES[0][1]+(self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                        else :
                            tmp.append([_XYCoordinateOfOPRES[0][0] + 0.5 - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                        _XYCoordinateOfOPRES[0][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                            tmp.append([_XYCoordinateOfOPRES[0][0] + 0.5 - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                        _XYCoordinateOfOPRES[0][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
            
            elif _ResWidth % 2 == 1 and _ResLength % 2 == 1 :
                for i in range (0, _CONUMX) :
                    for j in range (0, _CONUMY) :
                        if (_CONUMX % 2 == 0) :
                            tmp.append([_XYCoordinateOfOPRES[0][0] + 0.5-(_CONUMX//2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                        _XYCoordinateOfOPRES[0][1] - 0.5 -(self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                            tmp.append([_XYCoordinateOfOPRES[0][0] + 0.5 -(_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                        _XYCoordinateOfOPRES[0][1] + 0.5 +(self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                        else :
                            tmp.append([_XYCoordinateOfOPRES[0][0] + 0.5 - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                        _XYCoordinateOfOPRES[0][1] - 0.5 - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                            tmp.append([_XYCoordinateOfOPRES[0][0] + 0.5 - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                        _XYCoordinateOfOPRES[0][1] + 0.5 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])

        #Define Coordinates
        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmp

        del tmp

            ## ################################################################################################################### Port1 Routing Coordinates Calculation
        #Define Boundary_element
        self._DesignParameter['_XYCoordinatePort1Routing'] = dict(
                                                                        _DesignParametertype=7,
                                                                        _XYCoordinates=[ ],
                                                                       )
        tmp = []
        # tmp.append([_XYCoordinateOfOPRES[0][0], _XYCoordinateOfOPRES[0][1] - (self._DesignParameter['_OPLayer']['_YWidth']//2 + _DRCObj._CoMinSpace2OP +
        #                                                                       (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)//2 + _DRCObj._CoMinWidth//2)])

        if _CONUMY == 1 :
            if _ResWidth % 2 == 0 and _ResLength % 2 == 0 :
                tmp.append([_XYCoordinateOfOPRES[0][0], _XYCoordinateOfOPRES[0][1] - (self._DesignParameter['_OPLayer']['_YWidth']//2 + _DRCObj._CoMinSpace2OP +
                                                                                (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)//2 + _DRCObj._CoMinWidth//2)])
                                                                                
            if _ResWidth % 2 == 0 and _ResLength % 2 == 1 :
                tmp.append([_XYCoordinateOfOPRES[0][0], _XYCoordinateOfOPRES[0][1] - 0.5 - (self._DesignParameter['_OPLayer']['_YWidth']//2 + _DRCObj._CoMinSpace2OP +
                                                                                (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)//2 + _DRCObj._CoMinWidth//2)])
            
            if _ResWidth % 2 == 1 and _ResLength % 2 == 0 :
                tmp.append([_XYCoordinateOfOPRES[0][0], _XYCoordinateOfOPRES[0][1] - (self._DesignParameter['_OPLayer']['_YWidth']//2 + _DRCObj._CoMinSpace2OP +
                                                                                (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)//2 + _DRCObj._CoMinWidth//2)])

            if _ResWidth % 2 == 1 and _ResLength % 2 == 1 :
                tmp.append([_XYCoordinateOfOPRES[0][0], _XYCoordinateOfOPRES[0][1] - 0.5 - (self._DesignParameter['_OPLayer']['_YWidth']//2 + _DRCObj._CoMinSpace2OP +
                                                                                (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)//2 + _DRCObj._CoMinWidth//2)])
        
        else :
            if _ResWidth % 2 == 0 and _ResLength % 2 == 0 :
                tmp.append([_XYCoordinateOfOPRES[0][0], _XYCoordinateOfOPRES[0][1] - (self._DesignParameter['_OPLayer']['_YWidth']//2 + _DRCObj._CoMinSpace2OP +
                                                                              (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)//2 + _DRCObj._CoMinWidth//2)])
                                                                              
            if _ResWidth % 2 == 0 and _ResLength % 2 == 1 :
                tmp.append([_XYCoordinateOfOPRES[0][0], _XYCoordinateOfOPRES[0][1] - 0.5 - (self._DesignParameter['_OPLayer']['_YWidth']//2 + _DRCObj._CoMinSpace2OP +
                                                                                (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)//2 + _DRCObj._CoMinWidth//2)])
            
            if _ResWidth % 2 == 1 and _ResLength % 2 == 0 :
                tmp.append([_XYCoordinateOfOPRES[0][0], _XYCoordinateOfOPRES[0][1] - (self._DesignParameter['_OPLayer']['_YWidth']//2 + _DRCObj._CoMinSpace2OP +
                                                                                (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)//2 + _DRCObj._CoMinWidth//2)])

            if _ResWidth % 2 == 1 and _ResLength % 2 == 1 :
                tmp.append([_XYCoordinateOfOPRES[0][0], _XYCoordinateOfOPRES[0][1] - 0.5 - (self._DesignParameter['_OPLayer']['_YWidth']//2 + _DRCObj._CoMinSpace2OP +
                                                                                (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)//2 + _DRCObj._CoMinWidth//2)])
        
        
        self._DesignParameter['_XYCoordinatePort1Routing']['_XYCoordinates'] = tmp
        del tmp

        # Downward

            ## ################################################################################################################### Port2 Routing Coordinates Calculation
        #Define Boundary_element
        self._DesignParameter['_XYCoordinatePort2Routing'] = dict(
                                                                        _DesignParametertype=7,
                                                                        _XYCoordinates=[ ],
                                                                       )

        tmp = []
        # tmp.append([_XYCoordinateOfOPRES[0][0], _XYCoordinateOfOPRES[0][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
        #             (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2 + _DRCObj._CoMinWidth // 2)])
        if _CONUMY == 1 :
            if _ResWidth % 2 == 0 and _ResLength % 2 == 0 :
                tmp.append([_XYCoordinateOfOPRES[0][0], _XYCoordinateOfOPRES[0][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                        (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2 + _DRCObj._CoMinWidth // 2)])

            if _ResWidth % 2 == 1 and _ResLength % 2 == 0 :
                tmp.append([_XYCoordinateOfOPRES[0][0], _XYCoordinateOfOPRES[0][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                        (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2 + _DRCObj._CoMinWidth // 2)])

            if _ResWidth % 2 == 0 and _ResLength % 2 == 1 :
                tmp.append([_XYCoordinateOfOPRES[0][0], _XYCoordinateOfOPRES[0][1] + 0.5 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                        (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2 + _DRCObj._CoMinWidth // 2)])

            if _ResWidth % 2 == 1 and _ResLength % 2 == 1 :
                tmp.append([_XYCoordinateOfOPRES[0][0] , _XYCoordinateOfOPRES[0][1] + 0.5 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                        (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2 + _DRCObj._CoMinWidth // 2)])
        
        else :
            if _ResWidth % 2 == 0 and _ResLength % 2 == 0 :
                tmp.append([_XYCoordinateOfOPRES[0][0], _XYCoordinateOfOPRES[0][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                        (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + _DRCObj._CoMinWidth // 2)])

            if _ResWidth % 2 == 1 and _ResLength % 2 == 0 :
                tmp.append([_XYCoordinateOfOPRES[0][0], _XYCoordinateOfOPRES[0][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                        (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + _DRCObj._CoMinWidth // 2)])

            if _ResWidth % 2 == 0 and _ResLength % 2 == 1 :
                tmp.append([_XYCoordinateOfOPRES[0][0], _XYCoordinateOfOPRES[0][1] + 0.5 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                        (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + _DRCObj._CoMinWidth // 2)])

            if _ResWidth % 2 == 1 and _ResLength % 2 == 1 :
                tmp.append([_XYCoordinateOfOPRES[0][0] , _XYCoordinateOfOPRES[0][1] + 0.5 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                        (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + _DRCObj._CoMinWidth // 2)])
        
        self._DesignParameter['_XYCoordinatePort2Routing']['_XYCoordinates'] = tmp
        del tmp

            ## ################################################################################################################### Metal1 Layer Calculation
        #Define Boundary_element
        self._DesignParameter['_Met1Layer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                               )

        #If _CONUMY == 1 :
        if _CONUMY == 1 :
            #Define Boundary_element _XWidth
            self._DesignParameter['_Met1Layer']['_XWidth'] = (_CONUMX - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO3 * 2
            #Define Boundary_element _YWidth
            self._DesignParameter['_Met1Layer']['_YWidth'] = (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO3 * 2
            #Define Boundary_element XYCoordinate
            self._DesignParameter['_Met1Layer']['_XYCoordinates'] = [self._DesignParameter['_XYCoordinatePort1Routing']['_XYCoordinates'][0], self._DesignParameter['_XYCoordinatePort2Routing']['_XYCoordinates'][0]]

        #If _CONUMY != 1 :
        else :
            #Define Boundary_element _XWidth
            self._DesignParameter['_Met1Layer']['_XWidth'] = (_CONUMX - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO3 * 2
            #Define Boundary_element _YWidth
            self._DesignParameter['_Met1Layer']['_YWidth'] = (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO3 * 2
            #Define Boundary_element XYCoordinate
            self._DesignParameter['_Met1Layer']['_XYCoordinates'] = [self._DesignParameter['_XYCoordinatePort1Routing']['_XYCoordinates'][0], self._DesignParameter['_XYCoordinatePort2Routing']['_XYCoordinates'][0]]



        ## ################################################################################################################################# Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')

## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_RcdacSar_A00_BasicBuildingBlock_1'
    cellname = 'A15_PolyRes_KJH_86'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

_ResWidth	=	5000,
_ResLength	=	500,
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
    Checker.lib_deletion()
    Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()
    print('#############################      Finished      ################################')
    # end of 'main():' ---------------------------------------------------------------------------------------------




